# Linux replay s33 — harvest note (14:06 IST 2026-09-29, Session 34, orchestrator)

**Delivered:** `~/Downloads/rh-linux-check-s33-logs.zip` (SHA-256 8f0986ab9ba62581…, 21 187 bytes, 26 files), the sponsor's run of `scripts/linux-comparator-check-s33.sh` on the Linux host (Ubuntu, kernel 7.0.0-34-generic, x86_64, 12 cores, 37 GB; Lean 4.33.0-rc2 (d8b18978), Mathlib 51e6992e); run 13:47:04 → 13:53:51 IST 2026-09-29, one pass, no script failure (the s30 brace-group bug is fixed in this script). Files copied verbatim into this folder; `hashes.txt` lists SHA-256 of the zip and every file.

## Result: every stage as expected — 5/5 PASS, print-axioms identical to the Mac

| Topic | print-axioms (Linux) | Mac record | Name sets | Comparator |
|---|---|---|---|---|
| `WeilContainmentC2One` (H5 rung 1, L = log 3) | 1 name on propext/Classical.choice/Quot.sound; sorryAx 0 | `results/h5-c2-lean-s32/rung1-print-axioms.log`: 1 | IDENTICAL | PASS, exit 0, nanoda 1, fake-landrun warnings 0 |
| `WeilContainmentC2` (H5) | 1; sorryAx 0 | `h5-c2-lean-s32/print-axioms.log`: 1 | IDENTICAL | PASS |
| `EpsteinWitnessSix` (I.1 rung 1) | 3; sorryAx 0 | `i1-witness-lean-s32/rung1-print-axioms.log`: 3 | IDENTICAL | PASS |
| `I1Witness` (I.1) | 14; sorryAx 0 | `i1-witness-lean-s32/print-axioms.log`: 14 | IDENTICAL | PASS |
| `PairChannel` (H4) | 8; sorryAx 0 | `h4-pair-lean-s33/print-axioms.log`: 8 | IDENTICAL | PASS |

Identity was checked by script (name, axiom-list) pairs extracted from each `04-print-axioms-*.log` against the Mac logs named above: five sets equal, every name on exactly `[propext, Classical.choice, Quot.sound]`. Builds: Zeta23 "Build completed successfully (9153 jobs)"; the five solution builds 8698–8703 jobs, 0 errors, 0 warnings (the two "error" grep hits in `02-build-zeta23.log` are the module name `ExplicitFormula.EntryError` and an unused-variable warning, not errors); lean4export, comparator, nanoda, landrun built.

## Sandbox — the same fact as Session 30, re-derived at the log
`09-landrun-test.log`: the strict probe FAILS with "missing kernel Landlock support. Got Landlock ABI v8, wanted Landlock V9" — the pinned landrun asks for ABI v9, the kernel offers v8; a tool-version fact, not a sandbox absence (s32 §E (h) precedent). `09b-landrun-best-effort-test.log`: under the comparator's own flags (`--best-effort`) the sandbox is REAL — a child's write outside the allowed paths is denied ("Permission denied"). Every comparator config therefore ran under a real Landlock sandbox at ABI v8, best-effort mode, as in Session 30. Tool binary hashes (`10-tool-hashes.txt`) differ from the Mac's, as the README says to expect (different OS/CPU); source revisions identical.

## What this changes on the record
Nothing mathematical. The five topics shipped since the s30 replay now carry a second-OS, sandboxed replay: label text unchanged for each ("replayed on Linux under a real Landlock sandbox" is a pointer, not a label change). Record actions: ↳ pointer rows beneath the A4 (H4), D1 (H5) and C3 (I.1) unit rows; zoo LINUX-REPLAY sub-bullets STAGED in `ZOO-LINES-STAGED.md` for the next zoo stream, together with the Lamzouri riders staged at `results/watch-poll-s34/ZOO-LINES-STAGED.md`. Sponsor action item 4(b) of the SESSION 34 QUEUE: CLOSED.
