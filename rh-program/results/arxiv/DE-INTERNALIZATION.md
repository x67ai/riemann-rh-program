# Work order — make the two outgoing papers standalone

**Opened 2026-08-27** after the sponsor read page 1 of the A4 PDF and asked, correctly, why the
project's internal narration was in a finished paper, and why the abstract's first sentence
referred to "the parent paper" as though the reader knew which one.

He is right, and the earlier "externalization pass" (commit `afd2cdd`) did not fix it. That pass
was cosmetic: it renamed session numbers to dates and rewrote the evidence list, and left the
apparatus standing. **The test to apply to every line: would a reader who has never heard of this
program understand it, and can they check it?** If not, it is either cut or rewritten.

## Done in this session

**A4** (44 pp → 41 pp)

* **Deleted both `datedrev` changelog blocks from page 1.** They narrated a revision history — "the
  interval hardening found the earlier ratio to be a grid artifact", "an independent novelty
  re-check was run before circulation" — which is version-control information, not scholarship.
  Verified before cutting that the substantive re-scoping is stated independently in the body
  (§4.3, §7, §8; the constant `0.98465` appears at four separate places), so nothing was lost.
* **Deleted the `Program: / Date: / Evidence discipline:` front block** — "RH program, direction
  A4 (merged A2+A4 cubic-certificate direction)", "this paper is that gate's absorption branch".
* **Deleted the 144-line `Revision record (2026-08-26)` section**, a referee-repair changelog
  (R1-M1, R2-m7, …). On arXiv, revision history is the v1/v2 mechanism, not a section.
* **Rewrote the abstract's first sentence.** Was: *"The parent paper's unconditional two-thirds
  theorem rests on a two-moment certificate…"*. Now names Alpöge and Furman, states their theorem,
  and cites `[P]` — in the first sentence, where the reader needs it.
* Removed four bibliography pointers into the excluded PDF corpus (`fetched/w-09` and friends).

**Seed no-go** (21 pp, unchanged)

* `Route A` / `Route C` / `M2b` / `N2` → named mathematically ("the characteristic-one square of
  Connes and Consani", "Deninger's foliated-dynamical route").
* "What dies / what does not die" → "What the no-go rules out / What it leaves untouched".
* Provenance remark trimmed of the program narration (the prior-art gate's search-phrasing counts,
  the barrier-taxonomy entry number, the "companion program note" pointer); the two genuine
  limitations it recorded — Akatsuka read via Tanaka, quotations checked against full texts — are
  kept, because those are scholarly caveats rather than internal process.
* "this note" → "this paper"; "the commissioned calculus" → "the required calculus".

Its abstract was already fine: it opens by naming Connes and Consani.

## Remaining — the A4 body pass

Counts as of this commit, in `a4-no-go/main.tex`:

| Term | Count | What to do |
|---|---|---|
| `the gate` | 40 | **Judgment per occurrence.** It means three different things: (i) the decision linear program itself, (ii) the pre-registered specification, (iii) the whole decision episode. Render (i) "the decision program", (ii) "the pre-registered specification", (iii) "the computation". Do **not** sed it — the paper defines the object properly in §1.3 and §2, so most occurrences only need the noun swapped. |
| `adjudicat*` | 15 | Attribute the *mathematics* directly and drop the process. "The adjudication ordered seven repairs" → state what the repairs were, or cut. Where it is genuinely a provenance claim, it belongs in the Provenance section, not the body. |
| `supplementary material` | 5 | Points at three companion documents: `theorems.md`, `pair-channel.md`, `data-tables.md`. **Decide once:** either inline what the paper actually relies on, or cite them as repository artifacts with their paths, as the availability section already does. The present half-way form — an italic phrase with no locator — tells the reader nothing. |
| `the program` | 7 | Usually removable. |
| `direction A4` | 2 | Remove; the paper is about a question, not a direction. |
| `deliverable` | 2 | Remove. |

Then: re-read §1.1–§1.3 end to end as a stranger would. That is where the paper still frames
itself as an internal answer to an internal question, and it is the part a referee reads first.

Also check both papers for: `\texttt{}` references to scripts in the body (~40 in A4). These are
defensible — the paper's headline is an exact equality with a hand-checkable witness, and the
repository is public so they resolve — but they are worth thinning to one pointer per section if a
more conventional look is wanted. **Sponsor's call, not the program's.**

## Acceptance test

1. `grep -ci "the gate\|adjudicat\|supplementary material\|direction A4\|deliverable" a4-no-go/main.tex`
   returns a number you can justify line by line.
2. Read the first two pages aloud. Nothing in them refers to a document the reader cannot open.
3. `bash results/arxiv/check-submittable.sh` still prints ALL CHECKS PASSED.
