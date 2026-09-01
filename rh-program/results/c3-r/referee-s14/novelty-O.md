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

Given N1, this is an immediate consequence of Deninger's own §8: a closed invariant set meeting every packet contains every packet (N1), hence contains the union of all periodic orbits, hence contains its closure Y₀ = X̌₀(S¹) ×_{Q>0} R^{>0} ([x-03] Thm 8.2, p. 50, unconditional for one-dimensional X₀ flat over spec Z via [Per11, Theorem 1] — read at p. 49: *"If spec A is a non-empty open subscheme of spec o_κ for some number field κ, then the set M in Claim 8.1 is always infinite, and it even has a positive Dirichlet density. This follows from [Per11, Theorem 1]."*), which [x-03] p. 49 says is "still infinite-dimensional". [x-06] **p. 12** repeats the point in the author's own words (vision-verified): *"The space X_{0E} is infinite dimensional if dim X₀ ≥ 1 and one could hope that the sub-dynamical system obtained as the closure of the union of all its compact orbits might be significantly smaller. **However, this is not the case** as follows from [Den22a, Theorem 8.2]."* So the only content beyond [x-03] §8 / [x-06] p. 12 is N1 itself plus a dimension argument.

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
* [x-03] **§6, p. 38**: "…Γ_{x₀} fibres over Ẑ^×_{(p)}/p^Ẑ = Aut(F̄_p^×)/Aut(F̄_p) with fibres the R^{>0}-orbits in Γ_{x₀}." (the tail of the sentence beginning "Thus all R^{>0}-orbits in Γ_{x₀} are circles R^{>0}/N x₀^Z and…")
* [x-06] **p. 12** (the italicised statement of Theorem 4.2), **vision-verified off the rendered page** because the text layer drops the × superscript: "In fact Γ_{x₀} is a fibre space over the compact group Aut(F̄_p^×)/Aut(F̄_p) where p = char κ(x) with fibres the compact orbits in Γ_{x₀}."
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

The same is in the founding paper of that literature, fetched and read this session: **Einsiedler–Lindenstrauss–Michel–Venkatesh, *The distribution of periodic torus orbits on homogeneous spaces*, arXiv:math/0607815v1 (= Duke Math. J. 148 (2009)), printed p. 3**, verbatim:

> "The periodic H orbits naturally come in **packets**, with all orbits in a packet sharing the same discriminant, regulator, and even shape. These packets can be understood as projections to Γ\G of orbits of adelic Q-tori on G(Q)\G(A). **The compact orbits belonging to a single packet are therefore parameterized by a finite abelian group – a suitable class group.**"

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

---

## 5. N5 — Theorem C: one-orbit-per-prime admissible cuts exist, are non-canonical, and forfeit the certified theory. Verdict: **NOVEL** (theorem); the conclusion is Deninger's own stated position.

### 5.1 What is new
The **exponent-reachability computation** — that the minimal admissible class of a chosen injective character χ^{a₀} reaches exactly the base classes a₀·p^Ẑ, so the bare letter of [x-03] Def. 4.1 permits a class whose packet locus is a single orbit per prime — is not in the literature. Nothing resembling it was found in any source. Log entries S-17, S-18, S-23.

### 5.2 What is not new: the conclusion
Every qualitative component of Theorem C's *verdict* is Deninger's own, in print, in his own words. All four read this session from the on-disk PDFs, footer-verified pages:

* **[x-03] p. 5** (introduction): *"There is a minimal condition E for which our theorems hold but **it does not look natural**. So this aspect is unsatisfactory."*
* **[x-03] p. 27** (§4, immediately before Definition 4.1): *"**The best condition on the characters P^× is not clear to me.** However the following two minimal conditions play an important role…"*
* **[x-03] p. 29** (§4, Remark): *"Incidentally, in the p-adic case where we will deal with multiplicative maps P into a p-adic valuation ring and N₀ = p^Z, the right condition E is the following: **P is additive mod p**. This can be rephrased in terms of absolute values and translated to the case where C is the complex number field. **However the resulting class E is not N-invariant.**"*
* **[x-03] p. 99** (§14, Remark after Def. 14.12): *"**I do not know how to transport such conditions to the points of X̌(C)**, where X is a scheme of finite type over spec Z and C is the complex number field."*
* **[x-06] p. 11**: *"In general, the dynamical system (X₀, φᵗ) has **too many periodic orbits**, since the N-space W_rat(X₀)(C) does not know enough about the addition in O_{X₀}. In the local p-adic situation below, we know the right modification to make. **However in the global case presently we can only impose an 'admissible' condition E** on the characters P^× …"*

Positive half likewise published: [x-03] **Theorem 5.2** (p. 34) already gives that packets are *full* whenever E ⊇ E_f, i.e. that no designated system cuts a packet.

**Required change — MINOR.** Theorem C should be stated as *supplying the theorem behind Deninger's stated intuition*, with the four quotations above cited at the point where the note says the cuts are "precisely Deninger's 'does not look natural'". The programme documents already gesture at this; the citation should be page-anchored rather than paraphrased, because the paraphrase currently reads as though the programme discovered the unnaturalness.

**One further note.** [x-06] p. 13 supplies a published *diagnosis* of the same defect that the programme should cite alongside Theorem C, since it is the author's own account of why no character-level condition can fix it: *"The absence of the Steinberg relations in rational cohomology is an indication that the space X_F(C) and hence also our space W_rat(X)(C) do not encode enough information about the additive structure of F resp. O_X."*

---

## 6. COMPLETE SEARCH LOG

All network queries were run 2026-09-01T20:2x–21:2x UTC = 2026-09-02 local. "no hit" means: no source stating or containing the claim under test; incidental hits on the primary sources themselves are not counted as hits.

### 6.1 Citing-literature enumeration (the backbone of the NOVEL verdicts)

| id | engine / endpoint | query | result |
|---|---|---|---|
| S-01 | Semantic Scholar Graph API, `paper/arXiv:1807.06400/citations` | citations of the preprint | **4 citing works**: Deninger *Primes, knots and periodic orbits* (2301.11643); Haran, *Non-Additive Geometry and Frobenius Correspondences* (2209.08536); Deninger, *There is no Weil-cohomology…* (2204.02714); *Knots and Primes: On the arithmetic of Toda flows* (2023, no arXiv id) |
| S-02 | Semantic Scholar Graph API, `paper/DOI:10.1016/j.indag.2024.05.007/citations` | citations of the published version | same 4 |
| S-03 | OpenAlex, `works?search=…` then `works?filter=cites:W2884984338` | citations of the published version | 2: Deninger 2204.02714 (Ann. SNS Pisa) and the *Introduction* chapter of the ÁLKL Springer LNM volume |
| S-04 | Crossref, `works/10.1007/978-3-032-15413-2_1` | identify that chapter | Álvarez López–Kordyukov–Leichtnam, *A Trace Formula for Foliated Flows*, Lecture Notes in Mathematics, Springer Nature Switzerland, 2026 — i.e. the book form of [r3s-17] |
| S-05 | zbMATH REST API, `/document/8143081` | the paper's zbMATH record + review | Indag. Math., New Ser. **37**, No. 1, 25–136 (2026); full reviewer text retrieved and read — **no mention of orbit closures, packet minimality, minimal sets, or Hausdorffness** |
| S-06 | zbMATH REST API, `/document/_search` | "Deninger dynamical systems arithmetic schemes" | 6 records, all already known to the programme |
| S-07 | Google Scholar (WebFetch) | `"Dynamical systems for arithmetic schemes" Deninger` | **BLOCKED** — 302 to `google.com/sorry` captcha. Cited-by list not obtained. |
| S-08 | zbMATH Open web (WebFetch) `zbmath.org/?q=an:8143081` | citation list | **BLOCKED** — HTTP 403 |
| S-09 | arXiv Atom API | `all:"Deninger"`, 60 most recent | 60 records; every one with dynamical/foliation content identified and triaged (see §7 open items) |
| S-10 | arXiv Atom API | `abs:"foliated dynamical"` | 9 records: 2508.15971, 2410.20758, 1912.02159, 1906.02424, math/0605724, 1308.3535, 1104.4852 + 2 unrelated |
| S-11 | arXiv Atom API | `abs:"foliated flow" AND abs:"trace formula"` | 4: 2402.06671, 2304.00798, 2112.03191, 1308.0637 |
| S-12 | arXiv Atom API | `abs:"arithmetic topology" AND abs:"dynamical"` | 3, all known |
| S-13 | arXiv Atom API | `abs:"rational Witt"` | 9; the only relevant are 1807.06400 and Kucharczyk–Scholze 1609.04717 |
| S-14 | arXiv Atom API | `abs:"Deninger's"` | 40; triaged, nothing new |
| S-15 | arXiv Atom API | `abs:"packets of periodic orbits"` | **1 record on all of arXiv**, and it is nlin/0307025 (semiclassical wave packets, Lorentz gas) — the phrase is unused in mathematics outside this programme |
| S-16 | arXiv Atom API | `abs:"scaling site"` | 11; the Connes–Consani cluster, all opened (§6.4) |

### 6.2 Web searches (deliberately varied vocabulary, per the charter)

| id | engine | phrasing | result |
|---|---|---|---|
| S-17 | WebSearch | `Deninger "dynamical systems for arithmetic schemes" packet periodic orbit closure minimal set` | no hit |
| S-18 | WebSearch | `arXiv 1807.06400 Deninger cited by orbit closure non-Hausdorff suspension packets` | no hit |
| S-19 | WebSearch | `"rational Witt vectors" Deninger dynamical system "periodic orbits" closure "Cantor" profinite Frobenius density` | no hit |
| S-20 | WebSearch | `"1807.06400" OR "Deninger" "packets of periodic orbits" arithmetic scheme lamination one orbit per prime` | no hit |
| S-21 | WebSearch | `Deninger packets periodic orbits average Haar measure "one orbit" prime selection condition E admissible` | **HIT** → Khayutin arXiv:1510.08481 (homogeneous-dynamics packet average; §4.1); followed to its source, ELMV arXiv:math/0607815 (fetched and read; §4.1) |
| S-22 | WebSearch | `trace formula flow "continuum of closed orbits" transverse measure lamination foliated Lefschetz degenerate family` | **HIT (context)** → Leichtnam math/0603576, ÁLKL 2402.06671, ÁLKM 2410.20758, Kim 1912.02159; none states the claim |
| S-23 | WebSearch | `"Kucharczyk" "Scholze" topological realisation absolute Galois group space non-Hausdorff orbit closure profinite` | no hit (their X_F is compact **Hausdorff**, so the phenomenon cannot occur there) |
| S-24 | WebSearch | `Connes Consani "Knots, primes and class field theory" arXiv Regulators V Pisa` | **HIT** → arXiv:2501.06560, Contemp. Math. (Regulators V) |
| S-25 | WebSearch | `Judith Lutz Münster thesis "rational Witt" p-adic points Fargues-Fontaine Deninger dissertation` | partial — project title located ("Rational Witt Spaces and their Relation to the Fargues–Fontaine Curve", Ada Lovelace Fellow, Deninger's group, uni-muenster.de news item 2022); **no thesis document located** → UNDETERMINED, §7 |
| S-26 | WebSearch | `Lefschetz trace formula flow "manifold of closed orbits" clean intersection Duistermaat Guillemin integral over family periodic orbits` | **HIT** → Zelditch, arXiv:math/0402356 (clean / Bott–Morse case; §4.2(iii)) |
| S-27 | WebSearch | `suspension solenoid "Cantor set" family of periodic orbits same length non-Hausdorff quotient "orbit closure" dense Frobenius profinite arithmetic` | no hit |
| S-28 | WebSearch | `Deninger foliated space "one closed orbit for each prime" obstruction packets too many orbits problem` | no hit |
| S-29 | WebSearch | `"closure of a periodic orbit" OR "orbit closures" Deninger arithmetic scheme "packet" suspension "Q>0" Witt` | no hit |
| S-30 | WebSearch | `"is not Hausdorff" Deninger dynamical system arithmetic scheme suspension periodic orbits not closed` | no hit |
| S-31 | WebSearch | `Deninger packets "uncountably many" periodic orbits per prime Cantor group circles arithmetic dynamical system defect` | no hit |
| S-32 | WebSearch | `Deninger "admissible" class of characters condition E choose one character per prime dynamical system subsystem "not natural" selection` | no hit |
| S-33 | WebSearch | `Deninger Singhof "dynamical trace formulas" transverse measure suspension foliated Lefschetz note` | context only (Deninger–Singhof counterexample to smooth leafwise Hodge decomposition; ÁLKL *Simple foliated flows*) |

### 6.3 Consensus (MCP paper search, 220M-paper index)

| id | query | result |
|---|---|---|
| S-34 | `Deninger dynamical system arithmetic scheme packet periodic orbits closure Hausdorff foliated` | 10 results; the relevant ones are all already on disk (2508.15971, 1906.02424, 1807.06400/Indag., 2410.20758, 1912.02159, math/0603576, Deninger's surveys) **plus one new item**: B. Morin, *Sur l'analogie entre le système dynamique de Deninger et le topos Weil-étale* (2010) — about the **conjectural** system, eight years before the W_rat construction; cannot contain the claims |
| S-35 | `trace formula foliated flow continuum of closed orbits transverse measure on family of periodic orbits` | 10 results; nothing with a continuum on the orbital side. Notable near-misses recorded for the file: Álvarez López, *A trace formula for foliated flows via adiabatic limits* (2007, no periodic orbits at all in the stated case); Miyanishi, *Circle Foliations Revisited: Periods of Flows whose Orbits are all Closed* (2024/2025) — flows all of whose orbits are closed, Wadsley/Besse circle-foliation theory; **that is the smooth analogue of a packet, and it carries no trace formula of the required type** |

### 6.4 On-disk corpus searches (grep over `pdftotext` extractions made by me this session)

Corpora searched: all of `fetched/x-01…x-24` (the Deninger/Weil-étale cluster) + `fetched/z-19` (the **published** Indagationes version) + all of `fetched-r3/r3s-01…r3s-22` + `fetched-r2/r-09` (Morishita, *Knots and Primes*, 2nd ed.) + `fetched-r2/r-26b` (Morishita 2009 survey) + `sources-extracted/connes-consani-jacobian-specZ-JNcG2026.pdf` + `sources-extracted/connes-zeta-spectral-triples-2026.pdf`, plus the four papers I fetched fresh (1510.08481, math/0607815, 1912.02159, 1906.02424, 2501.06560, 2401.08401, math/0402356, 1906.06753).

| id | term(s) | files containing it | outcome |
|---|---|---|---|
| S-36 | `packet` | x-03 (5×), x-06 (1×), z-19 (5×), r3s-08 (7×) — plus Ichino–Ikeda (unrelated sense: Vogan/L-packets) | every occurrence read; none is a closure, minimality or measure statement |
| S-37 | `orbit closure`, `minimal set`, `dense orbit` | **zero occurrences in the whole Deninger/Morishita cluster** | — |
| S-38 | `non-Hausdorff` / `Hausdorff` | r3s-17 (14×), r3s-18 (11×), x-03 (14×), z-19 (13×), x-06 (3×), r3s-19 (1×) | all read; [x-03]/[z-19] prove Hausdorffness for X̊(C), X̊₀(C), X̌(C), X̌₀(C) (Cor. 7.8/7.9) and **never** discuss the suspension; see §2.1 |
| S-39 | `continuum of periodic orbits`, `one closed orbit`, `one periodic orbit` | zero, zero, one (z-19, unrelated) | — |
| S-40 | `transverse measure` | r3s-17 (3×), r3s-20 (1×), r3s-21 (9×), x-20 (5×), x-21 (5×) | all read; the type-II/Ruelle–Sullivan machinery is present, the orbital side is always a discrete sum (§4.2) |
| S-41 | `Haar` | x-03 (1×), z-19 (1×), r3s-21 (4×), CC-Jacobian (1×), x-22/x-23 (2× each) | none is a measure on a packet or on a family of closed orbits |
| S-42 | `linking number` | r-09, r-26b, r3s-08, x-06 | Morishita's lk_p line only; no orbit-closure statement |
| S-43 | `coker`, `cokernel` | **zero occurrences in r3s-08**; the same group appears as a quotient in [x-03] p. 2 / p. 38 and [x-06] §4 | the "cokernel" phrasing is new, the object is not (§3.1) |
| S-44 | `irreducible`, `properly discontinuous` | x-03 pp. 49, 63, 64, 76 | the decisive N2a anchors (§2.1) |
| S-45 | `infinite dimensional` / `infinite-dimensional` | x-03: exactly 3 occurrences, all prose | no dimension theorem — observation in §2.2 |

### 6.5 Individual documents opened to test a specific hypothesis

* **arXiv:2510.19456** — probe B's own residual watch item ("surfaced by query (iii), content unexamined", `probe-9.3-b.md` line 141). **DISCHARGED:** it is J. M. Fraser and Yunlong Xu, *Dimensions of orbital sets in complex dynamics* (22 Oct 2025) — backwards orbits of compact sets under rational maps on the Riemann sphere; no arithmetic, no foliations, no Deninger. Probe B's residual obligation on that item can be closed.
* **arXiv:1912.02159** (J. Kim) and **arXiv:1906.02424** (Kim–Morishita–Noda–Terashima, Münster J. Math. 14(2) 2021) — fetched and searched; both work inside smooth 3-dimensional foliated dynamical systems with the usual simplicity hypotheses; neither touches W_rat(X)(C), packets, orbit closures or Hausdorffness.
* **arXiv:2501.06560** ([CC3]) and **arXiv:2401.08401** — fetched and searched: the string `packet` occurs **zero** times in each; `Hausdorff` occurs once in each, both times asserting that a *quotient of theirs is* Hausdorff (properness argument). Their C_p is one orbit per prime by construction.
* **ICMS abstract, `icms.ac.uk/.../Christopher-Deninger.pdf`** — fetched by curl and extracted; it is the talk abstract for the same paper, 1016 characters, no additional mathematical content.
* **Kucharczyk–Scholze** was tested only through S-23 and through [x-03]/[x-06]'s descriptions of it; their space is compact Hausdorff with no flow, so it is not a candidate host for N1/N2.

---

## 7. UNDETERMINED items and coverage gaps (for the sponsor, standing order 1)

Named so a later session can see exactly what was and was not covered.

1. **Google Scholar "cited by" for arXiv:1807.06400 / Indag. Math. 37 (2026) 25–136 — NOT OBTAINED.** WebFetch on `scholar.google.com` returns 302 → `google.com/sorry` captcha (S-07). Scholar's index is materially broader than Semantic Scholar's or OpenAlex's for this paper (both of which returned only 2–4 citing works). **This is the single largest gap in the sweep.** Recommend the sponsor pull the Scholar cited-by list by hand and hand it back; until then the NOVEL verdicts on N1, N2c, N3(ii), N5 rest on the S2/OpenAlex/arXiv-metadata enumeration, which is consistent but thin.
2. **zbMATH Open citation list — NOT OBTAINED.** `zbmath.org/?q=an:8143081` returns HTTP 403 to WebFetch (S-08); the free REST API exposes the record and the review but no "cited in" endpoint. The review itself was retrieved and is negative evidence (S-05).
3. **J. Lutz, PhD thesis, Universität Münster** — project title located ("Rational Witt Spaces and their Relation to the Fargues–Fontaine Curve", Ada Lovelace Fellowship in Deninger's group; uni-muenster.de news item of 18 May 2022), **no document located** (S-25). Cited as [Lut25] in [D25] = arXiv:2508.05329, and [x-06] p. 12 credits her with proving the A_inf representation faithful. Scope is the **local p-adic** side, so it is not a plausible host for N1, N2 or N5; it could bear on N3's local half and on Road 1. Fetch it (miami.uni-muenster.de is the Münster repository) and re-scan for: (a) any global E-condition, (b) any descent condition beyond Galois, (c) any packet or orbit-closure statement.
4. **ÁLKL, *A Trace Formula for Foliated Flows*, published Springer LNM volume (2026), DOI 10.1007/978-3-032-15413-2** — I read only the on-disk arXiv **v1** (`r3s-17`, arXiv:2402.06671v1). The book could carry an added remark on non-simple or non-isolated closed orbits that the v1 does not. Narrow risk, affects only N4(b)'s "no published foliated formula" clause. Fetch and re-check that one clause.
5. **[CC3] Connes–Consani, *Knots, primes and class field theory*** — I read arXiv:2501.06560v1. The **published** version is Contemp. Math. (Regulators V), AMS; I did not obtain it. The arXiv version contains no packet or orbit-closure content, so the risk is small.
6. **`sources-extracted/arxiv-2606.06604-…-fulltext.txt`** is a bare text file with **no PDF on disk**; its provenance cannot be verified from a title page. The arXiv abstract page was fetched this session and matches (Connes–Consani, *On the Absolute Geometry of Spec Z*, 4 June 2026), but the file is treated as **non-load-bearing** and nothing in §§1–5 depends on it. Recommend promoting the actual PDF to `fetched-r3/` if the programme wants to cite it.
7. **Not searched, and deliberately so:** paywalled review databases other than zbMATH (MathSciNet is permanently closed and discharged per `corpus-routing.md` caveat 13); non-English literature beyond what the indices surfaced; seminar-talk video (a Deninger talk recording surfaced in S-17 and was not viewed — talks are not citable prior art under standing order 5, but if the sponsor wants the belt-and-braces version it is `youtube.com/watch?v=T13Bha0hs7I`, "Dynamical systems for arithmetic schemes, Christopher Deninger, 10/03/2023").

---

## 8. EVERY DOCUMENT OPENED IN THIS SWEEP

**Programme documents (read in full or to the extent needed).**
`results/c3-r/probe-9.3-adjudication.md` (full); `results/c3-r/probe-9.4-note.md` (full); `results/c3-r/probe-9.3-a.md` (§§0–2 in full, plus the novelty-claim lines 67, 117, 155); `results/c3-r/probe-9.3-b.md` (the prior-art paragraph, line 141); `results/corpus-routing.md` (header caveats 1–20, as required before citing any corpus file).

**On-disk primary sources (own `pdftotext` extractions made this session; page anchors as stated).**
* `fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf` — pp. 2 (by vision), 5, 27, 29, 38–40, 49–50, 63–64, 76, 99, 101, 103.
* `fetched/z-19-deninger-2026-dynamical-systems-arithmetic-schemes-INDAG-published.pdf` — title page, introduction, §6, §7, §8 (the published Indag. Math. 37 (2026) 25–136 version; **confirmed to agree with arXiv v4 on every point at issue**).
* `fetched/x-06-deninger-2024-primes-knots-and-periodic-orbits.pdf` — §§3–4, pp. 10–13.
* `fetched/x-05-deninger-2025-bsd-for-dedekind-zeta-functions.pdf` — searched; no packet/orbit content.
* `fetched/x-01a, x-01b, x-02, x-04, x-07…x-24` — text-searched as a block (S-36…S-45); the Deninger surveys x-17…x-24 were searched for `transverse measure`, `packet`, `Hausdorff`, `dense`.
* `fetched-r3/r3s-08-morishita-deninger-cc-bridge-2508.15971.pdf` — §§1.2, 2.2, 2.3, 3 (pp. 2, 6–7, 16, 24, 25).
* `fetched-r3/r3s-17-…2402.06671v1….pdf` — chapter 1 and chapter 4 (the simplicity definitions).
* `fetched-r3/r3s-18-…2304.00798v1….pdf`, `fetched-r3/r3s-19-…2410.20758v1….pdf` (Introduction, (A1), Lemma 2.2), `fetched-r3/r3s-20-…1307.3851v1….pdf`, `fetched-r3/r3s-21-…math0603576v2….pdf` (transverse-measure construction, Lemma 6, Theorem 2), `fetched-r3/r3s-22-…2508.05329v1….pdf` (searched; no dynamical content).
* `fetched-r2/r-09-morishita-2024-knots-and-primes-2nd-ed-BOOK.pdf`, `fetched-r2/r-26b-morishita-2009-analogies-between-knots-and-primes-arxiv-0904.3399v1.pdf` — searched.
* `sources-extracted/connes-consani-jacobian-specZ-JNcG2026.pdf` (title page + searched), `sources-extracted/connes-zeta-spectral-triples-2026.pdf` (searched), `sources-extracted/arxiv-2606.06604-…-fulltext.txt` (searched; **provenance-flagged**, §7 item 6).

**Fetched fresh this session (into the session scratchpad; none promoted to the corpus — that is the sponsor's call).**
* arXiv:1510.08481 — Khayutin, *Arithmetic of Double Torus Quotients and the Distribution of Periodic Torus Orbits* (PDF; p. 5 quoted).
* arXiv:math/0607815 — ELMV, *The distribution of periodic torus orbits on homogeneous spaces* (PDF; p. 3 quoted).
* arXiv:math/0402356 — Zelditch, *Survey of the inverse spectral problem* (PDF; §8.1, PDF p. 78, and p. 21 quoted).
* arXiv:2501.06560 — Connes–Consani, *Knots, primes and class field theory* (PDF; searched).
* arXiv:2401.08401 — Connes–Consani, *Knots, Primes and the adele class space* (PDF; searched).
* arXiv:1912.02159 — J. Kim (PDF; searched). arXiv:1906.02424 — Kim–Morishita–Noda–Terashima (PDF; searched).
* arXiv:1906.06753 — ÁLKL, *Simple foliated flows* (PDF; abstract and contents read).
* `icms.ac.uk/.../Christopher-Deninger.pdf` (talk abstract).
* arXiv abs pages fetched: 2510.19456, 1510.08481, 1912.02159, 1906.02424, 2606.06604.

---

## 9. CONSOLIDATED FINDINGS, WITH SEVERITY

**MAJOR — the note must change.**
1. **N3(i) is ANTICIPATED verbatim.** The "structural identity" B_p = coker(Aut_ring → Aut_group) is Deninger's own displayed formula in the introduction of [x-03] (p. 2), repeated at p. 38 and in [x-06] §4 and in the published version. Replacement text supplied in §3.1. The mathematics is untouched; the novelty framing ("derived", "hereby explained", "design constraint") must be rewritten around the citation.
2. **N4(a): "Haar-average the packet (new in this note)" is not sustainable.** The identically-named object with the identically-defined canonical average measure is standard in homogeneous dynamics (ELMV, math/0607815 p. 3; Khayutin, 1510.08481 p. 5). Only the transplant is new. Replacement text supplied in §4.1.
3. **N2(a): non-Hausdorffness is not itself the discovery.** Deninger states the cause twice ([x-03] pp. 49, 76), warns that the leaf bijections are not homeomorphisms (p. 63), and proves an irreducible T₁ — hence non-Hausdorff — quotient of the same shape (Prop. 10.3, p. 64), and uses it. The increment is the *location* (inside one packet), the *consequence* (no periodic orbit is closed), and the witness. Also: the claim **contradicts** [r3s-08] Thms 2.2.8/2.2.9's "homeomorphism" wording, and the record should say "in conflict with", not only "not in the literature". §2.1.
4. **N4(c): a rival canonical packet-collapse is in print.** [r3s-08] Theorem 3.6(2), p. 25: every orbit of Γ_p maps onto the single Connes–Consani circle C_p under a canonical, Galois-equivariant, flow-anti-equivariant continuous Ψ_Q. Road 2 cannot be presented as the only Aut(C)-natural way to absorb the packet without addressing it. §4.3.

**MINOR — citation and scope repairs.**
5. N1: credit [x-03] p. 2 and [r3s-08] §2.2 for the packet base and lk_p; "the forcing group is coker(lk_p)" is a relabelling of published data. §1.3.
6. N4(b): add the scope sentence supplied in §4.2 — the "no published trace formula" clause is defensible only inside the foliated/laminated frameworks, and the two ancestors (Leichtnam's measured type-II formula; the clean/Bott–Morse case) must be named. Deninger's own "reminiscient of invariant tori" ([x-03] p. 2) points at the clean case and should be quoted where DQ-M is posed.
7. N5: page-anchor Deninger's four remarks ([x-03] pp. 5, 27, 29, 99; [x-06] p. 11) at the point where the note says the cuts are "precisely Deninger's 'does not look natural'". §5.2.
8. N3(ii): cite the classical inputs (cyclotomic + Steinitz surjectivity of Aut(C) → Ẑ^×; discontinuity of wild automorphisms) and present Prop. 1 as explaining [x-03] Thm 5.2 rather than as an independent obstruction. §3.2.

**Observation for the adjudicator (not a novelty finding, but it bears on which half of N2b is new).**
9. [x-03] never proves the infinite-dimensionality it asserts: the phrase occurs three times, all in prose, and there is no dimension theorem. If probe B's Corollary B consumes "[x-03] §8's still-infinite-dimensional line" as an input, it is consuming an assertion. Probe A's n-cell construction (Theorem B(b)) may therefore be the only theorem-backed route to N2b — which raises, not lowers, the priority of the dedicated referee pass the adjudication already owes it (§4 item 6 there). §2.2.

**Closure of an outstanding programme obligation.**
10. Probe B's residual watch item, arXiv:2510.19456 ("surfaced by query (iii), content unexamined"), is **discharged**: it is Fraser–Xu, *Dimensions of orbital sets in complex dynamics*, and is irrelevant. §6.5.

---

*— end of novelty sweep, check O —*
