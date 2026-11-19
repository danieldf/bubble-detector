#!/usr/bin/env python3
"""
High-Resolution 4K HUXGA (6400 x 4800, 4:3 Aspect Ratio) Visualization Suite
for `SectorDislocation_TechnicalReport.md` (v1.1.0).

Generates 18 publication-grade 4K HUXGA (6400 x 4800) PNGs (9 figures x 2 themes: pure white & pure black):
  1. `01_Sleeve_Taxonomy_Pareto_Frontier_{white,black}.png`
  2. `02_Flagship_Sector_Dislocation_Trajectories_{white,black}.png`
  3. `03_12_Event_Sector_Popperian_Matrix_{white,black}.png`
  4. `04_Sector_ETFs_vs_Single_Stocks_Granularity_{white,black}.png`
  5. `05_Signal_Mapping_Portfolio_Wealth_Drawdown_{white,black}.png`
  6. `06_Sector_8Pillar_Coalition_Anatomy_{white,black}.png`
  7. `07_Sector_5Engines_Homotopic_SEA_{white,black}.png`
  8. `08_6Sleeve_vs_7Sleeve_XLY_Diagnostic_{white,black}.png`
  9. `09_20Yr_Cross_Sector_Regime_Thermogram_{white,black}.png`

Author: Daniel D Ferrante, PhD | Date: November 18, 2026
License: CC-BY-NC-ND 4.0 | Classification: CONFIDENTIAL — PROPRIETARY IP
"""

from __future__ import annotations

import json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
import pandas as pd
from PIL import Image

STUDY_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = STUDY_DIR / "data"
PLOTS_DIR = STUDY_DIR

# Exact 4K HUXGA (6400 x 4800) at 4:3 Aspect Ratio
TARGET_W = 6400
TARGET_H = 4800
DPI = 400
FIGSIZE = (TARGET_W / DPI, TARGET_H / DPI)  # (16.0, 12.0) -> exact 6400 x 4800 px


def get_palette(theme: str) -> dict[str, str]:
    if theme == "white":
        return {
            "bg": "#FFFFFF",
            "panel": "#F8FAFC",
            "text": "#0F172A",
            "sub": "#334155",
            "axis": "#1E293B",
            "grid": "#CBD5E1",
            "grid_minor": "#E2E8F0",
            "blue": "#0052CC",
            "cyan": "#0284C7",
            "emerald": "#059669",
            "amber": "#D97706",
            "crimson": "#DC2626",
            "purple": "#7E22CE",
            "teal": "#0D9488",
            "pink": "#DB2777",
            "slate": "#475569",
            "card": "#FFFBEB",
            "card_blue": "#EFF6FF",
            "card_green": "#ECFDF5",
            "card_red": "#FEF2F2",
            "border": "#0F172A",
            "badge_bg": "#0F172A",
            "badge_fg": "#FFFFFF",
        }
    return {
        "bg": "#000000",
        "panel": "#090D16",
        "text": "#F8FAFC",
        "sub": "#CBD5E1",
        "axis": "#E2E8F0",
        "grid": "#334155",
        "grid_minor": "#1E293B",
        "blue": "#38BDF8",
        "cyan": "#00E5FF",
        "emerald": "#06D6A0",
        "amber": "#FFD166",
        "crimson": "#FF4D6D",
        "purple": "#C77DFF",
        "teal": "#2DD4BF",
        "pink": "#F472B6",
        "slate": "#94A3B8",
        "card": "#111827",
        "card_blue": "#0F172A",
        "card_green": "#0D1F1A",
        "card_red": "#1F1218",
        "border": "#94A3B8",
        "badge_bg": "#1E293B",
        "badge_fg": "#38BDF8",
    }


def add_header_footer(fig: plt.Figure, pal: dict[str, str], title: str, subtitle: str, footer: str) -> None:
    fig.patch.set_facecolor(pal["bg"])
    fig.text(0.035, 0.969, title, fontsize=11.5, fontweight="bold", color=pal["text"], ha="left", va="top")
    fig.text(0.035, 0.943, subtitle, fontsize=9.0, color=pal["sub"], ha="left", va="top")
    fig.text(
        0.965, 0.969,
        "CONFIDENTIAL  |  CC-BY-NC-ND 4.0  |  Daniel D Ferrante, PhD",
        fontsize=8.0, fontweight="bold", color=pal["badge_fg"], ha="right", va="top",
        bbox=dict(boxstyle="round,pad=0.32", facecolor=pal["badge_bg"], edgecolor=pal["border"], lw=0.8),
    )
    fig.text(0.035, 0.013, footer, fontsize=7.4, color=pal["sub"], ha="left", va="bottom", style="italic")
    fig.text(0.965, 0.013, "4K HUXGA (6400 × 4800, 4:3)  •  Horizon: 2006-01-02 – 2026-11-13 (N = 5,445)",
             fontsize=7.6, fontweight="bold", color=pal["sub"], ha="right", va="bottom")


def style_ax(ax: plt.Axes, pal: dict[str, str]) -> None:
    ax.set_facecolor(pal["panel"])
    for sp in ax.spines.values():
        sp.set_color(pal["axis"])
        sp.set_linewidth(0.9)
    ax.tick_params(colors=pal["text"], labelsize=8.5)
    ax.grid(True, which="major", color=pal["grid"], lw=0.65, alpha=0.75)
    ax.grid(True, which="minor", color=pal["grid_minor"], lw=0.4, alpha=0.5)


def save_exact_huxga(fig: plt.Figure, out_path: Path, bg_color: str) -> None:
    fig.savefig(out_path, dpi=DPI, facecolor=bg_color, bbox_inches=None)
    plt.close(fig)
    im = Image.open(out_path)
    assert im.size == (TARGET_W, TARGET_H), f"Expected {(TARGET_W, TARGET_H)}, got {im.size}"


def smooth_envelope(sc_raw: np.ndarray) -> np.ndarray:
    return (
        0.45 * pd.Series(sc_raw).rolling(63, min_periods=1).max().ewm(span=15).mean().to_numpy()
        + 0.55 * pd.Series(sc_raw).ewm(span=32).mean().to_numpy()
    )


# ==============================================================================
# FIGURE 1: Taxonomy Pareto Frontier & Dual Co-Primary Basis Audit (S_6^⊥ & T5)
# ==============================================================================
def plot_01_taxonomy_pareto(art: dict, df_m: pd.DataFrame, theme: str) -> None:
    pal = get_palette(theme)
    fig = plt.figure(figsize=FIGSIZE, dpi=DPI)
    gs = fig.add_gridspec(2, 2, left=0.055, right=0.965, top=0.895, bottom=0.068, hspace=0.31, wspace=0.22)

    add_header_footer(
        fig, pal,
        "Figure 1: Cross-Sectional Sleeve Dimensionality & Co-Primary Basis Audit (S_6^⊥ 6-Sleeve vs. T5 7-Sleeve)",
        "Empirical Proof Under the Mandatory >= 0.87 Gate: Why Both S_6^⊥ (K = 6 Parsimony Core) and T5 (K = 7 Granular Factor) Pass Co-Optimally",
        "Authentic GICS-11 Select Sector SPDR ETFs & SPY (1999–2026 causal warm-up; 2006–2026 out-of-sample audit, N = 5,445).",
    )

    ax1 = fig.add_subplot(gs[0, 0])
    style_ax(ax1, pal)
    ks = np.array([3, 4, 5, 6, 7, 11])
    x_pos = np.arange(len(ks))
    r2_1d = [0.8183, 0.8666, 0.8990, 0.9272, 0.9421, 1.0000]
    r2_21d = [0.8349, 0.8909, 0.9131, 0.9357, 0.9516, 1.0000]
    r2_dd = [0.8132, 0.9380, 0.9629, 0.9744, 0.9820, 1.0000]
    tau_unorth = [0.6483, 0.4817, 0.4013, 0.4473, 0.4414, 0.4068]
    tau_orth = [0.9976, 0.9968, 0.9931, 0.9953, 0.9936, 0.9904]

    ax1.axvspan(2.68, 4.32, color=pal["emerald"], alpha=0.14, label="Co-Primary Pareto Zone: K=6 (S_6^⊥) & K=7 (T5)")
    ax1.axhline(0.87, color=pal["crimson"], lw=2.2, ls="--", label="Mandatory 0.87 Confidence / Tolerance Cutoff")
    ax1.plot(x_pos, r2_dd, "o-", color=pal["emerald"], lw=2.4, ms=7, label="11-Sector Drawdown Spanning R²_DD")
    ax1.plot(x_pos, r2_21d, "s-", color=pal["blue"], lw=2.2, ms=6.5, label="21-Day Regime Return Spanning R²_21d")
    ax1.plot(x_pos, r2_1d, "^-", color=pal["amber"], lw=2.2, ms=6.5, label="1-Day Return Variance Spanning R²_1d")
    ax1.plot(x_pos, tau_orth, "D-", color=pal["purple"], lw=2.0, ms=6, label="Post-Gram-Schmidt Min Tolerance τ_min^⊥")
    ax1.plot(x_pos, tau_unorth, "x--", color=pal["slate"], lw=1.8, ms=7, label="Unorthogonalized Beta-Adj τ_min (< 0.87 FAIL)")

    ax1.set_xticks(x_pos)
    ax1.set_xticklabels([
        "K=3 (T1)\nMacro\n[FAIL R²]",
        "K=4 (T2)\nRegime\n[FAIL R²_1d]",
        "K=5 (T3)\nFactor\n[Blurs REIT]",
        "K=6* (S_6^⊥)\nParsimony Opt\n[CO-PRIMARY]",
        "K=7* (T5)\nGranular XLY\n[CO-PRIMARY]",
        "K=11 (T6)\nRaw GICS\n[FAIL VIF]",
    ], fontsize=7.9, fontweight="bold")
    ax1.set_ylim(0.32, 1.05)
    ax1.set_ylabel("Information / Spanning / Tolerance Score [0, 1]", fontsize=9.3, fontweight="bold", color=pal["text"])
    ax1.set_title("A. Taxonomy Dimensionality Frontier: Co-Primary K=6 (S_6^⊥) & K=7 (T5)", fontsize=10.4, fontweight="bold", color=pal["text"], pad=8)
    ax1.legend(loc="lower right", fontsize=7.3, framealpha=0.92, facecolor=pal["bg"], edgecolor=pal["grid"], labelcolor=pal["text"])

    ax1.annotate(
        "Co-Primary Winners (≥ 0.87):\n• S_6^⊥ (K=6): R²_1d=0.927, R²_DD=0.974, τ_min^⊥=0.995\n• T5 (K=7, XLY Split): R²_1d=0.942, R²_DD=0.982, τ_min^⊥=0.994",
        xy=(3.5, 0.935), xytext=(0.15, 0.56),
        fontsize=7.7, fontweight="bold", color=pal["text"],
        bbox=dict(boxstyle="round,pad=0.38", facecolor=pal["card_green"], edgecolor=pal["emerald"], lw=1.2),
        arrowprops=dict(arrowstyle="->", color=pal["emerald"], lw=1.6),
    )

    ax2 = fig.add_subplot(gs[0, 1])
    style_ax(ax2, pal)
    gics_11 = ["XLK", "XLC", "XLY", "XLI", "XLB", "XLF", "XLE", "XLV", "XLP", "XLU", "XLRE"]
    mask20 = (df_m.index >= "2006-01-02") & (df_m.index <= "2026-11-13")
    rets11 = pd.DataFrame({c: np.log(df_m[c] / df_m[c].shift(1)).fillna(0.0) for c in gics_11}).loc[mask20]
    corr11 = rets11.corr().to_numpy()
    im = ax2.imshow(corr11, cmap="RdYlBu_r", vmin=0.25, vmax=1.0, aspect="auto")
    ax2.grid(False)
    ax2.set_xticks(range(11))
    ax2.set_yticks(range(11))
    ax2.set_xticklabels(gics_11, rotation=40, ha="right", fontsize=8.2, fontweight="bold")
    ax2.set_yticklabels(gics_11, fontsize=8.2, fontweight="bold")
    for i in range(11):
        for j in range(11):
            val = corr11[i, j]
            txt_c = "#FFFFFF" if (val > 0.72 or val < 0.38) else "#0F172A"
            ax2.text(j, i, f"{val:.2f}", ha="center", va="center", fontsize=6.9, fontweight="bold", color=txt_c)
    cbar = fig.colorbar(im, ax=ax2, fraction=0.042, pad=0.025)
    cbar.ax.tick_params(labelsize=8.0, colors=pal["text"])
    ax2.set_title("B. Raw GICS-11 Return Correlation Matrix (η_spec = 0.329, τ_min = 0.155 < 0.87 — FAIL)",
                  fontsize=10.2, fontweight="bold", color=pal["text"], pad=8)

    ax3 = fig.add_subplot(gs[1, 0])
    style_ax(ax3, pal)
    pcs = ["PC1\n(Growth/Def)", "PC2\n(Energy/Infl)", "PC3\n(Credit/Rate)", "PC4\n(CapEx/Ind)", "PC5\n(Yield/REIT)", "PC6/PC7\n(Consumer/Res)"]
    raw_pca_flips = [22, 76, 96, 107, 120, 128]
    xp = np.arange(len(pcs))
    bars = ax3.bar(xp - 0.18, raw_pca_flips, width=0.36, color=pal["crimson"], alpha=0.88, label="Unconstrained Rolling 252d PCA (459 Total Sign Flips — DROPPED)")
    ax3.bar(xp + 0.18, [1.5] * 6, width=0.36, color=pal["emerald"], alpha=0.92, label="Structurally-Anchored S_6^⊥ & T5 Eigen-Sleeves (0 Sign Flips — RETAINED)")
    ax3.axhline(247 * 0.13, color=pal["amber"], ls="--", lw=1.6, label="Max Allowable Instability Ceiling (1 - 0.87 = 13% Flip Rate = 32 Steps)")
    for b, v in zip(bars, raw_pca_flips):
        ax3.text(b.get_x() + b.get_width() / 2, v + 3, f"{v} flips\n({v / 247 * 100:.0f}%)", ha="center", va="bottom", fontsize=7.5, fontweight="bold", color=pal["text"])
    for idx_b in xp:
        ax3.text(idx_b + 0.18, 4.0, "0 flips", ha="center", va="bottom", fontsize=7.5, fontweight="bold", color=pal["emerald"])
    ax3.set_xticks(xp)
    ax3.set_xticklabels(pcs, fontsize=8.0)
    ax3.set_ylim(0, 154)
    ax3.set_ylabel("Sign Inversions Across 247 Rolling 21d Steps", fontsize=9.2, fontweight="bold", color=pal["text"])
    ax3.set_title("C. Why Pure Unconstrained Factor PCA Fails: Rotational Sign Indeterminacy", fontsize=10.3, fontweight="bold", color=pal["text"], pad=8)
    ax3.legend(loc="upper left", fontsize=7.4, framealpha=0.92, facecolor=pal["bg"], edgecolor=pal["grid"], labelcolor=pal["text"])

    ax4 = fig.add_subplot(gs[1, 1])
    style_ax(ax4, pal)
    pa6 = art["pillar_audit_6sleeves"]
    pa7 = art["pillar_audit_7sleeves"]
    # Show S6-S1 Merged alongside all 7 sleeves of T5 (which includes the 5 shared sleeves!)
    combined_rows = [pa6[0]] + pa7
    s_names = [
        "S6-S1\nMerged\n(XLK/XLC/XLY)",
        "T5-S1\nCompute\n(XLK/XLC)",
        "T5-S2\nConsumer\n(XLY Solo)",
        "S2 / T5-S3\nIndustrials\n(XLI/XLB)",
        "S3 / T5-S4\nEnergy\n(XLE)",
        "S4 / T5-S5\nFinancials\n(XLF)",
        "S5 / T5-S6\nREIT/Util\n(XLRE/XLU)",
        "S6 / T5-S7\nDefensive\n(XLV/XLP)",
    ]
    t_mins = [r["tau_min"] for r in combined_rows]
    t_means = [r["tau_mean"] for r in combined_rows]
    etas = [r["eta_spec"] for r in combined_rows]
    xs = np.arange(len(s_names))
    w_bar = 0.25
    ax4.axvspan(0.52, 2.48, color=pal["cyan"], alpha=0.11, label="T5 Granular Split of S1 → (XLK/XLC) + (XLY)")
    b1 = ax4.bar(xs - w_bar, t_mins, width=w_bar, color=pal["blue"], label="Min Pillar Tolerance τ_min = min(1/VIF_j)")
    ax4.bar(xs, t_means, width=w_bar, color=pal["teal"], label="Mean Pillar Tolerance τ̄ (8 Orthogonal Pillars)")
    ax4.bar(xs + w_bar, etas, width=w_bar, color=pal["emerald"], label="Spectral Rank Efficiency η_spec = erank(R)/8")
    ax4.axhline(0.87, color=pal["crimson"], lw=2.2, ls="--", label="Mandatory 0.87 Cutoff (100% Pass: 48/48 & 56/56)")
    for b in b1:
        ax4.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.004, f"{b.get_height():.3f}", ha="center", va="bottom", fontsize=6.6, fontweight="bold", color=pal["text"])
    ax4.set_xticks(xs)
    ax4.set_xticklabels(s_names, fontsize=7.0, fontweight="bold")
    ax4.set_ylim(0.82, 1.028)
    ax4.set_ylabel("Orthogonal Information Metric [0, 1]", fontsize=9.2, fontweight="bold", color=pal["text"])
    ax4.set_title("D. 8-Pillar Basis Verification Across Both S_6^⊥ (48 Pillars) & T5 (56 Pillars)", fontsize=10.2, fontweight="bold", color=pal["text"], pad=8)
    ax4.legend(loc="lower right", fontsize=7.1, framealpha=0.92, facecolor=pal["bg"], edgecolor=pal["grid"], labelcolor=pal["text"])

    save_exact_huxga(fig, PLOTS_DIR / f"01_Sleeve_Taxonomy_Pareto_Frontier_{theme}.png", pal["bg"])


# ==============================================================================
# FIGURE 2: Flagship Multi-Sector Trajectories (XLK, XLI, XLE, XLF)
# ==============================================================================
def plot_02_flagship_trajectories(df_ts: pd.DataFrame, art: dict, theme: str) -> None:
    pal = get_palette(theme)
    fig = plt.figure(figsize=FIGSIZE, dpi=DPI)
    gs = fig.add_gridspec(4, 1, left=0.062, right=0.928, top=0.895, bottom=0.060, hspace=0.26)

    add_header_footer(
        fig, pal,
        "Figure 2: Multi-Sector Log-Growth & Smooth Causal Dislocation Envelope I_{k,t}^{Sec*} (2006–2026)",
        "Synchronized Out-of-Sample Trajectories Across Information Technology (XLK), Industrials (XLI), Energy (XLE), and Financials (XLF)",
        "Left Y1: L_k(t) = 100×[1 + ln(P_{k,t}/P_{k,0})]  |  Right Y2: Smooth Causal Sector Warning Envelope (%). Amber = Pre-Peak Warning; Crimson = Crash.",
    )

    events_by_sec: dict[str, list[dict]] = {}
    for ev in art["event_study_12"]:
        events_by_sec.setdefault(ev["sector"], []).append(ev)

    configs = [
        ("XLK", "A. Information Technology (XLK) — Capturing 2018 Cloud/QT (SD07), 2022 ZIRP Tech Reset (SD09: -33.6%), & 2025 AI CapEx Reset (SD12: -25.7%)", pal["blue"]),
        ("XLI", "B. Industrials (XLI) — Capturing 2011 CapEx Freeze (SD03: -25.8%), 2018 Tariff/QT Break (SD06: -23.8%), & 2020 COVID Lock-Stop (SD08: -42.3%)", pal["purple"]),
        ("XLE", "C. Energy (XLE) — Capturing 2008 $147 Oil Spike (SD02: -57.4%), 2014–16 Shale Bust (SD04: -46.7%), & 2022 Anti-Bubble Exemption (+64.3% Gain!)", pal["amber"]),
        ("XLF", "D. Financials (XLF) — Capturing 2007–09 GFC Banking Collapse (SD01: -82.7%, 157d Lead) & 2022–23 Rate/SVB Contagion (SD11: -25.8%, 252d Lead)", pal["teal"]),
    ]

    dates = df_ts.index
    for idx, (sec, sub_t, col_line) in enumerate(configs):
        ax = fig.add_subplot(gs[idx, 0])
        style_ax(ax, pal)
        ax2 = ax.twinx()

        px = df_ts[f"SecPrice_{sec}"].to_numpy()
        log_idx = 100.0 * (1.0 + np.log(px / px[0]))
        sc_env = smooth_envelope(df_ts[f"SecScore_{sec}"].to_numpy())

        for ev in events_by_sec.get(sec, []):
            pk = pd.Timestamp(ev["peak"])
            tr = pd.Timestamp(ev["trough"])
            pre_start = pk - pd.Timedelta(days=int(max(ev["lead_252d"], 35) * 1.42))
            ax.axvspan(max(dates[0], pre_start), pk, color=pal["amber"], alpha=0.18, zorder=1)
            ax.axvspan(pk, tr, color=pal["crimson"], alpha=0.22, zorder=1)
            pk_i = dates.get_indexer([pk], method="nearest")[0]
            tr_i = dates.get_indexer([tr], method="nearest")[0]
            ax.scatter([dates[pk_i]], [log_idx[pk_i]], marker="v", s=58, color=pal["crimson"], edgecolor=pal["bg"], lw=0.7, zorder=6)
            ax.scatter([dates[tr_i]], [log_idx[tr_i]], marker="^", s=58, color=pal["emerald"], edgecolor=pal["bg"], lw=0.7, zorder=6)
            ax.annotate(
                f"{ev['id']} ({ev['dd_pct']:.0f}%)\nPk:{ev['sec_pre_max']:.0f}% | Ld:{ev['lead_252d']}d",
                xy=(dates[pk_i], log_idx[pk_i]),
                xytext=(0, 9 if idx != 3 else 7), textcoords="offset points",
                fontsize=7.0, fontweight="bold", color=pal["text"], ha="center",
                bbox=dict(boxstyle="round,pad=0.2", facecolor=pal["card"], edgecolor=pal["axis"], lw=0.6, alpha=0.94),
                zorder=8,
            )

        if sec == "XLE":
            d22 = pd.Timestamp("2022-01-03")
            i22 = dates.get_indexer([d22], method="nearest")[0]
            ax.annotate(
                "2022 Anti-Bubble Proof:\nLate-'21 XLE Mean = 40.3% (<70%)\n→ XLE +64.3% in 2022 (Held!)",
                xy=(dates[i22], log_idx[i22]), xytext=(pd.Timestamp("2018-04-01"), log_idx.max() + 4),
                fontsize=7.2, fontweight="bold", color=pal["text"],
                bbox=dict(boxstyle="round,pad=0.25", facecolor=pal["card_green"], edgecolor=pal["emerald"], lw=1.0),
                arrowprops=dict(arrowstyle="->", color=pal["emerald"], lw=1.4),
                zorder=8,
            )

        l1, = ax.plot(dates, log_idx, color=col_line, lw=2.2, label=f"{sec} Log-Growth Index L_{sec}(t) [Left Y1]", zorder=5)
        env_color = pal["crimson"] if sec != "XLE" else pal["cyan"]
        l2, = ax2.plot(dates, sc_env, color=env_color, lw=1.7, alpha=0.88,
                       label=f"{sec} Smooth Causal Warning Envelope [Right Y2]", zorder=3)
        ax2.axhline(70.0, color=pal["crimson"], ls="--", lw=1.1, alpha=0.85)
        ax2.axhline(25.0, color=pal["emerald"], ls=":", lw=1.0, alpha=0.85)

        ax.set_ylabel(f"L_{sec}(t)", fontsize=8.8, fontweight="bold", color=col_line)
        ax2.set_ylabel("I^{Sec*} (%)", fontsize=8.6, fontweight="bold", color=pal["sub"])
        ax2.set_ylim(-3, 108)
        ax2.tick_params(colors=pal["text"], labelsize=8.2)
        ax.set_ylim(log_idx.min() - 28, log_idx.max() + 62)
        ax.set_xlim(dates[0], dates[-1])
        ax.xaxis.set_major_locator(mdates.YearLocator(2))
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
        ax.set_title(sub_t, fontsize=9.5, fontweight="bold", color=pal["text"], loc="left", pad=4)
        ax.legend([l1, l2], [l1.get_label(), l2.get_label()], loc="upper left", fontsize=7.3,
                  framealpha=0.92, facecolor=pal["bg"], edgecolor=pal["grid"], labelcolor=pal["text"])

    save_exact_huxga(fig, PLOTS_DIR / f"02_Flagship_Sector_Dislocation_Trajectories_{theme}.png", pal["bg"])


# ==============================================================================
# FIGURE 3: 12-Event Sector Popperian Matrix
# ==============================================================================
def plot_03_popperian_matrix(art: dict, theme: str) -> None:
    pal = get_palette(theme)
    fig = plt.figure(figsize=FIGSIZE, dpi=DPI)
    gs = fig.add_gridspec(2, 1, height_ratios=[1.32, 1.0], left=0.060, right=0.960, top=0.892, bottom=0.068, hspace=0.28)

    add_header_footer(
        fig, pal,
        "Figure 3: 12-Event Sector Dislocation Popperian Falsification & Separation Matrix (2006–2026)",
        "100% Sensitivity (12/12 Pre-Peak Maxima >= 70.0%, Mean 91.1%) & 100% Trough Reset (12/12 Minima <= 1.8%, Mean Separation 90.8%, Mean Lead 217.8d)",
        "Evaluated across Systemic Contagion Crashes (SD01–SD03, SD08–SD11) and Idiosyncratic Sector Fractures (SD04 Oil, SD05 Biotech, SD06/07 2018, SD12 2025).",
    )

    evs = art["event_study_12"]
    x = np.arange(len(evs))
    labels = [f"{e['id']}: {e['sector']}\n({e['peak'][:7]})\nDD {e['dd_pct']:.0f}%" for e in evs]

    ax1 = fig.add_subplot(gs[0, 0])
    style_ax(ax1, pal)
    pk_sec = [e["sec_pre_max"] for e in evs]
    pk_mahal = [e["mahal_pre"] for e in evs]
    pk_spca = [e["spca_pre"] for e in evs]
    pk_dfm = [e["dfm_pre"] for e in evs]
    pk_diff = [e["diff_pre"] for e in evs]
    tr_sec = [e["sec_trough_min"] for e in evs]

    ax1.fill_between(x, tr_sec, pk_sec, color=pal["cyan"], alpha=0.14, label="Peak-to-Trough Regime Separation Span (Mean Δ = 90.8%)")
    ax1.axhline(70.0, color=pal["crimson"], lw=2.0, ls="--", label="Critical Pre-Peak Warning Gate (70.0% — 12/12 Hit Rate)")
    ax1.axhline(25.0, color=pal["emerald"], lw=1.8, ls=":", label="Contrarian Trough Accumulation Floor (25.0% — 12/12 Reset)")

    ax1.plot(x, pk_mahal, "s--", color=pal["crimson"], lw=1.4, ms=5.5, alpha=0.78, label="Sector Mahalanobis I^{Mahal} Pre-Peak Max")
    ax1.plot(x, pk_spca, "D--", color=pal["purple"], lw=1.4, ms=5.5, alpha=0.78, label="Sector Sparse PCA I^{SPCA} Pre-Peak Max (Localized Driver)")
    ax1.plot(x, pk_dfm, "^:", color=pal["amber"], lw=1.4, ms=5.5, alpha=0.78, label="Sector Kalman DFM I^{DFM} Pre-Peak Max")
    ax1.plot(x, pk_diff, "v:", color=pal["teal"], lw=1.4, ms=5.5, alpha=0.78, label="Sector Copula Diffusion I^{Diff} Pre-Peak Max")
    ax1.plot(x, pk_sec, "o-", color=pal["blue"], lw=2.8, ms=8.5, label="Sector Master Composite I^{Sec*} Pre-Peak Max (Mean 91.1%)", zorder=7)
    ax1.plot(x, tr_sec, "P-", color=pal["emerald"], lw=2.5, ms=8.5, label="Sector Master I^{Sec*} Crash-Trough Min (Mean 0.25%, Max 1.8%)", zorder=7)

    for i, (hi, lo) in enumerate(zip(pk_sec, tr_sec)):
        y_off = -11.0 if hi > 90.0 else 3.5
        ax1.annotate(
            f"{hi:.1f}%", xy=(i, hi), xytext=(0, y_off), textcoords="offset points",
            ha="center", va="center", fontsize=7.6, fontweight="bold", color=pal["blue"],
            bbox=dict(boxstyle="round,pad=0.15", facecolor=pal["bg"], edgecolor=pal["blue"], lw=0.6, alpha=0.92),
            zorder=8,
        )
        ax1.text(i, lo + 2.8, f"{lo:.1f}%", ha="center", va="bottom", fontsize=7.4, fontweight="bold", color=pal["emerald"])

    ax1.set_xticks(x)
    ax1.set_xticklabels(labels, fontsize=7.9, fontweight="bold")
    ax1.set_ylim(-5, 112)
    ax1.set_ylabel("Composite Dislocation Score (%)", fontsize=9.6, fontweight="bold", color=pal["text"])
    ax1.set_title("A. Five-Engine Pre-Peak Warning Maxima vs. Crash-Liquidation Damper Trough Minima Across 12 Sector Dislocations",
                  fontsize=10.6, fontweight="bold", color=pal["text"], pad=8)
    ax1.legend(loc="center right", bbox_to_anchor=(0.995, 0.43), fontsize=7.5, framealpha=0.94, facecolor=pal["bg"], edgecolor=pal["grid"], labelcolor=pal["text"])

    ax2 = fig.add_subplot(gs[1, 0])
    style_ax(ax2, pal)
    ax2_r = ax2.twinx()
    dds = [abs(e["dd_pct"]) for e in evs]
    leads = [e["lead_252d"] for e in evs]

    bars = ax2.bar(x - 0.17, dds, width=0.34, color=pal["crimson"], alpha=0.85, label="Realized Unhedged Sector Peak-to-Trough Drawdown |DD_k| (%) [Left Y1]")
    bars_ld = ax2_r.bar(x + 0.17, leads, width=0.34, color=pal["amber"], alpha=0.85, label="252d Pre-Peak Early-Warning Lead Horizon (Business Days, Mean = 217.8d) [Right Y2]")

    for b, v in zip(bars, dds):
        ax2.text(b.get_x() + b.get_width() / 2, v + 1.4, f"-{v:.1f}%", ha="center", va="bottom", fontsize=7.5, fontweight="bold", color=pal["crimson"])
    for b, v in zip(bars_ld, leads):
        ax2_r.text(b.get_x() + b.get_width() / 2, v + 5, f"{v}d", ha="center", va="bottom", fontsize=7.5, fontweight="bold", color=pal["amber"])

    ax2.set_xticks(x)
    ax2.set_xticklabels(labels, fontsize=7.9, fontweight="bold")
    ax2.set_ylim(0, 102)
    ax2_r.set_ylim(0, 315)
    ax2.set_ylabel("Unhedged Sector Crash |DD_k| (%)", fontsize=9.4, fontweight="bold", color=pal["crimson"])
    ax2_r.set_ylabel("Early-Warning Lead (Business Days)", fontsize=9.4, fontweight="bold", color=pal["amber"])
    ax2_r.tick_params(colors=pal["text"], labelsize=8.4)
    ax2.set_title("B. Sector Dislocation Severity vs. Fiduciary Advance Warning Lead Cushion (Mean |DD| = 36.6%, Mean Lead = 217.8 Business Days)",
                  fontsize=10.5, fontweight="bold", color=pal["text"], pad=8)

    h1, l1 = ax2.get_legend_handles_labels()
    h2, l2 = ax2_r.get_legend_handles_labels()
    ax2.legend(h1 + h2, l1 + l2, loc="upper center", ncol=2, fontsize=7.7, framealpha=0.94, facecolor=pal["bg"], edgecolor=pal["grid"], labelcolor=pal["text"])

    save_exact_huxga(fig, PLOTS_DIR / f"03_12_Event_Sector_Popperian_Matrix_{theme}.png", pal["bg"])


# ==============================================================================
# FIGURE 4: Asset Granularity Audit — ETFs vs. 46 Single Stocks (Includes XLY)
# ==============================================================================
def plot_04_etf_vs_single_stocks(art: dict, theme: str) -> None:
    pal = get_palette(theme)
    fig = plt.figure(figsize=FIGSIZE, dpi=DPI)
    gs = fig.add_gridspec(2, 2, left=0.060, right=0.960, top=0.892, bottom=0.068, hspace=0.30, wspace=0.22)

    add_header_footer(
        fig, pal,
        "Figure 4: Asset Granularity Audit — Sector ETFs (>= 0.87) vs. Single Stocks (< 0.87)",
        "Empirical Audit of 11 GICS Sector ETFs vs. 46 S&P 500 Blue-Chip Constituents (2006–2026): Jump Contamination & Ruin/Absorption Barrier Asymmetry",
        "Self-reconstituting Sector ETFs satisfy P(τ_ruin < ∞) = 0 (validating Trough Re-Entry), whereas Single Stocks exhibit 10.9% 8-yr impairment.",
    )

    gs_sum = art["granularity_summary"]
    etf_m = gs_sum["etf_mean"]
    stk_m = gs_sum["stock_mean"]

    ax1 = fig.add_subplot(gs[0, 0])
    style_ax(ax1, pal)
    metrics_lbl = ["Annualized\nVolatility (%)", "|r_1d| ≥ 5%\nJump Days", "|r_1d| ≥ 8%\nExtreme Gaps",
                   "Catastrophic\n≥75% Crash (%)", "8-Yr Unrecovered\nImpairment (%)"]
    v_etf = [etf_m["ann_vol"], etf_m["jumps_5pct"], etf_m["jumps_8pct"], etf_m["catastrophic_75_pct"], 0.0]
    v_stk = [stk_m["ann_vol"], stk_m["jumps_5pct"], stk_m["jumps_8pct"], stk_m["catastrophic_75_pct"], stk_m["secular_impairment_8yr_pct"]]
    xm = np.arange(len(metrics_lbl))
    b_e = ax1.bar(xm - 0.18, v_etf, width=0.36, color=pal["emerald"], label="11 GICS Sector ETFs (γ = 0.95 ≥ 0.87 — RETAINED)")
    b_s = ax1.bar(xm + 0.18, v_stk, width=0.36, color=pal["crimson"], label="46 S&P 500 Single Stocks (γ = 0.58 < 0.87 — DROPPED as Targets)")
    for b in b_e:
        ax1.text(b.get_x() + b.get_width() / 2, b.get_height() + 2.0, f"{b.get_height():.1f}", ha="center", va="bottom", fontsize=7.8, fontweight="bold", color=pal["emerald"])
    for b in b_s:
        ax1.text(b.get_x() + b.get_width() / 2, b.get_height() + 2.0, f"{b.get_height():.1f}", ha="center", va="bottom", fontsize=7.8, fontweight="bold", color=pal["crimson"])
    ax1.set_xticks(xm)
    ax1.set_xticklabels(metrics_lbl, fontsize=8.1, fontweight="bold")
    ax1.set_ylim(0, 172)
    ax1.set_ylabel("Empirical Count / Percentage (2006–2026)", fontsize=9.2, fontweight="bold", color=pal["text"])
    ax1.set_title("A. Jump-Diffusion Noise & Permanent Impairment: ETFs vs. Single Stocks", fontsize=10.3, fontweight="bold", color=pal["text"], pad=8)
    ax1.legend(loc="upper right", fontsize=7.6, framealpha=0.92, facecolor=pal["bg"], edgecolor=pal["grid"], labelcolor=pal["text"])

    ax2 = fig.add_subplot(gs[0, 1])
    style_ax(ax2, pal)
    st_det = pd.DataFrame(gs_sum["stock_details"])
    et_det = pd.DataFrame(gs_sum["etf_details"])
    imp = st_det[st_det["secular_impairment_8yr"]]
    ok_st = st_det[~st_det["secular_impairment_8yr"]]

    ax2.scatter(ok_st["jumps_5pct"], ok_st["max_dd"], s=52, color=pal["amber"], alpha=0.80, edgecolors=pal["axis"], lw=0.6, label="Surviving S&P 500 Single Stocks")
    ax2.scatter(imp["jumps_5pct"], imp["max_dd"], s=90, marker="X", color=pal["crimson"], edgecolors=pal["axis"], lw=0.8, label="8-Yr Unrecovered Value Traps (AIG, C, BAC, SLB, NKE)", zorder=6)
    ax2.scatter(et_det["jumps_5pct"], et_det["max_dd"], s=95, marker="D", color=pal["emerald"], edgecolors=pal["axis"], lw=0.9, label="11 GICS Sector ETFs (Diversified & Self-Cleansing)", zorder=5)
    ax2.axhline(-75.0, color=pal["crimson"], ls="--", lw=1.4, label="-75% Catastrophic Impairment Line (32.6% Stocks vs. 9.1% ETFs)")

    for _, r in imp.iterrows():
        ax2.annotate(r["ticker"], (r["jumps_5pct"], r["max_dd"]), xytext=(6, -2), textcoords="offset points", fontsize=7.9, fontweight="bold", color=pal["crimson"])
    for tkr_lbl in ["XLP", "XLK", "XLY", "XLE", "XLF"]:
        row_e = et_det[et_det["ticker"] == tkr_lbl].iloc[0]
        dx_off = -28 if tkr_lbl == "XLK" else 6
        ax2.annotate(tkr_lbl, (row_e["jumps_5pct"], row_e["max_dd"]), xytext=(dx_off, 2), textcoords="offset points", fontsize=7.6, fontweight="bold", color=pal["emerald"])

    ax2.set_xlabel("Idiosyncratic |r_1d| ≥ 5% Daily Jump Sessions (2006–2026)", fontsize=9.1, fontweight="bold", color=pal["text"])
    ax2.set_ylabel("Worst Realized Peak-to-Trough Drawdown (%)", fontsize=9.1, fontweight="bold", color=pal["text"])
    ax2.set_ylim(-104, -26)
    ax2.set_xlim(-10, 560)
    ax2.set_title("B. Cross-Sectional Jump Frequency vs. Tail Drawdown Dispersion", fontsize=10.3, fontweight="bold", color=pal["text"], pad=8)
    ax2.legend(loc="upper right", fontsize=7.4, framealpha=0.94, facecolor=pal["bg"], edgecolor=pal["grid"], labelcolor=pal["text"])

    ax3 = fig.add_subplot(gs[1, 0])
    style_ax(ax3, pal)
    stocks_df = pd.read_parquet(DATA_DIR / "single_stocks_1999_2026.parquet").loc["2006-01-02":"2026-11-13"].ffill().bfill()
    df_m = pd.read_parquet(DATA_DIR / "sector_master_panel_1999_2026.parquet").loc["2006-01-02":"2026-11-13"]
    for tkr, col, lbl, lw in [
        ("XLF", pal["emerald"], "XLF Financials Sector ETF (Full Secular Recovery to New Highs)", 2.3),
        ("JPM", pal["blue"], "JPM (Survivor Winner)", 1.5),
        ("C", pal["amber"], "Citigroup (C) — -97% Crash, Never Recovered 2007 Peak in 19 Years!", 1.8),
        ("AIG", pal["crimson"], "AIG — -99% Bailout Dilution, Permanent Absorption Trap!", 1.8),
    ]:
        ser = df_m["XLF"] if tkr == "XLF" else stocks_df[tkr]
        w_norm = 100.0 * (ser / ser.iloc[0])
        ax3.plot(w_norm.index, w_norm.to_numpy(), color=col, lw=lw, label=lbl)
    ax3.set_yscale("log")
    ax3.axhline(100.0, color=pal["slate"], ls=":", lw=1.1)
    ax3.set_ylabel("$100 Initial Investment (Log Scale)", fontsize=9.1, fontweight="bold", color=pal["text"])
    ax3.set_title("C. Why Contrarian Trough Re-Entry (<25%) Fails on Single Stocks: Absorption Ruin", fontsize=10.1, fontweight="bold", color=pal["text"], pad=8)
    ax3.legend(loc="lower left", fontsize=7.4, framealpha=0.92, facecolor=pal["bg"], edgecolor=pal["grid"], labelcolor=pal["text"])

    ax4 = fig.add_subplot(gs[1, 1])
    style_ax(ax4, pal)
    sd = art["standalone_sector_defense"]
    s_tks = [r["sector"] for r in sd]
    dd_u = [abs(r["unhedged_max_dd"]) for r in sd]
    dd_h = [abs(r["hedged_max_dd"]) for r in sd]
    saved = [r["dd_saved"] for r in sd]
    xs = np.arange(len(s_tks))
    ax4.bar(xs - 0.19, dd_u, width=0.35, color=pal["crimson"], alpha=0.85, label="Unhedged Sector ETF Worst Drawdown |MaxDD| (%)")
    ax4.bar(xs + 0.19, dd_h, width=0.35, color=pal["emerald"], alpha=0.90, label="Sector I^{Sec*} Shielded Worst Drawdown |MaxDD| (%)")
    for i, (u, h, sv) in enumerate(zip(dd_u, dd_h, saved)):
        ax4.text(i - 0.19, u + 1.3, f"-{u:.1f}%", ha="center", va="bottom", fontsize=6.9, fontweight="bold", color=pal["crimson"])
        ax4.text(i + 0.21, h + 1.3, f"-{h:.1f}%\n(+{sv:.0f}%)", ha="center", va="bottom", fontsize=6.6, fontweight="bold", color=pal["emerald"])
    ax4.set_xticks(xs)
    ax4.set_xticklabels([f"{r['sector']}\nSh {r['unhedged_sharpe']:.2f}→{r['hedged_sharpe']:.2f}" for r in sd], fontsize=7.3, fontweight="bold")
    ax4.set_ylim(0, 96)
    ax4.set_ylabel("Worst 20-Year Drawdown Magnitude (%)", fontsize=9.2, fontweight="bold", color=pal["text"])
    mean_sv = float(np.mean(saved))
    ax4.set_title(f"D. Standalone Sector ETF Defense Across 7 Flagship ETFs (Mean +{mean_sv:.1f}% DD Saved)", fontsize=10.0, fontweight="bold", color=pal["text"], pad=8)
    ax4.legend(loc="upper right", fontsize=7.4, framealpha=0.92, facecolor=pal["bg"], edgecolor=pal["grid"], labelcolor=pal["text"])

    save_exact_huxga(fig, PLOTS_DIR / f"04_Sector_ETFs_vs_Single_Stocks_Granularity_{theme}.png", pal["bg"])


# ==============================================================================
# FIGURE 5: Signal Mapping Mechanics — Head-to-Head 6-Sleeve vs. 7-Sleeve (T5)
# ==============================================================================
def plot_05_signal_mapping_backtest(df_ts: pd.DataFrame, art: dict, theme: str) -> None:
    pal = get_palette(theme)
    fig = plt.figure(figsize=FIGSIZE, dpi=DPI)
    gs = fig.add_gridspec(3, 1, height_ratios=[1.28, 0.95, 0.92], left=0.060, right=0.808, top=0.892, bottom=0.060, hspace=0.24)

    add_header_footer(
        fig, pal,
        "Figure 5: Signal Mapping Mechanics & 20-Year Portfolio Performance — S_6^⊥ (6-Sleeve) vs. T5 (7-Sleeve)",
        "Head-to-Head Out-of-Sample Comparison (2006–2026, 15 bps Friction, 1d Causal Lag, Actual IRX T-Bills): M4 Cash Shield & M3 Active Tilt vs. M1/M2 & SPY",
        "S_6^⊥ M4 (Sharpe 0.70, MaxDD -19.66%, Calmar 0.47) & T5 M4 (Sharpe 0.67, MaxDD -25.11%) both outperform SPY (Sharpe 0.54, MaxDD -55.19%).",
    )

    dates = df_ts.index
    bt = art["backtest_summary"]["irx"]

    ax1 = fig.add_subplot(gs[0, 0])
    style_ax(ax1, pal)
    series_cfg = [
        ("Wealth_SPY", pal["slate"], "--", 1.8, f"SPY Buy & Hold\n(${bt['SPY_BuyHold']['end_wealth']:.0f} | {bt['SPY_BuyHold']['cagr']:.2f}% | {bt['SPY_BuyHold']['sharpe']:.2f} Sh)"),
        ("S6_Wealth_M3_CoreTilt_Retained", pal["blue"], "-", 2.3, f"M3 (S_6^⊥ 6-Sleeve Tilt)\n(${bt['M3_CoreTilt_6S']['end_wealth']:.0f} | {bt['M3_CoreTilt_6S']['cagr']:.2f}% | {bt['M3_CoreTilt_6S']['sharpe']:.2f} Sh)"),
        ("S7_Wealth_M3_CoreTilt_Retained", pal["cyan"], "--", 2.0, f"M3 (T5 7-Sleeve Tilt)\n(${bt['M3_CoreTilt_7S']['end_wealth']:.0f} | {bt['M3_CoreTilt_7S']['cagr']:.2f}% | {bt['M3_CoreTilt_7S']['sharpe']:.2f} Sh)"),
        ("S6_Wealth_M4_Fiduciary_Optimal", pal["emerald"], "-", 2.7, f"M4 (S_6^⊥ 6-Sleeve Shield)\n(${bt['M4_Fiduciary_6S']['end_wealth']:.0f} | {bt['M4_Fiduciary_6S']['cagr']:.2f}% | {bt['M4_Fiduciary_6S']['sharpe']:.2f} Sh)"),
        ("S7_Wealth_M4_Fiduciary_Optimal", pal["purple"], "-.", 2.2, f"M4 (T5 7-Sleeve Shield)\n(${bt['M4_Fiduciary_7S']['end_wealth']:.0f} | {bt['M4_Fiduciary_7S']['cagr']:.2f}% | {bt['M4_Fiduciary_7S']['sharpe']:.2f} Sh)"),
        ("S6_Wealth_BroadOnly_Defensive", pal["teal"], ":", 1.7, f"Broad I* Only (No Sectors)\n(${bt['BroadOnly_Defensive']['end_wealth']:.0f} | {bt['BroadOnly_Defensive']['cagr']:.2f}% | {bt['BroadOnly_Defensive']['sharpe']:.2f} Sh)"),
        ("S6_Wealth_M1_Binary_Dropped", pal["amber"], ":", 1.5, f"M1 Binary 70% [DROPPED]\n(${bt['M1_Binary_Dropped_6S']['end_wealth']:.0f} | {bt['M1_Binary_Dropped_6S']['sharpe']:.2f} Sh)"),
        ("S6_Wealth_M2_LongShort_Dropped", pal["crimson"], ":", 1.5, f"M2 Long/Short [DROPPED]\n(${bt['M2_LongShort_Dropped_6S']['end_wealth']:.0f} | {bt['M2_LongShort_Dropped_6S']['sharpe']:.2f} Sh)"),
    ]
    for col, c, ls, lw, lbl in series_cfg:
        ax1.plot(dates, df_ts[col].to_numpy(), color=c, ls=ls, lw=lw, label=lbl)
    ax1.set_yscale("log")
    ax1.yaxis.set_major_formatter(mticker.ScalarFormatter())
    ax1.set_yticks([50, 100, 200, 400, 600, 900])
    ax1.set_xlim(dates[0], dates[-1])
    ax1.set_ylabel("$100 Cumulative Wealth (Log)", fontsize=9.1, fontweight="bold", color=pal["text"])
    ax1.set_title("A. Cumulative $100 Wealth Trajectories: S_6^⊥ (6-Sleeve) & T5 (7-Sleeve) vs. Benchmarks",
                  fontsize=10.2, fontweight="bold", color=pal["text"], loc="left", pad=5)
    ax1.legend(loc="upper left", bbox_to_anchor=(1.01, 1.03), fontsize=7.0, frameon=True, facecolor=pal["panel"], edgecolor=pal["grid"], labelcolor=pal["text"])

    ax2 = fig.add_subplot(gs[1, 0], sharex=ax1)
    style_ax(ax2, pal)
    ax2.fill_between(dates, df_ts["DD_SPY"].to_numpy(), 0, color=pal["crimson"], alpha=0.16, label=f"SPY Unhedged\n(MaxDD = {bt['SPY_BuyHold']['max_dd']:.2f}%)")
    ax2.plot(dates, df_ts["DD_SPY"].to_numpy(), color=pal["crimson"], lw=1.2, alpha=0.72)
    ax2.plot(dates, df_ts["S6_DD_M3_CoreTilt_Retained"].to_numpy(), color=pal["blue"], lw=1.7, label=f"M3 (S_6^⊥ 6-Sleeve)\n(MaxDD = {bt['M3_CoreTilt_6S']['max_dd']:.2f}%)")
    ax2.plot(dates, df_ts["S7_DD_M3_CoreTilt_Retained"].to_numpy(), color=pal["cyan"], ls="--", lw=1.5, label=f"M3 (T5 7-Sleeve)\n(MaxDD = {bt['M3_CoreTilt_7S']['max_dd']:.2f}%)")
    ax2.plot(dates, df_ts["S6_DD_BroadOnly_Defensive"].to_numpy(), color=pal["teal"], ls=":", lw=1.6, label=f"Broad I* Only\n(MaxDD = {bt['BroadOnly_Defensive']['max_dd']:.2f}%)")
    ax2.plot(dates, df_ts["S7_DD_M4_Fiduciary_Optimal"].to_numpy(), color=pal["purple"], ls="-.", lw=2.0, label=f"M4 (T5 7-Sleeve Shield)\n(MaxDD = {bt['M4_Fiduciary_7S']['max_dd']:.2f}%)")
    ax2.plot(dates, df_ts["S6_DD_M4_Fiduciary_Optimal"].to_numpy(), color=pal["emerald"], lw=2.5, label=f"M4 (S_6^⊥ 6-Sleeve Shield)\n(MaxDD = {bt['M4_Fiduciary_6S']['max_dd']:.2f}% | Best!)")
    ax2.axhline(-20.0, color=pal["emerald"], ls="--", lw=1.3, label="-20% Fiduciary Ceiling")
    ax2.set_ylim(-60, 3)
    ax2.set_ylabel("Underwater Drawdown (%)", fontsize=9.1, fontweight="bold", color=pal["text"])
    ax2.set_title("B. Underwater Drawdowns — S_6^⊥ Caps GFC Drawdown at -19.66% vs. -25.11% on T5 (Sep-'08 XLY Bear Bounce) & -55.19% on SPY",
                  fontsize=10.0, fontweight="bold", color=pal["text"], loc="left", pad=5)
    ax2.legend(loc="upper left", bbox_to_anchor=(1.01, 1.03), fontsize=7.2, frameon=True, facecolor=pal["panel"], edgecolor=pal["grid"], labelcolor=pal["text"])

    ax3 = fig.add_subplot(gs[2, 0], sharex=ax1)
    style_ax(ax3, pal)
    w_cols = [
        ("S6_Weight_S1_Tech_Growth", "S1: Compute & Growth (36% Base)", pal["blue"]),
        ("S6_Weight_S2_Industrial_CapEx", "S2: Industrials & CapEx (12% Base)", pal["purple"]),
        ("S6_Weight_S3_Energy_Supply", "S3: Energy Supply (7% Base)", pal["amber"]),
        ("S6_Weight_S4_Financial_Credit", "S4: Financials & Credit (15% Base)", pal["teal"]),
        ("S6_Weight_S5_Rate_RealEstate", "S5: Real Estate & Util (8% Base)", pal["crimson"]),
        ("S6_Weight_S6_Defensive_Quality", "S6: Health & Staples (22% Base)", pal["emerald"]),
        ("S6_Weight_Cash", "3M Treasury Bill Shield Reserve", "#94A3B8" if theme == "white" else "#475569"),
    ]
    ys = [df_ts[c].to_numpy() for c, _, _ in w_cols]
    ax3.stackplot(dates, ys, labels=[lbl for _, lbl, _ in w_cols], colors=[col for _, _, col in w_cols], alpha=0.86)
    ax3.set_ylim(0, 100)
    ax3.set_xlim(dates[0], dates[-1])
    ax3.xaxis.set_major_locator(mdates.YearLocator(2))
    ax3.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax3.set_ylabel("S_6^⊥ Allocation (%)", fontsize=9.1, fontweight="bold", color=pal["text"])
    ax3.set_title("C. S_6^⊥ (6-Sleeve) M4 Schmitt-Trigger Allocation Dynamics (143.8%/yr Turnover; T5 7-Sleeve Allocation Shown in Figure 8)",
                  fontsize=10.0, fontweight="bold", color=pal["text"], loc="left", pad=5)
    ax3.legend(loc="upper left", bbox_to_anchor=(1.01, 1.02), fontsize=7.3, frameon=True, facecolor=pal["panel"], edgecolor=pal["grid"], labelcolor=pal["text"])

    save_exact_huxga(fig, PLOTS_DIR / f"05_Signal_Mapping_Portfolio_Wealth_Drawdown_{theme}.png", pal["bg"])


# ==============================================================================
# FIGURE 6 (V1): 8-Pillar Orthogonal Fingerprint & Sparse Coalition Anatomy
# ==============================================================================
def plot_06_8pillar_coalition_anatomy(df_ts: pd.DataFrame, art: dict, theme: str) -> None:
    pal = get_palette(theme)
    fig = plt.figure(figsize=FIGSIZE, dpi=DPI)
    gs_top = fig.add_gridspec(1, 1, left=0.165, right=0.965, top=0.892, bottom=0.515)
    gs_bot = fig.add_gridspec(1, 3, left=0.058, right=0.950, top=0.415, bottom=0.068, wspace=0.22)

    add_header_footer(
        fig, pal,
        "Figure 6: 8-Pillar Sector-Orthogonal Basis (B_{k,8}^⊥) Fingerprint & Sparse Coalition Anatomy",
        "Pre-Peak Orthant Activation Across All 12 Sector Dislocations (SD01–SD12) + Q4 2021 XLE Anti-Bubble Control & Archetype Decompositions",
        "Explains visually why Sparse PCA (I^{SPCA}, 99.3% peak) and Precision Mahalanobis (I^{Mahal}, 97.9% peak) govern localized sector coalitions.",
    )

    # Panel A: 8 Pillars x 13 Regimes Pre-Peak Orthant Activation Heatmap
    ax_hm = fig.add_subplot(gs_top[0, 0])
    style_ax(ax_hm, pal)
    fps = art["coalition_fingerprints"]
    pillar_lbls = [
        "P1: Secular Stretch (+)",
        "P2: Recursive BSADF (+)",
        "P3: LPPLS Singularity (+)",
        "P4: TDA Entropy Collapse (-)",
        "P5: Wavelet Spectral Lock (-)",
        "P6: Vol/Skew Complacency (+)",
        "P7: Single-Stock Breadth (+)",
        "P8: Macro/Credit Coupling (+)",
    ]
    mat = np.column_stack([fp["pillars_95p"] for fp in fps])  # (8, 13)
    col_lbls = [f"{fp['label']}\n[{fp['active_coalition_count']}/8 Active]" for fp in fps]

    im = ax_hm.imshow(mat, cmap="YlOrRd", vmin=0.0, vmax=3.2, aspect="auto")
    ax_hm.grid(False)
    ax_hm.axvline(11.5, color=pal["emerald"], lw=2.8, ls="--")
    ax_hm.set_xticks(range(len(fps)))
    ax_hm.set_xticklabels(col_lbls, fontsize=7.5, fontweight="bold")
    ax_hm.set_yticks(range(8))
    ax_hm.set_yticklabels(pillar_lbls, fontsize=8.3, fontweight="bold")
    for r_i in range(8):
        for c_j in range(len(fps)):
            val = mat[r_i, c_j]
            txt_c = "#FFFFFF" if val >= 1.85 else "#0F172A"
            ax_hm.text(c_j, r_i, f"{val:.2f}σ", ha="center", va="center", fontsize=7.2, fontweight="bold", color=txt_c)
    cbar = fig.colorbar(im, ax=ax_hm, fraction=0.022, pad=0.015)
    cbar.set_label("95th-Pct Pre-Peak Orthant u_{k,j} (σ)", fontsize=8.4, fontweight="bold", color=pal["text"])
    cbar.ax.tick_params(labelsize=8.0, colors=pal["text"])
    ax_hm.set_title(
        "A. 8-Pillar Pre-Peak Activation Matrix (u_{k,j} ≥ 0.85σ Active Coalition): 6–8 Pillars Fire Before SD01–SD12 Crashes vs. 0/8 on Q4'21 XLE Anti-Bubble!",
        fontsize=10.3, fontweight="bold", color=pal["text"], pad=8,
    )

    # Bottom 3 Archetype Panels: (B) XLK 2019–2026, (C) XLE 2013–2024, (D) XLF 2006–2012
    archetypes = [
        (
            0, "XLK", "2019-01-01", "2026-11-13",
            "B. Tech Archetype (XLK, 2019–2026):\nBSADF + ^VXN Skew + Narrow Breadth (P7)",
            [("P2+P3 Explosiveness", ["Upos_XLK_P2", "Upos_XLK_P3"], pal["crimson"]),
             ("P7 Breadth Crowding", ["Upos_XLK_P7"], pal["purple"]),
             ("P6 ^VXN Vol/Skew", ["Upos_XLK_P6"], pal["amber"]),
             ("P1+P4+P5+P8 Base", ["Upos_XLK_P1", "Upos_XLK_P4", "Upos_XLK_P5", "Upos_XLK_P8"], pal["blue"])],
            "SD09 ('21) & SD12 ('25)\nSparse Coalitions → ≥91%",
        ),
        (
            1, "XLE", "2013-01-01", "2023-12-31",
            "C. Energy Archetype (XLE, 2013–2023):\n2014 Shale Bust vs. 2021 Secular Gate Exemption",
            [("P1 Secular Stretch", ["Upos_XLE_P1"], pal["amber"]),
             ("P2+P3 Oil Run-Up", ["Upos_XLE_P2", "Upos_XLE_P3"], pal["crimson"]),
             ("P6+P8 ^OVX Coupling", ["Upos_XLE_P6", "Upos_XLE_P8"], pal["purple"]),
             ("P4+P5+P7 Topology", ["Upos_XLE_P4", "Upos_XLE_P5", "Upos_XLE_P7"], pal["teal"])],
            "Q4'21: 7Yr Rel Gate\nSuppresses Score <70%!",
        ),
        (
            2, "XLF", "2006-01-02", "2012-06-30",
            "D. Credit Archetype (XLF, 2006–2012):\n2007 Credit Peak vs. 2009 Damper Reset (0.0%)",
            [("P8 Credit/Housing PTI", ["Upos_XLF_P8"], pal["crimson"]),
             ("P7 Bank Breadth Decay", ["Upos_XLF_P7"], pal["purple"]),
             ("P4+P5 TDA/Wavelet Lock", ["Upos_XLF_P4", "Upos_XLF_P5"], pal["amber"]),
             ("P1+P2+P3+P6 Valuation", ["Upos_XLF_P1", "Upos_XLF_P2", "Upos_XLF_P3", "Upos_XLF_P6"], pal["teal"])],
            "Mar '09 GFC Trough:\nΛ_Crash → 0.0% (<25%)",
        ),
    ]

    for col_i, sec, d0, d1, ttl, grp_list, note_txt in archetypes:
        ax = fig.add_subplot(gs_bot[0, col_i])
        style_ax(ax, pal)
        ax_r = ax.twinx()
        sub = df_ts.loc[d0:d1]
        dts = sub.index

        stacks = []
        cols = []
        lbls = []
        for g_lbl, c_names, c_hex in grp_list:
            arr = np.sum([pd.Series(sub[cn]).ewm(span=21, min_periods=1).mean().to_numpy() for cn in c_names], axis=0)
            stacks.append(arr)
            cols.append(c_hex)
            lbls.append(g_lbl)

        ax.stackplot(dts, stacks, labels=lbls, colors=cols, alpha=0.72)
        sc_env = smooth_envelope(sub[f"SecScore_{sec}"].to_numpy())
        ax_r.plot(dts, sc_env, color=pal["text"], lw=2.1, label=f"I_{{{sec}}}^{{Sec*}} Envelope (%)")
        ax_r.axhline(70.0, color=pal["crimson"], ls="--", lw=1.2)
        ax_r.axhline(25.0, color=pal["emerald"], ls=":", lw=1.1)
        ax_r.set_ylim(-4, 108)
        ax_r.tick_params(colors=pal["text"], labelsize=7.8)
        if col_i == 2:
            ax_r.set_ylabel("I^{Sec*} (%)", fontsize=8.6, fontweight="bold", color=pal["text"])
        if col_i == 0:
            ax.set_ylabel("Stacked Orthant ∑ u_{k,j} (21d EMA)", fontsize=8.8, fontweight="bold", color=pal["text"])

        ax.text(
            0.97, 0.95, note_txt, transform=ax.transAxes, ha="right", va="top",
            fontsize=7.1, fontweight="bold", color=pal["text"],
            bbox=dict(boxstyle="round,pad=0.25", facecolor=pal["card"], edgecolor=pal["axis"], lw=0.7, alpha=0.93),
        )
        ax.xaxis.set_major_locator(mdates.YearLocator(2))
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
        ax.set_xlim(dts[0], dts[-1])
        ax.set_ylim(0, max(float(np.max(np.sum(stacks, axis=0))) * 1.26, 6.0))
        ax.set_title(ttl, fontsize=9.2, fontweight="bold", color=pal["text"], pad=6)
        ax.legend(loc="upper left", fontsize=6.7, framealpha=0.90, facecolor=pal["bg"], edgecolor=pal["grid"], labelcolor=pal["text"])

    save_exact_huxga(fig, PLOTS_DIR / f"06_Sector_8Pillar_Coalition_Anatomy_{theme}.png", pal["bg"])


# ==============================================================================
# FIGURE 7 (V2): Homotopic Phase-Time SEA Across All 5 Summary Engines & 8 Pillars
# ==============================================================================
def plot_07_homotopic_sea_engines(art: dict, theme: str) -> None:
    pal = get_palette(theme)
    fig = plt.figure(figsize=FIGSIZE, dpi=DPI)
    gs_top = fig.add_gridspec(1, 1, left=0.060, right=0.962, top=0.892, bottom=0.505)
    gs_bot = fig.add_gridspec(1, 2, left=0.060, right=0.962, top=0.405, bottom=0.068, wspace=0.33)

    add_header_footer(
        fig, pal,
        "Figure 7: Sector Homotopic Phase-Time Superposed Epoch Analysis (θ ∈ [-1, +1]) & Pillar Attribution",
        "Canonical Alignment of 180d Pre-Peak Buildup [-1, 0] and Peak-to-Trough Unwind [0, +1] Across All 12 Sector Dislocations (SD01–SD12)",
        "Proves why Sparse PCA & Mahalanobis lead sector peaks while Crash Damper Λ_{k,Crash} eliminates the 57.2% trough panic of naive indicators.",
    )

    hsea = art["homotopic_sea"]
    theta = np.array(hsea["theta"])

    # Panel A: Full-Width 5 Summary Engines + Naive Univariate Failure in Homotopic Phase-Time
    ax1 = fig.add_subplot(gs_top[0, 0])
    style_ax(ax1, pal)
    ax1.axvspan(-1.0, 0.0, color=pal["amber"], alpha=0.11, label="Phase I: Pre-Peak Bubble Buildup Window (180d → Peak θ = 0)")
    ax1.axvspan(0.0, 1.0, color=pal["crimson"], alpha=0.11, label="Phase II: Peak-to-Trough Crash Unwind (Peak θ = 0 → Trough θ = +1)")
    ax1.axvline(0.0, color=pal["axis"], lw=2.0, ls="-")
    ax1.axhline(70.0, color=pal["crimson"], lw=1.8, ls="--", label="Popperian Pre-Peak Warning Gate (70.0%)")
    ax1.axhline(25.0, color=pal["emerald"], lw=1.7, ls=":", label="Contrarian Trough Accumulation Floor (25.0%)")

    ax1.fill_between(theta, hsea["sec_master_p25"], hsea["sec_master_p75"], color=pal["blue"], alpha=0.20,
                     label="Sector Master I^{Sec*} Cross-Event IQR [25th–75th Pct]")
    ax1.plot(theta, hsea["spca_med"], "--", color=pal["purple"], lw=2.0, label="Sector Sparse PCA I^{SPCA} Median (Localized Coalition Leader)")
    ax1.plot(theta, hsea["mahal_med"], "-.", color=pal["crimson"], lw=2.0, label="Sector Precision Mahalanobis I^{Mahal} Median (Joint Tail Distance)")
    ax1.plot(theta, hsea["dfm_med"], ":", color=pal["amber"], lw=2.1, label="Sector State-Space Kalman DFM I^{DFM} Median")
    ax1.plot(theta, hsea["diff_med"], "--", color=pal["teal"], lw=1.8, label="Sector Copula-Rank Diffusion I^{Diff} Median")
    ax1.plot(theta, hsea["univ_raw_med"], "x--", markevery=12, color=pal["slate"], lw=1.9, ms=6,
             label="Failed Naive Univariate Sector Score (Stays Elevated at Troughs — DROPPED)")
    ax1.plot(theta, hsea["sec_master_med"], "-", color=pal["blue"], lw=3.2, label="Sector Master Composite I^{Sec*} Median Trajectory", zorder=7)

    ax1.annotate(
        "Cycle Peak Inflection (θ = 0):\nSPCA & Mahalanobis Saturate >80–99%\nMonths Ahead of Sector Top",
        xy=(-0.12, hsea["spca_med"][88]), xytext=(-0.62, 92),
        fontsize=8.0, fontweight="bold", color=pal["text"],
        bbox=dict(boxstyle="round,pad=0.32", facecolor=pal["card"], edgecolor=pal["purple"], lw=1.1),
        arrowprops=dict(arrowstyle="->", color=pal["purple"], lw=1.5),
    )
    ax1.annotate(
        "Exact Sector Trough (θ = +1):\nI^{Sec*} Resets to 0.0%–1.8% (<25%)\nvs. Naive Univariate Stuck High!",
        xy=(0.98, hsea["sec_master_med"][-1]), xytext=(0.45, 58),
        fontsize=8.0, fontweight="bold", color=pal["text"],
        bbox=dict(boxstyle="round,pad=0.32", facecolor=pal["card_green"], edgecolor=pal["emerald"], lw=1.1),
        arrowprops=dict(arrowstyle="->", color=pal["emerald"], lw=1.5),
    )

    ax1.set_xlim(-1.0, 1.0)
    ax1.set_ylim(-4, 108)
    ax1.set_xticks([-1.0, -0.75, -0.50, -0.25, 0.0, 0.25, 0.50, 0.75, 1.0])
    ax1.set_xticklabels(["θ=-1.0\n(-180d)", "-0.75\n(-135d)", "-0.50\n(-90d)", "-0.25\n(-45d)",
                         "θ=0.0\n[PEAK]", "+0.25\n(25% DD)", "+0.50\n(Mid-Crash)", "+0.75\n(75% DD)", "θ=+1.0\n[TROUGH]"],
                        fontsize=8.1, fontweight="bold")
    ax1.set_ylabel("Composite Regime Score (%)", fontsize=9.5, fontweight="bold", color=pal["text"])
    ax1.set_title("A. Canonical Phase-Time Trajectory Across All 5 Summary Engines (SD01–SD12 Cross-Event Median & IQR)",
                  fontsize=10.5, fontweight="bold", color=pal["text"], pad=8)
    ax1.legend(loc="lower left", ncol=2, fontsize=7.3, framealpha=0.93, facecolor=pal["bg"], edgecolor=pal["grid"], labelcolor=pal["text"])

    # Panel B: Class I Systemic Contagion vs. Class II Asynchronous Idiosyncratic Sector Busts
    ax2 = fig.add_subplot(gs_bot[0, 0])
    style_ax(ax2, pal)
    ax2.axvline(0.0, color=pal["axis"], lw=1.6)
    ax2.axhline(70.0, color=pal["crimson"], ls="--", lw=1.4)
    ax2.axhline(25.0, color=pal["emerald"], ls=":", lw=1.3)
    ax2.plot(theta, hsea["class1_sec_mean"], "-", color=pal["blue"], lw=2.6, label="Class I Systemic Contagion: Sector I^{Sec*} Mean (7 Events)")
    ax2.plot(theta, hsea["class2_sec_mean"], "-", color=pal["emerald"], lw=2.6, label="Class II Idiosyncratic Fractures: Sector I^{Sec*} Mean (5 Events)")
    ax2.plot(theta, hsea["class2_broad_mean"], "--", color=pal["crimson"], lw=2.0,
             label="Broad SPY I^* During Class II Sector Busts (Fails Trough Reset!)")
    ax2.fill_between(theta, hsea["class2_sec_p25"], hsea["class2_sec_p75"], color=pal["emerald"], alpha=0.15)
    ax2.set_xlim(-1.0, 1.0)
    ax2.set_ylim(-4, 105)
    ax2.set_xlabel("Normalized Homotopic Phase-Time θ ∈ [-1, +1]", fontsize=9.0, fontweight="bold", color=pal["text"])
    ax2.set_ylabel("Mean Dislocation Score (%)", fontsize=9.1, fontweight="bold", color=pal["text"])
    ax2.set_title("B. Class I Systemic vs. Class II Asynchronous Busts (Why Broad I^* Alone Fails)", fontsize=10.1, fontweight="bold", color=pal["text"], pad=8)
    ax2.legend(loc="lower left", fontsize=7.3, framealpha=0.93, facecolor=pal["bg"], edgecolor=pal["grid"], labelcolor=pal["text"])

    # Panel C: 20-Year Pillar Attribution & Dual-Taxonomy Orthogonal Tolerance (S_6^⊥ vs. T5)
    ax3 = fig.add_subplot(gs_bot[0, 1])
    style_ax(ax3, pal)
    ax3_t = ax3.twiny()
    p_attr = art["pillar_20yr_attribution"]
    yp = np.arange(len(p_attr))[::-1]
    p_names_short = [r["name"] for r in p_attr]
    u95_vals = [r["mean_pre_peak_u95"] for r in p_attr]
    freq_vals = [r["coalition_freq_pct"] / 50.0 for r in p_attr]  # scaled to [0..2] on bottom x-axis for clean comparison
    tau6 = [r["tau_mean_6s"] for r in p_attr]
    tau7 = [r["tau_mean_7s"] for r in p_attr]

    b_u = ax3.barh(yp + 0.16, u95_vals, height=0.30, color=pal["blue"], alpha=0.86, label="Mean Pre-Peak 95p Intensity u_{k,j} (σ) [Bottom X]")
    ax3.barh(yp - 0.16, freq_vals, height=0.30, color=pal["amber"], alpha=0.82, label="Pre-Peak Active Coalition Share (÷50, e.g. 2.0 = 100%) [Bottom X]")
    for b, r_row in zip(b_u, p_attr):
        ax3.text(b.get_width() + 0.04, b.get_y() + b.get_height() / 2,
                 f"{r_row['mean_pre_peak_u95']:.2f}σ ({r_row['coalition_freq_pct']:.0f}%)",
                 va="center", ha="left", fontsize=7.2, fontweight="bold", color=pal["text"])

    ax3_t.plot(tau6, yp, "o-", color=pal["emerald"], lw=1.9, ms=6, label="S_6^⊥ Mean Tolerance τ̄_6 (≥0.974) [Top X]")
    ax3_t.plot(tau7, yp, "D--", color=pal["purple"], lw=1.7, ms=5.5, label="T5 Mean Tolerance τ̄_7 (≥0.973) [Top X]")
    ax3_t.axvline(0.87, color=pal["crimson"], ls="--", lw=1.6)
    ax3_t.set_xlim(0.84, 1.015)
    ax3_t.tick_params(colors=pal["emerald"], labelsize=8.0)
    ax3_t.set_xlabel("Orthogonal Tolerance τ̄ = 1/VIF (Mandatory Gate ≥ 0.87)", fontsize=8.4, fontweight="bold", color=pal["emerald"])

    ax3.set_yticks(yp)
    ax3.set_yticklabels(p_names_short, fontsize=8.0, fontweight="bold")
    ax3.set_xlim(0, 2.48)
    ax3.set_xlabel("Pre-Peak Orthant Intensity (σ) / Scaled Coalition Share", fontsize=8.8, fontweight="bold", color=pal["text"])
    ax3.set_title("C. 20-Year Pillar Attribution & S_6^⊥ vs. T5 Tolerance Audit", fontsize=10.1, fontweight="bold", color=pal["text"], pad=22)

    h_a, l_a = ax3.get_legend_handles_labels()
    h_b, l_b = ax3_t.get_legend_handles_labels()
    ax3.legend(h_a + h_b, l_a + l_b, loc="lower right", fontsize=6.8, framealpha=0.93, facecolor=pal["bg"], edgecolor=pal["grid"], labelcolor=pal["text"])

    save_exact_huxga(fig, PLOTS_DIR / f"07_Sector_5Engines_Homotopic_SEA_{theme}.png", pal["bg"])


# ==============================================================================
# FIGURE 8 (V3): Head-to-Head S_6^⊥ (6-Sleeve) vs. T5 (7-Sleeve XLY Split)
# ==============================================================================
def plot_08_6sleeve_vs_7sleeve_xly(df_ts: pd.DataFrame, art: dict, theme: str) -> None:
    pal = get_palette(theme)
    fig = plt.figure(figsize=FIGSIZE, dpi=DPI)
    gs = fig.add_gridspec(2, 2, height_ratios=[1.15, 1.0], left=0.060, right=0.962, top=0.892, bottom=0.068, hspace=0.31, wspace=0.22)

    add_header_footer(
        fig, pal,
        "Figure 8: Co-Primary Taxonomy Diagnostic — S_6^⊥ (6-Sleeve) vs. T5 / S_7^⊥ (Granular 7-Sleeve Splitting XLY)",
        "Structural Decoupling of Compute & Digital Platforms (XLK/XLC, 26%) from Household Consumer Discretionary (XLY, 10%) Over 2006–2026",
        "T5 maximizes regime attribution & drawdown spanning (98.20%), while S_6^⊥ maximizes GFC bear-rally whipsaw immunity (-19.66% vs. -25.11% MaxDD).",
    )

    dates = df_ts.index
    # Panel A: 20-Year Dislocation Envelope Divergence — T5-S1 (XLK/XLC) vs T5-S2 (XLY) vs S6-S1 Merged
    ax1 = fig.add_subplot(gs[0, :])
    style_ax(ax1, pal)
    env_s6 = smooth_envelope(df_ts["Score_S1_Tech_Growth"].to_numpy())
    env_t5_tech = smooth_envelope(df_ts["Score_T5_S1_Compute_Digital"].to_numpy())
    env_t5_xly = smooth_envelope(df_ts["Score_T5_S2_Consumer_Disc"].to_numpy())

    ax1.axhline(70.0, color=pal["crimson"], lw=1.7, ls="--", label="Critical Pre-Peak Warning Gate (70.0%)")
    ax1.axhline(25.0, color=pal["emerald"], lw=1.5, ls=":", label="Contrarian Trough Floor (25.0%)")
    ax1.fill_between(dates, env_t5_tech, env_t5_xly, color=pal["purple"], alpha=0.14,
                     label="Compute (XLK/XLC) vs. Consumer (XLY) Regime Divergence Spread")
    ax1.plot(dates, env_t5_tech, color=pal["blue"], lw=2.3, label="T5-S1: Secular Compute & Digital (XLK/XLC, 26% Base | Live Nov'26 = 45.3%)")
    ax1.plot(dates, env_t5_xly, color=pal["crimson"], lw=2.1, label="T5-S2: Household Consumer Discretionary (XLY Solo, 10% Base | Live Nov'26 = 61.8%)")
    ax1.plot(dates, env_s6, color=pal["emerald"], ls="--", lw=1.8, alpha=0.90, label="S_6^⊥-S1: Merged Growth Sleeve (XLK/XLC/XLY, 36% Base | Live Nov'26 = 68.4%)")

    # Key structural annotations
    i_21 = dates.get_indexer([pd.Timestamp("2021-11-19")], method="nearest")[0]
    ax1.annotate(
        "Q4 2021 Stimulus Goods Mania:\nXLY Hits 97.5% (vs. 77.1% XLK)\n→ XLY Crashes -36.3% in 2022!",
        xy=(dates[i_21], env_t5_xly[i_21]), xytext=(pd.Timestamp("2015-06-01"), 9.5),
        fontsize=7.5, fontweight="bold", color=pal["text"],
        bbox=dict(boxstyle="round,pad=0.28", facecolor=pal["card_red"], edgecolor=pal["crimson"], lw=1.0),
        arrowprops=dict(arrowstyle="->", color=pal["crimson"], lw=1.4),
    )
    i_08 = dates.get_indexer([pd.Timestamp("2008-09-08")], method="nearest")[0]
    ax1.annotate(
        "Sep 2008 Oil-Drop Bounce:\nSolo XLY Briefly Exits Shield\nBefore Lehman (S_6^⊥ Stays Shielded!)",
        xy=(dates[i_08], env_t5_xly[i_08]), xytext=(pd.Timestamp("2009-07-01"), 83),
        fontsize=7.4, fontweight="bold", color=pal["text"],
        bbox=dict(boxstyle="round,pad=0.28", facecolor=pal["card"], edgecolor=pal["amber"], lw=1.0),
        arrowprops=dict(arrowstyle="->", color=pal["amber"], lw=1.4),
    )
    ax1.annotate(
        "Nov 2026 Live Split:\nCompute = 45.3% (Healthy)\nConsumer XLY = 61.8% (Watch)",
        xy=(dates[-1], env_t5_tech[-1]), xytext=(pd.Timestamp("2022-09-01"), 9.5),
        fontsize=7.5, fontweight="bold", color=pal["text"],
        bbox=dict(boxstyle="round,pad=0.28", facecolor=pal["card_blue"], edgecolor=pal["blue"], lw=1.0),
        arrowprops=dict(arrowstyle="->", color=pal["blue"], lw=1.4),
    )

    ax1.set_xlim(dates[0], dates[-1])
    ax1.set_ylim(-3, 108)
    ax1.xaxis.set_major_locator(mdates.YearLocator(2))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax1.set_ylabel("Smooth Dislocation Envelope (%)", fontsize=9.3, fontweight="bold", color=pal["text"])
    ax1.set_title("A. 20-Year Dislocation Trajectory Divergence: Compute/Cloud (XLK/XLC) vs. Household Consumer (XLY)",
                  fontsize=10.4, fontweight="bold", color=pal["text"], pad=8)
    ax1.legend(loc="upper left", ncol=2, fontsize=7.3, framealpha=0.93, facecolor=pal["bg"], edgecolor=pal["grid"], labelcolor=pal["text"])

    # Panel B: Head-to-Head Structural & Portfolio Scorecard Bar Comparison
    ax2 = fig.add_subplot(gs[1, 0])
    style_ax(ax2, pal)
    bt_irx = art["backtest_summary"]["irx"]
    cats = [
        "1d Return\nSpanning R²",
        "21d Regime\nSpanning R²",
        "Drawdown\nSpanning R²",
        "Orthogonal\nτ_min^⊥",
        "Compute\nBasis τ_min",
        "M4 Shield\nSharpe",
        "M4 Preservation\n(1 - |MaxDD|)",
    ]
    v6 = [0.9272, 0.9357, 0.9744, 0.9953, 0.9637, bt_irx["M4_Fiduciary_6S"]["sharpe"], 1.0 - abs(bt_irx["M4_Fiduciary_6S"]["max_dd"]) / 100.0]
    v7 = [0.9421, 0.9516, 0.9820, 0.9936, 0.9694, bt_irx["M4_Fiduciary_7S"]["sharpe"], 1.0 - abs(bt_irx["M4_Fiduciary_7S"]["max_dd"]) / 100.0]
    xc = np.arange(len(cats))
    b6 = ax2.bar(xc - 0.18, v6, width=0.35, color=pal["emerald"], label="S_6^⊥: Optimal 6-Sleeve (Parsimony & Defense Leader, γ = 0.96)")
    b7 = ax2.bar(xc + 0.18, v7, width=0.35, color=pal["blue"], label="T5 / S_7^⊥: Granular 7-Sleeve (Spanning & Attribution Leader, γ = 0.94)")
    for b in b6:
        ax2.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.012, f"{b.get_height():.3f}" if b.get_height() > 0.85 else f"{b.get_height():.2f}",
                 ha="center", va="bottom", fontsize=6.7, fontweight="bold", color=pal["emerald"])
    for b in b7:
        ax2.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.012, f"{b.get_height():.3f}" if b.get_height() > 0.85 else f"{b.get_height():.2f}",
                 ha="center", va="bottom", fontsize=6.7, fontweight="bold", color=pal["blue"])
    ax2.axhline(0.87, color=pal["crimson"], ls="--", lw=1.6, label="0.87 Spanning / Tolerance Gate (100% Pass on Columns 1–5)")
    ax2.set_xticks(xc)
    ax2.set_xticklabels(cats, fontsize=7.4, fontweight="bold")
    ax2.set_ylim(0.55, 1.06)
    ax2.set_ylabel("Normalized Metric / Ratio", fontsize=9.1, fontweight="bold", color=pal["text"])
    ax2.set_title("B. Head-to-Head Structural & Fiduciary Trade-Off: S_6^⊥ vs. T5", fontsize=10.1, fontweight="bold", color=pal["text"], pad=8)
    ax2.legend(loc="lower left", fontsize=7.1, framealpha=0.93, facecolor=pal["bg"], edgecolor=pal["grid"], labelcolor=pal["text"])

    # Panel C: T5 (7-Sleeve) M4 Dynamic Portfolio Allocation Stackplot
    ax3 = fig.add_subplot(gs[1, 1])
    style_ax(ax3, pal)
    w7_cols = [
        ("S7_Weight_T5_S1_Compute_Digital", "T5-S1: Compute XLK/XLC (26%)", pal["blue"]),
        ("S7_Weight_T5_S2_Consumer_Disc", "T5-S2: Consumer XLY (10%)", pal["pink"]),
        ("S7_Weight_T5_S3_Industrial_CapEx", "T5-S3: Industrials XLI/XLB (12%)", pal["purple"]),
        ("S7_Weight_T5_S4_Energy_Supply", "T5-S4: Energy XLE (7%)", pal["amber"]),
        ("S7_Weight_T5_S5_Financial_Credit", "T5-S5: Financials XLF (15%)", pal["teal"]),
        ("S7_Weight_T5_S6_Rate_RealEstate", "T5-S6: REIT/Util XLRE/XLU (8%)", pal["crimson"]),
        ("S7_Weight_T5_S7_Defensive_Quality", "T5-S7: Health/Staples (22%)", pal["emerald"]),
        ("S7_Weight_Cash", "3M T-Bill Shield Reserve", "#94A3B8" if theme == "white" else "#475569"),
    ]
    ys7 = [df_ts[c].to_numpy() for c, _, _ in w7_cols]
    ax3.stackplot(dates, ys7, labels=[lbl for _, lbl, _ in w7_cols], colors=[col for _, _, col in w7_cols], alpha=0.86)
    ax3.set_ylim(0, 100)
    ax3.set_xlim(dates[0], dates[-1])
    ax3.xaxis.set_major_locator(mdates.YearLocator(3))
    ax3.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax3.set_ylabel("T5 7-Sleeve Allocation (%)", fontsize=9.1, fontweight="bold", color=pal["text"])
    ax3.set_title("C. T5 (7-Sleeve) M4 Dynamic Allocation (148.7%/yr Turnover; Independent XLY Shielding)", fontsize=10.0, fontweight="bold", color=pal["text"], pad=8)
    ax3.legend(loc="lower left", ncol=2, fontsize=6.6, framealpha=0.92, facecolor=pal["bg"], edgecolor=pal["grid"], labelcolor=pal["text"])

    save_exact_huxga(fig, PLOTS_DIR / f"08_6Sleeve_vs_7Sleeve_XLY_Diagnostic_{theme}.png", pal["bg"])


# ==============================================================================
# FIGURE 9 (V4): 20-Year Cross-Sectional Regime Thermogram & Indicator Scorecard
# ==============================================================================
def plot_09_20yr_regime_thermogram(df_ts: pd.DataFrame, art: dict, theme: str) -> None:
    pal = get_palette(theme)
    fig = plt.figure(figsize=FIGSIZE, dpi=DPI)
    gs_top = fig.add_gridspec(1, 1, left=0.215, right=0.965, top=0.892, bottom=0.510)
    gs_bot = fig.add_gridspec(1, 2, left=0.060, right=0.962, top=0.415, bottom=0.068, wspace=0.22)

    add_header_footer(
        fig, pal,
        "Figure 9: 20-Year Cross-Sectional Dislocation Thermogram & Executive Indicator Performance Compendium",
        "Panoramic Regime Strip (2006–2026) Across Broad SPY (I^*) & All 7 Granular Sleeves (T5 / S_6^⊥) + 20-Year Summary Engine Scorecard",
        "Vertical crimson bands reveal synchronous systemic contagion (2008, 2020, 2022); isolated horizontal hotspots reveal asynchronous sector bubbles.",
    )

    # Panel A: 8 x 250 Biweekly-Pooled 20-Year Regime Thermogram
    ax1 = fig.add_subplot(gs_top[0, 0])
    style_ax(ax1, pal)
    strip_cols = [
        ("Broad_I_Star", "Broad Market SPY (I^*) [Live: 45.4%]"),
        ("Score_T5_S1_Compute_Digital", "T5-S1: Compute XLK/XLC [Live: 45.3%]"),
        ("Score_T5_S2_Consumer_Disc", "T5-S2: Consumer XLY [Live: 61.8%]"),
        ("Score_T5_S3_Industrial_CapEx", "S2/T5-S3: Industrials XLI/XLB [Live: 63.8%]"),
        ("Score_T5_S4_Energy_Supply", "S3/T5-S4: Energy XLE [Live: 48.6%]"),
        ("Score_T5_S5_Financial_Credit", "S4/T5-S5: Financials XLF [Live: 72.8%]"),
        ("Score_T5_S6_Rate_RealEstate", "S5/T5-S6: REIT/Util XLRE/XLU [Live: 16.5%]"),
        ("Score_T5_S7_Defensive_Quality", "S6/T5-S7: Health/Staples [Live: 73.7%]"),
    ]
    # Resample to monthly-half / 10-business-day smooth regime windows for razor-sharp visual legibility
    df_strip = pd.DataFrame({c: smooth_envelope(df_ts[c].to_numpy()) for c, _ in strip_cols}, index=df_ts.index)
    df_biwk = df_strip.resample("2W").max()
    mat_t = df_biwk.to_numpy().T  # (8, ~545)

    cmap_thermo = LinearSegmentedColormap.from_list(
        "regime_thermo",
        [(0.00, "#059669"), (0.25, "#34D399"), (0.50, "#F8FAFC" if theme == "white" else "#1E293B"),
         (0.70, "#F59E0B"), (0.85, "#EF4444"), (1.00, "#7F1D1D")],
    )
    x_num = mdates.date2num(df_biwk.index.to_pydatetime())
    im = ax1.imshow(
        mat_t, cmap=cmap_thermo, vmin=0.0, vmax=100.0, aspect="auto",
        extent=[x_num[0], x_num[-1], len(strip_cols) - 0.5, -0.5], interpolation="nearest",
    )
    ax1.grid(False)
    ax1.axhline(0.5, color=pal["axis"], lw=1.8, ls="--")
    ax1.axhline(2.5, color=pal["cyan"], lw=1.3, ls=":")
    ax1.set_yticks(range(len(strip_cols)))
    ax1.set_yticklabels([lbl for _, lbl in strip_cols], fontsize=8.0, fontweight="bold")
    ax1.xaxis_date()
    ax1.xaxis.set_major_locator(mdates.YearLocator(2))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

    cbar = fig.colorbar(im, ax=ax1, fraction=0.022, pad=0.015)
    cbar.set_label("Smooth Dislocation Envelope (%)  [<25% Value | ≥70% Bubble]", fontsize=8.2, fontweight="bold", color=pal["text"])
    cbar.ax.tick_params(labelsize=8.0, colors=pal["text"])
    ax1.set_title(
        "A. 20-Year Cross-Sectional Dislocation Regime Thermogram (Top Row: Systemic SPY I^*; Rows 2–3 Merge into S_6^⊥-S1; Rows 2–8 = Full T5 7-Sleeve)",
        fontsize=10.2, fontweight="bold", color=pal["text"], pad=8,
    )

    # Panel B: 20-Year Executive Performance Scorecard of the 5 Summary Indicator Engines
    ax2 = fig.add_subplot(gs_bot[0, 0])
    style_ax(ax2, pal)
    evs = art["event_study_12"]
    eng_names = ["Master\nI^{Sec*}", "Sparse PCA\nI^{SPCA}", "Mahalanobis\nI^{Mahal}", "Kalman DFM\nI^{DFM}", "Copula Diff\nI^{Diff}", "Naive Univ\n[DROPPED]"]
    pre_means = [
        float(np.mean([e["sec_pre_max"] for e in evs])),
        float(np.mean([e["spca_pre"] for e in evs])),
        float(np.mean([e["mahal_pre"] for e in evs])),
        float(np.mean([e["dfm_pre"] for e in evs])),
        float(np.mean([e["diff_pre"] for e in evs])),
        78.4,
    ]
    sep_means = [
        float(np.mean([e["sec_sep"] for e in evs])),
        float(np.mean([e["spca_pre"] - e["sec_trough_min"] for e in evs])),
        float(np.mean([e["mahal_pre"] - e["sec_trough_min"] for e in evs])),
        float(np.mean([e["dfm_pre"] - e["sec_trough_min"] for e in evs])),
        float(np.mean([e["diff_pre"] - e["sec_trough_min"] for e in evs])),
        78.4 - float(np.mean([e["univ_trough_max"] for e in evs])),
    ]
    gammas = [95.0, 95.0, 95.0, 93.0, 91.0, 66.0]

    xe = np.arange(len(eng_names))
    w_e = 0.26
    ax2.bar(xe - w_e, pre_means, width=w_e, color=pal["blue"], label="12-Event Pre-Peak Sensitivity Mean (%)")
    b_sep = ax2.bar(xe, sep_means, width=w_e, color=pal["emerald"], label="Peak-to-Trough Separation Δ (%)")
    b_gam = ax2.bar(xe + w_e, gammas, width=w_e, color=pal["purple"], label="Epistemological Confidence Score (γ × 100)")
    ax2.axhline(87.0, color=pal["crimson"], ls="--", lw=1.8, label="Mandatory 87.0% (γ = 0.87) Quality Cutoff")
    for b in b_sep:
        ax2.text(b.get_x() + b.get_width() / 2, b.get_height() + 1.5, f"{b.get_height():.1f}%", ha="center", va="bottom", fontsize=6.9, fontweight="bold", color=pal["emerald"])
    for b in b_gam:
        ax2.text(b.get_x() + b.get_width() / 2, b.get_height() + 1.5, f"{b.get_height()/100:.2f}", ha="center", va="bottom", fontsize=6.8, fontweight="bold", color=pal["purple"])
    ax2.set_xticks(xe)
    ax2.set_xticklabels(eng_names, fontsize=7.7, fontweight="bold")
    ax2.set_ylim(0, 114)
    ax2.set_ylabel("20-Year Empirical Score (%)", fontsize=9.1, fontweight="bold", color=pal["text"])
    ax2.set_title("B. 20-Year Executive Scorecard Across the 5 Summary Indicator Engines", fontsize=10.1, fontweight="bold", color=pal["text"], pad=8)
    ax2.legend(loc="lower left", fontsize=7.1, framealpha=0.93, facecolor=pal["bg"], edgecolor=pal["grid"], labelcolor=pal["text"])

    # Panel C: Systemic SPY (8 Dislocations) vs. Cross-Sector (12 Dislocations & S_6^⊥ / T5 Shields) Executive Synthesis
    ax3 = fig.add_subplot(gs_bot[0, 1])
    style_ax(ax3, pal)
    bt_irx = art["backtest_summary"]["irx"]
    comp_lbls = [
        "Hit Rate\n(D1–8 / SD1–12)",
        "Peak–Trough\nSeparation (%)",
        "1-Yr Lead\nRunway (% Yr)",
        "MaxDD Capital\nPreserved (%)",
        "Portfolio Sharpe\n(×100 IRX)",
    ]
    v_sys = [100.0, 93.2, 225.2 / 252.0 * 100.0, 100.0 - 23.48, bt_irx["BroadOnly_Defensive"]["sharpe"] * 100.0]
    v_s6 = [100.0, 90.8, 217.8 / 252.0 * 100.0, 100.0 - abs(bt_irx["M4_Fiduciary_6S"]["max_dd"]), bt_irx["M4_Fiduciary_6S"]["sharpe"] * 100.0]
    v_t5 = [100.0, 90.8, 217.8 / 252.0 * 100.0, 100.0 - abs(bt_irx["M4_Fiduciary_7S"]["max_dd"]), bt_irx["M4_Fiduciary_7S"]["sharpe"] * 100.0]

    xk = np.arange(len(comp_lbls))
    ax3.bar(xk - 0.25, v_sys, width=0.24, color=pal["teal"], label="Tier-1 Systemic Master I^* (8 Broad Dislocations)")
    b_6 = ax3.bar(xk, v_s6, width=0.24, color=pal["emerald"], label="S_6^⊥ 6-Sleeve Sector Architecture (12 Sector Busts)")
    b_7 = ax3.bar(xk + 0.25, v_t5, width=0.24, color=pal["blue"], label="T5 7-Sleeve Granular Architecture (Standalone XLY)")
    for b in b_6:
        ax3.text(b.get_x() + b.get_width() / 2, b.get_height() + 1.4, f"{b.get_height():.1f}", ha="center", va="bottom", fontsize=6.9, fontweight="bold", color=pal["emerald"])
    for b in b_7:
        ax3.text(b.get_x() + b.get_width() / 2, b.get_height() + 1.4, f"{b.get_height():.1f}", ha="center", va="bottom", fontsize=6.9, fontweight="bold", color=pal["blue"])
    ax3.set_xticks(xk)
    ax3.set_xticklabels(comp_lbls, fontsize=7.6, fontweight="bold")
    ax3.set_ylim(0, 114)
    ax3.set_ylabel("20-Year Benchmark Metric (0–100 Scale)", fontsize=9.1, fontweight="bold", color=pal["text"])
    ax3.set_title("C. Unified 20-Year Synthesis: Systemic I^* vs. S_6^⊥ (6-Sleeve) & T5 (7-Sleeve)", fontsize=10.0, fontweight="bold", color=pal["text"], pad=8)
    ax3.legend(loc="lower right", fontsize=7.1, framealpha=0.93, facecolor=pal["bg"], edgecolor=pal["grid"], labelcolor=pal["text"])

    save_exact_huxga(fig, PLOTS_DIR / f"09_20Yr_Cross_Sector_Regime_Thermogram_{theme}.png", pal["bg"])


def main() -> None:
    with open(DATA_DIR / "empirical_study_results.json", encoding="utf-8") as f:
        art = json.load(f)
    df_ts = pd.read_parquet(DATA_DIR / "plot_timeseries_2006_2026.parquet")
    df_m = pd.read_parquet(DATA_DIR / "sector_master_panel_1999_2026.parquet")

    for theme in ("white", "black"):
        print(f"Rendering all 9 4K HUXGA (6400 x 4800) figures for theme={theme}...")
        plot_01_taxonomy_pareto(art, df_m, theme)
        plot_02_flagship_trajectories(df_ts, art, theme)
        plot_03_popperian_matrix(art, theme)
        plot_04_etf_vs_single_stocks(art, theme)
        plot_05_signal_mapping_backtest(df_ts, art, theme)
        plot_06_8pillar_coalition_anatomy(df_ts, art, theme)
        plot_07_homotopic_sea_engines(art, theme)
        plot_08_6sleeve_vs_7sleeve_xly(df_ts, art, theme)
        plot_09_20yr_regime_thermogram(df_ts, art, theme)
    print("All 18 High-Resolution 4K HUXGA (6400 x 4800, 4:3) PNG visualizations generated and verified!")


if __name__ == "__main__":
    main()
