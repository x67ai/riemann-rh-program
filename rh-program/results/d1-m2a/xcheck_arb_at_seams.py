#!/usr/bin/env python3
"""xcheck_arb_at_seams.py -- run the Arb/FLINT leg (producer_arb.py, UNTRUSTED) for ONE prism at each seam of a
manifest produced by the OTHER leg, so that the SPEC P-11 cell-wise cross-check can be made at every seam of that
leg's chain (the two legs' adaptive chains have different seams; only seam 0 is common).  Each seam gets its own
sub-directory <out>/seam-NNNN/ with the usual instance02-prism-0000.json (+ manifest, log).  The prisms produced
here are cross-check prisms, NOT part of any chain.

usage: xcheck_arb_at_seams.py <manifest-of-other-leg.json> <out-dir> [--instance row2] [--skip N]
"""
import argparse, json, os, sys, time, datetime
from fractions import Fraction
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import producer_arb as PA

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest"); ap.add_argument("out")
    ap.add_argument("--instance", default="row2"); ap.add_argument("--skip", type=int, default=0)
    ap.add_argument("--only", default="", help="comma-separated seam indices to run (default all)")
    a = ap.parse_args()
    man = json.load(open(a.manifest))
    seams = [Fraction(int(e["seam"]["n"]), int(e["seam"]["d"])) for e in man["prisms"]]
    only = set(int(s) for s in a.only.split(",") if s) if a.only else None
    os.makedirs(a.out, exist_ok=True)
    logf = open(os.path.join(a.out, "xcheck-arb.log"), "a")
    def log(m):
        line = f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {m}"; print(line); sys.stdout.flush(); logf.write(line + "\n"); logf.flush()
    log(f"xcheck_arb_at_seams: {len(seams)} seams from {a.manifest}; instance {a.instance}")
    t0 = time.time()
    for j, s in enumerate(seams):
        if j < a.skip or (only is not None and j not in only):
            continue
        d = os.path.join(a.out, f"seam-{j:04d}")
        if os.path.exists(os.path.join(d, "instance02-prism-0000.json")):
            log(f"seam {j} = {s}: already present, skipping"); continue
        log(f"seam {j} = {s} ({float(s):.9f})")
        PA.run_instance(d, 0, 1, False, 10 ** 12, 10 ** 6, Fraction(1, 6), 30, 36, 40, s, None, 16, instance=a.instance, log=log)
    log(f"done in {time.time() - t0:.0f}s")

if __name__ == "__main__":
    main()
