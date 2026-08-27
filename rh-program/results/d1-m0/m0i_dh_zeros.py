"""m0i_dh_zeros.py -- DH on-line zeros to t = 155 (sign scan of the real
completed Xi_DH on the critical line, machinery of results/ccm-dh-test/dh.py),
for the M0(i) reconciliation: the mean on-line zero gap near t = 85.7 feeds the
CCM verdict's spectral-visibility model (resolution pi/log(lambda) < mean gap),
and the zero list feeds the zero-side consistency check (m0i_zeroside.py).

Usage: python3 m0i_dh_zeros.py OUT.json
"""
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', 'ccm-dh-test')))

import mpmath as mp

import dh

mp.mp.dps = 20
GAMMA = mp.mpf('85.699348485377592')

t0 = time.time()
zs = dh.online_zeros(mp.mpf(155), step=mp.mpf('0.11'))
elapsed = round(time.time() - t0, 1)

below = [z for z in zs if z < GAMMA]
above = [z for z in zs if z > GAMMA]
win = [z for z in zs if 70 <= z <= 100]
gaps = [win[i + 1] - win[i] for i in range(len(win) - 1)]
mean_gap = mp.fsum(gaps)/len(gaps)

out = {
    'date': '2026-08-26', 'dps': 20, 'scan_step': '0.11', 'tmax': 155,
    'n_online_zeros_to_155': len(zs),
    'online_zeros': [mp.nstr(z, 15) for z in zs],
    'scan_time_s': elapsed,
    'offline_gamma': mp.nstr(GAMMA, 18),
    'nearest_online_below': mp.nstr(below[-1], 12),
    'nearest_online_above': mp.nstr(above[0], 12),
    'dist_below': mp.nstr(GAMMA - below[-1], 6),
    'dist_above': mp.nstr(above[0] - GAMMA, 6),
    'mean_gap_70_100': mp.nstr(mean_gap, 6),
    'n_zeros_70_100': len(win),
    'visibility_model': {
        'statement': ('CCM verdict resolution model: off-line zero spectrally '
                      'visible when mode spacing pi/log(lambda) < mean on-line '
                      'gap near t=85.7'),
        'lambda_vis': mp.nstr(mp.e**(mp.pi/mean_gap), 6),
        'mu_vis': mp.nstr(mp.e**(2*mp.pi/mean_gap), 6)}}

with open(sys.argv[1], 'w') as fh:
    json.dump(out, fh, indent=1)
print('zeros:', len(zs), 'mean gap [70,100]:', out['mean_gap_70_100'],
      'neighbors:', out['nearest_online_below'], out['nearest_online_above'],
      'mu_vis:', out['visibility_model']['mu_vis'], flush=True)
