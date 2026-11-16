# Graph Report - Merrill  (2026-11-15)

## Corpus Check
- 97 files · ~182,597 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 19 file(s) not represented in the graph (top: .parquet 9, .csv 6, (none) 2)

## Summary
- 1260 nodes · 2641 edges · 77 communities (64 shown, 13 thin omitted)
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 226 edges (avg confidence: 0.88)
- Token cost: 64,000 input · 3,600 output

## Graph Freshness
- Built from commit: `8925dcc4`
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
- Appendix B: Institutional Due-Diligence & Third-Party Technical Q&A (IP-Protected Audit)
- econometric.py
- B.4 Model Construction, Pre-2006 Crises, Damper Ablations, Parameter Sensitivity & Version Lineage
- generate_deck.py
- compute_tech_exuberance_metrics
- test_ui_ux_wasm_optimizations.py
- calculate_contrast_ratio
- dashboard.py
- B.4 Model Construction, Pre-2006 Crises, Damper Ablations, Parameter Sensitivity & Version Lineage
- HighFidelityEventStudy_Executive_Report.md
- HighFidelityEventStudy/README.md
- Appendix B: Institutional Due-Diligence & Third-Party Technical Q&A (IP-Protected Audit)
- Appendix B: Institutional Due-Diligence & Third-Party Technical Q&A (IP-Protected Audit)
- generate_high_fidelity_plots.py
- FredETL
- test_no_gaussian_bumps.py
- FinraETL
- numpy
- composite_summary.py
- test_tda_wavelet_rigor.py
- ui/__init__.py
- Changelog
- build_tech_exuberance_fig
- polars
- B.1 False Alarms & Full-Period Behavior Outside the Eight Peaks (2006–2026)
- System Architecture and Operational Rules for Agents
- 📊 8 Interactive Dashboard Modules
- config.py
- panel_dashboard.py
- sw.js
- B.1 False Alarms & Full-Period Behavior Outside the Eight Peaks (2006–2026)
- DataIngestor
- test_wasm_pyodide_sandbox.py
- 📉 Multidimensional Market Bubble Detector & Structural Break System
- 🔬 Mathematical Formulations
- Appendix: Architectural Principles & Methodological Justification (IP-Protected Technical Overview)
- compute_tda_wavelet_complexity
- Section 1: Executive Summary of the Composite Indicators & Strategic Mandate
- High-Fidelity 20-Year Dislocation Event Study & Composite Regime Synthesis (2006–2026)
- Section 2: Scale-Invariant Log-Growth Trajectory & Dual-Phase Dislocation Corridors
- Section 3: 8-Dislocation Popperian Falsification & Peak-vs-Trough Regime Separation
- Section 4: Homotopic Phase-Time Superposed Epoch Analysis Across Dislocation Cycles
- Section 5: Institutional Capital Preservation & Early-Warning Lead Cushion Profile
- compute_validation_summary_statistics
- Appendix A: Architectural Principles & Methodological Justification (IP-Protected Technical Overview)
- B.6 Current Live Readings (`November 13, 2026`) & Role of the Knowledge-Graph Engine
- Appendix A: Architectural Principles & Methodological Justification (IP-Protected Technical Overview)
- B.6 Current Live Readings (`November 13, 2026`) & Role of the Knowledge-Graph Engine
- 💻 Local Setup & Execution Guide
- _prepare_trace
- features/__init__.py
- [v2.1.0] - 2026-09-02
- Section 1: Executive Summary of the Composite Indicators & Strategic Mandate
- Section 1: Executive Summary of the Composite Indicators & Strategic Mandate
- Section 2: Scale-Invariant Log-Growth Trajectory & Dual-Phase Dislocation Corridors
- Section 3: 8-Dislocation Popperian Falsification & Peak-vs-Trough Regime Separation
- Section 5: Institutional Capital Preservation & Early-Warning Lead Cushion Profile
- Section 2: Scale-Invariant Log-Growth Trajectory & Dual-Phase Dislocation Corridors
- Section 3: 8-Dislocation Popperian Falsification & Peak-vs-Trough Regime Separation
- Section 5: Institutional Capital Preservation & Early-Warning Lead Cushion Profile

## God Nodes (most connected - your core abstractions)
1. `DashboardState` - 51 edges
2. `MacroMahalanobisDetector` - 37 edges
3. `generate_wasm_dataset()` - 31 edges
4. `DataIngestor` - 31 edges
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
- `Added` --references--> `compute_exuberance_spans()`  [INFERRED]
  CHANGELOG.md → bubble_detector/features/tech_exuberance.py
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

## Communities (77 total, 13 thin omitted)

### Community 0 - "Market Bubble Structural Analysis Report"
Cohesion: 0.08
Nodes (35): NiceGUI Layout & Plotly Dashboard, Data Ingestion (DataIngestor), AGVI Implementation Plan Document, Feature Engineering Pipeline, XGBoost Model Training & Walk-Forward CV, AGVI Technical Specification Document, NiceGUI Dashboard UI, Polars DataFrame Integration (+27 more)

### Community 1 - "test_mahalanobis.py"
Cohesion: 0.06
Nodes (18): compute_macro_valuations(), fast_ledoit_wolf_cov(), MacroMahalanobisDetector, test_compute_macro_valuations(), test_drawdown_probability_not_in_covariance(), test_p_cape_elimination(), mock_indicators_df(), test_anomaly_driver_attribution() (+10 more)

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
Cohesion: 0.17
Nodes (16): build_composite_summary_fig(), build_dislocation_fidelity_fig(), build_econometric_fig(), build_leverage_fig(), build_macro_valuation_fig(), build_mahalanobis_fig(), _build_packaging_proxy_fig(), build_sector_health_fig() (+8 more)

### Community 6 - "StructuralBreakPredictor"
Cohesion: 0.05
Nodes (20): BubbleDetectorError, DataFetchError, ModelTrainingError, ValidationError, StructuralBreakPredictor, 10. Institutional Code Commentary, Packaging & Agent Navigation:, 1. System, Configuration & Date Horizons (`config.py` & `date_horizons.py`):, 3. Data Ingestion & Storage (`ingestor.py`): (+12 more)

### Community 8 - "Appendix B: Institutional Due-Diligence & Third-Party Technical Q&A (IP-Protected Audit)"
Cohesion: 0.04
Nodes (45): Appendix B: Institutional Due-Diligence & Third-Party Technical Q&A (IP-Protected Audit), B.1 False Alarms & Full-Period Behavior Outside the Eight Peaks (2006–2026), B.2 Lead Times, Window Caps & Pre-Peak Duty Cycles, B.3 Defensive Backtest Mechanics, Re-Entry Causality & Actual Treasury-Bill Rerun, B.4 Model Construction, Pre-2006 Crises, Damper Ablations, Parameter Sensitivity & Version Lineage, B.5 Resolution of Report & Chart Conventions Flagged in Section 5 (`v1.2.0` Harmonization), B.6 Current Live Readings (`November 13, 2026`) & Role of the Knowledge-Graph Engine, Executive-Level Answer (+37 more)

### Community 9 - "econometric.py"
Cohesion: 0.17
Nodes (5): _batch_adf_from_log_windows(), _in_window_coint_adf(), compute_wild_bootstrap_critical_values(), _rolling_adf_vectorized(), test_wild_bootstrap_critical_value_bounds()

### Community 11 - "B.4 Model Construction, Pre-2006 Crises, Damper Ablations, Parameter Sensitivity & Version Lineage"
Cohesion: 0.13
Nodes (15): B.4 Model Construction, Pre-2006 Crises, Damper Ablations, Parameter Sensitivity & Version Lineage, Executive-Level Answer, Executive-Level Answer, Executive-Level Answer, Executive-Level Answer, Executive-Level Answer, IP-Protected Technical Justification & Damper Ablation Table, IP-Protected Technical Justification & Intermediate Correction Scorecard (+7 more)

### Community 12 - "generate_deck.py"
Cohesion: 0.20
Nodes (3): create_presentation(), add_card(), add_metric_badge()

### Community 13 - "compute_tech_exuberance_metrics"
Cohesion: 0.14
Nodes (7): compute_exuberance_spans(), compute_tech_exuberance_metrics(), test_spy_backward_compounding_no_cliff(), test_vxo_vix_seam_continuity(), test_xlk_backward_compounding_no_cliff(), test_compute_exuberance_spans(), test_dual_conditions_logic()

### Community 14 - "test_ui_ux_wasm_optimizations.py"
Cohesion: 0.17
Nodes (5): test_keyboard_operability_and_aria_landmarks(), test_responsive_legend_layout_logic(), test_service_worker_file_validity(), test_wasm_build_packaging_html_size(), test_wasm_dependency_version_locking_and_resilience_bridge()

### Community 16 - "calculate_contrast_ratio"
Cohesion: 0.08
Nodes (19): calculate_contrast_ratio(), get_plotly_template(), is_wcag_aa_compliant(), parse_hex_color(), relative_luminance(), 2. UI & Accessibility Engine (`ui_theme.py`):, test_ui_theme_alias_parity(), test_contrast_ratio_calculation() (+11 more)

### Community 17 - "dashboard.py"
Cohesion: 0.05
Nodes (40): PortfolioBacktestEngine, build_composite_summary_chart(), build_composite_validation_chart(), build_dislocation_fidelity_chart(), build_econometric_chart(), build_leverage_chart(), build_macro_valuation_chart(), build_mahalanobis_chart() (+32 more)

### Community 18 - "B.4 Model Construction, Pre-2006 Crises, Damper Ablations, Parameter Sensitivity & Version Lineage"
Cohesion: 0.13
Nodes (15): B.4 Model Construction, Pre-2006 Crises, Damper Ablations, Parameter Sensitivity & Version Lineage, Executive-Level Answer, Executive-Level Answer, Executive-Level Answer, Executive-Level Answer, Executive-Level Answer, IP-Protected Technical Justification & Damper Ablation Table, IP-Protected Technical Justification & Intermediate Correction Scorecard (+7 more)

### Community 19 - "HighFidelityEventStudy_Executive_Report.md"
Cohesion: 0.22
Nodes (8): 4.1 Executive Explanation of the Composite Indicator in This View, 4.2 High-Resolution 4K Visualization: Homotopic Phase-Time Analysis (`4096 × 3072`), 4.3 Detailed Walkthrough of the Plot, Axes & Labeled Callouts, Document Changelog (SemVer), Executive Summary Abstract, High-Fidelity 20-Year Dislocation Event Study & Composite Regime Synthesis (2006–2026), Section 4: Homotopic Phase-Time Superposed Epoch Analysis Across Dislocation Cycles, Table of Contents

### Community 20 - "HighFidelityEventStudy/README.md"
Cohesion: 0.22
Nodes (8): 4.1 Executive Explanation of the Composite Indicator in This View, 4.2 High-Resolution 4K Visualization: Homotopic Phase-Time Analysis (`4096 × 3072`), 4.3 Detailed Walkthrough of the Plot, Axes & Labeled Callouts, Document Changelog (SemVer), Executive Summary Abstract, High-Fidelity 20-Year Dislocation Event Study & Composite Regime Synthesis (2006–2026), Section 4: Homotopic Phase-Time Superposed Epoch Analysis Across Dislocation Cycles, Table of Contents

### Community 21 - "Appendix B: Institutional Due-Diligence & Third-Party Technical Q&A (IP-Protected Audit)"
Cohesion: 0.15
Nodes (13): Appendix B: Institutional Due-Diligence & Third-Party Technical Q&A (IP-Protected Audit), B.2 Lead Times, Window Caps & Pre-Peak Duty Cycles, B.3 Defensive Backtest Mechanics, Re-Entry Causality & Actual Treasury-Bill Rerun, B.5 Resolution of Report & Chart Conventions Flagged in Section 5 (`v1.2.0` Harmonization), Executive-Level Answer, Executive-Level Answer, Executive-Level Answer, Executive-Level Summary of All Six Harmonizations Applied in `v1.2.0` (+5 more)

### Community 22 - "Appendix B: Institutional Due-Diligence & Third-Party Technical Q&A (IP-Protected Audit)"
Cohesion: 0.15
Nodes (13): Appendix B: Institutional Due-Diligence & Third-Party Technical Q&A (IP-Protected Audit), B.2 Lead Times, Window Caps & Pre-Peak Duty Cycles, B.3 Defensive Backtest Mechanics, Re-Entry Causality & Actual Treasury-Bill Rerun, B.5 Resolution of Report & Chart Conventions Flagged in Section 5 (`v1.2.0` Harmonization), Executive-Level Answer, Executive-Level Answer, Executive-Level Answer, Executive-Level Summary of All Six Harmonizations Applied in `v1.2.0` (+5 more)

### Community 23 - "generate_high_fidelity_plots.py"
Cohesion: 0.17
Nodes (8): get_palette(), main(), plot_1_scale_invariant_log_growth(), plot_2_popperian_regime_separation(), plot_3_homotopic_phase_time(), plot_4_dislocation_capital(), save_and_verify_4k(), style_axes_common()

### Community 24 - "FredETL"
Cohesion: 0.11
Nodes (8): FredETL, get_fred_data(), parse_fred_macro_series(), test_fred_publication_lags(), test_central_bank_balance_sheet_splicing_continuity(), test_global_liquidity_derived_metrics(), test_global_liquidity_schema_and_publication_lags(), test_authentic_fred_gdp_and_housing()

### Community 25 - "test_no_gaussian_bumps.py"
Cohesion: 0.15
Nodes (5): get_shiller_data(), parse_shiller_excel(), ShillerETL, test_shiller_provenance_schema_and_bounds(), test_authentic_shiller_provenance_workbook()

### Community 26 - "FinraETL"
Cohesion: 0.12
Nodes (9): FinraETL, get_finra_margin_debt(), parse_finra_margin_debt_series(), precompile_wasm_parquet_datasets(), _serialize_df_to_json_dict(), stage_all(), sync_parquet_to_json(), test_finra_margin_publication_lag() (+1 more)

### Community 27 - "numpy"
Cohesion: 0.07
Nodes (15): compute_gsadf_gpt_decomposition(), calibrate_lppls_filimonov(), compute_lppls_confidence_indicator(), _get_lppls_grid(), test_adf_lag_selection_k0_vs_k1(), test_adf_stat_explosive_vs_stationary(), test_recursive_backward_supremum_grid(), test_compute_gsadf_gpt_decomposition() (+7 more)

### Community 28 - "composite_summary.py"
Cohesion: 0.06
Nodes (20): build_band_polygon(), causal_ffill_clean(), causal_gram_schmidt(), causal_stationary_unit_variance(), CompositeSummaryEngine, compute_composite_validation_metrics(), compute_dislocation_fidelity_metrics(), compute_orthogonal_basis_and_summaries_numpy() (+12 more)

### Community 29 - "test_tda_wavelet_rigor.py"
Cohesion: 0.13
Nodes (9): _compute_morlet_wavelet_energy_and_entropy(), _compute_persistence_landscape_and_entropy(), _compute_rips_persistence_diagrams(), _get_morlet_toeplitz_matrices(), _takens_embedding(), test_bubenik_l2_norm_and_persistence_entropy(), test_morlet_wavelet_scaleogram_and_spectral_entropy(), test_persistence_entropy_herding_collapse() (+1 more)

### Community 31 - "Changelog"
Cohesion: 0.05
Nodes (25): postprocess_wasm_content(), clean_bokeh_templates(), postprocess_wasm_html(), sync_wasm_build_directories(), [3.0.0] - 2026-09-03, [3.1.0] - 2026-10-05, [3.2.0] - 2026-11-03, [3.3.0] - 2026-11-05 (+17 more)

### Community 33 - "build_tech_exuberance_fig"
Cohesion: 0.15
Nodes (7): build_tech_exuberance_fig(), test_pane_tech_exuberance_in_dashboard_tabs(), test_precompile_wasm_parquet_datasets(), test_tech_exuberance_columns_in_core_wasm(), test_tech_exuberance_fig_structure_desktop(), test_tech_exuberance_fig_structure_mobile(), test_tech_exuberance_fig_structure_option_3()

### Community 34 - "polars"
Cohesion: 0.05
Nodes (14): IndicatorComputationError, compute_margin_leverage_metrics(), compute_options_volatility_metrics(), compute_technical_indicators(), ensure_synchronized_wasm_datasets(), market_simulation_df(), test_strictly_causal_one_day_execution_lag(), test_compute_margin_leverage_metrics() (+6 more)

### Community 35 - "B.1 False Alarms & Full-Period Behavior Outside the Eight Peaks (2006–2026)"
Cohesion: 0.20
Nodes (10): B.1 False Alarms & Full-Period Behavior Outside the Eight Peaks (2006–2026), Executive-Level Answer, Executive-Level Answer, Executive-Level Answer, IP-Protected Technical Justification, IP-Protected Technical Justification & Complete 66-Crossing Audit Table, IP-Protected Technical Justification & Year-by-Year Audit, Q1.1 & Q1.2: Full-Period Daily Score Distribution (2006–2026) & Share of Days at or Above `70.0%` (+2 more)

### Community 36 - "System Architecture and Operational Rules for Agents"
Cohesion: 0.40
Nodes (4): 1. Core Econometric & Statistical Rules, 2. Directory Layout & Key Modules, 3. Execution & Verification Rules, System Architecture and Operational Rules for Agents

### Community 37 - "📊 8 Interactive Dashboard Modules"
Cohesion: 0.22
Nodes (9): 1. Macro Valuation Anchors, 2. Systemic Liquidity & Leverage, 3. Econometric Explosive Bubble Diagnostics, 4. Options Sentiment & Behavioral Tracking, 5. Sector Vulnerability & Topological Dynamics, 6. Signed Macro Mahalanobis Distance & Dynamic Equity Exposure, 7. Tech Exuberance Score: Macro Decoupling vs Statistical Singularity, 8. Composite Summary Indicators: Information-Maximizing Orthogonal Synthesis ($\mathcal{B}_{13}^{\perp}$) (+1 more)

### Community 38 - "config.py"
Cohesion: 0.10
Nodes (5): get_vxo_data(), parse_authentic_vxo_series(), VxoETL, test_vxo_authenticity_and_black_monday(), test_authentic_cboe_vxo_black_monday()

### Community 39 - "panel_dashboard.py"
Cohesion: 0.13
Nodes (8): build_band_polygon(), build_composite_validation_fig(), compute_composite_validation_metrics(), compute_dislocation_fidelity_metrics(), get_current_date(), get_dynamic_50yr_date_range(), get_dynamic_horizon_metadata(), precompile_wasm_parquet_datasets()

### Community 41 - "B.1 False Alarms & Full-Period Behavior Outside the Eight Peaks (2006–2026)"
Cohesion: 0.20
Nodes (10): B.1 False Alarms & Full-Period Behavior Outside the Eight Peaks (2006–2026), Executive-Level Answer, Executive-Level Answer, Executive-Level Answer, IP-Protected Technical Justification, IP-Protected Technical Justification & Complete 66-Crossing Audit Table, IP-Protected Technical Justification & Year-by-Year Audit, Q1.1 & Q1.2: Full-Period Daily Score Distribution (2006–2026) & Share of Days at or Above `70.0%` (+2 more)

### Community 42 - "DataIngestor"
Cohesion: 0.06
Nodes (19): clamp_to_trading_day(), get_current_date(), get_dynamic_50yr_date_range(), get_dynamic_horizon_metadata(), DataIngestor, ingestor(), test_dynamic_50yr_date_generator(), test_option_1_50yr_data_ingestion() (+11 more)

### Community 43 - "test_wasm_pyodide_sandbox.py"
Cohesion: 0.09
Nodes (7): apply_postprocessing(), test_dist_index_html_on_disk(), test_dist_index_html_postprocessing_idempotence(), test_json_datasets_staging(), test_template_and_cards_reconstruction(), test_wasm_full_script_pure_numpy_fallback_execution(), test_wasm_full_script_pyodide_execution()

### Community 46 - "📉 Multidimensional Market Bubble Detector & Structural Break System"
Cohesion: 0.25
Nodes (7): Benchmark Comparison (50-Year Multi-Decade Horizon), 📅 Dynamic 50-Year Multi-Horizon Date Engine, 🎯 Falsifiable Historical Peak Validation Event Study, 📈 Institutional Cost-Inclusive Portfolio Backtest, 📜 License, 🌟 Live Interactive WebAssembly Dashboard, 📉 Multidimensional Market Bubble Detector & Structural Break System

### Community 47 - "🔬 Mathematical Formulations"
Cohesion: 0.25
Nodes (8): 1. Continuous Backward Compounding (Cliff Eradication), 2. Signed Macro Mahalanobis Distance & Directional Projection, 3. Dynamic Portfolio Equity Sizing ($w_{\text{equity}}$), 4. Canonical PSY Recursive Right-Tailed Unit Root Testing (GSADF / BSADF), 5. Topological Data Analysis (TDA) & Wavelet Spectral Entropy, 6. Log-Periodic Power Law Singularity (LPPLS) Subordination Model, 7. Global Liquidity Index & Dual-Condition Conjoint Exuberance, 🔬 Mathematical Formulations

### Community 48 - "Appendix: Architectural Principles & Methodological Justification (IP-Protected Technical Overview)"
Cohesion: 0.25
Nodes (7): A.1 Scope & Intellectual Property Boundary, A.2 Stage I: Eliminating Look-Ahead Bias & Non-Stationary Drift via Strictly Causal Standardization, A.3 Stage II: Eliminating Multicollinearity via Sequential Cross-Domain Orthogonalization, A.4 Stage III: Structural Mechanics of the Five Complementary Summary Engines, A.5 Stage IV: Directional Polarity Alignment & The Crash-Liquidation Damper, A.6 License & Confidentiality Attestation, Appendix A: Architectural Principles & Methodological Justification (IP-Protected Technical Overview)

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
Cohesion: 0.09
Nodes (7): BacktestResult, _compute_empirical_false_alarm_rate(), compute_validation_summary_statistics(), generate_historical_validation_table(), _date_seeded_normals(), [3.7.0] - 2026-11-15, Fixed & Enhanced (Red Team Remediation Release `RT-CRIT-01` – `RT-LOW-28`)

### Community 59 - "Appendix A: Architectural Principles & Methodological Justification (IP-Protected Technical Overview)"
Cohesion: 0.29
Nodes (7): A.1 Scope & Intellectual Property Boundary, A.2 Stage I: Eliminating Look-Ahead Bias & Non-Stationary Drift via Strictly Causal Standardization, A.3 Stage II: Eliminating Multicollinearity via Sequential Cross-Domain Orthogonalization, A.4 Stage III: Structural Mechanics of the Five Complementary Summary Engines, A.5 Stage IV: Directional Polarity Alignment & The Crash-Liquidation Damper, A.6 License & Confidentiality Attestation, Appendix A: Architectural Principles & Methodological Justification (IP-Protected Technical Overview)

### Community 60 - "B.6 Current Live Readings (`November 13, 2026`) & Role of the Knowledge-Graph Engine"
Cohesion: 0.29
Nodes (7): B.6 Current Live Readings (`November 13, 2026`) & Role of the Knowledge-Graph Engine, Executive-Level Answer, Executive-Level Answer, IP-Protected Technical Justification, IP-Protected Technical Justification & Live November 13, 2026 Telemetry Table, Q6.1: What Is the Master Score Today (`November 13, 2026`)?, Q6.2: Does the Knowledge-Graph Engine (`graphify`) Feed the Quantitative Signal at All?

### Community 61 - "Appendix A: Architectural Principles & Methodological Justification (IP-Protected Technical Overview)"
Cohesion: 0.29
Nodes (7): A.1 Scope & Intellectual Property Boundary, A.2 Stage I: Eliminating Look-Ahead Bias & Non-Stationary Drift via Strictly Causal Standardization, A.3 Stage II: Eliminating Multicollinearity via Sequential Cross-Domain Orthogonalization, A.4 Stage III: Structural Mechanics of the Five Complementary Summary Engines, A.5 Stage IV: Directional Polarity Alignment & The Crash-Liquidation Damper, A.6 License & Confidentiality Attestation, Appendix A: Architectural Principles & Methodological Justification (IP-Protected Technical Overview)

### Community 62 - "B.6 Current Live Readings (`November 13, 2026`) & Role of the Knowledge-Graph Engine"
Cohesion: 0.29
Nodes (7): B.6 Current Live Readings (`November 13, 2026`) & Role of the Knowledge-Graph Engine, Executive-Level Answer, Executive-Level Answer, IP-Protected Technical Justification, IP-Protected Technical Justification & Live November 13, 2026 Telemetry Table, Q6.1: What Is the Master Score Today (`November 13, 2026`)?, Q6.2: Does the Knowledge-Graph Engine (`graphify`) Feed the Quantitative Signal at All?

### Community 63 - "💻 Local Setup & Execution Guide"
Cohesion: 0.29
Nodes (7): 1. Prerequisites & Virtual Environment, 2. Run the High-Performance NiceGUI Application, 3. Run the Local HoloViz Panel Dashboard, 4. Build and Run Client-Side WebAssembly (Pyodide), 5. Run the Automated Test Suite, 6. Synchronize Repository Knowledge Graph, 💻 Local Setup & Execution Guide

### Community 64 - "_prepare_trace"
Cohesion: 0.40
Nodes (3): lttb_downsample(), normalize_tda_indicator(), _prepare_trace()

### Community 65 - "features/__init__.py"
Cohesion: 0.18
Nodes (6): calculate_adf_stat(), lttb_downsample(), normalize_tda_indicator(), takens_embedding(), Added, test_lttb_downsample_edge_cases()

### Community 66 - "[v2.1.0] - 2026-09-02"
Cohesion: 0.67
Nodes (3): Added, Fixed, [v2.1.0] - 2026-09-02

### Community 67 - "Section 1: Executive Summary of the Composite Indicators & Strategic Mandate"
Cohesion: 0.40
Nodes (5): 1.1 The Core Institutional Challenge: Information Redundancy vs. Structural Blind Spots, 1.2 Our Ultimate Strategic Goal: Maximum Information Extraction & Asymmetric Capital Defense, 1.3 Overview of the Five Complementary Composite Summary Indicators, 1.4 High-Level Empirical Scorecard Across the 20-Year Horizon (2006–2026), Section 1: Executive Summary of the Composite Indicators & Strategic Mandate

### Community 68 - "Section 1: Executive Summary of the Composite Indicators & Strategic Mandate"
Cohesion: 0.40
Nodes (5): 1.1 The Core Institutional Challenge: Information Redundancy vs. Structural Blind Spots, 1.2 Our Ultimate Strategic Goal: Maximum Information Extraction & Asymmetric Capital Defense, 1.3 Overview of the Five Complementary Composite Summary Indicators, 1.4 High-Level Empirical Scorecard Across the 20-Year Horizon (2006–2026), Section 1: Executive Summary of the Composite Indicators & Strategic Mandate

### Community 69 - "Section 2: Scale-Invariant Log-Growth Trajectory & Dual-Phase Dislocation Corridors"
Cohesion: 0.50
Nodes (4): 2.1 Executive Explanation of the Composite Indicator in This View, 2.2 High-Resolution 4K Visualization: Scale-Invariant Log-Growth (`4096 × 3072`), 2.3 Detailed Walkthrough of the Plot, Axes & Labeled Callouts, Section 2: Scale-Invariant Log-Growth Trajectory & Dual-Phase Dislocation Corridors

### Community 70 - "Section 3: 8-Dislocation Popperian Falsification & Peak-vs-Trough Regime Separation"
Cohesion: 0.50
Nodes (4): 3.1 Executive Explanation of the Composite Indicator in This View, 3.2 High-Resolution 4K Visualization: 8-Dislocation Popperian Matrix (`4096 × 3072`), 3.3 Detailed Walkthrough of the Plot, Axes & Labeled Callouts, Section 3: 8-Dislocation Popperian Falsification & Peak-vs-Trough Regime Separation

### Community 71 - "Section 5: Institutional Capital Preservation & Early-Warning Lead Cushion Profile"
Cohesion: 0.50
Nodes (4): 5.1 Executive Explanation of the Composite Indicator in This View, 5.2 High-Resolution 4K Visualization: Dislocation Capital Preservation (`4096 × 3072`), 5.3 Detailed Walkthrough of the Plot, Axes & Labeled Callouts, Section 5: Institutional Capital Preservation & Early-Warning Lead Cushion Profile

### Community 72 - "Section 2: Scale-Invariant Log-Growth Trajectory & Dual-Phase Dislocation Corridors"
Cohesion: 0.50
Nodes (4): 2.1 Executive Explanation of the Composite Indicator in This View, 2.2 High-Resolution 4K Visualization: Scale-Invariant Log-Growth (`4096 × 3072`), 2.3 Detailed Walkthrough of the Plot, Axes & Labeled Callouts, Section 2: Scale-Invariant Log-Growth Trajectory & Dual-Phase Dislocation Corridors

### Community 73 - "Section 3: 8-Dislocation Popperian Falsification & Peak-vs-Trough Regime Separation"
Cohesion: 0.50
Nodes (4): 3.1 Executive Explanation of the Composite Indicator in This View, 3.2 High-Resolution 4K Visualization: 8-Dislocation Popperian Matrix (`4096 × 3072`), 3.3 Detailed Walkthrough of the Plot, Axes & Labeled Callouts, Section 3: 8-Dislocation Popperian Falsification & Peak-vs-Trough Regime Separation

### Community 74 - "Section 5: Institutional Capital Preservation & Early-Warning Lead Cushion Profile"
Cohesion: 0.50
Nodes (4): 5.1 Executive Explanation of the Composite Indicator in This View, 5.2 High-Resolution 4K Visualization: Dislocation Capital Preservation (`4096 × 3072`), 5.3 Detailed Walkthrough of the Plot, Axes & Labeled Callouts, Section 5: Institutional Capital Preservation & Early-Warning Lead Cushion Profile

## Knowledge Gaps
- **16 isolated node(s):** `market-bubble-detector`, `Polars DataFrame Integration`, `Margin Debt Growth Velocity`, `May 2026 Month-over-Month Change (+8.53%)`, `May 2026 Margin Debt Nominal Value ($1.416T)` (+11 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 652 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **13 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `MacroMahalanobisDetector` connect `test_mahalanobis.py` to `panel_dashboard.py`, `DataIngestor`, `dashboard.py`, `compute_validation_summary_statistics`, `FinraETL`, `composite_summary.py`?**
  _High betweenness centrality (0.035) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `DashboardState` (e.g. with `PortfolioBacktestEngine` and `DataIngestor`) actually correct?**
  _`DashboardState` has 11 INFERRED edges - model-reasoned connections that need verification._
- **What connects `market-bubble-detector`, `Polars DataFrame Integration`, `Margin Debt Growth Velocity` to the rest of the system?**
  _16 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Market Bubble Structural Analysis Report` be split into smaller, more focused modules?**
  _Cohesion score 0.07563025210084033 - nodes in this community are weakly interconnected._
- **Why does `DashboardState` connect `dashboard.py` to `test_mahalanobis.py`, `polars`, `StructuralBreakPredictor`, `DataIngestor`, `calculate_contrast_ratio`, `generate_high_fidelity_plots.py`, `numpy`, `composite_summary.py`, `ui/__init__.py`?**
  _High betweenness centrality (0.028) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `MacroMahalanobisDetector` (e.g. with `DashboardState` and `Fixed & Enhanced (Red Team Remediation Release `RT-CRIT-01` – `RT-LOW-28`)`) actually correct?**
  _`MacroMahalanobisDetector` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `test_mahalanobis.py` be split into smaller, more focused modules?**
  _Cohesion score 0.060451977401129946 - nodes in this community are weakly interconnected._