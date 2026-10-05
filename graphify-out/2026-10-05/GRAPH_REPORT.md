# Graph Report - Merrill  (2026-10-05)

## Corpus Check
- 82 files · ~105,956 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 747 nodes · 1386 edges · 49 communities (36 shown, 9 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 35 edges (avg confidence: 0.89)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `dff2e7ac`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Market Bubble Structural Analysis Report
- test_mahalanobis.py
- generate_wasm_dataset
- Implied Volatility Metrics Table (July 2026)
- config.py
- panel_dashboard.py
- StructuralBreakPredictor
- market-bubble-detector
- PortfolioBacktestEngine
- test_bsadf_rigor.py
- Overview of Completed Implementation: Multidimensional Market Bubble Detector
- Detailed Slide Breakdown by Section & Group
- 📉 Multidimensional Market Bubble Detector & Structural Break System
- dashboard.py
- test_ui_ux_wasm_optimizations.py
- ShillerETL
- postprocess_wasm_content
- test_no_gaussian_bumps.py
- calculate_contrast_ratio
- test_data_provenance.py
- FredETL
- DataIngestor
- features/__init__.py
- compute_lppls_confidence_indicator
- compute_options_volatility_metrics
- compute_tda_wavelet_complexity
- compute_margin_leverage_metrics
- VxoETL
- compute_technical_indicators
- test_wasm_tech_exuberance.py
- compute_exuberance_spans
- test_features.py
- System Architecture and Operational Rules for Agents
- get_current_date
- stage_provenance.py
- compute_gsadf_gpt_decomposition
- sw.js
- [3.1.0] - 2026-10-05
- test_wasm_full_script_pyodide_execution
- test_wasm_full_script_pure_numpy_fallback_execution
- test_template_and_cards_reconstruction
- test_dist_index_html_on_disk
- precompile_wasm_parquet_datasets
- .load_data
- test_json_datasets_staging

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
- `sample_df()` --uses--> `DataIngestor`  [INFERRED]
  tests/test_features.py → bubble_detector/data/ingestor.py
- `processed_df()` --uses--> `DataIngestor`  [INFERRED]
  tests/test_models.py → bubble_detector/data/ingestor.py
- `test_predict_drawdown_probability()` --calls--> `StructuralBreakPredictor`  [EXTRACTED]
  tests/test_models.py → bubble_detector/models/structural_breaks.py
- `test_structural_break_predictor_walk_forward()` --calls--> `StructuralBreakPredictor`  [EXTRACTED]
  tests/test_models.py → bubble_detector/models/structural_breaks.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Econometric and Mathematical Bubble Detection Framework** — marketbubble_ddfv100_gsadf_psy_procedure, marketbubble_ddfv100_tda_wavelet, marketbubble_ddfv100_lppls_model [EXTRACTED 1.00]
- **AGVI Indicator and Feature Engineering Pipeline** — marketbubble_ddfv100_shiller_cape_ratio, marketbubble_ddfv100_payout_adjusted_cape, marketbubble_ddfv100_buffett_indicator, marketbubble_ddfv100_gsadf_psy_procedure [EXTRACTED 1.00]
- **FINRA Margin Debt Metrics** — finra_margin_debt_tracker, finra_may_2026_nominal_value, finra_may_2026_mom_change, finra_may_2026_yoy_change [INFERRED 0.85]
- **Implied Volatility Term Structure Components** — impliedvolatilitymetric_vix1d, impliedvolatilitymetric_vix_spot, impliedvolatilitymetric_vix3m, impliedvolatilitymetric_vix1y [EXTRACTED 1.00]

## Communities (49 total, 9 thin omitted)

### Community 0 - "Market Bubble Structural Analysis Report"
Cohesion: 0.07
Nodes (38): Graphify Rules Document, Graphify Query Rule, Graphify Workflow Document, NiceGUI Layout & Plotly Dashboard, Data Ingestion (DataIngestor), AGVI Implementation Plan Document, Feature Engineering Pipeline, XGBoost Model Training & Walk-Forward CV (+30 more)

### Community 1 - "test_mahalanobis.py"
Cohesion: 0.06
Nodes (41): Multidimensional Econometric & Quantitative Market Bubble Detection System.…, Regime Classification & Structural Break Machine Learning Subpackage.…, MacroMahalanobisDetector, DataFrame, ndarray, Macro Mahalanobis Distance Regime-Switching Bubble Detector.…, Multi-dimensional signed statistical distance regime-switching bubble detector., Derive stationary indicators if raw ticker series are present. (+33 more)

### Community 2 - "generate_wasm_dataset"
Cohesion: 0.20
Nodes (10): generate_wasm_dataset(), Generate high-speed financial time series dataset for Pyodide WebAssembly.…, Verify 100% numerical parity for TDA Persistence L2 Norm between WASM app and…, test_tda_wasm_parity(), Verify pure NumPy fallback operates with zero dependencies when neither parquet…, Verify candidate dataset selection correctly maps 50-year rolling horizons to…, Simulate Pyodide MEMFS where polars and bubble_detector are unavailable, and…, test_date_horizon_selector_robust_against_year_shift() (+2 more)

### Community 3 - "Implied Volatility Metrics Table (July 2026)"
Cohesion: 0.60
Nodes (6): Implied Volatility Metrics Table (July 2026), Implied Volatility Term Structure (Upward Sloping), VIX1D (8.73 - 11.61): Extreme near-term calm, VIX1Y (~23.00): Elevated long-term risk premium, VIX3M (~19.00): Anticipation of future turbulence, VIX Spot (15.57 - 17.16): Low baseline fear

### Community 4 - "config.py"
Cohesion: 0.10
Nodes (28): BubbleDetectorError, DataFetchError, IndicatorComputationError, Global Configuration, Logging Infrastructure & Constants Module.…, Root base exception for all domain-specific errors in the Bubble Detector…, Raised when financial market, macroeconomic, or provenance data acquisition…, Raised when econometric, technical, or topological indicator calculations fail.…, Raised when financial time-series integrity constraints or schemas are… (+20 more)

### Community 5 - "panel_dashboard.py"
Cohesion: 0.17
Nodes (32): build_econometric_fig(), build_leverage_fig(), build_macro_valuation_fig(), build_mahalanobis_fig(), build_sector_health_fig(), build_sentiment_vol_fig(), build_tech_exuberance_fig(), fetch_dataset() (+24 more)

### Community 6 - "StructuralBreakPredictor"
Cohesion: 0.12
Nodes (19): ModelTrainingError, Raised when machine learning or statistical regime estimation fails. Triggered…, Any, DataFrame, ndarray, Extract features and construct forward drawdown target variable without…, Train ML model and fit isotonic probability calibrator using expanding-window…, Predict calibrated structural break drawdown probabilities. (+11 more)

### Community 8 - "PortfolioBacktestEngine"
Cohesion: 0.08
Nodes (26): BacktestResult, PortfolioBacktestEngine, Any, DataFrame, ndarray, Institutional Cost-Inclusive Portfolio Backtest Simulation Engine.…, Execute comparative backtest across Dynamic Exposure, Buy & Hold, and Naive…, Simulate single portfolio with frictions, cash yields, and rebalancing costs. (+18 more)

### Community 9 - "test_bsadf_rigor.py"
Cohesion: 0.16
Nodes (15): calculate_adf_stat(), compute_wild_bootstrap_critical_values(), ndarray, Econometric Bubble Detection Module (Canonical PSY & GSADF).…, Compute wild bootstrap critical values (95% and 99%) under the null hypothesis…, Calculate Augmented Dickey-Fuller t-statistic for right-tailed explosive root…, Unit tests for Econometric Rigor: Canonical PSY (2015) Recursive BSADF & GPT…, Verifies Rademacher wild bootstrap critical values remain within empirical… (+7 more)

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
Cohesion: 0.06
Nodes (54): create_cta_banner(), create_ios_card(), UI Accessible Components & iOS 13+ Design System Module.…, Render a high-impact Call-To-Action (CTA) section with heavy typography and…, Create an iOS 13+ inset card container with subtle elevation, rounded corners,…, build_econometric_chart(), build_leverage_chart(), build_macro_valuation_chart() (+46 more)

### Community 18 - "test_ui_ux_wasm_optimizations.py"
Cohesion: 0.12
Nodes (18): lttb_downsample(), Any, Downsample a 2D time series (dates, values) using the Largest Triangle Three…, Automated Test Suite for UI/UX WebAssembly Optimizations & Red Team…, Assert that dist/index.html compiled with WASM_BUILD_PACKAGING=1 is < 120 KB,…, Verify sw.js existence, cache versioning, and cache strategy rules., Verify that dist/index.html contains WCAG 2.2 AA accessibility and landmark…, Verify desktop vs mobile legend orientations and margin allocations. (+10 more)

### Community 19 - "ShillerETL"
Cohesion: 0.16
Nodes (13): get_shiller_data(), parse_shiller_excel(), DataFrame, Path, Robert Shiller Monthly ie_data ETL & Point-in-Time Provenance Ingestor…, ETL Pipeline for Robert Shiller's monthly S&P Composite and CAPE dataset., Fetch Shiller data, parse real workbook and cache to parquet., Interpolate monthly Shiller series to daily business days with strictly causal… (+5 more)

### Community 20 - "postprocess_wasm_content"
Cohesion: 0.20
Nodes (10): postprocess_wasm_content(), postprocess_wasm_html(), Path, Post-Processing Utility for Panel WebAssembly Compiled Artifacts…, Apply post-processing transformations to the compiled Panel WebAssembly HTML…, Apply post-processing transformations to the HTML content string. Pure…, apply_postprocessing(), Helper delegating to the production WebAssembly postprocessing engine. (+2 more)

### Community 21 - "test_no_gaussian_bumps.py"
Cohesion: 0.17
Nodes (11): Institutional Data Provenance Certification & Anti-Synthetic Regression Suite.…, Certifies FRED nominal GDP and Case-Shiller index match official BEA/FRED…, Scans all source files in bubble_detector/data/ to certify that NO disguised…, Certifies Shiller ie_data.xls contains genuine S&P data from 1871 to present., Certifies CBOE VXO captures the exact 150.19 close on October 19, 1987., Certifies FINRA margin debt reflects true regulatory figures exceeding $1.4…, test_authentic_cboe_vxo_black_monday(), test_authentic_finra_margin_debt() (+3 more)

### Community 22 - "calculate_contrast_ratio"
Cohesion: 0.11
Nodes (23): calculate_contrast_ratio(), get_plotly_template(), get_theme_css(), is_wcag_aa_compliant(), parse_hex_color(), UI Theme and Accessibility Design System for Bubble Detector.…, UI Theme and Accessibility Design System Module (UI Package Binding).…, Return the Plotly template identifier for the specified theme mode. Parameters… (+15 more)

### Community 23 - "test_data_provenance.py"
Cohesion: 0.14
Nodes (16): FinraETL, get_finra_margin_debt(), parse_finra_margin_debt_series(), DataFrame, Path, FINRA & NYSE Margin Debt Point-in-Time ETL Module.…, ETL Pipeline for FINRA & NYSE margin debt with strict publication lag…, Stage FINRA margin debt dataset to parquet. (+8 more)

### Community 24 - "FredETL"
Cohesion: 0.13
Nodes (18): FredETL, get_fred_data(), parse_fred_macro_series(), DataFrame, Path, FRED Macroeconomic & Global Liquidity Point-in-Time Data ETL Module.…, ETL Pipeline for FRED macroeconomic series with strict publication lag…, Stage FRED macro dataset to parquet. (+10 more)

### Community 25 - "DataIngestor"
Cohesion: 0.08
Nodes (23): DataIngestor, DataFrame, Path, Construct seamless asset time series with continuous backward return…, Merge authentic point-in-time macroeconomic series (Shiller CAPE, FRED GDP,…, High-performance ingestion engine orchestrating market prices, macroeconomic…, Fetch historical price and macroeconomic datasets for SPY, sectors, and…, ingestor() (+15 more)

### Community 26 - "features/__init__.py"
Cohesion: 0.27
Nodes (9): Quantitative Feature Engineering & Mathematical Signal Processing Subpackage.…, calculate_adf_stat(), normalize_tda_indicator(), ndarray, Shared Mathematical & Topological Utilities.…, Calculate Augmented Dickey-Fuller t-statistic for right-tailed explosive root…, Transform 1D time series into Takens delay-coordinate high-dimensional point…, Causally rescale raw TDA Persistence Landscape L2 Norm to span [target_min,… (+1 more)

### Community 27 - "compute_lppls_confidence_indicator"
Cohesion: 0.16
Nodes (15): calibrate_lppls_filimonov(), compute_lppls_confidence_indicator(), Any, DataFrame, ndarray, Log-Periodic Power Law Singularity (LPPLS) Module.…, Computes rolling multi-scale LPPLS Bubble Confidence Indicator CI(t) in [0.0,…, Calibrate the LPPLS model on log-prices using the Filimonov & Sornette (2013)… (+7 more)

### Community 28 - "compute_options_volatility_metrics"
Cohesion: 0.22
Nodes (8): compute_options_volatility_metrics(), DataFrame, Options Market Microstructure & Volatility Behavioral Dynamics Module.…, Compute VIX term structure slope, SKEW tail-risk alert, dispersion index, and…, Options Market Microstructure & Volatility Behavioral Dynamics Module.…, test_compute_options_volatility_metrics(), Verify options_volatility module function matches canonical implementation., test_options_volatility_alias_parity()

### Community 29 - "compute_tda_wavelet_complexity"
Cohesion: 0.10
Nodes (28): _compute_morlet_wavelet_energy_and_entropy(), _compute_persistence_landscape_and_entropy(), _compute_rips_persistence_diagrams(), compute_tda_wavelet_complexity(), DataFrame, ndarray, Topological Data Analysis (TDA) & Wavelet Complexity Module.…, Calculate Peter Bubenik (2015) persistence landscape L2 norm and persistence… (+20 more)

### Community 30 - "compute_margin_leverage_metrics"
Cohesion: 0.22
Nodes (8): compute_margin_leverage_metrics(), DataFrame, Systemic Leverage & Margin Debt Dynamics Module.…, Compute FINRA Margin Debt YoY growth, velocity, leverage gap, and exhaustion…, Systemic Margin Leverage & Credit Exhaustion Indicator Module.…, test_compute_margin_leverage_metrics(), Verify margin_leverage module function matches canonical implementation., test_margin_leverage_alias_parity()

### Community 31 - "VxoETL"
Cohesion: 0.16
Nodes (13): get_vxo_data(), parse_authentic_vxo_series(), DataFrame, Path, CBOE S&P 100 Volatility Index (^VXO) ETL & Historical Splicer (1986–Present).…, ETL Pipeline for CBOE VXO volatility index., Stage authentic VXO dataset to parquet., Get daily VXO series reindexed to requested business dates. (+5 more)

### Community 32 - "compute_technical_indicators"
Cohesion: 0.24
Nodes (8): Technical Indicators & Momentum Oscillators Module.…, compute_technical_indicators(), DataFrame, Append technical momentum, trend, and volatility indicators to the input Polars…, test_compute_technical_indicators(), Unit tests for canonical module aliases and backward compatibility bindings.…, Verify technical module function matches canonical implementation., test_technical_alias_parity()

### Community 33 - "test_wasm_tech_exuberance.py"
Cohesion: 0.17
Nodes (11): Unit tests for WebAssembly Tab 7: Tech Exuberance Score & Parity Engine.…, Precompile WASM Parquet and JSON datasets to ensure up-to-date parquet/json…, Verify desktop construction of Tab 7 figure with 4 subplots and all expected…, Verify mobile construction with responsive horizontal legend and tight margins., Verify all required Tab 7 columns are registered in CORE_WASM_COLUMNS., Verify Tab 7 is bound to dashboard_tabs with title 'Tech Exuberance Score'., test_pane_tech_exuberance_in_dashboard_tabs(), test_precompile_wasm_parquet_datasets() (+3 more)

### Community 34 - "compute_exuberance_spans"
Cohesion: 0.22
Nodes (9): compute_exuberance_spans(), DataFrame, Tech Exuberance Score & Dual-Condition Integration Module.…, Extract contiguous start and end date intervals where Tech_Exuberance_Signal is…, Unit tests for Tech Exuberance Score: Dual Conditions (Macro & Statistical) &…, Asserts: 1. Condition_Macro triggers when M2 growth is slowing AND tech…, Verifies contiguous date span extraction for Plotly vrect highlight bands., test_compute_exuberance_spans() (+1 more)

### Community 35 - "test_features.py"
Cohesion: 0.22
Nodes (8): compute_macro_valuations(), DataFrame, Macroeconomic Valuation & Long-Horizon Equilibrium Module.…, Compute Shiller CAPE, Payout-Adjusted CAPE (P-CAPE), and Buffett Indicator…, fixture, Unit tests for Feature Engineering Modules (technicals, macro valuations,…, sample_df(), test_compute_macro_valuations()

### Community 36 - "System Architecture and Operational Rules for Agents"
Cohesion: 0.40
Nodes (4): 1. Core Econometric & Statistical Rules, 2. Directory Layout & Key Modules, 3. Execution & Verification Rules, System Architecture and Operational Rules for Agents

### Community 37 - "get_current_date"
Cohesion: 0.43
Nodes (7): get_current_date(), get_dynamic_50yr_date_range(), get_dynamic_horizon_metadata(), Any, date, Return current execution date, or parse override date string/object., Compute rolling 50-year date range from current execution date. Safely handles…

### Community 38 - "stage_provenance.py"
Cohesion: 0.31
Nodes (8): compute_tech_exuberance_metrics(), Computes tech outperformance ratio (XLK / SPY), Macro Condition, Statistical…, precompile_wasm_parquet_datasets(), Provenance Data Staging & WebAssembly Binary Pre-Compilation Pipeline.…, Convert existing staged Parquet datasets into clean JSON tables for WebAssembly…, Pre-compile production Parquet and lightweight clean JSON datasets for client-…, stage_all(), sync_parquet_to_json()

### Community 39 - "compute_gsadf_gpt_decomposition"
Cohesion: 0.22
Nodes (9): compute_gsadf_gpt_decomposition(), DataFrame, Computes canonical recursive expanding-window Backward Supremum ADF (BSADF)…, test_compute_gsadf_gpt_decomposition(), processed_df(), fixture, Unit tests for StructuralBreakPredictor machine learning module., test_predict_drawdown_probability() (+1 more)

### Community 41 - "[3.1.0] - 2026-10-05"
Cohesion: 0.33
Nodes (5): [3.0.0] - 2026-09-03, [3.1.0] - 2026-10-05, Added, Changed, Changelog

## Knowledge Gaps
- **73 isolated node(s):** `market-bubble-detector`, `PRECACHE_ASSETS`, `1. Core Econometric & Statistical Rules`, `2. Directory Layout & Key Modules`, `3. Execution & Verification Rules` (+68 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 378 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **9 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `MacroMahalanobisDetector` connect `test_mahalanobis.py` to `generate_wasm_dataset`, `panel_dashboard.py`, `stage_provenance.py`, `.load_data`, `dashboard.py`?**
  _High betweenness centrality (0.083) - this node is a cross-community bridge._
- **Why does `DataIngestor` connect `DataIngestor` to `test_mahalanobis.py`, `generate_wasm_dataset`, `test_features.py`, `config.py`, `panel_dashboard.py`, `stage_provenance.py`, `compute_gsadf_gpt_decomposition`, `.load_data`, `dashboard.py`?**
  _High betweenness centrality (0.063) - this node is a cross-community bridge._
- **Why does `DashboardState` connect `dashboard.py` to `test_mahalanobis.py`, `config.py`, `StructuralBreakPredictor`, `PortfolioBacktestEngine`, `.load_data`, `calculate_contrast_ratio`, `DataIngestor`?**
  _High betweenness centrality (0.060) - this node is a cross-community bridge._
- **Are the 6 inferred relationships involving `DashboardState` (e.g. with `PortfolioBacktestEngine` and `DataIngestor`) actually correct?**
  _`DashboardState` has 6 INFERRED edges - model-reasoned connections that need verification._
- **Are the 6 inferred relationships involving `DataIngestor` (e.g. with `DashboardState` and `ingestor()`) actually correct?**
  _`DataIngestor` has 6 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `StructuralBreakPredictor` (e.g. with `ModelTrainingError` and `DashboardState`) actually correct?**
  _`StructuralBreakPredictor` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `market-bubble-detector`, `PRECACHE_ASSETS`, `1. Core Econometric & Statistical Rules` to the rest of the system?**
  _73 weakly-connected nodes found - possible documentation gaps or missing edges._