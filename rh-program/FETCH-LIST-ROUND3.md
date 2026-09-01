# FETCH LIST — ROUND 3 (sponsor copy)

**Written:** 2026-08-19, Session 5 close. **This is the complete list of what the sponsor needs to fetch.** It supersedes the working "ROUND 3" section inside FETCH-LIST.md (that section's annotations record how the original 13 items shrank to the 6 below: 21 sources were self-fetched into `fetched-r3/` — Wayback beat the IAS botwall — and 2 items were found already on disk).

> **UPDATE 2026-08-26 (Session 6): the sponsor load is down from 6 documents to 3.** A fetch-hunt agent legitimately self-fetched items 1, 2, 5 into `fetched-r3/`, each identity-verified per standing order 5 (no recalled-citation errors found; all [recalled] titles/volumes/pages matched):
> - **#1 DGH** → `r3s-01-…-arxiv-math0110092v1.pdf` — the arXiv **preprint** (math/0110092 v1, 59 pp) of Compositio 139 (2003) 297–360; title exact. (Published version is Kluwer/Springer DOI 10.1023/B:COMP.0000018137.38458.68 — NOT Cambridge; Compositio moved to CUP only in 2004.)
> - **#2 Halász** → `r3s-02-…-realj-extract.pdf` — the **published journal pages themselves** (Acta Math. Acad. Sci. Hungar. Tomus 19 (3–4), 1968, pp. 365–403), extracted from the Hungarian Academy's REAL-J full-volume scan (real-j.mtak.hu/7416). Title exact; add fascicle detail 19(3–4).
> - **#5 Ichino–Ikeda** → `r3s-05-…-ikeda-kyoto-preprint.pdf` — the **author preprint** (83 pp, Ikeda's Kyoto homepage) of GAFA 19 (2010) no. 5, 1378–1425 (DOI 10.1007/s00039-009-0040-4); title and cited pages confirmed.
>
> **Still sponsor-only (both confirmed closed-access everywhere legitimate; OpenAlex `is_oa: false`):**
> - **#3 Wintner** — confirmed citation: "Random factorizations and Riemann's hypothesis", Duke Math. J. **11** (1944), no. 2, **267–275**; DOI 10.1215/S0012-7094-44-01122-1 (Project Euclid).
> - **#4 Guo** — confirmed citation: "On the positivity of the central critical values of automorphic L-functions for GL(2)", Duke Math. J. **83** (1996), no. 1, **157–190**; DOI 10.1215/S0012-7094-96-08307-6 (Project Euclid).
> - **#6 Graham–Kolesnik** (book) — unchanged; a copyrighted CUP monograph is not self-fetchable.
> The fetched-r3/ backup reminder now covers 24 PDFs.

> **UPDATE 2026-08-26 (Session 6, evening): SPONSOR DELIVERY RECEIVED — six PDFs hand-dropped into `fetched-r3/` (17:07–17:12). Verified and dispositioned the same evening:**
> - **#3 Wintner — DELIVERED, VERIFIED ✅.** `wintner1944.pdf` → `r3s-11-wintner-random-factorizations-duke11-1944-pp267-275.pdf`. Title/venue exact ("Random Factorizations and Riemann's Hypothesis", Duke Math. J. 11 (1944)); complete, 9 pp = 267–275 (last page vision-checked: references end, Johns Hopkins byline). **The BARRIER-ZOO I.5 recalled-flag is discharged** — the recalled characterization was faithful; theorem quotes with page references now sit in the zoo entry.
> - **#4 Guo — DELIVERED, VERIFIED ✅.** `guo1996.pdf` → `r3s-12-guo-positivity-central-values-gl2-duke83-1996-pp157-190.pdf`. Title/venue exact (Duke Math. J. 83 (1996), no. 1, April 1996); complete, 34 pp = 157–190 (last page vision-checked: references end, Columbia/Stanford byline).
> - **#6 Graham–Kolesnik — the file named `graham1991.pdf` was NOT the book.** It is actually **G. A. Hiary, "A nearly-optimal method to compute the truncated theta function, its derivatives, and integrals", Annals of Mathematics 174 (2011) 859–889** (complete, 31 pp). Kept as a **bonus**: `r3s-13-hiary-truncated-theta-annals174-2011-pp859-889.pdf` — directly relevant to D1's M3 (Bober–Hiary rigorized isolated-window evaluation). *But see the next bullet: the real book arrived minutes later.*
> - **#6 Graham–Kolesnik — DELIVERED, VERIFIED ✅ (seventh file, 17:17).** `Van der Corputs Method of Exponential Sums.pdf` → `r3s-16-graham-kolesnik-van-der-corput-method-lms126-cup1991.pdf`. Genuine: S. W. Graham & G. Kolesnik, LMS Lecture Note Series **126**, CUP, first published 1991 (2008 digital reissue, ISBN 978-0-521-33927-8; series-list page shows entry 126). Complete: 128 PDF pages = front matter + printed 1–120, TOC (7 chapters) and final index page checked; **PDF page = printed page + 8**; CVISION OCR text layer (searchable; displayed math garbled — vision for formulas). **A4 load-bearing pin verified by vision:** §5.4, printed p. 63 — Rankin's Constant R = inf(k+l) = 0.8290213568591335924092397772831120509883432703 ± 8×10⁻⁴³; with Theorem 4.1 (printed p. 38: ζ(1/2+it) ≪ t^{(2k+2l−1)/4} log t) this gives the classical exponent-pair floor (2R−1)/4 ≈ 0.16451068 — the "~0.1645 Rankin infimum". Note the book itself never prints the decimal 0.1645; it prints R.
> - **#2 Halász (redundant delivery) — KEEP-BOTH.** `10.1007@BF01894515.pdf` is Springer's official DOI-bearing digitization (PageGenie/TIF, 2005, OCR text layer, 1.5 MB) of the same journal pages 365–403 → kept as `r3s-14-halasz-mittelwerte-acta-hungar-19-1968-springer-digitized-bf01894515.pdf`, alongside the REAL-J extract `r3s-02` (independent scan lineage; the REAL-J copy has the cleaner diacritics, the Springer copy the canonical provenance).
> - **#5 Ichino–Ikeda (redundant delivery) — KEEP-BOTH.** `gp_revised.pdf` is the **revised author preprint** (dvipdfmx Jan 2009, 60 pp, A4 — the near-final GAFA form) → kept as `r3s-15-ichino-ikeda-periods-gross-prasad-gafa19-gp-revised-2009-author-preprint-60pp.pdf`, distinct from the earlier 83-pp Kyoto preprint `r3s-05`.
> - **#1 DGH (redundant delivery) — STRICT DUPLICATE.** `0110092v1.pdf` is the same arXiv math/0110092 v1 as `r3s-01` (59 pp, same stamp; byte-different only from arXiv PDF regeneration — extracted text agrees to 1 character in 100,966 after whitespace normalization) → moved to `fetched-r3/duplicates/0110092v1-sponsor-2026-08-26-duplicate-of-r3s-01.pdf` (not deleted).
>
> **Remaining sponsor load: NONE. The Round-3 fetch list is fully closed** — all six items delivered and verified (plus the Hiary bonus). The fetched-r3/ backup reminder now covers 35 PDFs (+1 in `duplicates/`).

**Delivery:** drop the PDFs into a new folder (e.g. `fetched-r3-sponsor/`) at the rh-program root, or into `fetched-r3/` alongside the self-fetched files — either works; the next session will verify and route them. Where only a scan is available, that is fine (the program reads scans by vision).

---

## The 6 documents needed (all P1/P2 — nothing else is missing)

| # | Document | Exact citation (verified parts) | Why the program needs it |
|---|----------|--------------------------------|--------------------------|
| 1 | **Diaconu–Goldfeld–Hoffstein** | Compositio Mathematica **139** (2003), pp. **297–360**. Title [recalled — verify at delivery]: "Multiple Dirichlet series and moments of zeta and L-functions" | The proven natural-boundary class + FE-group trichotomy — load-bearing for the Weyl-group-MDS ceiling certificate (barrier-zoo formalization queue) |
| 2 | **Halász** | Acta Mathematica Academiae Scientiarum Hungaricae **19** (1968), pp. **365–403**. Title [recalled]: "Über die Mittelwerte multiplikativer zahlentheoretischer Funktionen" | Source pin for the pretentious-blindness no-go (the branch's master theorem; the program cites its formalized floor and must pin the original) |
| 3 | **Wintner** ✅ sponsor-delivered 2026-08-26, verified → `r3s-11` | Duke Mathematical Journal **11** (1944). Title [recalled — verify]: the random-multiplicative-functions / "Random factorizations" paper | First link in the model-vs-truth fluctuation-scale chain for the Harper quenched-transfer no-go (zoo I.5 flag DISCHARGED 2026-08-26) |
| 4 | **Guo** ✅ sponsor-delivered 2026-08-26, verified → `r3s-12` | Duke Mathematical Journal, ~**1996** (volume [recalled]: 83). Title [recalled]: "On the positivity of the central critical values of automorphic L-functions for GL(2)" | Central-value nonnegativity lineage — input to the automorphic edge-cap adjudication (sweep shortlist #4(b)) |
| 5 | **Ichino–Ikeda** | Geometric and Functional Analysis (GAFA) **19** (2010). Title [recalled]: "On the periods of automorphic forms on special orthogonal groups and the Gross–Prasad conjecture" (pp. [recalled] 1378–1425) | Same nonnegativity lineage — the refined period conjecture the edge-cap design must quote precisely |
| 6 | **Graham–Kolesnik** (book) ✅ sponsor-delivered 2026-08-26 (17:17), verified → `r3s-16` (the earlier same-day "graham1991.pdf" was the Hiary Annals paper, kept as bonus `r3s-13`) | "Van der Corput's Method of Exponential Sums", London Mathematical Society Lecture Note Series **126**, Cambridge University Press, 1991 | Pins the Rankin ~0.1645 infimum and exponent-pair background for the decoupling/ANTEDB DH-blindness ceiling audit (A4's "known ceiling" clause) — Rankin pin: §5.4 printed p. 63, R = 0.82902135685913…, floor (2R−1)/4 ≈ 0.16451068 |

Citation-fidelity note (standing order 5 discipline): journal/volume/page data above came from the wave-2 scouts' online verification; items marked **[recalled]** are from model memory and must be checked against the delivered file at verification time — if a delivered paper's title/venue differs from the [recalled] guess but the volume/pages match the cited claim, the delivery is still correct.

## One non-fetch action for the sponsor

- **Back up `fetched-r3/`** (21 PDFs, ~self-fetched this session). Like `fetched/` and `fetched-r2/`, it is deliberately kept off GitHub (gitignored, local-only) — the sponsor's backup is the only redundancy. Nothing else needs backing up; everything non-PDF is on GitHub.

## Explicitly NOT needed (do not fetch)

- **MathSciNet** — permanently closed and discharged (Round 2); never re-listed.
- **Optional published-text upgrades** (Fokas tnz006, Ford PLMS 85, Bourgain JAMS 30, Sakellaridis–Venkatesh Astérisque 396, the DGG Progr. Math. 300 chapter): author/preprint versions are already on disk and sufficient; fetch only if a future session escalates one as load-bearing — it would then appear on a Round-4 list.
- **Videos** (Drinfeld/Bhatt lectures): a viewing task for a future session, not a fetch.
- Everything on the original 13-item ROUND-3 list not repeated above: already on disk (see FETCH-LIST.md ROUND-3 annotations).

**Bottom line: 6 documents + 1 backup, and Sessions 6–7 are fully unblocked.** None of the six gates Session 6's first actions (the C3/D1 adversarial cycles and A4's M2 gate need nothing from this list); they gate the barrier-zoo formalization and edge-cap work later in the queue.

**As of 2026-08-26 evening: the Round-3 list is FULLY CLOSED — no items remain.** All six documents (plus the Hiary bonus) are on disk and verified (see the dated update blocks above); the backup reminder now covers 35 PDFs (+1 in `duplicates/`).

## Session 14 (2026-09-02) — watch-list sweep self-fetches (list stays at zero sponsor items)

- ✅ **r3s-23** Lutz 2025 Münster dissertation (the [Lut25] watch item): found open-access (CC BY 4.0) at repositorium.uni-muenster.de, verified visually, installed. Needs OCR (image-only).
- ✅ **r3s-24** Hua–Yang arXiv:2608.16034v2 (24 Aug 2026), installed from arXiv, title verified from the PDF text.
- ⏳ Prüzelius Zenodo draft 10.5281/zenodo.21980224 — free (CC BY 4.0) but Zenodo blocks this network (HTTP 403); fetch when the block lifts. Not load-bearing.
- Recorded, not fetched: Nikzad–Deninger arXiv:2608.11943 (p-adic Corona II — off-road); Springer LNM *A Trace Formula for Foliated Flows* (Álvarez López–Kordyukov–Leichtnam, 2026, ISBN 978-3-032-15413-2, paywalled; the memoir r3s-17 is the arXiv version).
