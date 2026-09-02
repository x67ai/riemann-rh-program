# REFEREE REPORT O — probe B, Corollary A.1: the converse inclusion cl(γ) ⊆ Γ^E_p

**Program:** RH program, direction C3-r (geometric substrate, reduced recommission). **Session 14 — 2026-09-02.**
**Referee:** O (Claude Opus 5), one of two independent referees on this item under standing order 7; the second referee is a different model. Nothing below is softened in the expectation that the other pass will catch it.
**Item under review:** Corollary A.1 of `results/c3-r/probe-9.3-b.md` — specifically the parenthetical that carries the converse inclusion (the note's own Q-c; adjudication §4 item 6, §5 Q-c).
**Read first, in full:** `results/c3-r/probe-9.3-adjudication.md`; `results/c3-r/probe-9.3-b.md`; the header caveats of `results/corpus-routing.md`.
**Standing order 5:** every source sentence quoted below was read this session from the on-disk PDF at the stated page, in a `pdftotext -layout` extraction made fresh in the session scratchpad. For [x-03] the printed page equals the PDF page (verified: PDF page 26 carries the printed folio "26"); likewise for [x-06] and [r3s-08]. Nothing below is recalled.

---

## 0. INDEPENDENCE DISCLOSURE — read this before weighing the verdict

This item has been refereed before. `results/c3-r/referee-s14/` already contained `B-corA1-F.md`, `B-corA1-O.md` and `B-corA1-adjudication.md` (timestamps 2026-09-02 02:10–02:24) when this pass began, and **both files I was instructed to read first already carry the earlier outcome inside them**:

- `probe-9.3-adjudication.md` §4 now opens with a dated block stating that the converse "is now DISCHARGED at referee grade … PASS-WITH-REPAIRS, 0 FATAL / 2 MAJOR", and names the mechanism ("it is the fiber over the closed point x₀ of a continuous map X₀ → X₀ descended from pr_{X₀}").
- `probe-9.3-b.md` §5 now carries a full "REFEREE PASS 2026-09-02" block with the replacement Proposition A.1′ and its proof.

**So this pass is not blind, and I will not claim that it is.** What I did do, and what the reader may rely on: I did **not** open `B-corA1-F.md`, `B-corA1-adjudication.md`, or the previous `B-corA1-O.md` body (I read only the first 20 and last 25 lines of the last, to establish that the slot was a re-run of the same item). Everything in §§2–8 below was re-derived this session from the on-disk primary sources, every anchor re-read at the page, and §7 records four separate attempts to *break* the result rather than to confirm it. Where I disagree with the severity or the scope recorded in the leaked blocks, I say so (see F3 and §9).

---

## 1. VERDICT

> ### PASS-WITH-REPAIRS
>
> **0 FATAL — 3 MAJOR — 4 MINOR.**
>
> **The claim is true, and true in a strictly stronger form than the note states.** There is no "char-p part" hedge and no chart caveat:
>
> **Proposition O.1.** For every arithmetic scheme X₀ in the sense of [x-03] §7, every admissible class E (Def. 4.1), and every point x₀ of X₀ with finite residue field, the packet Γ^E_{x₀} is a **closed**, flow-invariant subset of the suspension 𝕏₀ = X̌₀(C)_E ×_{Q₀^{>0}} R^{>0}.
>
> **Corollary O.2.** Hence cl_{𝕏₀}(A) ⊆ Γ^E_{x₀} for every subset A ⊆ Γ^E_{x₀}; in particular cl_{𝕏₀}(γ) ⊆ Γ^E_{x₀} for every periodic orbit γ ⊆ Γ^E_{x₀}. For X₀ = Spec Z, N₀ = N, where Theorem A is banked, **cl_{𝕏₀}(γ) = Γ^E_p exactly** — as subsets of the whole suspension, not of a stratum and not of a chart. Corollary A.1's headline ("packets are minimal sets") is therefore true, and only now proved.
>
> **The argument the note gives for it does not reach the statement** (F1, MAJOR); **its exclusion criterion is incomplete, and if it were complete the equality would be false** (F2, MAJOR); **the conclusion it does state is logically equivalent to Theorem A and so carries no converse content at all** (F3, MAJOR). All three are repaired below with exact replacement text. Four MINOR findings follow.
>
> **Novelty, honestly (standing order 7):** Proposition O.1 is **not a novel theorem.** It is one inference step from a sentence already in print — [r3s-08] p. 14 asserts that the projection pr_K from the suspension to the scheme is continuous — and the fibre description it needs is [x-03] p. 31 verbatim. The genuinely new content of this item is the *equality*, which needs Theorem A; and the new *negative* content is that Deninger's and Morishita's compactness/homeomorphism statements cannot be used to get here (§8, §9).

---

## 2. The text under review, quoted exactly

From `probe-9.3-b.md` §5, immediately after Theorem A (the original wording, preserved at the foot of the section beneath the later repair block):

> **Corollary A.1 (packets are minimal sets; the "invariant tori" made precise).** Every orbit of Γ^E_p is dense in Γ^E_p; Γ^E_p is the orbit closure of each of its points and is the smallest closed invariant set containing any one of its orbits. (With Step 5's converse inclusion — every limit of {F_n(P₀)}_n along any subnet is P₀^b for some b ∈ Ẑ_{(p)}, by compactness of Ẑ_{(p)} and the same pointwise evaluation; limits with some component of b equal to 0 kill a μ_{ℓ^∞} and violate (Tors), so they leave the space — one gets cl(γ) ∩ (char-p part) = Γ^E_p exactly. Stated proposition-grade; the kill only needs ⊇.)

Three assertions are in play and must be separated:

- **(A1-head)** every orbit of Γ^E_p is dense in Γ^E_p; Γ^E_p is the orbit closure of each of its points; Γ^E_p is the smallest closed invariant set containing any one of its orbits.
- **(A1-mech)** every subnet limit of {F_n(P₀)} is P₀^b with b ∈ Ẑ_{(p)}; those with a zero component violate (Tors) and leave the space.
- **(A1-concl)** cl(γ) ∩ (char-p part) = Γ^E_p.

(A1-head) is what the program uses (adjudication §4 item 1: "packets are minimal sets"). (A1-concl) is what the parenthetical delivers. **They are not the same statement**, and the gap between them is the whole item.

**Notation used in this report.** X₀ is the *scheme* (Deninger's base); 𝕏₀ is the *dynamical system* X̌₀(C)_E ×_{Q₀^{>0}} R^{>0}. [x-03] overloads "X₀" for both; the note inherits the overload, which is one reason (A1-concl)'s "char-p part" reads ambiguously. q : X̌₀(C)_E × R^{>0} ↠ 𝕏₀ is the suspension quotient map; π : X•(C) ↠ X•₀(C) and π̌ : X̌(C) ↠ X̌₀(C) are the Galois quotients; F_ν are the Frobenius endomorphisms.

---

## 3. Task item (1)–(2): the exact topology on 𝕏₀, re-derived, and whether "pointwise convergence" describes it

The task memo points at "[x-03] §§3–5" for the topology. **That pointer is wrong and I did not use it**: §§3–5 are purely set-/monoid-theoretic (§3's Prop. 3.7 does put a topology on κ(x)^×, but that is the *source* of the characters, not the character space). The topology is built in **§7, pp. 40–47**, and the suspension's topology is used in **§§9–10, pp. 61–63**. The note cites §7 correctly.

### 3.1 The affine chart: pointwise convergence, verbatim

[x-03] p. 40, §7 opening:

> "We begin with the affine case X₀ = spec R₀ and write X = spec R. Viewing X•(C) as a set of multiplicative maps P : R → C as in Remark 3.4 we give X•(C) the topology of pointwise convergence. It is the subspace topology induced by the Tychonov topology of C^R = ∏_R C on X•(C) via the inclusion X•(C) ⊂ C^R, P ↦ (P(r))_{r∈R}. Since R is countable, X•(C) is a metrizable topological space."

So on the affine chart, and *only* there to begin with, "pointwise convergence of multiplicative maps" is exactly right, and the space is metrizable — sequences suffice.

Two facts proved immediately afterwards will be used repeatedly.

[x-03] p. 40, **Lemma 7.1** and its proof, verbatim:

> "Lemma 7.1. For affine arithmetic schemes X₀, the natural map pr_X : X•(C) → X, (x, P^×) ↦ x or P ↦ p = P^{-1}(0) is continuous.
> *Proof.* A closed subset A of X has the form A = {p ⊃ I} for some ideal I in R. Consider a convergent sequence P_n → P in X•(C) where P_n ∈ pr_X^{-1}(A) for all n, i.e. p_n = P_n^{-1}(0) ⊃ I. Since P_n(r) → P(r) for all r ∈ R, it follows that P(r) = 0 for r ∈ I and hence p = P^{-1}(0) ⊃ I i.e. P ∈ pr_X^{-1}(A). Hence pr_X^{-1}(A) is closed and therefore pr_X is continuous."

[x-03] p. 41, **Lemma 7.2**: "The space X′•(C) is an open subspace of X•(C)" for an open affine X′₀ ⊂ X₀.

### 3.2 Gluing to a general arithmetic scheme, and the Galois quotient

[x-03] pp. 41–42: for a general arithmetic scheme, "We give X•(C) the topology for which O ⊂ X•(C) is open if and only if O ∩ X′•(C) is open in X′•(C) for any X′₀", and it suffices to test on one affine open cover. Then p. 42, verbatim:

> "Let G = Aut_{K₀}(K). We equip X•₀(C) = X•(C)/G with the quotient topology. Using Lemma 7.1 one sees that pr_X : X•(C) → X and hence also pr_{X₀} : X•₀(C) → X₀ are continuous."

### 3.3 The colimit: the charts are clopen, so the colimit topology restricts to pointwise convergence

[x-03] p. 42, **Lemma 7.3**: G acts by homeomorphisms and "the injective maps F_ν : X•(C) ↪ X•(C) for ν ∈ N are continuous, closed and open. In particular F_ν(X•(C)) is closed and open in X•(C)."

[x-03] p. 43, verbatim:

> "We give X̌(C) = colim_{N₀} X•(C) the inductive limit topology. It is the finest topology such that for all ν ∈ N₀ the inclusions F_ν^{-1}|_{X•(C)} : X•(C) ↪ X̌(C) are continuous. Thus Z ⊂ X̌(C) is closed, resp. open if and only if F_ν(Z) ∩ X•(C) is closed, resp. open in X•(C) for all ν ∈ N₀."

> "Proposition 7.4. a) X•(C) is a closed and open subspace of X̌(C). b) F_q : X̌(C) → X̌(C) is a homeomorphism for every q ∈ Q₀^{>0}. c) The group G acts by homeomorphisms on X̌(C)."

> "We give X̌₀(C) = X̌(C)/G the quotient topology. Then X̌₀(C) is homeomorphic to colim_{N₀} X•₀(C) with the inductive limit topology. The projections π : X•(C) → X•₀(C) and π̌ : X̌(C) → X̌₀(C) are continuous and since G acts by homeomorphisms, also open. Moreover the projections pr_X : X̌(C) → X and pr_{X₀} : X̌₀(C) → X₀ are continuous."

**Consequence I derive (this is the honest answer to task item (2)).** By Prop. 7.4 a) plus b), each chart U_ν := F_ν^{-1}(X•(C)) is **open and closed** in X̌(C), and the U_ν form an increasing directed family covering X̌(C). Therefore:

- **(T1)** For U open, cl_{X̌}(A) ∩ U = cl_U(A ∩ U). Hence closures in X̌(C) are computed chart-by-chart, and inside a chart the topology is (a Frobenius transport of) pointwise convergence. In this precise sense the colimit topology is **not finer than pointwise convergence on any chart** — it agrees with it there.
- **(T2)** Every net in X̌(C) that converges to z ∈ U_ν is **eventually in U_ν** (U_ν is an open neighborhood of z) and converges there. Hence no net inside one chart can "escape" the chart in the limit, and — since U_ν is also *closed* — no net inside U_ν can converge to a point outside U_ν either. So the colimit topology creates **no new limits and destroys none**: the "finer colimit vs. pointwise" worry that the task memo raises is real in general but **does not arise here**, because Deninger's charts are clopen and his Frobenii are homeomorphisms onto clopen images.

[x-03] p. 47 extends all of this to the E-loci, verbatim:

> "Given an admissible class E as in Definition 4.1 we equip X•(C)_E and X•₀(C)_E with the subspace topologies of X•(C) and X•₀(C). … We give X̌(C)_E = colim_{N₀} X•(C)_E and X̌₀(C)_E = colim_{N₀} X•₀(C)_E the inductive limit topologies. They agree with the subspace topologies via X̌(C)_E ⊂ X̌(C) and X̌₀(C)_E ⊂ X̌₀(C) because the subspaces F_ν^{-1}X•(C) and F_ν^{-1}X•₀(C) are open in X̌(C) resp. X̌₀(C) for all ν ∈ N₀. … **All preceding results in this section remain true if we replace X•(C) etc. by X•(C)_E etc.**"

That last sentence is the licence for using Lemma 7.1, Lemma 7.3, Prop. 7.4 and the continuity of pr_{X₀} in the E-setting. It is quoted here because the whole repair below leans on it.

### 3.4 The suspension: which topology, and what warrants it

[x-03] §6 p. 38 defines the suspension **as a set**:

> "consider the suspension X₀ = X̌₀(C)_E ×_{Q₀^{>0}} R^{>0}. It is the quotient of X̌₀(C)_E × R^{>0} by the right Q₀^{>0}-action given by (P₀, u)q = (P₀q, q^{-1}u) = (F_q(P₀), q^{-1}u) for q ∈ Q₀^{>0}."

No topology is named there, and I could find no sentence anywhere in [x-03] that says "we give the suspension the quotient topology" (I grepped the whole extraction for "quotient topology": it occurs on pp. 43, 44, 47, 49, 60, 61 — never for the suspension). This is a genuine, if small, gap in the note's §3.1, which calls the quotient topology "implicit". The warrants that do exist, all read this session:

1. **[r3s-08] p. 14, verbatim, for the identical construction** — the strongest warrant, and it is explicit:
   > "We equip X_K twith he quotient topology of the product X̌_K(C) × R₊." (the transposition "twith he" is in the source)
2. **[x-03] p. 61**, in the connectedness proof: after showing that the composition pr_X^{-1}(η) × R^{>0} ↠ pr_X^{-1}(η) ↠ Q₀^{>0}Ẑ^× is open, Deninger concludes "Since Q₀^{>0} acts by homeomorphisms on these spaces, we obtain a continuous open and surjective map π : X_η ↠ Y := Q₀^{>0}Ẑ^×/Q₀^{>0}." Deducing *continuity* of a map out of the suspension from continuity of its lift is exactly the universal property of the quotient topology; the step is invalid for any strictly coarser topology.
3. **[x-03] p. 63, §10**, for π : X̃ = M × R^{>0} → X = M ×_Q R^{>0}: "R_X = (π_∗R_X̃)^Q ⊂ (π_∗C⁰_X̃)^Q = C⁰_X" — the displayed identification of the sheaf of continuous functions downstairs with the Q-invariant continuous functions upstairs. Same page, the caution that matters for §8 below: "in general the continuous bijection π|_{M×{u}} : M × {u} → π(M × {u}) will not be a homeomorphism if π(M × {u}) is equipped with the subspace topology of X."
4. **[x-06] p. 11**: "Set X₀ = (X̌₀(C) × R^{>0})/Q^{>0} where Q^{>0} acts diagonally."

**Adopted, and flagged:** 𝕏₀ carries the quotient topology. Everything in §4 consumes this and nothing else about the suspension. If a future reader ever wants a *coarser* topology on 𝕏₀ (nobody in the program does), Proposition O.1 must be re-checked — see F5 and the scope note in §10.

### 3.5 Two properties of q that the item actually needs

- **q is open.** Q₀^{>0} acts on X̌₀(C)_E by homeomorphisms (Prop. 7.4 b) + p. 47), so for U open the saturation q^{-1}q(U) = ⋃_q U·q is open, hence q(U) is open. ✓
- **q is not proper, and the action is not properly discontinuous.** [x-03] p. 49, verbatim: "The Q^{>0}-action on Ȟ_{Etors} × R^{>0} is not properly discontinuous. In section 10, we will see that this works to our advantage." So q does **not** reflect convergence: a convergent net downstairs need not lift to a convergent net upstairs. This is precisely why the note's instrument (compute limits upstairs, at a fixed prime, of one sequence of characters) cannot by itself compute cl_{𝕏₀}(γ) — finding F1.

What *does* survive is the closure identity for open quotient maps, which I will use in the second proof:

> **Lemma O.0 (open-map closure identity).** If f : Y → Z is continuous, surjective and open, then f^{-1}(cl_Z A) = cl_Y(f^{-1}A) for every A ⊆ Z.
> *Proof.* f^{-1}(cl A) is closed and contains f^{-1}A, so it contains cl(f^{-1}A). Conversely let y ∉ cl(f^{-1}A); pick U ∋ y open with U ∩ f^{-1}A = ∅. Then f(U) is open, contains f(y), and misses A (if a ∈ f(U) ∩ A, write a = f(u) with u ∈ U; then u ∈ U ∩ f^{-1}A). So f(y) ∉ cl A, i.e. y ∉ f^{-1}(cl A). ∎

Applying Lemma O.0 to q and to γ, whose q-preimage is q^{-1}(γ) = O(P₀) × R^{>0} with O(P₀) = {F_r P₀ : r ∈ Q₀^{>0}} the full Q₀^{>0}-orbit:

  **cl_{𝕏₀}(γ) = q( cl_{X̌₀(C)_E}(O(P₀)) × R^{>0} ).**  (★)

(The product splits because cl(A × R^{>0}) = cl A × R^{>0}.) Equation (★) is the *correct* upstairs reduction. Note what it says: the relevant upstairs object is the closure of the **entire Q₀^{>0}-orbit** in the **whole colimit**, not the closure of the sequence {F_n P₀} in one chart. That is finding F1 in one line.

---

## 4. The repair, first proof: packets are fibres of a continuous map to the scheme

This is the short, complete, chart-free argument. It answers task items (3), (4) and (5) at once, because a fibre of a continuous map is closed, disjoint from every other fibre, and computed globally.

### 4.1 Ingredient 1 — the base action is trivial and the projection is continuous

[x-03] p. 27, verbatim, immediately after (30) and (31):

> "Both pr_X and pr_{X₀} are N₀-equivariant if we let N₀ act trivially on X₀ and X. Note that the maps pr_X and pr_{X₀} above extend Q₀^{>0}-equivariantly to maps pr_X : X̌(C)_E → X and pr_{X₀} : X̌₀(C)_E → X₀. **Here we let Q₀^{>0} act trivially on X and X₀.**"

So, as a set map, pr_{X₀}(F_q P₀) = pr_{X₀}(P₀) for all q ∈ Q₀^{>0}. And by [x-03] p. 43 ("the projections pr_X : X̌(C) → X and pr_{X₀} : X̌₀(C) → X₀ are continuous") together with p. 47 ("All preceding results in this section remain true if we replace X•(C) etc. by X•(C)_E etc."), the map

  pr_{X₀} : X̌₀(C)_E ⟶ X₀ (Zariski topology)

is continuous. Deninger's own proof of continuity in the colimit is worth recording because it is the only place where the colimit structure is consumed: "It suffices to show that pr_X is continuous, i.e. that pr_X ∘ (F_ν^{-1}|_{X•(C)}) : X•(C) → X is continuous for each ν ∈ N₀. Since pr_X = pr_X ∘ F_ν, this follows from the continuity of pr_X : X•(C) → X which was noted before Lemma 7.3." (p. 43)

### 4.2 Ingredient 2 — the packet is the pr-fibre, by Deninger's own definition

[x-03] p. 31, verbatim:

> "The fibres of pr_{X₀} : X̌₀(C)_{Etors} → X₀ are Q₀^{>0}-invariant. We will now analyze the structures of the Q₀^{>0}-sets C_{x₀} = pr_{X₀}^{-1}(x₀) in X̌₀(C)_{Etors} for points x₀ of X₀ whose residue field κ(x₀) is finite."

and, on the same page,

> "The fibre pr₀^{-1}(x₀) in X•₀(C)_{Etors} is N₀-invariant. Its extension to a Q₀^{>0}-invariant subset of X̌₀(C)_{Etors} is the set C_{x₀} = pr₀^{-1}(x₀)^{Q₀^{>0}} = ⋃_{ν∈N₀} F_ν^{-1} pr₀^{-1}(x₀) ⊂ X̌₀(C)_{Etors}."

[x-03] p. 34, Thm 5.2, defines C^E_{x₀} = C_{x₀} ∩ X̌₀(C)_E; and p. 38, §6, defines

> "For a point x₀ of X₀ with finite residue field of characteristic p set Γ_{x₀} = C_{x₀} ×_{Q₀^{>0}} R^{>0} ⊂ X₀. … We set Γ^E_{x₀} = C^E_{x₀} ×_{Q₀^{>0}} R^{>0} where C^E_{x₀} = C_{x₀} ∩ X̌₀(C)_E. If e.g. E_f ⊂ E then Γ^E_{x₀} = Γ_{x₀}."

**Sub-lemma (the two descriptions of C^E_{x₀} agree).** C^E_{x₀} = pr_{X₀}^{-1}(x₀) ∩ X̌₀(C)_E, i.e. C^E_{x₀} is the fibre of pr_{X₀} restricted to the E-locus.
*Proof.* ⊆ is immediate from C_{x₀} = pr_{X₀}^{-1}(x₀). For ⊇, let z ∈ X̌₀(C)_E with pr_{X₀}(z) = x₀. Write z = F_ν^{-1}(P) with P ∈ X•₀(C)_E for some ν ∈ N₀ (definition of the colimit). Since Q₀^{>0} acts trivially on X₀ (§4.1), pr₀(P) = pr_{X₀}(F_ν^{-1}P) = x₀, so P ∈ pr₀^{-1}(x₀); note P ∈ X•₀(C)_E ⊆ X•₀(C)_{Etors}, the inclusion holding because Definition 4.1 (p. 27) requires "the characters in E should satisfy (Tors)". Hence z ∈ F_ν^{-1}pr₀^{-1}(x₀) ⊆ C_{x₀}, and z ∈ X̌₀(C)_E. ∎
(Prop. 4.2, p. 27 — "It is foreward- and backward invariant under the N₀-action" — is what keeps the E-locus stable under F_ν^{±1}, so the intersection may be taken before or after applying F_ν without changing anything.)

### 4.3 Ingredient 3 — a point with finite residue field is a closed point

**Lemma O.3.** Let X₀ be a scheme and x₀ ∈ X₀ with κ(x₀) finite. Then {x₀} is closed in X₀.
*Proof.* Choose an affine open Spec A ∋ x₀, corresponding to a prime 𝔭 ⊂ A. Then A/𝔭 is an integral domain contained in its fraction field κ(x₀), which is finite; so A/𝔭 is a finite integral domain, hence a field, hence 𝔭 is maximal and {x₀} is closed in Spec A. For an arbitrary affine open V ⊆ X₀: if x₀ ∉ V then V ∩ {x₀} = ∅ is closed in V; if x₀ ∈ V then V ∩ {x₀} = {x₀} is closed in V by the same argument applied to V. Since closedness may be checked on an affine open cover, {x₀} is closed in X₀. ∎
For X₀ = Spec Z the points with finite residue field are exactly the (p), p prime, and the generic point (0) is not among them.

### 4.4 Proposition O.1 and its proof

> **Proposition O.1 (packets are closed).** Let X₀ be an arithmetic scheme ([x-03] §7 p. 40: integral normal with countable function field), C an algebraically closed field with a valuation satisfying the conditions before Corollary 4.4, E an admissible class (Def. 4.1, p. 27), and let 𝕏₀ = X̌₀(C)_E ×_{Q₀^{>0}} R^{>0} carry the quotient topology (§3.4). Then for every point x₀ of X₀ with finite residue field, the packet Γ^E_{x₀} is a **closed** and **flow-invariant** subset of 𝕏₀. Moreover the packets are pairwise disjoint and disjoint from the part of 𝕏₀ lying over any other point of X₀, in particular from the generic stratum.

*Proof.*

**(i) A continuous map 𝕏₀ → X₀.** Let h : X̌₀(C)_E × R^{>0} → X₀ be h(P₀, u) = pr_{X₀}(P₀). It is continuous (composite of the projection to the first factor with pr_{X₀}, both continuous — §4.1). It is constant on Q₀^{>0}-orbits: h((P₀,u)q) = h(F_q P₀, q^{-1}u) = pr_{X₀}(F_q P₀) = pr_{X₀}(P₀) = h(P₀,u) (§4.1, trivial action on the base). Since 𝕏₀ carries the quotient topology of q, h descends to a unique **continuous** map

  **Π : 𝕏₀ ⟶ X₀,  Π[P₀, u] = pr_{X₀}(P₀).**

**(ii) Π is flow-invariant.** The flow is φ^t[P₀,u] = [P₀, u e^t] ([x-03] p. 38: "We write φ^t for this action i.e. φ^t([P₀,u]) = [P₀, ue^t]"), which does not touch the first coordinate; so Π ∘ φ^t = Π for all t, and every fibre of Π is a flow-invariant set.

**(iii) The packet is a fibre.** q^{-1}(Γ^E_{x₀}) = C^E_{x₀} × R^{>0} (the set Γ^E_{x₀} is by definition the image of C^E_{x₀} × R^{>0}, and C^E_{x₀} is Q₀^{>0}-stable, so this product is q-saturated). By the Sub-lemma of §4.2, C^E_{x₀} × R^{>0} = h^{-1}(x₀) = q^{-1}(Π^{-1}(x₀)). Since q is surjective, **Γ^E_{x₀} = Π^{-1}(x₀)**.

**(iv) Closedness.** {x₀} is closed in X₀ (Lemma O.3), Π is continuous, hence Γ^E_{x₀} = Π^{-1}({x₀}) is closed in 𝕏₀.

**(v) Disjointness.** Fibres of a map are pairwise disjoint; and Π^{-1}(η₀) (η₀ the generic point) is disjoint from every Π^{-1}(x₀). ∎

> **Corollary O.2 (the converse inclusion, unhedged).** For every A ⊆ Γ^E_{x₀}, cl_{𝕏₀}(A) ⊆ Γ^E_{x₀}. In particular, for every periodic orbit γ ⊆ Γ^E_{x₀}, cl_{𝕏₀}(γ) ⊆ Γ^E_{x₀}: the closure meets no other packet and does not meet the generic stratum.
>
> **Corollary O.4 (equality; X₀ = Spec Z, N₀ = N, E admissible).** cl_{𝕏₀}(γ) = Γ^E_p — with ⊇ the banked Theorem A and ⊆ Corollary O.2. Consequently Γ^E_p is a nonempty closed flow-invariant set in which every orbit is dense, i.e. **a minimal set** of the flow, the orbit closure of each of its points, and the smallest closed invariant set containing any one of its orbits. **(A1-head) is proved.**

**Remark (why (v) settles task item (4) completely).** The question "can cl(γ) meet other strata?" is not a question about the char-p stratum at all; it is a question about the whole colimit and the whole suspension. Π answers it in one stroke, because a fibre is closed *in the total space*. Nothing chart-local is needed, and the "char-p part" hedge is dissolved rather than verified. This matters more than it looks: the generic stratum is **dense** in 𝕏₀ ([x-03] Cor. 9.7 proof, p. 62: "By Theorem 9.6 the spaces X_η and X_{0η₀} are connected. By Theorem 9.2 they are dense in X resp. X₀"), so an argument that only controlled the char-p behavior of a sequence would have left open the possibility that cl(γ) picks up generic-stratum points — and *a priori* that is exactly the direction in which a dense stratum invites accidents.

---

## 5. Second, independent proof: the note's own instrument, repaired and carried through

Proposition O.1 settles the item. But a referee pass owes the note an answer at the level of its own argument: *can* the pointwise-convergence computation be pushed to the conclusion, and what exactly does it give? The answer is yes, with five reductions the note does not make, and with a corrected (Tors) criterion. I carry it out because (a) it independently confirms Corollary O.4 without using Π, (b) it is where the note's actual error lives (F2), and (c) it makes the scope statement in §10 precise.

Throughout: X₀ = Spec Z, X = Spec Z̄ (normalization in Q̄), C = ℂ, N₀ = N, p a fixed prime, x ∈ X over (p), κ(x) = F̄_p, κ(x)^× = μ^{(p)} = ⨁_{ℓ≠p} μ_{ℓ^∞}. Fix the injective reference character χ = χ_x ([x-03] p. 32: "we obtain the injective character χ_x = ι ∘ i_x^{-1} : κ(x)^× ↪ C^×"). Write P_b := (x, χ^{b}) ∈ X•(C) for b ∈ Ẑ_{(p)} = ∏_{ℓ≠p} Z_ℓ, where χ^b = χ ∘ ( )^b; as a multiplicative map Z̄ → ℂ it is r ↦ χ(r̄)^b for r ∉ 𝔭_x and r ↦ 0 for r ∈ 𝔭_x. Normalize γ = {[P₀, w] : w ∈ R^{>0}} with P₀ = π(P_{a₀}), a₀ ∈ Ẑ^×_{(p)}, licensed by (35)/(38) on p. 32.

### 5.1 (R1) The exponent parametrization is a homeomorphism onto a compact set

**Lemma O.5.** β : Ẑ_{(p)} → X•(C), b ↦ P_{a₀ b}, is a homeomorphism onto a compact subset K ⊂ X•(C), and K ⊂ pr_X^{-1}(x).

*Proof.* **Continuity.** X•(C) carries pointwise convergence (p. 40). Fix r ∈ Z̄. If r ∈ 𝔭_x, b ↦ β(b)(r) = 0 is constant. If r ∉ 𝔭_x, then r̄ ∈ F̄_p^× = μ^{(p)} has finite order m prime to p, so b ↦ χ(r̄)^{a₀ b} depends only on a₀b mod m, i.e. it is **locally constant** in b. So every coordinate function is continuous, hence β is continuous into C^{Z̄} and therefore into the subspace X•(C). (This is the same computation Deninger performs in general at (56), p. 47: "Using ι, we have a topological isomorphism Ẑ → Ĥ, a ↦ (ζ ↦ ι(ζ)^a)", where Ĥ = Hom(μ(K), μ(C)) carries the topology of pointwise convergence — I re-derive it here for μ^{(p)} rather than μ(K) because that is the group in play, and because Deninger's (56) is stated for Ẑ, not Ẑ_{(p)}.)
**Injectivity.** χ^{a₀b} = χ^{a₀b′} on μ^{(p)} forces (a₀(b−b′)) to annihilate μ^{(p)} (χ injective), i.e. b = b′, since Ẑ_{(p)} = Aut(μ^{(p)}) acts faithfully ([x-03] p. 32, (34): "The group of automorphisms of the abelian group κ(x)^× is given by Ẑ^×_{(p)} where Ẑ_{(p)} = ∏_{l≠p} Z_l") and a₀ is a unit.
**Homeomorphism onto its image.** Ẑ_{(p)} is compact; X•(C) is metrizable (p. 40) hence Hausdorff; a continuous injection from a compact space to a Hausdorff space is a homeomorphism onto its (compact, hence closed) image.
**Location.** β(b)^{-1}(0) = 𝔭_x for every b (χ(r̄)^b is a root of unity, never 0), so pr_X(β(b)) = x. ∎

### 5.2 (R2) The closure of the Frobenius returns, in one chart, at the fixed prime

The return identity of Theorem A is [F_n P₀, u] = [P₀, nu] ∈ γ for n ∈ N ([x-03] p. 38 suspension relation), and F_n(P_{a₀}) = P_{a₀ n}. So S̃ := {P_{a₀ n} : n ∈ N} = β(N).

**Lemma O.6.** cl_{X•(C)}(S̃) = β(Ẑ_{(p)}) = K.
*Proof.* N is dense in Ẑ_{(p)} = lim_{(M,p)=1} Z/M: the positive integers surject onto every Z/M with (M,p)=1 (CRT), so β(N) meets every basic open set of Ẑ_{(p)}. β is a homeomorphism onto the closed set K (Lemma O.5), so cl(β(N)) = β(cl_{Ẑ_{(p)}} N) = β(Ẑ_{(p)}) = K. ∎

This is the sub-claim (A1-mech) makes, and **at this level the note is right**: every subnet limit of {F_n(P₀)} is P_{a₀b} for some b ∈ Ẑ_{(p)}, by compactness and pointwise evaluation. Note that K lies entirely over x: **no limit of the Frobenius returns escapes to another prime or to characteristic 0, already upstairs.**

### 5.3 (R3) TASK ITEM (3): what exactly "leaves the space", and by what

Which P_{a₀b} are points of X•(C)_{Etors}, hence candidates to lie in the E-locus? Since χ is injective, ker(χ^{a₀b}) = ker(( )^{a₀b}) on μ^{(p)}, and a₀ is a unit, so

  ker(χ^{a₀ b}) = ⨁_{ℓ≠p} μ_{ℓ^{v_ℓ(b_ℓ)}},  v_ℓ(b_ℓ) ∈ {0,1,2,…,∞}, with v_ℓ(0) := ∞.

Condition (Tors) ([x-03] p. 27, verbatim: "(Tors) the group ker(χ)_{tors} = ker(χ|_{μ(κ)}) is finite and |(ker χ)_{tors}| ∈ N₀") therefore holds **iff**

  (⋆) v_ℓ(b_ℓ) < ∞ for every ℓ ≠ p **and** v_ℓ(b_ℓ) = 0 for all but finitely many ℓ,

equivalently **b ∈ N′ · Ẑ^×_{(p)}**, where N′ ⊂ N is the set of positive integers prime to p (for N₀ = N; in general N₀′·Ẑ^×_{(p)}).

**This is finding F2.** The note's criterion is only the first half of (⋆): "limits with some component of b equal to 0 kill a μ_{ℓ^∞} and violate (Tors), so they leave the space". That sentence is *true* but *not exhaustive*, and the shortfall is not cosmetic:

- **Counterexample to the note's criterion as a criterion.** Take b = (ℓ)_{ℓ≠p} ∈ Ẑ_{(p)}, i.e. b_ℓ = ℓ for every ℓ ≠ p. Every component is nonzero, so the note's test declares nothing wrong; but v_ℓ(b_ℓ) = 1 for every ℓ, so ker(χ^{a₀b}) = ⨁_{ℓ≠p} μ_ℓ is **infinite** and (Tors) fails. The point P_{a₀b} is a genuine limit of Frobenius returns (Lemma O.6) and is **not** a packet point. Concretely it is the limit of P_{a₀ n_k} along n_k = ∏_{ℓ ≤ k, ℓ≠p} ℓ · (unit correction), which is a legitimate subsequence of the returns.
- **Consequence if the note's criterion were the whole criterion.** Then the surviving limit set would be β({b : all b_ℓ ≠ 0}) ⊋ β(N′Ẑ^×_{(p)}) = the packet exponents, and the claimed equality cl(γ) ∩ (char-p part) = Γ^E_p would be **false**. So the incompleteness is load-bearing for the conclusion, not for its presentation. That is why I rate it MAJOR and not MINOR.
- **The conclusion nonetheless survives**, because the true criterion (⋆) is *more* restrictive than the note's, and the b's it additionally excludes are excluded for the same reason ((Tors)).

**And by what are they excluded?** By **(Tors)**, hence by membership in the space, not by the topology and not by the class E specifically. Three sharpenings the note does not make:

1. Every admissible E satisfies E ⊆ E_tors by Definition 4.1 ("Moreover the characters in E should satisfy (Tors)", p. 27), so the exclusion is uniform in E: no admissible system contains the bad limits. What varies with E is only which of the *good* b's are in E.
2. The exclusion is **not** topological. In the un-cut space X̌₀(C) (no (Tors) imposed) the bad limits are present, and the equality genuinely fails: take n_k = ∏_{ℓ≤k, ℓ≠p} ℓ^k → 0 in Ẑ_{(p)}; then P_{a₀ n_k} → P_0 = (x, **1**), the trivial character, whose Q^{>0}-isotropy is all of Q^{>0} and which is not in any packet. So [P_0, u] ∈ cl(γ) there. **The hypothesis E ⊆ E_tors is necessary for Corollary O.4**, a scope point the note does not record.
3. Because the closure is taken *in* 𝕏₀, which is built on X̌₀(C)_E, the bad limits are simply not in the ambient space; closure in a subspace is the trace of the ambient closure (cl_Y(A) = cl_X(A) ∩ Y for A ⊆ Y ⊆ X). No "escape" argument is needed — the phrase "they leave the space" is right in spirit, but the *space* has to be named, and the note never says in which space it is taking the closure at this point. That ambiguity is the seed of F1.

### 5.4 (R4) Descent through G and (R5) through the charts, then to 𝕏₀

Two more reductions, both missing from the note.

**(R4) Galois.** π : X•(C) → X•₀(C) is continuous and **open** (p. 43), G is compact and acts continuously (Prop. 7.5, p. 44: "the right-action map X•(C) × G → X•(C) is continuous"; G = Aut_{K₀}(K) is a profinite group, hence compact). For a compact group acting continuously, cl(A·G) = cl(A)·G and π(cl A) = cl(π A) for G-stable closures; concretely, since π is open, Lemma O.0 gives π^{-1}(cl π(S̃)) = cl(π^{-1}π(S̃)) = cl(S̃·G) = cl(S̃)·G = K·G, so cl_{X•₀(C)}(π S̃) = π(K). The Galois action on the exponents is through the decomposition group, (34) p. 32: "N x₀^Ẑ = Gal(κ(x)/κ(x₀)) ↪ Aut(κ(x)^×) = Ẑ^×_{(p)}", i.e. through p^Ẑ for x₀ = (p) of degree 1 — so π(K) = β(Ẑ_{(p)})/p^Ẑ.

**(R5) Charts.** By (T1) of §3.3, closures in the colimit are computed chart-locally on the clopen charts U_ν = F_ν^{-1}(X•₀(C)_E), and F_ν : U_ν → X•₀(C)_E is a homeomorphism (Prop. 7.4 b) + p. 47). The orbit O(P₀) = {F_r P₀ : r ∈ Q₀^{>0}} meets U_ν exactly in {F_q P₀ : D(q) | ν}, where D(q) denotes the prime-to-p part of the denominator of q in lowest terms. (Reason: F_q P₀ ∈ U_ν iff F_{νq}P₀ ∈ X•₀(C)_E; by (51) on p. 42, F_{1/m}(F_{m′}P₀) ∈ X•₀(C) iff χ^{a m′} is trivial on μ_m(K); χ is injective on μ^{(p)} and trivial on μ_{p^∞} — for ζ ∈ μ_{p^∞} one has ζ ≡ 1 mod 𝔭_x — so this holds iff the prime-to-p part of m is 1. The isotropy relation F_p P₀ = P₀ (Thm 5.2, p. 34: "For any point P₀ ∈ C^E_{x₀} the isotropy group of P₀ is (Q₀^{>0})_{P₀} = N x₀^Z") is what makes the p-part of the denominator free.) Transporting by F_ν, each chart-closure is again the closure of a set of the form {P_{a c} : c ∈ N·p^Z} in X•₀(C)_E, and since p is a **unit** of Ẑ_{(p)}, N·p^Z has the same closure Ẑ_{(p)} there as N does; so Lemma O.6 + §5.3 + (R4) apply verbatim in every chart. Hence

  cl_{X̌₀(C)_E}(O(P₀)) = ⋃_{ν∈N₀} F_ν^{-1}( π(K) ∩ X•₀(C)_E ) = ⋃_{ν∈N₀} F_ν^{-1}( pr₀^{-1}(x₀) ∩ X•₀(C)_E ) = C^E_{x₀},

the middle equality being §5.3: the (Tors)-admissible exponents b ∈ N′Ẑ^×_{(p)} give, via (35)–(36) on p. 32, exactly the points of pr₀^{-1}(x₀) at x, and every point of pr₀^{-1}(x₀) arises this way ("Explicitely this gives the N₀-equivariant bijection S/N x₀^Ẑ ≅ pr₀^{-1}(x₀)", p. 32).

**Descent to the suspension.** By (★) of §3.5, cl_{𝕏₀}(γ) = q(cl(O(P₀)) × R^{>0}) = q(C^E_{x₀} × R^{>0}) = Γ^E_p. **Both inclusions at once, independently of Proposition O.1.** ∎

### 5.5 TASK ITEM (5): what is proved — chartwise or globally?

**Globally, in 𝕏₀, and the chart question dissolves.** The equality cl_{𝕏₀}(γ) = Γ^E_p is a statement about one closure in one space. The second proof does pass through charts, and there the statement it verifies chart-by-chart is the upstairs one: for every ν, cl(O(P₀)) ∩ U_ν = C^E_{x₀} ∩ U_ν. Because the charts are clopen and the colimit topology restricts to pointwise convergence on each (§3.3, (T1)–(T2)), there is no discrepancy between "equality in every chart" and "equality in the colimit" to worry about — the note's Q-c as posed ("whether the equality holds verbatim in every chart") presupposes a discrepancy that Prop. 7.4 a) rules out. The first proof (§4) never enters a chart at all.

**And there is no residual "char-p part" content.** The part of 𝕏₀ over (p) *is* Γ^E_p (Prop. O.1 (iii)); so the hedged equation is the unhedged one intersected with its own right-hand side. See F3.

---

## 6. FINDINGS, with exact replacement text

Locations are given as (file, section, quoted phrase). Severity per the program rubric: FATAL = a stated theorem is false or its proof has an unfillable gap; MAJOR = gap fillable, but the note must change; MINOR = wording, citation, typo.

### F1 — MAJOR. The parenthetical's instrument computes a different closure from the one claimed.

**Location.** `probe-9.3-b.md` §5, Corollary A.1, "every limit of {F_n(P₀)}_n along any subnet is P₀^b … by compactness of Ẑ_{(p)} and the same pointwise evaluation".

**The defect.** What is computed is cl_{X•(C)}{F_n P₀ : n ∈ N} — the closure of a **sequence**, in **one chart**, of the **upstairs** space, at a **fixed prime**. What is asserted is a statement about cl_{𝕏₀}(γ), the closure of a **circle** in the **suspension** of the **Galois quotient** of the **colimit**. Four distinct reductions separate them, and none is present: (R1)/(R2) the sequence vs. the full Q₀^{>0}-orbit — by (★) the relevant upstairs set is O(P₀) = {F_r P₀ : r ∈ Q₀^{>0}}, not {F_n P₀ : n ∈ N}; (R4) the Galois quotient π, which is open, so closures do descend, but this must be said; (R5) the colimit, where closure is chart-local and the orbit visits infinitely many charts; and the suspension quotient q, which is **not proper** and whose action is **not properly discontinuous** ([x-03] p. 49, verbatim) — so q does *not* reflect convergence and "compute upstairs, push down" is not available as a general principle. What *is* available is Lemma O.0 (q is open), and that has to be invoked.

**Fill attempt: succeeds.** §5 carries the instrument through all five reductions and reaches the conclusion. **Break attempt: fails** — see §7.1; the instrument is repairable, not wrong.

**Replacement text** (replaces the whole parenthetical of Corollary A.1):

> (The converse inclusion is Proposition A.1″ below. **Proposition A.1″ (packets are closed).** For every arithmetic scheme X₀, every admissible E and every point x₀ of X₀ with finite residue field, Γ^E_{x₀} is a closed flow-invariant subset of 𝕏₀ = X̌₀(C)_E ×_{Q₀^{>0}} R^{>0} with its quotient topology. *Proof.* pr_{X₀} : X̌₀(C)_E → X₀ is continuous into the Zariski topology ([x-03] Lemma 7.1 p. 40; p. 42–43 for the general and colimit cases; p. 47 for the E-version) and Q₀^{>0}-invariant, Q₀^{>0} acting trivially on X₀ (p. 27, after (31)). Hence (P₀,u) ↦ pr_{X₀}(P₀) is continuous on X̌₀(C)_E × R^{>0} and constant on Q₀^{>0}-orbits, so it descends through the quotient map to a continuous Π : 𝕏₀ → X₀ with Π∘φ^t = Π. By [x-03] p. 31, C_{x₀} = pr_{X₀}^{-1}(x₀) in X̌₀(C)_{Etors}, and since every admissible E satisfies E ⊆ E_tors (Def. 4.1), C^E_{x₀} = pr_{X₀}^{-1}(x₀) ∩ X̌₀(C)_E; this set is Q₀^{>0}-stable, so Γ^E_{x₀} = q(C^E_{x₀} × R^{>0}) = Π^{-1}(x₀). A point with finite residue field is a closed point (A/𝔭 is a finite domain, hence a field), so Γ^E_{x₀} is closed. ∎ Consequently cl_{𝕏₀}(γ) ⊆ Γ^E_p for every periodic orbit γ ⊆ Γ^E_p, and with Theorem A, **cl_{𝕏₀}(γ) = Γ^E_p exactly**, with no intersection taken: the closure meets no other packet and no point of the generic stratum.)

*Editorial note on numbering.* I write "Proposition A.1″" to keep my proposed insertion distinct from anything already inserted into the note by an earlier pass. If the adjudicator has already placed a Proposition A.1′ carrying this statement, **it is the same statement and only one number should survive** — do not create two.

### F2 — MAJOR. The exclusion criterion is incomplete, and completing it is necessary for the conclusion.

**Location.** `probe-9.3-b.md` §5, Corollary A.1, "limits with some component of b equal to 0 kill a μ_{ℓ^∞} and violate (Tors), so they leave the space".

**The defect.** (Tors) fails for P_{a₀b} exactly when ⨁_{ℓ≠p} μ_{ℓ^{v_ℓ(b_ℓ)}} is infinite, i.e. when **either** some v_ℓ(b_ℓ) = ∞ (the note's case, b_ℓ = 0) **or** v_ℓ(b_ℓ) > 0 for infinitely many ℓ. The note names only the first disjunct. **Counterexample to the criterion:** b = (ℓ)_{ℓ≠p} has all components nonzero, passes the note's test, and violates (Tors) with infinite kernel ⨁_{ℓ≠p} μ_ℓ. Were the note's criterion exhaustive, the limit set would strictly exceed the packet and **the claimed equality would be false**. The correct criterion is b ∈ N₀′·Ẑ^×_{(p)} (N₀′ = the elements of N₀ prime to p).

**Fill attempt: succeeds** (§5.3). **Break attempt: fails** — the extra bad b's are excluded by the same condition, so the conclusion is unharmed; only the reason is wrong.

**Replacement text** (for that clause, if the parenthetical is kept in any form):

> "the limit P₀^b satisfies (Tors) if and only if ker(( )^b) = ⨁_{ℓ≠p} μ_{ℓ^{v_ℓ(b_ℓ)}} is finite, i.e. if and only if b ∈ N₀′·Ẑ^×_{(p)} — every component nonzero **and** all but finitely many components units. Limits failing either half (e.g. b with a zero component, killing a μ_{ℓ^∞}; or b = (ℓ)_{ℓ≠p}, with every component nonzero but no component a unit) violate (Tors) and are not points of X̌₀(C)_E for any admissible E, since Definition 4.1 imposes (Tors) on every admissible class."

### F3 — MAJOR. The stated conclusion is logically equivalent to Theorem A and carries no converse content; Corollary A.1's headline is therefore unproved in the note.

**Location.** `probe-9.3-b.md` §5, Corollary A.1, "one gets cl(γ) ∩ (char-p part) = Γ^E_p exactly", read against the headline "Γ^E_p is the orbit closure of each of its points and is the smallest closed invariant set containing any one of its orbits".

**The defect.** "char-p part" is not defined in the note. Both available readings make the displayed equation vacuous as a converse:
- Read as *the part of 𝕏₀ over the point (p)*: that part **is** Γ^E_p (Prop. O.1 (iii)), so the equation reduces to cl(γ) ⊇ Γ^E_p, i.e. Theorem A.
- Read as *the union of all positive-characteristic strata* (the suspension of ⋃_p X̌₀(C)_{p,E}, in the notation of [x-03] p. 33): the equation then asserts additionally that cl(γ) meets no *other* prime's packet — which is true, but is nowhere argued, and is exactly a statement about the whole colimit that the fixed-prime computation cannot see.

Either way the note does not establish cl(γ) ⊆ Γ^E_p, and therefore does not establish that Γ^E_p is **the** orbit closure, or that it is **the smallest closed invariant set** containing an orbit, or that it is a **minimal set**. Those are the statements the program banked (adjudication §4 item 1). The gap is fillable (§4, §5) but the note must change: MAJOR.

*I record a disagreement with the leaked adjudication block, which rates the "∩ (char-p part)" hedge MINOR on the ground that "the claim as hedged is true and merely weaker than the truth".* Truth is not the test; adequacy to the stated corollary is. A corollary whose proof establishes only its converse-free half has a MAJOR defect even when every sentence in it is true. I hold F3 at MAJOR. (I do not dispute the adjudicator's right to merge F3 into F1 as one defect with two faces — derivation-side and conclusion-side — and if merged, one MAJOR is the correct count. I do dispute demoting it.)

**Replacement text** (for Corollary A.1's headline sentence, making the dependency explicit):

> "**Corollary A.1 (packets are minimal sets; the 'invariant tori' made precise).** Γ^E_p is nonempty, closed (Proposition A.1″) and flow-invariant, and every one of its orbits is dense in it (Theorem A). Hence Γ^E_p is a **minimal set** of the flow φ^t on 𝕏₀: it is the orbit closure of each of its points, and the smallest closed invariant set containing any one of its orbits. Both halves are needed — Theorem A alone gives only that every closed invariant set meeting Γ^E_p contains it, which is what Corollary A.3 and Corollary B consume."

### F4 — MINOR. Wrong cross-reference.

**Location.** "(With Step 5's converse inclusion — …". Step 5 of Theorem A is the sweep establishing ⊇; it contains no converse. **Replacement:** "(For the converse inclusion see Proposition A.1″ — …".

### F5 — MINOR. The topology on the suspension is load-bearing here and is cited as "implicit".

**Location.** `probe-9.3-b.md` §3.1, "the suspension X₀ carries the quotient topology (implicit throughout §§8, 10, e.g. 'topological closure' in §8, the sheaf-theoretic §10)".

**The defect.** The reading is correct, but for the converse it is *the* hypothesis: Π's continuity in Prop. O.1 is exactly the universal property of the quotient topology, and a strictly coarser topology on 𝕏₀ would void it. I confirm by grep that [x-03] never writes "quotient topology" for the suspension. **Replacement:**

> "the suspension carries the quotient topology of X̌₀(C)_E × R^{>0}. [x-03] §6 p. 38 defines it as a quotient without naming a topology; the warrants are (i) [r3s-08] p. 14 verbatim for the identical construction, 'We equip X_K twith he quotient topology of the product X̌_K(C) × R₊'; (ii) [x-03] p. 61, where continuity of π : X_η ↠ Y is deduced from continuity of its lift — valid only for the quotient topology; (iii) [x-03] §10 p. 63, R_X = (π_∗R_X̃)^Q ⊂ (π_∗C⁰_X̃)^Q = C⁰_X; (iv) [x-06] p. 11. The quotient map q is open (Q₀^{>0} acts by homeomorphisms, Prop. 7.4 b) but not proper, and the action is not properly discontinuous ([x-03] p. 49), so q does not reflect convergence; closures nevertheless descend through the open-map identity q^{-1}(cl A) = cl(q^{-1}A)."

### F6 — MINOR. The necessity of E ⊆ E_tors is not recorded, and the equality is false without it.

**Location.** Corollary A.1 as a whole. **The point.** In the un-cut suspension X̌₀(C) ×_{Q₀^{>0}} R^{>0} the equality fails: with n_k = ∏_{ℓ≤k, ℓ≠p} ℓ^k → 0 in Ẑ_{(p)} one gets [P₀, n_k u] = [F_{n_k}P₀, u] → [(x, **1**), u], a point whose Q₀^{>0}-isotropy is all of Q₀^{>0} and which lies in no packet. **Replacement:** append to Corollary A.1: "The hypothesis that E be admissible — specifically E ⊆ E_tors, imposed by Definition 4.1 — is necessary and not merely convenient: in the un-cut suspension the closure of γ additionally contains [(x, 1), u], and the equality fails."

### F7 — MINOR. Two traps in the neighbourhood of this item should be named where a reader will meet them.

**Location.** `probe-9.3-b.md` §3.2 (quoting Deninger's "compact packets") and §3.3 (the Morishita caution).

**(a) Compactness does not give closedness here.** [x-03] p. 2 ("the closed points x₀ of X₀ correspond bijectively to compact packets Γ_{x₀}") and [x-06] p. 12 ("The compact subsets Γ_{x₀} ⊂ X₀ … are pairwise disjoint") are asserted without proof, and — crucially — **the standard inference compact ⟹ closed is unavailable in 𝕏₀**, which is non-Hausdorff along the packets (Cor. A.2, adjudication §3). Anyone tempted to derive the converse inclusion from Deninger's compactness sentence is making an invalid step. Prop. O.1 is needed, and it is independent of compactness. **Replacement (add to §3.2):** "Deninger asserts compactness of Γ_{x₀} without proof ([x-03] p. 2; [x-06] p. 12). Note that compactness does **not** yield closedness in 𝕏₀, which is non-Hausdorff along the packets (Cor. A.2); closedness must be proved separately (Proposition A.1″), and compactness likewise (Corollary A.5)."

**(b) The Morishita caution is right but can now be stated exactly, and it moves.** Γ_p ⊂ 𝕏₀ *is* closed (Prop. O.1) and, for E ⊇ E_f, compact (Cor. A.5 below) — so there is nothing wrong with treating it as a compact subset. What fails is (i) Hausdorffness of Γ_p in its subspace topology, which refutes [r3s-08] Thm 2.2.9(1)'s "homeomorphism" onto the compact Hausdorff mapping-torus model Ẑ^×_{(p)}/p^Ẑ ×_{p^Z} R₊ (p. 17), and (ii) closedness of the individual orbits, which refutes reading Thm 2.2.9(2)'s "decomposition into connected closed R₊-orbits" (p. 18) in that topology, every orbit being dense in Γ_p by Theorem A. **Replacement for the ledger's W11 row:** "[r3s-08] Thms 2.2.8/2.2.9 give model bijections, not subspace-topology statements. In 𝕏₀ the packet Γ_p is closed (referee O, Prop. O.1) and, for E ⊇ E_f, compact (Cor. A.5), but non-Hausdorff (adjudication §3); so 2.2.9(1)'s homeomorphism onto a compact Hausdorff model is false in the subspace topology, and 2.2.9(2)'s 'closed R₊-orbits' is false there too. Harmless to the class-field-theoretic content; never cite for topology. Conversely, [r3s-08] p. 14's assertion that pr_K : X_K → Spec O_K is continuous **is** correct and is the shortest published route to Prop. O.1."

---

## 7. Attempts to BREAK the result (all four fail; the fourth produces a new theorem)

A referee pass that only fills gaps has not tested anything. Here is what I tried.

### 7.1 Break the instrument: make the note's computation give a strictly larger closure

*Attempt.* Find a net in γ whose 𝕏₀-limit is not of the form [P_{a₀b}, u] — exploiting that q is not proper, so a convergent net downstairs need not lift.
*Outcome: fails, and provably so.* Lemma O.0 converts the question into an upstairs one without lifting individual nets: cl_{𝕏₀}(γ) = q(cl(O(P₀)) × R^{>0}) exactly, because q is open. The properness failure costs nothing at the level of closures. (It costs a great deal at the level of *limits of a given net*, which is why Cor. A.2's two-limit phenomenon is possible; but "which points are in the closure" is insensitive to it.)

### 7.2 Break the topology: deny that 𝕏₀ carries the quotient topology

*Attempt.* [x-03] never writes "quotient topology" for the suspension (verified by grep, §3.4). If 𝕏₀ carried some strictly coarser topology, Π's continuity would fail and Prop. O.1 would collapse.
*Outcome: fails.* Three independent warrants (§3.4): Morishita's explicit sentence for the identical construction ([r3s-08] p. 14); Deninger's own inference of continuity of π : X_η ↠ Y from continuity of its lift ([x-03] p. 61), which is valid only under the quotient topology; and the §10 sheaf identity C⁰_X = (π_∗C⁰_X̃)^Q (p. 63). *Residual honesty:* this is the one hypothesis of Prop. O.1 that rests on a reading rather than on a quoted sentence of [x-03]. It is recorded as F5 and in the scope note §10.

### 7.3 Break the fibre identification: find a point of 𝕏₀ over (p) that is not in Γ^E_p

*Attempt.* Deninger builds C_{x₀} as a union ⋃_ν F_ν^{-1} pr₀^{-1}(x₀) rather than as a fibre in the colimit; if the union were smaller than the fibre, Π^{-1}((p)) would strictly contain Γ^E_p and Prop. O.1 would prove closedness of the wrong set. Also, Thm 5.5 b) (p. 37) warns that over positive-characteristic points there can be points with nontrivial isotropy that one does *not* want.
*Outcome: fails.* The Sub-lemma of §4.2 shows the union *is* the fibre, using only the triviality of the Q₀^{>0}-action on the base (p. 27) and the definition of the colimit. And Thm 5.5 b) is about points x₀ of positive characteristic whose residue field is **not finite** — for those Deninger notes the unwanted isotropy; but for x₀ with finite residue field Thm 5.2 (p. 34) gives isotropy exactly N x₀^Z, and those are the only x₀ in play. Note also that Prop. O.1 does *not* care: it proves that Π^{-1}(x₀) is closed for **every** point x₀ of X₀ that happens to be closed, whether or not the fibre is a packet.

### 7.4 Audit the result against the rest of the program: does closedness contradict Cor. A.2 or Theorem A?

*Attempt.* Corollary O.4 says a compact circle γ is dense in a strictly larger closed set Γ^E_p, and that **uncountably many** pairwise disjoint circles are each dense in the same set. In any Hausdorff space that is absurd (a compact orbit would be closed, hence equal to its closure). So either the space is very strange, or something above is wrong.
*Outcome: fails to break; the space really is that strange, and the audit yields a sharper statement than either the note or the adjudication records.*

> **Corollary O.7 (new; 𝕏₀ is not even T1 along its packets, and every point of a packet is dense in it).** Let X₀ = Spec Z, E admissible, p a prime, z ∈ Γ^E_p. Then cl_{𝕏₀}({z}) = Γ^E_p. In particular no point of a packet is a closed subset of 𝕏₀, and Γ^E_p is a minimal set in the strongest sense (every subset of it is dense).
>
> *Proof.* ⊆ is Prop. O.1. For ⊇, write z = [P₀, w] with P₀ = π(x, χ^{a}), a ∈ Ẑ^×_{(p)}. Since q is a quotient map, it suffices to produce limit points of the fibre q^{-1}(z) = {(F_q P₀, q^{-1}w) : q ∈ Q^{>0}} outside itself and identify their images. Fix ν ∈ N and an **irrational** s > 0. Choose M_k = k! and j_k with p^{j_k} > k·M_k, then an integer m_k ≡ 1 (mod M_k) with |m_k/p^{j_k} − s| ≤ M_k/p^{j_k} < 1/k (any interval of length ≥ M_k contains a residue class rep). Put q_k := m_k/(ν p^{j_k}) ∈ Q^{>0}, so q_k → s/ν in R. The prime-to-p part of the denominator of q_k divides ν, hence F_{q_k}P₀ lies in the chart U_ν = F_ν^{-1}(X•₀(C)_E) (using ( )^p invertible on the characteristic-p locus, [x-03] p. 46: "the Frobenius endomorphisms F_p of X•(C) and X•₀(C) restrict to homeomorphisms F_p of X•(C)_p and X•₀(C)_p"). Transport by the homeomorphism F_ν : U_ν → X•₀(C)_E: F_ν(F_{q_k}P₀) = F_{m_k p^{−j_k}}P₀ = π(x, χ^{a m_k p^{−j_k}}). Now m_k → 1 in Ẑ_{(p)} (as m_k ≡ 1 mod k!), and after passing to a subsequence with j_k → t in the compact group Ẑ we get p^{−j_k} → p^{−t} ∈ p^Ẑ, so a m_k p^{−j_k} → a p^{−t}. Since p^Ẑ = Gal(κ(x)/F_p) sits inside Ẑ^×_{(p)} = Aut(κ(x)^×) by (34) (p. 32) and G_x surjects onto it (p. 32, "It surjects onto Gal(κ(x)/κ(x₀))"), π(x, χ^{a p^{−t}}) = π(x, χ^a) = P₀. Hence F_ν(F_{q_k}P₀) → P₀ in X•₀(C)_E, i.e. F_{q_k}P₀ → F_{1/ν}P₀ in X̌₀(C)_E; and q_k^{−1}w → (ν/s)w ∈ R^{>0}. So (F_{1/ν}P₀, (ν/s)w) ∈ cl(q^{-1}(z)), whence q(F_{1/ν}P₀, (ν/s)w) = [P₀, w/s] ∈ cl({z}). As s ranges over the positive irrationals, {w/s} is dense in R^{>0}, so cl({z}) contains a dense subset of the circle γ = {[P₀, v] : v > 0}, hence contains cl(γ) = Γ^E_p by Theorem A. ∎
>
> *Why this does not contradict anything.* The Q^{>0}-orbit of (P₀, w) fails to be closed for a transparent reason: in the packet the relevant completion of the exponent group is Ẑ_{(p)}, from which the p-component has been **removed**, so p is a unit there and the sequence (p^{j}, p^{−j}) accumulates — Q^{>0} is not discrete in Ẑ^×_{(p)} × R^{>0}. Contrast [x-03] p. 64, verbatim: "By [LR00, Lemma 3.1], the orbits of the Q^{>0}-action on Q^{>0}Ẑ^× × R^{>0} are closed. The same argument works for Q₀^{>0} instead of Q^{>0} and it follows that the points of Y are closed, i.e. Y is a T₁-space." There the full Ẑ^× is present and Q^{>0} *is* discrete. **So the generic quotient is T₁ and the packets are not** — a clean structural dichotomy inside the same space.
>
> *Status.* Corollary O.7 is **not needed for the item** and is not part of what I certify below. It is reported because it is the audit that convinced me Corollary O.4 is consistent, because it strengthens "minimal set" to "every point dense" (which makes minimality immediate: any nonempty closed invariant S ⊆ Γ^E_p contains a point z, hence contains cl{z} = Γ^E_p), and because it is a fifth independent negative structural datum about 𝕏₀ (after W6, W7, W9, W12). **It owes its own referee pass before it is used or circulated.**

---

## 8. Supporting results proved this session (compactness, nowhere density) and the traps they close

These are not needed for the converse inclusion, but two of them were quoted in the note as source facts and deserve proofs, and one of them is a trap.

> **Corollary O.8 (compactness of the packets; "Corollary A.5" in the note's numbering).** Let X₀ = Spec Z, C = ℂ, and E ⊇ E_f, so that Γ^E_p = Γ_p (Thm 5.2, p. 34: "If e.g. E ⊃ E_f then C^E_{x₀} = C_{x₀}"; §6 p. 38: "If e.g. E_f ⊂ E then Γ^E_{x₀} = Γ_{x₀}"). Then Γ_p is compact.
> *Proof.* By (38) (p. 32) every point of C_{x₀} is [a, r] with a ∈ Ẑ^×_{(p)}/p^Ẑ and r ∈ Q^{>0}, i.e. is F_r(π(x, χ^a)) for a **unit** a; so every point of Γ_p is [F_r π(x,χ^a), u] = [π(x,χ^a), ru]. Since F_p π(x,χ^a) = π(x, χ^{ap}) = π(x,χ^a) (Frobenius lies in the Galois image, (34)), we have [π(x,χ^a), pv] = [π(x,χ^a), v], so the R-parameter may be taken in the compact interval [1, p]. Hence Γ_p = q( (π∘β)(Ẑ^×_{(p)}) × [1,p] ), a continuous image of a compact set (β is continuous by Lemma O.5; Ẑ^×_{(p)} = ∏_{ℓ≠p} Z_ℓ^× is compact, each Z_ℓ^× being clopen in Z_ℓ). ∎
> This **proves** the compactness Deninger asserts without proof at [x-03] p. 2 ("the closed points x₀ of X₀ correspond bijectively to compact packets Γ_{x₀}") and [x-06] p. 12 ("The compact subsets Γ_{x₀} ⊂ X₀ … are pairwise disjoint").

> **Corollary O.9 (nowhere density).** For X₀ = Spec Z, C = ℂ, E ⊇ E_f, each Γ_p is closed with empty interior.
> *Proof.* Γ_p is closed (Prop. O.1). Its complement contains Π^{-1}(η₀), the generic stratum X_{0η₀}, which is dense in 𝕏₀ ([x-03] Cor. 9.7 proof, p. 62, verbatim: "By Theorem 9.6 the spaces X_η and X_{0η₀} are connected. By Theorem 9.2 they are dense in X resp. X₀"). A closed set whose complement contains a dense set has empty interior. ∎
> This is what reconciles closedness of the packets with connectedness of 𝕏₀ (Cor. 9.7): the packets are closed, pairwise disjoint, uncountably many, and *nowhere dense*, so removing them does not disconnect anything.

> **The trap, stated plainly.** Do **not** derive Prop. O.1 from compactness. In a Hausdorff space compact ⟹ closed; 𝕏₀ is not Hausdorff along the packets (adjudication §3, probe B Cor. A.2), and by Corollary O.7 it is not even T₁ there. Deninger's "compact packets" sentence is therefore *not* a source for the converse inclusion, and any future write-up that leans on it has an unfillable step. Corollary O.8's proof is independent of Prop. O.1, and Prop. O.1's proof is independent of Corollary O.8; neither implies the other in this space.

---

## 9. Novelty and priority (standing order 7), stated against my own repair

I state this against my own result, because standing order 7 exists precisely to stop a referee from flattering the repair he wrote.

1. **Proposition O.1 is not a new theorem; it is one step from a printed sentence.** [r3s-08] p. 14, verbatim: "let pr_K : X_K → X_K be the composition of the projection X_K → X̌_K(C) with p̌r_K. These projections p̌ṙ_K, p̌r_K and pr_K are continuous." Here the first X_K is the suspension and the second is Spec(O_K): Morishita **asserts in print the continuity of the very map Π** that Prop. O.1 uses, and he does so immediately after equipping the suspension with the quotient topology. Given that sentence, "the packet is a fibre of a continuous map to a scheme, over a closed point, hence closed" is a one-line inference. Anyone claiming Prop. O.1 as new should be told this first. (Morishita's sentence has a defect of its own — there is no "projection X_K → X̌_K(C)" from the suspension, the map being only defined after descent — so the assertion is correct but sloppily justified; that is another reason to give the two-line proof rather than cite it.)
2. **Nobody on disk draws the conclusion.** [x-03] states the packets are *compact* (p. 2) and *fibred over Ẑ^×_{(p)}/p^Ẑ* (pp. 33, 38) and *pairwise disjoint* ([x-06] p. 12); it never says a packet is closed in 𝕏₀, and its structural results for packets are stated as **bijections**, not homeomorphisms ("The Q^{>0}-bijection (39) induces an R^{>0}-bijection", p. 38). [r3s-08] Thm 2.2.9 upgrades those to "homeomorphism" and to "connected closed R₊-orbits" (pp. 17–18), both of which are **false in the subspace topology of 𝕏₀** given Theorem A and Cor. A.2 — so the one place in the literature that appears to assert the relevant topology asserts something incorrect about it.
3. **What is actually new here is the equality and its consequences**, and the equality's substance is Theorem A (banked, three derivations), not the converse. Corollary O.7 (non-T₁; every point of a packet dense in it) appears to be new, and I do not find it in the sources I read.
4. **External sweep, honestly scoped.** Two server-side web searches were run this session (2026-09-02): "Deninger dynamical system arithmetic scheme packet periodic orbits closed subset orbit closure suspension" and "'Deninger' foliated dynamical system packet Gamma_p 'minimal set' every periodic orbit dense non-Hausdorff suspension arithmetic". Both returned only the primary sources already on disk ([x-03] arXiv and ScienceDirect, [x-06], [r3s-08]), Deninger's survey slides, [r3s-19] (arXiv:2410.20758), and unrelated generic material on minimal dynamical systems. **No result on packet closedness, packet minimality, or T₁/Hausdorff failure was found in the open literature; no deeper sweep (MathSciNet, zbMATH, citation-graph of [x-03]) was performed, and none is claimed.** This is a two-query check, not a priority search.

---

## 10. What is now established at referee grade, and its precise scope

**Established.** For every arithmetic scheme X₀ in the sense of [x-03] §7 (integral normal, countable function field), every algebraically closed valued C admissible for the construction, every admissible class E in the sense of Definition 4.1, and every point x₀ of X₀ with finite residue field, the packet Γ^E_{x₀} is a **closed, flow-invariant** subset of the suspension 𝕏₀ = X̌₀(C)_E ×_{Q₀^{>0}} R^{>0} carrying the quotient topology — it is the fibre over the closed point x₀ of a continuous flow-invariant map Π : 𝕏₀ → X₀ descended from pr_{X₀} ([x-03] pp. 27, 31, 34, 38, 40, 42–43, 47). Consequently the closure of any subset of a packet stays inside that packet, and — for **X₀ = Spec Z, N₀ = N**, where Theorem A is banked — **cl_{𝕏₀}(γ) = Γ^E_p exactly**, for every admissible E and every periodic orbit γ ⊆ Γ^E_p, with no "char-p part" hedge, no chart caveat, and no residual proposition-grade content. Hence Corollary A.1's headline is true: each packet is a **minimal set** of the flow, the orbit closure of each of its points, and the smallest closed invariant set containing any one of its orbits. This is proved twice and independently in §4 and §5, the second time by carrying the note's own instrument through the five reductions it was missing. Adjudication §5's **Q-c is settled YES**, and adjudication §4 item 1's phrase "packets are minimal sets" — which silently used this converse — is now backed.

**Scope limits, stated honestly.**
(i) **Nothing here touches the mapping face of S4.** The result is a statement about closed subsets of 𝕏₀. A compact-but-not-closed invariant subspace, or the image of a continuous flow-equivariant map from a compact lamination, is entirely unconstrained by it — indeed Cor. A.2 and Cor. O.7 make the gap between "compact" and "closed" in 𝕏₀ enormous. **Q\* of the Session-8 adjudication (§5) is unchanged in every respect, and the C3 kill-criterion is unaffected.** If anything, Cor. O.7 widens the escape hatch on the mapping face rather than narrowing it.
(ii) **Closedness is uniform in E; the equality is not.** Prop. O.1 holds for every admissible E and every arithmetic scheme. The equality needs Theorem A, which is banked for X₀ = Spec Z with N₀ = N; for a general arithmetic scheme the ⊇ direction requires N₀ to be dense in the relevant Ẑ^×_{(p)}-quotient and has **not** been re-derived here. Do not state the equality for general X₀.
(iii) **E ⊆ E_tors is necessary**, not decorative: in the un-cut suspension the equality is false (F6).
(iv) **The quotient topology on the suspension is a reading, not a quoted sentence of [x-03]** (§3.4, §7.2, F5). It is warranted by [r3s-08] p. 14 verbatim, by [x-03] p. 61's inference and p. 63's sheaf identity, and by [x-06] p. 11; but a strictly coarser topology on 𝕏₀ would void Prop. O.1. This is the single hypothesis on which the whole item balances.
(v) **Compactness is claimed only for E ⊇ E_f** (Cor. O.8); for admissible E ⊉ E_f the packet may be smaller, and closedness survives while compactness is not claimed. **Nowhere density** (Cor. O.9) additionally needs C = ℂ and X₀ flat of finite type over Spec Z (the hypotheses of Cor. 9.7).
(vi) **Corollary O.7 is outside the certification.** It is new, it was derived this session, it passed my own checks, and it owes a separate referee pass before any use.
(vii) **This pass was not blind** (§0). Weigh it accordingly, and let the adjudicator weight the other referee's pass — which may have been blind — higher on any point where we differ.

---

## 11. Sources read this session, page by page

**[x-03]** C. Deninger, *Dynamical systems for arithmetic schemes*, arXiv:1807.06400v4, `fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf` (120 PDF pages; printed folio = PDF page, verified on pp. 1, 2, 26, 27, 31, 38, 40, 63). Pages read in the fresh `pdftotext -layout` extraction: **p. 2** (intro: the suspension, "compact packets Γ_{x₀} of periodic orbits of length log N x₀", the fibration over Aut(F̄_p)/Aut(F_p)^); **p. 26** (Prop. 3.7, Cor. 3.8, §4 opening); **p. 27** ((Tors), (Image), Def. 4.1, Prop. 4.2, (30)–(31) and the sentence "Here we let Q₀^{>0} act trivially on X and X₀"); **p. 28** (Lemma 4.3, Cor. 4.4, examples E_tors, E_max); **p. 29** (E_f, E_fg, E_fd, E_fd0, the "additive mod p … not N-invariant" remark, stability); **p. 30** (Prop. 4.5 proof, Lemma 4.6); **p. 31** (Lemma 4.6 proof; §5 opening; (32); (33); **C_{x₀} = pr_{X₀}^{-1}(x₀)** verbatim); **p. 32** ((34), (35), (36), (37), (38), the injective χ_x, "It surjects onto Gal(κ(x)/κ(x₀))"); **p. 33** ((39), the fibration over Ẑ^×_{(p)}/p^Ẑ with fibres the Q₀^{>0}-orbits, (40)–(46), the p- and Q-strata X̌(C)_{p,Etors}, X̌(C)_{Q,Etors}); **p. 34** (Prop. 5.1 with proof; **Thm 5.2** and "If e.g. E ⊃ E_f then C^E_{x₀} = C_{x₀}"); **p. 37** (Remark 5.4, Thm 5.5 a) b) with proof); **p. 38** (Thm 5.5 b) proof end; **§6**: the suspension and its Q₀^{>0}-action, φ^t, Γ_{x₀} = C_{x₀} ×_{Q₀^{>0}} R^{>0}, the R^{>0}-**bijection**, Γ^E_{x₀}, "If e.g. E_f ⊂ E then Γ^E_{x₀} = Γ_{x₀}"); **p. 39** (**Thm 6.1** and the packet paragraph; the X₀(C) ×_{F∞} R^× immersion); **p. 40** (the Y₀ question verbatim; **§7 opening**: arithmetic schemes, "the topology of pointwise convergence", Tychonov, metrizability; **Lemma 7.1 with proof**); **p. 41** (Lemma 7.2 with proof; the glued topology on X•(C)); **p. 42** ("We equip X•₀(C) = X•(C)/G with the quotient topology … pr_X and hence also pr_{X₀} are continuous"; **Lemma 7.3** with proof and (51)–(52)); **p. 43** (the inductive limit topology and its closed/open criterion; **Prop. 7.4** a)–c) with proof; "We give X̌₀(C) = X̌(C)/G the quotient topology"; π, π̌ continuous and open; "**the projections pr_X : X̌(C) → X and pr_{X₀} : X̌₀(C) → X₀ are continuous**" with its proof); **p. 44** (Prop. 7.5 with proof, Prop. 7.6, Prop. 7.7); **p. 45** (Cor. 7.8 metrizability/Hausdorffness of X•₀(C); **Cor. 7.9** — Hausdorffness proved for X•(C), X•₀(C), X̌(C), X̌₀(C), and **for nothing else**); **p. 46** (the separatedness remark; the in-loci with quotient = subspace topology; F_p restricts to homeomorphisms on the characteristic-p loci; **Thm 7.10**); **p. 47** (Remarks 1–2 "not homeomorphisms in general"; the **E-versions** paragraph — subspace topologies, colimit = subspace because the charts are open, "**All preceding results in this section remain true if we replace X•(C) etc. by X•(C)_E etc.**"; (56) Ẑ ≅ Ĥ as **topological** groups; (57) the cyclotomic character); **p. 48** ((58)–(66), r continuous, Ȟ_{Etors}); **p. 49** ((67)–(68); "**The Q^{>0}-action on Ȟ_{Etors} × R^{>0} is not properly discontinuous. In section 10, we will see that this works to our advantage.**"; **§8** opening, "the system Y₀ is still infinite-dimensional", Y₀ = X̌₀(S¹) ×_{Q^{>0}} R^{>0}, Claim 8.1); **p. 50** (Claim 8.1 continued, [Per11], X̌(C)_per, **Thm 8.2** with proof, Lemma 8.3); **p. 53** (Lemma 8.3 proof end; **§9** opening, X•(C)′, **Prop. 9.1** with proof); **p. 54** (**Thm 9.2** with proof); **pp. 60–62** (the maps r, r₀ (90)–(96); the openness of r; "we obtain a continuous open and surjective map π : X_η ↠ Y"; strong approximation; **Cor. 9.7** with its proof "By Theorem 9.2 they are dense in X resp. X₀"; the E_tors remark; Thm 9.8); **p. 63** (**§10**: π : X̃ = M × R^{>0} → X = M ×_Q R^{>0}; **R_X = (π_∗R_X̃)^Q ⊂ (π_∗C⁰_X̃)^Q = C⁰_X**; "will not be a homeomorphism if π(M × {u}) is equipped with the subspace topology of X"; the non-local-triviality remark; Def. 10.1); **p. 64** (Thm 10.2 with proof; Prop. 10.3 irreducibility; **the [LR00, Lemma 3.1] remark: "the orbits of the Q^{>0}-action on Q^{>0}Ẑ^× × R^{>0} are closed … the points of Y are closed, i.e. Y is a T₁-space"**).

**[x-06]** C. Deninger, *Primes, knots and periodic orbits*, arXiv:2301.11643, `fetched/x-06-deninger-2024-primes-knots-and-periodic-orbits.pdf`. Read: **printed p. 11** (Thm 4.1; the colimit X̌₀(C) = colim_N X•₀(C); "**Set X₀ = (X̌₀(C) × R^{>0})/Q^{>0} where Q^{>0} acts diagonally**"; φ^t; the admissibility discussion; Thm 4.2); **printed p. 12** ("**The compact subsets Γ_{x₀} ⊂ X₀ consist of periodic orbits of length log N x₀ … and they are pairwise disjoint**"; the invariant-tori sentence; Thm 4.3 connectedness; the "closure of the union of all its compact orbits … this is not the case" paragraph; the p- and Q-strata).

**[r3s-08]** M. Morishita, arXiv:2508.15971v5, `fetched-r3/r3s-08-morishita-deninger-cc-bridge-2508.15971.pdf` (printed folio = PDF page, verified pp. 14, 17, 18). Read: **p. 14** ((2.2.1) the suspension and its Q₊-action; "**We equip X_K twith he quotient topology of the product X̌_K(C) × R₊**"; (2.2.2) the flow; ϖ_{L/K}; "**These projections p̌ṙ_K, p̌r_K and pr_K are continuous**"); **p. 17** (Thm 2.2.8(1)-type statements for infinite residue field; **Thm 2.2.9(1)** with the R₊-equivariant "homeomorphism" Ẑ^×_{(p)}/Np^Ẑ ×_{p^Z} R₊ ≅ Γ_p); **p. 18** (**Thm 2.2.9(2)** γ_{p,a} ≅ R₊/Np^Z and "the decomposition into connected closed R₊-orbits"; §2.3 opening, the coverings and monodromy set-up).

**[D25]** Deninger, *Rational Witt vectors and associated sheaves*, arXiv:2508.05329v1, `fetched-r3/r3s-22-…pdf` — **not opened for this item.** Nothing in Corollary A.1 or in the repairs cites it, and I make no claim about it.

**Program files.** `results/c3-r/probe-9.3-adjudication.md` (in full, including the leaked Session-14 block — see §0); `results/c3-r/probe-9.3-b.md` (in full, including the Session-14 repair blocks — see §0); `results/corpus-routing.md` (header caveats). **Deliberately not opened:** `results/c3-r/referee-s14/B-corA1-F.md`, `results/c3-r/referee-s14/B-corA1-adjudication.md`, and the body of the pre-existing `B-corA1-O.md`.

**Machine checks.** `results/c3-r/referee-s14/B-corA1-O-checks.py` / `.json`, run this session, all pass. They cover only the three elementary arithmetic claims — CRT density of N in Ẑ_{(p)}; the exact (Tors) criterion together with the F2 counterexample b = (ℓ)_{ℓ≠p} (kernel order 3, 15, 105, 1155, 15015, … → ∞ as more primes enter, with every component nonzero); and the approximation construction of Corollary O.7 (m_k ≡ 1 mod k!, |m_k/p^{j_k} − √2| < 1/k for k ≤ 12). **The topological content — Prop. O.1, Cor. O.2, Cor. O.4, Cor. O.8, Cor. O.9 — is a hand derivation from quoted sources and is not machine-checkable; the checks file makes no claim about it.**

*Extraction method:* `pdftotext -layout` into the session scratchpad, then a page-split index; every quotation above was re-read from those extractions at the stated page. No derived text artifact was written into `fetched/` or `fetched-r3/`.

— end of referee report O —
