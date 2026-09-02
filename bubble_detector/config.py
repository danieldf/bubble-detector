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

import datetime
from typing import Dict, Any, Tuple, Optional, Union

def get_current_date(override: Optional[Union[datetime.date, str]] = None) -> datetime.date:
    """Return current execution date, or parse override date string/object."""
    if override is not None:
        if isinstance(override, str):
            return datetime.date.fromisoformat(override)
        return override
    return datetime.date.today()

def get_dynamic_50yr_date_range(today: Optional[Union[datetime.date, str]] = None) -> Tuple[str, str]:
    """
    Compute rolling 50-year date range from current execution date.
    Safely handles leap-year edge cases (e.g. Feb 29 -> Feb 28 50 years prior).
    """
    curr = get_current_date(today)
    end_date_str = curr.strftime("%Y-%m-%d")
    try:
        start_date = curr.replace(year=curr.year - 50)
    except ValueError:
        start_date = curr.replace(year=curr.year - 50, day=28)
    start_date_str = start_date.strftime("%Y-%m-%d")
    return start_date_str, end_date_str

# Horizon Option IDs
HORIZON_OPTION_1_ID = "option_1"
HORIZON_OPTION_2_ID = "option_2"

def get_dynamic_horizon_metadata(today: Optional[Union[datetime.date, str]] = None) -> Dict[str, Dict[str, Any]]:
    """
    Construct dynamic horizon metadata dictionary anchored to current execution date.
    Option 1: 50-Year Multi-Decade Horizon (e.g. 1976–2026, 9 historical regimes).
    Option 2: Modern 5-Regime Horizon (2015–present, 5 regimes, 100% native fidelity).
    """
    curr = get_current_date(today)
    start_50yr, end_today = get_dynamic_50yr_date_range(curr)
    start_year_50 = start_50yr[:4]
    curr_year = end_today[:4]

    return {
        HORIZON_OPTION_1_ID: {
            "label": f"Option 1: 50-Year Multi-Decade Horizon ({start_year_50}–{curr_year})",
            "start_date": start_50yr,
            "end_date": end_today,
            "regimes_count": 9,
            "native_fidelity": "~85%",
            "fidelity_status": "50-Year Multi-Decade Historical Spectrum",
            "badge_color": "green",
            "included_crashes": [
                "1970s Stagflation & 1980–1982 Volcker Rate Shock (20% Fed Funds Rate)",
                "1987 Black Monday Crash (-20.5% single-day drawdown)",
                "1990–1991 Early 1990s Recession & S&L Crisis",
                "1999–2000 Dot-Com Tech Bubble & Crash (CAPE 44.19 Peak)",
                "2007–2009 Subprime Housing Crisis & GFC Crash (Housing PTI ~7.0x)",
                "2018 Volmageddon & Q4 QT Compression",
                "2020 COVID-19 Flash Crash (VIX 82.7 Spike)",
                "2022 Fed Rate Tightening & Tech Drawdown",
                "2024–2026 AI CapEx Mega-Cap Rally (CAPE 41.37)"
            ],
            "description": f"Encompasses a rolling 50-year range ({start_50yr} to {end_today}) spanning 9 historical regimes from 1970s stagflation through 2026 AI exuberance. Earlier eras utilize historical S&P index anchors and proxy modeling."
        },
        HORIZON_OPTION_2_ID: {
            "label": f"Option 2: Modern 5-Regime Horizon (2015–{curr_year})",
            "start_date": "2015-01-01",
            "end_date": end_today,
            "regimes_count": 5,
            "native_fidelity": "100%",
            "fidelity_status": "Native High-Fidelity Coverage",
            "badge_color": "blue",
            "included_crashes": [
                "2018 Volmageddon & Q4 QT Compression",
                "2020 COVID-19 Flash Crash (VIX 82.7 Spike)",
                "2020-2021 Post-COVID Liquidity Exuberance",
                "2022 Fed Rate Tightening & Tech Drawdown",
                "2024–2026 AI CapEx Mega-Cap Rally (CAPE 41.37)"
            ],
            "description": "Provides 100% native data integrity across all 12 model features (including VIX1D, OVX, SKEW, and DSPX) with zero back-filling or proxy interpolation required."
        }
    }

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

