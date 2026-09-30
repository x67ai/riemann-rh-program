# CERT — Haglund's Conjecture 1 fails at N = 27 (producer A: Arb ball arithmetic)

Unit `haglund-cert-s37`, Session 37, 2026-09-30. Producer A. Tools: macOS 27.0.1 (Apple M4), /usr/bin/python3 3.9.6,
python-flint 0.6.0 bundling FLINT 3.0.1 (Arb). Producer B's folder was not read.

## 1. Theorem H (certified)

Objects exactly as Haglund, arXiv:0910.5228 (text on disk, `novel-wave-s36/staircase/lit/haglund-0910.5228.txt`):
Ξ (1) p. 1; G(w; a, b) (6) and (10) p. 2; Φ_n (14) p. 3; Ξ_N = Σ_{n≤N} Φ_n (13) p. 3; Ξ = Σ_{n≥1} Φ_n (12) p. 3;
Q = {Re z ≥ 0, Im z ≥ 0} p. 1; Conjecture 1 and "monotonic zeros" p. 3; Remark 1 (weak form) p. 4.

- **(H1)** Ξ₂₇ has a real zero x₁ ∈ (3144.8946, 3144.8947):
  Ξ₂₇(3144.8946) ∈ [−1.76019463127752e−1070 ± 4.1e−1085], Ξ₂₇(3144.8947) ∈ [+1.06871649226171e−1070 ± 3.3e−1085]
  (balls as printed, display rounding included; the Arb radii are 3.3e−1435 by route L at 4800 bits, 6.0e−1915 at
  6400 bits, 5.0e−1138 by route T at 256 bits — all four evaluations give the same signs).
- **(H2)** Ξ₂₇ has a zero z₀ in the closed square S = c + [−r, r]², c = 3143.2206824215 + 0.3152587994 i, for
  r = 10⁻³ and for the smallest r reached, **r = 4·10⁻¹¹**: the winding number of Ξ₂₇ along ∂S is **k = 1** in every
  run (r = 1e−3 at 256 and 512 bits; r = 1e−6, 1e−10, 4e−11 at 256 bits). Total ΔArg = 6.28318530717959 ± 4e−15.
  So z₀ ∈ [3143.2206824215 ± 4e−11] + i[0.3152587994 ± 4e−11] (the NOTE's 50-digit value lies inside).
- **(H3)** Hence z₀ ∈ Q is non-real (Im z₀ ≥ 0.3152587994 − 4e−11 > 0.3152) with Re z₀ ≤ 3143.2206824215 + 4e−11
  < 3143.2207 < 3144.8946 < x₁, and x₁ is a real zero (Im x₁ = 0 < Im z₀). Listing the zeros of Ξ₂₇ in Q by increasing
  real part, z₀ precedes x₁ while Im z₀ > Im x₁: the imaginary parts are not nondecreasing, so **Conjecture 1 is false
  for N = 27**; and z₀ is a non-real zero in Q whose real part is less than a real zero of Ξ₂₇ (hence less than the
  largest one), so **the weak form (Remark 1) is false for N = 27** too. (The pair (z₀, x₁) violates the conjecture
  under any enumeration consistent with "increasing real part", so Haglund's side assumption of at most one zero per
  vertical line does not matter.)
- **(H4, optional, done)** a second real zero x₂ ∈ (3145.5998, 3145.5999): Ξ₂₇(3145.5998) ∈ [+1.12975694291664e−1070
  ± 1.9e−1085], Ξ₂₇(3145.5999) ∈ [−1.14913915362778e−1070 ± 2.9e−1085] (both routes, same four precisions).

Numerical location (not load-bearing): z₀ ≈ 3143.220682421536585287 + 0.3152587993782148453823 i, where
Ξ₂₇ ≈ 2.5787820316330e−1085 + 1.7049877228997e−1084 i (route L and route T agree, |L − T| ≤ 1.2e−1288).

## 2. Method and trust base

- **Route L** (`hag_core.XiN_L`): the literal sum (13) of (14), G by (10), Γ(s, a) = `acb(a).gamma_upper(s)` (FLINT's
  acb_hypgeom_gamma_upper; convention Γ(order s, lower limit a) checked in `ladder.log` C0: Γ(1,2) = e⁻², Γ(3,2) = 10e⁻²),
  a^{−s} = exp(−s log a). At z = 3144.8946 the terms fall from |Φ₁| ≈ |Φ₂| ≈ 8.0e−9 to |Φ₂₇| ≈ 1.5e−991 while the sum
  is −1.76e−1070 (~1062 digits cancel), so L is used only at exact points, at 4800 and 6400 bits (radii 3e−1435 and
  6e−1915: the cancellation is fully resolved).
- **Route T** (`hag_core.XiN_T`): Ξ₂₇ = Ξ − Σ_{n=28}^{31} Φ_n − R₃₁, with Ξ by (1) from FLINT's acb_zeta and acb_gamma,
  Φ₂₈…Φ₃₁ as in route L but on ball inputs, and |R₃₁| ≤ 2U₃₂ (Lemma T) added to Re and Im as an error ball. All terms are
  ~1e−1066 or smaller (Φ₂₈ ≈ 1.49e−1066 ≈ Ξ near z₀, Φ₂₉ ≈ 3e−1144, 2U₃₂ ≈ 2e−1393): no catastrophic cancellation, so T
  is sharp on ball inputs (256 bits: output radius ≈ 1.2e−1063 × input radius, value ~1e−1076 at c).
- **Trust base.** Every arithmetic operation and special function (±, ×, ÷, exp, log, arg, Γ, ζ, Γ(s, a), decimal-string
  -> ball conversion) is FLINT/Arb's, whose contract is that the output ball contains the exact value for every input in
  the input balls; comparisons `x > 0` are True only when certain (checked: [−1, 1] > 0 and [1 ± 1.5] > 0 are False).
  No floating-point value is used in any decision. The only non-computed inputs are Lemmas B, Γ, T, the half-plane
  lemma (proved below), identity (12) (Haglund p. 2–3, read on disk, see §3.4), the intermediate value theorem and the
  argument principle.

## 3. Analytic ingredients (all proved here, or cited from a page read on disk)

**3.1 Lemma B.** For w ∈ ℂ, a > 0, b ∈ ℝ: |G(w; a, b)| ≤ 2Γ(β, a)/a^β with β = b + |Im w|.
*Proof.* G(w; a, b) = 4∫₀^∞ cos(2wu) e^{2bu − a e^{2u}} du (Haglund (6), p. 2; the integrand decays super-exponentially,
so this is entire in w and equals (10) by the real substitution t = a e^{2u}, Haglund (7)–(10)). For u ≥ 0,
|cos(x + iy)|² = cos²x + sinh²y ≤ cosh²y, so |cos(2wu)| ≤ cosh(2u Im w) ≤ e^{2u|Im w|}. Hence
|G| ≤ 4∫₀^∞ e^{2βu − a e^{2u}} du, and the substitution t = a e^{2u} (du = dt/2t) turns this into
2a^{−β}∫_a^∞ t^{β−1}e^{−t} dt = 2Γ(β, a)/a^β. ∎

**3.2 Lemma Γ.** For β ≥ 1 and a > β − 1: Γ(β, a)/a^β ≤ e^{−a}/(a − β + 1).
*Proof.* With t = ax, Γ(β, a)/a^β = ∫₁^∞ x^{β−1}e^{−ax} dx. For x ≥ 1, log x ≤ x − 1 and β − 1 ≥ 0, so
x^{β−1} ≤ e^{(β−1)(x−1)}; hence the integral is ≤ e^{−a}∫₀^∞ e^{−(a−β+1)y} dy = e^{−a}/(a − β + 1). ∎
(The orchestrator's sketch in BRIEF §2 is correct, provided β ≥ 1; for β < 1 it can fail. Here β ≥ 5/4 always.)

**3.3 Lemma T (tail).** Let Y ≥ |Im z|, β₉ = 9/4 + Y/2, β₅ = 5/4 + Y/2, a_n = πn², and M ≥ 1 with a_{M+1} − β₉ + 1 > 0.
Put U_n = 2e^{−a_n}(2π²n⁴ + 3πn²)/(a_n − β₉ + 1). Then |Σ_{n>M} Φ_n(z)| ≤ Σ_{n>M} U_n ≤ 2U_{M+1}.
*Proof.* Φ_n(z) = 2π²n⁴G(z/2; a_n, 9/4) − 3πn²G(z/2; a_n, 5/4) and |Im(z/2)| ≤ Y/2. By Lemmas B and Γ (β₉ ≥ β₅ ≥ 5/4 ≥ 1
and a_n ≥ a_{M+1} > β₉ − 1 ≥ β₅ − 1): |Φ_n| ≤ 2π²n⁴·2e^{−a_n}/(a_n − β₉ + 1) + 3πn²·2e^{−a_n}/(a_n − β₅ + 1) ≤ U_n,
since a_n − β₅ + 1 > a_n − β₉ + 1 > 0. For n ≥ 1, U_{n+1}/U_n = e^{−π(2n+1)} · [2π²(n+1)⁴ + 3π(n+1)²]/[2π²n⁴ + 3πn²]
· (a_n − β₉ + 1)/(a_{n+1} − β₉ + 1) ≤ e^{−3π} · 16 · 1 < 1.3·10⁻³ (the middle factor is ≤ ((n+1)/n)⁴ ≤ 16 by the mediant
inequality; the last is < 1). So Σ_{n>M} U_n ≤ U_{M+1}/(1 − 1.3·10⁻³) ≤ 2U_{M+1}. ∎
In code (`tail_bound`): Y = Arb upper bound of |Im z| over the input box, M = N + 4 (= 31 for N = 27, 5 for N = 1,
6 for N = 2), and the code asserts a_{M+1} − β₉ + 1 > 1. At N = 27, Y ≤ 0.317: 2U₃₂ ≤ 2e−1393.

**3.4 Identity (12)** Ξ(z) = Σ_{n≥1} Φ_n(z), all z ∈ ℂ. Source read on disk: Haglund p. 1, (2)–(3) (Riemann's
Ξ(z) = ∫₀^∞ cos(zt)φ(t) dt, φ = Σ φ_n, from Riemann's memoir via Edwards) and p. 2–3, (6) and (12): since
(6) with w = z/2 has integrand cos(zu)e^{2bu − a e^{2u}}, ∫₀^∞ cos(zt)φ_n(t) dt = Φ_n(z) (8π²n⁴/4 = 2π²n⁴ and
12πn²/4 = 3πn², as in (14)). The interchange of Σ and ∫ (Haglund: "uniform convergence") also follows by dominated
convergence: the proof of Lemma B bounds ∫₀^∞ |cos(zt)φ_n(t)| dt, and by Lemma Γ these bounds are ≤ U_n (Y = |Im z|)
for all large n, a summable sequence. Route T depends on (12); route L does not.
Numerical corroboration (not a proof): routes L and T agree at every one of the 18 points compared (§6), to
|L − T| ≤ 1.2e−1288 at 1024 bits, and at N = 1, 2 (R1).

**3.5 Half-plane lemma (winding increments).** Let γ: [0, 1] → ℂ be a path and E a closed axis-parallel box with
0 ∉ E and γ([0, 1]) ⊂ E. Then E lies in one of the open half-planes Re > 0, Re < 0, Im > 0, Im < 0 (the code certifies
which one), and the continuous change of arg along γ equals the principal value Arg(γ(1)/γ(0)) ∈ (−π, π).
*Proof.* A box excluding 0 has, in at least one coordinate, both endpoints of the same strict sign, so it lies in an open
half-plane H = {Re(w e^{−iθ}) > 0}. On H the branch arg_H ∈ (θ − π/2, θ + π/2) is continuous, so the continuous change
is arg_H(γ(1)) − arg_H(γ(0)) ∈ (−π, π), which is ≡ Arg(γ(1)/γ(0)) mod 2π; two numbers in (−π, π] that agree mod 2π are
equal. ∎ The code also checks that the Arb enclosure of each Arg lies strictly inside (−π, π) (no branch-cut ambiguity).

**3.6 Argument principle.** Ξ₂₇ is entire (a finite sum of entire functions: Γ(s, a) is entire in s for a > 0, Haglund p. 3, below (12)); if it has no zero
on the positively oriented boundary of the square S, the number of its zeros in S, with multiplicity, equals
(1/2π)·(total continuous change of arg Ξ₂₇ along ∂S). A certified total in (2π(k − ½), 2π(k + ½)) gives k zeros.

## 4. Ladder (BRIEF §4), run first, same code (`ladder.py` -> `ladder.log`, 256 bits, 11.9 s)

| step | object | result |
|---|---|---|
| C0 | `gamma_upper` convention | Γ(1,2) = e⁻² and Γ(3,2) = 10e⁻² (overlapping balls) |
| R1 | Ξ₁ on (14.04543957, 14.04543959) | +1.347060456147e−11 / −1.704102125315e−11, both routes (L rad 5e−75, T rad 7e−47) |
| R1 | Ξ₂ on (39.5324810797, 39.5324810799) | +3.605517254360e−21 / −4.593418771015e−21, both routes (L rad 3e−75, T rad 2e−64) |
| R2 | Ξ₁, square r = 1e−10 at Haglund's 20.62534600592171760132974 + 2.697151842339519632505712 i (App. p. 15) | 1516 pieces, ΔArg = 2π ± 4e−15, **k = 1** |
| R3a | Ξ₁, same centre + 0.5, r = 0.1 (zero-free) | 271 pieces, ΔArg ∈ [± 2e−39], **k = 0** |
| R3b | Ξ₁, same centre + 3e−10, r = 1e−10 (zero 2e−10 outside) | 637 pieces, ΔArg ∈ [± 7e−30], **k = 0** |

## 5. H1 and H2 runs

**H1/H4** (`h1.py` -> `h1.log`, 10.4 s): four evaluations per endpoint — T at 256 and 1024 bits, L at 4800 and 6400 bits
(L: 0.7 s and 1.1 s per point). All four certify the sign changes of §1; L (4800) and T (256) overlap at all four
endpoints, |L − T| ≤ 5.1e−1138.

**H2** (`h2.py` -> `h2.log`, 36.2 s): K₀ = 16 initial pieces per side, bisection of any piece whose enclosure meets 0
(max depth 16, never reached); every accepted piece's enclosure lies in a certified open half-plane; every increment is
enclosed strictly inside (−π, π); every enclosure and increment is printed in the log.

| run | r | bits | pieces | total ΔArg | k | time |
|---|---|---|---|---|---|---|
| H2 | 1e−3 | 256 | 512 | 6.28318530717959 ± 4e−15 | 1 | 3.8 s |
| H2 | 1e−3 | 512 | 512 | 6.28318530717959 ± 4e−15 | 1 | 10.2 s |
| H2 | 1e−6 | 256 | 512 | 6.28318530717959 ± 4e−15 | 1 | 3.7 s |
| H2 | 1e−10 | 256 | 663 | 6.28318530717959 ± 4e−15 | 1 | 5.0 s |
| H2 | 4e−11 | 256 | 807 | 6.28318530717959 ± 4e−15 | 1 | 6.1 s |
| control | 1e−3 at c + 2.5e−3 | 256 | 269 | [± 7e−66] | 0 | 1.9 s |
| control | 1e−10 at c + 1.5e−10 (zero 1.3e−11 outside) | 256 | 714 | [± 1e−57] | 0 | 5.4 s |

r = 4e−11 is the smallest r reached; with this centre no r < 3.66e−11 can contain the zero (it sits at c + 3.66e−11 −
2.18e−11 i by the NOTE's 50-digit solve), so the certified square is within 10% of the smallest possible one.

## 6. Cross-check L (4800 bits) vs T (256 / 1024 bits) at exact points (`xcheck.py` -> `xcheck.log`, 10.4 s)

| point | Ξ₂₇ by route L (8 digits shown) | abs(L − T₂₅₆) ≤ | abs(L − T₁₀₂₄) ≤ | overlap |
|---|---|---|---|---|
| centre c | 1.6557370e−1076 + 2.0178675e−1076i | 3.31e−1137 | 1.18e−1288 | yes |
| z0* (NOTE 50-digit zero, truncated) | 2.5787820e−1085 + 1.7049877e−1084i | 3.30e−1137 | 1.18e−1288 | yes |
| r=1e−3 corner SW | −5.154499e−1069 + 6.9527026e−1069i | 6.39e−1137 | 1.17e−1288 | yes |
| r=1e−3 corner SE | −6.967925e−1069 − 5.1198207e−1069i | 6.40e−1137 | 1.18e−1288 | yes |
| r=1e−3 corner NE | 5.1349801e−1069 − 7.0026807e−1069i | 6.43e−1137 | 1.18e−1288 | yes |
| r=1e−3 corner NW | 6.9874455e−1069 + 5.1697997e−1069i | 6.43e−1137 | 1.17e−1288 | yes |
| r=1e−3 mid S | −6.048746e−1069 + 9.1158497e−1070i | 3.30e−1137 | 1.18e−1288 | yes |
| r=1e−3 mid E | −9.289432e−1070 − 6.0563421e−1069i | 6.41e−1137 | 1.18e−1288 | yes |
| r=1e−3 mid N | 6.0737362e−1069 − 9.2134453e−1070i | 3.31e−1137 | 1.18e−1288 | yes |
| r=1e−3 mid W | 9.0395426e−1070 + 6.0661024e−1069i | 6.41e−1137 | 1.17e−1288 | yes |
| r=4e−11 corner SW | −4.021729e−1077 + 4.8089430e−1076i | 6.40e−1137 | 1.18e−1288 | yes |
| r=4e−11 corner SE | −1.135338e−1076 − 4.0042475e−1078i | 6.41e−1137 | 1.18e−1288 | yes |
| r=4e−11 corner NE | 3.7136471e−1076 − 7.7320787e−1077i | 6.41e−1137 | 1.18e−1288 | yes |
| r=4e−11 corner NW | 4.4468125e−1076 + 4.0757776e−1076i | 6.40e−1137 | 1.18e−1288 | yes |

Plus the four H1/H4 endpoints (`h1.log`): overlap, |L − T₂₅₆| ≤ 5.1e−1138. 18 points in all, all overlapping.

## 7. Reproduction, run times, versions, remarks

- In this folder: `python3 ladder.py > ladder.log` (11.9 s), `python3 h1.py > h1.log` (10.4 s), `python3 h2.py > h2.log`
  (36.2 s), `python3 xcheck.py > xcheck.log` (10.4 s), `python3 h5.py > h5.log` (3.2 s); all use `hag_core.py`. One process at a time, Apple M4, single
  thread. Versions: /usr/bin/python3 3.9.6; python-flint 0.6.0 (bundled libflint.18.0 = FLINT 3.0.1, with GMP, MPFR).
- Remarks on the brief. (a) Lemma Γ needs β ≥ 1 (for β < 1 it can fail: β = 0, a = 1 gives E₁(1) = 0.219 > e⁻¹/2);
  all uses here have β ≥ 5/4. (b) `acb(x).gamma_upper(s)` = Γ(s, x) confirmed (C0). (c) Route T is sharp on balls
  because the n ≥ 28 terms are all ≤ ~1e−1066 at this height (Φ₂₈ ≈ Ξ ≈ 1.49e−1066 near z₀): the only cancellation is
  the benign Ξ − Φ₂₈ one (relative size ~ |z − z₀|), handled at 256 bits even at r = 4e−11.
- Standing-order check: the bounds used (Lemmas B, Γ, T, half-plane lemma) are proved in §3; the only cited identity (12)
  is from pages read on disk; no recalled bound is load-bearing.

## 8. Optional H5: the seed's chain ξ_N (staircase NOTE §1, §4), N = 24 (`h5.py` -> `h5.log`, 3.2 s)

ξ_N(s) = ½ + ½s(s−1)Σ_{n≤N} g_n(s), g_n(s) = X^{−s/2}Γ(s/2, X) + X^{−(1−s)/2}Γ((1−s)/2, X), X = πn² (NOTE §1).
Route L: this literal sum (4800 bits; it cancels ~855 digits). Route T: ξ − ½s(s−1)Σ_{n=25}^{28} g_n − tail, using
ξ(s) = ½ + ½s(s−1)Σ_{n≥1} g_n(s) (Riemann; derivation re-done in NOTE §1: split ∫₀^∞ψ(x)x^{s/2−1}dx at 1, use
ψ(1/x) = √xψ(x) + (√x − 1)/2, ψ(x) = Σ_{n≥1} e^{−πn²x}; Jacobi's theta relation is the one classical input of H5
that is not re-proved here — H1–H3 do not use it).
**Lemma G.** For −1 ≤ Re s = σ ≤ 2: |g_n(s)| ≤ 2e^{−X}/X. *Proof.* |X^{−s/2}Γ(s/2, X)| ≤ X^{−σ/2}∫_X^∞ t^{σ/2−1}e^{−t}dt
= ∫₁^∞ x^{σ/2−1}e^{−Xx}dx ≤ ∫₁^∞ e^{−Xx}dx = e^{−X}/X as σ/2 − 1 ≤ 0; the same for (1−s)/2 as (1−σ)/2 − 1 ≤ 0. The ratio
of consecutive bounds is e^{−π(2n+1)}n²/(n+1)² < ½, so |½s(s−1)Σ_{n>M} g_n| ≤ ½|s(s−1)|·2·2e^{−X_{M+1}}/X_{M+1}. ∎
- **(H5a)** on-line zeros, both routes: ξ₂₄(½ + 2510.2026 i) ∈ [+2.81317536164e−854 ± 5e−866], ξ₂₄(½ + 2510.2027 i) ∈
  [−1.65267129215e−854 ± 3e−866]; ξ₂₄(½ + 2510.7086 i) ∈ [−3.23281139505e−854 ± 4e−866], ξ₂₄(½ + 2510.7087 i) ∈
  [+6.14184061542e−855 ± 4e−867] (ξ_N(½ + it) is real: ξ_N(1 − s) = ξ_N(s) and ξ_N(s̄) = conj ξ_N(s), term by term):
  zeros at t ∈ (2510.2026, 2510.2027) and (2510.7086, 2510.7087).
- **(H5b)** winding of ξ₂₄ along the s-square centred 0.8159896243 + 2508.2839748053 i: k = 1 for r = 1e−3 (151 pieces)
  and r = 1e−10 (174 pieces); control (centre + 2.5e−3 i, r = 1e−3): k = 0. L and T overlap at the centre and at the
  NOTE's zero. Hence a zero ρ with Re ρ ≥ 0.8159896242 > ½ and Im ρ ≤ 2508.2839748054 lies below on-line zeros:
  **the ordering invariant (NOTE §4.1) fails for ξ₂₄.** H5's route T rests on Riemann's identity above (NOTE §1).

## 9. SHA-256 (logs and scripts as delivered; the hash of this file is in SHARED.md)

    d88efc8879dc7b22b9fac0bb01c5f47baf983c92778f14c208765053848d473a  ladder.log
    e9ac0878ea67ef58e57dfcb23838436b2b3fdd92185ace6286f7d6faa21d7c56  h1.log
    90a00e963b1f7891c092e4d65127568aea99f06b45789e54db96ce91e70d7f90  h2.log
    e05c73a7d4ce1e7c0fc8fbd0a9b5be0c595b9a4ec10d22a9752ccc160e4d799e  xcheck.log
    48455c3a41864bdf1208557f491085351991d5d968a97b46c772a09c6277ae05  h5.log
    938427c9589f4faf063a3d4176a942634083c6f227ba86dacdec769ca0799e7a  hag_core.py
    1661d3729a009034d73a0b40f5daa9b284c8fe0e1b11a624de3e2b53cb5ed3b4  ladder.py
    f3df91f8e6a61a593188042412fe122dd38a365c73239ce47e504d50589fa339  h1.py
    4fc3b6803b43a18f055b104f71c828092386b2ef926be6bb3bbec788e4b293a5  h2.py
    238f8d111445399dde5d640f26c99ee3ebbaf0a83b3eb1d46f18a284ee2fa32e  xcheck.py
    1d12bf4c154ac1b27d082dd9bbd7a099dbd9d57c290db59723c37667e033c3b4  h5.py
