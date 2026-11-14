# Graph Report - Merrill  (2026-11-13)

## Corpus Check
- 85 files · ~126,219 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 19 file(s) not represented in the graph (top: .parquet 9, .csv 6, (none) 2)

## Summary
- 940 nodes · 2252 edges · 47 communities (38 shown, 9 thin omitted)
- Extraction: 92% EXTRACTED · 8% INFERRED · 0% AMBIGUOUS · INFERRED: 188 edges (avg confidence: 0.88)
- Token cost: 64,000 input · 3,600 output

## Graph Freshness
- Built from commit: `980bd093`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Market Bubble Structural Analysis Report
- MacroMahalanobisDetector
- deploy.yml
- Implied Volatility Metrics Table (July 2026)
- 📉 Multidimensional Market Bubble Detector & Structural Break System
- build_mahalanobis_fig
- StructuralBreakPredictor
- market-bubble-detector
- PortfolioBacktestEngine
- test_bsadf_rigor.py
- generate_deck.py
- test_composite_summary_tab8.py
- test_ui_ux_wasm_optimizations.py
- ui_theme.py
- dashboard.py
- lttb_downsample
- stage_provenance.py
- postprocess_wasm.py
- pandas
- calculate_contrast_ratio
- Overview of Completed Implementation: Multidimensional Market Bubble Detector
- FredETL
- test_no_gaussian_bumps.py
- FinraETL
- compute_lppls_confidence_indicator
- composite_summary.py
- test_tda_wavelet_rigor.py
- precompile_wasm_parquet_datasets
- compute_tech_exuberance_metrics
- Detailed Slide Breakdown by Section & Group
- build_tech_exuberance_fig
- polars
- DataIngestor
- System Architecture and Operational Rules for Agents
- panel_dashboard.py
- get_vxo_data
- get_current_date
- sw.js
- mock_indicators_df
- build_composite_summary_fig
- test_wasm_pyodide_sandbox.py
- DataIngestor

## God Nodes (most connected - your core abstractions)
1. `DashboardState` - 48 edges
2. `MacroMahalanobisDetector` - 36 edges
3. `DataIngestor` - 31 edges
4. `generate_wasm_dataset()` - 31 edges
5. `StructuralBreakPredictor` - 30 edges
6. `compute_tda_wavelet_complexity()` - 26 edges
7. `test_all_7_tabs_plot_trace_parity()` - 24 edges
8. `compute_gsadf_gpt_decomposition()` - 23 edges
9. `precompile_wasm_parquet_datasets()` - 22 edges
10. `build_tech_exuberance_fig()` - 21 edges

## Surprising Connections (you probably didn't know these)
- `3. Data Ingestion & Storage (`ingestor.py`):` --references--> `DataIngestor`  [INFERRED]
  ImplementationOverview_DDFv100.md → bubble_detector/data/ingestor.py
- `Fixed` --references--> `DataIngestor`  [INFERRED]
  README.md → bubble_detector/data/ingestor.py
- `5. Machine Learning Model (`structural_breaks.py`):` --references--> `StructuralBreakPredictor`  [INFERRED]
  ImplementationOverview_DDFv100.md → bubble_detector/models/structural_breaks.py
- `Added` --references--> `test_all_tabs_legends_right_flushed()`  [INFERRED]
  README.md → tests/test_mahalanobis.py
- `Added` --references--> `test_tda_normalization_tabs_5_and_6()`  [INFERRED]
  README.md → tests/test_mahalanobis.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **AGVI Indicator and Feature Engineering Pipeline** — marketbubble_ddfv100_shiller_cape_ratio, marketbubble_ddfv100_payout_adjusted_cape, marketbubble_ddfv100_buffett_indicator, marketbubble_ddfv100_gsadf_psy_procedure [EXTRACTED 1.00]
- **Econometric and Mathematical Bubble Detection Framework** — marketbubble_ddfv100_gsadf_psy_procedure, marketbubble_ddfv100_tda_wavelet, marketbubble_ddfv100_lppls_model [EXTRACTED 1.00]
- **Implied Volatility Term Structure Components** — impliedvolatilitymetric_vix1d, impliedvolatilitymetric_vix_spot, impliedvolatilitymetric_vix3m, impliedvolatilitymetric_vix1y [EXTRACTED 1.00]
- **FINRA Margin Debt Metrics** — finra_margin_debt_tracker, finra_may_2026_nominal_value, finra_may_2026_mom_change, finra_may_2026_yoy_change [INFERRED 0.85]

## Communities (47 total, 9 thin omitted)

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
Cohesion: 0.06
Nodes (31): 1. Continuous Backward Compounding (Cliff Eradication), 1. Macro Valuation Anchors, 1. Prerequisites & Virtual Environment, 2. Run the High-Performance NiceGUI Application, 2. Signed Macro Mahalanobis Distance & Directional Projection, 2. Systemic Liquidity & Leverage, 3. Dynamic Portfolio Equity Sizing ($w_{\text{equity}}$), 3. Econometric Explosive Bubble Diagnostics (+23 more)

### Community 5 - "build_mahalanobis_fig"
Cohesion: 0.15
Nodes (14): build_econometric_fig(), build_leverage_fig(), build_macro_valuation_fig(), build_mahalanobis_fig(), _build_packaging_proxy_fig(), build_sector_health_fig(), build_sentiment_vol_fig(), generate_explanatory_markdown() (+6 more)

### Community 6 - "StructuralBreakPredictor"
Cohesion: 0.13
Nodes (6): StructuralBreakPredictor, test_predict_drawdown_probability(), test_structural_break_predictor_walk_forward(), test_structural_breaks_embargo_no_lookahead(), test_reliability_diagram_monotonicity(), test_walk_forward_brier_score()

### Community 8 - "PortfolioBacktestEngine"
Cohesion: 0.08
Nodes (7): BacktestResult, PortfolioBacktestEngine, compute_validation_summary_statistics(), generate_historical_validation_table(), market_simulation_df(), test_backtest_fee_deduction(), test_exposure_rule_vs_naive_cape()

### Community 9 - "test_bsadf_rigor.py"
Cohesion: 0.13
Nodes (10): calculate_adf_stat(), compute_gsadf_gpt_decomposition(), compute_wild_bootstrap_critical_values(), test_adf_lag_selection_k0_vs_k1(), test_adf_stat_explosive_vs_stationary(), test_recursive_backward_supremum_grid(), test_wild_bootstrap_critical_value_bounds(), test_compute_gsadf_gpt_decomposition() (+2 more)

### Community 12 - "generate_deck.py"
Cohesion: 0.17
Nodes (3): create_presentation(), add_card(), add_metric_badge()

### Community 13 - "test_composite_summary_tab8.py"
Cohesion: 0.09
Nodes (12): build_band_polygon(), compute_composite_validation_metrics(), compute_dislocation_fidelity_metrics(), build_composite_validation_chart(), build_composite_validation_fig(), Added, Added, test_dislocation_8_fidelity_metrics_popperian_falsification_20yr() (+4 more)

### Community 14 - "test_ui_ux_wasm_optimizations.py"
Cohesion: 0.11
Nodes (9): lttb_downsample(), test_keyboard_operability_and_aria_landmarks(), test_lttb_downsample_edge_cases(), test_lttb_downsample_extrema_retention(), test_lttb_downsample_monotonic_dates(), test_service_worker_file_validity(), test_wasm_build_packaging_html_size(), test_wasm_dependency_version_locking_and_resilience_bridge() (+1 more)

### Community 16 - "ui_theme.py"
Cohesion: 0.24
Nodes (3): get_plotly_template(), parse_hex_color(), relative_luminance()

### Community 17 - "dashboard.py"
Cohesion: 0.07
Nodes (28): normalize_tda_indicator(), create_cta_banner(), create_ios_card(), build_composite_summary_chart(), build_dislocation_fidelity_chart(), build_econometric_chart(), build_leverage_chart(), build_macro_valuation_chart() (+20 more)

### Community 18 - "lttb_downsample"
Cohesion: 0.29
Nodes (3): calculate_adf_stat(), takens_embedding(), 4. Quantitative Indicator Modules (`features/` & `features/utils.py`):

### Community 19 - "stage_provenance.py"
Cohesion: 0.16
Nodes (7): ShillerETL, VxoETL, stage_all(), sync_parquet_to_json(), test_authentic_cboe_vxo_black_monday(), test_authentic_shiller_provenance_workbook(), test_json_datasets_staging()

### Community 20 - "postprocess_wasm.py"
Cohesion: 0.06
Nodes (29): postprocess_wasm_content(), clean_bokeh_templates(), postprocess_wasm_html(), sync_wasm_build_directories(), [3.2.0] - 2026-11-03, Added, Changed, Added (+21 more)

### Community 21 - "pandas"
Cohesion: 0.24
Nodes (4): multi_decade_df(), test_spy_backward_compounding_no_cliff(), test_vxo_vix_seam_continuity(), test_xlk_backward_compounding_no_cliff()

### Community 22 - "calculate_contrast_ratio"
Cohesion: 0.19
Nodes (8): calculate_contrast_ratio(), get_theme_css(), is_wcag_aa_compliant(), 2. UI & Accessibility Engine (`ui_theme.py`):, test_ui_theme_alias_parity(), test_contrast_ratio_calculation(), test_theme_css_generation(), test_wcag_aa_compliance()

### Community 23 - "Overview of Completed Implementation: Multidimensional Market Bubble Detector"
Cohesion: 0.22
Nodes (8): 10. Institutional Code Commentary, Packaging & Agent Navigation:, 3. Data Ingestion & Storage (`ingestor.py`):, 5. Machine Learning Model (`structural_breaks.py`):, 6. Macro Mahalanobis Distance Engine (`regime_mahalanobis.py`):, 7. Interactive Dashboards & Dual-Runtime Architecture:, 8. Data Red Team Remediation & Institutional Hardening:, 9. Comprehensive Verification Suite:, Overview of Completed Implementation: Multidimensional Market Bubble Detector

### Community 24 - "FredETL"
Cohesion: 0.12
Nodes (8): FredETL, get_fred_data(), parse_fred_macro_series(), test_fred_publication_lags(), test_central_bank_balance_sheet_splicing_continuity(), test_global_liquidity_derived_metrics(), test_global_liquidity_schema_and_publication_lags(), test_authentic_fred_gdp_and_housing()

### Community 25 - "test_no_gaussian_bumps.py"
Cohesion: 0.21
Nodes (3): get_shiller_data(), parse_shiller_excel(), test_shiller_provenance_schema_and_bounds()

### Community 26 - "FinraETL"
Cohesion: 0.16
Nodes (5): FinraETL, get_finra_margin_debt(), parse_finra_margin_debt_series(), test_finra_margin_publication_lag(), test_authentic_finra_margin_debt()

### Community 27 - "compute_lppls_confidence_indicator"
Cohesion: 0.13
Nodes (6): calibrate_lppls_filimonov(), compute_lppls_confidence_indicator(), test_lppls_confidence_indicator_pipeline(), test_lppls_historical_bubble_detection(), test_lppls_parameter_recovery_synthetic(), test_lppls_sornette_filtering_bounds()

### Community 28 - "composite_summary.py"
Cohesion: 0.13
Nodes (8): causal_ffill_clean(), causal_gram_schmidt(), causal_stationary_unit_variance(), CompositeSummaryEngine, compute_orthogonal_basis_and_summaries_numpy(), norm_cdf_numpy(), test_orthogonal_basis_13_spectral_entropy_and_vif_20yr(), test_strict_causal_filtration_zero_lookahead()

### Community 29 - "test_tda_wavelet_rigor.py"
Cohesion: 0.12
Nodes (11): _compute_morlet_wavelet_energy_and_entropy(), _compute_persistence_landscape_and_entropy(), _compute_rips_persistence_diagrams(), compute_tda_wavelet_complexity(), _takens_embedding(), test_compute_tda_wavelet_complexity(), test_bubenik_l2_norm_and_persistence_entropy(), test_morlet_wavelet_scaleogram_and_spectral_entropy() (+3 more)

### Community 31 - "compute_tech_exuberance_metrics"
Cohesion: 0.10
Nodes (14): compute_exuberance_spans(), compute_tech_exuberance_metrics(), [3.0.0] - 2026-09-03, [3.1.0] - 2026-10-05, [3.3.0] - 2026-11-05, [3.4.0] - 2026-11-05, [3.5.0] - 2026-11-05, Added (+6 more)

### Community 32 - "Detailed Slide Breakdown by Section & Group"
Cohesion: 0.22
Nodes (8): Detailed Slide Breakdown by Section & Group, Executive Presentation Deck Overview, Group 2: Supporting Evidence: Valuation, Econometrics & ML (Group Confidence Score: 0.93), Group 3: Sector Specific Application: Tech vs. Energy (Group Confidence Score: 0.91), Group 4: Implications for Systemic Stability (Group Confidence Score: 0.95), Group 5: Strategic Recommendations (Group Confidence Score: 0.96), Verification Results, Walkthrough: Multidimensional Econometric & Quantitative Market Bubble Detection PowerPoint Deck

### Community 33 - "build_tech_exuberance_fig"
Cohesion: 0.15
Nodes (8): build_tech_exuberance_fig(), fetch_dataset(), test_pane_tech_exuberance_in_dashboard_tabs(), test_precompile_wasm_parquet_datasets(), test_tech_exuberance_columns_in_core_wasm(), test_tech_exuberance_fig_structure_desktop(), test_tech_exuberance_fig_structure_mobile(), test_tech_exuberance_fig_structure_option_3()

### Community 34 - "polars"
Cohesion: 0.08
Nodes (13): compute_margin_leverage_metrics(), compute_macro_valuations(), compute_options_volatility_metrics(), compute_technical_indicators(), test_compute_macro_valuations(), test_compute_margin_leverage_metrics(), test_compute_options_volatility_metrics(), test_compute_technical_indicators() (+5 more)

### Community 35 - "DataIngestor"
Cohesion: 0.05
Nodes (17): BubbleDetectorError, DataFetchError, IndicatorComputationError, ModelTrainingError, ValidationError, get_current_date(), get_dynamic_50yr_date_range(), get_dynamic_horizon_metadata() (+9 more)

### Community 36 - "System Architecture and Operational Rules for Agents"
Cohesion: 0.40
Nodes (4): 1. Core Econometric & Statistical Rules, 2. Directory Layout & Key Modules, 3. Execution & Verification Rules, System Architecture and Operational Rules for Agents

### Community 37 - "panel_dashboard.py"
Cohesion: 0.15
Nodes (8): build_band_polygon(), build_dislocation_fidelity_fig(), compute_composite_validation_metrics(), compute_dislocation_fidelity_metrics(), lttb_downsample(), normalize_tda_indicator(), precompile_wasm_parquet_datasets(), _prepare_trace()

### Community 38 - "get_vxo_data"
Cohesion: 0.19
Nodes (3): get_vxo_data(), parse_authentic_vxo_series(), test_vxo_authenticity_and_black_monday()

### Community 39 - "get_current_date"
Cohesion: 0.43
Nodes (3): get_current_date(), get_dynamic_50yr_date_range(), get_dynamic_horizon_metadata()

### Community 42 - "build_composite_summary_fig"
Cohesion: 0.29
Nodes (3): build_composite_summary_fig(), test_tab8_dislocation_fidelity_dual_ui_parity(), test_tab8_dual_ui_parity_across_all_horizons()

### Community 43 - "test_wasm_pyodide_sandbox.py"
Cohesion: 0.08
Nodes (9): apply_postprocessing(), test_date_horizon_selector_robust_against_year_shift(), test_dist_index_html_on_disk(), test_dist_index_html_postprocessing_idempotence(), test_template_and_cards_reconstruction(), test_wasm_full_script_pure_numpy_fallback_execution(), test_wasm_full_script_pyodide_execution(), test_wasm_pyodide_json_memfs_loading() (+1 more)

### Community 49 - "DataIngestor"
Cohesion: 0.08
Nodes (10): DataIngestor, generate_wasm_dataset(), Added, ingestor(), test_dashboard_state_horizon_switching(), sample_df(), test_tda_wasm_parity(), test_all_indicators_numerical_parity() (+2 more)

## Knowledge Gaps
- **16 isolated node(s):** `market-bubble-detector`, `Polars DataFrame Integration`, `Margin Debt Growth Velocity`, `May 2026 Month-over-Month Change (+8.53%)`, `May 2026 Margin Debt Nominal Value ($1.416T)` (+11 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 458 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **9 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `build_dislocation_fidelity_chart()` connect `dashboard.py` to `📉 Multidimensional Market Bubble Detector & Structural Break System`, `test_bsadf_rigor.py`, `build_composite_summary_fig`, `test_composite_summary_tab8.py`, `postprocess_wasm.py`, `compute_tech_exuberance_metrics`?**
  _High betweenness centrality (0.052) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `DashboardState` (e.g. with `PortfolioBacktestEngine` and `DataIngestor`) actually correct?**
  _`DashboardState` has 11 INFERRED edges - model-reasoned connections that need verification._
- **What connects `market-bubble-detector`, `Polars DataFrame Integration`, `Margin Debt Growth Velocity` to the rest of the system?**
  _16 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Market Bubble Structural Analysis Report` be split into smaller, more focused modules?**
  _Cohesion score 0.07563025210084033 - nodes in this community are weakly interconnected._
- **Why does `8. Composite Summary Indicators: Information-Maximizing Orthogonal Synthesis ($\mathcal{B}_{13}^{\perp}$)` connect `📉 Multidimensional Market Bubble Detector & Structural Break System` to `dashboard.py`, `panel_dashboard.py`?**
  _High betweenness centrality (0.048) - this node is a cross-community bridge._
- **Should `MacroMahalanobisDetector` be split into smaller, more focused modules?**
  _Cohesion score 0.07878787878787878 - nodes in this community are weakly interconnected._
- **Why does `DataIngestor` connect `DataIngestor` to `polars`, `DataIngestor`, `panel_dashboard.py`, `config.py`, `test_composite_summary_tab8.py`, `dashboard.py`, `stage_provenance.py`, `postprocess_wasm.py`, `pandas`, `Overview of Completed Implementation: Multidimensional Market Bubble Detector`, `precompile_wasm_parquet_datasets`?**
  _High betweenness centrality (0.048) - this node is a cross-community bridge._