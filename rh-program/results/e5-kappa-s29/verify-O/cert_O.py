#!/usr/bin/env python3
"""cert_O.py -- Opus reader, E5: independent re-certification of a Theorem-D' certificate at fixed eps (NOTE section 5).
Certificate file: s (hat coefficients, half-width hu, nodes u_k = k hu, k = 0..K).  sigma = sum_k s_k H_k (H_0 one hat, H_k the
symmetric pair) is the piecewise-linear interpolant of the s_k, so sigma >= -d_eff du with d_eff := max(0, -min s_k).
Claim certified:  psi(tau) := 2 pi [ a(tau) + r Psi_G(tau) ] - sigmahat(tau) + 2 eta/(1 + tau^2) >= 0 for all real tau,
r = 2(1-eps)/eps, G = first NZ zeros (reader's own mpmath.zetazero call).  Then (Theorem D for a_eps, repair
sigma' = sigma - eta e^{-|u|} >= -(d_eff + eta)):  kappa >= eps (2 - d_eff - eta).
Reader's method (different from the writer's first-derivative Lipschitz cells): a SECOND-derivative bound per cell,
  psi >= min(psi(x0), psi(x1)) - M h^2/8 - ERR on [x0, x1],  h = x1 - x0,
  M = 2 pi M_a + 2 pi r pi^2 e^{pi h} min(Psi(x0), Psi(x1)) + M_sigma + 4 eta,
  M_a = 2 zeta(3, 1/4)/(8 pi) >= sup|A''| >= sup|a''|   (A'' = -(1/8pi) Re psi''(1/4 + ir/2), |psi''(z)| <= 2 sum 1/(n + 1/4)^3; mu_0 has mass 1),
  |d^2/dtau^2 sech(pi(tau - g))| <= pi^2 sech(pi(tau - g)), and log Psi_G is pi-Lipschitz (so sup_cell Psi <= e^{pi h} min endpoint values),
  M_sigma = hu [ (hu/2)^2 D2 S0 + 2 (hu/2) D1 S1 + S2 ],  D1 = sup|(sinc^2)'|, D2 = sup|(sinc^2)''| (computed, x 1.01),
  S_j = sum_k mult_k |s_k| u_k^j;   |d^2/dtau^2 (2/(1+tau^2))| <= 4.
Tail tau >= T_v: 2 pi a(T_v) - 4 S0/(hu T_v^2) > 0 (a increasing: Lemma A3; Psi_G >= 0 and the repair dropped).
a(tau): float64 closed form (2.1), checked against mpmath at 4002 points to 9e-14 (aform_O_run.log); ERR = 1e-9 absorbs all
float64 evaluation error (a: 2pi*1e-13; sigmahat: 801 terms of size <= 1.2 -> < 1e-12; Psi: relative 1e-15 x r).
Usage: python3 cert_O.py <npy> <hu> <eps> <d_tilde_from_json> [eta ...]"""
import numpy as np, mpmath as mp, json, time, sys, os
from scipy.special import digamma
t0 = time.time()
def log(m): print(m, flush=True)
npy, hu, eps, d_json = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
etas = [float(x) for x in sys.argv[5:]] or [0.0, 2e-5]
NZ = int(os.environ.get("NZ", "200")); T_v = 1000.0; ERR = 1e-9
s = np.load(npy); K = len(s) - 1; k = np.arange(K + 1); uk = k*hu; mult = np.where(k == 0, 1.0, 2.0)
S0 = float(np.sum(mult*np.abs(s))); S1 = float(np.sum(mult*np.abs(s)*uk)); S2 = float(np.sum(mult*np.abs(s)*uk**2))
d_eff = max(0.0, -float(s.min()))
log(f"certificate {os.path.basename(npy)}: K = {K}, U = {K*hu:g}, hu = {hu}, eps = {eps}; min s = {s.min():.10f} -> d_eff = {d_eff:.10f} (writer's LP d = {d_json:.10f}); S0 = {S0:.4f}, S1 = {S1:.4f}, S2 = {S2:.4f}")
mp.mp.dps = 20
zeros = np.array([float(mp.im(mp.zetazero(j))) for j in range(1, NZ + 1)])
log(f"{NZ} zeros from mpmath.zetazero: gamma_1 = {zeros[0]:.12f}, gamma_{NZ} = {zeros[-1]:.6f}  [{time.time()-t0:.0f}s]")
LOGPI = np.log(np.pi)
def a_fn(t):
    z = 0.5j*t
    return (np.real((1 - 1j*t)*digamma(0.5 + z) + 1j*t*digamma(1.0 + z)) - 1.0 - LOGPI)/(2*np.pi)
def Psi(t):
    out = np.empty(len(t))
    for i in range(0, len(t), 4000):
        tt = t[i:i+4000, None]
        x1 = np.minimum(np.abs(np.pi*(tt - zeros)), 700); x2 = np.minimum(np.abs(np.pi*(tt + zeros)), 700)
        out[i:i+4000] = 0.5*(1/np.cosh(x1) + 1/np.cosh(x2)).sum(axis=1)
    return out
def sighat(t):
    out = np.empty(len(t))
    for i in range(0, len(t), 4000):
        tt = t[i:i+4000]
        C = np.cos(np.outer(tt, uk)) @ (mult*s)
        if not np.all(np.isfinite(C)):  # guard against the spurious-BLAS path: recompute without BLAS
            C = (np.cos(np.outer(tt, uk))*(mult*s)).sum(axis=1)
        assert np.all(np.isfinite(C))
        out[i:i+4000] = hu*np.sinc(hu*tt/(2*np.pi))**2*C
    return out
x = np.linspace(0, 12, 1200001); sc2 = np.sinc(x/np.pi)**2
D1 = 1.01*np.abs(np.gradient(sc2, x)).max(); D2 = 1.01*np.abs(np.gradient(np.gradient(sc2, x), x)).max()
M_a = float(2*mp.zeta(3, mp.mpf(1)/4)/(8*mp.pi))
M_sig = hu*((hu/2)**2*D2*S0 + 2*(hu/2)*D1*S1 + S2)
r = 2*(1 - eps)/eps
_rng = np.random.default_rng(3); _tt = np.concatenate([_rng.uniform(0, 40, 1500), _rng.uniform(40, 1000, 500)])
_ref = np.array([hu*np.sinc(hu*t/(2*np.pi))**2*float(np.sum(np.cos(t*uk)*(mult*s), dtype=np.longdouble)) for t in _tt])
log(f'sighat BLAS vs longdouble loop at 2000 points: max diff {np.abs(sighat(_tt) - _ref).max():.2e}')
log(f"D1 = {D1:.4f}, D2 = {D2:.4f}, M_a = {M_a:.4f}, M_sigma = {M_sig:.3f}, r = {r:.6f}")
out = dict(npy=os.path.basename(npy), hu=hu, eps=eps, d_eff=d_eff, d_json=d_json, S0=S0, S1=S1, S2=S2, M_sigma=M_sig, M_a=M_a, NZ=NZ, runs={})
tail = 2*np.pi*float(a_fn(np.array([T_v]))[0]) - 4*S0/(hu*T_v**2)
log(f"tail beyond T_v = {T_v}: 2 pi a(T_v) - 4 S0/(hu T_v^2) = {tail:.4f} ({'ok' if tail > 0 else 'FAIL'})")
for eta in etas:
    te = time.time()
    def psi(t): return 2*np.pi*(a_fn(t) + r*Psi(t)) - sighat(t) + 2*eta/(1 + t**2)
    edges = np.arange(0.0, T_v + 1e-12, 0.01); lo, hi = edges[:-1], edges[1:]
    vlo_all = None; ncell = 0; depth = 0; ok = True; gmin = np.inf; gmin_at = None; worst_bound = np.inf
    while len(lo) and depth < 30:
        pts = np.unique(np.concatenate([lo, hi])); vals = psi(pts); Pv = Psi(pts)
        vl = vals[np.searchsorted(pts, lo)]; vh = vals[np.searchsorted(pts, hi)]
        Pl = Pv[np.searchsorted(pts, lo)]; Ph = Pv[np.searchsorted(pts, hi)]
        h = hi - lo; m = np.minimum(vl, vh)
        assert np.all(np.isfinite(m)), 'non-finite psi'
        if m.min() < gmin: gmin = float(m.min()); gmin_at = float(lo[m.argmin()])
        if np.any(m < 0): ok = False; log(f"  eta = {eta:g}: NEGATIVE psi = {m.min():.3e} at tau = {lo[m.argmin()]:.5f}"); break
        M = 2*np.pi*M_a + 2*np.pi*r*np.pi**2*np.exp(np.pi*h)*np.minimum(Pl, Ph) + M_sig + 4*eta
        lb = m - M*h**2/8 - ERR
        good = lb >= 0; ncell += int(good.sum())
        if good.any(): worst_bound = min(worst_bound, float(lb[good].min()))
        bl, bh = lo[~good], hi[~good]; mid = (bl + bh)/2
        lo = np.concatenate([bl, mid]); hi = np.concatenate([mid, bh]); depth += 1
    if len(lo) and ok: ok = False; log(f"  eta = {eta:g}: {len(lo)} cells unresolved at depth {depth}")
    ok = ok and tail > 0
    kap = eps*(2 - d_eff - eta) if ok else None
    log(f"  eta = {eta:g}: {'CERTIFIED' if ok else 'not certified'}; cells closed {ncell}, max depth {depth}, min psi at cell ends {gmin:.4e} (tau = {gmin_at}), "
        f"smallest certified lower bound on a cell {worst_bound:.3e}; kappa >= eps(2 - d_eff - eta) = {kap}  [{time.time()-te:.0f}s]")
    out["runs"][f"{eta:g}"] = dict(ok=bool(ok), kappa_cert=kap, cells=ncell, depth=depth, min_psi=gmin, min_psi_at=gmin_at, min_cell_lb=worst_bound, seconds=time.time()-te)
    json.dump(out, open(os.environ.get("OUT", "cert_O_out.json"), "w"), indent=1)
out["tail"] = tail; out["seconds"] = time.time() - t0
json.dump(out, open(os.environ.get("OUT", "cert_O_out.json"), "w"), indent=1); log(f"done in {time.time()-t0:.1f}s")
