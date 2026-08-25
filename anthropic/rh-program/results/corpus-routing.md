# corpus-routing.md — routing index for the sponsor-delivered PDF corpora

**2026-08-19 (corpus-ingest bookkeeping).** Routes every *load-bearing* corpus item to the program consumer it feeds. Not an inventory (that is the responses' §1/§9 indices); an item appears here only if the response/verification docs flag it as substantive. Grounding: `FETCH-LIST-RESPONSE.md` (Round 1, esp. §3–§7), `FETCH-RESPONSE-ROUND2.md` (Round 2, esp. §1–§4), `FETCH-VERIFICATION.md` (both appendices), `results/paper-v5-assessment-2026-08-14.md`. Nothing here is from memory.

**Location + deliberate deviation.** Round 1 = `fetched/` (174 PDFs), Round 2 = `fetched-r2/` (160 PDFs + the two round-2 markdown docs). Both corpora are **verified and accepted** and **stay where they are** — gitignored, local-only, per the sponsor decision (Session 4.95). The older `FETCH-LIST.md` instruction to rename PDFs into `sources-extracted/` predates that decision and is **deliberately not followed**; this file replaces that renaming step as the routing record. File paths: every id below is the filename prefix, i.e. item `w-08` = `fetched/w-08-*.pdf`, item `u-36a` = `fetched-r2/u-36a-*.pdf` (chapter extracts carry their host-volume id + `-CHAPTER`).

---

## Standing corpus-wide caveats (apply before reading ANY file)

1. **OCR is Claude's vision only — no third-party OCR, ever** (response §0 R-1; tesseract destroyed exactly the ξ-vs-ξ′ distinctions the program lives on). No derived text artifacts in the corpora (R-2). poppler is installed — the Read tool renders PDF pages directly.
2. **Round-1 vision-needed list is 9 files, not 5** (verification correction 3): image-only `w-05b`, `p2-09`, `p3-25a`, `x-01a`, `x-01b`; glyph-soup text layers `w-07`, `w-21`, `x-16` (x-16 has the arXiv twin `x-10` for text); Cyrillic-but-usable `p3-27`.
3. **Round-2 read-visually list**: `t-03a`, `t-08a` (image-only); `t-56a` (OCR garbled; its own masthead OCRs as "185-236" — true range **187–236**); `u-01a` (broken CP1251 encoding, **silently drops the letter Р**); **`u-33b` (Meyer, Duke 127) — text layer silently drops the letter "c"** ("idele lass group"); print verified clean — **never text-search this file**; `u-41a`/`u-42a` (Paper-Capture OCR — navigate and cite by page, never quote by copy-paste).
4. **`w-05b` (de Branges 1994): the embedded page TIFFs are stored FLIPPED top-to-bottom** — extract via pypdf and PIL `FLIP_TOP_BOTTOM` before vision reading; native 1824×2745; watch thin overbars in superscripts.
5. **`t-46a` (Nikolski correction) is Ann. Inst. Fourier 68(2) (2018) 563–567** — the Round-2 response §1.4's "1739–1742" is a RESPONSE ERROR (verification, Round-2 appendix correction 1). Cite AIF 68(2) 563–567.
6. **`u-13` (Montgomery–Vaughan MNT-II author draft): internal build date is 9 Oct 2024**; the "post-publication, 1 June 2026" claim is an HTTP header, unverified from disk. Chapter/section-level citation sound (bookmark tree matches the published CUP book); **page-level citation is not** (file page = folio + 12).
7. **Zagier chapter lives at PDF pages 312–341 of `p3-25b`** (printed folios 302–331; constant +10 offset); the volume's re-typeset text layer has at least one math typo (eq. (2): y² for y^s) — cross-check formula-critical passages against the `p3-25a` scan.
8. **`w-08` Corollary 2 and Theorem 1 inequalities are NON-STRICT** (≥ / ≤, not > / <) — quote with ≥/≤ in all propagation (verification correction 1). Constants 0.6792/0.6845 and 1.3208/1.3155 are correct.
9. **[SUPERSEDED 2026-08-26, Session 6 — D1 killer cycle, verified against the PDF three ways] Standing bounds (watch-list calibration): 0 ≤ Λ ≤ 0.2** is the de Bruijn–Newman bracket of record — **Λ ≤ 0.2 is Platt–Trudgian, Bull. LMS 53 (2021), Corollary 2** (on disk `fetched/p3-22a1` §3.4: Polymath15 Table 1 row 2 gives Λ ≤ 0.2 once H > 2.51·10¹², and PT verify H = 3·10¹²; text-layer quote re-verified by the Session-6 orchestrator AND two independent cycle agents). The old caveat's "[0, 0.22] bracket of record" was a Round-2 verification error (correction 28 checked only the strict phrase "Λ < 0.2" and never opened p3-22a1 §3.4); literature.md's 0.2 line was right all along. STILL BINDING: never write the STRICT "Λ < 0.2" (unproven; the next Polymath15 table row, Λ < 0.19, needs H > 10¹³ per PT). Watch (unverified, network-blocked Session 6): a 2026 unrefereed computer-assisted claim Λ ≤ 0.1787854 (Gomila, judegomila.com; reportedly Polymath15 Thms 1.2/1.3 at a new parameter row from the existing 3·10¹² verification; snippet-verified only) — D1's first claim-screening customer, NOT a record. Rigorous zero-verification record **3·10¹²** (Platt–Trudgian; Gourdon's 10¹³ is NOT rigorous — data source only).
10. **Woracek's pages live at `haraldworacek.github.io`** — the TU-Wien ASC server is dead; prefer the live homepage over Wayback.
11. **Page-mapping caveats (Round 2 §2)**: `r-07a` file page k = journal page 356+k; `t-55a` k = 268+k; `t-52a` n = journal 2316+n. **No page mapping exists** from `u-38x`, `u-37a` (first-view, 1–8), `u-39c`, `t-19a`, `t-24a`, `t-51c`, `s-16c`, `u-13`. Superseded-for-citation: `r-08c` → cite `u-36a`; `s-07a` → cite `u-08a` (English); `s-04x1b`/`s-04x2b` → cite `t-57a`; `r-03a` (living-reference) vs `u-43a-…-CHAPTER` (printed 345–371) — do not silently swap the two DOIs.
12. **Normalization trap**: Lagarias (`w-07`) defines ξ WITH the ½ factor; Conrey–Li omit it — the whole source of a factor-of-4 discrepancy when cross-checking their (3.2) numerically.
13. **MathSciNet is PERMANENTLY CLOSED and discharged** (zbMATH Open substitute); the five §4.3 closed items and Beiträge zur Analysis III / Dimitrov 1997 are firm dead ends — do not re-investigate any of them.

---

## Routing — by program consumer

### Merged A2+A4 cubic-certificate direction (pair-correlation / large-values ledger; v5 §7.3 template)

| item | file | feeds | caveat |
|---|---|---|---|
| w-08 | fetched/ | THE A2 pre-emption: CGdL SDP 0.6792 (RH) / 0.6845 (GRH) already in 2020 — real gap is 0.6792 → 0.6818287 = 0.0026; ceiling side (adversarial-law LP) remains the novel deliverable | arXiv preprint of Adv. Math. 361; **Cor 2 / Thm 1 inequalities NON-STRICT** |
| w-10, w-11 | fetched/ | the simple-zero record: CGG 19/27 = 70.37% under RH+GLH; Bui–Heath-Brown same under **RH alone** (mechanism = GLH-removal, not GRH) | hypothesis-ladder precision per verification correction 2 |
| w-19 | fetched/ | GGÖS super-bandwidth input: under GRH for Dirichlet L, F(α) ≥ 3/2−|α|−ε on 1 ≤ |α| ≤ 3/2−2ε — "stop calling bandwidth 1 a wall" (delta 4) | GRH-conditional |
| w-09 | fetched/ | Lagarias–Rodgers punctures A2 novelty claim (5) on the title alone; must join the prior-art gate | — |
| w-16 + w-20 | fetched/ | the RS96/Hejhal prior-art gate, now dischargeable | — |
| w-12 + w-13 | fetched/ | family row: CLLR bandwidth 2 in families, 91% under GRH; priced by Quesada-Herrera | w-13 is sole-author |
| w-14, w-15 | fetched/ | Carneiro et al. three-integrals / Hilbert-spaces pair-correlation comparanda | — |
| y-21, y-22 | fetched/ | GLSS I/II: PCC ⇒ 100% simple+critical RH-free; AH-Pairs variants | **+ Suriajaya** on both (filenames under-credit) |
| y-23 | fetched/ | box-hypothesis dictionary: 0.67250064 / 0.34500129; proportion = 2−C, joint = 3−2C; **corrects y-24's published error terms — use y-23's error terms everywhere** | + Suriajaya, Turnage-Butterbaugh; constants are the **b = 0.001 table row**, not a literal b→0 limit; "4.187" is a table row, not prose |
| y-24 + r-07a + u-38x | fetched/ + fetched-r2/ | BGSTB unconditional Montgomery theorem (published Acta Arith. 214 (2024) 357–376); Thm 3 runs the density-hypothesis bridge (A4 novelty must be strictly λ_max / orthonormalization / tr R³) | y-24 on disk = arXiv v1 (2023), no journal imprint; page-precise cites via **r-07a mapping k = 356+k**; u-38x's OA flag is a resolver false positive |
| y-25 | fetched/ | CMR Fourier optimization over the Cohn–Elkies class — already in the ledger | + Ramos; 2023 not 2025 |
| z-05 | fetched/ | Maynard–Pratt half-isolated zeros / zero-density — large-values corpus | — |
| p2-07, p2-08 | fetched/ | pair-correlation ⟺ primes-in-short-intervals no-go exactness (GM87 + MS04) | chapter = printed 183–203; OCR "Bugh" for "Hugh" |
| r-12a (+ w-17) | fetched-r2/ | FGL published 3-author text: the ξ′ pair-correlation layer; **v5 Remark 7.1 supersedes**: unconditional 0.85838/0.92919, quartic 0.86864 > FGL's RH-conditional constant — cite v5 as primary | w-17 = 2008 two-author preprint of the same paper (§3.1) — never cite for published statements |
| u-27b | fetched-r2/ | Alon–Vinzant gap distributions — direct quasicrystal ↔ pair-correlation link | journal data not established |

### A3 families/derivatives

| item | file | feeds | caveat |
|---|---|---|---|
| w-12 | fetched/ | CLLR — M5 re-scoped as "de-conditionalize CLLR" (mandatory repair 1/5) | — |
| r-12a | fetched-r2/ | FGL for sub-direction (ii)/M6 baselines; with the v5 Remark 7.1 supersession note (see A3 work log 2026-08-19) | — |

### B3 arithmetic de Branges (canonical systems, de Branges spaces, κ_a)

| item | file | feeds | caveat |
|---|---|---|---|
| y-12 | fetched/ | **THE paper B3 needs** (not the AIF paper): Thm 2.1 + p.7 remark, Thms 2.2–2.4, §7.2 (pp. 19–20), §8 remarks (3) p. 21 and (6); M5's goal = Suzuki's own open problem §8(3) | JFA 281 (2021) 109116 = arXiv:1606.05726**v3** (v1 = w-03, a different paper) |
| w-05 | fetched/ | the inverse-problem ENGINE ((K1)–(K5) ⇒ Hamiltonian formula); y-12's Thms 2.1–2.2 are applications; **local uniqueness confirmed ABSENT** — gap 1 lives here | JFA 279 (2020) 108699 |
| u-36a (+ r-08c) | fetched-r2/ | **gap 1 SUPPLIED**: Langer–Woracek Thm 1.2 = local Borg–Marchenko for canonical systems; Pontryagin analog per Remark 1.3 | **det H > 0 caution**: ∫√(det H) degenerates when det H = 0 a.e. — the converse write-up must check det H > 0 on its class; cite u-36a (IOP typeset), not r-08c |
| r-13b, r-14b, r-15b | fetched-r2/ | Langer–Woracek two-singular-endpoints local uniqueness; Romanov–Woracek direct side; Romanov survey notes | — |
| r-16c…r-21c | fetched-r2/ | Kaltenbäck–Woracek *Pontryagin spaces of entire functions* I–VI; **VI (`r-21c`) carries the indefinite de Branges inverse/uniqueness theorem** | VI (2010) published before V (2011) |
| t-56a, r-01b, r-22a, r-02a | fetched-r2/ | Krein–Langer N_κ originals (I, II, Szeged 1981, IEOT 2014 translation) — the κ_a index-ladder foundations (shared with C1 salvage) | t-56a: read visually; = pp. 187–236 |
| u-41a-CHAPTER | fetched-r2/ | Langer 1986 — **the canonical κ-index-ladder statement** (generalized zeros of negative type in N_κ), = pp. 201–212 | OT 17 scan, poor OCR — read visually |
| u-42a-CHAPTER, u-43a-CHAPTER, t-61a, r-03a, r-04a | fetched-r2/ | N_κ toolbox: Dijksma–Langer NP interpolation (= pp. 69–91); Luger survey (= pp. 345–371); Alpay–Dijksma–Langer OT 176 (the "Dijksma–Langer survey" placeholder resolution, §3.22); Langer LNM 948 | u-42a Paper-Capture OCR; cite the printed Luger chapter, not the living-reference DOI, for pp. 345–371 |
| w-04, w-05a, w-05b | fetched/ | de Branges originals = Conrey–Li refs [2][3][4] — the "essentially due to de Branges" fidelity check (largest residual risk on the §4 result) | **w-05b image-only, TIFFs flipped** — vision pipeline per caveat 4 |
| w-07 | fetched/ | Lagarias 2006 Thm 1 (p. 9): E_χ ∈ HB ⟺ RH(χ), strict ⟺ +simple; B_χ = −(d/dz)A_χ — **the primary citation for B3's former "Exactly new" item (2)** (tilt-jet = Lagarias's kernel; verified verbatim by vision) | Type-3 fonts — vision only; ξ WITH ½ factor |
| w-06 | fetched/ | Lagarias 2005 (Acta Arith. 120, 159–184): E_a Hermite–Biehler for a ≥ 1 | cite the arXiv version — it corrects a Lemma 2.2 proof |
| w-02 | fetched/ | the Λ(n)-flavoured unimodular family u(z) = exp(−2η(ξ′/ξ)(½−iz)) — the correct coefficient class for M5's R4 fix | — |
| p2-B1x | fetched/ | Suzuki Weil-distribution space: Thm 1.1 RH-conditional but **Thms 1.4/1.5 unconditional** (R2 fix: the true claim is "no compression, no Gram matrix, no certificate") | arXiv:2301.00421v3, Canad. J. Math. FirstView |
| y-13 | fetched/ | nearest unconditional κ_a substitute: Prop 1.2 (Θ_ω inner ∀ω>ω₀ ⟺ ζ ≠ 0 for Re s > ½+ω₀) | RIMS Kôkyûroku Bessatsu B34 (2012), proceedings volume |
| y-09, y-10, y-11 | fetched/ | Suzuki screw-function line (Weil quadratic form via screw functions; Li coefficients as norms) | y-11 title: "…as norms **of functions in** a model space" |
| w-01 | fetched/ | the screw-function engine under p2-B1x/y-10/y-09 | — |
| p1-05a/b | fetched/ | RKHS chains from unimodular functions; p. 1: E_ξ ∈ HB ⟺ RH | NOT the B3-load-bearing paper (that is y-12 + w-05) |
| p1-06 | fetched/ | Conrey–Li read (§4): B3 line 30 is the correct hypothesis-vs-identity argument, two fixes required (F(W) not a space of entire functions; add ξ(·,χ₄) and the a=1 inequivalence) | counterexamples unnumbered; IMRN pagination unverified |

### C1 requirements-first field

| item | file | feeds | caveat |
|---|---|---|---|
| p1-06 | fetched/ | **C1 lines 29 & 39 are UNSUPPORTED AND INVERTED** — Conrey–Li operate at E(z) = ξ(1−iz) = C1's a = 1, not a = ½; conditions strictly stronger than RH; drafted replacement text in response §4 must be used | Sarnak's remark spreads the failure over ALL Re s > ½ |
| p1-02 | fetched/ | DMV Beurling worlds = the quantitative-input test any C1 successor axiom set must fail (salvage v) | complete pp. 1–36 |
| t-56a et al. (κ_a cluster above) | fetched-r2/ | the κ_a < ∞ open-hypothesis layer (salvage iv) — shared with B3 | κ_a finiteness for a ∈ (½,1) is OPEN (response §4 end) |

### B4 zero dynamics (de Bruijn–Newman flow)

| item | file | feeds | caveat |
|---|---|---|---|
| p2-11 | fetched/ | Ki–Kim–Lee: "H_t has finitely many non-real zeros ∀t>0" — load-bearing for flow arguments | true title "On the de Bruijn–Newman constant", Adv. Math. 222 (2009) 281–306 |
| p2-13 | fetched/ | Lehmer-pair → Λ lower-bound constants (certified-search priors) | — |
| p3-22a3, p3-22a4/a5 | fetched/ | Rodgers–Tao Λ ≥ 0; Polymath15 Λ ≤ 0.22 (arXiv + published) | the standing bracket 0 ≤ Λ ≤ 0.22 |
| t-08a | fetched-r2/ | Norfolk–Ruttan–Varga: −0.385 < Λ (historical lower-bound line) | image-only; 17th page is an unnumbered figure plate |
| t-60b | fetched-r2/ | Michalowski: dBN kernel certified NOT PF₅ (5×5 Toeplitz minor, interval arithmetic) | global PF₄ question open |
| y-14, y-15 | fetched/ | Dobner Newman-conjecture extension; dBN-type constants | — |
| t-03a | fetched-r2/ | Berry 1985 spectral rigidity — origin of the rigidity notion under the Berry–Keating line (also feeds B2's spectral-zoo closure) | image-only, vision |

### B2 refutation program / barrier zoo / computational arm

| item | file | feeds | caveat |
|---|---|---|---|
| p1-02 | fetched/ | the canonical RH-false Beurling construction — foundation stone of the falsification suite and degree-one rigidity calibration | — |
| w-18a–g + r-11a | fetched/ + fetched-r2/ | the complete Hilberdink Beurling run; **r-11a = the 2025 JNT erratum to w-18e** (proof flaw fixed with a slightly weaker result in one part; Cor 2 essentially unaffected) — check any citation of w-18e against it | erratum is JNT **269 (2025)** 460–464, not 2024 |
| z-01–z-03, z-18, t-11b–t-19a, t-50 | fetched/ + fetched-r2/ | Beurling zero-density state of the art (Révész, Broucke, Pintz–Révész; Diamond–Zhang reference book) — barrier-zoo calibration | t-19a: no published pagination (11 pp vs 13; the one Acta item not derivable — purchase stands, EUR 8) |
| p2-12 | fetched/ | Farmer — the honesty clause of the computational arm's charter | cite arXiv v4; **no BAMS version exists** |
| p2-14a | fetched/ | Bober–Hiary rigorous evaluation heights — window design for targeted searches | — |
| p3-22a1 | fetched/ | Platt–Trudgian 3·10¹² record | — |
| z-08–z-14, t-05a, t-09a, t-31b, t-33b, t-34b, t-06a, t-07a, t-10a | fetched/ + fetched-r2/ | Jensen–Pólya / Turán / Laguerre branch closure (GORZ + critiques + Wronskian hierarchy) | t-07a ≠ Chen–Jia–Wang arXiv:1706.10245 (different paper) |
| p2-15, p2-16, p3-30a | fetched/ | Knauf spin-chain reduction certificate (Re s > 3/2 threshold) | p2-16 = CMP 196 preprint; p3-30a = the actual survey |
| p3-29c | fetched/ | Voronin universality exact statement — anti-tameness theorem | — |
| t-59b, u-39c | fetched-r2/ | Nakamura lookalike class (Dirichlet series with Riemann's FE, real zeros) | u-39c: apply the unprinted author erratum (§3.3: H_j(1/2+it) → H_j(t)); issue is 74(4); no journal pagination |
| y-28–y-32, t-27b, t-28b, p3-30c1/c2 | fetched/ + fetched-r2/ | Hilbert–Pólya operator-construction zoo (incl. Suo PRA — non-normalizable, self-declared) | p3-30c1 is Suo, NOT Berry–Keating |
| s-19a-CHAPTER | fetched-r2/ | Unterberger pseudodifferential arithmetic (§7–§8 Hilbert–Pólya proposal) | **read against §3.11: the author withdrew every related arXiv preprint** |
| p3-24, p3-26a/b, p3-27, p3-28a/b | fetched/ | dead-end certificates quote exact statements (Sarnak CPAM 34; Lax–Phillips 1977; Pavlov–Faddeev 1972 Russian; Colin de Verdière) | p3-27 Cyrillic; Lax–Phillips is 1977 |

### Lee–Yang dark horse (feasibility brief)

| item | file | feeds | caveat |
|---|---|---|---|
| p1-03b | fetched/ | Newman 1976 — the exact closure axioms of class **L** | full article behind JSTOR cover sheet |
| p2-17 | fetched/ | Newman GHS 1991 — exact GHS-representability implication | — |
| r-05a, r-06a, r-23a | fetched-r2/ | GHS original; Newman 1974 partition-function zeros; Newman 1975 Lee–Yang inequalities | — |
| y-17, y-18, y-19, y-20 | fetched/ | van Dantzig/Lee–Yang, totally positive functions, Laguerre–Pólya-type classes | — |
| u-37a, t-41b | fetched-r2/ | degree-one Laguerre–Pólya / radical LP class (Pascoe(–Woerdeman)) | u-37a first-view, folios 1–8, no offset exists |
| t-32b | fetched-r2/ | Pólya–Schur ↔ free probability — the bridge between the Jensen line and second-order freeness | — |

### C2 rigidity/conservation + crystalline instrument

| item | file | feeds | caveat |
|---|---|---|---|
| p2-20 | fetched/ | Ghosh–Peres rigidity theorem — the C2 template | — |
| p2-18, p2-19a/b | fetched/ | unit-mass Fourier-quasicrystal ⟺ Lee–Yang classification (the bridge claim) | — |
| u-20b | fetched-r2/ | **Kurasov–Sarnak — the source paper of the whole line** (corpus previously held only the replies) | article number, no page range |
| u-30b, u-24b, u-27b, u-28b, u-34b, u-25a | fetched-r2/ | Lev–Olevskii rigidity; higher-dim FQ from Lee–Yang varieties; gap distributions; classification of summation formulas; Favorov sharpened; Meyer Guinand measures | several: journal data not yet fixed |
| y-33, y-34 | fetched/ | Favorov counterexample line (crystalline ≠ FQ) | — |
| z-06, z-07 | fetched/ | Euler-product / Dirichlet-series rigidity theorems | — |
| t-25b | fetched-r2/ | Kubota–Takeishi — the rigidity theorem behind the BC-system papers (C*-dynamics determines the number field) | — |
| t-44b | fetched-r2/ | Pfaffian point-process number rigidity | **not RH-directed** — rigidity strand only |

### Automorphic edge-cap adjudication

| item | file | feeds | caveat |
|---|---|---|---|
| p2-09 | fetched/ | Hoffstein–Ramakrishnan — exact reach of Siegel-zero positivity into the strip | **image-only — vision**; IMRN 1995 No. 6, printed 279–308 |
| p2-10a/b | fetched/ | Lapid–Rallis — exact scope of central-value nonnegativity | — |
| r-24a, r-25a | fetched-r2/ | Hoffstein–Lockhart + GHL appendix (effective Siegel-zero input) | JSTOR cover pages |

### ncg / CCM DH-filter test

| item | file | feeds | caveat |
|---|---|---|---|
| p1-01a/b/c | fetched/ | Connes 1999 trace formula — exact scope of "semilocal proven vs. global ⟺ RH"; every circularity audit | — |
| t-22b | fetched-r2/ | **"Zeta Spectral Triples" = arXiv:2511.22755v1 (27 Nov 2025, 34 pp)** — the CCM DH-filter finisher's primary text; byte-identical to `sources-extracted/connes-zeta-spectral-triples-2026.pdf` (the "July-2026 8 pp" record was a program-record error, corrected) | — |
| y-01–y-07, z-04 | fetched/ | the Connes–Consani(–Moscovici/Marcolli) prolate/Weil-positivity/zeta-cycles cluster | — |
| t-21b | fetched-r2/ | the scaling Hamiltonian — the link between the prolate papers and the Weil-positivity papers | — |
| p1-04 | fetched/ | Fuchs 1964 prolate leakage law e^{−4πλ²} — upgrades the certified margin law to a citable two-sided bound | complete 317–330 |
| s-14a, u-14b, u-15b, u-16b, u-17b, u-18b, t-20b | fetched-r2/ | BC-system Takagi lecture; 2025–26 Connes cluster (Letter Through Time; Absolute Geometry of Spec Z — **carries the blank-arXiv [CC7] entry**; Jacobian; Connes–van Suijlekom; Knots-primes-CFT) + the organizing Essay | [CC7] unposted — re-check no earlier than Nov 2026 |
| u-33b | fetched-r2/ | Meyer Duke 127 — the unconditional representation-theoretic form of the Connes spectral interpretation | **text layer drops "c" — never text-search** |
| w-21 | fetched/ | the Haagerup question CLOSED: Aarhus 1999 booklet, survey of Odlyzko, no original RH work | glyph-soup text layer — vision |
| p3-30b | fetched/ | Cohen 2004 — NCG × number theory interactions chapter (printed 87–103) | — |
| t-24a, t-45b | fetched-r2/ | Tabuada noncommutative RH (dg-categories); Nikolaev F₁/Cuntz–Krieger | t-24a: AAM, no published pagination (AMS wall ~Mar 2027) |

### Track-C de-novo construction (arithmetic-geometric substrates; rigidity calibration)

| item | file | feeds | caveat |
|---|---|---|---|
| x-01a, x-01b | fetched/ | Deninger gamma factors (Invent. 104) and local L-factors/regularized determinants (Invent. 107) — **two distinct papers** (had been memory-merged) | GDZ image-only scans — vision |
| x-03 + z-19 | fetched/ | Deninger dynamical systems for arithmetic schemes | cite **v4 only** (v1/v2 superseded); published = Indag. Math. 37 (2026) 25–136 (z-19, CC-BY) |
| x-09, x-14, x-07, x-08, x-10, x-15, x-16 | fetched/ | Weil-étale line; **x-09 (Morin) sources the "defect in high degrees" claim** — Flach showed infinite generation in even degrees i ≥ 4; x-14 is the correction itself | x-16 glyph-soup — use arXiv twin x-10 for text |
| x-11, x-12, x-13, p3-22b1–b3 | fetched/ | Scholze analytic geometry / Berkovich motives; Hesselholt THH; **Clausen six-functors→zeta attribution = FOLKLORE (four-way negative)** | no official Analytic Stacks notes exist |
| x-17–x-24, x-02, x-04–x-06 | fetched/ | Deninger foliated-spaces program + no-gos (x-04: no Weil cohomology with real coefficients); Manin motives lectures | — |
| t-04a, s-15a, t-35b, t-47a + u-07a | fetched-r2/ | Fesenko higher-adelic analysis I–II; Parshin Poisson formula + Tate–Iwasawa holomorphic version (English translation u-07a) | Fesenko I is a Documenta **Extra Volume** (§3.2 citation form) |
| r-09, r-26b, u-18b | fetched-r2/ | Morishita bridge for the geometric substrate (Knots and Primes 2nd ed.; free survey; Connes–Consani knots-primes-CFT link) | r-09 provenance caveat (§5) — cite `r-26b` where possible |
| u-26a, u-22a, u-32b, u-35b, z-07 | fetched-r2/ + fetched/ | Selberg-class structure (I: 0≤d≤1; VII: 1<d<2; small degrees; converse theorems) — the degree-one rigidity calibration every de-novo axiom set must clear | **read u-35b (orientation survey) first** |
| t-30b, t-43b, t-58a | fetched-r2/ | Banaszak–Uetake abstract intersection theory trilogy — independent operator-theoretic Weil-positivity axiomatization | — |
| r-10, r-27b, r-28b, t-29b, t-53, v-01x | fetched-r2/ | Lapidus complex-dimensions substitutes for the closed 2008 book (wave-2 lapidus scout) | v-01x = TOC finding aid ONLY; r-10 provenance caveat (§5) |
| p3-23 | fetched/ | Yoshida Hermitian forms — archimedean Weil-form positivity priority/credit + constants | ASPM 21, 281–325 |

### Nyman–Beurling / cotangent-sum cluster (B1-adjacent functional-analytic strand)

| item | file | feeds | caveat |
|---|---|---|---|
| t-48a | fetched-r2/ | Derevyanko–Kovalenko–Zhukovskii — **the single best orientation survey of the whole NB ↔ cotangent cluster** (found by volume scan, on no request list) | — |
| z-16, z-20, t-40a, u-06a, t-49a, t-55a | fetched/ + fetched-r2/ | Báez-Duarte strengthening; Balazard–Saias; numerical side; **Weingartner (u-06a) closes the Balazard–Saias question hole** (the "paywalled" claim was wrong); Yang generalizations | t-55a: page mapping k = 268+k |
| s-01b–s-12b, t-01a-CHAPTER, t-02a, s-02b, t-57a | fetched-r2/ | Maier–Rassias(-Raigorodskii) cotangent/NB line; Darses–Hillion probabilistic/Vasyunin line; Ehm Gram matrices; Corvalán equivalences | **do not conflate t-02a (Estermann) with s-02b (RH)** (§3.5); cite t-57a, not the s-04x stand-ins |
| t-38a + t-46a | fetched-r2/ | Nikolski cyclic vectors on the Hilbert multidisc — read ONLY with its correction | **t-46a = AIF 68(2) 563–567** |
| t-39a | fetched-r2/ | de Roton Hilbertian approach to GRH | — |
| s-07a + u-08a, u-01a–u-05a, t-26b, u-29b, t-52a, t-54a | fetched-r2/ | Kapustin operator-model line (Beurling/Davenport; zeta zeros as point spectrum; Morse potential; Mellin/de Branges/Bessel; pair correlations ↔ perturbations) + multiplicative Hilbert matrix + the X.-J. Li Weil-distribution sequence | cite u-08a (English); u-01a broken text layer; t-52a folios article-relative (2316+n); embargoed Kapustin ξ/Bessel opens 2027-04-01 (closest relative u-04a) |
| t-23b | fetched-r2/ | Ghosh–Kremnizer–Noor–Santos zero-free half-planes via analytic-function spaces (pairs with y-35) | — |
| z-15, z-17, z-21, z-22, y-35 | fetched/ | Burnol causality; BCF optimal polynomials; IEOT note; Colombeau; Noor Hardy-space Báez-Duarte | — |

### Li criterion / Weil-positivity spectral layer (B1 + u-40a cluster)

| item | file | feeds | caveat |
|---|---|---|---|
| u-19a | fetched-r2/ | Bombieri–Lagarias — the canonical Li ⇔ Weil-positivity bridge | — |
| u-21a | fetched-r2/ | Lagarias Li coefficients for automorphic L (GL(N) Weil functional) | — |
| u-23a | fetched-r2/ | Bombieri — the deepest single analysis of the Weil quadratic form, incl. the archimedean obstruction | — |
| u-40a chapters + u-09b–u-12b | fetched-r2/ | Balslev memorial volume: Sekatskii generalized-Li chapter (= 241–254, with its two arXiv halves), Green's-functions ζ(2n) chapter, Spreafico–Zaccagnini regularized products; Petridis–Risager deformations | u-09b is the arXiv posting; typeset chapter inside u-40a |
| y-08 | fetched/ | Miller highest/lowest zero positivity applications | — |
| t-54a, u-29b | fetched-r2/ | X.-J. Li explicit-formula / Hilbert–Schmidt-operator line (predecessors of the round-1 y-29) | — |

### Phase-5 synthesis / infrastructure

| item | file | feeds | caveat |
|---|---|---|---|
| u-13 | fetched-r2/ | Montgomery–Vaughan MNT-II (CUP 2026) author draft — analytic infrastructure; the "(to appear per y-23)" watch item has APPEARED | chapter/section citation only; build date 9 Oct 2024 |
| s-17a, s-18b | fetched-r2/ | Connes–Marcolli AMS Colloquium 55; NCG year 2000 — reference texts | — |
| t-20b, u-14b | fetched-r2/ | Connes' Essay + 2026 Letter Through Time — the organizing surveys for synthesis positioning | — |
| p3-29a/b/c | fetched/ | Steuding value-distribution (universality) | — |
| y-16, y-26, y-27 | fetched/ | Romik ξ expansions; Conrey–Farmer short mollifiers; Pratt–Robles perturbed moments — mollifier/moment context for A-track | — |
| y-08…y-35 misc, z-23, z-24, s-13b, s-16c, p3-22c1/c2, p3-22d1–d5 | fetched/ + fetched-r2/ | remaining coverage: Siegel-zeros × small gaps; S2-Iwasawa; p-adic Wan-RH; Weng rank 3; Hilberdink–Lapidus membranes; second-order freeness (closed negative) | s-16c author-corrected, don't cite pages 175–199 |

---

## Session-5 sufficiency (per FETCH-VERIFICATION.md)

**No fetch blocks any queued action.** A4 attempt 6 corpus complete (w-08…w-20, y-21…y-25, z-05); CCM DH-filter finisher complete (p1-01, p1-04, y-01…y-07, t-22b); B3/C1/A2 rewrites sourced (w-04/w-05a/w-05b, w-07, p1-06, y-12); B3 gap 1 sourced (u-36a). Purchase-optional remainder: Broucke–Hilberdink published text (EUR 8, the only item money still buys). Waiting on dates: Kapustin ξ/Bessel (2027-04-01), Tabuada published (≈Mar 2027), [CC7] (re-check ≥ Nov 2026).
