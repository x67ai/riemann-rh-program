#!/usr/bin/env python3
"""dh_control_new_heights_rerun.py -- RE-RUN of dh_control_new_heights.py (Session 23 item 0(c), 2026-09-17; DH-RERUN-BRIEF.md):
a copy with ONLY the on-line-zero refinement (`online_count`) changed, to a refinement on the rescaled S(u) at 40 digits; the orbits
are read from the record's dh_offline_scan.json (untouched -- this copy writes dh_control_new_heights_rerun.json instead) and the
control tables at t = 114.163343, 166.479306, 176.702461 are reprinted.  Log: logs/dh_control_new_heights_rerun.log.
Below this banner the record script is verbatim except the lines marked RE-RUN.
"""
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
logf = open(os.path.join(HERE, 'logs', 'dh_control_new_heights_rerun.log'), 'a')   # RE-RUN
def log(s):
    print(s, flush=True); logf.write(s + '\n'); logf.flush()
T0 = time.time()
J = os.path.join(HERE, 'dh_control_new_heights_rerun.json')   # RE-RUN: output file; the record JSON is read below and never written
out = json.load(open(os.path.join(HERE, 'dh_offline_scan.json')))
out['rerun_of'] = 'dh_offline_scan.json (controls_date %s)' % out.get('controls_date')
strip = out['found_in_strip']
new = [r for r in strip if abs(r['t'] - 85.699348) >= 0.01]
log("=" * 120)
log("[%s] dh_control_new_heights_rerun.py START (RE-RUN): %d strip orbits in the JSON (%d new); controls at the first %d new heights" % (cl.now(), len(strip), len(new), n_heights))
def Zline(u): return dh.z_dh(u)[0]
# [RE-RUN 2026-09-17, Session 23 item 0(c), DH-RERUN-BRIEF.md] refinement on the rescaled S(u) = Z_DH(u)/[(5/pi)^{3/4} |Gamma(3/4 + iu/2)|]
# at 40 digits (m6-rung1-note.md section 5.3; check-O.md section 3); the sign-change scan is the record's.  max |f_DH| is accumulated.
def Sscale(u): return (5/mp.pi)**mp.mpf(0.75)*abs(mp.gamma(mp.mpf(3)/4 + 1j*mp.mpf(u)/2))
def Sline(u): return Zline(u)/Sscale(u)
RERUN_FMAX = [mp.mpf(0)]; RERUN_SMAX = [mp.mpf(0)]
def refine40(a, b):
    with mp.workdps(40):
        try: r = mp.findroot(Sline, (a, b), solver='illinois')
        except Exception: r = mp.findroot(Sline, (a + b)/2, verify=False)
        try: r = mp.findroot(Sline, r)
        except Exception: pass
        RERUN_FMAX[0] = max(RERUN_FMAX[0], abs(dh.f_dh(mp.mpc(mp.mpf(1)/2, r)))); RERUN_SMAX[0] = max(RERUN_SMAX[0], abs(Sline(r)))
        return r
def online_count(T1, T2, step=mp.mpf('0.05')):
    zs = []; u = mp.mpf(T1); zp = Zline(u)
    while u < T2:
        u2 = min(u + step, mp.mpf(T2)); zn = Zline(u2)
        if zp*zn < 0: zs.append(refine40(u, u2))      # RE-RUN (record: mp.findroot(Zline, (u, u2), solver='illinois'))
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
    log("   [RE-RUN] max |f_DH(1/2 + i gamma)| over the refined on-line zeros so far = %.2e;  max |S(gamma)| = %.2e  (criterion: max |f_DH| <= 1e-25)" % (float(RERUN_FMAX[0]), float(RERUN_SMAX[0])))
    rec['online_max_abs_f'] = float(RERUN_FMAX[0])
    log("   CAVEATS (as at 85.7): window hypothesis not verified (further orbits every ~40 units in the scan); reflection condition t >= 21 L* %s (t/L* = %.2f); reflected points omitted." % ("holds" if t >= 21*Ls1 else "FAILS", t/Ls1))
    json.dump(out, open(J, 'w'), indent=1, default=float)
out['controls_date'] = cl.now(); out['controls_seconds'] = time.time() - T0
json.dump(out, open(J, 'w'), indent=1, default=float)
log("[%s] dh_control_new_heights_rerun.py DONE in %.0f s: DH negative control available at %d further height(s) (%s)" % (cl.now(), time.time() - T0, min(n_heights, len(new)), ", ".join("%.3f" % r['t'] for r in new[:n_heights])))
