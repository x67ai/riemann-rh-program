#!/usr/bin/env python3
"""NOTE Prop. 3.3: log #{partitions of k primes from (z,2z] into j-blocks} / log n -> 1 - 1/j  (n = product of those primes).
Usage: python3 partition_count.py > logs/partition_count.log"""
from math import lgamma, log
from sympy import primerange
for j in (2, 3, 5):
    for z in (10**3, 10**4, 10**5, 10**6, 10**7):
        ps = list(primerange(z + 1, 2 * z + 1))
        k = j * (len(ps) // j)
        logn = sum(log(p) for p in ps[:k])
        lcount = lgamma(k + 1) - (k / j) * lgamma(j + 1) - lgamma(k / j + 1)
        print(f"j={j} z=1e{len(str(z))-1} k={k:7d}  log#/log n = {lcount/logn:.4f}   (limit {1-1/j:.4f})")
