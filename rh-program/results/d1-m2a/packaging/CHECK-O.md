# D1 M2a packaging — CHECK-O (Session 20, queue item 1, Job 2: the independent checker)

**Stamp:** started 2026-09-10 (Session 20), machine clock; checker Claude Opus 5 (1M context). Brief:
`BRIEF.md` §0, §1, §3 (binding). This file is written as the work happens (RULE ONE); the autocommit
watchdog picks it up every ten minutes. Every finding below is re-derived by this job with its own
scripts; Job 1's testimony is read but never taken as evidence.

Scripts and raw logs of this job live under `packaging/check-o/`. The axioms log is
`packaging/CHECK-O-axioms.log`.

## 0. Status ledger (appended as each step lands)

| step | state |
|---|---|
| 1. clean clone + cold build | in progress |
| 2. `#print axioms` (own probe) | pending |
| 3. statement fidelity vs prose | pending |
| 4. independent literal check | pending |
| 5. trust greps (own script) | pending |
| 6. label check + verdict | pending |

## 1. Clean clone (brief §3 step 1) — DONE; provenance exact

**The pristine parent copy the brief names first is gone.** `…/riemann/anthropic/zeta-23-lean-main/`
does not exist (that directory now holds only four PDFs). So the clone was built from the parent's
canonical repository, over the network, as the brief's second option directs.

* **Repository:** `https://github.com/anthropics/zeta-23-lean` (public, cloned 2026-09-10, one
  attempt, no retry needed). Bare clone kept at `~/rh-lean-work/checker-clone-s20-src`
  (37 commits, `origin/HEAD` = `fbdc36bbf17d20af3fd0447c6d1a8a02773c9844`, 2026-09-05).
* **Upstream HEAD is NOT the working tree's version.** Since 2026-08-27 the repository has moved
  `Zeta23` into a `zeta23/` subdirectory (commit `1010de0`, "Move Zeta23 into zeta23/ subdirectory
  (multi-project layout)") and flattened `comparator/` into the project root (`Challenge.lean`,
  `comparator.json`, …). The working tree `~/rh-lean-work/zeta-23-lean-main` has the OLD root
  layout with a `comparator/` directory.
* **The commit the working tree is at, identified by blob search, not by trusting a label:**
  `git hash-object` on the working tree's `README.md`, `AUDIT.md`, `lakefile.toml`,
  `lean-toolchain`, `comparator/README.md` and `comparator/Challenge.lean` gives blobs whose
  common ancestor set narrows to

      3635e74826a4c1fcece7d1cd2b6fa75e43a00510   tag v1.0, 2026-08-10 09:28:04 -0700
      "Merge pull request #3 from anthropics/xiprime-pairceiling"

  (`README.md` blob `f1d8070f…` occurs at v1.0 and at no later commit; `lake-manifest.json`
  blob `af9ef405…` is unchanged from v1.0 to HEAD; the working tree's root `Zeta23.lean` blob
  `7973cf87…` occurs at NO commit — it is the program's edit, see below.)
* **Clean tree:** `git archive 3635e748 | tar -x -C ~/rh-lean-work/checker-clone-s20` — 341 files,
  no `.git`, no build artefacts, nothing taken from the working tree.

### 1.1 `diff -rq` of the pristine v1.0 tree against the working tree — every difference

Excluding `.lake`, `audit-tmp`, `scratch`. **Twelve lines, and every one of them is a program
addition**; there is no modified parent file anywhere except the root `Zeta23.lean`:

    Only in <work>/Zeta23: DBN
    Only in <work>/Zeta23/PairCeiling: GridCorner.lean
    Only in <work>/Zeta23/PairCeiling: GridParseval.lean
    Only in <work>/Zeta23/PairCeiling: GridWitness.lean
    Only in <work>/Zeta23: W1
    Files <clone>/Zeta23.lean and <work>/Zeta23.lean differ
    Only in <work>/comparator/Challenge: DBN.lean
    Only in <work>/comparator/ChallengeDeps: DBN
    Only in <work>/comparator/ChallengeDeps: DBN.lean
    Only in <work>/comparator/PrintAxioms: DBN.lean
    Only in <work>/comparator/Solution: DBN.lean
    Only in <work>/comparator: config-dbn.json

Raw log: `check-o/diff-clone-vs-worktree-raw.txt`. **Confirmed: the program modified no parent
library file, no lakefile, no manifest, no toolchain.** `Zeta23.lean` differs by exactly fifteen
ADDED `import` lines (nothing removed, nothing reordered) — `PairCeiling.Grid{Parseval,Witness,Corner}`,
`DBN.{Defs,BarrierCert,Asym,Instance02}`, `W1.{Format,Checker,Examples,Soundness,ArgPrinciple.Rect,
ArgPrinciple.General,ArgPrincipleBridge,Instances}` — i.e. exactly the brief's anticipated case.

### 1.2 Overlay of the committed mirror, and what the mirror does NOT carry

Mirror: `rh-program/lean/` at commit **`a4a14f6f47b7854693ee51f8556f6708f41c5d68`** (branch `main`;
`git -C rh-program rev-parse HEAD`; the packaging content landed at `9c87ff5`, `d0b54d3`, `f11f308`).
Overlaid with `rsync -a` at the same relative paths (`lean/Zeta23/` → `Zeta23/`,
`lean/comparator/` → `comparator/`).

**Independent set-comparison of the three trees** (`comm` on sorted `find` listings):

* Program `.lean` files under `Zeta23/` (present in the working tree, absent from pristine v1.0):
  **135**. Of these **132 are in the mirror and all 132 are byte-identical** (`cmp`) to the working
  tree. **Zero mirror files are not program files** — the mirror carries no parent library file.
* The six comparator DBN files (`ChallengeDeps/DBN.lean`, `ChallengeDeps/DBN/Instance02.lean`,
  `Challenge/DBN.lean`, `Solution/DBN.lean`, `PrintAxioms/DBN.lean`, `config-dbn.json`) are
  `cmp`-identical mirror ↔ working tree. Job 1's §4 claim checks out.
* **Three program files are NOT in the mirror:** `Zeta23/W1/AuditO.lean`, `AuditOCases.lean`,
  `AuditOFuzz.lean`. Their own header says "Auditor-O scratch module (Session 14 adversarial audit
  of D1 M1 v1). NOT part of the deliverable"; `grep -rl AuditO` over `Zeta23/`, `comparator/` and
  `Zeta23.lean` returns nothing — no module imports them. **Not a defect** (they are `#print axioms`
  probes, not library content), but recorded: the mirror is the deliverable, not a complete copy of
  the program's Lean scratch.
* **The mirror does NOT carry the root `Zeta23.lean`.** It is a parent file that the program edited,
  so a reader who reconstructs the tree from upstream + mirror gets a root that does not import the
  program's modules. Overlaid here from the working tree, as the brief permits, and recorded as
  CHECK-O finding **F-1** (§6).

**Reconstruction check.** After the overlay, `diff -rq` of the reconstructed clone against the
working tree reports exactly three lines — the three `AuditO*` scratch modules — and nothing else.
So the clean tree used for every build and every check below is, byte for byte,
**upstream v1.0 + the committed mirror + fifteen import lines**, with nothing else borrowed.

## 4. Independent literal check (brief §3 step 4) — 145 533 integers, 0 mismatches

Script: `check-o/check_literals.py`, written from scratch for this job. It imports, calls and
re-uses **nothing** from `packaging/emit_challengedeps_instance02.py`, `emit_lean_m2a.py`,
`lane-a/emit_lean_lane_a.py`, `lane-a/backparse_lane_a.py` or `packaging/cmp_literal_blocks.py`.
It strips the Lean comments with its own nesting-aware stripper, splits the file into `def`
blocks, tokenizes each literal into Python integers, and compares them with the JSON.

**This is a different check from Job 1's.** `cmp-literal-blocks.log` compares the trusted copy
against the **Zeta23 copy** (text ↔ text); if both had been emitted from a corrupted source they
would agree. This check goes trusted copy ↔ **JSON source**, so it closes that hole.

Sources: `transcripts/row2/manifest.json` + 39 `prism-NNNN.json`;
`transcripts/row2-arb/instance02-barrier-manifest.json` + 72 `instance02-prism-NNNN.json`;
`lane-a/asym-mp.json`, `lane-a/asym-arb.json`.

    def blocks parsed: 227
    Lane B mp : 39 prisms, 7176 segment rows
    Lane B arb: 72 prisms, 10771 segment rows
    Lane A    : 3 + 3 window rows + 2 tail rows
    integers compared: 145533
    mismatches: 0
    RESULT: IDENTICAL

Full log `check-o/check-literals.log`. What was compared, field by field: `row2Rect`'s eight
integers against both manifests' `rect`; `t0n`/`t0d` against `t0`; the prism list's **names and
order** against the manifest's `prisms` array and each prism's `index`; per prism `tn`/`td` ↔
`seam`, `K`/`A` ↔ `scales`, all four mesh sides ↔ `mesh.{bottom,right,top,left}` as (n, d) pairs,
every `W1Row` ↔ `segments[k].{reLo,reHi,imLo,imHi,argLo,argHi}` (including following the
`rows := <chunk def>` indirection), `Fn`/`Fd` ↔ `modulus_floor`, `E` ↔ `approx_defect`,
`D` ↔ `displacement`; per Lane A leg `K`, `t0n/d`, `y0n/d`, `yAn/d`, the three window rows
(`Nlo`, `Nhi`, `T`, `E`) and the tail row (`N1`, `Q1…Q4`, `E1`) — 25 integers per leg.
17 947 `W1Row`s (7 176 + 10 771) confirm Job 1's count. **Nothing was sampled**; every integer in
the trusted file that has a JSON counterpart was compared.

## 5. Trust greps re-run strictly (brief §3 step 5) — CLEAN

Script: `check-o/trust_greps_o.py`, this job's own (no code shared with `packaging/trust_greps.py`).
Comments and docstrings stripped FIRST, with a nesting-aware stripper that preserves line numbers
(so `/- … /- … -/ … -/`, `/-- … -/`, `/-! … -/` and `--` are all removed before the search);
then whole-word search over the remaining code. 127 files: the six comparator DBN files and all
121 modules under `Zeta23/DBN/`. Twelve patterns — KICKSTART 10(j)'s eight plus `sorryAx`,
`trust_me`, `lean_evalConst`, `#eval`:

    pattern           raw(text)  code-only
    axiom                     2          0
    native_decide           119          0
    unsafe                    0          0
    implemented_by            0          0
    extern                    0          0
    opaque                    0          0
    sorry                    12          7
    ofReduceBool              1          0
    sorryAx                   1          0
    trust_me                  0          0
    lean_evalConst            0          0
    #eval                     0          0

The seven code-only `sorry` hits are exactly the challenge placeholders,
`comparator/Challenge/DBN.lean` lines 84, 103, 116, 121, 125, 130, 134 — one per statement.
**Other code hits: 0. RESULT: CLEAN.** Log `check-o/trust-greps-o.log`. (My raw `sorry` count is
12 where Job 1's log says 11; the difference is a prose occurrence counted per-occurrence rather
than per-line. Code-only agrees exactly: 7, same seven lines.)

## 6. Label check and import discipline (brief §3 step 6) — CLEAN

Script `check-o/label_check_o.py`, log `check-o/label-check-o.log`. The search normalizes
whitespace first, so a label wrapped across a line still counts (`ChallengeDeps/DBN.lean` wraps it
mid-sentence; a naive exact-substring test reports a false absence there — noted so a later reader
does not repeat the mistake).

| file | exact §3.7 short label | "fully machine-checked" |
|---|---|---|
| `comparator/ChallengeDeps/DBN.lean` | 1 | 1 (prohibition) |
| `comparator/ChallengeDeps/DBN/Instance02.lean` | 1 | 1 (prohibition) |
| `comparator/Challenge/DBN.lean` | 4 | 3 (prohibitions) |
| `comparator/Solution/DBN.lean` | 4 | 4 (prohibitions) |
| `comparator/PrintAxioms/DBN.lean` | 1 | 1 (prohibition) |
| `comparator/config-dbn.json` | 0 — no label text at all | 0 |
| `lean/README.md` | 3 | 5 (prohibitions) |
| `lean/formalization.yaml` | 3 | 3 (prohibitions) |
| `packaging/FIDELITY.md` | 2 | 1 (prohibition) |

**The exact sentence "kernel-checked modulo H1, H2 (H2-B, H2-A, H-TAIL), H3" is present in every
file where a label appears.** `config-dbn.json` is a machine config (challenge module, solution
module, theorem names, permitted axioms, `enable_nanoda`) with no prose at all — the parent's own
`config.json` and `config-xiprime.json` are the same — so the requirement is vacuous there, not
violated. **All 19 occurrences of "fully machine-checked" are prohibitions** ("— never …",
"forbid …"), each classified by reading the 60 characters before the phrase; **zero uses as a
label**. `ChallengeDeps/DBN.lean` also carries SPEC §3.7's long form verbatim.

**Import discipline** (comments stripped before reading the `import` lines — the header prose of
`ChallengeDeps/DBN.lean` contains the word "import" mid-sentence and trips a naive grep):

* `comparator/Challenge/DBN.lean` → `ChallengeDeps.DBN`, `ChallengeDeps.DBN.Instance02`. **No
  `import Zeta23…`, anywhere in the file, in code or in a comment line position.**
* `comparator/ChallengeDeps/DBN.lean` → `Mathlib` only. No `Zeta23`.
* `comparator/ChallengeDeps/DBN/Instance02.lean` → `ChallengeDeps.DBN` only. No `Zeta23`.
* `comparator/Solution/DBN.lean` → `ChallengeDeps.DBN`, `ChallengeDeps.DBN.Instance02`,
  `Zeta23.DBN.Instance02`. **It never imports `Challenge.DBN`** — required, since importing the
  challenge would let the solution inherit the `sorry`s.

RESULT: **CLEAN**.

