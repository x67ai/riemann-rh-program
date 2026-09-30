# Opus reader, independent route. Line C (Bombieri Thm 1 (5), (7), twists) and brute force in F_{5^n}.
import itertools, math
from o_lines import counts, powersums

P = 5
def fp_poly_mod(a, m):            # a, m: coefficient lists low->high over F_5, m monic
    a = a[:]
    while len(a) >= len(m):
        c = a[-1] % P
        if c:
            s = len(a) - len(m)
            for i, mi in enumerate(m): a[s+i] = (a[s+i] - c*mi) % P
        a.pop()
    return a + [0]*(len(m)-1-len(a))
def irreducible(n):               # first monic degree-n poly with no root / no factor (n <= 4: check deg <= n/2 factors)
    for tail in itertools.product(range(P), repeat=n):
        m = list(tail) + [1]
        if m[0] == 0: continue
        ok = True
        for d in range(1, n//2 + 1):
            for f in itertools.product(range(P), repeat=d):
                if not ok: break
                g = list(f) + [1]
                if not any(fp_poly_mod(m, g)): ok = False
        if ok: return m
class F:
    def __init__(s, n):
        s.n, s.m = n, irreducible(n)
        s.elts = [tuple(e) for e in itertools.product(range(P), repeat=n)]
    def mul(s, a, b):
        prod = [0]*(2*s.n-1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b): prod[i+j] = (prod[i+j] + x*y) % P
        return tuple(fp_poly_mod(prod, s.m))
    def add(s, a, b): return tuple((x+y) % P for x, y in zip(a, b))
    def const(s, c): return tuple([c % P] + [0]*(s.n-1))

def count_curve(K, A, B, D):      # D*y^2 = x^3 + A x + B over K (A, B, D in K); includes the point at infinity
    sq = {}
    for y in K.elts:
        v = K.mul(D, K.mul(y, y)); sq[v] = sq.get(v, 0) + 1
    tot = 1
    for x in K.elts:
        rhs = K.add(K.add(K.mul(K.mul(x, x), x), K.mul(A, x)), B)
        tot += sq.get(rhs, 0)
    return tot
def nonsquare(K):
    sqs = {K.mul(y, y) for y in K.elts}
    return next(e for e in K.elts if e not in sqs)

def brute():
  for n in (1, 2, 4):
      K = F(n); d = nonsquare(K); one = K.const(1)
      e0 = count_curve(K, K.const(2), K.const(0), one); tw = count_curve(K, K.const(2), K.const(0), d)
      print(f'F_{P**n} (mod poly {K.m}): #E0 = {e0}, #E0^twist = {tw}, sum = {e0+tw} = 2(Q+1)? {e0+tw == 2*(P**n+1)}')

def bombieri(Q, g):               # Thm 1 (5) bound and (7) with the printed parameters (p. 239)
    al = round(math.log(Q, P)); assert P**al == Q and al % 2 == 0
    mu = al // 2; pm = P**mu; m = pm + 2*g; l = (g*pm)//(g+1) + g + 1
    hyp = (l*pm < Q, l >= g and m >= g, (l+1-g)*(m+1-g) > l*pm + m + 1 - g, Q > (g+1)**4)
    b5 = Q + (2*g+1)*math.isqrt(Q) + 1          # (5): nu_1 < b5   (Q an even power: sqrt exact)
    b7 = l + m*Q//pm + 1                          # (7): nu_1 <= b7
    return b5, b7, (mu, m, l), hyp

def lineC():
  print('\nLine C, g = 1: formal twist count = Q + 1 + a_r (= deg(pi_Q + 1)); lower bound 2(Q+1) - (7)')
  for name, t in (('V', 5), ('E0', 4)):
      a, N, b = counts(5, t, 6)
      for r in (2, 4, 6):
          Q = 5**r; b5, b7, par, hyp = bombieri(Q, 1); twist = Q + 1 + a[r]
          print(f'  {name} Q=5^{r}: N={N[r]}, twist={twist}; (5) "<{b5}": N {N[r] < b5}, twist {twist < b5}; '
                f'(7) "<={b7}" (mu,m,l)={par} hyp={all(hyp)}: twist {twist <= b7}; lower bound N >= {2*(Q+1)-b7}: {N[r] >= 2*(Q+1)-b7}')

if __name__ == '__main__':
    brute(); lineC()
