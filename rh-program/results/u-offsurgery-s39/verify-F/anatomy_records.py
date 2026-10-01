# Orchestrator (Session 40): anatomy of the overshoot of S5(rho) -- where are the record values of E attained,
# and are they single-integer multiplicity spikes?  Rule exactly as NOTE section 2:
#   m_n = max(0, floor(rho*(n-1) + 1 - N(n-1) - A(n) + 1/2)),  a_n = A(n) + m_n.
# Exact arithmetic: rho = num/den, counts as Python ints via numpy int64 arrays.
import numpy as np, sys, math
num, den = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) > 2 else (4, 5)
X = int(float(sys.argv[3])) if len(sys.argv) > 3 else 10**6
a = np.zeros(X + 1, dtype=np.int64); a[1] = 1
m = np.zeros(X + 1, dtype=np.int32)
N = 1
recE = []      # (n, E*den, a_n, m_n, E(n-1)*den)
reca = []      # records of a_n
maxa = 0; maxE = -10**18
busy_start = None; busy_max = 0; busy_records = []
prevE = 0
for n in range(2, X + 1):
    A = int(a[n])
    # floor(rho*(n-1) + 1 - N - A + 1/2) with rho = num/den:  floor((2*num*(n-1) + 2*den*(1 - N - A) + den) / (2*den))
    t = (2*num*(n-1) + 2*den*(1 - N - A) + den) // (2*den)
    k = t if t > 0 else 0
    if k:
        m[n] = k
        for _ in range(k):
            idx = np.arange(n, X + 1, n)
            # ascending in-place geometric series: must go in increasing order
            for j in idx.tolist():
                a[j] += a[j // n]
    an = int(a[n]); N += an
    Eden = den*N - num*(n-1) - den          # den * (N(n) - rho(n-1) - 1)
    if an > maxa:
        maxa = an; reca.append((n, an))
    if Eden > maxE:
        maxE = Eden; recE.append((n, Eden/den, an, k, prevE/den))
    prevE = Eden
def fac(n):
    f = []; d = 2
    while d*d <= n:
        while n % d == 0: f.append(d); n //= d
        d += 1
    if n > 1: f.append(n)
    return f
print(f"rho = {num}/{den}, X = {X}")
print("records of E(n) = N(n) - rho(n-1) - 1:  n, E(n), a_n, m_n, E(n-1), factorization, is the jump a single spike?")
for (n, E, an, k, pE) in recE[-25:]:
    print(f"  n = {n:>9d}  E = {E:8.2f}  a_n = {an:4d}  m_n = {k}  E(n-1) = {pE:8.2f}  n = {'*'.join(map(str, fac(n)))}")
print("records of a_n: n, a_n, factorization, log(a_n)/log(n)")
for (n, an) in reca[-20:]:
    print(f"  n = {n:>9d}  a_n = {an:4d}  {'*'.join(map(str, fac(n)))}   exponent {math.log(an)/math.log(n):.3f}")
# small g-primes and the carriers of the first refused primes
gp = [q for q in range(2, 400) if m[q] > 0]
print("g-primes < 400 (with multiplicity >1 marked):", [(q if m[q] == 1 else (q, int(m[q]))) for q in gp])
