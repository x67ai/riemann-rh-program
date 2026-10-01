# check_I1.py — U7-patterns: identity (I1) on data. For d = p1..p4: E(x_k/d) computed from the per-cell divisibility counts,
# E_div(k) = #{composites <= x_k divisible by d} - rho*(x_k/d - 1), must equal E(y), y = x_k/d, computed from the lattice data:
# E(y) = e_{k'} + 1 - tau + #{composites in (x_{k'}, y]} - rho*(y - x_{k'}), k' = last lattice index <= y. So
# D(k) := E_div(k) - [e_{k'} + 1 - tau - rho*(y - x_{k'})] must be an integer in [0, c_{k'+1} + b], b = 1 if the g-prime of cell k'+1 is
# placed early (at x_{k'+1} - delta <= y), else 0 (the composites, and the early prime, of the partial cell).
import sys, math, numpy as np
pre, D, tau, delta = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
rho = math.pi / D; t = 1 / rho
c = np.fromfile(pre + '.c.u8', np.uint8).astype(np.int64); e = np.fromfile(pre + '.e.u8', np.uint8).astype(np.int64)
pk = np.fromfile(pre + '.primes.u32', np.uint32)
arrs = [np.fromfile(pre + '.c1.u8', np.uint8)] + [np.fromfile(pre + '.d%d.u8' % q, np.uint8) for q in (2, 3, 4)]
K = len(c); k = np.arange(1, K + 1); xk = 1 + (k - 1 + tau) * t
bad = 0
for q in range(4):
    d = 1 + (pk[q] - 1 + tau) * t - delta
    Ediv = np.cumsum(arrs[q].astype(np.int64)) - rho * (xk / d - 1)
    y = xk / d; ok = y >= 1 + tau * t                        # need k' >= 1
    kp = np.floor((y[ok] - 1) * rho + 1 - tau).astype(np.int64)   # last lattice index <= y
    Elat = e[kp - 1] + 1 - tau - rho * (y[ok] - (1 + (kp - 1 + tau) * t))
    Dk = Ediv[ok] - Elat
    nint = np.abs(Dk - np.round(Dk)) > 1e-6; Dr = np.round(Dk).astype(np.int64)
    kn = np.minimum(kp, K - 1)                                   # 0-based index of cell k'+1
    isp = (c[kn] == 0) & (e[kn - 1] == 0)
    early = isp & (1 + (kn + tau) * t - delta <= y[ok])
    out = (Dr < 0) | (Dr > c[kn] + early)
    bad += int(nint.sum() + out.sum())
    print("d = p%d = %.6f: %d points, non-integer %d, outside [0, c] %d, max |D - round| %.2e" % (q + 1, d, ok.sum(), nint.sum(), out.sum(), np.abs(Dk - np.round(Dk)).max()))
print("RESULT", "PASS" if bad == 0 else "FAIL", pre)
