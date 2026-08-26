# T1 verification: grid Parseval decoupling.
# Finite-circle model (SPEC 1.4): flat window, bandwidth lambda, circle of circumference N,
# harmonics j with |j| <= lambda*N/2, u_j = 1/M (M = number of harmonics),
# c_s = sum_z m_z exp(-2 pi i s theta_z / N),
# tr G^2 = sum_{j1,j2} u_{j1} u_{j2} |c_{j1+j2}|^2 = sum_s W2(s) |c_s|^2.
# Claim (T1): on the (N+1)-site uniform grid (spacing N/(N+1)), at bandwidth 1 (M = N+1, N even),
# tr G_1^2 = sum_z m_z^2 EXACTLY for every site subset and mark assignment.
import numpy as np, json

rng = np.random.default_rng(20260826)
out = {}

def F_lambda(N, lam, thetas, marks):
    """tr G_lambda^2 by the SPEC 1.4 Fourier assembly (direct double sum over harmonics)."""
    J = int(round(lam * N / 2))
    js = np.arange(-J, J + 1)
    M = len(js)
    u = np.full(M, 1.0 / M)
    # c_s for all needed s = j1 + j2 in [-2J, 2J]
    svals = np.arange(-2 * J, 2 * J + 1)
    c = np.array([np.sum(marks * np.exp(-2j * np.pi * s * thetas / N)) for s in svals])
    # W2(s) = sum_j u_j u_{s-j} = (# pairs) / M^2 = (M - |s|)_+ / M^2
    W2 = np.maximum(M - np.abs(svals), 0) / M**2
    return float(np.sum(W2 * np.abs(c) ** 2))

def eig_F(N, lam, thetas, marks):
    """Same via the Hermitian frequency matrix B[j,j'] = sqrt(u_j u_j') c_{j-j'} (RUN-REPORT dev.1)."""
    J = int(round(lam * N / 2))
    js = np.arange(-J, J + 1)
    M = len(js)
    u = np.full(M, 1.0 / M)
    diff = js[:, None] - js[None, :]
    cmat = np.zeros_like(diff, dtype=complex)
    for s in np.unique(diff):
        cs = np.sum(marks * np.exp(-2j * np.pi * s * thetas / N))
        cmat[diff == s] = cs
    B = np.sqrt(np.outer(u, u)) * cmat
    ev = np.linalg.eigvalsh(B)
    return float(np.sum(ev**2)), ev

# --- (1) exactness on the grid, N = 64 and 128, random subsets and marks 1..8 ---
for N in (64, 128):
    devs, devs_eig = [], []
    for r in range(40):
        nsites = rng.integers(1, N + 2)
        sites = rng.choice(N + 1, size=nsites, replace=False)
        marks = rng.integers(1, 9, size=nsites).astype(float)
        thetas = sites * N / (N + 1.0)
        F1 = F_lambda(N, 1.0, thetas, marks)
        devs.append(abs(F1 - np.sum(marks**2)))
        if r < 6:
            F1e, _ = eig_F(N, 1.0, thetas, marks)
            devs_eig.append(abs(F1e - np.sum(marks**2)))
    out[f"grid_exact_N{N}_maxdev"] = max(devs)
    out[f"grid_exact_N{N}_maxdev_eig"] = max(devs_eig)
    print(f"N={N}: max |F1 - sum m^2| over 40 random grid configs = {max(devs):.3e} "
          f"(eig route, 6 configs: {max(devs_eig):.3e})")

# --- (2) control: OFF-grid configurations do NOT satisfy the identity ---
N = 64
devs_off = []
for r in range(20):
    nsites = rng.integers(2, 40)
    thetas = np.sort(rng.uniform(0, N, size=nsites))
    marks = rng.integers(1, 3, size=nsites).astype(float)
    F1 = F_lambda(N, 1.0, thetas, marks)
    devs_off.append(abs(F1 - np.sum(marks**2)))
out["offgrid_maxdev"] = max(devs_off)
out["offgrid_mindev"] = min(devs_off)
print(f"control (positions uniform, off-grid): |F1 - sum m^2| in "
      f"[{min(devs_off):.3e}, {max(devs_off):.3e}]  (generically NONZERO)")

# --- (3) the lambda' = 1/2 kernel is alive on the same grid ---
devs_half = []
for r in range(10):
    nsites = rng.integers(2, 66)
    sites = rng.choice(N + 1, size=nsites, replace=False)
    marks = rng.integers(1, 3, size=nsites).astype(float)
    thetas = sites * N / (N + 1.0)
    Fp = F_lambda(N, 0.5, thetas, marks)
    devs_half.append(abs(Fp - np.sum(marks**2)))
out["halfband_grid_dev_range"] = [min(devs_half), max(devs_half)]
print(f"lambda'=1/2 on the same grid: |F' - sum m^2| in "
      f"[{min(devs_half):.3e}, {max(devs_half):.3e}]  (kernel ALIVE: not decoupled)")

# --- (4) general flat-band lemma: M consecutive harmonics, M-site grid, ANY band offset ---
# tr G^2 with band {j0, ..., j0+M-1}, u_j = 1/M, sites k*N/M on circumference N.
def F_band(N, j0, M, sites, marks):
    js = np.arange(j0, j0 + M)
    thetas = sites * N / float(M)
    svals = np.arange(2 * j0, 2 * (j0 + M) - 1)
    c = np.array([np.sum(marks * np.exp(-2j * np.pi * s * thetas / N)) for s in svals])
    W2 = np.array([min(s - 2 * j0, 2 * (j0 + M - 1) - s) + 1 for s in svals]) / M**2
    return float(np.sum(W2 * np.abs(c) ** 2))

devg = []
for r in range(20):
    N2 = int(rng.integers(10, 200))
    M2 = int(rng.integers(2, 80))
    j0 = int(rng.integers(-40, 40))
    nsites = int(rng.integers(1, M2 + 1))
    sites = rng.choice(M2, size=nsites, replace=False)
    marks = rng.integers(1, 9, size=nsites).astype(float)
    devg.append(abs(F_band(N2, j0, M2, sites, marks) - np.sum(marks**2)))
out["general_band_lemma_maxdev"] = max(devg)
print(f"general flat-band lemma (random N, M, offset j0, 20 draws): max dev = {max(devg):.3e}")

# --- (5) continuum analog: integer lattice under sinc ---
def sinc(x):
    return np.sinc(x)  # np.sinc(x) = sin(pi x)/(pi x)

devs_c = []
for r in range(20):
    npts = rng.integers(2, 200)
    pos = rng.choice(4000, size=npts, replace=False).astype(float)  # integer lattice points
    marks = rng.integers(1, 9, size=npts).astype(float)
    D = pos[:, None] - pos[None, :]
    K = sinc(D) ** 2  # psi_1 = sinc(pi x): np.sinc uses sin(pi x)/(pi x)
    F1 = float(marks @ K @ marks)
    devs_c.append(abs(F1 - np.sum(marks**2)))
out["continuum_lattice_maxdev"] = max(devs_c)
print(f"continuum integer lattice under sinc: max |F1 - sum m^2| = {max(devs_c):.3e}")

# half-band on the lattice: psi_{1/2}(k) = sinc(pi k / 2) = 2/(pi k) (odd k) -- alive
ks = np.array([1, 3, 5, 7])
vals = np.sinc(ks / 2.0)
pred = 2.0 / (np.pi * ks) * np.array([1, -1, 1, -1])
out["halfband_lattice_check"] = float(np.max(np.abs(vals - pred)))
print(f"psi_1/2 at odd lattice offsets vs 2/(pi k)(-1)^((k-1)/2): max dev = {out['halfband_lattice_check']:.3e}")

json.dump(out, open("verify_t1_out.json", "w"), indent=1)
print("WROTE verify_t1_out.json")
