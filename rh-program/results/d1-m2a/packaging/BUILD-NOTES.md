# D1 M2a packaging — BUILD-NOTES (Session 20, queue item 1, Job 1: the builder)

**Stamp:** started 2026-09-10 (Session 20), machine clock; builder Claude Fable 5.1. Brief: `BRIEF.md` (this directory),
§0–§2 binding. Authorities read in the brief's order: `lane-a/{EMIT-NOTES,AUDIT-3d,PLAN-REVIEW §6}.md`; `SPEC.md` §1.1, §3
(§3.7), §5–§7; `RUN-REPORT.md` §6; `lean/README.md`; the parent's `comparator/README.md` ("Layout convention: one topic
per file") and the `XiPrime` topic files; `lean-repos.md` §1(d-ii), §1(e), §2; KICKSTART Part 2 items 5, 10(f), 10(i),
10(j), 11. Written as the work happens (RULE ONE); the autocommit watchdog picks it up every ten minutes.

**Label (SPEC §3.7, binding, verbatim, everywhere a label appears):** "kernel-checked modulo H1, H2 (H2-B, H2-A, H-TAIL), H3"
— never "fully machine-checked". Λ ≤ 0.2 is NOT proved; the bracket of record stays 0 ≤ Λ ≤ 0.2 on the literature.

Environment (measured at start): Lean v4.33.0-rc2, Lake 5.0.0, Mathlib 51e6992e; tree `~/rh-lean-work/zeta-23-lean-main`
(not a git repo); `caffeinate` running; both watchdogs running (`pgrep -f watchdog.sh` → 2); heavy jobs (> 50 % CPU) at
start: 0. One `lake` process at a time throughout.

## 0. Plan of record (decided before writing any Lean; the reasons are the ledger's item (f))

The comparator's trusted side must be Mathlib-only, so every structure of the statement vocabulary (`W1Row`, `W1Data`,
`PrismData`, `RectData`, `BarrierData`, `AsymRow`, `TailRow`, `AsymData`) is RE-DECLARED under `DBN.*`. Re-declared
structures are DISTINCT TYPES from Zeta23's (a `def` with an identical body is definitionally equal by unfolding; a
`structure` is not), so the solution side cannot delegate by `rfl` alone. The bridge is therefore:

1. transport maps `Solution`-side only (`DBN.W1Row.toZ`, `PrismData.toZ`, …, `AsymData.toZ`), each field-wise;
2. transport lemmas: `DBN.checkBarrier d = Zeta23.DBN.checkBarrier d.toZ`, `DBN.checkAsym a = Zeta23.DBN.checkAsym a.toZ`,
   `DBN.BarrierEnclOK G d ↔ Zeta23.DBN.BarrierEnclOK G d.toZ`, `DBN.AsymEnclOK g a ↔ …`, `DBN.TailOK g a ↔ …` (generic
   in `d`, `a`; by induction on the row/mesh lists for the recursive helpers, `rfl` for the rest);
3. the literal identities `DBN.row2BarrierMP.toZ = Zeta23.DBN.Instance02.row2BarrierMP` (etc.), which the kernel decides
   on the two literal copies (`decide +kernel` with a derived `DecidableEq`, or `rfl` — whichever elaborates; recorded below);
4. the instance statements (I) then delegate to `Zeta23.DBN.Instance02.lambda_le_point2` / `_arb` through 2 and 3;
5. the generic statements (G) delegate to a NEW generic lemma in `Solution/DBN.lean` (Zeta23 vocabulary) that repeats
   `row2_ray_mp`'s proof with `d`, `a` generic under the constraints the glue actually uses — `Zeta23` proves only the
   instance form, so (G) is a genuine consequence derived on the solution side (brief §2 item 1, (G) second clause).

The `#print axioms` verdict, the statement-identity check, the trust greps, the hashes and the owed list are in the
numbered sections below, appended as each lands.

