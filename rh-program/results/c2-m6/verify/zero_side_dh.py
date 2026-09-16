#!/usr/bin/env python3
"""zero_side_dh.py -- M6 rung 1: the ZERO side of the explicit formula for the Davenport-Heilbronn function at t = Im rho_0,
recomputed with an own transform (trapezoid, mpmath, dps 30), in two configurations:
  (a) the RECORD configuration of verify/dh_negative_control.py: the orbit {+-t +- i delta} of rho_0 plus the on-line zeros
      with |tau - t| <= 30 (expected W_Z = -0.26981111 at L = 10, -0.74823115 at L = 20);
  (b) the FULL configuration the coefficient side sees: ALL zeros of the completed function with |tau - t| <= W0 = 60
      (on-line by sign changes of Z_DH, step 0.05, refined; off-line orbits from results/c2-m2/campaign/dh_offline_scan.json,
      refined by Newton at dps 30), their count CHECKED against the argument principle on the rectangle
      [-1, 2] x [t - W0, t + W0] (a mismatch would mean zeros missed, e.g. outside the strip), plus the 24 other recorded
      off-line orbits up to tau = 900 evaluated explicitly, plus bounds for the reflected points and the tails.
The explicit formula equates the coefficient-side value to the sum over ALL zeros, i.e. to (b), not to (a); the
difference (b) - (a) is printed.  Builder: results/ccm-dh-test/dh.py (f_dh, xi_dh, z_dh, kappa).
"""
import json, time, sys, os, datetime
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'ccm-dh-test'))
import dh

def now(): return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
t0 = time.time()
T85 = 85.69934848537759
W0 = 60.0
out = dict(date=now())

# ---------------------------------------------------------------- rho_0 and the orbit
mp.mp.dps = 30
rho0 = mp.findroot(dh.f_dh, mp.mpc('0.8085171824566', '85.69934848537759'))
print(f"[{now()}] rho_0 = {mp.nstr(rho0, 25)}  |f_DH(rho_0)| = {mp.nstr(abs(dh.f_dh(rho0)), 3)};  t used on both sides = {T85!r} (Im rho_0 - t = {mp.nstr(rho0.imag - T85, 3)})")
t = mp.mpf(T85)           # the SAME double as the coefficient side
delta0 = rho0.real - mp.mpf(1)/2
out['rho0'] = mp.nstr(rho0, 25); out['abs_f_rho0'] = mp.nstr(abs(dh.f_dh(rho0)), 3); out['delta0'] = mp.nstr(delta0, 20)

# ---------------------------------------------------------------- on-line zeros in [t - W0, t + W0]
mp.mp.dps = 20
def zline(u): return dh.z_dh(u)[0]
# RESCALED real function for the root refinement: Z_DH(u) = Re Xi_DH(1/2 + iu) has the size of |Gamma(3/4 + iu/2)| ~ e^{-pi u/4}
# (1e-30 at u = 87), so a root finder that stops on |f| < tol stops after ONE step (this is what verify/dh_negative_control.py
# and the campaign's DH scans did: their on-line zeros are off by up to 1.4e-3 -- diagnosed 2026-09-16 23:45 by the M6 rung,
# logs/dh_zero_precision_check.log).  S(u) = Z_DH(u)/[(5/pi)^{3/4} |Gamma(3/4 + iu/2)|] is real, O(1) and has the same zeros.
def scale(u): return (5/mp.pi)**mp.mpf(0.75)*abs(mp.gamma(mp.mpf(3)/4 + 1j*mp.mpf(u)/2))
def sline(u): return zline(u)/scale(u)
step = mp.mpf('0.05')
onl = []; u = t - W0; zp = sline(u)
while u < t + W0:
    u2 = u + step; zn = sline(u2)
    if zp*zn < 0:
        r_ = mp.findroot(sline, (u, u2), solver="illinois")
        if abs(r_ - t) <= W0: onl.append(r_)
    u, zp = u2, zn
mp.mp.dps = 30
onl = [mp.findroot(sline, z) for z in onl]          # polish at 30 digits (secant from the 20-digit root)
res_S = max(abs(sline(z)) for z in onl)
print(f"[{now()}] on-line zeros refined on the rescaled S(u): max |S| at the roots = {mp.nstr(res_S, 3)} (S is O(1) away from zeros); "
      f"max |f_DH(1/2 + i gamma)| = {mp.nstr(max(abs(dh.f_dh(mp.mpc(0.5, z))) for z in onl), 3)}")
out['online_max_abs_S'] = mp.nstr(res_S, 3)
print(f"[{now()}] on-line zeros of DH in [{float(t-W0):.3f}, {float(t+W0):.3f}] by sign change (step 0.05): {len(onl)};  {time.time()-t0:.0f}s")
print("    ", [round(float(z), 4) for z in onl])
out['online'] = [mp.nstr(z, 18) for z in onl]

# ---------------------------------------------------------------- off-line orbits in the window and beyond (from the scan; refined)
scan = json.load(open(os.path.join(HERE, '..', '..', 'c2-m2', 'campaign', 'dh_offline_scan.json')))
mp.mp.dps = 30
offl = []
for rec in scan['offline']:
    b, tau = rec['rho']
    r = mp.findroot(dh.f_dh, mp.mpc(b, tau))
    offl.append(r)
offl.sort(key=lambda r: r.imag)
inwin = [r for r in offl if abs(r.imag - t) <= W0]
print(f"[{now()}] off-line zeros from the scan, refined at dps 30: {len(offl)} (all with |f| <= {mp.nstr(max(abs(dh.f_dh(r)) for r in offl), 2)}); in the window: {[mp.nstr(r, 12) for r in inwin]}")
out['offline_all'] = [mp.nstr(r, 20) for r in offl]

# ---------------------------------------------------------------- argument principle on the rectangle [-1, 2] x [t - W0, t + W0]
mp.mp.dps = 20
def arg_change(path, n):
    """sum of principal arg increments of f_DH along the polyline path sampled at n points per segment; returns (total/2pi, max |step|)."""
    tot = mp.mpf(0); mx = mp.mpf(0)
    for (a, b) in zip(path[:-1], path[1:]):
        prev = None
        for k in range(n + 1):
            s = a + (b - a)*mp.mpf(k)/n
            val = dh.f_dh(s)
            if prev is not None:
                d = mp.arg(val/prev)
                tot += d; mx = max(mx, abs(d))
            prev = val
    return tot/(2*mp.pi), mx
T1 = t - W0; T2 = t + W0
corners = [mp.mpc(-1, T1), mp.mpc(2, T1), mp.mpc(2, T2), mp.mpc(-1, T2), mp.mpc(-1, T1)]
# horizontal sides: 600 samples over length 3 (step 0.005); vertical sides: 6000 samples over length 120 (step 0.02)
tot = mp.mpf(0); mx = mp.mpf(0)
for (a, b, n) in [(corners[0], corners[1], 600), (corners[1], corners[2], 6000), (corners[2], corners[3], 600), (corners[3], corners[4], 6000)]:
    c, m = arg_change([a, b], n); tot += c; mx = max(mx, m)
N_rect = tot
expected = len(onl) + 2*len(inwin)
print(f"[{now()}] argument principle on [-1,2] x [t-{W0:g}, t+{W0:g}]: N = {mp.nstr(N_rect, 8)} (max |arg step| = {mp.nstr(mx, 3)} < pi required);  "
      f"found: {len(onl)} on-line + 2 x {len(inwin)} off-line = {expected};  {time.time()-t0:.0f}s")
out['argument_principle'] = dict(N_rect=float(N_rect), max_arg_step=float(mx), found=expected, n_online=len(onl), n_offline_orbits_in_window=len(inwin))
if abs(N_rect - expected) > 0.01:
    print("    MISMATCH: zeros are missing from the located set (possibly outside the strip) -- the FULL value below is not the full value")
    out['argument_principle']['mismatch'] = True
else:
    out['argument_principle']['mismatch'] = False

# ---------------------------------------------------------------- the transform and the datum at dps 30
mp.mp.dps = 30
M = 8192
nodes = [mp.mpf(j)/M - mp.mpf(1)/2 for j in range(1, M)]
braw = [mp.e**(-1/(1 - 4*x*x)) for x in nodes]
Zs = mp.fsum(braw); wts = [b/Zs for b in braw]
def bhat(z):
    z = mp.mpc(z)
    return mp.fsum(w*mp.e**(1j*z*x) for w, x in zip(wts, nodes))
def h_f(z, L): z = mp.mpc(z); return (z - t)*bhat(L*(z - t))
def term(g, L): return h_f(g, L)*mp.conj(h_f(mp.conj(g), L))
def c_edge(lam): return mp.fsum(w*mp.cosh(lam*x) for w, x in zip(wts, nodes))
def orbit_points(r):      # the four points {+-tau +- i delta} of the orbit of a zero rho = beta + i tau: gamma = tau - i(beta - 1/2)
    tau = r.imag; d = r.real - mp.mpf(1)/2
    return [mp.mpc(tau, -d), mp.mpc(tau, d), mp.mpc(-tau, -d), mp.mpc(-tau, d)]
DERIV_NORMS_RECORD = {2: 28.7726440417, 3: 642.301196307, 4: 38779.9672465, 5: 4291724.35138, 6: 766365507.977, 7: 201117898544.0,
    8: 7.28650765558e+13, 9: 3.48429007153e+16, 10: 2.12573067064e+19, 11: 1.61134800942e+22, 12: 1.48562110881e+25, 13: 1.63707485619e+28}
def tail_bound(L, U, strip_y=0.0, C1=2.0):
    """k-route: a point at distance u with |Im| = y contributes <= (u^2 + y^2) e^{yL} N_k^2 L^{-2k} u^{-2k}; shell count 2 C1 l_R per
    unit shell (C1 = 2 as an ESTIMATE for DH's density (1/2pi) log(5 tau/2pi) [recalled, unverified]; stated, not proved)."""
    lR = mp.log(4 + t + 81*L); best = None
    for k, Nk in DERIV_NORMS_RECORD.items():
        b = 2*C1*lR*mp.e**(strip_y*L)*mp.mpf(Nk)**2*mp.mpf(L)**(-2*k)*(mp.mpf(U) - 2)**(3 - 2*k)/(2*k - 3)
        if best is None or b < best[0]: best = (b, k)
    return best

res = {}
for L in (10, 20):
    L = mp.mpf(L)
    # (a) the record configuration: orbit of rho_0 (four points) + on-line zeros with |tau - t| <= 30 (and NOT their reflections)
    onl30 = [z for z in onl if abs(z - t) <= 30]
    W_online30 = mp.fsum(term(mp.mpc(z, 0), L) for z in onl30)
    W_orbit_plus = mp.fsum(term(g, L) for g in orbit_points(rho0)[:2])      # the pair at +t
    W_orbit_minus = mp.fsum(term(g, L) for g in orbit_points(rho0)[2:])     # the reflected pair at -t
    main = -2*delta0**2*c_edge(delta0*L)**2
    W_record = W_orbit_plus + W_online30
    # (b) the full configuration in the window: all on-line zeros in +-W0, both orbits (all four points each), + the other 24 orbits
    W_online60 = mp.fsum(term(mp.mpc(z, 0), L) for z in onl)
    W_orbits_win = mp.fsum(term(g, L) for r in inwin for g in orbit_points(r))
    W_orbits_far = mp.fsum(term(g, L) for r in offl if abs(r.imag - t) > W0 for g in orbit_points(r))
    W_refl_online = mp.fsum(term(mp.mpc(-z, 0), L) for z in onl)             # the reflected on-line points -tau_j
    W_full = W_online60 + W_orbits_win + W_orbits_far + W_refl_online
    # tails: on-line zeros beyond +-W0 (C1 = 2 estimate), further off-line orbits beyond tau = 900 at depth <= 1/2 (strip weight e^{L/2})
    tb_on, k_on = tail_bound(L, W0)
    tb_off, k_off = tail_bound(L, 900 - float(t), strip_y=0.5)
    row = dict(L=float(L), W_record=mp.nstr(W_record.real, 20), W_record_imag=mp.nstr(W_record.imag, 3), W_online30=mp.nstr(W_online30.real, 12),
               W_orbit_pair_plus=mp.nstr(W_orbit_plus.real, 20), main_term=mp.nstr(main, 20), orbit_minus_main=mp.nstr(W_orbit_plus.real - main, 3),
               W_orbit_pair_minus=mp.nstr(W_orbit_minus.real, 4), W_online60=mp.nstr(W_online60.real, 12), W_orbits_window=mp.nstr(W_orbits_win.real, 20),
               W_orbits_far=mp.nstr(W_orbits_far.real, 6), W_refl_online=mp.nstr(W_refl_online.real, 4), W_full=mp.nstr(W_full.real, 20),
               W_full_imag=mp.nstr(W_full.imag, 3), full_minus_record=mp.nstr(W_full.real - W_record.real, 6),
               tail_online_bound=mp.nstr(tb_on, 3), tail_online_k=k_on, tail_offline_beyond_900_bound=mp.nstr(tb_off, 3), tail_offline_k=k_off,
               second_orbit_contribution=mp.nstr(mp.fsum(term(g, L) for r in inwin if abs(r.imag - t) > 1 for g in orbit_points(r)).real, 6))
    res[int(L)] = row
    print(f"[{now()}] ZERO SIDE DH L={int(L)}: RECORD config (orbit + {len(onl30)} on-line in +-30) W = {mp.nstr(W_record.real, 15)} (imag {mp.nstr(W_record.imag, 2)});  "
          f"pair at +t = {mp.nstr(W_orbit_plus.real, 12)} vs -2 delta^2 c^2 = {mp.nstr(main, 12)}; reflected pair = {mp.nstr(W_orbit_minus.real, 3)}")
    print(f"      FULL config (all {len(onl)} on-line in +-{W0:g}, {len(inwin)} orbits in window, {len(offl)-len(inwin)} recorded orbits beyond, reflected on-line points) "
          f"W = {mp.nstr(W_full.real, 15)};  full - record = {mp.nstr(W_full.real - W_record.real, 4)};  second orbit (114.16) = {row['second_orbit_contribution']};  "
          f"far orbits = {mp.nstr(W_orbits_far.real, 3)};  refl on-line = {mp.nstr(W_refl_online.real, 3)};  tails: on-line beyond +-{W0:g} <= {mp.nstr(tb_on, 2)} (k={k_on}, C1=2 est.), off-line beyond 900 <= {mp.nstr(tb_off, 2)}")
out['rows'] = res
out['seconds'] = time.time() - t0
json.dump(out, open(os.path.join(HERE, 'out', 'zero_side_dh.json'), 'w'), indent=1)
print(f"[{now()}] wrote out/zero_side_dh.json in {time.time()-t0:.0f}s")
