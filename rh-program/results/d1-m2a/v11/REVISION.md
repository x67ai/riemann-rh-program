# v11 REVISION — repairs applied after the independent audit (AUDIT.md, verdict REPAIRED-CLEAN-OWED)

Session 16, 2026-09-06. Repairer: Fable 5.1. One line per repair; status column updated as each lands.
None of these touches a theorem, proof, displayed hypothesis, or axiom. Build/axiom evidence appended below as it exists.

| id | file | change | status |
|----|------|--------|--------|
| R-1a | `lean/README.md` | label clause: the short "modulo H1, H2, H3" sentence is NOT licensed yet (gated on Lane A; H2 = H2-B ∧ H2-A ∧ H-TAIL) | DONE 2026-09-06 (exact single-occurrence replacement; verified count 1) |
| R-1b | `results/d1-m2a/v11/GLUE-NOTES.md` | same clause, same ruling (AUDIT.md §3) | DONE 2026-09-06 (exact single-occurrence replacement; verified count 1) |
| R-2 | `Zeta23/DBN/BarrierCert.lean` (working tree, then copy-back) | two docstrings: `Polymath15Bridge` (iii) → `Polymath15Bridge'` (iii′) | DONE 2026-09-06 (git diff: 2 insertions, 2 deletions, both docstring lines; rebuilt; copied back; `diff -rq` empty) |
| R-3 | `results/d1-m2a/SPEC.md` §14 | erratum item 6: L-B3's hypothesis is Re z ≠ 0, and it landed in `BtFacts.lean` (AUDIT.md §1.2) | DONE 2026-09-06 (exact single-occurrence replacement; verified count 1) |

## Evidence (all files in this directory; verbatim outputs)

* **Repairs declined:** none. All three owed repairs (R-1a/R-1b counted as one MEDIUM item; R-2 and R-3 LOW) applied as
  written by the auditor. R-2 was NOT deferred: the rebuild cost ~1 min wall, so the deferral option was not taken and
  no new RUN-REPORT §6 item is needed.
* **Build after R-2** (`repair-build.log`): `lake build Zeta23.DBN.Instance02` in `/Users/jaytyagi/rh-lean-work/zeta-23-lean-main`,
  one lake process, `Build completed successfully (3263 jobs)`, exit 0, 1:02.19 wall (304 s user); 116 modules rebuilt
  (BarrierCert and everything downstream, the transcript modules included, so every `decide +kernel` fact re-ran).
  No `error`, `warning` or `sorry` line in the log.
* **`#print axioms` after the rebuild** (`repair-axioms-scratch.lean` = the audit's `glue-axioms-scratch.lean`, byte-copied;
  output in `repair-axioms.log`, body byte-identical to the audit's `glue-axioms.log` by `diff`):

      'Zeta23.DBN.Instance02.lambda_le_point2' depends on axioms: [propext, Classical.choice, Quot.sound]
      'Zeta23.DBN.Instance02.lambda_le_point2_arb' depends on axioms: [propext, Classical.choice, Quot.sound]
      'Zeta23.DBN.Instance02.row2_ray_mp' depends on axioms: [propext, Classical.choice, Quot.sound]
      'Zeta23.DBN.Instance02.row2_ray_arb' depends on axioms: [propext, Classical.choice, Quot.sound]
      'Zeta23.DBN.Instance02.hHol_of_entire' depends on axioms: [propext, Classical.choice, Quot.sound]

  No `sorryAx`, no `Lean.ofReduceBool`. The `#check` shapes of `lambda_le_point2`, `lambda_le_point2_arb` and
  `row2_ray_mp` are unchanged from the audit's log (same file, same diff).
* **Copy-back:** `rsync -a --delete` of `Zeta23/DBN/` from the working tree to `lean/Zeta23/DBN/`; `diff -rq` between the
  two directories is empty (exit 0) both before the repairs began and after the copy-back. `git diff --stat` on the
  program tree shows only `lean/Zeta23/DBN/BarrierCert.lean | 4 ++--` (the two docstring lines).
* **Old name after R-2:** unprimed `Polymath15Bridge` mentions remaining in the working tree's `Zeta23/` `.lean` files:
  /Users/jaytyagi/rh-lean-work/zeta-23-lean-main/Zeta23/DBN/Defs.lean:38:  1. `Polymath15Bridge` (v1.0, the merged "canopy" form: no zeros of H_t for ALL x ≥ X,
  (The audit found three comment-only hits and no declaration; R-2 removed two of them.)

## Final label (unchanged by the repairs; the binding wording is `Instance02.lean` line 59 and `Defs.lean` line 64)

`lambda_le_point2` / `lambda_le_point2_arb` — ∀ t ≥ 1/5, every zero of H_t is real — is **kernel-checked modulo the
displayed hypotheses H1 (`hH1 : ZeroVerification (116733/200000) 2500000097429`, exact, Platt–Trudgian Theorem 1 in
prose), H2-B (`hEncl : BarrierEnclOK (Ht/Bt) row2BarrierMP` / `row2BarrierARB`, the prism transcripts kernel-checked,
producers untrusted), H2-A in conclusion form (`hLaneA`, pending the Lane A checker), and H3
(`hH3 : Polymath15Bridge' ∧ HtEntire`, the Polymath15 analytic package)**; L-B3 and `hHol` are proved, not displayed;
`#print axioms` = `[propext, Classical.choice, Quot.sound]`. Never "fully machine-checked". The shorter sentence
"Λ ≤ 0.2 in ray form, kernel-checked modulo H1, H2, H3" is NOT licensed until Lane A lands (RUN-REPORT §6 items 3–4;
SPEC §6's H2 = H2-B ∧ H2-A ∧ H-TAIL behind a kernel-checked checker, of which only H2-B exists).
