# checkK.py -- unit s5-multiplicity-s40, close K: INDEPENDENT checker (second code path; shares no code with fcount/fcert).
# Input: n as "p^e" items, the list file of claimed g-prime divisors of n, the g-prime dump gpF_r08_1e9.u32.
# (1) every listed q divides n, q <= 10^9, and q is in the dump (binary search on the 50,829,666 sorted g-primes);
#     completeness: every divisor d <= 10^9 of n that is in the dump is listed;
# (2) f = #{multisets from the list with product n} modulo three primes ~ 2^31, by a numpy DP on the lattice of n0 = n / (top
#     primes) written as an int64 ndarray of shape (e_1+1, ..., e_r+1) with slice-additions (dimension-by-dimension prefix order),
#     then the top primes by the exponent-1 derivation f(m) = sum_{q in list, p | q | m} f(m/q), recursive with a dict memo;
# (3) compares with the claimed exact value (argument), and tests the K inequality in exact integers:
#     f > (94/25) n^(7/20) + 3   <=>   (25 (f - 3))^20 > 94^20 * n^7.
# Usage: python3 checkK.py gpfile listfile claimed_f "n0 items" "top primes"
import sys, numpy as np, itertools, math, time
gpfile, listfile, claimed = sys.argv[1], sys.argv[2], int(sys.argv[3])
n0items = sys.argv[4].split(); tops = [int(t) for t in sys.argv[5].split()]
P = []; Ex = []
for it in n0items:
    p, _, e = it.partition('^'); P.append(int(p)); Ex.append(int(e) if e else 1)
n0 = 1
for p, e in zip(P, Ex): n0 *= p ** e
n = n0
for t in tops: n *= t
assert all(n0 % t for t in tops) and len(set(tops)) == len(tops)
t0 = time.time()
G = np.fromfile(gpfile, dtype=np.uint32).reshape(-1, 2)
assert (G[:, 1] == 1).all(); G = G[:, 0].astype(np.int64)
L = sorted(set(int(x) for x in open(listfile)))
La = np.array(L, dtype=np.int64)
pos = np.searchsorted(G, La); assert (pos < len(G)).all() and (G[pos] == La).all(), "a listed number is not a g-prime"
assert all(n % q == 0 and 2 <= q <= 10**9 for q in L), "a listed number does not divide n or exceeds 10^9"
# completeness: enumerate divisors <= 1e9 of n
allp = P + tops; alle = Ex + [1] * len(tops)
divs = np.array([1], dtype=np.int64)
for p, e in zip(allp, alle):
    parts = [divs]; cur = divs
    for j in range(e):
        cur = cur[cur <= 10**9 // p] * p
        if len(cur) == 0: break
        parts.append(cur)
    divs = np.concatenate(parts)
divs = divs[divs >= 2]; pos = np.searchsorted(G, divs); pos[pos >= len(G)] = len(G) - 1
ing = divs[G[pos] == divs]
assert sorted(ing.tolist()) == L, "list incomplete or inconsistent"
print(f"list: {len(L)} g-prime divisors, all verified in the dump, complete ({len(divs)} divisors <= 1e9 scanned)  t={time.time()-t0:.0f}s", flush=True)
def vec(q):
    v = []
    for p in P:
        k = 0
        while q % p == 0: q //= p; k += 1
        v.append(k)
    return v, q            # q = leftover (product of top primes dividing it)
pure = []; withtop = {}
for q in L:
    v, rest = vec(q)
    if rest == 1: pure.append(v)
    else: withtop.setdefault(rest, []).append(v)
shape = tuple(e + 1 for e in Ex)
res = []
for MOD in (2147483647, 2147483629, 2147483587):
    f = np.zeros(shape, dtype=np.int64); f[(0,) * len(P)] = 1
    for v in pure:   # unbounded knapsack for one part: f[x] += f[x - v] for x >= v, in increasing order along one dimension j with v_j > 0
        j = next(i for i, c in enumerate(v) if c > 0)
        for lev in range(v[j], Ex[j] + 1):
            dst = tuple(lev if i == j else slice(v[i], None) for i in range(len(P)))
            src = tuple(lev - v[j] if i == j else slice(0, Ex[i] + 1 - v[i]) for i in range(len(P)))
            f[dst] = (f[dst] + f[src]) % MOD
    memo = {}
    def ftop(x, mask):       # f(T * prod_{i in mask} tops[i]), T = exponent vector x (tuple)
        if not mask: return int(f[x])
        key = (x, mask)
        if key in memo: return memo[key]
        i = max(mask); rest = tuple(k for k in mask if k != i); tot = 0
        for r in range(len(rest) + 1):
            for sub in itertools.combinations(rest, r):
                pp = tops[i] * math.prod(tops[k] for k in sub)
                for v in withtop.get(pp, []):
                    if all(a <= b for a, b in zip(v, x)):
                        tot += ftop(tuple(b - a for a, b in zip(v, x)), tuple(k for k in rest if k not in sub))
        memo[key] = tot % MOD; return memo[key]
    val = ftop(tuple(Ex), tuple(range(len(tops))))
    res.append((MOD, val, claimed % MOD)); print(f"mod {MOD}: checker {val}  claimed {claimed % MOD}  {'AGREE' if val == claimed % MOD else 'DISAGREE'}  t={time.time()-t0:.0f}s", flush=True)
ok = all(a == b for _, a, b in res)
K = (25 * (claimed - 3)) ** 20 > 94 ** 20 * n ** 7
print(f"n = {n}\nlog10 n = {math.log10(n):.6f}  claimed f = {claimed}  residues agree: {ok}")
print(f"K inequality f > 3.76 n^0.35 + 3 in exact integers: {K}   (log10 f - log10(3.76 n^0.35) = {math.log10(claimed) - math.log10(3.76) - 0.35*math.log10(n):+.6f})")
