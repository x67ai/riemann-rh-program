# REPAIR PASS — Session 14 wording repairs applied as dated blocks (2026-09-03)

**Program:** RH program, direction C3-r. **Session 14, 2026-09-03.** **Agent:** repair-pass agent (Claude Fable 5.1).
**Convention applied:** every repair is a block headed `**[REPAIR 2026-09-03 — Session 14 repair pass]**`, inserted immediately after the line it applies to; it states the finding, the replacement text, and the source. No existing text was deleted or rewritten; every earlier dated block (`[REFEREE PASS 2026-09-02 …]`, `[NOVELTY — dual-model check 2026-09-02/03]`) is intact. Replacement texts are quoted verbatim from the source records; where a source gives only an instruction, the minimal sentence was written and marked "[repair-pass wording]". No theorem, number or verdict was touched. U.S. English throughout.
**Method:** an anchor-based insertion script (scratchpad `repair_pass.py`, `repair_pass2.py`) that validates every anchor line as unique before writing anything, then inserts from the bottom of each file upward. 49 blocks, 14 files. The diff is insertion-only (numstat in §3).

---

## 1. Sources verified on disk during this pass (standing order 5)

- **Hurewicz–Wallman, *Dimension Theory* (1941; rev. ed. 1948)** — `fetched-r3/r3s-27-hurewicz-wallman-1941-dimension-theory-princeton-SPONSOR-PURCHASE.pdf` (purchased copy; PDF page = printed page + 8). Re-read this pass: printed p. 42 = PDF 50, "COROLLARY. The Euclidean n-cube has dimension n." (folio "42 … [CH. IV"); printed p. 26 = PDF 34, "Theorem III 1. A subspace of a space of dimension ≤ n has dimension ≤ n." (folio "26 … [CH. III"); printed p. 67 = PDF 75, "Theorem V 8. Covering Theorem. A space has dimension ≤ n if and only if every covering has a refinement of order ≤ n." (folio "§9] … 67"). The ≤ signs are garbled in the text layer; the wording matches `dim-cube-source.md` §2.2's transcription from the (deleted) scan.
- **[x-20] = Den05** — `fetched/x-20-deninger-2005-arithmetic-geometry-and-analysis-on-foliated-spaces.pdf`: the "Fact In the situation of the preceeding remark, ε_k(γ) = +1 …" and "complex conjugate numbers of absolute value Np^{1/2}" sentences re-located at PDF p. 33 (printed = PDF), the remark itself starting on p. 32. (`results/corpus-routing.md` has no [x-20] row; the `fetched/` file name is the path of record.)
- **[ÁLKL23] arXiv v1 vs v3** — v1 = `fetched-r3/r3s-18-…-arxiv-2304.00798v1-SESSION8-FETCH.pdf`; v3 fetched this pass from `arxiv.org/pdf/2304.00798v3` with a retry loop (scratchpad `alkl/2304.00798v3.pdf`, 748,540 bytes, CreationDate 2024-06-04 — the same file `w3-adjudication.md` §6 row C12 records). Both extracted with `pdftotext -layout`; every numbered statement of §§6–8 matched by text (difflib ratio after stripping equation numbers). Two v3 numbers (Cor. 6.14, Claim 6.46) additionally read in the published PDF `s14/novelty/ALKL-2024-topology-conormal-distributions-PUBLISHED-JPDOA-15-47.pdf`. The derived map is the table in the `w3-adjudication.md` §9 block; summary: §6 statements shift +2 from Prop. 6.8 and +3 from Cor. 6.24 (v3 inserts Cor. 6.26); §7 statements are unchanged through Prop. 7.4, shift +2 from Cor. 7.11 (v3 inserts Cor. 7.11 and Cor. 7.20, both "totally reflexive"), +3 from Cor. 7.28 (v3 inserts Cor. 7.30); Prop. 8.8 keeps its number but is reworded ("The bottom row of (8.4) is exact" → "The dual-conormal sequence of M at L is exact"); §§3–4 unchanged. One inferred entry ((6.46) → (6.47)) and one unverified tag ((7.38)) are marked as such in the block.
- All other quotations were taken from the source records named in the table (which read them on disk on 2026-09-02/03), not from memory.

---

## 2. Every repair: source → target → status

| # | Source | Repair | Target file + section | Status |
|---|---|---|---|---|
| A-R1 | `referee-s14/novelty-adjudication.md` §3 R1 (MAJOR) | Replacement paragraph "The structural identity underneath (Deninger's own …)"; §4 Consequence 1 parenthetical → "This is Deninger's displayed quotient, [x-03] p. 2"; §9 design constraint opens "Deninger's identity … generalizes as follows [judgment-grade]" | `probe-9.4-note.md` §0 (after the 2026-09-02 NOVELTY block), §4 Consequence 1, §9 (after the NOVELTY block) | APPLIED (3 blocks; §0 text verbatim) |
| A-R2 | §3 R2 (MAJOR) | Road 2 heading/opening replaced by "Road 2 — renounce selection; take the canonical packet measure. …"; §0 third paragraph's Road-2 clause → "(Road 2) renounce selection; the canonical packet measure (standard in homogeneous dynamics; transplanted here)" | `probe-9.4-note.md` §7 Road 2 (combined block with R3, after the NOVELTY block), §0 "What survives as positive road" | APPLIED (2 blocks; verbatim) |
| A-R3 | §3 R3 (MAJOR) | "First obstacle, named precisely: within the foliated/laminated frameworks …" | `probe-9.4-note.md` §7 Road 2 | APPLIED (verbatim, in the R2/R3 block) |
| A-R4 | §3 R4 (MAJOR) | Appended clause on [r3s-08] Thm 3.6(2) p. 25 as a published rival packet-collapse | `probe-9.4-note.md` §7 Road 3 | APPLIED (verbatim) |
| A-R5 | §3 R5 (MAJOR) | The "Deninger states the cause … New here: …" sentence preceding the non-Hausdorff claim; "New negative structural datum" → "new localization and consequence" | `probe-9.3-adjudication.md` §4 item 3; `probe-9.3-b.md` Cor. A.2 and §9 item 2 | APPLIED (3 blocks; verbatim). The ledger row W12 text is the sponsor's per the source — not touched. |
| A-R6 | §3 R6 (MINOR) | "the forcing group is Deninger's packet base Ẑ^×_(p)/p^Ẑ = coker(lk_p)", cited [x-03] pp. 2, 33, 38; [r3s-08] p. 16 | `probe-9.3-adjudication.md` §2/§4 item 1; `probe-9.3-b.md` §5.4 | APPLIED (2 blocks) |
| A-R7 | §3 R7 (MINOR) | Cite [x-03] p. 33 and Kucharczyk–Scholze pp. 6, 71 as the germ of Lemma D(iii); Lemma C's classical inputs; Prop. 1 as explaining Thm 5.2 | `probe-9.4-note.md` §5 (after the NOVELTY block) | APPLIED (quotations from the adjudication's §2 N3ii; connective wording marked) |
| A-R8 | §3 R8 (MINOR) | Five quotations ([x-03] pp. 5, 27, 29, 99; [x-06] p. 11) in place of the paraphrase; cite [x-06] p. 13 alongside | `probe-9.3-a.md` §0 item 3, §4.2 | APPLIED (2 blocks) |
| A-R9 | §3 R9 (MINOR) | One sentence: [x-03] pp. 2–3 / [x-06] p. 12 are set-level statements ("bijection", p. 38); only [r3s-08]'s "homeomorphism" wording (W11) is contradicted | `probe-9.3-b.md` Cor. A.2; `probe-9.3-adjudication.md` §4 item 3 | APPLIED (inside the R5 blocks; repair-pass wording) |
| A-R10 | §3 R10 (bookkeeping) | [Lut25] on disk and scanned; watch item discharged; [D25] promoted in Session 8 | `probe-9.4-note.md` §1, §8 item 3 (DQ-L) | APPLIED (2 blocks) |
| A-§8 | `novelty-adjudication.md` §8 (+ `novelty-lutz-O.md` §6 item 2) | Cite Lutz 2025 p. 2 ("It would be very valuable … currently this is not known") in the Road-1/D3 text; present D3 as the negative answer to a stated desideratum | `probe-9.4-note.md` §0 (D3), §4 Consequence 2, §7 Road 1 | APPLIED (3 blocks; quotation verbatim, connective wording marked) |
| B-(b2) | `referee-s14/dim-cube-source.md` §4 | Ready-to-install (b2) text, adapted per the tasking to cite Hurewicz–Wallman from the purchased copy r3s-27 (p. 42 Corollary; p. 26 Thm III 1; p. 67 Thm V 8) with r3s-25 as free corroboration; [RU] label dropped | `probe-9.3-a.md` §3 Theorem B(b), after the (b3) line of the replacement statement | APPLIED (the r3s-27 clauses are marked repair-pass wording; the rest is the source's §4 text) |
| B-M-4 | `dim-cube-source.md` §4 (amendments) → `A-thmB-adjudication.md` M-4 | [RU] discharged; §3.10 sentence amended (HW III 1, IV 1 + Cor., IV 2, V 8 verified and on disk; Engelking 3.1.4 left [RU]); §7 "(b2) [RU-conditional …]" → "on disk: [r3s-27] …; [r3s-25] Thm 7(i),(iii)"; §8 action item DONE | `referee-s14/A-thmB-adjudication.md` §4 (after the table), §3.10, §7, §8 | APPLIED (4 blocks) |
| C-1 | `s14/adversarial/adjudication.md` §7.1 | Quotient topology is source-grade: [x-03] p. 59 definition quoted verbatim; "judgment-grade, flagged" withdrawn | `s14/qstar-adjudication.md` §2 (last bullet), §11; `s14/qa-kill.md` §9.4(i); `s14/qa-build.md` §2.3, §10.2 | APPLIED (5 blocks) |
| C-2 | §7.2 | Strike/re-scope the Y₀ clause → "and for Y₀^E := (X̌₀(S¹) ∩ X̌₀(C)_E)×_{Q>0}R>0 ⊆ X₀^E", E-free Y₀ noted as counterexample; novelty items 3/6/9/10 re-scoped (item 10 → "compactness, given (Tors) at the generic point") | `s14/qstar-adjudication.md` §1 verdict table (block after the table), §4(D), §9 (novelty ledger); `m2c-feasibility-ledger.md` §13 (block pointing to §14/§15) | APPLIED (4 blocks). The C3 direction-file "frontier" text named in §7.2 was not in this pass's target list — DEFERRED to the orchestrator (see §4). |
| C-3 | §7.3 | Coarser-topology rationale inverted for face (b); the two faces pin the topology to p. 59's | `s14/qstar-adjudication.md` §2, §11 (+ note in `qa-build.md` §10.2) | APPLIED (inside the C-1 blocks) |
| C-4 | §7.4 | "S4 is DEAD" restated as the death of the quasi-compact, fixed-point-free, two-sided-R equivariant-source construction inside X₀^E; two escapes named | `s14/qstar-adjudication.md` §1 verdict table; `m2c-feasibility-ledger.md` §13 (pointer; §14 already enacts it) | APPLIED |
| D-strike | `s14/y0-witness/adjudication.md` §5, §4.1, §0.1 | Strike "lamination" for the witness and "first positive S4-shaped object" in ledger §14 | `m2c-feasibility-ledger.md` §14 (end) | APPLIED (dated block; §15's replacement phrases used) |
| D-D1–D4 | `s14/y0-witness/adjudication.md` §0.1 | Record the four construction repairs D1–D4 | `s14/adversarial/face-b-refuter-F.md` §3.4 | APPLIED (D1–D4 quoted verbatim; KMNT Lemma 3.2 credit and "not a lamination" noted) |
| E-C1 | `s14/novelty/adjudication.md` §3 R1 (MAJOR) | Items 1–2: credit [x-03] p. 61 (coarse topology by strong approximation), pp. 63–64; Yokoyama vocabulary; item 2 "credited, not novelty" | `s14/qstar-adjudication.md` §9 (after the NOVELTY block) | APPLIED (in the §9 block) |
| E-C3/C4 | §3 R5 (MODERATE) | Name Akin–Auslander Thm 6.3 / Antosiewicz–Dugundji as the classical parallelizable datum; Theorem 2 follows from the weight | `s14/qstar-adjudication.md` §4 (after the NOVELTY block) and §9 items 4/5/8; `s14/qa-kill.md` §10 item 9 | APPLIED (3 blocks) |
| E-C5 | §3 R4 (MODERATE) | Kim arXiv:1712.04181 Thms 2.1/2.2/3.2 for the mapping-torus cohomology (§3, §10 item 1); Fuller 1966 p. 838 for the index form (§10 item 4) | `s14/dqm-adjudication.md` §3 (after the NOVELTY block), §10 (after the NOVELTY block) | APPLIED (2 blocks; quotations from the adjudication's §2 C5) |
| E-C5(c) | §3 R7 (MINOR) | Segal's Haar-on-cosets evaluation; present the ℤ-valued-measure lemma as an observation | `s14/dqm-adjudication.md` §10 item 5 | APPLIED |
| E-C6 | §3 R2 (MAJOR, source integrity) | "(v1) = (v3 = published)" for every [ÁLKL23] §6/§7 statement; renumbering entered at v3 (1 Jun 2024); full map derived from v1 vs v3 | `s14/w3-adjudication.md` §0 (after the NOVELTY block), §3.5, §9 (after the NOVELTY block: the table) | APPLIED (3 blocks; map derived this pass, §1 above) |
| E-C6(ii) | §3 R6 (MODERATE) | N7 sentence: acyclicity of the model spectra follows from the printed compact-spectrum sentence plus Prop. 5.6; new is the (M\*) verification | `s14/w3-adjudication.md` §9 (second block, after the map) | APPLIED (verbatim) |
| E-C2 | §3 R7 (MINOR) | Cite Yokoyama Lemma 7.2 / Akin–Auslander 6.3 for the criterion; [x-03] p. 64 + LR00 Lemma 3.1 as the printed contrast; no conflict | `s14/y0-witness/adjudication.md` §4.3 (after the NOVELTY block) | APPLIED |
| E-C8 | §3 R7 (MINOR) | Hofmann–Morris Thm 8.22 via Lewis–Mader p. 2 as an ingredient at B9 | `referee-s14/A-thmB-adjudication.md` §7 (after the NOVELTY block) | APPLIED |
| E-C9 | §3 R3 (MAJOR) | Re-attribute the p^{1/2}·O return-derivative clause to [Den05] pp. 32–33 ([x-20]); credit KMNT Lemma 3.2 for the surgery shape; [x-18] p. 3 cited in ledger §15 | `s14/y0-witness/verify-O.md` §9 item 2; `s14/y0-witness/adjudication.md` §7 (after the NOVELTY block); ledger §15 block carries [x-18] p. 3 | APPLIED (2 blocks + §15) |
| E-C10 | §3 R3 (MAJOR) | Dated block "S4′ is Deninger's printed desideratum (2002/2005) and Leichtnam's Open Question 2 (2007), re-scoped" with the quotations; solved case [De02] = [x-22]; Leichtnam 2005 axiom list SPONSOR-FETCH | `m2c-feasibility-ledger.md` §15 (end of file) | APPLIED |

**Count:** 49 blocks applied across 14 files; 0 repairs refused. One item deferred (C-2's direction-file clause, §4).

---

## 3. `git diff --numstat` after all edits (from the repo root; insertions / deletions)

```
6	0	rh-program/results/c3-r/m2c-feasibility-ledger.md
9	0	rh-program/results/c3-r/probe-9.3-a.md
4	0	rh-program/results/c3-r/probe-9.3-adjudication.md
6	0	rh-program/results/c3-r/probe-9.3-b.md
34	0	rh-program/results/c3-r/probe-9.4-note.md
12	0	rh-program/results/c3-r/referee-s14/A-thmB-adjudication.md
8	0	rh-program/results/c3-r/s14/adversarial/face-b-refuter-F.md
7	0	rh-program/results/c3-r/s14/dqm-adjudication.md
4	0	rh-program/results/c3-r/s14/qa-build.md
5	0	rh-program/results/c3-r/s14/qa-kill.md
25	0	rh-program/results/c3-r/s14/qstar-adjudication.md
44	0	rh-program/results/c3-r/s14/w3-adjudication.md
4	0	rh-program/results/c3-r/s14/y0-witness/adjudication.md
3	0	rh-program/results/c3-r/s14/y0-witness/verify-O.md
```

Every touched file shows 0 deletions; nothing had to be reverted and redone.

---

## 4. Not applied, and why

1. **`directions/C3-geometric-substrate.md` ("C3 frontier text").** `s14/adversarial/adjudication.md` §7.2 says the Y₀ clause "must be corrected identically" in the ledger addendum §12, in §13 and in the C3 frontier text. The ledger §13 got its block (pointing to §14/§15, which enact the correction); the direction file was not among this pass's named targets and was not opened. DEFERRED to the orchestrator — one dated line in the direction file's "Current frontier" is all it needs.
2. **Ledger row W12 (R5).** The source says "the ledger row is the sponsor's"; the R5 sentence is installed at the three note-level points and in the proposed row text of `probe-9.3-b.md` §9 item 2, not in the ledger's row itself.
3. **Engelking "3.1.4".** Left [RU] as `dim-cube-source.md` §4 instructs; the Engelking on disk (`r3s-28`, the 1995 *Theory of Dimensions, Finite and Infinite*) is a different book from the 1978 one that number refers to, and its theorem numbers were not checked in this pass.
4. **Two entries of the [ÁLKL23] map** rest on inference rather than a text match and are marked so in the block: equation (6.46) → (6.47) (uniform +1 tag shift in that stretch) and the diagram tag (7.38) (v3 restates its bottom-row exactness as the new Cor. 7.30; the tag number was not verified).

— end of repair-pass report —
