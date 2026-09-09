# C3-r — the double-cover lemma (rider R1): check-O (Opus 5)

Dual-check per `results/c3-r/s20/dc/BRIEF.md` (standing orders 5, 6, 7); binding text
`results/c3-r/s20/insights-digest.md` §E. Written independently; `check-F.md` was NOT opened
(verified: no read of that path occurs in this stream). This is a check of a **transfer lemma**
only — no construction, and none is licensed (standing order 6). U.S. English. No network.

**Machine clock at start:** Thu Sep 10 04:30 IST 2026. Written in chunks, appended as drafted.

**Convention.** Downstairs objects carry no tilde; upstairs objects carry one. "Printed" means I
rendered the page and read it by vision in this stream; every such page is listed in the honesty
note with its PDF folio, its printed folio as it appears in the running head, and the offset.

---

## §1. The lemma, stated

**Hypotheses** (exactly as digest §E lists them; nothing added, nothing dropped).

1. **Downstairs.** (M, 𝓕, φ) in the contract's manifold case with the orientation clauses
   REMOVED — M a closed 3-manifold, 𝓕 a C² codimension-one foliation, φ a C¹ foliated flow
   satisfying (i)–(iv) and clause (0) — so that (D1)–(D6) hold; in particular **(D3)** (no compact
   leaf in N), **(D4)** (L ≅ D: Reading (iii)′, χ = +1), **(D5)** (K ⊂ L̄ an exceptional minimal
   set of 𝓕, via Theorem O-5's clause-(iii) argument).
2. **The cover.** A finite covering π : M̃ → M, at most 4-fold, with M̃ oriented and
   𝓕̃ = π*𝓕 transversely oriented.
3. **Regularity upstairs.** 𝓕̃ is C², codimension one, on a closed oriented 3-manifold with no
   boundary — so that Duminy's standing hypotheses (Warsaw p. 225) hold upstairs.
4. **Accumulation upstairs.** "Accumulates on X" in Warsaw's sense holds upstairs for L̃ and K̃
   (adjudication §1.4's reading of the hypothesis, itself flagged there as the adjudicator's
   inference for the one-ended case).
5. **The instrument.** Duminy's Theorem 1.1 upstairs, with the abstract's "if nonempty" clause
   disposed of exactly as in adjudication §1.4/D8 (the single end of L̃ ≅ D is asymptotic to K̃).
6. **Not needed.** The flow; clauses (i)–(ii) upstairs; the level of L; the Markov property of K.

**Conclusion (as digest §E states it).** For the contract object with the orientation clauses
removed, L is not semiproper — i.e. (S) PRINTED-NO holds without rider R1 — because a proper side
of L would lift to a proper side of L̃ ≅ D in a transversely oriented C² foliation of a closed
oriented 3-manifold, where L̃ accumulates on the exceptional minimal set K̃ ⊂ closure(L̃), and
Duminy's Theorem 1.1 would give ℰ^{K̃}(L̃) a Cantor set against L̃'s single end.

**Well-formedness note, carried into §2(i) and §4 and binding on the ledger wording.** Candel–Conlon I
p. 133 (printed, vision) says of semiproperness: *"This condition only makes sense for
transversely–orientable foliations of codimension 1 and is not meant to exclude the possibility that
the leaf is proper."* Under hypothesis 1 the orientation clauses are removed, so the word
"semiproper" in the conclusion above is, on the printed source's own terms, not defined downstairs.
The lemma's conclusion must therefore be carried in the orientation-free form the same page supplies
in the proof of Lemma 5.3.2:

> **(S′)** There exist x₀ ∈ L and a transverse arc J out of x₀ with J ∩ L = {x₀}.

(S′) needs no orientation; it coincides with "semiproper" whenever 𝓕 is transversely oriented
(Lemma 5.3.2, p. 133: *"A leaf L is semiproper if and only if it is a border leaf of some
W ∈ 𝒪(𝓕)"*, with the proof's *"if L is semiproper, let J be a transverse arc out of a point
x₀ ∈ L that meets L only in {x₀}"*); and (S′) is exactly what the sketch's arc argument lifts.
**What the lemma proves is ¬(S′).** This is a repair of the statement, not an added hypothesis.

---

## §2. The steps (a)–(i)

### (a) The cover exists with the stated properties, and 𝓕̃ is C² codimension one on a closed oriented M̃ — **CLOSES**

*Printed sentence (Candel–Conlon I, §3.5 "Orientation Covers", printed pp. 94–95 = PDF 101–102,
offset +7; §3.5 read at the page in this stream — nobody had read it before).*

> **Proposition 3.5.1.** *Let* (M, 𝓕) *be a foliated manifold, M connected. If M is nonorientable
> and/or 𝓕 is not transversely orientable, there is a connected covering space (either 2–fold or
> 4–fold)* π : M̃ → M *such that M̃ is orientable and the lifted foliation 𝓕̃ is transversely
> orientable. In this case, the leaves of 𝓕̃ are all orientable.*

That is hypothesis 2 verbatim, with "at most 4-fold" correct: if M is already orientable and 𝓕
already transversely orientable, take π = id (1-fold); otherwise the printed degree is 2 or 4.

Four riders, each a one-line argument, none appealing to "standard":

- **M connected.** Proposition 3.5.1 requires it. If (H0)-manifold's M is not assumed connected,
  replace M by the component M₀ containing L: M₀ is itself a closed 3-manifold, L̄ ⊆ M₀ (L̄ is
  connected and meets M₀), and K ⊆ L̄ ⊆ M₀ by (D5), so every object the lemma touches lives in M₀.
- **M̃ closed.** π is a k-fold covering with k ≤ 4 and M is compact: cover M by finitely many
  evenly-covered open sets U₁,…,U_m with compact K_j ⊆ U_j still covering M; then M̃ is covered by
  the finitely many compact sets (π|sheet)⁻¹(K_j), so M̃ is compact. ∂M̃ = π⁻¹(∂M) = ∅.
- **M̃ oriented, 𝓕̃ transversely oriented.** The Proposition gives *orientable* and *transversely
  orientable*; M̃ is connected, so an orientation of TM̃ and an orientation of ν(𝓕̃) each exist and
  are choices, not further hypotheses. Duminy's *"Remark that each leaf of 𝓕 is oriented"* is the
  Proposition's own last sentence, whose printed proof is on p. 95: *"A loop on a leaf L must
  preserve both the orientation of T(M̃) and of ν(𝓕̃), hence preserves the orientation of T(L)."*
- **C², codimension one.** Printed on p. 94, immediately above the Proposition: *"The differentiable
  structure of M is lifted to a differentiable structure of M̃, relative to which the covering
  projection is locally a diffeomorphism. … If there is a foliation 𝓕 on M (of arbitrary
  codimension), π lifts 𝓕 to a well-defined foliation 𝓕̃ = π*(𝓕)."* Since π is a local
  diffeomorphism, a foliated atlas of 𝓕 restricted to evenly-covered charts pulls back sheet by
  sheet to a foliated atlas of 𝓕̃ **with the same transition maps**; hence 𝓕̃ has the same
  differentiability class C² and the same codimension one.

### (b) The components of π⁻¹(L) are homeomorphic copies of L — **CLOSES**

Argument written out (the covering-space fact used is named and proved, not cited as known).

Let L̃ be a component of π⁻¹(L) — equivalently, since π maps each leaf of 𝓕̃ into a leaf of 𝓕, a
leaf of 𝓕̃ lying over L. Give L and L̃ their leaf topologies.

1. **π|L̃ is a local homeomorphism.** For x ∈ L choose a foliated chart U of 𝓕 at x contained in an
   evenly-covered open set (foliated charts form a basis, so this is possible). Then
   π⁻¹(U) = ⨆ᵢ Uᵢ with π|Uᵢ : Uᵢ → U a homeomorphism, each Uᵢ a foliated chart of 𝓕̃ whose plaques
   map homeomorphically onto plaques of U. Hence π carries plaques to plaques bijectively.
2. **π(L̃) is open in L.** Immediate from 1.
3. **π(L̃) is closed in L.** Let x ∈ L be in the leaf-topology closure of π(L̃), and let P be the
   plaque of x in U as in 1. Some point of π(L̃) lies in P; its preimage in L̃ lies in one of the
   plaques (π|Uᵢ)⁻¹(P), and that plaque, being connected and meeting the leaf L̃, is contained in
   L̃. Since π maps that plaque onto P ∋ x, we get x ∈ π(L̃).
4. **π|L̃ : L̃ → L is a covering map.** L is connected, so 2 + 3 give surjectivity; and 1 exhibits
   each plaque P ⊆ L as evenly covered by the plaques of (π|L̃)⁻¹(P).
5. **L is simply connected.** (D4): L ≅ D.
6. A covering map onto a simply connected, locally path-connected base, from a connected total
   space, is a homeomorphism. Hence π|L̃ : L̃ → L is a homeomorphism, and **L̃ ≅ D**.

(Nothing here uses orientability, the flow, or C².)

### (c) A proper side lifts — **CLOSES**

Take (S′) downstairs: x₀ ∈ L and a transverse arc J out of x₀ with J ∩ L = {x₀}.
Note first that any sub-arc of J out of x₀ still meets L only in {x₀}, so J may be shrunk freely.

Pick x̃₀ ∈ L̃ over x₀. π is a local homeomorphism, so there is an open Ṽ ∋ x̃₀ carried
homeomorphically onto an open V ∋ x₀. Shrink J so that J ⊆ V and put J̃ := (π|Ṽ)⁻¹(J). Then:

- **J̃ is a transverse arc out of x̃₀.** π|Ṽ is a diffeomorphism carrying 𝓕̃|Ṽ to 𝓕|V, so it
  carries arcs transverse to 𝓕 back to arcs transverse to 𝓕̃.
- **J̃ ∩ L̃ = {x̃₀}.** J̃ ∩ L̃ ⊆ J̃ ∩ π⁻¹(L) = (π|Ṽ)⁻¹(J ∩ L) = (π|Ṽ)⁻¹({x₀}) = {x̃₀}; and
  x̃₀ ∈ J̃ ∩ L̃.

So (S′) holds upstairs. Upstairs 𝓕̃ **is** transversely oriented, so there the printed vocabulary is
available and (S′) is exactly semiproperness: Lemma 5.3.2's proof (p. 133) turns the arc into the
open saturated set — *"The 𝓕–saturation W of int J is an element of 𝒪(𝓕) and L ⊆ δW"* — and
Lemma 5.3.2 then reads **L̃ is semiproper**. (The direction used is (S) downstairs ⟹ (S) upstairs;
that is the direction (h) needs.)

### (d) closure(L̃) ∩ π⁻¹(K) is nonempty, compact and 𝓕̃-saturated — **CLOSES**

- **Compact.** closure(L̃) is closed in the compact M̃ (a), hence compact; π⁻¹(K) is closed (K
  closed, π continuous); the intersection is a closed subset of a compact set.
- **π⁻¹(K) is 𝓕̃-saturated.** π maps each leaf of 𝓕̃ into a leaf of 𝓕 (it carries plaques to
  plaques, (b)1). If x̃ ∈ π⁻¹(K) then the leaf of x̃ maps into the leaf of π(x̃), which lies in K
  because K is 𝓕-saturated ((D5): K is a minimal set of 𝓕).
- **closure(L̃) is 𝓕̃-saturated.** Let ỹ ∈ closure(L̃) and let z̃ lie in the same plaque of a
  foliated chart Ũ ≅ D² × D¹ as ỹ. Points of L̃ converging to ỹ eventually lie in Ũ, hence in
  plaques of Ũ, and each such plaque lies wholly in L̃; the corresponding points of those plaques
  with the D²-coordinate of z̃ converge to z̃, so z̃ ∈ closure(L̃). Chaining plaques along a leaf
  gives that the whole leaf of ỹ lies in closure(L̃).
- **Nonempty.** π|L̃ : L̃ → L is onto (b), so π(closure(L̃)) ⊇ L; π(closure(L̃)) is a continuous
  image of a compact set, hence compact, hence closed in M; so π(closure(L̃)) ⊇ closure(L) = L̄.
  By (D5), K ⊆ L̄. Hence every y ∈ K has a preimage x̃ ∈ closure(L̃), and x̃ ∈ closure(L̃) ∩ π⁻¹(K).

### (e) A minimal set K̃ exists in it; it is not a compact leaf; it is not open — **CLOSES**

**Existence (Zorn, exactly as in Theorem O-5).** `refute-adjudication.md` §4, verbatim: *"L̄ is a
nonempty compact saturated set, so it contains a minimal set K (Zorn; chains of nonempty compact
saturated sets have nonempty compact saturated intersections)."* Apply the same to the nonempty
compact 𝓕̃-saturated set closure(L̃) ∩ π⁻¹(K) of (d): it contains a minimal set **K̃** of 𝓕̃, and
K̃ ⊆ closure(L̃) with π(K̃) ⊆ K.

**K̃ is not a compact leaf.** Suppose K̃ were a compact leaf of 𝓕̃, and let L′ be the leaf of 𝓕
containing π(K̃). By (b)1, π|K̃ : K̃ → L′ is a local homeomorphism in the leaf topologies, so π(K̃)
is open in L′; it is also compact, hence closed in L′; L′ is connected; so π(K̃) = L′ and **L′ is a
compact leaf of 𝓕**. But π(K̃) ⊆ K ⊆ L̄ ⊆ N, and (D3) says N contains no compact leaf.
Contradiction. (The transfer uses (D3) **downstairs** only, as the checklist requires.)

**K̃ is not open.** Suppose K̃ were open in M̃. π is a local homeomorphism, hence an open map, so
π(K̃) is a nonempty open subset of M contained in K. Now run Theorem O-5's clause-(iii) step
downstairs, verbatim from `refute-adjudication.md` §4: *"by clause (iii) L lies in the closure of
⋃_p γ_p, so L̄ ⊂ cl(⋃γ_p), and a nonempty open K inside that closure would meet some γ_p, but
K ⊂ N and γ_p ∩ N = ∅"*. Its two hypotheses are about M, not M̃, and both hold unchanged:
π(K̃) ⊆ K ⊆ L̄ ⊆ cl(⋃γ_p), so the nonempty open π(K̃) meets some γ_p; but π(K̃) ⊆ K ⊆ N and
γ_p ∩ N = ∅. Contradiction. **The step transfers because it is applied downstairs**, to π(K̃).

**K̃ is exceptional in the sense Theorem 1.1 needs.** Hurder's sense (not a compact leaf, not open)
is now established. Upgrade it to Candel–Conlon's, which is what Warsaw's "exceptional LMS" means:
by the trichotomy at Candel–Conlon I p. 176 (quoted in adjudication §1.5) a local minimal set is a
single leaf, an element of 𝒪(𝓕̃), or exceptional. K̃ is closed in the compact M̃, so if K̃ were a
single leaf it would be a closed hence compact leaf ((D2a), Epstein 1976 §§2.2–2.4 p. 268 — cited,
not claimed), excluded above; K̃ is not open, so it is not an element of 𝒪(𝓕̃). Hence K̃ is an
**exceptional minimal set of 𝓕̃**, and with U = M̃ ∈ 𝒪(𝓕̃) it is an exceptional LMS in Warsaw's
sense (p. 225: *"Let U ⊆ M be an open, 𝓕–saturated subset and let X ⊂ U be an exceptional minimal
set of 𝓕|U. … we say that X is an exceptional LMS (local minimal set) of 𝓕."*).

### (f) L̃ accumulates on K̃ in Warsaw's sense, and ℰ^{K̃}(L̃) is one point — **CLOSES (inheriting §1.4's flagged inference, adding none)**

L̃ ≅ D by (b), so ℰ(L̃) = {ẽ} is a single end. K̃ ⊆ closure(L̃) by (e). Two cases, exactly
adjudication §1.4 with (M̃, 𝓕̃, L̃, K̃) substituted:

- **L̃ ∩ K̃ ≠ ∅.** K̃ is 𝓕̃-saturated, so L̃ ⊆ K̃; then closure(L̃) is a nonempty compact saturated
  subset of the minimal K̃, so closure(L̃) = K̃. This is Corollary 1.2's case and
  ℰ^{K̃}(L̃) = ℰ(L̃) = {ẽ}.
- **L̃ ∩ K̃ = ∅.** Then K̃ ⊆ closure(L̃) ∖ L̃ ⊆ lim L̃ (§1.4's argument: a point of
  closure(L̃) ∖ L̃ is a limit of points of L̃ ∖ K_α for every compact K_α ⊂ L̃, since K_α is closed
  in M̃ and misses the point). For a one-ended leaf lim_ẽ L̃ = lim L̃ — Candel–Conlon I Lemma 4.3.7
  (printed p. 116, vision): *"lim L = ⋃_{e ∈ ℰ(L)} lim_e L"*, which for ℰ(L̃) = {ẽ} reads
  lim_ẽ L̃ = lim L̃. So K̃ ⊆ lim_ẽ L̃, and by Definition 4.3.6 (p. 116: *"The end e is asymptotic to
  each leaf of lim_e L"*) ẽ is asymptotic to every leaf of K̃, i.e. ẽ ∈ ℰ^{K̃}(L̃).

Either way **ℰ^{K̃}(L̃) = {ẽ}**: nonempty, a single point, not a Cantor set.

*Debt accounting.* §1.4 flags "for a one-ended leaf lim_e L = lim L" and the reading of "asymptotic
to X" as the adjudicator's inference. Lemma 4.3.7 supplies the first in print, which is more than
§1.4 had. The reading of "asymptotic to a set" remains §1.4's, and it is the **same** inference the
downstairs verdict already carries — this lemma inherits it and adds no new debt. It is not a
rider on R1.

### (g) Duminy applies verbatim upstairs — **CLOSES**

*Printed standing hypotheses (Cantwell–Conlon, "Endsets of exceptional leaves; a theorem of
G. Duminy", Warsaw 2000 proceedings, World Scientific 2002, printed p. 225 = PDF 234, offset −9,
vision):*

> *"Let (M, 𝓕) be a transversely oriented, C²–foliated manifold of codimension one, with M compact
> and oriented. We assume each component of ∂M, if any, is a leaf of 𝓕. Remark that each leaf of 𝓕
> is oriented."*
>
> **Theorem 1.1 (Duminy)** *"If the leaf F of 𝓕 is semiproper and if it accumulates on the
> exceptional LMS X, then ℰ^X(F) is homeomorphic to the Cantor set."*

Checked one by one against (M̃, 𝓕̃): transversely oriented — (a); C²-foliated of codimension one —
(a); M compact — (a); M oriented — (a); ∂M̃ = ∅ so the boundary clause is vacuous — (a). X = K̃ is
an exceptional LMS — (e). F = L̃ is semiproper — (c). F accumulates on X — (f). **Every hypothesis
is discharged by an earlier step; none is assumed.**

Second printed instance of the same standing hypotheses, as the brief directs (Cantwell–Conlon,
*Leaves of Markov local minimal sets in foliations of codimension one*, Publ. Mat. 33 (1989),
printed p. 461 = PDF 1, offset +460, vision): *"Let M be a compact, orientable manifold, 𝓕 a
transversely orientable C² foliation of M of codimension one. Each component of ∂M, if there are
any, is to be a leaf."* Same class; "orientable" where Warsaw prints "oriented".

Hypothesis 5's "if nonempty": the abstract at p. 225 reads *"the set ℰ^X(F) of ends of F asymptotic
to X, if nonempty, is homeomorphic to a Cantor set"*. (f) gives ℰ^{K̃}(L̃) = {ẽ} ≠ ∅, so the clause
is satisfied and cannot rescue the configuration — adjudication D8 upstairs, unchanged.

### (h) The conclusion descends — **CLOSES**

Suppose (S′) holds downstairs. By (c), L̃ is semiproper upstairs. By (g), Theorem 1.1 applies with
F = L̃, X = K̃ and gives ℰ^{K̃}(L̃) homeomorphic to the Cantor set. By (f), ℰ^{K̃}(L̃) is a single
point. A one-point space is not homeomorphic to the Cantor set. Contradiction.

Hence **¬(S′) for L**: no x₀ ∈ L admits a transverse arc J out of x₀ with J ∩ L = {x₀}; the
archimedean leaf of an object satisfying hypothesis 1 has no proper side, in the orientation-free
sense of §1. Rider R1 is discharged: the (S) PRINTED-NO verdict of S19-1 holds for the manifold
case **without** the orientation clauses, in the form ¬(S′).

The implication runs in the one direction (c) supplies — (S′) downstairs ⟹ (S) upstairs — so the
refutation upstairs refutes downstairs. Nothing is claimed in the converse direction.

### (i) Scope — **CLOSES**

- **Nothing about the flow lifts with its axioms intact.** φ lifts to M̃ (ℝ is simply connected, so
  the homotopy-lifting property of the covering π gives a unique φ̃ with φ̃⁰ = id), but clause (i)
  fails upstairs: a closed orbit γ_p of least period log p has π⁻¹(γ_p) a disjoint union of closed
  orbits of least period log p or a proper multiple of it (up to 4 log p in the 4-fold case), so
  "exactly one primitive closed orbit of least period log p, and no other closed orbits" is not
  preserved. **The lemma never uses φ̃.** Every flow-dependent input — (D3), (D4), (D5), clause
  (iii)'s γ_p argument — is used **downstairs**, in steps (b), (e) and (d). This is why the cover is
  not a change of object and why the lemma yields nothing about existence.
- **The lemma is about (S) only.** It does not transfer the level of L, the Markov property of K,
  the theory-of-levels apparatus, or any endset statement about K̃'s own leaves; and it decides no
  face of Q-S4⁗. S19-2 stands verbatim: ¬(S) kills the route (S) ⟹ (b-NO); it kills no object.
- **The statement repair of §1 is part of the scope.** Downstairs, without transverse orientability,
  "semiproper" is undefined on the printed source's own terms (Candel–Conlon I p. 133) and the
  printed apparatus that surrounds it — 𝒪(𝓕), border leaves, Lemma 5.3.2 — sits under §5.2's
  standing assumption (printed p. 126: *"We will simplify the discussion considerably by assuming
  that the foliation is transversely oriented and that ∂⋔M = ∅"*). The lemma's conclusion is
  therefore ¬(S′), which is well-formed with no orientation hypothesis and agrees with ¬(S)
  wherever both are defined. Any ledger wording that drops rider R1 must carry (S′).
- **No construction is licensed** (standing order 6). The lemma widens a PRINTED-NO; it exhibits
  nothing and refutes nothing that was not already refuted in the oriented class.

---

## §3. Hypothesis 2, supplied from the page

**SUPPLIED — Candel–Conlon I, §3.5 "Orientation Covers", printed pp. 94–95 (PDF 101–102, offset
+7). Read at the page in this stream by vision; §3.5 had been read by no one on this record
(adjudication §8 "Not read": "Candel–Conlon I §3.5 (the double-cover section p. 126 points to)").**

What the page gives, in its own order:

1. **The orientation double cover of M** (p. 94): *"Recall that, if a connected n–manifold M is not
   orientable, it has a canonical, connected, 2–fold cover π : M̃ → M such that M̃ is orientable.
   This is called the orientation cover…"* Formed from the two choices {±μ_x} of orientation of
   T_x(M), with π(±μ_x) = x. Its connectedness is characterized: *"This makes sense, even if M is
   orientable, in which case M̃ falls into two connected components, each of which is carried
   diffeomorphically onto M by π. Connectedness of M̃ is exactly the condition that M be
   nonorientable."* The page also records that the differentiable structure lifts, that π is
   locally a diffeomorphism, and that *"If there is a foliation 𝓕 on M (of arbitrary codimension),
   π lifts 𝓕 to a well-defined foliation 𝓕̃ = π*(𝓕)."*
2. **The transverse-orientation double cover of 𝓕** (p. 94): *"Given a connected, foliated manifold
   (M, 𝓕), there is a corresponding construction of a 2–fold cover π : M̃ → M such that π*(𝓕) is
   transversely orientable. One proceeds exactly as above, using local orientations of the normal
   bundle ν(𝓕) in place of local orientations of T(M). Again, M̃ will be connected if and only if
   ν(𝓕) is a nonorientable vector bundle."*
3. **Their combination** (p. 94, last line before the Proposition): *"Combining these observations,
   we have the following."* — then Proposition 3.5.1, quoted in full in §2(a): a **connected**
   covering space, **either 2–fold or 4–fold**, with M̃ orientable and 𝓕̃ transversely orientable,
   and all leaves of 𝓕̃ orientable. Its final assertion is proved on p. 95: *"A loop on a leaf L
   must preserve both the orientation of T(M̃) and of ν(𝓕̃), hence preserves the orientation of
   T(L)."* The page then states the device's purpose: *"This proposition often allows us to reduce
   the proof of a theorem to the special case in which everything in sight is orientable. This is
   especially useful for foliated manifolds of codimension one."*

**Is "at most 4-fold" right? Yes — and that is what the page says.** The printed degrees are 2 and 4;
the case where M is already orientable and 𝓕 already transversely orientable is outside the
Proposition's hypothesis and is covered by π = id. So the greatest degree ever needed is 4, and
"at most 4-fold" is exact. Hypothesis 2 is discharged in print, and the adjudicator's RECALLED tag
(§8: "that a finite cover on which M is oriented and 𝓕 transversely oriented exists (at most
4-fold) — used only in the D3 sketch") is now retired: it is Proposition 3.5.1.

**On the composite, precisely.** The page does **not** assert that the fiber product of the two
double covers is connected, and this check does not assert it either. What is printed is weaker and
sufficient: *there exists* a connected cover of degree 2 or 4 with both properties. (Degree 2 occurs
when one 2-fold cover already achieves both — e.g. M nonorientable with 𝓕 transversely orientable,
or the two local-orientation obstructions agreeing; degree 4 when two independent 2-fold covers must
be composed. The page states the dichotomy without partitioning it, and I record it as the page
does, adding nothing.) **Connectedness of the cover actually used is printed**, and the lemma needs
it: step (b) 6 requires L̃ connected but not M̃ connected, while step (a)'s choice of an orientation
of TM̃ and of ν(𝓕̃) is a single choice only because M̃ is connected.

**Page-locating note (for whoever checks this).** The offset drifts as the digest warns. §3.5 was
located by the table of contents (printed p. x, PDF 5: "§3.5. Orientation Covers 94"), then by
rendering PDF 98 (running head "3.4. Tangential Gluing", folio 91 ⇒ offset +7) and PDF 101–102
(folios 94, 95). Offsets confirmed in this stream: **+7 at printed 91–95**, **+6 at printed
115–117**, **+4 at printed 126 and 133**. Warsaw: **−9** (printed 225 = PDF 234). r5-01: **+460**
(printed 461 = PDF 1).

---

## §4. Verdict

**CLOSES.** Steps (a)–(i) all close: (a) CLOSES, (b) CLOSES, (c) CLOSES, (d) CLOSES, (e) CLOSES,
(f) CLOSES, (g) CLOSES, (h) CLOSES, (i) CLOSES.

**Two conditions attach to the close, neither of which reopens a step.**

1. **The conclusion must be carried as ¬(S′)** — "no x₀ ∈ L admits a transverse arc J out of x₀
   with J ∩ L = {x₀}" — not as "L is not semiproper". Candel–Conlon I p. 133 prints that
   semiproperness "only makes sense for transversely–orientable foliations of codimension 1", so
   the digest §E wording is not well-formed under hypothesis 1, which removes exactly that. (S′) is
   the printed content of Lemma 5.3.2's proof, is orientation-free, coincides with semiproperness
   whenever the latter is defined, and is precisely what step (c) lifts. This is a repair of the
   statement, not a defect in the argument.
2. **The inherited debts are unchanged, and no new one is created.** The lemma still rests on
   (D3), (D4), (D5) downstairs — so rider R3 (conditional on Reading (iii)′) and rider R2 (C² only)
   survive untouched — and on adjudication §1.4's reading of "asymptotic to a set", which the
   downstairs verdict already carries. **Only rider R1 is discharged.**

**Refutation-shaped close (KICKSTART 10(c)).** *The proof class "the printed instruments are
unavailable in the non-orientable class, so (S) is undecided there" cannot yield an open case,
because Candel–Conlon I Proposition 3.5.1 (printed p. 94) supplies a connected cover of degree at
most 4 on which M̃ is oriented and 𝓕̃ transversely oriented, a proper side lifts through a local
homeomorphism, and (D3)/(D5)'s downstairs content excludes both alternatives for the minimal set
upstairs — so Duminy's Theorem 1.1 applies upstairs to L̃ ≅ D and ¬(S′) holds downstairs.*
**And: this cannot yield existence of any object, because the flow's clause (i) does not survive
the cover and the lemma never uses the lifted flow.**

---

## §5. Proposed ledger block for S19-7 (≤ 8 lines), if the dual-check agrees

Insertion-only, dated, to replace the "alternatively…" clause of §16-sexies S19-7:

> **[DOUBLE-COVER LEMMA — dual-model check 2026-09-10, Session 20; `results/c3-r/s20/dc/check-F.md`, `check-O.md`, brief `dc/BRIEF.md`, digest §E]**
> **S19-7 amended. Rider R1 is DROPPED; (H0)-manifold returns to "C² codimension-one, no orientation hypothesis".** The transfer is printed at the page: Candel–Conlon I **Proposition 3.5.1, printed p. 94** — "If M is nonorientable and/or 𝓕 is not transversely orientable, there is a connected covering space (either 2–fold or 4–fold) π : M̃ → M such that M̃ is orientable and the lifted foliation 𝓕̃ is transversely orientable" — retiring the adjudicator's RECALLED "at most 4-fold" (§8).
> With π*𝓕 C² of codimension one on the closed oriented M̃ (p. 94: π "locally a diffeomorphism", 𝓕̃ = π*(𝓕)), each component L̃ of π⁻¹(L) is homeomorphic to L ≅ D (covering of a simply connected base); a transverse arc J out of x₀ ∈ L with J ∩ L = {x₀} lifts to J̃ with J̃ ∩ L̃ = {x̃₀}; closure(L̃) ∩ π⁻¹(K) is nonempty (π(closure L̃) ⊇ L̄ ⊇ K), compact and 𝓕̃-saturated, so it holds a minimal K̃, which is no compact leaf (its image would be one inside K ⊆ N, against (D3)) and not open (π open, so π(K̃) ⊆ K would be open in cl(⋃γ_p), against Theorem O-5's clause-(iii) step). Duminy's Theorem 1.1 then applies upstairs against ℰ^{K̃}(L̃) = one end.
> **Wording binding on every future citation:** the clause carried is **(S′)** — "no x₀ ∈ L admits a transverse arc J out of x₀ with J ∩ L = {x₀}" — because Candel–Conlon I p. 133 prints that semiproperness "only makes sense for transversely–orientable foliations of codimension 1"; (S′) agrees with ¬(S) wherever "semiproper" is defined.
> **Riders R2 (C²) and R3 (Reading (iii)′) are untouched.** **No verdict changes** — S19-2 stands: ¬(S) kills the route (S) ⟹ (b-NO), and kills no object. Nothing about the flow lifts (clause (i) fails upstairs); no construction is licensed (standing order 6).

Frontier line, if enacted: the double-cover lemma leaves the frontier list; the one remaining
program item of §16-sexies is closed.

---

## Honesty note (standing order 5) — read, recalled, inferred

**Read by vision, by me, in this stream** (`pdftoppm`, 100–140 dpi, then Read):
Candel–Conlon I (`fetched-r4/r4-15a-candel-conlon-foliations-I-GSM23.pdf`, image-only, 398 pages):
PDF 4–5 and 6–7 (contents, printed pp. x–xii); PDF 98 (printed 91, to fix the offset); **PDF 101–102
(printed 94–95, §3.5 "Orientation Covers" in full — the section the record had never read)**;
PDF 121 (printed 115, §4.3 Definitions 4.3.1/4.3.3/4.3.4, Lemmas 4.3.2/4.3.5); PDF 122 (printed 116,
Definition 4.3.6, Lemma 4.3.7, Definition 4.3.8, Lemma 4.3.9); PDF 123 (printed 117); PDF 130
(printed 126, the §5.2 preamble and Definitions 5.2.1/5.2.2); PDF 137 (printed 133, §5.3 with
Lemma 5.3.2 and its proof).
Warsaw volume (`fetched-r4/r4-01+12-…`): PDF 234 (printed 225 — title, abstract, §1 standing
hypotheses, LMS definition, endsets, Theorem 1.1).
r5-01 (`fetched-r5/r5-01-…`): PDF 1 (printed 461 — title, abstract, Introduction's standing
hypotheses).

**Read as on-disk records (not re-derived):** `results/c3-r/s20/dc/BRIEF.md`;
`results/c3-r/s20/insights-digest.md` §E in full (plus §F for the guard list);
`results/c3-r/s19/qs4quad/adjudication.md` §1 (all), §2 (all, D3 verbatim), §8;
`results/c3-r/s16/qs4prime/refute-adjudication.md` §4 (Theorem O-5 and Case A);
`results/c3-r/s19/insights-digest.md` §G, §H, §I (the contract, (D1)–(D6), the guards);
`results/c3-r/m2c-feasibility-ledger.md` §16-ter N-3 ((D4) and Reading (iii)′), §16-sexies
S19-1/S19-2/S19-7/S19-10.

**Not read:** `results/c3-r/s20/dc/check-F.md` (forbidden by the brief; not opened, not listed, not
inferred). Also not opened in this stream: Candel–Conlon I §8.1/§8.3/§8.4 (pp. 176, 187, 189–199) —
the adjudication's vision quotations of those pages are used as its quotations, and the only one
load-bearing here is the p. 176 LMS trichotomy in step (e); Hector–Hirsch; Hurder; Ghys; Epstein
1976 (cited through (D2a), never claimed).

**Inferred by me, flagged in place, each written out rather than asserted:** step (a)'s four riders
(M connected or restrict to L's component; M̃ compact; orientations chosen; C² and codimension
preserved by a local diffeomorphism); step (b)'s proof that π|L̃ is a covering map and hence a
homeomorphism; step (c)'s lift of the arc; step (d)'s saturation of closure(L̃) and of π⁻¹(K), and
the nonemptiness chain π(closure L̃) ⊇ L̄ ⊇ K; step (e)'s "π(K̃) = L′ is a compact leaf" and the
upgrade of Hurder-exceptional to Candel–Conlon-exceptional via the p. 176 trichotomy plus (D2a);
step (i)'s lift of the flow and the period statement; and the **well-formedness repair (S′)**, which
is mine and is the one substantive addition this check makes to the sketch.

**RECALLED, load-bearing for nothing:** nothing. Every fact used is either printed at a page listed
above, quoted from a record listed above, or argued out in §2. In particular the sketch's two
recalled items are now printed: "a finite cover, at most 4-fold, with M̃ oriented and 𝓕̃
transversely oriented" is Proposition 3.5.1 (p. 94), and "leaves of the pullback cover the leaves
below" is proved in step (b) rather than recalled.

**Where I would be wrong if a source were mis-set.** (1) If Proposition 3.5.1's degree bound were
misread and an infinite cover were needed, step (a) would fail and M̃ would not be compact, killing
(d) and (e); the page prints "either 2–fold or 4–fold" and I read it at 140 dpi. (2) If (D3) were
withdrawn, (e)'s compact-leaf exclusion lapses and the lemma is OPEN at (e). (3) If Reading (iii)′
were withdrawn, (D4) lapses, L̃ need not be simply connected, and both (b) and (f) fail — this is
rider R3, already carried. (4) If "asymptotic to X" were read so that a single end asymptotic to
every leaf of K̃ does not lie in ℰ^{K̃}(L̃), (f) lapses — this is adjudication §1.4's standing
inference, identical downstairs, and its failure would withdraw S19-1 itself, not merely this lemma.

**No file outside `results/c3-r/s20/dc/check-O.md` was created or modified by this stream.**

**Machine clock at finish:** 2026-09-10 04:33:46 IST, Session 20.
