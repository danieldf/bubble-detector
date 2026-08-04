"""
Unit tests for DataIngestor module.
"""

import pytest
import polars as pl
from bubble_detector.data.ingestor import DataIngestor

@pytest.fixture
def ingestor(tmp_path):
    return DataIngestor(cache_dir=tmp_path / "cache")

def test_fetch_market_data_schema_and_downcasting(ingestor):
    df = ingestor.fetch_market_data(start_date="2024-01-01", end_date="2024-06-01", use_cache=False)

    assert isinstance(df, pl.DataFrame)
    assert len(df) > 0
    assert "Date" in df.columns
    assert "SPY" in df.columns
    assert "FINRA_Margin_Debt" in df.columns
    assert "Shiller_CAPE" in df.columns
    assert "Housing_Price_to_Income" in df.columns

    # Verify Polars schema downcasting (float32 / int32)
    assert df["SPY"].dtype == pl.Float32
    assert df["FINRA_Margin_Debt"].dtype == pl.Float32
    assert df["Shiller_CAPE"].dtype == pl.Float32

def test_parquet_caching(ingestor):
    # First fetch writes cache
    df1 = ingestor.fetch_market_data(start_date="2024-01-01", end_date="2024-03-01", use_cache=True)
    # Second fetch reads from cache
    df2 = ingestor.fetch_market_data(start_date="2024-01-01", end_date="2024-03-01", use_cache=True)

    assert len(df1) == len(df2)
    assert df1.columns == df2.columns
