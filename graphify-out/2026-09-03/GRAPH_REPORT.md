# Graph Report - Merrill  (2026-09-03)

## Corpus Check
- 60 files · ~77,683 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 543 nodes · 1019 edges · 25 communities (23 shown, 2 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 33 edges (avg confidence: 0.77)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `b7fad9ac`
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
- get_dynamic_horizon_metadata
- AGVI Technical Specification Document
- etl_shiller.py
- etl_vxo.py
- ingestor.py
- etl_finra.py
- etl_fred.py

## God Nodes (most connected - your core abstractions)
1. `DashboardState` - 37 edges
2. `MacroMahalanobisDetector` - 33 edges
3. `DataIngestor` - 28 edges
4. `StructuralBreakPredictor` - 24 edges
5. `compute_tda_wavelet_complexity()` - 21 edges
6. `generate_wasm_dataset()` - 20 edges
7. `compute_gsadf_gpt_decomposition()` - 18 edges
8. `compute_margin_leverage_metrics()` - 15 edges
9. `compute_macro_valuations()` - 15 edges
10. `compute_options_volatility_metrics()` - 15 edges

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

## Communities (25 total, 2 thin omitted)

### Community 0 - "Merrill ETF Portfolio Reviews"
Cohesion: 0.06
Nodes (46): Graphify Rules Document, Graphify Query Rule, Graphify Workflow Document, NiceGUI Layout & Plotly Dashboard, Data Ingestion (DataIngestor), AGVI Implementation Plan Document, Feature Engineering Pipeline, XGBoost Model Training & Walk-Forward CV (+38 more)

### Community 1 - "AGVI System Pipeline and Dashboard"
Cohesion: 0.06
Nodes (38): Machine Learning Models Module, MacroMahalanobisDetector, DataFrame, ndarray, Macro Mahalanobis Distance Regime-Switching Bubble Detector.  Implements Method, Transform indicators into stationary, standardized rolling z-scores         with, Compute:         1. Mahalanobis Distance (DM)         2. Signed Bubble Projectio, Calculate standard rolling Mahalanobis Distance for backward compatibility. (+30 more)

### Community 2 - "Econometric Bubble Detection Models"
Cohesion: 0.05
Nodes (55): calculate_adf_stat(), compute_gsadf_gpt_decomposition(), compute_wild_bootstrap_critical_values(), DataFrame, ndarray, Econometric Bubble Detection Module (Canonical PSY & GSADF).  Implements the Phi, Calculate Augmented Dickey-Fuller t-statistic for right-tailed explosive root te, Compute wild bootstrap critical values (95% and 99%) under the null hypothesis (+47 more)

### Community 3 - "Implied Volatility Term Structure Metrics"
Cohesion: 0.60
Nodes (6): Implied Volatility Metrics Table (July 2026), Implied Volatility Term Structure (Upward Sloping), VIX1D (8.73 - 11.61): Extreme near-term calm, VIX1Y (~23.00): Elevated long-term risk premium, VIX3M (~19.00): Anticipation of future turbulence, VIX Spot (15.57 - 17.16): Low baseline fear

### Community 4 - "Graphify Settings and Rules"
Cohesion: 0.16
Nodes (18): Configuration and Logging Module for Bubble Detector., get_current_date(), get_dynamic_50yr_date_range(), get_dynamic_horizon_metadata(), Any, Dynamic 50-Year Multi-Horizon Date Engine.  Provides calendar-aware date horizon, Return current execution date, or parse override date string/object., Compute rolling 50-year date range from current execution date.     Safely handl (+10 more)

### Community 5 - "Valuation and Feature Engineering"
Cohesion: 0.05
Nodes (61): create_cta_banner(), create_ios_card(), UI Components Module.  Provides iOS 13+ card containers, segmented control tab w, Renders a Call-To-Action (CTA) section with powerful typography (600-800 weight), Creates an iOS 13+ inset card container with subtle shadow, rounded corners,, build_econometric_chart(), build_leverage_chart(), build_macro_valuation_chart() (+53 more)

### Community 6 - "FINRA Margin Debt Metrics"
Cohesion: 0.10
Nodes (23): ModelTrainingError, Raised when ML model training fails., Any, DataFrame, ndarray, Structural Break Machine Learning Classifier & Probability Calibration Module., Train ML model and fit isotonic probability calibrator using expanding-window, Predict calibrated structural break drawdown probabilities. (+15 more)

### Community 8 - "test_ui_theme.py"
Cohesion: 0.08
Nodes (25): BacktestResult, PortfolioBacktestEngine, Any, DataFrame, ndarray, Institutional Cost-Inclusive Portfolio Backtest Simulation Engine.  Simulates an, Simulate single portfolio with frictions, cash yields, and rebalancing costs., Performance statistics and equity curves for a single backtested strategy. (+17 more)

### Community 11 - "Overview of Completed Implementation"
Cohesion: 0.18
Nodes (10): 1. System, Configuration & Date Horizons (`config.py` & `date_horizons.py`):, 2. UI & Accessibility Engine (`ui_theme.py`):, 3. Data Ingestion & Storage (`ingestor.py`):, 4. Quantitative Indicator Modules (`features/` & `features/utils.py`):, 5. Machine Learning Model (`structural_breaks.py`):, 6. Macro Mahalanobis Distance Engine (`regime_mahalanobis.py`):, 7. Interactive Dashboards & Dual-Runtime Architecture:, 8. Data Red Team Remediation & Institutional Hardening: (+2 more)

### Community 13 - "Detailed Slide Breakdown by Section & Group"
Cohesion: 0.20
Nodes (9): Detailed Slide Breakdown by Section & Group, Executive Presentation Deck Overview, Group 1: Key Findings (Group Confidence Score: 0.94), Group 2: Supporting Evidence: Valuation, Econometrics & ML (Group Confidence Score: 0.93), Group 3: Sector Specific Application: Tech vs. Energy (Group Confidence Score: 0.91), Group 4: Implications for Systemic Stability (Group Confidence Score: 0.95), Group 5: Strategic Recommendations (Group Confidence Score: 0.96), Verification Results (+1 more)

### Community 16 - ".fetch_market_data"
Cohesion: 0.06
Nodes (33): 1. Macro Mahalanobis Distance & Dynamic Exposure Sizing, 1. Macro Valuation Anchors, 1. Prerequisites & Installation, 2. Run the High-Performance NiceGUI Application, 2. Systemic Liquidity & Leverage, 2. TDA Geometric Complexity Full-Range Dynamic Normalization, 3. Econometric Explosive Bubble Diagnostics, 3. Run the Local HoloViz Panel Dashboard (+25 more)

### Community 17 - "panel_dashboard.py"
Cohesion: 0.11
Nodes (34): calculate_adf_stat(), normalize_tda_indicator(), ndarray, Shared Mathematical & Topological Utilities.  Provides reusable numerical algori, Calculate Augmented Dickey-Fuller t-statistic for explosive root testing., Transform 1D time series into Takens delay-coordinate high-dimensional point clo, Causally rescale raw TDA Persistence Landscape L2 Norm to span [target_min, targ, takens_embedding() (+26 more)

### Community 18 - "get_dynamic_horizon_metadata"
Cohesion: 0.08
Nodes (21): DataIngestor, DataFrame, Path, Construct seamless asset time series with continuous backward return compounding, Merge authentic point-in-time macroeconomic series (Shiller CAPE, FRED GDP, FINR, Handles fetching, preprocessing, backward continuous return compounding,     Pol, Fetch historical price and macroeconomic datasets for SPY, sectors, and volatili, ingestor() (+13 more)

### Community 19 - "AGVI Technical Specification Document"
Cohesion: 0.15
Nodes (13): FinraETL, Path, ETL Pipeline for FINRA & NYSE margin debt with strict publication lag constraint, FredETL, Path, ETL Pipeline for FRED macroeconomic series with strict publication lag constrain, Pre-compilation and staging script for provenance and WASM Parquet datasets., stage_all() (+5 more)

### Community 20 - "etl_shiller.py"
Cohesion: 0.16
Nodes (13): _generate_authentic_historical_shiller_monthly(), get_shiller_data(), DataFrame, Path, Robert Shiller Monthly ie_data ETL & Point-in-Time Real Data Ingestor (1871–Pres, ETL Pipeline for Robert Shiller's monthly S&P Composite and CAPE dataset., Fetch Shiller data, validate schema and cache to parquet., Interpolate monthly Shiller series to daily business days with strictly causal (+5 more)

### Community 21 - "etl_vxo.py"
Cohesion: 0.16
Nodes (13): _generate_authentic_vxo_daily(), get_vxo_data(), DataFrame, Path, CBOE S&P 100 Volatility Index (^VXO) ETL & Historical Splicer (1986–Present).  P, Public helper to obtain daily CBOE VXO series., Generate authentic daily CBOE VXO index capturing empirical volatility regime dy, ETL Pipeline for CBOE VXO volatility index. (+5 more)

### Community 22 - "ingestor.py"
Cohesion: 0.18
Nodes (10): BubbleDetectorError, DataFetchError, IndicatorComputationError, Base exception for Bubble Detector package., Raised when data fetching fails., Raised when indicator computation fails., Raised when data validation fails., ValidationError (+2 more)

### Community 23 - "etl_finra.py"
Cohesion: 0.25
Nodes (8): _generate_authentic_margin_debt_series(), get_finra_margin_debt(), DataFrame, FINRA & NYSE Margin Debt Point-in-Time ETL Module.  Ingests monthly margin debt, Interpolate margin debt to daily business days, guaranteeing         the mandato, Public helper to obtain daily point-in-time FINRA margin debt data., Generate authentic monthly historical margin debt dataset spanning 1959 to 2026, Stage FINRA margin debt dataset to parquet.

### Community 24 - "etl_fred.py"
Cohesion: 0.25
Nodes (8): _generate_authentic_fred_macro_series(), get_fred_data(), DataFrame, FRED Macroeconomic Point-in-Time Data ETL Module.  Ingests and models macroecono, Stage FRED macro dataset to parquet., Interpolate FRED macro indicators to daily business days, guaranteeing         a, Public helper to obtain daily point-in-time FRED macroeconomic indicators., Generate authentic macroeconomic dataset spanning 1950 to 2026     matching publ

## Knowledge Gaps
- **57 isolated node(s):** `market-bubble-detector`, `1. System, Configuration & Date Horizons (`config.py` & `date_horizons.py`):`, `2. UI & Accessibility Engine (`ui_theme.py`):`, `3. Data Ingestion & Storage (`ingestor.py`):`, `4. Quantitative Indicator Modules (`features/` & `features/utils.py`):` (+52 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `MacroMahalanobisDetector` connect `AGVI System Pipeline and Dashboard` to `panel_dashboard.py`, `Econometric Bubble Detection Models`, `Valuation and Feature Engineering`?**
  _High betweenness centrality (0.098) - this node is a cross-community bridge._
- **Why does `DashboardState` connect `Valuation and Feature Engineering` to `AGVI System Pipeline and Dashboard`, `Econometric Bubble Detection Models`, `Graphify Settings and Rules`, `FINRA Margin Debt Metrics`, `test_ui_theme.py`, `panel_dashboard.py`, `get_dynamic_horizon_metadata`?**
  _High betweenness centrality (0.078) - this node is a cross-community bridge._
- **Why does `DataIngestor` connect `get_dynamic_horizon_metadata` to `AGVI System Pipeline and Dashboard`, `Econometric Bubble Detection Models`, `Graphify Settings and Rules`, `Valuation and Feature Engineering`, `FINRA Margin Debt Metrics`, `panel_dashboard.py`, `ingestor.py`?**
  _High betweenness centrality (0.069) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `DashboardState` (e.g. with `PortfolioBacktestEngine` and `DataIngestor`) actually correct?**
  _`DashboardState` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `DataIngestor` (e.g. with `DataFetchError` and `ValidationError`) actually correct?**
  _`DataIngestor` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `StructuralBreakPredictor` (e.g. with `ModelTrainingError` and `DashboardState`) actually correct?**
  _`StructuralBreakPredictor` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `market-bubble-detector`, `1. System, Configuration & Date Horizons (`config.py` & `date_horizons.py`):`, `2. UI & Accessibility Engine (`ui_theme.py`):` to the rest of the system?**
  _57 weakly-connected nodes found - possible documentation gaps or missing edges._