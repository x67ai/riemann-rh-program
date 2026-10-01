# read-O: complex zeros of L(s) = 1 + rho^s zeta(s, 1/2 + rho), rho = pi/16.
# (1) argument-principle counts on boxes (adaptive step: |d arg| < 0.3 rad per step, step halved otherwise);
# (2) Newton refinement of the NOTE's two quoted zeros and of grid minima inside the box (zeros listed).
import sys
from mpmath import mp, mpf, mpc, pi, zeta, arg, findroot, fabs
mp.dps = 20
rho = pi/16
a = mpf(1)/2 + rho
def L(s): return 1 + rho**s*zeta(s, a)

def winding(path, h0=mpf('0.05')):
    tot, minabs, nev = mpf(0), None, 0
    for z0, z1 in zip(path[:-1], path[1:]):
        z, f = z0, L(z0); nev += 1
        length = abs(z1 - z0); u = (z1 - z0)/length; done = mpf(0); h = h0
        while done < length:
            step = min(h, length - done)
            zn = z + u*step; fn = L(zn); nev += 1
            d = arg(fn/f)
            if fabs(d) > mpf('0.3') and step > mpf(10)**-6:
                h = step/2; continue
            tot += d; z, f = zn, fn; done += step
            m = abs(fn); minabs = m if minabs is None or m < minabs else minabs
            h = min(h*2, h0)
    return tot/(2*pi), minabs, nev

def box(s0, s1, t0, t1):
    P = [mpc(s0, t0), mpc(s1, t0), mpc(s1, t1), mpc(s0, t1), mpc(s0, t0)]
    w, m, n = winding(P)
    return w, m, n

which = sys.argv[1] if len(sys.argv) > 1 else "A"
if which == "A":
    for z in (mpc('0.730915', '42.089392'), mpc('0.512474', '22.437213')):
        r = findroot(L, z)
        print("Newton from NOTE value", z, "->", mp.nstr(r, 12), " |L| =", mp.nstr(abs(L(r)), 3), flush=True)
    for (s0, s1, t0, t1) in [(0.5, 1.0, 0.5, 50), (0.5, 1.0, 50, 100), (0.5, 0.75, 0.5, 100), (0.75, 1.0, 0.5, 100)]:
        w, m, n = box(mpf(s0), mpf(s1), mpf(t0), mpf(t1))
        print(f"box Re in [{s0},{s1}] Im in [{t0},{t1}]: winding = {mp.nstr(w, 6)}  min|L| on contour = {mp.nstr(m, 4)}  evals = {n}", flush=True)
elif which == "D":   # small box around the real zero: complex zeros with |Im s| < 0.5?
    for (s0, s1, t0, t1) in [(0.5, 0.95, -0.5, 0.5), (0.95, 1.2, 0.05, 0.5)]:
        w, m, n = box(mpf(s0), mpf(s1), mpf(t0), mpf(t1))
        print(f"box Re in [{s0},{s1}] Im in [{t0},{t1}]: winding = {mp.nstr(w, 6)}  min|L| on contour = {mp.nstr(m, 4)}  evals = {n}", flush=True)
elif which == "B":   # right of Re s = 1: is L zero-free at low height?
    for (s0, s1, t0, t1) in [(1.0, 1.25, 0.5, 250), (1.0, 1.25, 250, 500), (1.0, 1.25, 500, 750), (1.0, 1.25, 750, 1000)]:
        w, m, n = box(mpf(s0), mpf(s1), mpf(t0), mpf(t1))
        print(f"box Re in [{s0},{s1}] Im in [{t0},{t1}]: winding = {mp.nstr(w, 6)}  min|L| on contour = {mp.nstr(m, 4)}  evals = {n}", flush=True)
elif which == "C":   # list zeros in 1/2 < Re s < 1, 0.5 < Im s < 100 by grid minima + Newton
    found = []
    for i in range(0, 26):
        for j in range(0, 400):
            z = mpc(mpf('0.5') + mpf(i)/50, mpf('0.5') + mpf(j)/4)
            try:
                r = findroot(L, z, tol=mpf(10)**-15, maxsteps=30)
            except Exception:
                continue
            if mpf('0.5') < r.real < 1 and mpf('0.5') < r.imag < 100 and abs(L(r)) < mpf(10)**-12:
                if all(abs(r - q) > mpf(10)**-6 for q in found):
                    found.append(r); print("zero", mp.nstr(r, 12), flush=True)
    print("distinct zeros found:", len(found))
