"""F1 SPEC — two hand counts re-run (writer, Session 29).
(1) A9 precision: on A^1 over F_7, the host's pairing summed over pairs (m, n) of effective
    divisors with |m| = 1, |n| = 2 (Theorem 3.3 of E3, in units of log 7) versus the surface's
    (Gamma_Fr . Gamma_Fr^2) = q * N_1 = 49 (the curves y = x^7, y = x^49 meet at the 7 points of
    F_7 with multiplicity 7).
(2) P9j (T4) mismatch: host deg(Gamma_m cap Gamma_n) over Z (E3 Theorem 3.3 transferred; R-b')
    versus target (sigma_{a^m} . sigma_{a^n}) = log |a^m - a^n| on P^1_Z, for a = 2.
"""
from itertools import combinations_with_replacement, product
from math import log, gcd

# (1) A^1 over F_7: closed points of degree 1: 7; of degree 2: 21. Divisors as dicts point->mult.
q = 7
pts1 = [("d1", i) for i in range(7)]
pts2 = [("d2", i) for i in range(21)]
pts3 = [("d3", i) for i in range(112)]  # a_3 = (343 - 7)/3
deg = {p: 1 for p in pts1}
deg.update({p: 2 for p in pts2})
deg.update({p: 3 for p in pts3})
def divisors_of_degree(N):
    out = []
    pts = pts1 + pts2 + pts3
    def rec(i, rem, cur):
        if rem == 0:
            out.append(dict(cur)); return
        if i == len(pts): return
        p = pts[i]
        for k in range(0, rem // deg[p] + 1):
            if k: cur[p] = k
            rec(i + 1, rem - k * deg[p], cur)
            if k: del cur[p]
    rec(0, N, {})
    return out
def host_pair(m, n):  # Theorem 3.3, in units of log q
    diff = [p for p in set(m) | set(n) if m.get(p, 0) != n.get(p, 0)]
    if len(diff) != 1: return 0
    p = diff[0]
    return (1 + min(m.get(p, 0), n.get(p, 0))) * deg[p]
D1, D2 = divisors_of_degree(1), divisors_of_degree(2)
host_sum = sum(host_pair(m, n) for m in D1 for n in D2)
target = q * 7  # q^M * N_{N-M} with M=1, N=2, N_1 = 7
print("A9 check: #D1 =", len(D1), "#D2 =", len(D2), "host sum =", host_sum, "target =", target,
      "MISMATCH" if host_sum != target else "equal")
# also the diagonal row (Theorem 3.4) as a control: sum_{|n|=N} deg(Gamma_0, Gamma_n) = N_N
for N in (1, 2, 3):
    DN = divisors_of_degree(N)
    s = sum(host_pair({}, n) for n in DN)
    print("  control Theorem 3.4 at N =", N, ": host", s, "vs N_N =", q ** N)

# (2) P9j over Z, a = 2
def host_Z(m, n):
    if m == n: return None
    # differ at exactly one prime p: m/n a power of p
    r = max(m, n) // gcd(m, n); s = min(m, n) // gcd(m, n)
    if s != 1: return 0.0
    # r = p^k ?
    p = 2
    while p * p <= r and r % p: p += 1
    if r % p: p = r
    k = 0
    while r % p == 0: r //= p; k += 1
    if r != 1: return 0.0
    vm = 0; t = m
    while t % p == 0: t //= p; vm += 1
    vn = 0; t = n
    while t % p == 0: t //= p; vn += 1
    return (1 + min(vm, vn)) * log(p)
a = 2
for (m, n) in [(1, 2), (1, 3), (2, 3), (1, 4), (1, 5), (2, 4), (3, 6)]:
    h = host_Z(m, n); t = log(abs(a ** m - a ** n))
    print(f"P9j a=2 (Gamma_{m},Gamma_{n}): host {h:.6f}  target log|a^m-a^n| {t:.6f}  {'equal' if abs(h-t)<1e-9 else 'MISMATCH'}")
