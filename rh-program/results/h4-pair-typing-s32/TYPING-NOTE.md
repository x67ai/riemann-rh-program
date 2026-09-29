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

