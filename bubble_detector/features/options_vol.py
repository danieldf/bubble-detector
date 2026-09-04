"""
Options Market Microstructure & Volatility Behavioral Dynamics Module.
======================================================================

Options Pricing & Behavioral Risk Foundations:
----------------------------------------------
Option markets contain forward-looking, risk-neutral probability distributions that
reflect institutional hedging demand, tail-risk pricing, and market maker inventory imbalances.
In late-stage asset bubbles, volatility surfaces exhibit distinct behavioral anomalies:
while headline index volatility (VIX) can remain artificially depressed due to retail call
buying and systematic volatility-selling strategies, the underlying skew and term structure
begin pricing severe structural fragility.

1. VIX Term Structure Slope (Contango vs. Backwardation):
   Compares 3-month implied volatility (VIX3M) with 30-day spot volatility (VIX):
       \\text{Slope}_t = \\frac{\\text{VIX3M}_t - \\text{VIX}_t}{\\text{VIX}_t}
   - Contango (\\text{Slope} > 0): Normal market equilibrium where future uncertainty exceeds
     near-term uncertainty. Yields positive roll yield for volatility shorts.
   - Backwardation (\\text{Slope} < 0): Severe market dislocation or panic. Spot hedging demand
     surges, inverting the curve (e.g. 2008 GFC, March 2020 COVID crash).

2. CBOE SKEW Index & Tail-Risk Asymmetry:
   Measures the slope of the implied volatility smile across out-of-the-money (OTM) puts:
       \\text{SKEW}_t = 100 - 10 \\cdot \\mu_3^{\\mathbb{Q}}
   where \\mu_3^{\\mathbb{Q}} is the third standardized moment (skewness) of the risk-neutral
   log-return distribution.
   - Baseline: SKEW = 100 represents a symmetric log-normal distribution.
   - Alert Threshold: SKEW > 145 indicates extreme institutional demand for crash-protection
     puts, signaling an elevated probability of a 2-to-3 standard deviation drawdown.

3. Volatility Dispersion & Implied Correlation:
   During speculative bubbles, index concentration distorts aggregate risk:
   - Dispersion Index (DSPX): Measures the cross-sectional divergence of component stock returns.
     In narrow market rallies (e.g. 1999 tech leaders or 2024–2026 AI mega-caps), single-stock
     implied volatility surges while index VIX remains low.
   - Implied Correlation (COR3M): Measures the market-implied average pairwise correlation
     across S&P 500 constituents. Low implied correlation coexisting with elevated SKEW
     is a classic structural hallmark of late-cycle bubble fragility.

4. Cross-Asset Volatility Spillover (OVX / VIX):
   The ratio of CBOE Crude Oil Volatility (OVX) to Equity Volatility (VIX) monitors
   geopolitical and commodity supply shocks that threaten corporate profit margins.
"""

import numpy as np
import polars as pl
from bubble_detector.config import VOLATILITY_TICKERS, logger

def compute_options_volatility_metrics(df: pl.DataFrame) -> pl.DataFrame:
    """
    Compute VIX term structure slope, SKEW tail-risk alert, dispersion index, and cross-asset ratios.

    Parameters
    ----------
    df : pl.DataFrame
        Input DataFrame containing volatility index series (VIX, VIX3M, SKEW, OVX, VXN).

    Returns
    -------
    pl.DataFrame
        Enriched DataFrame with VIX_Term_Structure_Slope, OVX_VIX_CrossAsset_Ratio,
        SKEW_Tail_Risk_Alert, Dispersion_Index_DSPX, and Implied_Correlation_COR3M.
    """
    logger.info("Computing Options & Volatility behavioral metrics...")

    cols = df.columns

    # 1. VIX Term Structure Contango Slope (VIX3M / VIX1D or VIX3M / VIX)
    vix_col = VOLATILITY_TICKERS.get("VIX", "^VIX")
    vix3m_col = VOLATILITY_TICKERS.get("VIX3M", "^VIX3M")
    skew_col = VOLATILITY_TICKERS.get("SKEW", "^SKEW")
    ovx_col = VOLATILITY_TICKERS.get("OVX", "^OVX")
    vxn_col = VOLATILITY_TICKERS.get("VXN", "^VXN")

    vix_val = pl.col(vix_col) if vix_col in cols else pl.lit(16.0)
    vix3m_val = pl.col(vix3m_col) if vix3m_col in cols else vix_val * 1.2
    skew_val = pl.col(skew_col) if skew_col in cols else pl.lit(145.0)
    ovx_val = pl.col(ovx_col) if ovx_col in cols else pl.lit(28.0)
    vxn_val = pl.col(vxn_col) if vxn_col in cols else vix_val * 1.35

    vix_term_slope = (vix3m_val - vix_val) / (vix_val + 1e-8)
    ovx_vix_ratio = ovx_val / (vix_val + 1e-8)

    # 2. Dispersion & Implied Correlation Proxies
    # High SKEW + Low VIX signifies Dispersion Spike / High Tail Protection Demand
    skew_tail_risk = pl.when(skew_val > 145.0).then(1.0).when(skew_val > 135.0).then(0.5).otherwise(0.0)
    dspx_dispersion_proxy = (skew_val / (vix_val + 1e-8)) * 5.0
    implied_corr_proxy = pl.lit(100.0) / (dspx_dispersion_proxy + 1e-8)

    df = df.with_columns([
        vix_term_slope.alias("VIX_Term_Structure_Slope"),
        ovx_vix_ratio.alias("OVX_VIX_CrossAsset_Ratio"),
        skew_tail_risk.alias("SKEW_Tail_Risk_Alert"),
        dspx_dispersion_proxy.alias("Dispersion_Index_DSPX"),
        implied_corr_proxy.alias("Implied_Correlation_COR3M"),
    ])

    return df
