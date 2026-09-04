# Graph Report - Merrill  (2026-09-03)

## Corpus Check
- 71 files · ~432,761 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 627 nodes · 1178 edges · 34 communities (33 shown, 1 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 41 edges (avg confidence: 0.78)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `034aaf97`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Merrill ETF Portfolio Reviews
- AGVI System Pipeline and Dashboard
- Econometric Bubble Detection Models
- Implied Volatility Term Structure Metrics
- Graphify Settings and Rules
- Valuation and Feature Engineering
- FINRA Margin Debt Metrics
- Systemic Leverage Analysis
- test_ui_theme.py
- __init__.py
- Overview of Completed Implementation
- Detailed Slide Breakdown by Section & Group
- .fetch_market_data
- panel_dashboard.py
- AGVI Technical Specification Document
- etl_shiller.py
- etl_vxo.py
- ingestor.py
- etl_finra.py
- etl_fred.py
- generate_wasm_dataset
- __init__.py
- test_features.py
- stage_provenance.py
- compute_margin_leverage_metrics
- test_no_synthetic_gaussian_bumps_in_data_code
- compute_technical_indicators
- compute_macro_valuations
- System Architecture and Operational Rules for Agents
- apply_postprocessing

## God Nodes (most connected - your core abstractions)
1. `DashboardState` - 38 edges
2. `MacroMahalanobisDetector` - 34 edges
3. `DataIngestor` - 29 edges
4. `StructuralBreakPredictor` - 25 edges
5. `generate_wasm_dataset()` - 24 edges
6. `compute_tda_wavelet_complexity()` - 21 edges
7. `compute_gsadf_gpt_decomposition()` - 18 edges
8. `compute_margin_leverage_metrics()` - 18 edges
9. `compute_options_volatility_metrics()` - 18 edges
10. `compute_technical_indicators()` - 17 edges

## Surprising Connections (you probably didn't know these)
- `Joint ETF Strategy Portfolio (March 2026)` --conceptually_related_to--> `Real Estate Valuation Metrics`  [INFERRED]
  CRC_185050992_20260402.pdf → MarketBubble_DDFv100.md
- `Joint ETF Strategy Portfolio (May 2026)` --conceptually_related_to--> `Real Estate Valuation Metrics`  [INFERRED]
  CRC_185865214_20260502.pdf → MarketBubble_DDFv100.md
- `Joint ETF Strategy Portfolio (June 2, 2026)` --conceptually_related_to--> `Real Estate Valuation Metrics`  [INFERRED]
  CRC_186566428_20260602.pdf → MarketBubble_DDFv100.md
- `Joint ETF Strategy Portfolio (June 29, 2026)` --conceptually_related_to--> `Real Estate Valuation Metrics`  [INFERRED]
  CRC_187083673_20260629.pdf → MarketBubble_DDFv100.md
- `Joint ETF Strategy Portfolio (March 2026)` --conceptually_related_to--> `Technology & Semiconductors Sector`  [INFERRED]
  CRC_185050992_20260402.pdf → MarketBubble_DDFv100.md

## Import Cycles
- 1-file cycle: `bubble_detector/features/__init__.py -> bubble_detector/features/__init__.py`
- 1-file cycle: `bubble_detector/ui/__init__.py -> bubble_detector/ui/__init__.py`
- 1-file cycle: `bubble_detector/ui/theme.py -> bubble_detector/ui/theme.py`

## Hyperedges (group relationships)
- **Client Portfolio Performance History (Q2 2026)** — crc_185050992_20260402_joint_etf_strategy, crc_185865214_20260502_joint_etf_strategy, crc_186566428_20260602_joint_etf_strategy, crc_187083673_20260629_joint_etf_strategy [INFERRED 0.95]
- **Econometric and Mathematical Bubble Detection Framework** — marketbubble_ddfv100_gsadf_psy_procedure, marketbubble_ddfv100_tda_wavelet, marketbubble_ddfv100_lppls_model [EXTRACTED 1.00]
- **AGVI Indicator and Feature Engineering Pipeline** — marketbubble_ddfv100_shiller_cape_ratio, marketbubble_ddfv100_payout_adjusted_cape, marketbubble_ddfv100_buffett_indicator, marketbubble_ddfv100_gsadf_psy_procedure [EXTRACTED 1.00]
- **FINRA Margin Debt Metrics** — finra_margin_debt_tracker, finra_may_2026_nominal_value, finra_may_2026_mom_change, finra_may_2026_yoy_change [INFERRED 0.85]
- **Implied Volatility Term Structure Components** — impliedvolatilitymetric_vix1d, impliedvolatilitymetric_vix_spot, impliedvolatilitymetric_vix3m, impliedvolatilitymetric_vix1y [EXTRACTED 1.00]

## Communities (34 total, 1 thin omitted)

### Community 0 - "Merrill ETF Portfolio Reviews"
Cohesion: 0.06
Nodes (46): Graphify Rules Document, Graphify Query Rule, Graphify Workflow Document, NiceGUI Layout & Plotly Dashboard, Data Ingestion (DataIngestor), AGVI Implementation Plan Document, Feature Engineering Pipeline, XGBoost Model Training & Walk-Forward CV (+38 more)

### Community 1 - "AGVI System Pipeline and Dashboard"
Cohesion: 0.06
Nodes (40): Multidimensional Econometric & Quantitative Market Bubble Detection System. ====, Regime Classification & Structural Break Machine Learning Subpackage. ==========, MacroMahalanobisDetector, DataFrame, ndarray, Macro Mahalanobis Distance Regime-Switching Bubble Detector. ===================, Multi-dimensional signed statistical distance regime-switching bubble detector., Derive stationary indicators if raw ticker series are present. (+32 more)

### Community 2 - "Econometric Bubble Detection Models"
Cohesion: 0.18
Nodes (11): generate_wasm_dataset(), Any, Generate high-speed financial time series dataset for Pyodide WebAssembly.     S, Verify 100% numerical parity for TDA Persistence L2 Norm between WASM app and to, test_tda_wasm_parity(), Verify pure NumPy fallback operates with zero dependencies when     neither parq, Verify candidate dataset selection correctly maps 50-year rolling horizons to ma, Simulate Pyodide MEMFS where polars and bubble_detector are unavailable,     and (+3 more)

### Community 3 - "Implied Volatility Term Structure Metrics"
Cohesion: 0.60
Nodes (6): Implied Volatility Metrics Table (July 2026), Implied Volatility Term Structure (Upward Sloping), VIX1D (8.73 - 11.61): Extreme near-term calm, VIX1Y (~23.00): Elevated long-term risk premium, VIX3M (~19.00): Anticipation of future turbulence, VIX Spot (15.57 - 17.16): Low baseline fear

### Community 4 - "Graphify Settings and Rules"
Cohesion: 0.05
Nodes (47): BubbleDetectorError, DataFetchError, Root base exception for all domain-specific errors in the Bubble Detector ecosys, Raised when financial market, macroeconomic, or provenance data acquisition fail, Raised when financial time-series integrity constraints or schemas are violated., ValidationError, get_current_date(), get_dynamic_50yr_date_range() (+39 more)

### Community 5 - "Valuation and Feature Engineering"
Cohesion: 0.20
Nodes (9): Unit tests for Institutional Data Provenance & Publication Lags (Shiller, FRED,, Asserts real Shiller data spans 1871-present with valid CAPE, earnings, and divi, Asserts GDP and Case-Shiller releases are strictly point-in-time lagged by >= 60, Asserts margin debt data incorporates mandatory 3-week reporting lag., Asserts authentic CBOE VXO captures the 1987 Black Monday volatility spike., test_finra_margin_publication_lag(), test_fred_publication_lags(), test_shiller_provenance_schema_and_bounds() (+1 more)

### Community 6 - "FINRA Margin Debt Metrics"
Cohesion: 0.11
Nodes (19): ModelTrainingError, Raised when machine learning or statistical regime estimation fails.      Trigge, Any, DataFrame, ndarray, Extract features and construct forward drawdown target variable without lookahea, Train ML model and fit isotonic probability calibrator using expanding-window, Predict calibrated structural break drawdown probabilities. (+11 more)

### Community 8 - "test_ui_theme.py"
Cohesion: 0.08
Nodes (25): BacktestResult, PortfolioBacktestEngine, Any, DataFrame, ndarray, Institutional Cost-Inclusive Portfolio Backtest Simulation Engine. =============, Execute comparative backtest across Dynamic Exposure, Buy & Hold, and Naive CAPE, Simulate single portfolio with frictions, cash yields, and rebalancing costs. (+17 more)

### Community 9 - "__init__.py"
Cohesion: 0.18
Nodes (14): _compute_rips_persistence_diagrams(), compute_tda_wavelet_complexity(), _persistence_landscape_l2_norm(), DataFrame, ndarray, Topological Data Analysis (TDA) & Wavelet Complexity Module. ===================, Calculate Bubenik (2015) persistence landscape L2 norm representing topological, Compute sliding window Vietoris-Rips persistent homology L2 norm and Morlet Wave (+6 more)

### Community 11 - "Overview of Completed Implementation"
Cohesion: 0.17
Nodes (11): 10. Institutional Code Commentary, Packaging & Agent Navigation:, 1. System, Configuration & Date Horizons (`config.py` & `date_horizons.py`):, 2. UI & Accessibility Engine (`ui_theme.py`):, 3. Data Ingestion & Storage (`ingestor.py`):, 4. Quantitative Indicator Modules (`features/` & `features/utils.py`):, 5. Machine Learning Model (`structural_breaks.py`):, 6. Macro Mahalanobis Distance Engine (`regime_mahalanobis.py`):, 7. Interactive Dashboards & Dual-Runtime Architecture: (+3 more)

### Community 13 - "Detailed Slide Breakdown by Section & Group"
Cohesion: 0.20
Nodes (9): Detailed Slide Breakdown by Section & Group, Executive Presentation Deck Overview, Group 1: Key Findings (Group Confidence Score: 0.94), Group 2: Supporting Evidence: Valuation, Econometrics & ML (Group Confidence Score: 0.93), Group 3: Sector Specific Application: Tech vs. Energy (Group Confidence Score: 0.91), Group 4: Implications for Systemic Stability (Group Confidence Score: 0.95), Group 5: Strategic Recommendations (Group Confidence Score: 0.96), Verification Results (+1 more)

### Community 16 - ".fetch_market_data"
Cohesion: 0.05
Nodes (39): 1. Continuous Backward Compounding (Cliff Eradication), 1. Macro Valuation Anchors, 1. Prerequisites & Virtual Environment, 2. Run the High-Performance NiceGUI Application, 2. Signed Macro Mahalanobis Distance & Directional Projection, 2. Systemic Liquidity & Leverage, 3. Dynamic Portfolio Equity Sizing ($w_{\text{equity}}$), 3. Econometric Explosive Bubble Diagnostics (+31 more)

### Community 17 - "panel_dashboard.py"
Cohesion: 0.05
Nodes (79): normalize_tda_indicator(), Causally rescale raw TDA Persistence Landscape L2 Norm to span [target_min, targ, create_cta_banner(), create_ios_card(), UI Accessible Components & iOS 13+ Design System Module. =======================, Render a high-impact Call-To-Action (CTA) section with heavy typography and acce, Create an iOS 13+ inset card container with subtle elevation, rounded corners, a, build_econometric_chart() (+71 more)

### Community 19 - "AGVI Technical Specification Document"
Cohesion: 0.20
Nodes (11): get_shiller_data(), parse_shiller_excel(), DataFrame, Path, Robert Shiller Monthly ie_data ETL & Point-in-Time Provenance Ingestor (1871–Pre, ETL Pipeline for Robert Shiller's monthly S&P Composite and CAPE dataset., Fetch Shiller data, parse real workbook and cache to parquet., Interpolate monthly Shiller series to daily business days with strictly causal (+3 more)

### Community 20 - "etl_shiller.py"
Cohesion: 0.40
Nodes (4): postprocess_wasm_html(), Path, Post-Processing Utility for Panel WebAssembly Compiled Artifacts (`dist/index.ht, Apply post-processing transformations to the compiled Panel WebAssembly HTML bun

### Community 21 - "etl_vxo.py"
Cohesion: 0.17
Nodes (11): Institutional Data Provenance Certification & Anti-Synthetic Regression Suite., Certifies FRED nominal GDP and Case-Shiller index match official BEA/FRED public, Scans all source files in bubble_detector/data/ to certify that NO disguised, Certifies Shiller ie_data.xls contains genuine S&P data from 1871 to present., Certifies CBOE VXO captures the exact 150.19 close on October 19, 1987., Certifies FINRA margin debt reflects true regulatory figures exceeding $1.4 Tril, test_authentic_cboe_vxo_black_monday(), test_authentic_finra_margin_debt() (+3 more)

### Community 22 - "ingestor.py"
Cohesion: 0.13
Nodes (21): calculate_contrast_ratio(), get_plotly_template(), get_theme_css(), is_wcag_aa_compliant(), parse_hex_color(), UI Theme and Accessibility Design System for Bubble Detector. ==================, UI Theme and Accessibility Design System Module (UI Package Binding). ==========, Return the Plotly template identifier for the specified theme mode.      Paramet (+13 more)

### Community 23 - "etl_finra.py"
Cohesion: 0.20
Nodes (11): FinraETL, get_finra_margin_debt(), parse_finra_margin_debt_series(), DataFrame, Path, FINRA & NYSE Margin Debt Point-in-Time ETL Module. =============================, ETL Pipeline for FINRA & NYSE margin debt with strict publication lag constraint, Stage FINRA margin debt dataset to parquet. (+3 more)

### Community 24 - "etl_fred.py"
Cohesion: 0.20
Nodes (11): FredETL, get_fred_data(), parse_fred_macro_series(), DataFrame, Path, FRED Macroeconomic Point-in-Time Data ETL Module. ==============================, ETL Pipeline for FRED macroeconomic series with strict publication lag constrain, Stage FRED macro dataset to parquet. (+3 more)

### Community 25 - "generate_wasm_dataset"
Cohesion: 0.18
Nodes (13): calculate_adf_stat(), compute_gsadf_gpt_decomposition(), compute_wild_bootstrap_critical_values(), DataFrame, ndarray, Econometric Bubble Detection Module (Canonical PSY & GSADF). ===================, Computes canonical recursive expanding-window GSADF explosive test statistics, Calculate Augmented Dickey-Fuller t-statistic for right-tailed explosive root te (+5 more)

### Community 26 - "__init__.py"
Cohesion: 0.33
Nodes (7): Quantitative Feature Engineering & Mathematical Signal Processing Subpackage. ==, calculate_adf_stat(), ndarray, Shared Mathematical & Topological Utilities. ===================================, Calculate Augmented Dickey-Fuller t-statistic for right-tailed explosive root te, Transform 1D time series into Takens delay-coordinate high-dimensional point clo, takens_embedding()

### Community 28 - "test_features.py"
Cohesion: 0.18
Nodes (11): compute_options_volatility_metrics(), DataFrame, Options Market Microstructure & Volatility Behavioral Dynamics Module. =========, Compute VIX term structure slope, SKEW tail-risk alert, dispersion index, and cr, Options Market Microstructure & Volatility Behavioral Dynamics Module. =========, test_compute_options_volatility_metrics(), Unit tests for canonical module aliases and backward compatibility bindings.  Ve, Verify options_volatility module function matches canonical implementation. (+3 more)

### Community 29 - "stage_provenance.py"
Cohesion: 0.22
Nodes (10): Global Configuration, Logging Infrastructure & Constants Module. ===============, CBOE S&P 100 Volatility Index (^VXO) ETL & Historical Splicer (1986–Present). ==, ETL Pipeline for CBOE VXO volatility index., VxoETL, precompile_wasm_parquet_datasets(), Pre-compile production Parquet and lightweight clean JSON datasets for     clien, Provenance Data Staging & WebAssembly Binary Pre-Compilation Pipeline. =========, Convert existing staged Parquet datasets into clean JSON tables for WebAssembly (+2 more)

### Community 30 - "compute_margin_leverage_metrics"
Cohesion: 0.17
Nodes (9): compute_margin_leverage_metrics(), DataFrame, Systemic Leverage & Margin Debt Dynamics Module. ===============================, Compute FINRA Margin Debt YoY growth, velocity, leverage gap, and exhaustion ris, Systemic Margin Leverage & Credit Exhaustion Indicator Module. =================, Fetch and process full dataset pipeline for selected date horizon., test_compute_margin_leverage_metrics(), Verify margin_leverage module function matches canonical implementation. (+1 more)

### Community 31 - "test_no_synthetic_gaussian_bumps_in_data_code"
Cohesion: 0.24
Nodes (8): get_vxo_data(), parse_authentic_vxo_series(), DataFrame, Path, Stage authentic VXO dataset to parquet., Get daily VXO series reindexed to requested business dates., Public helper to obtain daily CBOE VXO series., Parse authentic CBOE VXO daily history spanning 1976 to present.      Splicing H

### Community 32 - "compute_technical_indicators"
Cohesion: 0.19
Nodes (10): IndicatorComputationError, Raised when econometric, technical, or topological indicator calculations fail., Technical Indicators & Momentum Oscillators Module. ============================, compute_technical_indicators(), DataFrame, Technical Indicators & Momentum Oscillators Module. ============================, Append technical momentum, trend, and volatility indicators to the input Polars, Unit tests for Feature Engineering Modules (technicals, macro valuations, levera (+2 more)

### Community 35 - "compute_macro_valuations"
Cohesion: 0.20
Nodes (9): compute_macro_valuations(), DataFrame, Macroeconomic Valuation & Long-Horizon Equilibrium Module. =====================, Compute Shiller CAPE, Payout-Adjusted CAPE (P-CAPE), and Buffett Indicator metri, test_compute_macro_valuations(), processed_df(), Unit tests for StructuralBreakPredictor machine learning module., test_predict_drawdown_probability() (+1 more)

### Community 36 - "System Architecture and Operational Rules for Agents"
Cohesion: 0.40
Nodes (4): 1. Core Econometric & Statistical Rules, 2. Directory Layout & Key Modules, 3. Execution & Verification Rules, System Architecture and Operational Rules for Agents

### Community 38 - "apply_postprocessing"
Cohesion: 0.13
Nodes (15): apply_postprocessing(), Unit tests for WebAssembly Pyodide Sandbox Isolation, End-to-End Execution, and, End-to-end execution of bubble_detector/ui/panel_dashboard.py under total packag, End-to-end execution of panel_dashboard.py under total package isolation in an e, Verify Executive Summary, Horizon Specifications Card, and FastListTemplate., Helper implementing the exact GitHub Actions deployment postprocessing., Verify that postprocessing is completely idempotent and never creates nested try, Verify that dist/index.html exists on disk and contains exactly one error bounda (+7 more)

## Knowledge Gaps
- **66 isolated node(s):** `market-bubble-detector`, `1. Core Econometric & Statistical Rules`, `2. Directory Layout & Key Modules`, `3. Execution & Verification Rules`, `1. System, Configuration & Date Horizons (`config.py` & `date_horizons.py`):` (+61 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `MacroMahalanobisDetector` connect `AGVI System Pipeline and Dashboard` to `panel_dashboard.py`, `Econometric Bubble Detection Models`, `stage_provenance.py`, `compute_margin_leverage_metrics`?**
  _High betweenness centrality (0.088) - this node is a cross-community bridge._
- **Why does `DashboardState` connect `panel_dashboard.py` to `AGVI System Pipeline and Dashboard`, `Graphify Settings and Rules`, `FINRA Margin Debt Metrics`, `test_ui_theme.py`, `ingestor.py`, `compute_margin_leverage_metrics`?**
  _High betweenness centrality (0.071) - this node is a cross-community bridge._
- **Why does `DataIngestor` connect `Graphify Settings and Rules` to `compute_technical_indicators`, `AGVI System Pipeline and Dashboard`, `Econometric Bubble Detection Models`, `compute_macro_valuations`, `panel_dashboard.py`, `stage_provenance.py`, `compute_margin_leverage_metrics`?**
  _High betweenness centrality (0.062) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `DashboardState` (e.g. with `PortfolioBacktestEngine` and `DataIngestor`) actually correct?**
  _`DashboardState` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `DataIngestor` (e.g. with `DataFetchError` and `ValidationError`) actually correct?**
  _`DataIngestor` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `StructuralBreakPredictor` (e.g. with `ModelTrainingError` and `DashboardState`) actually correct?**
  _`StructuralBreakPredictor` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `market-bubble-detector`, `1. Core Econometric & Statistical Rules`, `2. Directory Layout & Key Modules` to the rest of the system?**
  _66 weakly-connected nodes found - possible documentation gaps or missing edges._