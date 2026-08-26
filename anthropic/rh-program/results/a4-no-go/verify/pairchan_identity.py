"""Verify the exact single-pair interference identity, the hole-margin formula,
the capacity-margin curve, and refined depth-resolved worst-case searches."""
import numpy as np
from scipy.optimize import minimize
from pairchan_core import N, GRID, F1, S2, Tgt, abar, psiN

rng = np.random.default_rng(1234)

# ---- I1: exact identity  F1 - T = slacks + crosses + coupling + 2 m^2 abar(2d)^2
print("== I1: exact single-pair identity ==")
errs = []
for _ in range(25):
    na = int(rng.integers(1, 8))
    atoms = [(float(rng.uniform(0, N)), int(rng.integers(1, 5))) for _ in range(na)]
    th, d, m = float(rng.uniform(0, N)), float(rng.uniform(0.02, 1.2)), int(rng.integers(1, 4))
    lhs = F1(atoms, [(th, d, m)]) - Tgt(atoms, [(th, d, m)])
    slacks = sum((ma - 1) * (ma - 2) for _, ma in atoms) + 2 * (m - 1) * (m - 2)
    crosses = sum(atoms[i][1] * atoms[j][1] * (psiN(atoms[i][0] - atoms[j][0]) ** 2).real
                  for i in range(na) for j in range(na) if i != j)
    coupling = 4 * m * sum(ma * (psiN(ta - th + 1j * d) ** 2).real for ta, ma in atoms)
    rhs = slacks + crosses + coupling + 2 * m * m * abar(2 * d) ** 2
    errs.append(abs(lhs - rhs))
print(f"   max |identity error| over 25 random configs = {max(errs):.3e}")

# ---- I2: hole-margin formula  F1 - T = 2 m^2 abar(2d)^2 - 4 m (abar(d)^2 - 1) + 2(m-1)(m-2)
print("== I2: vacancy-hole margin formula ==")
vac = [(GRID[i], 1) for i in range(1, 65)]
errs = []
for d in (0.05, 0.15, 0.3, 0.6, 1.0):
    for m in (1, 2, 3):
        lhs = F1(vac, [(0.0, d, m)]) - Tgt(vac, [(0.0, d, m)])
        rhs = 2 * m * m * abar(2 * d) ** 2 - 4 * m * (abar(d) ** 2 - 1) + 2 * (m - 1) * (m - 2)
        errs.append(abs(lhs - rhs))
print(f"   max |formula error| = {max(errs):.3e}")

# ---- I3: capacity-margin curve (single-pair, m=1 core)
#    dip sum  nu(y) = sum over local minima cells of [-R_y]_+  (one per cell, cell sup)
#    available = 2 abar(2y)^2 + 8 (abar(y)^2 - 1)   [pair diagonal + flattening self-term]
#    exposure cap (marks<=2, one atom per dip) = 8 nu(y)
print("== I3: capacity margin curve ==")
xs = np.linspace(0, N, 8001, endpoint=False)
print("   y      abar(2y)   nu(y)      8nu(y)   avail=2a2^2+8(a^2-1)   margin")
for y in (0.05, 0.1, 0.159, 0.2, 0.25, 0.318, 0.4, 0.5, 0.7, 1.0, 1.5):
    R = np.array([(psiN(x + 1j * y) ** 2).real for x in xs])
    # per-cell supremum of [-R]_+: cells = 65 arcs centered at grid sites
    cell = np.floor((xs / (N / 65.0)) + 0.5).astype(int) % 65
    nu = sum(max(0.0, float(np.max(-R[cell == k]))) for k in range(65))
    a2, a1 = abar(2 * y), abar(y)
    avail = 2 * a2 ** 2 + 8 * (a1 ** 2 - 1)
    print(f"   {y:5.3f}  {a2:9.4f}  {nu:9.5f}  {8*nu:8.4f}   {avail:12.4f}      {avail-8*nu:9.4f}")

# ---- I4: depth-resolved TRUE worst case: one pair at depth d (m=1), atoms free
#    minimize F1 - T over: vacancy background on/off, extra free atoms (marks 1/2)
print("== I4: depth-resolved single-pair worst case (free atoms) ==")
def worst_at_depth(d, n_free=6, restarts=12):
    best = np.inf
    for _ in range(restarts):
        marks = [int(rng.integers(1, 3)) for _ in range(n_free)]
        for base in ([], vac):
            def obj(x):
                atoms = list(base) + [(x[i] % N, marks[i]) for i in range(n_free)]
                prs = [(x[n_free] % N, d, 1)]
                return F1(atoms, prs) - Tgt(atoms, prs)
            x0 = np.concatenate([rng.uniform(0, N, n_free), [rng.uniform(0, N)]])
            r = minimize(obj, x0, method="Nelder-Mead",
                         options={"maxiter": 4000, "fatol": 1e-12})
            best = min(best, r.fun)
    return best
for d in (0.05, 0.1, 0.159, 0.25, 0.318, 0.5, 0.8):
    print(f"   d={d:5.3f}: min(F1-T) = {worst_at_depth(d):.5f}")
