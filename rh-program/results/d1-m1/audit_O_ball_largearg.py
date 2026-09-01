"""audit_O_ball_largearg.py -- AUDITOR O: close a coverage GAP in ball.py's self-test.

ball.py --selftest draws its test points from |Re|, |Im| <= 5 (rnd_point_ball,
scale = 5), so mpmath's interval exp/cos/sin are exercised only at SMALL
arguments.  Production does not stay there: zeta_ball evaluates
pow_int_neg(n, s) = exp(-s log n), whose imaginary part is -t*log n, i.e. up to
|t| * log N ~ 1e4 * 8.5 = 8.5e4 for the T = 10^4 acceptance box -- deep in the
argument-reduction regime of iv.cos / iv.sin, which the self-test never enters.

This script tests Ball.exp, iv.cos, iv.sin, iv.exp and pow_int_neg at those
magnitudes against an independent dps-140 mp reference, with exact Fraction
membership.  A failure here would be a FATAL producer defect.
"""
import random, sys
from fractions import Fraction
from mpmath import mp, iv
from ball import Ball, set_prec, ivmpf_bounds, mpf_tuple_to_fraction as m2f
from zeta_encl import pow_int_neg

SEED = 14_2026_902
PREC = 288
EPS = Fraction(1, 10 ** 100)

rng = random.Random(SEED)
set_prec(PREC)
mp.dps = 140
fails = 0
n = 0


def frac(lo, hi, den=10 ** 9):
    return Fraction(rng.randint(int(lo * den), int(hi * den)), den)


def mpf_of(f):
    return mp.mpf(f.numerator) / mp.mpf(f.denominator)


def check(cond, what):
    global fails, n
    n += 1
    if not cond:
        fails += 1
        print("  FAIL:", what)


print("AUDIT O -- ball.py large-argument coverage, seed %d, prec %d, ref dps 140" % (SEED, PREC))
for k in range(400):
    b = frac(-2e5, 2e5)                    # the regime pow_int_neg actually uses
    a = frac(-25, 5)
    z = Ball.from_fractions(a, b).exp()
    ref = mp.exp(mp.mpc(mpf_of(a), mpf_of(b)))
    rlo, rhi = z.re_bounds(); ilo, ihi = z.im_bounds()
    zr, zi = m2f(ref.real._mpf_), m2f(ref.imag._mpf_)
    scale = max(abs(zr), abs(zi), Fraction(1, 10 ** 12))
    tol = scale * Fraction(1, 10 ** 60)
    check(rlo - tol <= zr <= rhi + tol and ilo - tol <= zi <= ihi + tol,
          "Ball.exp at %s + %si (widths %.3e)" % (a, b, float(z.max_width())))
    # the interval trig primitives themselves
    c = iv.cos(iv.mpf(b.numerator) / iv.mpf(b.denominator))
    clo, chi = ivmpf_bounds(c)
    cref = m2f(mp.cos(mpf_of(b))._mpf_)
    check(clo - EPS <= cref <= chi + EPS, "iv.cos at %s" % b)
    s = iv.sin(iv.mpf(b.numerator) / iv.mpf(b.denominator))
    slo, shi = ivmpf_bounds(s)
    sref = m2f(mp.sin(mpf_of(b))._mpf_)
    check(slo - EPS <= sref <= shi + EPS, "iv.sin at %s" % b)

# pow_int_neg exactly as zeta_ball calls it, at acceptance-scale heights
for k in range(200):
    sig = frac(0.5, 1.0)
    t = frac(-12000, 12000)
    nn = rng.randint(2, 6000)
    z = pow_int_neg(nn, Ball.from_fractions(sig, t))
    ref = mp.power(nn, -mp.mpc(mpf_of(sig), mpf_of(t)))
    rlo, rhi = z.re_bounds(); ilo, ihi = z.im_bounds()
    zr, zi = m2f(ref.real._mpf_), m2f(ref.imag._mpf_)
    tol = Fraction(1, 10 ** 60)
    check(rlo - tol <= zr <= rhi + tol and ilo - tol <= zi <= ihi + tol,
          "pow_int_neg(%d) at %s+%si" % (nn, sig, t))

# widest-interval stress: a genuinely WIDE imaginary interval (multiple periods)
for k in range(60):
    a = frac(-3, 1)
    b0 = frac(-1e5, 1e5)
    w = Fraction(rng.randint(1, 10 ** 4), 10 ** 3)     # up to 10 rad wide
    z = Ball.from_fraction_boxes((a, a), (b0, b0 + w)).exp()
    for u in (Fraction(0), Fraction(1, 3), Fraction(2, 3), Fraction(1)):
        bb = b0 + w * u
        ref = mp.exp(mp.mpc(mpf_of(a), mpf_of(bb)))
        rlo, rhi = z.re_bounds(); ilo, ihi = z.im_bounds()
        zr, zi = m2f(ref.real._mpf_), m2f(ref.imag._mpf_)
        tol = Fraction(1, 10 ** 60)
        check(rlo - tol <= zr <= rhi + tol and ilo - tol <= zi <= ihi + tol,
              "wide-Im Ball.exp a=%s b=[%s,%s] u=%s" % (a, b0, b0 + w, u))

print("  %d checks, %d failures" % (n, fails))
sys.exit(0 if fails == 0 else 1)
