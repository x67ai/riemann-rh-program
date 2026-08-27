#!/usr/bin/env python3
"""
A4 M2 gate -- dictionary.py (SPEC 3.3): structured seed families 1-7.

Every column is an explicit N-periodic marked configuration of total mass N
(realizability by construction, SPEC 3.2). Seeds:
  1. 5/6-extremal: (N-2k) simples + k doubles; lattice / sine-sampled / jitter
  2. depth family: doubles -> pairs at grid depths (block-continuity probe)
  3. cluster motifs: mark patterns packed within one lambda'-window, tiled
  4. finite sprinkling (K2): n = ceil(eps N / m^2) atoms of mark m = W
  5. garnish surrogates: deep pairs w in {1.5, 2} (ladder-priced columns)
  6. null-like: CUE-sampled all-simple configurations (feasibility anchors)
  7. random marked perturbations (via column_gen neighborhood moves + here)
"""
import math

import numpy as np

from kernels import make_config
from null_budgets import cue_angles

DEPTH_GRID = (1 / 64, 1 / 8, 1 / 4, 1 / 2, 3 / 4, 1.0)
DEEP_GRID = (1.5, 2.0)


def lattice_positions(N, npts, phase=0.0):
    return (np.arange(npts) * (N / npts) + phase) % N


def seed_pure(N, geom, W):
    """Pure structures: mark-m lattices (N/m sites of mark m, F1 = mN + o(1),
    cross-terms dead), pair lattices at each depth, and two-sublattice mixes.
    These are the LP's budget-mixing anchors (e.g. the all-doubles lattice +
    all-simples lattice mixture is the exact lemmaR_tight extremal LAW)."""
    cols = []
    for m in (1, 2, 3, 4, 6, 8):
        if m > W or N % m:
            continue
        pos = lattice_positions(N, N // m)
        cols.append(make_config(N, atoms=[(x, m) for x in pos], tag=f"pure_m{m}"))
    # pair lattices (n_p pair positions, mult mp)
    for w in DEPTH_GRID + DEEP_GRID:
        d = geom.depth_from_w(w)
        for mp in (1, 2):
            if mp > max(1, W // 2) or N % (2 * mp):
                continue
            npts = N // (2 * mp)
            pos = lattice_positions(N, npts)
            cols.append(make_config(N, pairs=[(x, mp, d) for x in pos],
                                    tag=f"purep_m{mp}_w{w}"))
    # two-sublattice doubles+simples at coprime-ish counts
    for k in (8, 12, 16, 20, 24):
        nsim = N - 2 * k
        if nsim <= 0:
            continue
        a1 = [(x, 2) for x in lattice_positions(N, k, phase=0.0)]
        a2 = [(x, 1) for x in lattice_positions(N, nsim, phase=N / (2 * max(nsim, 1)))]
        cols.append(make_config(N, atoms=a1 + a2, tag=f"twolat_k{k}"))
    return cols


def seed_extremal(N, ks=(6, 8, 10, 11, 12, 14, 16), rng=None):
    """(N-2k) simples + k doubles, several position modes."""
    cols = []
    rng = rng or np.random.default_rng(0)
    for k in ks:
        nsite = N - k                      # distinct sites
        # lattice with doubles maximally spread among sites
        pos = lattice_positions(N, nsite)
        marks = np.ones(nsite, dtype=int)
        if k > 0:
            idx = np.round(np.linspace(0, nsite, k, endpoint=False)).astype(int) % nsite
            marks[idx] = 2
        cols.append(make_config(N, atoms=list(zip(pos, marks)), tag=f"ext_lat_k{k}"))
        # sine-sampled positions (CUE draw of nsite points, rescaled)
        th = cue_angles(nsite, rng) * (N / nsite)
        cols.append(make_config(N, atoms=list(zip(th, marks)), tag=f"ext_cue_k{k}"))
        # jittered lattice
        pos2 = (pos + rng.normal(0, 0.15, nsite)) % N
        cols.append(make_config(N, atoms=list(zip(pos2, marks)), tag=f"ext_jit_k{k}"))
    return cols


def seed_depth(N, geom, ks=(8, 10, 12), depths=DEPTH_GRID, rng=None):
    """Extremal with doubles -> pairs at each grid depth (same mass; Nd = N)."""
    cols = []
    for k in ks:
        nsim = N - 2 * k
        pos_s = lattice_positions(N, nsim + k)
        for w in depths:
            d = geom.depth_from_w(w)
            atoms = [(pos_s[i], 1) for i in range(nsim)]
            pairs = [(pos_s[nsim + i], 1, d) for i in range(k)]
            cols.append(make_config(N, atoms=atoms, pairs=pairs, tag=f"dep_k{k}_w{w:.3f}"))
        # mixed: half doubles, half pairs at w
        for w in (1 / 64, 1 / 2, 1.0):
            d = geom.depth_from_w(w)
            k2 = k // 2
            atoms = [(pos_s[i], 1) for i in range(nsim)] + \
                    [(pos_s[nsim + i], 2) for i in range(k - k2)]
            pairs = [(pos_s[nsim + k - k2 + i], 1, d) for i in range(k2)]
            cols.append(make_config(N, atoms=atoms, pairs=pairs,
                                    tag=f"mix_k{k}_w{w:.3f}"))
    return cols


def seed_cluster(N, W, rng=None):
    """Cluster motifs: 2-4 atoms with marks from the alphabet packed within one
    lambda'-window (width 2 mean gaps at lambda' = 1/2), tiled periodically at
    varying local density; mass balanced by evenly spread simples."""
    cols = []
    patterns = [(1, 1), (1, 1, 1), (1, 1, 1, 1), (2, 1), (2, 2), (2, 1, 1)]
    if W >= 3:
        patterns += [(3, 1), (3, 3), (2, 2, 1)]
    if W >= 4:
        patterns += [(4, 2), (4, 4), (3, 2, 1)]
    if W >= 6:
        patterns += [(6, 2), (6, 6)]
    if W >= 8:
        patterns += [(8, 4)]
    for pat in patterns:
        pmass = sum(pat)
        for spacing in (0.25, 0.5, 1.0):
            for ntile in (2, 4, 8, max(1, N // (2 * pmass))):
                used = ntile * pmass
                if used > N:
                    continue
                nsim = N - used
                atoms = []
                centers = lattice_positions(N, ntile)
                for c0 in centers:
                    for i, m in enumerate(pat):
                        atoms.append((c0 + i * spacing, m))
                if nsim > 0:
                    # interleave simples away from clusters
                    sp = lattice_positions(N, nsim, phase=0.5 * N / max(nsim, 1))
                    atoms += [(p, 1) for p in sp]
                cols.append(make_config(N, atoms=atoms,
                                        tag=f"clu_{pat}_s{spacing}_t{ntile}"))
    return cols


def seed_sprinkle(N, W, rng=None):
    """K2's finite sprinkling: n = ceil(eps N / m^2) atoms of mark m = W plus
    mass-balancing simples, eps in {1/4, 1/2, 1}."""
    cols = []
    if W < 2:
        return cols
    for eps in (0.25, 0.5, 1.0):
        n_spr = max(1, math.ceil(eps * N / W ** 2))
        used = n_spr * W
        if used > N:
            continue
        nsim = N - used
        spr = lattice_positions(N, n_spr)
        atoms = [(p, W) for p in spr]
        if nsim:
            atoms += [(p, 1) for p in lattice_positions(N, nsim, phase=0.37)]
        cols.append(make_config(N, atoms=atoms, tag=f"spr_W{W}_e{eps}"))
        # sprinkle on top of doubles background
        k = max(0, (N - used) // 6)
        nsim2 = N - used - 2 * k
        if nsim2 >= 0 and k > 0:
            sites = lattice_positions(N, nsim2 + k, phase=0.11)
            marks = np.ones(nsim2 + k, dtype=int)
            marks[np.round(np.linspace(0, len(marks), k, endpoint=False)).astype(int) % len(marks)] = 2
            atoms = [(p, W) for p in spr] + list(zip(sites, marks))
            cols.append(make_config(N, atoms=atoms, tag=f"sprd_W{W}_e{eps}_k{k}"))
    return cols


def seed_garnish(N, geom, rng=None):
    """Deep-pair insertions at w in {1.5, 2} on extremal/simple backgrounds."""
    cols = []
    for w in DEEP_GRID:
        d = geom.depth_from_w(w)
        for npr in (1, 2, 4):
            for k in (0, 8, 10):
                nsim = N - 2 * npr - 2 * k
                if nsim < 0:
                    continue
                sites = lattice_positions(N, nsim + k, phase=0.23)
                marks = np.ones(nsim + k, dtype=int)
                if k:
                    marks[np.round(np.linspace(0, len(marks), k, endpoint=False)).astype(int) % len(marks)] = 2
                pairs = [(p, 1, d) for p in lattice_positions(N, npr, phase=0.61)]
                cols.append(make_config(N, atoms=list(zip(sites, marks)), pairs=pairs,
                                        tag=f"gar_w{w}_p{npr}_k{k}"))
    return cols


def seed_null(N, count, rng):
    """CUE all-simple draws (feasibility anchors)."""
    cols = []
    for i in range(count):
        th = cue_angles(N, rng)
        cols.append(make_config(N, atoms=[(t, 1) for t in th], tag=f"null_{i}"))
    return cols


def seed_random(N, geom, W, count, rng):
    """Random marked configurations (seed family 7)."""
    cols = []
    for i in range(count):
        mass = N
        atoms, pairs = [], []
        # random number of doubles / higher marks / pairs
        k2 = rng.integers(0, N // 4)
        mass -= 2 * k2
        kk = []
        for m in range(3, W + 1):
            km = rng.integers(0, max(1, N // (3 * m)))
            km = min(km, mass // m)
            kk.append((m, km))
            mass -= m * km
        npr = rng.integers(0, 4)
        npr = min(npr, mass // 2)
        mass -= 2 * npr
        nsim = mass
        pos = rng.uniform(0, N, nsim + k2 + sum(km for _, km in kk) + npr)
        j = 0
        for _ in range(nsim):
            atoms.append((pos[j], 1)); j += 1
        for _ in range(k2):
            atoms.append((pos[j], 2)); j += 1
        for m, km in kk:
            for _ in range(km):
                atoms.append((pos[j], m)); j += 1
        for _ in range(npr):
            w = DEPTH_GRID[rng.integers(0, len(DEPTH_GRID))]
            pairs.append((pos[j], 1, geom.depth_from_w(w))); j += 1
        cols.append(make_config(N, atoms=atoms, pairs=pairs, tag=f"rnd_{i}"))
    return cols


def build_seed_dictionary(N, geom, W, rng=None, null_count=120, rand_count=60):
    rng = rng or np.random.default_rng(20260826)
    cols = []
    cols += seed_pure(N, geom, W)
    cols += seed_extremal(N, rng=rng)
    cols += seed_depth(N, geom, rng=rng)
    cols += seed_cluster(N, W, rng=rng)
    for Ws in range(2, W + 1):
        cols += seed_sprinkle(N, Ws, rng=rng)
    cols += seed_garnish(N, geom, rng=rng)
    cols += seed_null(N, null_count, rng)
    cols += seed_random(N, geom, W, rand_count, rng)
    # dedupe by key, enforce mass = N
    seen, out = set(), []
    for c in cols:
        if c.mass() != N:
            continue
        k = c.key()
        if k in seen:
            continue
        seen.add(k)
        out.append(c)
    return out


if __name__ == "__main__":
    from kernels import Geometry, rows_for
    N = 64
    geom = Geometry(N, 1.0, 0.5, ("flat",), ("flat",))
    cols = build_seed_dictionary(N, geom, W=8)
    print(f"{len(cols)} seed columns")
    import collections
    fams = collections.Counter(c.tag.split("_")[0] for c in cols)
    print(dict(fams))
    # spot check rows on a few
    for c in cols[:3] + cols[-2:]:
        r, ev = rows_for(c, geom)
        print(f"{c.tag:22s} mass={r.mass} Nd={r.Nd} F1={r.F1:8.2f} Fp={r.Fp:8.2f} "
              f"Cp={r.Cp:9.2f} nV={r.nV.tolist()} nneg={r.nneg} "
              f"consist={r.eig_consistency:.1e}")
