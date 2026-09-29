# beta-shapes-s35 READER (Opus 5) independent recomputation. Written from the NOTE's statements,
# not from the writer's script. Python 3 + mpmath (dps 30) + sympy.
import math, itertools, random, datetime, platform
from fractions import Fraction
import mpmath as mp
from sympy import factorint, primerange, isprime, Matrix
mp.mp.dps = 30
print('beta-shapes-s35 reader numbers_O --', datetime.datetime.now().isoformat(), '--', platform.platform())

def Lam(n):
    f = factorint(n)
    return mp.log(list(f)[0]) if len(f) == 1 else mp.mpf(0)

print('\n[O1] Lambda(n), psi, theta, Euclid')
print('   ', ' '.join(f'{n}:{float(Lam(n)):.4f}' for n in range(2, 31)))
for x in (10, 100, 1000, 10000):
    psi = mp.fsum(Lam(n) for n in range(2, x+1)); th = mp.fsum(mp.log(p) for p in primerange(2, x+1))
    print(f'    x={x}: psi={mp.nstr(psi,12)} theta={mp.nstr(th,12)} pi(x)={len(list(primerange(2,x+1)))}')
e = 2*3*5*7*11*13+1; print('    Euclid 30031 =', factorint(e))

print('\n[O2] first prime with log p > kappa*(2+2g) (route b, d_p=1) and log p > 2 kappa (route a)')
for kap_name, kap in (('1', mp.mpf(1)), ('log2', mp.log(2))):
    for g in (0, 1, 2, 5):
        B = kap*(2+2*g); p = 2
        while mp.log(p) <= B: p = next(q for q in range(p+1, 10**7) if isprime(q))
        print(f'    kappa={kap_name} g={g}: bound={mp.nstr(B,10)} first p={p} log p={mp.nstr(mp.log(p),10)}')
    p = 2
    while mp.log(p) <= 2*kap: p = next(q for q in range(p+1, 10**6) if isprime(q))
    print(f'    route (a) kappa={kap_name}: first p with log p > 2 kappa: {p}')

print('\n[O3] route (b) prime powers: least k with d^k + 1 - log p/kappa > 2 g d^(k/2); and the sufficient k-bound')
for p in (2, 3, 5):
    for d in (2, 3, 4):
        for g in (1, 2, 5):
            L = mp.log(p); k = 1
            while not (d**k + 1 - L > 2*g*mp.sqrt(d)**k): k += 1
            kb = 2*mp.log((2*g+1)+L)/mp.log(d)
            # the sufficient bound must be >= the true threshold (i.e. every k > kb violates)
            ok = all(d**kk + 1 - L > 2*g*mp.sqrt(d)**kk for kk in range(int(mp.floor(kb))+1, int(mp.floor(kb))+30))
            print(f'    p={p} d={d} g={g}: first k={k}; NOTE bound k > {mp.nstr(kb,6)} sufficient: {ok}')

print('\n[O4] n = pq: d+1 <= 2 g sqrt(d)  <=>  d <= C_g = (g+sqrt(g^2-1))^2')
for g in (0, 1, 2, 3, 5, 10):
    if g == 0: print('    g=0: d+1 <= 0 impossible -> no d at all (genus 0 dies at the first composite)'); continue
    C = (g+mp.sqrt(g*g-1))**2
    fl = int(mp.floor(C))
    print(f'    g={g}: C_g={mp.nstr(C,13)} floor={fl}; at floor: {mp.nstr(fl+1-2*g*mp.sqrt(fl),6)} ; at floor+1: {mp.nstr(fl+2-2*g*mp.sqrt(fl+1),6)}')
print('    reader sharpening: d_p d_q <= C_g for ALL p != q with d_q >= 1 gives d_p <= C_g for EVERY p (not "all but one").')

print('\n[O5] N <= 10^5 with log N / kappa an integer (tolerance 1e-20 at 30 digits)')
for name, kap in (('1', mp.mpf(1)), ('log2', mp.log(2)), ('log6', mp.log(6)), ('log12', mp.log(12))):
    hits = [N for N in range(2, 10**5+1) if abs(mp.log(N)/kap - mp.nint(mp.log(N)/kap)) < mp.mpf('1e-20')]
    print(f'    kappa={name}: {len(hits)} hits: {hits[:17]}')
print('    dist(e^m, Z), m=1..12:', ' '.join(mp.nstr(abs(mp.e**m - mp.nint(mp.e**m)),4) for m in range(1, 13)))

print('\n[O6] Corollary 3.1 lemma: N^b = M^a (a,b>=1) => supp N = supp M; brute force N,M <= 3000, a,b <= 6 via exponent vectors')
cnt = mis = 0
fac = {n: factorint(n) for n in range(2, 3001)}
for N in range(2, 3001):
    for M in range(2, 3001):
        fN, fM = fac[N], fac[M]
        if set(fN) != set(fM):
            # N^b = M^a impossible when supports differ: check directly for small a,b
            continue
        for a in range(1, 7):
            for b in range(1, 7):
                if all(fN[l]*b == fM[l]*a for l in fN): cnt += 1
# direct check of the implication on all pairs with differing supports, via logs (no equality should occur)
viol = 0
for N in range(2, 400):
    for M in range(2, 400):
        if set(fac[N]) != set(fac[M]):
            for a in range(1, 7):
                for b in range(1, 7):
                    if N**b == M**a: viol += 1
print(f'    equal-support pairs with N^b = M^a: {cnt}; differing-support pairs (N,M<400) with N^b = M^a: {viol}')

print('\n[O7] ghost lattice L_N on [1,N]: index computed by BFS in the finite quotient; v_d basis; N!*e_n membership')
def moduli(N):
    cons = []
    for p in primerange(2, N+1):
        for j in range(1, N//p+1):
            v = 0; jj = j
            while jj % p == 0: jj //= p; v += 1
            cons.append((j, p*j, p**(1+v)))
    return cons
def in_L(a, N):
    return all((a[j-1]-a[pj-1]) % m == 0 for j, pj, m in moduli(N))
def index_L(N):
    cons = moduli(N)
    gens = []
    for n in range(1, N+1):
        gens.append(tuple(((1 if j == n else 0) - (1 if pj == n else 0)) % m for j, pj, m in cons))
    mods = [m for _, _, m in cons]
    zero = tuple(0 for _ in mods); seen = {zero}; frontier = [zero]
    while frontier:
        nf = []
        for x in frontier:
            for g in gens:
                y = tuple((xi+gi) % m for xi, gi, m in zip(x, g, mods))
                if y not in seen: seen.add(y); nf.append(y)
        frontier = nf
    return len(seen), math.prod(mods)
for N in range(1, 9):
    idx, prod = index_L(N)
    vs = [[d if j % d == 0 else 0 for j in range(1, N+1)] for d in range(1, N+1)]
    allv = all(in_L(v, N) for v in vs)
    det = abs(Matrix(vs).det()) if N > 0 else 1
    fe = all(in_L([math.factorial(N) if j == n else 0 for j in range(1, N+1)], N) for n in range(1, N+1))
    print(f'    N={N}: index(L_N)={idx}  prod moduli={prod}  N!={math.factorial(N)}  v_d in L_N: {allv}  det(v_d)={det}  N!e_n in L_N: {fe}')
for N in range(9, 41):
    ok = all(in_L([math.factorial(N) if j == n else 0 for j in range(1, N+1)], N) for n in range(1, N+1))
    okv = all(in_L([d if j % d == 0 else 0 for j in range(1, N+1)], N) for d in range(1, N+1))
    pm = math.prod(m for _, _, m in moduli(N))
    if not (ok and okv and pm == math.factorial(N)): print('    FAIL at N', N)
print('    N=9..40: N!e_n in L_N, v_d in L_N, prod moduli = N!: all True unless FAIL printed')
print('    zero-divisor: f in ker w_n, g = N! e_n: (f*g)_j = f_j g_j = 0 for all j since f_n = 0 and g_j = 0 (j != n); g != 0.')
# local version: for s with s_n != 0 (s outside the prime P over a prime of Z through Gamma_n), s*g = s_n N! e_n != 0.
print('    local version: s*g = s_n * N! * e_n != 0 whenever s_n != 0, so g survives localization at every prime of Gamma_n.')

print('\n[O7b] box levels F_b and J = prod p^(1+b_p): J e_n in L_F')
def box(b):
    F = [1]
    for p, e in b.items(): F = [f*p**k for f in F for k in range(e+1)]
    return sorted(F)
def in_LF(a, F):
    S = set(F)
    for j in F:
        for p in factorint(j*1).keys() | set(pp for f in F for pp in factorint(f)):
            if j*p in S:
                v = 0; jj = j
                while jj % p == 0: jj //= p; v += 1
                if (a[j]-a[j*p]) % p**(1+v): return False
    return True
for b in ({2: 2, 3: 1}, {2: 3, 3: 2, 5: 1}, {2: 1, 3: 1, 5: 1, 7: 1}, {2: 4}, {3: 2, 7: 1}):
    F = box(b); J = math.prod(p**(1+e) for p, e in b.items())
    Jmin = math.prod(p**e for p, e in b.items())
    ok = all(in_LF({j: (J if j == n else 0) for j in F}, F) for n in F)
    okmin = all(in_LF({j: (Jmin if j == n else 0) for j in F}, F) for n in F)
    print(f'    b={b}: |F|={len(F)} J={J}: {ok};  (reader: the smaller J\'=prod p^b_p={Jmin} also works: {okmin})')

print('\n[O8] rung 1: y^2 = x^3 + x + 1 over F_7, counted from scratch')
q = 7
aff = sum(1 for x in range(q) for y in range(q) if (y*y - (x**3 + x + 1)) % q == 0)
N1 = aff + 1; t = q + 1 - N1
# alpha, beta roots of T^2 - t T + q; N_k = q^k + 1 - (alpha^k + beta^k); s_k = alpha^k+beta^k via recursion
s = [2, t]
for k in range(2, 6): s.append(t*s[-1] - q*s[-2])
Nk = {k: q**k + 1 - s[k] for k in range(1, 5)}
def mobius(n):
    f = factorint(n); return 0 if any(e > 1 for e in f.values()) else (-1)**len(f)
ad = {d: sum(mobius(d//e)*Nk[e] for e in range(1, d+1) if d % e == 0)//d for d in range(1, 5)}
print(f'    #E(F_7) = {N1} (trace t = {t}); N_k = {Nk}; closed points of degree d: {ad}')
print('    fiber products q^{N_N}: support {7}; Q-span of the diagonal row = Q (dim 1): Theorem R silent (one residue characteristic).')
print('    Weil check |N_k - q^k - 1| <= 2 g q^(k/2), g=1:', all(abs(Nk[k]-q**k-1) <= 2*mp.sqrt(q)**k for k in Nk))
print('    A8 on rung 1 (Milne Ex. 1.7, C1=C2=S, f of degree d): (Gamma_f)^2 = -(2g-2) d; g=1 -> 0 for Delta and Frobenius; g=2, d=q=7 ->', -(2*2-2)*7, '= q(2-2g) =', 7*(2-4))

print('\n[O9] zeros of zeta with 0 < Im <= 100:', mp.nzeros(100), '; first:', [mp.nstr(mp.im(mp.zetazero(k)), 10) for k in range(1, 6)])

print('\n[O10] psi(x) - x')
acc = mp.mpf(0); marks = {10**k for k in range(2, 7)}; out = []
for n in range(2, 10**6+1):
    f = factorint(n) if n < 50 else None
for x in sorted(marks):
    pass
# fast psi via sieve
X = 10**6
spf = list(range(X+1))
for i in range(2, int(X**0.5)+1):
    if spf[i] == i:
        for j in range(i*i, X+1, i):
            if spf[j] == j: spf[j] = i
acc = 0.0; import math as m_
for n in range(2, X+1):
    p = spf[n]; k = n
    while k % p == 0: k //= p
    if k == 1: acc += m_.log(p)
    if n in marks: out.append((n, acc - n, (acc - n)/m_.sqrt(n)))
for n, d, r in out: print(f'    x={n}: psi-x={d:.7f}  (psi-x)/sqrt(x)={r:.6f}')

print('\n[O11] route (a) base-1 coefficient lemma: exp-polynomial uniqueness, randomized')
random.seed(35)
worst = mp.inf
for trial in range(200):
    s_ = random.randint(2, 7)
    lam = [mp.mpc(random.uniform(-3, 3), random.uniform(-3, 3)) for _ in range(s_)]
    M = mp.matrix([[l**k for l in lam] for k in range(1, s_+1)])
    worst = min(worst, abs(mp.det(M)))
print('    min |det(lambda_j^k)| over 200 random distinct nonzero sets:', mp.nstr(worst, 5), '(nonzero => coefficients vanish)')
# the injective identity at p: log p/kappa = 1 + d^k - sum chi_i^k for all k>=1 -> the coefficient at base 1 is an integer <= 2
print('    consequence: log p/kappa in Z_{<=2}; kappa=1 fails at p=11 (log 11 =', mp.nstr(mp.log(11), 10), ')')

print('\n[O12] Theorem R illustration: random FINITE fibers on prime powers <= 2000; Q-rank of {log N_D} = rank of exponent matrix')
pp = [n for n in range(2, 2001) if len(factorint(n)) == 1]
primes = list(primerange(2, 2001))
for trial in range(3):
    random.seed(100+trial)
    nf = random.choice([5, 20, 60])
    fib = {}
    for n in pp: fib.setdefault(random.randrange(nf), []).append(n)
    rows = []
    for D, mem in fib.items():
        v = {}
        for n in mem:
            p = list(factorint(n))[0]; v[p] = v.get(p, 0) + 1
        rows.append([v.get(p, 0) for p in primes])
    r = Matrix(rows).rank()
    maxsupp = max(sum(1 for x in row if x) for row in rows)
    print(f'    {nf} fibers: rank={r}; primes covered={len(primes)}; max support per fiber={maxsupp}; rank*maxsupp >= #primes: {r*maxsupp >= len(primes)}')
print('    (with finitely many fibers the supports are unbounded as the range grows -> Lemma F(a) forbids; with finite fibers, rank -> infinity)')

print('\n[O13] DH witness (carried by the NOTE, recomputed by the reader): Lambda_DH(n) from a_n log n = sum_{d|n} Lambda(d) a_{n/d}')
kap = (mp.sqrt(10-2*mp.sqrt(5))-2)/(mp.sqrt(5)-1)
def a(n): return [0, 1, kap, -kap, -1][n % 5]
LD = {}
for n in range(1, 40):
    if n == 1: LD[1] = mp.mpf(0); continue
    s = a(n)*mp.log(n) - mp.fsum(LD[d]*a(n//d) for d in range(1, n) if n % d == 0 and d > 1)
    LD[n] = s  # a(1) = 1
print('    kappa =', mp.nstr(kap, 13), '; Lambda_DH(3) =', mp.nstr(LD[3], 10), '; Lambda_DH(4) =', mp.nstr(LD[4], 10), '; Lambda_DH(12) =', mp.nstr(LD[12], 13))
print('\nEND', datetime.datetime.now().isoformat())
