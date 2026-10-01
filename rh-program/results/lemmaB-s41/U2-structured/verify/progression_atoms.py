#!/usr/bin/env python3
"""Sanity check for NOTE Lemma 5.2: for t = 3..12 find primes p != q in one class g != 1 mod t (order m >= 2) and verify that
p^i q^(m-i) (0 <= i <= m) are atoms of the monoid {n = 1 mod t} and p^m q^m = (p^(m-1) q)(p q^(m-1)) are two factorizations.
Usage: python3 progression_atoms.py > logs/progression_atoms.log"""
from sympy import primerange, n_order, divisors
def is_atom(n, t):
    # n = 1 mod t is an atom iff no divisor d with 1 < d < n, d = 1 mod t, n/d = 1 mod t
    return all(not (d % t == 1 and (n // d) % t == 1) for d in divisors(n) if 1 < d < n)
for t in range(3, 13):
    found = None
    by_class = {}
    for p in primerange(2, 500):
        if t % p == 0 or p % t == 1:
            continue
        by_class.setdefault(p % t, []).append(p)
        if len(by_class[p % t]) == 2:
            found = (p % t, by_class[p % t]); break
    g, (p, q) = found
    m = n_order(g, t)
    elems = [p**i * q**(m - i) for i in range(m + 1)]
    ok_cls = all(e % t == 1 for e in elems)
    ok_atoms = all(is_atom(e, t) for e in elems)
    two = (p**m) * (q**m) == (p**(m - 1) * q) * (p * q**(m - 1))
    print(f"t={t:2d} class g={g} order m={m} p={p} q={q}  elements in G={ok_cls} all atoms={ok_atoms}  p^m q^m = (p^(m-1)q)(pq^(m-1)): {two}")
