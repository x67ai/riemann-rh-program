#!/usr/bin/env python3
"""beta-shapes-s35 / verify/numbers_check.py -- every number used in NOTE.md, recomputed.
Python 3 + mpmath. Run: python3 numbers_check.py > numbers-check.log
Sections [1]..[11] are cited from NOTE.md by number."""
import sys, math, itertools, datetime, subprocess
from mpmath import mp, mpf, log, exp, sqrt, zetazero, nstr
mp.dps = 30

def P(*a): print(*a); sys.stdout.flush()

P("beta-shapes-s35 numbers-check --", datetime.datetime.now().isoformat(), "--", subprocess.run(["uname","-mprs"],capture_output=True,text=True).stdout.strip())
P("mpmath dps =", mp.dps)

# ---------- primes, Lambda, psi, theta ----------
def primes_upto(n):
    s = bytearray([1])*(n+1); s[0]=s[1]=0
    for i in range(2,int(n**0.5)+1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(n+1) if s[i]]
PR = primes_upto(2_000_000)
PSET = set(PR)
def Lambda(n):
    """von Mangoldt: log p if n = p^k (k>=1), else 0."""
    if n < 2: return mpf(0)
    for p in PR:
        if p*p > n: break
        if n % p == 0:
            while n % p == 0: n //= p
            return log(p) if n == 1 else mpf(0)
    return log(n)  # n prime
def psi(x):
    return sum(Lambda(n) for n in range(2, int(x)+1))
def theta(x):
    return sum(log(p) for p in PR if p <= x)

P("\n[1] Lambda(n), n = 2..30 (A5's diagonal row over Z), and the divergence of the fiber sum over Delta in T1")
P("    n :", " ".join(f"{n}" for n in range(2,31)))
P("    Lambda(n):", " ".join(nstr(Lambda(n),4) for n in range(2,31)))
for x in (10,100,1000,10000):
    P(f"    psi({x}) = {nstr(psi(x),12)}   theta({x}) = {nstr(theta(x),12)}   #primes<={x} = {sum(1 for p in PR if p<=x)}")
P("    Euclid witness: 2*3*5*7*11*13 + 1 =", 2*3*5*7*11*13+1, "= 59*509 :", (2*3*5*7*11*13+1) % 59 == 0 and (2*3*5*7*11*13+1)//59 == 509)
P("    => sum_{n>=2} Lambda(n) >= theta(x) -> infinity; T1's fiber sum over Delta is not a real number.")

P("\n[2] T3 injective sub-case, base-1 coefficient bound: log p <= kappa*(2 + 2g) (route (b), d_p = 1) and log p/kappa in {2-h,...,2} (route (a))")
for kappa in (mpf(1), log(2)):
    for g in (0,1,2,5):
        bound = kappa*(2+2*g)
        first = next(p for p in PR if log(p) > bound)
        P(f"    kappa={nstr(kappa,6)} g={g}: bound kappa(2+2g)={nstr(bound,8)}; first prime with log p > bound: p={first} (log p = {nstr(log(first),8)})")
P("    route (a), kappa = 1: log p/kappa <= 2 fails first at p = 11 (log 11 =", nstr(log(11),10), "> 2); log 7 =", nstr(log(7),10), "<= 2.")

P("\n[3] T3 route (b), d_p >= 2: the least k with d^k + 1 - log p/kappa > 2 g d^(k/2)  (Weil's inequality at p^k fails from that k on)")
for kappa in (mpf(1),):
    for p in (2,3,5):
        for d in (2,3,4):
            for g in (1,2,5):
                k = 1
                while not (mpf(d)**k + 1 - log(p)/kappa > 2*g*mpf(d)**(mpf(k)/2)): k += 1
                P(f"    p={p} d_p={d} g={g} kappa=1: first violating k = {k}   (lhs={nstr(mpf(d)**k+1-log(p)/kappa,8)}, rhs={nstr(2*g*mpf(d)**(mpf(k)/2),8)})")
P("    analytic form: d^(k/2) > 2g + (log p/kappa - 1)/d^(k/2) -- k > 2 log(2g+1)/log d suffices once log p/kappa <= 1 + d^(k/2)... (see NOTE 2.3.4)")

P("\n[4] T3 route (b), the composite-index bound: Lambda(pq) = 0 gives d_{pq} + 1 <= 2 g sqrt(d_{pq}), i.e. d_{pq} <= (g + sqrt(g^2-1))^2")
for g in (1,2,3,5,10):
    C = (g + sqrt(mpf(g)**2 - 1))**2
    P(f"    g={g}: d_pq <= {nstr(C,10)}  (floor {int(C)}); check: for d = floor: d+1 - 2g sqrt(d) = {nstr(int(C)+1-2*g*sqrt(int(C)),6)} <= 0 ; for d = floor+1: {nstr(int(C)+2-2*g*sqrt(int(C)+1),6)}")
P("    g = 1 forces d_2 = d_3 = 1 (d_6 <= 1).")

P("\n[5] Theorem R witness: which integers N <= 10^5 satisfy log N in kappa*Z (|log N/kappa - round| < 1e-12)?")
for name,kappa in (("1",mpf(1)),("log 2",log(2)),("log 6",log(6)),("log 12",log(12))):
    hits = [N for N in range(2,100001) if abs(log(N)/kappa - round(log(N)/kappa)) < mpf(10)**-12]
    P(f"    kappa = {name}: {len(hits)} hits; first ten: {hits[:10]}")
P("    kappa = 1: distance of e^m to the nearest integer, m = 1..12:", " ".join(nstr(abs(exp(m)-round(exp(m))),4) for m in range(1,13)))
P("    (the two-fiber unique-factorization argument of Theorem R needs no transcendence; this row is illustration only)")

P("\n[6] Theorem R, the proportionality lemma: N^b = M^a (a,b >= 1) forces equal prime support -- brute force over N,M <= 3000, a,b <= 6")
bad = 0; cases = 0
def support(n):
    s=set()
    for p in PR:
        if p*p>n: break
        if n%p==0:
            s.add(p)
            while n%p==0: n//=p
    if n>1: s.add(n)
    return s
for N in range(2,3001):
    for M in range(N,3001):
        for a in range(1,7):
            for b in range(1,7):
                if N**b == M**a:
                    cases += 1
                    if support(N) != support(M): bad += 1
P(f"    cases with N^b = M^a: {cases}; support mismatches: {bad}")

P("\n[7] T2, the non-Cartier step over Z at finite level N: N!*e_n lies in the truncated ghost lattice L_N (congruences 0801.1691 (1.10): a_j = a_{pj} mod p^(1+v_p(j)))")
def vp(n,p):
    c=0
    while n%p==0: n//=p; c+=1
    return c
def in_lattice(a, N):
    for p in PR:
        if p > N: break
        for j in range(1, N//p + 1):
            if (a[j-1] - a[p*j-1]) % (p**(1+vp(j,p))) != 0: return False
    return True
ok = True
for N in range(1,41):
    fact = math.factorial(N)
    for n in range(1,N+1):
        e = [0]*N; e[n-1] = fact
        if not in_lattice(e,N): ok=False; P("    FAIL", N, n)
    # the reader's basis v_d = (d*[d|n])_n and its determinant
    V = [[d if n % d == 0 else 0 for n in range(1,N+1)] for d in range(1,N+1)]
    if not all(in_lattice(row,N) for row in V): ok=False; P("    basis FAIL", N)
    det = 1
    for d in range(1,N+1): det *= V[d-1][d-1]   # triangular
    if det != fact: ok=False; P("    det FAIL", N)
P("    N = 1..40: N!*e_n in L_N for every n; v_d in L_N; det(v_d) = N! :", ok)
f = [720,0,0,0,0,0]; g = [0,720,0,0,0,0]
P("    zero-divisor witness at N = 6, component n = 2: f = 720*e_1 in L_6:", in_lattice(f,6), "(f_2 = 0, so f vanishes on Gamma_2); g = 720*e_2 in L_6:", in_lattice(g,6), "g != 0; f*g coordinatewise =", [x*y for x,y in zip(f,g)])
P("    general: for ANY f in L_N with f_n = 0, f * (N! e_n) = 0 coordinatewise -- every local equation of Gamma_n is a zero divisor (E3 Theorem 4.1(b)'s pattern, over Z at the line).")

P("\n[7b] T2 (b), the BOX version (Borger's E-typical finite levels) and the Legendre product of moduli")
import itertools as _it
def box(b):  # b: dict prime->bound
    idx=[1]
    for p,e in b.items():
        idx=[i*p**k for i in idx for k in range(e+1)]
    return sorted(idx)
def in_box_lattice(a, F):  # a: dict index->value
    for p in PR:
        if p > max(F): break
        for j in F:
            if p*j in F and (a[j]-a[p*j]) % (p**(1+vp(j,p))) != 0: return False
    return True
okb=True
for b in ({2:2,3:1},{2:3,3:2,5:1},{2:1,3:1,5:1,7:1},{2:4},{3:2,7:1}):
    F=box(b); J=1
    for p,e in b.items(): J*=p**(1+e)
    for n in F:
        a={j:(J if j==n else 0) for j in F}
        if not in_box_lattice(a,F): okb=False; P("    box FAIL", b, n)
    # a smaller multiple fails somewhere (J is sharp at the top index): witness that J/p is not enough for some n
    P(f"    box {b}: F = {F}; J = {J}; J*e_n in L_F for every n: {all(in_box_lattice({j:(J if j==n else 0) for j in F},F) for n in F)}")
P("    all boxes: J*e_n in L_F:", okb)
for N in (6,10,12,20,30):
    prod=1
    for p in PR:
        if p>N: break
        for j in range(1,N//p+1): prod*=p**(1+vp(j,p))
    P(f"    N={N}: product of the moduli p^(1+v_p(j)) over pj<=N = {prod} ; N! = {math.factorial(N)} ; equal: {prod==math.factorial(N)}")
P("    hence index(L_N) <= N! = index(span v_d), so L_N = span(v_d) = the image of W(Z) on [1,N]; v_d(j)-v_d(pj) = -d only when d does not divide j and d | pj, and then p^(1+v_p(j)) = p^(v_p(d)) | d:", all(all(((d*(j%d==0) - d*((p*j)%d==0)) % (p**(1+vp(j,p))) == 0) for j in range(1,41) for p in PR if p<=40) for d in range(1,41)))

P("\n[8] Rung 1 (y^2 = x^3 + x + 1 over F_7, E3's a_d = 5, 25, 125, 605): fiber products are q^{N_N}, a single residue characteristic")
a = {1:5,2:25,3:125,4:605}
for Nn in range(1,5):
    NN = sum(d*a[d] for d in range(1,Nn+1) if Nn % d == 0)
    P(f"    N={Nn}: N_N = sum_(d|N) d a_d = {NN}; fiber product = 7^{NN}; log(product)/log 7 = {NN} = (Delta . Gamma_Fr^N) in Z")
P("    single residue characteristic 7: the support of every fiber product is {7} -- Theorem R's proportionality holds, no contradiction (rung 1 passes).")

P("\n[9] The finite-h Lefschetz reading of the explicit formula: zeros of zeta with 0 < Im rho <= 100 (mpmath.zetazero)")
zs = []
k = 1
while True:
    z = zetazero(k)
    if z.imag > 100: break
    zs.append(z); k += 1
P(f"    count = {len(zs)}; first five imaginary parts: {[nstr(z.imag,10) for z in zs[:5]]}; all Re = 1/2 to 1e-25: {all(abs(z.real-mpf(1)/2)<mpf(10)**-25 for z in zs)}")
P("    (a finite Lefschetz identity with h eigencharacters n^rho would need h >= 2*", len(zs), "already below T = 100; Hadamard's theorem (infinitely many) is [recalled, unverified] and not load-bearing)")

P("\n[10] Chebyshev windows (route (b), non-injective, illustration): psi(x) - x and (psi(x)-x)/sqrt(x)")
for x in (10**2,10**3,10**4,10**5,10**6):
    ps = psi(x)
    P(f"    x=10^{int(round(math.log10(x)))}: psi-x = {nstr(ps-x,8)}; (psi-x)/sqrt(x) = {nstr((ps-x)/sqrt(x),6)}")
P("    Littlewood 1914 (psi(x)-x = Omega_pm(sqrt(x) log log log x)) is [recalled, unverified]: not on disk, not load-bearing.")

P("\n[11] Lemma F (finite fibers): a fiber with product N has at most log_2 N prime powers; the fiber of c(Gamma_p) contains p, so N_p >= p, (Delta . c(Gamma_p)) = log N_p / kappa >= log p / kappa")
for p in (2,3,5,7,11,101,1009):
    P(f"    p={p}: log p = {nstr(log(p),10)}; with kappa=1 the target's diagonal-row value at c(Gamma_p) is >= {nstr(log(p),6)} and equals log of an integer divisible by {p}")
P("\nEND", datetime.datetime.now().isoformat())
