"""Q3: the real axis for the pencil k. S_k(x) = Xi_{k+1}(x)/Phi_{k+1}(x) = A/B (B > 0 on the line).
Real zeros of F_k(.,t) are the solutions of S_k(x) = u, u = 1 - t.  Extrema of S_k with value in (0,1):
a local max at x* with S = v -> a pair of zeros lands at x* when u = v (tau* = -ln v);
a local min with value in (0,1) -> a pair of real zeros leaves the axis (a witness against (R)).
usage: python3 realaxis.py k x_end [dx0] [dx1] [dps]"""
import sys, json, time
sys.path.insert(0, '.')
import mpmath as mp, hb

def SdS(k, x):
    x = mp.mpf(x)
    h = mp.mpf(2)**(-mp.mp.prec//2)*max(1, abs(x))
    A, B = hb.AB(k, x)
    A2, B2 = hb.AB(k, x + h)
    S = A/B
    dS = (A2/B2 - S)/h
    return S, dS, A, B

def bis_dS(k, a, b, Sa, Sb):
    """zero of S' in (a,b) by bisection on the sign of S' (40 halvings or width 1e-12)."""
    sa = mp.sign(Sa[1])
    for it in range(60):
        m = (a + b)/2
        Sm = SdS(k, m)
        if mp.sign(Sm[1]) == sa:
            a, Sa = m, Sm
        else:
            b, Sb = m, Sm
        if b - a < mp.mpf('1e-12'):
            break
    m = (a + b)/2
    return m, SdS(k, m)

def run(k, x_end, dx0=0.05, dx1=0.01, lo=-0.5, hi=1.5, x_start=0):
    t0 = time.time()
    xs = []; vals = {}
    n0 = int(mp.ceil((x_end - x_start)/dx0))
    grid = [mp.mpf(x_start) + mp.mpf(j)*dx0 for j in range(n0 + 1)]
    for x in grid:
        vals[float(x)] = SdS(k, x)
    # refine cells where S at an end lies in (lo, hi)
    extra = []
    for j in range(n0):
        a, b = float(grid[j]), float(grid[j + 1])
        Sa, Sb = vals[a][0], vals[b][0]
        if lo < Sa < hi or lo < Sb < hi or (Sa - 0.5)*(Sb - 0.5) < 0:
            m = int(round(dx0/dx1))
            for i in range(1, m):
                extra.append(grid[j] + i*(grid[j + 1] - grid[j])/m)
    for x in extra:
        vals[float(x)] = SdS(k, x)
    pts = sorted(vals.keys())
    allx = {float(x): x for x in grid + extra}
    ext = []
    for a, b in zip(pts[:-1], pts[1:]):
        Va, Vb = vals[a], vals[b]
        if mp.sign(Va[1]) != mp.sign(Vb[1]):
            xm, Vm = bis_dS(k, allx[a], allx[b], Va, Vb)
            typ = 'max' if Va[1] > 0 else 'min'
            ext.append(dict(x=mp.nstr(xm, 15), S=mp.nstr(Vm[0], 15), type=typ,
                            in01=bool(0 < Vm[0] < 1)))
    # real zero counts: sign changes of S - 1 (t = 0) and of S (t = 1) on the merged grid
    def changes(c):
        return [(a, b) for a, b in zip(pts[:-1], pts[1:]) if (vals[a][0] - c)*(vals[b][0] - c) < 0]
    z0 = changes(1); z1 = changes(0)
    Bpos = all(vals[p][3] > 0 for p in pts)
    res = dict(k=k, x_start=x_start, x_end=x_end, dx0=dx0, dx1=dx1, refine_band=[lo, hi], dps=mp.mp.dps,
               n_points=len(pts), B_positive=Bpos,
               real_zeros_t0=len(z0), real_zeros_t1=len(z1),
               largest_t0=(z0[-1] if z0 else None), largest_t1=(z1[-1] if z1 else None),
               extrema_total=len(ext), extrema_in01=[e for e in ext if e['in01']],
               min_in01=[e for e in ext if e['in01'] and e['type'] == 'min'],
               extrema_near=[e for e in ext if -2 < float(mp.mpf(e['S'])) < 3],
               seconds=round(time.time() - t0, 1))
    return res

if __name__ == '__main__':
    k = int(sys.argv[1]); x_end = float(sys.argv[2])
    dx0 = float(sys.argv[3]) if len(sys.argv) > 3 else 0.05
    dx1 = float(sys.argv[4]) if len(sys.argv) > 4 else 0.01
    mp.mp.dps = int(sys.argv[5]) if len(sys.argv) > 5 else 30
    r = run(k, x_end, dx0, dx1)
    tag = '' if len(sys.argv) <= 3 else '-dx%g' % dx0
    tag += '' if mp.mp.dps == 30 else '-dps%d' % mp.mp.dps
    json.dump(r, open('../data/q3-k%d%s.json' % (k, tag), 'w'), indent=1)
    print(json.dumps({kk: r[kk] for kk in r if kk not in ('extrema_near',)}, indent=1))
