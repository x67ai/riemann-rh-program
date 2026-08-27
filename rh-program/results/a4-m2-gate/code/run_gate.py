#!/usr/bin/env python3
"""
A4 M2 gate -- run_gate.py: the orchestrating driver (SPEC section 7 order).

Phases (CLI: python3 run_gate.py <phase> [options]):
  colgen   -- column generation to convergence at anchor points (N = 64)
  scans    -- re-solve master over the accumulated dictionary at the whole
              (W, C_led, eps, Gamma, budget-variant) grid + pricing verification
  n128     -- N = 128 confirmation at the primary point
  explore  -- exploratory lambda' in {0.55, 0.6, 0.65} (labeled; outside
              proven-ladder regime)
  windows  -- cos-window combos (secondary; marginal cubic value only)
  tier2    -- near-CUE-pinned diagnostic at the primary point

State: dictionary persisted to runs/dict_N{N}.npz (configs + row values).
"""
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kernels import Geometry, Config, rows_for, c_coeffs
from dictionary import build_seed_dictionary
from master_lp import GateParams, solve_master, gate_point, rational_verify, filter_W
from column_gen import dual_coeffs, price, RC_TOL

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUNS = os.path.join(BASE, "runs")

VGRID = (2, 3, 4, 6, 8, 12, 16)


# ---------------------------------------------------------------- persistence
def save_dict(path, cols_rows):
    blobs = []
    for cfg, r in cols_rows:
        blobs.append(dict(
            ap=cfg.atom_pos.tolist(), am=cfg.atom_mrk.tolist(),
            pp=cfg.pair_pos.tolist(), pm=cfg.pair_mrk.tolist(),
            pd=cfg.pair_d.tolist(), tag=cfg.tag,
            F1=r.F1, Fp=r.Fp, Cp=r.Cp, nV=r.nV.tolist(), nneg=r.nneg,
            Nd=r.Nd, mass=r.mass, S1=(r.S1.tolist() if r.S1 is not None else None)))
    with open(path, "w") as f:
        json.dump(blobs, f)


def load_dict(path, N):
    from kernels import Rows
    with open(path) as f:
        blobs = json.load(f)
    out = []
    for b in blobs:
        cfg = Config(N, np.array(b["ap"]), np.array(b["am"], dtype=int),
                     np.array(b["pp"]), np.array(b["pm"], dtype=int),
                     np.array(b["pd"]), b["tag"])
        r = Rows(b["F1"], b["Fp"], b["Cp"], np.array(b["nV"]), b["nneg"],
                 b["Nd"], b["mass"], 0.0,
                 np.array(b["S1"]) if b["S1"] is not None else None)
        out.append((cfg, r))
    return out


def budgets_for(N, lamp=0.5, variant="matched"):
    tagl = str(lamp).replace(".", "p")
    with open(os.path.join(RUNS, f"budgets_lam{tagl}.json")) as f:
        bud = json.load(f)
    s = bud["sizes"][str(N)]
    closed = bud["closed_forms"]
    if variant == "matched":
        B = (s["m2_1"]["mean"] * N, s["m2p"]["mean"] * N, s["m3p"]["mean"] * N)
    else:
        B = (closed["m2_1"] * N, closed["m2p"] * N, closed["m3p"] * N)
    # bars: 2 SE + |analytic - MC| finite-size envelope (SPEC 2.2), per period
    bars = tuple((2 * s[k]["se"] + abs(closed[k] - s[k]["mean"])) * N
                 for k in ("m2_1", "m2p", "m3p"))
    return B, bars


# ---------------------------------------------------------------- column generation
def colgen_at(cols_rows, geom, p, pool, targets=("full", "base"), S_round=48,
              max_rounds=25, seed0=1000, verbose=True, tier2=False):
    """Alternating master/pricing until no improving column (per target)."""
    known = {cfg.key() for cfg, _ in cols_rows}
    history = []
    for rnd in range(max_rounds):
        found_any = False
        for tgt in targets:
            sol = solve_master(filter_W(cols_rows, p.Wcap), p,
                               include_cubic=(tgt == "full"), include_Fp=True)
            if sol["status"] != 0:
                history.append((rnd, tgt, "infeasible", None, 0))
                continue
            w = dual_coeffs(sol, p)
            cr_f = filter_W(cols_rows, p.Wcap)
            support = [cfg for i, (cfg, _) in enumerate(cr_f)
                       if sol["x"][i] > 1e-6]
            found = price(geom, w, p, support, S_round, pool,
                          seed0=seed0 + 100000 * rnd + (0 if tgt == "full" else 50000))
            newc = 0
            for rc, cfg in found[:30]:
                if cfg.key() in known or cfg.mass() != geom.N:
                    continue
                r, _ = rows_for(cfg, geom, tier2=tier2)
                if r.eig_consistency > 1e-8 or r.nneg > cfg.npairs():
                    continue
                cols_rows.append((cfg, r))
                known.add(cfg.key())
                newc += 1
            history.append((rnd, tgt, sol["P"], found[0][0] if found else 0.0, newc))
            if verbose:
                print(f"  round {rnd} {tgt}: P={sol['P']:.5f} "
                      f"best_rc={found[0][0] if found else 0.0:+.5f} new={newc}",
                      flush=True)
            found_any |= newc > 0
        if not found_any:
            break
    return history


def verify_optimality(cols_rows, geom, p, S_verify, pool,
                      targets=("full", "base"), seed0=777000):
    """Final pricing pass; returns min rc found per target (heuristic bound)."""
    out = {}
    for tgt in targets:
        sol = solve_master(filter_W(cols_rows, p.Wcap), p,
                           include_cubic=(tgt == "full"), include_Fp=True)
        if sol["status"] != 0:
            out[tgt] = dict(status="infeasible")
            continue
        w = dual_coeffs(sol, p)
        cr_f = filter_W(cols_rows, p.Wcap)
        support = [cfg for i, (cfg, _) in enumerate(cr_f) if sol["x"][i] > 1e-6]
        found = price(geom, w, p, support, S_verify, pool, seed0=seed0)
        out[tgt] = dict(P=sol["P"], min_rc=found[0][0] if found else 0.0,
                        n_improving=len(found), S=S_verify)
    return out


# ---------------------------------------------------------------- phases
def phase_colgen(N=64, S_round=48, S_verify=200):
    import multiprocessing as mp
    pool = mp.get_context("spawn").Pool(4)
    t0 = time.time()
    geom = Geometry(N, 1.0, 0.5, ("flat",), ("flat",))
    dpath = os.path.join(RUNS, f"dict_N{N}.json")
    if os.path.exists(dpath):
        cols_rows = load_dict(dpath, N)
        print(f"loaded dictionary: {len(cols_rows)} columns")
    else:
        cols = build_seed_dictionary(N, geom, W=8)
        cols_rows = []
        for c in cols:
            r, _ = rows_for(c, geom, tier2=True)
            assert r.eig_consistency < 1e-8, c.tag
            assert r.nneg <= c.npairs(), c.tag
            cols_rows.append((c, r))
        print(f"seed dictionary: {len(cols_rows)} columns")
    B, bars = budgets_for(N)

    anchors = [
        dict(Wcap=8, eps=0.05, C_led=100.0, fuzz="coupled", rounds=25),
        dict(Wcap=8, eps=0.05, C_led=100.0, fuzz="none", rounds=15),
        dict(Wcap=3, eps=0.05, C_led=100.0, fuzz="coupled", rounds=15),
        dict(Wcap=4, eps=0.05, C_led=100.0, fuzz="coupled", rounds=10),
        dict(Wcap=6, eps=0.05, C_led=100.0, fuzz="coupled", rounds=10),
        dict(Wcap=8, eps=0.02, C_led=10.0, fuzz="coupled", rounds=10),
        dict(Wcap=8, eps=0.10, C_led=1000.0, fuzz="coupled", rounds=8),
        dict(Wcap=2, eps=0.05, C_led=100.0, fuzz="coupled", rounds=8),
    ]
    log = {}
    for i, a in enumerate(anchors):
        p = GateParams(N=N, budgets=B, eps1=a["eps"], epsF=a["eps"],
                       eps3=a["eps"], C_led=a["C_led"], fuzz=a["fuzz"],
                       Wcap=a["Wcap"], Vgrid=VGRID)
        print(f"anchor {i}: W={a['Wcap']} eps={a['eps']} C={a['C_led']} "
              f"fuzz={a['fuzz']}", flush=True)
        h = colgen_at(cols_rows, geom, p, pool, S_round=S_round,
                      max_rounds=a["rounds"], seed0=1000 + 10 ** 6 * i, tier2=True)
        log[f"anchor_{i}"] = dict(a, history=[(r, t, P, rc, n) for r, t, P, rc, n in h])
        save_dict(dpath, cols_rows)
        print(f"  dictionary now {len(cols_rows)} columns "
              f"[{time.time()-t0:.0f}s]", flush=True)

    # final verification at the primary point
    p = GateParams(N=N, budgets=B, eps1=0.05, epsF=0.05, eps3=0.05,
                   C_led=100.0, fuzz="coupled", Wcap=8, Vgrid=VGRID)
    ver = verify_optimality(cols_rows, geom, p, S_verify, pool)
    log["verify_primary"] = ver
    print("primary verification:", ver)
    save_dict(dpath, cols_rows)
    with open(os.path.join(RUNS, f"colgen_N{N}.json"), "w") as f:
        json.dump(log, f, indent=1, default=str)
    pool.close(); pool.join()
    print(f"phase colgen done in {time.time()-t0:.0f}s; "
          f"{len(cols_rows)} columns")


def phase_scans(N=64, S_check=40):
    import multiprocessing as mp
    pool = mp.get_context("spawn").Pool(4)
    t0 = time.time()
    geom = Geometry(N, 1.0, 0.5, ("flat",), ("flat",))
    cols_rows = load_dict(os.path.join(RUNS, f"dict_N{N}.json"), N)
    print(f"{len(cols_rows)} columns")
    out = {"N": N, "grid": []}
    for variant in ("matched", "asymptotic"):
        B, bars = budgets_for(N, variant=variant)
        for W in (2, 3, 4, 6, 8):
            for C_led in (10.0, 100.0, 1000.0):
                for eps in (0.02, 0.05, 0.10):
                    for fz, Gam in (("coupled", 0.0), ("none", 0.0),
                                    ("gamma", 0.05), ("gamma", 0.10),
                                    ("gamma", 0.25)):
                        for use_bars in (False, True):
                            p = GateParams(N=N, budgets=B, eps1=eps, epsF=eps,
                                           eps3=eps, C_led=C_led, fuzz=fz,
                                           Gamma=Gam, Wcap=W, Vgrid=VGRID,
                                           bars=bars if use_bars else (0, 0, 0))
                            o, full, base, cal = gate_point(cols_rows, p)
                            rec = dict(variant=variant, W=W, C_led=C_led,
                                       eps=eps, fuzz=fz, Gamma=Gam,
                                       bars=use_bars, **{k: o[k] for k in
                                       ("P_full", "P_base", "P_cal", "delta_0",
                                        "g_full", "status")})
                            rec["active_full"] = o["active_full"]
                            out["grid"].append(rec)
        print(f"variant {variant} done [{time.time()-t0:.0f}s]", flush=True)

    # pricing spot-verification at W-scan points (centered, primary eps/C)
    B, bars = budgets_for(N, variant="matched")
    ver = {}
    for W in (3, 4, 6, 8):
        p = GateParams(N=N, budgets=B, eps1=0.05, epsF=0.05, eps3=0.05,
                       C_led=100.0, fuzz="coupled", Wcap=W, Vgrid=VGRID)
        ver[f"W{W}"] = verify_optimality(cols_rows, geom, p, S_check, pool,
                                         seed0=555000 + W)
        print(f"verify W={W}: {ver[f'W{W}']}", flush=True)
    out["verify"] = ver
    with open(os.path.join(RUNS, f"scans_N{N}.json"), "w") as f:
        json.dump(out, f, indent=1, default=str)
    pool.close(); pool.join()
    print(f"phase scans done in {time.time()-t0:.0f}s")


def phase_n128(S_round=32, S_verify=100):
    phase_colgen(N=128, S_round=S_round, S_verify=S_verify)
    phase_scans_confirm(N=128)


def phase_scans_confirm(N=128):
    """Reduced grid at N = 128: primary point + W-scan, centered + bars."""
    t0 = time.time()
    cols_rows = load_dict(os.path.join(RUNS, f"dict_N{N}.json"), N)
    out = {"N": N, "grid": []}
    for variant in ("matched", "asymptotic"):
        B, bars = budgets_for(N, variant=variant)
        for W in (2, 3, 4, 6, 8):
            for fz, Gam in (("coupled", 0.0), ("none", 0.0)):
                for use_bars in (False, True):
                    p = GateParams(N=N, budgets=B, eps1=0.05, epsF=0.05,
                                   eps3=0.05, C_led=100.0, fuzz=fz, Gamma=Gam,
                                   Wcap=W, Vgrid=VGRID,
                                   bars=bars if use_bars else (0, 0, 0))
                    o, full, base, cal = gate_point(cols_rows, p)
                    out["grid"].append(dict(variant=variant, W=W, fuzz=fz,
                                            bars=use_bars,
                                            **{k: o[k] for k in
                                               ("P_full", "P_base", "P_cal",
                                                "delta_0", "g_full", "status")}))
    with open(os.path.join(RUNS, f"scans_N{N}.json"), "w") as f:
        json.dump(out, f, indent=1, default=str)
    print(f"N=128 confirm done in {time.time()-t0:.0f}s")



def phase_tighteps(N=64, S_round=48, S_verify=200):
    """eps -> 0 drill (beyond the SPEC grid, labeled): the asymptotic system."""
    import multiprocessing as mp
    pool = mp.get_context("spawn").Pool(4)
    t0 = time.time()
    geom = Geometry(N, 1.0, 0.5, ("flat",), ("flat",))
    dpath = os.path.join(RUNS, f"dict_N{N}.json")
    cols_rows = load_dict(dpath, N)
    out = {"eps_trend": []}
    for variant in ("matched", "asymptotic"):
        B, bars = budgets_for(N, variant=variant)
        for eps in (0.02, 0.01, 0.005, 0.002):
            for fz in ("none", "coupled"):
                p = GateParams(N=N, budgets=B, eps1=eps, epsF=eps, eps3=eps,
                               C_led=100.0, fuzz=fz, Wcap=8, Vgrid=VGRID)
                colgen_at(cols_rows, geom, p, pool, S_round=S_round,
                          max_rounds=8, seed0=3_000_000 + int(eps * 10 ** 5),
                          verbose=False, tier2=True)
                o, full, base, cal = gate_point(cols_rows, p)
                rec = dict(variant=variant, eps=eps, fuzz=fz,
                           P_full=o["P_full"], P_base=o["P_base"],
                           P_cal=o["P_cal"], delta_0=o["delta_0"],
                           g=o["g_full"], status=o["status"])
                out["eps_trend"].append(rec)
                print(f"{variant} eps={eps} fuzz={fz}: P_full={o['P_full']} "
                      f"P_base={o['P_base']} d0={o['delta_0']}", flush=True)
        save_dict(dpath, cols_rows)
    # verification at the tightest asymptotic point
    B, bars = budgets_for(N, variant="asymptotic")
    p = GateParams(N=N, budgets=B, eps1=0.002, epsF=0.002, eps3=0.002,
                   C_led=100.0, fuzz="none", Wcap=8, Vgrid=VGRID)
    out["verify_tightest"] = verify_optimality(cols_rows, geom, p, S_verify, pool)
    print("verify tightest:", out["verify_tightest"])
    save_dict(dpath, cols_rows)
    with open(os.path.join(RUNS, f"tighteps_N{N}.json"), "w") as f:
        json.dump(out, f, indent=1, default=str)
    pool.close(); pool.join()
    print(f"phase tighteps done in {time.time()-t0:.0f}s")


def phase_tier2(N=64, S_round=48, S_verify=120):
    """Near-CUE-pinned diagnostic (SPEC 4.3/5.4 Tier-2 annotation)."""
    import multiprocessing as mp
    pool = mp.get_context("spawn").Pool(4)
    t0 = time.time()
    geom = Geometry(N, 1.0, 0.5, ("flat",), ("flat",))
    dpath = os.path.join(RUNS, f"dict_N{N}.json")
    cols_rows = load_dict(dpath, N)
    out = {"tier2": []}
    B, bars = budgets_for(N, variant="matched")
    for tau2 in (4.0, 1.0):
        for eps in (0.05, 0.02):
            p = GateParams(N=N, budgets=B, eps1=eps, epsF=eps, eps3=eps,
                           C_led=100.0, fuzz="none", Wcap=8, Vgrid=VGRID,
                           tier2_tau=tau2)
            colgen_at(cols_rows, geom, p, pool, S_round=S_round,
                      max_rounds=60, seed0=4_100_000 + int(tau2 * 1000),
                      verbose=False, tier2=True)
            o, full, base, cal = gate_point(cols_rows, p)
            rec = dict(tau2=tau2, eps=eps, P_full_T2=o["P_full"],
                       P_base_T2=o["P_base"], delta_0_T2=o["delta_0"],
                       status=o["status"], active_full=o["active_full"])
            out["tier2"].append(rec)
            print(f"tau2={tau2} eps={eps}: P_full_T2={o['P_full']} "
                  f"P_base_T2={o['P_base']} d0'={o['delta_0']}", flush=True)
            save_dict(dpath, cols_rows)
    p = GateParams(N=N, budgets=B, eps1=0.05, epsF=0.05, eps3=0.05,
                   C_led=100.0, fuzz="none", Wcap=8, Vgrid=VGRID, tier2_tau=1.0)
    out["verify"] = verify_optimality(cols_rows, geom, p, S_verify, pool,
                                      seed0=888000)
    print("tier2 verify:", out["verify"])
    save_dict(dpath, cols_rows)
    with open(os.path.join(RUNS, f"tier2_N{N}.json"), "w") as f:
        json.dump(out, f, indent=1, default=str)
    pool.close(); pool.join()
    print(f"phase tier2 done in {time.time()-t0:.0f}s")


def phase_explore(S_round=32):
    """Exploratory lambda' in {0.55, 0.6, 0.65} (labeled: outside the proven
    theta < 1 ladder regime; M5 payoff-curve table)."""
    import multiprocessing as mp
    pool = mp.get_context("spawn").Pool(4)
    t0 = time.time()
    N = 64
    out = {"explore": []}
    for lamp in (0.55, 0.60, 0.65):
        geom = Geometry(N, 1.0, lamp, ("flat",), ("flat",))
        cols = build_seed_dictionary(N, geom, W=8, null_count=60, rand_count=40)
        cols_rows = []
        for c in cols:
            r, _ = rows_for(c, geom, tier2=True)
            if r.eig_consistency < 1e-8 and r.nneg <= c.npairs():
                cols_rows.append((c, r))
        B, bars = budgets_for(N, lamp=lamp, variant="matched")
        for eps in (0.05, 0.02):
            p = GateParams(N=N, budgets=B, eps1=eps, epsF=eps, eps3=eps,
                           C_led=100.0, fuzz="none", Wcap=8, Vgrid=VGRID)
            colgen_at(cols_rows, geom, p, pool, S_round=S_round, max_rounds=8,
                      seed0=5_000_000 + int(lamp * 1000), verbose=False,
                      tier2=True)
            o, full, base, cal = gate_point(cols_rows, p)
            rec = dict(lamp=lamp, eps=eps, P_full=o["P_full"],
                       P_base=o["P_base"], P_cal=o["P_cal"],
                       delta_0=o["delta_0"], status=o["status"])
            out["explore"].append(rec)
            print(f"lamp={lamp} eps={eps}: P_full={o['P_full']} "
                  f"P_base={o['P_base']} d0={o['delta_0']}", flush=True)
        save_dict(os.path.join(RUNS, f"dict_N{N}_lam{str(lamp).replace('.','p')}.json"),
                  cols_rows)
    with open(os.path.join(RUNS, "explore_lamp.json"), "w") as f:
        json.dump(out, f, indent=1, default=str)
    pool.close(); pool.join()
    print(f"phase explore done in {time.time()-t0:.0f}s")


def phase_windows(S_round=32):
    """Secondary window scan: marginal value of the cubic block only."""
    import multiprocessing as mp
    from null_budgets import run_size
    pool = mp.get_context("spawn").Pool(4)
    t0 = time.time()
    N = 64
    combos = [
        (("flat",), ("cos", 0.8), "flat_cos08"),
        (("cos", 1 / 2 ** 0.5), ("flat",), "cosMT_flat"),
        (("cos", 1 / 2 ** 0.5), ("cos", 0.8), "cosMT_cos08"),
    ]
    out = {"windows": []}
    for win1, winp, tag in combos:
        geom = Geometry(N, 1.0, 0.5, win1, winp)
        # matched budgets for this window combo (same sampler, same code path)
        st = run_size(N, 0.5, 2500, True, pool, seed0=6_000_000,
                      win1=win1, winp=winp)
        B = (st["m2_1"]["mean"] * N, st["m2p"]["mean"] * N, st["m3p"]["mean"] * N)
        cols = build_seed_dictionary(N, geom, W=8, null_count=60, rand_count=40)
        cols_rows = []
        for c in cols:
            r, _ = rows_for(c, geom, tier2=True)
            if r.eig_consistency < 1e-8 and r.nneg <= c.npairs():
                cols_rows.append((c, r))
        for eps in (0.05, 0.02):
            p = GateParams(N=N, budgets=B, eps1=eps, epsF=eps, eps3=eps,
                           C_led=100.0, fuzz="none", Wcap=8, Vgrid=VGRID)
            colgen_at(cols_rows, geom, p, pool, S_round=S_round, max_rounds=8,
                      seed0=7_000_000, verbose=False, tier2=True)
            o, full, base, cal = gate_point(cols_rows, p)
            rec = dict(combo=tag, eps=eps, budgets=[round(b, 3) for b in B],
                       P_full=o["P_full"], P_base=o["P_base"], P_cal=o["P_cal"],
                       delta_0=o["delta_0"], status=o["status"])
            out["windows"].append(rec)
            print(f"{tag} eps={eps}: d0={o['delta_0']} P_full={o['P_full']}",
                  flush=True)
    with open(os.path.join(RUNS, "windows_N64.json"), "w") as f:
        json.dump(out, f, indent=1, default=str)
    pool.close(); pool.join()
    print(f"phase windows done in {time.time()-t0:.0f}s")


if __name__ == "__main__":
    phase = sys.argv[1] if len(sys.argv) > 1 else "colgen"
    if phase == "colgen":
        phase_colgen()
    elif phase == "scans":
        phase_scans()
    elif phase == "n128":
        phase_n128()
    elif phase == "tighteps":
        phase_tighteps()
    elif phase == "tier2":
        phase_tier2()
    elif phase == "explore":
        phase_explore()
    elif phase == "windows":
        phase_windows()
    else:
        raise SystemExit(f"unknown phase {phase}")
