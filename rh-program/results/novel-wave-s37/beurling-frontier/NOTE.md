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

## §5. The frontier (task 4): structured surgery, relative obstructions, rung 1

**5.1 Exact variance for finite deletions** [proved here; computed: `verify/finite_R_variance.py`, log `verify/logs/finite_R_variance.log`].
*Proposition 5.1.* Let R be a finite set of primes, Q = Π_{p∈R}p, ρ = φ(Q)/Q, E(x) = #{n ≤ x : (n, Q) = 1} − ρx. Then E is
Q-periodic with mean 0 and (1/Q)∫₀^Q E(x)²dx = ρ·2^{|R|}/12.
*Proof.* E(x) = −Σ_{m|Q}μ(m)ψ(x/m) with ψ(y) = {y} − ½ (Möbius inversion; Σ_{m|Q}μ(m) = 0). Franel's integral
∫₀¹ψ(au)ψ(bu)du = (a, b)²/(12ab) with a = Q/m, b = Q/m′ gives (1/Q)∫₀^Q ψ(x/m)ψ(x/m′)dx = (m, m′)²/(12mm′). Writing
(m, m′)² = Σ_{d|(m,m′)}J₂(d) (Jordan's totient) and Σ_{d|m|Q}μ(m)/m = (μ(d)/d)Π_{p|Q/d}(1 − 1/p):
Σ_{m,m′}μ(m)μ(m′)(m,m′)²/(12mm′) = (ρ²/12)Σ_{d|Q}Π_{p|d}(1 − p^{−2})(1 − 1/p)^{−2} = (ρ²/12)Π_{p∈R}(2p/(p − 1)) = ρ2^{|R|}/12. ∎
(Exact rational arithmetic confirms it for eight sets R up to Q = 2310.) The mean square equals ρ/12 times the number of
R-numbers (squarefree products of deleted primes). **Heuristic transfer:** at scale x only the R-numbers m ≤ x oscillate
(for m > x, {x/m} = x/m is smooth), so for an infinite sparse R one expects mean-square E(x)² ≍ #{R-numbers ≤ x} ≍ x^{α_R},
where α_R := lim sup log π_R(x)/log x — for **any** R, random or structured. Theorem B proves this for random R.

**5.2 Relative-obstruction conjecture (task 4's question, answered in conjectural form).**
*Conjecture O.* For every set R of primes with Σ_{p∈R}1/p < ∞ and every set A of added generalized primes, the system
(ℙ \ R) ∪ A satisfies β ≥ α_R/2. [Status: proved for Bernoulli R (Theorem B); exact over a period for finite R (5.1); tested on a
deterministic minimal-discrepancy R in §6.3.] Consequence under RH: for systems obtained by surgery on ℙ, α > ½ forces α_R = α
(the deleted set must carry the deviation, by BDR's Landau argument for pure additions, z-02 lines 1072–1090), hence
**β ≥ α/2 > ¼: under RH and Conjecture O, ¼ is an exact threshold for the surgery class.** This does not contradict Prop. 2.3,
because the bound is relative (α_R = 0 for ℙ itself). Additions should not help [heuristic]: the dilates E_{R-free}(x/a), a ∈ ⟨A⟩, have no common
rational frequencies for generic real a, so their mean squares add rather than cancel.

**5.3 How close to free can bounded error with RH false be?** [proved here] A *finite* surgery (deleting or adding finitely many
generalized primes q) multiplies ζ by Π(1 − q^{−s})^{±1}, whose zeros and poles lie on Re s = 0; it keeps α = α(ℙ) = Θ and the integer
error O(log x). So with Λ ≥ 0 (freeness) a finite modification never creates a zero off the line; F_{5,5} = ζ(s)(1 + 5·5^{−s} + 5^{1−2s})
does it with one Euler factor 1 + 5u + 5u² (u = 5^{−s}) whose logarithm has u²-coefficient −((ω₁ + ω₂)² − 2ω₁ω₂)/2 = −(25 − 10)/2 < 0
(ω₁,₂ = (−5 ± √5)/2): non-free at 25, as the charter records. Hilberdink 2012 (§1.6) is the periodic-class version: β = 0 in periodic
form forces a finite modification of ℙ. **To decouple α from Θ one needs infinitely many deletions, and (Theorem B / Conjecture O)
each such decoupling costs β ≥ α_R/2.** So "free + RH-false + β < ¼" is out of reach of surgery on ℙ, and at β < ½ nothing else is known.

**5.4 Rung-1 control (mandatory).** The virtual curve Z(u) = (1 − 5u + 5u²)/((1 − u)(1 − 5u)) (charter §0(e)) is a Beurling system
over the norm group 5^ℤ (closed-point counts b_d ≥ 0, free) with effective-divisor counts A_n = (5^n − 1)/4 *exactly* for n ≥ 1 —
perfect integer regularity — and zeros at Re s = 0.79899 (u = (5 − √5)/10). So in rung 1 **no threshold theorem exists at all**, even
at "β = 0" and even with the functional equation; any threshold argument over ℚ must use an input that the virtual curve lacks.
Over ℝ the virtual curve is not even an [α, β]-system (N(x)/x oscillates log-periodically: the norm group is discrete), so the first
archimedean input is "the norms have a density" — and Theorems A/B show that density plus β < ½ still admits α > ½ (under RH for ζ).
The input that separates real curves from the virtual one is Castelnuovo/Hodge-index positivity on C × C, whose ℚ-analogue is Weil's
positivity of the explicit-formula quadratic form — RH-equivalent. So the archimedean input a threshold theorem would need is RH itself.

## §6. Simulation (task 3) — evidence, not theorems

**6.1 Design** [computed: `verify/thin.c`, `verify/thin_aux.c`, driver `verify/run_all.sh`, log `verify/logs/run_all.log`,
data `verify/data/*.csv`, fits `verify/fit.py` → `verify/logs/fit.log`, `verify/data/fit_summary.json`].
- **Systems.** (i) T_α (Bernoulli thinning, w_p = p^{α−1}) for α = 0.60, 0.75, 0.90; seeds 1–8; the decision for prime p is a
  64-bit hash of (p, seed, α), so a run is reproducible from its command line. (ii) *Greedy* (structured) deletion: delete p iff
  #R∩[2, p) < F(p) := Σ_{q≤p}q^{α−1} — the deterministic set with |π_R(x) − F(x)| < 1, the most regular deletion with the same
  weights (task 4's "structured surgery"). (iii) Controls with the same code: *none* (ℙ itself; β = 0 expected); *Cramér* (2 prime,
  n ≥ 3 prime with probability 1/log n, Beurling integers counted with multiplicity by an exact multiplicative DP; a full random
  discretization, β = ½ expected); the *mean system* Σ_{n≤y}Π_{p|n}(1 − p^{α−1}) − y/ζ(2 − α) (deterministic; tests gap G1).
- **Exactness.** N_P(n) is an exact integer count for every n ≤ X = 10⁹ (a bitset sieve of R-free integers; deleted primes up to
  Y = 4·10⁹ enter ρ_P). ρ_P = Π_{p∈R,p≤Y}(1 − 1/p)·exp(−E₁((1 − α)log Y)) (mean tail ∫_Y^∞u^{α−2}du/log u); the tail's random part
  has standard deviation ≈ (Y^{α−2}/((2−α)log Y))^{1/2}, i.e. ≲ 4% of the signal x^{α/2} at x = X and negligible for x ≤ X/10.
  For Cramér, log ρ = ½ − γ − log log 3 + D + A + G₂ with D = lim[Σ_{3≤n≤M}1/(n log n) − log log M + log log 3], A = Σ_{n≥3}(1_P(n) −
  1/log n)/n, G₂ = Σ_{q∈P}(−log(1 − 1/q) − 1/q), summed to Y = 2·10⁹ (derivation: log ζ_P(s) + log(s − 1) → log ρ as s ↓ 1 with
  ∫₃^∞u^{−s}du/log u = E₁((s − 1)log 3) = −γ − log((s − 1)log 3) + o(1)).
- **Cross-checks.** `verify/check_small.py` re-derives R, ρ_P and N_P(10⁵) from the same hash in Python: identical (nR(10⁶) = 607,
  ρ_P = 0.180739782781, E(10⁵) = 2.021722). The Cramér DP matches a brute-force multiset count (N(2000) = 3097).
- **Statistics.** Log-bins of 20 per decade; per bin the exact sup of |N_P(x) − ρx| over real x and the RMS at half-integers.
  Exponents = least-squares slopes of log(running sup) and log(RMS) against log x over windows [10^k, 10⁹], k = 4, 5, 6, 7;
  error bars = standard error over seeds (8 for T_α); the spread between windows is reported as a systematic.

**5.5 Theorem C (the prime-power branch points of a structured deletion — unconditional)** [proved here; novelty: single-check].
Let 0 < α < 1, c > 0, w_p = min(1, c·p^{α−1}), F(x) = Σ_{p≤x}w_p, and let R be any set of primes with π_R(x) − F(x) = O(x^θ),
θ < α/k, where k = k_c := min{k ≥ 2 : c/k ∉ ℤ}. (The greedy set "delete p iff #R∩[2, p) < F(p)" has |π_R − F| ≤ 1 for all x — by
induction, since each step changes F by w_p ≤ 1 — so θ = 0 works.) Then, unless α/k is one of the finitely many coincidence points
listed below, ζ_{ℙ\R} is not analytic at the real point s = α/k, and hence **β(ℙ \ R) ≥ α/k_c**. For c = 1: β ≥ α/2. For c = 2: β ≥ α/3.
For c = 6: β ≥ α/4.
*Proof.* S₁(s) := Σ_{p∈R}p^{−s} = ∫u^{−s}dF(u) + s∫₁^∞(π_R − F)(u)u^{−s−1}du = c·P(s + 1 − α) + H(s), where H is analytic in Re s > θ
(and the finitely many p with w_p = 1 contribute an entire correction). log(1/ζ_R(s)) = −Σ_{j≥1}S₁(js)/j. At s near the real point
α/k: for j > k, Re(js + 1 − α) > 1 and S₁(js) is analytic; for j < k, js + 1 − α is real in (1 − α, 1) near s = α/k, where P(w) =
Σ_m μ(m)log ζ(mw)/m is analytic (ζ has no real zeros in (0, 1)) unless mw = 1 for some squarefree m ≥ 2 — the *coincidence points*
jα/k = 1/m − 1 + α; for j = k, w = ks + 1 − α → 1 and c·P(w)/k = −(c/k)log(ks − α) + analytic. Hence
  ζ_{ℙ\R}(s) = ζ(s)·(ks − α)^{c/k}·B(s),  B analytic and zero-free near α/k (the other j contribute exp(analytic)),
and ζ(α/k) ≠ 0. For c/k ∉ ℤ this is a branch point. The same continuation is reached along the real segment from s = α (where the
product converges) because the points α/j, 2 ≤ j < k, are regular (there (js − α)^{c/j} with c/j ∈ ℤ). If N_P(x) − ρx = O(x^{σ₁}) with
σ₁ < α/k, the Mellin transform s∫(N_P − ρx)x^{−s−1}dx = ζ_P(s) − ρs/(s − 1) would be analytic in Re s > σ₁, contradiction. ∎
*Also* (same argument): (a) P(w) = Σ_m μ(m)log ζ(mw)/m contains −½log ζ(2w) = ½log(2w − 1) + analytic near w = ½, so
−c·P(s + 1 − α) contributes (2s + 1 − 2α)^{−c/2}: a pole or branch point at the **real** point s = α − ½ for every c > 0, with
ζ(α − ½) ≠ 0. Hence, unconditionally, **β ≥ max(α/k_c, α − ½)** for structured deletions (when θ < α − ½; for c = 2 the point α − ½
is a simple pole, i.e. a secondary main term C·x^{α−½} in N_P). (b) Poles of ζ(s + 1 − α)^{−c} at ρ − 1 + α give β ≥ Θ + α − 1
generically (= α − ½ under RH: the same value as (a)).
*Remarks.* (i) The prime squares of the deleted set are what produce the α/2 point: S₂(s) = S₁(2s) is a Dirichlet series with
non-negative coefficients and abscissa α_R/2, singular there by Landau's theorem (quoted in BDR, z-02 lines 1077–1080). This is a
"relative Hilberdink wall": Hilberdink's ½ is also a square-root phenomenon (the diagonal Σ(1 − ρΛ(n))²n^{−2σ} of his proof, §1.1).
(ii) For random deletions the branch point is present too, but the Bernoulli fluctuation X(s) (natural scale Re s = α/2) dominates;
Theorem B holds for every c. (iii) Theorem C gives lower bounds only: the continuation of exp(−H) has no growth control, so no
Perron upper bound is available for structured deletions. Whether structured deletions *attain* max(α/k_c, α − ½) is the question
tested numerically in §6.3.

**6.2 Results at X = 10⁹: random thinning and controls** [computed; `verify/logs/fit.log`]. Slopes of log sup_{y≤x}|E(y)| over
[10⁴, 10⁹] (mean ± s.e. over seeds; in brackets the range over the four windows [10^k, 10⁹], k = 4..7):

| system | seeds | sup-slope | window range | α/2 | 1/(4−2α) | 1/(3−α) (Thm A) | 2α/(α+2) (BDR) |
|---|---|---|---|---|---|---|---|
| T_0.60 | 8 | 0.303 ± 0.008 | [0.303, 0.317] | 0.300 | 0.357 | 0.417 | 0.462 |
| T_0.75 | 8 | 0.353 ± 0.013 | [0.353, 0.373] | 0.375 | 0.400 | 0.444 | 0.545 |
| T_0.90 | 8 | 0.457 ± 0.012 | [0.455, 0.524] | 0.450 | 0.455 | 0.476 | 0.621 |
| none (ℙ itself) | 1 | 0.000 | [0.000, 0.000] | — | — | — | — |
| Cramér (full random) | 4 | 0.497 ± 0.006 | [0.428, 0.628] | — | — | — | — |

(Cramér: per-seed [10⁴, 2·10⁸] slopes 0.496, 0.504, 0.510, 0.480 — the β = ½ control.) RMS-slopes agree within errors
(0.303 ± 0.013, 0.337 ± 0.021, 0.466 ± 0.026). The measured RMS at the top decade is 0.75–4.4 × √(ρ_P·Q(x)/12), Q(x) = (6/π²)x^α/α the
expected number of squarefree R-numbers — the variance mechanism of §5.1 has the right size for random deletions
(`verify/analyze_extra.py`, log `verify/logs/analyze_extra.log`).
**Reading.** The random-thinning exponent sits at α/2, as the pre-derivation predicted and as Theorem B forces from below; the
rigorous upper bound 1/(3 − α) of Theorem A lies 14σ (α = 0.6) and 7σ (α = 0.75) above the data, 1/(4 − 2α) lies 7σ and 3.6σ above,
and BDR's 2α/(α + 2) is further still.
At α = 0.9 the candidates α/2 and 1/(4 − 2α) differ by 0.005 and cannot be separated.

**6.2′ The mean system (gap G1)** [computed, X = 2·10⁸]: sup-slopes of Σ_{n≤y}Π_{p|n}(1 − p^{α−1}) − y/ζ(2−α): 0.117 (window range
0.113–0.127) for α = 0.6; 0.247 (0.247–0.298) for α = 0.75; 0.390 (0.390–0.451) for α = 0.9. Predicted by the explicit-formula heuristic:
α − ½ = 0.10, 0.25, 0.40; the contour bound 1/(4 − 2α) = 0.357, 0.400, 0.455 is far above at α = 0.6, 0.75. So G1 (T(y) ≪ y^{α/2+ε}) is
strongly supported at α = 0.6 (0.12 vs α/2 = 0.30); at α = 0.75, 0.9 the top window [10⁷, 2·10⁸] drifts up (0.298, 0.451), still
≤ α/2 within the noise of a 1.3-decade window. Its proof is the open analytic step (§4.4).
(iv) *BDR's own deleted set is of Theorem-C type.* The Broucke–Vindas selection has π_S(x) − F(x) = O(1) (BDR, z-02 lines 1117–1118:
"the counting function of the sequence p_j is at most 1 apart from F"), and the transfer measure dE moves each excess q_j^{α−1} ≤ 1 to the
next prime, so ∫₁^x u^{α−1}dE(u) = O(1) as well: c = 1, θ = 0. Hence BDR's unpadded Section-5 systems satisfy β ≥ α/2 unconditionally,
and their hyperbola exponent 2α/(α + 2) sits between this lower bound and ½. (Their low-discrepancy random selection has tiny
fluctuation — each P_j is random only inside an interval of F-mass 1 — so it behaves like the greedy set of §6.3, not like T_α.)
