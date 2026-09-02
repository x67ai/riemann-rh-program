"""row2_summary.py -- per-prism table and totals for a producer_mp.py barrier transcript directory
(reads progress.json and the prism files; prints Markdown).  Untrusted reporting code; U.S. English.

usage: python3 row2_summary.py transcripts/row2
"""
import json
import os
import sys
from fractions import Fraction


def main(d):
    with open(os.path.join(d, "progress.json")) as fh:
        prog = json.load(fh)
    with open(os.path.join(d, "manifest.json")) as fh:
        man = json.load(fh)
    rows = prog["prisms"]
    print("| prism | seam τ | Δt | rows | floor Fn/K | E/K | D/K | DT = sup\\|∂_t f\\| | (E+D)/floor | s |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    tot_rows = tot_s = 0
    max_gate = 0
    for p in rows:
        with open(os.path.join(d, p["file"])) as fh:
            doc = json.load(fh)
        K = int(doc["scales"]["K"])
        Fn, Fd = int(doc["modulus_floor"]["Fn"]), int(doc["modulus_floor"]["Fd"])
        E, D = int(doc["approx_defect"]), int(doc["displacement"])
        gate = Fraction((E + D) * Fd, Fn * K)
        max_gate = max(max_gate, gate)
        tot_rows += p["rows"]
        tot_s += p["seconds"]
        print("| %d | %s | %.3e | %d | %.4f | %.3e | %.4f | %.4g | %.3f | %.0f |" % (
            p["index"], p["seam"], p["delta_t"], p["rows"], p["floor"], p["E"], p["D"], p["DT"], float(gate), p["seconds"]))
    last = rows[-1]
    print()
    print("prisms: %d; total rows: %d; wall: %.0f s (%.1f min); mean %.1f s/prism; chain reaches t = %s; complete: %s; "
          "max (E+D)/floor over prisms: %.3f (gate C-B12 needs < 1)" % (
              len(rows), tot_rows, tot_s, tot_s / 60, tot_s / len(rows), last["next"], prog["complete"], float(max_gate)))
    print("manifest t0 = %s/%s; producer status: %s" % (man["t0"]["n"], man["t0"]["d"], man["producer"]["status"][:60]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
