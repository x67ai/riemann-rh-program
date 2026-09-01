"""audit_F_claims.py -- AUDIT F: check every numerical claim of acceptance-report.md
sections 1-5 and of cost-curve.json against the artifacts on disk (the transcripts, their
producer metadata, and the logs).  Prints a claim-by-claim ledger; any mismatch is listed.
"""
import json
import math
import os
import re
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
ACC = os.path.join(HERE, "acceptance")

# acceptance-report.md section 1 + 3 tables: (file, segments, wall s, S_lo, S_hi, scale exponent, floor)
REPORT = {
    "w1-mp-null-t100.json": (52, 1.0, -24, 28, 12, 0.35555),
    "w1-arb-null-t100.json": (27, 0.09, -14, 13, 6, 0.08328),
    "w1-mp-null-t1000.json": (81, 8.6, -41, 40, 12, 0.015573),
    "w1-arb-null-t1000.json": (65, 0.14, -29, 36, 6, 0.013827),
    "w1-mp-null-t10000.json": (1294, 1564.7, -679, 637, 12, 8.13e-5),
    "w1-arb-null-t10000.json": (983, 2.6, -495, 488, 6, 7.64e-6),
    "w1-mp-null-deep-t100.json": (58, 1.1, -28, 30, 12, 0.35550),
    "w1-arb-null-deep-t100.json": (30, 0.09, -16, 14, 6, 0.03052),
    "w1-mp-dh-livefire.json": (40, 3.5, 999999999980, 1000000000020, 12, 2.467e-4),
    "w1-arb-dh-livefire.json": (50, 0.19, 999973, 1000023, 6, 3.019e-4),
}
POSCTRL = {"w1-poscontrol-mp.json": (77, 999999999962, 1000000000039, 12),
           "w1-poscontrol-arb.json": (183, 999911, 1000094, 6)}
CROSSCHECK_PAIRS = {"t100": 83, "t1000": 158, "t10000": 2547, "deep-t100": 90, "dh-livefire": 122, "poscontrol": 295}


def fr(o):
    return Fraction(int(o["n"]), int(o["d"]))


def main():
    mism = []
    print("AUDIT F: acceptance-report.md / cost-curve.json numerical claims vs artifacts")
    for fname, (segs, wall, slo, shi, aexp, floor) in REPORT.items():
        with open(os.path.join(ACC, fname)) as fh:
            d = json.load(fh)
        n = len(d["segments"])
        S_lo = sum(int(r["argLo"]) for r in d["segments"])
        S_hi = sum(int(r["argHi"]) for r in d["segments"])
        A = int(d["scales"]["A"])
        prod = d["producer"]
        wall_meta = prod.get("wall_seconds")
        fl = d.get("modulus_floor")
        flv = float(Fraction(int(fl["Fn"]), int(fl["Fd"]))) if fl else None
        ok = (n == segs and S_lo == slo and S_hi == shi and A == 10 ** aexp
              and (flv is not None and abs(flv - floor) / floor < 2e-3))
        mode_ok = (d["mode"] == ("refutation" if "dh" in fname else "exclusion"))
        m_ok = int(d["claimed_m"]) == (1 if "dh" in fname else 0)
        # wall time: mp leg records wall_seconds in metadata; arb leg does not (from logs)
        wall_src = "meta %.1f" % wall_meta if wall_meta is not None else "log"
        if wall_meta is None:
            logname = fname.replace("w1-", "").replace(".json", ".log")
            try:
                with open(os.path.join(ACC, "logs", logname)) as fh:
                    txt = fh.read()
                mt = re.search(r"real\s+(\d+)m([\d.]+)s|wall[^0-9]*([\d.]+)", txt)
                wall_src = "log: " + (mt.group(0) if mt else "no wall figure in log")
            except FileNotFoundError:
                wall_src = "no log"
        line = ("  %-28s segs %4d/%4d  S=[%d,%d]/%d vs report [%d,%d]e-%d  floor %.5g vs %.5g  mode/m %s/%s  wall %s"
                % (fname, n, segs, S_lo, S_hi, A, slo, shi, aexp, flv, floor, mode_ok, m_ok, wall_src))
        print(line + ("" if ok and mode_ok and m_ok else "   **MISMATCH**"))
        if not (ok and mode_ok and m_ok):
            mism.append(fname)
    for fname, (segs, slo, shi, aexp) in POSCTRL.items():
        with open(os.path.join(ACC, fname)) as fh:
            d = json.load(fh)
        n = len(d["segments"])
        S_lo = sum(int(r["argLo"]) for r in d["segments"])
        S_hi = sum(int(r["argHi"]) for r in d["segments"])
        A = int(d["scales"]["A"])
        s1 = fr(d["rect"]["sigma1"])
        ok = n == segs and S_lo == slo and S_hi == shi and A == 10 ** aexp and s1 <= Fraction(1, 2)
        print("  %-28s segs %4d/%4d  S=[%d,%d]/%d vs [%d,%d]e-%d  sigma1=%s (<=1/2: %s)%s"
              % (fname, n, segs, S_lo, S_hi, A, slo, shi, aexp, s1, s1 <= Fraction(1, 2), "" if ok else "  **MISMATCH**"))
        if not ok:
            mism.append(fname)
    # cost-curve.json vs transcripts
    with open(os.path.join(HERE, "cost-curve.json")) as fh:
        cc = json.load(fh)
    print("  cost-curve.json: %d points" % len(cc["points"]))
    for p in cc["points"]:
        with open(os.path.join(HERE, p["transcript"])) as fh:
            d = json.load(fh)
        n = len(d["segments"])
        S_lo = sum(int(r["argLo"]) for r in d["segments"])
        S_hi = sum(int(r["argHi"]) for r in d["segments"])
        A = int(d["scales"]["A"])
        width = (S_hi - S_lo) / A
        rect = "[%s, %s] x [%s, %s]" % tuple(fr(d["rect"][k]) for k in ("sigma1", "sigma2", "T1", "T2"))
        checks = [n == p["segments"], abs(width - p["winding_width_turns"]) <= 1e-3 * max(width, 1e-30),
                  int(d["claimed_m"]) == p["claimed_m"], d["scales"]["K"] == p["K"], d["scales"]["A"] == p["A"],
                  rect.replace(" ", "") == p["rect"].replace(" ", ""),
                  abs(float(fr(d["rect"]["sigma1"]) - Fraction(1, 2)) - p["depth_delta0"]) < 1e-12]
        if "wall_seconds" in d["producer"]:
            checks.append(abs(d["producer"]["wall_seconds"] - p["wall_seconds"]) < 0.05 + 1e-3 * p["wall_seconds"])
            checks.append(d["producer"].get("segment_evals") == p.get("segment_evals"))
            checks.append(d["producer"].get("endpoint_evals") == p.get("endpoint_evals"))
        ok = all(checks)
        print("    %-36s segs %4d width %.3e m=%s wall %s  -> %s" % (p["transcript"], n, width, d["claimed_m"], p["wall_seconds"], "ok" if ok else "**MISMATCH** %s" % checks))
        if not ok:
            mism.append(p["transcript"])
    # crosscheck pair counts from the log
    with open(os.path.join(ACC, "logs", "crosscheck.log")) as fh:
        txt = fh.read()
    with open(os.path.join(ACC, "logs", "crosscheck-t10000.log")) as fh:
        txt += fh.read()
    for key, pairs in CROSSCHECK_PAIRS.items():
        found = ("overlap pairs checked: %d" % pairs) in txt
        print("  crosscheck.log claims %-12s %4d overlap pairs: %s" % (key, pairs, "present" if found else "**NOT FOUND**"))
        if not found:
            mism.append("crosscheck " + key)
    print("MISMATCHES: %d %s" % (len(mism), mism))
    return 1 if mism else 0


if __name__ == "__main__":
    sys.exit(main())
