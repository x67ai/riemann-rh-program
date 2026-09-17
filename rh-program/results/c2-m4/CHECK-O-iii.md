# C2 — M4 (iii): Theorem M2's clause-6 assembly over `SepConfig`, modulo displayed hypotheses, with its clause-4 rung — independent check (Session 23, Job 2, Opus 5, clean clone)

Task: `results/c2-m4/BRIEF-iii.md` "Job 2 — INDEPENDENT CHECKER"; contract `results/c2-m2/followups/PRICING.md` §1(a) items 4–8,
§1(b) candidate (iii) and its dress-rehearsal rung, §5(e)'s M4 line; builder's own checklist `results/c2-m4/BUILD-NOTES-iii.md` §5.
Object checked: the builder's work (Job 1, Fable 5.1, 2026-09-17, 13:05–14:20 IST) as recorded in `BUILD-NOTES-iii.md`,
`SHARED.md` (the M4 (iii) blocks) and `hashes-iii.txt`. Method precedent: `results/c2-m4/CHECK-O.md` (M4 (i)).

Nothing in the repository, the mirror or the working tree was modified by this job, and nothing was committed by it.
Everything in §§2–13 was produced in my own clone at `~/rh-lean-check-s23/clone`, reset to upstream **v1.0** (`git checkout -- .`
+ `git clean -fd`, verified clean and at `3635e74826a4c1fcece7d1cd2b6fa75e43a00510`) and re-overlaid with the current
`rh-program/lean/` mirror, never in `~/rh-lean-work/zeta-23-lean-main`.

---

## §0 Headline verdict

| # | Item | Verdict |
|---|---|---|
| 1 | Clone provenance and overlay (upstream v1.0 `3635e748`, `lean/README.md` recipe) | **CLEAN** |
| 2 | Cold build of the overlaid clone — `lake build Zeta23` | **CLEAN** (9148 jobs, 0 errors, 431.93 s) |
| 3 | `lake build Solution.SeparationClause4 Solution.Separation6` | **CLEAN** (8708 jobs, 0 errors) |
| 4 | `#print axioms` — the two root theorems and all 48 new library declarations (18 + 30) | **CLEAN** (standard three ×50; 0 `sorryAx`, 0 `ofReduceBool`) |
| 5 | Trust greps over the ten M4 (iii) files (`axiom`, `native_decide`, `unsafe`, `implemented_by`, `extern`, `opaque`, `sorry`, `admit`, `ofReduceBool`) | **CLEAN** (the 2 deliberate challenge `sorry`s only) |
| 6 | Statement byte-identity challenge/solution ×2 (rung 305 B, `Separation6` 903 B) | **CLEAN** (IDENTICAL ×2) |
| 7 | The trusted definitions `SepConfig`, `W`, `BL`, `ftest`, `Rstar`, `Hedge`, `Hb1`, `HB3`, `Hout` read line by line against PRICING §1(b)(iii) and the note | **CLEAN** (character for character; `ft` for `paperFT` as declared) |
| 8 | Fidelity ledger (p1)–(p8) and (q1)–(q8): each a real divergence, each recorded in yaml (p)/(q) and `FIDELITY.md` (p)/(q) | **CLEAN** (16/16; no unlisted weakening found) |
| 9 | **(q1) — the honesty of "clause 5 displayed whole"**, at every place the unit describes itself | **CLEAN** (8 places checked; no text claims H-R₀, clause 5, clause 7 or "Theorem M2 is formalized") |
| 10 | Paper re-derivation of the formal statement against the note's clause 6 as the addendum A1–A3 restates it | **CLEAN** — the formal statement is the note's, not weaker |
| 11 | Comparator ×3 from the clean clone with nanoda (CONTROL, `config-separation-clause4.json`, `config-separation6.json`), artifacts removed before each | **CLEAN** (`Your solution is okay!` ×3, exit 0 ×3) |
| 12 | Import discipline (the solution modules never import the challenge) | **CLEAN** |
| 13 | The nine frozen statements (six D1/R1 + three M4 (i)) + the G1 rung | **CLEAN** (49-line body byte-identical to the builder's log; the 28 D1/R1 `#check` lines identical to the M4 (i) record; 10 axiom lines all standard) |
| 14 | `formalization.yaml` schema validation (corrected apostrophe-safe regex) | **CLEAN** (errors 0, undeclared names 0; main_results 22, alignment.statements 23) |
| 15 | 10(g) lint over the ten Lean files, `BUILD-NOTES-iii.md`, `SHARED.md`; U.S. English | **CLEAN** |
| 16 | Standing order 7 — no novelty overclaim; the unit's claim is only "Comparator-checked modulo H" | **CLEAN** |
| 17 | Hashes: SHA-256 of every file in `hashes-iii.txt`, plus `BUILD-NOTES-iii.md`'s own | **CLEAN** (41/41 + 1) |
| 18 | Untouched: no existing Lean file edited except the two additive imports in `Zeta23.lean`; mirror = working tree | **CLEAN** (21/21 identical; frozen-area `git diff` empty) |

**OVERALL: CLEAN. No FIX-FIRST.** Three MINOR prose items are recorded in §14; none touches a statement, a constant, a
proof or a run, and none blocks the unit.

**Which close of the brief applies.** The brief's rule-5 "lands" sentence holds **with H-out in place of H-R₀**:

> *"Theorem M2's clause-6 assembly is a Comparator-checked theorem over `SepConfig`, modulo the displayed H-edge, H-b₁,
> H-B‴ and **H-out**, on the three standard axioms, replayed by nanoda."*

and the brief's "fails" close applies to the clause-5 step alone ("the assembly is stated with clause 5 displayed as a
hypothesis — still a shipped pair, with the label"). That is exactly how the builder states it, in every file. The rung's
close holds as written: *"clause 4 of Theorem M2 is a Comparator-checked theorem over `SepConfig`, modulo the displayed
H-b₁ and H-B‴, on the three standard axioms, replayed by nanoda."* I verified every clause of both sentences independently.

**Non-vacuity, checked (not asked for, but it is what makes the label mean anything).** All five displayed Props are true
statements of the record (H-b₁, H-B‴ are the note's computed constants; H-edge is clause 2's proved lower bound; H-out is
clause 5, a theorem of §6 + A3 at R₀ = 73), (R*) holds for t ≥ 21L (A1), and the configuration hypotheses are jointly
satisfiable — e.g. C₁ = 2, t = L = 1000, δ = 1/2, Z = the orbit alone (reflection- and conjugation-invariant, local count
2 ≤ 2 log 1003), Z′ = the empty configuration: hL1 = 50 ≤ 1000, hL2 = 54.95 ≤ 1000, (R*) holds (t_min(1000, ½) = 480.7 < 1000),
2t = 2000 ≤ 73L so both out-window sets are empty and H-out holds with 0 ≤ e^{−1000}. The theorem then asserts
‖W_Z − W_{Z′}‖ ≥ 0.25·e^{250}. The statement is not vacuously true.

---

## §1 Clone provenance and the overlay — **CLEAN**

The clone at `~/rh-lean-check-s23/clone` (made for the M4 (i) check from `https://github.com/anthropics/zeta-23-lean.git`)
was reset to pristine upstream before any overlay:

```
git checkout -- . ; git clean -fdq
git status --porcelain   -> (empty)
HEAD: 3635e74826a4c1fcece7d1cd2b6fa75e43a00510
v1.0: 3635e74826a4c1fcece7d1cd2b6fa75e43a00510
lean-toolchain  leanprover/lean4:v4.33.0-rc2
lakefile.toml   rev = "51e6992efd06126df61a496bebf8f49482a4e129"   (Mathlib)
```

This is the commit `lean/README.md` "Building" names and the toolchain/Mathlib pair of every record in this program.

**Overlay measured before copying.** A file-by-file `cmp` of all **166** mirror files (`rh-program/lean/**`) against the
clean v1.0 tree: **164 NEW, 2 CHANGED** (`README.md`, `Zeta23.lean`), 0 identical. The `Zeta23.lean` difference is
exactly **21 added `import` lines and nothing else** — the M4 (i) record's 19, plus

```
import Zeta23.Separation.Clause4
import Zeta23.Separation.Assembly
```

so BUILD-NOTES-iii's "the only edit to an existing Lean file" is confirmed against upstream, not merely against the
previous commit. Overlay applied by the README recipe (`Zeta23/`, `comparator/`, `Zeta23.lean`, plus `formalization.yaml`
and `README.md`); post-overlay `git status` in the clone lists 34 entries, all of them the program's own files.

**Cold.** Before the build I removed every program build product from the clone's `.lake`
(`.lake/build/lib/lean/{Zeta23,Zeta23.*,Challenge,ChallengeDeps,Solution,PrintAxioms}`), leaving only the Mathlib package
cache. The whole `Zeta23` library, the program's additions included, therefore recompiled from source (431.93 s wall).

**Mirror = tree.** All 21 files this build wrote or edited are `cmp`-identical between the repository mirror
`rh-program/lean/` and the working tree `~/rh-lean-work/zeta-23-lean-main` (`Zeta23.lean`, `formalization.yaml`, the four
`Zeta23/Separation/` files, the eleven `comparator/` Lean files, the two configs, the two M4 (i) configs' siblings).

**Untouched.** `git diff --stat 4cd0b31 HEAD` restricted to `lean/Zeta23/{DBN,W1,PairCeiling}`, the DBN comparator files and
`Zeta23/Separation/{LemmaG,LemmaG1}.lean` is **empty**.

Load discipline: `ps -Ao pcpu,comm | awk '$1>50'` empty before each build and before each comparator run; one `lake`
process at a time throughout; no `-j`; `caffeinate` running.

## §2 Cold build of the overlaid clone — **CLEAN**

`lake exe cache get` (`No files to download; Already decompressed 8681 file(s)`), then `lake build Zeta23`:

```
Build completed successfully (9148 jobs).
      431.93 real      2669.98 user       669.87 sys
```

* **Job count 9148** — exactly the builder's figure, and the M4 (i) record's 9146 plus the two new modules.
* **Errors: 0.** The only line matching `error` case-insensitively is the module name `Zeta23.XiPrime.ExplicitFormula.EntryError`.
* **Warnings: 191 lines beginning `warning:` (247 lines containing the word)** — the same two counts the M4 (i) checker
  measured. **None names a `Zeta23/Separation/` or `comparator/` path.** The only warnings from program modules are the
  two pre-existing ones in `Zeta23/PairCeiling/Stability.lean` (49:4, 245:4), present identically in the M4 (i) build log.
* The four `Separation` modules compiled from source: `Built Zeta23.Separation.LemmaG1 (4.3s)`,
  `LemmaG (5.7s)`, **`Clause4 (6.6s)`**, **`Assembly (12s)`**, and nothing downstream broke.

Log: `~/rh-lean-check-s23/build-zeta23-iii.log`.

## §3 The two Solution modules — **CLEAN**

`lake build Solution.SeparationClause4 Solution.Separation6`:

```
✔ [8704/8708] Built ChallengeDeps.Separation (2.9s)
✔ [8705/8708] Built ChallengeDeps.SepConfig (3.0s)
✔ [8706/8708] Built ChallengeDeps.Separation6 (3.3s)
✔ [8707/8708] Built Solution.SeparationClause4 (3.4s)
✔ [8708/8708] Built Solution.Separation6 (3.0s)
Build completed successfully (8708 jobs).
       15.54 real
```

0 errors, no warning from any new module. (The builder built them separately at 8705 and 8707; 8708 is the union, the
arithmetic one expects.)

## §4 `#print axioms` — **CLEAN**

**(a) The two Challenge theorems, through the builder's PrintAxioms files, in my clone.**

`lake env lean comparator/PrintAxioms/SeparationClause4.lean`:

```
'separation_clause4_in_window_noise' depends on axioms: [propext, Classical.choice, Quot.sound]
```

`lake env lean comparator/PrintAxioms/Separation6.lean`:

```
'separation_clause6_assembly' depends on axioms: [propext, Classical.choice, Quot.sound]
```

**(b) Every top-level declaration of the two new library files**, through the builder's scratch probes
(`verify-iii/axioms_clause4_probe.lean.txt`, `axioms_separation6_probe.lean.txt`, copied into `/tmp` and run with
`lake env lean` against my build):

* `Zeta23/Separation/Clause4.lean` — **18 lines, every one `[propext, Classical.choice, Quot.sound]`**
  (`BL_contDiff`, `BL_eq_zero_of_le`, `BLc_contDiff`, `BLc_support`, `hasCompactSupport_BLc`, `hasDerivAt_BLc`,
  `deriv_BLc`, `paperFT_BLc`, `paperFT_ftest`, `gammaOf_of_re_eq_half`, `abs_cube_mul_norm_paperFT_Bc_le`, `term_le_b1`,
  `term_le_B3`, `sum_inv_pow_four_le`, `sum_inv_pow_four_le'`, `window_count_le`, `shell_sum_le`, `inWindowNoise_le`).
* `Zeta23/Separation/Assembly.lean` — **30 lines, every one `[propext, Classical.choice, Quot.sound]`**
  (`B_even` … `clause6_assembly`, the full §2–§7 list of BUILD-NOTES-iii §2).

`grep -c "sorryAx\|ofReduceBool"` over both probe outputs: **0** and **0**. Total: **50 declarations on the standard three,
zero `sorryAx`.**

## §5 Trust greps — **CLEAN**

`trust_greps_m4iii.py <clone-root>` on all ten M4 (iii) files (`Zeta23/Separation/{Clause4,Assembly}.lean`,
`comparator/ChallengeDeps/{SepConfig,Separation6}.lean`, `comparator/Challenge/{SeparationClause4,Separation6}.lean`,
`comparator/Solution/{SeparationClause4,Separation6}.lean`, `comparator/PrintAxioms/{SeparationClause4,Separation6}.lean`),
comments stripped:

```
comparator/Challenge/SeparationClause4.lean:46: [sorry] sorry
comparator/Challenge/Separation6.lean:59: [sorry] sorry
files present: 10; hits outside comments: 2
```

Exactly the two deliberate challenge `sorry`s and nothing else. No `axiom`, `native_decide`, `unsafe`, `implemented_by`,
`extern`, `opaque`, `admit`, `ofReduceBool` anywhere outside comments.

## §6 Statement identity, challenge against solution — **CLEAN**

`statement_identity_m4iii.py <clone-root> SeparationClause4 separation_clause4_in_window_noise`:

```
separation_clause4_in_window_noise   challenge 305 bytes, solution 305 bytes: IDENTICAL
RESULT: PASS
```

`statement_identity_m4iii.py <clone-root> Separation6 separation_clause6_assembly`:

```
separation_clause6_assembly          challenge 903 bytes, solution 903 bytes: IDENTICAL
RESULT: PASS
```

903 bytes is the builder's recorded figure. The elaborated statement, as extracted from both files:

```
theorem separation_clause6_assembly (C₁ t δ L : ℝ) (hC : 1 ≤ C₁) (ht : 3 ≤ t) (hδ0 : 0 < δ) (hδ : δ ≤ 1 / 2)
    (hL1 : 25 / δ ≤ L)
    (hL2 : 4 / δ * (Real.log (Real.log (3 + t)) + 2 * Real.log (1 / δ) + Real.log (2 * (87 / 10) * C₁)) ≤ L)
    (hRstar : Separation.Rstar t δ L)
    (Z Z' : Separation.SepConfig C₁)
    (hZorb : Separation.orbit t δ ⊆ Z.carrier) (hZmult : ∀ ρ ∈ Separation.orbit t δ, Z.mult ρ = 1)
    (hZ : ∀ ρ ∈ Z.carrier, |ρ.im - t| ≤ 73 * L → ρ ∉ Separation.orbit t δ → ρ.re = 1 / 2)
    (hZ' : ∀ ρ ∈ Z'.carrier, |ρ.im - t| ≤ 73 * L → ρ.re = 1 / 2)
    (hb1 : Separation.Hb1) (hB3 : Separation.HB3) (hedge : Separation.Hedge)
    (houtZ : Z.Hout t L (73 * L)) (houtZ' : Z'.Hout t L (73 * L)) :
    δ ^ 2 * Real.exp (δ * L / 2)
        ≤ ‖Z.W (Separation.ftest t L) (Separation.ftest t L) - Z'.W (Separation.ftest t L) (Separation.ftest t L)‖ ∧
      1 ≤ δ ^ 2 * Real.exp (δ * L / 2)
```

## §7 The trusted definitions, read line by line — **CLEAN**

Read in full: `comparator/ChallengeDeps/SepConfig.lean` (125 lines) and `comparator/ChallengeDeps/Separation6.lean` (84
lines), against PRICING §1(b) candidate (iii), the note's §0.1–§0.2, §3.2, §4, §6, §7.1 and the addendum A1–A3.

**(a) `SepConfig` is PRICING §1(b)(iii)'s structure.** PRICING asks for "`ZeroConfig` + a field
`localCount : ∀ x, (carrier ∩ {|Re γ − x| ≤ 1}).ncard (with multiplicity) ≤ C₁·log(3 + |x|)` + conjugation invariance".
`SepConfig C₁` has, in this order:

* the **seven `ZeroConfig` fields character for character** — `carrier : Set ℂ`, `mult : ℂ → ℕ`, `one_le_mult`, `strip`,
  `reflect_mem`, `mult_reflect`, `finite_window` — verified by `diff` of `SepConfig.lean` 73–82 against `Zeta23/Defs.lean` 121–130 in the clone: **empty**, i.e. identical
  character for character, the two field docstrings included;
* **conjugation invariance with equal multiplicities** — `conj_mem`, `mult_conj` (the note's second symmetry, §0.1);
* the **local count** — `localCount : ∀ x : ℝ, ((∑ᶠ ρ ∈ carrier ∩ {ρ | |ρ.im - x| ≤ 1}, mult ρ : ℕ) : ℝ) ≤ C₁ * Real.log (3 + |x|)`.

The `Im ρ` in the window is the note's `Re γ_ρ`: `gammaOf ρ = (ρ − 1/2)/i`, so for ρ = β + iτ, γ_ρ = τ − i(β − ½), hence
Re γ_ρ = Im ρ and γ_ρ is real iff Re ρ = ½. That is the note's §0.1 dictionary, and `gammaOf_of_re_eq_half`
(`Clause4.lean` 129) is the Lean form of the second half. The `∑ᶠ` is finite because `finite_window` makes the window set
finite, so the field is not vacuous — recorded as (p2) and confirmed here.

`gammaOf` and `reflect` in the trusted file are **byte-identical** to `Zeta23.gammaOf` / `Zeta23.reflect` (`Defs.lean`
105, 108).

**(b) `W` is the note's datum.** `SepConfig.Wsummand` and `SepConfig.W` are byte-identical to
`Zeta23.ZeroConfig.Wsummand` / `.W` (`Defs.lean` 164–170) except that `ft` stands where `paperFT` stands — and
`Separation.ft` (`ChallengeDeps/Separation.lean` 49) is byte-identical to `Zeta23.paperFT` (`Defs.lean` 44):

```
def ft      (f : ℝ → ℂ) (z : ℂ) : ℂ := ∫ u : ℝ, f u * Complex.exp (Complex.I * z * (u : ℂ))
def paperFT (f : ℝ → ℂ) (z : ℂ) : ℂ := ∫ u : ℝ, f u * Complex.exp (Complex.I * z * (u : ℂ))
```

So `Z.W f f = Σ'_{ρ ∈ carrier} m_ρ h_f(γ_ρ) conj(h_f(conj γ_ρ))` — the note's W_Z(f) of §0.1 with the multiset written as
points with multiplicity, as §0.3 requires.

**(c) The remaining trusted objects, each against the note.** I diffed the `def` lines of the trusted layer against the
library's (`Zeta23.Separation.*`) mechanically; all are **IDENTICAL** except `Hb1`, whose only difference is `ft` for
`paperFT` — the declared convention:

| object | trusted text | the note's object |
|---|---|---|
| `BL L u` | `B (u / L) / L` | §0.1's B_L(u) = B(u/L)/L ✓ |
| `ftest t L u` | `I * (deriv (BL L) u : ℂ) * exp (−(I t u))` | §0.1's f_{t,L}(u) = i(B_L)′(u)e^{−itu} ✓ (Mathlib `deriv` of the C^∞ real B_L = the classical derivative) |
| `Hb1` | `∀ η, (\|η\| * ‖ft B η‖)^2 ≤ 87/10` | §5's b₁ = sup\|ηB̂\|², §12.2's certified upper end **8.70** ✓ (87/10) |
| `HB3` | `∫ u, ‖iteratedDeriv 3 B u‖ ≤ 64231/100` | §5's ‖B‴‖₁ = **642.301** ✓ (64231/100) |
| `orbit t δ` | `{⟨½+δ, t⟩, ⟨½−δ, t⟩, ⟨½+δ, −t⟩, ⟨½−δ, −t⟩}` | §0.2's four points γ = ±t ± iδ ✓ (checked through `gammaOf_mk`) |
| `edge l` | `∫ v, B v * cosh (l * v)` | §0.1's c(λ) = ∫B(v)cosh(λv)dv ✓ |
| `Hedge` | `∀ l ≥ 25, exp(l/2 − √l − (3/4)·log l + 148088/100000) ≤ edge l` | §3.2's clause-2 **lower** bound with λ₀ = 25 and **κ₋ = κ_∞ = 1.48088** ✓ (148088/100000) |
| `Rstar t δ L` | `δL/2 + log((4t² + δ²)·CB²/((27/20)·δ²)) ≤ 2·cB·√(2tL) − 2·log(1 + (cB/2)·√(2tL))` | addendum **A1's (R\*)** verbatim, with 1.35 = 27/20 ✓ |
| `outWindow t R` | `carrier ∩ {ρ \| R < \|ρ.im − t\|}` | the complement of the note's window, **strict** ✓ |
| `Hout t L R` | `Summable (fun ρ : outWindow => ‖Wsummand f f ρ‖) ∧ ‖∑' ρ : outWindow, Wsummand f f ρ‖ ≤ exp(−L)` | §6's clause 5 (b) with **R = 73L** (addendum A3) ✓ |

`cB = 2 / Real.sqrt (72 * Real.exp 1)` and `CB = Real.exp 1 ^ 2 / Z` are the M4 (i) trusted constants, already checked
character for character by `CHECK-O.md` §7; nothing in this unit redefines them.

**Every displayed constant is the note's**: 87/10 = 8.70 (§12.2's certified upper end), 64231/100 = 642.31 (§5),
148088/100000 = κ₋ (§3.2), 27/20 = 1.35 (A1), 73 = R₀ (A3), 25 = λ₀, 4 = C₀, 1/2 = c₀. **The (R\*) in Lean is the
addendum A1 form, in log form, exactly.** No constant appears in the Lean statements that is not on the record, and no
record constant that the statement needs is missing. The number **21** appears nowhere in the Lean (checked by grep) —
(q3), as declared.

**Is anything WEAKER or DIFFERENT from the note's clause 6 beyond (p1)–(p8) and (q1)–(q8)? No.** §10 re-derives the
statement and the proof chain; §8 checks each ledger row; the only places where the formal text departs from the note are
the sixteen listed ones, and each is recorded. One departure runs the *favorable* way and is worth naming explicitly:
`Hout` displays `‖Σ‖ ≤ e^{−L}` where the note's clause 5 proves the strictly stronger `Σ‖·‖ ≤ e^{−L}`. A *weaker
hypothesis* makes the theorem *stronger*, so this is not a fidelity gap; it is written out verbatim in (q1) and in the
`Hout` docstring, so a referee cannot mistake it.

## §8 The fidelity ledger, row by row — **CLEAN (16/16)**

Checked against `lean/formalization.yaml` `fidelity` (p), (q) and `results/d1-m2a/packaging/FIDELITY.md` (p), (q), which
carry the same text. "Real?" = is it a genuine difference from the note/PRICING; "Recorded?" = is it stated in both
ledgers; "Verdict" = my own check of the claim.

### The rung, (p1)–(p8)

| # | claim | Real? | Recorded? | Verdict |
|---|---|---|---|---|
| (p1) | b₁ = 87/10 and ‖B‴‖₁ = 64231/100 are rationals and **displayed**, not proved; the "proved b₁ ≤ ‖B′‖₁² = 10.99" substitute not taken because 4e⁻²/Z² ≤ 10.99 needs a numeric lower bound on Z | yes | yes | **CLEAN** — the reason given is correct: `Z` is `∫ v in (−1/2)..(1/2), Braw v`, an integral with no digit asserted anywhere in Lean ((o)(b)); PRICING §1(a) item 4's "prefer the proved value" is declined with a stated cost, which the brief's rule 3 permits |
| (p2) | the class is `SepConfig C₁` in ρ-coordinates; seven `ZeroConfig` fields + conj invariance + `∑ᶠ` local count; only `finite_window` and `localCount` are consumed | yes | yes | **CLEAN** — verified in §7(a); the solution passes exactly `Z.carrier Z.mult Z.finite_window Z.localCount` |
| (p3) | the note's "every in-window point other than the orbit is real" is **not** a hypothesis of the rung; `inWindowNoise` sums over the on-line points by definition | yes | yes | **CLEAN** — a strengthening, correctly identified as such; `inWindowReal t R = carrier ∩ {ρ.re = 1/2 ∧ \|ρ.im − t\| ≤ R}` |
| (p4) | polynomial route only; Σ_{k≥1}k⁻⁴ ≤ 2 in place of 2ζ(4) = 2.165; closes at L ≥ 50 (4‖B‴‖₁²/L⁴ ≤ 0.264 ≤ 8.70); T₁^{Gev} and the intermediate form not stated | yes | yes | **CLEAN** — I recomputed 4·(642.31)²/50⁴ = 0.2640 ≤ 8.70; `sum_inv_pow_four_le'` is Σ_{j=1}^{K} j⁻⁴ ≤ 2, true (ζ(4) = 1.0823) and cruder than the note's; the note's L₁ = 17.9 is indeed not needed |
| (p5) | shell index ⌊·⌋₊ so shell 0 is \|γ − t\| < 1 (the note's ≤ 1); shell k ≥ 1 by the two windows at t ± (k + ½); ℓ_R = log(4 + t + R) | yes | yes | **CLEAN** — `shell_sum_le`'s hypotheses `hA` (every in-window on-line point) and `hB` (k ≤ \|Im ρ − t\|, k ≥ 1) make the boundary point at distance exactly 1 land in shell 1 under the **stronger** ‖B‴‖₁ bound, as the row says; the conclusion `C₁·log(4+t+R)·(a + 4b)` is the note's C₁ℓ_R(b₁/L² + 4‖B‴‖₁²/L⁶) |
| (p6) | `ftest` with Mathlib `deriv`; (0.1) is the proved `paperFT_ftest` via `paperFT_deriv` and the scaling `paperFT_BLc` | yes (recorded, not a gap) | yes | **CLEAN** — `paperFT_ftest : paperFT (ftest t L) r = (r − t) * paperFT B (L * (r − t))`, which is (0.1) with B̂_L(z) = B̂(Lz) folded in |
| (p7) | N_Z written with ‖h_f(γ_ρ)‖² directly, not as the Weil summand restricted to real γ | yes | yes | **CLEAN** — and the identity of the two is supplied in the assembly (`wsum_real`, proved), so nothing is lost |
| (p8) | H-b₁ is the sup form over all real η; H-B‴ is the L¹ norm of D³ of the **complex-valued** B | yes | yes | **CLEAN** — `‖D³(B : ℝ → ℂ)‖ = |D³B|` pointwise is (o)(g); consumed in `abs_cube_mul_norm_paperFT_Bc_le` |

### The assembly, (q1)–(q8)

| # | claim | Real? | Recorded? | Verdict |
|---|---|---|---|---|
| **(q1)** | **clause 5 displayed WHOLE as H-out**, not proved modulo the one-point check H-R₀; the §6 + A3 chain not formalized; H-R₀ therefore absent; the window split is `≤ R` / `> R`, a genuine partition; when 2t > 73L the reflected pair lies in the out-window part and its smallness is part of H-out | yes | yes | **CLEAN — see §9 for the labeling audit.** Each sub-claim checked: `Hout` is exactly the displayed Prop; no Lean declaration mentions F̃, P, incomplete gammas or R₀-as-hypothesis; `W_decomp` partitions on `\|ρ.im − t\| ≤ R` vs `R < \|ρ.im − t\|`, disjoint and exhaustive; `re_tsum_offline_le`'s docstring states the 2t > 73L case correctly |
| (q2) | H-edge is clause 2's **lower** bound only, κ₋ as 148088/100000; κ₊ not displayed; clause 3 and A2's margin **derived** in Lean as c² ≥ 1.875e^{λ/2} (the note's 1.884) | yes | yes | **CLEAN** — `edge_sq_ge` re-derived on paper in §10(5); 1.875 is weaker than the note's e^{m(25)} = 1.8841 and the chain still closes with margin 0.01 |
| (q3) | (R\*) is a **hypothesis of the theorem**, not an "H-"; "t ≥ 21L ⟹ (R\*)" not derived; **21 appears nowhere in Lean** | yes | yes | **CLEAN** — the bare number `21` occurs **0** times outside comments in all ten files (comment-stripped scan); `Rstar` is the A1 form byte for byte |
| (q4) | constants as rationals (87/10, 64231/100, 25, 4, 73, 1/2, 27/20, 148088/100000); the L-hypothesis as two inequalities rather than one `max` | yes | yes | **CLEAN** — `25/δ ≤ L ∧ (4/δ)(…) ≤ L` is definitionally `L ≥ max(25/δ, (4/δ)(…))`; no loss |
| (q5) | orbit and window in ρ-coordinates; the four window hypotheses; the strip and the two invariances carried but not consumed | yes | yes | **CLEAN** — the library theorem `clause6_assembly` takes only `carrier, mult, hfin, hcount` per configuration, so the unconsumed fields are visibly unconsumed |
| (q6) | one noise term (D8): N_{Z′} ≥ 0 dropped; absorptions cruder than A2's (N ≤ 0.039U, 2e^{−L} ≤ 0.001U; margin 2·1.875 − 2.7 − 1 = 0.05 ≥ 0.04); the (1 − e^{−L}) form not stated | yes | yes | **CLEAN** — D8 is what note §7.1's proof explicitly permits and what addendum A1's displayed inequality uses; I re-derived N/U ≤ 0.011 at the worst point (§10(6)), well inside 0.039; the margin arithmetic is right |
| (q7) | **clause 7 is NOT folded in**; `ft f t = 0` and the tight pair not stated | yes | yes | **CLEAN** — grep confirms no declaration about a double at ±t or about `ft f t = 0`; PRICING candidate (ii) remains open, and the ledger says so |
| (q8) | `SepConfig.W` character for character `Zeta23.ZeroConfig.W`; on-line summand = m_ρ‖h_f(γ_ρ)‖² (`wsum_real`, proved) | yes (recorded, not a gap) | yes | **CLEAN** — verified in §7(b) and by reading `wsum_real` |

**No unlisted weakening found.** The two things a reader might mistake for one — `Hout`'s `‖Σ‖` (weaker hypothesis ⇒
stronger theorem) and the dropped `N_{Z′}` (D8, the note's own permission) — are both in the ledger, (q1) and (q6).

## §9 (q1) weighed hardest: is "clause 5 displayed whole" labeled honestly everywhere? — **CLEAN**

I checked every place the unit describes itself. The question in each: does the text say that clause 5 is a **hypothesis**
and not a theorem of this unit, and does any text claim H-R₀, clause 5, clause 7 or "Theorem M2 is formalized"?

| place | says clause 5 is displayed whole? | claims H-R₀ / clause 5 / clause 7 / "M2 formalized"? |
|---|---|---|
| `comparator/ChallengeDeps/Separation6.lean` header, `Hout` docstring | **yes** — "Clause 5 is a THEOREM of the note (§6, addendum A3 with R₀ = 73); its proof … is not formalized here and the clause is displayed whole — the 'fails' close of PRICING §5(e) / the brief's rule 5, recorded as such" | no |
| `comparator/Challenge/Separation6.lean` header | **yes** — "H-out for Z and for Z′ (clause 5: …)"; "What is NOT claimed: … clause 5 (displayed), clause 2 (displayed) … clause 7" | no; label line: *"never 'Theorem M2 is formalized'"* |
| `comparator/Solution/Separation6.lean` header | **yes** — label line verbatim | no |
| `Zeta23/Separation/Assembly.lean` header | **yes** — "H-out for Z and Z′ (clause 5, displayed whole: absolute convergence of the out-window sum beyond 73L and its bound e^{−L})" | no |
| `lean/formalization.yaml` — `project.description` (43–44), `status.scope` (145–146), the two `main_results` entries (378, 395–403), `fidelity` (q1) (580–586), `review.notes` | **yes** in all five — "H-out is clause 5 DISPLAYED WHOLE …, not proved modulo a one-point check" | no; the single occurrence of "H-R₀" in the whole file (line 582) reads "**not** proved modulo the one-point check H-R₀ the build brief asked for" |
| `results/d1-m2a/packaging/FIDELITY.md` (q), (q1) | **yes** — "(q1) clause 5 is displayed WHOLE (H-out), not proved modulo the one-point check H-R₀ the brief asked for … H-R₀ … is not among the displayed hypotheses because the chain that would consume it is absent" | no |
| `results/c2-m4/BUILD-NOTES-iii.md` (the binding-label paragraph, §2, §5) | **yes** — "What 'H-out' means, plainly: clause 5 … is DISPLAYED WHOLE … not proved modulo the one-point check H-R₀ that the brief's §3 asked for. That is the brief's rule-5 'fails' close for the clause-5 step … taken deliberately" | no |
| `results/c2-m4/SHARED.md` (the 13:52 and 14:05 blocks) | **yes** — "H-out replaces the brief's H-R₀ (clause 5 displayed whole — the brief's rule-5 'fails' close for that step, declared in FIDELITY (q1))" | no |

Mechanical confirmation: `grep -rno "H-R₀\|H-R0"` over `lean/Zeta23/Separation/`, `lean/comparator/`, `lean/formalization.yaml`,
`BUILD-NOTES-iii.md`, `SHARED.md`, `FIDELITY.md` returns **eight occurrences on seven lines** — **none of them in a Lean
source file** — and every one of them is a sentence saying H-R₀ is *absent* ("not proved modulo the one-point check H-R₀",
"H-out replaces the brief's H-R₀", "H-R₀ … is not among the displayed hypotheses", "no text says H-R₀"). `grep -rn "M2 is formalized\|theorem is formalized"` outside the "never …" label lines returns **nothing**.

**Verdict: the (q1) labeling is honest at every place, and the label the unit earns is the one it prints.** The debt is
stated precisely enough for a referee to price it: the missing item is note §6 + A3 (three incomplete-gamma integrals, the
Laurent polynomial P, the one-point check F₁₃(50; 73) ≤ −0.3227 and the decrease from L = 6.11), the brief's ~900-line item.

**And the conclusion is the note's clause 6.** `δ^2 * exp(δ*L/2) ≤ ‖Z.W f f − Z'.W f f‖ ∧ 1 ≤ δ^2 * exp(δ*L/2)` is, letter
for letter, note §7.1's "**≥ δ²e^{(1−c₀)δL} ≥ 1**" at c₀ = ½ — and the addendum A1's restatement
"|W_Z(f) − W_{Z′}(f)| ≥ 2δ²c(δL)² − 2.7δ²e^{δL/2} − N − 2e^{−L} ≥ δ²e^{δL/2} ≥ 1, with N := 2b₁C₁ℓ_R/L² (one noise term,
which the proof of §7.1 allows — D8)". The one-noise-term accounting D8 is therefore exactly what the note permits, and the
addendum's own A2 margin computation uses it. The Lean conclusion is stated with ‖·‖ of the complex difference, which is
≥ |Re| — at least as strong as the note's statement about the real datum.

## §10 Paper re-derivation, from the Lean text — **CLEAN**

I re-derived the chain the builder says is proved inside, from the Lean statements only, and checked each step against the
note. Write U := δ²e^{δL/2}, c := c(δL) = `edge (δ*L)`, G := `Gmaj`.

**(1) The four-point accounting (note §0.2).** `gammaOf_mk : gammaOf ⟨a, b⟩ = b − (a − ½)i`. So the orbit's points map to
γ = t ∓ δi (at +t) and γ = −t ∓ δi (at −t) — `gammaOf_orbit_plus`, `gammaOf_orbit_minus`. `paperFT_ftest_sub_I` /
`_add_I` give h_f(t − si) = −si·c(sL) and h_f(t + si) = si·c(sL), which is (0.1) at r = t ∓ si combined with
B̂_L(∓iδ) = B̂(∓iLδ) = c(δL) (`paperFT_Bc_neg_I_mul` / `_I_mul`, from the evenness of B). Then `wsum_of_gammaOf_eq`:
a multiplicity-one point with γ_ρ = t − si contributes (−si·c)·conj(si·c) = −s²c², i.e. **−δ²c(δL)²** at s = ±δ (the
s = −δ case closing through `edge_neg`, c(−λ) = c(λ)). `wsum_orbit_plus` gives both points of the pair at +t. Total
**−2δ²c(δL)²**. *This is §0.2 exactly, including the sign, which comes from (−i)² = i² = −1 and not from a convention.*

**(2) Clause 1's reflected-pair bound from Lemma G's complex form (note §4).** `norm_paperFT_ftest_reflected`:
‖h_f(−t − si)‖ ≤ √(4t² + δ²)·e^{δL/2}·G(2tL) for |s| = δ. Derivation in the file: (0.1) gives
h_f(−t − si) = (−2t − si)·B̂(L(−2t − si)); |−2t − si| = √(4t² + s²) = √(4t² + δ²); and Lemma G's complex form
`norm_paperFT_Bc_le z : ‖B̂(z)‖ ≤ exp(|z.im|/2)·G(|z.re|)` at z = L(−2t − si), where z.re = −2tL and |z.im| = Lδ, gives
e^{δL/2}G(2tL). *This is the note's "Lemma G's complex case with ξ = −2tL, η′ = ±δL" verbatim.* Multiplying the two
factors (`norm_wsum_reflected`) gives **(4t² + δ²)e^{δL}G(2tL)² per reflected point**, hence **2(4t² + δ²)e^{δL}G(2tL)²**
for the pair — the note's bound on |E₋|.

**(3) Absorption under (R\*) (addendum A1).** `rstar_exp`: `Rstar t δ L` ⟹ 2(4t² + δ²)e^{δL}G(2tL)² ≤ (27/10)·δ²e^{δL/2}.
On paper: `Rstar` is δL/2 + log[(4t² + δ²)C_B²/((27/20)δ²)] ≤ 2c_Bs − 2log(1 + (c_B/2)s) with s = √(2tL); exponentiating and
rearranging, (4t² + δ²)·C_B²(1 + (c_B/2)s)²e^{−2c_Bs} ≤ (27/20)δ²e^{−δL/2}, i.e. (4t² + δ²)G(2tL)² ≤ (27/20)δ²e^{−δL/2};
multiply by 2e^{δL}. **≤ 2.7U.** *This is A1's proof line for line ("after dividing by 2δ²e^{δL} and taking logarithms …
which is (R\*)"), with 2.7 = 2·1.35.*

**(4) The decomposition (note §7.1, with referee O's MINOR (d)).** `W_decomp`: for R = 73L,
Σ'_{carrier} = Σ'_{|Im ρ − t| ≤ R ∧ Re ρ ≠ ½} + Σ'_{Re ρ = ½ ∧ |Im ρ − t| ≤ R} + Σ'_{R < |Im ρ − t|}, with the first two
finite by `finite_window` and the third summable by H-out's first conjunct. The three sets are pairwise disjoint and cover
the carrier: **a genuine partition**, with the boundary |Im ρ − t| = R assigned to the in-window side. That is PRICING's
"corrected partition" and referee O's MINOR (d): the reflected pair is assigned to clause 1 when it is in the window
(2t ≤ 73L) and to H-out when it is not (2t > 73L), and never to both. `re_tsum_offline_le` then bounds the first part:
its index set is contained in the orbit (`hZ`) and contains the two points at +t (`hZorb`, δ > 0), so its real part is at
most **−2δ²c² + 2(4t² + δ²)e^{δL}G(2tL)²**. `tsum_inWindow_eq` + `wsum_real` identify the second part with the rung's
real N_Z (for real γ, h_f(γ)conj(h_f(conj γ)) = |h_f(γ)|²). `hA'` kills Z′'s off-line in-window part (empty by `hZ'`).

**(5) H-edge ⟹ c² ≥ 1.875·e^{λ/2} (note §3.3 / A2).** `edge_sq_ge`. Squaring `Hedge` gives
c(λ)² ≥ exp(λ − 2√λ − (3/2)log λ + 2κ₋) = e^{λ/2}·e^{m(λ)} with m(λ) = λ/2 − 2√λ − (3/2)log λ + 2κ₋ — the note's m.
Lean then bounds m below by two elementary steps: √λ ≤ λ/10 + 5/2 (from (√λ − 5)² ≥ 0, valid for all λ ≥ 0) and
log λ ≤ log 25 + (λ/25 − 1) (from log x ≤ x − 1), together with log 25 ≤ 3.221173 and log 1.875 ≤ 0.63, both proved from
`Real.exp_one_gt_d9` and truncated exponential series (`log25_le`, `log_1875_le`). Arithmetic:
m(λ) ≥ (½ − ⅕ − 3/50)λ − 5 + 3/2 + 2κ₋ − (3/2)log 25 = 0.24λ − 5.36996, which at λ = 25 is **0.63004 ≥ 0.63 = the bound
used for log 1.875**, and increases in λ. So c² ≥ 1.875e^{λ/2} for λ ≥ 25. *The note's own value is e^{m(25)} = 1.8841;
Lean's 1.875 is weaker by 0.0091 and is declared in (q2). The step is the note's §3.3 with cruder elementary bounds.*

**(6) The L-hypothesis absorptions (note §7.1 (7.1) / addendum A2).** `absorb` proves, from `hL1 : 25/δ ≤ L` and
`hL2 : (4/δ)(log log(3+t) + 2log(1/δ) + log(2·(87/10)·C₁)) ≤ L`:

* **N := 2·(87/10)·C₁·log(4 + t + 73L)/L² ≤ 0.039·U.** On paper, from hL2, δL/2 ≥ 2Q with
  Q = log ℓ + 2log(1/δ) + log(17.4C₁), ℓ := log(3+t); so e^{δL/2} ≥ ℓ²δ^{−4}(17.4C₁)² and
  U = δ²e^{δL/2} ≥ ℓ²δ^{−2}(17.4C₁)² ≥ 4ℓ²(17.4C₁)². Hence N/U ≤ ℓ_R/(69.6·C₁·L²ℓ²) with ℓ_R ≤ ℓ + 73L
  (log(4+t+73L) ≤ log((3+t)(1+73L)) ≤ ℓ + 73L). At the worst admissible point (ℓ ≥ log 4 = 1.386 as `absorb` uses,
  C₁ ≥ 1, L ≥ 50): N/U ≤ (1.386 + 3650)/(69.6·2500·1.922) = **0.0109**, comfortably inside 0.039, and decreasing in both
  L and ℓ. *The note's A2 obtains 9.3·10⁻⁵ with the sharper ℓ_R accounting; Lean's 0.039 is cruder, as (q6) says.*
* **2e^{−L} ≤ 0.001·U.** With U ≥ 1 and L ≥ 50: 2e^{−50} = 3.9·10⁻²² ≤ 10⁻³. ✓
* **U ≥ 1**, i.e. δL/2 ≥ 2log(1/δ). From hL2, δL/2 ≥ 2(log ℓ + 2log(1/δ) + log(17.4C₁)) ≥ 2·2log(1/δ) since
  log ℓ ≥ log 1.386 > 0 and log(17.4C₁) > 0. *The note's §7.1 closing line, with the same factor to spare.*

Note that `hL1 : 25/δ ≤ L` with δ ≤ ½ gives **L ≥ 50**, which is what clause 4's rung needs (and what clause 5's own
L-hypothesis needs, since 4/δ ≥ 8 — §7.1's remark).

**(7) The final chain (note §7.1 / A1's displayed inequality).** In `clause6_assembly`, after `W_decomp` on both
configurations and `hA' = 0`:

```
Re(W_{Z′} − W_Z) = (N_{Z′} + Re O_{Z′}) − (Re A_Z + N_Z + Re O_Z)
                 ≥ 0 − e^{−L} − (−2δ²c² + 2.7U) − 0.039U − e^{−L}
                 = 2δ²c² − 2.7U − 0.039U − 2e^{−L}
                 ≥ 2·1.875·U − 2.7U − 0.039U − 0.001U        (edge_sq_ge; absorb)
                 = (3.75 − 2.7 − 0.039 − 0.001)U = 1.01·U ≥ U = δ²e^{δL/2}
```

and `‖W_Z − W_{Z′}‖ ≥ Re(W_{Z′} − W_Z)` by `Complex.re_le_norm` after `norm_sub_rev`. The `linarith` call at
`Assembly.lean` 641 takes exactly these nine facts. **Margin 0.01 in units of U** (the note's A2 margin, with its sharper
constants, is 0.0681). Second conjunct: U ≥ 1 from `absorb`.

**Verdict on the re-derivation: every step is the note's.** (1) is §0.2; (2) is §4's proof of clause 1's explicit bound;
(3) is A1; (4) is §7.1's split with referee O's MINOR (d) correction and the strict/non-strict convention; (5) is §3.2 →
§3.3 with elementary replacements; (6) is (7.1)'s accounting; (7) is A1's displayed inequality in the one-noise-term form
D8 that §7.1's proof and A2 both use. No step assumes anything the note does not, and none concludes less than the note
does.

**Clause 4's route, likewise re-derived (note §5).** Every term of N_Z is (γ − t)²B̂(L(γ − t))² ≥ 0 by (0.1)
(`paperFT_ftest` + `gammaOf_of_re_eq_half`); `term_le_b1` bounds it by b₁/L² for every point (H-b₁), `term_le_B3` by
‖B‴‖₁²/(L⁶k⁴) when k ≤ |γ − t|, k ≥ 1 (three integrations by parts: `paperFT_iteratedDeriv` at k = 3 through
`abs_cube_mul_norm_paperFT_Bc_le`, H-B‴). `window_count_le` turns `localCount` into a bound on any finite family inside a
unit window. `shell_sum_le` fibers the finite in-window set by k = ⌊|Im ρ − t|⌋₊ and sums: shell 0 ≤ C₁log(3+t) ≤ C₁ℓ_R
points at a each; shell k ≥ 1 ≤ 2C₁ℓ_R points (the two windows at t ± (k + ½), the note's D7) at b/k⁴ each; Σ_{k≥1}k⁻⁴ ≤ 2
gives **C₁ℓ_R(a + 4b)**. With a = b₁/L², b = ‖B‴‖₁²/L⁶ and 4b ≤ a at L ≥ 50 (4·642.31²/50⁴ = 0.264 ≤ 8.70):
**N_Z ≤ 2b₁C₁ℓ_R/L²**. *This is §5's theorem, with the factor 2 in the shell count that D4(a) records and the polynomial
route D4(b) prefers.*

## §11 The three Comparator runs from the clean clone, with nanoda — **CLEAN**

Runner `~/rh-lean-check-s23/run-clone-iii.sh` (the M4 (i) checker's `run-clone.sh` with an explicit pre-run cleanup step
that removes `.lake/build/lib/lean/{Challenge,ChallengeDeps,Solution,PrintAxioms}` and their top-level `.olean`/`.ilean`/
`.trace` siblings before each run, so comparator builds the comparator layer itself). Comparator v4.33.0,
lean4export v4.33.0-rc2, nanoda 0.4.17, `fake-landrun.sh` shim — five `WARNING: THIS IS NOT REAL LANDRUN!` lines per run,
as in the D1 and M4 (i) records (Landlock is Linux-only; declared, not sandboxed). All three from the clone root, one at a
time, nothing else heavy running.

**(a) CONTROL — `comparator/config.json`, the parent's fifteen theorems.** Cleanup removed 15 `ChallengeDeps` and 20
`Solution` artifacts first.

```
Build completed successfully (8699 jobs).      (challenge side)
Build completed successfully (8877 jobs).      (solution side)
Nanoda kernel accepts the solution
Running Lean default kernel on solution.
Lean default kernel accepts the solution
Your solution is okay!
--- comparator exit code: 0 ---
      148.21 real       138.93 user        14.57 sys
```

8699 / 8877 are the D1, M4 (i) and M4 (iii) records' figures exactly. **The toolchain is alive on this machine.**

**(b) `comparator/config-separation-clause4.json`.**

```
✔ [8698/8699] Built ChallengeDeps.SepConfig (3.0s)
⚠ [8699/8699] Built Challenge.SeparationClause4 (2.9s)
warning: comparator/Challenge/SeparationClause4.lean:42:8: declaration uses `sorry`
Build completed successfully (8699 jobs).
✔ [8705/8705] Built Solution.SeparationClause4 (3.0s)
Build completed successfully (8705 jobs).
Nanoda kernel accepts the solution
Lean default kernel accepts the solution
Your solution is okay!
--- comparator exit code: 0 ---
       70.72 real        61.79 user        15.26 sys      5 887 983 616 max RSS
```

Job counts 8699 / 8705 and the single `sorry` warning at 42:8 match the builder's record.

**(c) `comparator/config-separation6.json`.** Cleanup removed 5 `Challenge`, 10 `ChallengeDeps` and 5 `Solution` artifacts
first.

```
✔ [8697/8700] Built ChallengeDeps.Separation (2.9s)
✔ [8698/8700] Built ChallengeDeps.SepConfig (2.0s)
✔ [8699/8700] Built ChallengeDeps.Separation6 (2.9s)
⚠ [8700/8700] Built Challenge.Separation6 (2.9s)
warning: comparator/Challenge/Separation6.lean:46:8: declaration uses `sorry`
Build completed successfully (8700 jobs).
✔ [8707/8707] Built Solution.Separation6 (3.1s)
Build completed successfully (8707 jobs).
Exporting #[…, separation_clause6_assembly, propext, Quot.sound, Classical.choice, …] from Solution.Separation6
Running nanoda kernel on solution
Nanoda kernel accepts the solution
Running Lean default kernel on solution.
Lean default kernel accepts the solution
Your solution is okay!
--- comparator exit code: 0 ---
       82.39 real        72.10 user        16.59 sys      5 939 429 376 max RSS
```

Job counts 8700 / 8707 and the `sorry` warning at 46:8 match the builder's record. **What the run establishes**: the
statement in `Solution.Separation6` coincides constant for constant with its namesake in `Challenge.Separation6`
(the trusted `SepConfig`, `Hb1`, `HB3`, `Hedge`, `Rstar`, `Hout`, `ftest`, `W` included); the proof uses no axiom outside
the permitted three; nanoda re-checked the whole solution export and Lean's own kernel replayed it.

Logs: `~/rh-lean-check-s23/{control-run-iii.log, comparator-run-clause4-iii.log, comparator-run-separation6-iii.log}`.

## §12 Import discipline, frozen statements, yaml, lint — **CLEAN**

**Imports (read in the clone).**

```
Zeta23/Separation/Clause4.lean          import Zeta23.Separation.LemmaG
Zeta23/Separation/Assembly.lean         import Zeta23.Separation.Clause4
comparator/ChallengeDeps/SepConfig.lean import Mathlib; import ChallengeDeps.Separation
comparator/ChallengeDeps/Separation6.lean  import Mathlib; ChallengeDeps.Separation; ChallengeDeps.SepConfig
comparator/Challenge/SeparationClause4.lean import ChallengeDeps.SepConfig
comparator/Challenge/Separation6.lean   import ChallengeDeps.Separation6
comparator/Solution/SeparationClause4.lean  import ChallengeDeps.SepConfig; import Zeta23.Separation.Clause4
comparator/Solution/Separation6.lean    import ChallengeDeps.Separation6; import Zeta23.Separation.Assembly
comparator/PrintAxioms/*.lean           import Solution.*
```

**Neither solution module imports a `Challenge.*` module**, and neither trusted `ChallengeDeps` module imports `Zeta23`.
The trusted layer is Mathlib-only, as the headers claim.

**Frozen statements.** `verify-iii/frozen_probe.lean.txt` run in my clone after building `Solution.Separation` and
`Solution.SeparationG1` (8704 jobs): the 49-line output is **byte-identical** to the body of the builder's
`verify-iii/frozen-statements.log` (the only diff lines are that log's own `#` header and footer comments). Against the
earlier M4 (i) record `verify/frozen-statements.log`: the **28 `#check` lines of the six D1/R1 statements are identical, in
order** (`cert_of_checkW1`, `cert_of_checkW1_ap`, `cert_of_checkW1_fDH`, `cert_of_checkW1_of_diffOn`, `mpDH_zero`,
`arbDH_zero`). All **10** `#print axioms` lines (the six plus the three M4 (i) Lemma G roots plus the G1 rung) read
`[propext, Classical.choice, Quot.sound]`.

**`formalization.yaml` schema validation.** `results/d1-m2a/dr8/validate_yaml_sigma_strong.py` (PyYAML 6.0.3,
jsonschema 4.25.1; the three upstream schema files re-fetched and **IDENTICAL** to the on-disk copies):

```
VALIDATION errors: 0
main_results: 22   alignment.statements: 23   fidelity.divergences: 16611 chars
Lean names referenced in status.main_results + alignment.statements: 59
RESULT: PASS — errors: 0, undeclared names: 0
```

The apostrophe-safe `declared()` regex is the corrected one (primed names such as `cert_of_checkW1_of_diffOn'` resolve),
and the six new names — `Zeta23.Separation.{inWindowNoise_le, shell_sum_le, paperFT_ftest, clause6_assembly, W_decomp,
re_tsum_offline_le, rstar_exp, edge_sq_ge, absorb}` — all resolve to their files.

**10(g) lint.** No occurrence of "clearly", "obviously", "easy to see", "easily seen", "well known" or "well-known" in any
of the ten Lean files, `BUILD-NOTES-iii.md` or `SHARED.md` (the single hit is `BUILD-NOTES-iii.md` line 55, which is the
lint statement itself). **U.S. English** throughout: no `behaviour`, `colour`, `centre`, `analyse`, `recognise`,
`normalis*`, `characteris*`, `labelled`, `modelling`, `licence`, `defence`, `maths`, `grey`, `programme`, `towards`.

**Standing order 7.** The unit claims only "Comparator-checked modulo H-edge, H-b₁, H-B‴, H-out" (assembly) and "modulo
H-b₁, H-B‴" (rung). Nothing in the ten Lean files, the ledgers or `BUILD-NOTES-iii.md` claims new mathematics: PRICING
§1(c) already says M4 "is not new mathematics; nothing in §1(b) proves anything the note does not already prove", and the
files say the same. No novelty sentence was added by this unit.

## §13 Hashes — **CLEAN (41/41 + 1)**

`shasum -a 256 -c results/c2-m4/hashes-iii.txt`: **41 of 41 entries OK, 0 failures.** That covers all fourteen `lean/`
files and configs, `FIDELITY.md`, `BUILD-NOTES-iii.md`, `BRIEF-iii.md` and the twenty-four `verify-iii/` artifacts.

`BUILD-NOTES-iii.md`'s own SHA-256, recomputed:
`2ed307321a946f154a95150f0895e65c0a3dbce7d71724b07cc8bc2cf1bf5bdd` — identical to the value `SHARED.md`'s final block
records and to the entry in `hashes-iii.txt`.

SHA-256 of this file is in the chat report accompanying it.

## §14 MINOR items (recorded; no FIX-FIRST, no edit required)

1. **`Zeta23/Separation/Assembly.lean` module header, line 27** says "the L-hypothesis absorptions N ≤ (6/100)δ²e^{δL/2}".
   The theorem `absorb` proves the sharper **39/1000**, and the `absorb` docstring (line 490), `BUILD-NOTES-iii.md` §2,
   `FIDELITY.md` (q6) and the yaml all say 0.039. The header's statement is *true* (0.039 < 0.06) but is not the proved
   constant. One-line fix if the record wants it: in `Assembly.lean` line 27, replace `N ≤ (6/100)δ²e^{δL/2}` by
   `N ≤ (39/1000)δ²e^{δL/2}`.
2. **`SHARED.md`, the 13:52 IST block** gives line counts 79 for `ChallengeDeps/Separation6.lean` and 67 for
   `Challenge/Separation6.lean`; the shipped files are **84** and **59**. The block is explicitly headed "(in progress)"
   and is superseded by the 14:05 block, which gives 84 and 59 correctly. A progress log, not a claim of record.
3. **`BRIEF-iii.md`'s "Sources the builder reads first"** cites the note as "§4 (clause 4, in-window noise), §5 (clause 5,
   out-window), §7 (clause 6 assembly)"; the note's own numbering is §4 = clause 1, §5 = clause 4, §6 = clause 5,
   §7.1 = clause 6. The builder used the correct sections (`BUILD-NOTES-iii.md` cites §4, §5, §6, §7.1). An orchestrator
   typo in the brief, with no effect on the work.

## §15 What I checked, and what I did not (standing order 5)

**Checked, by running it in my own clone:** the clone's reset to pristine v1.0 and its toolchain pins; the overlay delta
against upstream (164 NEW / 2 CHANGED, `Zeta23.lean` = +21 imports only); the cold `lake build Zeta23` (9148 jobs,
0 errors, warnings attributed); the two Solution builds; `#print axioms` for the two Challenge theorems and for all 48 new
library declarations; the nine trust greps with comments stripped; challenge/solution statement identity for both
theorems; the line-by-line reading of both trusted files against PRICING §1(b)(iii) and the note; the byte identity of
`gammaOf`, `reflect`, `Wsummand`, `W`, `BL`, `ftest`, `Hb1`, `HB3`, `orbit`, `edge`, `Hedge`, `Rstar` against the library's
and of `ft` against `Zeta23.paperFT`; the import graph of every new module; all three Comparator runs with nanoda, each
after removing the comparator-layer artifacts; the nine frozen statements plus the G1 rung; the yaml schema validation and
the name-declaration sweep; the 10(g) and U.S.-English lint; all 41 SHA-256 values plus `BUILD-NOTES-iii.md`'s own;
`git diff` over the frozen areas; mirror = working tree for 21 files; the (q1) labeling at eight places.

**Re-derived on paper, from the Lean text:** the four-point accounting; clause 1's reflected-pair bound from Lemma G's
complex form; (R\*)'s exponentiation to |E₋| ≤ 2.7δ²e^{δL/2}; the three-way partition and the assignment of the reflected
pair; H-edge ⟹ c² ≥ 1.875e^{λ/2} including the two elementary inequalities and the 0.63004 ≥ 0.63 arithmetic; the three
L-hypothesis absorptions including N/U ≤ 0.0109 at the worst admissible point; the final chain with its 0.01 margin; and
clause 4's shell sum with 4‖B‴‖₁²/L⁴ = 0.264 ≤ 8.70. Each against note §0.2, §3.2–§3.3, §4, §5, §7.1 and addendum A1–A3.
I read `check-O.md` §4–§7 and the two corrections sections afterwards; they agree with my derivation.

**Not checked, and why.**
* **The correctness of Mathlib and of upstream Zeta23.** `Zeta23.paperFT_deriv`, `norm_paperFT_le`,
  `paperFT_iteratedDeriv`, `Measure.integral_comp_mul_left`, `Finset.sum_fiberwise_of_maps_to`,
  `summable_subtype_iff_indicator` and `Real.sum_le_exp_of_nonneg` are taken as given; they are upstream, kernel-checked,
  and outside this unit's scope. I did read the statements of the first three to confirm the Lean route uses them as the
  note's proof does.
* **Lemma G itself.** `norm_paperFT_Bc_le` is the M4 (i) theorem, already independently checked in `CHECK-O.md` §9. Here it
  is consumed, not re-derived; the brief's stop condition on H-G did not fire and no H-G is displayed.
* **The five displayed hypotheses are not verified as facts here.** H-b₁ (8.70) and H-B‴ (642.301) are quadrature results
  of `verify/b1_constant_run.log`; H-edge is note §3.2; H-out is note §6 + A3. That they are *true* is the note's business
  and its Opus checks'; that they are *displayed and labeled* is this unit's, and they are.
* **The sandbox.** The comparator runs use the `fake-landrun.sh` shim (five `WARNING: THIS IS NOT REAL LANDRUN!` lines per
  run), because Landlock is Linux-only. A referee who wants the sandbox re-runs
  `lake env comparator comparator/config-separation6.json` on a Linux host with landrun. Same limitation as the D1 and
  M4 (i) records, declared there and here.
* **Human review of the trusted text.** No human has read `ChallengeDeps/{SepConfig,Separation6}.lean` or
  `Challenge/Separation6.lean` against the note. This report is a second machine's independent check;
  `review.status: self-assessed` is the honest label and it stays.
* **Anything about ζ or RH.** Nothing here bears on either. The theorem is about two abstract configurations and one
  explicit test; clause 8 of the note is scope, not content, and neither the Lean files nor the ledgers claim otherwise.
  The ζ instance (`zeta_in_class_C1` with C₁ ≤ 2.4·10⁹) that PRICING §1(b)(iii) mentions is **not** in Lean and is not
  claimed to be.

## §16 Traceability

| what | where |
|---|---|
| clean clone, reset to v1.0 and re-overlaid | `~/rh-lean-check-s23/clone` (HEAD `3635e74826a4c1fcece7d1cd2b6fa75e43a00510`) |
| cold `lake build Zeta23`, 9148 jobs, 431.93 s, 0 errors | `~/rh-lean-check-s23/build-zeta23-iii.log` |
| `lake build Solution.SeparationClause4 Solution.Separation6`, 8708 jobs | `~/rh-lean-check-s23/build-solutions-iii.log` |
| CONTROL comparator run, PASS, 148.21 s | `~/rh-lean-check-s23/control-run-iii.log` |
| `config-separation-clause4.json` run, PASS, 70.72 s | `~/rh-lean-check-s23/comparator-run-clause4-iii.log` |
| `config-separation6.json` run, PASS, 82.39 s | `~/rh-lean-check-s23/comparator-run-separation6-iii.log` |
| the builder's record under check | `results/c2-m4/BUILD-NOTES-iii.md`, `SHARED.md` (the 13:15–14:10 blocks), `hashes-iii.txt`, `verify-iii/` |
| the contract | `results/c2-m2/followups/PRICING.md` §1(a) items 4–8, §1(b) candidates (ii)–(iii), §5(e); `results/c2-m4/BRIEF-iii.md` |
| the mathematics | `results/c2-m2/separation-note.md` §0.1–§0.2, §3.2–§3.3, §4, §5, §6, §7.1, §12.2, §12.8, both corrections sections, addendum A1–A3; `results/c2-m2/check-O.md` §4–§7 |
| the ledgers | `lean/formalization.yaml` (project description, `status.scope`, two `main_results`, `fidelity` (p), (q), two `review.notes`, two `alignment.statements`); `results/d1-m2a/packaging/FIDELITY.md` (p), (q) |
| the precedent | `results/c2-m4/CHECK-O.md` (M4 (i)); `results/d1-m2a/dr8/CHECK-sigma-strong-O.md` |
