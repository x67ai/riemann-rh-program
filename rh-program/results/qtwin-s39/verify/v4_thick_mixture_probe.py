"""v4 (qtwin-s39): the smallest open sub-class T (NOTE §7) -- positive J-symmetric Poisson mixtures F = zeta*D, D = sum_b m_b b^-s,
atoms b in [1, q] (q = 4): m_1 = 1, m_4 = 2, m_2 = t >= 0 (J-fixed), and for b in B_M = {n/d in (1,2) : d <= M}: m_b = w_b >= 0,
m_{4/b} = (2/b) w_b (J-symmetry m_{q/b} = sqrt(q) m_b / b).  FE, self-duality, dN >= 0 and the gap are AUTOMATIC; the only condition is
Pi_F = Pi_zeta + log*(m) >= 0.  Finite truncations are excluded by QC Theorem L' (finite S); this probe measures how far the
violation can be pushed: maximize min_{x <= X} Pi_F(x) over (t, w) by random-restart local search (evidence, not load).
log*(m) by the log-derivative recursion  m(x) log x = sum_{b y = x} m(b) L(y),  L(y) = log*(m)(y) log y.
"""
from fractions import Fraction as Fr
import math, random, sys
import numpy as np
from scipy.optimize import minimize

def pi_zeta(x):
    if x.denominator != 1:
        return 0.0
    n = x.numerator
    for p in range(2, n + 1):
        if n % p == 0:
            k, m = 0, n
            while m % p == 0:
                m //= p; k += 1
            return 1.0/k if m == 1 else 0.0
    return 0.0

def build(M, X):
    B = sorted({Fr(n, d) for d in range(2, M + 1) for n in range(d + 1, 2*d) if math.gcd(n, d) == 1})
    atoms = [Fr(1), Fr(2), Fr(4)] + B + [Fr(4)/b for b in B]
    gens = [a for a in atoms if a > 1]
    elems = {Fr(1)}
    frontier = [Fr(1)]
    while frontier:
        new = []
        for e in frontier:
            for g in gens:
                p = e*g
                if p <= X and p not in elems:
                    elems.add(p); new.append(p)
        frontier = new
    E = sorted(elems)
    idx = {e: i for i, e in enumerate(E)}
    # for each element x, list of (atom index, y index) with atom*y = x, atom > 1
    aidx = {a: i for i, a in enumerate(atoms)}
    fac = [[] for _ in E]
    for j, y in enumerate(E):
        for a in gens:
            x = a*y
            if x in idx:
                fac[idx[x]].append((aidx[a], j))
    return B, atoms, E, fac

def masses(params, B):
    t, w = params[0], params[1:]
    m = [1.0, t, 2.0] + list(w) + [2.0*float(1/b)*wb for b, wb in zip(B, w)]
    return m

def pi_F(params, B, atoms, E, fac, PZ):
    m = masses(params, B)
    aval = {a: i for i, a in enumerate(atoms)}
    L = np.zeros(len(E))
    out = np.zeros(len(E))
    for i, x in enumerate(E):
        if i == 0:
            continue
        lx = math.log(x)
        mx = m[aval[x]] if x in aval else 0.0
        s = mx*lx - sum(m[ai]*L[j] for ai, j in fac[i] if j != 0 or False) + 0.0
        # the term with y = 1 is m(x)*L(1) = 0; recursion: L(x) = m(x) log x - sum_{b>1, y<x} m(b) L(y)
        L[i] = mx*lx - sum(m[ai]*L[j] for ai, j in fac[i] if j != i)
        out[i] = PZ[i] + L[i]/lx
    return out

def run(M, X, starts=40, seed=1):
    B, atoms, E, fac = build(M, X)
    PZ = np.array([pi_zeta(e) for e in E])
    rng = random.Random(seed)
    best = (-1e18, None, None)
    def obj(p):
        p = np.maximum(p, 0.0)
        v = pi_F(p, B, atoms, E, fac, PZ)[1:]
        return -np.min(v)
    for s in range(starts):
        p0 = np.array([rng.uniform(0, 3)] + [rng.uniform(0, 2) for _ in B])
        r = minimize(obj, p0, method='Nelder-Mead', options={'maxiter': 4000, 'xatol': 1e-9, 'fatol': 1e-12})
        val = -r.fun
        if val > best[0]:
            v = pi_F(np.maximum(r.x, 0), B, atoms, E, fac, PZ)
            worst = E[int(np.argmin(v[1:])) + 1]
            best = (val, np.maximum(r.x, 0), worst)
    return B, len(E), best

if __name__ == "__main__":
    X = 64
    for M in (2, 3, 4):
        B, n, (val, p, worst) = run(M, X)
        print(f"q=4, M={M}: |B_M| = {len(B)}, monoid elements <= {X}: {n}; best max-min Pi_F on [1,{X}] = {val:.6f} "
              f"(binding at x = {worst}); t = {p[0]:.4f}, w = {[round(v, 4) for v in p[1:]]}")
        sys.stdout.flush()
