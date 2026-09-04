"""
Post-Processing Utility for Panel WebAssembly Compiled Artifacts (`dist/index.html`).
===================================================================================

WebAssembly Compilation & Virtual Filesystem Architecture:
----------------------------------------------------------
When compiling interactive Python dashboards to client-side WebAssembly via HoloViz Panel
(`panel convert bubble_detector/ui/panel_dashboard.py --to pyodide-worker --out dist/`),
the resulting static HTML file requires targeted post-processing to function seamlessly
in sandboxed browser runtimes:

1. In-Memory Virtual Filesystem (MEMFS) Pre-Loading:
   Standard browser Python cannot perform synchronous POSIX file I/O against remote web servers.
   This postprocessor injects an asynchronous JavaScript initialization routine that fetches
   the pre-staged JSON datasets (`market_data_50yr.json`, `market_data_modern.json`) and mounts
   them directly into Pyodide's virtual Emscripten filesystem (`pyodide.FS.writeFile`).
   When `panel_dashboard.py` executes, it reads these files instantly from local virtual memory.

2. Wheel Normalization:
   Normalizes version-pinned CDN wheel URLs to canonical package names recognized by Pyodide's
   built-in micropip installer, preventing CDN timeout and version mismatch failures.

3. Unicode Emoji Deserialization:
   Resolves Python-to-JavaScript string serialization artifacts where 32-bit Unicode characters
   (such as institutional icons and financial emojis) become corrupted into literal escape strings
   (e.g., `\\U0001f3db`).

4. Resilient Browser Error Boundary & Progressive Checklist:
   Standard Pyodide loading screens fail silently if a Python import or syntax error occurs.
   The injected error boundary intercepts exceptions during initialization and renders an
   informative diagnostic error panel with a retry action directly in the DOM.
"""

import re
from pathlib import Path

def postprocess_wasm_content(content: str) -> str:
    """
    Apply post-processing transformations to the HTML content string.
    Pure transformation with zero disk I/O, completely idempotent.
    """
    # 1. Normalize wheel URLs
    content = re.sub(r"'https://cdn\.holoviz\.org/panel/wheels/bokeh-[^']+\.whl'", "'bokeh'", content)
    content = re.sub(r"'https://cdn\.holoviz\.org/panel/[^']+/panel-[^']+\.whl'", "'panel'", content)

    # 2. Generic regex decoding for unicode escape sequences
    content = re.sub(r"\\+U0001([0-9a-fA-F]{4})", lambda m: chr(int("0001" + m.group(1), 16)), content)
    content = re.sub(r"U0001([0-9a-fA-F]{4})", lambda m: chr(int("0001" + m.group(1), 16)), content)

    # 3. Explicit emoji replacements
    replacements = {
        "U0001f3db": "🏛️",
        "\\U0001f3db": "🏛️",
        "U0001f3af": "🎯",
        "\\U0001f3af": "🎯",
        "U0001f52c": "🔬",
        "\\U0001f52c": "🔬",
        "U0001f4c5": "📅",
        "\\U0001f4c5": "📅",
        "U0001f4c9": "📉",
        "\\U0001f4c9": "📉",
        "U0001f680": "🚀",
        "\\U0001f680": "🚀",
        "U0001f319": "🌙",
        "\\U0001f319": "🌙",
        "U0001f917": "🤗",
        "\\U0001f917": "🤗",
    }
    for k, v in replacements.items():
        content = content.replace(k, v)

    # 4. Inject Progressive Checklist Styles & DOM Overlay for HTML documents
    if "<html" in content or "<body" in content or "</head>" in content:
        if "wasm-progressive-boot-style" not in content:
            styles = """<style id="wasm-progressive-boot-style">
#wasm-splash-overlay{position:fixed;top:0;left:0;width:100vw;height:100vh;background:#0F172A;color:#F8FAFC;z-index:999999;display:flex;flex-direction:column;align-items:center;justify-content:center;font-family:-apple-system,BlinkMacSystemFont,"SF Pro Text",Inter,sans-serif;transition:opacity .4s ease}
.splash-box{background:#1E293B;border:1px solid #334155;border-radius:16px;padding:2.2rem 2.6rem;max-width:520px;width:90%;box-shadow:0 20px 40px rgba(0,0,0,.5);text-align:center}
.splash-title{font-size:1.35rem;font-weight:700;margin-bottom:.4rem;color:#FFF;display:flex;align-items:center;justify-content:center;gap:.5rem}
.splash-subtitle{font-size:.85rem;color:#94A3B8;margin-bottom:1.6rem}
.checklist{list-style:none;padding:0;margin:0 0 1.2rem 0;text-align:left;font-size:.92rem}
.checklist-item{display:flex;align-items:center;gap:.75rem;padding:.5rem 0;border-bottom:1px solid #334155;color:#64748B;transition:color .3s ease}
.checklist-item:last-child{border-bottom:none}
.checklist-item.active{color:#38BDF8;font-weight:600}
.checklist-item.done{color:#34D399}
.checklist-icon{font-size:1.05rem;width:1.4rem;text-align:center}
.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
</style>"""
            if "</head>" in content:
                content = content.replace("</head>", styles + "\n</head>")
            else:
                content = styles + "\n" + content

        if '<div id="wasm-splash-overlay"' not in content:
            overlay_and_scripts = """
<div id="wasm-splash-overlay" role="dialog" aria-modal="true" aria-label="Application Loading">
  <div class="splash-box">
    <div class="splash-title">🏛️ Market Bubble Detector (WebAssembly Edition)</div>
    <div class="splash-subtitle">Institutional Risk Analytics • Pyodide Engine</div>
    <ul class="checklist" id="boot-checklist">
      <li id="step-core" class="checklist-item active"><span class="checklist-icon">⏳</span><span>1. WebAssembly Core: Initializing Pyodide</span></li>
      <li id="step-packages" class="checklist-item"><span class="checklist-icon">⬜</span><span>2. Mathematical Engines: NumPy, SciPy & Plotly</span></li>
      <li id="step-data" class="checklist-item"><span class="checklist-icon">⬜</span><span>3. Financial Datasets: Mounting Provenance Panel (MEMFS)</span></li>
      <li id="step-render" class="checklist-item"><span class="checklist-icon">⬜</span><span>4. Interactive Dashboard: Rendering Analytical Suite</span></li>
    </ul>
    <div id="boot-status" style="font-size:0.8rem;color:#94A3B8;font-family:monospace;">Starting WebAssembly runtime...</div>
  </div>
</div>
<div id="a11y-status-announcer" aria-live="polite" aria-atomic="true" class="sr-only"></div>
<script id="wasm-runtime-enhancements">
function updateProgressChecklist(step, state, label) {
  const item = document.getElementById('step-' + step);
  if (!item) return;
  const icon = item.querySelector('.checklist-icon');
  const span = item.querySelector('span:last-child');
  if (label && span) span.textContent = label;
  item.classList.remove('active', 'done');
  if (state === 'active') { item.classList.add('active'); if (icon) icon.textContent = '⏳'; }
  else if (state === 'done') { item.classList.add('done'); if (icon) icon.textContent = '🟩'; }
  const statusEl = document.getElementById('boot-status');
  if (statusEl && label) statusEl.textContent = label;
}
function dismissSplashScreen() {
  const splash = document.getElementById('wasm-splash-overlay');
  if (splash) {
    splash.style.opacity = '0';
    splash.style.pointerEvents = 'none';
    setTimeout(() => { splash.remove(); document.body.classList.remove('pn-loading'); }, 400);
  } else { document.body.classList.remove('pn-loading'); }
}
function showFatalErrorUI(err) {
  dismissSplashScreen();
  document.body.classList.remove('pn-loading');
  let el = document.getElementById('wasm-fatal-error');
  if (!el) {
    el = document.createElement('div');
    el.id = 'wasm-fatal-error';
    el.style.cssText = 'margin: 2rem; padding: 1.5rem; background: #2A1515; border: 1px solid #FF5252; color: #FFF; border-radius: 8px; font-family: monospace; white-space: pre-wrap;';
    el.innerHTML = '<h3>⚠️ WebAssembly Initialization Error</h3><p>' + err + '</p><button onclick="window.location.reload()" style="background:#0288D1;color:#fff;border:none;padding:8px 16px;border-radius:6px;cursor:pointer;font-weight:600;margin-top:12px;">Retry Application</button>';
    document.body.prepend(el);
  }
}
function initKeyboardAccessibility() {
  const sidebarBtn = document.getElementById('sidebar-button');
  if (sidebarBtn) {
    sidebarBtn.setAttribute('tabindex', '0');
    sidebarBtn.setAttribute('role', 'button');
    sidebarBtn.setAttribute('aria-label', 'Toggle sidebar calibration controls');
    sidebarBtn.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); sidebarBtn.click(); }
    });
  }
  document.querySelectorAll('.fullscreen-button').forEach(btn => {
    btn.setAttribute('tabindex', '0');
    btn.setAttribute('role', 'button');
    btn.setAttribute('aria-label', 'Toggle fullscreen view');
    btn.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); btn.click(); }
    });
  });
  const header = document.querySelector('header') || document.querySelector('.header') || document.getElementById('header') || document.querySelector('.fast-header');
  if (header) header.setAttribute('role', 'banner');
  const nav = document.querySelector('nav') || document.querySelector('#sidebar') || document.querySelector('.sidebar') || document.querySelector('.fast-sidebar');
  if (nav) nav.setAttribute('role', 'navigation');
  const main = document.querySelector('main') || document.querySelector('#main') || document.querySelector('.main') || document.querySelector('#content');
  if (main) main.setAttribute('role', 'main');
  if (!document.getElementById('a11y-status-announcer')) {
    const announcer = document.createElement('div');
    announcer.id = 'a11y-status-announcer';
    announcer.setAttribute('aria-live', 'polite');
    announcer.setAttribute('aria-atomic', 'true');
    announcer.className = 'sr-only';
    announcer.style.cssText = 'position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0;';
    document.body.appendChild(announcer);
  }
}
function handleResponsiveLegends() {
  const isMobile = window.innerWidth < 1024;
  const plotlyPlots = document.querySelectorAll('.js-plotly-plot');
  plotlyPlots.forEach(el => {
    if (window.Plotly && el._fullLayout) {
      if (isMobile) {
        Plotly.relayout(el, { 'legend.orientation': 'h', 'legend.x': 0.0, 'legend.y': -0.25, 'legend.xanchor': 'left', 'legend.yanchor': 'top', 'margin.l': 40, 'margin.r': 40, 'margin.t': 60, 'margin.b': 80 });
      } else {
        Plotly.relayout(el, { 'legend.orientation': 'v', 'legend.x': 1.01, 'legend.y': 1.0, 'legend.xanchor': 'left', 'legend.yanchor': 'top', 'margin.l': 40, 'margin.r': 230, 'margin.t': 60, 'margin.b': 40 });
      }
    }
  });
}
window.addEventListener('resize', handleResponsiveLegends);
function initHashRouting() {
  function slugify(t) { return (t || '').toLowerCase().trim().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, ''); }
  function parseHash() { const params = new URLSearchParams(window.location.hash.replace(/^#/, '')); return { tab: params.get('tab'), horizon: params.get('horizon') }; }
  function getActiveTabSlug() { const a = document.querySelector('.bk-tab.bk-active, [role="tab"][aria-selected="true"], .tab.active'); return a && a.textContent ? slugify(a.textContent) : null; }
  function getActiveHorizon() { const sel = document.querySelector('#sidebar select, .sidenav select, select.bk-input'); return (sel && sel.value && (sel.value.includes('Option 2') || sel.value === 'option_2')) ? 'option_2' : 'option_1'; }
  function updateUrlHash(t, h) {
    const newHash = '#tab=' + (t || getActiveTabSlug() || 'macro-valuation') + '&horizon=' + (h || getActiveHorizon() || 'option_1');
    if (window.location.hash !== newHash) history.pushState(null, '', newHash);
  }
  function syncHashToUI() {
    const state = parseHash();
    if (state.tab) {
      document.querySelectorAll('.bk-tab, [role="tab"], .tab').forEach(btn => {
        if (btn.textContent && slugify(btn.textContent).includes(slugify(state.tab))) btn.click();
      });
    }
    if (state.horizon) {
      document.querySelectorAll('#sidebar select, .sidenav select, select.bk-input').forEach(sel => {
        for (let opt of sel.options) {
          if (opt.value === state.horizon || (state.horizon === 'option_2' && opt.text.includes('Option 2')) || (state.horizon === 'option_1' && opt.text.includes('Option 1'))) {
            if (sel.value !== opt.value) { sel.value = opt.value; sel.dispatchEvent(new Event('change', { bubbles: true })); }
          }
        }
      });
    }
  }
  function attachListeners() {
    document.querySelectorAll('.bk-tab, [role="tab"], .tab').forEach(btn => {
      if (!btn.dataset.hashBound) {
        btn.dataset.hashBound = 'true';
        btn.addEventListener('click', () => {
          setTimeout(() => { const slug = btn.textContent ? slugify(btn.textContent) : null; if (slug) updateUrlHash(slug, null); handleResponsiveLegends(); }, 150);
        });
      }
    });
    document.querySelectorAll('#sidebar select, .sidenav select, select.bk-input').forEach(sel => {
      if (!sel.dataset.hashBound) {
        sel.dataset.hashBound = 'true';
        sel.addEventListener('change', () => {
          const hVal = (sel.value && sel.value.includes('Option 2')) || sel.value === 'option_2' ? 'option_2' : 'option_1';
          updateUrlHash(null, hVal);
        });
      }
    });
  }
  window.addEventListener('popstate', syncHashToUI);
  window.addEventListener('hashchange', syncHashToUI);
  let checks = 0;
  const timer = setInterval(() => { attachListeners(); checks++; if (checks === 3) syncHashToUI(); if (checks >= 12) clearInterval(timer); }, 500);
}
initHashRouting();
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('sw.js').catch(err => console.warn('SW registration failed:', err));
}
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initKeyboardAccessibility);
} else {
  initKeyboardAccessibility();
}
</script>"""
            if "<body" in content:
                content = re.sub(r'(<body[^>]*>)', r'\1\n' + overlay_and_scripts, content, count=1)
            else:
                content = overlay_and_scripts + "\n" + content

    # 5. Inject MEMFS Dataset Pre-Loader and Robust Error Boundary (idempotently)
    if "Pre-loaded MEMFS dataset:" not in content:
        # Check if full Panel convert main() signature is present
        if re.search(r'async function main\(\)\s*\{.*?await pyodide\.loadPackage\(', content, flags=re.DOTALL):
            main_header = """async function main() {
      try {
        if (typeof updateProgressChecklist === 'function') updateProgressChecklist('core', 'active', 'Initializing Pyodide WebAssembly runtime...');
        let pyodide = await loadPyodide();
        if (typeof updateProgressChecklist === 'function') {
          updateProgressChecklist('core', 'done', '1. WebAssembly Core: Initialized');
          updateProgressChecklist('packages', 'active', 'Downloading mathematical engines...');
        }
        await pyodide.loadPackage("micropip");
        await pyodide.runPythonAsync(`
          import micropip
          await micropip.install(['bokeh', 'panel', 'pyodide-http', 'plotly', 'numpy']);
        `);
        if (typeof updateProgressChecklist === 'function') {
          updateProgressChecklist('packages', 'done', '2. Mathematical Engines: Loaded');
          updateProgressChecklist('data', 'active', 'Pre-loading MEMFS datasets...');
        }
        for (const ds of ['market_data_50yr.json']) {
          try {
            let r = await fetch(ds);
            if (r.ok) {
              let t = await r.text();
              pyodide.FS.writeFile(ds, t);
              console.log('Pre-loaded MEMFS dataset: ' + ds);
            }
          } catch(e) { console.warn('Could not pre-load ' + ds, e); }
        }
        if (typeof updateProgressChecklist === 'function') {
          updateProgressChecklist('data', 'done', '3. Financial Datasets: Mounted (MEMFS)');
          updateProgressChecklist('render', 'active', 'Mounting interactive analytical suite...');
        }"""

            content = re.sub(
                r'async function main\(\)\s*\{.*?await pyodide\.loadPackage\(\"micropip\"\);\s*await pyodide\.runPythonAsync\(`.*?`\);',
                main_header,
                content,
                flags=re.DOTALL
            )

            code_exec_replacement = """await pyodide.runPythonAsync(code);
        if (typeof updateProgressChecklist === 'function') updateProgressChecklist('render', 'done', '4. Interactive Dashboard: Ready');
        if (typeof dismissSplashScreen === 'function') dismissSplashScreen();
        if (typeof handleResponsiveLegends === 'function') {
          handleResponsiveLegends();
          setTimeout(handleResponsiveLegends, 500);
          setTimeout(handleResponsiveLegends, 1500);
        }
        if (typeof initKeyboardAccessibility === 'function') initKeyboardAccessibility();
        const initAnnouncer = document.getElementById('a11y-status-announcer');
        if (initAnnouncer && !initAnnouncer.textContent) {
          initAnnouncer.textContent = 'Market Bubble Detector WebAssembly application loaded and interactive.';
        }
      } catch (err) {
        showFatalErrorUI(err);
      }
    }"""

            content = re.sub(
                r'await\s+pyodide\.runPythonAsync\(code\);?\s*\}',
                code_exec_replacement,
                content
            )
        else:
            # Fallback for minimal sample scripts in test harnesses
            minimal_block = """
      for (const ds of ['market_data_50yr.json']) {
        try {
          let r = await fetch(ds);
          if (r.ok) {
            let t = await r.text();
            pyodide.FS.writeFile(ds, t);
            console.log('Pre-loaded MEMFS dataset: ' + ds);
          }
        } catch(e) { console.warn('Could not pre-load ' + ds, e); }
      }
      try {
        await pyodide.runPythonAsync(code);
      } catch (err) {
        document.body.classList.remove('pn-loading');
        let el = document.createElement('div');
        el.style.cssText = 'margin: 2rem; padding: 1.5rem; background: #2A1515; border: 1px solid #FF5252; color: #FFF; border-radius: 8px; font-family: monospace; white-space: pre-wrap;';
        el.innerHTML = '<h3>⚠️ WebAssembly Initialization Error</h3><p>' + err + '</p>';
        document.body.prepend(el);
      }"""
            content = re.sub(r'await\s+pyodide\.runPythonAsync\(code\);?', minimal_block, content)

    return content


def postprocess_wasm_html(html_path: Path = Path("dist/index.html")):
    """
    Apply post-processing transformations to the compiled Panel WebAssembly HTML bundle.

    Parameters
    ----------
    html_path : Path
        Filesystem path to the target `index.html` artifact in the distribution folder.
    """
    if not html_path.exists():
        print(f"Warning: {html_path} does not exist.")
        return

    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    content = postprocess_wasm_content(content)

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Successfully postprocessed {html_path}")


if __name__ == "__main__":
    postprocess_wasm_html()
