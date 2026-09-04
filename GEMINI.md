## graphify

This project has a knowledge graph at `graphify-out/` with god nodes, community structure, and cross-file relationships.

Rules:
- For codebase questions, first run `graphify query "<question>"` when `graphify-out/graph.json` exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- If `graphify-out/wiki/index.md` exists, use it for broad navigation instead of raw source browsing.
- Read `graphify-out/GRAPH_REPORT.md` only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).

---

## Agent Operational Guide & System Architecture

### 1. Python Environment & Execution Context
- **Project Virtualenv**: Dedicated virtual environment is located at `./.venv/bin/python` with pytest at `./.venv/bin/pytest`.
- **macOS Sandbox Constraints**: On macOS with Nix-installed binaries, subagent terminal commands require `BypassSandbox: true` in `run_command` to permit dynamic library resolution.
- **Python Version**: Python 3.12+. Dependency resolution strictly managed via `uv` or pip using `pyproject.toml` and `requirements.txt`.

### 2. Architectural Blueprint & Directory Layout
```text
bubble_detector/
├── __init__.py           # Version definition (v3.0.0) and top-level exports
├── config.py             # Global constants, paths, logging (RotatingFileHandler), custom exceptions
├── ui_theme.py           # WCAG 2.2 AA contrast engine, Apple human interface styling, 8px rhythm
├── data/                 # Ground-truth point-in-time ETL pipelines and multi-decade horizon anchoring
│   ├── date_horizons.py  # Standalone calendar-anchored 50-year range (1976–2026, 13,045 trading days)
│   ├── etl_shiller.py    # Shiller ie_data.xls (1871–present) monthly S&P prices, CAPE, real earnings
│   ├── etl_fred.py       # FRED Nominal GDP, Case-Shiller HPI, Real Household Income (+60d publication lag)
│   ├── etl_finra.py      # FINRA & NYSE Customer Margin Debt (1959–present, +21d publication lag)
│   ├── etl_vxo.py        # CBOE VXO daily history (1986–present, 150.19 Black Monday peak)
│   └── ingestor.py       # Continuous backward compounding, multi-asset stitching, schema downcasting
├── features/             # Quantitative indicator engines & mathematical signal transforms
│   ├── technicals.py     # MA20/50/200, Bollinger %B, Wilder's RSI, 20d realized volatility
│   ├── macro_valuation.py# CAPE (41.37), P-CAPE, Buffett Indicator (218.1% GDP), CAEY yield
│   ├── leverage.py       # FINRA YoY growth, 20d debt velocity, margin credit exhaustion score
│   ├── econometric.py    # Phillips-Shi-Yu (2015) recursive BSADF, GPT AI CapEx ($754B) decomposition
│   ├── topology.py       # Takens delay embedding (m=3, tau=2), Vietoris-Rips persistent homology, CWT Morlet
│   ├── options_vol.py    # VIX term contango slope, SKEW tail risk (>145), DSPX vs COR3M dispersion
│   └── utils.py          # Central pure-math utilities (expanding z-scores, ADF OLS, TDA scaling)
├── models/               # Institutional statistical & machine learning regime classifiers
│   ├── regime_mahalanobis.py # Regularized Signed Mahalanobis distance with direction vector b in {-1, +1}^15
│   └── structural_breaks.py  # Purged-embargo walk-forward GBDT, isotonic probability calibration
├── backtest/             # Cost-inclusive portfolio simulation & Popperian falsification
│   ├── engine.py         # 15 bps turnover friction, 4.0% cash yield, 2% deadband, Sortino ratio
│   └── validation_table.py # 8-event historical crash validation table (100% warning hit rate, 66.5d lead)
└── ui/                   # Dual-runtime responsive visualization dashboards
    ├── dashboard.py      # NiceGUI server-side interactive 6-tab dashboard
    ├── panel_dashboard.py# HoloViz Panel Pyodide WebAssembly client-side dashboard (100% parity)
    └── postprocess_wasm.py # WebAssembly artifact post-processor (MEMFS loader, emoji sanitizer)
```

### 3. Non-Negotiable Engineering Constraints
1. **Zero Synthetic Gaussian Bumps**:
   - `tests/test_no_gaussian_bumps.py` scans `bubble_detector/data/*.py` for forbidden patterns (`np.exp(-((years - \d+`, `_generate_authentic_*`, `s_volcker =`, etc.).
   - NEVER introduce analytical Gaussian bell curves or hardcoded synthetic spikes into data ingestors.
2. **Continuous Splicing Cliff Elimination**:
   - When splicing modern and historical time series, always use continuous backward return compounding:
     $$P_{t-1} = P_t \times \frac{S_{t-1}}{S_t}$$
   - Guarantee single-day transition seam returns stay strictly $< 3\%$.
3. **Signed Mahalanobis Distance & Direction Vector $\mathbf{b}$**:
   - Do NOT use isotropic Mahalanobis distance for equity de-risking; isotropic distance penalizes deep value bottoms equally with euphoric bubbles.
   - Use pre-registered directional vector $\mathbf{b} \in \{-1, +1\}^{15}$ and projection $s_t = \frac{\mathbf{b}^\top \mathbf{\Sigma}^{-1} (\mathbf{z}_t - \boldsymbol{\mu})}{\sqrt{\mathbf{b}^\top \mathbf{\Sigma}^{-1} \mathbf{b}}}$.
   - Maintain high equity exposure ($w_{\text{equity}} \ge 0.80$) during crash troughs.
4. **Purged-Embargo Cross-Validation & Zero Target Leakage**:
   - When training forward drawdown predictors ($H=20, \theta=0.05$), maintain an explicit 20-day purge gap between train and validation splits.
   - Mask terminal 20 unobservable rows during training.
5. **WebAssembly Parity & MEMFS Mounting**:
   - WebAssembly dashboard in `panel_dashboard.py` mounts pre-staged Parquet tables via Pyodide virtual MEMFS (`pyodide.FS.writeFile`), guaranteeing 100% numerical parity with NiceGUI.
   - Standardize all Plotly visual layouts to right-flushed vertical legends (`orientation="v", x=1.01, y=1.0, margin.r=230`).

### 4. Verification & Testing Workflow
- Run full test suite:
  ```bash
  ./.venv/bin/pytest tests/ -v
  ```
  Expected result: **72 passed tests (100% pass rate)**.
- Anti-synthetic regression verification:
  ```bash
  ./.venv/bin/pytest tests/test_no_gaussian_bumps.py -v
  ```
- Numerical parity verification across runtimes:
  ```bash
  ./.venv/bin/pytest tests/test_full_indicator_parity.py -v
  ```
- After code modifications, always synchronize the knowledge graph:
  ```bash
  graphify update .
  ```

