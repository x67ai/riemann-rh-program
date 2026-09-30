# SHARED — seed N4 `tournament` (novel-approach wave, Session 36)

Agent: Opus 5.5 (subagent), 2026-09-30. Charter: `results/novel-wave-s36/WAVE-CHARTER.md` (read in full).

## 2026-09-30 block 1 — reading done, folder created

- Read: charter (full); STATUS.md lines 72–103 (hard constraints; S1–S5); BARRIER-ZOO.md §0 and the STATEMENT lines of I.1–I.8, II.1–II.5, III.1–III.21, IV.1–IV.19, V.4–V.5 (riders not read); `results/d4-infty-s36/BRIEF.md` §2 (Proposition N = the degree clause; Theorem S; Proposition B = regrading of the primes as a formal curve over F_2; Proposition A; Proposition C = the distributional cell is Weil's criterion with multiplier 1).
- Tools located: `results/ccm-dh-test/dh.py` (f_dh, xi_dh, find_zero; off-line zero near 0.808517 + 85.699348i); arXiv search pattern `results/beta-shapes-s35/verify/arxiv_search.sh`.
- Next: generate the 30+ candidate list (NOTE §1), verify the F_{a,q} control first (charter rule 2 says "verify it before use").

## 2026-09-30 block 2 — F_{a,q} control verified (`verify/faq_control.py` → `faq_control.log`)

- FE: q^s·π^{−s/2}Γ(s/2)ζ(s)P(s), P(s) = 1 + a q^{−s} + q^{1−2s}, is symmetric under s → 1−s (derived: P(1−s) = q^{2s−1}P(s); rel. err ≤ 1.2e-30 at 3 points × 4 parameter pairs).
- Zeros of P: u = q^{−s} real negative, u₁u₂ = 1/q, so σ₁ + σ₂ = 1, σ ≠ ½ whenever a > 2√q. Examples: (a,q) = (3,2): σ = 1 and 0 (ON the 1-line, a Re s = 1 zero!); (5,5): σ = 0.79899; (2.9,2): 0.82388; (4.5,5): 0.56932. Height Im s = π/log q (and its translates by 2π/log q): 4.5324 for q = 2, 1.9520 for q = 5 — the control's off-line zeros are LOW and infinitely many (periodic in t), so every test sees them at height ≤ 5.
- Where it breaks the axioms: Dirichlet coefficients c_n = 1 + a[q|n] + q[q²|n] ≥ 0 and a product over primes exist, but the local factor at q is (1 + a u + q u²)/(1 − u) = (1−αu)(1−βu)/(1−u) with α,β < 0 real, |β| > √q (Ramanujan fails at q) and Λ_F(q²) = log q·(1 − α² − β²) < 0 (e.g. −4 log 2 at (3,2)): Λ_F ≥ 0 fails; the local factor is a POLYNOMIAL numerator, not an inverse polynomial. It passes any test that uses only c_n ≥ 0, FE, and a product over primes.

## 2026-09-30 block 3 — replacement agent (Opus 5.5) resumes; NOTE.md created; batch 1 (T1–T5)

- Predecessor died emitting > 128k output in one response. Replacement rule: ≤ 6 kB per write; NOTE.md built in appends.
- Re-read: charter (full), SHARED blocks 1–2, `verify/faq_control.log`, zoo §0 + STATEMENT lines (I, III, IV, V), d4-infty BRIEF §2, STATUS 72–103, sibling §0s (N1 K, N2 K, N3 K).
- NOTE.md: header + §0 placeholder + §1 conventions + batch 1: T1 interlacing families (DEAD, I.5 + output type), T2 Gårding (DEAD, N1 Thm K), T3 Borcea–Brändén multiplier (DEAD, local factor zeros at Re s ∈ {0,1}), T4 Schoenberg PF∞ (EQUIV of LP), T5 Hurwitz limit of Hasse-compliant factors/curves (DEAD, derived: every factor has a zero at |t| ≤ π/log 2 = 4.53).
- Next: batches 2–7 (T6–T33), then three deep dives with `verify/` computations.

## 2026-09-30 block 4 — batch 2 (T6–T10) appended

- T6 ID of tilted kernel: DEAD with a self-contained proof (ID + all exponential moments ⇒ entire zero-free ch.f.; n | m for all n at any zero). T7 info functionals on dBN flow: DEAD (III.6, forward-only propagation). T8 free probability: DEAD / residue EQUIV (Lagarias Pick). T9 OT/electrostatics: DEAD (every zero set is critical for V′ = f″/f′; no f-independent field). T10 zeta distribution in the strip: EQUIV (Lévy mass infinite for σ ≤ 1).

## 2026-09-30 block 5 — batch 3 (T11–T15) appended

- T11 tropical: DEAD (III.10). T12 hyperfinite: EQUIV (+III.18). T13 proof complexity: DEAD (no generator). T14 Kronecker flow: DEAD (III.1). T15 symbolic dynamics: DEAD, derived finite-rank lemma (log p Q-independent) + countable-alphabet zeta = 1/(1 − P(s)).

## 2026-09-30 block 6 — batch 4 (T16–T20) appended

- T16 quantum graphs: DEAD (N1 Thm K; Weyl). T17 Mayer transfer operator: DEAD (III.19/III.3; domination reaches σ > 1 only). T18 passivity/KYP: DEAD (I.2; III.5). T19 truncated-Eisenstein Gram positivity: DEAD (residue norm |r|²T^{1−β}/(1−β) > 0 at any depth). T20 conic duality: EQUIV (Weil).

## 2026-09-30 block 7 — batch 5 (T21–T25) appended

- T21 Deligne squeeze on Prop-B regrading: DEAD (regraded "RH" free for any positive weights; Theorem S; IV.20). T22 exact ζ squeeze D_k(s) = ∫(ψ−x)^{2k}x^{−s−1}dx: EQUIV (mean-square PNT error), carried to deep dive 3. T23 Rankin/Landau: DEAD (no amplification, derived). T24 Stepanov: DEAD (III.4, III.20(A)). T25 condensed cohomology: DEAD (III.14).

## 2026-09-30 block 8 — batch 6 (T26–T30) appended

- T26 Lorentzian: DEAD (III.16). T27 Krein–Langer Pick rigidity on Re s > 1: EQUIV (Weil multiplier 1; IV.8(b) for counting), carried to deep dive 2. T28 one-sided majorants: DEAD (Haselgrove, Odlyzko–te Riele, Montgomery). T29 GORZ hierarchy: DEAD. T30 derivative descent: EQUIV per level.
