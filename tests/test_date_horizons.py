"""
Unit tests for Date Range Horizons (Option 1 vs Option 2).
"""

import pytest
import polars as pl
from bubble_detector.config import (
    HORIZON_METADATA, HORIZON_OPTION_1_ID, HORIZON_OPTION_2_ID
)
from bubble_detector.data.ingestor import DataIngestor
from bubble_detector.ui.dashboard import DashboardState

@pytest.fixture
def ingestor(tmp_path):
    return DataIngestor(cache_dir=tmp_path / "cache")

def test_option_1_data_ingestion(ingestor):
    meta = HORIZON_METADATA[HORIZON_OPTION_1_ID]
    df = ingestor.fetch_market_data(start_date=meta["start_date"], end_date=meta["end_date"], use_cache=False)

    assert isinstance(df, pl.DataFrame)
    assert len(df) > 0
    assert "SPY" in df.columns
    assert "Shiller_CAPE" in df.columns
    assert "Housing_Price_to_Income" in df.columns

def test_option_2_data_ingestion(ingestor):
    meta = HORIZON_METADATA[HORIZON_OPTION_2_ID]
    df = ingestor.fetch_market_data(start_date=meta["start_date"], end_date=meta["end_date"], use_cache=False)

    assert isinstance(df, pl.DataFrame)
    # Option 2 (1998-2026) should have substantially more rows than Option 1 (2015-2026)
    assert len(df) > 4000
    assert "SPY" in df.columns
    assert "Shiller_CAPE" in df.columns

def test_dashboard_state_horizon_switching(tmp_path):
    state = DashboardState(load_data=False)
    state.ingestor = DataIngestor(cache_dir=tmp_path / "cache")

    # Load Option 1
    state.load_data(horizon_id=HORIZON_OPTION_1_ID)
    assert state.selected_horizon_id == HORIZON_OPTION_1_ID
    assert "Drawdown_Probability" in state.df.columns
    len_opt1 = len(state.df)

    # Load Option 2
    state.load_data(horizon_id=HORIZON_OPTION_2_ID)
    assert state.selected_horizon_id == HORIZON_OPTION_2_ID
    assert "Drawdown_Probability" in state.df.columns
    len_opt2 = len(state.df)

    assert len_opt2 > len_opt1
