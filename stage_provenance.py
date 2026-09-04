"""
Provenance Data Staging & WebAssembly Binary Pre-Compilation Pipeline.
=====================================================================

Institutional Data Lineage & Build Architecture:
------------------------------------------------
This build automation script orchestrates the end-to-end extraction, verification,
and binary serialization of authentic macroeconomic and financial time series:

1. Provenance ETL Orchestration:
   - ShillerETL: Robert Shiller S&P Composite, CAPE, real earnings, dividends, and CPI (1871–present).
   - FredETL: Nominal GDP (quarterly, 60d lag) and Case-Shiller Housing Price-to-Income (monthly, 60d lag).
   - FinraETL: FINRA customer margin debit balances + NYSE historical archives (1959–present, 21d lag).
   - VxoETL: CBOE VXO daily quotes capturing the 1987 Black Monday peak (150.19) and modern VIX.

2. WebAssembly Dual-Format Serialization (Parquet & JSON MEMFS):
   - Pre-compiles full historical market data into zero-copy Apache Arrow Parquet files.
   - Converts core feature columns into lightweight JSON format (`market_data_50yr.json`, `market_data_modern.json`).
   - Replicates compiled datasets across `build/`, `dist/`, and `data/provenance/` directories,
     enabling instant synchronous loading inside Pyodide's virtual Emscripten filesystem.
"""

from pathlib import Path
from bubble_detector.config import PROVENANCE_DIR, BASE_DIR, CACHE_DIR, logger
from bubble_detector.data.etl_shiller import ShillerETL
from bubble_detector.data.etl_fred import FredETL
from bubble_detector.data.etl_finra import FinraETL
from bubble_detector.data.etl_vxo import VxoETL
from bubble_detector.ui.panel_dashboard import precompile_wasm_parquet_datasets, CORE_WASM_COLUMNS

def sync_parquet_to_json():
    """Convert existing staged Parquet datasets into clean JSON tables for WebAssembly MEMFS."""
    import json
    import numpy as np
    import polars as pl
    
    build_dir = BASE_DIR / "build"
    dist_dir = BASE_DIR / "dist"
    build_dir.mkdir(parents=True, exist_ok=True)
    dist_dir.mkdir(parents=True, exist_ok=True)
    PROVENANCE_DIR.mkdir(parents=True, exist_ok=True)
    
    mapping = [
        ("market_data_50yr.parquet", "market_data_50yr.json"),
        ("market_data_modern.parquet", "market_data_modern.json"),
    ]
    for p_name, j_name in mapping:
        p_path = PROVENANCE_DIR / p_name
        if not p_path.exists():
            p_path = build_dir / p_name
        if p_path.exists():
            df = pl.read_parquet(p_path)
            target_cols = [c for c in CORE_WASM_COLUMNS if c in df.columns]
            json_dict = {}
            for col in target_cols:
                if col == "Date":
                    json_dict["Date"] = [str(d)[:10] for d in df["Date"].to_list()]
                elif col == "Primary_Anomaly_Driver" or df[col].dtype in (pl.Utf8, pl.String):
                    json_dict[col] = df[col].to_list()
                else:
                    vals = df[col].to_list()
                    json_dict[col] = [round(float(v), 5) if (v is not None and not np.isnan(v)) else 0.0 for v in vals]
            for target_dir in [build_dir, PROVENANCE_DIR, dist_dir]:
                with open(target_dir / j_name, "w", encoding="utf-8") as f:
                    json.dump(json_dict, f)
                if not (target_dir / p_name).exists() or target_dir != p_path.parent:
                    df.write_parquet(target_dir / p_name)
            print(f"Synced {p_name} to {j_name} across provenance, build, and dist directories.")

def stage_all():
    print("Staging Shiller monthly dataset...")
    s_etl = ShillerETL(PROVENANCE_DIR)
    s_etl.fetch_and_stage(force_refresh=True)

    print("Staging FRED macro dataset...")
    f_etl = FredETL(PROVENANCE_DIR)
    f_etl.fetch_and_stage(force_refresh=True)

    print("Staging FINRA margin debt dataset...")
    m_etl = FinraETL(PROVENANCE_DIR)
    m_etl.fetch_and_stage(force_refresh=True)

    print("Staging CBOE VXO dataset...")
    v_etl = VxoETL(PROVENANCE_DIR)
    v_etl.fetch_and_stage(force_refresh=True)

    print("Precompiling WASM Parquet datasets...")
    precompile_wasm_parquet_datasets()
    sync_parquet_to_json()

    print("All provenance and WASM Parquet datasets successfully staged!")

if __name__ == "__main__":
    stage_all()
