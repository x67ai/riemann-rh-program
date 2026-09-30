# read-F — the orchestrator's read at the line of `NOTE.md` (seed N4 `tournament`)

Reader: Fable 5.1 (the orchestrator, in person — standing orders 7, 11(c)). Session 37, 2026-09-30. NOTE read whole (176 lines, all 35 rows, three deep dives).
Verdict: **AGREES. Close (N) UPHELD — nothing survives, correctly.** No FIX-FIRST item; one labeling rule for how the table may be used.

## 1. Re-derivations (done by the reader)

- T1: E_ε(1 − εx)^{−1} = ½[(1 − x)^{−1} + (1 + x)^{−1}] = (1 − x²)^{−1}. ✓   T3: g_p = −√p(1 − p^{−s})(1 − p^{s−1}), zeros on Re s = 0, 1. ✓ (= N3 Theorem D)
- T5: a Hasse-compliant factor vanishes at some |t| ≤ π/log q ≤ π/log 2 = 4.53 < 14.13; Hurwitz. ✓
- T6 (the one self-contained new proof in the table): an infinitely divisible law with all exponential moments has an n-th convolution root with the same
  property for every n, so φ = φ_n^n with φ_n entire; the order of any zero of φ is divisible by every n, hence there is none. ✓ So the tilted Riemann
  kernel Φ(u)e^{εu} is never infinitely divisible, whatever the truth of RH.
- T15: orbit lengths of a finite-alphabet suspension with a finite-coordinate roof lie in a finitely generated group; {log p} is Q-independent. ✓ (twin of IV.20)
- T18: Re[w/(1 − w)] at w = −|w| is −|w|/(1 + |w|) < 0. ✓   T34: ζ^{−1} = det₂(I − K_s)·e^{−P(s)} and P(s) = Σ_k μ(k)k^{−1} log ζ(ks). ✓
- DD1, F_{a,q}: Λ_F(q^k) = log q·[1 + (−1)^{k+1}(α^k + β^k)], so Λ_F(q²)/log q = 1 − a² + 2q < 1 − 2q < 0 for a > 2√q. ✓
- DD1, the virtual curve by hand: L(u) = 1 − 5u + 5u², α, β = (5 ± √5)/2, αβ = 5; N_1..N_5 = 1, 11, 76, 451, 2501; b_1..b_5 = 1, 5, 25, 110, 500;
  σ = log α/log 5 = 0.79899. ✓ (b_d ∈ Z for all d because N_n = tr of integer matrices' powers; b_d > 0 because 5^d dominates.)

## 2. The decisive computations, re-run (independent code)

`verify-F/rerun_dd1.py` (+ `.log`): (1) Epstein x² + 5y²: Λ(n) ≥ 0 for n < 36 and Λ(36) = −2.0000·log 36 (8 negatives below 400); x² + y² (class number one):
no negative value to 400. (2) The virtual curve over F₅: N_n ≥ 1 and b_d ≥ 0, integers, for all d ≤ 60 (the NOTE checked 40); functional equation residual 3e−16;
zeros at σ = 0.79899, 0.20101. (3) F_{2.9,2}, F_{5,5}, F_{3,2}: Λ(q²)/log q = −3.41, −14, −4. **CONFIRMED.**

## 3. How the table may be used (labeling rule, not a correction)

The 35 verdicts are BRIEF-TIME verdicts (zoo §0 protocol), not zoo entries. Rows whose kill or equivalence rests on a statement the writer labeled
`[recalled, unverified]` — T4 (Schoenberg), T10 and T12 (the Euler-product-convergence equivalence), T13, T17, T19, T23, T26, T28, T29, T30, T32, T33 — may be
cited as "screened at brief time" only; re-proposing one of them requires reading its recalled source first (standing order 5). Rows with proofs on the page
or resting on program theorems: T1, T2, T3, T5, T6, T15, T16, T18, T21, T34, T35. The zoo gains exactly two things from this seed: the control "virtual curve
over F₅" (DD1; the rung-1 twin test: a mechanism the virtual curve passes cannot be the generator) and the T6 lemma.

## 4. For the digest (the reader's reading of §4)

The four survivor properties are adopted as the next wave's filter, with one sharpening: property (4) is two different statements. (4a) On rung 1 the input
the virtual curve lacks is GEOMETRIC (a surface with an index theorem; a family with monodromy), and both are inputs about an object BESIDES the zeta function.
(4b) Over Z, Hamburger's rigidity says the zeta function determines itself from the FE and the Dirichlet-series shape; it supplies uniqueness, not an extra
object. A generator "consuming rigidity" would have to turn a uniqueness theorem into an inequality; the known way uniqueness becomes positivity is an
EXTREMAL characterization (the unique minimizer of a functional is where its second variation is nonnegative). That is a concrete shape for a seed:
find a variational problem on a class of functions with FE-type constraint whose unique extremal is ξ (uniqueness by a Hamburger-type argument) and whose
second variation at the extremal is a form in the zeros. Recorded for the funding decision, not claimed.
