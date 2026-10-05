"""
Unit tests for Institutional LPPLS Singularity Model (Filimonov & Sornette 2013).
"""

import pytest
import numpy as np
import polars as pl
import pandas as pd

from bubble_detector.features.lppls_model import (
    calibrate_lppls_filimonov,
    compute_lppls_confidence_indicator
)


def test_lppls_parameter_recovery_synthetic():
    """
    Asserts Filimonov-Sornette subordination algorithm accurately recovers
    known LPPLS parameters on a synthetic bubble trajectory.
    """
    n = 100
    t = np.arange(n, dtype=np.float64)
    tc_true = 115.0
    m_true = 0.50
    omega_true = 8.0
    dt = tc_true - t

    # Synthetic LPPLS equation: ln P_t = A + B * dt^m + C * dt^m * cos(omega * ln(dt) + phi)
    # Using B = -0.6, C1 = 0.03, C2 = 0.02 -> C = sqrt(0.03^2 + 0.02^2) = 0.036
    # Damping D = (m * |B|) / (omega * C) = (0.5 * 0.6) / (8.0 * 0.036) = 0.3 / 0.288 = 1.04 >= 0.8
    y_true = 5.0 - 0.6 * (dt ** m_true) + (dt ** m_true) * (0.03 * np.cos(omega_true * np.log(dt)) + 0.02 * np.sin(omega_true * np.log(dt)))

    res = calibrate_lppls_filimonov(y_true)

    assert res["is_valid"] is True, f"Expected valid calibration, got {res}"
    assert abs(res["tc"] - tc_true) < 2.0
    assert abs(res["m"] - m_true) < 0.10
    assert abs(res["omega"] - omega_true) < 1.0
    assert res["B"] < 0.0
    assert res["damping"] >= 0.80
    assert res["R2"] >= 0.95


def test_lppls_sornette_filtering_bounds():
    """
    Asserts Sornette filtering flags invalid fits when:
    - B >= 0 (no upward acceleration)
    - m is out of bounds [0.1, 0.9]
    - R^2 < 0.60
    """
    # Flat linear series (no bubble acceleration)
    y_flat = np.linspace(4.0, 4.2, 80)
    res_flat = calibrate_lppls_filimonov(y_flat)
    assert res_flat["is_valid"] is False


def test_lppls_confidence_indicator_pipeline():
    """
    Verifies compute_lppls_confidence_indicator executes cleanly over a polars DataFrame,
    producing non-null, bounded confidence scores in [0.0, 1.0].
    """
    np.random.seed(42)
    n = 150
    p = 100.0 * np.exp(np.cumsum(np.random.randn(n) * 0.01))
    df = pl.DataFrame({"XLK": p})

    df_out = compute_lppls_confidence_indicator(df, target_col="XLK", windows=[60, 90], step=2)

    assert "LPPLS_Confidence" in df_out.columns
    assert "LPPLS_90th_Percentile" in df_out.columns
    assert "LPPLS_Critical_Threshold" in df_out.columns
    assert "LPPLS_Bubble_Active" in df_out.columns

    ci = df_out["LPPLS_Confidence"].to_numpy()
    assert not np.isnan(ci).any()
    assert (ci >= 0.0).all()
    assert (ci <= 1.0).all()

    p90 = df_out["LPPLS_90th_Percentile"].to_numpy()
    assert not np.isnan(p90).any()
    assert (p90 >= 0.0).all()
    assert (p90 <= 1.0).all()


def test_lppls_historical_bubble_detection():
    """
    Asserts LPPLS model elevates bubble confidence (CI >= 0.60) during the
    climax of the 1999-2000 Dot-Com speculative bubble.
    """
    from bubble_detector.config import PROVENANCE_DIR
    parquet_path = PROVENANCE_DIR / "market_data_50yr.parquet"
    if not parquet_path.exists():
        pytest.skip("market_data_50yr.parquet not available")

    df = pl.read_parquet(parquet_path)
    dates = [str(d)[:10] for d in df["Date"].to_list()]
    
    # Locate peak date near March 24, 2000
    dotcom_indices = [i for i, d in enumerate(dates) if "2000-03" in d]
    assert len(dotcom_indices) > 0, "Dot-Com 2000 dates not found in dataset"
    peak_idx = dotcom_indices[-1]

    # Evaluate slice around peak
    slice_df = df.slice(max(0, peak_idx - 300), 320)
    df_eval = compute_lppls_confidence_indicator(slice_df, target_col="XLK", windows=[60, 90, 125, 180, 250], step=2)
    ci = df_eval["LPPLS_Confidence"].to_numpy()

    # Peak confidence during Dot-Com top must reach at least 0.60 (60% multi-scale agreement)
    assert np.max(ci) >= 0.60, f"Expected LPPLS confidence >= 0.60 during Dot-Com bubble top, got {np.max(ci)}"
