"""
Global Pytest Configuration and Test Fixtures.
==============================================
Ensures test environment prerequisites are satisfied prior to running test suites.
"""

import pytest
from pathlib import Path
import polars as pl

from bubble_detector.config import PROVENANCE_DIR
from bubble_detector.ui.panel_dashboard import HORIZON_OPTION_1_ID, HORIZON_METADATA


@pytest.fixture(scope="session", autouse=True)
def ensure_synchronized_wasm_datasets():
    """
    Ensure that staged WebAssembly Parquet and JSON datasets are strictly synchronized
    with the dynamic horizon dates for the active session. If datasets are absent or
    out of date relative to HORIZON_METADATA, automatically precompiles them once.
    """
    p50 = PROVENANCE_DIR / "market_data_50yr.parquet"
    target_end = HORIZON_METADATA[HORIZON_OPTION_1_ID]["end_date"]

    needs_compilation = True
    if p50.exists():
        try:
            df = pl.read_parquet(p50)
            max_date = str(df["Date"].max())[:10]
            if max_date == target_end:
                needs_compilation = False
        except Exception:
            needs_compilation = True

    if needs_compilation:
        from stage_provenance import precompile_wasm_parquet_datasets
        precompile_wasm_parquet_datasets()
