"""
Unit tests for canonical module aliases and backward compatibility bindings.

Verifies:
1. `bubble_detector.features.margin_leverage` aliases `bubble_detector.features.leverage`.
2. `bubble_detector.features.options_volatility` aliases `bubble_detector.features.options_vol`.
3. `bubble_detector.features.technical` aliases `bubble_detector.features.technicals`.
4. `bubble_detector.ui.theme` aliases `bubble_detector.ui_theme`.
"""

import pytest
import numpy as np
import polars as pl

from bubble_detector.features import (
    margin_leverage,
    options_volatility,
    technical,
    compute_margin_leverage_metrics,
    compute_options_volatility_metrics,
    compute_technical_indicators,
)
from bubble_detector.features.margin_leverage import compute_margin_leverage_metrics as alias_leverage
from bubble_detector.features.options_volatility import compute_options_volatility_metrics as alias_vol
from bubble_detector.features.technical import compute_technical_indicators as alias_tech
from bubble_detector.ui import theme
from bubble_detector.ui.theme import (
    LIGHT_THEME,
    DARK_THEME,
    calculate_contrast_ratio,
    is_wcag_aa_compliant,
)


def test_margin_leverage_alias_parity():
    """Verify margin_leverage module function matches canonical implementation."""
    assert alias_leverage is compute_margin_leverage_metrics
    assert hasattr(margin_leverage, "compute_margin_leverage_metrics")

    # Generate synthetic input
    n = 300
    df = pl.DataFrame({
        "Date": pl.date_range(start=pl.date(2020, 1, 1), end=pl.date(2020, 10, 26), interval="1d", eager=True)[:n],
        "SPY": np.linspace(300, 400, n, dtype=np.float32),
        "FINRA_Margin_Debt": np.linspace(600, 900, n, dtype=np.float32),
    })

    df_canonical = compute_margin_leverage_metrics(df)
    df_alias = alias_leverage(df)
    assert df_canonical.equals(df_alias)


def test_options_volatility_alias_parity():
    """Verify options_volatility module function matches canonical implementation."""
    assert alias_vol is compute_options_volatility_metrics
    assert hasattr(options_volatility, "compute_options_volatility_metrics")

    n = 50
    df = pl.DataFrame({
        "^VIX": np.full(n, 18.0, dtype=np.float32),
        "^VIX3M": np.full(n, 21.0, dtype=np.float32),
        "^SKEW": np.full(n, 135.0, dtype=np.float32),
        "^OVX": np.full(n, 30.0, dtype=np.float32),
        "^VXN": np.full(n, 22.0, dtype=np.float32),
    })

    df_canonical = compute_options_volatility_metrics(df)
    df_alias = alias_vol(df)
    assert df_canonical.equals(df_alias)


def test_technical_alias_parity():
    """Verify technical module function matches canonical implementation."""
    assert alias_tech is compute_technical_indicators
    assert hasattr(technical, "compute_technical_indicators")

    n = 250
    df = pl.DataFrame({
        "SPY": np.linspace(300, 450, n, dtype=np.float32),
    })

    df_canonical = compute_technical_indicators(df)
    df_alias = alias_tech(df)
    assert df_canonical.equals(df_alias)


def test_ui_theme_alias_parity():
    """Verify ui.theme module re-exports tokens and contrast algorithms identically."""
    assert theme.LIGHT_THEME == LIGHT_THEME
    assert theme.DARK_THEME == DARK_THEME
    assert callable(calculate_contrast_ratio)
    assert is_wcag_aa_compliant(LIGHT_THEME["accent_blue"], LIGHT_THEME["bg_card"])
