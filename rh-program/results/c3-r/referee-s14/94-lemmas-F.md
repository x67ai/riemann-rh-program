# REFEREE REPORT F — probe 9.4 note, Lemmas A–D and Proposition 1 (the transplant trichotomy D1–D3)

**Program:** RH program, direction C3-r (reduced recommission). **Date:** 2026-09-02 (Session 14). **Referee:** F (one of two independent referees on this item; the other is a different model, and nothing below assumes anything about their findings — standing order 7).
**Item under review:** `results/c3-r/probe-9.4-note.md` (dated 2026-08-26, Session 8), §§3–7: Lemma A (§4), Lemma C, Lemma D and Proposition 1 (§5), Lemma B (§6), the freshman's-dream N-invariance argument (§3) and the Haar formal count (§7). The note's own press points (§8 item 1): Lemma D(ii) for E_max's (Image) condition; the "fibers = Q^{>0}-orbits" consumption in Proposition 1; Lemma A's converse.
**Method:** the adjudication `results/c3-r/probe-9.3-adjudication.md` and the whole note were read first; every cited source location was opened on disk (pdftotext extraction made fresh this session, plus one page rendered to PNG where the text layer drops overlines); every step was re-derived below in full; each gap was attacked both ways (fill / break). Nothing load-bearing is from memory; the two places where a classical background theorem is consumed without an on-disk source are labeled [RU] and their weight is stated.
**Rules applied:** standing order 5 (nothing load-bearing from memory), standing order 7 (dual novelty check — not this report's job, but no finding is softened on the expectation that the other referee will catch it), U.S. English, honest labels.

**Headline (details and the verdict block in §10):** PASS-WITH-REPAIRS. 0 FATAL / 1 MAJOR / 12 MINOR. The single MAJOR is against Lemma A's *statement*, not against anything the note uses: as written for "an algebraically closed field κ of characteristic p" the lemma is false — its parenthetical "κ^× is prime-to-p torsion" fails for every algebraically closed κ ≠ F̄_p, its right-hand side is then undefined under the note's own definition of the Teichmüller section, and under the natural extended reading the (⇒) direction has counterexamples (§3.5). Every use in the note has κ = F̄_p, where the lemma is correct and is re-derived here with a fully elementary proof of the converse that removes the Witt-vector recollection. Lemmas B, C, D and Proposition 1 are re-derived line by line and hold as stated, with wording/citation repairs only; the fibers-are-orbits anchor is verified verbatim at [x-03] p. 33 *and* p. 38; the uncountability of B_p is re-derived two ways; Lemma D(ii)'s (Image) stability is verified for all six named classes.

---

## 1. Sources read this session (printed page = PDF page for [x-03] and [x-06]; verified on the page footers)

| tag | file | pages read verbatim | used for |
|---|---|---|---|
| [x-03] | `fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf` (arXiv:1807.06400v4, 119 pp.) | 5–6 (intro); 26–29 (§4: Def. 4.1, (Tors), (Image), the six example classes, both Remarks, (Stable Image)); 31–34 (§5: (32)–(47), Thm 5.2 with the "If e.g. E ⊃ E_f then C^E_{x0} = C_{x0}" clause); 38–40 (§6: suspension, Γ_{x0}, the fibration line, Thm 6.1, the S4 question); 89–90 (§14 opening, Defs. 14.1–14.2); 93–95 ((170)–(172), Def. 14.5, Remark 14.6, Prop. 14.7 with proof); 99–101 (Def. 14.12 = (183), the "I do not know how to transport" Remark, Prop. 14.13, Prop. 14.14 with proof); 113–116 (Thm 15.6 with proof of 6), Prop. 15.7, Prop. 15.8). Page 33 additionally rendered to PNG (`pdftoppm -r 110`) to read the overlines in the displayed formula. | packet coordinates, class definitions, the local principle, Thm 15.6 |
| [x-06] | `fetched/x-06-deninger-2024-primes-knots-and-periodic-orbits.pdf` (arXiv:2301.11643, 17 pp.) | 10–13 (Thm 4.1 with the G- and F_ν-actions written out; the "too many periodic orbits ... In the local p-adic situation below, we know the right modification" paragraph; Thm 4.2; Thms 4.3–4.4; the Steinberg paragraph) | orbit lengths in Γ_{x0}; the group and Frobenius actions |
| [r3s-08] | `fetched-r3/r3s-08-morishita-deninger-cc-bridge-2508.15971.pdf` | not needed for this item (the note does not cite it in §§3–7); the adjudication's flag "never cite [r3s-08] §2.2 for the identification of the packet" is respected | — |
| [D25] | `fetched-r3/r3s-22-...-2508.05329v1-SESSION8-FETCH.pdf` | not needed for this item (Road 1 only) | — |
| program | `results/c3-r/probe-9.3-adjudication.md` (all 125 lines, including the three Session-14 bookkeeping paragraphs); `results/c3-r/probe-9.4-note.md` (all 154 lines); `results/corpus-routing.md` header caveats | context; anchors already verified there are re-verified here where consumed |

**Verbatim quotations consumed below** (page in brackets; overlines restored from the PNG where the text layer drops them):

- [x-03, 27] Def. 4.1: "A class E of characters χ : κ^× → C^× on algebraically closed fields κ is (N_0−)admissible if for any σ ∈ Aut κ resp. ν ∈ N_0 the character χ is in E if and only if χ ∘ σ resp. χ_ν = χ ∘ ( )^ν is in E. Moreover the characters in E should satisfy (Tors)."
- [x-03, 27] "(Tors) the group ker(χ)_tors = ker(χ|_{µ(κ)}) is finite and |(ker χ)_tors| ∈ N_0." — "(Image) Only if char κ > 0. If χ(κ^×) is torsion, then κ^× is torsion as well, i.e. κ^× ⊗ Q ≠ 0 implies χ(κ^×) ⊗ Q ≠ 0."
- [x-03, 28–29] Example: "1) E_tors : (Tors) holds 2) E_max : (Tors) and (Image) hold 3) E_f : (Tors) and ker χ is finite. Equivalently: |ker χ| ∈ N_0 4) E_fg : (Tors) and ker χ is finitely generated 5) E_fd : (Tors) and ker χ ⊗ Q is finite dimensional 6) E_fd0 : (Tors) and (ker χ|_{κ(x_0)^×}) ⊗ Q is finite dimensional where x_0 = π(x)".
- [x-03, 29] Remark: "Incidentally, in the p-adic case where we will deal with multiplicative maps P into a p-adic valuation ring and N_0 = p^Z, the right condition E is the following: P is additive mod p. This can be rephrased in terms of absolute values and translated to the case where C is the complex number field. However the resulting class E is not N-invariant."
- [x-03, 31] "For every point x ∈ X over x_0 the residue field κ(x) is an algebraic closure of κ(x_0)." and (32): "i_x : µ^{(p)}(K) = µ^{(p)}(O_{X,x}) → κ(x)^×" (an isomorphism).
- [x-03, 32] (34): "N x_0^Ẑ = Gal(κ(x)/κ(x_0)) ↪ Aut(κ(x)^×) = Ẑ^×_{(p)}." — (35): "Ẑ^×_{(p)} × N_0 ↠ S, (a, ν) ↦ χ_x · (a, ν) := χ_x ∘ ( )^a ∘ ( )^ν. Two elements (a, ν) and (a′, ν′) are in the same fibre of this map if and only if ν′ = νp^n and a = p^n a′ for some n ∈ Z."
- [x-03, 32–33] (38): "(Ẑ^×_{(p)}/N x_0^Ẑ) ×_{p^Z} Q_0^{>0} → C_{x_0}" (a Q_0^{>0}-equivariant bijection); "It follows that all points P_0 ∈ C_{x_0} have isotropy subgroup (Q_0^{>0})_{P_0} = N x_0^Z."
- [x-03, 33] "The set C_{x_0} fibres over the compact group Ẑ^×_{(p)}/p^Ẑ = Aut(F̄_p^×)/Aut(F̄_p), and the fibres are the Q_0^{>0}-orbits in C_{x_0}." — "The maps (37), (38) and the fibration map depend on our choices of x and ι."
- [x-03, 34] Thm 5.2: "Let E be an admissible class with E ⊂ E_max. ... For any point P_0 ∈ C^E_{x_0} the isotropy group of P_0 is (Q_0^{>0})_{P_0} = N x_0^Z where N x_0 = |κ(x_0)|. If e.g. E ⊃ E_f then C^E_{x_0} = C_{x_0}."
- [x-03, 38] §6: "X_0 = X̌_0(C)_E ×_{Q_0^{>0}} R^{>0}. It is the quotient of X̌_0(C)_E × R^{>0} by the right Q_0^{>0}-action given by (P_0, u)q = (P_0 q, q^{−1}u) = (F_q(P_0), q^{−1}u)" — "Thus all R^{>0}-orbits in Γ_{x_0} are circles R^{>0}/N x_0^Z and Γ_{x_0} fibres over Ẑ^×_{(p)}/p^Ẑ = Aut(F̄_p^×)/Aut(F̄_p) with fibres the R^{>0}-orbits in Γ_{x_0}."
- [x-03, 39] Thm 6.1: "For any point x_0 ∈ Γ^E_{x_0} the isotropy group of x_0 is (R^{>0})_{x_0} = N x_0^Z." and "Any periodic orbit γ in X_0 is contained in Γ^E_{x_0} for a uniquely determined point x_0 of X_0 with finite residue field."
- [x-03, 6] "Incidentally, if we consider points of W_rat(X) with values in rings without "small multiplicative subgroups" like the complex number field C this process does not give more points." (This sentence is on p. 6, not p. 5 — see finding M-7.)
- [x-03, 89] "In the following we only consider the monoid N_0 generated by p i.e. the F_p = ( )^p action."
- [x-03, 94] Def. 14.5: "Y̌_α = {(x, y, P̌_y) ∈ X̌_c(o) | |P̌_y(r + s) − P̌_y(r) − P̌_y(s)| ≤ α for r, s ∈ Ô^♭_{{x},y}}. ... For α = 1/p we are looking at multiplicative maps P̌_y which mod p are also additive. Set Y̌ = Y̌_{1/p}." — (172): "Choose an element ω_α ∈ o with α ≤ |ω_α| < 1. Then (x, y, P̌_y) ∈ Y̌_α gives a ring homomorphism P̌_y : ZÔ^♭_{{x},y} → o with P̌_y(I_y) ⊂ ω_α o and hence an induced ring homomorphism W_p(P̌_y) : W_p(Ô^♭_{{x},y}) = lim_n ZÔ^♭_{{x},y}/I_y^n → lim_n o/ω_α^n = o."
- [x-03, 95] proof of Prop. 14.7: "= |(P̌_y(r + s) − P̌_y(r) − P̌_y(s))^{p^ν} + pc| for some c ∈ o ≤ max(|P̌_y(r + s) − P̌_y(r) − P̌_y(s)|^{p^ν}, |p|) ≤ max(α^{p^ν}, 1/p)."
- [x-03, 99] Remark after Def. 14.12: "I do not know how to transport such conditions to the points of X̌(C), where X is a scheme of finite type over spec Z and C is the complex number field."
- [x-03, 100] Prop. 14.14: "there is a natural bijection between (continuous) multiplicative maps χ : lim_{( )^p} A → o with χ(1) = 1, χ(0) = 0 for which the composition χ̄^♭ : A^♭ ≅ lim_{( )^p} A → o → o/p is additive and (continuous) ring homomorphisms χ^♭ : A^♭ → o^♭."
- [x-03, 113] "For (x, y) = (s, s) the continuous local ring homomorphisms P̂^♭_y : κ → o^♭ with P̂^♭_y(f) ≠ 0 for all 0 ≠ f ∈ lim_{( )^p} κ ≅ κ are simply the ring homomorphisms P̂_y : κ ↪ k ⊂ o^♭". Thm 15.6 1): "There is a natural G × Aut(o) × ⟨F_p⟩-equivariant identification Y^⋄ = Hom_cont(ô^♭_K, o^♭)"; [114] "Y^⋄_s := pr_X^{−1}(s) = Hom(κ, k)"; (224) "Y^⋄_{0 s_0} := pr_{X_0}^{−1}(s_0) → ∐_{τ_0} {0}/o^×_{K_0} = Hom(κ_0, k)"; 6) "The only periodic (i.e. finite) orbit of the F_p-action on Y^⋄_0 is Y^⋄_{0 s_0}. It has order log_p N(π_0) = r if q = p^r."
- [x-06, 11] Thm 4.1: "Here σ ∈ G acts on X̊(C) via (x, P^×)σ = (x^σ, P^× ∘ σ) and ν ∈ N acts G-equivariantly via F_ν(x, P^×) = (x, P^× ∘ ( )^ν)." — "In the local p-adic situation below, we know the right modification to make. However in the global case presently we can only impose an "admissible" condition E".
- [x-06, 11–12] Thm 4.2: "{x_0 ∈ X_0^E | φ^t(x_0) = x_0 for some t > 0} = ∐_{x_0} Γ_{x_0}. Here x_0 runs over the closed points of X_0 ... The compact subsets Γ_{x_0} ⊂ X_0 consist of periodic orbits of length log N x_0 where N x_0 = |κ(x_0)| (= |R_0/m_0|) and they are pairwise disjoint. In fact Γ_{x_0} is a fibre space over the compact group Aut(F̄_p^×)/Aut(F̄_p) where p = char κ(x) with fibres the compact orbits in Γ_{x_0}."

---

## 2. Preliminaries re-derived (shared by Lemmas A–D and Proposition 1)

Throughout, X_0 = Spec Z, x_0 = (p), x a point of X = Spec Z̄ over x_0, κ(x) = F̄_p ([x-03, 31]), K = Q̄, G = Gal(Q̄/Q), C the complex numbers (or any algebraically closed field of characteristic 0; the note's Lemma C states the latitude). N_0 = N (the global monoid), so Ẑ_{(p)} = ∏_{ℓ≠p} Z_ℓ and Ẑ^×_{(p)} = ∏_{ℓ≠p} Z_ℓ^×.

**P1 (χ_x is an isomorphism onto µ^{(p)}(C)).** i_x : µ^{(p)}(Q̄) → F̄_p^× is an isomorphism ([x-03, 31] (32)). ι : µ(Q̄) → µ(C) is injective by choice [x-03, 31]. Both groups are ≅ Q/Z; for each n the n-torsion µ_n has exactly n elements on both sides (algebraically closed fields of characteristic 0), so the injective map µ_n(Q̄) → µ_n(C) is bijective, hence ι is bijective. Thus χ_x := ι ∘ i_x^{−1} : F̄_p^× → µ^{(p)}(C) is an isomorphism of groups. (The note's "divisible-image" argument — a nonzero divisible subgroup of Q_ℓ/Z_ℓ is everything, since every proper subgroup is finite cyclic — gives the same conclusion; the torsion count is one line shorter.) ✓

**P2 (Aut of prime-to-p torsion; power maps commute with homomorphisms).** For T ≅ ⊕_{ℓ≠p} Q_ℓ/Z_ℓ, End(T) = ∏_{ℓ≠p} End(Q_ℓ/Z_ℓ) = ∏_{ℓ≠p} Z_ℓ = Ẑ_{(p)}, acting by y ↦ y^u (for y of order d, y^u := y^{u mod d}); Aut(T) = Ẑ^×_{(p)}. This is [x-03, 32] (34)'s "Aut(κ(x)^×) = Ẑ^×_{(p)}" specialized. For any homomorphism h : T → T′ of prime-to-p torsion groups and u ∈ Ẑ_{(p)}: h(y^u) = h(y^{u mod d}) = h(y)^{u mod d} = h(y)^u, since ord h(y) | d. ✓

**P3 (packet coordinates and base class).** By (35)–(38), fixing (x, ι), every point of C_{x_0} ⊂ X̌_0(C)_{E_tors} is [a, q] := F_{ν′}^{−1} π((x, χ_x ∘ ( )^a ∘ ( )^ν)) for q = ν/ν′, a ∈ Ẑ^×_{(p)}, uniquely up to the ×_{p^Z} identification [a, q] = [a p^{−n}, p^n q] (with p^Ẑ = N x_0^Ẑ since N x_0 = p). The **base class** of [a, q] is [a] ∈ B_p := Ẑ^×_{(p)}/p^Ẑ; it is well defined on C_{x_0} because a p^{−n} ≡ a mod p^Ẑ. The Q_0^{>0}-action is [a, q]·q′ = [a, qq′] (§6 definition, [x-03, 38]), so **the base class is constant on Q^{>0}-orbits**, and **the fiber of [a, q] ↦ [a] over a given class is exactly one Q^{>0}-orbit**: two points [a, q], [a′, q′] with [a] = [a′] satisfy a′ = a p^{m} with m ∈ Ẑ; but in Ẑ^×_{(p)}/N x_0^Ẑ = Ẑ^×_{(p)}/p^Ẑ that already makes a′ = a, so [a′, q′] = [a, q′] = [a, q]·(q′/q). This is exactly Deninger's sentence "the fibres are the Q_0^{>0}-orbits" ([x-03, 33]), re-derived; for general x_0 with N x_0 = p^f the same computation runs with p^Ẑ/p^{fẐ} ≅ Z/f on both sides, which is why (39) is written with ×_{p^{Z/deg x_0}}. In the suspension, [P_0, u] has the base class of P_0, constant along R^{>0}-orbits since [P_0, u] = [F_q P_0, q^{−1}u] and F_q preserves the base; [x-03, 38] states the suspended version verbatim ("Γ_{x_0} fibres over Ẑ^×_{(p)}/p^Ẑ ... with fibres the R^{>0}-orbits in Γ_{x_0}"). **Distinct base classes ⇒ distinct orbits.** ✓

**P4 (orbit length).** Isotropy of every point of C_{x_0} is N x_0^Z = p^Z ([x-03, 33]); in the suspension the flow is φ^t[P_0, u] = [P_0, e^t u] and [P_0, p u] = [F_p P_0, u], so [P_0, e^t u] = [P_0, u] iff e^t ∈ p^Z: every orbit in Γ_p is periodic of least period log p ([x-03, 39] Thm 6.1; [x-06, 12] Thm 4.2 verbatim "periodic orbits of length log N x_0"). ✓

**P5 (B_p is uncountable), two derivations.** (i) The adjudication's: for a finite set T of odd primes ≠ p, Ẑ^×_{(p)} ↠ ∏_{ℓ∈T} (Z/ℓ)^×/((Z/ℓ)^×)^2 ≅ (Z/2)^{|T|}; p maps to one element, so p^Ẑ maps into a subgroup of order ≤ 2 and B_p surjects onto a group of order ≥ 2^{|T|−1}; hence B_p is an infinite compact Hausdorff group, so it has no isolated points (homogeneity; an isolated point in a compact group forces finiteness), so it is a nonempty perfect compact Hausdorff space, hence uncountable (Baire). ✓ (ii) Sharper and Baire-free: take T = all odd primes ≠ p; Ẑ^×_{(p)} ↠ ∏_{ℓ∈T} {±1} = (Z/2)^T via the Legendre symbols; the closure of the cyclic group generated by the image of p is a subgroup of order ≤ 2; so B_p ↠ (Z/2)^T/(order ≤ 2), which has cardinality 2^{ℵ_0}. ✓ Either way |B_p| = 2^{ℵ_0}.

**P6 (the identity B_p = Aut(F̄_p^×)/Aut(F̄_p)).** (34) with N x_0 = p: Gal(F̄_p/F_p) = Aut(F̄_p) ≅ Ẑ ↪ Aut(F̄_p^×) = Ẑ^×_{(p)}, 1 ↦ p, image p^Ẑ. So Ẑ^×_{(p)}/p^Ẑ = Aut(F̄_p^×)/Aut(F̄_p), as displayed on [x-03, 33] and [x-03, 38] (PNG-verified). The note's §4 transcribes this as "Aut(F̄_p)^×/Aut(F_p)^" — a garbled rendering (finding M-1).

---

## 3. Lemma A (§4 of the note): mod-p-additive multiplicative maps = Teichmüller lifts of field embeddings

### 3.1 The statement as written

"Let o be as in §2 (residue field k algebraically closed of char p), κ an algebraically closed field of characteristic p, and P: κ → o multiplicative with P(0) = 0, P(1) = 1, whose restriction to κ^× is a group homomorphism into o (values automatically in µ^{(p)}(o), the prime-to-p roots of unity, since κ^× is prime-to-p torsion). Then |P(r+s) − P(r) − P(s)| ≤ |p| for all r, s ∈ κ **iff** P = [·]∘τ for a unique field embedding τ: κ ↪ k, where [·] is the Teichmüller section of the reduction µ^{(p)}(o) ≅ µ^{(p)}(k)."

Here o is "a p-adically complete rank-1 valuation ring with algebraically closed quotient field C of characteristic 0 and residue field k of characteristic p" (note §2, matching [x-03, 89]: "Let o be a p-adically complete rank one valuation ring with quotient field C, maximal ideal m and residue field k of characteristic p"), and the absolute value is normalized with |p| = 1/p, which is what makes Deninger's "α = 1/p" the mod-p-additivity threshold ([x-03, 94] Def. 14.5, "For α = 1/p we are looking at multiplicative maps P̌_y which mod p are also additive").

### 3.2 Where the statement is wrong: the generality "any algebraically closed κ of characteristic p"

The parenthetical justification is false unless κ is algebraic over F_p: for κ = F̄_p(t)^{alg} the element t has infinite order in κ^×. (κ^× is torsion iff every element is algebraic over F_p, i.e. iff κ = F̄_p up to isomorphism.) Two consequences for the lemma as stated:

1. The right-hand side is **undefined** for κ ≠ F̄_p: the note defines [·] only on µ^{(p)}(k) ∪ {0}, and for τ: κ ↪ k with τ(κ) ⊄ F̄_p, "[·]∘τ" has no meaning.
2. Under the natural extended reading ([·] = the full multiplicative Teichmüller section k → o, obtained from W(k) → o), the (⇒) direction is **false** — see the break attempt in §3.5.

Every use of Lemma A in the note has κ = κ(x) = F̄_p ([x-03, 31]: "the residue field κ(x) is an algebraic closure of κ(x_0)", with κ(x_0) = F_p for X_0 = Spec Z; and in the local consistency check the residue field of o_K, K an algebraic closure of a p-adic field, is likewise F̄_p — that is the κ of [x-03, 113]). So the repair is a restriction of hypothesis with no downstream effect. **Finding MAJ-1** (severity MAJOR; false-as-stated in its declared generality, fully repaired by restricting κ; replacement text in §10).

### 3.3 Re-derivation of Lemma A for κ = F̄_p (this is the lemma the note actually uses)

**Setting.** κ = F̄_p; o, k, C, m as above; P: F̄_p → o with P(0) = 0, P(1) = 1, P|_{F̄_p^×} a homomorphism into o^× (a homomorphism into the multiplicative monoid of o with P(1) = 1 lands in o^×, since P(r)P(r^{−1}) = 1).

**Step 0 — values are prime-to-p roots of unity.** Every r ∈ F̄_p^× lies in some F_q^×, q = p^n, so r^{q−1} = 1 with p ∤ q − 1; hence P(r)^{q−1} = 1 and P(r) ∈ µ^{(p)}(o). ✓ (This is where κ = F̄_p is used, and it is used again in the (⇒) direction.)

**Step 1 — reduction is injective on µ^{(p)}(o) ∪ {0}, and bijective onto µ^{(p)}(k) ∪ {0}.** Let ζ ∈ o with ζ^d = 1, p ∤ d, and ζ ≡ 1 mod m. Then 0 = ζ^d − 1 = (ζ − 1)(ζ^{d−1} + ⋯ + ζ + 1), and ζ^{d−1} + ⋯ + 1 ≡ d mod m is a unit of o because |d| = 1 (d is prime to p, and Z ⊂ o with |n| = 1 for p ∤ n since o is a valuation ring of a characteristic-0 field whose maximal ideal contains p). Hence ζ = 1. So the reduction homomorphism µ^{(p)}(o) → µ^{(p)}(k) is injective; for each d prime to p it maps the d-element group µ_d(o) (C algebraically closed of characteristic 0) injectively into the d-element group µ_d(k) (k algebraically closed of characteristic p), hence bijectively. Therefore the Teichmüller section [·]: µ^{(p)}(k) ∪ {0} → µ^{(p)}(o) ∪ {0} exists and is unique, and it is multiplicative. ✓ (The note's argument is the same; its surjectivity step via divisibility is replaced by the count.)

**Step 2 — (⇒).** Suppose |P(r+s) − P(r) − P(s)| ≤ |p| for all r, s. In a rank-1 valuation ring, |y| ≤ |p| ⟺ y/p ∈ o ⟺ y ∈ p·o, and p·o ⊆ m. Hence P̄ := (P mod m): F̄_p → k is additive; it is multiplicative and sends 0 ↦ 0, 1 ↦ 1 by hypothesis; so P̄ is a unital ring homomorphism from a field, hence injective; call it τ. For r ∈ F̄_p^×: P(r) ∈ µ^{(p)}(o) (Step 0) and [τ(r)] ∈ µ^{(p)}(o) have the same reduction τ(r), hence are equal (Step 1). For r = 0 both sides are 0. So P = [·]∘τ, and τ = P mod m is determined by P (uniqueness). ✓

**Step 3 — (⇐), elementary proof (no Witt vectors).** Let τ: F̄_p ↪ k be a field embedding and P = [·]∘τ. We must show [τ(r+s)] − [τ(r)] − [τ(s)] ∈ p·o for all r, s ∈ F̄_p. Put ζ = [τ(r)], η = [τ(s)] ∈ µ^{(p)}(o) ∪ {0}; choose q = p^n with r, s ∈ F_q, so ζ^q = ζ and η^q = η (either ζ = 0 or ζ^{q−1} = 1). Set x = ζ + η.

(a) *x^q ≡ x mod p·o.* By the binomial theorem, (u+v)^p ≡ u^p + v^p mod p·o for all u, v ∈ o. If u ≡ v mod p^i·o with i ≥ 1 then u^p ≡ v^p mod p^{i+1}·o (write u = v + p^i w; the binomial terms with 1 ≤ j ≤ p−1 carry a factor p·p^{ij} ∈ p^{i+1}o, and the last term p^{ip}w^p ∈ p^{ip}o ⊆ p^{i+1}o). Hence by induction on m, x^{p^m} ≡ ζ^{p^m} + η^{p^m} mod p·o for all m ≥ 0; with m = n this reads x^q ≡ ζ + η = x mod p·o.

(b) *The sequence x_j := x^{q^j} converges p-adically to an element ω with ω^q = ω and ω ≡ x mod p·o.* From x_1 ≡ x_0 mod p·o and the lifting statement in (a) applied n times, x_{j+1} = x_j^q ≡ x_{j−1}^q = x_j mod p^{j+n}·o ⊆ p^{j+1}·o for all j ≥ 1. So (x_j) is p-adically Cauchy; o is p-adically complete and separated (∩_n p^n o = 0 in a rank-1 valuation ring with |p| < 1), so x_j → ω ∈ o. Multiplication is continuous, so ω^q = lim x_j^q = lim x_{j+1} = ω. All x_j ≡ x mod p·o and p·o = {|y| ≤ |p|} is closed, so ω ≡ x mod p·o.

(c) *ω = [τ(r+s)].* From ω^q = ω, either ω = 0 or ω^{q−1} = 1, i.e. ω ∈ µ^{(p)}(o) ∪ {0}. Its reduction is ω̄ = x̄ = τ(r) + τ(s) = τ(r+s). By Step 1, ω = [τ(r+s)].

Hence [τ(r+s)] − [τ(r)] − [τ(s)] = ω − x ∈ p·o, i.e. |P(r+s) − P(r) − P(s)| ≤ |p|. (r = 0 or s = 0 is trivial.) ∎

This replaces the note's "[a] + [b] − [a+b] ∈ V W(k) = p W(k) in the Witt ring W(k) ⊆ o (first ghost/component coordinates agree; V F = p on Witt vectors of a perfect ring)". That argument is correct — the reduction W(k) → k is a ring homomorphism of which [·] is a set-theoretic section, so the element lies in ker = V W(k), and V W(k) = p W(k) because F is bijective on W(k) for perfect k and V F = p — but it consumes (i) the existence of a Teichmüller-compatible ring embedding W(k) ⊆ o and (ii) the identities V F = p, F bijective, neither of which is on disk; under standing order 5 both are [RU]. The elementary proof above uses only the binomial theorem, p-adic completeness of o, and Step 1, all derived here. **Finding MIN-2** (MINOR; the note's converse is right but rests on recalled Witt-vector facts; the replacement text in §10 makes it source-free). The note's press point "Lemma A's converse (the V F = p Witt identity)" is thereby discharged.

**Uniqueness of τ and the identification with Thm 15.6.** τ = P mod m. Any field embedding F̄_p ↪ k lands in the algebraic closure of F_p inside k, so Hom(F̄_p, k) = Aut(F̄_p) ≅ Ẑ (Frobenius closure), a torsor under Aut_ring(F̄_p) — exactly Deninger's Y^⋄_s = Hom(κ, k) at the closed point ([x-03, 114]) and, mod Galois, Y^⋄_{0 s_0} = Hom(κ_0, k) ([x-03, 114] (224)), which is one F_p-orbit of size r = [κ_0 : F_p] ([x-03, 114] Thm 15.6 6), proof on p. 115: "It is clear that Y^⋄_{0 s_0} → Hom(κ_0, k) is a periodic orbit of order r"). The note's "Consistency" paragraph is verified. Deninger's own reduction at (s, s) — "the continuous local ring homomorphisms P̂^♭_y : κ → o^♭ ... are simply the ring homomorphisms P̂_y : κ ↪ k ⊂ o^♭" ([x-03, 113]) — is the same statement in tilted form: for κ = F̄_p a ring homomorphism into o^♭ takes values in the roots of unity of o^♭, i.e. in k ⊂ o^♭. ✓

### 3.4 Consequence 1 (§4) checked

"The o-valued unit-exponent characters at a char-p point form a torsor under Aut_group(κ^×) = Ẑ^×_{(p)}": an injective homomorphism F̄_p^× → o^× has torsion image of prime-to-p orders, hence lands in µ^{(p)}(o) ≅ µ^{(p)}(k) = F̄_p^× (Step 1 with k ⊇ F̄_p), and an injective endomorphism of a group whose n-torsion is finite of size n for every n prime to p is bijective; so the set is Iso(F̄_p^×, µ^{(p)}(o)), a torsor under Aut(F̄_p^×) = Ẑ^×_{(p)} (P2). ✓ "Imposing mod-p additivity cuts this to the torsor Hom_ring(κ, k) under Aut_ring(κ) = Ẑ": Lemma A. ✓ "Globally, the C-valued packet base is B_p = Ẑ^×_{(p)}/p^Ẑ = coker(Aut_ring ↪ Aut_group)": P6. ✓ The identity itself is Deninger's ([x-03, 33]; the note's novelty block already records this).

### 3.5 Break attempt on the general-κ statement (succeeds; this is why MAJ-1 is a finding and not a quibble)

Take κ = k not algebraic over F_p (e.g. k = F̄_p(t)^{alg}) and o with residue field k (e.g. the valuation ring of the completion of an algebraic closure of Q_p(t) with the Gauss norm; its residue field is F̄_p(t)^{alg} = k). By [x-03, 100] Prop. 14.14 (read verbatim, proof pp. 100–101; with A^♭ replaced by the perfect ring κ the argument is the same: Hom_mult(κ, o) = Hom_mult(κ, o^♭) via ♯ and (170), and mod-p-additivity of χ ⟺ χ^♭ is a ring homomorphism), the multiplicative maps P: κ → o with P mod p additive, P(0) = 0, P(1) = 1 correspond bijectively to ring homomorphisms h: κ → o^♭. When κ = F̄_p every such h lands in µ(o^♭) = k^× ∪ {0} ⊂ o^♭ and is a Teichmüller lift — that is [x-03, 113]'s sentence and Lemma A. When κ = k is not algebraic over F_p there are ring homomorphisms h: k → o^♭ lifting id_k that are not the Teichmüller section: choose a transcendence basis T of k over F_p, lift each t ∈ T to any unit t̃ ∈ (o^♭)^× reducing to t, extend F_p(T) → Frac(o^♭) to k (Frac(o^♭) is algebraically closed as the tilt of an algebraically closed complete field [RU, standard]; the image lies in o^♭ because o^♭ is integrally closed), then compose with an automorphism of k/F_p(T) to make the reduction the identity; different choices of the lifts t̃ (e.g. t̃ versus t̃(1+ϖ), ϖ ∈ m^♭ nonzero) give different h. The corresponding P = ♯∘h satisfies |P(r+s) − P(r) − P(s)| ≤ |p| and P mod m = id_k = τ, yet P ≠ [·]∘τ because P mod p = pr_0∘h ≠ [·] mod p. So the (⇒) direction fails for every algebraically closed κ ≠ F̄_p that embeds in k. (The step "Frac(o^♭) is algebraically closed" is recalled and labeled [RU]; it is not needed for the finding itself, since the statement is already ill-defined for κ ≠ F̄_p under the note's definition of [·] — §3.2 item 1 — and the false parenthetical is a plain error. The counterexample only shows that no reading of the general statement can be rescued.)

### 3.6 Verdict on Lemma A

**PASS-WITH-REPAIRS.** For κ = F̄_p (the only case used) the lemma is correct; both directions are re-derived above, the converse now without any recalled input. The statement must be restricted to κ = F̄_p (MAJ-1) and the converse's proof should be replaced by §3.3 Step 3 (MIN-2). The note's press point on the converse is discharged.

---

## 4. Lemma B (§6 of the note): the archimedean threshold selects nothing on the packets (D2)

### 4.1 Statement as written

"For X_0 = Spec Z, at every point of every packet (any prime p, any character P in any class E ⊆ E_tors), the test r = s = 1 gives |P(1̄+1̄) − P(1̄) − P(1̄)| = |P(2̄) − 2| ≥ 1, since P(2̄) is a root of unity or 0 (κ(x)^× is torsion; 0 occurs iff p = 2). Hence the class 'archimedean defect ≤ ε at char-p points' is empty on the periodic locus for every ε < 1. Moreover the (F3) extension mechanism requires the defect ideal to land in a topologically nilpotent set (|·| < 1, so that lim ZR/I^n receives the evaluation — (172), p. 94); with a defect bounded below by 1 there is no completion and no A_inf-analog action."

### 4.2 Re-derivation

Let x be a point of X = Spec Z̄ over (p), κ(x) = F̄_p, and let Q: F̄_p → C be any multiplicative map with Q(0) = 0, Q(1) = 1 and Q|_{F̄_p^×} a homomorphism — this covers every representative of every point of the packet: a point of C_{x_0} is F_ν^{−1}π((x, P^×)) and the maps whose "defect" one can test are the multiplicative maps κ(y) → C at points y over p, all of which have this form (any G-conjugate y of x has κ(y) = F̄_p; for the p-power projective limit lim_{( )^p} F̄_p ≅ F̄_p — [x-03, 93] (170) — the same maps arise; for the full N-limit there is no addition at all, so no defect can be posed there). Then:

- p odd: 2̄ ∈ F_p^× ⊂ F̄_p^×, so Q(2̄) is torsion in C^×, i.e. a root of unity ζ with |ζ| = 1, and |Q(2̄) − 2| = |2 − ζ| ≥ |2| − |ζ| = 1 (equality iff ζ = 1).
- p = 2: 2̄ = 0, Q(0) = 0, |0 − 2| = 2 ≥ 1.

Q(1̄) = 1 because a homomorphism sends the identity to the identity. So the defect at (r, s) = (1̄, 1̄) is ≥ 1 for every such Q, every p, every representative, and a fortiori for every character in every class E ⊆ E_tors (the argument uses no condition on Q beyond multiplicativity and Q(1) = 1 — not even (Tors)). ✓ Hence a condition of the form "|Q(r+s) − Q(r) − Q(s)| ≤ ε for all r, s in the domain" with ε < 1 is satisfied by no point over any prime p, provided only that 1 is in the domain (it is: 1 ∈ Γ(X, O) = Z̄, 1 ∈ κ(y)). ✓

**Is "the periodic locus" the right locus?** The set of periodic points of X_0 = X_0^E is exactly ∐_{x_0} Γ^E_{x_0} ([x-03, 39] Thm 6.1 for E ⊆ E_max; [x-06, 11–12] Thm 4.2 verbatim; for E_tors itself the packets Γ_{x_0} are still where every point has isotropy p^Z, [x-03, 33]). S4 needs at least one periodic orbit in each Γ_p (ledger T1 / ALKL H4, [x-03, 40] "such that Y_0 contains at least one periodic orbit in Γ_{x_0} for every closed point x_0"). Lemma B shows the threshold condition removes all of Γ_p for every p. So the periodic locus is precisely the locus where the selection has to be nonempty, and it is empty there. ✓ Note that the lemma establishes emptiness at *char-p points*; it says nothing about what an archimedean condition would do at characteristic-0 points (κ(x) = Q̄), and it need not: the periodic orbits live over the primes.

**A scope remark the note should carry (MIN-3).** The local principle's interesting locus is the pair (x, y) = (η, s) — a *generic* point x with a *specialization* y to the closed point, where the condition lives on the tilt Ô^♭_{{x},y} of the completed local ring ([x-03, 113]: "For (x, y) = (η, s) ... the continuous injective ring homomorphisms ô^♭_K → o^♭"); the closed-point pair (s, s) is the one that produces the single periodic orbit (Thm 15.6 6)). The global C-valued points (x, P^×) carry no specialization datum y ([x-03, 27]; [x-06, 11] Thm 4.1), so the only verbatim transplant of the defect condition is at the residue field κ(x) itself — which is what Lemma B tests, and which is the (s, s)-type locus. The note's "verbatim archimedean translation" is therefore the translation at the (s, s)-type points; that is the right test for S4, but the sentence "the verbatim archimedean translation ... selects the EMPTY set on the periodic locus" should say so explicitly, since a reader of [x-03] §15 will otherwise look for the (η, s) analog.

**The "Moreover" clause.** (172) on [x-03, 94] is verbatim: "Choose an element ω_α ∈ o with α ≤ |ω_α| < 1. Then (x, y, P̌_y) ∈ Y̌_α gives a ring homomorphism P̌_y : ZÔ^♭ → o with P̌_y(I_y) ⊂ ω_α o and hence an induced ring homomorphism W_p(P̌_y) : ... = lim_n ZÔ^♭/I_y^n → lim_n o/ω_α^n = o." The completion lim_n o/ω_α^n = o requires |ω_α| < 1 (ω_α topologically nilpotent); an archimedean analog would need the values on the defect ideal I to lie in a set whose powers shrink to 0, i.e. |·| < 1 on the generators [r+s] − [r] − [s], which Lemma B's test refutes at the generator [1+1] − 2[1]. ✓ The note's "(172), p. 94" anchor is correct.

**The supporting observations.** "This process does not give more points" is verbatim at [x-03, 6] (the note twice writes "intro p. 5"; the paragraph begins on p. 5 but the sentence is the first full sentence block on p. 6 — MIN-7). "Was necessary to obtain something interesting" is verbatim at [x-03, 6] ✓. Prop. 15.8 (p. 116) versus Thm 15.6 ✓ as characterized. The ultrametric step in Prop. 14.7's proof is verbatim at [x-03, 95] ("≤ max(|...|^{p^ν}, |p|)") ✓.

### 4.3 Break attempt

Could a different normalization of the threshold escape the test? A relative threshold |Q(r+s) − Q(r) − Q(s)| ≤ ε·|Q(r) + Q(s)| would give |ζ − 2| ≤ 2ε at (1̄,1̄), satisfiable with ζ = 1 when ε ≥ 1/2; the note's "What Lemma B does NOT close" paragraph already excludes "comparative" conditions from the lemma's scope, so this is not a counterexample to the lemma as stated, but it confirms that Lemma B kills exactly the uniform-threshold reading and nothing wider. No counterexample to the stated lemma exists: the inequality |2 − ζ| ≥ 1 for |ζ| = 1 is sharp and unconditional.

### 4.4 Verdict on Lemma B

**PASS** (with the scope wording MIN-3 and the page correction MIN-7). The test r = s = 1 is valid at every packet point in every representative, for every class E ⊆ E_tors and every prime; the periodic locus is the right locus; the (172) anchor is correct.

---

## 5. Lemma C (§5 of the note): Aut(C) → Aut(µ(C)) = Ẑ^× is surjective

### 5.1 Statement as written

"The restriction map Aut(C) → Aut(µ(C)) = Ẑ^× is surjective for C the complex numbers (or any algebraically closed field of characteristic 0 containing Q̄ with infinite transcendence degree). Derivation: u ∈ Ẑ^× defines an automorphism of Q(µ_∞) (cyclotomic theory); extend to Q̄ (isomorphism extension), then to C along a transcendence basis of C over Q̄ and to the algebraic closure C of the lifted subfield (Steinitz; uses AC)."

### 5.2 Re-derivation, step by step

Fix an algebraically closed field C of characteristic 0; it contains a unique algebraic closure Q̄ of its prime field Q, and µ(C) = µ(Q̄) ≅ Q/Z, so Aut(µ(C)) = Aut(Q/Z) = lim Aut(Z/n) = lim (Z/n)^× = Ẑ^× acting by ζ ↦ ζ^u (P2 with all primes).

**Step C1 (cyclotomic).** For every u ∈ Ẑ^× there is a unique automorphism σ_u of Q^{cyc} = Q(µ_∞) with σ_u(ζ) = ζ^u for all ζ ∈ µ_∞. This is the statement that the cyclotomic character Gal(Q^{cyc}/Q) → Ẑ^× is an isomorphism, equivalently that the n-th cyclotomic polynomial is irreducible over Q for every n (so that [Q(ζ_n) : Q] = φ(n) and every ζ_n ↦ ζ_n^a, gcd(a, n) = 1, is realized by an automorphism; compatibility along n | m is automatic by uniqueness). No on-disk source states this; it is classical (attribution recalled: Gauss for prime n, Kronecker/Dedekind in general — [RU]) and is labeled **[RU — classical, Galois theory of cyclotomic fields]**. It is load-bearing for Lemma C and hence for Proposition 1: without it one only knows that the image of Aut(C) in Ẑ^× is the image of Gal(Q̄/Q), and Proposition 1's "every base class" would weaken to "every base class in the image". The note calls this "cyclotomic theory" without a citation (MIN-4: cite it; the program has no cyclotomic-theory text on disk, so the label [RU-classical] must appear in the note).

**Step C2 (to Q̄).** Q̄ is an algebraic closure of Q^{cyc}. The isomorphism-extension theorem (an isomorphism of fields extends to an isomorphism of any two algebraic closures) gives σ̄_u ∈ Aut(Q̄) extending σ_u. Proof sketch, so that the use of choice is explicit: the set of pairs (L, τ) with Q^{cyc} ⊆ L ⊆ Q̄ and τ: L → Q̄ extending σ_u, ordered by extension, has upper bounds for chains (unions), so Zorn gives a maximal (L, τ); if L ≠ Q̄, pick α ∈ Q̄ ∖ L with minimal polynomial f over L; τ(f) has a root β in Q̄, and τ extends to L(α) → Q̄ by α ↦ β, contradicting maximality; so L = Q̄, and τ(Q̄) is an algebraically closed subfield of Q̄ algebraic over Q, hence τ is onto. Zorn's lemma is used. ✓

**Step C3 (along a transcendence basis).** Let B be a transcendence basis of C over Q̄ (exists by Zorn; B may be empty, finite or infinite — nothing in the argument needs it infinite). σ̄_u extends to the polynomial ring Q̄[B] by acting on coefficients and fixing B, hence to its fraction field Q̄(B) (an automorphism, since it is bijective on Q̄[B]). ✓

**Step C4 (to C).** C is algebraic over Q̄(B) (definition of transcendence basis) and algebraically closed, so C is an algebraic closure of Q̄(B); Step C2's extension argument (Zorn again) extends the automorphism of Q̄(B) to an automorphism σ of C. Its restriction to µ(C) = µ(Q̄) ⊂ Q^{cyc} is σ_u|_{µ_∞} = ( )^u. ✓

**Exact use of choice.** Zorn's lemma is used three times (Steps C2, C3, C4). For C = the complex numbers this is essential and not cosmetic: the existence of any automorphism of C other than the identity and complex conjugation is not provable in ZF alone [RU — Solovay-type models; recalled, zero weight, not load-bearing: it only calibrates what "Aut(C)-stable" means]. Proposition 1 is therefore a ZFC statement, and its hypothesis "Aut(C)-stable" is strong precisely because Aut(C) is enormous under AC. The note says "uses AC" but does not say that the surjectivity itself (not merely its proof) depends on choice; MIN-5 asks for one sentence.

**The parenthetical restriction "with infinite transcendence degree" is unnecessary** (MIN-6): Steps C1–C4 work for every algebraically closed field of characteristic 0, including Q̄ itself (B = ∅). It does no harm — the complex numbers have transcendence degree 2^{ℵ_0} — but as written it suggests a false necessity.

**The projection to Ẑ^×_{(p)}.** Proposition 1 needs σ with prescribed action u ∈ Ẑ^×_{(p)} on µ^{(p)}(C). Ẑ^× = Z_p^× × Ẑ^×_{(p)}; lift u to ũ = (1, u) ∈ Ẑ^×, apply Lemma C, and restrict: σ|_{µ^{(p)}(C)} = ( )^u. The note's proof of Proposition 1 says "pick σ with u_σ = u (Lemmas C–D)" without this one-line projection (folded into MIN-4's replacement text).

### 5.3 Break attempt

None possible: given C1, the extension steps are forced. Without C1 the statement is exactly as strong as the image of the cyclotomic character, which is the classical theorem.

### 5.4 Verdict on Lemma C

**PASS**, with the [RU-classical] label on the cyclotomic input (MIN-4), the AC sentence (MIN-5), and the removal of the transcendence-degree clause (MIN-6). Every extension step is re-derived; the exact uses of Zorn are listed.

---

## 6. Lemma D (§5 of the note): the Aut(C)-action on the character spaces

### 6.1 Statement as written

"Let σ ∈ Aut(C) act on X̌(C)_{E_tors} by post-composition, (x, P) ↦ (x, σ∘P). Then: (i) σ commutes with the G-action (pre-composition), with every F_ν, hence with the Q^{>0}-action, and descends to the suspension X_0^{E_tors} commuting with the flow φ^t and fixing the R-coordinate; (ii) σ preserves each example class E_tors, E_max, E_f, E_fg, E_fd, E_fd0 (kernels are unchanged — ker(σ∘P) = ker P — and images map by σ, preserving torsion and ⊗Q-dimension; Def. 4.1's operations are pre-compositions, which commute with σ); (iii) on the packet over p, σ maps the point with coordinates (a, ν) to the point with coordinates (u_σ a, ν), where u_σ ∈ Ẑ^×_{(p)} is σ's action on prime-to-p roots of unity: σ∘χ_x = σ|_µ∘χ_x = χ_x∘( )^{u_σ} ... Hence σ moves the base class [a] ↦ [u_σ a] in B_p and maps closed orbits of length log p to closed orbits of length log p in the same packet."

### 6.2 Re-derivation

**Well-definedness on X̊(C).** A point is a pair (x, P^×) with P^×: κ(x)^× → C^× a character ([x-03, 27]; [x-06, 11] Thm 4.1). σ ∈ Aut(C) restricts to a group automorphism of C^×, so σ∘P^× is again a character; the extension by zero of σ∘P^× is σ∘(extension by zero of P^×) since σ(0) = 0. In the multiplicative-map picture of Remark 3.4 (P: R → C with P^{−1}(0) = p_x), σ∘P is multiplicative with the same zero set, so the point x is unchanged. ✓ No continuity is claimed or needed anywhere in Lemma D or Proposition 1 (σ is in general discontinuous on C, hence on X̊(C)); everything below is set-theoretic.

**(i) Commutation.** G acts by (x, P^×)g = (x^g, P^×∘g) ([x-06, 11]); σ∘(P^×∘g) = (σ∘P^×)∘g. ✓ F_ν(x, P^×) = (x, P^×∘( )^ν); σ∘(P^×∘( )^ν) = (σ∘P^×)∘( )^ν. ✓ Since σ commutes with every F_ν and the F_ν are injective on X̊(C)_E ([x-03, 27] Prop. 4.2), σ induces a bijection of the colimit X̌(C)_E = colim_{N_0} X̊(C)_E (define σ(F_ν^{−1}(x, P)) := F_ν^{−1}(x, σ∘P); this respects the identifications F_ν^{−1}(x, P) = F_{νµ}^{−1}F_µ(x, P) because σF_µ = F_µσ), commuting with the Q^{>0}-action F_q. ✓ It commutes with G, so descends to X̌_0(C)_E = X̌(C)_E/G. ✓ On X̌_0(C)_E × R^{>0} let σ act by (P_0, u) ↦ (σP_0, u); then σ((P_0, u)q) = σ(F_q P_0, q^{−1}u) = (F_q σP_0, q^{−1}u) = (σP_0, u)q, so σ descends to the quotient X_0 = X̌_0(C)_E ×_{Q^{>0}} R^{>0} ([x-03, 38]) and commutes with φ^t[P_0, u] = [P_0, e^t u]. ✓ "Fixing the R-coordinate" means σ[P_0, u] = [σP_0, u], which is what was shown. ✓ σ^{−1} acts likewise, so σ acts bijectively on every one of these spaces. ✓

**(ii) Class stability, one class at a time** (definitions verbatim in §1; χ: κ^× → C^×, χ′ := σ∘χ). σ is injective, so ker χ′ = ker χ, and (ker χ′)_tors = (ker χ)_tors.

- E_tors: (Tors) says (ker χ)_tors is finite with order in N_0 — a property of ker χ alone. Preserved. ✓
- E_f: (Tors) and ker χ finite (equivalently |ker χ| ∈ N_0). Kernel-only. ✓
- E_fg: (Tors) and ker χ finitely generated. Kernel-only. ✓
- E_fd: (Tors) and ker χ ⊗ Q finite-dimensional. Kernel-only. ✓
- E_fd0: (Tors) and (ker χ|_{κ(x_0)^×}) ⊗ Q finite-dimensional. ker(χ′|_{κ(x_0)^×}) = ker(χ|_{κ(x_0)^×}) since restriction commutes with post-composition and σ is injective. ✓
- **E_max (the note's press point):** (Tors) plus (Image): "Only if char κ > 0. If χ(κ^×) is torsion, then κ^× is torsion as well." The condition depends on χ only through whether the subgroup χ(κ^×) ⊆ C^× is torsion. Now χ′(κ^×) = σ(χ(κ^×)), and σ is a group automorphism of C^×, which preserves the order of every element; so χ′(κ^×) is torsion iff χ(κ^×) is torsion, and the antecedent of (Image) holds for χ′ iff it holds for χ, while the consequent ("κ^× is torsion") does not involve χ at all. Preserved, in both directions (σ and σ^{−1}). ✓ For completeness: (Stable Image) ([x-03, 29]) is likewise preserved, since it only asks whether χ(κ̃^×) is torsion for subfields κ̃.

So every named class is Aut(C)-stable, and the note's parenthetical reasons are correct: "kernels are unchanged" and "images map by σ, preserving torsion". The phrase "preserving ... ⊗Q-dimension" is slightly misleading — the ⊗Q-dimension conditions in E_fd and E_fd0 are on the *kernel*, not the image, so what preserves them is ker χ′ = ker χ, not anything about images (MIN-8, wording). The remark "Def. 4.1's operations are pre-compositions, which commute with σ" is true and is what makes σ(E) admissible whenever E is; it is not needed for the stability of the six classes, which is what Proposition 1 uses.

**(iii) The coordinate formula.** By P1, χ_x: F̄_p^× → µ^{(p)}(C) is an isomorphism, so σ|_{µ^{(p)}(C)} = ( )^{u_σ} for a unique u_σ ∈ Ẑ^×_{(p)} (P2), and σ∘χ_x = ( )^{u_σ}∘χ_x = χ_x∘( )^{u_σ} (P2: power maps commute with homomorphisms of prime-to-p torsion groups). Hence σ∘(χ_x∘( )^a∘( )^ν) = χ_x∘( )^{u_σ}∘( )^a∘( )^ν = χ_x∘( )^{u_σ a}∘( )^ν, i.e. (a, ν) ↦ (u_σ a, ν) on the coordinates of (35)/(37). ✓ This is compatible with the fibers of (35) ((a, ν) ~ (p^n a′, νp^n) ↦ (u_σ p^n a′, νp^n) ~ (u_σ a′, ν)) and with the N x_0^Ẑ = p^Ẑ quotient of (37) (u_σ(a p^Ẑ) = (u_σ a)p^Ẑ, the group being abelian). On C_{x_0} via (38): σ[a, q] = [u_σ a, q] (σ commutes with F_{ν′}^{−1}, (i)). So the base class moves by translation, [a] ↦ [u_σ a] in B_p. ✓ σ fixes x, hence the fiber of pr_{X_0} over x_0 = (p), i.e. maps C_{x_0} to itself and Γ_p to itself; it commutes with the flow, so it maps orbits to orbits and preserves the isotropy ((R^{>0})_{σz} = (R^{>0})_z since σ is a flow-equivariant bijection), hence periodic orbits of length log p to periodic orbits of length log p. ✓

**Terminology.** The note says "closed orbits" for periodic orbits. The adjudication (§3, §4 item 3) records that no periodic orbit in Γ_p is closed as a subset of X_0 whenever ≥ 2 base classes are E-realized; the word should be "periodic orbit" throughout Lemma D and Proposition 1 (MIN-9).

### 6.3 Break attempt

(ii) could fail only for a class whose definition depends on the values of χ beyond kernel and torsion-ness of the image — e.g. a class defined by "χ(κ^×) ⊂ S^1" (the unitary locus of [x-03] §8), which is *not* Aut(C)-stable because wild σ do not preserve |·|. None of the six named classes does this, and the note (§5 scope (b), §6) already draws that line. (iii) could fail only if χ_x were not onto µ^{(p)}(C); P1 excludes it for X_0 = Spec Z. (For a general X_0 whose function field has fewer roots of unity — e.g. characteristic p — ι need not be onto µ^{(p)}(C) and the formula would need an adjustment; outside the note's scope.)

### 6.4 Verdict on Lemma D

**PASS** (wording MIN-8, MIN-9). All three parts re-derived; class stability verified for all six named classes, in particular for E_max's (Image) condition, which is preserved because σ preserves element orders in C^×; the coordinate formula follows from P1 + P2.

---

## 7. Proposition 1 (§5 of the note): the equivariance no-go (D1)

### 7.1 Statement as written

"Let E be any Aut(C)-stable class (all named example classes qualify) and let S ⊆ X_0^E be Aut(C)-stable and flow-invariant. If S contains one periodic point over the prime p, then for EVERY base class [c] ∈ B_p, S contains a closed orbit of length log p with base class [c]. In particular S contains uncountably many closed orbits over p (B_p is an infinite profinite group, hence uncountable — adjudication §2, re-derived there), and no Aut(C)-stable selection achieves one orbit per prime. Proof: by §4's coordinates the periodic point lies on an orbit γ with some base class [a]; for [c] = [ua] pick σ with u_σ = u (Lemmas C–D); σ(γ) ⊆ S is a closed orbit of the same length with base class [c]; distinct base classes lie on distinct orbits since the fibers of the (38)-fibration are the Q^{>0}-orbits ([x-03] p. 33)."

### 7.2 Re-derivation

Fix (x, ι) as in [x-03, 31–33]; base classes are taken with respect to this choice (the fibration map "depend[s] on our choices of x and ι", [x-03, 33]; the *set* of orbits in Γ_p and its cardinality do not).

1. *The periodic point z lies in Γ^E_p and on an orbit of base class [a].* "Over the prime p" means pr_{X_0}(z) = (p), i.e. z ∈ Γ^E_{x_0} for x_0 = (p) ([x-03, 38]: Γ_{x_0} = C_{x_0} ×_{Q^{>0}} R^{>0}, C_{x_0} = pr_{X_0}^{−1}(x_0)); every periodic point is in some Γ^E_{x_0} anyway ([x-03, 39] Thm 6.1 for E ⊆ E_max; for E = E_tors, points of X_0 over (p) with nontrivial isotropy are in Γ_{x_0} by definition). Its orbit γ ⊆ S by flow-invariance. By (38) z = [[a, q], u] for some a ∈ Ẑ^×_{(p)}, so γ has base class [a] (P3). ✓
2. *Choice of σ.* Given [c] ∈ B_p, put u := c a^{−1} ∈ Ẑ^×_{(p)} (B_p is a quotient group of Ẑ^×_{(p)}); by Lemma C plus the projection Ẑ^× ↠ Ẑ^×_{(p)} (§5.2 last paragraph) there is σ ∈ Aut(C) with σ|_{µ^{(p)}(C)} = ( )^u, i.e. u_σ = u. ✓
3. *σ(γ) is a periodic orbit of length log p in Γ^E_p with base class [c].* Lemma D(i): σ acts on X_0^E (E is Aut(C)-stable, Lemma D(ii) for the named classes) commuting with the flow, so σ(γ) is the orbit of σ(z), periodic with the same least period log p (P4; isotropy is preserved by a flow-equivariant bijection). Lemma D(iii): σ(z) = [[u a, q], u′] has base class [u a] = [c]. σ fixes x, so σ(z) ∈ Γ_p. ✓
4. *σ(γ) ⊆ S* by Aut(C)-stability of S. ✓
5. *Distinct base classes are distinct orbits* — P3, verbatim at [x-03, 33] ("the fibres are the Q_0^{>0}-orbits") and at [x-03, 38] for the suspension ("with fibres the R^{>0}-orbits"). So the orbits produced in step 3 for distinct [c] are distinct. ✓
6. *Count.* S contains at least |B_p| = 2^{ℵ_0} periodic orbits of length log p over p (P5). ✓ Hence no Aut(C)-stable flow-invariant S ⊆ X_0^E meets Γ_p in exactly one orbit (or in countably many) unless it misses Γ_p altogether. ✓

**The consumption of "[x-03] p. 33: fibers = Q^{>0}-orbits" is correct and is exactly what step 5 needs.** The adjudication had already verified the same sentence; it is re-derived in P3 above from (38) and the definition of the Q^{>0}-action, so the proposition does not depend on reading Deninger's sentence charitably.

**Generalization check (not claimed by the note, but confirms robustness).** For any arithmetic X_0 and closed point x_0 with N x_0 = p^f, the orbit space of Γ_{x_0} is a torsor under Ẑ^×_{(p)}/p^Ẑ (P3 with (39): fibers of C_{x_0} → Ẑ^×_{(p)}/p^Ẑ are again single Q^{>0}-orbits), still uncountable, still swept by Aut(C)-translations, so the same argument runs. The note restricts to Spec Z, correctly.

### 7.3 Break attempts

(a) *Could S be Aut(C)-stable, flow-invariant, meet Γ_p, and still avoid some base class?* No: step 2 realizes every u ∈ Ẑ^×_{(p)}, hence every translate. The only escape is an S that is not Aut(C)-stable — e.g. the Theorem-C cut E(a_0), whose packet locus is a single orbit and which is moved off itself by any σ with u_σ ∉ p^Ẑ; the note's scope item (c) records this and it is consistent (σ(χ^{a_0}) = χ^{u a_0} has base class [u a_0] ≠ [a_0]).
(b) *Could the hypothesis "Aut(C)-stable" be vacuous?* Under AC it is not (Lemma C). Under ZF without choice Aut(C) may be {id, conj}; then "Aut(C)-stable" is nearly empty as a condition and Proposition 1's conclusion would be false for a one-orbit S — but so is Lemma C in that setting, and the whole statement is a ZFC theorem (MIN-5).
(c) *Does the proposition need E ⊆ E_max?* No. Only Aut(C)-stability of E and the existence of Γ_p with its isotropy p^Z, which hold in E_tors ([x-03, 33]).
(d) *Does it need any topology?* No. S is an arbitrary subset; "closed orbit" means periodic orbit (MIN-9). This is a strength (no Hausdorff issue, cf. adjudication §3) and a limitation: the proposition does not constrain selections that use C's analytic structure, as the note's scope item (b) says correctly (a continuous automorphism of C is the identity on Q, hence on R by continuity, hence is id or conjugation — two lines, ✓).

### 7.4 The Corollary and the scope items (§5) — checked for consistency only

The Corollary ("any selection defined uniformly from the abstract field C and the scheme data ... is Aut(C)-stable ... must break Aut(C)-symmetry") is a transport-of-structure schema, explicitly flagged by the note as "a definability schema, not a theorem" (scope (a)). It is correctly scoped: a locus defined by a formula in the language of fields applied to (C, scheme data) is carried to itself by every σ ∈ Aut(C); a locus defined using the topology, the absolute value, or the real subfield is not. Scope (c)'s consistency with Theorem C and the "explains Thm 5.2" remark are consistent with Proposition 1 (Thm 5.2's "If e.g. E ⊃ E_f then C^E_{x_0} = C_{x_0}", [x-03, 34], is the statement that the kernel-defined classes carry full packets; Proposition 1 gives the base-class half of that for any Aut(C)-stable flow-invariant S, and admissibility gives the ν-shifts). No finding.

### 7.5 Verdict on Proposition 1

**PASS** (wording MIN-9; the projection step folded into MIN-4's replacement; the base-class convention MIN-10). Every step re-derived; the fibers-are-orbits anchor verified verbatim on pp. 33 and 38 and re-derived from (38); distinct base classes ⇒ distinct orbits; uncountability re-derived two ways.

---

## 8. The trichotomy D1–D3 as stated in the note's §0, and D3's derivation (§4 Consequence 2)

**D1** = Proposition 1 (§7 above): PASS. The §0 sentence "Aut(C) sweeps each packet base B_p = Ẑ^×_{(p)}/p^Ẑ transitively" is Lemma C + Lemma D(iii): the image of Aut(C) → Ẑ^×_{(p)} is everything, and Ẑ^×_{(p)} acts on its quotient B_p by translations, transitively. ✓

**D2** = Lemma B (§4 above): PASS. The §0 sentence "at every char-p packet point the test r = s = 1 gives |P(2̄) − 2| ≥ 1" is exactly what is proved. ✓

**D3** = Lemma A + the transport analysis (§4 Consequence 2). Re-derivation: fix j: µ^{(p)}(C) ≅ µ^{(p)}(C_p) (a torsor under Ẑ^×_{(p)} by P2). The composite red∘j∘χ_x: F̄_p^× → µ^{(p)}(o_{C_p}) → F̄_p^× is a group automorphism, hence ( )^{b_j} for a unique b_j ∈ Ẑ^×_{(p)}. For a character χ_x∘( )^a∘( )^ν with ν = p^k ν′, p ∤ ν′, the reduction of j∘χ_x∘( )^a∘( )^ν is y ↦ y^{ν′ b_j a p^k} (P2); by Lemma A (κ = F̄_p) the map j∘χ_x∘( )^a∘( )^ν is mod-p additive iff this reduction is a field embedding F̄_p → F̄_p, i.e. an element of Aut(F̄_p) = p^Ẑ ⊂ Ẑ^×_{(p)}; since ν′ b_j a has ℓ-adic valuation v_ℓ(ν′) at every ℓ | ν′ while elements of p^Ẑ are units, this forces ν′ = 1 and [a] = [b_j^{−1}] in B_p. So the j-transported condition selects, at the point x, the characters χ_x∘( )^a∘( )^{p^k} with a ∈ b_j^{−1}p^Ẑ, k ≥ 0 — in the packet, exactly the single Q^{>0}-orbit with base class [b_j^{−1}] (P3). Varying j over its Ẑ^×_{(p)}-torsor varies b_j over Ẑ^×_{(p)} and the selected base class over all of B_p. ✓ The selected class of characters is not closed under ( )^ν for ν ∉ p^N (§9.1 below), so it is not admissible; its admissible closure is the Theorem-C class E(a_0) with a_0 = b_j^{−1} (adjudication §4 item 5(b): reachability set a_0·p^Ẑ at unit exponents). **The note's §0 wording "the resulting class is precisely probe A's Theorem C cut E(a_0)" overstates the identity: the transported condition and E(a_0) select the same single orbit in Γ_p, but as classes of characters they differ (the transported class is not ν-closed; E(a_0) is its admissible hull).** MIN-11 (wording; replacement in §10). The substantive claims — one arbitrary point of a Cantor torsor per prime, not admissible, not N-invariant, forfeits the certified theory — are correct and are the adjudication's own record. D3: PASS with MIN-11.

The identity underneath (§0, §4 Consequence 1, §9 of the note) is P6, Deninger's displayed formula; the novelty block in the note already records this and is not this report's item.

---

## 9. The two remaining derived items

### 9.1 §3's freshman's-dream N-invariance argument

Claim: "additivity mod p is ( )^p-stable (Prop. 14.7's computation) but not ( )^ℓ-stable for ℓ ≠ p, since (r+s)^ℓ ≢ r^ℓ + s^ℓ mod p."

Re-derivation in the Lemma A model (κ = F̄_p, P = [·]∘τ mod-p additive). For ν ∈ N, P∘( )^ν = [·]∘τ∘( )^ν = [·]∘( )^ν∘τ (τ is a ring homomorphism), whose reduction mod m is ( )^ν∘τ. If P∘( )^ν were mod-p additive, its reduction would be additive (p·o ⊆ m), so ( )^ν would be additive on τ(F̄_p) = F̄_p, hence a ring endomorphism of F̄_p, hence a power of Frobenius ( )^{p^k}; comparing on F_{p^n}^× (cyclic of order p^n − 1) gives ν ≡ p^k mod (p^n − 1) for all large n, so ν = p^k. Conversely for ν = p^k the reduction is Frob^k∘τ, additive, and P∘( )^{p^k} = [·]∘(Frob^k∘τ) is mod-p additive by Lemma A (⇐). So the class of mod-p-additive characters is closed under ( )^ν exactly for ν ∈ p^N: it satisfies Def. 4.1's biconditional for N_0 = p^N ([x-03, 89] "we only consider the monoid N_0 generated by p") and fails it for N_0 = N — Deninger's "the resulting class E is not N-invariant" ([x-03, 29]). ✓ The note's one-line reason "(r+s)^ℓ ≢ r^ℓ + s^ℓ mod p" should read "for some r, s" (e.g. r = s = 1 whenever 2^ℓ ≢ 2 mod p; in general the argument above), MIN-12. In Deninger's own framework the F_ℓ are not even defined on X̌_c(o) (colimit over F_p only), so the statement is about the hypothetical N-extension, which is how the note uses it. Prop. 14.7's computation ([x-03, 95]) gives the p-stability in the α-threshold form (Y̌_α ⊂ Y̌_{1/p}, F_p(Y̌_α) = Y̌_α); the Lemma A model gives it at α = 1/p directly. PASS.

### 9.2 §7's Haar formal count

Claim: "the packet's aggregate orbit contribution is ∫_{B_p}(single-orbit term) dHaar = the single-orbit term, since the integrand is constant (all orbits in Γ_p have length log p — [x-06] Thm 4.2)."

[x-06, 12] Thm 4.2 verbatim: "The compact subsets Γ_{x_0} ⊂ X_0 consist of periodic orbits of length log N x_0 where N x_0 = |κ(x_0)|"; for X_0 = Spec Z, "log p" ([x-06, 12]: "i.e. log p if X_0 = spec Z"). Also [x-03, 38–39] (P4). ✓ The orbit space of Γ_p is in bijection with B_p (P3); the Haar probability measure on the compact group B_p is translation-invariant, hence independent of the (x, ι)-dependent identification (a change of ι translates by u ∈ Ẑ^×_{(p)}, a change of x by a Galois conjugate translates by the cyclotomic-character value; both are translations), and Aut(C) acts by translations (Lemma D(iii)) — so the measure is canonical and Aut(C)-invariant, and it is flow-invariant because the flow fixes the base (P3). ✓ The "formal count" is then the tautology that the integral of a constant against a probability measure is the constant; it presupposes that the single-orbit term of whatever trace formula is meant depends only on the orbit length (true for the length-and-multiplicity terms of the formulas the ledger names, but the note itself says "at the formal level" and lists the obstacles — no linearized Poincaré map, no published trace formula for orbit continua). Nothing to repair at the level of this report; the novelty block already re-scopes the "new in this note" claim. PASS as a formal statement.

---

## 10. VERDICT BLOCK

**Verdict on the item (Lemmas A–D + Proposition 1 + §3 + §7): PASS-WITH-REPAIRS.** 0 FATAL / 1 MAJOR / 12 MINOR. Per lemma: Lemma A PASS-WITH-REPAIRS (MAJ-1, MIN-2); Lemma B PASS (MIN-3, MIN-7); Lemma C PASS (MIN-4, MIN-5, MIN-6); Lemma D PASS (MIN-8, MIN-9); Proposition 1 PASS (MIN-9, MIN-10); D3 PASS (MIN-11); §3 PASS (MIN-12); §7 PASS; M-1 (transcription) against §4's packet-coordinates paragraph.

### 10.1 Findings, most severe first

| id | severity | location (note) | finding |
|---|---|---|---|
| MAJ-1 | **MAJOR** (false as stated in its declared generality; repair is a hypothesis restriction covering every use; no downstream consequence) | §4, Lemma A, statement and its parenthetical | For an algebraically closed κ of characteristic p other than F̄_p, κ^× is not torsion (t ∈ F̄_p(t)^{alg} has infinite order), so "values automatically in µ^{(p)}(o) ... since κ^× is prime-to-p torsion" is false; the right-hand side "[·]∘τ" is undefined for such κ under the note's definition of [·] (only on µ^{(p)}(k)); and under the extended Teichmüller reading the (⇒) direction fails (§3.5: non-Teichmüller ring homomorphisms κ → o^♭ exist when κ is transcendental over F_p, and each yields via [x-03, 100] Prop. 14.14 a mod-p-additive multiplicative P with P mod m = τ but P ≠ [·]∘τ). Every use in the note (packet points of Spec Z; the (s, s) fiber of Thm 15.6) has κ = F̄_p, where the lemma is correct (§3.3). |
| MIN-2 | MINOR | §4, Lemma A, proof of (⇐) | The Witt-vector argument is correct but consumes W(k) ⊆ o (Teichmüller-compatible), F bijective on W(k), and V F = p — none on disk, hence [RU] under standing order 5. Replace by the elementary proof of §3.3 Step 3 (binomial theorem + p-adic completeness + injectivity of reduction on µ^{(p)}(o)). |
| MIN-3 | MINOR | §6, Lemma B, framing | State that the verbatim transplant tested is the one at the residue field κ(x) (the (s, s)-type locus), the only one the C-valued points support since they carry no specialization datum y; the local principle's (η, s) locus ([x-03, 113]) has no C-valued counterpart, which is part of why "verbatim" is the right word. |
| MIN-4 | MINOR | §5, Lemma C, "cyclotomic theory" | The surjectivity of Gal(Q^{cyc}/Q) → Ẑ^× (irreducibility of every cyclotomic polynomial over Q) is load-bearing, classical, and not on disk: label it [RU — classical] and cite a standard text; add the one-line projection Ẑ^× ↠ Ẑ^×_{(p)} that Proposition 1's step "pick σ with u_σ = u" uses. |
| MIN-5 | MINOR | §5, Lemma C, "(uses AC)" | Say that the *statement* (not merely the proof) depends on choice: without AC, Aut(C) can be {id, conj} [RU], so Lemma C and Proposition 1 are ZFC results and "Aut(C)-stable" is a strong hypothesis only in ZFC. |
| MIN-6 | MINOR | §5, Lemma C, parenthetical | "with infinite transcendence degree" is unnecessary; the argument works for every algebraically closed field of characteristic 0 (B may be empty). Delete. |
| MIN-7 | MINOR | §2 Stage 2 and §6 ("intro p. 5") | "this process does not give more points" is on [x-03] p. 6, not p. 5 (the paragraph starts on p. 5; the sentence is on p. 6). |
| MIN-8 | MINOR | §5, Lemma D(ii) | "images map by σ, preserving torsion and ⊗Q-dimension": the ⊗Q-dimension conditions (E_fd, E_fd0) are on the kernel, which is unchanged; only (Image) concerns the image, and it is preserved because σ preserves element orders in C^×. Reword. |
| MIN-9 | MINOR | §5, Lemma D(iii) and Proposition 1 (four occurrences) | "closed orbit" → "periodic orbit": by the adjudicated Cor. A.2 no periodic orbit in Γ_p is closed as a subset of X_0 when ≥ 2 base classes are E-realized, which is the case for every Aut(C)-stable S meeting Γ_p (Proposition 1 itself). |
| MIN-10 | MINOR | §5, Proposition 1, statement | Base classes are relative to the fixed (x, ι) of [x-03] pp. 31–33 ("depend on our choices of x and ι", p. 33); say "with respect to any fixed choice of (x, ι)". The cardinality conclusion is choice-free. |
| MIN-11 | MINOR | §0 (D3) and §4 Consequence 2 | "the resulting class is precisely probe A's Theorem C cut E(a_0)" → "selects in Γ_p exactly the single orbit of base class [b_j^{−1}] — the same orbit that probe A's Theorem-C cut E(a_0), a_0 = b_j^{−1}, selects; as classes of characters the two differ (the transported class is not ν-closed; E(a_0) is its admissible hull)". |
| MIN-12 | MINOR | §3, freshman's dream | "(r+s)^ℓ ≢ r^ℓ + s^ℓ mod p" → "for some r, s ∈ F̄_p (indeed ( )^ν is additive on F̄_p iff ν is a power of p)". |
| M-1 | MINOR (transcription) | §4, "Packet coordinates recalled" | "B_p := Ẑ^×_{(p)}/p^Ẑ = Aut(F̄_p)^×/Aut(F_p)^" → "= Aut(F̄_p^×)/Aut(F̄_p)" ([x-03] p. 33, PNG-verified; p. 38; [x-06] p. 12). |

### 10.2 Replacement texts

**R-MAJ-1 (Lemma A statement).** Replace the first two sentences of Lemma A by:
"**Lemma A.** Let o be as in §2 (p-adically complete rank-1 valuation ring, algebraically closed fraction field C of characteristic 0, residue field k of characteristic p; absolute value normalized by |p| = 1/p), let κ = F̄_p (this is κ(x) for every point x of Spec Z̄ over (p), [x-03] p. 31, and the residue field at the closed point of Spec o_K in [x-03] §15), and let P: κ → o be multiplicative with P(0) = 0, P(1) = 1 and P|_{κ^×} a group homomorphism into o^×. Since κ^× is torsion of prime-to-p orders, P(κ^×) ⊆ µ^{(p)}(o). Then |P(r+s) − P(r) − P(s)| ≤ |p| for all r, s ∈ κ iff P = [·]∘τ for a unique field embedding τ: κ ↪ k, where [·] is the Teichmüller section of the reduction µ^{(p)}(o) ≅ µ^{(p)}(k). (The restriction to κ = F̄_p is essential: for algebraically closed κ transcendental over F_p, κ^× is not torsion, [·]∘τ is not defined by the above, and mod-p-additive multiplicative maps κ → o correspond to arbitrary ring homomorphisms κ → o^♭ — [x-03] Prop. 14.14 — which are not all Teichmüller.)"

**R-MIN-2 (Lemma A, proof of ⇐).** Replace "(⇐) [a] + [b] − [a+b] ∈ V W(k) = p W(k) ... has absolute value ≤ |p|." by:
"(⇐) Let ζ = [τ(r)], η = [τ(s)], x = ζ + η, and q = p^n with r, s ∈ F_q, so ζ^q = ζ, η^q = η. By the binomial theorem (u+v)^p ≡ u^p + v^p mod p·o, and u ≡ v mod p^i·o (i ≥ 1) implies u^p ≡ v^p mod p^{i+1}·o; hence x^q ≡ ζ^q + η^q = x mod p·o, and inductively x^{q^{j+1}} ≡ x^{q^j} mod p^{j+1}·o. So x^{q^j} converges p-adically (o is p-adically complete and separated) to some ω with ω^q = ω and ω ≡ x mod p·o. Thus ω ∈ µ_{q−1}(o) ∪ {0} with reduction τ(r) + τ(s) = τ(r+s), so ω = [τ(r+s)] by injectivity of reduction on µ^{(p)}(o) ∪ {0}, and [τ(r+s)] − [τ(r)] − [τ(s)] = ω − x ∈ p·o. ∎ (This is the usual Teichmüller-limit argument; it avoids citing V F = p on W(k).)"

**R-MIN-3 (Lemma B framing; insert after the first sentence of §6).** "The C-valued points (x, P^×) carry no specialization datum y ([x-03] Def. 14.1 versus Thm 4.1 of [x-06]), so the defect can only be posed on the residue field κ(x) — the analog of Deninger's (s, s) locus, [x-03] p. 113 — which is also where the periodic orbits live; the (η, s) locus of the local principle has no C-valued counterpart."

**R-MIN-4/5/6 (Lemma C).** Replace the statement and derivation by:
"**Lemma C (ZFC).** For every algebraically closed field C of characteristic 0 the restriction map Aut(C) → Aut(µ(C)) = Ẑ^× is surjective; composing with the projection Ẑ^× ↠ Ẑ^×_{(p)}, so is Aut(C) → Aut(µ^{(p)}(C)) = Ẑ^×_{(p)}. *Derivation.* µ(C) = µ(Q̄) ≅ Q/Z, so Aut(µ(C)) = Ẑ^× acting by ζ ↦ ζ^u. For u ∈ Ẑ^× there is a unique σ_u ∈ Gal(Q(µ_∞)/Q) with σ_u(ζ) = ζ^u — the cyclotomic character Gal(Q(µ_∞)/Q) → Ẑ^× is an isomorphism, i.e. every cyclotomic polynomial is irreducible over Q [RU — classical; e.g. Washington, *Introduction to Cyclotomic Fields*, Chapter 2, or any Galois-theory text — theorem number not verified on disk]. Extend σ_u to Q̄ (isomorphism extension, Zorn), then to Q̄(B) for a transcendence basis B of C over Q̄ (fix B pointwise; B exists by Zorn and may be empty), then to C = an algebraic closure of Q̄(B) (Zorn). The axiom of choice is used essentially: without it Aut(C) may consist of the identity and conjugation only, and the lemma and Proposition 1 are to be read in ZFC. ∎"

**R-MIN-8 (Lemma D(ii)).** Replace the parenthetical by: "(ker(σ∘P) = ker P since σ is injective, which settles (Tors), E_f, E_fg, E_fd, E_fd0; for (Image), σ(P(κ^×)) is torsion iff P(κ^×) is torsion because σ preserves element orders in C^×, which settles E_max)".

**R-MIN-9.** Replace "closed orbit(s)" by "periodic orbit(s)" in Lemma D(iii) and Proposition 1.

**R-MIN-10 (Proposition 1, statement).** "... then, with respect to any fixed choice of (x, ι) as in [x-03] pp. 31–33, for EVERY base class [c] ∈ B_p, S contains a periodic orbit of length log p with base class [c]; in particular (independently of the choice) S contains 2^{ℵ_0} periodic orbits over p."

**R-MIN-11.** As in the table.

**R-MIN-12.** As in the table.

**R-M-1 and R-MIN-7.** As in the table.

### 10.3 What is now established at referee grade, and its precise scope

At referee grade (this report; a second independent report is owed by standing order 7 and its findings are not assumed here): for X_0 = Spec Z and C an algebraically closed field of characteristic 0 (in ZFC), (1) **Lemma A for κ = F̄_p** — the multiplicative maps F̄_p → o that are additive modulo p·o are exactly the Teichmüller lifts [·]∘τ of field embeddings τ: F̄_p ↪ k, with a fully elementary converse; this is the packet-coordinate form of [x-03] Thm 15.6's closed-point fiber Y^⋄_s = Hom(κ, k), and it is not stated, and false, for algebraically closed κ transcendental over F_p; (2) **Lemma B** — every uniform archimedean threshold |P(r+s) − P(r) − P(s)| ≤ ε < 1 posed on the residue fields at points over primes fails at (r, s) = (1̄, 1̄) for every multiplicative P with P(1) = 1, hence selects no point of any packet Γ_p, hence no periodic orbit of X_0^E for any E ⊆ E_tors; it does not constrain non-uniform (relative, averaged, asymptotic) conditions and says nothing at characteristic-0 points; (3) **Lemma C** — Aut(C) ↠ Ẑ^× ↠ Ẑ^×_{(p)}, modulo the classical cyclotomic-character theorem [RU-classical] and the axiom of choice; (4) **Lemma D** — post-composition by Aut(C) is a set-theoretic action on X̊(C), X̌(C), X̌_0(C) and X_0 commuting with G, all F_ν, Q^{>0} and the flow, preserving each of E_tors, E_max, E_f, E_fg, E_fd, E_fd0, and acting on the packet base B_p by the translation [a] ↦ [u_σ a]; (5) **Proposition 1** — any Aut(C)-stable flow-invariant subset of X_0^E (E Aut(C)-stable) containing one periodic point over p contains a periodic orbit of length log p in every base class, hence 2^{ℵ_0} of them; so no Aut(C)-stable selection cuts a packet to one orbit; the statement is set-theoretic (no topology, no continuity of σ) and constrains only selections definable from the abstract field C — not those using |·|, the topology, or R ⊂ C; (6) **D3** — the j-transported local condition selects in Γ_p exactly the single orbit of base class [b_j^{−1}], which is the orbit of probe A's Theorem-C cut E(b_j^{−1}) (the classes differ; the orbits coincide), and varying j sweeps B_p; (7) the mod-p-additive class is ( )^ν-closed exactly for ν ∈ p^N, so it is p^N-admissible and not N-admissible, as Deninger states ([x-03] p. 29); (8) the Haar count is a tautology given orbit length log p throughout Γ_p ([x-06] Thm 4.2, [x-03] Thm 6.1). Together these make the trichotomy D1–D3 referee-grade as a statement about *selection-of-points* transplants over the existing C-valued system, with exactly the scope the note's §5 items (a)–(b) and §6's last paragraph state.

— end of referee report F —
