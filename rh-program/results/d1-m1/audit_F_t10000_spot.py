"""audit_F_t10000_spot.py -- AUDIT F: spot-check the value boxes of BOTH legs' t = 10^4 null
transcripts (the largest height in the suite) at fresh random interior points of randomly
chosen segments, against mpmath zeta at dps 40 (heuristic reference; a violation is
stop-the-line).  Own seed; 25 segments x 3 points per transcript."""
import json, random, sys
from fractions import Fraction
from mpmath import mp, mpc, mpf, zeta
mp.dps = 40
rng = random.Random(9973)
def fr(o): return Fraction(int(o["n"]), int(o["d"]))
bad = 0
for path in ("acceptance/w1-mp-null-t10000.json", "acceptance/w1-arb-null-t10000.json"):
    d = json.load(open(path)); K = int(d["scales"]["K"])
    s1, s2, t1, t2 = (fr(d["rect"][k]) for k in ("sigma1", "sigma2", "T1", "T2"))
    segs = []
    for edge in ("bottom", "right", "top", "left"):
        bps = [fr(x) for x in d["mesh"][edge]]
        for i in range(len(bps) - 1):
            segs.append((edge, bps[i], bps[i + 1]))
    assert len(segs) == len(d["segments"])
    idx = rng.sample(range(len(segs)), 25)
    n = 0
    for k in idx:
        edge, a, b = segs[k]; row = d["segments"][k]
        for _ in range(3):
            u = Fraction(rng.randint(0, 10**6), 10**6)
            x = a + (b - a) * u
            if edge in ("bottom", "top"):
                s = mpc(mpf(x.numerator) / x.denominator, mpf((t1 if edge == "bottom" else t2).numerator) / (t1 if edge == "bottom" else t2).denominator)
            else:
                sig = s2 if edge == "right" else s1
                s = mpc(mpf(sig.numerator) / sig.denominator, mpf(x.numerator) / x.denominator)
            v = zeta(s); n += 1
            ok = (int(row["reLo"]) - mpf("1e-25") <= K * v.real <= int(row["reHi"]) + mpf("1e-25")
                  and int(row["imLo"]) - mpf("1e-25") <= K * v.imag <= int(row["imHi"]) + mpf("1e-25"))
            if not ok:
                bad += 1; print("  VIOLATION %s seg %d (%s) at s=%s: zeta=%s row=%s" % (path, k, edge, s, v, row))
    print("  %s: %d sampled points in 25 random segments, %d violations" % (path, n, bad))
print("TOTAL violations: %d" % bad)
sys.exit(1 if bad else 0)
