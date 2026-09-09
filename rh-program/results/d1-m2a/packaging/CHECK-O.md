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
| 1. clean clone + cold build | DONE — provenance exact (upstream v1.0), builds clean |
| 2. `#print axioms` (own probe) | DONE — 131 names, no unpermitted axiom |
| 3. statement fidelity vs prose | DONE — one item missing from the ledger (FIX-FIRST 2) |
| 4. independent literal check | DONE — 145 533 integers, 0 mismatches |
| 5. trust greps (own script) | DONE — CLEAN |
| 6. label check + verdict | DONE — label CLEAN; **verdict FIX-FIRST**, §8 |

**VERDICT: FIX-FIRST — two items, §8. Neither is a soundness defect and neither needs a rebuild:**
(1) `lean/README.md`'s reproduction recipe is broken and the mirror lacks the root `Zeta23.lean`;
(2) the fidelity ledger lacks the item "nothing in Lean ties the trusted literals to the
transcripts of record". Everything substantive — provenance, builds, axioms, statements, literals,
greps, label — is CLEAN and re-derived independently.

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

### 1.3 Mathlib cache and the cold builds — clean, no errors, no program-module warnings

`lake exe cache get` **succeeded** in the clean tree (11.5 s: "Decompressing 8489 already-cached
file(s)… No files to download… Completed successfully"), so **nothing was copied from the working
tree's `.lake/packages`** — the brief's fallback was not needed. (The `.olean` cache comes from
Mathlib's own machine-global store, not from `~/rh-lean-work/zeta-23-lean-main`.)

| build (cold, in `~/rh-lean-work/checker-clone-s20`) | jobs | wall | user | exit | errors |
|---|---|---|---|---|---|
| `lake build Zeta23` | **9142** | **397.04 s** (6 min 37 s) | 2512.60 s | 0 | **0** |
| `lake build Solution.DBN` | 8826 | 54.31 s | 71.17 s | 0 | **0** |
| `lake build Challenge.DBN` | 8699 | 4.97 s | 3.68 s | 0 | **0** |

9142 jobs matches AUDIT-3d check 1 exactly. Logs: `check-o/build-zeta23.log`,
`build-solution-dbn.log`, `build-challenge-dbn.log`.

* `lake build Zeta23`: **191 warnings, all in parent-library modules** (`XiPrime/`, `FromPNTPlus/`,
  `ZeroSide/`, `WeilEF/`, `Taper/`, `ThmD/`, `ThmE/`, `RvM/`, `Assembly/`, `PairCeiling/Stability.lean`
  — every one of them a file present in pristine v1.0). **Zero warnings from any file the program
  added**: no `Zeta23/DBN/*`, no `Zeta23/W1/*`, no `Zeta23/PairCeiling/Grid*`, nothing under
  `comparator/`.
* `lake build Solution.DBN` — `Built ChallengeDeps.DBN (3.1s)`, `Built ChallengeDeps.DBN.Instance02
  (36s)`, `Built Solution.DBN (12s)`. No warnings at all. The 20 157-line trusted literal module
  elaborates in 36 s from cold in this tree (Job 1 measured 38 s; the brief's 30-minute fallback is
  nowhere near).
* `lake build Challenge.DBN` — **exactly 7 `declaration uses 'sorry'` warnings**, at lines 71, 96,
  109, 120, 124, 129, 133 (the seven `theorem` lines; the trust grep sees the `sorry` tokens seven
  lines further down at 84, 103, 116, 121, 125, 130, 134). No other warning, no error.

One `lake` process at a time throughout; `ps -Ao pcpu,comm | awk '$1>50'` checked before each build
and before the probe: 0 heavy processes every time. `caffeinate` running.

## 2. `#print axioms` — Job 2's own probe (brief §3 step 2) — CLEAN, 131 names

Probe generator `check-o/gen_axioms_probe.py`, probe file `check-o/check-o-axioms-probe.lean`.
It parses the sources itself (comment-stripped, namespace-tracked) and emits one `#print axioms`
per top-level `theorem`/`lemma`. **It does not read or reuse `comparator/PrintAxioms/DBN.lean` or
`packaging/print-axioms-bridge.lean`.** Run: `lake env lean check-o-axioms-probe.lean`, 3.64 s.
Full log: `packaging/CHECK-O-axioms.log` (164 lines).

Coverage — **131 names**, wider than Job 1's seven:

| source | theorems probed |
|---|---|
| `Zeta23/DBN/Asym.lean` | 4 |
| `Zeta23/DBN/BarrierCert.lean` | 28 |
| `Zeta23/DBN/BtFacts.lean` | 15 |
| `Zeta23/DBN/Defs.lean` | 0 (definitions only) |
| `Zeta23/DBN/Instance02.lean` | 17 |
| `comparator/Solution/DBN.lean` | 60 (the 7 root statements + 53 `DBNBridge` helpers) |
| `comparator/Challenge/DBN.lean` names, as proved in `Solution.DBN` | 7 |

**Result, every one of the 131:**

    90 × depends on axioms: [propext, Classical.choice, Quot.sound]
     6 × depends on axioms: [propext, Quot.sound]
    27 × depends on axioms: [propext]
     8 × does not depend on any axioms

**No `sorryAx`. No `Lean.ofReduceBool`. No `Lean.trustCompiler`. No axiom outside the permitted
three, anywhere.** `grep` for those three tokens over the whole log returns nothing.

The seven challenge names reproduce Job 1's `print-axioms.log` **exactly**:

    'dbn_ray_le_point2_of_certificates' … [propext, Classical.choice, Quot.sound]
    'dbn_ray_le_point2_mp'              … [propext, Classical.choice, Quot.sound]
    'dbn_ray_le_point2_arb'             … [propext, Classical.choice, Quot.sound]
    'dbn_row2BarrierMP_checked'         … [propext, Quot.sound]
    'dbn_row2BarrierARB_checked'        … [propext, Quot.sound]
    'dbn_row2AsymMP_checked'            … [propext]
    'dbn_row2AsymARB_checked'           … [propext]

`config-dbn.json`'s `permitted_axioms` are `propext`, `Quot.sound`, `Classical.choice` — the three
that occur, and no more.

**The elaborated types** (`#check @`, the same log, lines 132–164) confirm the shape independently
of the source text: `dbn_ray_le_point2_mp` and `_arb` take **exactly five hypotheses in the brief
§0 order** — `ZeroVerification (116733/200000) 2500000097429` → `BarrierEnclOK (fun t z => Ht t z /
Bt t z) row2Barrier*` → `AsymEnclOK (fun z => Ht (93/500) z / Bt (93/500) z) row2Asym*` → `TailOK
(…) row2Asym*` → `Polymath15Bridge' ∧ HtEntire` — and conclude `∀ t : ℝ, 1/5 ≤ t → ∀ z : ℂ,
Ht t z = 0 → z.im = 0`. Nothing else. **MP literals appear only in the mp theorem and ARB only in
the Arb theorem** — the legs are not merged (D-R3). The (K) statements are exactly
`checkBarrier row2Barrier* = true` / `checkAsym row2Asym* = true`.

**Statement identity, re-derived** (`check-o/stmt_identity_o.py`, log `check-o/stmt-identity-o.log`;
no code shared with `packaging/statement_identity.py`): 7 challenge statements, 7 solution root
statements, **all 7 IDENTICAL** after comment-stripping and whitespace normalization (758 / 399 /
403 / 69 / 71 / 60 / 62 characters — my normalization keeps the binder names, hence the different
character counts from Job 1's log); `config-dbn.json`'s `theorem_names` equal the challenge's names
in order; **no solution root theorem outside the challenge's seven** (the 53 helpers are all inside
`namespace DBNBridge`).

## 3. Statement fidelity (brief §3 step 3) — re-derived, not weighed

Read: `comparator/Challenge/DBN.lean` in full, against SPEC §1.1 (the target theorem), SPEC §3.7
(the label and its gloss), SPEC §1.2 (P15 Theorem 1.2 quoted), SPEC §3.2–§3.6, PLAN-REVIEW §6
(what the Session-19 replacement bought), EMIT-NOTES §4, AUDIT-3d §1 checks 3/14/15, and
`Zeta23/DBN/Instance02.lean`'s header and docstrings.

### 3.1 The (I) statements ARE the referee's statements

`Zeta23.DBN.Instance02.lambda_le_point2` (lines 242–248) and `_arb` (255–261) take, in order,
`hH1`, `hEncl`, `hAsym`, `hTail`, `hH3` and conclude `∀ t : ℝ, (1/5 : ℝ) ≤ t → ∀ z : ℂ,
Ht t z = 0 → z.im = 0`. `dbn_ray_le_point2_mp` / `_arb` are **character-identical** to those five
binders and that conclusion, with `row2Barrier*`/`row2Asym*` resolving to the trusted copies. The
elaborated types (§2) confirm it independently of the source text. SPEC §1.1's target theorem is
`∀ t : ℝ, 1/5 ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0` — the same. **No divergence.**

### 3.2 The trusted vocabulary IS the Zeta23 vocabulary, verified two ways

* **Text** (`check-o/vocab_copy_o.py`, my own extractor; log `check-o/vocab-copy-o.log`): all **79**
  declarations of `ChallengeDeps/DBN.lean` are found in `Zeta23/DBN/{Defs,BarrierCert,Asym}.lean`
  and `Zeta23/W1/{Format,Checker,Soundness}.lean` **and every one is character-for-character
  identical, docstring included. 79 identical, 0 different, 0 missing.** (My first pass reported
  26 "different" — my own extractor was mis-attaching docstrings across back-to-back one-line
  declarations, the same class of bug Job 1 records fixing in its generator. Fixed, then 79/79.)
* **Proof** — and this is the part that matters, because a verbatim text copy elaborated under
  `import Mathlib` rather than Zeta23's granular imports could in principle mean something else:
  `Solution/DBN.lean` §1 proves `DBN.X = Zeta23.DBN.X := rfl` for all ten copied `def`s
  (`Phi`, `Ht`, `ZeroVerification`, `alpha`, `M0`, `Mt`, `Bt`, `HtEntire`, `Polymath15Bridge'`,
  `windowIdx`), and §3 proves `checkBarrier_eq`, `checkAsym_eq`, `PrismEnclOK_iff`,
  `BarrierEnclOK_iff`, `AsymEnclOK_iff`, `TailOK_iff` — all **`↔`/`=`, both directions**, so the
  trusted Props are neither stronger nor weaker than Zeta23's. §4 decides
  `toZBarrier DBN.row2BarrierMP = Zeta23.…row2BarrierMP` (and the three siblings) by
  **`decide +kernel`** — i.e. the Lean kernel itself compared all 17 947 rows and every mesh
  coordinate — and `#print axioms` on those four identities is **empty**. That is a stronger
  statement of "byte-identical" than any `cmp`.
* Code of the three trusted files contains **zero** references to `Zeta23` (comments stripped), no
  `deriving`, no `macro`/`syntax`/`elab`/`attribute`, and one `set_option maxRecDepth 100000`
  (an elaboration budget in the data module; it cannot make the kernel accept anything).

### 3.3 Every numeric claim in the challenge's docstrings — recomputed, all correct

`check-o/arith-check-o.log`:

| claim (Challenge/DBN.lean, Instance02.lean, FIDELITY (a)/(h)) | recomputed | verdict |
|---|---|---|
| yA = 3962323/5000000 = 0.7924646 | exact | ✓ |
| √(157/250) = 0.79246451… | 0.792464510246357972… | ✓ |
| yA − √(157/250) = 8.975·10⁻⁸ | 8.97536420274901·10⁻⁸ | ✓ |
| yA² − 157/250 = 3556329/(25·10¹²) = 1.42·10⁻⁷ | 1.4225316·10⁻⁷, and the fraction is exact | ✓ |
| (1 + y₀)/2 = 116733/200000 (H1's σ₀) | exact | ✓ |
| X/2 = 2 500 000 097 429 (H1's T₀) | exact | ✓ |
| t₀ + y₀²/2 ≤ 1/5 (L-G) | 0.19999966445 ≤ 0.2 | ✓ |
| mp leg: 39 prisms, 7 176 rows | 39 / 7 176 from the JSON | ✓ |
| Arb leg: 72 prisms, 10 771 rows | 72 / 10 771 from the JSON | ✓ |
| N ∈ [630783, 5140999], N₁ = 5 141 000, last Nhi + 1 = N₁ | from the JSON | ✓ |

The AUDIT-3d A-1 correction (the "1.5·10⁻⁷" figure was the gap in the SQUARES) is carried
correctly everywhere in the packaged files: they say 9.0·10⁻⁸ in y and 1.42·10⁻⁷ in the squares.

### 3.4 Divergences I found, checked against Job 1's `fidelity.divergences` (a)–(j)

Job 1's ledger (`FIDELITY.md`, mirrored verbatim in `formalization.yaml` `fidelity.divergences`,
4 455 characters) is accurate on every point I could test, and covers: (a) the y-band asymmetry
with the corrected figures; (b) C-A6 kernel-checked but not consumed and H-TAIL displayed in
conclusion form; (c) untrusted producers, five displayed hypotheses, the exact label; (d) ray form
vs Λ; (e) `Polymath15Bridge'` vs P15 Theorem 1.2 ((ii′), the y² form, the p3 box, `HtEntire`);
(f) (G) vs Zeta23's instance-only proof, the re-declared types and their transports, the (K)
addition; (g) no reductions, and what is deliberately off the trusted side; (h) H1's exact shape
and prose discharge; (i) two legs, two theorems, no agreement statement; (j) what is proved rather
than displayed, `Bt`'s principal-branch transcription, `Ht`'s Bochner junk value.

**One divergence I judge genuine and NOT recorded there — FIX-FIRST item 2 (§7):**

* **Nothing in Lean ties the trusted literals to the transcripts of record.** The (I) and (K)
  statements are about `ChallengeDeps.DBN.Instance02.row2BarrierMP` etc.; that those 20 157 lines
  are the contents of `results/d1-m2a/transcripts/row2*/…json` and `lane-a/asym-{mp,arb}.json` is
  established **only by untrusted scripts** — Job 1's emitter and `cmp_literal_blocks.py`, and this
  job's `check_literals.py`. The kernel's `decide +kernel` identities tie the trusted copy to the
  **Zeta23** copy, not to the JSON; if both copies were emitted from the same corrupted source they
  would agree and the kernel would not notice. The consequence is benign — the literals appear only
  inside displayed hypotheses, so a wrong literal makes the hypotheses be about different numbers
  rather than making a false theorem true — but a referee writing "with the numerical hypotheses
  verified" should be told where the formal chain stops. Ledger items (c) and (g) come close and do
  not say it.

**Wording, not a divergence:** the challenge header calls (G) "the GENERIC soundness statement,
literal-free". It is free of the *transcript* literals, but the statement still pins seven instance
constants (X = 5 000 000 194 858, X + 1, y₀ = 16733/100000, y₂ = 1, t₀ = 93/500,
yA = 3962323/5000000, N_start = 630783) and H1's two rationals — as the same docstring then says in
full, and as ledger item (f) records. The phrase is the brief's own; I flag it only so a reader does
not take "generic" for "for all rectangles and times". No fix demanded.

## 7. Observations that need no fix (recorded so a later reader does not re-derive them)

1. **Hashes.** All seven SHA-256 values in BUILD-NOTES §5 for the packaged files reproduce exactly
   against the mirror (`b55cb89b…`, `1eb81bf8…`, `2c928d4b…`, `dcc18e39…`, `cca0c760…`,
   `aa0b9fcd…`, `eb798527…`), as do the line counts (562 / 20 157 / 136 / 422 / 28 / 386).
   Tree = mirror on all six comparator files (`cmp`).
2. **The mirror does not carry `Zeta23/W1/AuditO.lean`, `AuditOCases.lean`, `AuditOFuzz.lean`.**
   Their own header says "Auditor-O scratch module … NOT part of the deliverable", and nothing in
   the tree imports them (`grep -rl AuditO` over `Zeta23/`, `comparator/` and `Zeta23.lean`:
   nothing). Correct to omit; recorded so the 135-vs-132 file count is not read as a discrepancy.
3. **`Challenge/DBN.lean` does not `import ChallengeDeps`** (the parent's base trusted module),
   where `comparator/README.md`'s layout table writes `import ChallengeDeps` (+ the topic's own).
   It needs nothing from the base module, so the deviation **shrinks** the trusted reading surface.
   Not a defect; worth one line in BUILD-NOTES if the topic is ever submitted upstream.
4. **The trusted reading surface of this topic is 20 855 lines** (562 + 20 157 + 136), where the
   parent's README promises its readers "≈60 lines of mathematics — read it". 20 157 of those lines
   are producer integers that no human will read. This does not break the trust story — the numbers
   enter only through displayed hypotheses (ledger (c)) — but "trusted: read it" means something
   different here than in the parent's topics, and the README's topic table would be more honest if
   it said so. Recommendation, not a FIX-FIRST item.
5. **`formalization.yaml` re-validated.** Parses under Ruby's Psych; twelve top-level keys, all in
   v0.4 (`version`, `project`, `repository`, `sources`, `related_formalizations`, `classification`,
   `status`, `automation`, `fidelity`, `review`, `alignment`, `acknowledgements`); 11
   `main_results`; `fidelity.divergences` 4 455 characters; `review.status: self-assessed` with
   `reviewers: []` and the honest note that no human has read the challenge against the prose. Job
   1's BUILD-NOTES §7 item 4 owes a `jsonschema` reference validation; a network-allowed job should
   run it. I did not install packages.
6. **Job 1's recorded job count 8827 for `lake build Challenge.DBN Solution.DBN`** reconciles with
   my 8826 (`Solution.DBN` alone) + `Challenge.DBN`'s own job. No discrepancy.
7. **This job left one file in the clean tree**, `~/rh-lean-work/checker-clone-s20/check-o-axioms-probe.lean`
   (its own probe). Nothing under `~/rh-lean-work/zeta-23-lean-main` or `rh-program/lean/` was
   touched by this job at any point.

## 8. VERDICT — **FIX-FIRST** (two items; neither is a soundness defect, neither needs a rebuild)

**Everything substantive is CLEAN and re-derived, not weighed:**

* clone provenance exact — upstream `anthropics/zeta-23-lean` at tag **v1.0**
  (`3635e74826a4c1fcece7d1cd2b6fa75e43a00510`), and the working tree differs from it **only** by
  program additions plus fifteen added `import` lines in the root `Zeta23.lean`;
* cold builds clean — `lake build Zeta23` 9142 jobs / 397 s / 0 errors / **0 warnings from any
  program module**; `Solution.DBN` 8826 jobs / 54 s; `Challenge.DBN` 8699 jobs with **exactly 7**
  deliberate `sorry` warnings;
* `#print axioms` over **131** names (Job 1 probed 7): 90 × the three standard axioms, 6 ×
  `[propext, Quot.sound]`, 27 × `[propext]`, 8 × none. **No `sorryAx`, no `Lean.ofReduceBool`,
  no unpermitted axiom anywhere.** The seven challenge names reproduce Job 1's log exactly;
* the (I) statements are the referee's statements verbatim, the elaborated types show exactly the
  five displayed hypotheses in order, MP with MP and ARB with ARB;
* the trusted vocabulary is 79/79 character-for-character Zeta23, **and proved equivalent** by
  `rfl`/`↔` bridges plus four kernel-decided literal identities;
* **145 533 integers** compared trusted-copy ↔ JSON by this job's own parser, **0 mismatches**;
* trust greps, this job's own script, twelve patterns, comments stripped first: **code-only 0 for
  every pattern except the seven challenge `sorry`s**;
* the label check passes: the exact §3.7 sentence present in every file that carries a label, all
  19 occurrences of "fully machine-checked" are prohibitions, no `import Zeta23` on the trusted
  side, and `Solution/DBN.lean` never imports the challenge module;
* every numeric claim in the docstrings recomputes correctly, including the corrected A-1 figures.

**FIX-FIRST 1 — the deliverable does not reproduce from its own recipe (reproducibility, not
soundness).** `lean/README.md` § "Building" says:

    git clone https://github.com/anthropics/zeta-23-lean
    cd zeta-23-lean
    cp -R /path/to/this/repo/rh-program/lean/Zeta23/. Zeta23/
    lake exe cache get && lake build

I ran it. It is broken three ways: (i) upstream HEAD (`fbdc36b`, 2026-09-05) moved the library into
a `zeta23/` subdirectory on 2026-08-27, so the repository root has no `Zeta23/`, no `comparator/`,
no `lakefile.toml` and no `lean-toolchain` — the `cp` creates a stray root directory and `lake`
fails with "no default toolchain configured"; (ii) the recipe never copies `comparator/`, so the
whole new topic is absent; (iii) `rh-program/lean/` **does not contain the root `Zeta23.lean`**,
which the program edited (fifteen added imports), so even at the right commit `lake build Zeta23`
would build the parent only. The stale "*Build completed successfully (2081 jobs)*" should also go
(my cold build of the full tree: 9142 jobs).

*Exact fix.* (a) Add `rh-program/lean/Zeta23.lean` — the v1.0 root plus the fifteen program imports
(copy `~/rh-lean-work/zeta-23-lean-main/Zeta23.lean` verbatim). (b) Replace the recipe with

    git clone https://github.com/anthropics/zeta-23-lean
    cd zeta-23-lean
    git checkout v1.0        # 3635e74826a4c1fcece7d1cd2b6fa75e43a00510 — the base these files overlay;
                             # main has since moved the library into a zeta23/ subdirectory
    cp -R /path/to/this/repo/rh-program/lean/Zeta23/. Zeta23/
    cp -R /path/to/this/repo/rh-program/lean/comparator/. comparator/
    cp    /path/to/this/repo/rh-program/lean/Zeta23.lean Zeta23.lean
    lake exe cache get && lake build Zeta23 && lake build Solution.DBN

and record the measured figures: `lake build Zeta23` 9142 jobs, 397 s cold on the checker's
machine; `lake build Solution.DBN` 8826 jobs, 54 s. (c) Say in the same section that the base
commit is v1.0 and that `Zeta23/W1/AuditO*.lean` are deliberately not mirrored.

**FIX-FIRST 2 — one missing fidelity item.** Add to `FIDELITY.md` and to `formalization.yaml`
`fidelity.divergences` an item (k), in substance:

> (k) **Nothing in Lean ties the trusted literals to the transcripts of record.** The (I) and (K)
> statements are about `ChallengeDeps.DBN.Instance02.row2Barrier{MP,ARB}` / `row2Asym{MP,ARB}`;
> that those 20 157 lines are the contents of `results/d1-m2a/transcripts/row2/*.json`,
> `transcripts/row2-arb/*.json` and `lane-a/asym-{mp,arb}.json` is established only by untrusted
> scripts (`packaging/emit_challengedeps_instance02.py` and `cmp_literal_blocks.py`; independently
> re-derived by `packaging/check-o/check_literals.py`, 145 533 integers, 0 mismatches). The
> kernel's `decide +kernel` identities tie the trusted copy to the Zeta23 copy, not to the JSON.
> The consequence is benign — the literals occur only inside displayed hypotheses — but the formal
> chain stops at the Lean literals, and a referee should be told so.

**Neither item requires re-elaborating any Lean.** No `.lean` file needs to change; the fixes are a
new mirrored `Zeta23.lean`, an edited README section, and one paragraph in two files. Once they
land, this verdict becomes CLEAN. Nothing here blocks Job 3 (the Comparator run) — it can start now.

## 9. Files this job wrote, with SHA-256 (KICKSTART 10(i))

Nothing outside these paths was written; `~/rh-lean-work/zeta-23-lean-main` and `rh-program/lean/`
were read only.

    4086aa6b3cde1a80ead88769d37db621c707e29a65b0c6dc66bfa5bf5bc089c3  CHECK-O-axioms.log
    e0b2c291be88806ab53a9324dedf7e7d7ee3ca51edb1d219b45cfdf4d6d8a25f  check-o/check_literals.py
    96697df800f0ac539772064ae56537cd9659cef72955558de32706cbec0670de  check-o/gen_axioms_probe.py
    1249ef2c927f82dff158d77e93814b3ab19b743108cd4b15662867b806ef8509  check-o/label_check_o.py
    4eb9392b12c37bebc44137e02a08ee34d21494f542e8e52a6a6bc8179ba3b447  check-o/stmt_identity_o.py
    962faebaff5d2da0a5eb2d8218b690e89ed28e94669b77bbcb0fd518e0afc7aa  check-o/trust_greps_o.py
    7376976a272dc3aeb1b7c4bffc5e2f66f06302dba44a13568689e41c326d7485  check-o/vocab_copy_o.py
    013fe260bfb72a4df4de766f8ca1f384acfdc90d47c982a4703d78d9294bdf65  check-o/arith-check-o.log
    8a9cf83f6b1cc4b681e41f26f357d79851377c9ba92b42a7c7116a0cfb411490  check-o/axioms-probe-time.log
    6934bff5a7a5f349194bb783f056e32de8c98094c2f3e3db22661d1656d79bce  check-o/build-challenge-dbn.log
    42d069d3b88bc26590868443af33537bda771245eacf9aa821cb1b9fc5b58f45  check-o/build-solution-dbn.log
    282fd58e5f158da93b5521f316549479172d1e9b000ec6e937793a90f5c161d9  check-o/build-zeta23.log
    1ad2f91ff900f997b057345c24deebbb068434ad9bc882f71f87f4ba774e20ad  check-o/check-literals.log
    ccb505ea9d4ef47196285446e82488f0c7441b33bf6797a394fd4c39e1d467f4  check-o/label-check-o.log
    ae89b19072902d13b2a3f1821e4d0cd9b627a02c127672b3f1484e7915d7c056  check-o/stmt-identity-o.log
    5e92780e51ce39ac3984ac489daa59ccabd6304b4e2657c62c140652eab972d0  check-o/trust-greps-o.log
    c8e1f8ce2798156ac261d1c7327921b79962d88aa2aeefa73478856a9e4fd80b  check-o/vocab-copy-o.log
    581844a29d6d3160fdc40a98ae2ecd6f13ed69fc98d65c69a1fbe86eb04a3347  check-o/check-o-axioms-probe.lean
    aec28c11994fa568e14119219be2c037289dd4be526aee47a1905e0cd4593c22  check-o/diff-clone-vs-worktree-raw.txt

Working trees used: `~/rh-lean-work/checker-clone-s20-src` (the bare-ish clone of
`anthropics/zeta-23-lean`, 37 commits, `origin/HEAD` `fbdc36bb…`) and
`~/rh-lean-work/checker-clone-s20` (the clean tree: `git archive` of tag v1.0 `3635e748…`, plus the
`rh-program` mirror at commit `a4a14f6f47b7854693ee51f8556f6708f41c5d68`, plus the root
`Zeta23.lean`). Both may be deleted once Job 3 has run; the clean tree is the one a Comparator run
should use if a pristine base is wanted.
