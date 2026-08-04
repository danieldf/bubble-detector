"""
Macro Valuation Indicators Module.

Computes Shiller CAPE, Payout-Adjusted CAPE (P-CAPE), and the Buffett Indicator (Market Cap / GDP).
"""

import numpy as np
import polars as pl
from bubble_detector.config import SP500_TICKER, logger

def compute_macro_valuations(df: pl.DataFrame) -> pl.DataFrame:
    """
    Compute Shiller CAPE, Payout-Adjusted CAPE (P-CAPE), and Buffett Indicator metrics.
    """
    logger.info("Computing Macro Valuation indicators...")

    # Ensure required columns exist
    cols = df.columns
    if "Shiller_CAPE" not in cols:
        cape = pl.Series("Shiller_CAPE", np.full(len(df), 41.37, dtype=np.float32))
        df = df.with_columns(cape)

    if "P_CAPE" not in cols:
        p_cape = pl.col("Shiller_CAPE") * 0.88
        df = df.with_columns(p_cape.alias("P_CAPE"))

    # Buffett Indicator = (SPY Price * Scaling Factor / GDP) * 100
    if "GDP_Nominal" in cols and SP500_TICKER in cols:
        # Approximate S&P 500 Market Cap ratio to Nominal GDP
        buffett = (pl.col(SP500_TICKER) * 85.0 / pl.col("GDP_Nominal")) * 100.0
        df = df.with_columns(buffett.alias("Buffett_Indicator"))
    else:
        df = df.with_columns(pl.Series("Buffett_Indicator", np.full(len(df), 218.1, dtype=np.float32)))

    # Historical Z-Scores for CAPE & Buffett Indicator
    cape_mean = 17.0
    cape_std = 6.5
    buffett_mean = 100.0
    buffett_std = 35.0

    df = df.with_columns([
        ((pl.col("Shiller_CAPE") - cape_mean) / cape_std).alias("CAPE_ZScore"),
        ((pl.col("P_CAPE") - (cape_mean * 0.88)) / (cape_std * 0.88)).alias("P_CAPE_ZScore"),
        ((pl.col("Buffett_Indicator") - buffett_mean) / buffett_std).alias("Buffett_ZScore"),
    ])

    return df
