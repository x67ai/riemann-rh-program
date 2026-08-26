"""POSITIVE CONTROL harness, Arb leg — WINDING-MACHINERY TEST ONLY.

Same test as pos_control_mp.py on the independent Arb/python-flint leg:
R = [2/5, 3/5] x [14, 143/10] straddling the critical line around
rho_1 ~ 1/2 + 14.1347i. DELIBERATE C2 violation (sigma1 = 2/5 <= 1/2);
NOT an off-line-zero claim, NOT a W1 certificate. Machinery pass criterion:
winding m = 1. The reference checker MUST reject the emitted file at C2.

Reuses producer_arb.py's refine_edge/argument_row/EndpointCache verbatim
(imported); only the produce() assembly loop is replicated minus the
rectangle precondition. Output: w1-poscontrol-arb.json.
"""
import datetime
import json
import os
import sys
import time
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))  # results/d1-m1

import flint  # noqa: E402
from flint import ctx  # noqa: E402
from producer_arb import (EVALUATORS, TRUST_LABELS, EndpointCache,  # noqa: E402
                          argument_row, frac_json, refine_edge)

K = 10 ** 30
A = 10 ** 6
PREC = 300
MAX_DEPTH = 40


def main():
    t0 = time.time()
    sigma1, sigma2 = Fraction(2, 5), Fraction(3, 5)
    T1, T2 = Fraction(14), Fraction(143, 10)
    assert not (Fraction(1, 2) < sigma1), \
        "positive control must straddle the line (sigma1 <= 1/2)"
    f = EVALUATORS["zeta"]
    ctx.prec = PREC
    print("pos-control (arb leg): rect=[%s, %s]x[%s, %s] STRADDLES the line"
          % (sigma1, sigma2, T1, T2))

    edges = {
        "bottom": ("h", sigma1, sigma2, T1),
        "right": ("v", T1, T2, sigma2),
        "top": ("h", sigma2, sigma1, T2),
        "left": ("v", T2, T1, sigma1),
    }
    mesh = {}
    rows = []
    cache = EndpointCache(f, PREC)
    total_segs = 0
    for name in ("bottom", "right", "top", "left"):
        ctx.prec = PREC
        pieces = refine_edge(f, edges[name], K, MAX_DEPTH)
        total_segs += len(pieces)
        breakpoints = [pieces[0][0][1]] + [sg[2] for sg, _ in pieces]
        mesh[name] = breakpoints
        for sg, box in pieces:
            argLo, argHi = argument_row(cache, sg, box, A)
            rows.append(box + (argLo, argHi))

    S_lo = sum(r[4] for r in rows)
    S_hi = sum(r[5] for r in rows)
    print("  winding sum: S_lo=%d S_hi=%d width=%d (A=%d)"
          % (S_lo, S_hi, S_hi - S_lo, A))
    assert 2 * (S_hi - S_lo) < A, "C8-style width bound failed"
    m_lo = -((-S_lo) // A)
    m_hi = S_hi // A
    assert m_lo == m_hi, "no unique integer winding"
    m = m_lo
    print("  MACHINERY RESULT: winding m = %d (expected 1: the argument "
          "principle sees rho_1)" % m)
    if m != 1:
        print("POSITIVE CONTROL FAILED: m != 1")
        return 1

    doc = {
        "format": "W1-rect-transcript",
        "version": "1.0",
        "mode": "refutation",
        "function": "zeta",
        "trust_label": TRUST_LABELS["zeta"],
        "rect": {"sigma1": frac_json(sigma1), "sigma2": frac_json(sigma2),
                 "T1": frac_json(T1), "T2": frac_json(T2)},
        "scales": {"K": str(K), "A": str(A)},
        "claimed_m": str(m),
        "mesh": {name: [frac_json(q) for q in mesh[name]]
                 for name in ("bottom", "right", "top", "left")},
        "segments": [
            {"reLo": str(r[0]), "reHi": str(r[1]), "imLo": str(r[2]),
             "imHi": str(r[3]), "argLo": str(r[4]), "argHi": str(r[5])}
            for r in rows
        ],
        "producer": {
            "leg": "arb",
            "implementation": "pos_control_arb.py harness over "
                              "producer_arb.py machinery",
            "library": "python-flint %s" % flint.__version__,
            "python": sys.version.split()[0],
            "prec_bits_base": PREC,
            "segments": total_segs,
            "winding_sum": {"S_lo": str(S_lo), "S_hi": str(S_hi)},
            "wall_seconds": round(time.time() - t0, 2),
            "timestamp_utc": datetime.datetime.now(datetime.timezone.utc)
            .strftime("%Y-%m-%dT%H:%M:%SZ"),
        },
        "comment": "POSITIVE CONTROL — WINDING-MACHINERY TEST ONLY. The box "
                   "straddles the critical line (sigma1 = 2/5 <= 1/2) around "
                   "rho_1 ~ 1/2 + 14.1347i, DELIBERATELY violating the W1 "
                   "precondition. NOT an off-line-zero claim, NOT a W1 "
                   "certificate. The reference checker MUST reject this file "
                   "at exactly C2; the machinery pass criterion is m = 1, "
                   "asserted by the harness before writing.",
    }
    out = os.path.join(HERE, "w1-poscontrol-arb.json")
    with open(out, "w") as fh:
        json.dump(doc, fh, indent=1)
        fh.write("\n")
    print("  wrote %s (%d segments, %.2fs total)"
          % (out, total_segs, time.time() - t0))
    return 0


if __name__ == "__main__":
    sys.exit(main())
