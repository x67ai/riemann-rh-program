# Opus reader, independent route: the genus-2 twin V2 and the box search. Exact integers (Newton identities).
import math, numpy as np
from o_lines import mobius
from o_fields import bombieri

q = 5
def data(a1, a2, n=40):
    # L(u) = 1 + a1 u + a2 u^2 + q a1 u^3 + q^2 u^4 = prod (1 - alpha_i u); e_k = (-1)^k coeff_k
    e = [1, -a1, a2, -q*a1, q*q]
    s = [4]                                     # Newton: s_k = sum_{i<k} (-1)^(i) e_{i+1}... explicit:
    for k in range(1, n+1):
        top = k - 1 if k <= 4 else 4
        v = sum((-1)**(i-1) * e[i] * s[k-i] for i in range(1, top+1))
        if k <= 4: v += (-1)**(k-1) * k * e[k]
        s.append(v)
    N = [None] + [q**k + 1 - s[k] for k in range(1, n+1)]
    b = [None]
    for d in range(1, n+1):
        t = sum(mobius(d//f) * N[f] for f in range(1, d+1) if d % f == 0)
        b.append(t // d if t % d == 0 else None)
    return s, N, b

s, N, b = data(-1, 11)
print('V2: L = 1 - u + 11u^2 - 5u^3 + 25u^4; h = L(1) =', 1 - 1 + 11 - 5 + 25)
print('  N_1..6 =', N[1:7], ' b_1..6 =', b[1:7])
print('  min N_n, min b_d (<= 40):', min(N[1:]), min(x for x in b[1:]), ' all b_d integers:', all(x is not None for x in b[1:]))
r = np.roots([25, -5, 11, -1, 1])                 # roots u of L; reciprocal roots alpha = 1/u
al = sorted(abs(1/r)); print('  |alpha_i| =', [round(x, 4) for x in al], ' sqrt q =', round(math.sqrt(q), 4))
print('  Re s of zeros (u = q^-s):', sorted({round(-math.log(abs(x))/math.log(q), 4) for x in r}))
print('  x-poly x^2 + a1 x + (a2 - 2q) = x^2 - x + 1, disc =', 1 - 4*1, '(< 0: non-real x_i, RH false)')
for rr in (2, 4, 6, 8):
    Q = q**rr
    try: b5, b7, par, hyp = bombieri(Q, 2)
    except AssertionError: continue
    print(f'  Q=5^{rr}: N-Q-1 = {N[rr]-Q-1}; Thm 1 hyp Q>(g+1)^4={Q > 81}, (7) hyp {all(hyp[:3])}; '
          f'(5) N < {b5}: {N[rr] < b5}; (7) N <= {b7}: {N[rr] <= b7}')

# Box search: |a1| <= 20, |a2| <= 60; non-real x_i; N_n >= 0, b_d >= 0 integers (n, d <= 40); h >= 1.
hits = []
for a1 in range(-20, 21):
    for a2 in range(-60, 61):
        if a1*a1 - 4*(a2 - 2*q) >= 0: continue
        h = 1 + a1 + a2 + q*a1 + q*q
        if h < 1: continue
        s_, N_, b_ = data(a1, a2)
        if min(N_[1:]) < 0 or any(x is None or x < 0 for x in b_[1:]): continue
        hits.append((a1, a2, h))
print('box hits:', len(hits), '; first 5 by (|a1|, a1, |a2|):', sorted(hits, key=lambda x: (abs(x[0]), x[0], abs(x[1])))[:5])
print('(-1, 11) in hits:', any(x[:2] == (-1, 11) for x in hits))
# which hits violate Bombieri Thm 1 (5) at Q = 5^4 or 5^6 or 5^8 (one-sided test)
caught = [x for x in hits if any(data(x[0], x[1], 8)[1][rr] >= bombieri(q**rr, 2)[0] for rr in (4, 6, 8))]
print('hits caught by Thm 1 (5) at some Q in {5^4, 5^6, 5^8}:', len(caught), 'of', len(hits))
