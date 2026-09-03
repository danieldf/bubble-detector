"""
Backtesting & Historical Empirical Validation Module.
"""

from .engine import PortfolioBacktestEngine, BacktestResult
from .validation_table import (
    HISTORICAL_CRASH_EVENTS,
    generate_historical_validation_table,
    compute_validation_summary_statistics,
)

__all__ = [
    "PortfolioBacktestEngine",
    "BacktestResult",
    "HISTORICAL_CRASH_EVENTS",
    "generate_historical_validation_table",
    "compute_validation_summary_statistics",
]
