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

## 2026-09-30 block 9 — batch 7 (T31–T35) appended; table complete (35 rows)

- T31 Λ² squares: DEAD (III.4). T32 modular bootstrap: DEAD (I.1 Ep). T33 Lagarias–Suzuki modulus continuity: DEAD (I.1 Ep). T34 det₂: EQUIV. T35 Beurling–Deny Weil symbol: EQUIV (J_p ≥ 0 from Λ ≥ 0 but infinite mass).
- Tally: 35 rows; DEAD 24, EQUIV 11, OPEN 0 at brief time.
- Deep dives chosen (the three whose brief-time verdict leaves a computable question): DD1 Λ-positivity of Epstein zetas (decides whether the positive-Λ + FE axiom set used by T6/T10/T18/T35 has a computed RH-false member); DD2 Krein–Langer Pick instrument (T27) on DH vs ζ, χ₄; DD3 Landau squeeze D_k (T22) on ζ vs F_{2.9,2}.

## 2026-09-30 block 10 — DD1 computed (`verify/dd1_lambda_sign.{py,log}`, `verify/dd1_rung1_virtual.{py,log}`)

- Tally correction to block 9: DEAD 26, EQUIV 9, OPEN 0 (35 rows).
- Λ_F(n) ≥ 0 test, n ≤ 2·10^5 (recursion a(n)log n = Σ_{d|n}Λ(d)a(n/d)): Euler-product controls x²+y², x²+xy+2y², ζ_{Q(√−5)}: 0 negatives, off-prime-power |Λ|/log n ≤ 4e-14. Epstein h=2 (x²+5y²): first negative n = 36, Λ(36) = −2 log 36 (hand-verified: 6 log 6 − (3 log 4 + 4 log 6 + 3 log 9) = −4 log 6); 2604 negatives. x²+6y²: 3279; x²+xy+6y² (h=3): 6101; x²+14y² (h=4): 2508. DH: first negative n = 3; F_{2.9,2}: negatives exactly at 4^k.
- So the axiom set 𝒫 = {FE + Λ ≥ 0 at every n} excludes all three computed RH-false controls (DH, F, Ep).
- Rung 1: Z(u) = (1 − 5u + 5u²)/((1−u)(1−5u)) over F_5 has FE, N_N = 1 + 5^N − L_N ≥ 1 integral (1, 11, 76, 451, …), closed-point counts b_d nonnegative integers for d ≤ 40 (1, 5, 25, 110, 500, …), zeros at σ = 0.79899 / 0.20101: an RH-false "virtual curve" with Euler product, Λ ≥ 0, FE, rationality. The rung-1 analog of 𝒫 does NOT imply RH.
- Next: DD2 (Krein–Langer Pick kernel on DH vs ζ).

## 2026-09-30 block 11 — DD2 computed (`verify/dd2_pick_kernel.{py,log}`, `verify/dd2_visibility.{py,log}`)

- Carathéodory/Pick kernel K(s,w) = (F(s) + conj F(w))/(s + w̄ − 1), F = ξ′/ξ, n points on |s − (1.5 + iT)| = r (inside Re s > 1). DH at T = 85.699 (its zero's height): exactly one negative eigenvalue, −0.051 (n = 12), −0.102 (n = 24), −0.153 (n = 36) vs max 38–115. ζ at the same four centers, n ≤ 36: no eigenvalue below −1e-55·max (dps 70). Krein–Langer count (one negative square per off-line pair) confirmed.
- Visibility law (dps 90, n = 24): log10(−min/max) for height offset D = 0, 1, 2.5, 5, 7.5, 10: r = 0.3: −2.9, −4.7, −10.6, −24.4, −40.5, −58.3; r = 0.45: −1.9, −3.6, −8.8, −20.9, −35.2, −51.2. About 6–7 digits (r = 0.3) or 5–6 digits (r = 0.45) per unit of height offset, slightly super-linear; at DH's zero density ≈ 0.67/unit this is ≈ 10 digits per intervening on-line zero.
- Verdict: EQUIV stands; as an instrument the negative square is global in principle (Krein–Langer) but exponentially local in practice (IV.9): a disk sees an off-line zero only within ≈ 10 units of height at 60–90 digits, so scanning to height H costs ≥ H/10 disks — no gain over direct verification.

## 2026-09-30 block 12 — DD3 computed (`verify/dd3_landau_squeeze.{py,log}`, X = 10^7, 6.6 s)

- D_1^X(σ) = ∫_1^X (ψ_F(x) − x·[pole])² x^{−σ−1}dx; growth per decade of log10 D (last decade 10^6→10^7): ζ: σ=0.9 0.045, σ=1.0 0.014 (constant: log growth, abscissa 1), σ ≥ 1.3 → 0. F_{2.9,2}: σ=1.0 0.664 (theory 2Θ_F − σ = 0.648), 1.3 0.349 (0.348), 1.5 0.143 (0.148), 1.7 0.025 → 0: abscissa 1.648 read correctly from X = 10^4. DH: σ=1.0 0.22 → 0.35 → 0.52 (theory 0.617), σ=1.3 0.10 (0.317), σ=1.5 0.012 (0.117): not yet asymptotic — the off-line term (amplitude x^{0.8085}/85.7) dominates only for X ≳ 85.7^{1/0.3085} ≈ 10^{6.3} (IV.9 visibility: X ≳ |ρ|^{1/δ}).
- Rung 1: Σ_N (N_N − 1 − q^N)^{2k} q^{−Ns} is rational with nonnegative coefficients for the RH-false virtual curve (5,5) too; positivity + rationality + FE give only "abscissa = largest pole". Deligne's real input is the weight bound from the Lefschetz-pencil family (monodromy + induction), absent for a single virtual curve and absent over Z.
