# H4 — IV.17's pair channel (Prop. 4.5) in Lean with a dyadic certificate on ā: the TYPING NOTE (Session 32, queue rank 3, first half; TYPING-NOTE agent, Fable 5.1)

Started Tue Sep 29 07:13:29 IST 2026. Brief: `results/h4-pair-typing-s32/BRIEF.md` (SHA-256 `508dad4d61c6d9b8755da7e320f95a3adbc50999a4306022595f3c279eeff0dc`, recomputed at the start). This is a READ that
prices a unit: no `lake build`, no theorem proved, no certificate computed; one scratch typing probe (§5). Every source below was read
at the line in the brief's order; sentences marked "I infer" are mine. **Nothing about ζ or RH follows from anything here; the label
the unit may earn is fixed by the brief and quoted verbatim in §6.** The label the unit may earn is "barrier". Paths contain spaces.

Toolchain of the built clone `~/rh-lean-work/checker-clone-s21`: `leanprover/lean4:v4.33.0-rc2`, Lake 5.0.0-src+d8b1897, Mathlib
`51e6992efd` (`git rev-parse --short HEAD` in `.lake/packages/mathlib`). The four `Zeta23/PairCeiling/*.lean` files in the clone
are `cmp`-identical to `rh-program/lean/Zeta23/PairCeiling/` (checked this session), and their oleans exist
(`.lake/build/lib/lean/Zeta23/PairCeiling/{GridCorner,GridParsevalRat,GridGap}.olean`).

## §1 The trusted integer-frequency row

### 1.1 What the paper's row is, at the line

`results/a4-no-go/paper.md` line 121: "c_s = Sum_z m_z e^{-2 pi i s theta_z / N} (a conjugate pair at theta +/- i d contributes
2 m cosh(2 pi s d / N) e^{-2 pi i s theta / N})"; line 126: "tr G-hat^2 = Sum_s W2(s) |c_s|^2, W2(s) = Sum_{j in B, s-j in B}
u_j u_{s-j}"; line 119: "B = {j in Z : |j| <= lambda N/2}, with M = |B| harmonics and uniform weights u_j = 1/M". So the paper's §2.3
row is the SINGLE-convolution form over the integer frequency s, with W2 a filtered double sum over the band, for GENERAL u_j (the
uniform value is substituted afterwards). `results/a4-no-go/pair-channel.md` line 39: "harmonics u_j = 1/65 for |j| <= J = 32;
assembly weights w_s = (65 - |s|)/65^2 for |s| <= 64 (the autocorrelation w = u * u; Sum_s w_s = 1)"; line 46–47: "c_s = Sum_a m_a
e^{-2 pi i s theta_a / N} + Sum_p 2 m_p cosh(2 pi s d_p / N) e^{-2 pi i s theta_p / N}, F1 = Sum_{|s| <= 64} w_s |c_s|^2". So
`pair-channel.md` uses the FLAT u_j = 1/65 and the closed-form weight (65 − |s|)/65²; the paper's W2 at flat u is that closed form
(the count of ordered pairs (j, s − j) in B × B is 65 − |s| for |s| ≤ 64). The two are the same row; the closed form is a lemma to be
proved, not a definition to be assumed (`W2_eq` below).

The shipped Lean rows are the DOUBLE-convolution form: `GridCorner.lean` line 111–115 `gridRow n m := Σ_{j1 ∈ Icc (−n) n} Σ_{j2 ∈
Icc (−n) n} (1/(2n+1))² · normSq (dftMark (zetaM (2n+1)) m ((j1 : ZMod (2n+1)) + (j2 : ZMod (2n+1))))`, and `GridParsevalRat.lean`
line 226–230 `gridRowQ` with `dftMarkQ` in place of `dftMark` — checked: line 226 IS `gridRowQ`'s definition (the brief's first stop
line does not fire). `GridParseval.lean` line 36–41 says why: "We formalize the double-convolution assembly Σ_{j₁,j₂ ∈ B} u u
|c_{j₁+j₂}|² (not the folded single-convolution Σ_s W₂(s)|c_s|²) because it is SPEC 1.4's literal definition of the row … for each j₁
the map j₂ ↦ j₁ + j₂ mod M is a bijection from the band onto ℤ/M". Line 25–26: "the form factor c is the DFT of the mark vector on
ℤ/M — it depends on s only through s mod M". That periodicity is what lets the shipped rows index the coefficient at the REDUCED
residue `(j1 : ZMod (2n+1)) + (j2 : ZMod (2n+1))`. A pair breaks it: its term 2μ cosh(2π s d/N) grows with |s| and is not periodic
mod 2n + 1, so on a pair-containing configuration the shipped rows compute a DIFFERENT number from the paper's row.

**Confirmed at the number (scratchpad, mpmath at 30 digits; `typing-probe` is not involved).** At (d, μ) = (1/4, 1/20), N = 64,
u_j = 1/65, on Prop. 4.5's configuration: the integer-frequency row gives F1 − S2 = −0.0352002534 (the record's −3.520·10⁻²,
`pair-channel.md` line 104), the closed form 2μ²ā(2d)² − 4μ(ā(d)² − 1) gives the same digits, and the mod-65-REDUCED row (the
`gridRowQ` shape with the pair's cosh evaluated at the reduced residue in [−32, 32]) gives −0.0144817. So ORCHESTRATOR-NOTES item 2
holds as computed, not only as read: "a pair contributes 2μ cosh(2π s d/N) at the UNREDUCED s ∈ [−2n, 2n] … which is not periodic mod
65" — the unit needs the new row.

### 1.2 The row, in Lean-typed pseudocode (every type explicit)

All in `noncomputable section`, `open Finset`, namespace `Zeta23.PairCeiling.PairRow` (I infer the name from the file pattern),
importing `Zeta23.PairCeiling.GridParsevalRat` (which brings `chi`, `dftMarkQ`, `zetaM`, `gridRowQ`). `n : ℕ` throughout; the grid
has M = 2n + 1 sites and the circle has circumference N = 2n (`GridParseval.lean` line 394: "Even period N = 2n, M = N + 1 = 2n + 1").

    -- the assembly weight of paper §2.3 line 126 at the flat u_j = 1/(2n+1) (u is substituted, W2's shape is the paper's):
    def W2 (n : ℕ) (s : ℤ) : ℝ :=
      ∑ j ∈ (Finset.Icc (-(n : ℤ)) (n : ℤ)).filter (fun j : ℤ => s - j ∈ Finset.Icc (-(n : ℤ)) (n : ℤ)),
        (1 / (2 * (n : ℝ) + 1)) * (1 / (2 * (n : ℝ) + 1))

    -- the pair-containing form factor at the UNREDUCED integer frequency s:
    --   atoms on the grid with rational marks m (the DFT at the reduced residue (s : ZMod (2n+1)) — periodic, so harmless),
    --   pairs at grid sites p.1 with real mark p.2.1 and real depth p.2.2 — 2 μ cosh(2π s d / N) χ(s · θ_p), s UNREDUCED inside cosh:
    def pairFormFactor (n : ℕ) (m : ZMod (2 * n + 1) → ℚ)
        (pairs : Finset (ZMod (2 * n + 1) × ℝ × ℝ)) (s : ℤ) : ℂ :=
      dftMarkQ (zetaM (2 * n + 1)) m (s : ZMod (2 * n + 1))
        + ∑ p ∈ pairs,
            ((2 * p.2.1 * Real.cosh (2 * Real.pi * (s : ℝ) * p.2.2 / (2 * (n : ℝ))) : ℝ) : ℂ)
              * chi (zetaM (2 * n + 1)) ((s : ZMod (2 * n + 1)) * p.1)

    -- the row of paper §2.3 line 126, over the unreduced s ∈ [−2n, 2n]:
    def pairRow (n : ℕ) (m : ZMod (2 * n + 1) → ℚ) (pairs : Finset (ZMod (2 * n + 1) × ℝ × ℝ)) : ℝ :=
      ∑ s ∈ Finset.Icc (-(2 * (n : ℤ))) (2 * (n : ℤ)), W2 n s * Complex.normSq (pairFormFactor n m pairs s)

    -- ā of pair-channel.md line 69, "abar(x) := psi(ix) = Sum_j u_j cosh(2 pi j x / N)":
    def abar (n : ℕ) (x : ℝ) : ℝ :=
      ∑ j ∈ Finset.Icc (-(n : ℤ)) (n : ℤ), (1 / (2 * (n : ℝ) + 1)) * Real.cosh (2 * Real.pi * (j : ℝ) * x / (2 * (n : ℝ)))

    -- Prop. 4.5's atom part, "the vacancy lattice (unit atoms on grid sites g_1..g_64)" (paper.md line 405): mark 1 off the hole g_0 = 0:
    def vacancyMark (n : ℕ) : ZMod (2 * n + 1) → ℚ := fun k => if k = 0 then 0 else 1

Where each object lives, and which casts occur:
* `s : ℤ` is the integer frequency, summed over `Finset.Icc (−2n) (2n) : Finset ℤ` (`Mathlib/Data/Int/Interval.lean` supplies the
  `LocallyFiniteOrder ℤ` instance; `Int.card_Icc` at its line 96). It enters the pair term through `Int.cast : ℤ → ℝ` (`(s : ℝ)`,
  unreduced) and the atom term and the pair's phase through `Int.cast : ℤ → ZMod (2n+1)` (`(s : ZMod (2n+1))`, reduced). The two casts
  of the same `s` are the whole point of the row.
* `j : ℤ` in `W2` and `abar`: the band index, `Finset.Icc (−n) n`, with the flat weight written out as `(1/(2n+1))·(1/(2n+1))` exactly
  as `gridRowQ` writes it (line 228) so that the agreement lemma (§2) meets it syntactically.
* `p.1 : ZMod (2n+1)` the pair's grid site; `p.2.1 : ℝ` its mark μ; `p.2.2 : ℝ` its depth d. A `Finset` of triples needs no
  `DecidableEq ℝ` for `Finset.sum` (the singleton `{(0, 1/20, 1/4)}` the certificate uses needs only `Singleton`); it does need
  `DecidableEq` for `insert`, which the real-valued components supply only classically — acceptable in a `noncomputable section`
  (I infer; the probe checks the singleton only).
* `Real.cosh : ℝ → ℝ` (`Mathlib/Analysis/Complex/Trigonometric.lean` line 760 `cosh_eq (x : ℝ) : cosh x = (exp x + exp (-x)) / 2`);
  `Real.pi`; the product `2 · μ · cosh(…) : ℝ` is then cast to `ℂ` by `Complex.ofReal` (the `((… : ℝ) : ℂ)` ascription) and
  multiplied by the character `chi (zetaM (2n+1)) ((s : ZMod (2n+1)) * p.1) : ℂ` (`GridParseval.lean` line 144 `chi ζ x := ζ ^ x.val`;
  line 357 `zetaM M := Complex.exp (2 * Real.pi * Complex.I / M)`).
* `Complex.normSq : ℂ → ℝ` gives |c_s|²; `W2 n s * normSq (…) : ℝ`; the row is a real number, as `gridRowQ` is.
* Atom marks are `ℚ` (so that `pairRow n m ∅` can be compared with `gridRowQ n m`, §2); pair marks are `ℝ` (Prop. 4.5 says "REAL mark
  mu > 0", paper line 405). Mixed mark types are deliberate; the brief's `atoms : Finset (ZMod (2n+1) × ℚ)` is replaced by the function
  `m : ZMod (2n+1) → ℚ` because that is the shipped vocabulary (`gridRowQ n m`) and "atoms of m" in the agreement lemma is then `m`
  itself. Decision recorded as fidelity row (F4) below.

### 1.3 Is the row the paper's §2.3 row character for character? — a restatement; the fidelity rows

* **(F1) Weights.** The paper's W2 is defined for general u (line 126) and then flat u is substituted (line 119 "uniform weights
  u_j = 1/M"). `W2 n s` above is the paper's filtered double sum with the flat value written in; the closed form
  `W2 n s = (2n + 1 − |s|)/(2n + 1)²` for |s| ≤ 2n (`pair-channel.md` line 39) is the lemma `W2_eq`, proved by `Int.card_Icc` on the
  filter (which is `Icc (max (−n) (s − n)) (min n (s + n))`) — the same bookkeeping as `weight_telescoping` (`GridParseval.lean`
  line 453–517, 65 lines, which proves the residue-class sum of exactly this closed form). I infer 20–30 lines. The row does not depend
  on `W2_eq`; only the closed-form reading of `pair-channel.md` does.
* **(F2) Sign of the character.** The paper's phase is e^{−2πi s θ/N}; `chi` is ζ^{x.val} with ζ = e^{2πi/M}, i.e. e^{+2πi r k/M}.
  `GridParseval.lean` line 143: "the sign convention is immaterial: the statements below pair r with −r". With a pair the same holds:
  `normSq` is invariant under conjugation of every term, and the cosh factor is real and even in s. No content changes; recorded.
* **(F3) Pair positions.** The paper's pair sits at any real θ_p; the row above puts pairs on GRID SITES (`p.1 : ZMod (2n+1)`), because
  Prop. 4.5 needs only "one pair at the hole g_0" (paper line 405) and because a real θ_p would need a second character
  `Complex.exp (−2πi s θ/N)` outside the `chi` vocabulary. This is a RESTRICTION of the paper's row, not a change of any value on
  grid-supported pairs. The general-position row is typeable (replace `chi (…) (s · p.1)` by `Complex.exp (−2 * π * I * s * θ / N)`)
  and is not needed by the unit.
* **(F4) Mark types.** Atoms ℚ, pairs ℝ (§1.2). The paper's atoms in Prop. 4.5 are unit marks; ℚ ⊇ ℤ ∋ 1.
* **(F5) The circle length.** N = 2n is written `2 * (n : ℝ)` inside the cosh argument, and M = 2n + 1 as `2 * (n : ℝ) + 1` in the
  weights — the shipped files' spellings (`GridCorner.lean` line 113).
* **(F6) Reduction.** The pair's cosh takes the UNREDUCED `(s : ℝ)`; the atoms' DFT and the pair's phase take the reduced
  `(s : ZMod (2n+1))`. §1.1's numbers show the reduced-cosh alternative is a different row (−0.01448 versus −0.03520 at the anchor).

**Where the mark type enters (the IV.17 precedent's question, `results/iv17-lean-s30/TYPING-NOTE.md` line 12–24).** Through
`dftMarkQ` only (`GridParsevalRat.lean` line 137–138: `(m k : F) * chi ζ (r * k)`, `Rat.cast` into a field) and through the real
product `2 * p.2.1 * Real.cosh (…)`; nothing in the row is an inequality, so no integrality is consumed in §1. The integer-mark safety
chain of Prop. 4.5 (§6) is where `m : ℕ`, `1 ≤ m` enters, and it enters through `nlinarith`, exactly as `per_atom_slack`
(`GridGap.lean` line 62–69) does.

## §2 The agreement lemma

**Statement.** \`pairRow_eq_gridRowQ : ∀ (n : ℕ) (m : ZMod (2 * n + 1) → ℚ), pairRow n m ∅ = gridRowQ n m\` — no pairs, grid atoms
with rational marks. With \`gridRowQ_eq\` (\`GridParsevalRat.lean\` line 234–239: \`gridRowQ n m = ((Σ_k (m k)^2 : ℚ) : ℝ)\`) it gives
\`pairRow n m ∅ = Σ_k m_k²\` at once — the atom-only Parseval on the new row, which Prop. 4.5's proof consumes for the vacancy lattice.

**Do the existing lemmas give it directly? — No; they start one step later.** \`sum_band_pair\` (\`GridParseval.lean\` line 313–329)
collapses the DOUBLE sum over (j1, j2) ∈ B × B of a function of the residue \`(j1 : ZMod M) + (j2 : ZMod M)\` to \`M · Σ_{r : ZMod M} f r\`,
and \`flat_band_trace_sq\`/\`trace_sq_grid\` (lines 339–352, 426–439) apply it to \`dftMark\`. The agreement lemma is the step BEFORE the
double sum: it regroups the SINGLE sum over the integer s ∈ [−2n, 2n], weighted by the filtered pair count \`W2 n s\`, into the double sum
over (j1, j2). Nothing shipped does that regrouping (\`weight_telescoping\`, line 453–517, regroups the closed-form weight by residue
class, which is the SAME regrouping composed with \`sum_band_pair\` — usable as an alternative route, see below). So a new lemma is
needed; no new idea is.

**The route (I infer; the probe of §5 elaborates the statements).**
1. \`sum_W2_mul (n) (g : ℤ → ℝ) : Σ_{s ∈ Icc (−2n) (2n)} W2 n s * g s = Σ_{j1 ∈ B} Σ_{j2 ∈ B} (1/M)(1/M) * g (j1 + j2)\` — generic in
   \`g\`, used by §2 (with \`g s = normSq (dftMarkQ … (s : ZMod M))\`) and by §3 (with \`g s = cosh(2π s x/N)\`). Proof: unfold \`W2\`,
   pull \`g s\` into the filtered sum (\`Finset.sum_mul\`), rewrite the filtered sum over j as a sum over the fiber
   \`{(j1, j2) ∈ B ×ˢ B | j1 + j2 = s}\` (the bijection j ↦ (j, s − j), \`Finset.sum_nbij'\` with inverse \`Prod.fst\` — the shape of
   \`sum_band\`'s five obligations, line 280–307), then \`Finset.sum_fiberwise_of_maps_to\` (\`Mathlib/Algebra/BigOperators/Group/Finset/Basic.lean\`
   line 256, additive form by \`to_additive\`: \`(h : ∀ i ∈ s, g i ∈ t) → ∑ y ∈ t, ∑ x ∈ s with g x = y, f x = ∑ x ∈ s, f x\`) with the map
   \`(j1, j2) ↦ j1 + j2 : B ×ˢ B → Icc (−2n) (2n)\` (the membership obligation is \`omega\` after \`Finset.mem_Icc\`), and finally
   \`Finset.sum_product\` (\`…/Finset/Sigma.lean\` line 80) to split \`B ×ˢ B\` into the iterated sum. Estimated 40–55 lines.
2. \`pairRow_eq_gridRowQ\`: unfold \`pairRow\`, \`pairFormFactor\` with \`pairs = ∅\` (\`Finset.sum_empty\`, \`add_zero\`), apply
   \`sum_W2_mul\`, then match \`gridRowQ\` termwise: the only difference is the cast \`((j1 + j2 : ℤ) : ZMod M)\` against
   \`(j1 : ZMod M) + (j2 : ZMod M)\` — \`Int.cast_add\` (\`push_cast\`). Estimated 10–15 lines.

Alternative route (not recommended): prove \`W2_eq\` first (§1 (F1)), then filter the s-sum by residue class and use
\`weight_telescoping_rat\` (line 522–536) plus \`sum_dftMarkQ_mul_neg\`; that reproves Parseval instead of reusing \`gridRowQ_eq\`, and
needs the residue-class fibering anyway. The fiberwise route reuses everything.

**Size against the precedents.** \`sum_band\` is 30 lines for one \`sum_nbij'\`; \`sum_band_pair\` 17 lines; \`weight_telescoping\` 65
lines. I estimate the agreement lemma plus its generic regrouping at 55–70 lines, and \`W2_eq\` (optional) at 20–30.

## §3 The generating identity (T1)

**Source.** \`pair-channel.md\` line 71: "(T1) Generating identity. Sum_s w_s q^s = (Sum_j u_j q^j)^2 for every q != 0 (w = u * u)";
line 104 (Prop. 3.1's proof): "Sum_s w_s cosh(beta s) = abar(d)^2 and Sum_s w_s cosh(2 beta s) = abar(2d)^2 (both from (T1) at
imaginary arguments)"; \`paper.md\` line 411: "the assembly weights w = u * u factor through psi at imaginary arguments".

**Statement over ℝ with \`Finset\` sums.** \`sum_W2_cosh : ∀ (n : ℕ) (x : ℝ), Σ_{s ∈ Icc (−2n) (2n)} W2 n s * Real.cosh (2π s x / (2n))
= abar n x ^ 2\`, with \`abar n x := Σ_{j ∈ Icc (−n) n} (1/M) * Real.cosh (2π j x / (2n))\` (§1.2). Prop. 4.5 consumes it at x = d and
x = 2d, and at x = 0 (where it reads \`Σ_s W2 n s = 1\`, since \`Real.cosh_zero\` and \`abar n 0 = 1\`).

**The exact route (I infer).** Not the q-power form (which would need \`Real.exp\` and the negative-power bookkeeping): the
\`cosh_add\` form, which needs no \`exp\` at all.
1. \`sum_W2_mul\` (§2 item 1) with \`g s = cosh(β s)\`, β = 2π x/(2n): the left side becomes
   \`Σ_{j1} Σ_{j2} (1/M)(1/M) cosh(β(j1 + j2))\`; the cast \`((j1 + j2 : ℤ) : ℝ) = (j1 : ℝ) + (j2 : ℝ)\` by \`push_cast\`, and
   β(j1 + j2) = βj1 + βj2 by \`ring\` inside the argument (\`congr 1\` or \`mul_add\`).
2. \`Real.cosh_add\` (\`Mathlib/Analysis/Complex/Trigonometric.lean\` line 776: \`cosh (x + y) = cosh x * cosh y + sinh x * sinh y\`):
   the double sum splits by \`Finset.sum_add_distrib\` into \`Σ Σ u u cosh cosh + Σ Σ u u sinh sinh\`; each is a product of two single
   sums by \`Finset.sum_mul_sum\` (used at \`GridParseval.lean\` line 235) read right to left: \`(Σ_j u cosh(βj))² + (Σ_j u sinh(βj))²\`.
3. The sinh sum vanishes on the symmetric band: \`Σ_{j ∈ Icc (−n) n} u * sinh(βj) = 0\` by \`Finset.sum_involution\`
   (\`…/Finset/Basic.lean\` line 665, additive form) with the involution j ↦ −j, \`Real.sinh_neg\` (line 754), the fixed point j = 0
   where \`sinh 0 = 0\`, and \`Finset.mem_Icc\` + \`omega\` for the membership obligations; or by \`Finset.sum_nbij'\` with negation giving
   S = −S. Estimated 15–20 lines.
4. Then \`abar n x ^ 2 + 0 ^ 2\`; \`sq\`, \`ring\`. The whole identity: 35–50 lines. The precedent of the same flavor is
   \`sum_dftMark_mul_neg\` (line 228–272, 45 lines, the same \`sum_mul_sum\` + \`sum_comm\` + orthogonality shape).

**Mathlib check.** \`Real.cosh_add\`, \`Real.sinh_neg\`, \`Real.cosh_neg\` (line 769), \`Real.cosh_zero\` (766) exist at 51e6992e (read at the
line). Nothing here needs a bound; (T1) is exact algebra, as the record says ("exact identities", \`pair-channel.md\` line 65).

## §4 The dyadic certificate

### 4.1 The target and the configuration, from the source

\`paper.md\` line 405–407 (Prop. 4.5, verbatim): "Let c_mu be the vacancy lattice (unit atoms on grid sites g_1..g_64) plus one pair at
the hole g_0 with depth d > 0 and REAL mark mu > 0. Then, exactly, F1(c_mu) - S2(c_mu) = 2 mu^2 abar(2d)^2 - 4 mu (abar(d)^2 - 1)";
line 399: "N = 64, flat window, lambda = 1; … grid g_k = k 64/65"; line 411: "the numeric check at (d, mu) = (0.25, 0.05) reproduces
it to 1e-12, with F1 - S2 = -3.520e-2". \`pair-channel.md\` line 49: "S2 = Sum_a m_a^2 + 2 Sum_p m_p^2". In the vocabulary of §1:
n = 32, atoms \`vacancyMark 32 : ZMod 65 → ℚ\` (mark 1 on the 64 sites k ≠ 0, mark 0 at the hole k = 0), one pair
\`{((0 : ZMod 65), (1/20 : ℝ), (1/4 : ℝ))}\` at the hole with μ = 1/20 and d = 1/4; S2 = 64 + 2μ² = 64 + 1/200. **The target is the
FLOOR's failure:** \`floor_fails_anchor : pairRow 32 (vacancyMark 32) {(0, 1/20, 1/4)} < 64 + 2 · (1/20)²\`. At this anchor (MI) holds
(BRIEF "Why", second bullet: T = 60.300, F1 − T = +3.67 > 0); the certificate says nothing about (MI).

### 4.2 F1 − S2 in closed form, and what the proof of Prop. 4.5 needs

From \`paper.md\` line 411: "On the vacancy lattice the atom form factor is phi_0(s) = 64 at s ≡ 0 and -1 otherwise; the pair adds
2 mu cosh(beta s), beta = 2 pi d/N. Expanding F1 = Sum_s w_s |c_s|^2 with the generating identities Sum_s w_s cosh(beta s) = abar(d)^2
and Sum_s w_s cosh(2 beta s) = abar(2d)^2 … gives the display". The direct expansion, in the row of §1 (I infer the Lean steps):

    c_s = φ₀(s) + 2μ cosh(βs)   (real: the pair's phase at the hole is chi (zetaM 65) (s · 0) = 1, GridParseval.lean line 147 chi_zero)
    Σ_s W2(s) c_s² = Σ_s W2 φ₀²  +  4μ Σ_s W2 φ₀ cosh(βs)  +  4μ² Σ_s W2 cosh²(βs)
                   = 2n          +  4μ [W2(0)·2n − (ā(d)² − W2(0))]  +  2μ² [Σ_s W2 + ā(2d)²]
                   = 2n + 4μ [(2n + 1)/(2n + 1) − ā(d)²] + 2μ² [1 + ā(2d)²]
                   = (2n + 2μ²) + 2μ² ā(2d)² − 4μ (ā(d)² − 1).

The five ingredients, each a lemma of the unit: (i) \`Σ_s W2 φ₀² = 2n\` — the agreement lemma (§2) + \`gridRowQ_eq\` + \`Σ_k (vacancyMark n k)²
= 2n\` (\`Finset.sum_ite\`, \`ZMod.card\`; kernel-free, generic n); (ii) \`φ₀(s) = if (s : ZMod (2n+1)) = 0 then 2n else −1\` — the DFT of
the all-ones vector minus the hole, from character orthogonality \`sum_chi_mul\` (\`GridParseval.lean\` line 190) and \`chi_zero\`;
together with "\`(s : ZMod (2n+1)) = 0\` iff s = 0 for |s| ≤ 2n" from \`ZMod.intCast_zmod_eq_zero_iff_dvd\` and
\`int_eq_zero_of_dvd_of_bounds\` (line 104, already in the file); (iii) \`W2 n 0 = 1/(2n+1)\` (the filter at s = 0 is the whole band,
\`Int.card_Icc\`); (iv) §3's identity at x = d, x = 2d and x = 0 (\`Σ_s W2 = 1\`); (v) \`cosh² y = (1 + cosh 2y)/2\` from
\`Real.cosh_two_mul\` (line 830) and \`Real.cosh_sq\` (line 823) — \`cosh (2y) = cosh² y + sinh² y = 2 cosh² y − 1\`. The form factor's
reality: \`Complex.normSq_ofReal\` after \`dftMarkQ\` at \`vacancyMark\` is rewritten to a real cast. Prop. 4.1's ledger (\`pair-channel.md\`
line 112–122) is NOT needed — the paper's proof of Prop. 4.5 (line 411) does not use it; Theorem C's "one-line cosh² factorization"
(line 29) is item (v). So Prop. 4.5 is provable for EVERY n, d, μ from §2–§3 plus five small lemmas; the probe's \`prop45\` states it for
general n.

### 4.3 The transcendental quantities, the signs, the error budget

F1 − S2 = 2μ²ā(2d)² − 4μ(ā(d)² − 1) is increasing in ā(2d) and decreasing in ā(d). So an UPPER bound U ≥ ā(1/2) and a LOWER bound
L ≤ ā(1/4) give \`F1 − S2 ≤ 2μ²U² − 4μ(L² − 1)\`, and the certificate is that this right side is < 0 at μ = 1/20. The quantities:
* ā(1/4) = (1/65) Σ_{j=−32}^{32} cosh(πj/128), arguments |x| ≤ π/4 = 0.7854 — needs cosh LOWER bounds;
* ā(1/2) = (1/65) Σ_{j=−32}^{32} cosh(πj/64), arguments |x| ≤ π/2 = 1.5708 — needs cosh UPPER bounds;
* π, through \`Real.pi_gt_d6 : 3.141592 < π\` and \`Real.pi_lt_d6 : π < 3.141593\` (\`Mathlib/Analysis/Real/Pi/Bounds.lean\` lines 178,
  184, namespace \`Real\` at line 26; present at 51e6992e).
Values (scratchpad, 30 digits): ā(1/4) = 1.1094437000, ā(1/2) = 1.4814055033, 2μ²ā(1/2)² = 0.0109728, 4μ(ā(1/4)² − 1) = 0.0461731,
F1 − S2 = −0.0352003 (the record).

**Error budget (the brief's form).** With ā(1/4) ≥ L = ā(1/4) − δ₁ and ā(1/2) ≤ U = ā(1/2) + δ₂, to first order the bound on F1 − S2
worsens by 8μ ā(1/4) δ₁ + 4μ² ā(1/2) δ₂ = 0.4438 δ₁ + 0.0148 δ₂ (the brief's "4μ·2ā·δ + 2μ²·2ā(2d)·δ′"). Against the margin 0.0352:
δ₁ < 0.0793 alone, δ₂ < 2.376 alone. A safe split is δ₁ ≤ 0.04 and δ₂ ≤ 1.0. Since ā is the AVERAGE of 65 cosh values, a uniform
per-cosh error δ_c gives δ ≤ δ_c: **the per-cosh tolerance is 0.04 at d = 1/4 (lower bounds) and 1.0 at 2d = 1/2 (upper bounds).**
Dyadic precision 2⁻²⁰ ≈ 10⁻⁶ is four to six orders of magnitude finer than needed; 2⁻⁸ would do.

### 4.4 How each enclosure is proved — the Mathlib lemmas that exist at 51e6992e

No \`norm_num\` extension evaluates \`Real.exp\`, \`Real.cosh\` or \`Real.pi\` (grep over \`Mathlib/Tactic/NormNum/\` and \`Mathlib/Tactic/Positivity/\`:
empty). The enclosures therefore go through Taylor bounds, as Unit B's \`ZEnclosure.lean\` did (lines 112–146: \`exp_neg_le_inv_taylor\`
from \`Real.sum_le_exp_of_nonneg\`, \`exp_le_taylorT\` from \`Real.exp_bound'\` at n = 8). Two GENERIC lemmas suffice, and both statements
elaborated in the probe (§5, items (g)):
* **Lower, all x:** \`1 + x²/2 ≤ Real.cosh x\`. Proof route: \`cosh x = cosh (2·(x/2)) = cosh²(x/2) + sinh²(x/2) = 1 + 2 sinh²(x/2)\`
  (\`Real.cosh_two_mul\`, \`Real.cosh_sq\`); \`(x/2)² ≤ sinh²(x/2)\` from \`Real.abs_sinh : |sinh x| = sinh |x|\` (DerivHyp.lean line 419)
  and \`Real.self_le_sinh_iff : x ≤ sinh x ↔ 0 ≤ x\` (line 451) applied at |x/2|; \`nlinarith\`. About 12 lines. Alternative:
  \`Real.cosh_eq_tsum\` (Series.lean line 149) with \`sum_le_tsum\` at two terms. Error at |x| ≤ π/4: cosh x − 1 − x²/2 ≤ x⁴/24·cosh x
  ≤ 0.021; averaged with the j-weights it is 0.0034 (scratchpad: L = 1.1060211 against 1.1094437) — under the tolerance 0.04.
* **Upper, |x| ≤ 9/2:** \`Real.cosh x ≤ 1 + x²/2 + x⁴/24 + x⁶/720 + x⁸/20160\`. Proof route: \`Complex.exp_bound'\`
  (\`Mathlib/Analysis/Complex/Exponential.lean\` line 407: \`‖x‖ / n.succ ≤ 1/2 → ‖exp x − Σ_{m<n} x^m/m!‖ ≤ ‖x‖^n / n! * 2\`) at n = 8,
  which asks only |x| ≤ 9/2 (so π/2 is covered without any half-angle device), transferred to ℝ by \`Complex.ofReal_exp\` and
  \`Complex.norm_real\` (I infer the transfer at 10–15 lines; the Real version \`Real.exp_bound\` at line 517 needs |x| ≤ 1 and would force a
  half-angle step for j ≥ 21 at 2d = 1/2); applied at x and −x, the odd terms cancel in \`cosh_eq\` and the two remainders add to
  2x⁸/8! = x⁸/20160. About 30 lines. Error at x = π/2: the remainder 2(π/2)⁸/40320 = 0.0018 — three orders under the tolerance 1.0.
  (The x⁶ term alone is 0.021 at π/2; even \`1 + x²/2 + x⁴/24 + x⁶/500\`, a cruder cap, gives U ≤ 1.48273, scratchpad.)
* **π:** \`pi_gt_d6\`/\`pi_lt_d6\`, and monotonicity of each even power in π on [3.141592, 3.141593] (\`pow_le_pow_left\`, positivity of π —
  \`Real.pi_pos\`). If the record's "dyadic integers" wording (10(j)) is wanted literally, the bracket \`3294198/2²⁰ < π < 3294200/2²⁰\`
  follows from the two d6 lemmas by \`norm_num\` and loses 2⁻¹⁹ — invisible at these tolerances.

**Import fact from the probe (§5).** \`Real.pi_gt_d6\`, \`pi_lt_d6\`, \`self_le_sinh_iff\`, \`abs_sinh\`, \`one_le_cosh\`, \`cosh_le_exp_half_sq\`
were "unknown constants" under \`import Zeta23.PairCeiling.GridParsevalRat\` while \`Real.cosh_eq\`, \`cosh_two_mul\`, \`cosh_sq\` resolved.
Read at the line, all six live in \`namespace Real\` of files that \`GridParseval.lean\`'s eight imports (lines 84–91) do not reach:
\`Mathlib/Analysis/Real/Pi/Bounds.lean\`, \`…/SpecialFunctions/Trigonometric/DerivHyp.lean\`, \`…/Trigonometric/Series.lean\`. I infer the
certificate module must \`import\` those three explicitly (ChallengeDeps imports \`Mathlib\` wholesale, line 33, and is unaffected). This
is a one-line fix per file, recorded here so that the unit does not spend a build on it.

### 4.5 Two routes, the cell count, the kernel time, the ten-minute line

**Route P (power sums; recommended).** Because ā is linear in the 65 cosh values, the two generic bounds pass through the sum
symbolically: Σ_j (1/65)(1 + (πj/64)²/2 + (πj/64)⁴/24 + (πj/64)⁶/720 + (πj/64)⁸/20160) = 1 + π²S₂/(2·64²·65) + π⁴S₄/(24·64⁴·65) +
π⁶S₆/(720·64⁶·65) + π⁸S₈/(20160·64⁸·65) with the INTEGER power sums S₂ = 22880, S₄ = 14492192, S₆ = 10924353440, S₈ = 8964042662432
over j ∈ [−32, 32] (scratchpad; S₂ kernel-checked by the probe). Kernel-checked cells: (1) the lower generic lemma; (2) the upper generic
lemma; (3)–(6) the four power sums by \`decide +kernel\` over \`Finset.Icc (−32 : ℤ) 32\` — the probe closed S₂ = 22880 inside a 7.41 s
file whose import alone accounts for most of that (the IV.17 probe, same import weight, took 8.53 s with three \`decide +kernel\` facts on
\`ZMod 65\`), so I infer ≤ 1 s each; (7) \`ā(1/2) ≤ U(3.141593)\` and \`ā(1/4) ≥ L(3.141592)\` — two π-bracket steps; (8) the final
rational inequality \`2μ²U² − 4μ(L² − 1) < 0\` by \`norm_num\` over ℚ, numerators of about 60 digits (Unit B's \`cert_numeric\` did 294- and
577-digit numerators in a 3.4 s module, \`results/c2-m4/BUILD-NOTES-B.md\` line 14). Value of the certified bound: 2(1/20)²(1.48273)² −
4(1/20)(1.10602² − 1) = 0.010993 − 0.044656 = **−0.0337 < 0** (scratchpad; the record's −0.0352 with 0.0015 of margin spent). **Cells: 9.
No per-term cosh enclosure at all.** Symbolic glue (not cells): expanding the weighted polynomial sum into the power sums —
\`Finset.sum_add_distrib\`, \`Finset.mul_sum\`, \`mul_pow\`, \`push_cast\`, \`Int.cast_sum\` — about 40 lines; the hypothesis |πj/64| ≤ 9/2 for
|j| ≤ 32 from \`pi_lt_d6\` — 5 lines.
**Kernel time estimate:** import and elaboration 8–10 s (the probe's 7.41 s), four \`decide +kernel\` ≤ 4 s, one \`norm_num\` ≤ 2 s, the
generic lemmas' \`nlinarith\`/\`positivity\` ≤ 5 s: **15–30 s for the certificate module** against the ten-minute line (Unit B's
\`ZEnclosure\` 3.8 s builder / 3.38 s checker / 8.2 s cold, CHECK-O-B lines 63, 77; \`Clause5Cert\` 3.4 s; IV.17's \`GridGap\` 1.3 s with
three kernel facts). **Under the line by a factor of 20 or more; no module split is needed.** By the 10(j) discipline the unit still
keeps the certificate in its own module (\`PairCert.lean\`: the two generic bounds, the four power sums, the bracket, the final
inequality) beside the identity module (\`PairRow.lean\`: §1–§3, Prop. 4.5, the safety chain), so that a reader sees "numerics as one
small certificate module".

**Route T (per-term, the brief's shape; fallback).** 33 distinct |j| × 2 depths = 66 cosh enclosures, each the generic lemma at the
rational multiple πj/64 or πj/128 of π followed by the π bracket and one \`norm_num\` — 66 cells, plus the two sum assemblies (\`cosh_neg\`
folds j and −j). Per cell ≤ 0.3 s by the \`ZEnclosure\` rate (16 cells with degree-8 Taylor rationals in 3.4–3.8 s); **about 20–40 s the
module**, still far under ten minutes. Route T needs no power-sum glue but 66 named facts; it is the fallback if the symbolic
expansion of Route P proves fiddly. Neither route needs a module split; neither approaches the line.

**Precision, once more, in the brief's terms.** A degree-8 Taylor polynomial with \`Complex.exp_bound'\`'s remainder at |x| ≤ π/2 reaches
0.002 per cosh — 500 times finer than the tolerance 1.0 at 2d = 1/2; the degree-2 lower bound reaches 0.021 per cosh at |x| ≤ π/4,
0.0034 after averaging — 10 times finer than the tolerance 0.04 at d = 1/4. Nothing needs 2⁻²⁰.

## §5 The scratch typing probe

**File.** \`results/h4-pair-typing-s32/typing-probe.lean\` (96 lines): \`import Zeta23.PairCeiling.GridParsevalRat\`; the six definitions of
§1 (\`W2\`, \`pairFormFactor\`, \`pairRow\`, \`abar\`, \`vacancyMark\`) in a probe namespace; ten theorem statements, every proof \`sorry\`:
(a) \`W2_eq\`; (b) \`sum_W2_mul\`, \`pairRow_eq_gridRowQ\` (§2); (c) \`sum_W2_cosh\` (§3); (d) \`prop45\` for every n, d, μ; (e) \`abar_sq_le\`,
\`floor_holds_integer\`; (f) \`floor_fails_anchor\` — the certificate's statement, \`pairRow 32 (vacancyMark 32) {(0, 1/20, 1/4)} < 64 + 2(1/20)²\`;
(g) the two generic cosh bounds; (h) fifteen \`#check\`s; (i) one \`decide +kernel\` power sum. **Command, log:** \`typing-probe.log\` — cwd
\`~/rh-lean-work/checker-clone-s21\`, \`lake env lean "<the probe's absolute path>"\`, toolchain \`leanprover/lean4:v4.33.0-rc2\`, Lake
5.0.0-src+d8b1897, Mathlib 51e6992efd; started 07:15:22 IST, **7.41 s wall**, exit code 1. No \`lake build\` was run; the clone's oleans were
not touched.

**Result.** Every definition and every one of the ten statements ELABORATED (the log shows exactly ten "declaration uses \`sorry\`"
warnings at lines 41, 45, 51, 55, 60, 65, 66, 70, 74, 75, and no error at any of them): the casts \`(s : ℝ)\` and \`(s : ZMod (2n+1))\` of
the same \`s : ℤ\`, the \`Finset (ZMod (2n+1) × ℝ × ℝ)\` of pairs with the singleton \`{((0 : ZMod 65), (1/20 : ℝ), (1/4 : ℝ))}\`, the
\`((… : ℝ) : ℂ)\` ascription of the cosh factor, \`Complex.normSq\`, \`Finset.Icc\` on ℤ with the filter, and \`gridRowQ n m\` on the right of
the agreement lemma all typecheck against the built \`GridParsevalRat\`. The \`decide +kernel\` fact \`Σ_{j ∈ Icc (−32 : ℤ) 32} j² = 22880\`
(line 95) closed inside the 7.41 s. One linter warning (line 18): the summation binder \`j\` of \`W2\` is unused in its constant summand —
cosmetic (\`_j\`, or \`(filter …).card • (1/M)²\`). **Errors: six, all \`#check\` lines** — "Unknown constant" for \`Real.pi_gt_d6\`,
\`Real.pi_lt_d6\`, \`Real.self_le_sinh_iff\`, \`Real.abs_sinh\`, \`Real.cosh_le_exp_half_sq\`, \`Real.one_le_cosh\` — the import-closure fact
of §4.4 (the names are read at the line in \`namespace Real\`; their files are not imported by \`GridParseval.lean\`); \`Real.exp_bound\`,
\`Complex.exp_bound'\`, \`Real.cosh_eq\`, \`Real.cosh_two_mul\`, \`Real.cosh_sq\`, \`Finset.sum_fiberwise_of_maps_to\`, \`Finset.sum_involution\`,
\`Finset.sum_product\`, \`Int.card_Icc\` printed their types (the log holds them; \`sum_fiberwise_of_maps_to\` needs \`[DecidableEq κ]\` on the
target index type — ℤ has it). **Stop line (iii) does not fire** (the import elaborated within the 7.41 s run, the line was 60 s).
Time against the brief's ≤ 30 s: 7.41 s.

## §6 The price

**The label the unit may earn (BRIEF, verbatim, binding):** "IV.17's pair channel: Prop. 4.5 Comparator-checked for every depth and real
mark, the integer-mark safety chain a theorem, and **the floor F1 ≥ S2's failure** for a real-marked pair at (1/4, 1/20) kernel-checked by
a dyadic certificate — over Mathlib alone, no displayed hypothesis, the three standard axioms, replayed by nanoda". The three phrasings
the brief forbids (a failure attributed to (MI) rather than to the floor; "formalized" said of IV.17; "closed" said of the pair channel —
Theorems 4.6–4.9 of the no-go paper stay at paper grade) do not appear in this note. Label: barrier.

**Components (builder; Lean lines are my estimates from §2–§4 against the precedents' line counts).**

| # | component | new Lean, lines | what it reuses | slot |
|---|---|---|---|---|
| 1 | trusted row: \`W2\`, \`pairFormFactor\`, \`pairRow\`, \`abar\`, \`vacancyMark\`; \`W2_eq\`; the generic regrouping \`sum_W2_mul\`; the agreement lemma \`pairRow_eq_gridRowQ\` (+ \`gridRowQ_eq\` corollary) | 130–160 | \`dftMarkQ\`, \`chi\`, \`zetaM\`, \`gridRowQ\`, \`gridRowQ_eq\`; \`sum_band\`'s \`sum_nbij'\` idiom; \`Int.card_Icc\` | ¼ |
| 2 | (T1) \`sum_W2_cosh\`; \`abar n 0 = 1\`; \`1 ≤ abar n x\` (needs \`Real.one_le_cosh\`, DerivHyp import) | 60–80 | \`sum_W2_mul\`; \`Real.cosh_add\`, \`sinh_neg\`; \`Finset.sum_involution\` | ⅛ |
| 3 | Prop. 4.5 for every n, d, μ (\`prop45\`): the vacancy DFT \`φ₀\`, the residue lemma for \`|s| ≤ 2n\`, \`W2 n 0\`, the reality of the form factor at the hole, the expansion and assembly | 130–170 | \`sum_chi_mul\`, \`chi_zero\`, \`int_eq_zero_of_dvd_of_bounds\`, \`Complex.normSq_ofReal\`; items 1–2; \`Real.cosh_sq\`/\`cosh_two_mul\` — NOT Prop. 4.1's ledger | ⅜ |
| 4 | integer-mark safety chain: \`abar_sq_le\` (Cauchy–Schwarz with constant weights, \`(Σ (1/M) c_j)² ≤ (1/M) Σ c_j²\` — the Mathlib name for this form, \`Finset.inner_mul_le_norm_mul_norm\` or \`sq_sum_le_card_mul_sum_sq\`, was NOT verified this session) and the cosh² identity; \`floor_holds_integer\` by \`nlinarith\` from \`1 ≤ (m : ℝ)\` and \`1 ≤ abar\`. This chain is NEW; \`per_atom_slack\`/\`mi_holds_integer\` are atom statements and are not reused (integrality enters here as \`1 ≤ m\`, one line) | 50–70 | \`one_le_cosh\` | ⅛ |
| 5 | the certificate (Route P): two generic cosh bounds (the \`Complex.exp_bound'\` transfer to ℝ is the fiddly part), four \`decide +kernel\` power sums, the π bracket, the symbolic expansion, the final \`norm_num\`; separate module \`PairCert.lean\` with three added Mathlib imports | 120–160 | \`ZEnclosure\`'s Taylor idiom; \`pi_gt_d6\`/\`pi_lt_d6\` | ⅜ |
| 6 | Comparator packaging: \`ChallengeDeps/PairChannel.lean\` (the seven IntegralityGap definitions + five new, character for character, \`import Mathlib\`); \`Challenge/PairChannel.lean\` (seven statements: agreement, (T1), \`prop45\`, \`abar_sq_le\`, \`floor_holds_integer\`, \`floor_fails_anchor\`, \`W2_eq\`; the WHAT IS CLAIMED / NOT paragraph — nothing about (MI), Theorems 4.6–4.9, laws, general positions, ζ); \`Solution/PairChannel.lean\` (delegations); \`PrintAxioms\`, config; yaml rows, README section, formalization-status addendum. ONE topic and ONE config (the IV.17 topic carried sixteen statements in one config); two configs only if the certificate must be checkable separately, which nothing asks | 250–300 (+ yaml/README) | the IntegralityGap files as templates | ¼ |

Builder total: **1½ slots** (about 750–950 lines of new Lean; unlike D5 and IV.17, where proofs transferred word for word, here every
proof is new, and items 3 and 5 carry the risk). Clean-clone checker (the CHECK-O pattern: cold \`lake build\`, \`#print axioms\`, statement
identity, the comparator run, trust greps): **¾ slot** (IV.17's checker was 211k against the builder's 259k; here the build is larger but
the check is the same shape). **Total 2¼ slots**, range 2–2½. Against the record — D5 273k + 198k for thirteen statements; IV.17
259k + 211k, both with proofs that transferred — **the brief's 1½–2 is right for the BUILDER and low for builder plus checker;** price the
unit at 2¼ and fund it only with a fresh session for the checker (RULE ZERO).

**Stop and report when (10(m)), for the unit's brief:**
* (i) the generic regrouping \`sum_W2_mul\` is not closed after two build attempts or 120 lines — report; the fallback is the
  \`W2_eq\` + \`weight_telescoping_rat\` route (§2, alternative), which reproves Parseval instead of reusing \`gridRowQ_eq\`;
* (ii) Prop. 4.5 for general n passes 250 lines or needs any hypothesis beyond \`n : ℕ\` and \`d μ : ℝ\` — restate it at n = 32 (which
  the certificate needs) and report; the label's "every depth and real mark" survives, "every n" was never in it;
* (iii) the certificate module's build passes ten minutes (Unit B's stop (d), \`results/c2-m4/BRIEF-B.md\` item 4) — split the four power
  sums into their own module; if still over, the sign stays at paper grade and the identity ships alone (BRIEF's close-both-ways);
* (iv) the ℝ transfer of \`Complex.exp_bound'\` does not close in 60 lines — fall back to \`Real.exp_bound\` (|x| ≤ 1) with the half-angle
  step \`cosh x = 2 cosh²(x/2) − 1\` for the twelve values j = 21..32 at 2d = 1/2, or to Route T;
* (v) any statement of the topic needs a displayed hypothesis — the label's "no displayed hypothesis" clause fails; stop and report
  before the Comparator packaging;
* (vi) the builder passes 1¾ slots before the Comparator packaging starts — stop; ship the built modules with the label reduced per
  10(c) (identity Comparator-checked, sign at paper grade), and hand the packaging to the next session.

## §7 Honesty note

**Read at the line, whole or by the ranges named in \`SHARED.md\`:** the brief; the IV.17 \`TYPING-NOTE.md\` (69 lines) and \`BUILD-NOTES.md\`
§0–§2; \`pair-channel.md\` §0–§4, §7 (line 240), §10; \`paper.md\` §2.3 and §4.2; the four \`PairCeiling\` files whole (583 + 263 + 249 + 168);
the two \`IntegralityGap\` comparator files whole (77 + 140); \`ZEnclosure.lean\` whole (188); the Unit B timing lines of
\`BUILD-NOTES-B.md\`/\`CHECK-O-B.md\` by grep; the Mathlib files at the clone by the line ranges in \`SHARED.md\`. \`pairchan_identity.py\` and
\`pairchan_core.py\` were opened by grep (the \`abar\` definition and the weights, lines 4–22 of \`pairchan_core.py\`); **neither was run.**
**Probed:** one file, §5, 7.41 s, everything \`sorry\`. **Computed** (scratchpad \`h4nums.py\`, mpmath, outside the project; not a
certificate): ā(1/4), ā(1/2), F1 − S2 by the closed form, by the direct integer-frequency row, and by the mod-65-reduced row; the four
power sums; the tolerances; the crude enclosure's value. **Inferred (marked "I infer" in the text):** the proof routes and line counts
of §2–§4, the kernel-time estimates, the import-closure explanation of the six probe errors, the prices of §6, the Mathlib name for
constant-weight Cauchy–Schwarz (unverified). **Not done, by the brief:** no \`lake build\`; no theorem proved; no certificate computed;
no commit; no file written outside \`results/h4-pair-typing-s32/\` except the scratchpad script.

**Files touched:** \`results/h4-pair-typing-s32/TYPING-NOTE.md\` (this), \`SHARED.md\`, \`typing-probe.lean\`, \`typing-probe.log\`. \`BRIEF.md\`
untouched (its SHA-256 is at the top). Nothing in \`lean/\`, nothing in the clone.

**10(o).** Nothing about ζ or RH follows from anything in this note. No theorem was proved; no build was run; the one probe elaborated
statements whose proofs are \`sorry\`. The unit, if funded, earns at most the label quoted in §6, and that label is a barrier statement
about a finite-circle model row, not about ζ.

**Closing stamp: Tue Sep 29 07:20:39 IST 2026.**
