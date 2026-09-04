# Graph Report - Merrill  (2026-09-03)

## Corpus Check
- 73 files · ~435,654 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 659 nodes · 1252 edges · 47 communities (40 shown, 7 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 41 edges (avg confidence: 0.78)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `574783da`
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
- test_ui_ux_wasm_optimizations.py
- AGVI Technical Specification Document
- etl_shiller.py
- etl_vxo.py
- ingestor.py
- etl_finra.py
- etl_fred.py
- generate_wasm_dataset
- __init__.py
- __init__.py
- test_features.py
- stage_provenance.py
- compute_margin_leverage_metrics
- test_no_synthetic_gaussian_bumps_in_data_code
- compute_technical_indicators
- test_splicing_continuity.py
- ._append_real_macro_indicators
- compute_macro_valuations
- System Architecture and Operational Rules for Agents
- get_current_date
- apply_postprocessing
- test_ingestor.py
- sw.js
- mock_indicators_df
- test_wasm_full_script_pyodide_execution
- test_wasm_full_script_pure_numpy_fallback_execution
- test_template_and_cards_reconstruction
- test_dist_index_html_on_disk
- precompile_wasm_parquet_datasets

## God Nodes (most connected - your core abstractions)
1. `DashboardState` - 38 edges
2. `MacroMahalanobisDetector` - 35 edges
3. `DataIngestor` - 30 edges
4. `StructuralBreakPredictor` - 26 edges
5. `generate_wasm_dataset()` - 24 edges
6. `compute_tda_wavelet_complexity()` - 22 edges
7. `compute_gsadf_gpt_decomposition()` - 19 edges
8. `compute_margin_leverage_metrics()` - 19 edges
9. `compute_options_volatility_metrics()` - 19 edges
10. `compute_technical_indicators()` - 18 edges

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

## Communities (47 total, 7 thin omitted)

### Community 0 - "Merrill ETF Portfolio Reviews"
Cohesion: 0.06
Nodes (46): Graphify Rules Document, Graphify Query Rule, Graphify Workflow Document, NiceGUI Layout & Plotly Dashboard, Data Ingestion (DataIngestor), AGVI Implementation Plan Document, Feature Engineering Pipeline, XGBoost Model Training & Walk-Forward CV (+38 more)

### Community 1 - "AGVI System Pipeline and Dashboard"
Cohesion: 0.06
Nodes (33): Regime Classification & Structural Break Machine Learning Subpackage. ==========, MacroMahalanobisDetector, DataFrame, ndarray, Macro Mahalanobis Distance Regime-Switching Bubble Detector. ===================, Multi-dimensional signed statistical distance regime-switching bubble detector., Derive stationary indicators if raw ticker series are present., Transform indicators into stationary, standardized rolling z-scores         with (+25 more)

### Community 2 - "Econometric Bubble Detection Models"
Cohesion: 0.20
Nodes (10): generate_wasm_dataset(), Generate high-speed financial time series dataset for Pyodide WebAssembly.     S, Verify 100% numerical parity for TDA Persistence L2 Norm between WASM app and to, test_tda_wasm_parity(), Verify pure NumPy fallback operates with zero dependencies when     neither parq, Verify candidate dataset selection correctly maps 50-year rolling horizons to ma, Simulate Pyodide MEMFS where polars and bubble_detector are unavailable,     and, test_date_horizon_selector_robust_against_year_shift() (+2 more)

### Community 3 - "Implied Volatility Term Structure Metrics"
Cohesion: 0.60
Nodes (6): Implied Volatility Metrics Table (July 2026), Implied Volatility Term Structure (Upward Sloping), VIX1D (8.73 - 11.61): Extreme near-term calm, VIX1Y (~23.00): Elevated long-term risk premium, VIX3M (~19.00): Anticipation of future turbulence, VIX Spot (15.57 - 17.16): Low baseline fear

### Community 4 - "Graphify Settings and Rules"
Cohesion: 0.15
Nodes (19): Global Configuration, Logging Infrastructure & Constants Module. ===============, get_current_date(), get_dynamic_50yr_date_range(), get_dynamic_horizon_metadata(), Any, date, Dynamic 50-Year Multi-Horizon Date Engine. =====================================, Construct dynamic horizon metadata dictionary anchored to the operational execut (+11 more)

### Community 5 - "Valuation and Feature Engineering"
Cohesion: 0.20
Nodes (23): build_econometric_fig(), build_leverage_fig(), build_macro_valuation_fig(), build_sector_health_fig(), build_sentiment_vol_fig(), fetch_dataset(), generate_explanatory_markdown(), get_figure_margin() (+15 more)

### Community 6 - "FINRA Margin Debt Metrics"
Cohesion: 0.10
Nodes (20): Any, DataFrame, ndarray, Structural Break Machine Learning Classifier & Probability Calibration Module. =, Extract features and construct forward drawdown target variable without lookahea, Train ML model and fit isotonic probability calibrator using expanding-window, Predict calibrated structural break drawdown probabilities., Calculate Brier Score: BS = (1/N) * sum((y_prob - y_true)^2). (+12 more)

### Community 8 - "test_ui_theme.py"
Cohesion: 0.08
Nodes (26): BacktestResult, PortfolioBacktestEngine, Any, DataFrame, ndarray, Institutional Cost-Inclusive Portfolio Backtest Simulation Engine. =============, Execute comparative backtest across Dynamic Exposure, Buy & Hold, and Naive CAPE, Simulate single portfolio with frictions, cash yields, and rebalancing costs. (+18 more)

### Community 9 - "__init__.py"
Cohesion: 0.16
Nodes (14): calculate_adf_stat(), compute_gsadf_gpt_decomposition(), compute_wild_bootstrap_critical_values(), DataFrame, ndarray, Econometric Bubble Detection Module (Canonical PSY & GSADF). ===================, Computes canonical recursive expanding-window GSADF explosive test statistics, Calculate Augmented Dickey-Fuller t-statistic for right-tailed explosive root te (+6 more)

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
Cohesion: 0.07
Nodes (42): create_cta_banner(), create_ios_card(), UI Accessible Components & iOS 13+ Design System Module. =======================, Render a high-impact Call-To-Action (CTA) section with heavy typography and acce, Create an iOS 13+ inset card container with subtle elevation, rounded corners, a, build_econometric_chart(), build_leverage_chart(), build_macro_valuation_chart() (+34 more)

### Community 18 - "test_ui_ux_wasm_optimizations.py"
Cohesion: 0.12
Nodes (18): lttb_downsample(), Any, Downsample a 2D time series (dates, values) using the Largest Triangle Three Buc, Automated Test Suite for UI/UX WebAssembly Optimizations & Red Team Remediation., Assert that dist/index.html compiled with WASM_BUILD_PACKAGING=1 is < 120 KB,, Verify sw.js existence, cache versioning, and cache strategy rules., Verify that dist/index.html contains WCAG 2.2 AA accessibility and landmark enha, Verify desktop vs mobile legend orientations and margin allocations. (+10 more)

### Community 19 - "AGVI Technical Specification Document"
Cohesion: 0.16
Nodes (14): get_shiller_data(), parse_shiller_excel(), DataFrame, Path, Robert Shiller Monthly ie_data ETL & Point-in-Time Provenance Ingestor (1871–Pre, ETL Pipeline for Robert Shiller's monthly S&P Composite and CAPE dataset., Fetch Shiller data, parse real workbook and cache to parquet., Interpolate monthly Shiller series to daily business days with strictly causal (+6 more)

### Community 20 - "etl_shiller.py"
Cohesion: 0.20
Nodes (10): postprocess_wasm_content(), postprocess_wasm_html(), Path, Post-Processing Utility for Panel WebAssembly Compiled Artifacts (`dist/index.ht, Apply post-processing transformations to the compiled Panel WebAssembly HTML bun, Apply post-processing transformations to the HTML content string.     Pure trans, apply_postprocessing(), Helper delegating to the production WebAssembly postprocessing engine. (+2 more)

### Community 21 - "etl_vxo.py"
Cohesion: 0.20
Nodes (9): Institutional Data Provenance Certification & Anti-Synthetic Regression Suite., Certifies FRED nominal GDP and Case-Shiller index match official BEA/FRED public, Scans all source files in bubble_detector/data/ to certify that NO disguised, Certifies Shiller ie_data.xls contains genuine S&P data from 1871 to present., Certifies FINRA margin debt reflects true regulatory figures exceeding $1.4 Tril, test_authentic_finra_margin_debt(), test_authentic_fred_gdp_and_housing(), test_authentic_shiller_provenance_workbook() (+1 more)

### Community 22 - "ingestor.py"
Cohesion: 0.12
Nodes (23): calculate_contrast_ratio(), get_plotly_template(), get_theme_css(), is_wcag_aa_compliant(), parse_hex_color(), UI Theme and Accessibility Design System for Bubble Detector. ==================, UI Theme and Accessibility Design System Module (UI Package Binding). ==========, Return the Plotly template identifier for the specified theme mode.      Paramet (+15 more)

### Community 23 - "etl_finra.py"
Cohesion: 0.17
Nodes (13): FinraETL, get_finra_margin_debt(), parse_finra_margin_debt_series(), DataFrame, Path, FINRA & NYSE Margin Debt Point-in-Time ETL Module. =============================, ETL Pipeline for FINRA & NYSE margin debt with strict publication lag constraint, Stage FINRA margin debt dataset to parquet. (+5 more)

### Community 24 - "etl_fred.py"
Cohesion: 0.17
Nodes (13): FredETL, get_fred_data(), parse_fred_macro_series(), DataFrame, Path, FRED Macroeconomic Point-in-Time Data ETL Module. ==============================, ETL Pipeline for FRED macroeconomic series with strict publication lag constrain, Stage FRED macro dataset to parquet. (+5 more)

### Community 25 - "generate_wasm_dataset"
Cohesion: 0.18
Nodes (8): DataIngestor, Path, High-performance ingestion engine orchestrating market prices, macroeconomic ETL, sample_df(), ingestor(), Unit tests for DataIngestor module., processed_df(), Unit tests for StructuralBreakPredictor machine learning module.

### Community 26 - "__init__.py"
Cohesion: 0.28
Nodes (8): calculate_adf_stat(), normalize_tda_indicator(), ndarray, Shared Mathematical & Topological Utilities. ===================================, Calculate Augmented Dickey-Fuller t-statistic for right-tailed explosive root te, Transform 1D time series into Takens delay-coordinate high-dimensional point clo, Causally rescale raw TDA Persistence Landscape L2 Norm to span [target_min, targ, takens_embedding()

### Community 27 - "__init__.py"
Cohesion: 0.14
Nodes (14): BubbleDetectorError, DataFetchError, IndicatorComputationError, ModelTrainingError, Root base exception for all domain-specific errors in the Bubble Detector ecosys, Raised when financial market, macroeconomic, or provenance data acquisition fail, Raised when econometric, technical, or topological indicator calculations fail., Raised when machine learning or statistical regime estimation fails.      Trigge (+6 more)

### Community 28 - "test_features.py"
Cohesion: 0.15
Nodes (13): compute_options_volatility_metrics(), DataFrame, Options Market Microstructure & Volatility Behavioral Dynamics Module. =========, Compute VIX term structure slope, SKEW tail-risk alert, dispersion index, and cr, Options Market Microstructure & Volatility Behavioral Dynamics Module. =========, test_compute_options_volatility_metrics(), Unit tests for canonical module aliases and backward compatibility bindings.  Ve, Verify margin_leverage module function matches canonical implementation. (+5 more)

### Community 29 - "stage_provenance.py"
Cohesion: 0.18
Nodes (14): _compute_rips_persistence_diagrams(), compute_tda_wavelet_complexity(), _persistence_landscape_l2_norm(), DataFrame, ndarray, Topological Data Analysis (TDA) & Wavelet Complexity Module. ===================, Calculate Bubenik (2015) persistence landscape L2 norm representing topological, Compute sliding window Vietoris-Rips persistent homology L2 norm and Morlet Wave (+6 more)

### Community 30 - "compute_margin_leverage_metrics"
Cohesion: 0.22
Nodes (8): compute_margin_leverage_metrics(), DataFrame, Systemic Leverage & Margin Debt Dynamics Module. ===============================, Compute FINRA Margin Debt YoY growth, velocity, leverage gap, and exhaustion ris, Systemic Margin Leverage & Credit Exhaustion Indicator Module. =================, test_compute_margin_leverage_metrics(), End-to-end integration test of MacroMahalanobisDetector on market dataset., test_full_pipeline_polars_integration()

### Community 31 - "test_no_synthetic_gaussian_bumps_in_data_code"
Cohesion: 0.17
Nodes (12): parse_authentic_vxo_series(), DataFrame, Path, ETL Pipeline for CBOE VXO volatility index., Stage authentic VXO dataset to parquet., Get daily VXO series reindexed to requested business dates., Parse authentic CBOE VXO daily history spanning 1976 to present.      Splicing H, VxoETL (+4 more)

### Community 32 - "compute_technical_indicators"
Cohesion: 0.20
Nodes (7): Technical Indicators & Momentum Oscillators Module. ============================, compute_technical_indicators(), DataFrame, Technical Indicators & Momentum Oscillators Module. ============================, Append technical momentum, trend, and volatility indicators to the input Polars, Fetch and process full dataset pipeline for selected date horizon., test_compute_technical_indicators()

### Community 33 - "test_splicing_continuity.py"
Cohesion: 0.22
Nodes (8): multi_decade_df(), Unit tests for Continuous Backward Return Compounding Splicing (Zero Cliffs)., Asserts single-day return at 1993-01-22 seam is bounded within normal daily dist, Asserts 1998-12-16 seam discontinuity is < 3%, completely eliminating the legacy, Asserts 1990 VIX seam matches CBOE ^VXO within continuous market tolerance., test_spy_backward_compounding_no_cliff(), test_vxo_vix_seam_continuity(), test_xlk_backward_compounding_no_cliff()

### Community 34 - "._append_real_macro_indicators"
Cohesion: 0.38
Nodes (4): DataFrame, Construct seamless asset time series with continuous backward return compounding, Merge authentic point-in-time macroeconomic series (Shiller CAPE, FRED GDP, FINR, Fetch historical price and macroeconomic datasets for SPY, sectors, and volatili

### Community 35 - "compute_macro_valuations"
Cohesion: 0.32
Nodes (6): Quantitative Feature Engineering & Mathematical Signal Processing Subpackage. ==, compute_macro_valuations(), DataFrame, Macroeconomic Valuation & Long-Horizon Equilibrium Module. =====================, Compute Shiller CAPE, Payout-Adjusted CAPE (P-CAPE), and Buffett Indicator metri, test_compute_macro_valuations()

### Community 36 - "System Architecture and Operational Rules for Agents"
Cohesion: 0.40
Nodes (4): 1. Core Econometric & Statistical Rules, 2. Directory Layout & Key Modules, 3. Execution & Verification Rules, System Architecture and Operational Rules for Agents

### Community 37 - "get_current_date"
Cohesion: 0.43
Nodes (7): get_current_date(), get_dynamic_50yr_date_range(), get_dynamic_horizon_metadata(), Any, date, Return current execution date, or parse override date string/object., Compute rolling 50-year date range from current execution date.         Safely h

### Community 38 - "apply_postprocessing"
Cohesion: 0.28
Nodes (8): precompile_wasm_parquet_datasets(), Provenance Data Staging & WebAssembly Binary Pre-Compilation Pipeline. =========, Convert existing staged Parquet datasets into clean JSON tables for WebAssembly, Pre-compile production Parquet and lightweight clean JSON datasets for     clien, stage_all(), sync_parquet_to_json(), Verify that 21-column JSON datasets are created within strict payload size budge, test_json_datasets_staging()

### Community 39 - "test_ingestor.py"
Cohesion: 0.40
Nodes (5): lttb_downsample(), normalize_tda_indicator(), _prepare_trace(), ndarray, Decimate time series via pure NumPy LTTB, or take compact 2-point proxy during W

### Community 41 - "mock_indicators_df"
Cohesion: 0.18
Nodes (15): build_mahalanobis_chart(), Build Plotly figure for Macro Mahalanobis Distance Dashboard (Method 1)., build_mahalanobis_fig(), Build Plotly figure for Macro Mahalanobis Distance Dashboard (matching NiceGUI 1, mock_indicators_df(), Unit tests for Macro Mahalanobis Distance Regime-Switching Bubble Detector (Meth, Verify that Tab 6 contains all 8 traces with right-flushed legend in both NiceGU, Verify that all 8 traces plotted on Tab 6 have 0 NaNs and fall cleanly within [0 (+7 more)

## Knowledge Gaps
- **67 isolated node(s):** `market-bubble-detector`, `PRECACHE_ASSETS`, `1. Core Econometric & Statistical Rules`, `2. Directory Layout & Key Modules`, `3. Execution & Verification Rules` (+62 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **7 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `MacroMahalanobisDetector` connect `AGVI System Pipeline and Dashboard` to `compute_technical_indicators`, `Econometric Bubble Detection Models`, `Valuation and Feature Engineering`, `apply_postprocessing`, `test_ui_theme.py`, `mock_indicators_df`, `panel_dashboard.py`, `compute_margin_leverage_metrics`?**
  _High betweenness centrality (0.091) - this node is a cross-community bridge._
- **Why does `DashboardState` connect `panel_dashboard.py` to `compute_technical_indicators`, `AGVI System Pipeline and Dashboard`, `Graphify Settings and Rules`, `FINRA Margin Debt Metrics`, `test_ui_theme.py`, `mock_indicators_df`, `ingestor.py`, `generate_wasm_dataset`?**
  _High betweenness centrality (0.064) - this node is a cross-community bridge._
- **Why does `DataIngestor` connect `generate_wasm_dataset` to `compute_technical_indicators`, `test_splicing_continuity.py`, `._append_real_macro_indicators`, `Econometric Bubble Detection Models`, `Graphify Settings and Rules`, `Valuation and Feature Engineering`, `apply_postprocessing`, `test_ui_theme.py`, `__init__.py`, `mock_indicators_df`, `panel_dashboard.py`, `__init__.py`, `compute_margin_leverage_metrics`?**
  _High betweenness centrality (0.063) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `DashboardState` (e.g. with `PortfolioBacktestEngine` and `DataIngestor`) actually correct?**
  _`DashboardState` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `DataIngestor` (e.g. with `DataFetchError` and `ValidationError`) actually correct?**
  _`DataIngestor` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `StructuralBreakPredictor` (e.g. with `ModelTrainingError` and `DashboardState`) actually correct?**
  _`StructuralBreakPredictor` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `market-bubble-detector`, `PRECACHE_ASSETS`, `1. Core Econometric & Statistical Rules` to the rest of the system?**
  _67 weakly-connected nodes found - possible documentation gaps or missing edges._