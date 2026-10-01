# fito.py -- read-O: running-sup slopes from gen7o B-lines (20 log-bins per decade). Own convention, stated:
# R_b = max_{b' <= b} sup_bin |.|, x_b = upper end of bin b = 10^((b+1)/20); slope = least squares of log R_b on log x_b
# over the bins with lower end >= 10^k. Quantities: absE (sup|N(x) - rho x - (1-rho)| over real x), psi (sup|psi_P - x|), Mg, MP.
import re, sys, math
def load(fn):
    rows = []
    for l in open(fn):
        if l.startswith('B '):
            b = int(l.split()[1]); d = dict(re.findall(r'(\w+)=([-\d.e+]+)', l)); rows.append((b, d))
    return rows
def slope(xs, ys):
    n = len(xs); mx = sum(xs)/n; my = sum(ys)/n
    return sum((x-mx)*(y-my) for x, y in zip(xs, ys))/sum((x-mx)**2 for x in xs)
for fn in sys.argv[1:]:
    rows = load(fn); out = []
    for key in ('absE', 'psi', 'Mg', 'MP'):
        run = 0; pts = []
        for b, d in rows:
            run = max(run, float(d[key])); pts.append((b, run))
        sl = []
        for k in range(3, 8):
            sel = [(math.log((b+1)/20*math.log(10)) if False else (b+1)/20*math.log(10), math.log(r)) for b, r in pts if b >= 20*k and r > 0]
            sl.append(slope([p[0] for p in sel], [p[1] for p in sel]))
        out.append((key, sl))
    print(fn.split('/')[-1])
    for key, sl in out: print('  %-5s k=3..7: %s' % (key, ' '.join('%.3f' % s for s in sl)))
    a = dict(out)['psi']; b = dict(out)['absE']
    print('  a-2b  k=3..7: %s' % ' '.join('%+.2f' % (x - 2*y) for x, y in zip(a, b)))
