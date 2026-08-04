# Graph Report - Merrill  (2026-07-29)

## Corpus Check
- 30 files · ~52,718 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 212 nodes · 369 edges · 11 communities (10 shown, 1 thin omitted)
- Extraction: 92% EXTRACTED · 8% INFERRED · 0% AMBIGUOUS · INFERRED: 30 edges (avg confidence: 0.79)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Merrill ETF Portfolio Reviews
- AGVI System Pipeline and Dashboard
- Econometric Bubble Detection Models
- Implied Volatility Term Structure Metrics
- Graphify Settings and Rules
- Valuation and Feature Engineering
- FINRA Margin Debt Metrics
- Systemic Leverage Analysis
- Volatility Term Structure Plots
- __init__.py

## God Nodes (most connected - your core abstractions)
1. `DashboardState` - 19 edges
2. `DataIngestor` - 18 edges
3. `StructuralBreakPredictor` - 15 edges
4. `compute_tda_wavelet_complexity()` - 12 edges
5. `Market Bubble Structural Analysis Report` - 12 edges
6. `compute_gsadf_gpt_decomposition()` - 11 edges
7. `compute_margin_leverage_metrics()` - 10 edges
8. `compute_macro_valuations()` - 10 edges
9. `compute_options_volatility_metrics()` - 10 edges
10. `compute_technical_indicators()` - 9 edges

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

## Communities (11 total, 1 thin omitted)

### Community 0 - "Merrill ETF Portfolio Reviews"
Cohesion: 0.17
Nodes (20): Merrill Quarterly Performance Review - April 2026, Joint ETF Strategy Portfolio (March 2026), Merrill Quarterly Performance Review - May 2026, Joint ETF Strategy Portfolio (May 2026), Merrill Quarterly Performance Review - June 2, 2026, Joint ETF Strategy Portfolio (June 2, 2026), Merrill Quarterly Performance Review - June 29, 2026, Joint ETF Strategy Portfolio (June 29, 2026) (+12 more)

### Community 1 - "AGVI System Pipeline and Dashboard"
Cohesion: 0.09
Nodes (26): Graphify Rules Document, Graphify Query Rule, Graphify Workflow Document, NiceGUI Layout & Plotly Dashboard, Data Ingestion (DataIngestor), AGVI Implementation Plan Document, Feature Engineering Pipeline, XGBoost Model Training & Walk-Forward CV (+18 more)

### Community 2 - "Econometric Bubble Detection Models"
Cohesion: 0.07
Nodes (37): _calculate_adf_stat(), compute_gsadf_gpt_decomposition(), DataFrame, ndarray, Econometric Bubble Detection Module.  Implements the PSY procedure (GSADF test s, Calculate Augmented Dickey-Fuller t-statistic for explosive root testing., Computes rolling GSADF explosive test statistics and GPT-adjusted fundamental de, Feature Engineering Module (+29 more)

### Community 3 - "Implied Volatility Term Structure Metrics"
Cohesion: 0.60
Nodes (6): Implied Volatility Metrics Table (July 2026), Implied Volatility Term Structure (Upward Sloping), VIX1D (8.73 - 11.61): Extreme near-term calm, VIX1Y (~23.00): Elevated long-term risk premium, VIX3M (~19.00): Anticipation of future turbulence, VIX Spot (15.57 - 17.16): Low baseline fear

### Community 4 - "Graphify Settings and Rules"
Cohesion: 0.08
Nodes (25): BubbleDetectorError, DataFetchError, IndicatorComputationError, ModelTrainingError, Configuration and Logging Module for Bubble Detector., Base exception for Bubble Detector package., Raised when data fetching fails., Raised when indicator computation fails. (+17 more)

### Community 5 - "Valuation and Feature Engineering"
Cohesion: 0.12
Nodes (25): create_cta_banner(), create_ios_card(), UI Components Module.  Provides iOS 13+ card containers, segmented control tab w, Renders a Call-To-Action (CTA) section with powerful typography (600-800 weight), Creates an iOS 13+ inset card container with subtle shadow, rounded corners,, build_econometric_chart(), build_leverage_chart(), build_macro_valuation_chart() (+17 more)

### Community 6 - "FINRA Margin Debt Metrics"
Cohesion: 0.19
Nodes (10): Machine Learning Models Module, DataFrame, ndarray, Predict structural break drawdown probabilities for input dataframe., Predicts market structural break and drawdown probabilities using Gradient Boost, Extract features and construct forward drawdown target variable., Train ML model using expanding window TimeSeriesSplit cross-validation., StructuralBreakPredictor (+2 more)

### Community 7 - "Systemic Leverage Analysis"
Cohesion: 0.16
Nodes (16): calculate_contrast_ratio(), get_theme_css(), is_wcag_aa_compliant(), parse_hex_color(), UI Theme and Accessibility Design System for Bubble Detector.  Enforces: - WCAG, Generate dynamic CSS variables and global stylesheet enforcing UI/UX & accessibi, Parse hex color string (e.g., '#007AFF' or '#000') into RGB floats [0..1]., Calculate WCAG 2.2 relative luminance for RGB floats [0..1]. (+8 more)

### Community 8 - "Volatility Term Structure Plots"
Cohesion: 0.33
Nodes (6): _persistence_landscape_norm(), ndarray, Topological Data Analysis (TDA) & Wavelet Complexity Module.  Computes point-clo, Transform 1D time series into Takens' delay-coordinate high-dimensional point cl, Calculate point cloud dispersion / L2 persistence landscape norm proxy., _takens_embedding()

## Knowledge Gaps
- **17 isolated node(s):** `Graphify Query Rule`, `Graphify Workflow Document`, `Payout-Adjusted CAPE Ratio`, `GPT Adjustments for Tech Shocks`, `Tail Risk Pricing` (+12 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `DataIngestor` connect `Graphify Settings and Rules` to `Econometric Bubble Detection Models`, `Valuation and Feature Engineering`?**
  _High betweenness centrality (0.114) - this node is a cross-community bridge._
- **Why does `StructuralBreakPredictor` connect `FINRA Margin Debt Metrics` to `Econometric Bubble Detection Models`, `Graphify Settings and Rules`, `Valuation and Feature Engineering`?**
  _High betweenness centrality (0.086) - this node is a cross-community bridge._
- **Why does `DashboardState` connect `Valuation and Feature Engineering` to `Econometric Bubble Detection Models`, `Graphify Settings and Rules`, `FINRA Margin Debt Metrics`, `Systemic Leverage Analysis`?**
  _High betweenness centrality (0.085) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `DashboardState` (e.g. with `DataIngestor` and `StructuralBreakPredictor`) actually correct?**
  _`DashboardState` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `DataIngestor` (e.g. with `DataFetchError` and `ValidationError`) actually correct?**
  _`DataIngestor` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `StructuralBreakPredictor` (e.g. with `ModelTrainingError` and `DashboardState`) actually correct?**
  _`StructuralBreakPredictor` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Graphify Query Rule`, `Graphify Workflow Document`, `Payout-Adjusted CAPE Ratio` to the rest of the system?**
  _17 weakly-connected nodes found - possible documentation gaps or missing edges._