# read-O: (i) products <= 400 and the truncated signed Euler product of L_{pi/16} (real values);
# (ii) the exact local Chebyshev identity sum_{n in I} log n dN_L = sum_beta Lambda_L(beta) N_L(I/beta) and (*) of NOTE 6.2
# at short windows around products of k = 2, 3, 4 atoms. Own code; mpmath 30 digits.
from mpmath import mp, mpf, pi, log, zeta, digamma, factorial as mfac
from math import factorial
from collections import Counter
mp.dps = 30
rho = pi/16
def ell(k): return 1 + (k - mpf(1)/2)/rho
X0 = mpf(9000)
KMAX = int(rho*(X0 - 1) + mpf(1)/2) + 1
L = [None] + [ell(k) for k in range(1, KMAX + 1)]
# enumerate all multisets (nondecreasing index tuples) with product <= X0
elems = []                                   # (value, tuple of indices)
def rec(start, val, idx):
    for k in range(start, KMAX + 1):
        v = val*L[k]
        if v > X0: break
        t = idx + (k,)
        elems.append((v, t)); rec(k, v, t)
rec(1, mpf(1), ())
elems.sort()
def cweight(t):                              # Pi_L weight = (-1)^{k+1}(k-1)!/prod e_i!
    c = Counter(t); k = len(t); den = 1
    for x in c.values(): den *= factorial(x)
    return mpf((-1)**(k+1)*factorial(k-1))/den
def mexp(t):                                 # Euler exponent via Moebius over j | gcd(e)
    from math import gcd
    from functools import reduce
    c = Counter(t); g = reduce(gcd, c.values())
    def mob(n):
        r, p = 1, 2
        while p*p <= n:
            if n % p == 0:
                n //= p
                if n % p == 0: return 0
                r = -r
            p += 1
        return -r if n > 1 else r
    tot = mpf(0)
    for j in range(1, g + 1):
        if g % j == 0 and mob(j) != 0:
            tj = tuple(sorted(sum([[i]*(e//j) for i, e in c.items()], [])))
            tot += mob(j)*cweight(tj)/j
    return tot
print("semigroup elements <= 9000:", len(elems), " atoms:", KMAX)
small = [(v, t) for v, t in elems if v <= 400]
cnt = Counter((len(t), tuple(sorted(Counter(t).values()))) for v, t in small)
print("elements <= 400 by (k, multiplicity pattern):", dict(cnt))
ms = Counter((len(t), tuple(sorted(Counter(t).values())), int(mexp(t))) for v, t in small)
print("  with Euler exponent m:", dict(ms))
# truncated product over lambda <= 400 vs L(s)
for s in (mpf(3), mpf('2.5')):
    prod = mpf(1)
    for v, t in small: prod *= (1 - v**(-s))**(-mexp(t))
    Ls = 1 + rho**s*zeta(s, mpf(1)/2 + rho)
    print(f"s={s}: truncated product = {mp.nstr(prod, 12)}  L = {mp.nstr(Ls, 12)}")
# (ii) local Chebyshev identity and (*) at windows around chosen products
atoms = [mpf(1)] + L[1:]
def NL(a, b):                                # number of atoms (incl. 1) in (a, b]
    return sum(1 for x in atoms if a < x <= b)
AL = 1 + rho*log(rho) - rho*digamma(mpf(1)/2 + rho)     # constant term of L at s = 1
print("A_L (constant term of L at 1) =", mp.nstr(AL, 12))
h = mpf(10)**-8
tests = {"l1 l2": (1, 2), "l1^2": (1, 1), "l1 l2 l3": (1, 2, 3), "l1^2 l2": (1, 1, 2), "l1^3": (1, 1, 1),
         "l1 l2 l3 l4": (1, 2, 3, 4), "l1^4": (1, 1, 1, 1), "l2 l5": (2, 5), "l1 l2 l7": (1, 2, 7)}
for nm, t in tests.items():
    lam = [v for v, tt in elems if tt == t][0]
    x = lam - h/2
    lhs_id = sum(log(a) for a in atoms if x < a <= x + h)
    rhs_id = sum(cweight(tt)*log(v)*NL(x/v, (x + h)/v) for v, tt in elems if v <= x + h)
    star_l = sum(cweight(tt)*log(v)*(NL(x/v, (x + h)/v) - rho*h/v) for v, tt in elems if v <= x)
    star_r = (NL(x, x + h) - rho*h)*log(x) + AL*h
    print(f"{nm:12s} lambda={mp.nstr(lam, 10):>12s} Pi_L={mp.nstr(cweight(t), 4):>5s}  identity: {mp.nstr(lhs_id, 5)} = {mp.nstr(rhs_id, 5)}"
          f"   (*) LHS-RHS = {mp.nstr(star_l - star_r, 8)}  (-Pi_L log lambda = {mp.nstr(-cweight(t)*log(lam), 8)})"
          f"  (*) {'FAILS' if star_l > star_r else 'holds'}")
