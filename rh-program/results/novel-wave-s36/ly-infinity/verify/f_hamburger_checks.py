"""f_hamburger_checks.py -- the orchestrator's addendum: Hamburger's theorem as an acceptance test.

Hamburger (as stated by Burnol, arXiv:1106.4749v2 p.2): f meromorphic on C of finite order (hence
finitely many poles), f = sum a_n n^{-s} absolutely convergent for Re s > 1, and g(s) = chi(s) f(1-s)
a convergent Dirichlet series sum b_n n^{-s} for Re s >> 1  ==>  f = c * zeta.
chi(s) = pi^{s-1/2} Gamma((1-s)/2)/Gamma(s/2);  Riemann's FE: f(s) = chi(s) f(1-s).

(1) RH-FALSE control for the test (Nakamura, arXiv:2008.02570v4, abstract): for an even primitive
    character chi mod q,  f(s,chi) = q^s L(s,chi) + G(chi) L(s, conj chi)  satisfies Riemann's FE,
    and has infinitely many zeros off the line when chi is non-real.  Here q = 7, chi cubic
    (3 is a primitive root mod 7; chi(3) = e^{2 pi i/3}; chi(-1) = chi(6) = 1, even, non-real).
    We (a) check Riemann's FE numerically, (b) locate zeros with Re s != 1/2, (c) note the support:
    q^s L(s,chi) = sum chi(n) (n/q)^{-s} has frequencies log(n/q), NOT in log N  (hypothesis (i) fails).
(2) The finite models against (i)-(iii):
    (a) Lee-Yang f_S(s) = E(s) + eps P^{1/2-s} E(1-s), E = prod_{p in S}(1 + p^{-s}): integer-lattice
        Dirichlet polynomial (i: yes), entire of order 1 (iii: yes), its own FE with conductor P and
        NO Gamma factor holds, Riemann's FE fails (ii: no)  -- measured.
    (b) archimedean analytic F(s) = A(s) + chi(s) A(1-s), A = prod(1 + p^{-s}): Riemann's FE holds
        exactly (ii: yes); F is not a Dirichlet series (i: no); F has poles at s = 3, 5, 7, ...
        because A(1-s) does not vanish at s = 3, 5, ... (no 'trivial zeros'), so (iii) fails:
        infinitely many poles (Knopp's abundance regime) -- measured at s = 3 + eps.
"""
import mpmath as mp, numpy as np, time

mp.mp.dps = 30


def chi_fe(s):
    return mp.power(mp.pi, s - mp.mpf(1) / 2) * mp.gamma((1 - s) / 2) / mp.gamma(s / 2)


q = 7
w = mp.exp(2j * mp.pi / 3)
chi = [0, 1, w ** 2, w, w, w ** 2, 1]          # chi(0..6): chi(1)=1, chi(3)=w, chi(2)=w^2, chi(6)=1, chi(4)=w, chi(5)=w^2
chib = [mp.conj(x) for x in chi]
G = mp.fsum(chi[r] * mp.exp(2j * mp.pi * r / q) for r in range(1, q))


def fN(s):
    return mp.power(q, s) * mp.dirichlet(s, chi) + G * mp.dirichlet(s, chib)


def main():
    t0 = time.time()
    print('== (1) Nakamura control: q = 7, cubic even character ==')
    print('chi(1..6) =', [mp.nstr(x, 6) for x in chi[1:]], '  chi(-1) = chi(6) =', chi[6])
    print('G(chi) =', mp.nstr(G, 15), ' |G|^2 =', mp.nstr(abs(G) ** 2, 15), '(should be 7)')
    worst = 0
    for s in (mp.mpc(0.3, 7.1), mp.mpc(0.8, 21.3), mp.mpc(-0.4, 3.3), mp.mpc(1.7, 13.9)):
        a = fN(s); b = chi_fe(s) * fN(1 - s)
        rel = abs(a - b) / abs(a)
        worst = max(worst, rel)
        print(f'  s = {mp.nstr(s, 5)}: f(s) = {mp.nstr(a, 10)}   chi(s) f(1-s) = {mp.nstr(b, 10)}   rel diff {mp.nstr(rel, 3)}')
    print('  Riemann FE f(s) = chi(s) f(1-s): worst relative residual =', mp.nstr(worst, 3))
    # zeros off the line
    found = []
    for sg in (0.6, 0.8, 1.0, 1.2, 1.4):
        for tt in np.linspace(0.5, 40, 80):
            try:
                z = mp.findroot(fN, mp.mpc(sg, tt))
            except Exception:
                continue
            if abs(fN(z)) < 1e-20 and abs(z.real - 0.5) > 1e-6 and -2 < z.real < 3 and 0 < z.imag < 45:
                if not any(abs(z - v) < 1e-8 for v in found):
                    found.append(z)
    found.sort(key=lambda z: z.imag)
    print(f'  zeros with Re s != 1/2 (0 < t < 45): {len(found)}')
    for z in found[:12]:
        print(f'    {mp.nstr(z.real, 12)} + {mp.nstr(z.imag, 12)} i   |f| = {mp.nstr(abs(fN(z)), 3)}   '
              f'partner 1-conj: |f(1 - conj z)| = {mp.nstr(abs(fN(1 - mp.conj(z))), 3)}')
    # on-line zeros count for reference
    print('  support: q^s L(s,chi) = sum chi(n) (n/7)^(-s): frequencies log(n/7) (n = 1..6 give NEGATIVE log) -> not in log N')

    print('\n== (2a) Lee-Yang finite model f_S = E(s) + eps P^{1/2-s} E(1-s), E = prod(1 + p^{-s}), S = {2,3,5,7} ==')
    S = [2, 3, 5, 7]; P = 210; eps = mp.exp(0.7j)
    E = lambda s: mp.fprod(1 + mp.power(p, -s) for p in S)
    Estar = lambda s: mp.conj(E(mp.conj(s)))
    fS = lambda s: E(s) + eps * mp.power(P, mp.mpf(1) / 2 - s) * Estar(1 - s)
    for s in (mp.mpc(0.3, 7.1), mp.mpc(0.9, 21.3)):
        own = fS(s) - eps * mp.power(P, mp.mpf(1) / 2 - s) * mp.conj(fS(1 - mp.conj(s)))
        riem = fS(s) - chi_fe(s) * mp.conj(fS(1 - mp.conj(s)))
        print(f'  s={mp.nstr(s, 4)}: own FE (conductor P, no Gamma) residual {mp.nstr(abs(own) / abs(fS(s)), 3)};'
              f'  Riemann FE residual {mp.nstr(abs(riem) / abs(fS(s)), 3)}')
    print('  (i) integer lattice: yes (divisors of 210); (iii) entire, order 1: yes; (ii) Riemann FE: NO')

    print('\n== (2b) archimedean analytic model F(s) = A(s) + chi(s) A(1-s), A = prod_{p<=7}(1 + p^{-s}) ==')
    A = lambda s: mp.fprod(1 + mp.power(p, -s) for p in S)
    F = lambda s: A(s) + chi_fe(s) * A(1 - s)
    for s in (mp.mpc(0.3, 7.1), mp.mpc(0.9, 21.3)):
        print(f'  s={mp.nstr(s, 4)}: Riemann FE residual |F(s) - chi(s)F(1-s)|/|F| = {mp.nstr(abs(F(s) - chi_fe(s) * F(1 - s)) / abs(F(s)), 3)}')
    for k in (3, 5, 7):
        for e in (mp.mpf('1e-3'), mp.mpf('1e-6')):
            print(f'  |F({k} + {mp.nstr(e, 2)})| = {mp.nstr(abs(F(k + e)), 6)}   (A(1-{k}) = A({1-k}) = {mp.nstr(A(1 - k), 8)} != 0 -> pole of chi survives)')
    print('  zeta, by contrast: zeta(1-k) = 0 for k = 3, 5, 7 (trivial zeros) cancel the poles of chi.')
    print('  => (ii) yes, (i) no, (iii) no (infinitely many poles at s = 3, 5, 7, ...).')
    print(f'\nelapsed {time.time() - t0:.1f} s')


if __name__ == '__main__':
    main()
