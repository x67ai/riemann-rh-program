#!/usr/bin/env python3
"""ktest_O.py -- Opus reader (Session 41). Exact-integer and 60-digit checks of the K close of s5-multiplicity-s40.
Inputs: f = f_G(n_K) as counted by lattice_O.c (argv[1]); n_K from its factorization. No code shared with the unit."""
import sys
from decimal import Decimal, getcontext
from fractions import Fraction
getcontext().prec = 60

fac = {2: 8, 3: 5, 5: 9, 7: 3, 11: 2, 13: 1, 17: 1, 19: 3, 23: 1, 29: 2, 37: 1, 41: 2, 59: 1, 61: 1, 79: 1, 89: 1, 109: 1, 149: 1}
n = 1
for p, e in fac.items():
    n *= p ** e
f = int(sys.argv[1]) if len(sys.argv) > 1 else 3403961916617140
print('n_K =', n, ' digits:', len(str(n)))
print('f   =', f)
# K test: f - 3 > (94/25) n^(7/20)  <=>  (25(f-3))^20 > 94^20 n^7   (both sides positive integers)
lhs, rhs = (25 * (f - 3)) ** 20, 94 ** 20 * n ** 7
print('K test (25(f-3))^20 > 94^20 n^7 :', lhs > rhs)
# a stronger exact test: is a_n - 0.8 > 2 * 1.88 * n^0.35 ?  <=> (25(5f - 4))^20 > (5*94)^20 n^7 ... done via Decimal below
D = Decimal
ln_n, ln_f = D(n).ln(), D(f).ln()
r035 = (D(7) / D(20) * ln_n).exp()
print('log10 n = %s' % (ln_n / D(10).ln()))
print('log f / log n = %s' % (ln_f / ln_n))
print('f / (3.76 n^0.35) = %s' % (D(f) / (D('3.76') * r035)))
print('f / n^0.35 = %s' % (D(f) / r035))
print('(f - 0.8) / (2 n^0.35) [least constant c in |C(u)| <= c u^0.35 consistent with a_nK] = %s' % ((D(f) - D('0.8')) / (2 * r035)))
print('log10 f - log10(3.76 n^0.35) = %s' % ((ln_f - D('3.76').ln() - D(7) / D(20) * ln_n) / D(10).ln()))
# exponent theta below which even c = 1.88 fails at n_K: solve 2*1.88 n^theta = f - 0.8
th = ((D(f) - D('0.8')) / D('3.76')).ln() / ln_n
print('largest theta with 3.76 n_K^theta >= f - 0.8 : %s' % th)
# Rouche tolerance for Theorem K' (u-offsurgery-s39 NOTE §4): tail c*|s| X^(theta - sigma)/(sigma - theta) + |C(X)| X^-sigma
X = D(10) ** 9
th0 = D('0.35')
for (s, t) in [(D('0.7459'), D('30.346')), (D('0.7459'), D('30.306')), (D('0.7859'), D('30.346'))]:
    mods = (s * s + t * t).sqrt()
    integ = mods * (( th0 - s) * X.ln()).exp() / (s - th0)
    first8 = 8 * ((-s) * X.ln()).exp()
    print('sigma=%s t=%s : |s|X^(th-s)/(s-th) = %.6f ; 8 X^-s = %.3e' % (s, t, integ, first8))
print('0.0394 / 0.0210 = %.5f' % (0.0394 / 0.0210))
