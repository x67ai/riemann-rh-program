#!/usr/bin/env python3
"""checkpoints_O.py — table of N(V), pi_P(V), E(V) = N(V) - rho (V - 1) - 1 at V = floor(10^(h/2)) from the 10^10 generator
logs, plus the lattice point x_m just below V (m = cell - 1) with E(x_m) = e_m + 1/2 (read-O, U6)."""
import re
from flint import arb, ctx
ctx.prec = 128
for D in (16, 32):
    rho = arb.pi() / D
    print("S8(pi/%d)  V | N(V) | pi_P(V) | E(V) | m (x_m < V < x_{m+1}) | N(x_m) | E(x_m)" % D)
    for line in open("logs/gen_pi%d_1e10.log" % D):
        mm = re.match(r"CHECK V=(\d+) cell=(\d+) N\(V\)=(\d+) pi\(V\)=(\d+) \| lattice x_(\d+): N=(\d+) pi=(\d+) e=(\d+)", line)
        if not mm: continue
        V, cell, NV, piV, m, Nm, pim, em = map(int, mm.groups())
        EV = arb(NV) - rho * (V - 1) - 1
        print("%d | %d | %d | %s | %d | %d | %d.5" % (V, NV, piV, EV.str(10), m, Nm, em))
    for line in open("logs/gen_pi%d_1e10.log" % D):
        if line.startswith("FINAL"): print(line.strip())
