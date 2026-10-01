"""analyze_x.py -- is the prime-side fluctuation of S7 coherent or walk-like?  Reads the s7gen x-dump (uint32 pairs (n, m) for
every prime power whose decision differs from the default: m != 1 at primes, m != 0 at higher powers).
T(x) = sum_{p<=x} (m_p - 1) log p  (the prime-level part of psi_P - psi), and the walk scale V(x) = sqrt(sum_{p<=x} (m_p-1)^2 log^2 p)
(the size T would have if the m_p - 1 were independent with these values).  Prints T, V, sup|T| at checkpoints, the ratio sup|T|/V,
and the higher-prime-power decisions.  Usage: python3 analyze_x.py x.u32 X"""
import sys, math, numpy as np
fx, X = sys.argv[1], int(sys.argv[2])
d = np.fromfile(fx, dtype=np.uint32).reshape(-1, 2).astype(np.int64); n, m = d[:, 0], d[:, 1]
r = int(math.isqrt(X)); sv = np.ones(r + 1, bool); sv[:2] = False
for i in range(2, int(r**0.5) + 1):
    if sv[i]: sv[i*i::i] = False
pp = set()
for p in np.nonzero(sv)[0]:
    q = int(p) * int(p)
    while q <= X: pp.add(q); q *= int(p)
hi = np.isin(n, np.array(sorted(pp), dtype=np.int64)); P, M = n[~hi], m[~hi]
print("# %s X=%d: non-default prime decisions %d (refused m=0: %d; m>=2: %d), higher prime powers with m>0: %d"
      % (fx.split('/')[-1], X, len(P), int((M == 0).sum()), int((M >= 2).sum()), int(hi.sum())))
L = np.log(P.astype(float)); step = (M - 1) * L; T = np.cumsum(step); V2 = np.cumsum(step**2); aT = np.maximum.accumulate(np.abs(T))
print("# x  T(x)  V(x)  sup_{y<=x}|T(y)|  sup|T|/V")
for k in np.arange(4.0, math.log10(X) + 0.01, 0.5):
    i = np.searchsorted(P, 10**k, side='right') - 1
    if i < 0: continue
    print("%.3g %.6g %.6g %.6g %.2f" % (10**k, T[i], math.sqrt(V2[i]), aT[i], aT[i] / math.sqrt(V2[i])))
print("# higher prime powers with m>0 (first 30): n m ->", " ".join("%d:%d" % (a, b) for a, b in zip(n[hi][:30], m[hi][:30])))
