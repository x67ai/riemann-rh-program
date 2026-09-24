# C2 — M4 residue, Unit A (`Separation6b`): b₁ proved in symbolic form, the clause-7 fold, `rstar_of_21L` — independent check (Session 24 item 3, Job 2, Opus 5, clean clone)

Task: `results/c2-m4/BRIEF-A.md` "Job 2 — INDEPENDENT CHECKER"; contract `results/c2-m4/PRICING-RESIDUE.md` §1 Pieces 2, 3
(3-sym), 6 and §2 row A; the builder's own checklist `results/c2-m4/BUILD-NOTES-A.md` §5. Object checked: the builder's
work (Job 1, Fable 5.1, 2026-09-24, 19:20–19:55 IST) as recorded in `BUILD-NOTES-A.md`, `SHARED.md` (the Unit A blocks)
and `hashes-A.txt`. Method precedent: `results/c2-m4/CHECK-O-iii.md` (layout repeated), `CHECK-O.md`.

Nothing in the repository, the mirror or the builder's working tree was modified by this job, and nothing was committed
by it. Everything in §§2–12 was produced in a FRESH clone made for this check, `~/rh-lean-check-s24/clone` (cloned from
`https://github.com/anthropics/zeta-23-lean.git` at 19:58 IST, checked out at tag v1.0), overlaid with the current
`rh-program/lean/` mirror; never in `~/rh-lean-work/zeta-23-lean-main`. Scripts and logs: `results/c2-m4/verify-A-O/`.

---

## §0 Headline verdict

**OVERALL: CLEAN — no FIX-FIRST; 3 MINOR (§13).** Every item of the brief's Job 2 and BUILD-NOTES-A §5, run from a fresh
clone of upstream v1.0 with the mirror overlaid: cold build **9150 jobs, 0 errors**; `#print axioms` standard three on the
4 roots and on all 30 library declarations; trust greps = the 4 deliberate challenge `sorry`s; statement identity ×4;
**Comparator with nanoda ×3 — CONTROL, `SeparationClause4b`, `Separation6b` — `Your solution is okay!`, exit 0**; the twelve
frozen statements byte-identical; yaml PASS; lint clean; hashes 37/37. The points weighed hardest (§9): (i) no digit of
b₁ and no lower bound on Z outside `rstar_of_21L`'s C_B step — CLEAN; (ii) `absorb_b` closes at 39/1000 and 1/1000 from
b₁sym ≥ 4 only, root conclusion unchanged — CLEAN; (iii) the double is 2·(2t)²‖B̂(−2tL)‖² = check-O §12.3's 8t²B̂(2tL)²
(1.80836·10⁻³¹ at (30, 40), recomputed) and the tight pair is note §7.2 — CLEAN; (iv)–(v) CLEAN; (vi) the binders are
equivalent under the hypotheses (kernel-checked probe, including the composition assembly-with-21L) and the label is
honest — CLEAN; (vii) L*(0.1, 10⁶; C₁ = 1) = 403.4973 → 412.8235 — CLEAN. The full table is at the end.

---

## §1 Clone provenance and the overlay — **CLEAN**

A new clone, not a reset of an earlier one:

```
git clone https://github.com/anthropics/zeta-23-lean.git clone ; git checkout v1.0
HEAD:          3635e74826a4c1fcece7d1cd2b6fa75e43a00510
v1.0^{commit}: 3635e74826a4c1fcece7d1cd2b6fa75e43a00510
git status --porcelain -> (empty)
lean-toolchain  leanprover/lean4:v4.33.0-rc2
lakefile.toml   rev = "51e6992efd06126df61a496bebf8f49482a4e129"   (Mathlib)
```

This is the commit `lean/README.md` "Building" names and the toolchain/Mathlib pair of every record in this program.

**Overlay measured before copying.** A file-by-file `cmp` of all **177** mirror files (`rh-program/lean/**`) against the
pristine v1.0 tree: **175 NEW, 2 CHANGED** (`README.md`, `Zeta23.lean`), 0 identical. The `Zeta23.lean` difference is
exactly **23 added `import` lines and nothing else** (the M4 (iii) record's 21 plus `import Zeta23.Separation.B1Sym`,
`import Zeta23.Separation.Assembly2`), so BUILD-NOTES-A's "the ONE edit to an existing Lean file is the two additive
imports in `Zeta23.lean`" is confirmed against upstream, not merely against the previous commit. Overlay applied by the
README recipe (`Zeta23/`, `comparator/`, `Zeta23.lean`, plus `formalization.yaml` and `README.md`); post-overlay
`git status --porcelain` in the clone lists 43 entries, all of them the program's own files.

**Cold.** The clone has no `.lake/build` at all: the Mathlib package directory (`.lake/packages`, 7.8 GB) was copied by an
APFS clone from the earlier checker's clone (`cp -Rc`), and `lake exe cache get` then reported `No files to download;
Already decompressed 8681 file(s)` (`verify-A-O/cache-get.log`). The whole `Zeta23` library, the program's additions
included, therefore compiled from source.

Load discipline: one `lake` process at a time throughout; no `-j`; `caffeinate` running; nothing else heavy in parallel.

## §2 Cold build of the overlaid clone — **CLEAN**

`lake build Zeta23` (19:58:49–20:05:48 IST; `verify-A-O/build-zeta23.log`):

```
✔ [8795/9150] Built Zeta23.Separation.B1Sym (4.7s)
✔ [8859/9150] Built Zeta23.Separation.Assembly2 (18s)
Build completed successfully (9150 jobs).
      419.13 real      2680.37 user       656.21 sys
exit=0
```

* **Job count 9150** — the builder's figure exactly, and the M4 (iii) record's 9148 plus the two new modules.
* **Errors: 0.** The only two lines matching `error` case-insensitively name the module `Zeta23.XiPrime.ExplicitFormula.EntryError`.
* **Warnings: 191 lines beginning `warning:`** — the count the M4 (i) and M4 (iii) checkers measured. None names
  `B1Sym`, `Assembly2` or any `comparator/` path; the only warnings from program modules are the two pre-existing ones
  in `Zeta23/PairCeiling/Stability.lean` (49:4, 245:4).
* All six `Separation` modules compiled from source: `LemmaG1 (4.2s)`, `LemmaG (5.7s)`, **`B1Sym (4.7s)`**,
  `Clause4 (6.3s)`, `Assembly (12s)`, **`Assembly2 (18s)`**.

## §3 The two Solution modules — **CLEAN**

`lake build Solution.SeparationClause4b Solution.Separation6b` (`verify-A-O/build-solutions.log`):

```
✔ [8709/8711] Built ChallengeDeps.Separation6b (2.0s)
✔ [8710/8711] Built Solution.SeparationClause4b (3.5s)
✔ [8711/8711] Built Solution.Separation6b (3.6s)
Build completed successfully (8711 jobs).
```

0 errors; no warning from any new module (the one warning in the log is the upstream `Zeta23/Taper/Gevrey.lean:342:80`
unused-variable lint, a tracked v1.0 file, replayed). BUILD-NOTES-A §3 records the same 8711.

## §4 `#print axioms` — **CLEAN**

**(a) The four root theorems, through the builder's PrintAxioms files, in my clone** (`verify-A-O/print-axioms-roots-AO.log`):

```
'separation_clause4_in_window_noise_b' depends on axioms: [propext, Classical.choice, Quot.sound]
'separation_clause6_assembly_b' depends on axioms: [propext, Classical.choice, Quot.sound]
'separation_clause7_tight_pair' depends on axioms: [propext, Classical.choice, Quot.sound]
'rstar_of_21L' depends on axioms: [propext, Classical.choice, Quot.sound]
```

**(b) Every library declaration.** I did not reuse the builder's probe list: `verify-A-O/axioms_AO_probe.lean.txt` is
generated by a grep of every line beginning `theorem ` in `B1Sym.lean` (16) and `Assembly2.lean` (13), plus the
definition `b1sym`; neither file has any `lemma`, `private` or `protected` declaration. Result
(`verify-A-O/print-axioms-library-AO.log`): **30 of 30 lines `[propext, Classical.choice, Quot.sound]`, nothing else** —
the builder's 29 theorems, the same names, plus `b1sym`. No `sorryAx`, no `Lean.ofReduceBool`.

## §5 Trust greps — **CLEAN**

The builder's `verify-A/trust_greps_A.py` (comments stripped; nine words) on the nine Unit A files in my clone
(`verify-A-O/trust-greps-AO.log`): **exactly four hits, the four deliberate challenge `sorry`s** —
`Challenge/SeparationClause4b.lean:43`, `Challenge/Separation6b.lean:70, 93, 100`. I read the script: its comment
stripper handles nested `/- -/` and `--`, so a word in a docstring is not a hit, and a word in code is.

An extra grep of my own over the same files (`verify-A-O/extra-greps-AO.log`: `set_option`, `macro`, `elab`, `@[`,
`attribute`, `instance`, `notation`, `axiom`, `decreasing_by`, `partial`, `def `): the code hits are exactly the two
`def b1sym` lines (library and trusted) and the three `set_option linter.unusedVariables false in` lines (library 294,
challenge 72, solution 50). No attribute, instance, macro or notation is declared anywhere in the unit.

## §6 Statement identity, challenge against solution — **CLEAN**

Two independent extractions (`verify-A-O/statement-identity-AO.log`):

* the builder's `statement_identity_A.py` (regex up to the ` :=` that starts the proof): rung 291 characters,
  `separation_clause6_assembly_b` 889, `separation_clause7_tight_pair` 1057, `rstar_of_21L` 143 — IDENTICAL ×4, PASS;
* my own `stmt_identity_AO.py` (scan from `theorem <name>` to the first `:=` outside every bracket pair and comment;
  UTF-8 bytes): 315 / 970 / 1162 / 161 bytes, IDENTICAL ×4, PASS, with SHA-256 prefixes
  `444525975a688dff`, `9203e9309edb8ac3`, `4b4027faf5d3d745`, `d74308b606df73c0`.

The Comparator runs of §11 re-establish the same identity at the level of kernel terms.

## §7 The trusted definitions, read line by line — **CLEAN**

`comparator/ChallengeDeps/Separation6b.lean` (42 lines) read in full. Its code is:

```
import Mathlib
import ChallengeDeps.Separation6
namespace Separation
noncomputable section
def b1sym : ℝ := (2 * Real.exp (-1) / Z) ^ 2
end
end Separation
```

* **It imports the frozen `ChallengeDeps.Separation6` and adds only `b1sym` (item (iv)).** No other declaration, no
  `attribute`, no `instance`, no re-declaration: `Rstar`, `Hedge`, `HB3`, `Hout`, `orbit`, `edge`, `SepConfig`, `W`,
  `ftest`, `cB`, `CB`, `Z` are the declarations of the frozen files, identity by import. The frozen trusted files
  (`SepConfig.lean`, `Separation6.lean`) and the two old challenge/solution pairs are SHA-256-identical in my clone to
  `hashes-iii.txt` (11 of 11 Lean/config files; `verify-A-O/frozen-files-vs-hashes-iii.log` — the only two differences
  are `Zeta23.lean` (the two added imports) and `formalization.yaml`, both expected).
* **`b1sym`, character for character.** `diff` of the `def b1sym` line in `ChallengeDeps/Separation6b.lean` and in
  `Zeta23/Separation/B1Sym.lean`: empty. The `Z` it reads is `Separation.Z` (`ChallengeDeps/Separation.lean:42`) on the
  trusted side and `Zeta23.Separation.Z` (`LemmaG1.lean:58`) on the library side; those two lines and the `Braw`, `B`
  lines above them are identical text (`def Z : ℝ := ∫ v in (-1 / 2 : ℝ)..(1 / 2), Braw v`), as the M4 (i) and (iii)
  checks recorded, and the kernel accepted the solution's delegation (§11), which requires the two to unfold to the
  same term.
* **It is the note's quantity.** (2e^{−1}/Z)² = (2B(0))² = ‖B′‖₁² (note §5's "hand-proved bound b₁ ≤ ‖B′‖₁² = 10.984"):
  recomputed at 40 digits, Z = 0.22199690808404, ‖B′‖₁ by quadrature of |B′| = 3.31427535947642 = 2e^{−1}/Z to all
  15 printed digits, b₁sym = 10.9844211584326 (`verify-A-O/paper-numerics-AO.log`). No digit is asserted in Lean.
* **The two new statements against the frozen ones** (`diff` of the theorem blocks): the rung differs from
  `separation_clause4_in_window_noise` only by its name, the deletion of `(hb1 : Separation.Hb1)` and `2 * (87 / 10)` →
  `2 * Separation.b1sym` in the conclusion; the assembly differs from `separation_clause6_assembly` only by its name,
  `hb1` deleted, `Real.log (2 * (87 / 10) * C₁)` → `Real.log (2 * Separation.b1sym * C₁)` in `hL2`, and the line
  break of `:= by`. Nothing else: the conclusion is byte-identical.

## §8 The fidelity ledger, row by row — **CLEAN (5/5; no unlisted weakening)**

Against PRICING-RESIDUE §1 Pieces 2, 3, 6, the note §5, §7.2, A1 and check-O §12.2–§12.3; each row is recorded in yaml
(t)/(s)/(w) and in `FIDELITY.md` (t)/(s)/(w) (read).

| row | claim | checked against | verdict |
|---|---|---|---|
| (t1) | b₁ is the real number (2e^{−1}/Z)² = ‖B′‖₁², proved; no digit; the note's 8.70 not stated; hL2 stronger by log(10.984/8.70) = 0.233 nats | note §5 (line 263), check-O §12.2 ("10.99 … at the cost of 0.24 nats"), Piece 3 | CLEAN — `hb1sym` proves (|η|‖B̂(η)‖)² ≤ b₁sym for every real η; log(b₁sym/8.70) = 0.233155 (log(10.984/8.70) = 0.233117; check-O's "0.24" is the upward rounding of log(10.99/8.70) = 0.2337). A stronger hypothesis is a weakening of the theorem, and it is the listed one |
| (s1) | the double at −t contributes 2·(2t)²‖B̂(−2tL)‖² = 8t²B̂(2tL)², not the body's 16t² | check-O §12.3, Piece 2 | CLEAN — see §10 (3) and §9 (iii) |
| (s2) | "double at ±t" = multiplicity 2 on the two carrier points ⟨1/2, ±t⟩ | note §7.2 ("the points t and −t each with multiplicity two"); `SepConfig`'s distinct-points-with-multiplicity convention | CLEAN |
| (w1) | 21 enters Lean only as the corollary's hypothesis; (q3) amended | Piece 6, A1 | CLEAN — the only `21` in code is `h21 : 21 * L ≤ t` (challenge 98, solution 77, library 404) |
| (w2) | the proof is a direct tangent-line chain, the statement is A1's | A1 ("Let t ≥ 3, L ≥ 50, δ ∈ [25/L, ½]") | CLEAN — the binders are A1's domain verbatim; `Rstar` is the frozen trusted definition |

No constant in any statement of the unit differs from the frozen M4 (iii) statements except 87/10 → b₁sym; 64231/100,
148088/100000, 73, 25, 4, 27/20, 39/1000 and 1/1000 are unchanged.

## §9 The points weighed hardest — **CLEAN ×7**

**(i) No digit of b₁ and no lower bound on Z outside `rstar_of_21L`'s C_B step.** `verify-A-O/digit_grep_AO.py` runs
the brief's patterns (`8.7`, `87/10`, `10.99`, `1099`, `0.22`, `Z_lo`, `1/18`, `one_div_eighteen`) plus `10.98`,
`eighteen`, `8.6`, `3.31`, `0.23`, the bare `18`, `exp (-4 / 3)` and every `Z_pos`/`Z_le`/`≤ Z` pattern, over the nine
files, code AND comments, classifying each hit (`verify-A-O/digit-grep-AO.log`, 50 lines). Every hit accounted for:

* **Code hits, digit patterns:** only `Assembly2.lean` 352 (`exp_neg_four_thirds_le_Braw`), 364–380
  (`one_div_eighteen_le_Z`), 386–398 (`log_CB_le`: `18 * Real.exp 1 ^ 2`, `Real.log 18 ≤ Real.log 25`). A grep of the
  WHOLE clone (`Zeta23/`, `comparator/`) for `log_CB_le`, `one_div_eighteen_le_Z`, `exp_neg_four_thirds_le_Braw` and
  `cB_ge`: the only consumer of `one_div_eighteen_le_Z` is `log_CB_le` (line 388), and the only consumer of `log_CB_le`
  is `rstar_of_21L` (line 445). So Z ≥ 1/18 lives in the C_B step of that one lemma and nowhere else; it is in no
  statement of either challenge file.
* **Code hits, Z patterns:** `Z_pos` (0 < Z, the pre-existing `LemmaG1` fact, qualitative — no digit) in `deriv_B_nonpos`,
  `deriv_B_nonneg`, `four_le_b1sym`, `log_CB_le`; `Z_le_exp_neg_one` (an UPPER bound on Z, which gives b₁ from BELOW —
  the pricing observation §0 (i)); `Z.inWindowNoise` (the configuration named `Z`; a false positive).
* **Comment hits:** 8.70, 87/10, 10.984 and 0.233 occur only in docstrings/headers that say they are NOT stated
  ("The note's 8.70 and the hand computation's 10.984 are not stated"; "stronger by log(10.984/8.70) = 0.233 nats").
* `cB_ge : 1429 / 10000 ≤ cB` is a digit of c_B (not b₁, not Z), used by `rstar_of_21L` only.

**(ii) `absorb_b` closes at the same 39/1000 and 1/1000 with only b₁sym ≥ 4; the root conclusion is unchanged.**
`diff` of `absorb` (`Assembly.lean`) against `absorb_b`: the statement changes only `87 / 10` → `b1sym` (twice) — the
constants `39 / 1000`, `1 / 1000` and the third conjunct are byte-identical. Inside the proof, `set b := b1sym` makes it
opaque and the only fact about it used is `four_le_b1sym` (`hb4`, then `hb0 : 0 < b`, `hbC4 : 4 ≤ b * C₁`). Paper check
of the closing step: 2bC₁(Lℓ)² ≤ (39/1000)·4ℓ²(2bC₁)²L² ⟺ 2 ≤ 0.624·bC₁ ⟺ bC₁ ≥ 3.205, supplied by bC₁ ≥ 4; the
replaced intermediate ℓ + 73L ≤ (Lℓ)² holds from Lℓ ≥ 69 (L ≥ 50, ℓ ≥ 1.38): (Lℓ)² ≥ 69Lℓ ≥ 68·1.38L + 50ℓ ≥ 73L + ℓ.
The second conjunct (2e^{−L} ≤ U/1000) does not involve b, and U ≥ 1 uses b only through 1 ≤ 4·1.38²·(2·4)², i.e. b ≥ 4 again.
`clause6_assembly_b` vs `clause6_assembly` (`diff`): name, `hL2`, `hb1` deleted; the conclusion identical. At the
challenge level, §7's last bullet. **The root theorem's conclusion is unchanged.**

**(iii) The clause-7 double and the tight-pair statement.** `wsum_double_minus` states
`mult ⟨1/2, −t⟩ = 2 → wsum mult (ftest t L) ⟨1/2, −t⟩ = ↑(2 * (2 * t) ^ 2 * ‖paperFT B (−(2tL))‖ ^ 2)`: 2·4t² = 8t², the
value of check-O §12.3 ("m_ρ|h_f(−t)|² = 2·4t²B̂(2tL)² = 8t²B̂(2tL)²"), not the note body's 16t². Independent
numerics: at (t, L) = (30, 40), 2·(2t)²·B̂(2tL)² = **1.8083631·10⁻³¹** (`paper-numerics-AO.log`, 60-digit quadrature on
400 cells), which is check-O §12.3's "1.80836·10⁻³¹, half the note's figure" (the 16t² form gives 3.6167·10⁻³¹).
`wsum_double_plus` gives 0 at +t (h_f(t) = (t − t)B̂(0)), the note's first sentence. The tight-pair statement is the
note's §7.2: "Under the hypotheses of clause 6, let Z′ carry … an on-line double at ±t (the points t and −t each with
multiplicity two) and be otherwise as before. Then the same bound holds" — `separation_clause7_tight_pair` has all 17
hypotheses of `separation_clause6_assembly_b` verbatim plus `⟨1/2, t⟩ ∈ Z'.carrier`, `⟨1/2, −t⟩ ∈ Z'.carrier`,
`Z'.mult ⟨1/2, t⟩ = 2`, `Z'.mult ⟨1/2, −t⟩ = 2`, and the identical conclusion (the note's "|W_Z(f) − W_{Z′}(f)| ≥
δ²e^{δL/2} ≥ 1"). The value of the double is a solution-side lemma, not part of the statement — which is what the
challenge header says. **Non-vacuity**: C₁ = 2, t = L = 1000, δ = 1/2, Z = the orbit, Z′ = {1/2 ± 1000i} each with
multiplicity 2 is a `SepConfig 2` (reflection 1 − conj ρ fixes on-line points; conjugation swaps the two; local count
2 ≤ 2 log 1003), hL2 = 8·(1.933 + 1.386 + 3.784) = 56.8 ≤ 1000, (R*) holds (t_min(1000, ½) = 480.7), 2t = 2000 ≤ 73L so
both out-window sets are empty and H-out holds; the hypotheses are jointly satisfiable.

**(iv) `ChallengeDeps/Separation6b.lean` imports the frozen `ChallengeDeps.Separation6` and adds only `b1sym`.** §7.

**(v) The `linter.unusedVariables` option hides nothing else.** `set_option … in` scopes to the one declaration that
follows and changes a linter only, never elaboration or the kernel term. To see what it hides I re-elaborated both
tight-pair theorems with the option REMOVED (`verify-A-O/linter_probe_AO.lean.txt`, `linter-probe-AO.log`, exit 0): the
linter reports exactly four warnings — `hZ'plus`, `hZ'minus`, `hZ'plus2`, `hZ'minus2` not referenced — all in the
library copy; the solution-shaped copy (term-mode delegation) produces none. The four hypotheses are genuinely unused
because the conclusion is the assembly's and Z′ is already arbitrary on-line inside the window (note §7.2: "Nothing
else changes"); the builder records this as design note (iii). Nothing else is hidden.

**(vi) `rstar_of_21L`'s binder `25 / L ≤ δ` against the assembly's `25 / δ ≤ L`.** Ruling: **equivalent under the
hypotheses, and the label is honest as stated.** Kernel-checked in my probe (`verify-A-O/compose_probe_AO.lean.txt`,
`compose-probe-AO.log`, exit 0, all four on the standard three axioms):
* `probe_binders_equiv : 0 < δ → 0 < L → (25 / L ≤ δ ↔ 25 / δ ≤ L)`;
* `probe_assembly_to_corollary : 0 < δ → δ ≤ 1/2 → 25 / δ ≤ L → 50 ≤ L ∧ 25 / L ≤ δ` — the assembly's binders give
  every binder of `rstar_of_21L` except `21 * L ≤ t` (t ≥ 3 is common);
* `probe_corollary_to_assembly : 50 ≤ L → 25 / L ≤ δ → 0 < δ ∧ 25 / δ ≤ L` — and conversely;
* `probe_assembly_of_21L`: `separation_clause6_assembly_b` with `hRstar` REPLACED by `h21 : 21 * L ≤ t`, proved in
  four lines from the two Comparator-checked theorems `separation_clause6_assembly_b` and `rstar_of_21L`.
The corollary's conclusion `Separation.Rstar t δ L` is literally the assembly's hypothesis `hRstar` (same trusted
constant). So "(R*) implied by t ≥ 21L as a proved corollary" is exactly what is shipped. The composed form is not
itself a shipped theorem (recorded in FIDELITY (w1): "the two forms are not identified in Lean, so a user of both
supplies the assembly's form separately"); MINOR M1 in §13 suggests adding it — not required by the label.

**(vii) The record consequence L*(0.1, 10⁶; C₁ = 1).** L* = max(25/δ, (4/δ)(log log(3 + t) + 2 log(1/δ) +
log(2b₁C₁))). Recomputed (`paper-numerics-AO.log`): at b₁ = 8.70, **L* = 403.4973**; at b₁ = b₁sym = 10.98442,
**L* = 412.8235**; difference 9.3262 = 4·log(b₁sym/8.70)/0.1 = 4·0.2331550/0.1 exactly. **403.5 → 412.8 confirmed**
(25/δ = 250 is not the binding term at either value).

## §10 Paper re-derivation, from the Lean text — **CLEAN**

**(1) `abs_mul_norm_paperFT_Bc_le_integral`: |η|·‖B̂(η)‖ ≤ ∫‖D¹B‖.** One integration by parts: `paperFT_iteratedDeriv`
at k = 1 gives the transform of B′ as (−iη)·B̂(η) (up to the sign convention of `paperFT`), and `norm_paperFT_le` bounds
the transform of an integrable function supported in [−½, ½] by its L¹ norm at real η (weight e⁰ = 1). Taking norms:
|η|‖B̂(η)‖ ≤ ∫|B′|. This is tx_032's bound as note §5 uses it.

**(2) `integral_norm_deriv_Bc`: ∫|B′| = 2B(0) = 2e^{−1}/Z.** On |u| < ½, B_raw(u) = exp(−1/(1 − 4u²)) and
d/du[−(1 − 4u²)^{−1}] = −8u/(1 − 4u²)², so B′(u) = B(u)·(−8u)/(1 − 4u²)² (`hasDerivAt_Braw`, re-derived): ≤ 0 on [0, ½),
≥ 0 on (−½, 0]; B′ = 0 on |u| ≥ ½ (B vanishes on both closed rays; the one-sided derivative argument at the endpoints
is `deriv_B_eq_zero_of_half_le`). Hence ∫|B′| = ∫_{−½}^0 B′ − ∫_0^{½} B′ = (B(0) − B(−½)) − (B(½) − B(0)) = 2B(0),
and B(0) = e^{−1}/Z. Numerically 3.31427535947642 both ways (§7). The sign step is 60 lines (`hasDerivAt_Braw` …
`deriv_B_nonneg`, lines 66–146), inside the brief's 120-line stop line.

**(3) `four_le_b1sym`.** B_raw ≤ e^{−1} (−1/(1 − 4v²) ≤ −1 for 0 < 1 − 4v² ≤ 1), so Z ≤ e^{−1}·1, so
2e^{−1}/Z ≥ 2 and b₁sym ≥ 4. The only numeric fact about Z the b₁ side uses is this upper bound.

**(4) `wsum_double_minus`.** `wsum_real` gives the on-line summand m·‖h_f(γ)‖², `gammaOf ⟨1/2, −t⟩ = −t`, and
`paperFT_ftest` gives h_f(γ) = (γ − t)·B̂(L(γ − t)); at γ = −t: (−2t)·B̂(−2tL), so 2·‖·‖² = 2·(2t)²‖B̂(−2tL)‖² = 8t²B̂(2tL)²
(B real and even, so B̂ even). §9 (iii) for the numerical value.

**(5) `rstar_of_21L`, the chain.** With s = √(2tL): t ≥ 21L, L ≥ 50 give s² = 2tL ≥ 42L² ≥ (25L/4)² and s ≥ √(42·2500)
= 324.04. Upper bounds on the left of (R*): log((4t² + δ²)C_B²/(1.35δ²)) ≤ log(s⁴C_B²) = 4 log s + 2 log C_B, since
4t² + δ² ≤ 1.35δ²·4t²L² when δL ≥ 25; log s ≤ s/403 + 5 (tangent of log at e⁶ ≥ 403); log C_B ≤ log 25 + 2 (C_B = e²/Z
≤ 18e² from Z ≥ 1/18); δL/2 ≤ L/4 ≤ s/25. Lower bound on the right: −2 log(1 + (c_B/2)s) ≥ −2(log 25 + (1 + c_B s/2)/25 − 1)
(tangent at 25), and c_B s ≥ 0.1429s. The linear combination leaves (49/25·0.1429 − 1/25 − 4/403)·s − 22.08 − 4 log 25 =
0.230158·s − 34.955 ≥ **39.62 nats** at s = 324.04 with δL/2 bounded by s/25, and **40.09 nats** with δL/2 = 12.5 exact
(the builder's 40.1); increasing in s, so positive on the whole region. The exact (R*) margin at (1050, ½, 50) is
**50.3837 nats** (A1's 50.4); at (21000, ½, 1000) 1561.31 exact / 1465.87 chain (A1's 1561). Every step is one of the
lines the `linarith` call is given; the pricing's "≥ 47 nats" used sharper constants (tangent at s₀ = 324, Z ≥ 0.13), so
40 against 47 is the cost of the simpler chain, not an error. Positive margin: the stop line did not fire.

**(6) `inWindowNoise_le_b`.** The shell device `shell_sum_le` with a = b₁sym/L² (from `hb1sym`) and b = (64231/100)²/L⁶
(from H-B‴), then 4b ≤ a: 4·(642.31)²/L⁴ ≤ 4·412562/6.25·10⁶ = 0.264 ≤ 1 ≤ 4 ≤ b₁sym at L ≥ 50. Needs b₁ from below
only (pricing observation §0 (i), verified).

## §11 The three Comparator runs from the clean clone, with nanoda — **CLEAN**

Runner `verify-A-O/run-clone-A.sh` — the M4 (iii) checker's `run-clone-iii.sh` with the clone path changed (`diff`:
two lines, the comment and the `cd`), including its pre-run cleanup of `.lake/build/lib/lean/{Challenge, ChallengeDeps,
Solution, PrintAxioms}` and their `.olean/.ilean/.trace` siblings before each run, so comparator builds the comparator
layer itself. Comparator v4.33.0, lean4export v4.33.0-rc2, nanoda 0.4.17, `fake-landrun.sh` shim — five
`WARNING: THIS IS NOT REAL LANDRUN!` lines per run, as in every earlier record (Landlock is Linux-only; declared, not
sandboxed). All three from the clone root, one at a time, nothing else heavy running.

**(a) CONTROL — `comparator/config.json`, the parent's fifteen theorems** (`verify-A-O/control-run-AO.log`). Cleanup
removed 20 `ChallengeDeps` and 10 `Solution` artifacts first.

```
Build completed successfully (8699 jobs).
Build completed successfully (8877 jobs).
Nanoda kernel accepts the solution
Lean default kernel accepts the solution
Your solution is okay!
      150.00 real       140.71 user        15.29 sys
--- comparator exit code: 0 ---
```

8699 / 8877 are the D1, M4 (i), M4 (iii) and builder's figures. **The toolchain is alive on this machine.**

**(b) `comparator/config-separation-clause4b.json`** (`verify-A-O/comparator-run-clause4b-AO.log`). The comparator
layer was rebuilt from source (`Built ChallengeDeps.Separation (2.0s)`, `SepConfig (3.1s)`, …).

```
⚠ [8701/8701] Built Challenge.SeparationClause4b (3.1s)
warning: comparator/Challenge/SeparationClause4b.lean:39:8: declaration uses `sorry`
Build completed successfully (8701 jobs).
✔ [8710/8710] Built Solution.SeparationClause4b (3.1s)
Build completed successfully (8710 jobs).
Nanoda kernel accepts the solution
Lean default kernel accepts the solution
Your solution is okay!
       79.37 real        66.55 user        18.92 sys
--- comparator exit code: 0 ---
```

**(c) `comparator/config-separation6b.json`, three theorem names** (`verify-A-O/comparator-run-separation6b-AO.log`).
Cleanup removed 5 `Challenge`, 20 `ChallengeDeps` and 5 `Solution` artifacts first.

```
⚠ [8701/8701] Built Challenge.Separation6b (3.1s)
warning: comparator/Challenge/Separation6b.lean:56:8: declaration uses `sorry`
warning: comparator/Challenge/Separation6b.lean:77:8: declaration uses `sorry`
warning: comparator/Challenge/Separation6b.lean:97:8: declaration uses `sorry`
Build completed successfully (8701 jobs).
Exporting #[…, separation_clause6_assembly_b, separation_clause7_tight_pair, rstar_of_21L, propext, Quot.sound, Classical.choice, …]
✔ [8710/8710] Built Solution.Separation6b (3.2s)
Build completed successfully (8710 jobs).
Nanoda kernel accepts the solution
Lean default kernel accepts the solution
Your solution is okay!
       88.28 real        75.96 user        19.11 sys
--- comparator exit code: 0 ---
```

Job counts 8701 / 8710 and the `sorry` warnings (39:8; 56:8, 77:8, 97:8) match the builder's record exactly. **What the
runs establish**: each of the four statements in the solution modules coincides constant for constant with its
namesake in the challenge modules (the trusted `SepConfig`, `b1sym`, `HB3`, `Hedge`, `Rstar`, `Hout`, `ftest`, `W`
included); the proofs use no axiom outside the permitted three; nanoda re-checked each solution export and Lean's own
kernel replayed it.

## §12 Import discipline, the frozen statements, yaml, lint — **CLEAN**

**Imports (read in the clone).**

```
Zeta23/Separation/B1Sym.lean              import Zeta23.Separation.LemmaG
Zeta23/Separation/Assembly2.lean          import Zeta23.Separation.Assembly; import Zeta23.Separation.B1Sym
comparator/ChallengeDeps/Separation6b.lean import Mathlib; import ChallengeDeps.Separation6
comparator/Challenge/SeparationClause4b.lean  import ChallengeDeps.Separation6b
comparator/Challenge/Separation6b.lean    import ChallengeDeps.Separation6b
comparator/Solution/SeparationClause4b.lean   import ChallengeDeps.Separation6b; import Zeta23.Separation.Assembly2
comparator/Solution/Separation6b.lean     import ChallengeDeps.Separation6b; import Zeta23.Separation.Assembly2
comparator/PrintAxioms/*b.lean            import Solution.*b
```

Neither solution module imports a `Challenge.*` module; the trusted layer (`ChallengeDeps.*`) is Mathlib-only.

**The twelve frozen statements.** The builder's `verify-A/frozen_probe.lean.txt` run in my clone after building
`Solution.{Separation, SeparationG1, SeparationClause4, Separation6}` (8710 jobs): the 82-line output
(`verify-A-O/frozen-statements-AO.log`) is **byte-identical** to the body of the builder's `verify-A/frozen-statements.log`
(`diff` empty after its one header line), and, parsed per declaration, all 20 `#check`/`#print axioms` blocks of
`verify-iii/frozen-statements.log` (the six D1/R1 + three M4 (i) + G1 rung) are identical in my clone (the parser's one
apparent difference is that record's trailing comment line). The two M4 (iii) statements (`separation_clause4_in_window_noise`,
`separation_clause6_assembly`) appear with `87 / 10` and `Hb1` as frozen, on the standard three. 12 axiom lines, all
`[propext, Classical.choice, Quot.sound]`. Together with §7's SHA-256 match of the frozen files: the old pairs are
untouched.

**yaml.** `results/d1-m2a/dr8/validate_yaml_sigma_strong.py` on the mirror `lean/formalization.yaml` (`cmp`-identical
to the clone's): upstream schema IDENTICAL ×3, **VALIDATION errors: 0; RESULT: PASS — errors: 0, undeclared names: 0**;
main_results 24, alignment.statements 25 (`verify-A-O/yaml-validation-AO.log`). The binding label occurs verbatim in the
yaml (×2), `FIDELITY.md`, `BUILD-NOTES-A.md`, `Challenge/Separation6b.lean` and `Assembly2.lean`; no file of the unit
asserts "Theorem M2 is formalized" (every occurrence is under "never").

**Lint (10(g); U.S. English)** over the nine Lean files, `BUILD-NOTES-A.md`, `FIDELITY.md` (t)/(s)/(w), the Unit A
blocks of `SHARED.md` and the yaml additions (`verify-A-O/lint-AO.log`): the `-ise` hits are *noise*, *inWindowNoise*,
*otherwise*; the four 10(g) words occur once each, all on `BUILD-NOTES-A.md` line 112, which quotes the banned list.
No violation.

**Hashes and the mirror.** All 37 entries of `hashes-A.txt` recomputed: 37/37 SAME (`verify-A-O/hashes-A-recheck.log`;
tree files read in my clone, records in the repository). `BUILD-NOTES-A.md` SHA-256 `41e16774…aa81`, the value in the
builder's commit line. The mirror `rh-program/lean/` and the builder's tree agree on all 25 Separation-related files
(`cmp`).

## §13 MINOR items (recorded; no FIX-FIRST, no edit required)

* **M1 (optional).** The composition "assembly with t ≥ 21L in place of (R*)" is two lines from the two shipped theorems
  (my `probe_assembly_of_21L`, kernel-checked) but is not itself shipped; FIDELITY (w1) says so honestly. A fourth
  theorem in a later unit would let a reader cite one name.
* **M2.** `Assembly2.lean`'s header says "about 39 nats in this chain", BUILD-NOTES-A says 40.1; both are right (39.62 with
  δL/2 bounded by s/25, 40.09 with δL/2 = 12.5 exact). No statement depends on either.
* **M3.** In the challenge and solution files the `set_option linter.unusedVariables false in` is inert (the linter
  does not fire there, §9 (v)); only the library copy needs it. Harmless.

## §14 What I checked, and what I did not

**Checked, by running it in my own fresh clone:** provenance and overlay delta against upstream v1.0; the cold build
(9150 / 0); the two solution modules; `#print axioms` on the four roots and on 30 library declarations from my own list;
trust greps and my extra greps; statement identity by two extractions; the trusted file read in full and diffed; the
frozen probe and the frozen files' hashes; the three Comparator runs with nanoda; yaml validation; lint; hashes. **By
paper and independent numerics:** ∫|B′| = 2B(0), b₁sym ≥ 4, `absorb_b`'s closing inequality, the double's value
(1.80836·10⁻³¹ at (30, 40)), the `rstar_of_21L` chain and exact margins, L* = 403.5 → 412.8. **Kernel-checked probes of
my own:** the binder equivalence and the 21L composition (item (vi)); the linter re-elaboration (item (v)).
**Not checked:** the sandbox (the `fake-landrun.sh` shim, as in every earlier record; a Linux host with landrun would
close it); upstream v1.0's own library beyond building it.

---

## Verdict table

| # | Item | Verdict |
|---|---|---|
| 1 | Clone provenance (fresh clone, v1.0 `3635e748`) and overlay (175 new, 2 changed; `Zeta23.lean` +23 imports only) | **CLEAN** |
| 2 | Cold build `lake build Zeta23` | **CLEAN** (9150 jobs, 0 errors, 419 s) |
| 3 | `lake build Solution.SeparationClause4b Solution.Separation6b` | **CLEAN** (8711 jobs, 0 errors) |
| 4 | `#print axioms` — 4 roots + 30 library declarations | **CLEAN** (standard three ×34) |
| 5 | Trust greps (nine files) + extra greps | **CLEAN** (the 4 deliberate challenge `sorry`s only) |
| 6 | Statement identity ×4, two extractions | **CLEAN** |
| 7 | Trusted `ChallengeDeps/Separation6b.lean` read line by line; `b1sym` = library's; the frozen trusted files SHA-identical | **CLEAN** |
| 8 | Fidelity ledger (t1), (s1), (s2), (w1), (w2) | **CLEAN** (5/5; no unlisted weakening) |
| 9 (i) | No digit of b₁ and no lower bound on Z outside `rstar_of_21L`'s C_B step | **CLEAN** |
| 9 (ii) | `absorb_b` at 39/1000 and 1/1000 from b₁sym ≥ 4 only; root conclusion unchanged | **CLEAN** |
| 9 (iii) | Double = 2·(2t)²‖B̂(−2tL)‖² (check-O §12.3); tight pair = note §7.2 | **CLEAN** |
| 9 (iv) | `Separation6b.lean` imports frozen `Separation6`, adds only `b1sym` | **CLEAN** |
| 9 (v) | The linter option hides only the four unused tight-pair hypotheses | **CLEAN** |
| 9 (vi) | `25 / L ≤ δ` vs `25 / δ ≤ L`: equivalent under the hypotheses (kernel-checked); label honest | **CLEAN** |
| 9 (vii) | L*(0.1, 10⁶; C₁ = 1) = 403.4973 → 412.8235 (+9.3262 = 4·0.23316/0.1) | **CLEAN** |
| 10 | Paper re-derivation (∫|B′| = 2B(0); the `rstar_of_21L` chain, 39.6–40.1 nats vs exact 50.38) | **CLEAN** |
| 11 | Comparator ×3 from the clean clone with nanoda (CONTROL, Clause4b, Separation6b) | **CLEAN** (`Your solution is okay!` ×3, exit 0 ×3) |
| 12 | Import discipline; 12 frozen statements; yaml; lint; hashes 37/37 | **CLEAN** |

**OVERALL: CLEAN. No FIX-FIRST.** Three MINOR items in §13. The binding label holds as written:
*"Theorem M2's clause-6 assembly is a Comparator-checked theorem over `SepConfig`, modulo the displayed H-edge, H-B‴ and
H-out, on the three standard axioms, replayed by nanoda — with b₁ = ‖B′‖₁² proved, clause 7 folded, and (R*) implied by
t ≥ 21L as a proved corollary"*; and for the rung: *"clause 4 of Theorem M2 is kernel-checked modulo H-B‴, with
b₁ = ‖B′‖₁² proved."*
