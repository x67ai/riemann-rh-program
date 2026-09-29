# RH program — second independent kernel check on Linux (package `rh-linux-check-s33`, built 2026-09-29, Session 33)

**What this is.** A self-contained package to re-run, on a Linux machine, the machine-checked verification of the three Lean units
the RH research program shipped since its first Linux replay (Session 30): H5 (IV.1's prime-side containment into Zeta23's C² test
class for continuous g; Comparator topics `WeilContainmentC2One` and `WeilContainmentC2`), I.1's witness table (Epstein Λ_Q(6),
Λ_Q(36) and Davenport–Heilbronn Λ(3), (4), (6), (12) kernel-checked; topics `EpsteinWitnessSix` and `I1Witness`), and H4 (IV.17's
pair channel: Prop. 4.5 for every depth and real mark, the integer-mark safety chain, the floor's failure at (1/4, 1/20) by a kernel-
checked certificate; topic `PairChannel`). Every run of these so far was on a Mac, where the verification tool's sandbox (`landrun`,
Linux Landlock) cannot work and a "fake landrun" stand-in was used. On Linux the sandbox is real, the binaries are different, and the
CPU is different — a green run here is a further kernel replay on a second OS with the sandbox exercised, exactly as the Session-30
package did for the earlier units.

**If the Session-30 package was run on this machine,** `~/rh-lean-linux/` already holds the base library, Mathlib's cache and the
four tools; this run reuses all of it and only refreshes the program's files and builds the five new topics (≈ 10–20 minutes). Its
logs go to `~/rh-lean-linux/logs-s33/` so the Session-30 logs are untouched. On a fresh machine it installs everything as before.

**What is in the package.**
- `lean/` — the program's own Lean 4 additions (Apache 2.0; `lean/README.md` documents them), including `lean/comparator/` with the
  trusted challenge files, the untrusted solutions and every config (the five new ones are the ones this run uses).
- `zeta-23-lean-v1.0/` — a pristine copy (git archive) of Anthropic's `zeta-23-lean` library at tag v1.0, commit 3635e748…, the base
  the program's files overlay (Apache 2.0, Copyright 2026 Anthropic, PBC; canonical home https://github.com/anthropics/zeta-23-lean).
- `scripts/linux-comparator-check-s33.sh` — the whole procedure, unattended (the Session-30 script is included too, for reference).
- `records/` — the Mac-side records to compare against: `COMPARATOR-RUN.md` (tools, revisions, hashes; §2 explains the sandbox
  caveat), and for each unit its `BUILD-NOTES.md`, `CHECK-O.md` (the independent Mac clean-clone check), `FIDELITY.md`, `hashes.txt`.

**What the machine needs.** Ubuntu (or any Linux from 2021 on, kernel ≥ 5.13 with Landlock); git, curl, tar, a C compiler and make
(`sudo apt install build-essential git curl` — the only step that needs sudo, already done if the Session-30 run happened here);
≈ 12 GB free disk; 8 GB RAM; internet (downloads go into `$HOME` only).

**How to run (two commands).**
```
bash scripts/linux-comparator-check-s33.sh
ls ~/rh-lean-linux/logs-s33
```
The script never uses sudo, never posts anything anywhere, and writes only under `~/rh-lean-linux/`.

**What "success" looks like** (`~/rh-lean-linux/logs-s33/99-summary.txt`): `landrun sandbox: REAL (Landlock works on this kernel)`;
`print-axioms WeilContainmentC2One: 1 names on the three standard axioms; sorryAx: 0`; `print-axioms WeilContainmentC2: 1 …`;
`print-axioms EpsteinWitnessSix: 3 …`; `print-axioms I1Witness: 14 …`; `print-axioms PairChannel: 8 …`; and five lines
`comparator config-…: PASS (exit 0; nanoda: 1; fake-landrun warnings: 0)`. The tool hashes in `10-tool-hashes.txt` will DIFFER
from the Mac's (different OS and CPU) — expected; the source revisions are the same and are printed in the logs. (The Session-30 run
reported the best-effort sandbox at Landlock ABI v8 and the strict probe as FAIL because the pinned landrun asks for ABI v9 — the
same line is expected here and is not a failure of the check.)

**What to send back.** The whole folder `~/rh-lean-linux/logs-s33/` (a few hundred KB), zipped. Nothing else is needed.

---

## For the Claude Code session on the Linux machine — paste this as the prompt

```
Read README-LINUX.md in this package and follow it: run scripts/linux-comparator-check-s33.sh unattended (it reuses
~/rh-lean-linux if the earlier package left it there, and otherwise installs everything it needs into $HOME without sudo; if it
reports that git, curl, a C compiler or make are missing, tell me the one apt command to run and wait). When it finishes, read
~/rh-lean-linux/logs-s33/99-summary.txt and 00-main.log, and report in plain English: whether the landrun sandbox was REAL, the
five print-axioms lines (expected 1, 1, 3, 14, 8 names on the three standard axioms, sorryAx 0), the five comparator results with
their exit codes, and the Lean and Mathlib versions printed. If any stage failed, read that stage's log and tell me what it says. Do
not modify anything under lean/ or zeta-23-lean-v1.0/; do not post anything anywhere. Then zip ~/rh-lean-linux/logs-s33 into
~/rh-linux-check-s33-logs.zip for me to send back.
```
