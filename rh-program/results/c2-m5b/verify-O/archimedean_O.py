#!/usr/bin/env python3
"""archimedean_O.py — the Opus reader's independent check of FORMULATION.md §0.2 (eq. (0.2), (0.2'), (0.3)).
Reader's own derivation (from C2 line 14's mu_inf, via the integral psi(z) = -gamma + int_0^inf (e^{-t} - e^{-zt})/(1 - e^{-t}) dt,
then t = 2u):  A_inf(g) := int ghat(tau) mu_inf(tau) dtau
      = -(gamma_E + log pi) g(0) - int_0^inf [g(u) e^{u/2} - g(0) e^{-u}] / sinh u du          (reader form R)
This differs in shape from the writer's (0.2) (which subtracts g(0), not g(0)e^{-u}, and carries log 4pi): the two agree iff
int_0^inf (1 - e^{-u})/sinh u du = 2 log 2 — checked below. Then the dilation law: with g_eps(u) = g(u/eps),
      A(g_eps) = g(0) log(1/eps) + a(g) + O(eps),
      a(g) = -int_0^1 (g(v) - g(0))/v dv + g(0) [K - c2 - gamma_E - log pi],  (supp g in [-1,1])
      K := int_0^1 (e^{w/2}/sinh w - 1/w) dw + int_1^inf e^{w/2}/sinh w dw,  c2 := int_0^inf (e^{u/2} - e^{-u})/sinh u du.
Quadrature: mpmath tanh-sinh; the tau-side integral with ghat computed by its own quadrature (not a closed form).
"""
import mpmath as mp, time
mp.mp.dps = 20
t0 = time.time()
gE, lp = mp.euler, mp.log(mp.pi)
def mu_inf(tau): return (mp.re(mp.digamma(mp.mpf(1)/4 + 1j*tau/2)) - lp) / (2*mp.pi)
def make(g, R):
    def ghat(tau): return 2*mp.quad(lambda u: g(u)*mp.cos(tau*u), [0, R/2, R])
    return ghat
import numpy as np
from scipy import integrate, special
def A_inf_tau(g, R, cut=400):
    """tau-side direct integral in double precision: ghat by QAWO (weight cos), mu_inf by scipy's complex digamma;
    integral over [0, cut] on panels of length pi/R; the tail beyond cut is bounded by the printed |ghat| decay."""
    gf = lambda u: float(g(mp.mpf(u)))
    gh = lambda t: 2*integrate.quad(gf, 0, R, weight='cos', wvar=t, limit=200, epsabs=1e-13)[0]
    mu = lambda t: (special.psi(0.25 + 0.5j*t).real - np.log(np.pi))/(2*np.pi)
    edges = np.arange(0, cut + 1e-9, np.pi/R); tot = 0.0
    for a, b in zip(edges[:-1], edges[1:]):
        tot += integrate.quad(lambda t: gh(t)*mu(t), a, b, epsabs=1e-13, limit=100)[0]
    return mp.mpf(2*tot), abs(gh(cut))
def A_inf_u(g, R):
    return -(gE + lp)*g(0) - mp.quad(lambda u: (g(u)*mp.exp(u/2) - g(0)*mp.exp(-u))/mp.sinh(u), [0, R/2, R, mp.inf])
print("identity check: int_0^inf (1 - e^{-u})/sinh u du =", mp.quad(lambda u: (1-mp.exp(-u))/mp.sinh(u), [0, mp.inf]), " vs 2 log 2 =", 2*mp.log(2))
c1 = mp.quad(lambda u: (mp.exp(u/2)-1)/mp.sinh(u), [0, mp.inf]); cA = mp.log(4*mp.pi) + gE + c1
print("c1 =", mp.nstr(c1, 14), "  c_A = log 4pi + gamma + c1 =", mp.nstr(cA, 14), "  (writer: 2.26394350735, 5.37218341922)")
bumps = {"(1-u^2)^3 on [-1,1]": (lambda u: (1-u**2)**3 if abs(u) < 1 else mp.mpf(0), 1),
         "(1-(u/2)^2)^4 on [-2,2]": (lambda u: (1-(u/2)**2)**4 if abs(u) < 2 else mp.mpf(0), 2)}
for name, (g, R) in bumps.items():
    au = A_inf_u(g, R)
    for cut in (200, 400):
        at, gtail = A_inf_tau(g, R, cut)
        print(f"{name}: u-side (reader form R) {mp.nstr(au, 12)}; tau-side direct, |tau| <= {cut}: {mp.nstr(at, 12)}; diff {mp.nstr(at-au, 3)}; |ghat(cut)| = {gtail:.1e}  [{time.time()-t0:.0f} s]", flush=True)
# dilation law for g = (1-u^2)^3
g = lambda u: (1-u**2)**3 if abs(u) < 1 else mp.mpf(0)
K = mp.quad(lambda w: mp.exp(w/2)/mp.sinh(w) - 1/w, [0, 1]) + mp.quad(lambda w: mp.exp(w/2)/mp.sinh(w), [1, mp.inf])
c2 = mp.quad(lambda u: (mp.exp(u/2)-mp.exp(-u))/mp.sinh(u), [0, mp.inf])
a_pred = -mp.quad(lambda v: (g(v)-1)/v, [0, 1]) + K - c2 - gE - lp
print("predicted a(g) for (1-u^2)^3 (reader closed form; int_0^1 (g-1)/v = -11/12):", mp.nstr(a_pred, 12))
for eps in ("0.5", "0.1", "0.02", "0.005", "0.001", "0.0002"):
    e = mp.mpf(eps); ge = lambda u, e=e: g(u/e)
    A = mp.quad(lambda u: ge(u)*2*mp.cosh(u/2), [-e, 0, e]) + A_inf_u(ge, e)
    print(f"  eps = {eps:>7}: A(g_eps) - log(1/eps) = {mp.nstr(A - mp.log(1/e), 10)}; minus a_pred = {mp.nstr(A - mp.log(1/e) - a_pred, 4)}")
print(f"total {time.time()-t0:.1f} s")
