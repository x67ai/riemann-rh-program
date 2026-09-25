# CHECK-O-B — D4 Job 2 parts B and C (Opus 5, the independent second model): my own Control-1 launches, and the post-sweep re-check of the note

**Opened Fri Sep 25 16:22 IST 2026 (machine clock). Contract: `CHECK-O-B-BRIEF.md` (read in full), `BRIEF.md` "Job 2" parts B and C. Every number below is printed by a script under `checker-O/`, and the script's log is named in place. I edited nothing of Job 1's: not the note, not a JSON, not `hashes.txt`, not the harness. I wrote only under `checker-O/`, this file, and dated rows appended to `SHARED.md`. Nothing was committed by hand (the watchdogs do that). Standing orders 5 and 7 bind.**

**Hashes checked FIRST, before anything ran (`shasum -a 256`, 16:22:30 IST):**
* my evaluator, source `checker-O/twsumO.go` = 90e144f502fbaf6d0214fe605d9923ee0f0111da27193b1d315f2be768ff1437, and binary `checker-O/twsumO` = d57080a8eeee7da8e59322df2446c976a3b8ee64a18cf6064975dced489d0f45. Both match part A, so there was **no rebuild** and stop line (3) does not arise. `replayOB.py` asserts the binary hash again before each batch.
* The inputs, as the brief names them: `d4-sweep-note.md` 80a14ea23bc732a48c2b8b163d3ab5d0d487b6668a853470b222909d01852086; `SHARED.md` dea0d1810d1978af5bfbcf5924609388e51278d73fcc608c463953ea9ece180c (before my rows); `hashes.txt` bbc1426041f5ff129dfb95b2257790531064a9330acce9293f54cececbd82a2f; `CHECK-O-A.md` 261e53fea34ab605d801d020c5525736364c61ae239dd3faca6c1ba580815d3e; `BRIEF.md` 8ca22341af0eaa9b1e4be2c5175037918fcb1881a5025cb01322baeaf77d096d.

**Inputs read at the page:**
* `CHECK-O-B-BRIEF.md` and `CHECK-O-A.md`, in full.
* `d4-sweep-note.md`: §0–§5, §7–§12 in full, and §6 by script (all 133 rows are parsed in C.1).
* `SHARED.md`: the checkpoints, the Control-1 rows and the close block.
* `harness/eps_phi.json`, `sweep_plan.json`, `d4_twisted_sum.rs` (lines 1–40, 140–150, 380–410, 470–500), `d4_point.py` (the hashing and binary-call lines), `d4_plan.py` (the ladder line), `d4_run_tier.py` (the replay block).
* The five sidecars; the zeta, control1 and replayO JSONs (by script).
* The prior-art texts and the Odlyzko 1992 pages, in C.3.
* The directions files at the lines named, in C.6.

