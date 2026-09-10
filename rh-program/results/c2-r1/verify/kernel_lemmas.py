#!/usr/bin/env python3
"""kernel_lemmas.py -- numerical record for Lemma P, Lemma D, Lemma A and Lemma K of confinement-note.md.

Conventions: what(xi) = int w(u) e^{-i u xi} du;  k_y(u) = cosh(y u)/cosh(u/2);  mu_y = (1/2pi) * FT[k_y];
closed form mu_y(xi) = 2 cos(pi y) cosh(pi xi) / (cosh(2 pi xi) + cos(2 pi y)).
Checks:
  P(i)   closed form against direct quadrature of the transform; positivity; monotonicity.
  P(ii)  mass 1, peak 1/cos(pi y) = 1/sin(pi delta).
  P(iii) tail constant: max_{|xi|>=1} mu_y(xi) e^{pi|xi|} / sin(pi delta) against 2(1+e^{-2pi})/(1-e^{-2pi})^2.
  P(iv)  k_y(u) e^{delta|u|} <= 2.
  D      |Re psi(z) - log|z|| <= 3/(2|Im z|) on a grid with Re z in [1/4, 1], |Im z| in [1, 1e6];
         Gauss's integral psi(z) = int_0^inf (e^{-tau}/tau - e^{-z tau}/(1 - e^{-tau})) dtau against mpmath.digamma.
  A      (1/2pi) int pi_a(r - x) [Re psi(1/4 + i r/2) - log pi] dr  ==  Re psi((1/2 + a + i x)/2) - log pi,
         pi_a(r) = 2a/(a^2 + r^2), at several (a, x).
  K      transform of the Poisson kernel; the de la Vallee Poussin element's what >= 0 and w >= 0 at sample points.
Budget: < 2 minutes. Output: kernel_lemmas_out.json.
"""
import json, sys, time
import numpy as np
import mpmath as mp

t0 = time.time()
out = {}
mp.mp.dps = 30

def mu_closed(xi, y):
    return 2 * np.cos(np.pi * y) * np.cosh(np.pi * xi) / (np.cosh(2 * np.pi * xi) + np.cos(2 * np.pi * y))

# ---- P(i): closed form checked by Fourier inversion: int mu_y(xi) cos(u xi) dxi == k_y(u) = cosh(yu)/cosh(u/2) ------
# (the direct transform of k_y converges slowly for y near 1/2 -- decay e^{-delta|u|} -- while mu_y decays like 2e^{-pi|xi|})
rec = []
for y in (0.0, 0.25, 0.4, 0.45, 0.49):
    for uu in (0.0, 0.7, 3.0, 12.0):
        f = lambda x: 2 * mp.cos(mp.pi * y) * mp.cosh(mp.pi * x) / (mp.cosh(2 * mp.pi * x) + mp.cos(2 * mp.pi * y)) * mp.cos(uu * x)
        q = mp.quad(f, [-30, -5, -1, 0, 1, 5, 30])
        k = mp.cosh(y * uu) / mp.cosh(uu / 2)
        rec.append(dict(y=y, u=uu, inversion_integral=float(q), k_y=float(k), diff=float(abs(q - k))))
maxdiff_i = max(r["diff"] for r in rec)
out["P_i_closed_form_by_fourier_inversion"] = dict(max_abs_diff=maxdiff_i, samples=rec)
print(f"P(i)  closed form by Fourier inversion (int mu_y cos(u xi) dxi vs k_y(u)): max |diff| = {maxdiff_i:.3e} over {len(rec)} samples")

# monotonicity and positivity on a grid
xi = np.linspace(0, 12, 120001)
mono_ok = True; pos_ok = True
for y in (0.0, 0.25, 0.4, 0.45, 0.49, 0.499):
    m = mu_closed(xi, y)
    pos_ok &= bool(np.all(m > 0))
    mono_ok &= bool(np.all(np.diff(m) <= 0))
out["P_i_positive"] = pos_ok; out["P_i_monotone_decreasing_in_abs_xi"] = mono_ok
print(f"P(i)  positive: {pos_ok}; strictly decreasing in |xi| on grid: {mono_ok}")

# ---- P(ii): mass and peak ------------------------------------------------------------------------
xi2 = np.linspace(-14, 14, 560001)
mass = {}; peak = {}
for y in (0.0, 0.25, 0.4, 0.45, 0.49):
    m = mu_closed(xi2, y)
    mass[y] = float(np.trapezoid(m, xi2))
    peak[y] = (float(mu_closed(0.0, y)), float(1 / np.cos(np.pi * y)), float(1 / np.sin(np.pi * (0.5 - y))))
out["P_ii_mass"] = mass; out["P_ii_peak_closed_vs_1_over_cos_vs_1_over_sin"] = peak
print("P(ii) mass:", {k: round(v, 12) for k, v in mass.items()})
print("P(ii) peak (closed, 1/cos(pi y), 1/sin(pi delta)):", peak)

# ---- P(iii): tail constant ----------------------------------------------------------------------
xi3 = np.linspace(1, 12, 220001)
cP_sharp = 2 * (1 + np.exp(-2 * np.pi)) / (1 - np.exp(-2 * np.pi)) ** 2
ratios = {}
for y in (0.0, 0.25, 0.4, 0.45, 0.49, 0.499, 0.4999):
    d = 0.5 - y
    r = mu_closed(xi3, y) * np.exp(np.pi * xi3) / np.sin(np.pi * d)
    ratios[y] = float(r.max())
out["P_iii_tail_ratio_max_over_xi_ge_1"] = ratios
out["P_iii_cP_sharp_at_xi_1"] = float(cP_sharp)
out["P_iii_first_bound_ok"] = bool(all(np.all(mu_closed(xi3, y) <= np.sin(np.pi * (0.5 - y)) * np.cosh(np.pi * xi3) / np.sinh(np.pi * xi3) ** 2 + 1e-15) for y in ratios))
print(f"P(iii) max_(|xi|>=1) mu_y e^(pi|xi|)/sin(pi delta): {ratios}")
print(f"P(iii) 2(1+e^-2pi)/(1-e^-2pi)^2 = {cP_sharp:.6f}  (c_P := 2.012 covers it); first bound sin(pi d) cosh/sinh^2 holds: {out['P_iii_first_bound_ok']}")

# ---- P(iv): k_y e^{delta|u|} <= 2 ---------------------------------------------------------------
u = np.linspace(-60, 60, 240001)
kmax = {}
for y in (0.0, 0.25, 0.4, 0.45, 0.49):
    d = 0.5 - y
    kmax[y] = float(np.max(np.cosh(y * u) / np.cosh(u / 2) * np.exp(d * np.abs(u))))
out["P_iv_max_k_y_e_delta_u"] = kmax
print("P(iv) max k_y(u) e^(delta|u|):", kmax, "(<= 2 required)")

# ---- Lemma D: |Re psi(z) - log|z|| <= 3/(2|Im z|); Gauss integral -----------------------------
worst = 0.0; worst_pt = None
for x in (0.25, 0.5, 0.75, 1.0):
    for yv in (1, 2, 5, 14, 28, 100, 1e3, 1e4, 1e6):
        z = mp.mpc(x, yv)
        lhs = abs(mp.re(mp.digamma(z)) - mp.log(abs(z)))
        bound = mp.mpf(3) / (2 * yv)
        ratio = float(lhs / bound)
        if ratio > worst:
            worst = ratio; worst_pt = (x, yv, float(lhs), float(bound))
out["D_max_ratio_lhs_over_bound"] = worst; out["D_worst_point"] = worst_pt
print(f"D     max |Re psi(z) - log|z|| / (3/(2|Im z|)) = {worst:.4f} at (Re, Im, lhs, bound) = {worst_pt}  (< 1 required)")
# Gauss integral check
gauss = []
for z in (mp.mpc(0.25, 0.0), mp.mpc(0.25, 7.0), mp.mpc(0.75, 50.0), mp.mpc(0.5, 0.0)):
    def f(tau):
        if tau < mp.mpf('1e-8'):
            return (z - mp.mpf(3) / 2) + tau * (mp.mpf(5) / 12 + z / 2 - z * z / 2)  # Taylor expansion of the integrand at tau = 0
        return mp.exp(-tau) / tau - mp.exp(-z * tau) / (1 - mp.exp(-tau))
    val = mp.quad(f, [0, mp.mpf('1e-8'), mp.mpf('0.01'), 0.5, 2, 10, 60, 200])
    gauss.append(dict(z=str(z), integral=str(val), digamma=str(mp.digamma(z)), diff=float(abs(val - mp.digamma(z)))))
out["D_gauss_integral_check"] = gauss
print("D     Gauss integral vs digamma, |diff|:", [g["diff"] for g in gauss])
# monotonicity of psi on (0, 1]: psi(1) = -gamma
out["psi_1"] = float(mp.digamma(1)); out["psi_half"] = float(mp.digamma(0.5))
print(f"      psi(1) = {out['psi_1']:.10f} (= -Euler gamma), psi(1/2) = {out['psi_half']:.10f}; 2 + psi(1) - log pi = {2 + out['psi_1'] - float(mp.log(mp.pi)):.6f}")

# ---- Lemma A: Poisson evaluation of the archimedean integral ----------------------------------
mp.mp.dps = 20
def F(r):
    return mp.re(mp.digamma(mp.mpf(1) / 4 + 1j * r / 2)) - mp.log(mp.pi)
recA = []
for (a, x) in ((0.6, 0.0), (0.6, 30.0), (1.0, 100.0), (0.55, 1000.0), (1.5, 0.0)):
    integrand = lambda th: F(x + a * mp.tan(th)) / mp.pi          # r = x + a tan(theta): Poisson weight becomes dtheta/pi
    val = mp.quad(integrand, [-mp.pi / 2, -1.5, -1.0, 0, 1.0, 1.5, mp.pi / 2])
    rhs = mp.re(mp.digamma((mp.mpf(1) / 2 + a + 1j * x) / 2)) - mp.log(mp.pi)
    recA.append(dict(a=a, x=x, poisson_integral=float(val), rhs=float(rhs), diff=float(abs(val - rhs))))
    print(f"A     a={a}, x={x}: Poisson integral = {float(val):.10f}, Re psi((1/2+a+ix)/2) - log pi = {float(rhs):.10f}, diff = {float(abs(val-rhs)):.2e}")
out["A_poisson_evaluation"] = recA

# ---- Lemma K / clause 7: Poisson kernel transform; dlVP element positivity --------------------
pk = 2 * mp.quadosc(lambda r: 2 * 0.7 / (0.7 ** 2 + r ** 2) * mp.cos(r * 1.3), [0, mp.inf], omega=1.3)
out["K_poisson_kernel_transform"] = dict(value=float(pk), expected=float(2 * mp.pi * mp.exp(-0.7 * 1.3)))
print(f"K     int 2a/(a^2+r^2) cos(r xi) dr at a=0.7, xi=1.3: {float(pk):.10f} vs 2 pi e^(-a xi) = {out['K_poisson_kernel_transform']['expected']:.10f}")
# dlVP element w = e^{-a|u|} cosh(u/2) (3 + 4 cos tu + cos 2tu), a > 1/2; what = sum of Poisson kernels with weights (1/2)c_k at +-kt, b = a -+ 1/2
a, tt = 0.7, 5.0
def what_dlvp(xi):
    s = 0.0
    for k, c in ((0, 3.0), (1, 2.0), (-1, 2.0), (2, 0.5), (-2, 0.5)):
        for b in (a - 0.5, a + 0.5):
            s += 0.5 * c * 2 * b / (b * b + (xi + k * tt) ** 2)
    return s
ug = np.linspace(-40, 40, 400001)
w_dl = np.exp(-a * np.abs(ug)) * np.cosh(ug / 2) * (3 + 4 * np.cos(tt * ug) + np.cos(2 * tt * ug))
out["K_dlvp_w_min"] = float(w_dl.min())
xig = np.linspace(-200, 200, 40001)
out["K_dlvp_what_min"] = float(min(what_dlvp(x) for x in xig))
# check what_dlvp formula against direct quadrature at two frequencies
for xi in (0.0, 5.0):
    per = 2 * mp.pi / tt
    pts = [k * per for k in range(0, int(420 / per) + 1)]      # e^{-(a-1/2) u} = e^{-0.2 u} < 1e-36 at u = 420
    q = 2 * mp.quad(lambda uu: mp.exp(-a * uu) * mp.cosh(uu / 2) * (3 + 4 * mp.cos(tt * uu) + mp.cos(2 * tt * uu)) * mp.cos(uu * xi), pts)
    print(f"K     dlVP what({xi}) formula {what_dlvp(xi):.8f} vs quadrature {float(q):.8f}")
    out[f"K_dlvp_what_check_xi_{xi}"] = dict(formula=float(what_dlvp(xi)), quad=float(q))
print(f"K     dlVP element (a=0.7, t=5): min w on grid = {out['K_dlvp_w_min']:.3e} (>= 0), min what on grid = {out['K_dlvp_what_min']:.3e} (> 0)")

out["runtime_s"] = time.time() - t0
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "kernel_lemmas_out.json", "w"), indent=1, default=str)
print(f"done in {time.time()-t0:.1f}s")
