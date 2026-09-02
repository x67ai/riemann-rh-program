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

## 2. The standing picture, re-derived (used by all five statements)

Fix X₀ = Spec Z from here on, x₀ = (p), X = the normalization of Spec Z in Q̄, x a point of X over x₀, so κ(x) ≅ F̄<sub>p</sub> and N x₀ = p, deg x₀ = 1. E is an admissible class in the sense of Def. 4.1 (§1.1(a)).

**(2.1) κ(x)<sup>×</sup> = F̄<sub>p</sub><sup>×</sup> ≅ ⊕<sub>ℓ≠p</sub> Q<sub>ℓ</sub>/Z<sub>ℓ</sub>, and Aut of it is Ẑ<sup>×</sup><sub>(p)</sub>.** F̄<sub>p</sub><sup>×</sup> = ∪<sub>n</sub> F<sub>p<sup>n</sup></sub><sup>×</sup> is a torsion abelian group, all of whose elements have order prime to p, and for each ℓ ≠ p its ℓ-primary part is the increasing union of cyclic groups of ℓ-power order, i.e. Q<sub>ℓ</sub>/Z<sub>ℓ</sub>. End(Q<sub>ℓ</sub>/Z<sub>ℓ</sub>) = Z<sub>ℓ</sub> and Hom(Q<sub>ℓ</sub>/Z<sub>ℓ</sub>, Q<sub>ℓ′</sub>/Z<sub>ℓ′</sub>) = 0 for ℓ ≠ ℓ′, so End(F̄<sub>p</sub><sup>×</sup>) = ∏<sub>ℓ≠p</sub>Z<sub>ℓ</sub> = Ẑ<sub>(p)</sub> and Aut = Ẑ<sup>×</sup><sub>(p)</sub>. This is [x-03] (34), §1.1(e), which I therefore do not merely import: it is re-derived. ✔

**(2.2) Aut(µ(C)) = Ẑ<sup>×</sup> for C algebraically closed of characteristic 0.** µ(C) = ∪<sub>n</sub>µ<sub>n</sub>(C) with µ<sub>n</sub>(C) cyclic of order n (X<sup>n</sup> − 1 is separable in characteristic 0 and splits), so µ(C) ≅ Q/Z = ⊕<sub>ℓ</sub>Q<sub>ℓ</sub>/Z<sub>ℓ</sub> and, exactly as in (2.1), End(Q/Z) = Ẑ, Aut(Q/Z) = Ẑ<sup>×</sup>. ✔

**(2.3) The packet, its base, and the flow.** By §1.1(f) the Q₀<sup>>0</sup>-set C<sub>x₀</sub> ⊂ X̌₀(C)<sub>E<sub>tors</sub></sub> is (Ẑ<sup>×</sup><sub>(p)</sub>/p<sup>Ẑ</sup>) ×<sub>p<sup>Z</sup></sub> Q₀<sup>>0</sup> (using N x₀<sup>Ẑ</sup> = p<sup>Ẑ</sup> for X₀ = Spec Z), it fibres over **B<sub>p</sub> := Ẑ<sup>×</sup><sub>(p)</sub>/p<sup>Ẑ</sup>**, and *the fibres are exactly the Q₀<sup>>0</sup>-orbits*. Suspending, §1.1(h) states the same for Γ<sub>x₀</sub> = C<sub>x₀</sub> ×<sub>Q₀<sup>>0</sup></sub> R<sup>>0</sup> directly: all R<sup>>0</sup>-orbits in Γ<sub>x₀</sub> are circles of length log p and *the fibres of Γ<sub>x₀</sub> → B<sub>p</sub> are exactly the R<sup>>0</sup>-orbits*.
*The elementary translation, verified so that nothing is imported:* [P₀, u] and [P₀′, u′] lie on a common φ-orbit ⟺ ∃t: [P₀, ue<sup>t</sup>] = [P₀′, u′] ⟺ ∃q ∈ Q₀<sup>>0</sup>: P₀′ = F<sub>q</sub>(P₀) and u′ = q<sup>−1</sup>ue<sup>t</sup> ⟺ P₀ and P₀′ lie on one Q₀<sup>>0</sup>-orbit. So "flow orbit" and "Q<sup>>0</sup>-orbit" are the same partition, and **two points of Γ<sub>p</sub> with different base classes lie on different closed orbits.** ✔
*Also verified:* F<sub>ν</sub> acts on the coordinates of (35)/(38) by (a, ν₀) ↦ (a, ν₀ν), i.e. **on the second coordinate only, so the base class is fixed by every Frobenius and by the whole flow.** ✔

**(2.4) B<sub>p</sub> is an infinite profinite group, hence uncountable.** Ẑ<sup>×</sup><sub>(p)</sub> = ∏<sub>ℓ≠p</sub>Z<sub>ℓ</sub><sup>×</sup> is profinite; p<sup>Ẑ</sup> is by definition the closure of ⟨p⟩, so B<sub>p</sub> is a compact Hausdorff (indeed profinite) group. *Infinite:* let T be a finite set of odd primes ≠ p. Reduce Ẑ<sup>×</sup><sub>(p)</sub> ↠ ∏<sub>ℓ∈T</sub>(Z/ℓ)<sup>×</sup> ↠ ∏<sub>ℓ∈T</sub>(Z/ℓ)<sup>×</sup>/((Z/ℓ)<sup>×</sup>)<sup>2</sup> ≅ (C₂)<sup>|T|</sup> (each (Z/ℓ)<sup>×</sup> is cyclic of even order ℓ−1 for ℓ odd). The image of the *whole* subgroup p<sup>Ẑ</sup> is the cyclic subgroup generated by the image of p, of order ≤ 2. Hence B<sub>p</sub> surjects onto a group of order ≥ 2<sup>|T|−1</sup>, and |T| is unbounded. *Uncountable:* an infinite profinite group has no isolated points (if one point were isolated then by homogeneity all are, so the group would be discrete and compact, hence finite), and a nonempty compact Hausdorff space with no isolated points is uncountable by Baire. ✔ *(The 9.3 adjudication re-derived this too; I did not import it.)*

**(2.5) The image of Aut<sub>ring</sub>(F̄<sub>p</sub>) in Aut<sub>group</sub>(F̄<sub>p</sub><sup>×</sup>) is p<sup>Ẑ</sup>.** Aut(F̄<sub>p</sub>) = Gal(F̄<sub>p</sub>/F<sub>p</sub>) is topologically generated by the Frobenius y ↦ y<sup>p</sup>, whose image in Aut(F̄<sub>p</sub><sup>×</sup>) = Ẑ<sup>×</sup><sub>(p)</sub> is the element p; the map is injective because a field automorphism of F̄<sub>p</sub> is determined by its restriction to F̄<sub>p</sub><sup>×</sup>. Hence the image is the closed subgroup p<sup>Ẑ</sup> and **B<sub>p</sub> = coker(Aut<sub>ring</sub>(F̄<sub>p</sub>) ↪ Aut<sub>group</sub>(F̄<sub>p</sub><sup>×</sup>))** — which is literally Deninger's own p. 33 display (§1.4). ✔

---

## 3. LEMMA A — verdict **PASS-WITH-REPAIRS** (2 MAJOR, 2 MINOR)

### 3.1 What the note states

> "Let o be as in §2 (residue field k algebraically closed of char p), κ an algebraically closed field of characteristic p, and P: κ → o multiplicative with P(0) = 0, P(1) = 1, whose restriction to κ<sup>×</sup> is a group homomorphism into o (values automatically in µ<sup>(p)</sup>(o), the prime-to-p roots of unity, since κ<sup>×</sup> is prime-to-p torsion). Then |P(r+s) − P(r) − P(s)| ≤ |p| for all r, s ∈ κ **iff** P = [·]∘τ for a unique field embedding τ: κ ↪ k, where [·] is the Teichmüller section of the reduction µ<sup>(p)</sup>(o) ≅ µ<sup>(p)</sup>(k)."

### 3.2 FINDING A-1 (MAJOR) — the hypothesis "κ an algebraically closed field of characteristic p" is false as used, and the conclusion does not typecheck

The parenthetical asserts "**κ<sup>×</sup> is prime-to-p torsion**" for an arbitrary algebraically closed field κ of characteristic p. **That is false.** κ<sup>×</sup> is torsion if and only if κ is algebraic over F<sub>p</sub>, i.e. (κ being algebraically closed) if and only if **κ ≅ F̄<sub>p</sub>**. *Counterexample to the parenthetical:* κ = the algebraic closure of F<sub>p</sub>(t); then t ∈ κ<sup>×</sup> has infinite order, since t<sup>n</sup> = 1 would make t algebraic over F<sub>p</sub>.

The damage is not confined to the parenthetical. The note *defines* [·] as "the Teichmüller section of the reduction µ<sup>(p)</sup>(o) ≅ µ<sup>(p)</sup>(k)", i.e. as a map **defined only on µ<sup>(p)</sup>(k) ∪ {0}**. So the expression "[·]∘τ" is only well-formed when τ(κ) ⊆ µ<sup>(p)</sup>(k) ∪ {0}, i.e. again only when κ<sup>×</sup> is torsion, i.e. only when κ ≅ F̄<sub>p</sub>. **The stated biconditional therefore does not typecheck outside κ ≅ F̄<sub>p</sub>.**

*BREAK attempt (does the lemma become false, or merely ill-posed?).* Two regimes. (i) If κ ⊋ F̄<sub>p</sub> and k = F̄<sub>p</sub>, both sides are empty — there is no ring embedding κ ↪ k (transcendence degree), and the left side is empty because the forward implication (§3.4 step 1) would produce one — so the biconditional is *vacuously true* but says nothing. (ii) If κ ⊋ F̄<sub>p</sub> and k ⊇ κ, the right side is nonempty but the formula "[·]∘τ" has no meaning under the note's own definition of [·]. In neither regime is a counterexample available, and in the second the statement can be rescued (see the second paragraph of R-A1): Deninger himself provides the needed section, "**Then k is also a subfield of o<sup>♭</sup> such that k ⊂ o<sup>♭</sup> → k is the identity**" ([x-03] p. 106, §1.1(r)), whence the composite k ⊂ o<sup>♭</sup> →<sup>♯</sup> o is a multiplicative section of o ↠ k defined on all of k. **But that section depends on a choice of coefficient field of o<sup>♭</sup> and is not canonical, whereas on µ<sup>(p)</sup> the section is unique.** That is exactly why restricting to κ ≅ F̄<sub>p</sub> is the right repair rather than generalizing.

**Severity MAJOR: the note must change.** Impact on the note's own argument: **none.** Lemma A is applied in §4 only at char-p packet points of X₀ = Spec Z, where κ(x) ≅ F̄<sub>p</sub>, and in the consistency check against Thm 15.6, where "κ is the common residue field of o<sub>K</sub>, ô<sub>K</sub> and ô<sup>♭</sup><sub>K</sub>, **an algebraic closure of κ₀**" ([x-03] p. 106) — a finite field's algebraic closure, i.e. again F̄<sub>p</sub>. Replacement text: **R-A1**.

### 3.3 FINDING A-2 (MAJOR) — the converse's justification is unavailable under the note's own hypotheses; the statement is nevertheless TRUE

The note proves (⇐) thus: "[a] + [b] − [a+b] ∈ V W(k) = p W(k) in the Witt ring W(k) ⊆ o (first ghost/component coordinates agree; V F = p on Witt vectors of a perfect ring), so the defect of [·]∘τ has absolute value ≤ |p|."

Three separate problems, each fatal to the *argument* (not to the statement):

1. **"W(k) ⊆ o" is not available.** o is a p-adically complete rank-1 valuation ring with residue field k. A ring homomorphism W(k) → o lifting id<sub>k</sub> is *not* automatic: the universal property of p-typical Witt vectors of a perfect F<sub>p</sub>-algebra produces Hom<sub>ring</sub>(W(k), o) ≅ Hom<sub>ring</sub>(k, o/p), and the reduction map o/p ↠ o/m = k has kernel m/po, which is **not** nilpotent in general (for o = o<sub>C<sub>p</sub></sub>, m ⊋ po strictly), so no lift along it is provided by anything in the note or in [x-03].
2. **"V W(k) = p W(k)" is a fact about W(k), which is not the ring the defect lives in.** The defect [ā] + [b̄] − [ā+b̄] is computed in o, and no map from W(k) to o has been produced.
3. The identity is invoked from memory. Under standing order 5 it must be labelled — I label it **[classical, not on disk]** — and, since the note is a derivation, it must be replaced.

**The statement is true.** Here is a self-contained proof that uses nothing beyond integer binomial coefficients, multiplicativity, and the ultrametric inequality on o — no Witt vectors, no unramified lifting, no fact I could not verify.

> **(⇐), proved.** Let τ : F̄<sub>p</sub> ↪ k be a field embedding and let ζ = [τ(r)], ξ = [τ(s)], η = [τ(r+s)] ∈ µ<sup>(p)</sup>(o) ∪ {0} be the Teichmüller lifts. Set w = ζ + ξ and δ = w − η. Since reduction mod m is a ring homomorphism and sends ζ, ξ, η to τ(r), τ(s), τ(r+s) = τ(r) + τ(s), we have δ ∈ m, i.e. |δ| < 1. Choose f ≥ 1 with r, s, r+s ∈ F<sub>q</sub>, q = p<sup>f</sup>; then ζ<sup>q</sup> = ζ, ξ<sup>q</sup> = ξ, η<sup>q</sup> = η (each is either 0 or a (q−1)-st root of unity).
> *(a) Freshman's dream in o.* For any u, v ∈ o, (u+v)<sup>p</sup> = u<sup>p</sup> + v<sup>p</sup> + p·c with c = Σ<sub>0<i<p</sub> (1/p)binom(p,i) u<sup>i</sup>v<sup>p−i</sup> ∈ o (the binomials are divisible by p). Hence (u+v)<sup>p</sup> ≡ u<sup>p</sup> + v<sup>p</sup> (mod p o), and by induction (u+v)<sup>p<sup>n</sup></sup> ≡ u<sup>p<sup>n</sup></sup> + v<sup>p<sup>n</sup></sup> (mod p o) for every n ≥ 0.
> *(b) A p-power of w returns to w mod p.* Apply (a) with u = ζ, v = ξ and n a multiple of f: w<sup>p<sup>n</sup></sup> ≡ ζ<sup>p<sup>n</sup></sup> + ξ<sup>p<sup>n</sup></sup> = ζ + ξ = w (mod p o), because p<sup>n</sup> = q<sup>n/f</sup> and x<sup>q</sup> = x for x ∈ {ζ, ξ}.
> *(c) The same p-power drives w to η.* Apply (a) with u = η, v = δ: w<sup>p<sup>n</sup></sup> = (η + δ)<sup>p<sup>n</sup></sup> ≡ η<sup>p<sup>n</sup></sup> + δ<sup>p<sup>n</sup></sup> = η + δ<sup>p<sup>n</sup></sup> (mod p o), again using η<sup>q</sup> = η. Hence |w<sup>p<sup>n</sup></sup> − η| ≤ max(|δ|<sup>p<sup>n</sup></sup>, |p|).
> *(d) Conclude.* Since |δ| < 1 and |p| > 0, choose n a multiple of f with |δ|<sup>p<sup>n</sup></sup> ≤ |p| (possible: |δ|<sup>p<sup>n</sup></sup> → 0). Then by (b) |w − w<sup>p<sup>n</sup></sup>| ≤ |p| and by (c) |w<sup>p<sup>n</sup></sup> − η| ≤ |p|, so by the ultrametric inequality **|ζ + ξ − η| = |w − η| ≤ |p|**, which is the assertion |P(r) + P(s) − P(r+s)| ≤ |p| for P = [·]∘τ. ∎

**The constant is sharp.** Take p = 2, r = s = 1: ζ = ξ = 1, r+s = 0, η = 0, and the defect is exactly 2, of absolute value |p|. So "≤ |p|" cannot be improved to "< |p|", and Deninger's threshold α = 1/p in Def. 14.5 is attained. ✔

**Severity MAJOR** (the note's displayed proof must be replaced). Impact on the note's conclusions: none — the statement stands. Replacement text: **R-A2**.

### 3.4 Lemma A, re-derived in full (κ ≅ F̄<sub>p</sub>; k algebraically closed of characteristic p; o a p-adically complete rank-1 valuation ring with residue field k and |p| < 1)

**Step 0 — the Teichmüller map exists and is unique on µ<sup>(p)</sup>.** *Injectivity of reduction on µ<sup>(p)</sup>(o):* if ζ<sup>d</sup> = 1 with d prime to p and ζ ≡ 1 (mod m), write ζ = 1 + ε, ε ∈ m; then 0 = ζ<sup>d</sup> − 1 = ε·(d + ε·(…)) and d + ε(…) is a unit because |d| = 1 (d is prime to p, hence a unit in o) and |ε(…)| < 1; so ε = 0. ✔ *Surjectivity onto µ<sup>(p)</sup>(k):* because the valuation has rank 1 and |p| < 1, the sets p<sup>n</sup>o = {x : |x| ≤ |p|<sup>n</sup>} are cofinal among the valuation neighbourhoods of 0, so the p-adic and the valuation topologies on o coincide; o is p-adically complete, hence complete for the valuation, hence **henselian**. Given c ∈ µ<sup>(p)</sup>(k) of order d prime to p, the polynomial X<sup>d</sup> − 1 ∈ o[X] has the simple root c in k (its derivative dX<sup>d−1</sup> is a unit at c), so Hensel lifts it uniquely to a root in o. ✔ Hence **[·] : µ<sup>(p)</sup>(k) ∪ {0} → µ<sup>(p)</sup>(o) ∪ {0}** is a well-defined multiplicative bijection inverse to reduction, and it is *canonical* — no choice enters. **This replaces the note's own justification, which is circular; see finding A-5.**

**Step 1 — (⇒).** Assume |P(r+s) − P(r) − P(s)| ≤ |p| for all r, s ∈ κ. In a valuation ring, |x| ≤ |p| ⟺ x ∈ p o, and p o ⊆ m. So the reduction P̄ := (P mod m) : κ → k is additive; it is multiplicative because P is; and P̄(1) = 1. Hence **P̄ is a ring homomorphism**, and it is injective because κ is a field and P̄(1) ≠ 0. Put τ := P̄ : κ ↪ k. ✔
Now for r ∈ κ<sup>×</sup> = F̄<sub>p</sub><sup>×</sup>: r has finite order n prime to p, so P(r)<sup>n</sup> = P(r<sup>n</sup>) = P(1) = 1, i.e. **P(r) ∈ µ<sup>(p)</sup>(o) automatically** (this is a *consequence* of multiplicativity plus κ ≅ F̄<sub>p</sub>, not a hypothesis — cf. finding A-1). Both P(r) and [τ(r)] lie in µ<sup>(p)</sup>(o) and reduce to τ(r); by Step 0's injectivity, **P(r) = [τ(r)]**. And P(0) = 0 = [τ(0)]. So P = [·]∘τ. ✔
**Uniqueness of τ:** τ is recovered from P as its reduction mod m, hence is unique. ✔

**Step 2 — (⇐).** Proved in §3.3 above, self-containedly. ✔

**Consistency with the source, checked independently.** For X₀ = spec o<sub>K₀</sub>, at the closed point (x, y) = (s, s) one has O<sub>{x},y</sub> = κ, its p-adic completion is κ and its tilt is lim<sub>( )<sup>p</sup></sub>κ ≅ κ (κ perfect); so Def. 14.12's condition is exactly the condition of Lemma A, with α = 1/p = |p|. [x-03] p. 113 says the resulting maps "**are simply the ring homomorphisms P̂<sup>♭</sup><sub>y</sub> : κ ↪ k ⊂ o<sup>♭</sup>**", and Thm 15.6(1) records the fibre as "**Y<sup>⋄</sup><sub>s</sub> = Hom(κ, k)**" (p. 114). Since κ = an algebraic closure of the finite field κ₀ (p. 106), κ ≅ F̄<sub>p</sub> and Hom(κ, k) = Hom(F̄<sub>p</sub>, k) is a torsor under Aut(F̄<sub>p</sub>) = Ẑ. **Lemma A is exactly the closed-point stratum of Deninger's Theorem 15.6, and my re-derivation reproduces it.** ✔ Under Prop. 14.14 (p. 100) the correspondence P̂<sub>y</sub> ↔ P̂<sup>♭</sup><sub>y</sub> is precisely "χ multiplicative with χ mod p additive ↔ ring homomorphism on the tilt", and ♯ carries κ ⊂ k ⊂ o<sup>♭</sup> back to the Teichmüller lifts — so "P = [·]∘τ" is the ♯-image of "P̂<sup>♭</sup><sub>y</sub> : κ ↪ k". ✔

**And the note's own consistency sentence checks:** "Hom(κ₀, k) is a single F<sub>p</sub>-orbit of size r = deg(κ₀/F<sub>p</sub>), which suspends to one closed orbit of length r·log p = log N(π₀)". Hom(F<sub>q</sub>, k) with q = p<sup>r</sup> has exactly r elements, permuted simply transitively by F<sub>p</sub> (composition with the Frobenius of F<sub>q</sub>), and [x-03] (224) identifies Y<sup>⋄</sup><sub>0s₀</sub> with it, while 15.6(6) gives the order r; N(π₀) = q = p<sup>r</sup>, so log N(π₀) = r log p. ✔

### 3.5 FINDING A-3 (MINOR) — the coefficient setup is cited to the wrong pages

The note's §2 says the coefficients are "o = a p-adically complete rank-1 valuation ring with **algebraically closed** quotient field C of characteristic 0 and residue field k of characteristic p", citing "[x-03] §§13–14, pp. 78, 89". On p. 89 Deninger assumes only "a p-adically complete rank one valuation ring with quotient field C, maximal ideal m and residue field k of characteristic p" — **neither C nor k is assumed algebraically closed there** (§1.1(l)). Both algebraically-closed hypotheses, and the characteristic-0 hypothesis on C, are introduced at pp. 105–106 (§1.1(r)). Lemma A's proof *uses* k algebraically closed (to have F̄<sub>p</sub> ⊆ k at all, i.e. so that Hom(κ, k) ≠ ∅). The citation must be corrected — **R-A3**.

### 3.6 FINDING A-5 (MINOR) — the surjectivity half of µ<sup>(p)</sup>(o) ≅ µ<sup>(p)</sup>(k) is argued circularly

The note writes: "Surjectivity onto µ<sup>(p)</sup>(k): an injective homomorphism between groups abstractly ≅ ⊕<sub>ℓ≠p</sub>Q<sub>ℓ</sub>/Z<sub>ℓ</sub> has divisible, hence full, ℓ-primary images." This presupposes that **µ<sup>(p)</sup>(o) is abstractly ≅ ⊕<sub>ℓ≠p</sub>Q<sub>ℓ</sub>/Z<sub>ℓ</sub>**, i.e. that o contains all prime-to-p roots of unity — which is exactly the surjectivity being proved. The divisibility argument is fine once that input is in hand, but the input is not supplied. The correct and short argument is Hensel's lemma, together with the observation that the p-adic and valuation topologies on a rank-1 o with |p| < 1 coincide, so that p-adic completeness gives henselianity (Step 0 above). **R-A5**.

### 3.7 The two Consequences drawn from Lemma A

**Consequence 1 ("why the local principle succeeds") — verified.** The injective characters κ(x)<sup>×</sup> → µ<sup>(p)</sup>(o) form a torsor under Aut(κ(x)<sup>×</sup>) = Ẑ<sup>×</sup><sub>(p)</sub> (2.1). By Lemma A the mod-p-additive ones are exactly {[·]∘τ : τ ∈ Hom(F̄<sub>p</sub>, k)}, and Hom(F̄<sub>p</sub>, k) is a torsor under Aut<sub>ring</sub>(F̄<sub>p</sub>) = Ẑ (every such τ is injective with image the algebraic closure of F<sub>p</sub> in k, so any two differ by an automorphism of F̄<sub>p</sub>). By (2.5) the image of Ẑ in Ẑ<sup>×</sup><sub>(p)</sub> is p<sup>Ẑ</sup>. **So mod-p additivity cuts a Ẑ<sup>×</sup><sub>(p)</sub>-torsor down to a p<sup>Ẑ</sup>-torsor, and the residue is exactly B<sub>p</sub> = coker(Aut<sub>ring</sub> ↪ Aut<sub>group</sub>) — which is verbatim Deninger's p. 33 display.** ✔ This is the note's best sentence and it is correct; finding T-1 records that the note's own transcription of that display obscures it.

**Consequence 2 (the transport reading, D3) — see §8.** Verified with one MAJOR correction (A-4).

---

## 4. LEMMA B — verdict **PASS**, strengthened (0 MAJOR, 3 MINOR)

### 4.1 Statement and re-derivation

> "**Lemma B.** For X₀ = Spec Z, at every point of every packet (any prime p, any character P in any class E ⊆ E<sub>tors</sub>), the test r = s = 1 gives |P(1̄+1̄) − P(1̄) − P(1̄)| = |P(2̄) − 2| ≥ 1, since P(2̄) is a root of unity or 0 (κ(x)<sup>×</sup> is torsion; 0 occurs iff p = 2). Hence the class 'archimedean defect ≤ ε at char-p points' is empty on the periodic locus for every ε < 1."

**Re-derivation.** The evaluation of a global section on a point of W<sub>rat</sub>(X)(C) is, by [x-03] (163) (p. 90) and its C-valued analogue, [α](x, P) = P(α(x)) where α(x) = α mod m<sub>x</sub> ∈ κ(x); for X₀ = Spec Z, Γ(X₀, O) = Z and an integer n evaluates to P(n̄), n̄ = n mod p ∈ F̄<sub>p</sub>. The additive defect of the evaluation Z → C at the pair (1, 1) is therefore
> D := P(1̄ + 1̄) − P(1̄) − P(1̄) = P(2̄) − 2 (using P(1) = 1).

Two cases, both elementary and both checked:
* **p = 2.** 2̄ = 0, and P is the extension by zero of a character into C<sup>×</sup>, so P(0) = 0 and D = −2, |D| = 2 ≥ 1. ✔
* **p odd.** 2̄ ∈ F<sub>p</sub><sup>×</sup> has order n | p−1, so P(2̄)<sup>n</sup> = P(2̄<sup>n</sup>) = P(1) = 1, i.e. P(2̄) ∈ µ<sub>n</sub>(C) and **|P(2̄)| = 1** for the archimedean absolute value. Hence |D| ≥ |2| − |P(2̄)| = 2 − 1 = **1**. ✔

So |D| ≥ 1 always, and the class {archimedean defect ≤ ε} with ε < 1 contains **no** point with char κ(x) > 0. **Lemma B is correct.** ✔

**Sharpness.** |D| = 1 exactly when P(2̄) = 1, which does occur (any P whose kernel contains 2̄, e.g. p = 7 and P killing the order-3 subgroup ⟨2̄⟩). So the threshold 1 cannot be raised: **ε < 1 gives the empty set; ε = 1 does not.** The note's "for every ε < 1" is exactly right, and no stronger constant is available from this test. ✔

**The second half of the lemma also checks.** The note says the (F3) extension mechanism "requires the defect ideal to land in a topologically nilpotent set (|·| < 1, so that lim ZR/I<sup>n</sup> receives the evaluation — (172), p. 94)". Read verbatim at §1.1(m): the mechanism first *chooses* ω<sub>α</sub> with α ≤ |ω<sub>α</sub>| < 1, then forms lim<sub>n</sub> o/ω<sub>α</sub><sup>n</sup> **= o**, which is where the ring homomorphism W<sub>p</sub>(P̌<sub>y</sub>) lands. With a defect bounded below by 1 there is no admissible ω<sub>α</sub> at all. ✔ *I add a sharper reason, verifiable without any further source:* the construction needs the coefficient ring to be a **non-archimedean** valuation ring in which ω is a non-unit; over C the only candidate "o" is C itself, every nonzero ω is a unit, and lim<sub>n</sub> C/ω<sup>n</sup>C = 0. **The mechanism does not merely become vacuous over C; it degenerates to the zero ring.** ✔

### 4.2 Is "the periodic locus" the right locus? — the charter's explicit press point

**No: it is too small, and the note's phrasing is also too strong in the other direction.** Both corrections point the same way and neither hurts D2.

* **Too small.** Nothing in the derivation used periodicity, or E, or even that x lies over a *closed* point of X₀. All it used is **char κ(x) = p > 0** (so that 2̄ is 0 or a root of unity) and multiplicativity. Hence the sharp statement is: *for any arithmetic scheme X₀ flat over Spec Z, at **every** point (x, P<sup>×</sup>) of X̌₀(C)<sub>E<sub>tors</sub></sub> with char κ(x) > 0 — periodic or not, in any class or none — the archimedean additivity defect of the evaluation of Z is ≥ 1.* The periodic locus is contained in this (by Thm 6.1, periodic points lie in packets over points with finite residue field, so char κ(x) > 0), which is why the note's version is true; but the true locus is the whole positive-characteristic locus X̌₀(C)<sub>p,E<sub>tors</sub></sub> of [x-03] p. 33. **R-B2** upgrades the statement.
* **Too strong.** The note's headline (D2 in §0) says the archimedean reading "selects the EMPTY set". Selects the empty set **on the positive-characteristic locus** — but the class is **not** empty on X₀. The classical points X₀(C) ⊂ X̌₀(C) ([x-03] p. 39, "the map X₀(C) × R<sup>>0</sup> → X₀ … is an R<sup>>0</sup>-equivariant inclusion") are honest field embeddings κ(x) ↪ C, for which the additive defect is **identically 0**. So the threshold condition selects a large nonempty set that happens to contain **no periodic points whatever**. That is a *sharper and more damaging* statement than "empty", because it says the archimedean reading produces a dynamical system with an empty periodic locus — the worst possible outcome for a Lefschetz-type program, and one that cannot be repaired by lowering ε. **R-B1** restates D2 accordingly.

**Two further independent reasons the archimedean threshold class is unusable, both re-derived here.**
1. *It is not admissible.* Let E<sub>ε</sub> = {characters whose evaluation has archimedean defect ≤ ε}. Def. 4.1 requires the biconditional ν-closure. Even ignoring the emptiness on char p, F<sub>ν</sub>(P) = P ∘ ( )<sup>ν</sup> has defect P((r+s)<sup>ν</sup>) − P(r<sup>ν</sup>) − P(s<sup>ν</sup>) = P(r+s)<sup>ν</sup> − P(r)<sup>ν</sup> − P(s)<sup>ν</sup>, which is not controlled by the defect of P. **So the archimedean reading fails Def. 4.1 for the same structural reason the p-adic one does** — and this means Deninger's p. 29 verdict "the resulting class E is not N-invariant" fits the *threshold* reading just as well as the transport reading. This weakens the note's §6 closing inference; see finding B-3.
2. *Frobenius self-improvement is unavailable.* Prop. 14.7's normalization of the constant ([x-03] p. 95) is ultrametric through and through: the step "|d<sup>p<sup>ν</sup></sup> + pc| ≤ max(|d|<sup>p<sup>ν</sup></sup>, |p|)" is the strong triangle inequality. Over C one gets only |d<sup>p<sup>ν</sup></sup> + pc| ≤ |d|<sup>p<sup>ν</sup></sup> + p|c|, and no threshold is dynamically forced. So the archimedean reading loses **canonicity of the constant** as well as nonemptiness. ✔ (The note says this in one clause — "The ultrametric inequality is load-bearing in (F2)'s self-improvement as well"; I confirm it by re-reading the proof.)

### 4.3 FINDING B-1 (MINOR) — "selects the empty set" needs its locus, and the closing inference is unsupported

Two parts. (a) As above, "empty" is true on the positive-characteristic locus and false on X₀; the *stronger* true statement is "selects a set containing no periodic point". (b) The note closes §6 with: "Deninger's own asserted translation (p. 29) cannot live here in nonempty form as a threshold condition, so his intended reading is presumably the transport reading of §4 (D3), consistent with his 'not N-invariant' verdict on it." The note flags this judgment-grade, correctly, and I do not overturn it — but I record that **the stated ground for the inference does not hold**: as shown in 4.2(1), the *threshold* reading is also non-N-invariant, so p. 29's "not N-invariant" verdict does not discriminate between the two readings. The inference should be flagged as pure conjecture with no evidential support, or dropped. **R-B1**.

### 4.4 FINDING B-2 (MINOR) — the justification names the wrong fact

The note justifies "P(2̄) is a root of unity or 0" by "κ(x)<sup>×</sup> is torsion". True at packet points, but the operative fact is weaker and more useful: **2̄ lies in the prime field F<sub>p</sub>**, hence is 0 or a root of unity of order dividing p−1, whatever κ(x) is. Stating it that way is what extends Lemma B to every positive-characteristic point of every arithmetic scheme (§4.2). **R-B2**.

### 4.5 FINDING B-3 (MINOR) — a missing consequence worth banking

Lemma B's statement should record the consequence that makes it a *trichotomy branch*, not just a computation: the archimedean threshold class, being disjoint from the whole positive-characteristic locus, **contains no periodic orbits at all**, so it cannot satisfy requirement 1 of §3 (cut each packet to one orbit) even in the degenerate sense — it deletes the packets rather than cutting them. **R-B3**.

### 4.6 BREAK attempts on Lemma B (all failed)

* *Choose P with P(2̄) close to 2?* Impossible: |P(2̄)| ∈ {0, 1}, so |P(2̄) − 2| ∈ {2} ∪ [1, 3].
* *Use a different pair (r, s) to get a smaller defect and dodge the lemma?* Irrelevant — Def. 14.5/14.12 quantify over **all** r, s, so a single bad pair kills membership. The lemma needs only one, and r = s = 1 is available in every Z-algebra.
* *Rescale the absolute value on C?* The archimedean absolute value on C is unique up to a positive power |·|<sup>t</sup>; |D| ≥ 1 is then |D|<sup>t</sup> ≥ 1, and the threshold "ε < 1" rescales with it. The statement is normalization-free. ✔
* *Work with a non-archimedean absolute value on C?* Then one is no longer doing "the archimedean reading", and moreover a rank-1 non-archimedean C with residue characteristic p is precisely the local situation Deninger already solved. No escape.

---

## 5. LEMMA C — verdict **PASS** (0 MAJOR, 3 MINOR)

### 5.1 Statement

> "**Lemma C (derived; Steinitz).** The restriction map Aut(C) → Aut(µ(C)) = Ẑ<sup>×</sup> is surjective for C the complex numbers (or any algebraically closed field of characteristic 0 containing Q̄ with infinite transcendence degree). *Derivation:* u ∈ Ẑ<sup>×</sup> defines an automorphism of Q(µ<sub>∞</sub>) (cyclotomic theory); extend to Q̄ (isomorphism extension), then to C along a transcendence basis of C over Q̄ and to the algebraic closure C of the lifted subfield (Steinitz; uses AC)."

### 5.2 Re-derivation, one extension step at a time (the charter's explicit demand)

Let C be any algebraically closed field of characteristic 0 and let u ∈ Ẑ<sup>×</sup>. By (2.2), Aut(µ(C)) = Ẑ<sup>×</sup>, and u is the automorphism ζ ↦ ζ<sup>u</sup> (meaning: if ζ has order n, ζ<sup>u</sup> := ζ<sup>u<sub>n</sub></sup> for u<sub>n</sub> = u mod n ∈ (Z/n)<sup>×</sup>; well defined and compatible).

* **Step 1 (cyclotomic).** Q(µ<sub>∞</sub>) ⊆ C is the subfield generated by all roots of unity. The cyclotomic character Gal(Q(µ<sub>∞</sub>)/Q) → Ẑ<sup>×</sup> is injective (an element fixing every root of unity fixes the whole field) and **surjective**, because [Q(µ<sub>n</sub>) : Q] = φ(n) for every n — i.e. because the n-th cyclotomic polynomial is irreducible over Q. **[classical, not on disk]** I flag this rather than pretend to have read it; it is the *only* external input in Lemma C, it is not available in [x-03]/[x-06]/[D25], and the note should name it (finding C-2). So there is τ ∈ Aut(Q(µ<sub>∞</sub>)/Q) with τ(ζ) = ζ<sup>u</sup> for every root of unity. ✔
* **Step 2 (to Q̄).** Q̄ ⊆ C is the algebraic closure of Q in C, and Q̄/Q(µ<sub>∞</sub>) is algebraic. By the isomorphism-extension theorem, τ extends to an embedding τ̄ : Q̄ → C; its image is algebraic over Q, hence contained in Q̄, and equals Q̄ because τ̄(Q̄) is algebraically closed (an isomorphic copy of Q̄) and contains Q. So τ̄ ∈ Aut(Q̄). **Choice used: Zorn's lemma.** ✔
* **Step 3 (along a transcendence basis).** Let B be a transcendence basis of C over Q̄ (**choice: Zorn**). Then Q̄(B) ⊆ C is a purely transcendental extension. Because B is algebraically independent over Q̄ and τ̄(Q̄) = Q̄, the assignment "act by τ̄ on coefficients, fix each element of B pointwise" is a well-defined ring automorphism of the polynomial ring Q̄[B], hence extends to a field automorphism τ̃ of Q̄(B). ✔
* **Step 4 (to C).** C is algebraic over Q̄(B) — indeed C is *an* algebraic closure of Q̄(B), since C is algebraically closed and algebraic over Q̄(B) by the definition of a transcendence basis. By isomorphism extension again (**choice: Zorn**), τ̃ extends to an embedding σ : C → C which is surjective because σ(C) is algebraically closed and contains Q̄(B), over which C is algebraic. So σ ∈ Aut(C). ✔
* **Step 5.** σ|<sub>µ(C)</sub> = τ|<sub>µ(C)</sub> = (ζ ↦ ζ<sup>u</sup>) = u. Hence Aut(C) ↠ Aut(µ(C)) = Ẑ<sup>×</sup>. ∎ ✔

**Choice is used exactly three times** (Steps 2, 3, 4), all as Zorn's lemma; Step 1 is choice-free. **No hypothesis on the transcendence degree is used anywhere** — the argument works for C = Q̄ (Steps 3–4 are then vacuous, B = ∅). ✔

### 5.3 The realizing automorphisms are necessarily discontinuous — proved here, and it matters

Suppose σ ∈ Aut(C) (C = the complex numbers, usual topology) is continuous. σ fixes Q pointwise (it fixes 1 and is a ring map), hence fixes R pointwise by density and continuity, hence σ(i) = ±i and σ ∈ {id, complex conjugation}. Both act on µ(C) by u = 1 resp. u = −1. **Therefore every σ realizing u ∉ {±1} is discontinuous (equivalently: "wild").** ✔ Consequences, both of which I record as scope, not as defects:
* Lemma C is a genuinely non-constructive, AC-dependent statement: in a universe where every automorphism of C is continuous, Aut(C) → Ẑ<sup>×</sup> has image {±1} and **Lemma C is false**. So Lemma C — and with it Proposition 1's force — is a ZFC theorem, not a ZF one. *(I do not cite a consistency result for that universe; the honest, self-contained half is the displayed proof above, which is all Proposition 1 needs.)*
* Nothing derived from Lemma C or Lemma D may be composed with any *topological* statement about X₀ — in particular not with the 9.3 adjudication's Theorem A, which is a closure statement. See finding D-1.

### 5.4 FINDING C-1 (MINOR) — an unnecessary and misleading hypothesis

"(or any algebraically closed field of characteristic 0 containing Q̄ with infinite transcendence degree)". Neither clause is needed: an algebraically closed field of characteristic 0 automatically contains a copy of Q̄, and the transcendence degree is irrelevant (Steps 3–4 handle every cardinality, including 0). Stating a superfluous hypothesis invites a later reader to think the lemma is delicate where it is not. **R-C1**.

### 5.5 FINDING C-2 (MINOR) — the derivation's last clause is garbled, and its one external input is unnamed

"…then to C along a transcendence basis of C over Q̄ and to the algebraic closure C of the lifted subfield (Steinitz; uses AC)" runs Steps 3 and 4 together and calls C both the target and "the algebraic closure of the lifted subfield". Also, the phrase "u ∈ Ẑ<sup>×</sup> defines an automorphism of Q(µ<sub>∞</sub>) (cyclotomic theory)" conceals the actual input — surjectivity of the cyclotomic character, i.e. irreducibility of the cyclotomic polynomials over Q. Under standing order 5 that input must be named and flagged as classical. **R-C2**.

### 5.6 FINDING C-3 (MINOR) — the discontinuity fact belongs in Lemma C, not only in §5's scope note

The note records wildness in the *Corollary's* scope note (b) and uses it there only to say Proposition 1 does not constrain analytic selections. It belongs in Lemma C itself, because it is what makes the whole Aut(C)-argument set-theoretic and therefore non-composable with topology (D-1). **R-C3**.

### 5.7 BREAK attempt (failed)

*Could the image of Aut(C) → Ẑ<sup>×</sup> be a proper subgroup for some algebraically closed C of characteristic 0?* No: Steps 1–5 realize every u for every such C. *Could Aut(µ(C)) be larger than Ẑ<sup>×</sup>?* No, by (2.2). *Could the restriction map fail to be a group homomorphism?* No: restriction of automorphisms to a characteristic subgroup is a homomorphism, and µ(C) is characteristic in C<sup>×</sup> (it is the torsion subgroup).

---

## 6. LEMMA D — verdict **PASS** (0 MAJOR, 4 MINOR)

### 6.1 D(i): commutation — re-derived

σ ∈ Aut(C) acts on X<sup>•</sup>(C) by (x, P<sup>×</sup>) ↦ (x, σ ∘ P<sup>×</sup>). This is well defined: σ|<sub>C<sup>×</sup></sub> is a group automorphism, so σ ∘ P<sup>×</sup> is again a character κ(x)<sup>×</sup> → C<sup>×</sup>.

* **With G.** [x-06] Thm 4.1 (p. 11) records the G-action verbatim as (x, P<sup>×</sup>)<sup>σ′</sup> = (x<sup>σ′</sup>, P<sup>×</sup> ∘ σ′): **pre**-composition. Post- and pre-composition commute: σ ∘ (P ∘ σ′) = (σ ∘ P) ∘ σ′. ✔
* **With every F<sub>ν</sub>.** F<sub>ν</sub>(x, P<sup>×</sup>) = (x, P<sup>×</sup> ∘ ( )<sup>ν</sup>) ([x-06] p. 11, verbatim), again pre-composition. ✔
* **With the Q<sup>>0</sup>-action.** X̌(C) = colim<sub>N₀</sub>X<sup>•</sup>(C) and the Q₀<sup>>0</sup>-action is induced from the N₀-action on the colimit; a map commuting with all F<sub>ν</sub> passes to the colimit and commutes with the induced group action. Also, by the description (29) ([x-03] p. 25, §1.1 — "P̌<sup>×</sup> … factors over pr<sub>ν</sub> for some ν"), post-composition by σ preserves X̌(C), since factoring over pr<sub>ν</sub> is unaffected. ✔
* **Descent to X₀ and commutation with the flow.** σ commutes with G, so it descends to X̌₀(C)<sub>E</sub> = X̌(C)<sub>E</sub>/G; it commutes with the Q₀<sup>>0</sup>-action, so σ × id<sub>R<sup>>0</sup></sub> descends to the suspension X₀ = X̌₀(C)<sub>E</sub> ×<sub>Q₀<sup>>0</sup></sub>R<sup>>0</sup>, by [P₀, u] ↦ [σP₀, u]; and φ<sup>t</sup>[P₀, u] = [P₀, ue<sup>t</sup>] visibly commutes with it. ✔ **Verdict: D(i) is correct.**

**FINDING D-4 (MINOR).** The note adds "and fixing the R-coordinate". There is no R-coordinate on X₀: u is only defined up to the Q₀<sup>>0</sup>-identification (P₀, u) ∼ (F<sub>q</sub>P₀, q<sup>−1</sup>u), so "fixing the R-coordinate" has no invariant meaning. What *is* true and is what the argument uses: σ commutes with φ<sup>t</sup>, preserves each packet Γ<sub>x₀</sub>, and acts trivially on the canonical projection (40) C<sub>x₀</sub> → Q₀<sup>>0</sup>/p<sup>Z</sup> of [x-03] p. 33 (because σ does not change |ker P<sup>×</sup>| — kernels are unchanged). **R-D4**.

### 6.2 D(ii): class stability — one class at a time, including (Image) for E<sub>max</sub> (the note's own press point)

Throughout, σ|<sub>C<sup>×</sup></sub> is a **group automorphism of C<sup>×</sup>**; in particular it is injective, it carries torsion to torsion in both directions, and it restricts to an automorphism of µ(C). Write χ′ = σ ∘ χ.

* **ker is unchanged:** ker χ′ = χ<sup>−1</sup>(σ<sup>−1</sup>(1)) = χ<sup>−1</sup>(1) = ker χ, and likewise ker(χ′|<sub>µ(κ)</sub>) = ker(χ|<sub>µ(κ)</sub>). This single observation settles five of the six classes.
* **E<sub>tors</sub>** — (Tors) is "ker(χ)<sub>tors</sub> = ker(χ|<sub>µ(κ)</sub>) is finite and its order ∈ N₀". Unchanged. **Biconditional ✔** (apply the same to σ<sup>−1</sup>).
* **E<sub>f</sub>** — "(Tors) and ker χ is finite (equivalently |ker χ| ∈ N₀)". Unchanged. ✔
* **E<sub>fg</sub>** — "(Tors) and ker χ is finitely generated". Unchanged (same subgroup). ✔
* **E<sub>fd</sub>** — "(Tors) and ker χ ⊗ Q is finite dimensional". Unchanged (same subgroup, hence the same Q-vector space). ✔
* **E<sub>fd0</sub>** — "(Tors) and (ker χ|<sub>κ(x₀)<sup>×</sup></sub>) ⊗ Q is finite dimensional, x₀ = π(x)". The subgroup ker χ ∩ κ(x₀)<sup>×</sup> is unchanged, and x₀ is a datum of the point x, untouched by post-composition. ✔
* **E<sub>max</sub> — (Image), the press point.** Verbatim (p. 27): "Only if char κ > 0. If χ(κ<sup>×</sup>) is torsion, then κ<sup>×</sup> is torsion as well." The hypothesis of the condition is a property of the *image* — and χ′(κ<sup>×</sup>) = σ(χ(κ<sup>×</sup>)) is **isomorphic as an abstract group** to χ(κ<sup>×</sup>) (σ is injective on C<sup>×</sup>). Torsionness of an abelian group is an isomorphism invariant, so "χ′(κ<sup>×</sup>) is torsion" ⟺ "χ(κ<sup>×</sup>) is torsion"; the conclusion "κ<sup>×</sup> is torsion" does not mention χ at all. Hence (Image) holds for χ′ iff it holds for χ. **Biconditional ✔** — and note that **(Image) is the *easiest* of the six, not the hardest**: it is the one condition whose verification needs nothing but injectivity of σ.
* **Admissibility of σ ∘ E.** Def. 4.1's operations are χ ↦ χ ∘ τ (τ ∈ Autκ) and χ ↦ χ ∘ ( )<sup>ν</sup>, both **pre**-compositions; post-composition by σ commutes with both, so σ ∘ E is admissible whenever E is, and E = σ ∘ E for each of the six. ✔

**Verdict: D(ii) is correct, biconditionally, for all six named classes.** ✔

**FINDING D-2 (MINOR).** The note's one-line reason reads "kernels are unchanged … and images map by σ, preserving torsion **and ⊗Q-dimension**". The ⊗Q-dimension conditions (E<sub>fd</sub>, E<sub>fd0</sub>) are conditions on **kernels**, not on images; attaching them to the image side is a mis-assignment that would mislead anyone checking the lemma. Only (Image) uses the image, and it uses only torsionness. **R-D2**.

**FINDING D-3 (MINOR).** The note calls E "Aut(C)-stable" but shortens this to "stable" in places. In [x-03] p. 29 "**stable**" is a *different* technical term ("χ ∈ E implies χ|<sub>κ̃<sup>×</sup></sub> ∈ E for all algebraically closed subfields κ̃ ⊂ κ"), and under that meaning "**All classes in the example are stable except for (Image) and hence E<sub>max</sub>**" — i.e. the very class the note's press point concerns is *not* stable in Deninger's sense while it *is* Aut(C)-stable in the note's. The two senses must be kept typographically distinct. **R-D3**.

### 6.3 D(iii): the coordinate formula (a, ν) ↦ (u<sub>σ</sub>a, ν) — re-derived, including the divisible-image step

**The divisible-image step, in full.** χ<sub>x</sub> = ι ∘ i<sub>x</sub><sup>−1</sup> : κ(x)<sup>×</sup> ↪ C<sup>×</sup> is injective ([x-03] p. 32, §1.1(e)). Its source is ⊕<sub>ℓ≠p</sub>Q<sub>ℓ</sub>/Z<sub>ℓ</sub> (2.1) and its target's torsion subgroup is µ(C) ≅ ⊕<sub>ℓ</sub>Q<sub>ℓ</sub>/Z<sub>ℓ</sub> (2.2). A group homomorphism preserves orders of elements up to division, so the ℓ-primary part maps into the ℓ-primary part, and no ℓ-primary element of order ℓ<sup>n</sup> can land outside µ(C); hence im χ<sub>x</sub> ⊆ µ<sup>(p)</sup>(C) = ⊕<sub>ℓ≠p</sub>Q<sub>ℓ</sub>/Z<sub>ℓ</sub>. For each ℓ ≠ p the image of Q<sub>ℓ</sub>/Z<sub>ℓ</sub> is a nonzero **divisible** subgroup of Q<sub>ℓ</sub>/Z<sub>ℓ</sub> (divisibility is preserved by surjections onto images), and the only such subgroup is the whole of Q<sub>ℓ</sub>/Z<sub>ℓ</sub> (every proper subgroup of Q<sub>ℓ</sub>/Z<sub>ℓ</sub> is finite cyclic, hence not divisible). Therefore **χ<sub>x</sub> : κ(x)<sup>×</sup> →∼ µ<sup>(p)</sup>(C)** is an isomorphism. ✔ *(This is the same argument the note gestures at with "divisible-image argument as in Lemma A", and here it is legitimate — unlike its use in Lemma A, where the analogous claim was the thing being proved; cf. finding A-5.)*

**The formula.** Let σ ∈ Aut(C) restrict to u ∈ Ẑ<sup>×</sup> on µ(C) (2.2), and let u<sub>σ</sub> ∈ Ẑ<sup>×</sup><sub>(p)</sub> be its image under the projection Ẑ<sup>×</sup> = ∏<sub>ℓ</sub>Z<sub>ℓ</sub><sup>×</sup> ↠ ∏<sub>ℓ≠p</sub>Z<sub>ℓ</sub><sup>×</sup> = Ẑ<sup>×</sup><sub>(p)</sub>. For r ∈ κ(x)<sup>×</sup> of order n (prime to p),
> σ(χ<sub>x</sub>(r)) = χ<sub>x</sub>(r)<sup>u</sup> = χ<sub>x</sub>(r)<sup>u mod n</sup> = χ<sub>x</sub>(r<sup>u mod n</sup>) = χ<sub>x</sub>(r<sup>u<sub>σ</sub></sup>),
using that χ<sub>x</sub> is a homomorphism and that u ≡ u<sub>σ</sub> mod n because n is prime to p. Hence **σ ∘ χ<sub>x</sub> = χ<sub>x</sub> ∘ ( )<sup>u<sub>σ</sub></sup>**, and therefore
> σ ∘ (χ<sub>x</sub> ∘ ( )<sup>a</sup> ∘ ( )<sup>ν</sup>) = (σ ∘ χ<sub>x</sub>) ∘ ( )<sup>a</sup> ∘ ( )<sup>ν</sup> = χ<sub>x</sub> ∘ ( )<sup>u<sub>σ</sub>a</sup> ∘ ( )<sup>ν</sup>,
i.e. **(a, ν) ↦ (u<sub>σ</sub>a, ν)** in the coordinates of (35). ✔
Passing to (37)/(38): multiplication by u<sub>σ</sub> is an automorphism of the abelian group Ẑ<sup>×</sup><sub>(p)</sub> commuting with the quotient by N x₀<sup>Ẑ</sup> = p<sup>Ẑ</sup> and with the ×<sub>p<sup>Z</sup></sub>-identification, so it descends and acts on the base **B<sub>p</sub> by the translation [a] ↦ [u<sub>σ</sub>a]**. ✔ Combining with Lemma C and the surjectivity of Ẑ<sup>×</sup> ↠ Ẑ<sup>×</sup><sub>(p)</sub>: **every translation of B<sub>p</sub> is realized by some σ ∈ Aut(C)** — the action of Aut(C) on B<sub>p</sub> is transitive. ✔
Finally, σ maps closed orbits of length log p to closed orbits of length log p, because it commutes with φ<sup>t</sup> and hence preserves periods. ✔ **Verdict: D(iii) is correct.**

### 6.4 FINDING D-1 (MINOR, but it must be added) — the Aut(C)-action is not continuous, and the note nowhere says so

By §5.3 every σ realizing u<sub>σ</sub> ∉ {±1} is a discontinuous automorphism of C. The topology on X<sup>•</sup>(C) is pointwise convergence of the maps P : R → C ([x-03] p. 40, §1.1(j)), so post-composition by a discontinuous σ is **not** continuous for it: a sequence P<sub>n</sub> → P pointwise need not give σ ∘ P<sub>n</sub> → σ ∘ P. Consequently:
* Lemma D and Proposition 1 are **set-theoretic, flow-equivariant** statements only. They must not be chained with any closure, compactness or minimality statement — in particular not with the 9.3 adjudication's Theorem A (a closure law) or its Corollary A.1/A.2.
* Conversely, this is *why* Proposition 1 is compatible with the packet being a single minimal set: both say the packet is homogeneous, but for different reasons and in different categories.
The note never states this. It must, because the note's own §7 Road 2 then *uses* Lemma D to argue about measures, where continuity is exactly what one would want and does not have (see §10, finding H-1). **R-D1**.

### 6.5 BREAK attempts on Lemma D (all failed)

* *Could σ move the point x?* No: the action is post-composition; x is untouched, so σ preserves each fibre of pr<sub>X</sub> and each packet.
* *Could σ fail to preserve periodicity because it is discontinuous?* No: periodicity is "φ<sup>t</sup>z = z for some t > 0", a purely algebraic condition, and σφ<sup>t</sup> = φ<sup>t</sup>σ.
* *Could σ ∘ E ≠ E for some admissible E?* Certainly — the Theorem-C cuts E(a₀) are the witness (§7.5). The lemma only claims it for the six named classes, and there it is proved.
* *Could u<sub>σ</sub> fail to be a unit?* No: σ|<sub>µ(C)</sub> is an automorphism, so u ∈ Ẑ<sup>×</sup>, and the projection of a unit is a unit.

---

## 7. PROPOSITION 1 (D1, the equivariance no-go) — verdict **PASS-WITH-REPAIRS** (1 MAJOR, 1 MINOR)

### 7.1 Statement

> "**Proposition 1 (derived).** Let E be any Aut(C)-stable class (all named example classes qualify) and let S ⊆ X₀<sup>E</sup> be Aut(C)-stable and flow-invariant. If S contains one periodic point over the prime p, then for EVERY base class [c] ∈ B<sub>p</sub>, S contains a closed orbit of length log p with base class [c]. In particular S contains uncountably many closed orbits over p …, and **no Aut(C)-stable selection achieves one orbit per prime**. *Proof:* by §4's coordinates the periodic point lies on an orbit γ with some base class [a]; for [c] = [ua] pick σ with u<sub>σ</sub> = u (Lemmas C–D); σ(γ) ⊆ S is a closed orbit of the same length with base class [c]; distinct base classes lie on distinct orbits since the fibers of the (38)-fibration are the Q<sup>>0</sup>-orbits ([x-03] p. 33). ∎"

### 7.2 Re-derivation, line by line

Let X₀ = Spec Z, p a prime, E an admissible Aut(C)-stable class **with E ⊆ E<sub>max</sub>** (see finding P-2 — the note omits this), S ⊆ X₀<sup>E</sup> Aut(C)-stable and flow-invariant, and z ∈ S a periodic point with pr<sub>X₀</sub>(z) = (p).

1. **z lies in the packet Γ<sup>E</sup><sub>p</sub>, on a closed orbit with a well-defined base class.** By [x-03] **Thm 6.1** (p. 39, §1.1(i)) — hypothesis E ⊆ E<sub>max</sub> — the set of points of X₀ with nontrivial R<sup>>0</sup>-isotropy is ∐<sub>x₀</sub>Γ<sup>E</sup><sub>x₀</sub>, and "any periodic orbit γ in X₀ is contained in Γ<sup>E</sup><sub>x₀</sub> for a uniquely determined x₀ with finite residue field", with isotropy N x₀<sup>Z</sup>. For X₀ = Spec Z and x₀ = (p) this says: the flow orbit γ of z (which lies in S, S being flow-invariant) is a **circle of length log p** inside Γ<sup>E</sup><sub>p</sub>. By (2.3) it is a fibre of Γ<sub>p</sub> → B<sub>p</sub>; call its base class [a]. ✔
2. **Every base class is reachable by an automorphism of C.** Given [c] ∈ B<sub>p</sub>, set u := c a<sup>−1</sup> ∈ Ẑ<sup>×</sup><sub>(p)</sub> (B<sub>p</sub> is a group, so this is defined modulo p<sup>Ẑ</sup> and any representative works). By Lemma C there is σ̃ ∈ Aut(C) whose action on µ(C) is any prescribed element of Ẑ<sup>×</sup>; choosing a preimage of u under the surjection Ẑ<sup>×</sup> ↠ Ẑ<sup>×</sup><sub>(p)</sub> gives σ ∈ Aut(C) with u<sub>σ</sub> = u. ✔
3. **σ(γ) is a closed orbit of the same length in the base class [c], inside X₀<sup>E</sup>.** By D(i) σ commutes with φ<sup>t</sup>, so σ(γ) is a flow orbit with the same period log p. By D(ii) σ preserves E (E is Aut(C)-stable), so σ(γ) ⊆ X₀<sup>E</sup>. By D(iii) σ translates the base class: [a] ↦ [u<sub>σ</sub>a] = [ua] = [c]. ✔
4. **σ(γ) ⊆ S**, because S is Aut(C)-stable. ✔
5. **Distinct base classes ⟹ distinct orbits.** By (2.3), whose source anchor for the *suspension* is [x-03] **p. 38** verbatim: "Γ<sub>x₀</sub> fibres over Ẑ<sup>×</sup><sub>(p)</sub>/p<sup>Ẑ</sup> … **with fibres the R<sup>>0</sup>-orbits in Γ<sub>x₀</sub>**". ✔
6. **Uncountability.** B<sub>p</sub> is uncountable by (2.4), re-derived here from scratch. ✔
7. **Conclusion.** S contains one closed orbit of length log p in *every* base class, hence uncountably many closed orbits over p; in particular S does not meet Γ<sub>p</sub> in exactly one orbit. As p was an arbitrary prime over which S has a periodic point, **no Aut(C)-stable, flow-invariant S achieves one orbit per prime**. ∎ ✔

Every hypothesis is used: E's Aut(C)-stability in step 3; S's flow-invariance in step 1; S's Aut(C)-stability in step 4; Lemma C's surjectivity in step 2; the fibration in step 5; **and E ⊆ E<sub>max</sub> in step 1**.

### 7.3 FINDING P-2 (MAJOR) — the proof consumes an unstated hypothesis that fails for E<sub>tors</sub>

Step 1 is the only place where the *periodic point* is converted into *a closed orbit inside a packet with a base class and length log p*. The only instrument in the sources for that conversion is [x-03] Thm 5.2 / Thm 6.1, and **both are stated with the hypothesis "Let E be an admissible class with E ⊂ E<sub>max</sub>"** (§1.1(g), (i), read verbatim). The note's Proposition 1 states no such hypothesis; it says "any Aut(C)-stable class", and its parenthetical "(all named example classes qualify)" invites the reader to include **E<sub>tors</sub>**. But by the inclusion chain read verbatim on p. 29, **E<sub>max</sub> ⊂ E<sub>tors</sub>**, so E<sub>tors</sub> ⊄ E<sub>max</sub> and Thm 6.1 is unavailable for it. For E = E<sub>tors</sub> the packet decomposition of the periodic locus is *not* established anywhere in [x-03] — the point of (Image) is precisely to exclude characters with torsion image at points whose residue field is not torsion, which is where extra isotropy could hide.

*Is the parenthetical itself wrong?* No — all six named classes **are** Aut(C)-stable (§6.2), so the parenthetical is correct as a statement about Aut(C)-stability. The defect is the missing E ⊆ E<sub>max</sub>, which the proposition needs but never states.

*FILL.* Add the hypothesis. Every use the note makes of Proposition 1 already satisfies it: the certified window is E ⊇ E<sub>f</sub> and the relevant classes are E<sub>f</sub> ⊆ E<sub>fg</sub> ⊆ E<sub>fd</sub> ⊆ E<sub>fd0</sub> ⊆ E<sub>max</sub>, all ⊆ E<sub>max</sub>. Alternatively, weaken the hypothesis on z from "periodic point over the prime p" to "**periodic point lying in the packet Γ<sup>E</sup><sub>p</sub>**", which makes the proposition true for every admissible Aut(C)-stable E including E<sub>tors</sub>, at the cost of a slightly weaker headline. Replacement text: **R-P2** (both variants supplied).

*BREAK.* I could not construct a periodic point of X₀<sup>E<sub>tors</sub></sup> outside every packet — the natural candidates (characters of Q̄<sup>×</sup> with torsion image, which violate (Image)) need a Galois-stable splitting of Q̄<sup>×</sup> to acquire isotropy, and I did not produce one. **So I do not claim Proposition 1 is false for E<sub>tors</sub>; I claim it is _not re-derived_ for E<sub>tors</sub>, which under this program's rules is a finding, not a verdict of falsity.**

**Severity MAJOR** (a stated proposition's proof consumes an unstated hypothesis, and the class for which the hypothesis fails is one the proposition's own parenthetical invites). Impact on the trichotomy: **none**, once the clause is added.

### 7.4 FINDING P-1 (MINOR) — the cited anchor is one page weaker than the one available

The note supports step 5 with "the fibers of the (38)-fibration are the Q<sup>>0</sup>-orbits ([x-03] p. 33)". That statement is about **C<sub>x₀</sub> ⊆ X̌₀(C)** and **Q<sup>>0</sup>-orbits**, so it needs the (easy, but unstated) translation to flow orbits in the suspension, which I supply at (2.3). The statement Proposition 1 actually wants is printed for the suspension itself on **p. 38** and needs no translation. **R-P1**.

### 7.5 The Corollary and its scope notes

**Corollary (the transplant no-go).** "any global selection with the analogous naturality — in particular, any selection defined uniformly from the abstract field C and the scheme data … retains the full packet. **A viable global selection must break Aut(C)-symmetry.**"

* The *input* facts are correctly cited and I verified each: Deninger's construction takes an **abstract** algebraically closed C as input ("Let C be an algebraically closed field which satisfies the conditions before Corollary 4.4", p. 31, §1.1(d)); the local principle is equivariant for the full coefficient automorphism group (Thm 15.6(1): "**G × Aut(o) × ⟨F<sub>p</sub>⟩-equivariant identification**", p. 113; Remark 14.17, p. 104). ✔
* **(F1) checks, and I can make it exact at the only threshold that matters.** By Prop. 14.7/14.13 the only threshold is α = 1/p, and |x| ≤ 1/p = |p| in a valuation ring means **x ∈ p·o** — a condition stated purely in ring-theoretic terms, manifestly preserved by every ring automorphism of o since σ(p) = p. So Aut(o)-equivariance of the selection is not merely cheap, it is **automatic**, with no argument about value groups needed. ✔ (The value-group argument also works: a ring automorphism of a rank-1 valuation ring induces an order-automorphism of the value group; fixing v(p) ≠ 0 in an Archimedean ordered group forces the identity. But the p·o formulation is shorter and needs nothing.)
* **The bridge "canonical ⟹ Aut(C)-stable" is a definability schema, not a theorem, and the note says so.** I concur, and I record that the schema is **not needed** for the theorem-grade content: Proposition 1 is a theorem about Aut(C)-stable selections, and taking S = X₀<sup>E</sup> in it yields the clean corollary below, which is a theorem outright.
* **Corollary 1′ (referee-derived, recommended as an addition — R-P3).** *For every admissible Aut(C)-stable E ⊆ E<sub>max</sub> and every prime p: if X₀<sup>E</sup> contains one periodic point over p, then Γ<sup>E</sup><sub>p</sub> = Γ<sub>p</sub>, the full packet.* (Take S = X₀<sup>E</sup>, which is Aut(C)-stable because E is and flow-invariant by construction.) This is an **independent second proof of the full-packet phenomenon**, under a hypothesis (Aut(C)-stability) not comparable with [x-03] Thm 5.2's E ⊇ E<sub>f</sub>; the two agree on every named class in E<sub>f</sub> … E<sub>max</sub>, all of which satisfy both. The note calls this a "conceptual explanation" of Thm 5.2 in its consistency check (c); it is more — it is a theorem with an independent hypothesis, and it is the cleanest available statement of D1's positive content.
* **Consistency check (c) is correct and functions as a _sharpness witness_.** The Theorem-C cuts E(a₀) are admissible, flow-invariant, one orbit per prime, and **not** Aut(C)-stable (σ sends χ<sup>a₀</sup> to χ<sup>u<sub>σ</sub>a₀</sup>, whose base class [u<sub>σ</sub>a₀] ≠ [a₀] as soon as u<sub>σ</sub> ∉ p<sup>Ẑ</sup>, while the adjudication's reachability computation puts E(a₀)'s members' exponents in a₀·p<sup>Ẑ</sup>). So dropping E's Aut(C)-stability makes the conclusion **false**, i.e. **Proposition 1's hypothesis is necessary and the proposition is sharp.** *(I did not re-derive Theorem C's reachability computation — it is outside this item, and the adjudication states it re-derived it. Nothing in my verdicts depends on it: the sharpness witness is a bonus, not an input.)*

### 7.6 BREAK attempts on Proposition 1 (all failed)

* *An Aut(C)-stable one-orbit-per-prime S?* Steps 1–7 exclude it outright (given E ⊆ E<sub>max</sub>).
* *Weaken "Aut(C)-stable" to "σ(S) ⊆ S for every σ"?* No escape: Aut(C) is a group, so σ(S) ⊆ S for all σ forces σ(S) = S.
* *Use only the inner automorphisms available without choice (id and conjugation)?* Then u<sub>σ</sub> ∈ {±1}, only two base classes are reached, and the proposition gives nothing. **This is the honest boundary of D1: it is a ZFC statement** (§5.3). It does not weaken the note's use of it, because the note's target is the *definability* schema — a locus defined uniformly from the abstract field C is stable under **all** field automorphisms, whether or not one can exhibit them.
* *Could σ(γ) equal γ although [u<sub>σ</sub>a] ≠ [a]?* No, by step 5 (distinct base classes, distinct orbits).
* *Could S be Aut(C)-stable and meet Γ<sub>p</sub> in one orbit while containing no periodic point over p?* Vacuous: an orbit in Γ<sub>p</sub> **is** periodic (Thm 6.1).

---

## 8. §4 Consequence 2 — the transport reading (D3) — verdict **PASS-WITH-REPAIRS** (1 MAJOR)

### 8.1 Re-derivation

Fix an isomorphism j : µ<sup>(p)</sup>(C) →∼ µ<sup>(p)</sup>(o) (o = o<sub>C<sub>p</sub></sub>, say). Both groups are ≅ ⊕<sub>ℓ≠p</sub>Q<sub>ℓ</sub>/Z<sub>ℓ</sub> (2.2, and Step 0 of §3.4 for o), so such j exist and the set of them is a torsor under Aut(⊕<sub>ℓ≠p</sub>Q<sub>ℓ</sub>/Z<sub>ℓ</sub>) = Ẑ<sup>×</sup><sub>(p)</sub>. By §6.3, χ<sub>x</sub> : κ(x)<sup>×</sup> →∼ µ<sup>(p)</sup>(C), so
> θ := [·]<sup>−1</sup> ∘ j ∘ χ<sub>x</sub> : κ(x)<sup>×</sup> →∼ F̄<sub>p</sub><sup>×</sup>
is a **group** isomorphism ([·]<sup>−1</sup> being reduction, Step 0 of §3.4). For b ∈ Ẑ<sup>×</sup><sub>(p)</sub> and ν ∈ N₀,
> j ∘ (χ<sub>x</sub> ∘ ( )<sup>b</sup> ∘ ( )<sup>ν</sup>) = [·] ∘ (θ ∘ ( )<sup>b</sup> ∘ ( )<sup>ν</sup>).
By **Lemma A**, this is mod-p additive **iff** θ ∘ ( )<sup>b</sup> ∘ ( )<sup>ν</sup> is (the restriction to κ(x)<sup>×</sup> of) a **field** isomorphism κ(x) → F̄<sub>p</sub>. Two consequences:
* ν must have prime-to-p part 1 (else the map is not injective: its kernel is µ<sub>ν′</sub>, ν′ = prime-to-p part of ν, cf. [x-03] (42), p. 33), so the selected points have injective characters;
* the field isomorphisms form a sub-torsor under Aut<sub>ring</sub>(F̄<sub>p</sub>) = Ẑ inside the Ẑ<sup>×</sup><sub>(p)</sub>-torsor of group isomorphisms, whose image in Ẑ<sup>×</sup><sub>(p)</sub> is p<sup>Ẑ</sup> (2.5). Hence {b : selected} is a **single coset b₀·p<sup>Ẑ</sup>, i.e. exactly one base class in B<sub>p</sub>**. ✔
Varying j across its Ẑ<sup>×</sup><sub>(p)</sub>-torsor translates b₀ and therefore **sweeps every base class**. ✔ So: *the faithful transport of the local principle selects, for each choice of j, exactly one base class per prime, and the choice of j is exactly a choice of a point of a Cantor torsor.* **D3's substance is verified.** ✔

### 8.2 FINDING A-4 (MAJOR) — the displayed identification contains a clause that is false under either reading

The note writes:
> "the faithful transport of the local principle **is** the adjudicated Theorem-C cut E(a₀), with j in place of a₀: it exists, it is one arbitrary point of a Cantor torsor per prime, it is not admissible-with-theory (forfeits every certified theorem), **and it is not N-invariant** — precisely [x-03]'s p. 29 Remark."

There are two objects here and the sentence conflates them.
* **The transported condition** C<sub>j</sub> := {characters χ : j ∘ χ is mod-p additive}. This is **not** an admissible class at all: it fails Def. 4.1's ν-closure (that is exactly §3's freshman's-dream point, re-proved in §9 below). So "it **is** the Theorem-C cut E(a₀)" is false for C<sub>j</sub>: E(a₀) is admissible by construction.
* **The admissible closure** E(a₀) := the smallest admissible class containing the selected injective character. This exists (admissibility is a biconditional closure condition and is preserved by intersections, and E<sub>tors</sub> is an admissible class containing everything in sight), and being admissible **it is N-invariant**. So "**and it is not N-invariant**" is false for E(a₀).

Either way one clause is false, and the sentence as printed asserts both. **The corrected statement, which is what §4 actually establishes:** *the transported condition C<sub>j</sub> is not admissible (it is not N-invariant — precisely [x-03] p. 29); it selects exactly the single base class determined by j; and its admissible closure is the Theorem-C cut E(a₀), which is admissible but non-canonical and theory-forfeiting. Nothing new is gained.* **D3 survives unchanged** — indeed the corrected version is stronger, because it exhibits *two* independent defects (non-admissibility of the raw condition; non-canonicity of its closure) where the note claimed one object with both properties. Replacement text: **R-A4**.

**Severity MAJOR** (a displayed conclusion contains a false clause; the note must change). Impact on the trichotomy: none.

---

## 9. §3's freshman's-dream N-invariance argument — verdict **PASS**, strengthened

**What the note says.** "additivity mod p is ( )<sup>p</sup>-stable (Prop. 14.7's computation) but not ( )<sup>ℓ</sup>-stable for ℓ ≠ p, since (r+s)<sup>ℓ</sup> ≢ r<sup>ℓ</sup> + s<sup>ℓ</sup> mod p. A mod-p-type selection and the full-Q<sup>>0</sup> suspension design cannot coexist; one must give."

**Re-derivation.**
* *p-stability* is [x-03] Prop. 14.7, read verbatim (p. 94): "F<sub>p</sub>(Y̌<sub>α</sub>) = Y̌<sub>α</sub>", proved from F<sub>p</sub>(I<sub>y</sub>) = I<sub>y</sub>. So the class is biconditionally closed under ( )<sup>p</sup>. ✔
* *Failure of ℓ-stability, with an explicit witness I computed.* Let κ = F̄<sub>5</sub>, k = F̄<sub>5</sub>, o = o<sub>C<sub>5</sub></sub>, τ = id, P = [·] (mod-p additive by Lemma A). Take ℓ = 3 and Q := F₃(P) = [·] ∘ ( )<sup>3</sup>. Then the reduction of Q mod m is the map r ↦ r<sup>3</sup> on F̄<sub>5</sub>, and (1+1)<sup>3</sup> = 8 = 3 ≠ 2 = 1<sup>3</sup> + 1<sup>3</sup> in F<sub>5</sub>. So the reduction of Q is **not** additive, and by Lemma A step 1 (the (⇒) direction, contrapositive) **Q is not mod-p additive**. Def. 4.1's biconditional — "χ is in E **if and only if** χ ∘ ( )<sup>ν</sup> is in E" — therefore fails. ✔
* *Generalization, proved.* For **every** mod-p-additive P at a char-p point and **every** ν ∈ N whose prime-to-p part is > 1, F<sub>ν</sub>(P) is not mod-p additive. *Proof.* By Lemma A, P = [·]∘τ. If F<sub>ν</sub>(P) = P ∘ ( )<sup>ν</sup> were mod-p additive then, by Lemma A step 1, its reduction τ ∘ ( )<sup>ν</sup> would be a ring homomorphism F̄<sub>p</sub> → k, i.e. (a+b)<sup>ν</sup> = a<sup>ν</sup> + b<sup>ν</sup> for all a, b ∈ F̄<sub>p</sub> (τ injective). But the polynomial (X+Y)<sup>ν</sup> − X<sup>ν</sup> − Y<sup>ν</sup> ∈ F<sub>p</sub>[X, Y] is nonzero whenever ν is not a power of p (some binomial coefficient binom(ν, i), 0 < i < ν, is prime to p — e.g. by Kummer/Lucas, or directly: write ν = p<sup>e</sup>m with p ∤ m, m > 1, then binom(ν, p<sup>e</sup>) ≡ m ≢ 0 mod p), and a nonzero polynomial over the infinite field F̄<sub>p</sub> has a non-root. Contradiction. ∎ ✔
* *So the note's claim is right, and it is also Deninger's own verdict* (p. 29: "the resulting class E is not N-invariant") and the reason he restricts to N₀ = p<sup>Z</sup> in §14 (p. 89, verbatim, §1.1(l)). ✔

**Strengthening (referee-derived, recommended as an addition — R-N1).** The note's §3 leaves the reader with "one must give", without saying what the *residue* is. Combining the above with §8: the smallest admissible class containing a mod-p-additive character **exists**, and by the adjudication's reachability computation it is precisely the cut E(a₀). So the correct closing statement of §3 is not merely a stability failure but a **complete accounting**:
> A mod-p-type condition is not admissible for N₀ = N; passing to its admissible closure destroys the condition (the closure contains characters at arbitrarily bad defect, by the displayed generalization) while retaining exactly one base class per prime; hence the *only* trace the local principle can leave on the global system is a non-canonical one-orbit-per-prime cut. **§3 and §4's D3 are the same phenomenon seen twice.**

---

## 10. §7's Haar formal count — verdict **PASS-WITH-REPAIRS** (1 MAJOR)

**What the note says.** "the packet base B<sub>p</sub> is a compact group, its Haar probability measure is translation-invariant, and by Lemma D(iii) Aut(C) acts on B<sub>p</sub> by group translations — so **Haar measure is canonical AND Aut(C)-equivariant**: it passes exactly where every selection fails. … The flow fixes the base (§4), so the measure is flow-invariant. At the formal level the T1 count then comes out right: the packet's aggregate orbit contribution is ∫<sub>B<sub>p</sub></sub>(single-orbit term) dHaar = the single-orbit term, **since the integrand is constant (all orbits in Γ<sub>p</sub> have length log p — [x-06] Thm 4.2)**."

**What checks.**
* B<sub>p</sub> is a compact (profinite) group (2.4), so it carries a **unique** Haar probability measure. ✔
* Aut(C) acts on B<sub>p</sub> by translations (D(iii), §6.3), and translations preserve Haar. ✔
* The flow acts trivially on B<sub>p</sub>, because the fibres of Γ<sub>p</sub> → B<sub>p</sub> are the R<sup>>0</sup>-orbits ([x-03] p. 38, verbatim). ✔
* **[x-06] Thm 4.2 says exactly what the note says it says**, read verbatim this session (§1.2): "The compact subsets Γ<sub>x₀</sub> ⊂ X₀ consist of periodic orbits of length log N x₀ … Γ<sub>x₀</sub> is a fibre space over the compact group Aut(F̄<sub>p</sub><sup>×</sup>)/Aut(F̄<sub>p</sub>) … with fibres the compact orbits in Γ<sub>x₀</sub>", and one line later "all of which have length log N x₀ i.e. log p if X₀ = spec Z". ✔ *(The same is in [x-03] Thm 6.1, p. 39, as the isotropy statement (R<sup>>0</sup>)<sub>x₀</sub> = N x₀<sup>Z</sup>.)*

**A sharpening the note misses, and should have (R-H2).** [x-03] p. 33 warns, verbatim: "**The maps (37), (38) and the fibration map depend on our choices of x and ι.**" That is precisely the ambiguity which makes a *point* of B<sub>p</sub> non-canonical — the whole content of D3. But every change of choices acts on the base by a **translation**: replacing ι by ι ∘ ( )<sup>u</sup> replaces a by ua, and replacing x by another point over x₀ acts through Gal(κ(x)/κ(x₀)) = N x₀<sup>Ẑ</sup> = p<sup>Ẑ</sup>, which is trivial on B<sub>p</sub>. Hence, canonically, **the base of the packet fibration is a torsor under B<sub>p</sub>, not the group B<sub>p</sub> itself** — and a torsor under a compact group carries a unique invariant probability measure. So the Haar candidate is canonical **for exactly the reason that the point-selection is not**. This is a sharper statement of Road 2's thesis than the note gives, and it follows from anchors already read.

**FINDING H-1 (MAJOR).** "since the integrand is constant (all orbits in Γ<sub>p</sub> have length log p)" does **not** establish what it is asked to establish. The integrand is "the single-orbit term" of a trace formula that has not been specified; the note gives no definition of it, and nothing forces such a term to be a function of the orbit's **length alone**. (Whatever the eventual formula, an orbital term generically also depends on transverse data attached to the orbit — that dependence is exactly why the trace-formula frameworks the ledger tracks carry hypotheses about the orbits being simple and isolated, which the note itself cites as Road 2's first obstacle. I do not attach a literature citation to this remark, because I did not open those sources for this item; the *logical* point stands without one: equality of one attribute of the orbits is not constancy of an unspecified function of the orbits.) As written the sentence would let a later reader believe the count "comes out right" for a reason that has not been checked.

*FILL (supplied — and it runs through Lemma D, i.e. through this very item).* The right reason is **homogeneity**, not length:
> Let W be any assignment γ ↦ W(γ) of a weight to the closed orbits of Γ<sub>p</sub> which is invariant under those automorphisms of the ambient system that commute with the flow. By Lemma D every σ ∈ Aut(C) is such an automorphism, and by D(iii) + Lemma C the induced action on the set of closed orbits of Γ<sub>p</sub> is the **transitive** translation action on B<sub>p</sub>. Hence W is constant on Γ<sub>p</sub>, and ∫<sub>B<sub>p</sub></sub>W dHaar = W(γ) for any single γ, Haar being a probability measure.

*How weak this fill is — stated explicitly, because the note must not over-claim it.* By finding D-1 the σ's are **not homeomorphisms**. So the class of weights the fill covers is the class of weights invariant under *set-theoretic, flow-commuting* automorphisms — and an orbital weight built from transverse analytic data (holonomy, a transverse measure, a Poincaré/linearization determinant, a leafwise heat kernel) has **no reason whatever** to be invariant under a discontinuous automorphism. I searched for a *continuous* transitive action on B<sub>p</sub> and found none: the Galois action has already been quotiented out (X̌₀ = X̌/G), the Q<sup>>0</sup>-action fixes the base by (2.3), and changing ι is the same operation as applying some σ. **Therefore: constancy of an analytically defined orbital weight along B<sub>p</sub> is _open_, and it is a second precondition of Road 2 alongside DQ-M's existence question.** The repair below states the fill and this limitation together. **R-H1**.

**What is NOT repaired, and must stay open.** The repair establishes constancy for a naturality class that no analytic weight is known to belong to; it does not establish (i) that a distributional trace exists for a flow with a continuum of closed orbits, (ii) that its orbital side is an integral over the packet at all, or (iii) that the transverse analysis survives the non-Hausdorffness recorded by the 9.3 adjudication (its §4 item 3, W12). The note is right to route these to DQ-M. **Road 2's status is unchanged by this repair: the formal count is now correctly labelled, and it remains formal — and it acquires one further named precondition (weight-homogeneity in the analytic category).**

---

## 11. Citation and transcription layer (5 MINOR)

**T-1 (MINOR) — a displayed identity that is false as transcribed.** §4 of the note prints the packet base as
> "B<sub>p</sub> := Ẑ<sup>×</sup><sub>(p)</sub>/p<sup>Ẑ</sup> = Aut(F̄<sub>p</sub>)<sup>×</sup>/Aut(F<sub>p</sub>)^"
Taken literally this is false twice over: Aut(F<sub>p</sub>) is the **trivial** group (F<sub>p</sub> has no nontrivial field automorphisms), so the right side would be all of "Aut(F̄<sub>p</sub>)<sup>×</sup>" and the quotient by p<sup>Ẑ</sup> would have vanished; and the × is placed outside the Aut rather than on its argument. The source display, read from a page render (§1.4) because `pdftotext` drops the overlines and floats the superscript, is
> **Ẑ<sup>×</sup><sub>(p)</sub>/p<sup>Ẑ</sup> = Aut(F̄<sub>p</sub><sup>×</sup>)/Aut(F̄<sub>p</sub>)** ([x-03] p. 33; the same display recurs verbatim on p. 38 and in [x-06] Thm 4.2, p. 12).
The corrected reading **is literally the note's own §4 Consequence 1** — "coker(Aut<sub>ring</sub> ↪ Aut<sub>group</sub>)" — so the transcription slip obscures the note's best sentence. Nothing downstream consumes the mis-transcription. **R-T1**.

**T-2 (MINOR).** "…this process does not give more points" is on **[x-03] p. 6**, not p. 5: the page break falls between "…in these diagrams we have to consider not only those maps but all continuous maps on the projective limits" (p. 5) and the "Incidentally, if we consider points of W<sub>rat</sub>(X) with values in rings without 'small multiplicative subgroups'…" sentence (p. 6). The note cites p. 5 for it twice (§2 Stage 2 and §6). *(p. 5 does carry the separate "minimal condition E … does not look natural" line, which the note cites correctly.)* **R-T2**.

**T-3 (MINOR).** The [D25] quotation in §7 Road 1 inserts "= (ZĀ)<sup>G</sup>" **inside** the quotation marks. The source sentence reads "…the more information the ring W<sub>rat</sub>(A) has about the additive structure of A" (p. 2). The gloss is factually correct — it is the paper's own display (3) — but must be bracketed or moved outside the quotation. **R-T3**.

**T-4 (MINOR).** §1 lists "§14 pp. 89–100" for "Defs. 14.1/14.2/14.5/14.12, Props. 14.7/14.13/14.14". Prop. 14.14's statement is on p. 100 and its **proof begins on p. 101**; Remark 14.17, which the note's (F5) leans on for the Aut(o)-action, is on p. 104. The range should read **89–101** (and (F5)'s Remark 14.17 should be cited at p. 104). **R-T4**.

**T-5 (MINOR).** §10 records [D25] as "scratchpad copy only … flagged for `fetched-r3/` promotion". **The promotion has happened**: the file is on disk at `fetched-r3/r3s-22-deninger-rational-witt-vectors-associated-sheaves-arxiv-2508.05329v1-SESSION8-FETCH.pdf` (verified this session; the §7 Road 1 quotation was read from it), under a filename different from the one the note suggests. The bookkeeping item is discharged. **R-T5**.

---

## 12. REPAIRS — exact replacement text

Each repair is written so the adjudicator can paste it into the note. Nothing here edits the note; this report is a separate file, per the task instruction.

### R-A1 (for MAJOR A-1) — Lemma A's hypothesis
*Replace* "κ an algebraically closed field of characteristic p, and P: κ → o multiplicative with P(0) = 0, P(1) = 1, whose restriction to κ<sup>×</sup> is a group homomorphism into o (values automatically in µ<sup>(p)</sup>(o), the prime-to-p roots of unity, since κ<sup>×</sup> is prime-to-p torsion)"
*by:*
> "κ ≅ F̄<sub>p</sub> (equivalently: an algebraically closed field **algebraic over F<sub>p</sub>** — this is the only case in which κ<sup>×</sup> is torsion, and it is the only case used below and the only case occurring in [x-03] §15, where κ is 'the common residue field of o<sub>K</sub>, ô<sub>K</sub> and ô<sup>♭</sup><sub>K</sub>, an algebraic closure of κ₀', p. 106), and P: κ → o multiplicative with P(0) = 0, P(1) = 1, whose restriction to κ<sup>×</sup> is a group homomorphism. (Its values then lie automatically in µ<sup>(p)</sup>(o): if r has order n prime to p then P(r)<sup>n</sup> = P(r<sup>n</sup>) = 1. This is a **consequence** of multiplicativity, not a hypothesis.)"

*Optional footnote to add, recording the general case honestly:* "For a general algebraically closed κ of characteristic p the statement as written does not typecheck, because [·] is defined only on µ<sup>(p)</sup>(k) ∪ {0}. It can be restated using the full multiplicative section k ⊂ o<sup>♭</sup> →<sup>♯</sup> o supplied by [x-03] p. 106 ('Then k is also a subfield of o<sup>♭</sup> such that k ⊂ o<sup>♭</sup> → k is the identity'), but that section depends on a choice of coefficient field of o<sup>♭</sup>, whereas on µ<sup>(p)</sup> the section is unique. The canonical case is κ ≅ F̄<sub>p</sub>."

### R-A2 (for MAJOR A-2) — Lemma A's converse
*Replace* "(⇐) [a] + [b] − [a+b] ∈ V W(k) = p W(k) in the Witt ring W(k) ⊆ o (first ghost/component coordinates agree; V F = p on Witt vectors of a perfect ring), so the defect of [·]∘τ has absolute value ≤ |p|."
*by:*
> "(⇐) Let τ : F̄<sub>p</sub> ↪ k, r, s ∈ F̄<sub>p</sub>, and put ζ = [τ(r)], ξ = [τ(s)], η = [τ(r+s)], w = ζ + ξ, δ = w − η. Reduction mod **m** is a ring homomorphism, so δ ∈ **m**, i.e. |δ| < 1. Choose f with r, s, r+s ∈ F<sub>q</sub>, q = p<sup>f</sup>; then ζ<sup>q</sup> = ζ, ξ<sup>q</sup> = ξ, η<sup>q</sup> = η. For any u, v ∈ o one has (u+v)<sup>p</sup> = u<sup>p</sup> + v<sup>p</sup> + pc with c ∈ o, since p divides binom(p, i) for 0 < i < p; iterating, (u+v)<sup>p<sup>n</sup></sup> ≡ u<sup>p<sup>n</sup></sup> + v<sup>p<sup>n</sup></sup> mod p·o. Take n a multiple of f. With (u, v) = (ζ, ξ): w<sup>p<sup>n</sup></sup> ≡ ζ + ξ = w mod p·o. With (u, v) = (η, δ): |w<sup>p<sup>n</sup></sup> − η| ≤ max(|δ|<sup>p<sup>n</sup></sup>, |p|). Choosing n large enough that |δ|<sup>p<sup>n</sup></sup> ≤ |p| and applying the ultrametric inequality gives |ζ + ξ − η| ≤ |p|, which is the claim. The bound is **sharp**: for p = 2, r = s = 1 the defect is exactly 2, of absolute value |p|. (No Witt vectors and no embedding W(k) ⊆ o are needed — and none is available in general, since o ↠ k has kernel **m** ⊋ p·o.)"

### R-A3 (for MINOR A-3) — the coefficient-setup citation
*In §2, replace* "([x-03] §§13–14, pp. 78, 89)" *for the coefficient hypotheses by* "([x-03] p. 89 for 'p-adically complete rank one valuation ring with quotient field C, maximal ideal **m** and residue field k of characteristic p'; **the algebraically-closed hypotheses on C and on k, and char C = 0, are introduced at pp. 105–106**)".

### R-A4 (for MAJOR A-4) — §4 Consequence 2, the transport identification
*Replace* "So the faithful transport of the local principle **is** the adjudicated Theorem-C cut E(a₀), with j in place of a₀: it exists, it is one arbitrary point of a Cantor torsor per prime, it is not admissible-with-theory (forfeits every certified theorem), and it is not N-invariant — precisely [x-03]'s p. 29 Remark."
*by:*
> "So the faithful transport of the local principle produces, for each j, a condition C<sub>j</sub> that selects exactly one base class per prime. Two things must be said about it, and they are different things. (i) **C<sub>j</sub> is not an admissible class**: it fails Def. 4.1's ν-closure, i.e. it is not N-invariant — precisely [x-03]'s p. 29 Remark, and precisely §3's freshman's-dream computation. (ii) **Its admissible closure is the adjudicated Theorem-C cut E(a₀)**, with j in place of a₀; that class *is* admissible, hence N-invariant, but it is one arbitrary point of a Cantor torsor per prime and it forfeits every theorem [x-03] certifies. Nothing new is gained: the known dead end is re-derived from the local principle itself, now with two distinct defects rather than one."

### R-A5 (for MINOR A-5) — the Teichmüller section
*Replace* "Surjectivity onto µ<sup>(p)</sup>(k): an injective homomorphism between groups abstractly ≅ ⊕<sub>ℓ≠p</sub>Q<sub>ℓ</sub>/Z<sub>ℓ</sub> has divisible, hence full, ℓ-primary images."
*by:*
> "Surjectivity onto µ<sup>(p)</sup>(k): since the valuation has rank 1 and |p| < 1, the sets p<sup>n</sup>o are cofinal among the neighbourhoods of 0, so the p-adic and valuation topologies on o agree; o is p-adically complete, hence complete for the valuation, hence **henselian**. For c ∈ µ<sup>(p)</sup>(k) of order d prime to p, the polynomial X<sup>d</sup> − 1 has c as a simple root mod **m** (its derivative dX<sup>d−1</sup> is a unit there), so Hensel lifts it uniquely. Hence [·] is a well-defined multiplicative bijection inverse to reduction, and it is canonical."
*(The divisibility argument as printed is circular: it assumes µ<sup>(p)</sup>(o) ≅ ⊕<sub>ℓ≠p</sub>Q<sub>ℓ</sub>/Z<sub>ℓ</sub>, which is the surjectivity being proved. The same divisibility argument **is** legitimate where §5 Lemma D(iii) uses it, because there the source group is known.)*

### R-B1 (for MINOR B-1) — the locus, and the closing inference
*In §0 (D2) and in §6, replace* "selects the EMPTY set on the periodic locus" *by* "selects a class **containing no periodic point at all**: the additivity defect is ≥ 1 at **every** point with char κ(x) > 0, so the class is empty on the whole positive-characteristic locus. (It is **not** empty on X₀: the classical points X₀(C) ⊂ X̌₀(C) have defect 0. That makes the outcome worse, not better — the archimedean reading yields a system with an empty periodic locus.)"
*And replace the last sentence of §6* ("…so his intended reading is presumably the transport reading of §4 (D3), consistent with his 'not N-invariant' verdict on it") *by:*
> "…so a nonempty threshold reading is unavailable. Which reading Deninger intended is **not determined by the evidence on disk**: the threshold class is *also* non-N-invariant (F<sub>ν</sub> of a small-defect character has defect P(r+s)<sup>ν</sup> − P(r)<sup>ν</sup> − P(s)<sup>ν</sup>, uncontrolled), so the p. 29 verdict does not discriminate between the readings. [Conjecture, no evidential support; flagged.]"

### R-B2 (for MINOR B-2) — Lemma B's statement and justification
*Replace* "at every point of every packet (any prime p, any character P in any class E ⊆ E<sub>tors</sub>) … since P(2̄) is a root of unity or 0 (κ(x)<sup>×</sup> is torsion; 0 occurs iff p = 2)"
*by:*
> "at **every** point (x, P<sup>×</sup>) with char κ(x) = p > 0 — periodic or not, in any class or none — of any arithmetic scheme flat over Spec Z … since 2̄ lies in the **prime field** F<sub>p</sub>, so P(2̄) is 0 (iff p = 2) or a root of unity of order dividing p−1; in either case |P(2̄)| ∈ {0, 1} and |P(2̄) − 2| ≥ 1, with equality iff P(2̄) = 1."

### R-B3 (for MINOR B-3) — the consequence to bank
*Add at the end of Lemma B:* "In particular the archimedean threshold class satisfies **none** of §3's requirements even degenerately: it does not cut each packet to one orbit, it deletes every packet; and it is not admissible, since F<sub>ν</sub> does not preserve a defect threshold."

### R-C1 (for MINOR C-1) — Lemma C's hypothesis
*Replace* "for C the complex numbers (or any algebraically closed field of characteristic 0 containing Q̄ with infinite transcendence degree)" *by* "for **any** algebraically closed field C of characteristic 0 (no hypothesis on the transcendence degree is needed; C automatically contains a copy of Q̄)".

### R-C2 (for MINOR C-2) — Lemma C's derivation
*Replace the derivation* by:
> "*Derivation.* (1) The cyclotomic character Gal(Q(µ<sub>∞</sub>)/Q) → Ẑ<sup>×</sup> is an isomorphism — injective because Q(µ<sub>∞</sub>) is generated by µ<sub>∞</sub>, surjective because [Q(µ<sub>n</sub>):Q] = φ(n), i.e. by irreducibility of the cyclotomic polynomials over Q **[classical; not verified from an on-disk source]**. Pick τ ∈ Aut(Q(µ<sub>∞</sub>)/Q) with τ(ζ) = ζ<sup>u</sup>. (2) Extend τ to τ̄ ∈ Aut(Q̄) by the isomorphism-extension theorem (Zorn). (3) Choose a transcendence basis B of C over Q̄ (Zorn) and extend τ̄ to Q̄(B) by acting on coefficients and fixing B pointwise. (4) C is an algebraic closure of Q̄(B); extend again (Zorn) to σ ∈ Aut(C). Then σ|<sub>µ(C)</sub> = u. **Choice is used exactly three times, in (2), (3), (4).** ∎"

### R-C3 (for MINOR C-3) — record the discontinuity inside Lemma C
*Add to Lemma C:* "**Scope.** Any σ realizing u ∉ {±1} is necessarily **discontinuous**: a continuous automorphism of C fixes Q, hence R by density, hence is the identity or complex conjugation, which realize u = 1 and u = −1. Consequently Lemma C is a ZFC statement, and nothing derived from it may be composed with a topological statement about X₀ (see Lemma D's scope note)."

### R-D1 (for MINOR D-1) — the missing scope statement on Lemma D
*Add as a new clause (iv) of Lemma D:* "**(iv) Scope: the action is not continuous.** X<sup>•</sup>(C) carries the topology of pointwise convergence ([x-03] p. 40) and by Lemma C's scope note the relevant σ are discontinuous automorphisms of C, so P ↦ σ ∘ P is not continuous. Lemma D, Proposition 1 and everything derived from them are therefore **set-theoretic, flow-equivariant** statements. They must not be chained with any closure, compactness or minimality statement — in particular not with the 9.3 adjudication's Theorem A."

### R-D2 (for MINOR D-2) — Lemma D(ii)'s one-line reason
*Replace* "(kernels are unchanged — ker(σ∘P) = ker P — and images map by σ, preserving torsion and ⊗Q-dimension; Def. 4.1's operations are pre-compositions, which commute with σ)"
*by:*
> "(σ|<sub>C<sup>×</sup></sub> is a group automorphism, so ker(σ∘P) = ker P and (ker(σ∘P))|<sub>κ(x₀)<sup>×</sup></sub> = (ker P)|<sub>κ(x₀)<sup>×</sup></sub> — which settles (Tors), E<sub>f</sub>, E<sub>fg</sub>, E<sub>fd</sub>, E<sub>fd0</sub>, **all of which are kernel conditions, the ⊗Q-dimension ones included**; and (Image), the only image condition, asks whether P(κ(x)<sup>×</sup>) is torsion, which is invariant under the group isomorphism σ. Def. 4.1's operations are pre-compositions and commute with σ, so σ∘E is admissible whenever E is. Each verification is biconditional, applying the same to σ<sup>−1</sup>.)"

### R-D3 (for MINOR D-3) — the word "stable"
*Everywhere the note writes "stable" for the Aut(C)-property, write "**Aut(C)-stable**", and add once:* "([x-03] p. 29 uses '**stable**' for a different property — restriction to algebraically closed subfields — under which '**all classes in the example are stable except for (Image) and hence E<sub>max</sub>**'. The two senses are unrelated; E<sub>max</sub> is Aut(C)-stable but not stable in Deninger's sense.)"

### R-D4 (for MINOR D-4) — the "R-coordinate"
*Replace* "descends to the suspension X₀<sup>E<sub>tors</sub></sup> commuting with the flow φ<sup>t</sup> and fixing the R-coordinate"
*by:*
> "descends to the suspension X₀<sup>E</sup> by [P₀, u] ↦ [σP₀, u] and commutes with the flow φ<sup>t</sup> (there is no invariant 'R-coordinate' on X₀: u is defined only up to the Q<sup>>0</sup>-identification). It preserves each packet Γ<sup>E</sup><sub>x₀</sub> and acts trivially on the canonical projection (40) C<sub>x₀</sub> → Q₀<sup>>0</sup>/p<sup>Z</sup>, since it does not change |ker P<sup>×</sup>|."

### R-P1 (for MINOR P-1) — Proposition 1's anchor
*Replace* "since the fibers of the (38)-fibration are the Q<sup>>0</sup>-orbits ([x-03] p. 33)"
*by:*
> "since the fibres of the packet fibration are the flow orbits — stated for the suspension itself at [x-03] **p. 38**, verbatim: '*Thus all R<sup>>0</sup>-orbits in Γ<sub>x₀</sub> are circles R<sup>>0</sup>/N x₀<sup>Z</sup> and Γ<sub>x₀</sub> fibres over Ẑ<sup>×</sup><sub>(p)</sub>/p<sup>Ẑ</sup> = Aut(F̄<sub>p</sub><sup>×</sup>)/Aut(F̄<sub>p</sub>) with fibres the R<sup>>0</sup>-orbits in Γ<sub>x₀</sub>*' (the p. 33 statement is the pre-suspension version and needs a translation the note does not give)"

### R-P2 (for MAJOR P-2) — Proposition 1's missing hypothesis
*Either* **(a)** *replace* "Let E be any Aut(C)-stable class (all named example classes qualify)" *by*
> "Let E be an admissible Aut(C)-stable class **with E ⊆ E<sub>max</sub>** (so that [x-03] Thms 5.2/6.1 apply; E<sub>f</sub>, E<sub>fg</sub>, E<sub>fd</sub>, E<sub>fd0</sub> and E<sub>max</sub> all qualify — **E<sub>tors</sub> does not**, since E<sub>max</sub> ⊂ E<sub>tors</sub>)"
*or* **(b)** *keep the class general and replace the hypothesis on the point by*
> "If S contains a periodic point **lying in the packet Γ<sup>E</sup><sub>p</sub>**"
*In either case add to the proof, at step 1:* "by [x-03] Thm 6.1 (p. 39) — this is where E ⊆ E<sub>max</sub> is used — the periodic point lies in a unique packet Γ<sup>E</sup><sub>x₀</sub>, its orbit is a circle of length log N x₀ = log p, and by the p. 38 fibration it has a well-defined base class [a] ∈ B<sub>p</sub>."
*(Variant (a) is recommended: it matches the certified window E ⊇ E<sub>f</sub> and keeps the headline. Nothing the note does with Proposition 1 needs E<sub>tors</sub>.)*

### R-P3 (addition, not a defect) — Corollary 1′, the sharpest form of D1
*Add after Proposition 1:*
> "**Corollary 1′.** For every admissible Aut(C)-stable E ⊆ E<sub>max</sub> and every prime p: if X₀<sup>E</sup> contains one periodic point over p, then Γ<sup>E</sup><sub>p</sub> = Γ<sub>p</sub>. (Take S = X₀<sup>E</sup> in Proposition 1.) This is an independent second proof of [x-03] Thm 5.2's full-packet phenomenon, under a hypothesis not comparable with E ⊇ E<sub>f</sub>; the two agree on every named class in E<sub>f</sub> … E<sub>max</sub>. It is the theorem-grade core of D1, and it does not use the 'canonical ⟹ Aut(C)-stable' schema at all."

### R-H1 (for MAJOR H-1) — §7 Road 2's count
*Replace* "since the integrand is constant (all orbits in Γ<sub>p</sub> have length log p — [x-06] Thm 4.2)"
*by:*
> "the integrand being constant for the following reason — **not** because the orbits share a length, which alone says nothing about an unspecified orbital weight. Let W be any assignment of a weight to the closed orbits of Γ<sub>p</sub> that is invariant under automorphisms of the ambient system commuting with the flow. By Lemma D every σ ∈ Aut(C) is such an automorphism, and by Lemma D(iii) with Lemma C the induced action on the closed orbits of Γ<sub>p</sub> is the **transitive** translation action on B<sub>p</sub>; hence W is constant and ∫<sub>B<sub>p</sub></sub>W dHaar = W(γ). **Caveat, which must travel with this argument:** the σ are discontinuous (Lemma D(iv)), so this covers only weights invariant under *set-theoretic* flow-commuting automorphisms. An orbital weight built from transverse analytic data need not be of that kind, and no continuous transitive action on B<sub>p</sub> is available (the Galois action is already quotiented out; the flow fixes the base; changing ι is the same operation as some σ). **Homogeneity of an analytically defined orbital weight along B<sub>p</sub> is therefore a second open precondition of Road 2, alongside DQ-M.**"

### R-H2 (addition, not a defect) — why Haar is canonical although the coordinates are not
*Add to Road 2:*
> "The canonicity has a precise form. [x-03] p. 33 warns that '*The maps (37), (38) and the fibration map depend on our choices of x and ι*'. Every change of those choices acts on the base by a **translation** (ι ↦ ι∘( )<sup>u</sup> gives a ↦ ua; changing x acts through Gal(κ(x)/κ(x₀)) = p<sup>Ẑ</sup>, trivial on B<sub>p</sub>). So canonically the base is a **torsor** under B<sub>p</sub>, not the group B<sub>p</sub>; a torsor under a compact group carries a unique invariant probability measure, and that measure is what Road 2 uses. **Haar is canonical for exactly the reason that a point of B<sub>p</sub> is not** — which is D3, restated as a positive."

### R-N1 (addition, not a defect) — the complete accounting in §3
*Add at the end of §3:*
> "Sharper: for **every** mod-p-additive P at a char-p point and every ν whose prime-to-p part exceeds 1, F<sub>ν</sub>(P) is not mod-p additive. (By Lemma A, P = [·]∘τ; if F<sub>ν</sub>(P) were mod-p additive its reduction τ∘( )<sup>ν</sup> would be a ring homomorphism, forcing (a+b)<sup>ν</sup> = a<sup>ν</sup> + b<sup>ν</sup> on F̄<sub>p</sub>, which fails because (X+Y)<sup>ν</sup> − X<sup>ν</sup> − Y<sup>ν</sup> is a nonzero polynomial over F<sub>p</sub> when ν is not a p-power — e.g. binom(ν, p<sup>e</sup>) ≡ m mod p for ν = p<sup>e</sup>m, p ∤ m — and a nonzero polynomial over the infinite field F̄<sub>p</sub> has a non-root.) So the admissible closure of a mod-p-additive condition contains characters at arbitrarily bad defect while retaining exactly one base class per prime: **§3 and §4's D3 are the same phenomenon seen twice.**"

### R-T1 … R-T5 (transcription)
* **R-T1.** Print the display as "**B<sub>p</sub> := Ẑ<sup>×</sup><sub>(p)</sub>/p<sup>Ẑ</sup> = Aut(F̄<sub>p</sub><sup>×</sup>)/Aut(F̄<sub>p</sub>)**" ([x-03] p. 33; also p. 38 and [x-06] p. 12) — the × belongs on F̄<sub>p</sub> inside the first Aut, and the second Aut is of the **field** F̄<sub>p</sub>.
* **R-T2.** Change the two citations of "does not give more points" from p. 5 to **p. 6**.
* **R-T3.** Print the [D25] quotation as "…the more information the ring W<sub>rat</sub>(A) has about the additive structure of A…" and put the gloss outside the quotation, e.g. "(W<sub>rat</sub>(A) = (ZĀ)<sup>G</sup>, the paper's display (3), p. 2)".
* **R-T4.** Change "§14 pp. 89–100" to "§14 pp. 89–101", and cite Remark 14.17 at **p. 104** where (F5) invokes the Aut(o)-action.
* **R-T5.** Replace the [D25] bookkeeping bullet by: "[D25] is on disk at `fetched-r3/r3s-22-deninger-rational-witt-vectors-associated-sheaves-arxiv-2508.05329v1-SESSION8-FETCH.pdf`; the promotion item is discharged."

---

## 13. VERDICT BLOCK

**Overall verdict on the assigned item (Lemmas A–D, Proposition 1, plus §3 and §7's derivations): PASS-WITH-REPAIRS.**
**FATAL 0 · MAJOR 5 · MINOR 18.**

| # | Severity | Location | Finding | Repair |
|---|---|---|---|---|
| **A-1** | **MAJOR** | §4, Lemma A statement | "κ an algebraically closed field of characteristic p" is wrong: κ<sup>×</sup> is torsion only for κ ≅ F̄<sub>p</sub>, and "[·]∘τ" does not typecheck otherwise ([·] is defined only on µ<sup>(p)</sup>). | R-A1 |
| **A-2** | **MAJOR** | §4, Lemma A (⇐) | The converse's justification ("W(k) ⊆ o", "V F = p") is unavailable under the note's own hypotheses (**m** ⊋ p·o; no map W(k) → o constructed) and is invoked from memory. **The statement is TRUE**; a self-contained proof is supplied. | R-A2 |
| **A-4** | **MAJOR** | §4 Consequence 2 (D3) | The identification carries a false clause under either reading: the transported condition C<sub>j</sub> is *not* admissible, while E(a₀) *is* admissible and therefore **is** N-invariant. | R-A4 |
| **P-2** | **MAJOR** | §5, Proposition 1 | The proof's step 1 consumes [x-03] Thm 6.1, whose hypothesis **E ⊆ E<sub>max</sub>** the proposition does not state and which **fails for E<sub>tors</sub>**, a class the proposition's parenthetical invites. Not re-derived for E<sub>tors</sub>. | R-P2 |
| **H-1** | **MAJOR** | §7 Road 2 | "the integrand is constant (all orbits in Γ<sub>p</sub> have length log p)" does not establish constancy of an unspecified orbital weight. A homogeneity fill is supplied **together with an explicit statement of how weak it is** (the σ are discontinuous). | R-H1 |
| A-3 | MINOR | §2 | Coefficient setup attributed to pp. 78/89; the algebraically-closed and char-0 hypotheses are at pp. 105–106. | R-A3 |
| A-5 | MINOR | §4, Lemma A | The surjectivity half of µ<sup>(p)</sup>(o) ≅ µ<sup>(p)</sup>(k) is argued circularly; Hensel supplies it in two lines. | R-A5 |
| B-1 | MINOR | §0 (D2), §6 | "empty set" needs its locus (empty on the char-p locus, **not** on X₀); and the closing inference about Deninger's intent has no evidential support, since the threshold reading is *also* non-N-invariant. | R-B1 |
| B-2 | MINOR | §6, Lemma B | Justification cites "κ(x)<sup>×</sup> is torsion"; the operative fact is that 2̄ ∈ F<sub>p</sub>, which extends the lemma to the whole positive-characteristic locus of any arithmetic scheme. | R-B2 |
| B-3 | MINOR | §6, Lemma B | The consequence that makes it a trichotomy branch (no periodic point survives; the class is not admissible either) is not stated. | R-B3 |
| C-1 | MINOR | §5, Lemma C | "containing Q̄ with infinite transcendence degree" is superfluous. | R-C1 |
| C-2 | MINOR | §5, Lemma C | Derivation's last clause is garbled; the one external input (surjectivity of the cyclotomic character) is unnamed and must be flagged classical. | R-C2 |
| C-3 | MINOR | §5, Lemma C | The realizing σ are necessarily discontinuous; this belongs in Lemma C, not only in a later scope note. | R-C3 |
| D-1 | MINOR | §5, Lemma D | Missing scope clause: the action is not continuous, so Lemma D/Prop. 1 must not be chained with closure statements (e.g. the 9.3 Theorem A). | R-D1 |
| D-2 | MINOR | §5, Lemma D(ii) | The ⊗Q-dimension conditions are **kernel** conditions; the printed one-liner attaches them to the image side. | R-D2 |
| D-3 | MINOR | §§5–6 | "stable" collides with [x-03] p. 29's technical term, under which E<sub>max</sub> is *not* stable. | R-D3 |
| D-4 | MINOR | §5, Lemma D(i) | "fixing the R-coordinate": there is no invariant R-coordinate on X₀. | R-D4 |
| P-1 | MINOR | §5, Prop. 1 proof | Cites p. 33 (C<sub>x₀</sub>, Q<sup>>0</sup>-orbits) where p. 38 states the suspension version directly. | R-P1 |
| T-1 | MINOR | §4 | The displayed identity for B<sub>p</sub> is false as transcribed; the source reads Aut(F̄<sub>p</sub><sup>×</sup>)/Aut(F̄<sub>p</sub>) (verified by page render). | R-T1 |
| T-2 | MINOR | §2, §6 | "does not give more points" is on p. 6, not p. 5. | R-T2 |
| T-3 | MINOR | §7 Road 1 | Unbracketed interpolation inside a verbatim [D25] quotation. | R-T3 |
| T-4 | MINOR | §1 | §14 range should be 89–101; Remark 14.17 is on p. 104. | R-T4 |
| T-5 | MINOR | §10 | The [D25] promotion has happened; the bookkeeping bullet is stale. | R-T5 |

Non-defect additions recommended: **R-P3** (Corollary 1′ — the theorem-grade core of D1), **R-H2** (why Haar is canonical although the coordinates are not), **R-N1** (the complete accounting in §3).

### What is now established at referee grade, and its precise scope

**Established.** (1) **Lemma A**, for κ ≅ F̄<sub>p</sub>, k algebraically closed of characteristic p, and o a p-adically complete rank-1 valuation ring with residue field k: the multiplicative maps κ → o with additivity defect ≤ |p| are exactly the prime-to-p Teichmüller lifts of the field embeddings κ ↪ k, uniquely, and |p| is the **sharp** constant (witness p = 2, r = s = 1). Both directions are re-derived here in full; the converse now has a proof using nothing but integer binomial coefficients and the ultrametric inequality, and the Teichmüller section is obtained from henselianity rather than from a circular divisibility argument. Independently, the statement is confirmed against [x-03] p. 113 ("the ring homomorphisms P̂<sup>♭</sup><sub>y</sub> : κ ↪ k ⊂ o<sup>♭</sup>") and Thm 15.6(1)'s closed-point fibre Y<sup>⋄</sup><sub>s</sub> = Hom(κ, k) (p. 114), both read verbatim. Consequently mod-p additivity cuts the Ẑ<sup>×</sup><sub>(p)</sub>-torsor of coefficient identifications down to a p<sup>Ẑ</sup>-torsor, and the residue is exactly **B<sub>p</sub> = coker(Aut(F̄<sub>p</sub>) ↪ Aut(F̄<sub>p</sub><sup>×</sup>))** — Deninger's own display on p. 33.
(2) **Lemma B**, in the strengthened form: at every positive-characteristic point of any arithmetic scheme flat over Spec Z, and for every character whatever, the pair r = s = 1 forces archimedean additivity defect ≥ 1, with equality attainable; so a uniform archimedean threshold ε < 1 selects a class with **no periodic points at all** (though it is not the empty class — it contains the classical points), and [x-03]'s I-adic extension mechanism (172) degenerates to the zero ring over C. The threshold class also fails Def. 4.1.
(3) **Lemma C**: Aut(C) ↠ Aut(µ(C)) = Ẑ<sup>×</sup> for every algebraically closed C of characteristic 0, with choice used exactly three times, with one named classical input (irreducibility of the cyclotomic polynomials, flagged), and with the realizing automorphisms necessarily discontinuous.
(4) **Lemma D**: the post-composition action of Aut(C) commutes with G, with every F<sub>ν</sub>, with the Q<sup>>0</sup>-action and with the flow; it preserves **biconditionally** each of E<sub>tors</sub>, E<sub>max</sub>, E<sub>f</sub>, E<sub>fg</sub>, E<sub>fd</sub>, E<sub>fd0</sub> — (Image) for E<sub>max</sub>, the note's own press point, being the *easiest* of the six; and it acts on the packet coordinates by (a, ν) ↦ (u<sub>σ</sub>a, ν), i.e. by translation on B<sub>p</sub>, transitively.
(5) **Proposition 1**, once R-P2 is applied: for admissible Aut(C)-stable E ⊆ E<sub>max</sub>, no Aut(C)-stable flow-invariant subset of X₀<sup>E</sup> contains exactly one periodic orbit over a prime; it contains one in every base class, hence uncountably many. Every input — the (34)/(35)/(38) coordinates, the p. 38 fibration whose fibres are the orbits, the uncountability of B<sub>p</sub>, the transitivity of Aut(C) on B<sub>p</sub> — was re-derived here from the primary text, not imported. The proposition is **sharp**: dropping E's Aut(C)-stability is exactly what the Theorem-C cuts do, and they satisfy the negated conclusion.

**Scope, stated precisely.** These results are about **X₀ = Spec Z with C-valued points in Deninger's [x-03] framework**, and about **set-level, flow-equivariant** structure only. They use **no topology**: the Aut(C)-action is not continuous (D-1), so nothing here may be composed with the 9.3 adjudication's Theorem A, with compactness, with closure, or with minimality. Proposition 1 constrains **Aut(C)-stable** selections; the passage from "canonical" to "Aut(C)-stable" is a definability schema, flagged as such in the note and left flagged here — the theorem-grade content is Corollary 1′ (R-P3): every Aut(C)-stable admissible E ⊆ E<sub>max</sub> that meets a packet carries the **full** packet. Lemma B rules out the **uniform-threshold** archimedean reading only; averaged, asymptotic and comparative defect-profile conditions are untouched, as the note correctly says, and I add that no candidate for those appears in any source read here. Lemma A is a statement about the **closed-point stratum** of the local theory; it says nothing about the generic stratum Y<sup>⋄</sup><sub>η</sub>, where the Fargues–Fontaine content lives. Nothing in this report bears on the ledger's substrate defects W1/W6/W12, on positivity or Hodge-type clauses (the note's own Z2 quarantine), on Theorem C's reachability computation (imported, not re-derived, and not load-bearing here), or on whether any trace formula exists — Road 2's count is now correctly labelled as formal, and it acquires one further named open precondition (homogeneity of an analytic orbital weight along B<sub>p</sub>). Finally, **the trichotomy D1–D3 stands**: D1 on Proposition 1 (verified, sharp, with one hypothesis to be added), D2 on Lemma B (verified, strengthened, with its locus corrected), D3 on Lemma A plus the transport analysis (verified, with the identification corrected by R-A4). After the five MAJOR repairs are applied the note's §0 verdict is, in my judgment, correct as stated and correctly scoped.

---

## 14. Sources — every page read this session

Extraction with `pdftotext -layout` (poppler 26.08.0); two displays additionally read as rendered images (`pdftoppm -r 200 -png`), per corpus-routing caveat 1 (no third-party OCR; Claude vision only).

* **[x-03]** Deninger, *Dynamical systems for arithmetic schemes*, arXiv:1807.06400v4 — `fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf`. **Printed page = PDF page** (verified on pp. 27, 33). Pages read: **5** (intro: "minimal condition E … does not look natural"; the completion narrative); **6** ("this process does not give more points"; "The answer is simple, Y<sup>⋄</sup> consists of …"; "the process of 'completion' … was necessary"); **25** ((28), (29), Def. 3.6, Prop. 3.7); **26** ("The best condition on the characters P<sup>×</sup> is not clear to me." begins; the passage to subsystems); **27** ((Tors), (Image), **Def. 4.1**, **Prop. 4.2**, (30), (31)); **28** (Lemma 4.3, Cor. 4.4, E<sub>tors</sub>, E<sub>max</sub>); **29** (E<sub>f</sub>, E<sub>fg</sub>, E<sub>fd</sub>, E<sub>fd0</sub>; the inclusion chain; the "**additive mod p … not N-invariant**" Remark; the *stable*-class definition and the E<sub>max</sub> exception; functoriality); **30** (Prop. 4.5 proof, Lemma 4.6); **31** (§5 setup, the hypothesis on C, the choice of ι, (32), (33), C<sub>x₀</sub>); **32** (**(34)**, **(35)**, the fibre relation, (36), (37), the isotropy computation); **33** (**(38)**, **(39)**, **the fibration display — read by page render**, the "depend on our choices of x and ι" warning, (40)–(46)); **34** (Prop. 5.1, **Thm 5.2** with its hypothesis E ⊂ E<sub>max</sub>, (47), (48)); **38** (§6: the suspension, φ<sup>t</sup>, Γ<sub>x₀</sub>, **"all R<sup>>0</sup>-orbits … are circles … Γ<sub>x₀</sub> fibres over … with fibres the R<sup>>0</sup>-orbits"**); **39** (**Thm 6.1** with its hypothesis and the "any periodic orbit … is contained in Γ<sup>E</sup><sub>x₀</sub>" sentence; the X<sup>•</sup>-description remark; the X₀(C) × R<sup>>0</sup> immersion); **40** (§7 opening: **the pointwise-convergence topology**, metrizability; Lemma 7.1; **the S4 question with both alternatives**); **89** (§14 setup, "**we only consider the monoid N₀ generated by p**", Def. 14.1); **90** (Def. 14.1's diagram, (163), Def. 14.2); **91** (the continuity discussion, Prop. 14.3); **93** (Fontaine (170)–(171), A<sub>inf</sub>(X), the [CD14] presentation of W<sub>p</sub>(R), I generated by [r+s]−[r]−[s]); **94** (**Def. 14.5**, (172)–(174), **Prop. 14.7**); **95** (the proof of 14.7 — the ultrametric estimate and the (175)/(176) second proof); **98** (Prop. 14.11, (181)); **99** (**Def. 14.12 = (183)**, (184), (185), **the "I do not know how to transport such conditions" Remark**); **100** (**Prop. 14.13**, **Prop. 14.14**, (186)–(191)); **101** (the proof of 14.14, (192)–(194)); **104** (**Remark 14.17**, §15 opening, the Lubin–Tate setup, (197)); **105** ((198)–(200); "**From now on let o be …**"); **106** ("**k its algebraically closed residue field**"; "**k is also a subfield of o<sup>♭</sup>**"; H<sub>κ₀</sub>(o<sup>♭</sup>), (201)–(203); "**κ … an algebraic closure of κ₀**"); **113** (the (η,s)/(s,s) strata, "**the ring homomorphisms P̂<sup>♭</sup><sub>y</sub> : κ ↪ k ⊂ o<sup>♭</sup>**", (219)–(220), **Thm 15.6(1)**); **114** (**Thm 15.6(2)–(6)**, (221)–(226), the closing Remark); **115** (the proof of 15.6(6), **Prop. 15.7**, (227)–(228)); **116** (**Prop. 15.8** and its proof).
* **[x-06]** Deninger, *Primes, knots and periodic orbits*, arXiv:2301.11643 — `fetched/x-06-deninger-2024-primes-knots-and-periodic-orbits.pdf`. Pages read: **10** (W<sub>rat</sub>(X)(S), the Teichmüller map, (11)); **11** (**Thm 4.1** with the G- and N-actions written out, the suspension X₀ and φ<sup>t</sup>, the "**too many periodic orbits / we can only impose an 'admissible' condition E**" paragraph, **Thm 4.2** begins); **12** (**Thm 4.2** concluded — orbit length log N x₀, **the fibre space over Aut(F̄<sub>p</sub><sup>×</sup>)/Aut(F̄<sub>p</sub>) with fibres the compact orbits, read by page render**, "all of which have length log N x₀ i.e. log p"; Thm 4.3; the infinite-dimensionality paragraph; X<sup>•</sup>(C)<sub>in</sub>); **13** (**Thm 4.4** and the non-homeomorphism remark; Kucharczyk–Scholze; the Steinberg-relations sentence).
* **[D25]** Deninger, *Rational Witt vectors and associated sheaves*, arXiv:2508.05329v1 — `fetched-r3/r3s-22-deninger-rational-witt-vectors-associated-sheaves-arxiv-2508.05329v1-SESSION8-FETCH.pdf`. Pages read: **1–3** (introduction in full: the "numbers are functions" argument, displays (1)–(3), and the "**stronger descent conditions**" sentence, verbatim).
* **[r3s-08]** Morishita, arXiv:2508.15971 — `fetched-r3/r3s-08-morishita-deninger-cc-bridge-2508.15971.pdf`. On disk; **not consulted for any claim in this report**.

**Program-internal documents read.** `results/c3-r/probe-9.3-adjudication.md` (in full); `results/c3-r/probe-9.4-note.md` (in full, 136 lines); `results/corpus-routing.md` standing caveats 1–20.

**Classical facts used and flagged (each either non-load-bearing or replaced).**
1. *Surjectivity of the cyclotomic character* Gal(Q(µ<sub>∞</sub>)/Q) ↠ Ẑ<sup>×</sup> — **[classical, not on disk]**. Used only in Lemma C step 1; it is the single external input of the whole item, and R-C2 requires the note to name and flag it.
2. *The Witt identity V W(k) = p W(k) for perfect k* — **[classical, not on disk]**, invoked only to *describe* what the note's converse argument was reaching for. My repair R-A2 replaces it entirely with an argument that reads nothing off-disk.

— end of referee report O —
