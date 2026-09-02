# NOVELTY CHECK AGAINST THE LUTZ THESIS — check F of two (standing order 7) — Session-8 claims N1–N5

**Program:** RH program, direction C3-r (geometric substrate, reduced recommission). **Session:** 14, 2026-09-02. **Author:** referee/verification agent F (Fable 5.1; one of two independent checks — nothing about the other check was assumed or consulted).
**Source under examination:** Judith Marie Lutz, *p-adic points of rational Witt spaces*, Inaugural-Dissertation, Universität Münster, 2025. On disk as `fetched-r3/r3s-23-lutz-2025-p-adic-points-rational-witt-spaces-muenster-diss-SESSION14-FETCH.pdf` (99 PDF pages, image-only) with the tesseract text `fetched-r3/r3s-23-lutz-2025-p-adic-points-rational-witt-spaces-muenster-diss-OCR.txt`. Referees read off the PDF page image: *"Erster Gutachter: Prof. Dr. Christopher Deninger. Zweiter Gutachter: Prof. Dr. Thomas Nikolaus. Tag der mündlichen Prüfung: 5. Juni 2025"* (PDF p. 2).
**Why this file exists:** `novelty-F.md` §6 item 5 and `novelty-O.md` §7 item 3 both list the thesis as UNDETERMINED — existence confirmed by search, no document reached. Check O's routing guess was: *"Scope is the local p-adic side, so it is not a plausible host for N1, N2 or N5; it could bear on N3's local half and on Road 1. Fetch it ... and re-scan for: (a) any global E-condition, (b) any descent condition beyond Galois, (c) any packet or orbit-closure statement."* Those three re-scan items are answered below (§4.2), all three negative.
**Standing order 5:** every quotation below was read from the PDF page image (the `Read` tool's page render), not from the OCR. The OCR was used only to locate passages and to build the grep table in §5; its mathematics is unreliable (superscripts, tilts, blackboard letters are garbled). Page numbers are the thesis's **printed folios**, with the PDF page in parentheses where it differs; the offset is PDF = printed + 6 throughout the body.
**Claims under review:** N1–N5 as stated in the Session-14 charter (and in `probe-9.3-a.md`, `probe-9.3-b.md`, `probe-9.3-adjudication.md`, `probe-9.4-note.md`; the claim wording used here is the charter's).

---

## 0. VERDICTS (stated first)

| Claim | Verdict w.r.t. the thesis | One-line reason |
|---|---|---|
| **N1** packet-closure law in X_0 = X(Spec Z); forcing group coker(lk_p); profinite accumulation of Frobenius return exponents | **NOVEL-w.r.t.-thesis** | The thesis never constructs, names, or topologizes X_0, Γ_p, packets, periodic orbits, or a flow. Its only "orbits" are (i) finite orbits of a profinite group acting on a ring (Thm 2.18, 2.20, pp. 11–14) and (ii) "Frobenius orbits" = Z-orbits of Frobenius translates of classical p-adic points (p. 2, Thm 5.1 p. 43). Its one density theorem (Thm B / 5.1) is an A_inf-function-separation statement about the union of all such Z-orbits inside the p-adic set X^+(V); it is not a topological closure, not about one orbit, and not archimedean. |
| **N2** X_0 non-Hausdorff along packets; closed invariant sets meeting every packet are infinite-dimensional; first alternative of Deninger's §6 question answered NO | **NOVEL-w.r.t.-thesis** | The words Hausdorff, closed orbit, flow, invariant set, dimension, sub-dynamical system do not occur. The only topology in the thesis is Chapter 8 (pp. 85–90): a metric on the p-adic quotient X^+(V)/G transported from m_V^♭ — Hausdorff by construction and on the other (p-adic) side of the program. Deninger's §6 question is not cited (the thesis cites [Den22] Chapters 1, 3–4, 13–15 only). |
| **N3** B_p = coker(Aut_ring(F̄_p) → Aut_group(F̄_p^×)) = coker(lk_p); no Aut(C)-stable one-orbit-per-packet selection; transport of mod-p additivity to C selects nothing canonical | **NOVEL-w.r.t.-thesis**, with one printed sentence the program must cite | Neither Ẑ, Ẑ×_(p), Aut(F̄_p^×), lk_p, nor any archimedean automorphism group appears. All equivariance statements are for the Galois group G of the *source* field K|K_0 (Thm 3.29 p. 26; Lemmas 6.28, 6.41; Cor. 7.3), never for automorphisms of the target C or V. On the transport clause the thesis prints the open problem, not a solution: *"It would be very valuable to find an analogous modifications of W_rat(X)(C) but currently this is not known."* (p. 2). The nearest structural analogue — a local fibration of the p-adic points over Hom(κ_0, k) with fibers (m_V(τ_0)^♭ \ {0})/O_{K_0}^× (p. 59) — is Deninger's own [Den22, Ch. 15] reproduced, local, and Lubin–Tate, not the packet base. |
| **N4** Haar-averaging the packet base; measured trace formula for a continuum of periodic orbits | **NOVEL-w.r.t.-thesis** | Haar, measure, trace, Lefschetz, transverse, foliation: zero hits in 99 pages. No averaging device of any kind. |
| **N5** one-orbit-per-prime admissible cuts exist but are non-canonical | **NOVEL-w.r.t.-thesis** | No cuts, no selection, no E-condition, no admissible class, no global object at all. "choice" occurs only inside proofs (choice of a lift, of a sequence, of a uniformizer: pp. 40, 63, 65, 69, 75, 79). |

**Net:** the thesis anticipates none of N1–N5, in whole or in part. It is a local, p-adic, Witt-vector / perfectoid / diamond study of the *p-adic* points of Deninger's rational Witt spaces; the archimedean dynamical system X_0, its packets, and its topology are outside its scope by its own declaration (p. 1: *"This thesis explores some of them in the p-adic setting."*). The DQ-L item of `probe-9.4-note.md` can be closed. Two things the program should take from it are recorded in §7: a citable printed statement that the C-side analogue of the mod-p additivity modification was unknown as of June 2025 (bears on N3's transport clause and on Road 1), and the fact that the thesis's [Den22] is the 2022 arXiv text, not the 2026 Indagationes print.

---

## 1. What the thesis does (page-cited)

**Scope sentence, p. 1 (PDF 7):** *"The work of Deninger [Den22] extending the notion of points on an arithmetic scheme using rational Witt vectors has raised many interesting questions. This thesis explores some of them in the p-adic setting."* The motivation paragraph is the only place the global picture is mentioned: *"A hypothetical means of bridging this gap between analysis and arithmetic is to associate to such an X an analytic structure incorporating both the archimedean places and the finite places above each prime p. Clearly, just looking at the points of X in the classical sense is not enough—the classical points of X = Spec(Z) over C are just one point spaces whose structure does not reflect the complexity of the Riemann zeta function."* and *"Presently, there is no satisfactory answer for what these more general spaces of C-valued points, denoted by Ẋ(C), should be."* (p. 1). The thesis then turns p-adic: *"Changing to the p-adic world, the first object to consider is W_rat(X)(C_p). For a comparison with spaces occurring in p-adic Hodge theory, this set is still too large (see [Den22, Chapter 4]). Hence, we focus on the subset W_rat(X)(O_{C_p}) or, more generally, W_rat(X)(V) for V a rank one valuation ring of mixed characteristic."* (p. 1).

**Summary paragraph.** For X a normal integral scheme over Z_p with algebraically closed function field (the category *Schemes^aic*, Def. 3.24 p. 26) and V a p-adically complete rank-one valuation ring of mixed characteristic, the thesis follows [Den22, Ch. 14] in cutting the set of V-valued points W_rat(X)(V) of Deninger's rational Witt space down, in four steps, to a set X^+(V): a continuity condition, formal inversion of the Witt Frobenius F_p (colimit), completion to all continuous maps on the tilt, and finally *"an additivity condition modulo p"* (§4.5 p. 36: *"To obtain A_inf(X) as functions on a subset of X_c^∇(V), Deninger imposes an additivity condition modulo p. ... The resulting subset in the uncompleted case turns out to be quite small (see [Den22, Proposition 15.8]). Hence, we will mostly work with the corresponding F_p-invariant subset"*), equivalently quasi-additivity *"|φ(x + y) − φ(x) − φ(y)| ≤ 1/p for all x and y in the ring"* (p. 2). The five main results, all stated on pp. 2–3 (PDF 8–9) and proved in Chapters 2, 5, 6, 7, 8:

- **Theorem A (= Thm 6.42, p. 71):** *"For X = Spec(R) and R a ring of finite type over Z_p, and C the algebraically closed quotient field of V there is an injection from the generic fibre of X^+(V) to the C^♭-valued points of the diamond given by R and the elements in the image can be characterized."* Displayed form p. 71: *"There is an injection X_0^+(V)_η := X^+(V)_η/G ↪ Spa((R_0)_p, R_0)^◇(Spa(C^♭, V^♭))."* The thesis adds (p. 2): *"This generalizes [Den22, Theorem 15.6] and demonstrates how the higher dimensional case is more complicated as the map is no longer a bijection."* The one-dimensional case X_0 = Spec(O_{K_0}) is re-proved as Thm 6.19 (p. 58): *"There is a bijection 𝔛_0^+(V)_η → Spa(K_0, O_{K_0})^◇(Spa(C^♭, V^♭))"*, both by Deninger's Lubin–Tate route (§6.3.1, pp. 58–60) and by diamonds (§6.3.2, p. 60).
- **Theorem B (= Thm 5.1, p. 43):** *"The restriction of the morphism e, see Equation 1.1, to a morphism e′: A_inf(X) → C(X^#(V), V) (1.2) is injective."* Here X^#(V) is *"the union of the Frobenius orbits coming from classical points X(V)"* (p. 2), defined on p. 43 as the set of triples (ker(j∘φ), (j∘φ)^{-1}(m_V), (j∘φ)_e ∘ F_p^m) with φ ∈ Hom(R, Z̄_p) ≅ X(Z̄_p) and m ∈ Z. The thesis's gloss, p. 43: *"This theorem implies the remarkable fact that the set X^#(Z̄_p) formed by the classical scheme theoretic points and their Frobenius translates is "A_inf(X)-dense" in X^+(V) in the following sense: a function on X^+(V) which comes from an element of A_inf(X) and which is zero on the subset X^#(Z̄_p) ⊆ X^+(V) is already zero on the whole of X^+(V)."* Proof *"Diophantine in nature"* via the reduced fiber theorem and lifting theorems (p. 2). (This is the result [x-06] p. 12 credits to her — the faithfulness of the A_inf representation.)
- **Theorem C (= Thm 7.24, p. 83):** *"There is a natural map from the set X^+(A) to the Cartier divisors of the relative Fargues-Fontaine curve given by K_0 and A^♭ which recovers for A = V a rank one valuation ring previous results from [Den22]."* Displayed p. 83: 𝔛^+(A^+)/G → Div^1(X_{S,K_0}), φG ↦ (W_{O_{K_0}}(φ)(ξ)); *"the restriction of this map to the subset corresponding to the generic fibre of 𝔛_0^+(V) recovers the map from [Den22, Chapter 15]."*
- **Theorem D (= Thm 2.20, p. 13):** *"Let S be a normal integral domain whose quotient field is algebraically closed. Let T be a ring on which a profinite group G acts with finite orbits. Then the canonical map Hom(T, S)/G → Hom(T^G, S) is a bijection."* (pp. 2–3; p. 13 states it for S *"absolutely integrally closed"*.) The thesis presents it as generalizing *"[KS16, Lemma 4.9], [Den22, Corollary 1.8], and Theorem 2.18"* (p. 13).
- **Theorem E (= Thm 8.5, p. 88):** *"If a sequence of elements in the quotient X^+(V)/G converges to an element with regard to the metric coming from the maximal ideal of V^♭, then the sequence converges everywhere pointwise and on a certain dense subset uniformly."* (p. 3). The metric is d(φG_∞, ψG_∞) = |φ(t) − ψ(t)|^♭ transported through Ψ_t: Hom_cont(κ_0[[t^♭]]^sep‾, V^♭)/G_∞ → m_V^♭ (§8.2 p. 87).

Everything above is p-adic: V is always *"a p-adically complete rank one valuation ring"* (pp. 1, 3, 43), the target of Chapter 7 is a perfectoid-type ring A^+, and the geometry is adic spaces, perfectoid spaces, diamonds and the (relative) Fargues–Fontaine curve (Chapter 6 §6.1, Chapter 7).

---

## 2. Per-claim evidence

### N1 — packet-closure law. NOVEL-w.r.t.-thesis.

*Searched for:* packet, closure (topological), orbit, periodic, flow, dense, minimal, accumulation, Frobenius, linking, Ẑ, profinite, solenoid, compact group, log, length. Hits and their meaning:

- **"orbit" (19 OCR hits)** — every one is either the finite orbit of an element of a ring under a profinite group (Thm 2.18(2) proof, p. 13: *"Let x ∈ T. Then the orbit of x under the action of G is finite. Denote the conjugate elements by x_1, …, x_n"*; Lemma 2.17 p. 10; Lemma 6.17–6.18 pp. 54–57; Def. 8.2 p. 86 *"if the group acts with finite orbits the infimum becomes a minimum"*), or the Z-orbit of a classical point under the Witt Frobenius (p. 2 *"the union of the Frobenius orbits coming from classical points X(V)"*; p. 43 *"their Frobenius translates"*). No R-flow, no periodic orbit, no orbit of X_0.
- **"closure" (41 hits)** — all algebraic or integral closure (*"algebraic closure of K_0"*, *"integral closure of R_0 in K"*, *"separable closure"*, *"topological closure which equals K̂^♭"* p. 58 — the last is the closure of a field inside a completed field, not of an orbit).
- **"dense" (14 hits)** — the A_inf-density of Theorem B (pp. 2, 43) and ordinary Zariski/topological density of point sets in proofs (pp. 46, 65, 67, 69, 77). Theorem B is the nearest-sounding statement in the thesis, so it is worth being exact about why it does not touch N1: it says that the *union over all* classical points of their Frobenius Z-orbits separates A_inf-functions on the *p-adic* set X^+(V); it says nothing about the closure of a *single* orbit, nothing about a topology on X^+(V) at all (Chapter 8 supplies one only for X_0 = Spec O_{K_0}), and nothing about the archimedean X_0 or its packets.
- **Ẑ, Ẑ×_(p), Aut(F̄_p^×), lk_p, linking, monodromy, Morishita, Connes:** 0 hits each.
- **profinite (5 hits):** only as "a profinite group G acts continuously, i.e. with finite orbits" (pp. 2, 11, 13, 14, 54) — the hypothesis of Theorem D. No profinite accumulation argument, no CRT, no Frobenius return times.

*Verdict.* Nothing in the thesis states, implies, or is a special case of the closure law, the minimality of a packet, the forcing group, or the accumulation mechanism. NOVEL-w.r.t.-thesis.

### N2 — non-Hausdorffness, infinite-dimensionality, Deninger's §6 question. NOVEL-w.r.t.-thesis.

- **Hausdorff, separated (topological sense), quotient topology, dimension, invariant set, sub-dynamical, closed orbit:** 0 hits ("separated" occurs three times, pp. 17, 18, 32, for separated presheaves and p-adically separated rings).
- **The only topology in the thesis** is Chapter 8, *"Induced topology on 𝔛^+(V)"* (pp. 85–90): *"The aim of this chapter is to investigate a possible notion of convergence on 𝔛^+(V)/G. For 𝔛 the normalization of Spec(Z_p) in an algebraic closure of Q_p and G the Galois group, there is a bijection (see [Den22, Chapter 15]) with the space m_V^♭. The latter can be endowed with a topology coming from the rank one valuation ring V."* (p. 85). This is a metric (p. 87), hence Hausdorff, on a p-adic quotient. It is on the other side of the program from N2.
- **Adjacent-only remark, for completeness.** Example 8.3 (p. 86) — *"We give an example that convergence in the quotient by a group action is weaker than convergence in the quotient topology of the topology of pointwise convergence"* — is a two-line observation about quotients of function spaces by a transitive finite group action (Z/pZ on itself), not about X_0, flows, or non-Hausdorff quotients. It does not bear on N2.
- **Deninger's §6 question ([x-03] p. 40)** is not cited: the thesis's citations of [Den22] are to Chapters 1, 3–4, 13, 14, 15 and to specific items (Lemma 1.7, Cor. 1.8, Thm 1.5, Prop. 1.3, Thm 13.3, Def. 14.2, 14.5, 14.12, Prop. 14.13, Prop. 15.8, Thm 15.6, Eq. 145) — all read from the page images listed in §6.

*Verdict.* NOVEL-w.r.t.-thesis.

### N3 — packet base as a cokernel; Aut(C) no-go; transport of mod-p additivity to C. NOVEL-w.r.t.-thesis, with one sentence to cite.

- **The cokernel identity.** Aut(F̄_p^×), Aut(F̄_p), Ẑ×_(p)/p^Ẑ, coker, lk_p: 0 hits. "Aut(" occurs twice, both on p. 26, for G = Aut(K|K_0) with K an algebraic closure of the function field K_0 — the Galois group of the *source*. Thm 3.29 (p. 26, presented as *"[Den22, Theorem 13.3]"*): *"the canonical map Ẋ(V)/G = W_rat(𝔛)(V)/G → W_rat(𝔛_0)(V) is an F_p-equivariant bijection"*, glossed p. 27: *"studying the V-valued points of the normalization in an algebraic closure is a feasible approach, as we can come back to the V-valued points of the scheme by looking at the quotient modulo the Galois group."* This is the p-adic counterpart of the passage from X to X_0, not the packet base.
- **Nearest structural analogue (adjacent, not anticipating).** In §6.3.1 (p. 59), reproducing [Den22, Ch. 15], the p-adic points of Spec O_{K_0} are fibered over the finite set Hom(κ_0, k) with fibers a punctured tilted disk modulo the local units: *"Looking at the quotient by G we obtain a bijection Hom_cont(κ_0[[t^♭]]^sep‾, V^♭)/G → ∐_{τ_0 ∈ Hom(κ_0,k)} m_V(τ_0)^♭/O_{K_0}^×"*, with *"Γ := G/G_∞ = Gal(K_∞|K_0) ≅ O_{K_0}^×"* acting through the Lubin–Tate endomorphisms τ_0([γ]). The acting group here is the local unit group O_{K_0}^× via a chosen Lubin–Tate law, and the thesis records the dependence (p. 58: *"Choose a Lubin-Tate formal group law over O_{K_0}"*), but draws no conclusion about canonicity or selection. It is a different base (finite, Hom(κ_0,k)), a different fiber, a different group, on the p-adic side. It does not anticipate B_p = coker(lk_p).
- **The Aut(C) no-go.** Every equivariance statement in the thesis is for G acting on the source (Lemma 6.28 p. 64 *"The map ς is G-equivariant"*; Lemma 6.41 p. 70 *"There exists a canonical G-equivariant injection"*; Cor. 7.3 p. 75 *"natural G-equivariant bijection"* — *"Here, the action of G on Ẋ(A^+) is defined by precomposition."*; Thm 3.29). The thesis states the role of G once and plainly, p. 10: *"To come back to the original ring one can look at the fixed points of the action of the Galois group of the field extension."* The automorphism group of the target (C, V, C^♭) is never considered; "selection", "canonical choice", "one orbit per" do not occur. The trichotomy D1–D3 has no counterpart.
- **The transport clause.** The thesis contains the clearest printed statement I have seen that the C-side analogue of the mod-p additivity modification is open — p. 2 (PDF 8): *"This enhanced set of V-valued points is denoted by X^+(V) and is endowed with a bijective Frobenius. It still contains all ordinary points, so the desirable properties mentioned earlier hold. It would be very valuable to find an analogous modifications of W_rat(X)(C) but currently this is not known."* That is not an anticipation of N3's negative (that the transport selects nothing canonical); it is a statement, refereed by Deninger in June 2025, that no such transport was known. The program's N3 discussion should cite it as the printed status of the problem.

*Verdict.* NOVEL-w.r.t.-thesis. Action: cite Lutz 2025 p. 2 in the N3 / Road-1 text as the printed "currently this is not known" for the C-side modification.

### N4 — Haar-averaging; measured trace formula. NOVEL-w.r.t.-thesis.

Haar 0, measure 0, trace 0, Lefschetz 0, transverse 0, foliat 0, Fuller 0, average 0, integral (in the measure sense) 0 — the thesis has no analysis of this kind anywhere; its "analytic" content is p-adic convergence (Chapter 8). NOVEL-w.r.t.-thesis.

### N5 — one-orbit-per-prime admissible cuts. NOVEL-w.r.t.-thesis.

No global object, no condition E, no admissible class, no cut, no selection (0 hits for "select", "cut", "admissible", "condition E"). The only conditions imposed on point sets are the local ones of Chapter 4 (continuity, Frobenius inversion, completion, additivity mod p), each attributed to [Den22, Ch. 14]. NOVEL-w.r.t.-thesis.

---

## 3. Does the thesis treat the archimedean / C-valued points?

**No, beyond two sentences of framing.** (i) p. 1, the Motivation, quoted in §1 — the archimedean places and Ẋ(C) are named as the goal *"presently"* without *"satisfactory answer"*, and the thesis turns to C_p in the next paragraph. (ii) p. 2, the sentence *"It would be very valuable to find an analogous modifications of W_rat(X)(C) but currently this is not known."* (iii) p. 1 also records the Kucharczyk–Scholze deformation-retract fact for C-points of Spec of a field with all roots of unity, and their negative result *"the Steinberg relations do not hold in sheaf cohomology with rational coefficients, which is a deficit of the space."* Nothing else. **Notational trap for a grep:** the letter C in Theorem 2.18 (p. 11), Theorem 2.20's proof (p. 14), Theorem 3.29 (p. 26), Theorem 5.1 (p. 43) and throughout Chapter 6 denotes the algebraically closed *p-adic* quotient field of S or V (*"C the algebraically closed quotient field of V"*, p. 2), not the complex numbers. The 24 OCR hits for "(C)" are of this kind except the five on pp. 1–2.

## 4. Other items the charter asked to record

### 4.1 "Stronger descent" condition
**Absent.** "descent"/"descen": 0 hits. "strong": 6 hits, all *"strongly Noetherian"* (Tate rings, pp. 52–53, 62). The only descent-like mechanism is Galois descent in the form of Theorem D (Hom(T,S)/G ≅ Hom(T^G,S)) and its Huber-pair extension (Lemma 6.17–6.18, pp. 54–57), which is the Kucharczyk–Scholze / Deninger Lemma 1.7–Cor. 1.8 pattern generalized, not a new descent condition.

### 4.2 Check O's three re-scan items (`novelty-O.md` §7 item 3)
(a) global E-condition — **none** (no global object). (b) descent condition beyond Galois — **none** (§4.1). (c) packet or orbit-closure statement — **none** (§2, N1).

### 4.3 Packets, orbit closures, Haar measure, trace formulas
None, anywhere (grep table §5). The thesis uses "Frobenius orbits" once (p. 2) for the Z-orbits X^#(V), and Deninger's Ch. 15 fibration over Hom(κ_0,k) (p. 59), and that is the whole of its orbit vocabulary.

---

## 5. Grep hit table (OCR text, case-insensitive; pages converted to printed folios)

| Term | Hits | Where / what it means |
|---|---|---|
| packet | 0 | — |
| closure | 41 | all algebraic / integral / separable closure of fields and rings (pp. 3, 4, 7, 10, 13, 26, 27, 31, 40, 41, 43–46, 57, 58, 61, 62, 73, 85); none topological-dynamical |
| Hausdorff | 0 | — |
| Haar | 0 | — |
| trace | 0 | — |
| orbit | 19 | finite orbits of a profinite group on a ring (pp. 2, 4, 10, 13, 14, 54, 56, 57, 59, 86); "Frobenius orbits" = Z-orbits of Frobenius translates (p. 2; Thm 5.1 p. 43) |
| linking | 0 | — |
| Frobenius | 45 | Witt-vector Frobenius F_n / F_p and its formal inversion (§3.2.1 p. 24, §4.3 p. 34, §7.2 Def. 7.9 p. 78); Frobenius-equivariant bijections (pp. 26, 38); perfectoid Frobenius (pp. 52, 62, 82) |
| descent | 0 | — |
| additive | 7 | "additive modulo p" / quasi-additivity: the [Den22, Def. 14.5] condition (pp. 1–3, 6, 18, 29, 36–37, 80–81) |
| Teichmüller | 0 | (the multiplicative map is written [·], never named) |
| selection / select | 0 | — |
| dynamical | 1 | only the title of [Den22] in the bibliography (p. 91) |
| periodic / period | 0 / 5 | "period" only in *infinitesimal period ring* A_inf (pp. 3, 4, 29) |
| flow / suspension / solenoid / compact group / Ẑ | 0 | — |
| measure / Lefschetz / foliat / transverse / Fuller | 0 | — |
| archimedean | 2 | p. 1 (motivation: "both the archimedean places and the finite places"); p. 82 ("non-archimedean field") |
| complex number(s) / C-valued | 1 / 3 | p. 1 only |
| Aut( / automorphism | 2 / 4 | p. 26 only: G = Aut(K\|K_0), source Galois group; p. 29 "it is not an automorphism" (Frobenius on X_c(V)) |
| Galois | 17 | source Galois group G of K\|K_0 throughout (pp. 1, 3–5, 7, 10, 11, 27, 57, 60, 61, 73, 85) |
| equivariant | 9 | F_p- and G-equivariance of the constructed maps (pp. 26, 38, 59, 61, 64, 70, 71, 75, 76) |
| profinite | 5 | hypothesis "profinite group acting with finite orbits" (pp. 2, 11, 13, 14, 54) |
| roots of unity | 3 | p. 1 (KS16 setting), p. 63, p. 79 (p^n-th roots of unity in R, in proofs) |
| choice / canonical | 8 / 36 | "choice" only inside proofs (pp. 40, 63, 65, 69, 75, 79); "canonical" = canonical maps/bijections of the theory, never a canonicity-of-selection discussion |
| Deninger / Den22 | 20 / 39 pp. | cited on pp. 1–4, 6, 7, 9–11, 13–15, 17, 19, 20, 22, 24, 26, 29, 31, 33–38, 51, 58, 59, 64, 77, 81–83, 85 (the bibliography's own list, p. 91) |
| Morishita / Connes / Consani / Leichtnam / Kordyukov / Álvarez López / Bost / class field / knot / monodromy / adele | 0 | — |
| Kucharczyk / KS16 | 7 | pp. 1–3, 11, 13, 14 (Lemma 4.9 generalized by Thm D); bibliography p. 91 |
| Fargues / Scholze | 18 / 7 | Fargues–Fontaine curve (Chs. 6–7); [FFC18], [FS24], [Far17], [Sch12], [Sch22], [SW20], [BMS19] |
| zeta / Riemann | 3 / 2 | p. 1 only (motivation) |

---

## 6. Bibliography entries relevant to the program (read from the page images, pp. 91–92 = PDF 97–98)

The bibliography has 25 entries (16 on p. 91, 9 on p. 92). Relevant ones, verbatim:

- **[Den22]** *"Christopher Deninger. Dynamical systems for arithmetic schemes. 2022. arXiv: 1807.06400 [math.DS] (cit. on pp. 1–4, 6, 7, 9–11, 13–15, 17, 19, 20, 22, 24, 26, 29, 31, 33–38, 51, 58, 59, 64, 77, 81–83, 85)."* — the only Deninger dynamical-systems paper cited; dated 2022 (an arXiv version), not the 2026 Indagationes print.
- **[CD13]** *"Joachim J. R. Cuntz and Christopher Deninger. An alternative to Witt vectors. arXiv: Number Theory (2013) (cit. on p. 36)."*
- **[KS16]** *"Robert A Kucharczyk and Peter Scholze. Topological realisations of absolute Galois groups. Conference on the Cohomology of Arithmetic Groups on the occasion of Joachim Schwermer's 66th birthday. Springer. 2016, pp. 201–288 (cit. on pp. 1–3, 11, 13, 14)."*
- **[FFC18]** Fargues–Fontaine (with Colmez's preface), *Courbes et fibrés vectoriels en théorie de Hodge p-adique*, Astérisque 2018; **[FS24]** Fargues–Scholze, *Geometrization of the local Langlands correspondence*, arXiv:2102.13459; **[Far17]** Fargues arXiv:1705.01526; **[Sch12]**, **[Sch22]** (arXiv:1709.07343), **[SW20]** Scholze / Scholze–Weinstein; **[BMS19]** Bhatt–Morrow–Scholze arXiv:1602.03148; **[BIM18]** Bhatt–Iyengar–Ma; **[Ked15]** Kedlaya; **[Hub93]**, **[Wed19]** (adic spaces); **[Kum52]** Kummer (cited p. 20).
- **Not cited:** Morishita (any), Álvarez López–Kordyukov–Leichtnam (any), Connes–Consani (any), Deninger arXiv:2301.11643, arXiv:2508.05329, arXiv:2204.02714, Leichtnam, Kim, Ueki, Deninger–Kucharczyk. The thesis therefore carries no citation-graph route to the dynamical or class-field-theoretic literature that N1–N5 live in.

---

## 7. Notes for the adjudicator

1. **DQ-L closes.** The thesis is entirely on the p-adic side, as Check O guessed; the three items it was to be re-scanned for are all absent (§4.2). No claim's verdict in `novelty-F.md` or `novelty-O.md` changes on account of it.
2. **One citation to add.** In the N3 / Road-1 discussion of transporting the local mod-p additivity principle to C, cite Lutz 2025 p. 2 — *"It would be very valuable to find an analogous modifications of W_rat(X)(C) but currently this is not known."* — as the printed, Deninger-refereed status of the problem as of June 2025. It supports the program's framing that the transport is nontrivial; it does not decide the program's negative.
3. **A citation to correct if it is used.** `novelty-O.md` §7 gives the thesis's title as *p-adic points of rational Witt spaces* via [D25]'s [Lut25]; `novelty-F.md` §6 item 5 has *"p-adic points of rational Witt schemes"* from a search summary. The title page (PDF 1) reads **"p-adic points of rational Witt spaces"**; Münster, 2025; oral examination and promotion 5 June 2025 (PDF 2).
4. **What the thesis's "Frobenius orbits" are**, so nobody later mistakes them for packets: Z-orbits {P ∘ F_p^m : m ∈ Z} of a p-adic point under the Witt Frobenius (p. 43); discrete, one per classical point, no flow, no length.
5. **Version of [Den22].** The thesis works from the 2022 arXiv text. Where the program relies on the 2026 Indagationes print (z-19) for wording, the thesis's citations of chapter and theorem numbers ([Den22, Thm 13.3], Def. 14.5, Prop. 15.8, Thm 15.6) are to the arXiv numbering; Check O reported that intro and §8 wording is identical between v4 and print, and nothing here depends on the difference.

---

## 8. Pages read as page images (standing order 5)

PDF pages 1–2 (title, referees); 7–10 (printed 1–4: Introduction — motivation, Theorems A–E, overview, notation); 16 (printed 10: Cor. 2.15, Prop. 2.16, Lemma 2.17); 17–20 (printed 11–14: §2.3, Thms 2.18–2.20, Cor. 2.21); 32–33 (printed 26–27: Def. 3.24, Lemma 3.27, Notation 3.28, Thm 3.29); 35 (printed 29: Chapter 4 opening); 42 (printed 36: §4.5 Additivity modulo p); 49 (printed 43: Chapter 5 opening, Thm 5.1, A_inf-density gloss); 63–66 (printed 57–60: end of proof of Thm 6.15, §6.3 classical case, Thm 6.19, §6.3.1 Lubin–Tate route, §6.3.2 diamonds); 70 (printed 64: Lemma 6.28); 76 (printed 70: Lemma 6.41, §6.4.5); 77 (printed 71: Thm 6.42); 81 (printed 75: Def. 7.2, Cor. 7.3); 89 (printed 83: Thm 7.24); 91–94 (printed 85–88: Chapter 8, Defs. 8.1–8.2, Example 8.3, §8.2 metric, Lemma 8.4, Thm 8.5); 97–98 (printed 91–92: bibliography). Thirty-one pages in all. The OCR text was read in full for pages 1–10 and 96–99 and grepped for the rest; no quotation above is taken from the OCR.
