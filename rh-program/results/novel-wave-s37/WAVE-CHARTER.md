# NOVEL-APPROACH WAVE 2 (Session 37, 2026-09-30) — charter and seed briefs

Orchestrator: Fable 5.1. Agents: Opus, default effort (standing orders 11, 12). Standing orders 0, 1, 5, 7, 10, 12 and KICKSTART 10(a)–(o), 16 bind.
Each seed writes `results/novel-wave-s37/<seed>/{NOTE.md, SHARED.md, verify/, sources/}` and closes T (theorem) / G (alive, one named gap) /
K (killed by a theorem or a counterexample) / N (nothing, correctly). A narrative close is returned.

## 0. Where this wave starts (binding inputs — read the four `read-F.md` files of `results/novel-wave-s36/*/` first)

Wave 1 closed N1 K, N2 K, N3 K, N4 N, all upheld at the line in Session 37. What they fixed:
 (a) Prime channels ADD zero density (N1 Theorem K); ξ's zero density is archimedean; primes must enter with zero net winding — through the phase of
     an OUTER function on Re s > ½ — and "outer" is RH restated. (b) No prime-by-prime positivity induction: ζ's Euler factor sits on the destroying side
     of the Hasse bound by (√p − 1)² (N3 Theorem D). (c) Approximation staircases are height filtrations (N2 Prop. F); no early warning (N2, N3).
 (d) N4's four survivor properties: consume Λ ≥ 0 JOINTLY with the functional equation (FE); act globally; survive divergent prime mass;
     FAIL on the rung-1 twin. (e) THE RUNG-1 TWIN (new control, N4 DD1): the virtual curve Z(u) = (1 − 5u + 5u²)/((1 − u)(1 − 5u)) over F₅ — rational,
     FE, nonnegative integer point counts N_n and closed-point counts b_d (checked to d = 60), an Euler product with STANDARD local factors, class number 1,
     Riemann–Roch-consistent divisor counts A_n = (5ⁿ − 1)/4 — and zeros at Re s = 0.79899. So no "zeta-level" axiom set implies RH on rung 1.
 (f) Over Q the record's RH-false worlds all fail an axiom: Davenport–Heilbronn and Epstein (h > 1) have no Euler product and Λ < 0 somewhere;
     F_{a,q} has Λ(q²) < 0; Beurling systems (zoo I.2) have Euler product and Λ ≥ 0 but no FE and integer error exponent β ≥ ½. [CORRECTION 2026-10-01, Session 39 (insertion-only; the sentence stands as history) — the wave-2 digest, `results/novel-wave-s37/insights-digest.md` §E, E.2(e): "integer error exponent β ≥ ½" "is imprecise: {α > ½, β < ½} is populated under RH (BDR Thm 1.3) and, non-constructively, unconditionally (Prop. 2.1)" — Prop. 2.1 of `results/novel-wave-s37/beurling-frontier/NOTE.md`.]
The orchestrator's reading (Session 37; single-check, to be attacked): RH needs the MULTIPLICATIVE structure (Euler product, Λ ≥ 0) and the ADDITIVE
structure of N (equally spaced integers; Poisson summation; the FE) together. Beurling systems are exactly "multiplicative structure with the additive
structure relaxed", and the integer error exponent β (N_B(x) = ρx + O(x^β)) measures how additive a system is: N has β = 0 and an exact FE.
The record has never asked how much additivity forces RH. Seeds M1a, M1b ask it from both ends; M2 mines rung 1 for the separating inputs.

## Seed M1a `beurling-fe` — is Spec Z rigid among Beurling systems with Riemann's functional equation? (the rung-Z twin question)

QUESTION. Does there exist a Beurling generalized prime system P = {1 < p₁ ≤ p₂ ≤ …} ⊂ R, other than the rational primes, whose zeta
ζ_P(s) = Π(1 − p_j^{−s})^{−1} = Σ n_k^{−s} satisfies Riemann's FE exactly: π^{−s/2}Γ(s/2)ζ_P(s) invariant under s ↦ 1 − s, meromorphic with poles only at 0, 1?
 (1) Reformulate: FE ⟺ θ_P(x) = Σ e^{−πn_k²x} obeys Riemann's theta relation ⟺ the even measure μ = δ₀ + Σ_k(δ_{n_k} + δ_{−n_k}) is a tempered
     distribution equal to its own Fourier transform (a self-dual crystalline measure with positive integer masses whose support is ± a free
     multiplicative semigroup). Prove the equivalences with exact hypotheses.
 (2) PRIOR-ART GATE FIRST (standing order 1; read at the page, quote): on disk — Hilberdink–Lapidus 2006 (`fetched*/p3-22c1-…`: "characterise the existence
     of a suitable generalised functional equation"), Hilberdink 2012 periodic counting (`p3-22c2-…`), Hilberdink 2005 (`w-18a`), DMV (`fetched/p1-02`),
     the N1 sources folder `results/novel-wave-s36/ly-infinity/sources/` (Lev–Olevskii u-30b, Kurasov–Sarnak u-20b, Olevskii–Ulanovskii p2-19b, Meyer u-25a,
     Favorov, Gonçalves), Nakamura 2008.02570 and Burnol 1106.4749 (Hamburger); fetch if needed (arXiv): Bochner–Chandrasekharan, Chandrasekharan–Mandelbrojt,
     Kahane–Mandelbrojt 1958, Lagarias "Beurling generalized integers with the Delone property" (1999), Olofsson 2011, Broucke–Debruyne–Révész 2309.01567.
     State exactly what is already a theorem. If the question is settled in print, the close is N with the citation, and the unit moves to (5).
 (3) The uniformly discrete case: a proof or a disproof of rigidity (expected tools: Lev–Olevskii; Serre–Stark for weight ½; positivity + free generation).
 (4) The non-uniformly-discrete case: construct or refute. Translation-boundedness follows from positivity + self-duality (prove). Try to build an
     exotic system numerically (a search over finite truncations with the theta relation as a least-squares constraint is a legitimate experiment —
     but a numerical near-solution is not an example; say which).
 (5) Relaxations, each to a verdict: continuous Beurling prime measures (orchestrator's sketch, check it: ζ·G with G(s) = Π(s − ρ_j)/Π(s − a_j) symmetric,
     ρ_j an off-line quadruple, a_j real poles in (β₀, 1): the prime measure stays ≥ 0 and the FE is exact, at the price of real poles in the strip —
     is an ENTIRE completed function possible? the orchestrator's Phragmén–Lindelöf argument says G entire of finite order ⟹ G ≡ 1 only when G = ζ_P/ζ is
     entire, which is not automatic); FE with a conductor; FE up to a finite Euler factor.
 CONTROLS: the virtual curve (rung 1: exact FE, standard local factors, RH false — what is the function-field analog of the rigidity, and why does it fail
 there?); F_{5,5} = ζ(s)(1 + 5·5^{−s} + 5^{1−2s}) (nonnegative INTEGER coefficients, FE of conductor 25, RH false, but Λ(25) < 0: not a free semigroup).
 CLOSE: T = a rigidity theorem with proof and exact scope ("Hamburger for Beurling zeta functions"), or K-by-example = an exotic system (a new control:
 Euler product + Λ ≥ 0 + exact FE, with RH false or undetermined), or G with the one missing lemma.
 Stop and report when: a printed theorem settles (3)–(4) (quote it), or a verified exotic system is in hand.

## Seed M1b `beurling-frontier` — does integer regularity below the square-root barrier force RH? (the (α, β) frontier under ½)

DEFINITIONS (Hilberdink; zoo I.2(b)): an [α, β]-system has ψ_P(x) = x + O(x^{α+ε}) and N_P(x) = ρx + O(x^{β+ε}), exponents sharp. Known (read at the page
first: Hilberdink 2005 `w-18a`; Broucke–Debruyne–Révész arXiv:2309.01567; Broucke–Vindas 2102.08478; zoo I.2): max{α, β} ≥ ½; every α ∈ [0, 1), β ∈ [½, 1)
is populated; N is a [Θ, 0]-system. The region β < ½ is the frontier. QUESTION: for which β < ½ do RH-false systems (α > ½) exist? If a threshold β* > 0
existed below which α = ½ is forced, RH would be the case β = 0 of a Beurling-type theorem.
 ORCHESTRATOR'S PRE-DERIVATION (single-check; attack it first, it may be wrong or already in print): "sparse random surgery on the primes". Fix
 ρ₀ = β₀ + iγ₀, ½ < β₀ < 1, and G(s) = (s − ρ₀)(s − ρ̄₀)/s². Then log G(s) = ∫₁^∞ x^{−s} dν(x) with density (2/x − 2x^{β₀−1}cos(γ₀ log x))/log x —
 of relative size O(x^{β₀−1}) against the prime density. Remove actual primes and add generalized primes at random with E[added − removed] = dν
 (possible for x large since 2x^{β₀−1} < 1; finitely many small primes handled by hand). Then ζ_P = ζ·G·e^{h} with h a random Dirichlet series that
 converges a.s. and is analytic for Re s > β₀/2 (variance Σ x^{β₀−1−2σ}); so ζ_P has the zero ρ₀ (α ≥ β₀ > ½, unconditionally), and the modification
 has only ≈ x^{β₀} atoms below x, so the integer error should be ≈ x^{β₀/2+ε} by square-root cancellation in Σ_m c_m{x/m} — NOT the x^{1/2} noise of a
 full discretization. Predicted: [α, β] = [β₀, β₀/2]-systems for every β₀ ∈ (½, 1): RH-false systems with integers MORE regular than the square-root
 barrier, filling ¼ < β < ½; and nothing below ¼ by this method.
 TASKS: (1) prior art — is the region β < ½ populated in print, conditionally or not (BDR's "only under RH" — read what exactly)? (2) prove or refute the
 pre-derivation: the a.s. analyticity of h; the zero; the bound N_P(x) − ρx ≪ x^{β₀/2+ε} a.s. (the hard step: uniform-in-x cancellation in sawtooth sums
 over a random multiplicative measure; a truncated-Perron route needs growth of ζ(σ+it)e^{h} — say which route works); (3) SIMULATE: build the surgery
 for β₀ = 0.6, 0.75, 0.9 (primes to ≥ 10⁷, several seeds), compute N_P(x) exactly, fit the error exponent, report with error bars; control: the same code
 on the unmodified primes returns β = 0 and on a full random discretization returns ½; (4) the frontier: can STRUCTURED (non-random) surgery beat β₀/2?
 Is there an obstruction of the form β ≥ f(α) > 0 for α > ½ — prove one or exhibit the mechanism that evades it (Hilberdink's periodic systems; F_{5,5}
 has bounded-type error with RH false but is not free — how close to free can such a system be made?); (5) state the sharpest conjecture the data support.
 CONTROLS: rung 1 (the virtual curve: perfect integer regularity, RH false — so no threshold theorem can be "formal"; what archimedean input would it need?).
 CLOSE: T (a theorem populating a region with β < ½, or an obstruction β ≥ f(α)), K (the pre-derivation refuted, with the reason), G, or N (in print).
 Stop and report when: the region is found populated in print (quote it), or the simulation contradicts the prediction at all three β₀.

## Seed M2 `proof-mine` — the virtual-curve line in every proof of RH for curves

For EACH known proof of the Riemann hypothesis for curves over finite fields (at least: Weil via correspondences/Castelnuovo–Severi; Mattuck–Tate–Grothendieck
via the Hodge index on C × C; Weil's Jacobian/Rosati proof; Hasse for genus 1 (degree of isogenies); Stepanov; Bombieri's Riemann–Roch form of Stepanov;
Deligne (Weil I: Lefschetz pencils, monodromy, Rankin squaring); Deligne–Laumon/Katz (Fourier transform, Weil II); p-adic (Dwork/Kedlaya: only if a
complete proof of RH for curves is in print — check); any proof via modular/automorphic methods for special curves; Connes–Consani–Marcolli's translation;
Hrushovski's difference-field route — check what it proves), find the EXACT LINE at which the virtual curve (q, a) = (5, 5) cannot be substituted: which
object is asked for that a formal zeta function does not supply, stated as a lemma ("the proof uses X; the virtual curve has no X because Y").
 Sources: read at the page (corpus folders `fetched*/` — grep the routing file `results/corpus-routing.md`; Milne's notes and Bombieri's Bourbaki talk may be
 on disk; fetch arXiv/free texts otherwise; label anything not read `[recalled, unverified]`). For each separating input X give: (i) its analog over Z on
 the program's record (SPEC A1–A13 in `results/f1-spec-s29/` or wherever `grep -rl "A13" results` finds it; zoo IV.20, Theorem S in
 `results/d4-infty-s36/NOTE.md`; zoo III.14, III.20), (ii) whether the analog exists, is refuted, or is unbuilt, (iii) the cheapest construction-or-refutation
 unit that would decide it. Then the THEOREM-SHAPED CLOSE: a partition of the proofs by separating input (expected: a surface with Riemann–Roch; a family
 with monodromy; honest sections + a Frobenius endomorphism; a group law), with a proof that each class's input is NOT a function of the zeta function
 alone (the virtual curve is the witness), and the one input — if any — whose Z-analog is not already dead on the record.
 CONTROLS: a genuine curve with the same (q, g) (e.g. an elliptic curve over F₅ with a = 4) must pass every line the virtual curve fails.
 CLOSE: T (the partition theorem + the table), G (one input with a live Z-analog and its named gap), or N.
 Stop and report when: a proof is found that the virtual curve passes (that would be an error in the control or a false proof — report at once).

## Rules for every seed

Ladder (10(b)): rung 1 first where a rung exists; controls are mandatory and their outputs are printed. Every computation is a script in `verify/` with its
log. Every quoted source is on disk under `sources/` with page or line. Recalled statements are labeled and never load-bearing (standing order 5).
Novelty claims are `[novelty: single-check]`. Nearest published object for every new definition (10(n)). SHARED.md gets a dated block after each batch.
Do not run git. At most one CPU-heavy process at a time per agent. Paths contain spaces: quote them.
