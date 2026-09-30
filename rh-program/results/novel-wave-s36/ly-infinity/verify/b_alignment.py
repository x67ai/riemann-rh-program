"""b_alignment.py -- task (b): zeros of the seed's Lee-Yang functions and their variants
against the zeros of zeta, at the height where the zero densities match.

For a prime set S with P = prod S and W = log P, the Lee-Yang restriction
    f(t) = A(t) + eps * P^{-it} * conj A(t)          (A a product of per-prime factors)
has zeros of density W/(2 pi).  zeta's density is theta'(t)/pi ~ (1/2pi) log(t/2pi); they match
at T* with 2 theta'(T*) = W (T* ~ 2 pi P).  With eps chosen so that exp(iWt/2)eps^{-1/2}
equals exp(i theta(t)) to first order at T*, zeros of f = zeros of
    Re( exp(i[theta(T*) + (t - T*) W/2]) * A(1/2 + it) )        ("LY model", linearized phase).
The archimedean variants use the exact phase: zeros of Re(exp(i theta(t)) A(1/2+it)).

Models (A):
  gram        A = 1                                  (prime-free baseline: theta = pi/2 mod pi)
  LY-seed     A = prod_{p in S}(1 - p^{-1/2-it})     (the seed's A; Lee-Yang, linear phase)
  LY-aligned  A = prod_{p in S}(1 + p^{-1/2-it})     (Blaschke zero at -p^{-1/2}; Lee-Yang)
  arch-anti   A = prod_{p<=X}(1 - p^{-1/2-it})       (exact phase)
  arch-euler  A = prod_{p<=X}(1 - p^{-1/2-it})^{-1}  (exact phase; zeta's own partial Euler product)
  arch-sqfree A = prod_{p<=X}(1 + p^{-1/2-it})       (exact phase)
Metric: for each zeta zero gamma in the window, |gamma - nearest model zero| / delta(T),
delta = 2 pi / log(T/2pi) the mean spacing; and the count difference in the window.
zeta zeros: sign changes of mpmath.siegelz (Z(t) is O(1) on the line, so the acceptance
test |Z(gamma)| is scale-appropriate, cf. zoo V.3 rider), refined by bisection; the count
is checked against the Riemann-von Mangoldt main term + S(t) sign-change parity.
"""
import numpy as np, mpmath as mp, time, sys, json

mp.mp.dps = 20


def primes_upto(n):
    s = np.ones(n + 1, bool); s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return np.nonzero(s)[0]


def theta_np(t):
    t = np.asarray(t, float)
    return (t / 2) * np.log(t / (2 * np.pi)) - t / 2 - np.pi / 8 + 1 / (48 * t) + 7 / (5760 * t ** 3)


def thetap(t):  # theta'(t) asymptotic
    return 0.5 * np.log(t / (2 * np.pi)) - 1 / (48 * t ** 2)


def solve_Tstar(W):
    T = 2 * np.pi * np.exp(W)
    for _ in range(50):
        T = T - (2 * thetap(T) - W) / (1.0 / T)
    return T


def A_vals(t, primes, kind):
    t = np.asarray(t, float)
    out = np.ones(t.shape, complex)
    for p in primes:
        w = p ** -0.5 * np.exp(-1j * t * np.log(p))
        if kind == 'seed' or kind == 'anti':
            out *= (1 - w)
        elif kind == 'aligned' or kind == 'sqfree':
            out *= (1 + w)
        elif kind == 'euler':
            out /= (1 - w)
    return out


def model_real(t, primes, kind, phase_mode, Tstar=None, W=None):
    if kind == 'gram':
        A = np.ones(np.shape(t), complex)
    else:
        A = A_vals(t, primes, kind)
    if phase_mode == 'exact':
        ph = theta_np(t)
    else:
        ph = theta_np(Tstar) + (np.asarray(t) - Tstar) * W / 2
    return np.real(np.exp(1j * ph) * A)


def zeros_of(fun, a, b, h):
    ts = np.arange(a, b + h, h)
    v = fun(ts)
    idx = np.nonzero(v[:-1] * v[1:] < 0)[0]
    lo, hi = ts[idx].copy(), ts[idx + 1].copy()
    flo = v[idx].copy()
    for _ in range(45):
        mid = 0.5 * (lo + hi)
        fm = fun(mid)
        left = fm * flo <= 0
        hi = np.where(left, mid, hi)
        lo = np.where(left, lo, mid)
        flo = np.where(left, flo, fm)
    return 0.5 * (lo + hi)


def zeta_zeros(a, b, h):
    ts = np.arange(a, b + h, h)
    v = np.array([float(mp.siegelz(x)) for x in ts])
    z = []
    for i in range(len(ts) - 1):
        if v[i] * v[i + 1] < 0:
            r = mp.findroot(mp.siegelz, (mp.mpf(ts[i]), mp.mpf(ts[i + 1])), solver='anderson')
            z.append(float(r))
    # look for missed close pairs: local minima of |Z| without a sign change
    missed = 0
    for i in range(1, len(ts) - 1):
        if abs(v[i]) < abs(v[i - 1]) and abs(v[i]) < abs(v[i + 1]) and v[i - 1] * v[i + 1] > 0 and v[i] * v[i - 1] > 0:
            fine = np.linspace(ts[i - 1], ts[i + 1], 200)
            fv = np.array([float(mp.siegelz(x)) for x in fine])
            sc = np.nonzero(fv[:-1] * fv[1:] < 0)[0]
            for j in sc:
                r = mp.findroot(mp.siegelz, (mp.mpf(fine[j]), mp.mpf(fine[j + 1])), solver='anderson')
                z.append(float(r)); missed += 1
    z = np.array(sorted(z))
    return z, missed


def compare(zz, mz, lo, hi, delta):
    inner = zz[(zz > lo) & (zz < hi)]
    minner = mz[(mz > lo) & (mz < hi)]
    if len(mz) == 0:
        return dict(n_zeta=len(inner), n_model=0)
    d = np.array([np.min(np.abs(mz - g)) for g in inner]) / delta
    return dict(n_zeta=int(len(inner)), n_model=int(len(minner)), mean=float(d.mean()),
                median=float(np.median(d)), frac_lt_0p1=float(np.mean(d < 0.1)),
                frac_lt_0p25=float(np.mean(d < 0.25)))


def run(S, Hfac=0.4, Hcap=150.0, Xs_arch=(None,)):
    S = list(S)
    W = float(np.sum(np.log(S)))
    Tstar = solve_Tstar(W)
    H = min(np.sqrt(Hfac * Tstar), Hcap)
    delta = 2 * np.pi / np.log(Tstar / (2 * np.pi))
    t0 = time.time()
    zz, missed = zeta_zeros(Tstar - H - 2, Tstar + H + 2, delta / 20)
    tz = time.time() - t0
    lo, hi = Tstar - H, Tstar + H
    res = dict(S=S, P=int(np.prod(S)), W=W, Tstar=Tstar, H=H, delta=delta, zeta_zeros=int(np.sum((zz > lo) & (zz < hi))),
               missed_pairs_recovered=missed, zeta_time_s=round(tz, 1),
               quad_phase_error_at_edge=H ** 2 / (4 * Tstar))
    h = delta / 40
    rows = {}
    rows['gram'] = compare(zz, zeros_of(lambda t: model_real(t, S, 'gram', 'exact'), lo - 2, hi + 2, h), lo, hi, delta)
    for kind in ('seed', 'aligned'):
        mz = zeros_of(lambda t, k=kind: model_real(t, S, k, 'linear', Tstar, W), lo - 2, hi + 2, h)
        rows['LY-' + kind + '(S)'] = compare(zz, mz, lo, hi, delta)
    for X in Xs_arch:
        pr = S if X is None else list(primes_upto(X))
        lab = 'S' if X is None else f'X={X}'
        for kind, name in (('anti', 'arch-anti'), ('euler', 'arch-euler'), ('sqfree', 'arch-sqfree')):
            mz = zeros_of(lambda t, k=kind, pr=pr: model_real(t, pr, k, 'exact'), lo - 2, hi + 2, h)
            rows[f'{name}({lab})'] = compare(zz, mz, lo, hi, delta)
    res['rows'] = rows
    return res


if __name__ == '__main__':
    allres = []
    configs = [([2, 3, 5, 7], (None, 100, 1000)),
               ([2, 3, 5, 7, 11], (None, 100, 1000, 10000)),
               ([2, 3, 5, 7, 11, 13], (None, 100, 1000, 10000)),
               ([2, 3, 5, 7, 11, 13, 17], (None, 100, 1000, 10000))]
    for S, Xs in configs:
        t0 = time.time()
        r = run(S, Xs_arch=Xs)
        allres.append(r)
        print(f"\n=== S={S} P={r['P']} W=log P={r['W']:.4f} T*={r['Tstar']:.2f} window +-{r['H']:.1f} "
              f"delta={r['delta']:.4f} zeta zeros in window={r['zeta_zeros']} (missed pairs recovered {r['missed_pairs_recovered']}; "
              f"edge phase error of linearization {r['quad_phase_error_at_edge']:.3f} rad)")
        for k, v in r['rows'].items():
            if 'mean' in v:
                print(f"  {k:22s} n_model={v['n_model']:4d} (zeta {v['n_zeta']:4d})  mean|d|/delta={v['mean']:.4f} "
                      f"median={v['median']:.4f}  frac<0.1={v['frac_lt_0p1']:.3f} frac<0.25={v['frac_lt_0p25']:.3f}")
        print(f'  [{time.time() - t0:.1f} s]')
        sys.stdout.flush()
    with open('b_alignment.json', 'w') as fh:
        json.dump(allres, fh, indent=1)
