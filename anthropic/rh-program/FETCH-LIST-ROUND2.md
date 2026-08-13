# FETCH-LIST-ROUND2.md — precise fetch checklist for all planned sessions

**2026-08-13 (Session 4.5).** Supersedes the "ROUND 2" sketch inside `FETCH-LIST.md`. **Every citation below was verified online this session** (6 agents; Crossref/zbMATH/publisher/arXiv/author pages; raw evidence in `results/fetch-round2-citations-2026-08-13.json`) — zero recalled bibliography. Items are split by who needs to act: §A needs **you** (paywalled, no free copy found); §B is **free** (agents fetch at point of use — no action from you); §C is video watch-items; §D is corrections discovered while verifying.

**Delivery:** drop PDFs into `anthropic/rh-program/fetched/` (already gitignored — nothing you put there can reach GitHub). Any filename works; the `r2-NN-` prefixes below are suggestions.

---

## A. NEEDS YOU — paywalled, no free copy verified anywhere

### A1 — the one P1 action (unlocks the no-go-library closure)

- [ ] **MathSciNet pass** (login-gated; carried over from Round 1). Queries, verbatim: `Iwasawa + Riemann hypothesis` · `operator algebras + Riemann hypothesis` · `rigidity + "Riemann zeta"` · `Beurling + Riemann hypothesis` · `"Jensen polynomials" + "Riemann hypothesis"`. Export or screenshots of the hit lists suffice. Alternative that takes ~10 min: log into `mathscinet.ams.org` in Chrome during a session and Claude drives it via the browser extension.

### A2 — P2 papers: fetch when convenient (become load-bearing when the κ_a index-ladder / Lee–Yang / edge-cap work is commissioned)

- [ ] `r2-01` — M.G. Krein, H. Langer, *Über einige Fortsetzungsprobleme, die eng mit der Theorie hermitescher Operatoren im Raume Πκ zusammenhängen. I. Einige Funktionenklassen und ihre Darstellungen*, **Math. Nachr. 77 (1977) 187–236**. DOI `10.1002/mana.19770770116` (Wiley). German. The foundational N_κ paper. (Parts II: J. Funct. Anal. 30 (1978) 390–447; III: Beiträge Anal. 14 (1979) 25–40 — reported by search results, not independently verified; grab if easy.)
- [ ] `r2-02` — M.G. Krein, H. Langer, *Continuation of Hermitian Positive Definite Functions and Related Questions*, **Integral Equations Operator Theory 78 (2014) no. 1, 1–69**. DOI `10.1007/s00020-013-2091-z` (Springer). Posthumous English translation; this is w-05's ref [16].
- [ ] `r2-03` — A. Luger, *Generalized Nevanlinna Functions: Operator Representations, Asymptotic Behavior*, in D. Alpay (ed.), **Operator Theory, Springer Basel, 2015, pp. 345–371**. DOI `10.1007/978-3-0348-0667-1_35`. The standard modern English N_κ survey.
- [ ] `r2-04` — H. Langer, *Spectral functions of definitizable operators in Krein spaces*, in **Functional Analysis (Dubrovnik 1981), Lecture Notes in Math. 948, Springer, 1982, pp. 1–46**. DOI `10.1007/BFb0069840`. The classic Krein-space operator-theory survey.
- [ ] `r2-05` — R.B. Griffiths, C.A. Hurst, S. Sherman, *Concavity of Magnetization of an Ising Ferromagnet in a Positive External Field*, **J. Math. Phys. 11 (1970) no. 3, 790–795**. DOI `10.1063/1.1665211` (AIP). The original GHS inequality.
- [ ] `r2-06` — C.M. Newman, *Zeros of the partition function for generalized Ising systems*, **Comm. Pure Appl. Math. 27 (1974) no. 2, 143–159**. DOI `10.1002/cpa.3160270203` (Wiley).
- [ ] `r2-07` — S.A.C. Baluyot, D.A. Goldston, A.I. Suriajaya, C.L. Turnage-Butterbaugh, *An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta-function*, **Acta Arith. 214 (2024) 357–376**. DOI `10.4064/aa230612-20-3` (IMPAN). The PUBLISHED version — on-disk y-24 is arXiv v1 (2023) and the published error terms (which y-23 corrects) cannot be audited from it.
- [ ] `r2-08` *(optional upgrade)* — M. Langer, H. Woracek, *A local inverse spectral theorem for Hamiltonian systems*, **Inverse Problems 27 (2011) no. 5, 055002, 17 pp**. DOI `10.1088/0266-5611/27/5/055002` (IOP). **The load-bearing local Borg–Marchenko theorem for B3 gap 1.** A free preprint is verified in §B — fetch the published version only for citation-exactness once B3's converse write-up begins.

### A3 — P2 books: fetch ONLY when Phase 5 commissions the matching direction

- [ ] `r2-09` — M. Morishita, *Knots and Primes: An Introduction to Arithmetic Topology*, **2nd ed., Universitext, Springer Nature Singapore, 2024, 259 pp**. ISBN 978-981-99-9254-6 (softcover) / 978-981-99-9255-3 (eBook), DOI `10.1007/978-981-99-9255-3`. (1st ed.: Springer London 2012, ISBN 978-1-4471-2157-2, DOI `10.1007/978-1-4471-2158-9`.) For the geometric-substrate direction's Morishita bridge; free survey in §B may suffice first.
- [ ] `r2-10` — M.L. Lapidus, M. van Frankenhuijsen, *Fractal Geometry, Complex Dimensions and Zeta Functions: Geometry and Spectra of Fractal Strings*, **2nd rev. and enl. ed., Springer Monographs in Mathematics, Springer New York, 2013**. ISBN 978-1-4614-2175-7 / 978-1-4614-2176-4, DOI `10.1007/978-1-4614-2176-4`. For the wave-2 lapidus scout if it flags need; two free surveys in §B postpone it.

### A4 — P3 closure, cheap, no urgency

- [ ] `r2-11` — T.W. Hilberdink, *Correction to: "Ω-results for Beurling's zeta function and lower bounds for the generalised Dirichlet divisor problem"*, **J. Number Theory 269 (2025) 460–464**. DOI `10.1016/j.jnt.2024.09.010` (Elsevier; no arXiv version exists). Note: **2025, not 2024** as previously recorded. Per its abstract: a proof flaw rectified with a slightly weaker result in one part; Corollary 2 essentially unaffected — this affects how w-18e may be cited.
- [ ] `r2-12` — D.W. Farmer, S.M. Gonek, Y. Lee, *Pair correlation of the zeros of the derivative of the Riemann ξ-function*, **J. London Math. Soc. (2) 90 (2014) no. 1, 241–269**. DOI `10.1112/jlms/jdu026` (OUP). The published 3-author text; on-disk w-17 = arXiv:0803.0425 is the 2008 two-author Farmer–Gonek precursor and may differ.

---

## B. FREE COPIES VERIFIED — no action from you; agents fetch at point of use

All URLs below were fetched/verified working this session.

| item | citation | free copy |
|---|---|---|
| **Langer–Woracek 2011 (THE B3 gap-1 theorem)** | Inverse Problems 27 (2011) 055002 | Wayback preprint: `https://web.archive.org/web/20220925044752/https://www.asc.tuwien.ac.at/~woracek/homepage/downloads/JournalPapers/2011/lokinv.pdf` (title page verified; Woracek's TU-Wien site is offline, all his preprints live on in the Wayback snapshots) |
| Langer–Woracek, *Direct and inverse spectral theorems for a class of canonical systems with two singular endpoints*, Fields Inst. Commun. 87 (2023) 105–205, DOI 10.1007/978-3-031-39270-2_5 | states a LOCAL uniqueness theorem for singular Weyl coefficients | arXiv:1510.02635 |
| Romanov–Woracek, *Canonical systems with discrete spectrum*, JFA 278 (2020) 108318 | direct-side companion | arXiv:1904.03662 |
| Romanov, *Canonical systems and de Branges spaces* (lecture notes, preprint-only) | the inverse-theory survey | arXiv:1408.6022 |
| Kaltenbäck–Woracek, *Pontryagin spaces of entire functions* **I**: IEOT 33 (1999) 34–97 · **II**: IEOT 33 (1999) 305–380 · **III**: Acta Sci. Math. (Szeged) 69 (2003) 241–310 · **IV**: 72 (2006) 709–835 · **V**: 77 (2011) 223–336 · **VI**: 76 (2010) 511–560 (VI = the indefinite de Branges inverse theorem; series published V after VI) | Wayback preprints, all title-page-verified: `.../1999/Db-IEOT.pdf`, `.../1999/p2db-IE.pdf`, `.../2003/p3dbj.pdf`, `.../2006/p4db.pdf`, `.../2011/p5db.pdf`, `.../2010/p6db.pdf` under `web.archive.org/web/2022*/https://www.asc.tuwien.ac.at/~woracek/homepage/downloads/JournalPapers/` (exact snapshot URLs in the results JSON) |
| Krein–Langer, *Some propositions on analytic matrix functions related to the theory of operators in the space Πκ*, Acta Sci. Math. (Szeged) 43 (1981) 181–205 (English) | `http://acta.bibl.u-szeged.hu/14808/1/math_043_fasc_001_002_181-205.pdf` (Szeged repository) |
| Newman, *Inequalities for Ising models and field theories which obey the Lee-Yang Theorem*, CMP 41 (1975) 1–9, DOI 10.1007/BF01608542 | Project Euclid: `https://projecteuclid.org/euclid.cmp/1103860582` |
| Hoffstein–Lockhart, *Coefficients of Maass Forms and the Siegel Zero*, Ann. of Math. (2) 140 (1994) 161–176, DOI 10.2307/2118543 | `https://www.math.columbia.edu/~goldfeld/CoeffMaassForms.pdf` (HTTP 200 verified) |
| Goldfeld–Hoffstein–Lieman, *Appendix: An Effective Zero-Free Region*, Ann. of Math. (2) 140 (1994) 177–181, DOI 10.2307/2118544 (own JSTOR record, distinct from the main paper) | `https://www.math.columbia.edu/~goldfeld/EffectiveZeroFreeRegion.pdf` (HTTP 200 verified) |
| Morishita, *Analogies between Knots and Primes, 3-Manifolds and Number Rings* (2009 expository survey) | arXiv:0904.3399 |
| Lapidus, *An Overview of Complex Fractal Dimensions: From Fractal Strings to Fractal Drums, and Back*, Contemp. Math. (2019) | arXiv:1803.10399 |
| Lapidus–van Frankenhuijsen, *Fractality, Self-Similarity and Complex Dimensions*, Proc. Sympos. Pure Math. (Mandelbrot Jubilee) | arXiv:math/0401156 |

## C. WATCH ITEMS (video — human-optional, low value; the zeta attribution is already a four-way negative)

- **Analytic Stacks** (Clausen–Scholze, IHES/MPI Bonn, 24 lectures, began **18 Oct 2023** — not 2024): official playlist `https://www.youtube.com/playlist?list=PLx5f8IelFRgGmu6gmL-Kf_Rl_6Mm7juZO` (Lecture 1: `watch?v=YxSZ1mTIpaA`); linked from `people.mpim-bonn.mpg.de/scholze/AnalyticStacks.html`; crowd notes `github.com/ysulyma/analytic-stacks`.
- **Weil Anima** (Clausen, IHES, 4 lectures, 10–23 Feb 2026): `https://www.carmin.tv/en/collections/dustin-clausen-weil-anima` (YouTube: 1/4 `q5L8jeTuflU`, 2/4 `7yN8HTOXL7c`, 3/4 `fhFMT0BWVEM`, 4/4 `Vk5Y-68TU2I` — IDs from search-result titles, playlist page directly verified). Companion preprint arXiv:2605.11950 = on-disk `p3-22b2`.

## D. Corrections found while verifying (propagate at ingest)

1. **Hilberdink corrigendum is J. Number Theory 269 (2025) 460–464** — the "2024" in earlier notes came from its 2024 DOI registration. Its abstract concedes a proof flaw fixed with a slightly weaker result → check impact on how `w-18e` is cited.
2. **w-17 caveat sharpened:** arXiv:0803.0425 is the 2008 **two-author** version; there is no free copy of the published 3-author JLMS text.
3. **Analytic Stacks began October 2023** (community notes on disk say "2024 course").
4. Kaltenbäck–Woracek series: part **VI (2010) precedes V (2011)** in print; VI carries the inverse/uniqueness theorem.
5. Acta Arith. published title hyphenates "zeta-function" (arXiv title doesn't) — cite accordingly.

## Watch-list (unchanged; not actionable)

Montgomery–Vaughan (to appear, per y-23) · Connes–Consani [CC7] *Absolute coefficients and their Galois theory* (forthcoming) · any Λ < 0.2 or zero-verification > 3·10¹² announcement.
