#!/usr/bin/env python3
"""rung1_finite.py — lemmaG-s39, ladder rung 1 (finite R), a route independent of Franel/Parseval.
Claim (proved in NOTE §1.1): for finite R with period Q and a prime q not in R, E' = E_{R+q} satisfies
  E'(x) = E(x) - E(x/q),  <E, E(./q)>_{period Qq} = MS(R)/q,  hence MS(R+q) = 2(1 - 1/q) MS(R), MS(empty) = 1/12,
so MS(R) = rho * 2^|R| / 12.  Here everything is computed EXACTLY in rationals by integrating the piecewise-linear E
over one full period: on [n, n+1) E(x) = N(n) - rho x, so int_n^{n+1} E^2 = (N(n) - rho(n+1/2))^2 + rho^2/12.
The cross term int E(x)E(x/q) is computed on the common refinement of the unit grid and the q-grid (both piecewise linear)."""
from fractions import Fraction as F
from itertools import combinations
import sys

def rfree_counts(R, L):
    Q = 1
    for p in R: Q *= p
    ok = [1] * (L + 1); ok[0] = 0
    for p in R:
        for m in range(p, L + 1, p): ok[m] = 0
    N = [0] * (L + 1)
    for n in range(1, L + 1): N[n] = N[n - 1] + ok[n]
    return N

def rho_of(R):
    r = F(1)
    for p in R: r *= F(p - 1, p)
    return r

def ms_period(R):
    Q = 1
    for p in R: Q *= p
    N = rfree_counts(R, Q); rho = rho_of(R)
    s = F(0)
    for n in range(Q):
        c = N[n] - rho * (F(2 * n + 1, 2)); s += c * c + rho * rho / 12
    return s / Q

def Eval(N, rho, x):            # E(x) = N(floor x) - rho x, x a Fraction >= 0
    return N[x.numerator // x.denominator] - rho * x

def cross(R, q):
    """(1/(Qq)) int_0^{Qq} E(x) E(x/q) dx, exact: on each piece between consecutive points of the grid Z u qZ... E(x) is
    linear on [n, n+1) and E(x/q) is linear on [qm, q(m+1)); the product of two linear functions is integrated by Simpson (exact)."""
    Q = 1
    for p in R: Q *= p
    L = Q * q
    N = rfree_counts(R, L); rho = rho_of(R)
    tot = F(0)
    for n in range(L):              # the q-grid points are integers, so the unit grid refines both
        a, b = F(n), F(n + 1)
        m = F(2 * n + 1, 2)
        # left limits: use values at a, midpoint, and b^- (limit from the left inside the piece)
        fa, fm = Eval(N, rho, a), Eval(N, rho, m)
        fb = N[n] - rho * b            # E(b^-) on [n, n+1)
        ga = N[(n) // q] - rho * a / q
        gm = N[(n) // q] - rho * m / q
        gb = N[(n) // q] - rho * b / q  # x/q stays in [floor(n/q), ...) since n+1 <= q*(floor(n/q)+1)
        tot += (fa * ga + 4 * fm * gm + fb * gb) / 6
    return tot / L

log = []
sets = [(), (2,), (3,), (2, 3), (2, 5), (3, 5), (2, 3, 5), (3, 5, 7), (2, 3, 5, 7), (2, 5, 11), (3, 7, 11), (2, 3, 5, 7, 11)]
allok = True
for R in sets:
    ms = ms_period(R) if R else F(1, 12)
    pred = rho_of(R) * 2 ** len(R) / 12
    ok = (ms == pred); allok &= ok
    log.append("MS%s = %s  (%.12f)  rho*2^k/12 = %s  exact-equal=%s" % (list(R), ms, float(ms), pred, ok))
# the recursion's cross term <E_R, E_R(./q)> = MS(R)/q
for R, q in [((2,), 3), ((3,), 2), ((2, 3), 5), ((3, 5), 7), ((2, 5), 3), ((2, 3, 5), 7)]:
    c = cross(R, q); ms = ms_period(R)
    ok = (c == ms / q); allok &= ok
    log.append("cross<E_%s, E_%s(./%d)> = %s ; MS/q = %s ; exact-equal=%s" % (list(R), list(R), q, c, ms / q, ok))
log.append("ALL EXACT: %s" % allok)
print("\n".join(log))
