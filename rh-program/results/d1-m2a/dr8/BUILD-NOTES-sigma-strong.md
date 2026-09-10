# D1 — the σ-strong sibling `cert_of_checkW1_of_diffOn'` and the box-form f_DH corollaries — build notes (Job 1, Fable 5.1; Session 21, 2026-09-10 14:33–14:45 IST)

Brief: `dr8/BUILD-BRIEF-sigma-strong.md` (Job 1). Specification: `dr8/CHECK-fDH-O.md` §12 FIX-FIRST 1 "Exact fix"; `dr8/BUILD-NOTES-fDH.md` §7 "Owed after the fix pass" (a); `dr8/PRICING-fDH.md` §3.1–§3.2. Tree `~/rh-lean-work/zeta-23-lean-main` (Lean v4.33.0-rc2, Mathlib 51e6992e), mirror `rh-program/lean/` (cmp-identical after the build). Base commit `d4c7fc4`. Not independently checked yet: Job 2 (Opus, clean clone) is the next step.

## 1. What was added (nothing removed, nothing frozen touched)

**`lean/Zeta23/W1/Soundness.lean`** (1300 → 1534 lines): one insertion between the end of `cert_of_checkW1_of_diffOn` (line 1181) and the docstring of `cert_of_checkW1` — lines 1–1181 and the tail from `cert_of_checkW1` onward are byte-identical to the pre-edit mirror (`diff` of `sed` ranges; `dr8/sigma-strong-no-regression.log`). The inserted theorem, statement exactly as printed in CHECK-fDH-O §12:

```lean
theorem cert_of_checkW1_of_diffOn' (f : ℂ → ℂ) (hf : DifferentiableOn ℂ f {s : ℂ | s.re < 1})
    (d : W1Data) (hc : checkW1 d = true) (hEncl : W1EnclOK f d) (hAP : RectArgPrinciple f) :
    (1 ≤ d.m → ∃ ρ : ℂ, f ρ = 0 ∧ sigma1 d < ρ.re ∧ ρ.re < sigma2 d
        ∧ T1 d < ρ.im ∧ ρ.im < T2 d) ∧ (d.m = 0 → ∀ s ∈ W1Rect d, f s ≠ 0) := by
```

The body is the unprimed body line for line (220 lines) with exactly one line changed: `exact ⟨ρ, hρ0, lt_trans hhalf hr1, lt_trans hr2 hs2lt1, hi1, hi2⟩` → `exact ⟨ρ, hρ0, hr1, hr2, hi1, hi2⟩`. `hhalf` and `hs2lt1` remain in use elsewhere in the body (the `hAP` application and the `hUsub` block), so no `have` becomes unused and the module compiles without warnings. Docstring: dated, names the source of the obligation, says which theorems are unchanged.

**`lean/Zeta23/W1/FDH.lean`** (176 → 249 lines): (i) `cert_of_checkW1_fDH'` — the f_DH twin of the primed theorem (`cert_of_checkW1_of_diffOn' fDH differentiable_fDH.differentiableOn d hc hEncl (rectArgPrinciple_of_local fDH)`), statement shape of `cert_of_checkW1_fDH` with `sigma1 d < ρ.re ∧ ρ.re < sigma2 d` for `1/2 < ρ.re ∧ ρ.re < 1`; (ii) a new §4 with the four unfolding lemmas of the `mpDH_T1` kind — `mpDH_sigma1 : sigma1 mpDH = 4 / 5`, `mpDH_sigma2 : sigma2 mpDH = 41 / 50`, `arbDH_sigma1`, `arbDH_sigma2` (`show ((4 : ℤ) : ℝ) / ((5 : ℤ) : ℝ) = 4 / 5; norm_num`, etc.) — and the box-form corollaries, statement as specified by the brief step 2:

```lean
theorem mpDH_zero' (hEncl : W1EnclOK fDH mpDH) :
    ∃ ρ : ℂ, fDH ρ = 0 ∧ (4/5 : ℝ) < ρ.re ∧ ρ.re < 41/50 ∧ 1/2 < ρ.re ∧ ρ.re < 1
      ∧ (8569/100 : ℝ) < ρ.im ∧ ρ.im < 8571/100
```

(`arbDH_zero'` likewise from `arbDH_check`), proved from `cert_of_checkW1_fDH'`, `rw` with the four unfolding lemmas, and `lt_trans (by norm_num) hr1` / `lt_trans hr2 (by norm_num)` for the two half-strip clauses; (iii) module doc: one dated bullet in "WHAT IS PROVED HERE" and a dated "σ-STRONG SIBLING" paragraph carrying the box-form label for the primed theorems only. `mpDH_zero`, `arbDH_zero`, `cert_of_checkW1_fDH` and everything in §1–§3 are unchanged.

**Decision recorded (builder's call).** The brief counts "four new names" and "+4 results"; its steps 1–2 name three theorems. The fourth is `cert_of_checkW1_fDH'`, the f_DH instance of the primed generic theorem — the natural intermediate (the unprimed chain is generic → fDH → instances, and the primed chain now mirrors it), and the theorem a reader of `cert_of_checkW1_fDH` expects to find beside it. The four new theorem names are therefore `cert_of_checkW1_of_diffOn'`, `cert_of_checkW1_fDH'`, `mpDH_zero'`, `arbDH_zero'`; the four lemmas `{mp,arb}DH_sigma{1,2}` are plumbing and are probed alongside.

## 2. Checks (all logs in `dr8/`)

* **Build.** `lake build Zeta23` (one lake process, no `-j`; no other compile running — checked with `ps`): *Build completed successfully (9144 jobs)*, 0 errors, 82.7 s wall (14:37:05–14:38:28 IST); no warning or error line names any `W1/` module (the 191 warning lines are upstream deprecation warnings replayed from cached modules). `sigma-strong-build.log`.
* **Axioms.** `#print axioms` on the four new theorems and the four lemmas: every one `[propext, Classical.choice, Quot.sound]`. `#check` of the four statements printed for statement fidelity. `sigma-strong-axioms.log` (probe source appended).
* **No regression.** `#check` + `#print axioms` of the frozen set — the brief's five plus `arbDH_zero`, six names: `cert_of_checkW1`, `cert_of_checkW1_ap`, `cert_of_checkW1_fDH`, `cert_of_checkW1_of_diffOn`, `mpDH_zero`, `arbDH_zero` — BEFORE (14:34, pre-edit oleans, mirror = tree cmp-verified) and AFTER (14:39): NO DIFFERENCE. Plus the source-level byte-identity of the unprimed regions. `sigma-strong-no-regression.log`.
* **Trust greps.** `axiom`, `native_decide`, `unsafe`, `implemented_by`, `extern`, `opaque`, `sorry` (+ `admit`, `ofReduceBool`), comments stripped, on the two edited files: 0 hits (`trust_greps_sigma_strong.py`, `trust_greps_fdh.py` restricted to the two files). Raw grep with comments included also finds nothing. `sigma-strong-trust-greps.log`.
* **Untouched.** All 143 files under `Zeta23/DBN/**` and `comparator/**`: SHA-256 manifest before (14:33) and after (14:39) IDENTICAL; the six `comparator/*` lines of `packaging/hashes.txt` verify. `sigma-strong-untouched.log`. `Instances.lean`, `Ledger.lean`, `ArgPrincipleBridge.lean`, `Format.lean`, `Checker.lean`, `Examples.lean`, `Zeta23.lean` not touched.
* **Mirror.** `Soundness.lean`, `FDH.lean`, `formalization.yaml`: tree = mirror (cmp). Hashes in `hashes-sigma-strong.txt` (with the pre-edit values from commit `d4c7fc4`).

## 3. Label bookkeeping (brief step 4) — box form for the PRIMED theorems only

The box-form sentence (PRICING-fDH.md §3.2, verbatim) — *"f_DH has at least one zero in R = [4/5, 41/50] × [85.69, 85.71] with Re s > 1/2 — kernel-checked modulo the displayed hypothesis H-ENCL_DH (the two producers' enclosures of f_DH on ∂R are true; producers untrusted)."* — now labels `cert_of_checkW1_fDH'`, `mpDH_zero'`, `arbDH_zero'`; the unprimed theorems keep the half-strip label of the D-R8 fix pass. Where it was written (every site dated 2026-09-10, Session 21; insertion-only; content-located anchors, each asserted to match exactly once):

1. `results/d1-m1/FORMAT.md` §9.2 — a second dated block after the D-R8 block (states the primed theorems, the box-form label for them only, that the producers'/checkers'/JSONs' printed label is unchanged, fidelity (m) closed).
2. `lean/README.md` — table rows for `Soundness.lean` (1534 lines) and `FDH.lean` (249 lines); new section "σ-strong sibling (2026-09-10, Session 21)" between the D-R8 and M3-seed sections, with both statements, the checks, and the label.
3. `directions/D1-certified-refutation-arm.md` — the "Next D-R8 item (OWED, not written)" sentence in the 2026-09-10 dated block gets a bold dated DONE note; a dated work-log entry (append-only list); a "SESSION-21 σ-STRONG SIBLING BUILT" frontier paragraph after the SESSION-20 D-R8 paragraph, carrying the refutation-shaped close wording of the brief's "On completion" (KICKSTART 10(c)).
4. `lean/formalization.yaml` — four `status.main_results` entries (14 → 18) for the four new theorems (each `sorry_count: 0`, standard axioms, the box-form label quoted on `mpDH_zero'`); fidelity (m) gets a dated CLOSED sentence (kept in place, append-only); the two `alignment.statements` `lean:` fields (FDH, Soundness) list the primed names. Re-validated with PyYAML + jsonschema against the upstream schema (dispatcher, v0.3, v0.4 re-fetched and IDENTICAL to the on-disk dr8 copies): **errors: 0**; every `Zeta23.*` name in `declaration`/`lean` fields is declared in the mirror (44 names). `sigma-strong-yaml.log`, `validate_yaml_sigma_strong.py`; one dated line appended to `formalization-yaml-jsonschema.log`. Copied to the tree.
5. `results/d1-m2a/packaging/FIDELITY.md` — (m) gets the same dated CLOSED sentence.

**Not touched, by the brief:** the two DH JSON transcripts, `producer_mp.py`, `producer_arb.py`, `checker_ref.py`, `reference_checker.py`, `w1-schema.json` — their printed label describes the checker's acceptance, whose Lean backing is the unprimed theorem. `PRICING-fDH.md` §3.2 is not edited (record item; its "SUPERSEDED" note now reads as history — the box form it carries is again in force, for the primed theorems). No STATUS.md/LOG.md edits (the orchestrator's). No commit by this job — but note that the session's autocommit watchdog committed the in-progress files at `8d5fc38` (14:43) before the yaml script and log reached their final form; the orchestrator's commit lands the final state on top.

## 4. Notes for Job 2 (Opus, clean clone)

* Statement fidelity: the primed generic theorem is character-for-character the CHECK-fDH-O §12 text; the corollaries are the brief's step-2 text (which prints `(4/5 : ℝ) < ρ.re ∧ ρ.re < 41/50 ∧ 1/2 < ρ.re ∧ ρ.re < 1 ∧ (8569/100 : ℝ) < ρ.im ∧ ρ.im < 8571/100`). `#check` prints `4 / 5 < ρ.re ∧ ρ.re < 41 / 50 ∧ 1 / 2 < ρ.re ∧ ρ.re < 1 ∧ 8569 / 100 < ρ.im ∧ ρ.im < 8571 / 100`.
* Box arithmetic: `sigma1 mpDH` unfolds to `((4 : ℤ) : ℝ) / ((5 : ℤ) : ℝ)` (`p1 := 4; q1 := 5` in `Instances.lean` line 2824), `sigma2 mpDH` to `41/50` (`p2 := 41; q2 := 50`); the Arb literal has the same four rationals (lines 2884–2887).
* If `check-o/yaml_o.py` is reused, its `declared()` regex ends in `\b`, which cannot match a name ending in an apostrophe (`\b` between `'` and a space is not a word boundary): the four primed names will print as NOT DECLARED. `dr8/validate_yaml_sigma_strong.py` uses a lookahead instead and is the corrected form.
* The frozen set checked here is six names (the brief's five plus `arbDH_zero`).

## 5. SHA-256 (also `dr8/hashes-sigma-strong.txt`)

```
6881e6dbb40d6d927a2cc8198bcf9ce88b901a46196b6a593dac5116b7ce7496  lean/Zeta23/W1/Soundness.lean        (was aeb8f62e…)
26c323216e7287f2a1e2bab1084276e9237601034c4007c5efbb6a57fc8d2fab  lean/Zeta23/W1/FDH.lean              (was ed6d8892…)
479976cd081e4cd5dab83458e648e85810296a0273069c21fd3ff62f650e70fc  lean/README.md                       (was 9917e357…)
d7b7518968ca6f272ac2b105ba729a1d0c5d20a30041319cb8eec7d65e82eb3c  lean/formalization.yaml              (was 99b77f80…)
59c2069fc8cec3cd706fd17359671729eaeb1a17f24c88665f342166dc98de5a  results/d1-m1/FORMAT.md              (was ccd56d8e…)
ffdd32059e16157676b0241f0b567a721bf67c402a1815bdb3cf4ea06104104d  directions/D1-certified-refutation-arm.md   (was fe024120… at d4c7fc4)
6030b9cc679687ccb2eb30a9df8118f43908d0704325197a6558f4627636c88f  results/d1-m2a/packaging/FIDELITY.md (was dee704cf…)
3afb20f0bf8a34369a77e021536800002cfcfdc74579f38dd86a9249e2d21db7  results/d1-m2a/dr8/formalization-yaml-jsonschema.log (was bdb3274b…)
5d5269a4c4ca310b8fa43231f3dc05fca99a96055a931a390bcff14c0168e4d6  results/d1-m2a/dr8/sigma-strong-axioms.log
9dd79fdbb0da88e266fbaf49aa4226f081db0fa8e12c6202fa60cc1c2eefd27c  results/d1-m2a/dr8/sigma-strong-no-regression.log
4f1fd8fbea8d068213797af5c5364f42603ad239e4a10dbc15fea4aa5d40ed38  results/d1-m2a/dr8/sigma-strong-trust-greps.log
395765d577c8e47b6ef56d7d51a6c757016b8891084ac99591c82e8ecfff6d1c  results/d1-m2a/dr8/sigma-strong-untouched.log
7e9b2325c947cadbea2fd678684c73b6c1cabcc1ee417fc7ada581bbea2717ee  results/d1-m2a/dr8/sigma-strong-build.log
4b5969fe8b9a24b28fce8ab30bb42507b3bcbcc0c67015357028722ce086adc7  results/d1-m2a/dr8/sigma-strong-yaml.log
85350db78d2d202f9ce3f92abbec4c3631eea158fb212eb763a3b6878501c738  results/d1-m2a/dr8/trust_greps_sigma_strong.py
f68bc574631a5eb75de2c5d3e655ea7e1bcaf51cde07c26a57777acd16e759b1  results/d1-m2a/dr8/validate_yaml_sigma_strong.py
```
`hashes-sigma-strong.txt` itself and this file are hashed in the final report and in LOG.md at the commit.
