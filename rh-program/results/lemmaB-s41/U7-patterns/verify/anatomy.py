# anatomy.py — U7-patterns: anatomy of the largest e-excursions of S8 from an s8gen watch dump.
# usage: python3 anatomy.py prefix rho tau delta statsfile ntop mode
#   mode=windows : write prefix.watch.in (cells [a-40, b] of the top excursions + 3 control windows each) and exit
#   mode=analyze : read prefix.watch.txt (lines: k f nfac idx...), print one ANAT line per excursion and the control baseline
import sys, math, re, random
import numpy as np
pre, rho, tau, delta, statsf, ntop, mode = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), sys.argv[5], int(sys.argv[6]), sys.argv[7]
t = 1 / rho
tops = []
for l in open(statsf):
    if l.startswith('TOP'):
        d = dict(re.findall(r'(\w+)=([-\d.e+]+)', l)); tops.append({k: float(v) for k, v in d.items()})
tops = tops[:ntop]
random.seed(12345)
ctrl = []
for T in tops:
    L = int(T['cell_b'] - T['cell_a']) + 41
    for j in range(3):
        a = int(T['cell_a']) + random.choice([-1, 1]) * random.randint(200000, 2000000); ctrl.append((a, a + L - 1))
if mode == 'windows':
    W = [(int(T['cell_a']) - 40, int(T['cell_b'])) for T in tops] + ctrl
    W.sort()
    with open(pre + '.watch.in', 'w') as f:
        for a, b in W: f.write('%d %d\n' % (a, b))
    print('wrote', len(W), 'windows'); sys.exit(0)
# analyze
pk = np.memmap(pre + '.primes.u32', np.uint32, 'r'); pv = lambda j: 1 + (float(pk[j]) - 1 + tau) * t - delta
e = np.memmap(pre + '.e.u8', np.uint8, 'r'); c = np.memmap(pre + '.c.u8', np.uint8, 'r')
comp = {}   # cell -> list of (f, idx tuple)
for l in open(pre + '.watch.txt'):
    p = l.split(); k = int(p[0]); comp.setdefault(k, []).append((float(p[1]), tuple(int(x) for x in p[3:])))
def classes(cells):
    sp = np.zeros(8); om = np.zeros(4); div = np.zeros(8)
    bins = [0, 1, 2, 3, 10, 100, 1000, 10**12]
    for k in cells:
        for f, idx in comp.get(k, []):
            s = idx[0]; sp[np.searchsorted(bins, s, side='right') - 1] += 1
            om[min(len(idx), 5) - 2] += 1
            for q in set(idx):
                if q < 8: div[q] += 1
    return sp, om, div
xk = lambda k: 1 + (k - 1 + tau) * t
ucell = lambda y: (y - 1) * rho + 1 - tau
def primes_in(y1, y2):   # g-primes with lattice cell k' and x_k' in (y1, y2]
    k1, k2 = int(math.floor(ucell(y1))) + 1, int(math.floor(ucell(y2)))
    if k2 < k1: return 0, 0
    cc = np.asarray(c[k1-1:k2]); ee = np.asarray(e[k1-2:k2-1]); return int(((cc == 0) & (ee == 0)).sum()), k2 - k1 + 1
def frac_primes(y, span=100000):
    k = int(ucell(y)); a = max(2, k - span); b = k + span
    cc = np.asarray(c[a-1:b]); ee = np.asarray(e[a-2:b-1]); return ((cc == 0) & (ee == 0)).mean()
# control baseline per cell
csp = np.zeros(8); com = np.zeros(4); ncell = 0
for a, b in ctrl:
    s1, o1, _ = classes(range(a, b + 1)); csp += s1; com += o1; ncell += b - a + 1
# exact shares w_class = sum over q in class of (1/q) prod_{p<q} (1 - 1/p); M(sqrt x) closes the decomposition
bins = [0, 1, 2, 3, 10, 100, 1000]
def shares(x):
    z = math.sqrt(x); M = 1.0; w = np.zeros(8); j = 0
    while True:
        q = pv(j)
        if q > z: break
        cls = np.searchsorted(bins, j, side='right') - 1; w[min(cls, 7)] += M / q; M *= (1 - 1 / q); j += 1
    return w, M
print('BASE per-cell spf classes [p1,p2,p3,p4..p10,p11..p100,p101..p1000,>p1000]:', ' '.join('%.4f' % v for v in csp[:7] / ncell),
      '| Omega 2,3,4,>=5:', ' '.join('%.4f' % v for v in com / ncell), '| cells', ncell)
for i, T in enumerate(tops):
    a, pk_, b, h = int(T['cell_a']), int(T['cell_peak']), int(T['cell_b']), int(T['h']); lb = pk_ - a + 1
    sp, om, div = classes(range(a, pk_ + 1))
    exp_sp = csp / ncell * lb; exp_om = com / ncell * lb
    X = [div[q] - lb / pv(q) for q in range(5)]          # = Delta E(W/p_q) exactly
    lower = []
    for q in range(5):
        y1, y2 = xk(a - 1) / pv(q), xk(pk_) / pv(q)
        npr, ncl = primes_in(y1, y2); fp = frac_primes((y1 + y2) / 2)
        k1, k2 = int(ucell(y1)), int(ucell(y2)) + 1
        emax = int(np.asarray(e[max(k1-1, 0):k2]).max()); e0 = int(e[max(k1 - 2, 0)])
        lower.append('q%d: dE=%+.2f primes=%d/%.2f emax=%d e0=%d' % (q + 1, X[q], npr, fp * (y2 - y1) * rho, emax, e0))
    w, Msq = shares(xk(pk_)); ex = sp[:7] - lb * w[:7]
    if abs(ex.sum() - lb * Msq - h) > 1e-6: print('decomposition check failed', i, ex.sum() - lb * Msq, h)
    print('ANAT %d h=%d x=%.4e lbuild=%d len=%d arrivals=%d | exact spf-class excess C-lb*w [p1,p2,p3,p4-10,p11-100,p101-1000,>p1000]:' % (i, h, xk(a), lb, b - a, int(sp.sum())),
          ' '.join('%+.2f' % v for v in ex), '(z:', ' '.join('%+.1f' % (v / math.sqrt(lb * ww)) for v, ww in zip(ex, w[:7])), ') -lb*M(sqrt x)=%.2f' % (-lb * Msq), '| Omega excess 2,3,4,5+:', ' '.join('%+.1f' % v for v in om - exp_om), '|', ' ; '.join(lower))
