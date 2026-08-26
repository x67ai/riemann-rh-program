"""POSITIVE CONTROL harness, mpmath-ball leg — WINDING-MACHINERY TEST ONLY.

Runs the mpmath-ball producer's mesh/argument machinery on a rectangle that
STRADDLES the critical line around the first zeta zero rho_1 ~ 1/2 + 14.1347i:

    R = [2/5, 3/5] x [14, 143/10]

The box DELIBERATELY violates the W1 precondition 1/2 < sigma1 (checker C2).
This is NOT an off-line-zero claim and NOT a W1 certificate: it validates that
the argument-principle machinery sees the known zero (m = 1), and that the
reference checker then REJECTS the transcript at exactly C2 — the format
refusing, by design, to bless a straddling box.

Reuses producer_mp.py's build_mesh/argument_rows verbatim (imported, not
copied); only the produce() assembly is replicated here minus the rectangle
precondition, so the machinery under test is byte-identical to the production
leg's. Output: w1-poscontrol-mp.json (comment field carries this label).
"""
import datetime
import json
import os
import sys
import time
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))  # results/d1-m1

import mpmath  # noqa: E402
from ball import set_prec  # noqa: E402
from producer_mp import (FUNCTIONS, TRUST_LABELS, argument_rows,  # noqa: E402
                         build_mesh)

K = 10 ** 30
A = 10 ** 12
PREC = 288
H0 = Fraction(1, 20)
MAXDEPTH = 14


def main():
    t0 = time.time()
    set_prec(PREC)
    rect = (Fraction(2, 5), Fraction(3, 5), Fraction(14), Fraction(143, 10))
    s1, s2, t1, t2 = rect
    assert not (Fraction(1, 2) < s1), \
        "positive control must straddle the line (sigma1 <= 1/2)"
    fball = FUNCTIONS["zeta"]
    stats = {"evals": 0, "point_evals": 0}
    print("pos-control (mp leg): rect=[%s, %s]x[%s, %s] STRADDLES the line"
          % (s1, s2, t1, t2))
    segments, mesh = build_mesh(fball, rect, H0, K, MAXDEPTH, stats, print)
    arows = argument_rows(fball, segments, rect, A, stats, print)
    S_lo = sum(r[0] for r in arows)
    S_hi = sum(r[1] for r in arows)
    print("  winding sum: S_lo=%d S_hi=%d width=%d (A=%d)"
          % (S_lo, S_hi, S_hi - S_lo, A))
    assert 2 * (S_hi - S_lo) < A, "C8-style width bound failed"
    m_min = -((-S_lo) // A)
    m_max = S_hi // A
    assert m_min == m_max, "no unique integer winding"
    m = m_min
    print("  MACHINERY RESULT: winding m = %d (expected 1: the argument "
          "principle sees rho_1)" % m)
    if m != 1:
        print("POSITIVE CONTROL FAILED: m != 1")
        return 1

    def rat(fr):
        return {"n": str(fr.numerator), "d": str(fr.denominator)}

    doc = {
        "format": "W1-rect-transcript",
        "version": "1.0",
        "mode": "refutation",
        "function": "zeta",
        "trust_label": TRUST_LABELS["zeta"],
        "rect": {"sigma1": rat(s1), "sigma2": rat(s2),
                 "T1": rat(t1), "T2": rat(t2)},
        "scales": {"K": str(K), "A": str(A)},
        "claimed_m": str(m),
        "mesh": {e: [rat(v) for v in mesh[e]]
                 for e in ("bottom", "right", "top", "left")},
        "segments": [
            {"reLo": str(sg.vrow[0]), "reHi": str(sg.vrow[1]),
             "imLo": str(sg.vrow[2]), "imHi": str(sg.vrow[3]),
             "argLo": str(ar[0]), "argHi": str(ar[1])}
            for sg, ar in zip(segments, arows)
        ],
        "producer": {
            "implementation": "pos_control_mp.py harness over producer_mp.py "
                              "machinery (mpmath-ball leg)",
            "mpmath_version": mpmath.__version__,
            "python_version": sys.version.split()[0],
            "iv_prec_bits": PREC,
            "segment_evals": stats["evals"],
            "endpoint_evals": stats["point_evals"],
            "wall_seconds": round(time.time() - t0, 1),
            "timestamp_utc": datetime.datetime.now(datetime.timezone.utc)
            .isoformat(),
        },
        "comment": "POSITIVE CONTROL — WINDING-MACHINERY TEST ONLY. The box "
                   "straddles the critical line (sigma1 = 2/5 <= 1/2) around "
                   "rho_1 ~ 1/2 + 14.1347i, DELIBERATELY violating the W1 "
                   "precondition. NOT an off-line-zero claim, NOT a W1 "
                   "certificate. The reference checker MUST reject this file "
                   "at exactly C2; the machinery pass criterion is m = 1, "
                   "asserted by the harness before writing.",
    }
    out = os.path.join(HERE, "w1-poscontrol-mp.json")
    with open(out, "w") as fh:
        json.dump(doc, fh, indent=1)
        fh.write("\n")
    print("  wrote %s (%d segments, %.1fs total)"
          % (out, len(segments), time.time() - t0))
    return 0


if __name__ == "__main__":
    sys.exit(main())
