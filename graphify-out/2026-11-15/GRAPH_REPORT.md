# Graph Report - Merrill  (2026-11-15)

## Corpus Check
- 96 files · ~155,253 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 20 file(s) not represented in the graph (top: .parquet 10, .csv 6, (none) 2)

## Summary
- 1121 nodes · 2504 edges · 64 communities (51 shown, 13 thin omitted)
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 226 edges (avg confidence: 0.88)
- Token cost: 64,000 input · 3,600 output

## Graph Freshness
- Built from commit: `dfd94827`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Market Bubble Structural Analysis Report
- test_mahalanobis.py
- deploy.yml
- Implied Volatility Metrics Table (July 2026)
- 📋 Changelog
- build_mahalanobis_fig
- StructuralBreakPredictor
- market-bubble-detector
- .load_data
- numpy
- config.py
- generate_deck.py
- polars
- test_ui_ux_wasm_optimizations.py
- calculate_contrast_ratio
- test_full_indicator_parity.py
- dashboard.py
- HighFidelityEventStudy_Executive_Report.md
- HighFidelityEventStudy/README.md
- DashboardState
- test_all_indicators_numerical_parity
- generate_high_fidelity_plots.py
- FredETL
- test_no_gaussian_bumps.py
- FinraETL
- compute_lppls_confidence_indicator
- composite_summary.py
- test_tda_wavelet_rigor.py
- test_cross_horizon_date_invariance_and_zero_nulls
- postprocess_wasm_content
- build_tech_exuberance_fig
- polars
- DataIngestor
- System Architecture and Operational Rules for Agents
- 📊 8 Interactive Dashboard Modules
- get_vxo_data
- panel_dashboard.py
- sw.js
- test_date_horizons.py
- test_wasm_pyodide_sandbox.py
- compute_margin_leverage_metrics
- generate_wasm_dataset
- Appendix: Architectural Principles & Methodological Justification (IP-Protected Technical Overview)
- test_composite_summary_tab8.py
- Section 1: Executive Summary of the Composite Indicators & Strategic Mandate
- High-Fidelity 20-Year Dislocation Event Study & Composite Regime Synthesis (2006–2026)
- Section 2: Scale-Invariant Log-Growth Trajectory & Dual-Phase Dislocation Corridors
- Section 3: 8-Dislocation Popperian Falsification & Peak-vs-Trough Regime Separation
- Section 4: Homotopic Phase-Time Superposed Epoch Analysis Across Dislocation Cycles
- Section 5: Institutional Capital Preservation & Early-Warning Lead Cushion Profile
- compute_validation_summary_statistics
- 📉 Multidimensional Market Bubble Detector & Structural Break System
- 🔬 Mathematical Formulations
- 💻 Local Setup & Execution Guide
- features/__init__.py
- [v2.1.0] - 2026-09-02

## God Nodes (most connected - your core abstractions)
1. `DashboardState` - 51 edges
2. `MacroMahalanobisDetector` - 37 edges
3. `DataIngestor` - 31 edges
4. `generate_wasm_dataset()` - 31 edges
5. `StructuralBreakPredictor` - 30 edges
6. `precompile_wasm_parquet_datasets()` - 24 edges
7. `test_all_7_tabs_plot_trace_parity()` - 24 edges
8. `compute_tda_wavelet_complexity()` - 23 edges
9. `compute_gsadf_gpt_decomposition()` - 22 edges
10. `build_tech_exuberance_fig()` - 21 edges

## Surprising Connections (you probably didn't know these)
- `3. Data Ingestion & Storage (`ingestor.py`):` --references--> `DataIngestor`  [INFERRED]
  ImplementationOverview_DDFv100.md → bubble_detector/data/ingestor.py
- `Fixed` --references--> `DataIngestor`  [INFERRED]
  README.md → bubble_detector/data/ingestor.py
- `Changed` --references--> `calculate_adf_stat()`  [INFERRED]
  CHANGELOG.md → bubble_detector/features/utils.py
- `4. Quantitative Indicator Modules (`features/` & `features/utils.py`):` --references--> `takens_embedding()`  [INFERRED]
  ImplementationOverview_DDFv100.md → bubble_detector/features/utils.py
- `Added` --references--> `compute_exuberance_spans()`  [INFERRED]
  CHANGELOG.md → bubble_detector/features/tech_exuberance.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **AGVI Indicator and Feature Engineering Pipeline** — marketbubble_ddfv100_shiller_cape_ratio, marketbubble_ddfv100_payout_adjusted_cape, marketbubble_ddfv100_buffett_indicator, marketbubble_ddfv100_gsadf_psy_procedure [EXTRACTED 1.00]
- **Econometric and Mathematical Bubble Detection Framework** — marketbubble_ddfv100_gsadf_psy_procedure, marketbubble_ddfv100_tda_wavelet, marketbubble_ddfv100_lppls_model [EXTRACTED 1.00]
- **Implied Volatility Term Structure Components** — impliedvolatilitymetric_vix1d, impliedvolatilitymetric_vix_spot, impliedvolatilitymetric_vix3m, impliedvolatilitymetric_vix1y [EXTRACTED 1.00]
- **FINRA Margin Debt Metrics** — finra_margin_debt_tracker, finra_may_2026_nominal_value, finra_may_2026_mom_change, finra_may_2026_yoy_change [INFERRED 0.85]

## Communities (64 total, 13 thin omitted)

### Community 0 - "Market Bubble Structural Analysis Report"
Cohesion: 0.08
Nodes (35): NiceGUI Layout & Plotly Dashboard, Data Ingestion (DataIngestor), AGVI Implementation Plan Document, Feature Engineering Pipeline, XGBoost Model Training & Walk-Forward CV, AGVI Technical Specification Document, NiceGUI Dashboard UI, Polars DataFrame Integration (+27 more)

### Community 1 - "test_mahalanobis.py"
Cohesion: 0.07
Nodes (15): fast_ledoit_wolf_cov(), MacroMahalanobisDetector, test_drawdown_probability_not_in_covariance(), test_p_cape_elimination(), mock_indicators_df(), test_anomaly_driver_attribution(), test_dynamic_exposure_bounds_and_monotonicity(), test_mahalanobis_distance_non_negative() (+7 more)

### Community 2 - "deploy.yml"
Cohesion: 0.07
Nodes (30): runs-on, steps, concurrency, cancel-in-progress, group, environment, needs, runs-on (+22 more)

### Community 3 - "Implied Volatility Metrics Table (July 2026)"
Cohesion: 0.60
Nodes (6): Implied Volatility Metrics Table (July 2026), Implied Volatility Term Structure (Upward Sloping), VIX1D (8.73 - 11.61): Extreme near-term calm, VIX1Y (~23.00): Elevated long-term risk premium, VIX3M (~19.00): Anticipation of future turbulence, VIX Spot (15.57 - 17.16): Low baseline fear

### Community 4 - "📋 Changelog"
Cohesion: 0.12
Nodes (16): Added, Added, Added, Added, Added, Added, Added, 📋 Changelog (+8 more)

### Community 5 - "build_mahalanobis_fig"
Cohesion: 0.15
Nodes (20): build_band_polygon(), build_composite_summary_fig(), build_composite_validation_fig(), build_dislocation_fidelity_fig(), build_econometric_fig(), build_leverage_fig(), build_macro_valuation_fig(), build_mahalanobis_fig() (+12 more)

### Community 6 - "StructuralBreakPredictor"
Cohesion: 0.05
Nodes (20): BubbleDetectorError, DataFetchError, IndicatorComputationError, ModelTrainingError, ValidationError, StructuralBreakPredictor, 10. Institutional Code Commentary, Packaging & Agent Navigation:, 1. System, Configuration & Date Horizons (`config.py` & `date_horizons.py`): (+12 more)

### Community 8 - ".load_data"
Cohesion: 0.17
Nodes (4): PortfolioBacktestEngine, test_backtest_fee_deduction(), test_exposure_rule_vs_naive_cape(), test_dashboard_state_horizon_switching()

### Community 9 - "numpy"
Cohesion: 0.10
Nodes (11): _batch_adf_from_log_windows(), compute_gsadf_gpt_decomposition(), _in_window_coint_adf(), _rolling_adf_vectorized(), test_adf_lag_selection_k0_vs_k1(), test_adf_stat_explosive_vs_stationary(), test_recursive_backward_supremum_grid(), test_wild_bootstrap_critical_value_bounds() (+3 more)

### Community 12 - "generate_deck.py"
Cohesion: 0.20
Nodes (3): create_presentation(), add_card(), add_metric_badge()

### Community 13 - "polars"
Cohesion: 0.10
Nodes (8): compute_exuberance_spans(), compute_tech_exuberance_metrics(), precompile_wasm_parquet_datasets(), ensure_synchronized_wasm_datasets(), market_simulation_df(), test_strictly_causal_one_day_execution_lag(), test_compute_exuberance_spans(), test_dual_conditions_logic()

### Community 14 - "test_ui_ux_wasm_optimizations.py"
Cohesion: 0.11
Nodes (9): lttb_downsample(), test_keyboard_operability_and_aria_landmarks(), test_lttb_downsample_edge_cases(), test_lttb_downsample_extrema_retention(), test_lttb_downsample_monotonic_dates(), test_responsive_legend_layout_logic(), test_service_worker_file_validity(), test_wasm_build_packaging_html_size() (+1 more)

### Community 16 - "calculate_contrast_ratio"
Cohesion: 0.08
Nodes (21): toggle_theme(), calculate_contrast_ratio(), get_plotly_template(), get_theme_css(), is_wcag_aa_compliant(), parse_hex_color(), relative_luminance(), 2. UI & Accessibility Engine (`ui_theme.py`): (+13 more)

### Community 17 - "test_full_indicator_parity.py"
Cohesion: 0.16
Nodes (12): build_composite_summary_chart(), build_composite_validation_chart(), build_econometric_chart(), build_leverage_chart(), build_macro_valuation_chart(), build_sector_health_chart(), build_sentiment_vol_chart(), build_tech_exuberance_chart() (+4 more)

### Community 18 - "dashboard.py"
Cohesion: 0.15
Nodes (8): create_cta_banner(), create_ios_card(), create_app(), on_horizon_change(), refresh_dashboard(), run_diagnostics(), render_executive_summary_card(), render_horizon_explanatory_note()

### Community 19 - "HighFidelityEventStudy_Executive_Report.md"
Cohesion: 0.06
Nodes (32): 1.1 The Core Institutional Challenge: Information Redundancy vs. Structural Blind Spots, 1.2 Our Ultimate Strategic Goal: Maximum Information Extraction & Asymmetric Capital Defense, 1.3 Overview of the Five Complementary Composite Summary Indicators, 1.4 High-Level Empirical Scorecard Across the 20-Year Horizon (2006–2026), 2.1 Executive Explanation of the Composite Indicator in This View, 2.2 High-Resolution 4K Visualization: Scale-Invariant Log-Growth (`4096 × 3072`), 2.3 Detailed Walkthrough of the Plot, Axes & Labeled Callouts, 3.1 Executive Explanation of the Composite Indicator in This View (+24 more)

### Community 20 - "HighFidelityEventStudy/README.md"
Cohesion: 0.06
Nodes (32): 1.1 The Core Institutional Challenge: Information Redundancy vs. Structural Blind Spots, 1.2 Our Ultimate Strategic Goal: Maximum Information Extraction & Asymmetric Capital Defense, 1.3 Overview of the Five Complementary Composite Summary Indicators, 1.4 High-Level Empirical Scorecard Across the 20-Year Horizon (2006–2026), 2.1 Executive Explanation of the Composite Indicator in This View, 2.2 High-Resolution 4K Visualization: Scale-Invariant Log-Growth (`4096 × 3072`), 2.3 Detailed Walkthrough of the Plot, Axes & Labeled Callouts, 3.1 Executive Explanation of the Composite Indicator in This View (+24 more)

### Community 21 - "DashboardState"
Cohesion: 0.18
Nodes (7): build_mahalanobis_chart(), DashboardState, test_full_system_integration(), test_tab6_all_traces_finite_and_bounded(), test_tab6_figure_traces_and_right_flushed_legend(), test_tda_normalization_tabs_5_and_6(), test_dashboard_state_theme_toggle()

### Community 23 - "generate_high_fidelity_plots.py"
Cohesion: 0.17
Nodes (8): get_palette(), main(), plot_1_scale_invariant_log_growth(), plot_2_popperian_regime_separation(), plot_3_homotopic_phase_time(), plot_4_dislocation_capital(), save_and_verify_4k(), style_axes_common()

### Community 24 - "FredETL"
Cohesion: 0.12
Nodes (8): FredETL, get_fred_data(), parse_fred_macro_series(), test_fred_publication_lags(), test_central_bank_balance_sheet_splicing_continuity(), test_global_liquidity_derived_metrics(), test_global_liquidity_schema_and_publication_lags(), test_authentic_fred_gdp_and_housing()

### Community 25 - "test_no_gaussian_bumps.py"
Cohesion: 0.20
Nodes (4): parse_shiller_excel(), ShillerETL, test_shiller_provenance_schema_and_bounds(), test_authentic_shiller_provenance_workbook()

### Community 26 - "FinraETL"
Cohesion: 0.15
Nodes (6): FinraETL, get_finra_margin_debt(), parse_finra_margin_debt_series(), stage_all(), test_finra_margin_publication_lag(), test_authentic_finra_margin_debt()

### Community 27 - "compute_lppls_confidence_indicator"
Cohesion: 0.12
Nodes (7): calibrate_lppls_filimonov(), compute_lppls_confidence_indicator(), _get_lppls_grid(), test_lppls_confidence_indicator_pipeline(), test_lppls_historical_bubble_detection(), test_lppls_parameter_recovery_synthetic(), test_lppls_sornette_filtering_bounds()

### Community 28 - "composite_summary.py"
Cohesion: 0.07
Nodes (14): build_band_polygon(), causal_ffill_clean(), causal_gram_schmidt(), causal_stationary_unit_variance(), CompositeSummaryEngine, compute_composite_validation_metrics(), compute_dislocation_fidelity_metrics(), compute_orthogonal_basis_and_summaries_numpy() (+6 more)

### Community 29 - "test_tda_wavelet_rigor.py"
Cohesion: 0.12
Nodes (11): _compute_morlet_wavelet_energy_and_entropy(), _compute_persistence_landscape_and_entropy(), _compute_rips_persistence_diagrams(), compute_tda_wavelet_complexity(), _get_morlet_toeplitz_matrices(), _takens_embedding(), test_bubenik_l2_norm_and_persistence_entropy(), test_morlet_wavelet_scaleogram_and_spectral_entropy() (+3 more)

### Community 31 - "postprocess_wasm_content"
Cohesion: 0.09
Nodes (12): postprocess_wasm_content(), clean_bokeh_templates(), postprocess_wasm_html(), sync_wasm_build_directories(), [3.2.0] - 2026-11-03, Added, Changed, build_pdf() (+4 more)

### Community 33 - "build_tech_exuberance_fig"
Cohesion: 0.13
Nodes (8): build_tech_exuberance_fig(), normalize_tda_indicator(), test_pane_tech_exuberance_in_dashboard_tabs(), test_precompile_wasm_parquet_datasets(), test_tech_exuberance_columns_in_core_wasm(), test_tech_exuberance_fig_structure_desktop(), test_tech_exuberance_fig_structure_mobile(), test_tech_exuberance_fig_structure_option_3()

### Community 34 - "polars"
Cohesion: 0.12
Nodes (6): compute_options_volatility_metrics(), compute_technical_indicators(), test_compute_options_volatility_metrics(), test_compute_technical_indicators(), test_options_volatility_alias_parity(), test_technical_alias_parity()

### Community 35 - "DataIngestor"
Cohesion: 0.07
Nodes (13): DataIngestor, ingestor(), test_option_1_50yr_data_ingestion(), test_option_2_modern_data_ingestion(), test_option_3_20yr_data_ingestion(), sample_df(), ingestor(), test_fetch_market_data_schema_and_downcasting() (+5 more)

### Community 36 - "System Architecture and Operational Rules for Agents"
Cohesion: 0.40
Nodes (4): 1. Core Econometric & Statistical Rules, 2. Directory Layout & Key Modules, 3. Execution & Verification Rules, System Architecture and Operational Rules for Agents

### Community 37 - "📊 8 Interactive Dashboard Modules"
Cohesion: 0.22
Nodes (9): 1. Macro Valuation Anchors, 2. Systemic Liquidity & Leverage, 3. Econometric Explosive Bubble Diagnostics, 4. Options Sentiment & Behavioral Tracking, 5. Sector Vulnerability & Topological Dynamics, 6. Signed Macro Mahalanobis Distance & Dynamic Equity Exposure, 7. Tech Exuberance Score: Macro Decoupling vs Statistical Singularity, 8. Composite Summary Indicators: Information-Maximizing Orthogonal Synthesis ($\mathcal{B}_{13}^{\perp}$) (+1 more)

### Community 38 - "get_vxo_data"
Cohesion: 0.14
Nodes (5): get_vxo_data(), parse_authentic_vxo_series(), VxoETL, test_vxo_authenticity_and_black_monday(), test_authentic_cboe_vxo_black_monday()

### Community 39 - "panel_dashboard.py"
Cohesion: 0.15
Nodes (6): compute_composite_validation_metrics(), compute_dislocation_fidelity_metrics(), get_current_date(), get_dynamic_50yr_date_range(), get_dynamic_horizon_metadata(), precompile_wasm_parquet_datasets()

### Community 42 - "test_date_horizons.py"
Cohesion: 0.17
Nodes (6): clamp_to_trading_day(), get_current_date(), get_dynamic_50yr_date_range(), get_dynamic_horizon_metadata(), test_dynamic_50yr_date_generator(), test_weekend_and_offline_clamping()

### Community 43 - "test_wasm_pyodide_sandbox.py"
Cohesion: 0.07
Nodes (12): _serialize_df_to_json_dict(), sync_parquet_to_json(), apply_postprocessing(), test_date_horizon_selector_robust_against_year_shift(), test_dist_index_html_on_disk(), test_dist_index_html_postprocessing_idempotence(), test_json_datasets_staging(), test_template_and_cards_reconstruction() (+4 more)

### Community 46 - "compute_margin_leverage_metrics"
Cohesion: 0.11
Nodes (7): compute_margin_leverage_metrics(), compute_macro_valuations(), test_compute_macro_valuations(), test_compute_margin_leverage_metrics(), test_full_pipeline_polars_integration(), processed_df(), test_margin_leverage_alias_parity()

### Community 47 - "generate_wasm_dataset"
Cohesion: 0.18
Nodes (5): generate_wasm_dataset(), test_compute_gsadf_gpt_decomposition(), test_compute_tda_wavelet_complexity(), test_tda_wasm_parity(), test_wasm_loads_exact_parquet_dataset()

### Community 48 - "Appendix: Architectural Principles & Methodological Justification (IP-Protected Technical Overview)"
Cohesion: 0.25
Nodes (7): A.1 Scope & Intellectual Property Boundary, A.2 Stage I: Eliminating Look-Ahead Bias & Non-Stationary Drift via Strictly Causal Standardization, A.3 Stage II: Eliminating Multicollinearity via Sequential Cross-Domain Orthogonalization, A.4 Stage III: Structural Mechanics of the Five Complementary Summary Engines, A.5 Stage IV: Directional Polarity Alignment & The Crash-Liquidation Damper, A.6 License & Confidentiality Attestation, Appendix: Architectural Principles & Methodological Justification (IP-Protected Technical Overview)

### Community 49 - "test_composite_summary_tab8.py"
Cohesion: 0.16
Nodes (6): build_dislocation_fidelity_chart(), test_five_summary_indicators_bounds_and_crash_separation_20yr(), test_tab8_dislocation_fidelity_dual_ui_parity(), test_tab8_dual_ui_parity_across_all_horizons(), test_tab8_validation_6_color_bands_and_wealth_parity(), test_dislocation_fidelity_chart_light_dark_contrast()

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

### Community 56 - "compute_validation_summary_statistics"
Cohesion: 0.06
Nodes (18): BacktestResult, _compute_empirical_false_alarm_rate(), compute_validation_summary_statistics(), generate_historical_validation_table(), _date_seeded_normals(), [3.0.0] - 2026-09-03, [3.1.0] - 2026-10-05, [3.3.0] - 2026-11-05 (+10 more)

### Community 60 - "📉 Multidimensional Market Bubble Detector & Structural Break System"
Cohesion: 0.25
Nodes (7): Benchmark Comparison (50-Year Multi-Decade Horizon), 📅 Dynamic 50-Year Multi-Horizon Date Engine, 🎯 Falsifiable Historical Peak Validation Event Study, 📈 Institutional Cost-Inclusive Portfolio Backtest, 📜 License, 🌟 Live Interactive WebAssembly Dashboard, 📉 Multidimensional Market Bubble Detector & Structural Break System

### Community 61 - "🔬 Mathematical Formulations"
Cohesion: 0.25
Nodes (8): 1. Continuous Backward Compounding (Cliff Eradication), 2. Signed Macro Mahalanobis Distance & Directional Projection, 3. Dynamic Portfolio Equity Sizing ($w_{\text{equity}}$), 4. Canonical PSY Recursive Right-Tailed Unit Root Testing (GSADF / BSADF), 5. Topological Data Analysis (TDA) & Wavelet Spectral Entropy, 6. Log-Periodic Power Law Singularity (LPPLS) Subordination Model, 7. Global Liquidity Index & Dual-Condition Conjoint Exuberance, 🔬 Mathematical Formulations

### Community 63 - "💻 Local Setup & Execution Guide"
Cohesion: 0.29
Nodes (7): 1. Prerequisites & Virtual Environment, 2. Run the High-Performance NiceGUI Application, 3. Run the Local HoloViz Panel Dashboard, 4. Build and Run Client-Side WebAssembly (Pyodide), 5. Run the Automated Test Suite, 6. Synchronize Repository Knowledge Graph, 💻 Local Setup & Execution Guide

### Community 65 - "features/__init__.py"
Cohesion: 0.17
Nodes (6): compute_wild_bootstrap_critical_values(), calculate_adf_stat(), normalize_tda_indicator(), takens_embedding(), Added, test_ripser_persistence_landscapes_causal()

### Community 66 - "[v2.1.0] - 2026-09-02"
Cohesion: 0.67
Nodes (3): Added, Fixed, [v2.1.0] - 2026-09-02

## Knowledge Gaps
- **16 isolated node(s):** `market-bubble-detector`, `Polars DataFrame Integration`, `Margin Debt Growth Velocity`, `May 2026 Month-over-Month Change (+8.53%)`, `May 2026 Margin Debt Nominal Value ($1.416T)` (+11 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 574 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **13 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `DataIngestor` connect `DataIngestor` to `features/__init__.py`, `[v2.1.0] - 2026-09-02`, `test_mahalanobis.py`, `StructuralBreakPredictor`, `panel_dashboard.py`, `.load_data`, `numpy`, `test_date_horizons.py`, `config.py`, `polars`, `compute_margin_leverage_metrics`, `generate_wasm_dataset`, `dashboard.py`, `DashboardState`, `FinraETL`?**
  _High betweenness centrality (0.044) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `DashboardState` (e.g. with `PortfolioBacktestEngine` and `DataIngestor`) actually correct?**
  _`DashboardState` has 11 INFERRED edges - model-reasoned connections that need verification._
- **What connects `market-bubble-detector`, `Polars DataFrame Integration`, `Margin Debt Growth Velocity` to the rest of the system?**
  _16 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Market Bubble Structural Analysis Report` be split into smaller, more focused modules?**
  _Cohesion score 0.07563025210084033 - nodes in this community are weakly interconnected._
- **Why does `DashboardState` connect `DashboardState` to `test_mahalanobis.py`, `DataIngestor`, `StructuralBreakPredictor`, `.load_data`, `test_date_horizons.py`, `polars`, `generate_wasm_dataset`, `calculate_contrast_ratio`, `test_full_indicator_parity.py`, `dashboard.py`, `test_composite_summary_tab8.py`, `test_all_indicators_numerical_parity`, `generate_high_fidelity_plots.py`, `composite_summary.py`?**
  _High betweenness centrality (0.039) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `MacroMahalanobisDetector` (e.g. with `DashboardState` and `Fixed & Enhanced (Red Team Remediation Release `RT-CRIT-01` – `RT-LOW-28`)`) actually correct?**
  _`MacroMahalanobisDetector` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `test_mahalanobis.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06848357791754019 - nodes in this community are weakly interconnected._