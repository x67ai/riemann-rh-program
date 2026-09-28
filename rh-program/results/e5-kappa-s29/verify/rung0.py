#!/usr/bin/env python3
"""rung0.py -- dress rehearsal of the pipeline (kappa_pipeline.py) on instances with a KNOWN answer (BRIEF section 3, binding).

Instance A (exact answer):  a_0 := (1/2pi) sigmahat_0 with sigma_0 = -d_0 trap(U1,U2) + nu_a [hat_{h_nu}(u-u_a) + hat_{h_nu}(u+u_a)],
   d_0 = 1.9, U1 = 0.7071, U2 = 1.4142 (trapezoid: 1 on |u|<=U1, linear to 0 at U2), u_a = 1.7321, h_nu = 0.3, nu_a = 0.5
   (knots deliberately OFF every LP grid).  kappa(a_0) = 2 - d_0 = 0.1 EXACTLY:
   >= : the certificate (d_0, sigma_0, psi = 0) in Theorem D;   <= : any cone element w supported in [-U1, U1] has
   B_0(w)/what(0) = 2 + int w dsigma_0 / int w = 2 - d_0 (h_0 = 1 and nu_0 = 0 on supp w).  Both checked below numerically
   in tau-space too (the transform conventions).  a_0 decays like 1/tau^2 with sign changes, so the dual is verified on the
   window [0, T_v] only (the target's tail argument needs a growing a; that is instance B).
Instance B (target-like tail):  a_1 := a_0 + p,  p(tau) = (1/2pi) log^+(|tau|/T_0), T_0 = 60.  kappa(a_1) >= 0.1 by the
   certificate (d_0, sigma_0, psi = 2 pi p >= 0); kappa(a_1) <= primal value (delta_ub < 1e-3 expected: f-hat = triangle of
   half-width X <= 29 gives what supported in [-58, 58] where p = 0, and w ~ sinc^4 has < 4e-4 of its mass outside [-U1,U1]).
   The full certification path (repair + adaptive Lipschitz cells + tail) is the target's.
Instance C (bathtub-sharp): a_2 := -c e^{-tau^2/2}, c = 1/2; kappa = 2 - c sqrt(2 pi) = 0.7466 (sup what = what(0);
   the certificate sigma = -c sqrt(2pi) e^{-u^2/2} is smooth and NOT on any grid).  Window-only dual.
"""
import numpy as np, json, time, sys
from kappa_pipeline import *
t0 = time.time(); out = {}; LOG = []
def log(msg): print(msg); LOG.append(msg)

d0, U1, U2, ua, hnu, nua = 1.9, 0.7071, 1.4142, 1.7321, 0.3, 0.5
def sigmahat0(t):
    t = np.asarray(t, float); tt = np.where(np.abs(t) < 1e-9, 1e-9, t)
    trap = 2*(np.cos(U1*tt) - np.cos(U2*tt))/((U2 - U1)*tt**2)
    trap = np.where(np.abs(t) < 1e-9, U1 + U2, trap)
    return -d0*trap + nua*2*hnu*sinc2(hnu*t/2)*np.cos(ua*t)
a0 = lambda t: sigmahat0(t)/(2*np.pi)
T0 = 60.0
p = lambda t: np.log(np.maximum(np.abs(np.asarray(t, float))/T0, 1.0))/(2*np.pi)
a1 = lambda t: a0(t) + p(t)
cC = 0.5
a2 = lambda t: -cC*np.exp(-np.asarray(t, float)**2/2)
# rigorous-style Lipschitz bounds: |sigmahat_0'| <= int |u| |sigma_0| du
uu = np.linspace(-3, 3, 600001); du = uu[1] - uu[0]
trap_u = np.clip((U2 - np.abs(uu))/(U2 - U1), 0, 1)
hat_u = np.maximum(0, 1 - np.abs(np.abs(uu) - ua)/hnu)
sig0_u = -d0*trap_u + nua*hat_u
M1 = np.sum(np.abs(uu)*np.abs(sig0_u))*du
lipA = lambda T: M1/(2*np.pi)*1.01
lipB = lambda T: (M1 + 1/T0)/(2*np.pi)*1.01
tailB = lambda T: p(T) - (4*d0/(U2 - U1) + 8*nua/hnu)/(T**2)/(2*np.pi)
log(f"instance A: a_0(0) = {float(a0(0.0)):.6f}; int|u||sigma_0| = {M1:.4f}; exact kappa_0 = {2-d0}")

# --- independent check of the exact answer in tau-space: w = cubic B-spline supported in [-U1, U1]
from scipy.integrate import quad
def bspline3(x):  # cubic B-spline on [-2,2], C^2, >= 0, transform sinc^4 >= 0
    x = np.abs(x); return np.where(x < 1, (4 - 6*x**2 + 3*x**3)/6, np.where(x < 2, (2 - x)**3/6, 0.0))
scale = U1/2
w_test = lambda u: bspline3(u/scale)
what_test = lambda t: scale*(np.sinc(scale*t/(2*np.pi)))**4 * 1.0   # int bspline3 = 1 -> what(0) = scale
what0 = scale
val_tau, err = quad(lambda t: what_test(t)*a0(np.array([t]))[0], 0, 4000, limit=4000)
R_tau = 2 + 2*val_tau/what0
val_u = np.sum(w_test(uu)*sig0_u)*du/(np.sum(w_test(uu))*du)
log(f"  primal check, w = B-spline in [-U1,U1]:  tau-space 2 + int what a_0/what(0) = {R_tau:.6f} (quad err {2*err/what0:.1e});  u-space 2 + int w dsigma_0/int w = {2+val_u:.6f};  exact 0.1")
out["A_exact_check_tau"] = R_tau; out["A_exact_check_u"] = 2 + val_u
assert abs(R_tau - 0.1) < 5e-4 and abs(2 + val_u - 0.1) < 1e-6

# --- instance A: dual LP (window) at two grids, primal squares
resA = {}
for hu in (0.02, 0.01):
    log(f"instance A dual LP, hu = {hu}, U = 3, Tmax = 60")
    r = dual_lp(a0, U=3.0, hu=hu, Tmax=60.0, coarse=(0.05, 40.0, 0.25), fine=(0.002, 40.0, 0.01), log=log)
    resA[hu] = r; out[f"A_dual_hu{hu}"] = dict(kappa_lp=r["kappa_lp"], d=r["d"], rounds=r["rounds"], rows=r["n_rows"], seconds=r["seconds"], min_psi_fine=r["min_psi_fine"])
log("instance A primal (squares family)")
prA = {}
for X in (15.0, 29.0):
    r = primal_squares(a0, X=X, hx=0.05, log=log)
    ex = primal_value_exact(a0, r["c"], 0.05)
    prA[X] = ex; out[f"A_primal_X{X}"] = dict(value=r["value"], exact_recheck=ex, n=r["n"], seconds=r["seconds"])
    log(f"  X = {X}: primal value {r['value']:.8f}, re-evaluated with 24-point quadrature {ex:.8f}")
kA_lb = resA[0.01]["kappa_lp"]; kA_ub = min(prA.values())
log(f"instance A bracket: [{kA_lb:.6f}, {kA_ub:.6f}] vs exact 0.1 -> gap {kA_ub-kA_lb:.2e} ({100*(kA_ub-kA_lb)/0.1:.2f}% of the answer)")
out["A_bracket"] = [kA_lb, kA_ub]

# --- instance B: full certification path
log("instance B (a_0 + growing tail p), dual LP hu = 0.01, U = 3, Tmax = 200")
rB = dual_lp(a1, U=3.0, hu=0.01, Tmax=200.0, coarse=(0.05, 40.0, 0.5), fine=(0.002, 40.0, 0.02), log=log)
out["B_dual"] = dict(kappa_lp=rB["kappa_lp"], d=rB["d"], rounds=rB["rounds"], rows=rB["n_rows"], seconds=rB["seconds"], active=[float(x) for x in rB["active"][:40]])
log(f"  active taus (first 40): {np.round(rB['active'][:40], 3).tolist()}")
vB = verify_dual(a1, lipB, tailB, rB["s"], rB["d"], 0.01, eta=1e-4, c_rep=1.0, T_v=200.0, h0=0.01, log=log)
out["B_verify"] = {k: v for k, v in vB.items()}
log(f"  certified kappa_lb(B) = {vB['kappa_cert']}  (LP value {rB['kappa_lp']:.6f}, repair cost eta = 1e-4)")
log("instance B primal")
rBp = primal_squares(a1, X=29.0, hx=0.05, log=log); exB = primal_value_exact(a1, rBp["c"], 0.05)
out["B_primal"] = dict(value=rBp["value"], exact_recheck=exB)
log(f"instance B bracket: [{vB['kappa_cert']}, {exB:.6f}] vs known [0.1, 0.1 + delta] -> gap {exB - (vB['kappa_cert'] or 0):.2e} ({100*(exB-(vB['kappa_cert'] or 0))/0.1:.2f}%)")
out["B_bracket"] = [vB["kappa_cert"], exB]

# --- instance C: window-only dual + primal
log("instance C (Gaussian), dual LP hu = 0.01, U = 6, Tmax = 40 (window)")
rC = dual_lp(a2, U=6.0, hu=0.01, Tmax=40.0, coarse=(0.05, 40.0, 0.5), fine=(0.002, 40.0, 0.02), log=log)
rCp = primal_squares(a2, X=29.0, hx=0.05, log=log); exC = primal_value_exact(a2, rCp["c"], 0.05)
kC = 2 - cC*np.sqrt(2*np.pi)
log(f"instance C bracket: [{rC['kappa_lp']:.6f}, {exC:.6f}] vs exact {kC:.6f} -> gap {exC - rC['kappa_lp']:.2e} ({100*(exC-rC['kappa_lp'])/kC:.2f}%)")
out["C_bracket"] = [rC["kappa_lp"], exC, kC]
out["seconds"] = time.time() - t0
json.dump(out, open("rung0_out.json", "w"), indent=1, default=float)
log(f"done in {time.time()-t0:.1f}s")
