# v11 REVISION — repairs applied after the independent audit (AUDIT.md, verdict REPAIRED-CLEAN-OWED)

Session 16, 2026-09-06. Repairer: Fable 5.1. One line per repair; status column updated as each lands.
None of these touches a theorem, proof, displayed hypothesis, or axiom. Build/axiom evidence appended below as it exists.

| id | file | change | status |
|----|------|--------|--------|
| R-1a | `lean/README.md` | label clause: the short "modulo H1, H2, H3" sentence is NOT licensed yet (gated on Lane A; H2 = H2-B ∧ H2-A ∧ H-TAIL) | DONE 2026-09-06 (exact single-occurrence replacement; verified count 1) |
| R-1b | `results/d1-m2a/v11/GLUE-NOTES.md` | same clause, same ruling (AUDIT.md §3) | DONE 2026-09-06 (exact single-occurrence replacement; verified count 1) |
| R-2 | `Zeta23/DBN/BarrierCert.lean` (working tree, then copy-back) | two docstrings: `Polymath15Bridge` (iii) → `Polymath15Bridge'` (iii′) | IN PROGRESS |
| R-3 | `results/d1-m2a/SPEC.md` §14 | erratum item 6: L-B3's hypothesis is Re z ≠ 0, and it landed in `BtFacts.lean` (AUDIT.md §1.2) | DONE 2026-09-06 (exact single-occurrence replacement; verified count 1) |
