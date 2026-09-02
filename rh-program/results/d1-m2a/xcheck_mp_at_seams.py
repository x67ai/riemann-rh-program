#!/usr/bin/env python3
"""xcheck_mp_at_seams.py -- run the mpmath-ball leg (producer_mp.py, UNTRUSTED) for ONE prism at each seam of a
manifest produced by the OTHER leg (the Arb leg), for the SPEC P-11 cell-wise cross-check at every seam of that
chain.  Output: <out>/prism-NNNN.json, index NNNN = the position of the seam in the other leg's manifest, plus
xcheck-mp.log and a small index file.  Cross-check prisms only, NOT a chain.

usage: xcheck_mp_at_seams.py <manifest-of-other-leg.json> <out-dir> [--instance row2] [--only i,j,k]
(run from results/d1-m2a so that the moment files resolve)
"""
import argparse, json, os, sys, time, datetime
from fractions import Fraction
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); os.chdir(HERE)
import producer_mp as PM
from ft_mp import PREC_DEFAULT

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest"); ap.add_argument("out")
    ap.add_argument("--instance", default="row2"); ap.add_argument("--only", default="")
    a = ap.parse_args()
    man = json.load(open(a.manifest))
    seams = [Fraction(int(e["seam"]["n"]), int(e["seam"]["d"])) for e in man["prisms"]]
    only = set(int(s) for s in a.only.split(",") if s) if a.only else None
    os.makedirs(a.out, exist_ok=True)
    logf = open(os.path.join(a.out, "xcheck-mp.log"), "a")
    def log(m):
        line = f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {m}"; print(line); sys.stdout.flush(); logf.write(line + "\n"); logf.flush()
    inst = PM.INSTANCES[a.instance]
    log(f"xcheck_mp_at_seams: {len(seams)} seams from {a.manifest}; instance {a.instance}")
    P = PM.Producer(inst, a.out, 10 ** 24, 10 ** 12, Fraction(1, 50), 12, Fraction(1, 2), PREC_DEFAULT, log)
    idx = []
    t0 = time.time()
    for j, s in enumerate(seams):
        if only is not None and j not in only:
            continue
        if os.path.exists(os.path.join(a.out, "prism-%04d.json" % j)):
            log(f"seam {j} = {s}: already present, skipping"); continue
        rec = P.produce_prism(j, s, inst["t0"])
        idx.append({"index": j, "seam": str(s), "file": rec["file"], "next": str(rec["next"]), "rows": rec["rows"], "seconds": rec["seconds"]})
        with open(os.path.join(a.out, "xcheck-index.json"), "w") as fh:
            json.dump(idx, fh, indent=1)
    log(f"done in {time.time() - t0:.0f}s")

if __name__ == "__main__":
    main()
