# winvar.py — U7-patterns: detrended window variances of the S8 arrival process (non-overlapping windows of h cells).
# usage: python3 winvar.py prefix rho tau x_lo x_hi [extra]   (extra=1: also the parts divisible by p2 and smallest factor > p4)
# For each h: mean and linearly detrended variance (residuals of a straight-line fit in window index, which removes the slow drift of
# the arrival rate across the band) of A = arrivals, A1 = arrivals divisible by p1 (= N at scale x/p1, exactly), R = A - A1,
# P = g-primes (idle cells), and cov(A1, R). Fano = var/mean; Poisson has Fano 1.
import sys, math, numpy as np
pre, rho, tau, xlo, xhi = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])
extra = len(sys.argv) > 6 and sys.argv[6] == '1'
ka = int(math.floor((xlo - 1)*rho + 1 - tau)); kb = int(math.floor((xhi - 1)*rho + 1 - tau))
c = np.memmap(pre + '.c.u8', np.uint8, 'r'); e = np.memmap(pre + '.e.u8', np.uint8, 'r'); c1 = np.memmap(pre + '.c1.u8', np.uint8, 'r')
kb = min(kb, len(c))
cs = np.asarray(c[ka:kb]); c1s = np.asarray(c1[ka:kb]); es = np.asarray(e[ka-1:kb-1])
ps = ((cs == 0) & (es == 0)).astype(np.uint8)
parts = {'A': cs, 'A1': c1s, 'P': ps}
if extra:
    d2 = np.asarray(np.memmap(pre + '.d2.u8', np.uint8, 'r')[ka:kb]); parts['D2'] = d2
    s = [np.asarray(np.memmap(pre + '.s%d.u8' % q, np.uint8, 'r')[ka:kb]) for q in (1, 2, 3)]
    parts['R4'] = (cs.astype(np.int16) - c1s - s[0] - s[1] - s[2]).astype(np.uint8)
print("# winvar %s x in [%.3g, %.3g) cells %d..%d (n=%d)" % (pre, xlo, xhi, ka + 1, kb, kb - ka))
hs = sorted(set([int(round(b * 2**i)) for i in range(0, 25) for b in (1, 1.5)]))
for h in hs:
    n = (kb - ka) // h
    if n < 40: break
    S = {k: v[:n*h].reshape(n, h).sum(1, dtype=np.int64).astype(np.float64) for k, v in parts.items()}
    S['R'] = S['A'] - S['A1']
    idx = np.arange(n, dtype=np.float64)
    def dvar(y):
        a, b = np.polyfit(idx, y, 1); r = y - (a*idx + b); return r, r.var()
    rA, vA = dvar(S['A']); r1, v1 = dvar(S['A1']); rR, vR = dvar(S['R']); rP, vP = dvar(S['P'])
    out = "h=%d nwin=%d mean=%.4f var=%.4f fano=%.5f var/h=%.5f | A1: mean=%.4f var=%.4f | R: var=%.4f fanoR=%.5f cov(A1,R)=%.4f | P: mean=%.4f var=%.4f fanoP=%.4f" % (
        h, n, S['A'].mean(), vA, vA / S['A'].mean(), vA / h, S['A1'].mean(), v1, vR, vR / S['R'].mean(), np.mean(r1 * rR), S['P'].mean(), vP, vP / max(S['P'].mean(), 1e-9))
    if extra:
        r2, v2 = dvar(S['D2']); r4, v4 = dvar(S['R4']); out += " | D2: var=%.4f | R4: mean=%.4f var=%.4f fano=%.5f" % (v2, S['R4'].mean(), v4, v4 / S['R4'].mean())
    print(out, flush=True)
