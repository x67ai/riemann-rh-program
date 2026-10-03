"""L-lit, task 3: two checks of the formulas that differ between arXiv:0910.5228v1 and the
author's web copy (rh8.pdf). (1) the z^-4 coefficient of eq. (47); (2) the constants of eq. (52)
from eq. (51). Run: python3 check_task3.py  (needs sympy, mpmath)."""
import sympy as sp, mpmath as mp
a, b, z, u = sp.symbols('a b z u', positive=True)
def T(w, K=8):                      # sum_{k>=0} a^k / (w (w+1)_k), truncated: exact through w^-(K+1)
    s, term = 0, 1/w
    for k in range(K):
        s += term; term = term*a/(w+k+1)
    return s
lhs = -sp.exp(-a)*(T(b+sp.I*z) + T(b-sp.I*z))           # left side of (47) as printed in both copies
e = sp.expand(sp.series(sp.simplify(lhs.subs(z, 1/u)), u, 0, 6).removeO())
c2, c4 = sp.simplify(e.coeff(u, 2)*sp.exp(a)), sp.expand(sp.simplify(e.coeff(u, 4)*sp.exp(a)))
web = 2*((b-a)**3 + 3*a**2 - 3*a*b - a)
v1 = 2*(b**3 - 2*a*b**2 - a*b + 3*a**2*b + 3*a**2 - a**3)
print("z^-2 coefficient * e^a :", sp.factor(c2), "(both copies: 2(a-b))")
print("z^-4 coefficient * e^a :", sp.factor(c4))
print("  equals web copy :", sp.expand(c4 - web) == 0, "| equals v1 :", sp.expand(c4 - v1) == 0)
mp.mp.dps = 120   # the partial sums cancel to ~1e-60 by n = 7
tot = mp.mpf(0)
for n in range(1, 8):
    c = (4*n**4*mp.pi**2*(n**2*mp.pi - mp.mpf(9)/4) - 6*n**2*mp.pi*(n**2*mp.pi - mp.mpf(5)/4))/mp.exp(n**2*mp.pi)
    tot += c
    print("n=%d coef of 1/x^2 in Phi_n: %s   partial sum: %s" % (n, mp.nstr(c, 15), mp.nstr(tot, 6)))
print("printed v1 : -.01974938206, .01974934121, .4132639753e-7")
print("printed web: -.0197493826339, .0197493413075, .4132639781905e-7")
