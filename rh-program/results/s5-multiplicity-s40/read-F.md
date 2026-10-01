# read-F — the orchestrator's read of `results/s5-multiplicity-s40/NOTE.md` (Fable 5.1, Session 41, 16:54 IST 2026-10-01)

NOTE at ced8b67448b79cdd… (331 lines). §4 read at the line before the Opus `read-O.md` (23092da42a583d03…) was opened; K's integer was recounted by the orchestrator in Session 40 (`verify-F/recount_nK_F.py`, equal). **Verdict: AGREES-WITH-CORRECTIONS — close K + T stands.**

## Re-derived at the line (§4)
- **T1** ✓. m_q ≥ 2 gives a_{q^k} ≥ k + 1; two distinct multisets M, M′ with product n₀ give the k + 1 distinct multisets j·M ⊎ (k − j)·M′ with product n₀^k (the multiplicity of an element where M and M′ differ is strictly monotone in j). So bounded multiplicity ⟺ a_n ≤ 1 ⟺ m_q ≤ 1 and multiplicative independence.
- **T2** ✓. V = {g-primes ≤ x} ∖ {rational primes in (x/2, x]} lies in ⟨primes ≤ x/2⟩ (a composite q ≤ x has every prime factor ≤ x/2), is independent, so A(x/2) + K(x) ≤ π(x/2): K(x) ≤ R(x/2), and (b) follows.
- **T3** ✓ given the quoted Landau-type PNT for Beurling systems (DMV pp. 2–3): R(y) − R(y/2) ≤ |π − li|(y) + |li − π_P|(y), summed dyadically. The converse example (ℙ ∖ R) ∪ {2p : p ∈ R} ✓ (triangular exponent vectors; H absolutely convergent at θ).
- **Lemma A, T4** ✓ line by line (log 1/u ≤ −log(1 − e^{−u}) ≤ log 1/u + u for u > 0; σ = c/log y, δ = σ/2; the tail condition is the stated lower bound for log x). **T4′** ✓ modulo Chebyshev, which the quoted PNT supplies.

## The reader's FIX-FIRST items — upheld
- F1: the NOTE's §9 rider headline claims more than T4′ proves (x^{κ/log log x} is not a power). The zoo line was narrowed to S5 itself before insertion (LOG, zoo-s40).
- F2: prior art. Olofsson 2010, pp. 10–11, checked by the orchestrator at the line (`novel-wave-s37/beurling-fe/sources/olofsson-2010-properties-beurling-primes.txt` l. 658–662): "if two different Beurling integers have the same value α, then there are at least n + 1 different Beurling integers having the value αⁿ, hence the remainder term is of at least logarithmic growth" — T1's quantitative core in print. Lagarias 1999 as the printed relative of T2–T3: accepted on the reader's zbMATH reading; the paper itself was not opened by either reader (label: [quoted from the review]).
- F3: "β > 0.383 ⇒ α ≤ 2β" needs α = Re ρ₁, which the record has only as α ≥ Re ρ₁ under a hypothesis K refutes.

## Pairs
18/18 applied by `scripts/apply-read-pairs.py`; pre-reader copy `NOTE.pre-reader.md`. Unit CLOSED DUAL-READ: K (n_K, four code paths) + T (T1 on a printed core; T2, T3, T4, T4′ new as statements).
