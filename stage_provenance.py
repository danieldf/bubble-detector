"""
Pre-compilation and staging script for provenance and WASM Parquet datasets.
"""

from pathlib import Path
from bubble_detector.config import PROVENANCE_DIR, BASE_DIR, CACHE_DIR, logger
from bubble_detector.data.etl_shiller import ShillerETL
from bubble_detector.data.etl_fred import FredETL
from bubble_detector.data.etl_finra import FinraETL
from bubble_detector.data.etl_vxo import VxoETL
from bubble_detector.ui.panel_dashboard import precompile_wasm_parquet_datasets

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

    print("All provenance and WASM Parquet datasets successfully staged!")

if __name__ == "__main__":
    stage_all()
