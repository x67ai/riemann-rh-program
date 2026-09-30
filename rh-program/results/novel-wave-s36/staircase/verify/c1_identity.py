"""
c1_identity.py -- unit 1 of seed N2 (staircase).

Checks, at high precision and at several complex s, Riemann's incomplete-gamma identity

    Lambda(s) := pi^{-s/2} Gamma(s/2) zeta(s) = -1/s - 1/(1-s) + sum_{n>=1} g_n(s),
    g_n(s) = (pi n^2)^{-s/2} Gamma(s/2, pi n^2) + (pi n^2)^{-(1-s)/2} Gamma((1-s)/2, pi n^2),

(Gamma(a, x) = upper incomplete gamma = int_x^inf u^{a-1} e^{-u} du), and its xi-form

    xi(s) = (1/2) s (s-1) Lambda(s) = 1/2 + (1/2) s (s-1) sum_n g_n(s).

Independent cross-checks:
  (i) the identity at two working precisions (60 and 90 digits) -- agreement of the two runs;
  (ii) Gamma(a, x) from mpmath.gammainc against direct numerical quadrature of int_x^inf u^{a-1} e^{-u} du
      at one complex a (catches a wrong-branch or wrong-convention gammainc);
  (iii) the derivation of the identity is re-done in NOTE.md (split of the Mellin integral at x = 1 and
      the theta relation psi(1/x) = sqrt(x) psi(x) + (sqrt(x) - 1)/2).
Also computes the constant c_N = 1/2 + sum_{n<=N} (1 - 4 pi n^2) e^{-pi n^2} (predicted limit of xi_N on the
critical line as |t| -> infinity) and checks c_infinity = 0 (the theta identity 4 psi'(1) + psi(1) = -1/2).
"""
import sys
import mpmath as mp


def g_n(s, n):
    x = mp.pi * n * n
    return x**(-s/2) * mp.gammainc(s/2, x) + x**(-(1 - s)/2) * mp.gammainc((1 - s)/2, x)


def Lambda_exact(s):
    return mp.pi**(-s/2) * mp.gamma(s/2) * mp.zeta(s)


def Lambda_series(s, nmax):
    return -1/s - 1/(1 - s) + mp.fsum(g_n(s, n) for n in range(1, nmax + 1))


def run(dps):
    mp.mp.dps = dps
    pts = [mp.mpc(2, 3), mp.mpc('0.3', 7), mp.mpc('0.5', '14.134725141734693790457'),
           mp.mpc('-1.5', 2), mp.mpc(5, -11), mp.mpc('0.8', 30), mp.mpc('0.5', 60),
           mp.mpc(12, 25), mp.mpc('-7.25', '40.5')]
    # nmax: need e^{-pi n^2} * (growth) below 10^{-dps-10}
    nmax = int(mp.sqrt((dps + 15) * mp.log(10) / mp.pi)) + 3
    out = []
    for s in pts:
        a = Lambda_exact(s)
        b = Lambda_series(s, nmax)
        rel = abs(a - b) / abs(a)
        xi_a = s*(s - 1)/2 * a
        xi_b = mp.mpf(1)/2 + s*(s - 1)/2 * (b + 1/s + 1/(1 - s))
        out.append((s, a, b, rel, xi_a, xi_b))
    return nmax, out


if __name__ == '__main__':
    res = {}
    for dps in (60, 90):
        nmax, out = run(dps)
        res[dps] = out
        print(f'=== dps = {dps}, terms n <= {nmax} ===')
        for (s, a, b, rel, xa, xb) in out:
            print(f's = {mp.nstr(s, 12)}')
            print(f'   Lambda (zeta)  = {mp.nstr(a, 30)}')
            print(f'   Lambda (series)= {mp.nstr(b, 30)}')
            print(f'   rel. diff      = {mp.nstr(rel, 5)}   |  xi = {mp.nstr(xa, 20)}')
    mp.mp.dps = 60
    print('=== cross-precision agreement of the series (dps 60 vs 90) ===')
    for (r60, r90) in zip(res[60], res[90]):
        print(f's = {mp.nstr(r60[0], 10)}: |S60 - S90|/|S90| = {mp.nstr(abs(r60[2] - r90[2])/abs(r90[2]), 5)}')
    # (ii) gammainc vs quadrature at a complex a
    mp.mp.dps = 40
    a = mp.mpc('0.25', '7.0')
    x = mp.pi
    q = mp.quad(lambda u: u**(a - 1) * mp.exp(-u), [x, x + 5, x + 20, x + 60, mp.inf])
    gi = mp.gammainc(a, x)
    print('=== gammainc vs quadrature, a = 0.25+7i, x = pi ===')
    print('gammainc  =', mp.nstr(gi, 30))
    print('quadrature=', mp.nstr(q, 30))
    print('rel diff  =', mp.nstr(abs(gi - q)/abs(q), 5))
    # c_N constants
    mp.mp.dps = 50
    print('=== c_N = 1/2 + sum_{n<=N} (1 - 4 pi n^2) e^{-pi n^2} ===')
    for N in range(1, 9):
        cN = mp.mpf(1)/2 + mp.fsum((1 - 4*mp.pi*n*n) * mp.exp(-mp.pi*n*n) for n in range(1, N + 1))
        tail = mp.fsum((4*mp.pi*n*n - 1) * mp.exp(-mp.pi*n*n) for n in range(N + 1, N + 40))
        print(f'N = {N}: c_N = {mp.nstr(cN, 20)}   (tail sum_(n>N) (4 pi n^2 - 1) e^(-pi n^2) = {mp.nstr(tail, 20)})')
    cinf = mp.mpf(1)/2 + mp.fsum((1 - 4*mp.pi*n*n) * mp.exp(-mp.pi*n*n) for n in range(1, 60))
    print('c_infinity (n <= 59) =', mp.nstr(cinf, 10))
