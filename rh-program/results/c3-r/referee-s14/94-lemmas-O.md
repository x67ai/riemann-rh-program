# REFEREE REPORT O — probe 9.4 note, Lemmas A–D and Proposition 1 (the transplant trichotomy D1–D3)

**Program:** RH program, direction C3-r (geometric substrate, reduced recommission). **Date:** 2026-09-02 (Session 14).
**Referee:** referee O, one of two independent referees on this item (the other is a different model; no communication, no assumption about its findings — standing order 7).
**Note under review:** `results/c3-r/probe-9.4-note.md` (probe 9.4, dated 2026-08-26, Session 8), §§3–7, specifically Lemmas A, B, C, D and Proposition 1 with its Corollary, plus §3's freshman's-dream N-invariance argument and §7 Road 2's Haar formal count.
**Binding context read first, in full:** `results/c3-r/probe-9.3-adjudication.md` (Session-8 adjudication, with its three Session-14 bookkeeping paragraphs), then the whole 9.4 note.
**Standing order 5 discipline:** every source claim below was read this session from the on-disk PDF, with pdftotext extractions made fresh, and is quoted verbatim with its printed page (printed page = PDF page for both [x-03] and [x-06]; verified by page footers). Nothing is asserted from memory; the two places where I reason from unsourced standard algebra are labeled **[RU]** and carry no weight in any verdict.

---

## 0. VERDICT (stated first)

**PASS-WITH-REPAIRS.** 0 FATAL, 6 MAJOR, 12 MINOR.

Every one of the five displayed results survives re-derivation **as a mathematical statement about the objects the note actually applies them to** (X₀ = Spec Z; κ(x) = F̄_p; C = ℂ). I re-derived all of them line by line and, where the note's derivation was incomplete, supplied the missing derivation myself; I also attempted to break each one and failed in every case. The six MAJOR findings are: one over-general hypothesis (Lemma A), one internal contradiction with the adjudication over what "admissible" means (§4 Consequence 2), one asserted-but-not-derived step (§3), one over-reaching definability schema (Proposition 1's Corollary), one unsound interpretive inference (§6's closing paragraph, which I refute by explicit counterexample), and one under-derived constancy claim (§7's Haar count). None of them touches the trichotomy's conclusion; all six have replacement text supplied in §10 below.

Per-lemma verdicts, each argued in its own section:

| Item | Verdict | Findings |
|---|---|---|
| **Lemma A** (mod-p-additive ⇔ Teichmüller) and its converse | **PASS-WITH-REPAIRS** | O-M1 (hypothesis too general); O-m6, O-m7, O-m9 |
| **§3** freshman's-dream N-invariance | **PASS-WITH-REPAIRS** | O-M3 (asserted, not derived — full derivation supplied) |
| **Lemma B** (archimedean threshold empty on the periodic locus) | **PASS** (statement), **PASS-WITH-REPAIRS** (§6's closing inference) | O-M5 (the closing inference is false — counterexample given); O-m12 |
| **Lemma C** (Aut(C) ↠ Aut(μ(C)) = Ẑ^×) | **PASS** | O-m4, O-m5, O-m11 |
| **Lemma D** (i)(ii)(iii) | **PASS** | O-m6, O-m7, O-m8 (all strengthenings, no error found) |
| **Proposition 1** | **PASS** | O-m3, O-m4 |
| **Prop. 1's Corollary** (the no-go schema) | **PASS-WITH-REPAIRS** | O-M4 |
| **§4 Consequence 2** (D3, the transport collapse) | **PASS-WITH-REPAIRS** | O-M2 |
| **§7 Road 2** Haar formal count | **PASS-WITH-REPAIRS** | O-M6, O-m10 |

**Not re-derived (declared):** nothing in this item. Two inputs are consumed from other program documents rather than re-derived here, and are flagged as such wherever used: (i) probe A's Theorem C(b) reachability computation (adjudication §4 item 5b), which I use only to *name* the cut class E(a₀), and (ii) the adjudication's own re-derivations of the (34)–(39) anchors — which I nevertheless re-read verbatim on disk this session anyway (§1 below), so nothing here rests on them at second hand.

---

## 1. Sources read this session, with the verbatim anchors

Extractions: `pdftotext -layout` on the two on-disk PDFs named in the task, plus a 4-page extraction of [D25]. Printed page = PDF page in both [x-03] and [x-06] (checked against page footers on pp. 2, 27, 33, 34, 38, 40, 94, 99, 114, 116 and [x-06] pp. 11, 12, 13).

**[x-03] = Deninger, *Dynamical systems for arithmetic schemes*, arXiv:1807.06400v4, `fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf`.** Pages read in full this session: 2, 5, 6, 26, 27, 28, 29, 31, 32, 33, 34, 37, 38, 39, 40, 89, 90, 91, 94, 95, 99, 104, 113, 114, 116.

- **p. 2** — "If p = char κ(x₀), then Γ_{x₀} is fibred over the compact group  Aut(F̄_p^×)/Aut(F̄_p) = Ẑ^×_{(p)}/p^Ẑ". Also, same page: "the closed points x₀ of X₀ correspond bijectively to compact packets Γ_{x₀} of periodic orbits of length log N x₀ on  X₀ = X̌₀(C) ×_{Q^{>0}} R^{>0}."
- **p. 6** — "Incidentally, if we consider points of W_rat(X) with values in rings without "small multiplicative subgroups" like the complex number field C this process does not give more points." And: "The answer is simple, Y⋄ consists of all the diagrams in X⋄_c(o) whose maps are not only multiplicative but mod p also additive." And: "Thus the process of "completion" to pass from X̌₀(o) to X⋄₀(o) was necessary to obtain something interesting."
- **p. 27** — "(Tors) the group ker(χ)_tors = ker(χ|_{μ(κ)}) is finite and |(ker χ)_tors| ∈ N₀."  "(Image) Only if char κ > 0. If χ(κ^×) is torsion, then κ^× is torsion as well, i.e. κ^× ⊗ Q ≠ 0 implies χ(κ^×) ⊗ Q ≠ 0."  "**Definition 4.1.** A class E of characters χ : κ^× → C^× on algebraically closed fields κ is (N₀−)admissible if for any σ ∈ Autκ resp. ν ∈ N₀ the character χ is in E if and only if χ ∘ σ resp. χ_ν = χ ∘ ( )^ν is in E. Moreover the characters in E should satisfy (Tors)."  Also "The best condition on the characters P^× is not clear to me." Also Prop. 4.2 (E-loci G-invariant, forward- and backward N₀-invariant).
- **p. 28** — "Example. 1) E_tors : (Tors) holds  2) E_max : (Tors) and (Image) hold".
- **p. 29** — "3) E_f : (Tors) and ker χ is finite. Equivalently: |ker χ| ∈ N₀  4) E_fg : (Tors) and ker χ is finitely generated  5) E_fd : (Tors) and ker χ ⊗ Q is finite dimensional  6) E_fd0 : (Tors) and (ker χ|_{κ(x₀)^×}) ⊗ Q is finite dimensional where x₀ = π(x)". And the Remark: "in the p-adic case where we will deal with multiplicative maps P into a p-adic valuation ring and N₀ = p^Z, the right condition E is the following: P is additive mod p. This can be rephrased in terms of absolute values and translated to the case where C is the complex number field. However the resulting class E is not N-invariant."
- **p. 31** — "Fix an injective homomorphism ι : μ(K) ↪ μ(C)." "Let C be an algebraically closed field which satisfies the conditions before Corollary 4.4." The isomorphism (32) i_x : μ^{(p)}(K) ≅ κ(x)^×.
- **p. 32** — (34) "N x₀^Ẑ = Gal(κ(x)/κ(x₀)) ↪ Aut(κ(x)^×) = Ẑ^×_{(p)}"; (35) "Ẑ^×_{(p)} × N₀ ↠ S , (a, ν) ↦ χ_x·(a,ν) := χ_x ∘ ( )^a ∘ ( )^ν", with "Two elements (a, ν) and (a′, ν′) are in the same fibre of this map if and only if ν′ = νp^n and a = p^n a′ for some n ∈ Z"; and (38) "(Ẑ^×_{(p)}/N x₀^Ẑ) ×_{p^Z} Q₀^{>0} ≅ C_{x₀}".
- **p. 33** — "The set C_{x₀} fibres over the compact group  Ẑ^×_{(p)}/p^Ẑ = Aut(F̄_p^×)/Aut(F̄_p) ,  and the fibres are the Q₀^{>0}-orbits in C_{x₀}." And: "The maps (37), (38) and the fibration map depend on our choices of x and ι."
- **p. 34** — "**Theorem 5.2.** … {P₀ ∈ X̌₀(C)_E | (Q₀^{>0})_{P₀} ≠ 1} = ∐_{x₀} C^E_{x₀}. For any point P₀ ∈ C^E_{x₀} the isotropy group of P₀ is (Q₀^{>0})_{P₀} = N x₀^Z where N x₀ = |κ(x₀)|. If e.g. E ⊃ E_f then C^E_{x₀} = C_{x₀}."
- **p. 38** — the suspension: "X₀ = X̌₀(C)_E ×_{Q₀^{>0}} R^{>0}. It is the quotient of X̌₀(C)_E × R^{>0} by the right Q₀^{>0}-action given by  (P₀, u)q = (P₀q, q^{−1}u) = (F_q(P₀), q^{−1}u)"; "φ^t([P₀,u]) = [P₀, ue^t]"; "Γ_{x₀} = C_{x₀} ×_{Q₀^{>0}} R^{>0} ⊂ X₀"; and decisively **"Thus all R^{>0}-orbits in Γ_{x₀} are circles R^{>0}/N x₀^Z and Γ_{x₀} fibres over Ẑ^×_{(p)}/p^Ẑ = Aut(F̄_p^×)/Aut(F̄_p) with fibres the R^{>0}-orbits in Γ_{x₀}."**
- **p. 39** — "**Theorem 6.1.** … {x₀ ∈ X₀ | (R^{>0})_{x₀} ≠ 1} = ∐_{x₀} Γ^E_{x₀}. For any point x₀ ∈ Γ^E_{x₀} the isotropy group of x₀ is (R^{>0})_{x₀} = N x₀^Z."
- **p. 40** — "**In this section, C is an algebraically closed field with a valuation | | and the corresponding topology.** … we give X(C)• the topology of pointwise convergence. It is the subspace topology induced by the Tychonov topology of C^R = ∏_R C … Since R is countable, X(C)• is a metrizable topological space."
- **p. 89** — "Let o be a p-adically complete rank one valuation ring with quotient field C, maximal ideal m and residue field k of characteristic p." And: "In the following we only consider the monoid N₀ generated by p i.e. the F_p = ( )^p action."
- **p. 90** — Definition 14.1 (triples (x, y, P^×) with the commutative diagram κ(y)→k, O_{{x},y}→o, κ(x)→C; equivalently multiplicative P_y : O_{{x},y} → o "sending 1 to 1 and 0 to 0"); Definition 14.2 (the p-adic continuity condition).
- **p. 94** — "**Definition 14.5.** … Y̌_α = {(x,y,P̌_y) ∈ X̌_c(o) | |P̌_y(r+s) − P̌_y(r) − P̌_y(s)| ≤ α for r, s ∈ Ô_{{x},y}}." "For α = 1/p we are looking at multiplicative maps P̌_y which mod p are also additive. Set Y̌ = Y̌_{1/p}." "**Proposition 14.7.** For 0 < α < 1 we have F_p(Y̌_α) = Y̌_α and Y̌_α ⊂ Y̌, and hence Y̌_α = Y̌ for α ≥ 1/p." Also (172) W_p(P̌_y) : W_p(Ô^♭) = lim ZÔ^♭/I^n → lim o/ω_α^n = o, and (174).
- **p. 95** — the proof of Prop. 14.7: "= |(P̌_y(r+s) − P̌_y(r) − P̌_y(s))^{p^ν} + pc| for some c ∈ o  ≤ max(|P̌_y(r+s)−P̌_y(r)−P̌_y(s)|^{p^ν}, |p|)  ≤ max(α^{p^ν}, 1/p)."
- **p. 99** — Definition 14.12 = (183); and the Remark: "I do not know how to transport such conditions to the points of X̌(C), where X is a scheme of finite type over spec Z and C is the complex number field."
- **p. 104** — "**Remark 14.17.** … G × Aut(o) operates F_p-equivariantly on X(o)• = W_rat(X)(o) and X̌(o). Since automorphisms of o are p-adically continuous we have compatible G × Aut(o)-operations on X_c(o)•, X̌_c(o), X⋄_c(o) and Y⋄ in the obvious way."
- **p. 113** — "For (x,y) = (s,s) the continuous local ring homomorphisms P̂_y^♭ : κ → o^♭ with P̂_y^♭(f) ≠ 0 … are simply the ring homomorphisms P̂_y : κ ↪ k ⊂ o^♭". "**Theorem 15.6.** … 1) There is a natural G × Aut(o) × ⟨F_p⟩-equivariant identification Y⋄ = Hom_cont(ô_K^♭, o^♭)".
- **p. 114** — "Y⋄_s := pr_X^{−1}(s) = Hom(κ, k)."  "Y⋄_{0s₀} := pr_{X₀}^{−1}(s₀) ≅ ∐_{τ₀}{0}/o^×_{K₀} = Hom(κ₀, k)."  "6) The only periodic (i.e. finite) orbit of the F_p-action on Y⋄₀ is Y⋄_{0s₀}. It has order log_p N(π₀) = r if q = p^r."
- **p. 116** — "**Proposition 15.8.** For X₀ = spec Z_p and o = o_p, the set Y̌₀ ⊂ Y⋄₀ consists of the F_p-fixed point s₀ = (ô_p^♭ → F̄_p → ô_p^♭)G and the (infinite) F_p^Z-orbit of η₀ = (ô_p^♭ →^{id} ô_p^♭)G."

**[x-06] = Deninger, *Primes, knots and periodic orbits*, arXiv:2301.11643, `fetched/x-06-deninger-2024-primes-knots-and-periodic-orbits.pdf`.** Pages read: 11, 12, 13.

- **p. 11** — Theorem 4.1, including the group actions verbatim: "Here σ ∈ G acts on X(C)• via (x, P^×)^σ = (x^σ, P^× ∘ σ) and ν ∈ N acts G-equivariantly via F_ν(x, P^×) = (x, P^× ∘ ( )^ν)."  And: "the dynamical system (X₀, φ^t) has too many periodic orbits, since the N-space W_rat(X₀)(C) does not know enough about the addition in O_{X₀}. In the local p-adic situation below, we know the right modification to make. However in the global case presently we can only impose an "admissible" condition E on the characters P^× : κ(x)^× → C^×".  "**Theorem 4.2.** … {x₀ ∈ X₀^E | φ^t(x₀) = x₀ for some t > 0} = ∐_{x₀} Γ_{x₀}."
- **p. 12** — "The compact subsets Γ_{x₀} ⊂ X₀ consist of periodic orbits of length log N x₀ where N x₀ = |κ(x₀)| (= |R₀/m₀|) and they are pairwise disjoint. In fact Γ_{x₀} is a fibre space over the compact group Aut(F̄_p^×)/Aut(F̄_p) where p = char κ(x) with fibres the compact orbits in Γ_{x₀}."
- **p. 13** — Theorem 4.4 and "In view of Theorem 4.3 the map in the theorem is not a homeomorphism since X₀ is connected, whereas the left hand side is disconnected." Also, relevant to Lemma D(iii): "Consider a field of characteristic zero containing all roots of unity, and fix an injective homomorphism ι : μ(F) = μ(F̄) ↪ C^×. … **One can show that the connected components of W_rat(spec F)(C) are parametrized by the embeddings μ(F) ↪ C^×** and that X_F(C) is the component corresponding to ι." And "The absence of the Steinberg relations in rational cohomology is an indication that the space X_F(C) and hence also our space W_rat(X)(C) do not encode enough information about the additive structure of F resp. O_X."

**[D25] = Deninger, *Rational Witt vectors and associated sheaves*, arXiv:2508.05329v1, `fetched-r3/r3s-22-deninger-rational-witt-vectors-associated-sheaves-arxiv-2508.05329v1-SESSION8-FETCH.pdf`.** Introduction (pp. 1–3) extracted and grepped: the note's §7 Road 1 quote is present verbatim — "The algebra ZA knows nothing about the addition in A. However, the larger G is, … may be interesting to experiment with stronger descent conditions than the Galois … additive structure of A to remedy the defects in the constructions of [KS16] and [Den24]". Quote confirmed; not otherwise load-bearing for this item.

**Not consulted for this item:** [r3s-08] Morishita. The adjudication's §4 item 4 and its third Session-14 bookkeeping paragraph forbid citing [r3s-08] §2.2 for the packet identification or for topology; nothing in Lemmas A–D or Proposition 1 needs it, and I cite it nowhere.

---

## 2. The standing setup, re-derived from the page anchors (so that §§3–9 are checkable without the note)

Throughout, X₀ = Spec Z (the note fixes this from its §4 onward), K = Q̄, X = Spec Z̄ the normalization of Spec Z in Q̄, G = Gal(Q̄/Q). C = ℂ. Fix once and for all a closed point x₀ = (p) of X₀, a point x of X over x₀, and Deninger's injective ι : μ(K) ↪ μ(C) (p. 31).

**(S1) The objects.** X(C)• = {(x, P^×) : x ∈ X, P^× ∈ Hom(κ(x)^×, C^×)} ([x-06] p. 11). G acts by (x,P^×)^σ = (x^σ, P^×∘σ); N acts by F_ν(x,P^×) = (x, P^×∘( )^ν) ([x-06] p. 11, verbatim). X₀(C)• = X(C)•/G; X̌₀(C) = colim_N X₀(C)•, on which Q^{>0} acts; X₀ = X̌₀(C)_E ×_{Q^{>0}} R^{>0} with (P₀,u)q = (F_q(P₀), q^{−1}u) and φ^t[P₀,u] = [P₀, ue^t] ([x-03] p. 38). The extension by zero of P^× is written P : κ(x) → C, with P(0)=0 ([x-03] p. 27).

**(S2) Packet coordinates.** κ(x) ≅ F̄_p; i_x : μ^{(p)}(K) ≅ κ(x)^× (32); χ_x = ι∘i_x^{−1} : κ(x)^× ↪ C^×. By (35) (p. 32) every character with finite cyclic kernel of order in N₀ is χ_x·(a,ν) = χ_x∘( )^a∘( )^ν with (a,ν) ∈ Ẑ^×_{(p)} × N₀, and (a,ν) ~ (a′,ν′) iff ν′ = νp^n, a = p^n a′. By (38) C_{x₀} ≅ (Ẑ^×_{(p)}/N x₀^Ẑ) ×_{p^Z} Q₀^{>0}; for X₀ = Spec Z, N x₀ = p, and p acts trivially on Ẑ^×_{(p)}/p^Ẑ, so C_{(p)} ≅ B_p × (Q₀^{>0}/p^Z) with **B_p := Ẑ^×_{(p)}/p^Ẑ**.

**(S3) The base class and the fibration — the exact statement Proposition 1 consumes.** Deninger states the fibration twice. At the level of C_{x₀} (p. 33): "The set C_{x₀} fibres over the compact group Ẑ^×_{(p)}/p^Ẑ = Aut(F̄_p^×)/Aut(F̄_p), and the fibres are the Q₀^{>0}-orbits in C_{x₀}." At the level of the **suspension** (p. 38): "Γ_{x₀} fibres over Ẑ^×_{(p)}/p^Ẑ = Aut(F̄_p^×)/Aut(F̄_p) with fibres the R^{>0}-orbits in Γ_{x₀}." Write β : Γ_{(p)} → B_p for the second map and call β(z) the **base class** of z. Explicitly, in (35)-coordinates, β([χ_x·(a,ν), u]) = a mod p^Ẑ; this is well-defined precisely because the (35)-fibre relation moves a inside p^Z ⊆ p^Ẑ.

*Re-derivation of "fibres = orbits" for X₀ = Spec Z, for completeness.* With N x₀ = p, (38) reads C_{(p)} = (Ẑ^×_{(p)}/p^Ẑ) ×_{p^Z} Q₀^{>0} where p^Z acts trivially on the left factor, so C_{(p)} = B_p × (Q₀^{>0}/p^Z) and the projection to B_p has fibres the Q^{>0}-orbits, since Q^{>0} acts only on the second factor. Suspending, Γ_{(p)} = C_{(p)} ×_{Q^{>0}} R^{>0} = B_p × (R^{>0}/p^Z), and the R^{>0}-action is on the second factor alone; its orbits are the circles R^{>0}/p^Z of length log p, and they are exactly the fibres of β. This reproduces Deninger's p. 38 sentence, and — the point that matters below — **the flow acts trivially on the base B_p**. ∎

**(S4) The periodic locus.** By Theorem 6.1 (p. 39) the set of points of X₀ with non-trivial R^{>0}-isotropy is exactly ∐_{x₀} Γ^E_{x₀}, with isotropy N x₀^Z; for X₀ = Spec Z this is ∐_p Γ^E_{(p)} with all orbits of length log p. Equivalently ([x-06] Thm 4.2, p. 11–12) "{x₀ ∈ X₀^E | φ^t(x₀) = x₀ for some t > 0} = ∐_{x₀} Γ_{x₀}", with "periodic orbits of length log N x₀ … pairwise disjoint". For X₀ = Spec Z the periodic locus therefore coincides with the char-p locus of X̌₀(C)_E: X̌₀(C)_{p,E} = pr_{X₀}^{−1}((p))^{Q^{>0}} = C_{(p)}. **So "the periodic locus" is the right locus, and for Spec Z it is not merely contained in but equal to the char-p locus** (this settles one of the press points on Lemma B; see §5).

**(S5) Two topological caveats that bear on the scope of Proposition 1.** (i) From §7 on, C is *not* an abstract field: "In this section, C is an algebraically closed field with a valuation | | and the corresponding topology" (p. 40), and the topology on X(C)• is pointwise convergence into (C, | |). (ii) The identifications (37), (38) and β "depend on our choices of x and ι" (p. 33). Both caveats are used in §8 and §9.

---

## 3. LEMMA A — re-derivation, converse, and the one finding

### 3.1 The statement under review

> **Lemma A (note, §4).** Let o be as in §2 (residue field k algebraically closed of char p), κ an algebraically closed field of characteristic p, and P : κ → o multiplicative with P(0)=0, P(1)=1, whose restriction to κ^× is a group homomorphism into o (values automatically in μ^{(p)}(o), the prime-to-p roots of unity, since κ^× is prime-to-p torsion). Then |P(r+s) − P(r) − P(s)| ≤ |p| for all r,s ∈ κ **iff** P = [·]∘τ for a unique field embedding τ : κ ↪ k, where [·] is the Teichmüller section of the reduction μ^{(p)}(o) ≅ μ^{(p)}(k).

### 3.2 Fidelity of the hypothesis to the source

The condition is Deninger's Def. 14.5/14.12 with α = 1/p, read at the fibre where it is a condition on κ. Verbatim (p. 94): "Y̌_α = {(x,y,P̌_y) ∈ X̌_c(o) | |P̌_y(r+s) − P̌_y(r) − P̌_y(s)| ≤ α for r,s ∈ Ô_{{x},y}}" and "For α = 1/p we are looking at multiplicative maps P̌_y which mod p are also additive." Two checks:

1. **The threshold is immaterial.** Prop. 14.7 (p. 94) gives Y̌_α ⊂ Y̌_{1/p} for every 0 < α < 1 and equality for α ≥ 1/p. So "|defect| ≤ α for some α < 1" and "|defect| ≤ |p|" define the same locus. The note's F2 quotes this correctly; the proof (p. 95) is exactly the ultrametric estimate "|(defect)^{p^ν} + pc| ≤ max(α^{p^ν}, 1/p)". Lemma A may therefore be stated with |p| without loss. **Checked.**
2. **The domain.** At the closed point the relevant local ring *is* the residue field: p. 113, "The corresponding local rings O_{{x},η} are o_K resp. κ = o_K/m_K", and for (x,y) = (s,s) the completion is κ itself. So Lemma A is precisely the (s,s)-fibre computation of Deninger's §15. **Checked** — and this is why the note's consistency check against Thm 15.6 is the right check.

### 3.3 Finding O-M1 (MAJOR): the hypothesis "κ algebraically closed of characteristic p" is too general; both the statement and the proof require κ^× torsion, i.e. κ = F̄_p

The parenthetical "values automatically in μ^{(p)}(o) … since κ^× is prime-to-p torsion" is **false** for a general algebraically closed field of characteristic p. κ^× is torsion if and only if κ is an algebraic closure of a finite field: if κ ⊋ F̄_p then κ contains an element t transcendental over F_p, and t is not a root of unity. (Concretely take κ = the algebraic closure of F_p(t).)

The failure is not cosmetic; it propagates twice.

- **The statement becomes ill-formed.** "[·]" is defined only on μ^{(p)}(k) (the note says so: "the Teichmüller section of the reduction μ^{(p)}(o) ≅ μ^{(p)}(k)"). If k^× is not torsion, [·]∘τ is not defined on all of κ^×, so the right-hand side of the "iff" has no meaning.
- **The (⇒) proof's last step fails.** The step "For r ∈ κ^×, P(r) and [τ(r)] are prime-to-p roots of unity with the same reduction, hence equal" uses exactly the torsion hypothesis. Without it one obtains only P(r) ≡ [τ(r)] mod m, i.e. P = ε·([·]∘τ) with ε : κ^× → 1 + m a group homomorphism, and 1 + m is a *divisible* group (see §3.5(b) below), so Hom(κ^×, 1+m) ≠ 0 as soon as κ^×/μ(κ) ≠ 0. The additivity bound must then be used a second time to kill ε — which the note does not do.

**Severity MAJOR, not FATAL**, because in every place the note applies Lemma A the field is F̄_p: the packet coordinates have κ(x) ≅ F̄_p ([x-03] p. 31–32), and Thm 15.6's closed-point fibre has κ = o_K/m_K = F̄_p with k = F̄_p ([x-03] pp. 113–114). Replacement text in §10.

### 3.4 The corrected Lemma A, re-derived in full (κ = F̄_p)

**Lemma A′ (referee's re-derivation).** Let o be a p-adically complete rank-one valuation ring with maximal ideal m, algebraically closed fraction field C of characteristic 0, and residue field k of characteristic p (o = O_{C_p}, k = F̄_p is the case used). Let κ be an algebraic closure of F_p (so κ^× = μ^{(p)}(κ) is torsion of prime-to-p order) and let P : κ → o be multiplicative with P(0) = 0, P(1) = 1 and P|_{κ^×} a group homomorphism into o∖{0}. Then

  |P(r+s) − P(r) − P(s)| ≤ |p| for all r,s ∈ κ  ⟺  P = [·]∘τ for a unique field embedding τ : κ ↪ k,

where [·] : μ^{(p)}(k) → μ^{(p)}(o) is the inverse of reduction.

*Step 0 — [·] exists and is unique.* Reduction red : μ^{(p)}(o) → μ^{(p)}(k) is (a) **injective**: if ζ^d = 1 with (d,p)=1 and ζ ∈ 1+m, write ζ = 1+y with y ∈ m; then 0 = ζ^d − 1 = (ζ−1)·Σ_{i<d} ζ^i and Σ_{i<d} ζ^i = d + x with x ∈ m; since (d,p) = 1, d is a unit of o and so is d+x; hence ζ = 1. (This is the note's argument, and it is correct.) (b) **surjective**: μ^{(p)}(o) = μ^{(p)}(C) ≅ ⊕_{ℓ≠p} Q_ℓ/Z_ℓ because C is algebraically closed of characteristic 0 and all roots of unity are integral; μ^{(p)}(k) ≅ ⊕_{ℓ≠p} Q_ℓ/Z_ℓ because k is algebraically closed of characteristic p. red preserves ℓ-primary components, is injective on each, and the image of the divisible group Q_ℓ/Z_ℓ is divisible; the only non-zero divisible subgroup of Q_ℓ/Z_ℓ is itself (its proper subgroups are the finite Z/ℓ^n). Hence red is onto. So [·] := red^{−1} exists, is unique, and is multiplicative. **The note's parenthetical for Step 0 is correct as written.** ✓

*Step 1 (⇒).* In a rank-one valuation ring, {z : |z| ≤ |p|} = p·o (z/p ∈ o iff |z| ≤ |p|). So the defect lies in p·o ⊆ m, and τ := (P mod m) : κ → k is additive; it is multiplicative and sends 1 ↦ 1, hence is a ring homomorphism; being a ring homomorphism out of a field with τ(1) ≠ 0 it is injective. For r ∈ κ^×, P(r) lies in μ^{(p)}(o) (P|_{κ^×} is a homomorphism from a prime-to-p torsion group), and [τ(r)] ∈ μ^{(p)}(o) has the same reduction τ(r); by Step 0(a), P(r) = [τ(r)]. Both sides vanish at 0. Hence P = [·]∘τ, and τ = [·]^{−1}∘P|_{κ^×} is unique. ✓

*Step 2 (⇐) — the press point, the V F = p identity.* Let τ : κ ↪ k be a field embedding and P = [·]∘τ. Since k is perfect (algebraically closed of char p) and o is p-adically complete with residue field k, there is a ring homomorphism ι_W : W(k) → o lifting id_k, and it is injective (W(k) is a p-adic DVR, ∩_n p^n W(k) = 0, and p ↦ p ≠ 0 in the characteristic-0 domain o). The Witt Teichmüller [a]_W = (a,0,0,…) satisfies [a]_W^d = [a^d]_W = 1 for a of finite order d, so ι_W([a]_W) is a prime-to-p root of unity in o reducing to a; by the uniqueness in Step 0 it *is* [a]. So it suffices to compute in W(k).

For a,b ∈ k the first Witt component (equivalently the 0-th ghost component) of a Witt sum is the sum of the first components, so [a]_W + [b]_W − [a+b]_W has first component 0, i.e. lies in V W(k). Since k has characteristic p and is perfect, F is bijective on W(k) and VF = FV = p, so V W(k) = V F W(k) = p W(k). Hence
  [a]_W + [b]_W − [a+b]_W ∈ p W(k), so |[a] + [b] − [a+b]| ≤ |p| in o.
Now for r,s ∈ κ, using that τ is a ring homomorphism, P(r+s) − P(r) − P(s) = [τ(r)+τ(s)] − [τ(r)] − [τ(s)], which by the display has absolute value ≤ |p|. ✓

**Verdict on the converse: the V F = p step is correct as the note states it**, with the two clarifications made explicit above (the ring map W(k) → o, and the identification of the Witt Teichmüller with the note's [·]). The [RU] content is only the classical Witt-vector facts (first component additive; VF = FV = p for perfect char-p rings; W(k) → o for p-adically complete rings with perfect residue field). No dimension-theory- or Witt-theory source is on disk; I flag this as **[RU]** and note that Deninger's own text uses the same facts (p. 94 (172), Prop. 14.14 p. 100, "[CD14] presentation"), so the note is not more exposed here than the source it is checking.

### 3.5 Break attempt on Lemma A′ (failed — the lemma is sharp)

(a) *Try to perturb a Teichmüller lift.* Any P satisfying the bound has P = ε·([·]∘τ) with ε : κ^× → 1 + m a homomorphism, and ε must be trivial: κ^× = μ^{(p)}(κ) ≅ ⊕_{ℓ≠p} Q_ℓ/Z_ℓ is torsion, so ε(κ^×) is a torsion subgroup of 1+m; a prime-to-p root of unity ≠ 1 is not ≡ 1 mod m (Step 0(a)), so the torsion of 1+m is contained in μ_{p^∞}; and Hom(Q_ℓ/Z_ℓ, μ_{p^∞}) = Hom(Q_ℓ/Z_ℓ, Q_p/Z_p) = 0 for ℓ ≠ p. Hence ε ≡ 1. **No perturbation exists.**

(b) *Why the same attempt succeeds in the over-general statement, confirming O-M1.* 1+m is divisible: for u ∈ 1+m and n ≥ 1, y^n = u has a solution y ∈ C with |y| = 1, and ȳ^n = 1 in the perfect field k forces ȳ = 1 when n is a power of p, while for n prime to p the reduction argument plus divisibility of k^× gives a solution in 1+m after multiplying by a root of unity. So 1+m is a divisible abelian group with torsion μ_{p^∞}, hence contains uniquely divisible (Q-vector space) summands as soon as it is not torsion. If κ^×/μ(κ) ≠ 0 (i.e. κ ⊋ F̄_p), Hom(κ^×, 1+m) ≠ 0, so the *reduction argument alone* does not pin P. This is exactly the hole named in O-M1. (Whether the additivity bound nevertheless forces P = [·]∘τ for large κ is a genuine question — a limit argument along the perfection, using (r+s)^{1/p^n} = r^{1/p^n} + s^{1/p^n}, plausibly closes it — but **I did not re-derive it and do not assert it**; the repair is simply to restrict the hypothesis, which costs the note nothing.)

(c) *Try to evade P(1) = 1.* Deninger's multiplicative maps send 1 to 1 and 0 to 0 (Def. 14.1, p. 90), so this is not available.

### 3.6 Consistency with Theorem 15.6 (the note's own check), verified

p. 113 verbatim: for (x,y) = (s,s) the relevant maps "are simply the ring homomorphisms P̂_y : κ ↪ k ⊂ o^♭"; p. 114: "Y⋄_s := pr_X^{−1}(s) = Hom(κ, k)"; p. 114 part 6: "The only periodic (i.e. finite) orbit of the F_p-action on Y⋄₀ is Y⋄_{0s₀}. It has order log_p N(π₀) = r if q = p^r", with (224) "Y⋄_{0s₀} ≅ Hom(κ₀,k)". So over the closed point the mod-p-additive points are exactly the field embeddings — which is Lemma A′ — and their count downstairs is |Hom(κ₀,k)| = [κ₀:F_p] = r, one F_p-orbit, suspending to a single circle of length r·log p = log N(π₀). **The note's consistency check is correct and I confirm it against the printed statements.** ✓

---

## 4. §3's freshman's-dream N-invariance argument — asserted, not derived (finding O-M3, MAJOR), and the derivation supplied

### 4.1 What the note says

> "The freshman's-dream asymmetry makes it precise: additivity mod p is ( )^p-stable (Prop. 14.7's computation) but not ( )^ℓ-stable for ℓ ≠ p, since (r+s)^ℓ ≢ r^ℓ + s^ℓ mod p. A mod-p-type selection and the full-Q^{>0} suspension design cannot coexist; one must give. [Derived; consistent with both Deninger remarks in F6.]" And §10 lists "the freshman's-dream N-invariance argument (§3)" among the things "fully derived here".

### 4.2 Why this does not yet establish the claim

Three defects in the displayed reason.

1. **The congruence is mis-stated.** We are working *in* characteristic p; there is nothing to reduce mod p. The correct statement about κ = F̄_p is (r+s)^ℓ ≠ r^ℓ + s^ℓ in κ, for ℓ ≠ p.
2. **The implication is not valid as stated.** The failure of the freshman's dream *in κ* does not by itself say anything about the additivity defect of P∘( )^ℓ, because P is not additive to begin with — only additive modulo p. One has to compute the defect of the composite in o, not the failure of a power map in κ.
3. **The (⇐) half is also under-derived.** "( )^p-stability" is attributed to "Prop. 14.7's computation"; Prop. 14.7 (p. 94–95) proves F_p(Y̌_α) = Y̌_α at the level of the *whole* space Y̌_α, which is exactly the right citation — that half is fine — but the note does not connect it to Lemma A's classification, which is where the asymmetry becomes transparent.

**Severity MAJOR:** the conclusion is true (I prove it below), but §10's "fully derived" claim is not met by the sentence as written, and the sentence is the note's only support for requirement 4 of §3 (compatibility with the Q^{>0}-suspension) and hence for the framing of the whole trichotomy.

### 4.3 The derivation (referee's, complete)

Fix κ = F̄_p, o and k = F̄_p as in Lemma A′, and let **E_loc := {P : κ → o multiplicative, P(0)=0, P(1)=1, |P(r+s) − P(r) − P(s)| ≤ |p| ∀r,s}**. By Lemma A′, E_loc = {[·]∘τ : τ ∈ Hom_ring(κ,k)} = {[·]∘τ : τ ∈ Aut(F̄_p)} (every field endomorphism of F̄_p is an automorphism, since it is injective and every element of F̄_p is algebraic with all conjugates in the image). Deninger's Frobenius acts by pre-composition: F_ν(P) = P∘( )^ν ([x-06] p. 11, verbatim).

**(a) E_loc is F_p-stable, both ways.** For P = [·]∘τ, F_p(P)(r) = P(r^p) = [τ(r^p)] = [τ(r)^p] = [τ(r)]^p = P(r)^p; and τ∘Frob is again a field embedding κ ↪ k, so F_p(P) = [·]∘(τ∘Frob) ∈ E_loc. Conversely, Frob is bijective on κ so τ ↦ τ∘Frob is a bijection of Hom_ring(κ,k), giving F_p(E_loc) = E_loc. (This reproves, in the classified form, the half of Prop. 14.7 that says F_p(Y̌_α) = Y̌_α.) ✓

**(b) E_loc is not F_ℓ-stable for any prime ℓ ≠ p.** Let P = [·]∘τ ∈ E_loc and set Q := F_ℓ(P) = P∘( )^ℓ, i.e. Q(r) = [τ(r)^ℓ] = [ψ(r)] with ψ := ( )^ℓ∘τ. Q is multiplicative, Q(0)=0, Q(1)=1, and Q|_{κ^×} is a homomorphism, so Lemma A′ applies to Q: Q ∈ E_loc iff Q = [·]∘τ′ for a field embedding τ′. Since [·] is injective on μ^{(p)}(k) = k^×, that forces τ′ = ψ, so Q ∈ E_loc iff ψ = ( )^ℓ∘τ is **additive**. It is not: take a = τ(r), b = τ(s) with a = b = 1; then ψ(r+s) = (a+b)^ℓ = 2^ℓ while ψ(r) + ψ(s) = 2, and 2^ℓ = 2 in F̄_p iff 2(2^{ℓ−1} − 1) = 0 in F_p, i.e. iff p = 2 or p | 2^{ℓ−1} − 1. Choosing ℓ = 2 and p = 3 gives 4 = 1 ≠ 2 = 1 + 1 in F̄_3. Hence Q ∉ E_loc. ✓

**(c) An explicit witness, defect computed in o.** p = 3, ℓ = 2, r = s = 1 ∈ F̄_3, P = [·]∘id:
  F_2(P)(1+1) − F_2(P)(1) − F_2(P)(1) = P(2²) − 2P(1²) = P(1̄) − 2 = 1 − 2 = −1,
and |−1| = 1 > |3|. So the defect of F_2(P) is a *unit*: not merely above the threshold |p|, but at the maximum possible value. ✓

**(d) Conclusion.** E_loc satisfies the p^Z-half of Deninger's admissibility biconditional (Def. 4.1, p. 27: "χ is in E if and only if χ∘σ resp. χ_ν = χ∘( )^ν is in E") and violates the ν-half for every ν with a prime factor ℓ ≠ p. This is exactly Deninger's own verdict, p. 29: "However the resulting class E is not N-invariant." And it is exactly why his local setting can afford the condition: p. 89, "In the following we only consider the monoid N₀ generated by p i.e. the F_p = ( )^p action." So the note's requirement 4 stands, now proved rather than asserted. ∎

**Note for the record:** the asymmetry is *not* about the freshman's dream in κ per se; it is that ( )^p is a **ring** endomorphism of κ while ( )^ℓ is only a **group** endomorphism of κ^×, and Lemma A′ says precisely that mod-p additivity is the condition that remembers the ring structure. That is the same observation the note's own Consequence 1 makes; §3 should be phrased through it.

---

## 5. LEMMA B — the archimedean defect bound (D2)

### 5.1 The statement, re-derived

> **Lemma B (note, §6).** For X₀ = Spec Z, at every point of every packet (any prime p, any character P in any class E ⊆ E_tors), the test r = s = 1 gives |P(1̄+1̄) − P(1̄) − P(1̄)| = |P(2̄) − 2| ≥ 1, since P(2̄) is a root of unity or 0. Hence the class "archimedean defect ≤ ε at char-p points" is empty on the periodic locus for every ε < 1.

*Referee's re-derivation.* Let x be a point of X = Spec Z̄ over (p), so κ(x) ≅ F̄_p, and let P^× : κ(x)^× → ℂ^× be any group homomorphism, P its extension by zero (Deninger's convention, p. 27). Since κ(x)^× = F̄_p^× is a torsion group, P^×(κ(x)^×) ⊆ μ(ℂ), so every non-zero value of P has modulus 1. Now 1̄ + 1̄ = 2̄ in κ(x), and P(1̄) = 1 (multiplicativity plus P(1) = 1). Two cases:
- p ≠ 2: 2̄ ∈ κ(x)^×, so |P(2̄)| = 1 and |P(2̄) − 2| ≥ 2 − |P(2̄)| = 1, with equality iff P(2̄) = 1, i.e. iff 2̄ ∈ ker P^×.
- p = 2: 2̄ = 0, P(2̄) = 0, and |0 − 2| = 2 ≥ 1.
So the defect at (r,s) = (1,1) is ≥ 1 at **every** character over **every** char-p point, with no hypothesis on E beyond E ⊆ E_tors (indeed with no hypothesis at all — (Tors) is not used). Since the note's §6 frames the condition on global functions ("the evaluation ZΓ(X,O) → C"), and r = s = 1 ∈ Γ(X,O) = Z̄ evaluates to 1̄ ∈ κ(x), the test is available in that framing. By §2 (S4), for X₀ = Spec Z the periodic locus of X₀ is exactly ∐_p Γ^E_{(p)}, i.e. exactly the char-p locus; so **the selected set is empty on the periodic locus for every threshold ε < 1**. ∎ ✓

The bound is **sharp**: ε = 1 is attained (take P^× trivial on the subgroup generated by 2̄, e.g. P^× = 1). So "for every ε < 1" is exactly the right quantifier, and it matches the local principle's own range 0 < α < 1 (Defs. 14.5, 14.12).

### 5.2 The second half of Lemma B (no completion mechanism), checked

The note adds: "the (F3) extension mechanism requires the defect ideal to land in a topologically nilpotent set (|·| < 1, so that lim ZR/I^n receives the evaluation — (172), p. 94); with a defect bounded below by 1 there is no completion and no A_inf-analog action." Verified against (172) on p. 94: "Choose an element ω_α ∈ o with α ≤ |ω_α| < 1. Then (x,y,P̌_y) ∈ Y̌_α gives a ring homomorphism P̌_y : ZÔ^♭ → o with P̌_y(I_y) ⊂ ω_α o and hence an induced ring homomorphism W_p(P̌_y) : W_p(Ô^♭) = lim ZÔ^♭/I_y^n → lim o/ω_α^n = o." The construction consumes |ω_α| < 1 twice: to have I_y map into ω_α o and to have lim o/ω_α^n = o. With a defect of modulus ≥ 1 neither holds. **Checked.** ✓ I add one strengthening the note does not state: there is also **no self-improvement** archimedeanly. Over ℂ, if d := P(r+s) − P(r) − P(s), then F_2(P)'s defect at (r,s) is P(r+s)² − P(r)² − P(s)² = 2P(r)P(s) + 2d(P(r)+P(s)) + d², whose leading term has modulus 2 when |P(r)| = |P(s)| = 1. So Prop. 14.7's mechanism (p. 95, the ultrametric estimate max(α^{p^ν}, 1/p)) not only fails to transfer but reverses sign: powers *increase* the archimedean defect. This is worth recording because F2's self-improvement is what makes the local threshold canonical.

### 5.3 Is "the periodic locus" the right locus? — YES for Spec Z, with a scope sentence owed

Press point answered in §2 (S4): by Theorem 6.1 (p. 39) the periodic points are exactly ∐ Γ^E_{x₀}; for X₀ = Spec Z, C_{(p)} = X̌₀(C)_{p,E}, so the periodic locus and the char-p locus coincide and Lemma B's derivation covers both. For **general** X₀ of dimension ≥ 1 the two differ (there are char-p points with infinite residue field, which are not periodic under E ⊆ E_max by Thm 5.2, p. 34); Lemma B's computation still kills the threshold condition on all char-p points with κ(x) = F̄_p, but the phrase "at char-p points" then needs "with finite residue field at the image point". Since the note fixes X₀ = Spec Z from §4 onward this is a scope sentence, not an error: **MINOR O-m12**.

### 5.4 Finding O-M5 (MAJOR): §6's closing inference about Deninger's intended reading is false — counterexample

The note's §6 closes:

> "*What Lemma B does NOT close:* … Deninger's own asserted translation (p. 29) cannot live here in nonempty form as a threshold condition, so his intended reading is presumably the transport reading of §4 (D3), consistent with his 'not N-invariant' verdict on it. [Judgment-grade reading, flagged.]"

This inference is unsound, and I can refute it outright. Deninger's sentence (p. 29, read verbatim this session) is: "This can be rephrased in terms of absolute values and translated to the case where C is the complex number field. **However the resulting class E is not N-invariant.**" The note's reasoning is: the threshold class is empty, an empty class would be trivially N-invariant, so Deninger cannot mean the threshold class. **The premise "empty" is false at the level of the whole class.** Lemma B shows emptiness only on the char-p locus. The class

  E_ε := {χ : κ(x)^× → ℂ^× : the extension by zero has |χ(r+s) − χ(r) − χ(s)| ≤ ε for all r,s ∈ κ(x)}

is **non-empty**: at the generic point of X = Spec Z̄ we have κ(x) = Q̄, and any field embedding τ : Q̄ ↪ ℂ has defect **0**, so τ|_{Q̄^×} ∈ E_ε for every ε > 0; and τ satisfies (Tors) (ker τ|_{μ} = 1, |1| = 1 ∈ N₀). And E_ε is **not N-invariant**: F_2(τ)(r) = τ(r)², whose defect is τ(r+s)² − τ(r)² − τ(s)² = 2τ(r)τ(s), which is unbounded on Q̄ × Q̄; so τ ∈ E_ε while F_2(τ) ∉ E_ε, violating Def. 4.1's biconditional (p. 27).

So the threshold reading produces exactly the object Deninger describes: a class obtained by rephrasing the p-adic condition "in terms of absolute values" and translating to ℂ, which is non-empty and **not N-invariant**. The note's inference to the contrary must go. This is a MAJOR finding **against a paragraph, not against Lemma B**, and correcting it *strengthens* D2: the literal, absolute-value reading is available, it is the one Deninger's sentence describes, it fails his own admissibility axiom for the reason he states, **and — this is the note's own new content — it is additionally empty on the entire periodic locus, so it cannot even serve as a non-admissible cut**. Replacement text in §10.

### 5.5 Break attempts on Lemma B (all failed)

(a) *Rescale the defect.* Any normalization by |P(r)|, |P(s)| is inert at char-p points because those moduli are 1. (b) *Restrict the pairs (r,s).* The local condition quantifies over all r,s ∈ Ô_{{x},y} (Def. 14.5, p. 94), and (1,1) is in every such domain; a condition that excludes (1,1) is not a translation of Deninger's. (c) *Move the condition to the local rings O_{X,x} rather than the residue field.* This is a genuinely different object — over ℂ the coefficient ring is a field, m = 0, so Def. 14.1's whole reduction-and-tilting architecture (the k-row of the p. 90 diagram) degenerates and there is no "mod p" to be additive modulo. It is therefore not a selection over the existing C-valued system, which is the note's charter question ("as a selection-of-points condition over the existing C-valued global system"). I record it as an unexplored *different* construction, not a gap in Lemma B. (d) *Take ε ≥ 1.* Then the (1,1) test is passable, but the local principle's own range is 0 < α < 1 (Defs. 14.5/14.12, p. 94, p. 99), and Prop. 14.7's threshold-independence is exactly the statement that all admissible thresholds collapse to |p|; an ε ≥ 1 archimedean condition has no local counterpart and no self-improvement (§5.2). Not a break.

**Lemma B: PASS.** The statement, its scope and its supporting mechanism-death observation all check. One MAJOR against the interpretive paragraph that follows it, one MINOR of scope.

---

## 6. LEMMA C — surjectivity of Aut(C) → Aut(μ(C)), step by step

> **Lemma C (note, §5).** The restriction map Aut(C) → Aut(μ(C)) = Ẑ^× is surjective for C the complex numbers (or any algebraically closed field of characteristic 0 containing Q̄ with infinite transcendence degree). *Derivation:* u ∈ Ẑ^× defines an automorphism of Q(μ_∞) (cyclotomic theory); extend to Q̄ (isomorphism extension), then to C along a transcendence basis of C over Q̄ and to the algebraic closure C of the lifted subfield (Steinitz; uses AC).

**Referee's re-derivation, one extension step at a time.**

*(0) The target group.* C = ℂ has characteristic 0 and is algebraically closed, so μ(ℂ) = ∪_n μ_n ≅ Q/Z, and Aut(Q/Z) ≅ Ẑ^× acting by ζ ↦ ζ^u. (Standard; the identification is the same one Deninger uses when he writes Aut(κ(x)^×) = Ẑ^×_{(p)} for κ(x)^× ≅ ⊕_{ℓ≠p}Q_ℓ/Z_ℓ, [x-03] p. 32.) ✓

*(1) Cyclotomic step.* The cyclotomic character Gal(Q(μ_∞)/Q) → Ẑ^× is an isomorphism, and the element with character u acts on μ_∞ by ζ ↦ ζ^u. So every u ∈ Ẑ^× is realized by some σ₀ ∈ Aut(Q(μ_∞)/Q). ✓ (This is the one classical input; **[RU]** — no algebraic-number-theory source is on disk. It is not program-specific and I flag it rather than lean on it.)

*(2) To Q̄.* Q̄ is an algebraic closure of Q(μ_∞); by the isomorphism extension theorem (Zorn), σ₀ extends to σ₁ ∈ Aut(Q̄), and σ₁|_{μ(ℂ)} = σ₀|_{μ_∞} = ( )^u since μ(ℂ) = μ(Q̄). ✓

*(3) Along a transcendence basis.* Let B be a transcendence basis of ℂ over Q̄ (exists by Zorn). Q̄(B) is purely transcendental over Q̄, so σ₁ extends to σ₂ ∈ Aut(Q̄(B)) by acting on coefficients and fixing B pointwise. ✓ (Any bijection of B would do; fixing B is the cheapest choice.)

*(4) To ℂ.* ℂ is algebraically closed and algebraic over Q̄(B) (B is a transcendence basis), hence ℂ is an algebraic closure of Q̄(B); isomorphism extension again gives σ ∈ Aut(ℂ) extending σ₂. ✓

*(5) Restriction.* σ|_{μ(ℂ)} = ( )^u by construction. Hence Aut(ℂ) → Aut(μ(ℂ)) = Ẑ^× is onto. ∎ ✓

**Use of choice.** Steps (2), (3), (4) each use Zorn's lemma; the note says so ("uses AC"). This is honest and correct. **Scope remark owed (MINOR O-m11):** the *force* of Proposition 1 comes entirely from wild (discontinuous) automorphisms, whose existence is a theorem of ZFC and not of ZF+DC; in models where every set of reals has the Baire property, Aut(ℂ) = {id, conjugation} and Proposition 1 says nothing. This does not weaken the note — Deninger's own construction is thoroughly choice-dependent (the splittings in Lemma 4.3, p. 28, and the choice of ι, p. 31) — but a referee-grade statement of D1 should say that it is a ZFC no-go.

**Findings.**
- **O-m4 (MINOR).** Lemma C delivers surjectivity onto Aut(μ(C)) = Ẑ^×, while Proposition 1 consumes surjectivity onto Aut(μ^{(p)}(C)) = Ẑ^×_{(p)}. The bridge is the projection Ẑ^× = ∏_ℓ Z_ℓ^× ↠ ∏_{ℓ≠p} Z_ℓ^× = Ẑ^×_{(p)}, which is onto. One clause, missing.
- **O-m5 (MINOR).** The parenthetical side condition "containing Q̄ with infinite transcendence degree" is unnecessary: steps (1)–(4) work for **any** algebraically closed field of characteristic 0 (transcendence degree 0 included, where step (3) is vacuous). Deleting the condition widens the lemma at no cost and matches Deninger's own generality ("Let C be an algebraically closed field which satisfies the conditions before Corollary 4.4", p. 31).

**Lemma C: PASS.**

---

## 7. LEMMA D — the Aut(C)-action: commutation, class stability, coordinates

Throughout, σ ∈ Aut(C) acts on X(C)• by post-composition: (x, P^×) ↦ (x, σ∘P^×). Note σ restricts to a group automorphism of C^×, so σ∘P^× is again a character. ✓

### 7.1 (i) Commutation — verified against the printed action formulas

The two actions are printed verbatim at [x-06] p. 11: "σ ∈ G acts on X(C)• via (x, P^×)^σ = (x^σ, P^×∘σ) and ν ∈ N acts G-equivariantly via F_ν(x, P^×) = (x, P^×∘( )^ν)."

- **With G.** σ_C∘(x, P^×)^g = σ_C(x^g, P^×∘g) = (x^g, σ_C∘P^×∘g) = (σ_C(x,P^×))^g. ✓ Post-composition commutes with pre-composition; this is the whole content.
- **With F_ν.** σ_C(F_ν(x,P^×)) = (x, σ_C∘P^×∘( )^ν) = F_ν(σ_C(x,P^×)). ✓
- **Descent to X̌.** X̌(C) = colim_N X(C)• along the (injective) F_ν; a map commuting with all F_ν descends to the colimit. So σ acts on X̌(C) and on X̌₀(C) = X̌(C)/G, and commutes with the Q^{>0}-action (generated by the F_ν and their formal inverses). ✓ **A point worth stating that the note omits:** no continuity of σ is needed here, because X̌(C) is defined as a colimit of *sets* under F_ν; the alternative description as continuous characters on lim_{N₀} κ(x)^× (Cor. 3.8, p. 26) is also preserved, since a character factoring through a projection to a discrete group is automatically continuous.
- **Descent to the suspension and commutation with the flow.** σ[P₀,u] := [σP₀,u] is well defined because σF_q = F_qσ, and φ^t[σP₀,u] = [σP₀,ue^t] = σ(φ^t[P₀,u]). The R^{>0}-coordinate is untouched, so σ preserves isotropy groups and hence orbit lengths. ✓ (The suspension and flow formulas are p. 38, quoted in §1.)

**(i): PASS.** No gap.

### 7.2 (ii) Class stability — checked one class at a time, including (Image) for E_max

The six classes are printed at [x-03] pp. 28–29 (quoted verbatim in §1). The key elementary fact: **ker(σ∘χ) = ker χ**, because σ|_{C^×} is injective. Therefore:

| Class | Defining condition (p. 28–29, verbatim) | σ-stability |
|---|---|---|
| E_tors | (Tors): ker(χ)_tors = ker(χ|_{μ(κ)}) finite and \|(ker χ)_tors\| ∈ N₀ | kernel unchanged ⇒ **stable** ✓ |
| E_max | (Tors) and (Image) | see below ⇒ **stable** ✓ |
| E_f | (Tors) and ker χ finite | kernel unchanged ⇒ **stable** ✓ |
| E_fg | (Tors) and ker χ finitely generated | kernel unchanged ⇒ **stable** ✓ |
| E_fd | (Tors) and ker χ ⊗ Q finite dimensional | kernel unchanged ⇒ **stable** ✓ |
| E_fd0 | (Tors) and (ker χ\|_{κ(x₀)^×}) ⊗ Q finite dimensional, x₀ = π(x) | ker χ ∩ κ(x₀)^× unchanged and x is unchanged ⇒ **stable** ✓ |

**(Image), the flagged press point, in full.** Verbatim (p. 27): "(Image) Only if char κ > 0. If χ(κ^×) is torsion, then κ^× is torsion as well, i.e. κ^× ⊗ Q ≠ 0 implies χ(κ^×) ⊗ Q ≠ 0."

*Route 1 (the note's).* σ|_{C^×} : C^× → C^× is a group isomorphism, so it carries χ(κ^×) isomorphically onto (σ∘χ)(κ^×). Being torsion is an isomorphism invariant, and −⊗Q is a functor, so χ(κ^×) ⊗ Q ≠ 0 ⟺ (σ∘χ)(κ^×) ⊗ Q ≠ 0. The hypothesis "κ^× ⊗ Q ≠ 0" does not involve χ at all. Hence (Image) transfers. ✓ **The note's justification is correct.**

*Route 2 (referee's, strictly stronger — finding O-m6, MINOR, a strengthening not an error).* χ(κ^×) ≅ κ^×/ker χ, so (Image) is a condition on the pair (κ, ker χ) alone; likewise every other row of the table. Hence **all six named classes are determined by the kernel** (given κ), and are therefore stable under post-composition by *any injective endomorphism* of C^×, not merely by Aut(C). This is worth putting in the note: it makes Lemma D(ii) a one-line observation, it makes the note's §5 aside "every certified (kernel-defined, hence Aut(C)-stable) class must carry full packets" a theorem rather than an aside, and it removes the need for the "preserving torsion and ⊗Q-dimension" clause, which is correct but does more work than necessary.

*The remaining clause.* The note adds "Def. 4.1's operations are pre-compositions, which commute with σ". Correct and needed for a different purpose: it says that if E is admissible then σ(E) is admissible; combined with the table (σ(E) = E for the named classes) it says the σ-action restricts to X̌₀(C)_E for each named E. Checked: (σ∘χ)∘τ = σ∘(χ∘τ) for τ ∈ Aut κ, and (σ∘χ)∘( )^ν = σ∘(χ∘( )^ν). ✓

**(ii): PASS.** No error; one strengthening offered.

### 7.3 (iii) The coordinate formula (a,ν) ↦ (u_σ a, ν)

*Referee's re-derivation.* χ_x = ι∘i_x^{−1} takes values in μ(C) (p. 31–32: i_x : μ^{(p)}(K) ≅ κ(x)^×, ι : μ(K) ↪ μ(C)). σ acts on μ(C) ≅ Q/Z as some u ∈ Ẑ^× (§6 step (0)); write u_σ ∈ Ẑ^×_{(p)} for its image under Ẑ^× ↠ Ẑ^×_{(p)}. For r ∈ κ(x)^×, χ_x(r) is a prime-to-p root of unity, so σ(χ_x(r)) = χ_x(r)^{u_σ}. Hence σ∘χ_x = ( )^{u_σ}∘χ_x. Finally, for a group homomorphism f between prime-to-p torsion abelian groups and w ∈ Ẑ^×_{(p)}, f(y^w) = f(y)^w (evaluate w in Z/d where d = ord(y); f(y) has order dividing d), so ( )^{u_σ}∘χ_x = χ_x∘( )^{u_σ}. Therefore
  σ∘(χ_x∘( )^a∘( )^ν) = (σ∘χ_x)∘( )^a∘( )^ν = χ_x∘( )^{u_σ a}∘( )^ν,
i.e. σ carries the point with (35)-coordinates (a,ν) to the point with coordinates (u_σ a, ν). ✓ Since the base class is a mod p^Ẑ (§2 (S3)), σ moves base classes by translation: **β(σz) = u_σ·β(z) in B_p**. ✓ And by §7.1, σ preserves orbit length; by §2 (S3) it maps the packet Γ_{(p)} into itself (it fixes x and hence the fibre of pr_{X₀}). ✓ ∎

**Findings.**
- **O-m7 (MINOR).** The note's justification invokes "χ_x is an isomorphism onto μ^{(p)}(C) (injective character between groups ≅ ⊕_{ℓ≠p}Q_ℓ/Z_ℓ, divisible-image argument as in Lemma A)". The divisible-image argument is *true* (ι : μ(K) → μ(C) is an injection between two copies of Q/Z, hence onto, so χ_x is onto μ^{(p)}(C)) but it is **not needed**: σ acts as ( )^u on all of μ(C), hence on any subgroup, so the formula holds whether or not χ_x is surjective. Simplify.
- **Corroboration found in the sources (not a finding, worth recording).** Lemma D(iii)'s mechanism is visible in print: [x-06] p. 13, "fix an injective homomorphism ι : μ(F) = μ(F̄) ↪ C^× … One can show that the connected components of W_rat(spec F)(C) are parametrized by the embeddings μ(F) ↪ C^×". Aut(C) permutes those embeddings simply transitively through Ẑ^×; that is the same torsor Lemma D(iii) computes on the packet base. And [x-03] p. 33 records the dependence: "The maps (37), (38) and the fibration map depend on our choices of x and ι."

**Lemma D: PASS** (i), (ii), (iii).

---

## 8. PROPOSITION 1 and its Corollary

### 8.1 The proposition, re-derived

> **Proposition 1 (note, §5).** Let E be any Aut(C)-stable class and let S ⊆ X₀^E be Aut(C)-stable and flow-invariant. If S contains one periodic point over the prime p, then for EVERY base class [c] ∈ B_p, S contains a closed orbit of length log p with base class [c]. In particular S contains uncountably many closed orbits over p, and no Aut(C)-stable selection achieves one orbit per prime.

*Referee's proof, from the anchors.* Let z ∈ S be periodic over p. By Theorem 6.1 (p. 39) — "{x₀ ∈ X₀ | (R^{>0})_{x₀} ≠ 1} = ∐_{x₀} Γ^E_{x₀}", isotropy N x₀^Z — z lies in Γ^E_{(p)} and its orbit γ = φ^R(z) is a circle of length log p. Let [a] = β(z) ∈ B_p be its base class (§2 (S3); constant along γ because the flow acts trivially on the base). Given a target [c] ∈ B_p, choose a representative c ∈ Ẑ^×_{(p)} and put u := c·a^{−1} ∈ Ẑ^×_{(p)} (legitimate: a is a unit). By Lemma C plus the surjection Ẑ^× ↠ Ẑ^×_{(p)} (finding O-m4), pick σ ∈ Aut(C) with u_σ = u. By Lemma D(i), σ commutes with the flow, so σ(γ) is again a flow orbit; it has the same period log p because σ preserves the R^{>0}-coordinate and hence the isotropy group; by Lemma D(iii) its base class is u·[a] = [c]. By Aut(C)-stability of S (and of E, so that the ambient X₀^E is σ-stable), σ(γ) ⊆ S. So S meets every base class. Distinct base classes give **distinct orbits** because, verbatim at [x-03] p. 38, "Γ_{x₀} fibres over Ẑ^×_{(p)}/p^Ẑ … with fibres the R^{>0}-orbits in Γ_{x₀}" — i.e. β is constant on orbits and separates them. Hence S contains at least |B_p| distinct closed orbits over p. ∎ ✓

*Uncountability of B_p, re-derived independently (not taken from the adjudication).* Let T be the set of odd primes ℓ ≠ p (infinite). Reduction gives a continuous surjection
  Ẑ^×_{(p)} = ∏_{ℓ≠p} Z_ℓ^× ↠ ∏_{ℓ∈T} (Z/ℓ)^× ↠ ∏_{ℓ∈T} (Z/ℓ)^×/((Z/ℓ)^×)² ≅ ∏_{ℓ∈T} C₂ =: V,
a compact group of cardinality 2^{ℵ₀}. The image of the closed subgroup p^Ẑ (the closure of {p^n : n ∈ Z}) is the closure of {n·g : n ∈ Z} where g is the image of p; since V has exponent 2 this set is {0,g}, already closed. Hence B_p = Ẑ^×_{(p)}/p^Ẑ surjects onto V/{0,g}, of cardinality 2^{ℵ₀}. So **B_p is uncountable**, indeed of the cardinality of the continuum. ∎ ✓ (Deninger records B_p's compactness and the identification Ẑ^×_{(p)}/p^Ẑ = Aut(F̄_p^×)/Aut(F̄_p) at pp. 2, 33, 38; the cardinality computation is mine.)

*The "in particular".* If S is Aut(C)-stable and flow-invariant then, over each prime p, S contains either 0 or uncountably many periodic orbits. Either way it never contains exactly one. ✓ So the headline is right.

**Proposition 1: PASS.** Findings: O-m3 (below) and O-m4 (above), both MINOR.

- **O-m3 (MINOR).** The note anchors "distinct base classes lie on distinct orbits" to p. 33 ("the fibres are the Q₀^{>0}-orbits in C_{x₀}"). That anchor is correct but is a statement about C_{x₀} ⊂ X̌₀(C); Proposition 1 needs it in the **suspension**, and the extra step (two points of Γ_{x₀} lie on one flow orbit iff their X̌₀-components lie in one Q^{>0}-orbit, immediate from [P₀,u] = [F_q(P₀), q^{−1}u]) is not written down. The cheaper fix is to cite **p. 38** instead, where Deninger states exactly the suspension-level fact: "Γ_{x₀} fibres over Ẑ^×_{(p)}/p^Ẑ … with fibres the R^{>0}-orbits in Γ_{x₀}." Both anchors were read verbatim this session and both say what the note says they say; **no misquotation was found.**

### 8.2 Break attempt on Proposition 1 (failed)

(a) *Deny surjectivity onto B_p.* Would need Aut(ℂ) → Ẑ^×_{(p)} not onto; refuted in §6. (b) *Deny that σ maps the packet to itself.* σ fixes x and commutes with G and Q^{>0}, so it preserves pr_{X₀}-fibres; refuted. (c) *Exploit non-continuity of σ.* Proposition 1 makes no topological claim: "closed orbit" here is "periodic orbit", i.e. an orbit with non-trivial isotropy (Theorem 6.1's sense), and the whole argument is set-theoretic. I checked specifically that no step needs σ to be a homeomorphism. Not a break — but see §8.3, where non-continuity *is* the crack in the Corollary. (d) *Find an Aut(C)-stable E with a one-orbit packet locus.* By probe A's Theorem C(b) the one-orbit cuts are the classes E(a₀); the note's own scope note (c) observes σ(χ^{a₀}) = χ^{u a₀} ∉ E(a₀) for u ∉ p^Ẑ, so those are not Aut(C)-stable. Consistent, not a break.

### 8.3 Finding O-M4 (MAJOR): the Corollary's definability schema over-reaches

> **Corollary (note, §5).** "…any global selection with the analogous naturality — in particular, any selection defined uniformly from the abstract field C and the scheme data, since Deninger's construction takes an abstract algebraically closed C as input ([x-03] §5, 'Let C be an algebraically closed field which satisfies the conditions…') and transport of structure then makes every uniformly-defined locus Aut(C)-stable — retains the full packet."

The clause "Deninger's construction takes an abstract algebraically closed C as input" is **true only up to §7 of [x-03] and false thereafter**, and the whole certified theory lives thereafter. Verbatim, p. 40: "**In this section, C is an algebraically closed field with a valuation | | and the corresponding topology.** … we give X(C)• the topology of pointwise convergence." From §7 on, the input datum is the *valued* field (C, | |), and a wild σ ∈ Aut(ℂ) does not preserve | |; the Aut(C)-action on X₀ is by bijections, not homeomorphisms. Consequently there exist **canonical, uniformly defined, and manifestly natural loci that are not Aut(C)-stable** — for instance Deninger's own unitary system, the subspace of pairs (x,P^×) with P^× : κ(x)^× → S¹ ([x-06] p. 12: "The closure is the subsystem obtained by replacing X(C)•_E … with the subspace of pairs (x,P^×) with P^× : κ(x)^× → S¹ a unitary character"). That locus is defined from ℂ-with-its-absolute-value, is canonical by anyone's standard, and is not preserved by wild automorphisms. Second, the construction also carries the auxiliary data x and ι, and Deninger flags their role explicitly (p. 33: "The maps (37), (38) and the fibration map depend on our choices of x and ι"); a locus defined using ι — which is exactly the note's own D3 transport — is likewise not Aut(C)-stable.

The note *does* say both things, but in the following paragraph (scope notes (a), (b), (c)) rather than in the statement. That is the wrong place: as written, the Corollary asserts a no-go whose stated hypothesis ("defined uniformly from the abstract field C and the scheme data") is met, on a natural reading, by loci the proposition demonstrably does not cover. A referee-grade statement must carry its exemptions. **Severity MAJOR** (the note must change; the mathematics is untouched). Replacement text in §10.

**A remark that partly rescues the intent, and is worth adding.** The unitary escape does not in fact cut packets: at a char-p point κ(x)^× is torsion, so *every* character is unitary, and X̌₀(S¹) contains every packet in full. So the most obvious topologically-defined canonical selection fails to cut for an independent, trivial reason. That observation belongs next to the Corollary, because it converts an apparent hole into a confirmed instance.

---

## 9. §4 Consequence 2 (branch D3) and §7 Road 2's Haar count

### 9.1 The transport computation, re-derived in full

The note asserts: "To impose it on the global C-valued characters one must first transport values: choose an isomorphism j : μ^{(p)}(C) → μ^{(p)}(C_p) … For each j, the class {χ_x·(a,ν) : j∘(that character) is mod-p additive} cuts the packet to the single base class determined by j; varying j over its torsor sweeps every base class."

*Referee's derivation.* Fix p, x over (p), κ(x) ≅ F̄_p, and let o = O_{C_p} with residue field k = F̄_p. Let j : μ^{(p)}(ℂ) → μ^{(p)}(C_p) be a group isomorphism (both sides ≅ ⊕_{ℓ≠p}Q_ℓ/Z_ℓ, so such j exist, and they form a torsor under Aut(⊕_{ℓ≠p}Q_ℓ/Z_ℓ) = Ẑ^×_{(p)}). Let χ = χ_x·(a,ν) be a packet character; its values lie in μ^{(p)}(ℂ), so j∘χ : κ(x)^× → μ^{(p)}(o) ⊂ o is defined, and its extension by zero is multiplicative with the right normalizations. By **Lemma A′**, j∘χ has additivity defect ≤ |p| iff j∘χ = [·]∘τ for a field embedding τ : F̄_p ↪ k = F̄_p, i.e. iff j∘χ = [·]∘Frob^t for some t ∈ Ẑ (Hom_ring(F̄_p, F̄_p) = Aut(F̄_p) = Ẑ, generated topologically by Frobenius).

Now [·] : F̄_p^× → μ^{(p)}(o) is a group isomorphism (Step 0 of §3.4), and χ_x : F̄_p^× → μ^{(p)}(ℂ) is a group isomorphism (ι is an injection Q/Z → Q/Z hence onto, and i_x is (32)). So a_j := χ_x^{−1}∘j^{−1}∘[·] ∈ Aut(F̄_p^×) = Ẑ^×_{(p)} is well defined, and

  j∘χ = [·]∘Frob^t  ⟺  χ = j^{−1}∘[·]∘Frob^t = χ_x∘( )^{a_j}∘( )^{p^t} = χ_x∘( )^{a_j p^t},

using that Frob^t acts on F̄_p^× as ( )^{p^t}, t ∈ Ẑ. In (35)-coordinates this is the set {(a_j p^t, 1) : t ∈ Ẑ}, i.e. **exactly one base class [a_j] ∈ B_p**, and (by (35)'s fibre relation (a,ν) ~ (p^n a, p^n ν)) exactly one Q^{>0}-orbit in C_{(p)}, hence exactly one flow orbit in Γ_{(p)}. Varying j over its Ẑ^×_{(p)}-torsor multiplies a_j by an arbitrary unit, so every base class is attained. ∎ ✓

**So the substance of D3 checks out, and it is a clean corollary of Lemma A′.** In particular the note's slogan "in packet coordinates the local principle selects exactly the Teichmüller base class" (§0, D3) is correct.

### 9.2 Finding O-M2 (MAJOR): "not admissible … and it is not N-invariant" contradicts the identification with E(a₀)

The note's sentence:

> "So the faithful transport of the local principle **is** the adjudicated Theorem-C cut E(a₀), with j in place of a₀: it exists, it is one arbitrary point of a Cantor torsor per prime, it is not admissible-with-theory (forfeits every certified theorem), and it is not N-invariant — precisely [x-03]'s p. 29 Remark."

Two different objects are conflated, and the composite sentence is self-contradictory against the binding adjudication.

- **Object (α), the raw transported condition** T_j := {χ : j∘χ has defect ≤ |p|} = {χ_x∘( )^{a_j p^t} : t ∈ Ẑ}. This is **not** admissible: by §4.3(b), F_ℓ(T_j) ⊄ T_j for ℓ ≠ p (indeed χ_x∘( )^{a_j p^t ℓ} = χ_x·(a_j p^t, ℓ) has kernel μ_ℓ ≠ 1 and is not of the displayed shape), so Def. 4.1's biconditional fails. So (α) **is not N-invariant** — matching Deninger's p. 29 remark.
- **Object (β), the admissible class E(a₀)** of probe A's Theorem C(b), banked in adjudication §4 item 5(b): "One-orbit-per-prime **admissible** cuts exist". Admissible means, by Def. 4.1 (p. 27, verbatim), closed under Aut κ and under ν-powers **in both directions**. So E(a₀) **is** N-invariant, by construction. Its packet locus is one Q^{>0}-orbit because the reachable exponents are a₀·p^Ẑ, i.e. one base class (adjudication §4 item 5b; consumed, not re-derived here — flagged).

The note's sentence therefore asserts of one object ("is the adjudicated Theorem-C cut E(a₀)") a property of the other ("it is not N-invariant"). This matters beyond bookkeeping: the note's §0 bullet D3 and its §9 design constraint both lean on "the transport reading collapses to the known non-canonical cut", and a reader who takes the collapse literally would conclude that the adjudicated one-orbit cuts are not N-invariant, contradicting the banked Theorem C(b) and re-opening a question the adjudication closed. **Severity MAJOR.** The fix is to separate the two objects; both facts survive and the trichotomy is unchanged. Replacement text in §10.

*Consistency check performed.* The admissible closure of T_j is exactly E(a_j): admissibility forces adjoining χ_x∘( )^{a_j p^t}∘( )^ν for all ν and all pre-compositions by Aut κ(x) = p^Ẑ, and the reachability computation (adjudication §4 item 5b) says nothing further is reachable; the base class is unchanged by ν-powers because the base class is the a-coordinate mod p^Ẑ (§2 (S3)). So "the faithful transport, closed up under admissibility, is E(a_j)" is the true statement. ✓

### 9.3 §7 Road 2 — the Haar formal count

> "the packet's aggregate orbit contribution is ∫_{B_p}(single-orbit term) dHaar = the single-orbit term, since the integrand is constant (all orbits in Γ_p have length log p — [x-06] Thm 4.2)."

**Verification of the cited fact.** [x-06] Thm 4.2 and the sentence after it, p. 11–12, read verbatim this session: "{x₀ ∈ X₀^E | φ^t(x₀) = x₀ for some t > 0} = ∐_{x₀} Γ_{x₀}. … The compact subsets Γ_{x₀} ⊂ X₀ consist of periodic orbits of length log N x₀ where N x₀ = |κ(x₀)| … In fact Γ_{x₀} is a fibre space over the compact group Aut(F̄_p^×)/Aut(F̄_p) … with fibres the compact orbits in Γ_{x₀}." **The citation is exact**: for X₀ = Spec Z all orbits in Γ_{(p)} have length log p. ✓ (Same fact at [x-03] p. 38: "all R^{>0}-orbits in Γ_{x₀} are circles R^{>0}/N x₀^Z".)

**Verification of the flow-invariance and equivariance claims.** The flow acts trivially on B_p (§2 (S3), from p. 38), so any measure pulled back from B_p is flow-invariant. ✓ Aut(C) acts on B_p by translations (Lemma D(iii)), and Haar measure on a compact group is translation-invariant, so the normalized Haar measure is Aut(C)-equivariant. ✓ Both correct.

**Finding O-M6 (MAJOR): the constancy of the integrand is not established.** "The integrand is constant" is inferred solely from "all orbits have length log p". That entitles one to constancy only if the single-orbit term is a function of the length alone. In every trace/Lefschetz formula of the type this program targets, the orbit term also carries transverse data — a holonomy or Poincaré-return factor, a Fuller-type index, or a multiplicity — and constancy of that datum across a packet is precisely what is *not* known here, since the packet's subspace topology is non-Hausdorff (adjudication §4 item 3, banked) and the Aut(C)-symmetry that permutes the orbits is not continuous (§8.3), so it transports no transverse structure. The honest statement is: *for a length-only orbit weight the Haar average reproduces the single-orbit weight, hence the T1 coefficient 1; for any weight depending on transverse data, constancy across the packet is an additional hypothesis, unverified.* Note that the note's own DQ-M (§8 item 2) poses exactly this as the open question, so the substance is not in dispute — but §7's "at the formal level the T1 count then comes out right" and §10's listing of "the Haar formal count (§7)" under "fully derived here" both overstate it. **Severity MAJOR** (the note must change; one sentence). Replacement text in §10.

**Finding O-m10 (MINOR, a strengthening): "canonical" is better justified via a torsor.** The note says "the Haar measure on B_p is canonical". Deninger explicitly records that the identification of the packet with B_p × circle depends on choices: p. 33, "The maps (37), (38) and the fibration map depend on our choices of x and ι." What *is* canonical is the orbit space Γ_{(p)}/R^{>0}, which by p. 38 is a **B_p-torsor** (β is canonical up to the choice of base point; the B_p-action on it is not). A torsor under a compact group carries a unique invariant probability measure, obtained by transporting Haar along any trivialization and independent of the trivialization. That is the canonical object, and Aut(C) acts on it by torsor translations, so the equivariance claim survives verbatim. This upgrade removes the only place where "canonical" could have been challenged.

### 9.4 Break attempt on Road 2 (partial, recorded)

I looked for a canonical *non*-Haar invariant measure on the packet orbit space that would spoil uniqueness: on a compact group (or torsor) the invariant probability measure is unique, so within the equivariance requirement there is no competitor. ✓ (The published rival the novelty check records — [r3s-08] Thm 3.6(2), a canonical packet collapse — is a different device, not a competing measure, and I did not open [r3s-08], per §1.) I also checked that the Haar average does not accidentally repair the count for *non-*periodic structure: it does not, because it is supported on the periodic locus by construction and says nothing about the accumulation set that Q* (adjudication §5) is about. Road 2 remains what the note says it is: a proposal whose burden has moved to DQ-M.

---

## 10. REPAIRS — exact replacement text

**R-1 (for O-M1, note §4, Lemma A's hypothesis line).** Replace
> "Let o be as in §2 (residue field k algebraically closed of char p), κ an algebraically closed field of characteristic p, and P : κ → o multiplicative with P(0) = 0, P(1) = 1, whose restriction to κ^× is a group homomorphism into o (values automatically in μ^{(p)}(o), the prime-to-p roots of unity, since κ^× is prime-to-p torsion)."
by
> "Let o be a p-adically complete rank-one valuation ring with maximal ideal m, algebraically closed fraction field C of characteristic 0 and **algebraically closed** residue field k of characteristic p (the case used below is o = o_{C_p}, k = F̄_p; note that [x-03] §14, p. 89, assumes only that k has characteristic p, so the algebraic closedness of k and C is an extra hypothesis imposed here). Let **κ be an algebraic closure of F_p**, so that κ^× = μ^{(p)}(κ) is torsion of prime-to-p order — this is the only case used below (κ(x) ≅ F̄_p in the packet coordinates, [x-03] p. 31, and κ = o_K/m_K = F̄_p in Theorem 15.6's closed-point fibre, p. 113) — and let P : κ → o be multiplicative with P(0) = 0, P(1) = 1 and P|_{κ^×} a group homomorphism, whose values then lie automatically in μ^{(p)}(o). **(The torsion hypothesis on κ^× is not cosmetic: for an algebraically closed κ ⊋ F̄_p the group κ^× is not torsion, [·]∘τ is not even defined on all of κ^×, and the last step of the (⇒) direction below fails, since 1+m is divisible and Hom(κ^×, 1+m) ≠ 0.)**"

**R-2 (for O-M3, note §3, last paragraph).** Replace
> "The freshman's-dream asymmetry makes it precise: additivity mod p is ( )^p-stable (Prop. 14.7's computation) but not ( )^ℓ-stable for ℓ ≠ p, since (r+s)^ℓ ≢ r^ℓ + s^ℓ mod p."
by
> "Lemma A makes it precise. Write E_loc for the mod-p-additive multiplicative maps κ → o with κ = F̄_p; by Lemma A, E_loc = {[·]∘τ : τ ∈ Hom_ring(κ,k)}. (a) E_loc is F_p-stable in both directions: F_p([·]∘τ) = [·]∘(τ∘Frob) and τ ↦ τ∘Frob is a bijection of Hom_ring(κ,k) — the classified form of Prop. 14.7's F_p(Y̌_α) = Y̌_α (p. 94). (b) For a prime ℓ ≠ p, F_ℓ([·]∘τ) = [·]∘ψ with ψ = ( )^ℓ∘τ, and by Lemma A's uniqueness this lies in E_loc iff ψ is additive; it is not, since ( )^ℓ is only a group endomorphism of κ^×, not a ring endomorphism of κ. Explicit witness: p = 3, ℓ = 2, r = s = 1 give F_2(P)(1+1) − 2F_2(P)(1) = P(4̄) − 2 = 1 − 2 = −1, of absolute value 1 — a unit, the maximum possible defect. So E_loc satisfies the p^Z-half of Def. 4.1's biconditional and violates the ν-half for every ν divisible by a prime ℓ ≠ p. The real asymmetry is that ( )^p is a ring endomorphism of κ while ( )^ℓ is not, and mod-p additivity is exactly the condition that remembers the ring structure (Consequence 1 below)."

**R-3 (for O-M2, note §4, Consequence 2, the final sentence).** Replace
> "So the faithful transport of the local principle **is** the adjudicated Theorem-C cut E(a₀), with j in place of a₀: it exists, it is one arbitrary point of a Cantor torsor per prime, it is not admissible-with-theory (forfeits every certified theorem), and it is not N-invariant — precisely [x-03]'s p. 29 Remark."
by
> "Two distinct objects must be kept apart. **(α)** The raw transported condition T_j = {χ : j∘χ is mod-p additive} = {χ_x∘( )^{a_j p^t} : t ∈ Ẑ} is **not admissible**: it fails Def. 4.1's ν-biconditional for every prime ℓ ≠ p (the argument of §3), which is precisely [x-03] p. 29's 'the resulting class E is not N-invariant'. **(β)** Its admissible closure is the adjudicated Theorem-C cut E(a_j): admissible by construction, hence N-invariant, cutting the packet to the single base class [a_j] because ν-powers do not move the base class. So the faithful transport, once made admissible, **is** E(a_j) — one arbitrary point of a Cantor torsor per prime, non-canonical, and theory-forfeiting (it fails E ⊇ E_f, so [x-03] Thm 5.2's full-packet regime and every theorem that consumes it are lost; adjudication §4 item 5). Nothing new is gained; the known dead end is re-derived from the local principle itself."

**R-4 (for O-M4, note §5, the Corollary).** Replace the parenthetical
> "— in particular, any selection defined uniformly from the abstract field C and the scheme data, since Deninger's construction takes an abstract algebraically closed C as input ([x-03] §5, 'Let C be an algebraically closed field which satisfies the conditions…') and transport of structure then makes every uniformly-defined locus Aut(C)-stable —"
by
> "— in particular, any selection defined uniformly from **the abstract field C alone** and the scheme data, using neither the valuation/topology of C nor the auxiliary choices (x, ι). Deninger's *set-level* construction does take an abstract algebraically closed C as input ([x-03] §5, p. 31, 'Let C be an algebraically closed field which satisfies the conditions…'), so transport of structure makes every such locus Aut(C)-stable; but two named exemptions are real and must be stated with the corollary rather than after it. **(i) The topology is not abstract:** from §7 on, '[i]n this section, C is an algebraically closed field with a valuation | | and the corresponding topology' (p. 40), and a wild σ ∈ Aut(ℂ) does not preserve | |, so Aut(C) acts on X₀ by bijections and not by homeomorphisms; a canonical topologically-defined locus such as Deninger's own unitary system X̌₀(S¹) ([x-06] p. 12) is *not* Aut(C)-stable, and Proposition 1 does not constrain it. (For that particular locus the conclusion holds anyway and for a trivial reason: at a char-p point κ(x)^× is torsion, so every character is unitary and the unitary system contains every packet in full.) **(ii) The choices are not abstract:** '[t]he maps (37), (38) and the fibration map depend on our choices of x and ι' (p. 33), and a locus defined through ι — which is exactly the transport reading D3 — is not Aut(C)-stable either. Within those two exemptions, any uniformly-defined selection —"

**R-5 (for O-M5, note §6, final paragraph).** Replace
> "…and Deninger's own asserted translation (p. 29) cannot live here in nonempty form as a threshold condition, so his intended reading is presumably the transport reading of §4 (D3), consistent with his 'not N-invariant' verdict on it. [Judgment-grade reading, flagged.]"
by
> "Deninger's p. 29 sentence is fully consistent with the threshold reading, and no inference to the transport reading is available. The class E_ε = {χ : the extension by zero has archimedean defect ≤ ε} is **non-empty** — at the char-0 points of X = Spec Z̄ the residue field is Q̄ and every field embedding τ : Q̄ ↪ ℂ has defect 0 and satisfies (Tors) — and it is **not N-invariant**, since F_2(τ)'s defect τ(r+s)² − τ(r)² − τ(s)² = 2τ(r)τ(s) is unbounded, so τ ∈ E_ε while F_2(τ) ∉ E_ε, violating Def. 4.1's biconditional (p. 27). That is exactly the object Deninger describes: obtained by rephrasing in terms of absolute values, translated to C, and not N-invariant. Lemma B's new content is therefore not that the translated class is empty — it is not — but that **it is empty precisely on the periodic locus**, so it cannot serve even as a non-admissible cut; and Deninger's §14 Remark (p. 99) — 'I do not know how to transport such conditions to the points of X̌(C)' — records that he claims no working transport either way."

**R-6 (for O-M6, note §7 Road 2, the count sentence; and §10's standing-order-5 record).** Replace
> "At the formal level the T1 count then comes out right: the packet's aggregate orbit contribution is ∫_{B_p}(single-orbit term) dHaar = the single-orbit term, since the integrand is constant (all orbits in Γ_p have length log p — [x-06] Thm 4.2)."
by
> "At the formal level the T1 **coefficient** then comes out right for a length-only orbit weight: all orbits in Γ_p have length log p ([x-06] Thm 4.2, p. 11–12, verbatim: 'The compact subsets Γ_{x₀} ⊂ X₀ consist of periodic orbits of length log N x₀'; same at [x-03] p. 38), and the invariant probability measure on the packet's orbit space — canonically a B_p-torsor, [x-03] p. 38 — integrates a constant to itself, giving aggregate weight 1 per prime. **This does not yet give the trace-formula count.** Any orbit weight that depends on transverse data (a holonomy or Poincaré-return factor, a Fuller index, a multiplicity) need not be constant across the packet, and constancy cannot be inferred from the Aut(C)-symmetry, which is discontinuous and transports no transverse structure; nor from the packet's product coordinates, whose subspace topology is not (profinite) × (circle) (adjudication §4 item 3). Constancy of the transverse weight is therefore an additional, unverified hypothesis, and it is part of DQ-M."
and in §10's standing-order-5 record replace "the Haar formal count (§7)" by "the Haar coefficient count for a length-only orbit weight (§7), with the transverse-weight constancy flagged open".

**Minor repairs (one line each).**
- **O-m1.** §2 (Stage 2) and §6: "([x-03] intro p. 5)" for the quotation "…this process does not give more points" → **p. 6**. (Both occurrences. The "necessary to obtain something interesting" quotation is correctly cited to p. 6.)
- **O-m2 (rendering).** §4: "B_p := Ẑ^×₍p₎/p^Ẑ = Aut(F̄_p)^×/Aut(F_p)^" → "B_p := Ẑ^×_{(p)}/p^Ẑ = Aut(F̄_p^×)/Aut(F̄_p)" (Deninger's own display, verbatim at p. 2, p. 33, p. 38, and [x-06] p. 12). As printed in the note, "Aut(F_p)" is the trivial group.
- **O-m12 (Lemma B scope).** §6: "the class 'archimedean defect ≤ ε at char-p points' is empty on the periodic locus" → add "(for X₀ = Spec Z the periodic locus *is* the char-p locus, by Thm 6.1 p. 39 together with X̌₀(C)_{p,E} = C_{(p)}; for higher-dimensional X₀ read 'char-p points over a closed point with finite residue field')".
- **O-m3.** §5, Proposition 1's proof: cite **[x-03] p. 38** ("Γ_{x₀} fibres over Ẑ^×_{(p)}/p^Ẑ … with fibres the R^{>0}-orbits in Γ_{x₀}") in place of, or alongside, p. 33; p. 33's statement is about Q^{>0}-orbits in C_{x₀} and needs the extra (trivial) passage to the suspension.
- **O-m4.** §5, between Lemmas C and D, insert: "and Ẑ^× = ∏_ℓ Z_ℓ^× ↠ ∏_{ℓ≠p} Z_ℓ^× = Ẑ^×_{(p)} is onto, so every u ∈ Ẑ^×_{(p)} is u_σ for some σ ∈ Aut(C)."
- **O-m5.** §5, Lemma C: delete "with infinite transcendence degree" — the derivation works for any algebraically closed field of characteristic 0.
- **O-m6.** §5, Lemma D(ii): add "Indeed all six classes are determined by ker χ (given κ): (Image) is the condition κ^× ⊗ Q ≠ 0 ⇒ (κ^×/ker χ) ⊗ Q ≠ 0. Hence they are stable under post-composition with any injective endomorphism of C^×, a fortiori under Aut(C)."
- **O-m7.** §5, Lemma D(iii): the divisible-image argument may be deleted; σ acts as ( )^{u} on all of μ(C) and hence on the subgroup χ_x(κ(x)^×), surjectivity of χ_x being unnecessary.
- **O-m8 (fidelity).** §2's description of o adds hypotheses to [x-03] §14 (p. 89: "a p-adically complete rank one valuation ring with quotient field C, maximal ideal m and residue field k of characteristic p" — no algebraic closedness of k, no char-0 hypothesis on C); and §4's "Let o be as in §2 (residue field k algebraically closed of char p)" attributes to §2 a hypothesis §2 did not state. Make §2 say explicitly which hypotheses are Deninger's and which the note imposes for the o = o_{C_p} case.
- **O-m9.** §4, Lemma A: "for a unique field embedding τ : κ ↪ k" → add "(with image in the algebraic closure of F_p inside k, automatic once κ = F̄_p, which is what makes [·]∘τ defined)".
- **O-m10.** §7 Road 2: "the Haar measure on B_p is canonical" → "the packet's orbit space is canonically a B_p-torsor ([x-03] p. 38), and a torsor under a compact group carries a unique invariant probability measure; that measure is canonical even though the identification with B_p itself depends on the choices of x and ι (p. 33)".
- **O-m11 (scope).** §5: add after Lemma C, "Proposition 1 is a ZFC statement: its force comes from wild automorphisms, and in models of ZF+DC where all sets of reals have the Baire property Aut(ℂ) = {id, conjugation} and the proposition is vacuous. This is consistent with the surrounding theory, which is choice-dependent throughout ([x-03] Lemma 4.3's splittings, p. 28; the choice of ι, p. 31)."
- **Citation hygiene (folded into O-m1).** §2 (F2) cites "Prop. 14.7, p. 94, proof read" — the statement is on p. 94, the proof on p. 95.

---

## 11. VERDICT BLOCK

### 11.1 Verdict

**PASS-WITH-REPAIRS** on the assigned item (the 9.4 note's Lemmas A–D and Proposition 1, i.e. the transplant trichotomy D1–D3, together with §3's N-invariance argument and §7's Haar count).
**0 FATAL / 6 MAJOR / 12 MINOR.** No stated theorem of the note is false, and none has an unfillable gap. Every MAJOR is repaired above with replacement text; four of the six repairs (R-2, R-3, R-5, R-6) leave the note's conclusions **stronger and better anchored** than the original wording.

### 11.2 Findings, severity-tagged, with locations

| # | Sev. | Location in `probe-9.4-note.md` | Finding | Repair |
|---|---|---|---|---|
| O-M1 | MAJOR | §4, Lemma A statement | Hypothesis "κ algebraically closed of char p" is too general: the statement is ill-formed and the (⇒) proof's last step fails unless κ^× is torsion, i.e. κ = F̄_p. The parenthetical "values automatically in μ^{(p)}(o) … since κ^× is prime-to-p torsion" is false for κ ⊋ F̄_p. All applications use κ = F̄_p. | R-1 |
| O-M2 | MAJOR | §4, Consequence 2, final sentence | Conflates the raw transported condition T_j (not admissible, not N-invariant) with the adjudicated cut E(a₀) (admissible, hence N-invariant, adjudication §4 item 5b); as written it contradicts a banked result. | R-3 |
| O-M3 | MAJOR | §3, last paragraph; §10 record | The freshman's-dream non-N-invariance is asserted, not derived; the stated reason ("(r+s)^ℓ ≢ r^ℓ + s^ℓ mod p") is mis-stated (we are *in* char p) and does not imply the claim, since P is only mod-p additive. Full derivation supplied (§4.3), with explicit witness p = 3, ℓ = 2. | R-2 |
| O-M4 | MAJOR | §5, Corollary | The definability schema "uniformly defined ⇒ Aut(C)-stable" over-reaches: from [x-03] §7 on, C carries a valuation and topology (p. 40, verbatim), so canonical topologically-defined loci (e.g. Deninger's unitary system) are not Aut(C)-stable; likewise loci defined through ι (p. 33). The exemptions must be in the statement. | R-4 |
| O-M5 | MAJOR | §6, final paragraph | The inference "Deninger's p. 29 translation cannot live here in nonempty form, so his intended reading is presumably the transport reading" is **false**: the threshold class contains every field embedding at char-0 points (defect 0) and is not N-invariant (F_2 of an embedding has unbounded defect), which is exactly what he describes. | R-5 |
| O-M6 | MAJOR | §7 Road 2; §10 record | "the integrand is constant" is inferred from equal orbit lengths alone; a transverse-data-dependent orbit weight need not be constant across the packet, and the Aut(C)-symmetry is discontinuous so transports none. The count is established only for a length-only weight. | R-6 |
| O-m1 | MINOR | §2 Stage 2; §6 | "does not give more points" is on [x-03] **p. 6**, not p. 5 (two occurrences). Also: Prop. 14.7's statement p. 94, proof p. 95. | §10 |
| O-m2 | MINOR | §4 | "Aut(F̄_p)^×/Aut(F_p)^" garbles Deninger's "Aut(F̄_p^×)/Aut(F̄_p)" (pp. 2, 33, 38; [x-06] p. 12); as printed, Aut(F_p) is trivial. | §10 |
| O-m3 | MINOR | §5, Prop. 1's proof | Better anchor available: p. 38 states the fibration at the **suspension** level with fibres the R^{>0}-orbits; p. 33 is the C_{x₀}-level statement and needs an unwritten extra step. Both anchors verified verbatim; no misquotation. | §10 |
| O-m4 | MINOR | §5, between Lemmas C and D | Lemma C gives surjectivity onto Ẑ^×; Prop. 1 consumes surjectivity onto Ẑ^×_{(p)}. Insert the projection step. | §10 |
| O-m5 | MINOR | §5, Lemma C | "with infinite transcendence degree" is an unnecessary hypothesis. | §10 |
| O-m6 | MINOR | §5, Lemma D(ii) | Strengthening: all six named classes are kernel-determined, hence stable under any injective endomorphism of C^×. (Note's own route is correct.) | §10 |
| O-m7 | MINOR | §5, Lemma D(iii) | The divisible-image argument is not needed for the displayed formula. | §10 |
| O-m8 | MINOR | §2; §4 | §2 adds hypotheses to [x-03] §14 p. 89 (k algebraically closed; C char 0) and §4 attributes to §2 a hypothesis §2 did not state. | §10 |
| O-m9 | MINOR | §4, Lemma A | "τ : κ ↪ k" should record that the image must lie in the prime-to-p roots of unity together with 0, i.e. in F̄_p ⊆ k. | §10 |
| O-m10 | MINOR | §7 Road 2 | "canonical" is better carried by the torsor argument: Γ_{(p)}/R^{>0} is canonically a B_p-torsor (p. 38) with a unique invariant probability measure; the identification with B_p itself depends on x and ι (p. 33). | §10 |
| O-m11 | MINOR | §5, after Lemma C | Prop. 1 is a ZFC statement; its force comes from wild automorphisms. Should be said. | §10 |
| O-m12 | MINOR | §6, Lemma B | Scope: for X₀ = Spec Z the periodic locus equals the char-p locus; for higher-dimensional X₀ the phrase needs "over a closed point with finite residue field". | §10 |

### 11.3 What is now established at referee grade, and its precise scope

At referee grade — line-by-line re-derived here from page-anchored primary text, with every step written out above and every break attempt recorded — the following now stands. **(1) Lemma A′:** for o a p-adically complete rank-one valuation ring with algebraically closed characteristic-0 fraction field and algebraically closed residue field k of characteristic p, and for κ **an algebraic closure of F_p**, a multiplicative P : κ → o with P(0)=0, P(1)=1 has additivity defect ≤ |p| if and only if P = [·]∘τ for a unique field embedding τ : κ ↪ k; the converse half is the Witt identity V W(k) = VF W(k) = pW(k), and the forward half is sharp (no perturbation exists, because Hom(κ^×, 1+m) = 0 for κ^× prime-to-p torsion). This matches, and re-derives from the source side, Deninger's Y⋄_s = Hom(κ,k) ([x-03] p. 114). Scope: κ^× torsion is essential; the general algebraically closed κ is **not** decided here. **(2)** In consequence, the mod-p-additivity class E_loc is stable under ( )^p in both directions and violates Def. 4.1's biconditional for every ν divisible by a prime ℓ ≠ p, with an explicit unit-sized defect witness — Deninger's "not N-invariant" (p. 29), now proved rather than quoted, and the precise obstruction to coexistence with the full Q^{>0}-suspension. **(3) Lemma B:** for X₀ = Spec Z, at every point of the periodic locus (= the char-p locus) the archimedean additivity defect at r = s = 1 is ≥ 1 for every character in every class E ⊆ E_tors, with equality attainable; so the archimedean threshold condition selects the empty set there for every ε < 1, and the (172)-completion mechanism has no archimedean counterpart, indeed the defect *grows* under Frobenius over ℂ. Scope: the *global* threshold class is **not** empty (it contains every field embedding at char-0 points) and is not N-invariant, exactly matching [x-03] p. 29 — the note's contrary inference is withdrawn. **(4) Lemma C:** Aut(ℂ) ↠ Aut(μ(ℂ)) = Ẑ^× ↠ Ẑ^×_{(p)}, by cyclotomic theory plus three isomorphism-extension steps; a ZFC theorem, vacuous without choice. **(5) Lemma D:** post-composition by σ ∈ Aut(C) commutes with the G-action, with every F_ν, with the Q^{>0}-action and with the suspension flow, fixes the R-coordinate and hence orbit lengths; it preserves each of E_tors, E_max, E_f, E_fg, E_fd, E_fd0 — indeed each is determined by ker χ, so (Image) for E_max is preserved for a reason stronger than the note gives; and on the packet it is (a,ν) ↦ (u_σ a, ν), moving base classes by translation by u_σ ∈ Ẑ^×_{(p)}. **(6) Proposition 1:** consequently, for X₀ = Spec Z and any Aut(C)-stable class E, an Aut(C)-stable flow-invariant subset of X₀^E containing one periodic point over p contains one periodic orbit of length log p in **every** base class, hence continuum-many (B_p has cardinality 2^{ℵ₀}, re-derived here via ∏_{ℓ odd, ℓ≠p} C₂ modulo a two-element subgroup); so no Aut(C)-stable selection realizes the T1 count of one orbit per prime. **(7) D3:** the faithful value-transport of the local principle selects, for each choice of j : μ^{(p)}(ℂ) ≅ μ^{(p)}(C_p), exactly the base class [a_j] — one flow orbit per prime — and its admissible closure is the adjudicated Theorem-C cut E(a_j); varying j sweeps B_p.

**The precise scope of the trichotomy after this pass.** D1 is a no-go **for selections definable from the abstract field ℂ and the scheme data alone**, excluding both the valuation/topology of ℂ and the auxiliary choices (x, ι) — with the note's own D3 exhibiting the ι-escape and Deninger's unitary system exhibiting the topology-escape (which fails to cut for an unrelated, trivial reason). D2 is a no-go **for uniform archimedean thresholds on the char-p locus**, and says nothing about defect *profiles* (averaged, asymptotic, comparative), nor about constructions that impose the defect on local rings rather than residue fields — over ℂ the latter is a different object, since the coefficient field has no residue structure and Def. 14.1's diagram degenerates. D3 is a re-derivation of a known dead end from the local principle itself. Taken together the three branches close "transplant-as-a-selection-of-points over the existing ℂ-valued system", which is exactly the charter question, and leave untouched — as the note says — Roads 1–3 and the measured exit DQ-M. Nothing here fires or blocks the C3 kill-criterion; nothing here bears on Q* (adjudication §5), whose content is p → ∞ accumulation and not packet structure.

**Honest labels.** Everything above is either quoted verbatim from a page I opened this session (§1) or derived here in full. Two classical inputs are flagged **[RU]** and are not program-specific: the cyclotomic character's surjectivity onto Ẑ^× (§6 step 1) and the Witt-vector facts used in §3.4 Step 2 (first component additive; VF = FV = p over a perfect char-p ring; the universal map W(k) → o for p-adically complete o with perfect residue field). No dimension theory, no Morishita, no recalled literature is used anywhere in this report. One input is consumed from a banked program document without re-derivation and is flagged at each use: probe A's Theorem C(b) reachability computation (adjudication §4 item 5b), used only to name E(a₀) in §9.2.

---

## 12. Sources section — every page read this session

**[x-03]** `fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf` (printed page = PDF page, verified by footers): **pp. 2, 5, 6, 26, 27, 28, 29, 31, 32, 33, 34, 37, 38, 39, 40, 89, 90, 91, 94, 95, 99, 104, 113, 114, 116.**
**[x-06]** `fetched/x-06-deninger-2024-primes-knots-and-periodic-orbits.pdf`: **pp. 11, 12, 13.**
**[D25]** `fetched-r3/r3s-22-deninger-rational-witt-vectors-associated-sheaves-arxiv-2508.05329v1-SESSION8-FETCH.pdf`: **pp. 1–4** (introduction; §7 Road 1 quotation confirmed verbatim).
**Program-internal, read in full:** `results/c3-r/probe-9.3-adjudication.md`; `results/c3-r/probe-9.4-note.md`.
**Deliberately not opened for this item:** `fetched-r3/r3s-08-morishita-deninger-cc-bridge-2508.15971.pdf` (adjudication §4 item 4 and its third Session-14 bookkeeping paragraph forbid citing it for the packet identification or for topology; nothing in this item needs it).

— end of referee report O —
