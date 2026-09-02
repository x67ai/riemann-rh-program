# NOVELTY / PRIOR-ART SWEEP — SESSION 14 CLAIMS C1–C10 — CHECK **O** (Opus 5)

**Program:** RH program, direction C3-r. **Session 14.** **Standing order 7** (two models,
independently). **Date of the sweep:** 2026-09-03 local.
**Author:** novelty agent, check **O**. The sibling check is a different model; I have not read its
output and nothing below is softened in the expectation that it will catch something.
**Standing order 5:** every statement below about a source is from a document I opened *in this
session* (URL or on-disk path + location stated). Nothing is from memory. Where a source could not
be reached it is named in full and marked UNDETERMINED.
**Extends, does not repeat:** `results/c3-r/referee-s14/novelty-O.md` §6 (search log S-01…S-45),
`novelty-F.md`, `novelty-adjudication.md`. Searches already run there are not re-run; where a
Session-14-earlier search bears on a claim here it is cited by its S-nn id.

*(status: in progress — sections appended as they are decided)*

---

## C6 — W3: the [ÁLKL23] coincidence statements, and the erratum question

**Claim under test.** (i) [ÁLKL23] = arXiv:2304.00798, *Topology of the space of conormal
distributions*, statements **Prop. 3.2, Cor. 3.4, Cor. 4.5, Prop. 6.10, Cor. 6.12, Cor. 6.19,
Cor. 7.11** are false as literally stated (explicit Cauchy-sequence witness; a one-point transversal
already suffices); (ii) Wengenroth's acyclicity criterion nevertheless holds for the compactly based
symbol spectra by a Landau–Kolmogorov-type interpolation; (iii) (M\*) is a formal invariant of
sup-seminorm parametrization over any compact Hausdorff T. Plus the charter's extra task: **find any
erratum, corrigendum, v4, or MathSciNet/zbMATH review noting the issue.**

### C6-a. The erratum question — ANSWERED, NEGATIVE, and the paper is PUBLISHED

| Fact | Source, opened this session |
|---|---|
| arXiv version history is **v1 (3 Apr 2023), v2 (29 Jul 2023), v3 (1 Jun 2024)**. **There is no v4.** Comments field is `55 pages, index of notation`; **no erratum/corrigendum note, no journal-ref on the abs page** | `https://arxiv.org/abs/2304.00798`, fetched 2026-09-03 |
| The paper **is published**: *J. Pseudo-Differ. Oper. Appl.* **15**:47 (2024), 68 printed pages, received 28 Jul 2023 / accepted 7 May 2024 / published online 9 Jun 2024, **© The Author(s) 2024, open access CC-BY** | published PDF, title page + running heads, opened this session |
| zbMATH Open record **Zbl 1564.46031** (zbMATH id 7901419), document_type `journal article`, DOI `10.1007/s11868-024-00617-y`, datestamp 2024-08-26. **The editorial contribution is of type `summary`, with `reviewer: name = null` and text `"zbMATH Open Web Interface contents unavailable due to conflicting licenses."` — i.e. there is NO independent zbMATH review, and nothing in the record notes any defect.** | zbMATH REST API `api.zbmath.org/v1/document/_search?search_string=Topology of the space of conormal distributions`, this session |
| Semantic Scholar: `citationCount: 0`; the citations endpoint for `arXiv:2304.00798` returns an **empty list**. So there is no citing work that could have recorded a correction | `api.semanticscholar.org/graph/v1/paper/DOI:10.1007/s11868-024-00617-y` and `.../paper/arXiv:2304.00798/citations`, this session |
| Unpaywall: `is_oa: true`, three OA locations (Springer, HAL `hal-04742200v1`, USC Minerva `hdl.handle.net/10347/34155`). **No "Correction to…" companion DOI is listed anywhere** | `api.unpaywall.org/v2/10.1007/s11868-024-00617-y`, this session |
| MathSciNet: **not searched** — permanently closed to this program (`results/corpus-routing.md` caveat 13). Named as the single residual gap for C6-a | — |

**Verdict C6-a: NO erratum, corrigendum, v4, retraction, correction-notice, or critical review exists
as of 2026-09-03.** The defective statements stand in the published, peer-reviewed, open-access text.
(Springer's own `link.springer.com` PDF endpoint is behind an Akamai "Client Challenge" JS wall and
returned a 3,038-byte HTML challenge page to `curl` on three attempts; the identical PDF was obtained
from the USC Minerva institutional repository, `https://minerva.usc.gal/bitstreams/f0f5fe37-86b7-464d-bf89-35de6fb7d44a/download`,
and is saved beside this file as `ALKL-2024-topology-conormal-distributions-PUBLISHED-JPDOA-15-47.pdf`.)

### C6-b. **MATERIAL FINDING — the program's statement numbers are arXiv-v1 numbers and DO NOT match the published article**

I read both texts side by side this session (`pdftotext -layout` of
`fetched-r3/r3s-18-…-arxiv-2304.00798v1-SESSION8-FETCH.pdf` and of the published PDF). §§3–4 keep
their numbering; **§§6–7 are renumbered in the published version.** The published statements are word
for word the same mathematics, so the refutation transfers — but every program citation of a §6/§7
number currently points at the wrong published statement.

| Statement | arXiv v1 (program's number) | **Published (J. Pseudo-Differ. Oper. Appl. 15:47)** | Published text, verbatim |
|---|---|---|---|
| symbol semi-norms | Prop. 3.2 | **Prop. 3.2** (unchanged) | "The semi-norms (3.4) and (3.5) together describe the topology of S^m(U × R^l)." |
| symbol coincidence | Cor. 3.4 | **Cor. 3.4** (unchanged) | "For m < m′, the topologies of S^{m′}(U × R^l) and C^∞(U × R^l) coincide on S^m(U × R^l). Therefore the topologies of S^∞(U × R^l) and C^∞(U × R^l) coincide on S^m(U × R^l)." |
| acyclicity of S^∞ | Cor. 3.6 | **Cor. 3.6** (unchanged) | "S^∞(U × R^l) is an acyclic Montel space, and therefore complete, boundedly retractive and reflexive." Proof: "Corollary 3.4 gives the property of being acyclic…" |
| conormal coincidence | Cor. 4.5 | **Cor. 4.5** (unchanged) | "For m < m′, m″, the topologies of I^{m′}(M, L) and I^{m″}(M, L) coincide on I^m(M, L)." Proof, in full: "Use Corollary 3.4 and the TVS-embeddings (4.10)." |
| A^m semi-norms | Prop. 6.10 | **Prop. 6.12** | "The semi-norms (6.42) and (6.43) together describe the topology of A^m(M)." |
| A-coincidence | Cor. 6.12 | **Cor. 6.14** | "If m′ < m, then the topologies of A^{m′}(M) and C^∞(M̊) coincide on A^m(M). Therefore the topologies of A(M) and C^∞(M̊) coincide on A^m(M)." |
| Ȧ-coincidence | Cor. 6.19 | **Cor. 6.21** | "For m < m′, m″, the topologies of Ȧ^{m′}(M) and Ȧ^{m″}(M) coincide on Ȧ^m(M)." |
| K(M)-coincidence (program says TRUE) | Cor. 6.24 | **Cor. 6.27** | "For m < m′, m″, the topologies of K^{m′}(M) and K^{m″}(M) coincide on K^m(M)." |
| J-coincidence | Cor. 7.11 | **Cor. 7.13** | "If m′ < m, then the topologies of J^{m′}(M, L) and C^∞(M\L) coincide on J^m(M, L). Therefore the topologies of J(M, L) and C^∞(M\L) coincide on J^m(M, L)." |
| K(M,L)-coincidence (program says TRUE) | Cor. 7.20 | **Cor. 7.22** | "For m < m′, m″, the topologies of K^{m′}(M, L) and K^{m″}(M, L) coincide on K^m(M, L)." |

Note the trap: in the **published** text, `Cor. 7.11` and `Cor. 7.20` are *totally-reflexive-Fréchet*
statements ("J^{(s)}(M, L) is a totally reflexive Fréchet space"; "K^{(s)}(M, L) is a totally
reflexive Fréchet space") — **true, and unrelated to the coincidence question.** A referee checking
the program's list against the published paper would find the program apparently calling a true and
elementary reflexivity statement false. Likewise published `Prop. 6.10` is a *density* statement
("For m′ < m, C_c^∞(M̊) is dense in x^m L^∞(M) with the topology of x^{m′}L^∞(M)"), not the
semi-norm statement the program refutes.

**Action owed (source-integrity, severity MAJOR for external circulation, nil for the mathematics):**
`results/c3-r/s14/w3-adjudication.md` §0, §3.1–§3.5, §5.1, §9 rows N1–N5, N9, N16 and every
downstream ledger line must cite **both** numberings, e.g. "[ÁLKL23] Cor. 6.12 (v1) = Cor. 6.14
(published)". The `w3-adjudication.md` header states the probes diffed v1 against v3 and found the
statements verbatim; that is consistent with what I see, but v3 is the accepted manuscript and the
**published** renumbering was not caught by either probe or by the adjudicator.

### C6-c. Prior-art verdicts on the substance

| Sub-claim | Verdict | Evidence |
|---|---|---|
| Prop. 3.2 / Cor. 3.4 / Cor. 4.5 / (v1) Prop. 6.10, Cor. 6.12, Cor. 6.19, Cor. 7.11 are **false as literally stated** | **NOVEL** | No erratum, no critical citing work, no review (C6-a); zero citations; the statements are printed unaltered in the peer-reviewed version. Nobody has published the observation. |
| Wengenroth acyclicity of the compactly based symbol spectra via a Landau–Kolmogorov-type interpolation | **PARTIAL — see C6-d below** | the *conclusion* (acyclicity/boundedly-retractive symbol LF-spaces) is in print elsewhere; the *verification of Wengenroth's 0-neighborhood criterion by interpolation* is what is new |
| (M\*) is a formal invariant of sup-seminorm parametrization over any compact Hausdorff T, both directions | **NOVEL (folklore-grade)** | no source located; see search log C6-S5…C6-S7 |
