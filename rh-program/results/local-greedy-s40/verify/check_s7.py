"""check_s7.py -- controls for the S7 generator (unit local-greedy-s40).
(1) term-by-term comparison of a_n from s7gen (segmented, multiplicative; uint16 dump) with s7dp (additive DP; uint32 dump);
(2) multiplicativity a(mn) = a(m) a(n) on random coprime pairs with mn <= X (s7dp's array: no multiplicativity was used to build it);
(3) g = mu * a from s7gen's int16 dump, checked against the Dirichlet convolution identity sum_{d|n} g(d) = a_n for n <= 10^5;
(4) max a_n against the divisor function d(n).
Usage: python3 check_s7.py a_gen.u16 a_dp.u32 g_gen.i16 X npairs seed"""
import sys, math, numpy as np
fa, fd, fg, X, npairs, seed = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
ag = np.fromfile(fa, dtype=np.uint16).astype(np.int64)
ad = np.fromfile(fd, dtype=np.uint32).astype(np.int64)
g = np.fromfile(fg, dtype=np.int16).astype(np.int64)
assert len(ag) == X + 1 and len(ad) == X + 1 and len(g) == X + 1, (len(ag), len(ad), len(g))
mism = np.nonzero(ag[1:] != ad[1:])[0]
print("(1) a_n mismatches s7gen vs s7dp over 1..%d: %d%s; N(X) gen=%d dp=%d; max a_n=%d (uint16 saturation would show as 65535)"
      % (X, len(mism), (" first at n=%d" % (mism[0] + 1)) if len(mism) else "", ag[1:].sum(), ad[1:].sum(), ad.max()))
rng = np.random.default_rng(seed); bad = 0; done = 0; tries = 0
while done < npairs:
    m = np.exp(rng.uniform(np.log(2), np.log(X / 2), size=2 * npairs)).astype(np.int64)
    n = (2 + rng.random(2 * npairs) * (X // m - 1)).astype(np.int64)
    ok = (m >= 2) & (n >= 2) & (m * n <= X); m, n = m[ok], n[ok]
    cop = np.gcd(m, n) == 1; m, n = m[cop], n[cop]
    k = min(len(m), npairs - done); m, n = m[:k], n[:k]
    bad += int(np.sum(ad[m * n] != ad[m] * ad[n])); done += k; tries += 1
print("(2) multiplicativity on %d random coprime pairs (m >= 2 log-uniform in [2, X/2], n >= 2 uniform in [2, X/m]): %d failures" % (done, bad))
Y = min(X, 10**5); conv = np.zeros(Y + 1, dtype=np.int64)
for d in range(1, Y + 1):
    if g[d]: conv[d::d] += g[d]
print("(3) sum_{d|n} g(d) == a_n for n <= %d: %d mismatches" % (Y, int(np.sum(conv[1:] != ag[1:Y + 1]))))
dv = np.zeros(X + 1, dtype=np.int32)
for d in range(1, int(X**0.5) + 1):
    dv[d*d::d] += 2; dv[d*d] -= 1   # pairs (d, n/d) with d < n/d, plus the square root
r = ad[1:] / dv[1:]; i = int(np.argmax(r)) + 1; j = int(np.argmax(ad[1:])) + 1
print("(4) max a_n = %d at n = %d (d(n) = %d); max a_n/d(n) = %.3f at n = %d (a = %d, d = %d); #(a_n > d(n)) = %d"
      % (ad[j], j, dv[j], r[i - 1], i, ad[i], dv[i], int(np.sum(ad[1:] > dv[1:]))))
