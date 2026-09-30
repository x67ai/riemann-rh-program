"""
reverify.py -- independent re-verification of reported off-line zeros of chain members.
For each zero z (given to >= 20 digits by census.py, which used the TAIL formula at 30 digits and
rectangular contours):
  (i)  re-solve with the DIRECT truncated sum at 80 digits (different formula, different precision):
       secant from z + 1e-12(1+i); report |z' - z| and the 25-digit value;
  (ii) argument principle on a CIRCLE of radius r around z (different contour shape), 40 digits,
       tail formula: the count must be exactly 1;
  (iii) exclusion to the right of the census box: zero count in [smax, 3 smax] x [0.05, T] must be 0.
Usage: python reverify.py <census json> [how many zeros, default 3]
"""
import sys, json
import mpmath as mp
sys.path.insert(0, '.')
import stair as st
from census import make_member


def circle_count(E, z, r, n0=64, dmax=0.4):
    pts = [z + r*mp.expjpi(2*mp.mpf(j)/n0) for j in range(n0 + 1)]
    tot = mp.mpf(0)
    for j in range(n0):
        d, m = st.arg_change_segment(E, pts[j], pts[j + 1], n0=2, dmax=dmax)
        tot += d
    return tot/(2*mp.pi)


if __name__ == '__main__':
    rep = json.load(open(sys.argv[1]))
    howmany = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    chain_name, N, T = rep['chain'], rep['N'], mp.mpf(rep['T'])
    out = {'source': sys.argv[1], 'checks': []}
    offs = rep['offline_zeros'][:howmany]
    C, w, E = make_member(chain_name, N)
    for (re_, im_) in offs:
        mp.mp.dps = 80
        z = mp.mpc(re_, im_)
        if chain_name == 'smooth':
            kd = 400
        else:
            kd = N
        Ed = lambda s: C.E_direct(mp.mpc(s), w, kd)
        z2, it, ok = st.secant_complex(Ed, z + mp.mpc('1e-12', '1e-12'), z + mp.mpc('2e-12', '-1e-12'),
                                       tol=mp.mpf('1e-60'))
        d = abs(z2 - z)
        mp.mp.dps = 40
        # radius: a tenth of the distance to the nearest other reported zero, capped at 0.2
        others = [mp.mpc(a, b) for (a, b) in rep['offline_zeros'] if mp.mpc(a, b) != z]
        others += [mp.mpc(mp.mpf(1)/2, mp.mpf(t)) for t in rep['real_zeros']]
        dist = min([abs(z - o) for o in others] + [mp.mpf(1)])
        r = min(mp.mpf('0.2'), dist/4)
        cnt = circle_count(E, mp.mpc(z2), r)
        rec = {'reported': [re_, im_], 'direct80': mp.nstr(z2, 26), 'direct80_converged': ok,
               'shift': mp.nstr(d, 3), 'circle_radius': mp.nstr(r, 4), 'circle_count': mp.nstr(cnt, 8)}
        out['checks'].append(rec)
        print(rec); sys.stdout.flush()
    # (iii) exclusion to the right of the census box
    mp.mp.dps = 30
    smax = mp.mpf(rep['smax'])
    n, mn = st.count_zeros_rect(E, smax, 3*smax, mp.mpf('0.05'), T, n0=64, dmax=0.5)
    out['beyond_smax'] = {'box': [str(smax), str(3*smax), '0.05', str(T)], 'count': mp.nstr(n, 8),
                          'min_abs_on_contour': mp.nstr(mn, 4)}
    print('beyond smax:', out['beyond_smax'])
    tag = sys.argv[1].replace('census_', 'reverify_')
    json.dump(out, open(tag, 'w'), indent=1)
    print('saved', tag)
