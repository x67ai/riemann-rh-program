#!/usr/bin/env python3
"""confinement_edge.py -- the zeta-anchored domination (clause 2, corrected hypothesis (D)) at heights 1e6, 1e7, 1e8.

Hypothesis (D) of confinement-note.md section 2:  2[mu_y(t-s) + mu_y(t+s)] <= Psi(s) + Psi(-s) for all s >= 0,
Psi(s) = sum_{gamma>0} 1/cosh(pi(s - gamma)).  Local content: 2/sin(pi delta) <= Psi(t).
For each height: fetch the zeros in |gamma - t| <= 10 (mpmath.zetazero), tabulate Psi on |s - t| <= 6 (zeros beyond +-10
contribute < 2e^{-4pi} each, noted), report min/mean of Psi against l/2pi (l = log(t/2pi)),
 (a) the LITERAL contract condition at s = -t (fails: left side 1/sin(pi delta) >= 1, right side Psi(-t) < 1e-19);
 (b) the corrected EXACT edge delta*(t') at seven t' near t: least delta with (D) on |s - t'| <= 6 (outside the window
     the tails are covered by Lemma P and Theorem G); reported with delta* l, against 4/l;
 (c) the window-minimum version of clause 3(i): delta_3 = (1/pi) arcsin(2/(min Psi - eps3)) if min Psi > 2;
 (d) the pricing's literal edge (1/sin = Psi on the window only) for comparison, to document the factor 2.
Budget: <= 9 minutes (time guard); one process.
"""
import json, sys, time
import numpy as np
import mpmath as mp

t0 = time.time(); out = {}
mp.mp.dps = 15
GUARD = 500.0
eps3 = 4.03 * np.exp(-4 * np.pi)

def N_approx(T):
    return (T / (2 * np.pi)) * np.log(T / (2 * np.pi * np.e)) + 7 / 8
def mu0(x):
    return 1.0 / np.cosh(np.pi * x)
def mu_y(x, y):
    x = np.abs(np.asarray(x, dtype=float))
    small = x < 10
    r = np.empty_like(x)
    xs = np.where(small, x, 0.0)
    r[small] = (2 * np.cos(np.pi * y) * np.cosh(np.pi * xs) / (np.cosh(2 * np.pi * xs) + np.cos(2 * np.pi * y)))[small]
    r[~small] = 2 * np.cos(np.pi * y) * np.exp(-np.pi * x[~small])
    return r

for t in (1e6, 1e7, 1e8):
    if time.time() - t0 > GUARD:
        print(f"time guard: skipping t = {t:.0e}"); break
    l = np.log(t / (2 * np.pi))
    n0 = int(N_approx(t - 10))
    g = float(mp.zetazero(n0).imag)
    while g > t - 10:
        n0 -= 1; g = float(mp.zetazero(n0).imag)
    while float(mp.zetazero(n0 + 1).imag) <= t - 10:
        n0 += 1
    zs = []; n = n0 + 1; aborted = False
    while True:
        gz = float(mp.zetazero(n).imag)
        if gz > t + 10: break
        zs.append(gz); n += 1
        if time.time() - t0 > GUARD + 60:
            aborted = True; print("time guard hit inside zero fetch"); break
    zs = np.array(zs)
    if aborted or len(zs) < 5:
        print(f"t={t:.0e}: insufficient zeros fetched ({len(zs)}), skipping"); break
    gaps = np.diff(zs)
    s = np.linspace(t - 6, t + 6, 2401)
    Psi = np.array([np.sum(mu0(ss - zs)) for ss in s])
    rec = dict(t=t, ell=float(l), n_zeros=int(len(zs)), first_index=n0 + 1, mean_gap=float(gaps.mean()), max_gap=float(gaps.max()), rvm_gap=float(2 * np.pi / l),
               Psi_min=float(Psi.min()), Psi_max=float(Psi.max()), Psi_mean=float(Psi.mean()), mean_density=float(l / (2 * np.pi)), fetch_time_s=time.time() - t0)
    print(f"t={t:.0e}: l = {l:.3f}, {len(zs)} zeros in |gamma - t| <= 10 (indices from {n0+1}); mean gap {gaps.mean():.4f} (RvM {2*np.pi/l:.4f}), max gap {gaps.max():.4f}; {time.time()-t0:.0f}s")
    print(f"   Psi on |s - t| <= 6: min {Psi.min():.4f}, mean {Psi.mean():.4f}, max {Psi.max():.4f};  mean density l/2pi = {l/(2*np.pi):.4f}")
    # (a) literal contract condition at s = -t
    Psi_minus_t_bound = float(np.sum(2 * np.exp(-np.pi * (t + zs))) + 2 * np.exp(-np.pi * (t + 14.13)))
    rec["literal_condition_at_s_minus_t"] = dict(lhs_ge=1.0, Psi_minus_t_le=Psi_minus_t_bound)
    print(f"   (a) literal contract condition at s = -t: left side >= mu_y(0) = 1/sin(pi delta) >= 1, right side Psi(-t) <= {Psi_minus_t_bound:.1e}: FAILS for every delta")
    # (b) corrected exact edge
    exact = {}
    for tp in (t - 2.0, t - 1.0, t - 0.5, t, t + 0.5, t + 1.0, t + 2.0):
        sw = np.linspace(tp - 6, tp + 6, 2401)
        Psw = np.array([np.sum(mu0(ss - zs)) for ss in sw])
        Psi_tp = float(np.sum(mu0(tp - zs)))
        def viol(d):
            yy = 0.5 - d
            return float(np.max(2 * (mu_y(tp - sw, yy) + mu_y(tp + sw, yy)) - Psw))
        def viol_literal(d):
            yy = 0.5 - d
            return float(np.max(mu_y(tp - sw, yy) + mu_y(tp + sw, yy) - Psw))
        def edge(vf):
            if vf(0.5) > 0:
                return None
            lo, hi = 1e-4, 0.5
            if vf(lo) <= 0: return lo
            for _ in range(50):
                mid = 0.5 * (lo + hi)
                if vf(mid) > 0: lo = mid
                else: hi = mid
            return hi
        d_corr = edge(viol); d_lit = edge(viol_literal)
        exact[f"{tp:.1f}"] = dict(Psi_at_tp=Psi_tp, delta_star_corrected=d_corr, delta_star_times_ell=None if d_corr is None else d_corr * l,
                                   delta_star_literal_window_only=d_lit, delta_lit_times_ell=None if d_lit is None else d_lit * l)
        print(f"   (b) t'={tp:.1f}: Psi(t') = {Psi_tp:.4f};  corrected edge delta* = {None if d_corr is None else round(d_corr,4)} (delta* l = {None if d_corr is None else round(d_corr*l,3)}; 4/l = {4/l:.3f});  literal-on-window edge = {None if d_lit is None else round(d_lit,4)} (x l = {None if d_lit is None else round(d_lit*l,3)})")
    rec["exact_edges"] = exact
    # (c) window-minimum clause 3(i)
    w4 = np.abs(s - t) <= 4
    Pmin4 = float(Psi[w4].min())
    rec["Psi_min_window_4"] = Pmin4
    if Pmin4 - eps3 > 2:
        d3 = float(np.arcsin(2 / (Pmin4 - eps3)) / np.pi)
        rec["delta_3_window_min"] = d3
        print(f"   (c) clause 3(i) window-min form: min_(|s-t|<=4) Psi = {Pmin4:.4f} > 2 -> every delta >= {d3:.4f} uncertifiable (delta_3 l = {d3*l:.3f})")
    else:
        rec["delta_3_window_min"] = None
        print(f"   (c) clause 3(i) window-min form: min_(|s-t|<=4) Psi = {Pmin4:.4f} <= 2 -> the uniform form says nothing at this height (a pair weighs two on-line zeros)")
    out[f"t={t:.0e}"] = rec

out["runtime_s"] = time.time() - t0
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "confinement_edge_out.json", "w"), indent=1)
print(f"done in {time.time()-t0:.1f}s")
