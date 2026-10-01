#!/usr/bin/env python3
"""read-O independent check of NOTE Thm R1 (rung-1 necklace deletion), written from the NOTE's definitions only.
Brute force: enumerate ALL monic polynomials over F_q (q prime) of degree <= nmax, find the irreducibles by trial
division, delete exactly M(a,N) irreducibles of each degree N under THREE different choice rules (first / last in
lex order / random), count R-free monic polynomials of each degree directly by trial division by the deleted set,
and compare with q^n - a q^(n-1).  Also checks M(a,N) <= M(q,N)."""
import random, sys, itertools

def mobius(n):
    m, p, res = n, 2, 1
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0: return 0
            res = -res
        p += 1
    return -res if m > 1 else res

def necklace(a, N):
    s = sum(mobius(N // d) * a ** d for d in range(1, N + 1) if N % d == 0)
    assert s % N == 0
    return s // N

def polys_monic(q, n):
    # coefficient tuples (c0..c_{n-1}, 1), low degree first
    for cs in itertools.product(range(q), repeat=n):
        yield tuple(cs) + (1,)

def divides(g, f, q):
    # does monic g divide f over F_q?  polynomial long division
    f = list(f); dg = len(g) - 1
    for i in range(len(f) - 1, dg - 1, -1):
        c = f[i] % q
        if c:
            for j in range(dg + 1):
                f[i - dg + j] = (f[i - dg + j] - c * g[j]) % q
    return all(x % q == 0 for x in f[:dg])

def run(q, a, nmax, rule, seed=1):
    irr = {}            # degree -> list of monic irreducibles (lex order of coefficient tuples)
    for N in range(1, nmax + 1):
        lst = []
        for f in polys_monic(q, N):
            if all(not divides(g, f, q) for d in range(1, N // 2 + 1) for g in irr[d]):
                lst.append(f)
        irr[N] = lst
    rng = random.Random(seed)
    R = []
    out = []
    for N in range(1, nmax + 1):
        m_a, m_q = necklace(a, N), necklace(q, N)
        assert len(irr[N]) == m_q, (N, len(irr[N]), m_q)
        assert m_a <= m_q
        if rule == 'first': pick = irr[N][:m_a]
        elif rule == 'last': pick = irr[N][-m_a:] if m_a else []
        else: pick = rng.sample(irr[N], m_a)
        R.extend(pick)
        out.append((N, m_q, m_a))
    counts = []
    for n in range(0, nmax + 1):
        c = 0
        for f in polys_monic(q, n):
            if all(not divides(g, f, q) for g in R if len(g) - 1 <= n):
                c += 1
        counts.append(c)
    return out, counts

if __name__ == '__main__':
    cases = [(3, 2, 8), (5, 2, 5), (5, 3, 5), (5, 4, 5), (7, 3, 4)]
    allok = True
    for q, a, nmax in cases:
        for rule in ('first', 'last', 'random'):
            out, counts = run(q, a, nmax, rule, seed=20261001)
            pred = [1] + [q ** n - a * q ** (n - 1) for n in range(1, nmax + 1)]
            ok = counts == pred
            allok &= ok
            print(f"q={q} a={a} rule={rule:6s} deg<= {nmax}: #irr/deleted per degree {[(N, mq, ma) for N, mq, ma in out]}")
            print(f"   N_P(n) brute = {counts}")
            print(f"   q^n-a q^(n-1) = {pred}   {'EQUAL' if ok else 'MISMATCH'}")
    print("ALL EQUAL" if allok else "SOME MISMATCH")
