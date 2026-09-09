# Ledger row `zeta_3-5_9-10_10000_10001` (R3) -- provenance

**Box:** R = [3/5, 9/10] x [10000, 10001], delta0 = sigma1 - 1/2 = 1/10. **Grade:** box. **Status:** accepted.

**Provenance kind:** `acceptance`. M1 v1 acceptance null test 3 (cost-curve height point T = 10^4, delta0 = 1/10; the mp leg's 1 294 segments and 1 565 s are the recorded cost ceiling of the Euler-Maclaurin leg): instrument-validation box chosen for the cost curve, not by any prior; results/d1-m1/acceptance-report.md sec. 1, RUN-REPORT.md sec. 1.4.

**Sentence (licensed, single box):** no zeros of zeta in the closed box [3/5, 9/10] x [10000, 10001] -- kernel-checked modulo the displayed hypothesis H-ENCL (producers untrusted)

**Legs:** mp `../d1-m1/acceptance/w1-mp-null-t10000.json` (mpNullT10000, SHA-256 `007c4977f2f58052b414dcd25eacf9eeccfb8046b6cfbff39d2d232267ee3168`, 1294 segments) and arb `../d1-m1/acceptance/w1-arb-null-t10000.json` (arbNullT10000, SHA-256 `5422646bd635edf0753874a44968a9e41c66d7aa7a4c054dbab3f2c5ca7381bf`, 983 segments); both Python checkers ACCEPT on both legs (re-run today); cross-check 2547 overlap pairs, CONSISTENT; kernel `mpNullT10000_check`, `arbNullT10000_check` (`[propext]`, results/d1-m1/recon_lean_instances.log); corollaries `mpNullT10000_exclusion`, `arbNullT10000_exclusion` in `lean/Zeta23/W1/Ledger.lean`.

**What the negative means:** nothing new about zeta -- the box lies far below the rigorous verification record 3*10^12 (Platt-Trudgian); it is the program's own certificate in its own trust vocabulary and one of the ledger's four format-validation rows.

**Added:** 2026-09-09T22:14:41Z by Claude Fable 5.1 (Session 20, D-R8 + M3-seed build, Job 1 builder; brief results/d1-m2a/dr8/BUILD-BRIEF-fDH.md addendum).
