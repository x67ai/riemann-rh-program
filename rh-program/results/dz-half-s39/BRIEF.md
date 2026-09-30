# UNIT `dz-half-s39` — Diamond–Zhang's random Beurling system has β₀ = ½ almost surely (digest U5a; the Theorem-B mechanism at α = 1) — BRIEF

**Written Session 39, 2026-10-01 (orchestrator Fable 5.1). Agent: Opus, default effort. Ranked unit 4 of the wave-2 digest (§F.2): a print-grade lemma settling the sharpest in-print test of Conjecture U.** Folder: `results/dz-half-s39/` — `NOTE.md`, `SHARED.md` (dated blocks as you go), `verify/`, `sources/`. Paths contain spaces — quote them. U.S. English. Do not commit. Do not edit files outside your folder.

## The record (read first, at the line)
`results/novel-wave-s37/beurling-frontier/read-O.md` §4 A3 and §7(a): the sketch "the Theorem-B one-scale mechanism at α = 1 gives β₀ = ½ a.s. for the Diamond–Zhang random construction (Bernoulli selection from the grid v_k = n + ℓ/2ⁿ), answering BDR's footnote 4 ('Most likely the value of β₀ equals 1/2')"; `beurling-frontier/NOTE.md` Theorem B (the one-scale variance σ_B² ≍ x^α/log x, the 0–1 law, Berry–Esseen) as repaired by read-O F2 (the coprime sums T_d, κ_p); the digest §F.2 item 4 (contract clause: "for almost every realization of the DZ construction, N_B(x) − k₂x ≠ O(x^τ) for every τ < ½"). Sources at the page: Diamond–Zhang, *Beurling Generalized Numbers* (AMS 2016), Thm 17.14 and its construction (on disk? grep `fetched*/` and `sources-extracted/`; if absent, the construction as quoted in BDR 2309.01567 v2 = Trans. AMS 378 (2025) 477–501, `beurling-frontier/sources/`); BDR p. 3 fn. 4.

## Contract clause
THEOREM (to prove): for almost every realization of the Diamond–Zhang construction, the integer counting function satisfies N(x) − ρx ≠ O(x^τ) for every τ < ½; together with DZ's own upper bound this gives β₀ = ½ a.s. Close T (a proof, every step written; the dependence structure across (x/2, x] handled explicitly — the read-O sketch's one named risk), or G (the exact step that fails, as a theorem: "the Theorem-B decomposition fails on DZ's grid because …"), or a citation if a paper after BDR settles fn. 4 (cite at the page; check arXiv listing for Beurling generalized numbers 2024–2026 and BDR's citers).

## Method
Ladder: the finite rung (simulate the DZ construction to x = 10⁸, five seeds; measure the sup-slope and the dyadic mean square against ½; controls: the deterministic grid without selection (β = 0 or its exact value), and the frontier's random surgery at α = 1); then the proof. Every constant re-derived; the variance computed two ways (exact sum over the grid; the Theorem-B route). Labels as usual; distance-from-upstream line (10(n)): nearest published object = Theorem B of the frontier NOTE and DZ Thm 17.14 — say exactly what is new. Compute policy: ≤ 1 heavy local process at a time (`ps -Ao pcpu,comm | awk '$1>50'`; wait if ≥ 4 run); ≤ 30 min per run.

**Stop and report when:** the dependence across (x/2, x] cannot be controlled by the Theorem-B decomposition and no alternative (martingale / second-moment on dyadic blocks) works — report the exact failing inequality; or a printed result settles fn. 4.

## Close
`NOTE.md` §0 with the close as a theorem; an Instruments row in `directions/B2-refutation-program.md`'s shape; Untried entries; the waste line.

HARD OUTPUT RULE: never write more than about 6 kB of text in a single response or tool call. Build every deliverable incrementally on disk — create the file, then append one section (or five table rows) at a time — and append a dated block to SHARED.md after each batch. Keep reasoning between tool calls short; think in the files, not in long messages. Your final report is under 60 lines.
