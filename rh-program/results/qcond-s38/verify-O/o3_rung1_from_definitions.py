"""o3 (read-O, qcond-s38): rung 1 (NOTE §3, verify/v3) recomputed FROM THE DEFINITIONS, exact integers, own route.

Genus 1 over F_5: L(u) = 1 - t u + 5 u^2, Z(u) = L(u)/((1-u)(1-5u)).
 * b_d (closed points of degree d) from the DEFINITION Z(u) = prod_d (1 - u^d)^{-b_d}: successive Euler factorization of
   the exact power series (b_d = coefficient of u^d after dividing out degrees < d) -- no Moebius inversion (v3 used it).
 * N_n two ways: N_n = sum_{d|n} d b_d (points over F_{5^n} from closed points) and N_n = 5^n + 1 - s_n (s_n = alpha^n + beta^n
   by the recursion s_n = t s_{n-1} - 5 s_{n-2}); they must agree.
 * F1: b_d >= 0 (d <= 60); F2: N_n >= 0 (n <= 60); F3: both roots of z^2 - t z + 5 in |z| <= 5 (exact: complex, or
   f(5) >= 0, f(-5) >= 0, |t|/2 <= 5); RH: t^2 <= 20.
 * Q-side transplant F_t = zeta(s) L(5^{-s}) (conductor 25): Q1 c(n) >= 0 (n <= 3000, by direct Dirichlet convolution);
   Q2 rho_q = sqrt25 * Res = 5 L(1/5) >= 1 (exact rational); Q3 Prop. E at p = 2: (5 - t)/2 >= (2/5) S(1/25), S(1/25) in (0, 1]
   (rational enclosure printed); Q4 Pi >= 0 on <5> <=> 1 - s_n >= 0 for all n (n <= 60).
"""
from fractions import Fraction as Fr

DMAX = 60

def mul(a, b, D=DMAX):
    out = [0]*(D + 1)
    for i, x in enumerate(a):
        if x == 0:
            continue
        for j in range(0, D + 1 - i):
            if b[j]:
                out[i + j] += x*b[j]
    return out

def binom_series(bexp, d, D=DMAX):
    """(1 - u^d)^bexp as an exact integer series to degree D (generalized binomial, any integer bexp)."""
    out = [0]*(D + 1)
    c = 1   # C(bexp, k) (-1)^k
    k = 0
    while k*d <= D:
        out[k*d] = c
        c = c*(bexp - k)*(-1)//(k + 1) if (c*(bexp - k)*(-1)) % (k + 1) == 0 else None
        assert c is not None
        k += 1
    return out

def closed_points(t):
    geo = [(5**(n + 1) - 1)//4 for n in range(DMAX + 1)]          # 1/((1-u)(1-5u))
    Z = mul([1, -t, 5] + [0]*(DMAX - 2), geo)
    G, b = Z[:], [None]*(DMAX + 1)
    for d in range(1, DMAX + 1):
        b[d] = G[d]
        G = mul(G, binom_series(b[d], d))                          # divide out (1 - u^d)^{-b_d}
        assert G[d] == 0
    assert all(x == 0 for x in G[1:]), "factorization incomplete"
    return b

def row(t):
    b = closed_points(t)
    s = [2, t]
    for n in range(2, DMAX + 1):
        s.append(t*s[-1] - 5*s[-2])
    N1 = [None] + [sum(d*b[d] for d in range(1, n + 1) if n % d == 0) for n in range(1, DMAX + 1)]
    N2 = [None] + [5**n + 1 - s[n] for n in range(1, DMAX + 1)]
    assert N1 == N2, t
    F1 = all(x >= 0 for x in b[1:]); F2 = all(x >= 0 for x in N1[1:])
    F3 = (t*t < 20) or (30 - 5*t >= 0 and 30 + 5*t >= 0 and abs(t) <= 10)
    RH = t*t <= 20
    ell = {1: 1, 5: -t, 25: 5}
    c = [None] + [sum(v for k, v in ell.items() if n % k == 0) for n in range(1, 3001)]
    Q1 = all(x >= 0 for x in c[1:])
    rho = 5*(1 - Fr(t, 5) + Fr(5, 25))
    Q2 = rho >= 1
    Q3 = Fr(5 - t, 2) >= Fr(2, 5)*S_upper and Fr(5 - t, 2) >= Fr(2, 5)*S_lower  # decided identically by both bounds
    Q3_undecided = (Fr(5 - t, 2) >= Fr(2, 5)*S_lower) != (Fr(5 - t, 2) >= Fr(2, 5)*S_upper)
    Q4 = all(1 - s[n] >= 0 for n in range(1, DMAX + 1))
    firstQ4 = next((n for n in range(1, DMAX + 1) if 1 - s[n] < 0), None)
    return dict(t=t, RH=RH, F1=F1, F2=F2, F3=F3, Q1=Q1, Q2=Q2, Q3=Q3, Q3u=Q3_undecided, Q4=Q4, fQ4=firstQ4,
                minb=min(b[1:]), b=b[1:7], N=N1[1:7], rho=rho)

# rational enclosure of S(1/25) = (sin x / x)^2, x = pi/25:  1 - x^2/6 < sin x / x < 1 - x^2/6 + x^4/120
PI_LO, PI_HI = Fr(314159, 100000), Fr(314160, 100000)
xl, xh = PI_LO/25, PI_HI/25
S_lower = (1 - xh**2/6)**2
S_upper = (1 - xl**2/6 + xl**4/120)**2

if __name__ == "__main__":
    print(__doc__.strip().splitlines()[0])
    print(f"S(1/25) in [{float(S_lower):.8f}, {float(S_upper):.8f}] (rational enclosure)")
    yn = lambda v: "Y" if v else "-"
    print("  t | RH F1 F2 F3 | Q1 Q2 Q3 Q4(first bad n) | rho_q | min b_d | b_1..b_6 | N_1..N_6")
    rows = [row(t) for t in range(-12, 13)]
    for r in rows:
        print(f"{r['t']:3d} |  {yn(r['RH'])}  {yn(r['F1'])}  {yn(r['F2'])}  {yn(r['F3'])} |  {yn(r['Q1'])}  {yn(r['Q2'])}  {yn(r['Q3'])}{'?' if r['Q3u'] else ''}  {yn(r['Q4'])}({r['fQ4']}) | {str(r['rho']):>4} | {r['minb'] if abs(r['minb']) < 10**9 else '%.3e' % r['minb']} | {r['b']} | {r['N']}")
    for k in ("RH", "F1", "F2", "F3", "Q1", "Q2", "Q3", "Q4"):
        print(f"{k}: t in {[r['t'] for r in rows if r[k]]}")
    print("F1 and not RH:", [r['t'] for r in rows if r['F1'] and not r['RH']])
    v = [r for r in rows if r['t'] == 5][0]
    print(f"virtual curve t=5: N_1..N_6 = {v['N']}, b_1..b_6 = {v['b']} (BFE §9: 1,11,76,451,2501,13376 / 1,5,25,110,500,2215)")
    w = [r for r in rows if r['t'] == -5][0]
    print(f"t=-5 (the L-polynomial of F_(5,5)): Q4 first failure n = {w['fQ4']} -> Pi(25) = (1 - s_2)/2 = {Fr(1 - (25 - 10), 2)}")
