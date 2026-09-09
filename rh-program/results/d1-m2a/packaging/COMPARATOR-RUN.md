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

Run 1 (`comparator-run/nanoda-evidence-dbn.log`, 02:17:02–02:18:24 IST): `lake env lean4export Solution.DBN -- <the 43 targets>` →
`solution.export` in `~/rh-lean-work/comparator-evidence-dbn/` (not committed; 406 013 219 bytes, 7 590 534 lines; header
`{"meta":{"exporter":{"name":"lean4export","version":"3.1.0"},"format":{"version":"3.1.0"},"lean":{"githash":"d8b18978…","version":"4.33.0-rc2"}}}`);
lean4export 13.34 s real, 6.14 GB peak RSS. Then `nanoda_bin nanoda-config.json` (file input instead of stdin, otherwise the comparator's
config plus `print_success_message: true`): **`Checked 56428 declarations with no typechecker errors, 1 pretty printer errors:
["Unable to print axioms"]`**, exit 0, 43.34 s real, 2.90 GB peak RSS. The "pretty printer error" is bookkeeping, not a check failure:
nanoda's `print_axioms` defaults to true and, with no pretty-printer destination configured, `pretty_printer.rs` l. 383–384 records
"Unable to print axioms" — the typechecker had already finished with zero errors (`main.rs` `use_config`: the message is built only
after `check_all_declars()`).
Run 2 (`comparator-run/nanoda-evidence-dbn-axioms.log`, 02:19:26 IST): the same with `pp_to_stdout: true` so nanoda prints the axioms it
admitted. Verbatim output:

    axiom propext {a b : Prop} : Iff a b → Eq a b
    axiom Quot.sound.{u} {α : Sort u} {r : α → α → Prop} {a b : α} : r a b → Eq (Quot.mk r a) (Quot.mk r b)
    axiom Classical.choice.{u} {α : Sort u} : Nonempty α → α
    Checked 56428 declarations with no errors

42.80 s real, 2.87 GB peak RSS; exit code on nanoda-config-pp.json: 0 (02:21:34).
Composition of the export (`comparator-run/export-kinds-dbn.txt`, this job's parser over the JSON lines): 42 101 `thm`, 11 209 `def`,
991 `inductive` (with their constructors and recursors), 46 `opaque`, 4 `quot`, **3 `axiom`** — the whole Mathlib + Zeta23 + trusted-copy
closure of the seven theorems, replayed declaration by declaration by a kernel written independently of Lean's (Rust). So: yes, the
external kernel re-checked the proofs — 56 428 declarations, no errors, exactly the three permitted axioms admitted.

## 6. Sponsor — nothing needed

No step needed sudo, a login, or a purchase. The only thing this machine cannot supply is the Linux Landlock sandbox (§2), and no
user-level or sponsor-level action on macOS supplies it; if a sandboxed run is ever wanted, the instruction is: on any Linux machine
with the same toolchain, clone the tree, build landrun from `main`, and run the command in §0 with real `landrun` on `PATH` (and the
`systemd-run` wrapper of the parent's README).

## 7. Figures at a glance

| run | config | theorems | wall | peak RSS (comparator) | final line | exit |
|---|---|---|---|---|---|---|
| CONTROL | `comparator/config.json` | 15 (parent) | 171.33 s (02:09:08–02:11:59 IST) | 6 393 495 552 B | `Your solution is okay!` | 0 |
| DBN | `comparator/config-dbn.json` | 7 (DBN) | 199.09 s (02:12:45–02:16:04 IST) | 9 575 104 512 B | `Your solution is okay!` | 0 |
| nanoda evidence | `Solution.DBN` export → nanoda_bin | (56 428 declarations) | export 13.3 s + nanoda 43.3 s / 42.8 s | 6.14 GB / 2.90 GB | `Checked 56428 declarations with no errors` | 0 |

Export size (DBN solution side): 406 013 219 B, 7 590 534 lines. Lake work inside the runs: control — `Built ChallengeDeps (24s)`,
`Built Challenge (3.4s)`, `Built Solution (2.9s)` (8699 / 8877 jobs); DBN — `Built ChallengeDeps.DBN (2.0s)`,
`Built ChallengeDeps.DBN.Instance02 (35s)`, `Built Challenge.DBN (2.7s)`, `Built Solution.DBN (12s)` (8699 / 8826 jobs). No producer ran;
one `lake` at a time; heavy-process check before each launch: none. No tooling fix, patch, or version change was needed by this job; the
orchestrator's builds (§1) were used as found and re-hashed. Nothing under `Zeta23/` or `comparator/` was edited.

## 8. `formalization.yaml` — outcome appended, re-validated, mirrored

Appended to `review.notes` (the schema's only free-text field under `review`; `review.status` left at `self-assessed` — no human has
read the trusted files) in `rh-program/lean/formalization.yaml` (386 → 411 lines) a paragraph beginning "Comparator run
(results/d1-m2a/packaging/COMPARATOR-RUN.md, Session 20 Job 3, …): performed without sandbox, nanoda enabled." with the verbatim final
lines, the versions, the nanoda evidence, the sandbox statement, the control run, and the label sentence. Validation after the edit
(`comparator-run/formalization-yaml-jsonschema-job3.log`): PyYAML 6.0.3 + jsonschema 4.25.1 (Draft 7) against the upstream dispatcher
`formalization.schema.json` (SHA-256 22bd0b61…, re-fetched by this job and byte-identical to the stored copy) resolving to
`v0.4.schema.json` (SHA-256 25ff6b25…) — **errors: 0**; and Job 1's route (Ruby/Psych → JSON → `validate_yaml.py`) — **validation
errors: 0**, no key outside the schema. Copied to `~/rh-lean-work/zeta-23-lean-main/formalization.yaml`, `cmp` identical.

## 9. Files this job wrote, with SHA-256 (KICKSTART 10(i))

All under `results/d1-m2a/packaging/` unless noted; the report's own hash is in `comparator-run/hashes.txt` (computed after the
report was final). The 406 MB export and its two nanoda configs stay in `~/rh-lean-work/comparator-evidence-dbn/` (outside the repo).

    ed12b901ad20a94429b0296e8232eb0294b48bae758803138b025bb2e3219f54  comparator-control-run.log
    29c2667ec37a334580c434c4dd3396df66f7d10b7f8a05ff48f3ef51ccf5a14b  comparator-run.log
    5de1cc10c11380c59e49e88bdac5bbece32f7dd6674bb8ffc3caa4d5527c8155  comparator-run/run.sh
    e941bc0c6f9f13f754365caa64e307677f0e10a174523c5fe50f82b6d47c6b23  comparator-run/prerun-cleanup.log
    a4b87c507497ea45d23c7d2a34df8116e6a552c2c6c70cdf49f59c99d1e7adb4  comparator-run/nanoda-evidence.sh
    2d52a1cc887991cc45b3f70eeccbde01dca6f893a706d2aad3cc313ea5976772  comparator-run/nanoda-evidence-dbn.log
    32dda3be8cfcab95314524533279215c3389e7f14794b575077982faefb73209  comparator-run/nanoda-evidence-dbn-axioms.log
    6b81cc67ecfdc85bce089f8bcc15bb616086c73211dbf5a8f6138dd404e4b439  comparator-run/export-kinds-dbn.txt
    faa8fed88ff98f71619fcfaa78a6041ebcec77d0c3ba9b33943fbf079c4ff8d2  comparator-run/validate_yaml_jsonschema.py
    780a5aa5f9cc93931510f6b33805552a9ca82202dec3a25050be285a7bc8c3f0  comparator-run/formalization-yaml-jsonschema-job3.log
    42e8d26d5c0c72c09f922fe1e0b0cfc21231f36d465c863be4a0ee0ad42e48b6  rh-program/lean/formalization.yaml
    42e8d26d5c0c72c09f922fe1e0b0cfc21231f36d465c863be4a0ee0ad42e48b6  /Users/jaytyagi/rh-lean-work/zeta-23-lean-main/formalization.yaml
    5eed7e04cec66b60eede56171e246cdf2fcd4807abaf0f4db477ad1de55e0acd  /Users/jaytyagi/rh-lean-work/comparator-evidence-dbn/solution.export
