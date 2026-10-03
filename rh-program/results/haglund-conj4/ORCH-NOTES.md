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

## N3. Theory — moved to `NOTE.md` §§1–5 (written 16:2x–16:4x IST; claimed, not yet read)

The level form (Lemmas 1.1–1.3), the real-axis theorem 2.1 and the conditional criterion 2.3 for (R), the frozen-level model (Lemma 3.1, Proposition 3.2), the off-axis-zero statement (Lemma 4.1, Proposition 4.2), and the three regimes (§5). Nothing there is a result before `read-O.md`.

## N4. A control on an object WITH off-axis zeros (16:17 IST 2026-10-03; `orch-probe/control.py`)

Object: f = Ξ + λ, λ > 0 (even, real, entire; it has zeros off the real axis above every negative lobe of Ξ whose minimum is > −λ). Its pencil is (Ξ_k + λ) + tΦ_{k+1} = f − L_t, and the real-axis quotient is (Ξ_{k+1} + λ)/Φ_{k+1}. Prediction of NOTE Theorem 2.1(d),(e) and Proposition 4.2: (R) and (D) must FAIL for this object. Run for k = 1 on [0.5, 45], step 0.005:
- λ = 0 (Haglund's own pencil): the extrema of the quotient with value in (0, 1) are three local maxima, at x = 22.140, 31.255, 38.515 with values 0.0837081, 1.32607e−4, 7.02799e−7 — the three landings of N2, found there by following branches (22.1424, 31.2550, 38.5169 at u = 0.0837083, 1.32607e−4, 7.02803e−7): two methods, same numbers. No local minimum.
- λ = 5e−5: a local maximum at x = 22.540 (value 0.628) and a LOCAL MINIMUM at x = 24.340 with value 0.612 ∈ (0, 1): as u = 1 − t decreases through 0.612, two real zeros meet at 24.34 and leave the real axis. The control violates (R), as predicted.
- λ = 1e−4: no extremum with value in (0, 1) on the range (the quotient is outside (0, 1) at its extrema there).
Sizes on the first negative lobe, for orientation: Ξ(16) = −7.69e−4, Q_1(16) = 1.21e−4, Q_2(16) = 5.5e−11.
So the test "no local minimum of the real-axis quotient with value in (0, 1)" is not vacuous: it fires on a function that has zeros off the axis and is silent on Ξ at k = 1.

## N5. The sign of Proposition 4.2, tested on the control (16:29 IST 2026-10-03; `orch-probe/signcheck.py`, `signcheck2.py`)

f = Ξ + λ, λ = 5e−5, has a zero off the axis at β = 28.6324463545 + 8.5242688193i (|f(β)| = 6e−20), with f′(β) = 2.9285e−5 + 3.9773e−5 i, so Im f′(β) > 0. Proposition 4.2 (applied to f in place of Ξ) predicts that the zero of (Ξ_k + λ) + tΦ_{k+1} near β moves UP as t increases. Computed, k = 2: Im z = 8.524267981346, 8.524268400330, 8.524268819313 at t = 0, ½, 1 — increasing, linearly in t, total +8.38e−7 (the size of Φ_3(β)/|f′(β)|); for k = 3, 4 the motion is below the 12 printed digits, as the factor Φ_{k+1}(0) predicts. The sign convention of the proposition is confirmed on this example. (A second zero of f off the axis was met on the way, at 61.548 + 26.785i.)

## N6. The far-field formula of NOTE §5 (III), tested (16:30 IST 2026-10-03; `orch-probe/far2.py`, log `far2.log`)

k = 2, zeros of Ξ_2 with real part near 500 (about nine times 2a = 2π·9). Found by Newton on log S_2: 495.53889+159.65294i, 498.17070+160.39391i, 500.79980+161.13340i, 503.42620+161.87143i. Below the zero curve |S_2| sits on a floor 1.6491e−9 = |c(1)/α_3|-type ratio of the algebraic parts (ln(1/floor) = 20.22). Each zero was followed through the pencil Ξ_2 + tΦ_3 (level-curve tracer, step 0.05): every one descends at every step (no step with increasing imaginary part) and ends at a non-real zero of Ξ_3; the first moved by +2.396 − 8.468i against the prediction δz = −ln(1/floor)/(T′/T) = +2.40 − 8.47i with T′/T = ½arg w − (i/2)ln|w/π|, w = 9/4 − iz/2 (the others in the log agree to the same three digits). So the heuristic of §5 (III) is quantitatively right at this point: far zeros descend, by about ln(c(0)/c(1))·Im(1/(T′/T)).

## N7. What a proof of (D) near the frontier would have to establish (16:33 IST 2026-10-03; a specification for a later proof unit, UNVERIFIED)

With q := Q_{k+1}/Φ_{k+1} and f := Ξ/Φ_{k+1} one has S_k = f − q; at a zero of the pencil f = u + q =: w, and S_k′ = w·Ψ − q′ with Ψ := Ξ′/Ξ − Φ_{k+1}′/Φ_{k+1}. So (D) at z is
  Re w·Im Ψ + Im w·Re Ψ < Im q′(z).
If the zeros of Ξ are real, Im Ξ′/Ξ = −y·S_2(z), S_2 := Σ_γ[|z − γ|^{−2} + |z + γ|^{−2}]. The other terms are small multiples of y: Im(Φ_{k+1}′/Φ_{k+1}) ≈ y(log Φ_{k+1})″(x), Im w = Im q ≈ y q′(x), Im q′ ≈ y q″(x) (each function is real on the axis), of relative sizes 1/a², x/a² and 1/a² with a = π(k+1)². Dividing by y·Re w, a sufficient condition is
  S_2(z) > C_1/a² + (C_2 x/a²)·|Re Ψ(z)|,
and |Re Ξ′/Ξ| ≤ (S_2·N)^{1/2} + O(log x) with N the number of zeros of Ξ within distance 1 of x. So the proof needs (i) explicit bounds for (log Φ_{k+1})″, q′/q and q″/q in a strip 0 < y ≤ Y over 0 ≤ x ≤ 4(k+2)² + X_0 (kernel estimates; the kernels are explicit); (ii) a lower bound S_2(z) ≥ c_0 in the same strip, i.e. a bound for the gaps between consecutive zeros of Ξ there (numerically known where RH is verified; under RH a theorem for large height). As y → 0 the condition becomes the real-axis criterion of NOTE Proposition 2.3, as it must. The middle and far regimes need uniform asymptotics of the incomplete gamma function instead (N6 shows the far-field law numerically).
