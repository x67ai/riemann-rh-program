# NOTE — seed M1b `beurling-frontier`: integer regularity below the square-root barrier vs RH for Beurling systems

Wave 2 (Session 37), 2026-09-30. Agent: Opus. Status labels: **[proved here]** (proof in this note),
**[computed]** (script + log in `verify/`), **[quoted]** (source on disk under `sources/`, page/line given),
**[recalled, unverified]** (never load-bearing), **[novelty: single-check]**.

Notation (Hilberdink; BDR). A Beurling system P = (p_j), N_P(x) = #{gen. integers ≤ x}, ψ_P(x) = Σ Λ_P(n_k).
An **[α, β]-system**: ψ_P(x) = x + O(x^{α+ε}) and N_P(x) = ρx + O(x^{β+ε}) for every ε > 0 and for no ε < 0.
"RH-false" for P means α > ½. Θ := sup{Re ρ : ζ(ρ) = 0} for the Riemann zeta function (Θ = ½ ⟺ RH).

## §1. Prior art, read at the page (task 1)

Sources (all under `sources/`, text by `pdftotext -layout`, line numbers refer to those .txt files):
- `z-02-…txt` = Broucke–Debruyne–Révész, *Some examples of well-behaved Beurling number systems*,
  arXiv:2309.01567**v2** (26 Jun 2024) — the arXiv listing (`arxiv-search-wellbehaved.xml`) shows v2 is the latest version.
- `w-18a-…txt` = Hilberdink, JNT 112 (2005) 332–344 (page images checked with the PDF reader for the garbled symbols).
- `z-18-…txt` = Broucke–Vindas, arXiv:2102.08478v2 (discretization).  `t-19a-…txt` = Broucke–Hilberdink, Acta Arith. 212 (2024).

**1.1 Hilberdink's wall** [quoted, w-18a p. 335 Theorem 1]: "Let P be an [α, β]-system. Then Θ = max{α, β} ≥ ½."
Corollary 2(b) [quoted, p. 336]: "If N_P(x) = ρx + O(x^β) for some constants ρ > 0 and β < ½, then for every
η′ ∈ (β, ½), ψ_P(x) − x = Ω(x^{η′}) and ζ_P(s) has infinitely many zeros in the strip {η′ < Re s < 1}."
(The proof, p. 336: Carlson's mean-value theorem applied to f = ζ_P − ρφ_P = Σ(1 − ρΛ_P(n))n^{−s}, of order 0
for Re s > Θ by Hilberdink–Lapidus Theorem A; the diagonal Σ(1 − ρΛ_P(n))²n^{−2σ} diverges for σ ≤ ½.)
So β < ½ forces α ≥ ½ — it does **not** say anything about α > ½.

**1.2 BDR, the populated region** [quoted, z-02 p. 3, line 131]: "Theorem 1.1. For any α ∈ [0, 1) and
β ∈ [1/2, 1) there exists an [α, β]-system." (unconditional).

**1.3 BDR, the region β < ½ — populated, conditionally on RH** [quoted, z-02 p. 4, line 183]:
"Theorem 1.3. Assume RH. Then there exists a [1/2, β]-system for each 0 ≤ β < 1/2 and an [α, β]-system for
1/2 < α < 2/3 and 2α/(α + 2) ≤ β < 1/2."  Figure 1 (p. 5, lines 236–249) labels this "region III", "constructed in
Section 5 under RH". So **the region {α > ½, β < ½} is populated in print, under RH**: the RH-false systems of
Theorem 1.3 have 2/5 < 2α/(α+2) ≤ β < ½ (α ↓ ½ gives 2α/(α+2) ↓ 2/5).

**1.4 What "only under RH" means exactly** [quoted, z-02 §5, pp. 16–21, lines 990–1260]:
- The template is (P, N) itself: "throughout this section we will assume the Riemann hypothesis, asserting that
  (P, N), the classical primes and integers, are a [1/2, 0]-system" (lines 1004–1006).
- Construction (lines 1096–1215): a random subsequence P_S of the classical primes, selected by the Broucke–Vindas
  procedure from the measure dF = u^{α−1}dπ(u) (a measure *supported on the primes*), is deleted, and the
  primes P^{1/β} = {p^{1/β}} are added as padding: P_{α,β} = P ∪ P^{1/β} \ P_S (line 1214).
- RH is used twice: (i) to know that the classical primes contribute only x^{1/2+ε} to ψ, so α is sharp; and
  (ii) (lines 1195–1205) for log ζ_S(s) = log ζ(s + 1 − α) + O(√log|t|) to give ζ_S, 1/ζ_S ≪ |t|^ε on
  Re s ≥ α/2 + ε: "(RH implies that both ζ(s) and 1/ζ(s) are ≪ε |t|^ε on half-planes Re s ≥ 1/2 + ε ...)".
  Use (ii) is structural: the deleted set is a set of **actual primes**, so its Dirichlet series carries the zeros of
  ζ shifted by α − 1 (see §3.2 below).
- The exponent 2α/(α+2) comes from Dirichlet's hyperbola method (Lemma 5.1, p. 17) applied to N * μ_S with
  N_S(x) + M_S(x) = ax^α + O(x^{α/2+ε}) (lines 1221–1228); the restriction α < 2/3 comes from the error measure dE
  (line 1201: "we use here that α < 2/3"); the double-prime variant allows α < 4/5 (Remark 5.3(1), line 1360).
- Remark 5.3(2) (line 1367): "We do not exclude the possibility that certain error terms in the calculation of
  N_{α,β}(x) can be improved with more advanced technology than Dirichlet's hyperbola method. Such improvements ...
  might give rise to a larger region of acceptable α and β in Theorem 1.3."
- Obstruction to adding (lines 1072–1090): "one cannot form [α, β]-systems with α > 1/2 and β < 1/2 by simply adding
  extra generalized primes to the classical primes P (if RH is true)." (Landau's theorem on log ζ_A.)
- Why the continuous-then-discretize route cannot reach β < ½ (p. 4, lines 171–179): any discretization giving
  O(x^θ), θ < ½, on one counting function "should have an uncertainty of size at least x^{1/2−ε}" on the other.

**1.5 Conclusion of task (1).** The frontier region {α > ½, β < ½} is **populated in print conditionally on RH**
(BDR Thm 1.3, sub-region 2α/(α+2) ≤ β < ½, ½ < α < 2/3). No unconditional example is in print (BDR p. 16, line 1003:
"for the classical primes ... we cannot yet prove α < 1"). Per the brief, the unit therefore moves to the frontier
questions; the orchestrator's pre-derivation is itself a frontier claim, since [β₀, β₀/2] lies strictly below BDR's
curve (β₀/2 < 2β₀/(β₀+2) for all β₀ < 2) and extends to β₀ ∈ [2/3, 1).
