"""Zeros of Xi_k and Xi_{k+1} in W_k = [0, X_k] x [0, Y_k], X_k = 2 pi (k+2)^2 + 30 (numerical argument principle,
not interval-rigorous), plus the non-real zeros of Xi_k up to X_k + margin (the starts of the branches).
usage: python3 census_zeros.py k [Y0] [margin]  -> ../data/k{k}-zeros.json"""
import sys, json, time
sys.path.insert(0, '.')
import mpmath as mp, hb, argp
mp.mp.dps = 30
k = int(sys.argv[1]); Y = float(sys.argv[2]) if len(sys.argv) > 2 else 30.0
margin = float(sys.argv[3]) if len(sys.argv) > 3 else 12.0
X = float(2*mp.pi*(k + 2)**2 + 30)
out = dict(k=k, X=X, margin=margin, dps=30)
t0 = time.time()
def log(*a):
    print(*a, '%.0f s' % (time.time() - t0)); sys.stdout.flush()
nt = lambda g, z: hb.newton(g, z)
for N in (k, k + 1):
    f = lambda z, N=N: hb.XiN(N, z)
    # Y: the count must not change when the top edge is raised by 15
    while True:
        c1, n1 = argp.count_window(f, X, Y); c2, n2 = argp.count_window(f, X, Y + 15)
        log('N=%d count(Y=%g)=%s count(Y=%g)=%s' % (N, Y, mp.nstr(c1, 6), Y + 15, mp.nstr(c2, 6)))
        if abs(c1 - c2) < 0.05 and abs(c1 - mp.nint(c1)) < 0.05:
            break
        Y += 15
    out['Y_%d' % N] = Y; out['total_%d' % N] = int(mp.nint(c1))
    xr = X + (margin if N == k else 0)
    zs = argp.find_zeros(f, 0, xr, mp.mpf('0.001'), Y + 15, newton=nt)
    zs = sorted(zs, key=lambda z: mp.re(z))
    out['nonreal_%d' % N] = [[mp.nstr(mp.re(z), 20), mp.nstr(mp.im(z), 20)] for z in zs]
    inW = [z for z in zs if mp.re(z) <= X]
    out['nonreal_in_W_%d' % N] = len(inW)
    out['real_in_W_%d' % N] = out['total_%d' % N] - 2*len(inW)
    log('N=%d: total %d, non-real in W %d (found up to X+%g: %d), implied real %d' % (N, out['total_%d' % N], len(inW),
        xr - X, len(zs), out['real_in_W_%d' % N]))
    json.dump(out, open('../data/k%d-zeros.json' % k, 'w'), indent=1)
Yk = max(out['Y_%d' % k], out['Y_%d' % (k + 1)])
out['Y_k'] = Yk
json.dump(out, open('../data/k%d-zeros.json' % k, 'w'), indent=1)
starts = out['nonreal_%d' % k]
json.dump(starts, open('../data/k%d-starts.json' % k, 'w'))
log('done; starts', len(starts))
