# NOVELTY CHECK AGAINST THE LUTZ DISSERTATION — check **O** (standing order 7, one of two independent checks)

**Program:** RH program, direction C3-r (geometric substrate, reduced recommission). **Session 14.**
**Date:** 2026-09-02.
**Author:** referee/verification agent, check **O** (Opus 5). A second agent (Fable 5.1) performs the same task independently; nothing below has been softened in expectation of what that check will find, and nothing from it was consulted.

**Target document.**
`fetched-r3/r3s-23-lutz-2025-p-adic-points-rational-witt-spaces-muenster-diss-SESSION14-FETCH.pdf`
Judith Marie Lutz, *p-adic points of rational Witt spaces*, Inaugural-Dissertation, Fachbereich Mathematik und Informatik, Universität Münster, 2025. 99 PDF pages (printed pp. i–iv, 1–92). Read from the PDF title pages: *"Erster Gutachter: Prof. Dr. Christopher Deninger. Zweiter Gutachter: Prof. Dr. Thomas Nikolaus. Tag der mündlichen Prüfung: 5. Juni 2025. Tag der Promotion: 5. Juni 2025."* (PDF p. 2, OCR-read; the page carries no mathematics.)

**Companion OCR.** `fetched-r3/r3s-23-…-OCR.txt` (tesseract, page-marked `=== page N ===`, N = PDF page). Used **only** to locate passages and to run the grep table in §4. Every quotation below was then read from the rendered page image with the Read tool. OCR completeness was audited: the only pages with <10 OCR lines are PDF pp. 02, 04, 21, 22, 33, 34, 48, 56, 78, 90, 99, and each was inspected — they are the title verso, blank versos, and short end-of-chapter pages. No page was silently dropped.

**Pagination convention used throughout.** PDF page N = printed page N − 6 in the body (front matter is unnumbered/roman). Both are given: e.g. "printed p. 2 (PDF p. 8)".

**Standing order 5 compliance.** Every claim below about the thesis is anchored to a page I rendered and read this session. Nothing is recalled. Where I rely on the OCR alone (only for negative grep evidence and for the two sparse-page checks) I say so explicitly.

---

## 0. VERDICT TABLE (stated first)

| # | Session-8 claim | Verdict w.r.t. **this thesis** |
|---|---|---|
| **N1** | Packet-closure law in Deninger's X₀ = X(Spec Z): cl(one periodic orbit) ⊇ its whole packet Γ_p; forcing group = coker(lk_p); mechanism = profinite accumulation of Frobenius return exponents | **NOVEL w.r.t. thesis** — the thesis contains no periodic orbit, no flow, no packet, no linking map, and no topological-dynamical closure. Does not touch. |
| **N2** | X₀ non-Hausdorff along its packets; every closed flow-invariant subset meeting every packet is infinite-dimensional; Deninger's first alternative ([x-03] §6 p. 40) answered NO | **NOVEL w.r.t. thesis** — no separation axiom, no dimension theory, no sub-dynamical system, no reference to Deninger's §6 question anywhere. Its one topological chapter (Ch. 8) is a p-adic metric/convergence study of X⁺(V)/G. Does not touch. |
| **N3(a)** | B_p = coker(Aut_ring(F̄_p) → Aut_group(F̄_p^×)) = coker(lk_p) as the packet base | **NOVEL w.r.t. thesis** — the group Ẑ^×_(p)/p^Ẑ, the map lk_p, and the word "packet" are absent. Does not touch. |
| **N3(b)** | No Aut(C)-stable one-orbit-per-packet selection exists | **NOVEL w.r.t. thesis** — Aut(C) never appears (the only two occurrences of `Aut(` are the Galois group Aut(K\|K₀)); no selection/choice-of-ι discussion, no descent datum. Does not touch. |
| **N3(c)** | The transport of the local mod-p-additivity principle to C selects nothing canonical | **PARTIAL** — the thesis is the fullest published exposition of the mod-p-additivity principle itself (Ch. 4, following Deninger's Def. 14.5/14.12), and it states **in print, on printed p. 2, that the C-analogue is desirable and "currently … not known."** The *desideratum* is therefore anticipated and must be cited; the *transport itself* is never attempted and no no-go is stated. See §2.3 — this is the one place the note's framing must change. |
| **N4** | Haar-averaging the packet base in place of a one-orbit selection; a trace formula for foliated flows with a continuum of periodic orbits and a transverse measure on the continuum | **NOVEL w.r.t. thesis** — zero occurrences of Haar, measure, trace, foliation, lamination, leaf, transverse. Does not touch. |
| **N5** | One-orbit-per-prime admissible cuts exist but are non-canonical | **NOVEL w.r.t. thesis** — no cut, no selection, no admissibility class, no condition E. Does not touch. |

**Net.** The Lutz dissertation **anticipates none of N1–N5 as a theorem or as a question**, and the DQ-L item can be closed on the negative side. The single substantive consequence for the Session-8 notes is a **framing obligation on N3(c)**, detailed in §2.3.

**The finding that gives these verdicts their weight (§3).** The thesis's *only* Deninger citation is `[Den22] = arXiv:1807.06400` — the very paper N1–N3 and N5 are about — cited on roughly forty of its ninety-two pages. But it draws exclusively on that paper's **Chapters 1–3 and 14–15** (rational Witt vectors, rational Witt spaces, the p-adic modification X⁺(V), the Fargues–Fontaine identification). It never uses §§4–13, where the flow, the suspension X₀ = X̌₀(C) ×_{Q^{>0}} R^{>0}, the packets Γ_{x₀}, the foliation and the cohomology live. This is not a coincidence of vocabulary: the dissertation is a deliberate development of the *other half* of [x-03]. That a student of Deninger, examined June 2025, worked for ninety pages inside that paper and never once touched the packet structure is about as strong a negative as a single document can give.

---

## 1. What the thesis actually does (page-cited)

**One-paragraph summary.** The thesis develops the **p-adic** branch of Deninger's rational-Witt-space program. Starting from Deninger's ringed space W_rat(X) (scheme X, same underlying space, structure sheaf sheafified from U ↦ W_rat(O_X(U))), it studies not the C-valued points but the V-valued points for V a p-adically complete rank-one valuation ring of mixed characteristic, and spells out Deninger's chain of modifications: impose p-adic continuity, invert Frobenius by a colimit, complete, and finally impose **additivity modulo p** (equivalently quasi-additivity, |φ(x+y) − φ(x) − φ(y)| ≤ 1/p), producing the set X⁺(V) with bijective Frobenius on which the infinitesimal period ring A_inf(X) induces V-valued functions via e: A_inf(X) → C(X⁺(V), V) (printed pp. 1–2, PDF pp. 7–8; the definitions are Def. 4.17 and Def. 4.20, printed p. 37, PDF p. 43, following [Den22, Def. 14.5] and [Den22, Def. 14.12]). Five results follow, all p-adic: **Theorem A** (= Thm 6.42, printed p. 71, PDF p. 77) — *"There is an injection X₀⁺(V)_η ≔ X⁺(V)_η/G ↪ Spa((R₀)_p, R₀)^◇(Spa(C♭, V♭))"*, generalizing [Den22, Thm 15.6] from Spec(O_{K₀}) to any R of finite type over Z_p, at the cost that the map is no longer a bijection; **Theorem B** (= Thm 5.1, printed p. 43, PDF p. 49) — the restriction e′: A_inf(X) → C(X^#(V), V) to the Frobenius translates of the classical points is **injective**, i.e. *"the set X^#(Z̄_p) formed by the classical scheme theoretic points and their Frobenius translates is 'A_inf(X)-dense' in X⁺(V)"* (printed p. 43, PDF p. 49), proved by a Diophantine construction using the reduced fibre theorem; **Theorem C** (= Thm 7.24, printed p. 83, PDF p. 89) — *"The map X⁺(A⁺)/G → Div¹(X_{S,K₀}), φG ↦ (W_{O_{K₀}}(φ)(ξ)) is well-defined … For A⁺ = V a p-adically complete rank one valuation ring with algebraically closed quotient field, the restriction of this map to the subset corresponding to the generic fibre of X₀⁺(V) recovers the map from [Den22, Chapter 15]"*, i.e. a map to the Cartier divisors of the **relative** Fargues–Fontaine curve; **Theorem D** (= Thm 2.20, quoted printed p. 2, PDF p. 8) — *"Let S be a normal integral domain whose quotient field is algebraically closed. Let T be a ring on which a profinite group G acts with finite orbits. Then the canonical map Hom(T,S)/G → Hom(T^G, S) is a bijection"*, a commutative-algebra generalization of [KS16, Lemma 4.9] and [Den22, Lemma 1.7]; and **Theorem E** (= Thm 8.5, quoted printed p. 3, PDF p. 9) — *"If a sequence of elements in the quotient X⁺(V)/G converges to an element with regard to the metric coming from the maximal ideal of V♭, then the sequence converges everywhere pointwise and on a certain dense subset uniformly."*

**Does it treat the archimedean / C-valued points at all?** **Only in the motivation, and only to say the C-side is unsolved.** Two passages, both read from the page image.

Printed p. 1 (PDF p. 7), verbatim:

> "A hypothetical means of bridging this gap between analysis and arithmetic is to associate to such an X an analytic structure incorporating both the archimedean places and the finite places above each prime p. Clearly, just looking at the points of X in the classical sense is not enough—the classical points of X = Spec(Z) over C are just one point spaces whose structure does not reflect the complexity of the Riemann zeta function.
> Presently, there is no satisfactory answer for what these more general spaces of C-valued points, denoted by Ẋ(C), should be."

and, on the same page, the only other archimedean content — a report of Kucharczyk–Scholze:

> "For X = Spec(F) with F a field containing all roots of unity the space studied earlier in [KS16] is a deformation retract of the resulting set of C-valued points W_rat(X)(C). In [KS16] it is on the one hand shown that this deformation retract has desirable properties, e.g. the étale fundamental group agrees with the absolute Galois group of F, thus relating an analytic with an arithmetic property. On the other hand they show that the Steinberg relations do not hold in sheaf cohomology with rational coefficients, which is a deficit of the space."

That is the entirety of the thesis's archimedean content. The word "archimedean" occurs exactly twice in the document (the second, on PDF p. 89 = printed p. 83, is "a non-archimedean field of residue…", i.e. the opposite sense). There is no X₀, no R-action, no packet, no orbit of length log p, no foliation, and no Ẋ(C) beyond the sentence above.

---

## 2. Per-claim findings

### 2.1 N1 (packet-closure law) — **NOVEL w.r.t. thesis; does not touch**

The three constituents of N1 are each absent as a matter of vocabulary *and* of subject:

* **Periodic orbit / flow / packet.** `periodic`, `flow`, `packet`, `suspension`, `leaf`, `lamination`, `solenoid`, `minimal set`, `one-parameter` — **0 occurrences each** in the 99-page OCR (§4).
* **Orbit.** 19 occurrences, every one of them either (i) a **Frobenius orbit** of a point of X(V) — printed p. 2 (PDF p. 8), read from the image: *"We saw that X⁺(V) contains X^#(V), the union of the Frobenius orbits coming from classical points X(V)"* — or (ii) the hypothesis "**finite orbits**" in Theorem D and its lemmas (printed p. 2, PDF p. 8: *"Let T be a ring on which a profinite group G acts with finite orbits"*). Both are algebraic orbits of a discrete/profinite group on a ring; neither is an R-orbit of a flow. The *finiteness* hypothesis is the exact opposite of N1's situation, where the orbit closure is an uncountable Cantor-group packet.
* **Closure.** 41 occurrences, of which the OCR distribution is: `algebraic closure` 25, `integral closure` 18, `absolute closure` 1, `separable closure` 1, `topological closure` 1, `the closure` 1. The last two were checked: the "topological closure" is *"…has a topological closure which equals K♭, see [Sch17, Proposition 1.4.27]"* (density of a subfield in a tilt, PDF p. 84 region, OCR), and "the closure" is the Zariski closure of a scheme point (*"Let U = Spec(R) be an open affine neighborhood of y. Then x ∈ U holds as y is in the closure of…"*, OCR). Neither is a dynamical orbit closure.
* **Linking / Frobenius return exponents.** `linking` and `monodromy` and `class field`: **0 occurrences**. `Frobenius` occurs 45 times, always as the Witt-vector ring endomorphism F_p (or F_n) and its inversion by colimit — never as an Artin symbol, never with a return exponent, never with lk_p.

Nothing in the thesis states, implies, or asks the packet-closure law. **Verdict: NOVEL w.r.t. this thesis.**

### 2.2 N2 (non-Hausdorffness; infinite-dimensionality; Deninger's first alternative) — **NOVEL w.r.t. thesis; does not touch**

* `Hausdorff` — **0 occurrences**. `separated` occurs only as "the presheaf W_rat(O_X) is separated" (sheafification) and "p-adically separated" (OCR-checked). No separation axiom is ever discussed for any space in the thesis.
* `infinite-dimensional`, `uncountab` — **0 occurrences**. `dimension` occurs 5 times, all Krull dimension / "higher dimensional X" in the sense of dim of a scheme of finite type over Z_p. There is no dimension theory of a topological space anywhere.
* Deninger's §6 question (a closed sub-dynamical system with one closed orbit of length log p per prime) is **never mentioned**. The thesis's citations into [Den22] are, by its own citation list, Chapters 1–3, 12, 14, 15 — it explicitly says on printed p. 3 (PDF p. 9, read from the image): *"As the resulting set of points of a rational Witt space turns out to not fulfill all desirable properties, see [Den22, Chapter 3 to 12 and 14], the set is modified in a controlled way."* That single pointer to "Chapter 3 to 12" is the closest the thesis comes to the dynamical half of [x-03], and it is a pointer, not a use.
* **The one adjacent passage, which does not anticipate.** Chapter 8, *Induced topology on X⁺(V)*, printed p. 85 (PDF p. 91), opening, read from the image:

  > "The aim of this chapter is to investigate a possible notion of convergence on X⁺(V)/G. For X the normalization of Spec(Z_p) in an algebraic closure of Q_p and G the Galois group, there is a bijection (see [Den22, Chapter 15]) with the space m_V♭. The latter can be endowed with a topology coming from the rank one valuation ring V. Here we explore what convergence properties this implies on the quotient X⁺(V)/G."

  and printed p. 86 (PDF p. 92), Definition 8.2 and Example 8.3, read from the image:

  > "**Definition 8.2** (Convergence in the quotient by a group action). … The sequence φ_nG ∈ C(R,S)/G converges to φG ∈ C(R,S)/G at r ∈ R if inf{|(φ_n ∘ g)(r) − (φ ∘ g̃)(r)| | g, g̃ ∈ G} converges to 0 for n → ∞. … Note that if the group acts with finite orbits the infimum becomes a minimum.
  > We give an example that convergence in the quotient by a group action is weaker than convergence in the quotient topology of the topology of pointwise convergence.
  > **Example 8.3.** … So the sequence converges in the quotient by the group action, see Definition 8.2. … So the sequence does not converge in the quotient topology of the topology of pointwise convergence."

  This is the only place in the thesis where a **quotient by a group action is shown to have a badly behaved topology**, and it is therefore the nearest structural echo of N2 anywhere in the document. It does **not** anticipate N2, for three separate reasons: the space is X⁺(V)/G (p-adic points modulo the absolute Galois group of K₀), not X₀ or a packet; the group is a Galois group acting with **finite** orbits (she says so explicitly), not a dense profinite accumulation; and the conclusion is that two *convergence notions* disagree, not that a space fails a separation axiom. I record it because a careful reader of both documents will notice it and should be told, in advance, why it is not the same phenomenon.

**Verdict: NOVEL w.r.t. this thesis.**

### 2.3 N3 — **(a) and (b) NOVEL w.r.t. thesis; (c) PARTIAL, with a framing obligation**

**(a) B_p = coker(lk_p) as the packet base.** The group Ẑ^×_(p)/p^Ẑ does not appear; `packet` = 0; `linking` = 0. The two occurrences of `Aut(` in the whole document are, from the OCR and confirmed in context, *"G = Aut(K|K₀) the group of automorphisms of K which fix K₀"* and the same phrase repeated a few lines later — the absolute Galois group, not Aut_ring(F̄_p) or Aut_group(F̄_p^×). **Does not touch.**

**(b) The Aut(C)-equivariance no-go.** `Aut(C)` = 0. `descent` = 0 (I also grepped `escent` to catch an OCR mangling: 0). `selection` = 0. There is no discussion of the choice of an embedding ι: μ(K̄) ↪ μ(C), no "choice of roots of unity", and no descent datum. Kucharczyk–Scholze is cited on printed pp. 1–3, 11, 13, 14 and is used **only** for Lemma 4.9, a commutative-algebra lifting lemma that Theorem D generalizes (printed p. 2, PDF p. 8, read from the image: *"we require a generalisation of a result in commutative algebra from Kucharczyk-Scholze [KS16, Lemma 4.9] and Deninger [Den22, Lemma 1.7]"*) — not for its descent discussion. **Does not touch.**

**(c) Transport of the local mod-p-additivity principle to C.** Here the thesis *is* relevant, in two ways, and one of them costs the Session-8 note a sentence.

First, the thesis is the fullest exposition in print of the principle N3(c) proposes to transport. §4.5 *Additivity modulo p*, printed p. 36 (PDF p. 42), read from the image:

> "To obtain A_inf(X) as functions on a subset of X_c^▽(V), Deninger imposes an additivity condition modulo p. This can be done in the uncompleted and completed case. The resulting subset in the uncompleted case turns out to be quite small (see [Den22, Proposition 15.8]). Hence, we will mostly work with the corresponding F_p-invariant subset of X_c^▽(V)."

with the definitions themselves, printed p. 37 (PDF p. 43), read from the image:

> "**Definition 4.17** (Additivity). Let X ∈ Schemes^aic and ε > 0. Denote the valuation of V by |·|. We define a subset of X_c^∨(V) by X_ε^∨(V) ≔ {A = (x, y, P̂ ∘ F_p^{−i}) ∈ X_c^∨(V) | |Ω_X(A)(r+s) − Ω_X(A)(r) − Ω_X(A)(s)| ≤ ε for all r, s ∈ Ô^♭_{x⤳y}}."
> "**4.5.2 Completed case.** An analogous F_p-invariant subset can be defined in the completed case, see [Den22, Definition 14.12]. **Definition 4.20** (Additivity). … X_ε^▽(V) ≔ {A = (x,y,P) ∈ X_c^▽(V) | |P(r+s) − P(r) − P(s)| ≤ ε for all r, s ∈ Ô^♭_{x⤳y}}."

and the selection of the threshold, printed p. 38 (PDF p. 44), read from the image:

> "For ε ≥ 1/p the sets X_ε^▽(V) are equal, see [Den22, Proposition 14.13]. Deninger is mostly interested in this set and we will hence give it an extra name. **Notation 4.23.** The set X_{1/p}^▽(V) is denoted by X⁺(V)."

I checked this attribution against the primary source: `fetched/x-03-…-arxiv-v4.pdf` does contain *"Definition 14.5. For any real number 0 < α < 1 define the G-invariant subset Y̌_α of X̌_c(o) … = {(x,y,P̌_y) ∈ X̌_c(o) | |P̌_y(r+s) − P̌_y(r) − P̌_y(s)| ≤ α for r, s ∈ Ô_{x̂,y}} … For α = 1/p we are looking at multiplicative maps P̌_y which mod p are also additive. Set Y̌ = Y̌_{1/p}"* (pdftotext extraction of the on-disk PDF, used here only to verify that Lutz's [Den22, Def. 14.5 / 14.12 / 14.13 / 14.15 / Thm 15.6] all exist with those numbers in arXiv:1807.06400v4 — they do). So the principle is **Deninger's, in the same paper**, and Lutz is its expositor and developer, not its originator.

Second — and this is the part the Session-8 note must absorb — **the thesis states the C-transport as an explicit, named, open desideratum.** Printed p. 2 (PDF p. 8), read from the image, verbatim:

> "Additivity modulo p can also be phrased as quasi-additivity, i.e. |φ(x + y) − φ(x) − φ(y)| ≤ 1/p for all x and y in the ring. This enhanced set of V-valued points is denoted by X⁺(V) and is endowed with a bijective Frobenius. It still contains all ordinary points, so the desirable properties mentioned earlier hold. **It would be very valuable to find an analogous modifications of W_rat(X)(C) but currently this is not known.**"

(The plural "modifications" after "an analogous" is in the original; quoted exactly.)

**What this does and does not do to N3(c).**
* It **does not** anticipate the claim. The thesis nowhere transports the condition to C, nowhere identifies what such a transport would select, and nowhere states a no-go. Its verdict on the transport is "not known", not "selects nothing canonical".
* It **does** anticipate the *idea of the transport as a live desideratum*, in print, from inside Deninger's own group, defended June 2025. Any wording in the Session-8 material to the effect that transporting the p-adic additivity condition to the archimedean side is an unnoticed or new proposal is **not sustainable** and must be replaced by a citation: Lutz 2025, printed p. 2. Positively, the same sentence is strong corroboration for the program's premise — the person best placed to have done it says, as of mid-2025, that it has not been done.
* It also supplies a useful independent confirmation for N3's broader framing: printed p. 1, *"Presently, there is no satisfactory answer for what these more general spaces of C-valued points … should be."*

**Verdict: PARTIAL on N3(c)** — anticipated as a desideratum, not as a result; severity of the required change: **MINOR** (one citation, one adjustment of framing).

### 2.4 N4 (Haar-averaging the packet base; measured trace formula for a continuum of periodic orbits) — **NOVEL w.r.t. thesis; does not touch**

`Haar` **0**, `measure` **0**, `trace` **0**, `foliat` **0**, `lamination` **0**, `leaf` **0**, `transverse` **0**, `equivariant` occurs 8 times and always means F_p- or G-equivariance of an algebraic map (e.g. printed p. 38, PDF p. 44, read from the image: *"These maps are multiplicative and F_p- and G-equivariant."*). The word `compact` occurs **once** in the entire thesis, and it is *"morphisms are quasi-compact by [Sta24, Tag 01WG]"* (OCR). There is no compact group, no invariant measure, no averaging, and no zeta/trace machinery of any kind. Note also that `zeta` occurs exactly three times, all three in the motivation paragraph on printed p. 1 (Hasse–Weil zeta functions, the Riemann zeta function) — the thesis proves nothing about a zeta function.

**Verdict: NOVEL w.r.t. this thesis.**

### 2.5 N5 (one-orbit-per-prime admissible cuts exist but are non-canonical) — **NOVEL w.r.t. thesis; does not touch**

`selection` 0, `cut` (as a noun of this kind) absent, no condition E, no admissibility class, no "one orbit per prime", no sub-dynamical system. The thesis's only "one per prime" structure is Deninger's decomposition of X⁺(V) into a generic and a special fibre for X affine — Definition 4.27 and §4.6, printed p. 40 (PDF p. 46), read from the image:

> "**Definition 4.27** (Generic fibre and special fibre of X⁺(V)). Let X be a scheme over Z_p in Schemes^aic. We call the preimage of (0) under pr_X the generic fiber of X⁺(V) and denote it by X⁺(V)_η. The preimage of (p) is called the special fiber and is denoted by X⁺(V)_s."
> "**4.6 Decomposition for X = Spec(O_K).** … **Lemma 4.28.** … Furthermore, the set is the disjoint union X⁺(V) = X⁺(V)_η ⊔̇ X⁺(V)_s with X⁺(V)_η = Hom_{cont,local,inj}(R̂♭, V♭), X⁺(V)_s = Hom_{cont,local}(κ, V♭) ≅ Hom_{cont,local,non-inj}(R̂♭, V♭)."

This is a two-piece decomposition of a p-adic point set by the characteristic of the residue field at a single fixed prime p — not a selection of one orbit per prime out of a family, and not a global object at all. It is not an ancestor of N5.

**Verdict: NOVEL w.r.t. this thesis.**

---

## 3. Structural finding: same paper, disjoint half

The bibliography (printed p. 91, PDF p. 97, read from the image) contains exactly **one** Deninger-authored entry as sole author and one as co-author, quoted verbatim:

> "[CD13] Joachim J. R. Cuntz and Christopher Deninger. *An alternative to Witt vectors.* arXiv: Number Theory (2013) (cit. on p. 36)."
> "[Den22] Christopher Deninger. *Dynamical systems for arithmetic schemes.* 2022. arXiv: 1807.06400 [math.DS] (cit. on pp. 1–4, 6, 7, 9–11, 13–15, 17, 19, 20, 22, 24, 26, 29, 31, 33–38, 51, 58, 59, 64, 77, 81–83, 85)."

So `[Den22]` **is** `[x-03]` — arXiv:1807.06400, the paper containing the packets, the suspension, the foliation, and the §6 question — and it is cited on about forty of the ninety-two printed pages. Yet every use of it, checked against her own text, lands in [Den22] Chapters 1–3 (Witt vectors, Witt spaces, Lemma 1.7 / Cor. 1.8 / Thm 1.5), Chapter 14 (Def. 14.5, Def. 14.12, Prop. 14.13, Prop. 14.15) and Chapter 15 (Thm 15.6, Prop. 15.8, "the map from [Den22, Chapter 15]"). Not one use lands in [Den22] §§4–13. The dissertation is the p-adic half of Deninger's paper carried forward; N1–N5 concern the archimedean/dynamical half, which the dissertation deliberately leaves alone (and, on printed p. 2, declares unsolved).

**Bibliography entries relevant to the program.**

| Entry | Present? | Use in the thesis |
|---|---|---|
| Deninger, *Dynamical systems for arithmetic schemes*, arXiv:1807.06400 (`[Den22]`, = `[x-03]`) | **YES** | The backbone; Chapters 1–3, 14, 15 only. Cited on printed pp. 1–4, 6, 7, 9–11, 13–15, 17, 19, 20, 22, 24, 26, 29, 31, 33–38, 51, 58, 59, 64, 77, 81–83, 85. |
| Deninger, arXiv:2301.11643 (`[x-06]`, the packets paper) | **NO** | — |
| Deninger, arXiv:2508.05329 (`[D25]`, which cites `[Lut25]`) | **NO** | Postdates the thesis. |
| Cuntz–Deninger, *An alternative to Witt vectors* (`[CD13]`) | **YES** | One use, printed p. 36 — the identification A_inf(X) = W_p(…) via the I-adic completion of the monoid ring. |
| Kucharczyk–Scholze, *Topological realisations of absolute Galois groups* (`[KS16]`) | **YES** | Printed pp. 1–3 (motivation: deformation retract of W_rat(X)(C); Steinberg relations fail) and pp. 11, 13, 14 (Lemma 4.9 only, generalized by her Theorem 2.20). No descent/roots-of-unity discussion. |
| Morishita (any work, incl. arXiv:2508.15971, *Knots and Primes*) | **NO** | `Morishita` = 0 occurrences. |
| ÁLKL / Álvarez López–Kordyukov–Leichtnam (arXiv:2402.06671 and the 2026 LNM volume) | **NO** | `Alvarez`, `Lopez`, `Kordyukov`, `Leichtnam` = 0 occurrences each. |
| Connes–Consani (any) | **NO** | `Connes`, `Consani` = 0 occurrences. |
| Kim–Morishita–Noda–Terashima | **NO** | 0 occurrences. |

The remaining 20 entries are Witt-vector, perfectoid, adic-space and commutative-algebra references: Almkvist, Atiyah–MacDonald, Bhatt–Iyengar–Ma, Bhatt–Morrow–Scholze, Fargues (2017), Fargues–Fontaine–Colmez, Fargues–Scholze, Flores–Weibel, Hazewinkel (×2), Huber, Kedlaya, Kummer, Lang, Liu, Matsumura, Scholze (*Perfectoid spaces*; *Étale cohomology of diamonds*), Schneider, Stacks Project, Scholze–Weinstein, Wedhorn. (All read from the bibliography page images, printed pp. 91–92 / PDF pp. 97–98.)

---

## 4. Grep hit table (OCR text; negative evidence only)

Run over the full 99-page OCR, case-insensitive. Counts are line-hits, not occurrence-counts, but the two coincide for every term with a small count, and every non-zero term was inspected.

| Term | Hits | What they are |
|---|---:|---|
| `packet` | **0** | — |
| `Hausdorff` | **0** | — |
| `Haar` | **0** | — |
| `trace` | **0** | — |
| `linking` | **0** | — |
| `descent` (and `escent`) | **0** | — |
| `Teichm` / `Teich` | **0** | — |
| `selection` | **0** | — |
| `foliat` / `lamination` / `leaf` / `transverse` | **0** | — |
| `cut` | **0** | — |
| `periodic` / `flow` / `suspension` / `solenoid` | **0** | — |
| `minimal set` / `uncountab` / `infinite-dimensional` | **0** | — |
| `monodromy` / `class field` / `one-parameter` | **0** | — |
| `measure` | **0** | — |
| `Morishita` / `Connes` / `Consani` / `Alvarez` / `Lopez` / `Kordyukov` / `Leichtnam` | **0** | — |
| `closure` | 41 | algebraic 25, integral 18, absolute 1, separable 1, topological 1 (density of a subfield in a tilt), Zariski "the closure of {x}" 1 |
| `orbit` | 19 | Frobenius orbits of classical points (printed p. 2); "acts with finite orbits" (Thm D and its lemmas); "unique orbit φG ∈ Hom_cont(R,S♭)/G" |
| `Frobenius` | 45 | the Witt-vector endomorphism F_n / F_p and its inversion by colimit; never an Artin symbol |
| `additiv` | 20 | additivity mod p (Deninger's Def. 14.5/14.12), quasi-additivity, additive Verschiebung |
| `Galois` | 17 | Gal(K\|K₀) and the quotient X⁺(V)/G |
| `Aut(` | 2 | both `Aut(K|K₀)` |
| `dynamic` | 1 | the bibliography title *Dynamical systems for arithmetic schemes* |
| `compact` | 1 | "quasi-compact by [Sta24, Tag 01WG]" |
| `archimed` | 2 | printed p. 1 (motivation); printed p. 83 ("non-archimedean field") |
| `C-valued` | 3 + 1 (`complex numbers`) | all four in the printed-p.-1/2 motivation |
| `zeta` | 3 | all three in the printed-p.-1 motivation |
| `dimension` | 5 | Krull dimension / "higher dimensional X" |
| `Fargues` / `diamond` / `untilt` / `perfectoid` | 18 / 30 / 23 / 34 | the actual subject matter |
| `Steinberg` | 1 | printed p. 1, reporting [KS16]'s deficit |

**Honest limit of this evidence.** Absence of a word from one 99-page document is decisive about *that document* and says nothing about the wider literature. It is offered here only to close the DQ-L item, not to strengthen any verdict in `novelty-O.md` or `novelty-F.md`.

---

## 5. Pages read (rendered page images, this session)

PDF pp. **7, 8, 9** (printed 1–3: Chapter 1, motivation, Theorems A–E, Overview) · **42, 43, 44** (printed 36–38: §4.5 Additivity modulo p, Defs. 4.17 and 4.20, Notation 4.23, Lemma 4.25) · **46** (printed 40: Def. 4.27, §4.6 Decomposition, Lemma 4.28) · **49** (printed 43: Chapter 5 opening, Theorem 5.1 = Theorem B) · **77** (printed 71: Theorem 6.42 = Theorem A) · **89** (printed 83: Theorem 7.24 = Theorem C) · **91, 92** (printed 85–86: Chapter 8 opening, Defs. 8.1 and 8.2, Example 8.3) · **97** (printed 91: Bibliography, first page). Thirteen page images.

Read via OCR only (locating, negative evidence, and sparse-page audit): PDF pp. 2, 4, 5, 6, 10, 17–22, 33, 34, 47, 48, 56, 78, 90, 93, 94, 98, 99, plus the whole-document greps in §4.

Cross-check source (pdftotext extraction, used only to verify that Lutz's `[Den22, …]` numbers exist in the primary): `fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf` — Definition 14.5, Definition 14.12, Proposition 14.13, Proposition 14.15, Theorem 15.6 all located at the cited numbers.

---

## 6. Consequences for the Session-8 material

1. **Close DQ-L / the standing-order-1 fetch item.** The Münster dissertation has been obtained and read. It anticipates none of N1–N5. `novelty-O.md` §7 item 3 and `novelty-F.md` §6 item 5 / §7 item 5 can be marked **resolved, negative**, and the three re-scan questions asked there answered: (a) no global E-condition — none of any kind; (b) no descent condition beyond Galois — the word does not occur; (c) no packet or orbit-closure statement — none.
2. **One framing change, N3(c), severity MINOR.** Cite Lutz 2025, printed p. 2: *"It would be very valuable to find an analogous modifications of W_rat(X)(C) but currently this is not known."* Do not present the transport of the mod-p-additivity condition to the archimedean side as an idea nobody has had; present it as a stated open desideratum of Deninger's group to which the note supplies a negative answer at the level of canonical selection.
3. **A corroboration worth keeping.** Lutz, printed p. 1: *"Presently, there is no satisfactory answer for what these more general spaces of C-valued points, denoted by Ẋ(C), should be."* Defended 5 June 2025, refereed by Deninger. This is the most recent independent statement on disk that the archimedean side of the program is open, and it is a fair thing to cite in the note's introduction.
4. **One adjacency to disclose, not to concede.** Lutz's Definition 8.2 / Example 8.3 (printed p. 86) show that convergence in a quotient by a group action is strictly weaker than convergence in the quotient topology. A reader may mistake this for a p-adic shadow of N2. It is not: finite Galois orbits, a different space, and a statement about two convergence notions rather than a separation axiom. Say so in a footnote rather than leaving it to be found.
