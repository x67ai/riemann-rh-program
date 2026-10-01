# check_psi_sieve.py -- independent check of the control's psi(x) - x at x = 1e7, 1e8 (numpy sieve, math.fsum)
import numpy as np, math
X = 10**8
s = np.ones(X + 1, dtype=bool); s[:2] = False
for p in range(2, int(X**0.5) + 1):
    if s[p]: s[p*p::p] = False
P = np.nonzero(s)[0]
for x in (10**7, 10**8):
    ps = P[P <= x]
    terms = [float(v) for v in np.log(ps.astype(np.float64))]
    for p in ps[ps * ps <= x]:
        k, q = 2, int(p) * int(p)
        while q <= x: terms.append(math.log(p)); q *= int(p)
    print(f"x = {x:.0e}: pi = {len(ps)}, psi - x = {math.fsum(terms) - x:.3f}")
