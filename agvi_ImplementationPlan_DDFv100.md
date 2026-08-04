<!-- ### -->
<!-- # BeGiN ImplementationPlan_DDFv100.md -->
<!-- ### -->

# Implementation Plan: Spec-Driven Development

Implementation Plan Confidence Score: 0.95

## Phase 1: SDD Setup and Initialization, Architecture and Configuration

1. **Initialize SpecKit Environment:** Execute the Specify CLI tool to bootstrap the project repository.
  1. Use the command `uvx --from git+[https://github.com/github/spec-kit.git](https://github.com/github/spec-kit.git) specify init bubble_detector`.
2. **Define Constitution:** Run `/speckit.constitution` in the coding agent to establish the `constitution.md` file. The rules will explicitly mandate TDD (writing `pytest` unit tests before implementation), enforce Polars for dataframe manipulation, and require all functions to have strict Python type hints and docstrings, and rigorous exception logging.
3. **Generate Spec & Plan:** Run `/speckit.specify` with the detailed macroeconomic, options, and sector indicators outlined above, followed by `/speckit.plan` to generate the technical architecture blueprint (NiceGUI, TA-Lib, Polars), and finally run `/speckit.analyze` to cross-reference the plan against the constitution for inconsistencies before writing code.

## Phase 2: Data Ingestion and Storage (TDD Loop)

1. **Tasks Generation:** Run `/speckit.tasks` focused strictly on the data ingestion module.
2. **Test Creation:** Write `pytest` fixtures for mocked `yfinance` responses.
3. **Implementation:** Run `/speckit.implement` to build the `DataIngestor` class fetching S&P 500 (SPY), sector ETFs, macro data, Tech (XLK, SMH), Energy (XLE), Housing (ITB), and Defense (ITA) data, plus macro factors (VIX, SKEW, FINRA Margin Debt, GDP).
4. **Serialization:** Ensure all ingested data is appropriately downcasted and strictly typed in Polars and saved locally in Parquet format for rapid downstream access.

## Phase 3: Quantitative Indicators and Feature Engineering

1. **Tasks Generation:** Run `/speckit.tasks` targeting feature engineering, and for the indicator and scaling pipeline.
2. **Implementation:**
  1. Calculate baseline technicals using TA-Lib. Build functions that consume the Polars DataFrames and utilize TA-Lib to append rolling indicators (RSI, Bollinger Bands, Moving Averages).
  2. Implement the Shiller CAPE and the dividend-adjusted P-CAPE logic.
  3. Calculate the Buffett Indicator (Market Cap / GDP).
  4. Implement the PSY procedure (GSADF test), adding the fundamental decomposition step for GPT tech shocks.
3. **Scaling:** Implement a Scikit-learn preprocessing pipeline. Apply `RobustScaler` to the price data and macro metrics. Map the exact Z-score normalization pipelines needed for the anomaly detection logic using Scikit-learn to prep data for the machine learning models, isolating extreme outliers dynamically.
4. **Test:** Ensure unit tests check for zero look-ahead bias and correct handling of `NaN` values.

## Phase 4: Machine Learning Model Setup and Integration

1. **Tasks Generation:** Run `/speckit.tasks` for the ML module.
2. **Implementation of the Model Training:** Train the `XGBoost` classifier to predict structural breaks and forward-looking drawdowns based on the engineered features (P-CAPE, Margin Credit, SKEW, housing metrics, etc.).
3. **Cross-Validation:** Implement expanding-window walk-forward cross-validation (TimeSeriesSplit) to maintain the chronological integrity of the financial time series.

## Phase 5: Dashboard, Visualization and UI/UX Layer

1. **Tasks Generation:** Run `/speckit.tasks` for the NiceGUI frontend and UI/UX layer.
2. **Design Tokens & Theme Engine:**
   1. Implement a centralized UI theme module (`styles.css` / theme manager) enforcing an 8px base grid spacing rhythm (`4px`, `8px`, `16px`, `24px`, `32px`, `48px`).
   2. Configure dyslexia-friendly typography defaults (SF Pro / Inter font stack, `0.015em` letter-spacing, `1.5` line-height, no decorative fonts, no all-caps blocks).
   3. Build a dual Light/Dark theme toggle with automatic system preference detection (`#F2F2F7` light vs `#000000` dark system backgrounds).
   4. Create automated contrast checks validating WCAG 2.2 AA (minimum 4.5:1 ratio for text) across both themes.
3. **NiceGUI Layout & iOS 13+ Patterns:** Construct an interactive dashboard utilizing NiceGUI styled with iOS 13+ design patterns (card container groups, segmented controls for tab switching, 12px rounded corners, and inset list styles).
4. **Call-To-Action (CTA) Section:** Build a dedicated high-impact CTA banner with powerful typography (600–800 font weight) and interactive action buttons for running real-time bubble diagnostics and exporting systemic risk assessment reports.
5. **Implementation and Plotly Integration:** Build interactive Plotly charts embedded in NiceGUI, dynamically updating chart templates (`plotly_white` / `plotly_dark`) upon theme toggling. Create the dedicated tabs: Macro Valuation, Systemic Leverage, Econometric Tests, Sentiment & Volatility, and Sector-Specific Health.
6. **Final Review & Verification:** Execute `/speckit.analyze` to cross-reference the final implementation against the updated specification, constitution, and accessibility criteria to ensure all designated indicators, UI patterns, and themes are fully operational.
7. **Implement:** Run `/speckit.implement` and finalize end-to-end integration and accessibility test suites.

<!-- ### -->
<!-- # eNd ImplementationPlan_DDFv100.md -->
<!-- ### -->
