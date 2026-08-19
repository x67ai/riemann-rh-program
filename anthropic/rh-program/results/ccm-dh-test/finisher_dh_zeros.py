"""
finisher_dh_zeros.py -- Does the D'' spectrum reproduce the TRUE on-line zeros of
the respective function (not just zeta's)?  Session-4 never archived the DH zero
list, so the DH spectral-matching claim was unverifiable.  Computes:

  - DH on-line zeros to t=46 (sign changes of the real completed Xi_DH on the line);
  - L(s,chi4) (odd char mod 4) and L(s,chi5) (Legendre mod 5) on-line zeros to t=46;
  - zeta zeros 1..10 (mp.zetazero);
  - error tables |D''_root - true zero| for the stored spectra
    (gz/gd lam2 N48, lam3 N40) and, if present, the finisher chi spectra (lam3 N48).

Output: outputs/finisher_dh_zeros.json
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
sys.path.insert(0, HERE)

import mpmath as mp
import dh

mp.mp.dps = 40


def xi_chi4(s):
    Lf = 4**(-s)*(mp.zeta(s, mp.mpf(1)/4) - mp.zeta(s, mp.mpf(3)/4))
    return (4/mp.pi)**((s + 1)/2)*mp.gamma((s + 1)/2)*Lf


def xi_chi5(s):
    Lf = 5**(-s)*(mp.zeta(s, mp.mpf(1)/5) - mp.zeta(s, mp.mpf(2)/5)
                  - mp.zeta(s, mp.mpf(3)/5) + mp.zeta(s, mp.mpf(4)/5))
    return (5/mp.pi)**(s/2)*mp.gamma(s/2)*Lf


def online_zeros(xifun, tmax, step=mp.mpf('0.12')):
    zs = []
    t = mp.mpf('0.4')
    v = xifun(mp.mpf('0.5') + 1j*t)
    assert abs(v.imag) < 1e-15*max(1, abs(v.real)), 'completed fn not real on line'
    zprev = v.real
    while t < tmax:
        t2 = t + step
        znew = xifun(mp.mpf('0.5') + 1j*t2).real
        if mp.sign(znew) != mp.sign(zprev) and zprev != 0:
            r = mp.findroot(lambda u: xifun(mp.mpf('0.5') + 1j*u).real,
                            (t, t2), solver='illinois')
            zs.append(r)
        t, zprev = t2, znew
    return zs


OUT = {}
print('scanning DH...', flush=True)
dh_zeros = online_zeros(dh.xi_dh, mp.mpf(46))
OUT['dh_online_zeros_to_46'] = [mp.nstr(z, 15) for z in dh_zeros]
print('DH zeros:', [mp.nstr(z, 8) for z in dh_zeros], flush=True)

print('scanning chi4...', flush=True)
c4_zeros = online_zeros(xi_chi4, mp.mpf(46))
OUT['chi4_online_zeros_to_46'] = [mp.nstr(z, 15) for z in c4_zeros]
print('chi4 zeros:', [mp.nstr(z, 8) for z in c4_zeros], flush=True)

print('scanning chi5...', flush=True)
c5_zeros = online_zeros(xi_chi5, mp.mpf(46))
OUT['chi5_online_zeros_to_46'] = [mp.nstr(z, 15) for z in c5_zeros]
print('chi5 zeros:', [mp.nstr(z, 8) for z in c5_zeros], flush=True)

zz = [mp.zetazero(k).imag for k in range(1, 11)]
OUT['zeta_zeros_1_10'] = [mp.nstr(z, 15) for z in zz]


def err_table(spec_strs, true_zeros, nmax=8):
    """Greedy nearest-match of the first nmax D'' roots to true zeros."""
    rows = []
    for s in spec_strs[:nmax]:
        r = mp.mpf(s)
        best = min(true_zeros, key=lambda z: abs(z - r))
        rows.append({'dpp_root': mp.nstr(r, 15), 'nearest_true_zero': mp.nstr(best, 15),
                     'abs_err': mp.nstr(abs(r - best), 3)})
    return rows


def load(fn):
    with open(fn) as fh:
        return json.load(fh)


gz2 = load('outputs/ground_gz_lam2.json')
gz3 = load('outputs/ground_gz_lam3.json')
gd2 = load('outputs/ground_gd_lam2.json')
gd3 = load('outputs/ground_gd_lam3.json')
spec = lambda data, N: next(r['dpp_spectrum_pos'] for r in data['runs']
                            if r.get('dpp_spectrum_pos') and r['N'] == N)
OUT['match_zeta_lam2_N48'] = err_table(spec(gz2, 48), zz)
OUT['match_zeta_lam3_N40'] = err_table(spec(gz3, 40), zz)
OUT['match_dh_lam2_N48'] = err_table(spec(gd2, 48), dh_zeros)
OUT['match_dh_lam3_N40'] = err_table(spec(gd3, 40), dh_zeros)

for batch, zeros in (('chi4', c4_zeros), ('chi5', c5_zeros)):
    fn = f'outputs/finisher_margin_{batch}.json'
    if os.path.exists(fn):
        data = load(fn)
        specs = [r for r in data if r.get('dpp_spectrum_pos')]
        if specs:
            OUT[f'match_{batch}_lam3_N48'] = err_table(
                specs[0]['dpp_spectrum_pos'], zeros)

# DH zero-count vs D'' count below 45 (density comparison)
OUT['counts_below_45'] = {
    'dh_true': sum(1 for z in dh_zeros if z < 45),
    'dh_dpp_lam3_N40': sum(1 for s in spec(gd3, 40) if mp.mpf(s) < 45),
    'zeta_true': sum(1 for z in zz if z < 45),
    'zeta_dpp_lam3_N40': sum(1 for s in spec(gz3, 40) if mp.mpf(s) < 45),
}
OUT['caveat'] = ('spectrum_from_xi only finds sign-change roots between consecutive '
                 'integer index points, so D-prime-prime root lists can MISS close '
                 'pairs; count comparisons are indicative only.')

with open('outputs/finisher_dh_zeros.json', 'w') as fh:
    json.dump(OUT, fh, indent=1)
print('done outputs/finisher_dh_zeros.json')
