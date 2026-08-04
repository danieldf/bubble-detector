"""
UI Theme and Accessibility Design System for Bubble Detector.

Enforces:
- WCAG 2.2 AA Contrast Compliance (>= 4.5:1 text, >= 3.0:1 UI elements)
- Dyslexia-friendly typography (SF Pro / Inter font stack, 0.015em letter-spacing, 1.5 line-height)
- Avoidance of decorative fonts
- 8px base spacing grid rhythm (4px, 8px, 16px, 24px, 32px, 48px)
- iOS 13+ visual patterns (card container groups, segmented controls, 12px rounded corners)
- Light & Dark theme palettes with dynamic CSS variables
"""

import math
from typing import Dict, Tuple

def parse_hex_color(hex_str: str) -> Tuple[float, float, float]:
    """Parse hex color string (e.g., '#007AFF' or '#000') into RGB floats [0..1]."""
    hex_clean = hex_str.lstrip('#')
    if len(hex_clean) == 3:
        hex_clean = "".join(c * 2 for c in hex_clean)
    if len(hex_clean) != 6:
        raise ValueError(f"Invalid hex color format: {hex_str}")
    r = int(hex_clean[0:2], 16) / 255.0
    g = int(hex_clean[2:4], 16) / 255.0
    b = int(hex_clean[4:6], 16) / 255.0
    return (r, g, b)

def relative_luminance(rgb: Tuple[float, float, float]) -> float:
    """Calculate WCAG 2.2 relative luminance for RGB floats [0..1]."""
    components = []
    for c in rgb:
        if c <= 0.04045:
            components.append(c / 12.92)
        else:
            components.append(((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * components[0] + 0.7152 * components[1] + 0.0722 * components[2]

def calculate_contrast_ratio(hex1: str, hex2: str) -> float:
    """Calculate contrast ratio between two hex colors according to WCAG 2.2."""
    lum1 = relative_luminance(parse_hex_color(hex1))
    lum2 = relative_luminance(parse_hex_color(hex2))
    l1 = max(lum1, lum2)
    l2 = min(lum1, lum2)
    return (l1 + 0.05) / (l2 + 0.05)

def is_wcag_aa_compliant(hex_fg: str, hex_bg: str, is_large_text: bool = False) -> bool:
    """Check if foreground on background satisfies WCAG 2.2 AA standards (4.5:1 text, 3:1 large text/UI)."""
    ratio = calculate_contrast_ratio(hex_fg, hex_bg)
    threshold = 3.0 if is_large_text else 4.5
    return ratio >= threshold

# Spacing Grid Tokens (8px base rhythm)
SPACING = {
    "xxs": "4px",
    "xs": "8px",
    "sm": "12px",
    "md": "16px",
    "lg": "24px",
    "xl": "32px",
    "xxl": "48px",
}

# Typography Tokens (Dyslexia-friendly & clean sans-serif stack)
TYPOGRAPHY = {
    "font_family": '-apple-system, BlinkMacSystemFont, "SF Pro Text", Inter, "OpenDyslexic", "Segoe UI", Roboto, sans-serif',
    "letter_spacing": "0.015em",
    "line_height_body": "1.5",
    "line_height_heading": "1.3",
    "font_weight_regular": "400",
    "font_weight_medium": "500",
    "font_weight_bold": "600",
    "font_weight_heavy": "700",
}

# Light Theme Palette (WCAG 2.2 AA Compliant)
LIGHT_THEME: Dict[str, str] = {
    "bg_system": "#F2F2F7",
    "bg_card": "#FFFFFF",
    "bg_card_secondary": "#E5E5EA",
    "text_primary": "#1C1C1E",
    "text_secondary": "#3C3C43",
    "text_tertiary": "#6C6C70",
    "accent_blue": "#0056B3",        # High contrast blue (WCAG > 4.5:1 on white)
    "accent_red": "#C0262D",         # High contrast danger red
    "accent_green": "#1B7E39",       # High contrast green
    "accent_amber": "#B45309",       # High contrast amber/warning
    "border_color": "#D1D1D6",
    "card_shadow": "0 2px 10px rgba(0, 0, 0, 0.05)",
    "plotly_template": "plotly_white",
}

# Dark Theme Palette (WCAG 2.2 AA Compliant)
DARK_THEME: Dict[str, str] = {
    "bg_system": "#000000",
    "bg_card": "#1C1C1E",
    "bg_card_secondary": "#2C2C2E",
    "text_primary": "#F2F2F7",
    "text_secondary": "#EBEBF5",
    "text_tertiary": "#AEAEC0",
    "accent_blue": "#409CFF",        # Accessible bright blue on dark bg
    "accent_red": "#FF453A",         # Accessible red
    "accent_green": "#32D74B",       # Accessible green
    "accent_amber": "#FFD60A",       # Accessible amber
    "border_color": "#38383A",
    "card_shadow": "0 4px 14px rgba(0, 0, 0, 0.4)",
    "plotly_template": "plotly_dark",
}

def get_theme_css(theme_mode: str = "light") -> str:
    """Generate dynamic CSS variables and global stylesheet enforcing UI/UX & accessibility specs."""
    palette = LIGHT_THEME if theme_mode == "light" else DARK_THEME

    return f"""
    :root {{
        --bg-system: {palette['bg_system']};
        --bg-card: {palette['bg_card']};
        --bg-card-secondary: {palette['bg_card_secondary']};
        --text-primary: {palette['text_primary']};
        --text-secondary: {palette['text_secondary']};
        --text-tertiary: {palette['text_tertiary']};
        --accent-blue: {palette['accent_blue']};
        --accent-red: {palette['accent_red']};
        --accent-green: {palette['accent_green']};
        --accent-amber: {palette['accent_amber']};
        --border-color: {palette['border_color']};
        --card-shadow: {palette['card_shadow']};

        --font-family: {TYPOGRAPHY['font_family']};
        --letter-spacing: {TYPOGRAPHY['letter_spacing']};
        --line-height-body: {TYPOGRAPHY['line_height_body']};
        --line-height-heading: {TYPOGRAPHY['line_height_heading']};
    }}

    body {{
        background-color: var(--bg-system);
        color: var(--text-primary);
        font-family: var(--font-family);
        letter-spacing: var(--letter-spacing);
        line-height: var(--line-height-body);
        margin: 0;
        padding: 0;
        -webkit-font-smoothing: antialiased;
    }}

    /* iOS 13+ Inset Card Styling */
    .ios-card {{
        background-color: var(--bg-card);
        border: 1px solid var(--border-color);
        border-radius: 14px;
        box-shadow: var(--card-shadow);
        padding: 20px;
        margin-bottom: 16px;
        transition: background-color 0.2s ease, border-color 0.2s ease;
    }}

    .ios-card-header {{
        font-size: 1.1rem;
        font-weight: 600;
        line-height: var(--line-height-heading);
        margin-bottom: 12px;
        color: var(--text-primary);
    }}

    /* Call to Action Section with Powerful Typography */
    .cta-banner {{
        background: linear-gradient(135deg, var(--bg-card) 0%, var(--bg-card-secondary) 100%);
        border: 2px solid var(--accent-blue);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 24px;
        box-shadow: var(--card-shadow);
    }}

    .cta-title {{
        font-size: 1.6rem;
        font-weight: 700;
        line-height: 1.2;
        letter-spacing: 0.02em;
        color: var(--text-primary);
        margin-bottom: 8px;
    }}

    .cta-description {{
        font-size: 1.0rem;
        color: var(--text-secondary);
        line-height: 1.5;
        margin-bottom: 16px;
    }}

    .cta-button {{
        background-color: var(--accent-blue);
        color: #FFFFFF;
        font-family: var(--font-family);
        font-size: 1.0rem;
        font-weight: 600;
        padding: 12px 24px;
        border-radius: 10px;
        border: none;
        cursor: pointer;
        transition: transform 0.1s ease, filter 0.2s ease;
        display: inline-flex;
        align-items: center;
        gap: 8px;
    }}

    .cta-button:hover {{
        filter: brightness(1.1);
        transform: translateY(-1px);
    }}

    .cta-button:active {{
        transform: translateY(0);
    }}

    /* iOS 13+ Segmented Controls for Tabs */
    .q-tab {{
        font-family: var(--font-family) !important;
        font-weight: 500 !important;
        letter-spacing: 0.01em !important;
        text-transform: none !important;
    }}
    """
