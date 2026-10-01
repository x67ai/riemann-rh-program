# star_check.py — test of NOTE §6.2 (★) on S8(pi/16) (own dump, g-integers <= 1e6) and on the template.
# (1) exact local Chebyshev identity: sum_{n in G cap I} log n = sum_{beta <= x+h} Lambda(beta) * #(G cap I/beta)
# (2) psi(I) = sum_{beta in I} Lambda(beta) >= 0, and its Mertens form
#     slack(I) := Delta R(I) log x + A h - sum_{beta <= x} Lambda(beta) Delta R(I/beta)   (should equal psi(I) + small)
#     with A = rho + int_1^inf R(u) u^-2 du (estimated from the data; tail beyond 1e6 with R ~ 1 - rho + mean E).
import numpy as np
rho = np.pi/16; t = 1/rho; X = 1e6
g = np.fromfile('/private/tmp/rh-s41-lemmaB-U5-obstruction/g_pi16_1e6.bin', dtype=np.float64)
G = np.concatenate([[1.0], g[g <= X]]); G.sort()
k = np.rint((G - 1)/t + 0.5); onlat = np.abs(G - (1 + (k - 0.5)*t)) < 1e-13*G
P = G[1:][onlat[1:]]                                  # g-primes = atoms on the lattice
print(f"N(1e6)={len(G)}  primes={len(P)}  (s8u5 log: 196350, 72603)")
beta, lam = [], []
for p in P:
    q = p
    while q <= X: beta.append(q); lam.append(np.log(p)); q *= p
o = np.argsort(beta); beta = np.array(beta)[o]; lam = np.array(lam)[o]
def Ncount(a, b):                                     # #(G cap (a, b]) vectorized
    return np.searchsorted(G, b, 'right') - np.searchsorted(G, a, 'right')
# A = rho + int_1^inf R u^-2 du, R(u) = N(u) - rho u piecewise
a = np.append(G, X); c = np.arange(1, len(G) + 1)     # N = c_j on [G_j, G_{j+1})
lo, hi = a[:-1], a[1:]
intR = np.sum(c*(1/lo - 1/hi)) - rho*np.sum(np.log(hi/lo))
Ebar = np.mean((c - rho*(lo - 1) - 1)[lo > X/2]); intR += (1 - rho + Ebar)/X
A = rho + intR; print(f"A = rho + int R u^-2 = {A:.6f}   (template value 1; log-mean check E-bar(top half) = {Ebar:.3f})")
rng = np.random.default_rng(7); worst = {}; ident = 0.0
for h in (1.0, 5.0, 20.0, 100.0):
    xs = rng.uniform(2e5, 9e5, 400); rows = []
    for x in xs:
        nI = G[(G > x) & (G <= x + h)]; lhs = np.sum(np.log(nI))
        m = beta <= x + h; cnt = Ncount(x/beta[m], (x + h)/beta[m]); rhs = np.sum(lam[m]*cnt)
        ident = max(ident, abs(lhs - rhs))
        psiI = np.sum(lam[(beta > x) & (beta <= x + h)])
        mb = beta <= x; dR = Ncount(x/beta[mb], (x + h)/beta[mb]) - rho*h/beta[mb]
        dRI = len(nI) - rho*h; slack = dRI*np.log(x) + A*h - np.sum(lam[mb]*dR)
        rows.append((psiI, slack))
    r = np.array(rows); d = r[:, 1] - r[:, 0]
    print(f"h={h:6.1f}: min psi(I) {r[:,0].min():.3f}   min slack {r[:,1].min():.3f}   "
          f"slack - psi: mean {d.mean():+.4f}  max|.| {np.abs(d).max():.4f}  (Mertens o(1)*h scale: {h*0.05:.3f})")
print(f"max |exact identity defect| over all windows: {ident:.2e}")
# template: psi_c(I) = int_I (1 - u^-rho) du >= 0; (★) with Delta R = 0 reads 0 <= A h, A = 1, slack - psi = h x^-rho
x = 5e5; h = 20.0; print(f"template at x=5e5, h=20: psi_c(I) = {h*(1 - x**-rho):.4f}, slack = A h = {h:.4f}, diff h x^-rho = {h*x**-rho:.4f}")
