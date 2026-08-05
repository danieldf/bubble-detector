"""
Unit tests for Feature Engineering Modules (technicals, macro valuations, leverage, GSADF/GPT, TDA, options).
"""

import pytest
import numpy as np
import polars as pl
from bubble_detector.data.ingestor import DataIngestor
from bubble_detector.features import (
    compute_technical_indicators, compute_macro_valuations,
    compute_margin_leverage_metrics, compute_gsadf_gpt_decomposition,
    compute_tda_wavelet_complexity, compute_options_volatility_metrics
)

@pytest.fixture
def sample_df(tmp_path):
    ingestor = DataIngestor(cache_dir=tmp_path / "cache")
    return ingestor.fetch_market_data(start_date="2024-01-01", end_date="2024-06-01", use_cache=False)

def test_compute_technical_indicators(sample_df):
    df_out = compute_technical_indicators(sample_df, target_col="SPY")
    assert "SPY_MA20" in df_out.columns
    assert "SPY_MA50" in df_out.columns
    assert "SPY_BB_Upper" in df_out.columns
    assert "SPY_RSI14" in df_out.columns
    assert "SPY_Vol20D" in df_out.columns

def test_compute_macro_valuations(sample_df):
    df_out = compute_macro_valuations(sample_df)
    assert "Shiller_CAPE" in df_out.columns
    assert "P_CAPE" in df_out.columns
    assert "Buffett_Indicator" in df_out.columns
    assert "CAPE_ZScore" in df_out.columns

def test_compute_margin_leverage_metrics(sample_df):
    df_out = compute_margin_leverage_metrics(sample_df)
    assert "Margin_Debt_YoY_Pct" in df_out.columns
    assert "Margin_Debt_Velocity_20D" in df_out.columns
    assert "Leverage_Exhaustion_Gap" in df_out.columns
    assert "Margin_Exhaustion_Score" in df_out.columns

def test_compute_gsadf_gpt_decomposition(sample_df):
    df_out = compute_gsadf_gpt_decomposition(sample_df, target_col="SPY", window_size=20)
    assert "GSADF_Stat" in df_out.columns
    assert "GSADF_GPT_Adjusted" in df_out.columns
    assert "Speculative_Bubble_Signal" in df_out.columns

def test_compute_tda_wavelet_complexity(sample_df):
    df_out = compute_tda_wavelet_complexity(sample_df, target_col="SPY", window_size=20)
    assert "TDA_Persistence_L2_Norm" in df_out.columns
    assert "Wavelet_Complexity_Score" in df_out.columns
    
    tda = df_out["TDA_Persistence_L2_Norm"].to_numpy()
    assert not np.isnan(tda).any(), "TDA_Persistence_L2_Norm contains NaN values"
    assert (tda >= 0.0).all(), "TDA_Persistence_L2_Norm values must be non-negative"
    assert (tda <= 0.25).all(), "TDA_Persistence_L2_Norm values must not exceed 0.25 threshold"


def test_compute_options_volatility_metrics(sample_df):
    df_out = compute_options_volatility_metrics(sample_df)
    assert "VIX_Term_Structure_Slope" in df_out.columns
    assert "OVX_VIX_CrossAsset_Ratio" in df_out.columns
    assert "SKEW_Tail_Risk_Alert" in df_out.columns

def test_tda_wasm_parity():
    """Verify 100% numerical parity for TDA Persistence L2 Norm between WASM app and topology.py engine."""
    from bubble_detector.ui.panel_dashboard import generate_wasm_dataset
    data_wasm = generate_wasm_dataset("2015-01-01", "2026-07-28")
    spy_prices = data_wasm["SPY"]
    df_polars = pl.DataFrame({"SPY": spy_prices})
    
    df_tda = compute_tda_wavelet_complexity(df_polars, target_col="SPY", window_size=30)
    tda_engine = df_tda["TDA_Persistence_L2_Norm"].to_numpy()
    tda_wasm = data_wasm["TDA_Persistence_L2_Norm"]
    
    np.testing.assert_allclose(tda_engine, tda_wasm, rtol=1e-5, atol=1e-5, err_msg="TDA WASM output must match topology.py engine 100% identically")

