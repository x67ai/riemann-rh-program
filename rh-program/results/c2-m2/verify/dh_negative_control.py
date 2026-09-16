#!/usr/bin/env python3
"""dh_negative_control.py -- zoo V.4 controls for the separation datum W_Z(f_{t,L}), ZERO-SIDE only (no prime-side evaluation).
NEGATIVE control (a case known to fail RH): the Davenport-Heilbronn function f_DH (builder results/ccm-dh-test/dh.py):
  on-line zeros in [t - W, t + W] located by sign changes of Z_DH(t) = Xi_DH(1/2 + it) (real), refined by Illinois;
  the off-line zero rho_0 = 0.808517... + 85.699348... i by Newton from the recorded seed;  t := Im rho_0, delta := Re rho_0 - 1/2.
  Z  := orbit {+-t +- i delta} + on-line zeros in the window (and their reflections);  Z' := on-line zeros only;
  Z'' := Z' + an on-line double at +-t (the II.4 tight pair).  Datum W_Z(f) = sum h_f(gamma) conj(h_f(conj gamma)).
POSITIVE control (a case known to hold): zeta's zeros in the same window (mpmath.zetazero), all on-line: W >= 0 and small.
Reported: W_Z, W_Z', separation |W_Z - W_Z'| against the clause-6 bound delta^2 e^{delta L/2} and against 1, at several L
including the theorem's L*(delta, t).  Caveat printed: the window hypothesis (R = R_0 L) is NOT verified for DH here.
Budget: < 10 min."""
import time, json, sys, os
import mpmath as mp
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "ccm-dh-test"))
import dh
t0 = time.time(); mp.mp.dps = 15
out = {}
# --- the off-line zero
rho0 = dh.find_zero(mp.mpc('0.8085', '85.6993'))
t = rho0.imag; delta = rho0.real - mp.mpf(1)/2
print(f"DH off-line zero rho_0 = {mp.nstr(rho0, 16)}  |f_DH(rho_0)| = {mp.nstr(abs(dh.f_dh(rho0)), 3)};  t = {mp.nstr(t,12)}, delta = Re rho_0 - 1/2 = {mp.nstr(delta,10)}")
out["rho0"] = [float(rho0.real), float(rho0.imag)]; out["t"] = float(t); out["delta"] = float(delta)
# --- on-line zeros of DH in [t-W, t+W]
Wd = mp.mpf(30); step = mp.mpf('0.05')
def zline(u): return dh.z_dh(u)[0]
zs = []; u = t - Wd; zp = zline(u)
while u < t + Wd:
    u2 = u + step; zn = zline(u2)
    if zp*zn < 0:
        zs.append(mp.findroot(zline, (u, u2), solver='illinois'))
    u, zp = u2, zn
print(f"DH on-line zeros in [{mp.nstr(t-Wd,6)}, {mp.nstr(t+Wd,6)}] by sign change (step {step}): {len(zs)} found")
print("   ", [round(float(z), 4) for z in zs])
out["dh_online_zeros_window"] = [float(z) for z in zs]
# expected count from the completed-function phase: theta(T) = (T/2) log(5/pi) + Im log Gamma(3/4 + iT/2); N(T2)-N(T1) ~ (theta(T2)-theta(T1))/pi + O(1)
def theta(T): T = mp.mpf(T); return T/2*mp.log(5/mp.pi) + mp.im(mp.loggamma(mp.mpf(3)/4 + 1j*T/2))
expct = (theta(t+Wd) - theta(t-Wd))/mp.pi
print(f"    phase count (theta(t+W)-theta(t-W))/pi = {mp.nstr(expct,5)}  vs on-line found {len(zs)} + 2 (the off-line pair) = {len(zs)+2}   [indicative: S(T) fluctuations are O(1)]")
out["phase_count_window"] = float(expct)
# --- the test and the datum
def Braw(v):
    v = mp.mpf(v)
    if abs(v) >= mp.mpf(1)/2: return mp.mpf(0)
    return mp.e**(-1/(1-4*v*v))
Zn = mp.quad(Braw, [-0.5, -0.25, 0, 0.25, 0.5])
def Bhat(z):   # int B(v) e^{i z v} dv, complex z, by quadrature (|Im z| L-scaled up to ~ 30: fine at dps 15 with subdivision)
    z = mp.mpc(z); n = max(8, int(abs(z.real))//3 + 8)
    pts = [-0.5 + k/n for k in range(n+1)]
    return mp.quad(lambda v: Braw(v)*mp.e**(1j*z*v), pts)/Zn
def h_f(z, L): z = mp.mpc(z); return (z - t)*Bhat(L*(z - t))
def W_of(points, L):
    return mp.fsum(h_f(gm, L)*mp.conj(h_f(mp.conj(gm), L)) for gm in points)
def c_of(lam): return mp.quad(lambda v: Braw(v)*mp.cosh(lam*v), [-0.5, -0.25, 0, 0.25, 0.5])/Zn
orbit = [mp.mpc(t, -delta), mp.mpc(t, delta), mp.mpc(-t, -delta), mp.mpc(-t, delta)]
online = [mp.mpc(z, 0) for z in zs] + [mp.mpc(-z, 0) for z in zs]
b1 = 8.647
Lstar = max(25/delta, 4/delta*(mp.log(mp.log(3+t)) + 2*mp.log(1/delta) + mp.log(2*b1)))
print(f"theorem bandwidth at (t, delta): L* = max(25/delta, 4/delta (loglog(3+t) + 2 log(1/delta) + log(2 b1))) = {mp.nstr(Lstar,5)}")
out["L_star"] = float(Lstar)
rows = []
for L in [10, 20, 30, 40, 50, 60, 70, 80, float(Lstar), 100, 120]:
    L = mp.mpf(L)
    WZ = W_of(orbit + online, L); WZp = W_of(online, L)
    # Z'' = Z' + double at +-t: h_f(t)=0 exactly; h_f(-t) = -2t Bhat(-2tL) (tiny, real point) -> contributes 2|h_f(-t)|^2 twice (multiplicity 2)
    dbl = 2*abs(h_f(mp.mpc(-t,0), L))**2*2
    main = -2*delta**2*c_of(delta*L)**2
    bound = delta**2*mp.e**(delta*L/2)
    sep = abs(WZ - WZp)
    rows.append(dict(L=float(L), W_Z=float(WZ.real), W_Zprime=float(WZp.real), W_Zdouble=float((WZp+dbl).real), main_term=float(main), separation=float(sep), bound_clause6=float(bound), ratio=float(sep/bound), im_parts=[float(WZ.imag), float(WZp.imag)]))
    print(f"L={mp.nstr(L,5):>7}: W_Z = {mp.nstr(WZ.real,8):>14}  W_Z' = {mp.nstr(WZp.real,8):>12}  (Z'' - Z' = {mp.nstr(dbl,3)})  main -2d^2c^2 = {mp.nstr(main,8):>14}  |W_Z - W_Z'| = {mp.nstr(sep,8):>12}  bound d^2 e^(dL/2) = {mp.nstr(bound,6):>10}  ratio = {mp.nstr(sep/bound,5)}  fires(>=1): {sep >= 1}")
out["rows"] = rows
# --- positive control: zeta zeros in the same window
zz = []; n = 1
while True:
    g = mp.zetazero(n).imag
    if g > t + Wd: break
    if g >= t - Wd: zz.append(g)
    n += 1
zeta_pts = [mp.mpc(g, 0) for g in zz] + [mp.mpc(-g, 0) for g in zz]
print(f"POSITIVE control: {len(zz)} zeta zeros in the window (indices up to {n-1}); W_zeta(f_{{t,L}}) at the same t:")
pos = []
for L in [20, 40, 60, float(Lstar), 100]:
    L = mp.mpf(L); Wz = W_of(zeta_pts, L); pos.append(dict(L=float(L), W_zeta=float(Wz.real), noise_bound=float(b1*mp.log(3+t+Wd)/L**2)))
    print(f"    L={mp.nstr(L,5)}: W_zeta = {mp.nstr(Wz.real,6)} (>= 0; imag {mp.nstr(Wz.imag,2)});  b1 log(3+t+W)/L^2 = {mp.nstr(b1*mp.log(3+t+Wd)/L**2,4)};  clause-6 bound d^2 e^(dL/2) at DH's delta = {mp.nstr(delta**2*mp.e**(delta*L/2),4)}")
out["positive_control"] = pos
# also DH with the orbit removed but the on-line double added is Z'': its datum equals W_Z' + tiny (printed above)
print("CAVEAT (printed by design): the theorem's window hypothesis -- all points of Z other than the orbit real within |Re gamma - t| <= R_0 L* -- is NOT verified for DH here (R_0 L* is thousands; DH has further off-line zeros); the control shows the datum firing on the known off-line orbit, with the in-window on-line zeros present, at the theorem's bandwidth and below it.")
out["runtime_s"] = time.time() - t0
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "dh_negative_control_out.json", "w"), indent=1)
print(f"done in {time.time()-t0:.1f}s")
