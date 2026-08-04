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

def test_compute_options_volatility_metrics(sample_df):
    df_out = compute_options_volatility_metrics(sample_df)
    assert "VIX_Term_Structure_Slope" in df_out.columns
    assert "OVX_VIX_CrossAsset_Ratio" in df_out.columns
    assert "SKEW_Tail_Risk_Alert" in df_out.columns
