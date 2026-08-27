# T4 supplemental: independent CUE Monte Carlo for the sine moments at lambda' = 1/2
# (fresh implementation, fresh seeds; finite-circle Hermitian frequency assembly
#  B[j,j'] = sqrt(u_j u_j') c_{j-j'}, the alias-free compression of RUN-REPORT dev.1).
import numpy as np, json, time

rng = np.random.default_rng(424242)
out = {}

def cue_angles(n):
    Z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / np.sqrt(2)
    Q, R = np.linalg.qr(Z)
    Q = Q * (np.diag(R) / np.abs(np.diag(R)))[None, :]
    ang = np.angle(np.linalg.eigvals(Q))
    return (ang % (2 * np.pi)) * n / (2 * np.pi)   # unfolded to circumference n

def moments(thetas, n, lam):
    J = int(round(lam * n / 2))
    js = np.arange(-J, J + 1); M = len(js)
    u = 1.0 / M
    smax = 2 * J
    svals = np.arange(-smax, smax + 1)
    c = np.exp(-2j * np.pi * np.outer(svals, thetas) / n).sum(axis=1)
    cdict = dict(zip(svals.tolist(), c))
    diff = js[:, None] - js[None, :]
    B = u * np.vectorize(lambda s: cdict[s])(diff)
    tr2 = np.real(np.sum(B * B.conj().T.conj().T))  # placeholder replaced below
    tr2 = np.real(np.trace(B @ B))
    tr3 = np.real(np.trace(B @ B @ B))
    return tr2 / n, tr3 / n

t0 = time.time()
for n, R in ((64, 600), (256, 300)):
    m2s, m3s = [], []
    for r in range(R):
        th = cue_angles(n)
        a, b = moments(th, n, 0.5)
        m2s.append(a); m3s.append(b)
    m2m, m2se = np.mean(m2s), np.std(m2s) / np.sqrt(R)
    m3m, m3se = np.mean(m3s), np.std(m3s) / np.sqrt(R)
    out[f"n{n}"] = {"R": R, "m2": m2m, "m2_se": m2se, "m3": m3m, "m3_se": m3se}
    print(f"n = {n} (R = {R}): m2(1/2) = {m2m:.5f}({m2se:.5f}), m3(1/2) = {m3m:.4f}({m3se:.4f})")
print(f"closed forms: 13/6 = {13/6:.5f}, 5; finite-n values must sit below with a ~1/n gap")
# crude 2-point 1/n extrapolation
x = np.array([1/64, 1/256]); y2 = np.array([out['n64']['m2'], out['n256']['m2']])
y3 = np.array([out['n64']['m3'], out['n256']['m3']])
m2inf = y2[1] + (y2[1] - y2[0]) * x[1] / (x[0] - x[1])
m3inf = y3[1] + (y3[1] - y3[0]) * x[1] / (x[0] - x[1])
out["extrap"] = {"m2_inf": m2inf, "m3_inf": m3inf}
print(f"two-point 1/n extrapolation: m2 -> {m2inf:.4f} (13/6 = {13/6:.4f}), m3 -> {m3inf:.4f} (5)")
print(f"elapsed {time.time()-t0:.1f}s")
json.dump(out, open("verify_t4_mc_out.json", "w"), indent=1, default=float)
print("WROTE verify_t4_mc_out.json")
