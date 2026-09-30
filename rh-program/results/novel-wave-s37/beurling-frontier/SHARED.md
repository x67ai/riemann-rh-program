# SHARED.md — seed M1b `beurling-frontier` (NOVEL-APPROACH WAVE 2, Session 37)

Dated blocks, appended after each batch. Newest at the bottom.

## 2026-09-30 — block 0: start

- Charter read (§0, seed M1b brief, rules). Zoo I.2 read: it records "(b) [α,β]-systems (BDR 2309.01567): populated
  unconditionally for all α ∈ [0,1), β ∈ [1/2,1); hard wall max{α,β} ≥ 1/2; β < 1/2 only under RH" — to be checked at the page.
- On disk (found by listing `fetched*/`): z-02 = Broucke–Debruyne–Révész 2025 "well-behaved Beurling number systems" (the
  published 2309.01567?), z-18 = Broucke–Vindas 2024 "generalized prime random approximation" (2102.08478?), z-01 = BDV 2020,
  w-18a Hilberdink 2005, p3-22c1 Hilberdink–Lapidus, p3-22c2 Hilberdink 2012 periodic, p1-02 DMV, t-50 Diamond–Zhang book.
- Plan: (1) prior art at the page -> sources/*.txt + NOTE.md §1; (2) pre-derivation attack; (3) simulation; (4) frontier; (5) close.

## 2026-09-30 — block 1: prior art done (NOTE §1) + logical frame (NOTE §2)

- **Region {α > ½, β < ½} is populated in print, conditionally on RH**: BDR arXiv:2309.01567v2 Theorem 1.3 (p. 4, line 183):
  "Assume RH. ... an [α, β]-system for 1/2 < α < 2/3 and 2α/(α + 2) ≤ β < 1/2." RH is used (i) for sharp α and (ii) because the
  deleted primes are actual primes, so log ζ_S(s) ≈ log ζ(s+1−α) carries ζ's zeros. Exponent 2α/(α+2) = hyperbola method;
  BDR Remark 5.3(2) says a better integer analysis "might give rise to a larger region".
- Unconditional, non-constructive: the region is populated anyway (if RH fails, (P, N) is [Θ, 0]) — Prop. 2.1. Any valid threshold
  β* has β* ≤ 2/5 and implies RH (Cor. 2.2). Obstructions β ≥ f(α) > 0 over all systems imply "no Θ in (½, a)" (Prop. 2.3).
- Hilberdink 2012 (p3-22c2): periodic N(x) − cx forces ζ_P = ζ × finite Euler product — rigidity at β = 0 in the periodic class.
- arXiv sweep since Jun 2024: nothing on β < ½.
- Next: §3 attack on the pre-derivation (it is BDR §5's construction with a claimed sharper integer analysis).
