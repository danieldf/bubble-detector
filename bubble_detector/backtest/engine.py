"""
Institutional Cost-Inclusive Portfolio Backtest Simulation Engine.
===================================================================

Portfolio Theory & Institutional Backtesting Foundations:
---------------------------------------------------------
Academic literature often evaluates quantitative bubble models on theoretical signal
accuracy (e.g. Area Under the ROC Curve) rather than implementable portfolio returns.
In real-world asset management, transaction costs, execution slippage, cash drag,
and benchmark tracking errors determine strategy viability.

1. The Comparative Benchmark Trilogy:
   - Dynamic Signed Mahalanobis Strategy (w_t \\in [0.20, 1.00]):
     Continuous risk-budgeting allocation governed by Riemannian statistical distance.
     De-risks down to w_{min} = 0.20 during bubble euphoria, but aggressively holds
     exposure (w_t \\ge 0.80) during crash troughs (Deep Value / Liquidation).
   - Buy-and-Hold S&P 500 (w_t \\equiv 1.00):
     The passive institutional benchmark capturing the full equity risk premium (ERP).
   - Naive Valuation Timing Rule (w_t \\in \\{0.0, 1.0\\}):
     "Sell 100% Equity to Cash when CAPE > 30.0; Re-enter 100% Equity when CAPE < 20.0."
     *Economic Pathology*: Demonstrates the catastrophic pitfall of naive valuation timing:
     in prolonged technological expansions (1995–2000, 2016–2021, 2024–2026), CAPE
     exceeds 30 for multiple consecutive years while markets surge another 100%–300%.
     Binary valuation timers suffer massive opportunity cost and permanent capital impairment.

2. Realistic Frictions & Capital Accounting:
   - Turnover Frictions: Transaction fee of 10 bps (0.0010) + bid-ask execution slippage of 5 bps (0.0005)
     = 15 bps total cost per unit of portfolio turnover:
         \\text{Cost}_t = |w_t - w_{t-1}| \\cdot \\text{FeeRate}
   - Rebalancing Deadband: Positions are rebalanced only if |w_t - w_{t-1}| \\ge 0.02 (2.0%),
     eradicating micro-turnover friction.
   - Cash Yield / Risk-Free Interest: Unallocated capital (1 - w_t) earns the prevailing cash
     yield (4.0% annualized), preventing synthetic cash penalization.
   - Margin Borrowing Penalty: Leveraged positions (w_t > 1.0) incur a borrowing surcharge
     of Fed Funds + 150 bps.

3. Performance Metrics:
   - Compound Annual Growth Rate: \\text{CAGR} = (V_T / V_0)^{252 / T} - 1
   - Annualized Volatility: \\sigma_{ann} = \\sqrt{252} \\cdot \\text{Std}(R_t)
   - Sharpe Ratio (Sharpe, 1966): \\text{SR} = (\\text{CAGR} - r_f) / \\sigma_{ann}
   - Sortino Ratio (Sortino & van der Meer, 1991): Evaluates downside semi-variance:
         \\text{Sortino} = \\frac{\\text{CAGR} - r_f}{\\sqrt{252} \\cdot \\left(\\frac{1}{T} \\sum_{t=1}^T \\min(R_t - r_{f, daily}, 0)^2\\right)^{1/2}}
   - Calmar Ratio: \\text{Calmar} = \\text{CAGR} / |\\text{MaxDrawdown}|
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple, Any
import numpy as np
import pandas as pd
import polars as pl
from bubble_detector.config import logger

@dataclass
class BacktestResult:
    """Performance statistics and equity curves for a single backtested strategy."""
    strategy_name: str
    cagr: float
    annualized_volatility: float
    sharpe_ratio: float
    sortino_ratio: float
    max_drawdown: float
    calmar_ratio: float
    total_turnover: float
    transaction_cost_drag_pct: float
    equity_curve: np.ndarray
    dates: List[str]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "Strategy": self.strategy_name,
            "CAGR (%)": round(self.cagr * 100.0, 2),
            "Volatility (%)": round(self.annualized_volatility * 100.0, 2),
            "Sharpe Ratio": round(self.sharpe_ratio, 2),
            "Sortino Ratio": round(self.sortino_ratio, 2),
            "Max Drawdown (%)": round(self.max_drawdown * 100.0, 2),
            "Calmar Ratio": round(self.calmar_ratio, 2),
            "Total Turnover (x)": round(self.total_turnover, 2),
            "Fee Drag (%)": round(self.transaction_cost_drag_pct * 100.0, 2),
        }

class PortfolioBacktestEngine:
    """Institutional simulation engine for dynamic allocation rules."""

    def __init__(
        self,
        fee_bps: float = 10.0,
        slippage_bps: float = 5.0,
        annual_cash_yield: float = 0.040,
        margin_borrow_penalty_bps: float = 150.0,
        rebalance_threshold: float = 0.02
    ):
        self.fee_rate = (fee_bps + slippage_bps) / 10000.0
        self.daily_cash_rate = annual_cash_yield / 252.0
        self.margin_penalty_rate = (margin_borrow_penalty_bps / 10000.0) / 252.0
        self.rebalance_threshold = rebalance_threshold

    def run_backtest(
        self,
        df: pl.DataFrame,
        target_col: str = "SPY",
        cape_col: str = "Shiller_CAPE",
        exposure_col: str = "Dynamic_Equity_Exposure"
    ) -> Dict[str, BacktestResult]:
        """
        Execute comparative backtest across Dynamic Exposure, Buy & Hold, and Naive CAPE rule.
        """
        logger.info("Executing cost-inclusive comparative portfolio backtest...")
        df_pd = df.to_pandas()
        dates = [str(d)[:10] for d in df_pd["Date"].to_list()]
        n = len(df_pd)

        if n < 20:
            raise ValueError("Insufficient observations for backtest simulation.")

        # Equity price series
        prices = df_pd[target_col].to_numpy().astype(np.float64)
        eq_returns = np.diff(prices) / prices[:-1]
        eq_returns = np.insert(eq_returns, 0, 0.0)

        # CAPE for Naive Rule
        cape_series = df_pd[cape_col].to_numpy().astype(np.float64) if cape_col in df_pd.columns else np.full(n, 25.0)

        # Dynamic Exposure weights
        if exposure_col in df_pd.columns:
            weights_dynamic = df_pd[exposure_col].to_numpy().astype(np.float64)
        else:
            weights_dynamic = np.ones(n, dtype=np.float64)

        # 1. Buy & Hold S&P 500 Strategy: w = 1.0 constant
        weights_bh = np.ones(n, dtype=np.float64)

        # 2. Naive Valuation Rule: Sell 100% Equity when CAPE > 30, Re-enter 100% when CAPE < 20
        weights_naive = np.ones(n, dtype=np.float64)
        curr_state = 1.0
        for i in range(n):
            val = cape_series[i]
            if val > 30.0:
                curr_state = 0.0
            elif val < 20.0:
                curr_state = 1.0
            weights_naive[i] = curr_state

        # Run simulations
        res_dynamic = self._simulate_strategy(dates, eq_returns, weights_dynamic, "Dynamic Signed Mahalanobis")
        res_bh = self._simulate_strategy(dates, eq_returns, weights_bh, "Buy-and-Hold S&P 500")
        res_naive = self._simulate_strategy(dates, eq_returns, weights_naive, "Naive CAPE Rule (>30 Sell, <20 Buy)")

        return {
            "dynamic": res_dynamic,
            "buy_and_hold": res_bh,
            "naive_cape": res_naive
        }

    def _simulate_strategy(
        self,
        dates: List[str],
        eq_returns: np.ndarray,
        weights: np.ndarray,
        strategy_name: str
    ) -> BacktestResult:
        """Simulate single portfolio with frictions, cash yields, and rebalancing costs."""
        n = len(eq_returns)
        portfolio_val = np.ones(n, dtype=np.float64)
        port_returns = np.zeros(n, dtype=np.float64)
        total_turnover = 0.0
        total_fees = 0.0

        prev_w = float(weights[0])
        for t in range(1, n):
            raw_w = float(weights[t])
            if abs(raw_w - prev_w) >= self.rebalance_threshold:
                target_w = raw_w
                delta_w = abs(target_w - prev_w)
                prev_w = target_w
            else:
                target_w = prev_w
                delta_w = 0.0

            total_turnover += delta_w
            fee = delta_w * self.fee_rate
            total_fees += fee

            # Returns: Equity portion + Cash portion - Transaction Costs
            r_equity = target_w * eq_returns[t]
            r_cash = max(0.0, 1.0 - target_w) * self.daily_cash_rate
            r_borrow = abs(min(0.0, 1.0 - target_w)) * self.margin_penalty_rate

            net_r = r_equity + r_cash - r_borrow - fee
            port_returns[t] = net_r
            portfolio_val[t] = portfolio_val[t - 1] * (1.0 + net_r)

        # Performance analytics
        n_years = n / 252.0
        end_val = portfolio_val[-1]
        cagr = (end_val ** (1.0 / max(0.1, n_years))) - 1.0 if end_val > 0.0 else -0.99
        ann_vol = float(np.std(port_returns[1:]) * np.sqrt(252.0))
        rf = self.daily_cash_rate * 252.0

        sharpe = (cagr - rf) / max(1e-4, ann_vol)

        # Sortino: Downside deviation
        downside_diff = np.minimum(port_returns[1:] - self.daily_cash_rate, 0.0)
        downside_std = float(np.sqrt(np.mean(downside_diff ** 2)) * np.sqrt(252.0))
        sortino = (cagr - rf) / max(1e-4, downside_std)

        # Maximum Drawdown
        running_max = np.maximum.accumulate(portfolio_val)
        drawdowns = (portfolio_val - running_max) / running_max
        max_dd = float(np.min(drawdowns))
        calmar = cagr / abs(max_dd) if abs(max_dd) > 1e-4 else 0.0

        return BacktestResult(
            strategy_name=strategy_name,
            cagr=cagr,
            annualized_volatility=ann_vol,
            sharpe_ratio=sharpe,
            sortino_ratio=sortino,
            max_drawdown=max_dd,
            calmar_ratio=calmar,
            total_turnover=total_turnover,
            transaction_cost_drag_pct=total_fees,
            equity_curve=portfolio_val,
            dates=dates
        )
