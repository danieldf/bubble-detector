"""
Post-processing utility for Panel WebAssembly compiled output (dist/index.html).
Injects MEMFS dataset pre-loader, adds error boundary, and decodes unicode emojis.
"""

import re
from pathlib import Path

def postprocess_wasm_html(html_path: Path = Path("dist/index.html")):
    if not html_path.exists():
        print(f"Warning: {html_path} does not exist.")
        return

    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

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

    # 4. Inject MEMFS Dataset Pre-Loader and Error Boundary (idempotently)
    preloader_and_error_boundary = """
      for (const ds of ['market_data_50yr.json', 'market_data_modern.json']) {
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

    if "WebAssembly Initialization Error" not in content:
        content = re.sub(r"await\s+pyodide\.runPythonAsync\(code\);?", preloader_and_error_boundary, content)

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Successfully postprocessed {html_path}")

if __name__ == "__main__":
    postprocess_wasm_html()
