# Second-model read of prospectus v5 — Opus 5, 2026-09-09

**Reader:** Opus 5 (1M context), sponsor standing order 7 second-model read, before publication.
**Target:** `prospectus.html` (47,395 bytes, mtime 2026-09-09 20:49), page TEXT only.
**Method:** the page was stripped of CSS and read in full as text; every claim in the v5-changed
parts was checked against the on-disk record named in the table. Nothing here is from memory; no
claim was accepted because it "sounds right". `prospectus.html` was NOT edited.

**VERDICT: FIX-FIRST** — three fixes, all in wording, none touching a theorem, number or verdict.
Two of them (F1, F2) are needed because the sentence as printed says more than the record supports;
one (F3) risks reading as "the courtesy note has gone to the authors", which the sponsor's rule
forbids. Everything else checked OK, including both hard rules on the D1 label, the U.S.-English
sweep and the HTML well-formedness check.

---

## Mechanical checks (run first)

| Check | Method | Result |
|---|---|---|
| HTML well-formed, every tag closed | `html.parser` stack walk over the whole file (void elements excluded) | **OK** — 0 mismatches, 0 unclosed, 0 stray closes |
| No unescaped `<` in text | regex over the tag-stripped body | **OK** — none |
| No unescaped `&` in text | regex over the tag-stripped body | **OK** — none |
| D1 label appears EXACTLY as licensed | exact-string count on the tag-stripped text | **OK** — 2 occurrences, both verbatim: `kernel-checked modulo H1, H2-B, H2-A (in conclusion form, pending the Lane A checker) and H3 (producers untrusted)`; matches `directions/D1-certified-refutation-arm.md:162` character for character |
| Short `modulo H1, H2, H3` sentence absent | grep | **OK** — absent (only other "kernel-checked modulo" is "…the enclosure hypothesis alone", correct per `directions/D1-certified-refutation-arm.md:156,158`) |
| "Antosiewicz–Dugundji" absent | grep | **OK** — the string does not occur (correct byline is Dugundji–Antosiewicz, `results/fetch-r4/RECORD-CORRECTIONS-s19.md:16`, ledger §16-quinquies) |
| "Calegari" not cited for the period-group dichotomy | grep | **OK** — "Calegari" does not occur anywhere in the page; §7 cites Candel–Conlon (`BARRIER-ZOO.md:428`: "Never cite 'Calegari §9.3' for this") |
| Kopei not said to carry fixed points | read of the C3-r card | **OK** — see row C3-8 |
| Courtesy note never described as sent | grep on "sent", "emailed", "has been sent" | **OK on those strings**; but see **F3** — "found and reported" |
| U.S. English | regex sweep for `-ise/-isation/-our/-tre/maths/grey/towards/programme/-lled/defence/licence/judgement/analyse/centre/fibre/behaviour/colour` over the tag-stripped text | **OK** — only hits are `precise`, `pointwise`, `premise`, `four/Four`, and `analyses` (US plural of *analysis*, correct as used: "convexified analyses of the pair class are unsound") |

---

## Claim-by-claim table

### Masthead and §1 "Sessions 9–19" callout

| # | Claim (quoted) | Checked against | Verdict |
|---|---|---|---|
| M-1 | "Session 19 · 2026-09-09" | `STATUS.md:98` ("SESSION 19 — 2026-09-09 — THE RH PROGRAM RESUMED") | OK |
| M-2 | "Phases 1–5 closed · build-out running · two papers posted (Zenodo) · one courtesy note ready for its authors" | `STATUS.md:48` (phase 4.5 closed), `:131` (papers posted, Zenodo), `:114` (note ready, gate open, sponsor emails) | OK — "ready for its authors", not sent |
| M-3 | "source: rh-program/ · github.com/x67ai/riemann-rh-program" | `git remote -v` → `https://github.com/x67ai/riemann-rh-program.git` | OK |
| M-4 | "35 branches scouted across two waves, and no Grossmann exists" | `STATUS.md:48` (wave 1 = 24 scouts), `:53` (wave 2 = 11 corners, 0 candidates, closure verdict "no Grossmann, proceed de novo") | OK — 24 + 11 = 35 |
| S1-1 | "(1) Two papers are posted (x67.ai and Zenodo, 2026-09-02): the cubic-augmentation no-go paper (DOI 10.5281/zenodo.22171688) and the Tate-products seed no-go (DOI 10.5281/zenodo.22171136)." | `STATUS.md:131` (concept DOI 22171688 = cubic-augmentation; 22171136 = Tate-products; mapping confirmed 2026-09-02) and `:142` | OK — both DOIs and their assignment correct |
| S1-2 | "(2) … the M1 v1.1 transcript checker and the M2a glue theorem lambda_le_point2 prove, in Lean, that every zero of H_t is real for all t ≥ 1/5 — kernel-checked modulo H1, H2-B, H2-A (in conclusion form, pending the Lane A checker) and H3 (producers untrusted)" | `directions/D1-certified-refutation-arm.md:158,162`; `STATUS.md:111` (queue item 1 requires exactly this label) | OK — label exact |
| S1-3 | "the Lane A producers and their checker are running now (§ 8)" | `STATUS.md:100` ("Running now / resume here: queue item 2 Lane A, run wf_ab066aa4-165"), `:182` | OK |
| S1-4 | "The bracket of record is unchanged: 0 ≤ Λ ≤ 0.2." | `directions/D1-certified-refutation-arm.md:162`; `STATUS.md:24` | OK |
| S1-5 | "(3) The Deninger leg of C3-r was reduced to a single decidable gate by four adversarial streams" | `STATUS.md:122` — the four Session-16 streams: (c) Q-S4′ mini-sweep, (c′) adversarial dual-model pass, (c″) Opus check of Theorem A, (e) novelty sweep | OK (note: only (c′) is strictly "adversarial"; "four dual-model streams" would be exact. Non-blocking — the count and the outcome are right.) |
| S1-6 | "Route 2 is dead (its kill-criterion fired), and the residue S4′ is Leichtnam's printed axiom list plus one clause the axioms do not imply" | `STATUS.md:131` (kill-criterion ENACTED for Route 2 into X₀^E); `directions/C3-geometric-substrate.md` frontier ("S4′ is Leichtnam's printed axiom list (2008 §5.1; 2013 §4.1) … read with clause (0) … because the four clauses imply neither") | OK |
| S1-7 | "the program's Theorem A (dual-model, binding) shows that on any compact object the archimedean lamination is hyperbolic, measure-null and never conformal along the archimedean leaf, and a closed 3-manifold cannot carry the length spectrum {log p} on a finite-type tangency set" | C3 frontier (Theorem A(C1)–(C4), Cor. A.1); `BARRIER-ZOO.md:419–428` (IV.13, B1′) | OK |
| S1-8 | "What remains is Q-S4⁗, a literature decision, not a construction." | `STATUS.md:113`; C3 frontier ("no construction attempt is licensed until Q-S4⁗ is re-posed") | OK |
| S1-9 | "(4) … the topology-coincidence statements of Álvarez López–Kordyukov–Leichtnam's 2024 JPDOA paper are false as stated" | `STATUS.md:131` (W3, "[ÁLKL23] falsity NOVEL-DUAL-CHECKED (no erratum exists)"); `LOG.md:1316` (published JPDOA numbering) | OK |
| S1-10 | "(explicit counterexamples, thirteen agents across two models, the repaired lemma supplied)" | `LOG.md:1416,1418` — the 13-agent run is `alkl23-xcheck-s17`: "Six refuters (Fable 5.1) in two lanes, each followed by an Opus 5 verify, then a Fable adjudicator" = 13 agents, two models | OK on the count and the two models. (Precision note: those 13 agents cross-checked the *note against an outside assessment*; the falsity itself was established earlier, Session 14 W3. §8 states this correctly.) |
| S1-11 | "a four-page courtesy note with an eleven-page derivations companion is verified send-ready and in the sponsor's hands for the authors" | `STATUS.md:114` (`alkl23-note.pdf` 4 pp. AND `alkl23-derivations.pdf` 11 pp.; GATE OPEN, verify3 SEND); `:185` | OK — send-ready, not sent |
| S1-12 | **"(4) A published error was found and reported:"** | same as above | **FIX — F3** (see below) |
| S1-13 | "(5) Lamzouri's … (arXiv:2609.02882, 2 Sep 2026) was read and dual-checked: same constants, same degeneracy, inside the II.1 ceiling — an independent confirmation of the walls in § 2, not a new route." | `STATUS.md:72`; `:127` (dual-check AGREES-WITH-CORRECTIONS, `results/watch-lamzouri-2609.02882/dual-check-O.md`) | OK |
| S1-14 | "(6) The corpus is complete: four sponsor fetch rounds, every delivered file identified page-by-page against its printed source" | `FETCH-LIST-ROUND4.md` header ("THE ROUND-4 LIST IS CLOSED"); `FETCH-RESPONSE-ROUND4.md` (13 ingest agents, one report per file in `results/fetch-r4/`) | OK |
| S1-15 | **"and every citation the program makes is now anchored to a page on disk"** | `FETCH-LIST-ROUND4.md` header: items **7 and 8 CLOSED — UNAVAILABLE** ("the journal-paginated texts could not be obtained; the program keeps citing the author copies (Ghys 1999 **by section**, Leichtnam 2008 §5.1)"); ledger §16-quinquies (`results/c3-r/m2c-feasibility-ledger.md:609`): memoir pages must still be **re-cited from the page map before publication** | **FIX — F1** |
| S1-16 | "the September 9 pass rewrote eleven attributions the record had gotten wrong (authors' names, chapter numbers, volume numbers, one citation key that the source paper itself had resolved to the wrong book)" | `results/fetch-r4/RECORD-CORRECTIONS-s19.md:173` — the enacted list is exactly eleven: Dugundji–Antosiewicz byline; Kopei without fixed points; Moore–Schochet Ch. III p. 57; memoir page map; Mangino 185; Wengenroth (M) = (Q); ALK 2002 → C5(a); Candel–Conlon I §9.3 for KMNT's "[7, 9.3]"; Leichtnam 2005 "[31]" refuted; Ghys 1995 wording; KMNT Lemma 3.3 flag withdrawn. The "wrong book" clause = `BARRIER-ZOO.md:428` | OK — the count is exactly right |

### Phase table, row 6

| # | Claim (quoted) | Checked against | Verdict |
|---|---|---|---|
| P6-1 | "6 · Build-out (Sessions 6–19) · running" | `STATUS.md:24`, `:98` | OK |
| P6-2 | "Two papers posted" | `STATUS.md:131,142` | OK |
| P6-3 | "D1's M1 v1.1 checker and M2a glue theorem kernel-checked (Lane A compute stream in flight)" | `directions/D1-certified-refutation-arm.md:156,158,162`; `STATUS.md:182` (run wf_ab066aa4-165 RUNNING) | OK |
| P6-4 | "C3-r's Deninger leg reduced to the Q-S4⁗ gate through four adversarial streams" | `STATUS.md:122` | OK (same non-blocking note as S1-5) |
| P6-5 | "barrier zoo at 51 entries" | `BARRIER-ZOO.md:11` — "IV.11–IV.15 (entered 2026-09-06) make **51 entries** — I: 7, II: 5, III: 21, IV: 15, V: 3" | OK |
| P6-6 | "the ÁLKL courtesy note send-ready" | `STATUS.md:114` | OK — send-ready, not sent |
| P6-7 | "corpus complete after four fetch rounds" | `FETCH-LIST-ROUND4.md` header (list CLOSED; items 7/8 closed-unavailable) | OK as a summary — the overreach is in S1-15, not here |

### §2 Lamzouri paragraph

| # | Claim (quoted) | Checked against | Verdict |
|---|---|---|---|
| L-1 | "Lamzouri's matrix-free proof of the same 2/3 theorem (arXiv:2609.02882) reaches the same constant 0.672500703679 by a Hilbert-space Bessel inequality on the two moments" | `STATUS.md:72` ("same constants by a Hilbert-space Bessel inequality on the two moments (trace + Hilbert–Schmidt norm + integer atoms)"; value 0.672500703679) | OK |
| L-2 | "exhibits the lemmaR_tight degeneracy verbatim" | `STATUS.md:72` ("exhibits lemmaR_tight's double ≡ shallow-pair degeneracy verbatim") | OK |
| L-3 | "sits inside the bandwidth-one ceiling as a Theorem-B-type certificate with (c₀, r) = (2 − Q(0), −2Q restricted to [0, 1]), Q = η²∗η²" | `STATUS.md:72` — the **corrected** pair, verbatim; `:127` (the correction was the dual-check's finding, `dual-check-O.md`) | OK — this is the corrected pair the Session-17 queue required |
| L-4 | "value 0.672500703679 against the ceiling 0.681837145932 for that r" | `STATUS.md:72`, same figures | OK |
| L-5 | "Dual-model checked; not a new route and not a new positivity generator." | `STATUS.md:72` ("Not a new route; not a new positivity generator"), `:127` (AGREES-WITH-CORRECTIONS, Opus 5, 2026-09-05) | OK |
| L-6 | Header "Independent confirmation (September 2026)." | `STATUS.md:72` (2 Sep 2026; dual-model checked 2026-09-05) | OK |

### §6 C3-r card, "Sessions 14–19" paragraph

| # | Claim (quoted) | Checked against | Verdict |
|---|---|---|---|
| C3-1 | "The kill-probe fired: Route 2 (the solenoid intermediate) is dead — Deninger's packet space is not T₀, no Q>0-suspension of a compact base is T₁, and the quasi-compact kill closes both faces (zoo IV.11–IV.12)." | `BARRIER-ZOO.md:402` (IV.11 face (a): packets indiscrete, "no T₀ … subspace of X₀ meets a packet in two points"; face (b) the X₀^E quasi-compact kill), `:410` (IV.12 Theorem T); `STATUS.md:131` (kill-criterion ENACTED) | OK |
| C3-2 | "What survives is S4′: Leichtnam's printed axiom list (2008 §5.1; 2013 §4.1) read with one extra clause, (0) = the fixed-point SO(2) axiom plus Deninger's own α = 1, because the four printed clauses imply neither." | C3 frontier, SESSION-16 STATE ("clause (0) = (0-fix) + (0-coh) — the fixed-point SO(2) axiom (Leichtnam (13)) and Deninger's own α = 1 … because the four clauses imply neither") | OK |
| C3-3 | "Theorem A (derived by one model, re-derived twice, checked by the other — binding)" | `directions/C3-geometric-substrate.md:195,197` (refuters F/O + Fable adjudicator; Opus check UPHELD with narrowings → "dual-model and BINDING") | OK |
| C3-4 | "the archimedean lamination (the closure of the χ ≠ 0 leaf) contains no compact and no euclidean leaf, consists of hyperbolic Riemann surfaces, has invariant-transverse-measure zero, and the flow is not conformal along the archimedean leaf at any time" | C3 frontier, verbatim except "and no euclidean leaf", which is entailed by "consists of hyperbolic Riemann surfaces"; `results/c3-r/s19/insights-digest.md:128` (Theorem A(C1)–(C4), Cor. A.1) | OK |
| C3-5 | "adding Deninger's global conformality (31) to a fixed point under α = 1 is inconsistent on a compact space (Schwarz–Pick, Candel, and the flow-invariance of measures carried by preserved leaves)" | C3 frontier, same three mechanisms in the same order | OK |
| C3-6 | "The [De02] guard is stated with it: Deninger's solved elliptic-curve case has (31) global, α = 1 and euclidean leaves but no fixed point, so Theorem A says only that α = 1 is inconsistent with a fixed point on a leaf along which (31) holds." | C3 frontier "[De02] GUARD" sentence, verbatim in substance; `results/c3-r/s19/insights-digest.md:238` (brief-quote 11: "Theorem A must never be paraphrased as 'α = 1 is impossible on a compact space'") | OK — the guard is stated, not dropped |
| C3-7 | "A separate kill: a closed 3-manifold cannot carry the length spectrum {log p} on a finite-type tangency set (finite rank of the period group by iterated Mayer–Vietoris against the Q-linear independence of the logarithms of primes; zoo IV.13)." | `BARRIER-ZOO.md:421,427` (B1′: `dim_Q(Λ_{M₀} ⊗ Q) ≤ dim_Q H₁(M ∖ N; Q)` by iterated Mayer–Vietoris; **finite RANK, never "finitely generated"** — the page says "finite rank", correct; Q-independence kill of {log p}) | OK |
| C3-8 | "the printed manifold class — Deninger, KMNT, ÁLKL — which puts the archimedean fixed points on compact leaves, while **Kopei's class is defined without fixed points and places any it has in compact leaves**" | `BARRIER-ZOO.md:439` (2026-09-09 RECORD CORRECTION: "Kopei's class (2011, Def. 2.1 p. 143) is defined WITHOUT fixed points; Remark 2.5 p. 144 … the contrast … reads: in Deninger's, KMNT's and ÁLKL's manifold class the archimedean fixed points lie on compact preserved leaves, and in Kopei's class fixed points, if any, lie in compact leaves"); `results/fetch-r4/RECORD-CORRECTIONS-s19.md:62` | **OK — the reversed wording is correctly avoided**; the page states the corrected contrast |
| C3-9 | "Theorem A(D) and the narrowed statement A-II are novel and must travel with their printed contrasts (Leichtnam's report of Deninger's caution, math/0603576v2 p. 12; …)" | ledger §16-quater (`results/c3-r/m2c-feasibility-ledger.md:595`): "N-C Theorem A(D) NOVEL; N-F the narrowed A-II NOVEL (each must travel with its printed contrast: Deninger's private caution reported by Leichtnam, math/0603576v2 printed **p. 12** …)" | OK — p. 12, the corrected page (the adjudicator's change was "Leichtnam p. 12 not p. 11") |
| C3-10 | "parts (A)–(C), B1′ and N1 are partial — they supply proofs of assertions Deninger printed without proof (his Remarks 2–3), with Cantwell–Conlon 1981 and the ÁLKL memoir as printed relatives" | C3 frontier, verbatim; ledger §16-quater; `STATUS.md:122` | OK — and note the page cites the memoir with **no page number**, which is correct: ledger §16-quinquies requires memoir pages to be re-cited from `results/fetch-r4/a06-memoir-pagemap.md` before publication |
| C3-11 | "the closed-leaf lemma is Epstein 1976, cited and never claimed" | ledger §16-quater ("N-E ANTICIPATED: Epstein, Ann. Inst. Fourier 26 (1976) … cite, never claim"); digest §J item 10 | OK |
| C3-12 | "The gate now: Q-S4⁗. Can a compact lamination by Riemann surfaces contain a finite-type χ = +1 leaf inside a measure-null saturated set of hyperbolic preserved leaves that is the non-transverse set of a foliated flow; in the manifold case, with rank H₁(M ∖ N; Q) infinite?" | `STATUS.md:113` (queue item 3, same wording, "manifold case with rank_Q H₁(M ∖ N; Q) = ∞"); `results/c3-r/s19/insights-digest.md:126` (§16-ter §8.4 refinements (i) and (ii)) | OK — both refinements are carried |
| C3-13 | "Duminy's theorem (Cantwell–Conlon 2002, exact hypotheses now on disk) and Hurder's open Problem 5.4 are the instruments; Ghys 1995 was read and is silent on it" | `results/c3-r/s19/insights-digest.md:133–135` (Duminy Thm 1.1/Cor. 1.2 with exact hypotheses, `a01-12-warsaw.md`; Hurder Problem 5.4 OPEN; Ghys 1995 "SILENT", `a02-ghys1995.md`); ledger `:587`; `STATUS.md:113` | OK |
| C3-14 | "the next decidable step is whether the archimedean leaf is semiproper. A literature decision is licensed; a construction is not." | ledger `:587` and digest §J item 12, binding wording: "the next decidable step is whether the archimedean leaf of an S4′ object is semiproper"; digest §G ("Standing order 6: 'NO for S4′; YES for a bounded literature decision on Q-S4⁗ and for nothing else'") | OK |

### §6 D1 card, "Sessions 8–19" paragraph

| # | Claim (quoted) | Checked against | Verdict |
|---|---|---|---|
| D1-1 | "M1 v1 was built with the DH live fire firing on both producer legs (mpmath-ball and Arb, cross-validated digit for digit by the Lean W1 checker), audited, and repaired clean" | `STATUS.md:24` ("D1 M1 v1 BUILT with the DH live fire FIRING both legs … Lean checker cross-validating Python digit-for-digit"), `:131` ("M1 v1 audited repaired-clean") | OK |
| D1-2 | "v1.1 discharged the argument-principle hypothesis, so cert_of_checkW1_ap is kernel-checked modulo the enclosure hypothesis alone" | `STATUS.md:131` ("v1.1 DONE — H-AP discharged … `cert_of_checkW1_ap` kernel-checked modulo H-ENCL alone"); `directions/D1-certified-refutation-arm.md:162` | OK |
| D1-3 | "Defs.lean v1.1 carries the instantiable Polymath15 bridge, L-B3 is a theorem, and lambda_le_point2 proves in Lean that for all t ≥ 1/5 every zero of H_t is real — the ray form of Λ ≤ 0.2" | `directions/D1-certified-refutation-arm.md:158,162` (`Polymath15Bridge'`, L-B3 PROVED in `BtFacts.lean`, `lambda_le_point2`) | OK |
| D1-4 | "from four displayed hypotheses: H1 (the exact Platt–Trudgian row), H2-B (kernel-checked barrier transcripts, one per leg), H2-A (the final-time asymptotic nonvanishing, displayed in conclusion form until its own checker lands) and H3 (the bridge and entireness)" | `directions/D1-certified-refutation-arm.md:162`, hypothesis-by-hypothesis match (`hH1` exact PT row, `hEncl` H2-B one leg each, `hLaneA` H2-A in conclusion form, `hH3 : Polymath15Bridge' ∧ HtEntire`) | OK |
| D1-5 | "The licensed label is exactly kernel-checked modulo H1, H2-B, H2-A (in conclusion form, pending the Lane A checker) and H3 (producers untrusted)" | `directions/D1-certified-refutation-arm.md:162` ("**Licensed label:** …" — identical string); `STATUS.md:111` | OK — **rule (1) satisfied** |
| D1-6 | "#print axioms is standard; the Opus audit was clean after three documentation repairs." | `directions/D1-certified-refutation-arm.md:162` ("`#print axioms` standard; Opus audit CLEAN after three documentation repairs"); `:158` (axioms = [propext, Classical.choice, Quot.sound]) | OK |
| D1-7 | "In flight: Lane A — the P-9/P-10 producers (about 4.5 million windows, priced from a measured batch of 12,010 on both legs; the planner's projection governs the launch)" | `STATUS.md:182` — `rows-plan.json`: N_start 630783, N1 5,141,000, 3 rows, **4,510,217 windows**; pricing batch already run on both legs, **13 probe rows, 12,010 windows** (mp 177.8 s, arb 6.2 s); `LOG.md:1451` ("4.51 M windows … the planner's own projection governs") | OK — both numbers exact |
| D1-8 | "and the checkAsym checker with its soundness theorem, after which H2-A becomes a kernel-checked fact and the label shortens by one clause" | `directions/D1-certified-refutation-arm.md:158,162`; `STATUS.md:112` ("`checkAsym` + `cert_of_checkAsym` + L-A1/L-A2 … then replace `hLaneA` … drop the conclusion-form gloss") | OK |
| D1-9 | "The Gomila claim Λ ≤ 0.1787854 stays screen-open, not a record." | `directions/D1-certified-refutation-arm.md:156,164`; `STATUS.md:143` | OK |

### §6 A4 card, "Posted" sentence

| # | Claim (quoted) | Checked against | Verdict |
|---|---|---|---|
| A4-1 | "Posted 2026-09-02 as the cubic-augmentation paper, DOI 10.5281/zenodo.22171688" | `STATUS.md:131` (concept DOI 10.5281/zenodo.22171688 = the cubic-augmentation paper; posted 2026-09-02, x67.ai + Zenodo; mapping confirmed) | OK |
| A4-2 | "(the 0.9775 crowding constant was found to be a grid artifact before posting and repaired: C* < 1 is certified only for w ≤ 0.98, with S_gen2 > 1 certified inside the family)" | `STATUS.md:24` Session-8 text ("A4 polish found the 0.9775 GRID ARTIFACT (certified C* < 1 only for w ≤ 0.98; Sgen2 > 1 certified inside the family, d* ∈ (0.156, 0.158) — paper repair owed)"); `:139` (Session-9 queue item 2, the dated-revision repair) and `:135` (Session 10: "the A4 dated revision applied and referee-checked") — repair landed Session 10, posting Session 14 (2026-09-02), so "before posting" is correct | OK |

### §7 The barrier zoo

| # | Claim (quoted) | Checked against | Verdict |
|---|---|---|---|
| Z-1 | "51 barriers in 5 groups" | `BARRIER-ZOO.md:11` — 51 entries; I: 7, II: 5, III: 21, IV: 15, V: 3 (= 51, five groups) | OK |
| Z-2 | "Session 16 added the Deninger-substrate obstruction family, IV.11–IV.15: packet indiscreteness and the quasi-compact kill; Theorem T (no Q>0-suspension of a compact base is T₁) with the inert Y₀ witness; the closed-3-manifold length-group kill; Theorem A with the [De02] guard; and the specification rider that S4′ carries clause (0)." | `BARRIER-ZOO.md:402` (IV.11 packet indiscreteness + X₀^E quasi-compact kill), `:410` (IV.12 Theorem T + inert Y₀ witness), `:419` (IV.13 closed-3-manifold length-group kill), `:430` (IV.14 Theorem A), `:441` (IV.15 specification rider: S4′ carries clause (0)); `:11` ("IV.11–IV.15 (entered 2026-09-06)"); `STATUS.md:24` ("zoo IV.11–IV.15 (51 entries)") | OK — all five headers match in order and in content, and "Session 16 added" is right (IV.11/IV.12 were *derived* in Session 14 but **entered** 2026-09-06, Session 16) |
| Z-3 | "Each was read against its cited records by the second model, and each carries its prior-art block" | `results/c3-r/s16/zoo-entries-read-O.md` (named in the digest's inputs, `results/c3-r/s19/insights-digest.md` header item (5)); `BARRIER-ZOO.md:427,439` (dated `[NOVELTY — dual-model check 2026-09-06]` blocks) | OK |
| Z-4 | "the September 9 corrections pass added the printed relatives the sweep had not yet opened (Candel–Conlon's Foliations I §9.3 for the period-group dichotomy, in place of a citation key the source paper had resolved to the wrong book)" | `BARRIER-ZOO.md:428` — verbatim: KMNT's "[7, 9.3]" is "a resolved-wrong citation key — arXiv v1 wrote '[CCI; 9.3]', resolved at publication to Calegari instead of Candel–Conlon"; the correct source is "Candel–Conlon, *Foliations I*, GSM 23 (2000), §9.3, Def. 9.3.5 / Cor. 9.3.8, p. 219"; "**Never cite 'Calegari §9.3' for this**" | OK — and the page never names Calegari |

### §8 Operations and next actions

| # | Claim (quoted) | Checked against | Verdict |
|---|---|---|---|
| O-1 | "Posted (x67.ai and Zenodo, 2026-09-02): the cubic-augmentation no-go paper, DOI 10.5281/zenodo.22171688, and the Tate-products seed no-go, DOI 10.5281/zenodo.22171136." | `STATUS.md:131`, `:142` | OK |
| O-2 | "The S1 axiom note and the non-circularity gate stay internal results of record." | `STATUS.md:133` (circulation recommendation: "post TWO, keep TWO" — m0-axiom and m1-noncircularity stay internal), `:142` | OK |
| O-3 | "Send-ready (the sponsor emails it): the courtesy note to Álvarez López, Kordyukov and Leichtnam … (four pages, with an eleven-page derivations companion; verified send-ready after a thirteen-agent cross-check against an outside assessment)." | `STATUS.md:114` (4 pp. + 11 pp., GATE OPEN, sponsor emails), `:186` (xcheck 13 agents, HOLDS-WITH-REPAIR), `:185` (repair3 → verify SEND) | OK — **rule (2) satisfied here**; wording is exemplary |
| O-4 | "Formalized: the grid-Parseval law, the W1 transcript checker, and the M2a chain Defs → BarrierCert → Instance02, all sorry-free with standard axioms." | `STATUS.md:24` (GridParseval sorry-free), `:131`/`directions/D1-certified-refutation-arm.md:158,162` (Defs v1.1, BarrierCert.lean, Instance02, `#print axioms` = [propext, Classical.choice, Quot.sound]) | OK |
| O-5 | "Order 0 — document as you go. … Order 3, amended — sequential streams. One workflow at a time, at most two agents side by side … three usage-limit deaths in one day each killed ten or more agents in flight." | `STATUS.md:131` (orders 0, 3-amended, 7 landed Session 14; "four usage-limit deaths survived by the document-as-you-go rule"); `STATUS.md:110` (SESSION 17 QUEUE header: "sequential streams, one at a time, ≤ 2 agents in flight") | OK |
| O-6 | "Order 7 — dual-model novelty. … two earlier single-model claims were later found in print (Winkelmann 2002; Bertrand 1997)." | `STATUS.md:35` — verbatim: "the seed no-go's Theorems 1–3 turned out to be Winkelmann 2002; the '(T1) unrecorded' claim was Bertrand's, in print since 1997"; `LOG.md:482` (Diaz, JTNB 9 (1997) p. 231, attributed there to D. Bertrand) | OK |
| O-7 | "The 2026-09-09 refinement of order 6 also stands: a Grossmann scout judges fit against S1–S5 only; the absence of any published connection between a branch and ζ is the condition being searched for, never evidence against the branch." | `STATUS.md:34` (refinement adopted 2026-09-09); `LOG.md:1441` ("Scouts judge fit against S1–S5 only and must never discount a branch for lacking an RH literature") | OK |
| O-8 | "In flight (Session 19): D1 Lane A — the P-9/P-10 producers and the checkAsym checker, after which hLaneA is replaced by a kernel-checked fact; then packaging in the challenge/solution pattern with an independent checker" | `STATUS.md:112`, `:182`; `directions/D1-certified-refutation-arm.md:162` | OK |
| O-9 | "(the Alpöge–Buckmaster and OpenAI fluid-blowup releases of 2026-09-08 were studied for process, and their shipping standard for formal results was adopted)" | `STATUS.md:104` ("External study of the 2026-09-08 fluid-blowup releases COMPLETE … adopted as KICKSTART Part 2 item 10 (a)–(j)"); `KICKSTART.md:72,76,77`; `LOG.md:1438,1440`; `results/external/openai-ns-2026/euler-and-context.md:9,190` | OK (minor: Quanta records Buckmaster's announcement as "just before midnight September 7"; the A–B preprint PDF is dated 2026-09-08 and all press coverage is 2026-09-08, so "of 2026-09-08" stands) |
| O-10 | "C3-r next: the Q-S4⁗ literature decision — two scouts on two models plus an adjudicator, briefed from a consolidation digest of every Session 14–18 stream; the next decidable step is the semiproperness of the archimedean leaf. No construction is licensed until it reports." | `STATUS.md:113` (two scouts, one per model, + adjudicator; literature only; no construction licensed); `results/c3-r/s19/insights-digest.md` header ("a digest … of every on-disk result of the C3-r streams of Sessions 14–18 that bears on the Q-S4⁗ gate") | OK (precision note: the digest covers the **C3-r** streams bearing on the gate, not literally every stream of those sessions. Optional tightening: "…of every C3-r stream of Sessions 14–18". Non-blocking.) |
| O-11 | "D1 after Lane A: the f_DH-in-Lean statement, the M3 exclusion ledger, the Gomila M2a′ decision." | `directions/D1-certified-refutation-arm.md:162` (next in order: (3) f_DH-in-Lean (D-R8); (4) M3 exclusion ledger; (5) the Gomila M2a′ decision) | OK |
| O-12 | **"Sponsor to-dos: email the courtesy note (body and both PDFs are prepared); nothing else — the fetch lists are closed. The local corpus (fetched/ through fetched-r4/) is deliberately kept off GitHub; the sponsor holds the backup."** | `STATUS.md:114` — the sponsor-action item ends "…; **back up `fetched-r3/` (62 files, local-only)**", never marked done; `LOG.md:1390` (Session-17 close, "Sponsor items: the courtesy note to email; the fetch list; **back up fetched-r3/ (62 files)**"); `STATUS.md:171` ("sponsor should keep their own local backup since the remote will not have them"); `STATUS.md:104` (the only verified backup is `~/riemann-backup-before-purge-2026-09-09.bundle`, **local only**) | **FIX — F2** ("nothing else" and "the sponsor holds the backup" are both unsupported; the fetch-list half is correct) |
| O-13 | "Watch items: [CC7] … (re-check ≥ Nov 2026); the prismatic Stage-1 question; Dong et al. 2509.09771; the Gomila claim (screen-open — not a record); Engelking r3s-28 OCR; BGSTB 2025 / Goldston–Suriajaya; the MD(λ, δ) community-target write-up." | `STATUS.md:143` ([CC7] ≥ Nov 2026; prismatic Stage-1 nothing; Dong et al. 2509.09771 v1; Gomila), `:126` (Engelking r3s-28 OCR), `:129` (BGSTB 2025 / Goldston–Suriajaya on watch; MD write-up) | OK |
| O-14 | "Program documentation: STATUS.md … results/c3-r/m2c-feasibility-ledger.md (the Deninger-leg obstruction ledger, §1–§16-quinquies)." | `results/c3-r/m2c-feasibility-ledger.md:599` — §16-quinquies is the last section; file ends at 609 | OK |
| O-15 | "All adjudications computationally verified under sponsor standing order 5: no decisive action rests on an unverified claim." | `STATUS.md` standing order 5; unchanged from v4 | OK |

---

## The fixes, with exact replacement text

### F1 — §1, Sessions 9–19 callout, item (6). Overclaim: two sources are on disk only as author copies, one without journal pages.

**Currently reads (prospectus.html line 108):**

> (6) The corpus is complete: four sponsor fetch rounds, every delivered file identified page-by-page against its printed source, and every citation the program makes is now anchored to a page on disk — the September 9 pass rewrote eleven attributions the record had gotten wrong …

**Why it must change.** `FETCH-LIST-ROUND4.md`'s delivery header records items 7 and 8 as
**CLOSED — UNAVAILABLE**: "the journal-paginated texts could not be obtained; the program keeps
citing the author copies (Ghys 1999 **by section**, Leichtnam 2008 §5.1 …)". Ledger §16-quinquies
(`results/c3-r/m2c-feasibility-ledger.md:609`) adds that memoir citations still have to be
re-cited from the LNM 2387 page map **before publication**. So "every citation … is now anchored
to a page on disk" is false as stated, and it is false in the one direction a reader would
penalize.

**Replacement (exact):**

> (6) The corpus is complete: four sponsor fetch rounds, every delivered file identified
> page-by-page against its printed source, and every citation the program makes is anchored to a
> source on disk — with two journal-paginated texts that could not be obtained, so Ghys 1999 is
> cited by section and Leichtnam 2008 from the author copy — the September 9 pass rewrote eleven
> attributions the record had gotten wrong (authors' names, chapter numbers, volume numbers, one
> citation key that the source paper itself had resolved to the wrong book).

### F2 — §8, "Sponsor to-dos". Two unsupported claims in one sentence.

**Currently reads (prospectus.html line 251):**

> Sponsor to-dos: email the courtesy note (body and both PDFs are prepared); nothing else — the
> fetch lists are closed. The local corpus (fetched/ through fetched-r4/) is deliberately kept off
> GitHub; the sponsor holds the backup.

**Why it must change.** "nothing else" is contradicted by the record: `STATUS.md:114` still carries
"back up `fetched-r3/` (62 files, local-only)" as an open sponsor action, and `LOG.md:1390` lists
it at the Session-17 close alongside the courtesy note. And "the sponsor holds the backup" states a
fact about the sponsor's possession that no file asserts — `STATUS.md:171` records the *advice*
("sponsor should keep their own local backup since the remote will not have them"), and the only
backup on the record is `~/riemann-backup-before-purge-2026-09-09.bundle`, marked **local only**
(`STATUS.md:104`).

**Replacement (exact):**

> Sponsor to-dos: email the courtesy note (body and both PDFs are prepared); and one piece of
> housekeeping — a local backup of fetched-r3/ (62 files), which lives nowhere but this machine.
> The fetch lists are closed. The local corpus (fetched/ through fetched-r4/) is deliberately kept
> off GitHub, so the sponsor's own copy is the only copy.

### F3 — §1, Sessions 9–19 callout, item (4) lead-in. Reads as though the authors have been told.

**Currently reads (prospectus.html line 108):**

> **(4) A published error was found and reported:** the topology-coincidence statements of Álvarez
> López–Kordyukov–Leichtnam's 2024 JPDOA paper are false as stated …

**Why it must change.** The rest of the sentence is correct ("verified send-ready and in the
sponsor's hands for the authors"), and §8 is exemplary. But the bolded lead-in says the error was
**reported**, and a reader meets that word four clauses before the correction. The sponsor's rule
is that the note is never described as sent, and "reported" is the natural English for
"communicated to the authors". The record supports "found and written up", not "reported":
`STATUS.md:114` has the email gate OPEN with the act still the sponsor's.

**Replacement (exact):** change the bolded lead-in only, leaving the rest of item (4) untouched —

> **(4) A published error was found and written up for its authors:**

*(An equally good alternative, if the bold should stay parallel with (1)–(3): "**(4) A published
error was found:**".)*

---

## What was checked and found clean, worth saying explicitly

- **Both hard rules pass.** The D1 label occurs twice, both times character-identical to the
  licensed string in `directions/D1-certified-refutation-arm.md:162`; the forbidden short sentence
  does not occur anywhere in the file. The courtesy note is "send-ready", "ready for its authors",
  "in the sponsor's hands", "the sponsor emails it" — F3 is a lead-in word, not a status claim.
- **No reversed wording survives.** Kopei is stated in the corrected form (defined without fixed
  points; any it has lie in compact leaves). "Antosiewicz–Dugundji" does not occur — nor does
  Dugundji–Antosiewicz, which the prospectus simply does not need. "Calegari" does not occur, and
  §7 credits Candel–Conlon *Foliations I* §9.3 for the period-group dichotomy, exactly as
  `BARRIER-ZOO.md:428` requires.
- **The numbers hold.** 51 zoo entries; 35 branches; 4,510,217 ≈ 4.5 M Lane-A windows; the 12,010-
  window pricing batch; DOIs 22171688 (cubic-augmentation) and 22171136 (Tate-products) assigned to
  the right papers; the Lamzouri pair (2 − Q(0), −2Q|[0,1]) in its *corrected* form with
  0.672500703679 against 0.681837145932; 0 ≤ Λ ≤ 0.2 with no "Λ < 0.2" anywhere; four pages plus
  eleven; thirteen agents; eleven rewritten attributions.
- **HTML is sound** — no unclosed tags, no unescaped `<` or `&`.
- **U.S. English throughout** — no British spelling anywhere in the page text.

## Two optional tightenings (not blocking; the reader may leave them)

1. §1 item (3) and phase row 6: "four adversarial streams" → "four dual-model streams". Of the four
   Session-16 streams (`STATUS.md:122`) only the (c′) pass was adversarial in the program's sense;
   the others were a mini-sweep, an Opus re-check and a novelty sweep. The count is right either way.
2. §8, C3-r next: "a consolidation digest of every Session 14–18 stream" → "…of every C3-r stream of
   Sessions 14–18". The digest's own header scopes itself to the C3-r streams bearing on the gate.

---

*Read performed 2026-09-09 by Opus 5 under standing order 7. `prospectus.html` was not modified.*
