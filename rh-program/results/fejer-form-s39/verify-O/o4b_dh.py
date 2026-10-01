"""o4b_dh.py — read-O: Davenport–Heilbronn zeros in 50 < t < 120 and the zeros form Z3, own code.
f(s) = ((1-ik)/2) L(s,chi) + ((1+ik)/2) L(s,chibar), chi mod 5, chi(2) = i, k = (sqrt(10-2sqrt5) - 2)/(sqrt5 - 1);
real coefficients: f(s) = 5^{-s}[z(s,1/5) + k z(s,2/5) - k z(s,3/5) - z(s,4/5)]; Lam(s) = (5/pi)^{(s+1)/2} G((s+1)/2) f(s).
Route (differs from verify/z3_weil_fejer.py): FE checked numerically; on-line zeros by sign changes of Lam(1/2+it);
off-line zeros LOCATED (zero test |f| < 1e-12, f without the Gamma factor) by argument-principle box counts on the right half-strip (no recalled starting values), then
findroot; total count by the argument principle on the FULL rectangle [-2, 3] x [50, 120] (arg tracked on steps <= 0.05, bisected while a step turns > 0.6 rad).
W(T) = sum over all zeros (both signs) of K(gamma_rho - T) + K(gamma_rho + T), L = 20; grid + refinement. Output o4b_dh.log."""
import mpmath as mp, numpy as np
mp.mp.dps = 20
kap = (mp.sqrt(10 - 2 * mp.sqrt(5)) - 2) / (mp.sqrt(5) - 1)
def f(s): return mp.power(5, -s) * (mp.zeta(s, mp.mpf(1) / 5) + kap * mp.zeta(s, mp.mpf(2) / 5) - kap * mp.zeta(s, mp.mpf(3) / 5) - mp.zeta(s, mp.mpf(4) / 5))
def Lam(s): return mp.power(5 / mp.pi, (s + 1) / 2) * mp.gamma((s + 1) / 2) * f(s)
out = ["kappa = %s" % mp.nstr(kap, 15)]
for s in (mp.mpc(0.3, 70), mp.mpc(0.8, 90.5)):
    a, b = Lam(s), Lam(1 - s)
    out.append("FE check Lam(s) vs Lam(1-s) at %s: rel. diff %s" % (mp.nstr(s, 4), mp.nstr(abs(a - b) / abs(a), 3)))
# on-line zeros
ts = [50 + 0.02 * k for k in range(3501)]
vals = [Lam(mp.mpc(0.5, t)) for t in ts]
out.append("max |Im Lam(1/2+it)|/|Lam| on the grid: %s" % mp.nstr(max(abs(mp.im(v)) / (abs(v) + 1e-30) for v in vals), 3))
on = []
for k in range(3500):
    if mp.re(vals[k]) * mp.re(vals[k + 1]) < 0:
        on.append(mp.findroot(lambda t: mp.re(Lam(mp.mpc(0.5, t))), (ts[k], ts[k + 1]), solver="anderson"))
out.append("on-line zeros in (50,120) by sign change: %d ; first %s, last %s" % (len(on), mp.nstr(on[0], 10), mp.nstr(on[-1], 10)))
def darg(path, maxd=0.6):  # adaptive arg change along a polyline
    tot = mp.mpf(0)
    fine = []
    for z0, z1 in zip(path[:-1], path[1:]):          # pre-split every side into steps <= 0.05 (no blind long chords)
        n = int(mp.ceil(abs(z1 - z0) / 0.05))
        fine += [z0 + (z1 - z0) * k / n for k in range(n)]
    fine.append(path[-1])
    vals = [Lam(z) for z in fine]
    for z0, z1, f0, f1 in zip(fine[:-1], fine[1:], vals[:-1], vals[1:]):
        stack = [(z0, z1, f0, f1)]
        while stack:
            a, b, fa, fb = stack.pop()
            d = mp.im(mp.log(fb / fa))
            if abs(d) > maxd and abs(b - a) > 1e-6:
                m = (a + b) / 2; fm = Lam(m); stack.append((m, b, fm, fb)); stack.append((a, m, fa, fm))
            else: tot += d
    return tot
def box(s0, s1, t0, t1):
    return darg([mp.mpc(s0, t0), mp.mpc(s1, t0), mp.mpc(s1, t1), mp.mpc(s0, t1), mp.mpc(s0, t0)]) / (2 * mp.pi)
Nfull = box(-2, 3, 50, 120)
out.append("argument principle, full rectangle [-2,3]x[50,120]: N = %s" % mp.nstr(Nfull, 8))
off = []
for t0 in range(50, 120, 10):
    n = box(0.52, 3, t0, t0 + 10)
    if abs(n) > 0.5:
        out.append("   right half-strip box [0.52,3]x[%d,%d]: %s zero(s)" % (t0, t0 + 10, mp.nstr(n, 6)))
        best = None
        for sig in (0.6, 0.75, 0.9):
            for tt in np.arange(t0 + 0.5, t0 + 10, 1.0):
                try:
                    z = mp.findroot(Lam, mp.mpc(sig, tt))
                except Exception:
                    continue
                if mp.re(z) > 0.52 and t0 <= mp.im(z) <= t0 + 10 and abs(f(z)) < 1e-12:
                    if all(abs(z - w) > 1e-6 for w in off): off.append(z)
out.append("off-line zeros found (right of the line): %s" % [mp.nstr(z, 12) for z in off])
mir = [1 - mp.re(z) + 1j * mp.im(z) for z in off]
out.append("|f| at the zeros and at the mirrors 1 - beta + i gamma: %s / %s" % ([mp.nstr(abs(f(z)), 3) for z in off], [mp.nstr(abs(f(mp.mpc(w))), 3) for w in mir]))
out.append("count: on %d + off %d + mirrors %d = %d vs argument principle %s" % (len(on), len(off), len(mir), len(on) + 2 * len(off), mp.nstr(Nfull, 6)))
# W(T)
L = 20.0
gam = [complex(float(t), 0) for t in on] + [complex(float(mp.im(z)), -(float(mp.re(z)) - 0.5)) for z in off] + \
      [complex(float(mp.im(z)), (float(mp.re(z)) - 0.5)) for z in off]
gam = np.array(gam + [-g for g in gam])                       # both signs
def K(x):
    zz = L * x / 2
    return L * (np.sin(zz) / zz) ** 2
def W(T): return (K(gam[None, :] - T[:, None]) + K(gam[None, :] + T[:, None])).sum(axis=1).real
TD = np.arange(60, 110, 0.01); WD = W(TD); i = int(WD.argmin())
offmask = np.abs(gam.imag) > 1e-9
share = (K(gam[offmask] - TD[i]) + K(gam[offmask] + TD[i])).sum().real
out.append("DH W(T): grid min over [60,110) step 0.01 = %.4f at T = %.2f ; off-line share %.4f ; on-line share %.4f"
           % (WD[i], TD[i], share, WD[i] - share))
Tf = np.arange(TD[i] - 0.02, TD[i] + 0.02, 1e-5); Wf = W(Tf); jf = int(Wf.argmin())
out.append("   refined (step 1e-5): min W = %.4f at T = %.5f" % (Wf[jf], Tf[jf]))
open("o4b_dh.log", "w").write("\n".join(out) + "\n")
print("\n".join(out))
