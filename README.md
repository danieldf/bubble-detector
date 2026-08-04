# 📉 Multidimensional Market Bubble Detector & Structural Break System

[![Deploy WebAssembly Dashboard](https://github.com/danieldf/bubble-detector/actions/workflows/deploy.yml/badge.svg)](https://github.com/danieldf/bubble-detector/actions/workflows/deploy.yml)
[![Live WebAssembly Dashboard](https://img.shields.io/badge/Live_Dashboard-GitHub_Pages-0288D1?style=flat&logo=github)](https://danieldf.github.io/bubble-detector/)

An enterprise-grade quantitative econometric system and machine learning framework designed to detect financial asset bubbles, diagnose macro regime shifts, and predict structural market crash probabilities. 

---

## 🌟 Live Interactive WebAssembly Dashboard

🚀 **[Access the Live Panel WebAssembly Dashboard on GitHub Pages](https://danieldf.github.io/bubble-detector/)**

*(Compiled directly to WebAssembly using HoloViz Panel & Pyodide — runs 100% client-side in your browser with zero backend server required!)*

---

## 📅 Multi-Horizon Date Range Selector

The system supports dual calibration horizons for model parameter tuning and regime walk-forward validation:

| Horizon Option | Date Bounds | Regimes | Native Feature Fidelity | Target Coverage |
| :--- | :--- | :--- | :--- | :--- |
| **Option 1: Modern 5-Regime Horizon** | `2015-01-01` to `2026-07-28` | 5 Regimes | **100% Native High-Fidelity** | 2018 Volmageddon, 2020 COVID Flash Crash, 2020–2021 Post-COVID Exuberance, 2022 Fed Rate Hikes, 2024–2026 AI CapEx Rally |
| **Option 2: Expanded 7-Regime Horizon** | `1998-01-01` to `2026-07-28` | 7 Regimes | **~92% Extended Historical Spectrum** | Spans all 7 major crashes including **1999–2000 Dot-Com Peak (CAPE 44.19)** and **2007–2009 Subprime GFC (Housing PTI ~7.0x)** |

---

## 📊 5 Interactive Dashboard Modules

1. **Macro Valuation Anchors**: Tracks Shiller CAPE (41.37), Payout-Adjusted CAPE (P-CAPE), and the Buffett Indicator (218.1% of GDP) against historical quintile bands.
2. **Systemic Liquidity & Leverage**: Monitors FINRA Margin Debt ($1.416T Peak), YoY velocity, and excess debt capacity ("Margin Exhaustion Score").
3. **Econometric Explosive Bubble Diagnostics**: Computes Generalized Supremum ADF (GSADF / PSY Procedure) with General-Purpose Technology (GPT) decomposition filtering $754B AI CapEx shocks.
4. **Options Sentiment & Behavioral Tracking**: Analyzes VIX contango term structure (VIX1D vs VIX3M), CBOE SKEW tail-risk alerts (>145), and OVX/VIX cross-asset volatility decoupling.
5. **Sector Vulnerability & Topological Dynamics**: Measures Housing Price-to-Income affordability (7.11x) alongside Topological Data Analysis (TDA) persistence landscape L2 norm and Morlet wavelet complexity scores.

---

## 💻 Local Setup & Execution

### 1. Installation
```bash
git clone https.github.com/danieldf/bubble-detector.git
cd bubble-detector
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

### 2. Run Local NiceGUI App
```bash
python -m bubble_detector.ui.dashboard
```
*Navigates to `http://localhost:8080`*

### 3. Run Local Panel (HoloViz) App
```bash
panel serve bubble_detector/ui/panel_dashboard.py --show
```
*Navigates to `http://localhost:5006`*

### 4. Build WebAssembly Bundle Locally
```bash
panel convert bubble_detector/ui/panel_dashboard.py --to pyodide-worker --out dist/
python -m http.server 8000 --directory dist/
```

---

## 🧪 Running Unit & Integration Tests

```bash
pytest tests/
```

---

## 📜 License
MIT License. Developed for quantitative systemic risk assessment and econometric research.
