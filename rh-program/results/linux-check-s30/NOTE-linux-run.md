# Note from the Linux session (2026-09-29, Ubuntu, kernel 7.0.0-34-generic, x86_64, 12 cores, 37 GB RAM)

Written by the Claude Code session that ran the package `rh-linux-check-s30` on the sponsor's Linux machine. Read this before the logs.

## Two runs, one script bug

**Run 1** (`bash scripts/linux-comparator-check.sh`, unmodified, 01:55–02:17 IST) installed everything, built Zeta23, produced the three
print-axioms results, built the four tools, and ran the FIRST comparator config (`config-weil-containment-one.json`) — PASS, exit 0,
nanoda and the Lean kernel both accepted — and then **stopped**. No second or third comparator run, no `99-summary.txt`. Cause: line 92
of the script wraps each comparator run in a brace group `{ …; exit $rc; } > "$L"`. A brace group runs in the current shell, so
`exit $rc` ended the whole script after the first config (exit status 0, silently). Run 1's comparator log is preserved as
`11-comparator-config-weil-containment-one.RUN1.log`. Run 1's lines are the first block of `00-main.log`.

**Run 2** (05:33 IST) used a copy of the script with two changes (`fixed-script/linux-comparator-check.fixed.sh`; exact diff against the
package's script in `fixed-script/linux-comparator-check.diff`), invoked with the package root as its argument:
1. the brace group became a subshell `( … )`, so `exit $rc` only ends that config's block and the loop continues;
2. a second landrun sanity test was added (see below). The original strict test was left in place unchanged.
Run 2 passed its first comparator config again, but my added landrun test was itself wrong (it omitted the comparator's `-ldd -add-exec`
flags, so the sandbox rightly refused to execute `/bin/true` and the test reported FAIL). I stopped run 2 after its first config, fixed the
test, and launched **run 3** (05:36 IST) with the corrected copy. Run 3 is the run of record: its lines are the last block of
`00-main.log`, its comparator logs are `11-comparator-*.log`, and `99-summary.txt` is its summary. Nothing under `lean/`,
`zeta-23-lean-v1.0/`, `comparator/` or `Zeta23/` was touched by any run. Runs 2 and 3 re-used the already-installed toolchains, Mathlib
cache, Zeta23 build and tool builds (all no-ops), removed the Challenge/ChallengeDeps/Solution build artifacts as the script does, and
ran the comparator from scratch on each config.

## The landrun sandbox: the script's test says FAIL, but the comparator's runs WERE sandboxed

The script's sanity test runs `landrun --rox / -- /bin/true` (no `--best-effort`). landrun at the pinned commit 811cfff (v0.1.18,
go-landlock v0.9.0) then demands Landlock ABI **v9** (`internal/sandbox/sandbox.go`: the handled access set is "everything Landlock V9
supports", including v9's UNIX-socket connect scoping). This kernel (7.0.0) supports Landlock ABI **v8** — confirmed two ways:
landrun's own error (`09-landrun-test.log`: "Got Landlock ABI v8, wanted {Landlock V9; …}") and a direct
`landlock_create_ruleset(NULL, 0, LANDLOCK_CREATE_RULESET_VERSION)` syscall (`fixed-script/landlock_abi.c`, output in
`fixed-script/landlock-abi-probe.txt`: 8). So the strict test fails: it is not "kernel without Landlock", it is "kernel one ABI
version behind what this landrun build asks for by default".

The comparator never invokes landrun that way. `comparator/Main.lean`, `buildLandrunArgs`, hard-codes
`--best-effort --ro / --rw /dev -ldd -add-exec …` for every sandboxed step (Challenge build, Solution build, both exports, nanoda).
With `--best-effort`, go-landlock applies the strictest ruleset the running kernel supports — here ABI v8: full filesystem and TCP
restrictions and signal/abstract-socket scoping; the only thing dropped relative to v9 is the UNIX-domain-socket connect rule, which
is irrelevant to a Lean build. The added test (`09b-landrun-best-effort-test.log`) runs landrun with the comparator's exact flags
(`--best-effort --ro / --rw /dev -ldd -add-exec`) and then proves the sandbox bites: a child told to write
`logs/landrun-write-probe.txt` under `--ro /` is refused with "Permission denied" and the file does not exist afterwards. The comparator logs (`11-comparator-*.log`) contain zero `NOT REAL LANDRUN` lines: the
fake shim was never involved. Verdict: **the sandbox in all three comparator runs was REAL Landlock (ABI v8, best-effort mode).**

## Tool hashes differ from the Mac's — expected
Different OS, CPU and binaries; see `10-tool-hashes.txt`. Source revisions are the pinned ones (the script checks them out by commit).

## Which run each file belongs to
- `00-main.log`: all three runs, in order (run 1 from 01:55, run 2 from 05:33, run 3 from 05:35). Run 1's block carries the one-time
  installs (elan, Rust, Go, Lean download, Mathlib cache download, the full Zeta23 build "971 log lines", tool clones and builds).
- `01-…` to `10-…`: overwritten by run 3, so they show the cached re-runs (e.g. `02-build-zeta23.log` is the replay, `08-build-landrun.log`
  is empty because `go build` had nothing to do). The print-axioms logs (`04-*`) are identical in content across runs.
- `11-comparator-*.log` and `99-summary.txt`: run 3. `11-comparator-config-weil-containment-one.RUN1.log`: run 1's copy of the same
  config (also PASS, exit 0), kept for comparison.
- `fixed-script/`: the script copy that runs 2 and 3 used, its diff against the package's script, and the Landlock ABI probe.

## Result (run 3, 05:35–05:38 IST)
Lean 4.33.0-rc2 (x86_64-unknown-linux-gnu, commit d8b18978), Mathlib 51e6992efd06126df61a496bebf8f49482a4e129, same as the Mac record.
print-axioms: WeilContainment 12 names, WeilContainmentOne 1, IntegralityGap 16 — all on [propext, Classical.choice, Quot.sound], sorryAx 0.
comparator: config-weil-containment-one PASS (exit 0), config-weil-containment PASS (exit 0), config-integrality-gap PASS (exit 0);
each with "Nanoda kernel accepts the solution", "Lean default kernel accepts the solution", "Your solution is okay!"; 0 fake-landrun lines.
Sandbox: REAL Landlock (ABI v8, comparator's --best-effort mode). Wall time per comparator run 35–51 s, peak RSS ≈ 7.2 GB.
