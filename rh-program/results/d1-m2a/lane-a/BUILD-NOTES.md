# D1 M2a Lane A — BUILD-NOTES (builder, phase 3 jobs A and B)

**Stamp:** 2026-09-09 21:26–21:37 IST, machine clock (Session 19, builder after PLAN.md GO and PLAN-REVIEW.md APPROVED).
Brief: `BRIEF.md`; recipe: `PLAN.md` §1 (Lean), §3.5 (command lines), §4 phase 3 (a)–(b); review fixes honored: F-3 (below),
F-6 (the "what the kernel does not use" sentence is in the module header). Trust vocabulary unchanged: the producers are
UNTRUSTED; the kernel checks C-A1…C-A6 on integers; H2-A and H-TAIL stay DISPLAYED; never "fully machine-checked". U.S. English.

## A. Lean — `Zeta23/DBN/Asym.lean` (DONE, nothing owed)

**Tree changes (exactly two, nothing else):**
1. NEW `~/rh-lean-work/zeta-23-lean-main/Zeta23/DBN/Asym.lean` (12 639 bytes) — `windowIdx`, `AsymRow`, `TailRow`, `AsymData`,
   `checkAsymRow`, `consecutive`, `lastNhi`, `checkAsym` (C-A1…C-A6), `At0`/`Ay0`/`AyA`, `AsymEnclOK` (H2-A), `TailOK` (H-TAIL),
   `cover_of_consecutive`, `cert_of_checkAsym` (SPEC §8.3 statement verbatim), `windowIdx_mono` (L-A2), `row2_windowIdx_ge` (L-A1).
   Text = `laneA-shapes-scratch.lean` (planner) = `review-shapes.lean` (reviewer), re-namespaced `Zeta23.DBN.LaneAScratch` → `Zeta23.DBN`;
   header in the style of `BarrierCert.lean` (trust model, what the kernel does not use = PLAN-REVIEW F-6, "NOT HERE" for the literals).
   No `sorry`, no `axiom`, no `native_decide` (the two grep hits on the file are the header's own words "sorry-free" / "no `native_decide`").
   Placement note: the orchestrator put L-A1 (`row2_windowIdx_ge`) in this module; PLAN §1.5's placement paragraph had it in the literal
   modules. It depends only on `windowIdx` and `Real.pi_lt_d6`, not on any literal, so the emitted `Instance02/Asym_{mp,arb}.lean` simply
   reference `row2_windowIdx_ge` from here (the glue lemma text of PLAN §1.5 is unchanged).
   NO literal is in the tree: the placeholder (float plan, NOT a certificate) lives only in the scratch files under `results/`.
2. `Zeta23.lean` (the DBN module list; there is no `Zeta23/DBN.lean`): one line `import Zeta23.DBN.Asym` inserted after
   `import Zeta23.DBN.BarrierCert`, before `import Zeta23.DBN.Instance02`. Backup of the previous root: scratchpad `Zeta23.lean.bak`.
   `Instance02.lean` NOT touched (the replacement waits for the literal, PLAN §1.5 / phase 3(d)).

**Build (`asym-build.log`).** `lake build Zeta23.DBN.Asym`: `Built Zeta23.DBN.Asym (9.6s)`, `Build completed successfully (3142 jobs)`,
zero warnings, 11.8 s wall, 3.06 GB RSS. Then the root `lake build Zeta23` with the new import: `Built Zeta23 (16s)`, `Build completed
successfully (9140 jobs)`; the only warnings are two pre-existing deprecation replays in `Zeta23/XiPrime/FamilyHypsV.lean` (not ours).
**`-j2` note:** this Lake (5.0.0-src+d8b1897, Lean v4.33.0-rc2) has NO jobs option — `-j2`, `-j 2`, `-j=2`, `--jobs=2` all fail with
"unknown short/long option" (the `lake --help` OPTIONS section is copied into the log). Session 16 also used plain `lake build <target>`
(`lean-notes.md`). A single-module build with every dependency already built spawns ONE `lean` process, so the thermal intent (≤ 2 compile
jobs) held; one `lake` process at a time throughout, no producer running during either build (heavy-jobs-before = 0 in the log).

**`#print axioms` (`asym-axioms.log`, scratch `asym-axioms-scratch.lean`, `lake env lean` against the BUILT module, exit 0):**
    'Zeta23.DBN.cover_of_consecutive' depends on axioms: [propext, Quot.sound]
    'Zeta23.DBN.cert_of_checkAsym'    depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.DBN.windowIdx_mono'       depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.DBN.row2_windowIdx_ge'    depends on axioms: [propext, Classical.choice, Quot.sound]
No `sorryAx` anywhere.

**Build verification on the module's own names (`asym-check-scratch.lean` → `asym-check.log`, exit 0, 2.2 s, zero errors/warnings):**
the 3-row PLACEHOLDER literal `checkAsym … = true` by `decide +kernel` → `[propext]`; the two negative controls (row gap → C-A4 false;
tail sum + 4·10²¹ → C-A6 false) → `[propext]`; the glue lemma `row2_laneA` (PLAN §1.5 text) → `[propext, Classical.choice, Quot.sound]`;
the reviewer's three composition tests (PLAN-REVIEW A18) feeding `row2_laneA hAsym hTail` into the REAL `lambda_le_point2`,
`lambda_le_point2_arb`, `row2_ray_mp` of the built `Instance02.lean` as their `hLaneA` argument all elaborate. So the emitter's target
(the literal module + glue, phase 3(d)) is known to compose with this module character for character.

**Repo mirror.** `rh-program/lean/Zeta23/DBN/Asym.lean` = byte-identical copy (`cmp` clean), as Session 16 did for the other four DBN
files (which are still byte-identical to the tree, checked). The mirror has no root `Zeta23.lean`; the added import line is recorded here.

**Owed from job A: nothing.** All four theorems closed (no sorry, no axiom). Phase 3(d) still owes: the two literal modules
`Instance02/Asym_{mp,arb}.lean` (emitter = successor of `emit_lean_m2a.py`, back-parse), the `hLaneA` replacement in `Instance02.lean`,
`#print axioms` there, the label/bookkeeping edits of PLAN-REVIEW F-5, and the Opus audit.

## B. Producers — the full P-9/P-10 run (LAUNCHED 21:36:29 IST, detached)

**F-3 applied first (PLAN-REVIEW §7, "phase-3 driver robustness"), identically to both legs, by `apply_f3.py` (scratchpad; exact-match,
each pattern once per file), record `f3-patch.diff`, dated comments in the code.** Arithmetic untouched — the derivation code (`Leg`,
`Tables`, `G`, `sub_box`, `defect_window`, `tail_row`) is not in the diff.
  (a) `run_rows` ends with `sys.exit(6)` when any row recorded an exception or `ok = False` (so `run_leg.sh`'s `|| exit 3` fires and the
      leg does NOT proceed to tail/assemble);
  (b) `--resume` skips a row only when its record loads with `ok is True`; a record with an exception or `ok = False` is recomputed;
  (c) the `tail-done` status MERGES into the leg's dict (`merge_status`), so `windows_done/windows_total/started/rows_*` survive the tail
      phase, and the tail error (if any) is appended to `errors`;
  (+) `run_tail` exits 7 when its `ok` is false (same spirit as (a): fail loud before `assemble`);
  (+) `update_status` adds a TOP-LEVEL roll-up to `STATUS.json` — `phase` ("mp:<phase> arb:<phase>"), `windows_done` (min over legs),
      `windows_total` (max), `started` (earliest), `updated`, `eta_hours` (max), `errors` (leg-prefixed) — so the file carries the brief's
      keys at the top level as well as per leg (`STATUS.json["mp"]`, `["arb"]`; also `STATUS-mp.json`, `STATUS-arb.json`).
  Tested before launch in a scratch dir (`scratchpad/f3test`, not under the repo): Arb on the reviewer's 50-window plan → 3/3 ok,
  bit-identical `T`, `E`, `T_lo` to `review-batch/`; second run with `--resume` → 3 skips; a record injected with `ok=false` → that row
  alone recomputed; tail (no `--direct`) → merged status keeps `windows_* = 50`; a plan with Nlo > Nhi → error recorded, top-level
  `errors = ['arb: row 0: AssertionError()']`, **exit 6**. mp on row 0 → bit-identical to `review-batch/batches/mp-row_0000.json`
  (13.0 s), `--resume` → skip. `python3 -m py_compile` clean on both.

**Launch (`launch_producers.sh` → `producers.log`), exactly PLAN §3.5's two lines, from this directory, OUT = `.`:**
    nohup ./run_leg.sh mp  . > producers-mp.log  2>&1 &        # pid 5302  (child: python3 p9_mp.py  rows --plan rows-plan.json --out . --resume)
    nohup ./run_leg.sh arb . > producers-arb.log 2>&1 &        # pid 5303  (child: python3 p9_arb.py …)
macOS has no `setsid`; detachment = `nohup` + `&` + `disown` + stdin `/dev/null`; verified after the launching shell returned: both
`run_leg.sh` have parent pid 1 (launchd). PIDs also in `producers-mp.pid`, `producers-arb.pid`. Heavy jobs before launch: 0; during the
run: 2 (one python3 per leg; no `lake`), RSS 31 MB (mp) / 24 MB (Arb). `caffeinate` running (pid 5186). Logs: `producers.log` (launch
record), `producers-mp.log`, `producers-arb.log` (per-leg stdout/stderr, PLAN's names).

**Resume command (after a kill, from this directory; rows on disk with ok = true are skipped, tail + assemble re-run):**
    cd "…/rh-program/results/d1-m2a/lane-a" && ./launch_producers.sh
(or either PLAN line alone for one leg). A kill loses at most one row (≤ 14 s mp) or the tail in flight (≤ 7 min mp with `--direct`).

**First verification (21:36:41 IST, 12 s after launch).** Arb: 3/3 rows `ok=True` in 1.3 s — T_lo = 0.012023114801271918 /
0.012022114003010781 / 0.1544290524314511, E_hi = 1.059·10⁻⁷ / 8.50·10⁻⁸ / 2.69·10⁻⁸ (E/T ≤ 8.8·10⁻⁶; the float plan's T 0.012025 /
0.012024 / 0.15443 reproduced to 4 digits, E a little above the plan's on the wide rows = the hull); `batches/arb-row_000{0,1,2}.json`
on disk; `STATUS.json` written with the roll-up; the Arb `--direct` tail running. mp: `rows` running (row 0 in flight).

**Second verification (21:38:05 IST, 96 s after launch) — batches landing, STATUS.json updating per batch: CONFIRMED.**
* Arb leg: **DONE 21:36:43 IST** (14 s wall). Tail (`batches/arb-tail.json`): Q₁…Q₄, E₁ = 1780738683686 / 178607231320 / 18638466998 /
  19014989007 / 1823 at K = 10¹², sum 1 996 999 372 834 < 2·10¹², (S1)–(S4) true, `--direct` contained = true (11.8 s); `asym-arb.json`
  assembled, "all ok: True". Bit-identical to the pricing tail of PLAN §3.2.
* mp leg: rows **3/3 ok in 40.6 s** (13.5 / 13.5 / 13.7 s): T_lo = 0.012023114801271918 / 0.012022114003010781 / 0.1544290524314511 —
  identical to the Arb leg's T_lo to every printed digit (P-11's T agreement already visible); E_hi = 1.0307·10⁻⁷ / 7.569·10⁻⁸ /
  2.129·10⁻⁸ (E/T ≤ 8.6·10⁻⁶). `batches/mp-row_000{0,1,2}.json` on disk (21:36:44, 21:36:57, 21:37:10). The mp tail with `--direct`
  started 21:37:10 (pid 5338), expected ≈ 415 s → done ≈ 21:44 IST; then `assemble` → `asym-mp.json`.
* `STATUS.json` updated at 21:36:31, 21:36:42, 21:37:10 (one write per batch), top level `{phase: "arb:tail-done mp:rows-done",
  windows_done: 4510217, windows_total: 4510217, started: "2026-09-09 21:36:29 IST", updated: …, eta_hours: 0.0, errors: []}`,
  per-leg dicts under `"mp"` and `"arb"`. Heavy jobs during the run: 2 → now 1 (the mp tail); no `lake`.
* Certified vs planned T: 0.0120231 vs 0.0120250, 0.0120221 vs 0.0120238, 0.154429 vs 0.154430 — agreement to 4–5 digits, as
  PLAN §4 risk (i) expected; no row came out with T ≤ E (margins > 10⁵×), so no split is needed.

**FOR STEP (c) — PLAN-REVIEW F-2 is now a fact, with numbers.** Cross-leg E_hi ratios (Arb/mp) on the three planned rows:
row 0 (115 713 windows) 1.0589·10⁻⁷ / 1.0307·10⁻⁷ = **1.027**; row 1 (722 945) 8.504·10⁻⁸ / 7.569·10⁻⁸ = **1.124**; row 2 (3 671 559)
2.686·10⁻⁸ / 2.129·10⁻⁸ = **1.261** — Arb the larger on every row (its ball hull over the wide x-range), T_lo agreeing to all digits,
`ok = True` on both legs. `crosscheck_lane_a.py .` with the default `--etol 1e-3` WILL exit 1 on E for all three rows — the benign
hull-slack case of F-2, not a producer disagreement. Per the review's fix: record the ratios (here) and the larger leg (Arb), re-run with
`--etol` just above the observed maximum (e.g. `--etol 0.3`), and note the widened tolerance in the transcripts' `producer` block; any
T_lo/Q_i disagreement or an `ok` mismatch stays a stop-the-line. Each leg's E is < 10⁻⁵ of its own T, and each leg carries its own E in
its own literal (D-R3), so the soundness argument is untouched. The builder did NOT run the crosscheck (step (c) is the orchestrator's).

**Row records pre-checked (21:40 IST, read-only Python on the six `batches/*-row_*.json`; UNTRUSTED, the kernel re-does it):**
C-A3 and C-A4 hold on both legs; per leg E/T = 8.6·10⁻⁶ / 6.3·10⁻⁶ / 1.4·10⁻⁷ (mp), 8.8·10⁻⁶ / 7.1·10⁻⁶ / 1.7·10⁻⁷ (Arb); cross-leg
|T_lo(mp) − T_lo(Arb)|/T_lo = 3.9·10⁻⁷⁹ / 4.2·10⁻⁷⁹ / 2.8·10⁻⁸⁰ (P-11's rtol 10⁻⁹ on T passes with 70 digits to spare). mp integers at
K = 10²⁴: T = 12023114801271919081297 / 12022114003010781117361 / 154429052431451108544607, E = 103072920877602897 / 75688809572996497 /
21290798704178334; Arb at K = 10¹²: T = 12023114801 / 12022114003 / 154429052431, E = 105892 / 85041 / 26856. `asym-arb.json` (assembled
21:36:43) carries format `M2a-barrier-transcript` 1.0, kind `asymptotic`, the trust label, K/t0/y0/yA, the 3 rows, the tail
{N1 5141000, Q1 1780738683686, Q2 178607231320, Q3 18638466998, Q4 19014989007, E1 1823} and the `producer` block; a Python pre-check of
C-A1…C-A6 on its integers is all-true (first Nlo = 630783 = L-A1's constant; windows = 4 510 217).

**Provenance of the producer patch.** The pre-F-3 `p9_mp.py` / `p9_arb.py` are byte-identical to their copies at git commit `6161fc2`
(Session 19 auto-commit 20:59 IST; repo root `…/Math/riemann`, in-repo path `rh-program/results/d1-m2a/lane-a/`); the patched files were
auto-committed at `af6a336` (21:39). `f3-patch.diff` is the exact difference. `apply_f3.py` (scratchpad, session-local) is reproduced by
the diff; nothing else was changed in either producer.

**Thermal-guard defect found and fixed (21:43 IST).** On this Mac the legs run as `/Library/Developer/CommandLineTools/…/Python p9_mp.py …`
(capital P), so `pgrep -fl 'python3|lake'` — the guard in the first version of `launch_producers.sh`, and the BRIEF's own
`pgrep -fl "python|arb|lake"` — does NOT see the mp leg (the Arb leg is caught only through the substring `arb`). The heavy-job counts
reported above were taken from `ps … | grep -E "run_leg.sh|p9_mp.py|p9_arb.py"` and are correct (2 during rows, 1 during the mp tail);
a case-insensitive name pattern turned out noisy too (the status line spawns short-lived `Python` processes; `lake` matches other
names), so the launcher's guard now counts processes above 50 % CPU (`ps -axo pcpu=,command= | awk '$1 > 50'`), lists them in
`producers.log`, and refuses above 2 — verified to read exactly 1 (the mp tail) while it ran. Recommendation for the brief's
checklist: judge "heavy" by CPU (`ps -axo pcpu=,command= | awk '$1 > 50'`), not by the name `python`.

**Final verification (2026-09-09 21:44:37 IST).** mp leg: == mp done Wed Sep  9 21:43:55 IST 2026; producer processes remaining: none; heavy jobs now: 0.
* mp tail (`batches/mp-tail.json`, 404.3 s wall incl. `--direct` 403.6 s): Q₁…Q₄, E₁ = 1780738683685954234282109 / 178607231319632698856344 / 18638466997109653259291 / 19014989006495801050358 / 1822923348119831 at K = 10²⁴, sum 1996999372832115735567933 < 2K (margin (2K − Σ)/K = 3.000627e-03), (S1)–(S4) {'S1': True, 'S2': True, 'S3': True, 'S4': True}, `--direct` contained = True, ok = True.
  - cross-leg Q1: |mp − Arb|/mp = 7.43e-82
  - cross-leg Q2: |mp − Arb|/mp = 2.50e-81
  - cross-leg Q3: |mp − Arb|/mp = 3.97e-81
  - cross-leg Q4: |mp − Arb|/mp = 4.92e-81
  - cross-leg E1 (hull bounds): Arb/mp = 1.000000
* `asym-mp.json` assembled (2026-09-09 21:43:55 IST): kind asymptotic, K = 1000000000000000000000000, rows [('630783', '746495'), ('746496', '1469440'), ('1469441', '5140999')], tail N1 = 5141000, producer rows ok = [True, True, True], tail ok = True.
  - Python pre-check C-A1…C-A6 on the mp literal (UNTRUSTED; the kernel re-does it): [True, True, True, True, True, True].
* `STATUS.json` top level: phase = "arb:tail-done mp:tail-done", windows_done/total = 4510217/4510217, started 2026-09-09 21:36:29 IST, updated 2026-09-09 21:43:55 IST, eta_hours = 0.0, errors = []; per leg: mp tail-done (rows 3/3), arb tail-done (rows 3/3).
* Both legs' transcripts are on disk (`asym-mp.json`, `asym-arb.json`) with every per-row/tail record under `batches/`. Next (orchestrator, PLAN §4 phase 3 (c)–(d)): `python3 crosscheck_lane_a.py .` (expect the F-2 E-ratio trip on the wide rows — see above — then `--etol` above the observed maximum), emit the two literal modules, back-parse, `lake build`, replace `hLaneA` per PLAN §1.5, `#print axioms`, F-5 bookkeeping, Opus audit.

**[DATED CORRECTION 2026-09-09 22:25 IST, phase-3(d) fix pass (AUDIT-3d.md A-2).]** The line "cross-leg E1 (hull bounds): Arb/mp = 1.000000"
in the final-verification block above does not describe the E₁ bounds as written: E₁ = 1823 at K = 10¹² (Arb) against
1822923348119831 at K = 10²⁴ (mp) gives Arb/mp = 1.0000420 (`crosscheck-full.txt`: rel 4.3·10⁻⁸, larger: arb; `backparse.log`:
1.000042). 1.000000 would be right only for the two ceilings taken at the same K = 10¹² (⌈1822.92…⌉ = 1823 = 1823). The
emitter's module headers had copied the figure; they were corrected in the same pass (`EMIT-NOTES.md` §9). Nothing else in
this file is affected. The line above is kept as the record.
