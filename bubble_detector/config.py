"""
Global Configuration, Logging Infrastructure & Constants Module.
=================================================================

Architectural Purpose:
----------------------
Serves as the centralized single source of truth for runtime directories, logging topology,
custom exception hierarchies, ticker mappings, and date horizon parameters across the
entire Bubble Detector ecosystem.

Directory Structure:
--------------------
- BASE_DIR: Repository root filesystem path.
- LOG_DIR: Target for rotating application logs (`logs/bubble_detector.log`).
- CACHE_DIR: Persistent intermediate query cache (`data/cache/`).
- PROVENANCE_DIR: Permanent institutional raw datasets (`data/provenance/`).
"""

import os
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

# Base Paths
BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"
CACHE_DIR = BASE_DIR / "data" / "cache"
PROVENANCE_DIR = BASE_DIR / "data" / "provenance"

LOG_DIR.mkdir(parents=True, exist_ok=True)
CACHE_DIR.mkdir(parents=True, exist_ok=True)
PROVENANCE_DIR.mkdir(parents=True, exist_ok=True)

# Logger Setup
LOG_FILE = LOG_DIR / "bubble_detector.log"
logger = logging.getLogger("bubble_detector")
logger.setLevel(logging.INFO)

if not logger.handlers:
    file_handler = RotatingFileHandler(
        LOG_FILE, maxBytes=10 * 1024 * 1024, backupCount=5, encoding="utf-8"
    )
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s (%(filename)s:%(lineno)d): %(message)s"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

# Custom Exceptions
class BubbleDetectorError(Exception):
    """Base exception for Bubble Detector package."""
    pass

class DataFetchError(BubbleDetectorError):
    """Raised when data fetching fails."""
    pass

class IndicatorComputationError(BubbleDetectorError):
    """Raised when indicator computation fails."""
    pass

class ModelTrainingError(BubbleDetectorError):
    """Raised when ML model training fails."""
    pass

class ValidationError(BubbleDetectorError):
    """Raised when data validation fails."""
    pass

# Financial & Market Constants (2026 Macro Environment Defaults)
SP500_TICKER = "SPY"
SECTOR_TICKERS = {
    "Technology": "XLK",
    "Semiconductors": "SMH",
    "Energy": "XLE",
    "Housing": "ITB",
    "Defense": "ITA",
}

VOLATILITY_TICKERS = {
    "VIX": "^VIX",
    "VIX1D": "^VIX1D",
    "VIX3M": "^VIX3M",
    "SKEW": "^SKEW",
    "VXN": "^VXN",
    "OVX": "^OVX",
}

from bubble_detector.data.date_horizons import (
    get_current_date,
    get_dynamic_50yr_date_range,
    HORIZON_OPTION_1_ID,
    HORIZON_OPTION_2_ID,
    get_dynamic_horizon_metadata,
)

# Evaluated defaults
_dyn_start_50, _dyn_end = get_dynamic_50yr_date_range()
DEFAULT_START_DATE = _dyn_start_50
DEFAULT_END_DATE = _dyn_end

HORIZON_OPTION_1_LABEL = f"Option 1: 50-Year Multi-Decade Horizon ({_dyn_start_50[:4]}–{_dyn_end[:4]})"
HORIZON_OPTION_1_START = _dyn_start_50

HORIZON_OPTION_2_LABEL = f"Option 2: Modern 5-Regime Horizon (2015–{_dyn_end[:4]})"
HORIZON_OPTION_2_START = "2015-01-01"

HORIZON_METADATA = get_dynamic_horizon_metadata()


# Historical Threshold Anchors (2026 Baseline)
CAPE_HISTORICAL_MEAN = 17.0
CAPE_2026_CURRENT = 41.37
BUFFETT_HISTORICAL_MEAN = 100.0  # % of GDP
BUFFETT_2026_CURRENT = 218.1     # % of GDP
HOUSING_PRICE_TO_INCOME_CURRENT = 7.11
MARGIN_DEBT_2026_PEAK_B = 1416.0 # Billion $

