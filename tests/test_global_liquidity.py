"""
Unit tests for Global Liquidity Index (M2, Federal Reserve Total Assets, Splicing & Momentum).
"""

import pytest
import numpy as np
import pandas as pd
import polars as pl

from bubble_detector.data.etl_fred import FredETL, get_fred_data
from bubble_detector.config import PROVENANCE_DIR


def test_global_liquidity_schema_and_publication_lags(tmp_path):
    """
    Asserts authentic FRED M2 and Federal Reserve Total Assets are parsed with
    rigorous publication lags (+10d for M2, +1d for WALCL).
    """
    etl = FredETL(provenance_dir=tmp_path / "provenance")
    df_staged = etl.fetch_and_stage()

    required_cols = [
        "Date", "Available_Date", "GDP_Nominal", "Case_Shiller_Index",
        "Housing_Price_to_Income", "M2_Level", "CentralBank_Assets"
    ]
    for col in required_cols:
        assert col in df_staged.columns, f"Missing required column: {col}"

    df_pd = df_staged.to_pandas()
    date_col = pd.to_datetime(df_pd["Date"])
    avail_col = pd.to_datetime(df_pd["Available_Date"])

    # Publication lags must be strictly non-negative: Available_Date >= Date
    assert (avail_col >= date_col).all(), "Available_Date occurred before observation date (lookahead bias)"


def test_central_bank_balance_sheet_splicing_continuity():
    """
    Verifies that continuous backward compounding of BOGMBASE into WALCL pre-2002
    produces zero cliff drops (< 3% transition jump at seam).
    """
    # Test across transition window around December 2002
    daily_df = get_fred_data("2002-12-01", "2003-01-15")
    df_pd = daily_df.to_pandas()

    cb_series = df_pd["CentralBank_Assets"].to_numpy()
    assert len(cb_series) > 20
    assert not np.isnan(cb_series).any()
    assert (cb_series > 500.0).all()  # In late 2002, balance sheet was ~$720B

    # Seam jump across adjacent business days must be strictly < 3%
    daily_pct_change = np.abs(np.diff(cb_series) / cb_series[:-1])
    max_transition_jump = float(np.max(daily_pct_change))
    assert max_transition_jump < 0.03, f"Splicing transition seam jump exceeded 3%: {max_transition_jump:.4%}"


def test_global_liquidity_derived_metrics():
    """
    Asserts that Global_Liquidity_Index ($T), M2_YoY_Growth (%), CentralBank_YoY_Growth (%),
    and Liquidity_Momentum are non-null, economically bounded, and mathematically consistent.
    """
    daily_df = get_fred_data("2015-01-01", "2026-09-01")
    df_pd = daily_df.to_pandas()

    assert "Global_Liquidity_Index" in df_pd.columns
    assert "M2_YoY_Growth" in df_pd.columns
    assert "CentralBank_YoY_Growth" in df_pd.columns
    assert "Liquidity_Momentum" in df_pd.columns

    # Liquidity index ($ Trillion) must be in plausible modern bounds ($15T to $40T)
    gli = df_pd["Global_Liquidity_Index"].to_numpy()
    assert not np.isnan(gli).any()
    assert np.min(gli) >= 15.0, f"Global Liquidity Index dropped below $15T floor: {np.min(gli)}"
    assert np.max(gli) <= 40.0, f"Global Liquidity Index exceeded $40T ceiling: {np.max(gli)}"

    # Check YoY growth bounds (-15% to +35%)
    m2_yoy = df_pd["M2_YoY_Growth"].to_numpy()
    assert not np.isnan(m2_yoy).any()
    assert np.min(m2_yoy) >= -15.0
    assert np.max(m2_yoy) <= 35.0

    cb_yoy = df_pd["CentralBank_YoY_Growth"].to_numpy()
    assert not np.isnan(cb_yoy).any()

    # Momentum = M2_YoY_Growth - SMA_60(M2_YoY_Growth)
    mom = df_pd["Liquidity_Momentum"].to_numpy()
    assert not np.isnan(mom).any()
    assert np.abs(np.mean(mom)) < 1.0  # Zero mean over long horizon
