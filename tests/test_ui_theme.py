"""
Unit tests for UI Theme and Accessibility module (WCAG 2.2 AA Contrast & Typography Tokens).
"""

import pytest
from bubble_detector.ui_theme import (
    calculate_contrast_ratio, is_wcag_aa_compliant,
    get_theme_css, LIGHT_THEME, DARK_THEME, TYPOGRAPHY
)

def test_contrast_ratio_calculation():
    # Black on White should be 21:1
    ratio = calculate_contrast_ratio("#000000", "#FFFFFF")
    assert ratio >= 20.0

    # Same color should be 1:1
    ratio_same = calculate_contrast_ratio("#1C1C1E", "#1C1C1E")
    assert pytest.approx(ratio_same, 0.01) == 1.0

def test_wcag_aa_compliance():
    # Light theme primary text (#1C1C1E) on card bg (#FFFFFF)
    assert is_wcag_aa_compliant(LIGHT_THEME["text_primary"], LIGHT_THEME["bg_card"])

    # Light theme accent blue (#0056B3) on white bg
    assert is_wcag_aa_compliant(LIGHT_THEME["accent_blue"], LIGHT_THEME["bg_card"])

    # Dark theme primary text (#F2F2F7) on card bg (#1C1C1E)
    assert is_wcag_aa_compliant(DARK_THEME["text_primary"], DARK_THEME["bg_card"])

def test_typography_tokens():
    assert "SF Pro Text" in TYPOGRAPHY["font_family"]
    assert "Inter" in TYPOGRAPHY["font_family"]
    assert TYPOGRAPHY["letter_spacing"] == "0.015em"
    assert TYPOGRAPHY["line_height_body"] == "1.5"

def test_theme_css_generation():
    css_light = get_theme_css("light")
    assert "var(--bg-system)" in css_light
    assert LIGHT_THEME["bg_system"] in css_light

    css_dark = get_theme_css("dark")
    assert DARK_THEME["bg_system"] in css_dark

def test_dashboard_state_theme_toggle():
    from bubble_detector.ui.dashboard import DashboardState

    state = DashboardState(load_data=False)
    assert state.theme_mode == "light"
    assert state.get_plotly_template() == "plotly_white"
    assert state.get_palette() == LIGHT_THEME

    # Toggle to dark
    mode = state.toggle_theme()
    assert mode == "dark"
    assert state.theme_mode == "dark"
    assert state.get_plotly_template() == "plotly_dark"
    assert state.get_palette() == DARK_THEME

    # Toggle back to light
    mode_2 = state.toggle_theme()
    assert mode_2 == "light"
    assert state.theme_mode == "light"
    assert state.get_plotly_template() == "plotly_white"
    assert state.get_palette() == LIGHT_THEME
