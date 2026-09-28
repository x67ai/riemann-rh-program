#!/usr/bin/env python3
"""target_dual_mixed.py -- rung 2': the MIXED dual (Theorem D', NOTE section 5): K0's convex combination (weight 1 - eps on the
zero side, eps on the archimedean side) plus a grid correction sigma_g >= -D on [-U, U]; certificate kappa >= 2 eps - D.
Psi_G from the first 200 zeros (mpmath), Psi_G := 0 beyond gamma_200 (a valid subset).  Then repair + verification with an
escalating eta.  Usage: python3 target_dual_mixed.py [config indices]"""
import numpy as np, json, time, sys, os, mpmath as mp
from scipy.special import digamma
from kappa_pipeline import *
t0 = time.time(); out = {}
def log(m): print(m, flush=True)
LOGPI = np.log(np.pi)
def a_fn(tau):
    tau = np.asarray(tau, float); z = 0.5j*tau
    return (np.real((1 - 1j*tau)*digamma(0.5 + z) + 1j*tau*digamma(1.0 + z)) - 1.0 - LOGPI)/(2*np.pi)
NZ = int(os.environ.get("E5_NZ", "200"))
zeros = np.array([float(mp.zetazero(k).imag) for k in range(1, NZ + 1)])
log(f"{NZ} zeros loaded, gamma_1 = {zeros[0]:.6f}, gamma_{NZ} = {zeros[-1]:.4f}  [{time.time()-t0:.1f}s]")
def Psi_fn(tau):
    tau = np.asarray(tau, float); outp = np.zeros_like(tau)
    for i in range(0, len(tau), 5000):
        t = tau[i:i+5000, None]
        x = np.pi*(t - zeros[None, :]); y = np.pi*(t + zeros[None, :])
        outp[i:i+5000] = 0.5*(1/np.cosh(np.clip(x, -700, 700)) + 1/np.cosh(np.clip(y, -700, 700))).sum(axis=1)
    return outp
# Lipschitz bounds
A_LIP = 0.377896*1.05
tg = np.arange(0, zeros[-1] + 5, 0.001); Pg = Psi_fn(tg); PL = float(np.abs(np.diff(Pg)/0.001).max()*1.1)
log(f"sup|Psi_G'| (grid 0.001, x1.1) = {PL:.4f}; sup Psi_G = {Pg.max():.4f}")
a_lip = lambda T: A_LIP; a_tail_min = lambda T: float(a_fn(T))
configs = [dict(U=4.0, hu=0.01, Tmax=1000.0), dict(U=6.0, hu=0.01, Tmax=1000.0), dict(U=8.0, hu=0.01, Tmax=1000.0),
           dict(U=12.0, hu=0.02, Tmax=1000.0), dict(U=3.0, hu=0.02, Tmax=1000.0), dict(U=16.0, hu=0.02, Tmax=1000.0)]
sel = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else [0, 1, 2]
OUTNAME = os.environ.get("E5_OUT", "target_dual_mixed_out.json")
for ci in sel:
    cf = configs[ci]; tc = time.time()
    log(f"=== mixed config {ci}: U = {cf['U']}, hu = {cf['hu']}, Tmax = {cf['Tmax']}")
    r = dual_lp_mixed(a_fn, Psi_fn, U=cf["U"], hu=cf["hu"], Tmax=cf["Tmax"], coarse=(0.05, 40.0, 0.05), fine=(0.002, 40.0, 0.01), margin=2e-5, log=log)
    if r is None: continue
    np.save(f"target_dual_mixed_s_config{ci}.npy", r["s"])
    log(f"  kappa_lp = {r['kappa_lp']:.6e} (eps = {r['eps']:.6e}, D = {r['D']:.6e}); active taus: {np.round(r['active'][:40], 3).tolist()} ({len(r['active'])} total)")
    cert = None
    for eta in (2e-5, 5e-5, 2e-4, 8e-4):
        if eta >= r["kappa_lp"]: break
        v = verify_dual_mixed(a_fn, a_lip, a_tail_min, Psi_fn, PL, r["s"], r["eps"], r["D"], cf["hu"], eta=eta, c_rep=1.0, T_v=cf["Tmax"], h0=0.01, log=log)
        if v["ok"]: cert = v; break
    log(f"  CERTIFIED: {cert is not None}  kappa_cert = {cert['kappa_cert'] if cert else None}  [{time.time()-tc:.1f}s]")
    s = r["s"]; K = r["K"]; uk = np.arange(K+1)*cf["hu"]
    hole = uk[s < -r["D"] + 1e-9] if r["D"] > 0 else np.array([])
    log(f"  shape: full-deficit nodes {len(hole)} on [{hole.min() if len(hole) else float('nan'):.3f}, {hole.max() if len(hole) else float('nan'):.3f}]; s>0 at {int((s > 1e-9).sum())} nodes; max s = {s.max():.4e} at u = {uk[np.argmax(s)]:.3f}")
    out[f"config{ci}"] = dict(cf=cf, kappa_lp=r["kappa_lp"], eps=r["eps"], D=r["D"], rounds=r["rounds"], rows=r["n_rows"], lp_seconds=r["seconds"],
                             active=[float(x) for x in r["active"]], verify=cert, s=[float(x) for x in s])
    json.dump(out, open(OUTNAME, "w"), indent=1)
out["seconds"] = time.time() - t0
json.dump(out, open(OUTNAME, "w"), indent=1)
log(f"done in {time.time()-t0:.1f}s")
