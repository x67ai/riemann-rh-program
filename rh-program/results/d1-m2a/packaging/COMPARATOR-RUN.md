# D1 M2a packaging — COMPARATOR-RUN (Session 20, queue item 1, Job 3: the Comparator run with nanoda)

**Written 2026-09-10 (Session 20, Job 3, Fable 5.1), appended as the runs land.** Standing order 9: REQUIRED, no shortcuts.
Label (SPEC §3.7, binding, verbatim): the packaged theorem is "kernel-checked modulo H1, H2 (H2-B, H2-A, H-TAIL), H3" —
never "fully machine-checked". Λ ≤ 0.2 is NOT proved; the bracket of record stays 0 ≤ Λ ≤ 0.2 on the literature. A passing
comparator run adds exactly this: an independent tool (Lean FRO's `comparator`) rebuilt the trusted `Challenge.DBN` and the untrusted
`Solution.DBN`, exported both through `lean4export`, verified that the seven solution theorems prove the challenge statements with every
mentioned constant coinciding, that only `propext`, `Quot.sound`, `Classical.choice` are used, and replayed the solution through the Lean
kernel AND the independent `nanoda` kernel. It says nothing about the truth of the five displayed hypotheses.

## 0. What was run, where, by what

* Lean tree (repository root for every run): `~/rh-lean-work/zeta-23-lean-main`, `lean-toolchain` = `leanprover/lean4:v4.33.0-rc2`
  (Lean 4.33.0-rc2, arm64-apple-darwin, commit d8b18978), Mathlib 51e6992e; machine: 10-core Apple Silicon, 24 GiB RAM, 261 GB free.
* Configs (the parent's, unchanged; nothing under `comparator/` or `Zeta23/` was edited by this job):
  `comparator/config.json` (CONTROL — the parent's fifteen theorems, `Challenge`/`Solution`), `comparator/config-dbn.json`
  (the DBN topic — seven theorems, `Challenge.DBN`/`Solution.DBN`), both with `enable_nanoda: true`.
* Command (comparator README, "Full comparator run"; from the repository root, NOT pre-building Challenge/Solution):
  `lake env ~/rh-lean-work/tools/comparator/.lake/build/bin/comparator comparator/config[-dbn].json`
  through `results/d1-m2a/packaging/comparator-run/run.sh` (records env, versions, `/usr/bin/time -l`), env
  `COMPARATOR_LANDRUN=~/rh-lean-work/tools/comparator/scripts/fake-landrun.sh`, `COMPARATOR_LEAN4EXPORT=…/lean4export`,
  `COMPARATOR_NANODA=…/nanoda_bin` (all three read by `Main.lean` of comparator v4.33.0, `M.run`).
* Pre-run cleanup (comparator README assumption 2 — do not pre-build `Solution`): Job 1 had built `ChallengeDeps.DBN`,
  `ChallengeDeps.DBN.Instance02`, `Challenge.DBN`, `Solution.DBN` in this tree. Their build artifacts
  (`.lake/build/lib/lean/{Challenge,ChallengeDeps,Solution}/` and `.lake/build/ir/{…}/`, 40 files listed in
  `comparator-run/prerun-cleanup.log`) were removed before the first run so that comparator builds every comparator-layer module itself.
  The parent's top-level `Challenge.olean`/`Solution.olean`/`ChallengeDeps.olean` had never been built in this tree. Nothing under
  `Zeta23/` (the library the solution delegates to) was rebuilt — it is the untrusted side either way.

## 1. Tooling — verified by this job (versions, commits, SHA-256)

Built by the orchestrator 2026-09-10 01:07–01:41 IST (`~/rh-lean-work/comparator-tools-2026-09-10.log`); each re-verified here.

| tool | source / tag / commit | binary | SHA-256 |
|---|---|---|---|
| comparator | `leanprover/comparator` tag `v4.33.0`, commit `3927ad383f208ae977c340a91c48ac9b497d2097`; built with toolchain `leanprover/lean4:v4.33.0`; its `Export.Parse` dependency `leanprover/lean4export` rev `15f6055e…` (export format 3.1.0) | `~/rh-lean-work/tools/comparator/.lake/build/bin/comparator` (100 516 016 B) | `fe1222e25fc301dc51ec3f9964a59ab557ea4f9ae6bb758842d70dbb341a5d08` |
| lean4export | `leanprover/lean4export` tag `v4.33.0-rc2`, commit `9fb131bb100eb32ccf6836f14e4f8328d13b6792`, toolchain `leanprover/lean4:v4.33.0-rc2` (= the project's); export format version `3.1.0` (`Export.lean` l. 423) | `~/rh-lean-work/tools/lean4export/.lake/build/bin/lean4export` (173 515 312 B) | `de4ffedf1412873c0d196f4c4eb98d3b45af43f37bd6cc07e2517706481a7775` |
| nanoda | `ammkrn/nanoda_lib` commit `4c544ed4099c8227f07d5de77ad1e69fb0740a27` (2026-09-09; `git describe` v0.3.2-44-g4c544ed; `Cargo.toml` version `0.4.17`), Rust 1.98.1, `cargo build --release`; accepts export format ≥ 3.1.0 and < 3.2.0 (`src/parser.rs` l. 22–23) | `~/rh-lean-work/tools/nanoda_lib/target/release/nanoda_bin` (1 200 160 B) | `d6c87133b59c2286fed27e2417fb17f9419326c2dde904de9f85d288594948bb` |
| landrun | `Zouuup/landrun` commit `811cfff51ceaf3d9843708aa6d22e9b84ccac8b4` (v0.1.17-4-g811cfff), Go 1.27.1, `go build ./cmd/landrun` exit 0 | `/tmp/landrun-test` (orchestrator's build) — **cannot run on macOS**, see §2 | — |
| fake-landrun.sh | comparator tarball `scripts/fake-landrun.sh` ("insecure … landrun shim that doesn't sandbox … intended for development on systems that don't support landrun (i.e. OSX)") | `~/rh-lean-work/tools/comparator/scripts/fake-landrun.sh` (1 431 B) | `167507c89d8b3c7667ad78b50df7b19f89883751a01efd1457404fa34a994e8b` |

Version-compatibility check (parent README's warning): comparator v4.33.0 is the same-era release as the project toolchain
v4.33.0-rc2; lean4export v4.33.0-rc2 matches the toolchain exactly; both comparator's parser and nanoda read export format 3.1.0.
The comparator's `--help` "no such file or directory" noted by the orchestrator is expected: `main` treats its first argument as the
config path and tries to read it (`Main.lean`, `def main`).

## 2. Sandbox status — NOT SANDBOXED (and why)

`landrun` sandboxes through Linux Landlock (an LSM); on macOS the built binary fails at runtime, verbatim (orchestrator, 01:41 IST):
`[landrun:error] 2026/09/10 01:41:07 Failed to apply sandbox: failed to apply Landlock restrictions: missing kernel Landlock support. Landlock is only supported on Linux`.
There is no user-level route around this on macOS (Landlock is a kernel feature; neither sudo nor a purchase would supply it — only a Linux
host would). So `COMPARATOR_LANDRUN` points at the comparator's own `fake-landrun.sh`, which accepts and discards landrun's flags and
`exec`s the command unsandboxed, printing `WARNING: THIS IS NOT REAL LANDRUN! UNSAFELY RUNNING exec …` to stderr for every sandboxed
step (build, export, nanoda). Consequently comparator README assumptions 3–4 (landrun in PATH and working) do NOT hold for these runs;
the `systemd-run` guard is Linux-only and was not used. What this costs: the guarantee against a *malicious* `Solution.DBN` tampering
with the trusted `Challenge.DBN` build during its own build. Here the solution file was written by this program (Job 1) and read by the
independent checker (Job 2, CHECK-O.md: no `import Challenge`, no `native_decide`, trust greps clean), so the un-sandboxed run loses
nothing the record does not already cover; a referee who wants the sandbox re-runs the same two commands on a Linux host with landrun.

## 3. CONTROL run — `comparator/config.json` (the parent's fifteen theorems)

(appended below as it lands; log `results/d1-m2a/packaging/comparator-control-run.log`)

Launched 2026-09-10 (see the log's first line for the timestamp) as `nohup run.sh comparator/config.json CONTROL`; heavy processes
(> 50 % CPU) before launch: none. Reading note for both logs: comparator's own `IO.println` lines ("Building X", "Exporting …",
"Running … kernel") go through a buffered stdout while its children (`lake`, `lean4export`, the shim's WARNING lines) write straight to
the same file, so the comparator lines can appear *later* in the log than the child output they precede; the ORDER of the comparator's
own lines among themselves is the run's true order.

**Result: PASS — `Your solution is okay!`, comparator exit code 0.** Start 02:09:08 IST, end 02:11:59 IST; `/usr/bin/time -l`:
`171.33 real  137.72 user  16.78 sys`, maximum resident set size 6 393 495 552 B (≈ 6.0 GiB; the comparator process, which holds both
exports as strings and the parsed solution environment; the separate `lean4export` child was observed at ≈ 5.9 GB RSS mid-export).
Steps, in the comparator's own order (log lines): `Building Challenge` → lake `Built ChallengeDeps (24s)`, `Built Challenge (3.4s)`
with the fifteen deliberate `declaration uses \`sorry\`` warnings (Challenge.lean lines 40–123), `Build completed successfully (8699 jobs)`;
`Exporting #[Nat, String, String.mk, Char, Quot, Quot.mk, Quot.lift, Quot.ind, <15 theorem names>, propext, Quot.sound, Classical.choice,
Nat.add, …, eagerReduce] from Challenge` (lean4export, format 3.1.0); `Building Solution` → 226:✔ [8876/8877] Built Solution (2.9s);227:Build completed successfully (8877 jobs).; (Zeta23 modules `Replayed`, the
parent's own deprecation warnings only); the same export `from Solution`; then, verbatim, the final lines:

    Running nanoda kernel on solution
    Nanoda kernel accepts the solution
    Running Lean default kernel on solution.
    Lean default kernel accepts the solution
    Your solution is okay!

Fifteen theorems compared (config.json order): two_thirds_on_critical_line, two_thirds_on_critical_line_cumulative,
half_simple_on_critical_line, half_simple_on_critical_line_cumulative, three_quarters_distinct, three_quarters_distinct_cumulative,
montgomery_taylor_on_critical_line, montgomery_taylor_simple_on_critical_line, montgomery_taylor_distinct,
dirichlet_two_thirds_on_critical_line, dirichlet_half_simple_on_critical_line, dirichlet_three_quarters_distinct,
dirichlet_montgomery_taylor_on_critical_line, dirichlet_montgomery_taylor_simple_on_critical_line, dirichlet_montgomery_taylor_distinct.
The shim's `WARNING: THIS IS NOT REAL LANDRUN!` line appears once per sandboxed step (build ×2, export ×2, nanoda ×1) — the run was
NOT sandboxed (§2). Verdict for attribution: the tool chain (comparator v4.33.0 + lean4export v4.33.0-rc2 + nanoda 0.4.17 + shim) works
end-to-end on this machine and this toolchain; any failure of the DBN run would be attributable to the DBN topic, not the tooling.
No tooling fix was needed for the control run.

## 4. DBN run — `comparator/config-dbn.json` (the seven DBN theorems)

(appended below as it lands; log `results/d1-m2a/packaging/comparator-run.log`)
Launched 02:12:45 IST as `nohup run.sh comparator/config-dbn.json DBN`, immediately after the control run; heavy processes before launch:
none; one `lake` at a time (the control run had exited). Config unchanged (`enable_nanoda: true`, the seven names, the three axioms).

**Result: PASS — `Your solution is okay!`, comparator exit code 0.** Start 02:12:45 IST, end 02:16:04 IST; `/usr/bin/time -l`:
`199.09 real  209.73 user  17.43 sys`, maximum resident set size 9 575 104 512 B (≈ 8.9 GiB, the comparator process; the machine has
24 GiB — no swapping: `0 swaps`). Not "tens of minutes and gigabytes of export": lean4export exports only the closure of the requested
constants, not the whole Mathlib environment, so the export is minutes and hundreds of megabytes (measured independently in §5).

Steps, in the comparator's own order, with the child output verbatim:

    Building Challenge.DBN
    WARNING: THIS IS NOT REAL LANDRUN! UNSAFELY RUNNING exec lake build Challenge.DBN
    ✔ [8697/8699] Built ChallengeDeps.DBN (2.0s)
    ✔ [8698/8699] Built ChallengeDeps.DBN.Instance02 (35s)
    ⚠ [8699/8699] Built Challenge.DBN (2.7s)
    warning: comparator/Challenge/DBN.lean:71:8: declaration uses `sorry`      (and :96, :109, :120, :124, :129, :133 — the seven statements, deliberate)
    Build completed successfully (8699 jobs).
    Exporting #[Nat, String, String.mk, Char, Quot, Quot.mk, Quot.lift, Quot.ind, dbn_ray_le_point2_of_certificates, dbn_ray_le_point2_mp,
      dbn_ray_le_point2_arb, dbn_row2BarrierMP_checked, dbn_row2BarrierARB_checked, dbn_row2AsymMP_checked, dbn_row2AsymARB_checked,
      propext, Quot.sound, Classical.choice, Nat.add, Nat.sub, Nat.mul, Nat.pow, Nat.gcd, Nat.div, Nat.mod, Nat.beq, Nat.ble, Nat.land,
      Nat.lor, Nat.xor, Nat.shiftLeft, Nat.shiftRight, String.ofList, Char.ofNat, List, eagerReduce] from Challenge.DBN
    Building Solution.DBN
    WARNING: THIS IS NOT REAL LANDRUN! UNSAFELY RUNNING exec lake build Solution.DBN
    ✔ [8826/8826] Built Solution.DBN (12s)
    Build completed successfully (8826 jobs).
    Exporting #[… the same 43 targets …] from Solution.DBN
    Running nanoda kernel on solution
    Nanoda kernel accepts the solution
    Running Lean default kernel on solution.
    Lean default kernel accepts the solution
    Your solution is okay!

Seven theorems compared (config-dbn.json order): `dbn_ray_le_point2_of_certificates` (G), `dbn_ray_le_point2_mp`, `dbn_ray_le_point2_arb`
(I — the referee's statements, five displayed hypotheses each), `dbn_row2BarrierMP_checked`, `dbn_row2BarrierARB_checked`,
`dbn_row2AsymMP_checked`, `dbn_row2AsymARB_checked` (K). What comparator established for each (its README, "Internals" 4–6, and
`Main.lean` `verifyMatch`): `Comparator.compareAt` — every constant reachable from the statement in `Challenge.DBN`'s export coincides
with the same-named constant in `Solution.DBN`'s export (this covers the 79 copied `ChallengeDeps.DBN` definitions and the 227 literal
`def`s of `ChallengeDeps.DBN.Instance02` that the statements mention — the trusted copy is what was compared, never `Zeta23`);
`Comparator.checkAxioms` — the solution proofs use no axiom outside `propext`, `Quot.sound`, `Classical.choice`; then nanoda re-checked the
whole solution export (§5 for the evidence) and Lean's kernel replayed it (`Environment.replay` in the comparator's own process).
Sandbox: NOT sandboxed (§2) — five shim WARNING lines, one per sandboxed step. No tooling fix was needed for the DBN run either.

## 5. nanoda evidence — did the external kernel actually re-check the proofs?

In the comparator's log the evidence is the pair `Running nanoda kernel on solution` / `Nanoda kernel accepts the solution` (Main.lean
`runNanoda`: nanoda_bin is spawned on the SOLUTION export piped to its stdin with config `{"use_stdin": true, "permitted_axioms": [the
three], "unpermitted_axiom_hard_error": true, "nat_extension": true, "string_extension": true}`; the "accepts" line is printed only when
the process exits 0, and a non-zero exit prints "Nanoda kernel rejected the solution" and fails the run). The shim line
`… UNSAFELY RUNNING exec …/nanoda_bin /var/folders/…` is the spawn itself. nanoda with that config prints nothing on success
(`print_success_message` unset, `main.rs`), so to see *how much* it checked, the export was reproduced outside comparator and fed to
nanoda with `print_success_message: true` (`comparator-run/nanoda-evidence.sh`, identical target list, identical config otherwise):

