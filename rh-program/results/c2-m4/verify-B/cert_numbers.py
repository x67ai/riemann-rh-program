#!/usr/bin/env python3
"""cert_numbers.py -- the rationals of the Unit B certificate (Piece 8, n = 16 cells per half, and 1(b)), computed with
exact rational arithmetic (fractions) plus mpmath for the reference values.  Run from results/c2-m4/verify-B/.
(1) rational enclosures: e (exp_one_gt_d9 / lt_d9), c_B = 2/sqrt(72 e) = 1/sqrt(18 e), sqrt 73;
(2) the 16-cell Z enclosure: x_i = 256/(256 - i^2) at v_i = i/32; upper cell bound exp(-x) <= 1/sum_{k<8} x^k/k!;
    lower cell bound exp(-x) >= 1/(sum_{m<8} y^m/m! + y^8 * 9/(8! * 8))^q with y = x/q <= 1, q = ceil(x);
    Z_lo = (2/32) sum_{i=1}^{16} lo_i, Z_hi = (2/32) sum_{i=0}^{15} hi_i (Braw antitone on [0, 1/2], Braw(1/2) = 0);
(3) F13(50) at the endpoints: C_B <= e_hi^2/Z_lo, b1sym >= (2/(e_hi Z_hi))^2, c_B in [c_lo, c_hi], sqrt 73 in [r_lo, r_hi];
    the exp lower bound exp(E_lo) >= e_lo^40 * sum_{i<6} (E_lo - 40)^i/i!."""
from fractions import Fraction as Fr
from math import factorial, ceil
import mpmath as mp
mp.mp.dps = 40
e_lo, e_hi = Fr("2.7182818283"), Fr("2.7182818286")
# c_B = 1/sqrt(18 e): c_lo^2 * 18 * e_hi <= 1 and c_hi^2 * 18 * e_lo >= 1
cB = 1 / mp.sqrt(18 * mp.e)
c_lo = Fr(str(mp.nstr(cB, 11, strip_zeros=False))) - Fr(1, 10**10)
c_hi = Fr(str(mp.nstr(cB, 11, strip_zeros=False))) + Fr(1, 10**10)
assert c_lo**2 * 18 * e_hi <= 1 and c_hi**2 * 18 * e_lo >= 1, "c_B enclosure"
r73 = mp.sqrt(73)
r_lo = Fr(str(mp.nstr(r73, 12, strip_zeros=False))) - Fr(1, 10**10)
r_hi = Fr(str(mp.nstr(r73, 12, strip_zeros=False))) + Fr(1, 10**10)
assert r_lo**2 <= 73 <= r_hi**2, "sqrt 73 enclosure"
print(f"(1) e in [{e_lo}, {e_hi}];  c_B = {mp.nstr(cB, 14)} in [{c_lo}, {c_hi}];  sqrt 73 = {mp.nstr(r73, 14)} in [{r_lo}, {r_hi}]")
# (2) the 16 cells
def hi_bound(x, n=8):   # exp(-x) <= 1/sum_{k<n} x^k/k!
    return 1 / sum(x**k / factorial(k) for k in range(n))
def lo_bound(x, n=8):   # exp(-x) >= 1/(sum_{m<n} y^m/m! + y^n (n+1)/(n! n))^q
    q = max(1, ceil(x)); y = x / q
    assert 0 <= y <= 1
    return 1 / (sum(y**m / factorial(m) for m in range(n)) + y**n * (n + 1) / (factorial(n) * n))**q
cells = []
for i in range(0, 17):
    v = Fr(i, 32)
    if i == 16:
        lo = hi = Fr(0); x = None
    else:
        x = 1 / (1 - 4 * v * v); lo = lo_bound(x); hi = hi_bound(x)
        assert mp.mpf(lo.numerator)/lo.denominator <= mp.exp(-mp.mpf(x.numerator)/x.denominator) <= mp.mpf(hi.numerator)/hi.denominator
    cells.append((i, x, lo, hi))
Z_lo = Fr(2, 32) * sum(c[2] for c in cells if c[0] >= 1)
Z_hi = Fr(2, 32) * sum(c[3] for c in cells if c[0] <= 15)
Zref = mp.quad(lambda v: mp.exp(-1 / (1 - 4 * v * v)), [-mp.mpf(1) / 2, mp.mpf(1) / 2])
print("(2) cells i, x_i = 256/(256 - i^2), lo_i <= exp(-x_i) <= hi_i:")
for i, x, lo, hi in cells:
    print(f"    i = {i:2d}  x = {x}  q = {max(1, ceil(x)) if x is not None else '-'}  lo = {float(lo):.10f}  hi = {float(hi):.10f}  exp(-x) = {mp.nstr(mp.exp(-mp.mpf(x.numerator)/x.denominator), 10) if x is not None else 0}")
print(f"    Z_lo = {Z_lo} = {float(Z_lo):.12f};  Z (quadrature) = {mp.nstr(Zref, 14)};  Z_hi = {Z_hi} = {float(Z_hi):.12f};  Z_lo <= Z <= Z_hi: {mp.mpf(Z_lo.numerator)/Z_lo.denominator <= Zref <= mp.mpf(Z_hi.numerator)/Z_hi.denominator}")
print(f"    relative width: Z_lo/Z - 1 = {float(mp.mpf(Z_lo.numerator)/Z_lo.denominator / Zref - 1):+.5f}, Z_hi/Z - 1 = {float(mp.mpf(Z_hi.numerator)/Z_hi.denominator / Zref - 1):+.5f}")
Z_lo_dec = Fr(str(mp.nstr(mp.mpf(Z_lo.numerator) / Z_lo.denominator, 6, strip_zeros=False))) - Fr(1, 10**6)
Z_hi_dec = Fr(str(mp.nstr(mp.mpf(Z_hi.numerator) / Z_hi.denominator, 6, strip_zeros=False))) + Fr(1, 10**6)
assert Z_lo_dec <= Z_lo and Z_hi <= Z_hi_dec
print(f"    decimal enclosure stated in Lean: {Z_lo_dec} <= Z <= {Z_hi_dec}")
# (3) F13(50) at the endpoints (exact rationals)
def gammaPoly(n, a, s): return sum(Fr(factorial(n), factorial(j)) * s**j / a**(n + 1 - j) for j in range(n + 1))
def PrelaxQ(m, L, cb_hi, cb_lo, CB2, r):
    s = r * L; a = 2 * cb_lo
    return (1 + Fr(3, 2 * (73 * 50 - 1)))**m * CB2 * ((73 * L)**m * (1 + cb_hi / 2 * s)**2 +
        Fr(2) / L**(m + 1) * (gammaPoly(2 * m + 1, a, s) + cb_hi * gammaPoly(2 * m + 2, a, s) + cb_hi**2 / 4 * gammaPoly(2 * m + 3, a, s)))
CB2_hi = (e_hi**2 / Z_lo_dec)**2
b1_lo = (2 / (e_hi * Z_hi_dec))**2
Q_hi = Fr(105, 100) * PrelaxQ(2, 50, c_hi, c_lo, CB2_hi, r_hi) + PrelaxQ(3, 50, c_hi, c_lo, CB2_hi, r_hi)
E_lo = 50 * 2 * c_lo * r_lo - Fr(13, 8) * 50 - 2 * c_hi / r_lo
exp_lo = e_lo**40 * sum((E_lo - 40)**i / factorial(i) for i in range(6))
lhs = Q_hi / b1_lo
print(f"(3) E_lo = {float(E_lo):.9f} (E - 40 = {float(E_lo - 40):.6f} >= 0);  exp lower bound e_lo^40 * S_6 = {mp.nstr(mp.mpf(exp_lo.numerator) / exp_lo.denominator, 12)};  exp(E_lo) = {mp.nstr(mp.exp(mp.mpf(E_lo.numerator) / E_lo.denominator), 12)}")
print(f"    Q_hi/b1_lo = {mp.nstr(mp.mpf(lhs.numerator) / lhs.denominator, 12)};  log(Q_hi/b1_lo) - E_lo = {mp.nstr(mp.log(mp.mpf(lhs.numerator) / lhs.denominator) - mp.mpf(E_lo.numerator) / E_lo.denominator, 6)} (F13(50) at the endpoints; must be < 0)")
print(f"    the certificate inequality Q_hi/b1_lo <= exp_lo holds: {lhs <= exp_lo};  margin in nats: {mp.nstr(mp.log(mp.mpf(exp_lo.numerator) / exp_lo.denominator) - mp.log(mp.mpf(lhs.numerator) / lhs.denominator), 6)}")
print(f"    digits: numerator of Q_hi/b1_lo has {len(str(lhs.numerator))} digits, of exp_lo {len(str(exp_lo.numerator))} digits")
