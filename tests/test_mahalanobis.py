"""
Unit tests for Macro Mahalanobis Distance Regime-Switching Bubble Detector (Method 1).
"""

import pytest
import numpy as np
import polars as pl

from bubble_detector.models.regime_mahalanobis import MacroMahalanobisDetector, INDICATORS_15
from bubble_detector.data.ingestor import DataIngestor
from bubble_detector.features import (
    compute_technical_indicators, compute_macro_valuations,
    compute_margin_leverage_metrics, compute_gsadf_gpt_decomposition,
    compute_tda_wavelet_complexity, compute_options_volatility_metrics
)
from bubble_detector.models.structural_breaks import StructuralBreakPredictor

@pytest.fixture
def mock_indicators_df():
    """Generate mock 500-day Polars DataFrame containing all 15 indicators."""
    np.random.seed(42)
    n = 500
    dates = pl.date_range(start=pl.date(2020, 1, 1), end=pl.date(2021, 12, 31), interval="1d", eager=True)[:n]
    
    data = {"Date": dates}
    for col in INDICATORS_15:
        data[col] = (100.0 + np.cumsum(np.random.randn(n))).astype(np.float32)
    
    return pl.DataFrame(data)

def test_stationary_features_shape_and_values(mock_indicators_df):
    detector = MacroMahalanobisDetector(rolling_window=60)
    Z = detector.preprocess_stationary_features(mock_indicators_df)
    
    assert Z.shape == (len(mock_indicators_df), 15)
    assert not np.isnan(Z).any()
    assert not np.isinf(Z).any()
    # Means of z-scores should hover near zero
    assert np.all(np.abs(np.mean(Z[100:], axis=0)) < 1.0)

def test_mahalanobis_distance_non_negative(mock_indicators_df):
    detector = MacroMahalanobisDetector(rolling_window=60)
    Z = detector.preprocess_stationary_features(mock_indicators_df)
    m_dist = detector.compute_mahalanobis_distance(Z)
    
    assert len(m_dist) == len(mock_indicators_df)
    assert not np.isnan(m_dist).any()
    assert np.all(m_dist >= 0.0)

def test_regime_probability_bounds(mock_indicators_df):
    detector = MacroMahalanobisDetector(rolling_window=60)
    Z = detector.preprocess_stationary_features(mock_indicators_df)
    m_dist = detector.compute_mahalanobis_distance(Z)
    probs = detector.compute_regime_probability(m_dist)
    
    assert len(probs) == len(mock_indicators_df)
    assert np.all((probs >= 0.0) & (probs <= 1.0))

def test_dynamic_exposure_bounds_and_monotonicity():
    detector = MacroMahalanobisDetector(min_equity_exposure=0.20)
    test_probs = np.array([0.0, 0.25, 0.50, 0.75, 1.0], dtype=np.float32)
    exposures = detector.compute_dynamic_exposure(test_probs)
    
    assert np.isclose(exposures[0], 1.0)
    assert np.isclose(exposures[-1], 0.20)
    # Monotonically decreasing
    assert np.all(np.diff(exposures) <= 0.0)
    assert np.all((exposures >= 0.20) & (exposures <= 1.0))

def test_anomaly_driver_attribution(mock_indicators_df):
    detector = MacroMahalanobisDetector(rolling_window=60)
    Z = detector.preprocess_stationary_features(mock_indicators_df)
    
    # Intentionally inject massive anomaly into Shiller_CAPE at index 300
    cape_idx = INDICATORS_15.index("Shiller_CAPE")
    Z[300, cape_idx] = 12.5
    
    primary_drivers, summaries = detector.get_top_anomaly_drivers(Z, top_k=3)
    
    assert primary_drivers[300] == "Shiller_CAPE"
    assert "Shiller_CAPE" in summaries[300]
    assert "+12.5σ" in summaries[300]

def test_full_pipeline_polars_integration(tmp_path):
    """End-to-end integration test of MacroMahalanobisDetector on market dataset."""
    ingestor = DataIngestor(cache_dir=tmp_path / "cache")
    df = ingestor.fetch_market_data("2024-01-01", "2026-07-28", use_cache=False)
    df = compute_technical_indicators(df)
    df = compute_macro_valuations(df)
    df = compute_margin_leverage_metrics(df)
    df = compute_gsadf_gpt_decomposition(df)
    df = compute_tda_wavelet_complexity(df)
    df = compute_options_volatility_metrics(df)
    
    predictor = StructuralBreakPredictor()
    probs = predictor.predict_drawdown_probability(df)
    df = df.with_columns(pl.Series("Drawdown_Probability", probs))
    
    detector = MacroMahalanobisDetector(rolling_window=100)
    res_df = detector.process(df)
    
    expected_cols = [
        "Mahalanobis_Distance",
        "Bubble_Regime_Probability",
        "Dynamic_Equity_Exposure",
        "Primary_Anomaly_Driver",
        "Anomaly_Summary"
    ]
    for col in expected_cols:
        assert col in res_df.columns
        assert res_df[col].null_count() == 0
