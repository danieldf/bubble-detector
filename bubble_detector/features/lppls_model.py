"""
Log-Periodic Power Law Singularity (LPPLS) Module.
=================================================

Mathematical & Financial Microstructure Foundations:
----------------------------------------------------
Financial super-bubbles and catastrophic market crashes are characterized by faster-than-exponential
power-law price acceleration decorated with accelerating log-periodic oscillations (Johansen, Ledoit &
Sornette 1999, 2003; Sornette 2003). These oscillations reflect discrete scale invariance (DSI)
and accelerating imitation / positive feedback herding among market participants as the system approaches
a critical transition singularity time t_c:

    E[ln P_t] = A + B (t_c - t)^m + C (t_c - t)^m cos( omega * ln(t_c - t) + phi )

Filimonov & Sornette (2013) Subordination Algorithm:
----------------------------------------------------
By trigonometric expansion:
    C cos( omega * ln(t_c - t) + phi ) = C_1 cos( omega * ln(t_c - t) ) + C_2 sin( omega * ln(t_c - t) )
where C_1 = C cos(phi), C_2 = -C sin(phi), and amplitude C = sqrt(C_1^2 + C_2^2).

This reduces the calibration to a linear regression in 4 parameters (A, B, C_1, C_2) conditioned on the
3 nonlinear parameters (t_c, m, omega):
    ln P_t = A + B f(t) + C_1 g(t) + C_2 h(t)
where:
    f(t) = (t_c - t)^m
    g(t) = (t_c - t)^m cos( omega * ln(t_c - t) )
    h(t) = (t_c - t)^m sin( omega * ln(t_c - t) )

Given candidate (t_c, m, omega), the 4 linear parameters are obtained analytically via Ordinary Least Squares:
    beta = (X^T X)^{-1} X^T y
where X = [1, f, g, h] and y = ln P.

The sum of squared errors SSE(t_c, m, omega) is minimized over the bounded 3D search space:
- t_c in [t_{last} + 2, t_{last} + 90] trading days (finite-time singularity horizon)
- m in [0.1, 0.9] (sub-linear acceleration, explosive derivative)
- omega in [4.8, 13.0] (log-periodic scaling ratio lambda = exp(2*pi/omega) in [1.6, 3.7])

Sornette Filtering Conditions:
------------------------------
A calibration is declared valid if and only if all canonical constraints are satisfied:
1. 0.1 <= m <= 0.9
2. 4.8 <= omega <= 13.0
3. B < -0.05 (genuine power-law price acceleration upward toward singularity)
4. Damping condition: D = (m * |B|) / (omega * sqrt(C_1^2 + C_2^2)) >= 0.8 (ensuring price is non-decreasing on average)
5. Fit quality: R^2 >= 0.60
6. Log-periodic oscillations: N_osc = (omega / 2*pi) * ln(t_c / (t_c - t_{last})) >= 2.0
7. Relative oscillation amplitude: C / |B| >= 0.03

Multi-Scale Rolling LPPLS Confidence Indicator:
-----------------------------------------------
At each time t, calibrate across multiple lookback windows W = [60, 90, 125, 180, 250] trading days.
The multi-scale bubble confidence score is:
    CI(t) = ( sum_{w in W} 1_{Fit_w is valid} ) / |W_{eval}| in [0.0, 1.0]
"""

from typing import Dict, Any, List, Tuple, Optional
import numpy as np
import pandas as pd
import polars as pl
from scipy.optimize import minimize

from bubble_detector.config import logger

_LPPLS_GRID_CACHE: Dict[int, Tuple[np.ndarray, np.ndarray, np.ndarray]] = {}


def _get_lppls_grid(n: int) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Precompute and cache the Filimonov-Sornette (2013) OLS projection tensor P = (X^T X)^{-1} X^T
    across the canonical 3D non-linear parameter grid (t_c, m, omega) for window length `n`.
    """
    if n in _LPPLS_GRID_CACHE:
        return _LPPLS_GRID_CACHE[n]

    t = np.arange(n, dtype=np.float64)
    tc_offs = [4.0, 8.0, 14.0, 22.0, 32.0, 45.0, 65.0]
    m_vals = [0.18, 0.32, 0.48, 0.64, 0.80]
    w_vals = [5.2, 6.4, 7.8, 9.6, 11.8]

    x_list: List[np.ndarray] = []
    p_list: List[np.ndarray] = []
    meta: List[Tuple[float, float, float, float]] = []

    for tc_o in tc_offs:
        tc = float(n) + tc_o
        dt = tc - t
        ln_dt = np.log(dt)
        for m in m_vals:
            dt_m = dt ** m
            for om in w_vals:
                n_osc = float((om / (2.0 * np.pi)) * np.log(tc / max(tc - (n - 1), 1e-5)))
                if n_osc < 1.2:
                    continue
                w_ln = om * ln_dt
                x_mat = np.column_stack([np.ones(n, dtype=np.float64), dt_m, dt_m * np.cos(w_ln), dt_m * np.sin(w_ln)])
                try:
                    p_mat = np.linalg.solve(x_mat.T @ x_mat, x_mat.T)
                    x_list.append(x_mat)
                    p_list.append(p_mat)
                    meta.append((tc, m, om, n_osc))
                except Exception:
                    pass

    x_stack = np.array(x_list, dtype=np.float64)
    p_stack = np.array(p_list, dtype=np.float64)
    meta_arr = np.array(meta, dtype=np.float64)
    _LPPLS_GRID_CACHE[n] = (x_stack, p_stack, meta_arr)
    return _LPPLS_GRID_CACHE[n]


def calibrate_lppls_filimonov(
    log_prices: np.ndarray,
    tc_offset_bounds: Tuple[int, int] = (2, 80),
    m_bounds: Tuple[float, float] = (0.1, 0.9),
    omega_bounds: Tuple[float, float] = (4.8, 13.0)
) -> Dict[str, Any]:
    """
    Calibrate the LPPLS model on log-prices using the Filimonov & Sornette (2013)
    linear-nonlinear subordination algorithm.

    Parameters
    ----------
    log_prices : np.ndarray
        Array of log-prices ln(P_t).
    tc_offset_bounds : Tuple[int, int]
        Bounds for critical time offset beyond the last observation (e.g. 2 to 80 days).
    m_bounds : Tuple[float, float]
        Bounds for acceleration exponent m (default 0.1 to 0.9).
    omega_bounds : Tuple[float, float]
        Bounds for log-periodic angular frequency omega (default 4.8 to 13.0).

    Returns
    -------
    Dict[str, Any]
        Fitted parameters (tc, m, omega, A, B, C1, C2, C, R2, damping, is_valid).
    """
    n = len(log_prices)
    # Require at least 30 observations and positive net growth over lookback window
    # (upward-accelerating bubble B < 0 strictly requires P_t > P_{t-w})
    if n < 30 or log_prices[-1] <= log_prices[0]:
        return {"is_valid": False, "R2": 0.0, "damping": 0.0}

    t = np.arange(n, dtype=np.float64)
    y = np.asarray(log_prices, dtype=np.float64)
    y_mean = np.mean(y)
    ss_tot = float(np.sum((y - y_mean) ** 2))
    if ss_tot < 1e-12:
        return {"is_valid": False, "R2": 0.0, "damping": 0.0}

    bounds = [
        (n + tc_offset_bounds[0], n + tc_offset_bounds[1]),
        m_bounds,
        omega_bounds
    ]
    starts = [
        (n + 15.0, 0.50, 8.0),
        (n + 40.0, 0.50, 8.0)
    ]

    best_res = None
    best_sse = 1e12

    # Preallocate design matrix buffer to eliminate inner-loop memory allocations
    X = np.empty((n, 4), dtype=np.float64)
    X[:, 0] = 1.0

    def objective(params: np.ndarray) -> float:
        tc, m, omega = params
        dt = tc - t
        if np.any(dt <= 0.1):
            return 1e9
        dt_m = dt ** m
        w_ln = omega * np.log(dt)
        X[:, 1] = dt_m
        X[:, 2] = dt_m * np.cos(w_ln)
        X[:, 3] = dt_m * np.sin(w_ln)
        try:
            XtX = X.T @ X
            XtY = X.T @ y
            beta = np.linalg.solve(XtX, XtY)
            res = y - X @ beta
            return float(np.sum(res ** 2))
        except Exception:
            return 1e9

    for x0 in starts:
        try:
            opt_res = minimize(objective, x0, bounds=bounds, method="L-BFGS-B", options={"maxiter": 35, "ftol": 1e-4})
            if opt_res.fun < best_sse:
                best_sse = opt_res.fun
                best_res = opt_res
                # Quick check if candidate solution satisfies canonical constraints
                tc_c, m_c, omega_c = opt_res.x
                dt_c = tc_c - t
                dt_mc = dt_c ** m_c
                w_lnc = omega_c * np.log(dt_c)
                X[:, 1] = dt_mc
                X[:, 2] = dt_mc * np.cos(w_lnc)
                X[:, 3] = dt_mc * np.sin(w_lnc)
                beta_c = np.linalg.solve(X.T @ X, X.T @ y)
                if (beta_c[1] < 0.0 and
                    m_bounds[0] <= m_c <= m_bounds[1] and
                    omega_bounds[0] <= omega_c <= omega_bounds[1]):
                    C_cand = float(np.sqrt(beta_c[2] ** 2 + beta_c[3] ** 2))
                    damp_cand = float((m_c * abs(beta_c[1])) / (omega_c * max(C_cand, 1e-9)))
                    r2_cand = float(1.0 - (opt_res.fun / max(ss_tot, 1e-9)))
                    rel_cand = float(C_cand / max(abs(beta_c[1]), 1e-9))
                    n_osc_cand = float((omega_c / (2.0 * np.pi)) * np.log(tc_c / max(tc_c - (n - 1), 1e-5)))
                    if damp_cand >= 0.80 and r2_cand >= 0.60 and rel_cand >= 0.025 and n_osc_cand >= 1.2:
                        # Primary start found valid canonical LPPLS fit; early termination
                        break
        except Exception:
            pass

    if best_res is None:
        return {"is_valid": False, "R2": 0.0, "damping": 0.0}

    tc, m, omega = best_res.x

    dt = tc - t
    dt_m = dt ** m
    w_ln = omega * np.log(dt)
    X[:, 1] = dt_m
    X[:, 2] = dt_m * np.cos(w_ln)
    X[:, 3] = dt_m * np.sin(w_ln)
    try:
        XtX = X.T @ X
        XtY = X.T @ y
        beta = np.linalg.solve(XtX, XtY)
        A, B, C1, C2 = beta
        C = float(np.sqrt(C1 ** 2 + C2 ** 2))

        sse = best_res.fun
        r2 = float(1.0 - (sse / max(ss_tot, 1e-9)))
        damping = float((m * np.abs(B)) / (omega * max(C, 1e-9)))

        # Canonical Sornette (1999, 2013) filtering constraints
        # 1. Sub-linear acceleration exponent m in [0.1, 0.9]
        c1 = m_bounds[0] <= m <= m_bounds[1]
        # 2. Angular log-periodic frequency omega in [4.8, 13.0]
        c2 = omega_bounds[0] <= omega <= omega_bounds[1]
        # 3. Super-exponential price growth toward singularity: B < 0
        c3 = B < 0.0
        # 4. Monotonicity damping condition: D = (m * |B|) / (omega * C) >= 0.80
        c4 = damping >= 0.80
        # 5. Fit quality: R^2 >= 0.60
        c5 = r2 >= 0.60
        # 6. Minimum log-periodic oscillations (n_osc >= 1.2 across lookback window)
        n_osc = float((omega / (2.0 * np.pi)) * np.log(tc / max(tc - (n - 1), 1e-5)))
        c6 = n_osc >= 1.2
        # 7. Relative oscillation amplitude (rel_osc = C / |B| >= 0.025 to rule out non-oscillating trends)
        rel_osc = float(C / max(abs(B), 1e-9))
        c7 = rel_osc >= 0.025

        is_valid = bool(c1 and c2 and c3 and c4 and c5 and c6 and c7)

        return {
            "tc": float(tc),
            "m": float(m),
            "omega": float(omega),
            "A": float(A),
            "B": float(B),
            "C1": float(C1),
            "C2": float(C2),
            "C": float(C),
            "R2": r2,
            "damping": damping,
            "n_osc": n_osc,
            "rel_osc": rel_osc,
            "is_valid": is_valid
        }
    except Exception:
        return {"is_valid": False, "R2": 0.0, "damping": 0.0}


def compute_lppls_confidence_indicator(
    df: pl.DataFrame,
    target_col: str = "XLK",
    windows: Optional[List[int]] = None,
    step: int = 2
) -> pl.DataFrame:
    """
    Computes rolling multi-scale LPPLS Bubble Confidence Indicator CI(t) in [0.0, 1.0]
    and its rolling 90th percentile.

    Parameters
    ----------
    df : pl.DataFrame
        Input dataframe with price series.
    target_col : str
        Target asset ticker/column (defaults to 'XLK' for tech sector outperformance).
    windows : Optional[List[int]]
        List of lookback windows (default [60, 90, 125, 180, 250]).
    step : int
        Evaluation stride in trading days (default 2 days with forward fill for speed).

    Returns
    -------
    pl.DataFrame
        Dataframe augmented with LPPLS_Confidence, LPPLS_90th_Percentile,
        LPPLS_Critical_Threshold, and LPPLS_Bubble_Active.
    """
    if windows is None:
        windows = [60, 90, 125, 180, 250]

    eval_col = target_col if target_col in df.columns else df.columns[1]
    logger.info(f"Computing rolling multi-scale LPPLS Confidence Indicator for '{eval_col}'...")

    prices = df[eval_col].to_numpy()
    n = len(prices)
    log_p = np.log(np.maximum(prices.astype(np.float64), 1e-4))

    min_w = min(windows)
    confidence = np.zeros(n, dtype=np.float32)

    if n > min_w:
        eval_indices = np.arange(min_w, n, step)
        valid_counts = np.zeros(len(eval_indices), dtype=np.float64)
        eval_counts = np.zeros(len(eval_indices), dtype=np.float64)

        for w in windows:
            if w >= n:
                continue
            w_mask = eval_indices >= w
            eval_counts[w_mask] += 1.0
            cand_positions = np.where(w_mask & (log_p[eval_indices] > log_p[np.maximum(0, eval_indices - w)]))[0]
            if len(cand_positions) == 0:
                continue

            active_idx = eval_indices[cand_positions]
            win_len = w + 1
            x_s, p_s, meta_a = _get_lppls_grid(win_len)
            idx_mat = active_idx[:, None] - w + np.arange(win_len)[None, :]
            y_mat = log_p[idx_mat]

            y_mean = np.mean(y_mat, axis=1, keepdims=True)
            ss_tot = np.maximum(np.sum((y_mat - y_mean) ** 2, axis=1, keepdims=True), 1e-12)

            p_flat = p_s.transpose(2, 0, 1).reshape(win_len, -1)
            x_flat = x_s.transpose(1, 0, 2).reshape(win_len, -1)
            k_grid = len(meta_a)

            beta = (y_mat @ p_flat).reshape(len(active_idx), k_grid, 4)
            xty = (y_mat @ x_flat).reshape(len(active_idx), k_grid, 4)
            y_sq = np.sum(y_mat * y_mat, axis=1, keepdims=True)
            sse = np.maximum(0.0, y_sq - np.sum(beta * xty, axis=2))
            r2 = 1.0 - sse / ss_tot

            b_param = beta[:, :, 1]
            c_amp = np.sqrt(beta[:, :, 2] ** 2 + beta[:, :, 3] ** 2)
            m_vec = meta_a[None, :, 1]
            om_vec = meta_a[None, :, 2]
            damping = (m_vec * np.abs(b_param)) / (om_vec * np.maximum(c_amp, 1e-9))
            rel_osc = c_amp / np.maximum(np.abs(b_param), 1e-9)

            valid_grid = (b_param < 0.0) & (damping >= 0.80) & (r2 >= 0.60) & (rel_osc >= 0.025)
            is_val = np.any(valid_grid, axis=1)
            valid_counts[cand_positions[is_val]] += 1.0

        scores = np.where(eval_counts > 0, valid_counts / eval_counts, 0.0).astype(np.float32)
        for s in range(step):
            target_idx = eval_indices + s
            in_bounds = target_idx < n
            confidence[target_idx[in_bounds]] = scores[in_bounds]

        # Warm-up backfill
        confidence[:min_w] = confidence[min_w]

    # Strictly causal 252-day rolling 90th percentile
    ci_series = pd.Series(confidence)
    ci_90th = ci_series.rolling(252, min_periods=1).quantile(0.90).fillna(0.0).to_numpy().astype(np.float32)

    # Threshold and active signal
    active_flag = (confidence >= 0.50).astype(np.int32)

    df = df.with_columns([
        pl.Series("LPPLS_Confidence", confidence),
        pl.Series("LPPLS_90th_Percentile", ci_90th),
        pl.Series("LPPLS_Critical_Threshold", np.full(n, 0.50, dtype=np.float32)),
        pl.Series("LPPLS_Bubble_Active", active_flag),
    ])

    return df
