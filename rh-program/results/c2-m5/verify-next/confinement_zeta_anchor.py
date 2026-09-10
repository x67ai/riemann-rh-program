#!/usr/bin/env python3
"""confinement_zeta_anchor.py -- sanity computation for the zeta-anchored confinement theorem (candidate R1, version (a)).

Mechanism (PRICING-next-unit.md section 1.1): for every cone element, budget B(w) >= zero share Z(w) = 2 int what(s) Psi(s) ds,
Psi(s) := sum_{gamma > 0} mu_0(s - gamma), mu_0(x) = 1/cosh(pi x); a hypothetical orbit {+-t +- iy}, y = 1/2 - delta, has share
4 (what * mu_y)(t) = 2 int what(s) [mu_y(t - s) + mu_y(t + s)] ds.  If  mu_y(t - s) + mu_y(t + s) <= Psi(s) for all s, no cone
certificate at (t, y) exists at any bandwidth.  Near s = t the left side peaks at mu_y(0) = 1/cos(pi y) = 1/sin(pi delta).

For t in {1e4, 1e6}: fetch the zeros within |gamma - t| <= 8 (mpmath.zetazero), tabulate Psi on |s - t| <= 4, its minimum, the
mean density l/2pi (l = log(t/2pi)), and delta* solving 1/sin(pi delta*) = min Psi (the layer edge implied at this height);
compare with de la Vallee Poussin's certified 1 - sigma >= 1/(5.573412 log t) (Mossinghoff-Trudgian, PRICING.md section 4) and with 4/l.
Also checks the far-tail inequality on 14 <= s <= t - 4 numerically via the gap bound (max gap between consecutive zeros in the fetched range).
Budget: < 10 minutes (the zero fetch dominates).
"""
import time, json, sys
import numpy as np
import mpmath as mp

t0 = time.time()
out = {}
mp.mp.dps = 20

def N_approx(T):
    return (T / (2 * np.pi)) * np.log(T / (2 * np.pi * np.e)) + 7 / 8

def mu0(x):
    return 1.0 / np.cosh(np.pi * x)

def mu_y(x, y):
    x = np.asarray(x, dtype=float)
    ax = np.abs(x)
    small = ax < 10
    out = np.empty_like(ax)
    xs = np.where(small, ax, 0.0)
    out[small] = (2 * np.cos(np.pi * y) * np.cosh(np.pi * xs) / (np.cosh(2 * np.pi * xs) + np.cos(2 * np.pi * y)))[small]
    # |x| >= 10: cosh(pi x)/(cosh(2 pi x) + cos 2 pi y) = e^{-pi|x|} (1 + O(e^{-2 pi |x|}))
    out[~small] = 2 * np.cos(np.pi * y) * np.exp(-np.pi * ax[~small])
    return out

for t in (1e4, 1e6):
    l = np.log(t / (2 * np.pi))
    n0 = int(N_approx(t - 8))
    # locate: step the index until gamma_n <= t-8 < gamma_{n+1}
    g = float(mp.zetazero(n0).imag)
    while g > t - 8:
        n0 -= 1; g = float(mp.zetazero(n0).imag)
    while True:
        g2 = float(mp.zetazero(n0 + 1).imag)
        if g2 > t - 8:
            break
        n0 += 1; g = g2
    zs = []
    n = n0 + 1
    while True:
        gz = float(mp.zetazero(n).imag)
        if gz > t + 8:
            break
        zs.append(gz); n += 1
        if time.time() - t0 > 420:
            print("time guard hit"); break
    zs = np.array(zs)
    gaps = np.diff(zs)
    s = np.linspace(t - 4, t + 4, 1601)
    Psi = np.array([np.sum(mu0(ss - zs)) for ss in s])   # zeros farther than 8 contribute < e^{-4 pi} each; ignored (tail noted)
    Psi_min = float(Psi.min()); Psi_mean = float(Psi.mean())
    # delta* : 1/sin(pi delta) = Psi_min  ->  delta* = arcsin(1/Psi_min)/pi  (if Psi_min >= 1, else no confinement at this height)
    delta_star = float(np.arcsin(1 / Psi_min) / np.pi) if Psi_min >= 1 else None
    dlvp = 1 / (5.573412 * np.log(t))
    rec = dict(t=t, ell=float(l), n_zeros_in_window=int(len(zs)), first_index=n0 + 1, mean_gap=float(gaps.mean()), max_gap=float(gaps.max()),
               rvm_gap=float(2 * np.pi / l), Psi_min=Psi_min, Psi_mean=Psi_mean, mean_density_l_over_2pi=float(l / (2 * np.pi)),
               delta_star=delta_star, one_minus_sigma_layer=delta_star, four_over_ell=float(4 / l), dlvp_certified=float(dlvp))
    print(f"t={t:.0e}: l={l:.3f}, {len(zs)} zeros in |gamma-t|<=8 (indices from {n0+1}); mean gap {gaps.mean():.4f} (RvM {2*np.pi/l:.4f}), max gap {gaps.max():.4f}")
    print(f"   Psi on |s-t|<=4: min {Psi_min:.4f}, mean {Psi_mean:.4f}; mean density l/2pi = {l/(2*np.pi):.4f}")
    if delta_star is None:
        print(f"   Psi_min < 1: the pointwise domination fails for every delta at this height -> no confinement statement at t={t:.0e} (the layer is the whole strip)")
    else:
        print(f"   layer edge at this height: delta* = {delta_star:.4f} (1 - sigma >= delta* is uncertifiable by any cone test);  4/l = {4/l:.4f};  dlVP certified 1-sigma >= {dlvp:.5f}")
    # far-tail check: for s with 4 <= |s - t| <= 8 (inside fetched range), mu_y(t-s)+mu_y(t+s) <= Psi(s) at y = 1/2 - delta*? check at delta = 0.01 (deepest)
    y = 0.49
    s2 = np.linspace(t - 8, t + 8, 3201)
    Psi2 = np.array([np.sum(mu0(ss - zs)) for ss in s2])
    lhs = mu_y(t - s2, y) + mu_y(t + s2, y)
    far = np.abs(s2 - t) >= 4
    rec["far_tail_ok_4_to_8_at_y_0.49"] = bool(np.all(lhs[far] <= Psi2[far]))
    rec["far_tail_max_ratio"] = float(np.max(lhs[far] / Psi2[far]))
    print(f"   far tail 4<=|s-t|<=8 at y=0.49: max (mu_y(t-s)+mu_y(t+s))/Psi(s) = {np.max(lhs[far]/Psi2[far]):.3e} (<=1 required)")
    # near-t check at delta = delta*(1.05) and delta*(0.95): does domination hold / fail as predicted?
    if delta_star is not None:
        for fac in (0.9, 1.1):
            d = delta_star * fac; yy = 0.5 - d
            ok = bool(np.all(mu_y(t - s, yy) + mu_y(t + s, yy) <= Psi))
            print(f"   delta = {fac} * delta* = {d:.4f}: pointwise domination on |s-t|<=4 holds: {ok}")
            rec[f"domination_at_{fac}_delta_star"] = ok
    # exact layer edge at heights t' near t (zeros already fetched cover |s - t| <= 4 for |t' - t| <= 2):
    # least delta with max_s [mu_y(t'-s) + mu_y(t'+s) - Psi(s)] <= 0 on |s - t'| <= 2, by bisection (delta in (0, 1/2))
    exact = {}
    for tp in (t - 2.0, t - 1.0, t - 0.5, t, t + 0.5, t + 1.0, t + 2.0):
        sw = np.linspace(tp - 2, tp + 2, 1601)
        Psw = np.array([np.sum(mu0(ss - zs)) for ss in sw])
        Psi_at_t = float(np.sum(mu0(tp - zs)))
        def viol(d):
            yy = 0.5 - d
            return float(np.max(mu_y(tp - sw, yy) + mu_y(tp + sw, yy) - Psw))
        if viol(0.4999) > 0:
            dstar = None
        else:
            lo, hi = 1e-4, 0.4999
            if viol(lo) <= 0:
                dstar = lo
            else:
                for _ in range(40):
                    mid = 0.5 * (lo + hi)
                    if viol(mid) > 0: lo = mid
                    else: hi = mid
                dstar = hi
        exact[f"{tp:.1f}"] = dict(Psi_at_t=Psi_at_t, delta_star_exact=dstar, delta_star_times_ell=None if dstar is None else dstar * l)
        print(f"   t'={tp:.1f}: Psi(t') = {Psi_at_t:.4f};  exact layer edge delta*(t') = {dstar if dstar is None else round(dstar,4)}  (delta* * l = {None if dstar is None else round(dstar*l,3)};  2/l = {2/l:.3f})")
    rec["exact_layer_edge_near_t"] = exact
    out[f"t={t:.0e}"] = rec

# the mechanism's asymptotic constant: 1/sin(pi delta) = (l/2pi)(1 - eps)  ->  delta ~ 2/l ; with the pair factor 2 in the theorem's statement
# (orbit share 4 (what*mu_y)(t) versus Z = 2 int what Psi): 2 mu_y(0) <= 2 Psi  <=>  mu_y(0) <= Psi, i.e. 1/sin(pi delta) <= Psi_min ~ l/2pi  ->  delta >~ 2/l.
out["asymptotic_constant_note"] = "domination needs 1/sin(pi delta) <= Psi_min; with Psi_min ~ l/2pi (RH-strength local density) the layer is 1 - sigma <= (2/l)(1 + o(1))"
out["runtime_s"] = time.time() - t0
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "confinement_zeta_anchor_out.json", "w"), indent=1)
print(f"done in {time.time()-t0:.1f}s")
