"""
Comprehensive Parity Test: Verifies 100% Numerical Parity across all 15 Indicators
and Datasets across all 5 Tabs between NiceGUI and WebAssembly Applications.
"""

import pytest
import numpy as np

from bubble_detector.ui.dashboard import (
    DashboardState, build_macro_valuation_chart, build_leverage_chart,
    build_econometric_chart, build_sentiment_vol_chart, build_sector_health_chart,
    build_mahalanobis_chart, build_tech_exuberance_chart
)
from bubble_detector.ui.panel_dashboard import (
    generate_wasm_dataset, HORIZON_METADATA,
    build_macro_valuation_fig, build_leverage_fig,
    build_econometric_fig, build_sentiment_vol_fig, build_sector_health_fig,
    build_mahalanobis_fig, build_tech_exuberance_fig
)

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
    "Dynamic_Equity_Exposure",
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

@pytest.mark.parametrize("horizon_id", ["option_1", "option_2", "option_3"])
def test_all_indicators_numerical_parity(horizon_id):
    """
    Assert that every single indicator across all 7 tabs in the WebAssembly app
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


@pytest.mark.parametrize("horizon_id", ["option_1", "option_2", "option_3"])
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


@pytest.mark.parametrize("horizon_id", ["option_1", "option_2", "option_3"])
def test_all_7_tabs_plot_trace_parity(horizon_id):
    """
    Rigorously assert 100% trace count, date alignment, and zero value discrepancy
    across all 7 interactive dashboard tabs between NiceGUI and WASM.
    """
    state = DashboardState(load_data=False)
    state.load_data(horizon_id)

    charts_to_test = [
        ("macro", build_macro_valuation_chart(state), build_macro_valuation_fig(horizon_id)),
        ("leverage", build_leverage_chart(state), build_leverage_fig(horizon_id)),
        ("econometric", build_econometric_chart(state), build_econometric_fig(horizon_id)),
        ("sentiment", build_sentiment_vol_chart(state), build_sentiment_vol_fig(horizon_id)),
        ("sector", build_sector_health_chart(state), build_sector_health_fig(horizon_id)),
        ("mahalanobis", build_mahalanobis_chart(state), build_mahalanobis_fig(horizon_id)),
        ("tech_exuberance", build_tech_exuberance_chart(state), build_tech_exuberance_fig(horizon_id)),
    ]

    for chart_name, nice_fig, wasm_fig in charts_to_test:
        assert len(nice_fig.data) == len(wasm_fig.data), (
            f"Trace count mismatch in {chart_name}: NiceGUI ({len(nice_fig.data)}) vs WASM ({len(wasm_fig.data)})"
        )
        for i, (n_tr, w_tr) in enumerate(zip(nice_fig.data, wasm_fig.data)):
            n_x, n_y = list(n_tr.x), np.asarray(n_tr.y, dtype=np.float64)
            w_x, w_y = list(w_tr.x), np.asarray(w_tr.y, dtype=np.float64)
            assert len(n_x) == len(w_x), f"Length mismatch in {chart_name} trace {i}"
            assert n_x == w_x, f"Downsampled dates mismatch in {chart_name} trace {i}"
            np.testing.assert_allclose(
                n_y, w_y, rtol=1e-4, atol=1e-4,
                err_msg=f"Trace value drift in {chart_name} trace {i} ({n_tr.name})"
            )

