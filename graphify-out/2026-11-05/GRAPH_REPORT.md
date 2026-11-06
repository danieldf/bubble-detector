# Graph Report - Merrill  (2026-11-03)

## Corpus Check
- 83 files · ~101,154 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 19 file(s) not represented in the graph (top: .parquet 9, .csv 6, (none) 2)

## Summary
- 858 nodes · 2003 edges · 47 communities (42 shown, 5 thin omitted)
- Extraction: 93% EXTRACTED · 7% INFERRED · 0% AMBIGUOUS · INFERRED: 147 edges (avg confidence: 0.87)
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
- config.py
- build_econometric_fig
- StructuralBreakPredictor
- market-bubble-detector
- PortfolioBacktestEngine
- test_bsadf_rigor.py
- ingestor.py
- generate_deck.py
- features/__init__.py
- Detailed Slide Breakdown by Section & Group
- 📉 Multidimensional Market Bubble Detector & Structural Break System
- test_mahalanobis.py
- test_ui_ux_wasm_optimizations.py
- stage_provenance.py
- postprocess_wasm.py
- dashboard.py
- calculate_contrast_ratio
- pytest
- FredETL
- test_no_gaussian_bumps.py
- FinraETL
- compute_lppls_confidence_indicator
- ui_theme.py
- test_tda_wavelet_rigor.py
- features/__init__.py
- 📋 Changelog
- Overview of Completed Implementation: Multidimensional Market Bubble Detector
- build_tech_exuberance_fig
- compute_technical_indicators
- .fetch_market_data
- System Architecture and Operational Rules for Agents
- panel_dashboard.py
- dashboard.py
- test_splicing_continuity.py
- sw.js
- DataIngestor
- takens_embedding
- test_wasm_pyodide_sandbox.py
- precompile_wasm_parquet_datasets
- test_ingestor.py
- _prepare_trace

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
- `Fixed` --references--> `DataIngestor`  [INFERRED]
  README.md → bubble_detector/data/ingestor.py
- `Added` --references--> `compute_exuberance_spans()`  [INFERRED]
  CHANGELOG.md → bubble_detector/features/tech_exuberance.py
- `5. Machine Learning Model (`structural_breaks.py`):` --references--> `StructuralBreakPredictor`  [INFERRED]
  ImplementationOverview_DDFv100.md → bubble_detector/models/structural_breaks.py
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

## Communities (47 total, 5 thin omitted)

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
Cohesion: 0.11
Nodes (10): BubbleDetectorError, DataFetchError, ValidationError, get_current_date(), get_dynamic_50yr_date_range(), get_dynamic_horizon_metadata(), 1. System, Configuration & Date Horizons (`config.py` & `date_horizons.py`):, ingestor() (+2 more)

### Community 5 - "build_econometric_fig"
Cohesion: 0.18
Nodes (13): build_econometric_fig(), build_leverage_fig(), build_macro_valuation_fig(), build_mahalanobis_fig(), _build_packaging_proxy_fig(), build_sector_health_fig(), build_sentiment_vol_fig(), generate_explanatory_markdown() (+5 more)

### Community 6 - "StructuralBreakPredictor"
Cohesion: 0.09
Nodes (7): ModelTrainingError, StructuralBreakPredictor, test_predict_drawdown_probability(), test_structural_break_predictor_walk_forward(), test_structural_breaks_embargo_no_lookahead(), test_reliability_diagram_monotonicity(), test_walk_forward_brier_score()

### Community 8 - "PortfolioBacktestEngine"
Cohesion: 0.12
Nodes (3): BacktestResult, PortfolioBacktestEngine, test_backtest_fee_deduction()

### Community 9 - "test_bsadf_rigor.py"
Cohesion: 0.14
Nodes (9): calculate_adf_stat(), compute_gsadf_gpt_decomposition(), compute_wild_bootstrap_critical_values(), test_adf_lag_selection_k0_vs_k1(), test_adf_stat_explosive_vs_stationary(), test_recursive_backward_supremum_grid(), test_wild_bootstrap_critical_value_bounds(), test_canonical_monthly_gsadf_dotcom_spike() (+1 more)

### Community 11 - "ingestor.py"
Cohesion: 0.18
Nodes (4): get_finra_margin_debt(), get_fred_data(), get_shiller_data(), get_vxo_data()

### Community 12 - "generate_deck.py"
Cohesion: 0.20
Nodes (3): create_presentation(), add_card(), add_metric_badge()

### Community 13 - "features/__init__.py"
Cohesion: 0.13
Nodes (6): compute_exuberance_spans(), compute_tech_exuberance_metrics(), market_simulation_df(), mock_indicators_df(), test_compute_exuberance_spans(), test_dual_conditions_logic()

### Community 14 - "Detailed Slide Breakdown by Section & Group"
Cohesion: 0.22
Nodes (8): Detailed Slide Breakdown by Section & Group, Executive Presentation Deck Overview, Group 2: Supporting Evidence: Valuation, Econometrics & ML (Group Confidence Score: 0.93), Group 3: Sector Specific Application: Tech vs. Energy (Group Confidence Score: 0.91), Group 4: Implications for Systemic Stability (Group Confidence Score: 0.95), Group 5: Strategic Recommendations (Group Confidence Score: 0.96), Verification Results, Walkthrough: Multidimensional Econometric & Quantitative Market Bubble Detection PowerPoint Deck

### Community 16 - "📉 Multidimensional Market Bubble Detector & Structural Break System"
Cohesion: 0.06
Nodes (30): 1. Continuous Backward Compounding (Cliff Eradication), 1. Macro Valuation Anchors, 1. Prerequisites & Virtual Environment, 2. Run the High-Performance NiceGUI Application, 2. Signed Macro Mahalanobis Distance & Directional Projection, 2. Systemic Liquidity & Leverage, 3. Dynamic Portfolio Equity Sizing ($w_{\text{equity}}$), 3. Econometric Explosive Bubble Diagnostics (+22 more)

### Community 17 - "test_mahalanobis.py"
Cohesion: 0.08
Nodes (22): build_econometric_chart(), build_leverage_chart(), build_macro_valuation_chart(), build_mahalanobis_chart(), build_sector_health_chart(), build_sentiment_vol_chart(), build_tech_exuberance_chart(), DashboardState (+14 more)

### Community 18 - "test_ui_ux_wasm_optimizations.py"
Cohesion: 0.09
Nodes (11): calculate_adf_stat(), lttb_downsample(), normalize_tda_indicator(), test_keyboard_operability_and_aria_landmarks(), test_lttb_downsample_edge_cases(), test_lttb_downsample_extrema_retention(), test_lttb_downsample_monotonic_dates(), test_responsive_legend_layout_logic() (+3 more)

### Community 19 - "stage_provenance.py"
Cohesion: 0.13
Nodes (6): parse_authentic_vxo_series(), VxoETL, stage_all(), sync_parquet_to_json(), test_vxo_authenticity_and_black_monday(), test_authentic_cboe_vxo_black_monday()

### Community 20 - "postprocess_wasm.py"
Cohesion: 0.08
Nodes (18): postprocess_wasm_content(), clean_bokeh_templates(), postprocess_wasm_html(), sync_wasm_build_directories(), [3.0.0] - 2026-09-03, [3.1.0] - 2026-10-05, [3.2.0] - 2026-11-03, Added (+10 more)

### Community 21 - "dashboard.py"
Cohesion: 0.19
Nodes (8): create_ios_card(), create_app(), on_horizon_change(), refresh_dashboard(), run_diagnostics(), toggle_theme(), render_executive_summary_card(), render_horizon_explanatory_note()

### Community 22 - "calculate_contrast_ratio"
Cohesion: 0.20
Nodes (7): calculate_contrast_ratio(), is_wcag_aa_compliant(), 2. UI & Accessibility Engine (`ui_theme.py`):, test_ui_theme_alias_parity(), test_contrast_ratio_calculation(), test_wcag_aa_compliance(), test_wcag_aa_color_contrast_tokens()

### Community 23 - "pytest"
Cohesion: 0.18
Nodes (4): generate_wasm_dataset(), test_compute_gsadf_gpt_decomposition(), test_compute_tda_wavelet_complexity(), test_tda_wasm_parity()

### Community 24 - "FredETL"
Cohesion: 0.13
Nodes (7): FredETL, parse_fred_macro_series(), test_fred_publication_lags(), test_central_bank_balance_sheet_splicing_continuity(), test_global_liquidity_derived_metrics(), test_global_liquidity_schema_and_publication_lags(), test_authentic_fred_gdp_and_housing()

### Community 25 - "test_no_gaussian_bumps.py"
Cohesion: 0.18
Nodes (4): parse_shiller_excel(), ShillerETL, test_shiller_provenance_schema_and_bounds(), test_authentic_shiller_provenance_workbook()

### Community 26 - "FinraETL"
Cohesion: 0.20
Nodes (4): FinraETL, parse_finra_margin_debt_series(), test_finra_margin_publication_lag(), test_authentic_finra_margin_debt()

### Community 27 - "compute_lppls_confidence_indicator"
Cohesion: 0.13
Nodes (6): calibrate_lppls_filimonov(), compute_lppls_confidence_indicator(), test_lppls_confidence_indicator_pipeline(), test_lppls_historical_bubble_detection(), test_lppls_parameter_recovery_synthetic(), test_lppls_sornette_filtering_bounds()

### Community 28 - "ui_theme.py"
Cohesion: 0.19
Nodes (5): get_plotly_template(), get_theme_css(), parse_hex_color(), relative_luminance(), test_theme_css_generation()

### Community 29 - "test_tda_wavelet_rigor.py"
Cohesion: 0.12
Nodes (10): _compute_morlet_wavelet_energy_and_entropy(), _compute_persistence_landscape_and_entropy(), _compute_rips_persistence_diagrams(), compute_tda_wavelet_complexity(), _takens_embedding(), test_bubenik_l2_norm_and_persistence_entropy(), test_morlet_wavelet_scaleogram_and_spectral_entropy(), test_persistence_entropy_herding_collapse() (+2 more)

### Community 30 - "features/__init__.py"
Cohesion: 0.09
Nodes (10): compute_margin_leverage_metrics(), compute_macro_valuations(), compute_options_volatility_metrics(), test_compute_macro_valuations(), test_compute_margin_leverage_metrics(), test_compute_options_volatility_metrics(), test_full_pipeline_polars_integration(), processed_df() (+2 more)

### Community 31 - "📋 Changelog"
Cohesion: 0.15
Nodes (13): Added, Added, Added, Added, Added, 📋 Changelog, Fixed, [v1.0.0] - 2026-08-05 (+5 more)

### Community 32 - "Overview of Completed Implementation: Multidimensional Market Bubble Detector"
Cohesion: 0.25
Nodes (7): 10. Institutional Code Commentary, Packaging & Agent Navigation:, 5. Machine Learning Model (`structural_breaks.py`):, 6. Macro Mahalanobis Distance Engine (`regime_mahalanobis.py`):, 7. Interactive Dashboards & Dual-Runtime Architecture:, 8. Data Red Team Remediation & Institutional Hardening:, 9. Comprehensive Verification Suite:, Overview of Completed Implementation: Multidimensional Market Bubble Detector

### Community 33 - "build_tech_exuberance_fig"
Cohesion: 0.15
Nodes (8): build_tech_exuberance_fig(), fetch_dataset(), test_pane_tech_exuberance_in_dashboard_tabs(), test_precompile_wasm_parquet_datasets(), test_tech_exuberance_columns_in_core_wasm(), test_tech_exuberance_fig_structure_desktop(), test_tech_exuberance_fig_structure_mobile(), test_tech_exuberance_fig_structure_option_3()

### Community 34 - "compute_technical_indicators"
Cohesion: 0.20
Nodes (4): IndicatorComputationError, compute_technical_indicators(), test_compute_technical_indicators(), test_technical_alias_parity()

### Community 35 - ".fetch_market_data"
Cohesion: 0.18
Nodes (3): test_option_1_50yr_data_ingestion(), test_option_2_modern_data_ingestion(), test_option_3_20yr_data_ingestion()

### Community 36 - "System Architecture and Operational Rules for Agents"
Cohesion: 0.40
Nodes (4): 1. Core Econometric & Statistical Rules, 2. Directory Layout & Key Modules, 3. Execution & Verification Rules, System Architecture and Operational Rules for Agents

### Community 37 - "panel_dashboard.py"
Cohesion: 0.24
Nodes (4): get_current_date(), get_dynamic_50yr_date_range(), get_dynamic_horizon_metadata(), precompile_wasm_parquet_datasets()

### Community 38 - "dashboard.py"
Cohesion: 0.15
Nodes (3): compute_validation_summary_statistics(), generate_historical_validation_table(), create_cta_banner()

### Community 39 - "test_splicing_continuity.py"
Cohesion: 0.20
Nodes (4): multi_decade_df(), test_spy_backward_compounding_no_cliff(), test_vxo_vix_seam_continuity(), test_xlk_backward_compounding_no_cliff()

### Community 41 - "DataIngestor"
Cohesion: 0.29
Nodes (3): DataIngestor, 3. Data Ingestion & Storage (`ingestor.py`):, sample_df()

### Community 42 - "takens_embedding"
Cohesion: 0.50
Nodes (3): takens_embedding(), 4. Quantitative Indicator Modules (`features/` & `features/utils.py`):, Added

### Community 43 - "test_wasm_pyodide_sandbox.py"
Cohesion: 0.08
Nodes (8): test_date_horizon_selector_robust_against_year_shift(), test_dist_index_html_on_disk(), test_json_datasets_staging(), test_template_and_cards_reconstruction(), test_wasm_full_script_pure_numpy_fallback_execution(), test_wasm_full_script_pyodide_execution(), test_wasm_pyodide_json_memfs_loading(), test_wasm_pyodide_pure_numpy_fallback()

### Community 45 - "test_ingestor.py"
Cohesion: 0.33
Nodes (3): ingestor(), test_fetch_market_data_schema_and_downcasting(), test_parquet_caching()

### Community 46 - "_prepare_trace"
Cohesion: 0.40
Nodes (3): lttb_downsample(), normalize_tda_indicator(), _prepare_trace()

## Knowledge Gaps
- **16 isolated node(s):** `market-bubble-detector`, `Polars DataFrame Integration`, `Margin Debt Growth Velocity`, `May 2026 Month-over-Month Change (+8.53%)`, `May 2026 Margin Debt Nominal Value ($1.416T)` (+11 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 420 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `📋 Changelog` connect `📋 Changelog` to `📉 Multidimensional Market Bubble Detector & Structural Break System`, `postprocess_wasm.py`?**
  _High betweenness centrality (0.078) - this node is a cross-community bridge._
- **Are the 7 inferred relationships involving `DashboardState` (e.g. with `PortfolioBacktestEngine` and `DataIngestor`) actually correct?**
  _`DashboardState` has 7 INFERRED edges - model-reasoned connections that need verification._
- **What connects `market-bubble-detector`, `Polars DataFrame Integration`, `Margin Debt Growth Velocity` to the rest of the system?**
  _16 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Market Bubble Structural Analysis Report` be split into smaller, more focused modules?**
  _Cohesion score 0.07394957983193277 - nodes in this community are weakly interconnected._
- **Why does `DataIngestor` connect `DataIngestor` to `.fetch_market_data`, `config.py`, `panel_dashboard.py`, `dashboard.py`, `test_splicing_continuity.py`, `PortfolioBacktestEngine`, `takens_embedding`, `ingestor.py`, `precompile_wasm_parquet_datasets`, `test_ingestor.py`, `test_mahalanobis.py`, `stage_provenance.py`, `pytest`, `features/__init__.py`, `📋 Changelog`?**
  _High betweenness centrality (0.071) - this node is a cross-community bridge._
- **Should `test_mahalanobis.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07878787878787878 - nodes in this community are weakly interconnected._
- **Why does `📉 Multidimensional Market Bubble Detector & Structural Break System` connect `📉 Multidimensional Market Bubble Detector & Structural Break System` to `📋 Changelog`?**
  _High betweenness centrality (0.062) - this node is a cross-community bridge._