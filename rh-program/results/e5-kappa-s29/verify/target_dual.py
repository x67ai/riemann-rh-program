#!/usr/bin/env python3
"""target_dual.py -- rung 2: the dual LP (lower bounds on kappa) for the target density a, with CERTIFICATION.
Configurations (U, hu, Tmax) run in sequence; each: cutting-plane LP (kappa_lp), then repair (eta, c_rep) and the
pointwise verification of psi' >= 0 (adaptive Lipschitz cells on [0, T_v], analytic tail beyond) -> kappa_cert.
a from Lemma A1 (closed form); sup|a'| on [0,T]: a'(tau) = (1/2pi) Re{ -i psi(1/2+i tau/2) + (1-i tau)(i/2) psi'(1/2+i tau/2)
+ i psi(1+i tau/2) + i tau (i/2) psi'(1+i tau/2) } computed by mpmath on a grid, max * 1.05 (a' is positive, peaks near
tau ~ 0.6 and decays like 1/(2 pi tau)); a_min(T) = a(T) by Lemma A3.  Usage: python3 target_dual.py [config index list]"""
import numpy as np, json, time, sys, mpmath as mp
from scipy.special import digamma
from kappa_pipeline import *
t0 = time.time(); out = {}; LOG = []
def log(m): print(m, flush=True); LOG.append(m)
LOGPI = np.log(np.pi)
def a_fn(tau):
    tau = np.asarray(tau, float); z = 0.5j*tau
    return (np.real((1 - 1j*tau)*digamma(0.5 + z) + 1j*tau*digamma(1.0 + z)) - 1.0 - LOGPI)/(2*np.pi)
# sup |a'| : mpmath derivative on a grid
mp.mp.dps = 25
def a_mp(t):
    t = mp.mpf(t); z = mp.mpc(0, t/2)
    return (mp.re((1 - mp.mpc(0, t))*mp.digamma(mp.mpf('0.5') + z) + mp.mpc(0, t)*mp.digamma(1 + z)) - 1 - mp.log(mp.pi))/(2*mp.pi)
grid = np.concatenate([np.linspace(0, 5, 501), np.linspace(5, 100, 191), np.linspace(100, 1000, 91)])
ap = np.array([float(mp.diff(a_mp, float(t))) for t in grid])
imax = np.argmax(ap)
log(f"sup a' on [0,1000] (grid) = {ap.max():.6f} at tau = {grid[imax]:.3f}; a'(1000) = {ap[-1]:.6f} vs 1/(2 pi 1000) = {1/(2*np.pi*1000):.6f}; a' positive on grid: {bool(np.all(ap > 0))}")
A_LIP = float(ap.max()*1.05)
a_lip = lambda T: A_LIP
a_tail_min = lambda T: float(a_fn(T))
out["sup_a_prime"] = float(ap.max()); out["a_lip_used"] = A_LIP
configs = [dict(U=3.0, hu=0.02, Tmax=1000.0, coarse=(0.05, 40.0, 0.1), eta=5e-5, margin=2e-5),
           dict(U=4.0, hu=0.01, Tmax=1000.0, coarse=(0.05, 40.0, 0.05), eta=5e-5, margin=2e-5),
           dict(U=6.0, hu=0.01, Tmax=1000.0, coarse=(0.05, 40.0, 0.05), eta=5e-5, margin=2e-5),
           dict(U=8.0, hu=0.01, Tmax=1000.0, coarse=(0.05, 40.0, 0.05), eta=5e-5, margin=2e-5),
           dict(U=12.0, hu=0.02, Tmax=1000.0, coarse=(0.05, 40.0, 0.05), eta=5e-5, margin=2e-5),
           dict(U=16.0, hu=0.02, Tmax=1000.0, coarse=(0.05, 40.0, 0.05), eta=5e-5, margin=2e-5),
           dict(U=24.0, hu=0.04, Tmax=1000.0, coarse=(0.05, 40.0, 0.05), eta=5e-5, margin=2e-5),
           dict(U=6.0, hu=0.01, Tmax=1000.0, coarse=(0.05, 40.0, 0.5), eta=5e-5, margin=2e-5),
           dict(U=8.0, hu=0.01, Tmax=1000.0, coarse=(0.05, 40.0, 0.5), eta=5e-5, margin=2e-5),
           dict(U=12.0, hu=0.02, Tmax=1000.0, coarse=(0.05, 40.0, 0.5), eta=5e-5, margin=2e-5)]
sel = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else list(range(4))
import os
OUTNAME = os.environ.get('E5_OUT', 'target_dual_out.json')
for ci in sel:
    cf = configs[ci]; tc = time.time()
    log(f"=== config {ci}: U = {cf['U']}, hu = {cf['hu']}, Tmax = {cf['Tmax']}, coarse {cf['coarse']}")
    r = dual_lp(a_fn, U=cf["U"], hu=cf["hu"], Tmax=cf["Tmax"], coarse=cf["coarse"], fine=(0.002, 40.0, 0.01), margin=cf["margin"], time_limit=1500.0, log=log)
    if r is None: continue
    log(f"  kappa_lp = {r['kappa_lp']:.7f}; active taus: {np.round(r['active'][:30], 3).tolist()} ... ({len(r['active'])} total)")
    v = verify_dual(a_fn, a_lip, a_tail_min, r["s"], r["d"], cf["hu"], eta=cf["eta"], c_rep=1.0, T_v=cf["Tmax"], h0=0.01, log=log)
    log(f"  CERTIFIED: {v['ok']}  kappa_cert = {v['kappa_cert']}  (d' = {v['d_prime']:.7f})  [{time.time()-tc:.1f}s]")
    s = r["s"]; K = r["K"]; uk = np.arange(K+1)*cf["hu"]
    hole = uk[s < -r["d"] + 1e-6]; pos = uk[s > 1e-6]
    log(f"  certificate shape: s_k = -d (full deficit) on u in [{hole.min() if len(hole) else float('nan'):.3f}, {hole.max() if len(hole) else float('nan'):.3f}] ({len(hole)} nodes); s_k > 0 at {len(pos)} nodes, first few u: {np.round(pos[:12],3).tolist()}; max s = {s.max():.3f} at u = {uk[np.argmax(s)]:.3f}; sum mult*s*hu (net mass of sigma) = {float((np.where(np.arange(K+1)==0,1,2)*s).sum()*cf['hu']):.4f}")
    out[f"config{ci}"] = dict(cf=cf, kappa_lp=r["kappa_lp"], d=r["d"], rounds=r["rounds"], rows=r["n_rows"], lp_seconds=r["seconds"],
                             active=[float(x) for x in r["active"]], verify={k: (v[k] if not isinstance(v[k], np.ndarray) else None) for k in v},
                             s=[float(x) for x in s], hole=[float(hole.min()), float(hole.max())] if len(hole) else None)
    json.dump(out, open(OUTNAME, "w"), indent=1)
    np.save(f"target_dual_s_config{ci}.npy", s)
out["seconds"] = time.time() - t0
json.dump(out, open(OUTNAME, "w"), indent=1)
log(f"done in {time.time()-t0:.1f}s")
