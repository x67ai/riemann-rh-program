"""Re-check of r1_lp.py's class-(B) verdict without BLAS matmul (numpy 2 + Accelerate raised spurious FP warnings there):
for every RH-false datum with a genuine list, re-solve LP (B) and evaluate min f on 200 001 points by explicit sums."""
import json, math
import numpy as np
from scipy.optimize import linprog
Z = json.load(open('r1_zeta_data.json')); G = json.load(open('r1_genuine.json'))
M = 8; TH = np.linspace(0, math.pi, 200001); CS = [np.cos(n * TH) for n in range(1, M + 1)]
tot = weil = notweil = 0; worst = []
for key in ('g1_q5', 'g2_q5', 'g1_q7', 'g2_q7', 'g1_q11'):
    g, q = int(key[1]), int(key.split('q')[1])
    rows = [r for r in Z[str(q)] if r['g'] == g]
    gs = set(tuple(x) if isinstance(x, list) else x for x in G[key])
    gen = [r for r in rows if (r['t'] in gs if g == 1 else (r['a1'], r['a2']) in gs)]
    P = lambda r: [r['s'][n] / q**(n / 2) for n in range(1, M + 1)]
    A = [[-x for x in P(r)] for r in gen]; b = [float(g)] * len(gen)
    for r in rows:
        if r['rh']: continue
        res = linprog(P(r), A_ub=A, b_ub=b, bounds=[(-1, 1)] * M, method='highs')
        if res.status != 0 or g + res.fun > -1e-9: continue
        f = np.ones_like(TH)
        for n in range(M): f = f + 2 * res.x[n] * CS[n]
        tot += 1; fm = float(f.min())
        if fm >= -1e-9: weil += 1
        else: notweil += 1
        worst.append(fm)
print("class B separations re-checked: %d; optimum a Weil test (f >= 0 on the circle): %d; not: %d; max over cases of min f = %.4f"
      % (tot, weil, notweil, max(worst)))
