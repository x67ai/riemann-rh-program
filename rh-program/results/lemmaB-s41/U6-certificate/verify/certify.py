#!/usr/bin/env python3
"""Certificates from one moment file: sigma_1 (largest 12-decimal sigma with F_X(sigma) > 0 PROVED, arb),
the bracket of the zero of F_X, and sigma_2 (smallest 9-decimal sigma with F_X(sigma) + tail(sigma) < 0 PROVED)
for each stated tail hypothesis. Usage: certify.py <file.mom> <16|32> <lo> <hi>   (lo, hi: decimal strings)"""
import sys
from fractions import Fraction as Fr
from flint import arb, fmpq
from feval import Moments, tail_log2, tail_pow, tail_ms

def q(fr):
    return fmpq(fr.numerator, fr.denominator)

def sign(ball):
    if ball > 0: return 1
    if ball < 0: return -1
    return 0

def largest_pos(g, lo, hi, digits):
    """largest d-decimal sigma in [lo, hi) with g(sigma) > 0 proved, given g(lo) > 0 proved, g(hi) < 0 proved."""
    assert sign(g(q(lo))) == 1 and sign(g(q(hi))) == -1, "bad initial bracket"
    step = Fr(1, 10**digits)
    a, b = lo, hi       # invariant: g(a) > 0 proved; g(b) not proved > 0
    while b - a > step:
        m = Fr(round((a + b) / 2 / step)) * step
        if m <= a or m >= b:
            break
        if sign(g(q(m))) == 1: a = m
        else: b = m
    return a, b

def smallest_neg(g, lo, hi, digits):
    """smallest d-decimal sigma in (lo, hi] with g(sigma) < 0 proved, given g(hi) < 0 proved."""
    for h in (hi, Fr("0.9"), Fr("0.95"), Fr("0.99")):
        if h >= hi and sign(g(q(h))) == -1:
            hi = h; break
    else:
        raise AssertionError("upper end not negative")
    step = Fr(1, 10**digits)
    a, b = lo, hi       # invariant: g(b) < 0 proved; g(a) not proved < 0
    while b - a > step:
        m = Fr(round((a + b) / 2 / step)) * step
        if m <= a or m >= b:
            break
        if sign(g(q(m))) == -1: b = m
        else: a = m
    return b

if __name__ == "__main__":
    path, den = sys.argv[1], int(sys.argv[2])
    lo, hi = Fr(sys.argv[3]), Fr(sys.argv[4])
    mo = Moments(path, den)
    print("#", mo.head)
    print(f"# X = x_K = {mo.X.str(20)}, K = {mo.K}, N(X) = {mo.N}, pi(X) = {mo.pi}, E(X) = {mo.eK}.5")
    F = mo.F
    s1, s1b = largest_pos(F, lo, hi, 12)
    f1 = F(q(s1)); f1b = F(q(s1b))
    print(f"SIGMA1 {float(s1):.12f}  F_X(sigma1) = {f1.str(6, radius=True)}  (proved > 0)")
    print(f"ZERO_OF_F_X in ({float(s1):.12f}, {float(s1b):.12f}): F_X(right end) = {f1b.str(6, radius=True)}"
          f"  proved < 0: {sign(f1b) == -1}")
    for K in ("0.1", "1", "10", "100"):
        g = lambda s, K=K: F(s) + tail_log2(s, mo.X, arb(K))
        s2 = smallest_neg(g, s1, hi, 9)
        print(f"SIGMA2 hyp E(u) <= {K} log^2 u (u >= X): sigma2 = {float(s2):.9f}  F+tail = {g(q(s2)).str(5, radius=True)}")
    th = s1 / 2
    th9 = Fr(int(th * 10**9), 10**9)      # 9-decimal truncation of sigma1/2, just below sigma1/2
    for C in ("1", "100"):
        g = lambda s, C=C: F(s) + tail_pow(s, mo.X, q(th9), arb(C))
        s2 = smallest_neg(g, s1, hi, 9)
        print(f"SIGMA2 hyp E(u) <= {C} u^{float(th9):.9f} (u >= X): sigma2 = {float(s2):.9f}  F+tail = {g(q(s2)).str(5, radius=True)}")
    g = lambda s: F(s) + tail_ms(s, mo.X, q(th9), arb(1))
    s2 = smallest_neg(g, s1, hi, 9)
    print(f"SIGMA2 hyp int_Y^2Y E^2 <= Y^(1+2*{float(th9):.9f}) (Y >= X): sigma2 = {float(s2):.9f}  F+tail = {g(q(s2)).str(5, radius=True)}")
