#!/usr/bin/env python3
"""v2b -- seed M1a beurling-fe.  Re-examine the 'near-solutions' found by v2 (best per K, copied from v2_lsq_exotic_search.log).
Each system = {free primes found by v2} U {rational primes >= 12}.  Two exposures:
 (a) theta-relation defect at 60 digits on x in [1/8, 8] (rho = v2's fitted value, which is 1.000000 to 6 digits; we use rho = 1
     and ALSO the exact residue rho_true = prod over replaced primes, printed);
 (b) the Fejer sum S_F = sum_k sinc^2(n_k) over generalized integers <= 20000 (Theorem T: an exact solution has S_F = 0).
"""
import math
import mpmath as mp
mp.mp.dps = 60

near = {
    "K=3 {2,3,8.470247}": [2.0, 3.0, 8.470247],
    "K=4 {2,3,5.391211,9.447272}": [2.0, 3.0, 5.391211, 9.447272],
    "K=5 {2,3,6.044415,8.385313,10.877985}": [2.0, 3.0, 6.044415, 8.385313, 10.877985],
    "K=7 {2,3,5.560587,7.580187,9.110379,10.341306,10.5167}": [2.0, 3.0, 5.560587, 7.580187, 9.110379, 10.341306, 10.5167],
    "Z (control)": [2.0, 3.0, 5.0, 7.0, 11.0],
}

def rational_primes(lo, X):
    s = bytearray([1]) * (X + 1); s[0] = s[1] = 0
    for i in range(2, int(X ** 0.5) + 1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(lo, X + 1) if s[i]]

def gen(ps, X):
    ps = sorted(ps); out = [1.0]
    def rec(i0, v):
        for i in range(i0, len(ps)):
            w = v * ps[i]
            if w > X * (1 + 1e-12): break
            out.append(w); rec(i, w)
    rec(0, 1.0); out.sort(); return out

def sinc2(t):
    v = math.sin(math.pi * t) / (math.pi * t); return v * v

X = 20000
big = rational_primes(12, X)
for name, free in near.items():
    P = free + big
    # exact residue relative to zeta: rho = prod_{p<12 rational}(1-1/p) / prod_{free}(1-1/p)
    rho_true = 1.0
    for p in [2, 3, 5, 7, 11]: rho_true *= (1 - 1 / p)
    for p in free: rho_true /= (1 - 1 / p)
    N = gen(P, X)
    SF = sum(sinc2(n) for n in N[1:])
    Nsm = [mp.mpf(n) for n in N if n <= 80]
    psi = lambda x: mp.fsum(mp.e ** (-mp.pi * n * n * x) for n in Nsm)
    worst1 = max(abs((1 + 2 * psi(1 / x)) - mp.sqrt(x) * (1 + 2 * psi(x))) for x in [mp.mpf(2) ** k for k in range(-3, 4) if k != 0])
    worstT = max(abs((rho_true + 2 * psi(1 / x)) - mp.sqrt(x) * (rho_true + 2 * psi(x))) for x in [mp.mpf(2) ** k for k in range(-3, 4) if k != 0])
    first = [round(n, 4) for n in N[:12]]
    print(f"{name}\n   first integers {first}\n   rho_true = {rho_true:.6f}   max theta defect (rho=1) on x=2^-3..2^3: {mp.nstr(worst1, 3)}"
          f"   (rho=rho_true): {mp.nstr(worstT, 3)}\n   Fejer sum S_F = {SF:.4e}")
