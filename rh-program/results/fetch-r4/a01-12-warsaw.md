# Round-4 ingest report — agent a01-12-warsaw (Session 18, 2026-09-09)

**File:** `fetched-r4/r4-01+12-walczak-conlon-langevin-foliations-geometry-dynamics-warsaw2000-WS2002-VOLUME.pdf`
(462 PDF pages). Proceedings *Foliations: Geometry and Dynamics* (Euroworkshop, Warsaw, May 29 – June 9, 2000),
ed. P. Walczak et al., World Scientific, Singapore, 2002, ISBN 981-02-4796-6.

**List items covered:** item 1 (P1) Cantwell–Conlon, *Endsets of exceptional leaves; a theorem of G. Duminy*,
pp. 225–261; item 12 (P3) Álvarez López–Kordyukov, *Distributional Betti numbers of transitive foliations of
codimension one*, pp. 159–183.

**Status:** COMPLETE — all five sections written (see end of file).

## §1. Identity verification

**The volume.** PDF p. 5 (copyright page): "FOLIATIONS: GEOMETRY AND DYNAMICS / Proceedings of the Euroworkshop /
Copyright © 2002 by World Scientific Publishing Co. Pte. Ltd. … ISBN 981-02-4796-6 / Printed in Singapore".
PDF p. 6 (Preface): Euroworkshop held in Warsaw at the Banach Centre and the Mathematical Institute of the Polish
Academy of Sciences, May 29 – June 9, 2000; "All the papers contained in this volume were refereed by experts."
Every article carries the running header "Proceedings of FOLIATIONS: GEOMETRY AND DYNAMICS, held in Warsaw,
May 29–June 9, 2000, ed. by Paweł WALCZAK et al., World Scientific, Singapore, 2002, pp. a–b" on its first page.
Contents on PDF pp. 8–9 (printed vii–viii). PDF is a pdfsam merge (2010), 462 pages, page size 409×610 pt.

**PDF-page ↔ printed-page offset: printed page = PDF page − 9** (printed 3 = PDF 12; printed 159 = PDF 168;
printed 225 = PDF 234). Checked at three points; uniform throughout the body.

**Text layer health.** PDF pp. 1–3 and 7, 10 are near-empty (title pages, blank pages) — that is content, not a
defect. From PDF p. 4 onward there is a usable OCR text layer; running text is clean, but mathematics is garbled
in the usual way (𝓕 → "J"/"3"/"?", ℰ → "£", superscripts flattened, "Duminy" OCR'd as "Dummy" in the Contents).
Every formula-bearing statement quoted in §3 below was verified by vision (pages rendered at 110 dpi).

### Item 1 — Cantwell–Conlon
- Printed on the file (PDF p. 234 header): "pp. 225–261"; title "ENDSETS OF EXCEPTIONAL LEAVES; A THEOREM OF
  G. DUMINY"; John Cantwell (St. Louis University), Lawrence Conlon (Washington University). Last page PDF p. 270
  = printed 261, ending with the references and "Received October 24, 2000, revised December 29, 2000."
- **PDF pages 234–270** (37 pages). Text layer: clean prose, garbled math.
- **Matches the list citation EXACTLY** (Cantwell–Conlon, Foliations: Geometry and Dynamics (Warsaw, 2000),
  World Scientific 2002). Hurder's reference [84] (r3s-29, text line 1550) gives "World Scientific Publishing
  Co. Inc., River Edge, N.J., 2002: 225–261" — same pages; the volume's own imprint says Singapore. No mismatch.

### Item 12 — Álvarez López–Kordyukov
- Printed on the file (PDF p. 168 header): "pp. 159–183"; title "DISTRIBUTIONAL BETTI NUMBERS OF TRANSITIVE
  FOLIATIONS OF CODIMENSION ONE"; Jesús A. Álvarez López (Santiago de Compostela), Yuri A. Kordyukov (Ufa State
  Aviation Technical University).
- **PDF pages 168–192** (25 pages). Text layer: clean prose, garbled math.
- **Matches the list citation EXACTLY.** (The list gives no page range; the printed one is 159–183.)

---

## §2. What the program asked for

**Item 1.** `results/c3-r/s16/qs4prime/adjudication.md` §4 item 4 (and §5): "S. Hurder, *Foliation
geometry/topology problem set* … §5, verbatim: '**Duminy's Theorem [84] shows that the semiproper leaves of K
must have a Cantor set of ends.**' and, as an open problem, '**PROBLEM 5.4. Show that every leaf of K has a
Cantor set of ends.**' (K = an exceptional minimal set of a codimension-one C² foliation of a compact
manifold.) … *Not read.* This is now the **highest-value fetch for C3-r**." §5 step 1: "get the exact statement,
its regularity hypothesis (C² is expected), and its definition of *semiproper*. Then check whether the
archimedean leaf of an S4′ object is semiproper — this is decidable from A-IV's structure (L̄ ∖ L ≠ ∅ and
L̄ ⊆ N) plus the definition." STATUS Session 17 queue item 3 asks the same ("Instruments: Duminy's theorem
(Cantwell–Conlon 2002 — SPONSOR FETCH; Hurder's problem set r3s-29 §5 quotes it), Hurder Problem 5.4 …").

**Item 12.** `results/c3-r/s14/novelty/adjudication.md` §4 item 6: "J. A. Álvarez López, Y. A. Kordyukov,
*Distributional Betti numbers of transitive foliations of codimension one* … — C5(a) residual (F/O; unchanged;
Kim 2017 now supplies the nearest print)." Claim C5(a) (§2 C5 there, and `s14/dqm-adjudication.md` §3 dated
block): "the mapping-torus trace without non-degeneracy" — the program's distributional identity
Tr(φ*|H̄ⁿ_F) = ℓ Σ_k tr((h*)^k) δ_{kℓ} on a mapping torus, proved with **no** non-degeneracy hypothesis (H4) on
Fix(ϕ^k); the question is whether any print anticipates the distributional trace, the trace-class statement, or
the dropping of H4. Kim 2017 was found to anticipate the cohomological core (Thms 2.1, 2.2, 3.2) but not the
distributional identity.

---

## §3. The answer from the source

### §3.1 Item 1 — Cantwell–Conlon, *Endsets of exceptional leaves; a theorem of G. Duminy*, pp. 225–261

All quotations vision-verified on PDF pp. 234–236 (printed 225–227) unless marked otherwise.

**Abstract (p. 225), verbatim:** "In 1977 Gerard Duminy proved that, if F is a semiproper leaf of a C²
codimension-one foliation 𝓕 of a compact n-manifold M and X is an exceptional local minimal set of 𝓕, then
the set ℰ^X(F) of ends of F asymptotic to X, if nonempty, is homeomorphic to a Cantor set. No proof of this
remarkable result has ever appeared, even in preprint form. Here, we offer a proof of our own."

**Standing hypotheses (§1, p. 225, first paragraph), verbatim:** "Let (M, 𝓕) be a transversely oriented,
C²-foliated manifold of codimension one, with M compact and oriented. We assume each component of ∂M, if any,
is a leaf of 𝓕. Remark that each leaf of 𝓕 is oriented."

So the printed hypotheses on the manifold are: **M compact; M oriented; 𝓕 transversely oriented (hence every
leaf oriented); boundary allowed, but every boundary component must be a leaf; codimension one; regularity
C².** Dimension n is arbitrary. Nothing is assumed about M being connected or closed beyond this.

**Definitions used (§1, p. 225), verbatim:**
- "Let U ⊆ M be an open, 𝓕-saturated subset and let X ⊂ U be an exceptional minimal set of 𝓕|U. As in [2] and
  elsewhere, we say that X is an exceptional LMS (local minimal set) of 𝓕." ([2] = Cantwell–Conlon,
  *Poincaré–Bendixson theory for leaves of codimension one*, Trans. AMS 265 (1981) 181–209.) "Exceptional
  minimal set" itself is not re-defined in the paper; it is the standard notion (a minimal set that is neither
  a compact leaf nor all of the ambient open set — Hurder's wording is "K is exceptional if K is not a compact
  leaf, and not an open set"). §2 (p. 228) uses the consequence: "Since X is exceptional, the closed subset X
  of F̄ meets each open, 𝓕-transverse arc, if at all, in an open subset of a Cantor set."
- "If F is a leaf of 𝓕, let ℰ(F) denote the space of ends of F and let ℰ^X(F) denote the subspace of ends
  that are asymptotic to X."
- **Semiproper (p. 225 bottom – p. 226 top), verbatim:** "Here, *semiproper* is taken to mean that at least
  one side of F is proper, so we include the case in which F is a proper leaf."
  (No further formalization is printed; "side of F is proper" is the standard Dippolito/Cantwell–Conlon
  notion: a side of F on which F does not accumulate on itself. The paper's §2 Lemma 2.1 uses exactly this:
  "the closure F̄ of F in M accumulates on F from at most one side".)

**Theorem 1.1 (Duminy), p. 225, verbatim:** "If the leaf F of 𝓕 is semiproper and if it accumulates on the
exceptional LMS X, then ℰ^X(F) is homeomorphic to the Cantor set."

**Corollary 1.2, p. 226, verbatim:** "If X is an exceptional minimal set of 𝓕 and if F ⊂ X is a semiproper
leaf, then ℰ(F) is homeomorphic to the Cantor set." Followed by: "Indeed, since X is minimal, ℰ^X(F) = ℰ(F)."

**Theorem 1.3, p. 226, verbatim** (the technical result from which 1.1 is deduced; notation set up in the two
preceding paragraphs): "If ε > 0, f, H, and α are as above and (a, b) is a component of (0, ε) ∖ F̄ then there
is an integer N ≥ 0 such that if σ is a loop on L′ based at 0⁺ then h_σ(f^k(b)) = f^k(b) all k ≥ N."
Setup, verbatim (p. 226): "let L be any semiproper leaf of 𝓕 that is approached by a possibly different
semiproper leaf F. By the transverse orientation, L has a positive and a negative side, and we assume
(reversing the transverse orientation, if necessary) that the positive side is a side on which F accumulates.
Let 0 ∈ L and let [0, ε] be a parametrized, 𝓕-transverse arc issuing from 0 on the positive side. If σ is a
loop on L based at 0, then h_σ will denote the holonomy in [0, ε] defined by σ. If H ⊂ L is a compact,
connected, nonseparating, oriented submanifold of codimension one (a 'handle'), then the homological
intersection number of the loop σ with H will be denoted by σ ⌢ H. Let L′ be L cut apart along the handle H.
… In Section 7 we show that there exists an ε > 0, a contraction f of [0, ε) to 0, a handle H, and curve α as
above with α ⌢ H = +1 and f = h_α."

**Theorem 1.4 (Duminy), p. 226, verbatim:** "If e ∈ ℰ^X(F), then every neighbourhood of e in F contains a
complete submanifold that spirals on L with juncture H. Consequently, e is a cluster point of ℰ^X(F) and this
set is a Cantor set." (Described as "the following theorem that was the basis of Duminy's original proof of
Theorem 1.1". "Spirals … with juncture H" is Definition 2.7, p. 230.)

**The conjectures printed right after (pp. 226–227), verbatim:** "It is natural to conjecture that, if F ⊂ X,
the requirement in Theorem 1.1 that F be semiproper can be dropped. This is true for Markov LMS [4] but is
unknown in general. A weaker conjecture would be that the generic leaf of an exceptional minimal set X have a
Cantor set of ends. Here generic can be taken either in the sense of [5] or [7]. It is not hard to show that
the generic leaf has one end or a Cantor set of ends." ([4] = Cantwell–Conlon, Publ. Mat. 33 (1989) 461–484;
[5] = Cantwell–Conlon, *Generic leaves*, CMH 73 (1998); [7] = Ghys, *Topologie des feuilles génériques*,
Ann. of Math. 141 (1995).) — This is exactly Hurder's Problem 5.4, printed here as the authors' own conjecture.

**Credit remark (p. 227), verbatim:** "Duminy deserves full credit for Theorem 1.1. The proof given here is
essentially one that we worked out about 15 years ago and we take responsibility for whatever shortcomings it
may have."

**Other stated results (text layer, spot-checked by vision where math-bearing):**
- Lemma 2.1 (p. 228): "The leaf L lies at finite level and the closure F̄ of F in M accumulates on F from at
  most one side." (Proof cites [1, Lemma 8.3.23] "No leaf at infinite level can have a proper side" and
  [1, Corollary 8.3.12]; [1] = Candel–Conlon, *Foliations I*.)
- Definition 2.7 (p. 230): the notion of a complete connected submanifold V ⊂ F "spiral[ing] onto L with
  juncture H" (three clauses; text layer, not re-verified by vision).
- Definition 3.1 / Theorem 3.2 (p. 231): "The holonomy of L is unbounded on any side that is approached by F."
  Remark following: by Dippolito's semi-stability theorem [6, Theorem 3] this is the expected input.
- Section headings: 3 "Unbounded holonomy" (p. 231); 4 "Some derivative estimates" (p. 232; Lemma 4.6 is "the
  'key lemma' of [1, p. 170]"); 5 "In the absence of a contraction"; 6 "Existence of the contraction";
  7 "A compactly supported cohomology class" (Prop. 7.16, Lemma 7.15); 8 "Problems" (p. 257); 9 "Examples of
  Markov minimal sets" (p. 258).
- §8 "Problems" (pp. 257–258), verbatim: Dippolito's question "Let X be an exceptional LMS and L ⊂ X a leaf.
  Is H_x(L, X) either trivial or infinite cyclic and generated by the germ of a contraction that is unique in
  a suitable neighborhood of x in C? Do exactly a countable infinity of leaves in X have H_x(L, X) ≅ ℤ and are
  all the semi-proper leaves among these?" Remark: "In this paper we have shown that a semiproper leave can
  not have trivial holonomy but in a subtle sense have not proven that H_x(L, X) = ℤ. For x not on a
  semi-proper leaf there are no results." Hector's question [11]: "If X is an exceptional LMS does X have
  finitely many semi-proper leaves?" And: "If X is an exceptional LMS, does it have Lebesgue measure |X| = 0?"
  (These are Hurder's Problems 5.1, 5.2, 5.3 respectively; "these are theorems for Markov LMS's [3].")

**Proof structure (one paragraph; the source says).** Theorem 1.1 and Theorem 1.4 are deduced in §2 from
Theorem 1.3. Given the semiproper leaf F accumulating on X, pick a semiproper leaf L ⊂ X on which F
accumulates (from L's nonproper side). Sections 3–7 produce, on the side of L approached by F, a
contraction f = h_α of a transverse arc [0, ε) to 0 realized as the holonomy of a loop α on L crossing a
"handle" H ⊂ L exactly once (§3: the holonomy of L is unbounded on the approached side — Theorem 3.2, via
Dippolito's semi-stability; §4: derivative estimates from the C² "key lemma" of Candel–Conlon p. 170; §§5–6:
existence of the contraction; §7: a compactly supported cohomology class, which yields the handle H and the
loop α with α ⌢ H = +1 and Theorem 1.3, i.e., the holonomy of every loop on L cut open along H eventually
fixes the iterates f^k(b) of a gap endpoint b ∈ F). Then (§2) the plaque-chain holonomy defines finite
covering maps π_i of L′ onto complete submanifolds B_i ⊂ F (Lemmas 2.2–2.3), which are pairwise disjoint
except along consecutive copies H_i of H (Lemma 2.4), so V_j = ∪_{i≥j} B_i is a fundamental neighborhood
system of an end e* ∈ ℰ^X(F) that is a cluster point of ℰ^X(F) (Cor. 2.6); since any neighborhood of any
e ∈ ℰ^X(F) contains such a V_j, every point of ℰ^X(F) is a cluster point, and a compact totally disconnected
metrizable perfect set is a Cantor set. Prop. 2.8 shows each π_i is a homeomorphism, giving Theorem 1.4
(spiraling).

**Comparison with Hurder's quotation (r3s-29 §5, text layer, lines 501–522).** Hurder's standing setup:
"Let K be an exceptional minimal set for a codimension one C²-foliation F of a compact n-manifold M." and
"Duminy's Theorem [84] shows that the semiproper leaves of K must have a Cantor set of ends."
- **Regularity and compactness agree:** C², codimension one, compact M — identical.
- **What Hurder omits:** the paper's standing hypotheses that M is **oriented** and 𝓕 is **transversely
  oriented**, and that any boundary components are leaves. (Both orientability conditions are removable by
  passing to a finite cover in the usual way, but the paper does not say so, and Hurder does not mention them.
  I infer, not the source.)
- **What Hurder's sentence is:** it is **Corollary 1.2** (minimal set, F ⊂ K), not Theorem 1.1. Theorem 1.1 is
  strictly more general: X need only be an exceptional **local** minimal set (minimal in an open saturated
  U ⊆ M), F need not lie in X (it need only accumulate on X), and the conclusion is about ℰ^X(F), the ends
  asymptotic to X — which is why the abstract adds "if nonempty" (Theorem 1.1 as printed has no such clause;
  the hypothesis "accumulates on X" makes it nonempty).
- **Hurder's "must have a Cantor set of ends"** matches Corollary 1.2's "ℰ(F) is homeomorphic to the Cantor
  set". No discrepancy in substance.
- **Hurder's Problem 5.4** ("every leaf of K has a Cantor set of ends") is the paper's first conjecture (p. 226:
  drop "semiproper" when F ⊂ X; "true for Markov LMS [4] but is unknown in general"). The paper also prints a
  weaker conjecture (generic leaf) and the remark that the generic leaf has "one end or a Cantor set of ends".
- **"Semiproper" in Hurder** is used without definition; the paper's definition ("at least one side of F is
  proper", proper leaves included) is what the program should carry.

**Plain-English reading for the §2 question (I infer).** The instrument the adjudication wanted is exactly as
Hurder quoted it, with two additions the program must carry: (i) the theorem's transverse-orientability and
orientability hypotheses; (ii) the precise definition of semiproper — "at least one side of F is proper", i.e.,
F does not accumulate on itself from at least one side (proper leaves count). For the archimedean-leaf test in
§5 step 1: if the S4′ leaf L lies in an exceptional (local) minimal set X of a C² transversely oriented
codimension-one foliation of a compact manifold and L has a proper side, Corollary 1.2 / Theorem 1.1 gives
ℰ(L) ≅ Cantor set, so L is not a plane. If L has no proper side (accumulates on itself from both sides) the
paper prints the case as an open conjecture (= Hurder 5.4), and in a lower regularity class (C¹) nothing is
claimed. The paper's Lemma 2.1 also gives, for free, that a semiproper leaf lies at finite level and that F̄
accumulates on F from at most one side.

### §3.2 Item 12 — Álvarez López–Kordyukov, *Distributional Betti numbers of transitive foliations of codimension one*, pp. 159–183

All displayed statements below vision-verified on PDF pp. 168–172 (printed 159–163). Received November 3, 2000.

**Abstract (p. 159), verbatim:** "Let 𝓕 be a transitive foliation of codimension one on a closed manifold M.
This means that there is an infinitesimal transformation X of (M, 𝓕) transverse to the leaves. The flow of X
induces an ℝ-action on the reduced leafwise cohomology H̄(𝓕). By using leafwise Hodge theory, the trace of this
action on each H̄^i(𝓕) can be defined as a distribution β^i_dis on ℝ, which is called distributional Betti
number because it is kind of a finite measure of the 'size' of H̄^i(𝓕). So the corresponding distributional
Euler characteristic, χ_dis(𝓕), is a distribution on ℝ too. This is relevant because H̄(𝓕) may be of infinite
dimension, even when the leaves are dense, and its Euler characteristic makes no sense in general. The
singularity at 0 of χ_dis(𝓕) is expressed in terms of the Connes' Λ-Euler characteristic, where Λ is the
holonomy invariant transverse measure of 𝓕 induced by the volume form dt on ℝ. Moreover the whole of χ_dis(𝓕)
is computed by showing a dynamical Lefschetz formula."

**Standing hypotheses and the spaces (§1, pp. 159–161), verbatim where quoted:**
- "Let M be a closed manifold and 𝓕 a smooth foliation on M of codimension one." 𝔛(M, 𝓕) ⊂ 𝔛(M) = the
  infinitesimal transformations of (M, 𝓕); 𝔛(𝓕) = the ideal of leafwise fields; for X ∈ 𝔛(M, 𝓕) the flow is
  X_t : (M, 𝓕) → (M, 𝓕).
- **Transitive (p. 160):** "The foliation 𝓕 is called *transitive* when T_xM = {X(x) | X ∈ 𝔛(M, 𝓕)}. … we get
  that 𝓕 is transitive if and only if there is some X ∈ 𝔛(M, 𝓕) transverse to the leaves; i.e., T_xM =
  ℝ X(x) ⊕ T_x𝓕 for all x ∈ M. Then the orbits of X_t, t ∈ ℝ, are non-singular and transverse to the leaves.
  Note that 𝔛(M, 𝓕)/𝔛(𝓕) ≅ ℝ (1) if the leaves are dense, which is the most interesting case."
- **Leafwise complex and reduced cohomology (p. 160):** "The leafwise de Rham complex of 𝓕, (Ω(𝓕), d_𝓕), is
  the restriction of the de Rham complex of M to the leaves; i.e., it is given by the smooth sections of the
  exterior vector bundle ⋀ T𝓕* over M. Its cohomology is called the *leafwise cohomology* of 𝓕, and will be
  denoted by H(𝓕). Moreover (Ω(𝓕), d_𝓕) is a topological complex with the C^∞ topology, and H(𝓕) is a
  topological vector space with the induced topology. It is well known that H(𝓕) may not be Hausdorff [14]
  [Haefliger 1980]. So it is interesting to consider its quotient over the closure of the trivial subspace,
  which is called the *reduced leafwise cohomology* of 𝓕, and is denoted by H̄(𝓕) in this paper."
- **Metric (p. 160):** "Consider a Riemannian metric on M such that X is of norm one and orthogonal to the
  leaves. So all flow orbits are geodesics of speed one orthogonal to the leaves. This is what is called a
  *bundle-like* metric on M." δ_𝓕, Δ_𝓕 = leafwise coderivative and Laplacian on Ω(𝓕); "The kernel 𝓗(𝓕) of
  Δ_𝓕 is the space of harmonic forms on the leaves that are smooth on M." Δ̄_𝓕 = closure of Δ_𝓕 in L²Ω(𝓕),
  self-adjoint since the metric is bundle-like [5, 16]; Π̄ = orthogonal projection L²Ω(𝓕) → ker Δ̄_𝓕; "By [3],
  Π̄ has the restriction Π : Ω(𝓕) → 𝓗(𝓕), and there is an orthogonal decomposition Ω(𝓕) = 𝓗(𝓕) ⊕ (im d_𝓕)‾ ⊕
  (im δ_𝓕)‾, which can be called a leafwise Hodge decomposition. In particular, the inclusion 𝓗(𝓕) ⊂ ker d_𝓕
  induces an isomorphism 𝓗(𝓕) ≅ H̄(𝓕) (2), whose inverse is induced by the orthogonal projection Π : ker d_𝓕
  → 𝓗(𝓕)." ([3] = Álvarez López–Kordyukov, *Long time behaviour of leafwise heat flow for Riemannian
  foliations*, dg-ga/9612010, to appear Compositio.)
- **The operator (p. 161):** "For any function f ∈ C_c^∞(ℝ), define an operator A_f on Ω(𝓕) by the formula
  A_f = Π ∘ ∫_ℝ X_t^* · f(t) dt ∘ Π, and let A_f^{(i)} denote its restriction to Ω^i(𝓕)."

**Theorem 1.1 (p. 161), verbatim:** "For any function f ∈ C_c^∞(ℝ), the operator A_f is of trace class, and
the functional f ↦ Tr(A_f^{(i)}) defines a distribution β^i_dis(𝓕) on ℝ for each i."
Then: "The distributions β^i_dis(𝓕) depend only on 𝓕 and the class of X in 𝔛(M, 𝓕)/𝔛(𝓕) (Lemma 2.3); thus,
when the leaves are dense, they depend only on 𝓕 up to linear isomorphisms of ℝ by (1)."
**No hypothesis on closed orbits enters Theorem 1.1.** (Proof: §2.2–2.3 and §3.1, via Proposition 3.1 — A_f
is a smoothing operator whose kernel depends continuously on f; the operator-norm estimate (8) is "given in
our work [3] with more generality".)

**Definition (p. 162), verbatim:** "the germs at 0 of the distributions β^i_dis(𝓕) could be called
distributional Betti numbers. But, for the sake of simplicity, the whole distributions β^i_dis(𝓕) will be
called the *distributional Betti numbers* of 𝓕, even though they should be better considered as Lefschetz
numbers away from 0. We also define the *distributional Euler characteristic* of 𝓕 by the formula
χ_dis(𝓕) = Σ_i (−1)^i β^i_dis(𝓕)."

**Theorem 1.2 (p. 162), verbatim:** "In some neighbourhood of 0 in ℝ, we have χ_dis(𝓕) = χ_Λ(𝓕) · δ_0, where
δ_0 denotes the Dirac measure at 0." (χ_Λ = Connes' Λ-Euler characteristic, Λ = the transverse Riemannian
volume element = dt on ℝ; "The similar result was obtained in [18] [Lazarov, GAFA 10 (2000)] when the flow is
isometric.")

**Simple orbits (p. 162), verbatim:** "Recall that a closed orbit c of length l of the flow X_t on (M, 𝓕) is
called *simple* when det(id − X_l^* : T_x𝓕* → T_x𝓕*) ≠ 0 for any x ∈ c. The following theorem proves, for
this type of foliations, a conjecture stated by Deninger in [10]. Under some additional assumptions, it was
proved in [11, 18]." ([10] = Deninger, Doc. Math. ICM98 extra vol. 163–186; [11] = "C. Deninger and
W. Singhof, A note on dynamical trace formulas, manuscript, 2000" — this is round-4 fetch item 5; [18] =
Lazarov.)

**Theorem 1.3 (p. 162), verbatim:** "Assume that all closed orbits of the flow X_t on (M, 𝓕) are simple. Then
we have χ_dis(𝓕) = Σ_c l(c) Σ_{k=1}^∞ sign det(id − X_{l(c)}^* : T_x𝓕* → T_x𝓕*) · δ_{kl(c)} on ℝ_+, where c
runs over all primitive closed orbits of the flow X_t, l(c) denotes the length of c, and x is an arbitrary
point of c." "Of course, in Theorem 1.3, a symmetric formula for χ_dis(𝓕) also holds in ℝ_−."
[Vision note: the sign det inside the sum is printed with X_{l(c)}^*, i.e., the return map over one period of
the primitive orbit, and the same sign is used for every k — the text is as printed; whether the authors
intend X_{kl(c)}^* is not resolved on the page. Proof (§6, p. 181) computes the contribution of an orbit of
period s_0 = kl as "sign det(id − X_{kl}^* : T_{(x,v)}(W × {v}) → T_{(x,v)}(W × {v}))", i.e., with k.]

**Corollaries (p. 163), verbatim:**
- Corollary 1.4: "If dim 𝓗(𝓕) < ∞, then χ_dis(𝓕), χ_Λ(𝓕) and χ(𝓕) vanish."
- Corollary 1.5: "Assume that all closed orbits of the flow X_t on (M, 𝓕) are simple. If dim 𝓗(𝓕) < ∞,
  then, for any l ∈ ℝ, Σ_c (1/μ(c)) sign det(id − X_l^* : T_x𝓕* → T_x𝓕*) = 0, where c runs over all closed
  orbits of the flow X_t of period l, μ(c) denotes the multiplicity of c, and x ∈ c is an arbitrary point."
- Corollary 1.6: "Assume that 𝓕 is of dimension two with dense leaves. Then the singular part of β^i_dis(𝓕)
  around 0 is β^i_Λ(𝓕) · δ_0 for each degree i." Question 1.7: "For each degree i, is it true that the singular
  part of β^i_dis(𝓕) around 0 is β^i_Λ(𝓕) · δ_0?"
- Corollary 1.8 (p. 164, text layer): χ_dis(𝓕) = δ_0 · ∫_M Pf(R_L/2π) ∧ Λ around 0; for dim 𝓕 = 2,
  χ_dis(𝓕) = δ_0 · (1/2π) ∫_M K_𝓕(x) ω_M(x) around 0.

**Other statements (text layer):** Theorem 5.1 (p. 179), "The distribution χ_dis(𝓕) is supported in the set of
all s ∈ ℝ such that X_s has a fixed point in M." — proved with **no** simplicity hypothesis (localization).
§6 (pp. 180–181) proves Theorem 1.3 from Theorem 5.1 by a heat-kernel computation near each closed orbit;
simplicity is used exactly once: "there are no other fixed points of elements of Γ ∩ (s_0 + U) in some open
neighbourhood W of x in L because all X-orbits are simple", after which "by [7, 13]" (Atiyah–Bott, Gilkey)
the local integral converges to the sign of the determinant. Closing remarks p. 164 (text layer, prose):
"This type of foliations are just Lie foliations of codimension one. So this is a particular case of our work
on distributional Betti numbers for arbitrary Lie foliations [4] [preprint 2000; the published form is the
Lefschetz-distribution paper the adjudicator opened as math/0703753]. … moreover the codimension one case is
relevant for Deninger's approach to Riemann Hypothesis [10, 11]."

**Does it settle what s14 novelty §4 item 6 asks? (Plain-English reading.)**
- *The source says:* the trace-class property and the distributional trace on reduced leafwise cohomology
  (Theorem 1.1) and the localization to periods with fixed points (Theorem 5.1) are proved for **every**
  transitive codimension-one foliation of a closed manifold with **no** hypothesis on the closed orbits. The
  explicit Lefschetz formula (Theorem 1.3) is proved **only under "all closed orbits simple"**, which in the
  mapping-torus case is exactly the non-degeneracy hypothesis H4 (det(id − (h^k)^* on T_x S*) ≠ 0 at fixed
  points of h^k).
- *The source does not contain:* any treatment of the suspension / mapping torus S × ℝ/(x, t) ∼ (h(x), t + ℓ),
  the identity ℓ Σ_k tr((h^*)^k) δ_{kℓ}, or any coefficient reading (Fuller index) at a degenerate or continuum
  fixed-point set. "Suspension", "mapping torus", "fibration", "Fuller" do not occur in the text layer.
- *I infer:* for the fiber foliation of a mapping torus with the suspension field X (which is transitive; a
  bundle-like metric with |X| = 1 exists by choosing a path of fiber metrics from g to h^*g), ALK Theorem 1.1
  already gives, in print and without H4, the trace-class and distribution claims of C5(a) — the trace of
  A_f on 𝓗(𝓕) ≅ C^∞_h(ℝ, H(S)) then evaluates to ℓ Σ_k f(kℓ) tr((h^*)^k) by a one-line computation the paper
  does not perform. So the printed anticipation of C5(a) improves from "Kim 2017 (cohomological core only)" to
  "Kim 2017 (spectrum) + ALK 2002 Theorem 1.1 (trace class / distribution, general, no H4)"; what remains the
  program's is the explicit mapping-torus evaluation, the statement that the δ_{kℓ}-coefficient is the total
  fixed-point index (Fuller) rather than the simple-orbit sign sum, and the reading at a continuum of fixed
  points. The printed Lefschetz formula (Thm 1.3) is, as the adjudication expected, under H4 — it is the
  Deninger conjecture from [10], and the paper says Deninger–Singhof [11] and Lazarov [18] proved it earlier
  "under some additional assumptions". **Recommend (not enacted): the s14 novelty record for C5(a) should add
  ALK 2002 Theorem 1.1 and Theorem 5.1 as printed relatives; the verdict PARTIAL stands.**

---

## §4. Anything else in the source a future session should know (volume table of contents)

Contents as printed on pp. vii–viii (PDF pp. 8–9); OCR names normalized ("Dummy" → Duminy, "Endests" →
Endsets, "Haefiiger" → Haefliger). Printed page = PDF page − 9.

SURVEY ARTICLES
- T. Asuke: Some results on secondary characteristic classes of transversely holomorphic foliations: 3–16
- H. Colman: LS-categories for foliated manifolds: 17–28
- S. Hurder: Dynamics and the Godbillon–Vey class: a history and survey: 29–60 (PDF 38–69) — the same author
  as the problem set r3s-29; likely restates the exceptional-minimal-set problems with references.
- R. Langevin: Similarity and conformal geometry of foliations: 61–74
- Y. Mitsumatsu: Foliations and contact structures on 3-manifolds: 75–125 (lecture notes)
- H. Moriyoshi: Operator algebras and the index theorem on foliated manifolds: 127–155 (lecture notes)

RESEARCH PAPERS
- J. Álvarez López and Y. Kordyukov: Distributional Betti numbers of transitive foliations of codimension one:
  159–183 (PDF 168–192) — item 12.
- S. Aranson and E. Zhuzhoma: Circle at infinity influences on the smoothness of surface flows: 185–196
- A. Biś and P. Walczak: Entropies of hyperbolic groups and some foliated spaces: 197–211
- M. Brittenham: Tautly foliated 3-manifolds with no R-covered foliations: 213–224
- J. Cantwell and L. Conlon: Endsets of exceptional leaves; a theorem of G. Duminy: 225–261 (PDF 234–270) —
  item 1.
- M. Frydrych and J. Kalina: Some remarks on partially holomorphic foliations: 263–273
- A. Haefliger: Foliations and compactly generated pseudogroups: 275–295 (PDF 284–304) — the standard
  reference for compactly generated pseudogroups; relevant if the program ever needs the holonomy pseudogroup
  of a compact lamination in Haefliger's vocabulary.
- J. Heitsch: Traces and invariants for non-compact manifolds: 297–314
- M. Hilsum: Hilbert modules of foliated manifolds with boundary: 315–332
- V. Kaimanovich: Non-Euclidean affine laminations: 333–349 (PDF 342–358) — laminations by hyperbolic
  surfaces with affine structure; may bear on the compact-lamination half of Q-S4⁗.
- R. Langevin and P. Walczak: Transverse Lusternik–Schnirelmann category and non-proper leaves: 351–354
- V. Medvedev and E. Zhuzhoma: Structurally stable diffeomorphisms have no codimension one Plykin attractors
  on 3-manifolds: 355–370
- T. Mizutani: On exact Poisson manifolds of dimension 3: 371–386
- Y. Nakae: Foliation cones corresponding to some pretzel links: 387–402
- T. Noda and T. Tsuboi: Regular projectively Anosov flows without compact leaves: 403–419
- T. Tsuboi: On the perfectness of groups of diffeomorphisms of the interval tangent to the identity at the
  endpoints: 421–440
- R. Wolak: Basic distribution for singular Riemannian foliations: 441–447
- List of participants: 449; Program: 451.

Other one-liners:
- Cantwell–Conlon §9 (pp. 258–261) gives a general construction realizing any subshift of finite type as the
  holonomy of a Markov exceptional minimal set of a codimension-one foliation — a source of examples if the
  program ever needs an exceptional minimal set with prescribed holonomy.
- Cantwell–Conlon's bibliography item [1] cites Candel–Conlon *Foliations I* (fetched as r4-15a) for
  Lemma 8.3.23 ("No leaf at infinite level can have a proper side"), Corollary 8.3.12 (finite-level structure
  of F̄), the "key lemma" p. 170, and §8.4 (spiraling).
- ALK's reference [11] "Deninger and Singhof, A note on dynamical trace formulas, manuscript, 2000" is fetch
  item 5 (Contemp. Math. 290); ALK Theorem 1.3 is stated as proving Deninger's [10] conjecture in general for
  transitive codimension-one foliations, with [11, 18] as the earlier partial cases.

---

## §5. Caveats for `corpus-routing.md`

- `r4-01+12` — the Contents page OCR reads "J. Cantwell and L. Conlon: Endests of exceptional leaves; a
  theorem of G. Dummy"; grep for "Duminy" in the text layer misses the Contents. Fix: grep "Dummy|Duminy", or
  go by PDF page (234–270).
- `r4-01+12` — script letters are lost in the text layer: 𝓕 appears as "J", "3", "7", "?", "𝓕|U" as "$\U";
  ℰ^X(F) as "£ X ( F )" or "EX(F)"; H̄ as "H"; the bar distinguishing H̄(𝓕) (reduced) from H(𝓕) (unreduced) is
  invisible in the text layer. Fix: vision-verify every statement in which reduced vs. unreduced cohomology
  or the endset matters (done here for pp. 225–227 and 159–163).
- `r4-01+12` — printed page = PDF page − 9 throughout the body; PDF pp. 1–3, 7, 10 are title/blank pages
  (empty text layer is not a defect).
- `r4-01+12` — ALK Theorem 1.3 as printed has X_{l(c)}^* (one period) inside the k-sum while the proof (p. 181)
  uses X_{kl}^*; quote as printed and flag, do not silently correct.

**Status: COMPLETE (2026-09-09).**
