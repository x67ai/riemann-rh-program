# lyap.py — U7-patterns: candidate potentials for e_k on a contiguous slice of cells (exact multiscale data from s8gen).
# usage: python3 lyap.py prefix D tau delta x_start ncells
# Computes on the slice: E_q(k) = E(x_k/p_q) (q = 1..4, exact via divisibility counts, identity (I1)), the rough walks
# r1 (arrivals not divisible by p1, service 1 - 1/p1) and rU (arrivals divisible by none of p1..p4, service 1 - sum 1/p_q),
# then: least-squares R^2 of e on (1, E_1..E_4); slack of the proved bounds B1 = E_1 + tau + r1 and BU = sum_q (E_q + tau) + rU;
# fraction of cells where each bound is within 1 of e; and the best single weight a with e <= a*E_1 + tau + r1 (a = 1 is proved).
import sys, math, numpy as np
pre, D, tau, delta, xs, n = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]), int(sys.argv[6])
rho = math.pi / D; t = 1 / rho
k0 = int(math.floor((xs - 1) * rho + 1 - tau))          # first cell of the slice (1-based)
mm = lambda suf: np.memmap(pre + suf, np.uint8, 'r')
c, e, c1 = mm('.c.u8'), mm('.e.u8'), mm('.c1.u8')
d = {1: c1, 2: mm('.d2.u8'), 3: mm('.d3.u8'), 4: mm('.d4.u8')}
s = {1: mm('.s1.u8'), 2: mm('.s2.u8'), 3: mm('.s3.u8')}
pk = np.memmap(pre + '.primes.u32', np.uint32, 'r'); p = {q: 1 + (float(pk[q-1]) - 1 + tau) * t - delta for q in range(1, 5)}
def prefix(a, upto):                                       # sum of a[0:upto] in chunks
    tot = 0; B = 1 << 26
    for i in range(0, upto, B): tot += int(np.asarray(a[i:min(i + B, upto)]).sum(dtype=np.int64))
    return tot
lo, hi = k0 - 1, k0 - 1 + n                                # array indices of the slice
k = np.arange(k0, k0 + n, dtype=np.float64); xk = 1 + (k - 1 + tau) * t
E = {}
for q in range(1, 5):
    base = prefix(d[q], lo)
    E[q] = base + np.cumsum(np.asarray(d[q][lo:hi]), dtype=np.int64) - rho * (xk / p[q] - 1)
ev = np.asarray(e[lo:hi]).astype(np.float64); cv = np.asarray(c[lo:hi]).astype(np.float64)
rough1 = cv - np.asarray(c1[lo:hi]); rough4 = rough1 - np.asarray(s[1][lo:hi]) - np.asarray(s[2][lo:hi]) - np.asarray(s[3][lo:hi])
M1 = 1 - 1 / p[1]; SU = 1 - sum(1 / p[q] for q in range(1, 5))
# reflected walks: start the slice with r = 0 after a warm-up of 10^5 cells (discard the warm-up from statistics)
def walk(inc):
    r = np.empty(n); x = 0.0
    for i in range(n):
        x = x + inc[i]
        if x < 0: x = 0.0
        r[i] = x
    return r
r1 = walk(rough1 - M1); rU = walk(rough4 - SU)
w = slice(100000, n)
X = np.column_stack([np.ones(n - 100000)] + [E[q][w] for q in range(1, 5)])
coef, res, *_ = np.linalg.lstsq(X, ev[w], rcond=None); R2 = 1 - ((ev[w] - X @ coef) ** 2).sum() / ((ev[w] - ev[w].mean()) ** 2).sum()
B1 = E[1][w] + tau + r1[w]; BU = sum(E[q][w] + tau for q in range(1, 5)) + rU[w]
busy = ev[w] > 0
print("# lyap %s slice x0=%.4g cells %d..%d p1..p4 = %s" % (pre, xs, k0, k0 + n - 1, ' '.join('%.4f' % p[q] for q in range(1, 5))))
print("R2(e ~ 1 + E1..E4) = %.4f  coef = %s" % (R2, ' '.join('%.4f' % v for v in coef)))
print("corr(E_q, E_q') matrix:", ' '.join('%.3f' % np.corrcoef(E[a][w], E[b][w])[0, 1] for a in range(1, 5) for b in range(a + 1, 5)))
print("bound B1 = E1+tau+r1: max(e - B1) = %.3e (proved <= 0, up to the warm-up), mean slack on busy cells %.3f, frac(B1 - e < 1 | busy) %.3f, max e %d, max B1 %.2f, max r1 %.2f"
      % ((ev[w] - B1).max(), (B1 - ev[w])[busy].mean(), ((B1 - ev[w]) < 1)[busy].mean(), ev[w].max(), B1.max(), r1[w].max()))
print("bound BU = sum_q(E_q+tau)+rU: max(e - BU) = %.3e, mean slack on busy cells %.3f, frac(BU - e < 1 | busy) %.3f, max BU %.2f, max rU %.2f (service %.4f)"
      % ((ev[w] - BU).max(), (BU - ev[w])[busy].mean(), ((BU - ev[w]) < 1)[busy].mean(), BU.max(), rU[w].max(), SU))
for a in (0.0, 0.5, 1.0, 1.5, 2.0):
    print("a=%.1f: max(e - a*E1 - tau - r1) = %.3f" % (a, (ev[w] - a * E[1][w] - tau - r1[w]).max()))
