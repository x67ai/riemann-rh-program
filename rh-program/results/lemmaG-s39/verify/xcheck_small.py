#!/usr/bin/env python3
"""xcheck_small.py — second route for lg.c at X = 1e5: (1) regenerate R in Python (sympy.nextprime / exact integer Weyl rule /
greedy) and compare with lg's R-list; (2) recompute every bin's sumE2 with N_P(n) = sum_{m in <R>, m<=n} mu(m) floor(n/m)
(inclusion-exclusion over squarefree R-numbers — a different route from lg's sieve bitset), using lg's rho; (3) rho by an
independent mpmath product (larger cutoff, same tail model) where cheap."""
import sys, math, subprocess
import mpmath as mp
from sympy import nextprime, primerange
mp.mp.dps = 30
X = 100000

def run_lg(args):
    out = subprocess.run(["./lg"] + args, capture_output=True, text=True).stdout.splitlines()
    head = [l for l in out if l.startswith("#")][0]
    rho = float(head.split(" rho=")[1].split()[0]); run = head.split("run=")[1].split()[0]
    bins = [l.split(",") for l in out if not l.startswith("#")]
    R = [int(l) for l in open("data/R_%s.txt" % run)]
    return run, rho, bins, R, head

def rnums(R, X):                        # squarefree R-numbers <= X with mu
    out = [(1, 1)]; Rs = sorted(R)
    def rec(i, b, mu):
        for j in range(i, len(Rs)):
            if b * Rs[j] > X: break
            out.append((b * Rs[j], -mu)); rec(j + 1, b * Rs[j], -mu)
    rec(0, 1, 1); return out

def check(args, Rpy, label):
    run, rho, bins, R, head = run_lg(args)
    okR = (sorted(R) == sorted(r for r in Rpy if r <= X))
    ms = rnums(R, X); worst = 0.0
    import numpy as np
    N = np.zeros(X + 1, dtype=np.int64)
    for m, mu in ms:                    # N(n) = sum mu(m) floor(n/m): accumulate via difference arrays per m
        n = np.arange(X + 1); N += mu * (n // m)
    N[0] = 0
    for b in bins:
        lo, hi, s2 = int(b[1]), int(b[2]), float(b[5])
        n = np.arange(lo, hi + 1); ec = N[lo:hi + 1] - rho * (n + 0.5)
        mine = float((ec * ec).sum()); worst = max(worst, abs(mine - s2) / max(1.0, abs(s2)))
    print("%-10s %s | R-lists equal: %s (%d primes <= X) | max rel. diff of bin sumE2 (sieve vs inclusion-exclusion): %.2e" % (label, run, okR, len(R), worst))
    return rho

# sq: R = {nextprime(p^2)}
Rsq = [nextprime(p * p) for p in primerange(2, 400)]
rho = check(["sq", "2", "1e5"], Rsq, "sq")
lr = mp.fsum(mp.log(1 - mp.mpf(1) / nextprime(p * p)) for p in primerange(2, 300000))
lt = mp.fsum(mp.log(1 - mp.mpf(p) ** -2) for p in primerange(300000, 3000000))
t2 = -mp.e1(mp.log(3000000))            # prod_{p>3e6}(1-1/p^2) ~ exp(-sum 1/p^2) ~ exp(-E1(ln P))
print("   rho(sq) lg = %.15f ; independent (P=3e5 exact, (3e5,3e6] p^2, tail E1) = %s" % (rho, mp.nstr(mp.e ** (lr + lt + t2), 16)))
# nsq: R = {nextprime(n^2)}
Rn = sorted(set(nextprime(n * n) for n in range(1, 320)))
rho = check(["nsq", "2", "1e5"], Rn, "nsq")
lr = mp.fsum(mp.log(1 - mp.mpf(1) / nextprime(n * n)) for n in range(1, 100001))
print("   rho(nsq) lg = %.15f ; independent (N1=1e5 exact, tail N1/(N1+1)) = %s" % (rho, mp.nstr(mp.e ** (lr + mp.log(mp.mpf(100000) / 100001)), 16)))
# weyl: exact integer rule u_p = p*T mod 2^64 < w_p 2^64
T = 0x6A09E667F3BCC908
Rw = [p for p in primerange(2, 400000) if (p * T) % 2 ** 64 < min(1.0, 1.0 * p ** (0.6 - 1)) * 2.0 ** 64]
check(["weyl", "0.6", "1", "1e5", "4e5"], Rw, "weyl")
# neck (tight): first M(2,N) primes after 4^N
def M(a, N):
    from sympy import mobius
    return sum(mobius(N // d) * a ** d for d in range(1, N + 1) if N % d == 0) // N
Rk = []
for Nn in range(1, 10):
    p = 4 ** Nn
    for _ in range(M(2, Nn)): p = nextprime(p); Rk.append(p)
check(["neck", "2", "1e5", "12"], Rk, "neck")
