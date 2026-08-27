"""Adversarial search: minimize F1 - T (and F1 - S2) over integer-mark configurations
with pairs. Continuous positions/depths optimized; marks enumerated.
Families:
  A. vacancy lattice (64 grid atoms) + 1 pair, position+depth free, m_p in 1..4
  B. v-vacancy lattices + k pairs at/near holes, positions+depths free
  C. dip attack: 1 pair + atoms (marks 1 or 2) seeded at the dips of R(x)=Re psi^2(x+id),
     positions then locally optimized
  D. pair crowds: k pairs alone (no atoms), positions+depths free (frustration probe)
  E. random mixed configs, positions+depths+the pair/atom split random, local opt
  F. two-depth-class anti-phased probe (half-circle offset)
All with scipy Nelder-Mead / Powell local optimization, multi-start.
Records the global minimum of F1 - T and F1 - S2 found, and the argmin config.
"""
import numpy as np
from scipy.optimize import minimize
from pairchan_core import N, GRID, F1, S2, Tgt, abar, psiN

rng = np.random.default_rng(777)

BEST = {"T": (np.inf, None), "S2": (np.inf, None)}

def record(atoms, pairs, tag):
    f = F1(atoms, pairs)
    gT = f - Tgt(atoms, pairs)
    gS = f - S2(atoms, pairs)
    if gT < BEST["T"][0]:
        BEST["T"] = (gT, (tag, [(round(t,4),m) for t,m in atoms],
                          [(round(t,4),round(d,4),m) for t,d,m in pairs]))
    if gS < BEST["S2"][0]:
        BEST["S2"] = (gS, (tag, [(round(t,4),m) for t,m in atoms],
                           [(round(t,4),round(d,4),m) for t,d,m in pairs]))
    return gT, gS

def opt_positions_depths(atoms_fixed, atom_free_marks, pair_marks, x0, tag,
                         dmax=2.5, iters=2000):
    """x = [atom positions..., pair positions..., pair log-depths...]"""
    na, npr = len(atom_free_marks), len(pair_marks)
    def build(x):
        atoms = list(atoms_fixed) + [(x[i] % N, atom_free_marks[i]) for i in range(na)]
        prs = [(x[na + i] % N, min(np.exp(x[na + npr + i]), dmax), pair_marks[i])
               for i in range(npr)]
        return atoms, prs
    def obj(x):
        a, p = build(x)
        return F1(a, p) - Tgt(a, p)
    res = minimize(obj, x0, method="Nelder-Mead",
                   options={"maxiter": iters, "xatol": 1e-8, "fatol": 1e-12})
    a, p = build(res.x)
    return record(a, p, tag), res.fun

# ---- A. vacancy lattice + 1 pair ----------------------------------------------
vac = [(GRID[i], 1) for i in range(1, 65)]
print("== A: vacancy lattice + 1 pair ==")
for m in (1, 2, 3, 4):
    best = np.inf
    for _ in range(24):
        x0 = np.array([rng.uniform(-0.6, 0.6), np.log(rng.uniform(0.02, 1.8))])
        (gT, gS), _ = opt_positions_depths(vac, [], [m],
                        np.array([0.0, x0[0], x0[1]])[1:], f"A m={m}")
        best = min(best, gT)
    print(f"  m={m}: min(F1-T) = {best:.6f}")

# ---- B. v-vacancy lattices + k pairs ------------------------------------------
print("== B: multi-vacancy lattices + k pairs ==")
for k in (1, 2, 3):
    for m in (1, 2):
        v = 2 * k * m - 1 if 2 * k * m - 1 > 0 else 1   # mass balance-ish (not required)
        # holes at sites 0..v-1 (clustered) and spread variant
        for holes in (list(range(v + 1)), list(range(0, 65, max(1, 64 // (v + 1))))[:v + 1]):
            atoms_fixed = [(GRID[i], 1) for i in range(65) if i not in holes]
            best = np.inf
            for _ in range(16):
                x0 = []
                for i in range(k):
                    x0.append(GRID[holes[i % len(holes)]] + rng.uniform(-0.4, 0.4))
                for i in range(k):
                    x0.append(np.log(rng.uniform(0.02, 1.5)))
                (gT, gS), _ = opt_positions_depths(atoms_fixed, [], [m] * k,
                                np.array(x0), f"B k={k} m={m} v={v}")
                best = min(best, gT)
            print(f"  k={k} m={m} v={v} holes={'clust' if holes[1]==1 else 'spread'}: "
                  f"min(F1-T) = {best:.6f}")

# ---- C. dip attack -------------------------------------------------------------
print("== C: dip attack (pair + atoms at dips of R) ==")
xs = np.linspace(0, N, 4001, endpoint=False)
for d in (0.1, 0.2, 0.3, 0.5, 0.8, 1.2):
    R = np.array([ (psiN(x + 1j * d) ** 2).real for x in xs ])
    # local minima with R<0
    dips = [xs[i] for i in range(1, len(xs) - 1)
            if R[i] < 0 and R[i] <= R[i-1] and R[i] <= R[i+1]]
    for m in (1, 2):
        for ma in (1, 2):
            atoms = [(x, ma) for x in dips]
            pairs = [(0.0, d, m)]
            gT, gS = record(atoms, pairs, f"C d={d} m={m} ma={ma} ndip={len(dips)}")
            # then locally optimize atom positions too (subset: keep it light for many dips)
            print(f"  d={d} m={m} ma={ma} ndips={len(dips)}: F1-T={gT:.4f} F1-S2={gS:.4f}")

# ---- D. pair crowds ------------------------------------------------------------
print("== D: pair crowds (no atoms) ==")
for k in (2, 3, 4, 6):
    for m in (1, 2):
        best = np.inf
        for _ in range(20):
            x0 = list(rng.uniform(0, N, size=k)) + list(np.log(rng.uniform(0.05, 2.0, size=k)))
            (gT, gS), _ = opt_positions_depths([], [], [m] * k, np.array(x0), f"D k={k} m={m}")
            best = min(best, gT)
        print(f"  k={k} m={m}: min(F1-T) = {best:.6f}")

# ---- E. random mixed + local opt ----------------------------------------------
print("== E: random mixed configs ==")
best = np.inf
for trial in range(60):
    na = int(rng.integers(0, 7)); k = int(rng.integers(1, 4))
    am = [int(rng.integers(1, 4)) for _ in range(na)]
    pm = [int(rng.integers(1, 3)) for _ in range(k)]
    base = [] if rng.random() < 0.5 else [(GRID[i], 1) for i in range(1, 65, int(rng.integers(1, 4)))]
    x0 = list(rng.uniform(0, N, size=na + k)) + list(np.log(rng.uniform(0.03, 2.0, size=k)))
    (gT, gS), _ = opt_positions_depths(base, am, pm, np.array(x0), f"E trial={trial}")
    best = min(best, gT)
print(f"  min(F1-T) over 60 trials = {best:.6f}")

# ---- F. anti-phased two-class probe -------------------------------------------
print("== F: anti-phased two-depth-class probe ==")
best = np.inf
for m in (1, 2):
    for _ in range(20):
        x0 = [rng.uniform(-1, 1), 32.0 + rng.uniform(-1, 1),
              np.log(rng.uniform(0.05, 2.0)), np.log(rng.uniform(0.05, 2.0))]
        (gT, gS), _ = opt_positions_depths([], [], [m, m], np.array(x0), f"F m={m}")
        best = min(best, gT)
print(f"  min(F1-T) = {best:.6f}")

print()
print("==== GLOBAL MINIMA FOUND ====")
print(f"min F1 - T  = {BEST['T'][0]:.8f}   at {BEST['T'][1]}")
print(f"min F1 - S2 = {BEST['S2'][0]:.8f}   at {BEST['S2'][1]}")
