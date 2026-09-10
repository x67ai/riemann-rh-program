# D1 σ-strong sibling — independent check (Session 21, Job 2, Opus 5, clean clone)

Task: `results/d1-m2a/dr8/BUILD-BRIEF-sigma-strong.md` "Job 2". Object checked: the builder's work
recorded in `dr8/BUILD-NOTES-sigma-strong.md` and `dr8/hashes-sigma-strong.txt` (Job 1, Fable 5.1,
2026-09-10). Specification of the primed generic theorem: `dr8/CHECK-fDH-O.md` §12 FIX-FIRST 1
("Exact fix"). Method precedent: `dr8/CHECK-fDH-O.md` §0–§11.

Nothing in the working tree or the mirror was modified by this job, and nothing was committed by it.

---

## 1. Clone provenance

**Fresh clone, made for this check.** `git clone https://github.com/anthropics/zeta-23-lean.git`
into `~/rh-lean-work/checker-clone-s21`, then `git checkout v1.0` →
HEAD **`3635e74826a4c1fcece7d1cd2b6fa75e43a00510`**, the commit `lean/README.md` "Building" names as
the base this program's files overlay. `lean-toolchain` = `leanprover/lean4:v4.33.0-rc2`;
`lakefile.toml` pins Mathlib `51e6992efd06126df61a496bebf8f49482a4e129`. This is a new clone from
the network, not a reuse of `checker-clone-s20`.

**What the overlay adds, measured before copying.** A file-by-file `cmp` of all **143** mirror files
(`rh-program/lean/**`) against the v1.0 clone: 2 CHANGED (`README.md`, `Zeta23.lean`), 141 NEW.
At tag v1.0 the upstream repository contains none of `Zeta23/W1/**`, `Zeta23/DBN/**`,
`Zeta23/PairCeiling/Grid*.lean`, the six `comparator/*DBN*` files or `formalization.yaml` — so the
whole program layer is an addition, and the DBN/comparator byte-identity question (§7) is settled
against `packaging/hashes.txt` and against git history, not against the clone.

The `Zeta23.lean` diff is exactly **17 added `import` lines** and no other change (the README
sentence still says "fifteen", written before `W1/FDH.lean` and `W1/Ledger.lean` were added — a
stale count in prose, recorded here, not a defect in any statement).

**Overlay applied** exactly as the README recipe prescribes: `Zeta23/`, `comparator/`,
`Zeta23.lean`, plus `formalization.yaml` and `README.md`. Post-overlay `git status` in the clone:
14 entries, all of them the program's own files.

**Mirror provenance.** Program repo `…/riemann` at HEAD **`c24e63c`**, working tree clean. The
builder's base commit is **`d4c7fc4`**; every "pre-edit" SHA-256 in `hashes-sigma-strong.txt` was
re-derived here from `git show d4c7fc4:…` and every "changed" SHA-256 from the working tree, and
all fourteen values match line for line. (`HEAD~1` = `aed5f20` already contains the σ-strong build,
so `d4c7fc4` — not `HEAD~1` — is the pre-work baseline used throughout this report.)

Load discipline: `ps -Ao pcpu,comm | awk '$1>50'` empty before the build; one `lake` process
throughout; `caffeinate` running.

## 2. Cold build of the overlaid clone — **CLEAN**

`lake exe cache get`, then `lake build Zeta23`, one `lake` process, no `-j`, nothing else compiling.

```
Build completed successfully (9144 jobs).
      400.39 real      2537.74 user       601.68 sys      6.33 GB max RSS
```

* **Job count 9144** — the builder's figure, and the figure of the D-R8 clean-clone build.
* **Errors: 0.** No line of the 9144-job log matches `error` at all (the D-R8 check's two
  `EntryError` module-name lines do not appear because that module builds from cache here).
* **Warnings: 191, none from a program module.** No warning names any path under `Zeta23/W1/`,
  `Zeta23/DBN/` or `comparator/`; all 191 are upstream Zeta23 deprecations
  (`Set.mem_setOf_eq`, `ENat.toNat_coe`) in `Statement/`, `WeilEF/`, `XiPrime/`, `ThmE/`, `RvM/`.
* The two edited modules compiled from source, and the whole DBN cascade rebuilt behind them:
  `Zeta23.W1.Soundness` 14 s, `Zeta23.W1.Instances` 42 s, `Zeta23.W1.ArgPrincipleBridge` 3.6 s,
  `Zeta23.W1.Ledger` 3.3 s, `Zeta23.W1.FDH` 3.5 s. So the added theorems break no downstream module.

The 400 s wall time is a genuinely cold build (nothing in this clone's `.lake` before today); the
builder's 83 s and the D-R8 checker's 79 s were warm-cache rebuilds of the changed modules.
Log: `~/rh-lean-work/s21-build.log`.

## 3. `#print axioms` — **CLEAN**

Probe `~/rh-lean-work/probe_s21.lean`, run with `lake env lean` against the built clone; output
`~/rh-lean-work/probe_s21.out`. It is my own probe, generated from the mirror's source, not the
builder's.

**The four new theorems** — each exactly `[propext, Classical.choice, Quot.sound]`:

```
'Zeta23.W1.cert_of_checkW1_of_diffOn'' depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.W1.cert_of_checkW1_fDH''      depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.W1.mpDH_zero''                depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.W1.arbDH_zero''               depends on axioms: [propext, Classical.choice, Quot.sound]
```

**The four unfolding lemmas** — `mpDH_sigma1`, `mpDH_sigma2`, `arbDH_sigma1`, `arbDH_sigma2`:
each exactly `[propext, Classical.choice, Quot.sound]`.

**The six frozen theorems** — `cert_of_checkW1`, `cert_of_checkW1_ap`, `cert_of_checkW1_fDH`,
`cert_of_checkW1_of_diffOn`, `mpDH_zero`, `arbDH_zero`: each exactly
`[propext, Classical.choice, Quot.sound]`.

**Sweep over every top-level declaration of the two edited files.** I extracted the declaration
names mechanically from the mirror's `Soundness.lean` and `FDH.lean` and printed axioms for all of
them: **98 declarations**, all on a subset of the three standard axioms — 99 prints
`[propext, Classical.choice, Quot.sound]`, 8 `[propext]`, 2 `[propext, Quot.sound]`, 2 "does not
depend on any axioms". **Zero occurrences of `sorryAx`, `Lean.ofReduceBool`, or any other axiom.**
(Three names in my extraction — `corollaries`, `exhibits`, `forall` — were false positives of my
own regex reading module-doc prose and the `₂` in `forall₂_mem_right`; `forall₂_mem_right` was
probed separately and is on `[propext]`. No real declaration was skipped.)

## 4. Statement fidelity of `cert_of_checkW1_of_diffOn'` — **CLEAN, byte-identical**

I extracted the ```` ```lean ```` block from `dr8/CHECK-fDH-O.md` §12 FIX-FIRST 1 ("Exact fix") and
the theorem header from `lean/Zeta23/W1/Soundness.lean` (lines 1192–1195) and compared them as
bytes. After removing the trailing ` := by` that the Lean file must carry and the specification
block does not, the two are **identical**, including line breaks, indentation and spacing:

```
sha256(spec block)          add88f1af83b5766040a23278acafea29eb4d82abe6ea6e50a4450db16ff7dd8
sha256(Lean header, no ':= by')  add88f1af83b5766040a23278acafea29eb4d82abe6ea6e50a4450db16ff7dd8
```

The elaborated statement agrees (`#check`):

```
cert_of_checkW1_of_diffOn' : ∀ (f : ℂ → ℂ), DifferentiableOn ℂ f {s | s.re < 1} → ∀ (d : W1Data),
  checkW1 d = true → W1EnclOK f d → RectArgPrinciple f →
    (1 ≤ d.m → ∃ ρ, f ρ = 0 ∧ sigma1 d < ρ.re ∧ ρ.re < sigma2 d ∧ T1 d < ρ.im ∧ ρ.im < T2 d) ∧
      (d.m = 0 → ∀ s ∈ W1Rect d, f s ≠ 0)
```

**The proof body is the unprimed body with exactly one line changed**, as the specification
prescribes. I diffed the two 226-line regions (lines 956–1181 and 1192–1417): apart from the
6-line vs 4-line header, the only difference in 220 lines of proof is

```
-    exact ⟨ρ, hρ0, lt_trans hhalf hr1, lt_trans hr2 hs2lt1, hi1, hi2⟩
+    exact ⟨ρ, hρ0, hr1, hr2, hi1, hi2⟩
```

The three derived statements match the brief's step 2 text as well:
`cert_of_checkW1_fDH'` is the f_DH instance with `sigma1 d < ρ.re ∧ ρ.re < sigma2 d`, and both
corollaries elaborate to

```
∃ ρ, fDH ρ = 0 ∧ 4 / 5 < ρ.re ∧ ρ.re < 41 / 50 ∧ 1 / 2 < ρ.re ∧ ρ.re < 1
   ∧ 8569 / 100 < ρ.im ∧ ρ.im < 8571 / 100
```

with hypothesis `W1EnclOK fDH mpDH` (resp. `arbDH`) — the single displayed hypothesis H-ENCL_DH,
no other.

## 5. Box arithmetic, from the transcripts — **CLEAN**

Checked from the JSON transcripts and the unchanged `Instances.lean` literals, not from the
builder's word.

**The transcripts.** `results/d1-m1/acceptance/w1-mp-dh-livefire.json` and
`w1-arb-dh-livefire.json`, parsed with `json.load`, both carry

```
rect = {'sigma1': {'n': '4', 'd': '5'}, 'sigma2': {'n': '41', 'd': '50'},
        'T1': {'n': '8569', 'd': '100'}, 'T2': {'n': '8571', 'd': '100'}}
function = f_DH        claimed_m = 1
```

**The Lean literals** (`Zeta23/W1/Instances.lean`, unchanged by this build — see §7):
`def mpDH` has `p1 := 4; q1 := 5`, `p2 := 41; q2 := 50`, `a1 := 8569; b1 := 100`,
`a2 := 8571; b2 := 100`, `m := 1`; `def arbDH` has the same four rationals and `m := 1`. So the
Lean rectangle is the transcript rectangle on both legs.

**The accessors** (`Soundness.lean` lines 85–91): `sigma1 d = (d.p1 : ℝ) / d.q1`,
`sigma2 d = (d.p2 : ℝ) / d.q2`, `T1 d = (d.a1 : ℝ) / d.b1`, `T2 d = (d.a2 : ℝ) / d.b2`.
Hence `sigma1 mpDH = ((4 : ℤ) : ℝ) / ((5 : ℤ) : ℝ)` and `sigma2 mpDH = ((41 : ℤ) : ℝ) / ((50 : ℤ) : ℝ)`,
which is exactly what the four unfolding lemmas discharge by `show … ; norm_num`. Their elaborated
statements, from my own `#check` in the built clone:

```
mpDH_sigma1  : sigma1 mpDH  = 4 / 5      mpDH_sigma2  : sigma2 mpDH  = 41 / 50
arbDH_sigma1 : sigma1 arbDH = 4 / 5      arbDH_sigma2 : sigma2 arbDH = 41 / 50
```

and the pre-existing `mpDH_T1/T2`, `arbDH_T1/T2` give `8569/100`, `8571/100` on both legs.
**The Arb twin is genuinely the twin:** the four rationals are the same on both legs (the legs
differ only in `A`, the mesh and the row data — `A = 10^12` for mp, `A = 10^6` for Arb — and are
never merged, D-R3).

**Numerically:** 4/5 = 0.8, 41/50 = 0.82, 8569/100 = 85.69, 8571/100 = 85.71 — the box
R = [4/5, 41/50] × [85.69, 85.71] of the binding label. The two half-strip clauses the corollaries
also carry are implied by the box clauses, and the proofs derive them that way
(`lt_trans (by norm_num) hr1` from 1/2 < 4/5, `lt_trans hr2 (by norm_num)` from 41/50 < 1) — so the
box form is strictly stronger than the D-R8 half-strip form and loses nothing.

**Label soundness against the statement.** The theorems give the OPEN box (strict inequalities);
the label claims a zero "in R", the CLOSED box, with Re s > 1/2. Open ⊂ closed and 4/5 > 1/2, so
the label is implied by the statement rather than exceeding it. This is the direction FIX-FIRST 1
asked for, and it now holds.

## 6. No regression on the six frozen theorems — **CLEAN**

The brief's frozen set plus `arbDH_zero`, six names. Two independent arguments.

**(a) Source, against the pre-work mirror in git.** `git diff d4c7fc4 HEAD` over
`rh-program/lean/`, with `-U0`:

```
Zeta23/W1/Soundness.lean : one hunk, @@ -1177,0 +1178,234 @@   deleted lines: 0
Zeta23/W1/FDH.lean       : four hunks, all @@ -N,0 +M,k @@       deleted lines: 0
```

Both edits are **pure insertions — zero deleted lines in either file** — so every pre-existing
character of both files, and therefore every one of the six frozen statements and every one of
their proofs, is unchanged character-for-character. No line-by-line comparison of individual
theorem texts can say more than this. The only other files changed anywhere under `lean/` are
`README.md` and `formalization.yaml` (documentation).

**(b) Elaborated statements, from the built clone.** `#check` of the six in my own build:

```
cert_of_checkW1          : … (1 ≤ d.m → ∃ ρ, riemannZeta ρ = 0 ∧ 1/2 < ρ.re ∧ ρ.re < 1 ∧ T1 d < ρ.im ∧ ρ.im < T2 d) ∧ (d.m = 0 → …)
cert_of_checkW1_ap       : … same, without the RectArgPrinciple hypothesis
cert_of_checkW1_fDH      : … same shape with fDH
cert_of_checkW1_of_diffOn: … generic in f, half-strip conclusion 1/2 < ρ.re ∧ ρ.re < 1
mpDH_zero                : W1EnclOK fDH mpDH  → ∃ ρ, fDH ρ = 0 ∧ 1/2 < ρ.re ∧ ρ.re < 1 ∧ 8569/100 < ρ.im ∧ ρ.im < 8571/100
arbDH_zero               : W1EnclOK fDH arbDH → ∃ ρ, fDH ρ = 0 ∧ 1/2 < ρ.re ∧ ρ.re < 1 ∧ 8569/100 < ρ.im ∧ ρ.im < 8571/100
```

Every one of the six still concludes the HALF-STRIP, not the box. Nothing was strengthened in
place; the strengthening lives only in the four new primed names.

## 7. DBN / comparator byte-identity — **CLEAN, three ways**

1. **Against `packaging/hashes.txt`.** All **six** `comparator/*DBN*` lines
   (`ChallengeDeps/DBN.lean`, `ChallengeDeps/DBN/Instance02.lean`, `Challenge/DBN.lean`,
   `Solution/DBN.lean`, `PrintAxioms/DBN.lean`, `config-dbn.json`) verify against the current
   mirror, as do all but two of the file's remaining lines. The two that do not are
   `lean/formalization.yaml` and `results/d1-m2a/packaging/FIDELITY.md`, both of which the file's
   own append-only note already records as superseded, and both of which this build legitimately
   edited (§8, §9). See the MINOR in §11.
2. **Against git.** `git diff d4c7fc4 HEAD -- lean/Zeta23/DBN lean/comparator` is **empty**; the
   complete list of files changed under `lean/` is `README.md`, `Zeta23/W1/FDH.lean`,
   `Zeta23/W1/Soundness.lean`, `formalization.yaml`. `Instances.lean`, `Ledger.lean`,
   `ArgPrincipleBridge.lean`, `Format.lean`, `Checker.lean`, `Examples.lean` and `Zeta23.lean` are
   untouched — which is what makes §5's reading of the `mpDH`/`arbDH` literals load-bearing.
3. **Against the builder's own manifest, in my clone.** I replayed all **143** lines of the
   post-build manifest in `dr8/sigma-strong-untouched.log` (121 files under `Zeta23/DBN/**` and 22
   under `comparator/**`, the latter including the upstream v1.0 comparator files) against my
   independently overlaid clone: **143 OK, 0 mismatches, 0 missing.**

   (The mirror `rh-program/lean/comparator/` holds only the six program files, so the
   DBN+comparator count is 127 there and 143 in the tree/clone. The README sentence "all 143 files
   under `Zeta23/DBN/` and `comparator/`" is the tree count and is correct as written.)

## 8. Label sweep — **CLEAN**

The question is whether the box-form sentence of `dr8/PRICING-fDH.md` §3.2 —

> "f_DH has at least one zero in R = [4/5, 41/50] × [85.69, 85.71] with Re s > 1/2 — kernel-checked
> modulo the displayed hypothesis H-ENCL_DH (the two producers' enclosures of f_DH on ∂R are true;
> producers untrusted)."

now appears anywhere it is NOT scoped to the primed names, and whether any unprimed label moved.

**Every live occurrence, and its scope.** A grep for `at least one zero in R` over the whole
repository returns 18 hits. Ten are in D-R8-era records and logs (`PRICING-fDH.md`,
`CHECK-fDH-O.md` check-o artifacts, `label-sweep-checkers.log`, the two build briefs/notes) and are
history. The **five live sites** are:

| site | scope stated |
|---|---|
| `lean/Zeta23/W1/FDH.lean` §"σ-STRONG SIBLING" and the §4 section header | "For the primed theorems ONLY"; `mpDH_zero`/`arbDH_zero` explicitly "unchanged", half-strip |
| `results/d1-m1/FORMAT.md` §9.2, new dated block | "**For the primed theorems ONLY**"; names the six unprimed theorems as keeping the half-strip label |
| `lean/README.md` new "σ-strong sibling" section | "For the PRIMED theorems … only"; "The unprimed theorems keep the half-strip label" |
| `lean/formalization.yaml` `main_results` entry for `mpDH_zero'` | "for the primed theorems only"; "The unprimed `mpDH_zero` keeps the half-strip label" |
| `directions/D1-certified-refutation-arm.md` work-log + frontier entries | "Label for the primed theorems ONLY (box form …)"; "The unprimed theorems keep the half-strip label" |

No site attaches the box sentence to an unprimed name, and no site drops the never-say list
(nothing about ζ, RH or Λ; not "RH-for-DH disproved"; not "fully machine-checked"). All five edits
are insertions dated 2026-09-10, Session 21.

**Unprimed labels unchanged.** The eight artifacts that print the half-strip trust label are
byte-identical to `d4c7fc4`: `producer_mp.py`, `producer_arb.py`, `checker_ref.py`,
`reference_checker.py`, `w1-schema.json`, both live-fire JSONs, `acceptance-report.md`. The D-R8
block of FORMAT §9.2 and the D-R8 sections of `lean/README.md` and the D1 direction file are
untouched (insertion-only diffs). This is the right call: those artifacts describe the checker's
acceptance, whose Lean backing is the unprimed theorem.

**Direction file.** The "Next D-R8 item (OWED, not written)" sentence keeps its text and gains a
bold dated DONE note; a dated work-log entry and a "SESSION-21 σ-STRONG SIBLING BUILT" frontier
paragraph were appended, the latter carrying the refutation-shaped close of KICKSTART 10(c) and the
honest "Opus check pending". `FIDELITY.md` (m) and `formalization.yaml` fidelity (m) each keep the
original OWED text and append a dated CLOSED sentence — append-only, as the program's convention
requires.

## 9. `formalization.yaml` — **CLEAN, 0 errors**

Ran the builder's `dr8/validate_yaml_sigma_strong.py` (PyYAML 6.0.3, jsonschema 4.25.1). I read the
script before running it; it validates the mirror's YAML against the upstream dispatcher schema
from the on-disk copies and independently re-fetches the three upstream schema files to compare.

```
on-disk formalization.schema.dispatcher.json  sha256 22bd0b61…  upstream: IDENTICAL to the on-disk copy
on-disk v0.3.schema.json                      sha256 93247a80…  upstream: IDENTICAL to the on-disk copy
on-disk v0.4.schema.json                      sha256 25ff6b25…  upstream: IDENTICAL to the on-disk copy

VALIDATION errors: 0
main_results: 18   alignment.statements: 19   fidelity.divergences: 7737 chars
Lean names referenced in status.main_results + alignment.statements: 43 — all DECLARED in the mirror
RESULT: PASS — errors: 0, undeclared names: 0
```

`main_results` went 14 → 18, one entry per new theorem, each with `sorry_count: 0` and the three
standard axioms — which §3 confirms independently against the kernel. The two `alignment.statements`
`lean:` fields now list the primed names alongside the unprimed ones.

**The regex point is real, and the builder's fix is the correct one.** I reproduced it directly:
`check-o/yaml_o.py`'s `declared()` ends its pattern in `\b`, and for a name ending in an apostrophe
there is no word boundary after the `'`, so `mpDH_zero'` would print as NOT DECLARED.
`validate_yaml_sigma_strong.py` replaces `\b` with the negative lookahead `(?![A-Za-z0-9_'])`.
Test, on a two-line source containing both declarations:

```
mpDH_zero'   old (\b): False   new (lookahead): True
mpDH_zero    old (\b): True    new (lookahead): True
```

The lookahead form is not merely equivalent, it is strictly more accurate: `\b` would also let the
unprimed name `mpDH_zero` match the primed declaration `theorem mpDH_zero'`, which the lookahead
correctly rejects.

## 10. Trust greps — **CLEAN, 0 hits**

My own comment stripper (block comments with nesting, then line comments), run on the two edited
mirror files, for `axiom`, `native_decide`, `unsafe`, `implemented_by`, `extern`, `opaque`,
`sorry`, `admit`, `ofReduceBool`, `sorryAx`, `Lean.ofReduceBool`, `partial`:

```
Zeta23/W1/Soundness.lean   71776 raw chars → 57468 after stripping   all twelve tokens: 0 hits
Zeta23/W1/FDH.lean         15569 raw chars →  4893 after stripping   all twelve tokens: 0 hits
```

The three raw-text hits that the stripper removes are prose: `sorry`-free in each module doc, and
`` `#print axioms` `` in `FDH.lean`'s header. No `decide`/`native_decide` was introduced — the two
`by decide` uses in the primed corollaries discharge `1 ≤ mpDH.m` and `1 ≤ arbDH.m`, kernel
`decide` on a literal, the same tactic the unprimed corollaries already use.

This is corroborated from the other side by §3's sweep: 98 declarations, no axiom outside
`{propext, Classical.choice, Quot.sound}`.

## 11. Verdict

**Per item, as the brief asks:**

| # | item | verdict |
|---|---|---|
| 1 | Clone provenance (fresh clone, upstream v1.0 `3635e748`, mirror overlay per `lean/README.md`) | **CLEAN** |
| 2 | Cold build — 9144 jobs, 0 errors, 0 warnings from any program module, 400 s | **CLEAN** |
| 3 | `#print axioms` — 4 new theorems, 4 unfolding lemmas, 6 frozen theorems, and a 98-declaration sweep of the two edited files: standard axioms only | **CLEAN** |
| 4 | Statement fidelity of `cert_of_checkW1_of_diffOn'` vs CHECK-fDH-O §12 FIX-FIRST 1 — byte-identical, same SHA-256; body differs from the unprimed one in exactly the prescribed line | **CLEAN** |
| 5 | Box arithmetic from the transcripts — `sigma1 = 4/5`, `sigma2 = 41/50`, `T1 = 8569/100`, `T2 = 8571/100` on both legs; the Arb twin is the twin; the label is implied by the statement, not the reverse | **CLEAN** |
| 6 | No regression — both Lean diffs are pure insertions (0 deleted lines), and all six frozen statements still elaborate to the half-strip form | **CLEAN** |
| 7 | DBN/comparator byte-identity — six `packaging/hashes.txt` lines verify; `git diff` over `DBN`/`comparator` empty; 143/143 manifest lines match in my clone | **CLEAN** |
| 8 | Label sweep — the box sentence appears at five live sites, every one scoped to the primed names; the eight artifacts printing the unprimed label are byte-identical to the base commit | **CLEAN** |
| 9 | `formalization.yaml` — jsonschema 0 errors, 18 main results, 43 Lean names all declared; the primed-name regex fix verified and strictly better than `\b` | **CLEAN** |
| 10 | Trust greps on the two edited files, comments stripped — 0 hits on all twelve tokens | **CLEAN** |

**VERDICT: CLEAN.** No FIX-FIRST item. The work delivers exactly what `CHECK-fDH-O.md` §12
FIX-FIRST 1 specified: the σ-strong sibling is stated character-for-character as prescribed, the
box-form corollaries hold on the transcripts' own rationals, every frozen statement is untouched,
and the box-form label is now backed by a theorem for the names that carry it. Fidelity item (m) is
properly closed.

### MINOR 1 (record hygiene, not a claim defect) — `packaging/hashes.txt`'s superseding note is now itself stale

`results/d1-m2a/packaging/hashes.txt` carries an append-only note from D-R8 giving replacement
SHA-256 values for its two stale lines: `lean/formalization.yaml → 99b77f80…` and
`packaging/FIDELITY.md → dee704cf…`. This build changed both files again, so those replacement
values no longer verify either (current: `d7b75189…` and `6030b9cc…`, both recorded in
`dr8/hashes-sigma-strong.txt`). Nothing false is asserted about any theorem; the fix is one more
appended line naming the Session-21 values. The brief did not ask for it, so it is not a FIX-FIRST.

### Observations, recorded so they are not re-litigated

* `lean/README.md` "Building" still says the working tree differs from v1.0 "by fifteen `import`
  lines added to the root `Zeta23.lean`". The actual count is **17**, and has been since
  `W1/FDH.lean` and `W1/Ledger.lean` landed at D-R8 — the sentence predates this build and is not
  something this build touched. Prose count only; the recipe itself is correct and reproduced the
  build exactly.
* The DBN+comparator file count is 143 in the tree and the clone (which include the upstream v1.0
  comparator files) and 127 in the mirror, which holds only the six program comparator files. Both
  numbers are right for their scope; the records use the tree number.
* `STATUS.md`'s live entry writes the primed names as `` `cert_of_checkW1_of_diffOn` ``′ with the
  prime outside the code span. Cosmetic, in the orchestrator's own file.

### Honesty note — what this check does and does not establish

* Everything in §§2–7 and §10 was produced in **my own clean clone**, from a clone I made from the
  network today at upstream tag v1.0, overlaid by the mirror at program HEAD `c24e63c`. §5's
  transcript numbers came from my own `json.load` of the two JSONs and my own reading of
  `Instances.lean`. §9 ran the builder's script, which I read first; its jsonschema verdict is
  independent of the network, and the three schema files were confirmed identical to upstream at
  the time of this run.
* **What is still assumed, unchanged by this work.** H-ENCL_DH is a displayed hypothesis, not a
  theorem: the two producers' enclosures of f_DH on ∂R are untrusted. The identification of the
  producers' f_DH with Lean's `fDH` remains a meta-level convention match (`formalization.yaml`
  fidelity (l)). The box-form theorems say nothing about ζ, nothing about RH, nothing about Λ, and
  are not a machine-checked disproof of RH for the Davenport–Heilbronn function — they exhibit ONE
  off-line zero in the witness direction, modulo H-ENCL_DH.
* **What this check did not do**, and no one should read it as having done: I did not re-derive κ
  (that is `dr8/kappa-check.log`, D-R8), did not re-run the producers or the reference checkers,
  did not re-verify the 145 533 transcript integers against the Lean literals (D-R8's packaging
  check), and did not build `Solution.DBN` or `Challenge.DBN` — the DBN layer is untouched by this
  work, which §7 establishes three independent ways, so rebuilding it would test nothing this
  build could have broken.
* No file in the working tree or the mirror was modified by this job, and this job made no commit.
  Its only writes are this report and the artifacts under `~/rh-lean-work/`.
