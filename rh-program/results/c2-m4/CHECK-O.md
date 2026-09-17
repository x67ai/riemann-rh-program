# C2 — M4 (i): Lemma G of Theorem M2 as Comparator-style Lean pairs — independent check (Session 23, Job 2, Opus 5, clean clone)

Task: `results/c2-m4/BRIEF.md` "Job 2 — INDEPENDENT CHECKER"; contract `results/c2-m2/followups/PRICING.md` §1(b)
candidate (i) and its dress-rehearsal rung; builder's own checklist `results/c2-m4/BUILD-NOTES.md` §5. Object checked:
the builder's work (Job 1, Fable 5.1, 2026-09-17) as recorded in `BUILD-NOTES.md`, `SHARED.md`, `hashes.txt`.
Method precedent: `results/d1-m2a/dr8/CHECK-sigma-strong-O.md`.

Nothing in the repository, the mirror or the working tree was modified by this job, and nothing was committed by it.
Everything in §§2–9 was produced in my own fresh clone at `~/rh-lean-check-s23/clone`, never in
`~/rh-lean-work/zeta-23-lean-main`.

---

## §0 Headline verdict

| # | Item | Verdict |
|---|---|---|
| 1 | Clone provenance and overlay (upstream v1.0 `3635e748`, `lean/README.md` recipe) | **CLEAN** |
| 2 | Cold build of the overlaid clone — `lake build Zeta23` | **CLEAN** (9146 jobs, 0 errors) |
| 3 | `lake build Solution.SeparationG1 Solution.Separation` | **CLEAN** (8704 jobs, 0 errors) |
| 4 | `#print axioms` — the four root theorems and all 51 new library declarations | **CLEAN** |
| 5 | Trust greps (`axiom`, `native_decide`, `unsafe`, `implemented_by`, `extern`, `opaque`, `sorry`, `admit`, `ofReduceBool`) | **CLEAN** (the 4 deliberate challenge `sorry`s only) |
| 6 | Statement identity challenge/solution, and against PRICING §1(b)(i) and the note's Lemma G | **CLEAN** (identical ×4) |
| 7 | Trusted definitions `Braw`, `Z`, `B`, `ft`, `cB`, `CB` versus the library's and versus `Zeta23.paperFT` | **CLEAN** (character for character) |
| 8 | Fidelity ledger (a)–(g) and (n1)–(n5): each a real divergence, each recorded in yaml (n)/(o) and `FIDELITY.md` (n)/(o) | **CLEAN** |
| 9 | Paper re-derivation of the formal statements against the note's Lemma G and its constants | **CLEAN** — the formal statements are the note's, not weaker |
| 10 | Comparator ×3 from the clean clone with nanoda (CONTROL, `config-separation-g1.json`, `config-separation.json`) | **CLEAN** (`Your solution is okay!` ×3, exit 0 ×3) |
| 11 | Import discipline (the solution modules never import the challenge) | **CLEAN** |
| 12 | The six frozen D1/R1 statements against the σ-strong record | **CLEAN** (character for character) |
| 13 | `formalization.yaml` schema validation (corrected regex) | **CLEAN** (errors 0, undeclared names 0) |
| 14 | 10(g) lint over the nine new Lean files, `BUILD-NOTES.md`, `SHARED.md` | **CLEAN** |
| 15 | Standing order 7 — nothing claimed as novel that should not be | **CLEAN** |
| 16 | Hashes: SHA-256 of every file in `hashes.txt`, plus `BUILD-NOTES.md`'s own | **CLEAN** (35/35 + 1) |
| 17 | Untouched: no existing Lean file edited except the two additive imports in `Zeta23.lean` | **CLEAN** |

**OVERALL: CLEAN. No FIX-FIRST.** Two MINOR prose inaccuracies in `BUILD-NOTES.md` are recorded in §11; neither
touches a statement, a proof, a constant or a run, and neither blocks the unit.

**The label the unit earns, checked:** *"Lemma G — |B̂(η)| ≤ (e²/Z)(1 + (c_B/2)√|η|)e^{−c_B√|η|} with c_B = 2/√(72e)
for the bump B — is a Comparator-checked theorem over Mathlib's `expNegInvGlue`, with no displayed hypothesis, axioms
propext/Classical.choice/Quot.sound, replayed by nanoda."* I verified every clause of that sentence independently.
PRICING §5(e)'s alternative ("G1 is checked and G is stated with G1 displayed as H-G1") does not apply: G is proved.

---

## §1 Clone provenance and the overlay — **CLEAN**

`git clone https://github.com/anthropics/zeta-23-lean.git` into `~/rh-lean-check-s23/clone` (a new clone from the
network, made for this check; not a reuse of `checker-clone-s20` or `-s21`), then `git checkout v1.0`:

```
HEAD 3635e74826a4c1fcece7d1cd2b6fa75e43a00510
lean-toolchain  leanprover/lean4:v4.33.0-rc2
lakefile.toml   rev = "51e6992efd06126df61a496bebf8f49482a4e129"   (Mathlib)
```

This is the commit `lean/README.md` "Building" names, and the toolchain/Mathlib pair the record uses throughout.

**Overlay measured before copying.** A file-by-file `cmp` of all **154** mirror files (`rh-program/lean/**`) against the
clean v1.0 tree: **152 NEW, 2 CHANGED** (`README.md`, `Zeta23.lean`), 0 identical. The `Zeta23.lean` difference is
exactly **19 added `import` lines and nothing else** — the σ-strong record's 17, plus

```
import Zeta23.Separation.LemmaG1
import Zeta23.Separation.LemmaG
```

so the builder's "the only edit to an existing Lean file is two additive imports" is confirmed against upstream, not
merely against the previous commit. Overlay applied by the README recipe (`Zeta23/`, `comparator/`, `Zeta23.lean`,
plus `formalization.yaml` and `README.md`); post-overlay `git status` in the clone lists 23 entries, all of them the
program's own files.

**Mirror = tree.** All thirteen files the build wrote or edited are `cmp`-identical between the repository mirror
`rh-program/lean/` and the working tree `~/rh-lean-work/zeta-23-lean-main` (`Zeta23.lean`, the two
`Zeta23/Separation/` files, the seven `comparator/` files, the two configs, `formalization.yaml`).

**Untouched.** `git diff --stat eed6cde HEAD -- lean/` (`eed6cde` is the last commit before the M4 (i) work) lists
exactly thirteen paths: the twelve new files plus `Zeta23.lean` (+2) and `formalization.yaml` (+131/−4). The same diff
restricted to `lean/Zeta23/{DBN,W1,PairCeiling}` and every `comparator/*DBN*` path is **empty**.

Load discipline: `ps -Ao pcpu,comm | awk '$1>50'` empty before each build and before each comparator run; one `lake`
process at a time throughout; no `-j`; `caffeinate` running.

## §2 Cold build of the overlaid clone — **CLEAN**

`lake exe cache get` (`No files to download; Decompressed 8489 already-cached file(s)`), then `lake build Zeta23`:

```
Build completed successfully (9146 jobs).
      411.94 real      2621.41 user       649.79 sys       6.33 GB max RSS
```

* **Job count 9146** — exactly the builder's figure, and the σ-strong record's 9144 plus the two new modules.
* **Errors: 0.** No line of the log matches `error` at all.
* **Warnings: 191 lines beginning `warning:` (247 lines containing the word, 63 `⚠` module lines) — none from a program
  module.** No warning names any path under `Zeta23/Separation/`, `Zeta23/W1/`, `Zeta23/DBN/` or `comparator/`; all are
  upstream deprecations (`Set.mem_setOf_eq`, `MeasureTheory.integral_finset_sum`, …). The builder's "247 warning lines"
  is the count of lines containing the word and my clone reproduces it exactly.
* The two new modules compiled from source: `Built Zeta23.Separation.LemmaG1 (3.0s)`,
  `Built Zeta23.Separation.LemmaG (6.3s)`, and nothing downstream broke.
* 412 s is a genuinely cold build (nothing in this clone's `.lake` before today); the builder's 6.13 s was a warm
  rebuild of an already-compiled tree.

Log: `~/rh-lean-check-s23/build-zeta23.log`.

## §3 The two Solution modules — **CLEAN**

`lake build Solution.SeparationG1 Solution.Separation`:

```
✔ [8702/8704] Built ChallengeDeps.Separation (2.9s)
✔ [8703/8704] Built Solution.SeparationG1 (3.4s)
✔ [8704/8704] Built Solution.Separation (3.4s)
Build completed successfully (8704 jobs).
```

0 errors, no warning from any new module. (The builder built them separately: 8701 and 8703; 8704 is the union, which
is the arithmetic one expects.)

## §4 `#print axioms` — **CLEAN**

**(a) The four Challenge theorems, through the builder's PrintAxioms files, in my clone.**

`lake env lean comparator/PrintAxioms/SeparationG1.lean`:

```
'separation_braw_iteratedDeriv_le' depends on axioms: [propext, Classical.choice, Quot.sound]
```

`lake env lean comparator/PrintAxioms/Separation.lean`:

```
'separation_bump_fourier_decay' depends on axioms: [propext, Classical.choice, Quot.sound]
'separation_bump_fourier_decay_complex' depends on axioms: [propext, Classical.choice, Quot.sound]
'separation_bump_fourier_decay_pure_exp' depends on axioms: [propext, Classical.choice, Quot.sound]
```

Exactly the standard three, and **no displayed hypothesis appears in any of the four** (§6 prints the elaborated
statements: they are closed, with no `H-…` premise).

**(b) Sweep over EVERY top-level declaration of the two new library files.** My own probe
(`~/rh-lean-check-s23/verify/probe_axioms.lean`), generated mechanically from the two sources with block comments
stripped so prose cannot produce a false name: **51 declarations** (26 in `LemmaG1.lean`, 25 in `LemmaG.lean` — the
number the BUILD-NOTES declaration tables imply). Result:

* **50** print exactly `[propext, Classical.choice, Quot.sound]`;
* **1** prints `[propext]` alone — `Zeta23.Separation.pow_mul_pow_le`, the pure-ℕ inequality i^i(k−i)^{k−i} ≤ k^k, a
  strict subset of the permitted three;
* **zero** occurrences of `sorryAx`, `Lean.ofReduceBool`, or any other axiom.

Output: `~/rh-lean-check-s23/verify/probe_axioms.out`.

## §5 Trust greps (10(j)) — **CLEAN**

`trust_greps_m4.py <clone-root>` (the builder's script, run by me against my clone; it strips nested `/- -/` blocks and
`--` line comments before matching the nine words `axiom`, `native_decide`, `unsafe`, `implemented_by`, `extern`,
`opaque`, `sorry`, `admit`, `ofReduceBool`), over all nine new Lean files:

```
comparator/Challenge/SeparationG1.lean:40: [sorry] sorry
comparator/Challenge/Separation.lean:44: [sorry] sorry
comparator/Challenge/Separation.lean:53: [sorry] sorry
comparator/Challenge/Separation.lean:60: [sorry] sorry
files present: 9; hits outside comments: 4
```

Exactly the four deliberate challenge `sorry`s and nothing else. A raw grep with no comment stripping adds only six
further hits, every one inside a file header explaining that the `sorry` is deliberate or that `sorryAx` must not
appear. **Nothing under `Zeta23/Separation/` contains a `sorry`.**

## §6 Statement identity, and what the statements say — **CLEAN**

**(a) Challenge versus Solution, byte for byte** (`statement_identity_m4.py`, my run, my clone):

```
separation_braw_iteratedDeriv_le              challenge 174, solution 174: IDENTICAL   RESULT: PASS
separation_bump_fourier_decay                 challenge 219, solution 219: IDENTICAL
separation_bump_fourier_decay_complex         challenge 269, solution 269: IDENTICAL
separation_bump_fourier_decay_pure_exp        challenge 218, solution 218: IDENTICAL   RESULT: PASS
```

**(b) Against PRICING §1(b)(i)'s displayed statements.** Read side by side, the four agree with the contract clause
for clause:

| PRICING §1(b)(i) | Lean, as built |
|---|---|
| rung: `∀ k ≥ 1, ∀ v, \|iteratedDeriv k Braw v\| ≤ (k + 1)·(72/e)^k·k^{2k}` | `∀ k : ℕ, 1 ≤ k → ∀ v : ℝ, \|iteratedDeriv k Separation.Braw v\| ≤ ((k : ℝ) + 1) * (72 / Real.exp 1) ^ k * (k : ℝ) ^ (2 * k)` |
| (G1) `∀ η : ℝ, ‖ft (fun v => (B v : ℂ)) η‖ ≤ CB·(1 + (cB/2)·√\|η\|)·exp(−cB·√\|η\|)` | `‖Separation.ft (fun v => (Separation.B v : ℂ)) η‖ ≤ Separation.CB * (1 + Separation.cB / 2 * Real.sqrt \|η\|) * Real.exp (-(Separation.cB * Real.sqrt \|η\|))` |
| complex form `∀ z : ℂ, ‖ft B z‖ ≤ exp(\|z.im\|/2)·G(\|z.re\|)` | `… ≤ Real.exp (\|z.im\| / 2) * (Separation.CB * (1 + Separation.cB / 2 * Real.sqrt \|z.re\|) * Real.exp (-(Separation.cB * Real.sqrt \|z.re\|)))` — G written out |
| (G2) with `cB′ = (7/8)cB`, `CB′ = 4e^{−3/4}CB` | `… ≤ 4 * Real.exp (-3 / 4) * Separation.CB * Real.exp (-(7 / 8 * Separation.cB * Real.sqrt \|η\|))` |

**(c) Elaborated statements, from my own build** (`#check` against `Solution.Separation`, `Solution.SeparationG1`):

```
separation_braw_iteratedDeriv_le : ∀ (k : ℕ),
  1 ≤ k → ∀ (v : ℝ), |iteratedDeriv k Separation.Braw v| ≤ (↑k + 1) * (72 / Real.exp 1) ^ k * ↑k ^ (2 * k)
separation_bump_fourier_decay : ∀ (η : ℝ),
  ‖Separation.ft (fun v => ↑(Separation.B v)) ↑η‖ ≤
    Separation.CB * (1 + Separation.cB / 2 * √|η|) * Real.exp (-(Separation.cB * √|η|))
separation_bump_fourier_decay_complex : ∀ (z : ℂ),
  ‖Separation.ft (fun v => ↑(Separation.B v)) z‖ ≤
    Real.exp (|z.im| / 2) * (Separation.CB * (1 + Separation.cB / 2 * √|z.re|) * Real.exp (-(Separation.cB * √|z.re|)))
separation_bump_fourier_decay_pure_exp : ∀ (η : ℝ),
  ‖Separation.ft (fun v => ↑(Separation.B v)) ↑η‖ ≤
    4 * Real.exp (-3 / 4) * Separation.CB * Real.exp (-(7 / 8 * Separation.cB * √|η|))
```

No premise other than `1 ≤ k` in the rung. **No displayed hypothesis anywhere** — this is the program's first
Comparator statement carrying no "modulo H" label, and the claim is true as stated.

**(d) The trusted definitions, read by me.** `comparator/ChallengeDeps/Separation.lean` imports **Mathlib only** and
defines, in namespace `Separation`:

```
def Braw (v : ℝ) : ℝ := if |v| < 1 / 2 then Real.exp (-1 / (1 - 4 * v ^ 2)) else 0
def Z : ℝ := ∫ v in (-1 / 2 : ℝ)..(1 / 2), Braw v
def B (v : ℝ) : ℝ := Braw v / Z
def ft (f : ℝ → ℂ) (z : ℂ) : ℂ := ∫ u : ℝ, f u * Complex.exp (Complex.I * z * (u : ℂ))
def cB : ℝ := 2 / Real.sqrt (72 * Real.exp 1)
def CB : ℝ := Real.exp 1 ^ 2 / Z
```

Compared mechanically against `Zeta23/Separation/LemmaG1.lean` §1 and against `Zeta23/Defs.lean` line 44:

```
Braw   IDENTICAL   Z   IDENTICAL   B   IDENTICAL   cB  IDENTICAL   CB  IDENTICAL
ft vs paperFT (after renaming ft → paperFT): IDENTICAL
    dep: def ft       (f : ℝ → ℂ) (z : ℂ) : ℂ := ∫ u : ℝ, f u * Complex.exp (Complex.I * z * (u : ℂ))
    lib: def paperFT  (f : ℝ → ℂ) (z : ℂ) : ℂ := ∫ u : ℝ, f u * Complex.exp (Complex.I * z * (u : ℂ))
```

**So yes: `Separation.ft` is `Zeta23.paperFT` verbatim** (the paper's h_f(z) = ∫ f(u)e^{izu}du: sign +i, no 2π, complex
argument), and **the constants are the note's**: `cB = 2/√(72e)` and `CB = e²/Z` with `Z` the integral of `Braw` over
[−1/2, 1/2], as separation-note §2 states them.

## §7 Paper re-derivation from the Lean statement — **CLEAN, the formal statement is the note's**

Re-derived by me from the Lean text, independently of the builder's prose and of `check-O.md` §4 (which I then read and
which agrees).

**G1.** With g = `expNegInvGlue`, `Braw v = g(4v + 2)·g(2 − 4v)`: for |v| < 1/2 put x = v + ½ ∈ (0,1), then
1 − 4v² = 4x(1 − x) and 1/(4x(1−x)) = 1/(4x) + 1/(4(1−x)); off the interval one factor vanishes. The affine chain rule
gives 4^k·(18/e)^k k^{2k} per factor from Zeta23's `Taper.abs_iteratedDeriv_g_le`, so Leibniz gives
Σ_i C(k,i)·4^k(18/e)^k·[i^i(k−i)^{k−i}]². Splitting each term as [C(k,i)i^i(k−i)^{k−i}]·[i^i(k−i)^{k−i}] and bounding
the first by k^k (one nonnegative term of `add_pow` for (i + (k−i))^k) and the second by k^i·k^{k−i} = k^k gives
k + 1 terms each ≤ (72/e)^k k^{2k}. That is **exactly** the note's step (iii) and **exactly** what
`choose_mul_pow_mul_pow_le` / `pow_mul_pow_le` / `choose_mul_sq_le` / `choose_mul_gb_le` prove. The Lean theorem is
stated for **every** k (k = 0 reads |B_raw| ≤ 1 with 0⁰ = 1), i.e. it is **stronger** than the note's k ≥ 1; the
challenge keeps the note's binder.

**Lemma G, complex form.** Set s = |Re z| and κ = (c_B/2)√s. Then κ = √s/√(72e), which is the note's
κ = √(|η|/A₁)/e with A₁ = 72/e (√(s·e/72)/e = √s/√(72e)); and c_B√s = 2κ. The Lean `key_ineq` hypothesis
(72/e)κ² = s/e² holds identically: κ² = s/(72e).

* κ ≥ 1, k = ⌊κ⌋₊ ≥ 1: (72/e)k² ≤ (72/e)κ² = s/e², so (72/e)^k k^{2k} = ((72/e)k²)^k ≤ (s/e²)^k; k + 1 ≤ 1 + κ; and
  e^{−2k} ≤ e²e^{−2κ} because κ < k + 1. Hence (k+1)(72/e)^k k^{2k}/Z ≤ (e²/Z)(1+κ)e^{−2κ}s^k = C_B(1+κ)e^{−2κ}s^k.
  Dividing the k-fold-integration-by-parts bound ‖B̂(z)‖·s^k ≤ e^{|Im z|/2}(k+1)(72/e)^k k^{2k}/Z by s^k > 0 gives the
  stated inequality. This is the note's display, line for line.
* κ < 1: ‖B̂(z)‖ ≤ e^{|Im z|/2}·∫‖B‖ = e^{|Im z|/2}, and C_B(1+κ)e^{−2κ} ≥ C_Be^{−2} = 1/Z ≥ 1 because Z ≤ 1. The note's
  branch, with the same two inputs (∫B = 1 and Z ≤ 1), both proved in Lean (`integral_norm_Bc`, `Z_le_one`).

The strip weight: Lean gets e^{|Im z|·Λ} with Λ = 1/2 from `Zeta23.norm_paperFT_le` applied to the support
[−1/2, 1/2] — the note's |e^{iζv}| = e^{η′v} ≤ e^{|η′|/2}. Since the note writes ζ = ξ − iη′, |Im ζ| = |η′| and
Re ζ = ξ, so **e^{|Im z|/2}·G(|Re z|) is the note's e^{|η′|/2}·G(|ξ|)**, identically.

**G2.** (1 + x/2)e^{−x} ≤ 4e^{−3/4}e^{−7x/8} ⟺ 1 + x/2 ≤ 4e^{(x−6)/8}, which follows from e^t ≥ 1 + t at
t = (x − 6)/8: 4(1 + (x−6)/8) = 4 + x/2 − 3 = 1 + x/2. The note obtains the same constant by maximizing
(1 + s/2)e^{−s/8} at s = 6 (value 4e^{−3/4}). Same c_B′ = (7/8)c_B, same C_B′ = 4e^{−3/4}C_B. Lean's `G2_aux` holds for
all real x, so it is at least as strong.

**(G1) real form** is the complex form at z = (η : ℂ) (`Complex.ofReal_im`, `ofReal_re`), which is how the note gets it.

**Conclusion.** The formal statements are the note's Lemma G with the note's constants. **In no respect is the formal
statement weaker than or different from the prose one beyond the seven divergences (a)–(g) of PRICING §1(b)(i)**, and in
two respects (G1 for all k; G2_aux for all real x) it is stronger. No FIX-FIRST on fidelity.

## §8 The fidelity ledger, item by item — **CLEAN**

Each row: is it a real divergence, and is it recorded in `lean/formalization.yaml` (paragraph (n) or (o)) and in
`results/d1-m2a/packaging/FIDELITY.md` (section (n) or (o))?

| Item | What it says | A divergence? | Recorded in yaml | Recorded in FIDELITY.md | Verified by me against the files |
|---|---|---|---|---|---|
| (a) | B defined by the exp formula in the trusted layer; G0 factorization is solution-side; "B = θ^{1/4}" nowhere in Lean | Yes | (o) | (o) | Yes — `Braw` is the `if`/`exp` formula; `Braw_eq_mul` is in `LemmaG1.lean`; `θ` occurs only in three comment lines, in no statement |
| (b) | Z, C_B are reals defined by an integral; no digit asserted | Yes | (o) | (o) | Yes — no decimal for Z or C_B appears outside docstrings; what is proved is `Z_pos`, `Z_le_one`, `integral_norm_Bc` (∫B = 1) |
| (c) | the transform is the paper's h_k, re-declared as `ft`; nothing claimed for Mathlib's `𝓕` | Yes | (o) | (o) | Yes — `ft` = `Zeta23.paperFT` character for character (§6(d)); `𝓕`/`fourierIntegral` appear in no statement |
| (d) | the prefactor (1 + (c_B/2)√\|η\|) is kept; (G2) is a separate statement | Yes | (o) | (o) | Yes — three separate theorems, (G2) with 4·e^{−3/4}·C_B and (7/8)c_B written out |
| (e) | the challenge states an inequality with the number 2/√(72e); its provenance is not a theorem | Yes | (o) | (o) | Yes — `cB := 2 / Real.sqrt (72 * Real.exp 1)`; "4·(18/e)" appears only in headers |
| (f) | strip weight \|Im z\|/2 for the support [−1/2, 1/2]; the clause-5 use at L(x−t) − iLy is not stated | Yes | (o) | (o) | Yes — `Real.exp (\|z.im\| / 2)`; there is **no** fourth (scaling) theorem, as (f) says it may be either a remark or a theorem — the builder chose the remark and said so |
| (g) | `iteratedDeriv` versus classical derivatives: identical for C^∞ functions — no divergence, but say so | Not a divergence (correctly labeled as such) | (o) | (o) | Yes — `B_contDiff`, `Braw_contDiff`; `norm_iteratedDeriv_Bc` transports the norm through `Complex.ofRealLI` |
| (n1) | trusted `Braw` by the exp formula; factorization solution-side; θ^{1/4} nowhere | Yes | (n) | (n) | Yes |
| (n2) | k^{2k} is `(k : ℝ) ^ (2 * k)`, the ℕ exponent; 0⁰ = 1 in both | Yes (a convention note) | (n) | (n) | Yes — and identical for natural k |
| (n3) | the challenge keeps k ≥ 1; the library theorem holds for every k | Yes (the library is stronger) | (n) | (n) | Yes — `abs_iteratedDeriv_Braw_le (k : ℕ)` with no hypothesis |
| (n4) | 72/e as `72 / Real.exp 1`; its provenance is in headers, not content | Yes | (n) | (n) | Yes |
| (n5) | `iteratedDeriv` versus the classical derivative — no divergence | Not a divergence (correctly labeled) | (n) | (n) | Yes — `Braw_contDiff` |

Two further points the ledger records as **not** divergences, which I confirm: the real form is derived from the
complex form at z = (η : ℂ); and the monotonicity of G in η, which the note proves, is **not** stated in Lean (grep for
`Antitone`/`Monotone`: none) — it is not needed, because the complex form carries G(|Re z|) directly.

`review.status` remains `self-assessed` and both `review.notes` paragraphs say plainly "No human has read
comparator/Challenge/Separation.lean against the note; the independent clean-clone check (Opus 5,
results/c2-m4/CHECK-O.md) is the next job." That was honest when written and is the correct standing description: this
report is a machine check by a second model, not human review of the trusted text.

## §9 Comparator with nanoda, three runs from the clean clone — **CLEAN**

My own runner `~/rh-lean-check-s23/verify/run-clone.sh` — the builder's `verify/run.sh` with the working-tree path
replaced by my clone's — same binaries (comparator v4.33.0, lean4export v4.33.0-rc2, nanoda 0.4.17, the
`fake-landrun.sh` shim: **NOT sandboxed**, for the Linux-only reason `COMPARATOR-RUN.md` §2 gives). The clone had
**no** comparator-layer artifacts before the CONTROL run (it had never built them); between runs I removed every
`.lake/build` entry under `Challenge*`, `ChallengeDeps*`, `Solution*`, `PrintAxioms*` (52 entries after CONTROL, 30
after the rung; log `~/rh-lean-check-s23/verify/prerun-cleanup.log`) so comparator rebuilt each layer itself, as
`COMPARATOR-RUN.md` §0 requires.

**Run 1 — CONTROL, `comparator/config.json` (the parent's fifteen theorems) — PASS.** 12:17:54–12:20:21 IST.

```
Build completed successfully (8699 jobs).      ← Challenge
Build completed successfully (8877 jobs).      ← Solution
Running nanoda kernel on solution
Nanoda kernel accepts the solution
Running Lean default kernel on solution.
Lean default kernel accepts the solution
Your solution is okay!
      146.83 real       138.54 user        14.33 sys      6.40 GB max RSS
--- comparator exit code: 0 ---
```

Job counts 8699 / 8877 are the D1 record's and the builder's, to the job. **The tool chain is alive in my clone**, so
anything the topic runs showed would be attributable to the topic.

**Run 2 — the rung, `comparator/config-separation-g1.json` — PASS.** 12:20:51–12:22:00 IST.

```
✔ [8697/8698] Built ChallengeDeps.Separation (2.9s)
⚠ [8698/8698] Built Challenge.SeparationG1 (2.9s)
warning: comparator/Challenge/SeparationG1.lean:37:8: declaration uses `sorry`
Build completed successfully (8698 jobs).
Exporting #[…, separation_braw_iteratedDeriv_le, propext, Quot.sound, Classical.choice, …] from Challenge.SeparationG1
✔ [8701/8701] Built Solution.SeparationG1 (2.0s)
Build completed successfully (8701 jobs).
Exporting #[…, separation_braw_iteratedDeriv_le, propext, Quot.sound, Classical.choice, …] from Solution.SeparationG1
Running nanoda kernel on solution
Nanoda kernel accepts the solution
Running Lean default kernel on solution.
Lean default kernel accepts the solution
Your solution is okay!
       68.50 real        61.21 user        13.56 sys      5.92 GB max RSS
--- comparator exit code: 0 ---
```

**Run 3 — the topic, `comparator/config-separation.json` — PASS.** 12:22:08–12:23:23 IST.

```
✔ [8697/8698] Built ChallengeDeps.Separation (2.9s)
⚠ [8698/8698] Built Challenge.Separation (2.9s)
warning: comparator/Challenge/Separation.lean:40:8: declaration uses `sorry`
warning: comparator/Challenge/Separation.lean:48:8: declaration uses `sorry`
warning: comparator/Challenge/Separation.lean:56:8: declaration uses `sorry`
Build completed successfully (8698 jobs).
✔ [8703/8703] Built Solution.Separation (2.0s)
Build completed successfully (8703 jobs).
Running nanoda kernel on solution
Nanoda kernel accepts the solution
Running Lean default kernel on solution.
Lean default kernel accepts the solution
Your solution is okay!
       75.11 real        67.80 user        13.63 sys      5.93 GB max RSS
--- comparator exit code: 0 ---
```

Job counts 8698 / 8701 / 8703 match the builder's to the job. Exactly the deliberate `sorry` warnings, no others.

**Import discipline, read by me, not inferred.** `comparator/Solution/SeparationG1.lean` imports
`ChallengeDeps.Separation` and `Zeta23.Separation.LemmaG1`; `comparator/Solution/Separation.lean` imports
`ChallengeDeps.Separation` and `Zeta23.Separation.LemmaG`. **Neither imports any `Challenge.*` module**, and neither
library module imports anything but `Zeta23.Taper.Gevrey`, `Zeta23.Separation.LemmaG1` and `Zeta23.Poisson.PaperFT`.
`ChallengeDeps/Separation.lean` imports `Mathlib` alone. So the challenge side is trusted and independent of the proof
side, as the pattern requires.

## §10 Frozen statements, yaml, lint, novelty — **CLEAN**

**(a) The six frozen D1/R1 statements.** My own probe in my clone, importing `Zeta23.W1.Soundness`, `Instances`, `FDH`,
`Ledger` **and** `Zeta23.Separation.LemmaG` (so the new modules are in the environment): `#check` + `#print axioms` of
`cert_of_checkW1`, `cert_of_checkW1_ap`, `cert_of_checkW1_fDH`, `cert_of_checkW1_of_diffOn`, `mpDH_zero`,
`arbDH_zero`. Diffed line by line against the AFTER section of `results/d1-m2a/dr8/sigma-strong-no-regression.log`:
**all 34 lines character-for-character identical** (the record's four extra lines are its own timing, verdict and probe
imports). Also identical to the builder's `verify/frozen-statements.log` body. All six on exactly
`[propext, Classical.choice, Quot.sound]`. **No regression.**

**(b) `formalization.yaml` schema validation.** `results/d1-m2a/dr8/validate_yaml_sigma_strong.py` run by me (its
apostrophe-safe `declared()` regex is the corrected one, so primed names such as `norm_paperFT_Bc_ofReal_le'` and
`cert_of_checkW1_of_diffOn'` are matched):

```
on-disk formalization.schema.dispatcher.json / v0.3 / v0.4 : upstream IDENTICAL to the on-disk copy (all three)
VALIDATION errors: 0
main_results: 20   alignment.statements: 21   fidelity.divergences: 11488 chars
Lean names referenced in status.main_results + alignment.statements: 49 — every one declared in the mirror
RESULT: PASS — errors: 0, undeclared names: 0
```

The six new `Zeta23.Separation.*` names (`Braw_eq_mul`, `abs_iteratedDeriv_Braw_le`, `norm_paperFT_Bc_le`,
`norm_paperFT_Bc_ofReal_le`, `norm_paperFT_Bc_ofReal_le'`, `paperFT_iteratedDeriv`) all resolve to the two new library
files. The clone's `formalization.yaml` is `cmp`-identical to the mirror's, so this validates the shipped file.

**(c) 10(g) lint.** Over the nine new Lean files: **no** "clearly / obviously / easy to see / easily seen /
well known"; **no** British spelling (`-ise`, `-isation`, `-ised`, `colour`, `behaviour`, `centre`, `defence`,
`licence`, `analyse`, `modelling`, `towards`, `maths`, `grey`, …); no trailing whitespace. Over `BUILD-NOTES.md` and
`SHARED.md`: the only hits are the sentence in BUILD-NOTES §4 that *records* the lint. Lines longer than 120
characters occur (49, nearly all in file headers), which matches the established house style of these comparator files
(`comparator/*/DBN.lean` has 50 such lines); not a defect.

**(d) Standing order 7 — novelty.** Nothing in the nine new files, in `BUILD-NOTES.md` or in the two ledger entries
claims the mathematics as novel. The mathematics is classical Gevrey/Fourier decay, and the note's own §2 10(n)
paragraph names the nearest published object (Rodino, Ch. 1; Hörmander §1.4). The only claims made are (i)
"Comparator-checked", (ii) "no displayed hypothesis", (iii) "the first statements of **this program** that carry no
'modulo H' label" — a claim about this program's own ledger, which I verified is true (every D1/R1 main_results entry
carries a "modulo H…" label; these two do not), and (iv) the provenance claim that 2/√(72e) is what Zeta23's
`gevrey_expNegInvGlue` constant gives for this bump, which is stated as provenance and not as a theorem. **No
overclaim found.**

## §11 MINOR observations (not FIX-FIRST; nothing blocked)

1. **`BUILD-NOTES.md` §4, "(50 names)".** The yaml validation log it cites says **49** (`Lean names referenced in
   status.main_results + alignment.statements: 49`), and my own run reproduces 49. Exact fix, one line: in
   `results/c2-m4/BUILD-NOTES.md` §4 change "declared in the mirror (50 names)" to "declared in the mirror (49 names)".
2. **`BUILD-NOTES.md` §3, "three deliberate `sorry` warnings (lines 44, 53, 60 of the challenge)".** 44/53/60 are where
   the `sorry` tokens sit; the warnings Lean emits name the declaration positions 40, 48, 56 (`:40:8`, `:48:8`,
   `:56:8`), as both the builder's own log and mine show. Exact fix, one line: change "(lines 44, 53, 60 of the
   challenge)" to "(at the declarations on lines 40, 48, 56)".

Neither changes a statement, a proof, a constant, a run or a verdict; both are prose in the build record.

## §12 Hashes — **CLEAN**

Every line of `results/c2-m4/hashes.txt` recomputed with SHA-256 from the repository, by me:

```
lines 35, mismatches 0, missing 0
```

and the file the table does not cover:

```
BUILD-NOTES.md   f667f2fa248fc090cf7690b4d9ba12908ac30695e30e47ffe22732e7ebc24962
                 (= the value recorded in SHARED.md's final block)
```

## §13 What I checked, and what I did not (standing order 5)

**Checked, by running it in my own clean clone:** the clone's provenance and toolchain pins; the overlay delta against
upstream v1.0; the cold `lake build Zeta23` (9146 jobs, 0 errors, warnings attributed); the two Solution builds;
`#print axioms` for the four Challenge theorems and for all 51 new library declarations; the nine trust greps with
comments stripped and again raw; challenge/solution statement identity for all four theorems; the elaborated statements
by `#check`; the byte identity of the six trusted definitions against the library's and of `ft` against
`Zeta23.paperFT`; the import graph of every new module; all three Comparator runs with nanoda, each after removing the
comparator-layer artifacts; the six frozen statements against the σ-strong record; the yaml schema validation and the
name-declaration sweep; the 10(g) lint; all 36 SHA-256 values; `git diff` over the frozen areas; mirror = working tree.

**Re-derived on paper, from the Lean text:** Lemma G0, Lemma G1 with its step (iii), the κ bookkeeping and both
branches of Lemma G, the strip weight, and (G2) — each against separation-note §2 and its constants. I read
`check-O.md` §4 afterwards and it agrees with my derivation.

**Not checked, and why.**
* **The correctness of Mathlib and of upstream Zeta23.** `Taper.gevrey_expNegInvGlue`, `Taper.abs_iteratedDeriv_g_le`,
  `Zeta23.paperFT_deriv` and `norm_paperFT_le` are taken as given; they are upstream, kernel-checked, and outside this
  unit's scope. I did read the statements of `norm_paperFT_le` and `paperFT_deriv` to confirm the Lean route uses them
  as the note's proof does.
* **The sandbox.** The comparator runs use the `fake-landrun.sh` shim (five `WARNING: THIS IS NOT REAL LANDRUN!` lines
  per run), because Landlock is Linux-only. A referee who wants the sandbox re-runs
  `lake env comparator comparator/config-separation.json` on a Linux host with landrun. Same limitation as the D1
  record, and it is declared there and here.
* **The numerical claims of the note** (Z ≈ 0.2219969, C_B ≈ 33.28, the ≈ 0.85 per √η empirical decay rate). None of
  them is asserted in Lean — that is divergence (b) — so none is in scope for this check, and none is a theorem.
* **Human review of the trusted text.** No human has read `Challenge/Separation.lean` against the note. This report is
  a second machine's independent check; `review.status: self-assessed` is the honest label and it stays.
* **Anything about ζ or RH.** Nothing here bears on either, and neither the Lean files nor the ledger claims otherwise.

## §14 Traceability

| Claim | Where it was produced |
|---|---|
| Clone HEAD, toolchain, Mathlib rev | `~/rh-lean-check-s23/clone` (`git rev-parse HEAD`, `lean-toolchain`, `lakefile.toml`) |
| Overlay delta 152 NEW / 2 CHANGED; `Zeta23.lean` = +19 imports | my `cmp` sweep; `diff <(git show v1.0:Zeta23.lean) lean/Zeta23.lean` |
| 9146 jobs, 0 errors, 191/247 warning lines | `~/rh-lean-check-s23/build-zeta23.log` |
| 8704 jobs, Solution modules | `~/rh-lean-check-s23/build-solutions.log` |
| the four `#print axioms` lines | `~/rh-lean-check-s23/verify/printaxioms-g1.log`, `printaxioms-sep.log` |
| 51-declaration axiom sweep | `~/rh-lean-check-s23/verify/probe_axioms.lean`, `probe_axioms.out` |
| trust greps | `~/rh-lean-check-s23/verify/trust-greps.log` (script: `results/c2-m4/verify/trust_greps_m4.py`) |
| statement identity ×4 | `results/c2-m4/verify/statement_identity_m4.py`, run in the clone |
| elaborated statements | `~/rh-lean-check-s23/verify/check_stmts.lean`, `check_stmts.out` |
| CONTROL / rung / topic Comparator runs | `~/rh-lean-check-s23/verify/control-run.log`, `comparator-run-g1.log`, `comparator-run-separation.log`; runner `verify/run-clone.sh`; cleanup `verify/prerun-cleanup.log` |
| frozen six | `~/rh-lean-check-s23/verify/frozen_probe.lean`, `frozen.out`, diffed against `results/d1-m2a/dr8/sigma-strong-no-regression.log` |
| yaml validation | `results/d1-m2a/dr8/validate_yaml_sigma_strong.py`, run by me against `rh-program/lean/formalization.yaml` |
| hashes | recomputed from `results/c2-m4/hashes.txt` |
| the note's Lemma G, G0–G2, constants | `results/c2-m2/separation-note.md` §2, §12.6, §12.12 |
| the contract's four statements and (a)–(g) | `results/c2-m2/followups/PRICING.md` §1(b) candidate (i) |
| ledger (n), (o) | `lean/formalization.yaml` lines 462–493; `results/d1-m2a/packaging/FIDELITY.md` sections (n), (o) |
