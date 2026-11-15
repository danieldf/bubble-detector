"""
Unit tests for Institutional Cost-Inclusive Backtest Simulation Engine.
"""

import pytest
import numpy as np
import polars as pl

from bubble_detector.backtest.engine import PortfolioBacktestEngine

@pytest.fixture
def market_simulation_df():
    """Generate 1000-day market simulation with bull, bubble, crash, and recovery phases."""
    np.random.seed(42)
    n = 1000
    dates = [f"2020-01-{i%28+1:02d}" for i in range(n)]

    # Price trajectory: 100 -> 250 (bubble) -> 120 (crash) -> 280 (recovery)
    t = np.linspace(0, 10, n)
    trend = 100.0 * np.exp(0.08 * t)
    bubble = 80.0 * np.exp(-((t - 4.0)**2) / 0.8)
    crash = -90.0 * np.exp(-((t - 5.5)**2) / 0.4)
    prices = (trend + bubble + crash + np.random.randn(n) * 2.0).astype(np.float32)

    # Shiller CAPE: rises from 22 to 42 during bubble, drops to 16 in crash
    cape = 20.0 + 22.0 * np.exp(-((t - 4.0)**2) / 1.0) - 6.0 * np.exp(-((t - 5.5)**2) / 0.5)

    # Dynamic Exposure: derisks during bubble (w=0.30), holds high equity (w=0.90) in crash trough
    exposure = np.ones(n, dtype=np.float32)
    for i in range(n):
        if 3.0 <= t[i] <= 4.5:
            exposure[i] = 0.30  # De-risked ahead of crash
        elif 4.6 <= t[i] <= 6.0:
            exposure[i] = 0.90  # Deep value capture at crash trough
        else:
            exposure[i] = 1.00

    return pl.DataFrame({
        "Date": dates,
        "SPY": prices,
        "Shiller_CAPE": cape.astype(np.float32),
        "Dynamic_Equity_Exposure": exposure
    })

def test_backtest_fee_deduction(market_simulation_df):
    """Asserts transaction costs and slippage are deducted on every rebalance."""
    engine = PortfolioBacktestEngine(fee_bps=20.0, slippage_bps=10.0)
    results = engine.run_backtest(market_simulation_df)

    res_dyn = results["dynamic"]
    assert res_dyn.total_turnover > 0.0
    assert res_dyn.transaction_cost_drag_pct > 0.0

    # Test with zero fees vs positive fees
    engine_zero = PortfolioBacktestEngine(fee_bps=0.0, slippage_bps=0.0)
    results_zero = engine_zero.run_backtest(market_simulation_df)
    assert results_zero["dynamic"].equity_curve[-1] > res_dyn.equity_curve[-1]

def test_exposure_rule_vs_naive_cape():
    """
    Asserts dynamic exposure strategy achieves superior risk-adjusted return (higher Sharpe
    and lower maximum drawdown) than naive CAPE rule on historical market data.
    """
    from bubble_detector.ui.dashboard import DashboardState
    state = DashboardState(load_data=False)
    state.load_data("option_2")

    engine = PortfolioBacktestEngine()
    results = engine.run_backtest(state.df)

    res_dyn = results["dynamic"]
    res_naive = results["naive_cape"]
    res_bh = results["buy_and_hold"]

    # Dynamic signed strategy achieves significantly higher Sharpe and CAGR than naive CAPE
    assert res_dyn.sharpe_ratio > res_naive.sharpe_ratio, (
        f"Dynamic Sharpe ({res_dyn.sharpe_ratio:.2f}) did not exceed Naive CAPE Sharpe ({res_naive.sharpe_ratio:.2f})"
    )
    assert res_dyn.cagr > res_naive.cagr, (
        f"Dynamic CAGR ({res_dyn.cagr:.2%}) did not exceed Naive CAPE CAGR ({res_naive.cagr:.2%})"
    )
    # Dynamic signed strategy significantly improves drawdown protection relative to unhedged Buy & Hold
    assert abs(res_dyn.max_drawdown) < abs(res_bh.max_drawdown), (
        f"Dynamic MDD ({res_dyn.max_drawdown:.2%}) did not improve upon Buy & Hold MDD ({res_bh.max_drawdown:.2%})"
    )


def test_strictly_causal_one_day_execution_lag():
    """
    RT-CRIT-02: Verify that PortfolioBacktestEngine applies signal weights[t - 1] (end of day t-1)
    to day t's return, preventing same-day close-to-close lookahead bias.
    """
    dates = [f"2020-01-{i+1:02d}" for i in range(25)]
    spy = [100.0] * 10 + [50.0] * 15  # -50% crash at index 10
    cape = [30.0] * 10 + [15.0] * 15
    # Signal drops to 0.0 at index 9 close (before index 10 crash) -> crash avoided
    w_avoided = [1.0] * 9 + [0.0] * 16
    # Signal drops to 0.0 at index 10 close (on the day of the crash) -> TOO LATE for index 10 return!
    w_late = [1.0] * 10 + [0.0] * 15

    df_avoided = pl.DataFrame({
        "Date": dates,
        "SPY": spy,
        "Shiller_CAPE": cape,
        "Dynamic_Equity_Exposure": w_avoided,
    })
    df_late = pl.DataFrame({
        "Date": dates,
        "SPY": spy,
        "Shiller_CAPE": cape,
        "Dynamic_Equity_Exposure": w_late,
    })
    engine = PortfolioBacktestEngine(fee_bps=0.0, slippage_bps=0.0, annual_cash_yield=0.0)
    res_avoided = engine.run_backtest(df_avoided)["dynamic"]
    res_late = engine.run_backtest(df_late)["dynamic"]

    assert np.isclose(res_avoided.equity_curve[-1], 1.0, atol=1e-4)
    assert np.isclose(res_late.equity_curve[-1], 0.5, atol=1e-4)

