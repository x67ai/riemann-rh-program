# Orchestrator's pre-derivation checks (Session 36, 2026-09-30). Python 3 + numpy + mpmath.
# [P1] Theorem S bound: sup{L : (1+x-L)^2 <= 4g^2 x, (1+x^2-L)^2 <= 4g^2 x^2} = (1+2g)(1+r_g), r_g=(1+sqrt(1+8g))/2
# [P2] norm-clause form: (1+n-Lambda(n)/kappa)^2 <= 4 g^2 n fails for every finite g at some n
# [P3] Prop B: a regrading of the rational primes with base d=2, kappa=1: blocks, eps_N, positive definiteness
import math, numpy as np
from sympy import primerange, factorint

print('[P1] Theorem S bound')
for g in [0.0, 0.25, 0.5, 1.0, 2.0, 5.0, 10.0, 50.0]:
    r = (1 + math.sqrt(1 + 8*g))/2
    bound = (1 + 2*g)*(1 + r)
    # brute force: for x on a fine grid, feasible L-interval is the intersection of
    # [1+x-2g sqrt x, 1+x+2g sqrt x] and [1+x^2-2g x, 1+x^2+2g x]
    best = -1e9
    xs = np.linspace(0, (r**2)*1.5 + 2, 400001)
    lo = np.maximum(1 + xs - 2*g*np.sqrt(xs), 1 + xs**2 - 2*g*xs)
    hi = np.minimum(1 + xs + 2*g*np.sqrt(xs), 1 + xs**2 + 2*g*xs)
    feas = hi >= lo - 1e-12
    best = hi[feas].max()
    print(f'  g={g:6.2f}  r_g={r:.6f}  closed form {(bound):.6f}  brute-force sup {best:.6f}  max feasible x {xs[feas].max():.4f} (r_g^2={r*r:.4f})')
    # largest prime allowed at kappa = 1
print('  kappa=1, g=1: log p <= 9  ->  p <=', int(math.exp(9)))

print('[P2] norm clause: smallest g allowed by n (kappa=1), g >= |1+n-Lambda(n)|/(2 sqrt n)')
def Lam(n):
    f = factorint(n)
    return math.log(list(f)[0]) if len(f) == 1 else 0.0
for n in [2, 3, 4, 6, 10, 30, 210, 2310, 10**6, 2**20, 2**40]:
    print(f'  n={n:>14d}  Lambda={Lam(n):.4f}  g >= {abs(1+n-Lam(n))/(2*math.sqrt(n)):.4f}')

print('[P3] Prop B: regrading with d=2, kappa=1')
d, kappa, NMAX = 2, 1.0, 22
primes = list(primerange(2, 40_000_000))
logs = [math.log(p) for p in primes]
idx = 0
w = {}      # block sums
blocks = {}
L = {}
eps = {}
for N in range(1, NMAX+1):
    target_L = kappa*(1 + d**N)
    lower = sum(w[e] for e in range(1, N) if N % e == 0)
    target_w = target_L - lower
    s, blk = 0.0, []
    # greedy: take consecutive primes while the block sum stays <= target, then take one more if it brings the sum closer
    while idx < len(primes) and s + logs[idx] <= target_w:
        s += logs[idx]; blk.append(primes[idx]); idx += 1
    if idx < len(primes) and abs(s + logs[idx] - target_w) < abs(s - target_w):
        s += logs[idx]; blk.append(primes[idx]); idx += 1
    assert idx < len(primes), 'ran out of primes'
    w[N], blocks[N] = s, blk
    L[N] = lower + s
    eps[N] = 1 + d**N - L[N]/kappa
    print(f'  N={N:2d} #block={len(blk):7d} first={blk[0] if blk else None} last={blk[-1] if blk else None} w_N={s:.6f} L_N={L[N]:.6f} eps_N={eps[N]:+.6f} e_N=eps_N d^(-N/2)={eps[N]*d**(-N/2):+.3e}')
tail = sum(2*abs(eps[N])*d**(-N/2) for N in range(1, NMAX+1))
print('  sum_{N<=%d} 2|e_N| = %.6f  -> any 2g >= this (plus the tail) makes the Toeplitz form diagonally dominant' % (NMAX, tail))
for twog in [tail*1.05, 2.0, 4.0]:
    e = [twog] + [eps[N]*d**(-N/2) for N in range(1, NMAX+1)]
    T = np.array([[e[abs(a-b)] for b in range(NMAX+1)] for a in range(NMAX+1)])
    ev = np.linalg.eigvalsh(T)
    print(f'  2g={twog:.4f}: min eigenvalue of the (N<={NMAX}) Toeplitz matrix e_|a-b| = {ev.min():+.6f}, max = {ev.max():.6f}')
# the actual Gram matrix W(a,b) = d^{min(a,b)} eps_{|a-b|}, W(a,a) = 2g d^a, on gamma_0..gamma_NMAX
twog = tail*1.05
W = np.array([[ (twog*d**a if a==b else d**min(a,b)*eps[abs(a-b)]) for b in range(NMAX+1)] for a in range(NMAX+1)], dtype=float)
D = np.diag([d**(-a/2) for a in range(NMAX+1)])
print('  scaled Gram D W D min eigenvalue:', np.linalg.eigvalsh(D@W@D).min())
# Weil inequality per N: |1 + d^N - L_N/kappa| <= 2g d^{N/2}
print('  Weil inequality check: max_N |eps_N|/d^{N/2} =', max(abs(eps[N])*d**(-N/2) for N in eps), ' vs 2g =', twog)
# Q-rank sanity: every prime used once
used = [p for N in blocks for p in blocks[N]]
print('  primes used:', len(used), 'distinct:', len(set(used)), 'largest:', max(used))
