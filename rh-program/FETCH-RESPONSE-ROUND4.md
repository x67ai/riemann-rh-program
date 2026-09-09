# FETCH-RESPONSE-ROUND4.md — delivery record for the Round-4 sponsor fetch

**Session 18, 2026-09-09 (INGEST ONLY — the RH program is not resumed this session).** Demand: `FETCH-LIST-ROUND4.md`. Delivery: `fetched-r4/` (gitignored, local-only; filenames `r4-<item>-…`; `duplicates-of-r3/` and `not-on-list/` subfolders). Verification and extraction: ten ingest agents, brief `results/fetch-r4/BRIEF.md`, one report per agent in `results/fetch-r4/`. Mechanical sweep: `results/fetch-r4/a10-sweep.md` + `sweep-2026-09-09.json`. Nothing in this file is from memory; every statement below points at a report that points at a page.

**Sponsor-side clarification recorded:** "KMNT 2021" (list items 6 and 17) = Kim–Morishita–Noda–Terashima, *On 3-dimensional foliated dynamical systems and Hilbert type reciprocity law*, Münster J. Math. 14 (2021) 323–348, on disk as `fetched-r3/r3s-36`.

## Delivery status by item

| # | P | Item | Status | File | Report |
|---|---|---|---|---|---|
| 1 | P1 | Cantwell–Conlon, *Endsets of exceptional leaves; a theorem of G. Duminy* | **DELIVERED, verified** — printed pp. 225–261 of the Warsaw volume | `r4-01+12` (PDF 234–270; printed = PDF − 9) | `a01-12-warsaw.md` |
| 2 | P1 | Ghys 1995, Ann. of Math. 141 | delivered — verification pending | `r4-02` | `a02-ghys1995.md` |
| 3 | P2 | Kopei 2011, Abh. Hamburg 81 | delivered — verification pending | `r4-03` | `a03-kopei.md` |
| 4 | P2 | Leichtnam, *Invitation*, Contemp. Math. 387 | delivered (whole volume, image-only) — verification pending | `r4-04` | `a04-leichtnam-cm387.md` |
| 5 | P2 | Deninger–Singhof, Contemp. Math. 290, pp. 41–55 | **NOT DELIVERED — still open** | — | — |
| 6 | P2 | Farber SMM 108 §2.1 / Calegari OUP 2007 §9.3 | Farber delivered (image-only); **Calegari NOT DELIVERED — still open** | `r4-06a` | `a05-…md` |
| 7 | P3 | Ghys 1999, SMF journal version | re-delivered as the AUTHOR COPY again — pagination check pending | `r4-07` | `a09-…md` |
| 8 | P3 | Leichtnam 2008, Rend. Mat. Appl. journal version | re-delivered as an author copy (dated 27 Nov 2008) — edition check pending | `r4-08` | `a09-…md` |
| 9 | P3 | ÁLKL memoir, LNM 2387 (published) | delivered — page map pending | `r4-09` | `a06-memoir-pagemap.md` |
| 10 | P3 | Komatsu 1967, JMSJ 19 | delivered — pending | `r4-10` | `a05-…md` |
| 11 | P3 | Wengenroth 1996, Studia 120 | delivered (2-up scan, image-only) — pending | `r4-11` | `a05-…md` |
| 12 | P3 | Álvarez López–Kordyukov, *Distributional Betti numbers* | **DELIVERED, verified** — printed pp. 159–183 of the Warsaw volume | `r4-01+12` (PDF 168–192) | `a01-12-warsaw.md` |
| 13 | P3 | Dugundji–Antosiewicz 1961; Hájek 1971 | delivered (Hájek inside the whole Proc. AMS 27 issue) — pending | `r4-13a`, `r4-13b` | `a07-…md` |
| 14 | P3 | Mangino 1997, Math. Nachr. | delivered — **file header says vol. 186, list says 185**; pending | `r4-14` | `a05-…md` |
| 15 | P3 | Candel–Conlon I; Moore–Schochet; Hector–Hirsch A | delivered — Candel–Conlon I image-only; **Moore–Schochet is the 1988 FIRST edition, not CUP 2006**; Hector–Hirsch A is the 1986 2nd ed.; pending. Bonus: Candel–Conlon II (GSM 60), Hector–Hirsch B | `r4-15a`, `r4-15b`, `r4-15c` (+ `r4-15a2`, `r4-15c2`) | `a08-…md` |
| 16 | P3 | Sullivan 1976; Plante 1975 | delivered — pending | `r4-16a`, `r4-16b` | `a07-…md` |
| 17 | P3 | zbMATH reviews (Epstein 1976, Cantwell–Conlon 1981, KMNT 2021) | not delivered by the sponsor; agent attempting zbMATH Open directly — pending | — | `a09-…md` |
| — | — | Bonus: Edwards–Millett–Sullivan 1977, Topology 16, 13–32 | delivered, not requested | `r4-x1` | `a09-…md` |
| — | — | Re-deliveries of r3s-32 (Cantwell–Conlon 1981) and r3s-34 (Epstein 1976) | parked, not needed | `duplicates-of-r3/` | `a09-…md` |
| — | — | Stray: arXiv:1703.03827v16 (Blinovsky, math.GM "Proof of Riemann hypothesis") | not requested; parked unread | `not-on-list/` | — |

## Findings by item (filled at harvest; each entry cites its report)

### Item 1 — Cantwell–Conlon, Duminy's theorem (report `a01-12-warsaw.md`, COMPLETE)
- **Standing hypotheses (p. 225, verbatim):** "(M, 𝓕) a transversely oriented, C²-foliated manifold of codimension one, with M compact and oriented. We assume each component of ∂M, if any, is a leaf of 𝓕."
- **Semiproper (pp. 225–226):** a leaf F is semiproper if "at least one side of F is proper, so we include the case in which F is a proper leaf."
- **Theorem 1.1 (Duminy):** "If the leaf F of 𝓕 is semiproper and if it accumulates on the exceptional LMS X, then ℰ^X(F) is homeomorphic to the Cantor set" — X an exceptional *local* minimal set (an exceptional minimal set of 𝓕|U, U open saturated). **Corollary 1.2** is exactly Hurder's sentence (F ⊂ X minimal ⟹ ℰ(F) is a Cantor set). Theorems 1.3, 1.4 and the proof structure are transcribed in the report.
- **Versus Hurder r3s-29 §5:** C², codimension one, compact M agree; Hurder omits the orientability / transverse-orientability and boundary-leaf hypotheses and quotes the corollary, not Theorem 1.1. Hurder's Problem 5.4 is printed on p. 226 as the authors' own conjecture ("true for Markov LMS but unknown in general"), alongside a weaker generic-leaf conjecture and the remark that the generic leaf has one end or a Cantor set of ends. The paper's §8 prints the Dippolito, Hector and measure-zero questions (= Hurder 5.1–5.3).
- **What it settles for Q-S4⁗:** the exact statement with its hypotheses is now on disk; the manifold half still waits on Ghys 1995 (item 2). No verdict changed this session.

### Item 12 — Álvarez López–Kordyukov 2002, distributional Betti numbers (report `a01-12-warsaw.md`, COMPLETE)
- **Theorem 1.1 (p. 161):** for any transitive codimension-one foliation of a closed manifold, A_f = Π ∘ ∫ X_t^* f(t) dt ∘ Π is trace class and f ↦ Tr A_f^{(i)} is a distribution — **no hypothesis on closed orbits**. Theorem 5.1 (localization to periods with fixed points) also needs none. Theorem 1.3 (the Lefschetz formula, presented as proving Deninger's ICM-98 conjecture) assumes "all closed orbits simple" — on a mapping torus exactly the program's H4.
- The paper never mentions suspensions / mapping tori, the identity ℓ Σ tr((h*)^k) δ_{kℓ}, or a Fuller-index coefficient.
- **Agent's inference, recorded as such and NOT enacted:** ALK 2002 Thms 1.1 and 5.1 anticipate in print the trace-class/distribution part of claim C5(a) without H4; the mapping-torus evaluation and the index reading remain the program's. Recommendation for the next program session: add ALK 2002 Thms 1.1/5.1 as printed relatives in the C5(a) record; PARTIAL stands.
- ALK's ref. [11], "Deninger–Singhof, A note on dynamical trace formulas, manuscript 2000", is round-4 item 5, cited as an earlier partial proof — one more reason item 5 stays P2.
- **Printed-vs-proof discrepancy:** Thm 1.3 as printed has X_{l(c)}^* inside the k-sum while the proof (p. 181) uses X_{kl}^*. Quote as printed and flag; do not silently correct.

## Caveats for `results/corpus-routing.md` (collected; copied there at harvest)

- `r4-01+12` (Warsaw volume): printed page = PDF page − 9; PDF pp. 1–3, 7, 10 are title/blank pages. The Contents OCR reads "Endests … G. Dummy" — grep "Dummy|Duminy" or go by PDF page. Script letters are lost in the text layer (𝓕 → "J"/"3"/"7"/"?"; ℰ^X(F) → "£ X ( F )"/"EX(F)"; the bar on H̄ is invisible, so reduced vs. unreduced cohomology cannot be told apart by text) — vision-verify every statement where that matters. ALK Thm 1.3 printed/proof mismatch as above.
