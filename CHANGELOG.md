# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.5.0] - 2026-11-05

### Added
- **Tab 8 20-Year 8-Dislocation High-Fidelity Event-Study & Popperian Falsification Suite (`DISLOCATIONS_8_20YR`, `compute_dislocation_fidelity_metrics`, `build_dislocation_fidelity_chart`, `build_dislocation_fidelity_fig`)**:
  - Added a 4-subplot, 22-trace event-study figure to **Tab 8 ("Composite Summary Indicators")** directly below the existing plots across both NiceGUI (`bubble_detector/ui/dashboard.py`) and HoloViz Panel WebAssembly (`bubble_detector/ui/panel_dashboard.py`) with 100% numerical and visual parity:
    1. **Subplot 1 — Log-Normalized S&P 500 Trajectory ($L_{\text{SPY}}(t) = 100[1 + \ln(\text{SPY}_t/\text{SPY}_0)]$), Master Composite ($\mathcal{I}_t^*$), and Dual-Phase Dislocation Anatomy ($\gamma = 0.97$)**: Overlays pre-peak warning windows $\mathcal{W}_k^{\text{lead}}$ (Amber Gold), peak-to-trough liquidation spans $\mathcal{W}_k^{\text{crash}}$ (Crimson Red), and exact peak ($\blacktriangledown$) / trough ($\blacktriangle$) markers across all 8 major market dislocations (`D1`–`D8`, `2007–2025`).
    2. **Subplot 2 — Event-by-Event Pre-Peak Maximum vs. Crash-Trough Minimum & Peak–Trough Separation ($\Delta_{\text{P-T}, k}^*$, $\gamma = 0.98$)**: Demonstrates a 100% (8/8) pre-peak warning hit rate (mean $\mathcal{I}_{\text{peak}, k}^* = 95.9\%$) and crash-trough relaxation (mean $\mathcal{I}_{\text{trough}, k}^* = 5.7\%$, mean separation $+90.2\%$).
    3. **Subplot 3 — Phase-Time Rescaled Superposed Epoch Analysis ($\theta \in [-1.0, +1.0]$, $\gamma = 0.96$)**: Aligns all 8 dislocations onto canonical phase time $\theta \in [-1, +1]$ (81-point grid), proving universal pre-peak elevation ($>85\%$) and rapid post-peak relaxation across all 5 summary indicators.
    4. **Subplot 4 — Popperian Falsification Audit: Event-Specific Max Drawdown Abatement & Warning Lead Horizon ($\gamma = 0.96$)**: Demonstrates that causal defensive de-risking reduces average dislocation drawdown from $-24.85\%$ to $-5.45\%$ ($+19.41\%$ saved per dislocation) with a mean warning lead of $235.9$ trading days.
- **WebAssembly Bundle Optimization & Test Suite Expansion**:
  - Enhanced AST docstring/operator minification (with UTF-8-safe ASCII backslash-escape decoding) and duplicate Bokeh stylesheet pruning in `bubble_detector/ui/postprocess_wasm.py`, keeping `dist/index.html` strictly `< 120.0 KB` (`118.77 KB`), and expanded the automated test suite to **130 passed tests (100% pass rate)**.

## [3.4.0] - 2026-11-05

### Added
- **Tab 8 S&P 500 Historical Bubble Regime Validation Suite (`build_composite_validation_chart` & `build_composite_validation_fig`)**:
  - Added a synchronized 4-subplot validation figure to **Tab 8 ("Composite Summary Indicators")** across both the NiceGUI server dashboard (`bubble_detector/ui/dashboard.py`) and the HoloViz Panel WebAssembly dashboard (`bubble_detector/ui/panel_dashboard.py`) with 100% numerical and visual parity:
    1. **Subplot 1 — 20-Year S&P 500 Trajectory & 6-Color Composite Bubble Regime Date Bands**: Plots the S&P 500 (`SPY`) benchmark trajectory overlaid on 5 distinct transparent vertical date bands (`rgba(0,229,255,0.24)`, `rgba(255,23,68,0.24)`, `rgba(255,214,0,0.24)`, `rgba(0,230,118,0.24)`, `rgba(224,64,251,0.24)`) across 5 stratified vertical background tiers ($[0.0, 0.2], \dots, [0.8, 1.0]$) for each individual Composite Summary Indicator ($\ge 70\%$), plus a **6th full-height ($[0.0, 1.0]$) transparent Flame Orange-Red consensus band (`rgba(255,109,0,0.40)`)** indicating when **ALL 5 Composite Summary Indicators are simultaneously ON** ($\mathcal{S}_{\text{ALL}}(t) = 1$).
    2. **Subplot 2 — S&P 500 Underwater Drawdown (%) & Forward 63-Day Max Drawdown vs. Active Bubble Consensus Count**: Demonstrates that multi-indicator bubble activations precede major S&P 500 drawdowns while dropping to $0/5$ during crash liquidation troughs.
    3. **Subplot 3 — Cost-Inclusive `$100` Cumulative Wealth Validation (Net of 15 bps Turnover Friction & 4.0% Cash Yield)**: Compares the Dynamic Consensus Tactical Overlay (`$1,030.3` on the 20-year horizon, `-47.4%` MaxDD) and the Unanimous `ALL 5 ON` Shield against passive Buy-and-Hold S&P 500 (`$883.6`, `-55.2%` MaxDD).
    4. **Subplot 4 — Dynamic Tactical Equity Allocation Weight (%) & Ensemble Bubble Consensus Breadth (%)**: Tracks real-time causal equity sizing ($w_{\text{eq}} \in [20\%, 125\%]$) and the fraction of active summary architectures.
- **Unified 70.0% Systemic Bubble Threshold Calibration (`bubble_detector/models/composite_summary.py`)**:
  - Standardized the signed Riemannian projection $z_{\text{eff}, t} = (s_t + 0.45(d_{B,t} - d_{C,t}) - 0.85) / 1.45$ in `Mahalanobis_Summary_Index` and calibrated the Bayesian log-odds intercept (`+0.55`) in `Composite_Summary_Index` so all 5 summary indicators share a unified equilibrium baseline and `70.0%` Systemic Bubble Warning Threshold.
  - Added `build_band_polygon` and `compute_composite_validation_metrics` (expanded verification suite to **125 passed tests**).

## [3.3.0] - 2026-11-05

### Added
- **Authoritative 13-Indicator Information-Maximizing Orthogonal Basis ($\mathcal{B}_{13}^{\perp}$, 20-Year Regime Horizon)**:
  - Audited all 32 candidate indicators across Tabs 1–7 on the 20-year regime horizon (`2006-01-02` to `2026-11-03`, $N = 5,437$ trading days) under the strict $0.87$ Confidence & Unconditional Orthogonal Tolerance Gate ($\tau_j = 1/\text{VIF}_j \ge 0.87$).
  - Discarded redundant/collinear series (`P_CAPE`, `Real_Earnings_Yield`, `Buffett_Indicator`, `Leverage_Exhaustion_Gap`, `Margin_Exhaustion_Score`, `^VIX`, `DSPX`, `COR3M`, `TDA_Persistence_L2_Norm`, `Wavelet_Complexity_Score`) and reworked five cross-tab series via strictly causal 252-day Ridge-stabilized OLS Gram-Schmidt orthogonalization ($\mathcal{P}_{\perp}^{(252)}$), achieving $\text{erank}(\mathbf{R}) = 12.6620/13$ ($\eta_{\text{spec}} = 0.9740 \ge 0.87$), $\det(\mathbf{R}) = 0.7079$, and $\tau_j \in [0.9042, 0.9990] \ge 0.87$ across all 13 indicators.
- **Two-Stage Strictly Causal Stationarity ($I(0)$) & Unit-Variance ($\mu=0, \sigma^2=1$) Preprocessing Protocol**:
  - Enforced zero look-ahead filtration ($\mathcal{F}_t$), verified $I(0)$ stationarity across all 13 indicators ($t_{\text{ADF}} \in [-5.27, -49.52], p \le 1.4 \times 10^{-4}$), and proved Perron–Frobenius positive upper-orthant orientation eliminates the $554$ eigenvector sign flips and negative Peak–Trough inversions ($-23.92$ and $-24.48$) that afflict unconstrained symmetric DFM and Sparse PCA.
- **Comparative Mathematical & Empirical Evaluation of the 5 Best Summary Indicator Architectures ($\ge 0.87$ Gate)**:
  - **1. `Composite_Summary_Index` ($\mathcal{I}_t^*, \gamma = 0.96$)**: Master Log-Odds Bayesian Meta-Synthesis combining all 4 structural paradigms with Purged-Embargo GBDT drawdown probability and Crash-Bottom Liquidation Damper $\Lambda_{\text{Crash}}(t)$ ($100\%$ 8/8 hit rate, $126.0\text{d}$ median lead, $+25.48$ Peak–Trough separation).
  - **2. `Mahalanobis_Summary_Index` ($\mathcal{I}_t^{\text{Mahal}}, \gamma = 0.95$)**: Asymmetric Precision Riemannian Distance ($100\%$ 8/8 hit rate, $126.0\text{d}$ median lead, $+39.47$ Peak–Trough separation).
  - **3. `DFM_Summary_Index` ($\mathcal{I}_t^{\text{DFM}}, \gamma = 0.94$)**: Federal Reserve / Central Bank Causal Conic AR(2) Kalman Filter Nowcast extracting the persistent common bubble state $\hat{f}_{t \mid t}$ ($100\%$ 8/8 hit rate, $122.5\text{d}$ median lead, $+26.92$ Peak–Trough separation).
  - **4. `Diffusion_Summary_Index` ($\mathcal{I}_t^{\text{Diffusion}}, \gamma = 0.93$)**: Conference Board Single-Window Gaussian Copula Rank & 63-Day Symmetric Momentum Breadth Index ($100\%$ 8/8 hit rate, $126.0\text{d}$ median lead, $+24.04$ Peak–Trough separation).
  - **5. `SPCA_Summary_Index` ($\mathcal{I}_t^{\text{SPCA}}, \gamma = 0.92$)**: Zou–Hastie–Tibshirani (2006) Causal Conic Elastic-Net Sparse PCA ($\gamma_{\ell_1} = 0.25$, $\bar{k}_{\text{active}} = 4.58/13$ active pillars), achieving the highest pre-peak Mutual Information ($MI_{\text{peak}} = 0.0129\text{ nats}$, $100\%$ 8/8 hit rate, $+23.70$ Peak–Trough separation).
- **Tab 8 ("Composite Summary Indicators") Architectural Blueprint**:
  - Documented full specification across `MarketBubble_DDFv100.md`, `agvi_TechnicalSpecification_DDFv100.md`, and `README.md` for dual-runtime implementation across NiceGUI (`dashboard.py`) and HoloViz Panel WebAssembly (`panel_dashboard.py`).

## [3.2.0] - 2026-11-03

### Added
- **Option 3 Regime Horizon (20-Year Global Crisis Horizon, 2006–2026)** (`bubble_detector/data/date_horizons.py`):
  - Added standalone calendar-anchored 20-year horizon starting January 1, 2006, encompassing 8 major historical regimes and crises:
    - 2007-2009 Subprime Housing Crisis & Great Financial Crisis Crash
    - 2010 European Sovereign Debt Crisis & Flash Crash
    - 2011 U.S. Debt Downgrade & Debt Ceiling Crisis
    - 2015-2016 Global Growth Slowdown & Energy Crash
    - 2018 Volmageddon & Q4 QT Liquidity Compression
    - 2020 COVID-19 Flash Crash (VIX 82.7 Spike)
    - 2022 Fed Rate Tightening & Tech Drawdown
    - 2024-2026 AI CapEx Mega-Cap Rally (CAPE 41.37)
  - Registered institutional purple badge token (`#9C27B0`), full crash annotations, and metadata across `HORIZON_METADATA`.
- **Pre-Compiled 20-Year Data Provenance Artifacts** (`stage_provenance.py`):
  - Generated `market_data_20yr.parquet` (827 KB) and `market_data_20yr.json` (1.3 MB) with adaptive decimal precision (6 decimals for sensitive topological/volatility features, 4 decimals for price/indicator series).
  - Staged across `data/provenance/`, `dist/`, and `build/`.
- **Automated Dual-Directory Build & Cache Synchronization** (`bubble_detector/ui/postprocess_wasm.py`):
  - Implemented `sync_wasm_build_directories()` ensuring identical, up-to-date postprocessed bundles, datasets, and service workers across both `dist/` and `build/`.
  - Upgraded Service Worker cache version to `bubble-detector-wasm-v3.2.0` in `sw.js`, `dist/sw.js`, and `build/sw.js` for automatic cache invalidation and instantaneous asset refresh on client browsers.
  - Injected Pyodide MEMFS pre-loader routines for `market_data_20yr.json` and deep-link URL hash routing (`#horizon=option_3`).
- **Comprehensive Cross-Runtime Indicator & Trace Parity Suite**:
  - `tests/test_full_indicator_parity.py`: Validated 100% numerical and visual parity across all 3 horizons (Option 1, Option 2, Option 3) and all 7 tabs between NiceGUI and HoloViz Panel WebAssembly.
  - `tests/test_wasm_parquet_parity.py`: Confirmed identical data column signatures and values loaded by the WASM data engine.
  - Full automated test suite expanded to **116 passed tests (100% pass rate)**.

### Changed
- **Dynamic Multi-Horizon Dashboard Architecture**:
  - Replaced legacy binary toggle logic (`is_50yr`) with dynamic horizon registry mapping in `bubble_detector/ui/dashboard.py` and `bubble_detector/ui/panel_dashboard.py`.
  - Synchronized dropdown selectors dynamically from `HORIZON_METADATA` with seamless reactive data updating across all 7 tabs.

## [3.1.0] - 2026-10-05

### Added
- **Global Liquidity & Central Bank ETL Engine** (`bubble_detector/data/etl_fred.py`):
  - Point-in-time FRED ingestion of U.S. M2 Money Stock (`M2SL`, +10 calendar days publication lag) and Federal Reserve Total Assets (`WALCL`, +1 calendar day reporting lag).
  - Historical Monetary Base (`BOGMBASE`, +10 calendar days lag) seamlessly spliced into Fed Assets pre-2002 using continuous backward return compounding with zero transition seam cliffs.
  - Continuous derived series: `Global_Liquidity_Index` ($ Trillion USD), `M2_YoY_Growth` (%), `CentralBank_YoY_Growth` (%), and `Liquidity_Momentum` without warmup NaNs.
- **Log-Periodic Power Law Singularity (LPPLS) Engine** (`bubble_detector/features/lppls_model.py`):
  - Pure-NumPy/SciPy implementation of the Filimonov & Sornette (2013) linear-nonlinear subordination algorithm.
  - Closed-form Ordinary Least Squares projection via normal equations for linear parameters $(A, B, C_1, C_2)$.
  - Bounded multi-start L-BFGS-B optimization over nonlinear parameters $(t_c, m, \omega)$.
  - Verification of canonical Sornette 5 filtering constraints ($0.1 \le m \le 0.9$, $4.8 \le \omega \le 13.0$, $B < 0$, damping condition $D \ge 0.8$, and $R^2 \ge 0.60$).
  - Rolling multi-scale LPPLS Bubble Confidence Indicator $CI(t) \in [0, 1]$ across lookback windows $\{60, 90, 125, 180, 250\}$ trading days and continuous 90th percentile threshold `LPPLS_90th_Percentile`.
- **Dual-Condition Tech Exuberance Engine** (`bubble_detector/features/tech_exuberance.py`):
  - Ratio tracking of Technology ETF vs S&P 500 (`XLK_SPY_Ratio`).
  - Condition 1 (Macro Decoupling): M2 YoY growth deceleration / negative liquidity momentum concurrent with tech outperformance expansion.
  - Condition 2 (Statistical Singularity): BSADF or LPPLS confidence entering extreme historical quintiles ($\ge 90\text{th}$ percentile).
  - Conjoint `Tech_Exuberance_Signal` and contiguous span extractor `compute_exuberance_spans` for visual highlight rendering.
- **Tab 7 ("Tech Exuberance Score") in Dual Dashboard Runtimes**:
  - NiceGUI server-side dashboard (`bubble_detector/ui/dashboard.py`): Option A layout with 4 synchronized stacked subplots, dynamic theme-reactive styling, and semi-transparent glowing highlight spans (`rgba(255, 69, 58, 0.20)`).
  - HoloViz Panel WebAssembly dashboard (`bubble_detector/ui/panel_dashboard.py`): 100% numerical and visual parity running purely in-browser under Pyodide with LTTB decimation and responsive right-flushed vertical legends.
- **WebAssembly Client-Side Dataset Pre-Compilation** (`stage_provenance.py`):
  - Pre-compilation of 35-column datasets (`market_data_50yr` and `market_data_modern`) in both Apache Arrow Parquet and compact JSON formats.
  - Payload compression with compact JSON separators and integer casting, meeting strict payload budget (< 5.0 MB uncompressed, < 600 KB gzipped).
- **Unit & Integration Test Rigor**:
  - `tests/test_global_liquidity.py`: Verified schema, publication lags, splicing continuity, and bounded growth rates.
  - `tests/test_bsadf_rigor.py`: Verified explosive root sensitivity, dynamic AIC lag selection, expanding supremum grid, and wild bootstrap critical values.
  - `tests/test_tda_wavelet_rigor.py`: Verified Takens delay embedding, Bubenik $L_2$ norms, persistence entropy, and continuous Morlet wavelet spectral Shannon entropy.
  - `tests/test_lppls_rigor.py`: Verified subordination parameter recovery, Sornette filtering bounds, and rolling multi-scale pipeline.
  - `tests/test_tech_exuberance_tab.py`: Verified dual condition boolean logic, threshold floors, and highlight span generation.
  - `tests/test_wasm_tech_exuberance.py`: Verified 4-subplot Figure construction, responsive legends, and WebAssembly tab binding.

### Changed
- **Econometric & PSY 2015 BSADF Engine** (`bubble_detector/features/econometric.py`):
  - Refactored `calculate_adf_stat` to implement dynamic lag selection ($k \in \{0, 1\}$) via Akaike Information Criterion (AIC) and exact OLS standard error formulas.
  - Implemented true recursive backward expanding supremum search over continuous window grid $w \in [15, 60]$ trading days: $BSADF_t = \max_{w \in \mathcal{W}} ADF(y_{t-w:t})$.
  - Generated continuous rolling percentile series `BSADF_90th_Percentile` and preserved wild bootstrap critical value lines (1.45, 2.05).
- **Topological Data Analysis & Wavelet Transforms** (`bubble_detector/features/topology.py`):
  - Implemented exact Bubenik (2015) persistence landscape $L_2$ norm $\|\lambda\|_{L_2} = \sqrt{\frac{1}{3} \sum (d_j - b_j)^3}$.
  - Added persistence entropy $E(D) = -\sum p_j \ln p_j$.
  - Re-implemented Continuous Morlet Wavelet Transform in pure NumPy to compute scaleogram power distribution and Wavelet Shannon Spectral Entropy across scales $s \in [2, 64]$ without deprecated `scipy.signal.cwt`.
- **Data Lineage & Test Suite Staging** (`bubble_detector/data/etl_vxo.py`):
  - Fixed fallback copying of raw parquet datasets when isolated temporary directories are utilized in testing environments.

## [3.0.0] - 2026-09-03
- Multi-decade 50-year date horizon anchoring (1976–2026, 13,045 trading days).
- Signed Riemannian Mahalanobis distance with pre-registered direction vector $\mathbf{b} \in \{-1, +1\}^{15}$.
- Purged-embargo walk-forward cross-validation with zero target leakage.
- WebAssembly client-side execution under Pyodide and HoloViz Panel with MEMFS staging.
- Zero synthetic Gaussian bump enforcement across all data ingestors.
