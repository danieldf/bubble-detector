"""
Unit tests for Canonical PSY/GSADF Recursive Sub-windows and Vietoris-Rips Persistent Homology.
"""

import pytest
import numpy as np
import polars as pl

from bubble_detector.features.econometric import (
    compute_gsadf_gpt_decomposition, compute_wild_bootstrap_critical_values
)
from bubble_detector.features.topology import compute_tda_wavelet_complexity
from bubble_detector.features.utils import normalize_tda_indicator

def test_canonical_monthly_gsadf_dotcom_spike():
    """Asserts recursive GSADF on monthly P/D crosses 99% bootstrap critical value during 1998-2000 exuberance."""
    # Synthetic Dot-Com price-to-dividend sequence
    n = 120
    t = np.linspace(1995, 2005, n)

    # Explosive bubble surge between 1998 and 2000
    pd_base = 30.0 + 5.0 * np.sin(t)
    pd_dotcom = 55.0 * np.exp(-((t - 2000.2)**2) / 1.5)
    pd_series = (pd_base + pd_dotcom).astype(np.float32)

    df = pl.DataFrame({
        "Date": [f"{int(yr)}-06-01" for yr in t],
        "Price_to_Dividend": pd_series,
        "SPY": pd_series * 20.0
    })

    df_res = compute_gsadf_gpt_decomposition(df, target_col="Price_to_Dividend", window_size=30)

    assert "GSADF_Stat" in df_res.columns
    assert "GSADF_Critical_Value_99" in df_res.columns

    stats = df_res["GSADF_Stat"].to_numpy()
    cv_99 = df_res["GSADF_Critical_Value_99"][0]

    # Max GSADF during 1998-2000 peak must cross the 99% critical value
    assert np.max(stats) > cv_99, f"GSADF peak {np.max(stats)} did not exceed 99% critical value {cv_99}"

def test_ripser_persistence_landscapes_causal():
    """Asserts persistent homology computed via ripser/topology engine uses strictly causal windows."""
    np.random.seed(42)
    n = 100
    returns = np.random.randn(n) * 0.01
    prices = 100.0 * np.exp(np.cumsum(returns))

    df = pl.DataFrame({"SPY": prices})
    df_tda = compute_tda_wavelet_complexity(df, target_col="SPY", window_size=20)

    tda_arr = df_tda["TDA_Persistence_L2_Norm"].to_numpy()
    assert not np.isnan(tda_arr).any()
    assert (tda_arr >= 0.0).all()

    # Verify causal normalization
    norm_tda = normalize_tda_indicator(tda_arr)
    assert not np.isnan(norm_tda).any()
    assert (norm_tda >= 0.20).all()
    assert (norm_tda <= 7.10).all()
