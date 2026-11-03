# Graph Report - Merrill  (2026-11-02)

## Corpus Check
- 82 files · ~99,334 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 18 file(s) not represented in the graph (top: .parquet 8, .csv 6, (none) 2)

## Summary
- 844 nodes · 1952 edges · 49 communities (39 shown, 10 thin omitted)
- Extraction: 93% EXTRACTED · 7% INFERRED · 0% AMBIGUOUS · INFERRED: 142 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `94aea8e3`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Market Bubble Structural Analysis Report
- test_mahalanobis.py
- deploy.yml
- Implied Volatility Metrics Table (July 2026)
- config.py
- test_mahalanobis.py
- StructuralBreakPredictor
- market-bubble-detector
- PortfolioBacktestEngine
- test_bsadf_rigor.py
- generate_deck.py
- features/__init__.py
- 📋 Changelog
- 📉 Multidimensional Market Bubble Detector & Structural Break System
- dashboard.py
- test_ui_ux_wasm_optimizations.py
- test_data_provenance.py
- postprocess_wasm_content
- .fetch_market_data
- calculate_contrast_ratio
- FinraETL
- FredETL
- test_splicing_continuity.py
- utils.py
- numpy
- stage_provenance.py
- test_tda_wavelet_rigor.py
- compute_technical_indicators
- test_no_gaussian_bumps.py
- technicals.py
- build_tech_exuberance_fig
- .load_data
- generate_wasm_dataset
- System Architecture and Operational Rules for Agents
- get_current_date
- datetime
- DataIngestor
- sw.js
- [3.1.0] - 2026-10-05
- build_tech_exuberance_fig
- test_wasm_pyodide_sandbox.py
- compute_options_volatility_metrics
- test_ingestor.py
- panel_dashboard.py
- test_psy_ripser_integrity.py
- pytest

## God Nodes (most connected - your core abstractions)
1. `DashboardState` - 39 edges
2. `MacroMahalanobisDetector` - 35 edges
3. `DataIngestor` - 31 edges
4. `StructuralBreakPredictor` - 30 edges
5. `generate_wasm_dataset()` - 28 edges
6. `compute_tda_wavelet_complexity()` - 27 edges
7. `compute_gsadf_gpt_decomposition()` - 24 edges
8. `compute_margin_leverage_metrics()` - 21 edges
9. `compute_options_volatility_metrics()` - 20 edges
10. `compute_technical_indicators()` - 20 edges

## Surprising Connections (you probably didn't know these)
- `3. Data Ingestion & Storage (`ingestor.py`):` --references--> `DataIngestor`  [INFERRED]
  ImplementationOverview_DDFv100.md → bubble_detector/data/ingestor.py
- `Fixed` --references--> `DataIngestor`  [INFERRED]
  README.md → bubble_detector/data/ingestor.py
- `Added` --references--> `compute_exuberance_spans()`  [INFERRED]
  CHANGELOG.md → bubble_detector/features/tech_exuberance.py
- `Added` --references--> `test_tda_normalization_tabs_5_and_6()`  [INFERRED]
  README.md → tests/test_mahalanobis.py
- `Added` --references--> `test_all_tabs_legends_right_flushed()`  [INFERRED]
  README.md → tests/test_mahalanobis.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **AGVI Indicator and Feature Engineering Pipeline** — marketbubble_ddfv100_shiller_cape_ratio, marketbubble_ddfv100_payout_adjusted_cape, marketbubble_ddfv100_buffett_indicator, marketbubble_ddfv100_gsadf_psy_procedure [EXTRACTED 1.00]
- **Econometric and Mathematical Bubble Detection Framework** — marketbubble_ddfv100_gsadf_psy_procedure, marketbubble_ddfv100_tda_wavelet, marketbubble_ddfv100_lppls_model [EXTRACTED 1.00]
- **Implied Volatility Term Structure Components** — impliedvolatilitymetric_vix1d, impliedvolatilitymetric_vix_spot, impliedvolatilitymetric_vix3m, impliedvolatilitymetric_vix1y [EXTRACTED 1.00]
- **FINRA Margin Debt Metrics** — finra_margin_debt_tracker, finra_may_2026_nominal_value, finra_may_2026_mom_change, finra_may_2026_yoy_change [INFERRED 0.85]

## Communities (49 total, 10 thin omitted)

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

### Community 4 - "config.py"
Cohesion: 0.14
Nodes (7): get_current_date(), get_dynamic_50yr_date_range(), get_dynamic_horizon_metadata(), get_finra_margin_debt(), get_shiller_data(), get_vxo_data(), test_dynamic_50yr_date_generator()

### Community 5 - "test_mahalanobis.py"
Cohesion: 0.15
Nodes (13): build_leverage_fig(), build_macro_valuation_fig(), build_mahalanobis_fig(), _build_packaging_proxy_fig(), build_sector_health_fig(), build_sentiment_vol_fig(), get_figure_margin(), get_right_flushed_legend() (+5 more)

### Community 6 - "StructuralBreakPredictor"
Cohesion: 0.05
Nodes (20): BubbleDetectorError, DataFetchError, ModelTrainingError, ValidationError, StructuralBreakPredictor, 10. Institutional Code Commentary, Packaging & Agent Navigation:, 1. System, Configuration & Date Horizons (`config.py` & `date_horizons.py`):, 3. Data Ingestion & Storage (`ingestor.py`): (+12 more)

### Community 8 - "PortfolioBacktestEngine"
Cohesion: 0.10
Nodes (5): BacktestResult, PortfolioBacktestEngine, market_simulation_df(), test_backtest_fee_deduction(), test_exposure_rule_vs_naive_cape()

### Community 9 - "test_bsadf_rigor.py"
Cohesion: 0.14
Nodes (8): calculate_adf_stat(), compute_gsadf_gpt_decomposition(), compute_wild_bootstrap_critical_values(), test_adf_lag_selection_k0_vs_k1(), test_adf_stat_explosive_vs_stationary(), test_recursive_backward_supremum_grid(), test_wild_bootstrap_critical_value_bounds(), test_compute_gsadf_gpt_decomposition()

### Community 12 - "generate_deck.py"
Cohesion: 0.20
Nodes (3): create_presentation(), add_card(), add_metric_badge()

### Community 13 - "features/__init__.py"
Cohesion: 0.20
Nodes (4): compute_exuberance_spans(), compute_tech_exuberance_metrics(), test_compute_exuberance_spans(), test_dual_conditions_logic()

### Community 14 - "📋 Changelog"
Cohesion: 0.14
Nodes (14): Added, Added, Added, Added, Added, Added, 📋 Changelog, Fixed (+6 more)

### Community 16 - "📉 Multidimensional Market Bubble Detector & Structural Break System"
Cohesion: 0.06
Nodes (30): 1. Continuous Backward Compounding (Cliff Eradication), 1. Macro Valuation Anchors, 1. Prerequisites & Virtual Environment, 2. Run the High-Performance NiceGUI Application, 2. Signed Macro Mahalanobis Distance & Directional Projection, 2. Systemic Liquidity & Leverage, 3. Dynamic Portfolio Equity Sizing ($w_{\text{equity}}$), 3. Econometric Explosive Bubble Diagnostics (+22 more)

### Community 17 - "dashboard.py"
Cohesion: 0.06
Nodes (25): create_cta_banner(), create_ios_card(), build_econometric_chart(), build_leverage_chart(), build_macro_valuation_chart(), build_mahalanobis_chart(), build_sector_health_chart(), build_sentiment_vol_chart() (+17 more)

### Community 18 - "test_ui_ux_wasm_optimizations.py"
Cohesion: 0.12
Nodes (8): lttb_downsample(), test_keyboard_operability_and_aria_landmarks(), test_lttb_downsample_edge_cases(), test_lttb_downsample_extrema_retention(), test_lttb_downsample_monotonic_dates(), test_service_worker_file_validity(), test_wasm_build_packaging_html_size(), test_wasm_dependency_version_locking_and_resilience_bridge()

### Community 19 - "test_data_provenance.py"
Cohesion: 0.19
Nodes (5): parse_shiller_excel(), ShillerETL, stage_all(), test_shiller_provenance_schema_and_bounds(), test_authentic_shiller_provenance_workbook()

### Community 20 - "postprocess_wasm_content"
Cohesion: 0.15
Nodes (6): postprocess_wasm_content(), clean_bokeh_templates(), postprocess_wasm_html(), test_no_synthetic_gaussian_bumps_in_data_code(), apply_postprocessing(), test_dist_index_html_postprocessing_idempotence()

### Community 21 - ".fetch_market_data"
Cohesion: 0.18
Nodes (3): test_option_1_50yr_data_ingestion(), test_option_2_modern_data_ingestion(), sample_df()

### Community 22 - "calculate_contrast_ratio"
Cohesion: 0.08
Nodes (20): calculate_contrast_ratio(), get_plotly_template(), get_theme_css(), is_wcag_aa_compliant(), parse_hex_color(), relative_luminance(), 2. UI & Accessibility Engine (`ui_theme.py`):, test_ui_theme_alias_parity() (+12 more)

### Community 23 - "FinraETL"
Cohesion: 0.20
Nodes (4): FinraETL, parse_finra_margin_debt_series(), test_finra_margin_publication_lag(), test_authentic_finra_margin_debt()

### Community 24 - "FredETL"
Cohesion: 0.12
Nodes (8): FredETL, get_fred_data(), parse_fred_macro_series(), test_fred_publication_lags(), test_central_bank_balance_sheet_splicing_continuity(), test_global_liquidity_derived_metrics(), test_global_liquidity_schema_and_publication_lags(), test_authentic_fred_gdp_and_housing()

### Community 25 - "test_splicing_continuity.py"
Cohesion: 0.20
Nodes (4): multi_decade_df(), test_spy_backward_compounding_no_cliff(), test_vxo_vix_seam_continuity(), test_xlk_backward_compounding_no_cliff()

### Community 26 - "utils.py"
Cohesion: 0.29
Nodes (3): calculate_adf_stat(), takens_embedding(), 4. Quantitative Indicator Modules (`features/` & `features/utils.py`):

### Community 27 - "numpy"
Cohesion: 0.18
Nodes (4): calibrate_lppls_filimonov(), test_lppls_parameter_recovery_synthetic(), test_lppls_sornette_filtering_bounds(), mock_indicators_df()

### Community 28 - "stage_provenance.py"
Cohesion: 0.18
Nodes (4): compute_lppls_confidence_indicator(), precompile_wasm_parquet_datasets(), ensure_synchronized_wasm_datasets(), test_lppls_confidence_indicator_pipeline()

### Community 29 - "test_tda_wavelet_rigor.py"
Cohesion: 0.14
Nodes (8): _compute_morlet_wavelet_energy_and_entropy(), _compute_persistence_landscape_and_entropy(), _compute_rips_persistence_diagrams(), _takens_embedding(), test_bubenik_l2_norm_and_persistence_entropy(), test_morlet_wavelet_scaleogram_and_spectral_entropy(), test_persistence_entropy_herding_collapse(), test_takens_delay_embedding_shape()

### Community 30 - "compute_technical_indicators"
Cohesion: 0.16
Nodes (6): compute_margin_leverage_metrics(), test_compute_margin_leverage_metrics(), test_margin_leverage_alias_parity(), test_options_volatility_alias_parity(), test_technical_alias_parity(), test_tda_wavelet_complexity_full_pipeline()

### Community 31 - "test_no_gaussian_bumps.py"
Cohesion: 0.15
Nodes (4): parse_authentic_vxo_series(), VxoETL, test_vxo_authenticity_and_black_monday(), test_authentic_cboe_vxo_black_monday()

### Community 33 - "build_tech_exuberance_fig"
Cohesion: 0.17
Nodes (5): test_pane_tech_exuberance_in_dashboard_tabs(), test_precompile_wasm_parquet_datasets(), test_tech_exuberance_columns_in_core_wasm(), test_tech_exuberance_fig_structure_desktop(), test_tech_exuberance_fig_structure_mobile()

### Community 34 - ".load_data"
Cohesion: 0.20
Nodes (3): compute_macro_valuations(), test_compute_macro_valuations(), processed_df()

### Community 35 - "generate_wasm_dataset"
Cohesion: 0.18
Nodes (7): compute_technical_indicators(), compute_tda_wavelet_complexity(), generate_wasm_dataset(), test_compute_tda_wavelet_complexity(), test_compute_technical_indicators(), test_tda_wasm_parity(), test_full_pipeline_polars_integration()

### Community 36 - "System Architecture and Operational Rules for Agents"
Cohesion: 0.40
Nodes (4): 1. Core Econometric & Statistical Rules, 2. Directory Layout & Key Modules, 3. Execution & Verification Rules, System Architecture and Operational Rules for Agents

### Community 37 - "get_current_date"
Cohesion: 0.43
Nodes (3): get_current_date(), get_dynamic_50yr_date_range(), get_dynamic_horizon_metadata()

### Community 39 - "DataIngestor"
Cohesion: 0.22
Nodes (3): DataIngestor, ingestor(), test_dashboard_state_horizon_switching()

### Community 41 - "[3.1.0] - 2026-10-05"
Cohesion: 0.33
Nodes (5): [3.0.0] - 2026-09-03, [3.1.0] - 2026-10-05, Added, Changed, Changelog

### Community 42 - "build_tech_exuberance_fig"
Cohesion: 0.25
Nodes (5): normalize_tda_indicator(), build_tech_exuberance_fig(), lttb_downsample(), normalize_tda_indicator(), _prepare_trace()

### Community 43 - "test_wasm_pyodide_sandbox.py"
Cohesion: 0.07
Nodes (9): sync_parquet_to_json(), test_date_horizon_selector_robust_against_year_shift(), test_dist_index_html_on_disk(), test_json_datasets_staging(), test_template_and_cards_reconstruction(), test_wasm_full_script_pure_numpy_fallback_execution(), test_wasm_full_script_pyodide_execution(), test_wasm_pyodide_json_memfs_loading() (+1 more)

### Community 45 - "test_ingestor.py"
Cohesion: 0.33
Nodes (3): ingestor(), test_fetch_market_data_schema_and_downcasting(), test_parquet_caching()

### Community 46 - "panel_dashboard.py"
Cohesion: 0.24
Nodes (6): build_econometric_fig(), fetch_dataset(), generate_explanatory_markdown(), get_cached_or_build_fig(), precompile_wasm_parquet_datasets(), update_all_charts()

## Knowledge Gaps
- **16 isolated node(s):** `market-bubble-detector`, `Polars DataFrame Integration`, `Margin Debt Growth Velocity`, `May 2026 Month-over-Month Change (+8.53%)`, `May 2026 Margin Debt Nominal Value ($1.416T)` (+11 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 414 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **10 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `📋 Changelog` connect `📋 Changelog` to `📉 Multidimensional Market Bubble Detector & Structural Break System`?**
  _High betweenness centrality (0.076) - this node is a cross-community bridge._
- **Are the 6 inferred relationships involving `DashboardState` (e.g. with `PortfolioBacktestEngine` and `DataIngestor`) actually correct?**
  _`DashboardState` has 6 INFERRED edges - model-reasoned connections that need verification._
- **What connects `market-bubble-detector`, `Polars DataFrame Integration`, `Margin Debt Growth Velocity` to the rest of the system?**
  _16 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Market Bubble Structural Analysis Report` be split into smaller, more focused modules?**
  _Cohesion score 0.07394957983193277 - nodes in this community are weakly interconnected._
- **Why does `DataIngestor` connect `DataIngestor` to `.load_data`, `generate_wasm_dataset`, `config.py`, `test_mahalanobis.py`, `StructuralBreakPredictor`, `PortfolioBacktestEngine`, `test_ingestor.py`, `panel_dashboard.py`, `📋 Changelog`, `dashboard.py`, `.fetch_market_data`, `test_splicing_continuity.py`, `stage_provenance.py`?**
  _High betweenness centrality (0.072) - this node is a cross-community bridge._
- **Should `test_mahalanobis.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07878787878787878 - nodes in this community are weakly interconnected._
- **Why does `📉 Multidimensional Market Bubble Detector & Structural Break System` connect `📉 Multidimensional Market Bubble Detector & Structural Break System` to `📋 Changelog`?**
  _High betweenness centrality (0.063) - this node is a cross-community bridge._