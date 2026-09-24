# C2 — M4 residue, Unit B (`Separation5`): clause 5 (the rung, 1(a) modulo H-R₀, 1(b) with H-R₀ discharged by a 16-cell Z enclosure) — independent check (Session 25 item 2, Job 2, Opus 5, clean clone)

Task: `results/c2-m4/BRIEF-B.md` "Job 2 — INDEPENDENT CHECKER"; contract `results/c2-m4/PRICING-RESIDUE.md` §1 Piece 1
(items 1–11), Piece 8, §2 row B; the builder's checklist `results/c2-m4/BUILD-NOTES-B.md` §5. Object checked: the builder's
work (Job 1, Fable 5.1, 2026-09-24, 22:09–23:05 IST) as recorded in `BUILD-NOTES-B.md`, the Unit B blocks of `SHARED.md`
(stages 0–7) and `hashes-B.txt`. Pattern: `results/c2-m4/CHECK-O-A.md` (layout repeated, suffix `-B`).

Nothing in the repository, the mirror or the builder's working tree was modified by this job, and nothing was committed
by it (the watchdogs commit). Everything in §§1–12 was produced in a FRESH clone made for this check,
`~/rh-lean-check-s25/clone` (cloned from `https://github.com/anthropics/zeta-23-lean.git` at 23:07 IST, checked out at tag
v1.0), overlaid with the current `rh-program/lean/` mirror; never in `~/rh-lean-work/zeta-23-lean-main`. Scripts and logs:
`results/c2-m4/verify-B-O/`. Check window 23:07–23:26 IST (machine clock).

---

## §0 Headline verdict

**OVERALL: CLEAN — no FIX-FIRST; 4 MINOR (§13).** From a fresh clone of upstream v1.0 with the mirror overlaid: cold build
**9153 jobs, 0 errors**; `#print axioms` standard three on the 5 roots and on all 99 library declarations (74 theorems,
25 definitions; `qcell` depends on no axiom at all); trust greps = the 5 deliberate challenge `sorry`s; statement identity
×5 by two extractions; **Comparator with nanoda ×4 — CONTROL, `SeparationClause5Sum`, `Separation5`, `Separation5c` —
`Your solution is okay!`, exit 0 ×4**; the sixteen frozen statements (Unit A's twelve plus the four theorems of Unit A's
two root pairs) byte-identical; yaml PASS; lint clean; hashes-B 52/52. The points weighed hardest (§9): (i) `P2`, `P3`,
`F13` equal `r0_73_check.py` 22–33 term for term — relative difference 0.0 at L = 50, 100, 10³, 10⁴ on my own
transcription, the only differences b₁sym for 8.69808 and 105/100 for 1.05, both declared in (r2) — CLEAN; (ii) the
antiderivative identity, the chain rule through u = s²/L and the limit at +∞ — CLEAN (paper re-derivation, symbolic
check n ≤ 12, quadrature); (iii) `HR0` is A3's one-point check at R₀ = 73 with exponent 13/8, both conjuncts; the decrease
on [50, ∞) is proved from the second conjunct; the assembly's conclusion is byte-identical to `separation_clause6_assembly_b`;
the absorption is spent once — CLEAN; (iv) Z_lo = 0.2105013520 ≥ 421/2000, Z_hi = 0.2336502280 ≤ 233651/10⁶, F₁₃(50) at the
endpoints = −0.34741, certificate margin 0.34714 nats, all recomputed on my own exact-rational code; the 16-cell bridging is
sound; `cert_numeric` is the inequality `F13_50_neg` consumes — CLEAN; (v) `strip` consumed only at `norm_wsum_le_strip`
(Clause5.lean 118), passed as `Z.strip` in the three solutions — CLEAN. The full table is at the end.

---

## §1 Clone provenance and the overlay — **CLEAN**

```
git clone https://github.com/anthropics/zeta-23-lean.git clone ; git checkout v1.0      (23:07 IST)
HEAD = v1.0^{commit} = 3635e74826a4c1fcece7d1cd2b6fa75e43a00510 ; git status --porcelain -> (empty)
lean-toolchain leanprover/lean4:v4.33.0-rc2 ; lakefile.toml Mathlib rev 51e6992efd06126df61a496bebf8f49482a4e129
```

The commit, toolchain and Mathlib pair of every record in this program (CHECK-O-A §1).

**Overlay measured before copying** (`verify-B-O/overlay-delta-BO.log`): a file-by-file `cmp` of all 193 mirror files against
the pristine v1.0 tree — **191 NEW, 2 CHANGED** (`README.md`, `Zeta23.lean`), 0 identical. The `Zeta23.lean` difference is
exactly **26 added `import` lines and nothing else** (Unit A's 23 plus `Clause5`, `ZEnclosure`, `Clause5Cert`), so
BUILD-NOTES-B's "the ONE edit to an existing Lean file is the three additive imports in `Zeta23.lean`" holds against
upstream. Overlay by the README recipe (`Zeta23/`, `comparator/`, `Zeta23.lean`, `formalization.yaml`, `README.md`);
post-overlay `git status --porcelain` lists 56 entries, all the program's own files.

**Cold.** The clone had no `.lake/build`. The Mathlib package directory was APFS-cloned (`cp -Rc`) from the Unit A
checker's clone; `lake exe cache get` reported `No files to download; Already decompressed 8681 file(s)`
(`verify-B-O/cache-get-BO.log`). The whole `Zeta23` library, the program's additions included, compiled from source.
Load discipline: one `lake` process at a time; `caffeinate` running; nothing else heavy in parallel.

## §2 Cold build of the overlaid clone — **CLEAN**

`lake build Zeta23` (23:08:21–23:15:34 IST; `verify-B-O/build-zeta23-BO.log`):

```
✔ [8816/9153] Built Zeta23.Separation.ZEnclosure (8.2s)
✔ [9012/9153] Built Zeta23.Separation.Clause5 (23s)
✔ [9023/9153] Built Zeta23.Separation.Clause5Cert (5.7s)
Build completed successfully (9153 jobs).
      432.46 real      2730.96 user       704.99 sys
exit=0
```

* **9153 jobs** — the builder's figure exactly, Unit A's 9150 plus the three new modules.
* **Errors: 0.** The two lines matching `error` name the module `Zeta23.XiPrime.ExplicitFormula.EntryError`.
* **Warnings: 191 lines `warning:`** — the count of CHECK-O-A and the earlier checks. None names `Clause5`, `ZEnclosure`,
  `Clause5Cert` or any `comparator/` path; the only program-module warnings are the two pre-existing ones in
  `Zeta23/PairCeiling/Stability.lean` (49:4, 245:4).
* **Stop line (d), timed in isolation** (`verify-B-O/timing-cert-BO.log`, `lake env lean` re-elaborating each file from
  source against the built imports): `ZEnclosure.lean` **3.38 s**, `Clause5Cert.lean` **2.99 s** wall — the builder's 3.8 s /
  3.4 s; ten minutes is the stop line.

## §3 The three Solution modules — **CLEAN**

`lake build Solution.SeparationClause5Sum Solution.Separation5 Solution.Separation5c` (`verify-B-O/build-solutions-BO.log`):
`Built ChallengeDeps.Separation5 (3.7s)`, `Built Solution.SeparationClause5Sum (3.8s)`, `Solution.Separation5c (3.8s)`,
`Solution.Separation5 (3.3s)`, `Build completed successfully (8716 jobs)`, exit 0 (one joint build; the builder's 8711 /
8712 / 8713 are the three separate builds, reproduced inside the Comparator runs of §11). The one warning is the upstream
`Zeta23/Taper/Gevrey.lean:342:80` unused-variable lint, a tracked v1.0 file.

## §4 `#print axioms` — **CLEAN**

**(a) The five roots through the builder's PrintAxioms files** (`verify-B-O/print-axioms-roots-BO.log`):

```
'separation_clause5_summable' depends on axioms: [propext, Classical.choice, Quot.sound]
'separation_clause5_out_window' depends on axioms: [propext, Classical.choice, Quot.sound]
'separation_clause6_assembly_c' depends on axioms: [propext, Classical.choice, Quot.sound]
'separation_clause5_out_window_c' depends on axioms: [propext, Classical.choice, Quot.sound]
'separation_clause6_assembly_d' depends on axioms: [propext, Classical.choice, Quot.sound]
```

**(b) Every library declaration, from my own list.** `verify-B-O/axioms_BO_probe.lean.txt` is generated by a grep of every
line beginning `theorem ` or `def ` in `Clause5.lean` (49 + 10), `ZEnclosure.lean` (14 + 3), `Clause5Cert.lean` (11 + 12),
plus the five roots — 104 `#print axioms` lines. No file has a `lemma`, `private`, `protected`, indented declaration,
`attribute`, `instance`, `macro`, `notation` or `set_option` (extra grep, §5). Result (`verify-B-O/print-axioms-library-BO.log`):
**103 lines `[propext, Classical.choice, Quot.sound]`**, and `'Zeta23.Separation.qcell' does not depend on any axioms` (a
`Nat`-valued `if`-chain). The builder's 74 theorems are among the 103; no `sorryAx`, no `Lean.ofReduceBool`.

## §5 Trust greps — **CLEAN**

`verify-B-O/trust-greps-BO.log`, over the thirteen Unit B Lean files (three library, `ChallengeDeps/Separation5.lean`, three
challenges, three solutions, three PrintAxioms):

* the builder's `verify-B/trust_greps_B.py` (read first: nested `/- -/` and `--` stripped, nine words): **exactly five hits,
  the five deliberate challenge `sorry`s** — `SeparationClause5Sum.lean:44`, `Separation5.lean:51, 69`, `Separation5c.lean:47, 64`;
* my raw word-bounded grep, comments NOT stripped (`axiom`, `native_decide`, `unsafe`, `implemented_by`, `extern`, `opaque`,
  `sorry`, `admit`, `ofReduceBool`): the same five code lines plus docstring mentions only (the challenge headers' "the `sorry`
  below is deliberate", the PrintAxioms headers' "no sorryAx, no Lean.ofReduceBool (= no native_decide)"). The three library
  files have **zero** hits even in comments. No `decide` of any kind, no `csimp`. `cert_numeric` and `Z_enclosure` close by
  `norm_num` over ℚ, kernel-checked.

## §6 Statement identity, challenge against solution — **CLEAN**

Two independent extractions (`verify-B-O/statement-identity-BO.log`):

* the builder's `statement_identity_B.py`: RESULT PASS ×3 topics;
* my `stmt_identity_BO.py` (scan from `theorem <name>` to the first `:=` outside every bracket pair and comment; UTF-8 bytes):

```
separation_clause5_summable       236 B  sha256[:16] 119b55687fa7bc09  IDENTICAL
separation_clause5_out_window     281 B  sha256[:16] 1c2f7e346ad8c724  IDENTICAL
separation_clause6_assembly_c     927 B  sha256[:16] fb7c2b19ceeb998e  IDENTICAL
separation_clause5_out_window_c   256 B  sha256[:16] b03e22187628f44d  IDENTICAL
separation_clause6_assembly_d     904 B  sha256[:16] bb1004b1e5a917be  IDENTICAL
```

The Comparator runs of §11 re-establish the identity at the level of kernel terms.

## §7 The trusted layer, read line by line — **CLEAN**

**`comparator/ChallengeDeps/Separation5.lean`** (73 lines) read in full. Code: `import Mathlib`, `import ChallengeDeps.Separation6b`,
`namespace Separation`, and six `def`s — `gammaPoly`, `Prelax`, `P2`, `P3`, `F13`, `HR0` — nothing else (no `attribute`,
`instance`, re-declaration). `SepConfig`, `Hout`, `outWindow`, `Wsummand`, `ftest`, `cB`, `CB`, `Z`, `b1sym` are the frozen
declarations, by import. `cB := 2 / √(72e)` and `CB := e² / Z` (`ChallengeDeps/Separation.lean` 52, 55) are the script's
`cB`, `CB` (its line 19 asserts exactly these closed forms).

**Character for character with the library.** The six `def` blocks extracted from `ChallengeDeps/Separation5.lean` and
from `Zeta23/Separation/Clause5.lean` (398–833): `diff` empty (13 lines each). The solution `Separation5` passes the
trusted `hR0 : Separation.HR0` to the library's `clause5_out_window`, which takes `Zeta23.Separation.HR0`; the kernel
accepted it in §11, which requires the two to unfold to the same term.

**Import discipline (read in the clone).**

```
comparator/ChallengeDeps/Separation5.lean      import Mathlib; import ChallengeDeps.Separation6b
comparator/Challenge/SeparationClause5Sum.lean import ChallengeDeps.Separation6b
comparator/Challenge/Separation5.lean          import ChallengeDeps.Separation5
comparator/Challenge/Separation5c.lean         import ChallengeDeps.Separation6b
comparator/Solution/SeparationClause5Sum.lean  import ChallengeDeps.Separation6b; import Zeta23.Separation.Clause5
comparator/Solution/Separation5.lean           import ChallengeDeps.Separation5;  import Zeta23.Separation.Clause5
comparator/Solution/Separation5c.lean          import ChallengeDeps.Separation6b; import Zeta23.Separation.Clause5Cert
```

**`Separation5c`'s challenge imports only the frozen `ChallengeDeps.Separation6b` — confirmed twice:** by the import line,
and by the Comparator run of §11(d), whose challenge build compiles `ChallengeDeps.{Separation, SepConfig, Separation6,
Separation6b}` and NOT `ChallengeDeps.Separation5` (8701 jobs). No new trusted definition enters the 1(b) topic.

**The crude majorant M_L appears in no statement.** `crudeM`, `crude_bound`, `crude_shell_bound`, `crude_series_le` occur
only in `Clause5.lean` §3; a grep of the whole `comparator/` tree for `crudeM|crude_` returns nothing.

**The new statements against the frozen ones** (`verify-B-O/statement-diffs-BO.log`, `diff` of the challenge blocks):
`separation_clause6_assembly_c` differs from `separation_clause6_assembly_b` only by its name and by the line
`(houtZ : Z.Hout t L (73 * L)) (houtZ' : Z'.Hout t L (73 * L))` → `(hR0 : Separation.HR0)`; `_d` only by its name and the
deletion of that line; `_c` → `_d` only by `hR0` deleted; `separation_clause5_out_window` → `_c` only by name and `hR0`
deleted. The conclusion block of `_b`, `_c`, `_d` has the same SHA-256 (`20325f77…24eb`). The rung's statement is the first
conjunct of the frozen `Hout` (`ChallengeDeps/Separation6.lean` 76–78) at R = 73L, verbatim, under t ≥ 3, L > 0.

## §8 The fidelity ledger, row by row — **CLEAN (6/6; no unlisted weakening)**

Against PRICING-RESIDUE Piece 1, the note §6 and A3, check-O §12.8; recorded in `formalization.yaml` fidelity (r) and
`FIDELITY.md` (r) (lines 66–70, read).

| row | claim | checked against | verdict |
|---|---|---|---|
| (r1) | H-out → H-R₀ (`Separation5`) → nothing (`Separation5c`) | §7's statement diffs; A3 | CLEAN — the only hypothesis change in each pair is that one line |
| (r2) | `gammaPoly`, `Prelax`, `P2`, `P3`, `F13` = `r0_73_check.py` 22–33, b₁ = b₁sym, 1.05 = 105/100 | §9 (i) | CLEAN — the two substitutions are the only differences and both are named in (r2) |
| (r3) | `strip` consumed first in `norm_wsum_le_strip` | §9 (v) | CLEAN |
| (r4) | shell index ⌊|Im ρ − t|⌋₊ ≥ ⌊73L⌋₊ ≥ 73L − 1; every shell by the two windows at t ± (k + ½) | `Clause5.lean` 1029 (`hK₀ge`), `shell_count_le` 147 | CLEAN — k ≤ |Im ρ − t| < k + 1 puts Im ρ within 1 of t + k + ½ or of t − k − ½; each window holds ≤ C₁log(3 + |t ± (k + ½)|) ≤ C₁log(7/2 + t + k) |
| (r5) | absorption spent once, exponent 13/8, R₀ = 73 | §9 (iii) | CLEAN |
| (r6) | 421/2000 ≤ Z ≤ 233651/10⁶ PROVED, consumed by `F13_50_neg` only | §9 (iv); grep of consumers | CLEAN — `Z_enclosure` is used only by `CB_le_CBHi` and `b1Lo_le_b1sym`, both only on `F13_50_neg`'s path |

## §9 The points weighed hardest — **CLEAN ×5**

**(i) `P2`, `P3`, `F13` against `r0_73_check.py` lines 22–33.** Read side by side: `gamma_poly(n,a,s) = Σ_{j≤n} n!/j!·s^j/a^{n+1−j}`
↔ `∑ j ∈ range (n+1), (n! : ℝ)/(j! : ℝ) * s^j / a^(n+1−j)` (left-associated, the same parse); `P_relaxed(m, L, 73, 50)` with
`a = 2cB`, `sR = √73·L`, `u0 = 73L`, `beta = 1 + 3/(2(73·50 − 1))`, `phi0 = u0^m(1 + cB/2·sR)²`, `integ = (2/L^{m+1})(γ_{2m+1} +
cB·γ_{2m+2} + cB²/4·γ_{2m+3})(a, sR)`, return `beta^m·CB²·(phi0 + integ)` ↔ `Prelax` term for term; `Ftilde(L, 73, 50, 13/8) =
(13/8 − 2cB√73)L + 2cB/√73 + log((1.05·P₂ + P₃)/b1)` ↔ `F13` with `105 / 100` for `mpf('1.05')` and `b1sym` for `b1`. **The
two declared differences are the only ones.**

On MY OWN transcription — `verify-B-O/numerics_BO.py`, written from the Lean text of `ChallengeDeps/Separation5.lean` without
reading the builder's `p23_diff.py` — against the script's lines 22–33 exec'd verbatim from the file, at 50 digits, both with
cB, CB from Z computed by quadrature and with the record's json constants (`verify-B-O/numerics-BO.log`):

```
L=   50  P2 945084322266075.4  rel 0.0 | P3 rel 0.0 | F13(b1 rec) -0.322723205707064 = Ftilde, rel 0.0 | F13(b1sym) -0.5560988195
L=  100  P2 1.423155451809302e+16 rel 0.0 | P3 rel 0.0 | F13(b1 rec) -37.8221871827996 = Ftilde | F13(b1sym) -38.0555628
L= 1000  P2 1.347348423408449e+20 rel 0.0 | P3 rel 0.0 | F13(b1 rec) -762.492965035373 = Ftilde | F13(b1sym) -762.7263406
L=10000  P2 1.33998150879799e+24  rel 0.0 | P3 rel 0.0 | F13(b1 rec) -8112.19979935196 = Ftilde | F13(b1sym) -8112.433175
max relative difference: 0.0 -> AGREE (both constant sets)
```

F₁₃(50) at the record's b₁ = −0.32272 is A3's −0.3227; 5/(2c_B√73 − 13/8) = 6.113122 is A3's 6.113; the b₁sym shift is
log(b₁sym/8.69808) = 0.23338 nats in the favorable direction. The builder's `p23_diff.py`, re-run by me from
`results/c2-m2/verify/`, reproduces its log byte for byte after the header (`verify-B-O/p23-diff-rerun-BO.log`). Stop line (b)
did not fire.

**(ii) The tail integral.** Paper re-derivation from the Lean text:
* recursion (`gammaPoly_succ`): the j = n + 1 term of γ_{n+1} is s^{n+1}/a; for j ≤ n, (n + 1)!/j!·s^j/a^{n+2−j} =
  ((n + 1)/a)·n!/j!·s^j/a^{n+1−j}. So γ_{n+1} = s^{n+1}/a + ((n + 1)/a)γ_n.
* derivative (`hasDerivAt_exp_mul_gammaPoly`): d/ds[e^{−as}γ_n] = e^{−as}(γ_n′ − aγ_n), so the claim is aγ_n − γ_n′ = sⁿ.
  n = 0: γ₀ = 1/a. Step: aγ_{n+1} − γ_{n+1}′ = s^{n+1} + (n + 1)γ_n − (n + 1)sⁿ/a − ((n + 1)/a)γ_n′
  = s^{n+1} + ((n + 1)/a)(aγ_n − γ_n′ − sⁿ) = s^{n+1}. The Lean induction carries the `HasDerivAt` itself through the same
  recursion (`field_simp; ring` closes the step).
* limit (`tendsto_exp_mul_gammaPoly`): each monomial is a constant times s^j e^{−as} = a^{−j}(as)^j e^{−as} → 0
  (`Real.tendsto_pow_mul_exp_neg_atTop_nhds_zero` composed with s ↦ as, a > 0); a finite sum of such tends to 0.
* integral (`integral_pow_mul_exp_Ioi`, via `integral_Ioi_of_hasDerivAt_of_nonneg'` with F = −e^{−as}γ_n): 0 − F(s₀) =
  e^{−as₀}γ_n(a, s₀). The note's formula.
* Γ_m and the chain rule (`hasDerivAt_exp_mul_GammaM`, `hasDerivAt_Phi`): with E(s) := e^{−2c_Bs}Γ_m(s), E′(s) = −e^{−2c_Bs}(s^{2m+1}
  + c_Bs^{2m+2} + (c_B²/4)s^{2m+3}) = −s^{2m+1}(1 + (c_B/2)s)²e^{−2c_Bs}. With s = √(Lu), ds/du = L/(2s):
  Φ_m′(u) = −(2/L^{m+1})E′(s)·L/(2s) = s^{2m}(1 + (c_B/2)s)²e^{−2c_Bs}/L^m = u^m(1 + (c_B/2)√(Lu))²e^{−2c_B√(Lu)} = φ_m(u),
  since s^{2m} = L^m u^m. `tendsto_Phi` composes E → 0 with √(Lu) → ∞. Hence ∫_{u₀}^∞ φ_m = (2/L^{m+1})e^{−2c_Bs₀}Γ_m(s₀).
* Independent numerics (`verify-B-O/tail_integral_BO.py` → `tail-integral-BO.log`): the identity aγ_n − γ_n′ = sⁿ and the
  recursion hold symbolically (sympy) for n = 0…12; ∫_{s₀}^∞ sⁿe^{−as} against e^{−as₀}γ_n agrees to ≤ 1.2·10⁻²⁹ relative at
  n = 9, a = 2c_B, s₀ = √73·50 and s₀ = 427; ∫_{u₀}^∞ φ_m against the closed form agrees to 1.2·10⁻⁴¹ at (L, u₀) = (1, 5) and to
  ≤ 3.5·10⁻¹⁰ at (50, 3650), (100, 7300) for m = 2, 3 (quadrature-limited); Φ_m′ = φ_m by central difference to ≤ 6·10⁻²¹.
Stop line (c) did not fire: n = 9 is an instance of the general-n induction.

**(iii) `HR0`, the decrease, the assembly, the absorption.**
* `HR0 := F13 50 ≤ 0 ∧ 5 / (2 * cB * Real.sqrt 73 - 13 / 8) ≤ 50`. A3 (note line 547): "the one-point check is F₁₃(L₀) ≤ 0
  with 5/(2c_B√R₀ − 13/8) ≤ L₀", with F₁₃ carrying exponent 13/8 and R₀ = 73, L₀ = 50 (A3 line 549, "R₀ = 73.0,
  F₁₃(50) = −0.3227, decrease from L = 6.11 ≤ 50"). Both conjuncts are A3's, at A3's constants; `r0_73_check.py` line 36
  tests exactly these two (plus positivity of the slope, which `slope_pos` proves from c_B ≥ 0.1429 and √73 ≥ 8).
* The decrease (`F13_le_F13_50`): c := 2c_B√73 − 13/8 ≥ 1/10 is read from `hR0.2` (`div_le_iff₀` with `slope_pos`) — the
  digits are not used. With L = 50r, r ≥ 1: every monomial of P_m has degree ≤ m + 2 in L (the γ-terms: degree ≤ 2m + 3 in
  √73·L times L^{−(m+1)}), so `Prelax_mul_le` gives P_m(50r) ≤ r^{m+2}P_m(50), hence Q(L) ≤ r⁵Q(50) for Q = 1.05P₂ + P₃;
  F₁₃(L) − F₁₃(50) ≤ −c(L − 50) + 5 log r ≤ −c(L − 50) + 5(r − 1) = (L − 50)(1/10 − c) ≤ 0. Only [50, ∞) is proved and only
  [50, ∞) is consumed (L ≥ 50 in every statement); A3's "from 6.11" is not needed (MINOR M3).
* The assembly (`clause6_assembly_c`): the proof is `clause6_assembly_b` applied to `clause5_out_window` for Z and for Z′,
  with L ≥ 50 from 25/δ ≤ L, δ ≤ ½ and hL8 from hL2 (`hL8_of_hL2`: 4/δ ≥ 8, 2log(1/δ) ≥ 0, both remaining summands ≥ 0 at
  t ≥ 3, b₁sym ≥ 4, C₁ ≥ 1). Its conclusion is byte-identical to `_b`'s (§7).
* The absorption, spent once: `absorb_once` is called exactly once (`shell_series_le`, line 1026); the single hypothesis
  8(log log(3 + t) + log(2b₁C₁)) ≤ L gives log(3 + t)·2b₁C₁ ≤ e^{L/8}, hence 2C₁log(3 + t) ≤ e^{L/8}/b₁ and 2C₁ ≤ e^{L/8}/b₁
  (log(3 + t) ≥ log 6 ≥ 5/3 ≥ 1); log(7/2 + t) ≤ 1.05·log(3 + t) from log((7/2 + t)/(3 + t)) ≤ 1/12 ≤ 0.05·(5/3). Each shell
  term is then ≤ e^{L/2}·A·(1.05β²C_B²φ₂(k) + β³C_B²φ₃(k)), A = e^{L/8}/b₁, one factor A per term — A3's
  "S_Z ≤ (e^{5L/8}/b₁)(1.05Σ₂ + Σ₃)" (note line 547) — and the chain ends at e^{F₁₃(L) − L} ≤ e^{F₁₃(50) − L} ≤ e^{−L}. The
  exponent is 13/8, not the body's 7/4; the constant is 73, not 81.

**(iv) The certificate (1(b), Piece 8), recomputed on my own code** (`verify-B-O/numerics_BO.py`, exact `Fraction` arithmetic,
not the builder's `cert_numbers.py`; `numerics-BO.log`):
* Cells: x_i = 256/(256 − i²), q_i = ⌈x_i⌉ = 1, 2 (i = 1…11), 3, 3, 5, 9 — equal to Lean's `qcell` for every i (asserted).
  Per cell, lo_i := 1/T(x_i/q_i)^{q_i} ≤ e^{−x_i} ≤ hi_i := 1/Σ_{k<8}x_i^k/k!, checked against e^{−x_i} at 45 digits for all 16.
* **Z_lo := (Σ_{i=1}^{15} lo_i)/16 = 0.2105013520 ≥ 421/2000 (slack 1.35·10⁻⁶); Z_hi := (Σ_{i=0}^{15} hi_i)/16 = 0.2336502280 ≤
  233651/10⁶ (slack 7.7·10⁻⁷)**; true Z = 0.2219969081; the exact Riemann sums (no exp bounds) are 0.2105013598 and
  0.2334938249.
* Constant enclosures: e ∈ [eLo, eHi], c_B ∈ [cLo, cHi], √73 ∈ [rLo, rHi] all hold at 50 digits, and the exact rational side
  conditions the Lean proofs reduce to hold: 72·eHi ≤ (2/cLo)², (2/cHi)² ≤ 72·eLo, rLo² ≤ 73 ≤ rHi². CBHi = 35.1024 ≥ C_B =
  33.2845; b1Lo = 9.91598 ≤ b₁sym = 10.98442.
* **`cert_numeric`, exact:** LHS (1.05·PrelaxQ 2 + PrelaxQ 3)/b1Lo = 3.9385·10¹⁷ ≤ RHS eLo⁴⁰·Σ_{i<6}(ELo − 40)^i/i! = 5.5731·10¹⁷,
  **margin log(RHS/LHS) = 0.34714 nats**; ELo = 40.86217 ≥ 40. **F₁₃(50) at the endpoints = log(Q_hi/b₁_lo) − E_lo = −0.34741**
  (builder −0.3474, pricing −0.349), an upper bound on the true F₁₃(50) = −0.55610. Second conjunct: 2·cLo·rLo − 13/8 =
  0.81791, 5/0.81791 = 6.1131 ≤ 50. Cleared numerator sizes 294 and 577 digits (the builder's figures).
* **The bridging is sound** (read and re-derived): B_raw is antitone on [0, ½] (1/(1 − 4v²) increases on [0, ½), and
  B_raw(½) = 0 ≤ B_raw); g(x) := B_raw(x/32) is antitone on [0, 16]; `AntitoneOn.sum_le_integral` / `integral_le_sum` give
  Σ_{i<16} g(i + 1) ≤ ∫_0^{16} g ≤ Σ_{i<16} g(i); `integral_comp_div` gives ∫_0^{16} g = 32∫_0^{½}B_raw = 16Z (B_raw even,
  `Z_eq_two_mul`); g(i) = e^{−x_i} for i ≤ 15 (`Braw_cell`) and g(16) = 0 (`Braw_sixteen`). The upper cell bound is
  e^{x} ≥ Σ_{k<8}x^k/k! (`Real.sum_le_exp_of_nonneg`); the lower is e^{x} = (e^{x/q})^q ≤ T(x/q)^q with `Real.exp_bound'` at
  n = 8 on y = x/q ∈ [0, 1], which needs x_i ≤ q_i — hence q_i = ⌈x_i⌉ (`cellx_le_qcell`).
* **`cert_numeric` is the inequality `F13_50_neg` consumes:** `Clause5Cert.lean` 213–216, the middle link of
  Q/b₁sym ≤ Q_hi/b1Lo ≤ eLo⁴⁰·Σ ≤ e^{ELo}, then log ≤ ELo (`Real.log_le_iff_le_exp`) and the linear part ≤ −ELo (the
  c_B, √73 endpoint substitutions in `hlin`), so F₁₃(50) ≤ 0. `Prelax_50_le` substitutes c_B → cHi in the prefactors, c_B → cLo
  in a = 2c_B (γ_n is antitone in a: `gammaPoly_le`), √73 → rHi, C_B → CBHi — every monomial moves up, which is what an
  upper bound on P needs.

**(v) The `strip` field.** A grep of the whole clone for `.strip|hstrip`: in the Unit B files `hstrip` is consumed at exactly
two places, `Clause5.lean` 387 (`clause5_summable`) and 1153 (`clause5_out_window`), each as `norm_wsum_le_strip hL (hstrip ρ hρ.1)`
— the theorem at line 118, whose hypothesis `0 ≤ ρ.re ∧ ρ.re ≤ 1` becomes |½ − Re ρ| ≤ ½, the depth bound fed to
`norm_paperFT_ftest_le_strip` (e^{L|y|/2} ≤ e^{L/4}). Lines 1204–1205 only pass `hstrip`, `hstrip'` on to `clause5_out_window`.
The three solutions pass `Z.strip` (and `Z'.strip` for the assemblies) and nothing else new: `SeparationClause5Sum.lean` 34,
`Separation5.lean` 39, 57, `Separation5c.lean` 36, 54. No earlier program file uses the field (the other grep hits are
upstream v1.0 modules unrelated to `SepConfig`). This is (r3) as written.

## §10 The rung's shell device, read — **CLEAN**

`clause5_summable` (378) and `clause5_out_window` (1137) share `out_window_norm_le` (256): every finite sub-family of the
out-window subtype is fibered by k = ⌊|Im ρ − t|⌋₊ ≥ ⌊R⌋₊, shell k holds ≤ 2C₁log(7/2 + t + k) mass (`shell_count_le`),
and a bound c on every initial segment of the shell series gives Σ_F ≤ c, hence summability (`summable_of_sum_le`), the
tsum bound and the norm of the sum (`norm_tsum_le_tsum_norm`). The rung's per-shell weight is e^{L/2}M_L/(k + 1)⁵ with
Σ_k log(7/2 + t + k)/(k + 1)⁵ ≤ (9/2 + t)Σ(k + 1)⁻⁴ ≤ 2(9/2 + t); 1(a)'s is (k + 3/2)²e^{L/2}G(Lk)² (`shell_weight_le`:
u + ½ < ⌊u⌋₊ + 3/2 and G antitone). The kernel accepted both (§11).

## §11 The four Comparator runs from the clean clone, with nanoda — **CLEAN**

Runner `verify-B-O/run-clone-B.sh` — CHECK-O-A's `run-clone-A.sh` with the clone path changed (`diff`: the comment line and
the `cd`), including its pre-run cleanup of `.lake/build/lib/lean/{Challenge, ChallengeDeps, Solution, PrintAxioms}` before
each run, so comparator builds the comparator layer itself. Comparator v4.33.0, lean4export v4.33.0-rc2, nanoda 0.4.17
(the binaries under `~/rh-lean-work/tools/`, as CHECK-O-A used them), `fake-landrun.sh` shim — the shim's
`WARNING: THIS IS NOT REAL LANDRUN!` lines appear in every run, as in every record (not sandboxed; Landlock is Linux-only).
Sequential, one at a time, from the clone root.

| run | log | challenge build | solution build | acceptance | time | exit |
|---|---|---|---|---|---|---|
| (a) CONTROL `config.json` (15 theorems) | `control-run-BO.log` | 8699 jobs (15 `sorry` warnings) | 8877 jobs | Nanoda accepts / Lean kernel accepts / `Your solution is okay!` | 150.96 s | 0 |
| (b) `config-separation-clause5sum.json` | `comparator-run-clause5sum-BO.log` | 8701 (`SeparationClause5Sum.lean:40:8` sorry) | 8711 | the three lines | 88.71 s | 0 |
| (c) `config-separation5.json` (2 names) | `comparator-run-separation5-BO.log` | 8702 (`Built ChallengeDeps.Separation5`; 46:8, 56:8) | 8712 | the three lines | 95.41 s | 0 |
| (d) `config-separation5c.json` (2 names) | `comparator-run-separation5c-BO.log` | 8701 (no `ChallengeDeps.Separation5`; 43:8, 51:8) | 8713 | the three lines | 93.51 s | 0 |

The CONTROL run (23:17:57–23:20:28 IST) reproduces 8699 / 8877, the figure of every record: the toolchain is alive. The
exports name exactly the configured theorems (`separation_clause5_summable`; `separation_clause5_out_window`,
`separation_clause6_assembly_c`; `separation_clause5_out_window_c`, `separation_clause6_assembly_d`). Job counts and `sorry`
positions match the builder's record. **What the runs establish:** each statement in the solution modules coincides
constant for constant with its namesake in the challenge modules (the trusted `SepConfig`, `Hout`, `HR0`, `F13`, `b1sym`,
`HB3`, `Hedge`, `Rstar` included); the proofs use no axiom outside the permitted three; nanoda re-checked each solution
export and Lean's own kernel replayed it.

## §12 The frozen statements, yaml, lint, hashes — **CLEAN**

**The sixteen frozen statements.** After building `Solution.{Separation, SeparationG1, SeparationClause4, Separation6,
SeparationClause4b, Separation6b}` in the clone (8715 jobs), the builder's `verify-B/frozen_probe.lean.txt` run in my clone
(`verify-B-O/frozen-statements-BO.log`, 142 lines) is **byte-identical** to the body of `verify-B/frozen-statements.log`; its
first 82 lines are byte-identical to the body of `verify-A/frozen-statements.log` and to `verify-A-O/frozen-statements-AO.log`
(`verify-B-O/frozen-compare-BO.log`). 16 axiom lines, all `[propext, Classical.choice, Quot.sound]`. The four Unit A root
statements re-extracted in my clone have the SHA-256 prefixes CHECK-O-A §6 recorded (`444525975a688dff`, `9203e9309edb8ac3`,
`4b4027faf5d3d745`, `d74308b606df73c0`). File level (`verify-B-O/hashes-recheck-BO.log`): `hashes-A.txt` 34 of 37
entries SAME and `hashes-iii.txt` 37 of 41 SAME, every Lean and config file among them; the differences are `Zeta23.lean`
(the imports), `formalization.yaml`, `FIDELITY.md` (all expected) and, in `hashes-iii.txt` only, `BUILD-NOTES-iii.md`
(changed by the Session 23 close commit `594266c` on 2026-09-17, before Unit A; not a Unit B file).

**yaml.** `results/d1-m2a/dr8/validate_yaml_sigma_strong.py` on the mirror `lean/formalization.yaml` (`cmp`-identical to the
clone's): upstream schema IDENTICAL ×3, **VALIDATION errors: 0; RESULT: PASS — errors: 0, undeclared names: 0**;
main_results 27, alignment.statements 28; 96 referenced names, the Unit B ones resolved in `Clause5.lean`, `ZEnclosure.lean`,
`Clause5Cert.lean` (`verify-B-O/yaml-validation-BO.log`).

**Labels.** Every occurrence of the two forbidden labels (the M2-whole and clause-5-whole "… is formalized" forms) in the yaml, `FIDELITY.md`,
`BUILD-NOTES-B.md`, the challenge files and the library headers stands under "never". The 1(a) label is the one on
`Challenge/Separation5.lean` and in (r); the 1(b) label on `Challenge/Separation5c.lean`, in (r) and in BUILD-NOTES-B.

**Lint (10(g); U.S. English)** over the thirteen Lean files, `BUILD-NOTES-B.md`, `FIDELITY.md` (r), the Unit B blocks of
`SHARED.md` and the whole yaml (`verify-B-O/lint-BO.log`): the four 10(g) words occur once, on `BUILD-NOTES-B.md` line 78,
which quotes the banned list; the `-ise` hits are *pointwise*, *noise*, *otherwise*, *likewise*, *wise*. No violation.

**Hashes.** All 52 entries of `hashes-B.txt` recomputed (Lean files read in the clone, records in the repository):
**52/52 SAME**, among them `BUILD-NOTES-B.md` at SHA-256 `44b18ced…4267`.

## §13 MINOR items (recorded; no FIX-FIRST, no edit required)

* **M1 (wording).** The brief says "the frozen FOURTEEN earlier statements (Unit A's twelve + Unit A's two root pairs)";
  the two root pairs hold four theorems, so the probe covers sixteen declarations, as BUILD-NOTES-B says. All sixteen are
  byte-identical; the count is a matter of pairs versus theorems.
* **M2.** `qcell` is a `Nat`-valued definition that depends on no axiom; the builder's "all 74 library theorems on the
  standard three" is correct and counts theorems only. My probe covers the 25 definitions as well (24 on the standard three).
* **M3.** A3 states the decrease of F₁₃ from L = 6.113; the Lean proves it on [50, ∞) only (`F13_le_F13_50`), the range every
  statement uses. (r2) describes the method; a reader of (r2) could be told in one clause that the smaller range is the one
  consumed. No statement is affected.
* **M4.** The certificate's two margins differ in the fourth digit: F₁₃(50) at the endpoints is −0.34741 and the slack in
  `cert_numeric` is 0.34714 nats; the 2.7·10⁻⁴ gap is the 6-term Taylor truncation of e^{E_lo − 40}. BUILD-NOTES-B's
  "≈ 0.347 nats" covers both.

**Optional `zeta_in_class_C1` — SKIPPED.** PRICING-RESIDUE Piece 7 prices it at ½–1 slot and 150–250 new Lean lines: it is a
build, not a check, and a checker who writes it would then be checking its own proof and editing the tree its contract says
to leave untouched. It stays DEFERRED for a builder, with its own check.

## §14 What I checked, and what I did not

**Checked, by running it in my own fresh clone:** provenance and the overlay delta against upstream v1.0; the cold build
(9153 / 0); the solution modules; `#print axioms` on the five roots and on 99 library declarations from my own list; trust
greps (the builder's script and my raw grep); statement identity by two extractions and the diffs against the frozen
statements; the trusted file read in full and diffed against the library; the sixteen frozen statements and the frozen files'
hashes; the four Comparator runs with nanoda; yaml validation; lint; hashes-B 52/52; the certificate modules' elaboration
time. **By paper and my own numerics:** P₂, P₃, F₁₃ against the script at four L (relative difference 0.0); the tail-integral
identity, the chain rule and the limit (symbolic n ≤ 12, quadrature); HR0 against A3; the decrease; the single absorption;
the 16-cell enclosure and the certificate inequality in exact rationals. **Not checked:** the sandbox (the `fake-landrun.sh`
shim, as in every record; a Linux host with landrun would close it); upstream v1.0's own library beyond building it;
`zeta_in_class_C1` (skipped, above).

---

## Verdict table

| # | Item | Verdict |
|---|---|---|
| 1 | Clone provenance (fresh clone, v1.0 `3635e748`) and overlay (191 new, 2 changed; `Zeta23.lean` +26 imports only) | **CLEAN** |
| 2 | Cold build `lake build Zeta23` | **CLEAN** (9153 jobs, 0 errors, 432 s; ZEnclosure 3.4 s, Clause5Cert 3.0 s) |
| 3 | `lake build` of the three Solution modules | **CLEAN** (8716 jobs joint, 0 errors) |
| 4 | `#print axioms` — 5 roots + 99 library declarations | **CLEAN** (standard three ×103; `qcell` none) |
| 5 | Trust greps (thirteen files), two ways | **CLEAN** (the 5 deliberate challenge `sorry`s only) |
| 6 | Statement identity ×5, two extractions | **CLEAN** |
| 7 | Trusted `ChallengeDeps/Separation5.lean` read; defs = library's; imports; `Separation5c` on frozen deps only; M_L in no statement; statement diffs vs `_b` | **CLEAN** |
| 8 | Fidelity ledger (r1)–(r6) | **CLEAN** (6/6; no unlisted weakening) |
| 9 (i) | `P2`, `P3`, `F13` = `r0_73_check.py` 22–33 at L = 50, 100, 10³, 10⁴ (own transcription); only b₁sym and 105/100 differ, declared in (r2) | **CLEAN** |
| 9 (ii) | Antiderivative identity (induction), chain rule u = s²/L, limit at +∞ | **CLEAN** |
| 9 (iii) | `HR0` = A3's one-point check (13/8, R₀ = 73, L₀ = 50), both conjuncts; decrease from the second conjunct; assembly conclusion unchanged; absorption once | **CLEAN** |
| 9 (iv) | Z_lo = 0.2105013520, Z_hi = 0.2336502280, F₁₃(50) at endpoints −0.34741, margin 0.34714 nats (own exact code); bridging sound; `cert_numeric` consumed by `F13_50_neg` | **CLEAN** |
| 9 (v) | `strip` consumed only at `norm_wsum_le_strip`; `Z.strip` in the three solutions | **CLEAN** |
| 10 | The shell device (rung and 1(a)) read | **CLEAN** |
| 11 | Comparator ×4 from the clean clone with nanoda (CONTROL, Clause5Sum, Separation5, Separation5c) | **CLEAN** (`Your solution is okay!` ×4, exit 0 ×4) |
| 12 | Sixteen frozen statements; yaml; labels; lint; hashes-B 52/52 | **CLEAN** |

**OVERALL: CLEAN. No FIX-FIRST.** Four MINOR items in §13; `zeta_in_class_C1` skipped (a build, not a check). The label
this unit ships holds as written: *"Theorem M2's clause-6 assembly is a Comparator-checked theorem over `SepConfig`, modulo
the displayed H-edge and H-B‴, on the three standard axioms, replayed by nanoda"* (topic `Separation5c`); for the pair
`Separation5`: *"… modulo the displayed H-edge, H-B‴ and H-R₀ (the one-point check F₁₃(50; 73) ≤ 0 as a displayed real
inequality) …"*; for the rung: *"clause 5's summability is Comparator-checked"*.
