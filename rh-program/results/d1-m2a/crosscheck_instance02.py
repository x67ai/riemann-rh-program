#!/usr/bin/env python3
"""crosscheck_instance02.py -- M2a item (e), the TWO-PRODUCER CROSS-CHECK (SPEC.md P-11; design note section 4:
disagreement beyond radii is stop-the-line).  For every seam of a chain produced by leg X, the other leg Y was run
for one prism at exactly that seam (xcheck_*_at_seams.py).  This program compares, per seam, in exact rational
arithmetic (Fraction; no float is used in any verdict):

  (1) CELL-WISE VALUE BOXES on the common mesh refinement: for every pair of overlapping boundary segments (same
      edge, overlapping parameter intervals) the two value boxes [reLo,reHi]/K x [imLo,imHi]/K must INTERSECT --
      both enclose f_tau on the overlap, so a disjoint pair means at least one enclosure is false (stop-the-line);
  (2) ARGUMENT ROWS per edge: each leg's edge-total argument increment interval (sum of its rows over the edge, at
      scale A) must intersect the other's -- both enclose the same arg increment of f_tau along the edge;
  (3) the FLOOR: each leg's certified floor Fn/Fd must not exceed the other leg's maximum box modulus... more
      precisely floor_X <= sup over Y's boxes of |box| is implied by (1); reported: both floors and the ratio;
  (4) E and D: upper bounds obtained by different majorants -- reported with their ratio; agreement in order of
      magnitude expected, no verdict (they are not enclosures of the same number);
  (5) the winding: both legs' sums must contain 0 (each leg's own C-B9), reported.

usage: crosscheck_instance02.py <chain-manifest.json> <dir-of-other-leg-prisms> [--layout arbdirs|mpflat]
  arbdirs : <dir>/seam-NNNN/instance02-prism-0000.json (Arb leg run at the mp seams)
  mpflat  : <dir>/prism-NNNN.json                        (mp leg run at the Arb seams)
exit 0 = CONSISTENT at every compared seam, 1 = DISAGREEMENT (stop-the-line), 3 = some seams not yet produced.
"""
import argparse, json, os, sys
from fractions import Fraction as Fr

def rat(o): return Fr(int(o["n"]), int(o["d"]))

def load(path):
    p = json.load(open(path))
    K = int(p["scales"]["K"]); A = int(p["scales"]["A"])
    mesh = {e: [rat(r) for r in p["mesh"][e]] for e in ("bottom", "right", "top", "left")}
    rows = [tuple(int(r[k]) for k in ("reLo", "reHi", "imLo", "imHi", "argLo", "argHi")) for r in p["segments"]]
    segs = []
    for e in ("bottom", "right", "top", "left"):
        m = mesh[e]
        for a, b in zip(m, m[1:]): segs.append((e, min(a, b), max(a, b)))
    assert len(segs) == len(rows), path
    return dict(K=K, A=A, segs=segs, rows=rows, seam=rat(p["seam"]), floor=Fr(int(p["modulus_floor"]["Fn"]), int(p["modulus_floor"]["Fd"])),
                E=Fr(int(p["approx_defect"]), K), D=Fr(int(p["displacement"]), K), path=path)

def box(r, K): return (Fr(r[0], K), Fr(r[1], K), Fr(r[2], K), Fr(r[3], K))

def compare(a, b):
    """returns (disjoint_pairs, pairs, arg_disjoint_edges, details)"""
    bad = 0; pairs = 0; argbad = 0; det = []
    for e in ("bottom", "right", "top", "left"):
        ia = [i for i, s in enumerate(a["segs"]) if s[0] == e]
        ib = [j for j, s in enumerate(b["segs"]) if s[0] == e]
        # (1) value boxes on the common refinement
        for i in ia:
            _, lo_a, hi_a = a["segs"][i]; ba = box(a["rows"][i], a["K"])
            for j in ib:
                _, lo_b, hi_b = b["segs"][j]
                if hi_b <= lo_a or hi_a <= lo_b: continue
                bb = box(b["rows"][j], b["K"]); pairs += 1
                if ba[1] < bb[0] or bb[1] < ba[0] or ba[3] < bb[2] or bb[3] < ba[2]:
                    bad += 1
                    if len(det) < 6: det.append(f"DISJOINT {e} A[{i}]={tuple(float(v) for v in ba)} B[{j}]={tuple(float(v) for v in bb)}")
        # (2) edge-total argument increment (turns)
        Sa = (Fr(sum(a["rows"][i][4] for i in ia), a["A"]), Fr(sum(a["rows"][i][5] for i in ia), a["A"]))
        Sb = (Fr(sum(b["rows"][j][4] for j in ib), b["A"]), Fr(sum(b["rows"][j][5] for j in ib), b["A"]))
        if Sa[1] < Sb[0] or Sb[1] < Sa[0]:
            argbad += 1; det.append(f"ARG-DISJOINT {e}: A [{float(Sa[0]):.9f},{float(Sa[1]):.9f}] B [{float(Sb[0]):.9f},{float(Sb[1]):.9f}] turns")
    return bad, pairs, argbad, det

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest"); ap.add_argument("other"); ap.add_argument("--layout", choices=("arbdirs", "mpflat"), required=True)
    ap.add_argument("--labels", default="chain,other")
    a = ap.parse_args()
    la, lb = a.labels.split(",")
    man = json.load(open(a.manifest)); base = os.path.dirname(os.path.abspath(a.manifest))
    missing = 0; total_bad = 0; total_pairs = 0; total_argbad = 0; n = 0
    print(f"seam | tau | rows {la}/{lb} | overlapping pairs | disjoint | arg-disjoint edges | floor {la} / {lb} | E {la} / {lb} | D {la} / {lb} | winding {la} | winding {lb}")
    for e in man["prisms"]:
        j = int(e["index"])
        pa = load(os.path.join(base, e["file"]))
        pb_path = os.path.join(a.other, f"seam-{j:04d}", "instance02-prism-0000.json") if a.layout == "arbdirs" else os.path.join(a.other, f"prism-{j:04d}.json")
        if not os.path.exists(pb_path):
            missing += 1; print(f"{j:4d} | {float(pa['seam']):.9f} | (not produced yet)"); continue
        pb = load(pb_path)
        if pa["seam"] != pb["seam"]:
            print(f"{j:4d} SEAM MISMATCH {pa['seam']} vs {pb['seam']}"); total_bad += 1; continue
        bad, pairs, argbad, det = compare(pa, pb)
        n += 1; total_bad += bad; total_pairs += pairs; total_argbad += argbad
        wa = (sum(r[4] for r in pa["rows"]), sum(r[5] for r in pa["rows"])); wb = (sum(r[4] for r in pb["rows"]), sum(r[5] for r in pb["rows"]))
        print(f"{j:4d} | {float(pa['seam']):.9f} | {len(pa['rows'])}/{len(pb['rows'])} | {pairs} | {bad} | {argbad} | "
              f"{float(pa['floor']):.6f} / {float(pb['floor']):.6f} | {float(pa['E']):.4e} / {float(pb['E']):.4e} | "
              f"{float(pa['D']):.4e} / {float(pb['D']):.4e} | [{wa[0]},{wa[1]}]/{pa['A']:.0e} | [{wb[0]},{wb[1]}]/{pb['A']:.0e}")
        for d in det: print("      " + d)
    print(f"\ncompared {n} seams, {total_pairs} overlapping segment pairs: {total_bad} disjoint value-box pairs, {total_argbad} disjoint edge-argument intervals; {missing} seams not yet produced")
    if total_bad or total_argbad:
        print("DISAGREEMENT -- stop the line (design note section 4)"); sys.exit(1)
    print("CONSISTENT" + ("" if not missing else " so far (incomplete)"))
    sys.exit(3 if missing else 0)

if __name__ == "__main__":
    main()
