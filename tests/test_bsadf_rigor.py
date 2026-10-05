"""
Unit tests for Econometric Rigor: Canonical PSY (2015) Recursive BSADF & GPT Decomposition.
"""

import pytest
import numpy as np
import polars as pl
import pandas as pd

from bubble_detector.features.econometric import (
    calculate_adf_stat,
    compute_gsadf_gpt_decomposition,
    compute_wild_bootstrap_critical_values
)


def test_adf_stat_explosive_vs_stationary():
    """
    Asserts right-tailed ADF t-statistic is strongly positive for explosive series (gamma > 0)
    and negative/zero for stationary mean-reverting series.
    """
    np.random.seed(42)
    n = 60

    # 1. Explosive series: log-prices y_t = 1.04 * y_{t-1} + noise
    y_exp = np.zeros(n)
    y_exp[0] = 1.0
    for t in range(1, n):
        y_exp[t] = 1.04 * y_exp[t-1] + np.random.randn() * 0.01
    exp_series = np.exp(y_exp)

    t_stat_exp = calculate_adf_stat(exp_series)
    assert t_stat_exp > 2.0, f"Expected explosive t-stat > 2.0, got {t_stat_exp}"

    # 2. Stationary series: y_t = 0.5 * y_{t-1} + noise
    stat_series = np.zeros(n)
    stat_series[0] = 10.0
    for t in range(1, n):
        stat_series[t] = 0.5 * stat_series[t-1] + 5.0 + np.random.randn() * 0.5

    t_stat_stat = calculate_adf_stat(stat_series)
    assert t_stat_stat < 0.5, f"Expected non-explosive t-stat < 0.5, got {t_stat_stat}"


def test_adf_lag_selection_k0_vs_k1():
    """
    Asserts calculate_adf_stat properly handles explicit lag orders (k=0, k=1)
    and automatic AIC selection correctly selects k=1 when serial correlation is present.
    """
    np.random.seed(123)
    p = np.exp(np.cumsum(np.random.randn(50) * 0.02) + 4.0)

    stat_auto = calculate_adf_stat(p, lag_order=None)
    stat_k0 = calculate_adf_stat(p, lag_order=0)
    stat_k1 = calculate_adf_stat(p, lag_order=1)

    assert not np.isnan(stat_auto)
    assert not np.isnan(stat_k0)
    assert not np.isnan(stat_k1)
    assert np.isfinite(stat_auto)

    # Autocorrelated differences: dy_t = 0.45 * dy_{t-1} + eps_t
    np.random.seed(42)
    n = 45
    eps = np.random.randn(n) * 0.01
    dy = np.zeros(n)
    for t in range(1, n):
        dy[t] = 0.45 * dy[t-1] + eps[t]
    y_ar1 = np.cumsum(dy) + 4.0
    p_ar1 = np.exp(y_ar1)

    stat_ar_auto = calculate_adf_stat(p_ar1, lag_order=None)
    stat_ar_k1 = calculate_adf_stat(p_ar1, lag_order=1)
    # When significant serial correlation is present, AIC selects k=1
    assert np.isclose(stat_ar_auto, stat_ar_k1), (
        f"AIC should select k=1 for AR(1) differences, got {stat_ar_auto} vs k1={stat_ar_k1}"
    )


def test_recursive_backward_supremum_grid():
    """
    Asserts compute_gsadf_gpt_decomposition performs backward supremum across
    the window grid, populating GSADF_Stat, BSADF_Stat, BSADF_90th_Percentile,
    and critical values.
    """
    n = 150
    t = np.linspace(1995, 2005, n)
    # Explosive spike at index 80-100
    base = 100.0 + 10.0 * np.sin(t)
    spike = 80.0 * np.exp(-((np.arange(n) - 90) ** 2) / 30.0)
    prices = (base + spike).astype(np.float32)

    df = pl.DataFrame({
        "Date": [f"20{int(i/10):02d}-01-01" for i in range(n)],
        "SPY": prices,
        "XLK": prices * 1.2
    })

    res = compute_gsadf_gpt_decomposition(df, target_col="SPY", window_size=40, min_window=15)

    assert "GSADF_Stat" in res.columns
    assert "BSADF_Stat" in res.columns
    assert "BSADF_90th_Percentile" in res.columns
    assert "GSADF_GPT_Adjusted" in res.columns
    assert "GSADF_Critical_Value_95" in res.columns
    assert "GSADF_Critical_Value_99" in res.columns

    bsadf = res["BSADF_Stat"].to_numpy()
    assert not np.isnan(bsadf).any()
    assert (bsadf >= 0.0).all()

    # The peak of the explosive episode must cross the 95% critical value
    cv95 = res["GSADF_Critical_Value_95"][0]
    assert np.max(bsadf) > cv95, f"Peak BSADF {np.max(bsadf)} did not exceed CV 95% ({cv95})"

    # BSADF_90th_Percentile must be strictly positive and finite
    p90 = res["BSADF_90th_Percentile"].to_numpy()
    assert not np.isnan(p90).any()
    assert (p90 >= 0.0).all()


def test_wild_bootstrap_critical_value_bounds():
    """Verifies Rademacher wild bootstrap critical values remain within empirical bounds."""
    cv95, cv99 = compute_wild_bootstrap_critical_values(n_obs=50, n_boot=50)
    assert cv95 >= 1.45
    assert cv99 >= 2.05
    assert cv99 > cv95
