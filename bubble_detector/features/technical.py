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

Canonical Module Binding:
-------------------------
This module serves as the primary canonical alias for `bubble_detector.features.technicals`,
providing 100% interoperability across autonomous agent workflows and research pipelines.
"""

from typing import Optional
import polars as pl
from bubble_detector.features.technicals import compute_technical_indicators

__all__ = ["compute_technical_indicators"]
