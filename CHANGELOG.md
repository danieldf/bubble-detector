# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
