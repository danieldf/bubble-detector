<!-- ### -->
<!-- # BeGiN ImplementationOverview_DDFv100.md -->
<!-- ### -->

# Overview of Completed Implementation: Multidimensional Market Bubble Detector

## 1. System, Configuration & Date Horizons (`config.py` & `date_horizons.py`):

* `RotatingFileHandler` logging to `bubble_detector.log` with structured log records.
* Domain exception hierarchy (`DataFetchError`, `IndicatorComputationError`, `ModelTrainingError`, `ValidationError`).
* Standard 2026 macroeconomic baseline constants (CAPE 41.37, Buffett Indicator 218.1%, Margin Debt $1.416T).
* **Dynamic Calendar-Anchored 50-Year Engine (`date_horizons.py`)**: Extracted into a standalone leaf module with zero circular dependencies. Dynamically computes a rolling 50-year date range from execution date (e.g. 1976–2026, 13,045 trading days across 9 historical crash regimes).

## 2. UI & Accessibility Engine (`ui_theme.py`):

* *WCAG 2.2 AA Contrast Compliance:* Programmatic contrast ratio checker (`calculate_contrast_ratio` & `is_wcag_aa_compliant`).
* *Dyslexia-Friendly Typography:* `SF Pro Text` / `Inter` / `OpenDyslexic` font stack, `0.015em` letter-spacing, `1.5` line-height, strictly prohibiting decorative fonts.
* *8px Grid Rhythm:* Base spacing tokens (`4px`, `8px`, `16px`, `24px`, `32px`, `48px`).
* *iOS 13+ Visual Styling:* Inset card containers with 14px rounded corners and subtle shadows.
* *Light & Dark Theme Switcher:* Dynamic CSS variable engine with automatic system preference detection and Plotly template synchronization (`plotly_white` vs `plotly_dark`).
* *Standardized Right-Flushed Legends:* All Plotly visualization figures across Tabs 1 through 6 utilize right-flushed vertical legends (`orientation="v", x=1.01, y=1.0, margin.r=230`), eliminating trace obscuration.

## 3. Data Ingestion & Storage (`ingestor.py`):

* `DataIngestor` class fetching historical price data via `yfinance` with fallback synthetic time series.
* *Polars Schema Downcasting:* Enforces `float32` / `int32` memory-efficient types.
* *Missing Value Imputation:* Forward fill (`fill_null(strategy="forward")`) for daily price data and cubic spline interpolation for low-frequency macro data (GDP, Margin Debt).
* *Parquet Storage:* Local caching to `.parquet` files for optimized I/O.
* *Exchange Holiday Forward-Fill Integrity:* In `ingestor.py`, exchange prices are forward-filled within each ticker active lifetime prior to calling `combine_first(df_synth)`, preventing synthetic single-day holiday return dips.

## 4. Quantitative Indicator Modules (`features/` & `features/utils.py`):

* `technicals.py`: Moving Averages (MA20/50/200), RSI (14-day), Bollinger Bands (20-day, 2 std dev), 20-day rolling volatility.
* `macro_valuation.py`: Shiller CAPE (41.37), Payout-Adjusted CAPE (P-CAPE), Buffett Indicator (218.1% GDP), and Z-score metrics.
* `leverage.py`: FINRA Margin Debt YoY growth, velocity, and excess debt capacity ("Margin Credit Exhaustion Score").
* `econometric.py`: PSY procedure (GSADF t-statistic) with GPT fundamental decomposition to filter out false positive bubble signals on AI CapEx ($754B).
* `topology.py`: Takens delay coordinate embedding, Topological Data Analysis (TDA) persistence landscape $L_2$ norm, and Morlet wavelet scaleogram complexity score.
* `options_vol.py`: VIX contango term structure slope, CBOE SKEW index tail risk alert (>145), Dispersion (DSPX) vs Implied Correlation (COR3M), and OVX / VIX cross-asset volatility ratio.
* `utils.py`: Centralized pure-mathematical utilities providing `normalize_tda_indicator` (dynamic re-scaling to $[0.80, 7.00]$), `calculate_adf_stat`, and `takens_embedding`.

## 5. Machine Learning Model (`structural_breaks.py`):

* `StructuralBreakPredictor` using `RobustScaler` preprocessing (subtracts median, scales by IQR).
* Gradient Boosting classifier predicting forward 20-day drawdown risk ($y_t = \mathbb{I}\{(P_{t+20} - P_t)/P_t < -0.05\}$).
* *Expanding-Window Walk-Forward Cross-Validation:* `TimeSeriesSplit` cross-validation with an explicit **20-day purge embargo** (`train_idx[:-embargo]`) between train and validation splits.
* *Terminal Masking:* Masks the terminal 20 unobservable rows during training to guarantee zero forward target leakage.

## 6. Macro Mahalanobis Distance Engine (`regime_mahalanobis.py`):

* *Method 1 Mahalanobis Distance ($D_M$):* 15-dimensional regularized covariance distance using Tikhonov ridge regularization $\mathbf{\Sigma} + 10^{-2}\mathbf{I}$ with a $12.0\sigma$ numerical clipping ceiling.
* *Strictly Causal Expanding-Window Z-Scores:* During warm-up periods, rolling z-score standardization uses strictly causal expanding-window mean and standard deviation (`s.expanding(min_periods=1)`), completely eliminating lookahead leakage from 2026 into 1976.
* *Singularity Elimination:* Enforces a minimum sample threshold $N \ge \max(30, 2k) = 30$ before inverting rolling covariance matrices, eliminating artificial early-window $12.0\sigma$ crisis ceiling spikes.
* *Empirical Bubble Probability:* Non-parametric percentile rank $P_{\text{bubble}}(t) = \text{rank}(D_M(t)) / N_t \in [0, 1]$.
* *Dynamic Equity Exposure:* Continuous sizing rule $w_{\text{equity}}(t) = \text{clip}(1.0 - 0.80 P_{\text{bubble}}(t), 0.20, 1.00)$ with a mandatory 20% defensive liquidity floor.

## 7. Interactive Dashboards & Dual-Runtime Architecture:

* **Server-Side NiceGUI Application (`dashboard.py`)**: Powered by FastAPI and Polars multithreaded vectorized execution, featuring 6 interactive tabs:
  1. Macro Valuation Dashboard
  2. Systemic Leverage Dashboard
  3. Econometric Bubble Dashboard
  4. Sentiment & Volatility Dashboard
  5. Sector-Specific Health Dashboard
  6. Macro Mahalanobis Distance Dashboard
* **Client-Side WebAssembly Application (`panel_dashboard.py` / `build/index.html`)**: Compiled via HoloViz Panel and Pyodide, executing 100% in-browser with zero server requirements.
* *Runtime Unicode Emoji Rendering:* Uses ASCII-safe `chr()` string identifiers (`chr(0x1F3DB)`, `chr(0x1F3AF)`, `chr(0x1F4C5)`) to ensure authentic emoji rendering in browser WebAssembly sandboxes without unquoted escape artifacts (`U0001f3db️`).

## 8. Adversarial Red Team Hardening & Automated Verification:

* Comprehensive Red Team audit resolved all 9 vulnerabilities (RT-01 through RT-09).
* Full test suite expanded to **37 automated unit and integration tests passing with 100% success rate** (`pytest tests/ -v`).

<!-- ### -->
<!-- # eNd ImplementationOverview_DDFv100.md -->
<!-- ### -->
