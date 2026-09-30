"""b3_arch_realrootedness.py -- does real-rootedness survive the archimedean phase?

Model:  F(s) = A(s) + chi(s) A(1-s),   chi(s) = pi^{s-1/2} Gamma((1-s)/2)/Gamma(s/2),
so that on s = 1/2+it:  F = 2 e^{-i theta(t)} Re( e^{i theta(t)} A(1/2+it) ).
A in {euler: prod_{p<=X}(1-p^{-s})^{-1},  sqfree: prod(1+p^{-s}),  anti: prod(1-p^{-s})}.
Lee-Yang control:  F_LY(s) = A(s) + eps P^{1/2-s} A(1-s)  (A = prod_{p in S}(1+p^{-s})), |eps| = 1,
which has ALL zeros on the line (theorem) -- the counting code must return 0 off-line zeros.

For each (model, X, window [T-H, T+H]):
  N_line  = # sign changes of Re(e^{i theta} A) on the line (simple zeros on the line)
  N_box   = # zeros of F in the box |sigma - 1/2| < a, T-H < t < T+H (argument principle,
            adaptive boundary walk; poles of the euler model sit at sigma = 0 and 1, outside the box)
  N_off   = N_box - N_line  (zeros off the line inside the box)
  min phi' where phi(t) = theta(t) + arg A(1/2+it)  (phi' < 0 somewhere is the mechanism
            that ejects zeros from the line: F/2e^{-i theta} = |A| cos(phi))
Also: explicit dipole zeros of the euler model near s0 = 1 + 2 pi i k / log p (outside the box).
"""
import numpy as np, mpmath as mp, sys, time, json
from scipy.special import loggamma

LOGPI = np.log(np.pi)


def primes_upto(n):
    s = np.ones(n + 1, bool); s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return np.nonzero(s)[0]


def logchi(s):
    return (s - 0.5) * LOGPI + loggamma((1 - s) / 2) - loggamma(s / 2)


def logA(s, primes, kind):
    s = np.asarray(s, complex)
    out = np.zeros(s.shape, complex)
    for p in primes:
        w = np.exp(-s * np.log(p))
        if kind == 'euler':
            out -= np.log(1 - w)
        elif kind in ('sqfree', 'LY'):
            out += np.log(1 + w)
        elif kind == 'anti':
            out += np.log(1 - w)
    return out


def F_model(s, primes, kind, eps=None):
    s = np.asarray(s, complex)
    la, lb = logA(s, primes, kind), logA(1 - s, primes, kind)
    if kind == 'LY':
        P = float(np.prod(primes))
        return np.exp(la) + eps * np.exp((0.5 - s) * np.log(P) + lb)
    return np.exp(la) + np.exp(logchi(s) + lb)


def theta_np(t):
    t = np.asarray(t, float)
    return (t / 2) * np.log(t / (2 * np.pi)) - t / 2 - np.pi / 8 + 1 / (48 * t) + 7 / (5760 * t ** 3)


def line_real(t, primes, kind, eps=None):
    s = 0.5 + 1j * np.asarray(t, float)
    Fv = F_model(s, primes, kind, eps)
    if kind == 'LY':
        P = float(np.prod(primes))
        ph = np.exp(1j * np.asarray(t) * np.log(P) / 2) / np.sqrt(eps)
        return np.real(ph * Fv), np.imag(ph * Fv)
    ph = np.exp(1j * theta_np(t))
    return np.real(ph * Fv), np.imag(ph * Fv)


def count_line_zeros(primes, kind, lo, hi, h, eps=None):
    ts = np.arange(lo, hi + h, h)
    re, im = line_real(ts, primes, kind, eps)
    return int(np.sum(re[:-1] * re[1:] < 0)), float(np.max(np.abs(im)) / (np.max(np.abs(re)) + 1e-300))


def arg_walk(f, z0, z1, max_step):
    """accumulated change of arg f along the segment z0->z1 with adaptive refinement"""
    n = max(8, int(abs(z1 - z0) / max_step) + 1)
    zs = z0 + (z1 - z0) * np.linspace(0, 1, n + 1)
    v = f(zs)
    d = np.angle(v[1:] / v[:-1])
    total = 0.0
    bad = np.nonzero(np.abs(d) > np.pi / 3)[0]
    good = np.ones(len(d), bool); good[bad] = False
    total += d[good].sum()
    for i in bad:  # refine this sub-segment
        total += arg_walk(f, zs[i], zs[i + 1], abs(zs[i + 1] - zs[i]) / 16)
    return total


def count_box(primes, kind, lo, hi, a, step, eps=None):
    f = lambda z: F_model(z, primes, kind, eps)
    c = [0.5 - a + 1j * lo, 0.5 + a + 1j * lo, 0.5 + a + 1j * hi, 0.5 - a + 1j * hi]
    tot = 0.0
    for k in range(4):
        tot += arg_walk(f, c[k], c[(k + 1) % 4], step)
    return tot / (2 * np.pi)


def phase_deriv_min(primes, kind, lo, hi, h):
    t = np.arange(lo, hi + h, h)
    s = 0.5 + 1j * t
    # d/dt arg A(1/2+it) = Re(A'/A)(s)
    der = np.zeros(t.shape)
    for p in primes:
        lp = np.log(p); w = np.exp(-s * lp)
        if kind == 'euler':
            der += np.real(-lp * w / (1 - w))
        elif kind == 'sqfree':
            der += np.real(-lp * w / (1 + w))
        elif kind == 'anti':
            der += np.real(lp * w / (1 - w))
    thp = 0.5 * np.log(t / (2 * np.pi))
    phi_p = thp + der
    return float(phi_p.min()), float(np.mean(phi_p < 0))


def dipole(primes, p, k):
    """zero of the euler model near s0 = 1 + 2 pi i k/log p (pole of A(1-s) at s0)"""
    mp.mp.dps = 30
    prs = [int(q) for q in primes]

    def Fm(s):
        A = mp.mpf(1); B = mp.mpf(1)
        for q in prs:
            A /= (1 - mp.power(q, -s)); B /= (1 - mp.power(q, -(1 - s)))
        chi = mp.power(mp.pi, s - mp.mpf(1) / 2) * mp.gamma((1 - s) / 2) / mp.gamma(s / 2)
        return A + chi * B
    s0 = 1 + 2j * mp.pi * k / mp.log(p)
    # predicted offset: F ~ A(s0) + chi(s0) R/(s-s0), R = residue of A(1-s) at s0
    Arest = mp.mpf(1)
    for q in prs:
        if q != p:
            Arest /= (1 - mp.power(q, -(1 - s0)))
    R = Arest / mp.log(p)   # (1-p^{s-1})^{-1} ~ -1/((s-s0) log p) ... sign absorbed below
    A0 = mp.mpf(1)
    for q in prs:
        A0 /= (1 - mp.power(q, -s0))
    chi0 = mp.power(mp.pi, s0 - mp.mpf(1) / 2) * mp.gamma((1 - s0) / 2) / mp.gamma(s0 / 2)
    guess = s0 + chi0 * R / A0
    try:
        z = mp.findroot(Fm, guess)
        return complex(s0), complex(z), float(abs(Fm(z))), float(abs(chi0))
    except Exception as e:
        return complex(s0), None, None, float(abs(chi0))


def main():
    res = []
    windows = [(1319.47, 23.0), (14514.4, 40.0), (188680.0, 40.0)]
    print('== Lee-Yang control (must give N_off = 0) ==')
    for S, (T, H) in (([2, 3, 5, 7], windows[0]), ([2, 3, 5, 7, 11], windows[1])):
        eps = np.exp(1j * 0.7)
        h = 2 * np.pi / np.log(np.prod(S)) / 60
        nl, imrat = count_line_zeros(S, 'LY', T - H, T + H, h, eps)
        for a in (0.2, 0.45):
            nb = count_box(S, 'LY', T - H, T + H, a, h, eps)
            print(f'LY S={S} T={T} H={H} a={a}: N_line={nl} N_box={nb:.4f} N_off={nb - nl:.4f} (Im/Re residual {imrat:.1e})')
            res.append(dict(model='LY', S=S, T=T, H=H, a=a, N_line=nl, N_box=nb))
    print('\n== Archimedean-phase models ==')
    for (T, H) in windows:
        delta = 2 * np.pi / np.log(T / (2 * np.pi))
        h = delta / 60
        for kind in ('euler', 'sqfree', 'anti'):
            for X in (7, 13, 30, 100, 1000):
                pr = primes_upto(X)
                t0 = time.time()
                nl, imrat = count_line_zeros(pr, kind, T - H, T + H, h)
                mphi, frac = phase_deriv_min(pr, kind, T - H, T + H, h / 4)
                row = dict(model=kind, X=X, T=T, H=H, N_line=nl, min_phi_prime=mphi, frac_neg=frac)
                for a in (0.2, 0.45):
                    nb = count_box(pr, kind, T - H, T + H, a, h)
                    row[f'N_box_a{a}'] = nb
                res.append(row)
                print(f"T={T:9.1f} {kind:6s} X={X:5d}: N_line={nl:4d}  N_box(a=.2)={row['N_box_a0.2']:8.3f}  "
                      f"N_box(a=.45)={row['N_box_a0.45']:8.3f}  off(.45)={row['N_box_a0.45'] - nl:7.3f}  "
                      f"min phi'={mphi:8.3f}  frac(phi'<0)={frac:.4f}  theta'={0.5*np.log(T/(2*np.pi)):.3f} "
                      f"sum_p logp/sqrtp={np.sum(np.log(pr)/np.sqrt(pr)):.3f}  [{time.time()-t0:.1f}s]")
                sys.stdout.flush()
    print('\n== euler-model dipole zeros near s0 = 1 + 2 pi i k/log p (outside the strip box) ==')
    for X in (7, 30):
        pr = primes_upto(X)
        for p, k in ((2, 150), (3, 1000), (5, 2000)):
            s0, z, fz, chi0 = dipole(pr, p, k)
            print(f'X={X} p={p} k={k}: s0={s0:.6f}  zero={z}  |F(zero)|={fz}  |chi(s0)|={chi0:.3e}')
    with open('b3_arch_realrootedness.json', 'w') as fh:
        json.dump(res, fh, indent=1, default=str)


if __name__ == '__main__':
    t0 = time.time()
    main()
    print(f'elapsed {time.time() - t0:.1f} s')
