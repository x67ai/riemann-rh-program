"""Gray-zone stress: k pairs at near-grid mutual separations sharing dip atoms;
half-gap deep twins; mixed depth classes; the sharp conjecture
   F1 >= sum_atoms (3m-2) + sum_pairs 4 m^2   ( = T + sum_p 2(2m^2-3m+2) )
is tested via margin2 := F1 - T - sum_p 2(2m^2-3m+2)."""
import numpy as np
from scipy.optimize import minimize
from pairchan_core import N, GRID, F1, S2, Tgt, abar, psiN

rng = np.random.default_rng(4242)

def sharp_slack(pairs):
    return sum(2 * (2 * m * m - 3 * m + 2) for (_, _, m) in pairs)

GLOB = [np.inf, None]
def rec(atoms, pairs, tag):
    g = F1(atoms, pairs) - Tgt(atoms, pairs) - sharp_slack(pairs)
    if g < GLOB[0]:
        GLOB[0], GLOB[1] = g, (tag, len(atoms), [(round(t,3),round(d,3),m) for t,d,m in pairs])
    return g

# ---- G1: k pairs on adjacent grid cells + mark-1/2 atoms at the joint dips ----
print("== G1: pair chains sharing dips ==")
xs = np.linspace(0, N, 8001, endpoint=False)
for d in (0.1, 0.2, 0.318, 0.5):
    for k in (2, 3, 4):
        for m in (1, 2):
            pairs = [(GRID[1 + 2*i], d, m) for i in range(k)]   # every other cell
            # dips of the SUM of the k pairs' R-functions
            Rsum = np.zeros(len(xs))
            for (tp, dp, mp) in pairs:
                Rsum += mp * np.array([(psiN(x - tp + 1j*dp) ** 2).real for x in xs])
            dipidx = [i for i in range(1, len(xs)-1)
                      if Rsum[i] < 0 and Rsum[i] <= Rsum[i-1] and Rsum[i] <= Rsum[i+1]]
            for ma in (1, 2):
                atoms = [(xs[i], ma) for i in dipidx]
                g = rec(atoms, pairs, f"G1 d={d} k={k} m={m} ma={ma}")
                print(f"   d={d} k={k} m={m} ma={ma} ndip={len(dipidx)}: margin2 = {g:.4f}")

# ---- G2: free optimization of pair chains + limited free atoms ----------------
print("== G2: free chains (positions+depths free, 8 free atoms) ==")
best = np.inf
for k in (2, 3):
    for m in (1, 2):
        for _ in range(14):
            nfree = 8
            am = [int(rng.integers(1, 3)) for _ in range(nfree)]
            def obj(x):
                atoms = [(x[i] % N, am[i]) for i in range(nfree)]
                prs = [(x[nfree + i] % N, min(np.exp(x[nfree + k + i]), 2.0), m)
                       for i in range(k)]
                return F1(atoms, prs) - Tgt(atoms, prs) - sharp_slack(prs)
            x0 = np.concatenate([rng.uniform(0, 8, nfree),
                                 rng.uniform(0, 6, k), np.log(rng.uniform(0.03, 1.0, k))])
            r = minimize(obj, x0, method="Nelder-Mead",
                         options={"maxiter": 6000, "fatol": 1e-12})
            best = min(best, r.fun)
            # record via rec for global bookkeeping
            xx = r.x
            atoms = [(xx[i] % N, am[i]) for i in range(nfree)]
            prs = [(xx[nfree + i] % N, min(np.exp(xx[nfree + k + i]), 2.0), m) for i in range(k)]
            rec(atoms, prs, f"G2 k={k} m={m}")
print(f"   min margin2 over G2 = {best:.5f}")

# ---- G3: half-gap deep twins + vacancy backgrounds ----------------------------
print("== G3: half-gap deep twins ==")
vac = [(GRID[i], 1) for i in range(1, 65)]
for d in (0.5, 0.8, 1.2, 1.8):
    for dx in (0.3, 0.492, 0.7):
        for base, nm in (([], "free"), (vac, "vac")):
            prs = [(0.0, d, 1), (dx, d, 1)]
            g = rec(base, prs, f"G3 d={d} dx={dx} {nm}")
            print(f"   d={d} dx={dx} base={nm}: margin2 = {g:.4f}")

# ---- G4: mixed depth classes, same position (anti-resonance) ------------------
print("== G4: two classes same position, depth-split scan ==")
for d1 in (0.1, 0.3, 0.6):
    for d2 in (d1 + 0.01, d1 + 0.05, d1 * 2):
        prs = [(0.0, d1, 1), (0.0, d2, 1)]
        g = rec([], prs, f"G4 {d1}/{d2}")
        print(f"   d1={d1} d2={d2}: margin2 = {g:.4f}")

# ---- G5: random deep mixed with high marks ------------------------------------
print("== G5: random stress (deep + high marks) ==")
best = np.inf
for _ in range(150):
    k = int(rng.integers(1, 5)); na = int(rng.integers(0, 6))
    atoms = [(float(rng.uniform(0, N)), int(rng.integers(1, 9))) for _ in range(na)]
    prs = [(float(rng.uniform(0, N)), float(rng.uniform(0.02, 2.0)),
            int(rng.integers(1, 5))) for _ in range(k)]
    if rng.random() < 0.4:
        atoms += [(GRID[i], 1) for i in range(1, 65, int(rng.integers(1, 3)))]
    g = rec(atoms, prs, "G5")
    best = min(best, g)
print(f"   min margin2 over 150 random = {best:.5f}")

print()
print(f"==== GLOBAL min of  F1 - T - sum_p 2(2m^2-3m+2)  = {GLOB[0]:.6f}")
print(f"     at {GLOB[1]}")
