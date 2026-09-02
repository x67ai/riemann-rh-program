#!/usr/bin/env python3
"""validate_arb_ft.py -- independent (mpmath) cross-validation of the Arb leg's f_t + E enclosure of H_t/B_t.

NOT the second producer leg (that is the mpmath-BALL leg, a separate deliverable): this is heuristic
high-precision floating point (mpmath 1.3.0, dps 30) used only to check that the Arb leg's rigorous
enclosure f_t(z) (+-) (rad + E) CONTAINS the reference value H_t(z)/B_t(z).  A pass is evidence; a
failure is stop-the-line.

Reference evaluator (independent code path, mpmath only):
  * Phi(u) = sum_{n>=1} (2 pi^2 n^4 e^{9u} - 3 pi n^2 e^{5u}) exp(-pi n^2 e^{4u})        (P15 (3), p1)
  * H_0(z) = (1/8) xi(1/2 + i z/2), xi(s) = (s(s-1)/2) pi^{-s/2} Gamma(s/2) zeta(s)   (P15 (1)-(2), p1)
  * Derivation D-V1 (heat-flow representation used for t > 0 at large x, where the u-integral oscillates too
    fast for quadrature).  For w ~ N(0,1): E[cos((z + i sqrt(2t) w) u)] = cos(zu) E[cosh(sqrt(2t) w u)]
    - i sin(zu) E[sinh(sqrt(2t) w u)] = cos(zu) e^{t u^2}  (E cosh(a w) = e^{a^2/2}, sinh odd).  Hence, by Fubini
    (super-exponential decay of Phi), H_t(z) = int_0^inf e^{tu^2} Phi(u) cos(zu) du = E_w[ H_0(z + i sqrt(2t) w) ]
    = (2 pi)^{-1/2} int_R H_0(z + i sqrt(2t) w) e^{-w^2/2} dw.  With z = x+iy this is a NON-oscillatory Gaussian
    integral of xi along Re s = (1 - y - sqrt(2t) w)/2, Im s = x/2.  D-V1 is itself checked numerically against
    the direct u-integral at x in {50, 120, 200} (section A of the run).
  * B_t(z) = M_t((1+y-ix)/2) from (6), (9), (10), (11) re-implemented in mpmath.
The Arb side is called through producer_arb.point_hook (direct summation of (92) + the D-A2 defect bound).

Containment test: exact rational arithmetic on the ball's mid/rad (Fractions) against the reference converted
exactly from its binary mantissa/exponent, with a declared decimal slack 1e-25 (M1 harness lesson: never compare
prints, never feed floats).
"""
import os, sys, time
from fractions import Fraction
import mpmath
from mpmath import mp, mpf, mpc, pi, exp, cos, log, sqrt, gamma, zeta, quad, inf

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import producer_arb as PA  # the Arb leg (only its point hook and the exact ball->rational helpers are used)

mp.dps = 30


def Phi(u):
    s = mpf(0); n = 1
    while True:
        e4 = exp(4 * u)
        term = (2 * pi ** 2 * n ** 4 * exp(9 * u) - 3 * pi * n ** 2 * exp(5 * u)) * exp(-pi * n ** 2 * e4)
        s += term
        if abs(term) < mpf(10) ** (-mp.dps - 10) and n > 2:
            break
        n += 1
        if n > 200:
            break
    return s


def xi(s):
    return (s * (s - 1) / 2) * pi ** (-s / 2) * gamma(s / 2) * zeta(s)


def H0(z):
    return xi(mpf(1) / 2 + 1j * z / 2) / 8


def Ht_direct(z, t):
    f = lambda u: exp(t * u * u) * Phi(u) * cos(z * u)
    # Phi(u) ~ exp(9u - pi e^{4u}); negligible beyond u ~ 1.2
    return quad(f, mpmath.linspace(0, mpf("1.4"), 60))


def Ht_heat(z, t):
    if t == 0:
        return H0(z)
    c = sqrt(2 * t)
    f = lambda w: H0(z + 1j * c * w) * exp(-w * w / 2)
    return quad(f, mpmath.linspace(-12, 12, 25)) / sqrt(2 * pi)


def alpha_mp(s):
    return 1 / (2 * s) + 1 / (s - 1) + mpmath.log(s / (2 * pi)) / 2


def M0_mp(s):
    return (mpf(1) / 8) * (s * (s - 1) / 2) * pi ** (-s / 2) * sqrt(2 * pi) * exp((s / 2 - mpf(1) / 2) * mpmath.log(s / 2) - s / 2)


def Bt_mp(z, t):
    s = (1 + z.imag - 1j * z.real) / 2
    return exp(t / 4 * alpha_mp(s) ** 2) * M0_mp(s)


def mpf_to_frac(v):
    sign, man, e, bc = mpmath.mpf(v)._mpf_
    q = Fraction(int(man)) * (Fraction(2) ** e)
    return -q if sign else q


def main():
    out = []
    def log(msg):
        print(msg); out.append(msg); sys.stdout.flush()
    log(f"validate_arb_ft.py -- mpmath {mpmath.__version__} dps {mp.dps}; python-flint {PA.flint.__version__} prec {PA.PREC}")
    # ---- Section A: D-V1 (heat-flow representation) against the direct u-integral, and B_t both ways
    log("A. D-V1 heat-flow representation vs direct u-quadrature (moderate x):")
    for (x, y, t) in ((50, mpf("0.3"), mpf("0.1")), (120, mpf(1), mpf("0.186")), (200, mpf("0.16733"), mpf("0.05"))):
        z = mpc(x, y)
        d = Ht_direct(z, t); h = Ht_heat(z, t)
        log(f"   x={x} y={y} t={t}: direct={mpmath.nstr(d, 15)} heat={mpmath.nstr(h, 15)} rel.diff={mpmath.nstr(abs(d-h)/abs(d), 3)}")
        assert abs(d - h) / abs(d) < mpf(10) ** -12, "D-V1 check failed"
    log("   D-V1 PASS (rel diff < 1e-12)")
    # ---- Section B: containment at >= 30 points in region (5)
    log("B. containment H_t/B_t in f_t (+-) (rad + E), Arb leg vs mpmath reference:")
    xs = [200, 1000, 3000, 10000]
    ts = [Fraction(0), Fraction(1, 20), Fraction(93, 500), Fraction(1, 5)]
    ys = [Fraction(16733, 100000), Fraction(1, 2), Fraction(1)]
    n_ok = n_tot = 0; worst_ratio = 0
    widths = []
    for x in xs:
        for t in ts:
            for y in ys:
                t0 = time.time()
                z = mpc(x, mpf(y.numerator) / y.denominator)
                tt = mpf(t.numerator) / t.denominator
                H = Ht_heat(z, tt)
                B = Bt_mp(z, tt)
                r = H / B
                d = PA.point_hook(Fraction(x), y, t)
                f = d["f"]; E = d["E"]
                re_lo, re_hi = PA.ball_interval(f.real); im_lo, im_hi = PA.ball_interval(f.imag)
                mid_re = (re_lo + re_hi) / 2; mid_im = (im_lo + im_hi) / 2
                rad = max(re_hi - re_lo, im_hi - im_lo) / 2
                rr, ri = mpf_to_frac(r.real), mpf_to_frac(r.imag)
                dist2 = (rr - mid_re) ** 2 + (ri - mid_im) ** 2
                allow = rad + E + Fraction(1, 10 ** 25)
                contained = dist2 <= allow * allow
                # B_t agreement (both implementations of (6)-(11))
                Blo, Bhi = PA.ball_interval(d["B"].real); Bilo, Bihi = PA.ball_interval(d["B"].imag)
                Bref = B
                relB = abs(complex(float((Blo + Bhi) / 2 / (mpf_to_frac(Bref.real) if Bref.real != 0 else 1)))) if False else None
                bdiff = abs(mpc(float((Blo + Bhi) / 2), float((Bilo + Bihi) / 2)) - Bref) / abs(Bref) if abs(Bref) > 0 else mpf(0)
                dist = float(sqrt(mpf(dist2.numerator) / dist2.denominator))
                ratio = dist / float(E) if E > 0 else float("inf")
                worst_ratio = max(worst_ratio, ratio)
                widths.append((x, float(t), float(y), float(rad), float(E)))
                n_tot += 1; n_ok += contained
                log(f"   x={x:5d} t={float(t):.3f} y={float(y):.5f} N={d['N']:3d} |ref|={float(abs(r)):.5f} |f|={float(abs(complex(float(mid_re), float(mid_im)))):.5f} "
                    f"rad_f={float(rad):.1e} E={float(E):.3e} (eC0={float(d['E_C0']):.2e} eAB={float(d['E_AB']):.2e}) |ref-f|={dist:.3e} "
                    f"|ref-f|/E={ratio:.3f} contained={contained} relB={mpmath.nstr(bdiff, 2)} {time.time()-t0:.1f}s")
    log(f"   containment: {n_ok}/{n_tot} points; worst |ref-f|/E = {worst_ratio:.4f} (must be <= 1)")
    log("   widths (x, t, y, rad_f, E): rad_f is the ball radius of the Arb f_t; E the D-A2 defect (the enclosure of H_t/B_t has radius rad_f + E)")
    log(f"   min rad_f = {min(w[3] for w in widths):.2e}, max rad_f = {max(w[3] for w in widths):.2e}; E ranges {min(w[4] for w in widths):.2e} .. {max(w[4] for w in widths):.2e}")
    verdict = "ALL PASS" if n_ok == n_tot else "FAIL"
    log(f"VERDICT: {verdict}")
    with open(os.path.join(HERE, "arb-validation-run.txt"), "w") as fh:
        fh.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
