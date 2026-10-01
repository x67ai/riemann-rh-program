# read-F — the orchestrator's read at the line of `results/lemmaG-s39/NOTE.md` (Fable 5.1, Session 40, written 11:25 IST 2026-10-01)

NOTE read: SHA-256 37622108812a9942… (401 lines): §0, §1, §2, §3, §6 whole at the line; §4 (computation) and §5 (prior art) left to the Opus reader's independent re-run and page checks (`read-O.md`, in flight). Pairs are applied only after reconciliation.

**VERDICT LINE: AGREES on the close "G with T-parts and a rung-1 counterexample". Theorem R1, Theorem 2.1, Corollary 2.2, Proposition 2.3, T2, T3, T4, T5 re-derived step by step; Theorem F and Cor. F.1 checked as a modification of Theorem Z (structure only — the Opus reader re-derives Z4–Z5 with log C); the §6 statement about 𝒞_self is true by definition plus Prop. 2.3 and Theorem F. No FIX-FIRST from this side. Independent computation: Theorem R1 brute-forced by my own code in three cases.**

## 1. Re-derived at the line
- **Theorem R1** ✓: the cyclotomic identity 1 − au = Π_N(1 − u^N)^{M(a,N)} (compare logarithms: Σ_{N|n} N·M(a, N) = aⁿ); R-free generating function (1 − au)/(1 − qu), so N_P(n) = qⁿ − a·q^{n−1}, ρ_R = 1 − a/q, E ≡ 0; M(a, N) ≤ M(q, N) for a < q so the deletion exists; π_R(qⁿ) ≍ aⁿ/n. By hand at q = 3, a = 2, n = 1, 2 (1 and 3 R-free polynomials).
- **INDEPENDENT COMPUTATION** (`verify-F/necklace_F.py`, own enumeration of monic polynomials, irreducibles by marking products, R-free counts by multiplicative closure): q = 3, a = 2, degrees 1–7: 1, 3, 9, 27, 81, 243, 729 = qⁿ − aq^{n−1}; q = 5, a = 2, degrees 1–4: 3, 15, 75, 375; q = 5, a = 3: 2, 10, 50, 250 — all equal (the deleted set chosen differently from the writer's: the LAST M(a, N) of each degree — the theorem does not depend on the choice).
- **Theorem 2.1** ✓: (a) D_R = ζ_P/ζ meromorphic on σ > β₂, poles only at zeros of ζ with order ≤ ord ζ, no zeros or poles right of α_R; (b) P_R = −Σ μ(m)m⁻¹L(ms) by Möbius inversion of L = −Σ_k P_R(ks)/k, the tail m > (α_R + 2)/σ uniformly small, so each germ is −κ(s₀)log(s − s₀) + analytic with κ = Σ μ(m)n(ms₀)/m; (c) the integrality cases. **Cor. 2.2** ✓ (contrapositive). **Prop. 2.3** ✓ (RH puts ζ's zeros on σ = ½ > α_R, where n = 0).
- **T2** ✓: D_R = C(s)·Π_{p<p₀}(1 − p^{−ks})⁻¹·ζ(ks)⁻¹ with C absolutely convergent and zero-free on σ > 1/k − 1 + θ′ (< 1/(2k) because θ′ < 1 − 1/(2k)); the pole at ρ₁/k is forbidden right of β₂ unless ζ(ρ₁/k) = 0, impossible at height γ₁/k < 14.13. Inputs used: Ingham's gap exponent 5/8 (any exponent below 1 − 1/(2k) serves), the location and simplicity of ρ₁ — both standard, verified numerically by the writer; neither is RH.
- **T3** ✓ (a simple pole of P_R at 1/k, forbidden by 2.2(ii); distinctness needs kθ′ < k − 1, true for k ≥ 3). **T4** ✓ (T is eventually increasing since x^{α−1}/log x ≫ x^{α/2−1}, so the greedy set tracks it within 2; the planted poles s_j are dense on σ = α/2; one pole already suffices). **T5** ✓ (P_R = −Φ(s)log(s − ½) + analytic near ½ with Φ(½) = 2(√2 − 1); the germ is not κ·log + analytic for any κ because Φ is not constant — forbidden at Re s₀ = α_R).
- §1.3 ✓: at rung 1 −log D_R has nonnegative coefficients and D_R is t-periodic, so the real singularity at s = α_R recurs at every height 2πk/log q — Theorem Z's hypothesis is void there; (G₁) follows.

## 2. Minor (held for the one-pass application after read-O)
- **m1** — §3 header: the three "recalled" gap inputs carry no RH; say so in one clause where T2 is called unconditional (the proof uses only: a prime in [p^k, p^k + p^{kθ′}] for some θ′ < 1 − 1/(2k), and ζ(ρ₁/k) ≠ 0).
- **m2** — §0 item (1) "E ≡ 0 … β = −∞": add that the statement is degree-wise (the program's rung-1 convention), as §1.2 does.

## 3. Close
G with T-parts, as written; the rung-1 counterexample is a Group-I control candidate for the zoo stream (after read-O).
