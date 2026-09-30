#!/usr/bin/env python3
"""CHECK-O independent re-derivation numbers (checker-written, Session 36; the builder's tools/errata_numbers.py was not read).

[S1] the algebra of item 7, exact (sympy): the factorization, r^2 = r + 2g, 1 + r^2 + 2gr = (1 + 2g)(1 + r), and equality in both
     h1 and h2 at x = r^2, L = 1 + r^2 + 2gr (the bound is attained);
[S2] the feasible maximum of L for fixed g, by an exact-in-L scan over x (for each x the feasible L form an interval computable in
     closed form), compared with the bound; and a seeded random search over (g, x, L) including x < 0 and g = 0;
[S3] the necessity counterexamples, evaluated with Mathlib's totalizations (sqrt of a negative = 0, x/0 = 0, log 0 = 0);
[S4] first primes above exp(kappa * bound) for a few (kappa, g);
[S5] E1's kappa < 0 instance and kappa = 0 contradiction, numerically.
"""
import math, random
import sympy as sp

g, s, x, L, r = sp.symbols("g s x L r", real=True)
print("[S1] exact algebra")
lhs = s**4 - s**2 - 2*g*s**2 - 2*g*s
print("  s^4 - s^2 - 2g s^2 - 2g s == s (s + 1)(s^2 - s - 2g):", sp.expand(lhs - s*(s + 1)*(s**2 - s - 2*g)) == 0)
R = (1 + sp.sqrt(1 + 8*g)) / 2
print("  r^2 - r - 2g at r = (1 + sqrt(1 + 8g))/2:", sp.simplify(sp.expand(R**2 - R - 2*g)))
print("  1 + r^2 + 2gr - (1 + 2g)(1 + r) at that r:", sp.simplify(sp.expand(1 + R**2 + 2*g*R - (1 + 2*g)*(1 + R))))
X, LL = R**2, 1 + R**2 + 2*g*R
print("  h1 slack at x = r^2, L = 1 + r^2 + 2gr:", sp.simplify(sp.expand(4*g**2*X - (1 + X - LL)**2)))
print("  h2 slack at x = r^2, L = 1 + r^2 + 2gr:", sp.simplify(sp.expand(4*g**2*X**2 - (1 + X**2 - LL)**2)))
print("  bound at g = 0:", sp.simplify((1 + 2*g)*(1 + R)).subs(g, 0))

def bound(gv):
    return (1 + 2*gv) * (1 + (1 + math.sqrt(max(0.0, 1 + 8*gv))) / 2)

def feasible_L_interval(gv, xv):
    """h1: |1 + x - L| <= 2|g| sqrt(x) (needs x >= 0 unless g = 0); h2: |1 + x^2 - L| <= 2|g| |x|."""
    if gv == 0:
        return (1 + xv, 1 + xv) if abs((1 + xv) - (1 + xv*xv)) < 1e-15 else None
    if xv < 0:
        return None
    a = 2*abs(gv)*math.sqrt(xv); b = 2*abs(gv)*abs(xv)
    lo = max(1 + xv - a, 1 + xv*xv - b); hi = min(1 + xv + a, 1 + xv*xv + b)
    return (lo, hi) if lo <= hi + 1e-12 else None

print("[S2] feasible max of L vs the bound (x scanned on [0, 3 r^2] in 600001 steps)")
for gv in [0.0, 0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 100.0]:
    rv = (1 + math.sqrt(1 + 8*gv)) / 2
    best, argx = -math.inf, None
    N = 600000
    for i in range(N + 1):
        xv = 3*rv*rv * i / N
        iv = feasible_L_interval(gv, xv)
        if iv and iv[1] > best:
            best, argx = iv[1], xv
    print(f"  g={gv:7.2f}: bound {bound(gv):.10f}; scanned max L {best:.10f} at x {argx:.6f} (r^2 = {rv*rv:.6f}); max - bound = {best - bound(gv):+.2e}")
random.seed(20260930)
feas = above = neg_x = 0
for _ in range(400000):
    gv = random.choice([0.0, random.uniform(0, 5)])
    xv = random.uniform(-5, 30)
    Lv = random.uniform(-5, 60)
    ok1 = (1 + xv - Lv)**2 <= 4*gv*gv*xv
    ok2 = (1 + xv*xv - Lv)**2 <= 4*gv*gv*xv*xv
    if ok1 and ok2:
        feas += 1
        neg_x += xv < 0
        above += Lv > bound(gv) + 1e-9
print(f"  random search (seed 20260930, 400000 draws, x in [-5, 30], L in [-5, 60], g = 0 or U[0,5]): feasible {feas}, with x < 0: {neg_x}, above the bound: {above}")

print("[S3] necessity counterexamples with Mathlib's totalizations")
gv, xv, Lv = -1.0, 1.0, 1.0
sq = math.sqrt(1 + 8*gv) if 1 + 8*gv >= 0 else 0.0
print(f"  item 7 at g=-1, x=L=1: h1 {(1 + xv - Lv)**2} <= {4*gv*gv*xv}: {(1 + xv - Lv)**2 <= 4*gv*gv*xv}; h2 {(1 + xv*xv - Lv)**2} <= {4*gv*gv*xv*xv}: {(1 + xv*xv - Lv)**2 <= 4*gv*gv*xv*xv}; bound (1+2g)(1+(1+sqrt0(1+8g))/2) = {(1 + 2*gv)*(1 + (1 + sq)/2)}; L <= bound: {Lv <= (1 + 2*gv)*(1 + (1 + sq)/2)}")
print("  item 8 at kappa = 0 (log p / 0 = 0), d = 1, g = 1: h1 (1 + 1 - 0)^2 = 4 <= 4: True; h2 (1 + 1 - 0)^2 = 4 <= 4: True, at every prime")
print("  item 2: N = 0 -> log 0 = 0 (span {0}); N = 1 -> log 1 = 0 (span {0}): both finite-dimensional")

print("[S4] first prime above exp(kappa * bound(g))")
def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    f = 3
    while f * f <= n:
        if n % f == 0: return False
        f += 2
    return True
for kv, gv in [(1.0, 1.0), (1.0, 0.0), (1.0, 2.0), (math.log(2), 1.0), (1.0, 0.5)]:
    B = bound(gv); T = math.exp(kv * B); p = math.floor(T) + 1
    while not is_prime(p): p += 1
    print(f"  kappa={kv:.6f}, g={gv}: bound {B:.10f}, exp(kappa*bound) = {T:.4f}, first prime above: {p} (log p / kappa = {math.log(p)/kv:.6f})")

print("[S5] E1: kappa < 0 satisfiable; kappa = 0 contradictory at n = 2")
kv = -1.0
for n in [2, 3, 4, 6, 8, 9, 12]:
    Lam = math.log(min(q for q in range(2, n + 1) if n % q == 0)) if (lambda m: len({q for q in range(2, m + 1) if m % q == 0 and is_prime(q)}) == 1)(n) else 0.0
    v = Lam / kv
    print(f"  cls = id, n={n}: fiber {{n}}, fiber sum Lambda(n) = {Lam:.6f}; kappa * v(n) = {kv * v:.6f}; equal: {abs(Lam - kv*v) < 1e-15}")
print(f"  kappa = 0: the fiber sum at n = 2 is >= Lambda(2) = log 2 = {math.log(2):.6f} > 0 = 0 * v: contradictory")
