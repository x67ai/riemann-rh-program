"""n128_rerun.py -- Session 8 (2026-08-26): the mechanical N = 128 re-run of the
pair-channel certified curves (pair-channel.md O4: "all constants certified at
N = 64 ... The N = 128 re-run is mechanical (`pairchan_verify_all.py` is
N-parametric up to the grid constants)").

N-parametric re-implementation of the consolidated suite `pairchan_verify_all.py`
(vectorized, same formulas, same seed), run at BOTH:
  * N = 64  (control: must reproduce the stored pairchan_verify_out.json), and
  * N = 128 (the deliverable).

Model at general even N: M = N + 1 harmonics u_j = 1/M (|j| <= N/2), weights
w_s = (M - |s|)/M^2 (|s| <= N), circle circumference N (mean-gap units), grid
Delta = N/M, psi-zero grid g_k = k Delta (k = 0..N).  The depth family is in
mean-gap units (w = 2 pi d), hence N-independent: R5 family d <= 1/(2 pi).

Sections (as in pairchan_verify_all.py):
  V  basic identities (grid Parseval, block law, witness columns, translate sums,
     C-S chain)
  X  fractional-mark counterexample (exact closed-form match)
  I  exact interference identity (single pair)
  D  spectral backstop: tr B = M(c), tr B^2 = F1, n_+(B) <= #atoms + #pairs,
     N_d >= (4/9)(3 Mass - F1)
  C  capacity curves nu(y), S1(y), S1corr(y), joint-kernel Sgen2 windows,
     deep-tail ratios, alpha, abar table
  C8 Session-8 addition (both N): the corner behavior of Sgen2 near the R5
     endpoint -- the both-capped sup at Y* = 0.156, point values at d = d' =
     0.158/0.159/0.1591, and the crossing bracket of Sgen2 = 1.  (Session 8's
     interval certification found the Session-7 "0.9775 on the full family" to
     be a 0.004-grid artifact at N = 64: the continuum family sup exceeds 1
     beyond d ~= 0.1577.  The honest N = 128 re-run must check this too.)
  B  Theorem B(i) constants: max nu_joint over (0, 0.13]^2 and the in-cell
     coupling floor Phi_0 (float grade, as in the Session-7 record)

Float grade (numpy), same as the Session-7 certification it replicates; the
x-sampling density per cell is kept at the original's ~185 points/cell.
Writes n128_rerun_out.json next to this file.  THERMAL: single process.
"""
import json
import os
import time

import numpy as np

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))


class Model:
    def __init__(self, N):
        self.N = N
        self.M = N + 1
        self.J = N // 2
        self.S = np.arange(-N, N + 1)
        self.W = (self.M - np.abs(self.S)) / self.M ** 2
        self.JJ = np.arange(-self.J, self.J + 1)
        self.U = np.full(self.M, 1.0 / self.M)
        self.Delta = N / self.M
        self.GRID = np.arange(self.M) * self.Delta
        # x-sampling: original count at N = 64 (control must match the stored
        # record); same per-cell density (~185/cell) at other N
        self.NX = 12001 if N == 64 else 185 * self.M + 1
        self.xs = np.linspace(0, N, self.NX, endpoint=False)
        self.cell_idx = np.floor((self.xs / self.Delta) + 0.5).astype(int) % self.M
        self.PH = np.exp(-2j * np.pi * np.outer(self.xs, self.JJ) / N)
        order = np.argsort(self.cell_idx, kind="stable")
        self._order = order
        cs = self.cell_idx[order]
        self._starts = np.searchsorted(cs, np.arange(self.M + 1))
        self._Rcache = {}

    def abar(self, x):
        return float(np.sum(self.U * np.cosh(2.0 * np.pi * self.JJ * x / self.N)))

    def psiN(self, z):
        return complex(np.sum(self.U * np.exp(-2j * np.pi * self.JJ * z / self.N)))

    def assemble_c(self, atoms, pairs):
        c = np.zeros(len(self.S), dtype=complex)
        for (th, m) in atoms:
            c += m * np.exp(-2j * np.pi * self.S * th / self.N)
        for (th, d, m) in pairs:
            c += (2.0 * m * np.cosh(2.0 * np.pi * self.S * d / self.N)
                  * np.exp(-2j * np.pi * self.S * th / self.N))
        return c

    def F1(self, atoms, pairs):
        return float(np.sum(self.W * np.abs(self.assemble_c(atoms, pairs)) ** 2))

    @staticmethod
    def S2(atoms, pairs):
        return (sum(m * m for _, m in atoms)
                + 2 * sum(m * m for _, _, m in pairs))

    @staticmethod
    def Tgt(atoms, pairs):
        return (sum(3 * m - 2 for _, m in atoms)
                + sum(6 * m - 4 for _, _, m in pairs))

    def Rarr(self, y):
        key = round(float(y), 6)
        if key not in self._Rcache:
            g = np.exp(2.0 * np.pi * self.JJ * key / self.N) / self.M
            psi = self.PH @ g
            self._Rcache[key] = (psi * psi).real
        return self._Rcache[key]

    def nu_of(self, arr):
        a = -arr[self._order]
        st = self._starts
        return float(sum(max(0.0, a[st[k]:st[k + 1]].max())
                         for k in range(self.M)))


def run_suite(N, rng_seed=20260826):
    md = Model(N)
    rng = np.random.default_rng(rng_seed)
    out = {"N": N}
    # ---------- V ----------
    errs = []
    for _ in range(40):
        k = rng.integers(5, md.M + 1)
        sites = rng.choice(md.M, size=k, replace=False)
        marks = rng.integers(1, 9, size=k)
        atoms = [(md.GRID[i], int(m)) for i, m in zip(sites, marks)]
        errs.append(abs(md.F1(atoms, []) - md.S2(atoms, [])))
    out["V_grid_parseval_maxerr"] = max(errs)
    errs = []
    for _ in range(20):
        th, d, m = rng.uniform(0, N), rng.uniform(0.01, 1.0), int(rng.integers(1, 5))
        errs.append(abs(md.F1([], [(th, d, m)])
                        - 2 * m * m * (1 + md.abar(2 * d) ** 2)))
    out["V_pair_block_maxerr"] = max(errs)
    vac = [(md.GRID[i], 1) for i in range(1, md.M)]
    out["V_vacancy_F1"] = md.F1(vac, [])                    # want N exactly
    out["V_doubles_F1"] = md.F1([(md.GRID[i], 2) for i in range(N // 2)], [])
    tr_err = []
    for d in (0.1, 0.3, 0.7):
        x = rng.uniform(0, 1)
        s1 = sum((md.psiN(x + g + 1j * d) ** 2).real for g in md.GRID)
        s2v = sum(abs(md.psiN(x + g + 1j * d)) ** 2 for g in md.GRID)
        tr_err.append(abs(s1 - 1.0))
        tr_err.append(abs(s2v - md.abar(2 * d)))
    out["V_translate_identities_maxerr"] = max(tr_err)
    out["V_CS_chain_max_violation"] = max(
        md.abar(d) ** 2 - (1 + md.abar(2 * d)) / 2
        for d in np.linspace(0.01, 2.5, 60))
    # ---------- X ----------
    d, mu = 0.25, 0.05
    f = md.F1(vac, [(0.0, d, mu)])
    s = md.S2(vac, [(0.0, d, mu)])
    pred = 2 * mu ** 2 * md.abar(2 * d) ** 2 - 4 * mu * (md.abar(d) ** 2 - 1)
    out["X_fractional_F1_minus_S2"] = f - s
    out["X_fractional_predicted"] = pred
    out["X_violates"] = bool(f < s)
    # ---------- I ----------
    errs = []
    for _ in range(25):
        na = int(rng.integers(1, 8))
        atoms = [(float(rng.uniform(0, N)), int(rng.integers(1, 5)))
                 for _ in range(na)]
        th, dd, m = (float(rng.uniform(0, N)), float(rng.uniform(0.02, 1.2)),
                     int(rng.integers(1, 4)))
        lhs = md.F1(atoms, [(th, dd, m)]) - md.Tgt(atoms, [(th, dd, m)])
        slacks = (sum((ma - 1) * (ma - 2) for _, ma in atoms)
                  + 2 * (m - 1) * (m - 2))
        crosses = sum(atoms[i][1] * atoms[j][1]
                      * (md.psiN(atoms[i][0] - atoms[j][0]) ** 2).real
                      for i in range(na) for j in range(na) if i != j)
        coupling = 4 * m * sum(ma * (md.psiN(ta - th + 1j * dd) ** 2).real
                               for ta, ma in atoms)
        errs.append(abs(lhs - (slacks + crosses + coupling
                               + 2 * m * m * md.abar(2 * dd) ** 2)))
    out["I_identity_maxerr"] = max(errs)
    # ---------- D ----------
    def Bmat(atoms, pairs):
        c = md.assemble_c(atoms, pairs)
        idx = np.arange(md.M)
        return (np.sqrt(np.outer(md.U, md.U))
                * c[(idx[:, None] - idx[None, :]) + N])
    chk = []
    for _ in range(12):
        na, k = int(rng.integers(0, 5)), int(rng.integers(1, 4))
        atoms = [(float(rng.uniform(0, N)), int(rng.integers(1, 4)))
                 for _ in range(na)]
        pairs = [(float(rng.uniform(0, N)), float(rng.uniform(0.05, 1.5)),
                  int(rng.integers(1, 3))) for _ in range(k)]
        ev = np.linalg.eigvalsh(Bmat(atoms, pairs))
        Mass = sum(m for _, m in atoms) + 2 * sum(m for _, _, m in pairs)
        chk.append({
            "trB_minus_M": float(abs(ev.sum() - Mass)),
            "trB2_minus_F1": float(abs((ev ** 2).sum() - md.F1(atoms, pairs))),
            "npos_ok": bool((ev > 1e-9).sum() <= na + k),
            "backstop_holds": bool((na + 2 * k) >= (4.0 / 9.0)
                                   * (3 * Mass - md.F1(atoms, pairs)) - 1e-9),
        })
    out["D_all_npos_ok"] = all(c["npos_ok"] for c in chk)
    out["D_all_backstop"] = all(c["backstop_holds"] for c in chk)
    out["D_max_trB_err"] = max(c["trB_minus_M"] for c in chk)
    out["D_max_trB2_err"] = max(c["trB2_minus_F1"] for c in chk)
    # ---------- C ----------
    ygrid = ([round(y, 3) for y in np.arange(0.01, 1.01, 0.01)]
             + [1.25, 1.5, 1.75, 2.0])
    S1max = 0.0
    nu_tab = {}
    for y in ygrid:
        nu = md.nu_of(md.Rarr(y))
        nu_tab[y] = nu
        S1max = max(S1max, 8 * nu / (2 * md.abar(2 * y) ** 2))
    out["C_S1_max"] = S1max
    for yx in (0.05, 0.159, 0.318, 0.3183):
        if yx not in nu_tab:
            nu_tab[yx] = md.nu_of(md.Rarr(yx))
    out["C_nu_table"] = {str(y): round(nu_tab[y], 5) for y in
                         (0.05, 0.1, 0.159, 0.2, 0.25, 0.318, 0.4, 0.5,
                          0.7, 1.0, 1.5, 2.0)}

    def s1corr(y):
        Ry = md.Rarr(y)
        a = -Ry[md._order]
        st = md._starts
        kmax, nu, zw = 0.0, 0.0, 0.0
        for k in range(md.M):
            seg = a[st[k]:st[k + 1]]
            mx = max(0.0, float(seg.max()))
            nu += mx
            kmax = max(kmax, mx)
            xs_k = md.xs[md._order][st[k]:st[k + 1]]
            neg = xs_k[seg > 0]
            if len(neg) > 1:
                span = float(neg.max() - neg.min())
                if span < 5:
                    zw = max(zw, span)
        c0 = abs(md.psiN(min(zw, 0.9))) ** 2 if zw > 0 else 1.0
        best = max(4 * L * kmax - c0 * max(0, L * (L - 2)) for L in range(1, 80))
        mult = best / (8 * kmax) if kmax > 0 else 1.0
        return (8 * nu / (2 * md.abar(2 * y) ** 2)) * max(1.0, mult), kmax, zw, c0
    for yx in (0.45, 0.3183, 0.159):
        v = s1corr(yx)
        out[f"C_S1corr_at_{yx}"] = v[0]
        out[f"C_capconsts_at_{yx}"] = {"kappa_max": v[1], "zonewidth": v[2],
                                       "c0": v[3]}
    # Sgen2, mechanical Session-7 protocol: 0.004-step grid, both capped at Y
    dgrid = [round(x, 3) for x in np.arange(0.004, 0.1601, 0.004)]
    Ycap = 1 / (2 * np.pi)

    def nu_joint(d, dp):
        return md.nu_of(md.Rarr(d + dp) + md.Rarr(abs(d - dp)))

    def sgen2_grid(dcap, capmult, grid):
        worst, wd = 0.0, None
        ds = [d for d in grid if d <= dcap + 1e-12]
        for d in ds:
            supj = max(nu_joint(d, dp) for dp in ds)
            val = ((8 * md.nu_of(md.Rarr(d)) + capmult * supj)
                   / (2 * md.abar(2 * d) ** 2))
            if val > worst:
                worst, wd = val, d
        return worst, wd
    out["C_Sgen2_cap2_window_1over2pi_PROTOCOL7"] = sgen2_grid(Ycap, 4, dgrid)
    w_unc = None
    for dcap in (0.08, 0.10, 0.11, 0.115, 0.12, 0.125, 0.13):
        w, _ = sgen2_grid(dcap, 8, dgrid)
        if w <= 1.0:
            w_unc = dcap
    out["C_capmult8_largest_ok_dcap"] = w_unc
    out["C_deep_ratio_y1"] = md.abar(2.0) / md.abar(1.0)
    out["C_deep_ratio_target_A_ii"] = float(np.sqrt(2 * (N - 2)))
    out["alpha_exact"] = (np.pi / N) ** 2 * (md.M ** 2 - 1) / 3.0
    out["abar_values"] = {str(x): round(md.abar(x), 6) for x in
                          (0.1, 0.159, 0.2, 0.3183, 0.4, 0.6366, 1.0, 2.0)}
    # ---------- C8: Session-8 corner behavior ----------
    fine = [round(x, 4) for x in np.arange(0.002, 0.1561, 0.002)]
    out["C8_Sgen2_capped_0156"] = sgen2_grid(0.156, 4, fine)
    pts = {}
    for dd in (0.156, 0.157, 0.1575, 0.158, 0.159, 0.1591):
        supj = max(nu_joint(dd, dp) for dp in
                   [round(x, 4) for x in np.arange(0.002, dd + 1e-9, 0.002)]
                   + [dd])
        pts[str(dd)] = ((8 * md.nu_of(md.Rarr(dd)) + 4 * supj)
                        / (2 * md.abar(2 * dd) ** 2))
    out["C8_Sgen2_corner_points"] = pts
    cross = None
    for dd in np.arange(0.150, 0.1596, 0.0005):
        dd = round(float(dd), 4)
        supj = nu_joint(dd, dd)
        v = ((8 * md.nu_of(md.Rarr(dd)) + 4 * supj)
             / (2 * md.abar(2 * dd) ** 2))
        if v > 1.0 and cross is None:
            cross = dd
    out["C8_equal_depth_crossing_d"] = cross
    # ---------- B: Theorem B(i) constants (float grade) ----------
    best = 0.0
    g13 = [round(x, 4) for x in np.arange(0.004, 0.1301, 0.002)]
    for d1 in g13:
        for d2 in g13:
            if d2 < d1:
                continue
            best = max(best, nu_joint(d1, d2))
    out["B_max_nu_joint_013"] = best
    xh = md.Delta / 2
    phi0 = (min((md.psiN(xh + 1j * s) ** 2).real
                for s in [round(x, 3) for x in np.arange(0.002, 0.3184, 0.002)])
            + min((md.psiN(xh + 1j * t) ** 2).real
                  for t in [round(x, 3) for x in np.arange(0.0, 0.1592, 0.002)]))
    out["B_Phi0_floor_at_halfDelta"] = phi0
    out["B_selfconsistency_2nj_vs_Phi0"] = (2 * best, phi0, bool(2 * best < phi0))
    out["elapsed_s"] = round(time.time() - T0, 1)
    return out


def main():
    res = {}
    for N in (64, 128):
        print(f"==== running suite at N = {N} ====")
        res[str(N)] = run_suite(N)
        print(json.dumps(res[str(N)], indent=1, default=str))
    # control diff vs the stored Session-7 record
    stored_path = os.path.join(HERE, "pairchan_verify_out.json")
    diffs = {}
    if os.path.exists(stored_path):
        with open(stored_path) as fh:
            stored = json.load(fh)
        r64 = res["64"]
        for key, mine in (
                ("C_S1_max", r64["C_S1_max"]),
                ("C_S1corr_at_0.45", r64["C_S1corr_at_0.45"]),
                ("C_S1corr_at_0.3183", r64["C_S1corr_at_0.3183"]),
                ("C_S1corr_at_0.159", r64["C_S1corr_at_0.159"]),
                ("alpha_exact", r64["alpha_exact"]),
                ("C_deep_ratio_y1", r64["C_deep_ratio_y1"]),
                ("V_vacancy_F1", r64["V_vacancy_F1"]),
                ("X_fractional_F1_minus_S2", r64["X_fractional_F1_minus_S2"])):
            if key in stored:
                diffs[key] = {"stored": stored[key], "control": mine,
                              "absdiff": abs(float(stored[key]) - float(mine))}
        s7 = stored.get("C_Sgen2_cap2_window_1over2pi")
        if s7:
            diffs["C_Sgen2_grid_PROTOCOL7"] = {
                "stored": s7,
                "control": r64["C_Sgen2_cap2_window_1over2pi_PROTOCOL7"]}
    res["control_diff_vs_stored"] = diffs
    # comparison table
    print("\n==== N = 64 vs N = 128 comparison (key constants) ====")
    rows = [
        ("alpha (exact closed form)", "alpha_exact", "{:.6f}"),
        ("max S1", "C_S1_max", "{:.4f}"),
        ("S1corr(0.45)", "C_S1corr_at_0.45", "{:.4f}"),
        ("S1corr(0.3183)", "C_S1corr_at_0.3183", "{:.4f}"),
        ("S1corr(0.159)", "C_S1corr_at_0.159", "{:.4f}"),
        ("Sgen2 grid (Session-7 protocol)",
         "C_Sgen2_cap2_window_1over2pi_PROTOCOL7", "{}"),
        ("Sgen2 sup capped at 0.156 (fine grid)", "C8_Sgen2_capped_0156", "{}"),
        ("capmult8 largest OK dcap", "C_capmult8_largest_ok_dcap", "{}"),
        ("equal-depth Sgen2=1 crossing d", "C8_equal_depth_crossing_d", "{}"),
        ("max nu_joint (0,0.13]^2", "B_max_nu_joint_013", "{:.5f}"),
        ("Phi_0 floor at Delta/2", "B_Phi0_floor_at_halfDelta", "{:.4f}"),
        ("deep ratio abar(2)/abar(1)", "C_deep_ratio_y1", "{:.2f}"),
        ("deep-ratio target sqrt(2(N-2))", "C_deep_ratio_target_A_ii", "{:.2f}"),
        ("grid Parseval max err", "V_grid_parseval_maxerr", "{:.2e}"),
        ("interference identity max err", "I_identity_maxerr", "{:.2e}"),
        ("fractional attack F1-S2", "X_fractional_F1_minus_S2", "{:.6f}"),
    ]
    for label, key, fmt in rows:
        v64, v128 = res["64"].get(key), res["128"].get(key)
        f64 = fmt.format(v64) if not isinstance(v64, (tuple, list)) else str(v64)
        f128 = fmt.format(v128) if not isinstance(v128, (tuple, list)) else str(v128)
        print(f"  {label:42s}  N=64: {f64:28s} N=128: {f128}")
    print("\n==== C8 corner points (both N) ====")
    for dd in ("0.156", "0.157", "0.1575", "0.158", "0.159", "0.1591"):
        print(f"  Sgen2(d=d'={dd}):  N=64: "
              f"{res['64']['C8_Sgen2_corner_points'][dd]:.5f}   N=128: "
              f"{res['128']['C8_Sgen2_corner_points'][dd]:.5f}")
    with open(os.path.join(HERE, "n128_rerun_out.json"), "w") as fh:
        json.dump(res, fh, indent=1, default=str)
    print(f"\ntotal {time.time()-T0:.0f}s; wrote n128_rerun_out.json")


if __name__ == "__main__":
    main()
