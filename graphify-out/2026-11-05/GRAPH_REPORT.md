# Graph Report - Merrill  (2026-11-05)

## Corpus Check
- 85 files · ~125,523 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 19 file(s) not represented in the graph (top: .parquet 9, .csv 6, (none) 2)

## Summary
- 935 nodes · 2261 edges · 39 communities (32 shown, 7 thin omitted)
- Extraction: 92% EXTRACTED · 8% INFERRED · 0% AMBIGUOUS · INFERRED: 176 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `9caca659`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Market Bubble Structural Analysis Report
- MacroMahalanobisDetector
- deploy.yml
- Implied Volatility Metrics Table (July 2026)
- 📉 Multidimensional Market Bubble Detector & Structural Break System
- test_full_indicator_parity.py
- StructuralBreakPredictor
- market-bubble-detector
- PortfolioBacktestEngine
- test_bsadf_rigor.py
- config.py
- generate_deck.py
- features/__init__.py
- test_no_gaussian_bumps.py
- get_right_flushed_legend
- dashboard.py
- test_ui_ux_wasm_optimizations.py
- stage_provenance.py
- postprocess_wasm.py
- ui_theme.py
- FredETL
- test_no_gaussian_bumps.py
- FinraETL
- compute_lppls_confidence_indicator
- composite_summary.py
- test_tda_wavelet_rigor.py
- pytest
- Overview of Completed Implementation: Multidimensional Market Bubble Detector
- build_tech_exuberance_fig
- polars
- DataIngestor
- System Architecture and Operational Rules for Agents
- panel_dashboard.py
- get_current_date
- sw.js
- test_wasm_pyodide_sandbox.py
- DataIngestor

## God Nodes (most connected - your core abstractions)
1. `DashboardState` - 48 edges
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

## Communities (39 total, 7 thin omitted)

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

### Community 5 - "test_full_indicator_parity.py"
Cohesion: 0.13
Nodes (16): build_composite_summary_fig(), build_econometric_fig(), build_leverage_fig(), build_macro_valuation_fig(), build_mahalanobis_fig(), _build_packaging_proxy_fig(), build_sector_health_fig(), build_sentiment_vol_fig() (+8 more)

### Community 6 - "StructuralBreakPredictor"
Cohesion: 0.12
Nodes (6): StructuralBreakPredictor, test_predict_drawdown_probability(), test_structural_break_predictor_walk_forward(), test_structural_breaks_embargo_no_lookahead(), test_reliability_diagram_monotonicity(), test_walk_forward_brier_score()

### Community 8 - "PortfolioBacktestEngine"
Cohesion: 0.08
Nodes (7): BacktestResult, PortfolioBacktestEngine, compute_validation_summary_statistics(), generate_historical_validation_table(), market_simulation_df(), test_backtest_fee_deduction(), test_exposure_rule_vs_naive_cape()

### Community 9 - "test_bsadf_rigor.py"
Cohesion: 0.11
Nodes (10): calculate_adf_stat(), compute_gsadf_gpt_decomposition(), compute_wild_bootstrap_critical_values(), test_adf_lag_selection_k0_vs_k1(), test_adf_stat_explosive_vs_stationary(), test_recursive_backward_supremum_grid(), test_wild_bootstrap_critical_value_bounds(), test_compute_gsadf_gpt_decomposition() (+2 more)

### Community 11 - "config.py"
Cohesion: 0.16
Nodes (4): get_finra_margin_debt(), get_fred_data(), get_shiller_data(), get_vxo_data()

### Community 12 - "generate_deck.py"
Cohesion: 0.20
Nodes (3): create_presentation(), add_card(), add_metric_badge()

### Community 13 - "features/__init__.py"
Cohesion: 0.22
Nodes (4): compute_exuberance_spans(), compute_tech_exuberance_metrics(), test_compute_exuberance_spans(), test_dual_conditions_logic()

### Community 17 - "dashboard.py"
Cohesion: 0.06
Nodes (33): build_band_polygon(), create_cta_banner(), create_ios_card(), build_composite_summary_chart(), build_composite_validation_chart(), build_dislocation_fidelity_chart(), build_econometric_chart(), build_leverage_chart() (+25 more)

### Community 18 - "test_ui_ux_wasm_optimizations.py"
Cohesion: 0.10
Nodes (10): calculate_adf_stat(), lttb_downsample(), normalize_tda_indicator(), test_keyboard_operability_and_aria_landmarks(), test_lttb_downsample_edge_cases(), test_lttb_downsample_extrema_retention(), test_lttb_downsample_monotonic_dates(), test_service_worker_file_validity() (+2 more)

### Community 19 - "stage_provenance.py"
Cohesion: 0.17
Nodes (5): parse_authentic_vxo_series(), VxoETL, stage_all(), test_vxo_authenticity_and_black_monday(), test_authentic_cboe_vxo_black_monday()

### Community 20 - "postprocess_wasm.py"
Cohesion: 0.07
Nodes (23): postprocess_wasm_content(), clean_bokeh_templates(), postprocess_wasm_html(), sync_wasm_build_directories(), [3.0.0] - 2026-09-03, [3.1.0] - 2026-10-05, [3.2.0] - 2026-11-03, [3.3.0] - 2026-11-05 (+15 more)

### Community 22 - "ui_theme.py"
Cohesion: 0.08
Nodes (20): calculate_contrast_ratio(), get_plotly_template(), get_theme_css(), is_wcag_aa_compliant(), parse_hex_color(), relative_luminance(), 2. UI & Accessibility Engine (`ui_theme.py`):, test_ui_theme_alias_parity() (+12 more)

### Community 24 - "FredETL"
Cohesion: 0.13
Nodes (7): FredETL, parse_fred_macro_series(), test_fred_publication_lags(), test_central_bank_balance_sheet_splicing_continuity(), test_global_liquidity_derived_metrics(), test_global_liquidity_schema_and_publication_lags(), test_authentic_fred_gdp_and_housing()

### Community 25 - "test_no_gaussian_bumps.py"
Cohesion: 0.20
Nodes (4): parse_shiller_excel(), ShillerETL, test_shiller_provenance_schema_and_bounds(), test_authentic_shiller_provenance_workbook()

### Community 26 - "FinraETL"
Cohesion: 0.20
Nodes (4): FinraETL, parse_finra_margin_debt_series(), test_finra_margin_publication_lag(), test_authentic_finra_margin_debt()

### Community 27 - "compute_lppls_confidence_indicator"
Cohesion: 0.10
Nodes (10): calibrate_lppls_filimonov(), compute_lppls_confidence_indicator(), test_five_summary_indicators_bounds_and_crash_separation_20yr(), test_lppls_confidence_indicator_pipeline(), test_lppls_historical_bubble_detection(), test_lppls_parameter_recovery_synthetic(), test_lppls_sornette_filtering_bounds(), test_spy_backward_compounding_no_cliff() (+2 more)

### Community 28 - "composite_summary.py"
Cohesion: 0.08
Nodes (13): causal_ffill_clean(), causal_gram_schmidt(), causal_stationary_unit_variance(), CompositeSummaryEngine, compute_composite_validation_metrics(), compute_dislocation_fidelity_metrics(), compute_orthogonal_basis_and_summaries_numpy(), norm_cdf_numpy() (+5 more)

### Community 29 - "test_tda_wavelet_rigor.py"
Cohesion: 0.12
Nodes (11): _compute_morlet_wavelet_energy_and_entropy(), _compute_persistence_landscape_and_entropy(), _compute_rips_persistence_diagrams(), compute_tda_wavelet_complexity(), _takens_embedding(), test_compute_tda_wavelet_complexity(), test_bubenik_l2_norm_and_persistence_entropy(), test_morlet_wavelet_scaleogram_and_spectral_entropy() (+3 more)

### Community 31 - "Overview of Completed Implementation: Multidimensional Market Bubble Detector"
Cohesion: 0.06
Nodes (30): takens_embedding(), 10. Institutional Code Commentary, Packaging & Agent Navigation:, 3. Data Ingestion & Storage (`ingestor.py`):, 4. Quantitative Indicator Modules (`features/` & `features/utils.py`):, 5. Machine Learning Model (`structural_breaks.py`):, 6. Macro Mahalanobis Distance Engine (`regime_mahalanobis.py`):, 7. Interactive Dashboards & Dual-Runtime Architecture:, 8. Data Red Team Remediation & Institutional Hardening: (+22 more)

### Community 33 - "build_tech_exuberance_fig"
Cohesion: 0.15
Nodes (8): build_tech_exuberance_fig(), fetch_dataset(), test_pane_tech_exuberance_in_dashboard_tabs(), test_precompile_wasm_parquet_datasets(), test_tech_exuberance_columns_in_core_wasm(), test_tech_exuberance_fig_structure_desktop(), test_tech_exuberance_fig_structure_mobile(), test_tech_exuberance_fig_structure_option_3()

### Community 34 - "polars"
Cohesion: 0.08
Nodes (14): compute_margin_leverage_metrics(), compute_macro_valuations(), compute_options_volatility_metrics(), compute_technical_indicators(), test_compute_macro_valuations(), test_compute_margin_leverage_metrics(), test_compute_options_volatility_metrics(), test_compute_technical_indicators() (+6 more)

### Community 35 - "DataIngestor"
Cohesion: 0.05
Nodes (17): BubbleDetectorError, DataFetchError, IndicatorComputationError, ModelTrainingError, ValidationError, get_current_date(), get_dynamic_50yr_date_range(), get_dynamic_horizon_metadata() (+9 more)

### Community 36 - "System Architecture and Operational Rules for Agents"
Cohesion: 0.40
Nodes (4): 1. Core Econometric & Statistical Rules, 2. Directory Layout & Key Modules, 3. Execution & Verification Rules, System Architecture and Operational Rules for Agents

### Community 37 - "panel_dashboard.py"
Cohesion: 0.18
Nodes (8): build_band_polygon(), build_composite_validation_fig(), build_dislocation_fidelity_fig(), compute_composite_validation_metrics(), compute_dislocation_fidelity_metrics(), generate_explanatory_markdown(), precompile_wasm_parquet_datasets(), update_all_charts()

### Community 39 - "get_current_date"
Cohesion: 0.43
Nodes (3): get_current_date(), get_dynamic_50yr_date_range(), get_dynamic_horizon_metadata()

### Community 43 - "test_wasm_pyodide_sandbox.py"
Cohesion: 0.08
Nodes (7): test_date_horizon_selector_robust_against_year_shift(), test_dist_index_html_on_disk(), test_template_and_cards_reconstruction(), test_wasm_full_script_pure_numpy_fallback_execution(), test_wasm_full_script_pyodide_execution(), test_wasm_pyodide_json_memfs_loading(), test_wasm_pyodide_pure_numpy_fallback()

### Community 49 - "DataIngestor"
Cohesion: 0.09
Nodes (8): DataIngestor, generate_wasm_dataset(), ingestor(), test_dashboard_state_horizon_switching(), sample_df(), test_all_indicators_numerical_parity(), multi_decade_df(), test_wasm_loads_exact_parquet_dataset()

## Knowledge Gaps
- **16 isolated node(s):** `market-bubble-detector`, `Polars DataFrame Integration`, `Margin Debt Growth Velocity`, `May 2026 Month-over-Month Change (+8.53%)`, `May 2026 Margin Debt Nominal Value ($1.416T)` (+11 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 454 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **7 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `build_dislocation_fidelity_chart()` connect `dashboard.py` to `📉 Multidimensional Market Bubble Detector & Structural Break System`, `postprocess_wasm.py`, `compute_lppls_confidence_indicator`, `composite_summary.py`, `Overview of Completed Implementation: Multidimensional Market Bubble Detector`?**
  _High betweenness centrality (0.051) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `DashboardState` (e.g. with `PortfolioBacktestEngine` and `DataIngestor`) actually correct?**
  _`DashboardState` has 11 INFERRED edges - model-reasoned connections that need verification._
- **What connects `market-bubble-detector`, `Polars DataFrame Integration`, `Margin Debt Growth Velocity` to the rest of the system?**
  _16 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Market Bubble Structural Analysis Report` be split into smaller, more focused modules?**
  _Cohesion score 0.07563025210084033 - nodes in this community are weakly interconnected._
- **Why does `8. Composite Summary Indicators: Information-Maximizing Orthogonal Synthesis ($\mathcal{B}_{13}^{\perp}$)` connect `📉 Multidimensional Market Bubble Detector & Structural Break System` to `dashboard.py`, `panel_dashboard.py`?**
  _High betweenness centrality (0.049) - this node is a cross-community bridge._
- **Should `MacroMahalanobisDetector` be split into smaller, more focused modules?**
  _Cohesion score 0.07878787878787878 - nodes in this community are weakly interconnected._
- **Should `deploy.yml` be split into smaller, more focused modules?**
  _Cohesion score 0.06881720430107527 - nodes in this community are weakly interconnected._