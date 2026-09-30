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

**1.6 Other items read.** (a) Hilberdink 2012, *Generalised prime systems with periodic integer counting function*
[quoted, `p3-22c2-…txt` lines 30–40 (abstract) and Theorem A]: if N(x) − cx is periodic (β = 0 in the strongest form)
and N has finitely many discontinuities per bounded interval, "then N must be the counting function of the g-prime system
containing the usual primes except for finitely many." So in the periodic class, β = 0 forces ζ_P = ζ × (finite Euler
product), hence α(P) = Θ: **a periodic RH-false system exists iff RH is false** — rigidity, not a threshold.
(b) Broucke–Hilberdink 2024 (`t-19a`) concerns the opposite corner (α < ½, how small β can be): Ω(x·e^{−(log x)^{β}}), β > 2/3.
(c) arXiv sweep for later work (`sources/arxiv-search-beurling-recent.xml`: the 120 most recent abstracts containing
"Beurling", back to mid-2024; `arxiv-search-wellbehaved.xml`): no paper after BDR v2 (Jun 2024) treats [α, β]-systems with
β < ½. Items in the window on Beurling primes: 2602.07690, 2507.13780, 2409.10051, 2406.00736 (none on this corner).

## §2. The logical frame: what any threshold or obstruction theorem can and cannot say

**Proposition 2.1 (the region is populated unconditionally, non-constructively)** [proved here]. There exists a Beurling
system with α > ½ and β < ½.
*Proof.* If RH fails, take (P, N) itself. N(x) = ⌊x⌋, so |N(x) − x| < 1 and |N(n + ½) − (n + ½)| = ½: β = 0. If ζ(ρ₁) = 0 with
Re ρ₁ = σ₁ > ½ and ψ(x) − x = O(x^{σ₂}) with σ₂ < σ₁, then −ζ′(s)/ζ(s) − s/(s−1) = s∫₁^∞(ψ(x) − x)x^{−s−1}dx is analytic in
Re s > σ₂ — impossible at ρ₁. So α ≥ σ₁ > ½. If RH holds, BDR Theorem 1.3 (§1.3) gives [α, β]-systems with ½ < α < 2/3,
2α/(α+2) ≤ β < ½. ∎

**Corollary 2.2 (threshold theorems are capped and RH-strong)** [proved here]. Call β* ∈ (0, ½] a *valid threshold* if every
[α, β]-system with β < β* has α ≤ ½. Then (a) the existence of a valid threshold implies RH; (b) every valid threshold
satisfies β* ≤ 2/5, unconditionally.
*Proof.* (a) If RH fails, (P, N) has β = 0 < β* and α > ½ (proof of 2.1). (b) If RH fails, there is no valid threshold by (a).
If RH holds, BDR's [α, 2α/(α+2)]-systems (½ < α < 2/3) force β* ≤ 2α/(α+2) for every such α; let α ↓ ½. ∎
So the orchestrator's "if a threshold β* > 0 existed ... RH would be the case β = 0" is correct, and it is also the reason no such
theorem can be reached from the Beurling side without an input that already decides RH: the rational integers sit at β = 0.

**Proposition 2.3 (obstructions of the form β ≥ f(α) are RH-hard)** [proved here]. Let α(ℕ) := lim sup log|ψ(x) − x|/log x
for the rational primes. If for some a ∈ (½, 1] and f: (½, a) → (0, ∞) every [α, β]-system with α ∈ (½, a) has β ≥ f(α), then
α(ℕ) ∉ (½, a).
*Proof.* (P, N) has β = 0 (proof of 2.1); if α(ℕ) ∈ (½, a) it would be an [α(ℕ), 0]-system with 0 ≥ f(α(ℕ)) > 0. ∎
By the classical explicit formula α(ℕ) = Θ [recalled, unverified; the half α(ℕ) ≥ Θ is proved in 2.1]. So the conclusion is
"no Θ in (½, a)": no statement of the form
"Θ ∉ (½, a)" is known for any a > ½, so an obstruction theorem over all Beurling systems is at least as hard as a new zero-free
strip. A provable obstruction must be *relative*: it must bound β below by a quantity that vanishes on (P, N) itself — e.g. the
exponent α_R of a surgery R performed on (P, N) — see §5.

## §3. The orchestrator's pre-derivation, attacked clause by clause (task 2)

**3.0 It is BDR §5's construction.** "Remove actual primes at random with density ≍ p^{β₀−1}" is exactly the deletion of BDR
§5 (they delete a random subsequence of the classical primes drawn from dF = u^{α−1}dπ(u), z-02 lines 1096–1105). The
pre-derivation's new content is only the claimed integer exponent β₀/2 (vs BDR's 2α/(α+2)) and the claim "unconditionally".
We work with the cleanest instance, **Bernoulli thinning** T_α: delete each rational prime p independently with probability
w_p = p^{α−1} (α ∈ (½, 1); w_p ≤ 1 for all p, so no small primes need handling by hand, and no prime can be deleted twice —
the α < 2/3 and α < 4/5 restrictions of BDR, which come from their selection procedure, do not arise). Deleted set R,
P = ℙ \ R. The complex-zero variant is treated in 3.5.

**3.1 The density of log G — correct** [proved here]. For |s| > |ρ₀|, log G(s) = log(1 − ρ₀/s) + log(1 − ρ̄₀/s) =
−Σ_{k≥1}(ρ₀^k + ρ̄₀^k)/(k s^k), and 1/s^k = ∫₁^∞ x^{−s}(log x)^{k−1}/(k−1)! dx/x, so log G(s) = ∫₁^∞ x^{−s}·
[−Σ_k (ρ₀^k + ρ̄₀^k)(log x)^{k−1}/k!] dx/x = ∫₁^∞ x^{−s}(2 − x^{ρ₀} − x^{ρ̄₀})/(x log x) dx, i.e. the density
(2/x − 2x^{β₀−1}cos(γ₀ log x))/log x claimed. (Both sides are analytic in Re s > β₀, so the identity holds there.)

**3.2 "E[added − removed] = dν" — impossible as stated; the mean carries ζ's zeros** [proved here]. A deletion of actual
primes has mean Σ_p r(p)δ_p, a measure on the primes; no Poisson addition (absolutely continuous) can make the difference
equal to the absolutely continuous dν. What is left over is r(u)(dπ(u) − du/log u), and its Mellin transform is singular at
the zeros of ζ shifted by β₀ − 1. For T_α this is exact: with P(w) = Σ_p p^{−w} and X(s) := Σ_p (1_R(p) − w_p)p^{−s},
  Σ_{p∈R} p^{−s} = P(s + 1 − α) + X(s),   P(w) = log ζ(w) − Σ_{k≥2} P(kw)/k,
so (Prop. 4.2 below) ζ_P(s) = ζ(s)·ζ(s + 1 − α)^{−1}·U(s) with U analytic and zero-free in Re s > α/2 almost surely.
The factor ζ(s + 1 − α)^{−1} has a pole at s₀ = ρ − 1 + α for every zero ρ of ζ. Hence:
**Proposition 3.2.** If ζ has a zero ρ with Re ρ > 1 − α/2 and ζ(ρ − 1 + α) ≠ 0, then a.s. ζ_P has a pole at s₀ with
Re s₀ = Re ρ − (1 − α) > α/2, and N_P(x) − ρ_P x ≠ O(x^{σ}) for every σ < Re s₀; so β(P) ≥ Re ρ + α − 1 > α/2.
*Proof.* If N_P(x) − ρ_P x = O(x^σ), then ζ_P(s) − ρ_P s/(s − 1) = s∫₁^∞(N_P(x) − ρ_P x)x^{−s−1}dx (exact for Re s > 1) is analytic in
Re s > σ (Mellin transform of an O(x^σ) function), contradicting the pole at s₀ when σ < Re s₀. ∎
So the pre-derivation's "h ... converges a.s. and is analytic for Re s > β₀/2" is **false unconditionally**: it holds iff ζ(s + 1 − β₀)
has no zeros in Re s > β₀/2 that are not cancelled, i.e. (up to the coincidence clause) iff ζ has no zero with Re ρ > 1 − β₀/2.
The **fluctuating part X** of h is a.s. analytic in Re s > α/2 exactly as claimed (Lemma 4.1); the **mean part** is not.
Consequently "β = β₀/2" is not an unconditional statement: it implies a quasi-Riemann hypothesis at level 1 − β₀/2. This is
the same obstruction that makes BDR assume RH (§1.4(ii)). **Verdict on the unconditional claim: K.**

**3.3 The zero ρ₀ (α ≥ β₀) — correct unconditionally** [proved here, for T_α]. Near s = α all factors of U are analytic
(Re(k(s + 1 − α)) > 1 for k ≥ 2; X and the prime-square series converge for Re s > α/2), ζ(α) < 0 ≠ 0, and ζ(w)^{−1} has a
simple zero at w = 1. So ζ_P(α) = 0 a.s., and by the Mellin argument of 2.1 applied to −ζ_P′/ζ_P, α(P) ≥ α > ½. RH-false, unconditionally.

**3.4 The integer bound — what survives.** Under RH the mean part is harmless (§4). The pre-derivation's heuristic
"square-root cancellation in Σ_m c_m{x/m}" is right about the *size of the fluctuation* (Theorem B: it is ≥ x^{α/2} and this is sharp
in mean square), but a proof of the matching upper bound needs the error of the *mean system* Σ_{n≤y}Π_{p|n}(1 − p^{α−1}) to be
O(y^{α/2+ε}), which under RH is expected (≈ y^{α−1/2}) but which the standard contour argument only gives as y^{1/(4−2α)+ε} (§4.4).
The route that *is* complete: truncated Perron with the growth of ζ on Re s = α/2 + ε (the "ζ(σ+it)e^{h}" route of the brief)
gives β ≤ 1/(3 − α) (Theorem A). The hyperbola route (BDR) gives 2α/(α+2); the Perron route is strictly better for all α > ½.

**3.5 The complex-zero surgery (ρ₀ = β₀ + iγ₀) — same verdicts** [proved here, sketch of the bookkeeping]. The orchestrator's
recipe deletes primes where the density of ν is negative, with probability r(u) = (2u^{β₀−1}cos(γ₀ log u) − 2/u)₊, and adds
Poisson points where it is positive. Expanding (cos θ)₊ = Σ_k c_k e^{ikθ} (c₀ = 1/π, c_{±1} = ¼, …), the deleted mean is
Σ_k c_k·2P(s + 1 − β₀ − ikγ₀) + (terms regular in Re s > 0); its smooth part combines with the additions into log G by design,
and its prime part carries singularities at s = ρ − 1 + β₀ + ikγ₀ for every zero ρ and every k with c_k ≠ 0 — so 3.2 applies verbatim
with Re s₀ = Re ρ − (1 − β₀). A cleaner pure-deletion realization of a complex zero pair: w_p = min(1, p^{β₀−1}(2 + 2cos(γ₀ log p))),
which gives ζ_P = ζ(s)·ζ(s+1−β₀)^{−2}ζ(s+1−β₀−iγ₀)^{−1}ζ(s+1−β₀+iγ₀)^{−1}·U(s) (the min changes finitely many Euler factors):
zeros of order 2 at β₀ and order 1 at β₀ ± iγ₀. Everything in §4 goes through for it with the same exponents.

## §4. Theorems for Bernoulli thinning T_α

Throughout: ε_p ~ Bernoulli(w_p) independent, w_p = p^{α−1}, η_p = ε_p − w_p, v_p = w_p(1 − w_p), R = {p : ε_p = 1},
P = ℙ \ R, a_n = 1[n is R-free], N_P(x) = Σ_{n≤x} a_n, ρ_P = Π_{p∈R}(1 − 1/p) > 0 (Σ_{p∈R}1/p < ∞ a.s., mean Σ p^{α−2}).
X(s) = Σ_p η_p p^{−s}, Q_R(s) = Σ_{p∈R}Σ_{k≥2} p^{−ks}/k.

**Lemma 4.1 (the random part)** [proved here]. Let α ∈ (0, 1). Almost surely: (a) X(s) converges (in dyadic blocks) uniformly on
compact subsets of Re s > α/2 and is analytic there; (b) for each δ > 0, sup{|X(σ + it)| : σ ≥ α/2 + δ, |t| ≤ T} =
O((log T)^{1−2δ/α} + (log T)^{1/2}) = o(log T); (c) Q_R is bounded on Re s ≥ α/2 + δ.
*Proof.* (0) Small primes: S(y) := Σ_{p≤y}(ε_p + w_p)p^{−α/2−δ} has mean ≍ y^{α/2−δ}/log y and variance ≤ its mean; Chebyshev and
Borel–Cantelli along y = 2^j (monotone in y) give S(y) ≪ y^{α/2−δ} a.s. (1) Blocks: B_k = ℙ ∩ (2^k, 2^{k+1}], Y_k(s) = Σ_{p∈B_k} η_p p^{−s}.
For fixed σ ≥ α/2 + δ and t, Re Y_k and Im Y_k are sums of independent centred terms bounded by M_k = 2^{−kσ} with variance
≤ V_k := Σ_{p∈B_k} p^{α−1−2σ} ≤ 2^{−2kδ}. Bernstein: P(|Re Y_k| ≥ 2√(V_k L) + 2M_k L) ≤ 2e^{−L}. (2) Nets: for T = 2^j take the
grid of mesh 2^{−(j+k)} in (σ, t) ∈ [α/2 + δ, 2] × [−T, T] (≤ 2^{3(j+k)+3} points) and L = 4(j + k)log 2; since |∂Y_k| ≤
Σ_{p∈B_k}(ε_p + w_p)p^{−α/2} log p ≤ (k+1)2^{k(1−α/2)}, off-grid values move by ≤ 2(k+1)2^{−j−kα/2} (summable in k). The failure
probabilities sum to ≤ Σ_{j,k} 2^{3(j+k)+5}2^{−4(j+k)} < ∞: by Borel–Cantelli a.s. for all large j, all k and all grid-covered (σ, t),
|Y_k| ≤ 4√(V_k L) + 4M_k L + 2(k+1)2^{−j−kα/2}. (3) Sum, with the cut y₀ = j^{2/α}: the primes ≤ y₀ contribute ≤ S(y₀) ≪ j^{1−2δ/α};
the blocks above contribute ≪ Σ_k 2^{−kδ}√(j + k) + (j + log y₀)y₀^{−α/2} + 2^{−j} = O(√j) + O(1). Since j ≍ log T this is (b);
the same bounds with j fixed give (a). (c): |Q_R(s)| ≤ 2Σ_{p∈R} p^{−α−2δ}, whose mean Σ_p p^{−1−2δ} is finite. ∎

**Proposition 4.2 (structure)** [proved here]. A.s., for Re s > α,
  ζ_P(s) = ζ(s)Π_{p∈R}(1 − p^{−s}) = ζ(s)·ζ(s + 1 − α)^{−1}·U(s),  U(s) := exp(Σ_{k≥2}P(k(s + 1 − α))/k − X(s) − Q_R(s)),
and U is analytic, zero-free, with |U(s)|^{±1} ≤ exp(o(log|t|)) on Re s ≥ α/2 + δ. So ζ_P continues meromorphically to Re s > α/2
with poles only at s = 1 and possibly at s = ρ − 1 + α, ρ a zero of ζ (none with Re s > α/2 under RH, since then Re(ρ − 1 + α) = α − ½ < α/2), and a zero at s = α.
*Proof.* log Π_{p∈R}(1 − p^{−s})^{−1} = Σ_{p∈R}p^{−s} + Q_R(s) = Σ_p w_p p^{−s} + X(s) + Q_R(s), and Σ_p w_p p^{−s} = P(s + 1 − α) with
P(w) = log ζ(w) − Σ_{k≥2}P(kw)/k (from log ζ(w) = Σ_k P(kw)/k). For Re s > α/2 one has Re(s + 1 − α) > 1 − α/2 > ½, so
Σ_{k≥2}P(k(s+1−α))/k converges absolutely and is bounded; X, Q_R by Lemma 4.1. ∎

**Theorem A (RH ⟹ β ≤ 1/(3 − α) for T_α)** [proved here; novelty: single-check]. Assume RH and let ½ < α < 1. Almost surely,
  ψ_P(x) = x − x^α/α + O(x^{½+ε})  and  N_P(x) = ρ_P x + O(x^{1/(3−α)+ε})  for every ε > 0.
So a.s. P is an [α, β]-system with α/2 ≤ β ≤ 1/(3 − α) < ½ (lower bound: Theorem B).
*Proof.* Inputs quoted: under RH, ζ(s) and 1/ζ(s) are ≪ |t|^ε on Re s ≥ ½ + ε (BDR z-02 lines 1203–1205, citing Montgomery–Vaughan
Th. 13.18, 13.23); ψ(x) = x + O(x^{½+ε}) (the RH form quoted at z-02 lines 26–27, in the ψ-normalization). Recalled standard tools
[recalled, unverified]: |χ(σ + it)| ≍ |t|^{½−σ} in ζ(s) = χ(s)ζ(1 − s) (Stirling); the truncated Perron formula
Σ_{n≤x}a_n = (1/2πi)∫_{κ−iT}^{κ+iT}F(s)x^s ds/s + O(x^κ Σ_n |a_n| n^{−κ} min(1, 1/(T|log(x/n)|))); Bernstein's inequality; Phragmén–Lindelöf.
(i) Primes. ψ_P = ψ − ψ_R and ψ_R(x) = Σ_{p≤x} ε_p log p + O(√x log x). The centred part Σ_{p≤x} η_p log p has variance ≍ x^α log x;
Bernstein plus Borel–Cantelli along x = 2^j (monotone pieces between) give O(x^{α/2+ε}) a.s. The mean: Σ_{p≤x} p^{α−1}log p =
∫_{2−}^x u^{α−1}dθ(u) = x^α/α + O(x^{α−½+ε}) by partial summation from θ(u) = u + O(u^{½+ε}). As α/2, α − ½ < ½ < α, α(P) = α.
(ii) Integers. a_n ∈ {0, 1} is supported on ℕ, so with κ = 1 + 1/log x and 2 ≤ T ≤ x the Perron error is O(x log x/T + 1).
Let c′ = α/2 + δ. Under RH the rectangle [c′, κ] × [−T, T] contains no singularity of ζ_P(s)x^s/s except s = 1 (Prop. 4.2).
On Re s = c′: |ζ(c′ + it)| = |χ||ζ(1 − c′ − it)| ≪ |t|^{½−c′+δ} (1 − c′ > ½), |ζ(s + 1 − α)^{−1}| ≪ |t|^δ (Re(s + 1 − α) =
1 − α/2 + δ > ½), |U| ≪ |t|^δ (Lemma 4.1). So |ζ_P(c′ + it)| ≪ (|t| + 2)^{½−c′+3δ}; on the horizontal sides Phragmén–Lindelöf
interpolates between this and |ζ_P(1 + δ + it)| ≪ 1, so ∫|ζ_P(σ ± iT)|x^σdσ/T ≪ (x + x^{c′}T^{½−c′+3δ})/T. Hence
  N_P(x) = ρ_P x + O(x log x/T + x^{c′}T^{½−c′+3δ}).
Take T = x^{(1−c′)/(3/2−c′)} (< x): the error is O(x^{1/(3−2c′)+O(δ)}) = O(x^{1/(3−α)+O(δ)}); δ is arbitrary. ∎

**Corollary A′ (the region enlarged)** [proved here; novelty: single-check]. Assume RH. For every α ∈ (½, 1) and every
β ∈ (1/(3 − α), ½) there is an [α, β]-system: P_{α,β} = (ℙ \ R) ∪ ℙ^{1/β} for almost every realization R of T_α.
*Proof.* BDR Lemma 5.1 [quoted, z-02 p. 17, lines 1024–1040: if Σ_{n≤x,n∈N}1 = ax + O(x^γ) and Σ_{l≤x,l∈L}h(l) = bx^β + O(x^δ),
0 ≤ γ, δ < β < 1, then Σ_{nl≤x}h(l) = aH(1)x + bI(β)x^β + O(x^{(β−γδ)/(1−γ+β−δ)})] with N = R-free integers (a = ρ_P,
γ = 1/(3−α) + ε < β by Theorem A), L = ℕ^{1/β}, h ≡ 1 (b = 1, δ = 0): N_{α,β}(x) = ρ_Pζ(1/β)x + ζ_P(β)x^β + O(x^{β/(1+β−γ)}),
and β/(1 + β − γ) < β. Here I(β) = ζ_P(β) = ζ(β)ζ(β + 1 − α)^{−1}U(β) ≠ 0 (ζ < 0 on (0, 1), β + 1 − α ∈ (0, 1), U(β) = e^{real} > 0,
and β > 1/(3 − α) > α/2). So the integers are β-well-behaved and not better. The added primes p^{1/β} change ψ by O(x^β) = o(x^{½}),
so α is unchanged. ∎
*Comparison with print.* BDR Theorem 1.3 gives ½ < α < 2/3, 2α/(α + 2) ≤ β < ½. Since 2α/(α+2) − 1/(3−α) has the sign of
−(2α − 1)(α − 2) > 0 on (½, 2), region III ⊂ {1/(3−α) < β < ½}, strictly, and the α-range grows from (½, 2/3) to (½, 1). The corner
value is unchanged: 1/(3 − α) → 2/5 as α ↓ ½, so Corollary 2.2's cap β* ≤ 2/5 is not improved by Theorem A.

**Theorem B (random thinning cannot beat α/2 — unconditional)** [proved here]. For every α ∈ (0, 1), almost surely
N_P(x) − ρ_P x ≠ O(x^τ) for every τ < α/2. In particular β(T_α) ≥ α/2 a.s., with no hypothesis on ζ.
*Proof.* (1) Formula. With μ_R(m) = Π_{p|m}(−ε_p) on squarefree m, N_P(x) = Σ_m μ_R(m)⌊x/m⌋ and ρ_P = Σ_m μ_R(m)/m (absolutely
convergent a.s.), so E(x) := N_P(x) − ρ_P x = −Σ_m μ_R(m){x/m}, the sum over all squarefree m ({x/m} = x/m for m > x).
Write ε_p = w_p + η_p: μ_R = μ_w * μ_η with μ_w(k) = Π_{p|k}(−w_p), μ_η(d) = Π_{p|d}(−η_p), hence
  E(x) = −Σ_d μ_η(d)·T(x/d),  T(y) := Σ_k μ_w(k){y/k}  (deterministic; T(y) = ρ_w y for y < 1, ρ_w := Π_p(1 − w_p/p)),
where rearrangement is justified by Σ_{d,k}|μ_η(d)μ_w(k)|x/(dk) = xΠ_p(1 + |η_p|/p)(1 + w_p/p) < ∞ a.s.
(2) 0–1 law. If q ∉ R and R′ = R ∪ {q}, the P′-integers are the P-integers not divisible by q, and those divisible by q are q·(P-integers);
so N_{P′}(x) = N_P(x) − N_P(x/q), ρ′ = ρ(1 − 1/q), E′(x) = E(x) − E(x/q), and conversely E(x) = Σ_{j≥0}E′(x/q^j) (with |E′(y)| ≤ y
for y < 1). Hence {E(x) = O(x^τ)} is invariant under changing finitely many ε_p; by Kolmogorov's 0–1 law it has probability 0 or 1.
(3) One scale. Fix large x, B = ℙ ∩ (x/2, x], G = σ(ε_q : q ∉ B). Split d by its B-part: terms with no B-prime give Y (G-measurable);
terms with exactly one B-prime p (d = pe) give η_p·c_p with c_p = T(x/p) + ρ_w(x/p)(Π′ − 1) = κ·(x/p) − 1, where
Π′ = Π_{q∉B}(1 − η_q/q), κ = ρ_wΠ′ > 0 (because for 1 ≤ y < 2, T(y) = ρ_w y − 1, and x/(pe) < 1 for e ≥ 2); terms with ≥ 2 B-primes give
Z = −ρ_w xΠ′Σ_{f⊂B,|f|≥2}μ_η(f)/f, and E|Z| ≪ x·Σ_{p∈B}v_p p^{−2} ≪ x^{α−1}. So E(x) = Y + S_B + Z with S_B = Σ_{p∈B}η_p c_p,
the η_p (p ∈ B) independent of G. Given G, S_B has variance σ_B² = Σ_{p∈B}v_p(κx/p − 1)². The y = x/p ∈ [1, 2) with |κy − 1| < θ
form an interval of length ≤ 2θ/κ; by the prime number theorem in intervals of length ≍ x, at most a fraction 4θ/κ + o(1) of
the primes of B have x/p there. With θ = min(κ, 1)/16 and v_p ≍ x^{α−1} on B: σ_B² ≥ c·min(κ, 1)²x^α/log x. Berry–Esseen
(|η_p| ≤ 1, so E|η_p c_p|³ ≤ max|c|·v_p c_p²) gives P(|Y + S_B| ≤ λσ_B | G) ≤ λ + C(2κ + 1)/σ_B. As x → ∞, κ = κ_x → κ_∞ :=
ρ_wΠ_q(1 − η_q/q) ∈ (0, ∞) a.s. Therefore for every η₀ > 0 there are λ₀ > 0 and x₀ with
  P(|E(x)| ≤ λ₀x^{α/2}(log x)^{−1/2}) ≤ P(κ_x < η₀) + P(|Z| > x^{α/3}) + 2λ₀/(√c·η₀) + o(1) ≤ ½  for x ≥ x₀
(choose η₀ with P(κ_∞ < 2η₀) ≤ ⅛, then λ₀; the Berry–Esseen term is O((1 + E κ)√(log x)/(η₀x^{α/2})) → 0).
(4) If P(E = O(x^τ)) = 1 for some τ < α/2, then P(sup_x |E(x)|x^{−τ} ≤ C) ≥ ¾ for some C, while Cx^τ < λ₀x^{α/2}(log x)^{−1/2}
for large x, contradicting (3). So the probability is 0 for each τ < α/2; intersect over rational τ. ∎

*Remark.* This is the theorem form of the orchestrator's "nothing below ¼ by this method": α > ½ forces β ≥ α/2 > ¼ for the random
surgery, with no RH. The obstruction is *relative* (it is driven by the deleted set, and vanishes for R = ∅), so it does not
contradict Prop. 2.3.

**4.4 The mean system and the gap between α/2 and 1/(3 − α).** E[N_P(x)] = Σ_{n≤x}f(n), f(n) = Π_{p|n}(1 − p^{α−1}), whose Dirichlet
series is exactly ζ(s)/ζ(s + 1 − α) (f = 1 * g, g(d) = μ(d)d^{α−1}). From (1), E[E(x)] = −T(x) and Var E(x) = Σ_{d>1}V(d)T(x/d)²,
V(d) = Π_{p|d}v_p ≤ d^{α−1}. If T(y) ≪ y^{τ₀+ε} with τ₀ < α/2 then Var E(x) ≪ x^{α+ε}: the pointwise size of E(x) is x^{α/2+o(1)}.
Under RH the explicit formula for 1/ζ(s + 1 − α) predicts T(y) ≈ y^{α−½} (poles at ρ − 1 + α) [heuristic], and α − ½ < α/2; but
the contour argument of Theorem A applied to ζ(s)/ζ(s + 1 − α) only proves T(y) ≪ y^{1/(4−2α)+ε} (c′ = α − ½ + δ), and
1/(4 − 2α) > α/2 for all α < 1. **Named gap G1:** prove, under RH, Σ_{n≤y}Π_{p|n}(1 − p^{α−1}) = y/ζ(2 − α) + O(y^{α/2+ε}).
**G2:** upgrade the variance bound to a.s. uniformity (moments of the Bernoulli chaos Σ_d μ_η(d)T(x/d) of unbounded degree;
monotonicity of N_P reduces uniformity to a grid of mesh x^{α/2}). G1 + G2 would give β(T_α) = α/2 under RH.
