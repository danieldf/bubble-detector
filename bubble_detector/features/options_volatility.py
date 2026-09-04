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

Canonical Module Binding:
-------------------------
This module serves as the primary canonical alias for `bubble_detector.features.options_vol`,
providing 100% interoperability across autonomous agent workflows and research pipelines.
"""

from typing import Optional
import polars as pl
from bubble_detector.features.options_vol import compute_options_volatility_metrics

__all__ = ["compute_options_volatility_metrics"]
