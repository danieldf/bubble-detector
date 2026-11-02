# Graph Report - Merrill  (2026-10-05)

## Corpus Check
- 82 files · ~106,693 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 751 nodes · 1396 edges · 43 communities (36 shown, 3 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 35 edges (avg confidence: 0.89)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `73052c21`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Market Bubble Structural Analysis Report
- test_mahalanobis.py
- create_app
- Implied Volatility Metrics Table (July 2026)
- config.py
- test_all_tabs_legends_right_flushed
- StructuralBreakPredictor
- market-bubble-detector
- PortfolioBacktestEngine
- compute_gsadf_gpt_decomposition
- Overview of Completed Implementation: Multidimensional Market Bubble Detector
- Detailed Slide Breakdown by Section & Group
- 📉 Multidimensional Market Bubble Detector & Structural Break System
- dashboard.py
- test_ui_ux_wasm_optimizations.py
- test_data_provenance.py
- test_wasm_pyodide_sandbox.py
- test_no_gaussian_bumps.py
- calculate_contrast_ratio
- stage_provenance.py
- FredETL
- DataIngestor
- features/__init__.py
- compute_lppls_confidence_indicator
- options_vol.py
- compute_tda_wavelet_complexity
- compute_margin_leverage_metrics
- VxoETL
- compute_technical_indicators
- build_tech_exuberance_fig
- compute_exuberance_spans
- generate_wasm_dataset
- System Architecture and Operational Rules for Agents
- get_current_date
- test_full_indicator_parity.py
- test_wasm_parquet_parity.py
- sw.js
- [3.1.0] - 2026-10-05
- panel_dashboard.py

## God Nodes (most connected - your core abstractions)
1. `DashboardState` - 39 edges
2. `MacroMahalanobisDetector` - 35 edges
3. `DataIngestor` - 28 edges
4. `StructuralBreakPredictor` - 28 edges
5. `generate_wasm_dataset()` - 26 edges
6. `compute_tda_wavelet_complexity()` - 25 edges
7. `compute_gsadf_gpt_decomposition()` - 21 edges
8. `compute_margin_leverage_metrics()` - 19 edges
9. `compute_options_volatility_metrics()` - 19 edges
10. `compute_technical_indicators()` - 18 edges

## Surprising Connections (you probably didn't know these)
- `Data Ingestion (DataIngestor)` --conceptually_related_to--> `FINRA Margin Debt Tracker (2026)`  [INFERRED]
  agvi_ImplementationPlan_DDFv100.md → finra.png
- `processed_df()` --uses--> `DataIngestor`  [INFERRED]
  tests/test_models.py → bubble_detector/data/ingestor.py
- `test_all_indicators_numerical_parity()` --uses--> `DashboardState`  [INFERRED]
  tests/test_full_indicator_parity.py → bubble_detector/ui/dashboard.py
- `test_dashboard_state_theme_toggle()` --calls--> `DashboardState`  [EXTRACTED]
  tests/test_ui_theme.py → bubble_detector/ui/dashboard.py
- `test_wasm_loads_exact_parquet_dataset()` --uses--> `DashboardState`  [INFERRED]
  tests/test_wasm_parquet_parity.py → bubble_detector/ui/dashboard.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **AGVI Indicator and Feature Engineering Pipeline** — marketbubble_ddfv100_shiller_cape_ratio, marketbubble_ddfv100_payout_adjusted_cape, marketbubble_ddfv100_buffett_indicator, marketbubble_ddfv100_gsadf_psy_procedure [EXTRACTED 1.00]
- **Econometric and Mathematical Bubble Detection Framework** — marketbubble_ddfv100_gsadf_psy_procedure, marketbubble_ddfv100_tda_wavelet, marketbubble_ddfv100_lppls_model [EXTRACTED 1.00]
- **Implied Volatility Term Structure Components** — impliedvolatilitymetric_vix1d, impliedvolatilitymetric_vix_spot, impliedvolatilitymetric_vix3m, impliedvolatilitymetric_vix1y [EXTRACTED 1.00]
- **FINRA Margin Debt Metrics** — finra_margin_debt_tracker, finra_may_2026_nominal_value, finra_may_2026_mom_change, finra_may_2026_yoy_change [INFERRED 0.85]

## Communities (43 total, 3 thin omitted)

### Community 0 - "Market Bubble Structural Analysis Report"
Cohesion: 0.07
Nodes (38): Graphify Rules Document, Graphify Query Rule, Graphify Workflow Document, NiceGUI Layout & Plotly Dashboard, Data Ingestion (DataIngestor), AGVI Implementation Plan Document, Feature Engineering Pipeline, XGBoost Model Training & Walk-Forward CV (+30 more)

### Community 1 - "test_mahalanobis.py"
Cohesion: 0.06
Nodes (38): Multidimensional Econometric & Quantitative Market Bubble Detection System.…, Regime Classification & Structural Break Machine Learning Subpackage.…, MacroMahalanobisDetector, DataFrame, ndarray, Macro Mahalanobis Distance Regime-Switching Bubble Detector.…, Multi-dimensional signed statistical distance regime-switching bubble detector., Derive stationary indicators if raw ticker series are present. (+30 more)

### Community 2 - "create_app"
Cohesion: 0.23
Nodes (9): create_cta_banner(), create_ios_card(), UI Accessible Components & iOS 13+ Design System Module.…, Render a high-impact Call-To-Action (CTA) section with heavy typography and…, Create an iOS 13+ inset card container with subtle elevation, rounded corners,…, create_app(), Toggle between light and dark theme modes., Create and initialize full NiceGUI application. (+1 more)

### Community 3 - "Implied Volatility Metrics Table (July 2026)"
Cohesion: 0.60
Nodes (6): Implied Volatility Metrics Table (July 2026), Implied Volatility Term Structure (Upward Sloping), VIX1D (8.73 - 11.61): Extreme near-term calm, VIX1Y (~23.00): Elevated long-term risk premium, VIX3M (~19.00): Anticipation of future turbulence, VIX Spot (15.57 - 17.16): Low baseline fear

### Community 4 - "config.py"
Cohesion: 0.11
Nodes (27): BubbleDetectorError, DataFetchError, IndicatorComputationError, Global Configuration, Logging Infrastructure & Constants Module.…, Root base exception for all domain-specific errors in the Bubble Detector…, Raised when financial market, macroeconomic, or provenance data acquisition…, Raised when econometric, technical, or topological indicator calculations fail.…, Raised when financial time-series integrity constraints or schemas are… (+19 more)

### Community 5 - "test_all_tabs_legends_right_flushed"
Cohesion: 0.18
Nodes (19): build_econometric_fig(), build_leverage_fig(), build_macro_valuation_fig(), build_sentiment_vol_fig(), get_figure_margin(), get_right_flushed_legend(), Figure, Return standard legend configuration for Panel WASM (desktop right-flushed vs… (+11 more)

### Community 6 - "StructuralBreakPredictor"
Cohesion: 0.10
Nodes (22): ModelTrainingError, Raised when machine learning or statistical regime estimation fails. Triggered…, Any, DataFrame, ndarray, Structural Break Machine Learning Classifier & Probability Calibration Module.…, Extract features and construct forward drawdown target variable without…, Train ML model and fit isotonic probability calibrator using expanding-window… (+14 more)

### Community 8 - "PortfolioBacktestEngine"
Cohesion: 0.08
Nodes (26): BacktestResult, PortfolioBacktestEngine, Any, DataFrame, ndarray, Institutional Cost-Inclusive Portfolio Backtest Simulation Engine.…, Execute comparative backtest across Dynamic Exposure, Buy & Hold, and Naive…, Simulate single portfolio with frictions, cash yields, and rebalancing costs. (+18 more)

### Community 9 - "compute_gsadf_gpt_decomposition"
Cohesion: 0.11
Nodes (24): calculate_adf_stat(), compute_gsadf_gpt_decomposition(), compute_wild_bootstrap_critical_values(), DataFrame, ndarray, Econometric Bubble Detection Module (Canonical PSY & GSADF).…, Compute wild bootstrap critical values (95% and 99%) under the null hypothesis…, Computes canonical recursive expanding-window Backward Supremum ADF (BSADF)… (+16 more)

### Community 11 - "Overview of Completed Implementation: Multidimensional Market Bubble Detector"
Cohesion: 0.17
Nodes (11): 10. Institutional Code Commentary, Packaging & Agent Navigation:, 1. System, Configuration & Date Horizons (`config.py` & `date_horizons.py`):, 2. UI & Accessibility Engine (`ui_theme.py`):, 3. Data Ingestion & Storage (`ingestor.py`):, 4. Quantitative Indicator Modules (`features/` & `features/utils.py`):, 5. Machine Learning Model (`structural_breaks.py`):, 6. Macro Mahalanobis Distance Engine (`regime_mahalanobis.py`):, 7. Interactive Dashboards & Dual-Runtime Architecture: (+3 more)

### Community 13 - "Detailed Slide Breakdown by Section & Group"
Cohesion: 0.20
Nodes (9): Detailed Slide Breakdown by Section & Group, Executive Presentation Deck Overview, Group 1: Key Findings (Group Confidence Score: 0.94), Group 2: Supporting Evidence: Valuation, Econometrics & ML (Group Confidence Score: 0.93), Group 3: Sector Specific Application: Tech vs. Energy (Group Confidence Score: 0.91), Group 4: Implications for Systemic Stability (Group Confidence Score: 0.95), Group 5: Strategic Recommendations (Group Confidence Score: 0.96), Verification Results (+1 more)

### Community 16 - "📉 Multidimensional Market Bubble Detector & Structural Break System"
Cohesion: 0.04
Nodes (44): 1. Continuous Backward Compounding (Cliff Eradication), 1. Macro Valuation Anchors, 1. Prerequisites & Virtual Environment, 2. Run the High-Performance NiceGUI Application, 2. Signed Macro Mahalanobis Distance & Directional Projection, 2. Systemic Liquidity & Leverage, 3. Dynamic Portfolio Equity Sizing ($w_{\text{equity}}$), 3. Econometric Explosive Bubble Diagnostics (+36 more)

### Community 17 - "dashboard.py"
Cohesion: 0.11
Nodes (30): build_econometric_chart(), build_leverage_chart(), build_macro_valuation_chart(), build_mahalanobis_chart(), build_sector_health_chart(), build_sentiment_vol_chart(), build_tech_exuberance_chart(), DashboardState (+22 more)

### Community 18 - "test_ui_ux_wasm_optimizations.py"
Cohesion: 0.14
Nodes (16): lttb_downsample(), Any, Downsample a 2D time series (dates, values) using the Largest Triangle Three…, Automated Test Suite for UI/UX WebAssembly Optimizations & Red Team…, Assert that dist/index.html compiled with WASM_BUILD_PACKAGING=1 is < 120 KB,…, Verify sw.js existence, cache versioning, and cache strategy rules., Verify that dist/index.html contains WCAG 2.2 AA accessibility and landmark…, Assert that downsampling a 13,045-point series to 1,000 points strictly retains… (+8 more)

### Community 19 - "test_data_provenance.py"
Cohesion: 0.14
Nodes (16): get_shiller_data(), parse_shiller_excel(), DataFrame, Path, Robert Shiller Monthly ie_data ETL & Point-in-Time Provenance Ingestor…, ETL Pipeline for Robert Shiller's monthly S&P Composite and CAPE dataset., Fetch Shiller data, parse real workbook and cache to parquet., Interpolate monthly Shiller series to daily business days with strictly causal… (+8 more)

### Community 20 - "test_wasm_pyodide_sandbox.py"
Cohesion: 0.08
Nodes (27): postprocess_wasm_content(), postprocess_wasm_html(), Path, Post-Processing Utility for Panel WebAssembly Compiled Artifacts…, Apply post-processing transformations to the compiled Panel WebAssembly HTML…, Apply post-processing transformations to the HTML content string. Pure…, apply_postprocessing(), Unit tests for WebAssembly Pyodide Sandbox Isolation, End-to-End Execution, and… (+19 more)

### Community 21 - "test_no_gaussian_bumps.py"
Cohesion: 0.17
Nodes (11): Institutional Data Provenance Certification & Anti-Synthetic Regression Suite.…, Certifies FRED nominal GDP and Case-Shiller index match official BEA/FRED…, Scans all source files in bubble_detector/data/ to certify that NO disguised…, Certifies Shiller ie_data.xls contains genuine S&P data from 1871 to present., Certifies CBOE VXO captures the exact 150.19 close on October 19, 1987., Certifies FINRA margin debt reflects true regulatory figures exceeding $1.4…, test_authentic_cboe_vxo_black_monday(), test_authentic_finra_margin_debt() (+3 more)

### Community 22 - "calculate_contrast_ratio"
Cohesion: 0.11
Nodes (23): calculate_contrast_ratio(), get_plotly_template(), get_theme_css(), is_wcag_aa_compliant(), parse_hex_color(), UI Theme and Accessibility Design System for Bubble Detector.…, UI Theme and Accessibility Design System Module (UI Package Binding).…, Return the Plotly template identifier for the specified theme mode. Parameters… (+15 more)

### Community 23 - "stage_provenance.py"
Cohesion: 0.13
Nodes (17): FinraETL, get_finra_margin_debt(), parse_finra_margin_debt_series(), DataFrame, Path, FINRA & NYSE Margin Debt Point-in-Time ETL Module.…, ETL Pipeline for FINRA & NYSE margin debt with strict publication lag…, Stage FINRA margin debt dataset to parquet. (+9 more)

### Community 24 - "FredETL"
Cohesion: 0.13
Nodes (18): FredETL, get_fred_data(), parse_fred_macro_series(), DataFrame, Path, FRED Macroeconomic & Global Liquidity Point-in-Time Data ETL Module.…, ETL Pipeline for FRED macroeconomic series with strict publication lag…, Stage FRED macro dataset to parquet. (+10 more)

### Community 25 - "DataIngestor"
Cohesion: 0.07
Nodes (25): DataIngestor, DataFrame, Path, Construct seamless asset time series with continuous backward return…, Merge authentic point-in-time macroeconomic series (Shiller CAPE, FRED GDP,…, High-performance ingestion engine orchestrating market prices, macroeconomic…, Fetch historical price and macroeconomic datasets for SPY, sectors, and…, ingestor() (+17 more)

### Community 26 - "features/__init__.py"
Cohesion: 0.22
Nodes (10): Quantitative Feature Engineering & Mathematical Signal Processing Subpackage.…, Macroeconomic Valuation & Long-Horizon Equilibrium Module.…, calculate_adf_stat(), normalize_tda_indicator(), ndarray, Shared Mathematical & Topological Utilities.…, Calculate Augmented Dickey-Fuller t-statistic for right-tailed explosive root…, Transform 1D time series into Takens delay-coordinate high-dimensional point… (+2 more)

### Community 27 - "compute_lppls_confidence_indicator"
Cohesion: 0.15
Nodes (17): calibrate_lppls_filimonov(), compute_lppls_confidence_indicator(), Any, DataFrame, ndarray, Log-Periodic Power Law Singularity (LPPLS) Module.…, Computes rolling multi-scale LPPLS Bubble Confidence Indicator CI(t) in [0.0,…, Calibrate the LPPLS model on log-prices using the Filimonov & Sornette (2013)… (+9 more)

### Community 29 - "compute_tda_wavelet_complexity"
Cohesion: 0.12
Nodes (25): _compute_morlet_wavelet_energy_and_entropy(), _compute_persistence_landscape_and_entropy(), _compute_rips_persistence_diagrams(), compute_tda_wavelet_complexity(), DataFrame, ndarray, Topological Data Analysis (TDA) & Wavelet Complexity Module.…, Calculate Peter Bubenik (2015) persistence landscape L2 norm and persistence… (+17 more)

### Community 30 - "compute_margin_leverage_metrics"
Cohesion: 0.18
Nodes (11): compute_margin_leverage_metrics(), DataFrame, Systemic Leverage & Margin Debt Dynamics Module.…, Compute FINRA Margin Debt YoY growth, velocity, leverage gap, and exhaustion…, Systemic Margin Leverage & Credit Exhaustion Indicator Module.…, test_compute_margin_leverage_metrics(), Unit tests for canonical module aliases and backward compatibility bindings.…, Verify margin_leverage module function matches canonical implementation. (+3 more)

### Community 31 - "VxoETL"
Cohesion: 0.16
Nodes (13): get_vxo_data(), parse_authentic_vxo_series(), DataFrame, Path, CBOE S&P 100 Volatility Index (^VXO) ETL & Historical Splicer (1986–Present).…, ETL Pipeline for CBOE VXO volatility index., Stage authentic VXO dataset to parquet., Get daily VXO series reindexed to requested business dates. (+5 more)

### Community 32 - "compute_technical_indicators"
Cohesion: 0.14
Nodes (13): compute_tech_exuberance_metrics(), Computes tech outperformance ratio (XLK / SPY), Macro Condition, Statistical…, Technical Indicators & Momentum Oscillators Module.…, compute_technical_indicators(), DataFrame, Technical Indicators & Momentum Oscillators Module.…, Append technical momentum, trend, and volatility indicators to the input Polars…, Fetch and process full dataset pipeline for selected date horizon. (+5 more)

### Community 33 - "build_tech_exuberance_fig"
Cohesion: 0.16
Nodes (14): build_tech_exuberance_fig(), fetch_dataset(), Build Plotly figure for Tab 7: Tech Exuberance Score (matching NiceGUI 100%)., Unit tests for WebAssembly Tab 7: Tech Exuberance Score & Parity Engine.…, Precompile WASM Parquet and JSON datasets to ensure up-to-date parquet/json…, Verify desktop construction of Tab 7 figure with 4 subplots and all expected…, Verify mobile construction with responsive horizontal legend and tight margins., Verify all required Tab 7 columns are registered in CORE_WASM_COLUMNS. (+6 more)

### Community 34 - "compute_exuberance_spans"
Cohesion: 0.22
Nodes (9): compute_exuberance_spans(), DataFrame, Tech Exuberance Score & Dual-Condition Integration Module.…, Extract contiguous start and end date intervals where Tech_Exuberance_Signal is…, Unit tests for Tech Exuberance Score: Dual Conditions (Macro & Statistical) &…, Asserts: 1. Condition_Macro triggers when M2 growth is slowing AND tech…, Verifies contiguous date span extraction for Plotly vrect highlight bands., test_compute_exuberance_spans() (+1 more)

### Community 35 - "generate_wasm_dataset"
Cohesion: 0.15
Nodes (18): compute_macro_valuations(), DataFrame, Compute Shiller CAPE, Payout-Adjusted CAPE (P-CAPE), and Buffett Indicator…, compute_options_volatility_metrics(), DataFrame, Compute VIX term structure slope, SKEW tail-risk alert, dispersion index, and…, generate_wasm_dataset(), Generate high-speed financial time series dataset for Pyodide WebAssembly.… (+10 more)

### Community 36 - "System Architecture and Operational Rules for Agents"
Cohesion: 0.40
Nodes (4): 1. Core Econometric & Statistical Rules, 2. Directory Layout & Key Modules, 3. Execution & Verification Rules, System Architecture and Operational Rules for Agents

### Community 37 - "get_current_date"
Cohesion: 0.43
Nodes (7): get_current_date(), get_dynamic_50yr_date_range(), get_dynamic_horizon_metadata(), Any, date, Return current execution date, or parse override date string/object., Compute rolling 50-year date range from current execution date. Safely handles…

### Community 38 - "test_full_indicator_parity.py"
Cohesion: 0.29
Nodes (7): Exception, parametrize, Comprehensive Parity Test: Verifies 100% Numerical Parity across all 15…, Assert that every single indicator across all 7 tabs in the WebAssembly app is…, Rigorously test the Pyodide WebAssembly fallback branch by mocking out…, test_all_indicators_numerical_parity(), test_wasm_fallback_numerical_parity()

### Community 39 - "test_wasm_parquet_parity.py"
Cohesion: 0.40
Nodes (4): parametrize, Unit tests for WebAssembly Parquet Parity and Zero-Mathematical-Drift Loading., Asserts Pyodide WebAssembly dataset matches NiceGUI dataset with zero…, test_wasm_loads_exact_parquet_dataset()

### Community 41 - "[3.1.0] - 2026-10-05"
Cohesion: 0.33
Nodes (5): [3.0.0] - 2026-09-03, [3.1.0] - 2026-10-05, Added, Changed, Changelog

### Community 46 - "panel_dashboard.py"
Cohesion: 0.18
Nodes (17): build_mahalanobis_fig(), build_sector_health_fig(), generate_explanatory_markdown(), lttb_downsample(), normalize_tda_indicator(), precompile_wasm_parquet_datasets(), _prepare_trace(), ndarray (+9 more)

## Knowledge Gaps
- **73 isolated node(s):** `market-bubble-detector`, `PRECACHE_ASSETS`, `1. Core Econometric & Statistical Rules`, `2. Directory Layout & Key Modules`, `3. Execution & Verification Rules` (+68 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 380 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `MacroMahalanobisDetector` connect `test_mahalanobis.py` to `compute_technical_indicators`, `generate_wasm_dataset`, `panel_dashboard.py`, `dashboard.py`, `stage_provenance.py`, `DataIngestor`?**
  _High betweenness centrality (0.082) - this node is a cross-community bridge._
- **Why does `DataIngestor` connect `DataIngestor` to `compute_technical_indicators`, `test_mahalanobis.py`, `generate_wasm_dataset`, `config.py`, `panel_dashboard.py`, `dashboard.py`, `stage_provenance.py`?**
  _High betweenness centrality (0.062) - this node is a cross-community bridge._
- **Why does `DashboardState` connect `dashboard.py` to `compute_technical_indicators`, `test_mahalanobis.py`, `create_app`, `config.py`, `test_all_tabs_legends_right_flushed`, `StructuralBreakPredictor`, `test_full_indicator_parity.py`, `PortfolioBacktestEngine`, `test_wasm_parquet_parity.py`, `panel_dashboard.py`, `calculate_contrast_ratio`, `DataIngestor`?**
  _High betweenness centrality (0.060) - this node is a cross-community bridge._
- **Are the 6 inferred relationships involving `DashboardState` (e.g. with `PortfolioBacktestEngine` and `DataIngestor`) actually correct?**
  _`DashboardState` has 6 INFERRED edges - model-reasoned connections that need verification._
- **Are the 6 inferred relationships involving `DataIngestor` (e.g. with `DashboardState` and `ingestor()`) actually correct?**
  _`DataIngestor` has 6 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `StructuralBreakPredictor` (e.g. with `ModelTrainingError` and `DashboardState`) actually correct?**
  _`StructuralBreakPredictor` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `market-bubble-detector`, `PRECACHE_ASSETS`, `1. Core Econometric & Statistical Rules` to the rest of the system?**
  _73 weakly-connected nodes found - possible documentation gaps or missing edges._