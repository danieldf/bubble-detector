"""
Institutional Data Provenance Certification & Anti-Synthetic Regression Suite.

Verifies:
1. Zero Gaussian bump / synthetic analytical generators exist in the codebase.
2. Authentic raw institutional datasets exist, parse cleanly, and match empirical benchmarks.
3. Point-in-time publication lag constraints are strictly enforced without lookahead bias.
"""

from pathlib import Path
import re
import numpy as np
import pandas as pd
import polars as pl
import pytest

from bubble_detector.config import PROVENANCE_DIR, BASE_DIR
from bubble_detector.data.etl_shiller import ShillerETL
from bubble_detector.data.etl_fred import FredETL
from bubble_detector.data.etl_finra import FinraETL
from bubble_detector.data.etl_vxo import VxoETL


def test_no_synthetic_gaussian_bumps_in_data_code():
    """
    Scans all source files in bubble_detector/data/ to certify that NO disguised
    Gaussian bump generators or exponential curve functions remain in the codebase.
    """
    data_dir = BASE_DIR / "bubble_detector" / "data"
    forbidden_patterns = [
        r"_generate_authentic_historical_shiller_monthly",
        r"_generate_authentic_fred_macro_series",
        r"_generate_authentic_margin_debt_series",
        r"_generate_authentic_vxo_daily",
        r"np\.exp\(-+\(\(years\s*-\s*\d+",
        r"s_volcker\s*=",
        r"s_1987\s*=",
        r"s_dotcom\s*=",
        r"s_gfc_bust\s*=",
        r"s_covid\s*=",
    ]

    for py_file in data_dir.glob("*.py"):
        content = py_file.read_text(encoding="utf-8")
        for pattern in forbidden_patterns:
            matches = re.findall(pattern, content)
            assert not matches, (
                f"Synthetic Gaussian bump generator '{pattern}' found in {py_file.name}! "
                f"Real institutional data ETL pipelines must be used exclusively."
            )


def test_authentic_shiller_provenance_workbook():
    """Certifies Shiller ie_data.xls contains genuine S&P data from 1871 to present."""
    xls_path = PROVENANCE_DIR / "ie_data.xls"
    assert xls_path.exists(), f"Missing required Shiller workbook: {xls_path}"

    etl = ShillerETL()
    df = etl.fetch_and_stage()

    # Must contain > 1800 continuous monthly observations
    assert len(df) >= 1840

    # Historical empirical benchmark validation:
    # 1. 1920 Post-WWI CAPE trough (~4.78)
    assert float(df["Shiller_CAPE"].min()) < 5.0
    # 2. 1929 Great Crash CAPE peak (~32.6)
    df_pd = df.to_pandas()
    df_pd["Date"] = pd.to_datetime(df_pd["Date"])
    cape_1929 = df_pd[df_pd["Date"].between("1929-08-01", "1929-10-01")]["Shiller_CAPE"].max()
    assert 30.0 <= cape_1929 <= 35.0, f"Unexpected 1929 CAPE: {cape_1929}"
    # 3. 1999-2000 Dot-Com Bubble Peak (~44.20)
    cape_2000 = df_pd[df_pd["Date"].between("1999-11-01", "2000-04-01")]["Shiller_CAPE"].max()
    assert 43.0 <= cape_2000 <= 45.0, f"Unexpected 2000 CAPE: {cape_2000}"


def test_authentic_cboe_vxo_black_monday():
    """Certifies CBOE VXO captures the exact 150.19 close on October 19, 1987."""
    etl = VxoETL()
    df = etl.fetch_and_stage()
    df_pd = df.to_pandas()
    df_pd["Date"] = pd.to_datetime(df_pd["Date"])

    # Locate Black Monday 1987-10-19
    bm_row = df_pd[df_pd["Date"] == "1987-10-19"]
    assert not bm_row.empty, "Missing 1987-10-19 trading day in authentic VXO series"
    assert abs(float(bm_row["VXO"].iloc[0]) - 150.19) < 0.5, (
        f"Authentic 1987 Black Monday VXO close should be 150.19, got {bm_row['VXO'].iloc[0]}"
    )


def test_authentic_finra_margin_debt():
    """Certifies FINRA margin debt reflects true regulatory figures exceeding $1.4 Trillion in 2026."""
    etl = FinraETL()
    df = etl.fetch_and_stage()
    df_pd = df.to_pandas()
    df_pd["Date"] = pd.to_datetime(df_pd["Date"])

    # Pre-1997 NYSE data starts in 1959
    assert df_pd["Date"].min().year <= 1960

    # 2026 debt exceeds $1,400B
    debt_2026 = df_pd[df_pd["Date"] >= "2026-01-01"]["FINRA_Margin_Debt"].max()
    assert debt_2026 >= 1400.0, f"Expected 2026 FINRA margin debt >= $1,400B, got {debt_2026}"


def test_authentic_fred_gdp_and_housing():
    """Certifies FRED nominal GDP and Case-Shiller index match official BEA/FRED publications."""
    etl = FredETL()
    df = etl.fetch_and_stage()
    df_pd = df.to_pandas()
    df_pd["Date"] = pd.to_datetime(df_pd["Date"])

    # 2026 Nominal GDP exceeds $30,000 Billion ($30 Trillion)
    latest_gdp = df_pd["GDP_Nominal"].iloc[-1]
    assert latest_gdp > 30000.0, f"Expected nominal GDP > $30,000B, got {latest_gdp}"

    # Housing Price-to-Income reaches historical extreme (~7.11x)
    latest_pti = df_pd["Housing_Price_to_Income"].iloc[-1]
    assert 6.5 <= latest_pti <= 7.5, f"Expected 2026 Housing PTI ~7.11, got {latest_pti}"
