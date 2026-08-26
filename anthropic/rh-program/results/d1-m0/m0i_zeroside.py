"""m0i_zeroside.py -- zero-side consistency check for the M0(i) certification:
for a certified witness v, the Weil explicit formula (DH: entire, no pole term)
says   Q_DH(v) = sum_{on-line rho} |fhat(gamma_j)|^2  +  S_off(v),
with S_off(v) = 4 Re[ fhat(gamma - i delta) * conj(fhat(gamma + i delta)) ]
(the off-line quadruple at t = +-85.699, beta = 0.8085; real even f).
Rebuilds fhat from the frozen witness, sums over the computed on-line zeros
(m0i_dh_zeros.py list), and compares against the matrix-side Q.  Validates the
S_off normalization/sign convention used in the reconciliation analysis
independently of the matrix build (convention lineage: test_conventions.py T2).

Usage: python3 m0i_zeroside.py RUNG.json ZEROS.json OUT.json
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import mpmath as mp

from m0i_certify import BETA_S, GAMMA_S, sector_hat

rung = json.load(open(sys.argv[1]))
zdata = json.load(open(sys.argv[2]))

mp.mp.dps = 40
pnum, pden = rung['lambda_rational']
lam = mp.mpf(pnum)/mp.mpf(pden)
L = 2*mp.log(lam)
N = rung['N']
v = [mp.mpf(s) for s in rung['witness']['even']]

def fhat(t):
    sh = sector_hat(N, L, t, 'even')
    return mp.fsum(v[i]*sh[i] for i in range(N + 1))

zs = [mp.mpf(s) for s in zdata['online_zeros']]
gam = mp.mpf(GAMMA_S)
delta = mp.mpf(BETA_S) - mp.mpf('0.5')

terms = [2*abs(fhat(g))**2 for g in zs]
q_on_100 = mp.fsum(t for t, g in zip(terms, zs) if g <= 100)
q_on = mp.fsum(terms)
s_off = 4*(fhat(gam - 1j*delta)*mp.conj(fhat(gam + 1j*delta))).real
q_zero = q_on + s_off
q_mat = mp.mpf(rung['finder']['min_even'])

out = {
    'rung_lambda': rung['lambda'], 'N': N, 'n_online_zeros_used': len(zs),
    'tmax_online': 155,
    'Q_matrix_side': mp.nstr(q_mat, 15),
    'Q_zero_side': mp.nstr(q_zero, 15),
    'S_on_partial_T100': mp.nstr(q_on_100, 15),
    'S_on_partial_T155': mp.nstr(q_on, 15),
    'S_off_quadruple': mp.nstr(s_off, 15),
    'S_off_from_rung_analysis': rung['analysis']['even_decomp']['S_off(v)'],
    'rel_diff_matrix_vs_zero_side': mp.nstr(
        abs(q_mat - q_zero)/abs(q_mat), 4),
    'note': ('tail-limited: on-line zeros above t=155 omitted; the witness '
             'fhat is a packet at t ~ 85.7 so the omitted tail is small')}

with open(sys.argv[3], 'w') as fh:
    json.dump(out, fh, indent=1)
print('zero-side check:', out['rel_diff_matrix_vs_zero_side'],
      'S_off =', out['S_off_quadruple'], 'S_on(155) =',
      out['S_on_partial_T155'], flush=True)
