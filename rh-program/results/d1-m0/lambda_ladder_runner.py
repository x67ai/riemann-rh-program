"""lambda_ladder_runner.py -- D1 repair D-R5: empirical lambda-ladder cost curve
for the DH Weil-form stack (results/ccm-dh-test/weilform.py), the mandated
precursor to the M0(i) crash hunt at lambda in [11,13].

Phases timed per rung (lam, N, dps), kind='dh':
  t_coeff   : lambda_dh(nmax) coefficient recursion, nmax = floor(lam^2)
  t_build   : weilform.build_matrix(lam, N, 'dh')  [quadrature npts=(N+10)*K,
              K = max(30, 0.8*dps); prime sums of len(lamdict) terms]
  t_parity  : parity_blocks
  t_eig_e/o : mp.eigsy on the (N+1) even and N odd blocks
  t_witness : Gaussian index-packet Rayleigh quotient c^T Te c / |c|^2 with
              c_n = exp(-(n-n0)^2/(2 w^2)), n0 = t0*L/(2 pi), t0 = 85.699348...
              (the M0(i) witness-mode cost: O(N^2) once T exists) -- only when
              N >= n0 + 12 so the packet fits in the basis.
Also records min_even/min_odd (INDICATIVE ONLY at dps=30 -- the conductor-Fuchs
null scale e^{-4 pi mu/5} is ~1e-131 at mu=121, far below working precision;
positive minima at that scale are numerically indistinguishable from 0, and only
a MACROSCOPIC negative minimum would be meaningful reconnaissance), and peak RSS.

Usage: python3 lambda_ladder_runner.py OUT.json CAP_SECONDS lam:N:dps [...]
Rungs run in listed order (ascending cost); if a rung exceeds CAP_SECONDS the
remaining rungs in this process are skipped and marked so.
"""
import importlib
import json
import os
import resource
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
STACK = os.path.abspath(os.path.join(HERE, '..', 'ccm-dh-test'))
sys.path.insert(0, STACK)

import mpmath as mp

T0_DH = '85.699348485377592'


def run_rung(lam_s, N, dps):
    mp.mp.dps = dps
    import weilform as wf
    importlib.reload(wf)          # clears _GL_CACHE so RSS stays per-rung honest
    lam = mp.mpf(lam_s)
    L = 2*mp.log(lam)
    nmax = int(mp.floor(lam**2 + mp.mpf('1e-9')))
    K = max(30, int(mp.mp.dps*0.8))
    M = N + 10

    t = time.perf_counter()
    lamdict = wf.lambda_dh(nmax)
    t_coeff = time.perf_counter() - t

    t = time.perf_counter()
    T = wf.build_matrix(lam, N, 'dh')
    t_build = time.perf_counter() - t

    t = time.perf_counter()
    Te, To = wf.parity_blocks(T, N)
    t_parity = time.perf_counter() - t

    t = time.perf_counter()
    ee, Ve, order = wf.eig_sym(Te)
    t_eig_e = time.perf_counter() - t
    t = time.perf_counter()
    eo, _, _ = wf.eig_sym(To)
    t_eig_o = time.perf_counter() - t

    rec = {
        'lambda': lam_s, 'mu': float(mp.nstr(lam**2, 10)), 'N': N, 'dps': dps,
        'K': K, 'M_panels': M, 'npts_quad': M*K, 'nmax': nmax,
        'n_coeff_terms': len(lamdict),
        't_coeff': round(t_coeff, 3), 't_build': round(t_build, 2),
        't_parity': round(t_parity, 2),
        't_eig_even': round(t_eig_e, 2), 't_eig_odd': round(t_eig_o, 2),
        'min_even': mp.nstr(ee[0], 12), 'min_odd': mp.nstr(eo[0], 12),
        'even_low4': [mp.nstr(x, 8) for x in ee[:4]],
    }

    # witness mode: Gaussian index packet at the DH off-line height
    tz = mp.mpf(T0_DH)
    n0 = tz*L/(2*mp.pi)
    rec['packet_center_index_n0'] = float(mp.nstr(n0, 8))
    if N >= n0 + 12:
        w = mp.mpf(8)
        t = time.perf_counter()
        c = [mp.e**(-(mp.mpf(n) - n0)**2/(2*w*w)) for n in range(0, N + 1)]
        num = mp.fsum(c[i]*Te[i, j]*c[j]
                      for i in range(N + 1) for j in range(N + 1))
        den = mp.fsum(ci*ci for ci in c)
        rq = num/den
        rec['t_witness'] = round(time.perf_counter() - t, 2)
        rec['witness_rayleigh'] = mp.nstr(rq, 12)
    rec['t_total'] = round(t_coeff + t_build + t_parity + t_eig_e + t_eig_o
                           + rec.get('t_witness', 0), 2)
    rec['peak_rss_mb'] = round(
        resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576, 1)
    return rec


def main():
    out_path, cap_s = sys.argv[1], float(sys.argv[2])
    rungs = [a.split(':') for a in sys.argv[3:]]
    results = []
    skipped = False
    for lam_s, N_s, dps_s in rungs:
        if skipped:
            results.append({'lambda': lam_s, 'N': int(N_s), 'dps': int(dps_s),
                            'skipped_over_cap': True})
            continue
        t = time.perf_counter()
        rec = run_rung(lam_s, int(N_s), int(dps_s))
        rec['t_wall'] = round(time.perf_counter() - t, 2)
        results.append(rec)
        print(f"lam={lam_s} N={N_s} dps={dps_s}: build={rec['t_build']}s "
              f"eig={rec['t_eig_even']}+{rec['t_eig_odd']}s "
              f"total={rec['t_wall']}s min_even={rec['min_even']}", flush=True)
        with open(out_path, 'w') as fh:
            json.dump(results, fh, indent=1)
        if rec['t_wall'] > cap_s:
            skipped = True
    with open(out_path, 'w') as fh:
        json.dump(results, fh, indent=1)
    print('done', out_path)


if __name__ == '__main__':
    main()
