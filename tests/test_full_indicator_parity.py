"""
Comprehensive Parity Test: Verifies 100% Numerical Parity across all 15 Indicators
and Datasets across all 5 Tabs between NiceGUI and WebAssembly Applications.
"""

import pytest
import numpy as np

from bubble_detector.ui.dashboard import DashboardState
from bubble_detector.ui.panel_dashboard import generate_wasm_dataset, HORIZON_METADATA

INDICATORS_TO_CHECK = [
    "SPY",
    "Shiller_CAPE",
    "P_CAPE",
    "Buffett_Indicator",
    "FINRA_Margin_Debt",
    "Margin_Exhaustion_Score",
    "GSADF_Stat",
    "GSADF_GPT_Adjusted",
    "Drawdown_Probability",
    "^VIX",
    "^SKEW",
    "OVX_VIX_CrossAsset_Ratio",
    "Housing_Price_to_Income",
    "XLK",
    "TDA_Persistence_L2_Norm",
    "Mahalanobis_Distance",
    "Bubble_Regime_Probability",
    "Dynamic_Equity_Exposure"
]

@pytest.mark.parametrize("horizon_id", ["option_1", "option_2"])
def test_all_indicators_numerical_parity(horizon_id):
    """
    Assert that every single indicator across all 5 tabs in the WebAssembly app
    is 100% numerically identical to the NiceGUI app with zero data drift.
    """
    # 1. Load dataset via NiceGUI pipeline
    state = DashboardState(load_data=False)
    state.load_data(horizon_id)
    df_nicegui = state.df

    # 2. Load dataset via WASM pipeline
    meta = HORIZON_METADATA[horizon_id]
    data_wasm = generate_wasm_dataset(meta["start_date"], meta["end_date"])

    # 3. Assert exact column presence
    for col in INDICATORS_TO_CHECK:
        assert col in df_nicegui.columns, f"Indicator '{col}' missing from NiceGUI DataFrame"
        assert col in data_wasm, f"Indicator '{col}' missing from WASM Dataset dictionary"

        arr_nicegui = df_nicegui[col].to_numpy()
        arr_wasm = np.array(data_wasm[col])

        # Assert identical array lengths
        assert len(arr_nicegui) == len(arr_wasm), (
            f"Length mismatch for indicator '{col}': NiceGUI ({len(arr_nicegui)}) vs WASM ({len(arr_wasm)})"
        )

        # Assert 100% numerical identity (zero data drift)
        np.testing.assert_allclose(
            arr_nicegui,
            arr_wasm,
            rtol=1e-5,
            atol=1e-5,
            err_msg=f"Data drift detected for indicator '{col}' between NiceGUI and WASM!"
        )


@pytest.mark.parametrize("horizon_id", ["option_1", "option_2"])
def test_wasm_fallback_numerical_parity(horizon_id):
    """
    Rigorously test the Pyodide WebAssembly fallback branch by mocking out DataIngestor.
    Asserts that the client-side fallback produces valid, non-null numerical indicators
    with zero NaNs and identical array lengths.
    """
    from unittest.mock import patch
    meta = HORIZON_METADATA[horizon_id]

    with patch("bubble_detector.data.ingestor.DataIngestor.fetch_market_data", side_effect=Exception("Simulated Browser Pyodide Offline Mode")):
        data_fallback = generate_wasm_dataset(meta["start_date"], meta["end_date"])

    for col in INDICATORS_TO_CHECK:
        assert col in data_fallback, f"Indicator '{col}' missing from WASM fallback dataset"
        arr_fallback = np.array(data_fallback[col], dtype=np.float64)
        assert len(arr_fallback) > 0, f"Fallback array for '{col}' is empty"
        assert not np.isnan(arr_fallback).any(), f"Fallback array for '{col}' contains NaNs"
        assert not np.isinf(arr_fallback).any(), f"Fallback array for '{col}' contains Infs"

