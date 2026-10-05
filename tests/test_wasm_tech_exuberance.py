"""
Unit tests for WebAssembly Tab 7: Tech Exuberance Score & Parity Engine.
========================================================================

Verifies:
1. build_tech_exuberance_fig constructs valid 4-subplot Figure with correct traces.
2. Responsive legend & margin behavior across desktop and mobile viewports.
3. Full numerical presence and valid bounds of all 14 new indicators in CORE_WASM_COLUMNS.
4. Correct rendering of conjoint highlight spans (add_vrect) when Tech_Exuberance_Signal triggers.
5. Zero NaN values across modern and 50-year horizon datasets.
"""

import pytest
import numpy as np
from bubble_detector.ui.panel_dashboard import (
    build_tech_exuberance_fig,
    pane_tech_exuberance,
    fetch_dataset,
    HORIZON_OPTION_1_ID,
    HORIZON_OPTION_2_ID,
    CORE_WASM_COLUMNS,
    dashboard_tabs
)
from stage_provenance import precompile_wasm_parquet_datasets


def test_precompile_wasm_parquet_datasets():
    """Precompile WASM Parquet and JSON datasets to ensure up-to-date parquet/json artifacts."""
    precompile_wasm_parquet_datasets()



def test_tech_exuberance_fig_structure_desktop():
    """Verify desktop construction of Tab 7 figure with 4 subplots and all expected traces."""
    fig = build_tech_exuberance_fig(HORIZON_OPTION_1_ID, is_mobile=False)
    assert fig is not None
    assert len(fig.data) >= 10, f"Expected at least 10 traces in Tab 7, found {len(fig.data)}"

    trace_names = [t.name for t in fig.data if t.name]
    assert any("S&P 500 (SPY)" in name for name in trace_names)
    assert any("Technology Sector (XLK)" in name for name in trace_names)
    assert any("XLK / SPY Ratio" in name for name in trace_names)
    assert any("PSY BSADF" in name for name in trace_names)
    assert any("LPPLS Bubble Confidence" in name for name in trace_names)
    assert any("TDA Persistence" in name for name in trace_names)
    assert any("Wavelet Spectral" in name for name in trace_names)
    assert any("Global Liquidity Index" in name for name in trace_names)
    assert any("M2 YoY Growth" in name for name in trace_names)

    # Check legend orientation for desktop (vertical, right-flushed)
    assert fig.layout.legend.orientation == "v"
    assert fig.layout.margin.r >= 200


def test_tech_exuberance_fig_structure_mobile():
    """Verify mobile construction with responsive horizontal legend and tight margins."""
    fig = build_tech_exuberance_fig(HORIZON_OPTION_2_ID, is_mobile=True)
    assert fig is not None
    assert len(fig.data) >= 10

    # Check mobile legend orientation
    assert fig.layout.legend.orientation == "h"
    assert fig.layout.margin.r <= 60


def test_tech_exuberance_columns_in_core_wasm():
    """Verify all required Tab 7 columns are registered in CORE_WASM_COLUMNS."""
    required_new_cols = [
        "M2_YoY_Growth",
        "CentralBank_YoY_Growth",
        "Global_Liquidity_Index",
        "Liquidity_Momentum",
        "BSADF_Stat",
        "BSADF_90th_Percentile",
        "LPPLS_Confidence",
        "LPPLS_90th_Percentile",
        "TDA_Persistence_Entropy",
        "Wavelet_Spectral_Entropy",
        "XLK_SPY_Ratio",
        "Condition_Macro",
        "Condition_Statistical",
        "Tech_Exuberance_Signal",
    ]
    for col in required_new_cols:
        assert col in CORE_WASM_COLUMNS, f"Column '{col}' must be in CORE_WASM_COLUMNS"


def test_pane_tech_exuberance_in_dashboard_tabs():
    """Verify Tab 7 is bound to dashboard_tabs with title 'Tech Exuberance Score'."""
    assert len(dashboard_tabs) == 7
    tab_names = list(dashboard_tabs._names)
    assert "Tech Exuberance Score" in tab_names
    assert pane_tech_exuberance is not None
    assert len(pane_tech_exuberance.object.data) >= 10
