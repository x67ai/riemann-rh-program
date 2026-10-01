# U1-lookahead: independent brute-force check of the greedy threshold rule (no blocks, 50-digit arithmetic).
# S = all g-integers <= X generated so far (products of the primes placed so far); sweep in increasing order;
# a prime is placed at xs = 1 + (n - 1 + tau)/rho whenever the next element of S lies beyond xs (n = count processed).
# Usage: python3 validate_bf.py RHO_EXPR X TAU
import sys, bisect
from mpmath import mp, mpf, pi
mp.dps = 50
rho = eval(sys.argv[1], {"pi": pi, "mpf": mpf}); X = mpf(sys.argv[2]); tau = mpf(sys.argv[3])
S = [mpf(1)]; n = 0; primes = []; supE = mpf(-1); infEm = mpf(10); pos = 0
def add_prime(p):
    new = []
    for m in list(S):                       # S_old is complete up to X for the old primes
        v = m * p
        while v <= X:
            new.append(v); v *= p
    for v in new: bisect.insort(S, v)
while True:
    xs = 1 + (n - 1 + tau) / rho if n > 0 else None
    nxt = S[pos] if pos < len(S) else None
    if n == 0:                               # the unit 1
        n = 1; pos = 1; continue
    if nxt is not None and nxt <= xs:
        infEm = min(infEm, (n) - (rho * (nxt - 1) + 1)); n += 1; pos += 1
        supE = max(supE, n - (rho * (nxt - 1) + 1)); continue
    if xs > X: break
    primes.append(xs); add_prime(xs)          # xs itself is now in S at index pos (all new products exceed xs)
    infEm = min(infEm, n - (rho * (xs - 1) + 1)); n += 1; pos += 1
    supE = max(supE, n - (rho * (xs - 1) + 1))
print(f"BF rho={mp.nstr(rho, 12)} X={sys.argv[2]} tau={sys.argv[3]}: N={n} pi={len(primes)} supE={mp.nstr(supE, 8)} infE(x-)={mp.nstr(infEm, 8)}")
