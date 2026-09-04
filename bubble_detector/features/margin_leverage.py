"""
Systemic Margin Leverage & Credit Exhaustion Indicator Module.
==============================================================

Economic Foundations & Financial Instability Theory:
----------------------------------------------------
In leveraged macroeconomic regimes, asset price expansions become structurally coupled
with credit growth. As formulated by Hyman Minsky (1986, 1992) and formalized by
John Geanakoplos (2010) in "The Leverage Cycle":
- In the expansionary phase ("Hedge" to "Speculative" finance), collateral asset values rise,
  loosening broker margin lending constraints and expanding investor purchasing power.
- Investors deploy leverage to bid up risk assets, creating an endogenous feedback loop
  wherein rising collateral prices justify further credit expansion.
- Vulnerability occurs at the inflection point ("Leverage Exhaustion"): when margin borrowing
  accelerates far faster than underlying equity capitalization, excess borrowing capacity
  ("margin credit") is completely exhausted.
- At the peak ("Ponzi" regime), even modest adverse price shocks trigger regulatory maintenance
  margin calls under FINRA Rule 4210. Clearing brokers involuntarily liquidate customer
  collateral into an illiquid market, triggering a cascading fire-sale spiral.

Formulation & Metric Mathematics:
---------------------------------
1. YoY Margin Debt Growth Rate:
   Measures medium-term structural debt accumulation over 1 trading year (252 business days):
       \\Delta_{YoY}(t) = \\left(\\frac{\\text{MD}_t - \\text{MD}_{t-252}}{\\text{MD}_{t-252}}\\right) \\times 100\\%
   Empirically, sustained \\Delta_{YoY} > +30\\% preceded the 2000 Dot-Com crash and the 2007–2008 GFC.

2. Short-Term Debt Velocity:
   Measures instantaneous rate of borrowing change over a 20-day horizon (~1 calendar month):
       v_{MD}(t) = \\left(\\frac{\\text{MD}_t - \\text{MD}_{t-20}}{\\text{MD}_{t-20}}\\right) \\times 100\\%

3. Leverage Exhaustion Gap:
   Quantifies the divergence between debt growth velocity and collateral asset appreciation:
       \\text{Gap}_t = v_{MD}(t) - v_{SPY}(t)
   where v_{SPY}(t) is the 20-day percentage change in the benchmark S&P 500 ETF.
   - Positive Gap (Gap > 0): Debt is expanding faster than asset wealth, indicating overleveraged speculation.
   - Negative Gap (Gap < 0): Collateral wealth is growing faster than leverage, indicating organic deleveraging.

4. Calibrated Margin Exhaustion Score:
   Discretized risk index mapping the exhaustion gap into an institutional risk score [0, 1]:
       \\text{Score}_t = \\begin{cases}
       0.9 & \\text{if } \\text{Gap}_t > 5.0\\% \\quad (\\text{Severe Fire-Sale Liquidation Risk}) \\\\
       0.7 & \\text{if } 2.0\\% < \\text{Gap}_t \\le 5.0\\% \\quad (\\text{Elevated Fragility}) \\\\
       0.5 & \\text{if } 0.0\\% < \\text{Gap}_t \\le 2.0\\% \\quad (\\text{Moderate Expansion}) \\\\
       0.2 & \\text{if } \\text{Gap}_t \\le 0.0\\% \\quad (\\text{Deleveraged / Stable Regime})
       \\end{cases}

Canonical Module Binding:
-------------------------
This module serves as the primary canonical alias for `bubble_detector.features.leverage`,
providing 100% interoperability across autonomous agent workflows and research pipelines.
"""

from typing import Optional
import polars as pl
from bubble_detector.features.leverage import compute_margin_leverage_metrics

__all__ = ["compute_margin_leverage_metrics"]
