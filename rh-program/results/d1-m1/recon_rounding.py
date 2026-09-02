"""recon_rounding.py -- RECONCILIATION (2026-09-02) of AUDIT F finding F-1: exact
directed-rounding tests of mpmath 1.3.0's interval primitives at prec 288 against
prec-1200 nearest-rounded references (reference error 2^-1199 relative, ~10^-270 below
one prec-288 ulp; NO tolerance anywhere -- exact Fraction comparisons).

Three blocks:
 (1) the RAW primitives exactly as libmpi calls them (F-1 as filed: mpf_exp/log/atan/sqrt
     with round_floor/round_ceiling, and mpf_pi) -- reproduces audit_F_mpmath_rounding.py
     with the same seed; expected: exp ceilings below the truth (the finding), sqrt 0;
 (2) mpmath's OWN interval cos/sin (mpi_cos_sin, which perturbs its endpoints) in the
     regimes neither audit tested at the exact level: |x| <= 1e5 (the pow_int_neg regime
     at T = 1e4) and the cancellation regimes x ~ (k+1/2)pi (cos tiny), x ~ k pi (sin tiny);
 (3) the REPAIRED wrappers ball.iv_exp / iv_log / iv_atan / iv_pi / iv_cos / iv_sin
     (repair R1: outward inflation by 2^-(prec-16) relative), same samples as (1)/(2):
     expected 0 violations.
A violation is floor > truth or ceiling < truth."""
import math
import random
import sys
from fractions import Fraction

from mpmath import iv
from mpmath.libmp import (mpf_exp, mpf_log, mpf_atan, mpf_sqrt, mpf_pi, mpf_cos, mpf_sin,
                          mpf_mul, mpf_add, mpf_pos, from_int, from_man_exp,
                          round_floor, round_ceiling, round_nearest)
from mpmath.libmp.libmpi import mpi_cos_sin

import ball
from ball import ivmpf_bounds, mpf_tuple_to_fraction as fr, set_prec

PREC, HP = 288, 1200


def rnd_mpf(rng, lo, hi, prec=PREC):
    x = rng.uniform(lo, hi)
    man = rng.getrandbits(prec) | (1 << (prec - 1))
    e = math.frexp(abs(x))[1] - prec
    return from_man_exp(man if x >= 0 else -man, e, prec, round_nearest)


def report(name, n, viol, worst):
    print("  %-34s samples %6d  violations %5d  worst rel excess %.3e   (1 ulp at 288 bits = 2^-288 = %.3e)"
          % (name, n, viol, float(worst), 2.0 ** -288))


def raw_test(name, fn, xs):
    viol = 0
    worst = Fraction(0)
    for x in xs:
        ref = fr(fn(x, HP, round_nearest))
        lo, hi = fr(fn(x, PREC, round_floor)), fr(fn(x, PREC, round_ceiling))
        if lo > ref:
            viol += 1
            worst = max(worst, (lo - ref) / abs(ref) if ref else lo - ref)
        if hi < ref:
            viol += 1
            worst = max(worst, (ref - hi) / abs(ref) if ref else ref - hi)
    report(name, len(xs), viol, worst)
    return viol


def wrapped_test(name, wrapper, ref_fn, xs):
    viol = 0
    worst = Fraction(0)
    for x in xs:
        ref = fr(ref_fn(x, HP, round_nearest))
        lo, hi = ivmpf_bounds(wrapper(iv.make_mpf((x, x))))
        if lo > ref:
            viol += 1
            worst = max(worst, (lo - ref) / abs(ref) if ref else lo - ref)
        if hi < ref:
            viol += 1
            worst = max(worst, (ref - hi) / abs(ref) if ref else ref - hi)
    report(name, len(xs), viol, worst)
    return viol


def cossin_raw_test(name, xs):
    viol = 0
    worst = Fraction(0)
    for x in xs:
        (clo, chi), (slo, shi) = mpi_cos_sin((x, x), PREC)
        for lo, hi, ref in ((fr(clo), fr(chi), fr(mpf_cos(x, HP, round_nearest))),
                            (fr(slo), fr(shi), fr(mpf_sin(x, HP, round_nearest)))):
            if lo > ref:
                viol += 1
                worst = max(worst, (lo - ref) / abs(ref) if ref else lo - ref)
            if hi < ref:
                viol += 1
                worst = max(worst, (ref - hi) / abs(ref) if ref else ref - hi)
    report(name, len(xs), viol, worst)
    return viol


def main():
    set_prec(PREC)
    rng = random.Random(20260902)     # AUDIT F's seed, so block (1) reproduces its log
    total_raw = total_cs = total_wrapped = 0
    print("RECONCILER (2026-09-02): exact directed-rounding tests at prec 288 vs prec-1200 reference")
    print("(1) RAW mpmath primitives as libmpi calls them (AUDIT F-1 as filed; seed 20260902):")
    xs_exp = [rnd_mpf(rng, -30.0, 30.0) for _ in range(20000)]
    xs_exp1 = [rnd_mpf(rng, -1.0, 1.0) for _ in range(20000)]
    xs_log = [rnd_mpf(rng, 1e-3, 1e4) for _ in range(20000)]
    xs_atan = [rnd_mpf(rng, -50.0, 50.0) for _ in range(20000)]
    xs_sqrt = [rnd_mpf(rng, 1e-3, 1e4) for _ in range(20000)]
    total_raw += raw_test("exp [-30,30]", mpf_exp, xs_exp)
    total_raw += raw_test("exp [-1,1]", mpf_exp, xs_exp1)
    total_raw += raw_test("log [1e-3,1e4]", mpf_log, xs_log)
    total_raw += raw_test("atan [-50,50]", mpf_atan, xs_atan)
    total_raw += raw_test("sqrt [1e-3,1e4] (control)", mpf_sqrt, xs_sqrt)
    lo, hi = fr(mpf_pi(PREC, round_floor)), fr(mpf_pi(PREC, round_ceiling))
    ref = fr(mpf_pi(HP, round_nearest))
    print("  pi: floor <= truth: %s, ceiling >= truth: %s" % (lo <= ref, hi >= ref))
    total_raw += (lo > ref) + (hi < ref)
    print("  RAW total violations: %d  (F-1 REPRODUCED iff > 0 for exp and 0 for sqrt)" % total_raw)

    print("(2) mpmath's OWN interval cos/sin (mpi_cos_sin, perturbed endpoints), exact:")
    rng2 = random.Random(902)
    xs_big = [rnd_mpf(rng2, -1e5, 1e5) for _ in range(20000)]
    xs_small = [rnd_mpf(rng2, -10.0, 10.0) for _ in range(20000)]
    pi_hp = mpf_pi(HP, round_nearest)
    half = from_man_exp(1, -1)

    def near(k, plus_half):
        kk = from_int(k)
        if plus_half:
            kk = mpf_add(kk, half, HP, round_nearest)
        return mpf_pos(mpf_mul(kk, pi_hp, HP, round_nearest), PREC, round_nearest)
    xs_cos0 = [near(rng2.randint(-30000, 30000), True) for _ in range(5000)]
    xs_sin0 = [near(rng2.randint(-30000, 30000), False) for _ in range(5000)]
    total_cs += cossin_raw_test("cos/sin |x|<=1e5", xs_big)
    total_cs += cossin_raw_test("cos/sin |x|<=10", xs_small)
    total_cs += cossin_raw_test("cos/sin x~(k+1/2)pi (cos tiny)", xs_cos0)
    total_cs += cossin_raw_test("cos/sin x~k pi (sin tiny)", xs_sin0)
    print("  mpi_cos_sin total violations: %d" % total_cs)

    print("(3) REPAIRED wrappers (ball.py R1: outward inflation 2^-(prec-16) relative), exact:")
    total_wrapped += wrapped_test("iv_exp [-30,30]", ball.iv_exp, mpf_exp, xs_exp)
    total_wrapped += wrapped_test("iv_exp [-1,1]", ball.iv_exp, mpf_exp, xs_exp1)
    total_wrapped += wrapped_test("iv_log [1e-3,1e4]", ball.iv_log, mpf_log, xs_log)
    total_wrapped += wrapped_test("iv_atan [-50,50]", ball.iv_atan, mpf_atan, xs_atan)
    total_wrapped += wrapped_test("iv_cos |x|<=1e5", ball.iv_cos, mpf_cos, xs_big)
    total_wrapped += wrapped_test("iv_sin |x|<=1e5", ball.iv_sin, mpf_sin, xs_big)
    total_wrapped += wrapped_test("iv_cos x~(k+1/2)pi", ball.iv_cos, mpf_cos, xs_cos0)
    total_wrapped += wrapped_test("iv_sin x~k pi", ball.iv_sin, mpf_sin, xs_sin0)
    lo, hi = ivmpf_bounds(ball.iv_pi())
    print("  iv_pi: floor <= truth: %s, ceiling >= truth: %s" % (lo <= ref, hi >= ref))
    total_wrapped += (lo > ref) + (hi < ref)
    print("  REPAIRED total violations: %d  (must be 0)" % total_wrapped)
    print("SUMMARY: raw=%d  mpi_cos_sin=%d  repaired=%d" % (total_raw, total_cs, total_wrapped))
    return 0 if total_wrapped == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
