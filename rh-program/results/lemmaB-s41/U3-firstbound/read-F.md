# read-F — the orchestrator's read of `results/lemmaB-s41/U3-firstbound/NOTE.md` (Fable 5.1, Session 41, 18:50 IST 2026-10-01)

NOTE at f3dfc4539a5a58c8… (243 lines). Read at the line: §1.1–§1.5 (lines 42–137) — the identity, Lemmas B1, C1, D1, Corollary D2, Lemma E1, Theorem T1. NOT read here: §1.6 (threshold variants), §1.7–§1.8 (the explicit constants and the sharper form T1′), §1.9 (Mertens' second theorem), §2 (the class theorem) — left to the Opus reader launched the same hour (`read-O.md`) and to Session 42.

## §1.1–§1.5 re-derived — every step ✓
- **(*)** is the relation of `../ORCH-NOTES.md` O9 (correction block), derived there independently.
- **Lemma B1** ✓. At a g-prime y: E(y) = ½ and −∫_1^y E du/u < ½·log y (E > −½), so the left side of (*) is < log y; on the right Σ_{d≤y}Λ(d)E(y/d) ≥ −ψ(y)/2, so the right side is ≥ y·F(y) − ρ. Hence F(y) < (log y + ρ)/y.
- **Lemma C1** ✓. Between prime powers dF/dx = −(½ − ρ)ψ/x² − ρ/x < 0 (this is where ρ < ½ enters); F jumps by Λ(d)/(2d) at prime powers; after the last g-prime P ≤ x only powers p^j, j ≥ 2, occur, and their total is bounded by the convergent tail T(P) (g-primes are distinct lattice points). In Δ-form: (½ − ρ)ψ(x)/x ≤ ρΔ(x) + ε(x), ε → 0.
- **Lemma D1, Cor. D2** ✓. With g(t) = Ψ̃(e^t): g′ + 2ρg ≤ 2ρ(t − 1) + 2ε; the integrating factor e^{2ρt} and the particular solution t − 1 − 1/(2ρ) (checked by differentiation) give D(x) ≥ 1/(2ρ) − o(1), then Δ ≥ (1 − 2ρ)D − 2ε: a Mertens UPPER bound S(x) ≤ log x − 1/(2ρ) + o(1).
- **Lemma E1** ✓. At a record A = E(x)/x of E(u)/u: left side ≥ A·x·log x − A(x − 1); Σ Λ(d)E(x/d) ≤ A·x·S(x); the algebra gives (A + ρ)Δ ≤ (1 − ρ)ψ/x − (A + ρ)/x.
- **Theorem T1** ✓. At a record beyond X₀: A + ρ ≤ 2(1 − ρ)(ρ + ε₀/Δ₀)/(1 − 2ρ), i.e. A ≤ ρ/(1 − 2ρ) + o(1). No circularity found: every quantity is a finite sum at each x; D1 uses only C1; Δ₀ > 0 for X₀ large because liminf D ≥ 1/(2ρ) and ε → 0.

## Status after this read
**N(x) = O(x) for S8(ρ), 0 < ρ < ½, is PROVED as far as one writer and the orchestrator's read go — the first unconditional upper bound for the system at all scales; with it Σ 1/p and the Mertens sums are controlled from above.** The asymptotic constant of T1 is limsup E(x)/x ≤ ρ/(1 − 2ρ); the unit's sharper T1′ (≤ ρ, with explicit all-x constants 0.196413 and 0.098198) is not read here. This is far from Lemma B (which needs a power saving): the bound is linear. No correction pairs from this read.
