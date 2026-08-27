"""m0i_aggregate.py -- assemble results/d1-m0/m0i-crash-certificates.json from
the per-rung outputs of m0i_certify.py (+ m0i_dh_zeros.py, m0i_zeroside.py).

Usage: python3 m0i_aggregate.py RUNG_DIR OUT.json
"""
import glob
import json
import math
import os
import sys

rung_dir, out_path = sys.argv[1], sys.argv[2]

rungs = []
for p in sorted(glob.glob(os.path.join(rung_dir, 'r_*.json'))):
    rungs.append(json.load(open(p)))
rungs.sort(key=lambda r: r['lambda_rational'][0]/r['lambda_rational'][1])

zeros = None
zp = os.path.join(rung_dir, 'dh_zeros.json')
if os.path.exists(zp):
    zeros = json.load(open(zp))
zside = None
zsp = os.path.join(rung_dir, 'zeroside.json')
if os.path.exists(zsp):
    zside = json.load(open(zsp))

certified = []
recon_positive = []
departure = []
kinv_curve = []
for r in rungs:
    lam = r['lambda_rational'][0]/r['lambda_rational'][1]
    cert = r.get('certificate', {})
    row = {'lambda': r['lambda'], 'mu': r['mu'], 'N': r['N']}
    ev = cert.get('even', {})
    od = cert.get('odd', {})
    if ev.get('certified_negative'):
        row['certified_even_rayleigh_hi'] = ev['rayleigh_interval'][1]
        row['certified_even_rayleigh_lo'] = ev['rayleigh_interval'][0]
    if od.get('certified_negative'):
        row['certified_odd_rayleigh_hi'] = od['rayleigh_interval'][1]
    if ev.get('certified_negative') or od.get('certified_negative'):
        certified.append(row)
        minval = float(ev['rayleigh_interval'][1]) if ev.get(
            'certified_negative') else float(od['rayleigh_interval'][1])
        departure.append({
            'lambda': r['lambda'], 'mu': r['mu'],
            'min_certified_upper': minval,
            'ln_abs_min': math.log(abs(minval)),
            'baseline_ln_eps': r['baseline_ln_eps'],
            'status': 'certified-negative'})
    else:
        fe = float(r['finder']['min_even'])
        recon_positive.append({
            'lambda': r['lambda'], 'mu': r['mu'],
            'min_even_float': r['finder']['min_even'],
            'min_odd_float': r['finder']['min_odd'],
            'baseline_ln_eps': r['baseline_ln_eps'],
            'baseline_eps': r['baseline_eps'],
            'ratio_to_baseline': (fe/math.exp(r['baseline_ln_eps'])
                                  if fe > 0 else None),
            'status': 'reconnaissance-positive (NOT certified; positivity '
                      'certification is the hard branch, out of scope per '
                      'D-R5)'})
        departure.append({
            'lambda': r['lambda'], 'mu': r['mu'],
            'min_float': r['finder']['min_even'],
            'baseline_ln_eps': r['baseline_ln_eps'],
            'status': 'recon-positive'})
    an = r.get('analysis', {})
    if 'K_inv' in an and not str(an['K_inv']).startswith('FAILED'):
        kinv_curve.append({'lambda': r['lambda'], 'K_inv': an['K_inv'],
                           'coupling_nu1': an.get('coupling_nu1'),
                           'R_ray_p1': an.get('R_ray_p1')})

cert_lams = [r['lambda_rational'][0]/r['lambda_rational'][1] for r in rungs
             if r.get('certificate', {}).get('even', {}).get(
                 'certified_negative')
             or r.get('certificate', {}).get('odd', {}).get(
                 'certified_negative')]
lam_c_bound = min(cert_lams) if cert_lams else None

# K_inv = 1 crossing by log-linear interpolation on the bracketing pair
crossing = None
pts = [(float(k['lambda']), float(k['K_inv'])) for k in kinv_curve]
pts.sort()
for (l1, k1), (l2, k2) in zip(pts, pts[1:]):
    if k1 < 1 <= k2 and k1 > 0:
        crossing = l1 + (l2 - l1)*(0 - math.log(k1))/(
            math.log(k2) - math.log(k1))
        break

out = {
    'deliverable': 'D1 M0(i): certified DH Weil-form positivity-crash hunt',
    'date': '2026-08-26',
    'machine': 'MacBook Mac16,10 (Apple Silicon), python 3.9.6, mpmath 1.3.0 '
               'pure-Python backend (no gmpy2, no Arb)',
    'stack': 'results/ccm-dh-test/weilform.py (conventions triple-validated '
             'Sessions 4-6); certifier: results/d1-m0/m0i_certify.py',
    'scope_statements': [
        'This certifies: the truncated Davenport-Heilbronn Weil quadratic '
        'form QW^{lambda,N} (autocorrelation/PSD test class on '
        '[1/lambda,lambda], Gram convention v^T tau v; no pole term -- the '
        'completed DH function is entire, per the W3/D-R7 convention '
        'requirements, which the weilform stack satisfies) is NOT positive '
        'semidefinite at every certified support lambda. It is the M0 '
        'end-to-end true-positive validation of the detector on a known '
        'RH-false object and the prototype of witness W3.',
        'This is NOT a statement about the Riemann zeta function, and NOT a '
        'Lambda > 0 result.'],
    'certificate_semantics': (
        'Each witness v is an exact 40-decimal-digit vector (frozen from the '
        'dps-60 float eigensolve). Q_DH(v) and the Rayleigh quotient are '
        're-evaluated from scratch in mpmath interval arithmetic (directed '
        'rounding end-to-end: exact rational lambda, Lambda_DH divisor '
        'recursion with kappa from surd enclosures, prime sums, archimedean '
        'composite Gauss-Legendre quadrature, tail/constant terms, the '
        'quadratic form and the norm). rayleigh_interval = [lo, hi] with '
        'hi < 0 certifies negativity for the stated quadrature rule '
        '(M panels x K GL nodes); quadrature-discretization error is bounded '
        'by the grid-double rider (independent finer rule, certified shift '
        'recorded).'),
    'certified_lambda_c_upper_bound': lam_c_bound,
    'certified_negative_rungs': certified,
    'reconnaissance_positive_rungs': recon_positive,
    'baseline_departure': {
        'baseline': 'archived DH conductor-Fuchs fit ln eps = 3.5069 - '
                    '2.6043 mu + 2.7101 ln mu '
                    '(results/d1-m0/chi3-conductor-point.json, dh row)',
        'points': departure},
    'reconciliation': {
        'kinv_curve': kinv_curve,
        'kinv_crossing_lambda': crossing,
        'dh_online_zeros': zeros,
        'zero_side_check': zside},
    'rungs_full': rungs}

with open(out_path, 'w') as fh:
    json.dump(out, fh, indent=1)
print('aggregated', len(rungs), 'rungs; lambda_c <=', lam_c_bound,
      '; K_inv crossing ~', crossing)
