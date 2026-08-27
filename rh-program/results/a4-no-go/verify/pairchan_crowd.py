"""Crowd+sea attack: many pairs at the ledger-binding depth + heavy dip-atom seas.
Tests the regime where my cell-cap chain leaks. Also mass-64 (LP-class) variants.
And: depth-resolved cap constants kappa_max(y), zone width, c0(y), Lambda-hat(y),
corrected S1corr(y) for the single-pair all-depth theorem."""
import numpy as np
from pairchan_core import N, GRID, F1, S2, Tgt, abar, psiN

Delta = N / 65.0
xs = np.linspace(0, N, 12001, endpoint=False)
cell_idx = np.floor((xs / Delta) + 0.5).astype(int) % 65

def sharp_slack(pairs):
    return sum(2 * (2 * m * m - 3 * m + 2) for (_, _, m) in pairs)

print("== crowd+sea attacks at d = 0.156 (ledger-binding depth) ==")
d = 0.156
res = []
for k in (8, 16, 32, 65):
    # k pairs spread one per every 65/k-th cell
    step = max(1, 65 // k)
    pairs = [(GRID[(i * step) % 65], d, 1) for i in range(k)]
    # joint field of all pairs' R_d couplings on atoms: R_d relative to each pair
    field = np.zeros(len(xs))
    for (tp, dp, mp) in pairs:
        field += mp * np.array([(psiN(x - tp + 1j * dp) ** 2).real for x in xs])
    # atoms: greedy at field minima, marks 2, various sea sizes
    order = np.argsort(field)
    for nsea in (16, 32, 64, 130):
        used, atoms = [], []
        for idx in order:
            if len(atoms) >= nsea:
                break
            x = xs[idx]
            if all(min(abs(x - u), N - abs(x - u)) > 0.35 for u in used):
                used.append(x); atoms.append((x, 2))
        f = F1(atoms, pairs); t = Tgt(atoms, pairs)
        g, g2 = f - t, f - t - sharp_slack(pairs)
        res.append(g)
        print(f"  k={k:3d} pairs, {len(atoms):3d} mark-2 atoms: F1-T = {g:9.4f}  "
              f"(sharp margin {g2:8.4f})  massM={sum(m for _,m in atoms)+2*k}")
print(f"  min F1-T over crowd attacks: {min(res):.4f}")

print()
print("== mass-64 LP-class versions (Sum m = 64) ==")
for k in (8, 12, 16):
    pairs = [(GRID[(i * (65 // k)) % 65], d, 1) for i in range(k)]
    field = np.zeros(len(xs))
    for (tp, dp, mp) in pairs:
        field += np.array([(psiN(x - tp + 1j * dp) ** 2).real for x in xs])
    order = np.argsort(field)
    nsea = (64 - 2 * k) // 2   # mark-2 atoms to fill mass
    used, atoms = [], []
    for idx in order:
        if len(atoms) >= nsea:
            break
        x = xs[idx]
        if all(min(abs(x - u), N - abs(x - u)) > 0.35 for u in used):
            used.append(x); atoms.append((x, 2))
    rem = 64 - 2 * k - 2 * len(atoms)
    if rem > 0:
        atoms += [(GRID[1] + 0.001 * i, 1) for i in range(rem)]
    f = F1(atoms, pairs); t = Tgt(atoms, pairs)
    print(f"  k={k} pairs + {len(atoms)} atoms (mass {sum(m for _,m in atoms)+2*k}): "
          f"F1-T = {f-t:9.4f}")

print()
print("== depth-resolved cap constants (single-pair corrected ledger) ==")
print("   y      kappa_max  zonewidth  c0=psi^2(zw)  Lhat   S1     S1corr")
worst_corr = 0.0
for y in (0.1, 0.159, 0.25, 0.318, 0.4, 0.5, 0.6, 0.7, 0.85, 1.0, 1.1):
    R = np.array([(psiN(x + 1j * y) ** 2).real for x in xs])
    kmax = 0.0; nu = 0.0; zw = 0.0
    for k in range(65):
        seg = -R[cell_idx == k]
        m = max(0.0, float(np.max(seg)))
        nu += m; kmax = max(kmax, m)
        # zone width in this cell
        xs_k = xs[cell_idx == k]; neg = xs_k[(seg > 0)]
        if len(neg) > 1:
            # circular-safe: cells are contiguous except wrap; take span
            span = neg.max() - neg.min()
            if span < 5:
                zw = max(zw, span)
    c0 = abs(psiN(min(zw, 0.9))) ** 2 if zw > 0 else 1.0
    # integer Lambda-hat: argmax of 4*L*kmax - c0*max(0,L*(L-2))
    vals = [(4 * L * kmax - c0 * max(0, L * (L - 2)), L) for L in range(1, 40)]
    best, Lhat = max(vals)
    S1 = 8 * nu / (2 * abar(2 * y) ** 2)
    S1c = (best / (8 * kmax) if kmax > 0 else 1) * S1 * (8 * kmax / (4 * 2 * kmax)) if kmax > 0 else S1
    # S1corr: per-cell worst is <= (best/(8*kappa_k))*8*kappa_k summed -> multiplier best/(8 kmax) is
    # only valid at the worst cell; uniform multiplier = max over cells of (percell_best/(8 kappa_k)).
    # Conservative: multiplier = best/(8*kmax) evaluated at kmax (largest kappa gives largest mult).
    mult = best / (8 * kmax) if kmax > 0 else 1.0
    S1c = S1 * max(1.0, mult)
    worst_corr = max(worst_corr, S1c)
    print(f"   {y:5.3f}  {kmax:9.4f}  {zw:8.3f}   {c0:9.4f}  {Lhat:4d}  {S1:6.4f}  {S1c:6.4f}")
print(f"   max corrected S1corr over grid = {worst_corr:.4f}")
