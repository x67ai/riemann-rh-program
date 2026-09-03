# AxiomMath/ZetaZeros — independent build and axiom check (2026-09-03, Session 15)

- Repo: https://github.com/AxiomMath/ZetaZeros, commit `4bcaf70e544506c311d83a5a5b143a134b9fc5f7` (2 commits: "Publication of Files", "feat: remove an assumption (#1)").
- Toolchain: `leanprover/lean4:v4.34.0-rc2`; Mathlib `v4.34.0-rc2` (rev `85e3a25e006c35636f0e53b0e9296caca2685bc0`), oleans from `lake exe cache get`.
- Machine: the sponsor's MacBook (darwin arm64); local clone `~/rh-lean-work/zetazeros`; script `~/rh-lean-work/build-zetazeros.sh`; full log `~/rh-lean-work/zetazeros-build.log` (local-only).
- Wall clock: 15:39 → 15:45 IST, of which the toolchain download and the Mathlib cache fetch took ~5 minutes; the repository's own 32 modules (7,245 lines) built in ~35 s.

| Step | Result |
|---|---|
| `lake build ZetaZeros` | Build completed successfully (3634 jobs), exit 0 |
| `lake build Challenge Solution` | Build completed successfully (3637 jobs), exit 0; six "declaration uses `sorry`" warnings, all in `Challenge/Basic.lean` — the statement-only challenge file, by design |
| `#print axioms` on the six theorems as discharged by `Solution` | each `[propext, Classical.choice, Quot.sound]`; no `sorryAx`, no `Lean.ofReduceBool` |

Sorry / admit / native_decide / ofReduceBool scan over the repository's own sources (everything under `.lake/` is Mathlib and its dependencies, excluded):
    ./Challenge/Basic.lean:154:  sorry
    ./Challenge/Basic.lean:164:  sorry
    ./Challenge/Basic.lean:173:  sorry
    ./Challenge/Basic.lean:181:  sorry
    ./Challenge/Basic.lean:187:  sorry
    ./Challenge/Basic.lean:193:  sorry
    (Challenge/Basic.lean's six sorry lines are the challenge statements; no other match.)

Not run: `leanprover/comparator` (the README's Linux tool). The steps above reproduce what it certifies — the challenge statements are discharged using only the whitelisted axioms — except its independent kernel re-check (nanoda).

**Honest label if the program ever cites this repository:** *kernel-checked in Lean 4 (standard axioms only); Proposition 2.1 of Lamzouri unconditional; the zeta theorems modulo the two displayed hypotheses `RiemannVonMangoldt` and `PairCorrelation` (BGSTB24 Lemma 5), which are assumed as Props, not proved.* Statement faithfulness (Lean definitions versus the paper's) was NOT audited in this FYI session; the honest label must say so until it is.
