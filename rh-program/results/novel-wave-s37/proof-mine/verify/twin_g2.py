"""Seed M2: the one-sided caveat of the rung-1 twin test.
V (g = 1) is RH-false only through REAL reciprocal roots (t^2 > 4q forces real alpha), so every one-sided UPPER bound passes it.
Question: is there a genus-2 virtual curve over F_5 (integer L of degree 4 with FE, N_n >= 0, b_d >= 0, h >= 1) whose off-line
roots are NON-REAL? For such a V2, Bombieri's one-sided Theorem 1 ((5): N_r < Q + (2g+1)Q^(1/2) + 1, Q = 5^r, r even, Q > (g+1)^4)
should fail on V2 itself, with no twist. Exact integer Newton sums; numpy only for root magnitudes."""
import math, cmath
import numpy as np
from sympy import mobius
q, g = 5, 2
def newton(a1, a2, nmax):
    # reciprocal roots alpha_i are roots of T^4 + a1 T^3 + a2 T^2 + q a1 T + q^2 ; s_n = sum alpha_i^n (integers)
    c = [a1, a2, q * a1, q * q]; s = [4]
    for n in range(1, nmax + 1):
        v = -sum(c[j - 1] * s[n - j] for j in range(1, min(n, 4) + 1) if n - j >= 1) - (n * c[n - 1] if n <= 4 else 0)
        s.append(v)
    return s
found = []
for a1 in range(-20, 21):
    for a2 in range(-60, 61):
        # exact criterion: L's reciprocal-root polynomial = prod_i (T^2 - x_i T + q), x_1, x_2 roots of X^2 + a1 X + (a2 - 2q).
        # x_i non-real  <=>  a1^2 - 4(a2 - 2q) < 0  <=>  off-line NON-REAL roots (|alpha| = sqrt q would force x = alpha + conj(alpha) real)
        if a1 * a1 - 4 * (a2 - 2 * q) >= 0: continue
        roots = np.roots([1, a1, a2, q * a1, q * q])
        s = newton(a1, a2, 40)
        N = [None] + [q**n + 1 - s[n] for n in range(1, 41)]
        if min(N[1:]) < 0: continue
        b = [None]
        okb = True
        for d in range(1, 41):
            tot = sum(mobius(d // e) * N[e] for e in range(1, d + 1) if d % e == 0)
            if tot % d or tot < 0: okb = False; break
            b.append(tot // d)
        h = 1 + a1 + a2 + q * a1 + q * q
        if not okb or h < 1: continue
        found.append((max(abs(r) for r in roots), a1, a2, h, N[1:5], b[1:5], sorted(abs(r) for r in roots)))
found.sort()
print("genus-2 virtual curves over F_5 with non-real off-line roots, N_n >= 0 and b_d >= 0 (n, d <= 40), h >= 1: %d found in the box" % len(found))
for f in found[:3]:
    mx, a1, a2, h, N4, b4, mags = f
    print("  a1=%d a2=%d h=%d |alpha|=%s  Re s of zeros=%s  N_1..4=%s b_1..4=%s" % (
        a1, a2, h, [round(m, 4) for m in mags], [round(math.log(m) / math.log(q), 4) for m in mags], N4, b4))
if found:
    mx, a1, a2, h, N4, b4, mags = found[0]
    s = newton(a1, a2, 40)
    print("one-sided Bombieri (5) on the first one (no twist): Q = 5^r, r even, Q > (g+1)^4 = 81")
    for r in range(4, 41, 2):
        Q = q**r; Nr = Q + 1 - s[r]; bound = Q + (2 * g + 1) * math.sqrt(Q) + 1
        if Nr >= bound:
            print("  FIRST VIOLATION at r = %d: N_r - Q - 1 = %d > (2g+1) Q^(1/2) = %.1f" % (r, Nr - Q - 1, (2 * g + 1) * math.sqrt(Q))); break
    else:
        print("  no violation for even r <= 40")
