---
trigger: always_on
description: Institutional architecture, econometric guidelines, testing constraints, and zero-lookahead rules for autonomous coding agents.
---

# System Architecture and Operational Rules for Agents

## 1. Core Econometric & Statistical Rules
- **Signed Mahalanobis Projection**: Always utilize the pre-registered directional vector $\mathbf{b} \in \{-1, +1\}^{15}$ and projection $s_t = \frac{\mathbf{b}^\top \mathbf{\Sigma}^{-1} (\mathbf{z}_t - \boldsymbol{\mu})}{\sqrt{\mathbf{b}^\top \mathbf{\Sigma}^{-1} \mathbf{b}}}$ rather than isotropic Mahalanobis distance. This guarantees market-liquidation crash bottoms (e.g., March 2020, October 2008) are treated as undervaluation buying opportunities ($w_{\text{equity}} \ge 0.80$) rather than de-risking events.
- **Strictly Causal Expanding Statistics**: Zero lookahead bias allowed. Standardize features using strictly causal expanding-window mean and standard deviation during warm-up periods before full rolling windows are populated.
- **Purged-Embargo Walk-Forward CV**: For predictive models (e.g. forward 20-day drawdown risk), enforce an explicit 20-day purge gap between train and validation splits. Terminal unobservable rows must be masked during training.
- **Zero Synthetic Gaussian Bumps**: The test suite (`tests/test_no_gaussian_bumps.py`) audits all data ingestion files for forbidden synthetic curves (`exp(-((years - ...)**2))`). Ingest real ground-truth point-in-time series from `data/provenance/` with mandatory publication lags (FRED +60d, FINRA +21d, Shiller +5d).
- **Continuous Splicing Compounding**: Never stitch financial time series by level shifting or raw concatenation. Use backward continuous return compounding ($P_{t-1} = P_t \cdot S_{t-1} / S_t$) anchored at the first valid observation of the target series to ensure seam price jumps remain $< 3\%$.

## 2. Directory Layout & Key Modules
- `bubble_detector/data/`: Ingestion, ETL pipelines, and date horizon logic (`date_horizons.py`, `etl_shiller.py`, `etl_fred.py`, `etl_finra.py`, `etl_vxo.py`, `ingestor.py`).
- `bubble_detector/features/`: Indicators and feature extraction (`technicals.py`, `macro_valuation.py`, `leverage.py`, `econometric.py`, `topology.py`, `options_vol.py`, `utils.py`).
- `bubble_detector/models/`: Regime detection and predictive models (`regime_mahalanobis.py`, `structural_breaks.py`).
- `bubble_detector/backtest/`: Backtest simulation and historical validation (`engine.py`, `validation_table.py`).
- `bubble_detector/ui/`: Presentation and visualization (`dashboard.py`, `panel_dashboard.py`, `postprocess_wasm.py`, `ui_theme.py`).

## 3. Execution & Verification Rules
- **Virtualenv**: Use `./.venv/bin/python` and `./.venv/bin/pytest`.
- **Command Execution**: Always run commands with `BypassSandbox: true` due to macOS Nix store dylib resolution.
- **Verification Protocol**: Before submitting changes, run `./.venv/bin/pytest tests/ -v`. All 72 tests must pass with 100% success rate.
- **Knowledge Graph Synchronization**: Always execute `graphify update .` after code modifications.
