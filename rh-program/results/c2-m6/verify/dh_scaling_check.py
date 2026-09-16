#!/usr/bin/env python3
"""dh_scaling_check.py -- diagnostic: the DH coefficient-side minus zero-side residual as a function of L (5, 7, 10, 12, 15, 20),
to identify its origin (an L^-3 law = a constant error in the archimedean bracket; a fast decay = a zero-type term)."""
import json, math, os, sys, datetime
import numpy as np, mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'ccm-dh-test')); import dh
T85 = 85.69934848537759
# ARCH (numpy trapezoid Bhat, M=16384) with the DH bracket
M = 16384; v = np.arange(1, M)/M - 0.5
with np.errstate(all='ignore'): b = np.exp(-1/(1 - 4*v*v))
b[~np.isfinite(b)] = 0; wB = b/b.sum()
def bhat(eta):
    eta = np.atleast_1d(eta); out = np.empty_like(eta)
    for i in range(0, len(eta), 2000): out[i:i+2000] = np.cos(np.outer(eta[i:i+2000], v)) @ wB
    return out
def bracket_dh(r):
    mp.mp.dps = 20; return float(mp.re(mp.digamma(mp.mpf(3)/4 + 1j*mp.mpf(r)/2)) + mp.log(5/mp.pi))
def arch(L, h=0.25, H=3000.0):
    eta = np.arange(-H, H + h/2, h); F = eta*eta*bhat(eta)**2
    br = np.array([bracket_dh(T85 + e/L) for e in eta])
    return float(h*np.sum(F*br)/(2*np.pi*L**3))
# zero side from the saved zeros (dps 30 trapezoid)
zd = json.load(open(os.path.join(HERE, 'out', 'zero_side_dh.json')))
mp.mp.dps = 30
t = mp.mpf(T85)
onl = [mp.mpf(z) for z in zd['online'] if abs(mp.mpf(z) - t) <= 60]
offl = [mp.mpc(complex(z.replace(' ', ''))) for z in zd['offline_all']]
Mz = 8192; nodes = [mp.mpf(j)/Mz - mp.mpf(1)/2 for j in range(1, Mz)]
braw = [mp.e**(-1/(1 - 4*x*x)) for x in nodes]; Zs = mp.fsum(braw); wts = [q/Zs for q in braw]
def bh(z): z = mp.mpc(z); return mp.fsum(w*mp.e**(1j*z*x) for w, x in zip(wts, nodes))
def hf(z, L): z = mp.mpc(z); return (z - t)*bh(L*(z - t))
def term(g, L): return hf(g, L)*mp.conj(hf(mp.conj(g), L))
def orbit_pts(r): tau = r.imag; d = r.real - mp.mpf(1)/2; return [mp.mpc(tau, -d), mp.mpc(tau, d), mp.mpc(-tau, -d), mp.mpc(-tau, d)]
print("   L      P (coeff side)        ARCH_DH               W_rhs = ARCH - P        W_zero (full, +-60)     W_rhs - W_zero    ratio to L=10 value")
rows = []; d10 = None
for L in (5, 7, 10, 12, 15, 20):
    rs = json.load(open(os.path.join(HERE, 'out', f'dh_t85p7_L{L}.json')))
    A_ = arch(L)
    Wz = mp.fsum(term(mp.mpc(z, 0), L) for z in onl) + mp.fsum(term(g, L) for r in offl for g in orbit_pts(r))
    Wr = A_ - rs['P_dd']; d = Wr - float(Wz.real)
    if L == 10: d10 = d
    rows.append(dict(L=L, P=rs['P_dd'], arch=A_, W_rhs=Wr, W_zero=float(Wz.real), diff=d))
    print(f"  {L:3d}  {rs['P_dd']:+.15f}  {A_:+.15f}  {Wr:+.15f}  {float(Wz.real):+.15f}  {d:+.3e}")
for r in rows: r['ratio_to_L10'] = r['diff']/d10
print("ratios diff(L)/diff(10):", [(r['L'], round(r['ratio_to_L10'], 4)) for r in rows], " -- an L^-3 law would give", [(L, round((10/L)**3, 4)) for L in (5, 7, 10, 12, 15, 20)])
json.dump(rows, open(os.path.join(HERE, 'out', 'dh_scaling_check.json'), 'w'), indent=1)
