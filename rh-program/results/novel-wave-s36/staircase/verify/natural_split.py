"""
natural_split.py -- the Hermite-Biehler test for the NATURAL split of Riemann's formula:
    xi(s) = A(s) + A(1-s),   A(s) = 1/4 + (1/2) s (s-1) sum_{n>=1} (pi n^2)^{-s/2} Gamma(s/2, pi n^2)
(A entire, real coefficients, so A#(s) := conj A(1 - conj s) = A(1-s)).  If |A(s)| > |A(1-s)| on Re s > 1/2
then xi has no zeros there (RH).  Tests:
  (1) the phase phi(t) = arg A(1/2+it): the infinitesimal HB margin at the line is 4|A|^2 phi'(t)
      (d/d sigma of |A(s)|^2 - |A(1-s)|^2 at sigma = 1/2); count where phi' < 0 on t in [1, 100];
  (2) zeros of A in Re s > 1/2 (argument principle on [1/2, smax] x [0.5, 200], A != 0 on the line since
      Im A(1/2+it) ~ -psi(1) t); lowest few located;
  (3) min over a grid in 1/2 < Re s <= 3, 1 <= t <= 100 of |A(s)|/|A(1-s)| - 1;
  (4) the same for the Davenport-Heilbronn split (odd type, no constant).
"""
import sys, json, time
import mpmath as mp
sys.path.insert(0, '.')
import stair as st

mp.mp.dps = 30
t00 = time.time()


def A_zeta(s, nmax=40):
    s = mp.mpc(s)
    acc = mp.fsum((mp.pi*n*n)**(-s/2) * mp.gammainc(s/2, mp.pi*n*n) for n in range(1, nmax))
    return mp.mpf(1)/4 + s*(s - 1)/2 * acc


DH = st.Chain('DH')


def A_dh(s, nmax=60):
    s = mp.mpc(s)
    acc = mp.mpc(0)
    for k in range(1, nmax):
        c = DH.coeff(k)
        if c == 0:
            continue
        X = mp.pi*k*k/5
        acc += c*k*X**(-(s + 1)/2)*mp.gammainc((s + 1)/2, X)
    return acc


out = {}
for name, A, Efull in (('zeta', A_zeta, st.Chain('zeta').E_full), ('DH', A_dh, DH.E_full)):
    # sanity: A(s) + A(1-s) = E_full(s)
    s0 = mp.mpc('0.7', '23.4')
    sanity = abs(A(s0) + A(1 - s0) - Efull(s0))/abs(Efull(s0))
    # (1) phase on the line
    ts = [mp.mpf(1) + mp.mpf(j)/20 for j in range(0, 99*20 + 1)]
    ph = [mp.arg(A(mp.mpc(mp.mpf(1)/2, t))) for t in ts]
    dph = [(ph[j + 1] - ph[j]) for j in range(len(ph) - 1)]
    neg = sum(1 for d in dph if d < 0)
    ph_range = (min(ph), max(ph))
    # (3) HB margin grid
    worst, arg = None, None
    for i in range(1, 11):
        sig = mp.mpf(1)/2 + mp.mpf(i)/4
        for j in range(0, 199):
            t = 1 + mp.mpf(j)/2
            s = mp.mpc(sig, t)
            r = abs(A(s))/abs(A(1 - s)) - 1
            if worst is None or r < worst:
                worst, arg = r, s
    rec = {'sanity_A+A#=E': mp.nstr(sanity, 3), 'phase_steps': len(dph), 'phase_steps_negative': neg,
           'phase_range_on_[1,100]': [mp.nstr(ph_range[0], 6), mp.nstr(ph_range[1], 6)],
           'HB_margin_min_grid': mp.nstr(worst, 6), 'HB_margin_argmin': mp.nstr(arg, 8)}
    print(name, rec, f'({time.time()-t00:.0f}s)'); sys.stdout.flush()
    # (2) zeros in the right half-plane
    if name == 'zeta':
        n, mn = st.count_zeros_rect(A, mp.mpf(1)/2, mp.mpf(90), mp.mpf('0.5'), mp.mpf(200), n0=64, dmax=0.5)
        rec['zeros_in_[0.5,90]x[0.5,200]'] = mp.nstr(n, 8)
        # lowest zeros: scan a coarse grid for local minima of |A|, then secant
        grid = {}
        for i in range(0, 121):
            for j in range(0, 161):
                sig = mp.mpf('0.75') + mp.mpf(i)/4
                t = mp.mpf(1) + mp.mpf(j)/2
                grid[(i, j)] = (mp.mpc(sig, t), abs(A(mp.mpc(sig, t))))
        found = []
        for (i, j), (z, v) in grid.items():
            nb = [grid.get((i + a, j + b)) for a in (-1, 0, 1) for b in (-1, 0, 1) if (a, b) != (0, 0)]
            if all(x is not None and v <= x[1] for x in nb):
                r, it, ok = st.secant_complex(A, z, z + mp.mpc('0.05', '0.05'))
                if ok and r.real > mp.mpf('0.5') and all(abs(r - q) > 1e-8 for q in found):
                    found.append(r)
        found.sort(key=lambda z: z.imag)
        rec['lowest_zeros_of_A_right_half'] = [mp.nstr(z, 18) for z in found[:6]]
        print(name, 'zeros of A in right half:', rec['zeros_in_[0.5,90]x[0.5,200]'], 'lowest:', rec['lowest_zeros_of_A_right_half'][:3],
              f'({time.time()-t00:.0f}s)'); sys.stdout.flush()
    out[name] = rec
# (5) HB margin of the natural split of the MEMBERS xi_N = A_N + A_N(1-s), A_N = 1/4 + (1/2)s(s-1) sum_{n<=N} X^{-s/2}Gamma(s/2,X)
out['members'] = {}
for N in (1, 2, 3, 5):
    AN = lambda s, N=N: A_zeta(s, nmax=N + 1)
    worst, arg, negcount, tot = None, None, 0, 0
    for i in range(1, 11):
        sig = mp.mpf(1)/2 + mp.mpf(i)/4
        for j in range(0, 399):
            t = 1 + mp.mpf(j)/2
            s = mp.mpc(sig, t)
            r = abs(AN(s))/abs(AN(1 - s)) - 1
            tot += 1
            if r < 0:
                negcount += 1
            if worst is None or r < worst:
                worst, arg = r, s
    out['members'][N] = {'HB_margin_min_grid[0.75..3]x[1..200]': mp.nstr(worst, 6), 'argmin': mp.nstr(arg, 8),
                         'fraction_negative': mp.nstr(mp.mpf(negcount)/tot, 4)}
    print('member N =', N, out['members'][N], f'({time.time()-t00:.0f}s)'); sys.stdout.flush()
json.dump(out, open('natural_split.json', 'w'), indent=1)
print('saved natural_split.json')
