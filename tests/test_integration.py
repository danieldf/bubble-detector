"""
End-to-end integration test verifying data pipeline -> features -> model -> UI state.
"""

import pytest
import polars as pl
from bubble_detector.ui.dashboard import DashboardState

def test_full_system_integration(tmp_path):
    # Initialize Dashboard State which runs full pipeline
    state = DashboardState()

    assert isinstance(state.df, pl.DataFrame)
    assert len(state.df) > 0
    assert "Drawdown_Probability" in state.df.columns
    assert "Shiller_CAPE" in state.df.columns
    assert "GSADF_GPT_Adjusted" in state.df.columns

    # Verify theme mode and Plotly template
    assert state.theme_mode in {"light", "dark"}
    assert state.get_plotly_template() in {"plotly_white", "plotly_dark"}
