"""o4a_z3_zeta_F.py — read-O: the zeros form Z3 on zeta and on F_{2.9,2}, own code from NOTE §6's definition.
g_T(x) = 2(1 - |x|/L)_+ cos(Tx), L = 20; ghat_T(gamma) = int g_T(x) e^{i gamma x} dx = K(gamma - T) + K(gamma + T),
K(xi) = L (sin(L xi/2)/(L xi/2))^2 (entire; evaluated at complex gamma_rho = -i(rho - 1/2) for off-line zeros).
W(T) = sum over ALL zeros rho (both signs of Im rho) of ghat_T(gamma_rho).
Zeta: Odlyzko zeros1 below 1e4 (10142 of them), both signs. F_{2.9,2} = zeta(s)(1 + 2.9 2^{-s} + 2^{1-2s}):
factor zeros from 2w^2 + 2.9w + 1 = 0, w = 2^{-s} (both roots negative real), all heights |t| < 1800, plus zeta's
zeros below 1e4. Grid scan, then local refinement (golden section on mpmath at 30 digits). Output o4a_z3_zeta_F.log."""
import numpy as np, mpmath as mp
L = 20.0
zs = np.loadtxt("../sources/odlyzko-zeros1.txt"); zs = zs[zs < 1e4]
out = ["zeta zeros below 1e4: %d (first %.6f, last %.6f)" % (len(zs), zs[0], zs[-1])]

def Kc(xi):  # numpy, complex-safe
    z = L * xi / 2
    with np.errstate(all="ignore"):
        r = np.where(np.abs(z) < 1e-8, 1.0 + 0j, np.sin(z) / np.where(np.abs(z) < 1e-8, 1, z))
    return L * r * r

def W_real(T, gam):  # gam: real positive zeros; both signs -> factor 2
    return 2 * (Kc(gam[None, :] - T[:, None]) + Kc(gam[None, :] + T[:, None])).real.sum(axis=1)

Ts = np.arange(0.0, 1e4, 0.05); vals = np.empty(len(Ts))
for i in range(0, len(Ts), 1000):
    vals[i:i + 1000] = W_real(Ts[i:i + 1000], zs)
j = int(vals.argmin())
out.append("zeta: min over T in [0, 1e4) step 0.05 of W(T) = %.6f at T = %.2f ; W(0) = %.6f ; second-smallest local region:" % (vals[j], Ts[j], vals[0]))
# interior minimum away from T = 0 (exclude T < 5) and away from the truncation edge (T > 9990)
mask = (Ts > 5) & (Ts < 9990)
k = int(np.where(mask, vals, np.inf).argmin())
out.append("   interior min (5 < T < 9990) = %.6f at T = %.2f ; W at T = 9999.95 (truncation edge) = %.4f" % (vals[k], Ts[k], vals[-1]))
mp.mp.dps = 30
W0 = 2 * sum(2 * L * (mp.sin(L * mp.mpf(g) / 2) / (L * mp.mpf(g) / 2)) ** 2 for g in zs)
out.append("   W(0) at 30 digits = %s" % mp.nstr(W0, 10))
# F_{2.9,2}
a = mp.mpf("2.9"); ln2 = mp.log(2)
roots = [(-a + s * mp.sqrt(a * a - 8)) / 4 for s in (1, -1)]
betas = sorted([-mp.log(abs(w)) / ln2 for w in roots])
out.append("F_{2.9,2}: factor zeros Re s = %s, %s ; t = (2j+1) pi/log 2, pi/log 2 = %s"
           % (mp.nstr(betas[1], 12), mp.nstr(betas[0], 12), mp.nstr(mp.pi / ln2, 14)))
gf = []
for jj in range(-200, 200):
    t = (2 * jj + 1) * float(mp.pi / ln2)
    for b in betas: gf.append(complex(t, -(float(b) - 0.5)))
gf = np.array(gf); gzF = zs[:3000]
def WF(T):
    T = np.atleast_1d(T)
    fac = (Kc(gf[None, :] - T[:, None]) + Kc(gf[None, :] + T[:, None])).sum(axis=1).real
    return fac + W_real(T, gzF)
TF = np.arange(0.5, 30, 0.01); vF = WF(TF); i = int(vF.argmin())
out.append("   grid min over T in [0.5, 30) step 0.01: %.4f at T = %.2f" % (vF[i], TF[i]))
# refine with mpmath golden section around the grid minimum
def WFmp(T):
    T = mp.mpf(T); s = mp.mpf(0)
    def K(x):
        z = L * x / 2
        return L * (mp.sin(z) / z) ** 2 if abs(z) > 1e-20 else mp.mpf(L)
    for g in gf: s += mp.re(K(mp.mpc(g.real, g.imag) - T) + K(mp.mpc(g.real, g.imag) + T))
    for g in gzF[:600]: s += 2 * (K(mp.mpf(g) - T) + K(mp.mpf(g) + T))
    return s
lo, hi = TF[i] - 0.02, TF[i] + 0.02
gr = (mp.sqrt(5) - 1) / 2
x1, x2 = hi - gr * (hi - lo), lo + gr * (hi - lo); f1, f2 = WFmp(x1), WFmp(x2)
for _ in range(30):
    if f1 < f2: hi, x2, f2 = x2, x1, f1; x1 = hi - gr * (hi - lo); f1 = WFmp(x1)
    else: lo, x1, f1 = x1, x2, f2; x2 = lo + gr * (hi - lo); f2 = WFmp(x2)
out.append("   refined min (mpmath, zeta zeros truncated at 600 for the refinement): W = %s at T = %s" % (mp.nstr(f1, 10), mp.nstr(x1, 8)))
open("o4a_z3_zeta_F.log", "w").write("\n".join(out) + "\n")
print("\n".join(out))
