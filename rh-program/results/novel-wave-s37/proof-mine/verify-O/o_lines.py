# Opus reader, independent route (no import from ../verify). Exact integer / Fraction arithmetic.
# (q, t) = (5, 5) virtual curve V and (5, 4) control E0. Lines A, B, D here; C and brute force in o_fields.py.
from fractions import Fraction as Fr
import math

def mobius(n):
    r, m, p = 1, n, 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0: return 0
            r = -r
        p += 1
    return -r if m > 1 else r

def powersums(q, t, n):          # a_k = alpha^k + beta^k, a_k = t a_{k-1} - q a_{k-2}
    a = [2, t]
    while len(a) <= n: a.append(t * a[-1] - q * a[-2])
    return a

def counts(q, t, n):
    a = powersums(q, t, n)
    N = [None] + [q**k + 1 - a[k] for k in range(1, n + 1)]
    b = [None]
    for d in range(1, n + 1):
        s = sum(mobius(d // e) * N[e] for e in range(1, d + 1) if d % e == 0)
        assert s % d == 0; b.append(s // d)
    return a, N, b

# Z[pi] element x0 + x1*pi, pi^2 = t pi - q. norm = x * x' with x' = x0 + x1 * (t - pi).
def mul(x, y, q, t):
    c0 = x[0]*y[0] - q*x[1]*y[1]; c1 = x[0]*y[1] + x[1]*y[0] + t*x[1]*y[1]
    return (c0, c1)
def norm(x, q, t):               # deg(x0 + x1 pi) = x0^2 + t x0 x1 + q x1^2
    return x[0]**2 + t*x[0]*x[1] + q*x[1]**2
def pipow(n, q, t):
    r = (1, 0)
    for _ in range(n): r = mul(r, (0, 1), q, t)
    return r

def charpoly(M):                  # Faddeev-LeVerrier over Fractions: det(xI - M) coefficients, leading first
    n = len(M); I = [[Fr(int(i == j)) for j in range(n)] for i in range(n)]
    Mk = [[Fr(0)]*n for _ in range(n)]; c = [Fr(1)]
    for k in range(1, n + 1):
        A = [[sum(M[i][l]*Mk[l][j] for l in range(n)) + (c[-1] if i == j else 0) for j in range(n)] for i in range(n)]
        Mk = A
        AM = [[sum(M[i][l]*A[l][j] for l in range(n)) for j in range(n)] for i in range(n)]
        c.append(-sum(AM[i][i] for i in range(n)) / k)
    return c

def inertia(M):                   # symmetric => real-rooted char poly => Descartes is exact
    c = charpoly(M)
    while c and c[-1] == 0: c = c[:-1]           # strip zero eigenvalues
    sgn = lambda cs: sum(1 for u, v in zip([x for x in cs if x != 0], [x for x in cs if x != 0][1:]) if u*v < 0)
    pos = sgn(c); neg = sgn([x * (-1)**(len(c)-1-i) for i, x in enumerate(c)])
    return pos, neg

def gram(q, t, graphs):           # basis C1, C2, Gamma_{pi^i} (i in graphs); g = 1
    B = ['C1', 'C2'] + [('G', i) for i in graphs]
    def dot(u, v):
        if u == v and u in ('C1', 'C2'): return 0
        if {u, v} == {'C1', 'C2'}: return 1
        if 'C1' in (u, v):             # C1 . Gamma_f = deg f (Milne Ex. 1.7 convention d1 = deg f)
            w = v if u == 'C1' else u; return q**w[1]
        if 'C2' in (u, v): return 1
        x, y = pipow(u[1], q, t), pipow(v[1], q, t)
        return norm((x[0]-y[0], x[1]-y[1]), q, t)   # Gamma_phi . Gamma_psi = deg(phi - psi), g = 1
    return [[Fr(dot(u, v)) for v in B] for u in B]

def main():
    for name, (q, t) in {'V': (5, 5), 'E0': (5, 4)}.items():
        a, N, b = counts(q, t, 60)
        print(f'== {name} (q, t) = ({q}, {t})')
        print('  N_1..8 =', N[1:9], ' b_1..8 =', b[1:9], ' min N, min b (<=60):', min(N[1:]), min(b[1:]))
        print('  A: inertia <C1,C2,Delta,Gamma_pi> =', inertia(gram(q, t, [0, 1])),
              '; <C1,C2,Gamma_pi^0..3> =', inertia(gram(q, t, [0, 1, 2, 3])))
        d = lambda m, n: 2*(m*m + t*m*n + q*n*n)                       # def(m Delta + n Gamma_pi)
        print('  A: def(Gamma_pi - 2 Delta) =', d(-2, 1), '; Cor 1.6 |N_1 - q - 1| =', abs(N[1]-q-1), 'vs 2 sqrt q =', round(2*math.sqrt(q), 4))
        print('  A: CS on span(Delta, Gamma_pi^n) violated for n in', [n for n in range(1, 13) if a[n]**2 > 4*q**n])
        print('  D: deg(pi - 2) =', norm((-2, 1), q, t), '; deg(pi - 1) =', norm((-1, 1), q, t), '= N_1')
        # Rosati by matrices: pi ~ companion M, pi-dagger = adj(M) (M adj M = q I); trace((M-2)(adj M-2))
        M = [[0, -q], [1, t]]; adj = [[t, q], [-1, 0]]
        X = [[M[0][0]-2, M[0][1]], [M[1][0], M[1][1]-2]]; Y = [[adj[0][0]-2, adj[0][1]], [adj[1][0], adj[1][1]-2]]
        tr = sum(X[i][k]*Y[k][i] for i in range(2) for k in range(2))
        print('  D: Tr((pi-2)(pi-2)^dagger) =', tr)
        # B: Weil I (7.1) on H^2(C x C): eigenvalues alpha^2, alpha*beta, beta^2, q, q. Exact test via squares.
        disc = t*t - 4*q
        if disc > 0:   # real roots (t +- sqrt(disc))/2; alpha^2 > q^{3/2} <=> alpha^4 > q^3 (exact in Q(sqrt disc))
            al = (t + math.sqrt(disc))/2; be = q/al
            print(f'  B: alpha^2 = {al*al:.4f}, beta^2 = {be*be:.4f} vs [q^0.5, q^1.5] = [{q**0.5:.4f}, {q**1.5:.4f}]')
            print(f'  B: Rankin |alpha|^(2k) <= q^(k+1): k=1 {al**2:.3f} <= {q**2}: {al**2 <= q**2}; k=2 {al**4:.3f} <= {q**3}: {al**4 <= q**3}')
        else:
            print(f'  B: |alpha|^2 = {q} in [{q**0.5:.4f}, {q**1.5:.4f}]; Rankin 5^k <= 5^(k+1) all k')

if __name__ == '__main__':
    main()
