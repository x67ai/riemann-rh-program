#!/usr/bin/env python3
"""o4 -- OPUS READER, seed M1a beurling-fe.  Is the signed solution F of o3 RH-false?  Search zeros of F with Re s > 1.

F(s) = 5^{s/2} L(s,chi_5) + D(s) zeta(s), D(s) = -5^{s/2} - 5^{(1-s)/2} + sqrt5 (sqrt5/2)^{-s} + 2 (sqrt5/2)^{s}.
F has real coefficients, frequencies >= sqrt5/2 > 1, xi_F(s) = xi_F(1-s), simple poles of xi_F at 0, 1 only (o3).
A zero of F at Re s > 1 is a zero of xi_F off the critical line (and 1 - s is another): RH fails for F.
Method: coarse grid of |F| on sigma in [1.1, 3], t in [0, 60]; local minima refined by mpmath.findroot; zeros verified by
|F| < 1e-25 at 40 digits and by the FE partner xi_F(1 - s) = 0.
"""
import mpmath as mp
mp.mp.dps = 40
a = mp.sqrt(5)
chi5 = [0, 1, -1, -1, 1]
D = lambda s: -mp.power(5, s / 2) - mp.power(5, (1 - s) / 2) + a * mp.power(a / 2, -s) + 2 * mp.power(a / 2, s)
F = lambda s: mp.power(5, s / 2) * mp.dirichlet(s, chi5) + D(s) * mp.zeta(s)
xi = lambda s: mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * F(s)

mp.mp.dps = 15
# integer-indexed grid (a first version keyed the grid by floats and silently lost neighbours; fixed 2026-10-01)
sig = [1.1 + 0.1 * i for i in range(20)]
ts = [0.25 * j for j in range(0, 241)]
grid = {(i, j): abs(F(mp.mpc(sig[i], ts[j]))) for i in range(len(sig)) for j in range(len(ts))}
cands = []
for (i, j), v in grid.items():
    if 0 < i < len(sig) - 1 and 0 < j < len(ts) - 1 and v < 0.5 and \
       all(v <= grid[(i + di, j + dj)] for di in (-1, 0, 1) for dj in (-1, 0, 1)):
        cands.append((sig[i], ts[j], v))
print(f"grid minima with |F| < 0.5 in 1.2 <= sigma <= 2.9, 0.25 <= t <= 59.75: {len(cands)}")
mp.mp.dps = 40
zeros = []
for s_, t_, v in sorted(cands, key=lambda c: c[1]):
    try:
        z = mp.findroot(F, mp.mpc(s_, t_))
    except Exception:
        continue
    if mp.re(z) > 1 and abs(F(z)) < mp.mpf(10) ** -25 and all(abs(z - w) > 1e-8 for w in zeros):
        zeros.append(z)
for z in zeros[:12]:
    print(f"  zero of F: s = {mp.nstr(z, 15)}   |F(s)| = {mp.nstr(abs(F(z)), 3)}   |xi_F(1-s)| = {mp.nstr(abs(xi(1 - z)), 3)}")
print(f"zeros of F with Re s > 1 found (t <= 60): {len(zeros)}")

# Part 2: zero count in the rectangle [-1, 2] x [0.5, T] by the argument principle (phase unwrapping, step 0.01)
# versus sign changes of the REAL function Z(t) = xi_F(1/2 + it) on [0.5, T] (step 0.005).
mp.mp.dps = 20
print("min |F| on the grid (sigma >= 1.1):", mp.nstr(min(grid.values()), 5))
T = 40
import sys
if '--count' not in sys.argv: sys.exit(0)   # Part 2 (2.5 min) was run once; its output is kept in the log
def arg_change(path):
    tot = mp.mpf(0); prev = xi(path[0])
    for s in path[1:]:
        cur = xi(s); d = mp.arg(cur / prev); tot += d; prev = cur
    return tot
h = mp.mpf("0.01")
n_v = int((T - 0.5) / h); n_h = int(3 / h)
path = ([mp.mpc(2, 0.5 + k * h) for k in range(n_v + 1)] + [mp.mpc(2 - k * h, T) for k in range(1, n_h + 1)] +
        [mp.mpc(-1, T - k * h) for k in range(1, n_v + 1)] + [mp.mpc(-1 + k * h, 0.5) for k in range(1, n_h + 1)])
Nrect = arg_change(path) / (2 * mp.pi)
Z = lambda t: mp.re(xi(mp.mpc(0.5, t)))
tt = [0.5 + 0.005 * k for k in range(int((T - 0.5) / 0.005) + 1)]
vals = [Z(t) for t in tt]
sc = sum(1 for u, v in zip(vals, vals[1:]) if u * v < 0)
print(f"T = {T}: zeros of xi_F in [-1,2] x [0.5,T] (argument principle) = {mp.nstr(Nrect, 6)};  sign changes of xi_F(1/2+it) = {sc}")
print("  (Im xi_F(1/2+it) = 0 by the FE and real coefficients; a deficit Nrect - sc > 0 means zeros OFF the critical line)")
