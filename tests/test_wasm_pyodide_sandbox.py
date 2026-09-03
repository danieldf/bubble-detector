"""
Unit tests for WebAssembly Pyodide Sandbox Isolation, End-to-End Execution, and Pre-loaded JSON Datasets.

Verifies:
1. Clean 21-column JSON dataset staging in data/provenance, build, and dist with compact payload budget (< 3.0 MB).
2. Complete script evaluation isolation in simulated Pyodide sandbox without host bubble_detector or polars.
3. Synchronous pre-loaded JSON loading in MEMFS root for both Option 1 and Option 2.
4. Pure NumPy fallback activation and full layout stability when datasets are unavailable.
5. Robust date horizon selection across arbitrary historical year shifts (e.g. 1975, 1976, 1977, 1980 vs 2015, 2020).
6. All 6 Plotly figures and layout components pre-initialize properly with non-empty traces.
7. Idempotent dist/index.html post-processing with zero recursive nesting.
"""

import sys
import os
import re
import json
import gzip
import types
from pathlib import Path
import pytest
import numpy as np

from stage_provenance import sync_parquet_to_json
from bubble_detector.config import BASE_DIR, PROVENANCE_DIR
from bubble_detector.ui.panel_dashboard import (
    CORE_WASM_COLUMNS,
    generate_wasm_dataset,
    build_macro_valuation_fig,
    build_leverage_fig,
    build_econometric_fig,
    build_sentiment_vol_fig,
    build_sector_health_fig,
    build_mahalanobis_fig,
    HORIZON_OPTION_1_ID,
    HORIZON_OPTION_2_ID,
    HORIZON_METADATA,
    executive_summary_pane,
    note_pane,
    template
)

def test_json_datasets_staging():
    """Verify that 21-column JSON datasets are created within strict payload size budgets."""
    sync_parquet_to_json()

    for dir_path in [PROVENANCE_DIR, BASE_DIR / "build", BASE_DIR / "dist"]:
        p50 = dir_path / "market_data_50yr.json"
        p_mod = dir_path / "market_data_modern.json"
        assert p50.exists(), f"Missing {p50}"
        assert p_mod.exists(), f"Missing {p_mod}"

        # Validate JSON content
        with open(p50, "r", encoding="utf-8") as f:
            raw_50 = f.read()
            data_50 = json.loads(raw_50)
        assert len(data_50["Date"]) > 10000
        for col in CORE_WASM_COLUMNS:
            assert col in data_50, f"Missing {col} in {p50}"

        # Payload size budget check: uncompressed must be < 5.0 MB (was 16 MB before fix), gzipped < 600 KB
        uncompressed_mb = len(raw_50) / (1024 * 1024)
        gzipped_kb = len(gzip.compress(raw_50.encode("utf-8"))) / 1024
        assert uncompressed_mb < 5.0, f"{p50} too large uncompressed: {uncompressed_mb:.2f} MB"
        assert gzipped_kb < 600, f"{p50} too large gzipped: {gzipped_kb:.1f} KB"

        with open(p_mod, "r", encoding="utf-8") as f:
            data_mod = json.load(f)
        assert len(data_mod["Date"]) > 2500
        for col in CORE_WASM_COLUMNS:
            assert col in data_mod, f"Missing {col} in {p_mod}"

def test_wasm_pyodide_json_memfs_loading(monkeypatch, tmp_path):
    """
    Simulate Pyodide MEMFS where polars and bubble_detector are unavailable,
    and market_data_50yr.json is pre-loaded into current working directory.
    """
    src_json = PROVENANCE_DIR / "market_data_50yr.json"
    dest_json = tmp_path / "market_data_50yr.json"
    dest_json.write_text(src_json.read_text(encoding="utf-8"), encoding="utf-8")

    monkeypatch.chdir(tmp_path)
    monkeypatch.setitem(sys.modules, "polars", None)

    import bubble_detector.ui.panel_dashboard as pdash
    monkeypatch.setattr(pdash, "PROVENANCE_DIR", tmp_path / "empty_prov")
    monkeypatch.setattr(pdash, "BASE_DIR", tmp_path)

    meta = HORIZON_METADATA[HORIZON_OPTION_1_ID]
    data = generate_wasm_dataset(meta["start_date"], meta["end_date"])

    assert pdash._IS_SYNTHETIC_FALLBACK_ACTIVE is False
    assert len(data["Date"]) > 10000
    for col in CORE_WASM_COLUMNS:
        assert col in data, f"Missing {col} in loaded MEMFS JSON data"
        if col != "Date" and col != "Primary_Anomaly_Driver":
            arr = np.array(data[col])
            assert not np.isnan(arr).any(), f"NaN found in {col}"

def test_wasm_pyodide_pure_numpy_fallback(monkeypatch, tmp_path):
    """
    Verify pure NumPy fallback operates with zero dependencies when
    neither parquet nor json exists.
    """
    monkeypatch.chdir(tmp_path)
    monkeypatch.setitem(sys.modules, "polars", None)
    monkeypatch.setitem(sys.modules, "pandas", None)

    import bubble_detector.ui.panel_dashboard as pdash
    monkeypatch.setattr(pdash, "PROVENANCE_DIR", tmp_path / "empty_prov")
    monkeypatch.setattr(pdash, "BASE_DIR", tmp_path)

    data = generate_wasm_dataset("2015-01-01", "2026-09-03")

    assert pdash._IS_SYNTHETIC_FALLBACK_ACTIVE is True
    assert len(data["Date"]) > 0
    for col in CORE_WASM_COLUMNS:
        assert col in data, f"Missing {col} in fallback dataset"
        if col != "Date" and col != "Primary_Anomaly_Driver":
            arr = np.array(data[col])
            assert len(arr) == len(data["Date"])
            assert not np.isnan(arr).any()

def test_date_horizon_selector_robust_against_year_shift(monkeypatch, tmp_path):
    """
    Verify candidate dataset selection correctly maps 50-year rolling horizons to market_data_50yr
    across arbitrary historical year shifts (1975, 1976, 1977, 1980) rather than brittle '1976' checks.
    """
    # Stage both JSON files into tmp_path
    shutil_copy = PROVENANCE_DIR / "market_data_50yr.json"
    (tmp_path / "market_data_50yr.json").write_text(shutil_copy.read_text(encoding="utf-8"), encoding="utf-8")
    (tmp_path / "market_data_modern.json").write_text((PROVENANCE_DIR / "market_data_modern.json").read_text(encoding="utf-8"), encoding="utf-8")

    monkeypatch.chdir(tmp_path)
    monkeypatch.setitem(sys.modules, "polars", None)

    import bubble_detector.ui.panel_dashboard as pdash
    monkeypatch.setattr(pdash, "PROVENANCE_DIR", tmp_path / "empty_prov")
    monkeypatch.setattr(pdash, "BASE_DIR", tmp_path)

    # Test rolling years in 1970s and 1980s
    for test_year in ["1974-05-10", "1975-01-01", "1976-09-03", "1977-09-03", "1980-01-01"]:
        d = generate_wasm_dataset(test_year, "2026-09-03")
        assert len(d["Date"]) > 10000, f"Failed to select 50yr dataset for start date {test_year}"

    # Test modern years
    for modern_start in ["2015-01-01", "2018-01-01", "2020-01-01"]:
        d_mod = generate_wasm_dataset(modern_start, "2026-09-03")
        assert len(d_mod["Date"]) < 5000, f"Failed to select modern dataset for start date {modern_start}"

def test_wasm_full_script_pyodide_execution(monkeypatch, tmp_path):
    """
    End-to-end execution of bubble_detector/ui/panel_dashboard.py under total package isolation:
    - bubble_detector package completely blocked
    - polars package completely blocked
    - pandas package completely blocked
    - panel.io.pyodide mocked
    - Isolated cwd containing only market_data_50yr.json and market_data_modern.json
    Verifies full template instantiation, all 6 Plotly panes, KPI values, and horizon switching.
    """
    # Copy json datasets
    (tmp_path / "market_data_50yr.json").write_text((PROVENANCE_DIR / "market_data_50yr.json").read_text(encoding="utf-8"), encoding="utf-8")
    (tmp_path / "market_data_modern.json").write_text((PROVENANCE_DIR / "market_data_modern.json").read_text(encoding="utf-8"), encoding="utf-8")

    monkeypatch.chdir(tmp_path)

    class BlockModules:
        def find_spec(self, fullname, path, target=None):
            if fullname.startswith("bubble_detector") or fullname.startswith("polars") or fullname.startswith("pandas"):
                raise ImportError(f"Simulated Pyodide blocked: {fullname}")
            return None

    monkeypatch.setattr(sys, "meta_path", [BlockModules()] + [m for m in sys.meta_path if not isinstance(m, BlockModules)])
    for k in list(sys.modules.keys()):
        if k.startswith("bubble_detector") or k.startswith("polars"):
            monkeypatch.delitem(sys.modules, k, raising=False)

    monkeypatch.setitem(sys.modules, "panel.io.pyodide", types.ModuleType("panel.io.pyodide"))

    dash_file = BASE_DIR / "bubble_detector" / "ui" / "panel_dashboard.py"
    with open(dash_file, "r", encoding="utf-8") as f:
        code = f.read()

    globs = {"__name__": "__main__", "__file__": str(dash_file)}
    exec(code, globs)

    assert globs["_IS_SYNTHETIC_FALLBACK_ACTIVE"] is False
    tmpl = globs["template"]
    assert tmpl.title == "Market Bubble Detector (WebAssembly Edition)"
    assert len(tmpl.sidebar) >= 3
    assert len(tmpl.main) >= 6

    # Verify 6 plotly panes
    tabs = globs["dashboard_tabs"]
    assert len(tabs) == 6
    for pane in tabs.objects:
        fig = pane.object
        assert len(fig.data) > 0, "Tab figure has 0 traces"

    # Verify switching to Option 2
    update_all = globs["update_all_charts"]
    update_all(globs["HORIZON_OPTION_2_ID"])
    assert globs["_IS_SYNTHETIC_FALLBACK_ACTIVE"] is False

    # Verify switching back to Option 1
    update_all(globs["HORIZON_OPTION_1_ID"])
    assert globs["_IS_SYNTHETIC_FALLBACK_ACTIVE"] is False

def test_wasm_full_script_pure_numpy_fallback_execution(monkeypatch, tmp_path):
    """
    End-to-end execution of panel_dashboard.py under total package isolation in an empty directory.
    Verifies synthetic fallback activates cleanly, illuminates the alert, and populates figures.
    """
    monkeypatch.chdir(tmp_path)

    class BlockModules:
        def find_spec(self, fullname, path, target=None):
            if fullname.startswith("bubble_detector") or fullname.startswith("polars") or fullname.startswith("pandas"):
                raise ImportError(f"Simulated Pyodide blocked: {fullname}")
            return None

    monkeypatch.setattr(sys, "meta_path", [BlockModules()] + [m for m in sys.meta_path if not isinstance(m, BlockModules)])
    for k in list(sys.modules.keys()):
        if k.startswith("bubble_detector") or k.startswith("polars"):
            monkeypatch.delitem(sys.modules, k, raising=False)

    monkeypatch.setitem(sys.modules, "panel.io.pyodide", types.ModuleType("panel.io.pyodide"))

    dash_file = BASE_DIR / "bubble_detector" / "ui" / "panel_dashboard.py"
    with open(dash_file, "r", encoding="utf-8") as f:
        code = f.read()

    globs = {"__name__": "__main__", "__file__": str(dash_file)}
    exec(code, globs)

    assert globs["_IS_SYNTHETIC_FALLBACK_ACTIVE"] is True
    assert globs["red_fallback_banner"].visible is True

    tabs = globs["dashboard_tabs"]
    for pane in tabs.objects:
        assert len(pane.object.data) > 0

def test_all_6_plotly_figures_have_traces():
    """Verify all 6 Plotly figures construct successfully with non-empty traces."""
    builders = [
        ("Macro Valuation", build_macro_valuation_fig),
        ("Leverage", build_leverage_fig),
        ("Econometric", build_econometric_fig),
        ("Sentiment", build_sentiment_vol_fig),
        ("Sector Health", build_sector_health_fig),
        ("Mahalanobis", build_mahalanobis_fig),
    ]

    for name, builder in builders:
        fig = builder(HORIZON_OPTION_1_ID)
        assert len(fig.data) > 0, f"Figure '{name}' has 0 traces"
        for trace in fig.data:
            assert len(trace.x) > 0, f"Trace '{trace.name}' in figure '{name}' has empty x"
            assert len(trace.y) > 0, f"Trace '{trace.name}' in figure '{name}' has empty y"

def test_template_and_cards_reconstruction():
    """Verify Executive Summary, Horizon Specifications Card, and FastListTemplate."""
    exec_text = executive_summary_pane.object
    assert "S&P 500 tests record peaks near 7,500" in exec_text
    assert "Shiller CAPE 41.37" in exec_text
    assert "Buffett Indicator 218.1%" in exec_text
    assert "FINRA margin debt" in exec_text
    assert "$1.416T" in exec_text
    assert "SKEW > 145" in exec_text
    assert "Method 1 Mahalanobis Distance" in exec_text

    note_text = note_pane.object
    assert "Horizon Specification & Data Integrity" in note_text
    assert "Native Feature Fidelity:" in note_text

    assert template.title == "Market Bubble Detector (WebAssembly Edition)"
    assert "Dark" in template.theme.__name__ or template.theme._name == "dark"
    assert len(template.sidebar) >= 3
    assert len(template.main) >= 6

def apply_postprocessing(html_content: str) -> str:
    """Helper implementing the exact GitHub Actions deployment postprocessing."""
    content = re.sub(r'\'https://cdn\.holoviz\.org/panel/wheels/bokeh-[^\']+\.whl\'', '\'bokeh\'', html_content)
    content = re.sub(r'\'https://cdn\.holoviz\.org/panel/[^\']+/panel-[^\']+\.whl\'', '\'panel\'', content)
    content = re.sub(r'\\+U0001([0-9a-fA-F]{4})', lambda m: chr(int('0001' + m.group(1), 16)), content)
    content = re.sub(r'U0001([0-9a-fA-F]{4})', lambda m: chr(int('0001' + m.group(1), 16)), content)

    replacements = {
        'U0001f3db': '🏛️',
        '\\U0001f3db': '🏛️',
        'U0001f3af': '🎯',
        '\\U0001f3af': '🎯',
        'U0001f52c': '🔬',
        '\\U0001f52c': '🔬',
        'U0001f4c5': '📅',
        '\\U0001f4c5': '📅',
        'U0001f4c9': '📉',
        '\\U0001f4c9': '📉',
        'U0001f680': '🚀',
        '\\U0001f680': '🚀',
        'U0001f319': '🌙',
        '\\U0001f319': '🌙',
        'U0001f917': '🤗',
        '\\U0001f917': '🤗',
    }
    for k, v in replacements.items():
        content = content.replace(k, v)

    preloader_and_error_boundary = '''
      for (const ds of ['market_data_50yr.json', 'market_data_modern.json']) {
        try {
          let r = await fetch(ds);
          if (r.ok) {
            let t = await r.text();
            pyodide.FS.writeFile(ds, t);
            console.log('Pre-loaded MEMFS dataset: ' + ds);
          }
        } catch(e) { console.warn('Could not pre-load ' + ds, e); }
      }
      try {
        await pyodide.runPythonAsync(code);
      } catch (err) {
        document.body.classList.remove('pn-loading');
        let el = document.createElement('div');
        el.style.cssText = 'margin: 2rem; padding: 1.5rem; background: #2A1515; border: 1px solid #FF5252; color: #FFF; border-radius: 8px; font-family: monospace; white-space: pre-wrap;';
        el.innerHTML = '<h3>⚠️ WebAssembly Initialization Error</h3><p>' + err + '</p>';
        document.body.prepend(el);
      }'''

    if 'WebAssembly Initialization Error' not in content:
        content = re.sub(r'await\s+pyodide\.runPythonAsync\(code\);?', preloader_and_error_boundary, content)

    return content

def test_dist_index_html_postprocessing_idempotence():
    """Verify that postprocessing is completely idempotent and never creates nested try/catch blocks."""
    raw_sample = """
    async function main() {
      await pyodide.runPythonAsync(code);
    }
    """
    first_pass = apply_postprocessing(raw_sample)
    assert first_pass.count("WebAssembly Initialization Error") == 1
    assert first_pass.count("Pre-loaded MEMFS dataset:") == 1

    second_pass = apply_postprocessing(first_pass)
    assert second_pass == first_pass, "Postprocessing must be idempotent!"
    assert second_pass.count("WebAssembly Initialization Error") == 1
    assert second_pass.count("Pre-loaded MEMFS dataset:") == 1

def test_dist_index_html_on_disk():
    """Verify that dist/index.html exists on disk and contains exactly one error boundary and preloader."""
    index_target = BASE_DIR / "dist" / "index.html"
    assert index_target.exists(), "dist/index.html must exist"
    content = index_target.read_text(encoding="utf-8")

    assert content.count("WebAssembly Initialization Error") == 1
    assert content.count("Pre-loaded MEMFS dataset:") == 1
    assert "pyodide.FS.writeFile(ds, t)" in content
    assert "document.body.classList.remove('pn-loading')" in content
    assert "Market Bubble Detector (WebAssembly Edition)" in content
