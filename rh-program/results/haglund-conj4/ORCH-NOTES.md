# ORCH-NOTES — Haglund's Conjecture 4 (the pencil Ξ_k + tΦ_{k+1}) — the orchestrator's working notes

**UNVERIFIED — use it; check it (KICKSTART 10(r)).** Everything here is the orchestrator's own mathematics, written as it is worked out. Nothing in this file is a result until it has been checked (a computation, an Opus read, the page).

Opened 16:03 IST 2026-10-03. Trigger: the author's question, relayed by the sponsor (LOG, this side-session's opening entry).

## N0. The statement at the page

Haglund, arXiv:0910.5228v1, p. 11 (text on disk: `results/novel-wave-s36/staircase/lit/haglund-0910.5228.txt` l. 585–592). The lead-in: for Ξ_k(z) + tΦ_{k+1}(z), as t goes from 0 to 1, "computations indicate that the imaginary parts of the non-real zeros decrease monotonically (i.e. continuously), in a very regular manner, until, for high enough k, they collide with the corresponding zero (from Schwartz reflection) in the fourth quadrant, and arrive on the real line, where they remain." Then: "Conjecture 4 For k ≥ 1, the imaginary part of each non-real zero of Ξ_k(z)+t Φ_{k+1}(z) decreases monotonically (i.e. continuously) as t goes from 0 to 1."

Two parts, kept apart below: (D) DESCENT — a non-real zero in the upper half-plane has non-increasing imaginary part along its branch; (R) REMAIN — a zero that has reached the real axis stays real (in the lead-in, not in the displayed conjecture). A branch that leaves the real axis violates (D) as well, since just after leaving it is a non-real zero whose imaginary part increases.

Journal version (Cent. Eur. J. Math. 9 (2011) 302–318; text on disk `haglund-CEJM-2011-degruyter-fulltext.md`): conjectures are numbered by section there (his Conjecture 1 is "Conjecture 2.1"); the table entry at N = 4 is still 32 in the journal version.

Prior art on record (`results/haglund-cert-s37/NOVELTY-F.md` item 3; `results/arxiv/haglund-counterexample/lit/zenodo-22059236.md`): M. L. Baccaro, Zenodo 10.5281/zenodo.22059236 (22 Aug 2026), claims the case k = 1 with an interval-arithmetic certificate and a Lean project; its record says "Higher cases remain open". Nothing else found on Conjecture 4 at the Session-37 searches. A fresh dual-model search is owed before any novelty word is used (standing order 7).

## N1. The pencil is "Ξ minus a positive level" (exact)

From the paper's sandwich theorem (`results/arxiv/haglund-counterexample/main.tex`, Theorem sandwich and its proof): for n ≥ 2 the kernel φ̃_n is positive, strictly decreasing and strictly convex on [0, ∞), termwise; so by the Pólya argument Φ_n(x) = 2∫_0^∞ φ̃_n(u) cos(xu) du > 0 for every real x and every n ≥ 2 (the paper states it for the tail sum Q_N; the proof is termwise). With Q_N = Σ_{n>N} Φ_n (entire; Ξ_N = Ξ − Q_N):

  F_k(z, t) := Ξ_k(z) + tΦ_{k+1}(z) = Ξ(z) − L_t(z),   L_t := (1 − t)Φ_{k+1} + Q_{k+1} = (1 − t)Q_k + tQ_{k+1}.

On the real axis L_t(x) > 0 for 0 ≤ t ≤ 1 and k ≥ 1, and ∂F_k/∂t = Φ_{k+1}(x) > 0.

Equivalent form used for computing: with u = 1 − t, zeros of the pencil are the solutions of S_k(z) = u, where S_k := Ξ_{k+1}/Φ_{k+1}; along a branch dz/du = 1/S_k'(z), so dz/dt = −1/S_k'(z).
  (D) for k  ⟺  Im S_k'(z) ≤ 0 at every z with Im z > 0 and S_k(z) ∈ (0, 1)   [Im(dz/dt) = −Im(1/S') = Im S'/|S'|²].

## N2. First probe (orchestrator's own, `orch-probe/`; midpoint Arb arithmetic, not a certificate)

`orch-probe/c4probe.py` evaluates S_k = Ξ_{k+1}/Φ_{k+1} by two routes, both through the registered evaluator `results/arxiv/haglund-counterexample/certificate/producer-A/hag_core.py`: route T (Ξ from Arb's zeta, minus Φ_n for k+2 ≤ n ≤ M, tail as an error ball) and route L (the literal sum). Ladder: at Haglund's appendix zero 20.6253…+2.6971…i of Ξ_1 both routes give S_1 = 1 to 1e−22; routes T and L agree to all printed digits at 70+5i and 150+20i for k = 3. Speed on this machine: about 1 ms per value near the real axis (k = 1 and k = 27 alike), about 30 ms at 900+60i for k = 10.

`orch-probe/trace.py` follows a branch as the level curve Im S_k = 0, with u = Re S_k decreasing from 1 (predictor along −1/S', corrector along the normal, S' by central difference). Pencil k = 1, the first seven non-real zeros of Ξ_1 from Haglund's appendix (p. 16):

| start (zero of Ξ_1) | end | u at the end | imaginary part ever increased? |
|---|---|---|---|
| 20.6253+2.6972i | lands on the real axis at x = 22.1424 | 0.0837 | no |
| 26.0562+7.1254i | lands at x = 31.2550 | 1.33e−4 | no |
| 31.5014+10.7292i | lands at x = 38.5169 | 7.03e−7 | no |
| 36.7270+13.7596i | zero of Ξ_2 at 43.1389+3.2810i | 0 | no |
| 41.7370+16.4401i | zero of Ξ_2 at 47.5228+6.2525i | 0 | no |
| 46.5662+18.8819i | zero of Ξ_2 at 51.8283+8.9586i | 0 | no |
| 51.2446+21.1475i | zero of Ξ_2 at 56.1120+11.4796i | 0 | no |

The three landings fall in the three positive lobes of Ξ below 41 — (21.02, 25.01), (30.42, 32.94), (37.59, 40.92) — which is the count 1 + 2·3 = 7 of Haglund's table at N = 2. The landings happen at u = 0.08, 1e−4, 7e−7: the deformation is singular in t (most of the motion of the frontier happens for t within e^{−π(2k+3)} of 1), which is the natural reason Newton continuation in t stalls near t = 1 (Haglund p. 12, "about t = .99").
