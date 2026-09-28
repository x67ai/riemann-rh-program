#!/usr/bin/env python3
"""kappa_pipeline.py -- the E5 writer's primal/dual pipeline for  kappa(a) := inf { 2 + int what a / what(0) : w >= 0, what >= 0 }.

Conventions (NOTE.md section 2): what(xi) = int w(u) e^{-i u xi} du; w even.  For an even density a on the tau-line:

DUAL (Theorem D, NOTE section 2):  if d >= 0, sigma an even finite signed measure with sigma >= -d du (as measures) and
   psi(tau) := 2 pi a(tau) - sigmahat(tau) >= 0 for all tau,   then  kappa(a) >= 2 - d.
   [Proof: B - (2-d) what(0) = d int w + int what a = int w (d du + sigma) + (1/2pi) int what psi >= 0.]
   Discretization: sigma = sum_k s_k Lambda_k, Lambda_k = symmetric pair of hat functions of half-width hu at +-u_k (u_k = k hu),
   Lambda_0 = one hat at 0; sigmahat(tau) = hu sinc^2(hu tau/2) [ s_0 + 2 sum_{k>=1} s_k cos(u_k tau) ];  s_k >= -d.
   LP: minimize d subject to sigmahat(tau_i) <= 2 pi a(tau_i) on a tau-grid (cutting planes), s_k + d >= 0.
   Repair for certification: sigma' = sigma - eta e^{-c|u|}, d' = d + eta:  psi' = psi + 2 eta c/(c^2 + tau^2) > 0 margin.
   Certification: psi' >= 0 on [0, T_v] by adaptive Lipschitz cells; on [T_v, inf) by  2 pi a_min(T_v) - sup|sigmahat| + margin > 0,
   sup_{tau >= T} |sigmahat(tau)| <= 4 S0 / (hu T^2), S0 = |s_0| + 2 sum |s_k|  (sinc^2(x) <= 1/x^2).

PRIMAL (family (ii'), NOTE section 4): w = |f|^2 with fhat >= 0 piecewise constant on a grid of step hx (values c_i >= 0);
   then w >= 0 and what = (1/2pi) fhat * fhat~ (autocorrelation) >= 0;  what(0) = (hx/2pi) sum c_i^2;
   int what a = (hx/2pi) sum_{ij} c_i c_j abar_{i-j},  abar_k := int a(k hx + v) (1 - |v|/hx)_+ dv;
   R(c) = 2 + c^T M c / c^T c, M Toeplitz (abar).  Minimized over c >= 0 by L-BFGS-B from several starts.  Every c >= 0
   is a certified upper bound (Lemma A: band-limited squares are limits of C^2_c cone elements).
"""
import numpy as np, time
from scipy.optimize import linprog, minimize
from numpy.polynomial.legendre import leggauss

def sinc2(x):
    return np.sinc(x/np.pi)**2

# ---------------------------------------------------------------- dual LP
def sigmahat_matrix(taus, hu, K):
    """rows: taus; cols: s_0..s_K.  entry = hu sinc^2(hu tau/2) * (1 if k==0 else 2 cos(u_k tau))."""
    taus = np.asarray(taus, float)
    base = hu*sinc2(hu*taus/2)
    k = np.arange(K+1)
    M = 2*np.cos(np.outer(taus, k*hu))
    M[:, 0] = 1.0
    return base[:, None]*M

def dual_lp(a_fn, U, hu, Tmax, coarse=(0.05, 40.0, 0.5), fine=(0.002, 40.0, 0.02), max_rounds=25, add_per_round=300,
            viol_tol=1e-6, margin=0.0, S_max=1000.0, reg=1e-6, time_limit=600.0, log=print):
    """Cutting-plane LP.  Variables: s = s_plus - s_minus with s_plus in [0, S_max], s_minus in [0, d] (so s >= -d), and d >= 0.
    Objective: d + reg*hu*sum(s_plus + s_minus)  (reg selects the minimal-mass certificate among the optimal ones; it moves
    d by at most reg*hu*sum|s| ~ 1e-6*O(10)).  Returns dict with d, s, kappa_lp, rounds, n_rows, active taus, seconds."""
    t0 = time.time()
    K = int(round(U/hu))
    g1 = np.arange(0, coarse[1], coarse[0]); g2 = np.arange(coarse[1], Tmax + 1e-12, coarse[2])
    taus = np.unique(np.concatenate([g1, g2]))
    f1 = np.arange(0, fine[1], fine[0]); f2 = np.arange(fine[1], Tmax + 1e-12, fine[2])
    fine_taus = np.unique(np.concatenate([f1, f2]))
    a_fine = a_fn(fine_taus)
    def psi_fine(s):
        outp = np.empty(len(fine_taus))
        for i in range(0, len(fine_taus), 20000):
            outp[i:i+20000] = 2*np.pi*a_fine[i:i+20000] - sigmahat_matrix(fine_taus[i:i+20000], hu, K) @ s - margin
        return outp
    nv = 2*(K+1) + 1   # s_plus (K+1), s_minus (K+1), d
    cvec = np.concatenate([reg*hu*np.ones(K+1), reg*hu*np.ones(K+1), [1.0]])
    # s_minus_k - d <= 0
    A_box = np.zeros((K+1, nv)); A_box[:, K+1:2*(K+1)] = np.eye(K+1); A_box[:, -1] = -1.0
    b_box = np.zeros(K+1)
    bounds = [(0, S_max)]*(K+1) + [(0, None)]*(K+1) + [(0, None)]
    res = None; d = None; s = None; psi = None
    for rnd in range(max_rounds):
        A_tau = sigmahat_matrix(taus, hu, K)
        A_ub = np.vstack([np.hstack([A_tau, -A_tau, np.zeros((len(taus), 1))]), A_box])
        b_ub = np.concatenate([2*np.pi*a_fn(taus) - margin, b_box])
        res = linprog(cvec, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs", options=dict(time_limit=time_limit))
        if res.status != 0:
            log(f"  LP status {res.status}: {res.message}")
            if s is None: return None
            break
        s = res.x[:K+1] - res.x[K+1:2*(K+1)]; d = res.x[-1]
        psi = psi_fine(s)
        viol = np.where(psi < -viol_tol)[0]
        log(f"  round {rnd:2d}: rows {len(taus):6d}  d = {d:.8f}  kappa_lp = {2-d:.8f}  min psi(fine) = {psi.min(): .3e}  violations {len(viol)}  [{time.time()-t0:.1f}s]")
        if len(viol) == 0:
            break
        order = viol[np.argsort(psi[viol])][:add_per_round]
        taus = np.unique(np.concatenate([taus, fine_taus[order]]))
    slack = 2*np.pi*a_fn(taus) - sigmahat_matrix(taus, hu, K) @ s - margin
    active = taus[slack < 1e-7]
    log(f"  max s_k = {s.max():.4f} (S_max = {S_max}); min s_k = {s.min():.4f} (-d = {-d:.4f}); hu*sum|s| = {hu*np.abs(s).sum():.4f}")
    return dict(d=float(d), s=s, kappa_lp=float(2 - d), rounds=rnd+1, n_rows=len(taus), active=active,
                min_psi_fine=float(psi.min()), seconds=time.time() - t0, K=K, hu=hu, U=U, Tmax=Tmax)

def sigmahat_eval(taus, s, hu):
    K = len(s) - 1
    return sigmahat_matrix(taus, hu, K) @ s

def verify_dual(a_fn, a_lip, a_tail_min, s, d, hu, eta, c_rep, T_v, h0=0.01, max_depth=32, log=print):
    """Certify psi'(tau) = 2 pi a - sigmahat + 2 eta c/(c^2+tau^2) >= 0 on R.  a_lip(T) = sup_{[0,T]} |a'| (rigorous bound
    supplied by the instance); a_tail_min(T) = inf_{tau>=T} a.  Returns dict(ok, kappa_cert, ...)."""
    t0 = time.time()
    K = len(s) - 1; k = np.arange(K+1); mult = np.where(k == 0, 1.0, 2.0)
    S0 = float(np.sum(mult*np.abs(s))); S1 = float(np.sum(mult*np.abs(s)*k*hu))
    # |d/dtau sigmahat| <= hu [ (hu/2) * sup|(sinc^2)'| * S0 + S1 ],  sup|(sinc^2)'| < 0.55 (computed: max |2 sinc sinc'| = 0.5417 at x=1.17)
    L_sigma = hu*((hu/2)*0.55*S0 + S1)
    L_rep = 2*eta*c_rep*0.65/c_rep**2   # |d/dtau 2c/(c^2+tau^2)| = 4c tau/(c^2+tau^2)^2 <= (3sqrt3/8)/c^2 * 2 c ... bounded by 0.65*2/c
    L = 2*np.pi*a_lip(T_v) + L_sigma + L_rep
    def psi(t):
        t = np.asarray(t, float)
        return 2*np.pi*a_fn(t) - sigmahat_eval(t, s, hu) + 2*eta*c_rep/(c_rep**2 + t**2)
    # adaptive cells on [0, T_v]
    edges = np.arange(0.0, T_v + 1e-12, h0)
    if edges[-1] < T_v: edges = np.append(edges, T_v)
    lo, hi = edges[:-1], edges[1:]
    n_checked = 0; depth = 0; min_psi = np.inf; ok = True
    while len(lo) > 0 and depth < max_depth:
        vlo, vhi = psi(lo), psi(hi)
        m = np.minimum(vlo, vhi); min_psi = min(min_psi, float(m.min()))
        need = m < L*(hi - lo)/2
        n_checked += len(lo)
        bad_lo, bad_hi = lo[need], hi[need]
        if np.any(m[need] < 0):
            ok = False; log(f"  NEGATIVE psi' found at depth {depth}: min {m[need].min():.3e}"); break
        mid = (bad_lo + bad_hi)/2
        lo = np.concatenate([bad_lo, mid]); hi = np.concatenate([mid, bad_hi])
        depth += 1
    if len(lo) > 0 and ok:
        ok = False; log(f"  cells remaining at max depth: {len(lo)} (min psi' {min_psi:.3e})")
    # tail
    tail_sup = 4*S0/(hu*T_v**2)
    tail_ok = 2*np.pi*a_tail_min(T_v) - tail_sup > 0
    log(f"  verify: L = {L:.3f} (2pi a' {2*np.pi*a_lip(T_v):.3f}, sigma {L_sigma:.3f}), cells checked {n_checked}, depth {depth}, min psi' on grid {min_psi:.3e}, "
        f"tail: 2pi a_min({T_v}) = {2*np.pi*a_tail_min(T_v):.4f} vs sup|sigmahat| <= {tail_sup:.4f} -> {'ok' if tail_ok else 'FAIL'}  [{time.time()-t0:.1f}s]")
    return dict(ok=bool(ok and tail_ok), kappa_cert=float(2 - d - eta) if (ok and tail_ok) else None, d_prime=float(d + eta), eta=eta, c_rep=c_rep,
                L=float(L), S0=S0, S1=S1, cells=n_checked, depth=depth, min_psi=float(min_psi), tail_sup=float(tail_sup), T_v=T_v, seconds=time.time() - t0)

# ---------------------------------------------------------------- primal (squares family)
def abar_table(a_fn, hx, kmax, ngl=12):
    """abar_k = int a(k hx + v) (1 - |v|/hx)_+ dv, k = 0..kmax, by Gauss-Legendre on [-hx,0] and [0,hx]."""
    x, wgt = leggauss(ngl)
    out = np.zeros(kmax + 1)
    for sign in (-1, 1):
        v = sign*(x + 1)/2*hx; wv = wgt*hx/2*(1 - np.abs(v)/hx)
        for k in range(kmax + 1):
            out[k] += np.sum(wv*a_fn(k*hx + v))
    return out

def primal_squares(a_fn, X, hx, starts=None, maxiter=3000, log=print, abar=None):
    """fhat >= 0 piecewise constant on [0, 2X] with step hx (n = 2X/hx cells).  Returns best (value, c)."""
    t0 = time.time()
    n = int(round(2*X/hx))
    if abar is None: abar = abar_table(a_fn, hx, n)
    from scipy.linalg import toeplitz
    M = toeplitz(abar[:n])
    def R(c):
        q = c @ M @ c; nn = c @ c
        return 2 + q/nn
    def F(c):
        q = c @ M @ c; nn = c @ c
        return 2 + q/nn + (nn - 1)**2
    def grad(c):
        Mc = M @ c; q = c @ Mc; nn = c @ c
        return 2*(Mc*nn - q*c)/nn**2 + 4*(nn - 1)*c
    if starts is None:
        starts = []
        for frac in (1.0, 0.75, 0.5):      # Fejer-type: indicator of a sub-interval
            c0 = np.zeros(n); c0[:max(2, int(frac*n))] = 1.0; starts.append(c0)
        starts.append(1 - np.abs(np.linspace(-1, 1, n)))                # triangle
        starts.append(np.exp(-np.linspace(-2, 2, n)**2))                 # gaussian
    best = (np.inf, None)
    for i, c0 in enumerate(starts):
        c0 = c0/np.sqrt(c0 @ c0)
        res = minimize(F, c0, jac=grad, method="L-BFGS-B", bounds=[(0, None)]*n, options=dict(maxiter=maxiter, ftol=1e-15, gtol=1e-12))
        c = np.maximum(res.x, 0); val = R(c) if c @ c > 0 else np.inf
        log(f"  start {i}: R = {val:.8f}  (nit {res.nit}, {res.message[:40] if isinstance(res.message,str) else res.message})")
        if val < best[0]: best = (val, c)
    log(f"  primal best {best[0]:.8f}  [X = {X}, hx = {hx}, n = {n}, {time.time()-t0:.1f}s]")
    return dict(value=float(best[0]), c=best[1], X=X, hx=hx, n=n, seconds=time.time() - t0, abar=abar)

def primal_value_exact(a_fn, c, hx, ngl=24):
    """Re-evaluate R(c) with a finer abar quadrature (independent check of the reported upper bound)."""
    n = len(c); abar = abar_table(a_fn, hx, n, ngl=ngl)
    from scipy.linalg import toeplitz
    M = toeplitz(abar[:n])
    return float(2 + (c @ M @ c)/(c @ c))

def fejer_value(a_fn, T):
    from scipy.integrate import quad
    v, e = quad(lambda t: (1 - t/T)*a_fn(np.array([t]))[0], 0, T, limit=400)
    return 2 + 2*v
