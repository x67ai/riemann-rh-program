# A4 no-go paper — formalization status (verified 2026-08-27)

**Why this file exists.** The paper's Section 10 is titled "Formalization plan" and describes the
core results of Sections 3–4 as *formalizable*, listing them in a "dependency order for the queue."
That is stale, and stale in the paper's own favor: **four of the items in that queue are already
formalized, compiled, and machine-checked**, in Lean 4 against Mathlib, with no `sorry`, no
`native_decide`, and no numeric certificates. This file records exactly what is proved, how it was
verified, and what genuinely remains — so the paper can state the true position before circulation.

**No Magma anywhere in this program.** The computational stack is Lean 4 (formal proof), Python
with mpmath/numpy/sympy (numerics and LP), and Wolfram/Mathematica (an independent instrument).
A search of every `.md`, `.tex` and `.py` in the program returns zero occurrences of Magma.

## Environment (recorded so the check is reproducible)

| Item | Value |
|---|---|
| Lean | 4.33.0-rc2, commit `d8b18978322de05a8f3dba51ef03cf5461676c17`, arm64-apple-darwin24.6.0 |
| Toolchain pin | `leanprover/lean4:v4.33.0-rc2` (`lean-toolchain`) |
| Mathlib | rev `51e6992efd06126df61a496bebf8f49482a4e129` (`lake-manifest.json`) |
| Repo copy | `anthropic/zeta-23-lean-main/` (tracked) |
| Build tree | `~/rh-lean-work/zeta-23-lean-main/` (9.2 GB, local-only, not tracked) |
| Build result | `lake build Zeta23.PairCeiling.{GridParseval,GridWitness,GridCorner}` → **Build completed successfully (2081 jobs)** |
| Source parity | all three `.lean` files byte-identical between the tracked copy and the build tree |

## What is machine-checked

Three files, all under `Zeta23/PairCeiling/`, all sorry-free:

**`GridParseval.lean`** (578 lines) — the grid Parseval machinery.
- `flat_band_trace_sq` — the flat-band identity in algebraic form, over any integral domain with a
  primitive *M*-th root of unity: **the paper's Lemma 3.8**, proved for *any* band of *M*
  consecutive integer harmonics.
- `trace_sq_grid` — the literal tr Ĝ² = Σ_k m_k² collapse on the grid: **the paper's Theorem 3.9**.
- Supporting: character orthogonality on ℤ/M, DFT Parseval in the integer-mark pairing, the band
  reindexing, and the triangular-weight telescoping.

**`GridWitness.lean`** (20,984 bytes) — the worked witness instance.
- `vacancy_F1` — the N = 64 vacancy lattice has F1 = Σ m² = 64, for **every** vacancy position.
- `vacancy_half_band_value` — the λ′ = 1/2 half-band row of that same configuration is exactly
  **F′ = 4128/33**, for every vacancy position. This is the paper's hand-checkable worked value and
  the shipped witness column (125.0909…). Its integer core, Σ_{j₁,j₂∈[−16,16]} (4096·[j₁+j₂=0] +
  [j₁+j₂≠0]) = 136224, is `decide +kernel`-checked — kernel-checked, *not* `native_decide`.
- `half_band_alive` — F′ = 4128/33 ≠ 64 = Σ m²: **the "alive" half of the paper's Proposition
  3.10**, i.e. the two-bandwidth decoupling itself, in witness form.
- `sum_band_pair_tri` / `half_band_fold` / `sum_window_residues` — the finite/algebraic half of
  Proposition 3.10's display, including that the s-window is a complete residue system mod 65 (so
  no residue-class telescoping can occur, unlike the λ = 1 band).

**`GridCorner.lean`** (13,406 bytes) — the ε-budget LP corner on the grid class.
- `mark_one_count_ge` — **the paper's Lemma 4.2**, simple-fraction level.
- `grid_corner_pointwise` — **Theorem 4.3**, pointwise on the grid: mass N, F1-row ≤ (4/3)N(1+ε)
  ⟹ N_d ≥ N(5/6 − (2/3)ε) and n₁ ≥ N(2/3 − (4/3)ε).
- `grid_corner_law` — the same in **law form** (any finitely supported law), i.e. the LP lower
  bound with no discretization.
- `grid_corner_attained` — **exact attainment** at N = 64, ε = 1/32: the marks-{1,2} configuration
  with 12 doubles and 40 simples saturates the budget (F1 = 88 = (4/3)·64·(1+1/32)) and meets
  *both* corners with equality. Column data kernel-checked.

## The axiom footprint (the check that actually matters)

`#print axioms` on each headline theorem, run under `lake env lean` against the built tree:

```
'Zeta23.PairCeiling.GridParseval.flat_band_trace_sq'   depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.PairCeiling.GridParseval.trace_sq_grid'        depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.PairCeiling.GridWitness.vacancy_F1'            depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.PairCeiling.GridWitness.vacancy_half_band_value' depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.PairCeiling.GridWitness.half_band_alive'       depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.PairCeiling.GridCorner.mark_one_count_ge'      depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.PairCeiling.GridCorner.grid_corner_pointwise'  depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.PairCeiling.GridCorner.grid_corner_law'        depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.PairCeiling.GridCorner.grid_corner_attained'   depends on axioms: [propext, Classical.choice, Quot.sound]
```

Those are the three standard axioms of Lean's classical foundation and nothing else. In
particular there is **no `sorryAx`** (which any admitted step would introduce) and **no
`Lean.ofReduceBool`** (which `native_decide` would introduce, and which would move the compiler
into the trusted base). A whole-tree scan for real `sorry`/`admit` occurrences — comments and
doc-strings stripped first — returns **zero** across all 34 `.lean` files.

## What is NOT formalized (stated honestly)

- **Proposition 3.10's closing strict position-sensitivity statement** — two grid configurations
  with the same mark multiset but different F′. Needs a cyclotomic non-vanishing certificate; the
  precise gap is documented in `GridWitness.lean`'s header. The *witness* form (`half_band_alive`)
  is proved; the *general* form is not.
- **Theorem 4.3 off the grid** — on the atom-only class at arbitrary positions. Needs the
  position-space form of Lemma 4.1 (F1 ≥ Σ m² off the grid, i.e. the row with kernel K = D² ⪰ 0).
  On the grid that step is an *equality* by `trace_sq_grid`, which is why the grid case closes.
- Everything else in Section 10's queue: Proposition 3.3 / Theorem 3.4 (polynomial identities),
  Theorem 3.5, Theorem 7.1, Theorem 7.4, Theorem 4.9, and the capacity curves (where interval
  arithmetic would enter). None started.
- The pair-channel results of Section 4.3 are Python-certified, not formalized.

## Consequence for the paper

Section 10 must be rewritten before circulation. As it stands it presents as a *plan* what is in
fact a *partial execution*, and lists as queue items four results that are done. The honest and
stronger statement is: the grid Parseval identity, the two-bandwidth decoupling in witness form,
the integrality level, and the ε-budget corner (pointwise, law-form, and with exact attainment)
are **machine-checked in Lean 4 against Mathlib**, with the axiom footprint above; the remaining
queue is the off-grid extension, the general position-sensitivity statement, and the analytic
items.

## Reproducing this check

```
export PATH="$HOME/.elan/bin:$PATH"
cd ~/rh-lean-work/zeta-23-lean-main
lake build Zeta23.PairCeiling.GridParseval Zeta23.PairCeiling.GridWitness Zeta23.PairCeiling.GridCorner
# then, for the axiom footprint, create a scratch file importing the three modules
# and `#print axioms` each theorem named above, and run:  lake env lean <file>.lean
```

A cold build (no Mathlib cache) is hours; with the existing `.lake` tree the above is a no-op
plus the axiom check.
