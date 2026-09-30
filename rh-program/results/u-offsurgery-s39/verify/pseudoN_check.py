"""pseudoN_check.py -- independent re-derivation of S5 (route 2 for the counts): the greedy rule is the same,
but a(n) is computed by the log-derivative recursion a(n) log n = sum_{d|n, d>1} Lambda_P(d) a(n/d)
(divisors from a smallest-prime-factor table), not by the multiplicative DP of pseudoN.c.
Compares a_n with the C dump a_<label>.u16 and reports N(x) - rho x at checkpoints.
Usage: python3 pseudoN_check.py rho X label"""
import sys, math, numpy as np
rho, X, lab = float(sys.argv[1]), int(float(sys.argv[2])), sys.argv[3]
BIG = "/private/tmp/claude-501/-Users-jaytyagi-Library-Mobile-Documents-com-apple-CloudDocs-Documents-Work-2026-Math/a1ca2244-cf17-4f92-9355-9db717d0d6ae/scratchpad/big"
spf = list(range(X + 1))
for p in range(2, int(X**0.5) + 1):
    if spf[p] == p:
        for k in range(p*p, X + 1, p):
            if spf[k] == k: spf[k] = p
def divisors(n):
    ds = [1]
    while n > 1:
        p = spf[n]; e = 0
        while n % p == 0: n //= p; e += 1
        ds = [d * p**j for d in ds for j in range(e + 1)]
    return ds
Lam = {}                      # Lambda_P(d) for g-prime powers d (as known so far)
a = [0] * (X + 1); a[1] = 1; N = 1; out = []
for n in range(2, X + 1):
    s = 0.0
    for d in divisors(n):
        if d > 1 and d in Lam: s += Lam[d] * a[n // d]
    A = int(round(s / math.log(n)))
    need = rho * (n - 1) + 1 - (N + A)
    m = int(math.floor(need + 0.5)) if need > 0 else 0
    if m > 0:
        q = n
        while q <= X: Lam[q] = Lam.get(q, 0.0) + m * math.log(n); q *= n
    a[n] = A + m; N += a[n]
    if n in (10**3, 10**4, 10**5, 10**6, 2 * 10**6): out.append((n, N - (rho * (n - 1) + 1)))
c = np.fromfile(f"{BIG}/a_{lab}.u16", dtype=np.uint16)[:X].astype(np.int64)   # c[i] = a_{i+1}
mism = np.nonzero(c != np.array(a[1:]))[0]
print(f"rho={rho} X={X}: mismatches between log-derivative route and C dump: {len(mism)}"
      + (f" (first at n={mism[0]+1})" if len(mism) else ""), "; E at checkpoints:", out)
