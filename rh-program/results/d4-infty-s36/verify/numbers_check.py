# d4-infty-s36 — writer's independent numbers check (Session 36, 2026-09-30).
# Written from scratch; prederivation/pre_check.py was read but NOT reused.
# Python 3 + numpy + sympy + mpmath.  Run:  python3 numbers_check.py > numbers-check.log 2>&1
# Sections (cited in NOTE.md as [k]):
#  [1]  Theorem S(a): closed form sup L = (1+2g)(1+r_g) against brute force; the prime threshold at kappa = 1
#  [2]  Theorem S(b): the canonical-class form — bound L0(g,k,alpha,beta), the product case recovers [1]; sympy identity
#  [3]  degree clause: first n violating (1+n-Lambda(n)/kappa)^2 <= 4 g^2 n; thresholds at n = 6, 210, 2^k; number-ring weights
#  [4]  the (c-K) Gram model: index one on span(C1,C2,Delta,graphs) with the degree clause, non-product adjunction; K_Y cannot join
#  [5]  rung 1 (positive control): closed points by degree, (H-inj2) fails at every closed point; Weil's inequality
#  [6]  Proposition A toy: 0/1 sequences obeying a monic recurrence are eventually periodic; the base-1 coefficient
#  [7]  Chebyshev: theta(x) >= c x on [2, X] (numeric) and the analytic lower bound beyond
#  [8]  Proposition B: the greedy regradings (d, kappa) = (2,1), (2,log 2), (3,1), (3,1/2); blocks, eps_N, e_N, Lemma B.1, Toeplitz
#  [9]  Proposition C: the explicit formula tested against a Gaussian (kappa = 1 cancels, kappa != 1 does not); the smeared
#       diagonal's defect counts zeros (def(Delta_eps) against N(1/eps)); CC (13) archimedean density = x-18 (2)'s
import math, sys, time, itertools
import numpy as np
import sympy as sp
import mpmath as mp

T0 = time.time()
def hdr(s):
    print('\n' + '=' * 100 + '\n' + s + '\n' + '=' * 100, flush=True)

def vonmangoldt(n):
    f = sp.factorint(n)
    return math.log(next(iter(f))) if len(f) == 1 else 0.0

# ------------------------------------------------------------------------------------------------
hdr('[1] Theorem S(a): sup{L : (1+x-L)^2 <= 4g^2 x and (1+x^2-L)^2 <= 4g^2 x^2} against (1+2g)(1+r_g)')
def feasible_interval(g, x):
    """L-interval allowed at fiber degree x >= 0 by the two Cauchy-Schwarz inequalities."""
    lo = max(1 + x - 2*g*math.sqrt(x), 1 + x*x - 2*g*x)
    hi = min(1 + x + 2*g*math.sqrt(x), 1 + x*x + 2*g*x)
    return lo, hi
for g in [0.0, 0.25, 0.5, 1.0, 1.5, 2.0, 5.0, 10.0, 50.0]:
    r = (1 + math.sqrt(1 + 8*g)) / 2
    closed = (1 + 2*g) * (1 + r)
    # brute force 1: dense grid in x (independent of the derivation)
    xs = np.concatenate([np.linspace(0, 3*r*r + 3, 600001), [r*r]])
    lo = np.maximum(1 + xs - 2*g*np.sqrt(xs), 1 + xs**2 - 2*g*xs)
    hi = np.minimum(1 + xs + 2*g*np.sqrt(xs), 1 + xs**2 + 2*g*xs)
    ok = hi >= lo - 1e-12
    sup_grid = hi[ok].max(); xarg = xs[ok][np.argmax(hi[ok])]
    # brute force 2: random search in (x, L)
    rng = np.random.default_rng(1)
    X = rng.uniform(0, 3*r*r + 3, 2_000_000); Lr = rng.uniform(0, closed*1.2 + 3, 2_000_000)
    feas = ((1 + X - Lr)**2 <= 4*g*g*X + 1e-12) & ((1 + X*X - Lr)**2 <= 4*g*g*X*X + 1e-12)
    sup_rand = Lr[feas].max() if feas.any() else float('nan')
    print(f'  g={g:6.2f}  r_g={r:9.6f}  r_g^2-r_g-2g={r*r-r-2*g:+.1e}  closed (1+2g)(1+r_g)={closed:12.6f}  grid sup={sup_grid:12.6f} at x={xarg:10.5f} (r_g^2={r*r:10.5f})  random sup={sup_rand:12.6f}')
g0 = 0.0
print('  g = 0 case: both inequalities are equalities, L = 1+x = 1+x^2, x in {0,1}, L in {1,2}; feasible_interval(0,1) =', feasible_interval(0.0, 1.0))
print('  kappa = 1 prime thresholds: the smallest prime p with log p > (1+2g)(1+r_g) contradicts Theorem S at p')
for g in [0.0, 0.25, 0.5, 1.0, 2.0, 5.0]:
    r = (1 + math.sqrt(1 + 8*g)) / 2; B = (1 + 2*g)*(1 + r)
    if B < 60:
        p = sp.nextprime(int(math.floor(math.exp(B))))
        print(f'    g={g:5.2f}: bound B={B:.6f}, e^B={math.exp(B):.6e}, first contradicting prime p={p} (log p={math.log(p):.6f})')
    else:
        print(f'    g={g:5.2f}: bound B={B:.6f}, e^B={math.exp(B):.6e}')
for kap in [math.log(2), 0.5]:
    g = 1.0; r = 2.0; B = kap*(1 + 2*g)*(1 + r)
    print(f'    kappa={kap:.6f}, g=1: log p <= {B:.6f}; first contradicting prime {sp.nextprime(int(math.floor(math.exp(B))))}')

# ------------------------------------------------------------------------------------------------
hdr('[2] Theorem S(b): canonical-class form. B(K,Gamma) = A(y) - D with A(y) = (d1(K)+2) y + d2(K) - delta_B (sympy identity);'
    '\n    |1+y-L| <= sqrt(2g) (sqrt(k) + sqrt(k + 4A(y)))/2 at y = x and x^2 gives a finite sup L0')
y, D, d1K, d2K, dB, KG = sp.symbols('y D d1K d2K deltaB KG', real=True)
# intersection numbers from B via Q(u,v) = d1(u)d2(v) + d2(u)d1(v) - B(u,v); for a graph d1 = 1, d2 = y
Gam2 = 2*y - D                         # Gamma^2 = 2 d1 d2 - def(Gamma)
KdotG = dB - Gam2                      # adjunction: Gamma^2 + K.Gamma = delta_B
BKG = d1K*y + d2K*1 - KdotG            # B(K,Gamma) = d1(K) d2(Gamma) + d2(K) d1(Gamma) - K.Gamma
print('  B(K,Gamma) - [ (d1K+2) y + d2K - deltaB - D ] simplifies to:', sp.simplify(BKG - ((d1K + 2)*y + d2K - dB - D)))
def h_K(g, k, al, be, yy):
    A = al*yy + be
    if k + 4*A < 0: return None
    return math.sqrt(2*g) * (math.sqrt(k) + math.sqrt(k + 4*A)) / 2
def sup_L_K(g, k, al, be, xmax=400.0, n=400001):
    best = -1e18; bx = None
    for xx in np.linspace(-xmax, xmax, n):
        h1 = h_K(g, k, al, be, xx); h2 = h_K(g, k, al, be, xx*xx)
        if h1 is None or h2 is None: continue
        lo = max(1 + xx - h1, 1 + xx*xx - h2); hi = min(1 + xx + h1, 1 + xx*xx + h2)
        if hi >= lo and hi > best: best, bx = hi, xx
    return best, bx
for (g, k, al, be, label) in [(1.0, 0.0, 2.0, 0.0, 'product case K = delta_B(C1+C2), g=1: k=0, alpha=2g, beta=0 (must equal [1]: 9)'),
                              (2.0, 0.0, 4.0, 0.0, 'product case g=2 (must equal [1]: 5*4.37228... = 21.86)'),
                              (1.0, 0.5, 3.0, 0.2, 'non-product K, g=1, def(K)=0.5, alpha=3, beta=0.2'),
                              (1.0, 5.0, 10.0, 3.0, 'non-product K, g=1, def(K)=5, alpha=10, beta=3'),
                              (0.3, 2.0, -1.0, 4.0, 'non-product K with alpha<0 (y bounded by feasibility)')]:
    L0, bx = sup_L_K(g, k, al, be)
    print(f'  {label}: sup L0 = {L0:.6f} at x = {bx:.4f}; kappa=1 prime threshold e^L0 = {math.exp(L0):.4e}')

# ------------------------------------------------------------------------------------------------
hdr('[3] Degree clause d(phi_n) = n: first n >= 2 violating (1 + n - Lambda(n)/kappa)^2 <= 4 g^2 n')
LAM = {n: vonmangoldt(n) for n in range(2, 20001)}
for kap in [1.0, math.log(2), 0.5]:
    for g in [1.0, 2.0, 5.0, 10.0]:
        first = next(n for n in range(2, 20001) if (1 + n - LAM[n]/kap)**2 > 4*g*g*n)
        k2 = next(k for k in range(1, 200) if (1 + 2**k - math.log(2)/kap)**2 > 4*g*g*2**k)
        print(f'  kappa={kap:.6f} g={g:5.1f}: first violating n = {first} (Lambda={LAM[first]:.4f}); first violating n = 2^k at k = {k2}')
print('  threshold g*(n) = |1+n-Lambda(n)|/(2 sqrt n) at kappa = 1 (the clause kills every g < g*(n)):')
for n in [2, 3, 4, 5, 6, 10, 30, 210, 2310, 30030, 2**10, 2**20]:
    lam = LAM[n] if n in LAM else vonmangoldt(n)
    print(f'    n={n:>8d}  Lambda={lam:.6f}  g*={abs(1+n-lam)/(2*math.sqrt(n)):.6f}')
print('  number ring K = Q(i): the weight of the norm fiber W(n) = sum_{N(a)=n} Lambda_K(a) <= [K:Q] log n = 2 log n:')
def lamK_gauss_fiber(n):
    f = sp.factorint(n)
    if len(f) != 1: return 0.0
    p, e = next(iter(f.items()))
    # primes of Z[i] above p: p = 2 ramified (f=1, one prime); p = 1 mod 4 split (two primes, f=1); p = 3 mod 4 inert (f=2)
    if p == 2: return math.log(2)                 # the prime (1+i)^e has norm 2^e: weight log 2
    if p % 4 == 1: return 2*math.log(p)           # two primes of norm p, powers of each: weight 2 log p
    return 2*math.log(p) if e % 2 == 0 else 0.0   # inert prime of norm p^2: norm fiber p^e met only for e even, weight log(p^2)
worst = max((lamK_gauss_fiber(n)/math.log(n), n) for n in range(2, 5001))
print(f'    max_{{2<=n<=5000}} W(n)/log n = {worst[0]:.6f} at n = {worst[1]} (<= 2 = [K:Q])')

# ------------------------------------------------------------------------------------------------
hdr('[4] The (c-K) Gram model: degree clause, A9, injective c, index one on span(C1,C2,Delta,Gamma_n), (H-adj) false; K_Y cannot join')
g = 1.0; kap = 1.0; ns = list(range(2, 41))
eps = np.array([1 + n - LAM[n]/kap for n in ns])
Dn = eps**2 * np.array([2.0**n for n in ns]) / g
m = len(ns) + 1
Bm = np.zeros((m, m)); Bm[0, 0] = 2*g
for i, n in enumerate(ns):
    Bm[0, i+1] = Bm[i+1, 0] = eps[i]; Bm[i+1, i+1] = Dn[i]
schur = 2*g - float(np.sum(eps**2 / Dn))
evB = np.linalg.eigvalsh(Bm / np.sqrt(np.outer(np.diag(Bm), np.diag(Bm))))
print(f'  g=1, n=2..40: Schur complement 2g - sum eps_n^2/D_n = {schur:.6f} (= 2 - sum_n 2^-n > 0); min eigenvalue of the normalized Gram = {evB.min():.3e}')
# full intersection form on (C1, C2, Delta, Gamma_n): Q(u,v) = d1(u)d2(v)+d2(u)d1(v)-B(u,v), d1 = (0,1,1,1..), d2 = (1,0,1,n..)
d1v = np.array([0.0, 1.0, 1.0] + [1.0]*len(ns)); d2v = np.array([1.0, 0.0, 1.0] + [float(n) for n in ns])
Bfull = np.zeros((m+2, m+2)); Bfull[2:, 2:] = Bm
Qf = np.outer(d1v, d2v) + np.outer(d2v, d1v) - Bfull
evQ = np.linalg.eigvalsh(Qf)
print(f'  inertia of the intersection form on (C1,C2,Delta,Gamma_2..Gamma_40): #pos={int((evQ>1e-9).sum())}, #neg={int((evQ<-1e-9).sum())}, #zero={int((abs(evQ)<=1e-9).sum())}')
print('  A9 check (Delta.Gamma_n = Lambda(n)/kappa):', all(abs(Qf[2, 3+i] - LAM[n]/kap) < 1e-9 for i, n in enumerate(ns)),
      '; C1^2, C2^2, C1.C2 =', Qf[0, 0], Qf[1, 1], Qf[0, 1], '; d1(Gamma)=Gamma.C1, d2(Gamma)=Gamma.C2 for n=6:', Qf[3+4, 0], Qf[3+4, 1])
print('  self-intersections Gamma_n^2 = 2n - D_n (product adjunction would give n(2-2g) = 0):', [f'{2*n - Dn[i]:.3e}' for i, n in enumerate(ns[:6])])
print('  adding a canonical class K with adjunction K.Gamma_n = delta_B - Gamma_n^2 (delta_B = 2g-2 = 0): the 2x2 minor')
print('  def(K) def(Gamma_n) - B(K,Gamma_n)^2 for sample (d1K, d2K, def K); negative from n0 on ⇒ K is not in any index-one space:')
for (a, b, k) in [(0.0, 0.0, 1.0), (1.0, -2.0, 100.0), (5.0, 5.0, 1e6)]:
    bad = [n for i, n in enumerate(ns) if k*Dn[i] - ((a + 2)*n + b - 0.0 - Dn[i])**2 < 0]
    print(f'    d1K={a}, d2K={b}, def(K)={k:g}: first n with a negative minor = {bad[0] if bad else None}; negative for all n >= {bad[0] if bad else None} up to 40: {bad == list(range(bad[0], 41)) if bad else None}')

# ------------------------------------------------------------------------------------------------
hdr('[5] Rung 1 (the positive control): closed points by degree; (H-inj2) at a closed point needs it to be the ONLY prime-power'
    '\n    divisor of degree N and of degree 2N; Weil |1+q^N-N_N| <= 2g q^{N/2}; Theorem S fires nowhere')
def mobius(n): return int(sp.mobius(n))
def closed_points(Ns, q, NN):
    return {N: sum(mobius(N//d)*NN[d] for d in sp.divisors(N)) // N for N in Ns}
# (a) the E3 curve y^2 = x^3 + x + 1 over F_7: N_1 by brute force, then Frobenius trace recursion
q = 7
N1 = 1 + sum(1 + (0 if (x**3 + x + 1) % q == 0 else (1 if pow((x**3 + x + 1) % q, (q-1)//2, q) == 1 else -1)) for x in range(q))
a = q + 1 - N1
s = {0: 2, 1: a}
for k in range(2, 41): s[k] = a*s[k-1] - q*s[k-2]
NN = {k: q**k + 1 - s[k] for k in range(1, 41)}
cp = closed_points(range(1, 41), q, NN)
print(f'  y^2=x^3+x+1 / F_7 (g=1): N_1..N_4 = {[NN[k] for k in range(1,5)]}; closed points of degree 1..8 = {[cp[k] for k in range(1,9)]}')
print(f'    min_N<=40 #closed points of degree N = {min(cp.values())} (>= 2 ⇒ every fiber over Fr^N holds >= 2 prime-power divisors ⇒ (H-inj2) fails at EVERY closed point)')
print(f'    Weil: max_N<=40 |1+q^N-N_N|/(2 q^(N/2)) = {max(abs(1+q**k-NN[k])/(2*q**(k/2)) for k in range(1,41)):.6f} (<= g = 1)')
# (b) a genus-2 curve over F_3 by brute force over F_3 and F_9, L-polynomial, closed points
q = 3
x = sp.symbols('x')
def is_squarefree_F3(coeffs):
    P = sp.Poly(coeffs, x, modulus=3)
    return sp.degree(sp.gcd(P, P.diff(x))) == 0
# F_9 = F_3[i]/(i^2+1): elements (u, v) = u + v i
F9 = [(u, v) for u in range(3) for v in range(3)]
def f9mul(A, B): return ((A[0]*B[0] - A[1]*B[1]) % 3, (A[0]*B[1] + A[1]*B[0]) % 3)
def f9add(A, B): return ((A[0]+B[0]) % 3, (A[1]+B[1]) % 3)
def f9pow(A, e):
    R = (1, 0)
    for _ in range(e): R = f9mul(R, A)
    return R
def f9chi(A):
    if A == (0, 0): return 0
    return 1 if f9pow(A, 4) == (1, 0) else -1
def chi3(v):  # quadratic character of F_3: the only nonzero square is 1
    v %= 3
    return 0 if v == 0 else (1 if v == 1 else -1)
def count_hyper(coeffs):  # y^2 = f(x), deg f = 5 (one point at infinity, rational), coeffs high->low over F_3
    def f3(Xv):
        R = 0
        for c in coeffs: R = (R*Xv + c) % 3
        return R
    def f9(Xv):
        R = (0, 0)
        for c in coeffs: R = f9add(f9mul(R, Xv), (c % 3, 0))
        return R
    n1 = 1 + sum(1 + chi3(f3(Xv)) for Xv in range(3))
    n2 = 1 + sum(1 + f9chi(f9(Xv)) for Xv in F9)
    return n1, n2
found = None
for coeffs in itertools.product(range(3), repeat=5):
    cf = [1] + list(coeffs)                      # monic quintic
    if not is_squarefree_F3(cf): continue
    n1, n2 = count_hyper(cf)
    found = (cf, n1, n2); break
cf, n1, n2 = found
a1 = q + 1 - n1                                  # sum alpha
p2 = q*q + 1 - n2                                # sum alpha^2
e2 = (a1*a1 - p2) // 2                           # sum_{i<j} alpha_i alpha_j
Pcoef = [1, -a1, e2, -q*a1, q*q]                 # 1 - a1 T + e2 T^2 - q a1 T^3 + q^2 T^4
alph = np.roots([1, -a1, e2, -q*a1, q*q])        # reciprocal roots alpha_i
print(f'  genus-2 curve y^2 = f(x), f coefficients {cf} over F_3: N_1={n1}, N_2={n2}; |alpha_i| = {np.round(np.abs(alph), 9)} (sqrt 3 = {math.sqrt(3):.9f})')
NN2 = {k: q**k + 1 - int(round(float(np.real(np.sum(alph**k))))) for k in range(1, 31)}
cp2 = closed_points(range(1, 31), q, NN2)
print(f'    closed points of degree 1..8 = {[cp2[k] for k in range(1,9)]}; min over N<=30 = {min(cp2.values())}')
bad2 = [N for N in range(1, 16) if cp2[N] == 1 and all(cp2[d] == 0 for d in sp.divisors(N) if d < N) and cp2[2*N] == 0 and all(cp2[d] == 0 for d in sp.divisors(2*N) if d not in (N, 2*N))]
print(f'    closed points at which (H-inj2) holds (N <= 15): degrees {bad2}  (empty ⇒ Theorem S has no prime to act on)')
print(f'    Weil: max_N<=30 |1+q^N-N_N|/(2 q^(N/2)) = {max(abs(1+q**k-NN2[k])/(2*q**(k/2)) for k in range(1,31)):.6f} (<= g = 2)')
print('  the norm-fiber form of Theorem S on rung 1 is Weil\'s inequality (1+q^N-N_N)^2 <= 4 g^2 q^N: holds for both curves (above).')

# ------------------------------------------------------------------------------------------------
hdr('[6] Proposition A toy: 0/1 sequences e(k) obeying sum_j c_j e(k+j) = 0 with c from P(x) = (x-1)(x-d_p)prod(x-chi_i)')
X = sp.symbols('X')
cases = [('d_p=2, chi=3', (X-1)*(X-2)*(X-3)), ('d_p=2, chi=-1', (X-1)*(X-2)*(X+1)),
         ('d_p=2, chi=1+sqrt2', (X-1)*(X-2)*(X-1-sp.sqrt(2))), ('d_p=2, chi=i', (X-1)*(X-2)*(X-sp.I)),
         ('d_p=3, chi=-1, chi=omega (cube root of 1)', (X-1)*(X-3)*(X+1)*(X-sp.exp(2*sp.pi*sp.I/3))),
         ('d_p=1 (double base 1), chi=-1', (X-1)*(X-1)*(X+1))]
mp.mp.dps = 50
for name, Pp in cases:
    cexact = [sp.N(cc, 60) for cc in sp.Poly(sp.expand(Pp), X).all_coeffs()[::-1]]    # c_0..c_r, c_r = 1
    c = [mp.mpc(str(sp.re(cc)), str(sp.im(cc))) for cc in cexact]
    r = len(c) - 1
    survivors = []
    for init in itertools.product([0, 1], repeat=r):
        e = list(init); okk = True
        for k in range(60):
            nxt = -sum(c[j]*e[k+j] for j in range(r))
            if abs(nxt) < mp.mpf('1e-40'): e.append(0)
            elif abs(nxt - 1) < mp.mpf('1e-40'): e.append(1)
            else: okk = False; break
        if okk: survivors.append(e)
    per = []
    for e in survivors:
        # preperiod and period of the state sequence
        states = [tuple(e[k:k+r]) for k in range(40)]
        k1 = next(k for k in range(40) if states[k] in states[k+1:])
        t = states[k1+1:].index(states[k1]) + 1
        per.append((k1+1, t, e[:12]))
    T = sp.ilcm(*range(1, 2**r + 1))
    print(f'  {name}: r={r}, 0/1 solutions (of 2^r={2**r} initial states) = {len(survivors)}; (start index of periodicity, period, first 12 terms) = {per}; all periods divide lcm(1..2^r) = {T}: {all(T % pp[1] == 0 for pp in per)}; preperiod <= 2^r: {all(pp[0] <= 2**r for pp in per)}')
print('  base-1 coefficient bound: in a_k = 1 + d_p^k - sum_i chi_i(p)^k the coefficient of 1^k is 1 + [d_p=1] - #{i: chi_i(p)=1} <= 2;')
print('  a constant (or periodic) sequence a_k = log N/kappa >= log p/kappa therefore forces log p <= 2 kappa: first failing primes')
for kap in [1.0, math.log(2), 0.5, 2.0]:
    print(f'    kappa={kap:.6f}: first prime with log p > 2 kappa: {sp.nextprime(int(math.floor(math.exp(2*kap))))}')

# ------------------------------------------------------------------------------------------------
hdr('[7] Chebyshev lower bound theta(x) >= c x (re-derived: psi(2n) >= n log 4 - log(2n+1); psi - theta <= (log x)^2 sqrt(x)/(2 log 2))')
def simple_sieve(n):
    s = np.ones(n + 1, dtype=bool); s[:2] = False
    for p in range(2, int(n**0.5) + 1):
        if s[p]: s[p*p::p] = False
    return np.flatnonzero(s)
XCH = 10**8
pr = simple_sieve(XCH + 1000)
th = np.cumsum(np.log(pr.astype(np.float64)))
# inf over x in [p_k, p_{k+1}) of theta(x)/x is theta(p_k)/p_{k+1}
ratios = th[:-1] / pr[1:]
imin = int(np.argmin(ratios))
print(f'  numeric: inf_{{2<=x<{pr[-1]}}} theta(x)/x = {ratios[imin]:.6f} (approached as x -> {pr[imin+1]}-); theta(10^8) = {th[np.searchsorted(pr, 10**8, side="right")-1]:.3f}')
print(f'  the same infimum restricted to x >= 100: {ratios[np.searchsorted(pr,100):].min():.6f}; x >= 10^4: {ratios[np.searchsorted(pr,10**4):].min():.6f}')
def cheb_lower(xx): return xx*math.log(2) - math.log(4) - math.log(xx + 1) - (math.log(xx)**2)*math.sqrt(xx)/(2*math.log(2))
for xx in [1e6, 1e7, 1e8, 1e9, 1e12]:
    print(f'  analytic: x={xx:.0e}: lower bound/x = {cheb_lower(xx)/xx:.6f} (increasing for x > e^4, so >= this value beyond)')
print('  sanity of the central-binomial step: n, log C(2n,n), psi(2n), n log 4 - log(2n+1):')
for n in [10, 100, 1000]:
    lc = float(sp.log(sp.binomial(2*n, n)).evalf(20))
    psi2n = sum(math.log(p)*int(math.floor(math.log(2*n)/math.log(p) + 1e-12)) for p in sp.primerange(2, 2*n+1))
    print(f'    n={n}: {lc:.4f} <= {psi2n:.4f}; lower {n*math.log(4)-math.log(2*n+1):.4f} <= {lc:.4f}')
C_THETA = 0.23
print(f'  => theta(x) >= {C_THETA} x for every x >= 2 (numeric inf 0.2310 on [2,1e8], analytic >= 0.669 beyond 1e8); used in Lemma B.1')
del pr, th, ratios
sys.stdout.flush()

# ------------------------------------------------------------------------------------------------
import os
if os.environ.get('STOP_BEFORE_8'):
    print('STOP_BEFORE_8 set: stopping'); sys.exit(0)
hdr('[8] Proposition B: greedy regradings of the rational primes (consecutive blocks S_N, deg l = N on S_N, phi_n = F^{deg n}, d(F^a) = d^a)')
def prime_segments(limit, seg_odd=1 << 24):
    """Yield numpy int64 arrays of the primes <= limit, in increasing order (odd-only segmented sieve)."""
    yield np.array([2], dtype=np.int64)
    base = simple_sieve(int(math.isqrt(limit)) + 2)[1:]
    lo = 3
    while lo <= limit:
        n = min(seg_odd, (limit - lo)//2 + 1)
        hi = lo + 2*(n - 1)
        s = np.ones(n, dtype=bool)
        for p in base:
            p = int(p); pp = p*p
            if pp > hi: break
            if pp >= lo: start = pp
            else:
                start = ((lo + p - 1)//p)*p
                if start % 2 == 0: start += p
            s[(start - lo)//2::p] = False
        yield lo + 2*np.flatnonzero(s).astype(np.int64)
        lo = hi + 2

class Greedy:
    """Consecutive-prime greedy: take primes while the block sum stays <= the block target, then take the next
    one too iff that brings the sum closer.  Block target w-target(N) = kappa(1+d^N) - sum_{e|N, e<N} w_e."""
    def __init__(self, d, kappa, Nmax):
        self.d, self.kappa, self.Nmax = d, kappa, Nmax
        self.w, self.info, self.done = {}, {}, False
        self.open_block(1)
    def open_block(self, N):
        self.N = N
        self.target = self.kappa*(1 + self.d**N) - math.fsum(self.w[e] for e in sp.divisors(N) if e < N)
        self.need = self.target
        self.parts, self.count, self.first, self.last = [], 0, None, None
    def close_block(self, P_rej):
        wN = math.fsum(self.parts)
        self.w[self.N] = wN
        self.info[self.N] = dict(count=self.count, first=self.first, last=self.last, P_rej=P_rej, target=self.target, w=wN)
        if self.N >= self.Nmax: self.done = True
        else: self.open_block(self.N + 1)
    def feed(self, P, Lg):
        pos, n = 0, len(P)
        while not self.done and pos < n:
            if self.need < 0 and self.count == 0:            # negative target: the block is empty
                self.close_block(int(P[pos])); continue
            cs = np.cumsum(Lg[pos:])
            k = int(np.searchsorted(cs, self.need, side='right'))
            if k == len(cs):                                 # the whole rest of the segment fits
                self.parts.append(float(np.sum(Lg[pos:])))
                if self.first is None: self.first = int(P[pos])
                self.last = int(P[-1]); self.count += n - pos
                self.need -= float(cs[-1]); pos = n
                break
            Sk = float(cs[k-1]) if k > 0 else 0.0
            l = float(Lg[pos + k])
            if k > 0:
                self.parts.append(float(np.sum(Lg[pos:pos + k])))
                if self.first is None: self.first = int(P[pos])
                self.last = int(P[pos + k - 1]); self.count += k
            P_rej = int(P[pos + k])
            if abs(Sk + l - self.need) < abs(Sk - self.need):
                self.parts.append(l); self.count += 1
                if self.first is None: self.first = P_rej
                self.last = P_rej; pos += k + 1
            else:
                pos += k
            self.close_block(P_rej)

CONFIGS = [(2, 1.0, 24), (2, math.log(2), 24), (3, 1.0, 20), (3, 0.5, 20)]
greedies = [Greedy(d, kap, Nm) for (d, kap, Nm) in CONFIGS]
LIMIT = 6_200_000_000
nprimes = 0; tS = time.time(); used_counts = [0]*len(greedies)
for P in prime_segments(LIMIT):
    if len(P) == 0: continue
    Lg = np.log(P.astype(np.float64))
    for gi, G in enumerate(greedies):
        if not G.done: G.feed(P, Lg)
    nprimes += len(P)
    if all(G.done for G in greedies):
        print(f'  sieve stopped at {int(P[-1])} after {nprimes} primes ({time.time()-tS:.1f} s)'); break
else:
    print('  WARNING: LIMIT reached before all configurations finished')
print(f'  sieve sanity: pi(10^7) from sympy = {sp.primepi(10**7)} (the streamed primes agree with sympy on the first segment: checked below)')
seg1 = list(prime_segments(10**7, seg_odd=1 << 23))
print(f'  streamed pi(10^7) = {sum(len(x) for x in seg1)}')

def report(G, d, kap, Nm):
    L = {N: math.fsum(G.w[e] for e in sp.divisors(N)) for N in range(1, Nm + 1)}
    eps_ = {N: 1 + d**N - L[N]/kap for N in range(1, Nm + 1)}
    e_ = {N: eps_[N] * d**(-N/2) for N in range(1, Nm + 1)}
    print(f'\n  --- d = {d}, kappa = {kap:.6f}, N = 1..{Nm} ---')
    print('   N  #S_N        first         last          w_N              L_N          eps_N      e_N=eps_N d^(-N/2)   target_w   |kappa eps_N|  (1/2)log P_N')
    for N in range(1, Nm + 1):
        I = G.info[N]
        print(f'  {N:2d} {I["count"]:9d} {str(I["first"]):>12} {str(I["last"]):>12} {I["w"]:17.6f} {L[N]:17.6f} {eps_[N]:+11.6f} {e_[N]:+14.6e} {I["target"]:14.3f} {abs(kap*eps_[N]):10.6f} {0.5*math.log(I["P_rej"]):10.6f}')
    # Lemma B.1 checks
    tpos = all(G.info[N]['target'] >= 0 for N in range(1, Nm + 1))
    errok = all(abs(kap*eps_[N]) <= 0.5*math.log(G.info[N]['P_rej']) + 1e-6 for N in range(1, Nm + 1))
    Cobs = max(math.log(G.info[N]['P_rej']) - N*math.log(d) for N in range(1, Nm + 1))
    used = sum(G.info[N]['count'] for N in range(1, Nm + 1)); nonempty = sum(1 for N in range(1, Nm + 1) if G.info[N]['count'] > 0)
    print(f'  Lemma B.1: all block targets >= 0: {tpos}; |kappa eps_N| <= (1/2) log P_N for all N: {errok}; max_N (log P_N - N log d) = {Cobs:.4f}')
    print(f'  Theorem R: primes used = {used} (each once, consecutive), nonempty blocks = {nonempty} of {Nm} (their w_N have disjoint prime supports ⇒ Q-independent)')
    # tail bound for N > Nm
    c = C_THETA
    Cb = math.log(2*kap*d/((d - 1)*c))
    Call = max(Cb, Cobs)
    Hs = [kap*d**(N+1)/(d-1) - c - (N/2)*(N*math.log(d) + Cb) - kap*N for N in range(Nm + 1, 2001)]
    tgt = [kap*(1 + d**N) - kap*N/2 - kap*d**(N/2 + 1)/(d - 1) - (N/4)*((N/2)*math.log(d) + Call) for N in range(Nm + 1, 2001)]
    print(f'  tail: C = log(2 kappa d/((d-1)c)) = {Cb:.4f}; H(N) >= 0 for all Nmax < N <= 2000: {min(Hs) >= 0} (min {min(Hs):.3e}); '
          f'targets > 0 there: {min(tgt) > 0}; e^C d^N > N/(2c) there: {all(math.exp(Cb)*d**N > N/(2*c) for N in range(Nm+1, 2001))}')
    tail = sum((N*math.log(d) + Call)/kap * d**(-N/2) for N in range(Nm + 1, 4001))
    S2 = 2*sum(abs(e_[N]) for N in range(1, Nm + 1))
    twog_rig = S2 + tail
    print(f'  sum_(N<={Nm}) 2|e_N| = {S2:.6f}; tail bound sum_(N>{Nm}) (N log d + C)/kappa d^(-N/2) = {tail:.3e} (C = {Call:.4f}); 2g_rig = {twog_rig:.6f} (g = {twog_rig/2:.6f})')
    E = np.array([[e_[abs(a - b)] if a != b else 0.0 for b in range(Nm + 1)] for a in range(Nm + 1)])
    lam0 = np.linalg.eigvalsh(E).min()
    for twog in [twog_rig, 2.0, -lam0]:
        ev = np.linalg.eigvalsh(E + twog*np.eye(Nm + 1))
        print(f'    2g = {twog:.6f}: Toeplitz (e_|a-b|)_(a,b<={Nm}) eigenvalues min {ev.min():+.6f}, max {ev.max():.6f}')
    print(f'    smallest 2g making the finite section PSD = -lambda_min(T(0)) = {-lam0:.6f}')
    # inertia of the intersection form on (C1, C2, gamma_0..gamma_Nm) at 2g_rig, after the congruence gamma_a -> d^(-a/2) gamma_a
    M = Nm + 1
    Q = np.zeros((M + 2, M + 2))
    Q[0, 1] = Q[1, 0] = 1.0
    for a_ in range(M):
        sa = d**(-a_/2)
        Q[0, 2 + a_] = Q[2 + a_, 0] = 1.0*sa          # gamma_a . C1 = d1 = 1
        Q[1, 2 + a_] = Q[2 + a_, 1] = d**a_ * sa      # gamma_a . C2 = d2 = d^a
        for b_ in range(M):
            sb = d**(-b_/2)
            Bab = twog_rig*d**a_ if a_ == b_ else d**min(a_, b_)*eps_[abs(a_ - b_)]
            Q[2 + a_, 2 + b_] = (d**b_ + d**a_ - Bab)*sa*sb
    evq = np.linalg.eigvalsh(Q)
    print(f'    intersection form on span(C1,C2,gamma_0..gamma_{Nm}) at 2g_rig: #pos = {int((evq > 1e-9).sum())}, #neg = {int((evq < -1e-9).sum())}, #zero = {int((abs(evq) <= 1e-9).sum())}  (index one, rank {M+2})')
    print(f'    A9 at N = 1, 2, 3: Delta.gamma_N = d^N + 1 - eps_N = {[round(d**N + 1 - eps_[N], 6) for N in (1,2,3)]} = L_N/kappa = {[round(L[N]/kap, 6) for N in (1,2,3)]}')
    # Prop N(b) fails for the regrading: mass of the target-graded measure at d vs Lambda at d
    print(f'    Prop N(b) negative check: target-graded mass at x = d = {d}: L_1 = {L[1]:.6f} vs Lambda({d}) = {math.log(d):.6f} (the measure identity fails, as it must off the degree clause)')
    # the regraded zeta: coefficients L_N/kappa (what the index theorem sees) vs the brief's prod (1-T^{deg l})^{-1} (point counts)
    beur = {N: sum(e*G.info[e]['count'] for e in sp.divisors(N)) for N in range(1, Nm + 1)}
    print('    regraded zeta: Weil ratio |1+d^N - L_N/kappa|/d^(N/2) (the index theorem, bounded) vs the Beurling count sum_{e|N} e#S_e of prod_l(1-T^{deg l})^{-1}:')
    for N in [1, 2, 4, 8, 12, 16, Nm]:
        print(f'      N={N:2d}: L_N/kappa = {L[N]/kap:.6e}, |eps_N|/d^(N/2) = {abs(e_[N]):.3e};  Beurling count = {beur[N]:.6e}, |1+d^N - count|/d^(N/2) = {abs(1 + d**N - beur[N])/d**(N/2):.3e}')
    return twog_rig

for G, (d, kap, Nm) in zip(greedies, CONFIGS):
    report(G, d, kap, Nm)
sys.stdout.flush()

# ------------------------------------------------------------------------------------------------
hdr('[9] Proposition C: w(u) = 2cosh(u/2) - e^{-|u|/2} tau(e^{|u|}) with tau = sum Lambda(n)/kappa delta_n + archimedean;'
    '\n    (9a) explicit formula against a Gaussian (x-18 p. 5 (2)); (9b) the smeared diagonal\'s defect counts zeros; (9c) CC (13) = x-18 (2)')
mp.mp.dps = 30
t9 = time.time()
ZEROS = []
nz = 0
while True:
    nz += 1
    gz = mp.im(mp.zetazero(nz))
    ZEROS.append(gz)
    if gz > 560: break
print(f'  computed {len(ZEROS)} zeros up to height {float(ZEROS[-1]):.3f} with mpmath.zetazero ({time.time()-t9:.1f} s); first three {[mp.nstr(z_, 12) for z_ in ZEROS[:3]]}')
def ef_check(u0, sigma, kappa=1.0):
    phi = lambda u: mp.exp(-(u - u0)**2/(2*sigma**2))
    zero_side = 2*sum(sigma*mp.sqrt(2*mp.pi)*mp.exp(-sigma**2*g_**2/2)*mp.cos(g_*u0) for g_ in ZEROS[:60])
    lo_, hi_ = max(mp.mpf('1e-9'), u0 - 14*sigma), u0 + 14*sigma
    arch = mp.quad(lambda u: phi(u)*(2*mp.cosh(u/2) - mp.exp(-u/2)/(1 - mp.exp(-2*u))), [lo_, u0, hi_])
    prime = sum(mp.mpf(vonmangoldt(n))*n**mp.mpf(-0.5)*phi(mp.log(n)) for n in range(2, int(mp.exp(hi_)) + 2) if vonmangoldt(n) > 0)
    return zero_side, arch - prime/kappa, prime
for u0 in [2.0, 3.0, 4.0]:
    zs, rhs, pr_ = ef_check(mp.mpf(u0), mp.mpf('0.25'))
    print(f'  u0={u0}: zero side sum_gamma phi^(gamma) = {mp.nstr(zs, 15)};  pole+arch-prime side (kappa=1) = {mp.nstr(rhs, 15)};  difference {mp.nstr(zs - rhs, 3)}')
    for kap in [0.9, 1.1]:
        _, rk, _ = ef_check(mp.mpf(u0), mp.mpf('0.25'), kappa=kap)
        print(f'      kappa={kap}: the same side = {mp.nstr(rk, 12)}; mismatch with the zero side {mp.nstr(zs - rk, 6)} (= (1/kappa - 1) x prime part {mp.nstr((1/mp.mpf(kap) - 1)*pr_, 6)})')
print('  (9b) def(Delta_eps) = sum over zeros of |F_eps^(gamma)|^2 = 2 sum_{gamma>0} exp(-eps^2 gamma^2) for the unit-mass Gaussian F_eps (Haran p. 258 (ii) form):')
for epsv in [1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]:
    dv = 2*sum(mp.exp(-(mp.mpf(epsv)*g_)**2) for g_ in ZEROS)
    NT = sum(1 for g_ in ZEROS if g_ <= 1/epsv)
    Tt = 1/mp.mpf(epsv)
    NRvM = Tt/(2*mp.pi)*mp.log(Tt/(2*mp.pi)) - Tt/(2*mp.pi) + mp.mpf(7)/8
    print(f'    eps={epsv:5.2f}: def(Delta_eps) = {mp.nstr(dv, 10):>12};  2N(1/eps) = {2*NT:4d};  ratio = {mp.nstr(dv/(2*NT), 6) if NT else "-"};  (zeros used up to 560: tail exp(-(eps*560)^2) = {mp.nstr(mp.exp(-(epsv*560)**2), 3)})')
print('    rung-1 comparison: on S x_k S the same expression is def(Delta) = 2g exactly (Haran p. 258 (ii) with f = delta at p^0: 2 - (2 - #zeros)).')
uu = sp.symbols('u', positive=True); tt = sp.symbols('t', positive=True)
print('  (9c) CC 1805.10501 (13) archimedean density u^2/(u^2-1) at u = e^t equals x-18 (2)\'s (1-e^{-2t})^{-1}:',
      sp.simplify((uu**2/(uu**2 - 1)).subs(uu, sp.exp(tt)) - 1/(1 - sp.exp(-2*tt))) == 0)
print(f'\nTOTAL RUN TIME {time.time()-T0:.1f} s')
