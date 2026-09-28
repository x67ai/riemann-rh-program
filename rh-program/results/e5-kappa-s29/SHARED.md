# E5 (F2) — SHARED log (writer: Fable 5.1, Session 29). Dated blocks per section/run; machine clock via `date`.

## [Mon Sep 28 18:28:06 IST 2026] Launch
- Brief `BRIEF.md` SHA-256 015d697896191ba685ad2a743363688908f676a8622ee351a789fb3605a792e9 (verified); `PREDERIVATION.md` dfd54af3db2d43f76450b5eb5ac75cbcce3247830c2157f83821b1f3122bf49d (verified); `BARRIER-ZOO.md` 840f4362f21e87585b3120ede56e4064f16fd948bff633be5ed169636ba46cf7 (verified).
- Read: BRIEF, PREDERIVATION, `verify-orch/kappa_trivial_lb.py` + log + json; PRICING-next-unit §0, §1.1(b); `budget_floor.py` + log; BARRIER-ZOO IV.18 STATEMENT/STATUS/riders (i), (ii); C2 line 16; C2 Instruments rows "Budget-floor constant κ" and the X2 record note; ranking-read-O §1 M1; confinement-note §0.2, §1.2, §2, §6, §8.5; E1 FORMULATION line 46.
- Environment: numpy 2.0.2, scipy 1.13.1 (linprog/HiGHS), mpmath 1.3.0; no cvxpy. caffeinate running.
- Plan: §0 prior-art gate (Suzuki y-09 at the page; arXiv/web) → §1 K0 own script → conventions reproduction → §3 rung 0 → §4 primal → §5 dual LP + certification → §6 layer constant → §7 close.

## [Mon Sep 28 18:48:29 IST 2026] Conventions reproduced; closed form for a(τ) (own derivation); K0 re-derived
- `verify/conventions_check.py` → `_run.log`, `_out.json` (0.1 s). Closed form a(τ) = (1/2π)[Re{(1 − iτ)ψ(½ + iτ/2) + iτψ(1 + iτ/2)} − 1 − log π] agrees with direct quadrature of μ₀ ∗ A to ≤ 7·10⁻¹² at 16 points in [0, 1000] (≤ 4·10⁻¹⁵ away from τ₀) and with mpmath at 30 digits to ≤ 4·10⁻¹⁵. Record: a(0) = −0.653847 ✓, τ₀ = 6.31003 ✓, I₋ = 2.241523 ✓, Fejér T = 11: 0.135976 ✓ (continuous-T minimum 0.134298 at T* = 10.532). u-space form of ∫ŵa (Lemma A2) checked on the Fejér element: −1.864024 both ways (diff 10⁻¹⁰). a strictly increasing on (0, 200] on a 4·10⁵ grid (proof in NOTE §2).
- `verify/k0_rederive.py` → `_run.log`, `_out.json` (19.9 s, mpmath 40 digits, trap-free pointwise form 2Ψ − ε(2Ψ − a) ≥ 0). κ ≥ 6.3464273·10⁻¹⁹ with G = {γ₁}; G = first 10, first 30: the same (the ratio 2Ψ_G/|a| is increasing on {a < 0}, minimum at τ = 0). Orchestrator's 6.34642725583·10⁻¹⁹ vs this script's 6.34642725586·10⁻¹⁹ (relative 5·10⁻¹²; their a on a quadrature grid, mine closed form). Controls: ε*×10 fails (min −1.87·10⁻¹⁸), ε*×½ passes (min 1.04·10⁻¹⁹). Trap recorded: (1 − ε) == 1.0 in double for ε = 3.2·10⁻¹⁹.
- Verdict on K0: RE-DERIVED (NOTE §1).

## [Mon Sep 28 18:53:11 IST 2026] §0 prior-art gate, §1 K0, §2 problem statement written to NOTE.md
- Sources opened at the page: Suzuki Y-09 pp. 4–5 (Thm 1.4); arXiv full texts downloaded to `results/e5-kappa-s29/fetched/` (1708.04122v2, 1810.08843v2, 2108.09258v2, 2502.05106v1, 2404.08380v2, 2411.05095v1, 2608.24827v2, math/0110009v3), pdftotext, problem statements read at the page (NOTE §0 items 1–8). Verdict: no printed κ, no printed statement of the problem; stop line (iv) does not fire. Nearest objects: Das–Ismoilov–Ramos EP1 (shape), Zhu 2026 λ*(L) (certified-bracket method).
- Rung 0 first launch (18:38) failed: LP variables s_k unbounded above blew up on the coarse round-0 grid (overflow), primal quotient scale-drifted. Patched `kappa_pipeline.py` (S_max = 1000 on s_k; scale-pinning penalty (‖c‖² − 1)² in the primal); relaunched unbuffered at 18:53.

## [Mon Sep 28 18:56:37 IST 2026] §0 prior-art gate, §1 K0, §2 problem statement written to NOTE.md
- Sources opened at the page: Suzuki Y-09 pp. 4–5 (Thm 1.4); arXiv full texts downloaded to `results/e5-kappa-s29/fetched/` (1708.04122v2, 1810.08843v2, 2108.09258v2, 2502.05106v1, 2404.08380v2, 2411.05095v1, 2608.24827v2, math/0110009v3), pdftotext, problem statements read at the page (NOTE §0 items 1–8). Verdict: no printed κ, no printed statement of the problem; stop line (iv) does not fire. Nearest objects: Das–Ismoilov–Ramos EP1 (shape), Zhu 2026 λ*(L) (certified-bracket method).
- Rung 0 first launch (18:38) failed: LP variables s_k unbounded above blew up on the coarse round-0 grid (overflow), primal quotient scale-drifted. Patched `kappa_pipeline.py` (S_max = 1000 on s_k; scale-pinning penalty (‖c‖² − 1)² in the primal; violation tolerance 10⁻⁶ — instance A's certificate is tight everywhere so 10⁻⁷-level grid noise never clears at 10⁻⁹). Relaunched 18:53.

## [Mon Sep 28 19:03:51 IST 2026] §4 primal landed: κ ≤ 0.0009991 (a factor 136 below the Fejér 0.136)
- `verify/target_primal.py` → `_run.log`, `_out.json` (2.2 s): Fejér T = 11 → 0.135976 ✓; continuous minimum 0.134298 at T* = 10.532. Squares family w = |f|², f̂ ≥ 0 piecewise constant: best 0.0009991 at X ≥ 7.5, hx = 0.01 (f̂ a smooth bump of width 14.39; ŵ supported on |τ| ≤ 14.39, 85.5% of mass below τ₀; w/w(0) = 9·10⁻⁶ at log 2, 4·10⁻⁵ at log 3).
- `verify/target_primal_decomp.py` → `_run.log`, `_out.json` (27 s): explicit-formula check P + Z = 1.588·10⁻⁶ vs B = 1.590·10⁻⁶ (−0.1%); anatomy: γ₁ 34%, n = 4: 35%, 3: 8%, 5: 6%, 9: 4%, 13: 3%, 2: 1.5%.
- NOTE §4 written; §3 placeholder inserted (rung 0 instance A closed: [0.10000000, 0.10000144] vs exact 0.1; instances B, C running).
- Implication for §6 (to be written): C = 4(1 + 0.2415/κ) ≥ 970 even at κ = κ_ub; route (α) is dead as a competitor to the ζ-anchored 4/log t.

## [Mon Sep 28 19:22:20 IST 2026] §3 written (A, C final; B pending); general-cone primal LP stopped
- Rung 0 pass 2 (`rung0_run_pass1.log`): A bracket [0.10000000, 0.10000144] (exact 0.1); C window-LP 0.750158 > exact 0.746686 (negative control: window-only LP is not a bound), primal 0.748452. B: LP 0.1 but the crude tail bound needs T_v ≈ 1000 and a uniform LP margin; pass 3 running (Tmax = T_v = 1000, m = 2·10⁻⁵, η = 5·10⁻⁵): κ_lp = 0.0998183, cutting planes converging (~80 s/round).
- `verify/primal_cone.py` (general cone: piecewise-linear w of support ≤ 8, hats hu = 0.01, ŵ ≥ 0 by cutting planes on one period; Lemma A2 validated on a B-spline to 10⁻⁹): B/ŵ(0) = 0.0018856 stable over 6 rounds, above the squares' 0.000999 — stopped before certification, `[computed, not certified]`, informative only (compact support costs; band-limited squares are the better class).
- Target dual launched 19:22 in parallel (`verify/target_dual.py`, configs U = 3/4/6/8, hu = 0.02/0.01, Tmax = T_v = 1000, m = 2·10⁻⁵, η = 5·10⁻⁵).
