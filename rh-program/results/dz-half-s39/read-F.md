# read-F — the orchestrator's read at the line of `results/dz-half-s39/NOTE.md` (Fable 5.1, Session 40, written 11:27 IST 2026-10-01)

NOTE read: SHA-256 b5ff31f10e4eb33e… (407 lines): §0, §1, §2 whole at the line (every lemma and both proofs); §3–§4 (the variance tables and the 10⁸ simulation) and §5 (prior art) left to the Opus reader's independent re-run and page checks (`read-O.md`, in flight). Pairs are applied only after reconciliation.

**VERDICT LINE: AGREES on the close T. Theorem 1 (the one-scale lower bound) re-derived step by step — Lemma 2.1 (identity), Lemma 2.2 (variance), Lemma 2.3 (remainder), the Berry–Esseen step and, in particular, the passage from one-scale anti-concentration to the almost-sure statement, which is valid as written and needs no independence across scales. Proposition 2.4 (the second proof) re-derived. Corollary 2 follows given Diamond–Zhang's (i)–(iv) as quoted (the quotations are the Opus reader's page check). No FIX-FIRST from this side.**

## 1. Re-derived at the line
- **Lemma 2.1** ✓: two primes of the block (x/2, x] multiply beyond x (x ≥ 4), so a g-integer ≤ x holds at most one block prime q, to the first power, and its cofactor m′ ≤ x/q < 2 is built from g-primes < 2; N_{Q∖{q}}(y) = N_Q(y) − N_Q(y/q) gives ρ^c = ρe^{−S}; (c) is algebra.
- **Lemma 2.2** ✓: c_k = φ(x/v_k) + O(κ/x) with φ(y) = n₀(y) − κy piecewise linear of slope −κ on at most N₀ + 1 pieces; |φ| ≥ κ/(4(N₀ + 1)) off a set of measure ≤ ½; (H1) turns the measure into prime mass ≥ c_*x/(8 log x).
- **Lemma 2.3** ✓ (Chebyshev on {|D| > 1} and on {D² > 2u/(eκx)}).
- **The almost-sure step** ✓ — the point the brief asked the readers to press: with A_{x₀} = {|E(n)| ≤ λs_n for all integers n ≥ x₀}, P(A_{x₀}) ≤ inf_{n≥x₀}P(|E(n)| ≤ λs_n) ≤ h(λ); the events increase to {eventually |E(n)| ≤ λs_n} ⊃ {lim sup |E(n)|/s_n < λ}, so that event has probability ≤ h(λ) for every λ, and h(λ) → 0. A uniform single-scale bound suffices; no 0–1 law, no decoupling of scales. The conditional bound is legitimate because N₀, κ, Y and x₁(N₀) are G-measurable and Φ_x is set to 1 below x₁.
- **Prop. 2.4** ✓: W(σ) = Σ(X_k − p_k)v_k^{−σ} converges a.s. for all σ > ½ at once (convergence on a sequence σ_j ↓ ½ and Abel summation); V(σ) → ∞ and bounded summands give the CLT, so P(lim sup_{σ→½⁺}W = +∞) ≥ ½, a tail event, hence 1; −F₁ ≥ 0 on the real axis and |ζ_C| ≥ c₀ there; Landau's step is the boundedness of ζ_B on [½, ½ + δ] under E = O(x^τ), τ < ½.
- **Lemma 2.5, Cor. 2.6** ✓.
- Constant spot-check: c = 2c₁/(1 − e⁻⁴) with c₁ = 0.410616 is 0.8366 < 1, so (H1)'s lower constant for f_C is positive.

## 2. Independent computation
The decisive object here is the proof; the finite rung (§4) is evidence. Its independent re-run (own code, X = 10⁷, several seeds) is the Opus reader's task (d) — an independent model with independent code; the orchestrator did not duplicate it.

## 3. Minor (held for the one-pass application after read-O)
- **m1** — §2, proof of Theorem 1, line "Berry–Esseen … [recalled, unverified: Esseen 1945, any absolute constant C₀]": cite a page (e.g. Petrov, *Sums of Independent Random Variables*, Ch. V, Thm 3; or Feller II, XVI.5) once the reader has one at the page; the proof needs only the existence of an absolute constant.
- **m2** — §0 "(a proof, every step written; single writer — the standing dual read is still owed)" → replace by the dual-read line at the close.

## 4. Close
T, as written: almost every realization of Diamond–Zhang's Theorem 17.14 system is a [1, ½]-system (on Conjecture U's boundary; consistent with U), and Theorem 17.11's is a [½, ½]-system.
