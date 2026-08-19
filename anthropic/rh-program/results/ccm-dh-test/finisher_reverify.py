"""
finisher_reverify.py -- Session-5 independent re-verification of the load-bearing
numbers (sponsor standing order 5), plus the Fuchs-law cross checks.

R1  Rebuild the four headline ground-state points and diff against the stored JSON:
      (zeta, lam=3, N=48, dps=90), (dh, lam=3, N=48, dps=90),
      (zeta, lam=2, N=48, dps=60), (dh, lam=2, N=48, dps=60).
R2  Quadrature-independence: rebuild (zeta, 2.5, 44) and (dh, 2.5, 44) at dps=100
    (different GL order K=80 vs stored K=64) and diff against margin_*.json.
R3  Fuchs re-run at mu=9 with the stored M=103 and with M=131 (grid-independence),
    plus 1-chi4 at the NON-integer mu values of the margin grid (4.84, 6.25, 7.84)
    so the ratio eps_zeta/(1-chi4) can be tabulated pointwise (CCM Fig 4 claim).
R4  DH validation (dh.py main was never archived): kappa surd vs Gauss sum, FE
    residual, the classical off-line zero near 0.8085+85.699i (Newton + residual),
    and non-multiplicativity witnesses Lambda_DH(6), Lambda_DH(10), Lambda_DH(12).
R5  CCM/Fuchs constant (2^14/3) sqrt2 pi^5 recomputed; R4-ratio trend from
    fuchs.json extrapolated linearly in 1/mu.

Output: outputs/finisher_reverify.json
"""
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
sys.path.insert(0, HERE)

import mpmath as mp

OUT = {}


def ground(kind, lam_s, N, dps):
    mp.mp.dps = dps
    import importlib
    import weilform as wf
    importlib.reload(wf)
    lam = mp.mpf(lam_s)
    T = wf.build_matrix(lam, N, kind)
    Te, To = wf.parity_blocks(T, N)
    ee = mp.eigsy(Te, eigvals_only=True)
    eo = mp.eigsy(To, eigvals_only=True)
    ee = sorted(ee[i] for i in range(Te.rows))
    eo = sorted(eo[i] for i in range(To.rows))
    return ee[0], eo[0]


# ---------------- R1
stored = {
    ('zeta', '3', 48, 90): ('4.24190738560675e-38', '1.51107117054472e-34'),
    ('dh',   '3', 48, 90): ('7.56047597027275e-7', '0.000474379833768845'),
    ('zeta', '2', 48, 60): ('8.5061276670467e-13', '5.40385974462047e-10'),
    ('dh',   '2', 48, 60): ('0.0410170083912592', '1.01731885649129'),
}
r1 = []
for (kind, lam_s, N, dps), (se, so) in stored.items():
    t0 = time.time()
    me, mo = ground(kind, lam_s, N, dps)
    rel_e = abs(me - mp.mpf(se))/mp.mpf(se)
    rel_o = abs(mo - mp.mpf(so))/mp.mpf(so)
    r1.append({'kind': kind, 'lambda': lam_s, 'N': N, 'dps': dps,
               'recomputed_min_even': mp.nstr(me, 15),
               'stored_min_even': se,
               'rel_diff_even': mp.nstr(rel_e, 3),
               'recomputed_min_odd': mp.nstr(mo, 15),
               'rel_diff_odd': mp.nstr(rel_o, 3),
               'time_s': round(time.time() - t0, 1)})
    print('R1', kind, lam_s, 'rel_e', mp.nstr(rel_e, 3), flush=True)
OUT['R1_rebuild_headline_points'] = r1

# ---------------- R2 (different dps => different GL order K = 0.8*dps => independent quadrature)
stored2 = {('zeta', '2.5', 44): '6.04470568347261e-24',
           ('dh', '2.5', 44): '0.000446453052484867'}
r2 = []
for (kind, lam_s, N), se in stored2.items():
    me, mo = ground(kind, lam_s, N, 100)
    rel = abs(me - mp.mpf(se))/mp.mpf(se)
    r2.append({'kind': kind, 'lambda': lam_s, 'N': N, 'dps_new': 100,
               'dps_stored': 80, 'recomputed_min_even': mp.nstr(me, 15),
               'stored_min_even': se, 'rel_diff': mp.nstr(rel, 3)})
    print('R2', kind, lam_s, 'rel', mp.nstr(rel, 3), flush=True)
OUT['R2_quadrature_independence'] = r2

# ---------------- R3 Fuchs
mp.mp.dps = 70
import importlib
import weilform as wf
importlib.reload(wf)


def nystrom_eigs(kernel, n):
    xs, ws = wf.gl_nodes(n)
    Y = [(x + 1)/2 for x in xs]
    W = [w/2 for w in ws]
    A = mp.matrix(n, n)
    for i in range(n):
        for j in range(i, n):
            v = mp.sqrt(W[i]*W[j])*kernel(Y[i], Y[j])
            A[i, j] = v
            A[j, i] = v
    E = mp.eigsy(A, eigvals_only=True)
    return sorted([E[i] for i in range(n)], reverse=True)


def one_minus_chi4(mu, M):
    c = 2*mp.pi*mu
    lam = mp.sqrt(mu)
    kcos = lambda u, v: 2*lam*mp.cos(c*u*v)
    chis = nystrom_eigs(kcos, M)
    return mp.mpf(1) - chis[1], mp.mpf(1) - chis[0]


r3 = {}
v103, _ = one_minus_chi4(mp.mpf(9), 103)
v131, _ = one_minus_chi4(mp.mpf(9), 131)
r3['mu9_M103'] = mp.nstr(v103, 15)
r3['mu9_M131'] = mp.nstr(v131, 15)
r3['mu9_stored'] = '3.06721128344169e-39'
r3['mu9_rel_M131_vs_stored'] = mp.nstr(abs(v131 - mp.mpf(r3['mu9_stored']))/v131, 3)
print('R3 mu=9 1-chi4:', r3['mu9_M103'], r3['mu9_M131'], flush=True)

# eps_zeta / (1-chi4) pointwise at the margin-grid mu values
zeta_eps = {'4.0': '8.88276017882314e-13', '4.84': '7.35596072747776e-17',
            '6.25': '6.04470568347261e-24', '7.84': '4.0036353511347e-32',
            '9.0': '4.24190738560675e-38'}
tab = []
for mu_s, eps_s in zeta_eps.items():
    mu = mp.mpf(mu_s)
    M = int(1.3*float(2*mp.pi*mu)) + 40
    omc4, omc0 = one_minus_chi4(mu, M)
    ratio = mp.mpf(eps_s)/omc4
    tab.append({'mu': mu_s, 'eps_zeta': eps_s, 'one_minus_chi4': mp.nstr(omc4, 12),
                'ratio_eps_over_leak': mp.nstr(ratio, 8)})
    print('R3 ratio mu=', mu_s, mp.nstr(ratio, 8), flush=True)
OUT['R3_fuchs'] = r3
OUT['R3_eps_zeta_vs_prolate_leakage'] = tab

# ---------------- R4 DH validation
mp.mp.dps = 40
import dh
importlib.reload(dh)
k1 = dh.kappa()
k2, eps_chi = dh.kappa_from_gauss_sum()
worst, pts = dh.fe_check(samples=6)
rho = dh.find_zero(mp.mpc('0.81', '85.70'))
resid = abs(dh.f_dh(rho))
lamdh = wf.lambda_dh(30)
OUT['R4_dh_validation'] = {
    'kappa_surd': mp.nstr(k1, 25),
    'kappa_gauss_sum': mp.nstr(k2, 25),
    'kappa_absdiff': mp.nstr(abs(k1 - k2), 3),
    'fe_worst_rel': mp.nstr(worst, 3),
    'offline_zero': mp.nstr(rho, 25),
    'offline_zero_residual': mp.nstr(resid, 3),
    'offline_zero_re_minus_half': mp.nstr(rho.real - mp.mpf('0.5'), 8),
    'lambda_dh_6': mp.nstr(lamdh.get(6, mp.mpf(0)), 15),
    'lambda_dh_10': mp.nstr(lamdh.get(10, mp.mpf(0)), 15),
    'lambda_dh_12': mp.nstr(lamdh.get(12, mp.mpf(0)), 15),
    'note': 'Lambda_DH supported off prime powers = broken Euler product witness',
}
print('R4 offline zero:', OUT['R4_dh_validation']['offline_zero'],
      'resid', OUT['R4_dh_validation']['offline_zero_residual'], flush=True)

# ---------------- R5 Fuchs constant + prefactor trend
mp.mp.dps = 30
cst = (mp.mpf(2)**14/3)*mp.sqrt(2)*mp.pi**5
with open('outputs/fuchs.json') as fh:
    F = json.load(fh)
xs = [1/mp.mpf(r['mu']) for r in F[-4:]]
ys = [mp.mpf(r['R4_vs_CCM_2.3634e6']) for r in F[-4:]]
n = len(xs)
sx = mp.fsum(xs); sy = mp.fsum(ys)
sxx = mp.fsum(x*x for x in xs); sxy = mp.fsum(x*y for x, y in zip(xs, ys))
slope = (n*sxy - sx*sy)/(n*sxx - sx*sx)
intercept = (sy - slope*sx)/n
OUT['R5_fuchs_constant'] = {
    'ccm_constant_2e14_3_sqrt2_pi5': mp.nstr(cst, 12),
    'R4_extrapolated_mu_inf_linear_in_1_over_mu': mp.nstr(intercept, 8),
    'R4_at_mu9': mp.nstr(ys[-1], 8),
    'ratio_extrap_over_ccm': mp.nstr(intercept/cst, 6),
}
print('R5 const', mp.nstr(cst, 10), 'extrap', mp.nstr(intercept, 8), flush=True)

with open('outputs/finisher_reverify.json', 'w') as fh:
    json.dump(OUT, fh, indent=1)
print('done outputs/finisher_reverify.json')
