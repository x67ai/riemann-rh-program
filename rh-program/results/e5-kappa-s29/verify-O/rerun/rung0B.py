#!/usr/bin/env python3
"""rung0B.py -- rung 0, instance B alone (see rung0.py for the instance), with the chunked verifier; saves the certificate."""
import numpy as np, json, time
from kappa_pipeline import *
t0 = time.time(); out = {}
def log(m): print(m, flush=True)
d0, U1, U2, ua, hnu, nua = 1.9, 0.7071, 1.4142, 1.7321, 0.3, 0.5
def sigmahat0(t):
    t = np.asarray(t, float); tt = np.where(np.abs(t) < 1e-9, 1e-9, t)
    trap = np.where(np.abs(t) < 1e-9, U1 + U2, 2*(np.cos(U1*tt) - np.cos(U2*tt))/((U2 - U1)*tt**2))
    return -d0*trap + nua*2*hnu*sinc2(hnu*t/2)*np.cos(ua*t)
a0 = lambda t: sigmahat0(t)/(2*np.pi); T0 = 60.0
p = lambda t: np.log(np.maximum(np.abs(np.asarray(t, float))/T0, 1.0))/(2*np.pi)
a1 = lambda t: a0(t) + p(t)
uu = np.linspace(-3, 3, 600001); du = uu[1] - uu[0]
sig0_u = -d0*np.clip((U2 - np.abs(uu))/(U2 - U1), 0, 1) + nua*np.maximum(0, 1 - np.abs(np.abs(uu) - ua)/hnu)
M1 = np.sum(np.abs(uu)*np.abs(sig0_u))*du
lipB = lambda T: (M1 + 1/T0)/(2*np.pi)*1.01
tailB = lambda T: p(T) - (4*d0/(U2 - U1) + 8*nua/hnu)/(T**2)/(2*np.pi)
log("instance B: dual LP hu = 0.01, U = 3, Tmax = 1000, margin 2e-5")
rB = dual_lp(a1, U=3.0, hu=0.01, Tmax=1000.0, coarse=(0.05, 40.0, 0.1), fine=(0.002, 40.0, 0.01), margin=2e-5, log=log)
np.save("rung0B_s.npy", rB["s"]); out["lp"] = dict(kappa_lp=rB["kappa_lp"], d=rB["d"], rounds=rB["rounds"], rows=rB["n_rows"], seconds=rB["seconds"])
json.dump(out, open("rung0B_out.json", "w"), indent=1)
cert = None
for eta in (5e-5, 2e-4, 8e-4):
    v = verify_dual(a1, lipB, tailB, rB["s"], rB["d"], 0.01, eta=eta, c_rep=1.0, T_v=1000.0, h0=0.01, log=log)
    if v["ok"]: cert = v; break
log(f"certified kappa_lb(B) = {cert['kappa_cert'] if cert else None}  (LP {rB['kappa_lp']:.7f})")
out["verify"] = cert; out["primal_B"] = 0.10000144
json.dump(out, open("rung0B_out.json", "w"), indent=1)
if cert: log(f"instance B bracket: [{cert['kappa_cert']:.6f}, 0.100001] vs known [0.1, 0.1 + delta] -> gap {0.10000144 - cert['kappa_cert']:.2e} ({100*(0.10000144 - cert['kappa_cert'])/0.1:.2f}%)")
log(f"done in {time.time()-t0:.1f}s")
