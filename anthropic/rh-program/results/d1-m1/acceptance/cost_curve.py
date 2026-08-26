"""Assemble results/d1-m1/cost-curve.json — M3 search-economics calibration.

Acceptance test (iii) of the D1 first deliverable: certification cost vs
height T and depth delta0 = sigma1 - 1/2 for the null-test exclusion boxes
(plus the DH live-fire points, labeled separately — refutation targets, not
null tests). Data sources, all on disk and rerunnable:

* mp-leg wall seconds + eval counts: the transcript's own producer metadata
  (producer_mp.py writes wall_seconds, segment_evals, endpoint_evals);
* arb-leg wall seconds: parsed from the `time` line of the run log
  (producer_arb.py does not record wall time in the transcript);
* segments: len(transcript["segments"]) — the mesh size the checker pays for.

Wall times are single-run measurements on this machine (Apple Silicon arm64,
system Python 3.9.6, mpmath 1.3.0, python-flint 0.6.0), not statistics.
"""
import datetime
import json
import os
import platform
import re
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "cost-curve.json")

# (transcript, log, leg, kind)
RUNS = [
    ("w1-mp-null-t100.json", "mp-null-t100.log", "mpmath-ball", "null"),
    ("w1-mp-null-t1000.json", "mp-null-t1000.log", "mpmath-ball", "null"),
    ("w1-mp-null-t10000.json", "mp-null-t10000.log", "mpmath-ball", "null"),
    ("w1-mp-null-deep-t100.json", "mp-null-deep-t100.log", "mpmath-ball",
     "null"),
    ("w1-arb-null-t100.json", "arb-null-t100.log", "arb", "null"),
    ("w1-arb-null-t1000.json", "arb-null-t1000.log", "arb", "null"),
    ("w1-arb-null-t10000.json", "arb-null-t10000.log", "arb", "null"),
    ("w1-arb-null-deep-t100.json", "arb-null-deep-t100.log", "arb", "null"),
    ("w1-mp-dh-livefire.json", "mp-dh-livefire.log", "mpmath-ball",
     "dh-livefire"),
    ("w1-arb-dh-livefire.json", "arb-dh-livefire.log", "arb", "dh-livefire"),
]


def fr(obj):
    return Fraction(int(obj["n"]), int(obj["d"]))


def log_wall_seconds(path):
    """Parse zsh `time` output: '... cpu 2.608 total'."""
    with open(path) as fh:
        text = fh.read()
    m = re.findall(r"cpu ([0-9.]+) total", text)
    return float(m[-1]) if m else None


def main():
    points = []
    for tname, lname, leg, kind in RUNS:
        tpath = os.path.join(HERE, tname)
        lpath = os.path.join(HERE, "logs", lname)
        if not os.path.exists(tpath):
            print("MISSING transcript %s — cost point skipped" % tname)
            continue
        with open(tpath) as fh:
            doc = json.load(fh)
        s1, s2 = fr(doc["rect"]["sigma1"]), fr(doc["rect"]["sigma2"])
        t1, t2 = fr(doc["rect"]["T1"]), fr(doc["rect"]["T2"])
        prod = doc.get("producer", {})
        wall = prod.get("wall_seconds")
        if wall is None and os.path.exists(lpath):
            wall = log_wall_seconds(lpath)
        S_lo = sum(int(r["argLo"]) for r in doc["segments"])
        S_hi = sum(int(r["argHi"]) for r in doc["segments"])
        A = int(doc["scales"]["A"])
        pt = {
            "transcript": "acceptance/" + tname,
            "leg": leg,
            "kind": kind,
            "function": doc["function"],
            "mode": doc["mode"],
            "rect": "[%s, %s] x [%s, %s]" % (s1, s2, t1, t2),
            "height_T": float(t1),
            "depth_delta0": float(s1 - Fraction(1, 2)),
            "box_sigma_width": float(s2 - s1),
            "box_T_height": float(t2 - t1),
            "segments": len(doc["segments"]),
            "wall_seconds": wall,
            "winding_width_turns": float(Fraction(S_hi - S_lo, A)),
            "claimed_m": int(doc["claimed_m"]),
            "K": doc["scales"]["K"],
            "A": doc["scales"]["A"],
        }
        for k in ("segment_evals", "endpoint_evals"):
            if k in prod:
                pt[k] = prod[k]
        points.append(pt)

    out = {
        "role": "M1 v1 acceptance test (iii) — first M3 search-economics "
                "calibration points (cost vs height T and depth delta0)",
        "generated_utc": datetime.datetime.now(datetime.timezone.utc)
        .isoformat(),
        "machine": "%s %s, Python %s" % (platform.system(),
                                         platform.machine(),
                                         sys.version.split()[0]),
        "measurement": "single-run wall times (zsh time / producer "
                       "metadata); not statistics",
        "reading": [
            "arb leg: wall time grows ~linearly in segment count; segment "
            "count at fixed box is driven by |zeta| variation (height axis: "
            "27 -> 65 -> 983 segments for T = 100 -> 1000 -> 10000)",
            "mp leg: wall time dominated by Euler-Maclaurin term count "
            "N ~ T/2 per ball evaluation, on top of segment growth",
            "depth axis (T = 100): delta0 = 1/10 vs 1/40 cost nearly "
            "identical on both legs at this height — depth is not yet the "
            "binding cost driver at T ~ 100",
        ],
        "points": points,
    }
    with open(OUT, "w") as fh:
        json.dump(out, fh, indent=1)
        fh.write("\n")
    print("wrote %s with %d points" % (OUT, len(points)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
