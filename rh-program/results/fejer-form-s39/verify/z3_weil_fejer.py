"""Unit fejer-form-s39, Z side, Z3: the zeros-side Fejer form = Weil's functional with the translated Fejer test
g_T(x) = 2 (1 - |x|/L)_+ cos(T x) (positive definite); zero side W(T) = sum_rho [K(gamma_rho - T) + K(gamma_rho + T)],
K(xi) = L (sin(L xi/2)/(L xi/2))^2, gamma_rho = -i (rho - 1/2) (complex for an off-line zero).  L = 20.
zeta: Odlyzko's first 10142 zeros (gamma < 1e4; sources/odlyzko-zeros1.txt).  F_{2.9,2}: zeta's zeros + the factor's zeros
sigma_pm + i (2j+1) pi / log 2 (closed form).  DH: on-line zeros in [50, 120] by sign changes of the real function
Lambda_DH(1/2 + it), the off-line pair(s) by findroot, completeness by the argument principle on the half-rectangle."""
import math, cmath
import numpy as np
import mpmath as mp
mp.mp.dps = 20
L = 20.0
def K(xi):
    z = L * xi / 2
    return L * (cmath.sin(z) / z)**2 if abs(z) > 1e-12 else L
def W(T, gammas):
    return sum(K(g - T) + K(g + T) for g in gammas).real
zs = np.loadtxt('../sources/odlyzko-zeros1.txt'); zs = zs[zs < 1e4]
gz = list(zs) + list(-zs)
Ts = np.arange(0.0, 1e4, 0.05)
# vectorized for zeta: real gammas
def Wvec(T, g):
    z = L * (g[None, :] - T[:, None]) / 2
    return (L * np.sinc(z / np.pi)**2).sum(axis=1)
gzz = np.array(gz); vals = np.concatenate([Wvec(Ts[i:i + 2000], gzz) + Wvec(-Ts[i:i + 2000], gzz) for i in range(0, len(Ts), 2000)])
print("zeta, %d zeros < 1e4 (both signs), L = %.0f: min over T in [0, 1e4) step 0.05 of W(T) = %.6f at T = %.2f (every term >= 0: all gamma real)"
      % (len(zs), L, vals.min(), Ts[vals.argmin()]))
lg = math.log(2); a = 2.9
w1, w2 = [(-a + s * math.sqrt(a * a - 8)) / 4 for s in (1, -1)]
sig = sorted([-math.log2(abs(w1)), -math.log2(abs(w2))])
fz = [complex((2 * j + 1) * math.pi / lg, -(s - 0.5)) for j in range(-200, 200) for s in sig]
gF = fz + [complex(g) for g in zs[:3000]] + [complex(-g) for g in zs[:3000]]
TF = np.arange(0.5, 30, 0.01); WF = [W(T, gF) for T in TF]
i = int(np.argmin(WF))
print("F_{2.9,2}: factor zeros at Re s = %.10f, %.10f, t = (2j+1)*%.10f ; min W(T), T in [0.5, 30): %.4f at T = %.2f"
      % (sig[1], sig[0], math.pi / lg, WF[i], TF[i]))
kap = (mp.sqrt(10 - 2 * mp.sqrt(5)) - 2) / (mp.sqrt(5) - 1)
chi = [0, 1, 1j, -1j, -1]; chib = [0, 1, -1j, 1j, -1]
def Ld(s, ch): return 5**(-s) * sum(ch[k] * mp.zeta(s, mp.mpf(k) / 5) for k in range(1, 5))
def Lam(s): return (5 / mp.pi)**((s + 1) / 2) * mp.gamma((s + 1) / 2) * (((1 - 1j * kap) / 2) * Ld(s, chi) + ((1 + 1j * kap) / 2) * Ld(s, chib))
t = np.arange(50.0, 120.0001, 0.02); v = [mp.re(Lam(mp.mpc(0.5, x))) for x in t]
on = []
for k in range(len(t) - 1):
    if v[k] == 0 or v[k] * v[k + 1] < 0:
        lo, hi = t[k], t[k + 1]
        for _ in range(40):
            m = (lo + hi) / 2
            if mp.re(Lam(mp.mpc(0.5, lo))) * mp.re(Lam(mp.mpc(0.5, m))) <= 0: hi = m
            else: lo = m
        on.append((lo + hi) / 2)
off = []
for s0 in (mp.mpc('0.808517', '85.699348'), mp.mpc('0.650830', '114.163343')):
    r = mp.findroot(Lam, s0); off.append(complex(r)); off.append(complex(1 - r.real, r.imag))
# argument principle on the half-rectangle 1/2+50i -> 3+50i -> 3+120i -> 1/2+120i
def darg(path):
    tot = 0.0; prev = complex(Lam(path[0]))
    for s in path[1:]:
        cur = complex(Lam(s)); d = cmath.phase(cur / prev); tot += d; prev = cur
    return tot
P = [mp.mpc(x, 50) for x in np.arange(0.5, 3.0001, 0.005)] + [mp.mpc(3, y) for y in np.arange(50, 120.0001, 0.02)] + \
    [mp.mpc(x, 120) for x in np.arange(3.0, 0.4999, -0.005)]
Ncount = darg(P) / math.pi
print("DH: on-line zeros in [50,120]: %d ; off-line zeros found: %s ; argument-principle count in the strip: %.4f ; on + off = %d"
      % (len(on), [(round(z.real, 6), round(z.imag, 6)) for z in off], Ncount, len(on) + len(off)))
gD = [complex(g) for g in on] + [complex(-g) for g in on] + [complex(z.imag, -(z.real - 0.5)) for z in off] + [complex(-z.imag, -(z.real - 0.5)) for z in off]
TD = np.arange(60, 110, 0.01); WD = [W(T, gD) for T in TD]
i = int(np.argmin(WD)); T0 = TD[i]
pair = sum(K(g - T0) + K(g + T0) for g in gD if abs(g.imag) > 1e-9).real
print("DH: min over T in [60,110) of W(T) (zeros in [50,120] only) = %.4f at T = %.2f ; off-line pairs' share = %.4f ; on-line share = %.4f"
      % (WD[i], T0, pair, WD[i] - pair))
print("   out-of-window zeros contribute at most ~ 2 * 0.7 * 4 / (L * 10) = %.3f in absolute value (|gamma - T| >= 10 for T in [60,110])" % (2 * 0.7 * 4 / (L * 10)))
