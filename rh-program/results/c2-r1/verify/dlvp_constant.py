#!/usr/bin/env python3
"""dlvp_constant.py -- clause 7 of confinement-note.md: the de la Vallee Poussin element and its certified constant.

Element: w = e^{-a|u|} cosh(u/2) (3 + 4 cos tu + cos 2tu), a = sigma - 1/2 > 1/2, sigma = 1 + eta;  g = w/cosh(u/2).
  ghat(z) = sum_k c_k pi_a(z + k t),  pi_a(z) = 2a/(a^2 + z^2),  c_0 = 3, c_{+-1} = 2, c_{+-2} = 1/2.
  B(w) = sum_{j=0,1,2} d_j [ 2 Re(1/(s_j - 1) + 1/s_j) + Re psi(s_j/2) - log pi ],  d = (3, 4, 1),  s_j = sigma + i j t   (Lemma A).
  orbit share of a zero at beta + i t, y = beta - 1/2:  4 Re ghat(t - i y) = 4 sum_k c_k [ (a+y)/((a+y)^2 + x_k^2) + (a-y)/((a-y)^2 + x_k^2) ],
  x_k = (1+k) t;  the k = -1 term alone is >= 8/(a - y) = 8/(sigma - beta).
Proved bound (section 4): 1 - beta >= 0.143594/(5 l + C_t), l = log(t/2pi), C_t = 1.5274 + 13.5/t + 34/t^2  (t >= 28), hence > 1/(34.82 log t).
This script: (1) the constants; (2) the bracket bounds against exact values at sample t; (3) the element's EXACT certified reach
delta_max(t) = sup over eta of the largest delta = 1 - beta such that 4 Re ghat(t - i y) > B(w), against the proved bound.
Budget: < 1 minute.
"""
import json, sys, time
import numpy as np
import mpmath as mp

t0 = time.time(); out = {}
mp.mp.dps = 25
LOGPI = float(mp.log(mp.pi))
c_fac = (2 / np.sqrt(3) - 1) * (4 * np.sqrt(3) - 6)
out["two_over_sqrt3_minus_1"] = 2 / np.sqrt(3) - 1
out["four_sqrt3_minus_6"] = 4 * np.sqrt(3) - 6
out["product_0_143594"] = c_fac
out["c_certified_over_5"] = c_fac / 5
out["one_over_c"] = 5 / c_fac
psi1 = float(mp.digamma(1))
out["j0_constant_2_plus_psi1_minus_logpi"] = 2 + psi1 - LOGPI
out["total_constant_3x_plus_log2"] = 3 * (2 + psi1 - LOGPI) + np.log(2)
print(f"(2/sqrt3 - 1)(4 sqrt3 - 6) = {c_fac:.8f};  /5 = {c_fac/5:.8f};  1/(c/5) = {5/c_fac:.4f}")
print(f"j=0 bracket constant 2 + psi(1) - log pi = {2 + psi1 - LOGPI:.6f};  3*that + log 2 = {3*(2+psi1-LOGPI)+np.log(2):.6f}")

def bracket_exact(sigma, jt):
    s = mp.mpc(sigma, jt)
    return float(2 * mp.re(1 / (s - 1) + 1 / s) + mp.re(mp.digamma(s / 2)) - mp.log(mp.pi))

def B_exact(eta, t):
    sigma = 1 + eta
    return 3 * bracket_exact(sigma, 0.0) + 4 * bracket_exact(sigma, t) + bracket_exact(sigma, 2 * t)

def orbit_share(eta, t, delta):
    a = 0.5 + eta; y = 0.5 - delta
    s = 0.0
    for k, c in ((0, 3.0), (1, 2.0), (-1, 2.0), (2, 0.5), (-2, 0.5)):
        x = (1 + k) * t
        s += c * ((a + y) / ((a + y) ** 2 + x * x) + (a - y) / ((a - y) ** 2 + x * x))
    return 4 * s

# (2) bracket bounds vs exact
print("bracket_j exact vs bound log(jt/2pi) + 3/(jt) + 8/(jt)^2  (j>=1), and j=0 exact vs 2/eta + 0.2781:")
chk = []
for t in (28.0, 100.0, 1e4, 1e6):
    eta = 0.9282032 / (5 * np.log(t / (2 * np.pi)) + 2.06)
    sigma = 1 + eta
    b0 = bracket_exact(sigma, 0.0); b0_bound = 2 / eta + 0.2781
    row = dict(t=t, eta=eta, b0=b0, b0_bound=b0_bound)
    for j in (1, 2):
        bj = bracket_exact(sigma, j * t); bj_bound = np.log(j * t / (2 * np.pi)) + 3 / (j * t) + 8 / (j * t) ** 2
        row[f"b{j}"] = bj; row[f"b{j}_bound"] = bj_bound
    Bex = B_exact(eta, t)
    Bbd = 6 / eta + 5 * np.log(t / (2 * np.pi)) + 1.5274 + 13.5 / t + 34 / t ** 2
    row["B_exact"] = Bex; row["B_bound"] = Bbd
    chk.append(row)
    print(f"  t={t:.0e}: b0 {b0:.5f} <= {b0_bound:.5f}; b1 {row['b1']:.5f} <= {row['b1_bound']:.5f}; b2 {row['b2']:.5f} <= {row['b2_bound']:.5f}; B {Bex:.5f} <= {Bbd:.5f}: {Bex <= Bbd}")
out["bracket_checks"] = chk

# (3) exact certified reach of the element
def delta_max_for_eta(eta, t):
    # largest delta in (0, 1/2] with orbit_share(eta,t,delta) > B_exact(eta,t); share decreases in delta
    B = B_exact(eta, t)
    if orbit_share(eta, t, 1e-9) <= B:
        return 0.0
    lo, hi = 1e-9, 0.5
    if orbit_share(eta, t, hi) > B:
        return 0.5
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if orbit_share(eta, t, mid) > B: lo = mid
        else: hi = mid
    return lo

reach = []
for t in (28.0, 100.0, 1e3, 1e4, 1e6, 1e10, 1e20):
    l = np.log(t / (2 * np.pi))
    etas = np.exp(np.linspace(np.log(1e-3), np.log(1.0), 400))
    best = max(((delta_max_for_eta(e, t), e) for e in etas), key=lambda p: p[0])
    proved = c_fac / (5 * l + 1.5274 + 13.5 / t + 34 / t ** 2)
    rec = dict(t=t, ell=float(l), delta_max_exact=best[0], eta_star=best[1], delta_max_times_logt=best[0] * np.log(t),
               proved_lower_bound=float(proved), proved_times_logt=float(proved * np.log(t)), one_over_34_82_logt=float(1 / (34.8205 * np.log(t))))
    reach.append(rec)
    print(f"t={t:.0e}: exact reach of the element delta_max = {best[0]:.6f} (eta* = {best[1]:.4f}), delta_max*log t = {rec['delta_max_times_logt']:.4f};  proved bound {proved:.6f} (x log t = {rec['proved_times_logt']:.4f});  1/(34.82 log t) = {rec['one_over_34_82_logt']:.6f}")
out["exact_reach"] = reach
out["runtime_s"] = time.time() - t0
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "dlvp_constant_out.json", "w"), indent=1)
print(f"done in {time.time()-t0:.1f}s")
