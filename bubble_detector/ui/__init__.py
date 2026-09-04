"""
User Interface & Presentation Layer Subpackage.
================================================

Architectural Scope & Dual Runtimes:
------------------------------------
This subpackage houses the dual-runtime presentation layer for the Bubble Detector platform:

1. Server-Side Desktop Workstation (`dashboard.py`):
   - Built on NiceGUI, FastAPI, and multithreaded Polars Arrow processing.
   - Hosts the 6 interactive analytical tabs with real-time reactive parameter recalculation.
   - Dynamic dark/light theme switching with automatic system preference detection.

2. Client-Side WebAssembly (WASM) Dashboard (`panel_dashboard.py`):
   - Pre-compiled via HoloViz Panel, Bokeh, and Plotly for execution under Pyodide WASM.
   - Runs 100% in-browser with zero remote servers, zero compute fees, and zero data leakage.
   - Mounts pre-staged datasets directly into Pyodide's virtual in-memory filesystem (MEMFS).

3. Accessible Component Library (`components.py`):
   - iOS 13+ card containers and tactile call-to-action (CTA) banners.
   - Dyslexia-friendly typography and WCAG 2.2 AA compliant contrast hierarchy.

4. Design System & Theme Engine (`theme.py`, alias for `ui_theme.py`):
   - 8px spatial rhythm grid.
   - Relative luminance and contrast ratio algorithms.
   - Standardized right-flushed vertical legend layouts (`x=1.01, y=1.0, margin.r=230`).

5. WebAssembly Distribution Postprocessor (`postprocess_wasm.py`):
   - Post-processes `dist/index.html` after `panel convert` builds.
   - Injects MEMFS pre-loader script, wheel normalization, unicode emoji decoders,
     and diagnostic browser error boundaries.
"""

from .dashboard import create_app, DashboardState
from .components import create_cta_banner, create_ios_card
from . import theme

__all__ = [
    "create_app",
    "DashboardState",
    "create_cta_banner",
    "create_ios_card",
    "theme",
]
