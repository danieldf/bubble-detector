"""
Technical Indicators & Momentum Oscillators Module.
===================================================

Mathematical Foundations:
-------------------------
Technical indicators quantify short-to-intermediate price momentum, trend persistence,
and mean-reverting volatility boundaries. In bubble regime detection, indicators like
Bollinger Band %B and RSI serve as high-frequency momentum filters that signal when
macroeconomic or econometric deviations are translating into speculative buying climaxes.

1. Trend Moving Averages:
   For window lengths k \\in {20, 50, 200}:
       \\text{MA}_k(t) = \\frac{1}{k} \\sum_{i=0}^{k-1} P_{t-i}
   Moving average crosses (e.g. MA50 crossing MA200) identify structural regime transitions
   between secular bull and bear markets (Golden Cross / Death Cross).

2. Bollinger Bands & %B Dispersion (Bollinger, 1983):
   Given 20-day rolling sample standard deviation \\sigma_{20}(t):
       \\text{Upper}_t = \\text{MA}_{20}(t) + 2 \\cdot \\sigma_{20}(t)
       \\text{Lower}_t = \\text{MA}_{20}(t) - 2 \\cdot \\sigma_{20}(t)
   The normalized Bollinger %B indicator measures price location relative to the bands:
       \\%B_t = \\frac{P_t - \\text{MA}_{20}(t)}{2 \\cdot \\sigma_{20}(t) + \\epsilon}
   Interpretation:
       \\%B_t > 1.0 \\implies \\text{Upper band breakout (extreme momentum / exhaustion)}
       \\%B_t < 0.0 \\implies \\text{Lower band breakdown (panic capitulation)}

3. Relative Strength Index (Wilder, 1978):
   Decomposes single-period price change \\Delta P_t = P_t - P_{t-1} into directional gains and losses:
       U_t = \\max(\\Delta P_t, 0), \\quad D_t = \\max(-\\Delta P_t, 0)
   Over a 14-day rolling window:
       \\text{RS}_t = \\frac{\\overline{U}_{14}(t)}{\\overline{D}_{14}(t) + \\epsilon}
       \\text{RSI}_t = 100 - \\frac{100}{1 + \\text{RS}_t} \\in [0, 100]

4. Realized Annualized Volatility:
   Computed from single-day percentage returns R_t = \\frac{P_t - P_{t-1}}{P_{t-1}}:
       \\sigma_{20D}(t) = \\sqrt{252} \\cdot \\sqrt{\\frac{1}{19} \\sum_{i=0}^{19} (R_{t-i} - \\overline{R})^2}

All calculations are evaluated via native Polars multithreaded SIMD expressions.
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
    Append technical momentum, trend, and volatility indicators to the input Polars DataFrame.

    Parameters
    ----------
    df : pl.DataFrame
        Input DataFrame containing target price column.
    target_col : str
        Target asset ticker column name (default: SP500_TICKER / 'SPY').
    rsi_window : int
        Lookback window for Wilder's RSI (default: 14 trading days).
    bb_window : int
        Lookback window for Bollinger Bands SMA and volatility (default: 20 trading days).
    bb_std : float
        Standard deviation multiplier for band width (default: 2.0).

    Returns
    -------
    pl.DataFrame
        Enriched DataFrame with MA20, MA50, MA200, BB_Upper, BB_Lower, BB_PctB,
        RSI14, and Vol20D columns.
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
