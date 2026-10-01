# hurwitz_control.py — the lattice control L_rho(s) = 1 + sum_{k>=1} (1 + (k-1/2)/rho)^{-s}
#                                             = 1 + rho^s * zeta(s, 1/2 + rho)   (Hurwitz)
# (a) E_L = N_L - T in (-1/2, 1/2] on a grid; (b) real zero sigma*_L by bisection on (1-2rho, 1);
# (c) Theorem 1.6 floor L(s) >= 1/2 - rho/(1-s) on (0,1); (d) first-order law s0 + rho*L(s0), s0 = 1-rho;
# (e) the signed Euler factorization: L = prod (1 - lam^{-s})^{-m_lam}, m = (-1)^{k+1}(k-1)!/prod e_i!
#     (Moebius-corrected at perfect powers), checked against L at s = 3 and s = 2.5 by truncated products.
import mpmath as mp, math, sys, itertools
mp.mp.dps = 30
def L(s, rho): return 1 + rho**s * mp.zeta(s, mp.mpf(1)/2 + rho)
def zc(s, rho): return (s - 1 + rho) / (s - 1)
for name, rho in [("pi/16", mp.pi/16), ("pi/32", mp.pi/32), ("pi/64", mp.pi/64), ("pi/8", mp.pi/8)]:
    t = 1/rho
    # (a) E_L on a grid of 200000 points in [1, 1e5]
    emin, emax = 1.0, -1.0; r = float(rho); tt = float(t)
    for j in range(200000):
        x = 1 + j * 0.5 + 0.123456
        NL = 1 + max(0, math.floor((x - 1) * r + 0.5))
        e = NL - r * (x - 1) - 1; emin = min(emin, e); emax = max(emax, e)
    # (b) real zero
    lo, hi = 1 - 2*rho + mp.mpf('1e-6'), 1 - mp.mpf('1e-9')
    assert L(lo, rho) > 0 and L(hi, rho) < 0
    z = mp.findroot(lambda s: L(s, rho), (lo, hi), solver='bisect' if False else 'anderson')
    # (c) floor on a grid
    worst = min((L(mp.mpf(k)/1000, rho) - (mp.mpf(1)/2 - rho/(1 - mp.mpf(k)/1000))) for k in range(5, 1000, 5))
    s0 = 1 - rho
    print(f"{name}: rho={float(rho):.6f}  E_L range on grid [{emin:.4f},{emax:.4f}]  sigma*_L={mp.nstr(z,10)}"
          f"  1-rho={mp.nstr(s0,8)}  first-order {mp.nstr(s0 + rho*L(s0,rho),8)}  L(s0)={mp.nstr(L(s0,rho),6)}"
          f"  min[L-floor] on (0,1) grid={mp.nstr(worst,6)}  L(0)={mp.nstr(L(0,rho),8)}")
    sys.stdout.flush()
# (e) signed Euler factorization for rho = pi/16, truncated at Lam
rho = float(mp.pi/16); t = 1/rho; Lam = 400.0
lat = [1 + (k - 0.5)*t for k in range(1, int((Lam - 1)/t + 2)) if 1 + (k - 0.5)*t <= Lam]
elems = {}   # value -> exponent tuple (as dict index->e)
def rec(start, val, exps):
    for i in range(start, len(lat)):
        v = val * lat[i]
        if v > Lam: break
        e = dict(exps); e[i] = e.get(i, 0) + 1
        elems[round(v, 9)] = e; rec(i, v, e)
rec(0, 1.0, {})
def PiL(e):
    k = sum(e.values()); den = 1
    for x in e.values(): den *= math.factorial(x)
    return (-1)**(k + 1) * math.factorial(k - 1) / den
def mobius(n):
    r, p = 1, 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            if n % p == 0: return 0
            r = -r
        p += 1
    return -r if n > 1 else r
m = {}
for v, e in elems.items():
    g = 0
    for x in e.values(): g = math.gcd(g, x)
    tot = 0.0
    for j in range(1, g + 1):
        if g % j == 0: tot += mobius(j) * PiL({i: x // j for i, x in e.items()}) / j
    m[v] = round(tot); assert abs(tot - round(tot)) < 1e-9
from collections import Counter
byk = Counter(); vals = Counter()
for v, e in elems.items(): byk[(sum(e.values()), m[v])] += 1
print("rho=pi/16, Lam=400: #lattice pts", len(lat), " #semigroup elems", len(elems))
print("  (k = number of lattice factors, m) : count ->", sorted(byk.items()))
for s in (3.0, 2.5):
    prod = mp.mpf(1)
    for v in elems: prod *= (1 - mp.mpf(v)**(-s))**(-m[v])
    print(f"  s={s}: truncated signed Euler product {mp.nstr(prod,12)}  vs  L(s) {mp.nstr(L(s, mp.pi/16),12)}"
          f"  (truncation tail bound ~ sum_(lam>{Lam}) lam^-s ~ {Lam**(1-s)/(s-1)/t:.2e} for k=1 terms)")
