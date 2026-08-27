"""Two-producer cross-check (D-R3 / m2a-m2b-design sec. 4 stop-the-line rule).

Compares a PAIR of W1 transcripts for the SAME rectangle/function/mode, one
from each independent producer leg (mpmath-ball, Arb/python-flint), for
consistency. Soundness of each individual check used here:

* SAME-TARGET GUARD: rect, function, mode, claimed_m must agree exactly
  (rationals compared exactly via Fraction; claimed_m as integers).

* CELL-WISE VALUE-BOX CONSISTENCY (the "nonempty intersection cell-wise"
  criterion, on the common mesh refinement): the two legs mesh each edge
  differently, so segments are compared on OVERLAPS. If segment g1 of leg 1
  and segment g2 of leg 2 lie on the same edge and their closed parameter
  intervals intersect (in the varying coordinate; a shared single point
  counts, since value boxes are for-all-s enclosures over CLOSED segments),
  then any s in the overlap has f(s) in BOTH boxes under both legs'
  H-ENCL(a); therefore the boxes must intersect in Re and in Im. Interval
  intersection at different scales K1, K2 is decided by integer
  cross-multiplication: [a1/K1, b1/K1] meets [a2/K2, b2/K2] iff
  a1*K2 <= b2*K1 and a2*K1 <= b1*K2 (K1, K2 > 0). A disjoint pair proves at
  least one leg's enclosure FALSE -> STOP-THE-LINE.

* WINDING CONSISTENCY: both legs' total winding enclosures
  [S_lo/A, S_hi/A] (turn units, possibly different A) enclose the same true
  winding integral, so they must intersect as exact rational intervals; the
  claimed m must agree; and each leg's A*m must lie inside its own [S_lo,
  S_hi] (re-verified here even though the checkers already did).

* FLOORS (reported, not intersected): each leg's modulus_floor Fn/Fd is a
  certified LOWER bound on min |f| over the boundary; two lower bounds need
  not intersect, so both are printed for the record only.

Exit 0 = consistent; exit 1 = any inconsistency (reported, never softened).
Untrusted diagnostic tooling: this script produces no numbers that enter any
transcript; it can only STOP the line, not bless it.
"""
import json
import sys
from fractions import Fraction


def fr(obj):
    return Fraction(int(obj["n"]), int(obj["d"]))


def load(path):
    with open(path) as fh:
        return json.load(fh)


def edge_segments(doc):
    """Per-edge list of (lo, hi, row) with lo <= hi the varying coordinate."""
    out = {}
    k = 0
    segs = doc["segments"]
    for edge in ("bottom", "right", "top", "left"):
        bps = [fr(x) for x in doc["mesh"][edge]]
        rows = []
        for i in range(len(bps) - 1):
            a, b = bps[i], bps[i + 1]
            lo, hi = (a, b) if a <= b else (b, a)
            rows.append((lo, hi, segs[k]))
            k += 1
        out[edge] = rows
    assert k == len(segs), "segment count mismatch with mesh"
    return out


def boxes_intersect(r1, K1, r2, K2):
    """[a1/K1,b1/K1] meets [a2/K2,b2/K2] in Re AND Im (cross-multiplied)."""
    def meet(a1, b1, a2, b2):
        return a1 * K2 <= b2 * K1 and a2 * K1 <= b1 * K2
    return (meet(int(r1["reLo"]), int(r1["reHi"]),
                 int(r2["reLo"]), int(r2["reHi"]))
            and meet(int(r1["imLo"]), int(r1["imHi"]),
                     int(r2["imLo"]), int(r2["imHi"])))


def crosscheck(path1, path2):
    d1, d2 = load(path1), load(path2)
    name = "%s  vs  %s" % (path1, path2)
    failures = []

    # same-target guard
    for fld in ("sigma1", "sigma2", "T1", "T2"):
        if fr(d1["rect"][fld]) != fr(d2["rect"][fld]):
            failures.append("rect field %s differs" % fld)
    for fld in ("function", "mode"):
        if d1[fld] != d2[fld]:
            failures.append("%s differs: %r vs %r" % (fld, d1[fld], d2[fld]))
    m1, m2 = int(d1["claimed_m"]), int(d2["claimed_m"])
    if m1 != m2:
        failures.append("claimed_m differs: %d vs %d -> STOP-THE-LINE"
                        % (m1, m2))
    if failures:
        return name, failures, {}

    K1, K2 = int(d1["scales"]["K"]), int(d2["scales"]["K"])
    A1, A2 = int(d1["scales"]["A"]), int(d2["scales"]["A"])

    # cell-wise value boxes on the common refinement
    e1, e2 = edge_segments(d1), edge_segments(d2)
    pairs = 0
    for edge in ("bottom", "right", "top", "left"):
        for lo1, hi1, r1 in e1[edge]:
            for lo2, hi2, r2 in e2[edge]:
                if lo1 <= hi2 and lo2 <= hi1:  # closed overlap (points count)
                    pairs += 1
                    if not boxes_intersect(r1, K1, r2, K2):
                        failures.append(
                            "DISJOINT value boxes on edge %s, overlap "
                            "[%s, %s]x[%s, %s] -> at least one leg's "
                            "H-ENCL(a) is FALSE -> STOP-THE-LINE"
                            % (edge, max(lo1, lo2), min(hi1, hi2), lo1, hi1))

    # winding enclosures (turn units, exact rationals)
    S1 = (sum(int(r["argLo"]) for r in d1["segments"]),
          sum(int(r["argHi"]) for r in d1["segments"]))
    S2 = (sum(int(r["argLo"]) for r in d2["segments"]),
          sum(int(r["argHi"]) for r in d2["segments"]))
    w1 = (Fraction(S1[0], A1), Fraction(S1[1], A1))
    w2 = (Fraction(S2[0], A2), Fraction(S2[1], A2))
    if not (w1[0] <= w2[1] and w2[0] <= w1[1]):
        failures.append("winding enclosures DISJOINT: [%s, %s] vs [%s, %s] "
                        "turns -> STOP-THE-LINE"
                        % (w1[0], w1[1], w2[0], w2[1]))
    for tag, (Slo, Shi), A, m in (("leg1", S1, A1, m1), ("leg2", S2, A2, m2)):
        if not (Slo <= A * m <= Shi):
            failures.append("%s: A*m outside its own winding sum" % tag)

    info = {
        "pairs_checked": pairs,
        "winding_leg1_turns": "[%s, %s]" % (w1[0], w1[1]),
        "winding_leg2_turns": "[%s, %s]" % (w2[0], w2[1]),
        "m": m1,
        "floor_leg1": ("%s/%s" % (d1["modulus_floor"]["Fn"],
                                  d1["modulus_floor"]["Fd"])
                       if "modulus_floor" in d1 else None),
        "floor_leg2": ("%s/%s" % (d2["modulus_floor"]["Fn"],
                                  d2["modulus_floor"]["Fd"])
                       if "modulus_floor" in d2 else None),
    }
    return name, failures, info


def main(argv):
    if len(argv) < 2 or len(argv) % 2 != 0:
        print("usage: crosscheck.py leg1a.json leg2a.json "
              "[leg1b.json leg2b.json ...]")
        return 2
    bad = 0
    for i in range(0, len(argv), 2):
        name, failures, info = crosscheck(argv[i], argv[i + 1])
        print("== %s" % name)
        if info:
            print("   overlap pairs checked: %d, all value boxes intersect"
                  % info["pairs_checked"] if not failures else
                  "   overlap pairs checked: %d" % info["pairs_checked"])
            print("   winding leg1 %s vs leg2 %s turns, m = %d"
                  % (info["winding_leg1_turns"], info["winding_leg2_turns"],
                     info["m"]))
            if info["floor_leg1"] and info["floor_leg2"]:
                f1 = Fraction(*(int(x) for x in
                                info["floor_leg1"].split("/")))
                f2 = Fraction(*(int(x) for x in
                                info["floor_leg2"].split("/")))
                print("   floors (independent lower bounds): leg1 %.6g, "
                      "leg2 %.6g" % (float(f1), float(f2)))
            else:
                print("   floors: absent on at least one leg (optional row)")
        if failures:
            bad += 1
            for f in failures:
                print("   FAIL: %s" % f)
            print("   VERDICT: INCONSISTENT — STOP-THE-LINE")
        else:
            print("   VERDICT: CONSISTENT")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
