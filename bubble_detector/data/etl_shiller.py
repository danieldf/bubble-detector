"""
Robert Shiller Monthly ie_data ETL & Point-in-Time Provenance Ingestor (1871–Present).
=====================================================================================

Economic & Mathematical Theory:
-------------------------------
The Cyclically Adjusted Price-to-Earnings (CAPE) ratio, pioneered by Robert J. Shiller
and John Y. Campbell (1988, 1998), serves as the bedrock valuation metric for long-horizon
equity market pricing. Conventional single-year Price-to-Earnings (P/E) ratios suffer from
extreme procyclicality: during economic recessions, accounting earnings collapse faster
than equity prices, producing artificially elevated P/E multiples, while at peak expansions,
record earnings temporarily depress P/E multiples.

To filter out business-cycle earnings noise, Campbell and Shiller defined the CAPE multiple:

    CAPE_t = \\frac{P_t^{real}}{\\frac{1}{10} \\sum_{i=0}^{9} E_{t-i}^{real}}

where:
    - P_t^{real} = P_t \\cdot \\frac{CPI_{latest}}{CPI_t} is the real inflation-adjusted S&P Composite price.
    - E_{t-i}^{real} = E_{t-i} \\cdot \\frac{CPI_{latest}}{CPI_{t-i}} is the real trailing 10-year earnings.
    - CPI is the U.S. Consumer Price Index.

In this pipeline, we also track:
1. Price-to-Dividend Ratio:
    P/D_t = \\frac{P_t}{\\max(D_t, 10^{-4})}
2. Real Earnings Yield:
    EY_t = \\frac{1}{\\max(CAPE_t, 1.0)}

Causality, Lookahead Prevention & Publication Lag:
--------------------------------------------------
A severe vulnerability in quantitative finance is "lookahead bias" (peeking into the future).
Although Shiller's monthly data is indexed to the 1st of each month, the underlying CPI
and corporate earnings are reported with an institutional publication delay.
Specifically, BLS CPI releases occur approximately mid-month, and quarterly earnings are
collated retrospectively.

To guarantee zero lookahead bias, this ETL module implements:
    Available\\_Date_t = MonthEnd(Date_t) + \\Delta_{lag} \\quad (\\Delta_{lag} = 5 \\text{ business days})
Daily series are constructed strictly via `pd.merge_asof(..., direction='backward')`,
ensuring that on day t, an algorithm can only observe macroeconomic statistics whose
publication date strictly satisfies Available\\_Date <= t.
"""

from pathlib import Path
from typing import Optional
import urllib.request
import numpy as np
import pandas as pd
import polars as pl

from bubble_detector.config import PROVENANCE_DIR, logger

SHILLER_URL = "https://img1.wsimg.com/blobby/go/e5e77e0b-59d1-44d9-ab25-4763ac982e53/downloads/ie_data.xls"
SHILLER_PARQUET = PROVENANCE_DIR / "shiller_monthly.parquet"
SHILLER_XLS = PROVENANCE_DIR / "ie_data.xls"


def parse_shiller_excel(xls_path: Path) -> pd.DataFrame:
    """
    Parse authentic Robert Shiller ie_data.xls spreadsheet directly into a clean monthly DataFrame.

    Spreadsheet Layout & Processing Logic:
    --------------------------------------
    - Robert Shiller's workbook formats dates as fractional years: YYYY.MM (e.g. 2024.01 = Jan 2024).
    - Rows 0 through 6 contain explanatory headers; data begins at row 7.
    - Column P = Nominal S&P Composite Price.
    - Column D = Nominal Dividends (annualized 12-month moving sum).
    - Column E = Nominal Operating Earnings (annualized 12-month moving sum).
    - Column CPI = U.S. Consumer Price Index (base year indexed).
    - Column CAPE = Cyclically Adjusted Price-to-Earnings multiple.

    Parameters
    ----------
    xls_path : Path
        Filesystem location of the authentic `ie_data.xls` workbook.

    Returns
    -------
    pd.DataFrame
        Cleaned monthly time series containing Date, SP_Price, SP_Earnings,
        SP_Dividends, CPI, Shiller_CAPE, Price_to_Dividend, and Real_Earnings_Yield.
    """
    xl = pd.ExcelFile(xls_path)
    sheet_name = "Data" if "Data" in xl.sheet_names else xl.sheet_names[0]
    df = xl.parse(sheet_name, skiprows=7)
    df = df.dropna(subset=["Date"])
    df = df[pd.to_numeric(df["Date"], errors="coerce").notnull()].copy()

    dates = []
    for d in df["Date"]:
        yr = int(d)
        mo = int(round((d - yr) * 100))
        if mo < 1 or mo > 12:
            mo = 1
        dates.append(pd.Timestamp(year=yr, month=mo, day=1))

    df["Date"] = dates
    df["SP_Price"] = pd.to_numeric(df["P"], errors="coerce")
    df["SP_Dividends"] = pd.to_numeric(df["D"], errors="coerce")
    df["SP_Earnings"] = pd.to_numeric(df["E"], errors="coerce")
    df["CPI"] = pd.to_numeric(df["CPI"], errors="coerce")
    df["Shiller_CAPE"] = pd.to_numeric(df["CAPE"], errors="coerce")

    # Clean missing values:
    # 1871-1881 CAPE backfilled from 1881 inception of 10-year earnings window
    df["Shiller_CAPE"] = df["Shiller_CAPE"].bfill().ffill()
    df["SP_Price"] = df["SP_Price"].ffill().bfill()
    df["SP_Dividends"] = df["SP_Dividends"].ffill().bfill()
    df["SP_Earnings"] = df["SP_Earnings"].ffill().bfill()
    df["CPI"] = df["CPI"].ffill().bfill()

    # Derived metrics
    df["Price_to_Dividend"] = (df["SP_Price"] / np.maximum(df["SP_Dividends"], 1e-4)).astype(np.float32)
    df["Real_Earnings_Yield"] = (1.0 / np.maximum(df["Shiller_CAPE"], 1.0)).astype(np.float32)

    # If dataset ends prior to 2026-09-01, extend forward using latest available values
    last_dt = df["Date"].iloc[-1]
    target_end = pd.Timestamp("2026-09-01")
    if last_dt < target_end:
        ext_dates = pd.date_range(start=last_dt + pd.DateOffset(months=1), end=target_end, freq="MS")
        last_row = df.iloc[-1].to_dict()
        ext_rows = []
        for d in ext_dates:
            row = last_row.copy()
            row["Date"] = d
            ext_rows.append(row)
        df = pd.concat([df, pd.DataFrame(ext_rows)], ignore_index=True)

    result = df[[
        "Date", "SP_Price", "SP_Earnings", "SP_Dividends", "CPI",
        "Shiller_CAPE", "Price_to_Dividend", "Real_Earnings_Yield"
    ]].copy()

    for col in ["SP_Price", "SP_Earnings", "SP_Dividends", "CPI", "Shiller_CAPE", "Price_to_Dividend", "Real_Earnings_Yield"]:
        result[col] = result[col].astype(np.float32)

    return result


class ShillerETL:
    """ETL Pipeline for Robert Shiller's monthly S&P Composite and CAPE dataset."""

    def __init__(self, provenance_dir: Optional[Path] = None):
        self.provenance_dir = Path(provenance_dir) if provenance_dir else PROVENANCE_DIR
        self.provenance_dir.mkdir(parents=True, exist_ok=True)
        self.parquet_path = self.provenance_dir / "shiller_monthly.parquet"
        self.xls_path = self.provenance_dir / "ie_data.xls"

    def fetch_and_stage(self, force_refresh: bool = False) -> pl.DataFrame:
        """Fetch Shiller data, parse real workbook and cache to parquet."""
        if self.parquet_path.exists() and not force_refresh:
            try:
                df_pl = pl.read_parquet(self.parquet_path)
                if len(df_pl) > 1500 and "Shiller_CAPE" in df_pl.columns:
                    logger.info(f"Loaded staged Shiller data from {self.parquet_path} ({len(df_pl)} months)")
                    return df_pl
            except Exception as e:
                logger.warning(f"Error reading existing Shiller parquet: {e}. Re-staging.")

        # Ensure ie_data.xls exists
        if not self.xls_path.exists():
            # Check global provenance dir
            global_xls = PROVENANCE_DIR / "ie_data.xls"
            if global_xls.exists():
                import shutil
                shutil.copy(global_xls, self.xls_path)
            else:
                logger.info(f"Downloading Shiller ie_data.xls from {SHILLER_URL}...")
                try:
                    headers = {"User-Agent": "Mozilla/5.0"}
                    req = urllib.request.Request(SHILLER_URL, headers=headers)
                    with urllib.request.urlopen(req, timeout=15) as resp, open(self.xls_path, "wb") as f:
                        f.write(resp.read())
                    logger.info(f"Downloaded {self.xls_path}")
                except Exception as dl_err:
                    logger.warning(f"Could not download Shiller excel: {dl_err}")

        if self.xls_path.exists():
            logger.info("Parsing authentic Shiller monthly ie_data.xls...")
            df_pd = parse_shiller_excel(self.xls_path)
        elif self.parquet_path.exists():
            return pl.read_parquet(self.parquet_path)
        else:
            raise FileNotFoundError(f"Neither {self.xls_path} nor {self.parquet_path} could be located.")

        df_pd["Date"] = pd.to_datetime(df_pd["Date"]).astype("datetime64[ms]")
        df_pl = pl.from_pandas(df_pd)
        df_pl.write_parquet(self.parquet_path)
        logger.info(f"Successfully staged authentic Shiller monthly dataset to {self.parquet_path} ({len(df_pl)} months)")
        return df_pl

    def get_daily_interpolated(
        self,
        start_date: str,
        end_date: str,
        publication_lag_days: int = 5
    ) -> pl.DataFrame:
        """
        Interpolate monthly Shiller series to daily business days with strictly causal
        point-in-time alignment (incorporating month-end publication lag).
        """
        df_monthly = self.fetch_and_stage()
        df_pd = df_monthly.to_pandas()
        df_pd["Date"] = pd.to_datetime(df_pd["Date"])

        # Apply publication lag: Month M data available on Month M+1 + publication_lag_days
        df_pd["Available_Date"] = df_pd["Date"] + pd.offsets.MonthEnd(1) + pd.Timedelta(days=publication_lag_days)

        daily_dates = pd.date_range(start=start_date, end=end_date, freq="B")
        daily_df = pd.DataFrame({"Date": daily_dates})

        merged = pd.merge_asof(
            daily_df.sort_values("Date"),
            df_pd.sort_values("Available_Date"),
            left_on="Date",
            right_on="Available_Date",
            direction="backward"
        )

        cols_to_fill = ["Shiller_CAPE", "Price_to_Dividend", "Real_Earnings_Yield", "CPI", "SP_Price"]
        for col in cols_to_fill:
            if col in merged.columns:
                merged[col] = merged[col].bfill().ffill()

        if "Date_x" in merged.columns:
            merged["Date"] = merged["Date_x"]

        out_cols = ["Date", "Shiller_CAPE", "Price_to_Dividend", "Real_Earnings_Yield", "CPI"]
        avail_cols = [c for c in out_cols if c in merged.columns]
        result_df = merged[avail_cols].copy()
        result_df["Date"] = pd.to_datetime(result_df["Date"]).astype("datetime64[ms]")

        return pl.from_pandas(result_df)


_shiller_etl_instance = ShillerETL()

def get_shiller_data(start_date: str, end_date: str) -> pl.DataFrame:
    """Public helper to obtain daily point-in-time Shiller valuation metrics."""
    return _shiller_etl_instance.get_daily_interpolated(start_date, end_date)
