"""
Unit tests for Tech Exuberance Score: Dual Conditions (Macro & Statistical) & Highlighting Spans.
"""

import pytest
import numpy as np
import polars as pl
import pandas as pd

from bubble_detector.features.tech_exuberance import (
    compute_tech_exuberance_metrics,
    compute_exuberance_spans
)


def test_dual_conditions_logic():
    """
    Asserts:
    1. Condition_Macro triggers when M2 growth is slowing AND tech outperformance is expanding.
    2. Condition_Statistical triggers when BSADF or LPPLS hits an extreme threshold.
    3. Tech_Exuberance_Signal is strictly the logical AND of Condition_Macro and Condition_Statistical.
    """
    n = 100
    dates = pd.date_range("2020-01-01", periods=n, freq="B")

    # Construct test series
    spy = np.full(n, 100.0)
    # Tech outperforming in indices 40..80
    xlk = np.full(n, 100.0)
    xlk[40:80] = np.linspace(100.0, 150.0, 40)

    # M2 slowing (negative growth) in indices 30..60
    m2_growth = np.full(n, 5.0)
    m2_growth[30:60] = -2.0

    # Statistical BSADF extreme in indices 50..70
    bsadf = np.zeros(n)
    bsadf[50:70] = 2.5
    bsadf_p90 = np.full(n, 1.5)

    lppls = np.zeros(n)
    lppls_p90 = np.full(n, 0.5)

    df = pl.DataFrame({
        "Date": dates,
        "SPY": spy,
        "XLK": xlk,
        "M2_YoY_Growth": m2_growth,
        "Liquidity_Momentum": np.zeros(n),
        "BSADF_Stat": bsadf,
        "BSADF_90th_Percentile": bsadf_p90,
        "LPPLS_Confidence": lppls,
        "LPPLS_90th_Percentile": lppls_p90,
    })

    df_out = compute_tech_exuberance_metrics(df)

    assert "XLK_SPY_Ratio" in df_out.columns
    assert "Condition_Macro" in df_out.columns
    assert "Condition_Statistical" in df_out.columns
    assert "Tech_Exuberance_Signal" in df_out.columns

    c_macro = df_out["Condition_Macro"].to_numpy()
    c_stat = df_out["Condition_Statistical"].to_numpy()
    signal = df_out["Tech_Exuberance_Signal"].to_numpy()

    # Verify strict AND logic
    expected_signal = c_macro & c_stat
    np.testing.assert_array_equal(signal, expected_signal)

    # Overlap occurs where 40..80 (tech out) & 30..60 (m2 slowing) & 50..70 (bsadf extreme) intersect:
    # Intersection is 50..60
    assert signal[55] == 1, "Signal should be active during mutual overlap"
    assert signal[10] == 0, "Signal should be inactive outside overlap"
    assert signal[35] == 0, "Signal should be inactive when only macro is true"
    assert signal[65] == 0, "Signal should be inactive when only statistical is true"


def test_compute_exuberance_spans():
    """Verifies contiguous date span extraction for Plotly vrect highlight bands."""
    dates = ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05", "2023-01-06"]
    # Active span from index 1 to 3, and index 5
    signals = [0, 1, 1, 1, 0, 1]

    df = pl.DataFrame({
        "Date": dates,
        "Tech_Exuberance_Signal": signals
    })

    spans = compute_exuberance_spans(df)
    assert len(spans) == 2
    assert spans[0] == ("2023-01-02", "2023-01-04")
    assert spans[1] == ("2023-01-06", "2023-01-06")

    # Empty signals
    df_empty = pl.DataFrame({
        "Date": dates,
        "Tech_Exuberance_Signal": [0] * len(dates)
    })
    assert compute_exuberance_spans(df_empty) == []
