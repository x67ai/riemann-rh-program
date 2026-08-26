"""lambda_ladder_analyze.py -- aggregate the D-R5 ladder lanes, fit the cost law,
extrapolate to the production points, and write lambda-ladder-cost-curve.json.

Cost model (fitted here, all times macOS wall seconds, mpmath pure-python
backend, single core per rung):
  t_build ~= N*(N+10)*K(dps) * u(dps) us,  K = max(30, 0.8*dps),
             u(dps) = A_b + B_b * t_sin(dps)   [t_sin from micro-bench]
  t_eig   ~= 2*(N+1)^3 * e(dps) us,  e(dps) = A_e + B_e * dps  [both parities]
Certified (interval) witness path: iv_build_factor * t_build + t_eig(float
pointer) + O(N^2) iv quadratic form (measured directly).
"""
import glob
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SCRATCH = ("/private/tmp/claude-501/-Users-jaytyagi-Library-Mobile-Documents-"
           "com-apple-CloudDocs-Documents-Work-2026-Math-riemann/"
           "333e0ba0-59a2-4cd9-b46a-bb885e2c2464/scratchpad")

T_SIN = {30: 3.70, 60: 5.11, 100: 7.75, 150: 11.48, 200: 14.88, 300: 26.46}


def t_sin(dps):
    ks = sorted(T_SIN)
    for a, b in zip(ks, ks[1:]):
        if a <= dps <= b:
            f = (dps - a)/(b - a)
            return T_SIN[a] + f*(T_SIN[b] - T_SIN[a])
    return T_SIN[ks[-1]]*dps/ks[-1]


def lsq(xs, ys):
    n = len(xs)
    sx, sy = sum(xs), sum(ys)
    sxx = sum(x*x for x in xs)
    sxy = sum(x*y for x, y in zip(xs, ys))
    b = (n*sxy - sx*sy)/(n*sxx - sx*sx)
    a = (sy - b*sx)/n
    return a, b


def main():
    rungs = []
    for lane in 'ABCDE':
        fn = os.path.join(SCRATCH, f'ladder{lane}.json')
        for r in json.load(open(fn)):
            if not r.get('skipped_over_cap'):
                r['lane'] = lane
                rungs.append(r)
    micro = json.load(open(os.path.join(SCRATCH, 'micro.json')))
    ivs = json.load(open(os.path.join(SCRATCH, 'iv_sample.json')))

    # ---- fit build per-unit cost u(dps)
    upts = []
    for r in rungs:
        npts = r['npts_quad']
        u = 1e6*r['t_build']/(r['N']*npts)
        upts.append((r['dps'], u, r['lambda'], r['N']))
    by_dps = {}
    for d, u, lam, N in upts:
        by_dps.setdefault(d, []).append(u)
    xs = [t_sin(d) for d in sorted(by_dps)]
    ys = [sum(v)/len(v) for _, v in sorted(by_dps.items())]
    A_b, B_b = lsq(xs, ys)

    # ---- fit eig per-unit cost e(dps)  (even block, dim = N+1)
    epts = []
    for r in rungs:
        dim = r['N'] + 1
        epts.append((r['dps'], 1e6*r['t_eig_even']/dim**3))
    eby = {}
    for d, e in epts:
        eby.setdefault(d, []).append(e)
    A_e, B_e = lsq(sorted(eby), [sum(v)/len(v) for _, v in sorted(eby.items())])

    def predict(N, dps):
        K = max(30, int(0.8*dps))
        u = A_b + B_b*t_sin(dps)
        t_build = N*(N + 10)*K*u*1e-6
        t_eig = 2*(N + 1)**3*(A_e + B_e*dps)*1e-6
        return {'N': N, 'dps': dps, 'K': K,
                't_build_s': round(t_build, 0), 't_eig_both_s': round(t_eig, 0),
                't_total_s': round(t_build + t_eig, 0),
                't_total_min': round((t_build + t_eig)/60, 1),
                't_certified_witness_s': round(
                    ivs['kernel_iv_over_float']*t_build + t_eig
                    + ivs['iv_quadform_N128_s']*(N/128)**2, 0)}

    prod = {f"lam={lam},dps={dps},N={N}": predict(N, dps)
            for lam, dps in ((11, 150), (12, 175), (13, 200))
            for N in (128, 200)}
    # sanity: residuals of the model on the measured rungs
    resid = []
    for r in rungs:
        p = predict(r['N'], r['dps'])
        meas = r['t_build'] + r['t_eig_even'] + r['t_eig_odd']
        resid.append(round(meas/(p['t_total_s'] or 1), 2))

    out = {
        'title': 'D1 D-R5: lambda-ladder cost curve for the DH Weil-form stack',
        'date': '2026-08-26',
        'machine': 'MacBook (Mac16,10, Apple Silicon M-class), 10 cores, 24 GB; '
                   'mpmath 1.3.0 PURE-PYTHON backend (gmpy2 NOT installed, '
                   'python-flint/Arb NOT installed); thermal policy 4-wide max',
        'stack': 'results/ccm-dh-test/weilform.py build_matrix(lam, N, "dh") + '
                 'parity_blocks + mp.eigsy; prime cutoff nmax = floor(lam^2) '
                 '(POLYNOMIAL in lambda -- read from code; the exponential lives '
                 'in dps(mu) on the null branch, not in the prime sum)',
        'rungs': rungs,
        'micro_bench': micro,
        'iv_sample': ivs,
        'cost_model': {
            'build': 't_build[s] = N*(N+10)*K(dps)*u(dps)*1e-6, '
                     'K = max(30, 0.8*dps), u(dps) = A_b + B_b*t_sin(dps) [us]',
            'A_b_us': round(A_b, 2), 'B_b': round(B_b, 2),
            't_sin_us_by_dps': T_SIN,
            'eig': 't_eig_both[s] = 2*(N+1)^3*(A_e + B_e*dps)*1e-6 [us]',
            'A_e_us': round(A_e, 2), 'B_e_us_per_digit': round(B_e, 4),
            'model_over_measured_ratio_range': [min(resid), max(resid)],
            'dominant_cost_driver': 'N^2*K transcendental evals (build) and '
                                    '(N+1)^3 mpf ops (eigsy) -- comparable at '
                                    'production sizes; prime enumeration and '
                                    'coefficient recursion are negligible '
                                    '(<0.1 s at lam=13)',
        },
        'production_extrapolation': prod,
    }
    with open(os.path.join(HERE, 'lambda-ladder-cost-curve.json'), 'w') as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps({'A_b': round(A_b, 2), 'B_b': round(B_b, 2),
                      'A_e': round(A_e, 2), 'B_e': round(B_e, 4),
                      'resid_range': [min(resid), max(resid)]}, indent=1))
    for k, v in prod.items():
        print(k, v)


if __name__ == '__main__':
    main()
