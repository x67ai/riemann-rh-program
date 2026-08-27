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

## The A4 body pass — DONE 2026-08-27

Executed in three commits: `e8c9ff5` (the pass), `2db51b4` (the fixes its audit
found), `6938d57` (source rewrap, cosmetic).

**The counts.** `grep -ci "the gate\|adjudicat\|supplementary material\|direction A4\|deliverable"`
went **64 → 2**, and both survivors are justified line by line: the `\thanks`
footnote's use-of-AI disclosure ("the author ... adjudicated its decisions"), and
the real repository path `results/adjudication-A4.json` in the availability list.

**What was done, by class.**

* **`the gate` (40 → 0 in prose).** Judged per occurrence into the three senses
  the work order identified. Most became "the decision program", "the decision
  LP", "the computation", "the row system", or a property of the paper itself
  ("the primary geometry", "the admissible pair class") with a section pointer so
  the reader can check it. The 20 remaining string matches are all inside the
  path `results/a4-m2-gate/`, which is a real directory.
* **`adjudicat*` (15 → 1).** Where the sentence carried mathematics, the
  mathematics is stated directly. Where it was a repair label naming a real fix
  (`Theorem 1(ii)-repaired`, `R4: θ < 1 strict`, `repair R6`), the label was
  retired at *all* its sites together and replaced by the fact.
* **`supplementary material` (5 → 0).** Decided as Option B: the three companion
  documents are named and given their repository paths, matching the availability
  list. The pair-channel item now says plainly that Theorems 4.6 and 4.7 are
  proved there and only their proof architecture is given here.
* **`the program` (7 → 0), `direction A4` (2 → 0), `deliverable` (2 → 0).**

**The completeness sweep the work order asked for** found, and retired, a whole
tier the enumeration missed: Tier-1/Tier-2/Tier-A (13 sites, including the
surviving superscript `P^{T2}`), the milestone labels M2/M4/M5, R1–R7 in the
body, "the campaign", "this session", "shipped", "quarantined", "the audit's
finding N", "the direction file", session date stamps inside theorem statements,
JSON keys quoted as row names, and an unused `\newtheorem*{datedrev}`.

**§1.1–§1.3 were re-read cold** and the first two pages now refer to nothing the
reader cannot open. Gaps the de-internalization exposed were closed at the same
time: `P_base`/`P_full` are defined where the question is posed rather than 300
lines later; "bite" and "absorption" are glossed at first use (both were used
unglossed nine times downstream and in the abstract); so are "garnish", the
capacity fuzz row, `δ₀'`, `ε₃`, `Γ`, `B₁/B₂/B₃`, `p(c)`, `Sgen`, `ν_joint`,
`Φ₀`, "admissible", and the stop rule; and the baseline rows are numbered
(R-1)–(R-4) so the (R-5)–(R-9) sequence is no longer a fossil with a gap.

**`abstract.txt` is now generated from the TeX abstract, never hand-edited.** It
had been missed entirely and still carried "Direction A4 proposed" and "the
gate's R5 depth family" — the one artifact arXiv shows before the paper itself.

**Verification.** Sixteen agents across two workflows: six to propose the edits
per class and six to adversarially verify them, then four independent audit
lenses over the result (lost caveats, cold readability, fresh completeness sweep,
mathematical integrity). The integrity lens diffed every numeric literal, every
inline and display math span and all 35 theorem-family blocks between the before
and after files: **no mathematics changed.** Every scholarly caveat survives,
reworded rather than cut — the eight break attempts, flag F4's unproven bridge,
the (O1)–(O5) residue, the three [BGSTB24] riders, the pricing-is-heuristic
caveat, the audit's binding wording bar, and the "only fully clean-stop runs"
note. `bash results/arxiv/check-submittable.sh` prints ALL CHECKS PASSED, 41 pp.

## Left for the sponsor

1. **The ~40 `\texttt{}` script pointers in the body.** Untouched, as the work
   order said: this is the sponsor's call, not the program's.
2. **Nine bibliography entries are never cited in the body** (LR21, Mon73, Hej94,
   CGG98, KLS07, KLS11, CdLS22, KS66 and one more), several carrying annotations
   that state where they are cited. Citation style is also mixed — `\cite{}` in
   some places, hard-coded `[P]`, `[RS96]`, `[BGSTB24]` in others. Both are
   tidy-ups a referee would notice; neither is a de-internalization question.
3. **`θ` carries three unrelated meanings** (the ladder parameter in "θ < 1
   strict", grid positions θ_i, and the bandwidth offset). Fixing it means
   renaming a variable throughout, which is a mathematics edit, not a wording one.
4. **`pair-channel.md`, `theorems.md` and `data-tables.md` are themselves full of
   internal narration** ("Program: RH program, direction A4", "standing order 5",
   "AUDIT finding MINOR-4", pointers into `sources-extracted/` and `fetched-r3/`).
   The paper now cites them by repository path, which is honest. But if they are
   ever to ship as arXiv ancillary files — and `pair-channel.md` carries proofs
   the paper defers to — they need the same pass this paper just had.

---

## Original work order (retained for the record)

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
