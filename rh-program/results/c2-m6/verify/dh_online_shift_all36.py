#!/usr/bin/env python3
"""dh_online_shift_all36.py -- M6 rung 1 fix pass (2026-09-17, check-O.md §3 "Exact-wording corrections for §5.3"): ALL 36 on-line
zeros of the record's +-30 window (results/c2-m2/verify/dh_negative_control_out.json, `dh_online_zeros_window`, located by the
record's recipe at dps 15), each refined at 40 digits on the gamma-normalized real function S(u) = Z_DH(u)/[(5/pi)^{3/4}
|Gamma(3/4 + iu/2)|] (the note's fix, zero_side_dh.py); printed: the displacement of every point, |f_DH(1/2 + iu)| and |Z_DH(u)|
at the recorded point, |f_DH| at the refined point, and the ranges; then W_{Z'}(L) = sum_j (gamma_j - t)^2 Bhat(L(gamma_j - t))^2
over the 36 points with the RECORDED and with the REFINED positions at L = 10, 20 and L* = 86.907 (the record's rows), by an own
trapezoid transform at 40 digits (M = 16384 nodes; spot-checked against mpmath.quad), so that the record's W_{Z'} digit strings
are compared with a computation and not with the L*.Delta-gamma estimate of the note's first version.  Budget: about a minute."""
import json, os, sys, time, datetime
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
sys.path.insert(0, os.path.join(HERE, '..', '..', 'ccm-dh-test'))
import dh
def now(): return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
t0 = time.time()
rec = json.load(open(os.path.join(HERE, '..', '..', 'c2-m2', 'verify', 'dh_negative_control_out.json')))
zs = rec['dh_online_zeros_window']; t = mp.mpf(rec['t']); Lstar = rec['L_star']
rows = {round(r['L'], 3): r for r in rec['rows']}
print(f"[{now()}] {len(zs)} recorded on-line zeros in [{float(t)-30:.3f}, {float(t)+30:.3f}]; t = {rec['t']!r}; L* = {Lstar}")
def zline(u): return dh.z_dh(u)[0]
def scale(u): return (5/mp.pi)**mp.mpf(0.75)*abs(mp.gamma(mp.mpf(3)/4 + 1j*mp.mpf(u)/2))
def sline(u): return zline(u)/scale(u)
out = []
for u in zs:
    mp.mp.dps = 20
    ur = mp.mpf(u)
    f_rec = abs(dh.f_dh(mp.mpc(0.5, ur))); z_rec = abs(zline(ur))
    mp.mp.dps = 40
    a, b = ur - mp.mpf('0.01'), ur + mp.mpf('0.01')
    if sline(a)*sline(b) < 0: r = mp.findroot(sline, (a, b), solver='illinois')
    else: r = mp.findroot(sline, ur)
    r = mp.findroot(sline, r)
    f_ref = abs(dh.f_dh(mp.mpc(0.5, r)))
    out.append(dict(recorded=u, refined=mp.nstr(r, 25), shift=float(r - ur), f_rec=float(f_rec), z_rec=float(z_rec), f_ref=float(f_ref)))
    print(f"    u = {u:<18} -> {mp.nstr(r, 20)}  shift = {float(r-ur):+.3e}  |f_DH(1/2+iu)| recorded = {float(f_rec):.3e}, refined = {float(f_ref):.2e};  |Z_DH(u)| recorded = {float(z_rec):.2e}")
sh = [abs(o['shift']) for o in out]; fr = [o['f_rec'] for o in out]
print(f"[{now()}] over the 36 points: |displacement| from {min(sh):.3e} (u = {out[sh.index(min(sh))]['recorded']}) to {max(sh):.3e} (u = {out[sh.index(max(sh))]['recorded']});  "
      f"|f_DH| at the recorded points from {min(fr):.3e} to {max(fr):.3e};  max |Z_DH| at the recorded points {max(o['z_rec'] for o in out):.2e};  max |f_DH| at the refined points {max(o['f_ref'] for o in out):.2e};  {time.time()-t0:.0f}s")
# ---- the transform and W_{Z'}
mp.mp.dps = 40
M = 16384
nodes = [mp.mpf(j)/M - mp.mpf(1)/2 for j in range(1, M)]
braw = [mp.e**(-1/(1 - 4*x*x)) for x in nodes]
Zn = mp.fsum(braw)/M
def Bhat(z):   # real z; B is even, so Bhat is real
    z = mp.mpf(z); return mp.fsum(b*mp.cos(z*x) for b, x in zip(braw, nodes))/M/Zn
def Bhat_quad(z, dps=30):
    with mp.workdps(dps):
        z = mp.mpf(z); n = max(8, int(abs(z))//3 + 8); pts = [-0.5 + k/n for k in range(n + 1)]
        Zq = mp.quad(lambda v: mp.e**(-1/(1-4*v*v)) if abs(v) < mp.mpf(1)/2 else 0, [-0.5, -0.25, 0, 0.25, 0.5])
        return mp.quad(lambda v: (mp.e**(-1/(1-4*v*v)) if abs(v) < mp.mpf(1)/2 else 0)*mp.cos(z*v), pts)/Zq
for z in (0, 37.25, 250, 869.07, 2607.2):
    print(f"    transform check: Bhat({z}) trapezoid(M = {M}, 40 digits) = {mp.nstr(Bhat(z), 12)}  mpmath.quad(30 digits) = {mp.nstr(Bhat_quad(z), 12)}  diff = {mp.nstr(abs(Bhat(z) - Bhat_quad(z)), 2)}")
def Wprime(points, L):
    L = mp.mpf(L); return mp.fsum((g - t)**2*Bhat(L*(g - t))**2 for g in points)
res = {}
for L, key in ((10, 10.0), (20, 20.0), (Lstar, round(Lstar, 3))):
    Wr = Wprime([mp.mpf(o['recorded']) for o in out], L); Wf = Wprime([mp.mpf(o['refined']) for o in out], L)
    rr = rows.get(round(L, 3)) or rows.get(key)
    rec_val = rr['W_Zprime'] if rr else None
    print(f"[{now()}] L = {L:<8}: W_Z' recorded positions = {mp.nstr(Wr, 12)} (record's own value {rec_val!r});  refined positions = {mp.nstr(Wf, 12)};  relative change (refined - recorded)/recorded = {mp.nstr((Wf - Wr)/Wr, 4)};  leading digits in common: {sum(1 for a_, b_ in zip(mp.nstr(Wr, 12).replace('.', ''), mp.nstr(Wf, 12).replace('.', '')) if a_ == b_) if True else 0}")
    res[str(L)] = dict(W_recorded_positions=mp.nstr(Wr, 15), W_refined_positions=mp.nstr(Wf, 15), record_value=rec_val, rel_change=float((Wf - Wr)/Wr))
json.dump(dict(date=now(), t=rec['t'], L_star=Lstar, points=out, shift_min=min(sh), shift_max=max(sh), f_rec_min=min(fr), f_rec_max=max(fr),
               z_rec_max=max(o['z_rec'] for o in out), f_ref_max=max(o['f_ref'] for o in out), W_Zprime=res, seconds=time.time()-t0), open('out/dh_online_shift_all36.json', 'w'), indent=1)
print(f"[{now()}] wrote out/dh_online_shift_all36.json ({time.time()-t0:.0f}s)")
