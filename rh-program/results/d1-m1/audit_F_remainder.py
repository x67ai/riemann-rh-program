"""audit_F_remainder.py -- AUDIT F: direct numerical test of the Euler-Maclaurin remainder
bound (RB)/(RB') AS IMPLEMENTED: for random s (thin points) recompute, at dps 120 in plain
mpmath floats, the explicit part of (Z)/(Z') with the SAME (N, m) the code uses, subtract it
from mp.zeta to obtain the TRUE remainder R, and compare |R| with the code's certified pad r
(re-derived here from the code's own formula, exact Fractions).  Requirement: |R| <= r at
every point; the ratio r/|R| shows how loose the bound is (expected ~2 = C_{2m+2}/|B_{2m+2}|
times |s+2m+1|/(sigma+2m+1)).
"""
import math, random, sys
from fractions import Fraction
from mpmath import mp, mpf, mpc, zeta, power, rf, bernoulli
from zeta_encl import bern_exact, c_sup, _auto_params
from ball import Ball, set_prec

mp.dps = 120
rng = random.Random(4242)
set_prec(288)

def explicit_part(s, N, m, a=None):
    # sum_{n<N} (n+a)^{-s} + (N+a)^{1-s}/(s-1) + (N+a)^{-s}/2 + sum_k B_{2k}/(2k)! (s)_{2k-1} (N+a)^{-s-2k+1}
    if a is None:
        S = sum(power(n, -s) for n in range(1, N)); Na = mpf(N)
    else:
        S = sum(power(n + a, -s) for n in range(0, N)); Na = N + a
    S += power(Na, 1 - s) / (s - 1) + power(Na, -s) / 2
    for k in range(1, m + 1):
        B = bern_exact(2 * k)
        S += mpf(B.numerator) / B.denominator / math.factorial(2 * k) * rf(s, 2 * k - 1) * power(Na, -s - 2 * k + 1)
    return S

def code_pad(sig, t, N, m, a=Fraction(0)):
    # (RB') exactly as zeta_encl/hurwitz_encl compute r, for a thin point (sup = value)
    s = mpc(mpf(sig.numerator) / sig.denominator, mpf(t.numerator) / t.denominator)
    sigm = mpf(sig.numerator) / sig.denominator
    prod = mp.mpf(1)
    for j in range(0, 2 * m + 1):
        prod *= abs(s + j)
    s2m1 = abs(s + 2 * m + 1)
    c_ub, _ = c_sup(2 * m + 2)
    denom = mpf(math.factorial(2 * m + 1)) * (2 * m + 2) * (sigm + 2 * m + 1)
    Na = mpf(N) + mpf(a.numerator) / a.denominator
    return prod * s2m1 * (mpf(c_ub.numerator) / c_ub.denominator) * power(Na, -(sigm + 2 * m + 1)) / denom

worst = 0; n = 0
for regime in ("generic", "t~1e4", "sigma~1/2", "sigma~1"):
    for _ in range(12 if regime != "t~1e4" else 4):
        if regime == "generic": sig, t = rng.uniform(0.51, 0.99), rng.uniform(-300, 300)
        elif regime == "t~1e4": sig, t = rng.uniform(0.51, 0.99), rng.uniform(9990, 10001)
        elif regime == "sigma~1/2": sig, t = 0.5 + rng.uniform(1e-6, 1e-3), rng.uniform(-200, 200)
        else: sig, t = 1 - rng.uniform(1e-6, 1e-3), rng.uniform(-200, 200)
        sig, t = Fraction(sig).limit_denominator(10**9), Fraction(t).limit_denominator(10**9)
        s = mpc(mpf(sig.numerator) / sig.denominator, mpf(t.numerator) / t.denominator)
        N, m = _auto_params(Ball.from_fractions(sig, t))
        for a in (None, Fraction(1, 5), Fraction(3, 5)):
            am = None if a is None else mpf(a.numerator) / a.denominator
            true = zeta(s) if a is None else zeta(s, am)
            R = true - explicit_part(s, N, m, am)
            r = code_pad(sig, t, N, m, Fraction(0) if a is None else a)
            n += 1
            ratio = abs(R) / r
            worst = max(worst, ratio)
            if ratio > 1:
                print("  BOUND VIOLATED at s=%s a=%s: |R|=%s > r=%s" % (s, a, mp.nstr(abs(R), 8), mp.nstr(r, 8)))
    print("  regime %-10s done (N,m for last point = %d,%d; last |R| = %s, r = %s, r/|R| = %s)"
          % (regime, N, m, mp.nstr(abs(R), 6), mp.nstr(r, 6), mp.nstr(r / abs(R) if R != 0 else mpf('inf'), 6)))
print("%d (s, a) points; worst |R|/r = %s (must be <= 1)" % (n, mp.nstr(worst, 8)))
sys.exit(0 if worst <= 1 else 1)
