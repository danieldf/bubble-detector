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
2. **Liquidity & Leverage Dashboard:** Visualizing FINRA Margin Debt velocity versus S&P 500 market capitalization, highlighting margin credit exhaustion points.
3. **Econometric Bubble Dashboard:** Real-time plotting of the GSADF (PSY) test statistics, overlaying structural break signals on S&P 500 and Tech sector price charts.
4. **Sentiment & Volatility Dashboard:** Displaying the VIX term structure (contango/backwardation), SKEW index anomalies, and cross-asset volatility (OVX for Energy, VXN for Tech).
5. **Sector-Specific Health Dashboard:** Highlighting the Price-to-Income and Price-to-Rent housing metrics, alongside AI and Defense sector momentum and valuations.

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

<!-- ### -->
<!-- # eNd TechnicalSpecification_DDFv100.md -->
<!-- ### -->
