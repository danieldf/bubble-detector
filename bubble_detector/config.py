"""
Configuration and Logging Module for Bubble Detector.
"""

import os
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

# Base Paths
BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"
CACHE_DIR = BASE_DIR / "data" / "cache"

LOG_DIR.mkdir(parents=True, exist_ok=True)
CACHE_DIR.mkdir(parents=True, exist_ok=True)

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

DEFAULT_START_DATE = "2015-01-01"
DEFAULT_END_DATE = "2026-07-28"

# Horizon Options
HORIZON_OPTION_1_ID = "option_1"
HORIZON_OPTION_1_LABEL = "Option 1: Modern 5-Regime Horizon (2015–2026)"
HORIZON_OPTION_1_START = "2015-01-01"

HORIZON_OPTION_2_ID = "option_2"
HORIZON_OPTION_2_LABEL = "Option 2: Expanded 7-Regime Horizon (1998–2026)"
HORIZON_OPTION_2_START = "1998-01-01"

HORIZON_METADATA = {
    HORIZON_OPTION_1_ID: {
        "label": HORIZON_OPTION_1_LABEL,
        "start_date": HORIZON_OPTION_1_START,
        "end_date": DEFAULT_END_DATE,
        "regimes_count": 5,
        "native_fidelity": "100%",
        "fidelity_status": "Native High-Fidelity Coverage",
        "badge_color": "green",
        "included_crashes": [
            "2018 Volmageddon & Q4 QT Compression",
            "2020 COVID-19 Flash Crash (VIX 82.7 Spike)",
            "2020-2021 Post-COVID Liquidity Exuberance",
            "2022 Fed Rate Tightening & Tech Drawdown",
            "2024-2026 AI CapEx Mega-Cap Rally (CAPE 41.37)"
        ],
        "description": "Provides 100% native data integrity across all 12 model features (including VIX1D, OVX, SKEW, and DSPX) with zero back-filling or proxy interpolation required."
    },
    HORIZON_OPTION_2_ID: {
        "label": HORIZON_OPTION_2_LABEL,
        "start_date": HORIZON_OPTION_2_START,
        "end_date": DEFAULT_END_DATE,
        "regimes_count": 7,
        "native_fidelity": "~92%",
        "fidelity_status": "Extended Historical Spectrum (Proxy Imputed Pre-2007)",
        "badge_color": "amber",
        "included_crashes": [
            "1999-2000 Dot-Com Tech Bubble & Crash (CAPE 44.19 Peak)",
            "2007-2009 Subprime Housing Crisis & GFC Crash (Housing PTI ~7.0x)",
            "2018 Volmageddon & Q4 QT Compression",
            "2020 COVID-19 Flash Crash (VIX 82.7 Spike)",
            "2020-2021 Post-COVID Liquidity Exuberance",
            "2022 Fed Rate Tightening & Tech Drawdown",
            "2024-2026 AI CapEx Mega-Cap Rally (CAPE 41.37)"
        ],
        "description": "Extends coverage across 28.5 years to encompass all 7 major market bubbles/crashes. Options metrics prior to 2007 utilize synthetic proxy modeling."
    }
}

# Historical Threshold Anchors (2026 Baseline)
CAPE_HISTORICAL_MEAN = 17.0
CAPE_2026_CURRENT = 41.37
BUFFETT_HISTORICAL_MEAN = 100.0  # % of GDP
BUFFETT_2026_CURRENT = 218.1     # % of GDP
HOUSING_PRICE_TO_INCOME_CURRENT = 7.11
MARGIN_DEBT_2026_PEAK_B = 1416.0 # Billion $

