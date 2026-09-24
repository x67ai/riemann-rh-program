## 2026-09-24 18:20 IST — Session 24 item 2(c), the Siegel-zero scout (Fable 5.1): DONE, report on disk

- Deliverable: `results/c2-siegel/siegel-world-scout.md` §0–§8 + §F. Scripts/logs: `verify/siegel_setup.py`, `verify/planted_real_zero.py`, `verify/dh_repulsion.py` (+ `_run.log`, `_out.json`).
- Answers: (1) R1 says nothing at t = 0 (Ψ_K(0) = 1.2·10⁻³ at D = −20; (D_{0,y}) fails at every δ). (2) The exceptional-zero clause IS the cone sector's reach at t = 0, by the pole cap 2(ŵ∗μ_y)(0) ≤ 2ŵ(0): a single real zero is uncertifiable at any depth for |D| ≥ D₁ = 500.94 (a_K ≥ 0); at D = −20 the cone certifies every δ ≤ 0.1 (a_K(0) = −0.51); a double real zero is excluded within δ·log|D| → 0.343. (3) Deuring–Heilbronn from (0.3_K) alone is a bounded constant-factor repulsion (saturates as δ₀ → 0), not the log(1/δ₀) gain.
- Stop conditions: (a) identity residual 2.9·10⁻¹² — not fired; (b) Heath-Brown 1992 prints Principles 1–2 (p. 266) — not fired.
- Proposed (not inserted): Group-I entry "I.8 The Siegel-zero world" (§6); IV.18 rider (§6); C2 Untried exit line + Instruments row (§7); one FETCH row (Heath-Brown 1983, §F).
- V.4: double real zero fires at every |D| tested; single real zero at |D| ≥ 501 silent at every δ.
- Not committed (brief).

## 2026-09-24 18:52 IST — Session 24 item 2(c), independent check (Opus 5): DONE, `check-O.md` on disk

- Deliverable: `results/c2-siegel/check-O.md` (SHA-256 b11f970d6dea60dae1a73b6b56cad59d8c43ca21cce5caa852adc948adfe53ec). Own scripts and logs: `verify-O/o1_identity_thresholds.py`, `o2_planted_margins.py`, `o3_partB_tail.py` (+ `_run.log`, `_out.json`; hashes in `verify-O/hashes.txt`).
- Verdicts: item 1 (identity) CLOSES: own 58 L(χ₋₂₀) zeros agree to 5·10⁻¹⁰, residual ≤ 2.7·10⁻¹² on two new elements, the scout's w_A reproduced to every digit. Item 2 (Lemma C, thresholds) CLOSES: D₁ = 16π²e^{2γ} = 500.937, D₀ = 64π²e^{2γ} (closed forms, unchanged); a_K = (1/π)[Re ψ(½+is/2) − log π] + log|D|/2π, so monotonicity is proved; D₁ is sharp; D > 0 needs D₁⁺ = 3701.45. Items 3–7 FIX-FIRST.
- Moved: closing |D| at δ = 0.01 is ≥ 256 (was ≈ 230). The 0.343 double-zero constant belongs to the dlVP element only (e^{−a|u|}: 0.686; Gaussian: 1.003). Part B Poisson margins were too high by 0.13–0.14 (archimedean integral truncated at |s| ≤ 20; no sign changes). Two stray constants: 2.830 → 6.830 and 0.32 → 0.334. The §3 classical column is in the wrong units.
- Refuted: "R1 clause 2 is vacuous at t = 0 on every rung". The identity gives Z_K(w) ≥ w(0)log|D| − C, and the ŵ-mean zero density is 2.06 at |D| ≈ 10¹². Scope the claim to small conductor.
- Novelty: the pole cap has a printed antecedent on disk, GHL 1994 appendix Lemma p. 178 (pole order m ⇒ at most m real zeros within c/log M). The cone-wide form and the sharp D₁ were not found in the corpus. No web search.
- I.8: YES with amendments A1 (parity/D₁ closed form), A3 (KILLS: single simple zero; Σ_∞ only; c-clause), A4 (STATUS: standing order 4 + novelty label), A5 (test script). Amended text in check-O.md item 5(d). Rider A6 and Instruments row A7 are rescoped there.
- Not committed (brief).
