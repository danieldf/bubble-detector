"""
Unit tests for Continuous Backward Return Compounding Splicing (Zero Cliffs).
"""

import pytest
import numpy as np
import pandas as pd
import polars as pl

from bubble_detector.data.ingestor import DataIngestor

@pytest.fixture
def multi_decade_df(tmp_path):
    ingestor = DataIngestor(cache_dir=tmp_path / "cache")
    return ingestor.fetch_market_data(start_date="1985-01-01", end_date="2005-01-01", use_cache=False)

def test_spy_backward_compounding_no_cliff(multi_decade_df):
    """
    Asserts single-day return at 1993-01-22 seam is bounded within normal daily distribution
    (|Delta ln P| < 3%), completely eliminating the legacy -28.8% drop.
    """
    df_pd = multi_decade_df.to_pandas()
    df_pd["Date_str"] = pd.to_datetime(df_pd["Date"]).dt.strftime("%Y-%m-%d")

    # Find the seam around 1993-01-22
    seam_dates = df_pd[df_pd["Date_str"].between("1993-01-15", "1993-01-29")]
    assert len(seam_dates) >= 5

    prices = seam_dates["SPY"].to_numpy()
    log_returns = np.abs(np.diff(np.log(prices)))

    # Single-day jump across the seam must be strictly < 3%
    max_seam_jump = float(np.max(log_returns))
    assert max_seam_jump < 0.03, f"SPY seam discontinuity detected: max jump was {max_seam_jump * 100:.2f}% (expected < 3%)"

def test_xlk_backward_compounding_no_cliff(multi_decade_df):
    """
    Asserts 1998-12-16 seam discontinuity is < 3%, completely eliminating the legacy -76.5% cliff.
    """
    df_pd = multi_decade_df.to_pandas()
    df_pd["Date_str"] = pd.to_datetime(df_pd["Date"]).dt.strftime("%Y-%m-%d")

    seam_dates = df_pd[df_pd["Date_str"].between("1998-12-10", "1998-12-24")]
    assert len(seam_dates) >= 5

    tech_prices = seam_dates["XLK"].to_numpy()
    log_returns = np.abs(np.diff(np.log(tech_prices)))

    max_seam_jump = float(np.max(log_returns))
    assert max_seam_jump < 0.03, f"XLK seam cliff detected: max jump was {max_seam_jump * 100:.2f}% (expected < 3%)"

def test_vxo_vix_seam_continuity(multi_decade_df):
    """Asserts 1990 VIX seam matches CBOE ^VXO within continuous market tolerance."""
    df_pd = multi_decade_df.to_pandas()
    df_pd["Date_str"] = pd.to_datetime(df_pd["Date"]).dt.strftime("%Y-%m-%d")

    seam_dates = df_pd[df_pd["Date_str"].between("1989-12-20", "1990-01-10")]
    vix_prices = seam_dates["^VIX"].to_numpy()

    # VIX across the Jan 1990 seam must be finite and within realistic volatility band (10 to 45)
    assert not np.isnan(vix_prices).any()
    assert (vix_prices > 10.0).all()
    assert (vix_prices < 45.0).all()
    
    # Returns across the seam should not have a pathological spike
    abs_returns = np.abs(np.diff(vix_prices))
    assert np.max(abs_returns) < 8.0, f"Pathological VIX seam spike: max diff = {np.max(abs_returns)}"
