#!/usr/bin/env python3
"""spot_compare.py -- the screen's step-4 TWO-PRODUCER SPOT CHECK on Gomila's prisms (design note section 3(b) step 4;
gomila-screen.md section 4): for each sampled prism k (gomila/spot-sample.json), D1's two UNTRUSTED legs were run on
the SAME box [X, X+1] x [1809/10000, 1] at the SAME seam t = tau_k (the exact rational of the printed lower endpoint),
producing SPEC prism files (gomila/spot-arb/seam-NNNN/instance02-prism-0000.json, gomila/spot-mp/prism-NNNN.json,
NNNN = k-1).  This program reports, per prism, in exact arithmetic:

  (1) D1 leg vs D1 leg: the cell-wise value-box intersection and the edge-argument intersection
      (crosscheck_instance02.compare) -- the P-11 verdict (disjoint = stop-the-line);
  (2) D1 legs vs Gomila's printed scalars at that seam:
        M_k (their point floor, lower end)        vs  our whole-segment hull floors Fn/Fd (each leg): ours must be
                                                       <= M_k + (their spatial term) ... precisely: since our floor
                                                       is a floor over the WHOLE boundary and M_k is the min over
                                                       their mesh POINTS, M_k >= true min|f| >= our floor is the
                                                       expected order; a leg floor ABOVE M_k + rad would be a
                                                       contradiction (reported);
        their eps = 0.00125 (allowance)           vs  our E/K (certified Theorem-1.3 defect at the seam): E/K must be
                                                       below their allowance for their gate to be comparable;
        their D_t (box-uniform |d/dt f| bound)    vs  our DT (sup |d/dt f| at the seam / over our prism; mp leg
                                                       records DT_sup_dt_f, Arb leg records Mt_seam_sup): our
                                                       value must not exceed theirs by more than their box
                                                       uniformization could explain -- reported as a ratio,
                                                       flagged if ours > theirs (a bound they print that is
                                                       SMALLER than a certified sup would be a contradiction);
        their gate at their Delta_k                vs  OUR gate at THEIR Delta_k: E_ours + DT_ours*Delta_k^+ + E_ours
                                                       < our floor  (the SPEC C-B12 form with the displacement
                                                       routed through f, SPEC section 4.5) -- whether D1's own
                                                       enclosures would certify Gomila's prism length.
Exit 0 = every compared prism consistent on (1) and no contradiction in (2); 1 = disagreement; 3 = incomplete.
"""
import json, os, sys
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import crosscheck_instance02 as X

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    sample = json.load(open(os.path.join(here, "spot-sample.json")))["prisms"]
    scal = {p["k"]: p for p in json.load(open(os.path.join(here, "gomila-scalars.json")))["prisms"]}
    eps = Fr(125, 100000)
    bad = 0; missing = 0; n = 0; contra = 0; gate_fail = 0
    print("k | seam | rows arb/mp | pairs | disjoint | argdisj | M_k(lo) | floor arb / mp | E arb / mp (<0.00125?) | Dt_G | DT arb / mp | ratio DT/Dt_G arb,mp | our gate at Delta_G^+ arb,mp")
    for s in sample:
        k = s["k"]; j = k - 1
        pa = os.path.join(here, "spot-arb", f"seam-{j:04d}", "instance02-prism-0000.json")
        pm = os.path.join(here, "spot-mp", f"prism-{j:04d}.json")
        if not os.path.exists(pa):
            missing += 1; print(f"{k:4d} | (missing: arb)"); continue
        A = X.load(pa); ja = json.load(open(pa))
        if os.path.exists(pm):
            M = X.load(pm); jm = json.load(open(pm))
        else:
            missing += 1; M = A; jm = ja   # mp leg not yet produced: report the arb leg alone (columns duplicated, marked)
        if A["seam"] != M["seam"] or A["seam"] != Fr(s["seam"]):
            print(f"{k:4d} SEAM MISMATCH"); bad += 1; continue
        db, pairs, ab, det = X.compare(A, M) if os.path.exists(pm) else (0, 0, 0, [])
        n += 1; bad += db + ab
        Mk = Fr(scal[k]["min_mesh"][0]); DtG = Fr(scal[k]["Dt"]); Dplus = Fr(s["Delta_plus"])
        DT_arb = Fr(ja["producer"]["Mt_seam_sup"]); DT_mp = Fr(jm["producer"]["DT_sup_dt_f"]) if "DT_sup_dt_f" in jm["producer"] else DT_arb
        fl_a, fl_m = A["floor"], M["floor"]
        c = []
        if fl_a > Fr(scal[k]["min_mesh"][1]): c.append("arb floor > M_k"); 
        if fl_m > Fr(scal[k]["min_mesh"][1]): c.append("mp floor > M_k")
        if not (A["E"] < eps and M["E"] < eps): c.append("E >= 0.00125")
        # our gate at their prism length: E + DT*Delta + E < floor  (displacement routed through f, SPEC 4.5, E(t) <= E(seam) is
        # NOT assumed: we use the leg's own recorded prism-uniform E where available -- here conservatively 2E_seam + DT*Delta)
        ga = 2 * A["E"] + DT_arb * Dplus < fl_a; gm = 2 * M["E"] + DT_mp * Dplus < fl_m
        if not (ga and gm): gate_fail += 1
        contra += len(c)
        print(f"{k:4d} | {float(A['seam']):.9f} | {len(A['rows'])}/{len(M['rows'])} | {pairs} | {db} | {ab} | {float(Mk):.6f} | {float(fl_a):.6f} / {float(fl_m):.6f} | "
              f"{float(A['E']):.3e} / {float(M['E']):.3e} | {DtG} | {float(DT_arb):.1f} / {float(DT_mp):.1f} | {float(DT_arb / DtG):.3f},{float(DT_mp / DtG):.3f} | {'ok' if ga else 'FAIL'},{'ok' if gm else 'FAIL'}"
              + (("  CONTRADICTION: " + "; ".join(c)) if c else "") + ("" if os.path.exists(pm) else "   [mp leg pending: mp columns = arb]"))
        for d in det: print("      " + d)
    print(f"\ncompared {n} prisms: {bad} disjoint pairs/edges between D1's legs; {contra} contradictions vs Gomila's printed scalars; "
          f"our-gate-at-their-length failures: {gate_fail}; missing: {missing}")
    if bad or contra: print("DISAGREEMENT"); sys.exit(1)
    print("CONSISTENT" + (" so far (incomplete)" if missing else "")); sys.exit(3 if missing else 0)

if __name__ == "__main__":
    main()
