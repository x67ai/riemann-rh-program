# read-F (PARTIAL) — the orchestrator's read of `results/free-greedy-s40/theory/NOTE.md` (Fable 5.1, Session 40, written 12:19 IST 2026-10-01)

NOTE at SHA-256 caeb71db64b81ea3…. **Only Theorem 1.6 is read at the line here (from the unit's report and the definitions); the full read of §1–§6 and an Opus `read-O.md` are owed (SESSION 41 QUEUE).**

## Theorem 1.6 — re-derived, CORRECT
Statement: a discrete Beurling system with R(u) := N(u) − ρu ≥ r₀ > 0 for all u ≥ 1 and R(u) = O(u^θ), θ < r₀/(r₀ + ρ), has a real zero of ζ_P in [r₀/(r₀ + ρ), 1); hence α ≥ r₀/(r₀ + ρ).
Re-derivation. For σ > 1, ζ_P(σ) = σ∫₁^∞ N(u)u^{−σ−1}du = ρσ/(σ − 1) + σ∫₁^∞ R(u)u^{−σ−1}du, and the right side is analytic on σ > θ away from 1 (R = O(u^θ)), so it is the continuation. For θ < σ < 1: σ∫₁^∞ R(u)u^{−σ−1}du ≥ σ·r₀·∫₁^∞ u^{−σ−1}du = r₀, hence ζ_P(σ) ≥ r₀ − ρσ/(1 − σ), which is > 0 exactly when σ < r₀/(r₀ + ρ). The hypothesis θ < r₀/(r₀ + ρ) puts such σ inside the domain. As σ → 1⁻ the R-integral stays bounded (≤ C/(σ − θ)) while −ρσ/(1 − σ) → −∞. ζ_P is real and continuous on (θ, 1): a zero σ* exists, and σ* ≥ r₀/(r₀ + ρ) because ζ_P > 0 to the left of that point. A zero at σ* makes ζ′_P/ζ_P singular there, so ψ_P(x) − x ≠ O(x^σ) for σ < σ*: α ≥ σ*. ∎ (Elementary; uses only N(u) ≥ ρu + r₀, the O-bound, and discreteness nowhere.)
For S8 (threshold ½): E = N − T ≥ −½ with T(u) = ρu + (1 − ρ), so r₀ = ½ − ρ (positive iff ρ < ½) and the zero is ≥ (½ − ρ)/½ = 1 − 2ρ, which exceeds ½ iff ρ < ¼. **Consequence: for ρ < ¼, Conjecture U (α ≤ max{½, 2β}) fails for S8(ρ) as soon as N(x) − ρx = O(x^θ) for some θ < ½ − ρ** — no zero-finding, no Rouché margin, no certificate. With a rule that never lets N fall below T by more than τ, r₀ = 1 − ρ − τ and the zero is ≥ (1 − ρ − τ)/(1 − τ) — toward the template's zero 1 − ρ as τ → 0.
Remark (the orchestrator's): the statement does not need the system to be discrete — the continuous template dN = δ₁ + ρdx has R ≡ 1 − ρ and its zero is exactly 1 − ρ = r₀/(r₀ + ρ): the bound is sharp. What discreteness adds is that Conjecture U is about discrete systems; for them the open point is ONLY the O-bound on N.

## Not read here
Lemmas 1.0–1.5, the reflection and gap identities (Prop. 2.1: E ≤ ρ·(largest g-prime gap) − ½), the Legendre form, where routes (a)–(c) break, Theorems 4.1–4.2, the prior-art log (Diamond 1970 p. 24; Malliavin 1961 §6; BDR pp. 16–17; Lagarias 1999).

---

# read-F (COMPLETED) — Session 41, the orchestrator's read at the line (Fable 5.1, 16:52 IST 2026-10-01)

NOTE read whole at caeb71db64b81ea3… (440 lines) BEFORE the Opus `read-O.md` (9c8a5eec48f4d531…) was opened. **Verdict: AGREES-WITH-CORRECTIONS — close T + G stands.**

## What I re-derived
- Lemmas 1.0–1.2, 1.4, Cor. 1.4′, Lemma 1.5 (both forms of F_X), Theorem 1.6 (Session 40, above), Cor. 1.7: (ii) with the strict endpoint reads α > 1 − 2ρ ≥ max{½, 2θ} ≥ max{½, 2β} for ρ ≤ ¼, θ ≤ ½ − ρ. ✓
- Prop. 2.1 ✓ (k ≥ 1). The Lindley form, which the NOTE does not state: with x_k = 1 + (k − ½)/ρ, c_k = #composites in (x_{k−1}, x_k], e_k = N(x_k) − (k + 1): e_k = max(e_{k−1} + c_k − 1, 0), and a g-prime sits at x_k iff e_{k−1} = 0 and c_k = 0. (Proof: N(x) ≥ ⌈ρx + ½ − ρ⌉ forces N(x_k) ≥ k + 1 just after x_k; N(x_{k−1}) = k + e_{k−1}; the rule adds one g-integer at x_k exactly when e_{k−1} + c_k = 0.) S8 is a single-server queue, one service per lattice step, fed by composites; the g-primes are its idle steps. [proved here]
- §3.4 Legendre's identity and the floor M ≥ M_lat ✓ as identities.

## The reader's FIX-FIRST items — each re-derived before applying
- **F1 UPHELD.** Under the two-sided hypothesis, §3.4(i) gives E = o(x), so N ~ ρx; Diamond–Zhang Theorem 5.10 (checked at the page: `dz-half-s39/sources/t-50…txt` l. 2828–2835, "if and only if N has logarithmic density A") gives M(z) log z → e^{−γ}/ρ; the identity on (u, 2u] then gives π(u, 2u] ~ 2e^{−γ}u/log u; but N ~ ρx and π(x) ~ c·x/log x force c = 1 (compare log ζ_P(σ) = Σp^{−σ} + O(1) ~ c·log 1/(σ − 1) with ζ_P(σ) ~ ρ/(σ − 1)). 2e^{−γ} = 1.1229 ≠ 1. So the Legendre remainder carries the bias (1 − 2e^{−γ})u/log u and only one-sided forms can hold. I had not seen this in my own read.
- **F2 UPHELD** (two decision classes: a composite just below a live threshold, and one just above a threshold where a prime was placed; the unit audited the first only). Record-level; the certificates stand on the reader's double-double run.
- **F3 UPHELD** by arithmetic from the NOTE's own table: sup E/(ρ log²10⁶) = 0.375, 0.341, 0.257, 0.205, 0.213, 0.264.
- Minor m1–m13: read; all applied.

## The orchestrator's own finding (not in either read): the price of Lemma B_ρ
By Prop. 2.1, B_ρ for S8 has the strength of a g-prime gap bound x^θ, θ < ½ − ρ. A zero-density estimate N(σ, T) ≪ T^{A(1−σ)} yields gaps x^{1−1/A+ε}; even A = 2 gives ½. So no bootstrap through zero-density theorems (the Session-41 queue's route (iii)) reaches B_ρ for S8 as it stands; the route would need the design freedom of Theorem 1.6 to raise the admissible exponent (threshold τ → 0: θ < (1 − ρ − τ)/(2(1 − τ))), and even then stays below ½. This is why the stream `lemmaB-s41` carries two design units.

## Pairs
All 27 of the reader's pairs applied by `scripts/apply-read-pairs.py` (27/27 matched once); pre-reader copy `NOTE.pre-reader.md`. Unit CLOSED DUAL-READ: T (Lemmas 1.0–1.5, Theorem 1.6 — new as a statement on a printed core: Bateman–Grosswald 1964 p. 367; Phragmén — Cor. 1.7, Prop. 2.1, the Dichotomy, Theorems 4.1–4.2) + G (Lemma B_ρ; the one-sided Lemma S).
