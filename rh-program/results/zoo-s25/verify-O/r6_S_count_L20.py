# Reader check (Opus 5): |S ∩ [2, e^20]|, S = {p^k : p ≡ ±1 (5)} ∪ T, T = {n ≥ 2 : every prime factor ≡ ±2 (5)}.
# A sieve that knows nothing about Lambda_DH (the count the I.1 rider prints as 120 953 877 = 12 807 696 + 108 146 181).
import numpy as np, math
X = int(math.floor(math.exp(20)))
print('X = floor(e^20) =', X)
isp = np.ones(X + 1, dtype=bool); isp[:2] = False
for i in range(2, int(X**0.5) + 1):
    if isp[i]: isp[i*i::i] = False
primes = np.nonzero(isp)[0]; del isp
pm = primes[(primes % 5 == 1) | (primes % 5 == 4)]
# prime powers p^k <= X with p ≡ ±1 (5)
pp = len(pm) + sum(int(math.floor(math.log(X) / math.log(int(p)) + 1e-12)) - 1 for p in pm[pm <= int(X**0.5)])
# fix floor-log edge cases exactly
pp = 0
for p in pm.tolist():
    q = p
    while q <= X:
        pp += 1; q *= p
bad = np.zeros(X + 1, dtype=bool); bad[:2] = True
bad[0::5] = True
for p in pm.tolist():
    bad[p::p] = True
T = int(X + 1 - np.count_nonzero(bad))
print('prime powers p^k, p ≡ ±1 (5):', pp, '  |T|:', T, '  |S| =', pp + T)
