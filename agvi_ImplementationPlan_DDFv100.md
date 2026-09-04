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

## Phase 6: Macro Mahalanobis Distance Engine & Tab 6 Architecture

1. **Regularized Statistical Distance:** Implement 15-dimensional Riemannian statistical distance $D_M(t) = \sqrt{(\mathbf{z}_t - \boldsymbol{\mu}_t)^T (\hat{\mathbf{\Sigma}} + 10^{-2}\mathbf{I})^{-1} (\mathbf{z}_t - \boldsymbol{\mu}_t)}$ utilizing Ledoit-Wolf shrinkage and Tikhonov ridge regularization.
2. **Signed Directional Projection Vector $\mathbf{b}$:** Pre-register directional sign vector $\mathbf{b} \in \{-1, +1\}^{15}$ and signed projection $\text{Score}_{bubble}(t) = \frac{(\mathbf{z}_t - \boldsymbol{\mu}_t)^T \mathbf{\Sigma}^{-1} \mathbf{b}}{\sqrt{\mathbf{b}^T \mathbf{\Sigma}^{-1} \mathbf{b}}}$ to resolve quadratic form symmetry and eradicate disastrous de-risking during crash troughs (preserving $w_{\text{equity}} \ge 0.80$ at market bottoms).
3. **Tab 6 Visualization Module:** Deploy interactive Tab 6 ("Macro Mahalanobis Distance") in both NiceGUI and WebAssembly, rendering 8 synchronized macro traces, three critical risk thresholds ($3.8\sigma$ Equilibrium, $5.0\sigma$ Warning, $6.2\sigma$ Crisis), and right-flushed vertical legends (`orientation="v", x=1.01, y=1.0, margin.r=230`).
4. **Dynamic Calendar-Anchored 50-Year Engine:** Build `bubble_detector/data/date_horizons.py` dynamically anchoring historical lookbacks to 50 physical calendar years rolling from the execution date (e.g. 1976–2026, 13,045 trading days across 9 regimes).

## Phase 7: Data Red Team Remediation & Institutional Hardening

1. **Ground-Truth Point-in-Time Data ETL:**
   - Ingest Robert Shiller's official `ie_data.xls` (1,869 monthly records, 1871–present) with +5d publication lag.
   - Ingest FRED Nominal GDP, Case-Shiller Home Price Index, and Median Household Income with +60d publication lag.
   - Ingest FINRA customer margin debit statistics spliced with NYSE historical archives (1959–present) with +21d lag.
   - Ingest CBOE VXO daily history (1986–present) capturing the 150.19 Black Monday peak.
2. **Zero Synthetic Gaussian Bumps:** Eliminate all analytical Gaussian curve functions from data ingestors; certify via automated test `tests/test_no_gaussian_bumps.py`.
3. **Continuous Splicing Cliff Elimination:** Implement continuous backward return compounding ($P_{t-1} = P_t \times S_{t-1} / S_t$) anchored at target asset inceptions (SPY 1993, XLK 1998, VXO/VIX 1986), guaranteeing single-day seam returns remain strictly $< 3\%$.
4. **Endogeneity & Collinearity Leakage Elimination:** Exclude ML model prediction `Drawdown_Probability` and collinearly scaled `P_CAPE` from the 15-indicator covariance estimation matrix, reducing condition numbers by $> 500\times$.

## Phase 8: WebAssembly Virtual Filesystem, Backtesting & Validation

1. **Client-Side WebAssembly Pipeline (`panel_dashboard.py`):**
   - Stage pre-compiled Parquet and JSON datasets into virtual Emscripten memory (`pyodide.FS.writeFile`).
   - Compile via `python -m panel convert bubble_detector/ui/panel_dashboard.py --to pyodide-worker --out dist/`.
   - Post-process `dist/index.html` via `bubble_detector/ui/postprocess_wasm.py` (MEMFS pre-loader, wheel normalization, unicode emoji decoders, and DOM error boundaries).
2. **Cost-Inclusive Portfolio Backtest Simulation Engine (`engine.py`):**
   - Simulate portfolio dynamics with 10 bps transaction fees, 5 bps slippage (15 bps turnover cost), 2.0% rebalance deadband, 4.0% cash yield, and borrowing penalties.
   - Validate risk-adjusted outperformance against Buy-and-Hold S&P 500 and binary Naive CAPE timing rules.
3. **Falsifiable Historical Peak Validation Event Study (`validation_table.py`):**
   - Execute Popperian event study across 8 landmark historical crashes (1980 Volcker, 1987 Black Monday, 1990 S&L, 2000 Dot-Com, 2008 GFC, 2018 Volmageddon, 2020 COVID, 2022 Rate Shock).
   - Demonstrate 100% warning hit rate and 66.5-day median lead time.

## Phase 9: Institutional Code Commentary, Packaging, SemVer & Agent Rules

1. **Comprehensive Code Commentary:** Author exhaustive docstrings detailing mathematical formulas, economic theory, algorithmic derivations, design choices, and failure modes across all modules in `bubble_detector/`.
2. **Module Alias Architecture:** Provide seamless canonical module aliases (`margin_leverage.py`, `options_volatility.py`, `technical.py`, `ui/theme.py`) for frictionless agent navigation and import interoperability.
3. **Modern Packaging Infrastructure:** Deeply document `requirements.txt` and `pyproject.toml` with runtime role annotations, WASM constraints, and dependency groupings adhering to PEP 621.
4. **Agent Navigation & Architecture Rules:** Document strict operational guidelines in `GEMINI.md` and `.agents/rules/system_architecture.md` (macOS sandbox rules, virtualenv paths, zero Gaussian bump rules, verification commands).
5. **Quality Gate:** Guarantee 100% pass rate across the full automated test suite (`pytest tests/ -v`).
6. **Release Management:** Bump SemVer to `v3.0.0`, update changelogs in `README.md` and `MarketBubble_DDFv100.md`, tag git commit as `v3.0.0`, and synchronize remote GitHub repository.

<!-- ### -->
<!-- # eNd ImplementationPlan_DDFv100.md -->
<!-- ### -->
