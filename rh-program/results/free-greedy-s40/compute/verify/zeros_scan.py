# zeros_scan.py MOMFILE [TMAX=200] [SIGMIN=0.5] [SIGMAX=1.05] [DSIG=0.005]
# All zeros of F_X (block moments) in SIGMIN < sigma < SIGMAX, 0 <= t <= TMAX:
#  (1) G(s) = (s - 1) F_X(s) (entire) on a grid: sigma step DSIG, t step 2 pi / (2^21 w) ~ 0.030 (FFT);
#  (2) cells whose corner phases wind by +-2 pi -> Newton on F_X (analytic F');
#  (3) the total count on the rectangle by the argument principle along its boundary (adaptive: every step
#      changes arg G by < pi/8), compared with the number of distinct zeros found.
import sys, math, warnings, numpy as np
warnings.filterwarnings("ignore")
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from zeta_bm import load, F, F_grid, Gfun

def G(s, D): return Gfun(s, D)

def newton(s, D, it=60):
    for _ in range(it):
        v, dv = F(s, D, deriv=True)
        ds = v / dv; s -= ds
        if abs(ds) < 1e-14 * max(1.0, abs(s)): break
    v, dv = F(s, D, deriv=True)
    return s, abs(v), abs(dv)

def arg_path(z0, z1, D, g0=None, g1=None, depth=0):
    """change of arg G along the segment z0 -> z1, subdividing until each piece changes arg by < pi/8"""
    if g0 is None: g0 = G(z0, D)
    if g1 is None: g1 = G(z1, D)
    d = math.atan2((g1 / g0).imag, (g1 / g0).real)
    if abs(d) < math.pi / 8 or depth > 40: return d
    zm = 0.5 * (z0 + z1); gm = G(zm, D)
    return arg_path(z0, zm, D, g0, gm, depth + 1) + arg_path(zm, z1, D, gm, g1, depth + 1)

def winding_box(s0, s1, t0, t1, D, n=64):
    pts = [complex(s0, t0), complex(s1, t0), complex(s1, t1), complex(s0, t1), complex(s0, t0)]
    tot = 0.0
    for a, b in zip(pts[:-1], pts[1:]):
        zs = [a + (b - a) * k / n for k in range(n + 1)]
        gs = [G(z, D) for z in zs]
        for k in range(n): tot += arg_path(zs[k], zs[k + 1], D, gs[k], gs[k + 1])
    return tot / (2 * math.pi)

def scan(D, tmax=200.0, smin=0.5, smax=1.05, dsig=0.005):
    sig = np.arange(smin, smax + 1e-12, dsig)
    rows = []
    for sg in sig:
        t, Fv = F_grid(sg, D, tmax=tmax)
        rows.append((sg + 1j * t - 1) * Fv)
    Gv = np.array(rows)                       # [sigma, t]
    ph = np.angle(Gv)
    def dang(a, b): return np.angle(np.exp(1j * (b - a)))
    w = (dang(ph[:-1, :-1], ph[1:, :-1]) + dang(ph[1:, :-1], ph[1:, 1:]) + dang(ph[1:, 1:], ph[:-1, 1:]) + dang(ph[:-1, 1:], ph[:-1, :-1])) / (2 * math.pi)
    cells = np.argwhere(np.abs(w) > 0.5)
    zeros = []
    for i, m in cells:
        s0 = complex(sig[i] + dsig / 2, t[m] + (t[1] - t[0]) / 2)
        z, fv, fd = newton(s0, D)
        if not (smin - 0.02 < z.real < smax + 0.02 and -0.05 < z.imag < tmax + 0.05): continue
        if any(abs(z - q[0]) < 1e-7 for q in zeros): continue
        zeros.append((z, fv, fd, int(round(w[i, m]))))
    zeros.sort(key=lambda q: q[0].imag)
    return sig, t, zeros

if __name__ == "__main__":
    path = sys.argv[1]
    tmax = float(sys.argv[2]) if len(sys.argv) > 2 else 200.0
    smin = float(sys.argv[3]) if len(sys.argv) > 3 else 0.5
    smax = float(sys.argv[4]) if len(sys.argv) > 4 else 1.05
    dsig = float(sys.argv[5]) if len(sys.argv) > 5 else 0.005
    D = load(path)
    print(f"# zeros_scan {path}\n# X = {D['X']:.6e}  N = {D['N']}  E(X) = {D['EX']:.6f}  rho = {D['rho']:.15f}  rectangle {smin} < sigma < {smax}, 0 <= t <= {tmax}")
    sig, t, zeros = scan(D, tmax, smin, smax, dsig)
    inside = [q for q in zeros if smin < q[0].real < smax and 0 <= q[0].imag <= tmax]
    print(f"# grid: {len(sig)} sigma values x {len(t)} t values (dt = {t[1] - t[0]:.5f}); distinct zeros found by Newton: {len(inside)}")
    print("#   sigma              t                 |F_X| at zero   |F_X'|      cell winding")
    for z, fv, fd, wn in inside:
        print(f"  {z.real:.12f}  {z.imag:16.12f}  {fv:.2e}   {fd:10.4e}  {wn:+d}")
    tot = winding_box(smin, smax, 0.0, tmax, D, n=400) if "--count" in sys.argv else float("nan")
    print(f"# argument principle on the whole rectangle: winding = {tot:.4f}  (zeros found inside: {len(inside)})")
    if inside:
        best = max(inside, key=lambda q: q[0].real)
        print(f"# largest real part: {best[0].real:.10f} at t = {best[0].imag:.6f}")
        for T in [25, 50, 100, 150, 200]:
            sub = [q for q in inside if q[0].imag <= T]
            if sub: print(f"#   max sigma over zeros with t <= {T:4d}: {max(q[0].real for q in sub):.6f}  ({len(sub)} zeros)")
