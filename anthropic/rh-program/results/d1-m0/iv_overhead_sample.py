"""iv_sample.py -- direct iv-vs-float overhead on the dominant build kernel at a
sample rung (lam=13, N=128, dps=60 scale): the phi-mode quadrature sum
sum_i W[i] * g_arch[i] * sin(w y_i) over npts nodes, plus an O(N^2) certified
quadratic-form pass.  Also: ground-eigenvector localization at lam=8, N=64,
dps=30 (does the crashed mode sit at packet index n0 ~ 56.7 <-> t ~ 85.7?).
"""
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
STACK = "/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/anthropic/rh-program/results/ccm-dh-test"
sys.path.insert(0, STACK)

import mpmath as mp
from mpmath import iv

out = {}

# ---- kernel overhead at rung scale (dps=60, npts as lam=13/N=128: 6624)
dps = 60
mp.mp.dps = dps
iv.dps = dps
import weilform as wf
lam = mp.mpf(13)
L = 2*mp.log(lam)
N = 128
K = max(30, int(0.8*dps))
Y, W = wf.composite_grid(L, N + 10, K)
npts = len(Y)
a = mp.mpf(3)/4
g = []
for y in Y:
    den = -mp.expm1(-2*y)
    g.append(-2*mp.e**(-2*a*y)/den)
w_ = 2*mp.pi*70/L   # packet-center mode

t = time.perf_counter()
sfl = mp.fsum(W[i]*g[i]*mp.sin(w_*Y[i]) for i in range(npts))
t_float = time.perf_counter() - t

Yi = [iv.mpf(y) for y in Y]
Wi = [iv.mpf(x) for x in W]
gi = []
t = time.perf_counter()
for y in Yi:
    den = -(iv.exp(-2*y) - 1)
    gi.append(-2*iv.exp(-2*a*y)/den)
t_iv_prep = time.perf_counter() - t
wiv = iv.mpf(w_)
t = time.perf_counter()
acc = iv.mpf(0)
for i in range(npts):
    acc += Wi[i]*gi[i]*iv.sin(wiv*Yi[i])
t_iv = time.perf_counter() - t
out['kernel_dps60_npts'] = npts
out['kernel_float_s'] = round(t_float, 3)
out['kernel_iv_s'] = round(t_iv, 3)
out['kernel_iv_over_float'] = round(t_iv/t_float, 2)
out['iv_enclosure_width'] = mp.nstr(mp.mpf(acc.delta.a), 3)
out['iv_contains_float'] = bool(sfl in acc)
print('kernel iv/float =', out['kernel_iv_over_float'],
      'width', out['iv_enclosure_width'], flush=True)

# ---- O(N^2) certified quadratic form timing (iv dot with a matrix row proxy)
xs = [iv.mpf(mp.mpf(i % 7 + 1)/7) for i in range(N + 1)]
t = time.perf_counter()
tot = iv.mpf(0)
for i in range(N + 1):
    row = iv.mpf(0)
    for j in range(N + 1):
        row += xs[j]*xs[(i*j) % (N + 1)]
    tot += xs[i]*row
out['iv_quadform_N128_s'] = round(time.perf_counter() - t, 3)
print('iv quadform (N+1)^2 =', out['iv_quadform_N128_s'], 's', flush=True)

# ---- localization of the crashed ground state at lam=8, N=64, dps=30
mp.mp.dps = 30
import importlib
importlib.reload(wf)
lam8 = mp.mpf(8)
L8 = 2*mp.log(lam8)
N8 = 64
T = wf.build_matrix(lam8, N8, 'dh')
Te, To = wf.parity_blocks(T, N8)
ee, Ve, order = wf.eig_sym(Te)
gcol = order[0]
xi = [Ve[i, gcol] for i in range(N8 + 1)]
mags = [abs(x) for x in xi]
imax = max(range(N8 + 1), key=lambda i: mags[i])
n0 = mp.mpf('85.699348485377592')*L8/(2*mp.pi)
out['lam8_min_even'] = mp.nstr(ee[0], 12)
out['lam8_packet_center_n0'] = float(mp.nstr(n0, 6))
out['lam8_eigvec_argmax_index'] = imax
out['lam8_eigvec_top8'] = sorted(
    [[i, float(mp.nstr(mags[i], 4))] for i in range(N8 + 1)],
    key=lambda p: -p[1])[:8]
# weight of the eigenvector in the index window n0 +/- 12
wnd = mp.fsum(mags[i]**2 for i in range(N8 + 1) if abs(i - n0) <= 12)
tot2 = mp.fsum(m**2 for m in mags)
out['lam8_mass_within_12_of_n0'] = float(mp.nstr(wnd/tot2, 4))
print('lam8 ground:', out['lam8_min_even'], 'argmax idx', imax, 'n0', out['lam8_packet_center_n0'],
      'mass near n0:', out['lam8_mass_within_12_of_n0'], flush=True)

with open(os.path.join(HERE, 'iv_sample.json'), 'w') as fh:
    json.dump(out, fh, indent=1)
print('done')
