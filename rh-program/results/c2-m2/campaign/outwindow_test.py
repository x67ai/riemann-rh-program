#!/usr/bin/env python3
"""outwindow_test.py -- PRICING 2(a) item (6) / 2(d) item 4: the out-window contamination test, which needs NO zeta zeros.
INSTRUMENT (standing order 4): decides how loose the proved R_0 = 81 is; nothing about RH.

A second orbit at depth 1/2 is planted at real distance u from t: the points (t+u) -+ i/2 (their reflections at -(t+u)
are negligible and not included).  With h_f(r) = (r - t) Bhat(L (r - t)) and B real, even (Bhat(conj z) = conj Bhat(z)):
   h_f(gamma) conj(h_f(conj gamma)) = (u - i/2)^2 Bhat(z)^2,  z = L u - i L/2,   pair contribution = 2 Re[(u - i/2)^2 Bhat(z)^2]  (exact).
Clause 5's pointwise bound per point: (u + 1/2)^2 e^{L/2} G1(L u)^2  (note section 6 (a)); per pair twice that.
Tabulated: u in {5, 50, 500, 81 L} on an L-grid, the exact pair contribution (bhat_mp, Poisson-trapezoid in mpmath at the
precision the cancellation needs; skipped with the bound/estimate only where the node count x precision exceeds the work cap),
the ratio bound/exact (referee F's 1e9-1e22 looseness), and u_true(L) := the least u at which the TRUE pair contamination
falls to e^{-L} (bisection on the direct value), against the proved R_0 L = 81 L and the asymptote (7/(8 c_B))^2 = 37.5.
"""
import sys, os, json, math, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import mpmath as mp
import campaign_lib as cl

logf = open(os.path.join(HERE, 'logs', 'outwindow_test.log'), 'a')
def log(s):
    print(s, flush=True); logf.write(s + '\n'); logf.flush()
T0 = time.time()
log("=" * 120)
log("[%s] outwindow_test.py START (height-independent; no zeros)" % cl.now())
log("INSTRUMENT: decides the looseness of the proved out-window radius R_0 = 81; nothing about RH.")
MAX_WORK = 3.0e8

def pair_exact(L, u, rel=1e-8):
    """(value, M, dps) of the exact pair contribution 2 Re[(u - i/2)^2 Bhat(Lu - iL/2)^2], or (None, M, dps)."""
    xi = L*u; y = L/2
    lt = cl.log_env(xi) + y/2 + math.log(rel)                  # log of the target: estimate of |Bhat(z)| (strip weight e^{y/2} x real envelope) x rel
    if lt < -650:                                              # below the double range: the value is < 1e-280 -- bound / estimate only
        need = -lt + y/2 + 3; M = int((xi + (need/0.6)**2)/(2*math.pi)); dps = int(need/2.3 + 8)
        return None, M, dps
    val, M, dps = cl.bhat_mp(mp.mpc(xi, -y), math.exp(lt), max_work=MAX_WORK)
    if val is None: return None, M, dps
    with mp.workdps(dps):
        w = 2*mp.re((mp.mpc(u, -0.5))**2*val**2)
    return w, M, dps

def log10_bound_pair(L, u):
    return (math.log(2*(u + 0.5)**2) + L/2 + 2*cl.log_G1(L*u))/math.log(10)

def log10_est_pair(L, u):
    return (math.log(2*(u*u + 0.25)) + L/2 + 2*cl.log_env(L*u))/math.log(10)

out = dict(date=cl.now(), points=[], u_true=[])
L_list = [4, 8, 12, 16, 20, 30, 40, 50, 60, 80, 100, 120, 403.49, 1267.4]
log("\n(A) the four planted distances per L: exact pair contribution vs clause 5's pointwise bound 2 (u+1/2)^2 e^{L/2} G1(Lu)^2")
log("      L      u   |  log10|exact|   log10 bound   log10(bound/|exact|)   log10 est[envelope]   e^-L: log10   (M, dps)")
for L in L_list:
    for u in (5.0, 50.0, 500.0, 81.0*L):
        t1 = time.time()
        w, M, dps = pair_exact(L, u)
        lb = log10_bound_pair(L, u); le = log10_est_pair(L, u)
        if w is None:
            log("   %7.2f %8.1f |  not computed (M = %d, dps = %d exceeds the work cap)   %9.2f   -                   %9.2f   %9.2f" % (L, u, M, dps, lb, le, -L/math.log(10)))
            out['points'].append(dict(L=L, u=u, exact=None, log10_bound=lb, log10_est=le, M=M, dps=dps))
        else:
            lw = float(mp.log10(abs(w))) if w != 0 else -9999
            log("   %7.2f %8.1f |  %9.2f (%s)   %9.2f   %9.2f   %9.2f   %9.2f   (%d, %d)  %.1f s" % (L, u, lw, "neg" if w < 0 else "pos", lb, lb - lw, le, -L/math.log(10), M, dps, time.time() - t1))
            out['points'].append(dict(L=L, u=u, exact=float(w), log10_abs_exact=lw, log10_bound=lb, log10_bound_over_exact=lb - lw, log10_est=le, M=M, dps=dps))
json.dump(out, open(os.path.join(HERE, 'outwindow_test.json'), 'w'), indent=1)

log("\n(B) u_true(L): least u with |exact pair contamination| <= e^{-L} (bisection on the direct value; envelope start), against 81 L")
log("      L    u_true    u_true/L   | envelope u_est/L | bound-route u with 2(u+1/2)^2 e^{L/2} G1(Lu)^2 = e^{-L}: u_G1/L")
for L in [4, 8, 12, 16, 20, 30, 40, 50, 60, 80, 100, 120]:
    target = -L/math.log(10)
    # envelope start
    ue = 1.0
    while log10_est_pair(L, ue) > target: ue *= 1.5
    # G1 route
    ug = 1.0
    while log10_bound_pair(L, ug) > target: ug *= 1.5
    # direct bisection in [ue/4, 4 ue]
    lo, hi = ue/4, ue*4
    def f(u):
        w, M, dps = pair_exact(L, u)
        return float(mp.log10(abs(w))) if (w is not None and w != 0) else -9999
    if f(lo) <= target: lo = lo/4
    for _ in range(18):
        mid = math.sqrt(lo*hi)
        if f(mid) > target: lo = mid
        else: hi = mid
    ut = hi
    log("   %5.1f  %8.3f  %8.3f   |   %8.3f       |   %8.1f" % (L, ut, ut/L, ue/L, ug/L))
    out['u_true'].append(dict(L=L, u_true=ut, u_true_over_L=ut/L, u_env_over_L=ue/L, u_G1_over_L=ug/L))
    json.dump(out, open(os.path.join(HERE, 'outwindow_test.json'), 'w'), indent=1)
log("   proved: R_0 = 81 (all L >= 50), R_0(L_0) = 58.5/48/43/40/38 at L_0 = 100/200/403/1000/1e4, asymptote (7/(8 c_B))^2 = %.2f; the note's 'for the record' estimate with rate 0.85: (7/(8*0.85))^2 = 1.06; with the asymptotic rate 1/sqrt2: (7/(8*0.7071))^2 = %.2f" % ((7/(8*cl.C_B))**2, (7/(8*0.70711))**2))
out['date_end'] = cl.now(); out['seconds'] = time.time() - T0
json.dump(out, open(os.path.join(HERE, 'outwindow_test.json'), 'w'), indent=1)
log("[%s] outwindow_test.py DONE in %.1f s" % (cl.now(), time.time() - T0))
