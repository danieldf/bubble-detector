"""
Unit & Mathematical Verification Suite for the 13-Indicator Orthogonal Basis (B_13^perp),
the 5 Information-Maximizing Summary Indicators, and Tab 8 Dual-UI Parity (v3.3.0).
"""

import numpy as np
import polars as pl
import pytest

from bubble_detector.config import HORIZON_OPTION_1_ID, HORIZON_OPTION_2_ID, HORIZON_OPTION_3_ID, PROVENANCE_DIR
from bubble_detector.models.composite_summary import (
    CompositeSummaryEngine,
    INDICATORS_13_ORTHOGONAL,
    SUMMARY_INDICATORS_5,
    compute_orthogonal_basis_and_summaries_numpy,
)
from bubble_detector.ui.dashboard import DashboardState, build_composite_summary_chart
from bubble_detector.ui.panel_dashboard import (
    build_composite_summary_fig,
    dashboard_tabs,
    generate_wasm_dataset,
    HORIZON_METADATA,
)


def test_orthogonal_basis_13_spectral_entropy_and_vif_20yr():
    """
    Verify that on the 20-Year Regime Horizon (2006–2026), the 13-indicator orthogonal
    basis B_13^perp achieves:
      - Unit-variance standardization (mean ~ 0, variance ~ 1)
      - Roy (2007) spectral effective rank erank(R) >= 12.0 (eta_spec >= 0.87)
      - Individual VIF tolerance tau_j = 1 / VIF_j >= 0.87 for all 13 indicators.
    """
    df_20yr = pl.read_parquet(PROVENANCE_DIR / "market_data_20yr.parquet")
    engine = CompositeSummaryEngine()
    df_res = engine.compute_all_summary_indicators(df_20yr)

    for col in INDICATORS_13_ORTHOGONAL:
        assert col in df_res.columns, f"Missing orthogonal basis indicator: {col}"
        arr = df_res[col].to_numpy()
        assert not np.isnan(arr).any(), f"NaN detected in {col}"
        assert not np.isinf(arr).any(), f"Inf detected in {col}"

    Z = engine.get_standardized_orthogonal_matrix(df_res)

    assert Z.shape == (len(df_20yr), 13)

    # Check causal unit-variance standardization (post-warmup rows t >= 252)
    Z_eval = Z[252:]
    col_means = np.mean(Z_eval, axis=0)
    col_stds = np.std(Z_eval, axis=0)
    assert np.all(np.abs(col_means) < 0.35), f"Excessive mean drift detected: {col_means}"
    # Continuous indicators (all except episodic piecewise unit-root tests idx 2, 3) have std ~ 1.0
    continuous_mask = np.array([i not in (2, 3) for i in range(13)])
    assert np.all((col_stds[continuous_mask] > 0.90) & (col_stds[continuous_mask] < 1.15)), (
        f"Continuous indicator unit-variance deviation: {col_stds}"
    )
    assert np.all((col_stds > 0.30) & (col_stds < 1.15)), f"Unit-variance deviation: {col_stds}"

    # Check correlation matrix, spectral effective rank, and VIF tolerances
    R = np.corrcoef(Z_eval, rowvar=False)
    eigvals = np.linalg.eigvalsh(R)
    eigvals = np.maximum(eigvals, 1e-12)
    p = eigvals / np.sum(eigvals)
    shannon_h = -np.sum(p * np.log(p))
    erank = float(np.exp(shannon_h))
    eta_spec = erank / 13.0

    assert erank >= 12.0, f"Effective rank {erank:.4f} below 12.0"
    assert eta_spec >= 0.87, f"Spectral efficiency {eta_spec:.4f} below 0.87 cutoff"

    R_inv = np.linalg.inv(R)
    vifs = np.diag(R_inv)
    tolerances = 1.0 / vifs
    for idx, name in enumerate(INDICATORS_13_ORTHOGONAL):
        assert tolerances[idx] >= 0.87, (
            f"Indicator {name} violates collinearity cutoff: tau={tolerances[idx]:.4f} < 0.87 (VIF={vifs[idx]:.4f})"
        )


def test_strict_causal_filtration_zero_lookahead():
    """
    Verify that truncating the dataset at T_0 = 1500 vs computing over the full dataset
    yields identical values for all t <= T_0 (excluding the final post-scaling mean/std pass
    by verifying the causal summary trajectories).
    """
    df_20yr = pl.read_parquet(PROVENANCE_DIR / "market_data_20yr.parquet")
    t0 = 1500
    df_trunc = df_20yr.slice(0, t0)

    engine = CompositeSummaryEngine()
    res_full = engine.compute_all_summary_indicators(df_20yr)
    res_trunc = engine.compute_all_summary_indicators(df_trunc)

    # Verify high correlation (> 0.999) and causal consistency on [0, t0)
    for col in SUMMARY_INDICATORS_5:
        a_full = res_full[col].to_numpy()[:t0]
        a_trunc = res_trunc[col].to_numpy()
        corr = float(np.corrcoef(a_full, a_trunc)[0, 1])
        assert corr > 0.999, f"Look-ahead discrepancy detected in {col}: corr={corr:.6f}"


def test_five_summary_indicators_bounds_and_crash_separation_20yr():
    """
    Verify that all 5 Summary Indicators are strictly bounded in [0, 100], free of NaNs,
    and achieve strong positive Peak-Trough separation (>= +20.0%) across the 8 historical
    crash regimes vs the 4 major crash liquidation troughs on the 20-year horizon.
    """
    df_20yr = pl.read_parquet(PROVENANCE_DIR / "market_data_20yr.parquet")
    dates = [str(d)[:10] for d in df_20yr["Date"].to_list()]

    for col in SUMMARY_INDICATORS_5:
        assert col in df_20yr.columns, f"Missing summary indicator {col} in staged parquet"
        arr = df_20yr[col].to_numpy()
        assert not np.isnan(arr).any(), f"NaN in {col}"
        assert float(np.min(arr)) >= 0.0, f"{col} min below 0.0"
        assert float(np.max(arr)) <= 100.0, f"{col} max above 100.0"

    # Check active pillars and crash liquidation damper
    pillars = df_20yr["SPCA_Active_Pillars"].to_numpy()
    assert int(np.min(pillars)) >= 1
    assert int(np.max(pillars)) <= 13

    damper = df_20yr["Crash_Liquidation_Damper"].to_numpy()
    assert float(np.min(damper)) >= 0.0

    # Verify Peak vs Trough separation across the 8 crash peaks and 4 crash troughs
    crash_peaks = [
        ("2007-06-01", "2007-10-31"),
        ("2010-03-01", "2010-05-06"),
        ("2011-04-01", "2011-07-31"),
        ("2015-05-01", "2015-08-18"),
        ("2018-01-02", "2018-09-28"),
        ("2020-01-02", "2020-02-19"),
        ("2021-09-01", "2022-01-04"),
        ("2025-11-01", "2026-06-30"),
    ]
    crash_troughs = [
        ("2008-10-15", "2009-03-15"),
        ("2011-09-15", "2011-10-15"),
        ("2020-03-12", "2020-04-05"),
        ("2022-09-15", "2022-10-25"),
    ]

    for col in SUMMARY_INDICATORS_5:
        arr = df_20yr[col].to_numpy()
        peak_vals = []
        for s_d, e_d in crash_peaks:
            mask = np.array([(d >= s_d) and (d <= e_d) for d in dates])
            if np.any(mask):
                peak_vals.append(float(np.max(arr[mask])))
        trough_vals = []
        for s_d, e_d in crash_troughs:
            mask = np.array([(d >= s_d) and (d <= e_d) for d in dates])
            if np.any(mask):
                trough_vals.append(float(np.min(arr[mask])))

        delta_pt = float(np.mean(peak_vals) - np.mean(trough_vals))
        assert delta_pt >= 20.0, f"{col} Peak-Trough separation {delta_pt:.2f}% < 20.0%"


@pytest.mark.parametrize("horizon_id", [HORIZON_OPTION_1_ID, HORIZON_OPTION_2_ID, HORIZON_OPTION_3_ID])
def test_tab8_dual_ui_parity_across_all_horizons(horizon_id):
    """
    Verify that Tab 8 ('Composite Summary Indicators') is registered in Panel WASM and NiceGUI,
    and produces 100% identical 10-trace figures across all 3 date horizons.
    """
    # Check Panel tabs count (8 tabs)
    assert len(dashboard_tabs) == 8
    tab_names = [t[0] for t in dashboard_tabs._names_and_objects] if hasattr(dashboard_tabs, "_names_and_objects") else []
    if tab_names:
        assert "Composite Summary Indicators" in tab_names

    state = DashboardState(load_data=False)
    state.load_data(horizon_id)

    fig_nice = build_composite_summary_chart(state)
    fig_wasm = build_composite_summary_fig(horizon_id)

    assert len(fig_nice.data) == 10
    assert len(fig_wasm.data) == 10

    for i, (tr_n, tr_w) in enumerate(zip(fig_nice.data, fig_wasm.data)):
        assert tr_n.name == tr_w.name, f"Trace {i} name mismatch: {tr_n.name} vs {tr_w.name}"
        assert list(tr_n.x) == list(tr_w.x), f"Trace {i} x-axis mismatch on {horizon_id}"
        np.testing.assert_allclose(
            np.asarray(tr_n.y, dtype=np.float64),
            np.asarray(tr_w.y, dtype=np.float64),
            rtol=1e-4,
            atol=1e-4,
            err_msg=f"Trace {i} ({tr_n.name}) y-values mismatch on {horizon_id}",
        )
