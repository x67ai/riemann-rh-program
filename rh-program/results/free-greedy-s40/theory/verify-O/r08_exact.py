# Opus reader: S8(4/5) in EXACT integer arithmetic (t = 5/4: g-prime with lattice index n is (10n+3)/8).
# A g-integer with j prime factors is A/8^j, A = prod(10 n_i + 3); compared through the key A*8^(J-j).
# Checks NOTE l. 87-91 (no composite on the lattice when the numerator p of t = p/q is odd) and counts
# equal-valued composites (multiplicities), with the first few instances.  Block sweep as in s8dd.c.
import sys, collections
X = int(sys.argv[1]) if len(sys.argv) > 1 else 10**5
J = 48                                   # max number of factors handled (13/8)^48 > 10^10
SC = 8 ** J
def lat_key(N): return (10 * N + 3) * 8 ** (J - 1)          # x*(N) = 1 + (N - 1/2)(5/4) = (10N+3)/8
P = []                                   # (key, n) of g-primes, increasing
N, nties, mult = 1, 0, 0
supE, inst = -1.0, []
thr = lat_key(1); LOk = SC; Xk = X * SC
ratio_num, ratio_den = 13, 8             # p1 = 13/8 exactly; blocks (LO, LO*13/8]
seen = {}
def walk(i0, key, depth, path, HIk, out):
    for i in range(i0, len(P)):
        q = key * P[i][0] // SC          # exact: key*P/SC is an integer key (8^J divides the product of scalings)
        if q > HIk: break
        if depth >= 1 and q > LOk: out.append((q, path + (P[i][1],)))
        walk(i, q, depth + 1, path + (P[i][1],), HIk, out)
while LOk < Xk:
    HIk = min(LOk * ratio_num // ratio_den, Xk)
    out = []; walk(0, SC, 0, (), HIk, out); out.sort()
    for q, path in out:
        while thr < q:                   # deficit reaches 1/2 strictly before the composite: place a prime
            P.append((thr, N)); N += 1; thr = lat_key(N)
        if q == thr: nties += 1          # tie: composite exactly at a deficit time (counted first)
        if q in seen:
            mult += 1
            if len(inst) < 4: inst.append((q / SC, seen[q], path))
        else: seen[q] = path
        N += 1; thr = lat_key(N)
        E = N - 1 - 0.8 * (q / SC - 1); supE = max(supE, E)
    while thr <= HIk:
        P.append((thr, N)); N += 1; thr = lat_key(N)
    LOk = HIk
print(f"S8(4/5) exact to X={X}: N={N} pi={len(P)} supE={supE:.4f} ties={nties} equal-valued composite pairs={mult}")
print("first g-primes (numerators over 8):", [10 * n + 3 for _, n in P[:8]])
for v, a, b in inst:
    print(f"  equal value {v:.6f}: numerators {[10*n+3 for n in a]} and {[10*n+3 for n in b]}")
