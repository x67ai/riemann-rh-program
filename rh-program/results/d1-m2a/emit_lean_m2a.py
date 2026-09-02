#!/usr/bin/env python3
"""emit_lean_m2a.py -- UNTRUSTED JSON -> Lean emitter for M2a barrier transcripts (SPEC.md section 7.6, item P-12).

Writes, for a barrier manifest and a Lean name prefix P (e.g. `mp`, `arb`):
  <lean-root>/Zeta23/DBN/Instance02/Rect.lean            -- `row2Rect : RectData` (once; shared by both legs)
  <lean-root>/Zeta23/DBN/Instance02/<P>_NNNN.lean         -- one module per prism: row chunks of <= 1000 rows
                                                             (`<P>NNNN_rows_k`), `<P>NNNN : PrismData`, and the kernel
                                                             fact `<P>NNNN_check : checkPrism row2Rect <P>NNNN = true`
                                                             by `decide +kernel`
  <lean-root>/Zeta23/DBN/Instance02/<P>_Barrier.lean      -- `row2Barrier<P> : BarrierData`, the chain fact, the
                                                             per-prism assembly, and (optionally) the monolithic
                                                             `checkBarrier` fact
The emitter is untrusted: its fidelity is established by verify_lean_m2a.py (an independent back-parse of the
emitted modules against the JSON, field by field and row by row), and everything that matters is re-checked by
the kernel from the literals.  Program header: Copyright 2026 Kunal Tyagi, Apache-2.0 (as the other program files).

usage: emit_lean_m2a.py <manifest.json> <lean-root> <prefix> [--chunk 1000] [--no-monolithic]
"""
import argparse, json, os, sys
from fractions import Fraction

HEADER = """/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library; it imports it.
-/
"""

def rat(o):
    return (int(o["n"]), int(o["d"]))

def pair_lit(p):
    return f"({p[0]}, {p[1]})"

def row_lit(r):
    return "⟨" + ", ".join(str(int(r[k])) for k in ("reLo", "reHi", "imLo", "imHi", "argLo", "argHi")) + "⟩"

def emit_rect(rect, t0, root):
    path = os.path.join(root, "Zeta23", "DBN", "Instance02", "Rect.lean")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    (x1, x2, y1, y2) = rect
    body = HEADER + f"""/-
Zeta23/DBN/Instance02/Rect.lean — the common rectangle and final time of the Instance02 barrier certificate
(Polymath15 Table 1 row 2, SPEC.md §9): R = [X, X+1] × [y₀, 1] with X = 5 000 000 194 858, y₀ = 16733/100000,
t₀ = 93/500.  Its own small module so that the per-prism modules (SPEC.md §7.6) import it and not the prism list.
Mechanically emitted by results/d1-m2a/emit_lean_m2a.py (UNTRUSTED); verified by verify_lean_m2a.py.
-/
import Zeta23.DBN.BarrierCert

namespace Zeta23
namespace DBN
namespace Instance02

/-- R = [{x1[0]}/{x1[1]}, {x2[0]}/{x2[1]}] × [{y1[0]}/{y1[1]}, {y2[0]}/{y2[1]}] (SPEC.md §9). -/
def row2Rect : RectData :=
  ⟨{x1[0]}, {x1[1]}, {x2[0]}, {x2[1]}, {y1[0]}, {y1[1]}, {y2[0]}, {y2[1]}⟩

/-- t₀ = {t0[0]}/{t0[1]} as the pair (t0n, t0d). -/
def row2T0n : ℤ := {t0[0]}
def row2T0d : ℤ := {t0[1]}

end Instance02
end DBN
end Zeta23
"""
    with open(path, "w") as fh: fh.write(body)
    return path

def emit_prism(p, j, prefix, root, chunk, leg_desc):
    name = f"{prefix}{j:04d}"
    path = os.path.join(root, "Zeta23", "DBN", "Instance02", f"{prefix}_{j:04d}.lean")
    rows = p["segments"]
    seam = rat(p["seam"])
    K, A = int(p["scales"]["K"]), int(p["scales"]["A"])
    Fn, Fd = int(p["modulus_floor"]["Fn"]), int(p["modulus_floor"]["Fd"])
    E, D = int(p["approx_defect"]), int(p["displacement"])
    mesh = {e: [rat(r) for r in p["mesh"][e]] for e in ("bottom", "right", "top", "left")}
    out = [HEADER, f"""/-
Zeta23/DBN/Instance02/{prefix}_{j:04d}.lean — prism {j} of the {leg_desc} Instance02 barrier transcript
(seam τ = {seam[0]}/{seam[1]}, {len(rows)} rows, K = {K}, A = {A}), as a `PrismData` literal with its kernel fact
`{name}_check : checkPrism row2Rect {name} = true` (`decide +kernel`; no `native_decide`).  UNTRUSTED producer
data, mechanically emitted by results/d1-m2a/emit_lean_m2a.py and back-parse-verified by verify_lean_m2a.py.
The theorem is a statement about integers: C-B0..C-B12 hold for these literals.  Nothing analytic is asserted
here — H2-B (the enclosure claims) and hHol stay displayed (SPEC.md §6).
-/
import Zeta23.DBN.Instance02.Rect

namespace Zeta23
namespace DBN
namespace Instance02

set_option maxRecDepth 100000

"""]
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
    out.append(f"/-- kernel fact: C-B0..C-B12 hold for prism {j} (integer relations only). -/\n")
    out.append(f"theorem {name}_check : checkPrism row2Rect {name} = true := by decide +kernel\n\n")
    out.append("end Instance02\nend DBN\nend Zeta23\n")
    with open(path, "w") as fh: fh.write("".join(out))
    return path, name

def emit_barrier(names, prefix, root, t0, leg_desc, monolithic, nrows):
    path = os.path.join(root, "Zeta23", "DBN", "Instance02", f"{prefix}_Barrier.lean")
    Bname = f"row2Barrier{prefix.upper()}"
    out = [HEADER, f"""/-
Zeta23/DBN/Instance02/{prefix}_Barrier.lean — the {leg_desc} Instance02 barrier certificate assembled:
`{Bname} : BarrierData` ({len(names)} prisms, {nrows} rows, t₀ = {t0[0]}/{t0[1]}), the chain fact
`{Bname}_chain : checkBarrierChain {Bname} = true` (C-B0 global, C-B2′, C-B13; `decide +kernel`), the split
per-prism fact `{Bname}_prisms : ∀ p ∈ {Bname}.prisms, checkPrism {Bname}.rect p = true` assembled from the
per-prism modules (SPEC.md §7.6), and the monolithic `{Bname}_check : checkBarrier {Bname} = true`.
UNTRUSTED producer data, emitted by results/d1-m2a/emit_lean_m2a.py; the theorems are integer facts.  The
analytic conclusion is `cert_of_checkBarrier` applied to these facts MODULO H2-B and hHol — see Instance02.lean.
-/
"""]
    for n in names:
        out.append(f"import Zeta23.DBN.Instance02.{prefix}_{n[len(prefix):]}\n")
    out.append(f"""
namespace Zeta23
namespace DBN
namespace Instance02

set_option maxRecDepth 100000

/-- the {leg_desc} barrier certificate for row 2. -/
def {Bname} : BarrierData where
  rect := row2Rect
  t0n := {t0[0]}
  t0d := {t0[1]}
  prisms := [{", ".join(names)}]

/-- C-B0 (global), C-B2′, C-B13 for the {len(names)}-seam chain: first seam 0, strictly increasing, last seam < t₀. -/
theorem {Bname}_chain : checkBarrierChain {Bname} = true := by decide +kernel

/-- the split per-prism facts, assembled from the per-prism kernel theorems. -/
theorem {Bname}_prisms : ∀ p ∈ {Bname}.prisms, checkPrism {Bname}.rect p = true := by
  intro p hp
  simp only [{Bname}, List.mem_cons, List.not_mem_nil, or_false] at hp
  rcases hp with {" | ".join("rfl" for _ in names)}
  exacts [{", ".join(n + "_check" for n in names)}]
""")
    if monolithic:
        out.append(f"""
/-- the monolithic checker fact, from the chain fact and the per-prism facts (no second kernel evaluation of
the rows: `List.all_eq_true` turns `prisms.all` into the split fact `{Bname}_prisms`). -/
theorem {Bname}_check : checkBarrier {Bname} = true := by
  unfold checkBarrier
  rw [{Bname}_chain, Bool.true_and, List.all_eq_true]
  exact {Bname}_prisms
""")
    out.append("\nend Instance02\nend DBN\nend Zeta23\n")
    with open(path, "w") as fh: fh.write("".join(out))
    return path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest"); ap.add_argument("root"); ap.add_argument("prefix")
    ap.add_argument("--chunk", type=int, default=1000); ap.add_argument("--no-monolithic", action="store_true")
    ap.add_argument("--leg-desc", default="")
    a = ap.parse_args()
    m = json.load(open(a.manifest))
    base = os.path.dirname(os.path.abspath(a.manifest))
    rect = tuple(rat(m["rect"][k]) for k in ("x1", "x2", "y1", "y2"))
    t0 = rat(m["t0"])
    leg = a.leg_desc or f"{a.prefix}-leg"
    files = [emit_rect(rect, t0, a.root)]
    names = []; nrows = 0
    for e in m["prisms"]:
        p = json.load(open(os.path.join(base, e["file"])))
        j = int(e["index"]); assert int(p["index"]) == j
        assert rat(p["seam"]) == rat(e["seam"]) or Fraction(*rat(p["seam"])) == Fraction(*rat(e["seam"]))
        path, name = emit_prism(p, j, a.prefix, a.root, a.chunk, leg)
        files.append(path); names.append(name); nrows += len(p["segments"])
    files.append(emit_barrier(names, a.prefix, a.root, t0, leg, not a.no_monolithic, nrows))
    print(f"emitted {len(files)} modules ({len(names)} prisms, {nrows} rows) under {a.root}/Zeta23/DBN/Instance02/")
    for f in files: print("  ", f)

if __name__ == "__main__":
    main()
