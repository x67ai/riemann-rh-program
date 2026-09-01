"""audit_O_zeta_rows.py -- AUDITOR O: independent H-ENCL spot check of the ZETA
(null-test) transcripts, by the same from-scratch method as audit_O_dh_winding.py
but with f = mp.zeta.  Shares no code with either producer leg.
"""
import json, os, sys
from fractions import Fraction
from mpmath import mp

import audit_O_dh_winding as W          # reuse only the auditor's own helpers

HERE = os.path.dirname(os.path.abspath(__file__))
ACC = os.path.join(HERE, "acceptance")
mp.dps = 50


def main():
    lines = []

    def out(s):
        print(s); sys.stdout.flush(); lines.append(s)

    out("AUDIT O -- independent H-ENCL spot check of the zeta null transcripts")
    out("method: mp.zeta at dps 50 + dense principal-arg unwrapping; no producer code.")
    W.f_dh = mp.zeta                     # swap the target function
    bad = 0
    for fn in ("w1-mp-null-t100.json", "w1-arb-null-t100.json",
               "w1-mp-null-deep-t100.json", "w1-arb-null-deep-t100.json",
               "w1-arb-null-t1000.json"):
        bad += W.audit(os.path.join(ACC, fn), nsub=12, out=out)
    out("")
    out("TOTAL problems: %d" % bad)
    with open(os.path.join(HERE, "audit_O_zeta_rows.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    return bad


if __name__ == "__main__":
    sys.exit(0 if main() == 0 else 1)
