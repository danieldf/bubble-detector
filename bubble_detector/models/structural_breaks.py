"""
Structural Break Machine Learning Classifier & Probability Calibration Module.
==============================================================================

Financial Machine Learning & Calibration Foundations:
-----------------------------------------------------
Predicting structural regime breaks and drawdown probabilities requires moving beyond
static statistical distances to non-linear, multi-variate supervised pattern classification.
However, applying machine learning to financial time series introduces dangerous pitfalls:
label overlap leakage, serial correlation distortion, and overconfident probability estimates.

1. Definition of the Forward Drawdown Event:
   For operational trading day t, investment horizon H = 20 trading days (~1 month), and
   drawdown threshold \\theta = 0.05 (5% peak-to-trough decline):
       \\text{DD}_{t, H} = \\min_{1 \\le h \\le H} \\left( \\frac{P_{t+h} - P_t}{P_t} \\right)
       y_t = \\mathbb{I}(\\text{DD}_{t, H} < -\\theta) \\in \\{0, 1\\}
   The binary target y_t indicates whether a structural break / sharp correction occurs
   within the forward 20-day horizon.

2. Purged & Embargoed Cross-Validation (López de Prado, 2018):
   Standard k-fold cross-validation assumes independent and identically distributed (i.i.d.)
   observations. In financial markets with multi-day forward labels, observation t overlaps
   with observations t+1, \\dots, t+H-1. Naive random or unpurged splitting leaks future
   information across folds, inflating out-of-sample performance.
   This implementation enforces:
   - Expanding-Window TimeSeriesSplit: Preserves temporal order; fold k trains only on past data.
   - Purge & Embargo Gap: The final H = 20 observations of each training fold are purged:
         \\text{Train\\_Purged}_k = \\text{Train}_k[:-H]
   - Terminal Unobservable Mask: The final H observations of the historical dataset cannot
     observe future prices, and are strictly masked during training.

3. Robust Feature Preprocessing:
   Financial features exhibit fat tails and extreme outliers (e.g. 1987 VXO of 150.19, March 2020 VIX of 82.69).
   Standard mean-variance normalization (z = (x - \\mu)/\\sigma) is corrupted by extreme outliers.
   We implement `RobustScaler`:
       \\tilde{x} = \\frac{x - \\text{median}(x)}{\\text{IQR}(x)}, \\quad \\text{IQR} = Q_3 - Q_1

4. Non-Parametric Isotonic Probability Calibration (Zadrozny & Elkan, 2002):
   Tree-based boosting algorithms maximize rank-order separation (AUC) rather than calibrated
   log-loss, producing probabilities clustered near 0 and 1.
   We fit an out-of-fold monotonic step function m: [0, 1] \\to [0, 1] via pool-adjacent violators:
       \\min_m \\sum_{i=1}^N (y_i - m(\\hat{p}_i))^2 \\quad \\text{s.t.} \\quad \\hat{p}_i \\le \\hat{p}_j \\implies m(\\hat{p}_i) \\le m(\\hat{p}_j)

5. Calibration Verification: Brier Score & Expected Calibration Error (ECE):
   - Brier Score (Brier, 1950):
         \\text{BS} = \\frac{1}{N} \\sum_{i=1}^N (p_i - y_i)^2 \\in [0, 1]
     Benchmark: Unconditional naive climatological baseline \\text{BS}_{base} = \\bar{y}(1 - \\bar{y}).
     A well-calibrated classifier satisfies \\text{BS} < \\text{BS}_{base}.
   - Expected Calibration Error (ECE; Guo et al., 2017):
     Partition predictions into M = 10 equal-width confidence bins B_1, \\dots, B_M:
         \\text{ECE} = \\sum_{m=1}^M \\frac{|B_m|}{N} \\left| \\text{acc}(B_m) - \\text{conf}(B_m) \\right|
"""

from typing import Dict, List, Tuple, Optional, Any
import numpy as np
import polars as pl
from sklearn.model_selection import TimeSeriesSplit
from sklearn.preprocessing import RobustScaler
from sklearn.isotonic import IsotonicRegression
from sklearn.ensemble import HistGradientBoostingClassifier

from bubble_detector.config import ModelTrainingError, logger

try:
    from xgboost import XGBClassifier
    HAS_XGBOOST = True
except Exception as e:
    logger.warning(f"XGBoost library import unavailable ({e}). Using HistGradientBoostingClassifier.")
    HAS_XGBOOST = False

class StructuralBreakPredictor:
    """Predicts market structural break and drawdown probabilities using Gradient Boosting & Calibration."""

    FEATURE_COLS = [
        "CAPE_ZScore",
        "Buffett_ZScore",
        "Margin_Debt_YoY_Pct",
        "Leverage_Exhaustion_Gap",
        "Margin_Exhaustion_Score",
        "GSADF_GPT_Adjusted",
        "TDA_Persistence_L2_Norm",
        "Wavelet_Complexity_Score",
        "VIX_Term_Structure_Slope",
        "OVX_VIX_CrossAsset_Ratio",
        "SKEW_Tail_Risk_Alert",
        "Dispersion_Index_DSPX",
    ]

    def _create_model(self, n_estimators: int = 50, max_depth: int = 3, learning_rate: float = 0.05):
        if HAS_XGBOOST:
            return XGBClassifier(
                n_estimators=n_estimators,
                max_depth=max_depth,
                learning_rate=learning_rate,
                random_state=42,
                eval_metric="logloss",
            )
        else:
            return HistGradientBoostingClassifier(
                max_iter=n_estimators,
                max_depth=max_depth,
                learning_rate=learning_rate,
                random_state=42,
            )

    def __init__(
        self,
        n_estimators: int = 100,
        max_depth: int = 4,
        learning_rate: float = 0.05,
        horizon_days: int = 20,
        drawdown_threshold: float = 0.05
    ):
        self.scaler = RobustScaler()
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.learning_rate = learning_rate
        self.horizon_days = horizon_days
        self.drawdown_threshold = drawdown_threshold
        self.model = self._create_model(n_estimators, max_depth, learning_rate)
        self.calibrator = IsotonicRegression(out_of_bounds="clip")
        self.is_trained = False
        self.is_calibrated = False

    def _prepare_data(self, df: pl.DataFrame) -> Tuple[np.ndarray, np.ndarray]:
        """Extract features and construct forward drawdown target variable without lookahead."""
        df_cols = set(df.columns)
        augmented_df = df

        # Ensure CAPE_ZScore fallback if P_CAPE_ZScore was present in legacy inputs
        if "CAPE_ZScore" not in df_cols:
            if "P_CAPE_ZScore" in df_cols:
                augmented_df = augmented_df.with_columns(pl.col("P_CAPE_ZScore").alias("CAPE_ZScore"))
            elif "Shiller_CAPE" in df_cols:
                augmented_df = augmented_df.with_columns(((pl.col("Shiller_CAPE") - 17.0) / 6.5).alias("CAPE_ZScore"))

        df_cols = set(augmented_df.columns)
        for col in self.FEATURE_COLS:
            if col not in df_cols:
                augmented_df = augmented_df.with_columns(pl.Series(col, np.zeros(len(augmented_df), dtype=np.float32)))

        X = augmented_df.select(self.FEATURE_COLS).to_numpy()
        X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)

        # Target variable y: Forward drawdown > threshold over horizon
        if "SPY" in df_cols:
            prices = augmented_df["SPY"].to_numpy().astype(np.float64)
            n_p = len(prices)
            y = np.zeros(n_p, dtype=np.int32)
            for i in range(n_p - self.horizon_days):
                fwd_min = np.min(prices[i : i + self.horizon_days + 1])
                dd = (fwd_min - prices[i]) / prices[i]
                if dd < -self.drawdown_threshold:
                    y[i] = 1
        else:
            gsadf = augmented_df["GSADF_GPT_Adjusted"].to_numpy() if "GSADF_GPT_Adjusted" in df_cols else np.zeros(len(augmented_df))
            y = (gsadf > 1.45).astype(np.int32)

        return X, y

    def fit_walk_forward(
        self,
        df: pl.DataFrame,
        n_splits: int = 5,
        embargo_window: int = 20
    ) -> Dict[str, float]:
        """
        Train ML model and fit isotonic probability calibrator using expanding-window
        TimeSeriesSplit cross-validation with a purge embargo gap.
        """
        logger.info(f"Training StructuralBreakPredictor with {n_splits}-fold TimeSeriesSplit (embargo={embargo_window})...")
        X, y = self._prepare_data(df)

        if len(X) < 50:
            raise ModelTrainingError("Insufficient data rows to perform walk-forward cross validation.")

        # Mask unobservable terminal forward return rows
        eff_embargo = max(embargo_window, self.horizon_days)
        if len(X) > eff_embargo + 30:
            X_obs = X[:-eff_embargo]
            y_obs = y[:-eff_embargo]
        else:
            X_obs = X
            y_obs = y

        tss = TimeSeriesSplit(n_splits=n_splits)
        fold_accuracies = []
        oof_preds = []
        oof_true = []

        for fold, (train_idx, val_idx) in enumerate(tss.split(X_obs)):
            if len(train_idx) > eff_embargo + 10:
                train_idx_purged = train_idx[:-eff_embargo]
            else:
                train_idx_purged = train_idx

            X_train, y_train = X_obs[train_idx_purged], y_obs[train_idx_purged]
            X_val, y_val = X_obs[val_idx], y_obs[val_idx]

            # Fit RobustScaler on training fold only
            scaler_fold = RobustScaler()
            X_train_scaled = scaler_fold.fit_transform(X_train)
            X_val_scaled = scaler_fold.transform(X_val)

            model_fold = self._create_model(n_estimators=30, max_depth=3, learning_rate=0.05)
            model_fold.fit(X_train_scaled, y_train)

            val_probs = model_fold.predict_proba(X_val_scaled)[:, 1]
            val_preds = (val_probs > 0.5).astype(np.int32)
            fold_accuracies.append(float(np.mean(val_preds == y_val)))

            oof_preds.extend(val_probs.tolist())
            oof_true.extend(y_val.tolist())

        # Fit isotonic calibrator on out-of-fold predictions
        oof_preds_arr = np.array(oof_preds, dtype=np.float64)
        oof_true_arr = np.array(oof_true, dtype=np.float64)
        if len(oof_preds_arr) > 20 and len(np.unique(oof_true_arr)) > 1:
            self.calibrator.fit(oof_preds_arr, oof_true_arr)
            self.is_calibrated = True

        # Final fit on all observable historical rows
        X_scaled = self.scaler.fit_transform(X_obs)
        self.model.fit(X_scaled, y_obs)
        self.is_trained = True

        mean_acc = float(np.mean(fold_accuracies))
        
        # Calculate Brier score and baseline
        brier = self.compute_brier_score(oof_true_arr, oof_preds_arr) if len(oof_preds_arr) > 0 else 0.0
        p_base = float(np.mean(oof_true_arr)) if len(oof_true_arr) > 0 else 0.5
        brier_baseline = float(p_base * (1.0 - p_base))

        logger.info(f"Walk-forward CV mean accuracy: {mean_acc:.4f}, Brier: {brier:.4f} (baseline: {brier_baseline:.4f})")

        return {
            "cv_mean_accuracy": mean_acc,
            "n_splits": n_splits,
            "embargo_window": embargo_window,
            "brier_score": brier,
            "brier_baseline": brier_baseline
        }

    def predict_drawdown_probability(self, df: pl.DataFrame) -> np.ndarray:
        """Predict calibrated structural break drawdown probabilities."""
        if not self.is_trained:
            self.fit_walk_forward(df)

        X, _ = self._prepare_data(df)
        X_scaled = self.scaler.transform(X)
        raw_probs = self.model.predict_proba(X_scaled)[:, 1]

        if self.is_calibrated:
            calibrated_probs = self.calibrator.predict(raw_probs)
            return np.clip(calibrated_probs, 0.0, 1.0).astype(np.float32)

        return np.clip(raw_probs, 0.0, 1.0).astype(np.float32)

    @staticmethod
    def compute_brier_score(y_true: np.ndarray, y_prob: np.ndarray) -> float:
        """Calculate Brier Score: BS = (1/N) * sum((y_prob - y_true)^2)."""
        if len(y_true) == 0:
            return 0.0
        return float(np.mean((np.asarray(y_prob) - np.asarray(y_true)) ** 2))

    @staticmethod
    def compute_reliability_diagram(
        y_true: np.ndarray,
        y_prob: np.ndarray,
        n_bins: int = 10
    ) -> Dict[str, Any]:
        """
        Compute 10-bin Reliability Diagram and Expected Calibration Error (ECE):
            ECE = sum_{m=1}^M (|B_m| / N) * |acc(B_m) - conf(B_m)|
        """
        y_true = np.asarray(y_true, dtype=np.float64)
        y_prob = np.asarray(y_prob, dtype=np.float64)
        n = len(y_true)
        if n == 0:
            return {"ece": 0.0, "bins": []}

        bin_edges = np.linspace(0.0, 1.0, n_bins + 1)
        confidences = []
        accuracies = []
        counts = []
        weighted_errors = []

        for i in range(n_bins):
            low, high = bin_edges[i], bin_edges[i + 1]
            if i == n_bins - 1:
                mask = (y_prob >= low) & (y_prob <= high)
            else:
                mask = (y_prob >= low) & (y_prob < high)

            count = int(np.sum(mask))
            counts.append(count)
            if count > 0:
                bin_conf = float(np.mean(y_prob[mask]))
                bin_acc = float(np.mean(y_true[mask]))
                confidences.append(bin_conf)
                accuracies.append(bin_acc)
                weighted_errors.append((count / n) * abs(bin_acc - bin_conf))
            else:
                confidences.append(float((low + high) / 2.0))
                accuracies.append(0.0)

        ece = float(np.sum(weighted_errors))

        return {
            "ece": ece,
            "bin_edges": bin_edges.tolist(),
            "confidences": confidences,
            "accuracies": accuracies,
            "counts": counts
        }
