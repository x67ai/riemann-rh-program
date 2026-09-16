#!/usr/bin/env python3
"""dh_control_new_heights.py -- PRICING 2(c): the zero-side V.4 negative control at the NEW off-line orbits of f_DH that
dh_offline_scan.py located (its own 30-minute cap left no time for this stage).  Exactly the control of
verify/dh_negative_control.py at t = 85.7, with the campaign library's datum: Z = orbit {+-t +- i delta} + DH's on-line zeros
in [t - 30, t + 30] (sign changes of Z_DH at step 0.05, Illinois refinement), Z' = the on-line zeros only; W_Z, W_Z',
the main term -2 delta^2 c(delta L)^2, the ratio |W_Z - W_Z'|/(delta^2 e^{delta L/2}) at L = 10..100 and L*(delta, t; C1 = 1).
Caveats as at 85.7: the window hypothesis (all other points real within R_0 L*) is not verified (the scan shows further
orbits every ~40 units); the reflection condition t >= 21 L* fails at these t; the reflected points are omitted.
Writes the control rows INTO dh_offline_scan.json (keys control_rows, online_window of each strip record) and logs to
logs/dh_offline_scan.log.   usage: python3 dh_control_new_heights.py [n_heights = 3]
INSTRUMENT; nothing about RH.
"""
import sys, os, json, math, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '..', 'ccm-dh-test'))
import mpmath as mp, numpy as np
import dh, campaign_lib as cl
mp.mp.dps = 15
n_heights = int(sys.argv[1]) if len(sys.argv) > 1 else 3
logf = open(os.path.join(HERE, 'logs', 'dh_offline_scan.log'), 'a')
def log(s):
    print(s, flush=True); logf.write(s + '\n'); logf.flush()
T0 = time.time()
J = os.path.join(HERE, 'dh_offline_scan.json')
out = json.load(open(J))
strip = out['found_in_strip']
new = [r for r in strip if abs(r['t'] - 85.699348) >= 0.01]
log("=" * 120)
log("[%s] dh_control_new_heights.py START: %d strip orbits in the JSON (%d new); controls at the first %d new heights" % (cl.now(), len(strip), len(new), n_heights))
def Zline(u): return dh.z_dh(u)[0]
def online_count(T1, T2, step=mp.mpf('0.05')):
    zs = []; u = mp.mpf(T1); zp = Zline(u)
    while u < T2:
        u2 = min(u + step, mp.mpf(T2)); zn = Zline(u2)
        if zp*zn < 0: zs.append(mp.findroot(Zline, (u, u2), solver='illinois'))
        u, zp = u2, zn
    return zs
for rec in new[:n_heights]:
    t = rec['t']; d = rec['delta']; Wd = 30.0
    # re-verify the orbit
    r = mp.findroot(dh.f_dh, mp.mpc(rec['rho'][0], rec['rho'][1]), tol=1e-24, maxsteps=20, verify=False)
    onl = online_count(mp.mpf(t - Wd), mp.mpf(t + Wd))
    g = np.array([float(z) for z in onl])
    Ls1 = cl.Lstar(d, t, 1)
    log("   CONTROL at rho = %.12f + %.9f i (re-refined: |f| = %.1e), t = %.6f, delta = %.6f, L*(C1 = 1) = %.2f, t/L* = %.2f: %d DH on-line zeros in [t-30, t+30] (mean gap %.3f)" % (rec['rho'][0], rec['rho'][1], float(abs(dh.f_dh(r))), t, d, Ls1, t/Ls1, len(g), 60.0/max(1, len(g))))
    rows = []
    for L in [10, 20, 30, 40, 50, 60, 70, 80, Ls1, 100]:
        nz = cl.noise_at(t, g, float(L), Wd)
        c = float(cl.c_edge([d*L])[0]); main = -2*d*d*c*c; WZ = nz['N_Z'] + main; bound = d*d*math.exp(d*L/2)
        rows.append(dict(L=float(L), W_Z=WZ, W_Zprime=nz['N_Z'], main=main, sep=abs(WZ - nz['N_Z']), bound=bound, ratio=abs(WZ - nz['N_Z'])/bound, clause4_bound=2*cl.B1*math.log(3 + t + Wd)/L**2))
        log("   L=%7.2f: W_Z = %.6e  W_Z' = %.6e (clause-4 bound %.3e)  main = %.6e  |W_Z - W_Z'|/(d^2 e^{dL/2}) = %.4g  fires(>=1): %s  deltaL = %.1f" % (L, WZ, nz['N_Z'], rows[-1]['clause4_bound'], main, rows[-1]['ratio'], rows[-1]['sep'] >= 1, d*L))
    rec['control_rows'] = rows; rec['online_window'] = [float(x) for x in g]; rec['abs_f_refined'] = float(abs(dh.f_dh(r)))
    log("   CAVEATS (as at 85.7): window hypothesis not verified (further orbits every ~40 units in the scan); reflection condition t >= 21 L* %s (t/L* = %.2f); reflected points omitted." % ("holds" if t >= 21*Ls1 else "FAILS", t/Ls1))
    json.dump(out, open(J, 'w'), indent=1, default=float)
out['controls_date'] = cl.now(); out['controls_seconds'] = time.time() - T0
json.dump(out, open(J, 'w'), indent=1, default=float)
log("[%s] dh_control_new_heights.py DONE in %.0f s: DH negative control available at %d further height(s) (%s)" % (cl.now(), time.time() - T0, min(n_heights, len(new)), ", ".join("%.3f" % r['t'] for r in new[:n_heights])))
