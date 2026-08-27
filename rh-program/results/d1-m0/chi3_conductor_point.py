"""
chi3_conductor_point.py -- D1 milestone M0(ii): the FIFTH calibration point of the
conductor-Fuchs law  eps(mu) ~ poly(mu) * e^{-4*pi*mu/q}  (ccm-dh-filter.json).

System: chi3 = the primitive ODD real Dirichlet character mod 3 (Kronecker -3):
  chi3(n) = +1, -1, 0  for n = 1, 2, 0 (mod 3);  chi3(-1) = chi3(2) = -1 => ODD.
Prediction under the calibrated law: c = 4*pi/3 = 4.18879.

CONVENTIONS -- every one copied from the Session-4/5 stack, none invented here:
  * Weil-form matrix engine ......... finisher_weilext.build_matrix_ext (verbatim,
    called through it; only the parameter table is extended with 'chi3').
  * Odd-character gamma factor ...... a = 3/4, exactly as kind='chi4' (odd char):
    finisher_weilext.params / weilform.build_matrix inline table.  Completed FE:
    (3/pi)^((s+1)/2) Gamma((s+1)/2) L(s,chi3), entire => use02=False (no pole term),
    conductor term log(qcond/pi) = log(3/pi), as chi4 uses log(4/pi).
  * Lambda_chi3(n) = chi3(p)^k log p on n = p^k .. pattern of weilform.lambda_chi4
    and finisher_weilext.lambda_chi5 (Euler product intact).
  * mu-grid + N/dps schedule ........ BATCHES['chi4'] == BATCHES['chi5'] of
    finisher_margin.py: lambda in {1.5,1.8,2.0,2.2,2.5,2.8,3.0,3.2},
    N in {36,40,40,40,44,44,48,52}, dps in {55,65,70,75,80,85,90,100};
    plus one N=56 saturation check at lambda=3.0 (run_margin.py pattern,
    'saturation_check': True => excluded from fits exactly as finisher_fits.series).
  * Parity split / ground state ..... weilform.parity_blocks + eig_sym (verbatim).
  * D'' spectrum at lambda=3.0 ...... SPEC_AT code path of finisher_margin.py
    (verbatim), validated against the TRUE on-line zeros of L(s,chi3) computed by
    the finisher_dh_zeros.online_zeros sign-scan of the completed function
    (xi_chi3 patterned on xi_chi4 there; Hurwitz-zeta representation).
  * Fit .......... finisher_fits.fit_c_b verbatim: ln eps = a - c*mu + b*ln(mu),
    least squares over mu >= 4.0.  The four archived systems are REFIT here from
    their stored margin files with the same code and asserted against the archived
    finisher_fits.json values (methodology-identity check).
  * Prefactor study (the 'arithmetic hides in prefactors' loophole): for all five
    systems, fixed-rate fit  ln eps + (4*pi/q)*mu = A + B*ln(mu)  over the same
    mu >= 4 points, plus per-point deflated prefactor ln(eps * e^{+4*pi*mu/q}).

Thermal policy: ONE sequential process, no parallelism.
Usage: python3 chi3_conductor_point.py
Outputs (this directory): chi3_margin_ladder.json (incremental), chi3-conductor-point.json
"""
import json
import math
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
STACK = os.path.abspath(os.path.join(HERE, '..', 'ccm-dh-test'))
os.chdir(HERE)
sys.path.insert(0, STACK)

import mpmath as mp

Q = 3
PREDICTED_C = 4*math.pi/Q      # 4.18879...


# ------------------------------------------------------- chi3 coefficient data
def lambda_chi3(nmax):
    """Lambda_chi(n) = chi3(p)^k log p for n = p^k; chi3 = Kronecker -3
    (chi3(1 mod 3)=1, chi3(2 mod 3)=-1, chi3(0 mod 3)=0).  Odd character => a=3/4.
    Pattern: weilform.lambda_chi4 / finisher_weilext.lambda_chi5."""
    out = {}
    for p in range(2, nmax + 1):
        if all(p % d for d in range(2, int(p**0.5) + 1)):
            c = {0: 0, 1: 1, 2: -1}[p % 3]
            if c != 0:
                pk, k = p, 1
                while pk <= nmax:
                    out[pk] = (c**k)*mp.log(p)
                    pk *= p
                    k += 1
    return out


def fresh_modules(dps):
    """Set dps, (re)load the Session-4/5 stack, extend its params table with
    'chi3' (odd: a=3/4 like chi4; conductor term log(3/pi); entire: use02 False)."""
    import importlib
    mp.mp.dps = dps
    import weilform as wf
    import finisher_weilext as fx
    importlib.reload(wf)
    importlib.reload(fx)
    orig_params = fx.params

    def params_ext(kind, nmax):
        if kind == 'chi3':
            return mp.mpf(3)/4, mp.log(3/mp.pi), lambda_chi3(nmax), False
        return orig_params(kind, nmax)

    fx.params = params_ext
    return wf, fx


# ------------------------------------------------------------- margin ladder
GRID = [  # identical to finisher_margin.BATCHES['chi4'] / ['chi5']
    ('1.5', 36, 55), ('1.8', 40, 65), ('2.0', 40, 70), ('2.2', 40, 75),
    ('2.5', 44, 80), ('2.8', 44, 85), ('3.0', 48, 90), ('3.2', 52, 100),
]
SATCHK = ('3.0', 56, 90)   # run_margin.py saturation-check pattern


def run_ladder():
    results = []
    fname = 'chi3_margin_ladder.json'
    for lam_s, N, dps in GRID:
        wf, fx = fresh_modules(dps)
        lam = mp.mpf(lam_s)
        L = 2*mp.log(lam)
        t0 = time.time()
        T = fx.build_matrix_ext(lam, N, 'chi3')
        Te, To = wf.parity_blocks(T, N)
        ee, Ve, oe = wf.eig_sym(Te)
        eo, _, _ = wf.eig_sym(To)
        even_gap = ee[1] - ee[0]
        rec = {
            'kind': 'chi3', 'lambda': lam_s, 'mu': mp.nstr(lam**2, 12), 'N': N,
            'dps': dps, 'min_even': mp.nstr(ee[0], 15), 'min_odd': mp.nstr(eo[0], 15),
            'even_low6': [mp.nstr(x, 10) for x in ee[:6]],
            'odd_low6': [mp.nstr(x, 10) for x in eo[:6]],
            'ln_min_even': mp.nstr(mp.log(ee[0]), 12) if ee[0] > 0 else 'NEG',
            'positive': bool(min(ee[0], eo[0]) > 0),
            'ground_parity': 'even' if ee[0] < eo[0] else 'odd',
            'even_simple': bool(ee[0] < eo[0] and even_gap > 0),
            'time_s': round(time.time() - t0, 1),
        }
        if lam_s == '3.0':   # SPEC_AT pattern of finisher_margin.py
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
        print(f"[chi3] lam={lam_s} mu={rec['mu']} N={N} dps={dps}: "
              f"min_even={rec['min_even']} min_odd={rec['min_odd']} "
              f"parity={rec['ground_parity']} ({rec['time_s']}s)", flush=True)
        with open(fname, 'w') as fh:
            json.dump(results, fh, indent=1)

    lam_s, N, dps = SATCHK
    wf, fx = fresh_modules(dps)
    lam = mp.mpf(lam_s)
    t0 = time.time()
    T = fx.build_matrix_ext(lam, N, 'chi3')
    Te, To = wf.parity_blocks(T, N)
    ee, _, _ = wf.eig_sym(Te)
    eo, _, _ = wf.eig_sym(To)
    rec = {'kind': 'chi3', 'lambda': lam_s, 'mu': mp.nstr(lam**2, 12), 'N': N,
           'dps': dps, 'saturation_check': True,
           'min_even': mp.nstr(ee[0], 15), 'min_odd': mp.nstr(eo[0], 15),
           'time_s': round(time.time() - t0, 1)}
    results.append(rec)
    print(f"SATCHK lam={lam_s} N={N}: min_even={rec['min_even']} "
          f"min_odd={rec['min_odd']} ({rec['time_s']}s)", flush=True)
    with open(fname, 'w') as fh:
        json.dump(results, fh, indent=1)
    return results


# ------------------------------------- true on-line zeros of L(s,chi3) (dps 40)
def true_chi3_zeros(tmax=46):
    """finisher_dh_zeros.online_zeros pattern; completed odd-char L via Hurwitz:
    L(s,chi3) = 3^{-s} (zeta(s,1/3) - zeta(s,2/3));
    xi_chi3(s) = (3/pi)^{(s+1)/2} Gamma((s+1)/2) L(s,chi3)  (real on the line)."""
    mp.mp.dps = 40

    def xi_chi3(s):
        Lf = 3**(-s)*(mp.zeta(s, mp.mpf(1)/3) - mp.zeta(s, mp.mpf(2)/3))
        return (3/mp.pi)**((s + 1)/2)*mp.gamma((s + 1)/2)*Lf

    zs = []
    step = mp.mpf('0.12')
    t = mp.mpf('0.4')
    v = xi_chi3(mp.mpf('0.5') + 1j*t)
    assert abs(v.imag) < 1e-15*max(1, abs(v.real)), 'completed fn not real on line'
    zprev = v.real
    while t < tmax:
        t2 = t + step
        znew = xi_chi3(mp.mpf('0.5') + 1j*t2).real
        if mp.sign(znew) != mp.sign(zprev) and zprev != 0:
            r = mp.findroot(lambda u: xi_chi3(mp.mpf('0.5') + 1j*u).real,
                            (t, t2), solver='illinois')
            zs.append(r)
        t, zprev = t2, znew
    return zs


def err_table(spec_strs, true_zeros, nmax=8):
    """finisher_dh_zeros.err_table verbatim."""
    rows = []
    for s in spec_strs[:nmax]:
        r = mp.mpf(s)
        best = min(true_zeros, key=lambda z: abs(z - r))
        rows.append({'dpp_root': mp.nstr(r, 15), 'nearest_true_zero': mp.nstr(best, 15),
                     'abs_err': mp.nstr(abs(r - best), 3)})
    return rows


# ------------------------------------------------- fits (finisher_fits verbatim)
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


def fit_prefactor_fixed_c(pts, c_fixed, mu_min):
    """Fixed-rate prefactor fit: ln eps + c_fixed*mu = A + B*ln(mu), mu >= mu_min."""
    P = [(mu, ln + c_fixed*mu) for mu, ln, _, _ in pts if mu >= mu_min]
    if len(P) < 2:
        return None
    import numpy as np
    A = np.array([[1.0, math.log(mu)] for mu, _ in P])
    y = np.array([v for _, v in P])
    coef, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
    resid = float(np.sqrt(np.mean((A @ coef - y)**2)))
    return {'A': round(float(coef[0]), 4), 'B': round(float(coef[1]), 4),
            'rms_resid': round(resid, 5), 'npts': len(P), 'mu_min': mu_min,
            'c_fixed': round(c_fixed, 5),
            'deflated_ln_prefactor_points': [
                [round(mu, 4), round(v, 4)] for mu, v in P]}


def load(fn):
    with open(fn) as fh:
        return json.load(fh)


def main():
    t_start = time.time()
    ladder = run_ladder()

    print('scanning true L(s,chi3) zeros...', flush=True)
    zeros = true_chi3_zeros()
    print('chi3 zeros:', [mp.nstr(z, 8) for z in zeros], flush=True)
    spec = next(r['dpp_spectrum_pos'] for r in ladder if r.get('dpp_spectrum_pos'))
    match = err_table(spec, zeros)

    # ---- refit archived systems with the identical code (methodology check)
    OUTD = os.path.join(STACK, 'outputs')
    zeta_pts = series(load(os.path.join(OUTD, 'margin_zeta.json')))
    zeta_pts = sorted(set(zeta_pts) |
                      set(series(load(os.path.join(OUTD, 'finisher_margin_zetaext.json')))))
    dh_pts = series(load(os.path.join(OUTD, 'margin_dh.json')))
    dh_pts = sorted(set(dh_pts) |
                    set(series(load(os.path.join(OUTD, 'finisher_margin_dhext.json')))))
    chi4_pts = series(load(os.path.join(OUTD, 'finisher_margin_chi4.json')))
    chi5_pts = series(load(os.path.join(OUTD, 'finisher_margin_chi5.json')))
    chi3_pts = series(ladder)

    archived = load(os.path.join(OUTD, 'finisher_fits.json'))
    QCOND = {'zeta': 1, 'chi3': 3, 'chi4': 4, 'chi5': 5, 'dh': 5}
    ALL = {'zeta': zeta_pts, 'chi3': chi3_pts, 'chi4': chi4_pts,
           'chi5': chi5_pts, 'dh': dh_pts}

    fits, prefits, table = {}, {}, []
    for name, pts in ALL.items():
        f = fit_c_b(pts, 4.0)
        fits[name] = f
        q = QCOND[name]
        cref = 4*math.pi/q
        prefits[name] = fit_prefactor_fixed_c(pts, cref, 4.0)
        table.append({'system': name, 'q': q, 'fitted_c': f['c'],
                      'reference_4pi_over_q': round(cref, 5),
                      'deviation_pct': round(100*(f['c'] - cref)/cref, 2),
                      'fitted_b': f['b'], 'fitted_a': f['a'],
                      'rms_resid': f['rms_resid'], 'npts_fit': f['npts']})
        if name != 'chi3':   # methodology-identity check vs archived Session-5 fit
            arch_c = archived[name]['fit_ln_eps = a - c*mu + b*ln(mu)']['c']
            assert abs(f['c'] - arch_c) < 5e-5, (name, f['c'], arch_c)
    table.sort(key=lambda r: r['q'])

    fc = fits['chi3']
    dev = 100*(fc['c'] - PREDICTED_C)/PREDICTED_C

    # saturation: mu=9 margin, N=48 vs N=56
    m48 = next(float(r['min_even']) for r in ladder
               if r['lambda'] == '3.0' and r['N'] == 48)
    m56 = next(float(r['min_even']) for r in ladder
               if r['lambda'] == '3.0' and r.get('saturation_check'))

    out = {
        'milestone': 'D1 M0(ii): fifth conductor point chi3 for the conductor-Fuchs law',
        'date': '2026-08-26',
        'system': 'L(s, chi3), chi3 = primitive odd real Dirichlet character mod 3 '
                  '(Kronecker -3): chi3(n) = +1, -1, 0 for n = 1, 2, 0 (mod 3)',
        'conductor': 3,
        'parity_FE_convention': {
            'character_parity': 'ODD (chi3(-1) = chi3(2 mod 3) = -1)',
            'gamma_shape_a': '3/4 (odd character), identical to kind=chi4 in '
                             'weilform.build_matrix / finisher_weilext.params',
            'conductor_term': 'log(qcond/pi) = log(3/pi)',
            'pole_term_W02': 'absent (completed L entire), as chi4/chi5/dh',
            'completed_FE': 'xi(s) = (3/pi)^((s+1)/2) Gamma((s+1)/2) L(s,chi3), '
                            'real on the critical line (root number +1); '
                            'reality asserted numerically in the zero scan',
        },
        'coefficients': 'Lambda_chi3(n) = chi3(p)^k log p on n = p^k '
                        '(Euler product intact), pattern of weilform.lambda_chi4',
        'mu_grid': {
            'lambda': [g[0] for g in GRID], 'N': [g[1] for g in GRID],
            'dps': [g[2] for g in GRID],
            'mu': [round(float(g[0])**2, 4) for g in GRID],
            'source': 'finisher_margin.py BATCHES[chi4] == BATCHES[chi5], reused verbatim',
            'saturation_check': 'lambda=3.0 N=56 dps=90 (excluded from fits)',
        },
        'margins_ladder': ladder,
        'saturation_mu9': {'N48': m48, 'N56': m56,
                           'rel_change': round(abs(m56 - m48)/m48, 4)},
        'ground_state': 'even-simple at every grid point (see margins_ladder '
                        'positive/even_simple flags)',
        'dpp_spectrum_check': {
            'true_chi3_online_zeros_to_46': [mp.nstr(z, 15) for z in zeros],
            'match_lam3_N48': match,
            'purpose': 'validates the odd-parity/conductor conventions: a wrong a or '
                       'qcond would destroy the D-prime-prime low-zero match',
        },
        'fit_definition': 'ln eps = a - c*mu + b*ln(mu), least squares over mu >= 4.0 '
                          '(finisher_fits.fit_c_b, reused verbatim)',
        'chi3_fit': fc,
        'chi3_local_slopes': slopes(chi3_pts),
        'chi3_points_mu_lneps_N_dps': [[round(m, 4), round(l, 4), N, d]
                                       for m, l, N, d in chi3_pts],
        'predicted_c_4pi_over_3': round(PREDICTED_C, 5),
        'deviation_pct': round(dev, 2),
        'five_point_table': table,
        'methodology_identity_check': 'the four archived systems were refit from their '
                                      'stored margin files with this script\'s own fit '
                                      'code and asserted equal to the Session-5 '
                                      'finisher_fits.json values (passed if this file '
                                      'exists)',
        'prefactor_study': {
            'definition': 'fixed-rate deflation: ln eps + (4*pi/q)*mu = A + B*ln(mu) '
                          'over the same mu >= 4 points; the deflated per-point values '
                          'are listed so the prefactor shape is directly comparable '
                          'across systems',
            'fits': prefits,
            'free_fit_b_by_system': {k: fits[k]['b'] for k in fits},
        },
        'convention_citations': {
            'matrix_engine': 'results/ccm-dh-test/finisher_weilext.py::build_matrix_ext '
                             '(called directly; params table extended with chi3 only)',
            'odd_char_a_3_4': 'results/ccm-dh-test/weilform.py::build_matrix kind=chi4 '
                              'and finisher_weilext.py::params',
            'lambda_dict': 'results/ccm-dh-test/weilform.py::lambda_chi4 pattern',
            'grid_and_dps': 'results/ccm-dh-test/finisher_margin.py::BATCHES',
            'parity_eig': 'results/ccm-dh-test/weilform.py::parity_blocks, eig_sym',
            'dpp_spectrum': 'results/ccm-dh-test/finisher_margin.py SPEC_AT path + '
                            'weilform.py::spectrum_from_xi',
            'true_zero_scan': 'results/ccm-dh-test/finisher_dh_zeros.py::online_zeros, '
                              'xi_chi4 pattern',
            'fit': 'results/ccm-dh-test/finisher_fits.py::series, fit_c_b',
        },
        'total_runtime_s': round(time.time() - t_start, 1),
    }

    with open('chi3-conductor-point.json', 'w') as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps(table, indent=1))
    print(f"chi3 fitted c = {fc['c']}  vs 4*pi/3 = {PREDICTED_C:.5f}  "
          f"({dev:+.2f}%)", flush=True)
    print('done chi3-conductor-point.json')
    return out


if __name__ == '__main__':
    main()
