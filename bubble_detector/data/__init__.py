"""
Point-in-Time Data Ingestion & Multi-Decade Horizon Subpackage.
==============================================================

Architectural Scope & Data Lineage:
-----------------------------------
This subpackage provides institutional data ETL pipelines, multi-decade horizon anchoring,
and cliff-free time series splicing:

1. Dynamic Calendar-Anchored 50-Year Horizon Engine (`date_horizons.py`):
   - Dynamically anchors historical analysis to T = 50 physical calendar years rolling from
     the operational execution date (e.g. 1976–2026, 13,045 trading days).
   - Captures 9 historical stress regimes: 1970s Great Inflation, 1987 Black Monday,
     1990 S&L Crisis, 2000 Dot-Com Bubble, 2008 GFC, 2018 Volmageddon, 2020 COVID,
     2022 Fed rate hikes, and 2024–2026 AI CapEx concentration.
   - Robust leap-year snapping handles February 29 offsets deterministically.

2. Robert Shiller Monthly ie_data ETL (`etl_shiller.py`):
   - Direct ingestion of Robert Shiller's official `ie_data.xls` (1871–present).
   - Monthly S&P Composite prices, 10-year smoothed earnings, dividends, CPI, and CAPE.
   - Point-in-time +5 business day publication lag enforced via backward as-of merges.

3. FRED Macroeconomic ETL (`etl_fred.py`):
   - Official Federal Reserve Bank of St. Louis economic series:
     * Nominal GDP (quarterly SAAR, +60-day publication lag).
     * S&P CoreLogic Case-Shiller National Home Price Index (+60-day publication lag).
     * Real Median Household Income (annual Census release).
   - Normalized Housing Price-to-Income (PTI) ratio.

4. FINRA & NYSE Customer Margin Debt ETL (`etl_finra.py`):
   - Regulatory customer margin debit balances under FINRA Rule 4521 (1997–present).
   - Spliced with historical NYSE member firm debit archives (1959–1996).
   - Enforces strict +21 calendar day publication lag post month-end.

5. CBOE S&P 100 Implied Volatility Index ETL (`etl_vxo.py`):
   - Authentic CBOE VXO daily history (1986–present), capturing the 150.19 Black Monday peak.
   - Spliced with modern CBOE VIX quotes (1990–present) and VRP-adjusted realized volatility (1976–1985).

6. High-Throughput Panel Data Ingestor (`ingestor.py`):
   - Multi-asset panel construction, continuous backward return compounding ($P_{t-1} = P_t \\cdot S_{t-1}/S_t$).
   - Polars Arrow downcasting (Float32/Int32) and snappy-compressed Parquet caching.
"""

from .date_horizons import (
    get_current_date,
    get_dynamic_50yr_date_range,
    get_dynamic_horizon_metadata,
    HORIZON_OPTION_1_ID,
    HORIZON_OPTION_2_ID,
    DEFAULT_START_DATE,
    DEFAULT_END_DATE,
    HORIZON_METADATA,
)
from .ingestor import DataIngestor
from .etl_shiller import get_shiller_data
from .etl_fred import get_fred_data
from .etl_finra import get_finra_margin_debt
from .etl_vxo import get_vxo_data

__all__ = [
    "DataIngestor",
    "get_shiller_data",
    "get_fred_data",
    "get_finra_margin_debt",
    "get_vxo_data",
    "get_current_date",
    "get_dynamic_50yr_date_range",
    "get_dynamic_horizon_metadata",
    "HORIZON_OPTION_1_ID",
    "HORIZON_OPTION_2_ID",
    "DEFAULT_START_DATE",
    "DEFAULT_END_DATE",
    "HORIZON_METADATA",
]
