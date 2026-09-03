"""
Unit tests for Macro Mahalanobis Distance Regime-Switching Bubble Detector (Method 1).
"""

import pytest
import numpy as np
import polars as pl

from bubble_detector.models.regime_mahalanobis import MacroMahalanobisDetector, INDICATORS_15
from bubble_detector.data.ingestor import DataIngestor
from bubble_detector.features import (
    compute_technical_indicators, compute_macro_valuations,
    compute_margin_leverage_metrics, compute_gsadf_gpt_decomposition,
    compute_tda_wavelet_complexity, compute_options_volatility_metrics
)
from bubble_detector.models.structural_breaks import StructuralBreakPredictor

@pytest.fixture
def mock_indicators_df():
    """Generate mock 500-day Polars DataFrame containing all 15 indicators."""
    np.random.seed(42)
    n = 500
    dates = pl.date_range(start=pl.date(2020, 1, 1), end=pl.date(2021, 12, 31), interval="1d", eager=True)[:n]
    
    data = {"Date": dates}
    for col in INDICATORS_15:
        data[col] = (100.0 + np.cumsum(np.random.randn(n))).astype(np.float32)
    
    return pl.DataFrame(data)

def test_stationary_features_shape_and_values(mock_indicators_df):
    detector = MacroMahalanobisDetector(rolling_window=60)
    Z = detector.preprocess_stationary_features(mock_indicators_df)
    
    assert Z.shape == (len(mock_indicators_df), 15)
    assert not np.isnan(Z).any()
    assert not np.isinf(Z).any()
    # Means of z-scores should hover near zero
    assert np.all(np.abs(np.mean(Z[100:], axis=0)) < 1.0)

def test_mahalanobis_distance_non_negative(mock_indicators_df):
    detector = MacroMahalanobisDetector(rolling_window=60)
    Z = detector.preprocess_stationary_features(mock_indicators_df)
    m_dist = detector.compute_mahalanobis_distance(Z)
    
    assert len(m_dist) == len(mock_indicators_df)
    assert not np.isnan(m_dist).any()
    assert np.all(m_dist >= 0.0)

def test_regime_probability_bounds(mock_indicators_df):
    detector = MacroMahalanobisDetector(rolling_window=60)
    Z = detector.preprocess_stationary_features(mock_indicators_df)
    m_dist = detector.compute_mahalanobis_distance(Z)
    probs = detector.compute_regime_probability(m_dist)
    
    assert len(probs) == len(mock_indicators_df)
    assert np.all((probs >= 0.0) & (probs <= 1.0))

def test_dynamic_exposure_bounds_and_monotonicity():
    detector = MacroMahalanobisDetector(min_equity_exposure=0.20)
    test_probs = np.array([0.0, 0.25, 0.50, 0.75, 1.0], dtype=np.float32)
    exposures = detector.compute_dynamic_exposure(test_probs)
    
    assert np.isclose(exposures[0], 1.0)
    assert np.isclose(exposures[-1], 0.20)
    # Monotonically decreasing
    assert np.all(np.diff(exposures) <= 0.0)
    assert np.all((exposures >= 0.20) & (exposures <= 1.0))

def test_anomaly_driver_attribution(mock_indicators_df):
    detector = MacroMahalanobisDetector(rolling_window=60)
    Z = detector.preprocess_stationary_features(mock_indicators_df)
    
    # Intentionally inject massive anomaly into Shiller_CAPE at index 300
    cape_idx = INDICATORS_15.index("Shiller_CAPE")
    Z[300, cape_idx] = 12.5
    
    primary_drivers, summaries = detector.get_top_anomaly_drivers(Z, top_k=3)
    
    assert primary_drivers[300] == "Shiller_CAPE"
    assert "Shiller_CAPE" in summaries[300]
    assert "+12.5σ" in summaries[300]

def test_full_pipeline_polars_integration(tmp_path):
    """End-to-end integration test of MacroMahalanobisDetector on market dataset."""
    ingestor = DataIngestor(cache_dir=tmp_path / "cache")
    df = ingestor.fetch_market_data("2024-01-01", "2026-07-28", use_cache=False)
    df = compute_technical_indicators(df)
    df = compute_macro_valuations(df)
    df = compute_margin_leverage_metrics(df)
    df = compute_gsadf_gpt_decomposition(df)
    df = compute_tda_wavelet_complexity(df)
    df = compute_options_volatility_metrics(df)
    
    predictor = StructuralBreakPredictor()
    probs = predictor.predict_drawdown_probability(df)
    df = df.with_columns(pl.Series("Drawdown_Probability", probs))
    
    detector = MacroMahalanobisDetector(rolling_window=100)
    res_df = detector.process(df)
    
    expected_cols = [
        "Mahalanobis_Distance",
        "Bubble_Regime_Probability",
        "Dynamic_Equity_Exposure",
        "Primary_Anomaly_Driver",
        "Anomaly_Summary"
    ]
    for col in expected_cols:
        assert col in res_df.columns
        assert res_df[col].null_count() == 0

def test_tab6_figure_traces_and_right_flushed_legend():
    """Verify that Tab 6 contains all 8 traces with right-flushed legend in both NiceGUI and Panel."""
    from bubble_detector.ui.dashboard import DashboardState, build_mahalanobis_chart
    from bubble_detector.ui.panel_dashboard import build_mahalanobis_fig, HORIZON_OPTION_1_ID

    state = DashboardState(load_data=False)
    state.load_data("option_1")

    fig_nice = build_mahalanobis_chart(state)
    fig_panel = build_mahalanobis_fig(HORIZON_OPTION_1_ID)

    expected_traces = [
        "Macro Mahalanobis Distance (DM)",
        "Bubble Regime Probability (scaled x10)",
        "Shiller CAPE (scaled / 5)",
        "P-CAPE (scaled / 5)",
        "Buffett Indicator (scaled / 25)",
        "Housing Price-to-Income (7.11x Peak)",
        "Tech ETF XLK (scaled / 100)",
        "TDA Geometric Complexity (Normalized)"
    ]

    for fig, name in [(fig_nice, "NiceGUI"), (fig_panel, "Panel WASM")]:
        assert len(fig.data) == 8, f"{name} should have exactly 8 traces, got {len(fig.data)}"
        trace_names = [t.name for t in fig.data]
        for exp in expected_traces:
            assert any(exp in t for t in trace_names), f"Missing trace '{exp}' in {name}: got {trace_names}"
        
        # Verify provenance badging on every trace
        for t in fig.data:
            assert any(badge in t.name for badge in ["[REAL]", "[PROXY]", "[SYNTHETIC]"]), (
                f"Trace '{t.name}' in {name} is missing institutional provenance tag"
            )
        
        # Verify right-flushed vertical legend
        assert fig.layout.legend.orientation == "v", f"{name} legend orientation should be 'v'"
        assert fig.layout.legend.x >= 1.0, f"{name} legend x should be right-flushed (>= 1.0), got {fig.layout.legend.x}"
        assert fig.layout.yaxis.rangemode == "tozero", f"{name} yaxis rangemode should be 'tozero'"

def test_tab6_all_traces_finite_and_bounded():
    """Verify that all 8 traces plotted on Tab 6 have 0 NaNs and fall cleanly within [0, 13.0]."""
    from bubble_detector.ui.dashboard import DashboardState, build_mahalanobis_chart

    state = DashboardState(load_data=False)
    for horizon_id in ["option_1", "option_2"]:
        state.load_data(horizon_id)
        fig = build_mahalanobis_chart(state)
        for trace in fig.data:
            y_arr = np.array(trace.y, dtype=np.float64)
            assert not np.isnan(y_arr).any(), f"Trace '{trace.name}' has NaNs in {horizon_id}"
            assert not np.isinf(y_arr).any(), f"Trace '{trace.name}' has Infs in {horizon_id}"
            assert np.min(y_arr) >= 0.0, f"Trace '{trace.name}' has negative values in {horizon_id}: {np.min(y_arr)}"
            assert np.max(y_arr) <= 13.0, f"Trace '{trace.name}' exceeds 13.0 threshold in {horizon_id}: {np.max(y_arr)}"


def test_tda_normalization_tabs_5_and_6():
    """Verify that TDA Geometric Complexity on BOTH Tab 5 and Tab 6 spans the 0 to 7 y-range and max achieves ~7.0."""
    from bubble_detector.ui.dashboard import DashboardState, build_sector_health_chart, build_mahalanobis_chart
    from bubble_detector.ui.panel_dashboard import build_sector_health_fig, build_mahalanobis_fig

    state = DashboardState(load_data=False)
    for horizon_id in ["option_1", "option_2"]:
        state.load_data(horizon_id)
        
        figs = [
            (build_sector_health_chart(state), f"NiceGUI Tab 5 ({horizon_id})"),
            (build_mahalanobis_chart(state), f"NiceGUI Tab 6 ({horizon_id})"),
            (build_sector_health_fig(horizon_id), f"WASM Tab 5 ({horizon_id})"),
            (build_mahalanobis_fig(horizon_id), f"WASM Tab 6 ({horizon_id})"),
        ]

        for fig, label in figs:
            tda_traces = [t for t in fig.data if "TDA Geometric Complexity" in t.name]
            assert len(tda_traces) == 1, f"Expected 1 TDA trace in {label}, found {len(tda_traces)}"
            y_arr = np.array(tda_traces[0].y, dtype=np.float64)
            
            assert not np.isnan(y_arr).any(), f"TDA contains NaNs in {label}"
            assert not np.isinf(y_arr).any(), f"TDA contains Infs in {label}"
            
            # 1. Max must achieve ~7.0 (spanning the 0 to 7 y-range, NOT stalling at ~0.9)
            assert np.max(y_arr) >= 6.8, f"TDA max {np.max(y_arr)} is too low in {label} (expected ~7.0)"
            assert np.max(y_arr) <= 7.1, f"TDA max {np.max(y_arr)} exceeds 7.1 in {label}"
            
            # 2. Min must be strictly >= 0.20 (baseline at 0.80, never squishing into zero)
            assert np.min(y_arr) >= 0.20, f"TDA min {np.min(y_arr)} is below 0.20 in {label}"
            assert np.min(y_arr) <= 1.0, f"TDA min {np.min(y_arr)} is unexpectedly high in {label}"
            
            # 3. Median must sit comfortably in the causal expanding band (0.8 to 6.8)
            assert 0.8 <= np.median(y_arr) <= 6.8, f"TDA median {np.median(y_arr)} out of expected range in {label}"


def test_all_tabs_legends_right_flushed():
    """Verify that ALL tabs 1 to 6 in both NiceGUI and WASM use right-flushed vertical legends."""
    from bubble_detector.ui.dashboard import (
        DashboardState,
        build_macro_valuation_chart,
        build_leverage_chart,
        build_econometric_chart,
        build_sentiment_vol_chart,
        build_sector_health_chart,
        build_mahalanobis_chart,
    )
    from bubble_detector.ui.panel_dashboard import (
        build_macro_valuation_fig,
        build_leverage_fig,
        build_econometric_fig,
        build_sentiment_vol_fig,
        build_sector_health_fig,
        build_mahalanobis_fig,
    )

    state = DashboardState(load_data=False)
    state.load_data("option_1")

    all_figs = [
        ("NiceGUI Tab 1", build_macro_valuation_chart(state)),
        ("NiceGUI Tab 2", build_leverage_chart(state)),
        ("NiceGUI Tab 3", build_econometric_chart(state)),
        ("NiceGUI Tab 4", build_sentiment_vol_chart(state)),
        ("NiceGUI Tab 5", build_sector_health_chart(state)),
        ("NiceGUI Tab 6", build_mahalanobis_chart(state)),
        ("WASM Tab 1", build_macro_valuation_fig("option_1")),
        ("WASM Tab 2", build_leverage_fig("option_1")),
        ("WASM Tab 3", build_econometric_fig("option_1")),
        ("WASM Tab 4", build_sentiment_vol_fig("option_1")),
        ("WASM Tab 5", build_sector_health_fig("option_1")),
        ("WASM Tab 6", build_mahalanobis_fig("option_1")),
    ]

    for label, fig in all_figs:
        assert fig.layout.legend.orientation == "v", f"{label} legend orientation should be 'v', got {fig.layout.legend.orientation}"
        assert fig.layout.legend.x >= 1.0, f"{label} legend x should be >= 1.0 (right-flushed), got {fig.layout.legend.x}"
        assert fig.layout.margin.r >= 200, f"{label} right margin should be >= 200 to accommodate right legend, got {fig.layout.margin.r}"


def test_mahalanobis_no_early_rank_singularity():
    """Verify that early rows (0..30) do not artificially peg at the 12.0 crisis ceiling due to rank deficiency."""
    from bubble_detector.models.regime_mahalanobis import MacroMahalanobisDetector

    detector = MacroMahalanobisDetector()
    np.random.seed(42)
    # Generate 100 observations across 15 features
    Z = np.random.randn(100, 15).astype(np.float32)
    m_dist = detector.compute_mahalanobis_distance(Z)

    # In early rows, distance must be well-conditioned and strictly below the 12.0 clipping ceiling
    early_max = float(np.max(m_dist[:35]))
    assert early_max < 10.0, f"Early Mahalanobis distance spiked to {early_max}, indicating rank-deficient singularity"
    assert not np.isnan(m_dist).any(), "Early Mahalanobis distances contain NaNs"
    assert (m_dist >= 0.0).all(), "Mahalanobis distances contain negative values"



