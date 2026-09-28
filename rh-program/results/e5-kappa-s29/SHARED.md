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

## [Mon Sep 28 19:31:30 IST 2026] Primal refined; dual runs in flight; §6 written
- `verify/target_primal_fine.py` (2.3 s): hx = 0.005, n = 3000 → κ_ub = 0.00099853 (from 0.0009991; element in `target_primal_fine_best.json`). NOTE §4/§6 numbers updated (C(κ_ub) = 972, t > e^{3052}).
- Plain dual (`target_dual.py`): U = 3, hu = 0.02: κ_lp = −0.1094 (d = 2.1094; active constraints all beyond γ₁: 17.6, 19.4, 21.3, … 47.8; verification of the negative point moot); U = 4, hu = 0.01: round 0 d = 2.0388 (κ_lp = −0.039). U = 6, 8 (process A) and U = 12, 16, 24 (process B) running.
- Mixed dual (Theorem D′, `target_dual_mixed.py`, K0's convex combination + grid correction, first 200 zeros): U = 4 running.
- Rung 0 B: LP converged (κ_lp = 0.0998183); the adaptive certification over the tight region [0, 60] is refining (running since 19:20).

## [Mon Sep 28 19:46:23 IST 2026] Verifier memory defect fixed; dual re-formulated at fixed ε; relaunches
- Defect: `verify_dual` evaluated σ̂ on a whole refinement level in one dense matrix (10⁷ cells × 301 columns → 26 GB, swapping; rung 0 B's certification stalled 25 min). Fixed: `sigmahat_eval` chunked (20 000 rows). Rung 0 B relaunched alone (`rung0B.py`, saves `rung0B_s.npy`).
- Plain dual trend (`target_dual_run.log`): d − 2 = 0.1094 (U = 3, hu = 0.02), 0.0389 (U = 4, hu = 0.01) — no positive certificate; the LP's positive nodes sit at u = 0.68–0.69, 1.05–1.06, 1.21, 1.54, 1.64–1.65, 1.82, 1.98–1.99 (log 2, log 3, log 5, log 7 = 0.693, 1.099, 1.609, 1.946: the LP rediscovers the prime comb). U = 12/16 at hu = 0.02 timed out (600 s) — dropped. U = 6, 8 still running (process A).
- Mixed dual with free ε and a uniform margin 2·10⁻⁵ (`target_dual_mixed.py`, U = 4): ε = 2.2·10⁻⁵, D = 7.8·10⁻⁵, κ_lp = −3.4·10⁻⁵ — the margin is not meaningful when ε itself is 10⁻⁵ (K0's own point is infeasible under it). Killed. Re-formulated (`target_dual_eps.py`): at fixed ε the mixed class is the plain LP for a_ε := a + 2((1−ε)/ε)Ψ_G, κ ≥ ε·κ_plain(a_ε); margins live in the scaled problem; per-cell Lipschitz bound for the Ψ_G part. Launched: U = 6 (ε = 10⁻², 10⁻³, 10⁻⁴, 10⁻⁵) and U = 4 (10⁻³ … 10⁻⁶).

## [Mon Sep 28 20:13:28 IST 2026] Rung 0 PASSES (B certified 0.099768, gap 0.23%); mixed dual certifies κ ≥ 6.2·10⁻⁶ at U = 6; larger U launched
- `rung0B.py` (1394 s): LP 0.0998183, certified 0.0997683 (η = 5·10⁻⁵; 2.3·10⁷ cells, depth 12); bracket [0.099768, 0.100001] vs known [0.1, 0.1 + δ]. NOTE §3 completed.
- `target_dual_eps.py` U = 6, hu = 0.01: ε = 10⁻²: κ̃ = −4·10⁻⁵ (no cert); ε = 10⁻³: κ̃ = 0.006247, CERTIFIED κ ≥ 6.227·10⁻⁶ (η = 2·10⁻⁵, 7.1·10⁶ cells, depth 17); ε = 10⁻⁴: κ̃ = 0.015495, CERTIFIED 1.548·10⁻⁶; ε = 10⁻⁵: κ̃ = 0.030219 (verification running). U = 8, ε = 10⁻³: κ̃ = 0.010123 (κ_lp = 1.01·10⁻⁵, verifying); U = 12 (hu 0.02), ε = 10⁻³: κ̃ = 0.020645 (κ_lp = 2.06·10⁻⁵). Plain class U = 6 (small grid): d = 2.004572, no cert; U = 8, 12 running.
- Launched: U = 16 (hu 0.02; ε = 10⁻³, 2·10⁻³), U = 24 (hu 0.04; same), U = 32 (hu 0.04; 10⁻³). NOTE §5 table started.

## [Mon Sep 28 20:49:45 IST 2026] Certified bracket landed; NOTE.md finalized (re-patchable); two margin-10⁻⁴ reruns in flight
- ε-scan at U = 8, hu = 0.01 (`target_dual_eps_U8*_run.log`, `_out.json`): ε = 10⁻³ certified 1.0103·10⁻⁵; ε = 2·10⁻³ certified **1.5940·10⁻⁵** (η = 2·10⁻⁵, 3.55·10⁷ cells, depth 19) — the best; ε = 3·10⁻³: LP 2.1·10⁻⁵, certified only 1.58·10⁻⁶ (needed η = 6.4·10⁻³); ε = 5·10⁻³: LP 2.9·10⁻⁵, not certified (dips ≤ 4.6·10⁻⁶ at every η ≤ 1.6·10⁻³). U = 16 (hu 0.02), ε = 10⁻³: LP κ̃ = 0.010835 (κ_lp = 1.08·10⁻⁵), uncertified; U = 24 (hu 0.04): certified 3.95·10⁻⁶ (η = 6.4·10⁻³). Plain class: d − 2 = 0.00038 at U = 8.
- **Bracket: κ ∈ [1.594·10⁻⁵, 9.985·10⁻⁴], both ends certified; gap factor 63.** C(κ_lb) = 6.06·10⁴. NOTE §5 table/bracket, §6, §7 and the one-line result written by `verify/finalize_note.py` (`finalize_note_out.json`).
- Reruns launched (margin 10⁻⁴ in the scaled LP): U = 8, ε = 5·10⁻³ and 3·10⁻³ — if either certifies above 1.594·10⁻⁵ the three numbers (κ_lb, gap, C) are re-patched.

## [Mon Sep 28 21:14:33 IST 2026] Re-patched: κ_lb = 2.8186·10⁻⁵ (U = 8, hu = 0.01, ε = 5·10⁻³, LP margin 10⁻⁴, η = 2·10⁻⁵; 1.85·10⁷ cells, depth 15); gap factor 35.4; C(κ_lb) = 3.43·10⁴
- The margin-10⁻⁴ reruns certified: ε = 3·10⁻³ → 2.0319·10⁻⁵; ε = 5·10⁻³ → **2.8186·10⁻⁵** (`target_dual_eps_U8_eps5e-3_m1e-4_run.log`, `_out.json`, certificate `target_dual_eps_s_U8_hu0.01_eps0.005.npy`). `verify/repatch_note.py` rewrote the §5 table (with an LP-margin column), the bracket, §6, §7 and the one-line result (`finalize_note_out.json` updated). NOTE.md SHA-256 after the re-patch: 5b41e4fc1129cc1dad1e78fa9ce30ac6205847888a5b65dd33a1aa5adbe107cb.
- Last scan launched: U = 8, margin 10⁻⁴, ε = 7·10⁻³ and 10⁻² (≈ 20 min each). If either certifies higher, `repatch_note.py` is run again and the hashes below change; otherwise the bracket stands.

## [Mon Sep 28 21:30:43 IST 2026] Re-patched again: κ_lb = 4.2003·10⁻⁵ (U = 8, hu = 0.01, ε = 10⁻², margin 10⁻⁴, η = 2·10⁻⁵); gap 23.8; C(κ_lb) = 2.30·10⁴; scan continues upward in ε
- ε = 7·10⁻³ certified 3.4677·10⁻⁵; ε = 10⁻² certified 4.2003·10⁻⁵ (`target_dual_eps_U8_eps1e-2_m1e-4_run.log`, `_out.json`, `target_dual_eps_s_U8_hu0.01_eps0.01.npy`). Certified κ still rising with ε at 10⁻² → launched ε = 2, 3, 5·10⁻² (U = 8, margin 10⁻⁴). NOTE.md re-patched (e5e572b4… → after manual fixes of three stale sentences, hash below at the close).

## [Mon Sep 28 21:51:39 IST 2026] CLOSE — final bracket κ ∈ [6.589·10⁻⁵, 9.985·10⁻⁴] (gap factor 15.2); C(κ_lb) = 1.47·10⁴; all runs finished
- Final ε-scan (U = 8, hu = 0.01, margin 10⁻⁴, η = 2·10⁻⁵): ε = 2·10⁻²: certified 5.6485·10⁻⁵ (see `target_dual_eps_U8_eps2e-2_m1e-4_run.log`); ε = 3·10⁻²: κ̃ = 0.002216, **certified 6.5890·10⁻⁵** (`target_dual_eps_U8_eps3e-2_m1e-4_run.log`, `_out.json`, certificate `target_dual_eps_s_U8_hu0.01_eps0.03.npy`); ε = 5·10⁻²: LP 7.9·10⁻⁵, NOT certified. `repatch_note.py` applied; three stale sentences fixed by hand. No process running.
- Stop lines: (i) no, (ii) no, (iii) YES — the certified bound stalls at 6.6·10⁻⁵ < 10⁻³ at the largest grid the slot allowed (U = 8, hu = 0.01; larger U only at coarser hu, whose certificates fail verification); the bracket and gap are the result. (iv) no.
- Files: NOTE.md (194 lines), SHARED.md, verify/ (15 scripts, 30+ logs, JSON, .npy certificates), fetched/ (8 arXiv texts). Nothing outside results/e5-kappa-s29/ touched; nothing committed.
- Final hashes (after this block is written SHARED's hash changes; the reader hashes both files at launch):
  NOTE.md SHA-256 61aa86bd55f264abe142f454aa1bd899ef91a85150bcac6cf755362d0dd312b5
