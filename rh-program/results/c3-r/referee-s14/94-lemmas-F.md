# REFEREE REPORT F — probe 9.4 note, Lemmas A–D and Proposition 1 (the transplant trichotomy D1–D3)

**Program:** RH program, direction C3-r. **Date:** 2026-09-02 (Session 14). **Author:** referee F (line-by-line re-derivation agent; one of two independent referees on this item — the other is a different model, and nothing below assumes anything about its findings; standing order 7).
**Item under review:** `results/c3-r/probe-9.4-note.md` (dated 2026-08-26), §§3–7: Lemma A (§4), Lemma B (§6), Lemmas C and D and Proposition 1 with its Corollary (§5), the §3 freshman's-dream N-invariance argument, the §4 "Consequence 2" transport analysis (D3), and the §7 Haar formal count. Debt recorded at the note's §8 item 1.
**Method:** (1) read `results/c3-r/probe-9.3-adjudication.md` in full, then the whole 9.4 note; (2) opened the on-disk PDFs at every cited location and quoted the sentences verbatim below with the printed page (for [x-03] printed page = PDF page, checked against the running page numbers; for [x-06] the PDF has no separate printed numbering and pages are PDF pages); where the text layer garbled a formula (the packet base group on [x-03] pp. 33 and 38 and [x-06] p. 12) the page was rendered and read visually; (3) re-derived every step in my own words, in full; (4) at every gap I tried both to fill it (replacement text) and to break it (counterexample); (5) verdict block at the end. Standing order 5: nothing load-bearing is recalled; the two textbook facts I could not find on disk are labeled **[RU-standard]** with the theorem named, and neither carries a verdict on its own. U.S. English throughout.

---

## 0. VERDICT (stated first): **PASS-WITH-REPAIRS** — 0 FATAL, 1 MAJOR, 9 MINOR

Every statement in Lemmas A–D and Proposition 1 that the note actually *uses* downstream is true and is re-derived below from the on-disk sources. The one MAJOR finding is a hypothesis overreach in Lemma A (stated for an arbitrary algebraically closed field κ of characteristic p, while the statement is only well-formed, and the proof only valid, for κ an algebraic closure of F_p — which is the only case ever used). The MINOR findings are wording, scope and citation repairs, each with replacement text in §9.

| Item | Verdict | Findings (severity) |
|---|---|---|
| Lemma A (mod-p-additive ⟺ Teichmüller∘embedding), both directions | **PASS-WITH-REPAIRS** | MAJOR-1 (hypothesis κ; "W(k) ⊆ o" unjustified as stated — full replacement proof given); MINOR-2 (the Witt identity is on disk, [x-03] p. 101; cite it, do not recall "VF = p") |
| Lemma A's converse (the (⇐) direction, the note's own press point) | **PASS** after repair | covered by MAJOR-1's replacement proof, which needs no Witt-vector theory at all |
| Lemma B (archimedean threshold selects nothing on the packets) | **PASS-WITH-REPAIRS** | MINOR-3 ("periodic locus" is correct only for E ⊆ E_max; say "every packet Γ_p") |
| Lemma C (Aut(C) ↠ Aut(μ(C)) = Ẑ×) | **PASS-WITH-REPAIRS** | MINOR-4 (drop "infinite transcendence degree"; cite the on-disk cyclotomic anchor [x-03] (57) p. 47 + p. 59; state the AC dependence precisely) |
| Lemma D(i) (commutation with G, F_ν, Q^{>0}, flow) | **PASS-WITH-REPAIRS** | MINOR-5 (say explicitly: set-theoretic bijections, not homeomorphisms); MINOR-6 (cite [x-03] Remark 2.7 p. 21, where Deninger records this action) |
| Lemma D(ii) (stability of E_tors, E_max, E_f, E_fg, E_fd, E_fd0 — the note's press point for (Image)) | **PASS** | none — verified class by class against [x-03] pp. 27–29 |
| Lemma D(iii) (coordinate formula (a,ν) ↦ (u_σ a, ν)) | **PASS-WITH-REPAIRS** | MINOR-5(c) (typo in the printed form of B_p; the "structural identity" is Deninger's displayed formula, pp. 33 and 38 — attribute it) |
| Proposition 1 (D1) incl. the fibers-are-orbits consumption and uncountability | **PASS-WITH-REPAIRS** | MINOR-5(a) ("closed orbit" → "periodic orbit"); MINOR-5(b) (scope sentence on the non-topological nature of the Aut(C)-action); one sharpening offered (for Spec Z the conclusion is S ⊇ Γ^E_p) |
| §4 Consequence 2 (D3, transport reading) | **PASS-WITH-REPAIRS** | MINOR-7 (the transported class is not the admissible class E(a₀); what coincides is the selected periodic orbit) |
| §3 freshman's-dream argument | **PASS-WITH-REPAIRS** | MINOR-8 (make the statement precise: x ↦ x^ℓ is additive on F̄_p iff ℓ is a power of p) |
| §7 Haar formal count | **PASS** (as a formal identity; nothing analytic claimed) | none — [x-06] Thm 4.2 read verbatim: every orbit in Γ_p has length log p |

---

## 1. Sources read this session (every page opened, with what was taken from it)

All extractions fresh this session with `pdftotext` from the on-disk files named in the task; pages listed are printed pages of [x-03] = PDF pages (verified: the running number at the foot of PDF page n reads n for every page opened). Three pages were additionally rendered to PNG and read visually because the text layer garbles the formula Aut(F̄_p^×)/Aut(F̄_p).

**[x-03]** C. Deninger, *Dynamical systems for arithmetic schemes*, arXiv:1807.06400v4, `fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf` (119 PDF pages):
- p. 5: "Incidentally, if we consider points of W_rat(X) with values in rings without 'small multiplicative subgroups' like the complex number field C this process does not give more points." (note's §2 Stage 2 anchor — confirmed.)
- p. 6: "The answer is simple, Y⋄ consists of all the diagrams in X⋄_c(o) whose maps are not only multiplicative but mod p also additive." and "Thus the process of 'completion' to pass from X̌₀(o) to X⋄₀(o) was necessary to obtain something interesting." — confirmed.
- p. 21, Remark 2.7: "the group Aut(W_rat(X)) × Aut(S) operates on W_rat(X)(S) via the formula (Σ,τ)•f = Σ∘f∘τ^{-1}" and "Aut_N(W_rat(X)) × Aut(S) acts on W_rat(X)(S) by automorphisms which commute with the N-action." (anchor for Lemma D(i), see MINOR-6.)
- p. 22: definition of X•(C) as pairs (x, P^×), the right G-action "(x, P^×)σ = (x^σ, P^×∘σ) for σ ∈ G", the N-action "F_ν(x, P^×) = (x, P^×∘( )^ν)", and (26) W_rat(X)(C) = X•(C).
- p. 24: the colimit X̌(C) = colim_{N₀} X•(C), the Q₀^{>0}-action, "The G-action on X•(C) extends canonically to a G-action on X̌(C) commuting with the Q₀^{>0}-action and we have X̌₀(C) = X̌(C)/G."
- p. 25: (29) "X̌(C) is the set of pairs (x, P̌^×) where x ∈ X and P̌^× : lim_{N₀} κ(x)^× → C^× is a homomorphism which factors over pr_ν for some ν ∈ N₀."
- p. 27: conditions (Tors) and (Image) verbatim; Definition 4.1 verbatim; Proposition 4.2.
- pp. 28–29: the Example list E_tors, E_max, E_f, E_fg, E_fd, E_fd0 verbatim; the Remark "in the p-adic case … the right condition E is the following: P is additive mod p. This can be rephrased in terms of absolute values and translated to the case where C is the complex number field. However the resulting class E is not N-invariant."; the stable/functorial paragraph.
- p. 31: §5 opening, "Fix an injective homomorphism ι : μ(K) ↪ μ(C)", (32) i_x : μ^{(p)}(K) ≅ κ(x)^×.
- p. 32: χ_x = ι∘i_x^{-1}; (34) "N x₀^Ẑ = Gal(κ(x)/κ(x₀)) ↪ Aut(κ(x)^×) = Ẑ×_(p)"; (35) with its fiber description "Two elements (a, ν) and (a′, ν′) are in the same fibre of this map if and only if ν′ = νpⁿ and a = pⁿa′ for some n ∈ Z"; (36)–(38); the isotropy statement.
- p. 33 (text + visual): (39); "The set C_{x₀} fibres over the compact group Ẑ×_(p)/p^Ẑ = Aut(F̄_p^×)/Aut(F̄_p), and the fibres are the Q₀^{>0}-orbits in C_{x₀}."; "The maps (37), (38) and the fibration map depend on our choices of x and ι."
- p. 34: Theorem 5.2 verbatim incl. "If e.g. E ⊃ E_f then C^E_{x₀} = C_{x₀}."
- p. 38 (text + visual): §6 opening — the suspension X₀ = X̌₀(C)_E ×_{Q₀^{>0}} R^{>0}, the relation "(P₀, u)q = (P₀q, q^{-1}u) = (F_q(P₀), q^{-1}u)", the flow "φ^t([P₀, u]) = [P₀, ue^t]", Γ_{x₀} = C_{x₀} ×_{Q₀^{>0}} R^{>0}, "Thus all R^{>0}-orbits in Γ_{x₀} are circles R^{>0}/N x₀^Z and Γ_{x₀} fibres over Ẑ×_(p)/p^Ẑ = Aut(F̄_p^×)/Aut(F̄_p) with fibres the R^{>0}-orbits in Γ_{x₀}."
- p. 39: Theorem 6.1 verbatim, incl. "Any periodic orbit γ in X₀ is contained in Γ^E_{x₀} for a uniquely determined point x₀ of X₀ with finite residue field."; p. 40: the S4 question.
- p. 40: §7 opening: "In this section, C is an algebraically closed field with a valuation | | and the corresponding topology. … we give X•(C) the topology of pointwise convergence."
- p. 47: the E-space topology paragraph; "Fix an isomorphism ι : μ(K) ≅ μ(C)"; (56) "Ẑ ≅ H•, a ↦ (ζ ↦ ι(ζ)^a)"; (57) "κ : G ↠ Aut(K₀(μ(K))/K₀) = Aut(Q(μ(K))/K₀ ∩ Q(μ(K))) ⊂ Ẑ× be the cyclotomic character"; and, just above, "d_μ = (Ẑ× : κ(G))".
- p. 59: "d_μ = (K₀ ∩ Q(μ(K)) : Q) … Then d_μ = 1 if and only if K₀ is disjoint from the maximal cyclotomic extension of Q in K."
- p. 89: §14 opening incl. "In the following we only consider the monoid N₀ generated by p i.e. the F_p = ( )^p action."; p. 90: Definitions 14.1, 14.2.
- p. 93: the [CD14] presentation: "the natural map ZR → W_p(R) induces F_p-equivariant isomorphisms ZR/Iⁿ ≅ W_p(R)/pⁿW_p(R) for all n ≥ 1 and lim_n ZR/Iⁿ ≅ W_p(R)"; p. 94: "the ideal I is generated by the elements of the form [r+s] − [r] − [s]", Definition 14.5, (172), Proposition 14.7 statement; p. 95: proof of Prop. 14.7 (the ultrametric estimate "≤ max(|…|^{p^ν}, |p|)").
- pp. 99–101: Definition 14.12 = (183); the Remark "I do not know how to transport such conditions to the points of X̌(C), where X is a scheme of finite type over spec Z and C is the complex number field."; Proposition 14.13; Proposition 14.14 with proof, in particular p. 101: "The composition ZA♭ → W_p(A♭) → W_p(A♭)/p = A♭ is the map π and hence π(I) ⊂ pW_p(A♭)."
- pp. 113–114: the closed-point description "For (x, y) = (s, s) the continuous local ring homomorphisms P̂♭_y : κ → o♭ … are simply the ring homomorphisms P̂_y : κ ↪ k ⊂ o"; Theorem 15.6 in full, in particular "(1) There is a natural G × Aut(o) × ⟨F_p⟩-equivariant identification Y⋄ = Hom_cont(ô♭_K, o♭)", "Y⋄_s := pr_X^{-1}(s) = Hom(κ, k)", (224) "Y⋄₀_{s₀} … = Hom(κ₀, k)", "(6) The only periodic (i.e. finite) orbit of the F_p-action on Y⋄₀ is Y⋄₀_{s₀}. It has order log_p N(π₀) = r if q = p^r."; p. 115: proof of (6) ("It is clear that Y⋄₀_{s₀} ≅ Hom(κ₀, k) is a periodic orbit of order r"); p. 116: Proposition 15.8.

**[x-06]** C. Deninger, *Primes, knots and periodic orbits*, arXiv:2301.11643, `fetched/x-06-deninger-2024-primes-knots-and-periodic-orbits.pdf` (16 PDF pages): pp. 10–13 in full. p. 11: Theorem 4.1 (the G- and N-actions, same formulas as [x-03] p. 22), the suspension and flow "φ^t[P, u] = [P, e^t u]", the paragraph "In the local p-adic situation below, we know the right modification to make. However in the global case presently we can only impose an 'admissible' condition E"; Theorem 4.2 (p. 11) with its continuation on p. 12 (visual): "The compact subsets Γ_{x₀} ⊂ X₀ consist of periodic orbits of length log N x₀ where N x₀ = |κ(x₀)| … and they are pairwise disjoint. In fact Γ_{x₀} is a fibre space over the compact group Aut(F̄_p^×)/Aut(F̄_p) where p = char κ(x) with fibres the compact orbits in Γ_{x₀}."; p. 13: Theorem 4.4 and the Steinberg-relations paragraph.

**[r3s-08]** Morishita, arXiv:2508.15971v5, `fetched-r3/r3s-08-morishita-deninger-cc-bridge-2508.15971.pdf`: grep-located only (lines naming "the arithmetic linking homomorphism lk_p"); not load-bearing for this item — Proposition 1 consumes [x-03] p. 33 directly, not the Morishita bridge. Nothing here is cited from it for topology (adjudication §4 item 4 respected).

**[D25]** `fetched-r3/r3s-22-…2508.05329v1…pdf`: opened for the corpus record only; nothing in Lemmas A–D or Proposition 1 rests on it (it feeds the note's Road 1, outside this item).

**Program-internal:** `results/c3-r/probe-9.3-adjudication.md` (all sections; its §2 anchor list and its re-derivation of the uncountability of B_p were used as a cross-check, then re-derived independently in §6.4 below); `results/corpus-routing.md` header caveats 1–20 (nothing in them touches these four files beyond the standing rule that text layers are checked visually where a formula matters — done for the three garbled lines).

**[RU-standard] items (recalled, named, not on disk; each is a textbook theorem and is flagged where used):** (R1) for m prime to p, the cyclotomic polynomial Φ_m is separable modulo p (because X^m − 1 is), used only in the *elementary alternative* proof of Lemma A(⇐) in §2.5; (R2) the irreducibility of Φ_n over Q, i.e. Gal(Q(ζ_n)/Q) ≅ (Z/n)^× — but for the case K₀ = Q the *conclusion* needed (surjectivity of the cyclotomic character onto Ẑ×) is on disk at [x-03] p. 47 + p. 59, so (R2) is not load-bearing.

---

## 2. Lemma A — mod-p-additive multiplicative maps are exactly the Teichmüller lifts of field embeddings

### 2.1 The note's statement (verbatim, §4)

> "Let o be as in §2 (residue field k algebraically closed of char p), κ an algebraically closed field of characteristic p, and P: κ → o multiplicative with P(0) = 0, P(1) = 1, whose restriction to κ^× is a group homomorphism into o (values automatically in μ^{(p)}(o), the prime-to-p roots of unity, since κ^× is prime-to-p torsion). Then |P(r+s) − P(r) − P(s)| ≤ |p| for all r, s ∈ κ **iff** P = [·]∘τ for a unique field embedding τ: κ ↪ k, where [·] is the Teichmüller section of the reduction μ^{(p)}(o) ≅ μ^{(p)}(k)."

The proof offered: injectivity and surjectivity of reduction on μ^{(p)}(o); (⇒) reduce mod m to get a ring homomorphism τ, then compare roots of unity with equal reduction; (⇐) "[a] + [b] − [a+b] ∈ V W(k) = p W(k) in the Witt ring W(k) ⊆ o (first ghost/component coordinates agree; V F = p on Witt vectors of a perfect ring)".

### 2.2 Source anchors

- Deninger's condition at the closed point: [x-03] Definition 14.5 (p. 94) / Definition 14.12 = (183) (p. 99): "|P̂_y(r+s) − P̂_y(r) − P̂_y(s)| ≤ α for r, s ∈ Ô♭_{x,y}", with Y⋄ := Y⋄_{1/p} (p. 99) and Proposition 14.13 (p. 100) "Y⋄_α = Y⋄ for α ≥ 1/p". At the closed point (x,y) = (s,s) the tilted domain is lim_{( )^p} κ ≅ κ (p. 113), so the domain of the condition is κ itself — exactly Lemma A's setting.
- Deninger's own description of the closed-point locus, p. 113: "For (x, y) = (s, s) the continuous local ring homomorphisms P̂♭_y : κ → o♭ … are simply the ring homomorphisms P̂_y : κ ↪ k ⊂ o", and Theorem 15.6 p. 114: "Y⋄_s := pr_X^{-1}(s) = Hom(κ, k)". The inclusion "k ⊂ o" is Deninger's shorthand for the Teichmüller lift of k = F̄_p (roots of unity) — this is the on-disk form of Lemma A's conclusion and the note's "Consistency" line is confirmed.
- Theorem 15.6(6), p. 114, and its proof p. 115 ("It is clear that Y⋄₀_{s₀} ≅ Hom(κ₀, k) is a periodic orbit of order r for the F_p-action") — confirms the note's "Hom(κ₀, k) is a single F_p-orbit of size r = deg(κ₀/F_p)".
- The Witt identity the note recalls is **on disk**: p. 101, "The composition ZA♭ → W_p(A♭) → W_p(A♭)/p = A♭ is the map π and hence π(I) ⊂ pW_p(A♭)", with I "generated by the elements of the form [r+s] − [r] − [s]" (p. 94) and W_p(R)/p ≅ ZR/I for perfect R from [CD14] (p. 93). Read for a perfect field R: [r+s] − [r] − [s] ∈ pW_p(R). No "VF = p" is needed for this; see MINOR-2.

### 2.3 Re-derivation, step by step (for κ an algebraic closure of F_p — see 2.4 for why the hypothesis must be so restricted)

Standing facts about o used below, each checked: o is p-adically complete, so |p| < 1; the valuation restricted to Q is nontrivial with |p| < 1, hence equivalent to the p-adic one, so **|d| = 1 for every integer d prime to p**; C is algebraically closed, and o, being a valuation ring, is integrally closed in C, so **every root of unity of C lies in o**; for m prime to p the polynomial X^m − 1 is separable over C (derivative mX^{m−1}, m ≠ 0 in C), so **μ_m(o) = μ_m(C) is cyclic of order exactly m**.

**Step 0 (reduction μ^{(p)}(o) → μ^{(p)}(k) is a bijection).** *Injective:* let ζ ∈ μ_d(o), p ∤ d, ζ ≡ 1 mod m. Then 0 = ζ^d − 1 = (ζ − 1)(ζ^{d−1} + … + ζ + 1) and the second factor is ≡ d mod m, a unit of o since |d| = 1; so ζ = 1. (This is the note's argument; correct.) *Surjective, and in fact bijective on each μ_m:* μ_m(o) has exactly m elements, μ_m(k) has at most m (k is a field), and reduction is an injective group homomorphism μ_m(o) → μ_m(k); an injection of an m-element set into a set of size ≤ m is a bijection. Taking the union over m prime to p gives the bijection μ^{(p)}(o) → μ^{(p)}(k). (The note's divisible-image argument is also correct — the ℓ-primary part of the image is a nonzero divisible subgroup of Q_ℓ/Z_ℓ, and the only such subgroup is Q_ℓ/Z_ℓ itself, the proper subgroups being the finite cyclic Z/ℓⁿ — but it presupposes k algebraically closed and μ^{(p)}(k) ≅ ⊕_{ℓ≠p} Q_ℓ/Z_ℓ; the counting argument needs neither.) Define [·] := the inverse bijection, extended by [0] = 0.

**Step 1 (values of P).** For κ = F̄_p, every r ∈ κ^× has finite order d(r) prime to p (F̄_p^× = ∪_n F_{pⁿ}^×, each of order pⁿ − 1 prime to p). P|_{κ^×} is a homomorphism into o^× (P(r)P(r^{-1}) = P(1) = 1), so P(r)^{d(r)} = 1 and P(r) ∈ μ^{(p)}(o). ✓ (This is where κ = F̄_p enters: for κ ⊋ F̄_p the group κ^× is not torsion; see 2.4.)

**Step 2 (⇒).** Assume |P(r+s) − P(r) − P(s)| ≤ |p| for all r, s. Then P(r+s) − P(r) − P(s) ∈ p·o ⊆ m, so P̄ := P mod m : κ → k satisfies P̄(r+s) = P̄(r) + P̄(s), P̄(rs) = P̄(r)P̄(s), P̄(1) = 1: a unital ring homomorphism out of a field, hence injective; write τ := P̄ : κ ↪ k. For r ∈ κ^×, both P(r) and [τ(r)] lie in μ^{(p)}(o) (Step 1 and the definition of [·]) and have the same reduction τ(r); by Step 0 (injectivity) P(r) = [τ(r)]. For r = 0: P(0) = 0 = [τ(0)]. So P = [·]∘τ, and τ = P mod m is uniquely determined by P. ✓

**Step 3 (⇐), first proof — elementary, no Witt vectors.** Let τ : κ ↪ k be a field embedding and P := [·]∘τ. Fix r, s ∈ κ. If r = 0 or s = 0 the defect is 0. Otherwise choose m prime to p with r^m = s^m = 1 and (if r + s ≠ 0) (r+s)^m = 1 (possible: all three lie in some finite field F_{pⁿ}^×, take m = pⁿ − 1). Let ζ_m ∈ o be a primitive m-th root of unity and A := Z[ζ_m] ⊆ o. By Step 0, [τ(r)], [τ(s)], [τ(r+s)] are elements of μ_m(o) ∪ {0} = ⟨ζ_m⟩ ∪ {0} ⊆ A. Put d := P(r+s) − P(r) − P(s) ∈ A. Its reduction in k is τ(r+s) − τ(r) − τ(s) = 0 (τ is additive), so d ∈ P₀ := ker(A → o → k), a prime ideal of A containing p.
*Claim: P₀A_{P₀} = pA_{P₀}.* Let f ∈ Z[X] be the minimal polynomial of ζ_m over Q; it is monic with integer coefficients (ζ_m is integral), and Z[X] → A has kernel fZ[X] (Gauss's lemma: a polynomial in Z[X] vanishing at ζ_m is divisible by f in Q[X], hence in Z[X] since f is monic). So A ≅ Z[X]/(f) and A/pA ≅ F_p[X]/(f̄). Since ζ_m^m = 1, f divides X^m − 1 in Z[X], so f̄ divides X^m − 1 in F_p[X], which is separable because p ∤ m (its derivative mX^{m−1} is prime to it). Hence f̄ is separable, F_p[X]/(f̄) is a finite product of fields, and pA = P₁ ∩ … ∩ P_g = P₁⋯P_g with P₁, …, P_g the distinct (maximal) primes of A above p. P₀ is one of them, say P₁. In the localization A_{P₁} the ideals P₂, …, P_g become the unit ideal, so P₁A_{P₁} = pA_{P₁}. ∎(Claim)
By the Claim, d = p·a/s with a ∈ A and s ∈ A ∖ P₀. Since s ∉ P₀, the residue of s in k is nonzero, so s is a unit of the valuation ring o. Therefore d = p·a·s^{-1} ∈ p·o, i.e. |P(r+s) − P(r) − P(s)| ≤ |p|. ∎

**Step 3 (⇐), second proof — the Witt route, anchored on disk.** For the perfect field κ, [x-03] p. 93 gives ZR/I ≅ W_p(R)/p (R = κ, from [CD14]) and p. 101 states "π(I) ⊂ pW_p(A♭)", i.e. [a]+[b]−[a+b] ∈ pW_p(κ) for all a, b ∈ κ. To carry this into o one needs a ring homomorphism W_p(κ) → o extending τ on Teichmüller representatives, i.e. the identification of W_p(F̄_p) with the completion of Z_p[μ^{(p)}] under which Teichmüller representatives are the roots of unity — a standard fact **not on disk** in the four sources ([RU-standard]); the note's "W(k) ⊆ o" is this fact, asserted for a general algebraically closed k, where it is not even true as stated (the residue field of a p-adically complete valuation ring need not admit any ring-theoretic Teichmüller section k → o/p when k has transcendental elements). The first proof avoids all of this, so the note should adopt it (MAJOR-1 replacement text, §9).

**Step 4 (the note's consistency check).** With κ = F̄_p and k ⊇ F̄_p: the mod-p-additive P are the [·]∘τ, τ ∈ Hom(F̄_p, k) — a torsor under Aut(F̄_p) = Ẑ (Frobenius closure); this is Deninger's "Y⋄_s = Hom(κ, k)" (p. 114). For κ₀ = F_q, q = p^r, Hom(κ₀, k) has r elements permuted cyclically by F_p, one orbit of size r — Theorem 15.6(6), proof p. 115. ✓

### 2.4 Attempt to break the statement as written — succeeds against the hypothesis, not against the mathematics used

Take κ = an algebraic closure of F_p(t) (algebraically closed of characteristic p, as the statement allows), o = o_{C_p}, k = F̄_p. Then (i) κ^× is **not** prime-to-p torsion (t has infinite order), so the parenthetical "since κ^× is prime-to-p torsion" is false; (ii) the composite "[·]∘τ" is undefined, because [·] is only defined on μ^{(p)}(k) ∪ {0} and τ(t) ∉ μ(k) ∪ {0} — in fact here no field embedding τ : κ ↪ k exists at all (transcendence degree 1 into an algebraic field); (iii) Step 2's "P(r) and [τ(r)] are prime-to-p roots of unity" fails for r = t. The (⇒) direction, read literally for this κ, asserts that no mod-p-additive P : κ → o exists — which happens to be true (P mod m would be an injective ring homomorphism κ ↪ F̄_p), but the note's proof does not prove it in this form, and the (⇐) side is not even a statement. **The statement is only well-formed for κ algebraic over F_p, i.e. κ ≅ F̄_p, and that is the only case the note ever applies it to** (the packet residue fields κ(x) = F̄_p of Spec Z̄, [x-03] p. 31 "the residue field κ(x) is an algebraic closure of κ(x₀)"; Theorem 15.6's closed point). With the hypothesis restricted, every step of 2.3 holds and I found no way to break it: the (⇒) direction is forced by Step 0's injectivity, and the (⇐) direction by the elementary Claim.

**Finding MAJOR-1** (Lemma A hypothesis and (⇐) proof). Replacement text in §9. Downstream impact: none — Consequence 1, Consequence 2 (D3), the §3 argument and the Thm 15.6 consistency check all use κ = F̄_p.
**Finding MINOR-2** (cite [x-03] pp. 93–94, 101 for the Witt identity; drop the recalled "VF = p"; or, better, use the elementary proof).

---

## 3. Lemma B — the archimedean threshold reading is empty on every packet

### 3.1 The note's statement (verbatim, §6)

> "For X₀ = Spec Z, at every point of every packet (any prime p, any character P in any class E ⊆ E_tors), the test r = s = 1 gives |P(1̄+1̄) − P(1̄) − P(1̄)| = |P(2̄) − 2| ≥ 1, since P(2̄) is a root of unity or 0 (κ(x)^× is torsion; 0 occurs iff p = 2). Hence the class 'archimedean defect ≤ ε at char-p points' is empty on the periodic locus for every ε < 1. Moreover the (F3) extension mechanism requires the defect ideal to land in a topologically nilpotent set (|·| < 1, so that lim ZR/Iⁿ receives the evaluation — (172), p. 94); with a defect bounded below by 1 there is no completion and no A_inf-analog action."

### 3.2 Source anchors

- The local condition being translated: Definition 14.5 (p. 94) and (183) (p. 99), quoted in §2.2. The completion mechanism: p. 94, "Choose an element ω_α ∈ o with α ≤ |ω_α| < 1. Then (x, y, P̌_y) ∈ Y̌_α gives a ring homomorphism P̌_y : ZÔ♭ → o with P̌_y(I_y) ⊂ ω_α o and hence an induced ring homomorphism W_p(P̌_y) : W_p(Ô♭) = lim ZÔ♭/I_yⁿ → lim o/ω_αⁿ = o" (172). ✓ — the mechanism needs |ω_α| < 1, as the note says.
- Packet points: [x-03] p. 32, "The fibre pr₀^{-1}(x₀) consists of the G-orbits of all pairs (x, P^×) where x is a point of X over x₀ and P^× : κ(x)^× → C^× satisfies (Tors). Since κ(x)^× is torsion …". Points of X̌(C) over x: (29) p. 25, characters factoring over some pr_ν, i.e. F_ν^{-1}(x, P) with P a character of κ(x)^×.
- Which points are periodic: Theorem 6.1 (p. 39), for E ⊂ E_max: "Any periodic orbit γ in X₀ is contained in Γ^E_{x₀} for a uniquely determined point x₀ of X₀ with finite residue field." [x-06] Thm 4.2 (pp. 11–12) says the same for X₀^E.

### 3.3 Re-derivation

Let x ∈ Spec Z̄ lie over (p), κ(x) = F̄_p. A packet point is F_ν^{-1}(x, P) with P : κ(x)^× → C^× a character extended by P(0) = 0 (Remark 3.4, p. 23: P(0) = 0, P(1) = 1). The "verbatim archimedean translation" is: |P(r+s) − P(r) − P(s)|_∞ ≤ ε for all r, s in the domain (κ(x), or the ring Z̄ through the evaluation Z̄ → κ(x) — the computation below is the same for both, since P(n) = P(n̄) for n ∈ Z).
Test r = s = 1: P(1) = 1 (P|_{κ^×} is a homomorphism). *Case p = 2:* 1̄ + 1̄ = 0̄, P(0̄) = 0, defect = |0 − 2| = 2 ≥ 1. *Case p odd:* 2̄ ∈ F_p^× ⊆ κ(x)^× has finite order prime to p, so ζ := P(2̄) is a root of unity of C, |ζ| = 1, and |ζ − 2| ≥ |2| − |ζ| = 1, with equality iff ζ = 1. Hence **|P(2̄) − 2| ≥ 1 at every packet point, for every character P whatsoever** (not only E ⊆ E_tors: the argument uses only that κ(x)^× is torsion, which is true at every point over a prime; the class E is irrelevant). For ε < 1 the threshold condition therefore fails at r = s = 1. ✓
*Independence of the representative:* a point of the colimit has many representatives (x, P∘( )^{ν'}) at different levels; the inequality holds at each of them (P∘( )^{ν'} is again a character extended by zero), so the emptiness conclusion does not depend on which representative the condition is evaluated at — and also on which of the two candidate domains (residue field or Z̄) is used. ✓
*The completion remark:* (172) requires |ω_α| < 1 with the defect ideal mapped into ω_α·o; with a defect of absolute value ≥ 1 no such ω_α exists, and lim o/ω_αⁿ degenerates. ✓ (This is a remark about the mechanism, not a theorem; correctly labeled as such.)

### 3.4 Break attempt

None possible: for |ζ| ≤ 1 one has |ζ − 2| ≥ 1 by the triangle inequality, so no choice of x, P, ν, ε < 1 evades the test. The inequality is sharp exactly at P(2̄) = 1 (e.g. p = 3, P trivial on F_3^× — which is allowed in E_tors as long as the kernel restricted to μ(κ(x)) is finite, e.g. kernel of order 2 ∈ N₀; the defect is then exactly 1, still ≥ 1).

### 3.5 Is "the periodic locus" the right locus? — **MINOR-3**

For E ⊆ E_max, Theorem 6.1 (p. 39) identifies the periodic points of X₀ with ∐_p Γ^E_p, so "empty on the periodic locus" is literally correct there. For E = E_tors — which the lemma explicitly allows ("any class E ⊆ E_tors") — Theorem 6.1 is not stated (its hypothesis is E ⊂ E_max), and characters at the generic point with torsion image are admitted by E_tors but excluded by (Image), so the identification of the periodic locus with the packets is not available on disk for E_tors. The lemma's actual content is about the packets Γ_p, which is what S4's count concerns. Replacement wording in §9: "empty on every packet Γ_p, p prime — for E ⊆ E_max the whole periodic locus ([x-03] Thm 6.1, p. 39; [x-06] Thm 4.2, pp. 11–12)". No mathematical change.

**Lemma B: PASS-WITH-REPAIRS (MINOR-3 only).** The judgment-grade paragraph that follows the lemma in the note (Deninger's intended reading) is flagged as such in the note and is not adjudicated here.

---

## 4. Lemma C — Aut(C) → Aut(μ(C)) = Ẑ× is surjective

### 4.1 The note's statement (verbatim, §5)

> "The restriction map Aut(C) → Aut(μ(C)) = Ẑ× is surjective for C the complex numbers (or any algebraically closed field of characteristic 0 containing Q̄ with infinite transcendence degree). *Derivation:* u ∈ Ẑ× defines an automorphism of Q(μ_∞) (cyclotomic theory); extend to Q̄ (isomorphism extension), then to C along a transcendence basis of C over Q̄ and to the algebraic closure C of the lifted subfield (Steinitz; uses AC)."

### 4.2 Source anchors (on disk — the cyclotomic step does not have to be recalled)

- [x-03] p. 47, (56): "Using ι, we have a topological isomorphism Ẑ ≅ H•, a ↦ (ζ ↦ ι(ζ)^a)", where H• = Hom(μ(K), μ(C)) — i.e. End(μ(C)) = Ẑ once μ(K) ≅ μ(C); hence Aut(μ(C)) = Ẑ×.
- [x-03] p. 47, (57): "κ : G ↠ Aut(K₀(μ(K))/K₀) = Aut(Q(μ(K))/K₀ ∩ Q(μ(K))) ⊂ Ẑ× be the cyclotomic character", together with (same page) "d_μ = (Ẑ× : κ(G))" and p. 59 "d_μ = (K₀ ∩ Q(μ(K)) : Q) … d_μ = 1 if and only if K₀ is disjoint from the maximal cyclotomic extension of Q in K". For K₀ = Q, K = Q̄: d_μ = 1, so **κ : Gal(Q̄/Q) ↠ Ẑ× is surjective** — Deninger's own statement; this is exactly the cyclotomic step of Lemma C, so no textbook recall is load-bearing.

### 4.3 Re-derivation

**Step 0 (the target group).** C is algebraically closed of characteristic 0, so for each n ≥ 1 the polynomial Xⁿ − 1 is separable and μ_n(C) is cyclic of order n; μ(C) = ∪_n μ_n(C) ≅ Q/Z. An endomorphism of μ(C) restricts to an endomorphism of each μ_n(C) ≅ Z/n, i.e. to multiplication by some a_n ∈ Z/n, compatibly under n | n′; so End(μ(C)) = lim_n Z/n = Ẑ and Aut(μ(C)) = Ẑ× (on disk as (56)). ✓

**Step 1 (cyclotomic, and up to Q̄ — one step on disk).** Let Q̄ ⊆ C be the algebraic closure of Q inside C (C ⊇ Q since char C = 0; the algebraic elements form an algebraically closed subfield algebraic over Q, hence an algebraic closure of Q, and μ(C) ⊆ Q̄). Given u ∈ Ẑ×, by (57) + d_μ = 1 there is σ₀ ∈ Gal(Q̄/Q) with σ₀(ζ) = ζ^u for all ζ ∈ μ(Q̄) = μ(C). ✓ (Without the on-disk anchor: [RU-standard] R2 gives, for each n, a unique automorphism of Q(ζ_n) with ζ_n ↦ ζ_n^{u mod n}; these are compatible and define an automorphism of the countable union Q(μ_∞) with no choice; the isomorphism-extension theorem then extends it to Q̄. This is the note's two-step route; it is correct.)

**Step 2 (from Q̄ to C — Steinitz).** Choose a transcendence basis B of C over Q̄ [AC]. Q̄[B] is a polynomial ring, so σ₀ extends to a ring automorphism σ₁ of Q̄[B] acting on coefficients and fixing B, and hence to the fraction field Q̄(B). C is algebraic over Q̄(B) and algebraically closed, so C is an algebraic closure of Q̄(B); the isomorphism-extension theorem [Zorn] gives a field embedding σ : C → C extending σ₁. Its image σ(C) is an algebraically closed subfield of C containing σ₁(Q̄(B)) = Q̄(B), over which C is algebraic; hence σ(C) = C and σ ∈ Aut(C) with σ|_{μ(C)} = ( )^u. ✓ (If B = ∅, i.e. C = Q̄, Step 2 is empty — so the hypothesis "infinite transcendence degree" is not needed: **any** algebraically closed field of characteristic 0 works. MINOR-4.)

**Step 3 (what Proposition 1 actually needs).** Composing with the projection Ẑ× = ∏_ℓ Z_ℓ^× → ∏_{ℓ≠p} Z_ℓ^× = Ẑ×_(p) (surjective), every u ∈ Ẑ×_(p) is the prime-to-p part u_σ of the action of some σ ∈ Aut(C) on μ^{(p)}(C). ✓

**Exact use of choice.** (i) Existence of a transcendence basis of C over Q̄ — AC. (ii) The isomorphism-extension theorem for the algebraic extension C/Q̄(B) — Zorn. (iii) Step 1 needs no choice (countable tower; or Deninger's (57)). Choice is *essential* for C = the complex numbers: in ZF it is consistent (Solovay's model, where every set of reals is Lebesgue measurable) that every automorphism of C is measurable, hence continuous, hence the identity or complex conjugation [RU-standard: a measurable homomorphism between Polish groups is continuous; a continuous automorphism of C fixes Q, hence R, hence is id or conjugation] — in which case the image of Aut(C) in Ẑ× is {±1} and Proposition 1 is vacuous. So Lemma C and Proposition 1 are ZFC theorems whose content is choice-dependent; the note's "(uses AC)" is honest and should be made this precise (MINOR-4, optional sentence).

### 4.4 Break attempt

None available in ZFC: the surjectivity is forced by Step 1 (on disk) and Step 2 (Steinitz). The only "break" is the ZF remark above, which does not touch the note's claims.

**Lemma C: PASS-WITH-REPAIRS (MINOR-4).**

---

## 5. Lemma D — the Aut(C)-action: commutation, class stability, packet coordinates

### 5.1 The note's statement (verbatim, §5)

> "Let σ ∈ Aut(C) act on X̌(C)_{E_tors} by post-composition, (x, P) ↦ (x, σ∘P). Then: (i) σ commutes with the G-action (pre-composition), with every F_ν, hence with the Q^{>0}-action, and descends to the suspension X₀^{E_tors} commuting with the flow φ^t and fixing the R-coordinate; (ii) σ preserves each example class E_tors, E_max, E_f, E_fg, E_fd, E_fd0 (kernels are unchanged — ker(σ∘P) = ker P — and images map by σ, preserving torsion and ⊗Q-dimension; Def. 4.1's operations are pre-compositions, which commute with σ); (iii) on the packet over p, σ maps the point with coordinates (a, ν) to the point with coordinates (u_σ a, ν), where u_σ ∈ Ẑ×_(p) is σ's action on prime-to-p roots of unity: σ∘χ_x = σ|_μ∘χ_x = χ_x∘( )^{u_σ} because χ_x is an isomorphism onto μ^{(p)}(C) (injective character between groups ≅ ⊕_{ℓ≠p}Q_ℓ/Z_ℓ, divisible-image argument as in Lemma A) and power maps commute with any group homomorphism. Hence σ moves the base class [a] ↦ [u_σ a] in B_p and maps closed orbits of length log p to closed orbits of length log p in the same packet."

### 5.2 Source anchors (all verbatim this session)

- The two actions on X•(C), p. 22: "The group G acts on X•(C) from the right by (x, P^×)σ = (x^σ, P^×∘σ) for σ ∈ G. The G-action commutes with the N-action by F_ν(x, P^×) = (x, P^×∘( )^ν) for ν ∈ N." The colimit and its Q₀^{>0}-action, p. 24; the description (29), p. 25.
- Deninger's own record of the coefficient-automorphism action, Remark 2.7, p. 21: "the group Aut(W_rat(X)) × Aut(S) operates on W_rat(X)(S) via the formula (Σ, τ)•f = Σ∘f∘τ^{-1}" and "Aut_N(W_rat(X)) × Aut(S) acts on W_rat(X)(S) by automorphisms which commute with the N-action." With S = spec C, Aut(S) = Aut(C), and W_rat(X)(C) = X•(C) by (26), p. 22. (MINOR-6: cite this.)
- The classes: (Tors), (Image), Definition 4.1 (p. 27); E_tors … E_fd0 (pp. 28–29), quoted in §1.
- Packet coordinates: (32), χ_x = ι∘i_x^{-1}, (34), (35) with its fiber rule, (36)–(38) (p. 32); fibration and "fibres are the Q₀^{>0}-orbits" (p. 33); Γ_{x₀}, circles R^{>0}/N x₀^Z, fibration of Γ_{x₀} (p. 38); flow φ^t (p. 38).
- Topology, p. 40: "C is an algebraically closed field with a valuation | | and the corresponding topology … the topology of pointwise convergence."

### 5.3 Re-derivation of (i)

Let σ ∈ Aut(C); σ restricts to a group automorphism of C^×. For (x, P) ∈ X•(C) (P : κ(x)^× → C^× a homomorphism) set σ_*(x, P) := (x, σ∘P) — again a point of X•(C).
- *G:* σ_*((x,P)τ) = σ_*(x^τ, P∘τ) = (x^τ, σ∘P∘τ) = (σ_*(x,P))τ. ✓
- *F_ν:* σ_*(F_ν(x,P)) = (x, σ∘(P∘( )^ν)) = (x, (σ∘P)∘( )^ν) = F_ν(σ_*(x,P)). ✓
- Hence σ_* descends to X•₀(C) = X•(C)/G, is compatible with the transition maps F_ν of colim_{N₀}, so acts on X̌(C) and X̌₀(C); on X̌(C) it commutes with the bijections F_ν and their inverses, hence with the whole Q₀^{>0}-action. In the description (29), σ∘P̌^× factors over pr_ν iff P̌^× does. ✓
- *E-loci:* if σ_*E = E (part (ii)), σ_* preserves X̌(C)_E and X̌₀(C)_E. ✓
- *Suspension:* define σ_*[P₀, u] := [σ_*P₀, u]. Well-defined: (P₀, u)q = (F_q P₀, q^{-1}u) ↦ (σ_*F_q P₀, q^{-1}u) = (F_q σ_*P₀, q^{-1}u) = (σ_*P₀, u)q. Commutes with the flow: σ_*φ^t[P₀,u] = [σ_*P₀, ue^t] = φ^tσ_*[P₀,u]; fixes the R-coordinate by construction. ✓
- *Scope (MINOR-5(b)).* Everything above is set-theoretic. The topology on X•(C) is pointwise convergence for the valuation topology of C (p. 40). For C the complex numbers, a continuous automorphism fixes Q pointwise, hence R (density), hence is the identity or conjugation; every other σ is discontinuous on C, and then σ_* is discontinuous on X•(C): at the generic point η, characters P : Q̄^× → C^× take arbitrary values in C^× (Lemma 4.3, p. 28 constructs them freely on a Q-vector-space complement of μ), and a pointwise-convergent sequence P_n(r) → P(r) is not carried to one by a discontinuous σ. So **Aut(C) acts on (X₀, φ^t) by flow-equivariant bijections that are not homeomorphisms; the topological dynamical system is not Aut(C)-invariant.** Lemma D and Proposition 1 use no continuity, so nothing breaks — but the note must say so, because it fixes the reach of the Corollary (§6.6).

### 5.4 Re-derivation of (ii), one class at a time (the note's press point)

Throughout, χ : κ^× → C^× is a character on an algebraically closed field κ and σ_*χ := σ∘χ. Since σ|_{C^×} is injective, **ker(σ∘χ) = ker χ**; since σ|_{C^×} is a group automorphism, **(σ∘χ)(κ^×) = σ(χ(κ^×)) is a subgroup of C^× isomorphic to χ(κ^×)**.
- **(Tors)** "the group ker(χ)_tors = ker(χ|_{μ(κ)}) is finite and |(ker χ)_tors| ∈ N₀": depends only on ker χ. Invariant. **E_tors** ✓.
- **(Image)** "Only if char κ > 0. If χ(κ^×) is torsion, then κ^× is torsion as well, i.e. κ^× ⊗ Q ≠ 0 implies χ(κ^×) ⊗ Q ≠ 0": χ(κ^×) is torsion iff its isomorphic image σ(χ(κ^×)) is torsion; equivalently χ(κ^×) ⊗ Q ≅ σ(χ(κ^×)) ⊗ Q. So the implication holds for χ iff it holds for σ∘χ. Invariant. **E_max** = (Tors) ∧ (Image) ✓. (The note's "images map by σ, preserving torsion and ⊗Q-dimension" is exactly this; it needs only that σ is an automorphism of the abstract group C^×.)
- **E_f** (ker χ finite), **E_fg** (ker χ finitely generated), **E_fd** (ker χ ⊗ Q finite-dimensional): kernel conditions, invariant ✓.
- **E_fd0** ("(ker χ|_{κ(x₀)^×}) ⊗ Q is finite dimensional where x₀ = π(x)"): ker((σ∘χ)|_{κ(x₀)^×}) = ker(χ|_{κ(x₀)^×}). Invariant ✓.
- *Bonus, not needed:* Definition 4.1's operations χ ↦ χ∘σ′ (σ′ ∈ Aut κ) and χ ↦ χ∘( )^ν are pre-compositions and commute with post-composition by σ, so σ_* maps admissible classes to admissible classes, and likewise "stable" and "functorial" classes (p. 29) to such. Each named class satisfies σ_*E = E (not merely σ_*E ⊆ E, since σ^{-1} is also in Aut(C)).
**Lemma D(ii): PASS, no finding.** Break attempt: I looked for a named class whose definition consults the *values* of χ beyond torsion-ness — none does (all are kernel conditions or the torsion condition on the image), so no counterexample exists among the six.

### 5.5 Re-derivation of (iii)

Fix x over x₀ = (p) and ι : μ(K) ↪ μ(C) (p. 31), K = Q̄. (32): i_x : μ^{(p)}(K) ≅ κ(x)^×. **χ_x := ι∘i_x^{-1} is an isomorphism κ(x)^× → μ^{(p)}(C):** injective since ι is; for m prime to p, ι maps the cyclic group μ_m(K) of order m injectively into μ_m(C) of order m, hence onto; union over m gives surjectivity onto μ^{(p)}(C) (the note's divisible-image argument is a correct alternative). **u_σ:** σ restricts to an automorphism of the abstract group μ^{(p)}(C); an endomorphism of μ^{(p)}(C) = ∪_{(m,p)=1} μ_m(C) is a compatible family of multiplications by elements of Z/m, i.e. an element of lim_{(m,p)=1} Z/m = Ẑ_(p) (cf. (56), p. 47, for the full μ(C)); so σ|_{μ^{(p)}(C)} = ( )^{u_σ} with u_σ ∈ Ẑ×_(p), independent of x and ι. **σ∘χ_x = χ_x∘( )^{u_σ}:** for r ∈ κ(x)^× of order d (prime to p), χ_x(r) has order d, and ( )^{u_σ} acts on both r and χ_x(r) as ( )^{u_σ mod d}; χ_x being a homomorphism, σ(χ_x(r)) = χ_x(r)^{u_σ} = χ_x(r^{u_σ}). ✓ **Coordinates:** for a packet representative χ_x·(a,ν) = χ_x∘( )^a∘( )^ν ((35), p. 32), σ∘χ_x∘( )^a∘( )^ν = χ_x∘( )^{u_σ}∘( )^a∘( )^ν = χ_x∘( )^{u_σ a}∘( )^ν = χ_x·(u_σ a, ν), since power maps on an abelian group commute. Compatibility with the fiber rule of (35): (a,ν) ~ (a′,ν′) iff ν′ = νpⁿ and a = pⁿa′ ⟹ (u_σ a, ν) ~ (u_σ a′, ν′) with the same n. ✓ In the coordinates (38), the point π̌(F_μ^{-1}(x, χ_x·(a,ν))) = [a mod N x₀^Ẑ, ν/μ] goes to [u_σ a, ν/μ]: the base class in B_p = Ẑ×_(p)/p^Ẑ is translated by [u_σ], the Q^{>0}-coordinate is fixed. ✓ **Orbits:** σ_* fixes x and ν, so it maps C_{x₀} to itself and Γ_p = C_{x₀} ×_{Q^{>0}} R^{>0} to itself; every R^{>0}-orbit in Γ_p is a circle R^{>0}/p^Z (p. 38, N x₀ = p) and σ_* commutes with the flow, so periodic orbits of length log p go to periodic orbits of length log p inside Γ_p. ✓

**Lemma D(iii): PASS-WITH-REPAIRS — MINOR-5(c):** the note prints the packet base as "Aut(F̄_p)^×/Aut(F_p)^"; the source reads **Ẑ×_(p)/p^Ẑ = Aut(F̄_p^×)/Aut(F̄_p)** on p. 33 and p. 38 (verified visually; also [x-06] p. 12 "Aut(F̄_p^×)/Aut(F̄_p)"). Since this displayed formula *is* the note's §4 "structural identity" B_p = coker(Aut_ring(F̄_p) = p^Ẑ ↪ Aut_group(F̄_p^×) = Ẑ×_(p)), the identity should be attributed to Deninger; what the note adds (Consequence 1: mod-p additivity is the device cutting Aut_group down to Aut_ring, by Lemma A) is sound and is the note's own.

---

## 6. Proposition 1 (D1) and its Corollary

### 6.1 The note's statement (verbatim, §5)

> "Let E be any Aut(C)-stable class (all named example classes qualify) and let S ⊆ X₀^E be Aut(C)-stable and flow-invariant. If S contains one periodic point over the prime p, then for EVERY base class [c] ∈ B_p, S contains a closed orbit of length log p with base class [c]. In particular S contains uncountably many closed orbits over p (B_p is an infinite profinite group, hence uncountable — adjudication §2, re-derived there), and no Aut(C)-stable selection achieves one orbit per prime. *Proof:* by §4's coordinates the periodic point lies on an orbit γ with some base class [a]; for [c] = [ua] pick σ with u_σ = u (Lemmas C–D); σ(γ) ⊆ S is a closed orbit of the same length with base class [c]; distinct base classes lie on distinct orbits since the fibers of the (38)-fibration are the Q^{>0}-orbits ([x-03] p. 33)."

### 6.2 The consumed anchor, read verbatim and re-derived: "the fibres are the Q^{>0}-orbits"

[x-03] p. 33 (text and visual): "The set C_{x₀} fibres over the compact group Ẑ×_(p)/p^Ẑ = Aut(F̄_p^×)/Aut(F̄_p), and the fibres are the Q₀^{>0}-orbits in C_{x₀}." and p. 38: "Γ_{x₀} fibres over Ẑ×_(p)/p^Ẑ … with fibres the R^{>0}-orbits in Γ_{x₀}." — the note's citation is exact.
*Re-derivation from (38).* (38), p. 32: (Ẑ×_(p)/N x₀^Ẑ) ×_{p^Z} Q₀^{>0} ≅ C_{x₀}, Q₀^{>0}-equivariantly, where "A ×_Γ B is the quotient of A × B by γ(a,b) = (aγ^{-1}, γb)" and Q₀^{>0} acts on the second factor. The fibration is [a, r] ↦ a mod p^Ẑ, well-defined because p^Z·N x₀^Ẑ = p^Ẑ (for N x₀ = p^f: Z + fẐ = Ẑ, as Z ↠ Ẑ/fẐ = Z/f). Fiber over [a]: {[a pⁿ, r]} = {[a, pⁿ r]} = {[a, r′] : r′ ∈ Q₀^{>0}} = Q₀^{>0}·[a, 1] — exactly one orbit. ✓ Isotropy (p. 33, re-derived): [a, rq] = [a, r] iff ∃ n ∈ Z with a ≡ pⁿa mod N x₀^Ẑ and q = pⁿ, iff pⁿ ∈ p^Z ∩ (p^f)^Ẑ = p^{fZ}, iff q ∈ N x₀^Z ✓; in the suspension, φ^t[P₀, u] = [P₀, ue^t] = [P₀, u] iff e^t ∈ N x₀^Z, so the period is log N x₀ = log p for Spec Z. ✓
*For X₀ = Spec Z the statement is even simpler:* N x₀ = p, and p^Z acts trivially on Ẑ×_(p)/p^Ẑ, so C_{x₀} ≅ B_p × (Q^{>0}/p^Z) as Q^{>0}-sets and **the periodic orbits of Γ_p are in canonical bijection with B_p** (one orbit per base class, and conversely). "Distinct base classes lie on distinct orbits" is the injectivity half of this bijection. ✓

### 6.3 Proof re-derived

Let E satisfy σ_*E = E for all σ ∈ Aut(C) (all six named classes do, §5.4), and S ⊆ X₀^E with σ_*S ⊆ S for all σ and φ^t(S) = S for all t. Suppose y ∈ S is a periodic point over p, i.e. y ∈ Γ^E_p (for E ⊆ E_max this is every periodic point over p, Thm 6.1; for E_tors, "over p" means y ∈ Γ_p, where every point is periodic by (38)–(39)). Let γ be its orbit and [a] ∈ B_p its base class (constant along γ: F_q fixes the base, §6.2). Given [c] ∈ B_p, choose u ∈ Ẑ×_(p) with [u a] = [c] (B_p is a group). By Lemma C (Step 3 of §4.3) choose σ ∈ Aut(C) with u_σ = u. Then σ_*y ∈ S (Aut(C)-stability), σ_*y ∈ Γ_p with base class [u a] = [c] (Lemma D(iii)), and its orbit σ_*γ = σ_*{φ^t y} = {φ^t σ_* y} (Lemma D(i)) is periodic of period log p and contained in S (flow-invariance). Distinct [c] give distinct orbits (§6.2). Since B_p is uncountable (§6.4), S contains uncountably many periodic orbits over p; no such S meets Γ_p in a single orbit. ✓ **Sharpening for Spec Z:** by the bijection of §6.2 the orbit of base class [c] is unique, so the conclusion is **S ⊇ Γ^E_p** — every Aut(C)-stable flow-invariant subset of X₀^E that meets a packet contains the whole packet (for E ⊇ E_f, Γ^E_p = Γ_p by Thm 5.2 / p. 38). Suggested as an added sentence, not a repair.

### 6.4 Uncountability of B_p — re-derived independently of the adjudication

Ẑ×_(p) = ∏_{ℓ≠p} Z_ℓ^× is profinite; p^Ẑ (the closure of ⟨p⟩, the image of the continuous map Ẑ → Ẑ×_(p), n ↦ pⁿ) is a closed subgroup; the quotient B_p is a compact Hausdorff totally disconnected group, i.e. profinite. It is infinite: for any finite set T of odd primes ≠ p, the continuous surjection Ẑ×_(p) → ∏_{ℓ∈T} (Z/ℓ)^×/((Z/ℓ)^×)² ≅ (Z/2)^{|T|} sends p^Ẑ into the subgroup generated by the image of p (order ≤ 2), so B_p surjects onto a group of order ≥ 2^{|T|−1}, unbounded as |T| → ∞. An infinite profinite group has no isolated points (it is homogeneous, and one isolated point would make it discrete, hence finite by compactness), so by the Baire category theorem it is uncountable. ✓ (Agrees with adjudication §2.)

### 6.5 Break attempts

(a) *Within ZFC:* the proof has no free step — Lemma C supplies σ, Lemma D(iii) computes the base class, §6.2 separates orbits, §6.4 counts. No counterexample. (b) *The hypothesis on E:* the Theorem-C cuts E(a₀) are not Aut(C)-stable — σ_*(χ_x^{a₀}) = χ_x^{u_σ a₀} has base class [u_σ a₀], outside E(a₀)'s reachable set a₀·p^Ẑ whenever u_σ ∉ p^Ẑ (adjudication §4 item 5b) — so Proposition 1 does not contradict Theorem C; the note's Scope (c) says exactly this. ✓ (c) *Outside ZFC:* in ZF + all sets of reals measurable, Aut(C) = {id, conj}, u_σ = ±1, and Proposition 1 is vacuous — this is a remark on what "Aut(C)-stable" buys, not a defect.

### 6.6 The Corollary and its scope

The Corollary's bridge — "any selection defined uniformly from the abstract field C and the scheme data … transport of structure then makes every uniformly-defined locus Aut(C)-stable" — is true as a definability schema (a subset defined by a formula in the structure (C as a field, X₀) is fixed setwise by every automorphism of that structure), and the note labels it as a schema, not a theorem ✓. Its reach, however, is narrower than "selections not using C's analytic structure" (the note's Scope (b)): **the dynamical system (X₀, φ^t) itself is defined from (C, |·|), not from the abstract field C** (§7, p. 40), and by §5.3 the Aut(C)-action does not preserve its topology. Hence every selection that consults the topology of X₀ — closures, limits, minimal sets, continuity of a function, the unitary locus's closure of [x-03] §8 — is outside the Corollary, whether or not it looks "analytic". The honest reach: **Proposition 1 rules out every selection definable from the abstract field C and the scheme data alone; it says nothing about selections that use the topology of X₀ or the absolute value on C.** (MINOR-5(b) replacement sentence in §9.) With that sentence the Corollary is correct, and its methodological conclusion — a viable global selection must consume structure on C beyond the abstract field — stands.

**Proposition 1: PASS-WITH-REPAIRS (MINOR-5(a) terminology, MINOR-5(b) scope).** D1 is established at referee grade in ZFC, in the sharpened form S ⊇ Γ^E_p for Spec Z.

---

## 7. The other consumed items: §3 freshman's dream, §4 Consequence 2 (D3), §7 Haar count

### 7.1 §3 — mod-p additivity is F_p-stable but not F_ℓ-stable (ℓ ≠ p)

*Note's text:* "additivity mod p is ( )^p-stable (Prop. 14.7's computation) but not ( )^ℓ-stable for ℓ ≠ p, since (r+s)^ℓ ≢ r^ℓ + s^ℓ mod p."
*Anchors:* Proposition 14.7 (p. 94) "For 0 < α < 1 we have F_p(Y̌_α) = Y̌_α", with proof p. 95 (F_p(I_y) = I_y for the ( )^p-stability, and the ultrametric estimate "≤ max(|…|^{p^ν}, |p|)" for the α-improvement — the note's (F2) description is accurate); [x-03] p. 29 Remark "the resulting class E is not N-invariant".
*Re-derivation, made precise.* Let Y ⊆ {characters at points over p} be the class of mod-p-additive P (after Lemma A: P = [·]∘τ, τ ∈ Hom(F̄_p, k)). For ν ∈ N, F_ν(P) = P∘( )^ν = [·]∘(τ∘( )^ν) = [·]∘(r ↦ τ(r)^ν). By Lemma A(⇒) this is in Y iff r ↦ τ(r^ν) is additive on F̄_p, iff r ↦ r^ν is additive on F̄_p. The polynomial (X+Y)^ν − X^ν − Y^ν vanishes on the infinite field F̄_p (in two variables) iff it is the zero polynomial iff every binomial coefficient C(ν, j), 0 < j < ν, is ≡ 0 mod p, iff ν is a power of p. So **F_ν(Y) ⊆ Y iff ν ∈ p^N, and for ν = ℓ ≠ p prime, F_ℓ(P) ∉ Y for every P ∈ Y** — Y is not N-admissible in the sense of Definition 4.1 for any N₀ containing a prime ℓ ≠ p, which is Deninger's "not N-invariant" and the note's requirement-4 mismatch. ✓ (The note's "(r+s)^ℓ ≢ r^ℓ + s^ℓ mod p" is the right idea stated loosely — MINOR-8; the test r = s = 1 alone does not always detect it, e.g. ℓ = 7, p = 3 has 2^7 ≡ 2 mod 3, so the two-variable polynomial argument is the one to write.)

### 7.2 §4 Consequence 2 — the transport reading collapses to one base class per choice of j (D3)

*Re-derivation.* Fix an isomorphism j : μ^{(p)}(C) → μ^{(p)}(C_p) (exists: both ≅ ⊕_{ℓ≠p} Q_ℓ/Z_ℓ; the set of such j is a torsor under Aut(μ^{(p)}(C_p)) = Ẑ×_(p)). Fix a reference field isomorphism θ : κ(x) → F̄_p ⊆ k = residue field of o_{C_p}. Any group isomorphism κ(x)^× → μ^{(p)}(k) = F̄_p^× is θ∘( )^c for a unique c ∈ Ẑ×_(p) (Aut(F̄_p^×) = Ẑ×_(p), (34)); in particular [·]^{-1}∘j∘χ_x = θ∘( )^{a_j} for a unique a_j ∈ Ẑ×_(p). Then j∘(χ_x·(a,ν)) = [·]∘θ∘( )^{a_j a ν} : κ(x) → o_{C_p}, and by Lemma A this is mod-p additive iff r ↦ θ(r)^{a_j a ν} is a field embedding, iff ( )^{a_j a ν} is a field automorphism of F̄_p composed with θ, iff it is bijective (forces the prime-to-p part of ν to be 1, i.e. ν = pⁿ) and a_j a pⁿ ∈ Aut(F̄_p) = p^Ẑ, iff a ∈ a_j^{-1}·p^Ẑ. So the transported condition selects, in the packet over p, exactly the representatives {χ_x·(a, pⁿ) : a ∈ a_j^{-1}p^Ẑ, n ≥ 0}: the single base class [a_j^{-1}] ∈ B_p, i.e. (by §6.2) **exactly one periodic orbit of Γ_p**, and it is closed under F_p^{±1} but not under F_ℓ (§7.1). As j runs over its Ẑ×_(p)-torsor, a_j runs over Ẑ×_(p) and [a_j^{-1}] over all of B_p. ✓ The selected orbit is the periodic orbit of the Theorem-C cut E(a₀) with a₀ = a_j^{-1} (adjudication §4 item 5b: E(a₀) reaches the base classes a₀·p^Ẑ, i.e. the single class [a₀]).
*Wording (MINOR-7):* the note says "the resulting class is precisely probe A's Theorem C cut E(a₀)". Not as classes: E(a₀) is by construction admissible (closed under all F_ν^{±1}, Definition 4.1), while the transported class is not F_ℓ-closed. What coincides is the selected periodic orbit over p; E(a₀) is the admissible hull of the transported class's packet locus. The conclusion of D3 (one arbitrary point of the torsor per prime; non-canonical; not N-invariant; theory-forfeiting) is unaffected.

### 7.3 §7 — the Haar formal count

*Anchor:* [x-06] Theorem 4.2 (pp. 11–12), verbatim: "The compact subsets Γ_{x₀} ⊂ X₀ consist of periodic orbits of length log N x₀ where N x₀ = |κ(x₀)| … and they are pairwise disjoint. In fact Γ_{x₀} is a fibre space over the compact group Aut(F̄_p^×)/Aut(F̄_p) where p = char κ(x) with fibres the compact orbits in Γ_{x₀}." Also [x-03] p. 38 ("all R^{>0}-orbits in Γ_{x₀} are circles R^{>0}/N x₀^Z").
*Check.* (a) B_p is a compact (profinite) group (§6.4), so it carries a unique translation-invariant probability measure. (b) By Lemma D(iii), σ ∈ Aut(C) acts on B_p by translation by [u_σ], so Haar measure is Aut(C)-invariant. (c) The flow fixes the base (fibers = orbits, §6.2), so the measure on the orbit space of Γ_p is flow-invariant. (d) Every orbit in Γ_p has length log p (Thm 4.2), so any "single-orbit term" depending only on the orbit length is constant on B_p and ∫_{B_p} (const) dHaar = const. ✓ This is a formal identity; the note claims nothing analytic for it and defers everything to DQ-M. **PASS** as stated.

---

## 8. Findings, ranked

| # | Severity | Location | Finding |
|---|---|---|---|
| MAJOR-1 | MAJOR | §4, Lemma A statement and proof | Hypothesis "κ an algebraically closed field of characteristic p" is too broad: the parenthetical "κ^× is prime-to-p torsion" is false for κ ≠ F̄_p, the composite [·]∘τ is undefined there, and the (⇒) proof uses the torsion property. Also (⇐) invokes "W(k) ⊆ o" for a general algebraically closed k, unjustified as stated (and not needed). Fillable: restrict to κ an algebraic closure of F_p (the only case used) and use the elementary (⇐) proof of §2.3, or the on-disk Witt identity plus the map W_p(F̄_p) → o. No downstream statement changes. |
| MINOR-2 | MINOR | §4, Lemma A (⇐) | Cite [x-03] pp. 93–94, 101 for [r+s] − [r] − [s] ∈ pW_p(R) (perfect R) instead of recalling "VF = p"; or drop Witt vectors via §2.3. |
| MINOR-3 | MINOR | §6, Lemma B conclusion | "empty on the periodic locus" is on-disk-correct only for E ⊆ E_max (Thm 6.1); say "empty on every packet Γ_p (for E ⊆ E_max the whole periodic locus)". Note also that the inequality is representative- and domain-independent and holds for every character at every point over a prime, E irrelevant. |
| MINOR-4 | MINOR | §5, Lemma C | Drop "with infinite transcendence degree" (any algebraically closed field of characteristic 0 works); cite [x-03] p. 47 (57) with d_μ = (Ẑ× : κ(G)) and p. 59 (d_μ = 1 for K₀ = Q) for the cyclotomic step; optionally state the exact AC dependence. |
| MINOR-5(a) | MINOR | §5, Lemma D(iii) and Proposition 1 | "closed orbit" → "periodic orbit (a circle R^{>0}/p^Z, [x-03] p. 38)": by the adjudication's result 3 no periodic orbit of X₀ is a closed subset, so "closed orbit" invites a false reading. |
| MINOR-5(b) | MINOR | §5, Lemma D(i) and the Corollary's Scope (b) | State that the Aut(C)-action is by flow-equivariant *bijections, not homeomorphisms* (the topology of X₀ is defined from (C, \|·\|), [x-03] p. 40), so the topological dynamical system is not Aut(C)-invariant and the Corollary's reach is exactly: selections definable from the abstract field C and the scheme data. |
| MINOR-5(c) | MINOR | §4 packet-coordinates paragraph | Typo "Aut(F̄_p)^×/Aut(F_p)^" → "Aut(F̄_p^×)/Aut(F̄_p)" as printed at [x-03] pp. 33, 38 and [x-06] p. 12; and attribute the "structural identity" B_p = coker(Aut_ring ↪ Aut_group) to that displayed formula (the note's addition is Consequence 1's interpretation via Lemma A). |
| MINOR-6 | MINOR | §5, Lemma D(i) | Cite [x-03] Remark 2.7 (p. 21): Deninger records the Aut(S)-action on W_rat(X)(S) commuting with N; Lemma D(i) is its S = spec C case transported through (26) and the colimit. |
| MINOR-7 | MINOR | §4, Consequence 2 | "the resulting class is precisely probe A's Theorem C cut E(a₀)" → "selects precisely the periodic orbit of probe A's Theorem-C cut E(a₀), a₀ = a_j^{-1}; as a class it is the non-admissible (F_ℓ-unstable) core of E(a₀)". |
| MINOR-8 | MINOR | §3 | Replace "(r+s)^ℓ ≢ r^ℓ + s^ℓ mod p" by the precise statement: x ↦ x^ν is additive on F̄_p iff ν is a power of p; hence F_ν(Y) ⊆ Y iff ν ∈ p^N. |

No FATAL finding. No stated theorem is false; every gap is filled above.

## 9. Replacement text (verbatim, for the adjudicator to apply; the note itself is not edited by this report)

**R-MAJOR-1 — Lemma A, replace the statement and proof by:**

> **Lemma A.** Let o be a p-adically complete rank-one valuation ring with algebraically closed fraction field C of characteristic 0 and residue field k, and let κ be an algebraic closure of F_p. Reduction restricts to a bijection μ^{(p)}(o) → μ^{(p)}(k) on prime-to-p roots of unity; write [·] for its inverse, extended by [0] = 0. Let P : κ → o be multiplicative with P(0) = 0 and P(1) = 1. Then
> |P(r+s) − P(r) − P(s)| ≤ |p| for all r, s ∈ κ **iff** P = [·]∘τ for a (necessarily unique) field embedding τ : κ ↪ k.
>
> *Proof.* Since o is p-adically complete, |p| < 1 and |d| = 1 for every integer d prime to p; every root of unity of C lies in o (o is integrally closed); for m prime to p, μ_m(o) is cyclic of order m. *Reduction is bijective on μ^{(p)}:* if ζ^d = 1, p ∤ d, ζ ≡ 1 mod m, then (ζ − 1)(ζ^{d−1} + … + 1) = 0 with the second factor ≡ d, a unit, so ζ = 1; thus μ_m(o) → μ_m(k) is injective from an m-element group into a group of order ≤ m, hence bijective; take the union over m. *Values of P:* every r ∈ κ^× has finite order prime to p, so P(r) ∈ μ^{(p)}(o). *(⇒)* The defect lies in p·o ⊆ m, so P mod m : κ → k is a unital ring homomorphism, injective as κ is a field; call it τ. For r ≠ 0, P(r) and [τ(r)] are prime-to-p roots of unity with the same reduction, hence equal; P(0) = 0 = [τ(0)]. *(⇐)* Let r, s ∈ κ, both nonzero (else the defect is 0), and choose m prime to p with r, s, r+s ∈ μ_m(κ) ∪ {0}. Let ζ_m ∈ o be a primitive m-th root of unity and A = Z[ζ_m] ⊆ o; then P(r), P(s), P(r+s) ∈ A and d := P(r+s) − P(r) − P(s) ∈ A reduces to τ(r+s) − τ(r) − τ(s) = 0, so d ∈ P₀ := ker(A → k). Let f be the (monic, integral) minimal polynomial of ζ_m over Q; A ≅ Z[X]/(f) by Gauss's lemma, f | X^m − 1, and X^m − 1 is separable mod p since p ∤ m; so A/pA ≅ F_p[X]/(f̄) is a product of fields, pA = P₁⋯P_g with distinct maximal P_i, P₀ = P₁ say, and P₁A_{P₁} = pA_{P₁}. Hence d = p·a/s with a ∈ A, s ∈ A ∖ P₀; s has nonzero residue in k, so s ∈ o^×, and d ∈ p·o. ∎
>
> (Equivalently, (⇐) is the identity [a] + [b] − [a+b] ∈ pW_p(κ) of [x-03] pp. 93–94 and 101 — "π(I) ⊂ pW_p(A♭)" for the ideal I generated by [r+s] − [r] − [s] in ZA♭, A♭ perfect — transported into o along the ring homomorphism W_p(F̄_p) → o that extends τ on Teichmüller representatives.)

**R-MINOR-3 — Lemma B, last sentence before "Moreover":** "Hence the class 'archimedean defect ≤ ε at char-p points' is **empty on every packet Γ_p, p prime — for E ⊆ E_max the entire periodic locus ([x-03] Thm 6.1, p. 39; [x-06] Thm 4.2) —** for every ε < 1; the inequality holds for every character at every point over a prime, at every representative in the colimit, and whether the domain is taken to be κ(x) or Z̄."

**R-MINOR-4 — Lemma C, statement and first proof sentence:** "The restriction map Aut(C) → Aut(μ(C)) = Ẑ× is surjective for **any algebraically closed field C of characteristic 0** (in particular the complex numbers). *Derivation:* for K₀ = Q the cyclotomic character Gal(Q̄/Q) → Ẑ× is surjective ([x-03] p. 47, (57) with d_μ = (Ẑ× : κ(G)), and p. 59, d_μ = 1 for K₀ = Q), so u ∈ Ẑ× is realized by some σ₀ ∈ Gal(Q̄/Q), Q̄ the algebraic closure of Q in C; extend σ₀ to C along a transcendence basis of C over Q̄ (fixing the basis) and then to the algebraic closure C of the lifted subfield (Steinitz). Choice enters twice — the transcendence basis and the isomorphism-extension theorem — and is essential: in ZF it is consistent that Aut(C) = {id, conjugation}."

**R-MINOR-5(a) — throughout Lemma D(iii) and Proposition 1:** replace "closed orbit(s)" by "periodic orbit(s)" and add once: "(each a circle R^{>0}/p^Z, [x-03] p. 38; no periodic orbit is a closed subset of X₀ — adjudication §4 item 3)".

**R-MINOR-5(b) — Lemma D(i), add at the end:** "All of this is set-theoretic: the topology of X̊(C) is pointwise convergence for the valuation topology of C ([x-03] §7, p. 40), and a wild σ ∈ Aut(C) is discontinuous on C, so σ acts on (X₀, φ^t) by flow-equivariant bijections that are not homeomorphisms; the topological dynamical system is not Aut(C)-invariant." — and in the Corollary's Scope (b), replace "does NOT constrain selections using C's analytic structure" by "constrains exactly the selections definable from the abstract field C and the scheme data; it says nothing about selections that use the topology of X₀ or the absolute value on C (closures, limits, minimal sets, the unitary closure of [x-03] §8)".

**R-MINOR-5(c) — §4 first paragraph:** "… fibers over B_p := Ẑ×_(p)/p^Ẑ = Aut(F̄_p^×)/Aut(F̄_p) ([x-03] pp. 33, 38 verbatim; [x-06] p. 12) …" and in §0/§4: "The structural identity underneath — B_p = Ẑ×_(p)/p^Ẑ = Aut(F̄_p^×)/Aut(F̄_p), the cokernel of Aut_ring(F̄_p) = p^Ẑ ↪ Aut_group(F̄_p^×) = Ẑ×_(p) — is Deninger's displayed formula; what this note adds is its reading through Lemma A: …".

**R-MINOR-6 — Lemma D(i), first sentence:** "(This is the S = spec C case of the Aut(S)-action on W_rat(X)(S) that [x-03] Remark 2.7, p. 21, records as commuting with the N-action, transported through (26) and the colimit.)"

**R-MINOR-7 — §4 Consequence 2:** "So the faithful transport of the local principle selects, for each j, **precisely the periodic orbit of the adjudicated Theorem-C cut E(a₀) with a₀ = a_j^{-1}**; as a class of characters it is the non-admissible core of E(a₀) (closed under F_p^{±1}, not under F_ℓ, ℓ ≠ p), and E(a₀) is its admissible hull: …"

**R-MINOR-8 — §3:** "The freshman's-dream asymmetry makes it precise: x ↦ x^ν is additive on F̄_p iff ν is a power of p (the polynomial (X+Y)^ν − X^ν − Y^ν vanishes on F̄_p² iff all its binomial coefficients vanish mod p), so by Lemma A the mod-p-additive class Y satisfies F_ν(Y) ⊆ Y iff ν ∈ p^N; for every prime ℓ ≠ p and every P ∈ Y, F_ℓ(P) ∉ Y."

**R-MINOR-2** is subsumed by R-MAJOR-1's parenthetical.

**Optional sharpening (not a repair) — Proposition 1, add:** "For X₀ = Spec Z, p^Z acts trivially on Ẑ×_(p)/p^Ẑ in (38), so the periodic orbits of Γ_p are in canonical bijection with B_p and the conclusion reads: S ⊇ Γ^E_p."

## 10. Verdict block

- **Verdict: PASS-WITH-REPAIRS.** FATAL 0 · MAJOR 1 (MAJOR-1) · MINOR 9 (MINOR-2, -3, -4, -5(a), -5(b), -5(c), -6, -7, -8 — nine distinct findings; the three -5 items share one location cluster).
- **Not re-derived / recalled items, declared:** two textbook facts are labeled [RU-standard] (R1: separability of X^m − 1 mod p for p ∤ m — used in the elementary proof and elementary enough to be checked by differentiation; R2: Gal(Q(ζ_n)/Q) ≅ (Z/n)^× — *not* load-bearing, because the needed conclusion is on disk at [x-03] pp. 47, 59). The identification W_p(F̄_p) ≅ (Z_p[μ^{(p)}])^∧ with Teichmüller = roots of unity is [RU-standard] and is used only in the *alternative* Witt-route proof; the adopted proof avoids it. The ZF remark (Solovay) is [RU-standard] and is scope commentary only.
- **Every source citation in Lemmas A–D and Proposition 1 was opened and says what the note says it says**, with one transcription defect (the packet base group, MINOR-5(c)) and one omission of an available anchor (Remark 2.7, MINOR-6).

**What is now established at referee grade, and its precise scope.** In ZFC, for X₀ = Spec Z and C an algebraically closed field of characteristic 0 (in particular the complex numbers), the following are theorems with every input either on disk in [x-03]/[x-06] at the pages listed in §1 or derived in full above: (A) at a point over p, with coefficients in a p-adically complete rank-one valuation ring o with algebraically closed fraction field, a multiplicative map F̄_p → o is additive modulo p if and only if it is the Teichmüller lift of a field embedding F̄_p ↪ k — so the local principle, read in packet coordinates, selects exactly the Frobenius-orbit of Teichmüller characters, one base class in B_p per choice of an identification μ^{(p)}(C) ≅ μ^{(p)}(C_p), and that choice sweeps B_p (D3); (B) the archimedean threshold reading of the defect bound is empty on every packet Γ_p, for every ε < 1, every character, every p (D2); (C) Aut(C) surjects onto Ẑ×, acts on X₀ by flow-equivariant bijections (not homeomorphisms) preserving each of the six named classes, translates the packet base B_p = Ẑ×_(p)/p^Ẑ = Aut(F̄_p^×)/Aut(F̄_p) transitively, and consequently every Aut(C)-stable flow-invariant subset of X₀^E (E any of the named classes) that meets a packet Γ_p contains the whole of Γ^E_p — uncountably many periodic orbits of length log p (D1). The scope limits are exactly two: D1 constrains only selections definable from the abstract field C and the scheme data (nothing that uses the topology of X₀ or the absolute value of C), and its content depends on the axiom of choice; D2 constrains only uniform-threshold conditions on the archimedean defect (as the note itself says). The trichotomy D1–D3 therefore stands as stated in the note's §0, with the repairs of §9 applied.

— end of referee report F —
