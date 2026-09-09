# Ledger row `zeta_3-5_9-10_100_101` (R1) -- provenance

**Box:** R = [3/5, 9/10] x [100, 101], delta0 = sigma1 - 1/2 = 1/10. **Grade:** box. **Status:** accepted.

**Provenance kind:** `acceptance`. M1 v1 acceptance null test 1 (cost-curve height point T = 10^2, delta0 = 1/10): instrument-validation box chosen for the cost curve, not by any prior; results/d1-m1/acceptance-report.md sec. 1, RUN-REPORT.md sec. 1.4.

**Sentence (licensed, single box):** no zeros of zeta in the closed box [3/5, 9/10] x [100, 101] -- kernel-checked modulo the displayed hypothesis H-ENCL (producers untrusted)

**Legs:** mp `../d1-m1/acceptance/w1-mp-null-t100.json` (mpNullT100, SHA-256 `17f06458036b6df1a23e6406f409b5802757e776c376474e11900d81cba13212`, 52 segments) and arb `../d1-m1/acceptance/w1-arb-null-t100.json` (arbNullT100, SHA-256 `3248f7ca4a0160d5369bf61c8ac367ab95591e2bf5bd995b998878369e1899d5`, 27 segments); both Python checkers ACCEPT on both legs (re-run today); cross-check 83 overlap pairs, CONSISTENT; kernel `mpNullT100_check`, `arbNullT100_check` (`[propext]`, results/d1-m1/recon_lean_instances.log); corollaries `mpNullT100_exclusion`, `arbNullT100_exclusion` in `lean/Zeta23/W1/Ledger.lean`.

**What the negative means:** nothing new about zeta -- the box lies far below the rigorous verification record 3*10^12 (Platt-Trudgian); it is the program's own certificate in its own trust vocabulary and one of the ledger's four format-validation rows.

**Added:** 2026-09-09T22:13:35Z by Claude Fable 5.1 (Session 20, D-R8 + M3-seed build, Job 1 builder; brief results/d1-m2a/dr8/BUILD-BRIEF-fDH.md addendum).
