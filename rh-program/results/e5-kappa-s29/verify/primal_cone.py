#!/usr/bin/env python3
"""primal_cone.py -- rung 1 (iv): the primal over GENERAL cone elements of compact support: w = sum_k w_k H_k (H_k the
symmetric pair of hats of half-width hu at +-u_k, w_k >= 0), so w >= 0 and w is piecewise linear on [-U, U];
what(tau) = hu sinc^2(hu tau/2) Q(tau), Q(tau) := w_0 + 2 sum_{k>=1} w_k cos(u_k tau), and what >= 0 iff Q >= 0 on one
period [0, pi/hu].  The budget is computed on the u-line by Lemma A2 (NOTE 2.2):  int what a = <alpha, w> =
-(gamma + log pi) w(0) + 2 int_0^inf [w(0) q(u) - w(u) rho(u)] du, q = e^{-2u}/(1-e^{-2u}), rho = 2/((e^u+1)(1-e^{-2u})),
linear in the w_k:  coefficients alpha_k by adaptive quadrature.  LP: minimize 2 + sum w_k alpha_k subject to
hu (w_0 + 2 sum w_k) = 1, Q(tau_i) >= 0 (cutting planes on [0, pi/hu]), w_k >= 0.  Certification: add eta*H_0 (Q -> Q + eta)
and verify Q >= 0 by the Lipschitz bound |Q'| <= 2 sum w_k u_k on a grid.  Validation first: Lemma A2 on a cubic B-spline
(u-space vs tau-space, what = sinc^4)."""
import numpy as np, json, time, sys
from scipy.integrate import quad
from scipy.optimize import linprog
from scipy.special import digamma
t0 = time.time(); out = {}
def log(m): print(m, flush=True)
LOGPI = np.log(np.pi); EG = np.euler_gamma
def a_fn(tau):
    tau = np.asarray(tau, float); z = 0.5j*tau
    return (np.real((1 - 1j*tau)*digamma(0.5 + z) + 1j*tau*digamma(1.0 + z)) - 1.0 - LOGPI)/(2*np.pi)
q = lambda u: np.exp(-2*u)/(1 - np.exp(-2*u))
rho = lambda u: 2.0/((np.exp(u) + 1)*(1 - np.exp(-2*u)))
def alpha_of(wfun, w0, U):
    """<alpha, w> for an even w given on u >= 0 with w(0) = w0, support in [0, U]."""
    def integrand(u):
        if u < 1e-7: return -0.75*w0
        return w0*q(u) - wfun(u)*rho(u)
    v1, e1 = quad(integrand, 0, min(U, 1.0), limit=400, points=[1e-6, 1e-3, 0.05, 0.3])
    v2, e2 = quad(integrand, min(U, 1.0), max(U, 1.0) + 40, limit=800)
    return -(EG + LOGPI)*w0 + 2*(v1 + v2)
# --- validation on the cubic B-spline (support [-2,2], what = sinc^4(tau/2) * 1 (int = 1))
def bs3(x):
    x = np.abs(x); return np.where(x < 1, (4 - 6*x**2 + 3*x**3)/6, np.where(x < 2, (2 - x)**3/6, 0.0))
u_val = alpha_of(lambda u: float(bs3(u)), float(bs3(0.0)), 2.0)
t_val, te = quad(lambda t: (np.sinc(t/(2*np.pi)))**4*a_fn(np.array([t]))[0], 0, 4000, limit=4000); t_val *= 2
log(f"Lemma A2 validation on the cubic B-spline: u-space {u_val:.8f}  tau-space {t_val:.8f}  diff {u_val-t_val:.1e} (quad err {2*te:.1e});  B/what(0) = {2 + t_val:.6f}")
out["validation"] = [u_val, t_val]
assert abs(u_val - t_val) < 1e-5
# --- hat coefficients
U = float(sys.argv[1]) if len(sys.argv) > 1 else 8.0; hu = float(sys.argv[2]) if len(sys.argv) > 2 else 0.01
K = int(round(U/hu)); uk = np.arange(K+1)*hu
alpha = np.zeros(K+1)
# k = 0: hat at 0, w(0) = 1
alpha[0] = alpha_of(lambda u: max(0.0, 1 - u/hu), 1.0, hu)
# k >= 1: pair at +-u_k, w(0) = 0:  alpha_k = -2 int H_k rho  (only the u>0 hat)
for k in range(1, K+1):
    lo, hi = uk[k] - hu, uk[k] + hu
    v, e = quad(lambda u: (1 - abs(u - uk[k])/hu)*rho(u), lo, hi, limit=200, points=[uk[k]])
    alpha[k] = -2*v
log(f"alpha coefficients: K = {K}, alpha_0 = {alpha[0]:.6f}, alpha_1 = {alpha[1]:.6f}, alpha at u=1: {alpha[int(round(1/hu))]:.6f}, at u=4: {alpha[int(round(4/hu))]:.6e}  [{time.time()-t0:.1f}s]")
mult = np.where(np.arange(K+1) == 0, 1.0, 2.0)
# --- LP with cutting planes on Q >= 0 over [0, pi/hu]
P = np.pi/hu
taus = np.arange(0, P + 1e-12, 0.05); fine = np.arange(0, P + 1e-12, 0.005)
def Qmat(t): 
    M = 2*np.cos(np.outer(t, uk)); M[:, 0] = 1.0; return M
A_eq = (hu*mult)[None, :]; b_eq = [1.0]
res = None
for rnd in range(30):
    A_ub = -Qmat(taus); b_ub = np.zeros(len(taus))
    res = linprog(alpha, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=[(0, None)]*(K+1), method="highs", options=dict(time_limit=600))
    if res.status != 0: log(f"  LP status {res.status} {res.message}"); break
    w = res.x; val = 2 + alpha @ w
    Qf = np.empty(len(fine))
    for i in range(0, len(fine), 20000): Qf[i:i+20000] = Qmat(fine[i:i+20000]) @ w
    viol = np.where(Qf < -1e-9)[0]
    log(f"  round {rnd:2d}: rows {len(taus):6d}  B/what(0) = {val:.8f}  min Q(fine) = {Qf.min(): .3e}  violations {len(viol)}  [{time.time()-t0:.1f}s]")
    if len(viol) == 0: break
    taus = np.unique(np.concatenate([taus, fine[viol[np.argsort(Qf[viol])][:400]]]))
# --- certification: w' = w + eta H_0 -> Q' = Q + eta; verify Q' >= 0 on [0, P] with Lipschitz L = 2 sum w_k u_k
eta = 1e-6
wq = w.copy(); wq[0] += eta
L = 2*np.sum(wq[1:]*uk[1:])
h = eta/(2*L)*0.9
grid = np.arange(0, P + h, h); ok = True; mn = np.inf
for i in range(0, len(grid), 20000):
    Qg = Qmat(grid[i:i+20000]) @ wq; mn = min(mn, Qg.min())
    if Qg.min() < L*h/2: ok = False
valq = (2*hu*(mult @ wq) + alpha @ wq)/(hu*(mult @ wq))
log(f"certification: eta = {eta}, L = {L:.2f}, grid step {h:.2e} ({len(grid)} points), min Q' = {mn:.3e} >= L h/2 = {L*h/2:.3e}: {ok};  certified B/what(0) = {valq:.8f}")
# shape
supp = uk[wq > 1e-9*wq.max()]
log(f"w support up to u = {supp.max():.2f}; w(u)/w(0) at log2, log3, log4, log5, log7: {[f'{wq[int(round(np.log(p)/hu))]/wq[0]:.1e}' for p in (2,3,4,5,7)]}")
mins = [float(uk[i]) for i in range(1, K) if wq[i] < wq[i-1] and wq[i] <= wq[i+1] and wq[i] < 1e-3*wq.max()]
log(f"near-zeros of w (first 12): {[round(m,3) for m in mins[:12]]}")
out.update(dict(U=U, hu=hu, K=K, value_lp=float(val), value_certified=float(valq), certified=bool(ok), eta=eta, w=[float(x) for x in wq], near_zeros=mins[:20], seconds=time.time()-t0))
json.dump(out, open(f"primal_cone_out.json", "w"), indent=1)
log(f"done in {time.time()-t0:.1f}s")
