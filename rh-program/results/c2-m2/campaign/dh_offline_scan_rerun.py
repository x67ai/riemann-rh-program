#!/usr/bin/env python3
"""dh_offline_scan_rerun.py -- RE-RUN of dh_offline_scan.py (Session 23 item 0(c), 2026-09-17; DH-RERUN-BRIEF.md): the orbit
search is NOT redone -- the record's blocks and 26 orbits are read from dh_offline_scan.json (they were located on f_DH itself and
stand); ONLY the on-line-zero location of the control stage (`online_count`) is changed, to a refinement on the rescaled S(u) at 40
digits, and the control rows at the first two new heights are reprinted.  Log: logs/dh_offline_scan_rerun.log; JSON:
dh_offline_scan_rerun.json.  The record files are not written.  Below this banner the record script is verbatim except the blocks
marked RE-RUN (the scan loop is replaced by the JSON read).
"""
"""dh_offline_scan.py -- the DH sub-task of PRICING 2(c) / BRIEF rule 4: scan the Davenport-Heilbronn function f_DH for
one more off-line orbit in the strip at height <= 1e3 (30-minute cap), reusing results/ccm-dh-test/dh.py (the builder
finisher_dh_zeros.py imports) and its on-line sign-change scan; if found, run the zero-side control there exactly as
verify/dh_negative_control.py did at t = 85.7 (the campaign library's datum on DH's own on-line zeros + the orbit).
INSTRUMENT (V.4 negative control at a second height); nothing about RH.

Method.  N_DH(T) := number of zeros of f_DH with 0 < Im s < T (all real parts) = (theta(T) + arg f_DH(1/2 + iT))/pi + n_0,
with theta(T) = (T/2) log(5/pi) + Im log Gamma(3/4 + iT/2) (the completed function's phase; dh_negative_control.py) and
arg f_DH(1/2 + iT) by continuous variation along the horizontal segment from sigma = 3 (where |f_DH - 1| < 0.21, principal
argument) down to sigma = 1/2 in steps that keep consecutive arguments within pi/2 (halving otherwise); n_0 is fixed on
[0, 46] against the finisher's on-line list (all DH zeros below 46 are on the line -- Spira; checked here by the same count).
Per block [T1, T2] of height 5 (T1, T2 moved off any tiny |Z_DH|): excess := N_DH(T2) - N_DH(T1) - #(on-line sign changes
of Z_DH at step 0.05).  Excess 2 => one pair of zeros off the line in the block: located by Newton on f_DH from seeds
(beta0, tau) with beta0 in {0.6, 0.75, 0.9, 1.1, 1.3} and tau the block's centroid of the missing pair (the sum of the zeros
in the block by the contour integral (1/2 pi i) oint s f'/f minus the on-line sum); classified as IN THE STRIP (0 < beta < 1,
beta != 1/2 -- an orbit for the control) or OUTSIDE (beta > 1: not a point of any configuration in C(C1), corrections 12.4).
The known orbit at 85.699 must be re-found (the scanner's own positive control).
"""
import sys, os, json, math, time, signal
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '..', 'ccm-dh-test'))
import mpmath as mp, numpy as np
import dh, campaign_lib as cl

CAP_S = 30*60
T0 = time.time()
logf = open(os.path.join(HERE, 'logs', 'dh_offline_scan_rerun.log'), 'a')   # RE-RUN
def log(s):
    print(s, flush=True); logf.write(s + '\n'); logf.flush()
log("=" * 120)
log("[%s] dh_offline_scan_rerun.py START (RE-RUN; record log line follows) (cap %d s)  [attempt 4, 21:52 IST: attempt 3's mp.findroot locator wandered to huge |Im s| from far seeds (seconds per Hurwitz zeta) -- replaced by a bounded damped Newton from |f|-grid seeds; attempt 1 spent its time in an absolute |Z| test that Xi_DH's e^{-pi T/4} decay can never pass; attempt 2 (5-unit blocks, line step 0.05, contour-integral locator) ran at 35 s/block and re-found rho_0 = 0.808517182457 + 85.699348485 i, |f| = 2.4e-15 (its log is above); this attempt: 10-unit blocks, line step 0.1 with fine rescan, cheaper argument walk, Newton seed grid]" % (cl.now(), CAP_S))
mp.mp.dps = 15
out = dict(date=cl.now(), blocks=[], offline=[], found_in_strip=[], cap_s=CAP_S)
def elapsed(): return time.time() - T0

def theta(T):
    T = mp.mpf(T); return T/2*mp.log(5/mp.pi) + mp.im(mp.loggamma(mp.mpf(3)/4 + 1j*T/2))
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
def arg_track(T):
    """arg f_DH(sigma + iT) by continuous variation from sigma = 3 to 1/2: step 0.5 down to sigma = 1.25, then 0.05 to 1/2,
    halving whenever a jump exceeds pi/2 (a zero near the segment), to a floor of 1e-4."""
    s0 = mp.mpf(3); a = mp.arg(dh.f_dh(mp.mpc(s0, T)))
    if abs(a) > 0.5: log("   !! |arg f(3 + i%.3f)| = %.3f > 0.5 -- unexpected" % (T, float(a)))
    sig = s0; target = mp.mpf('0.5')
    while sig > target:
        base = mp.mpf('0.5') if sig > 1.25 else mp.mpf('0.05')
        step = base
        while True:
            nxt = max(target, sig - step)
            b = mp.arg(dh.f_dh(mp.mpc(nxt, T)))
            d = b - a
            while d > mp.pi: d -= 2*mp.pi
            while d < -mp.pi: d += 2*mp.pi
            if abs(d) > mp.pi/2 and step > mp.mpf('1e-4'):
                step /= 2; continue
            break
        a = a + d; sig = nxt
    return a
def N_DH(T):
    return float((theta(T) + arg_track(T))/mp.pi)
def safe_T(T):
    """move T so that |Z_DH(T)| is not tiny (no zero on the block boundary)."""
    T = mp.mpf(T)
    for k in range(20):
        v = Zline(T)
        # Xi_DH decays like e^{-pi T/4} (1e-307 at T = 900), so the test is RELATIVE to the neighbors
        if abs(v) > 1e-3*max(abs(Zline(T + mp.mpf('0.1'))), abs(Zline(T - mp.mpf('0.1')))): return T
        T += mp.mpf('0.013')
    return T
def online_count(T1, T2, step=mp.mpf('0.1')):
    zs = []; u = mp.mpf(T1); zp = Zline(u)
    while u < T2:
        u2 = min(u + step, mp.mpf(T2)); zn = Zline(u2)
        if zp*zn < 0: zs.append(refine40(u, u2))      # RE-RUN (record: mp.findroot(Zline, (u, u2), solver='illinois'))
        u, zp = u2, zn
    return zs

# [RE-RUN] the orbit search is NOT redone: the record's calibration, blocks and orbits are read from dh_offline_scan.json
REC = json.load(open(os.path.join(HERE, 'dh_offline_scan.json')))
for k in ('n0', 'n_low_46', 'blocks', 'offline', 'cap_hit_at'):
    if k in REC: out[k] = REC[k]
out['found_in_strip'] = [dict((kk, vv) for kk, vv in r.items() if kk not in ('control_rows', 'online_window', 'abs_f_refined')) for r in REC['found_in_strip']]
out['rerun_of'] = 'dh_offline_scan.json (date %s); the record scan stage of this script is skipped, see the banner' % REC.get('date')
log("   [RE-RUN] record scan read from dh_offline_scan.json: %d blocks, %d off-line zeros, %d in the strip, n_0 = %.3f, cap hit at %s" % (len(out['blocks']), len(out['offline']), len(out['found_in_strip']), out['n0'], out.get('cap_hit_at')))
strip = [r for r in out['found_in_strip']]
known = [r for r in strip if abs(r['t'] - 85.699348) < 0.01]
new = [r for r in strip if abs(r['t'] - 85.699348) >= 0.01]
log("   scanner's own control: the known orbit at 85.699 %s" % ("RE-FOUND" if known else "NOT re-found (scanner defect)"))
log("   further off-line orbits IN THE STRIP at height <= 1e3: %d  %s" % (len(new), [(round(r['rho'][0], 6), round(r['rho'][1], 6)) for r in new]))
out['known_refound'] = bool(known); out['new_in_strip'] = new

# the zero-side control at the new height(s), as at 85.7 (dh_negative_control.py): orbit + DH on-line zeros in a window
for rec in new[:2]:
    if elapsed() > CAP_S - 60: log("   cap: no time for the control at t = %.4f" % rec['t']); break
    t = rec['t']; d = rec['delta']
    Wd = 30.0
    onl = online_count(mp.mpf(t - Wd), mp.mpf(t + Wd))
    g = np.array([float(z) for z in onl])
    log("   CONTROL at t = %.6f, delta = %.6f: %d DH on-line zeros in [t-30, t+30]" % (t, d, len(g)))
    Ls = [10, 20, 30, 40, 50, 60, 70, cl.Lstar(d, t, 1), 100]
    rows = []
    for L in Ls:
        nz = cl.noise_at(t, g, float(L), Wd)
        c = float(cl.c_edge([d*L])[0]); main = -2*d*d*c*c; WZ = nz['N_Z'] + main; bound = d*d*math.exp(d*L/2)
        rows.append(dict(L=L, W_Z=WZ, W_Zprime=nz['N_Z'], main=main, sep=abs(WZ - nz['N_Z']), bound=bound, ratio=abs(WZ - nz['N_Z'])/bound))
        log("   L=%7.2f: W_Z = %.6e  W_Z' = %.6e  main = %.6e  |W_Z - W_Z'|/bound = %.4g  fires(>=1): %s" % (L, WZ, nz['N_Z'], main, rows[-1]['ratio'], rows[-1]['sep'] >= 1))
    rec['control_rows'] = rows; rec['online_window'] = [float(x) for x in g]
    log("   [RE-RUN] max |f_DH(1/2 + i gamma)| over the refined on-line zeros so far = %.2e;  max |S(gamma)| = %.2e  (criterion: max |f_DH| <= 1e-25)" % (float(RERUN_FMAX[0]), float(RERUN_SMAX[0])))
    rec['online_max_abs_f'] = float(RERUN_FMAX[0])
    log("   CAVEATS (as at 85.7): the window hypothesis (all other points real within R_0 L*) is not verified; the reflection condition t >= 21 L* %s at this t; the reflected points are omitted." % ("holds" if t >= 21*cl.Lstar(d, t, 1) else "FAILS"))
out['date_end'] = cl.now(); out['seconds'] = elapsed()
json.dump(out, open(os.path.join(HERE, 'dh_offline_scan_rerun.json'), 'w'), indent=1, default=float)   # RE-RUN
log("[%s] dh_offline_scan_rerun.py DONE in %.0f s; verdict: %s" % (cl.now(), elapsed(), ("DH control available at %d further height(s)" % len(new)) if new else "DH at one height only (no further off-line orbit in the strip found below %s)" % (out.get('cap_hit_at', 1000))))
