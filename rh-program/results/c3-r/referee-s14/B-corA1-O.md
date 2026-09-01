# REFEREE REPORT O — probe B, Corollary A.1: the converse inclusion cl(γ) ⊆ Γ^E_p

**Program:** RH program, direction C3-r (geometric substrate, reduced recommission). **Session 14, 2026-09-02.**
**Referee:** O (one of two independent referees on this item; the other is a different model. Standing order 7: nothing below is softened in the expectation that the other pass will catch it).
**Note under review:** `results/c3-r/probe-9.3-b.md`, Corollary A.1 and its parenthetical proof of the converse inclusion (probe B's own Q-c; adjudication §4 item 6, §5 Q-c).
**Binding context read first, in full:** `results/c3-r/probe-9.3-adjudication.md`; then `results/c3-r/probe-9.3-b.md` in full; `results/corpus-routing.md` standing caveats §§1–20.
**Standing order 5:** every source statement below was read this session from the on-disk PDF at the stated printed page (pdftotext extraction made fresh in the session scratchpad; page numbers of [x-03] are the printed pages, which coincide with the PDF pages of the v4 file). Nothing is recalled.

---

## VERDICT (stated first)

> **PASS-WITH-REPAIRS.**
>
> **The statement is true — and true in a strictly stronger form than the note claims.** The converse inclusion holds, with no "char-p part" hedge and no chart caveat:
>
> **cl_{X₀}(γ) = Γ^E_{x₀} in X₀, for every arithmetic scheme X₀, every admissible E, every point x₀ with finite residue field and every periodic orbit γ ⊂ Γ^E_{x₀}** — the ⊇ half being the banked Theorem A (for X₀ = Spec Z), the ⊆ half being Proposition O.1 below, which is proved for all arithmetic X₀. Indeed **every packet Γ^E_{x₀} is a closed subset of X₀** (Proposition O.1); the closure of anything inside it stays inside it.
>
> **The argument the note gives for it is not a proof** (finding F1, MAJOR) and its conclusion is mis-scoped (F2, MAJOR). Both are repaired below with exact replacement text. Four MINOR findings follow.
>
> **fatals 0 / majors 2 / minors 4.**
>
> The correct proof is two lines and uses none of the machinery the note reaches for: the Zariski topology on the base scheme plus continuity of pr_{X₀}. The note's chosen instrument — profinite compactness of Ẑ_(p) plus pointwise evaluation of characters — cannot reach the statement, for a structural reason (§4, §6.3) that is worth recording in its own right: the ⊇ direction lives upstairs and survives every quotient; the ⊆ direction is a statement about *all* nets downstairs, and downstairs convergence does not lift, precisely because the Q^{>0}-action is not properly discontinuous ([x-03] p. 49, verbatim in §2 below).

---

## 1. The text under review, quoted exactly

From `probe-9.3-b.md`, Corollary A.1 (§5):

> **Corollary A.1 (packets are minimal sets; the "invariant tori" made precise).** Every orbit of Γ^E_p is dense in Γ^E_p; Γ^E_p is the orbit closure of each of its points and is the smallest closed invariant set containing any one of its orbits. (With Step 5's converse inclusion — every limit of {F_n(P₀)}_n along any subnet is P₀^b for some b ∈ Ẑ_(p), by compactness of Ẑ_(p) and the same pointwise evaluation; limits with some component of b equal to 0 kill a μ_{ℓ^∞} and violate (Tors), so they leave the space — one gets cl(γ) ∩ (char-p part) = Γ^E_p exactly. Stated proposition-grade; the kill only needs ⊇.)

And §7, Q-c:

> **Q-c (bookkeeping).** Whether the equality cl(γ) = Γ^E_p of Cor. A.1 holds verbatim in every chart of the colimit (the ⊇ of Theorem A suffices for everything above; the ⊆ was argued at proposition grade).

The adjudication records the debt at §4 item 6 ("probe B's Cor. A.1 converse inclusion (flagged proposition-grade by B itself; not load-bearing) … Before any external circulation, Theorem B(b) and Cor. A.1 owe a dedicated referee pass; nothing in the adjudicated verdicts rests on them") and at §5 Q-c.

**One correction to the "not load-bearing" bookkeeping, before anything else** (finding F4): the *first sentence* of Corollary A.1 is not all ⊇. "Γ^E_p is the orbit closure of each of its points" is exactly the ⊆ direction. "Γ^E_p … is the smallest closed invariant set containing any one of its orbits", and the corollary's own title "packets are minimal sets", both require Γ^E_p to *be* closed — a minimal set is by definition a nonempty closed invariant set with no proper nonempty closed invariant subset. Theorem A alone gives only: every closed invariant set meeting Γ^E_p contains Γ^E_p. Without ⊆ one cannot say the packet *is* a minimal set, only that it is contained in every one. The adjudication re-publishes "packets are minimal sets (every orbit dense in its packet)" at referee grade in §4 item 1; the parenthetical is the ⊇ content, the headline is not. After Proposition O.1 the headline is true, so nothing has to be retracted — but the dependency was mis-booked and is now corrected.

---

## 2. Source anchors, read this session, verbatim

All from `fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf` unless stated. Printed page = PDF page for this file (verified: the folio "31" sits on PDF page 31, etc.).

**(A1) Topology on one chart — pointwise convergence** (p. 40, opening of §7):
> "We only consider integral normal schemes X₀ whose function field K₀ is countable. For brevity we call them arithmetic schemes. … We begin with the affine case X₀ = spec R₀ and write X = spec R. Viewing X⃗(C) as a set of multiplicative maps P : R → C as in Remark 3.4 we give X⃗(C) the topology of pointwise convergence. It is the subspace topology induced by the Tychonov topology of C^R = ∏_R C on X⃗(C) via the inclusion X⃗(C) ⊂ C^R, P ↦ (P(r))_{r∈R}. Since R is countable, X⃗(C) is a metrizable topological space."

**(A2) pr_X is continuous into the Zariski topology** (p. 40, Lemma 7.1 and its proof):
> "Lemma 7.1. For affine arithmetic schemes X₀, the natural map pr_X : X⃗(C) → X, (x, P^×) ↦ x or P ↦ p = P^{-1}(0) is continuous.
> Proof. A closed subset A of X has the form A = {p ⊃ I} for some ideal I in R. Consider a convergent sequence P_n → P in X⃗(C) where P_n ∈ pr_X^{-1}(A) for all n, i.e. p_n = P_n^{-1}(0) ⊃ I. Since P_n(r) → P(r) for all r ∈ R, it follows that P(r) = 0 for r ∈ I and hence p = P^{-1}(0) ⊃ I i.e. P ∈ pr_X^{-1}(A). Hence pr_X^{-1}(A) is closed and therefore pr_X is continuous."

Note what the closed sets of the target are: `{p ⊃ I}` — the **Zariski** topology. This is the whole engine of the repair.

**(A3) Quotient by G, and continuity downstairs** (p. 42):
> "Let G = Aut_{K₀}(K). We equip X₀⃗(C) = X⃗(C)/G with the quotient topology. Using Lemma 7.1 one sees that pr_X : X⃗(C) → X and hence also pr_{X₀} : X₀⃗(C) → X₀ are continuous."

**(A4) The colimit topology and its charts** (p. 43):
> "We give X̌(C) = colim_{N₀} X⃗(C) the inductive limit topology. It is the finest topology such that for all ν ∈ N₀ the inclusions F_ν^{-1}|_{X⃗(C)} : X⃗(C) ↪ X̌(C) are continuous. Thus Z ⊂ X̌(C) is closed, resp. open if and only if F_ν(Z) ∩ X⃗(C) is closed, resp. open in X⃗(C) for all ν ∈ N₀.
> Proposition 7.4. a) X⃗(C) is a closed and open subspace of X̌(C). b) F_q : X̌(C) → X̌(C) is a homeomorphism for every q ∈ Q₀^{>0}. c) The group G acts by homeomorphisms on X̌(C)."

**(A5) Continuity of the projections on the colimit** (p. 43):
> "We give X̌₀(C) = X̌(C)/G the quotient topology. Then X̌₀(C) is homeomorphic to colim_{N₀} X₀⃗(C) with the inductive limit topology. The projections π : X⃗(C) → X₀⃗(C) and π̌ : X̌(C) → X̌₀(C) are continuous and since G acts by homeomorphisms, also open. Moreover the projections pr_X : X̌(C) → X and pr_{X₀} : X̌₀(C) → X₀ are continuous."

**(A6) The E-versions inherit everything** (p. 47):
> "Given an admissible class E as in Definition 4.1 we equip X⃗(C)_E and X₀⃗(C)_E with the subspace topologies of X⃗(C) and X₀⃗(C). … We give X̌(C)_E = colim_{N₀} X⃗(C)_E and X̌₀(C)_E = colim_{N₀} X₀⃗(C)_E the inductive limit topologies. They agree with the subspace topologies via X̌(C)_E ⊂ X̌(C) and X̌₀(C)_E ⊂ X̌₀(C) because the subspaces F_ν^{-1}X⃗(C) and F_ν^{-1}X₀⃗(C) are open in X̌(C) resp. X̌₀(C) for all ν ∈ N₀. As above, the natural continuous bijection X̌(C)_E/G → X̌₀(C)_E is a homeomorphism. All preceding results in this section remain true if we replace X⃗(C) etc. by X⃗(C)_E etc."

**(A7) Q^{>0}-equivariance of pr with trivial action on the base** (p. 27):
> "Both pr_X and pr_{X₀} are N₀-equivariant if we let N₀ act trivially on X₀ and X. Note that the maps pr_X and pr_{X₀} above extend Q₀^{>0}-equivariantly to maps pr_X : X̌(C)_E → X and pr_{X₀} : X̌₀(C)_E → X₀. Here we let Q₀^{>0} act trivially on X and X₀."

**(A8) Admissibility and (Tors)** (p. 27):
> "(Tors) the group ker(χ)_tors = ker(χ|_{μ(κ)}) is finite and |(ker χ)_tors| ∈ N₀.
> Definition 4.1. A class E of characters χ : κ^× → C^× on algebraically closed fields κ is (N₀−)admissible if for any σ ∈ Autκ resp. ν ∈ N₀ the character χ is in E if and only if χ ∘ σ resp. χ^ν = χ ∘ ( )^ν is in E. Moreover the characters in E should satisfy (Tors)."

**(A9) Definition of C_{x₀} as a fibre** (p. 31):
> "The fibres of pr_{X₀} : X̌₀(C)_{Etors} → X₀ are Q₀^{>0}-invariant. We will now analyze the structures of the Q₀^{>0}-sets C_{x₀} = pr_{X₀}^{-1}(x₀) in X̌₀(C)_{Etors} for points x₀ of X₀ whose residue field κ(x₀) is finite. … The fibre pr₀^{-1}(x₀) in X₀⃗(C)_{Etors} is N₀-invariant. Its extension to a Q₀^{>0}-invariant subset of X̌₀(C)_{Etors} is the set C_{x₀} = pr₀^{-1}(x₀)Q₀^{>0} = ⋃_{ν∈N₀} F_ν^{-1} pr₀^{-1}(x₀) ⊂ X̌₀(C)_{Etors}."

Deninger's own first sentence there — "**The fibres of pr_{X₀} … are Q₀^{>0}-invariant … the Q₀^{>0}-sets C_{x₀} = pr_{X₀}^{-1}(x₀)**" — already *names C_{x₀} as the fibre*. That identification, plus (A2)/(A5), is the entire proof.

**(A10) Suspension and packets** (p. 38, §6):
> "consider the suspension X₀ = X̌₀(C)_E ×_{Q₀^{>0}} R^{>0}. It is the quotient of X̌₀(C)_E × R^{>0} by the right Q₀^{>0}-action given by (P₀, u)q = (P₀q, q^{-1}u) = (F_q(P₀), q^{-1}u) for q ∈ Q₀^{>0}. … For a point x₀ of X₀ with finite residue field of characteristic p set Γ_{x₀} = C_{x₀} ×_{Q₀^{>0}} R^{>0} ⊂ X₀. The Q₀^{>0}-bijection (39) induces an R^{>0}-bijection (Ẑ×_(p)/Nx₀^Ẑ) ×_{p^Z/deg x₀} R^{>0}/Nx₀^Z → Γ_{x₀}. Thus all R^{>0}-orbits in Γ_{x₀} are circles R^{>0}/Nx₀^Z and Γ_{x₀} fibres over Ẑ×_(p)/p^Ẑ = Aut(F̄_p)/Aut(F_p)^ with fibres the R^{>0}-orbits in Γ_{x₀}. We set Γ^E_{x₀} = C^E_{x₀} ×_{Q₀^{>0}} R^{>0} where C^E_{x₀} = C_{x₀} ∩ X̌₀(C)_E. If e.g. E_f ⊂ E then Γ^E_{x₀} = Γ_{x₀}."

**(A11) Theorem 6.1** (p. 39):
> "Theorem 6.1. Let E be an admissible class with E ⊂ E_max. The following decomposition holds, where x₀ runs over the points of X₀ with finite residue fields κ(x₀): {x₀ ∈ X₀ | (R^{>0})_{x₀} ≠ 1} = ⨿_{x₀} Γ^E_{x₀}. For any point x₀ ∈ Γ^E_{x₀} the isotropy group of x₀ is (R^{>0})_{x₀} = Nx₀^Z."
> "Any periodic orbit γ in X₀ is contained in Γ^E_{x₀} for a uniquely determined point x₀ of X₀ with finite residue field."

**(A12) The suspension carries the quotient topology — the on-disk warrant** (p. 63, §10):
> "Consider the projection: π : X̃ = M × R^{>0} → X = M ×_Q R^{>0}. … R_X = (π_∗R_X̃)^Q ⊂ (π_∗C⁰_X̃)^Q = C⁰_X. … Note that in general the continuous bijection π|_{M×{u}} : M × {u} → π(M × {u}) will not be a homeomorphism if π(M × {u}) is equipped with the subspace topology of X."

The identity `(π_∗C⁰_X̃)^Q = C⁰_X` is precisely the statement that a Q-invariant continuous function on X̃ descends to a *continuous* function on X — i.e. that X carries the quotient topology. Cross-check in [x-06] (`fetched/x-06-deninger-2024-primes-knots-and-periodic-orbits.pdf`, printed p. 11): "Set X₀ = (X̌₀(C) × R^{>0})/Q^{>0} where Q^{>0} acts diagonally."

**(A13) The Q^{>0}-action is not properly discontinuous** (p. 49, end of §7):
> "The Q^{>0}-action on Ȟ_{Etors} × R^{>0} is not properly discontinuous. In section 10, we will see that this works to our advantage."

**(A14) Hausdorffness — upstairs yes, suspension not claimed** (pp. 45–46):
> "Corollary 7.8. For any affine arithmetic scheme X₀ = spec R₀ there are a G-invariant metric d on X⃗(C) and a metric δ on X₀⃗(C) = X⃗(C)/G inducing the topology on X⃗(C) and the (quotient-)topology on X₀⃗(C). … The topological space X₀⃗(C) is metrizable and separable and in particular Hausdorff."
> "Corollary 7.9. Let X₀ be an arithmetic scheme which carries an ample invertible sheaf. Then the spaces X⃗(C), X₀⃗(C), X̌(C) and X̌₀(C) are Hausdorff."
And Proposition 7.7 (p. 44), which supplies the metric: "δ(xG, yG) = min_{σ,τ} d(x^σ, y^τ) = min_σ d(x^σ, y) = min_τ d(x, y^τ). The metric δ induces the quotient topology. In particular X/G is Hausdorff."

Nothing anywhere in §7 asserts Hausdorffness of the suspension; Corollaries 7.8/7.9 stop at X̌₀(C). (This is the adjudicated G1 = NO; nothing here disturbs it.)

**(A15) The (Tors) locus is dense, not closed** (p. 53, §9 and Proposition 9.1):
> "Let X⃗(C)′ ⊂ X⃗(C) denote the subspace of points (x, P^×) where (ker P^×)_tors is a possibly infinite N₀-primary group. … We have X̌(C)_{Etors} ⊂ X̌(C)′ etc. and X̌(C)′ = X̌(C) etc. if N₀ = N.
> Proposition 9.1. X⃗(C)′ is the topological closure of X⃗(C)_{Etors} in X⃗(C)."

**(A16) Density of the generic stratum, and connectedness of the suspension** (pp. 54, 62):
> "Theorem 9.2. Let η = spec K and η₀ = spec K₀ be the generic points of X resp. X₀. Then the fibres of X̌(C)_{Ef} and X̌₀(C)_{Ef} over η resp. η₀ are dense in X̌(C)′ resp. X̌₀(C)′."
> "Corollary 9.7. Let X₀ be an integral normal scheme which is flat of finite type over spec Z and let E be an admissible condition with E ⊃ E_f. Then the spaces X = X̌(C)_E ×_{Q^{>0}} R^{>0} and X₀ = X̌₀(C)_E ×_{Q^{>0}} R^{>0} are connected. Proof. By Theorem 9.6 the spaces X_η and X_{0η₀} are connected. By Theorem 9.2 they are dense in X resp. X₀. Hence X and X₀ are connected as well."

**(A17) Deninger asserts compactness of the packets, never closedness** ([x-03] printed p. 2; [x-06] printed p. 12):
> [x-03] p. 2: "the closed points x₀ of X₀ correspond bijectively to compact packets Γ_{x₀} of periodic orbits of length log Nx₀ on X₀ = X̌₀(C) ×_{Q^{>0}} R^{>0}."
> [x-03] p. 3: "The compact packets Γ_{x₀} are reminiscient of invariant tori. There are no fixed points of the flow."
> [x-06] p. 12: "The compact subsets Γ_{x₀} ⊂ X₀ consist of periodic orbits of length log Nx₀ where Nx₀ = |κ(x₀)| (= |R₀/m₀|) and they are pairwise disjoint."

**(A18) Morishita's topological wording** (`fetched-r3/r3s-08-morishita-deninger-cc-bridge-2508.15971.pdf`, printed pp. 17–18):
> "Theorem 2.2.9 ([D7, Sections 5, 6, 7]). (1) We have the Q₊-equivariant homeomorphism Ẑ×_(p)/Np^Ẑ ×_{p^Z} Q₊ → C_p, and the R₊-equivariant homeomorphism Ẑ×_(p)/Np^Ẑ ×_{p^Z} R₊ → Γ_p, which is the mapping torus of the multiplication by lk_p(p) in Ẑ×_(p)/Np^Ẑ."
> "(2) … So γ_{p,a} is a circle of length log Np and we have the decomposition into connected closed R₊-orbits Γ_p = ⊔_{a} γ_{p,a}."

---

## 3. Task item (1): the exact topology on X₀ in which the closure is taken

Assembled from (A1)–(A7), (A12). Four layers, applied in this order:

1. **One chart, upstairs.** For X₀ = Spec Z, X = Spec Z̄ is affine with R = Z̄ countable. X⃗(C) = the set of multiplicative maps P : Z̄ → C arising from pairs (x, P^×), with **the topology of pointwise convergence**, i.e. the subspace topology of the Tychonov product C^{Z̄}. Metrizable, and by Prop. 7.6 second countable and separable. X⃗(C)_E ⊂ X⃗(C) with the **subspace** topology (A6).
2. **Quotient by G = Gal(Q̄/Q).** X₀⃗(C)_E = X⃗(C)_E/G with the **quotient** topology, which by Prop. 7.7 + Cor. 7.8 is induced by δ(π(P), π(P′)) = min_{σ∈G} d(P^σ, P′). G is profinite, hence compact, hence the minimum is attained: **π(P_n) → π(P) downstairs ⟺ ∃σ_n ∈ G with P_n^{σ_n} → P upstairs.** Note the direction: downstairs convergence is *strictly weaker* than upstairs convergence of any fixed choice of representatives.
3. **Colimit over N₀ = N.** X̌₀(C)_E = colim_N X₀⃗(C)_E with the **inductive limit** topology; by Prop. 7.4a and (A6) each chart F_ν^{-1}(X₀⃗(C)_E) is **open** (and closed) in X̌₀(C)_E, the charts are directed by divisibility and cover, and F_ν is a homeomorphism of X̌₀(C)_E onto itself. Consequence used repeatedly below: **a net converges in X̌₀(C)_E if and only if it is eventually inside the (open) chart containing its limit and converges there** — i.e. after applying the homeomorphism F_ν, pointwise-mod-G in X₀⃗(C)_E.
4. **Suspension.** X₀ = X̌₀(C)_E ×_{Q^{>0}} R^{>0} = (X̌₀(C)_E × R^{>0})/Q^{>0} with the **quotient** topology (A10 for the algebra, A12 for the topology; [x-06] p. 11 for the same in Deninger's own survey wording). Write q : X̌₀(C)_E × R^{>0} → X₀ for the quotient map. **q is open**, because Q^{>0} acts by homeomorphisms (Prop. 7.4b upstairs, translation on the R^{>0}-factor), so q^{-1}(q(U)) = ⋃_{r∈Q^{>0}} U·r is open. **q is not proper and does not reflect convergence**: the Q^{>0}-action is *not properly discontinuous* (A13).

**Recorded as finding F5 (MINOR):** [x-03] never states in §6 which topology X₀ carries; the note says only "(implicit throughout §§8, 10 …)". The on-disk warrant is (A12) — §10 p. 63's identity `(π_∗C⁰_X̃)^Q = C⁰_X`, which is equivalent to "quotient topology" — together with [x-06] p. 11. Since the ⊆ proof below is exactly a continuity statement on X₀, this citation is load-bearing and must be made explicitly: a topology on X₀ strictly coarser than the quotient topology would invalidate it. (Any topology *finer* than the quotient topology would leave the proof intact, so the risk is one-sided and is closed by (A12).)

---

## 4. Task item (2): is "pointwise convergence of characters" the right description?

**Answer: no, in three separate ways, and the note's phrase "the same pointwise evaluation" silently assumes all three away.** The colimit is indeed finer than a naive pointwise description; the two group quotients are coarser. The net effect is that the ⊇ direction is unaffected and the ⊆ direction is unreachable by that instrument as the note wields it.

**(2a) Finer, layer 1 → 3: the colimit charts are open, so "denominators" cannot run away.** A net z_α in X̌₀(C)_E converging to z must eventually lie in *one* chart F_ν^{-1}(X₀⃗(C)_E) containing z, and converge there. So a family of points whose Frobenius denominators ν_α are unbounded in the divisibility order can never converge to a point of X₀⃗(C)_E, no matter how well any system of representatives converges pointwise. Any "pointwise" description of convergence in X̌₀(C)_E must therefore be *chart-relative*: it is pointwise convergence of F_ν(z_α) → F_ν(z), for one ν that works for the tail. The note never fixes a chart; its Theorem A does not need to (all of Step 3 happens in the single chart X₀⃗(C)_E, and this is why Theorem A is safe), but a claim about *all* limits of *all* nets does need to.

**(2b) Finer, layer 1: the E-locus carries the subspace topology inside X⃗(C), and is not closed there.** A net of E-points can converge pointwise in C^{Z̄} to a multiplicative map that is a perfectly good point of X⃗(C) but violates (Tors) and so is not in X⃗(C)_E. This is not a rare pathology: by Prop. 9.1 with N₀ = N (A15), X⃗(C)_{Etors} is **dense** in X⃗(C). So pointwise-limit reasoning must always be accompanied by the check "and the limit is still in the space" — which is (2b) below in §5, and which the note does perform, if incompletely.

**(2c) Coarser, layers 2 and 4: neither quotient reflects convergence.** Downstairs convergence in X₀⃗(C)_E means pointwise convergence *after an unknown, β-dependent Galois twist* (A14, Prop. 7.7's metric). And convergence in the suspension X₀ does not lift at all to convergence in X̌₀(C)_E × R^{>0}: quotient maps by non-properly-discontinuous actions (A13) do not reflect convergence. The best available lifting statement is:

> **Lemma O.0 (net lifting through an open quotient).** Let q : Y → Z be a continuous open surjection, (z_α) a net in Z with z_α → z, and y ∈ q^{-1}(z). Then there are a subnet (z_β) and points y_β ∈ q^{-1}(z_β) with y_β → y.
> *Proof.* Direct the set D of pairs (α, U), U an open neighborhood of y with z_α ∈ q(U), by (α,U) ≤ (α′,U′) iff α ≤ α′ and U ⊇ U′. D is nonempty and directed: for any U ∋ y open, q(U) is an open neighborhood of z, so z_α ∈ q(U) for all large α. For (α,U) ∈ D pick y_{(α,U)} ∈ U ∩ q^{-1}(z_α). Then (y_{(α,U)}) is a subnet-indexed family with q(y_{(α,U)}) = z_α and y_{(α,U)} → y. ∎

This costs a subnet and, crucially, lets one *choose* the fibre point y to converge to — it does not say that a given approximating net converges upstairs. Everything the note wants to compute upstairs must pass through Lemma O.0 or through an argument that never leaves the quotient. The note does neither.

**Where a subnet limit "exists pointwise but not in X₀", and conversely** — the two failure modes the task asks about, both real:
* *Pointwise but not in X₀*: the escaping (Tors)-violating limits of §5. These are limits in C^{Z̄} (and even in X⃗(C)) which are not points of X̌₀(C)_E at all.
* *In X₀ but not pointwise*: any pair of limits produced by the adjudicated Corollary A.2 construction. The sequence z_k = [P₀, n_k v] converges in X₀ both to [(x,χ^c), v] and to [P₀, w*]; upstairs, the single sequence (P₀, n_k v) converges to nothing, and the two limits are obtained from *different* choices of Q^{>0}-representative. That is exactly the non-Hausdorffness, and it is the clearest possible demonstration that "convergence in X₀" is not "pointwise convergence of characters" in any naive sense.

**Structural remark worth banking (new here, small):** X̌₀(C) is **Hausdorff** for X₀ = Spec Z — Spec Z is affine, hence carries an ample invertible sheaf, so Cor. 7.9 (A14) applies. Hence limits in X̌₀(C)_E are unique, and *all* of the non-Hausdorffness of the adjudicated Cor. A.2 is created by the last quotient, the suspension. This is why §6's proof, which works one level down in X̌₀(C)_E, is clean, and why any proof attempted at the level of X₀ has to fight the pathology.

---

## 5. Task item (3): the "leaves the space" claim — what excludes the bad limits, and does it matter

**What the note's sketch actually computes, done correctly.** Fix a prime p, a point x ∈ X = Spec Z̄ over (p), so κ(x) = F̄_p and κ(x)^× = μ^{(p)} = ⋃_{l≠p} μ_{l^∞}, and a character P₀^× : μ^{(p)} → C^× with finite kernel (A8). Write P₀ : Z̄ → C for the associated multiplicative map: P₀(r) = 0 for r ∈ p̄_x = the prime of Z̄ under x, and P₀(r) = P₀^×(r̄) otherwise. Every value P₀(r) is a root of unity of order prime to p (μ^{(p)} is torsion of prime-to-p order and a homomorphic image of a torsion group is torsion). By (34) [x-03] p. 32, Aut(μ^{(p)}) = Ẑ×_(p) with Ẑ_(p) = ∏_{l≠p} Z_l, and for any b ∈ Ẑ_(p) the map ( )^b : μ^{(p)} → μ^{(p)} is defined; write P₀^b : Z̄ → C, r ↦ P₀(r)^b (with 0 ↦ 0). Then:

> **Proposition O.5 (the corrected content of the note's parenthesis).**
> **(a)** The map Ẑ_(p) → C^{Z̄}, b ↦ P₀^b, is continuous and injective; Ẑ_(p) is compact and C^{Z̄} is Hausdorff, so it is a homeomorphism onto its image, and that image is compact.
> **(b)** F_n(P₀) = P₀^{ι(n)} where ι : N → Ẑ_(p) is the canonical map, and ι(N) is dense in Ẑ_(p). Hence the closure of {F_n(P₀) : n ∈ N} in C^{Z̄} is exactly {P₀^b : b ∈ Ẑ_(p)} ≅ Ẑ_(p).
> **(c)** P₀^b satisfies (Tors) **iff** ker(( )^b : μ^{(p)} → μ^{(p)}) is finite **iff** b ∈ ⋃_{ν ∈ N, p∤ν} ν·Ẑ×_(p). In that case b = νa with a ∈ Ẑ×_(p), and P₀^b = F_ν(P₀^a).
> **(d)** Therefore the set of limit points of the sequence (F_n(P₀))_n *in X⃗(C)_{Etors}* is {F_ν(P₀^a) : ν ∈ N prime to p, a ∈ Ẑ×_(p)}; all of these lie over the same x, and their images in X₀ satisfy [F_ν(P₀^a), u] = [P₀^a, νu], hence lie on the packet orbits. Every other subnet limit exists in C^{Z̄} (indeed in X⃗(C)) but not in X⃗(C)_{Etors}.

*Proofs.* (a) For fixed r with P₀(r) of multiplicative order m (prime to p), b ↦ P₀(r)^b is locally constant on Ẑ_(p) (it factors through Ẑ_(p) → Z/m), hence continuous; continuity into the product follows. Injectivity: if P₀^b = P₀^{b′} then c := b − b′ annihilates the image P₀^×(μ^{(p)}) = μ^{(p)}/ker P₀^×, which is again a group of type μ^{(p)} (a divisible torsion group modulo a finite subgroup), and the only element of Ẑ_(p) annihilating μ^{(p)} is 0. (b) F_n(P₀)(r) = P₀(r)^n and P₀(r) has prime-to-p order, so only ι(n) matters; N surjects onto Z/M for every M prime to p, so ι(N) is dense in Ẑ_(p) = lim_M Z/M. Now (a) makes the image compact, hence closed, and it contains the dense-in-itself image of N. (c) ( )^b acts on the l-primary component μ_{l^∞} as raising to b_l, with kernel μ_{l^{v_l(b_l)}} (all of μ_{l^∞} when b_l = 0). The total kernel ⊕_{l≠p} μ_{l^{v_l(b_l)}} is finite iff every v_l(b_l) < ∞ and v_l(b_l) = 0 for almost all l, i.e. iff b = νa with ν = ∏_l l^{v_l(b_l)} ∈ N prime to p and a ∈ Ẑ×_(p). Then ker(P₀^{×b}) = (( )^b)^{-1}(ker P₀^×) has order ν·|ker P₀^×| ∈ N = N₀, so (Tors) holds; conversely infinite kernel violates (Tors). (d) is (b)+(c) plus the suspension relation from (A10). ∎

**Answers to the three sub-questions of task item (3).**

* **What excludes the bad limits: (Tors), i.e. the class.** Not the topology. A limit P₀^b with infinite ker(( )^b) is a perfectly good point of X⃗(C) — multiplicative, with P^{-1}(0) = p̄_x — it merely fails (Tors), which every admissible E requires by Definition 4.1 (A8). For E ⊊ E_tors the exclusion can bite earlier (E itself may fail), but (Tors) is the universal mechanism. The topology's only role is to make "limit" mean something, and it does so through the **subspace** topology of X⃗(C)_E inside X⃗(C) (A6) plus the Hausdorffness of the ambient C^{Z̄}: a net converging in C^{Z̄} to a point outside X⃗(C)_E cannot converge in X⃗(C)_E to anything. The note's "they leave the space" is therefore correct in substance but does not say *which* space, and does not supply the ambient-Hausdorff step that turns "the natural limit is outside" into "there is no limit inside". Both belong in the replacement text.
* **Is the "zero component" the only failure mode? No** — finding F3 (MINOR). The note writes "limits with some component of b equal to 0 kill a μ_{ℓ^∞} and violate (Tors)". By O.5(c) the (Tors) locus in Ẑ_(p) is ⋃_{p∤ν} νẐ×_(p), whose complement also contains every b with all components nonzero but infinitely many of positive valuation. Explicit witness: **b = (b_l)_{l≠p} with b_l = l for every l ≠ p.** Every component is nonzero, yet ker(( )^b) = ⊕_{l≠p} μ_l is infinite, so P₀^b violates (Tors) and is not a point of X̌₀(C)_E. The note's characterization of the escaping set is thus incomplete, and its "so they leave the space" happens to still be true for the cases it names, but for a reason it states too narrowly.
* **Does it matter for the closure computed in X₀? No, and this is worth being precise about.** X₀ is built from X̌₀(C)_E and nothing else; points violating (Tors) are simply not in X₀, so they cannot be in cl_{X₀}(γ) whatever they do in C^{Z̄}. The escaping-limits analysis is therefore *not needed* for the ⊆ direction at all. Its only genuine role is negative: it shows that the naive "compactify Ẑ_(p) and read off the closure" picture is wrong, because the compactification adds points that are not in the space — which is exactly why the closure has to be computed by a method that never leaves X₀. §6 gives such a method. (And note the ambient warning from (A15): the (Tors) locus is *dense* in X⃗(C), so "escaping" is generic, not exceptional.)

---

## 6. Task item (4) and the repair: the closure meets no other stratum, because packets are closed

### 6.1 Proposition O.1 — every packet is a closed subset of the suspension

> **Proposition O.1.** Let X₀ be an arithmetic scheme ([x-03] §7: integral normal with countable function field K₀), C algebraically closed satisfying the conditions before Cor. 4.4, E an admissible class (Def. 4.1), and X₀ = X̌₀(C)_E ×_{Q₀^{>0}} R^{>0} the suspension with its quotient topology. Let x₀ be a point of X₀ with finite residue field. Then
> **Γ^E_{x₀} is a closed, flow-invariant subset of X₀**, and the packets, together with the union of all the other strata, partition X₀ into fibres of a continuous flow-invariant map onto the scheme X₀.

*Proof.* Five steps, each with its anchor.

**Step 1 (a continuous map from the suspension to the base scheme).** By (A5)+(A6), pr_{X₀} : X̌₀(C)_E → X₀ is continuous, the target carrying the **Zariski** topology (this is what Lemma 7.1's proof means by "a closed subset A of X has the form A = {p ⊃ I}", (A2)). By (A7) it is Q₀^{>0}-invariant: pr_{X₀}(F_q(P₀)) = pr_{X₀}(P₀) for all q ∈ Q₀^{>0}. Hence the composite

  X̌₀(C)_E × R^{>0} → X̌₀(C)_E → X₀,  (P₀, u) ↦ pr_{X₀}(P₀)

is continuous and constant on Q₀^{>0}-orbits, since (P₀,u)q = (F_q(P₀), q^{-1}u). Because X₀ carries the quotient topology (A12), the universal property of quotient maps yields a **continuous** map

  **Π : X₀ → X₀,  Π([P₀, u]) = pr_{X₀}(P₀),  with Π ∘ q = pr_{X₀} ∘ pr₁.**

**Step 2 (Π is flow-invariant).** φ^t[P₀,u] = [P₀, ue^t] (A10), so Π ∘ φ^t = Π. Hence every fibre of Π is flow-invariant.

**Step 3 (a point with finite residue field is closed in X₀).** Let U = Spec A be an affine open containing x₀, corresponding to a prime p ⊂ A with Frac(A/p) = κ(x₀) finite. A/p is a domain contained in its finite fraction field, hence a finite domain, hence a field; so p is maximal and {x₀} is closed in U. Now let y ∈ cl_{X₀}({x₀}) and pick an affine open V ∋ y. Every open neighborhood of y meets {x₀}, so x₀ ∈ V; by the affine argument applied in V, {x₀} is closed in V, whence y = x₀. So **{x₀} is closed in X₀**. (For X₀ = Spec Z this is the statement that the maximal ideals (p) are closed points, and the generic point (0) is not among them.)

**Step 4 (the packet is a fibre of Π).** By (A9), C_{x₀} = pr_{X₀}^{-1}(x₀) computed inside X̌₀(C)_{Etors} — Deninger names it as the fibre, and the identification is immediate: every element of X̌₀(C)_{Etors} = colim_{N₀}X₀⃗(C)_{Etors} is F_ν^{-1}(z) with z ∈ X₀⃗(C)_{Etors}, and pr_{X₀}(F_ν^{-1}z) = pr_{X₀}(z) by (A7), so pr_{X₀}^{-1}(x₀) = ⋃_{ν∈N₀}F_ν^{-1}(pr₀^{-1}(x₀)) = C_{x₀}. Since E is admissible its characters satisfy (Tors) (A8), so X̌₀(C)_E ⊆ X̌₀(C)_{Etors} and therefore

  C^E_{x₀} = C_{x₀} ∩ X̌₀(C)_E = pr_{X₀}^{-1}(x₀) computed inside X̌₀(C)_E.

C^E_{x₀} is Q₀^{>0}-stable, so q^{-1}(Γ^E_{x₀}) = C^E_{x₀} × R^{>0} = q^{-1}(Π^{-1}(x₀)); as q is surjective, **Γ^E_{x₀} = Π^{-1}(x₀)**.

**Step 5 (conclusion).** {x₀} is closed in X₀ (Step 3), Π is continuous (Step 1), so Γ^E_{x₀} = Π^{-1}(x₀) is closed in X₀; flow-invariance is Step 2. ∎

**Second proof of the key closedness, by pointwise evaluation, for X₀ = Spec Z** — recorded because the task asks whether the note's chosen instrument can be made to work. It can, but the evaluation must be performed at a rational prime, not at roots of unity. It suffices to show C^E_{(p)} is closed in X̌₀(C)_E, since then Lemma O.0 finishes: given z ∈ cl_{X₀}(γ) and any representative (Q,v) ∈ q^{-1}(z), lift a net from γ to obtain P_β → Q with P_β ∈ q^{-1}(γ)'s first coordinate = Q^{>0}P₀ ⊂ C^E_{(p)}, so Q ∈ cl(C^E_{(p)}) = C^E_{(p)} and z ∈ Γ^E_{(p)}. To see C^E_{(p)} closed: let P_β → Q in X̌₀(C)_E with P_β ∈ C^E_{(p)}. The chart F_ν^{-1}(X₀⃗(C)_E) containing Q is open (A4/A6), so the net is eventually inside it, and applying the homeomorphism F_ν we may assume P_β, Q ∈ X₀⃗(C)_E (F_ν preserves the fibre of pr_{X₀}, by (A7)). By Cor. 7.8's metric (A14) there are σ_β ∈ G with R_β := (representative of P_β)^{σ_β} → R (a representative of Q) **pointwise on Z̄**. Each R_β lies over a point of X above the prime p, so R_β(p) = 0 for every β; pointwise convergence at the single element r = p ∈ Z̄ gives R(p) = 0, i.e. p ∈ R^{-1}(0), i.e. R lies over (p). Hence Q ∈ C^E_{(p)}. ∎ This is Lemma 7.1's proof, evaluated at one element; it is the whole content, and it is what "the same pointwise evaluation" *should* have meant.

### 6.2 Theorem O.2 — the converse inclusion, and the equality

> **Theorem O.2.** Let X₀ = Spec Z, E admissible, p a prime, and γ ⊂ Γ^E_p a periodic orbit (a circle of length log p, Thm 6.1). Then
>   **cl_{X₀}(γ) ⊆ Γ^E_p**, and combined with the banked Theorem A (⊇), **cl_{X₀}(γ) = Γ^E_p.**
> More generally, for any arithmetic scheme X₀ and any x₀ with finite residue field, cl_{X₀}(S) ⊆ Γ^E_{x₀} for every subset S ⊆ Γ^E_{x₀}.

*Proof.* γ ⊆ Γ^E_p and Γ^E_p is closed (Proposition O.1); closure is monotone and idempotent on closed sets. The equality is Theorem A, adjudicated at referee grade with three independent derivations (`probe-9.3-adjudication.md` §2, §4 item 1). ∎

**This settles task item (4) completely.** cl(γ) meets no other stratum:
* not the **generic stratum** Π^{-1}(η₀): Π(cl(γ)) = {(p)} ∌ η₀;
* not **another prime's packet** Γ^E_{p′}, p′ ≠ p: distinct closed points of Spec Z;
* not, for a general higher-dimensional arithmetic X₀, **another closed point over the same rational prime**: distinct points of X₀, each closed by Step 3, so separated by Π. (The note's phrase "the char-p part" is ambiguous exactly here, and the ambiguity is now void.)
* and not any point outside X₀'s E-locus, since X₀ is built from X̌₀(C)_E only.

**Sanity checks against the adjudicated record — all pass.**
1. *No conflict with the non-Hausdorffness (adjudication §3, Cor. A.2).* Both limits produced there, [(x,χ^c),v] and [P₀,w*], lie inside Γ^E_p. Closedness of the packet and non-Hausdorffness *of* the packet are independent; the packet's own subspace topology is non-Hausdorff and the packet is closed in X₀.
2. *No conflict with "no periodic orbit is closed" (adjudication §4 item 3).* Orbits are not closed; packets are. Theorem A says each orbit is dense in its packet, so an orbit is closed iff its packet is a single orbit, which by uncountability of B_p = Ẑ×_(p)/p^Ẑ never happens for E ⊇ E_f.
3. *No conflict with connectedness (Cor. 9.7, (A16)).* For X₀ flat of finite type over Spec Z and E ⊇ E_f — in particular for X₀ = Spec Z and every E in the certified window — Γ^E_p is closed but has **empty interior**: the generic stratum is dense in X₀ (Thm 9.2 together with Cor. 9.7's proof, (A16)) and is disjoint from Γ^E_p. So Γ^E_p is closed and nowhere dense; X₀ stays connected. Had the packet been *clopen*, connectedness would have been contradicted — this is a genuine consistency test and the theorem passes it. Note the asymmetry that makes all of this coherent: cl({η₀}) = Spec Z, so limits may pass from the generic stratum into the packets (and by Thm 9.2 they do), but never out of a packet, since cl({(p)}) = {(p)}.
4. *No conflict with Theorem 7.10's "not homeomorphisms in general" (p. 47).* Theorem 7.10 exhibits the disjoint-union decomposition only as a continuous bijection; Proposition O.1 recovers exactly one topological consequence of that decomposition — closedness of the char-x₀ pieces — and *not* their openness, which is precisely the part that fails (openness of all pieces would disconnect X₀).

### 6.3 Corollaries now available

> **Corollary O.3 (Corollary A.1's headline, now proved).** Γ^E_{x₀}, when nonempty, is a **minimal set** of the flow on X₀: nonempty, closed (O.1), flow-invariant (O.1), and every orbit in it is dense in it (Theorem A). Hence it contains no proper nonempty closed invariant subset, and it *is* the smallest closed invariant set containing any one of its orbits, and it is the orbit closure of each of its points.

> **Corollary O.4 (Deninger's "compact packets", verified for E ⊇ E_f).** For E ⊇ E_f one has C^E_{x₀} = C_{x₀} (Thm 5.2, (A10)) and Γ_{x₀} is compact. *Proof.* Let Σ = pr_{X₀}^{-1}(x₀) ∩ X₀⃗(C)_{p,in} be the "ρ = 1" slice (Prop. 5.1, p. 34: ρ(Q̌) = 1 iff Q̌ = (x,Q^×) with Q^× injective on μ(κ(x))). Upstairs, the fibre of pr_X over a fixed x ∈ X above x₀ intersected with X⃗(C)_{in} is, via a ↦ χ_x ∘ ( )^a, the continuous injective image of the compact group Ẑ×_(p) = ∏_{l≠p} Z_l^× (closed in the compact Ẑ_(p)); the map is continuous by the argument of O.5(a) and lands in the Hausdorff X⃗(C), hence is a homeomorphism onto its image, which is therefore compact. Σ is its image under the continuous π, hence compact. F_p restricts to a homeomorphism of the characteristic-p locus (p. 46, verbatim: "the Frobenius endomorphisms F_p of X⃗(C) and X₀⃗(C) restrict to homeomorphisms F_p of X⃗(C)_p and X₀⃗(C)_p") and preserves Σ, so Γ_{x₀} = q(Σ × [1, Nx₀]) is a continuous image of a compact set, hence compact. ∎ Together with O.1: for E ⊇ E_f the packets are **compact, closed, nowhere dense, non-Hausdorff, flow-invariant minimal sets**. For a general admissible E, O.1 (closed) still holds; compactness needs the E-locus to be closed in Σ and is not claimed.

> **Corollary O.6 (the Morishita flag, sharpened — see F6).** With O.1 + Theorem A + adjudication Cor. A.2: in the subspace topology of X₀, Γ_p is closed and compact but **not Hausdorff**, and its orbits γ_{p,a} are **not closed** (each is dense in Γ_p). Hence [r3s-08] Thm 2.2.9(1)'s "R₊-equivariant homeomorphism Ẑ×_(p)/Np^Ẑ ×_{p^Z} R₊ → Γ_p" (printed p. 17) is false if Γ_p carries the subspace topology of X₀ — the source is compact Hausdorff and the target is not Hausdorff — and 2.2.9(2)'s "decomposition into connected closed R₊-orbits" (printed p. 18) is false in that topology. Both are correct as *model* descriptions of the underlying R₊-set, which is what [x-03] (38)–(39) and §6 supply (Deninger says **bijection**, verbatim in (A10)).

---

## 7. Break attempts (mandated: try to falsify what I just proved)

I tried four routes to a counterexample; all fail, and each failure localizes exactly one hypothesis.

1. **Attack the topology on X₀.** If X₀ carried a topology strictly *coarser* than the quotient topology, Π could fail to be continuous and packets could fail to be closed. Closed by (A12): §10 p. 63's `(π_∗C⁰_X̃)^Q = C⁰_X` forces the quotient topology, and [x-06] p. 11 writes the suspension as a quotient outright. Any *finer* topology leaves the proof intact. **No counterexample.**
2. **Attack Step 3 with a non-closed point of finite residue field.** If some x₀ with κ(x₀) finite were not closed in X₀, its packet would be Π^{-1}(x₀) with {x₀} non-closed and the argument would stall. Step 3 shows this cannot happen in *any* scheme: a prime with finite residue field is maximal in every affine chart, and closedness globalizes. **No counterexample.**
3. **Attack Step 4 by finding a packet point not in the fibre, or a fibre point not in the packet.** This is where a real gap could hide: the packet is defined in [x-03] via the parametrizations (35)–(39), and one might fear Γ^E_{x₀} is a proper subset of the fibre (e.g. only the "unit-exponent" twists). It is not: (A9) defines C_{x₀} as pr₀^{-1}(x₀)Q₀^{>0}, i.e. as the full Q^{>0}-saturated fibre, and Deninger's own opening sentence calls it the fibre. The parametrization (38) is then a *theorem about* the fibre, not its definition. **No counterexample.** (Had the packet been defined as a proper subset of the fibre, the honest verdict would have been ⊆ *fibre* only, and the ⊆ direction would be open. It is worth stating explicitly that this hinged on a definitional reading, and that the reading was checked verbatim.)
4. **Attack via a limit that "changes characteristic".** Concretely: can a net in Γ^E_p converge in X₀ to a generic-stratum point? By Theorem 9.2/Cor. 9.7 the generic stratum is dense, so generic points sit arbitrarily close to packet points; the question is whether the *limit* can be generic. It cannot: evaluation at r = p is identically 0 along the net and hence 0 in the limit (second proof, §6.1), so the limit's prime contains p. Equivalently, Π is continuous into a topology in which {(p)} is closed. **No counterexample** — and note the converse *does* happen, which is why the asymmetry is the content.

**Attempt to break the note's own argument instead of the statement.** Successful, and this is finding F1. Consider the honest question the sketch is answering: "what are the limits of {F_n(P₀)}_{n∈N}?" — and compare with the question that must be answered: "what are the limits of nets in γ = {[P₀,w] : w ∈ R^{>0}}?". These differ in three ways, each fatal to the sketch as a proof:
 (i) γ is a *circle*, i.e. the image of all of R^{>0}; the points [P₀, nu] with n ∈ N form a countable subset of it, and the identity [P₀, nu] = [F_n(P₀), u] only rewrites *those*. A net [P₀, w_α] with w_α ∈ R^{>0} ∖ (N·u ∪ Q^{>0}·u) is not covered at all.
 (ii) Even for the covered points, every point of X₀ has a whole Q^{>0}-orbit of representatives, and a convergent net in X₀ may only be liftable after passing to a subnet and after *choosing* the fibre point (Lemma O.0). The sketch reasons as if the representatives (P₀, n_k u) themselves converged upstairs; they do not (they are exactly the sequence with two suspension-limits in adjudication §3, and upstairs they converge to nothing).
 (iii) The sketch's conclusion is asserted "by compactness of Ẑ_(p)", i.e. by compactifying the exponent parameter. But the compactification adds points *outside* the space (§5), so compactness delivers no limit inside X₀ and cannot, by itself, bound the closure. In the sketch's own terms, compactness is used to produce candidates and (Tors) to discard some of them; nothing shows the list of candidates is exhaustive for nets in γ.
So the sketch establishes Proposition O.5 (true, and worth keeping) and does not establish Corollary A.1's converse inclusion (also true, by an unrelated argument).

---

## 8. FINDINGS, with severities, locations and exact replacement text

### F1 — MAJOR. `probe-9.3-b.md` §5, Corollary A.1, the parenthesis. The stated argument is not a proof of the converse inclusion.
It computes the subnet limits of the single sequence {F_n(P₀)}_{n∈N} upstairs in one chart, whereas cl_{X₀}(γ) is the closure of the full circle γ in the suspension. The gaps: γ is not exhausted by {[P₀, nu]}_{n∈N}; convergence in X₀ does not lift to convergence of representatives (the Q^{>0}-action is not properly discontinuous, [x-03] p. 49), so "the same pointwise evaluation" is unavailable downstairs without Lemma O.0; and compactness of Ẑ_(p) produces candidate limits outside the space, so it bounds nothing by itself. *The statement is nevertheless true.* **Replacement text (drop the parenthesis, and add Proposition A.1′ + proof):**

> **Proposition A.1′ (packets are closed; the converse inclusion).** Let X₀ be an arithmetic scheme, E admissible, x₀ a point of X₀ with finite residue field, and X₀ = X̌₀(C)_E ×_{Q₀^{>0}} R^{>0} with its quotient topology ([x-03] §10 p. 63, where (π_∗C⁰_X̃)^Q = C⁰_X; [x-06] p. 11). Then Γ^E_{x₀} is a closed, flow-invariant subset of X₀. Consequently cl_{X₀}(γ) ⊆ Γ^E_{x₀} for every periodic orbit γ ⊂ Γ^E_{x₀}, and with Theorem A, cl_{X₀}(γ) = Γ^E_{x₀}.
> *Proof.* The projection pr_{X₀} : X̌₀(C)_E → X₀ is continuous into the Zariski topology of the scheme X₀ ([x-03] Lemma 7.1 and p. 42, p. 43; the E-version by p. 47) and is Q₀^{>0}-invariant, Q₀^{>0} acting trivially on X₀ ([x-03] p. 27). Hence (P₀,u) ↦ pr_{X₀}(P₀) is continuous on X̌₀(C)_E × R^{>0} and constant on Q₀^{>0}-orbits, so it descends to a continuous map Π : X₀ → X₀ with Π([P₀,u]) = pr_{X₀}(P₀). Π is constant along flow lines, so its fibres are flow-invariant. By [x-03] p. 31, C_{x₀} is by definition the fibre pr_{X₀}^{-1}(x₀) in X̌₀(C)_{Etors}; since admissible classes satisfy (Tors), C^E_{x₀} = C_{x₀} ∩ X̌₀(C)_E is the fibre of pr_{X₀} over x₀ in X̌₀(C)_E, and therefore Γ^E_{x₀} = Π^{-1}(x₀). Finally a point with finite residue field is a closed point: in any affine open Spec A around it, A/p is a domain with finite fraction field, hence a finite field, so p is maximal; and if y lies in the closure of {x₀} then any affine open containing y contains x₀, so y = x₀. Thus {x₀} is closed in X₀ and Γ^E_{x₀} = Π^{-1}(x₀) is closed in X₀. ∎
> **Corollary A.1 (packets are minimal sets).** Γ^E_{x₀}, when nonempty, is nonempty, closed and flow-invariant (Proposition A.1′) and every one of its orbits is dense in it (Theorem A); hence it is a minimal set, it is the orbit closure of each of its points, and it is the smallest closed invariant set containing any one of its orbits.

### F2 — MAJOR. Same location. The conclusion is mis-scoped: "one gets cl(γ) ∩ (char-p part) = Γ^E_p exactly."
The hedge "∩ (char-p part)" is (i) undefined — the note never says whether "the char-p part" is the stratum over the single point (p) or the union of all strata of residue characteristic p, a distinction with content as soon as dim X₀ ≥ 2 — and (ii) unnecessary, since cl(γ) meets no other stratum whatsoever. **Replacement text:**

> cl_{X₀}(γ) = Γ^E_{x₀}, with no intersection taken: the closure meets neither the generic stratum, nor the packet of any other point of X₀ (of the same or of a different residue characteristic), because Π(cl(γ)) ⊆ cl({x₀}) = {x₀} in the Zariski topology of X₀.

### F3 — MINOR. Same location: "limits with some component of b equal to 0 kill a μ_{ℓ^∞} and violate (Tors)" — incomplete.
**Replacement text:**

> P₀^b satisfies (Tors) if and only if ker(( )^b : μ^{(p)} → μ^{(p)}) = ⊕_{l≠p} μ_{l^{v_l(b_l)}} is finite, i.e. if and only if b ∈ ⋃_{ν∈N, p∤ν} ν·Ẑ×_(p); equivalently, every component b_l is nonzero and v_l(b_l) = 0 for almost all l. Both failure modes occur: b with a zero component (which kills all of μ_{l^∞}), and b with every component nonzero but infinitely many of positive valuation — for instance b = (l)_{l≠p}, for which ker(( )^b) = ⊕_{l≠p} μ_l is infinite. In either case P₀^b is a point of X⃗(C) (it is multiplicative with the same zero set) but not of X⃗(C)_{Etors}; since X⃗(C)_E carries the subspace topology of X⃗(C) and the ambient C^{Z̄} is Hausdorff, the corresponding subnet has no limit in X⃗(C)_E at all. Compare [x-03] Prop. 9.1 (p. 53): for N₀ = N, X⃗(C)_{Etors} is dense in X⃗(C), so such escapes are generic, not exceptional.

### F4 — MINOR. Bookkeeping: the ⊆-dependence of "packets are minimal sets".
The note's Corollary A.1 title and its clauses "is the orbit closure of each of its points" and "is the smallest closed invariant set containing any one of its orbits" all require the ⊆ direction, which the note itself labels proposition-grade; the adjudication (§4 item 1) re-publishes "packets are minimal sets" at referee grade. **Replacement text for `probe-9.3-adjudication.md` §4 item 1 (adjudicator to apply):**

> …packets are minimal sets — nonempty, closed, flow-invariant, with every orbit dense (the density from Theorem A; the closedness from Proposition A.1′ / referee report `results/c3-r/referee-s14/B-corA1-O.md` §6.1, which supplies the converse inclusion that Cor. A.1 had left at proposition grade)…

and in §4 item 6, replace "probe B's Cor. A.1 converse inclusion (flagged proposition-grade by B itself; not load-bearing)" with:

> probe B's Cor. A.1 converse inclusion — **now discharged at referee grade** (referee report O, 2026-09-02): the statement is true and stronger than claimed (every packet is closed in X₀, for every arithmetic scheme and every admissible E), but probe B's argument for it does not prove it and is replaced.

### F5 — MINOR. The topology on the suspension is never cited.
`probe-9.3-b.md` §3.1 says only "the suspension X₀ carries the quotient topology (implicit throughout §§8, 10, e.g. 'topological closure' in §8, the sheaf-theoretic §10)". This is load-bearing for the ⊆ direction. **Replacement text:**

> the suspension X₀ carries the quotient topology of X̌₀(C)_E × R^{>0}. [x-03] does not state this in §6; the warrant is §10 p. 63, where the identity (π_∗C⁰_X̃)^Q = C⁰_X for π : X̃ = M × R^{>0} → X = M ×_Q R^{>0} says exactly that Q-invariant continuous functions upstairs are continuous functions downstairs, and [x-06] p. 11, "Set X₀ = (X̌₀(C) × R^{>0})/Q^{>0}". Note also that the quotient map q is open (Q^{>0} acts by homeomorphisms, [x-03] Prop. 7.4b) but not proper, and the Q^{>0}-action is not properly discontinuous ([x-03] p. 49), so q does not reflect convergence.

### F6 — MINOR (a sharpening of the existing W11 flag, not a defect of the note).
`probe-9.3-b.md` §3.3 and adjudication §4 item 4 say the Morishita "homeomorphism" wording "cannot be read as the subspace topology of Γ_p". With O.1 the flag can now be stated exactly, and it moves: the *packet* is closed and (for E ⊇ E_f) compact in X₀, so nothing is wrong with treating Γ_p as a compact subset; what fails is (a) Hausdorffness of Γ_p in the subspace topology, which kills [r3s-08] Thm 2.2.9(1)'s homeomorphism claim outright (a compact Hausdorff model cannot be homeomorphic to a non-Hausdorff space), and (b) closedness of the *orbits* γ_{p,a}, which kills the reading of Thm 2.2.9(2)'s phrase "connected closed R₊-orbits" (printed p. 18) in that topology. **Replacement text for the ledger's W11 row:** "[r3s-08] Thms 2.2.8/2.2.9 give model bijections, not subspace-topology statements: Γ_p ⊂ X₀ is closed (referee O, Prop. O.1) and, for E ⊇ E_f, compact — but non-Hausdorff (adjudication §3), so 2.2.9(1)'s homeomorphism onto the compact Hausdorff mapping-torus model is false in the subspace topology; and its orbits are dense in Γ_p (Theorem A), so 2.2.9(2)'s 'closed R₊-orbits' is false there too. Harmless to the class-field-theoretic content; never cite for topology."

---

## 9. What is now established at referee grade, and its precise scope

**Established.** For every arithmetic scheme X₀ in the sense of [x-03] §7, every algebraically closed valued C admissible for the construction, every admissible class E in the sense of Definition 4.1, and every point x₀ of X₀ with finite residue field, the packet Γ^E_{x₀} is a **closed, flow-invariant** subset of the suspension X₀ = X̌₀(C)_E ×_{Q₀^{>0}} R^{>0} with its quotient topology — indeed it is the fibre over x₀ of a continuous flow-invariant map Π : X₀ → X₀ onto the base scheme with its Zariski topology. Consequently, for X₀ = Spec Z, where Theorem A is banked, the closure of any single periodic orbit γ ⊂ Γ^E_p is **exactly** Γ^E_p, with no "char-p part" hedge, no chart caveat, and no residual proposition-grade content: the ⊇ half is the adjudicated Theorem A, the ⊆ half is Proposition O.1 above, proved from three verbatim ingredients of [x-03] (continuity of pr_{X₀} into the Zariski topology, its Q^{>0}-invariance with trivial action on the base, and the definition of C_{x₀} as the fibre) plus the elementary fact that a point with finite residue field is closed. Corollary A.1's headline is therefore true as stated: each packet is a **minimal set** of the flow, the orbit closure of each of its points, and the smallest closed invariant set containing any one of its orbits; for E ⊇ E_f it is in addition **compact** (verifying, with a proof, Deninger's unproved assertion at [x-03] p. 2 and [x-06] p. 12) and **nowhere dense** (the generic stratum is dense, [x-03] Thm 9.2/Cor. 9.7), which is what reconciles closedness with the connectedness of X₀. **Scope limits, stated honestly:** (i) the result is about the topology of X₀ and says nothing about the mapping face of S4 — a compact non-closed invariant subspace, or a continuous equivariant image, is untouched, and the adjudication's Q* (§5) is unchanged in every respect; (ii) for admissible E ⊊ E_f the packet may be empty or non-compact — closedness survives, compactness is not claimed; (iii) the proof consumes the quotient topology on the suspension, whose on-disk warrant is [x-03] §10 p. 63 and [x-06] p. 11 rather than an explicit sentence in §6, and a strictly coarser topology on X₀ would void it; (iv) Q-c of the note's §7 ("whether the equality holds verbatim in every chart of the colimit") is answered by dissolving it — the closure is computed once, in X₀, and no chart-by-chart verification arises, because the charts of X̌₀(C)_E are open and the statement is a global one about a fibre of a continuous map. **Priority:** the on-disk sources assert compactness and pairwise disjointness of the packets ([x-03] pp. 2–3, [x-06] p. 12) and give the packet's structure only as a bijection ([x-03] (38)–(39), §6 p. 38); none of them states that a packet is closed in X₀, and [r3s-08]'s Thm 2.2.9 asserts a homeomorphism that Corollary O.6 refutes in the subspace topology. One server-side web search was run this session (2026-09-02, "Deninger arithmetic schemes suspension packet closed subset orbit closure … periodic orbits") and returned only the primary sources themselves plus unrelated homogeneous-dynamics literature; **no deeper external sweep was performed for this item, and none is claimed.**

---

## 10. Sources read this session (page-by-page record)

**[x-03]** Deninger, *Dynamical systems for arithmetic schemes*, arXiv:1807.06400v4, `fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf` (119 pp.; printed page = PDF page, verified). Read in full at the stated pages: **pp. 2–3** (intro: compact packets, invariant tori, connectedness); **p. 7** (contents, for the section/page map); **pp. 26–30** (§4: (Tors), (Image), Def. 4.1, Prop. 4.2, (30)–(31) with the trivial Q^{>0}-action on the base, Lemma 4.3, Cor. 4.4, the examples E_tors/E_max/E_f/E_fg/E_fd/E_fd0, the "additive mod p / not N-invariant" remark, Prop. 4.5, Lemma 4.6); **pp. 31–34** (§5: (32)–(46), the definition of C_{x₀} as the fibre of pr_{X₀}, (34) Aut(κ(x)^×) = Ẑ×_(p), (35)–(39), the fibration over Ẑ×_(p)/p^Ẑ, ρ, Prop. 5.1, Thm 5.2); **p. 38** (§6: the suspension, the Q^{>0}-action, Γ_{x₀}, the R^{>0}-**bijection**, Γ^E_{x₀}, "If e.g. E_f ⊂ E then Γ^E_{x₀} = Γ_{x₀}"); **p. 39** (Thm 6.1 and the packet paragraph); **p. 40** (the Y₀ question; §7 opening: arithmetic schemes, pointwise convergence, metrizability; Lemma 7.1 with proof); **pp. 41–43** (Lemma 7.2, the glued topology, quotient by G, Lemma 7.3, the colimit topology and Prop. 7.4, continuity of pr_X, pr_{X₀} on the colimit); **pp. 44–45** (Props. 7.5, 7.6, 7.7, Cor. 7.8, Cor. 7.9); **pp. 46–47** (the remark on separatedness, the in-loci and their quotient/subspace agreement, Thm 7.10 and Remarks 1–2 "not homeomorphisms in general", the E-versions paragraph, (56)–(57)); **pp. 48–49** (r, (58)–(68), "The Q^{>0}-action … is not properly discontinuous"); **pp. 49–51** (§8: Claim 8.1, [Per11], X̌(C)_per, Thm 8.2 with proof, Lemma 8.3); **pp. 53–54** (§9 opening, X⃗(C)′, Prop. 9.1 with proof, Thm 9.2 with proof); **p. 57** (Thm 9.3, Lemma 9.4 setup); **pp. 60–62** (the r₀ map, the quotient-vs-subspace remark, (95)–(96), Cor. 9.7, Thm 9.8); **pp. 63–64** (§10: π : X̃ = M × R^{>0} → X = M ×_Q R^{>0}, R_X = (π_∗R_X̃)^Q ⊂ (π_∗C⁰_X̃)^Q = C⁰_X, the non-local-triviality remark, Def. 10.1).

**[x-06]** Deninger, *Primes, knots and periodic orbits*, arXiv:2301.11643, `fetched/x-06-deninger-2024-primes-knots-and-periodic-orbits.pdf`. Read: **printed pp. 11–12** (Thm 4.1, the colimit and the suspension X₀ = (X̌₀(C) × R^{>0})/Q^{>0}, the admissibility discussion, Thm 4.2 with the "compact subsets Γ_{x₀} … pairwise disjoint" sentence, the compact-packets paragraph, Thm 4.3 connectedness/almost path-connectedness).

**[r3s-08]** Morishita, arXiv:2508.15971v5, `fetched-r3/r3s-08-morishita-deninger-cc-bridge-2508.15971.pdf`. Read: **printed pp. 16–20** (Thm 2.2.8(1); Thm 2.2.9(1) the R₊-equivariant "homeomorphism" onto Γ_p as a mapping torus of multiplication by lk_p(p); Thm 2.2.9(2) γ_{p,a} ≅ R₊/Np^Z and "the decomposition into connected closed R₊-orbits"; the §2.3 covering/monodromy set-up).

**[D25]** Deninger, *Rational Witt vectors and associated sheaves*, arXiv:2508.05329v1, `fetched-r3/r3s-22-...pdf` — **not opened for this item**; nothing in Corollary A.1 or in the repair cites it, and I make no claim about it.

**Program files:** `results/c3-r/probe-9.3-adjudication.md` (in full); `results/c3-r/probe-9.3-b.md` (in full); `results/corpus-routing.md` (header caveats §§1–20 — none of them bears on x-03, x-06 or r3s-08 text extraction; caveat 14 confirms r3s-08 = arXiv:2508.15971 v5, title-page verified).

*Extraction method:* `pdftotext -layout` into the session scratchpad, then a page-tagged re-index; every quotation above was re-read from those extractions at the stated page. No third-party OCR was used and no derived text artifact was written into the corpora (corpus-routing caveats 1–2).

— end of referee report O —
