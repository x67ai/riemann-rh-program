#!/usr/bin/env python3
"""Same as rerun_thinning_numpy.py but with the deleted primes taken to Y = 1e9 (numpy sieve), so that the random tail of
rho_P (std ~ (Y^{alpha-2}/((2-alpha) log Y))^{1/2}, times x) is a few percent of the signal x^{alpha/2} at X = 1e7 for alpha = 0.9."""
import numpy as np, math, time
from mpmath import e1
X = 10**7; Y = 10**9; t0 = time.time()
s = np.ones(Y+1, dtype=bool); s[:2] = False
for i in range(2, int(Y**0.5)+1):
    if s[i]: s[i*i::i] = False
primes = np.flatnonzero(s).astype(np.int64); del s
print(f"primes <= {Y}: {len(primes)} ({time.time()-t0:.0f}s)", flush=True)
edges = np.unique(np.round(10**np.arange(4, 7.0001, 0.05)).astype(np.int64)); L = np.log(edges.astype(float))
x = np.arange(1, X+1, dtype=np.int64)
for alpha in (0.75, 0.90):
    ss=[]; sr=[]
    for seed in (1, 2, 3, 4):
        rng = np.random.default_rng(7000*seed + int(100*alpha)); u = rng.random(len(primes))
        deleted = primes[u < primes.astype(float)**(alpha-1)]
        rho = math.exp(float(np.sum(np.log1p(-1.0/deleted))) - float(e1((1-alpha)*math.log(Y))))
        free = np.ones(X+1, dtype=bool); free[0] = False
        for p in deleted[deleted <= X]: free[p::p] = False
        E = np.cumsum(free, dtype=np.int64)[1:] - rho*x; a = np.abs(E); run = np.maximum.accumulate(a)
        sup = np.array([run[e-1] for e in edges]); rms = np.array([math.sqrt(np.mean(a[int(e/10**0.05):e]**2)) for e in edges])
        s1 = np.polyfit(L, np.log(sup), 1)[0]; s2 = np.polyfit(L[1:], np.log(rms[1:]), 1)[0]; ss.append(s1); sr.append(s2)
        tailstd = math.sqrt(Y**(alpha-2)/((2-alpha)*math.log(Y)))*X
        print(f"  alpha={alpha} seed={seed}: rho={rho:.6f} (tail-std x X ~ {tailstd:.0f}), sup|E|(X)={sup[-1]:.1f}, sup-slope={s1:.3f}, rms-slope={s2:.3f}", flush=True)
    ss=np.array(ss); sr=np.array(sr)
    print(f"== alpha={alpha}: sup-slope {ss.mean():.3f} +- {ss.std(ddof=1)/2:.3f}; rms-slope {sr.mean():.3f} +- {sr.std(ddof=1)/2:.3f} | alpha/2={alpha/2:.3f} 1/(3-alpha)={1/(3-alpha):.3f} ({time.time()-t0:.0f}s)", flush=True)
