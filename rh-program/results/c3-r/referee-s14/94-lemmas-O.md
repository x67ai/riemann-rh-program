# REFEREE REPORT O — probe 9.4 note, Lemmas A–D and Proposition 1 (the transplant trichotomy D1–D3)

**Program:** RH program, direction C3-r (geometric substrate, reduced recommission). **Session 14.**
**Date:** 2026-09-02.
**Referee:** referee O — one of two independent referees on this item (standing order 7). No contact with, and no assumption about, the second referee's findings. Nothing below is softened in the expectation that another check will catch it.
**Note under review:** `results/c3-r/probe-9.4-note.md`, read in full (all 136 lines) before any source was opened.
**Binding prior record read in full first:** `results/c3-r/probe-9.3-adjudication.md`.
**Assigned item (9.4 note §8 item 1):** Lemmas A, B, C, D and Proposition 1 (§§4–6), plus the two auxiliary derivations the charter names — §3's freshman's-dream N-invariance argument and §7's Haar formal count.

**Method actually used.** Every source sentence quoted below was read this session from the on-disk PDF with `pdftotext -layout` (poppler 26.08.0); one display whose text layer is unreliable (superscripts and overlines) was additionally read by rendering the page to PNG at 200 dpi and reading the image (§1.4). Every lemma is re-derived here from scratch and in full, so that this report can be checked *without* the note in hand. Where the note's proof does not carry its statement I attempted both to FILL the gap (replacement text supplied in §12) and to BREAK the statement (counterexample search); both attempts are reported. Nothing is asserted from memory: the two places where a standard classical fact is used are marked **[classical, not on disk]** and each is either replaced by an on-disk-free elementary proof or shown not to be load-bearing.

---

## 0. VERDICT SUMMARY (stated first)

| Item | Verdict | Findings |
|---|---|---|
| **Lemma A** (§4) — mod-p-additive multiplicative maps = the Teichmüller class, *including its converse* | **PASS-WITH-REPAIRS** | 2 MAJOR (**A-1** the hypothesis is false in the stated generality and the conclusion does not typecheck; **A-2** the converse's Witt/`V F = p` justification is unavailable under the note's own hypotheses — the statement is nevertheless TRUE and a self-contained proof is supplied), 2 MINOR |
| **Lemma B** (§6) — the archimedean defect bound selects the empty set on the periodic locus | **PASS**, strengthened | 0 MAJOR, 3 MINOR. Correct, sharp, and true on a strictly larger locus than the note claims; but "selects nothing" needs scoping — the class is *non*-empty in characteristic 0. |
| **Lemma C** (§5) — Aut(C) ↠ Aut(µ(C)) = Ẑ<sup>×</sup>, via Steinitz | **PASS** | 0 MAJOR, 3 MINOR. All four extension steps and the exact use of choice re-derived; the realizing automorphisms are necessarily discontinuous (proved here). |
| **Lemma D** (§5) — the Aut(C)-action commutes with everything and preserves all six named classes | **PASS** | 0 MAJOR, 4 MINOR. (Image) for E<sub>max</sub> — the note's own press point — checks, and is the *easiest* of the six, not the hardest. D(iii)'s coordinate formula checks. |
| **Proposition 1** (§5) — the equivariance no-go (D1) | **PASS-WITH-REPAIRS** | 1 MAJOR (**P-2**: the proof consumes [x-03] Thm 6.1, whose hypothesis E ⊆ E<sub>max</sub> the proposition does not state and which **fails for E<sub>tors</sub>**, one of the six classes the proposition explicitly admits), 1 MINOR. Conclusion unaffected once the hypothesis is added. |
| **§4 Consequence 2** — the transport reading (D3) | **PASS-WITH-REPAIRS** | 1 MAJOR (**A-4**: the displayed identification carries a clause that is false under either reading — the transported condition is *not* admissible, while E(a₀) *is*, hence is N-invariant). The branch D3 itself survives. |
| **§3 freshman's-dream N-invariance argument** | **PASS**, strengthened | 0 findings; a strictly stronger statement is supplied and proved (§10). |
| **§7 Haar formal count** | **PASS-WITH-REPAIRS** | 1 MAJOR (**H-1**: "the integrand is constant" is not established by equality of orbit lengths; a fill is supplied *together with an explicit statement of how weak it is*). |
| Citation / transcription layer, §§1–7 | — | 5 MINOR (one of them a displayed identity that is false as transcribed; checked against a page render). |

**Overall on the assigned item: PASS-WITH-REPAIRS. FATAL 0 · MAJOR 5 · MINOR 18.**

**The trichotomy D1–D3 survives the pass.** None of the five MAJOR findings touches the truth of D1, D2 or D3. A-1/A-2 are defects in the *statement and proof* of Lemma A, not in the only case the note ever applies it to (κ ≅ F̄<sub>p</sub>); A-4 is a mis-identification inside D3 whose corrected form still yields D3; P-2 is a one-clause hypothesis omission that every application of Proposition 1 already satisfies; H-1 lies in Road 2, a positive-road proposal explicitly parked in DQ-M, which carries none of the trichotomy. After the repairs in §12 the note's §0 verdict is, in my judgment, established at referee grade within the scope stated in §13.

---

## 1. Sources: what was opened, and the verbatim anchors

### 1.1 [x-03] Deninger, *Dynamical systems for arithmetic schemes*, arXiv:1807.06400v4
`fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf`. **Printed page = PDF page** in this file (checked by extracting the trailing folio of PDF pages 27 and 33: they print "27" and "33"). All [x-03] page references below are therefore unambiguous.

Anchors read verbatim this session (transcriptions of the `pdftotext -layout` output with overlines/hats restored; where restoration was not obvious the page was rendered — §1.4):

**(a) p. 27 — the two conditions and Definition 4.1 (admissibility).**
> "(Tors) the group ker(χ)<sub>tors</sub> = ker(χ |<sub>µ(κ)</sub>) is finite and |(ker χ)<sub>tors</sub>| ∈ N₀."
> "(Image) Only if char κ > 0. If χ(κ<sup>×</sup>) is torsion, then κ<sup>×</sup> is torsion as well, i.e. κ<sup>×</sup> ⊗ Q ≠ 0 implies χ(κ<sup>×</sup>) ⊗ Q ≠ 0."
> "**Definition 4.1.** A class E of characters χ : κ<sup>×</sup> → C<sup>×</sup> on algebraically closed fields κ is (N₀−)admissible if for any σ ∈ Autκ resp. ν ∈ N₀ the character χ is in E **if and only if** χ ◦ σ resp. χ<sub>ν</sub> = χ ◦ ( )<sup>ν</sup> is in E. Moreover the characters in E should satisfy (Tors)."

Also on p. 27: "The best condition on the characters P<sup>×</sup> is not clear to me." And **Proposition 4.2**: "the set X<sup>•</sup>(C)<sub>E</sub> = {(x, P<sup>×</sup>) ∈ X<sup>•</sup>(C) | P<sup>×</sup> is in E} ⊂ X<sup>•</sup>(C) is G-invariant. It is foreward- and backward invariant under the N₀-action… The monoid N₀ acts by injections on X<sup>•</sup>(C)<sub>E</sub> and X<sub>0</sub><sup>•</sup>(C)<sub>E</sub>."

**(b) pp. 28–29 — the six named example classes, verbatim.**
> "Here are examples of admissible classes E of characters. **Example.** 1) E<sub>tors</sub> : (Tors) holds  2) E<sub>max</sub> : (Tors) and (Image) hold  3) E<sub>f</sub> : (Tors) and ker χ is finite. Equivalently: | ker χ| ∈ N₀  4) E<sub>fg</sub> : (Tors) and ker χ is finitely generated  5) E<sub>fd</sub> : (Tors) and ker χ ⊗ Q is finite dimensional  6) E<sub>fd0</sub> : (Tors) and (ker χ |<sub>κ(x₀)<sup>×</sup></sub>) ⊗ Q is finite dimensional where x₀ = π(x) under the projection π : X → X₀."
> "We have inclusions in the appropriate sense  E<sub>f</sub> ⊂ E<sub>fg</sub> ⊂ E<sub>fd</sub> ⊂ E<sub>fd0</sub> ⊂ E<sub>max</sub> ⊂ E<sub>tors</sub>."

**(c) p. 29 — the Remark the whole probe turns on, verbatim.**
> "Incidentally, in the p-adic case where we will deal with multiplicative maps P into a p-adic valuation ring and N₀ = p<sup>Z</sup>, the right condition E is the following: P is additive mod p. This can be rephrased in terms of absolute values and translated to the case where C is the complex number field. **However the resulting class E is not N-invariant.**"

Also p. 29, the *other* technical use of the word "stable", which matters for finding D-3:
> "We call a class E of characters χ : κ<sup>×</sup> → C<sup>×</sup> on algebraically closed fields κ **stable** if χ ∈ E implies that χ |<sub>κ̃<sup>×</sup></sub> ∈ E for all algebraically closed subfields κ̃ ⊂ κ. **All classes in the example are stable except for (Image) and hence E<sub>max</sub>.**"

**(d) p. 31 — the standing hypothesis on C, and the choice of ι.**
> "Let C be an algebraically closed field which satisfies the conditions before Corollary 4.4." … "Fix an injective homomorphism ι : µ(K) ↪ µ(C). It exists by our assumptions on char K₀ and char C." … "(32) i<sub>x</sub> : µ<sup>(p)</sup>(K) = µ<sup>(p)</sup>(O<sub>X,x</sub>) →∼ κ(x)<sup>×</sup>."

**(e) p. 32 — (34) and (35), the packet coordinates.**
> "The group of automorphisms of the abelian group κ(x)<sup>×</sup> is given by Ẑ<sup>×</sup><sub>(p)</sub> where Ẑ<sub>(p)</sub> = ∏<sub>l≠p</sub> Z<sub>l</sub>. We have a natural inclusion  **(34)  N x₀<sup>Ẑ</sup> = Gal(κ(x)/κ(x₀)) ↪ Aut(κ(x)<sup>×</sup>) = Ẑ<sup>×</sup><sub>(p)</sub>.**"
> "The monoid Ẑ<sup>×</sup><sub>(p)</sub> × N₀ acts by pre-composition on the set S of homomorphisms P<sup>×</sup> : κ(x)<sup>×</sup> → C<sup>×</sup> with finite cyclic kernel of order in N₀. We have a Ẑ<sup>×</sup><sub>(p)</sub> × N₀-equivariant surjection: **(35) Ẑ<sup>×</sup><sub>(p)</sub> × N₀ ↠ S, (a, ν) ↦ χ<sub>x</sub>·(a, ν) := χ<sub>x</sub> ◦ ( )<sup>a</sup> ◦ ( )<sup>ν</sup>.** Two elements (a, ν) and (a′, ν′) are in the same fibre of this map if and only if ν′ = νp<sup>n</sup> and a = p<sup>n</sup>a′ for some n ∈ Z."
> Earlier on the same page: "composing the fixed injection ι : µ(K) ↪ µ(C) above with (32) we obtain the injective character χ<sub>x</sub> = ι ◦ i<sub>x</sub><sup>−1</sup> : κ(x)<sup>×</sup> ↪ C<sup>×</sup>".

**(f) p. 33 — (38), (39), the fibration, and the non-canonicity warning.** Read **from a page render** (§1.4) because the text layer drops overlines and floats the superscript:
> "(38)  (Ẑ<sup>×</sup><sub>(p)</sub>/N x₀<sup>Ẑ</sup>) ×<sub>p<sup>Z</sup></sub> Q₀<sup>>0</sup> →∼ C<sub>x₀</sub>."
> "(39)  (Ẑ<sup>×</sup><sub>(p)</sub>/N x₀<sup>Ẑ</sup>) ×<sub>p<sup>Z/deg x₀</sup></sub> (Q₀<sup>>0</sup>/N x₀<sup>Z</sup>) →∼ C<sub>x₀</sub>."
> "The set C<sub>x₀</sub> fibres over the compact group  **Ẑ<sup>×</sup><sub>(p)</sub>/p<sup>Ẑ</sup> = Aut(F̄<sub>p</sub><sup>×</sup>)/Aut(F̄<sub>p</sub>) ,**  and the fibres are the Q₀<sup>>0</sup>-orbits in C<sub>x₀</sub>."
> "The maps (37), (38) and the fibration map **depend on our choices of x and ι**. On the other hand, the projection **(40)** C<sub>x₀</sub> → Q₀<sup>>0</sup>/p<sup>Z</sup> … is canonical".
> p. 32 bottom, the isotropy: "It follows that all points P₀ ∈ C<sub>x₀</sub> have isotropy subgroup (Q₀<sup>>0</sup>)<sub>P₀</sub> = N x₀<sup>Z</sup>."

**(g) p. 34 — Theorem 5.2, with its hypothesis.**
> "**Theorem 5.2.** Let E be an admissible class **with E ⊂ E<sub>max</sub>**. The following decomposition holds, where x₀ runs over the points of X₀ with finite residue field κ(x₀) and where C<sup>E</sup><sub>x₀</sub> = C<sub>x₀</sub> ∩ X̌₀(C)<sub>E</sub> :  (47) {P₀ ∈ X̌₀(C)<sub>E</sub> | (Q₀<sup>>0</sup>)<sub>P₀</sub> ≠ 1} = ∐<sub>x₀</sub> C<sup>E</sup><sub>x₀</sub>. For any point P₀ ∈ C<sup>E</sup><sub>x₀</sub> the isotropy group of P₀ is (Q₀<sup>>0</sup>)<sub>P₀</sub> = N x₀<sup>Z</sup> … **If e.g. E ⊃ E<sub>f</sub> then C<sup>E</sup><sub>x₀</sub> = C<sub>x₀</sub>.**"

**(h) p. 38 — the suspension, and the fibration *of the packet itself*.**
> "consider the suspension  X₀ = X̌₀(C)<sub>E</sub> ×<sub>Q₀<sup>>0</sup></sub> R<sup>>0</sup>. It is the quotient of X̌₀(C)<sub>E</sub> × R<sup>>0</sup> by the right Q₀<sup>>0</sup>-action given by (P₀, u)q = (P₀q, q<sup>−1</sup>u) = (F<sub>q</sub>(P₀), q<sup>−1</sup>u)"; "φ<sup>t</sup>([P₀, u]) = [P₀, ue<sup>t</sup>]"; "Γ<sub>x₀</sub> = C<sub>x₀</sub> ×<sub>Q₀<sup>>0</sup></sub> R<sup>>0</sup> ⊂ X₀".
> "**Thus all R<sup>>0</sup>-orbits in Γ<sub>x₀</sub> are circles R<sup>>0</sup>/N x₀<sup>Z</sup> and Γ<sub>x₀</sub> fibres over Ẑ<sup>×</sup><sub>(p)</sub>/p<sup>Ẑ</sup> = Aut(F̄<sub>p</sub><sup>×</sup>)/Aut(F̄<sub>p</sub>) with fibres the R<sup>>0</sup>-orbits in Γ<sub>x₀</sub>.** We set Γ<sup>E</sup><sub>x₀</sub> = C<sup>E</sup><sub>x₀</sub> ×<sub>Q₀<sup>>0</sup></sub> R<sup>>0</sup> … If e.g. E<sub>f</sub> ⊂ E then Γ<sup>E</sup><sub>x₀</sub> = Γ<sub>x₀</sub>."

**(i) p. 39 — Theorem 6.1, with its hypothesis.**
> "**Theorem 6.1.** Let E be an admissible class **with E ⊂ E<sub>max</sub>**. The following decomposition holds, where x₀ runs over the points of X₀ with finite residue fields κ(x₀):  {x₀ ∈ X₀ | (R<sup>>0</sup>)<sub>x₀</sub> ≠ 1} = ∐<sub>x₀</sub> Γ<sup>E</sup><sub>x₀</sub>. For any point x₀ ∈ Γ<sup>E</sup><sub>x₀</sub> the isotropy group of x₀ is (R<sup>>0</sup>)<sub>x₀</sub> = N x₀<sup>Z</sup>."
> "**Any periodic orbit γ in X₀ is contained in Γ<sup>E</sup><sub>x₀</sub> for a uniquely determined point x₀ of X₀ with finite residue field.**"

**(j) p. 40 — the topology, and the S4 question.**
> "we give X<sup>•</sup>(C) the topology of pointwise convergence… Since R is countable, X<sup>•</sup>(C) is a metrizable topological space."
> "Is there a sub-dynamical system Y₀ ⊂ X₀ = X̌₀(C) ×<sub>Q<sup>>0</sup></sub> R<sup>>0</sup> **or at least one which maps to X₀** such that dim Y₀ = 2d + 1 … and such that Y₀ contains at least one periodic orbit in Γ<sub>x₀</sub> for every closed point x₀ of X₀?"

**(k) pp. 5–6 — the introduction lines the note consumes.** Page 5: "There is a minimal condition E for which our theorems hold but it does not look natural." Page 6 (the page break falls before this sentence — see finding T-2): "Incidentally, if we consider points of W<sub>rat</sub>(X) with values in rings without “small multiplicative subgroups” like the complex number field C **this process does not give more points**." Page 6 also: "The answer is simple, Y<sup>⋄</sup> consists of all the diagrams in X<sup>⋄</sup><sub>c</sub>(o) whose maps are not only multiplicative but mod p also additive." And: "Thus the process of “completion” to pass from X̌₀(o) to X<sup>⋄</sup>₀(o) was necessary to obtain something interesting."

**(l) p. 89 — the local setting and the monoid reduction.**
> "Let o be a p-adically complete rank one valuation ring with quotient field C, maximal ideal m and residue field k of characteristic p." … "**In the following we only consider the monoid N₀ generated by p i.e. the F<sub>p</sub> = ( )<sup>p</sup> action.**"
> *Note: p. 89 does **not** assume C or k algebraically closed. See finding A-3.*

**(m) p. 94 — Definition 14.5, and the mechanism (172).**
> "**Definition 14.5.** … Y̌<sub>α</sub> = {(x, y, P̌<sub>y</sub>) ∈ X̌<sub>c</sub>(o) | |f(P̌<sub>y</sub>)| ≤ α for all f ∈ I<sub>y</sub>} = {(x, y, P̌<sub>y</sub>) ∈ X̌<sub>c</sub>(o) | |P̌<sub>y</sub>(r + s) − P̌<sub>y</sub>(r) − P̌<sub>y</sub>(s)| ≤ α for r, s ∈ Ô<sup>♭</sup><sub>{x},y</sub>}." … "For α = 1/p we are looking at multiplicative maps P̌<sub>y</sub> which mod p are also additive. Set Y̌ = Y̌<sub>1/p</sub>."
> "Choose an element ω<sub>α</sub> ∈ o with α ≤ |ω<sub>α</sub>| < 1. Then (x, y, P̌<sub>y</sub>) ∈ Y̌<sub>α</sub> gives a ring homomorphism P̌<sub>y</sub> : ZÔ<sup>♭</sup><sub>{x},y</sub> → o with P̌<sub>y</sub>(I<sub>y</sub>) ⊂ ω<sub>α</sub>o and hence an induced ring homomorphism **(172)** W<sub>p</sub>(P̌<sub>y</sub>) : W<sub>p</sub>(Ô<sup>♭</sup><sub>{x},y</sub>) = lim<sub>n</sub> ZÔ<sup>♭</sup><sub>{x},y</sub>/I<sub>y</sub><sup>n</sup> → lim<sub>n</sub> o/ω<sub>α</sub><sup>n</sup> = o."
> **Proposition 14.7** (statement p. 94): "For 0 < α < 1 we have F<sub>p</sub>(Y̌<sub>α</sub>) = Y̌<sub>α</sub> and Y̌<sub>α</sub> ⊂ Y̌, and hence Y̌<sub>α</sub> = Y̌ for α ≥ 1/p."

**(n) p. 95 — the proof of 14.7, both arguments.** The ultrametric estimate, verbatim: "|(P̌<sub>y</sub>(r + s) − P̌<sub>y</sub>(r) − P̌<sub>y</sub>(s))<sup>p<sup>ν</sup></sup> + pc| for some c ∈ o ≤ max(|P̌<sub>y</sub>(r+s) − P̌<sub>y</sub>(r) − P̌<sub>y</sub>(s)|<sup>p<sup>ν</sup></sup>, |p|) ≤ max(α<sup>p<sup>ν</sup></sup>, 1/p)". And the second proof via diagram (175): "It follows that the composition **(176)** Ô<sup>♭</sup><sub>{x},y</sub> → o → o/p is additive i.e. that P̌<sub>y</sub> ∈ Y̌<sub>1/p</sub>." *(Note that |p| = 1/p is Deninger's normalization, fixed by this display.)*

**(o) p. 99 — Definition 14.12 = (183), and the sentence that defines the whole probe.**
> "**Definition 14.12.** For any real number 0 < α < 1 we define a G-invariant subspace Y<sup>⋄</sup><sub>α</sub> of X<sup>⋄</sup><sub>c</sub>(o) just like we defined Y̌<sub>α</sub> ⊂ X̌<sub>c</sub>(o) in Definition 14.5  **(183)** Y<sup>⋄</sup><sub>α</sub> = {(x, y, P̂<sub>y</sub>) ∈ X<sup>⋄</sup><sub>c</sub>(o) | |f(P̂<sub>y</sub>)| ≤ α for all f ∈ I<sub>y</sub>} = {… | |P̂<sub>y</sub>(r + s) − P̂<sub>y</sub>(r) − P̂<sub>y</sub>(s)| ≤ α for r, s ∈ Ô<sup>♭</sup><sub>{x},y</sub>}."
> "**I do not know how to transport such conditions to the points of X̌(C), where X is a scheme of finite type over spec Z and C is the complex number field.**"

**(p) pp. 100–101 — Propositions 14.13 and 14.14.** 14.13: "For 0 < α < 1 we have F<sub>p</sub>(Y<sup>⋄</sup><sub>α</sub>) = Y<sup>⋄</sup><sub>α</sub> and Y<sup>⋄</sup><sub>α</sub> ⊂ Y<sup>⋄</sup> and hence Y<sup>⋄</sup><sub>α</sub> = Y<sup>⋄</sup> for α ≥ 1/p." 14.14 (statement p. 100, **proof pp. 100–101**): "Let A be a p-adically complete ring. Then there is a natural bijection between (continuous) multiplicative maps χ : lim<sub>( )<sup>p</sup></sub>A → o with χ(1) = 1, χ(0) = 0 for which the composition χ<sup>♭</sup> : A<sup>♭</sup> ≅ lim<sub>( )<sup>p</sup></sub>A → o → o/p is additive and (continuous) ring homomorphisms χ<sup>♭</sup> : A<sup>♭</sup> → o<sup>♭</sup>."

**(q) p. 104 — Remark 14.17 (the coefficient-automorphism action).**
> "In particular G × Aut(o) operates F<sub>p</sub>-equivariantly on X<sup>•</sup>(o) = W<sub>rat</sub>(X)(o) and X̌(o). **Since automorphisms of o are p-adically continuous** we have compatible G × Aut(o)-operations on X<sup>•</sup><sub>c</sub>(o), X̌<sub>c</sub>(o), X<sup>⋄</sup><sub>c</sub>(o) and Y<sup>⋄</sup> in the obvious way."

**(r) pp. 105–106 — where the algebraically-closed hypotheses actually are.**
> p. 105: "**From now on let o be a p-adically complete rank one valuation ring with (complete) algebraically closed quotient field C of characteristic zero.** Let m be its maximal ideal and" — p. 106 — "**k its algebraically closed residue field of characteristic p.** Then o<sup>♭</sup> is a complete rank one valuation ring of equicharacteristic p with complete algebraically closed quotient field C<sup>♭</sup> of characteristic p, maximal ideal m<sup>♭</sup> = lim<sub>( )<sup>p</sup></sub>m/po and residue field k. **Then k is also a subfield of o<sup>♭</sup> such that k ⊂ o<sup>♭</sup> → k is the identity.**"
> p. 106, the identification of κ: "Here κ is the common residue field of o<sub>K</sub>, ô<sub>K</sub> and ô<sup>♭</sup><sub>K</sub>, **an algebraic closure of κ₀**".

**(s) pp. 113–114 — Theorem 15.6.**
> p. 113: "For (x, y) = (s, s) the continuous local ring homomorphisms P̂<sup>♭</sup><sub>y</sub> : κ → o<sup>♭</sup> with P̂<sup>♭</sup><sub>y</sub>(f) ≠ 0 for all 0 ≠ f ∈ lim<sub>( )<sup>p</sup></sub>κ ≅ κ **are simply the ring homomorphisms P̂<sup>♭</sup><sub>y</sub> : κ ↪ k ⊂ o<sup>♭</sup>**".
> p. 113: "**Theorem 15.6.** Let X₀ = spec o<sub>K₀</sub> with generic point η₀ and closed point s₀. 1) There is a natural **G × Aut(o) × ⟨F<sub>p</sub>⟩-equivariant identification** Y<sup>⋄</sup> = Hom<sub>cont</sub>(ô<sup>♭</sup><sub>K</sub>, o<sup>♭</sup>) sending (x, y, P̂<sub>y</sub>) to P̂<sup>♭</sup><sub>y</sub>. Under the projection pr<sub>X</sub> : Y<sup>⋄</sup> → X<sub>top</sub> we have Y<sup>⋄</sup><sub>η</sub> := pr<sub>X</sub><sup>−1</sup>(η) = Hom<sub>cont,inj</sub>(ô<sup>♭</sup><sub>K</sub>, o<sup>♭</sup>)" — p. 114 — "and **Y<sup>⋄</sup><sub>s</sub> := pr<sub>X</sub><sup>−1</sup>(s) = Hom(κ, k)**."
> p. 114: "(224) Y<sup>⋄</sup><sub>0s₀</sub> := pr<sub>X₀</sub><sup>−1</sup>(s₀) →∼ ∐<sub>τ₀</sub>{0}/o<sup>×</sup><sub>K₀</sub> = **Hom(κ₀, k)**."
> p. 114: "6) **The only periodic (i.e. finite) orbit of the F<sub>p</sub>-action on Y<sup>⋄</sup>₀ is Y<sup>⋄</sup><sub>0s₀</sub>. It has order log<sub>p</sub> N(π₀) = r if q = p<sup>r</sup>.**"

**(t) pp. 115–116 — Prop. 15.7 and Prop. 15.8.** 15.7 gives e(f)(ϕ) = (θ ◦ W<sub>p</sub>(ϕ))(f) on Y<sup>⋄</sup> = Hom<sub>cont</sub>(ô<sup>♭</sup><sub>K</sub>, o<sup>♭</sup>). 15.8: "For X₀ = spec Z<sub>p</sub> and o = o<sub>p</sub>, the set Y̌₀ ⊂ Y<sup>⋄</sup>₀ consists of the F<sub>p</sub>-fixed point s₀ = (o<sup>♭</sup><sub>p</sub> → F<sub>p</sub> → o<sup>♭</sup><sub>p</sub>)G and the (infinite) F<sub>p</sub><sup>Z</sup>-orbit of η₀ = (o<sup>♭</sup><sub>p</sub> →<sup>id</sup> o<sup>♭</sup><sub>p</sub>)G."

### 1.2 [x-06] Deninger, *Primes, knots and periodic orbits*, arXiv:2301.11643
`fetched/x-06-deninger-2024-primes-knots-and-periodic-orbits.pdf`. Pages read: 10–13.

> p. 11: "In general, the dynamical system (X₀, φ<sup>t</sup>) **has too many periodic orbits, since the N-space W<sub>rat</sub>(X₀)(C) does not know enough about the addition in O<sub>X₀</sub>. In the local p-adic situation below, we know the right modification to make. However in the global case presently we can only impose an “admissible” condition E** on the characters P<sup>×</sup> : κ(x)<sup>×</sup> → C<sup>×</sup>".
> pp. 11–12, **Theorem 4.2**: "{x₀ ∈ X₀<sup>E</sup> | φ<sup>t</sup>(x₀) = x₀ for some t > 0} = ∐<sub>x₀</sub> Γ<sub>x₀</sub>. … **The compact subsets Γ<sub>x₀</sub> ⊂ X₀ consist of periodic orbits of length log N x₀ where N x₀ = |κ(x₀)| … and they are pairwise disjoint. In fact Γ<sub>x₀</sub> is a fibre space over the compact group Aut(F̄<sub>p</sub><sup>×</sup>)/Aut(F̄<sub>p</sub>) where p = char κ(x) with fibres the compact orbits in Γ<sub>x₀</sub>.**" And one line later: "compact packets of periodic orbits **all of which have length log N x₀ i.e. log p if X₀ = spec Z**."
> p. 13, **Theorem 4.4** and the remark: "In view of Theorem 4.3 the map in the theorem **is not a homeomorphism since X₀ is connected, whereas the left hand side is disconnected**."
> p. 13: "**The absence of the Steinberg relations in rational cohomology is an indication that** the space X<sub>F</sub>(C) and hence also **our space W<sub>rat</sub>(X)(C) do not encode enough information about the additive structure of F resp. O<sub>X</sub>.**"

### 1.3 [D25] Deninger, *Rational Witt vectors and associated sheaves*, arXiv:2508.05329v1
`fetched-r3/r3s-22-deninger-rational-witt-vectors-associated-sheaves-arxiv-2508.05329v1-SESSION8-FETCH.pdf`. Pages read: 1–3 (introduction, in full).
> pp. 2–3, verbatim: "**The algebra ZA knows nothing about the addition in A. However, the larger G is, the more information the ring W<sub>rat</sub>(A) has about the additive structure of A. It may be interesting to experiment with stronger descent conditions than the Galois descent above to obtain replacements of W<sub>rat</sub>(A) which know even more about the additive structure of A to remedy the defects in the constructions of [KS16] and [Den24].**"
> The displayed formula the note glosses is the paper's own **(3)**, on p. 2: "W<sub>rat</sub>(Ā) = (ZĀ)<sup>G</sup> ⟶ C(X<sub>A</sub>, C)". (See finding T-3: the gloss is right, the placement inside the quotation marks is not.)

### 1.4 The one display whose text layer is unreliable — read by page render
`pdftotext` drops the overlines on F̄<sub>p</sub> and floats the superscript × onto the preceding line, so the p. 33 display extracts as "Ẑ<sup>×</sup><sub>(p)</sub>/p<sup>Ẑ</sup> = Aut(F<sub>p</sub>)/Aut(F<sub>p</sub>)" with a stray "×" above. I rendered [x-03] p. 33 and [x-06] p. 12 at 200 dpi (`pdftoppm -r 200 -png`) and read the images. Both read, unambiguously:
> **Aut(F̄<sub>p</sub><sup>×</sup>) / Aut(F̄<sub>p</sub>)** — the × is inside the *first* Aut, on F̄<sub>p</sub>; the *second* Aut is of the **field** F̄<sub>p</sub>.
This is the anchor for finding T-1. (Independent confirmation that this must be the reading: Aut(F<sub>p</sub>) is the trivial group, so "Aut(F̄<sub>p</sub>)/Aut(F<sub>p</sub>)" would be Ẑ, not Ẑ<sup>×</sup><sub>(p)</sub>/p<sup>Ẑ</sup>.)

### 1.5 [r3s-08] Morishita, arXiv:2508.15971
`fetched-r3/r3s-08-morishita-deninger-cc-bridge-2508.15971.pdf` — present on disk; **not consulted for any claim in this report**, in line with the 9.3 adjudication §4 item 4 (do not cite it for topology).

### 1.6 Program-internal documents
`results/c3-r/probe-9.3-adjudication.md` (read in full; its §2 anchors were *re-read by me in the sources*, not imported); `results/c3-r/probe-9.4-note.md` (in full); `results/corpus-routing.md` standing caveats 1–20 (read before citing any corpus file; none of caveats 1–20 touches [x-03], [x-06] or [D25]).

---
