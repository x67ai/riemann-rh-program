# Watch-list sweep — 2026-09-02 (Session 14)

Previous sweep: 2026-08-27. Window for "NEW": anything first seen after that date, plus anything
older that the program's files do not yet record (checked by grep over `*.md`/`*.json` outside
`fetched*/`). Standing order 5 applied throughout: every claim below is from a page opened this
session (URL given), nothing from memory. Standing order 1: unreachable or paywalled sources are
named as such with full bibliographic data.

Method notes (so the next sweep does not repeat the dead ends):

* arXiv `/a/<author>` listing pages return 404 for these authors; the API form
  `au:Lastname_F` silently drops papers (it missed Deninger's 2508.05329). Plain-surname
  queries (`au:Deninger`, `au:Connes AND au:Consani`) sorted by `submittedDate` were reliable.
* Consani's publication list `https://math.jhu.edu/~kc/Publ2026.pdf` is behind a Cloudflare
  challenge (HTTP 403 to WebFetch, curl with a browser UA, and the r.jina.ai reader). UNREACHABLE.
* Springer pages are bot-blocked ("Client Challenge"); CrossRef (`api.crossref.org`) and the
  r.jina.ai reader gave the metadata instead.
* `grep` in this shell is ugrep; long `.\{0,N\}` context patterns hit its complexity limit — use
  `/usr/bin/grep` for those.

Next free fetch slot in `fetched-r3/`: **r3s-23** (highest on disk is r3s-22).

---

## 1. [CC7] Connes–Consani, "Absolute coefficients and their Galois theory" — NO CHANGE (still unposted); no new CC / CCM preprint since 2026-08-01

Evidence:

* `https://export.arxiv.org/api/query?search_query=au:Connes+AND+au:Consani&sortBy=submittedDate&sortOrder=descending` (opened 2026-09-02): newest entries are 2606.06604v1 "On the Absolute Geometry of Spec Z" (2026-06-04) and 2602.15941v1 "On the Jacobian of Spec Z" (2026-02-17). Nothing after 2026-06-04. Same result for `au:Connes_Alain` alone (adds 2602.04022v1, 2026-02-03, Connes solo) and `au:Consani` alone.
* `https://arxiv.org/abs/2606.06604` (opened 2026-09-02): still v1 only, "30 pages". Its reference list (PDF pulled from `export.arxiv.org/pdf/2606.06604v1` and text-extracted) reads verbatim: `[CC7] A. Connes and C. Consani, Absolute coefficients and their Galois theory, arXiv:` — the arXiv number is blank, i.e. not yet posted at the time of v1.
* `https://alainconnes.org/publications/` (curl, 2026-09-02): 2026 entries are #288 "Quadratic forms, Real zeros and Echoes of the Spectral Action" (Connes–van Suijlekom, 2026, dated 2026-07-18), #287 "On the Jacobian of Spec Z" (Connes–Consani, *Journal of Noncommutative Geometry*, Forthcoming; PDF `https://alainconnes.org/wp-content/uploads/JNcG2026-1.pdf`), #286 "Zeta Spectral Triples" (CCM, EMS Series of Lectures in Mathematics 2026, ISBN 978-3-98547-108-9), #285 "Knots, primes and class field theory" (Contemporary Mathematics 832 = Regulators V, pp. 105–132, 2026), #284 "The Riemann Hypothesis, Past, Present and a letter through time" (Connes, J. Open Math. Problems 2(1), pp. 1–52, 2026). The phrase "Absolute coefficients" occurs on that page only inside the 2015 abstract of "Absolute algebra and Segal's Gamma sets". No "Galois theory" title.
* Consani's own list (`https://math.jhu.edu/~kc/Publ2026.pdf`): UNREACHABLE (Cloudflare 403 by three routes). The search-engine snippet of it shows "On the absolute geometry of Spec Z (with A. Connes), Preprint 2026" and "On the Jacobian of Spec Z (with A. Connes), to appear in Journal of Noncommutative Geometry" — no [CC7] wording visible in the snippet.
* Per-prime Tate curves / "square of Spec Z" sweep: `export.arxiv.org` API `(abs:"Spec Z" OR abs:"arithmetic scheme(s)") AND (abs:"dynamical system(s)" OR abs:foliated OR abs:"Tate curve")` sorted by date — no 2026 entries at all (newest is Deninger 2301.11643).

Recommended action: ignore for now; keep on watch (≥ Nov 2026 as before). Bibliographic updates worth a one-line note in `results/literature.md`: the Jacobian paper is accepted at JNCG; "Knots, primes and class field theory" is now published (Contemp. Math. 832, 2026, pp. 105–132); "Zeta Spectral Triples" is out as an EMS lecture-notes volume.

---

## 2. Deninger — NEW (one new preprint, off-road) + [Lut25] thesis FOUND (load-bearing, open access)

**2a. New preprint since 2508.05329.** `https://export.arxiv.org/abs/2608.11943` (opened 2026-09-02): Behzad Nikzad, Christopher Deninger, "Invariant Functions on p-divisible Groups and the p-adic Corona Problem II", v1 2026-08-12 (7 KB). Abstract, in full: "This note removes the dimension one restriction of the main results in the paper with the same title by the second author." Not on file in the program (grep for `2608.11943`: no hits). Not on the dynamical-systems / descent road. Deninger's Münster page (`https://www.uni-muenster.de/FB10srvi/persdb/MM-member.php?id=62`, opened 2026-09-02) lists exactly four 2025–26 items — 2608.11943, 2508.13685, 2508.05329, 2504.15767 — and nothing marked "in preparation".

**2b. Sequels / "stronger descent" experiment.** `https://export.arxiv.org/abs/2508.05329` still v1 (2025-08-07). No sequel found by the API author query (`au:Deninger`, newest = 2608.11943) or on the Münster page. NO CHANGE.

**2c. [Lut25] — FOUND.** Deninger's 2508.05329 cites it (local copy `fetched-r3/r3s-22-…2508.05329v1…pdf`, text-extracted) as: "[Lut25] Judith Lutz. p-adic points of rational Witt schemes., 2025. PhD-thesis, Muenster." The actual thesis (title differs: *spaces*, not *schemes*):

* **Judith Marie Lutz, "p-adic points of rational Witt spaces", Inaugural-Dissertation (Dr. rer. nat.), Fachbereich Mathematik und Informatik, Universität Münster, 2025.** Referee: Christopher Deninger. License: **CC BY 4.0**. DOI 10.17879/31948612941; URN urn:nbn:de:hbz:6-31948609942.
* Record: `https://miami.uni-muenster.de/Record/17aedd3d-570b-4630-8c13-ca940dfd9fa2` (opened 2026-09-02; the `repositorium.uni-muenster.de/Record/…` mirror of the same id returned HTTP 500).
* PDF: `https://repositorium.uni-muenster.de/document/miami/17aedd3d-570b-4630-8c13-ca940dfd9fa2/diss_lutz_2025.pdf` — downloaded to the session scratchpad and verified: 99 pages, letter size, producer PDF-XChange 10.6; **no text layer** (pdffonts/pdfimages list nothing; pdftotext yields 3 bytes), so it needs OCR before grepping. Title page rendered and read: "p-adic points of rational Witt spaces … vorgelegt von Judith Marie Lutz aus Lauf an der Pegnitz, 2025". sha256 `7da56d9e71574d91588da4dbcfb136dcf21b18f96af606337122aba5c785f2e4`.
* Abstract (record page, verbatim): "In these thesis we explore how rational Witt vectors can be used to refine and extend the ring-valued points of a scheme X." The German abstract adds that the focus is mixed-characteristic rank-one valuation rings, that for affine X the new points are interpreted as untilts of tilts via perfectoid techniques and diamonds, generalizing Deninger's earlier results to higher dimension. Keywords on the record: Rational Witt Spaces, Rational Witt Vectors, p-adic points, Perfectoid Spaces, Fargues–Fontaine Curve, Diamonds.
* Chapter 1 opening (rendered page, read visually): "The work of Deninger [Den22] extending the notion of points on an arithmetic scheme using rational Witt vectors has raised many interesting questions. This thesis explores some of them in the p-adic setting." It also states that for X = Spec(R) the elements of the reduced monoid algebra of "functions invariant under Frobenius" from W_rat(X)(O_{C_p}) to V are the objects studied, and cites [KS16] for the deformation-retract / étale-fundamental-group facts.

Recommended action: **fetch into `fetched-r3/` as `r3s-23-lutz-2025-p-adic-points-rational-witt-spaces-muenster-diss-SESSION14-FETCH.pdf`.** It is load-bearing for the Deninger descent-enrichment road and CC BY 4.0, but it is not from arXiv, so per this session's brief it was staged, not installed. Staged copy: `/private/tmp/claude-501/-Users-jaytyagi-Library-Mobile-Documents-com-apple-CloudDocs-Documents-Work-2026-Math-riemann/71316f10-7ae8-4b36-ac7e-3a4e2696ed72/scratchpad/diss_lutz_2025.pdf` (same sha256 as above). Run OCR (e.g. `ocrmypdf`) on the copy before any text search. Also correct the citation in the program's files from "rational Witt schemes" to "rational Witt spaces". 2608.11943: list in `results/literature.md` as off-road; do not fetch.

---

## 3. Morishita — NO CHANGE

* `https://arxiv.org/abs/2508.15971` (opened 2026-09-02): v5, Wed 21 Jan 2026 04:51:16 UTC, is still the latest. Abstract unchanged: "We give a relation between Deninger's foliated dynamical systems associated to abelian number fields and Connes-Consani's adelic spaces. It fits with the analogy between knots and primes in arithmetic topology and lights up a geometric view of class field theory."
* `export.arxiv.org` API `au:Morishita AND cat:math.NT` sorted by date: nothing newer than 2508.15971v5; next most recent is 2407.02063v2 (Kim–Morishita, "Triple symbols in arithmetic", 2024-10-30).
* Linking-number sweep, API `(abs:"linking number(s)") AND (abs:primes OR abs:"number field")`: newest relevant item is Ray–Shah 2511.03446 "Arithmetic invariants of torus links" (2025-11-05); nothing in 2026 on lk_p or the Deninger–Connes–Consani bridge.

Recommended action: ignore.

---

## 4. Álvarez López–Kordyukov–Leichtnam (–Kim, –Morishita) — NO CHANGE on arXiv; NEW-to-file: the LNM book version

* `https://export.arxiv.org/abs/2410.20758` (opened 2026-09-02): still v1 (2024-10-28), no comments, no journal-ref. `https://export.arxiv.org/abs/2402.06671`: still v2 (2024-02-13), comments "176 pages", no journal-ref.
* API author queries (`au:Kordyukov`, `au:Leichtnam`, `au:"Alvarez Lopez"`, sorted by date): no new paper on foliated flows / trace formulas. Post-2024-10 items are all off-topic: Kordyukov 2608.07021 (Monte Carlo on symplectic manifolds, 2026-08-07), 2605.13575v2, 2502.12087 (semiclassical trace formula for the Bochner–Schrödinger operator — not foliations); Leichtnam 2511.21586 (G-signature theorem on Witt spaces, 2025-11-26); Álvarez López–Majadas-Moure 2601.11370v2 (Lefschetz numbers of homeomorphisms and open maps, v2 2026-08-11 — abstract mentions no foliations, flows, or Deninger).
* **Book (not recorded anywhere in the program's `.md` files — grep for `978-3-032-15413` and `15412` gives nothing):** J. A. Álvarez López, Y. A. Kordyukov, E. Leichtnam, *A Trace Formula for Foliated Flows*, Lecture Notes in Mathematics, Springer Nature Switzerland, Cham. Chapter 1 "Introduction" published online 2026-01-05 (CrossRef `https://api.crossref.org/works/10.1007/978-3-032-15413-2_1`, pp. 1–11); eBook 2026-05-03, softcover 2026-05-05; ISBN 978-3-032-15412-5 (print), 978-3-032-15413-2 (eBook); DOI 10.1007/978-3-032-15413-2. Volume number not exposed by CrossRef or the reader proxy. Table of contents as shown by the reader proxy: 1 Introduction (1–11), 2 Analytic Tools (13–99), 3 Foliation Tools (101–134) — possibly truncated (the arXiv version is 176 pages). "About this book" (verbatim, via `https://r.jina.ai/https://link.springer.com/book/10.1007/978-3-032-15413-2`): "This book presents a new Lefschetz trace formula for a foliated flow on a compact foliated manifold with a foliation of codimension one. The leaves preserved by the flow and its closed orbits are assumed to be transversely simple. The formula equates two distributions on the real line: one is a renormalized trace of the flow's action on two reduced leafwise cohomologies, defined via conormal and dual-conormal currents; the other consists of contributions from the preserved leaves, closed orbits, and a b-trace version of Connes' Euler characteristic, defined using a transverse invariant measure on the complement of the preserved leaves." So: still the *transversely simple* hypothesis — nothing on non-isolated orbits, continua of closed orbits, transverse measures on the periodic set, or totally disconnected transversals. **Paywalled** (Springer; the direct page and the front-matter PDF both return the bot challenge).

Recommended action: add the book to `results/literature.md` as the published form of 2402.06671 (cite the book; keep reading the arXiv v2, r3s-17). No fetch (paywalled; content matches the arXiv version we hold).

---

## 5. Alpöge–Furman arXiv:2608.13637 — NO CHANGE on arXiv (still **v2**); NEW follow-ups and repository activity

**Version count.** Both `https://arxiv.org/abs/2608.13637` and `https://export.arxiv.org/abs/2608.13637` (opened 2026-09-02; raw HTML grepped for `[vN]`) list exactly **v1 (Thu 13 Aug 2026 17:44:42 UTC) and v2 (Wed 19 Aug 2026 18:17:52 UTC)**. Title on arXiv: "More than two thirds of the zeta zeros are simple and on the critical line". Comments: "21 pages. Proof discovered autonomously by Claude (Anthropic); verified and communicated by the listed authors. See §1 for provenance. Lean formalization available". The program's own record agrees (`results/arxiv/novelty-check.md` line 154: "v1 13 Aug 2026 / v2 19 Aug 2026"). **The "currently v5" in this sweep's brief is not supported by any source opened; treat the pin as v2.** The A4 paper cites it without a version (`results/a4-no-go/theorems.md` line 4; `lean/README.md` line 23; CIRCULATION-PREP.md line 125 says the citation carries "the version pin" — check that the pin reads v2).

**Two Anthropic-hosted PDFs** (text-extracted this session): `www-cdn.anthropic.com/564f962e…pdf` is the earlier draft, title "More than two thirds of the zeros of the Riemann zeta function lie on the critical line", author line "CLAUDE"; `www-cdn.anthropic.com/95c24693…pdf` is titled "More than two thirds of the zeros of the Riemann zeta function are simple and on the critical line", author lines "CLAUDE / ANTHROPIC", with an abstract matching arXiv v2 word for word. `https://www.anthropic.com/research/riemann-zeta` (opened 2026-09-02): dated 2026-08-10, "updated on August 13, 2026, with an updated version of Claude's paper"; external readers named there: Brian Conrey and Dan Goldston.

**Citing / follow-up papers (NEW):**

* Semantic Scholar `paper/arXiv:2608.13637/citations` (opened 2026-09-02): one citing paper — **Zhixu Hua, Xiufan Yang, "Simple and distinct zeros in a prime-modulus Dirichlet family from near-microscopic to polylogarithmic heights", arXiv:2608.16034**, v1 2026-08-17, **v2 2026-08-24** (35 pages; "Version 2 substantially extends the height range … The main constants are unchanged"). The program already screened v1 for A4 novelty (`results/arxiv/novelty-check.md` line 156: "no cubic-augmentation content"); v2 is new. Its HTML (`https://arxiv.org/html/2608.16034v2`) says: "The finite compression of Weil's Hermitian form, the treatment of off-line orbits by inertia, and the rank–trace certificate first appeared in an Anthropic manuscript [19]. Alpöge and Furman subsequently gave a verified account for the Riemann zeta function and fixed primitive Dirichlet L-functions, together with a Lean 4 formalization [17]." Main constants (Theorem 2.1 there): C_MT = 0.672500703679… (the Montgomery–Taylor constant) and C_d = (1 + C_MT)/2 = 0.836250351839… — the closed forms did not survive the page extraction and are not reproduced here.
* Hua–Yang also record: "After the first version of the present paper appeared, Fredrik Prüzelius drew our attention to [17] and communicated a contemporaneous manuscript on the polylogarithmic-height regime, archived at https://doi.org/10.5281/zenodo.21980224." Zenodo API record (`https://zenodo.org/api/records/21980224`, opened 2026-09-02): **Fredrik Prüzelius (independent researcher, ORCID 0009-0006-9202-9610), "Two thirds of the zeros of Dirichlet L-functions at polylogarithmic height are simple and on the critical line, on average", version 2.4.1-draft, published 2026-08-23, CC-BY-4.0, version DOI 10.5281/zenodo.22071915** (concept DOI 10.5281/zenodo.21980224). Abstract opens "We outline a proof that for every sufficiently large prime q, at least 2/3 − O(1/log log q) of the zeros of the Dirichlet L-functions L(s, χ) in windows (T, 2T] at polylogarithmic height … are simple and lie on the critical line"; cites arXiv:2608.13637 for its "Theorem B"; declares "extensive AI assistance" from "Anthropic's Claude". Unrefereed draft.
* arXiv API sweep `(abs:"two thirds" OR abs:"Weil's Hermitian form" OR abs:"rank-trace") AND abs:zeta` sorted by date: only 2608.13637v2 itself plus Aryan 1902.05473 (2019). No comment, erratum, or refutation found. Tao's Palomar post (`https://terrytao.wordpress.com/2026/08/18/palomar-a-registry-of-lean-verified-mathematics/`, opened 2026-09-02) does not mention the paper or its authors in the post or the comments.

**Lean repository (NEW commits after the last sweep).** `https://github.com/anthropics/zeta-23-lean/commits/main` (opened 2026-09-02): 2026-08-27 — 1010de0 "Move Zeta23 into zeta23/ subdirectory (multi-project layout)", 34e6e7e "Add per-project Lean CI"; 2026-08-28 — 6d7d6dd "Lay out zeta23 as a Palomar template project", 2bafb8c merge of PR #24 "zeta23: consistent formalization-authorship account". PR #24 (opened 2026-09-02) states: "all Lean code in the repository, `Zeta23/LinAlg/` included, was written by Claude; the paper's authors wrote the mathematics, directed the formalization … and reviewed it, and wrote no Lean by hand." README now pins the project to arXiv:2608.13637 (no version) with `leanprover/lean4:v4.33.0-rc2` / Mathlib `v4.33.0-rc2`.

Recommended action: (i) correct the parent-paper version pin to v2 wherever the program says v5; (ii) add Hua–Yang v2 and the Prüzelius Zenodo draft to the A4 prior-art/citation ledger (both are free: arXiv and Zenodo CC-BY); Hua–Yang v2 is not load-bearing for A4 (already screened at v1), so **add to the fetch list** rather than fetching now — proposed name `r3s-24-hua-yang-2608.16034v2`; (iii) note the zeta-23-lean re-layout when the Lean cross-check is next touched (paths moved to `zeta23/`).

---

## 6. Dong et al. arXiv:2509.09771 and "prismatic Stage-1" — NO CHANGE

* `https://arxiv.org/abs/2509.09771` (opened 2026-09-02): Zikang Dong, Yutong Song, Weijia Wang, Hao Zhang, Shengbo Zhao, "Large values of Dirichlet polynomials with multiplicative coefficients", **v1 only** (Thu 11 Sep 2025 18:05:55 UTC; 11 pages). Abstract: studies large values of Σ_{n≤N} f(n) n^{it} for 1 ≪ t ≤ T, gives an improved Omega result in the range exp((log T)^{1/2+ε}) ≤ N ≤ √T, and an Omega result when log N ≍ √(log T log_2 T).
* Prismatic sweep, API `abs:prismatic AND (abs:"F_1" OR abs:"field with one element" OR abs:absolute OR abs:"Spec Z")` sorted by date: the only 2026 mathematics entries are Guo 2607.04931v2 ("conditions for objects in the absolute prismatic site … to cover the final object", 2026-07-07) and Bhatt–Gee–Kisin 2607.08660 (reduction mod p of crystalline representations, 2026-07-09) — neither touches F_1, a "square" of Spec Z, or positivity. Web search for prismatic + F_1/absolute + positivity, 2026: nothing beyond Bhatt–Lurie 2201.06120 and Antieau–Krause–Nikolaus 2310.12770 (v2 2026-05-07, "relative to δ-rings").

Recommended action: ignore; keep both on the list.

---

## 7. de Bruijn–Newman constant — NO CHANGE to the record (Platt–Trudgian 0 ≤ Λ ≤ 0.2); NEW minor activity on the Gomila claim; no credible new claimant

* arXiv API `ti:"de Bruijn" AND ti:Newman` sorted by date (opened 2026-09-02): newest is Michalowski 2602.20313v2 (2026-02-23, v2 2026-07-20) "On the Pólya Frequency Order of the de Bruijn–Newman Kernel: Certified Failure at Order Five" — abstract says it "does not resolve the Riemann Hypothesis"; it is not a bound on Λ (already on file, `results/literature.md`). No new upper-bound preprint.
* **Gomila repository** `https://github.com/judegomila/dbn-lambda-01787854-candidate-audit`: default branch `main` HEAD is still **a74738d** (2026-08-21T21:26:54Z, per `api.github.com/repos/…/commits?sha=main`) — no change to the sealed claim. Repository `pushed_at` = 2026-08-27T23:13:47Z from branch **`lean/certificate-and-argument-principle`**: two commits, both 2026-08-27T23:13:46Z — 3038be5 "lean/aristotle: kernel-checked e_C0 certificate value and the rectangle argument principle" ("Two further Aristotle projects, locally kernel-verified (61 theorems …): ec0_certificate: … proves the sharp Prop 4.10 budget bound e_C0 <= 233492848188649183/10^24 … argument_principle: … proves the general argument principle on rectangles … so the declared hAP hypothesis is now dischargeable") and ea09b2f "Reseal for the two new lean/aristotle projects" (SHA256SUMS only). Other branches: `agent/twistor-phase-freeze-under-015` (2026-08-19), `codex/extension-work-01782354` (2026-08-03). Issues: none (creation restricted); 1 open PR (the branch above). README headline unchanged: "Λ ≤ 893927/5000000 = 0.1787854", "It has not yet been peer reviewed."
* Claimant's blog post `https://www.judegomila.com/posts/riemann-lambda-0.1787854` (dated 2026-08-19): "The independent reviewer is Dan Romik, who verified the analytic lemmas and reworked the material into journal-grade manuscripts." and "formal publication is the remaining step." Contrast with the repository's own record: `EXTERNAL_REFEREE_REPORT_2026-07-28.md` identifies the referee as an "adversarial AI referee panel (four independent agents …), directed and synthesized by Claude (Opus 4.8)" and says "This is an AI adversarial review, not a substitute for human expert peer review"; `dan-reworking/CLAUDE.md` describes "Dan Romik's workspace for the independent referee review", byline "Jude Gomila and [additional authors TBD]", and "As of 2026-08-01: ALL GAPS RESOLVED", with no journal or submission named. The program's screen (`results/d1-m0/gomila-screen.md`) already records both the AI panel and the Romik promotion commit; the only new facts are the blog post's wording and the Aug 27 Lean branch. Still unrefereed; still never to be cited as the record.
* New claimants: one item surfaced, pre-window and not credible — ResearchGate publication 397356536, "A Constructive Determination of the de Bruijn-Newman Constant and a Proof of the Riemann Hypothesis via Li-Chuankai's Theory of Projection" (search snippet: posted November 2025; claims "the precise result Λ = 0" from an "LCK Algebra"; also mirrored on SSRN). Page UNREACHABLE (HTTP 403); author not confirmed. Ignore.

Recommended action: no fetch. Append the Aug 27 branch commits and the blog-post quote to `results/d1-m0/gomila-screen.md` at the next touch; record that main is unchanged at a74738d.

---

## 8. 2026 works citing Deninger arXiv:1807.06400 — one confirmed (the LNM book); nothing new since 2026-08-27

* OpenAlex `works?filter=cites:W2884984338` (the Indagationes version, DOI 10.1016/j.indag.2024.05.007; opened 2026-09-02): 2 citing works — Deninger, "There is no 'Weil-'cohomology theory with real coefficients for arithmetic curves" (2023, DOI 10.2422/2036-2145.202204_005) and **Álvarez López, "Introduction", 2026-01-01, DOI 10.1007/978-3-032-15413-2_1** — chapter 1 of the LNM book in item 4.
* Semantic Scholar `paper/arXiv:1807.06400/citations`: 4 entries, none dated 2025 or 2026 (Deninger 2301.11643; Haran 2209.08536; Deninger 2204.02714; Yalkinoglu "Knots and Primes: On the arithmetic of Toda flows", 2023). Coverage is plainly incomplete (Morishita 2508.15971 is absent), so this is a floor, not a count.
* arXiv abstract-mention proxy, API `abs:Deninger` sorted by date, 2026 entries: Kahn 2602.11135v2 (divided powers on abelian varieties, v2 2026-06-08); Pisolkar–Samanta 2601.20536 (p-typical Witt vectors of associative rings, 2026-01-28); Galet 2512.00886v2 (duality for higher local fields, v2 2026-03-13); Nikolaev 2404.12179v2 (local factors and Cuntz–Pimsner algebras, v2 2026-06-12, "to appear in Kyoto Journal of Mathematics"; abstract: "The nature of such factors is an open problem studied by Deninger and Serre"); Morishita 2508.15971v5 (2026-01-21). Only Morishita is known to cite 1807.06400; the others reference other Deninger work by their abstracts, and their bibliographies were not opened.
* Google Scholar was not usable by automated fetch; not attempted beyond the search-engine layer.

Recommended action: record the LNM book as the one 2026 citing work; ignore the rest.

---

## 9. Kucharczyk–Scholze, "Topological realisations of absolute Galois groups" — NO CHANGE

* `https://export.arxiv.org/abs/1609.04717` (opened 2026-09-02): v1 2016-09-15, v2 2016-10-19 ("77 pages. This second version differs from the first one by a few minor changes, most notably the addition of Proposition 7.10 …"); no journal-ref on arXiv. (Morishita's bibliography gives the published form: "In: Cohomology of arithmetic groups, On the Occasion of …" — the Springer proceedings volume.)
* `https://arxiv.org/search/?query=Kucharczyk%2C+Robert&searchtype=author` (opened 2026-09-02): nothing after 1806.09338 (2018).
* Semantic Scholar `paper/arXiv:1609.04717/citations`: 2025–26 entries are Deninger 2508.05329 (on file) and Kuessner–Przewocki–Zastrow 2506.03368 "On measure homology of mildly wild spaces" (2025-06-03, 70 pages; abstract is about injectivity of singular → measure homology for spaces with countable fundamental group; mentions none of Kucharczyk, Scholze, Galois groups, or number fields — irrelevant to a topological model of X(Spec Z)). No 2026 follow-up. API `abs:"absolute Galois group" AND abs:topological AND abs:realization`: nothing after 2018.

Recommended action: ignore.

---

## Summary table

| # | Item | Status | Action |
|---|------|--------|--------|
| 1 | [CC7] / new CC–CCM | NO CHANGE (CC7 still "arXiv:" blank in 2606.06604 refs; nothing since 2026-06-04) | ignore; note 3 publication-status updates |
| 2 | Deninger | NEW: 2608.11943 (off-road); **[Lut25] FOUND, CC BY 4.0, staged** | fetch thesis as r3s-23 (staged in scratchpad, needs OCR); list 2608.11943 |
| 3 | Morishita | NO CHANGE (v5, 2026-01-21) | ignore |
| 4 | ALKL(–Kim, –Morishita) | NO CHANGE on arXiv; NEW-to-file LNM book (Jan/May 2026, paywalled) | add book to literature.md; no fetch |
| 5 | Alpöge–Furman | NO CHANGE on arXiv (**v2**, not v5); NEW: Hua–Yang v2 (Aug 24), Prüzelius Zenodo draft (Aug 23), zeta-23-lean re-layout + authorship PR (Aug 27–28) | fix version pin; add both follow-ups to the fetch list (r3s-24 proposed for Hua–Yang v2) |
| 6 | Dong et al. / prismatic Stage-1 | NO CHANGE (v1 only; no 2026 prismatic–F_1 item) | ignore |
| 7 | de Bruijn–Newman | NO CHANGE to record; NEW: Gomila Lean branch commits 2026-08-27T23:13Z, blog post 2026-08-19 naming Romik; main still a74738d | append to gomila-screen.md; no fetch |
| 8 | 2026 citers of 1807.06400 | one confirmed (LNM book ch. 1); nothing new since Aug 27 | record; ignore |
| 9 | Kucharczyk–Scholze | NO CHANGE (v2, 2016; no 2026 follow-up) | ignore |

Nothing was written into `fetched-r3/` this session (no qualifying arXiv item). Next free slot remains r3s-23.
