# D1 M2a Lane A — phase 3(d) AUDIT (Job 2, independent checker per KICKSTART 10(f))

**Auditor:** Opus (second model), Session 19. **Stamp:** 2026-09-09 22:08–22:16 IST, machine clock.
**Scope:** BRIEF-3d.md Job 2, against the emitter's Job 1 output (`EMIT-NOTES.md`).
**Authorities read, in the brief's order:** `PLAN.md` §1.1, §1.5, §2.4; `PLAN-REVIEW.md` §6 and F-1…F-6;
`SPEC.md` §3.6, §3.7; `v11/GLUE-NOTES.md`; `RUN-REPORT.md` §6; `BRIEF-3d.md`.
**Thermal:** `pgrep` checked before every heavy step; exactly one `lake` process at a time; no producers run.
**Rule:** the auditor edited no file in the Lean tree and no file the emitter wrote.

## Verdict: **FIX-FIRST**

Everything trust-critical is **OK and independently reproduced**: the build, the eight `#print axioms`, the
displayed hypotheses, the 50 integers, the code-only diff, the trust greps, the label wording, and the two
substantive honesty facts (the y-band asymmetry and C-A6-not-consumed) are all present and correct.

Two **documentation-accuracy defects** were found, both numeric, both in trusted files, neither touching
soundness, the build, the axioms, the integers or the label. They are text-only edits (A-1, A-2 below).
A-1 is the one the brief singles out for checking ("the y-band asymmetry … stated, not glossed"): the figure
as written is wrong by a factor of 1.58 and contradicts the two decimals printed beside it in the same
sentence, so it fails that check on its own terms. Hence FIX-FIRST rather than CLEAN.

---

## 1. Table — every check of BRIEF-3d.md Job 2

| # | Check | How the auditor did it (independently) | Result |
|---|---|---|---|
| 1 | `lake build Zeta23` from a clean state | Deleted the `.olean`/`.trace` of `DBN.Asym`, `Instance02`, `Instance02.Asym_mp`, `Instance02.Asym_arb` so the four modules — and both `decide +kernel` calls — genuinely re-elaborated, then `lake build Zeta23`. Log `audit-rebuild.log`. | **OK.** `Built Zeta23.DBN.Asym (1.6s)`, `…Asym_mp (1.6s)`, `…Asym_arb (1.6s)`, `…Instance02 (1.5s)`, `Build completed successfully (9142 jobs)`, **7.23 s wall**. Zero errors; zero warnings from any DBN module (the only warnings in the log are pre-existing Mathlib deprecations in `Taper/` and `XiPrime/`). |
| 2 | `#print axioms` on the eight names, compared with `final-axioms.log` | Auditor's own probe `audit-axioms-scratch.lean` (written from scratch, not the emitter's file; it adds eight further names), `lake env lean`, 2.10 s. Log `audit-axioms.log`. | **OK, identical to `final-axioms.log`.** `lambda_le_point2`, `lambda_le_point2_arb`, `row2_ray_mp`, `row2_ray_arb`, `row2_laneA_mp`, `row2_laneA_arb` → `[propext, Classical.choice, Quot.sound]`; `row2AsymMP_check`, `row2AsymARB_check` → `[propext]`. Auditor's additions also clean: `cert_of_checkAsym` and the six `_t0/_y0/_yA` facts → the three standard axioms. **No `sorryAx`, no `Lean.ofReduceBool`** (i.e. no `native_decide`) anywhere. |
| 3 | The four theorems display exactly H1, H2-B, `hAsym`, `hTail`, H3 and nothing else | `#check @…` on all four in the same probe; read the elaborated types. | **OK.** Each of `lambda_le_point2`, `lambda_le_point2_arb`, `row2_ray_mp`, `row2_ray_arb` takes exactly five hypotheses in this order: `ZeroVerification (116733/200000) 2500000097429` (H1) → `BarrierEnclOK (fun t z => Ht t z / Bt t z) row2Barrier*` (H2-B) → `AsymEnclOK (fun z => Ht (93/500) z / Bt (93/500) z) row2Asym*` (H2-A, `hAsym`) → `TailOK (fun z => Ht (93/500) z / Bt (93/500) z) row2Asym*` (H-TAIL, `hTail`) → `Polymath15Bridge' ∧ HtEntire` (H3). Nothing else. **MP literals in the mp theorems, ARB in the Arb theorems** — the legs are not merged (D-R3). |
| 4 | The glue lemma's conclusion is character-for-character the former `hLaneA` type | Elaborated `#check` output vs `PLAN.md` §1.1's verbatim binder. | **OK.** `row2_laneA_mp` / `_arb` conclude `∀ (x y : ℝ), 5000000194858 + 1 ≤ x → 16733 / 100000 ≤ y → y ^ 2 ≤ 1 - 2 * (93 / 500) → Ht (93 / 500) (↑x + ↑y * Complex.I) ≠ 0` — identical to §1.1 modulo the coercion arrows the elaborator prints. |
| 5 | Re-run the back-parse | `python3 backparse_lane_a.py ~/rh-lean-work/zeta-23-lean-main asym-mp.json asym-arb.json`, exit 0. Log `audit-backparse.log`. | **OK, reproduces `backparse.log` line for line.** 50 integers compared exactly (25 per leg), 0 mismatches; cross-leg 0 mismatches. |
| 6 | Independent integer check (auditor's own path, no shared code) | The brief's back-parse re-run only re-runs the emitter's own script, so the auditor added a second, disjoint path: `#print` the two literals **as the kernel elaborated them** (from `audit-axioms.log`, i.e. from the `.olean`, not from the source text) and compare every field with `asym-{mp,arb}.json`. Script written for this audit; log `audit-kernel-vs-json.log`. | **OK. 50 integers, 0 mismatches.** K = 10²⁴ / 10¹², `N_start` 630783, N range [630783, 5140999], `N₁` 5141000, all as the brief specifies. The auditor also re-derived the checker conditions by hand from the printed literals: **C-A1** yA² = 15700003556329/(25·10¹²) ≥ 157/250 = 1 − 2t₀ ✓ and y₀ < yA ✓; **C-A3** E < T on all three rows, both legs ✓; **C-A4** rows consecutive (746495+1 = 746496; 1469440+1 = 1469441) ✓; **C-A5** last `Nhi` + 1 = 5140999 + 1 = 5141000 = N₁ ✓; **C-A6** Σ/K = 1.996999372832 (mp) and 1.996999372834 (Arb), both < 2 ✓. |
| 7 | Diff `Instance02.lean` against git HEAD of the mirror | The autocommit watchdog committed the emitter's work at 22:09 (`bf013f1`), so HEAD had already moved; the auditor diffed against the **pre-change** commit `5a4b06b` instead. To separate code from prose the auditor stripped Lean comments and docstrings from both revisions with its own stripper, then diffed the code. | **OK.** The code-only diff is **exactly PLAN §1.5's prescribed set and nothing more**: 2 imports added (`Zeta23.DBN.Instance02.Asym_mp`, `…Asym_arb`); the `hLaneA` binder replaced by the `hAsym`/`hTail` pair in all four theorems; the consumption token `hLaneA` → `(row2_laneA_mp hAsym hTail)` at line 169's `refine` and `(row2_laneA_arb hAsym hTail)` at line 188's; the two `lambda_le_point2*` bodies pass `hAsym hTail`. **No other line of code moved** — the barrier theorems, `hHol_of_entire`, `hH1_row2`, `row2Rect_*`, `row2_bound_le_point2` are byte-identical. `hLaneA` is **gone from code** everywhere in the tree. |
| 8 | Nothing else in the tree changed | `find` for `.lean` files touched today; byte-compare of the whole mirror. | **OK.** Only `Zeta23/DBN/Instance02.lean`, `Instance02/Asym_mp.lean`, `Instance02/Asym_arb.lean` (this job) and `Zeta23/DBN/Asym.lean` + the root `Zeta23.lean` (phase 3(c), earlier the same day). `Defs.lean`, `BarrierCert.lean`, `BtFacts.lean` and **all 116** `Instance02/` modules (the 114 Lane B literals included) are `cmp`-identical to the mirror. |
| 9 | Trust greps over `Zeta23/DBN/` | Re-run independently and **more strictly** than the emitter's: comments and docstrings stripped **first**, then the code grepped, over all 121 `.lean` files, for `sorry`, `native_decide`, `axiom`, `unsafe`, `implemented_by`, `extern`, `opaque`, `hLaneA`, `ofReduceBool`, `trust_me`, `lean_evalConst`. Log `audit-trust-greps.log`. | **OK — zero code hits for every pattern.** The raw counts (`sorry` 3, `native_decide` 116, `axiom` 5, `hLaneA` 12) are **all prose**: the `native_decide` hits are the 116 literal modules' "no `native_decide`" header lines; the `axiom` hits are five `#print axioms` sentences; the twelve `hLaneA` hits are the dated historical records in `Instance02.lean` and the two new module headers. Zero `axiom` declarations of the project's own. |
| 10 | SHA-256 (10(i)) and the mirror copies | `shasum -a 256`, `cmp`. | **OK, all three match `EMIT-NOTES.md` §5 exactly.** `Asym_mp.lean` `128eb310…7ac05`, `Asym_arb.lean` `767ee500…81987`, `Instance02.lean` `bcf81f5e…fce7cf9850`; `asym-mp.json` `7a99eedb…`, `asym-arb.json` `b7d1a782…`. Tree and mirror byte-identical on all three. |
| 11 | Label wording — `lean/README.md` | Read the R-1 paragraph (lines 140–152) and the dated note (154–186) against `SPEC.md` §3.7 and `PLAN-REVIEW.md` §6. | **OK.** The R-1 paragraph is **kept, not deleted**, and marked superseded by a dated block. The label appears verbatim: *"kernel-checked modulo H1, H2 (H2-B, H2-A, H-TAIL), H3"*; "never 'fully machine-checked'" is present. PLAN-REVIEW §6 is quoted verbatim as a block quote, all four bullets. The short public sentence is declared licensed with §3.7's gloss and R-1 correctly called **discharged, not reversed**. A new "M2a Lane A (2026-09-09)" section, a table row, an opening-paragraph sentence and the licensing count are all added. |
| 12 | Label wording — `v11/GLUE-NOTES.md` | Read the input table (lines 11–12), the honest-label block (90–106), the dated block (108–136) and "Left for the Lane A stream" (138–154). | **OK.** The 2026-09-06 H2-A row is kept and a dated 2026-09-09 row added beside it; the old honest-label block kept and superseded by a dated one carrying §3.7's label verbatim; "Left for the Lane A stream" now reads **STATUS: DONE (2026-09-09, Session 19)**. |
| 13 | Label wording — `RUN-REPORT.md` §6 | Read the 2026-09-09 dated note. | **OK.** Item 3 recorded LANDED with the full evidence trail; item 4's short sentence declared licensed with §3.7's gloss; the cut line moved to **item 5 (packaging)**; the label verbatim; and the honest closing sentence "Λ ≤ 0.2 is still not proved … the bracket of record stays 0 ≤ Λ ≤ 0.2 on the literature" is retained. |
| 14 | C-A6 kernel-checked but **not consumed** (PLAN-REVIEW F-6) — stated, not glossed | Grep and read in all five places. | **OK, stated everywhere and stated correctly.** Both literal module headers carry a dedicated "WHAT THE KERNEL DOES NOT USE" paragraph naming C-A2, C-A6 and C-A1's yA² ≥ 1 − 2t₀ as checked-but-never-consumed, and the sentence *"'C-A6 is kernel-checked' must not be read as 'the tail reduction is kernel-checked'"*. Repeated in `Instance02.lean`'s header, `lean/README.md`, `GLUE-NOTES.md` and `RUN-REPORT.md` §6. **The auditor verified F-6 in the proof itself, not from the report** — see §4 below: `cert_of_checkAsym`'s single `obtain` names exactly `hK`, `hrows`, `hcons`, `hN1` and discards every other conjunct with `-`. |
| 15 | The y-band asymmetry — stated, not glossed | Grep and read in all ten places; then check the arithmetic. | **Stated everywhere — but the figure is wrong. See FIX A-1.** |
| 16 | Cross-leg cross-check and the F-2 widened tolerance | Read `crosscheck-full.txt`, `crosscheck-full-default.txt`, `BUILD-NOTES.md` lines 108–110, and recomputed the ratios. | **OK, and F-2's prescribed fix was followed exactly.** The default run (`--etol 1e-3`) records `DISAGREEMENT — stop the line` on the three E ratios and is **kept on disk**; the accepted run widens `--etol` to 0.3 and is CONSISTENT. T agrees to ≤ 4.18·10⁻⁷⁹ and Q₁…Q₄ to ≤ 4.9·10⁻⁸¹ (RUN-REPORT's "≤ 5·10⁻⁷⁹" is correct), `ok = True` on both legs, `S1`–`S4` true, `direct-contained` true — so the trip is hull slack on E, exactly the benign case F-2 anticipated, and the widened tolerance is recorded. The apparent conflict between the two ratio triples in the record (`1.027/1.110/1.207` in `crosscheck-full.txt`, `1.027/1.124/1.261` in `backparse.log` and the module headers) is **not** a disagreement: `crosscheck` prints (arb − mp)/arb, `backparse` prints arb/mp, and 1/(1 − 0.10998) = 1.1236, 1/(1 − 0.20719) = 1.2613. Both are right under their own definition. |
| 17 | Emitter's measured quantities, spot-checked | Recomputed from the literals. | **OK.** T/K = 0.012023, 0.012022, 0.154429 (both legs); E/T = 8.57e-06, 6.30e-06, 1.38e-07 (mp) and 8.81e-06, 7.07e-06, 1.74e-07 (Arb) — RUN-REPORT's "E/T ≤ 9·10⁻⁶" holds. Window counts 115713 + 722945 + 3671559 = 4510217 ✓. Line counts 246 / 117 / 117 as `lean/README.md` states ✓. |

---

## 2. FIX A-1 — the y-band figure is the gap in the **squares**, not the gap in y (wrong by ×1.58)

**Severity:** documentation accuracy in trusted files. Not a soundness defect: the glue lemma derives `y ≤ yA`
from `y² ≤ 157/250` by `le_of_sq_le_sq` and the kernel confirms `yA² ≥ 1 − 2t₀`, both verified above. Nothing in
any proof depends on the figure.

**What is written** (ten places; the sentence is PLAN-REVIEW §6's, propagated):

> yA = 0.7924646 is **1.5·10⁻⁷ wider** than √(157/250) = 0.79246451…

**Why it is wrong.** "Wider than", applied to yA and √(157/250), is the difference of those two numbers:

    yA            = 0.7924646
    √(157/250)    = 0.7924645102463579725099031560295…
    yA − √(157/250) = 8.975364202749…·10⁻⁸  ≈  9.0·10⁻⁸        <- the true y-gap

The quoted 1.5·10⁻⁷ is the gap in the **squares**, which `PLAN.md` §1.5 states correctly and which the auditor
confirmed exactly:

    yA² − 157/250 = 3556329 / (25·10¹²) = 1.4225316·10⁻⁷        <- the gap in the squares

So the figure is off by a factor of 1.58 and — worse for a file whose purpose is honest labeling — it
**contradicts the two decimals printed beside it in the same sentence**: a reader who subtracts 0.79246451 from
0.7924646 gets 9·10⁻⁸, not 1.5·10⁻⁷. In `Asym_mp.lean` / `Asym_arb.lean` the correct squares figure
(`yA² − 157/250 = 3556329/(25·10¹²)`) appears **four lines above** the wrong y figure, in the same header.

**Where.** Eight occurrences in the corpus's own voice — these are the ones to fix:

| File | Line |
|---|---|
| `~/rh-lean-work/…/Zeta23/DBN/Instance02/Asym_mp.lean` (and the mirror) | 51 |
| `~/rh-lean-work/…/Zeta23/DBN/Instance02/Asym_arb.lean` (and the mirror) | 51 |
| `~/rh-lean-work/…/Zeta23/DBN/Instance02.lean` (and the mirror) | 72 |
| `rh-program/lean/README.md` | 215 |
| `rh-program/results/d1-m2a/v11/GLUE-NOTES.md` | 133 |
| `rh-program/results/d1-m2a/RUN-REPORT.md` | 142 |
| `rh-program/results/d1-m2a/lane-a/EMIT-NOTES.md` | 55, 68 |

Two further occurrences are **verbatim quotations** of PLAN-REVIEW §6 — `lean/README.md` line 179 (inside the
block quote) and `PLAN-REVIEW.md` line 170 itself. A direct quotation keeps its source's wording, so **do not
edit the block quote**; correct the source instead, with a dated note, and the quote then follows.

**Exact fix.** In each of the eight, replace the figure with the y-gap and keep the squares figure where the
distinction is worth making. Suggested wording, which is both correct and self-consistent with the printed
decimals:

    yA = 0.7924646 is 9.0·10⁻⁸ WIDER than the conclusion's y ≤ √(157/250) = 0.79246451…
    (equivalently yA² − 157/250 = 3556329/(25·10¹²) = 1.42·10⁻⁷ in the squares)

And in `PLAN-REVIEW.md` §6, append a dated correction under the third bullet rather than rewriting it:

    [DATED CORRECTION 2026-09-09, phase-3(d) audit.] "1.5·10⁻⁷ wider" above is the gap in the SQUARES
    (yA² − 157/250 = 3556329/(25·10¹²) = 1.4225·10⁻⁷).  The gap in y itself is yA − √(157/250) =
    8.975·10⁻⁸ ≈ 9.0·10⁻⁸.  The bullet's point — that TailOK's y-band is a hair WIDER than the
    conclusion's, so TailOK is not literally a sub-statement of hLaneA — is unaffected.

The substantive claim survives the correction untouched: yA is genuinely wider, both directions are genuinely
covered, and `TailOK` is genuinely not a sub-statement of `hLaneA`.

## 3. FIX A-2 — "Arb/mp = … 1.000000 on E₁" understates the Arb leg's excess

**Severity:** documentation accuracy in the two literal modules' transcript blocks (trusted files). No effect on
any proof — the E₁ values are per-leg and never compared by the kernel.

**Where.** `Asym_mp.lean:58` and `Asym_arb.lean:58` (and both mirror copies), in the cross-check sentence:

> the E upper bounds are hull bounds, Arb's the larger on every row, Arb/mp = 1.027, 1.124, 1.261 on rows 0–2
> and **1.000000** on E₁, recorded not gated, etol 0.3

**Why it is wrong.** E₁ is 1823 at K = 10¹² (Arb) against 1822923348119831 at K = 10²⁴ (mp):

    1823 / 1822.923348119831 = 1.0000420488…   ->  1.000042, not 1.000000

`backparse.log` and `audit-backparse.log` both print the correct `Arb/mp = 1.000042`, and
`crosscheck-full.txt` prints the same as `rel 4.3e-08`. Writing `1.000000` in a sentence whose own subject is
"Arb's the larger on every row" rounds the excess away and reads as exact agreement — the wrong direction of
error for a file whose job is to record what the two producers did *not* agree on.

**Exact fix.** In both module headers, `1.000000 on E₁` → `1.000042 on E₁`. Then re-copy both files to the
mirror and re-record their SHA-256 in `EMIT-NOTES.md` §5 (the two hashes change; `Instance02.lean`'s does not
unless A-1 also touches it, which it does — so re-record all three).

## 4. F-6 verified in the proof text, and found to be conservative

PLAN-REVIEW F-6 says `cert_of_checkAsym` consumes only K ≥ 1, C-A3, C-A4 and C-A5, and that C-A2, C-A6 and
C-A1's yA² ≥ 1 − 2t₀ are checked but never used. The auditor did not take this from the report: it is visible in
the proof's own destructuring, in `Zeta23/DBN/Asym.lean`, where every unused conjunct is discarded with `-`:

    obtain ⟨⟨⟨⟨⟨⟨⟨⟨⟨⟨⟨⟨⟨⟨⟨⟨⟨hK, -⟩, -⟩, -⟩, -⟩, -⟩, -⟩, -⟩, -⟩, hrows⟩, hcons⟩, hN1⟩, -⟩, -⟩, -⟩, -⟩, -⟩, -⟩ := hc

Exactly four conjuncts are named — `hK` (K ≥ 1), `hrows` (C-A3), `hcons` (C-A4), `hN1` (C-A5) — matching F-6
precisely. The seventeen `-` cover the other six C-A1 conjuncts (including yA² ≥ 1 − 2t₀), C-A2, and all six
C-A6 conjuncts. **F-6 is confirmed, mechanically.**

One refinement, in the safe direction and needing no change: within C-A3 the proof destructures
`⟨⟨-, -⟩, hET⟩` from `checkAsymRow` and uses **only `E < T`** — `Nlo ≤ Nhi` and `0 ≤ E` are discarded too, and
`cover_of_consecutive` is given `hcons` (C-A4), not `hrows`. So the modules' "what the kernel does not use"
paragraph *understates* how little is consumed. That errs toward claiming more is used than is, which is the
harmless direction for an honesty note; recorded, not asked to be changed.

## 5. Observations that need no fix

* **`Zeta23.lean` is not in the mirror.** The working tree's root `Zeta23.lean` gained `import Zeta23.DBN.Asym`
  at 21:29 (phase 3(c)), but `rh-program/lean/` has never carried a root `Zeta23.lean` — it mirrors
  `Zeta23/{DBN,PairCeiling,W1}` and `README.md` only. This is a pre-existing, consistent scope decision, not
  something phase 3(d) introduced. (The emitter's *verbal* summary said "`Zeta23.lean` cmp-identical to the
  mirror"; there is no mirror copy to compare against. `EMIT-NOTES.md` §7 on disk states the mirror scope
  correctly, so nothing on disk needs changing.)
* **The README's gloss adds a clause to SPEC §3.7.** `lean/README.md` line 164 renders H2 as "…from two
  independent producers, **behind the kernel-checked checkers `checkBarrier` and `checkAsym`**"; §3.7's own text
  stops at "from two independent producers". The added clause is true and is this corpus's established idiom
  (the R-1 paragraph at line 149 uses "behind a kernel-checked checker" in the same sense), and it makes the
  claim more precise rather than stronger. Recorded for the record; no change asked.
* **The emitter's "8 hunks" and the auditor's "4 hunks" are the same change**, counted on the raw diff and on
  the comment-stripped diff respectively. The *set* of code changes is identical and is exactly PLAN §1.5's.
* **Kernel time.** The auditor did not re-run the Lean profiler (thermal policy, and it is a performance figure,
  not a trust figure). The forced re-elaboration in check 1 is consistent with the emitter's measurement: each
  literal module rebuilt, `decide +kernel` included, in 1.6 s.

## 6. Files this audit wrote (all under `results/d1-m2a/lane-a/`)

| File | What it is |
|---|---|
| `AUDIT-3d.md` | this report |
| `audit-rebuild.log` | forced re-elaboration of the four modules + `lake build Zeta23`, 7.23 s wall, 9142 jobs, clean |
| `audit-axioms-scratch.lean` | the auditor's own `#print axioms` / `#check` / `#print` probe (16 names) |
| `audit-axioms.log` | its output: the eight names, eight more, the four elaborated statements, both literals as the kernel holds them |
| `audit-backparse.log` | independent re-run of `backparse_lane_a.py`, exit 0, reproduces `backparse.log` |
| `audit-kernel-vs-json.log` | the auditor's disjoint path: kernel-elaborated literals vs the producer JSON, 50 integers, 0 mismatches, plus C-A1/C-A3/C-A4/C-A5/C-A6 re-derived by hand |
| `audit-trust-greps.log` | trust greps run on comment-stripped code over all 121 DBN modules, eleven patterns, zero code hits |

**Nothing is owed from Job 2.** No file in the Lean tree and no file the emitter wrote was edited by the
auditor. On the two fixes above the emitter is re-run; every other check is OK and reproduced.
