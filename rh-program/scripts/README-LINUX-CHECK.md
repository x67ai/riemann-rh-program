# RH program — independent kernel check on Linux (package `rh-linux-check-s30`, built 2026-09-29)

**What this is.** A self-contained package to re-run, on a Linux machine, the machine-checked verification of two Lean units of the
RH research program (Session 30): D5 (the C1 containment theorem, barrier-zoo IV.1; Comparator topics `WeilContainment` and
`WeilContainmentOne`) and IV.17 (the fractional-mark integrality theorem and its rational-mark negation; topic `IntegralityGap`).
Every run so far was on a Mac, where the verification tool's sandbox (`landrun`, Linux Landlock) cannot work and a "fake landrun"
stand-in was used. On Linux the sandbox is real, the binaries are different, and the CPU is different — a green run here is a
fourth kernel replay on a second OS with the sandbox exercised for the first time.

**What is in the package.**
- `lean/` — the program's own Lean 4 additions (Apache 2.0; `lean/README.md` documents them), including `lean/comparator/` with the
  trusted challenge files, the untrusted solutions and the three configs.
- `zeta-23-lean-v1.0/` — a pristine copy (git archive) of Anthropic's `zeta-23-lean` library at tag v1.0, commit 3635e748…, the base
  the program's files overlay (Apache 2.0, Copyright 2026 Anthropic, PBC; canonical home https://github.com/anthropics/zeta-23-lean).
- `scripts/linux-comparator-check.sh` — the whole procedure, unattended.
- `records/` — the Mac-side records to compare against: `COMPARATOR-RUN.md` (tools, revisions, hashes; §2 explains the sandbox
  caveat), and for each unit its `BUILD-NOTES.md`, `CHECK-O.md` (the independent Mac clean-clone check), `FIDELITY.md`, `hashes.txt`.

**What the machine needs.** Ubuntu (or any Linux from 2021 on, kernel ≥ 5.13 with Landlock); git, curl, tar, a C compiler and make
(`sudo apt install build-essential git curl` — the only step that needs sudo); ≈ 12 GB free disk; 8 GB RAM; internet (it downloads
elan + Lean, Rust, Go, Mathlib's prebuilt cache, and the four tools from their public repositories, into `$HOME` only).

**How to run (two commands).**
```
bash scripts/linux-comparator-check.sh
ls ~/rh-lean-linux/logs
```
Roughly 30–60 minutes. The script never uses sudo, never posts anything anywhere, and writes only under `~/rh-lean-linux/`.

**What "success" looks like** (`~/rh-lean-linux/logs/99-summary.txt`): `landrun sandbox: REAL (Landlock works on this kernel)`;
`print-axioms WeilContainment: 12 names on the three standard axioms; sorryAx: 0`; `print-axioms WeilContainmentOne: 1 …`;
`print-axioms IntegralityGap: 16 …`; and three lines `comparator config-…: PASS (exit 0; nanoda: 1; fake-landrun warnings: 0)`.
The tool hashes in `10-tool-hashes.txt` will DIFFER from the Mac's (different OS and CPU) — that is expected; the source revisions
are the same and are printed in the logs.

**What to send back.** The whole folder `~/rh-lean-linux/logs/` (a few hundred KB). Nothing else is needed.

---

## For the Claude Code session on this machine — paste this as the prompt

```
Read README-LINUX.md in this package and follow it: run scripts/linux-comparator-check.sh unattended (it installs everything it
needs into $HOME without sudo; if it reports that git, curl, a C compiler or make are missing, tell me the one apt command to run
and wait). When it finishes, read ~/rh-lean-linux/logs/99-summary.txt and 00-main.log, and report in plain English: whether the
landrun sandbox was REAL, the three print-axioms lines, the three comparator results with their exit codes, and the Lean and
Mathlib versions printed. If any stage failed, read that stage's log and tell me what it says. Do not modify anything under lean/ or
zeta-23-lean-v1.0/; do not post anything anywhere. Then zip ~/rh-lean-linux/logs into ~/rh-linux-check-s30-logs.zip for me to send back.
```
