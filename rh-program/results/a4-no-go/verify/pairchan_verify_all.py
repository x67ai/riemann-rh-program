"""Pair-interference channel (AUDIT MINOR-4): consolidated verification suite.

Independent implementation (NOT the gate's code): finite-circle model N = 64,
lambda = 1 flat window, u_j = 1/65 (|j| <= 32), w_s = (65-|s|)/65^2,
  c_s = sum_atoms m e^{-2 pi i s theta/64} + sum_pairs 2 m cosh(2 pi s d/64) e^{-2 pi i s theta/64},
  F1  = sum_{|s|<=64} w_s |c_s|^2.
Targets: S2 = sum_a m^2 + 2 sum_p m^2;  T = sum_a (3m-2) + sum_p (6m-4) = 3M - 2N_d.

Sections:
  V  basic identities (grid Parseval, block law, witness, translate sums, C-S chain)
  X  fractional-mark counterexample (exact formula match)
  I  exact interference identity (single pair)
  D  spectral backstop facts: B Hermitian, tr B = M, tr B^2 = F1, n_+(B) <= n_at + n_pr
  C  capacity curves: nu(y), S1(y), S1corr(y), joint-kernel Sgen2 windows
Writes pairchan_verify_out.json next to this file.
"""
import json
import os
import numpy as np

N = 64
J = 32
S = np.arange(-2 * J, 2 * J + 1)
W = (65 - np.abs(S)) / 65.0 ** 2
JJ = np.arange(-J, J + 1)
U = np.full(65, 1.0 / 65.0)
Delta = N / 65.0
GRID = np.arange(65) * Delta
OUT = {}

def abar(x):
    return float(np.sum(U * np.cosh(2.0 * np.pi * JJ * x / N)))

def psiN(z):
    return complex(np.sum(U * np.exp(-2j * np.pi * JJ * z / N)))

def assemble_c(atoms, pairs):
    c = np.zeros(len(S), dtype=complex)
    for (th, m) in atoms:
        c += m * np.exp(-2j * np.pi * S * th / N)
    for (th, d, m) in pairs:
        c += 2.0 * m * np.cosh(2.0 * np.pi * S * d / N) * np.exp(-2j * np.pi * S * th / N)
    return c

def F1(atoms, pairs):
    return float(np.sum(W * np.abs(assemble_c(atoms, pairs)) ** 2))

def S2(atoms, pairs):
    return sum(m * m for _, m in atoms) + 2 * sum(m * m for _, _, m in pairs)

def Tgt(atoms, pairs):
    return sum(3 * m - 2 for _, m in atoms) + sum(6 * m - 4 for _, _, m in pairs)

rng = np.random.default_rng(20260826)

# ---------- V ----------
errs = []
for _ in range(40):
    k = rng.integers(5, 66)
    sites = rng.choice(65, size=k, replace=False)
    marks = rng.integers(1, 9, size=k)
    atoms = [(GRID[i], int(m)) for i, m in zip(sites, marks)]
    errs.append(abs(F1(atoms, []) - S2(atoms, [])))
OUT["V_grid_parseval_maxerr"] = max(errs)
errs = []
for _ in range(20):
    th, d, m = rng.uniform(0, N), rng.uniform(0.01, 1.0), int(rng.integers(1, 5))
    errs.append(abs(F1([], [(th, d, m)]) - 2 * m * m * (1 + abar(2 * d) ** 2)))
OUT["V_pair_block_maxerr"] = max(errs)
vac = [(GRID[i], 1) for i in range(1, 65)]
OUT["V_vacancy_F1"] = F1(vac, [])
OUT["V_32doubles_F1"] = F1([(GRID[i], 2) for i in range(32)], [])
tr_err = []
for d in (0.1, 0.3, 0.7):
    x = rng.uniform(0, 1)
    s1 = sum((psiN(x + g + 1j * d) ** 2).real for g in GRID)
    s2v = sum(abs(psiN(x + g + 1j * d)) ** 2 for g in GRID)
    tr_err.append(abs(s1 - 1.0))
    tr_err.append(abs(s2v - abar(2 * d)))
OUT["V_translate_identities_maxerr"] = max(tr_err)
OUT["V_CS_chain_max_violation"] = max(
    abar(d) ** 2 - (1 + abar(2 * d)) / 2 for d in np.linspace(0.01, 2.5, 60))

# ---------- X ----------
d, mu = 0.25, 0.05
f = F1(vac, [(0.0, d, mu)]); s = S2(vac, [(0.0, d, mu)])
pred = 2 * mu ** 2 * abar(2 * d) ** 2 - 4 * mu * (abar(d) ** 2 - 1)
OUT["X_fractional_F1_minus_S2"] = f - s
OUT["X_fractional_predicted"] = pred
OUT["X_violates"] = bool(f < s)

# ---------- I ----------
errs = []
for _ in range(25):
    na = int(rng.integers(1, 8))
    atoms = [(float(rng.uniform(0, N)), int(rng.integers(1, 5))) for _ in range(na)]
    th, dd, m = float(rng.uniform(0, N)), float(rng.uniform(0.02, 1.2)), int(rng.integers(1, 4))
    lhs = F1(atoms, [(th, dd, m)]) - Tgt(atoms, [(th, dd, m)])
    slacks = sum((ma - 1) * (ma - 2) for _, ma in atoms) + 2 * (m - 1) * (m - 2)
    crosses = sum(atoms[i][1] * atoms[j][1] * (psiN(atoms[i][0] - atoms[j][0]) ** 2).real
                  for i in range(na) for j in range(na) if i != j)
    coupling = 4 * m * sum(ma * (psiN(ta - th + 1j * dd) ** 2).real for ta, ma in atoms)
    errs.append(abs(lhs - (slacks + crosses + coupling + 2 * m * m * abar(2 * dd) ** 2)))
OUT["I_identity_maxerr"] = max(errs)

# ---------- D ----------
def Bmat(atoms, pairs):
    c = assemble_c(atoms, pairs)          # c_s for s in -64..64; index s+64
    B = np.zeros((65, 65), dtype=complex)
    for a in range(65):
        for b in range(65):
            B[a, b] = np.sqrt(U[a] * U[b]) * c[(a - b) + 64]
    return B
chk = []
for _ in range(12):
    na, k = int(rng.integers(0, 5)), int(rng.integers(1, 4))
    atoms = [(float(rng.uniform(0, N)), int(rng.integers(1, 4))) for _ in range(na)]
    pairs = [(float(rng.uniform(0, N)), float(rng.uniform(0.05, 1.5)),
              int(rng.integers(1, 3))) for _ in range(k)]
    B = Bmat(atoms, pairs)
    ev = np.linalg.eigvalsh(B)
    M = sum(m for _, m in atoms) + 2 * sum(m for _, _, m in pairs)
    chk.append({
        "trB_minus_M": float(abs(ev.sum() - M)),
        "trB2_minus_F1": float(abs((ev ** 2).sum() - F1(atoms, pairs))),
        "npos": int((ev > 1e-9).sum()),
        "n_at_plus_n_pr": na + k,
        "npos_ok": bool((ev > 1e-9).sum() <= na + k),
        "backstop_holds": bool((na + 2 * k) >= (4.0 / 9.0) * (3 * M - F1(atoms, pairs)) - 1e-9),
    })
OUT["D_spectral_checks"] = chk
OUT["D_all_npos_ok"] = all(c["npos_ok"] for c in chk)
OUT["D_max_trB_err"] = max(c["trB_minus_M"] for c in chk)
OUT["D_max_trB2_err"] = max(c["trB2_minus_F1"] for c in chk)

# ---------- C ----------
xs = np.linspace(0, N, 12001, endpoint=False)
cell_idx = np.floor((xs / Delta) + 0.5).astype(int) % 65
def Rarr(y):
    if y < 1e-9:
        return np.array([abs(psiN(x)) ** 2 for x in xs])
    return np.array([(psiN(x + 1j * y) ** 2).real for x in xs])
Rcache = {}
def R(y):
    key = round(float(y), 4)
    if key not in Rcache:
        Rcache[key] = Rarr(key)
    return Rcache[key]
def nu_of(arr):
    return float(sum(max(0.0, float(np.max(-arr[cell_idx == k]))) for k in range(65)))

nu_tab, S1_tab = {}, {}
ygrid = [round(y, 3) for y in np.arange(0.01, 1.01, 0.01)] + [1.25, 1.5, 1.75, 2.0]
S1max = 0.0
for y in ygrid:
    nu = nu_of(R(y))
    nu_tab[y] = nu
    S1_tab[y] = 8 * nu / (2 * abar(2 * y) ** 2)
    S1max = max(S1max, S1_tab[y])
OUT["C_S1_max"] = S1max
for yx in (0.159, 0.318, 0.3183):
    if yx not in nu_tab:
        nu_tab[yx] = nu_of(R(yx))
OUT["C_nu_table"] = {str(y): round(nu_tab[y], 5) for y in
                     (0.05, 0.1, 0.159, 0.2, 0.25, 0.318, 0.4, 0.5, 0.7, 1.0, 1.5, 2.0)}
# S1corr threshold
def s1corr(y):
    Ry = R(y); kmax = 0.0; nu = 0.0; zw = 0.0
    for k in range(65):
        seg = -Ry[cell_idx == k]; mx = max(0.0, float(np.max(seg)))
        nu += mx; kmax = max(kmax, mx)
        xs_k = xs[cell_idx == k]; neg = xs_k[seg > 0]
        if len(neg) > 1:
            span = float(neg.max() - neg.min())
            if span < 5:
                zw = max(zw, span)
    c0 = abs(psiN(min(zw, 0.9))) ** 2 if zw > 0 else 1.0
    best = max(4 * L * kmax - c0 * max(0, L * (L - 2)) for L in range(1, 80))
    mult = best / (8 * kmax) if kmax > 0 else 1.0
    return (8 * nu / (2 * abar(2 * y) ** 2)) * max(1.0, mult), kmax, zw, c0
OUT["C_S1corr_at_0.45"] = s1corr(0.45)[0]
OUT["C_S1corr_at_0.3183"] = s1corr(0.3183)[0]
OUT["C_S1corr_at_0.159"] = s1corr(0.159)[0]
# joint-kernel window (cap-2, Theorem B refined) and cap-4 (unconditional chain)
dgrid = [round(d, 3) for d in np.arange(0.004, 0.1601, 0.004)]
def sgen2(dcap, capmult):
    worst, wd = 0.0, None
    for d in dgrid:
        if d > dcap + 1e-9:
            continue
        sup_j = 0.0
        for dp in dgrid:
            if dp > dcap + 1e-9:
                continue
            nj = nu_of(R(round(d + dp, 4)) + R(round(abs(d - dp), 4)))
            sup_j = max(sup_j, nj)
        val = (8 * nu_of(R(d)) + capmult * sup_j) / (2 * abar(2 * d) ** 2)
        if val > worst:
            worst, wd = val, d
    return worst, wd
OUT["C_Sgen2_cap2_window_1over2pi"] = sgen2(1 / (2 * np.pi), 4)
w_unc = None
for dcap in (0.08, 0.10, 0.11, 0.115, 0.12, 0.125, 0.13):
    w, _ = sgen2(dcap, 8)
    if w <= 1.0:
        w_unc = dcap
OUT["C_capmult8_largest_ok_dcap"] = w_unc
OUT["C_deep_ratio_y1"] = abar(2.0) / abar(1.0)
OUT["C_deep_ratio_y1.1"] = abar(2.2) / abar(1.1)
OUT["alpha_exact"] = (np.pi / 64) ** 2 * (65 ** 2 - 1) / 3.0
OUT["abar_values"] = {str(x): round(abar(x), 6) for x in
                      (0.1, 0.159, 0.2, 0.3183, 0.4, 0.6366, 1.0, 2.0, 2.2)}

here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "pairchan_verify_out.json"), "w") as fh:
    json.dump(OUT, fh, indent=1, default=str)
print(json.dumps(OUT, indent=1, default=str))
