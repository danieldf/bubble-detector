"""
Structural Break Machine Learning Classifier.

Utilizes XGBoost with RobustScaler preprocessing and expanding-window TimeSeriesSplit
cross-validation to predict forward drawdown risk and structural break probabilities.
"""

from typing import Dict, List, Tuple
import numpy as np
import polars as pl
from sklearn.model_selection import TimeSeriesSplit
from sklearn.preprocessing import RobustScaler
from sklearn.ensemble import HistGradientBoostingClassifier, GradientBoostingClassifier

from bubble_detector.config import ModelTrainingError, logger

try:
    from xgboost import XGBClassifier
    HAS_XGBOOST = True
except Exception as e:
    logger.warning(f"XGBoost library import unavailable ({e}). Falling back to Scikit-Learn HistGradientBoostingClassifier.")
    HAS_XGBOOST = False

class StructuralBreakPredictor:
    """Predicts market structural break and drawdown probabilities using Gradient Boosting & RobustScaler."""

    FEATURE_COLS = [
        "P_CAPE_ZScore",
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

    def __init__(self, n_estimators: int = 100, max_depth: int = 4, learning_rate: float = 0.05):
        self.scaler = RobustScaler()
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.learning_rate = learning_rate
        self.model = self._create_model(n_estimators, max_depth, learning_rate)
        self.is_trained = False

    def _prepare_data(self, df: pl.DataFrame) -> Tuple[np.ndarray, np.ndarray]:
        """Extract features and construct forward drawdown target variable."""
        # Fill missing required columns if not present
        df_cols = df.columns
        for col in self.FEATURE_COLS:
            if col not in df_cols:
                df = df.with_columns(pl.Series(col, np.zeros(len(df), dtype=np.float32)))

        # Feature matrix X
        X = df.select(self.FEATURE_COLS).to_numpy()
        X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)

        # Target variable y: Forward 20-day drawdown > 5%
        if "SPY" in df_cols:
            prices = df["SPY"].to_numpy()
            forward_returns = np.full(len(prices), 0.0, dtype=np.float32)
            for i in range(len(prices) - 20):
                forward_returns[i] = (prices[i + 20] - prices[i]) / prices[i]
            y = (forward_returns < -0.05).astype(np.int32)
        else:
            # Synthetic break targets based on leverage exhaustion and GSADF
            gsadf = df["GSADF_GPT_Adjusted"].to_numpy() if "GSADF_GPT_Adjusted" in df_cols else np.zeros(len(df))
            y = (gsadf > 1.45).astype(np.int32)

        return X, y

    def fit_walk_forward(self, df: pl.DataFrame, n_splits: int = 5, embargo_window: int = 20) -> Dict[str, float]:
        """
        Train ML model using expanding window TimeSeriesSplit cross-validation
        with a purge embargo gap to eliminate overlapping forward target leakage.
        """
        logger.info(f"Training StructuralBreakPredictor with {n_splits}-fold TimeSeriesSplit (embargo={embargo_window})...")
        X, y = self._prepare_data(df)

        if len(X) < 50:
            raise ModelTrainingError("Insufficient data rows to perform walk-forward cross validation.")

        # Mask unobservable terminal forward return rows for training
        if len(X) > embargo_window + 30:
            X_obs = X[:-embargo_window]
            y_obs = y[:-embargo_window]
        else:
            X_obs = X
            y_obs = y

        tss = TimeSeriesSplit(n_splits=n_splits)
        fold_accuracies = []

        for fold, (train_idx, val_idx) in enumerate(tss.split(X_obs)):
            # Apply purge embargo: drop the last `embargo_window` rows of train to avoid leaking into validation
            if len(train_idx) > embargo_window + 10:
                train_idx_purged = train_idx[:-embargo_window]
            else:
                train_idx_purged = train_idx

            X_train, y_train = X_obs[train_idx_purged], y_obs[train_idx_purged]
            X_val, y_val = X_obs[val_idx], y_obs[val_idx]

            # Fit RobustScaler on training fold only (zero look-ahead bias)
            scaler_fold = RobustScaler()
            X_train_scaled = scaler_fold.fit_transform(X_train)
            X_val_scaled = scaler_fold.transform(X_val)

            model_fold = self._create_model(n_estimators=30, max_depth=3, learning_rate=0.05)
            model_fold.fit(X_train_scaled, y_train)

            val_preds = model_fold.predict(X_val_scaled)
            acc = float(np.mean(val_preds == y_val))
            fold_accuracies.append(acc)

        # Final fit on all observable historical rows
        X_scaled = self.scaler.fit_transform(X_obs)
        self.model.fit(X_scaled, y_obs)
        self.is_trained = True

        mean_acc = float(np.mean(fold_accuracies))
        logger.info(f"Walk-forward CV mean accuracy: {mean_acc:.4f}")

        return {"cv_mean_accuracy": mean_acc, "n_splits": n_splits, "embargo_window": embargo_window}

    def predict_drawdown_probability(self, df: pl.DataFrame) -> np.ndarray:
        """Predict structural break drawdown probabilities for input dataframe."""
        if not self.is_trained:
            # Auto-fit if not pre-trained
            self.fit_walk_forward(df)

        X, _ = self._prepare_data(df)
        X_scaled = self.scaler.transform(X)
        probs = self.model.predict_proba(X_scaled)[:, 1]
        return probs
