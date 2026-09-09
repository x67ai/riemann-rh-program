#!/usr/bin/env python3
"""gen_challengedeps_dbn.py -- writes comparator/ChallengeDeps/DBN.lean (module ChallengeDeps.DBN), the TRUSTED
Mathlib-only copy of the M2a statement vocabulary, by extracting each definition block CHARACTER FOR CHARACTER
from the program's Zeta23 sources (Defs.lean, W1/{Format,Checker,Soundness}.lean, BarrierCert.lean, Asym.lean)
and re-wrapping the blocks under the root-style namespace `DBN` (W1 vocabulary under `DBN.W1`).  Session 20,
D1 M2a packaging (BRIEF.md §2 item 1).  Prints the (file, name, source lines) table for BUILD-NOTES.

usage: gen_challengedeps_dbn.py <lean-root>
"""
import os, re, sys

ROOT = sys.argv[1]
def src(p): return open(os.path.join(ROOT, p), encoding="utf-8").read().split("\n")

FILES = {
    "Defs": src("Zeta23/DBN/Defs.lean"),
    "Format": src("Zeta23/W1/Format.lean"),
    "Checker": src("Zeta23/W1/Checker.lean"),
    "Soundness": src("Zeta23/W1/Soundness.lean"),
    "BarrierCert": src("Zeta23/DBN/BarrierCert.lean"),
    "Asym": src("Zeta23/DBN/Asym.lean"),
}
PATHS = {"Defs": "Zeta23/DBN/Defs.lean", "Format": "Zeta23/W1/Format.lean", "Checker": "Zeta23/W1/Checker.lean",
         "Soundness": "Zeta23/W1/Soundness.lean", "BarrierCert": "Zeta23/DBN/BarrierCert.lean", "Asym": "Zeta23/DBN/Asym.lean"}

def block(fkey, name):
    lines = FILES[fkey]
    pat = re.compile(r"^(?:def|structure)\s+" + re.escape(name) + r"(?=[\s(:{]|$)")
    idx = [i for i, l in enumerate(lines) if pat.match(l)]
    if len(idx) != 1:
        raise SystemExit(f"{fkey}: {name}: found {len(idx)} matches")
    i = idx[0]
    start = i
    # docstring immediately above (may span several lines)
    if i > 0 and lines[i - 1].rstrip().endswith("-/"):
        j = i - 1
        while not lines[j].lstrip().startswith("/--"):
            j -= 1
        start = j
    end = i + 1
    decl = re.compile(r"^(?:def|structure|theorem|lemma|instance|@\[|/--|end |namespace |section|open )")
    while end < len(lines) and lines[end].strip() != "" and not decl.match(lines[end]):
        end += 1
    return "\n".join(lines[start:end]), start + 1, end  # 1-based inclusive

SECTIONS = [
    ("/-! ## 1. The trusted definition layer — Zeta23/DBN/Defs.lean v1.1 (nine definitions, nothing else) -/", "Defs",
     ["Phi", "Ht", "ZeroVerification", "alpha", "M0", "Mt", "Bt", "HtEntire", "Polymath15Bridge'"]),
    ("W1-OPEN", None, None),
    ("/-! ### 2a. W1 transcript data — Zeta23/W1/Format.lean -/", "Format", ["W1Row", "W1Data"]),
    ("/-! ### 2b. W1 checker helpers — Zeta23/W1/Checker.lean -/", "Checker",
     ["ratEqB", "densPos", "chainLt", "chainGt", "firstOK", "lastOK", "edgeOK", "rowOK", "rowsOK", "sumArgLo", "sumArgHi",
      "mdist", "floorRowOK", "floorRowsOK"]),
    ("/-! ### 2c. W1 real/complex reading and the row enclosure — Zeta23/W1/Soundness.lean §1–§2 -/", "Soundness",
     ["ratVal", "sigma1", "sigma2", "T1", "T2", "cpt", "rectClosed", "rectOpen", "rectBdry", "consecPairs", "segPt",
      "bottomPts", "rightPts", "topPts", "leftPts", "segs", "logDerivSegIntegral", "argIncrement", "RowEnclOK"]),
    ("W1-CLOSE", None, None),
    ("/-! ## 3. Lane B: barrier data, checker, H2-B — Zeta23/DBN/BarrierCert.lean §1–§3 -/", "BarrierCert",
     ["PrismData", "RectData", "BarrierData", "toW1", "seams", "checkPrismW1", "checkPrism", "checkBarrierChain",
      "checkBarrier", "RectData.x1", "RectData.x2", "RectData.y1", "RectData.y2", "seamTime", "t0", "RectClosedOf",
      "RectBdryOf", "BarrierRect", "BarrierBdry", "nextSeams", "PrismEnclOK", "BarrierEnclOK"]),
    ("/-! ## 4. Lane A: window data, checker, H2-A, H-TAIL — Zeta23/DBN/Asym.lean -/", "Asym",
     ["windowIdx", "AsymRow", "TailRow", "AsymData", "checkAsymRow", "consecutive", "lastNhi", "checkAsym", "At0", "Ay0",
      "AyA", "AsymEnclOK", "TailOK"]),
]

HEADER = """/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library and does NOT import it: it imports Mathlib only.
-/
/-
comparator/ChallengeDeps/DBN.lean — the TRUSTED definition layer for the comparator topic `DBN`
(the de Bruijn–Newman milestone M2a; see comparator/README.md, "Layout convention: one topic per file", and
rh-program/results/d1-m2a/packaging/BUILD-NOTES.md).

Everything the challenge statements in Challenge/DBN.lean mention is defined HERE, from Mathlib alone:
  §1 the nine definitions of Zeta23/DBN/Defs.lean v1.1 (`Phi`, `Ht`, `ZeroVerification`, `alpha`, `M0`, `Mt`, `Bt`,
     `HtEntire`, `Polymath15Bridge'`);
  §2 the W1 transcript vocabulary the barrier lane reuses (Zeta23/W1/{Format,Checker,Soundness}.lean: `W1Row`,
     `W1Data`, the integer checker helpers, the real/complex reading of a transcript, `segs`, `RowEnclOK`);
  §3 the barrier lane (Zeta23/DBN/BarrierCert.lean §1–§3: `PrismData`, `RectData`, `BarrierData`, `checkPrismW1`,
     `checkPrism`, `checkBarrierChain`, `checkBarrier`, the rational accessors, `PrismEnclOK`, `BarrierEnclOK`);
  §4 the asymptotic lane (Zeta23/DBN/Asym.lean: `windowIdx`, `AsymRow`, `TailRow`, `AsymData`, `checkAsymRow`,
     `consecutive`, `lastNhi`, `checkAsym`, `At0`, `Ay0`, `AyA`, `AsymEnclOK`, `TailOK`).
This module imports NOTHING from Zeta23/.  Every `def`/`structure` block below is CHARACTER FOR CHARACTER the block of
the named Zeta23 source (docstrings included; extracted mechanically by
rh-program/results/d1-m2a/packaging/gen_challengedeps_dbn.py, source lines recorded in BUILD-NOTES.md §1), re-wrapped
under the root-style namespace `DBN` (the W1 vocabulary under `DBN.W1`, so that the copied text `W1.densPos`,
`W1.RowEnclOK`, … resolves unchanged).  Zeta23's live in `Zeta23.DBN` / `Zeta23.W1`, so that Solution/DBN.lean can
import both without name clashes.  The copied structures are DISTINCT TYPES from Zeta23's (a re-declared structure is
never definitionally equal to the original); the solution side bridges them by transport lemmas, never by import.

A reader auditing WHAT is claimed needs to read only this file, ChallengeDeps/DBN/Instance02.lean (the instance
literals) and Challenge/DBN.lean, trusting Mathlib and the Lean kernel.  Nothing here is proved: this is statement
vocabulary, the audit surface.

TRUST MODEL (SPEC §3.7, verbatim, for any publication): the M2a target theorem is "kernel-checked modulo the displayed
hypotheses: (H1) a producer-certified zero verification — `ZeroVerification (116733/200000) 2500000097429`, discharged
by Platt–Trudgian Theorem 1; (H2) producer-certified enclosures — the barrier prisms (H2-B), the final-time window rows
(H2-A) and the tail (H-TAIL), from two independent producers; (H3) the Polymath15 analytic package — Theorem 1.2 in the
form `Polymath15Bridge'` and the entirety of H_t — as hypotheses."  Short label: "kernel-checked modulo H1, H2 (H2-B,
H2-A, H-TAIL), H3" — never "fully machine-checked".  Λ ≤ 0.2 is NOT proved: the bracket of record stays 0 ≤ Λ ≤ 0.2 on
the literature.  The word Λ never appears in a formal statement (design note §1.2; the conclusion is the ray form
∀ t ≥ 1/5, every zero of H_t is real).  ANTI-CHEAT NOTE (Defs.lean): `Ht` is a Bochner integral; if the integrand were
not integrable the definition would collapse to 0, making EVERY z a zero and the target conclusion FALSE, not vacuous.
-/
import Mathlib

open scoped Real
open Real (exp)
open Complex (I)
open MeasureTheory

noncomputable section

namespace DBN
"""

out = [HEADER]
table = []
for title, fkey, names in SECTIONS:
    if title == "W1-OPEN":
        out.append("\n/-! ## 2. The W1 vocabulary reused by the barrier lane (namespace `DBN.W1`) -/\n\nnamespace W1\n")
        continue
    if title == "W1-CLOSE":
        out.append("\nend W1\n\nopen W1\n")
        continue
    out.append("\n" + title + "\n")
    for n in names:
        b, s, e = block(fkey, n)
        out.append("\n" + b + "\n")
        table.append((PATHS[fkey], n, s, e))
out.append("\nend DBN\n\nend\n")
path = os.path.join(ROOT, "comparator", "ChallengeDeps", "DBN.lean")
open(path, "w", encoding="utf-8").write("".join(out))
print("wrote", path)
print("| Zeta23 source | definition | lines |\n|---|---|---|")
for p, n, s, e in table:
    print(f"| `{p}` | `{n}` | {s}–{e} |")
