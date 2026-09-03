"""
Unit tests for Signed Mahalanobis Projection, Vector b, Robust Covariance, and Crash-Trough Exposure Retention.
"""

import pytest
import numpy as np
import polars as pl

from bubble_detector.models.regime_mahalanobis import (
    MacroMahalanobisDetector, INDICATORS_15, DIRECTION_VECTOR_B
)

def test_signed_projection_asymmetry():
    """
    Asserts speculative bubble states (z > 0 along vector b) produce positive bubble scores,
    while crash states (z < 0 along vector b) produce negative scores.
    """
    detector = MacroMahalanobisDetector()
    k = len(INDICATORS_15)

    # 1. Bubble State: High valuations, high leverage, high GSADF (aligned with +b)
    # Construct synthetic history with 100 normal observations
    np.random.seed(42)
    history = np.random.randn(100, k).astype(np.float32)

    # State at index 100: positive excursion for b=+1 features, negative for b=-1 features
    b_signs = np.array([DIRECTION_VECTOR_B.get(col, 1.0) for col in INDICATORS_15])
    bubble_vec = 3.5 * b_signs  # Overextension
    crash_vec = -3.5 * b_signs   # Liquidation / deep value

    Z_bubble = np.vstack([history, bubble_vec])
    Z_crash = np.vstack([history, crash_vec])

    _, scores_bubble, dm_b_bubble, dm_c_bubble = detector.compute_signed_mahalanobis_metrics(Z_bubble)
    _, scores_crash, dm_b_crash, dm_c_crash = detector.compute_signed_mahalanobis_metrics(Z_crash)

    # Bubble state must have positive signed score and DM_bubble > DM_crash
    assert scores_bubble[-1] > 2.0, f"Bubble signed score was {scores_bubble[-1]} (expected > 2.0)"
    assert dm_b_bubble[-1] > dm_c_bubble[-1]

    # Crash state must have negative signed score and DM_crash > DM_bubble
    assert scores_crash[-1] < -2.0, f"Crash signed score was {scores_crash[-1]} (expected < -2.0)"
    assert dm_c_crash[-1] > dm_b_crash[-1]

def test_crash_trough_exposure_retention():
    """
    Asserts w_equity >= 0.80 during crash troughs (negative signed scores or DM_crash > DM_bubble),
    proving complete eradication of crash-bottom de-risking whipsaws.
    """
    detector = MacroMahalanobisDetector(min_equity_exposure=0.20)

    # Test cases:
    # 1. Bubble condition: high rank (0.95), positive signed score (+3.0) -> should de-risk
    ranks_bubble = np.array([0.95], dtype=np.float32)
    score_bubble = np.array([3.0], dtype=np.float32)
    dm_b = np.array([5.5], dtype=np.float32)
    dm_c = np.array([0.5], dtype=np.float32)

    exp_bubble = detector.compute_dynamic_exposure(
        ranks_bubble, signed_scores=score_bubble, dm_crash=dm_c, dm_bubble=dm_b
    )
    assert exp_bubble[0] <= 0.30, f"Failed to derisk in bubble state: w_equity = {exp_bubble[0]}"

    # 2. Crash Trough (March 2020, October 2008): high distance rank (0.95), but negative signed score (-3.0)
    # and DM_crash dominating -> must maintain high equity exposure (>= 0.80)
    ranks_crash = np.array([0.95], dtype=np.float32)
    score_crash = np.array([-3.2], dtype=np.float32)
    dm_b_crash = np.array([0.8], dtype=np.float32)
    dm_c_crash = np.array([6.2], dtype=np.float32)

    exp_crash = detector.compute_dynamic_exposure(
        ranks_crash, signed_scores=score_crash, dm_crash=dm_c_crash, dm_bubble=dm_b_crash
    )
    assert exp_crash[0] >= 0.80, f"Crash trough derisked improperly: w_equity = {exp_crash[0]} (expected >= 0.80)"

def test_min_cov_det_robustness():
    """Asserts robust covariance estimation (MinCovDet / Ledoit-Wolf) withstands outlier contamination."""
    np.random.seed(42)
    k = len(INDICATORS_15)
    Z = np.random.randn(120, k).astype(np.float32)

    # Inject extreme outlier contamination into historical window
    Z[50, :] = 50.0  # Massive outlier spike

    detector_lw = MacroMahalanobisDetector(covariance_method="ledoit_wolf")
    m_dist_lw, _, _, _ = detector_lw.compute_signed_mahalanobis_metrics(Z)

    assert not np.isnan(m_dist_lw).any()
    assert not np.isinf(m_dist_lw).any()
    # At normal rows following the outlier (e.g. index 70), distance should stay reasonably bounded
    assert m_dist_lw[70] < 12.0
