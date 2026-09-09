#!/usr/bin/env python3
"""crosscheck_lane_a.py -- SPEC P-11 two-producer cross-check for Lane A: per row T and E, and the five tail quantities,
between the mpmath leg (batches/mp-row_*.json, mp-tail.json) and the Arb leg (batches/arb-row_*.json, arb-tail.json).

RULE (P-11 as applied to Lane B, arb-leg-notes.md section 5 / INSTANCE-REPORT.md section 2, carried over):
  * T_lo (the window floor) and the tail's Q1..Q4 are the SAME derived numbers (derivation M / Lemma T on the same exact
    rationals), computed independently at 288 and 320 bits: they must agree to rtol (default 1e-9), have the same sign, and
    both legs must reach the same ok verdict.  A larger difference = stop the line (exit 1).
  * E_hi and E1 are UPPER BOUNDS evaluated on x/y hulls (ball vs interval arithmetic; the dependency slack differs by
    library): they are reported side by side with the ratio; the verdict requires both legs ok and max/min <= 1 + etol
    (default 1e-3, the documented hull slack -- Lane B saw < 1e-4 on a 1-wide box, Lane A sees up to 6e-4 on a 10 000-window
    hull), and records which leg's bound is the larger.  Each leg's transcript carries its OWN E (one literal and one
    theorem per leg, D-R3; nothing merged), both legs' E < T being part of ok.
  Exact rational arithmetic on the recorded endpoints.  2026-09-09 (Session 19): the s17 draft applied rtol/atol to E as
  well, which fails on wide rows for the hull-slack reason above; amended to the Lane B rule.
usage: crosscheck_lane_a.py DIR [--rtol 1e-9] [--atol 1e-12] [--etol 1e-3]"""
import glob, json, os, sys
from fractions import Fraction as Fr

def fr(s): return Fr(s)

def close(a, b, rtol, atol):
    return abs(a - b) <= atol + rtol * max(abs(a), abs(b))

def ub_ok(a, b, etol):
    """two positive upper bounds of the same quantity: consistent if max/min <= 1 + etol."""
    if a <= 0 or b <= 0:
        return a == b
    return max(a, b) <= (1 + etol) * min(a, b)

def main():
    d = sys.argv[1]
    def opt(name, default):
        return Fr(sys.argv[sys.argv.index(name) + 1]) if name in sys.argv else default
    rtol = opt("--rtol", Fr(1, 10**9)); atol = opt("--atol", Fr(1, 10**12)); etol = opt("--etol", Fr(1, 10**3))
    bad = 0; n = 0; emax = Fr(0)
    mp = {os.path.basename(p)[7:11]: json.load(open(p)) for p in glob.glob(os.path.join(d, "batches", "mp-row_*.json"))}
    ar = {os.path.basename(p)[8:12]: json.load(open(p)) for p in glob.glob(os.path.join(d, "batches", "arb-row_*.json"))}
    for k in sorted(set(mp) & set(ar)):
        a, b = mp[k], ar[k]; n += 1
        if "error" in a or "error" in b:
            print(f"row {k}: ERROR recorded: mp={a.get('error')} arb={b.get('error')}"); bad += 1; continue
        Ta, Tb, Ea, Eb = fr(a["T_lo"]), fr(b["T_lo"]), fr(a["E_hi"]), fr(b["E_hi"])
        okT = close(Ta, Tb, rtol, atol) and ((Ta > 0) == (Tb > 0))
        okE = ub_ok(Ea, Eb, etol)
        okV = (a["ok"] == b["ok"])
        pc = all(close(fr(pa["T_lo"]), fr(pb["T_lo"]), rtol, atol) for pa, pb in zip(a["pieces"], b["pieces"])) and len(a["pieces"]) == len(b["pieces"])
        st = "OK" if (okT and okE and okV and pc) else "DISAGREE"
        if st != "OK": bad += 1
        erel = abs(Ea - Eb) / max(Ea, Eb); emax = max(emax, erel)
        print(f"row {k} [{a['Nlo']},{a['Nhi']}]: T_lo mp={float(Ta):.12f} arb={float(Tb):.12f} (rel diff {float(abs(Ta-Tb)/max(abs(Ta),abs(Tb),Fr(1,10**30))):.2e}); "
              f"E_hi mp={float(Ea):.6e} arb={float(Eb):.6e} (rel {float(erel):.2e}, larger: {'arb' if Eb > Ea else 'mp' if Ea > Eb else 'equal'}); "
              f"E/T <= {float(max(Ea,Eb)/min(Ta,Tb)):.2e}; ok mp={a['ok']} arb={b['ok']}; pieces {len(a['pieces'])}/{len(b['pieces'])} agree={pc} -> {st}")
    tm, ta = os.path.join(d, "batches", "mp-tail.json"), os.path.join(d, "batches", "arb-tail.json")
    if os.path.exists(tm) and os.path.exists(ta):
        A, B = json.load(open(tm)), json.load(open(ta)); n += 1
        line = []; okall = str(A["N1"]) == str(B["N1"]) and A["ok"] == B["ok"]
        for q in ("Q1", "Q2", "Q3", "Q4"):
            va, vb = fr(A[q]), fr(B[q]); c = close(va, vb, rtol, atol); okall &= c
            line.append(f"{q}: {float(va):.10g}/{float(vb):.10g} rel {float(abs(va-vb)/max(va,vb)):.1e}{'' if c else ' MISMATCH'}")
        va, vb = fr(A["E1"]), fr(B["E1"]); c = ub_ok(va, vb, etol); okall &= c
        line.append(f"E1: {float(va):.10g}/{float(vb):.10g} rel {float(abs(va-vb)/max(va,vb)):.1e} (upper bounds, larger: {'arb' if vb > va else 'mp' if va > vb else 'equal'}){'' if c else ' MISMATCH'}")
        dA, dB = A.get("direct", {}).get("contained"), B.get("direct", {}).get("contained")
        st = "OK" if okall else "DISAGREE"
        if st != "OK": bad += 1
        print(f"tail N1={A['N1']}/{B['N1']}: " + "; ".join(line) + f"; sum {A['sum_float']:.6f}/{B['sum_float']:.6f}; side {A['side']}/{B['side']}; direct-contained {dA}/{dB}; ok {A['ok']}/{B['ok']} -> {st}")
    print(f"compared {n} items; disagreements {bad}; max E rel diff {float(emax):.2e} (etol {float(etol):.0e}); " + ("CONSISTENT" if bad == 0 else "DISAGREEMENT -- stop the line"))
    sys.exit(0 if bad == 0 else 1)

if __name__ == "__main__":
    main()
