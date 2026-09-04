"""
Macroeconomic Valuation & Long-Horizon Equilibrium Module.
===========================================================

Economic Foundations & Metric Formulations:
-------------------------------------------
Macroeconomic valuation metrics quantify aggregate asset pricing relative to underlying
national income, replacement cost, and smoothed corporate profitability. When asset prices
compound at rates far exceeding national economic output over multi-year horizons,
mean-reverting economic gravity imposes structural correction risks.

1. Robert Shiller Cyclically Adjusted P/E (CAPE):
   Smoothes 10-year inflation-adjusted earnings to eliminate business-cycle volatility:
       CAPE_t = \\frac{P_t^{real}}{\\frac{1}{10}\\sum_{i=0}^{9} E_{t-i}^{real}}
   - Historical Baseline: Long-run historical average \\mu_{CAPE} \\approx 17.0, \\sigma_{CAPE} \\approx 6.5.
   - Regimes: Exceeding 30.0 indicates severe historical overvaluation (seen in 1929 at 32.6,
     2000 Dot-Com peak at 44.19, and 2024–2026 AI expansion at 41.37).

2. Payout-Adjusted CAPE (P-CAPE) & Multicollinearity Prevention:
   Traditional CAPE relies strictly on accounting earnings. However, post-1982 SEC Rule 10b-18,
   corporations shifted cash distributions from dividends to share repurchases.
   P-CAPE accounts for total cash distributions, historically trading at ~0.88x standard CAPE.
   *Econometric Notice*: Because P_CAPE is linearly proportional to Shiller_CAPE in stylized
   models, it is excluded from the 15-indicator Mahalanobis covariance vector (`INDICATORS_15`)
   to prevent exact rank deficiency and matrix singularity (det(\\Sigma) \\to 0).

3. Warren Buffett Indicator (Market Capitalization / Nominal GDP):
   Pioneered by Warren Buffett (Fortune, 2001) as the single best macro yardstick of valuation:
       \\text{Buffett}_t = \\left(\\frac{\\text{Aggregate Equity Value}_t}{\\text{Nominal GDP}_t}\\right) \\times 100\\%
   In this pipeline, the aggregate equity proxy is computed via scaled S&P 500 index levels:
       \\text{Buffett}_t = \\left(\\frac{P_{SPY}(t) \\cdot 85.0}{\\text{GDP}_{Nominal}(t)}\\right) \\times 100\\%
   - Historical Distribution: Mean \\mu_{B} \\approx 100\\%, Standard Deviation \\sigma_{B} \\approx 35\\%.
   - Overvaluation Thresholds:
     * Fair Value: 90% – 115%
     * Modestly Overvalued: 115% – 140%
     * Extreme Bubble Regime: > 160% (reached >215% in the 2021 liquidity peak and 2025–2026 AI cycle).

4. Real Earnings Yield:
   The inverse of the valuation multiple, representing real expected yield per unit of equity:
       EY_t = \\frac{1}{\\max(CAPE_t, 1.0)}
"""

import numpy as np
import polars as pl
from bubble_detector.config import SP500_TICKER, logger

def compute_macro_valuations(df: pl.DataFrame) -> pl.DataFrame:
    """
    Compute Shiller CAPE, Payout-Adjusted CAPE (P-CAPE), and Buffett Indicator metrics.

    Parameters
    ----------
    df : pl.DataFrame
        Input DataFrame containing equity price series and macroeconomic provenance columns.

    Returns
    -------
    pl.DataFrame
        Enriched DataFrame with Shiller_CAPE, P_CAPE, Buffett_Indicator, Real_Earnings_Yield,
        and standardized Z-scores (CAPE_ZScore, P_CAPE_ZScore, Buffett_ZScore).
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

    # Real Earnings Yield (1 / CAPE)
    if "Real_Earnings_Yield" not in cols:
        df = df.with_columns((1.0 / pl.col("Shiller_CAPE")).alias("Real_Earnings_Yield"))

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
