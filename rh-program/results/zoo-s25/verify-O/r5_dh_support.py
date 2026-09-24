# Reader check (Opus 5): the DH coefficient-support theorem on [2, e^10], exactly in Z[kappa] (kappa^4 = -2k^3 + 6k^2 + 2k - 1).
# Lambda_DH(n) is carried as {prime p: element of Z[kappa]} meaning sum_p c_p log p (logs of distinct primes are
# Q-independent, so an element vanishes iff every c_p = 0).
import math
from mpmath import mp, sqrt, mpf, log
mp.dps = 40
N = 22026  # floor(e^10)
kap = (sqrt(10 - 2*sqrt(5)) - 2)/(sqrt(5) - 1)
print('kappa =', kap, ' quartic residual =', kap**4 + 2*kap**3 - 6*kap**2 - 2*kap + 1)
def mul(a, b):
    c = [0]*7
    for i in range(4):
        for j in range(4):
            c[i+j] += a[i]*b[j]
    for d in (6, 5, 4):  # k^4 = -2k^3 + 6k^2 + 2k - 1
        x = c[d]; c[d] = 0
        c[d-1] += -2*x; c[d-2] += 6*x; c[d-3] += 2*x; c[d-4] += -x
    return c[:4]
A = {0: [0,0,0,0], 1: [1,0,0,0], 2: [0,1,0,0], 3: [0,-1,0,0], 4: [-1,0,0,0]}
a = lambda n: A[n % 5]
spf = list(range(N+1))
for i in range(2, int(N**0.5)+1):
    if spf[i] == i:
        for j in range(i*i, N+1, i):
            if spf[j] == j: spf[j] = i
def factor(n):
    f = {}
    while n > 1:
        p = spf[n]; f[p] = f.get(p, 0) + 1; n //= p
    return f
divs = [[] for _ in range(N+1)]
for d in range(2, N+1):
    for m in range(d, N+1, d):
        divs[m].append(d)
Lam = [None]*(N+1)
for n in range(2, N+1):
    fac = factor(n)
    acc = {p: [e*x for x in a(n)] for p, e in fac.items()}          # a(n) log n
    for d in divs[n]:
        if d == n: continue
        ad = a(n//d)
        if ad == [0,0,0,0]: continue
        for p, c in Lam[d].items():
            pr = mul(ad, c)
            v = acc.setdefault(p, [0,0,0,0])
            for i in range(4): v[i] -= pr[i]
    Lam[n] = {p: v for p, v in acc.items() if any(v)}
def residue_class(p): return p % 5 in (1, 4)
nonzero = [n for n in range(2, N+1) if Lam[n]]
S_pp = [n for n in range(2, N+1) if len(factor(n)) == 1 and residue_class(next(iter(factor(n))))]
T = [n for n in range(2, N+1) if n % 5 and all(p % 5 in (2, 3) for p in factor(n))]
S = set(S_pp) | set(T)
print('nonzero count', len(nonzero), '= |S|', len(S), '(prime powers', len(S_pp), '+ T', len(T), ')  support == S:', set(nonzero) == S)
print('zeros coprime to 5:', sum(1 for n in range(2, N+1) if n % 5 and not Lam[n]))
ev = lambda c: sum(mpf(v[0]) + v[1]*kap + v[2]*kap**2 + v[3]*kap**3 and (mpf(v[0]) + v[1]*kap + v[2]*kap**2 + v[3]*kap**3)*log(p) for p, v in c.items())
print('Lambda_DH(6) =', ev(Lam[6]), ' Lambda_DH(12) =', ev(Lam[12]))
print('Lambda_DH(2^13) =', ev(Lam[2**13]), ' closed form', (-1)**12*kap**13*log(2))
print('min |Lambda_DH| on S:', min(abs(ev(Lam[n])) for n in S))
