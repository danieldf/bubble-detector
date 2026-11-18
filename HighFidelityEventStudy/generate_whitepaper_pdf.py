#!/usr/bin/env python3
"""
Institutional White Paper Markdown-to-PDF Compiler (`generate_whitepaper_pdf.py`).

Converts `HighFidelityEventStudy/HighFidelityEventStudy_WhitePaper.md` into a
publication-grade, typeset institutional White Paper PDF (`HighFidelityEventStudy/HighFidelityEventStudy_WhitePaper.pdf`)
tailored for Family Investment Offices, Wealth Management Firms (RIAs), and Strategic Partners.

Enforces strict page-break architecture:
- Page 1: Dedicated Title Page (Title, Subtitle, Author: Daniel D Ferrante, PhD, Date: November 17, 2026, CC-BY-NC-ND 4.0 Disclaimer)
- Page 2: Dedicated Executive Abstract Page
- Page 3: Dedicated Table of Contents Page
- Sections 1–9: Every Section begins on a new clean page
- Final Page: Dedicated Confidentiality, IP Boundary Warnings & Attribution Colophon (Daniel D Ferrante, PhD | November 17, 2026)
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

STUDY_DIR = Path(__file__).resolve().parent
MD_PATH = STUDY_DIR / "HighFidelityEventStudy_WhitePaper.md"
TYP_PATH = STUDY_DIR / "HighFidelityEventStudy_WhitePaper.typ"
PDF_PATH = STUDY_DIR / "HighFidelityEventStudy_WhitePaper.pdf"

PANDOC_BIN = "/opt/homebrew/bin/pandoc"
TYPST_BIN = "/Users/danielsflscientific.com/.nix-profile/bin/typst"

TYPST_PREAMBLE = r"""// Institutional White Paper Typst Stylesheet (CC-BY-NC-ND 4.0 | CONFIDENTIAL)
#set document(
  title: "Asymmetric Systemic-Risk Intelligence & Capital Preservation: A 20-Year Out-of-Sample Dislocation Study for Family Offices, Wealth Managers & Strategic Partners (2006–2026)",
  author: "Daniel D Ferrante, PhD",
)

#set page(
  paper: "us-letter",
  margin: (left: 0.65in, right: 0.65in, top: 0.72in, bottom: 0.68in),
  header: context {
    if counter(page).get().first() > 1 [
      #set text(size: 7.8pt, fill: rgb("#475569"), weight: "bold")
      #grid(
        columns: (1fr, 1fr),
        align(left)[CONFIDENTIAL — PROPRIETARY IP  |  CC-BY-NC-ND 4.0],
        align(right)[Asymmetric Systemic-Risk Intelligence & Capital Preservation (2006–2026)],
      )
      #v(-4pt)
      #line(length: 100%, stroke: 0.6pt + rgb("#CBD5E1"))
    ]
  },
  footer: context {
    let pg = counter(page).get().first()
    let total = counter(page).final().first()
    if pg > 1 [
      #line(length: 100%, stroke: 0.6pt + rgb("#CBD5E1"))
      #v(2pt)
      #set text(size: 7.8pt, fill: rgb("#475569"))
      #grid(
        columns: (2fr, 1fr),
        align(left)[Daniel D Ferrante, PhD • Institutional White Paper v1.2.0 (Engine v3.7.0) • November 17, 2026],
        align(right)[*Page #pg of #total*],
      )
    ]
  },
)

#set text(
  font: ("Helvetica Neue", "Arial"),
  size: 9.8pt,
  fill: rgb("#0F172A"),
  lang: "en",
)

#set par(
  justify: true,
  leading: 0.58em,
  spacing: 0.92em,
)

// Heading hierarchy styling
#show heading.where(level: 1): it => {
  v(4pt)
  block(
    width: 100%,
    fill: rgb("#0F172A"),
    inset: (x: 12pt, y: 9pt),
    radius: 4pt,
    text(fill: rgb("#FFFFFF"), size: 13.5pt, weight: "bold", it.body),
  )
  v(4pt)
}

#show heading.where(level: 2): it => {
  v(8pt)
  text(fill: rgb("#0F172A"), size: 11.8pt, weight: "bold", it.body)
  v(-4pt)
  line(length: 100%, stroke: 1.0pt + rgb("#1D4ED8"))
  v(3pt)
}

#show heading.where(level: 3): it => {
  v(6pt)
  text(fill: rgb("#1E3A8A"), size: 10.5pt, weight: "bold", it.body)
  v(2pt)
}

#show heading.where(level: 4): it => {
  v(4pt)
  text(fill: rgb("#334155"), size: 9.8pt, weight: "bold", style: "italic", it.body)
  v(2pt)
}

// Blockquotes styled as institutional fiduciary/example callout cards
#show quote.where(block: true): it => {
  v(4pt)
  block(
    width: 100%,
    fill: rgb("#F8FAFC"),
    stroke: (left: 3.5pt + rgb("#1D4ED8"), top: 0.5pt + rgb("#CBD5E1"), right: 0.5pt + rgb("#CBD5E1"), bottom: 0.5pt + rgb("#CBD5E1")),
    inset: (x: 11pt, y: 8pt),
    radius: (right: 4pt),
    it.body,
  )
  v(4pt)
}

// Inline raw code styling
#show raw.where(block: false): box.with(
  fill: rgb("#F1F5F9"),
  inset: (x: 3pt, y: 0pt),
  outset: (y: 2pt),
  radius: 2pt,
)

// Publication-grade Table styling
#set table(
  stroke: (x, y) => if y == 0 {
    (top: 1.2pt + rgb("#0F172A"), bottom: 1.0pt + rgb("#0F172A"), left: 0.4pt + rgb("#CBD5E1"), right: 0.4pt + rgb("#CBD5E1"))
  } else {
    (top: 0.4pt + rgb("#CBD5E1"), bottom: 0.4pt + rgb("#CBD5E1"), left: 0.4pt + rgb("#CBD5E1"), right: 0.4pt + rgb("#CBD5E1"))
  },
  fill: (x, y) => if y == 0 {
    rgb("#0F172A")
  } else if calc.odd(y) {
    rgb("#F8FAFC")
  } else {
    rgb("#FFFFFF")
  },
  inset: (x: 5pt, y: 4.5pt),
)

#show table.cell.where(y: 0): set text(fill: rgb("#FFFFFF"), weight: "bold", size: 8.0pt)
#show table.cell.where(y: 0): it => {
  show raw.where(block: false): set text(fill: rgb("#0F172A"), weight: "bold")
  it
}
#show table.cell: set text(size: 8.0pt)

// Figure styling
#show figure: it => {
  v(6pt)
  block(
    width: 100%,
    stroke: 0.75pt + rgb("#CBD5E1"),
    inset: 6pt,
    radius: 4pt,
    fill: rgb("#FFFFFF"),
    [
      #it.body
      #v(3pt)
      #set text(size: 8.5pt, fill: rgb("#334155"), weight: "bold")
      #it.caption
    ]
  )
  v(6pt)
}

// Dedicated Page 1: Full-Page Institutional White Paper Title Page
#v(0.06in)
#block(
  width: 100%,
  fill: rgb("#0F172A"),
  inset: (x: 18pt, y: 18pt),
  radius: 6pt,
  [
    #set text(fill: rgb("#F8FAFC"))
    #text(size: 8.5pt, weight: "bold", fill: rgb("#F59E0B"))[
      CONFIDENTIAL — PROPRIETARY INTELLECTUAL PROPERTY  |  LICENSE: CC-BY-NC-ND 4.0
    ]
    #v(8pt)
    #text(size: 18.5pt, weight: "bold", fill: rgb("#FFFFFF"))[
      Asymmetric Systemic-Risk Intelligence & Capital Preservation: A 20-Year Out-of-Sample Dislocation Study for Family Offices, Wealth Managers & Strategic Partners (2006–2026)
    ]
    #v(8pt)
    #text(size: 11.2pt, fill: rgb("#CBD5E1"), style: "italic")[
      Solving Sequence-of-Returns Risk and Crash-Bottom Liquidation via Orthogonal 13-Pillar Regime Synthesis
    ]
    #v(10pt)
    #line(length: 100%, stroke: 0.75pt + rgb("#334155"))
    #v(8pt)
    #grid(
      columns: (1fr, 1fr),
      row-gutter: 6pt,
      text(size: 9.5pt, fill: rgb("#E2E8F0"))[*Author:* Daniel D Ferrante, PhD],
      text(size: 9.5pt, fill: rgb("#E2E8F0"))[*Publication Date:* November 17, 2026],
      text(size: 8.8pt, fill: rgb("#94A3B8"))[*Release Version:* White Paper v1.2.0 (Engine v3.7.0)],
      text(size: 8.8pt, fill: rgb("#94A3B8"))[*Target Audience:* Family Offices, RIAs & Strategic Partners],
    )
  ],
)

#v(0.14in)

// Key Headline Metric Strip on Title Page
#grid(
  columns: (1fr, 1fr, 1fr, 1fr),
  column-gutter: 8pt,
  block(width: 100%, fill: rgb("#F8FAFC"), stroke: 0.75pt + rgb("#CBD5E1"), inset: 9pt, radius: 4pt)[
    #align(center)[
      #text(size: 14pt, weight: "bold", fill: rgb("#1D4ED8"))[100% (12/12)] \
      #v(2pt)
      #text(size: 7.6pt, weight: "bold", fill: rgb("#334155"))[Crises Captured (1987–2026)] \
      #text(size: 7.0pt, fill: rgb("#64748B"))[8/8 Modern + 4/4 Pre-2006]
    ]
  ],
  block(width: 100%, fill: rgb("#F8FAFC"), stroke: 0.75pt + rgb("#CBD5E1"), inset: 9pt, radius: 4pt)[
    #align(center)[
      #text(size: 14pt, weight: "bold", fill: rgb("#B45309"))[225.2 Days] \
      #v(2pt)
      #text(size: 7.6pt, weight: "bold", fill: rgb("#334155"))[Mean Warning Runway] \
      #text(size: 7.0pt, fill: rgb("#64748B"))[89.4% of a 252-Day Year]
    ]
  ],
  block(width: 100%, fill: rgb("#F8FAFC"), stroke: 0.75pt + rgb("#CBD5E1"), inset: 9pt, radius: 4pt)[
    #align(center)[
      #text(size: 14pt, weight: "bold", fill: rgb("#047857"))[-6.0% vs -24.9%] \
      #v(2pt)
      #text(size: 7.6pt, weight: "bold", fill: rgb("#334155"))[75.8% Drawdown Reduction] \
      #text(size: 7.0pt, fill: rgb("#64748B"))[+18.8% Saved per Dislocation]
    ]
  ],
  block(width: 100%, fill: rgb("#F8FAFC"), stroke: 0.75pt + rgb("#CBD5E1"), inset: 9pt, radius: 4pt)[
    #align(center)[
      #text(size: 14pt, weight: "bold", fill: rgb("#0F172A"))[45.4% (Neutral)] \
      #v(2pt)
      #text(size: 7.6pt, weight: "bold", fill: rgb("#334155"))[Live Score (Nov 13, 2026)] \
      #text(size: 7.0pt, fill: rgb("#64748B"))[S&P 500 at 7,561.67]
    ]
  ],
)

#v(0.14in)

// Confidentiality & Proprietary IP Disclaimer Box on Title Page
#block(
  width: 100%,
  fill: rgb("#FFFBEB"),
  stroke: (left: 4pt + rgb("#D97706"), top: 0.6pt + rgb("#FCD34D"), right: 0.6pt + rgb("#FCD34D"), bottom: 0.6pt + rgb("#FCD34D")),
  inset: (x: 13pt, y: 10pt),
  radius: 4pt,
  [
    #text(size: 9.0pt, weight: "bold", fill: rgb("#92400E"))[
      CONFIDENTIALITY & PROPRIETARY INTELLECTUAL PROPERTY DISCLAIMER (CC-BY-NC-ND 4.0)
    ]
    #v(3pt)
    #set text(size: 8.4pt, fill: rgb("#78350F"))
    *CLASSIFICATION: CONFIDENTIAL — PROPRIETARY INTELLECTUAL PROPERTY* \
    *LICENSE: Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (`CC-BY-NC-ND 4.0`)* \
    #v(2pt)
    *NOTICE OF PROPRIETARY RIGHTS:* This White Paper and all accompanying high-resolution 4K visual artifacts, empirical tables, and quantitative architectures contain confidential, proprietary research and trade-secret methodologies developed by *Daniel D Ferrante, PhD* for institutional systemic-risk detection, fiduciary drawdown defense, and asymmetric capital preservation. Under the terms of the *Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (`CC-BY-NC-ND 4.0`)* license, this document may be shared in its unaltered, complete form with full attribution to the author for non-commercial due-diligence evaluation only. No part of this publication may be used for commercial purposes, modified, reverse-engineered, decompiled, or redistributed in derivative form without explicit prior written authorization from *Daniel D Ferrante, PhD*. Full quantitative parameterizations, exact Gram-Schmidt conditioning orderings, state-space transition matrices, and proprietary meta-synthesis weight vectors are intentionally withheld to safeguard Intellectual Property (IP).
  ],
)

#v(0.12in)
#block(
  width: 100%,
  fill: rgb("#F8FAFC"),
  stroke: 0.6pt + rgb("#CBD5E1"),
  inset: (x: 13pt, y: 9pt),
  radius: 4pt,
  [
    #set text(size: 8.3pt, fill: rgb("#334155"))
    *Evaluation Scope & Verification Summary:*
    - *Primary Out-of-Sample Audit Horizon:* January 2, 2006 – November 13, 2026 (`N = 5,445` weekday business sessions / `5,250` NYSE exchange sessions with causal holiday forward-fill).
    - *Master Causal Warm-Up & Out-of-Era Stress Horizon:* January 1, 1975 – November 13, 2026 (`N = 13,045` business sessions), capturing 1987 Black Monday, 1990 S&L/Gulf War, 1998 LTCM, and 2000–02 Dot-Com crashes.
    - *Production Software Verification:* Dual-runtime server (`NiceGUI`) and zero-server browser (`Pyodide WebAssembly`) architecture passing `135 / 135` automated econometric, anti-leakage, and numerical-parity regression tests.
  ],
)

#pagebreak()

// Helper Functions Emitted by Pandoc
#let horizontalrule = line(length: 100%, stroke: 0.6pt + rgb("#CBD5E1"))
"""


def build_whitepaper_pdf() -> Path:
    assert MD_PATH.exists(), f"Missing {MD_PATH}"

    md_text = MD_PATH.read_text(encoding="utf-8")
    # Strip the top Markdown title block prior to `## Executive Abstract` since Page 1 is rendered by our dedicated Typst Title Page block
    idx_abstract = md_text.find("## Executive Abstract")
    assert idx_abstract != -1, "Could not find '## Executive Abstract' in White Paper Markdown"
    md_body = md_text[idx_abstract:]
    # Remove literal `\newpage` markers before passing to Pandoc (we inject exact `#pagebreak()` in Typst)
    md_body = md_body.replace("\\newpage", "")

    # 1. Convert GFM Markdown body to Typst via Pandoc
    res = subprocess.run(
        [PANDOC_BIN, "-f", "gfm", "-t", "typst"],
        input=md_body,
        check=True,
        capture_output=True,
        text=True,
    )
    typ_body = res.stdout

    # Replace `#divider()` or `#horizontalrule` with clean spacing + subtle rule
    typ_body = typ_body.replace("#divider()", "#v(3pt)\n#horizontalrule\n#v(3pt)")
    typ_body = typ_body.replace("#horizontalrule", "#v(3pt)\n#horizontalrule\n#v(3pt)")

    # Enforce strict page breaks:
    # - Before `== Table of Contents` (so Executive Abstract is on Page 2, Table of Contents is on Page 3)
    typ_body = re.sub(
        r"\n(== Table of Contents)",
        r"\n#pagebreak()\n\1",
        typ_body,
    )
    # - Before every major Section (`= Section 1:` through `= Section 9:`) and before the Final Colophon Page (`= Confidentiality, Intellectual Property Boundary & Attribution Colophon`)
    typ_body = re.sub(
        r"\n(= Section [1-9]:|= Confidentiality, Intellectual Property Boundary)",
        r"\n#pagebreak()\n\1",
        typ_body,
    )

    # Ensure images scale cleanly to 96% width inside figures so section text + figure fit harmoniously
    typ_body = re.sub(
        r'#box\(image\("([^"]+)"\)\)',
        r'#image("\1", width: 96%)',
        typ_body,
    )
    typ_body = re.sub(
        r'image\("\./([^"]+)"\)',
        r'image("\1", width: 96%)',
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
    if TYP_PATH.exists():
        TYP_PATH.unlink()

    print(f"[OK] Compiled {PDF_PATH.name} ({PDF_PATH.stat().st_size / 1024:.1f} KB)")
    return PDF_PATH


if __name__ == "__main__":
    build_whitepaper_pdf()
