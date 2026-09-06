#!/usr/bin/env python3
"""crosscheck_lane_a.py -- SPEC P-11 two-producer cross-check for Lane A: per row T and E, and the five tail quantities,
between the mpmath leg (batches/mp-row_*.json, mp-tail.json) and the Arb leg (batches/arb-row_*.json, arb-tail.json).
Rule (P-11): each leg's pre-rounding enclosure must be consistent with the other's -- for the floors the two lower bounds
T_lo must agree to within a stated tolerance (they bound the same derived quantity with the same formulas), have the same
sign, and both legs must reach the same ok verdict; for E and the tail quantities the two upper bounds must agree to the
tolerance.  Disagreement = exit 1 (stop-the-line).  Exact rational arithmetic on the recorded endpoints.
usage: crosscheck_lane_a.py DIR [--rtol 1e-9] [--atol 1e-12]"""
import glob, json, os, sys
from fractions import Fraction as Fr

def fr(s): return Fr(s)

def close(a, b, rtol, atol):
    return abs(a - b) <= atol + rtol * max(abs(a), abs(b))

def main():
    d = sys.argv[1]; rtol = Fr(sys.argv[sys.argv.index("--rtol") + 1]) if "--rtol" in sys.argv else Fr(1, 10**9)
    atol = Fr(sys.argv[sys.argv.index("--atol") + 1]) if "--atol" in sys.argv else Fr(1, 10**12)
    bad = 0; n = 0
    mp = {os.path.basename(p)[7:11]: json.load(open(p)) for p in glob.glob(os.path.join(d, "batches", "mp-row_*.json"))}
    ar = {os.path.basename(p)[8:12]: json.load(open(p)) for p in glob.glob(os.path.join(d, "batches", "arb-row_*.json"))}
    for k in sorted(set(mp) & set(ar)):
        a, b = mp[k], ar[k]; n += 1
        if "error" in a or "error" in b:
            print(f"row {k}: ERROR recorded: mp={a.get('error')} arb={b.get('error')}"); bad += 1; continue
        Ta, Tb, Ea, Eb = fr(a["T_lo"]), fr(b["T_lo"]), fr(a["E_hi"]), fr(b["E_hi"])
        okT = close(Ta, Tb, rtol, atol) and ((Ta > 0) == (Tb > 0))
        okE = close(Ea, Eb, rtol, atol)
        okV = (a["ok"] == b["ok"])
        # per-piece comparison
        pc = all(close(fr(pa["T_lo"]), fr(pb["T_lo"]), rtol, atol) for pa, pb in zip(a["pieces"], b["pieces"])) and len(a["pieces"]) == len(b["pieces"])
        st = "OK" if (okT and okE and okV and pc) else "DISAGREE"
        if st != "OK": bad += 1
        print(f"row {k} [{a['Nlo']},{a['Nhi']}]: T_lo mp={float(Ta):.12f} arb={float(Tb):.12f} (rel diff {float(abs(Ta-Tb)/max(abs(Ta),abs(Tb),Fr(1,10**30))):.2e}); "
              f"E_hi mp={float(Ea):.6e} arb={float(Eb):.6e} (rel {float(abs(Ea-Eb)/max(Ea,Eb)):.2e}); ok mp={a['ok']} arb={b['ok']}; pieces {len(a['pieces'])}/{len(b['pieces'])} agree={pc} -> {st}")
    tm, ta = os.path.join(d, "batches", "mp-tail.json"), os.path.join(d, "batches", "arb-tail.json")
    if os.path.exists(tm) and os.path.exists(ta):
        A, B = json.load(open(tm)), json.load(open(ta)); n += 1
        line = []; okall = A["N1"] == B["N1"] and A["ok"] == B["ok"]
        for q in ("Q1", "Q2", "Q3", "Q4", "E1"):
            va, vb = fr(A[q]), fr(B[q]); c = close(va, vb, rtol, atol); okall &= c
            line.append(f"{q}: {float(va):.10g}/{float(vb):.10g} rel {float(abs(va-vb)/max(va,vb)):.1e}{'' if c else ' MISMATCH'}")
        st = "OK" if okall else "DISAGREE"
        if st != "OK": bad += 1
        print(f"tail N1={A['N1']}/{B['N1']}: " + "; ".join(line) + f"; sum {A['sum_float']:.6f}/{B['sum_float']:.6f}; ok {A['ok']}/{B['ok']} -> {st}")
    print(f"compared {n} items; disagreements {bad}; " + ("CONSISTENT" if bad == 0 else "DISAGREEMENT -- stop the line"))
    sys.exit(0 if bad == 0 else 1)

if __name__ == "__main__":
    main()
