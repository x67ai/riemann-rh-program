#!/usr/bin/env python3
"""U4-sparse: scaling-limit (macroscopic) version of the alternating brackets of Prop. 3.3.
Antitone map T(f) = (1 - c[f])^+, c[f] = density of exp*(f ds) - delta_0 - f ds, computed on a grid from the identity
s*g(s) = s*f(s) + int_0^s u f(u) g(s-u) du for the density g of exp*(f ds) - delta_0 (trapezoid rule).
f^0 = 1 (all lattice points); f^{2k} >= f0 >= f^{2k+1}. Reports, for each even level, the first tau where c[f^{2k}] >= 1
(the level-2k load crosses 1), and sup|f^n - f0|."""
import numpy as np, math
S, h = 12.0, 0.002
s = np.arange(0, S + h/2, h); n = len(s)
f0 = np.where(s > 0, (1 - np.exp(-s))/np.where(s > 0, s, 1), 1.0)
def comp(f):
    g = np.zeros(n); uf = s*f; g[0] = f[0]                       # g(0+) = f(0+)
    for i in range(1, n):
        acc = uf[1:i] @ g[i-1:0:-1] if i > 1 else 0.0          # sum_{j=1}^{i-1} u_j f_j g_{i-j}
        acc += 0.5*uf[i]*g[0]                                   # trapezoid endpoint j = i (endpoint j = 0 vanishes)
        g[i] = (s[i]*f[i] + h*acc)/s[i]
    c = g - f; c[0] = 0.0
    return c
f = np.ones(n); out = []
for lev in range(0, 9):
    c = comp(f)
    cross = s[np.argmax(c >= 1)] if np.any(c >= 1) else float('inf')
    out.append((lev, cross, float(np.max(np.abs(f - f0)))))
    print(f"level {lev}: load c[f^{lev}] first >= 1 at tau = {cross:.3f};  sup|f^{lev} - f0| on [0,{S}] = {out[-1][2]:.4f}", flush=True)
    f = np.clip(1 - c, 0, None)
print("check: c[f0] should equal 1 - f0:", float(np.max(np.abs(comp(f0) - (1 - f0)))))
