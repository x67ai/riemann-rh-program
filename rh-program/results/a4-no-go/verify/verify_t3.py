# T3 verification: exact off-line pair block law and the affine-plane identity.
# (i)  evaluation-vector route (continuum, windows at critical spacing 2 pi / L):
#      x_k = phihat(gamma + i delta - tau_k);  sum_k x_k^2 = L * Phi(0) (real, depth/position-indep);
#      sum_k |x_k|^2 = L * Phi(2 i delta);  block 2m(pp^T - qq^T), <p,q> = 0,
#      eigenvalues m(1 +/- A), A = Phi(2 i delta)/Phi(0);
# (ii) flat window: A(w) = sinh(w)/w at w = L*delta (dimensionless depth);
# (iii) charges: trace 2m, Frobenius 2m^2(1+A^2), cubic 2m^3(1+3A^2);
#      per-zero identity c = 3F - 2 (m = 1, every depth); atoms c = 3F - 2 + (m-1)(m-2);
#      general pair mult m: c - (3F - 2) = (m-1)(m-2) + 3m(m-1)A^2.
import numpy as np, json
from scipy.integrate import quad

out = {}
L = 40.0                       # window length (units where positions are tau)
spacing = 2 * np.pi / L        # critical window spacing
KMAX = 60000                   # window truncation

def phihat_flat(z):
    # phi = 1 on [-L/2, L/2]: phihat(z) = int_{-L/2}^{L/2} e^{-i s z} ds = 2 sin(L z / 2)/z
    z = np.asarray(z, dtype=complex)
    smallz = np.abs(z) < 1e-12
    val = np.where(smallz, L, 2 * np.sin(L * z / 2) / np.where(smallz, 1, z))
    return val

def phihat_cos(z):
    # phi(s) = cos(pi s / L) on [-L/2, L/2]:
    # phihat(z) = int cos(pi s/L) e^{-isz} ds = (2 pi / L) * cos(Lz/2) / ((pi/L)^2 - z^2)
    z = np.asarray(z, dtype=complex)
    a = np.pi / L
    denom = a**2 - z**2
    small = np.abs(denom) < 1e-10
    val = np.where(small, L / 2.0, 2 * a * np.cos(L * z / 2) / np.where(small, 1, denom))
    return val

def A_theory(profile, delta):
    if profile == "flat":
        w = L * delta
        return np.sinh(w) / w if w != 0 else 1.0
    # A(delta) = int phi^2 cosh(2 delta s) ds / int phi^2
    num = quad(lambda s: np.cos(np.pi * s / L) ** 2 * np.cosh(2 * delta * s), -L / 2, L / 2)[0]
    den = quad(lambda s: np.cos(np.pi * s / L) ** 2, -L / 2, L / 2)[0]
    return num / den

for profile, phihat in (("flat", phihat_flat), ("cos", phihat_cos)):
    a_const = {"flat": L, "cos": L / 2.0}[profile]      # a = L^{-1} int phi^2 => L^2 a = L * int phi^2
    norm = L * a_const                                   # = L * int phi^2 = L^2 a
    rows = []
    for w_dimless in (1 / 64, 1 / 8, 1 / 4, 1 / 2, 3 / 4, 1.0, 2.0):
        delta = w_dimless / L
        for gamma in (0.0, 0.37137, 2.7182818):          # position-independence probe
            taus = (np.arange(-KMAX, KMAX + 1)) * spacing
            x = phihat(gamma + 1j * delta - taus)
            xTx = np.sum(x ** 2)
            xx = np.sum(np.abs(x) ** 2)
            p, q = np.real(x), np.imag(x)
            pq = float(p @ q)
            A_num = xx / norm
            A_th = A_theory(profile, delta)
            # block for m = 1, normalized by L^2 a: eigenvalues of 2(pp^T - qq^T)/norm
            # rank-2: nonzero eigenvalues are 2|p|^2/norm and -2|q|^2/norm given p.q = 0
            lam_plus = 2 * float(p @ p) / norm
            lam_minus = -2 * float(q @ q) / norm
            rows.append({
                "w": w_dimless, "gamma": gamma,
                "xTx_over_norm_minus_1": abs(xTx / norm - 1),
                "pq_over_norm": abs(pq) / norm,
                "A_num": A_num, "A_th": A_th, "A_dev": abs(A_num - A_th),
                "lam_plus_dev": abs(lam_plus - (1 + A_th)),
                "lam_minus_dev": abs(lam_minus - (1 - A_th)),
            })
    worst = {k: max(r[k] for r in rows) for k in
             ("xTx_over_norm_minus_1", "pq_over_norm", "A_dev", "lam_plus_dev", "lam_minus_dev")}
    out[f"block_{profile}"] = worst
    print(f"[{profile}] worst over w in {{1/64..2}}, 3 positions: "
          f"|x^T x/L^2a - 1| = {worst['xTx_over_norm_minus_1']:.2e}, |<p,q>|/L^2a = {worst['pq_over_norm']:.2e}, "
          f"|A_num - A_th| = {worst['A_dev']:.2e}, eig devs = {worst['lam_plus_dev']:.2e}/{worst['lam_minus_dev']:.2e}")

# --- SPEC 1.2 flat A-values ---
spec_vals = {1/8: 1.00261, 1/4: 1.01045, 1/2: 1.04219, 3/4: 1.09642, 1.0: 1.17520, 2.0: 1.81343}
devs = {}
for w, v in spec_vals.items():
    mine = np.sinh(w) / w
    devs[w] = abs(mine - v)
    print(f"A({w}) = sinh(w)/w = {mine:.6f}  vs SPEC {v}  dev {devs[w]:.1e}")
out["spec_A_values_maxdev"] = max(devs.values())

# --- charges and the per-zero identity (exact algebra checked numerically) ---
ident = []
for m in (1, 2, 3, 5):
    for w in (1e-9, 1/64, 1/8, 1/2, 1.0, 2.0):
        A = np.sinh(w) / w if w > 0 else 1.0
        tr = m * (1 + A) + m * (1 - A)
        fro = (m * (1 + A)) ** 2 + (m * (1 - A)) ** 2
        cub = (m * (1 + A)) ** 3 + (m * (1 - A)) ** 3
        ident.append(abs(tr - 2 * m))
        ident.append(abs(fro - 2 * m**2 * (1 + A**2)))
        ident.append(abs(cub - 2 * m**3 * (1 + 3 * A**2)))
        # per-zero: F = fro/(2m) per unit mass?  per-zero (per unit of mass 2m): F = fro/(2m), c = cub/(2m)
        F = fro / (2 * m); c = cub / (2 * m)
        ident.append(abs((c - (3 * F - 2)) - ((m - 1) * (m - 2) + 3 * m * (m - 1) * A**2)))
out["charge_identity_maxdev"] = max(ident)
print(f"charges + per-zero identity (m in 1,2,3,5; all depths): max dev = {max(ident):.2e}")
print("  m = 1 pairs: c - (3F - 2) = 0 exactly at every depth (formula value = 0)")

# --- atoms: c = 3F - 2 + (m-1)(m-2), per unit mass F = m, c = m^2 ---
atom_dev = max(abs(m**2 - (3 * m - 2 + (m - 1) * (m - 2))) for m in range(1, 30))
out["atom_identity_maxdev"] = atom_dev
print(f"atom identity m^2 = 3m - 2 + (m-1)(m-2), m = 1..29: max dev = {atom_dev}")

# --- shallow-pair continuity: w -> 0 spectrum -> (2m, 0), cubic -> 8 m^3 ---
for w in (1/64, 1/8):
    A = np.sinh(w) / w
    print(f"w = {w}: eigenvalues (m=1) = ({1+A:.6f}, {1-A:.6f}), cubic charge = {2*(1+3*A**2):.4f}")
out["cubic_w_1_64"] = 2 * (1 + 3 * (np.sinh(1/64)/(1/64))**2)
out["cubic_w_1_8"] = 2 * (1 + 3 * (np.sinh(1/8)/(1/8))**2)

# --- master-formula 2x2 kernel route (consistency): K = [[1, A],[A, 1]], moments m^k tr K^k ---
for m in (1, 3):
    for w in (1/8, 1.0):
        A = np.sinh(w) / w
        K = np.array([[1, A], [A, 1]])
        t1 = m * np.trace(K); t2 = m**2 * np.trace(K @ K); t3 = m**3 * np.trace(K @ K @ K)
        assert abs(t1 - 2 * m) < 1e-12 and abs(t2 - 2 * m**2 * (1 + A**2)) < 1e-12 \
               and abs(t3 - 2 * m**3 * (1 + 3 * A**2)) < 1e-11
print("master-formula 2x2 kernel route reproduces (2m, 2m^2(1+A^2), 2m^3(1+3A^2)): PASS")

json.dump(out, open("verify_t3_out.json", "w"), indent=1, default=float)
print("WROTE verify_t3_out.json")
