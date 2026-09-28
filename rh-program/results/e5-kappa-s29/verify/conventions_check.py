#!/usr/bin/env python3
"""conventions_check.py -- E5 writer's own reproduction of the record's conventions (PRICING-next-unit.md section 0,
verify-next/budget_floor.py) plus a CLOSED FORM for the archimedean density a = mu_0 * A, derived by the writer:

  A(r)  = (1/2pi)[Re psi(1/4 + i r/2) - log pi],   mu_0(xi) = sech(pi xi),   a := mu_0 * A.
  Closed form (derived in NOTE.md section 2, Lemma A1):
     a(tau) = (1/2pi) [ Re{ (1 - i tau) psi(1/2 + i tau/2) + i tau psi(1 + i tau/2) } - 1 - log pi ].
  Derivation: Re psi(1/4 + i r/2) = -gamma + sum_n [1/(n+1) - 2 c_n/(c_n^2 + r^2)], c_n = 2n + 1/2;
  mu_0 * [c/(c^2 + .^2)] = Re[psi((c+3/2+i tau)/2) - psi((c+1/2+i tau)/2)]  (Fourier: sech(u/2) e^{-c|u|});
  the regularized double sum gives (1-2z)psi(1/2+z) + 2z psi(1+z) + gamma - 1 with z = i tau/2 (the -1 is the
  boundary term of the rearrangement, (N+1) sum_{m>N} 1/((m+a)(m+b)) -> 1).
Checks: (i) closed form vs direct quadrature of the convolution at many tau; (ii) record numbers a(0) = -0.653847,
tau_0 = 6.310, I_minus = 2.241523, Fejer minimum 0.13597 at T = 11; (iii) the u-space form of the archimedean term
(NOTE section 2, Lemma A2) on the Fejer element; (iv) monotonicity of a on (0, inf) numerically (proved in NOTE).
"""
import numpy as np, mpmath as mp, json, time, sys
from scipy.special import digamma
from scipy.integrate import quad
t0 = time.time(); out = {}
LOGPI = np.log(np.pi)

def A_fn(r):
    return (np.real(digamma(0.25 + 0.5j*np.asarray(r, float))) - LOGPI)/(2*np.pi)

def a_closed(tau):
    tau = np.asarray(tau, float); z = 0.5j*tau
    val = np.real((1 - 1j*tau)*digamma(0.5 + z) + 1j*tau*digamma(1.0 + z))
    return (val - 1.0 - LOGPI)/(2*np.pi)

def a_quad(tau, K=14.0):
    # direct quadrature of int sech(pi xi) A(tau - xi) dxi, tail |xi|>K < 2 e^{-pi K} * |A| ~ 1e-19 * log
    f = lambda xi: A_fn(tau - xi)/np.cosh(np.pi*xi)
    v1, e1 = quad(f, -K, 0, limit=400); v2, e2 = quad(f, 0, K, limit=400)
    return v1 + v2, e1 + e2

def a_mp(tau, dps=30):
    with mp.workdps(dps):
        t = mp.mpf(tau); z = mp.mpc(0, t/2)
        val = mp.re((1 - mp.mpc(0, t))*mp.digamma(mp.mpf('0.5') + z) + mp.mpc(0, t)*mp.digamma(1 + z))
        return (val - 1 - mp.log(mp.pi))/(2*mp.pi)

print("== (i) closed form vs quadrature")
maxdiff = 0.0
for tau in [0, 0.3, 1, 2, 3, 4.5, 6, 6.31, 8, 10, 14, 20, 30, 60, 100, 1000]:
    c = float(a_closed(tau)); q, qe = a_quad(tau); m = float(a_mp(tau))
    maxdiff = max(maxdiff, abs(c - q))
    print(f"  tau={tau:8.3f}  closed={c: .12f}  quad={q: .12f} (err est {qe:.1e})  mp30={m: .12f}  |closed-quad|={abs(c-q):.2e}  |closed-mp|={abs(c-m):.2e}")
out["max_abs_closed_minus_quad"] = maxdiff
assert maxdiff < 1e-9, "closed form disagrees with quadrature"

print("== (ii) record numbers")
a0 = float(a_closed(0.0)); out["a0"] = a0
tau0 = float(mp.findroot(lambda t: a_mp(t), 6.31)); out["tau0"] = tau0
# I_minus = 2 * int_0^tau0 |a|
Im, Ime = quad(lambda t: -a_closed(t), 0, tau0, limit=400); I_minus = 2*Im; out["I_minus"] = I_minus
print(f"  a(0) = {a0:.6f} (record -0.653847);  A(0) = {float(A_fn(0.0)):.6f} (record -0.855010)")
print(f"  tau_0 = {tau0:.5f} (record 6.310);  I_minus = {I_minus:.6f} (record 2.241523);  2 - I_minus = {2-I_minus:.6f}")
# Fejer family: B_T = 2 + int (1-|tau|/T)_+ a = 2 + 2 int_0^T (1 - t/T) a(t) dt
def BT(T):
    v, e = quad(lambda t: (1 - t/T)*a_closed(t), 0, T, limit=400); return 2 + 2*v
fe = {T: BT(T) for T in (4, 8, 10, 10.5, 11, 11.5, 12, 14, 16, 20, 30, 40)}
for T, v in fe.items(): print(f"  Fejer T={T:5.1f}  B/what(0) = {v:.6f}")
Tstar = float(mp.findroot(lambda T: mp.diff(lambda s: BT(float(s)), T), 11.0)) if False else None
# fine 1-d minimization of B_T over T
from scipy.optimize import minimize_scalar
res = minimize_scalar(BT, bounds=(9, 13), method="bounded", options={"xatol":1e-6})
out["fejer_min_T"] = float(res.x); out["fejer_min_value"] = float(res.fun); out["fejer_T11"] = fe[11]
print(f"  Fejer minimum over T: T* = {res.x:.4f}, value {res.fun:.6f};  at T = 11: {fe[11]:.6f} (record 0.13597)")
assert abs(a0 + 0.653847) < 2e-6 and abs(tau0 - 6.310) < 1e-3 and abs(I_minus - 2.241523) < 2e-5 and abs(fe[11] - 0.13597) < 2e-5

print("== (iii) u-space form of the archimedean term on the Fejer element (T = 11)")
# int what a = -(gamma + log pi) w(0) + 2 int_0^inf [ w(0) e^{-2u}/(1-e^{-2u}) - 2 w(u)/((e^u+1)(1-e^{-2u})) ] du,  w = (T/2pi) sinc^2(Tu/2)
T = 11.0
def w_fejer(u): x = T*u/2; return (T/(2*np.pi))*(np.sinc(x/np.pi))**2
w0 = w_fejer(0.0)
def integrand(u):
    if u < 1e-8:
        return -0.75*w0 + 0.0  # limit: w(0)(q - rho) -> -3/4 w(0); (w(u)-w(0)) rho -> 0
    q = np.exp(-2*u)/(1 - np.exp(-2*u)); rho = 2.0/((np.exp(u) + 1)*(1 - np.exp(-2*u)))
    return w0*q - w_fejer(u)*rho
v, e = quad(integrand, 0, 60, limit=800, points=[1e-6, 0.1, 1, 5, 20])
uspace = -(np.euler_gamma + LOGPI)*w0 + 2*v
tspace = fe[11] - 2
print(f"  u-space: {uspace:.6f}   tau-space (2 + int what a - 2): {tspace:.6f}   diff {uspace - tspace:.2e}")
out["uspace_T11"] = float(uspace); out["tspace_T11"] = float(tspace)
assert abs(uspace - tspace) < 1e-5

print("== (iv) monotonicity of a on (0, 200] (numerical; proof in NOTE)")
tt = np.linspace(1e-4, 200, 400001); aa = a_closed(tt); mono = bool(np.all(np.diff(aa) > 0))
print(f"  strictly increasing on the grid: {mono};  a(200) = {aa[-1]:.6f}  vs (1/2pi)log(200/2pi) = {np.log(200/(2*np.pi))/(2*np.pi):.6f}")
out["monotone_grid"] = mono
out["seconds"] = time.time() - t0
json.dump(out, open("conventions_check_out.json", "w"), indent=1)
print(f"done in {time.time()-t0:.1f}s")
