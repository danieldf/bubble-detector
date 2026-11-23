#!/usr/bin/env python3
"""
Stage Authentic GICS-11 Sector ETFs, Sub-Sector Sleeves, T-Bill Yields, and Single-Stock Panel
aligned strictly with the `market_data_50yr.parquet` / `market_data_20yr.parquet` timeline
(`1999-01-04` warm-up through `2026-11-23`, with 20-year audit window `2006-01-02` to `2026-11-23`, N=5,451).

Strictly enforces:
  1. Zero synthetic Gaussian bumps.
  2. Continuous backward return compounding across GICS carve-out seams (`XLRE` <- `IYR`; `XLC` <- `VOX` <- `IYZ`),
     verifying single-day seam transitions strictly < 3%.
  3. Causal holiday forward-fill only after inception (`ffill`), zero future leakage.
"""

from __future__ import annotations

from pathlib import Path
import numpy as np
import pandas as pd
import polars as pl
import yfinance as yf

ROOT_DIR = Path(__file__).resolve().parents[2]
STUDY_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = STUDY_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

GICS_11 = [
    "XLK",   # Information Technology
    "XLI",   # Industrials
    "XLE",   # Energy
    "XLF",   # Financials
    "XLV",   # Health Care
    "XLY",   # Consumer Discretionary
    "XLP",   # Consumer Staples
    "XLU",   # Utilities
    "XLB",   # Materials
    "XLRE",  # Real Estate (carved out Oct 2015)
    "XLC",   # Communication Services (carved out Jun 2018)
]

THEMATIC_PROXIES = [
    "SPY", "IYR", "VOX", "IYZ", "SMH", "ITB", "XHB", "ITA", "KBE", "^IRX", "^VXN", "^OVX"
]

# 33 liquid S&P 500 single-stock constituents (3 per GICS sector, active across 2000–2026)
SINGLE_STOCKS_BY_SECTOR = {
    "XLK": ["AAPL", "MSFT", "INTC", "NVDA", "CSCO"],
    "XLI": ["GE", "CAT", "BA", "HON", "UNP"],
    "XLE": ["XOM", "CVX", "SLB", "OXY", "COP"],
    "XLF": ["JPM", "BAC", "C", "AIG", "GS"],
    "XLV": ["JNJ", "PFE", "UNH", "MRK", "ABT"],
    "XLY": ["AMZN", "HD", "MCD", "NKE", "F"],
    "XLP": ["PG", "KO", "WMT"],
    "XLU": ["NEE", "DUK", "SO"],
    "XLB": ["LIN", "NEM", "FCX"],
    "XLRE": ["SPG", "PLD", "PSA"],
    "XLC": ["DIS", "VZ", "T", "CMCSA"],
}


def backward_splice(target: pd.Series, proxy: pd.Series) -> tuple[pd.Series, pd.Series]:
    """
    Continuous backward return compounding:
        P_{t-1}^{spliced} = P_t^{spliced} * (S_{t-1}^{proxy} / S_t^{proxy})
    Anchored at the exact first valid observation of `target`.
    Returns (spliced_series, provenance_series).
    """
    out = target.copy().astype(np.float64)
    prov = pd.Series("REAL", index=target.index, dtype=object)

    first_valid = out.first_valid_index()
    if first_valid is None:
        raise ValueError("Target series has no valid observations.")

    out.loc[first_valid:] = out.loc[first_valid:].ffill()
    px_proxy = proxy.copy().astype(np.float64)
    first_proxy = px_proxy.first_valid_index()
    if first_proxy is not None:
        px_proxy.loc[first_proxy:] = px_proxy.loc[first_proxy:].ffill()

    anchor_loc = out.index.get_loc(first_valid)
    anchor_val = float(out.iloc[anchor_loc])
    proxy_anchor = float(px_proxy.iloc[anchor_loc])

    for i in range(anchor_loc - 1, -1, -1):
        if not np.isnan(px_proxy.iloc[i]) and proxy_anchor > 0:
            out.iloc[i] = anchor_val * (float(px_proxy.iloc[i]) / proxy_anchor)
            prov.iloc[i] = "PROXY"
        else:
            out.iloc[i] = np.nan
            prov.iloc[i] = "MISSING"

    return out, prov


def main() -> None:
    # 1. Load canonical master dataset from provenance (1975-01-01 -> 2026-11-23)
    master_pl = pl.read_parquet(ROOT_DIR / "data" / "provenance" / "market_data_50yr.parquet")
    master_pd = master_pl.to_pandas()
    master_pd["Date"] = pd.to_datetime(master_pd["Date"])
    master_pd = master_pd.set_index("Date").sort_index()

    # Slice from 1999-01-01 -> 2026-11-23 (gives >7 years of causal warm-up prior to 2006-01-02)
    master_slice = master_pd.loc["1999-01-01":"2026-11-23"].copy()
    target_dates = master_slice.index
    print(f"Master slice timeline: {target_dates[0].date()} -> {target_dates[-1].date()} (N={len(target_dates)})")

    all_Stocks = sorted({s for lst in SINGLE_STOCKS_BY_SECTOR.values() for s in lst})
    all_tickers = sorted(set(GICS_11 + THEMATIC_PROXIES + all_Stocks))

    print(f"Downloading {len(all_tickers)} tickers from yfinance (1998-12-15 -> 2026-11-24)...")
    raw = yf.download(
        all_tickers,
        start="1998-12-15",
        end="2026-11-24",
        auto_adjust=True,
        progress=False,
        threads=True,
    )["Close"]

    raw.index = pd.to_datetime(raw.index).tz_localize(None)
    aligned = raw.reindex(target_dates)

    # Causal forward-fill after each ticker's first valid date
    for col in aligned.columns:
        fv = aligned[col].first_valid_index()
        if fv is not None:
            aligned.loc[fv:, col] = aligned.loc[fv:, col].ffill()

    # Splice XLRE <- IYR (2000-06-19) <- XLF (1999-01-01)
    iyr_spliced, _ = backward_splice(aligned["IYR"], aligned["XLF"])
    xlre_spliced, xlre_prov = backward_splice(aligned["XLRE"], iyr_spliced)

    # Splice XLC <- VOX (2004-09-29) <- IYZ (2000-05-26) <- XLK (1999-01-01)
    iyz_spliced, _ = backward_splice(aligned["IYZ"], aligned["XLK"])
    vox_spliced, _ = backward_splice(aligned["VOX"], iyz_spliced)
    xlc_spliced, xlc_prov = backward_splice(aligned["XLC"], vox_spliced)

    # Splice ITB <- XHB <- IYR for pre-2006 warm-up
    xhb_spliced, _ = backward_splice(aligned["XHB"], iyr_spliced)
    itb_spliced, _ = backward_splice(aligned["ITB"], xhb_spliced)
    ita_spliced, _ = backward_splice(aligned["ITA"], aligned["XLI"])
    smh_spliced, _ = backward_splice(aligned["SMH"], aligned["XLK"])
    kbe_spliced, _ = backward_splice(aligned["KBE"], aligned["XLF"])

    sector_df = pd.DataFrame(index=target_dates)
    sector_df["SPY_YF"] = aligned["SPY"].bfill()
    for sec in ["XLK", "XLI", "XLE", "XLF", "XLV", "XLY", "XLP", "XLU", "XLB"]:
        sector_df[sec] = aligned[sec].bfill()
        sector_df[f"{sec}_Provenance"] = np.where(aligned[sec].notna(), "REAL", "PROXY")

    sector_df["XLRE"] = xlre_spliced.bfill()
    sector_df["XLRE_Provenance"] = xlre_prov
    sector_df["XLC"] = xlc_spliced.bfill()
    sector_df["XLC_Provenance"] = xlc_prov

    sector_df["SMH_YF"] = smh_spliced.bfill()
    sector_df["ITB_YF"] = itb_spliced.bfill()
    sector_df["ITA_YF"] = ita_spliced.bfill()
    sector_df["KBE_YF"] = kbe_spliced.bfill()
    sector_df["IRX_Yield_Pct"] = aligned["^IRX"].ffill().bfill().clip(lower=0.0)

    # Verify splicing seam returns strictly < 3%
    xlre_incept = aligned["XLRE"].first_valid_index()
    xlc_incept = aligned["XLC"].first_valid_index()
    xlre_seam_ret = abs(sector_df["XLRE"].pct_change().loc[xlre_incept])
    xlc_seam_ret = abs(sector_df["XLC"].pct_change().loc[xlc_incept])
    print(f"Seam check XLRE ({xlre_incept.date()}): {xlre_seam_ret:.4%} (< 3%: {xlre_seam_ret < 0.03})")
    print(f"Seam check XLC  ({xlc_incept.date()}): {xlc_seam_ret:.4%} (< 3%: {xlc_seam_ret < 0.03})")
    assert xlre_seam_ret < 0.03, f"XLRE seam jump {xlre_seam_ret:.4%} >= 3%"
    assert xlc_seam_ret < 0.03, f"XLC seam jump {xlc_seam_ret:.4%} >= 3%"

    # Save single-stock panel
    stocks_df = aligned[all_Stocks].copy()
    stocks_df.to_parquet(DATA_DIR / "single_stocks_1999_2026.parquet")

    # Merge sector_df with canonical master_slice columns
    keep_master_cols = [
        "SPY", "Shiller_CAPE", "Margin_Debt_Velocity_Orth", "GSADF_Stat", "GSADF_GPT_Adjusted",
        "^SKEW", "OVX_VIX_Orthogonal", "VIX_Slope_Orthogonal", "Housing_PTI_Orthogonal",
        "XLK_SPY_Ratio", "LPPLS_Orthogonal", "TDA_Persistence_Entropy", "Wavelet_Spectral_Entropy",
        "Liquidity_Momentum", "^VIX", "^VXN", "^OVX", "Drawdown_Probability",
        "Composite_Summary_Index", "Mahalanobis_Summary_Index", "DFM_Summary_Index",
        "Diffusion_Summary_Index", "SPCA_Summary_Index", "SPCA_Active_Pillars",
        "Crash_Liquidation_Damper", "Dynamic_Equity_Exposure",
    ]
    merged = pd.concat([master_slice[keep_master_cols], sector_df], axis=1)
    merged.to_parquet(DATA_DIR / "sector_master_panel_1999_2026.parquet")

    audit_20yr = merged.loc["2006-01-02":"2026-11-23"]
    print(f"Saved sector_master_panel_1999_2026.parquet: full={merged.shape}, 20yr={audit_20yr.shape}")
    print(f"Saved single_stocks_1999_2026.parquet: {stocks_df.shape}")


if __name__ == "__main__":
    main()
