"""Data Ingestion Module"""
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
