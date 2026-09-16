#!/usr/bin/env python3
"""dh_tscan_check.py -- diagnostic: the coefficient-side minus zero-side residual at L = 10 for DH AND zeta at t = 60, 85.7, 120
(zeros from out/zero_side_dh.json and out/zero_side_zeta.json; tails negligible at these distances)."""
import json, math, os, sys
import numpy as np, mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__))
M = 16384; v = np.arange(1, M)/M - 0.5
with np.errstate(all='ignore'): b = np.exp(-1/(1 - 4*v*v))
b[~np.isfinite(b)] = 0; wB = b/b.sum()
def bhat(eta):
    eta = np.atleast_1d(eta); out = np.empty_like(eta)
    for i in range(0, len(eta), 2000): out[i:i+2000] = np.cos(np.outer(eta[i:i+2000], v)) @ wB
    return out
def bracket(kind, r):
    mp.mp.dps = 20
    return float(mp.re(mp.digamma(mp.mpf(3)/4 + 1j*mp.mpf(r)/2)) + mp.log(5/mp.pi)) if kind == 'dh' else float(mp.re(mp.digamma(mp.mpf(1)/4 + 1j*mp.mpf(r)/2)) - mp.log(mp.pi))
def arch(kind, t, L, h=0.25, H=3000.0):
    eta = np.arange(-H, H + h/2, h); F = eta*eta*bhat(eta)**2
    return float(h*np.sum(F*np.array([bracket(kind, t + e/L) for e in eta]))/(2*np.pi*L**3))
zd = json.load(open(os.path.join(HERE, 'out', 'zero_side_dh.json'))); zz = json.load(open(os.path.join(HERE, 'out', 'zero_side_zeta.json')))
mp.mp.dps = 30
Mz = 8192; nodes = [mp.mpf(j)/Mz - mp.mpf(1)/2 for j in range(1, Mz)]
braw = [mp.e**(-1/(1 - 4*x*x)) for x in nodes]; Zs = mp.fsum(braw); wts = [q/Zs for q in braw]
def bh(z): z = mp.mpc(z); return mp.fsum(w*mp.e**(1j*z*x) for w, x in zip(wts, nodes))
def W(points, t, L): return mp.fsum((g - t)*bh(L*(g - t))*mp.conj((mp.conj(g) - t)*bh(L*(mp.conj(g) - t))) for g in points)
dh_on = [mp.mpc(mp.mpf(z), 0) for z in zd['online']]
dh_off = []
for z in zd['offline_all']:
    r = complex(z.replace(' ', '')); tau, d = r.imag, r.real - 0.5
    dh_off += [mp.mpc(tau, -d), mp.mpc(tau, d)]
ze = [mp.mpc(mp.mpf(g), 0) for n, g in zz['t85_zeros']]
L = 10
for kind, pts in (('dh', dh_on + dh_off), ('zeta', ze)):
    for t in (60.0, 85.69934848537759, 120.0):
        tag = {60.0: 't60', 120.0: 't120'}.get(t, 't85p7')
        rs = json.load(open(os.path.join(HERE, 'out', f'{kind}_{tag}_L10.json')))
        A_ = arch(kind, t, L); Wz = float(W(pts, mp.mpf(t), L).real); Wr = A_ - rs['P_dd']
        print(f"  {kind:5} t={t:8.3f} L=10: ARCH = {A_:+.12f}  P = {rs['P_dd']:+.12f}  W_rhs = {Wr:+.12f}  W_zero = {Wz:+.12f}  diff = {Wr - Wz:+.3e}")
