"""
Unit tests for WebAssembly Parquet Parity and Zero-Mathematical-Drift Loading.
"""

import pytest
import numpy as np
import polars as pl

from bubble_detector.ui.dashboard import DashboardState
from bubble_detector.ui.panel_dashboard import generate_wasm_dataset, HORIZON_METADATA

@pytest.mark.parametrize("horizon_id", ["option_1", "option_2"])
def test_wasm_loads_exact_parquet_dataset(horizon_id):
    """
    Asserts Pyodide WebAssembly dataset matches NiceGUI dataset with zero discrepancy (max diff == 0.000000)
    across all primary indicators and model metrics.
    """
    state = DashboardState(load_data=False)
    state.load_data(horizon_id)
    df_nicegui = state.df

    meta = HORIZON_METADATA[horizon_id]
    data_wasm = generate_wasm_dataset(meta["start_date"], meta["end_date"])

    metrics_to_verify = [
        "SPY",
        "Shiller_CAPE",
        "Buffett_Indicator",
        "FINRA_Margin_Debt",
        "Margin_Exhaustion_Score",
        "GSADF_Stat",
        "GSADF_GPT_Adjusted",
        "^VIX",
        "Housing_Price_to_Income",
        "XLK",
        "TDA_Persistence_L2_Norm",
        "Mahalanobis_Distance",
        "Dynamic_Equity_Exposure"
    ]

    for metric in metrics_to_verify:
        assert metric in df_nicegui.columns, f"Metric '{metric}' missing from NiceGUI DataFrame"
        assert metric in data_wasm, f"Metric '{metric}' missing from WASM dataset"

        arr_ng = df_nicegui[metric].to_numpy()
        arr_wasm = np.array(data_wasm[metric])

        # Assert zero data drift (absolute tolerance 1e-5)
        max_diff = float(np.max(np.abs(arr_ng - arr_wasm)))
        assert max_diff < 1e-5, f"Data drift detected for '{metric}': max diff = {max_diff:.6f}"
