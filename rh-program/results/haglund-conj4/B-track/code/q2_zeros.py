"""Q2: zeros of Xi_26, Xi_27, Xi_28 in the box [x0, x1] x [0.001, Y] (argument principle + bisection + Newton),
with the count repeated for Y + 15; real zeros of Xi_N on [x0, x1] by the real-axis scans.
usage: python3 q2_zeros.py x0 x1 Y  -> ../data/q2-zeros.json"""
import sys, json, time
sys.path.insert(0, '.')
import mpmath as mp, hb, argp
mp.mp.dps = 30
x0, x1, Y = [float(a) for a in sys.argv[1:4]]
out = dict(box=[x0, x1, 0.001, Y], dps=30)
t0 = time.time()
def log(*a):
    print(*a, '%.0f s' % (time.time() - t0)); sys.stdout.flush()
for N in (26, 27, 28):
    f = lambda z, N=N: hb.XiN(N, z)
    A = argp.Arg(f)
    w1, A = argp.count_rect(f, x0, x1, 0.001, Y, A)
    w2, A2 = argp.count_rect(f, x0, x1, 0.001, Y + 15)
    log('N=%d winding Y=%g: %s, Y+15: %s' % (N, Y, mp.nstr(w1, 6), mp.nstr(w2, 6)))
    zs = argp.find_zeros(f, x0, x1, 0.001, Y, A=A, newton=lambda g, z: hb.newton(g, z))
    zs = sorted(zs, key=lambda z: mp.re(z))
    out['N%d' % N] = dict(count=float(w1), count_Yplus15=float(w2),
                          zeros=[[mp.nstr(mp.re(z), 20), mp.nstr(mp.im(z), 20)] for z in zs])
    log('N=%d found %d: %s' % (N, len(zs), [mp.nstr(z, 12) for z in zs]))
    json.dump(out, open('../data/q2-zeros.json', 'w'), indent=1)
log('done')
