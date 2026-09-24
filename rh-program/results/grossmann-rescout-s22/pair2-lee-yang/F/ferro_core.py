# ferro_core.py: the solver core of ferro_fit.py (v2, with the polish step), imported by ferro_shapes.py.
# Scout F: genus-2 feasibility.  For each RH-true class (p, a1, a2), each sign s in {+1 identity, -1 flip = quadratic twist},
# and each m = m_lo..m_hi: is T(z) = P~_s(z) (1+z)^m, P~_s(z) = 1 + s b1 z + b2 z^2 + s b1 z^3 + z^4, b1 = a1/sqrt q, b2 = a2/q,
# the partition function of an N = 4+m site +-1 ferromagnet with pair couplings J_e >= 0 and uniform fugacity z?
#   Z_J(z) = sum_sigma z^{#up} exp(sum_{e=ij} J_e sigma_i sigma_j);  with S = {up sites}, sum_e J_e s_i s_j = J_tot - 2 cut_J(S), so
#   Z_J(z)/Z_J(0) = sum_S z^{|S|} exp(-2 cut_J(S)) =: sum_k r_k(J) z^k,  r_0 = 1,  r_k = r_{N-k}  (global flip symmetry).
# Feasibility = solve r_k(J) = t_k := coeff_k(T)/coeff_0(T), k = 1..floor(N/2), J in [0, JCAP]^E, by bounded least squares on
# f_k = log r_k - log t_k with analytic Jacobian, multi-start.  ACCEPT: max|f| < TOL, no J_e within 1e-6 of JCAP (a J_e at the cap
# means "realizable only in the limit J -> infinity", which is NOT a finite realization).  Certificate printed: J vector,
# residual, sigma_min of the Jacobian (full row rank => regular point of the map), min J, max J.
# Necessary pre-check: all coefficients of T positive (r_k > 0 for every finite J).  Monotone in m: adjoining a decoupled spin
# (J = 0 to everything) multiplies Z by (1+z), so realizable at m => realizable at every m' >= m; we record the least m.
import json, math, sys, time, itertools
import numpy as np
from scipy.optimize import least_squares
t0 = time.time()
NSTART = 12
import os
JCAP = float(os.environ.get('JCAP', '8.0')); TOL = 1e-12   # JCAP 8: w = e^{-16} = 1.1e-7; a coupling at the cap is a limit point, not a finite realization
rng = np.random.default_rng(20260924)

def poly_mul(a, b):
    out = [0.0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out

_cache = {}
def structure(N):
    if N in _cache: return _cache[N]
    edges = list(itertools.combinations(range(N), 2)); E = len(edges)
    K = N // 2
    rows = []; kidx = []
    for k in range(1, K + 1):
        for S in itertools.combinations(range(N), k):
            Sset = set(S)
            rows.append([1.0 if ((i in Sset) != (j in Sset)) else 0.0 for (i, j) in edges])
            kidx.append(k - 1)
    CUT = np.array(rows); kidx = np.array(kidx)
    _cache[N] = (edges, E, K, CUT, kidx)
    return _cache[N]

def make_funcs(N, logt):
    edges, E, K, CUT, kidx = structure(N)
    def rk(J):
        wS = np.exp(-2.0 * CUT @ J)                       # exp(-2 cut_J(S)) per subset
        r = np.zeros(K); np.add.at(r, kidx, wS)
        return r, wS
    def fun(J):
        r, _ = rk(J); return np.log(r) - logt
    def jac(J):
        r, wS = rk(J)
        G = np.zeros((K, E))
        # d r_k / d J_e = sum_{S in k} -2 CUT[S,e] wS
        np.add.at(G, kidx, -2.0 * CUT * wS[:, None])
        return G / r[:, None]
    return fun, jac, K, E, edges

def solve(N, t):
    """t: normalized target coefficients t_1..t_K.  Returns dict."""
    logt = np.log(np.array(t))
    fun, jac, K, E, edges = make_funcs(N, logt)
    best = None
    for s in range(NSTART):
        if s == 0: J0 = np.full(E, 0.3)
        elif s == 1: J0 = np.full(E, 0.05)
        else: J0 = rng.uniform(0.0, 1.5, E) * (rng.uniform(size=E) < 0.7)
        res = least_squares(fun, J0, jac=jac, bounds=(0.0, JCAP), method='trf', xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=400)
        f = fun(res.x); err = float(np.max(np.abs(f)))
        if best is None or err < best['err']:
            G = jac(res.x); sv = np.linalg.svd(G, compute_uv=False)
            best = dict(err=err, J=res.x, smin=float(sv[-1]) if len(sv) == K else 0.0, starts=s + 1)
        if err < 1e-6 and np.max(res.x) < JCAP - 1e-6:
            break
    J = np.array(best['J'])
    # polish: fix couplings below 1e-6 at exactly 0 (a decoupled bond is admissible), Newton (least-norm) on the free ones
    if best['err'] < 1e-4 and np.max(J) < JCAP - 1e-6:
        free = J > 1e-6
        Jp = np.where(free, J, 0.0)
        for it in range(40):
            f = fun(Jp); G = jac(Jp)[:, free]
            if np.max(np.abs(f)) < 1e-14: break
            step = np.linalg.lstsq(G, -f, rcond=None)[0]
            Jn = Jp.copy(); Jn[free] += step
            if np.min(Jn[free]) < 0:   # a free coupling wants to go negative: shrink the step, then give up on this polish
                lam = 1.0
                while lam > 1e-6 and np.min(Jp[free] + lam * step) < 0: lam *= 0.5
                if lam <= 1e-6: break
                Jn = Jp.copy(); Jn[free] += lam * step
            Jp = Jn
        errp = float(np.max(np.abs(fun(Jp))))
        if errp < best['err'] and np.min(Jp) >= 0 and np.max(Jp) < JCAP - 1e-6:
            G = jac(Jp); sv = np.linalg.svd(G, compute_uv=False)
            best.update(err=errp, J=[float(x) for x in Jp], smin=float(sv[-1]) if len(sv) == K else 0.0, polished=True)
            J = Jp
    best['ok'] = bool(best['err'] < TOL and np.max(J) < JCAP - 1e-6 and np.min(J) >= 0)
    best['at_cap'] = bool(np.max(J) >= JCAP - 1e-6)
    best['Jmin'] = float(np.min(J)); best['Jmax'] = float(np.max(J))
    best['nzero'] = int(np.sum(J < 1e-9))
    best['J'] = [round(float(x), 10) for x in J]
    return best

