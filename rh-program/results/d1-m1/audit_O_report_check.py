"""audit_O_report_check.py -- AUDITOR O: every numerical claim in acceptance-report.md
and cost-curve.json recomputed from the artifacts on disk (task item 6).
"""
import json, os, sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
ACC = os.path.join(HERE, "acceptance")

FILES = ["w1-mp-null-t100", "w1-arb-null-t100", "w1-mp-null-t1000", "w1-arb-null-t1000",
         "w1-mp-null-t10000", "w1-arb-null-t10000", "w1-mp-null-deep-t100",
         "w1-arb-null-deep-t100", "w1-mp-dh-livefire", "w1-arb-dh-livefire",
         "w1-poscontrol-mp", "w1-poscontrol-arb"]

# (file, segments, S_lo, S_hi in units of A/1e12 or A/1e6, floor) as PRINTED in the report
REPORT_NULL = {
    # name: (segments, S_lo_units, S_hi_units, floor_string)
    "w1-mp-null-t100":      (52,  -24,  28,  "0.35555"),
    "w1-arb-null-t100":     (27,  -14,  13,  "0.08328"),
    "w1-mp-null-t1000":     (81,  -41,  40,  "0.015573"),
    "w1-arb-null-t1000":    (65,  -29,  36,  "0.013827"),
    "w1-mp-null-t10000":    (1294, -679, 637, "8.13e-05"),
    "w1-arb-null-t10000":   (983, -495, 488, "7.64e-06"),
    "w1-mp-null-deep-t100": (58,  -28,  30,  "0.35550"),
    "w1-arb-null-deep-t100":(30,  -16,  14,  "0.03052"),
}
REPORT_DH = {
    "w1-mp-dh-livefire":  (40, 999999999980, 1000000000020, 1, "2.467e-04"),
    "w1-arb-dh-livefire": (50, 999973, 1000023, 1, "3.019e-04"),
}
REPORT_POS = {
    "w1-poscontrol-mp":  (77, 999999999962, 1000000000039),
    "w1-poscontrol-arb": (183, 999911, 1000094),
}
REPORT_WALL = {  # report sec.1/3 "wall s" column
    "w1-mp-null-t100": 1.0, "w1-arb-null-t100": 0.09,
    "w1-mp-null-t1000": 8.6, "w1-arb-null-t1000": 0.14,
    "w1-mp-null-t10000": 1564.7, "w1-arb-null-t10000": 2.6,
    "w1-mp-null-deep-t100": 1.1, "w1-arb-null-deep-t100": 0.09,
    "w1-mp-dh-livefire": 3.5, "w1-arb-dh-livefire": 0.19,
}


def load(name):
    with open(os.path.join(ACC, name + ".json")) as fh:
        return json.load(fh)


def sums(doc):
    return (sum(int(r["argLo"]) for r in doc["segments"]),
            sum(int(r["argHi"]) for r in doc["segments"]))


def main():
    lines = []

    def out(s):
        print(s); sys.stdout.flush(); lines.append(s)

    bad = 0
    out("AUDIT O -- acceptance-report.md / cost-curve.json numbers vs artifacts")
    out("")
    out("%-24s %6s %6s  %-30s %-12s %s" % ("file", "rows", "rpt", "winding sum (S_lo, S_hi)", "floor", "verdict"))
    for name in FILES:
        doc = load(name)
        S_lo, S_hi = sums(doc)
        n = len(doc["segments"])
        A = int(doc["scales"]["A"])
        K = int(doc["scales"]["K"])
        fl = doc.get("modulus_floor")
        floor = (Fraction(int(fl["Fn"]), int(fl["Fd"])) if fl else None)
        notes = []
        if name in REPORT_NULL:
            rn, rlo, rhi, rfloor = REPORT_NULL[name]
            if n != rn:
                notes.append("SEGMENTS %d != report %d" % (n, rn)); bad += 1
            if (S_lo, S_hi) != (rlo, rhi):
                notes.append("WINDING (%d,%d) != report (%d,%d)" % (S_lo, S_hi, rlo, rhi)); bad += 1
            got = float(floor) if floor is not None else None
            want = float(rfloor)
            # report prints a truncated/rounded floor; require agreement to its printed precision
            if got is None or abs(got - want) > abs(want) * 2e-4:
                notes.append("FLOOR %.6g vs report %s" % (got if got else -1, rfloor)); bad += 1
        if name in REPORT_DH:
            rn, rlo, rhi, rm, rfloor = REPORT_DH[name]
            if n != rn:
                notes.append("SEGMENTS %d != report %d" % (n, rn)); bad += 1
            if (S_lo, S_hi) != (rlo, rhi):
                notes.append("WINDING (%d,%d) != report (%d,%d)" % (S_lo, S_hi, rlo, rhi)); bad += 1
            if int(doc["claimed_m"]) != rm:
                notes.append("m mismatch"); bad += 1
            got, want = float(floor), float(rfloor)
            if abs(got - want) > abs(want) * 2e-3:
                notes.append("FLOOR %.6g vs report %s" % (got, rfloor)); bad += 1
        if name in REPORT_POS:
            rn, rlo, rhi = REPORT_POS[name]
            if n != rn:
                notes.append("SEGMENTS %d != report %d" % (n, rn)); bad += 1
            if (S_lo, S_hi) != (rlo, rhi):
                notes.append("WINDING (%d,%d) != report (%d,%d)" % (S_lo, S_hi, rlo, rhi)); bad += 1
        # wall time from the producer metadata
        w = doc.get("producer", {}).get("wall_seconds")
        if name in REPORT_WALL and w is not None:
            rw = REPORT_WALL[name]
            if abs(w - rw) > max(0.05, 0.02 * rw):
                notes.append("WALL %.1f != report %.1f" % (w, rw)); bad += 1
        rpt = (REPORT_NULL.get(name) or REPORT_DH.get(name) or REPORT_POS.get(name) or (None,))[0]
        out("%-24s %6d %6s  [%d, %d] A=1e%d  %-12s %s"
            % (name, n, rpt, S_lo, S_hi, len(str(A)) - 1,
               ("%.6g" % float(floor)) if floor else "none",
               "OK" if not notes else " | ".join(notes)))
        # invariants
        if not 2 * (S_hi - S_lo) < A:
            out("   !! C8 fails"); bad += 1
        if not S_lo <= A * int(doc["claimed_m"]) <= S_hi:
            out("   !! C9 fails"); bad += 1
        if K != 10 ** 30 and "arb" not in name:
            out("   note: K = %d" % K)

    # ---- cost curve
    out("")
    out("cost-curve.json cross-check:")
    with open(os.path.join(HERE, "cost-curve.json")) as fh:
        cc = json.load(fh)

    def walk(o, path=""):
        if isinstance(o, dict):
            for k, v in o.items():
                yield from walk(v, path + "/" + str(k))
        elif isinstance(o, list):
            for i, v in enumerate(o):
                yield from walk(v, path + "[%d]" % i)
        else:
            yield path, o

    pts = cc.get("points") or cc.get("data") or None
    out("  top-level keys: %s" % ", ".join(cc.keys()))
    for p, v in walk(cc):
        if any(t in p.lower() for t in ("segment", "wall", "m", "sigma", "T")):
            pass
    # explicit comparison of every entry that names a transcript
    def find_entries(o, acc):
        if isinstance(o, dict):
            if "transcript" in o or "file" in o:
                acc.append(o)
            for v in o.values():
                find_entries(v, acc)
        elif isinstance(o, list):
            for v in o:
                find_entries(v, acc)
    ent = []
    find_entries(cc, ent)
    out("  entries naming a transcript: %d" % len(ent))
    for e in ent:
        fn = e.get("transcript") or e.get("file")
        base = os.path.splitext(os.path.basename(str(fn)))[0]
        try:
            doc = load(base)
        except Exception:
            out("  %-30s (no such transcript on disk)" % fn); bad += 1; continue
        n = len(doc["segments"])
        w = doc.get("producer", {}).get("wall_seconds")
        problems = []
        for key in ("segments", "n_segments", "segment_count"):
            if key in e and e[key] != n:
                problems.append("%s %s != %d" % (key, e[key], n)); bad += 1
        for key in ("wall_seconds", "wall_s", "seconds"):
            if key in e and w is not None and abs(float(e[key]) - w) > max(0.05, 0.02 * w):
                problems.append("%s %s != %s" % (key, e[key], w)); bad += 1
        out("  %-28s segments=%d wall=%s %s" % (base, n, w, " | ".join(problems) if problems else "OK"))
    out("")
    out("TOTAL mismatches: %d" % bad)
    with open(os.path.join(HERE, "audit_O_report_check.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    return bad


if __name__ == "__main__":
    sys.exit(0 if main() == 0 else 1)
