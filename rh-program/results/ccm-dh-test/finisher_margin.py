"""
finisher_margin.py -- Session-5 finisher margin ladders (controls + extensions).

Batches:
  chi4    : RH-true odd character mod 4  (Euler intact, conductor 4, a=3/4 like DH)
  chi5    : RH-true even character mod 5 (Euler intact, SAME conductor 5 as DH, a=1/4)
  dhext   : DH extension to lambda in {3.2, 3.5, 3.8} (+ N-saturation check at 3.5)
  zetaext : zeta extension to lambda = 3.2 (high dps)

At lambda=3.0 for chi4/chi5 the ground eigenvector's D'' spectrum is recorded
(Thm 5.10 root-finding, same code path as run_ground_state.py).

Usage: python3 finisher_margin.py <batch>
Output: outputs/finisher_margin_<batch>.json (incremental writes).
"""
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
sys.path.insert(0, HERE)

import mpmath as mp

BATCHES = {
    'chi4': ('chi4', [('1.5', 36, 55), ('1.8', 40, 65), ('2.0', 40, 70),
                      ('2.2', 40, 75), ('2.5', 44, 80), ('2.8', 44, 85),
                      ('3.0', 48, 90), ('3.2', 52, 100)]),
    'chi5': ('chi5', [('1.5', 36, 55), ('1.8', 40, 65), ('2.0', 40, 70),
                      ('2.2', 40, 75), ('2.5', 44, 80), ('2.8', 44, 85),
                      ('3.0', 48, 90), ('3.2', 52, 100)]),
    'dhext': ('dh', [('3.2', 52, 100), ('3.5', 56, 110), ('3.5', 64, 110),
                     ('3.8', 64, 120)]),
    'zetaext': ('zeta', [('3.2', 52, 150)]),
}

batch = sys.argv[1]
kind, grid = BATCHES[batch]
SPEC_AT = {('chi4', '3.0'), ('chi5', '3.0')}

results = []
fname = f'outputs/finisher_margin_{batch}.json'
for lam_s, N, dps in grid:
    mp.mp.dps = dps
    import importlib
    import weilform as wf
    import finisher_weilext as fx
    importlib.reload(wf)
    importlib.reload(fx)
    lam = mp.mpf(lam_s)
    L = 2*mp.log(lam)
    t0 = time.time()
    T = fx.build_matrix_ext(lam, N, kind)
    Te, To = wf.parity_blocks(T, N)
    ee, Ve, oe = wf.eig_sym(Te)
    eo, _, _ = wf.eig_sym(To)
    even_gap = ee[1] - ee[0]
    rec = {
        'kind': kind, 'lambda': lam_s, 'mu': mp.nstr(lam**2, 12), 'N': N,
        'dps': dps, 'min_even': mp.nstr(ee[0], 15), 'min_odd': mp.nstr(eo[0], 15),
        'even_low6': [mp.nstr(x, 10) for x in ee[:6]],
        'odd_low6': [mp.nstr(x, 10) for x in eo[:6]],
        'ln_min_even': mp.nstr(mp.log(ee[0]), 12) if ee[0] > 0 else 'NEG',
        'positive': bool(min(ee[0], eo[0]) > 0),
        'ground_parity': 'even' if ee[0] < eo[0] else 'odd',
        'even_simple': bool(ee[0] < eo[0] and even_gap > 0),
        'time_s': round(time.time() - t0, 1),
    }
    if (kind, lam_s) in SPEC_AT:
        gcol = oe[0]
        xi_e = [Ve[i, gcol] for i in range(N + 1)]
        xi = [mp.mpf(0)]*(2*N + 1)
        xi[N] = xi_e[0]
        for n in range(1, N + 1):
            xi[N + n] = xi_e[n]/mp.sqrt(2)
            xi[N - n] = xi_e[n]/mp.sqrt(2)
        roots = wf.spectrum_from_xi(xi, N, L, N)
        rec['dpp_spectrum_pos'] = [mp.nstr(r, 15) for r in roots if r > 0]
    results.append(rec)
    print(f"[{batch}] {kind} lam={lam_s} mu={rec['mu']} N={N} dps={dps}: "
          f"min_even={rec['min_even']} min_odd={rec['min_odd']} "
          f"parity={rec['ground_parity']} ({rec['time_s']}s)", flush=True)
    with open(fname, 'w') as fh:
        json.dump(results, fh, indent=1)

print('done', fname)
