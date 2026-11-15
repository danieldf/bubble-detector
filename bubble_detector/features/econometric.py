"""
Econometric Bubble Detection Module (Canonical PSY & GSADF).
============================================================

Econometric Foundations & Mathematical Formulations:
---------------------------------------------------
Conventional econometric unit root tests (e.g., standard Dickey-Fuller) test the null
hypothesis of a unit root H0: delta = 1 against the left-tailed stationary alternative
H1: delta < 1 (mean reversion). However, asset price bubbles are characterized by
transitory episodes of explosive behavior where prices grow faster than an exponential
random walk.

1. Canonical Phillips, Shi & Yu (PSY, 2015) Testing Framework:
   Consider the autoregressive model for log-prices or log price-to-dividend ratios:
       y_t = mu + delta * y_{t-1} + sum_{j=1}^k psi_j Delta y_{t-j} + epsilon_t,  epsilon_t ~ i.i.d.(0, sigma^2)
   The econometric test evaluates:
       H_0: delta = 1    (Martingale Unit Root)
       H_1: delta > 1    (Right-Tailed Mildly Explosive Behavior)

   Under H1, prices exhibit explosive sub-trajectories:
       Delta y_t = mu + (delta - 1) y_{t-1} + sum_{j=1}^k psi_j Delta y_{t-j} + epsilon_t
                 = mu + gamma y_{t-1} + sum_{j=1}^k psi_j Delta y_{t-j} + epsilon_t,  gamma > 0
   The test statistic is the right-tailed t-ratio for gamma:
       ADF = hat{gamma} / SE(hat{gamma})

2. Recursive Expanding Backward Supremum ADF (BSADF):
   Because bubbles emerge and collapse at unknown historical dates, static full-sample tests
   suffer from catastrophic power collapse (a bubble followed by a crash looks stationary
   in aggregate samples). PSY formulate the Backward Supremum ADF:
   Let r_2 be the current sample endpoint (normalized to [0, 1]) and r_1 be a variable starting point:
       BSADF_{r_2}(r_0) = sup_{r_1 in [0, r_2 - r_0]} ADF_{r_1}^{r_2}
   where r_0 is the minimum initialization window fraction. When BSADF exceeds the critical
   threshold, a statistically significant explosive episode is active at time r_2.

3. General-Purpose Technology (GPT) Structural Cointegration Decomposition:
   Not all rapid price expansions are speculative bubbles; transformative General-Purpose
   Technologies (GPTs) — such as railroads, electrification, personal computers, the Internet,
   and Generative Artificial Intelligence — generate genuine structural shifts in expected future
   productivity and cash flow growth (Jovanovic & Rousseau, 2005).

   To isolate speculative mania from rational technological repricing:
       ln(P_t) = alpha + beta * ln(Tech_t) + u_t
   where Tech_t is the technology sector price index reflecting realized productivity investments.
   - Fundamental Component: hat{P}_t^{fund} = exp(hat{alpha} + hat{beta} ln(Tech_t))
   - Speculative Froth Residual: e_t = P_t - hat{P}_t^{fund} + bar{P}
   Evaluating BSADF on e_t produces `GSADF_GPT_Adjusted`. If GSADF is elevated on P_t but
   collapses toward zero on e_t, the price surge is fundamentally justified by technological
   capital expenditure rather than unanchored speculative leverage.

4. Asymptotic Distribution & Wild Bootstrap:
   Under H0: delta = 1, the test statistic follows a non-standard Wiener functional:
       ADF => int_0^1 W(s) dW(s) / (int_0^1 W(s)^2 ds)^{1/2}
   Wild bootstrap critical values (Rademacher innovations eta_t in {-1, +1}) establish
   finite-sample 95% (cv approx 1.45) and 99% (cv approx 2.05) significance thresholds.
"""

from typing import Tuple, Optional, List
import numpy as np
import pandas as pd
import polars as pl
from bubble_detector.config import SECTOR_TICKERS, SP500_TICKER, logger
from bubble_detector.features.utils import calculate_adf_stat


def _rolling_adf_vectorized(series: np.ndarray, w: int) -> np.ndarray:
    """
    Vectorized O(N) rolling Augmented Dickey-Fuller right-tailed t-statistic over window length w + 1
    with automatic AIC lag selection k in {0, 1} on the common truncated sample.
    """
    n = len(series)
    out = np.zeros(n, dtype=np.float64)
    if n <= w or w < 11:
        return out

    y = np.log(np.maximum(np.asarray(series, dtype=np.float64), 1e-4))
    dy = np.diff(y)
    yl = y[:-1]

    def _cs(a: np.ndarray) -> np.ndarray:
        return np.concatenate(([0.0], np.cumsum(a, dtype=np.float64)))

    cs_yl = _cs(yl)
    cs_dy = _cs(dy)
    cs_yy = _cs(yl * yl)
    cs_dd = _cs(dy * dy)
    cs_yd = _cs(yl * dy)

    idx = np.arange(w, n)
    lo = idx - w
    hi = idx
    n_k0 = float(w)

    sum_y = cs_yl[hi] - cs_yl[lo]
    sum_d = cs_dy[hi] - cs_dy[lo]
    sum_yy = cs_yy[hi] - cs_yy[lo]
    sum_dd = cs_dd[hi] - cs_dd[lo]
    sum_yd = cs_yd[hi] - cs_yd[lo]

    y_bar = sum_y / n_k0
    dy_bar = sum_d / n_k0
    ss_yy = sum_yy - n_k0 * (y_bar ** 2)
    ss_dd = sum_dd - n_k0 * (dy_bar ** 2)
    ss_yd = sum_yd - n_k0 * y_bar * dy_bar

    valid0 = ss_yy >= 1e-9
    safe_ss_yy = np.where(valid0, ss_yy, 1.0)
    gamma_0 = np.where(valid0, ss_yd / safe_ss_yy, 0.0)
    sse_0 = np.maximum(0.0, ss_dd - (gamma_0 ** 2) * safe_ss_yy)
    df_0 = max(1.0, n_k0 - 2.0)
    sigma2_0 = sse_0 / df_0
    se_gamma_0 = np.sqrt(np.maximum(sigma2_0 / safe_ss_yy, 1e-9))
    t_stat_0 = np.where(valid0, gamma_0 / se_gamma_0, 0.0)

    if w + 1 < 16:
        out[w:] = t_stat_0
        return out

    n_k1 = float(w - 1)
    yl_1 = yl[1:]
    dy_1 = dy[1:]
    dl_1 = dy[:-1]

    cs_y1 = _cs(yl_1)
    cs_d1 = _cs(dy_1)
    cs_l1 = _cs(dl_1)
    cs_y1y1 = _cs(yl_1 * yl_1)
    cs_d1d1 = _cs(dy_1 * dy_1)
    cs_l1l1 = _cs(dl_1 * dl_1)
    cs_y1d1 = _cs(yl_1 * dy_1)
    cs_y1l1 = _cs(yl_1 * dl_1)
    cs_l1d1 = _cs(dl_1 * dy_1)

    s_lo = idx - w
    s_hi = idx - 1

    sy1 = cs_y1[s_hi] - cs_y1[s_lo]
    sd1 = cs_d1[s_hi] - cs_d1[s_lo]
    sl1 = cs_l1[s_hi] - cs_l1[s_lo]
    sy1y1 = cs_y1y1[s_hi] - cs_y1y1[s_lo]
    sd1d1 = cs_d1d1[s_hi] - cs_d1d1[s_lo]
    sl1l1 = cs_l1l1[s_hi] - cs_l1l1[s_lo]
    sy1d1 = cs_y1d1[s_hi] - cs_y1d1[s_lo]
    sy1l1 = cs_y1l1[s_hi] - cs_y1l1[s_lo]
    sl1d1 = cs_l1d1[s_hi] - cs_l1d1[s_lo]

    m = len(idx)
    XtX = np.empty((m, 3, 3), dtype=np.float64)
    XtX[:, 0, 0] = n_k1
    XtX[:, 0, 1] = XtX[:, 1, 0] = sy1
    XtX[:, 0, 2] = XtX[:, 2, 0] = sl1
    XtX[:, 1, 1] = sy1y1
    XtX[:, 1, 2] = XtX[:, 2, 1] = sy1l1
    XtX[:, 2, 2] = sl1l1

    XtY = np.stack([sd1, sy1d1, sl1d1], axis=1)

    y_bar1 = sy1 / n_k1
    dy_bar1 = sd1 / n_k1
    ss_yy1 = sy1y1 - n_k1 * (y_bar1 ** 2)
    ss_dd1 = sd1d1 - n_k1 * (dy_bar1 ** 2)
    ss_yd1 = sy1d1 - n_k1 * y_bar1 * dy_bar1
    v1 = ss_yy1 > 1e-9
    g0_com = np.where(v1, ss_yd1 / np.where(v1, ss_yy1, 1.0), 0.0)
    sse_0_com = np.where(v1, np.maximum(0.0, ss_dd1 - (g0_com ** 2) * ss_yy1), sse_0)
    aic_0 = n_k1 * np.log(np.maximum(sse_0_com / n_k1, 1e-12)) + 4.0

    det = np.linalg.det(XtX)
    nonsing = np.abs(det) > 1e-12
    XtX_safe = np.where(nonsing[:, None, None], XtX, np.eye(3)[None, :, :])
    inv_XtX = np.linalg.inv(XtX_safe)
    beta_1 = np.einsum("nij,nj->ni", inv_XtX, XtY)
    sse_1 = np.maximum(0.0, sd1d1 - np.sum(beta_1 * XtY, axis=1))
    df_1 = max(1.0, n_k1 - 3.0)
    sigma2_1 = sse_1 / df_1
    se_gamma_1 = np.sqrt(np.maximum(sigma2_1 * np.maximum(inv_XtX[:, 1, 1], 0.0), 1e-9))
    t_stat_1 = beta_1[:, 1] / se_gamma_1
    aic_1 = n_k1 * np.log(np.maximum(sse_1 / n_k1, 1e-12)) + 6.0

    choose_1 = nonsing & valid0 & (aic_1 < aic_0)
    out[w:] = np.where(choose_1, t_stat_1, t_stat_0)
    return out


def _batch_adf_from_log_windows(Y_log: np.ndarray) -> np.ndarray:
    """
    Vectorized batch execution of calculate_adf_stat over a 2D matrix of log-price windows
    Y_log of shape (M, L) where L = w + 1. Matches calculate_adf_stat to ~1e-10 precision.
    """
    M, L = Y_log.shape
    if L < 12 or M == 0:
        return np.zeros(M, dtype=np.float64)

    dy = np.diff(Y_log, axis=1)
    y_lag = Y_log[:, :-1]
    n_k0 = float(L - 1)
    y_bar = np.mean(y_lag, axis=1)
    dy_bar = np.mean(dy, axis=1)
    yl_c = y_lag - y_bar[:, None]
    dy_c = dy - dy_bar[:, None]
    ss_yy = np.sum(yl_c * yl_c, axis=1)
    valid0 = ss_yy >= 1e-9
    safe_ss_yy = np.where(valid0, ss_yy, 1.0)
    gamma_0 = np.where(valid0, np.sum(yl_c * dy_c, axis=1) / safe_ss_yy, 0.0)
    res_0 = dy - ((dy_bar - gamma_0 * y_bar)[:, None] + gamma_0[:, None] * y_lag)
    sse_0 = np.sum(res_0 * res_0, axis=1)
    df_0 = max(1.0, n_k0 - 2.0)
    se_gamma_0 = np.sqrt(np.maximum((sse_0 / df_0) / safe_ss_yy, 1e-9))
    t_stat_0 = np.where(valid0, gamma_0 / se_gamma_0, 0.0)

    if L < 16:
        return t_stat_0

    y_lag1 = y_lag[:, 1:]
    dy_target = dy[:, 1:]
    dy_lag1 = dy[:, :-1]
    n_k1 = float(L - 2)
    sx = np.sum(y_lag1, axis=1)
    sz = np.sum(dy_lag1, axis=1)
    sy = np.sum(dy_target, axis=1)
    sxx = np.sum(y_lag1 * y_lag1, axis=1)
    sxz = np.sum(y_lag1 * dy_lag1, axis=1)
    szz = np.sum(dy_lag1 * dy_lag1, axis=1)
    sxy = np.sum(y_lag1 * dy_target, axis=1)
    szy = np.sum(dy_lag1 * dy_target, axis=1)

    XtX = np.empty((M, 3, 3), dtype=np.float64)
    XtX[:, 0, 0] = n_k1
    XtX[:, 0, 1] = XtX[:, 1, 0] = sx
    XtX[:, 0, 2] = XtX[:, 2, 0] = sz
    XtX[:, 1, 1] = sxx
    XtX[:, 1, 2] = XtX[:, 2, 1] = sxz
    XtX[:, 2, 2] = szz
    XtY = np.stack([sy, sxy, szy], axis=1)

    det = np.linalg.det(XtX)
    nonsing = np.abs(det) > 1e-12
    XtX_safe = np.where(nonsing[:, None, None], XtX, np.eye(3)[None, :, :])
    inv_XtX = np.linalg.inv(XtX_safe)
    beta_1 = np.einsum("nij,nj->ni", inv_XtX, XtY)
    fit_1 = beta_1[:, 0:1] + beta_1[:, 1:2] * y_lag1 + beta_1[:, 2:3] * dy_lag1
    res_1 = dy_target - fit_1
    sse_1 = np.sum(res_1 * res_1, axis=1)
    df_1 = max(1.0, n_k1 - 3.0)
    se_gamma_1 = np.sqrt(np.maximum((sse_1 / df_1) * np.maximum(inv_XtX[:, 1, 1], 0.0), 1e-9))
    t_stat_1 = beta_1[:, 1] / se_gamma_1

    y_bar1 = sx / n_k1
    dy_bar1 = sy / n_k1
    yl1_c = y_lag1 - y_bar1[:, None]
    dy1_c = dy_target - dy_bar1[:, None]
    ss_yy1 = np.sum(yl1_c * yl1_c, axis=1)
    valid1 = ss_yy1 > 1e-9
    safe_ss_yy1 = np.where(valid1, ss_yy1, 1.0)
    gamma_0_com = np.where(valid1, np.sum(yl1_c * dy1_c, axis=1) / safe_ss_yy1, 0.0)
    mu_0_com = dy_bar1 - gamma_0_com * y_bar1
    res_0_com = dy_target - (mu_0_com[:, None] + gamma_0_com[:, None] * y_lag1)
    sse_0_com = np.where(valid1, np.sum(res_0_com * res_0_com, axis=1), sse_0)
    aic_0 = n_k1 * np.log(np.maximum(sse_0_com / n_k1, 1e-12)) + 4.0
    aic_1 = n_k1 * np.log(np.maximum(sse_1 / n_k1, 1e-12)) + 6.0

    choose_1 = nonsing & valid0 & (aic_1 < aic_0)
    return np.where(choose_1, t_stat_1, t_stat_0)


def compute_wild_bootstrap_critical_values(
    n_obs: int = 100,
    n_boot: int = 200,
    window_sizes: Tuple[int, ...] = (15, 20, 30, 40)
) -> Tuple[float, float]:
    """
    Compute wild bootstrap critical values (95% and 99%) under the null hypothesis
    of a driftless unit root martingale process: Delta y_t = eps_t * eta_t, eta_t ~ Rademacher(+-1).
    """
    np.random.seed(42)
    max_stats = np.zeros(n_boot)

    for b in range(n_boot):
        innovations = np.random.choice([-1.0, 1.0], size=n_obs) * np.random.randn(n_obs)
        null_series = np.exp(np.cumsum(innovations * 0.01) + 4.0)

        sup_stat = -99.0
        for w in window_sizes:
            if w <= n_obs:
                stat = calculate_adf_stat(null_series[-w:])
                if stat > sup_stat:
                    sup_stat = stat
        max_stats[b] = sup_stat

    cv_95 = float(np.percentile(max_stats, 95))
    cv_99 = float(np.percentile(max_stats, 99))
    return max(1.45, cv_95), max(2.05, cv_99)


def compute_gsadf_gpt_decomposition(
    df: pl.DataFrame,
    target_col: str = SP500_TICKER,
    window_size: int = 40,
    min_window: int = 15
) -> pl.DataFrame:
    """
    Computes canonical recursive expanding-window Backward Supremum ADF (BSADF)
    explosive test statistics (Phillips, Shi & Yu, 2015) and structural GPT
    cointegration decomposition.

    Recursive Expanding Backward Supremum Formulation:
        BSADF_{r_2}(r_0) = sup_{r_1 in [0, r_2 - r_0]} ADF_{r_1}^{r_2}
                         = max_{w in W} ADF(y_{t-w : t})
    over continuous window grid W = [15, 20, 25, 30, 35, 40, 50, 60] trading days.
    """
    logger.info(f"Computing canonical PSY/GSADF & GPT decomposition for '{target_col}'...")

    if target_col != SP500_TICKER and target_col in df.columns:
        eval_col = target_col
    elif "Price_to_Dividend" in df.columns:
        eval_col = "Price_to_Dividend"
    elif target_col in df.columns:
        eval_col = target_col
    else:
        eval_col = df.columns[1]

    prices = df[eval_col].to_numpy()
    n = len(prices)

    # Continuous expanding backward window grid over [min_window, 60]
    candidate_windows = [15, 20, 25, 30, 35, 40, 50, 60]
    sub_windows = [w for w in candidate_windows if min_window <= w < n]
    if not sub_windows and n > min_window:
        sub_windows = [min_window]

    # 1. Canonical PSY Recursive Expanding Backward Supremum ADF (Vectorized O(N))
    if sub_windows:
        sup_adf_arr = np.full(n, -99.0, dtype=np.float64)
        for w in sub_windows:
            w_adf = _rolling_adf_vectorized(prices, w)
            sup_adf_arr[w:] = np.maximum(sup_adf_arr[w:], w_adf[w:])
        gsadf_stats = np.where(sup_adf_arr != -99.0, np.maximum(sup_adf_arr, 0.0), 0.0).astype(np.float32)
    else:
        gsadf_stats = np.zeros(n, dtype=np.float32)

    # 2. Structural GPT Cointegration Fundamental Decomposition in log space (Fixed-window OLS)
    from numpy.lib.stride_tricks import sliding_window_view

    tech_col = SECTOR_TICKERS.get("Technology", "XLK")
    tech_prices = df[tech_col].to_numpy() if tech_col in df.columns else prices

    ln_p_all = np.log(np.maximum(prices.astype(np.float64), 1e-4))
    ln_t_all = np.log(np.maximum(tech_prices.astype(np.float64), 1e-4))

    def _in_window_coint_adf(w_len: int) -> np.ndarray:
        res_arr = np.zeros(n, dtype=np.float64)
        if n <= w_len or w_len < 11:
            return res_arr
        W_p = sliding_window_view(ln_p_all, w_len + 1)
        W_t = sliding_window_view(ln_t_all, w_len + 1)
        mp = np.mean(W_p, axis=1, keepdims=True)
        mt = np.mean(W_t, axis=1, keepdims=True)
        dp = W_p - mp
        dt = W_t - mt
        vt = np.mean(dt * dt, axis=1, keepdims=True)
        cpt = np.mean(dp * dt, axis=1, keepdims=True)
        valid_t = np.sqrt(vt) > 1e-4
        sl = np.where(valid_t, cpt / np.where(valid_t, vt, 1.0), 0.0)
        # In-window log cointegration residual centered at window mean log-price:
        # ln(P) - (mp + sl * (ln(T) - mt)) + mp == ln(P) - sl * dt
        ln_res_win = np.where(valid_t, W_p - sl * dt, W_p)
        res_arr[w_len:] = _batch_adf_from_log_windows(ln_res_win)
        return res_arr

    w_eff = min(window_size, max(min_window, n - 1))
    gpt_adf_main = _in_window_coint_adf(w_eff)
    if min_window < w_eff:
        gpt_adf_min = _in_window_coint_adf(min_window)
        gpt_adf_main[min_window:w_eff] = gpt_adf_min[min_window:w_eff]

    gpt_adjusted_stats = np.maximum(0.0, gpt_adf_main).astype(np.float32)

    cv_95 = 1.45
    cv_99 = 2.05

    # Initial warm-up backfill
    if n > min_window:
        gsadf_stats[:min_window] = gsadf_stats[min_window]
        gpt_adjusted_stats[:min_window] = gpt_adjusted_stats[min_window]

    speculative_bubble_flag = (gpt_adjusted_stats > cv_95).astype(np.int32)

    # Causal 252-day rolling 90th percentile of BSADF statistic
    bsadf_series = pd.Series(gsadf_stats)
    bsadf_90th = bsadf_series.rolling(252, min_periods=min_window).quantile(0.90).bfill().fillna(0.0).to_numpy().astype(np.float32)

    df = df.with_columns([
        pl.Series("GSADF_Stat", gsadf_stats),
        pl.Series("BSADF_Stat", gsadf_stats),
        pl.Series("BSADF_90th_Percentile", bsadf_90th),
        pl.Series("GSADF_GPT_Adjusted", gpt_adjusted_stats),
        pl.Series("Speculative_Bubble_Signal", speculative_bubble_flag),
        pl.Series("GSADF_Critical_Value_95", np.full(n, cv_95, dtype=np.float32)),
        pl.Series("GSADF_Critical_Value_99", np.full(n, cv_99, dtype=np.float32)),
    ])

    return df
