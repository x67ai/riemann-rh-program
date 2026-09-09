# D-R8 build notes — `cert_of_checkW1_fDH` (f_DH in Lean) + the M3 seed ledger (Session 20, Job 1 builder)

**Builder:** Claude Fable 5.1, 2026-09-10 (Session 20). Brief of record: `results/d1-m2a/dr8/BUILD-BRIEF-fDH.md` (Job 1 list 1–5 + the M3-seed addendum). Pricing of record: `PRICING-fDH.md` (§3.1 statement shape BINDING; §3.2 the only label; §2.2 Route G; §4.2 risk checklist) and `PRICING-M3-ledger.md` (§1.2–1.6 the row and the seed). Lean tree `~/rh-lean-work/zeta-23-lean-main` (Lean v4.33.0-rc2, Mathlib `51e6992e`); mirror `rh-program/lean/`. U.S. English. This file is written as the work lands (RULE ONE); the status line below is the resume point.

**Status line:** ALL SECTIONS DONE + FIX PASS APPLIED (§7, 2026-09-10 04:15 IST; Opus FIX-FIRST 1–4 closed; owed: the σ-strong sibling) (§0 setup · §1 Lean built, full cascade 9144 jobs · §2 M3 seed, ledger_check PASS · §3 label sweep · §4 verification logs + hashes · §5 formalization.yaml 0 errors · §6 owed). Job 2 (Opus, clean clone) is next; the commit to overlay is the one named in LOG.md at 03:5x IST (this file's last commit).

## 0. Setup and the pre-build baselines

* **Environment.** `caffeinate` (pid 26194) and both watchdogs running at start; `PATH` with `~/.elan/bin`; Lake 5.0.0 / Lean v4.33.0-rc2; Mathlib `51e6992e` oleans present in the tree; mpmath 1.3.0, PyYAML 6.0.3, jsonschema 4.25.1 for python3. Load check `ps -Ao pcpu,comm | awk '$1>50'` empty before every build. Mirror `rh-program/lean/` and tree `~/rh-lean-work/zeta-23-lean-main` were `cmp`-identical for all six W1 files, the root and `formalization.yaml` before any edit.
* **κ reproduction (non-negotiable (i); risk R2).** `dr8/kappa_check.py` → `dr8/kappa-check.log`: the contract line `kap = (sqrt(10-2*sqrt5) - 2)/(sqrt5 - 1)` is read from `FORMAT.md` §9.2 AND from `results/ccm-dh-test/dh.py` by regex (both found verbatim), evaluated at 60 digits; the Lean `kappaDH` transcription evaluated token by token; and the closed form tan θ with ε_χ = e^{2iθ} = τ(χ)/(i√5), χ mod 5, χ(2) = i, computed from the Gauss sum. All three agree: **κ = 0.284079043840412296028291832393126169091088088445737582759163**, |contract − Lean| = 0, |contract − closed form| = 3.9·10⁻⁶², i.e. 60 digits (≥ 30 demanded); leading digits 0.28407904… as PRICING §1.1. Radicand 10 − 2√5 = 5.5278… > 0 and denominator √5 − 1 = 1.2360… ≠ 0 (no `Real.sqrt`/division junk). VERDICT PASS.
* **Baseline `#check @Zeta23.W1.cert_of_checkW1_ap`** captured BEFORE any edit (scratch `check_ap_before.lean` via `lake env lean`, 2.8 s): statement as in `ArgPrincipleBridge.lean` lines 449–453; axioms `[propext, Classical.choice, Quot.sound]`. Goes into `dr8/no-regression.log` with the after-copy and the diff.
* **Baseline hashes** (non-negotiable (iv)): every `comparator/*` file in `results/d1-m2a/packaging/hashes.txt` (6) and the four `Zeta23/DBN/*` files of `lane-a/EMIT-NOTES.md` §5 (current pass) match the tree — `OK` ×10 — plus a full SHA-256 manifest of `Zeta23/DBN/**` and `comparator/**` (147 files) for the after-diff. Goes into `dr8/untouched.log`.

## 1. Lean — Route G in `Soundness.lean`, the new leaves `FDH.lean` and `Ledger.lean`

**Status: all four modules BUILT (first pass, 03:2x IST), no errors, no warnings after one deprecation fix; full-tree cascade `lake build Zeta23` running in the background.**

* `Zeta23/W1/Soundness.lean` (1262 → 1300 lines; diff 98 added / 63 removed lines, scratch `soundness.diff`, applied by `edit_soundness.py` with content-located anchors, then one `sed` for the deprecation). What changed, exactly:
  1. §9: the ζ-only lemma is replaced by the generic `continuousOn_logDeriv_seg_of_diffOn {f U} (hU : IsOpen U) (hf : DifferentiableOn ℂ f U) (hin) (hnz)` — PRICING Appendix B verbatim — plus `differentiableOn_riemannZeta_re_lt_one` (the former inline `hdiff` block as a lemma) and `continuousOn_zeta_logDeriv_seg` KEPT with its v1 name and statement as the instance at U = {Re s < 1}.
  2. §10: the soundness theorem is now `cert_of_checkW1_of_diffOn (f : ℂ → ℂ) (hf : DifferentiableOn ℂ f {s : ℂ | s.re < 1}) (d) (hc) (hEncl : W1EnclOK f d) (hAP : RectArgPrinciple f)`, with the v1 body verbatim except: `riemannZeta` → `f` (16 occurrences in the body), `hUopen` hoisted above the four `hcont*` blocks, the four blocks call the generic lemma with `hUopen hf` and their membership goals close by `simp only [Set.mem_ofPred_eq, cpt_re]` (was `[cpt_re]`), the inline `hdiff` block deleted and `hf` passed to H-AP. Nothing else in the 230-line body moved.
  3. `cert_of_checkW1` is re-stated with its v1 docstring and statement character-for-character and proved as `cert_of_checkW1_of_diffOn riemannZeta differentiableOn_riemannZeta_re_lt_one d hc hEncl hAP` (one line).
  4. The header's D-R8 sentence (lines 55–56) gains a dated block saying the theorem is generic since 2026-09-10 and pointing at `FDH.lean`.
  `lake build Zeta23.W1.Soundness`: *Built (4.4 s)*, 3142 jobs; four `Set.mem_setOf_eq` deprecation warnings fixed to `Set.mem_ofPred_eq` (the form the file already used) → rebuilt clean.
* `Zeta23/W1/FDH.lean` (NEW, 168 lines): `kappaDH`, `fDH` (PRICING §3.1 / Appendix A verbatim), `differentiable_fDH` (Appendix A's 12-line proof), `hasSum_hurwitzZeta_one_fifth` (the convention anchor as a theorem), `cert_of_checkW1_fDH` in EXACTLY the §3.1 statement shape, the four rational-unfolding lemmas `mpDH_T1/T2`, `arbDH_T1/T2` (`show … ; norm_num`), and `mpDH_zero`, `arbDH_zero` in §3.1's numeric form `(8569/100 : ℝ) < ρ.im ∧ ρ.im < 8571/100`. The module doc carries the §3.2 label verbatim, the never-say list, and the §1.3 convention paragraph. `lake build Zeta23.W1.FDH`: *Built (1.5 s)*.
* `Zeta23/W1/Ledger.lean` (NEW, 95 lines): the eight 3-line corollaries `{mp,arb}Null{T100,T1000,T10000,DeepT100}_exclusion`, PRICING-M3-ledger §1.6 shape verbatim (`(cert_of_checkW1_ap d (checkW1Floor_spec d_check).1 hEncl).2 (by decide)`); module doc = the row table, the per-row label, the never-say list. *Built (1.4 s)*.
* `Zeta23.lean` (root): `+ import Zeta23.W1.FDH`, `+ import Zeta23.W1.Ledger` (2 lines).
* `Instances.lean`, `Format.lean`, `Checker.lean`, `ArgPrincipleBridge.lean`, `Examples.lean`: UNTOUCHED (the bridge's `cert_of_checkW1_ap` consumes `cert_of_checkW1`, whose statement is unchanged, so the bridge re-elaborates without edit: *Built (1.6 s)*).
* Mirrored to `rh-program/lean/` (cmp-identical): `Zeta23/W1/Soundness.lean`, `Zeta23/W1/FDH.lean`, `Zeta23/W1/Ledger.lean`, `Zeta23.lean`.

* **Full cascade** (after §1): `lake build Zeta23` — *Build completed successfully (9144 jobs)*, **68 s** wall (285 s user, 740 % CPU; the 397 s on record was a cold clean clone — here Mathlib and the untouched modules replayed), 0 errors; the only warnings are upstream Zeta23 deprecations (`Statement.lean`, `ZeroSide.lean`, `PairCeiling/Stability.lean` …), none in any W1/DBN/comparator module. Then `lake build Solution.DBN` — *Build completed successfully (8826 jobs)*, 14 s — and `PrintAxioms/DBN.lean` re-run: the seven DBN statements on exactly the recorded axioms (`dr8/solution-dbn-rebuild.log`). One lake process throughout; `ps -Ao pcpu,comm | awk '$1>50'` empty before each build.
* **Interruption record.** The session died on a server-side HTTP 500 at ≈ 03:38 IST during §3; the watchdog had committed everything (`5348faa`, `9a96a3a`); resumed from this status line without redoing §0–§1.

## 2. The M3 seed ledger (`results/d1-m3/`) — DONE, `ledger_check.py` PASS (4 rows, 0 findings)

Layout exactly PRICING-M3-ledger §1.3 (pointer files instead of copies for the seed rows, as §1.3 specifies): `README.md` (charter line 48 and D-R6 quoted from the direction file BY CONTENT by the writer script, the licensed label, the v1.0-string note, the four provenance kinds, the status values, the layout, the add-a-row checklist, the never-say list, and the single-box sentence rule), `LEDGER.md` (append-only, header + four dated lines), `index.json` (regenerated by the checker; `{format, version, generated_by, rows}` — no timestamp so regeneration is byte-stable, no aggregate field), `ledger-schema.json` (JSON Schema 2020-12; `grade` enum `["box"]` so `turing` is refused; `status` `accepted` requires both legs and `CONSISTENT` via `if/then`; `additionalProperties: false` at every level so no aggregate can be added silently), `ledger_check.py` (UNTRUSTED: re-hashes, re-reads every transcript field the row quotes — rect = box, K, A, segment count, winding sums of the argument rows, floor Fn/Fd, embedded label — RE-RUNS `reference_checker.py`, `checker_ref.py` and `acceptance/crosscheck.py`, checks the Lean names in the mirror by regex in their exact declared shape (`def <d> : W1Data where`, `theorem <d>_check : checkW1Floor <d> <d>_floor = true := by decide +kernel`, and the 3-line corollary in `Ledger.lean`), checks the build record names `<d>_check` with `[propext]` and `fdh-axioms.log` names `<d>_exclusion` with the three standard axioms, recomputes `entry_sha256`, regenerates `index.json`; exit ≠ 0 on any drift), `seed_rows.py` (the one-off generator; reads everything from disk, re-runs the checkers for today's verdicts), and `rows/<row_id>/{ROW.json, PROVENANCE.md, REFS.txt}` ×4.

Rows (all `status: accepted`, `provenance.kind: acceptance`, `grade: box`, `function: zeta`, `mode: exclusion`, `claimed_m: "0"`): R1 `zeta_3-5_9-10_100_101` (δ₀ = 1/10; mp 52 segments S = [−24, 28], arb 27 segments S = [−14, 13]; 83 overlap pairs CONSISTENT); R2 `zeta_3-5_9-10_1000_1001` (mp 81 / arb 65; 158 pairs); R3 `zeta_3-5_9-10_10000_10001` (mp 1 294 / arb 983; 2 547 pairs); R4 `zeta_21-40_39-40_100_101` (δ₀ = 1/40; mp 58 / arb 30; 90 pairs). The eight transcript SHA-256s in the rows equal PRICING-M3-ledger §2's table (re-verified by the checker from the files on disk: `sha256 ok` ×8); both Python checkers ACCEPT on all eight today; Lean names `{mp,arb}Null{T100,T1000,T10000,DeepT100}` / `_floor` / `_check` / `_exclusion` all present. `dr8/ledger-check.log` is the checker's full output, exit 0.

**Two deliberate deviations from PRICING-M3-ledger §1.4's example, both toward honesty:** (a) the `sentence` field is the SINGLE-BOX sentence ("no zeros of zeta in the closed box [σ₁, σ₂] × [T₁, T₂] — kernel-checked modulo the displayed hypothesis H-ENCL (producers untrusted)"), not §1.4's range form "Re s ≥ ½ + δ₀ in [T₁, T₂]", because §4.1 of the same pricing says the range form is licensed only with a box family reaching σ = 1; `delta0` is recorded and a `delta0_form` field spells the honest single-box reading; (b) each leg carries `embedded_trust_label` (the v1.0 string inside the JSON) next to the row's licensed label, so the two are never confused. Also added beyond §1.4: `lean.corollary_module`, `lean.corollary_axioms_record`, `python_checkers.logs`. `LEDGER.md`'s "added" column is the UTC date (the rows' `added_utc`), hence 2026-09-09 for a 03:4x IST landing.

**Lean leaf** `Zeta23/W1/Ledger.lean`: §1. **No new rows, no producer runs, the six Arb calibration rows NOT run** (not authorized).

## 3. The label sweep — DONE; exactly which files, and why (for Job 2's audit)

The only label allowed is PRICING §3.2's sentence, verbatim: *"f_DH has at least one zero ρ with 1/2 < Re ρ < 1 and 85.69 < Im ρ < 85.71 (the live-fire window; the transcript's rectangle is R = [4/5, 41/50] × [85.69, 85.71]) — kernel-checked modulo the displayed hypothesis H-ENCL_DH (the two producers' enclosures of f_DH on ∂R are true; producers untrusted)."* Decision taken (no orchestrator question): the schema-enforced per-function `trust_label` constant for `f_DH` becomes THAT sentence, not §2.3's shorter proposal, so one string exists everywhere — it is box-specific by design, which is harmless because the only f_DH transcripts are the two live-fire ones on that box and any further f_DH transcript enters only by a version bump (FORMAT §9.2's own last sentence). Files edited, each by an anchored replacement asserted to match exactly once:

| file | what changed | why |
|---|---|---|
| `results/d1-m1/w1-schema.json` | the `f_DH` `trust_label` `const` → §3.2 sentence; a top-level `$comment` (JSON-Schema keyword, not a transcript field) with the dated note | the schema enforces the label per function; leaving the old string would make the two DH JSONs schema-invalid or the label inconsistent (standing order 5) |
| `results/d1-m1/producer_mp.py`, `producer_arb.py` | `TRUST_LABELS["f_DH"]` → §3.2 sentence, dated trailing comment | the producers write the field; a future re-emission must carry the same string |
| `results/d1-m1/checker_ref.py` | `_LABELS["f_DH"]` → §3.2 sentence | its shape check compares the field to the constant |
| `results/d1-m1/reference_checker.py` | `TRUST_LABELS['f_DH']` → §3.2 sentence (double-quoted — the sentence contains an apostrophe; the first single-quoted edit was a SyntaxError, caught by re-running the checker and fixed); the ACCEPT banner for non-ζ functions now prints `TRUST_LABELS[function]` instead of a concatenated copy of the old string | same as checker_ref; the banner was a second copy of the label (AUDIT O MINOR-1's laundering hazard in reverse) |
| `results/d1-m1/acceptance/w1-mp-dh-livefire.json` | `trust_label` → §3.2 sentence; the dated note appended to the existing `comment` field; nothing else (1-space JSON layout preserved by text replacement) | the on-disk transcript must carry the label the checkers now enforce |
| `results/d1-m1/acceptance/w1-arb-dh-livefire.json` | `trust_label` → §3.2 sentence; a `comment` field ADDED after `trust_label` (the Arb producer wrote none; `comment` is schema-optional) with the dated note | idem |
| `results/d1-m1/FORMAT.md` | dated block directly under the §9.2 heading (insertion-only; v1.0 text kept) | the contract's "checker-level only" scope is discharged; the label paragraph there is now false as a present-tense statement |
| `results/d1-m1/acceptance-report.md` | dated block after §0's closing sentence, with the old → new SHA-256 of both DH JSONs | the report's row 3 and its `trust_label` quotes are historical; the hash change must be on record where the hashes were |
| `directions/D1-certified-refutation-arm.md` | dated sub-bullet under the D-R8 line; a "SESSION-20 STATE, part 2" paragraph in Current frontier | the brief's item 3 |
| `lean/README.md` | table rows for `FDH.lean`, `Ledger.lean` (Soundness line count 1300); two dated sections "D-R8 (2026-09-10)" and "M3 seed (2026-09-10)" before "What these build against" | the brief's item 3 |
| `lean/Zeta23/W1/Soundness.lean` header | dated block after the D-R8 sentence (§1) | its "ζ-SPECIFIC" sentence is now history |

Verification after the sweep (`dr8/label-sweep-checkers.log`, one clean run): both checkers ACCEPT both DH JSONs; both checkers' negative-control self-tests pass; `recon_instances_verify.py` 0 mismatches over 12 instances (the label is outside `W1Data`, so `Instances.lean` is untouched and still back-parses); `crosscheck.py` on the DH pair CONSISTENT (122 pairs); both checkers ACCEPT all eight ζ null transcripts (their v1.0 label constant is untouched). New hashes: `w1-mp-dh-livefire.json` 756b1447… → see `hashes-fdh.txt` (13 732 bytes); `w1-arb-dh-livefire.json` e39b90cb… → see `hashes-fdh.txt` (15 994 bytes). Sweep grep: `checker-level only` now occurs only in historical records (AUDIT*.md, RUN-REPORT.md, recon logs, the v1.0 text of FORMAT §9.2 and acceptance-report kept under dated blocks, `reference_checker.py`'s AUDIT-O comment) and in the "was the v1.0 string" mentions of the new blocks; "RH-for-DH disproved" and "fully machine-checked" appear in the new text only inside the never-say lists, negated.

## 4. Verification logs and hashes (non-negotiables (ii), (iv), (vii), 10(i))

* `dr8/fdh-axioms.log`: `#print axioms` — `cert_of_checkW1_fDH`, `mpDH_zero`, `arbDH_zero`, `differentiable_fDH`, `hasSum_hurwitzZeta_one_fifth`, `cert_of_checkW1_of_diffOn`, `continuousOn_logDeriv_seg_of_diffOn`, `differentiableOn_riemannZeta_re_lt_one`, `continuousOn_zeta_logDeriv_seg`, `cert_of_checkW1`, `cert_of_checkW1_ap` (unchanged), and the eight `_exclusion` corollaries: every one `[propext, Classical.choice, Quot.sound]`; `mpDH_check`, `arbDH_check` `[propext]` (unchanged). Plus `#check` of every new statement and `#print` of `kappaDH`, `fDH` (the exact terms Job 2 compares with FORMAT §9.2).
* `dr8/no-regression.log`: `#check @Zeta23.W1.cert_of_checkW1_ap` before and after — NO DIFFERENCE (statement and axioms); `ArgPrincipleBridge.lean` untouched (same hash in tree and mirror).
* `dr8/untouched.log`: comparator DBN files ×6 vs `packaging/hashes.txt` OK; `Zeta23/DBN/{Instance02.lean, Instance02/Asym_mp.lean, Instance02/Asym_arb.lean, Asym.lean}` vs `lane-a/EMIT-NOTES.md` §5 OK; the full 143-file manifest of `Zeta23/DBN/**` + `comparator/**` IDENTICAL before/after the build. The "MIRROR DRIFT" line is the expected asymmetry — the tree's `comparator/` also holds the parent library's own files (`Challenge.lean`, `ChallengeDeps.lean`, `config.json`, …), which the mirror deliberately never carries — annotated in the log; every DBN-topic file is identical tree = mirror.
* `dr8/fdh-trust-greps.log`: comments stripped (nested block + line) by `trust_greps_fdh.py` over `FDH.lean`, `Ledger.lean`, `Soundness.lean`, `ArgPrincipleBridge.lean`, `Format.lean`, `Checker.lean`, `Instances.lean`, `Zeta23.lean`: **0 hits** for axiom / native_decide / unsafe / implemented_by / extern / opaque / sorry / admit / ofReduceBool; the raw grep's two hits are the words "sorry-free" and "#print axioms" in docstrings.
* `dr8/kappa-check.log` (§0), `dr8/label-sweep-checkers.log` (§3), `dr8/ledger-check.log` (§2), `dr8/solution-dbn-rebuild.log` (§1).
* **SHA-256 of every new/changed file** — `dr8/hashes-fdh.txt`, reproduced here:

```
# dr8/hashes-fdh.txt — SHA-256 of every file this build created or changed (KICKSTART 10(i)); 2026-09-10 03:48 IST; BUILD-NOTES-fDH.md itself is hashed in LOG.md at the commit
aeb8f62ee9876762095d04903121596be1bb5f654626dfe588a4fb6c1e48d056  lean/Zeta23/W1/Soundness.lean
3fa70b82d5a03d9b88a3c296dbdf24d1704290939e1e13fb604e5ca801f7d2f7  lean/Zeta23/W1/FDH.lean
4da558a65c48fc9ede3643b10e2fc742ac399aca0212c15ef42587743cbaf7a8  lean/Zeta23/W1/Ledger.lean
42e50a51121fd1fd3bdb5cc89abc7bbbd7f82c56ddfe3b481b4d5d9fc08afea4  lean/Zeta23.lean
89475ddbd24fa1da67b0dbd09cedf91124f1d712f68f6aada508368ce7e0d5e0  lean/formalization.yaml
074b9d0cd8f4921eac7afcc5729f6724de78fc64b797720c9eed5b4af908c5ee  lean/README.md
02563d15160b3834ba64c8746f4795010ae87af1021efbd325e3e6ef1b1aacfc  results/d1-m1/w1-schema.json
79c0271176c762fb78a05ae26595535e7247ef5cc8a84877cb97e05b43db4fd8  results/d1-m1/producer_mp.py
dee9e1be3ba1922f7709339cca86ac9e59c6f22b91d3792dedc22d3be79a6de5  results/d1-m1/producer_arb.py
c3957816c5fe6dd8c97fa1774096ba87712ab226af96ba9a3c143407ac7b40dd  results/d1-m1/checker_ref.py
8724d4ee7459f59dccb68bc3a06aaf3bc3d7a9b7e31ad2b8aa2304164f102ec4  results/d1-m1/reference_checker.py
7ea54aadecb02f9b7be7876807064972ded278f421e0097f76f81d31117b352e  results/d1-m1/FORMAT.md
16426c8831bb98af5363885805bf16fde6961b15926324a134dcfe79aa04e2a9  results/d1-m1/acceptance-report.md
fdd3701d2f353990beeac0d7e56808a8cbe959a1748c904d152fc221e93a0765  results/d1-m1/acceptance/w1-mp-dh-livefire.json
b652bde5aedb79d8d5723942adbd75ec83b2ca1fd0e603cdfcdb6c75b55eae9d  results/d1-m1/acceptance/w1-arb-dh-livefire.json
c1260c4b61fc5dc40c372fef36ac8b3e05f3875ec494fe49c9434e95648d5f54  directions/D1-certified-refutation-arm.md
64076af89b68d2cee064fb91a694c4d8303d25ac52ab8c0a5e285ed5c82ffeff  results/d1-m3/README.md
ec7cd0527ebc4761f6021a51c7faa7d8c1bdc8da2a091905e5b7e10c8b9b3eb1  results/d1-m3/LEDGER.md
70e0ca3c7a623c2dcddc2afcbf07c2f11f5bec593d5f6ba594e3fa4efd4edabc  results/d1-m3/index.json
864f4bdaa0c716390df41500924eab9f88427f06024ad15c7b78da041fc6cffe  results/d1-m3/ledger-schema.json
6217975864ca941695fe35eacd706649bd2624af7318b35baa4dbf974c2f34e7  results/d1-m3/ledger_check.py
6326912cee6db9af6a8a0ad27a8cec7bc2c25d932f2e31739e13447c66320cc8  results/d1-m3/seed_rows.py
a00dcd342fe31087e488867581e0a819de3ea03a9f3f36985b21e3d04cb4c1e2  results/d1-m3/rows/zeta_21-40_39-40_100_101/ROW.json
06384f15359315af2722b52cea1c173e6a9cc06f37a76f965d637ec673ef75d2  results/d1-m3/rows/zeta_3-5_9-10_100_101/ROW.json
3ba27bbfe4949cd49f1c5adc9fb5f16dd9a58338b7394933029178fbb7a52f17  results/d1-m3/rows/zeta_3-5_9-10_1000_1001/ROW.json
43825ac2dd9caa7c9464f62fc3b727ea36f8dec4a67f0e1190b637a82d9cf841  results/d1-m3/rows/zeta_3-5_9-10_10000_10001/ROW.json
a6cc69f084df216679561efb0510539790d7510f2ca3a3791b937ed7a9cea73b  results/d1-m3/rows/zeta_21-40_39-40_100_101/PROVENANCE.md
898f534c44866abe2c0b4b61c468baa9055f62fe374fd94b03def52d5b766bf0  results/d1-m3/rows/zeta_3-5_9-10_100_101/PROVENANCE.md
1119830d2572232897f7ef87a5576420240efa9f917b2043484325cba086c141  results/d1-m3/rows/zeta_3-5_9-10_1000_1001/PROVENANCE.md
72cd9fbd8e358b934786d79167cbcb80d943761ee358505dbe7b2739304d2112  results/d1-m3/rows/zeta_3-5_9-10_10000_10001/PROVENANCE.md
231323d9615222d4df0bb9b73a3a97e1934e5456070450df85b2e23fec2d20ba  results/d1-m3/rows/zeta_21-40_39-40_100_101/REFS.txt
c75771fbb5245565e04554095db65b8ea9f0084787e8b7714cea91cf66cc9012  results/d1-m3/rows/zeta_3-5_9-10_100_101/REFS.txt
93bea9652cce66d83e4114b0e279293d195ab7e97c1dabb90f2c9e31607d952e  results/d1-m3/rows/zeta_3-5_9-10_1000_1001/REFS.txt
310c242b5422217be0f39f258b0ccc71dcb0a6a2ba5d137b68a56a225ac533de  results/d1-m3/rows/zeta_3-5_9-10_10000_10001/REFS.txt
f3356ca4b074caaf6c30526f25a2cc562421238780e33c31473d3737c6f2b533  results/d1-m2a/dr8/kappa_check.py
aea399ea314c09700b48d0375a79e2f0aefdf06210fc6e89a444fdc332ff8709  results/d1-m2a/dr8/kappa-check.log
e5ad7118b29eed66394d0a8819331c6dcfeb7defdf54da4e509291085358fe39  results/d1-m2a/dr8/no-regression.log
4f5c1b16b70f2a16c5076c381681ca210838d30fa741de4a87add05646d36180  results/d1-m2a/dr8/untouched.log
bd8c04bb561673ac77918b6f0ce01fb08243d4f515fecf6f2143abbd1e4f51aa  results/d1-m2a/dr8/fdh-axioms.log
d9e1d89d1d11a0bffa16946056c5f14c6b250890d58948cb9f9651e26d7e83ec  results/d1-m2a/dr8/fdh-trust-greps.log
b0a0893420f30d75f502265d348893d7a834c9374e21ff634d5b2b80a691f246  results/d1-m2a/dr8/trust_greps_fdh.py
66e73fac0471495875dec0bceb9d30a3fafb8ddcf38fa67e934c76c73a040b98  results/d1-m2a/dr8/label-sweep-checkers.log
b1c179e9b29ed3baa7ffd1ee8fead7b52240e09d677b90145eb5ba6a0955ce44  results/d1-m2a/dr8/ledger-check.log
beeec217e95cc5a26fdfd0e11d50a8f0ea3cc712c552099008d03ccf31813c0b  results/d1-m2a/dr8/solution-dbn-rebuild.log
902f030ec61061b734adc26296185cb3c1fca79b7a5b667d438758f7f5aeba91  results/d1-m2a/dr8/formalization-yaml-jsonschema.log
22bd0b61631535fc68efbdf01e3013362437673ac836d721dfbdf80773244ec3  results/d1-m2a/dr8/formalization.schema.dispatcher.json
93247a8093ea0bb622650e8f387bcc95c4e4c7941408974d6779341844262b27  results/d1-m2a/dr8/v0.3.schema.json
25ff6b25ca4511635aff4443cf20480c15e59dddf19591c730950b442ea54fce  results/d1-m2a/dr8/v0.4.schema.json
# tree copies (must equal the mirror lines above): 
aeb8f62ee9876762095d04903121596be1bb5f654626dfe588a4fb6c1e48d056  /Users/jaytyagi/rh-lean-work/zeta-23-lean-main/Zeta23/W1/Soundness.lean
3fa70b82d5a03d9b88a3c296dbdf24d1704290939e1e13fb604e5ca801f7d2f7  /Users/jaytyagi/rh-lean-work/zeta-23-lean-main/Zeta23/W1/FDH.lean
4da558a65c48fc9ede3643b10e2fc742ac399aca0212c15ef42587743cbaf7a8  /Users/jaytyagi/rh-lean-work/zeta-23-lean-main/Zeta23/W1/Ledger.lean
42e50a51121fd1fd3bdb5cc89abc7bbbd7f82c56ddfe3b481b4d5d9fc08afea4  /Users/jaytyagi/rh-lean-work/zeta-23-lean-main/Zeta23.lean
89475ddbd24fa1da67b0dbd09cedf91124f1d712f68f6aada508368ce7e0d5e0  /Users/jaytyagi/rh-lean-work/zeta-23-lean-main/formalization.yaml
```

## 5. `lean/formalization.yaml` — DONE, validated, copied to the tree

Added: three `status.main_results` entries (the f_DH unit — `cert_of_checkW1_fDH`, `mpDH_zero`, `arbDH_zero`, `differentiable_fDH` with the §3.2 label verbatim; the generic soundness theorem; the eight ledger corollaries), three `alignment.statements` entries (FDH, the generic Soundness theorem, the Ledger), and `fidelity.divergences` item **(l)**: the f_DH identification is META-level (PRICING §1.3), κ a 60-digit-checked transcription, `W1Data` carries no function tag, the ledger corollaries license the single-box sentence only. Validated with PyYAML 6.0.3 + jsonschema 4.25.1 (Draft 2020-12) against the same upstream URL as `packaging/formalization-yaml-jsonschema.log` (the dispatcher, sha256 `22bd0b61…` unchanged, and its `$ref`s v0.3/v0.4 fetched with a retry loop; v0.4 sha256 `25ff6b25…` = the packaging copy): **errors: 0**; 14 main results, 19 alignment statements (`dr8/formalization-yaml-jsonschema.log`). Copied to the tree, `cmp`-identical.

## 6. Owed / not done — honest list

1. **Job 2 (Opus, clean clone) has not run**; nothing here is independently checked yet. The commit to overlay is named in LOG.md.
2. **`Zeta23/W1/Instances.lean`'s module doc** still says "for the two f_DH live-fire transcripts there is NO theorem about f_DH at all" (and `results/d1-m1/instances-doc.txt`, its source). Deliberately NOT regenerated: the file is emitter-written and back-parse-verified as it stands and the brief says "unchanged". Superseded by `FDH.lean`'s header and the README section; a future re-emission should update `instances-doc.txt` first.
3. **Historical records keep the old label** (`AUDIT.md`, `AUDIT-O.md`, `RUN-REPORT.md` line 5, `recon_checker_pass.log`, `recon_F2_before.log`, acceptance-report §3 body): left as dated history, covered by the acceptance-report's §0 dated block. `RUN-REPORT.md` did not get its own block (the brief did not list it); a one-line dated note there would be tidy.
4. **The seed rows' `wall_seconds` on the Arb leg** come from `cost-curve.json` (the zsh `time` figure), not from the JSON (the Arb producer records no wall time); the mp figure is the producer's own metadata. Noted so nobody reads the two columns as the same instrument.
5. **W1 packaging (10(j) challenge/solution pair for the W1 topic, f_DH twin included)** — not this brief's (PRICING §4.4 GO-later trigger); `formalization.yaml` lists the theorems, no `Challenge/W1.lean` exists.
6. **Not done by design:** no new ledger rows, no producer runs, no Arb calibration rows, no FORMAT version bump, no new function tag.
7. **STATUS.md** not touched (the orchestrator's); LOG.md got one entry (below).

## 7. Fix pass (2026-09-10 04:15 IST) — the Opus checker's FIX-FIRST 1–4 (`dr8/CHECK-fDH-O.md` §12), applied exactly, nothing more

Orchestrator's decision on FIX-FIRST 1: NO new Lean now; relabel. No proof, statement, transcript arithmetic or seed-ledger file changed. Content-located anchors throughout; every replacement asserted to match exactly once.

1. **Label (FIX-FIRST 1).** The §3.2 sentence claimed the zero lies "in R = [4/5, 41/50] × …" while `cert_of_checkW1_fDH` / `mpDH_zero` conclude only 1/2 < Re ρ < 1 ∧ T₁ < Im ρ < T₂ (the proof has `hρmem ∈ rectOpen …` in scope and discards `hr1`/`hr2` by `lt_trans`). The one string was replaced everywhere it appeared — 14 files: FORMAT.md §9.2 block, acceptance-report §0 block, the D1 direction file (both blocks), lean/README.md, `FDH.lean` module doc (re-wrapped, comment only), `formalization.yaml`, `w1-schema.json` (the `f_DH` const), `producer_mp.py`, `producer_arb.py`, `checker_ref.py`, `reference_checker.py`, both DH JSONs' `trust_label`, and §3 of this file — by the sentence that states exactly what the theorem proves, verbatim now:
   *"f_DH has at least one zero ρ with 1/2 < Re ρ < 1 and 85.69 < Im ρ < 85.71 (the live-fire window; the transcript's rectangle is R = [4/5, 41/50] × [85.69, 85.71]) — kernel-checked modulo the displayed hypothesis H-ENCL_DH (the two producers' enclosures of f_DH on ∂R are true; producers untrusted)."*
   The never-say lists are kept unchanged. **PRICING-fDH.md §3.2 (the pricing of record) is NOT edited** — its wording is superseded by this section and by CHECK-fDH-O.md; a future session must take the label from here, not from the pricing. Fidelity item **(m)** added to `formalization.yaml` and appended (with (l)) to `results/d1-m2a/packaging/FIDELITY.md`: the box-form conclusion is NOT stated; a σ-strong sibling `cert_of_checkW1_of_diffOn'` (sigma1 d < Re ρ < sigma2 d) with box-form instance corollaries is OWED (recorded below and in the D1 direction file as the next D-R8 item; frozen statements untouched). After the relabel: both Python checkers ACCEPT both DH JSONs (banners print the new sentence), both negative-control self-tests pass, `recon_instances_verify.py` 0 mismatches (`dr8/fix-pass-checkers.log`).
2. **`reference_checker.py` comment (FIX-FIRST 2).** The AUDIT-O MINOR-1 comment's trailing sentence ("an f_DH acceptance is checker-level only and carries no H-AP-backed conclusion") replaced by the checker's dated text (comment only; the file compiles; checker re-run above).
3. **`Instances.lean` module doc (FIX-FIRST 3).** One dated three-line note inserted after the "there is NO theorem about f_DH" bullet, in `results/d1-m1/instances-doc.txt` FIRST (the emitter's source) and then identically in `lean/Zeta23/W1/Instances.lean` and the tree copy (comment only: `git diff` = 3 added comment lines, nothing else). `Instances.lean` is named in neither `packaging/hashes.txt` nor `lane-a/EMIT-NOTES.md` §5 (checked by grep), so no packaging record breaks; the back-parse re-run gives 0 mismatches over 12 instances (the literals did not move). New hash in `hashes-fdh.txt` (fix-pass block). Owed item 2 of §6 is thereby closed.
4. **`packaging/hashes.txt` (MINOR 4).** Three-line dated supersession note appended (append-only): `lean/formalization.yaml` → 99b77f8022bfef03494c980acb1710e58b81dbf16c99f11749bc542d640746b0, `packaging/FIDELITY.md` → dee704cf8f3762db01a33c7893b5c26a53549b25a80c103f4a2552263e681c99; the six comparator/* lines still verify.

Rebuild: `lake build Zeta23` — *Build completed successfully (9144 jobs)*, 44 s; only `W1.Instances`, `W1.Ledger`, `W1.FDH` re-elaborated (comment changes), nothing else. Axioms re-probed with the same probe: unchanged (19 declarations on `[propext, Classical.choice, Quot.sound]`, the two `_check` facts on `[propext]`). `formalization.yaml` re-validated: **errors: 0** (appended to `dr8/formalization-yaml-jsonschema.log`); copied to the tree; `FDH.lean`, `Instances.lean`, `formalization.yaml` cmp-identical tree = mirror. Post-fix hashes: `dr8/hashes-fdh.txt`, fix-pass block (FDH.lean ed6d88926ed51c04…, Instances.lean 430a325f698e4ca0…, formalization.yaml 99b77f8022bfef03…, w1-mp-dh-livefire.json 125e6ca0420dc227…, w1-arb-dh-livefire.json 92494c7895b89326…).

**Owed after the fix pass (supersedes §6 items 1–2):** (a) the σ-strong sibling `cert_of_checkW1_of_diffOn'` + box-form `mpDH_zero'`/`arbDH_zero'` (next D-R8 item; ≈ 20 lines of Lean, one cascade rebuild, one Opus re-check); (b) the Opus re-check of this fix pass itself; (c) `PRICING-fDH.md` §3.2 wording superseded but not annotated (record item, not edited by decision); §6 items 3–7 stand.
