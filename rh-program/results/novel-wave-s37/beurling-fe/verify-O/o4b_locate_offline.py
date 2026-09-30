#!/usr/bin/env python3
"""o4b -- locate the zeros of xi_F (signed solution of o3) in 1/2 < Re s <= 2, 0.5 <= t <= 40, and the on-line zeros.
Grid of |F| on sigma in [0.52, 2], t in [0.5, 40] (F and xi_F share zeros for Re s > 0, s != 0); minima refined by findroot."""
import mpmath as mp
mp.mp.dps = 30
a = mp.sqrt(5); chi5 = [0, 1, -1, -1, 1]
D = lambda s: -mp.power(5, s / 2) - mp.power(5, (1 - s) / 2) + a * mp.power(a / 2, -s) + 2 * mp.power(a / 2, s)
F = lambda s: mp.power(5, s / 2) * mp.dirichlet(s, chi5) + D(s) * mp.zeta(s)
xi = lambda s: mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * F(s)
mp.mp.dps = 12
sig = [0.52 + 0.04 * i for i in range(38)]; ts = [0.5 + 0.1 * j for j in range(396)]
g = {(i, j): abs(F(mp.mpc(sig[i], ts[j]))) for i in range(len(sig)) for j in range(len(ts))}
c = [(i, j) for (i, j), v in g.items() if 0 < i < len(sig) - 1 and 0 < j < len(ts) - 1 and
     all(v <= g[(i + di, j + dj)] for di in (-1, 0, 1) for dj in (-1, 0, 1)) and v < 0.3]
mp.mp.dps = 30
found = []
for i, j in c:
    try: z = mp.findroot(F, mp.mpc(sig[i], ts[j]))
    except Exception: continue
    if mp.re(z) > 0.5 + 1e-6 and 0.5 <= mp.im(z) <= 40 and abs(F(z)) < 1e-20 and all(abs(z - w) > 1e-8 for w in found):
        found.append(z)
for z in found:
    print(f"OFF-LINE zero: s = {mp.nstr(z, 14)}  |F| = {mp.nstr(abs(F(z)), 3)}  partner 1-conj(s) = {mp.nstr(1 - mp.conj(z), 10)}"
          f"  |xi_F(1-conj s)| = {mp.nstr(abs(xi(1 - mp.conj(z))), 3)}")
on = []
for t0 in [0.5 + 0.05 * k for k in range(790)]:
    u, v = mp.re(xi(mp.mpc(0.5, t0))), mp.re(xi(mp.mpc(0.5, t0 + 0.05)))
    if u * v < 0: on.append(mp.findroot(lambda t: mp.re(xi(mp.mpc(0.5, t))), (t0, t0 + 0.05), solver='anderson'))
print("on-line zeros t (0.5 < t < 40):", [mp.nstr(t, 10) for t in on])
print(f"count: off-line {len(found)} (each with a mirror at 1 - conj s) + on-line {len(on)}")
