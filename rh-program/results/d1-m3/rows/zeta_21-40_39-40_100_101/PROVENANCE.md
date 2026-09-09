# Ledger row `zeta_21-40_39-40_100_101` (R4) -- provenance

**Box:** R = [21/40, 39/40] x [100, 101], delta0 = sigma1 - 1/2 = 1/40. **Grade:** box. **Status:** accepted.

**Provenance kind:** `acceptance`. M1 v1 acceptance null test 4 (depth point T = 10^2, delta0 = 1/40 -- the deep box): instrument-validation box chosen for the cost curve's depth axis, not by any prior; results/d1-m1/acceptance-report.md sec. 1, RUN-REPORT.md sec. 1.4.

**Sentence (licensed, single box):** no zeros of zeta in the closed box [21/40, 39/40] x [100, 101] -- kernel-checked modulo the displayed hypothesis H-ENCL (producers untrusted)

**Legs:** mp `../d1-m1/acceptance/w1-mp-null-deep-t100.json` (mpNullDeepT100, SHA-256 `2faaec2e251a1451a0f5a5e2257b39b9d4e2bd12c78b6d69c142baa5c3249f59`, 58 segments) and arb `../d1-m1/acceptance/w1-arb-null-deep-t100.json` (arbNullDeepT100, SHA-256 `53cc7897dee89a4f9cbb740eb322e7bd787fdbe9b0cad4d184453f9a8d75ba27`, 30 segments); both Python checkers ACCEPT on both legs (re-run today); cross-check 90 overlap pairs, CONSISTENT; kernel `mpNullDeepT100_check`, `arbNullDeepT100_check` (`[propext]`, results/d1-m1/recon_lean_instances.log); corollaries `mpNullDeepT100_exclusion`, `arbNullDeepT100_exclusion` in `lean/Zeta23/W1/Ledger.lean`.

**What the negative means:** nothing new about zeta -- the box lies far below the rigorous verification record 3*10^12 (Platt-Trudgian); it is the program's own certificate in its own trust vocabulary and one of the ledger's four format-validation rows.

**Added:** 2026-09-09T22:14:41Z by Claude Fable 5.1 (Session 20, D-R8 + M3-seed build, Job 1 builder; brief results/d1-m2a/dr8/BUILD-BRIEF-fDH.md addendum).
