#!/usr/bin/env python3
"""
High-Quality Executive Report Markdown-to-PDF Compiler (`generate_executive_pdf.py`).

Converts `HighFidelityEventStudy/HighFidelityEventStudy_Executive_Report.md` into a
publication-grade, typeset institutional PDF (`HighFidelityEventStudy/HighFidelityEventStudy_Executive_Report.pdf`)
using Pandoc (GFM parser) + Typst with custom executive typography, running confidentiality headers/footers,
styled callout boxes, publication tables, and embedded 4K HXGA white-background PNG figures.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

STUDY_DIR = Path(__file__).resolve().parent
MD_PATH = STUDY_DIR / "HighFidelityEventStudy_Executive_Report.md"
TYP_PATH = STUDY_DIR / "HighFidelityEventStudy_Executive_Report.typ"
PDF_PATH = STUDY_DIR / "HighFidelityEventStudy_Executive_Report.pdf"

PANDOC_BIN = "/opt/homebrew/bin/pandoc"
TYPST_BIN = "/Users/danielsflscientific.com/.nix-profile/bin/typst"

TYPST_PREAMBLE = r"""// Institutional Executive Report Typst Stylesheet (CC-BY-NC-ND 4.0 | CONFIDENTIAL)
#set document(
  title: "High-Fidelity 20-Year Dislocation Event Study & Composite Regime Synthesis (2006–2026)",
  author: "Market Bubble Detector & Structural Break System Research Team",
)

#set page(
  paper: "us-letter",
  margin: (left: 0.68in, right: 0.68in, top: 0.85in, bottom: 0.80in),
  header: context {
    if counter(page).get().first() > 1 [
      #set text(size: 8pt, fill: rgb("#475569"), weight: "bold")
      #grid(
        columns: (1fr, 1fr),
        align(left)[CONFIDENTIAL — PROPRIETARY IP  |  CC-BY-NC-ND 4.0],
        align(right)[High-Fidelity 20-Year Dislocation Event Study (2006–2026)],
      )
      #v(-4pt)
      #line(length: 100%, stroke: 0.6pt + rgb("#CBD5E1"))
    ]
  },
  footer: context {
    let pg = counter(page).get().first()
    let total = counter(page).final().first()
    [
      #line(length: 100%, stroke: 0.6pt + rgb("#CBD5E1"))
      #v(2pt)
      #set text(size: 8pt, fill: rgb("#475569"))
      #grid(
        columns: (2fr, 1fr),
        align(left)[Market Bubble Detector & Structural Break System • Horizon Through Nov 23, 2026 • v1.2.0 (Engine v3.9.0)],
        align(right)[*Page #pg of #total*],
      )
    ]
  },
)

#set text(
  font: ("Helvetica Neue", "Arial"),
  size: 10pt,
  fill: rgb("#0F172A"),
  lang: "en",
)

#set par(
  justify: true,
  leading: 0.68em,
  spacing: 1.05em,
)

#set list(indent: 8pt, body-indent: 6pt, spacing: 0.75em)
#set enum(indent: 8pt, body-indent: 6pt, spacing: 0.75em)
#show table.cell: set par(justify: false)

// Styled Inline Code Badges
#show raw.where(block: false): box.with(
  fill: rgb("#F1F5F9"),
  stroke: 0.4pt + rgb("#CBD5E1"),
  inset: (x: 3.5pt, y: 0pt),
  outset: (y: 2.2pt),
  radius: 2.5pt,
)
#show raw: set text(font: ("Menlo", "Monaco", "Courier New"), size: 8.8pt, fill: rgb("#0F172A"))

// Styled Callout Blockquotes
#show quote.where(block: true): it => block(
  width: 100%,
  fill: rgb("#F8FAFC"),
  stroke: (left: 3.5pt + rgb("#0052CC"), top: 0.6pt + rgb("#CBD5E1"), right: 0.6pt + rgb("#CBD5E1"), bottom: 0.6pt + rgb("#CBD5E1")),
  radius: (right: 4pt),
  inset: (x: 12pt, y: 10pt),
  above: 1.1em,
  below: 1.1em,
  it.body,
)

// Styled Headings
#show heading.where(level: 1): it => {
  v(0.6em)
  block(
    width: 100%,
    fill: rgb("#0F172A"),
    inset: (x: 12pt, y: 9pt),
    radius: 4pt,
    above: 1.0em,
    below: 0.9em,
    text(size: 14.5pt, weight: "bold", fill: rgb("#FFFFFF"), it.body),
  )
}

#show heading.where(level: 2): it => {
  block(
    width: 100%,
    above: 1.25em,
    below: 0.65em,
    [
      #text(size: 12.2pt, weight: "bold", fill: rgb("#0052CC"), it.body)
      #v(-4pt)
      #line(length: 100%, stroke: 0.8pt + rgb("#93C5FD"))
    ],
  )
}

#show heading.where(level: 3): it => {
  block(
    above: 1.1em,
    below: 0.55em,
    text(size: 10.8pt, weight: "bold", fill: rgb("#1E293B"), it.body),
  )
}

// Styled Publication Tables
#set table(
  stroke: 0.5pt + rgb("#CBD5E1"),
  fill: (x, y) => if y == 0 { rgb("#E2E8F0") } else if calc.odd(y) { rgb("#FFFFFF") } else { rgb("#F8FAFC") },
  inset: (x: 5pt, y: 5.5pt),
)
#show table: set text(size: 7.8pt)
#show table.cell.where(y: 0): set text(weight: "bold", fill: rgb("#0F172A"), size: 8.0pt)

// Styled Figures & High-Resolution 4K Plots
#show figure: it => block(
  width: 100%,
  breakable: false,
  above: 1.0em,
  below: 1.0em,
  stroke: 0.8pt + rgb("#CBD5E1"),
  radius: 4pt,
  inset: 6pt,
  fill: rgb("#FFFFFF"),
  [
    #align(center, it.body)
    #if it.has("caption") and it.caption != none [
      #v(4pt)
      #align(center, text(size: 8.8pt, style: "italic", fill: rgb("#334155"), it.caption))
    ]
  ],
)

// Helper Functions Emitted by Pandoc
#let horizontalrule = line(length: 100%, stroke: 0.6pt + rgb("#CBD5E1"))
"""


def build_pdf() -> Path:
    assert MD_PATH.exists(), f"Missing {MD_PATH}"

    # 1. Convert GFM Markdown to Typst body via Pandoc
    res = subprocess.run(
        [PANDOC_BIN, str(MD_PATH), "-f", "gfm", "-t", "typst"],
        check=True,
        capture_output=True,
        text=True,
    )
    typ_body = res.stdout

    # Replace `#divider()` or `#horizontalrule` with clean spacing + subtle rule,
    # and insert pagebreaks before each major `# Section` / `# Appendix` heading (`= Section ...` / `= Appendix...`)
    typ_body = typ_body.replace("#divider()", "#v(4pt)\n#horizontalrule\n#v(4pt)")
    typ_body = re.sub(
        r"\n(= Section [1-5]:|= Appendix [AB]:|= Appendix:)",
        r"\n#pagebreak()\n\1",
        typ_body,
    )

    # Ensure images scale cleanly to 100% width inside figures
    typ_body = re.sub(
        r'#box\(image\("([^"]+)"\)\)',
        r'#image("\1", width: 100%)',
        typ_body,
    )
    typ_body = re.sub(
        r'image\("\./([^"]+)"\)',
        r'image("\1", width: 100%)',
        typ_body,
    )

    full_typ = TYPST_PREAMBLE + "\n" + typ_body
    TYP_PATH.write_text(full_typ, encoding="utf-8")

    # 2. Compile Typst to PDF
    subprocess.run(
        [TYPST_BIN, "compile", str(TYP_PATH), str(PDF_PATH)],
        cwd=str(STUDY_DIR),
        check=True,
    )
    # Remove intermediate .typ file to keep folder clean
    if TYP_PATH.exists():
        TYP_PATH.unlink()

    print(f"[OK] Compiled {PDF_PATH.name} ({PDF_PATH.stat().st_size / 1024:.1f} KB)")
    return PDF_PATH


if __name__ == "__main__":
    build_pdf()
