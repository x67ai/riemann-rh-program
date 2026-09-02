"""hurwitz_encl.py -- rigorous complex-ball enclosures of the Hurwitz zeta
function zeta(s, a) for exact rational a in (0, 1], by Euler-Maclaurin with a
fully derived explicit remainder bound.  Needed for f_DH (FORMAT.md sec. 9.2:
f_DH is a rational-coefficient combination of zeta(s, j/5), j = 1..4).

D1 M1 v1, mpmath-ball producer leg (D-R3).  UNTRUSTED producer-side code;
output enters the certified statement only through H-ENCL (FORMAT.md sec. 8.1).

=============================================================================
DERIVATION (standing order 5; complete, with the general shift a)
=============================================================================
This file carries the SAME seven-step derivation as zeta_encl.py with
f(x) = (x + a)^{-s} in place of x^{-s}; steps 1, 2, 6 (the Euler-Maclaurin
identity (EM) with the periodized-Bernoulli remainder, and the certified
constant C_j = sup_{[0,1]} |B_j(x) - B_j|) are IDENTICAL word for word --
they never mention f -- and are not repeated; see zeta_encl.py STEPS 1-2, 6.
The specialization steps, redone here for the shifted function:

STEP 3' (specialize; let M -> infinity).  zeta(s, a) := sum_{n=0}^{infty}
(n+a)^{-s} for sigma > 1, continued elsewhere.  Take f(x) = (x+a)^{-s}, a in
(0, 1] fixed rational, so f is smooth on [0, infinity) and
f^{(j)}(x) = (-1)^j (s)_j (x+a)^{-s-j} ((s)_j the rising factorial).  Apply
(EM) of zeta_encl.py on [N, M], sigma > 1, and let M -> infinity (every M-term
is O(M^{-sigma}) and vanishes):
    sum_{n=N}^{infty} (n+a)^{-s}
      = (N+a)^{1-s}/(s-1) + (N+a)^{-s}/2
        + sum_{k=1}^{m} (B_{2k}/(2k)!) (s)_{2k-1} (N+a)^{-s-2k+1}
        + R_{N,m}(s, a),                                                  (T')
    R_{N,m}(s, a) = - ((s)_{2m+1}/(2m+1)!)
                      * integral_N^infty Bbar_{2m+1}(x) (x+a)^{-s-2m-1} dx,
using integral_N^infty (x+a)^{-s} dx = (N+a)^{1-s}/(s-1) and the same sign
bookkeeping as zeta_encl.py STEP 3.  Hence
    zeta(s, a) = sum_{n=0}^{N-1} (n+a)^{-s} + [right side of (T')].       (Z')

STEP 4' (analytic continuation).  Identical argument: for fixed N, m, a the
explicit part of (Z') is analytic on C minus {1} and the remainder integral is
locally uniformly convergent, hence analytic, on {sigma > -2m}; both sides
agree for sigma > 1, so (Z') holds on {sigma > -2m, s != 1}.  (mpmath's
mp.zeta(s, a) implements this same continuation; it is the independent
cross-check target, not an input.)

STEP 5' (remainder bound).  With G(x) = (Bbar_{2m+2}(x) - B_{2m+2})/(2m+2)
exactly as in zeta_encl.py STEP 5 (G(N) = 0, G' = Bbar_{2m+1}, |G| <=
C_{2m+2}/(2m+2)), integrate by parts:
    integral_N^infty Bbar_{2m+1}(x) (x+a)^{-s-2m-1} dx
      = (s+2m+1) * integral_N^infty G(x) (x+a)^{-s-2m-2} dx,
so
    |R_{N,m}(s, a)| <= |(s)_{2m+1}| * |s+2m+1| * C_{2m+2}
        / ( (2m+1)! * (2m+2) * (sigma+2m+1) ) * (N+a)^{-sigma-2m-1}.      (RB')
Validity: sigma + 2m + 1 > 0.  Note (N+a) >= N > 0 so the bound is finite and
the boundary term at x = N vanishes because G(N) = 0 (N an integer), exactly
as before -- the shift a does not move the INTEGER sample points, so the
periodized Bernoulli machinery is untouched.

STEP 7' (interval evaluation).  (n+a) = (n q + p)/q for a = p/q, so
    (n+a)^{-s} = exp(-s (log(n q + p) - log q))
with EXACT integer logarithms -- no rational rounding enters the exponent
before the (directed-rounded) iv log.  Everything else as zeta_encl.py STEP 7;
inclusion monotonicity gives: for every s in the input box, zeta(s, a) lies in
the output box.  Requirements enforced at run time: a = p/q with 0 < p <= q,
sigma_lo > 0 (scope guard), and the (s-1) box excludes 0 (certified in recip).

VALIDATION (python3 hurwitz_encl.py --validate): >= 200 random points s
(1/2 < sigma < 1, |t| <= 200) x random rational a including the four DH shifts
j/5: enclosure must contain mp.zeta(s, a) at dps 100 (independent float
pipeline), membership exact on Fractions with 10^-80 inflation; widths
reported.  Plus the a = 1 identity cross-check zeta(s, 1) = zeta(s) against
zeta_encl.py's INDEPENDENTLY WRITTEN evaluator (the two enclosures must
overlap, and each must contain the reference), and wide-box sampling.
"""

import math
from fractions import Fraction

from mpmath import iv

from ball import iv_exp   # outward-inflated transcendental endpoints (AUDIT F-1, repair R1)

from ball import (Ball, iv_from_fraction, iv_from_fraction_pair, iv_from_int,
                  ivmpf_bounds, set_prec)
from zeta_encl import bern_exact, c_sup, _log_int, _auto_params

__all__ = ["hurwitz_ball"]


def _pow_shift_neg(n, p, q, s_ball):
    """Ball enclosure of (n + p/q)^{-s} = exp(-s (log(nq+p) - log q))."""
    ln = _log_int(n * q + p) - _log_int(q)
    return Ball((-s_ball.re) * ln, (-s_ball.im) * ln).exp()


def hurwitz_ball(s_ball, a, N=None, m=None):
    """Rigorous enclosure of {zeta(s, a) : s in the input box}, a = Fraction in
    (0, 1], by (Z') + (RB')."""
    a = Fraction(a)
    p, q = a.numerator, a.denominator
    if not (0 < p <= q):
        raise ValueError("hurwitz_ball: need a = p/q in (0, 1], got %s" % (a,))
    N, m = _auto_params(s_ball, m, N)
    slo, _shi = s_ball.re_bounds()
    if not slo > 0:
        raise ValueError("hurwitz_ball scope guard: need sigma_lo > 0, got %s" % (slo,))

    # ---- partial sum  sum_{n=0}^{N-1} (n+a)^{-s}
    total = _pow_shift_neg(0, p, q, s_ball)
    for n in range(1, N):
        total = total + _pow_shift_neg(n, p, q, s_ball)

    # ---- (N+a)^{1-s}/(s-1) ;  ln(N+a) exactly as log(Nq+p) - log(q)
    lnNa = _log_int(N * q + p) - _log_int(q)
    one_minus_s = Ball.from_int(1) - s_ball
    na_pow_1ms = Ball(one_minus_s.re * lnNa, one_minus_s.im * lnNa).exp()
    total = total + na_pow_1ms * (s_ball - Ball.from_int(1)).recip()

    # ---- (N+a)^{-s}/2 and the Bernoulli sum
    NS = _pow_shift_neg(N, p, q, s_ball)
    total = total + NS.scale_iv(iv_from_fraction(Fraction(1, 2)))
    rising = s_ball
    napow = Fraction(1)                          # exact (N+a)^{-(2k-1)} accumulator
    for k in range(1, m + 1):
        if k >= 2:
            j = 2 * k - 3
            rising = rising * (s_ball + Ball.from_int(j)) * (s_ball + Ball.from_int(j + 1))
        napow = napow / (N + a) / (N + a) if k >= 2 else Fraction(1) / (N + a)
        c_k = bern_exact(2 * k) / math.factorial(2 * k) * napow
        total = total + (NS * rising).scale_iv(iv_from_fraction(c_k))

    # ---- remainder bound (RB')
    prod_ub = iv_from_int(1)
    for j in range(0, 2 * m + 1):
        prod_ub = prod_ub * (s_ball + Ball.from_int(j)).abs_iv()
    _, prod_ub_hi = ivmpf_bounds(prod_ub)
    _, s2m1_hi = ivmpf_bounds((s_ball + Ball.from_int(2 * m + 1)).abs_iv())
    c_ub, _ = c_sup(2 * m + 2)
    denom = Fraction(math.factorial(2 * m + 1)) * (2 * m + 2) * (slo + 2 * m + 1)
    expo = iv_from_fraction(-(slo + 2 * m + 1)) * lnNa
    _, napow_hi = ivmpf_bounds(iv_exp(expo))
    r = prod_ub_hi * s2m1_hi * c_ub * napow_hi / denom
    pad = iv_from_fraction_pair(-r, r)
    return total + Ball(pad, pad)


# ---------------------------------------------------------------- validation

def _validate(points=200, seed=1914, prec=288):
    import random
    from mpmath import mp
    from ball import mpf_tuple_to_fraction as m2f
    import zeta_encl

    rng = random.Random(seed)
    set_prec(prec)
    mp.dps = 100
    EPS = Fraction(1, 10 ** 80)
    failures = 0
    widths = []

    def frac(lo, hi, den=10 ** 6):
        return Fraction(rng.randint(int(lo * den), int(hi * den)), den)

    DH_SHIFTS = [Fraction(1, 5), Fraction(2, 5), Fraction(3, 5), Fraction(4, 5)]
    print("hurwitz_encl validation: %d random points, sigma in (0.501, 0.999), "
          "|t| <= 200, a in {j/5 (DH shifts), random p/q}, iv prec %d, "
          "reference mp.zeta(s, a) at dps 100" % (points, prec))
    for k in range(points):
        sig = frac(0.501, 0.999)
        t = frac(-200, 200)
        if k % 2 == 0:
            a = DH_SHIFTS[(k // 2) % 4]
        else:
            qd = rng.randint(2, 40)
            a = Fraction(rng.randint(1, qd), qd)
        s = Ball.from_fractions(sig, t)
        z = hurwitz_ball(s, a)
        ref = mp.zeta(mp.mpc(mp.mpf(sig.numerator) / sig.denominator,
                             mp.mpf(t.numerator) / t.denominator),
                      mp.mpf(a.numerator) / a.denominator)
        rlo, rhi = z.re_bounds()
        ilo, ihi = z.im_bounds()
        ok = (rlo - EPS <= m2f(ref.real._mpf_) <= rhi + EPS and
              ilo - EPS <= m2f(ref.imag._mpf_) <= ihi + EPS)
        widths.append(z.max_width())
        if not ok:
            failures += 1
            print("  CONTAINMENT FAIL at s = %s + %si, a = %s" % (sig, t, a))
    widths.sort()
    print("  containment: %d/%d PASS" % (points - failures, points))
    print("  enclosure widths: median %.3e, max %.3e"
          % (float(widths[len(widths) // 2]), float(widths[-1])))

    # a = 1 cross-check against the independently written zeta_encl evaluator
    xfail = 0
    for k in range(25):
        sig = frac(0.51, 0.99)
        t = frac(-120, 120)
        s = Ball.from_fractions(sig, t)
        zh = hurwitz_ball(s, Fraction(1))
        zz = zeta_encl.zeta_ball(s)
        ref = mp.zeta(mp.mpc(mp.mpf(sig.numerator) / sig.denominator,
                             mp.mpf(t.numerator) / t.denominator))
        for z in (zh, zz):
            rlo, rhi = z.re_bounds()
            ilo, ihi = z.im_bounds()
            if not (rlo - EPS <= m2f(ref.real._mpf_) <= rhi + EPS and
                    ilo - EPS <= m2f(ref.imag._mpf_) <= ihi + EPS):
                xfail += 1
        if zh.intersect(zz) is None:
            xfail += 1
            print("  a=1 OVERLAP FAIL at s = %s + %si" % (sig, t))
    print("  a = 1 cross-check vs zeta_encl (25 points, overlap + containment): "
          "%d failures" % xfail)

    # wide boxes
    box_fail = 0
    for k in range(15):
        sig = frac(0.55, 0.95)
        t = frac(-100, 100)
        dsig = Fraction(rng.randint(1, 200), 10 ** 4)
        dt = Fraction(rng.randint(1, 200), 10 ** 4)
        a = DH_SHIFTS[k % 4]
        s = Ball.from_fraction_boxes((sig, sig + dsig), (t, t + dt))
        z = hurwitz_ball(s, a)
        rlo, rhi = z.re_bounds()
        ilo, ihi = z.im_bounds()
        for u in (Fraction(0), Fraction(1, 2), Fraction(1)):
            for v in (Fraction(0), Fraction(1, 2), Fraction(1)):
                ps, pt = sig + dsig * u, t + dt * v
                ref = mp.zeta(mp.mpc(mp.mpf(ps.numerator) / ps.denominator,
                                     mp.mpf(pt.numerator) / pt.denominator),
                              mp.mpf(a.numerator) / a.denominator)
                if not (rlo - EPS <= m2f(ref.real._mpf_) <= rhi + EPS and
                        ilo - EPS <= m2f(ref.imag._mpf_) <= ihi + EPS):
                    box_fail += 1
                    print("  BOX FAIL a=%s box=(%s,%s)" % (a, sig, t))
    print("  wide-box sampling: 15 boxes x 9 points, %d failures" % box_fail)
    return failures + xfail + box_fail


if __name__ == "__main__":
    import sys
    if "--validate" in sys.argv:
        pts = 200
        for arg in sys.argv:
            if arg.startswith("--points="):
                pts = int(arg.split("=", 1)[1])
        rc = _validate(points=pts)
        sys.exit(0 if rc == 0 else 1)
    print(__doc__)
