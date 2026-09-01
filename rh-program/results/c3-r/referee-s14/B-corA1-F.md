# REFEREE REPORT F — probe B, Corollary A.1, the converse inclusion cl(γ) ⊆ Γ^E_p

**Program:** RH program, direction C3-r (geometric substrate, reduced recommission). **Session 14, 2026-09-02.**
**Referee:** F (model Claude Fable 5.1), one of two independent referees on this item under standing order 7; nothing from the other referee was seen, and nothing below is softened in the expectation that the other check will catch it.
**Item:** `results/c3-r/probe-9.3-b.md`, Corollary A.1, the parenthetical converse inclusion ("packets are exactly the orbit closures"); the debt recorded in `results/c3-r/probe-9.3-adjudication.md` §4 item 6 and §5 Q-c.
**Rules applied:** standing order 5 — every statement about a source below was read this session from the on-disk PDF at the stated printed page (text layer extracted with `pdftotext -layout`; all four files have clean LaTeX text layers; page numbers were verified against the page-break markers in the extraction). Nothing recalled from memory is load-bearing; the single recalled item is marked [RU]. The pass is a line-by-line re-derivation (§3), not an audit around the note. No probe note or direction file was edited.
**Companion files:** `B-corA1-F-checks.py` / `B-corA1-F-checks.json` (finite-truncation sanity checks of three elementary inputs; they prove nothing and are cited only where the derivation names them).

---

## 0. Verdict, stated first

**PASS-WITH-REPAIRS.** The converse inclusion is **TRUE**, and in a form stronger than the note states. For X₀ = Spec Z, C = ℂ, N₀ = N, every admissible class E (Def. 4.1 of [x-03]), every prime p, and every periodic orbit γ ⊂ Γ^E_p:

> **cl_{X₀}(γ) = Γ^E_p,**

where the closure is taken in the suspension X₀ = X̌₀(C)^E ×_{Q>0} R>0 with the quotient topology of X̌₀(C)^E × R>0, the equality holds in every chart F_ν⁻¹(X•₀(C)^E) of the colimit, and cl(γ) meets no other stratum of X₀ (neither the generic-point stratum nor any packet Γ_ℓ, ℓ ≠ p), so the note's hedge "cl(γ) ∩ (char-p part)" is unnecessary.

The note's one-sentence argument, however, is not a proof of this. It correctly identifies the upstairs limit set (the exponent orbit closes up to Ẑ_{(p)}), but:

- **F1 (MAJOR):** its criterion for which limits "leave the space" — "limits with some component of b equal to 0" — is incomplete; limits whose exponent b has every component nonzero but infinitely many non-unit components also violate (Tors) and are not accounted for. The correct criterion is b ∈ N·Ẑ×_{(p)}. The conclusion survives (those limits leave too), but the sentence as written does not yield the equality.
- **F2 (MAJOR):** the sentence computes a closure upstairs at a fixed prime x, in X•(C); the closure that is claimed is in X₀. The three reductions that connect them — the suspension quotient (open map), locality in the colimit charts, and Galois descent through X•(C) → X•₀(C) — are absent. Each is elementary; all three are supplied in §3 with replacement text in §4.
- **F3–F5 (MINOR):** the redundant hedge; a wrong internal cross-reference ("Step 5's converse inclusion"); a citation improvement for the topology on X₀.

Nothing adjudicated in Session 8 changes. One banked sentence of the adjudication (§4 item 1, "packets are minimal sets") silently used the closedness of Γ^E_p, i.e. this converse; it is now certified (§3.9).

---

## 1. The item under review, verbatim

Probe B, `probe-9.3-b.md` §5, Corollary A.1 (read in full this session):

> "**Corollary A.1 (packets are minimal sets; the "invariant tori" made precise).** Every orbit of Γ^E_p is dense in Γ^E_p; Γ^E_p is the orbit closure of each of its points and is the smallest closed invariant set containing any one of its orbits. (With Step 5's converse inclusion — every limit of {F_n(P₀)}_n along any subnet is P₀^b for some b ∈ Ẑ_{(p)}, by compactness of Ẑ_{(p)} and the same pointwise evaluation; limits with some component of b equal to 0 kill a μ_{ℓ^∞} and violate (Tors), so they leave the space — one gets cl(γ) ∩ (char-p part) = Γ^E_p exactly. Stated proposition-grade; the kill only needs ⊇.)"

Probe B §7, Q-c:

> "**Q-c (bookkeeping).** Whether the equality cl(γ) = Γ^E_p of Cor. A.1 holds verbatim in every chart of the colimit (the ⊇ of Theorem A suffices for everything above; the ⊆ was argued at proposition grade)."

Adjudication §4 item 6: "Checked at proof-sketch level against the sources, not line-by-line: ... probe B's Cor. A.1 converse inclusion (flagged proposition-grade by B itself; not load-bearing). Before any external circulation, Theorem B(b) and Cor. A.1 owe a dedicated referee pass; nothing in the adjudicated verdicts rests on them." Adjudication §5: "Q-c (probe B, bookkeeping): whether cl(γ) = Γ^E_p exactly (the ⊆ direction) — proposition-grade, not load-bearing, optional."

The note's own §3.1 fixes the topological conventions it uses: "X̊(C) ... carries the topology of pointwise convergence ...; X̊₀(C) = X̊(C)/G (quotient topology, metrizable, Cor. 7.8); X̌₀(C) = colim_N X̊₀(C) with the inductive limit topology, which agrees with the subspace topologies and in which each chart F_ν⁻¹(X̊₀(C)) is open (Prop. 7.4 and the paragraph after Cor. 7.9, p. 46); the E-subspaces carry subspace topologies (p. 46); the suspension X₀ carries the quotient topology (implicit throughout §§8, 10 ...)." These conventions are checked against the source in §2 and used in §3.

The five questions the task poses: (1) the exact topology on X₀ in which closures are taken; (2) whether "pointwise convergence of characters" describes it on the char-p stratum and on the whole space, and whether the colimit topology could be finer; (3) whether a limit with a zero component is excluded by (Tors), by E, or by the topology, and whether that matters for closures in X₀; (4) whether cl(γ) can meet other strata; (5) the exact scope of what is proved. They are answered in §3.1, §3.5, §3.6, §3.8 and §6 respectively.

---

## 2. Source anchors (printed pages; quoted verbatim from the on-disk PDFs)

Notation of the source: Deninger writes a dotted X(C) for the space of pairs (x, P×); this report writes **X•(C)**, **X•₀(C)** for the dotted spaces and X̌(C), X̌₀(C) for the colimits, as the note does with X̊.

### 2.1 [x-03] C. Deninger, *Dynamical systems for arithmetic schemes*, arXiv:1807.06400v4, `fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf` (119 pp.)

- **A1 (p. 22, §3).** "Let C be an algebraically closed field. We define X•(C) to be the set of pairs (x, P×) where x ∈ X and P×: κ(x)× → C× is a homomorphism. The group G acts on X•(C) from the right by (x, P×)σ = (x^σ, P× ∘ σ) for σ ∈ G. The G-action commutes with the N-action by F_ν(x, P×) = (x, P× ∘ ( )^ν) for ν ∈ N. Hence the quotient X•₀(C) = X•(C)/G inherits an N-action." — *No condition on P× at this level; (Tors) enters only with E in §4.*
- **A2 (p. 23, Remark 3.4).** "If X₀ = spec R₀ is affine, X = spec R, we will identify the points (x, P×) of X•(C) with the multiplicative maps P: R → C satisfying the following properties: 1) P(0) = 0, P(1) = 1. 2) p := P⁻¹(0) is additively closed and hence a prime ideal. 3) We have a factorization P: R → R/p → C."
- **A3 (p. 24).** "X̌(C) = colim_{N₀} X•(C) and X̌₀(C) = colim_{N₀} X•₀(C). ... Note that X•(C) ⊂ X̌(C) and X•₀(C) ⊂ X̌₀(C) canonically since the F_ν's are injective. We can write the points of X̌(C) in the form F_ν⁻¹P for some ν ∈ N₀ and P in X•(C)."
- **A4 (p. 27, §4).** "(Tors) the group ker(χ)_tors = ker(χ|_{μ(κ)}) is finite and |(ker χ)_tors| ∈ N₀." — "Definition 4.1. A class E of characters χ: κ× → C× on algebraically closed fields κ is (N₀−)admissible if for any σ ∈ Aut κ resp. ν ∈ N₀ the character χ is in E if and only if χ ∘ σ resp. χ^ν = χ ∘ ( )^ν is in E. Moreover the characters in E should satisfy (Tors)." — "Proposition 4.2. ... X•(C)_E ... is G-invariant. It is foreward- and backward invariant under the N₀-action, i.e. for P ∈ X•(C) we have P ∈ X•(C)_E if and only if F_ν(P) ∈ X•(C)_E. The set X̌(C)_E = colim_{N₀} X•(C)_E ⊂ X̌(C) is G- and Q>0₀-invariant."
- **A5 (pp. 31–33, §5).** p. 31: "C_{x₀} = pr₀⁻¹(x₀)Q>0₀ = ⋃_{ν∈N₀} F_ν⁻¹ pr₀⁻¹(x₀) ⊂ X̌₀(C)_{Etors}." p. 32: "The fibre pr₀⁻¹(x₀) consists of the G-orbits of all pairs (x, P×) where x is a point of X over x₀ and P×: κ(x)× → C× satisfies (Tors). Since κ(x)× is torsion this means that ker P× = (ker P×)_tors is finite hence cyclic and |ker P×| ∈ N₀. Given x and composing the fixed injection ι: μ(K) ↪ μ(C) above with (32) we obtain the injective character χ_x = ι ∘ i_x⁻¹: κ(x)× ↪ C×". p. 32, (34): "N x₀^Ẑ = Gal(κ(x)/κ(x₀)) ↪ Aut(κ(x)×) = Ẑ×_{(p)}. Here on the left, N x₀ corresponds to the Frobenius automorphism y ↦ y^{N x₀}". p. 32, (35): "The monoid Ẑ×_{(p)} × N₀ acts by pre-composition on the set S of homomorphisms P×: κ(x)× → C× with finite cyclic kernel of order in N₀. We have a Ẑ×_{(p)} × N₀-equivariant surjection: Ẑ×_{(p)} × N₀ ↠ S, (a, ν) ↦ χ_x · (a, ν) := χ_x ∘ ( )^a ∘ ( )^ν. Two elements (a, ν) and (a′, ν′) are in the same fibre of this map if and only if ν′ = νp^n and a = p^n a′ for some n ∈ Z." p. 32, (36): "S/N x₀^Ẑ → pr₀⁻¹(x₀), P× mod N x₀^Ẑ ↦ π((x, P×))". p. 32, (38): "(Ẑ×_{(p)}/N x₀^Ẑ) ×_{pZ} Q>0₀ → C_{x₀}" (Q>0₀-equivariant bijection), and "It follows that all points P₀ ∈ C_{x₀} have isotropy subgroup (Q>0₀)_{P₀} = N x₀^Z." p. 33, after (39): "The set C_{x₀} fibres over the compact group Ẑ×_{(p)}/p^Ẑ = Aut(F̄_p)/Aut(F_p)^, and the fibres are the Q>0₀-orbits in C_{x₀}."
- **A6 (p. 34, Theorem 5.2).** "{P₀ ∈ X̌₀(C)_E | (Q>0₀)_{P₀} ≠ 1} = ∐_{x₀} C^E_{x₀}. For any point P₀ ∈ C^E_{x₀} the isotropy group of P₀ is (Q>0₀)_{P₀} = N x₀^Z where N x₀ = |κ(x₀)|. If e.g. E ⊃ E_f then C^E_{x₀} = C_{x₀}."
- **A7 (p. 38, §6).** "X₀ = X̌₀(C)_E ×_{Q>0₀} R>0. It is the quotient of X̌₀(C)_E × R>0 by the right Q>0₀-action given by (P₀, u)q = (P₀q, q⁻¹u) = (F_q(P₀), q⁻¹u) for q ∈ Q>0₀. The Q>0₀-orbit of (P₀, u) is denoted by [P₀, u]. The group R>0 acts on X₀ via the second factor: [P₀, u]·v = [P₀, uv]." — "Γ_{x₀} = C_{x₀} ×_{Q>0₀} R>0 ⊂ X₀. The Q>0₀-bijection (39) induces an R>0-bijection (Ẑ×_{(p)}/N x₀^Ẑ) ×_{pZ/deg x₀} R>0/N x₀^Z → Γ_{x₀}. Thus all R>0-orbits in Γ_{x₀} are circles R>0/N x₀^Z and Γ_{x₀} fibres over Ẑ×_{(p)}/p^Ẑ = Aut(F̄_p)/Aut(F_p)^ with fibres the R>0-orbits in Γ_{x₀}. We set Γ^E_{x₀} = C^E_{x₀} ×_{Q>0₀} R>0 where C^E_{x₀} = C_{x₀} ∩ X̌₀(C)_E. If e.g. E_f ⊂ E then Γ^E_{x₀} = Γ_{x₀}." — *§6 places no topology on X₀.*
- **A8 (p. 39, Theorem 6.1; p. 40).** "{x₀ ∈ X₀ | (R>0)_{x₀} ≠ 1} = ∐_{x₀} Γ^E_{x₀}. For any point x₀ ∈ Γ^E_{x₀} the isotropy group of x₀ is (R>0)_{x₀} = N x₀^Z." p. 40: "Is there a sub-dynamical system Y₀ ⊂ X₀ = X̌₀(C) ×_{Q>0} R>0 or at least one which maps to X₀ such that dim Y₀ = 2d + 1 ...".
- **A9 (p. 40, §7 opening).** "Viewing X•(C) as a set of multiplicative maps P: R → C as in Remark 3.4 we give X•(C) the topology of pointwise convergence. It is the subspace topology induced by the Tychonov topology of C^R = ∏_R C on X•(C) via the inclusion X•(C) ⊂ C^R, P ↦ (P(r))_{r∈R}. Since R is countable, X•(C) is a metrizable topological space."
- **A10 (p. 40, Lemma 7.1).** "For affine arithmetic schemes X₀, the natural map pr_X: X•(C) → X, (x, P×) ↦ x or P ↦ p = P⁻¹(0) is continuous."
- **A11 (p. 42, Lemma 7.3).** "the group G acts by homeomorphisms on X•(C) and the injective maps F_ν: X•(C) ↪ X•(C) for ν ∈ N are continuous, closed and open. In particular F_ν(X•(C)) is closed and open in X•(C)." Proof, (51): "F_ν(X•(C)) = {P ∈ X•(C) | P(μ_ν(K)) = 1}"; "it follows that F_ν induces a homeomorphism onto its image F_ν(X•(C))."
- **A12 (p. 43).** "We give X̌(C) = colim_{N₀} X•(C) the inductive limit topology. It is the finest topology such that for all ν ∈ N₀ the inclusions F_ν⁻¹|_{X•(C)}: X•(C) ↪ X̌(C) (53) are continuous. Thus Z ⊂ X̌(C) is closed, resp. open if and only if F_ν(Z) ∩ X•(C) is closed, resp. open in X•(C) for all ν ∈ N₀." — "Proposition 7.4. a) X•(C) is a closed and open subspace of X̌(C). b) F_q: X̌(C) → X̌(C) is a homeomorphism for every q ∈ Q>0₀. c) The group G acts by homeomorphisms on X̌(C)." — "We give X̌₀(C) = X̌(C)/G the quotient topology. Then X̌₀(C) is homeomorphic to colim_{N₀} X•₀(C) with the inductive limit topology. The projections π: X•(C) → X•₀(C) and π̌: X̌(C) → X̌₀(C) are continuous and since G acts by homeomorphisms, also open. Moreover the projections pr_X: X̌(C) → X and pr_{X₀}: X̌₀(C) → X₀ are continuous."
- **A13 (p. 44, Props. 7.5–7.7).** "Proposition 7.5. Let X₀ be an arithmetic scheme. Then the right-action map X•(C) × G → X•(C) is continuous." — "Proposition 7.6. For affine arithmetic schemes X₀ = spec R₀, the space X•(C) carries a G-invariant metric inducing the topology." — "Proposition 7.7. Let (X, d) be a metric space with an action of a compact group G of isometries and such that the maps G → X, σ → x^σ are continuous for all x ∈ X. Then we obtain a metric δ on X/G by setting δ(xG, yG) = min_{σ,τ} d(x^σ, y^τ) = min_σ d(x^σ, y) = min_τ d(x, y^τ). The metric δ induces the quotient topology. In particular X/G is Hausdorff."
- **A14 (p. 45, Cors. 7.8–7.9).** "The topological space X•₀(C) is metrizable and separable and in particular Hausdorff." — "Corollary 7.9. Let X₀ be an arithmetic scheme which carries an ample invertible sheaf. Then the spaces X•(C), X•₀(C), X̌(C) and X̌₀(C) are Hausdorff."
- **A15 (pp. 46–47).** Theorem 7.10 (p. 46): "The following canonical R>0-equivariant maps are continuous bijections: ... → X = X̌(C)_{Etors} ×_{Q>0₀} R>0 and ... → X₀ = X̌₀(C)_{Etors} ×_{Q>0₀} R>0." — *This is the first place in [x-03] where the suspension is treated as a topological space.* Remark 2 (p. 47): "The continuous bijections in Theorem 7.10 are not homeomorphisms in general." p. 47: "Given an admissible class E as in Definition 4.1 we equip X•(C)_E and X•₀(C)_E with the subspace topologies of X•(C) and X•₀(C). ... We give X̌(C)_E = colim_{N₀} X•(C)_E and X̌₀(C)_E = colim_{N₀} X•₀(C)_E the inductive limit topologies. They agree with the subspace topologies via X̌(C)_E ⊂ X̌(C) and X̌₀(C)_E ⊂ X̌₀(C) because the subspaces F_ν⁻¹X•(C) and F_ν⁻¹X•₀(C) are open in X̌(C) resp. X̌₀(C) for all ν ∈ N₀. As above, the natural continuous bijection X̌(C)_E/G → X̌₀(C)_E is a homeomorphism. All preceding results in this section remain true if we replace X•(C) etc. by X•(C)_E etc."
- **A16 (p. 49, end of §7).** "The Q>0-action on Ȟ_{Etors} × R>0 is not properly discontinuous. In section 10, we will see that this works to our advantage."
- **A17 (pp. 49–50, §8).** "one idea would be to replace X₀ by the dynamical system Y₀ obtained as the topological closure of the union of all periodic orbits coming from closed points of X₀. In this section we will show that the system Y₀ is still infinite-dimensional". Theorem 8.2 (p. 50): "X̌(C)_per‾ = X̌(S¹) and X̌₀(C)_per‾ = X̌₀(S¹)."
- **A18 (p. 53, Proposition 9.1 and proof).** "X•(C)′ is the topological closure of X•(C)_{Etors} in X•(C)." Proof: "If P_n ∈ X•(C)′ converge to P ∈ X•(C) and if P(ζ) = 1 for some ζ ∈ μ_N(R) then P_n(ζ) = 1 for all n ≫ 0 since μ_N(C) is discrete in C×." — *Deninger's own use of the discreteness-of-roots-of-unity mechanism that drives §3.5 below.*
- **A19 (pp. 60–61, §9/§10 boundary).** "Incidentally, note that the quotient topology on pr_{X₀}⁻¹(η₀) = pr_X⁻¹(η)/G equals the subspace topology within X̌₀(C)_E, the latter being equipped with the quotient topology via X̌₀(C)_E = X̌(C)_E/G."
- **A20 (pp. 2–3, introduction).** "the closed points x₀ of X₀ correspond bijectively to compact packets Γ_{x₀} of periodic orbits of length log N x₀ on X₀ = X̌₀(C) ×_{Q>0} R>0. ... Each periodic orbit of X₀ lies in exactly one packet Γ_{x₀}. ... The compact packets Γ_{x₀} are reminiscient of invariant tori."

### 2.2 [x-06] C. Deninger, *Primes, knots and periodic orbits*, arXiv:2301.11643, `fetched/x-06-deninger-2024-primes-knots-and-periodic-orbits.pdf`

- **B1 (p. 11).** "Set X₀ = (X̌₀(C) × R>0)/Q>0 where Q>0 acts diagonally. Let t ∈ R act on X₀ by setting φ^t[P, u] = [P, e^t u]." — *The suspension as a set-quotient; no topology sentence.*
- **B2 (p. 12, Theorem 4.2).** "The compact subsets Γ_{x₀} ⊂ X₀ consist of periodic orbits of length log N x₀ where N x₀ = |κ(x₀)| ... and they are pairwise disjoint. In fact Γ_{x₀} is a fibre space over the compact group Aut(F̄_p)/Aut(F_p)^ where p = char κ(x) with fibres the compact orbits in Γ_{x₀}."

### 2.3 [r3s-08] M. Morishita, arXiv:2508.15971v5, `fetched-r3/r3s-08-morishita-deninger-cc-bridge-2508.15971.pdf`

- **C1 (p. 12).** "By Proposition 2.1.6, we can define a topology on Ẋ_Q(C). Namely, since Ẋ_Q(C) is the set of multiplicative maps, we equip it with the topology of pointwise convergence."
- **C2 (p. 13).** X̌_K(C) "equipped with the inductive limit topology".
- **C3 (p. 14).** "We equip X_K twith he quotient topology of the product X̌_K(C) × R₊." (sic — the transposition is in the source) — *the only explicit sentence in the primary corpus fixing the topology of the suspension.*
- **C4 (pp. 17–18, Theorem 2.2.9).** "(1) We have the Q₊-equivariant homeomorphism Ẑ×_{(p)}/Np^Ẑ ×_{pZ} Q₊ → C_p, and the R₊-equivariant homeomorphism Ẑ×_{(p)}/Np^Ẑ ×_{pZ} R₊ → Γ_p" (p. 17); "(2) ... So γ_{p,a} is a circle of length log Np and we have the decomposition into connected closed R₊-orbits Γ_p = ⊔_{a ∈ Ẑ×_{(p)}/p^Ẑ} γ_{p,a}" (p. 18).

### 2.4 [D25] C. Deninger, *Rational Witt vectors and associated sheaves*, arXiv:2508.05329v1, `fetched-r3/r3s-22-...pdf`

- Read: title page and introduction (pp. 1–2). The paper concerns sheaf properties of W_rat on various Grothendieck topologies ("In [KS16] and [Den24] using rational Witt vectors, topological spaces resp. topological dynamical systems were constructed ... The motivation for the present paper was to understand better why rings of rational Witt vectors arise at all", p. 2). A grep of the full text layer for "packet", "periodic orbit", "suspension", "Hausdorff", "closure of" returns nothing bearing on the item. **Not load-bearing here.**

### 2.5 Program files read in full
`results/c3-r/probe-9.3-adjudication.md` (107 lines); `results/c3-r/probe-9.3-b.md` (143 lines); `results/corpus-routing.md` header caveats (items 1–20).

---

## 3. Re-derivation (complete; checkable without the note)

### 3.0 Standing conventions

X₀ = Spec Z, K₀ = Q, K = Q̄, X = Spec Z̄ (Z̄ the integral closure of Z in Q̄), G = Gal(Q̄/Q), C = ℂ, N₀ = N (so Q>0₀ = Q>0), E an admissible class (A4; hence E ⊆ E_tors). Fix the closed point x₀ = (p) of Spec Z and a prime x of Z̄ above p; κ(x) = F̄_p, κ(x)× = μ^{(p)} (the prime-to-p roots of unity), a torsion group. End(μ^{(p)}) = Ẑ_{(p)} = ∏_{ℓ≠p} Z_ℓ and Aut(μ^{(p)}) = Ẑ×_{(p)} (A5, (34)). Two elementary facts about Ẑ_{(p)} used throughout:

- **(E1)** A positive integer n is a unit of Ẑ_{(p)} if and only if n is a power of p (n ∈ Z_ℓ× iff ℓ ∤ n). Consequently Ẑ×_{(p)} ∩ N = p^N, and "unit twists" and "integer Frobenius shifts" are different things: for a unit u and n ∈ N, nu is a unit iff n ∈ p^N.
- **(E2)** N is dense in Ẑ_{(p)}: for every M prime to p and every residue class mod M there is a positive integer in that class (CRT; check C1 in the companion file). Ẑ×_{(p)} = ∏ Z_ℓ× is closed in Ẑ_{(p)}.

χ := χ_x: μ^{(p)} ↪ C× is Deninger's injective reference character (A5, p. 32). For b ∈ Ẑ_{(p)} write χ^b := χ ∘ (·)^b; it is a homomorphism μ^{(p)} → C×, so (x, χ^b) ∈ X•(C) for **every** b (A1 imposes no condition). Its kernel is ker((·)^b) = ⊕_{ℓ≠p} μ_{ℓ^{v_ℓ(b)}} with v_ℓ(b) := ℓ-adic valuation of the component b_ℓ (v_ℓ = ∞ if b_ℓ = 0). Hence

- **(E3)** χ^b satisfies (Tors) ⟺ ker((·)^b) is finite ⟺ v_ℓ(b) < ∞ for every ℓ and v_ℓ(b) = 0 for all but finitely many ℓ ⟺ b ∈ N·Ẑ×_{(p)} (write b = n·u with n = ∏ ℓ^{v_ℓ(b)} ∈ N prime to p and u a unit). The second clause of (Tors), |ker| ∈ N₀, is vacuous for N₀ = N.

Maps: π: X•(C) → X•₀(C) = X•(C)/G and π̌: X̌(C) → X̌₀(C) (continuous and open, A12); the charts ι_ν := F_ν⁻¹|: X•₀(C) → X̌₀(C), ν ∈ N; the suspension quotient q: X̌₀(C)^E × R>0 → X₀, (P, u) ↦ [P, u]. For a point P ∈ X̌₀(C)^E, O(P) := {F_r P : r ∈ Q>0} is its Q>0-orbit.

### 3.1 The topology on X₀ (task question 1)

[x-03] defines X₀ as a set-quotient (A7) and from Theorem 7.10 on treats it as a topological space ("continuous bijections" into X₀, A15; "topological closure" in §8, A17) without a sentence fixing the topology. The quotient topology of X̌₀(C)^E × R>0 under q is the only topology under which A15 and A17 are meaningful, it is what the note's §3.1 assumes, and it is stated explicitly for the identical construction in [r3s-08] p. 14 (C3). **This report takes X₀ = (X̌₀(C)^E × R>0)/Q>0 with the quotient topology, X̌₀(C)^E carrying the colimit topology, which by A15 equals its subspace topology in X̌₀(C) = X̌(C)/G, and R>0 its usual topology.** Everything below is proved for that topology. (Finding F5 asks the note to add the [r3s-08] citation.)

Four general lemmas, with proofs, so that a reader needs nothing from outside this report.

**Lemma 1 (q is open).** Q>0 acts on X̌₀(C)^E × R>0 by homeomorphisms: F_r is a homeomorphism of X̌(C) (A12, Prop. 7.4 b), preserves X̌(C)^E (A4, Prop. 4.2) and is a homeomorphism of X̌(C)^E for its subspace = colimit topology (A15, last sentence); it commutes with G and π̌ is a quotient map, so F_r descends to a homeomorphism of X̌₀(C)^E = X̌(C)^E/G (continuity of F_r on the quotient follows from F_r ∘ π̌ = π̌ ∘ F_r, and likewise for F_r⁻¹); u ↦ r⁻¹u is a homeomorphism of R>0. For U open, q⁻¹(q(U)) = ⋃_{r∈Q>0} U·r is open, so q(U) is open. ∎

**Lemma 2 (closures through an open surjection).** Let f: Z → W be continuous, open and surjective. Then f⁻¹(cl A) = cl(f⁻¹A) for every A ⊆ W, hence cl A = f(cl(f⁻¹A)). Proof. f⁻¹(cl A) is closed and contains f⁻¹A, giving ⊇. If z ∉ cl(f⁻¹A), choose an open U ∋ z with U ∩ f⁻¹A = ∅; then f(U) is an open neighborhood of f(z), and f(U) ∩ A = ∅ (a point f(u) ∈ A would put u ∈ U ∩ f⁻¹A); so f(z) ∉ cl A, i.e. z ∉ f⁻¹(cl A). Apply f to both sides and use surjectivity. ∎

**Lemma 3 (closure is local on open sets).** For U open in Z and A ⊆ Z, cl_Z(A) ∩ U = cl_U(A ∩ U). Proof. ⊇ is clear. If z ∈ cl(A) ∩ U and V ∋ z is open in U, then V is open in Z, so V ∩ A ≠ ∅, and V ∩ A = V ∩ (A ∩ U) because V ⊆ U. ∎

**Lemma 4 (saturation under a compact group).** Let a compact group G act on a Hausdorff space Z with continuous action map Z × G → Z. Then AG := {a^σ} is closed for every closed A ⊆ Z, and cl(SG) = cl(S)·G for every S ⊆ Z. Proof. (z, σ) ↦ (z^σ, σ) is a homeomorphism of Z × G (inverse (w, σ) ↦ (w^{σ⁻¹}, σ)); the projection Z × G → Z is a closed map because G is compact (tube lemma); the action map is their composite, hence closed, and AG is the image of the closed set A × G. Then cl(SG) ⊆ cl(S)G because the latter is closed and contains SG, and cl(S)G ⊆ cl(SG) because each σ is a homeomorphism, so cl(S)^σ = cl(S^σ) ⊆ cl(SG). ∎

### 3.2 Normalization of the orbit and the reduction to X̌₀(C)^E

Let γ ⊂ Γ^E_{x₀} be a periodic orbit. By (38) (A5) every point of C_{x₀} is F_r(π(x, χ^a)) with a ∈ Ẑ×_{(p)} and r ∈ Q>0 (the colimit over ν of (37): (a, ν) ↦ π(x, χ^{aν}) = F_ν π(x, χ^a)). If F_r P₁ ∈ X̌₀(C)^E then P₁ ∈ X̌₀(C)^E by Q>0-invariance (A4, Prop. 4.2). In X₀, (P₁, rw)·r = (F_r P₁, r⁻¹·rw) = (F_r P₁, w), so [F_r P₁, w] = [P₁, rw]. Hence γ contains a point [P₀, 1] with

  P₀ := π(x, χ^{a₀}) ∈ X•₀(C)^E, a₀ ∈ Ẑ×_{(p)}, and γ = {[P₀, w] : w ∈ R>0} = q({P₀} × R>0).

(This is the same normalization as the adjudication's §2 step 1.) The q-saturation of {P₀} × R>0 is {(P₀, w)·r} = {(F_r P₀, r⁻¹w)} = O(P₀) × R>0. The closure of a product is the product of the closures, and cl(R>0) = R>0. By Lemmas 1 and 2 applied to q:

> **(R1)  cl_{X₀}(γ) = q( cl_{X̌₀(C)^E}(O(P₀)) × R>0 ).**

So the converse inclusion is *exactly* the statement cl_{X̌₀(C)^E}(O(P₀)) ⊆ C^E_{x₀}, because q(C^E_{x₀} × R>0) = Γ^E_{x₀} by definition (A7). Everything concerning the R>0-factor and the suspension identifications is absorbed in (R1); in particular there is no separate case "u_k → 0 or ∞", and no "subnet" bookkeeping is needed in X₀ itself.

### 3.3 The orbit chart by chart (task question 2, colimit part; Q-c)

Isotropy: F_p P₀ = P₀ in X•₀(C) (A6: isotropy p^Z; upstairs (x, χ^{a₀p}) = (x, χ^{a₀})^{Frob}, Frobenius lying in G_x by (34)). Hence O(P₀) = {F_{m/m′} P₀ : m, m′ ∈ N coprime, both prime to p}.

**Claim.** For M, M′ ∈ N coprime with p ∤ M′: F_{M/M′} P₀ ∈ X•₀(C) iff M′ = 1.
Proof. F_{M/M′}P₀ ∈ X•₀(C) means F_{M/M′}P₀ = Q for some Q ∈ X•₀(C), i.e. F_M P₀ = F_{M′} Q in X•₀(C), i.e. upstairs (x, χ^{a₀M})^σ = (y, ψ^{M′}) for some σ ∈ G and (y, ψ) ∈ X•(C) (A1). Restrict both characters to μ_{M′}(κ(y)): ψ^{M′} is trivial there; χ^{a₀M} ∘ σ is injective there, because χ is injective, σ: κ(y) → κ(x) is an isomorphism, and (·)^{a₀M} is an automorphism of μ_{M′} (a₀ is a unit at every ℓ | M′ and gcd(M, M′) = 1). So μ_{M′} = 1, i.e. M′ = 1. ∎

Since F_ν is a bijection of X̌₀(C), F_{m/m′}P₀ ∈ F_ν⁻¹(X•₀(C)) iff F_{νm/m′} P₀ ∈ X•₀(C); writing νm/m′ in lowest terms the denominator is m′/gcd(ν, m′), prime to p, so by the Claim this holds iff m′ | ν. Conversely, for m′ | ν, F_{m/m′}P₀ = F_ν⁻¹ F_{νm/m′} P₀ with νm/m′ ∈ N. Therefore

> **(R2)  O(P₀) ∩ F_ν⁻¹(X•₀(C)) = F_ν⁻¹(S),  S := O(P₀) ∩ X•₀(C) = {F_n P₀ : n ∈ N}.**

The charts U_ν := F_ν⁻¹(X•₀(C)^E) = F_ν⁻¹(X•₀(C)) ∩ X̌₀(C)^E are open and closed in X̌₀(C)^E and cover it: X•(C) is clopen in X̌(C) (A12, Prop. 7.4 a) and G-saturated, so X•₀(C) = π̌(X•(C)) is clopen in the quotient X̌₀(C); F_ν⁻¹ is a homeomorphism of X̌₀(C) (Lemma 1); X̌₀(C)^E carries the subspace topology (A15); and F_ν⁻¹(X•₀(C)) ∩ X̌₀(C)^E = F_ν⁻¹(X•₀(C)^E) by the backward N-invariance of the E-locus (A4, Prop. 4.2: if F_ν Q ∈ E then Q ∈ E). Lemma 3 on each chart, together with the homeomorphy of F_ν⁻¹, gives

> **(R3)  cl_{X̌₀(C)^E}(O(P₀)) = ⋃_{ν∈N} F_ν⁻¹( cl_{X•₀(C)^E}(S) ),**

where cl_{X•₀(C)^E}(S) = cl_{X•₀(C)}(S) ∩ X•₀(C)^E (subspace topology, A15 p. 47), and the topology of X•₀(C)^E as a subspace of the chart U_ν agrees with its topology as a subspace of X•₀(C) (a subspace of a subspace; F_ν is a homeomorphism onto its image, A11). **This settles Q-c:** whatever is established in the chart ν = 1 transports verbatim to every chart, and the closure in the colimit is the union of the chart closures. The colimit topology is *not* finer than the (quotient of the) pointwise topology on any chart — it only glues clopen charts on which it *is* that topology (A15: "They agree with the subspace topologies"). A net converging in X̌₀(C)^E is eventually inside a chart and converges there; a net converging in a chart converges in X̌₀(C)^E. The scenario the task names — a subnet limit existing pointwise but not in X₀, or conversely — cannot occur.

### 3.4 Galois descent

S = π(S̃) with S̃ := {(x, χ^{a₀n}) : n ∈ N} ⊂ X•(C), all at the *fixed* prime x. X•(C) is Hausdorff (metrizable, A9); G is compact (profinite); the action map is continuous (A13, Prop. 7.5); π is open (A12). Lemma 2 with f = π and Lemma 4:

> **(R4)  cl_{X•₀(C)}(S) = π( cl(π⁻¹ S) ) = π( cl(S̃G) ) = π( cl_{X•(C)}(S̃) · G ) = π( cl_{X•(C)}(S̃) ).**

(Equivalent route through A13, Prop. 7.7: δ(π P_k, π Q̃) → 0 iff there are σ_k with P_k^{σ_k} → Q̃; passing to a subsequence σ_k → σ in the compact G and using Prop. 7.5, P_k → Q̃^{σ⁻¹}. So a sequence converges downstairs iff a subsequence converges upstairs to a lift of the limit. This is the step the note's "along any subnet" silently needs: the sequence F_{n_k}(P₀) lives in X•₀(C), and its limits are limits of Galois-*translated* sequences upstairs; Lemma 4 is what returns them to the fixed prime x.)

### 3.5 The upstairs closure at a fixed prime (task question 2, pointwise part)

**Proposition.** cl_{X•(C)}(S̃) = K := {(x, χ^{a₀b}) : b ∈ Ẑ_{(p)}}, and β: Ẑ_{(p)} → K, b ↦ (x, χ^{a₀b}), is a homeomorphism.

Proof. (i) K ⊆ X•(C) by A1. (ii) β is continuous into C^{Z̄} (A9): for r ∈ p_x the r-coordinate of β(b) is 0 for all b; for r ∉ p_x it is χ(r̄)^{a₀b} = χ(r̄^{a₀b}), which depends only on a₀b modulo the finite order of r̄ ∈ μ^{(p)} and is therefore locally constant in b. β is injective: χ^{a₀b} = χ^{a₀b′} forces (·)^{a₀(b−b′)} = id on μ^{(p)} (χ injective), i.e. a₀(b − b′) = 0 in End(μ^{(p)}) = Ẑ_{(p)}, i.e. b = b′ (a₀ a unit). Ẑ_{(p)} is compact and X•(C) is Hausdorff, so β is a homeomorphism onto K, and K is compact, hence closed in X•(C). (iii) S̃ = β(N) ⊆ K, so cl(S̃) ⊆ K. (iv) K ⊆ cl(S̃): N is dense in Ẑ_{(p)} (E2) and β is continuous, so β(Ẑ_{(p)}) = β(cl N) ⊆ cl β(N) = cl S̃. Concretely: a basic neighborhood of β(b) is given by finitely many r₁, …, r_s ∈ Z̄ \ p_x, of orders m_i in μ^{(p)}, and finitely many r ∈ p_x; with M = lcm(m_i) (prime to p) any n ∈ N with n ≡ b (mod M) satisfies β(n)(r_i) = β(b)(r_i) *exactly* for all i, and both vanish on p_x. ∎

Three remarks that answer question 2 in the form the note needs.

(a) *Pointwise convergence is exactly the topology on the chart* (A9), but of multiplicative maps on all of Z̄ (A2), not of characters of a fixed κ(x)×. It is the vanishing locus that pins a limit to the same prime: if P_k → P in X•(C) with P_k(r) = 0 for all r ∈ p_x, then P(r) = 0 on p_x, so p_x ⊆ P⁻¹(0) ≠ Z̄ (P(1) = 1); p_x is a maximal ideal (Z̄ is integral over Z, so dim Z̄ = 1 and every nonzero prime is maximal — Cohen–Seidenberg [RU, standard]); hence P⁻¹(0) = p_x and P = (x, ψ) for some character ψ of κ(x)×. In the Proposition this is hidden inside "K is closed"; the direct form is what a reader of the note's sentence has to supply.

(b) *Roots of unity are what make "pointwise" rigid:* for r ∉ p_x the values χ(r̄)^{a₀n} lie in the finite set μ_m(C), m = ord(r̄), which is discrete; convergence of such a sequence means eventual constancy. Deninger uses exactly this in the proof of Prop. 9.1 (A18: "since μ_N(C) is discrete in C×"). So the limit of (x, χ^{a₀n_k}) in X•(C) exists iff, for each r, the residues n_k mod ord(r̄) stabilize, iff n_k converges in Ẑ_{(p)} (to the b with β(b) = the limit; by injectivity of β the limit b is unique) — check C2 in the companion file exhibits both a convergent case and a non-convergent one.

(c) *The colimit topology adds nothing* (§3.3).

### 3.6 The E-cut: which limits are points of X₀ (task question 3)

By (R4), cl_{X•₀(C)}(S) = π(K). The E-locus X•(C)^E is G-saturated (A4, Prop. 4.2), so π(K) ∩ X•₀(C)^E = π(K ∩ X•(C)^E) (if π(k) = π(e) with e ∈ E-locus then k = e^σ is in the E-locus). Hence

  cl_{X•₀(C)^E}(S) = π{ (x, χ^{a₀b}) : b ∈ Ẑ_{(p)}, χ^{a₀b} ∈ E }.

Which b survive? By (E3) there are exactly three classes:

- **(i) b ∈ N·Ẑ×_{(p)}**, b = n·u with n ∈ N prime to p and u ∈ Ẑ×_{(p)}: ker(χ^{a₀b}) = μ_n, finite, so (Tors) holds; χ^{a₀nu} = (χ^{a₀u})^n = F_n(χ^{a₀u}) is in E iff χ^{a₀u} is (A4, Def. 4.1, ν-biconditional), and π(x, χ^{a₀nu}) = F_n π(x, χ^{a₀u}) ∈ pr₀⁻¹(x₀). For E ⊇ E_f every such point is in E (finite kernel). These are the packet's own points.
- **(ii) some component b_ℓ = 0:** ker ⊇ μ_{ℓ^∞}, infinite; (Tors) fails; (x, χ^{a₀b}) ∉ X•(C)^E for **every** admissible E. This is the note's case.
- **(iii) every b_ℓ ≠ 0 but v_ℓ(b) > 0 for infinitely many ℓ** (e.g. b_ℓ = ℓ for all ℓ ≠ p, or b_ℓ = ℓ^{k_ℓ} with any k_ℓ ≥ 1): ker = ⊕_ℓ μ_{ℓ^{v_ℓ(b)}} is infinite; (Tors) fails; not in X•(C)^E for any admissible E. **The note's sentence does not cover this class** (check C3 in the companion file exhibits it: the kernel grows with the number of primes in the truncation while every component of b is nonzero).

There is no fourth class: if v_ℓ(b) < ∞ for all ℓ and v_ℓ(b) = 0 for almost all ℓ, then b = nu as in (i). All limit points of classes (ii)–(iii) exist in X•(C) — they are genuine points of Deninger's un-cut space W_rat(X₀)(C) = X•₀(C) — but they are not points of X•(C)^E, hence not of X̌₀(C)^E, hence not of X₀. The exclusion is therefore **by the class E, through the axiom (Tors) that every admissible class imposes (Def. 4.1), realized topologically by the subspace topology of the E-locus**; it is not an artifact of the colimit or suspension topologies. It matters in the following precise sense: in the un-cut suspension X̌₀(C) ×_{Q>0} R>0 (no E) the closure of γ is strictly larger than Γ_p — it contains for instance q(π(x, χ^0) × R>0), the point with the trivial character, whose Q>0-isotropy is all of Q>0 (F_r(x, 1) = (x, 1)) and whose R>0-"orbit" is R>0/Q>0. In X₀ this cannot arise because those points do not exist there. The question "excluded by (Tors), by E, or by the topology" has the answer: by (Tors) ⊆ E, and it is decisive for the closure computed in X₀ because closure in a subspace is the ambient closure intersected with the subspace.

Since {χ^{a₀nu} : n ∈ N prime to p, u ∈ Ẑ×_{(p)}} = {χ_x ∘ (·)^a ∘ (·)^ν : a ∈ Ẑ×_{(p)}, ν ∈ N} (as u runs over the units so does a₀u; a p-power factor of ν is itself a unit by (E1) and is absorbed into a) is, by (35) (A5), the set of **all** (Tors)-characters at x, and pr₀⁻¹(x₀) = π of those (A5, p. 32), we obtain

> **(R5)  cl_{X•₀(C)^E}(S) = pr₀⁻¹(x₀) ∩ X•₀(C)^E.**

### 3.7 Assembly

(R3) + (R5): cl_{X̌₀(C)^E}(O(P₀)) = ⋃_ν F_ν⁻¹( pr₀⁻¹(x₀) ∩ X•₀(C)^E ) = ( ⋃_ν F_ν⁻¹ pr₀⁻¹(x₀) ) ∩ X̌₀(C)^E = C_{x₀} ∩ X̌₀(C)^E = C^E_{x₀} (A5 p. 31 for C_{x₀}; A4 Prop. 4.2 to move the E-locus through F_ν⁻¹; A7 for C^E_{x₀}). Then by (R1), cl_{X₀}(γ) = q(C^E_{x₀} × R>0) = Γ^E_{x₀} (A7). ∎

> **Theorem (referee grade).** Let X₀ = Spec Z, C = ℂ, N₀ = N, E admissible, p a prime, and γ ⊂ Γ^E_p any periodic orbit. Then cl_{X₀}(γ) = Γ^E_p. (⊇ is Theorem A — three prior independent derivations; ⊆ is §§3.2–3.7 above.)

### 3.8 No other stratum is met (task question 4)

Independently of §§3.3–3.7: pr_{X₀}: X̌₀(C)^E → Spec Z is continuous (A12; E-version by A15) and Q>0-invariant (A4, Prop. 4.2), so pr_{X₀} ∘ pr₁: X̌₀(C)^E × R>0 → Spec Z is constant on q-fibers and descends to a continuous map X₀ → Spec Z (q is a quotient map). The point (p) is closed in Spec Z; γ lies in its fiber; therefore so does cl(γ). Hence cl(γ) contains no point of the generic stratum (over (0)) and no point of any Γ_ℓ, ℓ ≠ p. (Contrast §8 of [x-03], A17: the closure of the union over *all* p of the packets does reach the generic stratum — Theorem 8.2 — but a *single* packet's closure does not leave its fiber.) The note's hedge "cl(γ) ∩ (char-p part)" is therefore redundant (F3).

### 3.9 Consequences now at referee grade

(a) **Each packet Γ^E_{x₀} is a closed subset of X₀** (it equals cl(γ)).
(b) **Each packet is a minimal set** in the standard sense — nonempty, closed, flow-invariant, and every orbit in it dense in it (⊇ from Theorem A; closedness from (a)). The adjudication's banked wording "packets are minimal sets" (§4 item 1) used closedness, i.e. the converse inclusion; it is now certified at referee grade rather than resting on the note's proposition-grade sentence.
(c) **For E ⊇ E_f the packet is also compact** in the subspace topology of X₀: Γ_{x₀} = q(π(K^×) × R>0) with K^× := β(Ẑ×_{(p)}) (every point of Γ_{x₀} is [F_r π(x, χ^a), w] = [π(x, χ^a), rw], a a unit), and since [P, pu] = [F_p P, u] = [P, u] for P ∈ C_{x₀}, Γ_{x₀} = q(π(K^×) × [1, p]); Ẑ×_{(p)} is closed in Ẑ_{(p)} (E2), so K^× is compact and Γ_{x₀} is a continuous image of a compact set. This confirms Deninger's "compact packets" (A20; B2 "compact subsets Γ_{x₀}") in the subspace topology of X₀ — a topology which by Cor. A.2 is non-Hausdorff, so that "compact" and "closed" are independent properties there; (a) and (c) establish both. For a general admissible E, Γ^E_{x₀} = q(π(K^×_E) × [1, p]) with K^×_E = β({a ∈ Ẑ×_{(p)} : χ^a ∈ E}) is compact iff that set of exponents is closed in Ẑ×_{(p)}; not examined further, not needed.
(d) By (b) no periodic orbit is a closed subset (already banked); [r3s-08]'s "connected closed R₊-orbits" (C4, p. 18) is a statement about the model Ẑ×_{(p)}/p^Ẑ ×_{pZ} R₊, not about the subspace topology of Γ_p ⊂ X₀ — as the adjudication's §4 item 4 already says. Nothing here cites C4 for topology.

---

## 4. Findings against the note (severity-tagged, with locations and replacement text)

**F1 — MAJOR — Cor. A.1 parenthetical, the clause "limits with some component of b equal to 0 kill a μ_{ℓ^∞} and violate (Tors), so they leave the space — one gets cl(γ) ∩ (char-p part) = Γ^E_p exactly."**
The stated criterion is incomplete. The limit exponents b ∈ Ẑ_{(p)} whose limit point is not in X₀ are those with ker((·)^b) infinite, i.e. b ∉ N·Ẑ×_{(p)} (§3.0 (E3)); besides "some b_ℓ = 0" this includes every b with all components nonzero but infinitely many non-unit components (§3.6 class (iii), e.g. b_ℓ = ℓ for all ℓ ≠ p). The note classifies such b neither as leaving nor as staying, so the equality does not follow from the sentence as written. The gap is fillable — class (iii) also violates (Tors) and leaves — and the conclusion is unaffected. *Replacement text:* see the combined text under F2.

**F2 — MAJOR — the same parenthetical, "every limit of {F_n(P₀)}_n along any subnet is P₀^b for some b ∈ Ẑ_{(p)}, by compactness of Ẑ_{(p)} and the same pointwise evaluation".**
This is a statement about the closure, in X•(C) and at the fixed prime x, of the sequence (x, χ^{a₀n}); it is correct (§3.5). The closure claimed is in X₀. Three reductions are needed and none is in the note: (a) the suspension quotient q is open, so cl_{X₀}(γ) = q(cl(O(P₀)) × R>0) with O(P₀) the full Q>0-orbit in X̌₀(C)^E — (R1); (b) O(P₀) contains the points F_{m/m′}P₀ outside the chart ν = 1, so one needs the chart description (R2) and the locality (R3); (c) the sequence F_n(P₀) lives in X•₀(C) = X•(C)/G, and its limits downstairs are limits of Galois-translated sequences upstairs, so one needs (R4) (openness of π plus Lemma 4, or Prop. 7.7 plus compactness of G). Each step is elementary; together they are the proof. *Replacement text for the entire parenthetical of Cor. A.1 (F1 and F2 together):*

> (Converse inclusion, proof. Normalize as in Step 1: γ = {[P₀, w]}, P₀ = π(x, χ^{a₀}), a₀ ∈ Ẑ×_{(p)}. **(a)** The quotient map q: X̌₀(C)^E × R>0 → X₀ is open, Q>0 acting by homeomorphisms; hence cl_{X₀}(γ) = q(cl(q⁻¹γ)) = q(cl(O(P₀)) × R>0), where O(P₀) = {F_r P₀ : r ∈ Q>0} and the closure is taken in X̌₀(C)^E. **(b)** F_p P₀ = P₀, and for coprime m, m′ prime to p the character χ^{a₀m} is injective on μ_{m′}, so F_{m/m′}P₀ lies in the chart F_ν⁻¹(X•₀(C)^E) iff m′ | ν. The charts are open and cover X̌₀(C)^E, so cl(O(P₀)) = ⋃_ν F_ν⁻¹(cl_{X•₀(C)^E} S) with S = {F_n P₀ : n ∈ N}. **(c)** π: X•(C) → X•₀(C) is open and G is compact and acts continuously, so cl_{X•₀(C)}(S) = π(cl_{X•(C)} S̃) with S̃ = {(x, χ^{a₀n}) : n ∈ N} at the fixed prime x. **(d)** In X•(C) — pointwise convergence of multiplicative maps on Z̄; values at r ∉ p_x are roots of unity of finite order, a discrete set; the zeros on p_x persist in the limit and p_x is maximal — the map b ↦ (x, χ^{a₀b}) is a homeomorphism of Ẑ_{(p)} onto a compact set K ⊂ X•(C) that contains S̃ as the image of the dense subset N ⊂ Ẑ_{(p)}; hence cl S̃ = K. **(e)** (x, χ^{a₀b}) satisfies (Tors) iff ker((·)^b) = ⊕_ℓ μ_{ℓ^{v_ℓ(b)}} is finite iff b ∈ N·Ẑ×_{(p)}. The excluded b — those with some b_ℓ = 0, and those with all b_ℓ ≠ 0 but infinitely many non-unit components — give points of X•(C) that lie in no X•(C)^E, E admissible; so cl_{X•₀(C)^E}(S) = π{(x, χ^{a₀nu}) : n ∈ N, u ∈ Ẑ×_{(p)}} ∩ X•₀(C)^E = pr₀⁻¹(x₀) ∩ X•₀(C)^E by (35)–(36). **(f)** Assembling, cl(O(P₀)) = (⋃_ν F_ν⁻¹ pr₀⁻¹(x₀)) ∩ X̌₀(C)^E = C^E_{x₀}, hence cl_{X₀}(γ) = q(C^E_{x₀} × R>0) = Γ^E_p. Since pr_{X₀} descends to a continuous map X₀ → Spec Z with closed fiber over (p), cl(γ) meets no other stratum, and no restriction "∩ (char-p part)" is needed. In particular Γ^E_p is closed in X₀, and for E ⊇ E_f also compact.)

**F3 — MINOR — "cl(γ) ∩ (char-p part) = Γ^E_p exactly".** The intersection is redundant (§3.8). *Replacement:* "cl(γ) = Γ^E_p".

**F4 — MINOR — "With Step 5's converse inclusion".** Step 5 of Theorem A is the sweep ⊇; it contains no converse inclusion. *Replacement:* "With the converse inclusion, proved as follows".

**F5 — MINOR — §3.1, "the suspension X₀ carries the quotient topology (implicit throughout §§8, 10 ...)".** Correct as a reading of [x-03]; add the explicit primary-source statement: [r3s-08] p. 14, "We equip X_K with the quotient topology of the product X̌_K(C) × R₊", and [x-06] p. 11 for the set-quotient. Also §7 Q-c is now answered YES (§3.3); mark it settled.

**Incidental observation, outside the item (no verdict weight; for the adjudicator).** Theorem A, Step 5, last sentence: "Two such limit points lie on distinct orbits whenever the exponents differ by more than the countable group generated by p^Ẑ and the rational units". p^Ẑ ≅ Ẑ is uncountable, and a positive rational prime to p is a unit of Ẑ_{(p)} only if it is a power of p (E1). The correct statement is: two unit twists â, â′ lie on the same orbit iff â′ ∈ â·p^Ẑ, since the orbits are the fibers of Γ_{x₀} → Ẑ×_{(p)}/p^Ẑ (A7). Theorem A is unaffected (the adjudication's own step 6 is stated correctly).

---

## 5. Attempts to break the equality (all failed; recorded per protocol)

1. **Escape through the R>0-factor** (u_k → 0 or ∞, or [F_{n_k}P₀, u_k] with u_k wandering). Absorbed by (R1): the saturation of γ is O(P₀) × R>0, whose closure is cl(O(P₀)) × R>0; no point of X₀ outside q(C^E_{x₀} × R>0) arises.
2. **Escape to another stratum.** Impossible: §3.8.
3. **Escape by Galois twisting** ((x, χ^{a₀n_k})^{σ_k} with σ_k varying, possibly moving the prime). Lemma 4 (or Prop. 7.7 + compactness of G) returns every such limit to π(cl S̃); no new points.
4. **Escape by a non-(Tors) exponent.** Real in the un-cut space: with n_k ≡ 0 (mod ℓ^k) and n_k ≡ 1 (mod M_k), M_k prime to ℓp and increasing, [F_{n_k}P₀, 1] → [π(x, χ^{a₀b}), 1] with b_ℓ = 0 in X̌₀(C) ×_{Q>0} R>0 (no E); with n_k ≡ 0 (mod M_k) for all M_k prime to p, the limit is the trivial character, of Q>0-isotropy Q>0. These show that the hypothesis E ⊆ E_tors is *necessary* for the equality — the equality is false in W̌_rat(X₀)(C) ×_{Q>0} R>0 — but they are not points of X₀, so they are not counterexamples to the claim as stated.
5. **Nets versus sequences.** Every chart is metrizable (A9, A14) and closure is chart-local (R3); no net phenomenon escapes the sequential computation.
6. **The colimit topology finer than pointwise.** It is not, on any chart (§3.3).

---

## 6. Verdict block

**Verdict: PASS-WITH-REPAIRS.** Counts: FATAL 0, MAJOR 2 (F1, F2), MINOR 3 (F3, F4, F5). Nothing stated in Corollary A.1 is false; the converse inclusion is true and now proved; the note's argument for it is not a proof and must be replaced by the text under F2.

**Repairs (each with replacement text above):** F1+F2 — replace the parenthetical of Cor. A.1 by the six-step proof (a)–(f); F3 — drop "∩ (char-p part)"; F4 — fix the cross-reference; F5 — cite [r3s-08] p. 14 for the quotient topology and mark Q-c settled.

**What is now established at referee grade, and its precise scope.** In Deninger's system X₀ = X̌₀(C)^E ×_{Q>0} R>0 for X₀ = Spec Z, C = ℂ, N₀ = N and any admissible class E (Def. 4.1 of [x-03]), with X₀ carrying the quotient topology of X̌₀(C)^E × R>0 (the reading forced by [x-03] Thm 7.10 and §8 and stated explicitly in [r3s-08] p. 14), the closure of every periodic orbit γ ⊂ Γ^E_p is exactly its packet: cl_{X₀}(γ) = Γ^E_p. The equality holds in the whole space, not only within the characteristic-p part — cl(γ) lies in the fiber of the continuous map X₀ → Spec Z over (p), so it meets neither the generic stratum nor any other prime's packet — and it holds verbatim in every chart F_ν⁻¹(X•₀(C)^E) of the colimit, the closure in the colimit being the union of the chart closures. The mechanism is: the Frobenius return exponents N close up, in the pointwise topology upstairs at a fixed prime, to the full Cantor group Ẑ_{(p)} (a homeomorphic copy), and the class E — through the axiom (Tors) that every admissible class imposes — retains exactly the exponents in N·Ẑ×_{(p)}, which by [x-03] (35)–(36) are exactly the packet's own points; the exponents with a zero component *and* those with infinitely many non-unit components are limits in Deninger's un-cut space but are not points of X₀. Consequences certified: each packet is a closed subset of X₀ and a minimal set; for E ⊇ E_f it is also compact in the subspace topology (confirming Deninger's "compact packets" in that topology). The equality is *false* in the un-cut suspension X̌₀(C) ×_{Q>0} R>0 (no (Tors)), so the E ⊆ E_tors hypothesis is necessary. The scope does not extend, without further work, to bases X₀ other than Spec Z (the derivation used that the primes of Z̄ over p are maximal and that x₀ = (p) has degree 1 and N x₀ = p; the same argument should go through for any closed point of an arithmetic scheme with N x₀^Ẑ in place of p^Ẑ, but that is not certified here), nor to non-admissible E. Nothing in the Session-8 adjudicated verdicts changes; the one place that silently used this converse — the adjudication's phrase "packets are minimal sets" — is now backed at referee grade.

---

## 7. Sources — every page read this session

- **[x-03]** `fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf` (arXiv:1807.06400v4, 119 pp.; text layer extracted with `pdftotext -layout`, page breaks verified against the printed folios). Printed pages read: 2–5 (introduction: packets, "compact packets", the closure-of-periodic-orbits paragraph); 7 (contents); 21–25 (§2 end, §3: X•(C), Remark 3.4, Prop. 3.5, the colimits X̌(C), X̌₀(C), (28)–(29), Def. 3.6, Prop. 3.7, Cor. 3.8); 26–30 (§4: (Tors), (Image), Def. 4.1, Prop. 4.2, Lemma 4.3, Cor. 4.4, the examples E_tors ⊇ … ⊇ E_f, the p-adic remark, Prop. 4.5, Lemma 4.6); 31–38 (§5: (32)–(46), Prop. 5.1, Thm. 5.2 with proof, Lemma 5.3, Remark 5.4, Thm. 5.5); 38–40 (§6: suspension, Γ_{x₀}, Γ^E_{x₀}, Thm. 6.1, the Y₀ question); 40–49 (§7 in full: pointwise topology, Lemmas 7.1–7.3, (51)–(54), Prop. 7.4, Props. 7.5–7.7, Cors. 7.8–7.9, Thm. 7.10 with Remarks 1–2, the E-subspace paragraph, (56)–(68), the non-proper-discontinuity sentence); 49–52 (§8: Y₀, Claim 8.1, Thm. 8.2 with proof, Lemma 8.3 with proof); 53 (§9 opening, Prop. 9.1 with proof); 60–61 (§9/§10 boundary remark on the quotient-vs-subspace topology of pr⁻¹(η₀)).
- **[x-06]** `fetched/x-06-deninger-2024-primes-knots-and-periodic-orbits.pdf` (arXiv:2301.11643). Printed pages read: 10–12 (§4: the topology reference to [Den22a §7], Thm. 4.1, the definition X₀ = (X̌₀(C) × R>0)/Q>0, the admissibility paragraph, Thm. 4.2 and the "compact packets" paragraph, Thm. 4.3, the closure-of-compact-orbits paragraph).
- **[r3s-08]** `fetched-r3/r3s-08-morishita-deninger-cc-bridge-2508.15971.pdf` (arXiv:2508.15971v5). Printed pages read: 12–14 (topology of Ẋ_Q(C), X̌_K(C), and the quotient topology on X_K); 17–18 (Thm. 2.2.9 (1)–(2)).
- **[D25]** `fetched-r3/r3s-22-deninger-rational-witt-vectors-associated-sheaves-arxiv-2508.05329v1-SESSION8-FETCH.pdf`. Printed pages read: 1–2 (title, abstract, introduction); full text layer searched for "packet", "periodic orbit", "suspension", "Hausdorff", "closure of", "topolog" — nothing bearing on the item.
- **Program files:** `results/c3-r/probe-9.3-adjudication.md` (in full), `results/c3-r/probe-9.3-b.md` (in full), `results/corpus-routing.md` (header caveats 1–20).
- **Recalled, not load-bearing [RU]:** the Cohen–Seidenberg statement that an integral extension preserves Krull dimension (used only to say that nonzero primes of Z̄ are maximal; any reader can replace it by the going-up/incomparability theorems).
- **Companion checks:** `results/c3-r/referee-s14/B-corA1-F-checks.py`, output `B-corA1-F-checks.json` (all checks pass): C1 (CRT density in a truncation), C2 (stabilization of ζ^{n_k} iff n_k converges in Ẑ_{(p)}, both directions exhibited), C3 (the three exponent classes (i)–(iii), with the kernel of class (iii) growing with the number of primes while every component of b is nonzero).

— end of referee report F, item B-corA1 —
