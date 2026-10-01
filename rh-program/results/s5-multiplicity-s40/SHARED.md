# SHARED — unit `s5-multiplicity-s40` (dated blocks, appended as work lands)

## 11:25 IST 2026-10-01 — block 1: start
Read BRIEF.md in full; read u-offsurgery-s39 NOTE.md (§2, §4, all), READ-O-SUPPLEMENT.md §C, verify-F/ (s5gen_F.c, factor_count.py,
ascent.py, anatomy_records.py, zero_taylor_F.log), the 1e9 generation log on /private/tmp/rh-s40-shared/s5/. Load at start: 3 heavy
processes (other agents) — under the limit of 4. Plan: task 1 (exact reproduction, own generator as second code path), task 2 (exact
counter in C with 128-bit counts, smarter search), task 4 (structure theorems), task 5 (carrier model), task 3 (extension, priced), task 6.

## 11:34 IST 2026-10-01 — block 2: task 1 done (C1, C3 reproduced exactly)
gp list SHA-256 matches; dump scan (`verify/dump_records.c`): sup E = 274.8 at 902538000 (a = 276, E(n−1) = −0.4), inf E = −0.4,
54% of n ≤ 10⁹ have a_n = 0. Exact counter `verify/fcount.c` (128-bit): self-tests 276/26 pass; C3 exact: 20390; 2932627 (the
20.20 integer, re-found by rerunning the orchestrator's greedy over primes ≤ 47); 13461378553. Second path (orchestrator's
Python-int DP) agrees on the two smaller. NOTE §1 written. Running: greedy ascent over the first 25 primes (full DP, double),
`logs/search_greedy_K25.log` — already exponent 0.3535 at log₁₀n = 33.4 (excess vs 3.76n^0.35: −0.46 in log₁₀), rates ≈ 0.39.
Finding: the one-large-prime split counter (`verify/fsplit.c`) loses a factor 4.7–150 — multi-large-prime g-primes matter.
