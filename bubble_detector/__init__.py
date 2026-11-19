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
- ui: Dual interactive runtime dashboards: NiceGUI server-side and HoloViz Panel WebAssembly (Pyodide), featuring 8 synchronized analytical tabs.
"""

__version__ = "3.9.0"

from bubble_detector.data.date_horizons import (
    HORIZON_OPTION_1_ID,
    HORIZON_OPTION_2_ID,
    HORIZON_OPTION_3_ID,
    HORIZON_METADATA,
    get_current_date,
    get_dynamic_50yr_date_range,
    get_dynamic_horizon_metadata,
    clamp_to_trading_day,
)
from bubble_detector.data.ingestor import DataIngestor
from bubble_detector.models.regime_mahalanobis import MacroMahalanobisDetector
from bubble_detector.models.structural_breaks import StructuralBreakPredictor
from bubble_detector.models.composite_summary import (
    CompositeSummaryEngine,
    INDICATORS_13_ORTHOGONAL,
    SUMMARY_INDICATORS_5,
    DISLOCATIONS_8_20YR,
    build_band_polygon,
    compute_composite_validation_metrics,
    compute_dislocation_fidelity_metrics,
)
from bubble_detector.backtest.engine import PortfolioBacktestEngine

__all__ = [
    "__version__",
    "DataIngestor",
    "MacroMahalanobisDetector",
    "StructuralBreakPredictor",
    "CompositeSummaryEngine",
    "INDICATORS_13_ORTHOGONAL",
    "SUMMARY_INDICATORS_5",
    "DISLOCATIONS_8_20YR",
    "build_band_polygon",
    "compute_composite_validation_metrics",
    "compute_dislocation_fidelity_metrics",
    "PortfolioBacktestEngine",
    "HORIZON_OPTION_1_ID",
    "HORIZON_OPTION_2_ID",
    "HORIZON_OPTION_3_ID",
    "HORIZON_METADATA",
    "get_current_date",
    "get_dynamic_50yr_date_range",
    "get_dynamic_horizon_metadata",
    "clamp_to_trading_day",
]


