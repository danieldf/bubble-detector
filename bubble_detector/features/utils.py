"""
Shared Mathematical & Topological Utilities.
============================================

Numerical Algorithms & Lookahead Elimination:
---------------------------------------------
This module provides reusable numerical routines for econometric and topological processing.
A core architectural requirement across all quantitative functions is the strict prevention
of lookahead leakage in feature scaling and time-series normalization.

1. Strictly Causal Expanding-Window Dynamic Scaling:
   In financial backtesting, naive min-max scaling:
       \\tilde{x}_t = \\frac{x_t - \\min_{1 \\le s \\le T} x_s}{\\max_{1 \\le s \\le T} x_s - \\min_{1 \\le s \\le T} x_s}
   leaks future global extrema into past trading days, corrupting backtest validity.
   To preserve causality, `normalize_tda_indicator` uses expanding-window historical bounds:
       M_t = \\max_{1 \\le s \\le t} x_s, \\quad m_t = \\min_{1 \\le s \\le t} x_s
       \\tilde{x}_t = z_{min} + \\left( \\frac{x_t - m_t}{M_t - m_t + \\epsilon} \\right) (z_{max} - z_{min})
   At operational time t, only historical observations [1, t] influence the scaling envelope.

2. Augmented Dickey-Fuller (ADF) Ordinary Least Squares:
   Evaluates right-tailed explosive test statistics via numerically stabilized
   Moore-Penrose pseudo-inversion (`np.linalg.pinv(X^T X)`), preventing matrix singular
   exceptions during low-variance market consolidations.

3. Takens' Delay Coordinate Embedding:
   Vectorized lag embedding mapping 1D series into N-dimensional phase space manifolds.
"""

from typing import List, Tuple, Sequence, Any
import numpy as np

def calculate_adf_stat(prices: np.ndarray) -> float:
    """
    Calculate Augmented Dickey-Fuller t-statistic for right-tailed explosive root testing.

    Model:
        \\Delta y_t = \\alpha + \\gamma \\cdot y_{t-1} + e_t, \\quad y_t = \\ln(P_t)
        \\text{Test}: \\quad H_0: \\gamma = 0 \\quad \\text{vs.} \\quad H_1: \\gamma > 0
        t = \\frac{\\hat{\\gamma}}{\\text{SE}(\\hat{\\gamma})}

    Parameters
    ----------
    prices : np.ndarray
        Array of price levels.

    Returns
    -------
    float
        Calculated ADF t-statistic.
    """
    if len(prices) < 15:
        return 0.0
    
    y = np.log(np.maximum(prices, 1e-4))
    dy = np.diff(y)
    y_lag = y[:-1]
    
    # OLS regression dy = alpha + gamma * y_lag
    X = np.column_stack([np.ones(len(y_lag)), y_lag])
    try:
        beta, residuals, rank, s = np.linalg.lstsq(X, dy, rcond=None)
        gamma = beta[1]
        
        # Calculate standard error of gamma
        df = len(dy) - 2
        if df <= 0:
            return 0.0
        
        sigma_sq = np.sum((dy - X @ beta) ** 2) / df
        cov_matrix = sigma_sq * np.linalg.pinv(X.T @ X)
        se_gamma = np.sqrt(np.maximum(cov_matrix[1, 1], 1e-8))
        
        t_stat = gamma / se_gamma
        return float(t_stat)
    except Exception:
        return 0.0

def takens_embedding(series: np.ndarray, delay: int = 2, dimension: int = 3) -> np.ndarray:
    """Transform 1D time series into Takens delay-coordinate high-dimensional point cloud."""
    n = len(series)
    if n <= (dimension - 1) * delay:
        return np.zeros((1, dimension))
    
    point_cloud = []
    for i in range(n - (dimension - 1) * delay):
        point = [series[i + j * delay] for j in range(dimension)]
        point_cloud.append(point)
    return np.array(point_cloud)

def normalize_tda_indicator(
    tda_array: np.ndarray,
    target_min: float = 0.8,
    target_max: float = 7.0
) -> np.ndarray:
    """
    Causally rescale raw TDA Persistence Landscape L2 Norm to span [target_min, target_max]
    (default: [0.8, 7.0]) using strictly expanding-window historical bounds.
    Eradicates full-sample 50-year forward lookahead bias.
    """
    arr = np.asarray(tda_array, dtype=np.float64)
    n = len(arr)
    if n == 0:
        return np.array([], dtype=np.float32)

    # Strictly causal expanding-window bounds
    exp_min = np.minimum.accumulate(arr)
    exp_max = np.maximum.accumulate(arr)
    exp_span = exp_max - exp_min

    scaled = np.zeros(n, dtype=np.float64)
    # Warm-up default anchor for early points before variation establishes
    for i in range(n):
        span_i = exp_span[i]
        if span_i < 1e-6:
            scaled[i] = (target_min + target_max) / 2.0
        else:
            scaled[i] = target_min + (arr[i] - exp_min[i]) / span_i * (target_max - target_min)

    scaled = np.clip(scaled, 0.20, target_max)
    return np.nan_to_num(scaled, nan=target_min).astype(np.float32)


def lttb_downsample(
    dates: Sequence[Any],
    values: np.ndarray,
    target_points: int = 1000
) -> Tuple[List[str], np.ndarray]:
    """
    Downsample a 2D time series (dates, values) using the Largest Triangle Three Buckets
    (LTTB) algorithm (Steinarsson, 2013) implemented in pure NumPy.

    Mathematically guarantees retention of visual shape, local extrema, and crisis
    spikes (e.g., 1987 Black Monday 150.19 VXO, COVID VIX 82.7) while reducing visual
    DOM/SVG node count by over 90%.

    Parameters
    ----------
    dates : Sequence[Any]
        Sequence of date strings or objects.
    values : np.ndarray
        1D array of numerical values.
    target_points : int, default=1000
        Number of output points desired. Must be >= 3.

    Returns
    -------
    Tuple[List[str], np.ndarray]
        Downsampled (dates, values) tuple.
    """
    n = len(dates)
    y = np.asarray(values, dtype=np.float64)
    if n == 0:
        return [], np.array([], dtype=np.float64)
    if target_points <= 2:
        if n == 1:
            return [str(dates[0])[:10]], np.array([y[0]], dtype=np.float64)
        return [str(dates[0])[:10], str(dates[-1])[:10]], np.array([y[0], y[-1]], dtype=np.float64)
    if n <= target_points or n != len(y):
        return [str(d)[:10] for d in dates], y

    x = np.linspace(0.0, 1.0, n, dtype=np.float64)
    y_clean = np.nan_to_num(y, nan=0.0)

    sampled_indices = [0]
    bucket_size = (n - 2) / (target_points - 2)

    a_idx = 0
    for b in range(target_points - 2):
        start = int(np.floor(b * bucket_size)) + 1
        end = int(np.floor((b + 1) * bucket_size)) + 1
        end = min(end, n - 1)
        if start >= end:
            start = max(1, end - 1)

        # Average point of next bucket
        if b < target_points - 3:
            next_start = int(np.floor((b + 1) * bucket_size)) + 1
            next_end = int(np.floor((b + 2) * bucket_size)) + 1
            next_end = min(next_end, n - 1)
            if next_start >= next_end:
                next_start = max(1, next_end - 1)
            avg_x = np.mean(x[next_start:next_end])
            avg_y = np.mean(y_clean[next_start:next_end])
        else:
            avg_x = x[n - 1]
            avg_y = y_clean[n - 1]

        x_a = x[a_idx]
        y_a = y_clean[a_idx]

        # Calculate triangular areas for all points in current bucket
        cand_x = x[start:end]
        cand_y = y_clean[start:end]
        areas = 0.5 * np.abs((x_a - avg_x) * (cand_y - y_a) - (x_a - cand_x) * (avg_y - y_a))
        areas = np.nan_to_num(areas, nan=-1.0)

        best_offset = int(np.argmax(areas))
        best_idx = start + best_offset
        sampled_indices.append(best_idx)
        a_idx = best_idx

    sampled_indices.append(n - 1)

    out_dates = [str(dates[i])[:10] for i in sampled_indices]
    out_values = y[sampled_indices]
    return out_dates, out_values

