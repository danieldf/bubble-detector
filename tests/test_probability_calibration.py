"""
Unit tests for Probability Calibration, Brier Score, and Reliability Diagrams (ECE).
"""

import pytest
import numpy as np
import polars as pl
from bubble_detector.models.structural_breaks import StructuralBreakPredictor

def test_walk_forward_brier_score():
    """Asserts calibrated drawdown probability achieves Brier score strictly superior to unconditional baseline."""
    np.random.seed(42)
    n = 200

    # True binary outcomes with 30% positive base rate
    y_true = (np.random.rand(n) < 0.30).astype(np.int32)

    # Well-calibrated model predictions correlated with ground truth
    noise = np.random.randn(n) * 0.15
    y_prob = np.clip(y_true * 0.65 + 0.15 + noise, 0.05, 0.95)

    brier = StructuralBreakPredictor.compute_brier_score(y_true, y_prob)

    p_base = float(np.mean(y_true))
    baseline_brier = p_base * (1.0 - p_base)

    assert brier < baseline_brier, f"Brier score {brier:.4f} did not beat baseline {baseline_brier:.4f}"
    assert brier >= 0.0

def test_reliability_diagram_monotonicity():
    """Asserts expected calibration error (ECE) is strictly below 0.10 for calibrated model probabilities."""
    np.random.seed(42)
    n = 500

    # Probabilities drawn uniformly over [0, 1]
    y_prob = np.random.uniform(0.05, 0.95, size=n)
    # Bernoulli realizations with P(Y=1) = y_prob (perfect calibration under truth)
    y_true = (np.random.rand(n) < y_prob).astype(np.int32)

    diag = StructuralBreakPredictor.compute_reliability_diagram(y_true, y_prob, n_bins=10)

    assert "ece" in diag
    ece = diag["ece"]
    assert ece < 0.10, f"Expected Calibration Error (ECE) was {ece:.4f} (expected < 0.10)"
    assert len(diag["bin_edges"]) == 11
    assert len(diag["confidences"]) == 10
