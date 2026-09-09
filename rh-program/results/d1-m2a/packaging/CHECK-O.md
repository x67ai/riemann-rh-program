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

