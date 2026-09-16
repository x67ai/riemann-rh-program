#!/usr/bin/env python3
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
logf = open(os.path.join(HERE, 'logs', 'dh_offline_scan.log'), 'a')
def log(s):
    print(s, flush=True); logf.write(s + '\n'); logf.flush()
log("=" * 120)
log("[%s] dh_offline_scan.py START (cap %d s)  [attempt 4, 21:52 IST: attempt 3's mp.findroot locator wandered to huge |Im s| from far seeds (seconds per Hurwitz zeta) -- replaced by a bounded damped Newton from |f|-grid seeds; attempt 1 spent its time in an absolute |Z| test that Xi_DH's e^{-pi T/4} decay can never pass; attempt 2 (5-unit blocks, line step 0.05, contour-integral locator) ran at 35 s/block and re-found rho_0 = 0.808517182457 + 85.699348485 i, |f| = 2.4e-15 (its log is above); this attempt: 10-unit blocks, line step 0.1 with fine rescan, cheaper argument walk, Newton seed grid]" % (cl.now(), CAP_S))
mp.mp.dps = 15
out = dict(date=cl.now(), blocks=[], offline=[], found_in_strip=[], cap_s=CAP_S)
def elapsed(): return time.time() - T0

def theta(T):
    T = mp.mpf(T); return T/2*mp.log(5/mp.pi) + mp.im(mp.loggamma(mp.mpf(3)/4 + 1j*T/2))
def Zline(u): return dh.z_dh(u)[0]
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
        if zp*zn < 0: zs.append(mp.findroot(Zline, (u, u2), solver='illinois'))
        u, zp = u2, zn
    return zs

# n_0 on [0.4, 46]: the finisher's on-line zeros (all DH zeros below 46 are on the line) fix the additive constant
Tlow = safe_T(mp.mpf('46'))
n_low = len(online_count(mp.mpf('0.4'), Tlow))
n0 = n_low - N_DH(Tlow)
log("   calibration: %d on-line zeros of DH in (0.4, %.3f) by sign changes; phase count (theta + arg)/pi = %.3f; n_0 = %.3f (should be near an integer + 0)" % (n_low, float(Tlow), N_DH(Tlow), n0))
out['n0'] = n0; out['n_low_46'] = n_low
# blocks of height 10 from 46 to 1000 (coarse line step 0.1; fine rescan at 0.01 on any excess)
edges = [Tlow]
Tb = 50.0
while Tb < 1000 + 1e-9:
    edges.append(safe_T(Tb)); Tb += 10.0
Nprev = N_DH(edges[0]) + n0
for i in range(len(edges) - 1):
    if elapsed() > CAP_S - 120:
        log("   [%s] CAP reached at block [%.2f, %.2f]: scan stops here (heights above are unscanned)" % (cl.now(), float(edges[i]), float(edges[i+1]))); out['cap_hit_at'] = float(edges[i]); break
    T1, T2 = edges[i], edges[i+1]
    Nnext = N_DH(T2) + n0
    cnt_phase = Nnext - Nprev
    onl = online_count(T1, T2)
    excess = int(round(cnt_phase)) - len(onl)
    blk = dict(T1=float(T1), T2=float(T2), phase_count=cnt_phase, online=len(onl), excess=excess)
    if excess != 0:
        # rescan the line finely before declaring
        onl2 = online_count(T1, T2, step=mp.mpf('0.01'))
        excess2 = int(round(cnt_phase)) - len(onl2); blk['online_fine'] = len(onl2); blk['excess_fine'] = excess2
        if excess2 > 0:
            # locate: |f_DH| on a grid over the block (beta in [0.55, 1.2] step 0.05, tau step 0.25) picks the six best seeds;
            # a damped Newton (f'/f by mp.diff) that must stay inside the block (Re in [-0.5, 2], Im in [T1 - 1, T2 + 1]) refines
            # them (15 steps, stop at |f| < 1e-12); accepted once (distinct to 1e-6), beta != 1/2
            found = []
            grid = []
            tau = float(T1)
            while tau <= float(T2):
                for bb in [0.55 + 0.05*k for k in range(14)]:
                    sd = mp.mpc(bb, tau); grid.append((abs(dh.f_dh(sd)), sd))
                tau += 0.25
            grid.sort(key=lambda x: x[0])
            for _, sd in grid[:6]:
                x = sd; ok = False
                for it in range(15):
                    f = dh.f_dh(x)
                    if abs(f) < 1e-12: ok = True; break
                    fp = mp.diff(dh.f_dh, x)
                    if fp == 0: break
                    dx = f/fp
                    if abs(dx) > 0.5: dx = dx/abs(dx)*0.5
                    x = x - dx
                    if not (-0.5 < mp.re(x) < 2 and T1 - 1 < mp.im(x) < T2 + 1): break
                if ok and abs(mp.re(x) - 0.5) > 1e-6 and all(abs(x - q) > 1e-6 for q in found):
                    found.append(x)
            blk['tau_guess'] = None; beta_bar = float('nan')
            for r in found:
                beta = float(mp.re(r)); tau_r = float(mp.im(r))
                in_strip = (0 < beta < 1) and abs(beta - 0.5) > 1e-8
                rec = dict(rho=[beta, tau_r], abs_f=float(abs(dh.f_dh(r))), in_strip=in_strip, t=tau_r, delta=abs(beta - 0.5))
                out['offline'].append(rec)
                if in_strip: out['found_in_strip'].append(rec)
                log("   [%s] block [%.2f, %.2f]: phase count %.3f, on-line %d (fine %d), excess %d -> zero located at rho = %.12f + %.9f i, |f| = %.1e, %s" % (cl.now(), float(T1), float(T2), cnt_phase, len(onl), len(onl2), excess2, beta, tau_r, rec['abs_f'], "IN THE STRIP (off-line orbit)" if in_strip else "outside the strip (beta > 1 or < 0)"))
            if not found:
                log("   [%s] block [%.2f, %.2f]: excess %d but Newton found no zero from the seed grid -- recorded, unresolved" % (cl.now(), float(T1), float(T2), excess2))
        else:
            log("   block [%.2f, %.2f]: coarse excess %d resolved by the fine line scan (%d on-line)" % (float(T1), float(T2), excess, len(onl2)))
    out['blocks'].append(blk)
    if (i % 10) == 0: log("   [%s] block %d/%d [%.1f, %.1f]: phase %.3f on-line %d excess %d  (%.0f s elapsed)" % (cl.now(), i, len(edges) - 1, float(T1), float(T2), cnt_phase, len(onl), excess, elapsed()))
    Nprev = Nnext
    json.dump(out, open(os.path.join(HERE, 'dh_offline_scan.json'), 'w'), indent=1, default=float)

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
    log("   CAVEATS (as at 85.7): the window hypothesis (all other points real within R_0 L*) is not verified; the reflection condition t >= 21 L* %s at this t; the reflected points are omitted." % ("holds" if t >= 21*cl.Lstar(d, t, 1) else "FAILS"))
out['date_end'] = cl.now(); out['seconds'] = elapsed()
json.dump(out, open(os.path.join(HERE, 'dh_offline_scan.json'), 'w'), indent=1, default=float)
log("[%s] dh_offline_scan.py DONE in %.0f s; verdict: %s" % (cl.now(), elapsed(), ("DH control available at %d further height(s)" % len(new)) if new else "DH at one height only (no further off-line orbit in the strip found below %s)" % (out.get('cap_hit_at', 1000))))
