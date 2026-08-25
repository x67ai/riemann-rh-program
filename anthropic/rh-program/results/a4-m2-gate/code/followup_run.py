#!/usr/bin/env python3
"""
A4 M2 gate -- followup_run.py: auditor-mandated follow-ups (AUDIT.md findings
2 and 3), run after the gate decided ABSORPTION.

Task 1 (AUDIT major-2): promote the Tier-2 near-CUE-pinned system to decision
grade -- column generation to the SPEC 3.3 stop rule (S = 200 fruitless
restarts, rc < -1e-6) at N = 64 for tau2 in {1, 4} x eps in {0.05, 0.02}, and
at N = 128 for the primary cell (tau2 = 1, eps = 0.05); explicit near-CUE
witness law extracted and rationally re-verified (including the pinning rows).

Task 2 (AUDIT major-3): the p1-objective rerun (the old N4 question) -- same
dictionary and rows, objective = simple-point fraction (atoms of mark 1 count
1, pairs of multiplicity 1 count 2; higher marks/mults count 0), with and
without the cubic block, at the primary configuration and the tightest-eps
asymptotic variant, to the same stop rule.

REUSES the gate's own modules (kernels, master_lp, column_gen, dictionary,
run_gate); the only new code is (i) the objective plumbing (mode 'nd' | 'p1')
threaded through an objective-aware copy of the pricing worker, and (ii) the
convergence driver that applies the SPEC stop rule literally. mode='nd'
reproduces column_gen's scoring exactly (same formulas, same moves).

Dictionaries are extended into NEW files (dict_N{64,128}_fu.json) so the
audited gate snapshots stay untouched. Thermal: Pool(2), phases sequential.
"""
import json
import math
import os
import sys
import time
from fractions import Fraction as Fr

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kernels import Geometry, Config, Rows, make_config, rows_for, c_coeffs
from master_lp import GateParams, solve_master, rational_verify, filter_W
from column_gen import (dual_coeffs, RC_TOL, local_opt, to_cfg, cfg_to_skel,
                        random_skeleton, cfg_blob, _get_geom)
from dictionary import DEPTH_GRID
from run_gate import load_dict, save_dict, budgets_for, RUNS

VGRID = (2, 3, 4, 6, 8, 12, 16)
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


# ---------------------------------------------------------------- objectives
def nsimple(cfg):
    """Simple-point count: mark-1 atoms (1 zero each) + multiplicity-1 pairs
    (2 simple zeros each). Marks/mults >= 2 contribute 0."""
    ns = 0
    if len(cfg.atom_mrk):
        ns += int(np.sum(cfg.atom_mrk == 1))
    if len(cfg.pair_mrk):
        ns += 2 * int(np.sum(cfg.pair_mrk == 1))
    return ns


def obj_count(cfg, mode):
    return cfg.n_distinct() if mode == "nd" else nsimple(cfg)


def with_obj(cols_rows, mode):
    """Master-LP view of the dictionary under the chosen objective: Rows.Nd is
    the objective count (solve_master's objective is r.Nd / N). mode='nd' is
    the identity."""
    if mode == "nd":
        return cols_rows
    out = []
    for cfg, r in cols_rows:
        out.append((cfg, Rows(r.F1, r.Fp, r.Cp, r.nV, r.nneg,
                              obj_count(cfg, mode), r.mass,
                              r.eig_consistency, r.S1)))
    return out


# ------------------------------------------------- objective-aware pricing
# rc_exact / discrete_moves / _restart_task from column_gen with the single
# change objective_count(cfg, mode) in place of r.Nd (mode='nd' identical).
def rc_exact_obj(cfg, geom, w, p, mode):
    r, _ = rows_for(cfg, geom)
    rc = obj_count(cfg, mode) / p.N - w["y0"] - w["wF1"] * r.F1 \
        - w["wFp"] * r.Fp - w["wCp"] * r.Cp
    for i, V in enumerate(p.Vgrid):
        L = w["yV"].get(V, 0.0)
        if L:
            rc -= L * float(r.nV[i])
    if w["wT2"]:
        c = c_coeffs(cfg, geom.smax)
        for j, wt in w["wT2"].items():
            rc -= wt * float(np.abs(c[j]) ** 2)
    return rc, r


def discrete_moves_obj(cfg, geom, w, p, rng, mode, tries=24):
    best_rc, _ = rc_exact_obj(cfg, geom, w, p, mode)
    best = None
    Wcap = p.Wcap
    pm_cap = max(1, Wcap // 2)
    N = geom.N
    for _ in range(tries):
        a_pos = list(cfg.atom_pos); a_m = list(cfg.atom_mrk)
        p_pos = list(cfg.pair_pos); p_m = list(cfg.pair_mrk)
        p_d = list(cfg.pair_d)
        kind = rng.integers(0, 6)
        try:
            if kind == 0 and len(a_pos) >= 2:      # merge two atoms
                i, j = rng.choice(len(a_pos), 2, replace=False)
                if a_m[i] + a_m[j] <= Wcap:
                    a_m[i] += a_m[j]
                    del a_pos[j], a_m[j]
                else:
                    continue
            elif kind == 1 and a_pos:              # split an atom
                i = rng.integers(0, len(a_pos))
                if a_m[i] >= 2:
                    m1 = rng.integers(1, a_m[i])
                    a_pos.append(a_pos[i] + rng.uniform(0.15, 0.6))
                    a_m.append(a_m[i] - m1)
                    a_m[i] = m1
                else:
                    continue
            elif kind == 2 and a_pos:              # double -> pair
                cand = [i for i in range(len(a_pos)) if a_m[i] % 2 == 0
                        and a_m[i] // 2 <= pm_cap]
                if not cand:
                    continue
                i = cand[rng.integers(0, len(cand))]
                wd = DEPTH_GRID[rng.integers(0, len(DEPTH_GRID))]
                p_pos.append(a_pos[i]); p_m.append(a_m[i] // 2)
                p_d.append(geom.depth_from_w(wd))
                del a_pos[i], a_m[i]
            elif kind == 3 and p_pos:              # pair -> atom (double)
                i = rng.integers(0, len(p_pos))
                if 2 * p_m[i] <= Wcap:
                    a_pos.append(p_pos[i]); a_m.append(2 * p_m[i])
                    del p_pos[i], p_m[i], p_d[i]
                else:
                    continue
            elif kind == 4 and p_pos:              # pair depth move
                i = rng.integers(0, len(p_pos))
                wd = DEPTH_GRID[rng.integers(0, len(DEPTH_GRID))]
                p_d[i] = geom.depth_from_w(wd)
            elif kind == 5 and len(a_pos) >= 2:    # mark transfer
                i, j = rng.choice(len(a_pos), 2, replace=False)
                if a_m[i] >= 2 and a_m[j] + 1 <= Wcap:
                    a_m[i] -= 1; a_m[j] += 1
                    if a_m[i] == 0:
                        del a_pos[i], a_m[i]
                else:
                    continue
            else:
                continue
        except ValueError:
            continue
        cand = make_config(N, atoms=list(zip(a_pos, a_m)),
                           pairs=list(zip(p_pos, p_m, p_d)), tag="fu")
        if cand.mass() != N:
            continue
        rc, _ = rc_exact_obj(cand, geom, w, p, mode)
        if rc < best_rc - 1e-9:
            best_rc, best = rc, cand
    return best_rc, best


def _restart_task_obj(args):
    seed, desc, w, p, support_blobs, mode = args
    geom = _get_geom(desc)
    support = [Config(geom.N, np.array(b[0]), np.array(b[1], dtype=int),
                      np.array(b[2]), np.array(b[3], dtype=int),
                      np.array(b[4])) for b in support_blobs]
    rng = np.random.default_rng(seed)
    skel, theta0 = random_skeleton(geom.N, p.Wcap, geom, rng, support or None)
    try:
        theta = local_opt(skel, theta0, geom, w)
    except Exception:
        return None
    cfg = to_cfg(skel, theta, geom.N, tag="fu")
    rc, _ = rc_exact_obj(cfg, geom, w, p, mode)
    best_rc, best_cfg = rc, cfg
    for _ in range(3):
        rc2, cand = discrete_moves_obj(best_cfg, geom, w, p, rng, mode)
        if cand is None:
            break
        skel2, th2 = cfg_to_skel(cand)
        try:
            th2 = local_opt(skel2, th2, geom, w, maxiter=60)
        except Exception:
            pass
        cand2 = to_cfg(skel2, th2, geom.N, tag="fu")
        rc3, _ = rc_exact_obj(cand2, geom, w, p, mode)
        if min(rc2, rc3) < best_rc - 1e-9:
            best_rc = min(rc2, rc3)
            best_cfg = cand2 if rc3 <= rc2 else cand
        else:
            break
    return best_rc, cfg_blob(best_cfg)


def price_obj(geom, w, p, support_cfgs, S, pool, mode, seed0=0):
    desc = (geom.N, geom.lam1, geom.lamp, geom.win1, geom.winp)
    blobs = [cfg_blob(c) for c in (support_cfgs or [])]
    tasks = [(int(seed0 + i), desc, w, p, blobs, mode) for i in range(S)]
    results = pool.map(_restart_task_obj, tasks)
    found = []
    for r in results:
        if r is None:
            continue
        rc, tup = r
        if rc < RC_TOL:
            cfg = Config(geom.N, np.array(tup[0]), np.array(tup[1], dtype=int),
                         np.array(tup[2]), np.array(tup[3], dtype=int),
                         np.array(tup[4]), tag=f"fu_rc{rc:.5f}")
            found.append((rc, cfg))
    found.sort(key=lambda t: t[0])
    return found


# ---------------------------------------------------------------- convergence
def add_found(cols_rows, known, found, geom, cap=30):
    newc = 0
    for rc, cfg in found[:cap]:
        if cfg.key() in known or cfg.mass() != geom.N:
            continue
        r, _ = rows_for(cfg, geom, tier2=True)
        if r.eig_consistency > 1e-8 or r.nneg > cfg.npairs():
            continue
        cols_rows.append((cfg, r))
        known.add(cfg.key())
        newc += 1
    return newc


def solve_targets(cols_rows, p, mode):
    cr_true = filter_W(cols_rows, p.Wcap)
    cr = with_obj(cr_true, mode)
    full = solve_master(cr, p, include_cubic=True, include_Fp=True)
    base = solve_master(cr, p, include_cubic=False, include_Fp=True)
    cal = solve_master(cr, p, include_cubic=False, include_Fp=False)
    return cr_true, full, base, cal


def converge_cell(cols_rows, geom, p, pool, mode, S_round, S_stop, max_rounds,
                  max_outer, seed0, label):
    """Alternate master/pricing until the SPEC 3.3 stop rule holds for BOTH
    the full and base systems: S_stop restarts produce no column with reduced
    cost < -1e-6. Returns final record + convergence status."""
    known = {cfg.key() for cfg, _ in cols_rows}
    t0 = time.time()
    hist = []
    ver = None
    for outer in range(max_outer):
        for rnd in range(max_rounds):
            new_any = 0
            for tgt in ("full", "base"):
                cr_true = filter_W(cols_rows, p.Wcap)
                cr = with_obj(cr_true, mode)
                sol = solve_master(cr, p, include_cubic=(tgt == "full"),
                                   include_Fp=True)
                if sol["status"] != 0:
                    hist.append((outer, rnd, tgt, "infeasible", None, 0))
                    continue
                w = dual_coeffs(sol, p)
                support = [cfg for i, (cfg, _) in enumerate(cr_true)
                           if sol["x"][i] > 1e-6]
                found = price_obj(geom, w, p, support, S_round, pool, mode,
                                  seed0=seed0 + 977 * (10000 * outer + 100 * rnd)
                                  + (0 if tgt == "full" else 50021))
                nc = add_found(cols_rows, known, found, geom)
                hist.append((outer, rnd, tgt, sol["P"],
                             found[0][0] if found else 0.0, nc))
                new_any += nc
            if not new_any:
                break
        # SPEC stop-rule verification pass
        clean = True
        ver = {}
        for tgt in ("full", "base"):
            cr_true = filter_W(cols_rows, p.Wcap)
            cr = with_obj(cr_true, mode)
            sol = solve_master(cr, p, include_cubic=(tgt == "full"),
                               include_Fp=True)
            if sol["status"] != 0:
                ver[tgt] = dict(status="infeasible")
                clean = False
                continue
            w = dual_coeffs(sol, p)
            support = [cfg for i, (cfg, _) in enumerate(cr_true)
                       if sol["x"][i] > 1e-6]
            found = price_obj(geom, w, p, support, S_stop, pool, mode,
                              seed0=seed0 + 777000 + 1000 * outer
                              + (0 if tgt == "full" else 1))
            ver[tgt] = dict(P=sol["P"], min_rc=found[0][0] if found else 0.0,
                            n_improving=len(found), S=S_stop)
            if found:
                add_found(cols_rows, known, found, geom)
                clean = False
        log(f"[{label}] outer {outer}: "
            + " ".join(f"{t}: P={v.get('P'):.7f} min_rc={v.get('min_rc'):+.2e} "
                       f"n_imp={v.get('n_improving')}"
                       for t, v in ver.items() if v.get('P') is not None)
            + f" cols={len(cols_rows)} [{time.time()-t0:.0f}s]")
        if clean:
            return dict(converged=True, outer_used=outer + 1, verify=ver,
                        secs=round(time.time() - t0, 1), history=hist)
    return dict(converged=False, outer_used=max_outer, verify=ver,
                secs=round(time.time() - t0, 1), history=hist)


# ---------------------------------------------------------------- reporting
def cell_record(cols_rows, p, mode):
    """Final P_full / P_base / P_cal / delta and active rows at a cell."""
    cr_true, full, base, cal = solve_targets(cols_rows, p, mode)
    rec = dict(
        n_cols=len(cr_true),
        P_full=full.get("P"), P_base=base.get("P"), P_cal=cal.get("P"),
        status=(full["status"], base["status"], cal["status"]),
        delta_0=(full["P"] - base["P"]) if (full.get("P") is not None
                                            and base.get("P") is not None)
        else None,
        active_full={k: round(v, 8) for k, v in
                     (full.get("active_rows") or {}).items()},
    )
    return rec, full, base, cal


def rational_verify_t2(cols_rows_view, p, sol):
    """master_lp.rational_verify plus the Tier-2 pinning rows in Fraction
    arithmetic on 1e-12 rationalizations (same documented deviation as the
    main gate: kernel data are transcendental)."""
    rep = rational_verify(cols_rows_view, p, sol)
    if p.tier2_tau is None:
        return rep
    n = len(cols_rows_view)
    x = sol["x"]
    sup = [i for i in range(n) if x[i] > 1e-9]
    q = 10 ** 12

    def fr(v):
        return Fr(int(round(v * q)), q)

    ws = [fr(x[i]) for i in sup]
    t2_ok = True
    worst = None
    for j in range(1, p.N):
        Ej = sum(w * fr(float(cols_rows_view[i][1].S1[j - 1]))
                 for w, i in zip(ws, sup))
        lo, hi = Fr(j) - fr(p.tier2_tau), Fr(j) + fr(p.tier2_tau)
        ok = (lo - Fr(1, 10 ** 6) <= Ej <= hi + Fr(1, 10 ** 6))
        t2_ok = t2_ok and ok
        margin = min(float(Ej - lo), float(hi - Ej))
        if worst is None or margin < worst[1]:
            worst = (j, margin)
    rep["checks"]["tier2_all_j"] = bool(t2_ok)
    rep["tier2_worst_margin"] = dict(j=worst[0], margin=worst[1])
    rep["all_ok"] = rep["all_ok"] and bool(t2_ok)
    return rep


def witness_from(cols_rows, p, mode, sol, cr_true):
    """Explicit law (weights + configurations + row data) from a solve."""
    x = sol["x"]
    sup = [i for i in range(len(cr_true)) if x[i] > 1e-9]
    law = []
    for i in sup:
        cfg, r = cr_true[i]
        law.append(dict(
            weight=float(x[i]), tag=cfg.tag,
            Nd=int(r.Nd), n_simple=int(nsimple(cfg)),
            F1=float(r.F1), Fp=float(r.Fp), Cp=float(r.Cp),
            nV=[int(v) for v in r.nV], nneg=int(r.nneg),
            atoms=[[float(a), int(m)] for a, m in
                   zip(cfg.atom_pos, cfg.atom_mrk)],
            pairs=[[float(a), int(m), float(d)] for a, m, d in
                   zip(cfg.pair_pos, cfg.pair_mrk, cfg.pair_d)],
            S1=[float(v) for v in r.S1] if r.S1 is not None else None,
        ))
    E = dict(
        F1=float(sum(x[i] * cr_true[i][1].F1 for i in sup)),
        Fp=float(sum(x[i] * cr_true[i][1].Fp for i in sup)),
        Cp=float(sum(x[i] * cr_true[i][1].Cp for i in sup)),
        Nd=float(sum(x[i] * cr_true[i][1].Nd for i in sup)),
        n_simple=float(sum(x[i] * nsimple(cr_true[i][0]) for i in sup)),
    )
    if all(cr_true[i][1].S1 is not None for i in sup):
        ES1 = np.zeros(p.N - 1)
        for i in sup:
            ES1 += x[i] * cr_true[i][1].S1
        E["S1"] = [float(v) for v in ES1]
    return law, E


# ---------------------------------------------------------------- phases
def phase_t2(N, cells, dict_in, dict_out, out_name, S_round, S_stop,
             max_rounds, max_outer, do_witness_cell=None):
    import multiprocessing as mp
    pool = mp.get_context("spawn").Pool(2)     # thermal: <= 2 concurrent heavy
    t0 = time.time()
    geom = Geometry(N, 1.0, 0.5, ("flat",), ("flat",))
    cols_rows = load_dict(os.path.join(RUNS, dict_in), N)
    log(f"tier2 N={N}: loaded {len(cols_rows)} columns from {dict_in}")
    B, bars = budgets_for(N)
    Ba, _ = budgets_for(N, variant="asymptotic")
    out = {"N": N, "budgets_matched": list(B), "budgets_asymptotic": list(Ba),
           "S_stop": S_stop, "cells": []}
    for (tau2, eps) in cells:
        p = GateParams(N=N, budgets=B, eps1=eps, epsF=eps, eps3=eps,
                       C_led=100.0, fuzz="none", Wcap=8, Vgrid=VGRID,
                       tier2_tau=tau2)
        label = f"t2 N{N} tau{tau2:g} eps{eps:g}"
        conv = converge_cell(cols_rows, geom, p, pool, "nd", S_round, S_stop,
                             max_rounds, max_outer, seed0=9_000_000
                             + int(tau2 * 1000) + int(eps * 10 ** 5), label=label)
        rec, full, base, cal = cell_record(cols_rows, p, "nd")
        rec.update(tau2=tau2, eps=eps, variant="matched",
                   converged=conv["converged"], colgen=dict(
                       outer_used=conv["outer_used"], secs=conv["secs"],
                       verify=conv["verify"]))
        out["cells"].append(rec)
        log(f"[{label}] FINAL P_full={rec['P_full']:.7f} "
            f"P_base={rec['P_base']:.7f} delta0'={rec['delta_0']:.3e} "
            f"converged={rec['converged']}")
        save_dict(os.path.join(RUNS, dict_out), cols_rows)

        if do_witness_cell == (tau2, eps):
            # decision-grade witness + rational verification (incl. T2 rows)
            cr_true, fullw, basew, calw = solve_targets(cols_rows, p, "nd")
            law, E = witness_from(cols_rows, p, "nd", fullw, cr_true)
            rv = rational_verify_t2(with_obj(cr_true, "nd"), p, fullw)
            out["witness"] = dict(
                cell=dict(tau2=tau2, eps=eps, variant="matched",
                          fuzz="none", C_led=100.0, Wcap=8),
                P=fullw["P"], law=law, E=E, rational_verify=rv,
                active_rows={k: round(v, 8) for k, v in
                             (fullw.get("active_rows") or {}).items()})
            log(f"[{label}] witness: support={len(law)} "
                f"rational all_ok={rv['all_ok']}")
            # budget re-centering stability (SPEC 5.4 absorption rule):
            pa = GateParams(N=N, budgets=Ba, eps1=eps, epsF=eps, eps3=eps,
                            C_led=100.0, fuzz="none", Wcap=8, Vgrid=VGRID,
                            tier2_tau=tau2)
            conva = converge_cell(cols_rows, geom, pa, pool, "nd",
                                  S_round=S_stop, S_stop=S_stop, max_rounds=2,
                                  max_outer=3, seed0=9_500_000, label=label + " asym")
            reca, _, _, _ = cell_record(cols_rows, pa, "nd")
            reca.update(tau2=tau2, eps=eps, variant="asymptotic",
                        converged=conva["converged"], colgen=dict(
                            outer_used=conva["outer_used"], secs=conva["secs"],
                            verify=conva["verify"]))
            out["recenter_asymptotic"] = reca
            log(f"[{label} asym] P_full={reca['P_full']:.7f} "
                f"P_base={reca['P_base']:.7f} delta0'={reca['delta_0']:.3e}")
            save_dict(os.path.join(RUNS, dict_out), cols_rows)

    with open(os.path.join(RUNS, out_name), "w") as f:
        json.dump(out, f, indent=1, default=str)
    pool.close(); pool.join()
    log(f"phase t2 N={N} done in {time.time()-t0:.0f}s -> {out_name}")


def phase_p1(N=64, dict_in="dict_N64_fu.json", dict_out="dict_N64_fu.json",
             S_round=64, S_stop=200, max_rounds=40, max_outer=8):
    import multiprocessing as mp
    pool = mp.get_context("spawn").Pool(2)
    t0 = time.time()
    geom = Geometry(N, 1.0, 0.5, ("flat",), ("flat",))
    path_in = os.path.join(RUNS, dict_in)
    if not os.path.exists(path_in):
        path_in = os.path.join(RUNS, f"dict_N{N}.json")
    cols_rows = load_dict(path_in, N)
    log(f"p1 N={N}: loaded {len(cols_rows)} columns from {os.path.basename(path_in)}")
    B, bars = budgets_for(N)
    Ba, _ = budgets_for(N, variant="asymptotic")
    out = {"N": N, "objective": "p1 simple-point fraction "
           "(mark-1 atoms + 2 x mult-1 pairs)", "S_stop": S_stop, "cells": []}
    cells = [("matched", B, 0.05), ("asymptotic", Ba, 0.002)]
    for variant, Bv, eps in cells:
        p = GateParams(N=N, budgets=Bv, eps1=eps, epsF=eps, eps3=eps,
                       C_led=100.0, fuzz="none", Wcap=8, Vgrid=VGRID)
        label = f"p1 N{N} {variant} eps{eps:g}"
        conv = converge_cell(cols_rows, geom, p, pool, "p1", S_round, S_stop,
                             max_rounds, max_outer,
                             seed0=11_000_000 + int(eps * 10 ** 6), label=label)
        rec, full, base, cal = cell_record(cols_rows, p, "p1")
        # analytic marks-{1,2} corner for comparison: p1 = 2 - (B1/N)(1+eps)
        rec.update(variant=variant, eps=eps, fuzz="none", C_led=100.0,
                   converged=conv["converged"],
                   corner_analytic=2.0 - (Bv[0] / N) * (1 + eps),
                   colgen=dict(outer_used=conv["outer_used"], secs=conv["secs"],
                               verify=conv["verify"]))
        # witness for the full system + rational verification
        cr_true, fullw, _, _ = solve_targets(cols_rows, p, "p1")
        law, E = witness_from(cols_rows, p, "p1", fullw, cr_true)
        rv = rational_verify(with_obj(cr_true, "p1"), p, fullw)
        rec["witness"] = dict(P=fullw["P"], law_support=len(law), E=E,
                              rational_all_ok=rv["all_ok"])
        rec["witness_law"] = law
        rec["rational_verify"] = rv
        out["cells"].append(rec)
        log(f"[{label}] FINAL p1_full={rec['P_full']:.7f} "
            f"p1_base={rec['P_base']:.7f} p1_cal={rec['P_cal']:.7f} "
            f"delta={rec['delta_0']:.3e} corner={rec['corner_analytic']:.7f} "
            f"converged={rec['converged']}")
        save_dict(os.path.join(RUNS, dict_out), cols_rows)

    # LP-only cross-checks over the final dictionary (no colgen; labeled):
    # (i) coupled-fuzz variant at the primary cell; (ii) W-scan; (iii) the
    # on-line-only objective variant (pairs excluded from the simple count).
    p = GateParams(N=N, budgets=B, eps1=0.05, epsF=0.05, eps3=0.05,
                   C_led=100.0, fuzz="coupled", Wcap=8, Vgrid=VGRID)
    rec, _, _, _ = cell_record(cols_rows, p, "p1")
    out["primary_coupled_fuzz_LP_only"] = {k: rec[k] for k in
                                           ("P_full", "P_base", "P_cal",
                                            "delta_0", "status")}
    wscan = []
    for W in (2, 3, 4, 6, 8):
        pw = GateParams(N=N, budgets=B, eps1=0.05, epsF=0.05, eps3=0.05,
                        C_led=100.0, fuzz="none", Wcap=W, Vgrid=VGRID)
        r, _, _, _ = cell_record(cols_rows, pw, "p1")
        wscan.append(dict(W=W, P_full=r["P_full"], P_base=r["P_base"],
                          delta_0=r["delta_0"]))
    out["W_scan_LP_only"] = wscan

    def nsimple_online(cfg):
        return int(np.sum(cfg.atom_mrk == 1)) if len(cfg.atom_mrk) else 0

    cr_true = filter_W(cols_rows, 8)
    cr_ol = [(cfg, Rows(r.F1, r.Fp, r.Cp, r.nV, r.nneg, nsimple_online(cfg),
                        r.mass, r.eig_consistency, r.S1))
             for cfg, r in cr_true]
    p = GateParams(N=N, budgets=B, eps1=0.05, epsF=0.05, eps3=0.05,
                   C_led=100.0, fuzz="none", Wcap=8, Vgrid=VGRID)
    fol = solve_master(cr_ol, p, include_cubic=True, include_Fp=True)
    bol = solve_master(cr_ol, p, include_cubic=False, include_Fp=True)
    out["online_only_objective_LP_only"] = dict(
        P_full=fol.get("P"), P_base=bol.get("P"),
        delta_0=(fol["P"] - bol["P"]) if fol.get("P") is not None else None,
        note="labeled diagnostic: simple count restricted to on-line atoms; "
             "no colgen under this objective")

    with open(os.path.join(RUNS, f"followup_p1_N{N}.json"), "w") as f:
        json.dump(out, f, indent=1, default=str)
    pool.close(); pool.join()
    log(f"phase p1 done in {time.time()-t0:.0f}s")


if __name__ == "__main__":
    phase = sys.argv[1] if len(sys.argv) > 1 else "t2n64"
    if phase == "t2n64":
        phase_t2(64, cells=[(1.0, 0.05), (1.0, 0.02), (4.0, 0.05), (4.0, 0.02)],
                 dict_in="dict_N64.json", dict_out="dict_N64_fu.json",
                 out_name="followup_tier2_N64.json", S_round=64, S_stop=200,
                 max_rounds=40, max_outer=8, do_witness_cell=(1.0, 0.05))
    elif phase == "t2n128":
        phase_t2(128, cells=[(1.0, 0.05)],
                 dict_in="dict_N128.json", dict_out="dict_N128_fu.json",
                 out_name="followup_tier2_N128.json", S_round=48, S_stop=200,
                 max_rounds=40, max_outer=6, do_witness_cell=(1.0, 0.05))
    elif phase == "p1":
        phase_p1()
    else:
        raise SystemExit(f"unknown phase {phase}")
