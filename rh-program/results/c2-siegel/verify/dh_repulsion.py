#!/usr/bin/env python3
"""dh_repulsion.py -- Session 24 item 2(c), section 3 of siegel-world-scout.md: the Deuring-Heilbronn repulsion as a cone statement.

One-line consequence of the identity (0.3) for zeta_K: every share is nonnegative, so a real zero at beta_0 = 1 - delta_0 subtracts
  share_S := 2 Re ghat(-i y_0) = 2 (what * mu_{y_0})(0),  y_0 = 1/2 - delta_0,
from the budget available to every other orbit: any other orbit's share <= B_K(w) - share_S.  On the u-side,
  2 what(0) - share_S = 2 int w(u) [1 - cosh(y_0 u)/cosh(u/2)] du  -> 0 as delta_0 -> 0  (the pole share is what the Siegel zero consumes).
Quantified at the de la Vallee Poussin element w_{a,t} (confinement-note section 4), D = -20 and |D| = 1e6:
  (i) height t: complex orbit at (t, 1/2 - delta), share_4 = 4 sum_k c_k Re pi_a((1+k)t - iy); certified reach delta_max(t) = sup_eta
      of the largest delta with share_4 > B_K - share_S; compared with the reach without the planted zero (share_S = 0) and with the
      classical Deuring-Heilbronn shape c_2 log(1/delta_0)/log(q(2+t)) (Heath-Brown 1992 p. 266 Principle 2; c_2 < 2/3 p. 267).
  (ii) t = 0: a SECOND real zero at 1 - delta_1 given the first at 1 - delta_0: share_1(delta_1) > B_K - share_S: the excluded delta_1 range.
Budget: < 1 minute.
"""
import json, sys, time
import numpy as np
import mpmath as mp
t0 = time.time(); out = {}
mp.mp.dps = 25
def bracket_K(sigma, jt, logD):
    s = mp.mpc(sigma, jt)
    return float(2 * mp.re(1 / (s - 1) + 1 / s) + mp.re(mp.digamma(s / 2)) + mp.re(mp.digamma((s + 1) / 2)) - 2 * mp.log(mp.pi) + logD)
def B_K(eta, t, logD):
    sigma = 1 + eta
    return 3 * bracket_K(sigma, 0.0, logD) + 4 * bracket_K(sigma, t, logD) + bracket_K(sigma, 2 * t, logD)
CK = ((0, 3.0), (1, 2.0), (-1, 2.0), (2, 0.5), (-2, 0.5))
def re_pi(a, x, y): return (a + y) / ((a + y) ** 2 + x * x) + (a - y) / ((a - y) ** 2 + x * x)
def share_real(eta, t, delta0):
    a = 0.5 + eta; y = 0.5 - delta0
    return 2 * sum(c * re_pi(a, k * t, y) for k, c in CK)
def share_orbit(eta, t, delta):
    a = 0.5 + eta; y = 0.5 - delta
    return 4 * sum(c * re_pi(a, (1 + k) * t, y) for k, c in CK)
def what0(eta): return 8 * (1 / eta + 1 / (1 + eta))     # int w_{a,t} = 8 [1/(a - 1/2) + 1/(a + 1/2)] ... at t = 0 (q(0) = 8); general t: 3*(...) since int cos(ktu) e^{-a|u|}cosh(u/2) = Poisson at kt
def what0_t(eta, t):
    a = 0.5 + eta
    return 0.5 * sum(c * (2 * (a - 0.5) / ((a - 0.5) ** 2 + (k * t) ** 2) + 2 * (a + 0.5) / ((a + 0.5) ** 2 + (k * t) ** 2)) for k, c in CK)
# u-side check of the pole-minus-Siegel identity at t = 0: 2 what(0) - share_S = 2 int w (1 - k_{y0})  (closed form vs quadrature)
eta, d0 = 0.2, 0.01; a = 0.5 + eta; y0 = 0.5 - d0
lhs = 2 * what0_t(eta, 0.0) - share_real(eta, 0.0, d0)
rhs = 2 * float(mp.quad(lambda u: 8 * mp.exp(-a * abs(u)) * mp.cosh(u / 2) * (1 - mp.cosh(y0 * u) / mp.cosh(u / 2)), [-mp.inf, 0, mp.inf]))
print(f"u-side identity at t = 0, eta = 0.2, delta_0 = 0.01: 2 what(0) - share_S = {lhs:.10f}; 2 int w (1 - k_y0) = {rhs:.10f}; diff {lhs-rhs:.1e}")
out["uside_check"] = dict(lhs=lhs, rhs=rhs)
ETAS = np.exp(np.linspace(np.log(1e-4), np.log(1.0), 400))
def delta_max(t, logD, delta0):
    best = 0.0; best_eta = None
    for e in ETAS:
        budget = B_K(e, t, logD) - (share_real(e, t, delta0) if delta0 is not None else 0.0)
        if share_orbit(e, t, 1e-9) <= budget: continue
        lo, hi = 1e-9, 0.5
        if share_orbit(e, t, hi) > budget: dm = 0.5
        else:
            for _ in range(50):
                mid = 0.5 * (lo + hi)
                if share_orbit(e, t, mid) > budget: lo = mid
                else: hi = mid
            dm = lo
        if dm > best: best, best_eta = dm, e
    return best, best_eta
rows = []
print("(i) height t, dlVP element: certified reach delta_max for a complex orbit, without / with a planted real zero at 1 - delta_0")
for absD in (20, 10**6):
    logD = float(np.log(absD))
    for t in (28.0, 100.0, 1000.0, 1e4):
        L = np.log(absD * (2 + t))
        base, e0 = delta_max(t, logD, None)
        line = f"  |D| = {absD:.0e}, t = {t:6.0f}: none: {base:.6f} (x log(q(2+t)) = {base*L:.4f}, eta* {e0:.4f})"
        rec = dict(absD=absD, t=t, log_q_t=L, none=base, none_times_L=base * L)
        for d0 in (0.1, 0.01, 1e-3, 1e-4, 1e-6):
            dm, e = delta_max(t, logD, d0)
            rec[f"d0_{d0}"] = dm; rec[f"d0_{d0}_times_L"] = dm * L
            line += f" | d0={d0:g}: {dm:.6f} (x{dm*L:.3f}; DH shape (2/3)log(1/d0)/L = {(2/3)*np.log(1/d0)/L:.4f})"
        rows.append(rec); print(line)
out["height_t"] = rows
rows2 = []
print("(ii) t = 0, Poisson element: second real zero at 1 - delta_1 given the first at 1 - delta_0 -- the excluded range delta_1 < delta_1^max")
def delta1_max(logD, d0):
    best = 0.0
    for e in ETAS:
        budget = B_K(e, 0.0, logD) - share_real(e, 0.0, d0)
        f = lambda d1: share_real(e, 0.0, d1) - budget
        if f(1e-9) <= 0: continue
        if f(0.5) > 0: return 0.5
        lo, hi = 1e-9, 0.5
        for _ in range(50):
            mid = 0.5 * (lo + hi)
            if f(mid) > 0: lo = mid
            else: hi = mid
        best = max(best, lo)
    return best
for absD in (20, 10**6, 10**12):
    logD = float(np.log(absD)); line = f"  |D| = {absD:.0e}:"
    rec = dict(absD=absD)
    for d0 in (0.1, 0.01, 1e-3, 1e-4, 1e-6):
        dm = delta1_max(logD, d0); rec[f"d0_{d0}"] = dm
        line += f" d0={d0:g}: delta_1 < {dm:.5f} (x log|D| = {dm*logD:.3f}; DH (2/3)log(1/d0) = {(2/3)*np.log(1/d0):.3f})"
    rows2.append(rec); print(line)
out["t0_second_zero"] = rows2
out["runtime_s"] = time.time() - t0
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "dh_repulsion_out.json", "w"), indent=1)
print(f"done in {time.time()-t0:.1f}s")
