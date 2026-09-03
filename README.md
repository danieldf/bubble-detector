# 📉 Multidimensional Market Bubble Detector & Structural Break System

[![Deploy WebAssembly Dashboard](https://github.com/danieldf/bubble-detector/actions/workflows/deploy.yml/badge.svg)](https://github.com/danieldf/bubble-detector/actions/workflows/deploy.yml)
[![Live WebAssembly Dashboard](https://img.shields.io/badge/Live_Dashboard-GitHub_Pages-0288D1?style=flat&logo=github)](https://danieldf.github.io/bubble-detector/)
[![Version](https://img.shields.io/badge/Version-v2.1.1-4CAF50?style=flat)](https://github.com/danieldf/bubble-detector/releases/tag/v2.1.1)
[![Python Version](https://img.shields.io/badge/Python-3.11%2B%20%7C%203.14-blue?style=flat&logo=python)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/Tests-33%20Passed%20(100%25)-success?style=flat)](https://github.com/danieldf/bubble-detector/actions)

An enterprise-grade quantitative econometric system and machine learning framework engineered to detect financial asset bubbles, diagnose non-linear macroeconomic regime shifts, quantify systemic distance from historical equilibrium, and dynamically adjust portfolio equity exposure.

The platform provides dual runtime architectures: a high-performance server-side **NiceGUI (FastAPI/Polars)** analytical workstation and an entirely client-side **HoloViz Panel (Pyodide/WebAssembly)** dashboard running in-browser with zero backend dependencies.

---

## 🌟 Live Interactive WebAssembly Dashboard

🚀 **[Access the Live Panel WebAssembly Dashboard on GitHub Pages](https://danieldf.github.io/bubble-detector/)**

*(Compiled directly to WebAssembly using HoloViz Panel, Pyodide, and Bokeh/Plotly — executes 100% client-side in your web browser with zero server computing cost or data egress!)*

---

## 📅 Dynamic 50-Year Multi-Horizon Date Engine

The system features a calendar-aware date generator that dynamically anchors the historical spectrum to the exact execution date:

$$\\text{Start Date} = \\text{Current Date} - 50 \\text{ physical calendar years}$$

| Horizon Option | Dynamic Time Range | Regimes Captured | Data Ingestion Pipeline | Target Coverage |
| :--- | :--- | :--- | :--- | :--- |
| **Option 1: Comprehensive 50-Year Horizon** | Dynamic 50-year lookback (e.g. `1976-09-02` to `2026-09-02`) | **7 Macro Regimes** (13,045 trading days) | Polars parquet caching + calibrated synthetic backfill + exchange splicing | Volcker Disinflation, 1987 Black Monday, 2000 Dot-Com Bubble & Crash, 2008 Subprime GFC, 2020 COVID Flash Crash, 2022 Fed Rate Hiking Cycle, 2024–2026 AI CapEx Supercycle |
| **Option 2: Modern 11-Year Regime Horizon** | `2015-01-01` to current date | **5 Macro Regimes** (3,045 trading days) | 100% Native High-Fidelity Exchange Feeds (Yahoo Finance / CBOE / FRED) | 2018 Volmageddon, 2020 COVID Crash & QE Rebound, 2022 Inflation & Rate Hikes, 2024–2026 AI Infrastructure Boom |

---

## 📊 6 Interactive Dashboard Modules

### 1. Macro Valuation Anchors
- **Shiller CAPE (41.37)**: Inflation-adjusted 10-year P/E ratio, positioned in the second-highest valuation epoch in U.S. financial history.
- **Payout-Adjusted CAPE (P-CAPE)**: Growth-adjusted P/E incorporating corporate dividend payout ratios and share repurchase yields ($R^2 = 0.35$).
- **The Buffett Indicator (218.1% of GDP)**: Total Wilshire 5000 equity market capitalization divided by U.S. nominal GDP, signaling an extreme deviation from the historical mean ($+56.6\\%$).

### 2. Systemic Liquidity & Leverage
- **FINRA Margin Debt ($1.416T Peak)**: Nominal and inflation-adjusted borrowed collateral tracking leverage velocity ($+53.7\\%$ YoY).
- **Margin Exhaustion Score**: Measures unused institutional debt capacity (\"margin credit\") to detect forced liquidation vulnerabilities (\"Pingcang Line\" fire sales).

### 3. Econometric Explosive Bubble Diagnostics
- **Generalized Supremum ADF (GSADF / PSY Procedure)**: Recursive right-tailed unit root test detecting explosive Evans bubble dynamics.
- **General-Purpose Technology (GPT) Decomposition**: Econometric regression filtering $754B in hyperscaler AI capital expenditures to distinguish structural productivity repricing from irrational speculative exuberance.

### 4. Options Sentiment & Behavioral Tracking
- **VIX Term Structure Contango**: Compares ultra-short-term volatility (VIX1D) to 3-month (VIX3M) and 1-year (VIX1Y) expectations to detect volatility compression traps.
- **CBOE SKEW Tail-Risk Index (>145)**: Measures institutional out-of-the-money put option demand for catastrophic downside insurance.
- **OVX/VIX Cross-Asset Volatility Decoupling**: Tracks energy-equity divergence (3.5x ratio) to forecast exogenous inflation and supply shocks.
- **CBOE Dispersion Index (DSPX)**: Captures narrowing market leadership and collapsing implied correlation ($<8.0$).

### 5. Sector Vulnerability & Topological Dynamics
- **Housing Price-to-Income Ratio (7.11x Peak)**: Fundamental affordability anchor indicating domestic real estate overextension.
- **Tech ETF XLK**: Measures semiconductor and software capital expenditure concentration.
- **Topological Data Analysis (TDA) Geometric Complexity**: 3D Takens delay-coordinate embedding tracking persistence landscape $L_2$ norms, dynamically normalized to $[0.80, 7.00]$ to match physical sector asset multiples.
- **Continuous Morlet Wavelet Transform**: Dynamic scaleogram energy decomposition to adapt window sizes to non-linear frequency clustering.

### 6. Macro Mahalanobis Distance & Multi-Dimensional Regime Signals (NEW)
- **Macro Mahalanobis Distance ($D_M \\in [0.0\\sigma, 12.0\\sigma]$)**: Multi-dimensional, correlation-aware statistical distance measuring the divergence of the 15-dimensional macro state from historical equilibrium.
- **Non-Parametric Bubble Probability ($P_{\\text{bubble}} \\in [0, 1]$)**: Rolling empirical percentile rank quantifying regime-switching likelihood.
- **Dynamic Portfolio Equity Exposure ($w_{\\text{equity}} \\in [0.20, 1.00]$)**: Smooth mathematical position sizing eliminating binary whipsaw risk.
- **White-Box Anomaly Attribution**: Explains top-3 individual drivers behind systemic spikes (e.g., CAPE, Buffett Indicator, Margin Exhaustion, TDA Complexity).
- **Right-Flushed Vertical Legend**: Unobstructed chart canvas with reference threshold lines at $3.8\\sigma$ (Historical Norm), $5.0\\sigma$ (Warning), and $6.2\\sigma$ (Extreme Crisis).

---

## 🔬 Mathematical Formulations

### 1. Macro Mahalanobis Distance & Dynamic Exposure Sizing

Given the standardized vector of stationary macroeconomic features $\\mathbf{z}_t = (z_{1,t}, \\dots, z_{p,t})^T \\in \\mathbb{R}^p$ ($p=8$ core indicators):

$$\\mathbf{\\Sigma}_{\\text{reg}} = \\text{Cov}(\\mathbf{Z}_{[t-W:t]}) + \\lambda \\mathbf{I}, \\quad \\lambda = 10^{-2}$$

$$D_M(t) = \\min\\left(12.0, \\, \\sqrt{(\\mathbf{z}_t - \\boldsymbol{\\mu}_t)^T \\mathbf{\\Sigma}_{\\text{reg}}^{-1} (\\mathbf{z}_t - \\boldsymbol{\\mu}_t)}\\right)$$

$$\\text{Bubble Regime Probability}: \\quad P_{\\text{bubble}}(t) = \\text{PercentileRank}_{W}(D_M(t)) \\in [0, 1]$$

$$\\text{Dynamic Equity Exposure}: \\quad w_{\\text{equity}}(t) = 1.0 - 0.80 \\times P_{\\text{bubble}}(t) \\in [0.20, 1.00]$$

$$\\text{Driver Attribution}: \\quad A_j(t) = \\frac{|z_{j,t} - \\mu_{j,t}|}{\\sum_{k=1}^p |z_{k,t} - \\mu_{k,t}|}$$

### 2. TDA Geometric Complexity Full-Range Dynamic Normalization

Given daily log returns $r_t = \\ln(P_t / P_{t-1})$, a 3-dimensional point cloud is constructed via Takens delay embedding:

$$\\mathbf{v}_i = \\left(r_{i}, \\, r_{i-2}, \\, r_{i-4}\\right) \\in \\mathbb{R}^3$$

The persistence landscape $L_2$ norm measures point cloud dispersion from the centroid $\\mathbf{c}$:

$$\\text{TDA}_{\\text{L2}}(t) = \\text{std}(\\\\mathbf{v}_i - \\mathbf{c}\\_2) \\times \\sqrt{N}$$

To bridge the gap between raw topological dispersion ($\\approx 0.010 - 0.045$) and the physical visual canvas of Tabs 5 and 6 ($0$ to $7$), the indicator is dynamically mapped via an affine transformation:

$$\\text{TDA}_{\\text{norm}}(t) = 0.80 + (7.00 - 0.80) \\times \\frac{\\text{TDA}_{\\text{L2}}(t) - \\min(\\text{TDA}_{\\text{L2}})}{\\max(\\text{TDA}_{\\text{L2}}) - \\min(\\text{TDA}_{\\text{L2}})}$$

- **Minimum Floor**: Exactly $0.80$ (guaranteed $\\ge 0.20$).
- **Equilibrium Baseline**: Typical median of $1.40 - 2.20$.
- **Warning Band**: $3.50 - 5.00$ (aligning with $3.8\\sigma$ and $5.0\\sigma$ thresholds).
- **Crisis Peak**: Achieves the full $7.00$ ceiling during structural crashes (matching Housing PTI at $7.11$ and Tech XLK at $7.00$).

---

## 💻 Local Setup & Execution Guide

### 1. Prerequisites & Installation

```bash
# Clone the repository
git clone https://github.com/danieldf/bubble-detector.git
cd bubble-detector

# Create and activate virtual environment
uv venv --python 3.11
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt
```

### 2. Run the High-Performance NiceGUI Application

Launches the native Polars-accelerated desktop/server dashboard with dynamic dark/light theme switching:

```bash
python -m bubble_detector.ui.dashboard
```
*Access in browser at: `http://localhost:8080`*

### 3. Run the Local HoloViz Panel Dashboard

Serves the standalone Panel dashboard locally:

```bash
panel serve bubble_detector/ui/panel_dashboard.py --show --port 5006
```
*Access in browser at: `http://localhost:5006`*

### 4. Build and Run Client-Side WebAssembly (Pyodide)

Compiles the dashboard into zero-backend WebAssembly HTML/JS bundles:

```bash
# Compile to Pyodide WASM target
python -m panel convert bubble_detector/ui/panel_dashboard.py --to pyodide --requirements panel bokeh plotly numpy --out build/

# Synchronize index.html
cp build/panel_dashboard.html build/index.html

# Serve locally
python -m http.server 8000 --directory build/
```
*Access client-side WASM app at: `http://localhost:8000`*

### 5. Run the Automated Test Suite

Executes all 32 unit, integration, and cross-framework parity tests:

```bash
# Run all tests
pytest tests/ -v

# Run Mahalanobis and Tab 6 normalization tests specifically
pytest tests/test_mahalanobis.py -v

# Run 100% numerical parity verification between NiceGUI and WASM
pytest tests/test_full_indicator_parity.py -v
```

### 6. Update Knowledge Graph

Keep the repository knowledge graph in `graphify-out/` synchronized:

```bash
graphify update .
```

---

## 📋 Changelog

All notable changes to this project are documented in this section adhering to [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and [Semantic Versioning (SemVer)](https://semver.org/).

### [v2.1.1] - 2026-09-02

#### Added
- **Right-Flushed Legends Across All Tabs (1 through 6)**:
  - Standardized all Plotly visualization figure layouts across Tabs 1–6 in both **NiceGUI** (`dashboard.py`) and **WebAssembly** (`panel_dashboard.py`) to right-flushed vertical orientation (`orientation="v", x=1.01, y=1.0, margin.r=230`).
  - Added automated test `test_all_tabs_legends_right_flushed` verifying legend formatting across all 12 figures.
- **Executive Summary UI Components**:
  - Integrated high-impact Executive Summary cards in both NiceGUI and Panel WebAssembly editions, providing users with immediate macroeconomic context (CAPE 41.37, Margin Debt $1.416T, AI CapEx supercycle) and architectural breadth.
- **Enhanced Framework & Architecture Specifications**:
  - Updated WASM application sidebar note to comprehensively detail the complete technology stack: Polars, Apache Parquet, Pyodide, NumPy, SciPy, Scikit-Learn, Plotly, and Bokeh.
- **Modern `uv` Packaging Infrastructure**:
  - Authored deeply documented `pyproject.toml` adhering to PEP 621, setuptools build backend, and modern `[dependency-groups]`.
  - Authored deeply documented `requirements.txt` with architectural role annotations for every dependency.
- **Official Licensing**:
  - Added official `LICENSE` file for Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International Public License (CC BY-NC-ND 4.0).
- **Test Suite Expansion**:
  - Automated test suite expanded to **33 tests passed (100% pass rate)**.

---

### [v2.1.0] - 2026-09-02

#### Added
- **Method 1: Macro Mahalanobis Distance Engine** (`bubble_detector/models/regime_mahalanobis.py`):
  - Multi-dimensional regularized covariance distance $D_M(t)$ with Tikhonov ridge $\\lambda = 10^{-2}\\mathbf{I}$ and $12.0\\sigma$ ceiling.
  - Non-parametric empirical bubble probability score $P_{\\text{bubble}}(t) \\in [0, 1]$.
  - Continuous dynamic portfolio equity exposure sizing $w_{\\text{equity}}(t) \\in [0.20, 1.00]$ with 20% defensive liquidity floor.
  - White-box anomaly driver attribution decomposing systemic stress into top-3 contributors.
- **Tab 6: \"Macro Mahalanobis Distance\" Module**:
  - Added across both **NiceGUI** (`bubble_detector/ui/dashboard.py`) and **WebAssembly** (`bubble_detector/ui/panel_dashboard.py`).
  - Plots all 8 primary macro traces: Mahalanobis Distance, Bubble Probability, Shiller CAPE, P-CAPE, Buffett Indicator, Housing Price-to-Income, Tech ETF XLK, and TDA Geometric Complexity.
  - Right-flushed vertical legend (`orientation=\"v\", x=1.01`) preventing chart overlap.
  - Three critical regime threshold reference lines: $3.8\\sigma$ (Norm), $5.0\\sigma$ (Warning), $6.2\\sigma$ (Crisis).
- **Dynamic 50-Year Calendar Engine** (`bubble_detector/data/date_horizons.py`):
  - Dynamically calculates start date as exactly 50 physical calendar years prior to execution date.
- **TDA Full-Range Dynamic Normalization $[0.80, 7.00]$**:
  - Replaced static scalar multipliers ($\\times 5$ and $\\times 30$) with `normalize_tda_indicator` mapping raw persistence dispersion to the full $0.80 - 7.00$ visual canvas of Tabs 5 and 6.
  - Added initial sliding-window warm-up backfill eliminating the 30-day zero-flatline gap.
- **Test Suite Expansion**:
  - Added `test_tda_normalization_tabs_5_and_6` asserting $\\max(y) \\ge 6.8$ and $\\min(y) \\ge 0.20$.
  - Expanded total automated tests to **32 passed (100% pass rate)**.

#### Fixed
- **TDA ~0.9 Max Value Bottleneck**: Resolved issue where TDA Geometric Complexity was trapped below $0.96$ on charts spanning $0$ to $7$.
- **Exchange Holiday Data Discontinuity**: Fixed holiday forward-fill in `DataIngestor` to eliminate artificial single-day $150\\%$ return spikes on market holidays.
- **Ill-Conditioned Matrix Inversion Artifacts**: Upgraded Tikhonov ridge regularization to $\\lambda = 10^{-2}$ to prevent early-window matrix singularity spikes.

---

### [v1.0.0] - 2026-08-05

#### Added
- Initial enterprise release of the Multidimensional Market Bubble Detector.
- 5 core analytical modules: Macro Valuation, Systemic Leverage, Econometric Explosive Bubble, Sentiment & Volatility, and Sector Health.
- Dual runtime architecture: NiceGUI desktop application and HoloViz Panel WebAssembly (Pyodide) client-side bundle.
- 15 quantitative financial indicators with 100% numerical parity between Python and WebAssembly.
- Initial automated test suite across feature extraction, ML forecasting, and UI WCAG accessibility.

---

## 📜 License
Licensed under the **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International Public License (CC BY-NC-ND 4.0)**. Developed for quantitative systemic risk assessment, econometric research, and non-linear macroeconomic regime analysis. See the [`LICENSE`](LICENSE) file for complete legal terms.
