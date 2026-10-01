# zbox.py -- F_X(s) = sum_k M_k (s-s0)^k + 0.8*zeta(s, X+1) from zmom's moments: validation, Newton, winding, min|F_X| (read-O, S40)
import sys, mpmath as mp
mp.mp.dps = 30
log = sys.argv[1]; s0 = mp.mpc(float(sys.argv[2]), float(sys.argv[3]))
box = [float(x) for x in sys.argv[4].split(',')] if len(sys.argv) > 4 else [0.7459, 0.7859, 30.306, 30.346]
data = {}; cur = None
for line in open(log):
    p = line.split()
    if p[0] == 'X': cur = int(p[1]); data[cur] = {'M': [], 'D': []}
    elif p[0] == 'M': data[cur]['M'].append(mp.mpc(mp.mpf(p[2]), mp.mpf(p[3])))
    elif p[0] == 'D': data[cur]['D'].append((mp.mpc(float(p[1]), float(p[2])), mp.mpc(mp.mpf(p[3]), mp.mpf(p[4]))))
def S(M, s):  # Taylor polynomial (Horner)
    h = s - s0; r = mp.mpc(0)
    for c in reversed(M): r = r*h + c
    return r
def dS(M, s):
    h = s - s0; r = mp.mpc(0)
    for k in range(len(M)-1, 0, -1): r = r*h + k*M[k]
    return r
def tail(X, s):   # sum_{n>X} n^-s by Euler-Maclaurin (next term ~ |s|^3 X^(-sigma-3)/720, < 1e-22 for X >= 1e7)
    X = mp.mpf(X); return X**(1-s)/(s-1) - X**(-s)/2 + s*X**(-s-1)/12
def dtail(X, s):
    X = mp.mpf(X); L = mp.log(X)
    return -L*X**(1-s)/(s-1) - X**(1-s)/(s-1)**2 + L*X**(-s)/2 + X**(-s-1)/12 - s*L*X**(-s-1)/12
def F(X, s):  return S(data[X]['M'], s) + mp.mpf('0.8')*tail(X, s)
def dF(X, s): return dS(data[X]['M'], s) + mp.mpf('0.8')*dtail(X, s)
for X in sorted(data):
    M = data[X]['M']
    val = max(abs(S(M, s) - d) for s, d in data[X]['D'])
    z = mp.mpc(0.77, 30.35)
    for it in range(40):
        dz = F(X, z)/dF(X, z); z -= dz
        if abs(dz) < mp.mpf(10)**-25: break
    tail_ok = abs(mp.mpf(0.8)*tail(X, z))
    print(f"X={X:>11d}  Taylor-vs-direct max err {mp.nstr(val,3)}  zero {mp.nstr(z.real,12)} + {mp.nstr(z.imag,12)}i  |F'|={mp.nstr(abs(dF(X,z)),6)}  |0.8 zeta(s,X+1)| at zero {mp.nstr(tail_ok,4)}  newton steps {it}")
# winding number and min |F| on the boundary of the box, at the largest X and at 1e8
s1, s2, t1, t2 = box
for X in [x for x in sorted(data) if x in (10**8, 10**9)]:
    for NP in (400, 1600):
        pts = []
        for i in range(NP): pts.append(mp.mpc(s1 + (s2-s1)*i/NP, t1))
        for i in range(NP): pts.append(mp.mpc(s2, t1 + (t2-t1)*i/NP))
        for i in range(NP): pts.append(mp.mpc(s2 - (s2-s1)*i/NP, t2))
        for i in range(NP): pts.append(mp.mpc(s1, t2 - (t2-t1)*i/NP))
        vals = [F(X, s) for s in pts]; w = 0; mx = 0
        for i in range(len(vals)):
            d = mp.arg(vals[(i+1) % len(vals)]/vals[i]); w += d; mx = max(mx, abs(d))
        mn = min(abs(v) for v in vals); dmax = max(abs(dF(X, s)) for s in pts[::max(1, NP//100)])
        h = (s2-s1)/NP
        print(f"X={X} box {box} pts/side {NP}: winding {mp.nstr(w/(2*mp.pi),10)}  max phase step {mp.nstr(mx,4)} rad  min|F_X| {mp.nstr(mn,6)}  max|F_X'| (sampled) {mp.nstr(dmax,5)}  spacing*max|F'| {mp.nstr(h*dmax,4)}")
