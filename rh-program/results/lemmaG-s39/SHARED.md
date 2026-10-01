# SHARED — unit `lemmaG-s39` (dated blocks, appended as results land)

## 2026-10-01 05:40 — ladder rung 1 (lemmaG-s39)
- Rung 1a (finite R), third route (dilation recursion MS(R∪{q}) = 2(1−1/q)MS(R) via the homogeneity c(qξ) = c(ξ)/q): exact in rationals
  on 12 sets + 6 cross terms, ALL EXACT (`verify/logs/rung1_finite.log`).
- Rung 1b (F_q[T], RH true): **the degree-wise Conjecture O is FALSE** — deleting M(a,N) (necklace number) irreducibles of each degree N
  gives D_R(u) = 1 − au and E_R(n) ≡ 0 with α_R = log a/log q. Brute force in F_3[T] (degrees ≤ 8) and exact generating functions (≤ 60)
  confirm; regular (round(a^N/N)) and random deletions on the same rung sit at a^{n/2} (`verify/logs/rung1_ff.log`).
- Consequence being written up: any proof of O / Lemma G must use a property of ℚ absent in F_q[T] (injectivity of the norm on ⟨R⟩).
## 2026-10-01 06:05 — rung-1 consequence + instrument built (lemmaG-s39)
- NOTE §1.3 (G₁): Lemma G and O fail at rung 1 (necklace deletion); every input of Theorem Z's proof except zero-freeness of D_R
  holds there; a proof over ℚ must use injectivity of the norm on ⟨R⟩ (±1 coefficients of D_R, no aggregation).
- Instrument `verify/lg.c` (+ `lg_core.h`): families sq (nextprime(p²)), nsq (nextprime(n²)), weyl ({p√2} < p^{α−1}), neck
  (necklace clusters at 4^N, tight/spread), planted (greedy with a planted pole of D_R at 0.45 ± 5i, α = 0.6). Second route
  (`xcheck_small.py`, `xcheck_planted.py`): R-lists regenerated in Python equal; every bin's sumE2 recomputed by inclusion–exclusion
  over R-numbers agrees to print precision (≤ 5e−7); ρ(sq), ρ(nsq) by independent products agree to 3e−12, 3e−15.
- 1e9 batch launched 05:30 (`verify/run_all.sh`, log `verify/logs/run_all.log`).
