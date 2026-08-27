# Referee record — the 2026-08-27 dated revision (CIRCULATION-PREP step 1c)

**Scope:** the applied dated revision of `pair-channel.md` + `paper.md` (edit list:
`o1-n128-report.md` section 5), checked adversarially against the ground-truth certificates
(`verify/o1_crowding_interval_out.json`, `verify/n128_rerun_out.json`,
`verify/crowd_at_sliver_out.txt`). Two independent referee agents (workflow wf_029660e9-d56,
2026-08-27), one per file, cross-checking consistency with `theorems.md` (deliberately unedited).

**Verdict: PASS-WITH-REPAIRS — zero fatals; 3 distinct majors + 8 minors, ALL EXECUTED
same-day.** The revision's substance (re-scoping to w <= 0.98 certified / sliver failure
certified / attacks + backstop coverage) was confirmed correct against the certificates in every
finding; every defect was in wording, rounding, or unrevised surroundings.

## Majors (all repaired)

1. **Mis-rounded lower bound `+17.47`** (both files + the report's own sections 1/5, whence it
   propagated): the certified sliver-attack minimum is +17.4663 (d = 0.158 leg,
   `crowd_at_sliver_out.txt`), so a quoted floor of +17.47 was false by 0.0037 — a lower bound
   rounded UP, including inside Theorem 4.7. Repair: `>= +17.46` everywhere (and `(+17.5, ...)`
   in O1 likewise); correction note appended to `o1-n128-report.md`; its section-4 exact values
   were always correct.
2. **Unrevised proof-sketch tail of B(ii)** (`pair-channel.md`): still called the per-cell joint
   optimization "missing" and certified "by direct adversarial computation instead", and closed
   "proved modulo one certified constant" — contradicting the revision (the optimization was
   executed: certified on (0, 0.156]^2, certifiedly unattainable at the full family). Repair:
   tail rewritten — granted item is the one-pair-per-cell cap on (0.13, 0.156]; ledger constant
   interval-certified; sliver re-run cited.
3. **Stale Section 8.2 parenthetical** (`paper.md`): claimed the N = 128 re-run "was not run"
   seven lines above the updated O4 saying it was. Repair: rewritten to the executed re-run.

## Minors (all repaired)

4. Two-argument `Sgen2(d, d')` now defined at the ledger condition (was used undefined).
5. `Phi_0` definition restored at first use (edit 5 had removed the only defining expression).
6. Sliver re-run provenance added: Section 7 scripts line + Section 10 file list now cite
   `crowd_at_sliver.py` -> `crowd_at_sliver_out.txt` (and the two other Session-8 scripts).
7. N = 128 drift claim scoped to headline constants (deep-tail table values drift up to ~8%:
   nu(2.0) 8.2%), in both files' O4 and the report.
8. Section 0 consequence sentence restructured so the corner claim explicitly excludes the
   (0.98, 1] sliver class (the inserted exception had broken the em-dash parse).
9. Section 4.3 residue clause now attributes the sliver's coverage to the re-run attacks under
   (O1), not converged pricing (O2).
10. Section 4.3 title qualified: "closed on the R5 family (multi-pair to w <= 0.98)".
11. (+ the paper-side duplicates of 1, counted once above.)

**Post-repair state:** `grep +17.47` hits only the report's correction note (which names the old
string); no live full-family ledger claim outside historical/annotated context; both files'
dated-revision blocks agree with the certificates. The package is wording-final for LaTeX
conversion.
