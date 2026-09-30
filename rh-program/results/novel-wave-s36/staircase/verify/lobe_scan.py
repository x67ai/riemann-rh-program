"""
lobe_scan.py -- search for violations of the ordering invariant ("monotonic zeros") in the departure window of
each member, using the lobe laws (Theorems D, D'):
  * seed's C1:      xi_N(1/2+it) = Xi(t) + P_N(t),  P_N > 0  -> real zeros = pairs in NEGATIVE lobes of Xi deeper than P_N;
  * Haglund's Xi_N: Xi_N(t) = Xi(t) - Q_N(t),        Q_N > 0  -> real zeros = pairs in POSITIVE lobes deeper than Q_N
                    (plus one zero in the central lobe (0, gamma_1)).
A lobe that FAILS (depth < level) below a lobe that PASSES (depth > level) forces an off-line zero below a real zero:
a violation of the weak form of Haglund's Conjecture 1 (arXiv:0910.5228, Remark 1) for Xi_N, or of the ordering
invariant for xi_N.  This script only FLAGS candidates from the lobe pattern; flagged cases are verified by a direct
zero census of the member (verify_violation.py).
Window per N: [4(N+1)^2 - 40, 4(N+1)^2 + 90].  Zeros of Z(t) by sign changes (mpmath siegelz, step 0.01), checked
against mpmath nzeros on the window.  Xi(t) = -(t^2+1/4)/2 pi^{-1/4} |Gamma(1/4+it/2)| Z(t).
Usage: python lobe_scan.py Nmin Nmax
"""
import sys, json, time
import mpmath as mp
sys.path.insert(0, '.')
import stair as st

mp.mp.dps = 25
Z = st.Chain('zeta')


def Xi_from_Z(t, z):
    return -(t*t + mp.mpf(1)/4)/2 * mp.pi**(-mp.mpf(1)/4) * mp.exp(mp.re(mp.loggamma(mp.mpf(1)/4 + 1j*t/2))) * z


def P_N(t, N):
    s = mp.mpc(mp.mpf(1)/2, t)
    acc = mp.fsum(Z.T(s, n) for n in range(N + 1, N + 10))
    return ((mp.mpf(1)/4 + t*t)/2 * acc).real


def golden_max(f, a, b, it=50):
    g = (mp.sqrt(5) - 1)/2
    c, d = b - g*(b - a), a + g*(b - a)
    fc, fd = f(c), f(d)
    for _ in range(it):
        if fc > fd:
            b, d, fd = d, c, fc
            c = b - g*(b - a); fc = f(c)
        else:
            a, c, fc = c, d, fd
            d = a + g*(b - a); fd = f(d)
    return (c, fc) if fc > fd else (d, fd)


def zeros_in(a, b, h=mp.mpf('0.01')):
    n = int((b - a)/h)
    ts = [a + (b - a)*mp.mpf(j)/n for j in range(n + 1)]
    zs = [mp.siegelz(t) for t in ts]
    out = []
    for j in range(n):
        if mp.sign(zs[j]) != mp.sign(zs[j + 1]):
            lo, hi, flo = ts[j], ts[j + 1], zs[j]
            for _ in range(40):
                m = (lo + hi)/2
                fm = mp.siegelz(m)
                if mp.sign(fm) == mp.sign(flo):
                    lo, flo = m, fm
                else:
                    hi = m
            out.append((lo + hi)/2)
    return out


if __name__ == '__main__':
    Nmin, Nmax = int(sys.argv[1]), int(sys.argv[2])
    t00 = time.time()
    res = {}
    for N in range(Nmin, Nmax + 1):
        a = mp.mpf(4*(N + 1)**2 - 40)
        b = mp.mpf(4*(N + 1)**2 + 90)
        zs = zeros_in(a, b)
        nz_check = mp.nzeros(b) - mp.nzeros(a)
        cN = st.c_N(N)
        lobes = []
        for j in range(len(zs) - 1):
            lo, hi = zs[j], zs[j + 1]
            mid = (lo + hi)/2
            sgn = -mp.sign(mp.siegelz(mid))          # sign of Xi on the lobe
            f = lambda t: sgn*Xi_from_Z(t, mp.siegelz(t))
            tstar, depth = golden_max(f, lo, hi, it=30)
            PN = P_N(tstar, N)
            QN = cN - PN
            lobes.append({'lo': lo, 'hi': hi, 'sign': int(sgn), 'tstar': tstar, 'depth': depth,
                          'r_seed': depth/PN if sgn < 0 else None, 'r_hag': depth/QN if sgn > 0 else None,
                          'QN_pos': bool(QN > 0)})
        out = {'window': [str(a), str(b)], 'n_zeros_signchange': len(zs), 'n_zeros_nzeros': int(nz_check),
               'Q_N_positive_everywhere_sampled': all(L['QN_pos'] for L in lobes)}
        for key, sg in (('seed', -1), ('hag', 1)):
            seq = [(L['lo'], L['hi'], L['r_' + key]) for L in lobes if L['sign'] == sg]
            flags = [r > 1 for (_, _, r) in seq]
            # violation pattern: some False followed later by some True
            first_fail = next((i for i, f in enumerate(flags) if not f), None)
            viol = first_fail is not None and any(flags[first_fail + 1:])
            last_pass = max([i for i, f in enumerate(flags) if f], default=None)
            out[key] = {'violation_pattern': viol,
                        'first_fail': [mp.nstr(seq[first_fail][0], 12), mp.nstr(seq[first_fail][1], 12), mp.nstr(seq[first_fail][2], 5)] if first_fail is not None else None,
                        'last_pass': [mp.nstr(seq[last_pass][0], 12), mp.nstr(seq[last_pass][1], 12), mp.nstr(seq[last_pass][2], 5)] if last_pass is not None else None,
                        'ratios': [[mp.nstr(x, 10), mp.nstr(y, 10), mp.nstr(r, 4)] for (x, y, r) in seq]}
        res[N] = out
        print(f"N={N} window [{a},{b}]: zeros {len(zs)} (nzeros {int(nz_check)}); Q_N>0: {out['Q_N_positive_everywhere_sampled']}; "
              f"seed: violation={out['seed']['violation_pattern']} first_fail={out['seed']['first_fail']} last_pass={out['seed']['last_pass']}; "
              f"Haglund: violation={out['hag']['violation_pattern']} first_fail={out['hag']['first_fail']} last_pass={out['hag']['last_pass']}  "
              f"({time.time()-t00:.0f}s)")
        sys.stdout.flush()
        json.dump(res, open(f'lobe_scan_{Nmin}_{Nmax}.json', 'w'), indent=1)
    print('saved')
