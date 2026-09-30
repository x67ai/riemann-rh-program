"""DD1: sign of Lambda_F(n) (coefficients of -F'/F) for Epstein zetas of class-number > 1
forms, against Euler-product controls (x^2+y^2, x^2+xy+2y^2, zeta_K for K = Q(sqrt-5)) and the
RH-false controls DH and F_{2.9,2}.  Lambda_F is defined by a(n) log n = sum_{d|n} Lambda_F(d) a(n/d),
a(1) = 1 (normalized Dirichlet coefficients).  Positive-Lambda + FE is the axiom set of T6/T10/T18/T35.
"""
import math, sys, time
import numpy as np

N = int(sys.argv[1]) if len(sys.argv) > 1 else 200000


def reps(A, B, C, N):
    """r_Q(n), n <= N, for Q = A x^2 + B x y + C y^2 positive definite."""
    D = 4 * A * C - B * B
    r = np.zeros(N + 1, dtype=np.int64)
    ymax = int(math.isqrt(4 * A * N // D)) + 1
    xmax = int(math.isqrt(N // A)) + abs(B) * ymax + 2
    x = np.arange(-xmax, xmax + 1, dtype=np.int64)
    for y in range(-ymax, ymax + 1):
        q = A * x * x + B * x * y + C * y * y
        q = q[(q >= 1) & (q <= N)]
        np.add.at(r, q, 1)
    return r


def lam_from_coeffs(a, N):
    """Lambda(n) from normalized coefficients a (a[1] = 1)."""
    lam = np.zeros(N + 1)
    acc = np.zeros(N + 1)
    logs = np.log(np.arange(1, N + 2, dtype=float))[:N + 1]  # logs[n] = log(n+1): fix below
    logn = np.zeros(N + 1)
    logn[1:] = np.log(np.arange(1, N + 1, dtype=float))
    for n in range(2, N + 1):
        v = a[n] * logn[n] - acc[n]
        lam[n] = v
        if v != 0.0 and 2 * n <= N:
            kmax = N // n
            acc[2 * n::n][:kmax - 1] += v * a[2:kmax + 1]
    return lam


def prime_power_mask(N):
    sieve = np.ones(N + 1, dtype=bool); sieve[:2] = False
    for p in range(2, math.isqrt(N) + 1):
        if sieve[p]:
            sieve[p * p::p] = False
    mask = np.zeros(N + 1, dtype=bool)
    for p in np.nonzero(sieve)[0]:
        q = int(p)
        while q <= N:
            mask[q] = True; q *= p
    return mask


def report(name, a, N, ppmask):
    t0 = time.time()
    lam = lam_from_coeffs(a, N)
    n = np.arange(N + 1)
    logn = np.zeros(N + 1); logn[2:] = np.log(n[2:])
    rel = np.zeros(N + 1); rel[2:] = lam[2:] / logn[2:]
    neg = np.nonzero(rel[2:] < -1e-7)[0] + 2
    off = np.abs(rel[2:])[~ppmask[2:]]
    print(f"== {name}: N={N}  time {time.time()-t0:.1f}s")
    print(f"   #n with Lambda(n) < 0: {len(neg)};  first ones: {[(int(k), round(float(rel[k]), 6)) for k in neg[:8]]}")
    if len(neg):
        k = int(np.argmin(rel[2:]) + 2)
        print(f"   most negative Lambda(n)/log n = {rel[k]:.6g} at n = {k}")
    print(f"   max |Lambda(n)/log n| off prime powers = {off.max():.3g};  on prime powers min = {rel[2:][ppmask[2:]].min():.6g}")
    return rel


if __name__ == '__main__':
    pp = prime_power_mask(N)
    forms = {
        'x^2+y^2 (h=1, control: 4 zeta L(chi_-4))': (1, 0, 1),
        'x^2+xy+2y^2 (h=1, control: disc -7)': (1, 1, 2),
        'x^2+5y^2 (h=2, disc -20)': (1, 0, 5),
        'x^2+6y^2 (h=2, disc -24)': (1, 0, 6),
        'x^2+xy+6y^2 (h=3, disc -23)': (1, 1, 6),
        'x^2+14y^2 (h=4, disc -56)': (1, 0, 14),
    }
    R = {}
    for name, (A, B, C) in forms.items():
        r = reps(A, B, C, N)
        R[(A, B, C)] = r
        report(name, r / r[1], N, pp)
    # zeta_K, K = Q(sqrt -5): (r_{x^2+5y^2} + r_{2x^2+2xy+3y^2}) / w, w = 2
    rK = R[(1, 0, 5)] + reps(2, 2, 3, N)
    report('zeta_K, K=Q(sqrt-5) (Euler product control)', rK / rK[1], N, pp)
    # DH: a_n = (1, kappa, -kappa, -1, 0) mod 5
    s5 = math.sqrt(5.0)
    kap = (math.sqrt(10 - 2 * s5) - 2) / (s5 - 1)
    per = np.array([0.0, 1.0, kap, -kap, -1.0])  # index n mod 5
    aDH = per[np.arange(N + 1) % 5]; aDH[0] = 0
    report(f'Davenport-Heilbronn (kappa={kap:.10f})', aDH, N, pp)
    # F_{2.9,2} = zeta * (1 + 2.9 * 2^-s + 2 * 4^-s)
    n = np.arange(N + 1)
    aF = 1.0 + 2.9 * (n % 2 == 0) + 2.0 * (n % 4 == 0); aF[0] = 0
    report('F_{2.9,2}', aF, N, pp)
