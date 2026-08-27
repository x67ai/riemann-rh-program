"""
run_ground_state.py -- THE DH-filter test.

For each (lambda, N) and each of {zeta, dh}: build QW^{lambda,N}, split into parity
sectors, record the bottom of each sector -> test CCM 2511.22755 Section 8 missing
step (a): smallest eigenvalue SIMPLE with EVEN eigenvector; plus positivity, gaps,
and (optionally) the D'' spectrum vs the true zeros of the respective function.

The DH form is the same construction with
  - archimedean a = 3/4, conductor 5 (odd-character-shape gamma factor),
  - no W_{0,2} pole term (DH completed function entire),
  - Lambda(n) -> Lambda_DH(n) (non-multiplicative; supported on ALL n, e.g. n=6).

Usage:  python3 run_ground_state.py <lambda> <dps> <kind> <N1,N2,...> [tag] [--spec N]
   e.g. python3 run_ground_state.py 2 60 dh 8,16,24,32,40,48 lam2 --spec 48
"""
import json
import sys
import time
import mpmath as mp

lam_s, dps, kind, Ns = sys.argv[1], int(sys.argv[2]), sys.argv[3], \
    [int(x) for x in sys.argv[4].split(',')]
tag = sys.argv[5] if len(sys.argv) > 5 and not sys.argv[5].startswith('--') else kind + lam_s
specN = None
if '--spec' in sys.argv:
    specN = int(sys.argv[sys.argv.index('--spec') + 1])

mp.mp.dps = dps
import weilform as wf

lam = mp.mpf(lam_s)
L = 2*mp.log(lam)
results = {'lambda': lam_s, 'dps': dps, 'kind': kind, 'runs': []}
fname = f'outputs/ground_{tag}.json'

for N in Ns:
    t0 = time.time()
    T = wf.build_matrix(lam, N, kind)
    Te, To = wf.parity_blocks(T, N)
    ee, Ve, oe = wf.eig_sym(Te)
    eo, Vo, oo = wf.eig_sym(To)
    tmin = min(ee[0], eo[0])
    # gap data for the even-simple hypothesis
    even_gap = ee[1] - ee[0]
    cross_gap = eo[0] - ee[0]        # >0 iff ground state even
    rec = {
        'N': N, 'freq_reach': mp.nstr(2*mp.pi*N/L, 8),
        'min_even': mp.nstr(ee[0], 15), 'min_odd': mp.nstr(eo[0], 15),
        'even_low10': [mp.nstr(x, 10) for x in ee[:10]],
        'odd_low10': [mp.nstr(x, 10) for x in eo[:10]],
        'positive': bool(tmin > 0),
        'ground_parity': 'even' if ee[0] < eo[0] else 'odd',
        'even_gap_ratio': mp.nstr(ee[1]/ee[0], 8) if ee[0] != 0 else 'inf',
        'cross_gap_ratio': mp.nstr(eo[0]/ee[0], 8) if ee[0] != 0 else 'inf',
        'even_simple': bool(ee[0] < eo[0] and even_gap > 0),
        'time_s': round(time.time() - t0, 1),
    }

    if specN == N:
        # D'' spectrum from ground eigenvector (Thm 5.10); index units -> *2pi/L
        gcol = oe[0]
        xi_e = [Ve[i, gcol] for i in range(N + 1)]
        xi = [mp.mpf(0)]*(2*N + 1)
        xi[N] = xi_e[0]
        for n in range(1, N + 1):
            xi[N + n] = xi_e[n]/mp.sqrt(2)
            xi[N - n] = xi_e[n]/mp.sqrt(2)
        roots = wf.spectrum_from_xi(xi, N, L, N)
        rec['dpp_spectrum_pos'] = [mp.nstr(r, 15) for r in roots if r > 0]
        rec['ground_vector_even'] = [mp.nstr(x, 10) for x in xi_e]
    results['runs'].append(rec)
    print(f"[{kind} lam={lam_s}] N={N}: min_even={rec['min_even']} min_odd={rec['min_odd']} "
          f"parity={rec['ground_parity']} pos={rec['positive']} "
          f"gapE={rec['even_gap_ratio']} ({rec['time_s']}s)", flush=True)
    with open(fname, 'w') as fh:
        json.dump(results, fh, indent=1)

print('done', fname)
