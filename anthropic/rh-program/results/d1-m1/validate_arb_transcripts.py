#!/usr/bin/env python3
"""validate_arb_transcripts.py -- independent cross-validation of Arb-leg transcripts.

ROLE.  Binding rule for this session: "Cross-validate every rigorous enclosure
against independent high-precision evaluation."  This script checks Arb-leg W1
transcripts against mpmath (independent library, independent algorithms: mpmath
zeta/hurwitz vs FLINT/Arb acb zeta) at high working precision.

WHAT THIS IS NOT.  This is NOT the second producer leg (the mpmath BALL
producer is a separate D-R3 work item with its own evaluation code and its own
rigorous error bounds).  mpmath here is used heuristically -- plain arbitrary-
precision floats, no proven error bounds -- so a pass is EVIDENCE against
producer bugs, not a certificate.  A FAILURE, however, is a stop-the-line event
(m2a-m2b-design.md section 4: producer disagreement beyond stated radii).

Checks per transcript:
  V1: for every segment, mpmath values of f at 5 points of the closed segment
      (t = 0, 1/4, 1/2, 3/4, 1) lie inside the integer value box at scale K
      (box widths are astronomically larger than mpmath's error at dps 40, so
      plain containment is decisive in practice);
  V2: the total winding computed by dense principal-argument unwrapping along
      the boundary (heuristic continuity argument) equals claimed_m and lies in
      [S_lo, S_hi]/A;
  V3: min sampled |f| on the boundary respects the claimed modulus floor
      Fn/Fd (samples can only be ABOVE a true floor).

Usage: python3 validate_arb_transcripts.py FILE.json [FILE2.json ...]
Exit 0 iff all checks pass on all files.
"""

import json
import sys
from fractions import Fraction

import mpmath

mpmath.mp.dps = 40

FAILURES = []


def check(name, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {name}" + (f" -- {detail}" if detail else ""))
    if not ok:
        FAILURES.append(name)


def frac(obj):
    return Fraction(int(obj["n"]), int(obj["d"]))


def mpf_of(q):
    return mpmath.mpf(q.numerator) / mpmath.mpf(q.denominator)


KAP = (mpmath.sqrt(10 - 2 * mpmath.sqrt(5)) - 2) / (mpmath.sqrt(5) - 1)


def f_dh(s):
    # verbatim formula, results/ccm-dh-test/dh.py lines 5-8 via FORMAT.md 9.2
    return mpmath.power(5, -s) * (mpmath.zeta(s, Fraction(1, 5))
                                  + KAP * mpmath.zeta(s, Fraction(2, 5))
                                  - KAP * mpmath.zeta(s, Fraction(3, 5))
                                  - mpmath.zeta(s, Fraction(4, 5)))


def evaluator(function):
    if function == "zeta":
        return lambda s: mpmath.zeta(s)
    if function == "f_DH":
        return f_dh
    raise ValueError(function)


def segment_list(doc):
    """Reconstruct segments in global traversal order as ((p, q)) point pairs."""
    mesh = doc["mesh"]
    s1, s2 = frac(doc["rect"]["sigma1"]), frac(doc["rect"]["sigma2"])
    T1, T2 = frac(doc["rect"]["T1"]), frac(doc["rect"]["T2"])
    segs = []
    b = [frac(x) for x in mesh["bottom"]]
    segs += [((b[i], T1), (b[i + 1], T1)) for i in range(len(b) - 1)]
    r = [frac(x) for x in mesh["right"]]
    segs += [((s2, r[i]), (s2, r[i + 1])) for i in range(len(r) - 1)]
    t = [frac(x) for x in mesh["top"]]
    segs += [((t[i], T2), (t[i + 1], T2)) for i in range(len(t) - 1)]
    l = [frac(x) for x in mesh["left"]]
    segs += [((s1, l[i]), (s1, l[i + 1])) for i in range(len(l) - 1)]
    return segs


def validate(path):
    print(f"== {path}")
    with open(path) as fh:
        doc = json.load(fh)
    f = evaluator(doc["function"])
    K = int(doc["scales"]["K"])
    A = int(doc["scales"]["A"])
    m_claimed = int(doc["claimed_m"])
    segs = segment_list(doc)
    rows = doc["segments"]
    assert len(segs) == len(rows), "segment count mismatch"

    # V1: value-box containment at sampled points
    bad = 0
    min_abs = mpmath.inf
    for (p, q), row in zip(segs, rows):
        reLo, reHi = int(row["reLo"]), int(row["reHi"])
        imLo, imHi = int(row["imLo"]), int(row["imHi"])
        for tnum in (0, 1, 2, 3, 4):
            tt = Fraction(tnum, 4)
            x = p[0] + (q[0] - p[0]) * tt
            y = p[1] + (q[1] - p[1]) * tt
            v = f(mpmath.mpc(mpf_of(x), mpf_of(y)))
            min_abs = min(min_abs, abs(v))
            if not (reLo <= K * v.real <= reHi and imLo <= K * v.imag <= imHi):
                bad += 1
    check("V1 sampled values inside integer boxes",
          bad == 0, f"{5 * len(segs)} samples, {bad} outside")

    # V2: winding by dense principal-argument unwrapping (heuristic)
    pts = []
    for (p, q) in segs:
        for tnum in range(8):  # 8 subsamples per segment, endpoints covered by next
            tt = Fraction(tnum, 8)
            pts.append((p[0] + (q[0] - p[0]) * tt, p[1] + (q[1] - p[1]) * tt))
    pts.append(pts[0])
    total = mpmath.mpf(0)
    prev = None
    for (x, y) in pts:
        a = mpmath.arg(f(mpmath.mpc(mpf_of(x), mpf_of(y))))
        if prev is not None:
            d = a - prev
            while d > mpmath.pi:
                d -= 2 * mpmath.pi
            while d < -mpmath.pi:
                d += 2 * mpmath.pi
            total += d
        prev = a
    winding = total / (2 * mpmath.pi)
    S_lo = sum(int(r["argLo"]) for r in rows)
    S_hi = sum(int(r["argHi"]) for r in rows)
    ok2 = (abs(winding - m_claimed) < mpmath.mpf("0.01")
           and mpmath.mpf(S_lo) / A - mpmath.mpf("0.01") <= winding
           <= mpmath.mpf(S_hi) / A + mpmath.mpf("0.01"))
    check("V2 unwrapped winding matches claimed_m and [S_lo, S_hi]/A",
          ok2, f"winding = {mpmath.nstr(winding, 10)}, m = {m_claimed}, "
               f"S/A = [{S_lo}/{A}, {S_hi}/{A}]")

    # V3: modulus floor respected by samples
    if "modulus_floor" in doc:
        Fn, Fd = int(doc["modulus_floor"]["Fn"]), int(doc["modulus_floor"]["Fd"])
        floor_val = mpmath.mpf(Fn) / Fd
        check("V3 sampled min |f| >= claimed floor Fn/Fd",
              min_abs >= floor_val,
              f"min sampled |f| = {mpmath.nstr(min_abs, 8)}, floor = {mpmath.nstr(floor_val, 8)}")


def main():
    files = sys.argv[1:]
    if not files:
        print(__doc__)
        sys.exit(2)
    for p in files:
        validate(p)
    print()
    if FAILURES:
        print(f"RESULT: FAIL ({len(FAILURES)} check(s)) -- STOP-THE-LINE: "
              "producer disagreement beyond stated radii")
        sys.exit(1)
    print("RESULT: ALL CROSS-VALIDATION CHECKS PASS "
          "(evidence, not certificate -- see module docstring)")


if __name__ == "__main__":
    main()
