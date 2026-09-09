# Round-4 ingest report — agent `a12-calegari-kmnt` (Session 18, 2026-09-09)

**Scope:** ingest only (per `results/fetch-r4/BRIEF.md`). No verdict changes, no edits to direction files, adjudications, or the zoo.

**Files handled:**
- ITEM 6b (P2): `fetched-r4/r4-06b-calegari-2007-foliations-geometry-3-manifolds-OUP-PUBLISHED.pdf` — D. Calegari, *Foliations and the Geometry of 3-Manifolds*, OUP 2007, §9.3 (published numbering).
- BONUS: `fetched-r4/r4-x2-kmnt-arxiv-1906.02424v1-preprint-of-r3s-36-BONUS.pdf` — Kim–Morishita–Noda–Terashima arXiv v1 (June 2019), text-layer twin of `fetched-r3/r3s-36-kmnt-2021-mjm-14-323-348-PUBLISHED-SWEEP-F-FETCH.pdf`.

**Companion reports read first:** `results/c3-r/s16/novelty/adjudication.md` §4 item 4 (the flag); `results/fetch-r4/a05-farber-komatsu-wengenroth-mangino.md` §Item 6a (Farber half, done).

**Method:** text layer via `pdftotext` (stderr discarded — the Calegari file emits harmless "Illegal annotation destination" warnings); every formula-bearing quotation checked against a `pdftoppm -r 110` render read by vision. Sections are appended as finished.

---

## ITEM 6b (P2) — Calegari, *Foliations and the Geometry of 3-Manifolds*, §9.3

### §1 Identity verification

- **File:** `fetched-r4/r4-06b-calegari-2007-foliations-geometry-3-manifolds-OUP-PUBLISHED.pdf`, 378 PDF pages, page size 252 × 380 pt (a trimmed publisher PDF, not a scan; producer "PDF Page Organizer 2.93 - Foxit"; metadata author field is junk — "Staycare Mngmt" — ignore it). **Text layer present and clean**; `pdftotext` prints "Illegal annotation destination" warnings on stderr (harmless, redirect). Math in the text layer is mildly garbled (tildes over F detach, script letters drop) — formula-bearing quotations below were checked on `pdftoppm -r 110` renders of PDF 317 and 318 by vision.
- **What it is (title page PDF 3, copyright page PDF 4, verbatim):** "Foliations and the Geometry of 3-Manifolds / Danny Calegari / California Institute of Technology" — "Oxford Mathematical Monographs" (series page PDF 1–2, last listed title "Calegari: Foliations and the geometry of 3-manifolds") — "© Danny Calegari, 2007 … First published 2007 … ISBN 978–0–19–857008–0 … Typeset by Newgen Imaging Systems (P) Ltd., Chennai, India. Printed in Great Britain on acid-free paper by Biddles Ltd., King's Lynn, Norfolk". Preface signed "Danny Calegari. Pasadena, September 2006" (printed p. ix = PDF 10). This is the **published OUP book**, not the online draft. It matches the list's citation (Oxford Math. Monographs, OUP 2007, ISBN 978-0-19-857008-0) EXACTLY.
- **PDF ↔ printed offset: PDF = printed + 15, constant through the body.** Checks: PDF 311 carries running head "296 SLITHERINGS AND OTHER FOLIATIONS"; PDF 316 "EIGENLAMINATIONS 301"; PDF 317 "302 SLITHERINGS AND OTHER FOLIATIONS" (vision-checked); PDF 318 "UNIFORM AND NONUNIFORM FOLIATIONS 303" (vision-checked); PDF 200 "THE THURSTON NORM ON HOMOLOGY 185"; PDF 201 "186 FINITE DEPTH FOLIATIONS". Front matter: Preface vii = PDF 8, Contents xi–xiv = PDF 12–15, Chapter 1 p. 1 = PDF 16.
- **Contents entry for Chapter 9 (PDF 14, printed p. xiii, verbatim):** "9 Slitherings and other foliations 295 / 9.1 Slitherings 295 / 9.2 Eigenlaminations 298 / 9.3 Uniform and nonuniform foliations 302 / 9.4 The product structure on E∞ 305 / 9.5 Moduli of quadrilaterals 307 / 9.6 Constructing laminations 308 / 9.7 Foliations with one-sided branching 310 / 9.8 Long markers 312 / 9.9 Complementary polygons 314 / 9.10 Pseudo-Anosov flows 314". So the **published §9.3 = printed pp. 302–305 = PDF 317–320**, read in full (below) together with §9.1–9.2 (printed 295–302 = PDF 310–317) for context.
- **Edition caveat — the list's premise is wrong on one point.** The list says "§9.3 (published numbering — the online draft's §9.3 is a different section)", and the s16 adjudication §4 item 4 says the draft's §9.3 "is 'Uniform and nonuniform foliations' (draft numbering ≠ published)". The **published** §9.3 is *also* "Uniform and nonuniform foliations" (Contents p. xiii; section heading printed p. 302, vision-checked). So on the only evidence available (the section title the adjudicator recorded for the draft), the draft and the published book **agree** at §9.3; there is no evidence that the numbering differs there. The adjudicator's inference "draft numbering ≠ published, so the published §9.3 was not read" was an assumption, not a finding — see §3.3 below for what actually explains the mismatch between KMNT's citation and this section's content.
