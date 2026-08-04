"""
Technical Indicators Module.

Computes rolling moving averages, Relative Strength Index (RSI), Bollinger Bands,
and rolling volatility metrics using Polars expressions.
"""

import numpy as np
import polars as pl
from bubble_detector.config import SP500_TICKER, IndicatorComputationError, logger

def compute_technical_indicators(
    df: pl.DataFrame,
    target_col: str = SP500_TICKER,
    rsi_window: int = 14,
    bb_window: int = 20,
    bb_std: float = 2.0
) -> pl.DataFrame:
    """
    Appends technical indicators (RSI, Bollinger Bands, Moving Averages 20/50/200)
    to the input Polars DataFrame.
    """
    if target_col not in df.columns:
        raise IndicatorComputationError(f"Target column '{target_col}' not present in DataFrame.")

    logger.info(f"Computing technical indicators for '{target_col}'...")

    # Calculate Moving Averages
    df = df.with_columns([
        pl.col(target_col).rolling_mean(window_size=20).alias(f"{target_col}_MA20"),
        pl.col(target_col).rolling_mean(window_size=50).alias(f"{target_col}_MA50"),
        pl.col(target_col).rolling_mean(window_size=200).alias(f"{target_col}_MA200"),
    ])

    # Calculate Bollinger Bands
    ma20 = pl.col(f"{target_col}_MA20")
    std20 = pl.col(target_col).rolling_std(window_size=bb_window)

    df = df.with_columns([
        (ma20 + bb_std * std20).alias(f"{target_col}_BB_Upper"),
        (ma20 - bb_std * std20).alias(f"{target_col}_BB_Lower"),
        ((pl.col(target_col) - ma20) / (2.0 * std20 + 1e-8)).alias(f"{target_col}_BB_PctB"),
    ])

    # Calculate RSI
    delta = pl.col(target_col).diff()
    gain = pl.when(delta > 0).then(delta).otherwise(0.0)
    loss = pl.when(delta < 0).then(-delta).otherwise(0.0)

    avg_gain = gain.rolling_mean(window_size=rsi_window)
    avg_loss = loss.rolling_mean(window_size=rsi_window)

    rs = avg_gain / (avg_loss + 1e-8)
    rsi = 100.0 - (100.0 / (1.0 + rs))

    df = df.with_columns(rsi.alias(f"{target_col}_RSI14"))

    # Rolling Volatility (20-day annualized)
    returns = pl.col(target_col).pct_change()
    roll_vol = returns.rolling_std(window_size=20) * np.sqrt(252.0)
    df = df.with_columns(roll_vol.alias(f"{target_col}_Vol20D"))

    return df
