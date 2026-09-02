# AUDIT — the reconciled, binding audit of D1 M1 v1 (Session 14, 2026-09-02)

**Reconciler:** the D1 reconciliation agent (Fable 5.1), run `d1-audit-m2a-s14` (wf_135a6ecf-327).
**Inputs:** `AUDIT-F.md` (auditor F, Fable 5.1; 0 FATAL / 2 MAJOR / 6 MINOR) and `AUDIT-O.md`
(auditor O, Opus 5; 0 FATAL / 2 MAJOR / 6 MINOR / 3 INFO), written independently of each other.
**Protocol (binding):** every FATAL or MAJOR finding of either auditor was RE-VERIFIED by the
reconciler before being accepted — by re-running the auditor's script or the reconciler's own —
and the one disagreement between the auditors was settled by computation, not by vote. Small,
verified repairs were APPLIED and the affected validation re-run (before/after on disk); large
defects are DEMANDED with a cost. A first pass of this reconciliation (same run, earlier in the
session) applied repairs R1, R2 and O MINOR-1/-2 and died on the usage limit before writing this
file; its logs (`recon_*.log`) were re-checked and, where the re-run is cheap, re-run here.
**Trust vocabulary (binding, D-R3/D-R8):** producers are untrusted by design; the Lean side is
"kernel-checked modulo the displayed hypotheses H-ENCL and H-AP"; nothing is "fully
machine-checked". The Λ bracket of record is 0 ≤ Λ ≤ 0.2 (Platt–Trudgian Cor. 2); "Λ < 0.2" is
never written.

## 0. Verdict for the gate

**REPAIRED-CLEAN. 0 FATAL. Four MAJOR findings (two per auditor, one pair overlapping), all
re-verified, all APPLIED. Every MINOR either APPLIED or recorded as documentation. Two items
OVERRULED (one attribution, one optional clause). Four large items DEMANDED for M2a with costs.**
M2a may proceed. The constraints it inherits are listed in §4 and in `RUN-REPORT.md` §5–§6.

Both auditors agree on the substance: no bound in the mp leg is non-rigorous *as derived*
(Euler–Maclaurin remainder re-derived twice independently and matched to the code line by line;
C_{2m+2} certified by exact rational interval Horner, ratio 2.0247 to |B₃₀| paid not assumed); the
DH κ = tan θ constant is right (two independent recomputations, 10⁻⁶¹–10⁻¹⁴¹ agreement); every
fresh-seed enclosure test passed (F: 1 088 + 150 checks; O: 395 + 1 640 + ~5 200 boundary samples;
0 violations in all); the winding geometry (C6 ⟹ half-plane ⟹ |Δ| < π; C8 + C9 ⟹ Z = m)
re-derives correct and is machine-checked where it matters; 90 (F) and 90 (O) hand-corruptions
are rejected at the intended clause by both Python checkers, and 30 (F) / 8 (O) again by the
kernel; the Lean layer builds, is `sorry`-free and `native_decide`-free, and `#print axioms` on
`cert_of_checkW1` and `floor_of_checkW1Floor` gives `propext, Classical.choice, Quot.sound`
only; the DH live fire is a real true positive (winding 1 recomputed from scratch by both
auditors, three ways by F); every number in `acceptance-report.md` and `cost-curve.json` matches
the artifacts except one ratio (F-4). The MAJORs are (i) a false platform premise in the mp leg,
(ii) a producer bug on a non-default path, (iii) a coverage gap in the Lean evidence, and (iv) a
build limit on large data literals — none a soundness hole in the format, the checker, or the
theorem.

## 1. Per-finding table

| id | auditor | severity (filed → reconciled) | finding (one line) | reconciler's verification | repair | status |
|---|---|---|---|---|---|---|
| **F-1** | F | MAJOR → **MAJOR** | mpmath 1.3.0 `iv` transcendental primitives (exp/log/atan/pi) directed-round a guard-bit APPROXIMATION and are not enclosures: `mpf_exp(x, 288, round_ceiling)` fell below the truth in 11/40 000 samples; `ball.py`'s stated premise "every endpoint computed with directed rounding" was false | **Reproduced twice** (prior pass and this one): `recon_rounding.py` re-run this pass is byte-identical to `recon_rounding.log` modulo timing — RAW: exp 7 + 4 violations in 40 000 (worst 6.6·10⁻⁹¹ relative = 3.3·10⁻⁴ ulp), log/atan/sqrt/pi 0; mpmath's own perturbed `mpi_cos_sin` 0 in 50 000 incl. the cancellation regimes x ≈ (k+½)π, kπ; REPAIRED wrappers 0 violations in 92 000 exact prec-1200 comparisons. Read `libmpi.py` 273–303 and `mpi_cos_sin` (perturbation at wp+10 only for cos/sin) — F's mechanism is as filed. Grade: MAJOR upheld, not FATAL — the bound (RB) and every identity are rigorous; the Arb leg is independent and rigorous by construction; emitted transcripts provably unaffected (`audit_F_slack.log`: min slack ≥ 4.2·10⁻³/K vs error < 10⁻⁵⁰/K) and confirmed byte-identical on re-emission (below) | **R1 APPLIED** (prior pass, re-verified): `ball.py::_inflate` — outward relative widening by 2⁻⁽ᵖʳᵉᶜ⁻¹⁶⁾ of every transcendental endpoint (mpmath's own `mpi_cos_sin` recipe with a 2¹⁵-ulp margin); wrappers `iv_exp/iv_log/iv_atan/iv_pi/iv_cos/iv_sin` at all six call sites (`Ball.exp`, `Ball.log`, `arg_branch`, `zeta_encl._log_int`, both remainder pads, `producer_mp.argument_rows`); docstring and `mp-leg-notes.md` §3 corrected to the weak, tested assumption; selftest regression block (exact prec-1200 references + strict-widening property). After: `ball.py --selftest` 18 469 checks / 0 failures; `zeta_encl --validate` 100/100; `hurwitz_encl --validate` 60/60; `producer_mp --selftest-dh` 24/24 (`recon_selftests_after.log`); all five mp acceptance transcripts re-produced with numeric content byte-identical to Session 8 (`recon_mp_reproduce.log`; t = 10⁴: `recon_mp_reproduce_t10000.log`) | **APPLIED** |
| **F-2** | F | MAJOR → **MAJOR** | `producer_mp.py`'s D3 clamp to ±⌊A/2⌋ is unsound for odd A; `--A 0` (A = 1) EMITS a checker-ACCEPTED m = 0 exclusion transcript for the DH rectangle, which contains a zero — a false certificate (false H-ENCL(b); checker and format sound). `producer_arb.py` guards `A % 2 == 0`; `producer_mp.py` did not | **Reproduced this pass from the pre-repair code** (`git 5a7a32f` extracted to scratch): `recon_F2_before.log` — 40 rows all [0, 0], S = [0, 0], m = 0, `checker_ref.py` ACCEPT (C1–C11) and `reference_checker.py` ACCEPT. Mechanism confirmed by reading lines 280–281 of the old file: for odd A the integer clamp bounds lie strictly inside (−A/2, A/2) | **R2 APPLIED** (prior pass): `require_even_A` in `produce` and `argument_rows`, `--A` help text; **R5 APPLIED** (this pass): FORMAT §1 "A MUST be even and ≥ 2" (producer requirement), §6.1, §10. After: `recon_F2_after.log` — A = 1 refused with `PRODUCER STOP`, A = 100 accepted end-to-end. The optional "add `A % 2 = 0` to C1 in both checkers and Lean" is NOT applied — it would be a contract version bump and the checker is sound for every A ≥ 1 (only producers clamp) | **APPLIED** |
| **O MAJOR-1** (= F-6) | O (F filed the same fact as MINOR F-6) | MAJOR / MINOR → **MAJOR** (coverage; closed) | The Lean checker had never been run on a producer-emitted transcript: the acceptance report's "both checkers" are the two Python checkers; the JSON→Lean emitter FORMAT §10 names did not exist. No dishonesty (the report's §6 says so) — a coverage gap in the deliverable's central claim | Both auditors wrote emitters and kernel-ran the data (F: 10 accepted + 30 corrupted; O: 10 + 2 + 8, plus an 800 + 379-case differential fuzz and an independent back-parse of the literals, 0 mismatches). **Reconciler:** promoted O's emitter as `emit_lean.py` (program header; `set_option maxRecDepth` written; corruption modes removed), generated `lean/Zeta23/W1/Instances.lean` (10 acceptance transcripts + 2 positive controls; 3 265 lines), `lake build Zeta23.W1.Instances` — *Build completed successfully (656 jobs)*, 13.9 s; `#print axioms`: `[propext]` ×10 (`checkW1Floor = true`), none ×2 (`checkW1 = false`); independent back-parse `recon_instances_verify.py` (O's reader): 12 instances, 2 940 rows, **0 mismatches**; copied back byte-identical; `lean/README.md` updated (`recon_lean_instances.log`) | O's repairs 1–3 **APPLIED**: `emit_lean.py` + FORMAT §13 row; `Instances.lean` as the third checker column; `acceptance-report.md` §0/§6 amended with dated wording; **F-6's R6 APPLIED** in the same edits | **APPLIED (closed)** |
| **O MAJOR-2** (vs F-3) | O; F filed the symptom as MINOR F-3 | MAJOR / MINOR → **MAJOR at reduced scope** | A Lean data module of ≳ 10³ rows does not build at the default `maxRecDepth`. **Disagreement on the cause:** F attributed it to `decide +kernel`; O (after its own first draft said the same) isolated it to the definition compiler's list literal | **Settled by computation** (`recon_lean_instances.log`, experiments A/B/B′ re-run by the reconciler on `Instances.olean`): A — `decide +kernel` alone on the imported 1 294-row def at the DEFAULT limit: succeeds (7.4 s wall incl. import; no axioms); B — the def alone, no theorem, default limit: `maximum recursion depth has been reached` at the `def` line; B′ — same def with `maxRecDepth 100000` + `decide +kernel`: succeeds. **O's rewritten diagnosis CONFIRMED; F's attribution OVERRULED; the symptom and the remedy (the option) stand as both filed** | O repair 1 **APPLIED**: the emitter writes `set_option maxRecDepth 100000`; FORMAT §7.1 build note (F's R3 folded in, with the corrected cause; `lean/README.md` likewise). O repair 2 **DEMANDED** for M2a: settle the bulk-data representation of `BarrierCertData` (chunked `def`s joined by `++`, or a compact encoding decoded inside the checker) BEFORE `BarrierCert.lean` is written — a single list literal at Gomila scale (3 149 013 rows) is not viable at any limit. Cost: a design decision plus a ~100-row experiment, days. O's withdrawn `Checker.lean` tail-recursion rewrite is NOT adopted | **APPLIED (1) / DEMANDED (2)** |
| F-3 | F | MINOR → merged into O MAJOR-2 | kernel check of the 983/1 294-row transcripts needs `maxRecDepth 100000` (passes in 11.7 s) | as above; the timing reproduces (13.9 s for the whole 12-instance module) | as above | **APPLIED** (remedy) / **OVERRULED** (cause) |
| F-4 | F | MINOR → MINOR | `acceptance-report.md` §4 "~10³–10⁴× tighter" is wrong by two orders (artifacts: 5.2·10⁵× at t100, 7.5·10⁵× at t10000, 1.25·10⁶× on DH) | Re-read from `cost-curve.json` `winding_width_turns`: 5.2·10⁻¹¹ vs 2.7·10⁻⁵ (ratio 5.2·10⁵), 1.316·10⁻⁹ vs 9.83·10⁻⁴ (7.5·10⁵), 4·10⁻¹¹ vs 5·10⁻⁵ (1.25·10⁶) — F is right | **R4 APPLIED** in place, with the dated correction note | **APPLIED** |
| F-5 | F | MINOR → MINOR | FORMAT never required A even while mandating an integer clamp to [−A/2, A/2] — C7 and the clamp are inconsistent for odd A (root cause of F-2) | Confirmed by reading FORMAT §1/§6.1/§10 (v1.0 text) and the two clamps | **R5 APPLIED** (see F-2) | **APPLIED** |
| F-6 | F | MINOR → merged into O MAJOR-1 | "ACCEPTED by both checkers" meant the two Python checkers; the Lean checker had never been run on producer data | as O MAJOR-1 | R6 APPLIED (`acceptance-report.md` status line, §0, §6) | **APPLIED** |
| F-7 = O MINOR-4 | F, O | MINOR (informational) → MINOR | Lean `checkW1` has no C10 mode clause — `0 ≤ m` only; the split is at the theorem. Sound; the normative list did not say so | Confirmed by reading `Checker.lean` 146–147 and O's 1 300-case mode-free differential fuzz (`audit_O_lean_vs_py.expect.json`) | FORMAT §7 C10 bullet rewritten (O's text) | **APPLIED** |
| F-8 = O MINOR-5 | F, O | MINOR → MINOR | By-design blind spots: rotated `segments` (row↔segment misalignment), mis-scaled K or A with m adjusted, negated boxes — all ACCEPTED by all three checkers; each falsifies H-ENCL (vacuous, not wrong); only the two-producer cross-check can detect them; the contract did not say so | Confirmed (F M22, O `mpDH_ahalf` kernel-accepted) | FORMAT §8.1 "What the checker cannot see" paragraph + §10 pointer (both auditors' texts merged) | **APPLIED** |
| O MINOR-1 | O | MINOR → MINOR | `reference_checker.py` printed the ζ trust sentence ("modulo H-ENCL, H-AP") on f_DH files — a laundering hazard for D-R8 | Verified after the repair: `recon_checker_pass.log` shows "checker-level only (D-R8): format-checked modulo H-ENCL for f_DH; no Lean-backed conclusion" on both DH files and on the F-2 probe file | **APPLIED** (prior pass); `acceptance-report.md` §7 note 2 updated | **APPLIED** |
| O MINOR-2 | O | MINOR → MINOR | `ball.py --selftest` never entered the large-argument regime `pow_int_neg` uses at T = 10⁴ (|Im| ≈ 8.5·10⁴); no defect found (O: 1 640 checks, 0 failures) | Verified: `_large_argument_block` now in the selftest (100 thin + 100 wide-box checks at |Im| ≤ 2·10⁵ vs dps-140); selftest 18 469 / 0 | **APPLIED** (prior pass) | **APPLIED** |
| O MINOR-3 | O | MINOR → MINOR | `checkW1` vs the Python checkers have different accepted sets on floor-bearing transcripts (C11 lives in `checkW1Floor`); "both checkers accept" was not well-defined for them | Confirmed by reading `Checker.lean` and `checker_ref.py`; O's fuzz case `fz027` | FORMAT §7 "Floor variant" paragraph; `Instances.lean` asserts `checkW1Floor` for every floor-bearing transcript | **APPLIED** |
| O MINOR-6 | O | MINOR → MINOR | FORMAT §0/§6.3 promise "at least m zeros with multiplicity"; `cert_of_checkW1` delivers the existential form (H-AP in consequence form); `Soundness.lean` records the deferral, FORMAT did not | Confirmed by reading `Soundness.lean` 928–932 and the `RectArgPrinciple` definition | FORMAT §6.3 step 5 v1-scope note | **APPLIED** |
| O INFO-1/-2 | O | INFO | schema `mode ⟹ claimed_m` tie enforced at C10 not SHAPE; two "~" figures in §5 | read; correct as filed | none needed | recorded |
| O INFO-3 | O | INFO | audit scratch modules `Zeta23/W1/AuditO*.lean` left in the working tree, not copied | Verified present (`AuditO.lean`, `AuditOCases.lean`, `AuditOFuzz.lean` + oleans). Note: `AuditOCases.lean` declares the same identifiers as `Instances.lean` in namespace `Zeta23.W1`; they are never imported together and the scratch modules are not program files — left in place as audit evidence | none | recorded |
| side finding (LOG 08:30) | scout | — | `AUDIT-F.md` line 151 records the Mathlib revision as `123d1576…`; the Session-8 design-note addendum (`m2a-m2b-design.md` §7) does too | **Settled from disk:** `lake-manifest.json` `inputRev` and the package HEAD in `~/rh-lean-work/zeta-23-lean-main/.lake/packages/mathlib` are `51e6992efd06126df61a496bebf8f49482a4e129` (committed 2026-08-03), which is also what `lean/README.md` records; `git cat-file -t 123d1576` in that package: *not a valid object name*. The record of truth is the manifest: Mathlib `51e6992e`. The `123d1576` figure in the two Session-8/14 texts is wrong (its origin is not recoverable from disk) | recorded here and in `RUN-REPORT.md` §1; the two texts are audit records and are left as written with this note as the correction | recorded |

## 2. Re-verification record (what the reconciler ran, and where the evidence sits)

| what | script / command | result | log |
|---|---|---|---|
| F-1 raw primitives, `mpi_cos_sin`, repaired wrappers — exact prec-1200 comparisons, seed 20260902 | `python3 recon_rounding.py` (22 s) | raw = 11 violations (exp only), `mpi_cos_sin` = 0, repaired = 0; output identical to the prior pass's log | `recon_rounding.log` |
| F-2 before | pre-repair `producer_mp.py` (git 5a7a32f) `--A 0 --mode exclusion` on the DH rectangle, both checkers | producer exit 0; all 40 argument rows [0, 0]; `checker_ref.py` ACCEPT; `reference_checker.py` ACCEPT | `recon_F2_before.log` |
| F-2 after | repaired producer, A = 1 and A = 100 | A = 1: `PRODUCER STOP` exit 1; A = 100: 40 segments, m = 1, ACCEPT | `recon_F2_after.log` (prior pass) |
| mp-leg self-tests after R1/R2 | `ball.py --selftest`, `zeta_encl.py --validate --points=100`, `hurwitz_encl.py --validate --points=60`, `producer_mp.py --selftest-dh` | 18 469/0; 100/100; 60/60; 24/24 | `recon_selftests_after.log` (prior pass) |
| mp transcripts re-produced after repairs | acceptance §8 commands; `recon_compare_transcripts.py` (all fields except `producer`/`comment`) | t100, deep-t100, DH, t1000: IDENTICAL; t10000 (26 min): see the log | `recon_mp_reproduce.log`, `recon_mp_reproduce_t10000.log` |
| both Python checkers on all 12 acceptance transcripts after repairs | `checker_ref.py`, `reference_checker.py` | 10 ACCEPT (C1–C11, floors verified), 2 REJECT at C2; f_DH banner now D-R8-correct | `recon_checker_pass.log` (prior pass; Lean column appended this pass) |
| the Lean kernel on all 12 | `emit_lean.py` → `Instances.lean` → `lake build Zeta23.W1.Instances` → `#print axioms` | 656 jobs, 13.9 s; 10 × `checkW1Floor = true` (`[propext]`), 2 × `checkW1 = false` (no axioms); no `sorry`/`native_decide` | `recon_lean_instances.log` |
| literal fidelity | `recon_instances_verify.py` (O's independent back-parse reader) | 12 instances, 2 940 rows, 0 mismatches | `recon_lean_instances.log` |
| `maxRecDepth` cause | experiments A / B / B′ | A passes at default, B fails at the def line, B′ passes | `recon_lean_instances.log` |
| Mathlib revision | `lake-manifest.json`, package `git rev-parse HEAD`, `git cat-file -t 123d1576` | `51e6992e`; `123d1576` not an object | this file, §1 last row |

Both auditors' own scripts (`audit_F_*.py`, `audit_O_*.py`) and logs stay in this directory as the
primary evidence; O's resumed run had already re-run every `audit_O_*` script byte-identically
(`AUDIT-O.md` §10), and F's logs were spot-checked for consistency with the artifacts read here.

## 3. Repairs applied at reconciliation (files touched)

`ball.py` (R1 + selftest blocks; docstrings), `zeta_encl.py`, `hurwitz_encl.py`,
`producer_mp.py` (R1 call sites, R2), `reference_checker.py` (O MINOR-1), `mp-leg-notes.md` §3
(R1-doc), `FORMAT.md` (status line; §1, §6.1, §6.3, §7, §7.1, §8.1, §10, §13 — clarifications
only, contract stays v1.0), `acceptance-report.md` (status line, §0, §4, §6, §7), **new:**
`emit_lean.py`, `instances-doc.txt`, `recon_instances_verify.py`, `recon_F2_before.log`,
`recon_lean_instances.log`, `lean/Zeta23/W1/Instances.lean` (program file; also in the working
tree), `lean/README.md`. The Arb leg (`producer_arb.py`) and the Lean checker/soundness files are
untouched. The two audit reports are left as written; this file supersedes them where they differ.

## 4. Demanded repairs (large; not applied here) — with costs

| # | item | why | cost (from `m2a-m2b-design.md` §1.6 / this audit) | blocks |
|---|---|---|---|---|
| D-1 | **Bulk-data packaging for `BarrierCertData`** (O MAJOR-2 repair 2): chunked `def`s or a decoded compact encoding, decided before `BarrierCert.lean` | a single Lean list literal at Gomila scale (3.1·10⁶ rows) cannot compile; `Instances.lean` already needs `maxRecDepth 100000` at 1 294 rows | days (design + a ~10³-row chunking experiment) | M2a item (b) |
| D-2 | **`BarrierCert.lean`**: `BarrierCertData` (general rectangle — W1's C2 hard-wires the strip; t-slice list; Lipschitz-in-t row; per-slice floor consumption), `checkBarrier` reusing W1's C3–C9/C11 arithmetic, soundness generic in f with H-AP restated for general rectangles | Gomila step 3 and Instance02 both need it; not started | 2–3 weeks | Gomila step 3; M2a (e) |
| D-3 | **The f_t / H_t evaluator on BOTH legs** (Polymath15 Thm 1.3 effective A + B + C with the paper's explicit error terms; on-disk source `fetched/p3-22a4`), with a DERIVED remainder on the mpmath side | neither leg evaluates anything but ζ and f_DH; not one Gomila mesh cell is reproducible today | ~3–4 weeks Arb, ~2 weeks mpmath on top of the M1 core | Gomila step 4; M2a (c), (d) |
| D-4 | **Converter** from Gomila's sealed printed-decimal balls to `BarrierCertData` | step 3 input | ~1 week (after D-1/D-2) | Gomila step 3 |
| D-5 | **v1.1 — the rectangle argument principle in Lean** (D-R3): discharge H-AP for ζ on the strip (differentiable on U = {Re s < 1}); the multiplicity-counting form (O MINOR-6) | v1's displayed analytic debt | ½–1 session to generalize + 1–3 sessions to bridge IF the Gomila `lean/certificate-and-argument-principle` branch builds (`gomila-lean-branch-scout.md`: entire-function version, six gaps; a verify agent was running at write time), else research-scale | the "fully kernel-checked" wording |
| D-6 | Stress tests carried from Session 8 (acceptance §7 note 5): a Lehmer-pair-class near-degenerate target for C8; and a Riemann–Siegel-class mp evaluator for M3 heights (26 min at T = 10⁴ today) | untested regimes | days / weeks respectively | M3 pricing |

## 5. Overruled items (with the computation that overruled them)

1. **F-3's cause** ("`decide +kernel` fails with maximum recursion depth"): overruled by experiments
   A/B/B′ — the definition compiler fails on the list literal; `decide +kernel` at the default limit
   evaluates the 1 294-row `checkW1` in seconds once the data is imported. The symptom and the
   remedy F filed are correct and applied.
2. **F-5's optional clause** (add `A % 2 = 0` to C1 in both checkers and Lean): not applied — the
   checker is sound for every A ≥ 1 (only producers clamp; C7 is a reject-more tripwire), and the
   clause would be a contract version bump for no soundness gain. Recorded as a producer requirement
   instead (FORMAT §1).
3. **O's first-draft `Checker.lean` tail-recursion rewrite**: already withdrawn by O; not adopted.
4. **Severity of O MAJOR-1 vs F-6**: reconciled as MAJOR (coverage), because the deliverable's
   central claim — that the trusted checker is the Lean one — had, at Session 8's close, no evidence
   on producer data. Closed by the repair; it does not lower the gate verdict.

## 6. Gate verdict

**repaired-clean.** M2a proceeds. Constraints carried forward: D-1 must be settled before
`BarrierCert.lean`; D-3 on both legs before Gomila step 4; the mp leg's platform assumption is the
weak one stated in `ball.py::_inflate` (transcendental endpoints within 2⁻²⁷² relative of the
truth), tested and cross-checked by the Arb leg, never proved; every public sentence keeps the D-R3
wording "kernel-checked modulo the two displayed hypotheses; fully kernel-checked after v1.1".
