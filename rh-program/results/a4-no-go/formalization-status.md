# Formalization record for the absorption paper (checked 2026-08-27)

**What this file is.** The record behind Section 10, "Formalization: what is machine-checked, and
what remains," of the paper *The two-moment certificate is robust under Rudnick–Sarnak-range cubic
augmentation with capacity control* (source at `rh-program/results/arxiv/a4-no-go/main.tex`). That
section states that the core results of Sections 3–4 are **formalized, compiled, and
machine-checked** in Lean 4 against Mathlib, with no `sorry`, no `native_decide`, and no numeric
certificates. This file is the evidence for that claim: it records exactly what is proved, in which
file, in what environment, with what axiom footprint, and what genuinely remains unformalized.

**The computational stack.** Lean 4 (formal proof), Python with mpmath/numpy/sympy (numerics and
linear programming), and Wolfram/Mathematica (an independent instrument). Nothing else enters: in
particular no Magma computation is used at any point in this work.

## Environment (recorded so the check is reproducible)

| Item | Value |
|---|---|
| Lean | 4.33.0-rc2, commit `d8b18978322de05a8f3dba51ef03cf5461676c17`, arm64-apple-darwin24.6.0 |
| Toolchain pin | `leanprover/lean4:v4.33.0-rc2` (from the `lean-toolchain` of the Zeta23 checkout named below) |
| Mathlib | rev `51e6992efd06126df61a496bebf8f49482a4e129` (from that checkout's `lake-manifest.json`) |
| Files in this repository | `rh-program/lean/Zeta23/PairCeiling/{GridParseval,GridWitness,GridCorner}.lean` |
| Library they extend | Zeta23, the Lean 4 companion artifact to arXiv:2608.13637, at <https://github.com/anthropics/zeta-23-lean>; cited, not redistributed here (see `rh-program/lean/README.md`) |
| Build tree | a local checkout of that library with the three files above copied into it; 9.2 GB once Mathlib is built, and not part of this repository |
| Build result | `lake build Zeta23.PairCeiling.{GridParseval,GridWitness,GridCorner}` → **Build completed successfully (2081 jobs)** |
| Source parity | the three `.lean` files in this repository agree with the build tree's copies except in the copyright header comment block; the Lean content is identical |

## What is machine-checked

Three files, all under `rh-program/lean/Zeta23/PairCeiling/`, all sorry-free:

**`GridParseval.lean`** (583 lines) — the grid Parseval machinery.
- `flat_band_trace_sq` — the flat-band identity in algebraic form, over any integral domain with a
  primitive *M*-th root of unity: **the paper's Lemma 3.8**, proved for *any* band of *M*
  consecutive integer harmonics.
- `trace_sq_grid` — the literal tr Ĝ² = Σ_k m_k² collapse on the grid: **the paper's Theorem 3.9**.
- Supporting: character orthogonality on ℤ/M, DFT Parseval in the integer-mark pairing, the band
  reindexing, and the triangular-weight telescoping.

**`GridWitness.lean`** (402 lines) — the worked witness instance.
- `vacancy_F1` — the N = 64 vacancy lattice has F1 = Σ m² = 64, for **every** vacancy position.
- `vacancy_half_band_value` — the λ′ = 1/2 half-band row of that same configuration is exactly
  **F′ = 4128/33**, for every vacancy position. This is the hand-checkable worked value of the paper's Section 3.4 and its witness
  column (125.0909…). Its integer core, Σ_{j₁,j₂∈[−16,16]} (4096·[j₁+j₂=0] +
  [j₁+j₂≠0]) = 136224, is `decide +kernel`-checked — kernel-checked, *not* `native_decide`.
- `half_band_alive` — F′ = 4128/33 ≠ 64 = Σ m²: **the "alive" half of the paper's Proposition
  3.10**, i.e. the two-bandwidth decoupling itself, in witness form.
- `sum_band_pair_tri` / `half_band_fold` / `sum_window_residues` — the finite/algebraic half of
  Proposition 3.10's display, including that the s-window is a complete residue system mod 65 (so
  no residue-class telescoping can occur, unlike the λ = 1 band).

**`GridCorner.lean`** (263 lines) — the ε-budget LP corner on the grid class.
- `mark_one_count_ge` — **the paper's Lemma 4.2**, simple-fraction level.
- `grid_corner_pointwise` — **Theorem 4.3**, pointwise on the grid: mass N, F1-row ≤ (4/3)N(1+ε)
  ⟹ N_d ≥ N(5/6 − (2/3)ε) and n₁ ≥ N(2/3 − (4/3)ε).
- `grid_corner_law` — the same in **law form** (any finitely supported law), i.e. the LP lower
  bound with no discretization.
- `grid_corner_attained` — **exact attainment** at N = 64, ε = 1/32: the marks-{1,2} configuration
  with 12 doubles and 40 simples saturates the budget (F1 = 88 = (4/3)·64·(1+1/32)) and meets
  *both* corners with equality. Column data kernel-checked.

## The axiom footprint (the check that actually matters)

`#print axioms` on each of the twelve machine-checked theorems named above, run with `lake env lean`
against the built tree:

```
'Zeta23.PairCeiling.GridParseval.flat_band_trace_sq'   depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.PairCeiling.GridParseval.trace_sq_grid'        depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.PairCeiling.GridWitness.vacancy_F1'            depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.PairCeiling.GridWitness.vacancy_half_band_value' depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.PairCeiling.GridWitness.half_band_alive'       depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.PairCeiling.GridWitness.sum_band_pair_tri'     depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.PairCeiling.GridWitness.half_band_fold'        depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.PairCeiling.GridWitness.sum_window_residues'   depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.PairCeiling.GridCorner.mark_one_count_ge'      depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.PairCeiling.GridCorner.grid_corner_pointwise'  depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.PairCeiling.GridCorner.grid_corner_law'        depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.PairCeiling.GridCorner.grid_corner_attained'   depends on axioms: [propext, Classical.choice, Quot.sound]
```

Those are the three standard axioms of Lean's classical foundation and nothing else. In
particular there is **no `sorryAx`** (which any admitted step would introduce) and **no
`Lean.ofReduceBool`** (which `native_decide` would introduce, and which would move the compiler
into the trusted base). A scan for real `sorry`/`admit` occurrences — comments and
doc-strings stripped first — returns **zero** across all eight `.lean` files of this development
(`rh-program/lean/Zeta23/`). The axiom check above already covers everything imported as well: an
admitted step anywhere in the dependency graph would surface as `sorryAx`.

## What is NOT formalized (stated honestly)

- **Proposition 3.10's closing strict position-sensitivity statement** — two grid configurations
  with the same mark multiset but different F′. Needs a cyclotomic non-vanishing certificate; the
  precise gap is documented in `GridWitness.lean`'s header. The *witness* form (`half_band_alive`)
  is proved; the *general* form is not.
- **Theorem 4.3 off the grid** — on the atom-only class at arbitrary positions. Needs the
  position-space form of Lemma 4.1 (F1 ≥ Σ m² off the grid, i.e. the row with kernel K = D² ⪰ 0).
  On the grid that step is an *equality* by `trace_sq_grid`, which is why the grid case closes.
- The other items the paper's Section 10 lists as not yet formalized: Proposition 3.3 / Theorem 3.4 (polynomial identities),
  Theorem 3.5, Theorem 7.1, Theorem 7.4, Theorem 4.9, and the capacity curves (where interval
  arithmetic would enter). None started.
- The pair-channel results of Section 4.3 are Python-certified, not formalized.

## What this amounts to

The position recorded here is not a plan but a partial execution: the grid Parseval identity, the
two-bandwidth decoupling in witness form,
the integrality level, and the ε-budget corner (pointwise, law-form, and with exact attainment)
are **machine-checked in Lean 4 against Mathlib**, with the axiom footprint above; what remains is the off-grid extension, the general position-sensitivity statement, and the analytic
items.

## Reproducing this check

```
# 1. Get the library these files extend; it is cited here, not redistributed.
git clone https://github.com/anthropics/zeta-23-lean
cd zeta-23-lean

# 2. Copy this repository's Lean subtree in, preserving paths.
cp -R /path/to/riemann-rh-program/rh-program/lean/Zeta23/. Zeta23/

# 3. Build. elan installs the pinned toolchain from lean-toolchain;
#    `lake exe cache get` fetches prebuilt Mathlib.
export PATH="$HOME/.elan/bin:$PATH"
lake exe cache get
lake build Zeta23.PairCeiling.GridParseval Zeta23.PairCeiling.GridWitness Zeta23.PairCeiling.GridCorner

# 4. Axiom footprint: write a file that imports the three modules and carries one
#    `#print axioms <name>` line per theorem in the block above, then run it.
lake env lean axioms.lean
```

A cold build without the Mathlib cache takes hours; with `lake exe cache get` it is a download plus
this development's own compilation, and against an already built `.lake` tree steps 3 and 4 are a
no-op plus the axiom check.

## Addendum (dated 2026-09-29, Session 30, G8 — never an edit of the 2026-08-27 record above): the integrality level over ℚ

Two further modules extend the development above, in `rh-program/lean/Zeta23/PairCeiling/`, packaged as the Comparator topic
`IntegralityGap` (`lean/comparator/{ChallengeDeps,Challenge,Solution,PrintAxioms}/IntegralityGap.lean`, `config-integrality-gap.json`;
build record `results/iv17-lean-s30/BUILD-NOTES.md`, ledger `FIDELITY.md`, typing check `TYPING-NOTE.md`):

- `GridParsevalRat.lean` — the grid Parseval identity of `GridParseval.lean` (Theorem 1.2 above) with RATIONAL marks: the Parseval
  algebra proved once for a general coefficient vector `dftVec` over the same commutative domain, rational marks `dftMarkQ` (over a
  field) and integer marks `dftMark` as its instances; `trace_sq_grid_rat`, `gridRowQ`, `gridRowQ_eq`, and `gridRow_eq_gridRowQ`
  (the integer row is the rational row of the cast marks — one and the same row).
- `GridGap.lean` — the integrality level as a theorem AND a falsehood: `per_atom_slack : ∀ m : ℤ, 0 ≤ (m − 1)(m − 2)` (Lemma 2.2(a)'s
  per-atom line, the second integrality level of the Remark above; false over ℚ at 4/3, `per_atom_slack_fails_rational`);
  `per_atom_floor : ∀ m : ℤ, m ≤ m²` (false over ℚ at 1/2); `mi_holds_integer` (= `two_mul_distinct_ge`); the paper's §2.4 instance
  `fracMark` (48 atoms of mark 4/3 on the 65-site grid; mass 64, Σm² = 256/3, N_d = 48, row = (4/3)·64 — kernel-checked by
  `decide +kernel`); `mi_fails_rational` — the master inequality stated for nonnegative rational marks on `ZMod 65` is FALSE; and
  `corner_fails_rational`, `corner_bound_fails_rational` — the 5/6 corner (Theorem 2.3's first conclusion at N = 64, ε = 0) is false
  for fractional marks on the grid.

Axiom footprint of every new name (`results/iv17-lean-s30/print-axioms.log`): `[propext, Classical.choice, Quot.sound]` — no
`sorryAx`, no `Lean.ofReduceBool`; the Comparator run with nanoda on the sixteen topic statements passed
(`results/iv17-lean-s30/comparator.log`). Still NOT formalized: the pair channel (Section 4.3, Prop. 4.5), the law form of the
negation, anything off the grid; the list in "What is NOT formalized" above is otherwise unchanged. Label, verbatim: "IV.17's master
inequality is a Comparator-checked theorem over integer marks and a Comparator-checked FALSEHOOD over rational marks on the same
Frobenius row (the mark-4/3 instance kernel-checked), over Mathlib alone, no displayed hypothesis, axioms
propext/Classical.choice/Quot.sound, replayed by nanoda".

**[CORRECTION 01:22 IST 2026-09-29, Session 30 — CHECK-O F1 of `results/iv17-lean-s30/CHECK-O.md`.]** In the 2026-09-29 addendum above, "mass 64, Σm² = 256/3, N_d = 48, row = (4/3)·64 — kernel-checked by `decide +kernel`" is to be read: the first three facts are kernel-checked by `decide +kernel`; the row is proved by rational Parseval (`gridRowQ_eq`) plus `fracMark_sq`. The 2026-08-27 record above the addendum is untouched.
