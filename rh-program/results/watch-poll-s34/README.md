# Watch poll — Session 34 (orchestrator, zero agents), 13:57 IST 2026-09-29

**Why.** The SESSION 34 QUEUE funds no stream and says "wait on the watches" (rank 1 NONE FUNDED; s32 digest §E). Between digests nobody had been assigned to look at the watches; this poll is what "waiting" costs and buys. Method: the arXiv API (`poll.py`, raw Atom in `raw/`), exact-ID version checks for every arXiv number on the watch list, keyword/author searches restricted to submissions since 2026-09-01, the upstream Lean repo's head via the GitHub API. Every hit was screened at its abstract; one at the page. Nothing here is a novelty claim; classification lines are labeled.

## Watch items polled (SESSION 34 QUEUE item 6 → SESSION 32 item 7 → SESSION 30 item 6; s32 §E (a)–(e))

| Watch item | Result | Action |
|---|---|---|
| Lamzouri 2609.02882 later versions | **FIRED — v2, 8 Sep 2026** (17 pp., 1056 text lines vs 885); record held v1 only | Delta assessed at the statement level: `../watch-lamzouri-2609.02882/V2-DELTA-s34.md`; A4 Instruments row appended; two zoo riders staged (`ZOO-LINES-STAGED.md`); watch continues (v3+) |
| Suzuki 2606.09096 | v3 (23 Sep 2026) unchanged | none (rider written at v3, zoo-s33) |
| Dong et al. 2509.09771 | v1 unchanged | none |
| Haran 2204.03107 | v1 unchanged | none |
| BGSTB 2501.14545 | latest 2501.14545v3 2026-09-01 | none |
| [CC7] (au:Connes AND au:Consani, since 1 Sep) | 0 | none; watch date ≥ Nov 2026 stands |
| prismatic Stage-1 (all:prismatic AND Riemann/zeta/Spec Z) | 0 | none |
| exact-WKB positivity (J7's trigger) | 0 | none |
| Mitkovski–Poltoratski local form of Thm 1.6 / Krein integrality (G5 (a)–(b)) | 2 hits by author, both unrelated (double Hilbert transform invariant sets; Berezin approximation); Krein AND "de Branges" 0 | none |
| Goldston–Suriajaya; Eisenberg S(t); Gomila; Borger; Lehmer pairs | 0 each | none |
| a printed β below Z (SPEC A6–A7, A11) | **1 hit on the topic, screened at the page: NOT a β** — Nikolaev 2609.16360 "Number fields as curves over F₁" (Deitmar schemes; Galois extensions of ℚ as curves OVER F₁, above the absolute point, the Kapranov–Smirnov direction the s30 read already placed there); full text 651 lines: Witt 0, Borger 0, Cartier 0, pairing 0, "below" 0, topos 0, Spec 6 (all Spec of number rings / Deitmar) | none; recorded so it is not re-priced |
| pointer (a): an external DISPROOF claim passing the poster screen | Kazin–Kadyrov 2609.29898 "…Disproof of Yang's Conjecture": zeros off the line of Yang's TEMPERED ξ̂ (cosh → sinh in the integral representation), not ζ; unconditional Hadamard argument | not a pointer; none |
| upstream anthropics/zeta-23-lean main | head fbdc36bb 2026-09-05 (dependabot lean-action bump), previous 2bafb8c8 2026-08-28 (authorship PR) | none |
| Engelking OCR; MD(λ, δ) write-up; PBSS; Álvarez López reply; G5 (c); a printed κ | not pollable by arXiv query (sponsor items or unnamed authors) | unchanged |

## Externals noted, not on any watch (prior-art record only; standing order 5: no action rests on them)

- Desogus, 2609.20367v2 (17 Sep 2026), "The Three Gates: A Rooted-Operator Approach to Weil Positivity" — claims RH via "closure together with the restricted odd Weil criterion" from a certified endpoint Y = 7 and Schur induction. By its own abstract a Weil-positivity certificate argument, i.e. inside the ground the zoo's IV.1 family marks (a proof-side external claim; the program's  screen is disproof-side). No action; if the next digest's §B wants a sentence, this is it.
- Shi, 2609.04908 (4 Sep 2026), finite Hilbert–Pólya matrices from Weil's explicit formula — "No proof of RH is claimed"; a reconstruction theorem with the ordinates as inputs; III.13's ground.
- Mishra–Sarkar 2609.26787 (Robin-type finite inequality equivalent to RH) and Shunia 2609.30306 (120-state Turing machine halting iff RH false) — equivalence-level; no bearing on any direction.

## Hashes (10(i))
poll.py ef520fd95bdc4fd2…; poll-output.txt ded856e692acd8ff…; abstracts.txt a228020fbe9b9d65…; lamzouri v1 txt 4d1c606d8ce2ddee…; v2 txt de455968b82d0b60…; v1→v2 delta 44b8cab6fcc687fb…; nikolaev txt 456e477643254fab…; upstream-head.txt 91ceeedd51076276…. PDFs (third-party) local-only in `rh-program/fetched-watch/` (gitignored this session).

## Re-run
`python3 results/watch-poll-s34/poll.py` — move `SINCE` forward to the last poll date; add any new watch item as a row of `searches` or `ids`. Orchestrator cost only.
