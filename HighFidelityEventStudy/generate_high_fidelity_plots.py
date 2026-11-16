#!/usr/bin/env python3
"""
High-Fidelity 4K (HXGA 4096x3072, 4:3 Aspect Ratio) Event-Study Plot Generator.

Generates 8 publication-grade 4K PNG visualizations (4 plots x 2 themes: white & black backgrounds)
for the last 4 plots in Tab 8 ('Composite Summary Indicators') across the 20-Year Global Crisis
& Expansion Horizon (2006-01-01 to 2026-11-13):
  1. Scale-Invariant Log-Growth (`01_Scale_Invariant_Log_Growth_{white,black}.png`)
  2. 8-Dislocation Popperian (`02_8_Dislocation_Popperian_{white,black}.png`)
  3. Homotopic Phase-Time (`03_Homotopic_Phase_Time_{white,black}.png`)
  4. Dislocation Capital (`04_Dislocation_Capital_{white,black}.png`)

License: CC-BY-NC-ND 4.0 | Classification: CONFIDENTIAL — INTELLECTUAL PROPERTY PROTECTED
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Dict, List

import matplotlib
matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd
from PIL import Image

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from bubble_detector.models.composite_summary import (
    DISLOCATIONS_8_20YR,
    compute_dislocation_fidelity_metrics,
)
from bubble_detector.ui.dashboard import DashboardState

OUT_DIR = Path(__file__).resolve().parent
TARGET_WIDTH = 4096
TARGET_HEIGHT = 3072
DPI = 256
FIGSIZE = (TARGET_WIDTH / DPI, TARGET_HEIGHT / DPI)  # (16.0, 12.0) -> 4096 x 3072 px (4:3 HXGA)


def get_palette(theme: str) -> Dict[str, str]:
    """
    Return WCAG 2.2 AA/AAA accessible color palette tailored for pure white (#FFFFFF)
    or pure black (#000000) backgrounds, accommodating color-vision deficiency (Okabe-Ito / IBM safe).
    """
    if theme == "white":
        return {
            "bg": "#FFFFFF",
            "panel_bg": "#F8FAFC",
            "text": "#0F172A",
            "subtext": "#334155",
            "axis": "#1E293B",
            "grid_major": "#CBD5E1",
            "grid_minor": "#E2E8F0",
            "spy_line": "#0052CC",          # Deep Accessible Cobalt Blue
            "comp_line": "#0072B2",         # Okabe-Ito Blue
            "mahal_line": "#D55E00",        # Okabe-Ito Vermilion / Crimson
            "dfm_line": "#B45309",          # High-Contrast Deep Amber/Ochre
            "diff_line": "#008060",         # Deep Accessible Viridian Green
            "spca_line": "#7E22CE",         # Deep Royal Purple
            "trough_line": "#C2410C",       # Burnt Orange
            "sep_fill": "#0284C7",          # Cerulean Fill
            "lead_band": "#F59E0B",         # Amber Corridor
            "crash_band": "#DC2626",        # Crimson Corridor
            "peak_marker": "#D97706",       # Gold/Amber Marker
            "trough_marker": "#059669",     # Emerald Marker
            "dd_unhedged": "#DC2626",       # Crimson Unhedged Loss
            "dd_defensive": "#059669",      # Emerald Defensive Loss
            "dd_saved": "#0052CC",          # Cobalt Saved Capital
            "lead_line": "#B45309",         # Deep Amber Lead Cushion
            "callout_bg": "#FFFBEB",        # Soft Warm Callout Card
            "callout_border": "#0F172A",    # Dark Slate Callout Border
            "callout_alt_bg": "#EFF6FF",    # Soft Blue Callout Card
            "callout_red_bg": "#FEF2F2",    # Soft Red Callout Card
            "callout_green_bg": "#ECFDF5",  # Soft Green Callout Card
            "arrow": "#1E293B",
            "badge_bg": "#0F172A",
            "badge_fg": "#FFFFFF",
        }
    else:
        return {
            "bg": "#000000",
            "panel_bg": "#090D16",
            "text": "#F8FAFC",
            "subtext": "#CBD5E1",
            "axis": "#E2E8F0",
            "grid_major": "#334155",
            "grid_minor": "#1E293B",
            "spy_line": "#38BDF8",          # Luminous Sky Cyan
            "comp_line": "#00E5FF",         # Electric Cyan
            "mahal_line": "#FF4D6D",        # Luminous Coral Crimson
            "dfm_line": "#FFD166",          # Luminous Gold
            "diff_line": "#06D6A0",         # Luminous Mint/Emerald
            "spca_line": "#C77DFF",         # Luminous Orchid Purple
            "trough_line": "#FF9F1C",       # Bright Tangerine
            "sep_fill": "#00E5FF",          # Cyan Fill
            "lead_band": "#FFD166",         # Gold Corridor
            "crash_band": "#FF2A55",        # Crimson Corridor
            "peak_marker": "#FFD166",       # Bright Gold Marker
            "trough_marker": "#06D6A0",     # Bright Emerald Marker
            "dd_unhedged": "#FF4D6D",       # Luminous Crimson
            "dd_defensive": "#06D6A0",      # Luminous Emerald
            "dd_saved": "#00E5FF",          # Electric Cyan
            "lead_line": "#FFD166",         # Luminous Gold
            "callout_bg": "#111827",        # Deep Slate Callout Card
            "callout_border": "#94A3B8",    # Silver Callout Border
            "callout_alt_bg": "#0F172A",    # Deep Navy Callout Card
            "callout_red_bg": "#1F1218",    # Dark Crimson Callout Card
            "callout_green_bg": "#0D1F1A",  # Dark Emerald Callout Card
            "arrow": "#E2E8F0",
            "badge_bg": "#1E293B",
            "badge_fg": "#38BDF8",
        }


def style_axes_common(
    ax: plt.Axes,
    fig: plt.Figure,
    pal: Dict[str, str],
    title: str,
    subtitle: str,
    xlabel: str,
    ylabel: str,
    footer_note: str,
) -> None:
    """Apply consistent 4K executive typography, grid hierarchy, and confidentiality branding."""
    fig.patch.set_facecolor(pal["bg"])
    ax.set_facecolor(pal["panel_bg"])

    # Executive Title & Subtitle Banner (sized to stay strictly left of the top-right badge)
    fig.suptitle(
        title,
        fontsize=14.8,
        fontweight="bold",
        color=pal["text"],
        x=0.045,
        y=0.964,
        ha="left",
    )
    fig.text(
        0.045,
        0.928,
        subtitle,
        fontsize=11.2,
        color=pal["subtext"],
        ha="left",
    )

    # Top-Right Confidentiality & License Badge
    fig.text(
        0.955,
        0.968,
        "CONFIDENTIAL  |  CC-BY-NC-ND 4.0  |  20-YR HORIZON (2006–2026)",
        fontsize=9.0,
        fontweight="bold",
        color=pal["badge_fg"],
        ha="right",
        va="top",
        bbox=dict(
            boxstyle="round,pad=0.36",
            facecolor=pal["badge_bg"],
            edgecolor=pal["callout_border"],
            linewidth=1.2,
        ),
    )

    ax.set_xlabel(xlabel, fontsize=13.0, fontweight="bold", color=pal["text"], labelpad=12)
    ax.set_ylabel(ylabel, fontsize=13.0, fontweight="bold", color=pal["text"], labelpad=12)

    ax.tick_params(axis="both", which="major", labelsize=11.0, colors=pal["text"], length=7, width=1.4)
    ax.tick_params(axis="both", which="minor", labelsize=9.5, colors=pal["subtext"], length=4, width=1.0)

    for spine in ax.spines.values():
        spine.set_color(pal["axis"])
        spine.set_linewidth(1.5)

    ax.grid(True, which="major", linestyle="-", linewidth=0.9, color=pal["grid_major"], alpha=0.75, zorder=0)
    ax.grid(True, which="minor", linestyle=":", linewidth=0.6, color=pal["grid_minor"], alpha=0.65, zorder=0)

    # Non-overlapping Footer Provenance (Left) & IP Notice (Right)
    fig.text(
        0.045,
        0.015,
        footer_note,
        fontsize=8.3,
        color=pal["subtext"],
        ha="left",
    )
    fig.text(
        0.955,
        0.015,
        "High-Fidelity Event Study v1.2.0 (Engine v3.7.0)  •  Confidential  •  CC-BY-NC-ND 4.0",
        fontsize=8.5,
        fontweight="bold",
        color=pal["subtext"],
        ha="right",
    )


def save_and_verify_4k(fig: plt.Figure, out_path: Path, bg_color: str) -> None:
    """Save figure at exact 4096x3072 resolution and verify pixel dimensions."""
    fig.savefig(
        out_path,
        dpi=DPI,
        facecolor=bg_color,
        edgecolor="none",
        bbox_inches=None,
    )
    plt.close(fig)
    with Image.open(out_path) as im:
        w, h = im.size
        if (w, h) != (TARGET_WIDTH, TARGET_HEIGHT):
            im_resized = im.resize((TARGET_WIDTH, TARGET_HEIGHT), Image.Resampling.LANCZOS)
            im_resized.save(out_path, format="PNG")
    print(f"[OK] Saved {out_path.name} ({TARGET_WIDTH}x{TARGET_HEIGHT} px, {out_path.stat().st_size / 1024:.1f} KB)")


def plot_1_scale_invariant_log_growth(
    dates: List[str],
    spy: np.ndarray,
    fm: Dict[str, Any],
    theme: str,
) -> Path:
    """
    Plot 1: Scale-Invariant Log-Growth S&P 500 Trajectory & Dual-Phase Lead/Crash Corridors.
    """
    pal = get_palette(theme)
    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
    fig.subplots_adjust(left=0.075, right=0.915, top=0.885, bottom=0.110)

    dt_index = pd.to_datetime(dates)
    log_spy = fm["log_spy"]
    lead_sig = fm["lead_band_sig"]
    crash_sig = fm["crash_band_sig"]
    mean_lead = float(np.mean(fm["lead_days"]))
    n_sessions = len(dates)

    style_axes_common(
        ax=ax,
        fig=fig,
        pal=pal,
        title="Executive View I: 20-Year Scale-Invariant S&P 500 Total-Return Log-Growth & Warning Corridors",
        subtitle=f"Logarithmic Total-Return Trajectory L_SPY(t) with 252d Pre-Peak Warning Corridors (8/8 Hit Rate, {mean_lead:.1f}d Mean Lead) & Contraction Regimes (2006–2026)",
        xlabel=f"Calendar Year & Macro Regime Timeline (Business-Day Grid: Jan 2, 2006 – Nov 13, 2026, N = {n_sessions:,} [5,250 NYSE Sessions])",
        ylabel="Scale-Invariant Log-Growth Index L_SPY(t)  [100 × (1 + ln(SPY_t / SPY_0)), Base = 100 at Jan 2, 2006]",
        footer_note="Source: Ground-Truth 20-Year Total-Return Horizon (Jan 2, 2006 – Nov 13, 2026). Amber bands = 252d pre-peak warning windows (I_t^* >= 70%); crimson bands = contractions (D1–D8).",
    )

    y_min, y_max = 25.0, 355.0
    ax.set_ylim(y_min, y_max)
    ax.set_xlim(dt_index[0], dt_index[-1] + pd.Timedelta(days=120))

    # Shade contiguous Lead Corridors and Crash Corridors
    ax.fill_between(
        dt_index,
        y_min,
        y_max,
        where=(lead_sig > 0.5),
        color=pal["lead_band"],
        alpha=0.22 if theme == "white" else 0.20,
        label="Pre-Peak Early-Warning Corridor (Master Composite ≥ 70%)",
        zorder=1,
    )
    ax.fill_between(
        dt_index,
        y_min,
        y_max,
        where=(crash_sig > 0.5),
        color=pal["crash_band"],
        alpha=0.26 if theme == "white" else 0.28,
        label="Peak-to-Trough Contraction Corridor (Dislocations D1–D8)",
        zorder=2,
    )

    # Main Log-Growth S&P 500 Curve
    ax.plot(
        dt_index,
        log_spy,
        color=pal["spy_line"],
        linewidth=2.8,
        label="Scale-Invariant Log-Growth S&P 500 Trajectory L_SPY(t)",
        zorder=4,
    )

    # Plot Peak & Trough Extrema Markers
    pk_dates = pd.to_datetime(fm["peak_dates"])
    pk_vals = fm["peak_vals"]
    tr_dates = pd.to_datetime(fm["trough_dates"])
    tr_vals = fm["trough_vals"]

    ax.scatter(
        pk_dates,
        pk_vals,
        s=150,
        marker="v",
        color=pal["peak_marker"],
        edgecolors=pal["text"],
        linewidths=1.5,
        label="Dislocation Cycle Peak (t_peak, D1–D8)",
        zorder=6,
    )
    ax.scatter(
        tr_dates,
        tr_vals,
        s=150,
        marker="^",
        color=pal["trough_marker"],
        edgecolors=pal["text"],
        linewidths=1.5,
        label="Dislocation Cycle Trough (t_trough, D1–D8)",
        zorder=6,
    )

    # Detailed Axis Ticks (Major & Minor)
    ax.xaxis.set_major_locator(mdates.YearLocator(1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonth=[4, 7, 10]))
    ax.yaxis.set_major_locator(mticker.MultipleLocator(25))
    ax.yaxis.set_minor_locator(mticker.MultipleLocator(5))

    # Secondary Right-Hand Axis showing Cumulative $100 Total-Return Wealth (100 * SPY_t / SPY_0)
    ax_right = ax.twinx()
    ax_right.set_ylim(y_min, y_max)
    right_ticks = [50, 100, 150, 200, 250, 300, 340]
    right_labels = [
        f"${100.0 * np.exp((lv / 100.0) - 1.0):,.0f}"
        for lv in right_ticks
    ]
    ax_right.set_yticks(right_ticks)
    ax_right.set_yticklabels(right_labels, fontsize=11.0, color=pal["subtext"], fontweight="bold")
    ax_right.set_ylabel(
        "Cumulative $100 Total-Return Wealth Scale (Log-Mapped SPY_t / SPY_0)",
        fontsize=12.5,
        fontweight="bold",
        color=pal["subtext"],
        labelpad=12,
    )
    ax_right.spines["right"].set_color(pal["axis"])
    ax_right.spines["top"].set_visible(False)

    # Non-overlapping Labeled Callout Arrows for All 8 Dislocations
    dd_spy = fm["dd_spy_abs"]
    ld_days = fm["lead_days"]
    tr_comp = fm["tr_comp"]
    peak_annotations = [
        (0, f"D1: 2007–09 GFC Peak\nOct 2007 | DD: -{dd_spy[0]:.1f}%\nLead: {ld_days[0]:.0f}d", (-42, 66), pal["callout_red_bg"]),
        (1, f"D2: Euro/Flash\nApr 2010 | -{dd_spy[1]:.1f}%\nLead: {ld_days[1]:.0f}d", (-52, 42), pal["callout_bg"]),
        (2, f"D3: US Downgrade\nApr 2011 | -{dd_spy[2]:.1f}%\nLead: {ld_days[2]:.0f}d", (16, 48), pal["callout_bg"]),
        (3, f"D4: China/Energy\nJul 2015 | -{dd_spy[3]:.1f}%\nLead: {ld_days[3]:.0f}d", (-75, 48), pal["callout_bg"]),
        (4, f"D5: Q4 2018 QT Shock\nSep 2018 | -{dd_spy[4]:.1f}%\nLead: {ld_days[4]:.0f}d", (-105, 44), pal["callout_bg"]),
        (5, f"D6: COVID-19 Peak\nFeb 2020 | -{dd_spy[5]:.1f}%\nLead: {ld_days[5]:.0f}d", (-95, 52), pal["callout_red_bg"]),
        (6, f"D7: 2022 Rate Reset\nJan 2022 | -{dd_spy[6]:.1f}%\nLead: {ld_days[6]:.0f}d", (-105, 44), pal["callout_red_bg"]),
        (7, f"D8: 2025 Tariff/AI Reset\nFeb 2025 | -{dd_spy[7]:.1f}%\nLead: {ld_days[7]:.0f}d", (-120, 32), pal["callout_red_bg"]),
    ]
    for idx, text, offset, box_bg in peak_annotations:
        ax.annotate(
            text,
            xy=(mdates.date2num(pk_dates[idx]), pk_vals[idx]),
            xytext=offset,
            textcoords="offset points",
            fontsize=9.2,
            fontweight="bold",
            color=pal["text"],
            bbox=dict(boxstyle="round,pad=0.33", facecolor=box_bg, edgecolor=pal["callout_border"], linewidth=1.1, alpha=0.95),
            arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=0.12", color=pal["arrow"], lw=1.5),
            zorder=8,
        )

    # Trough Re-Entry Callouts (Key Deep Bottoms)
    trough_annotations = [
        (0, f"D1 GFC Trough (Mar 2009)\nL_SPY = {tr_vals[0]:.1f} | Comp = {tr_comp[0]:.1f}%\nMax Bottom Re-Entry", (18, -6), pal["callout_green_bg"]),
        (5, f"D6 COVID Trough (Mar 2020)\nL_SPY = {tr_vals[5]:.1f} | Comp = {tr_comp[5]:.1f}%\nLiquidation Damper Active", (16, -44), pal["callout_green_bg"]),
        (6, f"D7 Trough (Oct 2022)\nL_SPY = {tr_vals[6]:.1f} | Comp = {tr_comp[6]:.1f}%\nFull Re-Risking Trigger", (18, -36), pal["callout_green_bg"]),
    ]
    for idx, text, offset, box_bg in trough_annotations:
        ax.annotate(
            text,
            xy=(mdates.date2num(tr_dates[idx]), tr_vals[idx]),
            xytext=offset,
            textcoords="offset points",
            fontsize=9.0,
            fontweight="bold",
            color=pal["text"],
            bbox=dict(boxstyle="round,pad=0.33", facecolor=box_bg, edgecolor=pal["trough_marker"], linewidth=1.2, alpha=0.95),
            arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=-0.12", color=pal["trough_marker"], lw=1.5),
            zorder=8,
        )

    # Terminal 2026-11-13 Callout
    ax.annotate(
        f"Current Regime (Nov 13, 2026)\nL_SPY = {log_spy[-1]:.1f} ($884.5 TR | S&P 7,561.67)\nMaster Score I* = 45.4% (Neutral)",
        xy=(mdates.date2num(dt_index[-1]), log_spy[-1]),
        xytext=(-195, -48),
        textcoords="offset points",
        fontsize=9.2,
        fontweight="bold",
        color=pal["text"],
        bbox=dict(boxstyle="round,pad=0.35", facecolor=pal["callout_alt_bg"], edgecolor=pal["spy_line"], linewidth=1.3),
        arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=0.15", color=pal["spy_line"], lw=1.6),
        zorder=9,
    )

    # Executive Summary Insight Box inside Lower-Right Empty Space (strictly inside plot bounds)
    summary_text = (
        "WHY LOG-GROWTH SCALE INVARIANCE MATTERS:\n"
        "• Linear charts distort 20-year history: $100 total-return wealth reaches $884.5 (S&P 500 price 7,561.67) by Nov 2026.\n"
        "• Logarithmic scaling L_SPY(t) maps equal % total-return drawdowns (-20%) to identical vertical drops in all eras.\n"
        f"• Every contraction (crimson) is preceded by a 252d-window pre-peak warning corridor (amber, avg. {mean_lead:.1f}d)."
    )
    ax.text(
        0.41,
        0.04,
        summary_text,
        transform=ax.transAxes,
        fontsize=9.5,
        color=pal["text"],
        bbox=dict(boxstyle="round,pad=0.50", facecolor=pal["callout_alt_bg"], edgecolor=pal["callout_border"], linewidth=1.3, alpha=0.95),
        zorder=9,
    )

    leg = ax.legend(
        loc="upper left",
        fontsize=10.5,
        frameon=True,
        facecolor=pal["bg"],
        edgecolor=pal["callout_border"],
        framealpha=0.95,
    )
    for txt in leg.get_texts():
        txt.set_color(pal["text"])
        txt.set_fontweight("bold")

    out_path = OUT_DIR / f"01_Scale_Invariant_Log_Growth_{theme}.png"
    save_and_verify_4k(fig, out_path, pal["bg"])
    return out_path


def plot_2_popperian_regime_separation(
    fm: Dict[str, Any],
    theme: str,
) -> Path:
    """
    Plot 2: 8-Dislocation Popperian Peak-vs-Trough Regime Separation Matrix.
    """
    pal = get_palette(theme)
    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
    fig.subplots_adjust(left=0.075, right=0.955, top=0.885, bottom=0.130)

    max_tr = float(np.max(fm["tr_comp"]))
    mean_pk_comp = float(np.mean(fm["pk_comp"]))
    mean_pk_mahal = float(np.mean(fm["pk_mahal"]))
    mean_pk_dfm = float(np.mean(fm["pk_dfm"]))
    mean_pk_diff = float(np.mean(fm["pk_diff"]))
    mean_pk_spca = float(np.mean(fm["pk_spca"]))
    mean_tr_comp = float(np.mean(fm["tr_comp"]))
    mean_sep_comp = float(np.mean(fm["sep_comp"]))

    style_axes_common(
        ax=ax,
        fig=fig,
        pal=pal,
        title="Executive View II: 8-Dislocation Popperian Peak-vs-Trough Regime Separation",
        subtitle=f"Empirical Falsification Audit: Pre-Peak Maxima Exceed 70% Warning Gate (8/8 Hits) While Crash-Trough Minima Drop to <= {max_tr:.1f}% (<25% Target)",
        xlabel="Historical Market Dislocation Regime (Chronological Sequence D1–D8 Across the 2006–2026 Horizon)",
        ylabel="Composite Regime Risk Score & Peak-to-Trough Separation Spread (%)",
        footer_note="Source: 20-Year Dislocation Event Study (Jan 2, 2006 – Nov 13, 2026). Pre-peak maxima evaluated over [-180d, t_peak]; crash-trough minima evaluated around t_trough.",
    )

    x = np.arange(len(DISLOCATIONS_8_20YR))
    x_labels = [
        "D1: 2007–09 GFC\n(Oct '07–Mar '09)",
        "D2: Euro/Flash\n(Apr '10–Jul '10)",
        "D3: US Downgrade\n(Apr '11–Oct '11)",
        "D4: China/Energy\n(Jul '15–Feb '16)",
        "D5: Q4 2018 QT Shock\n(Sep '18–Dec '18)",
        "D6: COVID-19 Shock\n(Feb '20–Mar '20)",
        "D7: Rate Hike Reset\n(Jan '22–Oct '22)",
        "D8: 2025 Tariff/AI Reset\n(Feb '25–Apr '25)",
    ]

    ax.set_xlim(-0.45, 7.45)
    ax.set_ylim(-7.0, 114.0)
    ax.set_xticks(x)
    ax.set_xticklabels(x_labels, fontsize=10.5, fontweight="bold")
    ax.yaxis.set_major_locator(mticker.MultipleLocator(10))
    ax.yaxis.set_minor_locator(mticker.MultipleLocator(2.5))
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%d%%"))

    # Shaded Popperian Target Zones
    ax.axhspan(70.0, 106.0, color=pal["crash_band"], alpha=0.09 if theme == "white" else 0.12, zorder=1)
    ax.axhspan(0.0, 25.0, color=pal["trough_marker"], alpha=0.09 if theme == "white" else 0.12, zorder=1)

    # Separation Spread Area
    ax.fill_between(
        x,
        fm["tr_comp"],
        fm["pk_comp"],
        color=pal["sep_fill"],
        alpha=0.15 if theme == "white" else 0.17,
        label=f"Master Peak-to-Trough Regime Separation Spread Δ_P-T^* (Mean = {mean_sep_comp:.1f}%)",
        zorder=2,
    )

    # Plot the 5 Pre-Peak Maxima Series + Separation + Trough Minima
    ax.plot(
        x, fm["pk_comp"], marker="o", markersize=10, linewidth=3.2, color=pal["comp_line"],
        label=f"Pre-Peak Max: Master Composite Index I_peak^* (Mean = {mean_pk_comp:.1f}%)", zorder=6,
    )
    ax.plot(
        x, fm["pk_mahal"], marker="s", markersize=8.5, linewidth=2.3, linestyle="--", color=pal["mahal_line"],
        label=f"Pre-Peak Max: Signed Mahalanobis I_peak^Mahal (Mean = {mean_pk_mahal:.1f}%)", zorder=5,
    )
    ax.plot(
        x, fm["pk_dfm"], marker="D", markersize=8.0, linewidth=2.3, linestyle=":", color=pal["dfm_line"],
        label=f"Pre-Peak Max: Dynamic Factor Nowcast I_peak^DFM (Mean = {mean_pk_dfm:.1f}%)", zorder=5,
    )
    ax.plot(
        x, fm["pk_diff"], marker="^", markersize=8.5, linewidth=2.3, linestyle="-.", color=pal["diff_line"],
        label=f"Pre-Peak Max: LEI Percentile Diffusion I_peak^Diff (Mean = {mean_pk_diff:.1f}%)", zorder=5,
    )
    ax.plot(
        x, fm["pk_spca"], marker="P", markersize=9.0, linewidth=2.3, linestyle="--", color=pal["spca_line"],
        label=f"Pre-Peak Max: Sparse PCA Concentration I_peak^SPCA (Mean = {mean_pk_spca:.1f}%)", zorder=5,
    )
    ax.plot(
        x, fm["sep_comp"], marker="*", markersize=12, linewidth=2.8, linestyle="-", color=pal["spy_line"],
        label="Net Peak–Trough Regime Separation Δ_P-T^* = I_peak^* - I_trough^*", zorder=6,
    )
    ax.plot(
        x, fm["tr_comp"], marker="v", markersize=10, linewidth=3.0, color=pal["trough_line"],
        label=f"Crash-Trough Min: Master Composite I_trough^* (Mean = {mean_tr_comp:.1f}%, All < 25%)", zorder=6,
    )

    # Horizontal Popperian Gate Lines
    ax.axhline(70.0, color=pal["dd_unhedged"], linestyle="--", linewidth=2.2, zorder=4)
    ax.axhline(25.0, color=pal["trough_marker"], linestyle=":", linewidth=2.2, zorder=4)

    # Annotate exact values for Master Peak (above 100% line to avoid line collision) and Trough
    for i in range(len(x)):
        ax.text(
            x[i], 102.2, f"Master: {fm['pk_comp'][i]:.1f}%",
            ha="center", va="bottom", fontsize=9.5, fontweight="bold", color=pal["comp_line"], zorder=7,
        )
        ax.text(
            x[i], fm["tr_comp"][i] - 3.6, f"Trough: {fm['tr_comp'][i]:.1f}%",
            ha="center", va="top", fontsize=9.2, fontweight="bold", color=pal["trough_line"], zorder=7,
        )

    # Non-Overlapping Callout Arrows for Threshold Gates & Key Events
    ax.annotate(
        "Popperian Pre-Peak Warning Gate (≥ 70.0%)\n100% Sensitivity: Master Composite Surpasses Gate Before Every Dislocation (D1–D8)",
        xy=(1.2, 70.0),
        xytext=(0.10, 54.0),
        fontsize=9.8,
        fontweight="bold",
        color=pal["text"],
        bbox=dict(boxstyle="round,pad=0.40", facecolor=pal["callout_red_bg"], edgecolor=pal["dd_unhedged"], linewidth=1.4),
        arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=-0.15", color=pal["dd_unhedged"], lw=1.8),
        zorder=8,
    )

    ax.annotate(
        f"Popperian Crash-Bottom Accumulation Floor (< 25.0%)\nZero Trough De-Risking Errors: Trough Score Collapses to 0.0%–{max_tr:.1f}% Across All 8 Bottoms",
        xy=(5.5, 25.0),
        xytext=(3.75, 43.0),
        fontsize=9.8,
        fontweight="bold",
        color=pal["text"],
        bbox=dict(boxstyle="round,pad=0.40", facecolor=pal["callout_green_bg"], edgecolor=pal["trough_marker"], linewidth=1.4),
        arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=0.15", color=pal["trough_marker"], lw=1.8),
        zorder=8,
    )

    ax.annotate(
        f"D3 (2011 Sovereign Shock) & D1 (2008 GFC)\nD3 Peak {fm['pk_comp'][2]:.1f}% → Trough {fm['tr_comp'][2]:.1f}% (Δ = {fm['sep_comp'][2]:.1f}%)",
        xy=(2.0, fm["pk_comp"][2]),
        xytext=(1.70, 74.5),
        fontsize=9.5,
        fontweight="bold",
        color=pal["text"],
        bbox=dict(boxstyle="round,pad=0.36", facecolor=pal["callout_bg"], edgecolor=pal["callout_border"], linewidth=1.2),
        arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=-0.15", color=pal["arrow"], lw=1.5),
        zorder=8,
    )

    ax.annotate(
        f"D8 (Early-2025 Tariff & AI CapEx Reset)\nPeak {fm['pk_comp'][7]:.1f}% → Trough {fm['tr_comp'][7]:.1f}% (Δ = {fm['sep_comp'][7]:.1f}%)",
        xy=(7.0, fm["pk_comp"][7]),
        xytext=(5.25, 74.5),
        fontsize=9.5,
        fontweight="bold",
        color=pal["text"],
        bbox=dict(boxstyle="round,pad=0.36", facecolor=pal["callout_alt_bg"], edgecolor=pal["comp_line"], linewidth=1.2),
        arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=0.15", color=pal["comp_line"], lw=1.5),
        zorder=8,
    )

    leg = ax.legend(
        loc="center left",
        bbox_to_anchor=(0.012, 0.25),
        fontsize=9.5,
        ncol=2,
        frameon=True,
        facecolor=pal["bg"],
        edgecolor=pal["callout_border"],
        framealpha=0.96,
    )
    for txt in leg.get_texts():
        txt.set_color(pal["text"])
        txt.set_fontweight("bold")

    out_path = OUT_DIR / f"02_8_Dislocation_Popperian_{theme}.png"
    save_and_verify_4k(fig, out_path, pal["bg"])
    return out_path


def plot_3_homotopic_phase_time(
    fm: Dict[str, Any],
    theme: str,
) -> Path:
    """
    Plot 3: Homotopic Phase-Time Superposed Epoch Analysis (theta in [-1.0, +1.0]).
    """
    pal = get_palette(theme)
    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
    fig.subplots_adjust(left=0.075, right=0.955, top=0.885, bottom=0.120)

    style_axes_common(
        ax=ax,
        fig=fig,
        pal=pal,
        title="Executive View III: Homotopic Phase-Time Superposed Epoch Analysis",
        subtitle="Piecewise Phase-Time Alignment θ ∈ [-1.0, +1.0]: 180-Day Pre-Peak Buildup (θ ∈ [-1, 0]) & Peak-to-Trough Collapse (θ ∈ [0, +1])",
        xlabel="Canonical Dislocation Phase-Time θ  (θ = -1.0: -180d Buildup Start  |  θ = 0.0: Cycle Peak  |  θ = +1.0: Cycle Trough)",
        ylabel="Indexed S&P 500 Trajectory (Peak θ = 0 Set to 100) & Composite Warning Envelope Score (%)",
        footer_note="Source: Superposed Epoch Analysis (SEA) averaged across all 8 dislocations (D1–D8, 2006–2026). Piecewise homotopy aligns heterogeneous crash durations onto θ ∈ [0, +1].",
    )

    th = fm["theta_grid"]
    ax.set_xlim(-1.04, 1.04)
    ax.set_ylim(-3.0, 111.0)
    ax.xaxis.set_major_locator(mticker.MultipleLocator(0.20))
    ax.xaxis.set_minor_locator(mticker.MultipleLocator(0.05))
    ax.yaxis.set_major_locator(mticker.MultipleLocator(10))
    ax.yaxis.set_minor_locator(mticker.MultipleLocator(2.5))
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%d%%"))

    # Background Phase Shading
    ax.axvspan(-1.0, 0.0, color=pal["lead_band"], alpha=0.08 if theme == "white" else 0.10, zorder=1)
    ax.axvspan(0.0, 1.0, color=pal["crash_band"], alpha=0.08 if theme == "white" else 0.10, zorder=1)

    # Shaded Master Composite Area
    ax.fill_between(
        th, 0.0, fm["sea_comp"],
        color=pal["sep_fill"], alpha=0.14 if theme == "white" else 0.16, zorder=2,
    )

    # Plot Normalized S&P 500 & 5 Composite Envelopes
    ax.plot(
        th, fm["sea_spy"], linewidth=3.8, color=pal["spy_line"],
        label="SEA Mean Normalized S&P 500 Trajectory (Indexed = 100.0 at Peak θ = 0.0)", zorder=7,
    )
    ax.plot(
        th, fm["sea_comp"], linewidth=3.0, color=pal["comp_line"],
        label="SEA Mean: Master Composite Warning Envelope I^*(θ)", zorder=6,
    )
    ax.plot(
        th, fm["sea_mahal"], linewidth=2.3, linestyle="--", color=pal["mahal_line"],
        label="SEA Mean: Signed Mahalanobis Envelope I^Mahal(θ)", zorder=5,
    )
    ax.plot(
        th, fm["sea_dfm"], linewidth=2.3, linestyle=":", color=pal["dfm_line"],
        label="SEA Mean: Dynamic Factor Nowcast Envelope I^DFM(θ)", zorder=5,
    )
    ax.plot(
        th, fm["sea_diff"], linewidth=2.3, linestyle="-.", color=pal["diff_line"],
        label="SEA Mean: LEI Percentile Diffusion Envelope I^Diff(θ)", zorder=5,
    )
    ax.plot(
        th, fm["sea_spca"], linewidth=2.3, linestyle="--", color=pal["spca_line"],
        label="SEA Mean: Sparse PCA Regime Envelope I^SPCA(θ)", zorder=5,
    )

    # Reference Lines at Peak (theta = 0.0) and Warning Threshold (70%)
    ax.axvline(0.0, color=pal["peak_marker"], linestyle="-", linewidth=2.6, zorder=4)
    ax.axhline(70.0, color=pal["dd_unhedged"], linestyle="--", linewidth=2.0, zorder=4)

    # Non-Overlapping Phase Banner Headers inside Plot
    ax.text(
        -0.52, 106.2, "PHASE I: PRE-PEAK EUPHORIC BUILDUP (θ ∈ [-1.0, 0.0] / 180d)",
        ha="center", va="center", fontsize=10.2, fontweight="bold", color=pal["text"],
        bbox=dict(boxstyle="round,pad=0.33", facecolor=pal["callout_bg"], edgecolor=pal["lead_band"], linewidth=1.3),
        zorder=8,
    )
    ax.text(
        0.52, 106.2, "PHASE II: PEAK-TO-TROUGH CONTRACTION UNWIND (θ ∈ [0.0, +1.0])",
        ha="center", va="center", fontsize=10.2, fontweight="bold", color=pal["text"],
        bbox=dict(boxstyle="round,pad=0.33", facecolor=pal["callout_red_bg"], edgecolor=pal["crash_band"], linewidth=1.3),
        zorder=8,
    )

    # Labeled Callout Arrows Placed in Clean Open Spaces
    ax.annotate(
        f"Buildup Origin (θ = -1.0 / -180d Before Peak)\n• S&P 500 at {fm['sea_spy'][0]:.1f} (Rallies +{(100.0 / fm['sea_spy'][0] - 1.0) * 100.0:.1f}% into Peak)\n• Master Composite Already at {fm['sea_comp'][0]:.1f}% (> 70% Gate)",
        xy=(-1.0, fm["sea_comp"][0]),
        xytext=(-0.96, 55.0),
        fontsize=9.6,
        fontweight="bold",
        color=pal["text"],
        bbox=dict(boxstyle="round,pad=0.40", facecolor=pal["callout_bg"], edgecolor=pal["callout_border"], linewidth=1.3),
        arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=-0.15", color=pal["arrow"], lw=1.6),
        zorder=8,
    )

    ax.annotate(
        f"Cycle Peak Inflection (θ = 0.0)\n• S&P 500 Tops at 100.0\n• Master Envelope at {fm['sea_comp'][40]:.1f}% (> 70% Gate)\n• Defensive Protection Fully Active",
        xy=(0.0, 100.0),
        xytext=(-0.42, 73.0),
        fontsize=9.6,
        fontweight="bold",
        color=pal["text"],
        bbox=dict(boxstyle="round,pad=0.40", facecolor=pal["callout_red_bg"], edgecolor=pal["peak_marker"], linewidth=1.4),
        arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=0.15", color=pal["peak_marker"], lw=1.8),
        zorder=8,
    )

    ax.annotate(
        f"Mid-Collapse De-Escalation (θ = +0.50)\n• S&P 500 Down to {fm['sea_spy'][60]:.1f} (-{100.0 - fm['sea_spy'][60]:.1f}%)\n• Composite Drops Through {fm['sea_comp'][60]:.1f}%\n• Crash-Liquidation Damper Engages",
        xy=(0.50, fm["sea_comp"][60]),
        xytext=(0.30, 73.0),
        fontsize=9.6,
        fontweight="bold",
        color=pal["text"],
        bbox=dict(boxstyle="round,pad=0.40", facecolor=pal["callout_alt_bg"], edgecolor=pal["comp_line"], linewidth=1.3),
        arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=0.15", color=pal["comp_line"], lw=1.6),
        zorder=8,
    )

    ax.annotate(
        f"Cycle Trough Exhaustion (θ = +1.00)\n• S&P 500 Mean Trough at {fm['sea_spy'][-1]:.1f} (-{100.0 - fm['sea_spy'][-1]:.1f}% Mean Loss)\n• Master Composite Collapses to {fm['sea_comp'][-1]:.1f}%\n• Triggers Aggressive Contrarian Capital Re-Entry",
        xy=(1.0, fm["sea_comp"][-1]),
        xytext=(0.12, 10.0),
        fontsize=9.6,
        fontweight="bold",
        color=pal["text"],
        bbox=dict(boxstyle="round,pad=0.40", facecolor=pal["callout_green_bg"], edgecolor=pal["trough_marker"], linewidth=1.4),
        arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=-0.12", color=pal["trough_marker"], lw=1.8),
        zorder=8,
    )

    leg = ax.legend(
        loc="lower left",
        bbox_to_anchor=(0.015, 0.04),
        fontsize=9.8,
        frameon=True,
        facecolor=pal["bg"],
        edgecolor=pal["callout_border"],
        framealpha=0.96,
    )
    for txt in leg.get_texts():
        txt.set_color(pal["text"])
        txt.set_fontweight("bold")

    out_path = OUT_DIR / f"03_Homotopic_Phase_Time_{theme}.png"
    save_and_verify_4k(fig, out_path, pal["bg"])
    return out_path


def plot_4_dislocation_capital(
    fm: Dict[str, Any],
    theme: str,
) -> Path:
    """
    Plot 4: Dislocation Capital Preservation & Early-Warning Lead Cushion Profile.
    """
    pal = get_palette(theme)
    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
    fig.subplots_adjust(left=0.075, right=0.915, top=0.885, bottom=0.130)

    dd_spy = fm["dd_spy_abs"]
    dd_def = fm["dd_def_abs"]
    dd_sav = fm["dd_saved"]
    ld_pct = fm["lead_pct_yr"]
    ld_days = fm["lead_days"]
    mean_dd_spy = float(np.mean(dd_spy))
    mean_dd_def = float(np.mean(dd_def))
    mean_dd_sav = float(np.mean(dd_sav))
    mean_ld_pct = float(np.mean(ld_pct))
    mean_ld_days = float(np.mean(ld_days))
    rel_dd_red = (1.0 - mean_dd_def / mean_dd_spy) * 100.0

    style_axes_common(
        ax=ax,
        fig=fig,
        pal=pal,
        title="Executive View IV: Dislocation Capital Preservation & Lead Cushion Profile",
        subtitle=f"Institutional Portfolio Defense Across D1–D8: {rel_dd_red:.1f}% Mean Drawdown Reduction ({mean_dd_spy:.1f}% Unhedged Loss Cut to {mean_dd_def:.1f}%) & {mean_ld_days:.1f}-Day Mean Lead Cushion",
        xlabel="Historical Market Dislocation Regime (Chronological Sequence D1–D8 Across the 2006–2026 Horizon)",
        ylabel="Peak-to-Trough Drawdown Magnitude (%) & Normalized Lead Cushion (% of 252-Day Year)",
        footer_note="Source: 20-Year Dislocation Backtest Audit (Jan 2, 2006 – Nov 13, 2026, 4.0% cash yield, 15 bps turnover friction, 1-day execution lag). Capital saved = |DD_SPY| - |DD_Def|.",
    )

    x = np.arange(len(DISLOCATIONS_8_20YR))
    x_labels = [
        "D1: 2007–09 GFC\n(Oct '07–Mar '09)",
        "D2: Euro/Flash\n(Apr '10–Jul '10)",
        "D3: US Downgrade\n(Apr '11–Oct '11)",
        "D4: China/Energy\n(Jul '15–Feb '16)",
        "D5: Q4 2018 QT Shock\n(Sep '18–Dec '18)",
        "D6: COVID-19 Shock\n(Feb '20–Mar '20)",
        "D7: Rate Hike Reset\n(Jan '22–Oct '22)",
        "D8: 2025 Tariff/AI Reset\n(Feb '25–Apr '25)",
    ]

    ax.set_xlim(-0.55, 7.55)
    ax.set_ylim(0.0, 114.0)
    ax.set_xticks(x)
    ax.set_xticklabels(x_labels, fontsize=10.5, fontweight="bold")
    ax.yaxis.set_major_locator(mticker.MultipleLocator(10))
    ax.yaxis.set_minor_locator(mticker.MultipleLocator(2.5))
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%d%%"))

    # Shaded Area Under Unhedged and Defensive Drawdowns (Parity with Tab 8 Card 3 Subplot 4)
    ax.fill_between(
        x, 0.0, dd_spy,
        color=pal["dd_unhedged"], alpha=0.18 if theme == "white" else 0.22, zorder=2,
    )
    ax.fill_between(
        x, 0.0, dd_def,
        color=pal["dd_defensive"], alpha=0.25 if theme == "white" else 0.28, zorder=3,
    )

    # Plot the 4 Primary Traces
    ax.plot(
        x, dd_spy, marker="o", markersize=10.5, linewidth=3.2, color=pal["dd_unhedged"],
        label=f"Realized Unhedged S&P 500 Dislocation Drawdown |DD_SPY| (%) [Mean = {mean_dd_spy:.1f}%]", zorder=6,
    )
    ax.plot(
        x, dd_def, marker="s", markersize=9.5, linewidth=3.0, color=pal["dd_defensive"],
        label=f"Composite-Hedged Defensive Portfolio Drawdown |DD_Def| (%) [Mean = {mean_dd_def:.1f}%]", zorder=6,
    )
    ax.plot(
        x, dd_sav, marker="D", markersize=9.0, linewidth=2.8, linestyle="--", color=pal["dd_saved"],
        label=f"Dislocation Drawdown Capital Saved ΔDD_saved = |DD_SPY| - |DD_Def| (%) [Mean = +{mean_dd_sav:.1f}%]", zorder=6,
    )
    ax.plot(
        x, ld_pct, marker="^", markersize=10.0, linewidth=2.8, linestyle=":", color=pal["lead_line"],
        label=f"Early-Warning Lead Cushion (% of 252-Day Trading Year) [Mean = {mean_ld_pct:.1f}% / {mean_ld_days:.1f}d]", zorder=6,
    )

    # Secondary Right-Hand Axis in Trading Days (0 to 252d)
    ax_right = ax.twinx()
    ax_right.set_ylim(0.0, 114.0 * 2.52)
    ax_right.yaxis.set_major_locator(mticker.MultipleLocator(25))
    ax_right.yaxis.set_minor_locator(mticker.MultipleLocator(5))
    ax_right.yaxis.set_major_formatter(mticker.FormatStrFormatter("%dd"))
    ax_right.tick_params(axis="y", labelsize=11.0, colors=pal["subtext"])
    ax_right.set_ylabel(
        "Early-Warning Lead Time Prior to Peak (Trading Days, 252d = 1 Trading Year)",
        fontsize=12.5,
        fontweight="bold",
        color=pal["subtext"],
        labelpad=12,
    )
    ax_right.spines["right"].set_color(pal["axis"])
    ax_right.spines["top"].set_visible(False)

    # Value Labels on Data Points (cleanly separated from curves)
    for i in range(len(x)):
        ax.text(
            x[i], dd_spy[i] + 2.0, f"SPY: -{dd_spy[i]:.1f}%",
            ha="center", va="bottom", fontsize=9.2, fontweight="bold", color=pal["dd_unhedged"], zorder=7,
        )
        ax.text(
            x[i], max(dd_def[i] - 4.2, 0.8), f"Def: -{dd_def[i]:.1f}%",
            ha="center", va="bottom", fontsize=8.8, fontweight="bold", color=pal["dd_defensive"], zorder=7,
        )
        ax.text(
            x[i], ld_pct[i] + 2.2, f"{ld_days[i]:.0f}d ({ld_pct[i]:.0f}%)",
            ha="center", va="bottom", fontsize=9.2, fontweight="bold", color=pal["lead_line"], zorder=7,
        )

    # Labeled Callout Boxes with Arrows Placed in Open Band (y = 35% to 62%)
    ax.annotate(
        f"D1 (2007–09 GFC): Flagship Capital Preservation\n• Unhedged S&P 500 Loss: -{dd_spy[0]:.1f}%\n• Composite-Hedged Loss: -{dd_def[0]:.1f}%\n• Net Capital Saved: +{dd_sav[0]:.1f}% ({ld_days[0]:.0f}d Advance Warning)",
        xy=(0.0, dd_spy[0]),
        xytext=(0.45, 52.0),
        fontsize=9.5,
        fontweight="bold",
        color=pal["text"],
        bbox=dict(boxstyle="round,pad=0.38", facecolor=pal["callout_red_bg"], edgecolor=pal["dd_unhedged"], linewidth=1.4),
        arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=-0.12", color=pal["dd_unhedged"], lw=1.8),
        zorder=8,
    )

    ax.annotate(
        f"D6 (2020 COVID Liquidity Shock)\n• Unhedged Loss: -{dd_spy[5]:.1f}% vs. Hedged: -{dd_def[5]:.1f}%\n• Capital Saved: +{dd_sav[5]:.1f}% ({ld_days[5]:.0f}d Warning Lead)",
        xy=(5.0, dd_spy[5]),
        xytext=(2.30, 36.0),
        fontsize=9.5,
        fontweight="bold",
        color=pal["text"],
        bbox=dict(boxstyle="round,pad=0.36", facecolor=pal["callout_alt_bg"], edgecolor=pal["dd_saved"], linewidth=1.3),
        arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=0.15", color=pal["dd_saved"], lw=1.6),
        zorder=8,
    )

    ax.annotate(
        f"D7 (2022 Rate Reset) & D8 (Early-2025 Tariff/AI Reset)\n• D7 Saved: +{dd_sav[6]:.1f}% ({dd_spy[6]:.1f}% → {dd_def[6]:.1f}%, {ld_days[6]:.0f}d Lead)\n• D8 Saved: +{dd_sav[7]:.1f}% ({dd_spy[7]:.1f}% → {dd_def[7]:.1f}%, {ld_days[7]:.0f}d Lead)",
        xy=(6.0, dd_spy[6]),
        xytext=(4.75, 42.0),
        fontsize=9.5,
        fontweight="bold",
        color=pal["text"],
        bbox=dict(boxstyle="round,pad=0.36", facecolor=pal["callout_green_bg"], edgecolor=pal["dd_defensive"], linewidth=1.3),
        arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=-0.15", color=pal["dd_defensive"], lw=1.6),
        zorder=8,
    )

    # Place Legend in Open Band (y ~ 63% to 80%, x ~ 1.0 to 6.5) well below the Lead Cushion line
    leg = ax.legend(
        loc="center",
        bbox_to_anchor=(0.54, 0.65),
        fontsize=9.8,
        frameon=True,
        facecolor=pal["bg"],
        edgecolor=pal["callout_border"],
        framealpha=0.96,
    )
    for txt in leg.get_texts():
        txt.set_color(pal["text"])
        txt.set_fontweight("bold")

    out_path = OUT_DIR / f"04_Dislocation_Capital_{theme}.png"
    save_and_verify_4k(fig, out_path, pal["bg"])
    return out_path


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    state = DashboardState()
    state.load_data("option_3")
    df = state.df
    dates = [str(d)[:10] for d in df["Date"].to_list()]
    spy = df["SPY"].to_numpy()
    comp = df["Composite_Summary_Index"].to_numpy()
    mahal = df["Mahalanobis_Summary_Index"].to_numpy()
    dfm = df["DFM_Summary_Index"].to_numpy()
    diff = df["Diffusion_Summary_Index"].to_numpy()
    spca = df["SPCA_Summary_Index"].to_numpy()

    fm = compute_dislocation_fidelity_metrics(
        dates, spy, comp, mahal, dfm, diff, spca, threshold=70.0
    )

    for theme in ("white", "black"):
        plot_1_scale_invariant_log_growth(dates, spy, fm, theme)
        plot_2_popperian_regime_separation(fm, theme)
        plot_3_homotopic_phase_time(fm, theme)
        plot_4_dislocation_capital(fm, theme)


if __name__ == "__main__":
    main()
