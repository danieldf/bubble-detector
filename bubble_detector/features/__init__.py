"""
Quantitative Feature Engineering & Mathematical Signal Processing Subpackage.
=============================================================================

Architectural Overview & Indicator Ecosystem:
---------------------------------------------
This subpackage transforms raw historical prices, macroeconomic aggregates, and options
surfaces into stationary, standardized quantitative signals for systemic risk modeling:

1. Technical Momentum & Trend (`technicals.py`, alias `technical.py`):
   - Vectorized moving averages (MA20, MA50, MA200).
   - Bollinger %B dispersion measuring price location relative to 2-sigma volatility bands.
   - J. Welles Wilder Relative Strength Index (RSI14) momentum oscillator.
   - 20-day annualized realized volatility.

2. Macroeconomic Equilibrium & Valuation (`macro_valuation.py`):
   - Campbell-Shiller Cyclically Adjusted P/E (CAPE) smoothed across 10 years of earnings.
   - Payout-Adjusted CAPE (P-CAPE) incorporating corporate buybacks and dividend payout ratios.
   - Warren Buffett Indicator (Wilshire / S&P Market Capitalization to Nominal GDP).
   - Historical standardized Z-scores (zero lookahead).

3. Systemic Leverage & Margin Credit (`leverage.py`, alias `margin_leverage.py`):
   - FINRA Rule 4521 & NYSE customer margin debt YoY growth.
   - 20-day margin debt velocity.
   - Leverage exhaustion gap (debt velocity divergence from equity appreciation).
   - Calibrated 4-state margin credit exhaustion risk score.

4. Econometric Explosive Root Diagnostics (`econometric.py`):
   - Canonical Phillips, Shi & Yu (PSY, 2015) Generalized Supremum ADF (GSADF).
   - General-Purpose Technology (GPT) structural cointegration filtering AI CapEx shocks.

5. Geometric Phase Space & Topological Complexity (`topology.py`):
   - Takens delay-coordinate embedding (m=3, tau=2).
   - Vietoris-Rips persistent homology (H0 connected components, H1 topological loops).
   - Bubenik persistence landscape L2 norm and Morlet continuous wavelet transform energy.

6. Options Microstructure & Behavioral Skew (`options_vol.py`, alias `options_volatility.py`):
   - VIX term structure contango/backwardation slope.
   - CBOE SKEW index (>145) risk-neutral tail risk alert.
   - CBOE Dispersion Index (DSPX) and implied pairwise correlation (COR3M).
   - OVX / VIX cross-asset commodity-equity volatility spillover ratio.

7. Centralized Mathematical Utilities (`utils.py`):
   - Causal expanding-window dynamic scaling (`normalize_tda_indicator`).
   - Ordinary least-squares ADF test statistic calculation via pseudo-inversion.
   - Delay embedding vector transformations.
"""

from .technicals import compute_technical_indicators
from .macro_valuation import compute_macro_valuations
from .leverage import compute_margin_leverage_metrics
from .econometric import compute_gsadf_gpt_decomposition
from .topology import compute_tda_wavelet_complexity
from .options_vol import compute_options_volatility_metrics
from .utils import normalize_tda_indicator, calculate_adf_stat, takens_embedding, lttb_downsample

# Canonical aliases for agent accessibility and backward compatibility
from . import leverage as margin_leverage
from . import options_vol as options_volatility
from . import technicals as technical

__all__ = [
    "compute_technical_indicators",
    "compute_macro_valuations",
    "compute_margin_leverage_metrics",
    "compute_gsadf_gpt_decomposition",
    "compute_tda_wavelet_complexity",
    "compute_options_volatility_metrics",
    "normalize_tda_indicator",
    "calculate_adf_stat",
    "takens_embedding",
    "lttb_downsample",
    "margin_leverage",
    "options_volatility",
    "technical",
]
