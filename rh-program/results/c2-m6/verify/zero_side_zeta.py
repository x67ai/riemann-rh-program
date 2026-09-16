#!/usr/bin/env python3
"""zero_side_zeta.py -- M6 rung 1: the ZERO side W_zeta(f_{t,L}) = sum_rho m_rho ghat(gamma_rho), recomputed at 30+ digits
with an own transform (trapezoid rule in mpmath, M = 8192 nodes, dps 40), at (t, L) = (85.7, 10), (85.7, 20) from
mpmath.zetazero at dps 30, and at (1e6, 10), (1e6, 20) from the campaign's zeros file
results/c2-m2/campaign/zeros_t1e6.json (1133 zeros with |gamma - t| <= 297.22; 20 of them re-verified here at dps 30).

For a real zero gamma the term is |h_f(gamma)|^2 = (gamma - t)^2 Bhat(L (gamma - t))^2 (identity (0.1)); the sum runs over
ALL zeros rho, i.e. over +gamma_n and -gamma_n (the reflected points), which contribute (gamma_n + t)^2 Bhat(L(gamma_n + t))^2.
Truncation: zeros with gamma > t + U (and reflected points beyond) are bounded by the campaign's k-route
(campaign_lib.py docstring): tail <= 2 l_R N_k^2 L^{-2k} (U - 2)^{3 - 2k}/(2k - 3), N_k = ||B^(k)||_1 (DERIV_NORMS_RECORD,
k <= 13; C_1 = 1 operative for zeta, stated as such), minimized over k.
"""
import json, time, sys, os, datetime
import mpmath as mp

T85 = 85.69934848537759
def now(): return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
t0 = time.time()
DERIV_NORMS_RECORD = {1: 3.31427535948, 2: 28.7726440417, 3: 642.301196307, 4: 38779.9672465, 5: 4291724.35138, 6: 766365507.977,
    7: 201117898544.0, 8: 7.28650765558e+13, 9: 3.48429007153e+16, 10: 2.12573067064e+19, 11: 1.61134800942e+22,
    12: 1.48562110881e+25, 13: 1.63707485619e+28}   # campaign_lib.py (30-digit quadrature; k = 1..3 = the record's)

# ---------------------------------------------------------------- transform at dps 40, trapezoid M = 8192
mp.mp.dps = 40
M = 8192
nodes = [mp.mpf(j)/M - mp.mpf(1)/2 for j in range(1, M)]
braw = [mp.e**(-1/(1 - 4*x*x)) for x in nodes]
Zs = mp.fsum(braw)
wts = [b/Zs for b in braw]                      # sum = 1
def bhat(eta):
    eta = mp.mpf(eta)
    return mp.fsum(w*mp.cos(eta*x) for w, x in zip(wts, nodes))
# check against mpmath quadrature (dps 30) at three arguments
mp.mp.dps = 30
def braw_mp(x):
    x = mp.mpf(x); return mp.e**(-1/(1 - 4*x*x)) if abs(x) < mp.mpf(1)/2 else mp.mpf(0)
Zq = mp.quad(braw_mp, [-0.5, -0.25, 0, 0.25, 0.5])
def bhat_q(eta):
    eta = mp.mpf(eta); n = max(8, int(abs(eta))//3 + 8)
    return mp.quad(lambda x: braw_mp(x)*mp.cos(eta*x), [-0.5 + k/n for k in range(n+1)])/Zq
mp.mp.dps = 40
chk = [(e, mp.nstr(bhat(e), 20), mp.nstr(bhat_q(e), 20), mp.nstr(bhat(e) - bhat_q(e), 3)) for e in (0, 5.5, 37.25, 250)]
print(f"[{now()}] Z_trap(M=8192) = {mp.nstr(Zs/M, 20)}  Z_quad = {mp.nstr(Zq, 20)};  Bhat trapezoid(dps40) vs quad(dps30): {chk}")

def tail_bound(L, U, t, R=81.0):
    """campaign k-route tail bound beyond radius U (C_1 = 1 operative), minimized over 2 <= k <= 13."""
    lR = mp.log(4 + t + R*L)
    best = None
    for k in range(2, 14):
        Nk = mp.mpf(DERIV_NORMS_RECORD[k])
        b = 2*lR*Nk**2*mp.mpf(L)**(-2*k)*(mp.mpf(U) - 2)**(3 - 2*k)/(2*k - 3)
        if best is None or b < best[0]: best = (b, k)
    return best

out = dict(date=now(), bhat_check=chk, M=M, dps=40)

# ---------------------------------------------------------------- t = 85.7: zeros from zetazero at dps 30
mp.mp.dps = 30
U = 150.0
zs = []; n = 1
while True:
    g = mp.zetazero(n).imag
    if g > T85 + U: break
    zs.append((n, g)); n += 1
print(f"[{now()}] zeta zeros to gamma <= t + {U}: {len(zs)} zeros (n = 1..{len(zs)}), last gamma = {mp.nstr(zs[-1][1], 12)}; {time.time()-t0:.0f}s")
out['t85_zeros'] = [(n, mp.nstr(g, 25)) for n, g in zs]
mp.mp.dps = 40
res85 = {}
for L in (10, 20):
    t = mp.mpf(T85); L = mp.mpf(L)
    terms = []; refl = []
    for n, g in zs:
        u = g - t
        terms.append(u*u*bhat(L*u)**2)
        ur = g + t
        refl.append(ur*ur*bhat(L*ur)**2)
    S = mp.fsum(terms); R = mp.fsum(refl)
    tb, k = tail_bound(float(L), U, float(t))
    tbr, kr = tail_bound(float(L), float(zs[-1][1] + t), float(t))
    # the largest single term and the term of the zero nearest t, for the record
    big = max(terms); near = min(zs, key=lambda z: abs(z[1] - t))
    res85[float(L)] = dict(W_direct=mp.nstr(S, 25), W_reflected=mp.nstr(R, 6), tail_bound=mp.nstr(tb, 4), tail_k=k,
                          tail_bound_reflected=mp.nstr(tbr, 4), n_zeros=len(zs), U=U, largest_term=mp.nstr(big, 6),
                          nearest_zero=(near[0], mp.nstr(near[1], 15)), W_total=mp.nstr(S + R, 25))
    print(f"[{now()}] ZERO SIDE zeta t=85.7 L={float(L):g}: sum over {len(zs)} zeros = {mp.nstr(S, 20)};  reflected points = {mp.nstr(R, 4)};  "
          f"tail beyond U={U}: <= {mp.nstr(tb, 3)} (k={k}); reflected tail <= {mp.nstr(tbr, 3)};  W = {mp.nstr(S + R, 20)}")
out['t85'] = res85

# ---------------------------------------------------------------- t = 1e6: the campaign's zeros, own transform; 20 re-verified
zf = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'c2-m2', 'campaign', 'zeros_t1e6.json')))
gam = [(z[0], mp.mpf(z[1])) for z in zf['zeros']]
print(f"[{now()}] campaign zeros_t1e6.json: {len(gam)} zeros, U_data = {zf['U_data']}, dps = {zf['dps']}, checks = {zf['checks']}")
# re-verify 20 zeros at dps 30 (every 56th index)
mp.mp.dps = 30
ver = []
for i in range(0, len(gam), max(1, len(gam)//20))[:20]:
    n, g = gam[i]
    g30 = mp.zetazero(n).imag
    ver.append((n, mp.nstr(g, 17), mp.nstr(g30, 25), mp.nstr(g30 - g, 3)))
worst = max(abs(mp.mpf(v[3])) for v in ver)
print(f"[{now()}] 20 zeros re-verified at dps 30: worst |delta gamma| = {mp.nstr(worst, 3)}; {time.time()-t0:.0f}s")
out['t1e6_verify'] = ver; out['t1e6_worst_dgamma'] = mp.nstr(worst, 3)
mp.mp.dps = 40
rows = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'c2-m2', 'campaign', 'rows_t1e6.json')))
res6 = {}
for L in (10, 20):
    t = mp.mpf(1000000); Lm = mp.mpf(L)
    terms = [(g - t)**2*bhat(Lm*(g - t))**2 for n, g in gam]
    S = mp.fsum(terms)
    tb, k = tail_bound(L, float(zf['U_data']), 1e6)
    tbr, kr = tail_bound(L, 2e6 - float(zf['U_data']), 1e6)     # reflected points: radius >= 2t - U_data
    camp = [r for r in rows if abs(r['L'] - L) < 1e-9 and abs(r['delta'] - 0.1) < 1e-9][0]
    res6[L] = dict(W_direct=mp.nstr(S, 25), tail_bound=mp.nstr(tb, 4), tail_k=k, reflected_bound=mp.nstr(tbr, 4), n_zeros=len(gam),
                   campaign_N_Z=camp['N_Z'], diff_vs_campaign=mp.nstr(S - mp.mpf(camp['N_Z']), 4), campaign_tail=camp['tail_bound_at_U_row'])
    print(f"[{now()}] ZERO SIDE zeta t=1e6 L={L}: sum over {len(gam)} zeros (own transform, dps 40) = {mp.nstr(S, 20)};  campaign rows_t1e6 N_Z = {camp['N_Z']!r};  "
          f"diff = {mp.nstr(S - mp.mpf(camp['N_Z']), 3)};  tail beyond U_data <= {mp.nstr(tb, 3)} (k={k}); reflected <= {mp.nstr(tbr, 3)}")
out['t1e6'] = res6
out['seconds'] = time.time() - t0
json.dump(out, open('out/zero_side_zeta.json', 'w'), indent=1)
print(f"[{now()}] wrote out/zero_side_zeta.json in {time.time()-t0:.0f}s")
