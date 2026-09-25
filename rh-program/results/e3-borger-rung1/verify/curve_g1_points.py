#!/usr/bin/env python3
"""curve_g1_points.py -- E3 (Session 28): H3's numerical check on the rung-1 model, exact.
S: the complete curve y^2 = x^3 + x + 1 over F_7 (genus 1; results/c2-m5b/FORMULATION.md section 3.1:
N_1..N_4 = 5, 55, 380, 2475). Enumerates the closed points of S of degree <= NMAX (Frobenius orbits of
F_{7^d}-points, the point at infinity included), tabulates a_d = #{closed points of degree d}, and checks
    (H3)  sum_{n : |n| = N, n = k e_m} deg(Gamma_0 cap Gamma_n) / log q = sum_{d | N} d a_d = N_N,
where deg(Gamma_0 cap Gamma_{k e_m}) = deg(m) log q (Theorem 3.3 of NOTE.md) and N_N = #S(F_{7^N}) is
recounted here by brute force. F_{7^d} = F_7[t]/(irreducible of degree d).
"""
import itertools, sys, time
t0 = time.time(); q = 7
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 4
f = [1, 1, 0, 1]   # x^3 + x + 1, low degree first
def irreducible(d):
    if d == 1: return [0, 1]
    for coeffs in itertools.product(range(q), repeat=d):
        g = list(coeffs) + [1]
        # irreducible iff no root in F_{7^e} for e <= d/2: test by gcd with t^{7^e} - t
        ok = True
        for e in range(1, d // 2 + 1):
            # compute t^{7^e} mod g
            r = [0, 1]
            for _ in range(e):
                # raise to 7th power mod g
                s = [1]
                for _ in range(7):
                    s = polymulmod(s, r, g)
                r = s
            h = polygcd(polysub(r, [0, 1]), g)
            if len(h) > 1: ok = False; break
        if ok: return g
def trim(a):
    while a and a[-1] % q == 0: a.pop()
    return a
def polysub(a, b):
    n = max(len(a), len(b)); return trim([((a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)) % q for i in range(n)])
def polymulmod(a, b, g):
    r = [0] * (len(a) + len(b))
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b): r[i + j] = (r[i + j] + x * y) % q
    inv = pow(g[-1], q - 2, q)
    for k in range(len(r) - 1, len(g) - 2, -1):
        c = r[k] * inv % q
        if c:
            for i in range(len(g)): r[k - len(g) + 1 + i] = (r[k - len(g) + 1 + i] - c * g[i]) % q
    return trim(r[:len(g) - 1])
def polygcd(a, b):
    a, b = trim(a[:]), trim(b[:])
    while b:
        # a mod b
        a = a[:]; inv = pow(b[-1], q - 2, q)
        while len(a) >= len(b) and a:
            c = a[-1] * inv % q; k = len(a) - len(b)
            for i, y in enumerate(b): a[k + i] = (a[k + i] - c * y) % q
            trim(a)
        a, b = b, a
    return a
def field(d):
    g = irreducible(d)
    elems = [list(c) for c in itertools.product(range(q), repeat=d)]
    def mul(a, b): return polymulmod(a, b, g) if (a and b) else []
    def add(a, b):
        n = d; return trim([((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % q for i in range(n)])
    def frob(a):
        r = [1]
        for _ in range(7): r = mul(r, a) if a else []
        return r
    return [trim(e) for e in elems], add, mul, frob
N = {}; a = {}
for d in range(1, NMAX + 1):
    elems, add, mul, frob = field(d)
    pts = set()
    for x in elems:
        x2 = mul(x, x); x3 = mul(x2, x)
        rhs = add(add(x3, x), [1])
        for y in elems:
            if trim(mul(y, y)[:]) == rhs: pts.add((tuple(x), tuple(y)))
    N[d] = len(pts) + 1   # + the point at infinity (one rational point, y^2 = cubic)
    # closed points of degree exactly d: orbits of size d under Frobenius (x,y) -> (x^7, y^7), infinity has degree 1
    seen = set(); orbits = 0
    for P in pts:
        if P in seen: continue
        orb = []; Q = P
        while Q not in orb:
            orb.append(Q); Q = (tuple(frob(list(Q[0]))), tuple(frob(list(Q[1]))))
        seen |= set(orb)
        if len(orb) == d: orbits += 1
    a[d] = orbits + (1 if d == 1 else 0)
    print(f"d = {d}: N_{d} = #S(F_7^{d}) = {N[d]} (brute force); a_{d} = #closed points of degree {d} = {a[d]}  [{time.time()-t0:.1f}s]")
print("H3 check: sum_{|n| = N, n = k e_m} deg(Gamma_0 cap Gamma_n)/log 7 = sum_{d | N} d a_d  vs  N_N:")
ok = True
for Nn in range(1, NMAX + 1):
    s = sum(d * a[d] for d in a if Nn % d == 0)
    print(f"  N = {Nn}: {s} vs N_N = {N[Nn]}  {'OK' if s == N[Nn] else 'FAIL'}")
    ok = ok and s == N[Nn]
print("H3 numerical check on g = 1 over F_7:", "PASS" if ok else "FAIL", f"({time.time()-t0:.1f}s)")
