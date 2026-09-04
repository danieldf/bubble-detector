"""
Macro Mahalanobis Distance Regime-Switching Bubble Detector.
============================================================

Mathematical Foundations & Econometric Derivations:
---------------------------------------------------
Traditional statistical bubble models rely on Euclidean distance in feature space:
    d_{Euclid}(z, \\mu) = \\|z - \\mu\\|_2 = \\sqrt{\\sum_{i=1}^k (z_i - \\mu_i)^2}
However, financial indicators exhibit intense cross-sectional collinearity and heterogeneous
volatility. Euclidean distance ignores covariance structures, double-counting correlated
signals (e.g. CAPE and Buffett Indicator) and treating orthogonal informational shocks
identically to collinear movements.

1. Classical Mahalanobis Statistical Distance:
   Given standardized stationary feature vector z_t \\in \\mathbb{R}^k and rolling mean \\mu_t \\in \\mathbb{R}^k:
       D_M(z_t, \\mu_t) = \\sqrt{(z_t - \\mu_t)^T \\Sigma^{-1} (z_t - \\mu_t)}
   where \\Sigma \\in \\mathbb{R}^{k \\times k} is the regularized covariance matrix.
   Geometric Interpretation: Mahalanobis distance defines a Riemannian metric tensor where
   equidistant contours form hyper-ellipsoids aligned with the eigenvectors of \\Sigma.
   Deviations along high-variance directions are discounted, whereas deviations along tight,
   orthogonal axes receive significant statistical weight.

2. The Quadratic Form Symmetry Trap & Directional Asymmetry:
   Because the quadratic form (z - \\mu)^T \\Sigma^{-1} (z - \\mu) is strictly non-negative,
   standard Mahalanobis distance is completely blind to direction:
       D_M(+\\Delta z) = D_M(-\\Delta z)
   In empirical finance, this causes a catastrophic failure: during severe market crashes
   (e.g., October 2008 GFC trough, March 2020 COVID trough), indicators deviate massively
   from their historical means. A naive Mahalanobis detector misinterprets crash troughs
   as "extreme bubbles" and de-risks (sells equities) at the market bottom!

3. Pre-Registered Bubble Direction Vector b \\in \\{-1, +1\\}^k:
   To resolve directional ambiguity with theoretical rigor, each indicator is mapped to an
   economically grounded sign vector b:
       b_j = +1.0 \\implies \\text{Positive excursion represents speculative overextension}
       b_j = -1.0 \\implies \\text{Negative excursion represents valuation bubble (e.g. Real Earnings Yield)}

4. Signed One-Sided Riemannian Bubble Projection:
   We project the standardized innovation vector (z - \\mu) onto the bubble vector b in the
   inner product space defined by metric tensor \\Sigma^{-1}:
       \\text{Score}_{bubble}(t) = \\frac{(z_t - \\mu_t)^T \\Sigma^{-1} b}{\\sqrt{b^T \\Sigma^{-1} b}}
   - \\text{Score}_{bubble} > 0: State vector aligns with speculative bubble overextension.
   - \\text{Score}_{bubble} < 0: State vector aligns with market distress, panic selling, or deep value.

5. Orthogonal Distance Decomposition:
   We partition the raw innovation vector into positive (bubble) and negative (crash) components:
       u_t = \\max(z_t - \\mu_t, 0), \\quad v_t = \\max(-(z_t - \\mu_t), 0)
       \\text{DM}_{bubble}(t) = \\sqrt{u_t^T \\Sigma^{-1} u_t}, \\quad \\text{DM}_{crash}(t) = \\sqrt{v_t^T \\Sigma^{-1} v_t}

6. Robust Covariance Estimation & Numerical Regularization:
   In finite samples (T \\approx 252 trading days, k = 15 indicators), empirical sample
   covariance S is noisy and ill-conditioned (eigenvalues collapse toward zero).
   We provide two robust estimation backends:
   - Ledoit-Wolf Shrinkage (2004): Optimal convex combination of sample covariance and spherical target:
         \\hat{\\Sigma}_{LW} = (1 - \\rho) S + \\rho F, \\quad F = \\frac{\\text{Tr}(S)}{k} I_k
   - Minimum Covariance Determinant (MCD; Rousseeuw, 1984): High-breakdown affine-equivariant estimator.
   - Tikhonov / Ridge Regularization: \\Sigma_{reg} = \\hat{\\Sigma} + \\alpha I_k (\\alpha = 10^{-2})
     guaranteeing strictly positive eigenvalues: \\lambda_i(\\Sigma_{reg}) \\ge \\alpha > 0.

7. Leakage Eradication & Multicollinearity Prevention:
   - `Drawdown_Probability` is strictly excluded from `INDICATORS_15` (supervised target leakage).
   - `P_CAPE` is excluded because it is collinear with `Shiller_CAPE` (det(\\Sigma) \\to 0).
"""

from typing import List, Tuple, Optional, Dict, Any
import numpy as np
import pandas as pd
import polars as pl
from sklearn.covariance import LedoitWolf, MinCovDet

from bubble_detector.config import logger

# Authoritative 15 indicators spanning all quantitative dimensions
# Completely free of supervised target leakage (Drawdown_Probability removed)
# and exact collinearity (P_CAPE removed).
INDICATORS_15: List[str] = [
    "SPY_Dev_200DMA",
    "Shiller_CAPE",
    "Buffett_Indicator",
    "FINRA_Margin_Debt",
    "Margin_Exhaustion_Score",
    "GSADF_Stat",
    "GSADF_GPT_Adjusted",
    "Real_Earnings_Yield",
    "^VIX",
    "^SKEW",
    "OVX_VIX_CrossAsset_Ratio",
    "Housing_Price_to_Income",
    "XLK_SPY_Ratio",
    "TDA_Persistence_L2_Norm",
    "VIX_Term_Structure_Slope"
]

# Pre-registered bubble direction vector b in {-1, +1}^15
# +1 indicates positive excursion represents systemic / bubble overextension
# -1 indicates negative excursion represents valuation stress (high earnings yield = value, low = bubble)
DIRECTION_VECTOR_B: Dict[str, float] = {
    "SPY_Dev_200DMA": 1.0,
    "Shiller_CAPE": 1.0,
    "Buffett_Indicator": 1.0,
    "FINRA_Margin_Debt": 1.0,
    "Margin_Exhaustion_Score": 1.0,
    "GSADF_Stat": 1.0,
    "GSADF_GPT_Adjusted": 1.0,
    "Real_Earnings_Yield": -1.0,  # Lower earnings yield = higher bubble valuation
    "^VIX": 1.0,
    "^SKEW": 1.0,
    "OVX_VIX_CrossAsset_Ratio": 1.0,
    "Housing_Price_to_Income": 1.0,
    "XLK_SPY_Ratio": 1.0,
    "TDA_Persistence_L2_Norm": 1.0,
    "VIX_Term_Structure_Slope": 1.0
}

class MacroMahalanobisDetector:
    """
    Multi-dimensional signed statistical distance regime-switching bubble detector.
    """

    def __init__(
        self,
        indicators: Optional[List[str]] = None,
        rolling_window: int = 252,
        ridge_alpha: float = 1e-2,
        min_equity_exposure: float = 0.20,
        covariance_method: str = "ledoit_wolf"
    ):
        self.indicators = indicators or INDICATORS_15
        self.rolling_window = rolling_window
        self.ridge_alpha = ridge_alpha
        self.min_equity_exposure = min_equity_exposure
        self.covariance_method = covariance_method
        
        # Build direction vector b for configured indicators
        self.b_vec = np.array([DIRECTION_VECTOR_B.get(col, 1.0) for col in self.indicators], dtype=np.float64)

    def _ensure_derived_indicators(self, df: pl.DataFrame) -> pl.DataFrame:
        """Derive stationary indicators if raw ticker series are present."""
        cols = set(df.columns)
        
        # SPY_Dev_200DMA = (SPY - 200DMA) / 200DMA
        if "SPY_Dev_200DMA" not in cols and "SPY" in cols:
            spy_arr = df["SPY"].to_numpy().astype(np.float64)
            s_spy = pd.Series(spy_arr)
            ma200 = s_spy.rolling(200, min_periods=20).mean().to_numpy()
            ma200 = np.where(np.isnan(ma200), spy_arr, ma200)
            dev = (spy_arr - ma200) / np.maximum(ma200, 1e-4)
            df = df.with_columns(pl.Series("SPY_Dev_200DMA", dev.astype(np.float32)))

        # XLK_SPY_Ratio = XLK / SPY
        if "XLK_SPY_Ratio" not in cols:
            if "XLK" in cols and "SPY" in cols:
                ratio = df["XLK"] / pl.max_horizontal(df["SPY"], 1e-4)
                df = df.with_columns(ratio.alias("XLK_SPY_Ratio"))
            elif "XLK" in cols:
                df = df.with_columns(pl.col("XLK").alias("XLK_SPY_Ratio"))

        # Real_Earnings_Yield = 1.0 / Shiller_CAPE
        if "Real_Earnings_Yield" not in cols and "Shiller_CAPE" in cols:
            df = df.with_columns((1.0 / pl.max_horizontal(df["Shiller_CAPE"], 1.0)).alias("Real_Earnings_Yield"))

        # VIX_Term_Structure_Slope = VIX3M / VIX1D
        if "VIX_Term_Structure_Slope" not in cols:
            if "^VIX3M" in cols and "^VIX1D" in cols:
                slope = df["^VIX3M"] / pl.max_horizontal(df["^VIX1D"], 1e-4)
                df = df.with_columns(slope.alias("VIX_Term_Structure_Slope"))
            elif "^VIX" in cols:
                df = df.with_columns(pl.Series("VIX_Term_Structure_Slope", np.full(len(df), 1.05, dtype=np.float32)))

        return df

    def preprocess_stationary_features(
        self,
        df: pl.DataFrame,
        rolling_window: Optional[int] = None
    ) -> np.ndarray:
        """
        Transform indicators into stationary, standardized rolling z-scores
        with strictly causal expanding-window warm-up (zero lookahead).
        """
        df_augmented = self._ensure_derived_indicators(df)
        window = rolling_window or self.rolling_window
        n_rows = len(df_augmented)
        k_features = len(self.indicators)
        Z = np.zeros((n_rows, k_features), dtype=np.float32)

        for j, col in enumerate(self.indicators):
            if col not in df_augmented.columns:
                # If indicator is not present, check fallback or initialize with zeros
                logger.warning(f"Indicator '{col}' missing from DataFrame. Initializing with zeros.")
                continue

            arr = df_augmented[col].to_numpy().astype(np.float64)
            s = pd.Series(arr)
            min_p = max(15, window // 6)
            r_mean = s.rolling(window, min_periods=min_p).mean().to_numpy()
            r_std = s.rolling(window, min_periods=min_p).std().to_numpy()

            # Strictly causal expanding fallback
            exp_mean = s.expanding(min_periods=1).mean().to_numpy()
            exp_std = s.expanding(min_periods=1).std().to_numpy()
            exp_std = np.where(np.isnan(exp_std) | (exp_std < 1e-6), 1.0, exp_std)

            r_mean = np.where(np.isnan(r_mean), exp_mean, r_mean)
            r_std = np.where(np.isnan(r_std) | (r_std < 1e-6), exp_std, r_std)

            z_col = (arr - r_mean) / r_std
            z_col = np.nan_to_num(z_col, nan=0.0).astype(np.float32)
            Z[:, j] = z_col

        return Z

    def compute_signed_mahalanobis_metrics(
        self,
        Z: np.ndarray,
        rolling_window: Optional[int] = None
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """
        Compute:
        1. Mahalanobis Distance (DM)
        2. Signed Bubble Projection Score (Score_bubble = (z - mu)^T Sigma^-1 b / sqrt(b^T Sigma^-1 b))
        3. Bubble Distance Component (DM_bubble)
        4. Crash / Value Distance Component (DM_crash)
        """
        window = rolling_window or self.rolling_window
        n, k = Z.shape
        b = self.b_vec

        m_distances = np.zeros(n, dtype=np.float32)
        signed_scores = np.zeros(n, dtype=np.float32)
        dm_bubble = np.zeros(n, dtype=np.float32)
        dm_crash = np.zeros(n, dtype=np.float32)

        min_samples = max(30, 2 * k)
        eye_k = self.ridge_alpha * np.eye(k, dtype=np.float64)

        for i in range(min_samples, n):
            start_idx = max(0, i - window)
            w = Z[start_idx:i]
            if len(w) < min_samples:
                continue

            mu = np.mean(w, axis=0)
            diff = (Z[i] - mu).astype(np.float64)

            # Robust Covariance Estimation
            try:
                if self.covariance_method == "mcd" and len(w) > 3 * k:
                    cov = MinCovDet(random_state=42).fit(w).covariance_ + eye_k
                elif self.covariance_method == "ledoit_wolf":
                    cov = LedoitWolf().fit(w).covariance_ + eye_k
                else:
                    cov = np.cov(w, rowvar=False) + eye_k
            except Exception:
                cov = np.cov(w, rowvar=False) + eye_k

            try:
                inv_cov = np.linalg.pinv(cov)
                # 1. Total Mahalanobis distance
                dist_sq = float(diff @ inv_cov @ diff)
                m_distances[i] = np.sqrt(max(0.0, dist_sq))

                # 2. Signed One-Sided Bubble Projection
                # Score_bubble = (diff^T Sigma^-1 b) / sqrt(b^T Sigma^-1 b)
                denom = np.sqrt(max(1e-6, float(b @ inv_cov @ b)))
                signed_score = float((diff @ inv_cov @ b) / denom)
                signed_scores[i] = signed_score

                # 3. Partition into Bubble (positive excursion) vs Crash (negative excursion)
                u = np.maximum(diff, 0.0)   # expensive / bubble excursion
                v = np.maximum(-diff, 0.0)  # crash / liquidation excursion

                dm_bubble[i] = np.sqrt(max(0.0, float(u @ inv_cov @ u)))
                dm_crash[i] = np.sqrt(max(0.0, float(v @ inv_cov @ v)))
            except Exception:
                m_distances[i] = 0.0
                signed_scores[i] = 0.0
                dm_bubble[i] = 0.0
                dm_crash[i] = 0.0

        # Warm-up backfill
        if n > min_samples:
            m_distances[:min_samples] = m_distances[min_samples]
            signed_scores[:min_samples] = signed_scores[min_samples]
            dm_bubble[:min_samples] = dm_bubble[min_samples]
            dm_crash[:min_samples] = dm_crash[min_samples]

        return (
            np.clip(m_distances, 0.0, 12.0).astype(np.float32),
            signed_scores.astype(np.float32),
            dm_bubble.astype(np.float32),
            dm_crash.astype(np.float32)
        )

    def compute_mahalanobis_distance(
        self,
        Z: np.ndarray,
        rolling_window: Optional[int] = None,
        ridge_alpha: Optional[float] = None
    ) -> np.ndarray:
        """Calculate standard rolling Mahalanobis Distance for backward compatibility."""
        m_dist, _, _, _ = self.compute_signed_mahalanobis_metrics(Z, rolling_window)
        return m_dist

    def compute_regime_probability(
        self,
        m_distances: np.ndarray,
        rolling_window: Optional[int] = None
    ) -> np.ndarray:
        """
        Convert statistical distance into empirical 1-Year Distance Rank via rolling percentile.
        Formerly named 'Bubble_Regime_Probability'.
        """
        window = rolling_window or self.rolling_window
        n = len(m_distances)
        ranks = np.zeros(n, dtype=np.float32)

        for i in range(n):
            start_idx = max(0, i - window)
            w = m_distances[start_idx : i + 1]
            if len(w) < 5:
                ranks[i] = 0.5
            else:
                val = m_distances[i]
                rank = (np.sum(w < val) + 0.5 * np.sum(w == val)) / float(len(w))
                ranks[i] = float(np.clip(rank, 0.0, 1.0))

        return ranks

    def compute_dynamic_exposure(
        self,
        ranks: np.ndarray,
        signed_scores: Optional[np.ndarray] = None,
        dm_crash: Optional[np.ndarray] = None,
        dm_bubble: Optional[np.ndarray] = None,
        min_exposure: Optional[float] = None
    ) -> np.ndarray:
        """
        Compute continuous portfolio equity sizing (w_equity) eliminating crash-trough derisking.
        Scales down to min_exposure (default 20%) ONLY during bubble overextension (Score_bubble > 0).
        During crash troughs (March 2020, October 2008 where Score_bubble <= 0 or dm_crash > dm_bubble),
        maintains high equity exposure (w_equity >= 0.80) to capture recovery rebound.
        """
        min_exp = min_exposure if min_exposure is not None else self.min_equity_exposure
        n = len(ranks)
        exposure = np.ones(n, dtype=np.float32)

        for i in range(n):
            r = ranks[i]
            score = signed_scores[i] if signed_scores is not None else None
            crash = dm_crash[i] if dm_crash is not None else None
            bubble = dm_bubble[i] if dm_bubble is not None else None

            if signed_scores is None and dm_bubble is None and dm_crash is None:
                # 1-argument signature: standard monotonic rank-based position sizing
                exp_bubble = 1.0 - (1.0 - min_exp) * r
                exposure[i] = float(np.clip(exp_bubble, min_exp, 1.0))
            elif (score is not None and score < -0.5) or (crash is not None and bubble is not None and crash > bubble + 0.5):
                # Deep Value / Liquidation regime: do NOT derisk! Maintain >= 80% equity
                c_val = crash if crash is not None else 0.0
                exposure[i] = float(np.clip(0.85 + 0.15 * min(1.0, c_val / 6.0), 0.80, 1.0))
            elif bubble is not None and bubble > 3.5 and ((score is not None and score > 0.5) or r > 0.70):
                # Bubble / Overextension regime: de-risk proportionally to bubble overextension
                b_severity = max(r, min(1.0, (bubble - 3.5) / 3.0))
                exp_bubble = 1.0 - (1.0 - min_exp) * b_severity
                exposure[i] = float(np.clip(exp_bubble, min_exp, 1.0))
            elif score is not None and score > 1.0 and r > 0.80:
                exp_bubble = 1.0 - (1.0 - min_exp) * r
                exposure[i] = float(np.clip(exp_bubble, min_exp, 1.0))
            else:
                # Normal market regime: full equity
                exposure[i] = 1.0

        return exposure

    def get_top_anomaly_drivers(
        self,
        Z: np.ndarray,
        top_k: int = 3
    ) -> Tuple[List[str], List[str]]:
        """Identify top individual indicator anomaly contributors."""
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
        Execute full Method 1 pipeline:
        Appends:
        - 'Mahalanobis_Distance': Statistical abnormality score (DM).
        - 'Bubble_Score_Signed': Signed projection score.
        - 'DM_Bubble': Expensive/overextension distance component.
        - 'DM_Crash': Depressed/liquidation distance component.
        - 'One_Year_Distance_Rank': Calibrated historical percentile rank.
        - 'Bubble_Regime_Probability': Backward-compatibility alias for distance rank.
        - 'Dynamic_Equity_Exposure': Recommended portfolio equity allocation [0.20, 1.00].
        - 'Regime_Classification': Qualitative regime category.
        - 'Primary_Anomaly_Driver', 'Anomaly_Summary'.
        """
        logger.info("Computing Signed Macro Mahalanobis Distance and Regime Sizing...")
        window = rolling_window or self.rolling_window

        # 1. Stationary z-score transformation
        Z = self.preprocess_stationary_features(df, rolling_window=window)

        # 2. Signed Mahalanobis distance & projection
        m_dist, signed_scores, dm_b, dm_c = self.compute_signed_mahalanobis_metrics(Z, rolling_window=window)

        # 3. 1-Year Distance Rank (replaces Bubble_Regime_Probability)
        ranks = self.compute_regime_probability(m_dist, rolling_window=window)

        # 4. Dynamic portfolio exposure with crash-trough de-risking elimination
        exposure = self.compute_dynamic_exposure(
            ranks,
            signed_scores=signed_scores,
            dm_crash=dm_c,
            dm_bubble=dm_b,
            min_exposure=self.min_equity_exposure
        )
        if len(exposure) > 5:
            exposure = pd.Series(exposure).rolling(5, min_periods=1).mean().to_numpy().astype(np.float32)

        # 5. Qualitative Regime Classification
        regimes = []
        for i in range(len(m_dist)):
            if signed_scores[i] < -0.5 or dm_c[i] > dm_b[i] + 1.0:
                regimes.append("Deep Value / Liquidation")
            elif m_dist[i] > 6.2 and signed_scores[i] > 2.0:
                regimes.append("Extreme Bubble")
            elif m_dist[i] > 4.5 and signed_scores[i] > 1.0:
                regimes.append("Speculative Bubble")
            else:
                regimes.append("Normal Regime")

        # 6. Anomaly attribution
        primary_drivers, summaries = self.get_top_anomaly_drivers(Z, top_k=3)

        res_df = df.with_columns([
            pl.Series("Mahalanobis_Distance", m_dist),
            pl.Series("Bubble_Score_Signed", signed_scores),
            pl.Series("DM_Bubble", dm_b),
            pl.Series("DM_Crash", dm_c),
            pl.Series("One_Year_Distance_Rank", ranks),
            pl.Series("Bubble_Regime_Probability", ranks), # Backward compatibility alias
            pl.Series("Dynamic_Equity_Exposure", exposure),
            pl.Series("Regime_Classification", regimes),
            pl.Series("Primary_Anomaly_Driver", primary_drivers),
            pl.Series("Anomaly_Summary", summaries),
        ])

        logger.info("Successfully appended Signed Mahalanobis regime metrics.")
        return res_df
