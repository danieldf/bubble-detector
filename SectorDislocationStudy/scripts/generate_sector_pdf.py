#!/usr/bin/env python3
"""
Institutional Technical Report Markdown-to-PDF Compiler (`generate_sector_pdf.py`).

Compiles `SectorDislocationStudy/SectorDislocation_TechnicalReport.md` into a publication-grade
typeset PDF (`SectorDislocationStudy/SectorDislocation_TechnicalReport.pdf`) via Pandoc
(`gfm+tex_math_dollars`) + Typst, rendering full LaTeX equations, executive Title Banner,
styled tables, callouts, running CC-BY-NC-ND 4.0 headers/footers, and 4K HXGA figures.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

STUDY_DIR = Path(__file__).resolve().parents[1]
MD_PATH = STUDY_DIR / "SectorDislocation_TechnicalReport.md"
TYP_PATH = STUDY_DIR / "SectorDislocation_TechnicalReport.typ"
PDF_PATH = STUDY_DIR / "SectorDislocation_TechnicalReport.pdf"

PANDOC_BIN = "/opt/homebrew/bin/pandoc"
TYPST_BIN = "/Users/danielsflscientific.com/.nix-profile/bin/typst"

TYPST_PREAMBLE = r"""// Institutional Sector Dislocation Technical Report Stylesheet (CC-BY-NC-ND 4.0 | CONFIDENTIAL)
#set document(
  title: "Cross-Sectional Sector Dislocation Intelligence: Co-Primary 6-Sleeve & 7-Sleeve Orthogonal Taxonomies, Bifurcated Signal Synthesis & Fiduciary Mapping Mechanics (2006–2026)",
  author: "Daniel D Ferrante, PhD",
)

#set page(
  paper: "us-letter",
  margin: (left: 0.62in, right: 0.62in, top: 0.82in, bottom: 0.76in),
  header: context {
    if counter(page).get().first() > 1 [
      #set text(size: 7.25pt, fill: rgb("#475569"), weight: "bold")
      #grid(
        columns: (1.06fr, 0.94fr),
        align(left)[CONFIDENTIAL — PROPRIETARY IP  |  CC-BY-NC-ND 4.0  |  Daniel D Ferrante, PhD],
        align(right)[Cross-Sectional Sector Dislocation Report v1.1.0 (2006–2026)],
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
      #set text(size: 7.5pt, fill: rgb("#475569"))
      #grid(
        columns: (3.2fr, 0.8fr),
        align(left)[Daniel D Ferrante, PhD • November 18, 2026 • Sector Dislocation Report v1.1.0 (4K HUXGA 6400×4800, Cutoff >= 0.87)],
        align(right)[*Page #pg of #total*],
      )
    ]
  },
)

#set text(
  font: ("Helvetica Neue", "Arial"),
  size: 9.6pt,
  fill: rgb("#0F172A"),
  lang: "en",
)

#set par(
  justify: true,
  leading: 0.62em,
  spacing: 0.90em,
)

#set list(indent: 8pt, body-indent: 6pt, spacing: 0.62em)
#set enum(indent: 8pt, body-indent: 6pt, spacing: 0.62em)
#show table.cell: set par(justify: false)

// Styled Inline Code Badges
#show raw.where(block: false): box.with(
  fill: rgb("#F1F5F9"),
  stroke: 0.4pt + rgb("#CBD5E1"),
  inset: (x: 3pt, y: 0pt),
  outset: (y: 2pt),
  radius: 2.2pt,
)
#show raw: set text(font: ("Menlo", "Monaco", "Courier New"), size: 8.2pt, fill: rgb("#0F172A"))

// Styled Callout Blockquotes
#show quote.where(block: true): it => block(
  width: 100%,
  fill: rgb("#F8FAFC"),
  stroke: (left: 3.5pt + rgb("#0052CC"), top: 0.6pt + rgb("#CBD5E1"), right: 0.6pt + rgb("#CBD5E1"), bottom: 0.6pt + rgb("#CBD5E1")),
  radius: (right: 4pt),
  inset: (x: 11pt, y: 9pt),
  above: 0.95em,
  below: 0.95em,
  it.body,
)

// Styled Headings
#show heading.where(level: 1): it => {
  pagebreak(weak: true)
  block(
    width: 100%,
    fill: rgb("#0F172A"),
    inset: (x: 12pt, y: 9pt),
    radius: 4pt,
    above: 0.6em,
    below: 0.85em,
    text(size: 13.2pt, weight: "bold", fill: rgb("#FFFFFF"), it.body),
  )
}

#show heading.where(level: 2): it => {
  block(
    width: 100%,
    above: 1.15em,
    below: 0.60em,
    [
      #text(size: 11.6pt, weight: "bold", fill: rgb("#0052CC"), it.body)
      #v(-4pt)
      #line(length: 100%, stroke: 0.8pt + rgb("#93C5FD"))
    ],
  )
}

#show heading.where(level: 3): it => {
  block(
    above: 1.0em,
    below: 0.50em,
    text(size: 10.3pt, weight: "bold", fill: rgb("#1E293B"), it.body),
  )
}

// Styled Publication Tables (Breakable Across Pages Without Overflow!)
#set table(
  stroke: 0.5pt + rgb("#CBD5E1"),
  fill: (x, y) => if y == 0 { rgb("#0F172A") } else if calc.odd(y) { rgb("#FFFFFF") } else { rgb("#F8FAFC") },
  inset: (x: 3.5pt, y: 3.6pt),
)
#show table: set text(size: 6.6pt)
#show table: it => {
  show raw.where(block: false): r => text(font: ("Menlo", "Monaco", "Courier New"), size: 6.2pt, weight: "semibold", fill: rgb("#0F172A"), r.text)
  it
}
#show table.cell.where(y: 0): set text(weight: "bold", fill: rgb("#FFFFFF"), size: 6.7pt)
#show table.cell.where(y: 0): it => {
  show raw.where(block: false): r => text(font: ("Menlo", "Monaco", "Courier New"), fill: rgb("#FDE68A"), weight: "bold", size: 6.4pt, r.text)
  it
}

// Allow Table Figures to Break Cleanly Across Pages; Keep Image Figures Unbreakable
#show figure.where(kind: table): set block(breakable: true, width: 100%, above: 0.75em, below: 0.75em)

// Styled High-Resolution 4K HUXGA Image Figures
#show figure.where(kind: image): it => block(
  width: 100%,
  breakable: false,
  above: 0.9em,
  below: 0.9em,
  stroke: 0.75pt + rgb("#CBD5E1"),
  radius: 4pt,
  inset: 5pt,
  fill: rgb("#FFFFFF"),
  [
    #align(center, it.body)
    #if it.has("caption") and it.caption != none [
      #v(3pt)
      #align(center, text(size: 8.2pt, weight: "bold", fill: rgb("#334155"), it.caption))
    ]
  ],
)

// Dedicated Front Banner Block on Page 1
#block(
  width: 100%,
  fill: rgb("#0F172A"),
  inset: (x: 16pt, y: 15pt),
  radius: 5pt,
  [
    #text(size: 8.2pt, weight: "bold", fill: rgb("#F59E0B"))[
      CONFIDENTIAL — PROPRIETARY INTELLECTUAL PROPERTY  |  LICENSE: CC-BY-NC-ND 4.0
    ]
    #v(6pt)
    #text(size: 15.6pt, weight: "bold", fill: rgb("#FFFFFF"))[
      Cross-Sectional Sector Dislocation Intelligence: Co-Primary 6-Sleeve & 7-Sleeve Orthogonal Taxonomies, Bifurcated Signal Synthesis & Fiduciary Mapping Mechanics (2006–2026)
    ]
    #v(8pt)
    #line(length: 100%, stroke: 0.7pt + rgb("#334155"))
    #v(6pt)
    #grid(
      columns: (1fr, 1fr),
      row-gutter: 5pt,
      text(size: 9.0pt, fill: rgb("#E2E8F0"))[*Author:* Daniel D Ferrante, PhD],
      text(size: 9.0pt, fill: rgb("#E2E8F0"))[*Publication Date:* November 18, 2026],
      text(size: 8.4pt, fill: rgb("#94A3B8"))[*Version:* v1.1.0 (SemVer — 4K HUXGA 6400×4800)],
      text(size: 8.4pt, fill: rgb("#94A3B8"))[*Quality Gate:* Strict Confidence Cutoff >= 0.87],
    )
  ],
)
#v(6pt)

#let horizontalrule = line(length: 100%, stroke: 0.6pt + rgb("#CBD5E1"))
"""


def main() -> None:
    md_text = MD_PATH.read_text(encoding="utf-8")
    idx_abs = md_text.find("## Summary Abstract")
    assert idx_abs != -1, "Missing '## Summary Abstract'"
    md_body = md_text[idx_abs:]

    res = subprocess.run(
        [PANDOC_BIN, "-f", "gfm+tex_math_dollars", "-t", "typst"],
        input=md_body,
        check=True,
        capture_output=True,
        text=True,
    )
    typ_body = res.stdout
    typ_body = typ_body.replace("#divider()", "#v(2pt)\n#horizontalrule\n#v(2pt)")
    # Prevent trailing horizontal rule right before a Level-1 section pagebreak from creating a blank rule page
    typ_body = re.sub(r"#v\(2pt\)\s*#horizontalrule\s*#v\(2pt\)\s*(?== )", "\n", typ_body)
    typ_body = re.sub(r"#horizontalrule\s*(?== )", "\n", typ_body)

    full_typ = TYPST_PREAMBLE + "\n" + typ_body
    TYP_PATH.write_text(full_typ, encoding="utf-8")

    subprocess.run(
        [TYPST_BIN, "compile", "--root", str(STUDY_DIR), str(TYP_PATH), str(PDF_PATH)],
        check=True,
    )
    TYP_PATH.unlink(missing_ok=True)
    print(f"Compiled publication PDF: {PDF_PATH} ({PDF_PATH.stat().st_size / 1024:.1f} KB)")


if __name__ == "__main__":
    main()
