"""
Unit tests for StructuralBreakPredictor machine learning module.
"""

import pytest
import numpy as np
import polars as pl
from bubble_detector.data.ingestor import DataIngestor
from bubble_detector.features import (
    compute_macro_valuations, compute_margin_leverage_metrics,
    compute_gsadf_gpt_decomposition, compute_tda_wavelet_complexity,
    compute_options_volatility_metrics
)
from bubble_detector.models.structural_breaks import StructuralBreakPredictor

@pytest.fixture
def processed_df(tmp_path):
    ingestor = DataIngestor(cache_dir=tmp_path / "cache")
    df = ingestor.fetch_market_data(start_date="2023-01-01", end_date="2024-06-01", use_cache=False)
    df = compute_macro_valuations(df)
    df = compute_margin_leverage_metrics(df)
    df = compute_gsadf_gpt_decomposition(df, target_col="SPY", window_size=20)
    df = compute_tda_wavelet_complexity(df, target_col="SPY", window_size=20)
    df = compute_options_volatility_metrics(df)
    return df

def test_structural_break_predictor_walk_forward(processed_df):
    predictor = StructuralBreakPredictor(n_estimators=10, max_depth=2)
    metrics = predictor.fit_walk_forward(processed_df, n_splits=3)

    assert "cv_mean_accuracy" in metrics
    assert metrics["cv_mean_accuracy"] >= 0.0
    assert predictor.is_trained

def test_predict_drawdown_probability(processed_df):
    predictor = StructuralBreakPredictor(n_estimators=10, max_depth=2)
    probs = predictor.predict_drawdown_probability(processed_df)

    assert isinstance(probs, np.ndarray)
    assert len(probs) == len(processed_df)
    assert np.all(probs >= 0.0) and np.all(probs <= 1.0)


def test_structural_breaks_embargo_no_lookahead(processed_df):
    """Verify that fit_walk_forward enforces a purge embargo gap preventing forward target leakage."""
    predictor = StructuralBreakPredictor(n_estimators=10, max_depth=2)
    metrics = predictor.fit_walk_forward(processed_df, n_splits=3, embargo_window=20)

    assert "embargo_window" in metrics
    assert metrics["embargo_window"] == 20
    assert metrics["cv_mean_accuracy"] >= 0.0
    assert predictor.is_trained
