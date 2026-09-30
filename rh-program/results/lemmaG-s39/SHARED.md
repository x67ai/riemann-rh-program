# SHARED — unit `lemmaG-s39` (dated blocks, appended as results land)

## 2026-10-01 05:40 — ladder rung 1 (lemmaG-s39)
- Rung 1a (finite R), third route (dilation recursion MS(R∪{q}) = 2(1−1/q)MS(R) via the homogeneity c(qξ) = c(ξ)/q): exact in rationals
  on 12 sets + 6 cross terms, ALL EXACT (`verify/logs/rung1_finite.log`).
- Rung 1b (F_q[T], RH true): **the degree-wise Conjecture O is FALSE** — deleting M(a,N) (necklace number) irreducibles of each degree N
  gives D_R(u) = 1 − au and E_R(n) ≡ 0 with α_R = log a/log q. Brute force in F_3[T] (degrees ≤ 8) and exact generating functions (≤ 60)
  confirm; regular (round(a^N/N)) and random deletions on the same rung sit at a^{n/2} (`verify/logs/rung1_ff.log`).
- Consequence being written up: any proof of O / Lemma G must use a property of ℚ absent in F_q[T] (injectivity of the norm on ⟨R⟩).
