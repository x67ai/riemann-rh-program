# SHARED — unit `qcond-s38` (Q_cond: Beurling system with Riemann's exact FE at conductor q > 1)

Append-only, dated blocks. Writer: Opus 5.5 (unit agent). Outputs only under `results/qcond-s38/`.

## 2026-10-01 02:22 IST — START
- Read: BRIEF.md; `novel-wave-s37/beurling-fe/NOTE.md` (whole), `read-F.md`, `read-O.md`.
- Digest `novel-wave-s37/insights-digest.md`: NOT on disk at start (re-check before the close).
- Plan: NOTE.md built section by section (§0 question; §1 task 1 self-dual measures with a gap; §2 task 2 Euler-side
  constraints + decision; §3 rung-1 dictionary; §4 close). Every computation a script in `verify/` with its log.
- First idea on the table (to be proved in the NOTE, not load until written): (a) positive-definiteness of
  eta -> mu({eta}) for a positive self-dual measure (Bohr means = atoms) gives bounded multiplicities c(n) <= rho_q;
  (b) in the uniformly discrete case Lev-Olevskii + Hilberdink pigeonhole put all generalized integers in N, the
  coefficients become q-periodic, and a Landau (Pringsheim) argument on the q-part of the Euler product should
  exclude every conductor q > 1. To be checked at the line, with the periodic-coefficient step sourced.

## 2026-10-01 02:55 IST — batch 1 (task 1) landed
- NOTE §1.1–§1.4 written: the class 𝓜_r; examples (Poisson pairs π_a, the q = 4 example = π_{1/2}, F_{5,5} = π_{1/5} + (5/2)π_1,
  twisted combs); printed theorems Q1–Q7 quoted at the line; Lemma B (Bohr means = atoms), Lemma PD, Cor. 1 (masses ≤ ρ,
  equality ⟹ periodic atoms), Cor. 2 (window bound Σc² ≤ ρ² for atoms within length < r), Cor. 3 (ρ < 1.366 + masses ≥ 1 ⟹ lattice).
- verify/v1_selfdual_examples.{py,log}: all examples self-dual (Gauss 1e−40; Fejér within explicit ξ^{-2} tail bounds).
- New sources [here]: arxiv-0807.0783 (Saias–Weingartner 2009; Thm 1, Thm 4 at lines 62–64, 104–110), arxiv-1512.08735
  (Lev–Olevskii 2017). Query logs in sources/arxiv-queries/.
- Caveat recorded: Meyer's 1970 finite-mass theorem is on disk only as quoted by Kurasov–Sarnak (secondary).
- Next: §2 (Euler side: NOTE §11(iii) inequalities proved; sieved Bohr means ⟹ continuous part thin; Theorem U_q for the
  u.d. class via Lev–Olevskii + pigeonhole + Saias–Weingartner + Landau).

## 2026-10-01 03:20 IST — batch 2 (task 2 theory) landed
- NOTE §2.1 Prop. E (Fejér form of the Euler side, general admissible sieve w = exp*(−Π₁); BFE §11(iii) now an identity with
  remainder ≥ 2q^{-1/2}S(1/q)); §2.2 Prop. E′ (Bohr form) ⟹ E1 ρ_q ≥ 1, E2 ∫u^{-1}dΠ_c ≤ log ρ_q (no purely continuous solution at
  any conductor), E3 discrete systems are free (c ≡ 1); §2.3 Lemma L (Landau, proved) + THEOREM L′ (F = ζ·D, D any finite generalized
  Dirichlet polynomial, Beurling + FE ⟹ q = 1, D ≡ 1); §2.4 THEOREM U_q (u.d. generalized integers ⟹ q = 1 and ζ; weights allowed),
  Cor. U1 (discrete, ρ_q < 1.366 ⟹ ζ), Cor. U2 (any solution has non-u.d. integers).
- Next: verify/v2 (identity (E) checked numerically on the non-Beurling self-dual examples; the reduced u.d. family decided for
  q = 2, 3, 4, 5, 6, 9, 25 with exact certificates), then §2.5 (beyond u.d.), §3 (rung-1 dictionary, verify/v3), §4–§5 close.

## 2026-10-01 03:45 IST — batch 3 (task 2 computations, task 3 data) landed
- verify/v2_euler_identity_and_ud_family.{py,log}: Part A identity (E) exact to ≤1e−50 on 5 self-dual examples × 5 sieves
  (left side by the Poisson closed form of Σ S(ne)); Part B rigorous interval certificates: u.d. family infeasible for
  q = 2, 3, 5 (B = q²), 4 (B = 32), 9 (B = 81), 25 (B = 625), 6 (B = 108); no failed piece.
- verify/v3_rung1_dictionary.{py,log}: F_5 genus 1, t ∈ {−12..12}: b_d ≥ 0 ⟺ t ∈ {−5..6} (RH-false admissible −5, 5, 6);
  N_n ≥ 0 and |α| ≤ 5 ⟺ t ∈ {−6..6}; Q-transplant ζ(s)L(5^{-s}): dN ≥ 0 ⟺ t ≤ 1, ρ ≥ 1 ⟺ t ≤ 5, Euler–Fejér at p = 2 ⟺ t ≤ 4,
  q-part positivity (= F2 with the pole factor 1/(1−5u) removed) ⟺ NO t. Matches Theorem L′.
- NOTE §2.5 written. Next: §2.6 (beyond u.d.), §3 (dictionary), §4 (attack log), §5 close.

## 2026-10-01 04:20 IST — batch 4 (beyond u.d.; conditional discrete theorem) landed
- New sources [here]: arxiv-2104.06812 (Baake–Spindeler–Strungaru 2023: periodic and u.d. Fourier eigenmeasures classified;
  general classification open, §8), arxiv-2605.23884 (Mazáč–Richard–Strungaru 2026, context), arxiv-2403.08659 (Lawton–Tsikh,
  context). No primary of Meyer's 1970 finite-values theorem found; two printed secondary statements on disk (KS 43–44, LO15 63–68).
- NOTE §1.5 (moved after §1.4): Q8 (BSS) + task-1 verdict. §2.6 (beyond u.d.). §2.7: Lemma S–W′ (S–W Thm 2 with radical-frequency
  weights; proof checked step by step at lines 417–621 of the S–W text), Lemma Q (finitely valued quasi-periodic ⟹ periodic),
  THEOREM D: given Meyer's theorem (Q4), every DISCRETE Beurling system with Riemann's FE at any conductor is ζ.
- Remaining open: weighted/mixed systems with infinitely many distinct atom masses (Meyer not applicable); the primary of Q4.
- Next: §3 rung-1 dictionary (verify/v3), §4 attack log, §5 close; re-check the digest.

## 2026-10-01 04:55 IST — CLOSE: T (stated classes, every conductor) + G (named residue)
- Digest landed during the unit (insights-digest.md, SHA-256 e86f642a…): §F.2 ranks this unit FIRST (line 352); quoted in NOTE §0.1,
  and its five consolidator's notes are answered (§1.2, §1.2(b), §1.6 = read-O R4(4), v1/v2 Fejér/exact checks, §3).
- T (unconditional): Theorem U_q (u.d. generalized integers ⟹ q = 1 and ζ; weights allowed); Theorem L′ (ζ·finite generalized
  Dirichlet polynomial never reaches q ≠ 1 inside the Beurling class); Cor. E2 (∫u^{-1}dΠ_c ≤ log ρ_q; no continuous solution);
  E1, E3, §1.4 Cor. 1–3; §1.6 (two-system version at conductor q: ratio band q^{-1/2} ≤ ρ₁/ρ₂ ≤ q^{1/2} sharp for measures; no
  Beurling pair in the u.d. class).
- T given Q4 (Meyer's finite-values theorem, on disk only via Kurasov–Sarnak 43–44 and Lev–Olevskii 2015 63–68): Theorem D — every
  discrete Beurling system with Riemann's FE at any conductor is ζ (via Lemma S–W′, checked against the S–W proof lines 417–621).
- G: open exactly for weighted/mixed systems with clustering integers and infinitely many distinct masses; fetch item: Meyer, LNM 117,
  p. 25 (or Córdoba 1989) to make Theorem D unconditional.
- verify/: v1 (examples), v2 (identity (E) exact; u.d. family certificates q = 2,3,4,5,6,9,25), v3 (rung-1 table), v4 (radical
  family certificate). All logs on disk. No construction; no new control claimed. Nothing load-bearing is recalled.
