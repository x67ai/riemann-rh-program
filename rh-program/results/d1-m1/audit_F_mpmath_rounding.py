"""audit_F_mpmath_rounding.py -- AUDIT F: is mpmath 1.3.0's directed rounding of the
transcendental primitives the mp leg trusts (exp, log, atan, pi, sqrt) actually
rigorous?

ball.py (module docstring, TRUST SURFACE) states the leg's single platform-trust
item: mpmath's iv context "computes every endpoint with directed rounding".  The
libmpi sources show mpi_exp/mpi_log/mpi_atan/mpi_pi call the mpf primitive with
rnd=round_floor / round_ceiling; those primitives compute an APPROXIMATION at
prec + guard bits (14 for exp, 20 for log, 30+ for atan) and then round THAT
approximation in the requested direction (libelefun.py: from_man_exp(man, ...,
prec, rnd)).  Directed rounding of an approximation is not a rigorous bound: if
the true value lies just below a prec-representable number and the approximation
just above it, floor-rounding returns a value ABOVE the truth.  (mpi_cos_sin, by
contrast, multiplies its endpoints by (1 -+ 2^-wp+10) explicitly "to force
interval rounding" -- mpmath's own authors inflate there and NOT in exp/log/atan.)

This script searches for such violations empirically: for random arguments it
compares the prec-288 directed results against a prec-1200 nearest-rounded
reference (error <= 2^-1199 relative, far below one prec-288 ulp).  A violation
is: floor_result > ref  or  ceiling_result < ref  (exact Fraction comparison).
sqrt and division are correctly rounded in mpmath (integer algorithms) and are
included as controls: they must show ZERO violations.
"""
import random
import sys
from fractions import Fraction

from mpmath import mp
from mpmath.libmp import (mpf_exp, mpf_log, mpf_atan, mpf_sqrt, mpf_div, mpf_pi,
                          round_floor, round_ceiling, round_nearest, from_man_exp)
from mpmath import mpf


def fr(t):
    sign, man, exp, bc = t
    if man == 0:
        return Fraction(0)
    v = Fraction(man) * Fraction(2) ** exp
    return -v if sign else v


def rnd_mpf(rng, lo, hi, prec=288):
    # random dyadic with a full prec-bit mantissa in [lo, hi]
    x = rng.uniform(lo, hi)
    man = rng.getrandbits(prec) | (1 << (prec - 1))
    # scale to the magnitude of x
    import math
    e = math.frexp(abs(x))[1] - prec
    t = from_man_exp(man if x >= 0 else -man, e, prec, round_nearest)
    return t


def test(name, fn1, fnref, samples, rng, argrange):
    prec, hp = 288, 1200
    viol_lo = viol_hi = 0
    worst = Fraction(0)
    for i in range(samples):
        x = rnd_mpf(rng, *argrange, prec=prec)
        ref = fr(fnref(x, hp, round_nearest))
        lo = fr(fn1(x, prec, round_floor))
        hi = fr(fn1(x, prec, round_ceiling))
        if lo > ref:
            viol_lo += 1
            worst = max(worst, (lo - ref) / abs(ref) if ref else lo - ref)
        if hi < ref:
            viol_hi += 1
            worst = max(worst, (ref - hi) / abs(ref) if ref else ref - hi)
    print("  %-6s samples %6d  floor>truth: %5d  ceiling<truth: %5d  worst rel excess %.3e (2^-288 = %.3e)"
          % (name, samples, viol_lo, viol_hi, float(worst), 2.0 ** -288))
    return viol_lo + viol_hi


def main():
    rng = random.Random(20260902)
    total = 0
    print("AUDIT F: directed-rounding rigor of mpmath 1.3.0 primitives at prec 288 vs prec-1200 reference")
    total += test("exp", mpf_exp, mpf_exp, 20000, rng, (-30.0, 30.0))
    total += test("exp<1", mpf_exp, mpf_exp, 20000, rng, (-1.0, 1.0))
    total += test("log", mpf_log, mpf_log, 20000, rng, (1e-3, 1e4))
    total += test("atan", mpf_atan, mpf_atan, 20000, rng, (-50.0, 50.0))
    total += test("sqrt", mpf_sqrt, mpf_sqrt, 20000, rng, (1e-3, 1e4))
    # pi
    lo, hi = fr(mpf_pi(288, round_floor)), fr(mpf_pi(288, round_ceiling))
    ref = fr(mpf_pi(1200, round_nearest))
    print("  pi     floor<=truth: %s  ceiling>=truth: %s" % (lo <= ref, hi >= ref))
    total += (lo > ref) + (hi < ref)
    print("TOTAL directed-rounding violations found: %d" % total)
    print("(sqrt is correctly rounded by construction and serves as the control: it must be 0)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
