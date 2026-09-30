#!/usr/bin/env python3
"""read-F re-run (orchestrator, Fable 5.1, Session 38): Bernoulli thinning T_alpha by an INDEPENDENT route —
numpy sieve (not the NOTE's C code), numpy PCG64 RNG (not the NOTE's 64-bit hash), X = 1e7 (a lower rung than the
NOTE's 1e9/1e10), deleted primes to Y = 1e8 for rho_P with the mean tail E1((1-alpha) log Y). Reports the sup- and
RMS-slopes over [1e4, X] against alpha/2, 1/(3-alpha), 2 alpha/(alpha+2). Control: no deletion (slope 0)."""
import numpy as np, math, sys, time
from mpmath import e1
X = 10**7; Y = 10**8
t0 = time.time()
sieve = bytearray([1])*(Y+1); sieve[0] = sieve[1] = 0
for i in range(2, int(Y**0.5)+1):
    if sieve[i]: sieve[i*i::i] = bytearray(len(range(i*i, Y+1, i)))
primes = np.flatnonzero(np.frombuffer(bytes(sieve), dtype=np.uint8)).astype(np.int64)
print(f"primes <= {Y}: {len(primes)}  ({time.time()-t0:.1f}s)")
edges = np.unique(np.round(10**np.arange(4, 7.0001, 0.05)).astype(np.int64))
def slopes(E):
    a = np.abs(E)
    run = np.maximum.accumulate(a)
    sup = np.array([run[e-1] for e in edges])
    rms = np.array([math.sqrt(np.mean(a[int(e/10**0.05):e]**2)) for e in edges])  # rms over the bin below the edge
    L = np.log(edges.astype(float))
    ssup = np.polyfit(L, np.log(sup), 1)[0]; srms = np.polyfit(L[1:], np.log(rms[1:]), 1)[0]
    return ssup, srms, sup[-1]
print("== control: no deletion (E = N(x) - x = -{x}) ==")
x = np.arange(1, X+1, dtype=np.int64); E0 = np.floor(x) - x  # = 0 exactly at integers; sup over reals is <1: use half-integers
E0h = np.floor(x + 0.5) - (x + 0.5)  # = -0.5 at half-integers
print(f"  |E| at half-integers = {np.max(np.abs(E0h)):.3f} for all x: slope 0 by construction (N(x)=floor x)")
for alpha in (0.60, 0.75, 0.90):
    res = []
    for seed in (1, 2, 3):
        rng = np.random.default_rng(1000*seed + int(100*alpha))
        u = rng.random(len(primes))
        deleted = primes[u < primes.astype(float)**(alpha-1)]
        log_rho = float(np.sum(np.log1p(-1.0/deleted)))
        tail = float(e1((1-alpha)*math.log(Y)))
        rho = math.exp(log_rho - tail)
        free = np.ones(X+1, dtype=bool); free[0] = False
        for p in deleted[deleted <= X]:
            free[p::p] = False
        N = np.cumsum(free, dtype=np.int64)[1:]
        E = N - rho*x   # at integers; sup over reals of |N - rho x| is attained at integers or just before: take max(|E(n)|, |E(n)-rho|) ~ same exponent
        Em = np.maximum(np.abs(E), np.abs(E - rho))  # |N(n) - rho n| and |N(n-1) - rho n| = |E(n) - 1 + ... |; a bound-preserving proxy
        ssup, srms, supX = slopes(E)
        res.append((ssup, srms, supX))
        print(f"  alpha={alpha} seed={seed}: #deleted<=X {int((deleted<=X).sum())}, rho={rho:.6f}, sup|E|(X)={supX:.1f}, sup-slope={ssup:.3f}, rms-slope={srms:.3f}")
    ss = np.array([r[0] for r in res]); sr = np.array([r[1] for r in res])
    print(f"== alpha={alpha}: sup-slope {ss.mean():.3f} +- {ss.std(ddof=1)/math.sqrt(3):.3f}; rms-slope {sr.mean():.3f} +- {sr.std(ddof=1)/math.sqrt(3):.3f}"
          f"   | alpha/2={alpha/2:.3f}  1/(3-alpha)={1/(3-alpha):.3f}  2a/(a+2)={2*alpha/(alpha+2):.3f}   ({time.time()-t0:.0f}s)")
