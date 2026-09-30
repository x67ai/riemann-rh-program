"""xin.py -- box enclosures of Haglund's Xi(z), Phi_n(z), Xi_N(z)  (arXiv:0910.5228 (1), (10), (12)-(14)).  Producer B.
  s = 1/2 + i z;  Xi(z) = (1/2) s (s-1) pi^{-s/2} Gamma(s/2) zeta(s)                       [Haglund (1)]
  Phi_n(z) = 2X^2 [h(s/2+2) + h((1-s)/2+2)] - 3X [h(s/2+1) + h((1-s)/2+1)],  X = pi n^2   [(14) with (10); CERT B1]
  Xi = sum_{n>=1} Phi_n  [(12)],  so  Xi_N = Xi - sum_{N<n<=M} Phi_n - T_M,   |T_M| <= 18 pi (M+1)^2 e^{-pi (M+1)^2}  [CERT B5]
"""
import time
from ivc import *
from specfun import zeta_em, lngamma, h_enclose

STATS = {'Xi': 0, 'Phi': 0, 'methods': {}}


def s_of(z):
    return C(R('0.5') - z.im, z.re)          # s = 1/2 + i z


def Xi(z, relbits):
    s = s_of(z)
    w = s * R('0.5')
    A = cexp(lngamma(w) - w * iv.log(iv.pi))  # pi^{-s/2} Gamma(s/2)
    zt, N, m, bnd = zeta_em(s, relbits)
    STATS['Xi'] += 1
    STATS['zeta'] = (N, m, mp.nstr(bnd, 3))
    return s * (s - 1) * R('0.5') * A * zt


def Phi(n, z, relbits):
    s = s_of(z)
    X = iv.pi * n * n
    half = R('0.5')
    ws = [s * half + 2, (1 - s) * half + 2, s * half + 1, (1 - s) * half + 1]
    hs = []
    for w in ws:
        h, meth = h_enclose(w, X, relbits)
        STATS['methods'][(n, meth)] = STATS['methods'].get((n, meth), 0) + 1
        hs.append(h)
    STATS['Phi'] += 1
    return (hs[0] + hs[1]) * (2 * X * X) - (hs[2] + hs[3]) * (3 * X)


def tail_bound(M, z):
    """upper bound for |sum_{n>M} Phi_n(z)| (CERT B5).  Needs pi (M+1)^2 >= max(2 beta, 12), M+1 >= 2,
    beta = max_i max(Re w_i - 1, 0) over the box."""
    s = s_of(z)
    half = R('0.5')
    ws = [s * half + 2, (1 - s) * half + 2, s * half + 1, (1 - s) * half + 1]
    beta = max(max(hi(w.re) - 1, 0) for w in ws)
    n0 = M + 1
    X0 = iv.pi * n0 * n0
    if not (n0 >= 2 and lo(X0) >= max(2 * beta, 12)):
        raise ValueError('tail_bound hypotheses fail')
    return hi(18 * X0 * iv.exp(-X0))


def choose_M(N, z):
    """smallest M >= N + 3 whose proved tail bound is <= 1e-80 (at N = 27 this is M = 30)."""
    M = N + 3
    while tail_bound(M, z) > mp.mpf('1e-80'):
        M += 1
    return M


def XiN_tail(N, z, relbits):
    """Xi_N(z) = Xi(z) - sum_{n=N+1}^{M} Phi_n(z) - T_M."""
    M = choose_M(N, z)
    STATS['M'] = M
    F = Xi(z, relbits)
    for n in range(N + 1, M + 1):
        F = F - Phi(n, z, relbits)
    return F.widen(tail_bound(M, z))


def XiN_lit(N, z, relbits):
    """the literal sum (13): sum_{n<=N} Phi_n(z).  Only sensible at small N (no cancellation control)."""
    F = C(0)
    for n in range(1, N + 1):
        F = F + Phi(n, z, relbits)
    return F


def point(x, y='0'):
    """the exact complex number x + i y given by decimal strings, as a (tiny) box."""
    return C(R(x), R(y))


def fmt(F, n=15):
    return F.nstr(n)
