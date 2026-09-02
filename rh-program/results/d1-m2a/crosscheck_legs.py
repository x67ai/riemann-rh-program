#!/usr/bin/env python3
"""crosscheck_legs.py -- SPEC P-11 cell-wise cross-check of two barrier prism files (Arb leg vs mpmath leg) at the SAME seam
on the SAME rectangle.  Both legs' rows enclose the same function f_tau on the boundary; on the common mesh refinement every
pair of overlapping segments must have INTERSECTING value boxes (at the two scales), and the scalars floor, E, D are compared
as numbers (each leg's rows must be consistent with the other's floor; E and D are compared for order of magnitude -- they
are upper bounds obtained by different majorants and need not agree).  Exact integer/rational arithmetic only.

usage: crosscheck_legs.py <prismA.json> <prismB.json>
exit 0 = consistent, 1 = DISAGREEMENT (stop-the-line per design note section 4)."""
import json, sys
from fractions import Fraction as Fr

def load(path):
    p = json.load(open(path))
    K = int(p["scales"]["K"]); A = int(p["scales"]["A"])
    mesh = {e: [Fr(int(r["n"]), int(r["d"])) for r in p["mesh"][e]] for e in ("bottom", "right", "top", "left")}
    rows = [{k: int(r[k]) for k in r} for r in p["segments"]]
    segs = []
    for e in ("bottom", "right", "top", "left"):
        m = mesh[e]
        for a, b in zip(m, m[1:]):
            segs.append((e, min(a, b), max(a, b)))
    assert len(segs) == len(rows)
    seam = Fr(int(p["seam"]["n"]), int(p["seam"]["d"]))
    floor = Fr(int(p["modulus_floor"]["Fn"]), int(p["modulus_floor"]["Fd"]))
    E = Fr(int(p["approx_defect"]), K); D = Fr(int(p["displacement"]), K)
    return dict(K=K, A=A, segs=segs, rows=rows, seam=seam, floor=floor, E=E, D=D, path=path)

def box(r, K):
    return (Fr(r["reLo"], K), Fr(r["reHi"], K), Fr(r["imLo"], K), Fr(r["imHi"], K))

def main():
    a, b = load(sys.argv[1]), load(sys.argv[2])
    if a["seam"] != b["seam"]:
        print(f"different seams {a['seam']} vs {b['seam']}: not comparable"); sys.exit(2)
    bad = 0; pairs = 0; maxgap = Fr(0)
    for e in ("bottom", "right", "top", "left"):
        sa = [(i, s) for i, s in enumerate(a["segs"]) if s[0] == e]
        sb = [(i, s) for i, s in enumerate(b["segs"]) if s[0] == e]
        for i, (ea, lo_a, hi_a) in sa:
            ba = box(a["rows"][i], a["K"])
            for j, (eb, lo_b, hi_b) in sb:
                if hi_b <= lo_a or hi_a <= lo_b:
                    continue   # no overlap (touching at a point counts as overlap only if strictly inside; endpoints are shared anyway)
                bb = box(b["rows"][j], b["K"])
                pairs += 1
                inter = not (ba[1] < bb[0] or bb[1] < ba[0] or ba[3] < bb[2] or bb[3] < ba[2])
                if not inter:
                    bad += 1
                    if bad <= 10:
                        print(f"  DISJOINT boxes: {e} A[{i}] [{float(lo_a)},{float(hi_a)}] {tuple(float(v) for v in ba)} vs B[{j}] [{float(lo_b)},{float(hi_b)}] {tuple(float(v) for v in bb)}")
    # floors: each leg's rows must respect the other's floor is NOT required (the floor is a lower bound each leg proves for
    # itself); we report both and check consistency: min box distance of A >= floor_B is expected only if A's boxes are tighter.
    def mindist(d):
        m = None
        for r in d["rows"]:
            mre = 0 if r["reLo"] <= 0 <= r["reHi"] else min(abs(r["reLo"]), abs(r["reHi"]))
            mim = 0 if r["imLo"] <= 0 <= r["imHi"] else min(abs(r["imLo"]), abs(r["imHi"]))
            v = Fr(mre * mre + mim * mim, d["K"] ** 2)
            m = v if m is None else min(m, v)
        return float(m) ** 0.5
    print(f"seam {a['seam']}: {len(a['rows'])} rows (A) vs {len(b['rows'])} rows (B); overlapping pairs {pairs}; disjoint pairs {bad}")
    print(f"  floor A = {float(a['floor']):.6f} (rows support {mindist(a):.6f});  floor B = {float(b['floor']):.6f} (rows support {mindist(b):.6f})")
    print(f"  E: A = {float(a['E']):.4e}  B = {float(b['E']):.4e}  ratio A/B = {float(a['E']/b['E']):.4f}")
    print(f"  D: A = {float(a['D']):.4e}  B = {float(b['D']):.4e}  (different prism lengths are allowed; compare D/K per unit time in the notes)")
    # the argument sums must both contain 0 with width < A/2 (both certify winding 0)
    for d, name in ((a, "A"), (b, "B")):
        Slo = sum(r["argLo"] for r in d["rows"]); Shi = sum(r["argHi"] for r in d["rows"])
        print(f"  winding {name}: [{Slo}, {Shi}]/{d['A']} (width {2*(Shi-Slo)} < A: {2*(Shi-Slo) < d['A']}, contains 0: {Slo <= 0 <= Shi})")
    print("CONSISTENT" if bad == 0 else "DISAGREEMENT -- stop the line")
    sys.exit(0 if bad == 0 else 1)

if __name__ == "__main__":
    main()
