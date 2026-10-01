# carriers.py -- C2 check: which rational primes are refused, and which g-primes carry them (read-O, Session 40)
import numpy as np, sys
from sympy import primerange, factorint
gp = np.fromfile('/private/tmp/rh-s40-u-offsurgery/r08_1e9.gp', dtype=np.dtype([('n','<u4'),('m','u1')]))
n = gp['n'].astype(np.int64); print('g-primes:', len(n), 'max m:', gp['m'].max())
S = set(n[n < 10**6].tolist())
acc = [p for p in primerange(2, 200) if p in S]; ref = [p for p in primerange(2, 200) if p not in S]
print('accepted primes < 200:', acc); print('refused primes < 200:', ref)
for p in [5, 19, 29, 41, 43, 47]:
    c = n[(n % p == 0) & (n != p)][:14]
    print(f'g-primes divisible by {p}:', [f'{x}={dict(factorint(int(x)))}' for x in c[:10]])
# smallest g-prime that is composite and built ONLY from accepted primes (no refused prime factor)
accS = set(p for p in primerange(2, 10**4) if p in S)
cnt = 0
for x in n[n < 10**6]:
    f = factorint(int(x))
    if len(f) > 1 or max(f.values()) > 1:
        if all(q in accS for q in f):
            print('composite g-prime with only accepted prime factors:', x, f); cnt += 1
            if cnt >= 5: break
print('none found below 1e6' if cnt == 0 else '')
