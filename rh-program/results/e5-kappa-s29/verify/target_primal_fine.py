#!/usr/bin/env python3
"""target_primal_fine.py -- rung 1 refinement: the squares family at hx = 0.005 (n = 3000) around X = 7.5, warm-started from the
hx = 0.01 best (resampled to the same support), plus 6 random-perturbation restarts; reports whether 0.0009991 moves."""
import numpy as np, json, time
from scipy.special import digamma
from kappa_pipeline import *
t0 = time.time(); LOGPI = np.log(np.pi)
def a_fn(tau):
    tau = np.asarray(tau, float); z = 0.5j*tau
    return (np.real((1 - 1j*tau)*digamma(0.5 + z) + 1j*tau*digamma(1.0 + z)) - 1.0 - LOGPI)/(2*np.pi)
best = json.load(open("target_primal_out.json"))["best"]; cb = np.array(best["c"]); Xb = best["X"]; hxb = best["hx"]
rng = np.random.default_rng(1)
res = {}
for X, hx in ((7.5, 0.005), (8.0, 0.005)):
    n = int(round(2*X/hx))
    xs_new = (np.arange(n) + 0.5)*hx; xs_old = (np.arange(len(cb)) + 0.5)*hxb
    warm = np.interp(xs_new, xs_old, cb, left=0, right=0)          # same support in x
    starts = [warm] + [np.maximum(warm*(1 + 0.2*rng.standard_normal(n)), 0) for _ in range(4)] + [np.maximum(warm + 0.05*rng.random(n)*warm.max(), 0)]
    r = primal_squares(a_fn, X=X, hx=hx, starts=starts, log=lambda m: None)
    ex = primal_value_exact(a_fn, r["c"], hx)
    print(f"X = {X}, hx = {hx}, n = {n}: best {r['value']:.8f} (re-evaluated {ex:.8f})  [{time.time()-t0:.1f}s]", flush=True)
    res[f"X{X}_hx{hx}"] = dict(value=r["value"], exact=ex, n=n)
    if ex < best["kappa_ub"] - 1e-9:
        best = dict(kappa_ub=ex, X=X, hx=hx, c=[float(v) for v in r["c"]]); print("  improved; saved to target_primal_fine_best.json")
        json.dump(best, open("target_primal_fine_best.json", "w"))
json.dump(res, open("target_primal_fine_out.json", "w"), indent=1)
print(f"done in {time.time()-t0:.1f}s")
