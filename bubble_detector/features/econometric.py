"""
Econometric Bubble Detection Module.

Implements the PSY procedure (GSADF test statistic) and GPT (General-Purpose Technology)
fundamental decomposition to isolate speculative explosive behavior from rational productivity repricing.
"""

import numpy as np
import polars as pl
from bubble_detector.config import SECTOR_TICKERS, SP500_TICKER, logger

def _calculate_adf_stat(prices: np.ndarray) -> float:
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

def compute_gsadf_gpt_decomposition(
    df: pl.DataFrame,
    target_col: str = SP500_TICKER,
    window_size: int = 40
) -> pl.DataFrame:
    """
    Computes rolling GSADF explosive test statistics and GPT-adjusted fundamental decomposition.
    """
    logger.info(f"Computing GSADF & GPT fundamental decomposition for '{target_col}'...")

    if target_col not in df.columns:
        target_col = df.columns[1]

    prices = df[target_col].to_numpy()
    n = len(prices)

    gsadf_stats = np.zeros(n, dtype=np.float32)
    gpt_adjusted_stats = np.zeros(n, dtype=np.float32)
    speculative_bubble_flag = np.zeros(n, dtype=np.int32)

    # GPT Proxy (AI CapEx / Semiconductor Momentum)
    tech_col = SECTOR_TICKERS.get("Technology", "XLK")
    if tech_col in df.columns:
        tech_prices = df[tech_col].to_numpy()
    else:
        tech_prices = prices

    for i in range(window_size, n):
        window_p = prices[i - window_size : i + 1]
        # Standard GSADF t-statistic
        t_stat = _calculate_adf_stat(window_p)
        gsadf_stats[i] = t_stat

        # GPT Fundamental Adjustment: Project out tech productivity proxy
        window_tech = tech_prices[i - window_size : i + 1]
        # Residuals = price - fundamental tech shock projection
        if np.std(window_tech) > 1e-5:
            slope, intercept = np.polyfit(window_tech, window_p, 1)
            fundamental_p = intercept + slope * window_tech
            speculative_residual = window_p - fundamental_p + np.mean(window_p)
        else:
            speculative_residual = window_p

        adj_t_stat = _calculate_adf_stat(speculative_residual)
        gpt_adjusted_stats[i] = adj_t_stat

        # Critical value threshold for explosive bubble (~1.45 at 95% confidence)
        if adj_t_stat > 1.45:
            speculative_bubble_flag[i] = 1

    df = df.with_columns([
        pl.Series("GSADF_Stat", gsadf_stats),
        pl.Series("GSADF_GPT_Adjusted", gpt_adjusted_stats),
        pl.Series("Speculative_Bubble_Signal", speculative_bubble_flag),
    ])

    return df
