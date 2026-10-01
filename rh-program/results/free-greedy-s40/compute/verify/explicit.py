# explicit.py ZEROSFILE LOGTAG [XMIN=1e4] -- route 2 for alpha: psi_P(x) - x predicted by the zeros found,
#   P(x) = - sum_{zeros, t > 0} 2 Re(x^rho / rho) - sum_{real zeros} x^rho / rho,
# against the measured psi_P(x) - x (F rows of verify/logs/LOGTAG.log, 100 points per decade).
import sys, math, numpy as np
V = __file__.rsplit("/", 1)[0]
zf, tag = sys.argv[1], sys.argv[2]
xmin = float(sys.argv[3]) if len(sys.argv) > 3 else 1e4
Z = []
for ln in open(zf):
    p = ln.split()
    if p and not p[0].startswith("#"):
        Z.append(complex(float(p[0]), float(p[1])))
F = np.array([[float(v) for v in ln.split()[1:]] for ln in open(f"{V}/logs/{tag}.log") if ln.startswith("F ")])
x, d = F[:, 0], F[:, 4]
sel = x >= xmin; x, d = x[sel], d[sel]
lx = np.log(x)
P = np.zeros_like(x)
for z in Z:
    term = np.exp(z * lx) / z
    P -= (2 * term.real) if z.imag > 1e-9 else term.real
print(f"# explicit {zf} vs {tag}: {len(Z)} zeros (t > 0 counted with their conjugates)")
print("#  decade        rms(measured)   rms(predicted)  ratio   corr    | measured psi-x at end   predicted")
for k in range(int(math.log10(xmin)), int(math.log10(x[-1]) + 1e-9)):
    s = (x >= 10.0 ** k) & (x <= 10.0 ** (k + 1) * 1.0001)
    if s.sum() < 10: continue
    a, b = d[s], P[s]
    c = float(np.corrcoef(a, b)[0, 1])
    print(f"  [1e{k},1e{k + 1}]   {math.sqrt((a * a).mean()):14.1f}  {math.sqrt((b * b).mean()):14.1f}  {math.sqrt((b * b).mean() / (a * a).mean()):6.3f}  {c:+.3f}   | {a[-1]:14.1f}  {b[-1]:14.1f}")
# envelope exponents
for k in range(int(math.log10(xmin)), int(math.log10(x[-1]) + 1e-9)):
    s = (x >= 10.0 ** k) & (x <= 10.0 ** (k + 1) * 1.0001)
    if s.sum() < 10: continue
r = d - P
print(f"# residual (measured - predicted): rms over x >= {xmin:.0e} relative to rms(measured): {math.sqrt((r * r).mean() / (d * d).mean()):.3f}")
