# Ledger row `zeta_3-5_9-10_1000_1001` (R2) -- provenance

**Box:** R = [3/5, 9/10] x [1000, 1001], delta0 = sigma1 - 1/2 = 1/10. **Grade:** box. **Status:** accepted.

**Provenance kind:** `acceptance`. M1 v1 acceptance null test 2 (cost-curve height point T = 10^3, delta0 = 1/10): instrument-validation box chosen for the cost curve, not by any prior; results/d1-m1/acceptance-report.md sec. 1, RUN-REPORT.md sec. 1.4.

**Sentence (licensed, single box):** no zeros of zeta in the closed box [3/5, 9/10] x [1000, 1001] -- kernel-checked modulo the displayed hypothesis H-ENCL (producers untrusted)

**Legs:** mp `../d1-m1/acceptance/w1-mp-null-t1000.json` (mpNullT1000, SHA-256 `a18a7bf713b802ae4c7755d3f5f7041ef5c4b256f8fa40ec8f7572aabbcf8cc0`, 81 segments) and arb `../d1-m1/acceptance/w1-arb-null-t1000.json` (arbNullT1000, SHA-256 `36b7685a5ae464c6ad5dd6d93834bf2fa44fd63b32b090163c7fcedfd7809476`, 65 segments); both Python checkers ACCEPT on both legs (re-run today); cross-check 158 overlap pairs, CONSISTENT; kernel `mpNullT1000_check`, `arbNullT1000_check` (`[propext]`, results/d1-m1/recon_lean_instances.log); corollaries `mpNullT1000_exclusion`, `arbNullT1000_exclusion` in `lean/Zeta23/W1/Ledger.lean`.

**What the negative means:** nothing new about zeta -- the box lies far below the rigorous verification record 3*10^12 (Platt-Trudgian); it is the program's own certificate in its own trust vocabulary and one of the ledger's four format-validation rows.

**Added:** 2026-09-09T22:13:35Z by Claude Fable 5.1 (Session 20, D-R8 + M3-seed build, Job 1 builder; brief results/d1-m2a/dr8/BUILD-BRIEF-fDH.md addendum).
