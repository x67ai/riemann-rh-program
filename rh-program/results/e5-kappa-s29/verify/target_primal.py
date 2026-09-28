#!/usr/bin/env python3
"""target_primal.py -- rung 1: the primal (upper bounds on kappa) for the target density a (Lemma A1 closed form).
(i) Fejer family (reproduce 0.13597 at T = 11; continuous minimum); (ii) squares family w = |f|^2, fhat >= 0 piecewise
constant on [0, 2X] (Lemma A: certified upper bounds), several X and hx, starts include indicator (Fejer), triangle
(w = sinc^4, the product-of-Fejer case (iii)), trapezoid, gaussian; the best element saved to target_primal_best.json
with its shape described (where what sits relative to tau_0 and gamma_1; where w vanishes relative to log 2, log 3)."""
import numpy as np, json, time
from scipy.special import digamma
from kappa_pipeline import *
t0 = time.time(); out = {}; LOG = []
def log(m): print(m); LOG.append(m)
LOGPI = np.log(np.pi)
def a_fn(tau):
    tau = np.asarray(tau, float); z = 0.5j*tau
    return (np.real((1 - 1j*tau)*digamma(0.5 + z) + 1j*tau*digamma(1.0 + z)) - 1.0 - LOGPI)/(2*np.pi)
# (i) Fejer
from scipy.optimize import minimize_scalar
fe11 = fejer_value(a_fn, 11.0); res = minimize_scalar(lambda T: fejer_value(a_fn, T), bounds=(9, 13), method="bounded", options={"xatol": 1e-7})
log(f"(i) Fejer: T = 11 -> {fe11:.6f} (record 0.13597); continuous minimum {res.fun:.6f} at T* = {res.x:.4f}")
out["fejer_T11"] = fe11; out["fejer_min"] = [float(res.x), float(res.fun)]
# (ii) squares family
best = (np.inf, None)
for hx, Xs in ((0.02, (3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 10.0)), (0.01, None)):
    if Xs is None:
        Xs = (best[1]["X"] - 0.5, best[1]["X"], best[1]["X"] + 0.5)
    for X in Xs:
        n = int(round(2*X/hx))
        starts = []
        c0 = np.zeros(n); c0[:n] = 1.0; starts.append(c0)                        # Fejer (indicator)
        starts.append(1 - np.abs(np.linspace(-1, 1, n)))                          # triangle -> w = sinc^4
        starts.append(np.clip(2*(1 - np.abs(np.linspace(-1, 1, n))), 0, 1))       # trapezoid
        starts.append(np.exp(-np.linspace(-2, 2, n)**2))                          # gaussian
        if best[1] is not None and best[1]["hx"] == hx:                            # warm start from the previous best, resampled
            cb = best[1]["c"]; starts.append(np.interp(np.linspace(0, 1, n), np.linspace(0, 1, len(cb)), cb))
        r = primal_squares(a_fn, X=X, hx=hx, starts=starts, log=lambda m: None)
        ex = primal_value_exact(a_fn, r["c"], hx)
        log(f"(ii) X = {X:5.2f} hx = {hx}: best R = {r['value']:.7f} (24-pt re-evaluation {ex:.7f}), n = {r['n']}, {r['seconds']:.1f}s")
        out.setdefault("squares", []).append(dict(X=X, hx=hx, value=r["value"], exact=ex, n=r["n"]))
        if ex < best[0]: best = (ex, dict(X=X, hx=hx, c=r["c"]))
# best element: shape
X, hx, c = best[1]["X"], best[1]["hx"], best[1]["c"]; n = len(c); c = c/c.max()
log(f"BEST certified upper bound kappa_ub = {best[0]:.7f}  (X = {X}, hx = {hx})")
xs = (np.arange(n) + 0.5)*hx                                   # fhat cells on [0, 2X]
supp = xs[c > 1e-6*c.max()]
log(f"  fhat: support [{supp.min():.2f}, {supp.max():.2f}] (width {supp.max()-supp.min():.2f}); zero cells inside support: {int(np.sum((c < 1e-6) & (xs > supp.min()) & (xs < supp.max())))}")
# fhat profile at a few points
prof = [(float(x), float(v)) for x, v in zip(xs[::max(1, n//12)], c[::max(1, n//12)])]
log(f"  fhat profile (x, value/max): {[(round(x,2), round(v,3)) for x, v in prof]}")
# what = autocorrelation
what = np.correlate(c, c, mode="full")*hx/(2*np.pi); taus = np.arange(-(n-1), n)*hx
what = what/what.max()
half = what[taus >= 0]; tpos = taus[taus >= 0]
cum = np.cumsum(half)/np.sum(half)
log(f"  what: support [-{2*X:.1f}, {2*X:.1f}]; mass fraction on |tau| < tau_0 = 6.31: {cum[np.searchsorted(tpos, 6.31)]:.3f}; on |tau| < 11: {cum[min(len(cum)-1, np.searchsorted(tpos, 11.0))]:.3f}; what(gamma_1 = 14.13)/what(0) = {np.interp(14.1347, tpos, half):.4f}")
log(f"  what profile: {[(round(float(t),1), round(float(np.interp(t, tpos, half)),3)) for t in (0,2,4,6,6.31,8,10,12,14,16,18,20)]}")
# w = |f|^2 on the u-line
us = np.linspace(0, 6, 60001)
f = (c[None, :]*np.exp(1j*np.outer(us, xs))).sum(axis=1)*hx/(2*np.pi)
w = np.abs(f)**2; w = w/w[0]
def near(u0): i = np.argmin(np.abs(us - u0)); return float(w[i])
log(f"  w(u)/w(0) at u = log2, log3, log5, log7, log 11: {[round(near(np.log(p)),5) for p in (2,3,5,7,11)]}")
# local minima of w
mins = [float(us[i]) for i in range(1, len(us)-1) if w[i] < w[i-1] and w[i] < w[i+1] and us[i] < 4]
log(f"  local minima of w on (0, 4): {[round(m,3) for m in mins[:12]]}  (log2 = 0.693, log3 = 1.099, log5 = 1.609, log7 = 1.946)")
out["best"] = dict(kappa_ub=best[0], X=X, hx=hx, c=[float(v) for v in best[1]["c"]], fhat_support=[float(supp.min()), float(supp.max())],
                   what_mass_below_tau0=float(cum[np.searchsorted(tpos, 6.31)]), w_at_logp={str(p): near(np.log(p)) for p in (2,3,5,7,11)}, w_local_minima=mins[:12])
out["seconds"] = time.time() - t0
json.dump(out, open("target_primal_out.json", "w"), indent=1)
log(f"done in {time.time()-t0:.1f}s")
