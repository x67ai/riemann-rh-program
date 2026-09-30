"""Unit fejer-form-s39, rung 1, step 3: separation of the RH-false zeta data from the genuine curves, by LP and by Toeplitz.
Every functional linear in (g, N_1..N_M) vanishing at genus 0 is I_c(Z) = c0*g + sum_n c_n p_n(Z), p_n = s_n q^{-n/2}
(NOTE §2, identity (E)), and equals sum_j f(theta_j) with f = c0 + 2 sum_n c_n cos(n theta).  M = 8, c0 = 1 (mean of f is 1).
 (A)  Weil class:     f >= 0 on a grid of 4001 points of [0, pi] (then re-checked on 200 001 points).
 (A+) Oesterle class: (A) plus c_n >= 0 for n >= 2 (Oesterle's sign condition; see NOTE §5 for the duality).
 (B)  genuine class:  I_c(Z) >= 0 on every GENUINE curve of the same (q, g) (r1_genuine.json), |c_n| <= 1.
For each RH-false datum: min I_c(v) in each class; the first M with lambda_min(T_M) < 0 (T_M = [p_|a-b|], p_0 = 2g);
the untwisted / twisted Fejer tests K_M(theta), K_M(theta + pi), K_M = (1/(M+1))|sum_{k<=M} e^{ik theta}|^2."""
import json, math
import numpy as np
from scipy.optimize import linprog
Z = json.load(open('r1_zeta_data.json')); G = json.load(open('r1_genuine.json'))
M = 8; TH = np.linspace(0, math.pi, 4001); THF = np.linspace(0, math.pi, 200001)
COS = np.cos(np.outer(np.arange(1, M + 1), TH)); COSF = np.cos(np.outer(np.arange(1, M + 1), THF))
def pvec(r, q): return np.array([r['s'][n] / q**(n / 2) for n in range(1, M + 1)])
def tmin(p, g, m):
    P = np.concatenate([[2 * g], p[:m]]); T = np.array([[P[abs(a - b)] for b in range(m + 1)] for a in range(m + 1)])
    return np.linalg.eigvalsh(T)[0]
def fejer(p, g, m, twist):
    c = np.array([(1 - n / (m + 1)) * ((-1)**n if twist else 1) for n in range(1, m + 1)])
    return g + float(np.dot(c, p[:m]))
def lp(pv, g, cls, gen_ps=None, m=M):
    obj = pv[:m]                      # minimize g + c.p  (c0 = 1)
    A, b = [], []
    if cls in ('A', 'A+'):
        A = -2 * COS[:m].T; b = np.ones(len(TH))               # 1 + 2 c.cos >= 0
    if cls == 'B':
        A = -np.array([gp[:m] for gp in gen_ps]); b = np.full(len(gen_ps), float(g))   # g + c.p >= 0
    bounds = [(0 if (cls == 'A+' and n >= 2) else -1, 1) for n in range(1, m + 1)]
    res = linprog(obj, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    c = res.x; fmin = 1 + 2 * float(np.min(c @ COSF[:m])) if res.status == 0 else None
    return (g + res.fun if res.status == 0 else None), c, fmin
summary = {}
for q in (5, 7, 11):
    for g in (1, 2):
        rows = [r for r in Z[str(q)] if r['g'] == g]
        key = 'g%d_q%d' % (g, q)
        gen = None
        if key in G:
            gs = set(tuple(x) if isinstance(x, list) else x for x in G[key])
            gen = [r for r in rows if (r['t'] in gs if g == 1 else (r['a1'], r['a2']) in gs)]
        gen_ps = [pvec(r, q) for r in gen] if gen else None
        false = [r for r in rows if not r['rh']]
        # sanity: every RH-true datum has T_M PSD for M <= 8
        worst_true = min(tmin(pvec(r, q), g, m) for r in rows if r['rh'] for m in range(1, M + 1))
        stats = dict(n_false=len(false), n_gen=(len(gen) if gen else None), worst_lambda_RHtrue=worst_true,
                     Mstar={}, caught={'A': 0, 'A+': 0, 'B': 0, 'fejer': 0, 'twisted': 0}, B_is_weil=0, B_not_weil=0)
        for r in false:
            pv = pvec(r, q)
            ms = next((m for m in range(1, M + 1) if tmin(pv, g, m) < -1e-9), None)
            stats['Mstar'][str(ms)] = stats['Mstar'].get(str(ms), 0) + 1
            vA, cA, fA = lp(pv, g, 'A'); vAp, _, _ = lp(pv, g, 'A+')
            if vA is not None and vA < -1e-9: stats['caught']['A'] += 1
            if vAp is not None and vAp < -1e-9: stats['caught']['A+'] += 1
            if min(fejer(pv, g, m, False) for m in range(1, M + 1)) < -1e-9: stats['caught']['fejer'] += 1
            if min(fejer(pv, g, m, True) for m in range(1, M + 1)) < -1e-9: stats['caught']['twisted'] += 1
            if gen_ps:
                vB, cB, fB = lp(pv, g, 'B', gen_ps)
                if vB is not None and vB < -1e-9:
                    stats['caught']['B'] += 1
                    if fB >= -1e-9: stats['B_is_weil'] += 1
                    else: stats['B_not_weil'] += 1
        summary[key] = stats
        print(key, json.dumps(stats))
json.dump(summary, open('r1_lp_summary.json', 'w'), indent=1)
