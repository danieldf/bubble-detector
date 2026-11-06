# Graph Report - Merrill  (2026-11-05)

## Corpus Check
- 85 files · ~119,718 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 19 file(s) not represented in the graph (top: .parquet 9, .csv 6, (none) 2)

## Summary
- 917 nodes · 2197 edges · 48 communities (44 shown, 4 thin omitted)
- Extraction: 93% EXTRACTED · 7% INFERRED · 0% AMBIGUOUS · INFERRED: 164 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `226e4ef1`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Market Bubble Structural Analysis Report
- MacroMahalanobisDetector
- deploy.yml
- Implied Volatility Metrics Table (July 2026)
- 📉 Multidimensional Market Bubble Detector & Structural Break System
- build_econometric_fig
- StructuralBreakPredictor
- market-bubble-detector
- PortfolioBacktestEngine
- test_bsadf_rigor.py
- config.py
- generate_deck.py
- features/__init__.py
- test_mahalanobis.py
- 📊 7 Interactive Dashboard Modules
- DashboardState
- test_ui_ux_wasm_optimizations.py
- stage_provenance.py
- postprocess_wasm.py
- dashboard.py
- ui_theme.py
- polars
- FredETL
- test_no_gaussian_bumps.py
- FinraETL
- compute_lppls_confidence_indicator
- composite_summary.py
- test_tda_wavelet_rigor.py
- precompile_wasm_parquet_datasets
- 📋 Changelog
- 🔬 Mathematical Formulations
- build_tech_exuberance_fig
- features/__init__.py
- DataIngestor
- System Architecture and Operational Rules for Agents
- panel_dashboard.py
- .load_data
- get_current_date
- sw.js
- [v2.1.0] - 2026-09-02
- 💻 Local Setup & Execution Guide
- test_wasm_pyodide_sandbox.py
- [v3.2.0] - 2026-11-03
- build_mahalanobis_fig
- test_full_indicator_parity.py
- generate_wasm_dataset

## God Nodes (most connected - your core abstractions)
1. `DashboardState` - 46 edges
2. `MacroMahalanobisDetector` - 36 edges
3. `DataIngestor` - 31 edges
4. `generate_wasm_dataset()` - 31 edges
5. `StructuralBreakPredictor` - 30 edges
6. `compute_tda_wavelet_complexity()` - 27 edges
7. `compute_gsadf_gpt_decomposition()` - 24 edges
8. `test_all_7_tabs_plot_trace_parity()` - 24 edges
9. `precompile_wasm_parquet_datasets()` - 22 edges
10. `compute_margin_leverage_metrics()` - 21 edges

## Surprising Connections (you probably didn't know these)
- `3. Data Ingestion & Storage (`ingestor.py`):` --references--> `DataIngestor`  [INFERRED]
  ImplementationOverview_DDFv100.md → bubble_detector/data/ingestor.py
- `Fixed` --references--> `DataIngestor`  [INFERRED]
  README.md → bubble_detector/data/ingestor.py
- `Added` --references--> `compute_exuberance_spans()`  [INFERRED]
  CHANGELOG.md → bubble_detector/features/tech_exuberance.py
- `Added` --references--> `sync_wasm_build_directories()`  [INFERRED]
  README.md → bubble_detector/ui/postprocess_wasm.py
- `Added` --references--> `test_tda_normalization_tabs_5_and_6()`  [INFERRED]
  README.md → tests/test_mahalanobis.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **AGVI Indicator and Feature Engineering Pipeline** — marketbubble_ddfv100_shiller_cape_ratio, marketbubble_ddfv100_payout_adjusted_cape, marketbubble_ddfv100_buffett_indicator, marketbubble_ddfv100_gsadf_psy_procedure [EXTRACTED 1.00]
- **Econometric and Mathematical Bubble Detection Framework** — marketbubble_ddfv100_gsadf_psy_procedure, marketbubble_ddfv100_tda_wavelet, marketbubble_ddfv100_lppls_model [EXTRACTED 1.00]
- **Implied Volatility Term Structure Components** — impliedvolatilitymetric_vix1d, impliedvolatilitymetric_vix_spot, impliedvolatilitymetric_vix3m, impliedvolatilitymetric_vix1y [EXTRACTED 1.00]
- **FINRA Margin Debt Metrics** — finra_margin_debt_tracker, finra_may_2026_nominal_value, finra_may_2026_mom_change, finra_may_2026_yoy_change [INFERRED 0.85]

## Communities (48 total, 4 thin omitted)

### Community 0 - "Market Bubble Structural Analysis Report"
Cohesion: 0.08
Nodes (35): NiceGUI Layout & Plotly Dashboard, Data Ingestion (DataIngestor), AGVI Implementation Plan Document, Feature Engineering Pipeline, XGBoost Model Training & Walk-Forward CV, AGVI Technical Specification Document, NiceGUI Dashboard UI, Polars DataFrame Integration (+27 more)

### Community 1 - "MacroMahalanobisDetector"
Cohesion: 0.08
Nodes (12): MacroMahalanobisDetector, test_drawdown_probability_not_in_covariance(), test_p_cape_elimination(), test_anomaly_driver_attribution(), test_dynamic_exposure_bounds_and_monotonicity(), test_mahalanobis_distance_non_negative(), test_mahalanobis_no_early_rank_singularity(), test_regime_probability_bounds() (+4 more)

### Community 2 - "deploy.yml"
Cohesion: 0.07
Nodes (30): runs-on, steps, concurrency, cancel-in-progress, group, environment, needs, runs-on (+22 more)

### Community 3 - "Implied Volatility Metrics Table (July 2026)"
Cohesion: 0.60
Nodes (6): Implied Volatility Metrics Table (July 2026), Implied Volatility Term Structure (Upward Sloping), VIX1D (8.73 - 11.61): Extreme near-term calm, VIX1Y (~23.00): Elevated long-term risk premium, VIX3M (~19.00): Anticipation of future turbulence, VIX Spot (15.57 - 17.16): Low baseline fear

### Community 4 - "📉 Multidimensional Market Bubble Detector & Structural Break System"
Cohesion: 0.25
Nodes (7): Benchmark Comparison (50-Year Multi-Decade Horizon), 📅 Dynamic 50-Year Multi-Horizon Date Engine, 🎯 Falsifiable Historical Peak Validation Event Study, 📈 Institutional Cost-Inclusive Portfolio Backtest, 📜 License, 🌟 Live Interactive WebAssembly Dashboard, 📉 Multidimensional Market Bubble Detector & Structural Break System

### Community 5 - "build_econometric_fig"
Cohesion: 0.15
Nodes (13): build_composite_summary_fig(), build_econometric_fig(), build_leverage_fig(), build_macro_valuation_fig(), _build_packaging_proxy_fig(), build_sentiment_vol_fig(), generate_explanatory_markdown(), get_cached_or_build_fig() (+5 more)

### Community 6 - "StructuralBreakPredictor"
Cohesion: 0.05
Nodes (20): BubbleDetectorError, DataFetchError, IndicatorComputationError, ModelTrainingError, ValidationError, StructuralBreakPredictor, 10. Institutional Code Commentary, Packaging & Agent Navigation:, 1. System, Configuration & Date Horizons (`config.py` & `date_horizons.py`): (+12 more)

### Community 8 - "PortfolioBacktestEngine"
Cohesion: 0.12
Nodes (4): BacktestResult, PortfolioBacktestEngine, test_backtest_fee_deduction(), test_exposure_rule_vs_naive_cape()

### Community 9 - "test_bsadf_rigor.py"
Cohesion: 0.11
Nodes (11): calculate_adf_stat(), compute_gsadf_gpt_decomposition(), compute_wild_bootstrap_critical_values(), test_adf_lag_selection_k0_vs_k1(), test_adf_stat_explosive_vs_stationary(), test_recursive_backward_supremum_grid(), test_wild_bootstrap_critical_value_bounds(), test_compute_gsadf_gpt_decomposition() (+3 more)

### Community 11 - "config.py"
Cohesion: 0.14
Nodes (4): get_finra_margin_debt(), get_fred_data(), get_shiller_data(), get_vxo_data()

### Community 12 - "generate_deck.py"
Cohesion: 0.20
Nodes (3): create_presentation(), add_card(), add_metric_badge()

### Community 13 - "features/__init__.py"
Cohesion: 0.23
Nodes (4): compute_exuberance_spans(), compute_tech_exuberance_metrics(), test_compute_exuberance_spans(), test_dual_conditions_logic()

### Community 14 - "test_mahalanobis.py"
Cohesion: 0.27
Nodes (4): build_mahalanobis_chart(), test_tab6_all_traces_finite_and_bounded(), test_tab6_figure_traces_and_right_flushed_legend(), test_tda_normalization_tabs_5_and_6()

### Community 16 - "📊 7 Interactive Dashboard Modules"
Cohesion: 0.22
Nodes (9): 1. Macro Valuation Anchors, 2. Systemic Liquidity & Leverage, 3. Econometric Explosive Bubble Diagnostics, 4. Options Sentiment & Behavioral Tracking, 5. Sector Vulnerability & Topological Dynamics, 6. Signed Macro Mahalanobis Distance & Dynamic Equity Exposure, 📊 7 Interactive Dashboard Modules, 7. Tech Exuberance Score: Macro Decoupling vs Statistical Singularity (+1 more)

### Community 17 - "DashboardState"
Cohesion: 0.14
Nodes (14): build_composite_summary_chart(), build_composite_validation_chart(), build_econometric_chart(), build_leverage_chart(), build_macro_valuation_chart(), build_sector_health_chart(), build_sentiment_vol_chart(), build_tech_exuberance_chart() (+6 more)

### Community 18 - "test_ui_ux_wasm_optimizations.py"
Cohesion: 0.09
Nodes (11): calculate_adf_stat(), lttb_downsample(), takens_embedding(), 4. Quantitative Indicator Modules (`features/` & `features/utils.py`):, test_keyboard_operability_and_aria_landmarks(), test_lttb_downsample_edge_cases(), test_lttb_downsample_extrema_retention(), test_lttb_downsample_monotonic_dates() (+3 more)

### Community 19 - "stage_provenance.py"
Cohesion: 0.15
Nodes (6): parse_authentic_vxo_series(), VxoETL, stage_all(), sync_parquet_to_json(), test_vxo_authenticity_and_black_monday(), test_authentic_cboe_vxo_black_monday()

### Community 20 - "postprocess_wasm.py"
Cohesion: 0.07
Nodes (19): postprocess_wasm_content(), clean_bokeh_templates(), postprocess_wasm_html(), sync_wasm_build_directories(), [3.0.0] - 2026-09-03, [3.1.0] - 2026-10-05, [3.2.0] - 2026-11-03, [3.3.0] - 2026-11-05 (+11 more)

### Community 21 - "dashboard.py"
Cohesion: 0.14
Nodes (8): create_cta_banner(), create_ios_card(), create_app(), on_horizon_change(), refresh_dashboard(), run_diagnostics(), render_executive_summary_card(), render_horizon_explanatory_note()

### Community 22 - "ui_theme.py"
Cohesion: 0.08
Nodes (21): toggle_theme(), calculate_contrast_ratio(), get_plotly_template(), get_theme_css(), is_wcag_aa_compliant(), parse_hex_color(), relative_luminance(), 2. UI & Accessibility Engine (`ui_theme.py`): (+13 more)

### Community 23 - "polars"
Cohesion: 0.11
Nodes (7): compute_technical_indicators(), market_simulation_df(), test_five_summary_indicators_bounds_and_crash_separation_20yr(), test_orthogonal_basis_13_spectral_entropy_and_vif_20yr(), test_compute_technical_indicators(), mock_indicators_df(), test_technical_alias_parity()

### Community 24 - "FredETL"
Cohesion: 0.12
Nodes (7): FredETL, parse_fred_macro_series(), test_fred_publication_lags(), test_central_bank_balance_sheet_splicing_continuity(), test_global_liquidity_derived_metrics(), test_global_liquidity_schema_and_publication_lags(), test_authentic_fred_gdp_and_housing()

### Community 25 - "test_no_gaussian_bumps.py"
Cohesion: 0.20
Nodes (4): parse_shiller_excel(), ShillerETL, test_shiller_provenance_schema_and_bounds(), test_authentic_shiller_provenance_workbook()

### Community 26 - "FinraETL"
Cohesion: 0.20
Nodes (4): FinraETL, parse_finra_margin_debt_series(), test_finra_margin_publication_lag(), test_authentic_finra_margin_debt()

### Community 27 - "compute_lppls_confidence_indicator"
Cohesion: 0.13
Nodes (6): calibrate_lppls_filimonov(), compute_lppls_confidence_indicator(), test_lppls_confidence_indicator_pipeline(), test_lppls_historical_bubble_detection(), test_lppls_parameter_recovery_synthetic(), test_lppls_sornette_filtering_bounds()

### Community 28 - "composite_summary.py"
Cohesion: 0.10
Nodes (8): causal_ffill_clean(), causal_gram_schmidt(), causal_stationary_unit_variance(), CompositeSummaryEngine, compute_composite_validation_metrics(), compute_orthogonal_basis_and_summaries_numpy(), norm_cdf_numpy(), test_strict_causal_filtration_zero_lookahead()

### Community 29 - "test_tda_wavelet_rigor.py"
Cohesion: 0.12
Nodes (10): _compute_morlet_wavelet_energy_and_entropy(), _compute_persistence_landscape_and_entropy(), _compute_rips_persistence_diagrams(), compute_tda_wavelet_complexity(), _takens_embedding(), test_bubenik_l2_norm_and_persistence_entropy(), test_morlet_wavelet_scaleogram_and_spectral_entropy(), test_persistence_entropy_herding_collapse() (+2 more)

### Community 30 - "precompile_wasm_parquet_datasets"
Cohesion: 0.13
Nodes (6): compute_macro_valuations(), precompile_wasm_parquet_datasets(), ensure_synchronized_wasm_datasets(), test_compute_macro_valuations(), test_full_pipeline_polars_integration(), processed_df()

### Community 31 - "📋 Changelog"
Cohesion: 0.15
Nodes (13): Added, Added, Added, Added, Added, Added, 📋 Changelog, [v1.0.0] - 2026-08-05 (+5 more)

### Community 32 - "🔬 Mathematical Formulations"
Cohesion: 0.25
Nodes (8): 1. Continuous Backward Compounding (Cliff Eradication), 2. Signed Macro Mahalanobis Distance & Directional Projection, 3. Dynamic Portfolio Equity Sizing ($w_{\text{equity}}$), 4. Canonical PSY Recursive Right-Tailed Unit Root Testing (GSADF / BSADF), 5. Topological Data Analysis (TDA) & Wavelet Spectral Entropy, 6. Log-Periodic Power Law Singularity (LPPLS) Subordination Model, 7. Global Liquidity Index & Dual-Condition Conjoint Exuberance, 🔬 Mathematical Formulations

### Community 33 - "build_tech_exuberance_fig"
Cohesion: 0.15
Nodes (8): build_tech_exuberance_fig(), fetch_dataset(), test_pane_tech_exuberance_in_dashboard_tabs(), test_precompile_wasm_parquet_datasets(), test_tech_exuberance_columns_in_core_wasm(), test_tech_exuberance_fig_structure_desktop(), test_tech_exuberance_fig_structure_mobile(), test_tech_exuberance_fig_structure_option_3()

### Community 34 - "features/__init__.py"
Cohesion: 0.12
Nodes (6): compute_margin_leverage_metrics(), compute_options_volatility_metrics(), test_compute_margin_leverage_metrics(), test_compute_options_volatility_metrics(), test_margin_leverage_alias_parity(), test_options_volatility_alias_parity()

### Community 35 - "DataIngestor"
Cohesion: 0.06
Nodes (17): get_current_date(), get_dynamic_50yr_date_range(), get_dynamic_horizon_metadata(), DataIngestor, ingestor(), test_dynamic_50yr_date_generator(), test_option_1_50yr_data_ingestion(), test_option_2_modern_data_ingestion() (+9 more)

### Community 36 - "System Architecture and Operational Rules for Agents"
Cohesion: 0.40
Nodes (4): 1. Core Econometric & Statistical Rules, 2. Directory Layout & Key Modules, 3. Execution & Verification Rules, System Architecture and Operational Rules for Agents

### Community 37 - "panel_dashboard.py"
Cohesion: 0.18
Nodes (5): build_band_polygon(), build_band_polygon(), build_composite_validation_fig(), compute_composite_validation_metrics(), precompile_wasm_parquet_datasets()

### Community 38 - ".load_data"
Cohesion: 0.13
Nodes (5): compute_validation_summary_statistics(), generate_historical_validation_table(), test_tab8_dual_ui_parity_across_all_horizons(), test_tab8_validation_6_color_bands_and_wealth_parity(), test_dashboard_state_horizon_switching()

### Community 39 - "get_current_date"
Cohesion: 0.43
Nodes (3): get_current_date(), get_dynamic_50yr_date_range(), get_dynamic_horizon_metadata()

### Community 41 - "[v2.1.0] - 2026-09-02"
Cohesion: 0.67
Nodes (3): Added, Fixed, [v2.1.0] - 2026-09-02

### Community 42 - "💻 Local Setup & Execution Guide"
Cohesion: 0.29
Nodes (7): 1. Prerequisites & Virtual Environment, 2. Run the High-Performance NiceGUI Application, 3. Run the Local HoloViz Panel Dashboard, 4. Build and Run Client-Side WebAssembly (Pyodide), 5. Run the Automated Test Suite, 6. Synchronize Repository Knowledge Graph, 💻 Local Setup & Execution Guide

### Community 43 - "test_wasm_pyodide_sandbox.py"
Cohesion: 0.08
Nodes (8): test_date_horizon_selector_robust_against_year_shift(), test_dist_index_html_on_disk(), test_json_datasets_staging(), test_template_and_cards_reconstruction(), test_wasm_full_script_pure_numpy_fallback_execution(), test_wasm_full_script_pyodide_execution(), test_wasm_pyodide_json_memfs_loading(), test_wasm_pyodide_pure_numpy_fallback()

### Community 44 - "[v3.2.0] - 2026-11-03"
Cohesion: 0.67
Nodes (3): Added, Changed, [v3.2.0] - 2026-11-03

### Community 46 - "build_mahalanobis_fig"
Cohesion: 0.24
Nodes (6): normalize_tda_indicator(), build_mahalanobis_fig(), build_sector_health_fig(), lttb_downsample(), normalize_tda_indicator(), _prepare_trace()

### Community 48 - "test_full_indicator_parity.py"
Cohesion: 0.28
Nodes (3): test_all_7_tabs_plot_trace_parity(), test_all_indicators_numerical_parity(), test_wasm_fallback_numerical_parity()

### Community 49 - "generate_wasm_dataset"
Cohesion: 0.20
Nodes (4): generate_wasm_dataset(), test_compute_tda_wavelet_complexity(), test_tda_wasm_parity(), test_wasm_loads_exact_parquet_dataset()

## Knowledge Gaps
- **16 isolated node(s):** `market-bubble-detector`, `Polars DataFrame Integration`, `Margin Debt Growth Velocity`, `May 2026 Month-over-Month Change (+8.53%)`, `May 2026 Margin Debt Nominal Value ($1.416T)` (+11 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 449 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `📋 Changelog` connect `📋 Changelog` to `[v2.1.0] - 2026-09-02`, `[v3.2.0] - 2026-11-03`, `📉 Multidimensional Market Bubble Detector & Structural Break System`?**
  _High betweenness centrality (0.079) - this node is a cross-community bridge._
- **Are the 10 inferred relationships involving `DashboardState` (e.g. with `PortfolioBacktestEngine` and `DataIngestor`) actually correct?**
  _`DashboardState` has 10 INFERRED edges - model-reasoned connections that need verification._
- **What connects `market-bubble-detector`, `Polars DataFrame Integration`, `Margin Debt Growth Velocity` to the rest of the system?**
  _16 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Market Bubble Structural Analysis Report` be split into smaller, more focused modules?**
  _Cohesion score 0.07563025210084033 - nodes in this community are weakly interconnected._
- **Why does `DataIngestor` connect `DataIngestor` to `panel_dashboard.py`, `.load_data`, `StructuralBreakPredictor`, `[v2.1.0] - 2026-09-02`, `test_bsadf_rigor.py`, `config.py`, `test_mahalanobis.py`, `DashboardState`, `generate_wasm_dataset`, `stage_provenance.py`, `dashboard.py`, `composite_summary.py`, `precompile_wasm_parquet_datasets`, `📋 Changelog`?**
  _High betweenness centrality (0.068) - this node is a cross-community bridge._
- **Should `MacroMahalanobisDetector` be split into smaller, more focused modules?**
  _Cohesion score 0.07878787878787878 - nodes in this community are weakly interconnected._
- **Why does `📉 Multidimensional Market Bubble Detector & Structural Break System` connect `📉 Multidimensional Market Bubble Detector & Structural Break System` to `📊 7 Interactive Dashboard Modules`, `💻 Local Setup & Execution Guide`, `🔬 Mathematical Formulations`, `📋 Changelog`?**
  _High betweenness centrality (0.060) - this node is a cross-community bridge._