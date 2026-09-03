# Graph Report - Merrill  (2026-09-02)

## Corpus Check
- 41 files · ~64,507 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 361 nodes · 643 edges · 18 communities (17 shown, 1 thin omitted)
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 31 edges (avg confidence: 0.78)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `9d9e8ff7`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Merrill ETF Portfolio Reviews
- AGVI System Pipeline and Dashboard
- Econometric Bubble Detection Models
- Implied Volatility Term Structure Metrics
- Graphify Settings and Rules
- Valuation and Feature Engineering
- FINRA Margin Debt Metrics
- Systemic Leverage Analysis
- test_ui_theme.py
- __init__.py
- Overview of Completed Implementation
- Detailed Slide Breakdown by Section & Group
- .fetch_market_data
- panel_dashboard.py

## God Nodes (most connected - your core abstractions)
1. `DashboardState` - 30 edges
2. `DataIngestor` - 25 edges
3. `MacroMahalanobisDetector` - 22 edges
4. `StructuralBreakPredictor` - 19 edges
5. `compute_tda_wavelet_complexity()` - 17 edges
6. `generate_wasm_dataset()` - 16 edges
7. `compute_gsadf_gpt_decomposition()` - 15 edges
8. `compute_margin_leverage_metrics()` - 14 edges
9. `compute_macro_valuations()` - 14 edges
10. `compute_options_volatility_metrics()` - 14 edges

## Surprising Connections (you probably didn't know these)
- `Joint ETF Strategy Portfolio (March 2026)` --conceptually_related_to--> `Real Estate Valuation Metrics`  [INFERRED]
  CRC_185050992_20260402.pdf → MarketBubble_DDFv100.md
- `Joint ETF Strategy Portfolio (May 2026)` --conceptually_related_to--> `Real Estate Valuation Metrics`  [INFERRED]
  CRC_185865214_20260502.pdf → MarketBubble_DDFv100.md
- `Joint ETF Strategy Portfolio (June 2, 2026)` --conceptually_related_to--> `Real Estate Valuation Metrics`  [INFERRED]
  CRC_186566428_20260602.pdf → MarketBubble_DDFv100.md
- `Joint ETF Strategy Portfolio (June 29, 2026)` --conceptually_related_to--> `Real Estate Valuation Metrics`  [INFERRED]
  CRC_187083673_20260629.pdf → MarketBubble_DDFv100.md
- `Joint ETF Strategy Portfolio (March 2026)` --conceptually_related_to--> `Technology & Semiconductors Sector`  [INFERRED]
  CRC_185050992_20260402.pdf → MarketBubble_DDFv100.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Client Portfolio Performance History (Q2 2026)** — crc_185050992_20260402_joint_etf_strategy, crc_185865214_20260502_joint_etf_strategy, crc_186566428_20260602_joint_etf_strategy, crc_187083673_20260629_joint_etf_strategy [INFERRED 0.95]
- **Econometric and Mathematical Bubble Detection Framework** — marketbubble_ddfv100_gsadf_psy_procedure, marketbubble_ddfv100_tda_wavelet, marketbubble_ddfv100_lppls_model [EXTRACTED 1.00]
- **AGVI Indicator and Feature Engineering Pipeline** — marketbubble_ddfv100_shiller_cape_ratio, marketbubble_ddfv100_payout_adjusted_cape, marketbubble_ddfv100_buffett_indicator, marketbubble_ddfv100_gsadf_psy_procedure [EXTRACTED 1.00]
- **FINRA Margin Debt Metrics** — finra_margin_debt_tracker, finra_may_2026_nominal_value, finra_may_2026_mom_change, finra_may_2026_yoy_change [INFERRED 0.85]
- **Implied Volatility Term Structure Components** — impliedvolatilitymetric_vix1d, impliedvolatilitymetric_vix_spot, impliedvolatilitymetric_vix3m, impliedvolatilitymetric_vix1y [EXTRACTED 1.00]

## Communities (18 total, 1 thin omitted)

### Community 0 - "Merrill ETF Portfolio Reviews"
Cohesion: 0.12
Nodes (27): Feature Engineering Pipeline, TA-Lib Technical Indicators, Merrill Quarterly Performance Review - April 2026, Joint ETF Strategy Portfolio (March 2026), Merrill Quarterly Performance Review - May 2026, Joint ETF Strategy Portfolio (May 2026), Merrill Quarterly Performance Review - June 2, 2026, Joint ETF Strategy Portfolio (June 2, 2026) (+19 more)

### Community 1 - "AGVI System Pipeline and Dashboard"
Cohesion: 0.09
Nodes (23): Machine Learning Models Module, MacroMahalanobisDetector, DataFrame, ndarray, Macro Mahalanobis Distance Regime-Switching Bubble Detector.  Implements Method, Convert Mahalanobis Distance into empirical [0.0, 1.0] Bubble Regime Probability, Compute continuous portfolio equity sizing from Bubble Regime Probability., Identify top individual indicator anomaly contributors for each time step. (+15 more)

### Community 2 - "Econometric Bubble Detection Models"
Cohesion: 0.06
Nodes (48): _calculate_adf_stat(), compute_gsadf_gpt_decomposition(), DataFrame, ndarray, Econometric Bubble Detection Module.  Implements the PSY procedure (GSADF test s, Calculate Augmented Dickey-Fuller t-statistic for explosive root testing., Computes rolling GSADF explosive test statistics and GPT-adjusted fundamental de, Feature Engineering Module (+40 more)

### Community 3 - "Implied Volatility Term Structure Metrics"
Cohesion: 0.60
Nodes (6): Implied Volatility Metrics Table (July 2026), Implied Volatility Term Structure (Upward Sloping), VIX1D (8.73 - 11.61): Extreme near-term calm, VIX1Y (~23.00): Elevated long-term risk premium, VIX3M (~19.00): Anticipation of future turbulence, VIX Spot (15.57 - 17.16): Low baseline fear

### Community 4 - "Graphify Settings and Rules"
Cohesion: 0.06
Nodes (43): BubbleDetectorError, DataFetchError, get_current_date(), get_dynamic_50yr_date_range(), get_dynamic_horizon_metadata(), IndicatorComputationError, ModelTrainingError, Any (+35 more)

### Community 5 - "Valuation and Feature Engineering"
Cohesion: 0.08
Nodes (41): create_cta_banner(), create_ios_card(), UI Components Module.  Provides iOS 13+ card containers, segmented control tab w, Renders a Call-To-Action (CTA) section with powerful typography (600-800 weight), Creates an iOS 13+ inset card container with subtle shadow, rounded corners,, build_econometric_chart(), build_leverage_chart(), build_macro_valuation_chart() (+33 more)

### Community 6 - "FINRA Margin Debt Metrics"
Cohesion: 0.29
Nodes (7): DataFrame, ndarray, Predict structural break drawdown probabilities for input dataframe., Predicts market structural break and drawdown probabilities using Gradient Boost, Extract features and construct forward drawdown target variable., Train ML model using expanding window TimeSeriesSplit cross-validation., StructuralBreakPredictor

### Community 7 - "Systemic Leverage Analysis"
Cohesion: 0.12
Nodes (19): Graphify Rules Document, Graphify Query Rule, Graphify Workflow Document, NiceGUI Layout & Plotly Dashboard, Data Ingestion (DataIngestor), AGVI Implementation Plan Document, XGBoost Model Training & Walk-Forward CV, AGVI Technical Specification Document (+11 more)

### Community 8 - "test_ui_theme.py"
Cohesion: 0.16
Nodes (16): calculate_contrast_ratio(), get_theme_css(), is_wcag_aa_compliant(), parse_hex_color(), UI Theme and Accessibility Design System for Bubble Detector.  Enforces: - WCAG, Generate dynamic CSS variables and global stylesheet enforcing UI/UX & accessibi, Parse hex color string (e.g., '#007AFF' or '#000') into RGB floats [0..1]., Calculate WCAG 2.2 relative luminance for RGB floats [0..1]. (+8 more)

### Community 11 - "Overview of Completed Implementation"
Cohesion: 0.25
Nodes (7): 1. System & Logging Setup (`config.py`):, 2. UI & Accessibility Engine (`ui_theme.py`):, 3. Data Ingestion & Storage (`ingestor.py`):, 4. Quantitative Indicator Modules (`features/`):, 5. Machine Learning Model (`structural_breaks.py`):, 6. Interactive Dashboard & Components (`dashboard.py` & `components.py`):, Overview of Completed Implementation

### Community 13 - "Detailed Slide Breakdown by Section & Group"
Cohesion: 0.20
Nodes (9): Detailed Slide Breakdown by Section & Group, Executive Presentation Deck Overview, Group 1: Key Findings (Group Confidence Score: 0.94), Group 2: Supporting Evidence: Valuation, Econometrics & ML (Group Confidence Score: 0.93), Group 3: Sector Specific Application: Tech vs. Energy (Group Confidence Score: 0.91), Group 4: Implications for Systemic Stability (Group Confidence Score: 0.95), Group 5: Strategic Recommendations (Group Confidence Score: 0.96), Verification Results (+1 more)

### Community 16 - ".fetch_market_data"
Cohesion: 0.07
Nodes (27): 1. Macro Mahalanobis Distance & Dynamic Exposure Sizing, 1. Macro Valuation Anchors, 1. Prerequisites & Installation, 2. Run the High-Performance NiceGUI Application, 2. Systemic Liquidity & Leverage, 2. TDA Geometric Complexity Full-Range Dynamic Normalization, 3. Econometric Explosive Bubble Diagnostics, 3. Run the Local HoloViz Panel Dashboard (+19 more)

### Community 17 - "panel_dashboard.py"
Cohesion: 0.13
Nodes (28): build_econometric_fig(), build_leverage_fig(), build_macro_valuation_fig(), build_mahalanobis_fig(), build_sector_health_fig(), build_sentiment_vol_fig(), fetch_dataset(), generate_explanatory_markdown() (+20 more)

## Knowledge Gaps
- **50 isolated node(s):** `1. System & Logging Setup (`config.py`):`, `2. UI & Accessibility Engine (`ui_theme.py`):`, `3. Data Ingestion & Storage (`ingestor.py`):`, `4. Quantitative Indicator Modules (`features/`):`, `5. Machine Learning Model (`structural_breaks.py`):` (+45 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `DataIngestor` connect `Graphify Settings and Rules` to `panel_dashboard.py`, `Econometric Bubble Detection Models`, `Valuation and Feature Engineering`, `AGVI System Pipeline and Dashboard`?**
  _High betweenness centrality (0.088) - this node is a cross-community bridge._
- **Why does `DashboardState` connect `Valuation and Feature Engineering` to `AGVI System Pipeline and Dashboard`, `Econometric Bubble Detection Models`, `Graphify Settings and Rules`, `FINRA Margin Debt Metrics`, `test_ui_theme.py`?**
  _High betweenness centrality (0.081) - this node is a cross-community bridge._
- **Why does `MacroMahalanobisDetector` connect `AGVI System Pipeline and Dashboard` to `panel_dashboard.py`, `Econometric Bubble Detection Models`, `Valuation and Feature Engineering`?**
  _High betweenness centrality (0.073) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `DashboardState` (e.g. with `DataIngestor` and `MacroMahalanobisDetector`) actually correct?**
  _`DashboardState` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `DataIngestor` (e.g. with `DataFetchError` and `ValidationError`) actually correct?**
  _`DataIngestor` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `StructuralBreakPredictor` (e.g. with `ModelTrainingError` and `DashboardState`) actually correct?**
  _`StructuralBreakPredictor` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `1. System & Logging Setup (`config.py`):`, `2. UI & Accessibility Engine (`ui_theme.py`):`, `3. Data Ingestion & Storage (`ingestor.py`):` to the rest of the system?**
  _50 weakly-connected nodes found - possible documentation gaps or missing edges._