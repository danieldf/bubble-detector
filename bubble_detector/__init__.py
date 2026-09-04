"""
Multidimensional Econometric & Quantitative Market Bubble Detection System.
===========================================================================

A production-grade quantitative framework for identifying systemic financial bubbles,
structural breaks, and regime transitions across equity, macroeconomic, leverage,
and volatility dimensions.

Key Architectural Components:
-----------------------------
- data: Point-in-time provenance ETL (Shiller CAPE, FRED GDP, FINRA Margin Debt, CBOE VXO).
- features: Technical momentum, macro valuations, leverage velocity, canonical PSY GSADF,
  TDA Vietoris-Rips persistent homology, and options volatility term structure.
- models: Signed Riemannian Mahalanobis distance regime classifier and gradient boosted
  structural break predictor with purged-embargo isotonic calibration.
- backtest: Institutional portfolio simulation engine with transaction frictions,
  slippage, cash yields, and falsifiable historical peak validation event studies.
- ui: Dual interactive runtime dashboards: NiceGUI server-side and HoloViz Panel WebAssembly (Pyodide).
"""

__version__ = "3.0.0"

from bubble_detector.data.ingestor import DataIngestor
from bubble_detector.models.regime_mahalanobis import MacroMahalanobisDetector
from bubble_detector.models.structural_breaks import StructuralBreakPredictor
from bubble_detector.backtest.engine import PortfolioBacktestEngine

