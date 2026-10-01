# read-F — the orchestrator's read of `results/local-greedy-s40/NOTE.md` (Fable 5.1, Session 41, 16:55 IST 2026-10-01)

NOTE at bc5a4b6c7b87ec8a… (352 lines). §1 (definition, Lemmas 1.1–1.2) and §4 (K₇, Lemma 4.1, K₇^{≤2}) read at the line before the Opus `read-O.md` (459c85e26deec0c2…) was opened. **Verdict: AGREES-WITH-CORRECTIONS — close "K-candidate + two conditional theorems + G" stands.**

## Re-derived at the line
- **Lemma 1.1** ✓ (g-primes are prime powers, so representations factor over the primes and a_n is multiplicative).
- **Lemma 1.2** ✓: with y := ρ − E(q − 1) − A(q) + ½, E(q) = ½ − y + m_q; ⌊y⌋ ≥ 1 gives E(q) = ½ − {y} ∈ (−½, ½], y < 1 gives ½ − y > −½; between prime powers E falls by at most ρ per step; m_q ≤ y < ρ + 1 + ρ(q − 1 − q_prev).
- **Lemma 4.1** ✓: log Σ p₂(e)x^e = 2Σ_j j^{−1}x^j/(1 − x^j) ≤ π²/(3(1 − x)); at 1 − x = e^{−1/2}: p₂(e) ≤ exp(6√e); a_n ≤ exp(7√(ω(n)Ω(n))) = n^{o(1)}.
- **K₇, K₇^{≤2}** ✓ as conditional statements. Tail arithmetic re-done by hand at σ = 0.8010, θ = 0.40, X = 10⁹, |s| = 11.14: |s|X^{θ−σ}/(σ − θ) = 11.14 · 10^{−3.609}/0.401 = 6.83·10⁻³ (the NOTE's 0.00683), against min|F_X| = 0.0654 on the box — the latter is floating-point, by two producers (the unit and the Opus reader's direct sums).
- No generator of the orchestrator's own for S7; the Opus reader's two generators (sieve and additive DP) agree byte for byte with the unit's dumps to 10⁹ — two producers.

## The reader's FIX-FIRST items — upheld
- F1: "no other zero in σ ≥ 0.70 below height 100" is a scan of F_X at 10⁷, not a statement about ζ_P (at 0.70 + 94.63i the tail bound exceeds |F_X|).
- F2: Révész–Pintz's class also assumes Axiom A, which for S7 is the open hypothesis — S7^{≤2} is in their class only under H.
- m12, m13 (standing order 14): the two sentences about the Riemann hypothesis deleted.

## For the stream `lemmaB-s41`
S7^{≤2}(3/5) is the ℕ-supported counterpart of S8: multiplicities tamed by a proved lemma, a boxed zero of F_X at real part 0.824, and a missing growth lemma of the same kind (needed exponent ≤ 0.40 against a measured 0.19–0.22). Its downward half already needs prime-power gaps below x^{0.40}; S8 has no downward half to prove (E > −½ by construction), which is why S8 is the better target.

## Pairs
18/18 applied by `scripts/apply-read-pairs.py`; pre-reader copy `NOTE.pre-reader.md`. Unit CLOSED DUAL-READ: K-candidate (numerical; two producers) + T (Lemmas 1.1, 1.2, 4.1; K₇ and K₇^{≤2} conditional on H and on floating-point boxes) + G (Lemmas H₇, H₇^{≤2}).
