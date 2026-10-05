"""
Tech Exuberance Score & Dual-Condition Integration Module.
=========================================================

Macroeconomic & Statistical Foundations:
----------------------------------------
Asset market speculative manias reach their terminal instability phase when equity outperformance
decouples from underlying central bank liquidity expansion while simultaneously exhibiting
mathematical signatures of explosive autoregressive behavior (Phillips, Shi & Yu, 2015)
and log-periodic power-law singularities (Sornette, 2003).

This module implements the formal Dual-Condition Exuberance Engine:

1. Condition 1 (Macro Condition: Liquidity Decoupling):
   - M2 Growth Slowing:
         Delta_YoY_M2 < SMA_60(Delta_YoY_M2)  OR  Liquidity_Momentum < 0  OR  Delta_YoY_M2 < 0
   - Tech Outperformance:
         (XLK / SPY > SMA_50(XLK / SPY))  AND  (Delta_20d(XLK / SPY) > 0)
   - Macro Trigger:
         Condition_Macro = M2_Slowing AND Tech_Outperformance

2. Condition 2 (Statistical Condition: Mathematical Singularity):
   - Recursive Backward Supremum ADF (BSADF) Extreme:
         (BSADF_Stat > 1.45) OR ((BSADF_Stat >= 1.0) AND (BSADF_Stat >= BSADF_90th_Percentile))
   - Log-Periodic Power Law Singularity (LPPLS) Extreme:
         (LPPLS_Confidence >= 0.50) OR ((LPPLS_Confidence >= 0.20) AND (LPPLS_Confidence >= LPPLS_90th_Percentile))
   - Statistical Trigger:
         Condition_Statistical = BSADF_Extreme OR LPPLS_Extreme

🚨 Conjoint Tech Exuberance Signal:
   Tech_Exuberance_Signal = Condition_Macro AND Condition_Statistical
"""

from typing import List, Tuple
import numpy as np
import pandas as pd
import polars as pl
from bubble_detector.config import SP500_TICKER, SECTOR_TICKERS, logger


def compute_tech_exuberance_metrics(df: pl.DataFrame) -> pl.DataFrame:
    """
    Computes tech outperformance ratio (XLK / SPY), Macro Condition,
    Statistical Condition, and the Conjoint Tech Exuberance Signal.

    Parameters
    ----------
    df : pl.DataFrame
        DataFrame containing SPY, XLK, M2_YoY_Growth, Liquidity_Momentum,
        BSADF_Stat, BSADF_90th_Percentile, LPPLS_Confidence, LPPLS_90th_Percentile.

    Returns
    -------
    pl.DataFrame
        Augmented DataFrame with XLK_SPY_Ratio, Condition_Macro,
        Condition_Statistical, and Tech_Exuberance_Signal.
    """
    logger.info("Computing Tech Exuberance dual-condition indicators and conjoint signal...")

    df_pd = df.to_pandas()
    n = len(df_pd)

    # 1. Tech Outperformance Ratio: XLK / SPY
    tech_col = SECTOR_TICKERS.get("Technology", "XLK")
    spy_col = SP500_TICKER if SP500_TICKER in df_pd.columns else "SPY"

    if tech_col in df_pd.columns and spy_col in df_pd.columns:
        spy_vals = np.maximum(df_pd[spy_col].to_numpy(dtype=np.float64), 1e-4)
        xlk_vals = np.maximum(df_pd[tech_col].to_numpy(dtype=np.float64), 1e-4)
        ratio = xlk_vals / spy_vals
    else:
        ratio = np.ones(n, dtype=np.float64)

    s_ratio = pd.Series(ratio)
    # Strictly causal rolling window statistics (min_periods=1) with zero lookahead bias
    ratio_sma50 = s_ratio.rolling(50, min_periods=1).mean()
    ratio_d20 = (s_ratio - s_ratio.shift(20)).fillna(0.0)

    tech_outperformance = (s_ratio > ratio_sma50) & (ratio_d20 > 0.0)

    # 2. Condition 1 (Macro Condition: M2 Slowing & Tech Outperformance)
    if "M2_YoY_Growth" in df_pd.columns:
        m2_yoy = df_pd["M2_YoY_Growth"]
    else:
        m2_yoy = pd.Series(np.zeros(n))

    m2_sma60 = m2_yoy.rolling(60, min_periods=1).mean()
    if "Liquidity_Momentum" in df_pd.columns:
        liq_mom = df_pd["Liquidity_Momentum"]
    else:
        liq_mom = m2_yoy - m2_sma60

    m2_slowing = (m2_yoy < m2_sma60) | (liq_mom < 0.0) | (m2_yoy < 0.0)

    cond_macro = (m2_slowing & tech_outperformance).astype(np.int32).to_numpy()

    # 3. Condition 2 (Statistical Condition: BSADF or LPPLS Extreme)
    if "BSADF_Stat" in df_pd.columns:
        bsadf_stat = df_pd["BSADF_Stat"].to_numpy()
    elif "GSADF_Stat" in df_pd.columns:
        bsadf_stat = df_pd["GSADF_Stat"].to_numpy()
    else:
        bsadf_stat = np.zeros(n)

    if "BSADF_90th_Percentile" in df_pd.columns:
        bsadf_p90 = df_pd["BSADF_90th_Percentile"].to_numpy()
    else:
        bsadf_p90 = pd.Series(bsadf_stat).rolling(252, min_periods=1).quantile(0.90).fillna(0.0).to_numpy()

    if "LPPLS_Confidence" in df_pd.columns:
        lppls_ci = df_pd["LPPLS_Confidence"].to_numpy()
    else:
        lppls_ci = np.zeros(n)

    if "LPPLS_90th_Percentile" in df_pd.columns:
        lppls_p90 = df_pd["LPPLS_90th_Percentile"].to_numpy()
    else:
        lppls_p90 = pd.Series(lppls_ci).rolling(252, min_periods=1).quantile(0.90).fillna(0.0).to_numpy()

    bsadf_extreme = (bsadf_stat > 1.45) | ((bsadf_stat >= 1.0) & (bsadf_stat >= bsadf_p90))
    lppls_extreme = (lppls_ci >= 0.50) | ((lppls_ci >= 0.20) & (lppls_ci >= lppls_p90))

    cond_statistical = (bsadf_extreme | lppls_extreme).astype(np.int32)

    # 4. Conjoint Tech Exuberance Signal
    conjoint_signal = (cond_macro & cond_statistical).astype(np.int32)

    df = df.with_columns([
        pl.Series("XLK_SPY_Ratio", ratio.astype(np.float32)),
        pl.Series("Condition_Macro", cond_macro),
        pl.Series("Condition_Statistical", cond_statistical),
        pl.Series("Tech_Exuberance_Signal", conjoint_signal),
    ])

    return df


def compute_exuberance_spans(df: pl.DataFrame) -> List[Tuple[str, str]]:
    """
    Extract contiguous start and end date intervals where Tech_Exuberance_Signal is active.

    Parameters
    ----------
    df : pl.DataFrame
        DataFrame with 'Date' and 'Tech_Exuberance_Signal' columns.

    Returns
    -------
    List[Tuple[str, str]]
        List of (start_date_str, end_date_str) tuples for Plotly add_vrect highlighting.
    """
    if "Tech_Exuberance_Signal" not in df.columns or "Date" not in df.columns:
        return []

    dates = [str(d)[:10] for d in df["Date"].to_list()]
    signals = df["Tech_Exuberance_Signal"].to_numpy()

    spans: List[Tuple[str, str]] = []
    in_span = False
    start_date = ""

    for i in range(len(signals)):
        if signals[i] == 1 and not in_span:
            in_span = True
            start_date = dates[i]
        elif signals[i] == 0 and in_span:
            in_span = False
            end_date = dates[i - 1]
            spans.append((start_date, end_date))

    if in_span:
        spans.append((start_date, dates[-1]))

    return spans
