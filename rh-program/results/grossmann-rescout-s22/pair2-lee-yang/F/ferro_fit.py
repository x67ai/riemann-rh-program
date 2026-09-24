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
CLASSES = sys.argv[1]; STATE = sys.argv[2]; m_lo = int(sys.argv[3]); m_hi = int(sys.argv[4])
TLIM = float(sys.argv[5]) if len(sys.argv) > 5 else 540.0
NSTART = int(sys.argv[6]) if len(sys.argv) > 6 else 12
JCAP = 25.0; TOL = 1e-12
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

classes = json.load(open(CLASSES))
try: state = json.load(open(STATE))
except Exception: state = {}
done_n = 0
for c in classes:
    p, a1, a2 = c['p'], c['a1'], c['a2']
    b1 = a1 / math.sqrt(p); b2 = a2 / p
    for s in (+1, -1):
        key = f"{p},{a1},{a2},{'id' if s == 1 else 'flip'}"
        rec = state.setdefault(key, dict(p=p, a1=a1, a2=a2, sign=s, tried={}, least_m=None))
        if rec['least_m'] is not None: continue
        P = [1.0, s * b1, b2, s * b1, 1.0]
        for m in range(m_lo, m_hi + 1):
            if str(m) in rec['tried'] and rec['tried'][str(m)]['status'] != 'timeout': continue
            if time.time() - t0 > TLIM:
                json.dump(state, open(STATE, 'w')); print(f"TIME LIMIT at {key} m={m}; state saved; elapsed {time.time()-t0:.1f}s"); sys.exit(0)
            T = P
            for _ in range(m): T = poly_mul(T, [1.0, 1.0])
            N = 4 + m
            if min(T) <= 0:
                rec['tried'][str(m)] = dict(status='nonpositive', mincoef=min(T)); continue
            t = [T[k] / T[0] for k in range(1, N // 2 + 1)]
            r = solve(N, t)
            r['status'] = 'realized' if r['ok'] else ('cap' if r['at_cap'] else 'notfound')
            rec['tried'][str(m)] = r
            if r['ok']:
                rec['least_m'] = m; break
        done_n += 1
        if done_n % 20 == 0:
            json.dump(state, open(STATE, 'w'))
            print(f"... {done_n} (class,sign) pairs processed, elapsed {time.time()-t0:.1f}s", flush=True)
json.dump(state, open(STATE, 'w'))
# summary
n_real = {}; n_status = {}
for key, rec in state.items():
    for m, r in rec['tried'].items():
        n_status.setdefault(int(m), {}).setdefault(r['status'], 0)
        n_status[int(m)][r['status']] += 1
print("per-m status counts over (class,sign) pairs tried at that m:")
for m in sorted(n_status): print(f"  m={m}: {n_status[m]}")
least = [rec['least_m'] for rec in state.values()]
print("least_m distribution over (class,sign):", {m: least.count(m) for m in sorted(set(x for x in least if x is not None))}, " unresolved:", least.count(None))
# per class: realized (identity), realized (either sign)
cls = {}
for key, rec in state.items():
    cls.setdefault((rec['p'], rec['a1'], rec['a2']), {})[rec['sign']] = rec['least_m']
print("classes:", len(cls), " realized with identity sign:", sum(1 for v in cls.values() if v.get(1) is not None),
      " realized with either sign:", sum(1 for v in cls.values() if v.get(1) is not None or v.get(-1) is not None))
print(f"elapsed s: {time.time()-t0:.1f}")
