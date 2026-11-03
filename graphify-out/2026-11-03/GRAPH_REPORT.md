# Graph Report - Merrill  (2026-11-03)

## Corpus Check
- 83 files · ~100,328 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 19 file(s) not represented in the graph (top: .parquet 9, .csv 6, (none) 2)

## Summary
- 852 nodes · 1995 edges · 45 communities (40 shown, 5 thin omitted)
- Extraction: 93% EXTRACTED · 7% INFERRED · 0% AMBIGUOUS · INFERRED: 145 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `e38e8a1c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Market Bubble Structural Analysis Report
- test_mahalanobis.py
- deploy.yml
- Implied Volatility Metrics Table (July 2026)
- test_date_horizons.py
- build_econometric_fig
- StructuralBreakPredictor
- market-bubble-detector
- PortfolioBacktestEngine
- test_bsadf_rigor.py
- ingestor.py
- generate_deck.py
- features/__init__.py
- Overview of Completed Implementation: Multidimensional Market Bubble Detector
- 📉 Multidimensional Market Bubble Detector & Structural Break System
- test_mahalanobis.py
- test_ui_ux_wasm_optimizations.py
- stage_provenance.py
- postprocess_wasm_content
- dashboard.py
- calculate_contrast_ratio
- generate_wasm_dataset
- FredETL
- test_all_indicators_numerical_parity
- numpy
- compute_lppls_confidence_indicator
- DashboardState
- test_tda_wavelet_rigor.py
- compute_margin_leverage_metrics
- compute_gsadf_gpt_decomposition
- calibrate_lppls_filimonov
- build_tech_exuberance_fig
- compute_technical_indicators
- DataIngestor
- System Architecture and Operational Rules for Agents
- panel_dashboard.py
- .load_data
- test_splicing_continuity.py
- sw.js
- [3.1.0] - 2026-10-05
- features/__init__.py
- test_wasm_pyodide_sandbox.py
- test_mahalanobis.py

## God Nodes (most connected - your core abstractions)
1. `DashboardState` - 40 edges
2. `MacroMahalanobisDetector` - 35 edges
3. `DataIngestor` - 31 edges
4. `StructuralBreakPredictor` - 30 edges
5. `generate_wasm_dataset()` - 28 edges
6. `compute_tda_wavelet_complexity()` - 27 edges
7. `compute_gsadf_gpt_decomposition()` - 24 edges
8. `compute_margin_leverage_metrics()` - 21 edges
9. `build_tech_exuberance_fig()` - 21 edges
10. `compute_options_volatility_metrics()` - 20 edges

## Surprising Connections (you probably didn't know these)
- `3. Data Ingestion & Storage (`ingestor.py`):` --references--> `DataIngestor`  [INFERRED]
  ImplementationOverview_DDFv100.md → bubble_detector/data/ingestor.py
- `Added` --references--> `compute_exuberance_spans()`  [INFERRED]
  CHANGELOG.md → bubble_detector/features/tech_exuberance.py
- `4. Quantitative Indicator Modules (`features/` & `features/utils.py`):` --references--> `takens_embedding()`  [INFERRED]
  ImplementationOverview_DDFv100.md → bubble_detector/features/utils.py
- `5. Machine Learning Model (`structural_breaks.py`):` --references--> `StructuralBreakPredictor`  [INFERRED]
  ImplementationOverview_DDFv100.md → bubble_detector/models/structural_breaks.py
- `Added` --references--> `test_tda_normalization_tabs_5_and_6()`  [INFERRED]
  README.md → tests/test_mahalanobis.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **AGVI Indicator and Feature Engineering Pipeline** — marketbubble_ddfv100_shiller_cape_ratio, marketbubble_ddfv100_payout_adjusted_cape, marketbubble_ddfv100_buffett_indicator, marketbubble_ddfv100_gsadf_psy_procedure [EXTRACTED 1.00]
- **Econometric and Mathematical Bubble Detection Framework** — marketbubble_ddfv100_gsadf_psy_procedure, marketbubble_ddfv100_tda_wavelet, marketbubble_ddfv100_lppls_model [EXTRACTED 1.00]
- **Implied Volatility Term Structure Components** — impliedvolatilitymetric_vix1d, impliedvolatilitymetric_vix_spot, impliedvolatilitymetric_vix3m, impliedvolatilitymetric_vix1y [EXTRACTED 1.00]
- **FINRA Margin Debt Metrics** — finra_margin_debt_tracker, finra_may_2026_nominal_value, finra_may_2026_mom_change, finra_may_2026_yoy_change [INFERRED 0.85]

## Communities (45 total, 5 thin omitted)

### Community 0 - "Market Bubble Structural Analysis Report"
Cohesion: 0.07
Nodes (35): NiceGUI Layout & Plotly Dashboard, Data Ingestion (DataIngestor), AGVI Implementation Plan Document, Feature Engineering Pipeline, XGBoost Model Training & Walk-Forward CV, AGVI Technical Specification Document, NiceGUI Dashboard UI, Polars DataFrame Integration (+27 more)

### Community 1 - "test_mahalanobis.py"
Cohesion: 0.08
Nodes (12): MacroMahalanobisDetector, test_drawdown_probability_not_in_covariance(), test_p_cape_elimination(), test_anomaly_driver_attribution(), test_dynamic_exposure_bounds_and_monotonicity(), test_mahalanobis_distance_non_negative(), test_mahalanobis_no_early_rank_singularity(), test_regime_probability_bounds() (+4 more)

### Community 2 - "deploy.yml"
Cohesion: 0.07
Nodes (30): runs-on, steps, concurrency, cancel-in-progress, group, environment, needs, runs-on (+22 more)

### Community 3 - "Implied Volatility Metrics Table (July 2026)"
Cohesion: 0.60
Nodes (6): Implied Volatility Metrics Table (July 2026), Implied Volatility Term Structure (Upward Sloping), VIX1D (8.73 - 11.61): Extreme near-term calm, VIX1Y (~23.00): Elevated long-term risk premium, VIX3M (~19.00): Anticipation of future turbulence, VIX Spot (15.57 - 17.16): Low baseline fear

### Community 4 - "test_date_horizons.py"
Cohesion: 0.18
Nodes (4): get_current_date(), get_dynamic_50yr_date_range(), get_dynamic_horizon_metadata(), test_dynamic_50yr_date_generator()

### Community 5 - "build_econometric_fig"
Cohesion: 0.17
Nodes (14): build_econometric_fig(), build_leverage_fig(), build_macro_valuation_fig(), build_mahalanobis_fig(), _build_packaging_proxy_fig(), build_sector_health_fig(), build_sentiment_vol_fig(), generate_explanatory_markdown() (+6 more)

### Community 6 - "StructuralBreakPredictor"
Cohesion: 0.08
Nodes (6): ModelTrainingError, StructuralBreakPredictor, test_structural_break_predictor_walk_forward(), test_structural_breaks_embargo_no_lookahead(), test_reliability_diagram_monotonicity(), test_walk_forward_brier_score()

### Community 8 - "PortfolioBacktestEngine"
Cohesion: 0.12
Nodes (5): BacktestResult, PortfolioBacktestEngine, market_simulation_df(), test_backtest_fee_deduction(), test_exposure_rule_vs_naive_cape()

### Community 9 - "test_bsadf_rigor.py"
Cohesion: 0.19
Nodes (5): calculate_adf_stat(), compute_wild_bootstrap_critical_values(), test_adf_lag_selection_k0_vs_k1(), test_adf_stat_explosive_vs_stationary(), test_wild_bootstrap_critical_value_bounds()

### Community 11 - "ingestor.py"
Cohesion: 0.14
Nodes (3): get_finra_margin_debt(), get_shiller_data(), get_vxo_data()

### Community 12 - "generate_deck.py"
Cohesion: 0.20
Nodes (3): create_presentation(), add_card(), add_metric_badge()

### Community 13 - "features/__init__.py"
Cohesion: 0.22
Nodes (4): compute_exuberance_spans(), compute_tech_exuberance_metrics(), test_compute_exuberance_spans(), test_dual_conditions_logic()

### Community 14 - "Overview of Completed Implementation: Multidimensional Market Bubble Detector"
Cohesion: 0.08
Nodes (22): BubbleDetectorError, DataFetchError, IndicatorComputationError, ValidationError, 10. Institutional Code Commentary, Packaging & Agent Navigation:, 1. System, Configuration & Date Horizons (`config.py` & `date_horizons.py`):, 3. Data Ingestion & Storage (`ingestor.py`):, 4. Quantitative Indicator Modules (`features/` & `features/utils.py`): (+14 more)

### Community 16 - "📉 Multidimensional Market Bubble Detector & Structural Break System"
Cohesion: 0.06
Nodes (30): 1. Continuous Backward Compounding (Cliff Eradication), 1. Macro Valuation Anchors, 1. Prerequisites & Virtual Environment, 2. Run the High-Performance NiceGUI Application, 2. Signed Macro Mahalanobis Distance & Directional Projection, 2. Systemic Liquidity & Leverage, 3. Dynamic Portfolio Equity Sizing ($w_{\text{equity}}$), 3. Econometric Explosive Bubble Diagnostics (+22 more)

### Community 17 - "test_mahalanobis.py"
Cohesion: 0.18
Nodes (9): build_econometric_chart(), build_leverage_chart(), build_macro_valuation_chart(), build_sector_health_chart(), build_sentiment_vol_chart(), build_tech_exuberance_chart(), get_right_flushed_legend(), _prepare_trace() (+1 more)

### Community 18 - "test_ui_ux_wasm_optimizations.py"
Cohesion: 0.17
Nodes (5): test_keyboard_operability_and_aria_landmarks(), test_responsive_legend_layout_logic(), test_service_worker_file_validity(), test_wasm_build_packaging_html_size(), test_wasm_dependency_version_locking_and_resilience_bridge()

### Community 19 - "stage_provenance.py"
Cohesion: 0.05
Nodes (17): FinraETL, parse_finra_margin_debt_series(), parse_shiller_excel(), ShillerETL, parse_authentic_vxo_series(), VxoETL, precompile_wasm_parquet_datasets(), stage_all() (+9 more)

### Community 20 - "postprocess_wasm_content"
Cohesion: 0.19
Nodes (5): postprocess_wasm_content(), clean_bokeh_templates(), postprocess_wasm_html(), sync_wasm_build_directories(), test_no_synthetic_gaussian_bumps_in_data_code()

### Community 21 - "dashboard.py"
Cohesion: 0.15
Nodes (9): create_cta_banner(), create_ios_card(), create_app(), on_horizon_change(), refresh_dashboard(), run_diagnostics(), toggle_theme(), render_executive_summary_card() (+1 more)

### Community 22 - "calculate_contrast_ratio"
Cohesion: 0.11
Nodes (13): calculate_contrast_ratio(), get_plotly_template(), get_theme_css(), is_wcag_aa_compliant(), parse_hex_color(), relative_luminance(), 2. UI & Accessibility Engine (`ui_theme.py`):, test_ui_theme_alias_parity() (+5 more)

### Community 23 - "generate_wasm_dataset"
Cohesion: 0.15
Nodes (9): compute_macro_valuations(), compute_options_volatility_metrics(), compute_tda_wavelet_complexity(), generate_wasm_dataset(), test_compute_macro_valuations(), test_compute_options_volatility_metrics(), test_compute_tda_wavelet_complexity(), test_tda_wasm_parity() (+1 more)

### Community 24 - "FredETL"
Cohesion: 0.11
Nodes (9): FredETL, get_fred_data(), parse_fred_macro_series(), test_fred_publication_lags(), test_central_bank_balance_sheet_splicing_continuity(), test_global_liquidity_derived_metrics(), test_global_liquidity_schema_and_publication_lags(), test_authentic_cboe_vxo_black_monday() (+1 more)

### Community 26 - "numpy"
Cohesion: 0.17
Nodes (6): lttb_downsample(), test_predict_drawdown_probability(), test_tda_wavelet_complexity_full_pipeline(), test_lttb_downsample_edge_cases(), test_lttb_downsample_extrema_retention(), test_lttb_downsample_monotonic_dates()

### Community 27 - "compute_lppls_confidence_indicator"
Cohesion: 0.13
Nodes (3): compute_lppls_confidence_indicator(), test_lppls_confidence_indicator_pipeline(), test_lppls_historical_bubble_detection()

### Community 28 - "DashboardState"
Cohesion: 0.19
Nodes (4): DashboardState, test_full_system_integration(), test_dashboard_state_theme_toggle(), test_wasm_loads_exact_parquet_dataset()

### Community 29 - "test_tda_wavelet_rigor.py"
Cohesion: 0.14
Nodes (8): _compute_morlet_wavelet_energy_and_entropy(), _compute_persistence_landscape_and_entropy(), _compute_rips_persistence_diagrams(), _takens_embedding(), test_bubenik_l2_norm_and_persistence_entropy(), test_morlet_wavelet_scaleogram_and_spectral_entropy(), test_persistence_entropy_herding_collapse(), test_takens_delay_embedding_shape()

### Community 30 - "compute_margin_leverage_metrics"
Cohesion: 0.15
Nodes (4): compute_margin_leverage_metrics(), test_compute_margin_leverage_metrics(), test_margin_leverage_alias_parity(), test_options_volatility_alias_parity()

### Community 31 - "compute_gsadf_gpt_decomposition"
Cohesion: 0.18
Nodes (5): compute_gsadf_gpt_decomposition(), test_recursive_backward_supremum_grid(), test_compute_gsadf_gpt_decomposition(), test_canonical_monthly_gsadf_dotcom_spike(), test_ripser_persistence_landscapes_causal()

### Community 32 - "calibrate_lppls_filimonov"
Cohesion: 0.22
Nodes (3): calibrate_lppls_filimonov(), test_lppls_parameter_recovery_synthetic(), test_lppls_sornette_filtering_bounds()

### Community 33 - "build_tech_exuberance_fig"
Cohesion: 0.17
Nodes (7): build_tech_exuberance_fig(), fetch_dataset(), test_pane_tech_exuberance_in_dashboard_tabs(), test_tech_exuberance_columns_in_core_wasm(), test_tech_exuberance_fig_structure_desktop(), test_tech_exuberance_fig_structure_mobile(), test_tech_exuberance_fig_structure_option_3()

### Community 34 - "compute_technical_indicators"
Cohesion: 0.25
Nodes (3): compute_technical_indicators(), test_compute_technical_indicators(), test_technical_alias_parity()

### Community 35 - "DataIngestor"
Cohesion: 0.06
Nodes (25): DataIngestor, Added, Added, Added, Added, Added, Added, 📋 Changelog (+17 more)

### Community 36 - "System Architecture and Operational Rules for Agents"
Cohesion: 0.40
Nodes (4): 1. Core Econometric & Statistical Rules, 2. Directory Layout & Key Modules, 3. Execution & Verification Rules, System Architecture and Operational Rules for Agents

### Community 37 - "panel_dashboard.py"
Cohesion: 0.15
Nodes (7): get_current_date(), get_dynamic_50yr_date_range(), get_dynamic_horizon_metadata(), lttb_downsample(), normalize_tda_indicator(), precompile_wasm_parquet_datasets(), _prepare_trace()

### Community 38 - ".load_data"
Cohesion: 0.18
Nodes (3): compute_validation_summary_statistics(), generate_historical_validation_table(), test_dashboard_state_horizon_switching()

### Community 39 - "test_splicing_continuity.py"
Cohesion: 0.25
Nodes (3): test_spy_backward_compounding_no_cliff(), test_vxo_vix_seam_continuity(), test_xlk_backward_compounding_no_cliff()

### Community 41 - "[3.1.0] - 2026-10-05"
Cohesion: 0.33
Nodes (5): [3.0.0] - 2026-09-03, [3.1.0] - 2026-10-05, Added, Changed, Changelog

### Community 42 - "features/__init__.py"
Cohesion: 0.22
Nodes (3): calculate_adf_stat(), normalize_tda_indicator(), takens_embedding()

### Community 43 - "test_wasm_pyodide_sandbox.py"
Cohesion: 0.07
Nodes (9): apply_postprocessing(), test_date_horizon_selector_robust_against_year_shift(), test_dist_index_html_on_disk(), test_dist_index_html_postprocessing_idempotence(), test_template_and_cards_reconstruction(), test_wasm_full_script_pure_numpy_fallback_execution(), test_wasm_full_script_pyodide_execution(), test_wasm_pyodide_json_memfs_loading() (+1 more)

### Community 47 - "test_mahalanobis.py"
Cohesion: 0.19
Nodes (5): build_mahalanobis_chart(), mock_indicators_df(), test_tab6_all_traces_finite_and_bounded(), test_tab6_figure_traces_and_right_flushed_legend(), test_tda_normalization_tabs_5_and_6()

## Knowledge Gaps
- **16 isolated node(s):** `market-bubble-detector`, `Polars DataFrame Integration`, `Margin Debt Growth Velocity`, `May 2026 Month-over-Month Change (+8.53%)`, `May 2026 Margin Debt Nominal Value ($1.416T)` (+11 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 418 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `📋 Changelog` connect `DataIngestor` to `📉 Multidimensional Market Bubble Detector & Structural Break System`?**
  _High betweenness centrality (0.076) - this node is a cross-community bridge._
- **Are the 7 inferred relationships involving `DashboardState` (e.g. with `PortfolioBacktestEngine` and `DataIngestor`) actually correct?**
  _`DashboardState` has 7 INFERRED edges - model-reasoned connections that need verification._
- **What connects `market-bubble-detector`, `Polars DataFrame Integration`, `Margin Debt Growth Velocity` to the rest of the system?**
  _16 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Market Bubble Structural Analysis Report` be split into smaller, more focused modules?**
  _Cohesion score 0.07394957983193277 - nodes in this community are weakly interconnected._
- **Why does `DataIngestor` connect `DataIngestor` to `test_date_horizons.py`, `panel_dashboard.py`, `StructuralBreakPredictor`, `.load_data`, `test_splicing_continuity.py`, `ingestor.py`, `Overview of Completed Implementation: Multidimensional Market Bubble Detector`, `test_mahalanobis.py`, `stage_provenance.py`, `dashboard.py`, `generate_wasm_dataset`, `numpy`, `DashboardState`?**
  _High betweenness centrality (0.072) - this node is a cross-community bridge._
- **Should `test_mahalanobis.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07878787878787878 - nodes in this community are weakly interconnected._
- **Why does `📉 Multidimensional Market Bubble Detector & Structural Break System` connect `📉 Multidimensional Market Bubble Detector & Structural Break System` to `DataIngestor`?**
  _High betweenness centrality (0.062) - this node is a cross-community bridge._