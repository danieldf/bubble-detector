# Graph Report - Merrill  (2026-11-14)

## Corpus Check
- 95 files · ~149,725 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 19 file(s) not represented in the graph (top: .parquet 9, .csv 6, (none) 2)

## Summary
- 1071 nodes · 2424 edges · 58 communities (47 shown, 11 thin omitted)
- Extraction: 92% EXTRACTED · 8% INFERRED · 0% AMBIGUOUS · INFERRED: 189 edges (avg confidence: 0.88)
- Token cost: 64,000 input · 3,600 output

## Graph Freshness
- Built from commit: `f8afdba4`
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
- config.py
- generate_deck.py
- build_composite_validation_fig
- test_ui_ux_wasm_optimizations.py
- ui_theme.py
- dashboard.py
- lttb_downsample
- HighFidelityEventStudy_Executive_Report.md
- HighFidelityEventStudy/README.md
- pandas
- calculate_contrast_ratio
- generate_high_fidelity_plots.py
- FredETL
- test_no_gaussian_bumps.py
- FinraETL
- compute_lppls_confidence_indicator
- test_composite_summary_tab8.py
- test_tda_wavelet_rigor.py
- precompile_wasm_parquet_datasets
- compute_tech_exuberance_metrics
- Detailed Slide Breakdown by Section & Group
- build_tech_exuberance_fig
- polars
- DataIngestor
- System Architecture and Operational Rules for Agents
- build_dislocation_fidelity_fig
- get_vxo_data
- get_current_date
- sw.js
- mock_indicators_df
- dashboard.py
- test_wasm_pyodide_sandbox.py
- features/__init__.py
- pytest
- Appendix: Architectural Principles & Methodological Justification (IP-Protected Technical Overview)
- generate_wasm_dataset
- Section 1: Executive Summary of the Composite Indicators & Strategic Mandate
- High-Fidelity 20-Year Dislocation Event Study & Composite Regime Synthesis (2006–2026)
- Section 2: Scale-Invariant Log-Growth Trajectory & Dual-Phase Dislocation Corridors
- Section 3: 8-Dislocation Popperian Falsification & Peak-vs-Trough Regime Separation
- Section 4: Homotopic Phase-Time Superposed Epoch Analysis Across Dislocation Cycles
- Section 5: Institutional Capital Preservation & Early-Warning Lead Cushion Profile
- test_all_indicators_numerical_parity
- precompile_wasm_parquet_datasets

## God Nodes (most connected - your core abstractions)
1. `DashboardState` - 50 edges
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
- `Added` --references--> `test_all_tabs_legends_right_flushed()`  [INFERRED]
  README.md → tests/test_mahalanobis.py
- `Added` --references--> `test_tda_normalization_tabs_5_and_6()`  [INFERRED]
  README.md → tests/test_mahalanobis.py
- `Added` --references--> `sync_wasm_build_directories()`  [INFERRED]
  CHANGELOG.md → bubble_detector/ui/postprocess_wasm.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **AGVI Indicator and Feature Engineering Pipeline** — marketbubble_ddfv100_shiller_cape_ratio, marketbubble_ddfv100_payout_adjusted_cape, marketbubble_ddfv100_buffett_indicator, marketbubble_ddfv100_gsadf_psy_procedure [EXTRACTED 1.00]
- **Econometric and Mathematical Bubble Detection Framework** — marketbubble_ddfv100_gsadf_psy_procedure, marketbubble_ddfv100_tda_wavelet, marketbubble_ddfv100_lppls_model [EXTRACTED 1.00]
- **Implied Volatility Term Structure Components** — impliedvolatilitymetric_vix1d, impliedvolatilitymetric_vix_spot, impliedvolatilitymetric_vix3m, impliedvolatilitymetric_vix1y [EXTRACTED 1.00]
- **FINRA Margin Debt Metrics** — finra_margin_debt_tracker, finra_may_2026_nominal_value, finra_may_2026_mom_change, finra_may_2026_yoy_change [INFERRED 0.85]

## Communities (58 total, 11 thin omitted)

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
Cohesion: 0.04
Nodes (48): 1. Continuous Backward Compounding (Cliff Eradication), 1. Macro Valuation Anchors, 1. Prerequisites & Virtual Environment, 2. Run the High-Performance NiceGUI Application, 2. Signed Macro Mahalanobis Distance & Directional Projection, 2. Systemic Liquidity & Leverage, 3. Dynamic Portfolio Equity Sizing ($w_{\text{equity}}$), 3. Econometric Explosive Bubble Diagnostics (+40 more)

### Community 5 - "build_mahalanobis_fig"
Cohesion: 0.13
Nodes (21): normalize_tda_indicator(), build_composite_summary_fig(), build_econometric_fig(), build_leverage_fig(), build_macro_valuation_fig(), build_mahalanobis_fig(), _build_packaging_proxy_fig(), build_sector_health_fig() (+13 more)

### Community 6 - "StructuralBreakPredictor"
Cohesion: 0.07
Nodes (18): BubbleDetectorError, DataFetchError, ModelTrainingError, ValidationError, StructuralBreakPredictor, 10. Institutional Code Commentary, Packaging & Agent Navigation:, 1. System, Configuration & Date Horizons (`config.py` & `date_horizons.py`):, 3. Data Ingestion & Storage (`ingestor.py`): (+10 more)

### Community 8 - "PortfolioBacktestEngine"
Cohesion: 0.09
Nodes (6): BacktestResult, PortfolioBacktestEngine, compute_validation_summary_statistics(), generate_historical_validation_table(), test_backtest_fee_deduction(), test_exposure_rule_vs_naive_cape()

### Community 9 - "test_bsadf_rigor.py"
Cohesion: 0.11
Nodes (10): calculate_adf_stat(), compute_gsadf_gpt_decomposition(), compute_wild_bootstrap_critical_values(), test_adf_lag_selection_k0_vs_k1(), test_adf_stat_explosive_vs_stationary(), test_recursive_backward_supremum_grid(), test_wild_bootstrap_critical_value_bounds(), test_compute_gsadf_gpt_decomposition() (+2 more)

### Community 12 - "generate_deck.py"
Cohesion: 0.20
Nodes (3): create_presentation(), add_card(), add_metric_badge()

### Community 13 - "build_composite_validation_fig"
Cohesion: 0.24
Nodes (6): build_composite_validation_chart(), build_composite_validation_fig(), compute_composite_validation_metrics(), Added, Added, test_tab8_validation_6_color_bands_and_wealth_parity()

### Community 14 - "test_ui_ux_wasm_optimizations.py"
Cohesion: 0.11
Nodes (9): lttb_downsample(), test_keyboard_operability_and_aria_landmarks(), test_lttb_downsample_edge_cases(), test_lttb_downsample_extrema_retention(), test_lttb_downsample_monotonic_dates(), test_service_worker_file_validity(), test_wasm_build_packaging_html_size(), test_wasm_dependency_version_locking_and_resilience_bridge() (+1 more)

### Community 16 - "ui_theme.py"
Cohesion: 0.17
Nodes (6): toggle_theme(), get_plotly_template(), get_theme_css(), parse_hex_color(), relative_luminance(), test_theme_css_generation()

### Community 17 - "dashboard.py"
Cohesion: 0.12
Nodes (18): build_composite_summary_chart(), build_econometric_chart(), build_leverage_chart(), build_macro_valuation_chart(), build_mahalanobis_chart(), build_sector_health_chart(), build_sentiment_vol_chart(), build_tech_exuberance_chart() (+10 more)

### Community 18 - "lttb_downsample"
Cohesion: 0.29
Nodes (3): calculate_adf_stat(), takens_embedding(), 4. Quantitative Indicator Modules (`features/` & `features/utils.py`):

### Community 19 - "HighFidelityEventStudy_Executive_Report.md"
Cohesion: 0.06
Nodes (32): 1.1 The Core Institutional Challenge: Information Redundancy vs. Structural Blind Spots, 1.2 Our Ultimate Strategic Goal: Maximum Information Extraction & Asymmetric Capital Defense, 1.3 Overview of the Five Complementary Composite Summary Indicators, 1.4 High-Level Empirical Scorecard Across the 20-Year Horizon (2006–2026), 2.1 Executive Explanation of the Composite Indicator in This View, 2.2 High-Resolution 4K Visualization: Scale-Invariant Log-Growth (`4096 × 3072`), 2.3 Detailed Walkthrough of the Plot, Axes & Labeled Callouts, 3.1 Executive Explanation of the Composite Indicator in This View (+24 more)

### Community 20 - "HighFidelityEventStudy/README.md"
Cohesion: 0.06
Nodes (32): 1.1 The Core Institutional Challenge: Information Redundancy vs. Structural Blind Spots, 1.2 Our Ultimate Strategic Goal: Maximum Information Extraction & Asymmetric Capital Defense, 1.3 Overview of the Five Complementary Composite Summary Indicators, 1.4 High-Level Empirical Scorecard Across the 20-Year Horizon (2006–2026), 2.1 Executive Explanation of the Composite Indicator in This View, 2.2 High-Resolution 4K Visualization: Scale-Invariant Log-Growth (`4096 × 3072`), 2.3 Detailed Walkthrough of the Plot, Axes & Labeled Callouts, 3.1 Executive Explanation of the Composite Indicator in This View (+24 more)

### Community 21 - "pandas"
Cohesion: 0.18
Nodes (4): test_spy_backward_compounding_no_cliff(), test_vxo_vix_seam_continuity(), test_xlk_backward_compounding_no_cliff(), test_dual_conditions_logic()

### Community 22 - "calculate_contrast_ratio"
Cohesion: 0.23
Nodes (7): calculate_contrast_ratio(), is_wcag_aa_compliant(), 2. UI & Accessibility Engine (`ui_theme.py`):, test_ui_theme_alias_parity(), test_contrast_ratio_calculation(), test_wcag_aa_compliance(), Group 5: Strategic Recommendations (Group Confidence Score: 0.96)

### Community 23 - "generate_high_fidelity_plots.py"
Cohesion: 0.18
Nodes (8): get_palette(), main(), plot_1_scale_invariant_log_growth(), plot_2_popperian_regime_separation(), plot_3_homotopic_phase_time(), plot_4_dislocation_capital(), save_and_verify_4k(), style_axes_common()

### Community 24 - "FredETL"
Cohesion: 0.12
Nodes (8): FredETL, get_fred_data(), parse_fred_macro_series(), test_fred_publication_lags(), test_central_bank_balance_sheet_splicing_continuity(), test_global_liquidity_derived_metrics(), test_global_liquidity_schema_and_publication_lags(), test_authentic_fred_gdp_and_housing()

### Community 25 - "test_no_gaussian_bumps.py"
Cohesion: 0.16
Nodes (5): get_shiller_data(), parse_shiller_excel(), ShillerETL, test_shiller_provenance_schema_and_bounds(), test_authentic_shiller_provenance_workbook()

### Community 26 - "FinraETL"
Cohesion: 0.16
Nodes (6): FinraETL, parse_finra_margin_debt_series(), stage_all(), sync_parquet_to_json(), test_finra_margin_publication_lag(), test_authentic_finra_margin_debt()

### Community 27 - "compute_lppls_confidence_indicator"
Cohesion: 0.13
Nodes (6): calibrate_lppls_filimonov(), compute_lppls_confidence_indicator(), test_lppls_confidence_indicator_pipeline(), test_lppls_historical_bubble_detection(), test_lppls_parameter_recovery_synthetic(), test_lppls_sornette_filtering_bounds()

### Community 28 - "test_composite_summary_tab8.py"
Cohesion: 0.06
Nodes (14): build_band_polygon(), causal_ffill_clean(), causal_gram_schmidt(), causal_stationary_unit_variance(), CompositeSummaryEngine, compute_composite_validation_metrics(), compute_dislocation_fidelity_metrics(), compute_orthogonal_basis_and_summaries_numpy() (+6 more)

### Community 29 - "test_tda_wavelet_rigor.py"
Cohesion: 0.12
Nodes (12): _compute_morlet_wavelet_energy_and_entropy(), _compute_persistence_landscape_and_entropy(), _compute_rips_persistence_diagrams(), compute_tda_wavelet_complexity(), _takens_embedding(), test_compute_tda_wavelet_complexity(), test_predict_drawdown_probability(), test_bubenik_l2_norm_and_persistence_entropy() (+4 more)

### Community 30 - "precompile_wasm_parquet_datasets"
Cohesion: 0.25
Nodes (3): compute_tech_exuberance_metrics(), precompile_wasm_parquet_datasets(), ensure_synchronized_wasm_datasets()

### Community 31 - "compute_tech_exuberance_metrics"
Cohesion: 0.11
Nodes (14): compute_exuberance_spans(), [3.0.0] - 2026-09-03, [3.1.0] - 2026-10-05, [3.2.0] - 2026-11-03, [3.3.0] - 2026-11-05, [3.4.0] - 2026-11-05, [3.5.0] - 2026-11-05, Added (+6 more)

### Community 32 - "Detailed Slide Breakdown by Section & Group"
Cohesion: 0.25
Nodes (7): Detailed Slide Breakdown by Section & Group, Executive Presentation Deck Overview, Group 2: Supporting Evidence: Valuation, Econometrics & ML (Group Confidence Score: 0.93), Group 3: Sector Specific Application: Tech vs. Energy (Group Confidence Score: 0.91), Group 4: Implications for Systemic Stability (Group Confidence Score: 0.95), Verification Results, Walkthrough: Multidimensional Econometric & Quantitative Market Bubble Detection PowerPoint Deck

### Community 33 - "build_tech_exuberance_fig"
Cohesion: 0.14
Nodes (6): test_pane_tech_exuberance_in_dashboard_tabs(), test_precompile_wasm_parquet_datasets(), test_tech_exuberance_columns_in_core_wasm(), test_tech_exuberance_fig_structure_desktop(), test_tech_exuberance_fig_structure_mobile(), test_tech_exuberance_fig_structure_option_3()

### Community 34 - "polars"
Cohesion: 0.11
Nodes (6): IndicatorComputationError, compute_technical_indicators(), test_compute_technical_indicators(), test_margin_leverage_alias_parity(), test_options_volatility_alias_parity(), test_technical_alias_parity()

### Community 35 - "DataIngestor"
Cohesion: 0.07
Nodes (15): get_current_date(), get_dynamic_50yr_date_range(), get_dynamic_horizon_metadata(), DataIngestor, ingestor(), test_dashboard_state_horizon_switching(), test_dynamic_50yr_date_generator(), test_option_1_50yr_data_ingestion() (+7 more)

### Community 36 - "System Architecture and Operational Rules for Agents"
Cohesion: 0.40
Nodes (4): 1. Core Econometric & Statistical Rules, 2. Directory Layout & Key Modules, 3. Execution & Verification Rules, System Architecture and Operational Rules for Agents

### Community 37 - "build_dislocation_fidelity_fig"
Cohesion: 0.16
Nodes (9): build_dislocation_fidelity_chart(), build_band_polygon(), build_dislocation_fidelity_fig(), compute_dislocation_fidelity_metrics(), Added, 8. Composite Summary Indicators: Information-Maximizing Orthogonal Synthesis ($\mathcal{B}_{13}^{\perp}$), Added, test_tab8_dislocation_fidelity_dual_ui_parity() (+1 more)

### Community 38 - "get_vxo_data"
Cohesion: 0.17
Nodes (5): get_vxo_data(), parse_authentic_vxo_series(), VxoETL, test_vxo_authenticity_and_black_monday(), test_authentic_cboe_vxo_black_monday()

### Community 39 - "get_current_date"
Cohesion: 0.43
Nodes (3): get_current_date(), get_dynamic_50yr_date_range(), get_dynamic_horizon_metadata()

### Community 42 - "dashboard.py"
Cohesion: 0.13
Nodes (8): create_cta_banner(), create_ios_card(), create_app(), on_horizon_change(), refresh_dashboard(), run_diagnostics(), render_executive_summary_card(), render_horizon_explanatory_note()

### Community 43 - "test_wasm_pyodide_sandbox.py"
Cohesion: 0.05
Nodes (18): postprocess_wasm_content(), clean_bokeh_templates(), postprocess_wasm_html(), sync_wasm_build_directories(), Added, Changed, [v3.2.0] - 2026-11-03, test_no_synthetic_gaussian_bumps_in_data_code() (+10 more)

### Community 46 - "features/__init__.py"
Cohesion: 0.14
Nodes (8): compute_margin_leverage_metrics(), compute_macro_valuations(), compute_options_volatility_metrics(), test_compute_macro_valuations(), test_compute_margin_leverage_metrics(), test_compute_options_volatility_metrics(), test_full_pipeline_polars_integration(), processed_df()

### Community 48 - "Appendix: Architectural Principles & Methodological Justification (IP-Protected Technical Overview)"
Cohesion: 0.25
Nodes (7): A.1 Scope & Intellectual Property Boundary, A.2 Stage I: Eliminating Look-Ahead Bias & Non-Stationary Drift via Strictly Causal Standardization, A.3 Stage II: Eliminating Multicollinearity via Sequential Cross-Domain Orthogonalization, A.4 Stage III: Structural Mechanics of the Five Complementary Summary Engines, A.5 Stage IV: Directional Polarity Alignment & The Crash-Liquidation Damper, A.6 License & Confidentiality Attestation, Appendix: Architectural Principles & Methodological Justification (IP-Protected Technical Overview)

### Community 49 - "generate_wasm_dataset"
Cohesion: 0.25
Nodes (3): generate_wasm_dataset(), test_tda_wasm_parity(), test_wasm_loads_exact_parquet_dataset()

### Community 50 - "Section 1: Executive Summary of the Composite Indicators & Strategic Mandate"
Cohesion: 0.33
Nodes (5): 1.1 The Core Institutional Challenge: Information Redundancy vs. Structural Blind Spots, 1.2 Our Ultimate Strategic Goal: Maximum Information Extraction & Asymmetric Capital Defense, 1.3 Overview of the Five Complementary Composite Summary Indicators, 1.4 High-Level Empirical Scorecard Across the 20-Year Horizon (2006–2026), Section 1: Executive Summary of the Composite Indicators & Strategic Mandate

### Community 51 - "High-Fidelity 20-Year Dislocation Event Study & Composite Regime Synthesis (2006–2026)"
Cohesion: 0.40
Nodes (4): Document Changelog (SemVer), Executive Summary Abstract, High-Fidelity 20-Year Dislocation Event Study & Composite Regime Synthesis (2006–2026), Table of Contents

### Community 52 - "Section 2: Scale-Invariant Log-Growth Trajectory & Dual-Phase Dislocation Corridors"
Cohesion: 0.40
Nodes (4): 2.1 Executive Explanation of the Composite Indicator in This View, 2.2 High-Resolution 4K Visualization: Scale-Invariant Log-Growth (`4096 × 3072`), 2.3 Detailed Walkthrough of the Plot, Axes & Labeled Callouts, Section 2: Scale-Invariant Log-Growth Trajectory & Dual-Phase Dislocation Corridors

### Community 53 - "Section 3: 8-Dislocation Popperian Falsification & Peak-vs-Trough Regime Separation"
Cohesion: 0.40
Nodes (4): 3.1 Executive Explanation of the Composite Indicator in This View, 3.2 High-Resolution 4K Visualization: 8-Dislocation Popperian Matrix (`4096 × 3072`), 3.3 Detailed Walkthrough of the Plot, Axes & Labeled Callouts, Section 3: 8-Dislocation Popperian Falsification & Peak-vs-Trough Regime Separation

### Community 54 - "Section 4: Homotopic Phase-Time Superposed Epoch Analysis Across Dislocation Cycles"
Cohesion: 0.40
Nodes (4): 4.1 Executive Explanation of the Composite Indicator in This View, 4.2 High-Resolution 4K Visualization: Homotopic Phase-Time Analysis (`4096 × 3072`), 4.3 Detailed Walkthrough of the Plot, Axes & Labeled Callouts, Section 4: Homotopic Phase-Time Superposed Epoch Analysis Across Dislocation Cycles

### Community 55 - "Section 5: Institutional Capital Preservation & Early-Warning Lead Cushion Profile"
Cohesion: 0.40
Nodes (4): 5.1 Executive Explanation of the Composite Indicator in This View, 5.2 High-Resolution 4K Visualization: Dislocation Capital Preservation (`4096 × 3072`), 5.3 Detailed Walkthrough of the Plot, Axes & Labeled Callouts, Section 5: Institutional Capital Preservation & Early-Warning Lead Cushion Profile

## Knowledge Gaps
- **16 isolated node(s):** `market-bubble-detector`, `Polars DataFrame Integration`, `Margin Debt Growth Velocity`, `May 2026 Month-over-Month Change (+8.53%)`, `May 2026 Margin Debt Nominal Value ($1.416T)` (+11 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 552 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **11 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `build_dislocation_fidelity_chart()` connect `build_dislocation_fidelity_fig` to `dashboard.py`, `dashboard.py`, `test_composite_summary_tab8.py`, `test_tda_wavelet_rigor.py`?**
  _High betweenness centrality (0.046) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `DashboardState` (e.g. with `PortfolioBacktestEngine` and `DataIngestor`) actually correct?**
  _`DashboardState` has 11 INFERRED edges - model-reasoned connections that need verification._
- **What connects `market-bubble-detector`, `Polars DataFrame Integration`, `Margin Debt Growth Velocity` to the rest of the system?**
  _16 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Market Bubble Structural Analysis Report` be split into smaller, more focused modules?**
  _Cohesion score 0.07563025210084033 - nodes in this community are weakly interconnected._
- **Why does `DashboardState` connect `dashboard.py` to `MacroMahalanobisDetector`, `DataIngestor`, `build_dislocation_fidelity_fig`, `StructuralBreakPredictor`, `build_mahalanobis_fig`, `PortfolioBacktestEngine`, `dashboard.py`, `build_composite_validation_fig`, `pytest`, `generate_wasm_dataset`, `calculate_contrast_ratio`, `generate_high_fidelity_plots.py`, `test_all_indicators_numerical_parity`, `test_composite_summary_tab8.py`?**
  _High betweenness centrality (0.045) - this node is a cross-community bridge._
- **Should `MacroMahalanobisDetector` be split into smaller, more focused modules?**
  _Cohesion score 0.07878787878787878 - nodes in this community are weakly interconnected._
- **Should `deploy.yml` be split into smaller, more focused modules?**
  _Cohesion score 0.06881720430107527 - nodes in this community are weakly interconnected._