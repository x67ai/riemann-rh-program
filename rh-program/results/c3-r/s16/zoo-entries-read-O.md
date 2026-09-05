# READER'S CHECK (Opus 5) OF BARRIER-ZOO ENTRIES IV.11–IV.15
## Session 16, 2026-09-06 — target `rh-program/BARRIER-ZOO.md`, entries inserted by the writer stream

**Role.** Reader/verifier, second model. For every sentence of IV.11–IV.15 I opened the record file the
entry cites, at the section it names, and checked the statement, its hypotheses, its verification tag and
its scope. I weighed no testimony from the writer's report: where the writer's report and the record
disagreed I followed the record. Repairs are applied DIRECTLY in `BARRIER-ZOO.md` as dated bracketed
notes, additions only (git diff on this pass: 4 insertions, 1 deletion — the deletion is queue item 9's
line replaced by itself plus an appended note).

**Records opened this pass, at the sections cited by the entries:**
`results/c3-r/m2c-feasibility-ledger.md` §13, §14 (+ its repair block), §15 (+ novelty and repair blocks),
§16 (S16-1 … S16-8), §16-bis (verification labels; S16-3/4/5/6 narrowings), §16-ter (§8.1–§8.4 verbatim);
`results/c3-r/s14/qstar-adjudication.md` §1 (verdict table with corrections 2 and 4 in place), §2 (with
corrections 1 and 3), §3; `results/c3-r/s14/adversarial/adjudication.md` head (model attribution), §1, §3,
§4, §4.1, §5, §7; `results/c3-r/s14/y0-witness/adjudication.md` §0.1, §4.3, §4.4;
`results/c3-r/s16/qs4prime/adjudication.md` §2 row B1, §3.1, §3.4, §5, §7 (novelty ledger N1–N12);
`refute-adjudication.md` §0, §1.1, §3.3, §3.4, §5.5, §8; `refute-F.md` §3.3 (headings), `refute-O.md`
§3.4, §7; `f1-check-O.md` §0, §1, §2, §3, §4, §5, §6, §7, §8, §9. Corpus: `fetched/x-03-…arxiv-v4.pdf`
existence and version confirmed; STATUS.md line 54 for the "45 barriers" figure.

---

## §0. VERDICT PER ENTRY

| Entry | Verdict | Why |
|---|---|---|
| **IV.11** Packet indiscreteness / X₀^E quasi-compact kill | **PASS** | Every clause tracks `qstar-adjudication.md` §1–§2 (as repaired) and `adversarial/adjudication.md` §1, §3, §4, §4.1, §5, §7. The four binding corrections are reproduced faithfully, including the inversion of the coarsening rationale and the restatement of "S4 is DEAD". Scope ((Tors); two-sided R; p. 59 topology or finer; E-free excluded) is exact. Model attributions verified at the two file headers. No repair. |
| **IV.12** Theorem T and the inert Y₀ witness | **PASS-WITH-REPAIRS** | The mathematics, the D1–D4 repairs, Theorems B/C/O-3, the novelty PARTIAL and the compact-base rider are all exact. Two precisions applied: the SOURCE parenthetical attributes Leichtnam's flow formula to three files that do not contain it (it is in `adjudication.md` §1.A/§3.4, N4); and the EXECUTABLE TEST's "σ-compact ⇒ Theorem T does not apply" is a shorthand that the STATUS rider itself states correctly. |
| **IV.13** Closed-3-manifold length-group kill | **PASS-WITH-REPAIRS** | B1 matches `adjudication.md` §2 row B1 nearly verbatim; B1′ matches `f1-check-O.md` §6.1–§6.6 and ledger §16-ter (N-2) in all three corrections (finite RANK, tangency set, transverse orbits), including the double-cover and Baire repairs and the necessary condition. One repair: the STATUS line's "not in print in this form (Session-16 novelty ledger)" is exact for B1 (row N1) and unbacked for B1′ — the refute pass carries no novelty ledger and ran no prior-art search. |
| **IV.14** Theorem A vs. fixed points on compact laminations | **PASS-WITH-REPAIRS** | (A), (B) (in the strengthened form), (C1)–(C4) with the Candel narrowing, (D) with the §4.4 hypothesis set, Corollary A.1 with Reading (iii)′, the [De02] GUARD verbatim including the never-paraphrase sentence, and the A-III fall — all confirmed against `f1-check-O.md` §1–§5, §8 and `refute-adjudication.md` §1.5/§0. Three precisions applied: the prior-art claim over-cites the novelty ledger; the C⁰-seminorm reading is flagged by the record itself as its one recalled reading; the Ĉ case is given in its two-fixed-point half only. |
| **IV.15** S4′ carries clause (0) | **PASS** | Every clause tracks `refute-adjudication.md` §1.1 (printed chain, counter-configuration, the (0-fix)/(0-coh) text, the not-added list), `f1-check-O.md` §7.1–§7.3 (ε_x on the leaf; κ_p < 0 forcing; the 2×2 table; diag(1/4,3/4)) and §5.2 (Reading (iii)′), and §5.5 for clause (iv). The RETURNED-not-refuted disposition and the "SO(2) is an axiom, or a theorem under (31)" line are both the record's own. No repair. |
| Cross-reference rows (4 new) | **PASS** | All four rows check out, including "refuter O's '(0) = (31)' frontier" (verified at `refute-O.md` §7, which proposes exactly (20)/(31) as clause (0)) and the RETURNED/AMENDED disposition of the Session-14 four-clause statement. |
| Entry count (header, line 11) | **PASS** | Heading counts in the file: I 7, II 5, III 21, IV 15, V 3 = 51, exactly as printed. STATUS.md line 54 does record "45 barriers" at Session-5 creation, and no non-Group-IV entry has been added since, so 45 → 46 (IV.10) → 51 is consistent. The zoo itself contained no stale count string. |
| Formalization queue items 8, 9 | **PASS-WITH-REPAIRS** | Item 8 states finite rank, the tangency set and transverse orbits, and carries the honest Mathlib caveat. Item 9's hypothesis-set pointer names `f1-check-O.md` §4.4, which is Theorem A **(D)**'s hypothesis set, not (A)+(B)'s; note appended. |
| Protocol step 5(e) | **PASS** (beyond brief, correctly flagged) | The appended routing sentence is dated, leaves the original step-5 text intact as prefix, and orders the five audits in a defensible sequence (topology → suspension shape → tangency rank → conformality/measure → clause (0)). Without it the checklist never reaches IV.11–IV.15. |

**Nothing in IV.11–IV.15 is FAIL.** No entry paraphrases Theorem A as "α = 1 is impossible on a compact
space"; IV.14 prints the prohibition verbatim and the [De02] guard with all four of its scope clauses.
IV.13 says finite **RANK** (never "finitely generated" as its own conclusion — it explicitly kills that
restatement) on the **tangency** set, for closed orbits **transverse to F**. IV.12 carries the compact-base
scope rider as a dated STATUS rider with its three record anchors. All five STATUS lines say
`program-adjudicated` with dual-model tags and named record files; the only `literature-verified` claim in
the block is IV.15's, and it is confined to the axiom text of (13)/(14)/(15) read on disk at r3s-20 §4.1.

---

## §1. SENTENCE-LEVEL TABLE

Verdict key: **OK** = statement, hypotheses, tag and scope all confirmed at the cited record;
**OK-p** = confirmed, with a precision recorded in §2; **n/a** = connective or cross-reference.

### IV.11 (STATEMENT / KILLS / EXECUTABLE TEST / SOURCE / STATUS)

| Sentence or clause | Record checked | Verdict |
|---|---|---|
| X₀ = X̌₀(C) ×_{Q>0} R>0 for Spec Z; [x-03] arXiv v4 = `fetched/x-03` | qstar §2 (p. 38 suspension); file present, filename ends `-arxiv-v4.pdf` | OK |
| The quotient topology on the suspension is a printed DEFINITION, [x-03] p. 59 §9 — "not a reading of record" | qstar §2 REPAIR Correction 1 (quotes p. 59 verbatim); adversarial §7 item 1 | OK |
| Two theorems hold for every admissible E ([x-03] Def. 4.1 p. 27; (Tors) in force) | adversarial §1 face-(a) row; qstar §2 admissibility bullet | OK |
| Face (a): any two points of one packet (a fortiori one closed orbit) are topologically indistinguishable; each packet and each closed orbit is indiscrete | adversarial §3 Steps 1–6 + Corollary; qstar §1 face-(a) row | OK |
| No T₀ (hence no Hausdorff/metrizable/laminated) subspace meets a packet in two points | adversarial §3 Corollary (Q-a NO) | OK |
| Holds in the p. 59 topology or any coarser one | adversarial §1 face-(a) row ("or any coarser one") | OK |
| Holds verbatim in X̌₀(S¹)×_{Q>0}R>0 and E-free X̌₀(C)×_{Q>0}R>0; never consumes (Tors) | adversarial §1 face-(a) row, last sentence | OK |
| False in the strictly finer coproduct topology of Thm. 7.10 (p. 46) — a scope boundary, not a defect | adversarial §1 face-(a) row (same wording) | OK |
| Face (b) is for X₀^E = X̌₀(C)_E ×_{Q>0}R>0, E admissible, and ONLY there | adversarial §1 face-(b) row; §5 binding text | OK |
| W := ρ̂₀·u strictly positive, l.s.c., flow-conformal of exponent one (W∘φ^t = e^tW), W = +∞ exactly on the packets | adversarial §4 (A) with the l.s.c. re-derivation and the (Tors) clause; §5 | OK |
| Every nonempty quasi-compact WHOLE-R-invariant subset lies in ⨆_p Γ^E_p and meets only finitely many packets | adversarial §4 (B) dissipation + (C) clopen separation; §5 | OK |
| Hence no continuous flow-equivariant map from a nonempty quasi-compact space with a two-sided R-action meets infinitely many packets | adversarial §4 (D); §5 | OK |
| Exclusions (i) E-free Y₀ as printed ([x-03] p. 49; [x-06] p. 12), with K = Ω ∪ ⋃_p γ_p; (ii) forward-only invariance; (iii) strictly coarser topologies | adversarial §4.1 (counterexample re-derived); §5 "Excluded from the statement" | OK |
| The kill as scoped: quasi-compact, fixed-point-free, two-sided-R-equivariant source into X₀^E, and the subspace face — NOT "S4 is DEAD" | adversarial §7 item 4 (binding restatement); qstar §1 REPAIR Correction 4 | OK |
| [x-03] p. 40 poses S4 with no compactness; X₀ has no fixed points ([x-03] p. 3 verbatim) | adversarial §7 item 4 (both quotations) | OK |
| Route 2 with target X₀^E: FAILED, `failed-ledger-exhausted`; kill-criterion FIRED | ledger §14 "Status lines" | OK |
| Four binding record corrections (1)–(4) as listed | adversarial §7 items 1–4; ledger §14 Basis | OK |
| Two escapes: unbuilt Arakelov X̄₀ ([x-03] pp. 39–40, u → 0⁺, W5) and the E-free Y₀ (IV.12's case) | ledger §14 Residue (R-i), (R-ii) | OK |
| KILLS bullet (compact/quasi-compact sub-system; Hausdorff subspace meeting a packet; topology hedges in either direction) | adversarial §1, §5, §7 items 1 and 3 | OK |
| EXECUTABLE TEST (1) state topology, check T₀/T₁ at the packets; (2) state (Tors), evaluate W, check two-sided quasi-compactness; (3) archimedean fixed points — X₀ has none | adversarial §5 and §7 item 4; §4 (A)–(D) | OK |
| SOURCE anchors: ledger §13, §14; qstar §1; adversarial §1, §5, §7; [x-03] pp. 3, 27, 39–40, 46, 49, 59; [x-06] pp. 11–12 | each opened; all present and on point | OK |
| STATUS: dual-model — Fable 5.1 (Q* adjudicator, four probes two kill/two build, converged) + Opus 5 (adversarial adjudicator, four refuters two per face on two models); theorem grade as scoped | adversarial head ("Model: Opus 5 — deliberately distinct from Fable 5.1, which authored all three prior derivations of face (a)…"); qstar §1 probe-convergence paragraph | OK |
| "Entered 2026-09-06 from the Session-14 records; no new mathematics of Session 16 is in this entry" | true of the entry as written | OK |

### IV.12

| Sentence or clause | Record checked | Verdict |
|---|---|---|
| Theorem T statement (Z any Q>0-space; X = (Z×R>0)/Q>0; relatively compact orbit ⇒ orbit not closed ⇒ X not T₁ ⇒ not metrizable ⇒ not a foliated space in [Den05] §7.1 sense, not a Riemann-surface lamination) | y0-witness §4.3, Theorem T box, verbatim | OK |
| Proof sketch (v ∉ uQ>0; q_n → u/v; subnet q_{n_j}z → w; (w,v) in the closure and not in the orbit) | y0-witness §4.3 proof | OK |
| Corollary T1: Y₀ not T₁ via z = π(1_η); Deninger's §8 is a negative result (p. 49 "still infinite-dimensional") | y0-witness §4.3 Corollary T1 | OK |
| Corollary T2: no Q>0-suspension of a COMPACT base is T₁; independent of dimension, of E, of arithmetic; explains packet indiscreteness in one line (values in fixed finite sets of roots of unity) | y0-witness §4.3 Corollary T2 | OK |
| The witness: CONSTRUCTION-REPAIRED with four repairs D1–D4 (Lipschitz tube field; explicit rank-2 normal frame in the 4-dimensional ambient; radii O(p⁻²); E-free proof of packet indiscreteness) | y0-witness §0.1 (D1–D4 substantive; D5 minor and internal to verify-F); ledger §15 | OK |
| Compact metrizable 3-dimensional space: 2-torus with irrational flow + one cabled solid torus per prime; surgery shape credited to KMNT arXiv:1906.02424 Lemma 3.2 | ledger §15 and its novelty block (credit) | OK |
| Orbit spectrum {log p}: exactly one simple closed orbit of least period log p per prime, ε ≡ +1, no fixed points | ledger §15 positive residue | OK |
| Repelling core of rate ½ ⇒ return derivative p^{1/2}·(orthogonal), \|det A_p^k\| = p^k, a [Den05] §7.5-type formula returns T1 + T2 EXACTLY = p. 33's "absolute value Np^{1/2}" | ledger §15 positive residue | OK |
| Theorem B: no foliated-space structure with 2-dimensional leaves; d = 3, d = 0 excluded outright, d = 2 by the proof, d = 1 exists but trace-formula-empty ([Den05] (32) sums over closed orbits not contained in a leaf) | ledger §14 REPAIR (1) and §15; y0-witness §4.1 | OK |
| Theorem C: decomposition Y_η ⊔ ⨆_p Y_p, Y_p clopen, Y_η into the (Tors)-violating generic locus; converse; continuity automatic (verify-O's O-3); the map pulls back nothing; the comparison map is INERT | y0-witness §4.4; ledger §15 | OK |
| Net: X₀^E killed, Y₀ inert and not a lamination, X̄₀ unbuilt; the unmet half is topological — (a) Riemann-surface-leaved structure at the accumulation set, (b) archimedean leaf with χ ≠ 0 there (limit torus has χ = 0; no fixed points) | ledger §15 "Residue, rewritten" and positive residue | OK |
| S4′ is Deninger's and Leichtnam's published open existence problem, sharpened by four clauses; anchors [x-21] 2002 = [Den05] p. 26; [x-03] p. 40; Leichtnam 2007 Open Question 2; solved case [De02] | ledger §15 REPAIR block (quotations as read) | OK |
| "now amended by clause (0) (IV.15)" | ledger §16-bis; IV.15 | OK |
| KILLS bullet (suspension of a compact base; equivariant map pulls back structure; "orbit spectrum is the hard part"; "first positive S4-shaped object") | ledger §15; §14 REPAIR (2); y0-witness §4.4 | OK |
| EXECUTABLE TEST, first half (name Z and the action; exhibit a point with relatively compact orbit) | y0-witness §4.3 | OK |
| EXECUTABLE TEST, second half ("if the base is only σ-compact … Theorem T does not apply") | adjudication.md §3.4, §5, N5 — the record's own shorthand; the precise hypothesis is a relatively compact orbit | **OK-p** (repair R-12.2) |
| EXECUTABLE TEST, comparison-map half (list the structures claimed; check against Theorem C's decomposition) | y0-witness §4.4 | OK |
| SOURCE: ledger §14 repair block, §15; y0-witness §0 (0.1–0.4), §4.1, §4.3 (with the PARTIAL novelty and the Yokoyama / Akin–Auslander / Laca–Raeburn anchors), §4.4 | all four sections opened; §0.1–§0.4 present as described; novelty PARTIAL text present | OK |
| SOURCE, scope half: `adjudication.md` §3.4 (D-IV ruling, "Theorem T should not be cited again as ruling out the suspension shape in general"), §5, N5 | adjudication.md §3.4 (line-level: the sentence is there verbatim), §5 recommendation, §7 row N5 | OK |
| SOURCE parenthetical: `refute-adjudication.md` §3.3 (γ) / `refute-F.md` §3.3 / `refute-O.md` §3.4 for the σ-compact and "compactify" quotations **and** for the flow formula φ^t(l,x) = (ψ_x^t(l), x e^{−t}) / "not the plain suspension" | the σ-compact half is in all three; the flow-formula half is in NONE of them — it is `adjudication.md` §1.A and §3.4, novelty row N4 | **OK-p** (repair R-12.1) |
| STATUS: Theorem T single-check at proof level (five-line proof), novelty dual-model-checked PARTIAL; Theorems B and C two verifiers on two models + Opus 5 adjudicator | ledger §15 ("Theorem T (adjudicator, single-check)") and §15 header ("two verifiers on two models + Opus adjudicator"); y0-witness §4.3 novelty block | OK |
| Dated compact-base rider (Theorem T assumes a compact base or a relatively compact orbit; Leichtnam 2007's L is only σ-compact and his flow is not the plain suspension; must not be cited against the suspension shape in general) | adjudication.md §3.4, §5, N5; ledger §16-bis is silent on Theorem T, so the rider's anchors are the right ones | OK |

### IV.13

| Sentence or clause | Record checked | Verdict |
|---|---|---|
| B1 hypotheses: M closed 3-manifold, F codimension-one foliation by surfaces, φ foliated flow whose non-transverse set L^∞ is a finite union of compact leaves (KMNT Def. 1.5(i); or ALKL transverse simplicity on a closed manifold); M₀ = M ∖ L^∞ | adjudication.md §2 row B1, statement paragraph (near-verbatim) | OK |
| KMNT Lemma 1.10 (unique closed ω on M₀ with ω\|TF = 0, ω(φ̇) = 1) and Def. 1.11 (Λ = [ω](H₁(M₀;Z))) | adjudication.md §2 row B1 proof (1); f1-check-O §6.1 quotes Lemma 1.10 verbatim | OK |
| ∫_c ω = ℓ(c) for a closed orbit c ⊂ M₀ of least period | adjudication.md §2 row B1 proof (2) | OK |
| Cutting along L^∞ gives a compact 3-manifold with boundary ⇒ H₁(M₀;Z) finitely generated ⇒ Λ finitely generated | adjudication.md §2 row B1 proof (3) | OK |
| Every γ_p lies in M₀ (an orbit inside a leaf gives eigenvalue 1, against clause (ii)) | adjudication.md §2 row B1 proof (4); f1-check-O §6.3 | OK |
| {log p} Z-linearly independent by unique factorization ⇒ (i)+(ii) unrealizable on M | adjudication.md §2 row B1 proof (5) | OK |
| Sharp form of [Den05] p. 24 Rem. 3 in the presence of fixed points; the escape at [x-18] p. 3 ("one must allow the flow to have fixed points") is NOT sufficient inside the KMNT/ALKL class | adjudication.md §2 row B1 "What B1 does still do"; ledger §15 novelty block quotes [x-18] p. 3 | OK |
| "B1 (dual-check)" | adjudication.md §2 row B1 tag "[dual-check, hypotheses corrected]"; the ruling that scout F's hypothesis is right and scout O's unhypothesized conclusion is not what the argument proves | OK |
| B1′: tangency set N = {x : Y_φ(x) ∈ T_xF} a finite union of leaves each with dim_Q H₁ < ∞ ⇒ the group generated by the lengths of closed orbits TRANSVERSE to F has FINITE RANK, dim_Q(Λ_{M₀}⊗Q) ≤ dim_Q H₁(M ∖ N; Q) < ∞ | f1-check-O §6.4 (corrected statement) and §6.2, §6.3; ledger §16-ter (N-2) verbatim | OK |
| KMNT's ω exists and is locally exact on M ∖ N without transverse simplicity and without compactness of the leaves in N; with C¹ data read "closed" as "locally exact" | f1-check-O §6.1 including the regularity note | OK |
| Transverse-orientation double cover; lengths ℓ or 2ℓ; finite rank descends | f1-check-O §6.5 (2) — and it is the correction of the earlier "orientation double cover" | OK |
| Closure-minimal leaf closed in the complement by Baire (closure a countable union of compact plaques of finitely many leaves), properly embedded, two-sided, product neighborhood | f1-check-O §6.5 (3) | OK |
| Mayer–Vietoris: dim H₁(W ∖ L) ≤ dim H₁(W) + dim H₁(L); iterate | f1-check-O §6.5 (4)–(5) | OK |
| "Finitely generated" is NOT derivable (Z[1/2] rank 1, not finitely generated) | f1-check-O §6.4; ledger §16-ter (N-2) | OK |
| The kill is a dimension count: {log p} Q-linearly independent, spans an infinite-dimensional Q-subspace | f1-check-O §6.4 | OK |
| Closed orbits inside N are invisible to ω; under clause (ii) there are none; with clause (i) "exactly", Λ = Λ_{M₀} = ⟨log p⟩ | f1-check-O §6.3 | OK |
| Necessary condition rank_Q H₁(M ∖ N; Q) = ∞ — N has infinitely many leaves or a leaf of infinite topological type; "one plane/disk leaf plus finitely many finite-type leaves" is dead independently of Theorem A | f1-check-O §6.6; refute-adjudication §3.4 Consequences | OK |
| Vacuity as narrowed: for S4′ + clause (0), N is never a finite union of compact or finite-type leaves; for S4′ as posed the vacuity claim is not derivable and B1 bears on its subclass | ledger §16-bis S16-3 narrowing (verbatim) | OK |
| Side note: α = 0 forced by any compact preserved leaf, so [x-06] p. 6's manifold class has α = 0; [Den05] p. 24 Rem. 2 and [x-06] p. 8 force it only under "everywhere transversal"/"no fixed points" | ledger §16-bis S16-3 narrowing, last sentence; ledger §16 S16-3; refute-adjudication §0 T6 row | OK |
| KILLS bullet (KMNT/ALKL class; any finite-type tangency set; "a plane leaf plus a few compact leaves"; "fixed points suffice"; any "finitely generated" restatement) | f1-check-O §6.4, §6.6; adjudication.md §2 row B1 | OK |
| EXECUTABLE TEST (compute N and dim_Q H₁(M ∖ N;Q); if finite the brief is dead; else route to IV.14/IV.15) | f1-check-O §6.6; ledger §16-ter §8.4 (i) | OK |
| SOURCE anchors (ledger §16 S16-3, §16-bis, §16-ter N-2; adjudication.md §2 row B1; refute-F §3.4; refute-adjudication §3.4; f1-check-O §6.1–§6.6; KMNT text on disk `kmnt.txt`) | every section opened and on point; `kmnt.txt` cited as read by both f1-check-O §6.1 and refute-adjudication §3.4 | OK |
| STATUS: dual-model (B1: scouts F and O independently + Opus 5 adjudicator; B1′: refuter F + binding adjudicator on Fable 5.1, re-derived by Opus 5 §6, flipped to BINDING in §16-ter) | ledger §16 header (scouts Opus 5 and Fable 5.1; adjudication Opus 5); f1-check-O role paragraph (refuter F and adjudicator both Fable 5.1; f1-check is the second model); ledger §16-ter enactment | OK |
| STATUS: "Sharpens a printed remark ([Den05] p. 24 Rem. 3); not in print in this form (Session-16 novelty ledger)" | novelty ledger row N1 covers B1 only; no novelty row and no prior-art search exists for B1′ | **OK-p** (repair R-13.1) |

### IV.14

| Sentence or clause | Record checked | Verdict |
|---|---|---|
| Hypothesis set "exactly as fixed in `f1-check-O.md` §4.4": X compact foliated space with Riemann-surface leaves; g in the conformal class, Candel's class C_l^∞ (Candel §1.1–1.2 pp. 491–493); [x-20] p. 30 Warning; "continuous leafwise metric" does not license Candel's theorems; (A), (B), (C1), (C4) need only continuity of g | f1-check-O §4.4 and §3.1 ("(C1), (C4) and (B) do not need it") | OK |
| φ a foliated flow = jointly continuous R-action by homeomorphisms mapping leaves to leaves, smooth along leaves ([x-20] 7.3) | f1-check-O §1 statement and §1.3 attack 3; §8.1 ("Add to the hypothesis list: φ a jointly continuous R-action") | OK |
| N = the union of the preserved leaves (closed, saturated, flow-invariant) | f1-check-O §1.1 (P1) | OK |
| (A) every positive holonomy-invariant transverse measure concentrated on N is flow-invariant; the transverse map agrees with plaque-chain holonomy ON N; holonomy invariance quantifies over all Borel sets | f1-check-O §1.2 (★) and §1.3 attacks 1–2 | OK |
| (B) φ^{t*}[λ_g] = e^t[λ_g] in H̄²_F(X) (α = 1, [x-20] p. 27 = Leichtnam (15)) ⇒ no nonzero flow-invariant holonomy-invariant transverse measure; with (A), none concentrated on N | f1-check-O §2 (statement, §2.2 proof), §8.1 (strengthened form) | OK |
| (B)'s mechanism: C_µ bounded for the C⁰ seminorm, "one of the seminorms of Deninger's Fréchet topology, [x-20] pp. 14, 29", hence descends to reduced cohomology; then (e^t − 1)m = 0 with 0 < m < ∞ | f1-check-O §2.1(a) and (b) — but §9 flags the seminorm reading as the one place relying on a standard reading of an unspecified phrase | **OK-p** (repair R-14.2) |
| "One-dimensionality of H̄²_F is not used" | f1-check-O §2.2 remark (i); §8.1 | OK |
| (C1) N contains no compact leaf | f1-check-O §3.2 | OK |
| (C2)/(C3) with g in Candel's class: no euclidean preserved leaf; every preserved leaf hyperbolic; N is a compact Riemann-surface lamination with no invariant transverse measure (Candel Cor. 4.2, p. 497) | f1-check-O §3.3 (route via Theorem 4.3's first sentence / Cor. 4.2, applied to N with vacuous hypothesis; Candel's sanction quoted at p. 497) | OK |
| (C4) for every holonomy-invariant transverse measure µ and every regular transversal T, µ(T ∩ N) = 0; equivalently the Ruelle–Sullivan measure gives N measure zero and N contributes nothing to χ_Co(F, µ) | f1-check-O §3.4 (which says "positive holonomy-invariant"); ledger §16-ter (N-5) | OK-p (wording only; noted in repair R-14.3) |
| (D) with a fixed point x_∞ on a leaf L along which (31) holds: NO OBJECT | f1-check-O §4.4, §4.6 | OK |
| (D) proof chain: similarity of ratio e^{t/2}; orientation-preserving (det continuous, nonvanishing, +1 at t = 0) hence holomorphic; \|(φ^t)′(x_∞)\| = e^{t/2} (conformal factor cancels at a fixed point) | f1-check-O §4.1, §4.2 | OK |
| Schwarz–Pick excludes hyperbolic L; automorphism groups exclude tori and C^*; Ĉ excluded by (31)-along-L alone via a Möbius one-parameter group's second fixed point (reciprocal derivative); L ≅ C excluded by (C2) — the only place (0-coh) + compactness + Candel enter | f1-check-O §4.3 — which additionally handles the PARABOLIC Möbius case (one fixed point, derivative modulus 1) | **OK-p** (repair R-14.3) |
| Corollary A.1: under (0-fix) + (0-coh) the flow is not conformal along the archimedean leaf for any t ≠ 0; Deninger's "(31) probably too strong" (Leichtnam 2007 p. 11) is "inconsistent"; second half (χ = +1 ⇒ disk) only under Reading (iii)′ | f1-check-O §5.1, §5.2; ledger §16-ter §8.1 and (N-3) | OK |
| GUARD: [De02] = [x-20] §7.7 Example pp. 34–36 read at source — compact, (31) global, α = 1, all leaves conformally C, nonzero holonomy-invariant transverse measure, NO fixed point (p. 35 verbatim) | f1-check-O §4.5 (four bullets read verbatim); ledger §16-ter §8.3 | OK |
| GUARD's scope clauses: (C2) forbids euclidean leaves only INSIDE N; (B) forbids only FLOW-INVARIANT measures; (D) is false without the fixed point | f1-check-O §4.5 items 1–3; ledger §16-ter §8.3 | OK |
| "Theorem A must never be paraphrased as 'α = 1 is impossible on a compact space': what is impossible is α = 1 together with a fixed point on a leaf along which (31) holds." | ledger §16-ter §8.3 GUARD, verbatim; f1-check-O §4.5 item 4 | OK |
| Program consequences: "conformal to C, χ = +1" STRUCK (rested on [Den05] p. 33 Rem. 7 — an expectation presupposing a transverse measure, naming no leaf, predicting hyperbolic leaves for K ≠ Q) | ledger §16-bis S16-4 narrowing; refute-adjudication §0 T1 row and §1.5 | OK |
| The archimedean part of any S4′ + clause-(0) object is a compact saturated lamination of hyperbolic preserved leaves with µ(T ∩ N) = 0 | ledger §16-bis S16-5 narrowing + §16-ter (N-5) | OK |
| A-III FELL: the only printed route (Candel via a non-hyperbolic leaf) is closed inside N by (C3); a non-preserved non-hyperbolic leaf does produce a measure and occurs in [De02] | ledger §16-ter (N-6); refute-adjudication §0 T2 row and §2 | OK |
| KILLS bullet, all six clauses incl. "existence is an axiom (Leichtnam 2008 5] / 2013 5])" and "χ = +1 by Poincaré–Hopf on a non-compact leaf" | refute-adjudication §5.5; f1-check-O §5.2 (b) | OK |
| NOT killed (guard): α = 1 on a compact space as such; euclidean non-preserved leaves; nonzero non-flow-invariant measures — [De02] the witness for all three | f1-check-O §4.5 | OK |
| EXECUTABLE TEST (write the conformality hypothesis; locate fixed points and leaves; (D); else flow-invariance on N by (A); no compact or euclidean preserved leaf; Candel regularity stated; Reading (iii)′ stated) | f1-check-O §3.1, §4.4, §5.2; ledger §16-ter (N-1), (N-3) | OK |
| SOURCE anchors (refute-F §1.5; refute-adjudication §1.5, §1.6; f1-check-O §0–§5, §8; ledger §16-bis, §16-ter; Candel pp. 490–498; [x-20] pp. 14, 21, 27, 29–36) | all opened; §1.5/§1.6 of refute-adjudication and §1.5 of refute-F exist and carry Theorem F-1 / Theorem A + Corollary A.1 | OK |
| STATUS: dual-model chain Fable 5.1 (refuter F) → Fable 5.1 (binding adjudicator) → Opus 5 (`f1-check-O.md`), enacted BINDING with the narrowings in §16-ter; surrounding block already dual-model per §16-bis | f1-check-O role paragraph; ledger §16-bis "Verification labels" and §16-ter | OK |
| STATUS: "Not in print (Session-16 novelty ledger; Leichtnam's 2007 replacement of (31) by (15) is the printed precursor)" | the printed-precursor half is exact (refute-adjudication §1.1, r3s-21 p. 11 read); the novelty-ledger half is not — §7's rows N6/N7 are the statements Theorem A narrowed and felled, and no prior-art search was run in the refute pass | **OK-p** (repair R-14.1) |

### IV.15

| Sentence or clause | Record checked | Verdict |
|---|---|---|
| S4′'s four clauses as stated in Session 14 (ledger §15) | ledger §15 "Residue, rewritten (R-ii → S4′)" | OK |
| They do NOT imply the fixed-point source property | refute-adjudication §1.1 [ADJ-B]; f1-check-O §7.3 | OK |
| [Den05] p. 33 Fact quoted; it is a one-line corollary of global (31) ("in the situation of the preceeding remark", pp. 31–33) and has no other source | refute-adjudication §1.1, with (20) p. 21, (31) p. 27, Rem. 7.6(4) p. 31, Rem. 5 p. 32, the Fact p. 33 all read | OK |
| Leichtnam 2013 (r3s-20 §4.1) prints it as the separate axiom 3] a) (13) beside 3] b) (14) and 4] (15); Leichtnam 2008 §5.1 prints only the fixed-point form (12) | refute-adjudication §1.1 (both statements, "read"); ledger §16 S16-1 | OK |
| Counter-configuration: compact preserved leaf L ≅ S², φ^t\|L the flow of z ↦ e^{t/2}z on Ĉ (source at 0, sink at ∞, no closed orbits), violating nothing in (i)–(iv) | refute-adjudication §1.1 "Counter-configuration (F's, verified)" | OK |
| Clause (0) = (0-fix) [fixed point per archimedean place in clause (iii)'s leaf; e^{−t/2}T_xφ^t\|T_xF ∈ SO(T_xF) at every fixed point; Leichtnam (13) = Deninger's Fact] | refute-adjudication §1.1 "Clause (0) to be adopted [ADJ-B, binding]"; ledger §16-bis S16-4 narrowing | OK |
| (0-coh) [H̄²_F(X) ≅ R·[λ_g] and φ^{t*}[λ_g] = e^t[λ_g]; [Den05] p. 27 = Leichtnam 4] (15)] | same records | OK |
| NOT added: (0-glob) = (31), nor "each φ^t acts on each leaf by a biholomorphism"; with a fixed point on a compact space either is inconsistent with (0-coh) (IV.14 (D), Cor. A.1); Leichtnam replaced (31) by (15) in 2007 on Deninger's advice (r3s-21 p. 11), caution repeated in 2013 Comment 6 | refute-adjudication §1.1, last two bullets | OK |
| ε_x = sign det(1 − T_xφ^t\|T_xF) on the LEAF ([x-20] p. 31 Rem. 7.6(2); normal direction split into \|1 − e^{κ_x\|t\|}\|⁻¹) | f1-check-O §7.1 (derivation and the R<0 consistency check) | OK |
| Archimedean W_p ([x-20] p. 10) has κ_p = −1 (complex) or −2 (real), both NEGATIVE ⇒ matching forces ε_x = +1 on R>0 AND det = e^t on R<0; Deninger's "fits perfectly" is sufficiency, the sign of κ_p makes it necessary | f1-check-O §7.2; ledger §16-ter §8.1 ("upgraded: … it forces it, because κ_p < 0") | OK |
| T_xφ^t\|T_xF = exp(tB): tr B = 1 and ε_x = +1 force both eigenvalues into the open right half-plane — a leafwise hyperbolic SOURCE; saddle diag(2,−1) has ε_x = −1 and is EXCLUDED; the sink is excluded by tr B = 1 | f1-check-O §7.3 table; refute-adjudication §1.1 | OK |
| Neither condition nor both forces SO(2) (B = diag(1/4, 3/4)); SO(2) is an axiom, or a theorem under (31) | f1-check-O §7.3 closing paragraph (with the [x-20] p. 33 Fact re-derived under (31)) | OK |
| Reading (iii)′: finite topological type, χ = 2 − 2g − n; χ = +1 ⇒ L ≈ R² and, hyperbolic under (0-coh), L ≅ D; infinite type ⇒ χ undefined and clause (iii) says nothing; χ = +1 not derivable from (0-fix) + "one fixed point per leaf" (Poincaré–Hopf needs control at the ends) | f1-check-O §5.2 (all three bullets and remark (b)); ledger §16-ter (N-3) | OK |
| Clause (iv) restated: existence an axiom; under clause (0) never flow-invariant; modulus exactly e^{−t}; return map at γ_p scales by 1/p (Leichtnam 2007 Lemma 6, Prop. 2); µ(T ∩ N) = 0; the ALKL parenthetical void as justification (S16-5 (α)) while the χ_Co(F,µ)δ₀ rationale ([Den05] (24) p. 23, Rem. 6 p. 33) stands | refute-adjudication §5.5 (the enacted clause, verbatim); ledger §16-bis S16-6 narrowing; §16-ter (N-5) | OK |
| Clause (ii) forces every γ_p transverse to F | f1-check-O §6.3; refute-adjudication §1.3 | OK |
| KILLS / RETURNS bullet (no clause (0) ⇒ RETURNED not refuted; source behavior from (ii) alone; "SO(2) as a consequence"; χ without Reading (iii)′; a saddle at the fixed point; (31) added globally ⇒ IV.14) | refute-adjudication §1.1 and §0 T1 row; f1-check-O §7.3 | OK |
| EXECUTABLE TEST (axiom list for (0-fix)/(0-coh) verbatim; compute B; tr B = 1 and both real parts positive; find the axiom or (31) if SO(2) is claimed; state the reading of χ; clause (iv) with modulus e^{−t}, not flow-invariant, no ALKL justification) | f1-check-O §7.3; refute-adjudication §5.5 | OK |
| SOURCE anchors (ledger §16-bis, §16-ter N-3 and the ε_x upgrade; refute-adjudication §1.1, §5.5; f1-check-O §7.1–§7.3, §5.2; r3s-20 §4.1; Leichtnam 2008 author copy §5.1; r3s-21) | all opened and on point; the 2008 author copy is recorded as saved beside the adjudication (refute-adjudication §8 read-list) | OK |
| STATUS: dual-model (clause (0) required: three independent proofs, refuter F + refuter O + binding adjudicator; ε_x forcing: adjudicator on Fable 5.1, re-derived by Opus 5, enacted §16-ter); axiom text of (13)/(14)/(15) literature-verified on disk at r3s-20 §4.1; the specification statement and the forcing computation are the program's; BINDS …; supersedes the Session-14 four-clause statement, which stands as the printed open problem sharpened | ledger §16-bis "Verification labels" paragraph; f1-check-O role paragraph (refuter O = the second model, adjudicator = Fable 5.1); ledger §16 S16-1 for the printed axiom list | OK |

### Cross-reference rows, count, queue, protocol

| Item | Record checked | Verdict |
|---|---|---|
| Row "C3-r Route 2 (solenoid intermediate → X₀^E) … FAILED — `failed-ledger-exhausted` (Session 14); kill-criterion FIRED, scoped as a (Tors)-kill → IV.11, IV.12" | ledger §14 Status lines; adversarial §1 ("(Tors)-kill" adopted as the binding characterization) | OK |
| Row "Q-S4′ on a closed 3-manifold, KMNT/ALKL class … or any finite-type tangency set — DEAD (Session 16; B1 / B1′) → IV.13" | adjudication.md §2 row B1; f1-check-O §6; ledger §16-ter (N-2) | OK |
| Row "Deninger's global (31) + an archimedean fixed point on a compact lamination with α = 1 (refuter O's '(0) = (31)' frontier; the adjudication's 'conformal to C, χ = +1' row) — NO OBJECT / STRUCK (Session 16; Theorem A(D), Corollary A.1) → IV.14 (with IV.15)" | refute-O §7 (his clause (0) IS (20)/(31) verbatim); refute-adjudication §0 Conflict 2 ("O's frontier paragraph … describes an empty class"); ledger §16-bis S16-4 STRUCK | OK |
| Row "Session-14 'S4′ as four clauses' statement (ledger §15) — RETURNED, AMENDED (Session 16) … → IV.15" | ledger §16-bis root-cause sentence and S16-4 narrowing | OK |
| Header entry count 45 → 46 → 51 with the per-group split | heading count in the file (I 7, II 5, III 21, IV 15, V 3); STATUS.md line 54 "45 barriers"; no non-Group-IV entry added since Session 5 | OK |
| Queue item 8 (IV.13, Lean-amenable with the Mathlib caveat; "finite rank" never "finitely generated"; tangency set; transverse orbits) | f1-check-O §6.4–§6.6 | OK |
| Queue item 9 (IV.14 (A)+(B), paper-certificate grade; must print the hypothesis set of `f1-check-O.md` §4.4, the §8.3 GUARD, Candel's pages) | §4.4 is (D)'s hypothesis set; (A)+(B) live at §1 and §2.1(b) | **OK-p** (repair R-Q9) |
| Protocol step 5(e), dated, routing foliated-dynamics briefs through IV.11–IV.15 in order | the ordering matches the five entries' dependency chain; original step-5 text intact as prefix | OK |

---

## §2. REPAIRS APPLIED, VERBATIM

Four notes were inserted; nothing was deleted. Three are new bullets appended after the STATUS bullet of
IV.12, IV.13 and IV.14; one is appended inline to formalization-queue item 9.

### R-12.1 and R-12.2 — new bullet at the end of IV.12

> - **[READ 2026-09-06, Opus 5: reader's check of this entry against the cited records — two precisions, both additive.] (1) CITATION. The parenthetical on the SOURCE line that reads "`refute-adjudication.md` §3.3 (γ) and `refute-F.md` §3.3 / `refute-O.md` §3.4 (Leichtnam 2007, r3s-21 p. 2 … his flow φ^t(l, x) = (ψ_x^t(l), x e^{−t}) carries a renormalization factor and is not the plain suspension)" splits over two records: the σ-compactness and "allows to compactify" quotations ARE at `refute-adjudication.md` §3.3 (γ), `refute-F.md` §3.3 and `refute-O.md` §3.4, as printed; the FLOW FORMULA φ^t(l, x) = (ψ_x^t(l), x e^{−t}) and the ruling "Leichtnam's flow is **not** the plain suspension" are not in those three — they are in `s16/qs4prime/adjudication.md` §1.A (p. 198 of the file) and §3.4, and in novelty row N4. Read the flow-formula half at `adjudication.md`, which this entry already cites for the D-IV ruling. (2) SCOPE OF THE EXECUTABLE TEST. "if the base is only σ-compact … Theorem T does not apply" is a shorthand: Theorem T's hypothesis is a point with relatively compact Q>0-orbit, so it DOES apply to a σ-compact base that carries such a point (a Q>0-fixed point suffices). σ-compactness only removes the automatic supply of one; the first half of the test (exhibit such a point) is the operative clause, exactly as the STATUS rider states it. No claim in this entry is withdrawn.]**

### R-13.1 — new bullet at the end of IV.13

> - **[READ 2026-09-06, Opus 5: reader's check — one repair to the STATUS line's prior-art claim, additive.] "not in print in this form (Session-16 novelty ledger)" is exact for B1 and NOT yet established for B1′. The Session-16 novelty ledger is `s16/qs4prime/adjudication.md` §7, whose row **N1** is B1 (finitely-many-COMPACT-leaves case, tag [dual-check], "Sharpens [Den05] p. 24 Rem. 3"). B1′ — the finite-RANK generalization to a finite-type tangency set — was derived in the later refute pass, which carries no novelty ledger: `refute-adjudication.md` §8 and `f1-check-O.md` §9 record what was READ and what was DERIVED, not a prior-art search, and neither reports one for B1′. So B1′'s non-print status is at derivation-honesty grade, not sweep grade, and the V.2 prior-art gate (online, not recalled) is OWED before B1′ is circulated or cited as new. The mathematics of B1′ is unaffected — it is dual-model and BINDING per ledger §16-ter (N-2).]**

### R-14.1, R-14.2 and R-14.3 — new bullet at the end of IV.14

> - **[READ 2026-09-06, Opus 5: reader's check — three precisions, all additive; no statement withdrawn.] (1) PRIOR ART. "Not in print (Session-16 novelty ledger …)" over-cites: the Session-16 novelty ledger is `s16/qs4prime/adjudication.md` §7, and Theorem A appears in no row of it — its rows N6 (A-II) and N7 (A-III) are the statements Theorem A NARROWED and FELLED, and the ledger predates the refute pass. The refute pass and the Opus check carry honesty sections (`refute-adjudication.md` §8, `f1-check-O.md` §9) that record derivation, not a prior-art search. So "not in print" for Theorem A (A)–(D) and Corollary A.1 is at derivation-honesty grade; the V.2 prior-art gate is OWED. The printed precursor named in the entry (Leichtnam 2007 p. 11, (31) → (15) on Deninger's advice) is read at source and stands. (2) ONE RECALLED READING INSIDE (B), flagged per standing order 5. "the C⁰ seminorm, one of the seminorms of Deninger's Fréchet topology, [x-20] pp. 14, 29" is not printed by Deninger: `f1-check-O.md` §9 flags it as "the one place where I rely on the standard reading of an unspecified phrase" — [x-20] says "the natural Fréchet topology" without listing seminorms, and (B)'s descent of C_µ to reduced cohomology depends on the sup-norm being dominated. Every construction of leafwise Fréchet topologies in the literature uses uniform convergence of leafwise derivatives, which contains the sup-norm; but a brief that needs (B) at certificate grade must pin the seminorm family. (3) THE Ĉ CASE OF (D) is stated here in its two-fixed-point half only. `f1-check-O.md` §4.3 excludes Ĉ in both halves: a Möbius map ≠ id is either PARABOLIC (one fixed point, derivative modulus 1 there) or has two fixed points with reciprocal derivatives (moduli r and 1/r) — both contradict |(φ^t)′| = e^{t/2} > 1 at every fixed point of φ^t|L, and both by (31)-along-L alone. (C4) is also stated in the record for POSITIVE holonomy-invariant transverse measures.]**

### R-Q9 — appended inline to formalization-queue item 9

> **[READ 2026-09-06, Opus 5: pointer precision, additive.] §4.4 is the hypothesis set of Theorem A **(D)**, not of (A)+(B). For the two statements this item formalizes the operative hypotheses are: (A) — X a compact metrizable foliated space with 2-dimensional leaves and φ a JOINTLY continuous R-action mapping leaves to leaves (`f1-check-O.md` §1, preliminaries (P1)–(P3); separate continuity is not enough); (B) — additionally X compact and g a continuous leafwise metric, which is what gives 0 < m < ∞ (§2.1(b)), plus the C⁰-seminorm reading of Deninger's Fréchet topology flagged in §9. Candel's regularity class is needed only for (C2)/(C3)/(D). Printing §4.4 as well does no harm; printing it INSTEAD of §1–§2 would understate what (A)+(B) need and overstate what they assume.]**

---

## §3. WHAT I DID NOT REPAIR, AND WHY

* **IV.11** — nothing found. The entry is the tightest of the five; every scope clause I tried to break
  (coarser vs. finer topology; E-free vs. admissible; one-sided vs. two-sided R; subspace vs. mapping
  face; "S4 is DEAD") is already stated in the record's own corrected form.
* **IV.15** — nothing found. The one thing I checked hardest, "SO(2) is an axiom, or a theorem under
  (31)", is exactly `f1-check-O.md` §7.3's closing paragraph, and the entry does not overstate the
  forcing (it says det = e^t and ε_x = +1 force a source, not SO(2)).
* **"(A), (B), (C1), (C4) need only continuity of g"** in IV.14 is weaker than the truth for (A) (which
  needs no g at all) and does not misstate (B) (which needs continuity of g plus compactness of X for
  0 < m < ∞). Left as printed.
* **The writer's protocol step 5(e)** goes beyond the brief but is dated, additive and necessary; I
  endorse it rather than flag it.

## §4. HONESTY — read versus recalled

Read on disk this session, at the sections cited above: `BARRIER-ZOO.md` lines 1–40 and 396–510 in full;
`m2c-feasibility-ledger.md` §§13–16-ter in full; `qstar-adjudication.md` §§1–3; `adversarial/adjudication.md`
head, §§1, 3, 4, 4.1, 5, 7; `y0-witness/adjudication.md` §0.1, §4.3, §4.4; `s16/qs4prime/adjudication.md`
§2 row B1, §3.1, §3.4, §5, §7; `refute-adjudication.md` §0, §1.1, §3.3, §3.4, §5.5, §8; `refute-O.md`
§3.4, §7 and its heading map; `refute-F.md` heading map and §3.3 (the σ-compact line);
`f1-check-O.md` §§0–9 in full; `STATUS.md` line 54; the `fetched/` listing.

Not opened this pass (and not relied on): the primary PDFs themselves ([x-03], [x-20], [x-06], KMNT,
Candel, Leichtnam) — every page anchor in the five entries was checked against the program record that
reports having read it verbatim, not re-read at the PDF. Where a record flags its own reading as
recalled rather than read (the Fréchet seminorm family, `f1-check-O.md` §9), I carried the flag forward
into the zoo rather than resolving it. That is the one place where a further source check is owed, and
repair R-14.2 says so in the entry.
