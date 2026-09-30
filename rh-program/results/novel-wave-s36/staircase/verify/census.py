"""
census.py -- COMPLETE zero census of a chain member E (entire, E(1-s) = E(s), E(conj s) = conj E(s))
in the box {0 < Im s <= T} (all Re s), by:
  (1) real zeros on Re s = 1/2 : sign changes of E(1/2+it) (real) on a grid of step h, refined by a
      relative-tolerance Illinois bracket;
  (2) total count Z_tot in the symmetric rectangle [1-smax, smax] x [0, T] by the argument principle,
      computed from the right edge (Re s = smax, t: 0 -> T) and the right half of the top edge
      (t = T, Re s: smax -> 1/2), using E(1 - conj s) = conj E(s) for the left half and E > 0 on the real
      segment (checked);
  (3) off-line zeros in Re s > 1/2 : expected (Z_tot - Z_line)/2 ; located by secant from local minima of
      |E| on a band around the predicted branch, then by argument-principle quadtree if any are missing;
  (4) no zeros with Re s > smax, 0 < t <= T: checked by the ratio |E - Gamma_N|/|Gamma_N| < 1 on a grid of
      the strip smax <= Re s <= smax + 40 (Gamma_N = the dominant Gamma-part), and Gamma growth beyond.
Usage:  python census.py <chain> <N> <T> [smax]      chain in {zeta, trunc-zeta}; results to census_<tag>.json
"""
import sys, json, time
import mpmath as mp
sys.path.insert(0, '.')
import stair as st


def make_member(chain_name, N, extra=None):
    if chain_name == 'zeta':
        C = st.Chain('zeta')
        w = st.w_trunc(N)
    elif chain_name == 'smooth':      # C2: S-smooth index set, S = first N primes
        C = st.Chain('zeta')
        S = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37][:N]
        w = st.smooth_numbers_weight(S)
    elif chain_name.startswith('Faq'):
        _, a, q = chain_name.split(':')
        C = st.Chain('Faq', a=a, q=int(q))
        w = st.w_trunc(N)
    elif chain_name == 'DH':
        C = st.Chain('DH')
        w = st.w_trunc(N)
    elif chain_name == 'chi4':
        C = st.Chain('chi4')
        w = st.w_trunc(N)
    elif chain_name == 'haglund':      # Haglund's Xi_N = xi_N - c_N (arXiv:0910.5228, (13)-(14))
        C = st.Chain('zeta')
        w = st.w_trunc(N)
        cNh = st.c_N(N)

        def E(s):
            s = mp.mpc(s)
            return st.E_auto(C, s, w, N) - cNh
        return C, w, E
    else:
        raise ValueError(chain_name)
    kmax_direct = N if chain_name != 'smooth' else 10**6

    def E(s):
        s = mp.mpc(s)
        if chain_name == 'smooth':
            return st.E_auto(C, s, w, 400)
        return st.E_auto(C, s, w, N)
    return C, w, E


def gamma_part(C, s, w, N):
    """Dominant Gamma-part for Re s > 1/2 : pref(s) * sum_k w_k b_k X_k^{-(s+kap)/2} Gamma((s+kap)/2)."""
    kap = C.kap
    a1 = (s + kap)/2
    acc = mp.fsum(w(k) * C.coeff(k) * k**kap * (mp.pi*k*k/C.Q)**(-a1) for k in range(1, N + 1)
                  if w(k) != 0 and C.coeff(k) != 0)
    return C.pref(s) * mp.gamma(a1) * acc


def real_zeros(E, T, h, t0=mp.mpf('0.1')):
    fr = lambda t: E(mp.mpc(mp.mpf(1)/2, t)).real
    n = int(mp.ceil((T - t0)/h))
    ts = [t0 + (T - t0)*mp.mpf(j)/n for j in range(n + 1)]
    vs = [fr(t) for t in ts]
    zs = []
    for j in range(n):
        if vs[j] == 0:
            zs.append(ts[j]); continue
        if vs[j + 1] != 0 and mp.sign(vs[j]) != mp.sign(vs[j + 1]):
            zs.append(st.refine_real_root(fr, ts[j], ts[j + 1], vs[j], vs[j + 1]))
    # same-sign local minima that are tiny relative to neighbors (possible missed close pair)
    susp = []
    for j in range(1, n):
        a, b, c = abs(vs[j - 1]), abs(vs[j]), abs(vs[j + 1])
        if b < a and b < c and mp.sign(vs[j - 1]) == mp.sign(vs[j]) == mp.sign(vs[j + 1]) and b < 0.05*min(a, c):
            susp.append(ts[j])
    return zs, susp, ts, vs


def total_count(E, smax, T, dmax=0.5):
    cache = {}
    d_right, m1 = st.arg_change_segment(E, mp.mpc(smax, 0), mp.mpc(smax, T), n0=64, cache=cache, dmax=dmax)
    d_top, m2 = st.arg_change_segment(E, mp.mpc(smax, T), mp.mpc(mp.mpf(1)/2, T), n0=64, cache=cache, dmax=dmax)
    # bottom edge: E real on the real axis; check positivity on [1/2, smax]
    bottom = [E(mp.mpc(x, 0)) for x in [mp.mpf(1)/2 + (smax - mp.mpf(1)/2)*mp.mpf(j)/200 for j in range(201)]]
    minbottom = min(v.real for v in bottom)
    maxim = max(abs(v.imag) / abs(v) for v in bottom)
    Ztot = (d_right + d_top)/mp.pi
    return Ztot, d_right, d_top, minbottom, maxim, min(m1, m2)


def branch_curve(C, w, N, T, cN, t_lo):
    """sigma_c(t): |Gamma-part| = level on Re s > 1/2, for t in [t_lo, T] (None where Gamma-part > level at the line).
    cN is a constant level (even-type chains: the limit c_N of E_N on the line) or a callable level(s)
    (odd-type chains: |K_N|/|s|^2, K_N = lim t^2 E_N(1/2+it))."""
    out = []
    t = t_lo
    while t <= T:
        def L(sig):
            s = mp.mpc(sig, t)
            lev = cN(s) if callable(cN) else cN
            return mp.log(abs(gamma_part(C, s, w, N))) - mp.log(lev)
        if L(mp.mpf(1)/2) > 0:
            out.append((t, None))
        else:
            lo, hi = mp.mpf(1)/2, mp.mpf(1)
            while L(hi) < 0:
                lo, hi = hi, hi*2
            for _ in range(40):
                mid = (lo + hi)/2
                if L(mid) < 0:
                    lo = mid
                else:
                    hi = mid
            out.append((t, (lo + hi)/2))
        t += mp.mpf('0.5')
    return out


def locate_offline(E, curve, T, band=4, ds=mp.mpf('0.5'), dt=mp.mpf('0.5')):
    """Seeds from local minima of |E| on a band around the branch curve, refined by secant."""
    grid = {}
    pts = []
    for (t, sc) in curve:
        if sc is None:
            continue
        for j in range(-int(band/ds), int(band/ds) + 1):
            sig = sc + j*ds
            if sig <= mp.mpf('0.52'):
                continue
            key = (int(mp.nint(t/dt)), int(mp.nint(sig/ds)))
            grid[key] = (mp.mpc(sig, t), abs(E(mp.mpc(sig, t))))
    seeds = []
    for key, (z, v) in grid.items():
        i, j = key
        nb = [grid.get((i + a, j + b)) for a in (-1, 0, 1) for b in (-1, 0, 1) if (a, b) != (0, 0)]
        nb = [x for x in nb if x is not None]
        if len(nb) >= 5 and all(v <= x[1] for x in nb):
            seeds.append(z)
    zeros = []
    for z0 in seeds:
        r, it, ok = st.secant_complex(E, z0, z0 + mp.mpc('0.05', '0.05'))
        if ok and r.real > mp.mpf('0.5') + mp.mpf('1e-12') and 0 < r.imag <= T:
            if all(abs(r - q) > mp.mpf('1e-10') for q in zeros):
                zeros.append(r)
    return sorted(zeros, key=lambda z: z.imag), len(seeds)


def quadtree(E, s1, s2, t1, t2, depth=0, maxdepth=14, found=None):
    """All zeros in the open box by recursive argument-principle subdivision + secant."""
    found = [] if found is None else found
    n, mn = st.count_zeros_rect(E, s1, s2, t1, t2, n0=16, dmax=0.5)
    k = int(mp.nint(n.real))
    if k <= 0:
        return found
    if k == 1 or depth >= maxdepth:
        z0 = mp.mpc((s1 + s2)/2, (t1 + t2)/2)
        r, it, ok = st.secant_complex(E, z0, z0 + mp.mpc((s2 - s1)/10, (t2 - t1)/10))
        if ok and s1 <= r.real <= s2 and t1 <= r.imag <= t2:
            found.append(r)
            if k == 1:
                return found
    # split along the longer side
    if (s2 - s1) >= (t2 - t1):
        m = (s1 + s2)/2 + (s2 - s1)*mp.mpf('0.0137')
        quadtree(E, s1, m, t1, t2, depth + 1, maxdepth, found)
        quadtree(E, m, s2, t1, t2, depth + 1, maxdepth, found)
    else:
        m = (t1 + t2)/2 + (t2 - t1)*mp.mpf('0.0137')
        quadtree(E, s1, s2, t1, m, depth + 1, maxdepth, found)
        quadtree(E, s1, s2, m, t2, depth + 1, maxdepth, found)
    return found


if __name__ == '__main__':
    chain_name = sys.argv[1]
    N = int(sys.argv[2])
    T = mp.mpf(sys.argv[3])
    smax_arg = mp.mpf(sys.argv[4]) if len(sys.argv) > 4 else None
    h = mp.mpf(sys.argv[5]) if len(sys.argv) > 5 else mp.mpf('0.02')
    mp.mp.dps = 30
    tag = f'{chain_name.replace(":", "_")}_N{N}_T{int(T)}'
    C, w, E = make_member(chain_name, N)
    t0 = time.time()
    rep = {'chain': chain_name, 'N': N, 'T': str(T), 'dps': mp.mp.dps}
    # (1) real zeros
    zs, susp, ts, vs = real_zeros(E, T, h)
    rep['real_zeros'] = [mp.nstr(z, 22) for z in zs]
    rep['n_real'] = len(zs)
    rep['suspicious_same_sign_minima'] = [mp.nstr(x, 10) for x in susp]
    print(f'[{tag}] real zeros: {len(zs)}; suspicious minima: {len(susp)}  ({time.time()-t0:.0f}s)'); sys.stdout.flush()
    # (2) branch curve & smax
    if C.kind == 'zeta' and chain_name != 'haglund':
        cN = st.c_N(N) if chain_name == 'zeta' else mp.fsum((4*mp.pi*n*n - 1)*mp.exp(-mp.pi*n*n)
                                                              for n in range(2, 400) if w(n) == 0)
    elif C.kind == 'Faq':
        cN = mp.fsum(C.coeff(k)*(4*mp.pi*k*k/C.Q - 1)*mp.exp(-mp.pi*k*k/C.Q) for k in range(N + 1, N + 80))
    else:
        tbig = mp.mpf(3000)
        KN = tbig**2 * E(mp.mpc(mp.mpf(1)/2, tbig)).real
        rep['K_N_estimate'] = mp.nstr(KN, 12)
        cN = (lambda s, KN=KN: abs(KN)/abs(s*(1 - s)))
    rep['level_constant'] = mp.nstr(cN, 15) if not callable(cN) else 'K_N/|s(1-s)|'
    curve = []
    smax = smax_arg
    if cN is not None:
        t_lo = zs[-1] - 10 if zs else mp.mpf(1)
        curve = branch_curve(C, w, N if chain_name != 'smooth' else 400, T, cN, max(mp.mpf(1), t_lo))
        sc_max = max([sc for (t, sc) in curve if sc is not None] or [mp.mpf(1)])
        if smax is None:
            smax = mp.ceil(sc_max + 20)
        rep['branch_sigma_at_T'] = mp.nstr(curve[-1][1], 8) if curve[-1][1] is not None else None
    if smax is None:
        smax = mp.mpf(30)
    rep['smax'] = str(smax)
    # (3) total count
    Ztot, dr, dtop, minb, maxim, minabs = total_count(E, smax, T)
    rep['Z_total_raw'] = mp.nstr(Ztot, 10)
    rep['bottom_min'] = mp.nstr(minb, 5)
    rep['contour_min_abs'] = mp.nstr(minabs, 5)
    Zt = int(mp.nint(Ztot))
    rep['Z_total'] = Zt
    n_off = (Zt - len(zs))
    rep['n_offline_expected_right_half'] = n_off/2
    print(f'[{tag}] Z_total = {mp.nstr(Ztot, 8)} (smax = {smax}); real = {len(zs)}; off-line expected (right half) = {n_off/2}; bottom min = {mp.nstr(minb, 4)}  ({time.time()-t0:.0f}s)'); sys.stdout.flush()
    # (4) locate off-line zeros
    off = []
    if n_off > 0:
        if curve:
            off, nseeds = locate_offline(E, curve, T)
            rep['n_seeds'] = nseeds
        print(f'[{tag}] located {len(off)} off-line zeros from the branch band  ({time.time()-t0:.0f}s)'); sys.stdout.flush()
        if len(off) < n_off/2:
            # near-line band (in-strip off-line zeros are not on the branch): grid minima of |E| on
            # Re s in {0.6, 0.75, 0.9, 1.05, 1.25, 1.5}, t step 0.25, then secant
            band = {}
            sigs = [mp.mpf(x) for x in ('0.6', '0.75', '0.9', '1.05', '1.25', '1.5')]
            nt = int(T/mp.mpf('0.25'))
            for i, sg in enumerate(sigs):
                for j in range(1, nt + 1):
                    z = mp.mpc(sg, mp.mpf(j)/4)
                    band[(i, j)] = (z, abs(E(z)))
            for (i, j), (z, v) in band.items():
                nb = [band.get((i + a, j + b)) for a in (-1, 0, 1) for b in (-1, 0, 1) if (a, b) != (0, 0)]
                nb = [x for x in nb if x is not None]
                if len(nb) >= 3 and all(v <= x[1] for x in nb):
                    r, it, ok = st.secant_complex(E, z, z + mp.mpc('0.02', '0.02'))
                    if ok and r.real > mp.mpf('0.5') + mp.mpf('1e-12') and 0 < r.imag <= T and all(abs(r - q) > mp.mpf('1e-10') for q in off):
                        off.append(r)
            off.sort(key=lambda z: z.imag)
            print(f'[{tag}] near-line band: now {len(off)} off-line zeros  ({time.time()-t0:.0f}s)'); sys.stdout.flush()
        if len(off) < n_off/2:
            # quadtree over the whole half-box, avoiding a thin strip at the line
            print(f'[{tag}] missing {n_off/2 - len(off)}; running quadtree on [0.5+1e-3, smax] x [0, T]'); sys.stdout.flush()
            q = quadtree(E, mp.mpf('0.501'), smax, mp.mpf('0.05'), T)
            for r in q:
                if all(abs(r - z) > mp.mpf('1e-10') for z in off):
                    off.append(r)
            off.sort(key=lambda z: z.imag)
    rep['offline_zeros'] = [[mp.nstr(z.real, 22), mp.nstr(z.imag, 22)] for z in off]
    rep['n_offline_found'] = len(off)
    rep['complete'] = (len(off) == n_off/2)
    rep['elapsed_s'] = round(time.time() - t0)
    print(f'[{tag}] off-line zeros found: {len(off)} / expected {n_off/2}; complete = {rep["complete"]}  ({rep["elapsed_s"]}s)')
    if off:
        z = off[0]
        print(f'[{tag}] lowest off-line zero: {mp.nstr(z, 22)}')
        for z in off[:6]:
            print('      ', mp.nstr(z, 18), ' |E| =', mp.nstr(abs(E(z)), 3))
    with open(f'census_{tag}.json', 'w') as fh:
        json.dump(rep, fh, indent=1)
    print(f'[{tag}] saved census_{tag}.json')
