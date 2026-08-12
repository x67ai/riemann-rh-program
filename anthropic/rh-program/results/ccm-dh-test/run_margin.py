"""
run_margin.py -- zeta Weil-form margin ladder: smallest eigenvalue eps(lambda) of
QW^{lambda,N} (N saturated) vs lambda, to fit the decay law and adjudicate
   campaign  e^{-4 pi X}  (X = test-support half-width lambda?  X = mu = lambda^2?)
vs Fuchs     e^{-4 pi lambda^2}  as quoted in CCM 2511.22755.
Usage: python3 run_margin.py [tag] [kind]
"""
import json
import sys
import time
import mpmath as mp

TAG = sys.argv[1] if len(sys.argv) > 1 else 'main'
KIND = sys.argv[2] if len(sys.argv) > 2 else 'zeta'

GRID = [
    # (lambda_str, N, dps)
    ('1.2',  32, 50),
    ('1.35', 32, 50),
    ('1.5',  36, 55),
    ('1.65', 36, 60),
    ('1.8',  40, 65),
    ('2.0',  40, 70),
    ('2.2',  40, 75),
    ('2.5',  44, 80),
    ('2.8',  44, 85),
    ('3.0',  48, 90),
]

results = []
for lam_s, N, dps in GRID:
    mp.mp.dps = dps
    import importlib
    import weilform as wf
    importlib.reload(wf)
    lam = mp.mpf(lam_s)
    t0 = time.time()
    T = wf.build_matrix(lam, N, KIND)
    Te, To = wf.parity_blocks(T, N)
    ee, _, _ = wf.eig_sym(Te)
    eo, _, _ = wf.eig_sym(To)
    rec = {
        'lambda': lam_s, 'mu': mp.nstr(lam**2, 12), 'N': N, 'dps': dps,
        'min_even': mp.nstr(ee[0], 15), 'min_odd': mp.nstr(eo[0], 15),
        'even_low8': [mp.nstr(x, 10) for x in ee[:8]],
        'odd_low8': [mp.nstr(x, 10) for x in eo[:8]],
        'ln_min': mp.nstr(mp.log(min(ee[0], eo[0])), 12) if min(ee[0], eo[0]) > 0 else 'NEG',
        'positive': bool(min(ee[0], eo[0]) > 0),
        'ground_parity': 'even' if ee[0] < eo[0] else 'odd',
        'time_s': round(time.time() - t0, 1),
    }
    results.append(rec)
    print(f"lam={lam_s} mu={rec['mu']} N={N} dps={dps}: min_even={rec['min_even']} "
          f"min_odd={rec['min_odd']} parity={rec['ground_parity']} ({rec['time_s']}s)",
          flush=True)
    with open(f'outputs/margin_{TAG}.json', 'w') as fh:
        json.dump(results, fh, indent=1)

# saturation checks at two lambdas with bigger N
for lam_s, N, dps in [('2.0', 56, 70), ('3.0', 56, 90)]:
    mp.mp.dps = dps
    import importlib
    import weilform as wf
    importlib.reload(wf)
    lam = mp.mpf(lam_s)
    t0 = time.time()
    T = wf.build_matrix(lam, N, KIND)
    Te, To = wf.parity_blocks(T, N)
    ee, _, _ = wf.eig_sym(Te)
    eo, _, _ = wf.eig_sym(To)
    rec = {'lambda': lam_s, 'N': N, 'dps': dps, 'saturation_check': True,
           'min_even': mp.nstr(ee[0], 15), 'min_odd': mp.nstr(eo[0], 15),
           'time_s': round(time.time() - t0, 1)}
    results.append(rec)
    print(f"SATCHK lam={lam_s} N={N}: min_even={rec['min_even']} min_odd={rec['min_odd']}",
          flush=True)
    with open(f'outputs/margin_{TAG}.json', 'w') as fh:
        json.dump(results, fh, indent=1)

print('done')
