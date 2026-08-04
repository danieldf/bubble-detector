"""
UI Components Module.

Provides iOS 13+ card containers, segmented control tab wrappers, and high-impact CTA sections
with powerful typography and accessible styling.
"""

from typing import Callable, Optional
from nicegui import ui
from bubble_detector.ui_theme import TYPOGRAPHY, LIGHT_THEME, DARK_THEME

def create_cta_banner(
    on_run_diagnostics: Optional[Callable] = None,
    on_export_report: Optional[Callable] = None
):
    """
    Renders a Call-To-Action (CTA) section with powerful typography (600-800 weight),
    clear visual hierarchy, and action buttons.
    """
    with ui.element('div').classes('cta-banner w-full'):
        with ui.column().classes('gap-2 w-full'):
            ui.label("Systemic Risk Diagnostic Hub").classes('cta-title')
            ui.label(
                "Run real-time multidimensional econometric diagnostics (GSADF + GPT decomposition, "
                "FINRA margin credit exhaustion, TDA persistence landscape L2 norms, and options term structure) "
                "to evaluate 2026 market crash probability."
            ).classes('cta-description')

            with ui.row().classes('gap-4 items-center mt-2'):
                btn_diagnostics = ui.button(
                    "⚡ Run Real-Time Bubble Diagnostics", on_click=on_run_diagnostics
                ).classes('cta-button')

                btn_export = ui.button(
                    "📄 Export Systemic Risk Assessment Report", on_click=on_export_report
                ).props('outline').classes('cta-button')
                btn_export.style('background-color: transparent; border: 2px solid var(--accent-blue); color: var(--accent-blue);')

def create_ios_card(title: str, subtitle: Optional[str] = None):
    """
    Creates an iOS 13+ inset card container with subtle shadow, rounded corners,
    and dyslexia-friendly label typography.
    """
    card = ui.element('div').classes('ios-card w-full')
    with card:
        with ui.column().classes('w-full gap-1'):
            ui.label(title).classes('ios-card-header')
            if subtitle:
                ui.label(subtitle).style(
                    'font-size: 0.88rem; color: var(--text-secondary); margin-bottom: 12px;'
                )
    return card
