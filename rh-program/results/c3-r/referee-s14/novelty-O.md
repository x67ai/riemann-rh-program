# NOVELTY / PRIOR-ART SWEEP — CHECK O (standing order 7, one of two independent checks)

**Program:** RH program, direction C3-r (geometric substrate, reduced recommission). **Session 14.**
**Date of the sweep:** 2026-09-02 local (all network queries logged below carry the server-side UTC stamp 2026-09-01T20:2x–21:1x / 2026-09-02).
**Author:** referee agent, check **O**. The second check is a different model; nothing below has been softened in the expectation that the other check will catch it (standing order 7).
**Scope:** the five Session-8 novelty assertions N1–N5 named in the charter, as asserted in `results/c3-r/probe-9.3-a.md`, `probe-9.3-b.md`, `probe-9.3-adjudication.md`, `probe-9.4-note.md`.
**Not in scope:** re-derivation of the mathematics. Where a re-derivation issue is visible from the prior-art work it is flagged as an *observation for the adjudicator* and labelled as such.
**Standing order 5 compliance:** every claim below about a source was read this session from the on-disk PDF (page stated) or from a text I fetched this session (location stated). Nothing is recalled. Where I could not reach a source I say UNDETERMINED and name it.

---

## 0. VERDICT TABLE (stated first)

| # | Claim (abbreviated) | Verdict | Severity of the required change |
|---|---|---|---|
| **N1** | Packet-closure law (Thm A): cl(one periodic orbit) ⊇ its whole packet; forcing group = coker(lk_p); mechanism = profinite Frobenius-return accumulation; packets minimal; one orbit of length log p forces uncountably many | **NOVEL** (statement not in the literature) | MINOR — credit the two published ingredients, below |
| **N2a** | X₀ is non-Hausdorff along its packets; no periodic orbit is closed | **PARTIAL** | **MAJOR** — Deninger states the cause verbatim and proves an irreducible (hence non-Hausdorff) quotient of the same shape |
| **N2b** | Every closed flow-invariant subset meeting every packet is infinite-dimensional (n-cells for all n) | **PARTIAL** (derivative of [x-03] §8 + N1) | MINOR + one observation for the adjudicator |
| **N2c** | ⇒ the first alternative of Deninger's question ([x-03] §6 p. 40) has answer NO | **NOVEL** (conditional on N1 and on a dimension argument) | none |
| **N3i** | B_p = coker(Aut_ring(F̄_p) → Aut_group(F̄_p^×)) = coker(lk_p) | **ANTICIPATED** — verbatim displayed formula, [x-03] p. 2 | **MAJOR** — remove every novelty framing; cite [x-03] p. 2 |
| **N3ii** | Aut(C)-equivariance no-go (Prop. 1) and the D1–D3 trichotomy | **NOVEL** | MINOR |
| **N4a** | Haar-average the packet base: canonical, Aut(C)-equivariant, flow-invariant | **PARTIAL** — the device (packet + canonical uniform/Haar average over the orbits of the packet) is standard, named, and in print in homogeneous dynamics | **MAJOR** — the "new in this note" framing is not sustainable for the device; cite the packet-average literature |
| **N4b** | DQ-M: a measured trace formula for foliated flows with a continuum of periodic orbits | **PARTIAL** — nobody has done the foliated/Cantor-continuum + transverse-measure version (that is genuinely open and unclaimed), but (i) the measured/type-II lamination trace machinery is in print and (ii) trace formulas whose orbital side is an integral over a positive-dimensional family of periodic orbits are classical (clean / Bott–Morse) | MINOR — add a scope sentence |
| **N4c** | "Has anyone proposed Haar-averaging Deninger's packets?" | **NOVEL** — no. But a published canonical *packet-collapsing* map exists ([r3s-08] Thm 3.6 + Thm 3.7(2)) and must be cited | **MAJOR** — it is a rival canonical resolution of the same defect |
| **N5** | Thm C: one-orbit-per-prime admissible cuts exist (reachability a₀·p^Ẑ) but are non-canonical and forfeit the certified theory | **NOVEL** for the theorem; the *conclusion* is Deninger's own stated position | MINOR — cite his three remarks |

**Coverage note, stated up front and honestly.** The citing literature of arXiv:1807.06400 is unusually small and I enumerated it three independent ways (Semantic Scholar graph API, OpenAlex, and arXiv metadata sweeps on four phrasings) with consistent results; every member with any topological or dynamical content was opened and searched. That is what gives the NOVEL verdicts their weight. Two enumeration channels were **unreachable**: Google Scholar "cited by" (302 → `google.com/sorry` captcha) and zbMATH Open's web citation list (HTTP 403 to WebFetch; the zbMATH REST API carries no citation endpoint). A Scholar sweep is therefore still owed before external circulation — see §7.

---

## 1. N1 — the packet-closure law. Verdict: NOVEL.

### 1.1 What I looked for
Statements of the form "the closure of a single periodic orbit of Deninger's flow contains the whole packet", "the packet is a minimal set", "every orbit is dense in its packet", "one closed orbit of length log p forces uncountably many", in any vocabulary: dynamical (orbit closure / minimal set / dense orbit / quasi-orbit), foliation-theoretic (leaf closure, saturation), profinite-solenoidal (accumulation of a dense monoid, odometer, adding machine, Cantor group), class-field-theoretic (linking number, Frobenius, Artin symbol, monodromy), knot-theoretic (Morishita's linking), and Witt-vector (rational Witt space, W_rat).

### 1.2 What the primary sources actually contain (read this session, page-anchored)

* **[x-03] Deninger, arXiv:1807.06400v4, §8, printed p. 49**, verbatim: *"Since we want to keep periodic orbits for every closed point of X₀ one idea would be to replace X₀ by the dynamical system Y₀ obtained as the topological closure of the union of all periodic orbits coming from closed points of X₀. In this section we will show that the system Y₀ is still infinite-dimensional: Namely, for one-dimensional X₀, flat over spec Z and conditionally for all X₀ we have Y₀ = X̌₀(S¹) ×_{Q>0} R^{>0}."* — the closure computed there is of the **union of all** periodic orbits. No statement anywhere in the paper about the closure of one orbit, or of one packet.
* The **published** version — **[z-19] = Indagationes Mathematicae 37 (2026), no. 1, 25–136**, DOI 10.1016/j.indag.2024.05.007, on disk as `fetched/z-19-…-INDAG-published.pdf` — carries the same two sentences (intro and §8) word for word. Nothing was added between arXiv v4 and print on this point. (Bibliographic data read off the article's own first page: *"Indagationes Mathematicae 37 (2026) 25–136"*; confirmed independently against zbMATH document 8143081, whose source line is *"Indag. Math., New Ser. 37, No. 1, 25-136 (2026)"*.)
* **[x-06] Deninger, arXiv:2301.11643, §4**: the packets are described as *"compact subsets Γ_{x₀} ⊂ X₀ [that] consist of periodic orbits of length log N x₀ … and they are pairwise disjoint"*; no closure statement.
* **[r3s-08] Morishita, arXiv:2508.15971v5**: computes the **covering monodromy** around γ_{p,a} (Thms 2.2.8, 2.2.9, 2.3.1) and the CC correspondence; no orbit-closure statement, no minimality statement.
* **[r3s-19] Álvarez López–Kim–Morishita, arXiv:2410.20758v1**, **[r3s-21] Leichtnam, math/0603576v2**, **[r3s-17] ÁLKL, arXiv:2402.06671v1**: all are in the *simple/nondegenerate closed orbit* regime; they cannot state the claim (see §4.2).
* **Morishita, *Knots and Primes*, 2nd ed. (`fetched-r2/r-09`)** and **Morishita, arXiv:0904.3399v1 (`fetched-r2/r-26b`)**: the word "packet" does not occur; the Deninger references are to the pre-2018 programme papers plus arXiv:1807.06400**v2** as background only.
* **Connes–Consani** arXiv:2401.08401, arXiv:2501.06560 (= [CC3], *Knots, primes and class field theory*, Contemp. Math., Regulators V), arXiv:2606.06604, and *On the Jacobian of Spec Z* (J. Noncommut. Geom., submitted; on disk in `sources-extracted/`): the word "packet" does not occur in any of them. Their C_p is a **single** periodic orbit of length log p, so the phenomenon cannot arise there.

### 1.3 Ingredients that ARE in print, and must be credited rather than claimed

1. **The packet fibration and its base.** [x-03] **printed p. 2**, displayed, read by vision from the PDF page (not from the text layer, which garbles the superscripts):
   > "If p = char κ(x₀), then Γ_{x₀} is fibred over the compact group   Aut(F̄_p^×)/Aut(F̄_p) = Ẑ^×_{(p)}/p^Ẑ ,   with fibres the periodic orbits in Γ_{x₀}."
   Repeated at [x-03] **§6, printed p. 38** (as an R^{>0}-**bijection**, not a homeomorphism — see §2.3) and in [x-06] §4.
2. **lk_p.** [r3s-08], §2.2 (the passage beginning "and hence there is the natural inclusion lk_p : Gal(κ(P)/κ(p)) ↪ Aut(κ(P)^×) = Ẑ^×_{(p)}"), verbatim: *"We note that when K = Q and p = (p), the map lk_p is nothing but the arithmetic linking homomorphism lk_p in (1.2.1), (1.2.2) or (1.2.3)."* [r3s-08] also records, §1.2, that *"Connes and Consani noticed that the arithmetic linking homomorphism coincides with the following homomorphism of étale fundamental groups"* and that they proved lk_p *"gives really a geometric monodromy around the R⁺-orbit C_p"* ([CC3; Thm 0.2, Thm 3.2]).
3. **Density of N in Ẑ_{(p)}** is CRT.

Consequently the clause "**the forcing group is coker(lk_p)**" is a **relabelling of published data**, not a new identification: the group is Deninger's own displayed quotient and the map is Morishita's own lk_p. That costs the claim nothing, but the note must not present the identification as a discovery. **Severity MINOR.**

### 1.4 Verdict
**NOVEL.** No source found, on disk or online, states the single-orbit closure law, the minimality of the packet, or the uncountable-multiplicity forcing. Search log entries S-01…S-14, S-21, S-24 (§6).

---

## 2. N2 — non-Hausdorffness along packets; infinite-dimensionality; NO to Deninger's first alternative.

*(Pagination note: in `fetched/x-03-…-arxiv-v4.pdf` the PDF page number equals the printed page number throughout the range used here — verified by reading the page footers on pp. 2, 38, 49, 63, 64, 76.)*

### 2.1 N2a — "X₀ is non-Hausdorff along its packets; no periodic orbit is closed." Verdict: **PARTIAL**.

This is the finding of the sweep that most needs to reach the adjudicator. **Deninger states the structural cause of the phenomenon verbatim, twice, and proves non-Hausdorffness of a quotient of exactly this shape.** Four anchors, all read this session from `fetched/x-03-…v4.pdf`:

1. **p. 49**, immediately before §8, verbatim:
   > "The Q^{>0}-action on Ȟ_{E_tors} × R^{>0} is **not properly discontinuous**. In section 10, we will see that this works to our advantage."
2. **p. 76**, §12, verbatim — and this one is about the actual suspension, not an adelic model:
   > "It appears because the action of Q_0^{>0} on X̌₀(C) × R^{>0} is **not properly discontinuous** if the rank of Q₀ is greater than one."
3. **p. 63**, §10, verbatim — Deninger explicitly warns that the natural continuous bijections onto subspaces of the suspension need not be homeomorphisms, which is precisely the failure that makes Γ_p's subspace topology differ from B_p × S¹:
   > "Note that in general the continuous bijection π|_{M×{u}} : M × {u} → π(M × {u}) will **not be a homeomorphism** if π(M × {u}) is equipped with the subspace topology of X. If Q acts properly discontinuously on M × R^{>0} and if M is a manifold, then F is an actual 1-codimensional foliation. In general however the partition of X into the disjoint spaces π(M × {u}) for u ∈ R^{>0} mod Q will not be locally trivial."
4. **p. 64, Proposition 10.3 + the preceding paragraph and the following Remark**, verbatim:
   > "Recall that a topological space Y is called irreducible if it is not the union of two proper closed subsets or equivalently if any two non-empty open subsets have non-empty intersection. All continuous maps from an irreducible topological space Y to a Hausdorff space are constant. …
   > **Proposition 10.3.** Assume that char N₀ contains almost all prime numbers. If Q_0^{>0}Ẑ^× × R^{>0} carries the adele topology i.e. the subspace topology of Q_0^{>0}Ẑ^× × R, then the quotient space Y = Q_0^{>0}Ẑ^× ×_{Q_0^{>0}} R^{>0} is **irreducible**.
   > **Remark.** By [LR00, Lemma 3.1], the orbits of the Q^{>0}-action on Q^{>0}Ẑ^× × R^{>0} are closed. The same argument works for Q_0^{>0} … and it follows that the points of Y are closed, i.e. Y is a **T₁-space**."

   An irreducible T₁ space with more than one point is not Hausdorff (two distinct points would have disjoint neighbourhoods, contradicting irreducibility). So **a published theorem of [x-03] already exhibits a non-Hausdorff, T₁, suspension-shaped quotient Q_0^{>0}Ẑ^× ×_{Q_0^{>0}} R^{>0}** — the adelic shadow of X₀ under the map r of (66)/(93) — and Deninger uses that non-Hausdorffness *positively*, to prove H⁰_F = R (Theorem 10.2).

**What is therefore NOT new:** that a suspension of this shape by this non-properly-discontinuous Q^{>0}-action produces a non-Hausdorff quotient; that the leaf/packet bijections need not be homeomorphisms; that Deninger knew and exploited the failure.
**What IS new (nothing found in any source):** the statement that **X₀ itself** is non-Hausdorff; that the failure is **localised inside a single packet** (i.e. that Γ_p's own subspace topology is non-Hausdorff); that **no periodic orbit is closed as a subset of X₀**; and the explicit two-limit witness (a single sequence on one orbit with two distinct limits, one given by Theorem A and one by the p^Z-rotation).

**Required change — MAJOR.** Wherever the programme records "X₀ is non-Hausdorff along its packets" as a *new negative structural datum* (adjudication §4 item 3; probe B Cor. A.2), the record must place [x-03] pp. 49, 63, 76 and Prop. 10.3 (p. 64) in front of it and restate the increment as the three italicised items above. As written, a reader would take the non-Hausdorffness itself to be the discovery; it is not — the discovery is its location and its consequence for orbits.

**Standing conflict, already on the books, re-confirmed here.** [r3s-08] Thms 2.2.8/2.2.9 assert **homeomorphisms** for the packet models, while [x-03] §6 p. 38 asserts only **bijections** ("The Q_0^{>0}-bijection (39) induces an R^{>0}-bijection … → Γ_{x₀}"). The adjudication's W11 flag ("do not cite [r3s-08] for topology") is correct and is confirmed verbatim. N2a does not merely add to the literature here: it **contradicts** [r3s-08]'s wording. A novelty report must say so plainly, because a claim that contradicts a published statement is not "novel", it is *in conflict*, and the note owes the reader that sentence.

### 2.2 N2b — "every closed flow-invariant subset meeting every packet is infinite-dimensional". Verdict: **PARTIAL (derivative)**.

Given N1, this is an immediate consequence of Deninger's own §8: a closed invariant set meeting every packet contains every packet (N1), hence contains the union of all periodic orbits, hence contains its closure Y₀ = X̌₀(S¹) ×_{Q>0} R^{>0} ([x-03] Thm 8.2, p. 50, unconditional for one-dimensional X₀ flat over spec Z via [Per11, Theorem 1] — read at p. 49: *"If spec A is a non-empty open subscheme of spec o_κ for some number field κ, then the set M in Claim 8.1 is always infinite, and it even has a positive Dirichlet density. This follows from [Per11, Theorem 1]."*), which [x-03] p. 49 says is "still infinite-dimensional". So the only content beyond [x-03] §8 is N1 itself plus a dimension argument.

**Observation for the adjudicator (not a novelty finding; MINOR, but it should be checked).** The string "infinite dimensional"/"infinite-dimensional" occurs exactly **three** times in [x-03] (intro p. 5-area line "The resulting dynamical system is still infinite dimensional"; §8 opening p. 49 twice), always in prose. I found **no dimension-theoretic theorem** in [x-03] establishing dim X̌₀(S¹) ×_{Q>0} R^{>0} = ∞. If that is right, then probe A's n-cell construction (Theorem B(b)) is not decoration: it supplies a step [x-03] only asserts — which makes it *more* load-bearing than the adjudication's §4 item 6 treats it ("checked at proof-sketch level … its (a)-part and probe B's Cor. B, which carry the whole S4-closed kill, do not need it"). If Cor. B's route consumes "[x-03] §8's still-infinite-dimensional line" as an input, it is consuming an assertion, not a theorem. Recommend the adjudicator re-examine which of the two routes to N2b is actually theorem-backed.

### 2.3 N2c — "the first alternative of Deninger's question has answer NO". Verdict: **NOVEL**.

The question is open in print, in the **published** version. [z-19] = Indag. Math. 37 (2026) 25–136, §6, verbatim (and identical to [x-03] p. 40, footer-verified):
> "The system X̄₀ may have to be replaced by a much smaller system: Is there a sub-dynamical system Y₀ ⊂ X̄₀ = X̌₀(C) ×_{Q>0} R^{>0} or at least one which maps to X̄₀ such that dim Y₀ = 2d + 1 where d = dim X₀ and such that Y₀ contains at least one periodic orbit in Γ_{x₀} for every closed point x₀ of X₀? If d = 1, is there such a Y₀ which is a Riemann surface lamination in the sense of [26]?"

No answer, partial or full, to either alternative appears anywhere in the literature I reached. The zbMATH review of the published paper (zbMATH document 8143081, read via the zbMATH REST API this session) summarises the paper's topological and dynamical content and does **not** mention orbit closures, packet minimality or Hausdorffness — negative evidence from an independent expert reading.

---

## 3. N3 — the cokernel identity and the Aut(C)-equivariance no-go.

### 3.1 N3(i) — "B_p = coker(Aut_ring(F̄_p) → Aut_group(F̄_p^×)) = coker(lk_p)". Verdict: **ANTICIPATED**.

This is a **verbatim displayed formula in the introduction of the primary source.** [x-03], **printed p. 2** (read by vision off the rendered PDF page, because the text layer mangles the superscripts):

> "If p = char κ(x₀), then Γ_{x₀} is fibred over the compact group
>   **Aut(F̄_p^×)/Aut(F̄_p) = Ẑ^×_{(p)}/p^Ẑ** ,
> with fibres the periodic orbits in Γ_{x₀}."

`Aut(F̄_p^×)` is the group of automorphisms of the multiplicative group; `Aut(F̄_p)` is the group of automorphisms of the field, i.e. of the *ring*; the quotient of an abelian group by the image of a homomorphism **is** its cokernel. So Deninger's displayed formula and the 9.4 note's "structural identity" are the same statement, in the same notation, with the single word "cokernel" substituted for the solidus.

Three further occurrences of the same formula, all read this session:
* [x-03] **§6, p. 38**: "Γ_{x₀} fibres over Ẑ^×_{(p)}/p^Ẑ = Aut(F̄_p^×)/Aut(F̄_p) with fibres the R^{>0}-orbits in Γ_{x₀}."
* [x-06] §4 (the paragraph after Theorem 4.2): "Γ_{x₀} is a fibre space over the compact group Aut(F̄_p^×)/Aut(F̄_p) where p = char κ(x) with fibres the compact orbits in Γ_{x₀}."
* [z-19] (published), same sentence in the introduction.

And the "= coker(lk_p)" half is [r3s-08]'s verbatim identification (§1.4 above).

**Required change — MAJOR.** `probe-9.4-note.md` §0 presents this in bold as *"The structural identity underneath (§4, derived)"* and closes with *"W9 is hereby explained, not just recorded"*; §9 generalises it into a "design constraint". None of that survives contact with [x-03] p. 2. Replacement text the adjudicator can paste, preserving what is actually the note's own contribution:

> **The structural identity underneath (Deninger's own, [x-03] p. 2, displayed in his introduction).** The packet base is B_p = Aut(F̄_p^×)/Aut(F̄_p) = Ẑ^×_{(p)}/p^Ẑ — the cokernel of the map from ring-automorphisms of F̄_p to group-automorphisms of F̄_p^×; by [r3s-08] §2.2 that map is Morishita's arithmetic linking homomorphism lk_p, so B_p = coker(lk_p). **What this note adds is not the identity but its use:** Lemma A shows that mod-p additivity is exactly the device that cuts the group-automorphism torsor down to the ring-automorphism torsor Hom_ring(κ, k), so the surviving local ambiguity coincides with the dynamics, whereas over C the whole cokernel survives. That is the explanation of W9; the identity itself is quoted, not discovered.

The mathematics is unaffected. The novelty framing must go.

### 3.2 N3(ii) — Proposition 1 (Aut(C)-equivariance no-go) and the D1–D3 trichotomy. Verdict: **NOVEL**.

Nothing found. Searched for: Aut(C)-equivariance / field-automorphism equivariance obstructions on Deninger's or Kucharczyk–Scholze's spaces; wild automorphisms of C acting on spaces of multiplicative maps; "no canonical choice of a point per prime"; selection principles for admissible classes. Log entries S-06, S-15, S-16, S-19, S-22.

Two honest qualifications, neither of which touches the verdict:
* The ingredients are classical and should be cited as such rather than derived silently: surjectivity of Aut(C) → Aut(μ(C)) = Ẑ^× is cyclotomic theory plus Steinitz extension; the discontinuity of non-trivial automorphisms of C is standard.
* The **closest published relative** is [x-03] **Theorem 5.2** (p. 34), which already says packets are full for every E ⊇ E_f, i.e. the certified classes never cut a packet. Proposition 1 explains *why* (kernel-defined classes are Aut(C)-stable) and extends the conclusion to all Aut(C)-stable classes, admissible or not. That is a genuine extension; but the note should present it as explaining a published theorem, not as an independent obstruction.

---

## 4. N4 — the Haar-average road and DQ-M (a measured trace formula for orbit continua).

Three separable questions. I answer them separately because they get different verdicts.

### 4.1 N4(a) — "replace the one-orbit-per-prime demand by Haar measure on the packet base B_p". Verdict: **PARTIAL**.

**The device is standard, named, and in print — under the same word "packet".** In homogeneous dynamics a *packet* is a natural finite collection of periodic torus orbits forming a torsor under a class group, and the canonical measure on a packet is precisely the group-average of the individual orbit measures. Fetched and read this session (arXiv:1510.08481, I. Khayutin, *Arithmetic of Double Torus Quotients and the Distribution of Periodic Torus Orbits*), **printed p. 5**, verbatim:

> "The set of H-orbits in a single packet is a principal homogeneous space for the Picard group of the associated order, see [ELMV09, Corollary 4.4]. …
> **Each packet supports a canonical H-invariant probability measure. It is defined as the uniform average over the H-invariant probability measures supported on the individual periodic orbits in the packet.** … When n = 2 the convergence of periodic measures on H-invariant packets to the Haar measure is again a theorem of Duke [Duk88], cf. [ELMV12, Sku62]."

Structurally this is the 9.4 note's Road 2, one dictionary entry away: Deninger's Γ_p is a torsor under the compact group B_p exactly as the homogeneous-dynamics packet is a torsor under a Picard group, and "uniform average over the orbits of the packet" is Haar average over the torsor group. The finite-group case is the uniform average; the profinite case is Haar. The *transplant to Deninger's system* is not in print; the *idea* is a fifteen-year-old standard tool with its own equidistribution literature (Duke; Einsiedler–Lindenstrauss–Michel–Venkatesh).

**Required change — MAJOR.** `probe-9.4-note.md` §7 Road 2 is headed *"renounce selection; Haar-average the packet (**new in this note**)"*, and §0 lists it among the note's positive contributions. That heading must go. Replacement text:

> **Road 2 — renounce selection; take the canonical packet measure.** Proposition 1 kills selections but not measures. In homogeneous dynamics this is the standard move: a packet of periodic torus orbits is a torsor under a class group and carries a canonical invariant probability measure, the uniform average over the orbit measures (see e.g. Khayutin, arXiv:1510.08481, p. 5, and the Duke/ELMV equidistribution literature). The same device applies here verbatim, with B_p in place of the class group and Haar in place of the uniform average: B_p is a compact group, its Haar probability measure is translation-invariant, and by Lemma D(iii) Aut(C) acts on B_p by group translations, so Haar measure is canonical **and** Aut(C)-equivariant — it passes exactly the naturality test that every selection fails. **What is new here is only the transplant** — the observation that the naturality obstruction of Proposition 1 is a selection obstruction and evaporates for the packet-average measure — together with the DQ-M question it opens (§8).

**Two-line consequence the adjudicator should note.** Because the device is standard, the Road-2 programme also inherits the standard difficulty attached to it: in homogeneous dynamics the packet-average measure is useful because packets *equidistribute* as the discriminant grows (Duke's theorem and its higher-rank successors), and the analogous statement here — what the packet measures do as p → ∞ inside X₀ — is not addressed anywhere in the note. That is a research question, not a defect, but it is the obvious next one and the note does not name it.

### 4.2 N4(b) — DQ-M: a trace formula for foliated flows with a **continuum** of periodic orbits and a **transverse measure on the continuum**. Verdict: **PARTIAL**.

**(i) The note's negative premise is exactly right, and I confirmed it against all three on-disk frameworks.**
* **[r3s-17] ÁLKL, *A trace formula for foliated flows*, arXiv:2402.06671v1** (now published as a Springer *Lecture Notes in Mathematics* volume, 2026 — the chapter DOI 10.1007/978-3-032-15413-2_1 was retrieved from Crossref this session with author list López/Kordyukov/Leichtnam and container title *A Trace Formula for Foliated Flows*). Chapter 4, verbatim: *"Every simple closed orbit c, there are neighborhoods, V where c in M and I of ℓ(c) in R, such that c is the only closed orbit whose first positive period is in I… The flow φ is called simple if all of its fixed points and closed orbits are simple. If moreover M is closed, then Fix(φ) is finite, and C_I(φ) are finite for all compact I ⊂ R. Therefore P(φ) is a discrete subset of R."* A continuum of closed orbits of one common length is excluded by hypothesis.
* **[r3s-19] Álvarez López–Kim–Morishita, arXiv:2410.20758v1**, verbatim: *"We assume the condition **(A1) any closed orbit is simple**, which implies that P is a countable set."* And Lemma 2.2's proof: *"Since any closed orbit is simple … the closed orbits are isolated if we take the periods in a compact interval."*
* **[r3s-21] Leichtnam, *Scaling group flow and Lefschetz trace formula for laminated spaces with p-adic transversal*, math/0603576v2**: Theorem 2 opens *"Assume that the closed orbits γ of the flow φᵗ acting on S = L×R^{+*}/q^Z are non degenerate"*, and its orbital side is a **sum** Σ_γ Σ_{k≥1} l(γ) e^{−k l(γ)}(α(−k l(γ)) + α(k l(γ))) over primitive closed orbits.

**(ii) But the *measured* half of DQ-M is already built.** [r3s-21] constructs precisely the machinery the note asks for on the transversal side: *"The data of the Haar measure µ_{Z_p^m} in each local chart … induce a transverse measure µ_L on L"*; *"µ_L dx defines a transverse measure denoted Λ on (S,F)"*; the von Neumann algebra W(S,F) with the trace τ induced by that transverse measure, the Ruelle–Sullivan current C(Λ), and a type-II Lefschetz trace formula against it. So "measured trace formula on a lamination with a profinite transversal and Haar measure" is **published**; what is missing is only that its *orbital side* is a sum over isolated orbits rather than an integral over a continuum. DQ-M should be posed as a modification of Leichtnam's Theorem 2, not as a formula with no ancestor.

**(iii) And the "orbital side = integral over a family of periodic orbits" shape is classical.** Fetched and read this session: S. Zelditch, *Survey of the inverse spectral problem*, arXiv:math/0402356, **§8.1, PDF p. 78**, verbatim:
> "So far, we have mainly considered the trace of the wave group around nondegenerate periodic orbits. **For integrable systems, the periodic orbits usually come in families filling out invariant tori.** We now consider the appropriate notions of non-degeneracy in this context. We will always assume that the closed geodesics come in **clean families** … **Definition 8.1** A metric g on a compact manifold M will be said to have a simple clean length spectrum if the length function L_g on the loop space Map(S¹,M) is a Bott-Morse function which takes distinct values at distinct components of its critical set … The term Bott-Morse means that each component of Crit(L_g) is a manifold, whose tangent space is the kernel of dL_g. Equivalently, each component is a clean fixed point set for G_g^t. **One needs the clean (Bott-Morse) condition to get a nice wave trace expansion**."
and, on the same theme, PDF p. 21: *"in many examples (e.g. spheres or flat tori), the geodesics come in families, and the associated length T is the common length of closed geodesics in the family. In place of closed geodesics, one has components of the fixed point sets of G^T at this time … it is also common to assume that they are clean."*

This is the Duistermaat–Guillemin clean-case trace formula, in which the contribution of a positive-dimensional family of periodic orbits is an integral over that family. It is worth recording that **Deninger's own simile points straight at it**: [x-03] p. 2, *"The compact packets Γ_{x₀} are reminiscient of invariant tori."* The packets are the arithmetic analogue of exactly the degenerate situation the clean-case machinery was invented for.

**Verdict and required change (MINOR).** The note's sentence — *"no published trace formula admits a continuum of periodic orbits with a transverse measure on the continuum"* — is, read strictly (with the transverse-measure clause), one I could not falsify: the clean case gives a smooth family with a Liouville-type density, not a Cantor continuum with a holonomy-invariant transverse measure, and no foliated formula admits either. But as written a reader takes it for a blanket claim about trace formulas, which is false. Add the scope sentence:

> First obstacle, named precisely: **within the foliated/laminated frameworks** ([r3s-17] chapter 4, [r3s-19] (A1), [r3s-21] Thm 2) the closed orbits are simple/nondegenerate by hypothesis, hence isolated and countable, so no published foliated trace formula admits an orbit continuum. The two nearest ancestors are (a) Leichtnam's type-II formula, which already carries the Haar-induced transverse measure and the Ruelle–Sullivan/von Neumann trace but keeps a discrete orbital sum, and (b) the classical clean / Bott–Morse (Duistermaat–Guillemin) trace formulas, in which a positive-dimensional family of periodic orbits contributes an integral over the family. DQ-M asks for the common refinement: Leichtnam's transverse measure on the orbital side of the clean case.

### 4.3 N4(c) — "has anyone proposed Haar-averaging **Deninger's** packets?" Verdict: **NOVEL — but a rival canonical resolution is in print and must be cited.**

No proposal to average Deninger's packets was found anywhere. However, a **published, canonical, equivariant map that collapses each packet to a single closed orbit already exists**, and any claim that measure-averaging is the only canonical way to absorb the packet degeneracy is false as stated. [r3s-08] Morishita, **Theorem 3.6(2), p. 25**, verbatim:

> "(2) For a prime number p, an R⁺-orbit (circle) γ_p in the packet Γ_p is sent onto the circle C_p under Ψ_Q."

with Ψ_Q the R⁺-anti-equivariant, Galois-equivariant continuous map from Deninger's system X_Q to the Connes–Consani adelic space X̄_Q constructed in [r3s-08] §3 (Lemma 3.5, Theorem 3.6(1)); the paper's abstract states the point as *"closed orbits attached to primes in both spaces are corresponding."* So the whole packet maps onto one orbit, canonically, by a map Deninger himself asked for ([x-03] §7). That is a *quotient* resolution rather than a *measure* resolution, and it lands in a space where the flow is reversed and the certified theorems of [x-03] do not transfer — but it is on the board, it is canonical, and it is 2025.

Two further published constructions in the same direction, both by Connes–Consani, both read this session:
* **arXiv:2401.08401**, *Knots, Primes and the adele class space*: the scaling site X_Q has, by construction, exactly **one** periodic orbit C_p of length log p per prime, and π^{-1}(C_p) in the adele class space is the mapping torus of the Frobenius in π₁^{ét}(Spec Z_{(p)})^{ab}.
* **arXiv:2606.06604**, *On the Absolute Geometry of Spec Z* (Connes–Consani, 4 June 2026; abstract verified this session on the arXiv abs page; full text on disk in `sources-extracted/` as a `.txt` with no accompanying PDF — **provenance not verified from a title page, so treated as non-load-bearing**): over C, at each prime, the non-trivial points of (Spec Z)_{F₁} *"canonically form two principal homogeneous spaces (torsors) over the Weil groups W_p = Q_p^× and W_∞ = C^×"*, and quotienting the archimedean orbit by the Frobenius symmetries recovers *"the adelic periodic orbit C_p = R_+^×/p^Z"*.

**Required change — MAJOR.** The 9.4 note's §7 Road 3 dismisses the Morishita bridge in one clause ("transports no usable structure … do not cite for topology"), which is right about *topology* but wrong as a summary: on the specific question Road 2 exists to answer — *how does one canonically get one orbit per prime out of a packet* — [r3s-08] Thm 3.6(2) is a published answer, and the note's framing of Road 2 as the only Aut(C)-natural exit is not sustainable without addressing it.

