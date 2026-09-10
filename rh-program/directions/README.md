# directions/ — one living document per research direction

Created when Phase 3 design results land; maintained for the life of the program (months).

File naming: `A1-break-bandwidth.md`, `A2-richer-functionals.md`, `A3-families-derivatives.md`, `A4-lindelof-lock.md`, `B1-mult-positivity.md`, `B2-refutation-program.md`, `B3-arithmetic-debranges.md`, `B4-zero-dynamics.md`, `C1-requirements-first-field.md`, `C2-rigidity-conservation.md` — plus new files for directions born later (number them D1, D2, … or descriptive names; record birth in LOG.md).

Each file is the direction's complete state and must be self-sufficient for a cold restart:

```
# <ID>: <Title>
**Status:** proposed | verified-viable | active | blocked | refuted | absorbed-into-<ID> | dormant
**Track:** A (advance machinery) | B (new machinery) | C (new field)
**Last touched:** date

## Proposal (from Phase 3, immutable)
thesis / mechanism / novelty / obstruction-evasion / first theorem / milestones / lean hook / numerics / payoff / failure modes / designer confidence

## Verification verdicts (Phase 4)
critic findings, scores, surviving form of the proposal

## Work log (append-only)
dated entries: attempts, partial results, numerics run, proofs sketched/checked/failed, Lean progress

## Current frontier
the exact statement currently being attacked; what is blocking; next concrete action

## Dependencies / cross-links
inputs from other directions; shared instruments (ceiling LP, barrier zoo, Lean seams)
```

Discipline: when a direction is refuted or absorbed, do NOT delete the file — set status, record the refutation argument (refutations are load-bearing results for this program), and cross-link. The set of refuted directions with reasons is itself a primary output (cf. the zeta-campaign transcript's ~30 refuted routes, which seeded this program).


**Template amendment 2026-09-10 (Session 21; KICKSTART 10(k) and 10(m)).** Every direction file gains two sections, placed before "Current frontier": `## Instruments` — a table (quantity | current best value | result file | dated), recording, never ranking; and `## Untried` — ideas not yet attempted, each with its S1–S5 fit reason and its first ladder rung; an idea leaves only into a result file or a zoo entry. The next consolidation agent (10(a)) populates both for every live direction from the record; until then a direction file without them is not defective, only unpopulated.
