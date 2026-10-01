# Orchestrator's independent re-derivation of the "integer-greedy" system S5(rho) (u-offsurgery-s39 NOTE §2), written
# from the report's description only: g-primes are integers q >= 2 with multiplicities m_q >= 0 chosen greedily, in
# increasing q, so that the g-integer count N(q) tracks rho*(q-1)+1.  The g-integer coefficients a_n are the Dirichlet
# coefficients of prod_q (1 - q^{-s})^{-m_q}, built incrementally (each factor costs O(X/q)).  Output: the running sup of
# |E(x)| = |N(x) - (rho*(x-1)+1)| at decades, local sup-slopes, and the first composite g-primes.
import numpy as np, sys, math
rho = float(sys.argv[1]) if len(sys.argv) > 1 else 0.8
X = int(float(sys.argv[2])) if len(sys.argv) > 2 else 10**6
a = np.zeros(X + 1, dtype=np.float64); a[1] = 1.0
N = 1.0            # N(q-1) running count of g-integers <= q-1 (a[1..q-1] fixed once primes < q are chosen)
m = np.zeros(X + 1, dtype=np.int32)
comp_primes = []
def mult_factor(a, q, k):
    """multiply the coefficient array by (1 - q^{-s})^{-k} = sum_j C(k+j-1, j) q^{-js}, in place; only indices >= q change."""
    if k == 0: return
    # apply (1 - q^{-s})^{-1} k times: a_n += a_{n/q} for n = q, 2q, ... (ascending so that it is the geometric series)
    for _ in range(k):
        for n in range(q, X + 1, q):
            a[n] += a[n // q]
for q in range(2, X + 1):
    # a[q] currently = number of g-integers equal to q built from primes < q; choose m_q to make N(q) closest to target
    target = rho * (q - 1) + 1
    base = N + a[q]                      # N(q) with m_q = 0
    best_k, best_err = 0, abs(base - target)
    k = 1
    while True:
        # with multiplicity k the coefficient at q gains exactly k (from q^1 with the k-fold factor: C(k,1)=k... plus nothing else at q)
        err = abs(base + k - target)
        if err < best_err: best_k, best_err = k, err
        else: break
        k += 1
    if best_k > 0:
        m[q] = best_k; mult_factor(a, q, best_k)
        if any(q % d == 0 for d in range(2, int(math.isqrt(q)) + 1)) and len(comp_primes) < 12: comp_primes.append(q)
    N += a[q]
cum = np.cumsum(a)
E = cum[1:] - (rho * (np.arange(1, X + 1) - 1) + 1)
x = np.arange(1, X + 1)
print(f"rho = {rho}, X = {X}; #g-primes = {(m>0).sum()}, total multiplicity = {m.sum()}, first composite g-primes = {comp_primes}")
print("primes <= X refused (m_p = 0):", sum(1 for p in range(2, X+1) if m[p]==0 and all(p % d for d in range(2, int(math.isqrt(p))+1))), " of", sum(1 for p in range(2, X+1) if all(p % d for d in range(2, int(math.isqrt(p))+1))))
sup = np.maximum.accumulate(np.abs(E))
for k in range(2, int(math.log10(X)) + 1):
    xi = 10**k; print(f"  x = 1e{k}: running sup|E| = {sup[xi-1]:.3f}   N(x) = {cum[xi]:.0f}  rho*x = {rho*xi:.0f}")
ks = list(range(3, int(math.log10(X)) + 1))
for k in ks[:-1]:
    s1, s2 = sup[10**k - 1], sup[10**(k+1) - 1]
    print(f"  sup-slope on [1e{k}, 1e{k+1}]: {math.log10(s2/s1):.3f}")
# sanity at rho = 1: the rational primes exactly?
if abs(rho - 1) < 1e-12:
    print("  rho = 1 check: max|a_n - 1| =", np.abs(a[1:] - 1).max(), " composite g-primes:", comp_primes)
# route 1 for alpha: the Chebyshev function psi(x) = sum_{q^k <= x} m_q log q, and the running sup of |psi(x) - x|
psi = np.zeros(X + 1)
for q in range(2, X + 1):
    if m[q]:
        qk = q
        while qk <= X:
            psi[qk] += m[q] * math.log(q); qk *= q
psi = np.cumsum(psi)
D = psi[1:] - x
supD = np.maximum.accumulate(np.abs(D))
for k in range(3, int(math.log10(X)) + 1):
    xi = 10**k; print(f"  x = 1e{k}: psi(x) - x = {D[xi-1]:.1f}   running sup|psi - x| = {supD[xi-1]:.1f}   local exponent log10(sup)/k = {math.log10(supD[xi-1])/k:.3f}")
for k in range(3, int(math.log10(X))):
    print(f"  alpha-slope (sup|psi-x|) on [1e{k}, 1e{k+1}]: {math.log10(supD[10**(k+1)-1]/supD[10**k-1]):.3f}")
