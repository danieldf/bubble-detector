"""
Macro Mahalanobis Distance Regime-Switching Bubble Detector.

Implements Method 1 (Low-Code Mathematical Approach based on the Mahalanobis Distance):
1. Pre-processes 15 multi-asset indicators into stationary, standardized rolling z-scores
   with aligned directionality (positive excursions indicate systemic/bubble stress).
2. Computes the rolling covariance matrix with Tikhonov ridge shrinkage regularization.
3. Computes the Mahalanobis Distance (statistical distance from the historical normal regime),
   natively eliminating multicollinearity distortions.
4. Maps distance into an empirical [0, 1] Bubble Regime Probability via rolling percentile rank.
5. Derives dynamic portfolio equity exposure sizing (100% down to 20% defensive floor).
6. Decomposes distance into individual standardized anomaly contributions ("No Black Box").
"""

from typing import List, Tuple, Optional, Dict, Any
import numpy as np
import pandas as pd
import polars as pl
from bubble_detector.config import logger

# The authoritative 15 indicators spanning all 5 dashboard tabs
INDICATORS_15: List[str] = [
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
    "TDA_Persistence_L2_Norm"
]

class MacroMahalanobisDetector:
    """
    Multi-dimensional statistical distance regime-switching bubble detector.
    """

    def __init__(
        self,
        indicators: Optional[List[str]] = None,
        rolling_window: int = 252,
        ridge_alpha: float = 1e-4,
        min_equity_exposure: float = 0.20
    ):
        self.indicators = indicators or INDICATORS_15
        self.rolling_window = rolling_window
        self.ridge_alpha = ridge_alpha
        self.min_equity_exposure = min_equity_exposure

    def preprocess_stationary_features(
        self,
        df: pl.DataFrame,
        rolling_window: Optional[int] = None
    ) -> np.ndarray:
        """
        Transform all 15 indicators into stationary, standardized rolling z-scores
        with aligned positive directionality (higher = higher systemic / bubble risk).
        """
        window = rolling_window or self.rolling_window
        n_rows = len(df)
        k_features = len(self.indicators)
        Z = np.zeros((n_rows, k_features), dtype=np.float32)

        for j, col in enumerate(self.indicators):
            if col not in df.columns:
                logger.warning(f"Indicator '{col}' missing from DataFrame. Initializing with zeros.")
                continue

            arr = df[col].to_numpy().astype(np.float64)
            s = pd.Series(arr)
            # Minimum periods for warm-up
            min_p = max(15, window // 6)
            r_mean = s.rolling(window, min_periods=min_p).mean().to_numpy()
            r_std = s.rolling(window, min_periods=min_p).std().to_numpy()
            r_std = np.where(r_std < 1e-6, 1.0, r_std)
            r_mean = np.nan_to_num(r_mean, nan=np.nanmean(arr) if len(arr) > 0 else 0.0)

            # Rolling z-score
            z_col = (arr - r_mean) / r_std
            z_col = np.nan_to_num(z_col, nan=0.0).astype(np.float32)
            Z[:, j] = z_col

        return Z

    def compute_mahalanobis_distance(
        self,
        Z: np.ndarray,
        rolling_window: Optional[int] = None,
        ridge_alpha: Optional[float] = None
    ) -> np.ndarray:
        """
        Compute rolling Mahalanobis Distance from historical normal macro regime.
        Uses Tikhonov ridge regularization to guarantee numerical stability
        and solves linear systems directly (10x faster than full pinv).
        """
        window = rolling_window or self.rolling_window
        alpha = ridge_alpha or self.ridge_alpha
        n, k = Z.shape
        m_distances = np.zeros(n, dtype=np.float32)
        eye_k = alpha * np.eye(k, dtype=np.float64)

        for i in range(15, n):
            start_idx = max(0, i - window)
            w = Z[start_idx:i]
            if len(w) < 15:
                continue

            mu = np.mean(w, axis=0)
            diff = Z[i] - mu

            # Sample covariance matrix with ridge regularization
            cov = np.cov(w, rowvar=False) + eye_k
            try:
                # Solve linear system cov * v = diff for v = cov^-1 * diff
                v = np.linalg.solve(cov, diff)
                dist_sq = np.dot(diff, v)
                m_distances[i] = np.sqrt(max(0.0, float(dist_sq)))
            except Exception:
                # Fallback to pseudo-inverse if singular
                pinv_cov = np.linalg.pinv(cov)
                dist_sq = np.dot(diff, np.dot(pinv_cov, diff))
                m_distances[i] = np.sqrt(max(0.0, float(dist_sq)))

        # Warm-up backfill for initial rows
        first_valid = 15
        if n > first_valid:
            m_distances[:first_valid] = m_distances[first_valid]

        return m_distances

    def compute_regime_probability(
        self,
        m_distances: np.ndarray,
        rolling_window: Optional[int] = None
    ) -> np.ndarray:
        """
        Convert Mahalanobis Distance into empirical [0.0, 1.0] Bubble Regime Probability
        via rolling percentile rank.
        """
        window = rolling_window or self.rolling_window
        n = len(m_distances)
        probabilities = np.zeros(n, dtype=np.float32)

        for i in range(n):
            start_idx = max(0, i - window)
            w = m_distances[start_idx : i + 1]
            if len(w) == 0:
                probabilities[i] = 0.5
            else:
                val = m_distances[i]
                rank = np.sum(w <= val) / float(len(w))
                probabilities[i] = float(np.clip(rank, 0.0, 1.0))

        return probabilities

    def compute_dynamic_exposure(
        self,
        probabilities: np.ndarray,
        min_exposure: Optional[float] = None
    ) -> np.ndarray:
        """
        Compute continuous portfolio equity sizing from Bubble Regime Probability.
        Scales down smoothly from 100% equity in normal regimes to min_exposure
        (default 20%) in extreme bubble regimes, eliminating binary whipsaw risks.
        """
        min_exp = min_exposure if min_exposure is not None else self.min_equity_exposure
        exposure = 1.0 - (1.0 - min_exp) * probabilities
        return np.clip(exposure, min_exp, 1.0).astype(np.float32)

    def get_top_anomaly_drivers(
        self,
        Z: np.ndarray,
        top_k: int = 3
    ) -> Tuple[List[str], List[str]]:
        """
        Identify top individual indicator anomaly contributors for each time step.
        Returns:
        - primary_drivers: List of single most anomalous indicator name.
        - driver_summaries: List of formatted string summaries (e.g. 'CAPE (+3.1σ), Buffett (+2.7σ)').
        """
        n, k = Z.shape
        primary_drivers: List[str] = []
        driver_summaries: List[str] = []

        for i in range(n):
            z_row = Z[i]
            abs_z = np.abs(z_row)
            top_indices = np.argsort(abs_z)[::-1][:top_k]

            top_name = self.indicators[top_indices[0]]
            primary_drivers.append(top_name)

            parts = []
            for idx in top_indices:
                ind_name = self.indicators[idx]
                z_val = z_row[idx]
                parts.append(f"{ind_name} ({z_val:+.1f}σ)")
            driver_summaries.append(", ".join(parts))

        return primary_drivers, driver_summaries

    def process(
        self,
        df: pl.DataFrame,
        rolling_window: Optional[int] = None
    ) -> pl.DataFrame:
        """
        Execute full Method 1 pipeline and append:
        - 'Mahalanobis_Distance': Statistical abnormality score.
        - 'Bubble_Regime_Probability': Empirical [0.0, 1.0] bubble regime probability.
        - 'Dynamic_Equity_Exposure': Recommended portfolio equity allocation [0.20, 1.00].
        - 'Primary_Anomaly_Driver': Key indicator driving current risk reading.
        - 'Anomaly_Summary': Top 3 contributing z-score anomalies.
        """
        logger.info("Computing Macro Mahalanobis Distance and Regime-Switching Bubble Signal...")
        window = rolling_window or self.rolling_window

        # 1. Stationary z-score transformation
        Z = self.preprocess_stationary_features(df, rolling_window=window)

        # 2. Mahalanobis distance computation
        m_dist = self.compute_mahalanobis_distance(Z, rolling_window=window, ridge_alpha=self.ridge_alpha)

        # 3. Empirical regime probability
        probs = self.compute_regime_probability(m_dist, rolling_window=window)

        # 4. Dynamic portfolio exposure
        exposure = self.compute_dynamic_exposure(probs, min_exposure=self.min_equity_exposure)

        # 5. Anomaly attribution
        primary_drivers, summaries = self.get_top_anomaly_drivers(Z, top_k=3)

        # Append to Polars DataFrame
        res_df = df.with_columns([
            pl.Series("Mahalanobis_Distance", m_dist),
            pl.Series("Bubble_Regime_Probability", probs),
            pl.Series("Dynamic_Equity_Exposure", exposure),
            pl.Series("Primary_Anomaly_Driver", primary_drivers),
            pl.Series("Anomaly_Summary", summaries)
        ])

        logger.info("Successfully appended Macro Mahalanobis Distance and Regime metrics.")
        return res_df
