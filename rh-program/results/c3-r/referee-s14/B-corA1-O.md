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

**(R5) Charts.** By (T1) of §3.3, closures in the colimit are computed chart-locally on the clopen charts U_ν = F_ν^{-1}(X•₀(C)_E), and F_ν : U_ν → X•₀(C)_E is a homeomorphism (Prop. 7.4 b) + p. 47). The orbit O(P₀) = {F_r P₀ : r ∈ Q₀^{>0}} meets U_ν in {F_{m/m′}P₀ : m′ | ν, m ∈ N} up to the isotropy relation F_p P₀ = P₀ (Thm 5.2, p. 34: "For any point P₀ ∈ C^E_{x₀} the isotropy group of P₀ is (Q₀^{>0})_{P₀} = N x₀^Z"). Transporting by F_ν, each chart-closure is again the closure of a set of the form {P_{a n} : n ∈ N} in X•₀(C)_E, i.e. Lemma O.6 + §5.3 + (R4) again. Hence

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
