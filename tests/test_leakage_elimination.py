"""
Unit tests for Leakage Eradication & Multicollinearity Reduction.
"""

import pytest
from bubble_detector.models.regime_mahalanobis import INDICATORS_15, MacroMahalanobisDetector

def test_drawdown_probability_not_in_covariance():
    """Asserts 'Drawdown_Probability' is completely absent from INDICATORS_15 and covariance estimation."""
    assert "Drawdown_Probability" not in INDICATORS_15
    detector = MacroMahalanobisDetector()
    assert "Drawdown_Probability" not in detector.indicators

def test_p_cape_elimination():
    """Asserts 'P_CAPE' is not in the feature vector, resolving exact collinearity with Shiller_CAPE."""
    assert "P_CAPE" not in INDICATORS_15
    detector = MacroMahalanobisDetector()
    assert "P_CAPE" not in detector.indicators
    # Shiller_CAPE must be retained
    assert "Shiller_CAPE" in INDICATORS_15
