"""S5_structure.py -- anatomy of the S5 g-prime sets: deleted primes (m_p = 0), doubled primes (m_p >= 2),
composite g-primes; counting exponents d log(count)/d log x over [1e5, 1e8]. Usage: python3 S5_structure.py label..."""
import sys, numpy as np
BIG = "/private/tmp/claude-501/-Users-jaytyagi-Library-Mobile-Documents-com-apple-CloudDocs-Documents-Work-2026-Math/a1ca2244-cf17-4f92-9355-9db717d0d6ae/scratchpad/big"
X = 10**8
isp = np.ones(X + 1, dtype=bool); isp[:2] = False
for p in range(2, int(X**0.5) + 1):
    if isp[p]: isp[p*p::p] = False
def expo(pos):
    pos = np.sort(pos); out = []
    for lo in (1e5, 1e6):
        xs = np.logspace(np.log10(lo), 8, 25); c = np.searchsorted(pos, xs)
        m = c > 0
        out.append(np.polyfit(np.log(xs[m]), np.log(c[m]), 1)[0] if m.sum() > 3 else float('nan'))
    return out
for lab in sys.argv[1:]:
    g = np.fromfile(f"{BIG}/gp_{lab}.u32", dtype=np.uint32).reshape(-1, 2)
    n, m = g[:, 0].astype(np.int64), g[:, 1]
    mult = np.zeros(X + 1, dtype=np.uint8); mult[n] = m
    primes = np.nonzero(isp)[0]
    dele = primes[mult[primes] == 0]; dbl = primes[mult[primes] >= 2]
    comp = n[~isp[n]]
    print(f"{lab}: deleted primes {len(dele)} (first {dele[:8].tolist()}) exp{[round(e,3) for e in expo(dele)]}; "
          f"doubled {len(dbl)} (first {dbl[:6].tolist()}) exp{[round(e,3) for e in expo(dbl)]}; "
          f"composite g-primes {len(comp)} (first {comp[:8].tolist()}) exp{[round(e,3) for e in expo(comp)]}")
