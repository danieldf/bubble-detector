"""
Regime Classification & Structural Break Machine Learning Subpackage.
=====================================================================

Statistical Foundations & Predictive Machine Learning:
-------------------------------------------------------
This subpackage houses institutional regime classification and structural break forecasting models:

1. Macro Mahalanobis Distance Regime Classifier (`regime_mahalanobis.py`):
   - 15-dimensional Riemannian statistical distance utilizing Ledoit-Wolf shrinkage and Tikhonov ridge regularization (lambda = 10^-2).
   - Signed Riemannian Bubble Projection (Score_bubble = (z - mu)^T Sigma^-1 b / sqrt(b^T Sigma^-1 b)),
     resolving quadratic form symmetry via pre-registered economic vector b in {-1, +1}^15.
   - Eradicates crash-trough de-risking: maintains high equity exposure (w_equity >= 0.80) during
     market liquidation troughs (March 2020, October 2008).
   - White-box anomaly driver attribution isolating top-3 contributing indicators with standardized z-scores.

2. Structural Break Gradient Boosted Predictor (`structural_breaks.py`):
   - Predicts forward 20-day drawdown events (> 5% peak-to-trough decline).
   - Enforces Marcos López de Prado (2018) purged & embargoed walk-forward cross-validation (20-day embargo gap).
   - Strictly masks terminal 20 unobservable rows during training to guarantee zero target leakage.
   - Non-parametric isotonic probability calibration verified by Brier score and Expected Calibration Error (ECE < 0.10).
"""

from .structural_breaks import StructuralBreakPredictor
from .regime_mahalanobis import MacroMahalanobisDetector, INDICATORS_15

__all__ = [
    "StructuralBreakPredictor",
    "MacroMahalanobisDetector",
    "INDICATORS_15",
]
