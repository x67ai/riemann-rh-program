# D1 M2a Lane A — EMIT-NOTES (phase 3(d), Job 1: the emitter)

**Stamp:** 2026-09-09 21:51–22:05 IST, machine clock (Session 19; brief `BRIEF-3d.md`, written 21:47). Authorities read in
the brief's order: `PLAN.md` §1.5 (followed character for character) and §2.4; `PLAN-REVIEW.md` §6 and F-5; `BUILD-NOTES.md`;
`SPEC.md` §3.7, §7.6, §8.3; `v11/GLUE-NOTES.md`; `v11/AUDIT.md` R-1; `emit_lean_m2a.py`, `verify_lean_m2a.py`, the three leg
notes; `KICKSTART.md` Part 2 item 10(f)/(i)/(j). Trust vocabulary unchanged and binding: the producers are UNTRUSTED; the
kernel checks integer relations only; H2-A and H-TAIL stay DISPLAYED; never "fully machine-checked". U.S. English.

**Verdict: DONE.** Every proof closes; nothing is left out; no `sorry` anywhere; nothing owed from this job (§8).

## 1. What was done, in the brief's order

| item | result | record |
|---|---|---|
| 1 emitter | `lane-a/emit_lean_lane_a.py` (model `emit_lean_m2a.py`): `Zeta23/DBN/Instance02/Asym_mp.lean` (8 093 bytes, 117 lines) and `Asym_arb.lean` (7 956 bytes, 117 lines), each with the literal `row2AsymMP` / `row2AsymARB : AsymData` — 25 integers, the JSON's decimal strings written VERBATIM (no arithmetic; re-validated canonical), K as written (10²⁴ / 10¹²), N_start 630783, N₁ 5141000 — the kernel fact `row2Asym*_check : checkAsym row2Asym* = true := by decide +kernel`, the three `simp` facts `row2Asym*_t0/_y0/_yA`, and the glue lemma `row2_laneA_mp` / `row2_laneA_arb` exactly as PLAN §1.5 (conclusion character for character the type of the former `hLaneA`; the layout of `hyA`'s proof is the builder's verified scratch form). Header in the style of the Instance02 literal modules, carrying the transcript block (rows, tail, the cross-check's E hull ratios 1.027 / 1.124 / 1.261, Arb larger, recorded not gated), what the kernel checks, what it does NOT use (F-6), what the replacement buys (PLAN-REVIEW §6, y-band asymmetry stated), the SPEC §3.7 label. The emitter refuses (exits, emits nothing) on a non-asymptotic transcript, a non-canonical integer, parameters other than the instance's t₀/y₀/yA, a first Nlo ≠ 630783, N₁ ≠ 5141000, or an UNTRUSTED Python pre-check failure of C-A1…C-A6. Output is deterministic (the only stamp is the producer's, copied from the JSON). | `emit_lean_lane_a.py`; the two modules |
| 2 back-parse | `lane-a/backparse_lane_a.py` (regex only, no code shared with the emitter): both modules parsed back and compared with `asym-{mp,arb}.json` — **50 integers exact, 0 mismatches**; the kernel theorem text, the three parameter facts, the glue lemma's binders, its conclusion (verbatim the former `hLaneA` type), its pinned first row (= the literal's first row) and its three rewrite steps all present unaltered; no trust word in code. Cross-leg (where the legs must agree, never merged): window ranges and N₁ identical; T/K rel diff 2.3·10⁻¹¹ / 9.0·10⁻¹³ / 2.9·10⁻¹² and Q₁…Q₄/K ≤ 4.8·10⁻¹¹ (the K-scale rounding; the producers' own T_lo agree to 10⁻⁷⁹, `crosscheck-full.txt`); E/K Arb/mp = 1.0274 / 1.1236 / 1.2614, E₁ 1.000042 — hull bounds, recorded. Exit 0. | `backparse.log` |
| 3 builds | `lake build Zeta23.DBN.Instance02.Asym_mp`: `Built … (1.9s)`, 3.18 s wall, RSS 3.03 GB; `…Asym_arb`: `Built … (1.4s)`, 2.53 s wall. Zero warnings, zero errors. **Wall time of each `decide +kernel`** (Lean profiler, threshold 0, re-elaborated on the built literals in `asym-literal-kernel-time.lean`): kernel type checking **2.02 ms (mp) and 4.1 ms (Arb)**, elaboration ≤ 0.6 ms, the whole scratch 2.05 s wall (import loading). Both `[propext]`. | `asym-literal-build.log`, `asym-literal-kernel-time.{lean,log}` |
| 4 `hLaneA` replaced | `Instance02.lean`, exactly PLAN §1.5 — code changes and nothing else in code: 2 imports (`Zeta23.DBN.Instance02.Asym_mp`, `…Asym_arb`); in `row2_ray_mp`, `row2_ray_arb`, `lambda_le_point2`, `lambda_le_point2_arb` the binder `(hLaneA : …)` → the pair `(hAsym : AsymEnclOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) row2AsymMP)` `(hTail : TailOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) row2AsymMP)` (ARB in the two Arb theorems — each leg pairs its own Lane A literal with its own Lane B literal, D-R3); the consumption token `hLaneA ?_` → `(row2_laneA_mp hAsym hTail) ?_` / `(row2_laneA_arb hAsym hTail) ?_`; the two `lambda_le_point2*` bodies pass `hAsym hTail` where they passed `hLaneA`. `hLaneA` no longer occurs in code. Documentation in the same file updated to match (the header's hypothesis list and label; the four theorem docstrings), with the 2026-09-06 state kept as a dated record — see §3. Nothing else in the tree changed (`Asym.lean`, `Defs.lean`, `BarrierCert.lean`, `BtFacts.lean`, the 114 Lane B modules, `Zeta23.lean`: untouched, `cmp`-verified against the mirror). | `instance02-replacement.diff` (197 lines, `diff -u` against the mirror = git HEAD) |
| 5 root build, axioms, trust | `lake build Zeta23`: `Built Zeta23.DBN.Instance02 (1.7s)`, `Built Zeta23 (11s)`, **Build completed successfully (9142 jobs)**, 15.83 s wall; no warning or error in any DBN file (the replayed warnings are upstream `XiPrime/` files, pre-existing). `#print axioms` on the eight names: `lambda_le_point2`, `lambda_le_point2_arb`, `row2_ray_mp`, `row2_ray_arb`, `row2_laneA_mp`, `row2_laneA_arb` → **[propext, Classical.choice, Quot.sound]**; `row2AsymMP_check`, `row2AsymARB_check` → **[propext]**. The `#check` of the six theorems is in the same log: the four instance theorems display exactly `ZeroVerification …` (H1), `BarrierEnclOK … row2Barrier*` (H2-B), `AsymEnclOK … row2Asym*` (`hAsym`), `TailOK … row2Asym*` (`hTail`), `Polymath15Bridge' ∧ HtEntire` (H3) → the conclusion, and nothing else. Trust greps over `Zeta23/DBN/` (121 files; `axiom`, `native_decide`, `unsafe`, `implemented_by`, `extern`, `opaque`, `sorry`): **0 hits in code**; the 116 `native_decide` and 3 `sorry` word hits are header prose ("no `native_decide`", "sorry-free"), `axiom` 0. | `final-axioms.log`, `final-axioms-scratch.lean`, `trust-greps.log` |
| 6 F-5 bookkeeping | Dated blocks appended, nothing deleted (§4): `lean/README.md` (a dated note after the R-1 label paragraph — licensed with SPEC §3.7's gloss, PLAN-REVIEW §6 quoted verbatim from the file — plus a new section "M2a Lane A (2026-09-09)", a table row for the three new files, a dated sentence in the opening paragraph, the Licensing count); `v11/GLUE-NOTES.md` (a dated H2-A/H-TAIL row after the input table's H2-A row, a dated honest-label block after the R-1 block, "Left for the Lane A stream" → STATUS: DONE); `RUN-REPORT.md` §6 (a dated note after the Session-16 note: item 3 DONE, item 4's short sentence licensed with the §3.7 gloss, the cut line moves to item 5). The label, verbatim, in all three: **"kernel-checked modulo H1, H2 (H2-B, H2-A, H-TAIL), H3"** — never "fully machine-checked"; the y-band asymmetry and the C-A6 not-consumed fact are stated in each. | `git diff` of the three files |
| 7 mirror + notes | `rh-program/lean/Zeta23/DBN/Instance02.lean`, `Instance02/Asym_mp.lean`, `Instance02/Asym_arb.lean` copied from the tree, `cmp`-verified byte-identical (§5); `Asym.lean` was already mirrored by the builder and is still identical. This file. | §5 |

## 2. Every path

Lean tree (`~/rh-lean-work/zeta-23-lean-main`): NEW `Zeta23/DBN/Instance02/Asym_mp.lean`, NEW `Zeta23/DBN/Instance02/Asym_arb.lean`,
MODIFIED `Zeta23/DBN/Instance02.lean`. Nothing else.

Mirror (`rh-program/lean/Zeta23/DBN/`): the same three files, byte-identical.

This directory (`rh-program/results/d1-m2a/lane-a/`): `emit_lean_lane_a.py`, `backparse_lane_a.py`, `backparse.log`,
`asym-literal-build.log` (the two module builds + the root build), `asym-literal-kernel-time.lean` + `.log`,
`instance02-replacement.diff`, `final-axioms-scratch.lean` + `final-axioms.log`, `trust-greps.log`, `EMIT-NOTES.md` (this).

Bookkeeping (F-5): `rh-program/lean/README.md`, `rh-program/results/d1-m2a/v11/GLUE-NOTES.md`, `rh-program/results/d1-m2a/RUN-REPORT.md`.

Session-local (scratchpad, not in the repo; reproduced exactly by the diffs): `patch_instance02.py` (the exact-match
replacement script, every pattern asserted once per theorem block), `bookkeeping_f5.py` (the F-5 anchors),
`Instance02.lean.pre-3d.bak` (= the mirror = git HEAD, `cmp`-verified before patching).

## 3. The `Instance02.lean` change, precisely (for the auditor's diff)

**Code (comments stripped on both sides — the whole code diff is these 8 hunks):**

    +import Zeta23.DBN.Instance02.Asym_mp
    +import Zeta23.DBN.Instance02.Asym_arb
    row2_ray_mp:        binder hLaneA → (hAsym … row2AsymMP) (hTail … row2AsymMP);  hLaneA ?_ → (row2_laneA_mp hAsym hTail) ?_
    row2_ray_arb:       binder hLaneA → (hAsym … row2AsymARB) (hTail … row2AsymARB); hLaneA ?_ → (row2_laneA_arb hAsym hTail) ?_
    lambda_le_point2:   binder hLaneA → the MP pair;  exact row2_ray_mp hH1 hEncl hLaneA hH3 … → … hH1 hEncl hAsym hTail hH3 …
    lambda_le_point2_arb: binder hLaneA → the ARB pair; exact row2_ray_arb … hLaneA … → … hAsym hTail …

**Documentation in the same file (the rest of the 197-line diff):** the header's opening sentence (a dated "since
2026-09-09" clause), a LANE A transcript block after the Lane B one, the §2 hypothesis list (`hAsym`, `hTail` in place of
`hLaneA`, with (ii′) = `row2_laneA_* hAsym hTail`), the "WHAT IS DISPLAYED" block rewritten to the SPEC §3.7 label with
PLAN-REVIEW §6's three facts stated (window range = floor enclosure + kernel-checked coverage; `TailOK` the only displayed
nonvanishing conclusion, y-band 9.0·10⁻⁸ wider [figure corrected in the fix pass, §9; the first pass wrote "1.5·10⁻⁷", the squares gap]; C-A6 kernel-checked, not consumed) and the 2026-09-06 `hLaneA` state kept
as a DATED RECORD (superseded, not deleted); the four theorem docstrings updated to name `hAsym`/`hTail`. Rationale: a
trusted file whose header said "`hLaneA` … not yet run" next to theorems that no longer have `hLaneA` would be a false
label (D-R3/D-R8); the header itself foresaw "the theorem statement changes accordingly".

## 4. The label (verbatim, and what it may and may not say)

"kernel-checked modulo H1, H2 (H2-B, H2-A, H-TAIL), H3" — SPEC §3.7, with its gloss (H2 = the conjunction of three
producer-certified enclosure-type Props behind the kernel-checked checkers; "three displayed hypotheses" only with that
gloss). Never "fully machine-checked". RUN-REPORT §6 item 4's shorter sentence is now licensed with that gloss (R-1's
condition — item 3 landing — is met; R-1 is discharged, not reversed). Stated, not glossed, in every file touched:
(i) the window range N ∈ [630 783, 5 140 999] is a displayed floor-enclosure hypothesis plus kernel-checked coverage, no
longer a displayed nonvanishing claim; (ii) the displayed nonvanishing conclusion that remains is `TailOK` on N ≥ 5 141 000
with the y-band [y₀, yA], yA = 0.7924646 being 9.0·10⁻⁸ wider than √(157/250) = 0.79246451… (yA − √(157/250) = 8.975·10⁻⁸;
in the squares yA² − 157/250 = 1.42·10⁻⁷ — corrected in the fix pass, §9; the glue derives y ≤ yA from
y² ≤ 157/250; `TailOK` is "the tail region N ≥ N₁, y ∈ [y₀, yA]", not "part of what `hLaneA` said"); (iii) C-A6 is
kernel-checked on both literals but not consumed by any proof (F-6) — the tail reduction is prose. Λ ≤ 0.2 is not proved;
the bracket of record stays 0 ≤ Λ ≤ 0.2.

## 5. SHA-256 (KICKSTART 10(i); tree = mirror, verified)

**Pass 1 (21:51–22:05 IST) — SUPERSEDED at 22:27 IST by the fix pass (§9); kept as the record. These are the hashes the
auditor verified in AUDIT-3d.md check 10.**

    128eb3101c30032080e6ecdde79aee6af04de50a21111e6bf99f3c405ad7ac05  Zeta23/DBN/Instance02/Asym_mp.lean     (pass 1)
    767ee5000f358e1bb661efb282b46f0a6cc3fd4f201afc73d70bf41d27981987  Zeta23/DBN/Instance02/Asym_arb.lean    (pass 1)
    bcf81f5e179e14b12d4ddcc85cb970fef5a5cc6f048136bb9443f1fce7cf9850  Zeta23/DBN/Instance02.lean             (pass 1)
    de67acf7bc7e9653837f811f4df56f363da7151e1995a958a1e87494eb136ff2  lane-a/emit_lean_lane_a.py             (pass 1)

**Current (fix pass r2, 22:27 IST; tree = mirror, `cmp`-verified):**

    609e55f223331e4c99554853792a7e7fa97b752f6c2872481de68b289449512a  Zeta23/DBN/Instance02/Asym_mp.lean     (8339 bytes, 120 lines)
    d669fc31b1908b8db1688f1d0b87d7118541fef4a3806644c835212af6a44740  Zeta23/DBN/Instance02/Asym_arb.lean    (8202 bytes, 120 lines)
    810ee7d8d9c73c2cc320b7147bf5ecbc9aae3821884076a06cc65092aa1ca4de  Zeta23/DBN/Instance02.lean             (267 lines)
    c970ac26254c6ec22b690543395e172db1e75e272d07ab4421b711fae26b2f63  Zeta23/DBN/Asym.lean          (builder's, unchanged in both passes)
    7a99eedb4f09cdc4d992238ca16fe51be6a33e27ab05a0369faf9182bc573b85  lane-a/asym-mp.json           (input, untouched)
    b7d1a7824bb996c007cefeba48af53816bfaa14ff5271563f749538d3ce2819e  lane-a/asym-arb.json          (input, untouched)
    96bca54ae90180ea6eb437bfcd0c5523ce3ac852073bf57e29801f44501271d6  lane-a/emit_lean_lane_a.py    (template corrected, §9)
    645a82ec9b54e6882eb79d926ef24d4b65368e19656cb64a6b349befdae9ca51  lane-a/backparse_lane_a.py    (unchanged)

(The emitter is deterministic: re-running it on the same JSON reproduces the two current module hashes.)

## 6. Wall times, collected

| step | wall | note |
|---|---|---|
| emit (both legs) | < 0.1 s | Python |
| back-parse (both legs + cross-leg) | < 0.1 s | Python, exit 0 |
| `lake build …Asym_mp` | 3.18 s (module 1.9 s) | RSS 3.03 GB (import loading) |
| `lake build …Asym_arb` | 2.53 s (module 1.4 s) | |
| `decide +kernel` on `row2AsymMP` / `row2AsymARB` | **2.02 ms / 4.1 ms** kernel type checking | profiler, `asym-literal-kernel-time.log`; scratch 2.05 s wall incl. imports |
| `lake build Zeta23` (root, after the replacement) | 15.83 s (Instance02 1.7 s, root 11 s) | 9142 jobs, RSS 5.9 GB, no DBN warnings |
| `#print axioms` scratch | 2.23 s | |
| whole job, brief to notes | ≈ 14 min | 21:51–22:05 IST |

Thermal: one `lake` process at a time throughout (the two module builds and the root build were sequential; the two
`lake env lean` scratches ran alone); no producer ran; heavy jobs (> 50 % CPU) before/after each build: 0; `caffeinate`
running; the push and autocommit watchdogs running (`pgrep -f watchdog.sh` → 2).

## 7. Reproduction

    cd "…/rh-program/results/d1-m2a/lane-a"
    python3 emit_lean_lane_a.py asym-mp.json  ~/rh-lean-work/zeta-23-lean-main mp
    python3 emit_lean_lane_a.py asym-arb.json ~/rh-lean-work/zeta-23-lean-main arb
    python3 backparse_lane_a.py ~/rh-lean-work/zeta-23-lean-main asym-mp.json asym-arb.json      # exit 0 required
    (cd ~/rh-lean-work/zeta-23-lean-main && lake build Zeta23.DBN.Instance02.Asym_mp && lake build Zeta23.DBN.Instance02.Asym_arb && lake build Zeta23)
    (cd ~/rh-lean-work/zeta-23-lean-main && lake env lean "$PWD_LANEA/final-axioms-scratch.lean")

## 8. Owed / not done

Nothing is owed from Job 1: every proof closed (no proof left out, no `sorry`), every deliverable of the brief is on disk.
Not in this job's scope, for the orchestrator: the Opus audit (Job 2, `AUDIT-3d.md`), the commit/LOG.md hash entry (the
autocommit watchdog will pick the files up; the SHA-256s above are for LOG.md), STATUS.md, and RUN-REPORT §6 item 5
(packaging) which is now the cut line.

## 9. FIX PASS (r2) after AUDIT-3d.md — dated block, 2026-09-09 22:20–22:30 IST, machine clock

**Trigger.** The auditor (Job 2) returned FIX-FIRST: everything trust-critical OK and reproduced; two documentation-accuracy
defects, both numeric, both in trusted files. I verified each independently before editing anything (exact arithmetic,
Python `decimal` at 60 digits and `fractions`), then applied them. Nothing was rejected.

| item | verification | decision |
|---|---|---|
| **A-1** — the y-band figure | yA − √(157/250) = 0.7924646 − 0.79246451024635797… = **8.975364·10⁻⁸ ≈ 9.0·10⁻⁸**; the squares gap yA² − 157/250 = 3556329/(25·10¹²) = 1.4225316·10⁻⁷; ratio 1.585. Pass 1 wrote the squares gap as the y gap, contradicting the two decimals printed beside it. | **APPLIED.** The sentence now gives the y gap (9.0·10⁻⁸) and, in a parenthesis, the exact squares gap, in every place in the corpus's own voice (the auditor's list of eight, plus the emitter template it came from). |
| **A-2** — E₁ Arb/mp | 1823/(1822923348119831/10¹²) = **1.0000420488…**; `crosscheck-full.txt` rel 4.3·10⁻⁸ (larger: arb), `backparse.log` 1.000042. Pass 1's headers said 1.000000, copied from BUILD-NOTES' final-verification line. | **APPLIED** in both module headers (via the template), in `lean/README.md` line 195 (an occurrence the audit did not list), and a dated correction appended to `BUILD-NOTES.md` (the builder's line kept). |
| AUDIT §4 — F-6 note "understates how little is consumed" | Read in `Asym.lean` 189–197: the single `obtain` names `hK`, `hrows`, `hcons`, `hN1`; per row `obtain ⟨⟨-, -⟩, hET⟩` keeps only `E < T`; `cover_of_consecutive d.rows r hr hcons …` takes C-A4. Confirmed. | Not a fix request; **applied anyway as one clause** in the modules' "WHAT THE KERNEL DOES NOT USE" paragraph ("and of C-A3 only E < T per row (Nlo ≤ Nhi and 0 ≤ E are checked, then discarded; the coverage step uses C-A4 through `cover_of_consecutive` and C-A5)"), so the honesty note is exact rather than merely safe. Comment only; `Asym.lean`'s own paragraph is the builder's, not wrong, and was left alone. |

**What changed — text only. No code, no integer, no theorem statement, no proof, no import moved.**

* `emit_lean_lane_a.py`: three template edits (the F-6 clause, the A-1 sentence, the A-2 figure); both modules **regenerated
  from it** (not hand-edited), so the emitter still reproduces the module hashes. `diff` pass 1 → r2 per module: exactly the
  three header hunks; 117 → 120 lines; 8093 → 8339 bytes (mp), 7956 → 8202 (Arb). Record: `fixes-3d-r2.diff`.
* `Instance02.lean` header lines 72–73 (A-1); 266 → 267 lines. `instance02-replacement-r2.diff` (git `5a4b06b` → r2, 198 lines)
  supersedes `instance02-replacement.diff` (pass 1, kept); the code hunks are identical.
* `PLAN-REVIEW.md` §6: a dated correction appended under the third bullet; the bullet itself untouched (the source of the quote).
* `lean/README.md`: the verbatim block quote of §6 now carries the source's dated correction (so it still follows its source);
  E₁ 1.000000 → 1.000042; the "what the kernel does not use" paragraph's figure + a bracketed dated note; line counts 117 → 120
  (two places); the three SHA-256s (pass-1 values pointed to §5 here).
* `v11/GLUE-NOTES.md`, `RUN-REPORT.md` §6: the figure, plus a bracketed dated correction note at the end of the same paragraph.
* This file: §1 item-6 and §4 figures corrected with bracketed notes; §5 restructured (pass 1 kept as superseded); this §9.
* `BUILD-NOTES.md`: a dated correction appended (A-2's origin); nothing of the builder's removed.
* **Not edited:** `AUDIT-3d.md` (the auditor's), `BRIEF-3d.md` (the orchestrator's; it inherits the figure from PLAN-REVIEW §6,
  now corrected at the source), `instance02-replacement.diff` (pass-1 record), `Asym.lean`, the two JSON inputs, `Zeta23.lean`.

**Re-verification after the edits (all on disk).**

| check | result | record |
|---|---|---|
| back-parse, re-run on the regenerated modules | 50 integers exact, 0 mismatches, cross-leg 0, exit 0; identical to `backparse.log` except the stamps and the two byte counts | `backparse-r2.log` |
| `lake build Zeta23` (root; one lake process, no producers, heavy jobs 0 before and after) | `Built …Asym_mp (1.6s)`, `…Asym_arb (1.6s)`, `…Instance02 (1.5s)`, `Built Zeta23 (10s)`, **Build completed successfully (9142 jobs)**, 16.04 s wall, RSS 5.9 GB, no warning or error in any DBN file | `asym-literal-build-r2.log` |
| `#print axioms` on the eight names + the six `#check`s (the same scratch) | **identical to `final-axioms.log`** line for line (only the timing lines differ): six theorems `[propext, Classical.choice, Quot.sound]`, two kernel facts `[propext]`; the four instance theorems still display exactly H1, H2-B, `hAsym`, `hTail`, H3; 2.45 s wall | `final-axioms-r2.log` |
| trust greps, raw and CODE-ONLY (comments stripped, nested blocks handled; eleven patterns incl. `hLaneA`, `ofReduceBool`, `trust_me`, `lean_evalConst`; 121 files) | raw prose counts unchanged (axiom 0, native_decide 116, sorry 3, hLaneA 12); **code hits 0** for every pattern | `trust-greps-r2.log` |
| mirror | the three files re-copied to `rh-program/lean/Zeta23/DBN/`, `cmp`-identical; `Asym.lean` untouched and identical | §5 |
| leftover figures | `1.5·10⁻⁷` survives only inside quotations of the old wording and in correction notes (README 179 = the quoted bullet, followed by its correction; PLAN-REVIEW 170 = the bullet; the pass-1 diff; AUDIT-3d.md; BRIEF-3d.md); `1.000000` only in BUILD-NOTES' kept line, its correction, and AUDIT-3d.md | `grep -rn` at the end of the pass |

**Wall times:** emit < 0.1 s (both legs); back-parse < 0.1 s; root build 16.04 s; axioms scratch 2.45 s; whole pass ≈ 13 min.
Thermal: `caffeinate` and both watchdogs running throughout; one `lake` at a time; no producer ran.

**Owed:** nothing from the emitter. For the orchestrator: the commit / LOG.md hash entry (the autocommit watchdog picks the
files up; the current hashes are in §5), STATUS.md, and — if wanted — an Opus re-check of this pass, which needs only
`fixes-3d-r2.diff`, `final-axioms-r2.log` against `final-axioms.log`, and the §5 hashes.
