#!/usr/bin/env python3
"""Exact flat targets on free norm monoids of rank r: sign of the 'prime' coefficients.

Flat target on the free commutative monoid with r generators: T(h) = tau * w(h) for h != 1, T(1) = 1.
Its generating series is G = 1 - tau + tau * prod_{i<=r} (1 - x_i)^{-1}; exact realizability by a Beurling
system supported on the monoid requires the coefficients of F = log G (the prime-power measure) to be >= 0
(and, at multi-indices that are not proper powers, F_a = b_a must be a nonnegative integer multiple of w).
 (1) r = infinity, squarefree multi-indices (1,...,1) with k ones: F = kappa_k(tau)/... equals the k-th
     cumulant of Bernoulli(tau) (coefficient of t^k/k! in log(1 - tau + tau e^t)).
 (2) diagonal: D_r(x) = log(1 - tau + tau (1-x)^{-r}); sum_{|a|=n} F_a = [x^n] D_r.
 (3) full multivariate check for r = 2, 3 up to total degree DEG: first negative coefficient.
All arithmetic exact (Fraction). Usage: python3 rank_cumulants.py > logs/rank_cumulants.log
"""
from fractions import Fraction as Fr
from math import comb, factorial
import itertools, sys

def series_log(G, N):
    """1-D: log of a power series G (G[0] = 1) to order N, exact."""
    F = [Fr(0)] * (N + 1)
    for n in range(1, N + 1):
        s = G[n] * n
        for k in range(1, n):
            s -= k * F[k] * G[n - k]
        F[n] = s / n
    return F

def bernoulli_cumulants(tau, K):
    # log(1 - tau + tau e^t): G[n] = tau/n! for n >= 1
    G = [Fr(1)] + [tau / factorial(n) for n in range(1, K + 1)]
    F = series_log(G, K)
    return [F[k] * factorial(k) for k in range(K + 1)]

def diagonal(tau, r, N):
    # G = 1 - tau + tau (1-x)^{-r}: [x^n](1-x)^{-r} = C(n+r-1, r-1)
    G = [Fr(1)] + [tau * comb(n + r - 1, r - 1) for n in range(1, N + 1)]
    return series_log(G, N)

def multivariate_first_negative(tau, r, DEG):
    """Return (first multi-index with F_a < 0 in order of total degree, its value) or None, plus #checked."""
    idx = [a for n in range(DEG + 1) for a in itertools.product(range(n + 1), repeat=r) if sum(a) == n]
    G = {a: (Fr(1) if sum(a) == 0 else tau) for a in idx}
    F = {}
    for a in idx:
        n = sum(a)
        if n == 0:
            F[a] = Fr(0)
            continue
        s = n * G[a]
        # n G_a = sum_{0 != b <= a} |b| F_b G_{a-b}  =>  F_a = G_a - (1/n) sum_{0 != b < a} |b| F_b G_{a-b}
        for b in itertools.product(*[range(ai + 1) for ai in a]):
            nb = sum(b)
            if nb == 0 or b == a:
                continue
            s -= nb * F[b] * G[tuple(ai - bi for ai, bi in zip(a, b))]
        F[a] = s / n
    negs = [(sum(a), a, F[a]) for a in idx if F[a] < 0]
    negs.sort()
    return (negs[0] if negs else None), len(idx)

if __name__ == '__main__':
    taus = [Fr(1, 20), Fr(1, 10), Fr(1, 5), Fr(1, 4), Fr(1, 3), Fr(1, 2), Fr(2, 3), Fr(9, 10)]
    print("# (1) Bernoulli cumulants kappa_k(tau), k <= 40: first negative k and its value (relative to tau)")
    for tau in taus:
        kap = bernoulli_cumulants(tau, 40)
        neg = [k for k in range(1, 41) if kap[k] < 0]
        k0 = neg[0] if neg else None
        print(f"tau={str(tau):5s}  first k with kappa_k<0: {k0}  (#neg k<=40: {len(neg)})  "
              + (f"kappa_k0/tau={float(kap[k0]/tau):.4g}" if k0 else ""))
    print("\n# (2) diagonal log(1 - tau + tau (1-x)^{-r}): first n with [x^n] < 0, n <= 200")
    for r in (1, 2, 3, 4, 6):
        row = []
        for tau in taus:
            D = diagonal(tau, r, 200)
            neg = [n for n in range(1, 201) if D[n] < 0]
            row.append(f"{str(tau)}:{neg[0] if neg else '-'}")
        print(f"r={r}: " + "  ".join(row))
    print("\n# (3) full multivariate coefficients, first negative (total degree, multi-index, value)")
    for (r, DEG) in ((2, 40), (3, 18)):
        for tau in taus:
            first, cnt = multivariate_first_negative(tau, r, DEG)
            msg = (f"deg={first[0]} a={first[1]} F_a={float(first[2]):.4g}" if first else "none")
            print(f"r={r} DEG={DEG} tau={str(tau):5s} monomials={cnt}: {msg}")
            sys.stdout.flush()
