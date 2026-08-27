# A structured research program on the Riemann hypothesis

This repository is the complete, unedited record of a research program on the Riemann
hypothesis: every proposal, every computation, every adversarial review, every mistake, and
every correction, in the order they happened.

It is public because two of the papers below cite it as their data-and-code source, and a
citation you cannot follow is not a citation.

**Author:** Kunal Tyagi &lt;hello.jay.tyagi@gmail.com&gt;

**Use of AI, stated plainly.** The mathematics in this repository — the derivations, the
computations, the verification suites, the Lean formalization, and the text of the papers — was
produced by **Claude (Anthropic)** working under the author's direction inside this program. The
author set the objectives, adjudicated the decisions, and is responsible for the content. Claude
is a tool and is not an author. The same statement appears in a footnote on page 1 of every
paper. Because the whole program record is here, that disclosure is checkable rather than
merely asserted: `anthropic/rh-program/LOG.md` is the session-by-session history.

---

## The papers

All four are built and pass an automated submission check
(`anthropic/rh-program/results/arxiv/check-submittable.sh`). **Two are recommended for
circulation and two deliberately are not** — the reasoning is in
`anthropic/rh-program/results/arxiv/README.md`.

| Paper | PDF | Pages | Status |
|---|---|---|---|
| The two-moment certificate is robust under Rudnick–Sarnak-range cubic augmentation with capacity control | [`results/arxiv/a4-no-go/main.pdf`](anthropic/rh-program/results/arxiv/a4-no-go/main.pdf) | 44 | **recommended for posting** |
| Products of the per-prime Tate curves of absolute geometry carry no correspondence calculus for the Weil explicit formula | [`results/arxiv/seed-no-go/main.pdf`](anthropic/rh-program/results/arxiv/seed-no-go/main.pdf) | 21 | **recommended for posting** |
| The polarized-Frobenius axiom class | [`results/arxiv/m0-axiom/main.pdf`](anthropic/rh-program/results/arxiv/m0-axiom/main.pdf) | 14 | internal record — not recommended for posting |
| Castelnuovo–Severi/Hodge index from Riemann–Roch and ampleness | [`results/arxiv/m1-noncirc/main.pdf`](anthropic/rh-program/results/arxiv/m1-noncirc/main.pdf) | 13 | internal record — claims zero novelty in its own abstract |

**All four are negative results.** None claims to prove anything about the Riemann hypothesis.
Each shows that a specific proposed route does not work, and says exactly how far the failure
extends. The sorting criterion for the table above is not novelty but *would anyone otherwise have
tried this* — a negative result earns publication when it stops someone wasting time.

## What a skeptical reader should check first

The strongest evidence here does not require trusting anyone.

* **`anthropic/rh-program/results/d1-*/` (Lean).** Twelve theorems of the A4 paper are
  machine-checked in Lean 4 against a pinned Mathlib. `#print axioms` on all twelve returns
  `[propext, Classical.choice, Quot.sound]` — no `sorryAx`, no `Lean.ofReduceBool`. A whole-tree
  scan finds zero real `sorry` or `admit` across the development. Build it yourself and the
  claim stands or falls without reference to any prose.
* **`anthropic/rh-program/results/arxiv/citation-verification/`.** Every citation in the four
  papers was checked against a primary source before it was allowed into a file. Twenty-one
  proposed citations did **not** survive that check and were rejected; each rejection is recorded,
  dated, inside the paper it would have touched. `ADJUDICATION.md` settles the cases where two
  independent checks disagreed.
* **`anthropic/rh-program/results/c3-r/prior-art-r7a.md`.** Carries two dated **withdrawals** of
  its own earlier conclusions. The seed-no-go paper's first three theorems turned out to be
  Winkelmann's, from 2002; the paper now says so in its abstract.

## Layout

```
anthropic/rh-program/
  STATUS.md            the always-current dashboard: where the program is, what is next
  LOG.md               append-only session history — what was tried, and what was wrong
  BARRIER-ZOO.md       the taxonomy of obstructions the program has hit and banked
  CIRCULATION-PREP.md  the record of preparing the four papers for circulation
  directions/          the research directions, with their proposals retained verbatim
  results/             all output: papers, gate records, referee reports, raw data, Lean
  results/arxiv/       the four submission packages, and the guide to them
  scripts/             the multi-agent workflow scripts used to run reviews and checks
```

Not in the repository, deliberately: the program's PDF library of fetched literature
(`fetched/`, `fetched-r2/`, `fetched-r3/`), which is third-party copyrighted material and is not
redistributable. **Nothing in any paper depends on it** — every external claim is cited to its
published source.

## Honest limitations

* Two of the four papers are internal documents, listed above as such. One of them says in its
  own abstract that it claims zero novelty. That is not modesty; it is accurate.
* Several notes elsewhere in `results/` carry unpaid referee debts and are marked
  not-circulation-ready in `CIRCULATION-PREP.md`. They are here for completeness, not as claims.
* The program record includes its own errors. That is the point of publishing it.

## License

**Not yet chosen.** Until the author selects one, default copyright applies and the material is
readable and checkable but not licensed for reuse. Suggested, if and when he wants one: **CC BY
4.0** for the papers, notes and data, and **MIT** or **Apache-2.0** for the code and the Lean
development — the usual split for a repository of this shape. Adding a `LICENSE` file is the
author's decision to make, not the program's.
