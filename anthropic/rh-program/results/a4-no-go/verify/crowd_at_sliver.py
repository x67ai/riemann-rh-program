"""Crowd+sea attacks AT THE LEDGER-FAILURE SLIVER d in (0.1577, 1/(2 pi)].
Session-7's pairchan_crowd.py attacked only d = 0.156 (its ledger-binding depth).
Session 8 found the ledger constant exceeds 1 on the sliver, so the attacks must
be re-run there: same protocol (k pairs one per cell tranche + greedy mark-2 seas
at the joint-field minima), at d = 0.158 and 0.159.  Float grade, independent
assembly (same formulas as pairchan_core)."""
import numpy as np

N = 64
JJ = np.arange(-32, 33)
S = np.arange(-64, 65)
W = (65 - np.abs(S)) / 65.0 ** 2
Delta = N / 65.0
GRID = np.arange(65) * Delta
xs = np.linspace(0, N, 12001, endpoint=False)


def psi_arr(z_arr):
    return np.exp(-2j * np.pi * np.outer(z_arr, JJ) / N) @ (np.ones(65) / 65)


def F1(atoms, pairs):
    c = np.zeros(len(S), dtype=complex)
    for (th, m) in atoms:
        c += m * np.exp(-2j * np.pi * S * th / N)
    for (th, d, m) in pairs:
        c += 2.0 * m * np.cosh(2.0 * np.pi * S * d / N) * np.exp(-2j * np.pi * S * th / N)
    return float(np.sum(W * np.abs(c) ** 2))


def Tgt(atoms, pairs):
    return sum(3 * m - 2 for _, m in atoms) + sum(6 * m - 4 for _, _, m in pairs)


for d in (0.158, 0.159):
    print(f"== crowd+sea at d = {d} ==")
    res = []
    for k in (8, 16, 32, 65):
        step = max(1, 65 // k)
        pairs = [(GRID[(i * step) % 65], d, 1) for i in range(k)]
        field = np.zeros(len(xs))
        for (tp, dp, mp) in pairs:
            psi = np.exp(-2j * np.pi * np.outer(xs - tp, JJ) / N) @ \
                (np.exp(2 * np.pi * JJ * dp / N) / 65)
            field += mp * (psi ** 2).real
        order = np.argsort(field)
        for nsea in (16, 32, 64, 130):
            used, atoms = [], []
            for idx in order:
                if len(atoms) >= nsea:
                    break
                x = xs[idx]
                if all(min(abs(x - u), N - abs(x - u)) > 0.35 for u in used):
                    used.append(x)
                    atoms.append((x, 2))
            g = F1(atoms, pairs) - Tgt(atoms, pairs)
            res.append(g)
            print(f"  k={k:3d} pairs, {len(atoms):3d} mark-2 atoms: F1-T = {g:9.4f}")
    print(f"  min F1-T at d = {d}: {min(res):.4f}")
