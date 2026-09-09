#!/usr/bin/env python3
"""emit_challengedeps_instance02.py -- UNTRUSTED JSON -> Lean emitter for the TRUSTED comparator copy of the Instance02
literals: comparator/ChallengeDeps/DBN/Instance02.lean (module ChallengeDeps.DBN.Instance02).  Session 20, D1 M2a
packaging (BRIEF.md §2 item 1, second bullet).

A RE-TARGETING of the two program emitters, which it imports and whose literal-formatting code it calls unchanged:
  * results/d1-m2a/emit_lean_m2a.py        (Lane B: `rat`, `pair_lit`, `row_lit`; the `PrismData`/`BarrierData` layout)
  * results/d1-m2a/lane-a/emit_lean_lane_a.py (Lane A: `as_written`, `precheck`, the instance pins; the `AsymData` layout)
so that every `def` block here is BYTE-IDENTICAL to the corresponding block of the Zeta23 modules
(Zeta23/DBN/Instance02/{Rect,mp_NNNN,mp_Barrier,arb_NNNN,arb_Barrier,Asym_mp,Asym_arb}.lean) modulo the file header, the
imports and the namespace lines — checked afterwards by cmp_literal_blocks.py (`cmp` per def block).  No kernel facts
are emitted here (the trusted side carries DATA only; the `decide +kernel` facts stay on the Zeta23 side).  Integers are
the JSON's decimal strings written verbatim; nothing is computed.

usage: emit_challengedeps_instance02.py <mp-manifest.json> <arb-manifest.json> <asym-mp.json> <asym-arb.json> <lean-root>
"""
import importlib.util, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, rel))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
M2A = load("emit_lean_m2a", "../emit_lean_m2a.py")
LANEA = load("emit_lean_lane_a", "../lane-a/emit_lean_lane_a.py")
rat, pair_lit, row_lit = M2A.rat, M2A.pair_lit, M2A.row_lit
as_written, precheck = LANEA.as_written, LANEA.precheck

HEADER = """/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library and does NOT import it: it imports ChallengeDeps.DBN (Mathlib only).
-/
/-
comparator/ChallengeDeps/DBN/Instance02.lean — the TRUSTED copy of the Instance02 literals for the comparator topic
`DBN` (Polymath15 Table 1 row 2: X = 5 000 000 194 858, R = [X, X+1] × [16733/100000, 1], t₀ = 93/500; SPEC.md §9):
  * `row2Rect : RectData` — the common rectangle;
  * the mpmath-ball leg's barrier transcript (results/d1-m2a/transcripts/row2, {nmp} prisms, {rmp} rows, K = 10²⁴, A = 10¹²):
    `mp0000 … mp{lastmp} : PrismData` and `row2BarrierMP : BarrierData`;
  * the Arb/FLINT leg's barrier transcript (results/d1-m2a/transcripts/row2-arb, {narb} prisms, {rarb} rows, K = 10¹², A = 10⁶):
    `arb0000 … arb{lastarb} : PrismData` and `row2BarrierARB : BarrierData`;
  * the two Lane A transcripts (results/d1-m2a/lane-a/asym-{{mp,arb}}.json): `row2AsymMP`, `row2AsymARB : AsymData`
    (3 window rows covering N ∈ [630783, 5140999] consecutively, the tail row at N₁ = 5 141 000).
DATA ONLY: no theorem, no `decide`, no kernel evaluation happens here.  The kernel facts `checkPrism row2Rect … = true`,
`checkBarrierChain … = true`, `checkAsym … = true` (`decide +kernel`, no `native_decide`) live on the Zeta23 side
(Zeta23/DBN/Instance02/…); the solution module Solution/DBN.lean proves that these copies transport to Zeta23's literals
and delegates to them.  The challenge statements of Challenge/DBN.lean quote these literals by name, so a reader of the
trusted surface sees exactly which integers the displayed enclosure hypotheses H2-B, H2-A, H-TAIL are about.

Mechanically emitted a SECOND time from the same JSON sources as the Zeta23 modules by the UNTRUSTED
rh-program/results/d1-m2a/packaging/emit_challengedeps_instance02.py (a re-targeting of emit_lean_m2a.py and
lane-a/emit_lean_lane_a.py — the same literal-formatting code), so that every `def` block below is byte-identical to the
corresponding block of Zeta23/DBN/Instance02/{{Rect,mp_NNNN,mp_Barrier,arb_NNNN,arb_Barrier,Asym_mp,Asym_arb}}.lean
modulo header/import/namespace lines; record: packaging/cmp-literal-blocks.log.  The producers are UNTRUSTED; their
numbers enter the trusted statement only through the displayed hypotheses over these literals.
Label (SPEC §3.7): "kernel-checked modulo H1, H2 (H2-B, H2-A, H-TAIL), H3" — never "fully machine-checked".
-/
import ChallengeDeps.DBN

namespace DBN

set_option maxRecDepth 100000

"""

def rect_block(rect):
    (x1, x2, y1, y2) = rect
    return (f"/-- R = [{x1[0]}/{x1[1]}, {x2[0]}/{x2[1]}] × [{y1[0]}/{y1[1]}, {y2[0]}/{y2[1]}] (SPEC.md §9). -/\n"
            f"def row2Rect : RectData :=\n"
            f"  ⟨{x1[0]}, {x1[1]}, {x2[0]}, {x2[1]}, {y1[0]}, {y1[1]}, {y2[0]}, {y2[1]}⟩\n\n")

def prism_blocks(p, j, prefix, chunk=1000):
    """the `_rows_k` chunk defs and the `PrismData` def, exactly as emit_lean_m2a.emit_prism writes them."""
    name = f"{prefix}{j:04d}"
    rows = p["segments"]
    seam = rat(p["seam"])
    K, A = int(p["scales"]["K"]), int(p["scales"]["A"])
    Fn, Fd = int(p["modulus_floor"]["Fn"]), int(p["modulus_floor"]["Fd"])
    E, D = int(p["approx_defect"]), int(p["displacement"])
    mesh = {e: [rat(r) for r in p["mesh"][e]] for e in ("bottom", "right", "top", "left")}
    out = []
    nchunks = (len(rows) + chunk - 1) // chunk
    for c in range(nchunks):
        part = rows[c * chunk:(c + 1) * chunk]
        out.append(f"/-- rows {c * chunk}–{c * chunk + len(part) - 1} of prism {j}. -/\n")
        out.append(f"def {name}_rows_{c} : List W1.W1Row := [\n")
        out.append(",\n".join("  " + row_lit(r) for r in part))
        out.append("]\n\n")
    rows_expr = " ++ ".join(f"{name}_rows_{c}" for c in range(nchunks)) if nchunks else "[]"
    out.append(f"/-- prism {j}: seam {seam[0]}/{seam[1]}, floor {Fn}/{Fd}, E = {E}, D = {D}. -/\n")
    out.append(f"def {name} : PrismData where\n")
    out.append(f"  tn := {seam[0]}\n  td := {seam[1]}\n  K := {K}\n  A := {A}\n")
    for e in ("bottom", "right", "top", "left"):
        out.append(f"  {e} := [" + ", ".join(pair_lit(q) for q in mesh[e]) + "]\n")
    out.append(f"  rows := {rows_expr}\n")
    out.append(f"  Fn := {Fn}\n  Fd := {Fd}\n  E := {E}\n  D := {D}\n\n")
    return "".join(out), name, len(rows)

def barrier_block(names, prefix, t0, leg_desc):
    Bname = f"row2Barrier{prefix.upper()}"
    return (f"/-- the {leg_desc} barrier certificate for row 2. -/\n"
            f"def {Bname} : BarrierData where\n"
            f"  rect := row2Rect\n  t0n := {t0[0]}\n  t0d := {t0[1]}\n"
            f"  prisms := [{', '.join(names)}]\n\n")

def asym_block(json_path, prefix, leg_desc):
    """the `AsymData` literal exactly as emit_lean_lane_a.emit writes it (same pins, same UNTRUSTED pre-check)."""
    d = json.load(open(json_path))
    if d.get("kind") != "asymptotic" or d.get("format") != "M2a-barrier-transcript":
        raise SystemExit(f"not an asymptotic M2a transcript: {json_path}")
    K = as_written(d["scales"]["K"], "K")
    t0 = (as_written(d["t0"]["n"], "t0.n"), as_written(d["t0"]["d"], "t0.d"))
    y0 = (as_written(d["y0"]["n"], "y0.n"), as_written(d["y0"]["d"], "y0.d"))
    yA = (as_written(d["yA"]["n"], "yA.n"), as_written(d["yA"]["d"], "yA.d"))
    rows = [tuple(as_written(r[k], f"rows[{i}].{k}") for k in ("Nlo", "Nhi", "T", "E")) for i, r in enumerate(d["rows"])]
    tail = tuple(as_written(d["tail"][k], f"tail.{k}") for k in ("N1", "Q1", "Q2", "Q3", "Q4", "E1"))
    for name, got, want in (("t0", t0, LANEA.PIN_T0), ("y0", y0, LANEA.PIN_Y0), ("yA", yA, LANEA.PIN_YA)):
        if got != want: raise SystemExit(f"{name} = {got} is not the instance's {want}")
    if rows[0][0] != LANEA.PIN_NSTART or tail[0] != LANEA.PIN_N1: raise SystemExit("N_start / N1 pin failed")
    precheck(K, t0, y0, yA, rows, tail)
    from fractions import Fraction
    Kf = Fraction(int(K)); tsum = sum(int(q) for q in tail[1:])
    def f7(n): return f"{float(Fraction(int(n)) / Kf):.7g}"
    prod = d.get("producer", {}); stamp = prod.get("stamp", "?")
    lit = f"row2Asym{prefix.upper()}"
    out = [f"""/-- the {leg_desc}'s Lane A transcript (asym-{prefix}.json, producer stamp {stamp}), integers as written:
K = {LANEA.pow10(K)}, t₀ = {t0[0]}/{t0[1]}, y₀ = {y0[0]}/{y0[1]}, yA = {yA[0]}/{yA[1]}; rows ⟨Nlo, Nhi, T, E⟩ with
T/K ≈ {", ".join(f7(r[2]) for r in rows)}; tail ⟨N₁, Q₁, Q₂, Q₃, Q₄, E₁⟩ with Σ/K ≈ {float(tsum / Kf):.10f} < 2. -/
def {lit} : AsymData :=
  {{ K := {K},
    t0n := {t0[0]},
    t0d := {t0[1]},
    y0n := {y0[0]},
    y0d := {y0[1]},
    yAn := {yA[0]},
    yAd := {yA[1]},
    rows := [
"""]
    for i, r in enumerate(rows):
        sep = "," if i < len(rows) - 1 else "],"
        out.append(f"      ⟨{r[0]}, {r[1]}, {r[2]}, {r[3]}⟩{sep}\n")
    out.append(f"    tail := ⟨{tail[0]}, {tail[1]}, {tail[2]}, {tail[3]}, {tail[4]}, {tail[5]}⟩ }}\n\n")
    return "".join(out)

def leg(manifest_path, prefix, leg_desc):
    m = json.load(open(manifest_path)); base = os.path.dirname(os.path.abspath(manifest_path))
    rect = tuple(rat(m["rect"][k]) for k in ("x1", "x2", "y1", "y2")); t0 = rat(m["t0"])
    blocks, names, nrows = [], [], 0
    for e in m["prisms"]:
        p = json.load(open(os.path.join(base, e["file"]))); j = int(e["index"]); assert int(p["index"]) == j
        b, name, n = prism_blocks(p, j, prefix); blocks.append(b); names.append(name); nrows += n
    blocks.append(barrier_block(names, prefix, t0, leg_desc))
    return rect, t0, "".join(blocks), len(names), nrows

def main():
    mp_man, arb_man, asym_mp, asym_arb, root = sys.argv[1:6]
    rect_mp, t0_mp, mp_txt, nmp, rmp = leg(mp_man, "mp", "mpmath-ball leg (transcripts/row2)")
    rect_arb, t0_arb, arb_txt, narb, rarb = leg(arb_man, "arb", "Arb/FLINT leg (transcripts/row2-arb)")
    assert rect_mp == rect_arb and t0_mp == t0_arb, "the two legs must share the rectangle and t₀"
    hdr = HEADER.format(nmp=nmp, rmp=rmp, lastmp=f"{nmp-1:04d}", narb=narb, rarb=rarb, lastarb=f"{narb-1:04d}")
    body = [hdr, "/-! ## 1. The rectangle (Zeta23/DBN/Instance02/Rect.lean) -/\n\n", rect_block(rect_mp),
            "/-! ## 2. Lane B, mpmath-ball leg (Zeta23/DBN/Instance02/mp_0000 … mp_Barrier) -/\n\n", mp_txt,
            "/-! ## 3. Lane B, Arb/FLINT leg (Zeta23/DBN/Instance02/arb_0000 … arb_Barrier) -/\n\n", arb_txt,
            "/-! ## 4. Lane A, both legs (Zeta23/DBN/Instance02/Asym_mp, Asym_arb) -/\n\n",
            asym_block(asym_mp, "mp", "mpmath-ball leg"), asym_block(asym_arb, "arb", "Arb/FLINT leg"),
            "end DBN\n"]
    path = os.path.join(root, "comparator", "ChallengeDeps", "DBN", "Instance02.lean")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write("".join(body))
    print(f"wrote {path}: mp {nmp} prisms / {rmp} rows; arb {narb} prisms / {rarb} rows; Lane A both legs")

if __name__ == "__main__":
    main()
