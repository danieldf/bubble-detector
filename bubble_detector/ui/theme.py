"""
UI Theme and Accessibility Design System Module (UI Package Binding).
=====================================================================

Design System & Mathematical Accessibility Specifications:
----------------------------------------------------------
Institutional financial dashboards require strict adherence to visual accessibility
and human-factors engineering standards to ensure readability under high-stress trading
environments and diverse cognitive or visual conditions.

1. W3C WCAG 2.2 Relative Luminance & Contrast Formula:
   To evaluate perceptual luminance, non-linear 8-bit sRGB color channels [0, 255] are
   normalized to [0.0, 1.0] and transformed through inverse gamma expansion:
       C_{linear} = \\begin{cases}
       \\frac{C_{sRGB}}{12.92} & \\text{if } C_{sRGB} \\le 0.04045 \\\\
       \\left( \\frac{C_{sRGB} + 0.055}{1.055} \\right)^{2.4} & \\text{if } C_{sRGB} > 0.04045
       \\end{cases}
   The relative luminance L is calculated using CIE 1931 standard observer photopic weights:
       L = 0.2126 \\cdot R_{linear} + 0.7152 \\cdot G_{linear} + 0.0722 \\cdot B_{linear}
   The contrast ratio between two colors with luminances L_1 (lighter) and L_2 (darker) is:
       \\text{CR} = \\frac{L_1 + 0.05}{L_2 + 0.05} \\in [1.0, 21.0]

2. WCAG 2.2 Level AA Compliance Thresholds:
   - Body Text (< 18pt regular or < 14pt bold): \\text{CR} \\ge 4.5:1
   - Large Text (>= 18pt or >= 14pt bold) and User Interface Components: \\text{CR} \\ge 3.0:1
   All color tokens in `LIGHT_THEME` and `DARK_THEME` are verified to satisfy Level AA.

3. Cognitive & Dyslexia-Friendly Typographic Standards:
   - Typography stack incorporates Apple SF Pro, Inter, and OpenDyslexic fallbacks.
   - Proportional letter spacing (`0.015em`) and line height (`1.5` for body, `1.3` for headings)
     minimize visual crowding and eye fatigue.
   - Strict avoidance of decorative or low-legibility scripts.

4. 8px Base Spatial Rhythm:
   UI component padding and margins conform to an 8px grid (4px, 8px, 12px, 16px, 24px, 32px, 48px),
   ensuring proportional alignment across varied screen resolutions.

Canonical Module Binding:
-------------------------
This module serves as the primary canonical alias for `bubble_detector.ui_theme`,
providing 100% interoperability across UI packaging structures and agent workflows.
"""

from bubble_detector.ui_theme import (
    LIGHT_THEME,
    DARK_THEME,
    TYPOGRAPHY,
    SPACING,
    parse_hex_color,
    relative_luminance,
    calculate_contrast_ratio,
    is_wcag_aa_compliant,
    get_theme_css,
    get_plotly_template,
)

# Convenient alias
contrast_ratio = calculate_contrast_ratio

__all__ = [
    "LIGHT_THEME",
    "DARK_THEME",
    "TYPOGRAPHY",
    "SPACING",
    "parse_hex_color",
    "relative_luminance",
    "calculate_contrast_ratio",
    "contrast_ratio",
    "is_wcag_aa_compliant",
    "get_theme_css",
    "get_plotly_template",
]
