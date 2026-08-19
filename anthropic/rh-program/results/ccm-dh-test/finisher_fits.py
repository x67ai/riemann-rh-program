"""
finisher_fits.py -- collapse-rate analysis across all four coefficient systems.

Reads margin_zeta.json, margin_dh.json, finisher_margin_{chi4,chi5,dhext,zetaext}.json
and fuchs.json.  For each kind: table of (mu, ln eps), local slopes d(ln eps)/d(mu)
at midpoints, and a 2-parameter least-squares fit ln eps = -c*mu + b*ln(mu) + a over
the largest-mu points (>= mu_min_fit).  Reference rates: zeta -4pi = -12.566;
conductor law -4pi/q: chi4 -> -pi = -3.1416, chi5/DH -> -4pi/5 = -2.5133.

Output: outputs/finisher_fits.json
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
sys.path.insert(0, HERE)


def load(fn):
    with open(fn) as fh:
        return json.load(fh)


def series(recs, kind=None):
    pts = []
    for r in recs:
        if 'saturation_check' in r:
            continue
        if kind and r.get('kind', kind) != kind:
            continue
        mu = float(r['mu'])
        eps = float(r['min_even'])
        if eps > 0:
            pts.append((mu, math.log(eps), r['N'], r['dps']))
    # keep the largest-N entry per mu (saturation)
    best = {}
    for mu, ln, N, dps in pts:
        if mu not in best or N > best[mu][1]:
            best[mu] = (ln, N, dps)
    return sorted((mu, v[0], v[1], v[2]) for mu, v in best.items())


def slopes(pts):
    out = []
    for (m1, l1, _, _), (m2, l2, _, _) in zip(pts, pts[1:]):
        out.append({'mu_mid': round((m1 + m2)/2, 3),
                    'slope': round((l2 - l1)/(m2 - m1), 4)})
    return out


def fit_c_b(pts, mu_min):
    """ln eps = a - c*mu + b*ln(mu), least squares over pts with mu >= mu_min."""
    P = [(mu, ln) for mu, ln, _, _ in pts if mu >= mu_min]
    if len(P) < 3:
        return None
    import numpy as np
    A = np.array([[1.0, -mu, math.log(mu)] for mu, _ in P])
    y = np.array([ln for _, ln in P])
    coef, res, _, _ = np.linalg.lstsq(A, y, rcond=None)
    a, c, b = coef
    resid = float(np.sqrt(np.mean((A @ coef - y)**2)))
    return {'a': round(float(a), 4), 'c': round(float(c), 5),
            'b': round(float(b), 4), 'rms_resid': round(resid, 5),
            'npts': len(P), 'mu_min': mu_min}


OUT = {}
zeta_pts = series(load('outputs/margin_zeta.json'))
if os.path.exists('outputs/finisher_margin_zetaext.json'):
    zeta_pts = sorted(set(zeta_pts) | set(series(load('outputs/finisher_margin_zetaext.json'))))
dh_pts = series(load('outputs/margin_dh.json'))
if os.path.exists('outputs/finisher_margin_dhext.json'):
    dh_pts = sorted(set(dh_pts) | set(series(load('outputs/finisher_margin_dhext.json'))))
chi4_pts = series(load('outputs/finisher_margin_chi4.json')) \
    if os.path.exists('outputs/finisher_margin_chi4.json') else []
chi5_pts = series(load('outputs/finisher_margin_chi5.json')) \
    if os.path.exists('outputs/finisher_margin_chi5.json') else []

REF = {'zeta': -4*math.pi, 'dh': -4*math.pi/5, 'chi4': -math.pi,
       'chi5': -4*math.pi/5}
for name, pts in (('zeta', zeta_pts), ('dh', dh_pts), ('chi4', chi4_pts),
                  ('chi5', chi5_pts)):
    if not pts:
        continue
    OUT[name] = {
        'points_mu_lneps_N_dps': [[round(m, 4), round(l, 4), N, d]
                                  for m, l, N, d in pts],
        'local_slopes': slopes(pts),
        'fit_ln_eps = a - c*mu + b*ln(mu)': fit_c_b(pts, 4.0),
        'conductor_law_reference_c': round(-REF[name], 5),
    }

# headline ratios
def last_slope(name):
    s = OUT.get(name, {}).get('local_slopes', [])
    return s[-1]['slope'] if s else None


def fitc(name):
    f = OUT.get(name, {}).get('fit_ln_eps = a - c*mu + b*ln(mu)')
    return f['c'] if f else None


OUT['headline'] = {
    'fit_c': {k: fitc(k) for k in ('zeta', 'dh', 'chi4', 'chi5')},
    'last_local_slope': {k: last_slope(k) for k in ('zeta', 'dh', 'chi4', 'chi5')},
    'reference_minus_4pi_over_q': {'zeta(q=1)': round(4*math.pi, 5),
                                   'chi4(q=4)': round(math.pi, 5),
                                   'chi5(q=5)': round(4*math.pi/5, 5),
                                   'dh(q=5)': round(4*math.pi/5, 5)},
}

# eps at matched mu=9 across kinds (the single-mu contrast table)
def eps_at(pts, mu):
    for m, l, N, d in pts:
        if abs(m - mu) < 1e-9:
            return l
    return None


OUT['ln_eps_at_mu9'] = {k: eps_at(p, 9.0) for k, p in
                        (('zeta', zeta_pts), ('dh', dh_pts),
                         ('chi4', chi4_pts), ('chi5', chi5_pts))}

with open('outputs/finisher_fits.json', 'w') as fh:
    json.dump(OUT, fh, indent=1)
print(json.dumps(OUT['headline'], indent=1))
print(json.dumps(OUT.get('ln_eps_at_mu9', {}), indent=1))
print('done outputs/finisher_fits.json')
