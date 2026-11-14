# Graph Report - Merrill  (2026-11-14)

## Corpus Check
- 96 files · ~150,432 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 19 file(s) not represented in the graph (top: .parquet 9, .csv 6, (none) 2)

## Summary
- 1075 nodes · 2432 edges · 67 communities (55 shown, 12 thin omitted)
- Extraction: 92% EXTRACTED · 8% INFERRED · 0% AMBIGUOUS · INFERRED: 189 edges (avg confidence: 0.88)
- Token cost: 64,000 input · 3,600 output

## Graph Freshness
- Built from commit: `4d407b2d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Market Bubble Structural Analysis Report
- MacroMahalanobisDetector
- deploy.yml
- Implied Volatility Metrics Table (July 2026)
- 📋 Changelog
- build_mahalanobis_fig
- StructuralBreakPredictor
- market-bubble-detector
- PortfolioBacktestEngine
- test_bsadf_rigor.py
- config.py
- generate_deck.py
- features/__init__.py
- test_ui_ux_wasm_optimizations.py
- ui_theme.py
- dashboard.py
- Overview of Completed Implementation: Multidimensional Market Bubble Detector
- HighFidelityEventStudy_Executive_Report.md
- HighFidelityEventStudy/README.md
- pandas
- calculate_contrast_ratio
- generate_high_fidelity_plots.py
- FredETL
- test_no_gaussian_bumps.py
- FinraETL
- compute_lppls_confidence_indicator
- composite_summary.py
- test_tda_wavelet_rigor.py
- precompile_wasm_parquet_datasets
- postprocess_wasm.py
- Detailed Slide Breakdown by Section & Group
- build_tech_exuberance_fig
- polars
- DataIngestor
- System Architecture and Operational Rules for Agents
- 📊 8 Interactive Dashboard Modules
- get_vxo_data
- panel_dashboard.py
- sw.js
- CompositeSummaryEngine
- bubble_detector/__init__.py
- test_wasm_pyodide_sandbox.py
- features/__init__.py
- numpy
- Appendix: Architectural Principles & Methodological Justification (IP-Protected Technical Overview)
- test_composite_summary_tab8.py
- Section 1: Executive Summary of the Composite Indicators & Strategic Mandate
- High-Fidelity 20-Year Dislocation Event Study & Composite Regime Synthesis (2006–2026)
- Section 2: Scale-Invariant Log-Growth Trajectory & Dual-Phase Dislocation Corridors
- Section 3: 8-Dislocation Popperian Falsification & Peak-vs-Trough Regime Separation
- Section 4: Homotopic Phase-Time Superposed Epoch Analysis Across Dislocation Cycles
- Section 5: Institutional Capital Preservation & Early-Warning Lead Cushion Profile
- validation_table.py
- BubbleDetectorError
- test_ui_theme.py
- stage_provenance.py
- 📉 Multidimensional Market Bubble Detector & Structural Break System
- 🔬 Mathematical Formulations
- 💻 Local Setup & Execution Guide
- test_leakage_elimination.py
- test_psy_ripser_integrity.py
- [v2.1.0] - 2026-09-02

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
- `5. Machine Learning Model (`structural_breaks.py`):` --references--> `StructuralBreakPredictor`  [INFERRED]
  ImplementationOverview_DDFv100.md → bubble_detector/models/structural_breaks.py
- `Added` --references--> `compute_exuberance_spans()`  [INFERRED]
  CHANGELOG.md → bubble_detector/features/tech_exuberance.py
- `Added` --references--> `test_all_tabs_legends_right_flushed()`  [INFERRED]
  README.md → tests/test_mahalanobis.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **AGVI Indicator and Feature Engineering Pipeline** — marketbubble_ddfv100_shiller_cape_ratio, marketbubble_ddfv100_payout_adjusted_cape, marketbubble_ddfv100_buffett_indicator, marketbubble_ddfv100_gsadf_psy_procedure [EXTRACTED 1.00]
- **Econometric and Mathematical Bubble Detection Framework** — marketbubble_ddfv100_gsadf_psy_procedure, marketbubble_ddfv100_tda_wavelet, marketbubble_ddfv100_lppls_model [EXTRACTED 1.00]
- **Implied Volatility Term Structure Components** — impliedvolatilitymetric_vix1d, impliedvolatilitymetric_vix_spot, impliedvolatilitymetric_vix3m, impliedvolatilitymetric_vix1y [EXTRACTED 1.00]
- **FINRA Margin Debt Metrics** — finra_margin_debt_tracker, finra_may_2026_nominal_value, finra_may_2026_mom_change, finra_may_2026_yoy_change [INFERRED 0.85]

## Communities (67 total, 12 thin omitted)

### Community 0 - "Market Bubble Structural Analysis Report"
Cohesion: 0.08
Nodes (35): NiceGUI Layout & Plotly Dashboard, Data Ingestion (DataIngestor), AGVI Implementation Plan Document, Feature Engineering Pipeline, XGBoost Model Training & Walk-Forward CV, AGVI Technical Specification Document, NiceGUI Dashboard UI, Polars DataFrame Integration (+27 more)

### Community 1 - "MacroMahalanobisDetector"
Cohesion: 0.13
Nodes (7): MacroMahalanobisDetector, test_anomaly_driver_attribution(), test_dynamic_exposure_bounds_and_monotonicity(), test_mahalanobis_distance_non_negative(), test_mahalanobis_no_early_rank_singularity(), test_regime_probability_bounds(), test_stationary_features_shape_and_values()

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
Cohesion: 0.13
Nodes (6): ModelTrainingError, StructuralBreakPredictor, test_predict_drawdown_probability(), test_structural_break_predictor_walk_forward(), test_structural_breaks_embargo_no_lookahead(), test_reliability_diagram_monotonicity()

### Community 8 - "PortfolioBacktestEngine"
Cohesion: 0.13
Nodes (4): BacktestResult, PortfolioBacktestEngine, test_backtest_fee_deduction(), test_exposure_rule_vs_naive_cape()

### Community 9 - "test_bsadf_rigor.py"
Cohesion: 0.16
Nodes (6): calculate_adf_stat(), compute_wild_bootstrap_critical_values(), test_adf_lag_selection_k0_vs_k1(), test_adf_stat_explosive_vs_stationary(), test_recursive_backward_supremum_grid(), test_wild_bootstrap_critical_value_bounds()

### Community 11 - "config.py"
Cohesion: 0.13
Nodes (5): get_current_date(), get_dynamic_50yr_date_range(), get_dynamic_horizon_metadata(), ingestor(), test_dynamic_50yr_date_generator()

### Community 12 - "generate_deck.py"
Cohesion: 0.20
Nodes (3): create_presentation(), add_card(), add_metric_badge()

### Community 13 - "features/__init__.py"
Cohesion: 0.20
Nodes (4): compute_exuberance_spans(), compute_tech_exuberance_metrics(), test_compute_exuberance_spans(), test_dual_conditions_logic()

### Community 14 - "test_ui_ux_wasm_optimizations.py"
Cohesion: 0.09
Nodes (11): calculate_adf_stat(), lttb_downsample(), normalize_tda_indicator(), test_keyboard_operability_and_aria_landmarks(), test_lttb_downsample_edge_cases(), test_lttb_downsample_extrema_retention(), test_lttb_downsample_monotonic_dates(), test_responsive_legend_layout_logic() (+3 more)

### Community 16 - "ui_theme.py"
Cohesion: 0.24
Nodes (3): get_plotly_template(), parse_hex_color(), relative_luminance()

### Community 17 - "dashboard.py"
Cohesion: 0.06
Nodes (35): create_cta_banner(), create_ios_card(), build_composite_summary_chart(), build_composite_validation_chart(), build_dislocation_fidelity_chart(), build_econometric_chart(), build_leverage_chart(), build_macro_valuation_chart() (+27 more)

### Community 18 - "Overview of Completed Implementation: Multidimensional Market Bubble Detector"
Cohesion: 0.17
Nodes (10): takens_embedding(), 10. Institutional Code Commentary, Packaging & Agent Navigation:, 3. Data Ingestion & Storage (`ingestor.py`):, 4. Quantitative Indicator Modules (`features/` & `features/utils.py`):, 5. Machine Learning Model (`structural_breaks.py`):, 6. Macro Mahalanobis Distance Engine (`regime_mahalanobis.py`):, 7. Interactive Dashboards & Dual-Runtime Architecture:, 8. Data Red Team Remediation & Institutional Hardening: (+2 more)

### Community 19 - "HighFidelityEventStudy_Executive_Report.md"
Cohesion: 0.06
Nodes (32): 1.1 The Core Institutional Challenge: Information Redundancy vs. Structural Blind Spots, 1.2 Our Ultimate Strategic Goal: Maximum Information Extraction & Asymmetric Capital Defense, 1.3 Overview of the Five Complementary Composite Summary Indicators, 1.4 High-Level Empirical Scorecard Across the 20-Year Horizon (2006–2026), 2.1 Executive Explanation of the Composite Indicator in This View, 2.2 High-Resolution 4K Visualization: Scale-Invariant Log-Growth (`4096 × 3072`), 2.3 Detailed Walkthrough of the Plot, Axes & Labeled Callouts, 3.1 Executive Explanation of the Composite Indicator in This View (+24 more)

### Community 20 - "HighFidelityEventStudy/README.md"
Cohesion: 0.06
Nodes (32): 1.1 The Core Institutional Challenge: Information Redundancy vs. Structural Blind Spots, 1.2 Our Ultimate Strategic Goal: Maximum Information Extraction & Asymmetric Capital Defense, 1.3 Overview of the Five Complementary Composite Summary Indicators, 1.4 High-Level Empirical Scorecard Across the 20-Year Horizon (2006–2026), 2.1 Executive Explanation of the Composite Indicator in This View, 2.2 High-Resolution 4K Visualization: Scale-Invariant Log-Growth (`4096 × 3072`), 2.3 Detailed Walkthrough of the Plot, Axes & Labeled Callouts, 3.1 Executive Explanation of the Composite Indicator in This View (+24 more)

### Community 21 - "pandas"
Cohesion: 0.25
Nodes (3): test_spy_backward_compounding_no_cliff(), test_vxo_vix_seam_continuity(), test_xlk_backward_compounding_no_cliff()

### Community 22 - "calculate_contrast_ratio"
Cohesion: 0.24
Nodes (6): calculate_contrast_ratio(), is_wcag_aa_compliant(), 2. UI & Accessibility Engine (`ui_theme.py`):, test_ui_theme_alias_parity(), test_contrast_ratio_calculation(), test_wcag_aa_color_contrast_tokens()

### Community 23 - "generate_high_fidelity_plots.py"
Cohesion: 0.13
Nodes (10): build_pdf(), get_palette(), main(), plot_1_scale_invariant_log_growth(), plot_2_popperian_regime_separation(), plot_3_homotopic_phase_time(), plot_4_dislocation_capital(), save_and_verify_4k() (+2 more)

### Community 24 - "FredETL"
Cohesion: 0.13
Nodes (8): FredETL, get_fred_data(), parse_fred_macro_series(), test_fred_publication_lags(), test_central_bank_balance_sheet_splicing_continuity(), test_global_liquidity_derived_metrics(), test_global_liquidity_schema_and_publication_lags(), test_authentic_fred_gdp_and_housing()

### Community 25 - "test_no_gaussian_bumps.py"
Cohesion: 0.14
Nodes (5): get_shiller_data(), parse_shiller_excel(), ShillerETL, test_shiller_provenance_schema_and_bounds(), test_authentic_shiller_provenance_workbook()

### Community 26 - "FinraETL"
Cohesion: 0.16
Nodes (5): FinraETL, get_finra_margin_debt(), parse_finra_margin_debt_series(), test_finra_margin_publication_lag(), test_authentic_finra_margin_debt()

### Community 27 - "compute_lppls_confidence_indicator"
Cohesion: 0.13
Nodes (6): calibrate_lppls_filimonov(), compute_lppls_confidence_indicator(), test_lppls_confidence_indicator_pipeline(), test_lppls_historical_bubble_detection(), test_lppls_parameter_recovery_synthetic(), test_lppls_sornette_filtering_bounds()

### Community 28 - "composite_summary.py"
Cohesion: 0.24
Nodes (5): causal_ffill_clean(), causal_gram_schmidt(), causal_stationary_unit_variance(), compute_orthogonal_basis_and_summaries_numpy(), norm_cdf_numpy()

### Community 29 - "test_tda_wavelet_rigor.py"
Cohesion: 0.12
Nodes (11): _compute_morlet_wavelet_energy_and_entropy(), _compute_persistence_landscape_and_entropy(), _compute_rips_persistence_diagrams(), compute_tda_wavelet_complexity(), _takens_embedding(), test_compute_tda_wavelet_complexity(), test_bubenik_l2_norm_and_persistence_entropy(), test_morlet_wavelet_scaleogram_and_spectral_entropy() (+3 more)

### Community 30 - "precompile_wasm_parquet_datasets"
Cohesion: 0.29
Nodes (3): precompile_wasm_parquet_datasets(), ensure_synchronized_wasm_datasets(), test_precompile_wasm_parquet_datasets()

### Community 31 - "postprocess_wasm.py"
Cohesion: 0.08
Nodes (21): postprocess_wasm_content(), clean_bokeh_templates(), postprocess_wasm_html(), sync_wasm_build_directories(), [3.0.0] - 2026-09-03, [3.1.0] - 2026-10-05, [3.2.0] - 2026-11-03, [3.3.0] - 2026-11-05 (+13 more)

### Community 32 - "Detailed Slide Breakdown by Section & Group"
Cohesion: 0.22
Nodes (8): Detailed Slide Breakdown by Section & Group, Executive Presentation Deck Overview, Group 2: Supporting Evidence: Valuation, Econometrics & ML (Group Confidence Score: 0.93), Group 3: Sector Specific Application: Tech vs. Energy (Group Confidence Score: 0.91), Group 4: Implications for Systemic Stability (Group Confidence Score: 0.95), Group 5: Strategic Recommendations (Group Confidence Score: 0.96), Verification Results, Walkthrough: Multidimensional Econometric & Quantitative Market Bubble Detection PowerPoint Deck

### Community 33 - "build_tech_exuberance_fig"
Cohesion: 0.15
Nodes (7): build_tech_exuberance_fig(), normalize_tda_indicator(), test_pane_tech_exuberance_in_dashboard_tabs(), test_tech_exuberance_columns_in_core_wasm(), test_tech_exuberance_fig_structure_desktop(), test_tech_exuberance_fig_structure_mobile(), test_tech_exuberance_fig_structure_option_3()

### Community 34 - "polars"
Cohesion: 0.11
Nodes (5): IndicatorComputationError, compute_technical_indicators(), test_margin_leverage_alias_parity(), test_options_volatility_alias_parity(), test_technical_alias_parity()

### Community 35 - "DataIngestor"
Cohesion: 0.09
Nodes (10): DataIngestor, Added, test_option_1_50yr_data_ingestion(), test_option_2_modern_data_ingestion(), test_option_3_20yr_data_ingestion(), sample_df(), ingestor(), test_fetch_market_data_schema_and_downcasting() (+2 more)

### Community 36 - "System Architecture and Operational Rules for Agents"
Cohesion: 0.40
Nodes (4): 1. Core Econometric & Statistical Rules, 2. Directory Layout & Key Modules, 3. Execution & Verification Rules, System Architecture and Operational Rules for Agents

### Community 37 - "📊 8 Interactive Dashboard Modules"
Cohesion: 0.22
Nodes (9): 1. Macro Valuation Anchors, 2. Systemic Liquidity & Leverage, 3. Econometric Explosive Bubble Diagnostics, 4. Options Sentiment & Behavioral Tracking, 5. Sector Vulnerability & Topological Dynamics, 6. Signed Macro Mahalanobis Distance & Dynamic Equity Exposure, 7. Tech Exuberance Score: Macro Decoupling vs Statistical Singularity, 8. Composite Summary Indicators: Information-Maximizing Orthogonal Synthesis ($\mathcal{B}_{13}^{\perp}$) (+1 more)

### Community 38 - "get_vxo_data"
Cohesion: 0.15
Nodes (5): get_vxo_data(), parse_authentic_vxo_series(), VxoETL, test_vxo_authenticity_and_black_monday(), test_authentic_cboe_vxo_black_monday()

### Community 39 - "panel_dashboard.py"
Cohesion: 0.15
Nodes (6): compute_composite_validation_metrics(), compute_dislocation_fidelity_metrics(), get_current_date(), get_dynamic_50yr_date_range(), get_dynamic_horizon_metadata(), precompile_wasm_parquet_datasets()

### Community 41 - "CompositeSummaryEngine"
Cohesion: 0.21
Nodes (3): CompositeSummaryEngine, test_orthogonal_basis_13_spectral_entropy_and_vif_20yr(), test_strict_causal_filtration_zero_lookahead()

### Community 43 - "test_wasm_pyodide_sandbox.py"
Cohesion: 0.08
Nodes (10): apply_postprocessing(), test_date_horizon_selector_robust_against_year_shift(), test_dist_index_html_on_disk(), test_dist_index_html_postprocessing_idempotence(), test_json_datasets_staging(), test_template_and_cards_reconstruction(), test_wasm_full_script_pure_numpy_fallback_execution(), test_wasm_full_script_pyodide_execution() (+2 more)

### Community 46 - "features/__init__.py"
Cohesion: 0.12
Nodes (13): compute_gsadf_gpt_decomposition(), compute_margin_leverage_metrics(), compute_macro_valuations(), compute_options_volatility_metrics(), generate_wasm_dataset(), test_compute_gsadf_gpt_decomposition(), test_compute_macro_valuations(), test_compute_margin_leverage_metrics() (+5 more)

### Community 47 - "numpy"
Cohesion: 0.12
Nodes (6): market_simulation_df(), mock_indicators_df(), test_walk_forward_brier_score(), test_crash_trough_exposure_retention(), test_min_cov_det_robustness(), test_signed_projection_asymmetry()

### Community 48 - "Appendix: Architectural Principles & Methodological Justification (IP-Protected Technical Overview)"
Cohesion: 0.25
Nodes (7): A.1 Scope & Intellectual Property Boundary, A.2 Stage I: Eliminating Look-Ahead Bias & Non-Stationary Drift via Strictly Causal Standardization, A.3 Stage II: Eliminating Multicollinearity via Sequential Cross-Domain Orthogonalization, A.4 Stage III: Structural Mechanics of the Five Complementary Summary Engines, A.5 Stage IV: Directional Polarity Alignment & The Crash-Liquidation Damper, A.6 License & Confidentiality Attestation, Appendix: Architectural Principles & Methodological Justification (IP-Protected Technical Overview)

### Community 49 - "test_composite_summary_tab8.py"
Cohesion: 0.22
Nodes (4): compute_dislocation_fidelity_metrics(), test_dislocation_8_fidelity_metrics_popperian_falsification_20yr(), test_dislocation_fidelity_edge_cases_and_wasm_fallback_parity(), test_five_summary_indicators_bounds_and_crash_separation_20yr()

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

### Community 57 - "BubbleDetectorError"
Cohesion: 0.25
Nodes (5): BubbleDetectorError, DataFetchError, ValidationError, 1. System, Configuration & Date Horizons (`config.py` & `date_horizons.py`):, Group 1: Key Findings (Group Confidence Score: 0.94)

### Community 58 - "test_ui_theme.py"
Cohesion: 0.29
Nodes (4): toggle_theme(), get_theme_css(), test_theme_css_generation(), test_wcag_aa_compliance()

### Community 60 - "📉 Multidimensional Market Bubble Detector & Structural Break System"
Cohesion: 0.25
Nodes (7): Benchmark Comparison (50-Year Multi-Decade Horizon), 📅 Dynamic 50-Year Multi-Horizon Date Engine, 🎯 Falsifiable Historical Peak Validation Event Study, 📈 Institutional Cost-Inclusive Portfolio Backtest, 📜 License, 🌟 Live Interactive WebAssembly Dashboard, 📉 Multidimensional Market Bubble Detector & Structural Break System

### Community 61 - "🔬 Mathematical Formulations"
Cohesion: 0.25
Nodes (8): 1. Continuous Backward Compounding (Cliff Eradication), 2. Signed Macro Mahalanobis Distance & Directional Projection, 3. Dynamic Portfolio Equity Sizing ($w_{\text{equity}}$), 4. Canonical PSY Recursive Right-Tailed Unit Root Testing (GSADF / BSADF), 5. Topological Data Analysis (TDA) & Wavelet Spectral Entropy, 6. Log-Periodic Power Law Singularity (LPPLS) Subordination Model, 7. Global Liquidity Index & Dual-Condition Conjoint Exuberance, 🔬 Mathematical Formulations

### Community 63 - "💻 Local Setup & Execution Guide"
Cohesion: 0.29
Nodes (7): 1. Prerequisites & Virtual Environment, 2. Run the High-Performance NiceGUI Application, 3. Run the Local HoloViz Panel Dashboard, 4. Build and Run Client-Side WebAssembly (Pyodide), 5. Run the Automated Test Suite, 6. Synchronize Repository Knowledge Graph, 💻 Local Setup & Execution Guide

### Community 66 - "[v2.1.0] - 2026-09-02"
Cohesion: 0.67
Nodes (3): Added, Fixed, [v2.1.0] - 2026-09-02

## Knowledge Gaps
- **16 isolated node(s):** `market-bubble-detector`, `Polars DataFrame Integration`, `Margin Debt Growth Velocity`, `May 2026 Month-over-Month Change (+8.53%)`, `May 2026 Margin Debt Nominal Value ($1.416T)` (+11 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 553 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **12 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `📊 8 Interactive Dashboard Modules` connect `📊 8 Interactive Dashboard Modules` to `📉 Multidimensional Market Bubble Detector & Structural Break System`?**
  _High betweenness centrality (0.053) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `DashboardState` (e.g. with `PortfolioBacktestEngine` and `DataIngestor`) actually correct?**
  _`DashboardState` has 11 INFERRED edges - model-reasoned connections that need verification._
- **What connects `market-bubble-detector`, `Polars DataFrame Integration`, `Margin Debt Growth Velocity` to the rest of the system?**
  _16 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Market Bubble Structural Analysis Report` be split into smaller, more focused modules?**
  _Cohesion score 0.07563025210084033 - nodes in this community are weakly interconnected._
- **Why does `8. Composite Summary Indicators: Information-Maximizing Orthogonal Synthesis ($\mathcal{B}_{13}^{\perp}$)` connect `📊 8 Interactive Dashboard Modules` to `dashboard.py`, `build_mahalanobis_fig`?**
  _High betweenness centrality (0.052) - this node is a cross-community bridge._
- **Should `MacroMahalanobisDetector` be split into smaller, more focused modules?**
  _Cohesion score 0.1349206349206349 - nodes in this community are weakly interconnected._
- **Why does `build_dislocation_fidelity_chart()` connect `dashboard.py` to `📋 Changelog`, `📊 8 Interactive Dashboard Modules`, `bubble_detector/__init__.py`, `numpy`, `test_composite_summary_tab8.py`, `postprocess_wasm.py`?**
  _High betweenness centrality (0.052) - this node is a cross-community bridge._