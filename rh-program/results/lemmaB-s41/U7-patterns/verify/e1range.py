import sys, math, numpy as np
pre, D, xs, n, thr = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
rho = math.pi / D; t = 1 / rho; tau = 0.5
k0 = int(math.floor((xs - 1) * rho + 1 - tau)); lo, hi = k0 - 1, k0 - 1 + n
c1 = np.memmap(pre + '.c1.u8', np.uint8, 'r'); e = np.memmap(pre + '.e.u8', np.uint8, 'r')
pk = np.memmap(pre + '.primes.u32', np.uint32, 'r'); p1 = 1 + (float(pk[0]) - 1 + tau) * t
base = 0; B = 1 << 26
for i in range(0, lo, B): base += int(np.asarray(c1[i:min(i + B, lo)]).sum(dtype=np.int64))
k = np.arange(k0, k0 + n, dtype=np.float64); xk = 1 + (k - 1 + tau) * t
E1 = base + np.cumsum(np.asarray(c1[lo:hi]), dtype=np.int64) - rho * (xk / p1 - 1)
ev = np.asarray(e[lo:hi]); m = ev >= thr
print("%s: cells with e >= %d: %d; E(x/p1) on them: min %.3f max %.3f mean %.3f" % (pre, thr, m.sum(), E1[m].min(), E1[m].max(), E1[m].mean()))
