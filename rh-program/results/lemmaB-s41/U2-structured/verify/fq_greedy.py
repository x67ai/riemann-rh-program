#!/usr/bin/env python3
"""Rung 1: the F_q greedy with a prescribed integer target T_n (exact integer arithmetic).

Given T_0 = 1 and integer targets T_n, the greedy sets b_n := T_n - C_n, where C_n is the number of
degree-n g-integers that are products of >= 2 g-primes of degree < n, i.e. the u^n coefficient of
prod_{d<n} (1-u^d)^{-b_d}. The system is EXACT (A_n = T_n for all n) iff every b_n >= 0.
Checks:
 (a) template family T_n = m q^{n-1}: b_n == M(q,n) - M(q-m,n) (necklace polynomials), all >= 0;
 (b) one-sided family T_n = m q^{n-1} + c (c >= 1): b_n vs closed form via a_n = q^n + 1 - w1^n - w2^n,
     positivity, real zero s* = log(w1)/log(q);
 (c) rounded family T_n = ceil(rho q^n) + c, rho irrational: positivity.
Usage: python3 fq_greedy.py > ../verify/logs/fq_greedy.log
"""
import math
from fractions import Fraction

def mobius(n):
    res, p, m = 1, 2, n
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0:
                return 0
            res = -res
        p += 1
    if m > 1:
        res = -res
    return res

def necklace(Q, n):
    s = sum(mobius(n // d) * Q ** d for d in range(1, n + 1) if n % d == 0)
    assert s % n == 0
    return s // n

def greedy(T, nmax):
    """Return (b, A) with b_n = T_n - C_n (may be negative: then the target is not exactly realizable;
    we record b_n as computed and CONTINUE with b_n clipped at 0, i.e. the true greedy)."""
    A = [0] * (nmax + 1)   # coefficients of prod_{d<=current} (1-u^d)^{-b_d}
    A[0] = 1
    b = [0] * (nmax + 1)
    raw = [0] * (nmax + 1)
    for n in range(1, nmax + 1):
        C = A[n]                       # contributions of degrees < n only
        raw[n] = T(n) - C
        bn = max(raw[n], 0)
        b[n] = bn
        if bn:
            # multiply by (1-u^n)^{-bn}: A_new[k] = sum_j binom(bn+j-1, j) A_old[k - j n]
            for k in range(nmax, n - 1, -1):
                s, j, coef = 0, 1, 1
                while k - j * n >= 0:
                    coef = coef * (bn + j - 1) // j
                    s += coef * A[k - j * n]
                    j += 1
                A[k] += s
    return raw, b, A

def check_template(q, m, nmax):
    raw, b, A = greedy(lambda n: m * q ** (n - 1), nmax)
    ok = all(raw[n] == necklace(q, n) - necklace(q - m, n) for n in range(1, nmax + 1))
    pos = all(raw[n] >= 0 for n in range(1, nmax + 1))
    exact = all(A[n] == m * q ** (n - 1) for n in range(1, nmax + 1))
    s_star = math.log(q - m) / math.log(q) if q - m > 1 else float('-inf')
    return ok, pos, exact, s_star

def check_onesided(q, m, c, nmax):
    raw, b, A = greedy(lambda n: m * q ** (n - 1) + c, nmax)
    S, P = q + 1 - m - c, q - m - c * q
    disc = S * S - 4 * P
    w1, w2 = (S + math.sqrt(disc)) / 2, (S - math.sqrt(disc)) / 2
    neg = [n for n in range(1, nmax + 1) if raw[n] < 0]
    # closed form check for small n (floating, a_n = q^n + 1 - w1^n - w2^n; n b_n = sum mu a_d)
    cf_ok = True
    for n in range(1, min(nmax, 25) + 1):
        an = lambda d: q ** d + 1 - w1 ** d - w2 ** d
        nb = sum(mobius(n // d) * an(d) for d in range(1, n + 1) if n % d == 0)
        if abs(nb / n - raw[n]) > 1e-6 * max(1.0, abs(raw[n])):
            cf_ok = False
    s_star = math.log(w1) / math.log(q)
    return neg, cf_ok, w1, w2, s_star

def check_rounded(q, rho, c, nmax):
    T = lambda n: math.ceil(Fraction(rho) * q ** n) + c if n >= 1 else 1
    raw, b, A = greedy(T, nmax)
    neg = [n for n in range(1, nmax + 1) if raw[n] < 0]
    return neg

if __name__ == '__main__':
    NMAX = 40
    print("# (a) template family T_n = m q^(n-1): b_n == M(q,n) - M(q-m,n), positivity, exactness, s* = log(q-m)/log q")
    for q in (2, 3, 4, 5, 7, 16):
        for m in range(1, q):
            ok, pos, exact, s = check_template(q, m, NMAX)
            print(f"q={q:2d} m={m:2d} rho=m/q={m/q:.4f}  necklace_identity={ok} all_b>=0={pos} A_n==T_n={exact}  s*={s:.6f}")
    print("\n# (b) one-sided family T_n = m q^(n-1) + c: first negative raw b_n (none = exact to n=40), closed form check, zero")
    for q in (5, 7, 11, 16, 32, 64, 101):
        for (m, c) in ((1, 1), (1, 2), (max(1, q // 8), 1), (max(1, q // 8), 3), (max(1, q // 4), 1), (max(1, q // 4), 5)):
            neg, cf, w1, w2, s = check_onesided(q, m, c, NMAX)
            r0 = min(1 - m / q, c)
            print(f"q={q:3d} m={m:3d} c={c}  rho={m/q:.4f} r0={r0:.4f}  negatives={neg[:5]}  closed_form_ok={cf}  w1={w1:.4f} w2={w2:.4f}  s*={s:.6f}")
    print("\n# (c) rounded family T_n = ceil(rho q^n) + c, rho = 1/pi, 1/e, sqrt(2)-1")
    for q in (5, 16, 64):
        for rho in (Fraction(1 / math.pi), Fraction(1 / math.e), Fraction(math.sqrt(2) - 1)):
            for c in (0, 1, 2):
                neg = check_rounded(q, rho, c, 30)
                print(f"q={q:3d} rho={float(rho):.6f} c={c}  negatives(n<=30)={neg[:6]}")
