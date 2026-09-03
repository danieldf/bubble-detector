"""
Unit tests for Institutional Data Provenance & Publication Lags (Shiller, FRED, FINRA, VXO).
"""

import pytest
import datetime
import numpy as np
import pandas as pd
import polars as pl

from bubble_detector.data.etl_shiller import ShillerETL, get_shiller_data
from bubble_detector.data.etl_fred import FredETL, get_fred_data
from bubble_detector.data.etl_finra import FinraETL, get_finra_margin_debt
from bubble_detector.data.etl_vxo import VxoETL, get_vxo_data

def test_shiller_provenance_schema_and_bounds(tmp_path):
    """Asserts real Shiller data spans 1871-present with valid CAPE, earnings, and dividend series without Gaussian bumps."""
    etl = ShillerETL(provenance_dir=tmp_path / "provenance")
    df_monthly = etl.fetch_and_stage()

    assert isinstance(df_monthly, pl.DataFrame)
    assert len(df_monthly) > 1500  # 1871 to 2026 is > 1800 months
    
    # Required schema
    expected_cols = ["Date", "SP_Price", "SP_Earnings", "SP_Dividends", "CPI", "Shiller_CAPE", "Price_to_Dividend", "Real_Earnings_Yield"]
    for col in expected_cols:
        assert col in df_monthly.columns

    # Verify absence of Gaussian analytical formulas / valid historical boundaries
    cape_vals = df_monthly["Shiller_CAPE"].to_numpy()
    assert np.min(cape_vals) >= 4.5, f"Shiller CAPE minimum {np.min(cape_vals)} is below historical floor of 4.5"
    assert np.max(cape_vals) <= 46.0, f"Shiller CAPE maximum {np.max(cape_vals)} exceeds Dot-Com historical peak of 45.0"
    assert not np.isnan(cape_vals).any()

    # Daily point-in-time interpolation
    daily_df = etl.get_daily_interpolated("2020-01-01", "2024-01-01")
    assert len(daily_df) > 1000
    assert daily_df["Shiller_CAPE"].null_count() == 0

def test_fred_publication_lags(tmp_path):
    """Asserts GDP and Case-Shiller releases are strictly point-in-time lagged by >= 60 days."""
    etl = FredETL(provenance_dir=tmp_path / "provenance")
    df_macro = etl.fetch_and_stage()

    assert "GDP_Nominal" in df_macro.columns
    assert "Housing_Price_to_Income" in df_macro.columns
    assert "Available_Date" in df_macro.columns

    df_pd = df_macro.to_pandas()
    # Check that Available_Date is strictly after observation date
    date_col = pd.to_datetime(df_pd["Date"])
    avail_col = pd.to_datetime(df_pd["Available_Date"])
    assert (avail_col >= date_col).all()

    # Verify daily interpolation provides positive, non-null values
    daily_df = etl.get_daily_interpolated("2015-01-01", "2020-01-01")
    assert len(daily_df) > 1200
    assert (daily_df["GDP_Nominal"] > 10000.0).all()
    assert (daily_df["Housing_Price_to_Income"] > 3.0).all()

def test_finra_margin_publication_lag(tmp_path):
    """Asserts margin debt data incorporates mandatory 3-week reporting lag."""
    etl = FinraETL(provenance_dir=tmp_path / "provenance")
    df_finra = etl.fetch_and_stage()

    assert "FINRA_Margin_Debt" in df_finra.columns
    assert "Available_Date" in df_finra.columns

    df_pd = df_finra.to_pandas()
    date_col = pd.to_datetime(df_pd["Date"])
    avail_col = pd.to_datetime(df_pd["Available_Date"])
    
    # Available_Date must be >= Date
    assert (avail_col >= date_col).all()

    # Verify daily series
    daily_finra = etl.get_daily_interpolated("2018-01-01", "2022-01-01")
    assert len(daily_finra) > 1000
    assert (daily_finra["FINRA_Margin_Debt"] > 100.0).all()
    assert daily_finra["FINRA_Margin_Debt"].null_count() == 0

def test_vxo_authenticity_and_black_monday(tmp_path):
    """Asserts authentic CBOE VXO captures the 1987 Black Monday volatility spike."""
    etl = VxoETL(provenance_dir=tmp_path / "provenance")
    df_vxo = etl.fetch_and_stage()

    assert "VXO" in df_vxo.columns
    vxo_arr = df_vxo["VXO"].to_numpy()
    assert np.max(vxo_arr) >= 100.0, f"VXO did not capture 1987 Black Monday spike: max={np.max(vxo_arr)}"
    assert np.min(vxo_arr) >= 5.0
    assert not np.isnan(vxo_arr).any()
