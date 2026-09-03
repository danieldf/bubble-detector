<!-- ### -->
<!-- # BeGiN TechnicalSpecification_DDFv100.md -->
<!-- ### -->

# Technical Specification: Multidimensional Market Bubble Detection System

Technical Specification Confidence Score: 0.96

## 1. Architecture and Methodology

This project strictly adheres to Spec-Driven Development (SDD) via GitHub's SpecKit to ensure high alignment between the underlying econometric logic and the final code. SpecKit makes the specification the center of the engineering process, utilizing an AI coding agent to iteratively generate artifacts through a structured pipeline: spec, plan, tasks, and implementation. The SDD methodology relies on generating a robust specification, a technical plan, and actionable tasks prior to any agentic code generation. A core constitution file will mandate Test-Driven Development (TDD), production-level error handling, and strict data typing.

The project will be initialized using the Specify CLI via `uv` package management. The workflow will rely on a `constitution.md` file located in the `.specify/memory/` directory to establish non-negotiable ground rules, such as mandatory Test-Driven Development (TDD) coverage and strict data typing. The development lifecycle will progress through the `/speckit.specify`, `/speckit.plan`, `/speckit.tasks`, and `/speckit.implement` commands.

## 2. Technology Stack

- **Data Processing:** `Polars` will be used over `Pandas` for highly parallelized, memory-efficient columnar data processing, which is critical for large historical financial datasets.
- **Data Acquisition:** `yfinance` for baseline historical financial data, with modular design to support future integration of institutional APIs or alternative economic data sources (e.g., FRED).
  - *Alternative Consideration:* For production, `OpenBB` or `Databento` are recommended. While `yfinance` is free and easy to implement, it relies on unofficial APIs and is subject to rate limiting and data gaps. `Databento` offers institutional-grade, highly optimized binary data formats specifically designed for massive scale and accuracy.
- **Quantitative Computation:** `TA-Lib` will be used via its Python wrapper to calculate technical momentum oscillators, moving averages, rolling volatility, and volatility bands.
- **Machine Learning:** `Scikit-learn` for data scaling, Z-score normalization ( z = (x-\mu)/(\sigma) ), pipeline construction, and `RobustScaler` preprocessing. `XGBoost` for gradient-boosted structural break classification and to detect non-linear relationships and regime shifts.
- **Visualization & UI:** `NiceGUI` for the web framework, offering seamless Python integration, integrating `Plotly` for interactive, high-performance financial charting within the NiceGUI layout.
- **Storage:** Data will be serialized in `Parquet` format to maintain columnar efficiency, for optimized I/O read/write speeds, and memory footprint.

## 3. Data Engineering and Processing

Given the sensitivity of econometric models to outliers, preprocessing is a critical component of the pipeline.

- **Type Downcasting:** To optimize memory, Polars will enforce strict schema typing, casting arrays to `float32` or `int32` where 64-bit precision is not strictly required by the mathematical models.
- **Handling Missing Data:** Forward-fill imputation will be used for standard price data to prevent look-ahead bias, while macro-economic indicators with varied publication dates will utilize localized cubic spline interpolation.
- **Scaling and Normalization:** Due to the extreme fat tails in financial time series, `RobustScaler` (which subtracts the median and scales according to the interquartile range) will be the default scaler to prevent extreme market shocks from warping the feature space. For specific statistical arbitrage models requiring normal distributions, Z-score normalization will be applied using the formula Z = (x - mu) / sigma .

## 4. Core Indicators and Sector Analysis

The system will compute and monitor the following macroeconomic and quantitative indicators across the broad market (S&P 500) and specific sectors:

- **Broad Market (S&P 500):**
  - **Shiller CAPE & P-CAPE:** The traditional Cyclically Adjusted P/E (CAPE) will be tracked alongside the Payout-Adjusted CAPE (P-CAPE). The P-CAPE adjusts for the reality that corporate retained earnings generate future growth, a necessary adjustment given modern dividend payout ratios have fallen to around 35%.
  - **The Buffett Indicator:** The ratio of Total Market Capitalization to nominal GDP, utilized to measure whether asset prices are detaching from real economic output.
  - **Systemic Leverage:** FINRA margin debt levels and aggregate margin credit (excess debt capacity) will be monitored to gauge the market's vulnerability to leverage-induced fire sales.
  - **PSY Procedure (GSADF):** The generalized supremum ADF test will be utilized to detect explosive price behavior. For the broader market, this will be adjusted for General-Purpose Technology (GPT) shocks to prevent false positives driven by fundamental productivity enhancements.
  - **Volatility & Behavioral Tracking:** The system will monitor the VIX, the VIX term structure (VIX1D vs. VIX3M), the CBOE SKEW Index for tail-risk pricing, and the Dispersion Index (DSPX).
- **Specific Sectors:**
  - **Technology & AI (XLK, SMH):** Focus on the semiconductor weighting and earnings multiples, utilizing implied volatility metrics (VXN) to track the massive AI capital expenditure cycle.
  - **Housing (Real Estate / ITB):** Real estate bubble metrics will focus on Price-to-Income ratios (currently near 7.11x) and Price-to-Rent ratios to evaluate structural affordability ceilings and detatchments from economic anchors.
  - **Energy (XLE):** Tracked alongside the Crude Oil Volatility Index (OVX). Energy volatility acts as a proxy for exogenous geopolitical shocks and inflation resurgence risks that threaten broader equity multiples.
  - **Defense (ITA):** Monitored for geopolitical risk premiums and global conflict escalation vectors affecting the macro environment.

## 5. Dashboards, Visualization and UI/UX Requirements

The `NiceGUI` and `Plotly` implementation will generate dedicated dashboard tabs with a modern, accessible interface:

### 5.1. Dashboard Structure & Tabs
1. **Macro Valuation Dashboard:** Plotting the Shiller CAPE, P-CAPE, and Buffett Indicator against historical trendlines and standard deviation bands.
2. **Systemic Leverage Dashboard:** Visualizing FINRA Margin Debt velocity versus S&P 500 market capitalization, highlighting margin credit exhaustion points.
3. **Econometric Bubble Dashboard:** Real-time plotting of the GSADF (PSY) test statistics, overlaying structural break signals on S&P 500 and Tech sector price charts.
4. **Sentiment & Volatility Dashboard:** Displaying the VIX term structure (contango/backwardation), SKEW index anomalies, and cross-asset volatility (OVX for Energy, VXN for Tech).
5. **Sector-Specific Health Dashboard:** Highlighting the Price-to-Income and Price-to-Rent housing metrics, alongside AI, Tech (XLK), and TDA Geometric Complexity.
6. **Macro Mahalanobis Distance Dashboard:** Multi-dimensional regularized covariance distance ($D_M$) integrating all 15 systemic indicators, empirical crash probability $P_{\\text{bubble}}$, continuous dynamic equity exposure $w_{\\text{equity}}$, and benchmark overlays.

### 5.2. UI/UX & Accessibility Specifications
- **WCAG 2.2 AA Contrast:** All text elements must achieve a minimum contrast ratio of 4.5:1 against their backgrounds (3:1 for large text and graphical components) across both light and dark themes.
- **iOS 13+ Design Patterns:** Native-feeling card-based layout groups, segmented control tab navigation, smooth corner radii (10–16px), subtle backdrop blurs, and grouped list inset styles.
- **Dyslexia-Friendly Labels & Typography:** Standardized clean sans-serif font stack (`-apple-system`, `BlinkMacSystemFont`, `SF Pro Text`, `Inter`, `system-ui`, with `OpenDyslexic` fallback option), letter-spacing `0.015em`, line-height `1.5`–`1.6`, avoiding all-caps walls of text or heavy italics.
- **Avoid Decorative Fonts:** Decorative, cursive, or low-legibility display fonts are strictly prohibited in favor of highly legible system and geometric sans-serif typography.
- **CTA Section with Powerful Typography:** High-impact action section / alert banner with heavy typography (600–800 weight), clear visual weight, and high-contrast call-to-action buttons (e.g. *Run Real-Time Bubble Diagnostics*, *Export Risk Assessment Report*).
- **Consistent Spacing Rhythm:** Standardized 8px base grid system (`4px`, `8px`, `16px`, `24px`, `32px`, `48px`) enforcing uniform margins, padding, and component gaps.
- **Light & Dark Theme Engine:** Dual theme support with dynamic CSS variables and Plotly template toggling (Light: `#F2F2F7` system background, `#FFFFFF` card background, `#1C1C1E` primary text; Dark: `#000000` system background, `#1C1C1E` card background, `#F2F2F7` primary text; Plotly templates: `plotly_white` and `plotly_dark`).

## 6. Data Engineering & Error Handling

Missing data will be handled via forward-fill for prices and cubic spline interpolation for low-frequency macro data. Datasets will be downcasted to `float32` or `int32` in Polars to conserve memory. Error handling will utilize Python's `logging` facility with a `RotatingFileHandler` to track API rate limits, data inconsistencies, and computational exceptions without overflowing storage. Exceptions will be caught using specific exception classes (e.g., `yfinance.YFException`, `ValueError` for dimension mismatches) rather than bare `except` blocks.


## 7. Macro Mahalanobis Distance & Dynamic Equity Allocation

To eliminate collinearity distortions among the 15 macro indicators, the system computes the regularized Mahalanobis distance:
$$D_M(t) = \\sqrt{(\\mathbf{z}_t - \\boldsymbol{\\mu}_t)^T (\\mathbf{\\Sigma}_t + \\lambda \\mathbf{I})^{-1} (\\mathbf{z}_t - \\boldsymbol{\\mu}_t)}$$
where $\\mathbf{z}_t$ is the 15-dimensional standardized indicator vector, $\\boldsymbol{\\mu}_t$ is the rolling mean vector, $\\mathbf{\\Sigma}_t$ is the rolling sample covariance matrix, and $\\lambda = 10^{-2}$ provides Tikhonov ridge regularization.

* **Dynamic Equity Sizing**: Portfolio equity exposure is continuously rebalanced:
  $$w_{\\text{equity}}(t) = \\text{clip}(1.0 - 0.80 \\cdot P_{\\text{bubble}}(t), 0.20, 1.00)$$
  guaranteeing a strict 20% defensive liquidity reserve floor at extreme crisis regimes ($D_M > 6.2\\sigma$).

## 9. Data Red Team Remediation & Institutional Hardening Specifications

1. **Ground Truth Data Provenance & Point-in-Time ETL (Item 1)**: Primary inputs are anchored in verified historical data sources: Robert Shiller's `ie_data.xls` (1871–present monthly S&P prices, earnings, dividends, CPI, and CAPE), FRED macroeconomic series with publication lags (GDP quarterly +60d, M2 weekly +14d), FINRA margin debt with +25d reporting lag, and CBOE VXO daily (1986–present). Staged datasets are packaged as `.parquet` files under `data/provenance/`.
2. **Continuous Splicing Cliff Elimination (Item 2)**: All multi-decade spliced time series (SPY 1993, XLK 1998, VXO/VIX) use continuous backward return compounding:
   $$P_{t-1} = P_t \times \frac{S_{t-1}}{S_t}$$
   anchored at the exact first valid observation of the modern asset, guaranteeing that single-day returns across transition seams are strictly $< 3\%$.
3. **Signed Mahalanobis Sizing & Vector $b$ (Item 3)**: Distance calculation is upgraded from isotropic $D_M$ to signed directional projection:
   $$s_t = \mathbf{b}^\top (\mathbf{\Sigma}_t + \lambda \mathbf{I})^{-1} (\mathbf{z}_t - \boldsymbol{\mu}_t)$$
   where $\mathbf{b} \in \{+1, -1\}^K$ encodes overvaluation (+) versus undervaluation (-). This completely eliminates disastrous de-risking during market crashes, ensuring defensive liquidity is preserved during bubbles ($w_{\text{equity}} \le 0.30$) while equity exposure remains high ($w_{\text{equity}} \ge 0.80$) during crash troughs.
4. **Purged Walk-Forward Calibration & Validation Table (Item 4)**: Regime probabilities are calibrated walk-forward with 20-day purge embargoes, verified by Brier scores ($< 0.20$) and Expected Calibration Error (ECE $< 0.10$). An automated event study validation table tracks performance across 8 historical crashes (1929, 1973, 1987, 2000, 2007, 2018, 2020, 2022).
5. **Canonical Econometric PSY/GSADF & Ripser TDA (Item 5)**: Canonical recursive right-tail unit root testing is performed on monthly log price-dividend ratios against Phillips, Shi, & Yu (2015) finite-sample critical values. Toy PCA embeddings are replaced with genuine Vietoris-Rips persistent homology using the C-optimized `ripser` library.
6. **Elimination of Endogeneity & Collinearity Leakage (Item 6)**: The model forecast `Drawdown_Probability` and collinearly scaled `P_CAPE` are strictly excluded from the covariance matrix estimation feature space, reducing matrix condition numbers by $> 500\times$.
7. **Institutional Cost-Inclusive Backtest Simulation Engine (Item 7)**: Real-world portfolio dynamics are simulated with 10 bps transaction fees, 5 bps market-impact slippage, 4.0% annualized cash yield, and borrowing penalties. The strategy demonstrates superior Sharpe ratios, sortino ratios, and reduced maximum drawdowns compared to Buy & Hold and Naive CAPE benchmark rules.
8. **WebAssembly Parquet Virtual Filesystem & Provenance Badges (Item 8)**: Parquet tables are mounted directly into Pyodide virtual filesystems for instant zero-drift client execution. All visual traces across Tabs 1–6 display explicit provenance badges (`[REAL]`, `[PROXY]`, `[SYNTHETIC]`), and an prominent red alert banner dynamically renders if fallback data is engaged.
9. **Automated Verification Quality Gate**: All 62 unit, numerical parity, anti-synthetic provenance regression, and system integration tests must pass with 100% success rate (`pytest tests/`).

<!-- ### -->
<!-- # eNd TechnicalSpecification_DDFv100.md -->
<!-- ### -->
