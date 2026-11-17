# Graph Report - Merrill  (2026-11-16)

## Corpus Check
- 97 files · ~188,818 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 19 file(s) not represented in the graph (top: .parquet 9, .csv 6, (none) 2)

## Summary
- 1279 nodes · 2684 edges · 90 communities (76 shown, 14 thin omitted)
- Extraction: 92% EXTRACTED · 8% INFERRED · 0% AMBIGUOUS · INFERRED: 226 edges (avg confidence: 0.88)
- Token cost: 64,000 input · 3,600 output

## Graph Freshness
- Built from commit: `4376815d`
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
- B.1 False Alarms & Full-Period Behavior Outside the Eight Peaks (2006–2026)
- _rolling_adf_vectorized
- B.4 Model Construction, Pre-2006 Crises, Damper Ablations, Parameter Sensitivity & Version Lineage
- generate_deck.py
- pytest
- test_ui_ux_wasm_optimizations.py
- calculate_contrast_ratio
- dashboard.py
- config.py
- HighFidelityEventStudy_Executive_Report.md
- HighFidelityEventStudy/README.md
- Appendix B: Institutional Due-Diligence & Third-Party Technical Q&A (IP-Protected Audit)
- B.4 Model Construction, Pre-2006 Crises, Damper Ablations, Parameter Sensitivity & Version Lineage
- generate_high_fidelity_plots.py
- FredETL
- test_no_gaussian_bumps.py
- FinraETL
- numpy
- composite_summary.py
- test_tda_wavelet_rigor.py
- structural_breaks.py
- Changelog
- PortfolioBacktestEngine
- build_tech_exuberance_fig
- precompile_wasm_parquet_datasets
- B.1 False Alarms & Full-Period Behavior Outside the Eight Peaks (2006–2026)
- System Architecture and Operational Rules for Agents
- 📊 8 Interactive Dashboard Modules
- config.py
- get_current_date
- sw.js
- .load_data
- test_date_horizons.py
- test_wasm_pyodide_sandbox.py
- test_composite_summary_tab8.py
- B.4 Model Construction, Pre-2006 Crises, Damper Ablations, Parameter Sensitivity & Version Lineage
- 📉 Multidimensional Market Bubble Detector & Structural Break System
- 🔬 Mathematical Formulations
- Appendix: Architectural Principles & Methodological Justification (IP-Protected Technical Overview)
- CompositeSummaryEngine
- Section 1: Executive Summary of the Composite Indicators & Strategic Mandate
- High-Fidelity 20-Year Dislocation Event Study & Composite Regime Synthesis (2006–2026)
- Section 2: Scale-Invariant Log-Growth Trajectory & Dual-Phase Dislocation Corridors
- Section 3: 8-Dislocation Popperian Falsification & Peak-vs-Trough Regime Separation
- Section 4: Homotopic Phase-Time Superposed Epoch Analysis Across Dislocation Cycles
- Section 5: Institutional Capital Preservation & Early-Warning Lead Cushion Profile
- B.1 False Alarms & Full-Period Behavior Outside the Eight Peaks (2006–2026)
- Appendix B: Institutional Due-Diligence & Third-Party Technical Q&A (IP-Protected Audit)
- Appendix A: Architectural Principles & Methodological Justification (IP-Protected Technical Overview)
- B.6 Current Live Readings (`November 13, 2026`) & Role of the Knowledge-Graph Engine
- B.6 Current Live Readings (`November 13, 2026`) & Role of the Knowledge-Graph Engine
- Appendix B: Institutional Due-Diligence & Third-Party Technical Q&A (IP-Protected Audit)
- 💻 Local Setup & Execution Guide
- compute_lppls_confidence_indicator
- B.6 Current Live Readings (`November 13, 2026`) & Role of the Knowledge-Graph Engine
- [v2.1.0] - 2026-09-02
- Section 1: Executive Summary of the Composite Indicators & Strategic Mandate
- B.3 Defensive Backtest Mechanics, Re-Entry Causality & Actual Treasury-Bill Rerun
- B.3 Defensive Backtest Mechanics, Re-Entry Causality & Actual Treasury-Bill Rerun
- precompile_wasm_parquet_datasets
- Q1.1 & Q1.2: Full-Period Daily Score Distribution (2006–2026) & Share of Days at or Above `70.0%`
- Section 3: 8-Dislocation Popperian Falsification & Peak-vs-Trough Regime Separation
- generate_wasm_dataset
- Section 4: Homotopic Phase-Time Superposed Epoch Analysis Across Dislocation Cycles
- Q1.1 & Q1.2: Full-Period Daily Score Distribution (2006–2026) & Share of Days at or Above `70.0%`
- B.3 Defensive Backtest Mechanics, Re-Entry Causality & Actual Treasury-Bill Rerun
- Q4.3: Pre-Peak and Trough Scores with the Crash-Liquidation Damper (`Λ_Crash`) Switched OFF
- test_leakage_elimination.py
- Q4.5: Why Intermediate `~10%` Corrections (Early 2018 Volmageddon, Autumn 2023, Spring 2012) Were Excluded from `D1`–`D8`, and How the Model Performed on Them
- Q4.1 & Q4.2: Parameter Freezing / Walk-Forward Integrity & Pre-2006 Historical Crises (`1987`, `1990`, `1998`, `2000–02`)
- Q4.5: Why Intermediate `~10%` Corrections (Early 2018 Volmageddon, Autumn 2023, Spring 2012) Were Excluded from `D1`–`D8`, and How the Model Performed on Them
- precompile_wasm_parquet_datasets

## God Nodes (most connected - your core abstractions)
1. `DashboardState` - 51 edges
2. `MacroMahalanobisDetector` - 37 edges
3. `DataIngestor` - 31 edges
4. `generate_wasm_dataset()` - 31 edges
5. `StructuralBreakPredictor` - 30 edges
6. `test_all_7_tabs_plot_trace_parity()` - 24 edges
7. `precompile_wasm_parquet_datasets()` - 24 edges
8. `compute_tda_wavelet_complexity()` - 23 edges
9. `compute_gsadf_gpt_decomposition()` - 22 edges
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
- `Added` --references--> `compute_exuberance_spans()`  [INFERRED]
  CHANGELOG.md → bubble_detector/features/tech_exuberance.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **AGVI Indicator and Feature Engineering Pipeline** — marketbubble_ddfv100_shiller_cape_ratio, marketbubble_ddfv100_payout_adjusted_cape, marketbubble_ddfv100_buffett_indicator, marketbubble_ddfv100_gsadf_psy_procedure [EXTRACTED 1.00]
- **Econometric and Mathematical Bubble Detection Framework** — marketbubble_ddfv100_gsadf_psy_procedure, marketbubble_ddfv100_tda_wavelet, marketbubble_ddfv100_lppls_model [EXTRACTED 1.00]
- **Implied Volatility Term Structure Components** — impliedvolatilitymetric_vix1d, impliedvolatilitymetric_vix_spot, impliedvolatilitymetric_vix3m, impliedvolatilitymetric_vix1y [EXTRACTED 1.00]
- **FINRA Margin Debt Metrics** — finra_margin_debt_tracker, finra_may_2026_nominal_value, finra_may_2026_mom_change, finra_may_2026_yoy_change [INFERRED 0.85]

## Communities (90 total, 14 thin omitted)

### Community 0 - "Market Bubble Structural Analysis Report"
Cohesion: 0.08
Nodes (35): NiceGUI Layout & Plotly Dashboard, Data Ingestion (DataIngestor), AGVI Implementation Plan Document, Feature Engineering Pipeline, XGBoost Model Training & Walk-Forward CV, AGVI Technical Specification Document, NiceGUI Dashboard UI, Polars DataFrame Integration (+27 more)

### Community 1 - "test_mahalanobis.py"
Cohesion: 0.09
Nodes (12): fast_ledoit_wolf_cov(), MacroMahalanobisDetector, test_anomaly_driver_attribution(), test_dynamic_exposure_bounds_and_monotonicity(), test_mahalanobis_distance_non_negative(), test_mahalanobis_no_early_rank_singularity(), test_regime_probability_bounds(), test_stationary_features_shape_and_values() (+4 more)

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
Cohesion: 0.12
Nodes (22): build_band_polygon(), build_composite_summary_fig(), build_composite_validation_fig(), build_dislocation_fidelity_fig(), build_econometric_fig(), build_leverage_fig(), build_macro_valuation_fig(), build_mahalanobis_fig() (+14 more)

### Community 6 - "StructuralBreakPredictor"
Cohesion: 0.15
Nodes (5): StructuralBreakPredictor, test_predict_drawdown_probability(), test_structural_break_predictor_walk_forward(), test_structural_breaks_embargo_no_lookahead(), test_reliability_diagram_monotonicity()

### Community 8 - "B.1 False Alarms & Full-Period Behavior Outside the Eight Peaks (2006–2026)"
Cohesion: 0.20
Nodes (10): B.1 False Alarms & Full-Period Behavior Outside the Eight Peaks (2006–2026), Executive-Level Answer, Executive-Level Answer, Executive-Level Answer: The "Seismograph vs. Structural Envelope" Principle, IP-Protected Technical Justification, IP-Protected Technical Justification & Complete 66-Crossing Audit Table, IP-Protected Technical Justification: The Three Causal Signal-Processing Filters, Q1.3: Forward 6-, 12-, and 18-Month Index Returns & Worst Drawdowns for Every Crossing Above `70.0%` (+2 more)

### Community 9 - "_rolling_adf_vectorized"
Cohesion: 0.29
Nodes (3): _batch_adf_from_log_windows(), _in_window_coint_adf(), _rolling_adf_vectorized()

### Community 11 - "B.4 Model Construction, Pre-2006 Crises, Damper Ablations, Parameter Sensitivity & Version Lineage"
Cohesion: 0.12
Nodes (16): B.4 Model Construction, Pre-2006 Crises, Damper Ablations, Parameter Sensitivity & Version Lineage, Executive-Level Answer, Executive-Level Answer, Executive-Level Answer, Executive-Level Answer, Executive-Level Answer, High-Resolution 4K Visualization: Multi-Threshold Stratified Pre-Peak Warning Corridors (`75%`, `80%`, `85%`) & Dislocation Risk (`4096 × 3072`), IP-Protected Technical Justification & Damper Ablation Table (+8 more)

### Community 12 - "generate_deck.py"
Cohesion: 0.20
Nodes (3): create_presentation(), add_card(), add_metric_badge()

### Community 13 - "pytest"
Cohesion: 0.10
Nodes (4): ensure_synchronized_wasm_datasets(), market_simulation_df(), test_strictly_causal_one_day_execution_lag(), test_walk_forward_brier_score()

### Community 14 - "test_ui_ux_wasm_optimizations.py"
Cohesion: 0.09
Nodes (10): lttb_downsample(), normalize_tda_indicator(), test_keyboard_operability_and_aria_landmarks(), test_lttb_downsample_edge_cases(), test_lttb_downsample_extrema_retention(), test_lttb_downsample_monotonic_dates(), test_responsive_legend_layout_logic(), test_service_worker_file_validity() (+2 more)

### Community 16 - "calculate_contrast_ratio"
Cohesion: 0.09
Nodes (18): calculate_contrast_ratio(), get_plotly_template(), is_wcag_aa_compliant(), parse_hex_color(), relative_luminance(), 2. UI & Accessibility Engine (`ui_theme.py`):, test_ui_theme_alias_parity(), test_contrast_ratio_calculation() (+10 more)

### Community 17 - "dashboard.py"
Cohesion: 0.06
Nodes (36): create_cta_banner(), create_ios_card(), build_composite_summary_chart(), build_composite_validation_chart(), build_dislocation_fidelity_chart(), build_econometric_chart(), build_leverage_chart(), build_macro_valuation_chart() (+28 more)

### Community 18 - "config.py"
Cohesion: 0.12
Nodes (5): parse_finra_margin_debt_series(), parse_authentic_vxo_series(), test_spy_backward_compounding_no_cliff(), test_vxo_vix_seam_continuity(), test_xlk_backward_compounding_no_cliff()

### Community 19 - "HighFidelityEventStudy_Executive_Report.md"
Cohesion: 0.15
Nodes (12): 2.1 Executive Explanation of the Composite Indicator in This View, 2.2 High-Resolution 4K Visualization: Scale-Invariant Log-Growth (`4096 × 3072`), 2.3 Detailed Walkthrough of the Plot, Axes & Labeled Callouts, 5.1 Executive Explanation of the Composite Indicator in This View, 5.2 High-Resolution 4K Visualization: Dislocation Capital Preservation (`4096 × 3072`), 5.3 Detailed Walkthrough of the Plot, Axes & Labeled Callouts, Document Changelog (SemVer), Executive Summary Abstract (+4 more)

### Community 20 - "HighFidelityEventStudy/README.md"
Cohesion: 0.06
Nodes (32): 1.1 The Core Institutional Challenge: Information Redundancy vs. Structural Blind Spots, 1.2 Our Ultimate Strategic Goal: Maximum Information Extraction & Asymmetric Capital Defense, 1.3 Overview of the Five Complementary Composite Summary Indicators, 1.4 High-Level Empirical Scorecard Across the 20-Year Horizon (2006–2026), 2.1 Executive Explanation of the Composite Indicator in This View, 2.2 High-Resolution 4K Visualization: Scale-Invariant Log-Growth (`4096 × 3072`), 2.3 Detailed Walkthrough of the Plot, Axes & Labeled Callouts, 3.1 Executive Explanation of the Composite Indicator in This View (+24 more)

### Community 21 - "Appendix B: Institutional Due-Diligence & Third-Party Technical Q&A (IP-Protected Audit)"
Cohesion: 0.29
Nodes (7): Appendix B: Institutional Due-Diligence & Third-Party Technical Q&A (IP-Protected Audit), B.2 Lead Times, Window Caps & Pre-Peak Duty Cycles, B.5 Resolution of Report & Chart Conventions Flagged in Section 5 (`v1.2.0` Harmonization), Executive-Level Answer, Executive-Level Summary of All Six Harmonizations Applied in `v1.2.0`, IP-Protected Technical Justification & Complete Lead-Time Comparison Table, Q2.1, Q2.2, Q2.3 & Q2.4: Definition of Advance Warning Lead, `180d` vs. `252d` vs. Uncapped Windows, and Intra-Window Dropouts

### Community 22 - "B.4 Model Construction, Pre-2006 Crises, Damper Ablations, Parameter Sensitivity & Version Lineage"
Cohesion: 0.20
Nodes (10): B.4 Model Construction, Pre-2006 Crises, Damper Ablations, Parameter Sensitivity & Version Lineage, Executive-Level Answer, Executive-Level Answer, Executive-Level Answer, High-Resolution 4K Visualization: Multi-Threshold Stratified Pre-Peak Warning Corridors (`75%`, `80%`, `85%`) & Dislocation Risk (`4096 × 3072`), IP-Protected Technical Justification & Damper Ablation Table, IP-Protected Technical Justification & Multi-Threshold Sensitivity Matrix, Q4.3: Pre-Peak and Trough Scores with the Crash-Liquidation Damper (`Λ_Crash`) Switched OFF (+2 more)

### Community 23 - "generate_high_fidelity_plots.py"
Cohesion: 0.18
Nodes (10): get_palette(), main(), plot_1_scale_invariant_log_growth(), plot_2_popperian_regime_separation(), plot_3_homotopic_phase_time(), plot_4_dislocation_capital(), plot_5_log_growth_vs_master_composite(), plot_6_multi_threshold_corridors_75_80_85() (+2 more)

### Community 24 - "FredETL"
Cohesion: 0.12
Nodes (8): FredETL, get_fred_data(), parse_fred_macro_series(), test_fred_publication_lags(), test_central_bank_balance_sheet_splicing_continuity(), test_global_liquidity_derived_metrics(), test_global_liquidity_schema_and_publication_lags(), test_authentic_fred_gdp_and_housing()

### Community 25 - "test_no_gaussian_bumps.py"
Cohesion: 0.16
Nodes (5): get_shiller_data(), parse_shiller_excel(), ShillerETL, test_shiller_provenance_schema_and_bounds(), test_authentic_shiller_provenance_workbook()

### Community 26 - "FinraETL"
Cohesion: 0.18
Nodes (5): FinraETL, get_finra_margin_debt(), stage_all(), test_finra_margin_publication_lag(), test_authentic_finra_margin_debt()

### Community 27 - "numpy"
Cohesion: 0.06
Nodes (16): compute_wild_bootstrap_critical_values(), compute_exuberance_spans(), compute_tech_exuberance_metrics(), calculate_adf_stat(), test_adf_lag_selection_k0_vs_k1(), test_adf_stat_explosive_vs_stationary(), test_recursive_backward_supremum_grid(), test_wild_bootstrap_critical_value_bounds() (+8 more)

### Community 28 - "composite_summary.py"
Cohesion: 0.15
Nodes (8): build_band_polygon(), causal_ffill_clean(), causal_gram_schmidt(), causal_stationary_unit_variance(), compute_composite_validation_metrics(), compute_orthogonal_basis_and_summaries_numpy(), _compute_orthogonal_basis_matrix(), norm_cdf_numpy()

### Community 29 - "test_tda_wavelet_rigor.py"
Cohesion: 0.07
Nodes (20): _compute_morlet_wavelet_energy_and_entropy(), _compute_persistence_landscape_and_entropy(), _compute_rips_persistence_diagrams(), _get_morlet_toeplitz_matrices(), _takens_embedding(), takens_embedding(), 10. Institutional Code Commentary, Packaging & Agent Navigation:, 3. Data Ingestion & Storage (`ingestor.py`): (+12 more)

### Community 30 - "structural_breaks.py"
Cohesion: 0.12
Nodes (7): BubbleDetectorError, DataFetchError, IndicatorComputationError, ModelTrainingError, ValidationError, 1. System, Configuration & Date Horizons (`config.py` & `date_horizons.py`):, Group 1: Key Findings (Group Confidence Score: 0.94)

### Community 31 - "Changelog"
Cohesion: 0.05
Nodes (26): postprocess_wasm_content(), clean_bokeh_templates(), postprocess_wasm_html(), sync_wasm_build_directories(), [3.0.0] - 2026-09-03, [3.1.0] - 2026-10-05, [3.2.0] - 2026-11-03, [3.3.0] - 2026-11-05 (+18 more)

### Community 32 - "PortfolioBacktestEngine"
Cohesion: 0.09
Nodes (7): BacktestResult, PortfolioBacktestEngine, _compute_empirical_false_alarm_rate(), compute_validation_summary_statistics(), generate_historical_validation_table(), test_backtest_fee_deduction(), test_exposure_rule_vs_naive_cape()

### Community 33 - "build_tech_exuberance_fig"
Cohesion: 0.17
Nodes (7): build_tech_exuberance_fig(), fetch_dataset(), test_pane_tech_exuberance_in_dashboard_tabs(), test_tech_exuberance_columns_in_core_wasm(), test_tech_exuberance_fig_structure_desktop(), test_tech_exuberance_fig_structure_mobile(), test_tech_exuberance_fig_structure_option_3()

### Community 34 - "precompile_wasm_parquet_datasets"
Cohesion: 0.25
Nodes (4): compute_technical_indicators(), precompile_wasm_parquet_datasets(), test_compute_technical_indicators(), test_precompile_wasm_parquet_datasets()

### Community 35 - "B.1 False Alarms & Full-Period Behavior Outside the Eight Peaks (2006–2026)"
Cohesion: 0.14
Nodes (14): B.1 False Alarms & Full-Period Behavior Outside the Eight Peaks (2006–2026), Executive-Level Answer, Executive-Level Answer, Executive-Level Answer, Executive-Level Answer: The "Seismograph vs. Structural Envelope" Principle, High-Resolution 4K Visualization: Scale-Invariant Log-Growth vs. Smooth Causal Master Composite Envelope (`4096 × 3072`), IP-Protected Technical Justification, IP-Protected Technical Justification & Complete 66-Crossing Audit Table (+6 more)

### Community 36 - "System Architecture and Operational Rules for Agents"
Cohesion: 0.40
Nodes (4): 1. Core Econometric & Statistical Rules, 2. Directory Layout & Key Modules, 3. Execution & Verification Rules, System Architecture and Operational Rules for Agents

### Community 37 - "📊 8 Interactive Dashboard Modules"
Cohesion: 0.22
Nodes (9): 1. Macro Valuation Anchors, 2. Systemic Liquidity & Leverage, 3. Econometric Explosive Bubble Diagnostics, 4. Options Sentiment & Behavioral Tracking, 5. Sector Vulnerability & Topological Dynamics, 6. Signed Macro Mahalanobis Distance & Dynamic Equity Exposure, 7. Tech Exuberance Score: Macro Decoupling vs Statistical Singularity, 8. Composite Summary Indicators: Information-Maximizing Orthogonal Synthesis ($\mathcal{B}_{13}^{\perp}$) (+1 more)

### Community 38 - "config.py"
Cohesion: 0.18
Nodes (4): get_vxo_data(), VxoETL, test_vxo_authenticity_and_black_monday(), test_authentic_cboe_vxo_black_monday()

### Community 39 - "get_current_date"
Cohesion: 0.43
Nodes (3): get_current_date(), get_dynamic_50yr_date_range(), get_dynamic_horizon_metadata()

### Community 41 - ".load_data"
Cohesion: 0.18
Nodes (4): DataIngestor, Added, test_dashboard_state_horizon_switching(), sample_df()

### Community 42 - "test_date_horizons.py"
Cohesion: 0.06
Nodes (15): clamp_to_trading_day(), get_current_date(), get_dynamic_50yr_date_range(), get_dynamic_horizon_metadata(), _date_seeded_normals(), ingestor(), test_dynamic_50yr_date_generator(), test_option_1_50yr_data_ingestion() (+7 more)

### Community 43 - "test_wasm_pyodide_sandbox.py"
Cohesion: 0.10
Nodes (6): apply_postprocessing(), test_dist_index_html_on_disk(), test_dist_index_html_postprocessing_idempotence(), test_template_and_cards_reconstruction(), test_wasm_full_script_pure_numpy_fallback_execution(), test_wasm_full_script_pyodide_execution()

### Community 44 - "test_composite_summary_tab8.py"
Cohesion: 0.15
Nodes (7): compute_dislocation_fidelity_metrics(), test_dislocation_8_fidelity_metrics_popperian_falsification_20yr(), test_dislocation_fidelity_edge_cases_and_wasm_fallback_parity(), test_five_summary_indicators_bounds_and_crash_separation_20yr(), test_tab8_dislocation_fidelity_dual_ui_parity(), test_tab8_dual_ui_parity_across_all_horizons(), test_tab8_validation_6_color_bands_and_wealth_parity()

### Community 45 - "B.4 Model Construction, Pre-2006 Crises, Damper Ablations, Parameter Sensitivity & Version Lineage"
Cohesion: 0.20
Nodes (10): B.4 Model Construction, Pre-2006 Crises, Damper Ablations, Parameter Sensitivity & Version Lineage, Executive-Level Answer, Executive-Level Answer, Executive-Level Answer, High-Resolution 4K Visualization: Multi-Threshold Stratified Pre-Peak Warning Corridors (`75%`, `80%`, `85%`) & Dislocation Risk (`4096 × 3072`), IP-Protected Technical Justification & Multi-Threshold Sensitivity Matrix, IP-Protected Technical Justification & Pre-2006 Empirical Scorecard, Q4.1 & Q4.2: Parameter Freezing / Walk-Forward Integrity & Pre-2006 Historical Crises (`1987`, `1990`, `1998`, `2000–02`) (+2 more)

### Community 46 - "📉 Multidimensional Market Bubble Detector & Structural Break System"
Cohesion: 0.25
Nodes (7): Benchmark Comparison (50-Year Multi-Decade Horizon), 📅 Dynamic 50-Year Multi-Horizon Date Engine, 🎯 Falsifiable Historical Peak Validation Event Study, 📈 Institutional Cost-Inclusive Portfolio Backtest, 📜 License, 🌟 Live Interactive WebAssembly Dashboard, 📉 Multidimensional Market Bubble Detector & Structural Break System

### Community 47 - "🔬 Mathematical Formulations"
Cohesion: 0.25
Nodes (8): 1. Continuous Backward Compounding (Cliff Eradication), 2. Signed Macro Mahalanobis Distance & Directional Projection, 3. Dynamic Portfolio Equity Sizing ($w_{\text{equity}}$), 4. Canonical PSY Recursive Right-Tailed Unit Root Testing (GSADF / BSADF), 5. Topological Data Analysis (TDA) & Wavelet Spectral Entropy, 6. Log-Periodic Power Law Singularity (LPPLS) Subordination Model, 7. Global Liquidity Index & Dual-Condition Conjoint Exuberance, 🔬 Mathematical Formulations

### Community 48 - "Appendix: Architectural Principles & Methodological Justification (IP-Protected Technical Overview)"
Cohesion: 0.25
Nodes (7): A.1 Scope & Intellectual Property Boundary, A.2 Stage I: Eliminating Look-Ahead Bias & Non-Stationary Drift via Strictly Causal Standardization, A.3 Stage II: Eliminating Multicollinearity via Sequential Cross-Domain Orthogonalization, A.4 Stage III: Structural Mechanics of the Five Complementary Summary Engines, A.5 Stage IV: Directional Polarity Alignment & The Crash-Liquidation Damper, A.6 License & Confidentiality Attestation, Appendix A: Architectural Principles & Methodological Justification (IP-Protected Technical Overview)

### Community 49 - "CompositeSummaryEngine"
Cohesion: 0.16
Nodes (3): CompositeSummaryEngine, test_orthogonal_basis_13_spectral_entropy_and_vif_20yr(), test_strict_causal_filtration_zero_lookahead()

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

### Community 56 - "B.1 False Alarms & Full-Period Behavior Outside the Eight Peaks (2006–2026)"
Cohesion: 0.20
Nodes (10): B.1 False Alarms & Full-Period Behavior Outside the Eight Peaks (2006–2026), Executive-Level Answer, Executive-Level Answer, Executive-Level Answer: The "Seismograph vs. Structural Envelope" Principle, IP-Protected Technical Justification, IP-Protected Technical Justification & Complete 66-Crossing Audit Table, IP-Protected Technical Justification: The Three Causal Signal-Processing Filters, Q1.3: Forward 6-, 12-, and 18-Month Index Returns & Worst Drawdowns for Every Crossing Above `70.0%` (+2 more)

### Community 57 - "Appendix B: Institutional Due-Diligence & Third-Party Technical Q&A (IP-Protected Audit)"
Cohesion: 0.25
Nodes (7): Appendix B: Institutional Due-Diligence & Third-Party Technical Q&A (IP-Protected Audit), B.2 Lead Times, Window Caps & Pre-Peak Duty Cycles, B.5 Resolution of Report & Chart Conventions Flagged in Section 5 (`v1.2.0` Harmonization), Executive-Level Answer, Executive-Level Summary of All Six Harmonizations Applied in `v1.2.0`, IP-Protected Technical Justification & Complete Lead-Time Comparison Table, Q2.1, Q2.2, Q2.3 & Q2.4: Definition of Advance Warning Lead, `180d` vs. `252d` vs. Uncapped Windows, and Intra-Window Dropouts

### Community 59 - "Appendix A: Architectural Principles & Methodological Justification (IP-Protected Technical Overview)"
Cohesion: 0.29
Nodes (7): A.1 Scope & Intellectual Property Boundary, A.2 Stage I: Eliminating Look-Ahead Bias & Non-Stationary Drift via Strictly Causal Standardization, A.3 Stage II: Eliminating Multicollinearity via Sequential Cross-Domain Orthogonalization, A.4 Stage III: Structural Mechanics of the Five Complementary Summary Engines, A.5 Stage IV: Directional Polarity Alignment & The Crash-Liquidation Damper, A.6 License & Confidentiality Attestation, Appendix A: Architectural Principles & Methodological Justification (IP-Protected Technical Overview)

### Community 60 - "B.6 Current Live Readings (`November 13, 2026`) & Role of the Knowledge-Graph Engine"
Cohesion: 0.29
Nodes (7): B.6 Current Live Readings (`November 13, 2026`) & Role of the Knowledge-Graph Engine, Executive-Level Answer, Executive-Level Answer, IP-Protected Technical Justification, IP-Protected Technical Justification & Live November 13, 2026 Telemetry Table, Q6.1: What Is the Master Score Today (`November 13, 2026`)?, Q6.2: Does the Knowledge-Graph Engine (`graphify`) Feed the Quantitative Signal at All?

### Community 61 - "B.6 Current Live Readings (`November 13, 2026`) & Role of the Knowledge-Graph Engine"
Cohesion: 0.29
Nodes (7): B.6 Current Live Readings (`November 13, 2026`) & Role of the Knowledge-Graph Engine, Executive-Level Answer, Executive-Level Answer, IP-Protected Technical Justification, IP-Protected Technical Justification & Live November 13, 2026 Telemetry Table, Q6.1: What Is the Master Score Today (`November 13, 2026`)?, Q6.2: Does the Knowledge-Graph Engine (`graphify`) Feed the Quantitative Signal at All?

### Community 62 - "Appendix B: Institutional Due-Diligence & Third-Party Technical Q&A (IP-Protected Audit)"
Cohesion: 0.29
Nodes (7): Appendix B: Institutional Due-Diligence & Third-Party Technical Q&A (IP-Protected Audit), B.2 Lead Times, Window Caps & Pre-Peak Duty Cycles, B.5 Resolution of Report & Chart Conventions Flagged in Section 5 (`v1.2.0` Harmonization), Executive-Level Answer, Executive-Level Summary of All Six Harmonizations Applied in `v1.2.0`, IP-Protected Technical Justification & Complete Lead-Time Comparison Table, Q2.1, Q2.2, Q2.3 & Q2.4: Definition of Advance Warning Lead, `180d` vs. `252d` vs. Uncapped Windows, and Intra-Window Dropouts

### Community 63 - "💻 Local Setup & Execution Guide"
Cohesion: 0.29
Nodes (7): 1. Prerequisites & Virtual Environment, 2. Run the High-Performance NiceGUI Application, 3. Run the Local HoloViz Panel Dashboard, 4. Build and Run Client-Side WebAssembly (Pyodide), 5. Run the Automated Test Suite, 6. Synchronize Repository Knowledge Graph, 💻 Local Setup & Execution Guide

### Community 64 - "compute_lppls_confidence_indicator"
Cohesion: 0.12
Nodes (7): calibrate_lppls_filimonov(), compute_lppls_confidence_indicator(), _get_lppls_grid(), test_lppls_confidence_indicator_pipeline(), test_lppls_historical_bubble_detection(), test_lppls_parameter_recovery_synthetic(), test_lppls_sornette_filtering_bounds()

### Community 65 - "B.6 Current Live Readings (`November 13, 2026`) & Role of the Knowledge-Graph Engine"
Cohesion: 0.29
Nodes (7): B.6 Current Live Readings (`November 13, 2026`) & Role of the Knowledge-Graph Engine, Executive-Level Answer, Executive-Level Answer, IP-Protected Technical Justification, IP-Protected Technical Justification & Live November 13, 2026 Telemetry Table, Q6.1: What Is the Master Score Today (`November 13, 2026`)?, Q6.2: Does the Knowledge-Graph Engine (`graphify`) Feed the Quantitative Signal at All?

### Community 66 - "[v2.1.0] - 2026-09-02"
Cohesion: 0.67
Nodes (3): Added, Fixed, [v2.1.0] - 2026-09-02

### Community 67 - "Section 1: Executive Summary of the Composite Indicators & Strategic Mandate"
Cohesion: 0.40
Nodes (5): 1.1 The Core Institutional Challenge: Information Redundancy vs. Structural Blind Spots, 1.2 Our Ultimate Strategic Goal: Maximum Information Extraction & Asymmetric Capital Defense, 1.3 Overview of the Five Complementary Composite Summary Indicators, 1.4 High-Level Empirical Scorecard Across the 20-Year Horizon (2006–2026), Section 1: Executive Summary of the Composite Indicators & Strategic Mandate

### Community 68 - "B.3 Defensive Backtest Mechanics, Re-Entry Causality & Actual Treasury-Bill Rerun"
Cohesion: 0.33
Nodes (6): B.3 Defensive Backtest Mechanics, Re-Entry Causality & Actual Treasury-Bill Rerun, Executive-Level Answer, Executive-Level Answer, IP-Protected Technical Justification & Comparative Backtest Tables, Q3.1 & Q3.2: Exact Exposure Rules, Zero Trough-Date Look-Ahead, and Why Episode Losses Are `20–31%` of Index Losses, Q3.3 & Q3.4: 20-Year Return, Volatility & Turnover vs. Buy-and-Hold, and Rerun with Actual Historical T-Bill Yields (`2006–2026`)

### Community 69 - "B.3 Defensive Backtest Mechanics, Re-Entry Causality & Actual Treasury-Bill Rerun"
Cohesion: 0.33
Nodes (6): B.3 Defensive Backtest Mechanics, Re-Entry Causality & Actual Treasury-Bill Rerun, Executive-Level Answer, Executive-Level Answer, IP-Protected Technical Justification & Comparative Backtest Tables, Q3.1 & Q3.2: Exact Exposure Rules, Zero Trough-Date Look-Ahead, and Why Episode Losses Are `20–31%` of Index Losses, Q3.3 & Q3.4: 20-Year Return, Volatility & Turnover vs. Buy-and-Hold, and Rerun with Actual Historical T-Bill Yields (`2006–2026`)

### Community 70 - "precompile_wasm_parquet_datasets"
Cohesion: 0.33
Nodes (3): _serialize_df_to_json_dict(), sync_parquet_to_json(), test_json_datasets_staging()

### Community 71 - "Q1.1 & Q1.2: Full-Period Daily Score Distribution (2006–2026) & Share of Days at or Above `70.0%`"
Cohesion: 0.50
Nodes (4): Executive-Level Answer, High-Resolution 4K Visualization: Scale-Invariant Log-Growth vs. Smooth Causal Master Composite Envelope (`4096 × 3072`), IP-Protected Technical Justification & Year-by-Year Audit, Q1.1 & Q1.2: Full-Period Daily Score Distribution (2006–2026) & Share of Days at or Above `70.0%`

### Community 72 - "Section 3: 8-Dislocation Popperian Falsification & Peak-vs-Trough Regime Separation"
Cohesion: 0.50
Nodes (4): 3.1 Executive Explanation of the Composite Indicator in This View, 3.2 High-Resolution 4K Visualization: 8-Dislocation Popperian Matrix (`4096 × 3072`), 3.3 Detailed Walkthrough of the Plot, Axes & Labeled Callouts, Section 3: 8-Dislocation Popperian Falsification & Peak-vs-Trough Regime Separation

### Community 73 - "generate_wasm_dataset"
Cohesion: 0.08
Nodes (18): compute_gsadf_gpt_decomposition(), compute_margin_leverage_metrics(), compute_macro_valuations(), compute_options_volatility_metrics(), compute_tda_wavelet_complexity(), generate_wasm_dataset(), Fixed & Enhanced (Red Team Remediation Release `RT-CRIT-01` – `RT-LOW-28`), test_compute_gsadf_gpt_decomposition() (+10 more)

### Community 74 - "Section 4: Homotopic Phase-Time Superposed Epoch Analysis Across Dislocation Cycles"
Cohesion: 0.50
Nodes (4): 4.1 Executive Explanation of the Composite Indicator in This View, 4.2 High-Resolution 4K Visualization: Homotopic Phase-Time Analysis (`4096 × 3072`), 4.3 Detailed Walkthrough of the Plot, Axes & Labeled Callouts, Section 4: Homotopic Phase-Time Superposed Epoch Analysis Across Dislocation Cycles

### Community 77 - "Q1.1 & Q1.2: Full-Period Daily Score Distribution (2006–2026) & Share of Days at or Above `70.0%`"
Cohesion: 0.50
Nodes (4): Executive-Level Answer, High-Resolution 4K Visualization: Scale-Invariant Log-Growth vs. Smooth Causal Master Composite Envelope (`4096 × 3072`), IP-Protected Technical Justification & Year-by-Year Audit, Q1.1 & Q1.2: Full-Period Daily Score Distribution (2006–2026) & Share of Days at or Above `70.0%`

### Community 79 - "B.3 Defensive Backtest Mechanics, Re-Entry Causality & Actual Treasury-Bill Rerun"
Cohesion: 0.33
Nodes (6): B.3 Defensive Backtest Mechanics, Re-Entry Causality & Actual Treasury-Bill Rerun, Executive-Level Answer, Executive-Level Answer, IP-Protected Technical Justification & Comparative Backtest Tables, Q3.1 & Q3.2: Exact Exposure Rules, Zero Trough-Date Look-Ahead, and Why Episode Losses Are `20–31%` of Index Losses, Q3.3 & Q3.4: 20-Year Return, Volatility & Turnover vs. Buy-and-Hold, and Rerun with Actual Historical T-Bill Yields (`2006–2026`)

### Community 80 - "Q4.3: Pre-Peak and Trough Scores with the Crash-Liquidation Damper (`Λ_Crash`) Switched OFF"
Cohesion: 0.67
Nodes (3): Executive-Level Answer, IP-Protected Technical Justification & Damper Ablation Table, Q4.3: Pre-Peak and Trough Scores with the Crash-Liquidation Damper (`Λ_Crash`) Switched OFF

### Community 82 - "Q4.5: Why Intermediate `~10%` Corrections (Early 2018 Volmageddon, Autumn 2023, Spring 2012) Were Excluded from `D1`–`D8`, and How the Model Performed on Them"
Cohesion: 0.67
Nodes (3): Executive-Level Answer, IP-Protected Technical Justification & Intermediate Correction Scorecard, Q4.5: Why Intermediate `~10%` Corrections (Early 2018 Volmageddon, Autumn 2023, Spring 2012) Were Excluded from `D1`–`D8`, and How the Model Performed on Them

### Community 83 - "Q4.1 & Q4.2: Parameter Freezing / Walk-Forward Integrity & Pre-2006 Historical Crises (`1987`, `1990`, `1998`, `2000–02`)"
Cohesion: 0.67
Nodes (3): Executive-Level Answer, IP-Protected Technical Justification & Pre-2006 Empirical Scorecard, Q4.1 & Q4.2: Parameter Freezing / Walk-Forward Integrity & Pre-2006 Historical Crises (`1987`, `1990`, `1998`, `2000–02`)

### Community 84 - "Q4.5: Why Intermediate `~10%` Corrections (Early 2018 Volmageddon, Autumn 2023, Spring 2012) Were Excluded from `D1`–`D8`, and How the Model Performed on Them"
Cohesion: 0.67
Nodes (3): Executive-Level Answer, IP-Protected Technical Justification & Intermediate Correction Scorecard, Q4.5: Why Intermediate `~10%` Corrections (Early 2018 Volmageddon, Autumn 2023, Spring 2012) Were Excluded from `D1`–`D8`, and How the Model Performed on Them

## Knowledge Gaps
- **16 isolated node(s):** `market-bubble-detector`, `Polars DataFrame Integration`, `Margin Debt Growth Velocity`, `May 2026 Month-over-Month Change (+8.53%)`, `May 2026 Margin Debt Nominal Value ($1.416T)` (+11 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 665 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **14 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `📉 Multidimensional Market Bubble Detector & Structural Break System` connect `📉 Multidimensional Market Bubble Detector & Structural Break System` to `🔬 Mathematical Formulations`, `📋 Changelog`, `📊 8 Interactive Dashboard Modules`, `💻 Local Setup & Execution Guide`?**
  _High betweenness centrality (0.027) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `DashboardState` (e.g. with `PortfolioBacktestEngine` and `DataIngestor`) actually correct?**
  _`DashboardState` has 11 INFERRED edges - model-reasoned connections that need verification._
- **What connects `market-bubble-detector`, `Polars DataFrame Integration`, `Margin Debt Growth Velocity` to the rest of the system?**
  _16 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Market Bubble Structural Analysis Report` be split into smaller, more focused modules?**
  _Cohesion score 0.07563025210084033 - nodes in this community are weakly interconnected._
- **Why does `StructuralBreakPredictor` connect `StructuralBreakPredictor` to `test_mahalanobis.py`, `precompile_wasm_parquet_datasets`, `build_mahalanobis_fig`, `.load_data`, `test_date_horizons.py`, `generate_wasm_dataset`, `pytest`, `CompositeSummaryEngine`, `dashboard.py`, `config.py`, `test_tda_wavelet_rigor.py`, `structural_breaks.py`?**
  _High betweenness centrality (0.026) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `MacroMahalanobisDetector` (e.g. with `DashboardState` and `Fixed & Enhanced (Red Team Remediation Release `RT-CRIT-01` – `RT-LOW-28`)`) actually correct?**
  _`MacroMahalanobisDetector` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `test_mahalanobis.py` be split into smaller, more focused modules?**
  _Cohesion score 0.09291521486643438 - nodes in this community are weakly interconnected._