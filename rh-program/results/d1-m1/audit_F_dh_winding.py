"""audit_F_dh_winding.py -- AUDIT F: recompute the DH live-fire winding enclosure FROM
SCRATCH (no producer code, no ball code), three independent ways, and compare with the
two acceptance transcripts acceptance/w1-{mp,arb}-dh-livefire.json.

Rectangle (both transcripts): R = [4/5, 41/50] x [8569/100, 8571/100].
f_DH(s) = 5^{-s} [zeta(s,1/5) + kap*zeta(s,2/5) - kap*zeta(s,3/5) - zeta(s,4/5)],
kap = (sqrt(10-2*sqrt5) - 2)/(sqrt5 - 1)   (the quoted dh.py definition; here typed
independently from the formula, evaluated with mpmath's own Hurwitz zeta at dps 50).

Way 1 -- direct contour integral of f'/f over the four edges (mp.quad, f' from the
         analytic Hurwitz-zeta derivative mp.zeta(s, a, 1)); the result /(2 pi i) must be
         an integer (1) to many digits.
Way 2 -- dense adaptive argument unwrapping along the boundary: sample so that
         successive |arg jumps| < pi/2 (refine otherwise); the accumulated argument
         change / 2 pi is the winding.
Way 3 -- per-segment check against each transcript: for every transcript segment, the
         SAME unwrapping gives the increment Delta_k; A*Delta_k/2pi must lie inside the
         transcript's [argLo, argHi] (a violation means the row's H-ENCL(b) is false);
         also the value boxes are checked at the segment endpoints and midpoint (H-ENCL(a)
         spot check), and the certified floor is compared with the sampled boundary
         minimum.
Heuristic-float evidence (not a certificate) -- but a disagreement is a stop-the-line
event per m2a-m2b-design sec. 4.
"""
import json
import sys
from fractions import Fraction

from mpmath import mp, mpf, mpc, pi, quad, sqrt, zeta, power, arg, floor, ceil

mp.dps = 50
KAP = (sqrt(10 - 2 * sqrt(5)) - 2) / (sqrt(5) - 1)
A15 = [mpf(j) / 5 for j in (1, 2, 3, 4)]
COEF = [1, KAP, -KAP, -1]


def fdh(s):
    return power(5, -s) * sum(c * zeta(s, a) for c, a in zip(COEF, A15))


def fdh_prime(s):
    # d/ds [5^{-s} g(s)] = -log5 * 5^{-s} g + 5^{-s} g'
    g = sum(c * zeta(s, a) for c, a in zip(COEF, A15))
    gp = sum(c * zeta(s, a, 1) for c, a in zip(COEF, A15))
    return power(5, -s) * (gp - mp.log(5) * g)


def corners(rect):
    s1, s2, t1, t2 = rect
    return [mpc(s1, t1), mpc(s2, t1), mpc(s2, t2), mpc(s1, t2)]


def way1_contour(rect):
    c = corners(rect)
    total = mpc(0)
    for k in range(4):
        z, w = c[k], c[(k + 1) % 4]
        total += quad(lambda t: fdh_prime(z + t * (w - z)) / fdh(z + t * (w - z)) * (w - z), [0, 1])
    return total / (2 * pi * 1j)


def unwrap_increment(z, w, max_jump=pi / 2, depth_cap=24):
    """Continuous argument increment of f_DH along the straight segment z -> w by adaptive
    sampling: recursively halve until the principal-arg jump is < max_jump."""
    def rec(a, b, fa, fb, depth):
        d = arg(fb / fa)          # principal value in (-pi, pi]
        if abs(d) < max_jump or depth >= depth_cap:
            if depth >= depth_cap:
                raise RuntimeError("unwrap: depth cap hit near %s" % a)
            return d
        m = (a + b) / 2
        fm = fdh(m)
        return rec(a, m, fa, fm, depth + 1) + rec(m, b, fm, fb, depth + 1)
    return rec(z, w, fdh(z), fdh(w), 0)


def way2_unwrap(rect):
    c = corners(rect)
    return sum(unwrap_increment(c[k], c[(k + 1) % 4]) for k in range(4)) / (2 * pi)


def fr(o):
    return Fraction(int(o["n"]), int(o["d"]))


def way3_transcript(path, rect):
    with open(path) as fh:
        doc = json.load(fh)
    K, A = int(doc["scales"]["K"]), int(doc["scales"]["A"])
    s1, s2, t1, t2 = rect
    segs = []
    for edge in ("bottom", "right", "top", "left"):
        bps = [fr(x) for x in doc["mesh"][edge]]
        for i in range(len(bps) - 1):
            a, b = bps[i], bps[i + 1]
            if edge == "bottom":
                segs.append((mpc(mpf(a.numerator) / a.denominator, t1), mpc(mpf(b.numerator) / b.denominator, t1)))
            elif edge == "right":
                segs.append((mpc(s2, mpf(a.numerator) / a.denominator), mpc(s2, mpf(b.numerator) / b.denominator)))
            elif edge == "top":
                segs.append((mpc(mpf(a.numerator) / a.denominator, t2), mpc(mpf(b.numerator) / b.denominator, t2)))
            else:
                segs.append((mpc(s1, mpf(a.numerator) / a.denominator), mpc(s1, mpf(b.numerator) / b.denominator)))
    assert len(segs) == len(doc["segments"])
    bad_arg = bad_box = 0
    total_turns = mpf(0)
    minmod = mpf("inf")
    margins = []
    for k, ((z, w), row) in enumerate(zip(segs, doc["segments"])):
        inc = unwrap_increment(z, w)
        total_turns += inc / (2 * pi)
        scaled = A * inc / (2 * pi)
        lo, hi = int(row["argLo"]), int(row["argHi"])
        if not (lo - mpf("1e-20") <= scaled <= hi + mpf("1e-20")):
            bad_arg += 1
            print("   ARG ROW VIOLATION seg %d: A*Delta/2pi = %s not in [%d, %d]" % (k, mp.nstr(scaled, 20), lo, hi))
        margins.append(min(scaled - lo, hi - scaled))
        for t in (0, mpf(1) / 3, mpf(1) / 2, mpf(2) / 3, 1):
            v = fdh(z + t * (w - z))
            minmod = min(minmod, abs(v))
            if not (int(row["reLo"]) - mpf("1e-20") <= K * v.real <= int(row["reHi"]) + mpf("1e-20")
                    and int(row["imLo"]) - mpf("1e-20") <= K * v.imag <= int(row["imHi"]) + mpf("1e-20")):
                bad_box += 1
                print("   VALUE BOX VIOLATION seg %d t=%s: f=%s" % (k, t, v))
    S_lo = sum(int(r["argLo"]) for r in doc["segments"])
    S_hi = sum(int(r["argHi"]) for r in doc["segments"])
    fl = doc.get("modulus_floor")
    floor_ok = None
    if fl:
        floor_ok = Fraction(int(fl["Fn"]), int(fl["Fd"])) <= Fraction(mp.nstr(minmod, 40))
    print("  %s: %d segments, unwrapped total = %s turns; transcript S/A = [%d, %d]/%d = [%s, %s]; m = %s"
          % (path, len(segs), mp.nstr(total_turns, 25), S_lo, S_hi, A, mp.nstr(mpf(S_lo) / A, 12), mp.nstr(mpf(S_hi) / A, 12), doc["claimed_m"]))
    print("     total in transcript enclosure: %s; arg-row violations: %d; value-box violations: %d (%d sample points)"
          % (S_lo <= A * total_turns <= S_hi, bad_arg, bad_box, 5 * len(segs)))
    print("     tightest arg-row margin (scale-A units): %s; sampled boundary min|f| = %s; certified floor %s/%s = %s -> floor respected: %s"
          % (mp.nstr(min(margins), 6), mp.nstr(minmod, 10), fl["Fn"] if fl else "-", fl["Fd"] if fl else "-",
             mp.nstr(mpf(int(fl["Fn"])) / int(fl["Fd"]), 10) if fl else "-", floor_ok))
    return bad_arg + bad_box


def main():
    rect = (mpf(4) / 5, mpf(41) / 50, mpf(8569) / 100, mpf(8571) / 100)
    print("AUDIT F: DH live-fire winding recomputed from scratch, R = [4/5, 41/50] x [85.69, 85.71], dps %d" % mp.dps)
    rho = mp.findroot(fdh, mpc("0.808517182456637", "85.699348485377592"))
    print("  refined zero rho_DH = %s, |f(rho)| = %s, inside R: %s"
          % (mp.nstr(rho, 30), mp.nstr(abs(fdh(rho)), 5), rect[0] < rho.real < rect[1] and rect[2] < rho.imag < rect[3]))
    w1 = way1_contour(rect)
    print("  Way 1 (contour integral of f'/f / 2 pi i): %s" % mp.nstr(w1, 30))
    w2 = way2_unwrap(rect)
    print("  Way 2 (adaptive argument unwrapping):      %s turns" % mp.nstr(w2, 30))
    bad = 0
    for path in ("acceptance/w1-mp-dh-livefire.json", "acceptance/w1-arb-dh-livefire.json"):
        bad += way3_transcript(path, rect)
    print("VERDICT: %s" % ("all consistent, winding = 1" if bad == 0 and abs(w1 - 1) < mpf("1e-20") and abs(w2 - 1) < mpf("1e-20") else "INCONSISTENCY FOUND"))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
