"""Pair-interference channel: independent core assembly (NOT the gate's code).

Model (SPEC.md Sec 1.4, re-implemented from scratch):
  N = 64, lambda = 1, flat window: harmonics u_j = 1/65, |j| <= 32.
  c_s = sum_atoms m e^{-2 pi i s theta/64} + sum_pairs 2 m cosh(2 pi s d/64) e^{-2 pi i s theta/64}
  F1  = sum_{|s|<=64} w_s |c_s|^2,   w_s = (65 - |s|)/65^2.
Targets:
  S2 = sum_atoms m^2 + 2 sum_pairs m^2          (mark accounting, per zero m^2)
  T  = sum_atoms (3m-2) + sum_pairs (6m-4)      (what the 5/6 corner needs: F1 >= 3M - 2 N_d)
"""
import numpy as np

N = 64
J = 32
S = np.arange(-2 * J, 2 * J + 1)            # s = -64..64
W = (65 - np.abs(S)) / 65.0**2              # w_s
JJ = np.arange(-J, J + 1)                   # j = -32..32
U = np.full(65, 1.0 / 65.0)                 # u_j

def abar(x):
    """abar(x) = sum_j u_j cosh(2 pi j x / 64). Pair-block A at 'depth argument' x."""
    return float(np.sum(U * np.cosh(2.0 * np.pi * JJ * x / N)))

def assemble_c(atoms, pairs):
    """atoms: list of (theta, m); pairs: list of (theta, d, m). Returns c_s complex array."""
    c = np.zeros(len(S), dtype=complex)
    for (th, m) in atoms:
        c += m * np.exp(-2j * np.pi * S * th / N)
    for (th, d, m) in pairs:
        c += 2.0 * m * np.cosh(2.0 * np.pi * S * d / N) * np.exp(-2j * np.pi * S * th / N)
    return c

def F1(atoms, pairs):
    c = assemble_c(atoms, pairs)
    return float(np.sum(W * np.abs(c) ** 2))

def S2(atoms, pairs):
    return sum(m * m for (_, m) in atoms) + 2 * sum(m * m for (_, _, m) in pairs)

def Tgt(atoms, pairs):
    return sum(3 * m - 2 for (_, m) in atoms) + sum(6 * m - 4 for (_, _, m) in pairs)

def psiN(z):
    """psi_N at complex argument z: sum_j u_j e^{-2 pi i j z/64}."""
    return complex(np.sum(U * np.exp(-2j * np.pi * JJ * z / N)))

GRID = np.arange(65) * (N / 65.0)           # the 65-site psi_1-zero grid

if __name__ == "__main__":
    rng = np.random.default_rng(20260826)
    print("== verification suite ==")
    # V1: grid Parseval, random subsets/marks
    errs = []
    for _ in range(40):
        k = rng.integers(5, 66)
        sites = rng.choice(65, size=k, replace=False)
        marks = rng.integers(1, 9, size=k)
        atoms = [(GRID[i], int(m)) for i, m in zip(sites, marks)]
        errs.append(abs(F1(atoms, []) - S2(atoms, [])))
    print(f"V1 grid Parseval: max |F1 - sum m^2| = {max(errs):.3e}")
    # V2: single-pair block law  F1 = 2 m^2 (1 + abar(2d)^2)
    errs = []
    for _ in range(20):
        th = rng.uniform(0, N); d = rng.uniform(0.01, 1.0); m = int(rng.integers(1, 5))
        got = F1([], [(th, d, m)])
        want = 2 * m * m * (1 + abar(2 * d) ** 2)
        errs.append(abs(got - want))
    print(f"V2 pair block law: max err = {max(errs):.3e}")
    # V3: witness columns (RUN-REPORT Sec 5): F1 = 64 (vacancy lattice), 96, 128
    vac = [(GRID[i], 1) for i in range(1, 65)]
    print(f"V3 vacancy lattice F1 = {F1(vac, []):.12f} (want 64)")
    col3 = [(GRID[i], 2) for i in range(32)]
    print(f"V3 32-doubles-grid F1 = {F1(col3, []):.12f} (want 128)")
    # V4: translate-sum identities
    for d in (0.1, 0.3, 0.7):
        x = rng.uniform(0, 1)
        s1 = sum((psiN(x + g + 1j * d) ** 2).real for g in GRID)
        s2v = sum(abs(psiN(x + g + 1j * d)) ** 2 for g in GRID)
        print(f"V4 d={d}: sum_k Re psi^2 = {s1:.12f} (want 1);  sum_k |psi|^2 = {s2v:.9f} "
              f"(want abar(2d) = {abar(2*d):.9f})")
    # V5: C-S chain abar(d)^2 <= (1 + abar(2d))/2
    ds = np.linspace(0.01, 2.5, 60)
    worst = max(abar(d) ** 2 - (1 + abar(2 * d)) / 2 for d in ds)
    print(f"V5 C-S chain max violation (should be <= 0): {worst:.3e}")
    # V6: fractional-mark counterexample (F1 < S2 with real mark mu)
    d, mu = 0.25, 0.05
    hole_pair = [(GRID[0], d, mu)]
    f = F1(vac, hole_pair); s = S2(vac, hole_pair)
    pred = 2 * mu**2 * abar(2*d)**2 - 4 * mu * (abar(d)**2 - 1)
    print(f"V6 fractional attack: F1-S2 = {f-s:.6e} (predicted {pred:.6e}) -> "
          f"{'VIOLATION (as designed)' if f < s else 'no violation'}")
