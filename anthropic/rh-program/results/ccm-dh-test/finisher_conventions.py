"""
finisher_conventions.py -- re-run of the convention-arbitration tests (the Session-4
test_conventions.py log was never archived in outputs/).  Same T1/T2/T3 as
test_conventions.py with T2's zero count reduced 1200 -> 320 (tail ~ t^-5: rel
truncation ~ 1e-10, ample to validate conventions) so the run completes quickly.

T1: archimedean log-side formula vs direct spectral t-integral vs paper (3.15).
T2: c^T T c vs explicit-formula zero side for f = V_{-1} - 2 V_0 + V_1 (zeta, lam=2, N=6).
T3: D'' spectrum from ground vector vs first 8 zeta zeros (lam=3, N=24).

Output: outputs/finisher_conventions.json
"""
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
sys.path.insert(0, HERE)

import mpmath as mp
import weilform as wf
import test_conventions as tc

mp.mp.dps = 30
OUT = {}

dA, dB = tc.t1()
OUT['T1_absdiff_mine_vs_spectral'] = mp.nstr(dA, 3)
OUT['T1_absdiff_paper315_vs_spectral'] = mp.nstr(dB, 3)

# T2 with K=320
lam, N = mp.mpf(2), 6
L = 2*mp.log(lam)
T = wf.build_matrix(lam, N, 'zeta')
c = {j: mp.mpf(0) for j in range(-N, N + 1)}
c[-1], c[0], c[1] = mp.mpf(1), mp.mpf(-2), mp.mpf(1)
Qmat = mp.fsum(c[j]*c[k]*T[j + N, k + N]
               for j in range(-N, N + 1) for k in range(-N, N + 1))
fhat = lambda t: mp.fsum(c[j]*tc.vhat(j, L, t) for j in (-1, 0, 1))
K = 320
t0 = time.time()
zs = [mp.zetazero(k).imag for k in range(1, K + 1)]
Qzero = mp.fsum(2*abs(fhat(g))**2 for g in zs)
OUT['T2_matrix_side'] = mp.nstr(Qmat, 20)
OUT['T2_zero_side_K320'] = mp.nstr(Qzero, 20)
OUT['T2_rel_diff'] = mp.nstr(abs(Qmat - Qzero)/abs(Qmat), 3)
OUT['T2_time_s'] = round(time.time() - t0)
print('T2 rel diff', OUT['T2_rel_diff'], flush=True)

pos, zz = tc.t3()
OUT['T3_dpp_vs_zeros'] = [{'dpp': mp.nstr(r, 12), 'zero': mp.nstr(g, 12),
                           'err': mp.nstr(r - g, 3)} for r, g in zip(pos, zz)]

with open('outputs/finisher_conventions.json', 'w') as fh:
    json.dump(OUT, fh, indent=1)
print('done outputs/finisher_conventions.json')
