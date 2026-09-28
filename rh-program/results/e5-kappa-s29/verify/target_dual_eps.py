#!/usr/bin/env python3
"""target_dual_eps.py -- rung 2 (final form): the mixed certificate class of Theorem D' at FIXED eps, which is the plain LP
for the density  a_eps := a + 2 ((1-eps)/eps) Psi_G  (NOTE section 5):  kappa >= eps * kappa_plain(a_eps), where
kappa_plain(a_eps) = 2 - d~ is certified by Theorem D applied to a_eps (sigma~ >= -d~, psi~ = 2 pi a_eps - sigmahat~ >= 0).
Verification: adaptive cells with a PER-CELL Lipschitz bound (the Psi_G part varies by at most e^{pi h} across a cell of
width h: |Psi_G'| <= pi Psi_G, so L_cell = 2 pi A_LIP + L_sigma + 1.3 eta + 4 pi ((1-eps)/eps) pi e^{pi h} max(Psi(lo), Psi(hi)));
tail beyond T_v: 2 pi a(T_v) - 4 S0/(hu T_v^2) > 0 (Psi_G >= 0 dropped).  Usage: python3 target_dual_eps.py U hu eps1 eps2 ..."""
import numpy as np, json, time, sys, os, mpmath as mp
from scipy.special import digamma
from kappa_pipeline import *
t0 = time.time(); LOGPI = np.log(np.pi)
def log(m): print(m, flush=True)
def a_fn(tau):
    tau = np.asarray(tau, float); z = 0.5j*tau
    return (np.real((1 - 1j*tau)*digamma(0.5 + z) + 1j*tau*digamma(1.0 + z)) - 1.0 - LOGPI)/(2*np.pi)
NZ = int(os.environ.get("E5_NZ", "200"))
zeros = np.array([float(mp.zetazero(k).imag) for k in range(1, NZ + 1)])
def Psi_fn(tau):
    tau = np.asarray(tau, float); outp = np.zeros_like(tau)
    for i in range(0, len(tau), 5000):
        t = tau[i:i+5000, None]
        outp[i:i+5000] = 0.5*(1/np.cosh(np.clip(np.pi*(t - zeros[None, :]), -700, 700)) + 1/np.cosh(np.clip(np.pi*(t + zeros[None, :]), -700, 700))).sum(axis=1)
    return outp
A_LIP = 0.377896*1.05
U = float(sys.argv[1]); hu = float(sys.argv[2]); eps_list = [float(x) for x in sys.argv[3:]]
OUT = os.environ.get("E5_OUT", f"target_dual_eps_U{U:g}_hu{hu:g}_out.json"); out = {}
log(f"{NZ} zeros; U = {U}, hu = {hu}, eps list {eps_list}")

def verify_eps(s, d, eps, eta, c_rep, T_v, h0=0.01, max_depth=40):
    K = len(s) - 1; k = np.arange(K+1); mult = np.where(k == 0, 1.0, 2.0)
    S0 = float(np.sum(mult*np.abs(s))); S1 = float(np.sum(mult*np.abs(s)*k*hu))
    L_base = 2*np.pi*A_LIP + hu*((hu/2)*0.55*S0 + S1) + 1.3*eta/c_rep
    r = 2*(1 - eps)/eps
    def psi(t):
        t = np.asarray(t, float)
        return 2*np.pi*(a_fn(t) + r*Psi_fn(t)) - sigmahat_eval(t, s, hu) + 2*eta*c_rep/(c_rep**2 + t**2)
    edges = np.arange(0.0, T_v + 1e-12, h0)
    if edges[-1] < T_v: edges = np.append(edges, T_v)
    lo, hi = edges[:-1], edges[1:]; n_checked = 0; depth = 0; min_psi = np.inf; ok = True
    while len(lo) > 0 and depth < max_depth:
        vlo, vhi = psi(lo), psi(hi); Plo, Phi = Psi_fn(lo), Psi_fn(hi)
        h = hi - lo
        L = L_base + 2*np.pi*r*np.pi*np.exp(np.pi*h)*np.maximum(Plo, Phi)
        m = np.minimum(vlo, vhi); min_psi = min(min_psi, float(m.min()))
        need = m < L*h/2; n_checked += len(lo)
        if np.any(m[need] < 0):
            ok = False; log(f"    NEGATIVE psi at depth {depth}: min {m[need].min():.3e} near tau = {lo[need][np.argmin(m[need])]:.4f}"); break
        bad_lo, bad_hi = lo[need], hi[need]; mid = (bad_lo + bad_hi)/2
        lo = np.concatenate([bad_lo, mid]); hi = np.concatenate([mid, bad_hi]); depth += 1
    if len(lo) > 0 and ok: ok = False; log(f"    cells remaining at max depth: {len(lo)}")
    tail_sup = 4*S0/(hu*T_v**2); tail_ok = 2*np.pi*float(a_fn(T_v)) - tail_sup > 0
    log(f"    verify: eta = {eta:.1e}, cells {n_checked}, depth {depth}, min psi~ {min_psi:.3e}, tail {2*np.pi*float(a_fn(T_v)):.3f} vs {tail_sup:.3f} -> {'ok' if tail_ok else 'FAIL'}")
    return dict(ok=bool(ok and tail_ok), eta=eta, cells=n_checked, depth=depth, min_psi=float(min_psi), tail_sup=float(tail_sup), S0=S0, S1=S1)

for eps in eps_list:
    tc = time.time(); r = 2*(1 - eps)/eps
    a_eps = lambda t, r=r: a_fn(t) + r*Psi_fn(t)
    log(f"=== eps = {eps:.1e} (relaxation weight 2(1-eps)/eps = {r:.3e})")
    res = dual_lp(a_eps, U=U, hu=hu, Tmax=1000.0, coarse=(0.05, 40.0, 0.05), fine=(0.002, 40.0, 0.01), margin=2e-5, viol_tol=1e-7, time_limit=1500.0, log=log)
    if res is None: continue
    np.save(f"target_dual_eps_s_U{U:g}_hu{hu:g}_eps{eps:g}.npy", res["s"])
    kt = res["kappa_lp"]; log(f"  kappa~_lp = {kt:.6f}  ->  kappa >= eps * kappa~ = {eps*kt:.4e} (uncertified); active taus: {np.round(res['active'][:30], 3).tolist()} ({len(res['active'])})")
    cert = None
    if kt > 0:
        for eta in (2e-5, 1e-4, 4e-4, 1.6e-3, 6.4e-3):
            if eta >= kt: break
            v = verify_eps(res["s"], res["d"], eps, eta, 1.0, 1000.0)
            if v["ok"]: cert = dict(v, kappa_tilde_cert=kt - eta, kappa_cert=eps*(kt - eta)); break
    log(f"  CERTIFIED: {cert is not None}; kappa_cert = {cert['kappa_cert'] if cert else None}  [{time.time()-tc:.1f}s]")
    s = res["s"]; K = res["K"]; uk = np.arange(K+1)*hu
    out[f"eps{eps:g}"] = dict(eps=eps, U=U, hu=hu, d_tilde=res["d"], kappa_tilde_lp=kt, kappa_lp=eps*kt, rounds=res["rounds"], rows=res["n_rows"], lp_seconds=res["seconds"],
                             active=[float(x) for x in res["active"]], verify=cert, hole=[float(uk[s < -res["d"] + 1e-9].min()), float(uk[s < -res["d"] + 1e-9].max())] if np.any(s < -res["d"] + 1e-9) else None,
                             n_pos=int((s > 1e-9).sum()), max_s=float(s.max()), argmax_u=float(uk[np.argmax(s)]))
    json.dump(out, open(OUT, "w"), indent=1)
out["seconds"] = time.time() - t0; json.dump(out, open(OUT, "w"), indent=1); log(f"done in {time.time()-t0:.1f}s")
