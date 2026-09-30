"""
verify_violation.py -- direct verification of a flagged ordering violation for a chain member
(chain in {haglund, zeta}):  in the box B = [1/2 - w, 1/2 + w] x [t1, t2] around the FAILING lobe
  (1) real zeros of the member on the line in (t1, t2) (sign changes, step 0.005, bracketing refinement);
  (2) total zeros in B by the argument principle (adaptive, two precisions: 30 and 45 digits);
  (3) off-line zeros in the right half of B located by secant from grid minima of |E|, 22 digits, and re-counted
      by the argument principle on a circle (radius 0.02 or a quarter of the distance to the line);
  (4) the real zeros of the member on the line in the PASSING lobe (t3, t4) above.
A violation of the weak form is certified (numerically) when (2) - (1) >= 2 (an off-line pair inside B) and (4)
finds a real zero above t2.
Usage: python verify_violation.py chain N t1 t2 t3 t4 [w]
"""
import sys, json, time
import mpmath as mp
sys.path.insert(0, '.')
import stair as st
from census import make_member


def real_zeros(E, a, b, h):
    fr = lambda t: E(mp.mpc(mp.mpf(1)/2, t)).real
    n = int(mp.ceil((b - a)/h))
    ts = [a + (b - a)*mp.mpf(j)/n for j in range(n + 1)]
    vs = [fr(t) for t in ts]
    zs = []
    for j in range(n):
        if vs[j + 1] != 0 and mp.sign(vs[j]) != mp.sign(vs[j + 1]):
            zs.append(st.refine_real_root(fr, ts[j], ts[j + 1], vs[j], vs[j + 1]))
    return zs


if __name__ == '__main__':
    chain, N = sys.argv[1], int(sys.argv[2])
    t1, t2, t3, t4 = [mp.mpf(x) for x in sys.argv[3:7]]
    w = mp.mpf(sys.argv[7]) if len(sys.argv) > 7 else mp.mpf(1)
    t00 = time.time()
    rep = {'chain': chain, 'N': N, 'box': [str(t1), str(t2)], 'w': str(w)}
    counts = {}
    for dps in (30, 45):
        mp.mp.dps = dps
        C, wts, E = make_member(chain, N)
        n, mn = st.count_zeros_rect(E, mp.mpf(1)/2 - w, mp.mpf(1)/2 + w, t1, t2, n0=48, dmax=0.4)
        counts[dps] = n
        print(f'dps {dps}: argument-principle count in box = {mp.nstr(n, 10)} (min |E| on contour {mp.nstr(mn, 3)})  ({time.time()-t00:.0f}s)')
        sys.stdout.flush()
    mp.mp.dps = 30
    C, wts, E = make_member(chain, N)
    rz = real_zeros(E, t1, t2, mp.mpf('0.005'))
    print(f'real zeros in ({t1},{t2}): {len(rz)} -> {[mp.nstr(z, 15) for z in rz]}'); sys.stdout.flush()
    tot = int(mp.nint(counts[30].real))
    n_off = tot - len(rz)
    rep.update({'count_dps30': mp.nstr(counts[30], 10), 'count_dps45': mp.nstr(counts[45], 10),
                'real_zeros_box': [mp.nstr(z, 22) for z in rz], 'offline_in_box': n_off})
    # locate off-line zeros (right half)
    offs = []
    if n_off > 0:
        # seeds along the centre line of the box (the departing pair sits near the failing lobe's middle height);
        # secant from each; keep distinct roots inside the right half of the box (replaces a 1400-point grid)
        tm = (t1 + t2)/2
        for dsig in ('0.05', '0.12', '0.2', '0.3', '0.4', '0.55', '0.7', '0.85'):
            for dt in ('-0.3', '0', '0.3'):
                z = mp.mpc(mp.mpf(1)/2 + mp.mpf(dsig), tm + mp.mpf(dt))
                if not (t1 < z.imag < t2):
                    continue
                r, it, ok = st.secant_complex(E, z, z + mp.mpc('0.01', '0.01'))
                if ok and r.real > mp.mpf(1)/2 + mp.mpf('1e-15') and r.real < mp.mpf(1)/2 + w and t1 < r.imag < t2 \
                        and all(abs(r - q) > 1e-12 for q in offs):
                    offs.append(r)
            if len(offs) >= n_off // 2:
                break
        for r in offs:
            rad = min(mp.mpf('0.02'), (r.real - mp.mpf(1)/2)/4)
            pts = [r + rad*mp.expjpi(2*mp.mpf(k)/64) for k in range(65)]
            tot_arg = mp.mpf(0)
            for k in range(64):
                d, m = st.arg_change_segment(E, pts[k], pts[k + 1], n0=2, dmax=0.4)
                tot_arg += d
            cc = tot_arg/(2*mp.pi)
            # second precision re-solve
            with mp.workdps(50):
                C2, w2, E2 = make_member(chain, N)
                r2, it2, ok2 = st.secant_complex(E2, r + mp.mpc('1e-15', '1e-15'), r + mp.mpc('2e-15', '-1e-15'), tol=mp.mpf('1e-40'))
            rep.setdefault('offline_zeros', []).append({'zero': mp.nstr(r, 22), 'dist_to_line': mp.nstr(r.real - mp.mpf(1)/2, 10),
                                                        'circle_radius': mp.nstr(rad, 3), 'circle_count': mp.nstr(cc, 8),
                                                        'resolve_dps50': mp.nstr(r2, 26), 'shift': mp.nstr(abs(r2 - r), 3)})
            print('off-line zero:', rep['offline_zeros'][-1]); sys.stdout.flush()
    # passing lobe above
    rz2 = real_zeros(E, t3, t4, mp.mpf('0.005'))
    rep['real_zeros_passing_lobe'] = [mp.nstr(z, 22) for z in rz2]
    print(f'real zeros in passing lobe ({t3},{t4}): {[mp.nstr(z, 18) for z in rz2]}')
    rep['violation_certified'] = bool(n_off >= 2 and len(offs) >= 1 and len(rz2) >= 1)
    rep['elapsed_s'] = round(time.time() - t00)
    fn = f'violation_{chain}_N{N}_{int(t1)}.json'
    json.dump(rep, open(fn, 'w'), indent=1)
    print('violation certified (numerically):', rep['violation_certified'], '->', fn)
