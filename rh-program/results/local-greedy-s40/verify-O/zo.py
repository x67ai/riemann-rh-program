# zo.py -- read-O: F_X(s) = rho*zeta(s) + D_X(s) with D_X by DIRECT sums (fxo, no Taylor moments), zeta by mpmath (dps 30).
# Newton on F_X from rounded starting points (2 decimals, not the NOTE's digits). usage: zo.py dump X start1 [start2 ...]
import subprocess, sys, os, mpmath as mp
mp.mp.dps = 30
FXO = '/private/tmp/rh-s41-read-localgreedy/fxo'; TMP = '/private/tmp/rh-s41-read-localgreedy'
RN, RD = os.environ.get('RHO_NUM', '3'), os.environ.get('RHO_DEN', '5'); RHO = mp.mpf(RN)/int(RD)
def D(dump, X, pts):
    seg = os.path.join(TMP, 'seg_%d.txt' % os.getpid())
    with open(seg, 'w') as f:
        for s in pts: f.write('%.15f %.15f 0 0 0\n' % (s.real, s.imag))
    out = subprocess.run([FXO, dump, str(X), os.environ.get('RHO_NUM', '3'), os.environ.get('RHO_DEN', '5'), seg], capture_output=True, text=True, check=True).stdout.split('\n')
    res = []
    for l in out:
        if l.strip():
            v = l.split(); res.append((complex(float(v[3]), float(v[4])), complex(float(v[5]), float(v[6]))))
    return res
def F(dump, X, pts):
    r = []
    for s, (d, dd) in zip(pts, D(dump, X, pts)):
        z = mp.zeta(mp.mpc(s.real, s.imag)); zp = mp.zeta(mp.mpc(s.real, s.imag), derivative=1)
        r.append((complex(RHO*z) + d, complex(RHO*zp) + dd))
    return r
def newton(dump, X, starts, it=8, tol=1e-11):
    cur = list(starts); done = [False]*len(cur); hist = []
    for k in range(it):
        idx = [i for i in range(len(cur)) if not done[i]]
        if not idx: break
        vals = F(dump, X, [cur[i] for i in idx])
        for i, (f, fp) in zip(idx, vals):
            step = f/fp; cur[i] = cur[i] - step; hist.append((k, i, abs(f), abs(fp), abs(step)))
            if abs(step) < tol: done[i] = True
    fin = F(dump, X, cur)
    return cur, fin, hist
if __name__ == '__main__':
    dump, X = sys.argv[1], int(float(sys.argv[2])); starts = [complex(a) for a in sys.argv[3:]]
    cur, fin, hist = newton(dump, X, starts)
    for h in hist: print('iter %d zero %d |F|=%.3e |F\'|=%.4f |step|=%.3e' % h)
    for s, (f, fp) in zip(cur, fin): print('ZERO X=%d  s = %.10f + %.10fi  |F|=%.2e  |F\'|=%.4f' % (X, s.real, s.imag, abs(f), abs(fp)))
