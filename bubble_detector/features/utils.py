"""
Shared Mathematical & Topological Utilities.

Provides reusable numerical algorithms: Augmented Dickey-Fuller t-statistic calculation,
Takens delay-coordinate embedding, and dynamic range normalization for TDA persistence norms.
"""

import numpy as np

def calculate_adf_stat(prices: np.ndarray) -> float:
    """Calculate Augmented Dickey-Fuller t-statistic for explosive root testing."""
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
    Linearly rescale raw TDA Persistence Landscape L2 Norm to span [target_min, target_max]
    (default: [0.8, 7.0]) matching the vertical y-range of Tabs 5 and 6.
    Ensures that structural topological spikes reach the upper bounds without obscuring baselines.
    """
    arr = np.asarray(tda_array, dtype=np.float64)
    min_val = np.nanmin(arr)
    max_val = np.nanmax(arr)
    span = max_val - min_val

    if span < 1e-6:
        # Avoid division by zero if flat
        return np.full_like(arr, (target_min + target_max) / 2.0, dtype=np.float32)

    scaled = target_min + (arr - min_val) / span * (target_max - target_min)
    return np.nan_to_num(scaled, nan=target_min).astype(np.float32)
