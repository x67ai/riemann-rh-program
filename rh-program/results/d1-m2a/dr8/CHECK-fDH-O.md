# D-R8 independent check — `cert_of_checkW1_fDH` + the M3 seed ledger (Session 20, Job 2, Opus 5)

**Checker:** Claude Opus 5 (1M), 2026-09-10, KICKSTART 10(f) second model. Brief of record:
`results/d1-m2a/dr8/BUILD-BRIEF-fDH.md` (Job 2 paragraph + the 02:47 addendum). Pricing of record:
`PRICING-fDH.md` (§1.1 the object, §1.3 the convention, §3.1 the BINDING statement shape, §3.2 the
only label) and `PRICING-M3-ledger.md` (§1–§2). Everything below is RE-DERIVED with my own scripts
and my own clean-clone build; Job 1's scripts are read only to know what was claimed, never run in
place of my own. Scripts and raw logs: `results/d1-m2a/dr8/check-o/`. Written as the work lands
(RULE ONE).

**Status line:** COMPLETE. §0 clean-clone provenance · §1 build (9144 jobs, 0 errors, 0 program
warnings) · §2 axioms (112 declarations) · §3 κ (4 routes, 80 digits) · §4 convention · §5 statement
fidelity (0 divergences) · §6 no-regression · §7 untouched · §8 M3 seed · §9 label sweep · §10 trust
greps · §11 formalization.yaml · §12 findings.
**VERDICT: FIX-FIRST** — 3 label/documentation fixes + 1 hash-record fix, all in §12 with exact
text; the theorem, the proofs, the transcripts and the seed ledger are sound and independently
re-derived.

## 0. Setup, provenance of the tree I checked

**Tree checked.** Clean clone `~/rh-lean-work/checker-clone-s20/` (upstream tag v1.0 + the mirror at
`a4a14f6f`, built during the packaging check), overlaid with the CURRENT mirror `rh-program/lean/`
at git commit **`5fe6aa279ba68de83dfa737530810da1d26d62f3`** (`5fe6aa2`, "D-R8 Job 1 harvested; Job 2
launching"). Toolchain `leanprover/lean4:v4.33.0-rc2`, Mathlib `51e6992efd06126df61a496bebf8f49482a4e129`
(verified by `git -C .lake/packages/mathlib rev-parse HEAD` in the clone itself).

**What the overlay actually changed** (my own file-by-file `cmp` of all 143 mirror files against the
clone BEFORE copying — `check-o/overlay-plan.txt`): exactly **six** paths, and no others.

```
NEW      formalization.yaml
NEW      Zeta23/W1/FDH.lean
NEW      Zeta23/W1/Ledger.lean
CHANGED  README.md
CHANGED  Zeta23.lean
CHANGED  Zeta23/W1/Soundness.lean
```

Every other mirror file — all of `Zeta23/DBN/**`, all of `comparator/**`, `Instances.lean`,
`ArgPrincipleBridge.lean`, `Format.lean`, `Checker.lean`, `Examples.lean` — was **already
byte-identical** in a clone that predates this work. That is an independent confirmation of Job 1's
"untouched" claim that does not go through any hash file. Post-overlay SHA-256 of the five Lean/YAML
files equals `hashes-fdh.txt` line for line.

**The pre-change baseline is mine.** Before the overlay I ran, on the clean clone,
`#check @Zeta23.W1.cert_of_checkW1_ap` and `#print axioms` (`check-o/before_ap.lean`,
`check-o/no-regression-before.out`, 10.4 s). That is my own "before", not Job 1's `no-regression.log`.

Load discipline: `ps -Ao pcpu,comm | awk '$1>50'` empty before every build; one `lake` process
throughout. `caffeinate` and both watchdogs running.

## 1. Cold build of the overlaid clone — PASS

`lake build Zeta23` from the changed modules: **Build completed successfully (9144 jobs)**,
**79 s** wall (300.6 s user, 616 % CPU), started 03:50:50, ended 03:52:09
(`check-o/build-zeta23.log`, 878 lines).

* **Errors: 0.** The two lines matching `error` are the module name
  `Zeta23.XiPrime.ExplicitFormula.EntryError` and its file path — not diagnostics.
* **Warnings from any program module (`Zeta23/W1/**`, `Zeta23/DBN/**`, `comparator/**`): 0.**
  All 247 warnings are upstream Zeta23 deprecations (`Set.mem_setOf_eq`, `ENat.toNat_coe`,
  unreferenced binder names) in `Statement.lean`, `Assembly.lean`, `ZeroSide/**`,
  `FromPNTPlus/**`, `RvM/**`, `WeilEF/**`, `ThmE/**`, `XiPrime/**`.
* The four W1 modules built (not replayed) in order — `Soundness` 5.2 s, `ArgPrincipleBridge` 1.6 s,
  `Ledger` 1.6 s, `FDH` 1.7 s — and the whole DBN cascade (`BarrierCert` and the 116
  `Instance02.*` modules) rebuilt behind them and succeeded. So the generalization of
  `Soundness.lean` does not break a single downstream DBN module.

## 2. `#print axioms` — my own probe over every top-level declaration — PASS

Not Job 1's list: I stripped the (nested) block and line comments from `FDH.lean`, `Ledger.lean`
and `Soundness.lean` with my own parser and took **every** `theorem`/`lemma`/`def`/`abbrev`
declaration it found — 11 + 8 + 79 = 98 names — then added `cert_of_checkW1_ap`,
`rectArgPrinciple_riemannZeta`, the ten `_check` literals and `mpDH`/`arbDH`: **112 declarations**,
all probed in one file (`check-o/axioms_probe.lean`; full log
`results/d1-m2a/dr8/CHECK-fDH-O-axioms.log`, 2.1 s, exit 0).

| axiom set | count |
|---|---|
| `[propext, Classical.choice, Quot.sound]` | 87 |
| `[propext, Quot.sound]` | 2 |
| `[propext]` | 19 |
| "does not depend on any axioms" | 4 (`consecPairs`, `consecPairs_map`, `mpDH`, `arbDH`) |

112 = 87 + 2 + 19 + 4, so nothing was silently skipped. **Every set is a subset of the three
standard axioms.** No `sorryAx`, no `Lean.ofReduceBool` (i.e. no `native_decide` anywhere in the
dependency cone), no `Classical.em` as a separate axiom, no program-declared `axiom`. In particular

* `cert_of_checkW1_fDH`, `mpDH_zero`, `arbDH_zero`, `differentiable_fDH`,
  `hasSum_hurwitzZeta_one_fifth`, `cert_of_checkW1_of_diffOn`,
  `continuousOn_logDeriv_seg_of_diffOn`, `cert_of_checkW1`, `cert_of_checkW1_ap` and all eight
  `_exclusion` corollaries: `[propext, Classical.choice, Quot.sound]`;
* the ten `by decide +kernel` literals (`mpDH_check`, `arbDH_check`, the eight `*Null*_check`):
  `[propext]` — kernel reduction, not `native_decide`.

## 3. κ — four independent routes, 80 digits — PASS

My own script (`check-o/kappa_o.py`, log `check-o/kappa-o.log`); Job 1's `kappa_check.py` was
neither imported nor run. mpmath at `mp.dps = 80`.

| route | how | κ (60 digits) |
|---|---|---|
| A contract | the line `kap = (sqrt(10-2*sqrt5) - 2)/(sqrt5 - 1)` located by regex in **both** `results/d1-m1/FORMAT.md` and `results/ccm-dh-test/dh.py` (found verbatim in both), evaluated | 0.284079043840412296028291832393126169091088088445737582759163 |
| B Lean | `def kappaDH : ℝ := …` re-read by regex from `lean/Zeta23/W1/FDH.lean`; identifiers restricted to `Real.sqrt` (nothing else appears); Lean juxtaposition rewritten to Python calls by my own mini-parser | identical |
| C Gauss sum | χ mod 5 built from χ(2) = i on the primitive root 2 (χ(1)=1, χ(2)=i, χ(3)=−i, χ(4)=−1); τ(χ) = Σ χ(a)e^{2πia/5} = −1.17557… + 1.90211…i, \|τ\| = √5 exactly; ε = τ/(i√5), \|ε\| = 1; κ = tan(arg ε / 2) | identical |
| D dh.py | the body of `dh.py`'s `kappa()` re-read by regex and `exec`'d in an empty namespace (not imported) | identical |

Pairwise: A = B = D to the last bit (difference exactly 0); the Gauss-sum route agrees with all
three to **2.6·10⁻⁸¹**. The demand was ≥ 30 digits; this is > 50 by construction and ~80 in fact.
Guards: radicand 10 − 2√5 = 5.52786… > 0, denominator √5 − 1 = 1.23607… ≠ 0, so no `Real.sqrt`
junk value and no division by zero enters `kappaDH`. Leading digits 0.28407904…, as PRICING §1.1.
**This equals Job 1's figure to all 60 digits it printed.**

## 4. The Hurwitz convention — PARTLY A LEAN THEOREM, and I say which part

The brief asks whether the Mathlib-vs-mpmath-vs-Arb identification is a proof or a meta-level
identification. The honest answer has two halves, and Job 1's file states it correctly.

**(a) Proved in Lean.** Mathlib `51e6992e`, `Mathlib/NumberTheory/LSeries/HurwitzZeta.lean:72`
(read at the source in the clone's own `.lake/packages/mathlib`):

```lean
lemma hasSum_hurwitzZeta_of_one_lt_re {a : ℝ} (ha : a ∈ Icc 0 1) {s : ℂ} (hs : 1 < re s) :
    HasSum (fun n : ℕ ↦ 1 / (n + a : ℂ) ^ s) (hurwitzZeta a s)
```

`FDH.lean` instantiates it at a = 1/5 as `hasSum_hurwitzZeta_one_fifth`. I re-elaborated the same
instantiation **at all four shifts a = 1/5, 2/5, 3/5, 4/5** on the built tree, plus
`((1/5 : ℝ) : UnitAddCircle) ≠ ((2/5 : ℝ) : UnitAddCircle)`, plus `kappaDH = …` and
`∀ s, fDH s = …` by `rfl` against the FORMAT §9.2 combination
(`check-o/convention_probe.lean`, `check-o/convention-probe.out`, exit 0, no errors). So **pricing
risk R3 is closed by proof, not by inspection**: the four `UnitAddCircle` casts really are the
reals 1/5, 2/5, 3/5, 4/5 (confirmed again by `#print` under `pp.numericTypes`, which shows
`hurwitzZeta (↑(1 / 5 : ℝ)) s` and so on), and Lean's `fDH` really is
Σ-series-based on Re s > 1 with the shifts in the contract's order and signs.

**(b) META-level, and it cannot be otherwise.** That the two producers' *library calls* compute
that same series is not a Lean statement. I checked it at the source and numerically:

* `results/d1-m1/hurwitz_encl.py` STEP 3′ (lines 20–21): "`zeta(s, a) := sum_{n=0}^{infty}
  (n+a)^{-s}` for sigma > 1, continued elsewhere", continued by Euler–Maclaurin on
  {σ > −2m, s ≠ 1}, with "mpmath's `mp.zeta(s, a)` implements this same continuation" as the
  cross-check target (STEP 4′) — same series, same a-normalization.
* `producer_mp.py` `f_dh_ball` (lines 133–141): `h1 + h2.scale_iv(k) - h3.scale_iv(k) - h4` times
  `pow_int_neg(5, s)`, with `h_j = hurwitz_ball(s, Fraction(j, 5))` — the contract's shifts, order
  and signs exactly. `producer_arb.py` `eval_fdh` (lines 241–247): `s.zeta(acb(rat_ball(j/5)))`,
  same combination, `acb(5) ** (-s)` factor.
* **Numeric re-derivation** (`check-o/convention_o.py`, log `check-o/convention-o.log`, exit 0):
  at s ∈ {2, 3+i, 1.5+10i, 4−2.5i} and a ∈ {1/5, 2/5, 3/5, 4/5} I built Σ_{n≥0}(n+a)^{−s} myself
  as an exact head plus an Euler–Maclaurin tail (`mp.sumem` — a different mpmath entry point from
  `mp.zeta`, so agreement is evidence about the convention rather than about one implementation
  agreeing with itself) and compared with `mp.zeta(s, a)` and with python-flint
  `acb(s).zeta(acb(a))` (= Arb `acb_hurwitz_zeta`). All 16 cells agree; `mp.zeta` vs Arb agree to
  10⁻³⁸–10⁻⁴⁰, my EM route to 10⁻⁴⁹ except at s = 1.5 + 10i where `mp.sumem`'s own floor is
  1.3·10⁻²⁹ (identical for all four a, and it does not move with the truncation point — an
  accuracy floor, not a convention gap). A wrong convention (n ≥ 1 instead of n ≥ 0, a ↦ 1 − a, an
  unnormalized shift) moves the first digits, not the twentieth. The four assembled f_DH values
  agree to 10⁻⁵¹.

**Verdict on the convention: correct, and correctly labeled.** `FDH.lean`'s header calls the
identification "META-level, not a Lean theorem" and `formalization.yaml`'s divergence (l) repeats
it. That is the honest description: half (a) is a Mathlib theorem the file consumes, half (b) is a
documented convention match of exactly the same standing as "mpmath's `zeta(s)` is Mathlib's
`riemannZeta`" on the ζ leg — which is where H-ENCL_DH's meaning lives.

## 5. Statement fidelity against PRICING §3.1 — ZERO divergences

`check-o/fidelity_o.py` (log `check-o/fidelity-o.log`) lifts the binding objects out of the
pricing's own fenced blocks by regex and compares them character by character with the declarations
lifted out of `FDH.lean` (runs of whitespace normalized to one space — Lean line breaks carry no
meaning; every other character must match). For `def`s the WHOLE declaration is compared, body
included, because for `fDH` and `kappaDH` the body is the object under audit; for `theorem`s the
statement is compared (the proof term is the builder's business; the pricing binds the shape).

| object | result |
|---|---|
| `kappaDH` (77 chars, body included) | **IDENTICAL** |
| `fDH` (247 chars, body included) | **IDENTICAL** |
| `cert_of_checkW1_fDH` (214 chars) | **IDENTICAL** |
| `mpDH_zero` (132 chars) | **IDENTICAL** |
| `arbDH_zero` | is `mpDH_zero` with `mpDH` → `arbDH` and nothing else (the pricing says "and `arbDH_zero` likewise") |

The elaborated forms confirm it (`CHECK-fDH-O-axioms.log`): `cert_of_checkW1_fDH` is
`cert_of_checkW1_ap` with `riemannZeta` replaced by `Zeta23.W1.fDH` and `RectArgPrinciple`
discharged, and `cert_of_checkW1_of_diffOn` is the same statement universally quantified over
`f` with `DifferentiableOn ℂ f {s | s.re < 1}`.

### 5.1 The numeric box, against the transcripts, with my own parser

My parser reads the `rect` of each DH transcript, the `W1Data` literal's `p1 q1 p2 q2 a1 b1 a2 b2 m`
out of `Instances.lean`, and the rationals written into the corollary statements — three
independent readings — and compares all three. **12 checks per leg, 24 in all, all OK:**

```
transcript rect : sigma1 4/5  sigma2 41/50  T1 8569/100  T2 8571/100  claimed_m 1  function f_DH  mode refutation
Lean W1Data lit : p1/q1 4/5  p2/q2 41/50  a1/b1 8569/100  a2/b2 8571/100  m 1
corollary box   : 8569/100 < Im rho < 8571/100 ;  1/2 < Re rho < 1
```

identical on both legs. The corollary's `8569/100` and `8571/100` are the transcript's `T1`, `T2`
exactly; `mpDH_T1 … mpDH_T2` are proved by `show ((8569 : ℤ) : ℝ) / ((100 : ℤ) : ℝ) = 8569/100`,
which only elaborates if the literal's `a1/b1` really are those integers — so the identification of
the printed box with the literal's box is itself kernel-checked, not eyeballed.

### 5.2 One divergence that is NOT between §3.1 and the Lean file — it is between §3.1 and §3.2

See FIX-FIRST 1 in §12. In short: the theorem delivers `1/2 < ρ.re ∧ ρ.re < 1`, and the binding
label says the zero is "in R = [4/5, 41/50] × [85.69, 85.71]". R is a strict subset of that
half-strip, so the label states more than the theorem does.

## 6. No regression on `cert_of_checkW1_ap` — PASS, against my own baseline

`check-o/no-regression-before.out` (clean clone, before the overlay) vs the same `#check` after
(`CHECK-fDH-O-axioms.log`): the two statements are **identical token for token**, and so are
`cert_of_checkW1`'s and both axiom sets (`[propext, Classical.choice, Quot.sound]`).

```
Zeta23.W1.cert_of_checkW1_ap : ∀ (d : Zeta23.W1.W1Data),
  Zeta23.W1.checkW1 d = true →
    Zeta23.W1.W1EnclOK riemannZeta d →
      (1 ≤ d.m → ∃ ρ, riemannZeta ρ = 0 ∧ 1 / 2 < ρ.re ∧ ρ.re < 1 ∧ Zeta23.W1.T1 d < ρ.im ∧ ρ.im < Zeta23.W1.T2 d) ∧
        (d.m = 0 → ∀ s ∈ Zeta23.W1.W1Rect d, riemannZeta s ≠ 0)
```

`ArgPrincipleBridge.lean` is byte-identical to the pre-work clone (§0), so the ζ-side statement of
record has not moved: `cert_of_checkW1` is now proved as an instance of the generic
`cert_of_checkW1_of_diffOn` at `f = riemannZeta`, and its statement and its docstring survive that
unchanged. The 116-module DBN cascade re-elaborated on top of it (§1).

## 7. DBN and comparator untouched — PASS, three ways

`check-o/untouched_o.py` (log `check-o/untouched-o.log`):

1. every line of `results/d1-m2a/packaging/hashes.txt` re-verified against disk: **24 of 26 OK**;
   the two that changed are `lean/formalization.yaml` (this build, by design) and
   `results/d1-m2a/packaging/FIDELITY.md` (changed earlier in Session 20, commit `34c0332`) —
   see MINOR 3;
2. the eight "Current (fix pass r2)" hashes of `lane-a/EMIT-NOTES.md` §5 — the four DBN modules,
   the two lane-a JSONs, the emitter and the back-parser: **8 of 8 OK**;
3. the strong leg: **127 mirror files** under `Zeta23/DBN/**` and `comparator/**` compared with the
   clean clone, which was built from upstream v1.0 + mirror `a4a14f6f` **before any of this work
   existed** — **0 differ**, and the overlay touched exactly six paths, none of them under
   `Zeta23/DBN/` or `comparator/`. This leg consults no hash file the builder could have written.

## 8. The M3 seed ledger — PASS

**Job 1's `ledger_check.py` re-run by me** (`check-o/ledger-check-rerun.log`): exit 0, 4 rows,
**0 findings**, `sha256 ok` ×8, both Python checkers ACCEPT on all eight transcripts, four
cross-checks CONSISTENT (83 / 158 / 2 547 / 90 overlap pairs), all Lean names found. It regenerates
`index.json`; `git status` after the run is clean, so the committed index is byte-stable — the
property §1.3 claims.

**My own independent re-derivation** (`check-o/seed_o.py`, log `check-o/seed-o.log`), which imports
neither `ledger_check.py` nor `seed_rows.py`:

| what | count | result |
|---|---|---|
| legs checked | 8 | all |
| transcript SHA-256 + byte count recomputed from disk vs `ROW.json` | 8 | 8 OK |
| the same vs the table in `PRICING-M3-ledger.md` §2 (lifted out of the markdown by regex) | 8 | 8 OK |
| row box vs the transcript's own `rect` | 8 | 8 OK |
| row box vs the `W1Data` literal in `Instances.lean` — i.e. the set `W1Rect <literal>` that the corollary actually quantifies over | 8 | 8 OK |
| `segments` / `K` / `A` / `claimed_m` vs the transcript | 8 | 8 OK |
| winding sums recomputed by summing `argLo`/`argHi` over the transcript's own segments vs the row's `winding_lo_hi` | 8 | 8 OK ([−24, 28], [−14, 13], [−41, 40], [−29, 36], [−679, 637], [−495, 488], [−28, 30], [−16, 14]) |
| `_exclusion` corollary present **in PRICING-M3-ledger §1.6's exact shape**, on the right literal, m = 0 branch | 8 | 8 OK |
| literal's `m` = 0 | 8 | 8 OK |
| δ₀ = σ₁ − ½ exactly (Fraction arithmetic); ½ < σ₁ ≤ σ₂ < 1 (clause C2) | 4 rows | 4 OK |
| `function`/`mode`/`claimed_m`/`grade`/`status`/`provenance.kind` | 4 rows | 4 OK |
| `index.json` entries identical to the four `ROW.json` files; no aggregate field (§1.5) | — | OK |

The eight `_exclusion` statements elaborate to exactly `W1EnclOK riemannZeta <lit> → ∀ s ∈ W1Rect
<lit>, riemannZeta s ≠ 0` (`CHECK-fDH-O-axioms.log`) on the three standard axioms — one displayed
hypothesis, one box, nothing else. The two deviations Job 1 declares (the single-box `sentence`
instead of §1.4's range form, and the `embedded_trust_label` field) are both moves toward honesty
and I endorse them: §4.1 of the same pricing does say the range form needs a box family reaching
σ = 1, and every one of these boxes stops at σ₂ < 1.

## 9. The label sweep — PASS, with two stale sentences (§12)

**(a) The §3.2 sentence, verbatim, everywhere it is printed** (`check-o/fidelity-o.log` part C,
`check-o/labels-o.log`): present, character for character, exactly once, in all twelve of
`w1-schema.json`, `producer_mp.py`, `producer_arb.py`, `checker_ref.py`, `reference_checker.py`,
both DH JSONs, `FDH.lean`, `formalization.yaml`, `FORMAT.md`, `lean/README.md` and the D1 direction
file — and in `acceptance-report.md` too. Every one of those files carries a dated 2026-09-10 block.

**(b) The never-say phrases, over the text that is actually NEW.** The right scope is not the
repository (which is full of history, journals and external sources) but the lines this build
**added**: 5 345 added lines across 66 files, excluding my own outputs
(`check-o/newtext-neversay.log`). Searching those added lines for "RH-for-DH disproved", "RH for DH
disproved", "fully machine-checked", "machine-checked disproof", "disproof of RH", "RH is false",
"RH disproved", "RH for DH is disproved", "refutes RH", "RH refuted": **11 hits, every one of them
a negation or a never-say list** — `Never "RH-for-DH disproved"` (D1 direction), `not
"fully machine-checked"` (formalization.yaml, FORMAT §9.2), `not "RH-for-DH machine-checked
disproof"` (lean/README.md, FORMAT §9.2), `never "RH-for-DH disproved", never "fully
machine-checked"` (acceptance-report §0), the `d1-m3/README.md` never-say list, and BUILD-NOTES
reporting that fact. **No new line asserts any of them.**

**(c) The edited producer/checker/schema files: only strings changed? — one exception, benign.**
Diff against the pre-sweep tree (`git log --follow` puts the sweep in autocommits `5348faa` and
`1587876`; base `71ce55a5`), full diff in `check-o/label-sweep-code-diff.txt`:

* `w1-schema.json` — the `f_DH` `trust_label` `const`, plus a top-level `$comment` (a JSON-Schema
  keyword, not a transcript field). **String only.**
* `producer_mp.py`, `producer_arb.py`, `checker_ref.py` — one dictionary value each
  (`TRUST_LABELS["f_DH"]` / `_LABELS["f_DH"]`) plus a trailing `#` comment. **String only.**
* `reference_checker.py` — the same constant, **plus a real two-line code change** in `run_file`:
  the non-ζ ACCEPT banner was a hand-concatenated copy of the old label and is now
  `TRUST_LABELS.get(str(doc.get('function')), 'unknown function')`. I traced `label`: it occurs
  only in the `print(f'   VERDICT: ACCEPT …')` on the next line and nowhere else in the file, so no
  check, no parse and no verdict is affected. The change removes a second copy of the label — the
  laundering hazard AUDIT-O MINOR-1 was about — and I endorse it, but it is a logic change and the
  record should say so rather than "only label/comment strings changed".
* Style note, not a defect: in all four Python files the amending `#` comment now sits where the
  dictionary entry's terminating comma used to be, so the comma lives inside the comment. The files
  parse (both checkers ran), but adding an entry after that line would be a syntax error.

**(d) The two DH transcripts: `trust_label` and `comment` ONLY** (`check-o/dh-json-delta.log`, my
own key-by-key JSON comparison against the pre-sweep blobs): every other field — `format`,
`version`, `mode`, `function`, `rect`, `scales`, `claimed_m`, `mesh`, all 40 / 50 `segments`,
`modulus_floor`, `producer` — is identical object-for-object. The Arb leg gained a `comment` key
(schema-optional; it had none).

**(e) Both checkers re-run by me on both DH JSONs** — `reference_checker.py`: ACCEPT, ACCEPT
(C1–C11 each, exit 0), and the banner now prints the §3.2 sentence; `checker_ref.py`: ACCEPT,
ACCEPT (exit 0); `acceptance/crosscheck.py` on the DH pair: **CONSISTENT, 122 overlap pairs**.
And the amended schema still validates everything: both DH JSONs **0 errors**, and all eight ζ
null transcripts **0 errors** (their v1.0 `zeta` label constant is untouched).

## 10. Trust greps, comments stripped, my own stripper — PASS

`check-o/trustgreps_o.py` (log `check-o/trustgreps-o.log`). My stripper removes NESTED `/- … -/`
blocks and `--` line comments and blanks string literals as well (a forbidden token inside a string
would otherwise read as code). Over `FDH.lean`, `Ledger.lean`, `Soundness.lean`,
`ArgPrincipleBridge.lean`, `Format.lean`, `Checker.lean`, `Instances.lean`, `Zeta23.lean`
(5 610 lines): **0 hits** for `axiom`, `native_decide`, `unsafe`, `implemented_by`, `@[extern`,
`opaque`, `sorry`, `admit`, `ofReduceBool`, `trustCompiler`, `partial`, `macro_rules`/`elab`.

`decide` in code: `Instances.lean` 12 × `decide +kernel` (the checker evaluations),
`Checker.lean` 32 (inside the decidability plumbing), `FDH.lean` 2 and `Ledger.lean` 8 — the
`(by decide)` discharging `1 ≤ mpDH.m` and `<lit>.m = 0`, three-token integer facts. This matches
the axiom evidence: no `Lean.ofReduceBool` anywhere in the 112-declaration probe.

## 11. `formalization.yaml` — PASS

`check-o/yaml_o.py` (log `check-o/yaml-o.log`). PyYAML 6.0.3 + jsonschema 4.25.1, Draft 2020-12,
against the schema **fetched fresh from upstream in this run** (retry loop) rather than from a
local copy:

* dispatcher `…/formalization.yaml/main/schema/formalization.schema.json`, sha256 `22bd0b61…`;
  `$ref`s `v0.3.schema.json` (`93247a80…`) and `v0.4.schema.json` (`25ff6b25…`). All three of the
  builder's on-disk copies (`dr8/` and `packaging/`) are **identical to what upstream serves now**.
* **Validation errors: 0.** 14 `status.main_results`, 19 `alignment.statements`,
  `fidelity.divergences` 6 392 characters.
* **The new entries name declarations that exist.** I extracted every `Zeta23.*` identifier from
  `status.main_results` and `alignment.statements` (51 of them) and looked each up in the mirror by
  its declaration keyword: all 39 declaration names resolve to a file, including every new one —
  `cert_of_checkW1_fDH`, `mpDH_zero`, `arbDH_zero`, `differentiable_fDH`, `fDH`, `kappaDH`,
  `cert_of_checkW1_of_diffOn`, `continuousOn_logDeriv_seg_of_diffOn`, `rectArgPrinciple_of_local`,
  `cert_of_checkW1_ap` and all eight `*_exclusion`. The remaining 12 are MODULE names
  (`Zeta23.W1.FDH`, `Zeta23.DBN.Defs`, …), each with its `.lean` file present — not a finding.
* Divergence **(l)** says what §4 of this report says: the f_DH identification is meta-level, κ is
  a checked transcription, `W1Data` carries no function tag, the ledger corollaries license the
  single-box sentence only. I agree with every clause.

## 12. Findings and verdict

Everything the brief asked me to re-derive came out right: the build, the axioms, κ, the
convention, the statements, the boxes, the no-regression, the untouched manifest, the seed ledger,
the label sweep, the trust greps and the YAML. Nothing here is a mathematical error, and nothing
here threatens the theorem. What I found are four places where a **printed sentence says more, or
something older, than the machine-checked object it labels** — which is the exact defect class this
whole item exists to remove, so they are FIX-FIRST rather than notes.

### FIX-FIRST 1 — the binding label claims membership in R; the theorem does not deliver it

**What is wrong.** PRICING §3.2, used verbatim in twelve places, opens: *"f_DH has at least one
zero **in R = [4/5, 41/50] × [85.69, 85.71]** with Re s > 1/2 …"*. The theorems say:

```
mpDH_zero : W1EnclOK fDH mpDH → ∃ ρ, fDH ρ = 0 ∧ 1/2 < ρ.re ∧ ρ.re < 1 ∧ 8569/100 < ρ.im ∧ ρ.im < 8571/100
```

`85.69 < Im ρ < 85.71` is the box's Im-range, but `1/2 < Re ρ < 1` is **not** `4/5 ≤ Re ρ ≤ 41/50`:
R is a strict subset of that half-strip, so "in R" is not what the kernel checked. The sentence is
mathematically true — `Soundness.lean` line 1173–1175 obtains `hρmem : ρ ∈ rectOpen (sigma1 d)
(sigma2 d) (T1 d) (T2 d)` and then deliberately weakens it,
`exact ⟨ρ, hρ0, lt_trans hhalf hr1, lt_trans hr2 hs2lt1, hi1, hi2⟩` — but the label must be what
the statement says, not what the proof happens to know.

**Exact fix (recommended; strengthens rather than weakens, and preserves every frozen statement).**
In `Zeta23/W1/Soundness.lean`, beside `cert_of_checkW1_of_diffOn`, add the σ-strong variant whose
witness branch keeps `hr1`/`hr2`:

```lean
theorem cert_of_checkW1_of_diffOn' (f : ℂ → ℂ) (hf : DifferentiableOn ℂ f {s : ℂ | s.re < 1})
    (d : W1Data) (hc : checkW1 d = true) (hEncl : W1EnclOK f d) (hAP : RectArgPrinciple f) :
    (1 ≤ d.m → ∃ ρ : ℂ, f ρ = 0 ∧ sigma1 d < ρ.re ∧ ρ.re < sigma2 d
        ∧ T1 d < ρ.im ∧ ρ.im < T2 d) ∧ (d.m = 0 → ∀ s ∈ W1Rect d, f s ≠ 0)
```

— the body is the existing one with `exact ⟨ρ, hρ0, hr1, hr2, hi1, hi2⟩` in place of the
`lt_trans` line; then restate `mpDH_zero` / `arbDH_zero` as
`… ∧ (4/5 : ℝ) < ρ.re ∧ ρ.re < 41/50 ∧ 1/2 < ρ.re ∧ ρ.re < 1 ∧ (8569/100 : ℝ) < ρ.im ∧ ρ.im <
8571/100` (two `show … ; norm_num` unfolding lemmas of the `mpDH_T1` kind for `sigma1 mpDH`,
`sigma2 mpDH`). `cert_of_checkW1`, `cert_of_checkW1_ap` and `cert_of_checkW1_fDH` keep their
statements character-for-character, so the no-regression requirement is untouched; the cascade
rebuild is the same 79 s.

**Cheaper alternative if the Lean statements are to be frozen:** amend the §3.2 sentence's first
clause everywhere (one string, already centralized in twelve files) to
*"f_DH has at least one zero ρ with 1/2 < Re ρ < 1 and 85.69 < Im ρ < 85.71 — the transcript's
rectangle being R = [4/5, 41/50] × [85.69, 85.71] — kernel-checked modulo …"*. That is exactly the
theorem, and it loses nothing a reader needs.

### FIX-FIRST 2 — `reference_checker.py`'s AUDIT-O comment is now false in the present tense

`results/d1-m1/reference_checker.py` lines 246–248, immediately above the amended banner:

> `# AUDIT O MINOR-1 (applied at reconciliation 2026-09-02): the banner names the function's own`
> `# trust label (FORMAT.md sec. 9.2, D-R8) -- an f_DH acceptance is checker-level only and`
> `# carries no H-AP-backed conclusion.`

Both halves of the last sentence are now wrong: an f_DH acceptance is no longer checker-level only,
and H-AP is not assumed at all (`rectArgPrinciple_of_local` proves it for every `f`). The file's own
constant three lines away already carries the new label, so the file contradicts itself.

**Exact fix.** Replace that trailing sentence with:
`-- [Amended 2026-09-10 (Session 20, D-R8): an f_DH acceptance now backs the Lean theorem`
`-- Zeta23.W1.cert_of_checkW1_fDH modulo the displayed H-ENCL_DH only (H-AP is a theorem for every`
`-- f, rectArgPrinciple_of_local); the banner prints TRUST_LABELS[function], the schema constant.]`
Comment only; no re-run needed beyond the two checker invocations already scripted.

### FIX-FIRST 3 — `Instances.lean`'s module doc still says there is no theorem about f_DH

`lean/Zeta23/W1/Instances.lean` lines 33–34 (and its source `results/d1-m1/instances-doc.txt`
lines 21–22):

> `* For the two f_DH live-fire transcripts (mpDH, arbDH) there is NO theorem about f_DH at all:`
> `  they are checker-level true-positive firing tests (D-R8); …`

Job 1 lists this in "Owed" item 2 and left it deliberately, reasoning that the file is
emitter-written and back-parse-verified. That reasoning covers the `W1Data` literals; it does not
cover a module docstring, which is a comment and cannot affect the back-parse or any hash the
packaging depends on (`Instances.lean` is not among `comparator/**`, so
`packaging/hashes.txt` is unaffected). It is the single most-read false sentence left by this build:
a referee opening the file that defines `mpDH` is told there is no theorem about f_DH on the same
screen where `FDH.lean` proves one.

**Exact fix.** Insert one dated line after line 34 of `lean/Zeta23/W1/Instances.lean` and after
line 22 of `results/d1-m1/instances-doc.txt` (edit the `.txt` first so a future re-emission keeps
it): `* [2026-09-10, D-R8] Superseded: Zeta23/W1/FDH.lean now proves cert_of_checkW1_fDH and the`
`  instance corollaries mpDH_zero / arbDH_zero on these two literals, modulo the displayed`
`  H-ENCL_DH only. The literals below are unchanged.` Then re-run
`recon_instances_verify.py` (expected: 0 mismatches, as the literals do not move) and record the new
`Instances.lean` hash.

### MINOR 4 — `packaging/hashes.txt` now has two lines that no longer verify

Re-verified line by line (§7): `lean/formalization.yaml` (`eb798527…` recorded, `89475ddb…` on
disk — changed by this build, correctly) and `results/d1-m2a/packaging/FIDELITY.md` (`da045cd8…`
recorded, `b0927f5c…` on disk — changed earlier in Session 20 by commit `34c0332`, before D-R8).
Nothing is wrong with either file; what is wrong is that the packaging's own hash record silently
fails today, which is the situation standing order 5 exists to prevent.

**Exact fix.** Append to `results/d1-m2a/packaging/hashes.txt`:
`# [2026-09-10, Session 20] Two lines above are superseded: lean/formalization.yaml -> 89475ddb…`
`# (D-R8 build, dr8/hashes-fdh.txt) and packaging/FIDELITY.md -> b0927f5c… (item (k), commit`
`# 34c0332). The six comparator/* lines and every other line still verify.`

### Non-findings I record so the next session does not re-litigate them

* The two DH JSONs still contain the superseded v1.0 string — inside the *dated note appended to
  the `comment` field*, quoting what the label was. That is correct practice, not a leftover.
* `LEDGER.md` is dated 2026-09-09, not 2026-09-10: the rows' `added_utc` is UTC and the landing was
  03:4x IST. Consistent, and Job 1 says so.
* `Instances.lean`, `Format.lean`, `Checker.lean`, `Examples.lean`, `ArgPrincipleBridge.lean` are
  byte-identical to the pre-work clone: the bridge really did re-elaborate without an edit.
* `ledger_check.py` genuinely re-runs `reference_checker.py`, `checker_ref.py` and `crosscheck.py`
  by `subprocess` (I read it and timed a checker independently at 0.04 s — the 0.9 s total is real,
  not a cached verdict).
* The 32 bare `decide` calls in `Checker.lean` are pre-existing decidability plumbing, not new.

### VERDICT

**FIX-FIRST** — three label/documentation fixes and one hash-record fix, numbered above with the
exact text. None of them touches the mathematics, the proofs, the transcripts or the seed ledger.

On the substance the item is sound, and I say so without reservation: the theorem exists, it is the
twin of `cert_of_checkW1_ap` with `fDH` for `riemannZeta` and exactly one displayed hypothesis; it
is character-for-character the shape PRICING §3.1 made binding; it rests on
`[propext, Classical.choice, Quot.sound]` and on no `native_decide`, no `sorry` and no program
axiom, across all 112 declarations of the three files; κ is right to 80 digits by four routes
including the Gauss sum; the four `UnitAddCircle` shifts are proved to be the reals 1/5, 2/5, 3/5,
4/5 and the Hurwitz convention is a Mathlib theorem on the Lean side and a source-checked,
numerically re-derived match on the producers' side; the ζ statement of record did not move; DBN and
comparator are untouched against a tree that predates the work; and the M3 seed's four rows are
carried by eight transcripts whose hashes, boxes, winding sums and Lean corollaries I recomputed
myself and found exact.

**Checked by:** Claude Opus 5 (1M), Job 2, 2026-09-10. Scripts and raw logs: `dr8/check-o/`.
Re-derivations only; no verdict in this file rests on Job 1's testimony.
