# Opus reader: Lemma Z4 on small instances, and the LP optimum of kappa over supports in div(M).
# Object: c: finite support, sum c_k/k = 0; F_x = prod_k (floor(x/k)!)^{c_k}; g(t) = sum_k c_k floor(t/k) (period L = lcm supp).
# If g >= 0 everywhere and g >= 1 on [1, T): psi(x) <= kappa x + O(log^2 x), kappa = A T/(T-1), A = -sum c_k log k / k.
import math
from fractions import Fraction as Fr
from scipy.optimize import linprog
from sympy import divisors, primerange

def g_vals(c, L):  return [sum(ck * (m // k) for k, ck in c.items()) for m in range(L)]
def kappa(c):
    assert sum(Fr(ck, k) for k, ck in c.items()) == 0
    L = math.lcm(*c.keys()); g = g_vals(c, L)
    assert min(g) >= 0 and g[1] >= 1
    T = next(m for m in range(1, L + 1) if m == L or g[m] < 1)   # g >= 1 on [1, T)
    A = -sum(ck * math.log(k) / k for k, ck in c.items())
    return A, T, A * T / (T - 1), sorted(set(g))

cheb = {1: 1, 2: -1, 3: -1, 5: -1, 30: 1}
binom = {1: 1, 2: -2}
for nm, c in (('Chebyshev 1852', cheb), ('C(2n,n)', binom)):
    A, T, k, vals = kappa(c); print(f'{nm}: A = {A:.6f}, T = {T}, kappa = {k:.6f}, values of g = {vals}')

# identity check: log F_x = sum_{n<=x} Lambda(n) g(x/n) at x = 2000 (exact factorial logs via lgamma)
x = 2000
lhs = sum(ck * math.lgamma(x // k + 1) for k, ck in cheb.items())
lam = [0.0] * (x + 1)
for p in primerange(2, x + 1):
    pk = p
    while pk <= x: lam[pk] = math.log(p); pk *= p
rhs = sum(lam[n] * sum(ck * ((x // n) // k) for k, ck in cheb.items()) for n in range(1, x + 1))
psi = sum(lam); print(f'x = {x}: log F_x = {lhs:.4f}, sum Lambda(n) g(x/n) = {rhs:.4f}; psi(x)/x = {psi/x:.4f}; Ax = {0.921292*x:.1f}')

# LP: minimise kappa over real c supported on div(M), g >= 0 on [0, M), g >= 1 on [1, T), sum c_k/k = 0.
def lp(M, T):
    D = divisors(M); n = len(D)
    obj = [-math.log(k) / k * T / (T - 1) for k in D]             # kappa = A T/(T-1)
    Aub, bub = [], []
    for m in range(M):
        row = [-(m // k) for k in D]; Aub.append(row); bub.append(-1 if 1 <= m < T else 0)
    res = linprog(obj, A_ub=Aub, b_ub=bub, A_eq=[[1 / k for k in D]], b_eq=[0], bounds=[(-50, 50)] * n, method='highs')
    return (res.fun if res.status == 0 else None), res
out = []
for M in (6, 30, 210, 2310):
    best = None
    for T in range(2, min(M, 40) + 1):
        v, r = lp(M, T)
        if v is not None and (best is None or v < best[0]): best = (v, T)
    out.append((M, best)); print(f'M = {M}: min kappa over real c on div(M) = {best[0]:.6f} at T = {best[1]}')
print('all LP optima > 1:', all(b[0] > 1 for _, b in out))
