"""
Unit tests for Date Range Horizons (Dynamic 50-Year Horizon vs Modern Horizon).
"""

import pytest
import datetime
import polars as pl
from bubble_detector.config import (
    HORIZON_METADATA, HORIZON_OPTION_1_ID, HORIZON_OPTION_2_ID,
    get_dynamic_50yr_date_range, get_current_date
)
from bubble_detector.data.ingestor import DataIngestor
from bubble_detector.ui.dashboard import DashboardState

@pytest.fixture
def ingestor(tmp_path):
    return DataIngestor(cache_dir=tmp_path / "cache")

def test_dynamic_50yr_date_generator():
    """Verify that dynamic 50-year calculation yields exact 50-year window."""
    # Test specific date: 2026-09-02 -> 1976-09-02
    start_str, end_str = get_dynamic_50yr_date_range("2026-09-02")
    assert start_str == "1976-09-02"
    assert end_str == "2026-09-02"

    # Test leap-year edge case: 2024-02-29 -> 1974-02-28
    start_leap, end_leap = get_dynamic_50yr_date_range("2024-02-29")
    assert start_leap == "1974-02-28"
    assert end_leap == "2024-02-29"

    # Test default evaluation matches current year - 50
    curr = get_current_date()
    start_curr, end_curr = get_dynamic_50yr_date_range()
    assert end_curr == curr.strftime("%Y-%m-%d")
    assert int(end_curr[:4]) - int(start_curr[:4]) == 50

def test_option_1_50yr_data_ingestion(ingestor):
    """Verify 50-year multi-decade dataset ingestion (>10,000 rows, zero nulls)."""
    meta = HORIZON_METADATA[HORIZON_OPTION_1_ID]
    df = ingestor.fetch_market_data(start_date=meta["start_date"], end_date=meta["end_date"], use_cache=False)

    assert isinstance(df, pl.DataFrame)
    # 50 years of business days encompasses ~13,000 trading days
    assert len(df) > 10000
    assert "SPY" in df.columns
    assert "Shiller_CAPE" in df.columns
    assert "Housing_Price_to_Income" in df.columns
    assert "FINRA_Margin_Debt" in df.columns
    assert "GDP_Nominal" in df.columns

    # Verify bounds match requested start and end dates exactly
    first_date_str = str(df["Date"][0])[:10]
    last_date_str = str(df["Date"][-1])[:10]
    assert first_date_str == meta["start_date"]
    assert last_date_str == meta["end_date"]

    # Verify zero nulls across all columns
    for col in df.columns:
        assert df[col].null_count() == 0, f"Null values detected in column {col}"

def test_option_2_modern_data_ingestion(ingestor):
    """Verify Modern 5-regime horizon data ingestion."""
    meta = HORIZON_METADATA[HORIZON_OPTION_2_ID]
    df = ingestor.fetch_market_data(start_date=meta["start_date"], end_date=meta["end_date"], use_cache=False)

    assert isinstance(df, pl.DataFrame)
    assert len(df) > 2500
    assert "SPY" in df.columns
    assert "Shiller_CAPE" in df.columns

def test_dashboard_state_horizon_switching(tmp_path):
    """Verify DashboardState properly switches between 50-year and modern horizons."""
    state = DashboardState(load_data=False)
    state.ingestor = DataIngestor(cache_dir=tmp_path / "cache")

    # Load Option 1 (50-Year Multi-Decade)
    state.load_data(horizon_id=HORIZON_OPTION_1_ID)
    assert state.selected_horizon_id == HORIZON_OPTION_1_ID
    assert "Drawdown_Probability" in state.df.columns
    len_opt1 = len(state.df)

    # Load Option 2 (Modern)
    state.load_data(horizon_id=HORIZON_OPTION_2_ID)
    assert state.selected_horizon_id == HORIZON_OPTION_2_ID
    assert "Drawdown_Probability" in state.df.columns
    len_opt2 = len(state.df)

    # Option 1 (50 years) must have substantially more rows than Option 2 (~11 years)
    assert len_opt1 > len_opt2
    assert len_opt1 > 10000

