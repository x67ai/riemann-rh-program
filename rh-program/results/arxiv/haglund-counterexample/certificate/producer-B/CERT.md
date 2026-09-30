# CERT — producer B: Haglund's Conjecture 1 fails at N = 27 (interval-rigorous; no Arb, no python-flint)

Certificate B, 2026-09-30. Independent of certificate A, which was never opened. Arithmetic: mpmath 1.3.0 `mp.iv`
(outward-rounded real intervals; complex numbers as rectangular boxes built on them in `ivc.py`), exact rationals for Bernoulli
numbers. Every truncation adds a disk whose radius is a bound proved in §B. Scripts: `ladder.py`, `cert27.py` (Theorem H),
`crosscheck.py`, `selftest.py` (checks), `cert_h5.py` (optional H5); library `ivc.py`, `specfun.py`, `xin.py`, `winding.py`.

## 0. Theorem H (certified)

Ξ₂₇ = Σ_{n≤27} Φ_n (Haglund (13)–(14)); s = ½ + iz.
- **(H1)** Ξ₂₇(3144.8946) ∈ −1.760194631277516e−1070 and Ξ₂₇(3144.8947) ∈ +1.068716492261707e−1070 (box radii ≤ 6e−1121): a real zero
  in (3144.8946, 3144.8947).
- **(H2)** For c = 3143.2206824215 + 0.3152587994 i and S_r = c + [−r, r]², the winding number of Ξ₂₇ along ∂S_r is **k = 1** for
  r = 10⁻³ and for r = 10⁻⁵, 10⁻⁷, 10⁻⁹, 10⁻¹⁰, 5·10⁻¹¹, 4·10⁻¹¹, **3.7·10⁻¹¹ (smallest reached)**; k = 0 for r = 3.5·10⁻¹¹ (the zero
  sits just outside that square). So Ξ₂₇ has exactly one zero z₀ (simple) in the open square S_r for every such r.
- **(H2\*)** Re-centred at z* = 3143.220682421536585287281295989417800119257644961983569 + 0.3152587993782148453822863730092717652956513976685290909 i,
  the winding number is 1 on z* + [−r, r]² for r = 10⁻³⁰, 10⁻⁴⁰, 10⁻⁴⁵, 10⁻⁴⁸: **z₀ ∈ z* + [−10⁻⁴⁸, 10⁻⁴⁸]²** (NOTE §4's 22 digits agree).
- **(H3)** With r = 10⁻³: Im z₀ > 0.3142587994 > 0 and Re z₀ < 3143.2216824215 < 3144.8946 < x₁, x₁ the real zero of (H1). In Q, z₀
  precedes x₁ by real part but has the larger imaginary part: Ξ₂₇ does not have monotonic zeros in Q — **Conjecture 1 is false for
  N = 27**, and so is the weak form (Remark 1): z₀ is a non-real zero in Q with real part below the real zero x₁ ≤ largest real zero.
- **(H4)** Ξ₂₇(3145.5998) ∈ +1.129756942916642e−1070, Ξ₂₇(3145.5999) ∈ −1.149139153627783e−1070: a second real zero in (3145.5998, 3145.5999).
- Control (same model): square c + 0.01 + [−10⁻³, 10⁻³]² has winding number 0.

## A. Objects and identities (Haglund arXiv:0910.5228, text on disk `../../novel-wave-s36/staircase/lit/haglund-0910.5228.txt`)

- **A1 (definitions, pp. 1–3: (1), (6), (10), (11), (13), (14)).** Ξ(z) = ½(½+iz)(−½+iz)π^{−(½+iz)/2}Γ(½(½+iz))ζ(½+iz) = ξ(s);
  G(z; a, b) = Γ(b+iz, a)/a^{b+iz} + Γ(b−iz, a)/a^{b−iz}, Γ(w, a) = ∫_a^∞ e^{−t}t^{w−1}dt. With X = πn² and
  h(w) := X^{−w}Γ(w, X) = ∫₁^∞ e^{−Xu}u^{w−1}du (substitute t = Xu), and b ± iz/2 = b − ¼ ± (s − ½)/2:
  **Φ_n(z) = 2X²[h(s/2 + 2) + h((1−s)/2 + 2)] − 3X[h(s/2 + 1) + h((1−s)/2 + 1)]** (2π²n⁴ = 2X², 3πn² = 3X). This literal form is what
  `xin.Phi` evaluates (no reduction identity is used).
- **A2 (Haglund (12), p. 3).** Ξ(z) = Σ_{n≥1} Φ_n(z), hence **Ξ_N = Ξ − Σ_{n>N} Φ_n** (the tail route; no cancellation at N = 27:
  |Ξ| ≈ |Φ₂₈| ≈ 1.5e−1066, |Φ₂₉| ≈ 1e−1143). Checked numerically, not assumed blindly: literal (13) and tail route overlap at N = 1, 2
  (ladder, 16 digits) and at N = 27 (§E, X3).
- **A3 (reality).** By (6) G(z; a, b) = 4∫₀^∞ cos(2zu) e^{2bu − ae^{2u}}du is real for real z, so Φ_n and Ξ_N are real and continuous
  on ℝ: strict opposite signs of the real parts of two enclosures give a real zero in between (intermediate value theorem).

## B. Every analytic bound used (proved here, or cited from a DLMF page saved on disk in `lit/`, read 2026-09-30)

- **B1 Γ (Stirling; `specfun._stirling`, `lngamma`).** DLMF 5.11.1 and 5.11(ii) (`lit/dlmf-5.11.txt`): Ln Γ(w) = (w−½)ln w − w + ½ln 2π
  + Σ_{k=1}^{K−1} B_{2k}/(2k(2k−1)w^{2k−1}) + R_K, with |R_K| ≤ sec^{2K}(½ ph w)·|B_{2K}|/(2K(2K−1)|w|^{2K−1}) ("bounded in magnitude by
  sec^{2n}(½ph z) ... times the first neglected terms"). We use it only for Re w > 0, where sec²(½θ) = 2/(1 + cos θ) and
  cos θ = Re w/|w| ≥ Re w_min/|w|_max. If |w| ≥ 300 and Re w ≥ 0: K = 20, no shift (at |w| ≈ 1571.6 the bound is 2.9e−106).
  Otherwise Γ(w) = Γ(w+m)/Π_{j<m}(w+j) with Re(w+m) ≥ 45, K = 30, the product taken as Σ principal logs of boxes off the negative
  axis (`ivc.clog_gen`; any 2πi ambiguity vanishes on exponentiation).
- **B2 ζ (Euler–Maclaurin; `specfun.zeta_em`).** DLMF 2.10.1 (`lit/dlmf-2.10.txt`) with f(x) = x^{−s}, a = N, n → ∞ (σ > 1; both sides
  are then analytic for σ > 1 − 2m, s ≠ 1, since the remainder integral converges absolutely and locally uniformly there — the same
  formula is DLMF 25.2.9 in another normalization): ζ(s) = Σ_{n<N} n^{−s} + N^{1−s}/(s−1) + ½N^{−s}
  + Σ_{k=1}^{m−1} B_{2k}(s)_{2k−1}N^{1−s−2k}/(2k)! + R_m, R_m = ∫_N^∞ (B_{2m} − B̃_{2m}(x))(s)_{2m}x^{−s−2m}dx/(2m)!, (s)_j = s(s+1)⋯(s+j−1).
  DLMF 24.9.2 (`lit/dlmf-24.9.txt`): |B_{2m}(x) − B_{2m}| ≤ (2 − 2^{1−2m})|B_{2m}| on [0, 1], so
  **|R_m| ≤ (2 − 2^{1−2m})|B_{2m}|·|(s)_{2m}|·N^{1−σ−2m}/((2m)!(σ + 2m − 1))**. N = max(40, ⌈|s|/π⌉ + 10) (1012 at N = 27), m chosen
  adaptively until the bound is ≤ 2^{−190} (m = 94, bound 2.6e−58 at N = 27).
- **B3 h by integration by parts (`specfun.h_ibp`).** For any complex c, ∫₁^∞ e^{−Xu}u^c du = e^{−X}/X + (c/X)∫₁^∞ e^{−Xu}u^{c−1}du
  (boundary term at ∞ vanishes). Induction with c = w − 1: h(w) = e^{−X}Σ_{k<K} τ_k + ρ_K, τ_k = (w−1)(w−2)⋯(w−k)/X^{k+1},
  ρ_K = X^{−K}(w−1)⋯(w−K)∫₁^∞ e^{−Xu}u^{w−1−K}du. With β = Re w − 1 − K: u^β ≤ 1 if β ≤ 0, and u^β ≤ e^{β(u−1)} if β > 0
  (ln u ≤ u − 1); hence **|ρ_K| ≤ e^{−X}|τ_K|·X/(X − max(β, 0))** for X > max(β, 0). At n = 28 (X = 784π, |Im w| ≈ 1572) the
  ratio |w − k|/X ≈ 0.64, and K ≈ 300 terms reach 2^{−190}.
- **B4 h by Γ minus the lower series (`specfun.h_lower`).** For Re w > 0, γ(w, X) := ∫₀^X t^{w−1}e^{−t}dt = Γ(w) − Γ(w, X), and
  integration by parts gives γ(w, X) = X^w e^{−X}/w + γ(w+1, X)/w, so γ(w, X) = X^w e^{−X}Σ_{k<K}X^k/(w)_{k+1} + γ(w+K, X)/(w)_K;
  both sides are meromorphic on Re w > −K, so the identity holds there (w ∉ {0, −1, …}). Hence
  h(w) = X^{−w}Γ(w) − e^{−X}Σ_{k<K}X^k/(w)_{k+1} − X^{−w}γ(w+K, X)/(w)_K. If c := Re w + K ≥ X + 1, t^{c−1}e^{−t} is nondecreasing on
  [0, X] (derivative t^{c−2}e^{−t}(c−1−t)), so |γ(w+K, X)| ≤ X·X^{c−1}e^{−X}; with |X^{−w}| = X^{−Re w}:
  **remainder ≤ e^{−X}X^K/|(w)_K|**. (Used for small X in the ladder, and in cross-check X2/X3.)
- **B5 tail n > M (`xin.tail_bound`).** From B3 with K = 0 (or directly): |h(w)| ≤ e^{−X}/(X − β_w), β_w = max(Re w − 1, 0). Let
  β = max over the four arguments of A1 and the input box. For X ≥ max(2β, 12): 1/(X − β) ≤ 2/X, so
  |Φ_n| ≤ e^{−X}(2X²·4/X + 3X·4/X) = (8X + 12)e^{−X} ≤ 9Xe^{−X} =: a_n. For n ≥ 2, a_{n+1}/a_n = ((n+1)/n)²e^{−π(2n+1)} ≤ 2.25e^{−5π} < ½,
  so **|Σ_{n>M} Φ_n| ≤ 2a_{M+1} = 18π(M+1)²e^{−π(M+1)²}** (hypotheses checked in code). M = smallest ≥ N+3 with bound ≤ 1e−80:
  M = 30 at N = 27 (bound 3.7e−1307), M = 7 at N = 1, 2 (bound 1.7e−84).
- **B6 Taylor model (`winding.taylor_model`, `model_error`).** f = Ξ_N is entire; f(z) = Σ a_k(z−c)^k with **|a_k| ≤ M_R/R^k**
  (Cauchy's inequality from the integral formula on |z−c| = R), M_R ≥ max_{|z−c|=R}|f|. M_R is the largest upper modulus of the box
  enclosures of f on nbox boxes covering the circle: each arc of angle 2π/nbox lies within distance R(1 − cos(π/nbox)) (the sagitta)
  of its chord, hence inside the chord's bounding box widened by that amount. DFT on m points ζ_j = c + ρω^j, ω = e^{2πi/m}:
  inserting the (absolutely convergent) series and using Σ_j ω^{j(i−k)} = m·[i ≡ k mod m],
  **D_k := (1/m)Σ_j f(ζ_j)ω^{−jk}ρ^{−k} = Σ_{l≥0} a_{k+lm}ρ^{lm}** (0 ≤ k < m), so |D_k − a_k| ≤ (M_R/R^k)q^m/(1−q^m), q = ρ/R.
  For |z − c| ≤ r' < R, with x = r'/R:
  **|f(z) − Σ_{k<K} D_k(z−c)^k| ≤ E := M_R[q^m/(1−q^m)·Σ_{k<K}x^k + x^K/(1−x)]**. The D_k are computed in interval arithmetic from
  point enclosures of f on boxes containing ζ_j (ω^{−jk} enclosed too), so each D_k is a box containing the exact D_k.
- **B7 boundary walk (`winding.winding`).** ∂S (counterclockwise) is cut into segments; for a segment σ with end points p, p′ the model
  gives enclosures F_σ = P(box(σ)) + [−E, E]², F_p, F_{p′} (P = Σ_{k<K}D_k(z−c)^k by interval Horner; r' ≥ |sc − c| + √2 r).
  Lemma: if f(σ) ⊂ K with K convex, compact and 0 ∉ K, then K lies in an open half-plane through 0, a continuous argument of f
  varies along σ inside an interval of length < π, and its net change is the principal value of arg(f(p′)/f(p)) ∈ (−π, π).
  The code requires 0 ∉ F_σ (a rectangle, convex) and Re(F_{p′}/F_p) > 0, and then encloses the change by atan2(Im, Re) of the ratio
  box; otherwise it bisects the segment (≤ 14 levels, else it reports failure). The increments are summed in interval arithmetic;
  k is certified when the interval (sum)/2π contains exactly one integer (width < 1). By the argument principle (f entire, f ≠ 0 on
  ∂S) k = number of zeros of f in the open square, counted with multiplicity.
- **B8 arithmetic.** mp.iv intervals with outward rounding for +, −, ×, ÷, sqrt, exp, log, cos, sin, atan2 (atan2 used only as
  atan(u) = atan2(u, 1) and for boxes in Re > 0; `ivc.clog_gen` checked on 3000 random boxes × 5 sample points against mpmath's log, 0 violations — `selftest.py`).
  Complex products/quotients are formed from real interval operations (rectangular boxes; |z|² via a sign-aware square).
  Decimal inputs enter as intervals containing the exact decimal (`iv.mpf('3144.8946')`); circle points, π, ω^j are enclosed;
  Bernoulli numbers are exact Fractions (recurrence Σ_{j≤n} C(n+1, j)B_j = 0, spot-checked against B₂…B₁₂, B₂₄, B₆₀).
  Comparisons use exact interval end points (`ivc.lo/hi`), never iv's three-valued `<`.

## C. Ladder (specification §4), run BEFORE N = 27 with the same functions (`ladder.py` → `logs/ladder.log`, 118 s)

| item | claim | certified enclosures / result |
|---|---|---|
| R1, N = 1 | real zero in (14.04543957, 14.04543959) | Ξ₁ ∈ +1.347060456146727e−11 / −1.704102125314551e−11 (tail M = 7; literal overlaps) |
| R1, N = 2 | real zero in (39.5324810797, 39.5324810799) | Ξ₂ ∈ +3.605517254360067e−21 / −4.5934187710153e−21 (literal overlaps) |
| R2 | Haglund Appendix zero 20.62534600592171760132974 + 2.697151842339519632505712 i | k = 1 at r = 1e−3 and 1e−8 (R = 0.5, ρ = 0.01, m = 24, K = 12; E = 8.7e−26 / 5.5e−36 vs min over pieces of the lower modulus 8.1e−8 / 8.2e−13) |
| R3 | control square 17 + i + [−¼, ¼]² (no zero in Haglund's list) | k = 0 (sum/2π ∈ [−1.3e−5, 1.3e−5]; R = 1.5, ρ = 0.6, m = 48, K = 24) |

R2's model zero (non-rigorous Newton on the model, 220 bits): 20.62534600592171760132995 + 2.697151842339519632505936 i —
Haglund's 25-digit Appendix value agrees to ≈ 2e−22. The ladder exercised every component: Stirling with shift (small |w|), Euler–Maclaurin at low height, h by the lower series
(n ≤ 6) and by integration by parts (n = 7), the tail bound, the Taylor model and the boundary walk (both outcomes k = 1 and k = 0).

## D. N = 27 details (`cert27.py` → `logs/cert27.log`, 56 s incl. H2\* and X4)

- Tail route: Ξ₂₇ = Ξ − Φ₂₈ − Φ₂₉ − Φ₃₀ − T₃₀; ζ: N = 1012, m = 94; h for n = 28–30 always by B3 (no fallback needed).
  |Ξ(3144.8946)| = 1.4923145335789e−1066, |Φ₂₈| = 1.49249055304208e−1066: the tail route resolves Ξ₂₇ ≈ 1e−1070 with ≈ 50 spare digits.
- H2 model at c: M_R = 2.09255e−1065 (R = 0.1, 32 boxes); ρ = 0.002, m = 24, K = 12; aliasing term M_R q^m/(1−q^m) = 3.5e−1106.
  D₀ = (1.65573706402 + 2.01786756791 i)e−1076 (= the direct enclosure of f(c) to all digits shown; consistency checked),
  D₁ = (−0.91645674419 − 6.06123185485 i)e−1066 (|Ξ₂₇′(c)| ≈ 6.13e−1066).

| r | pieces | E | min lower modulus over pieces | k |
|---|---|---|---|---|
| 1e−3 | 32 | 1.36e−1087 | 5.89e−1069 | 1 |
| 1e−5, 1e−7, 1e−9 | 32 each | 3.51e−1106 | 5.90e−1071, 5.90e−1073, 5.68e−1075 | 1 |
| 1e−10, 5e−11, 4e−11 | 32, 32, 33 | 3.51e−1106 | 3.67e−1076, 7.41e−1077, 1.78e−1077 | 1 |
| 3.7e−11 | 36 | 3.51e−1106 | 1.97e−1078 | 1 |
| 3.5e−11 | 33 | 3.51e−1106 | 5.75e−1078 | 0 |
| control: c + 0.01, 1e−3 | 32 | 1.16e−1076 | 5.46e−1068 | 0 |

- H2\*: second model at z* (ρ = 0.001, m = 40): E = 2.09e−1145; k = 1 for r = 1e−30, 1e−40, 1e−45, 1e−48 (at 1e−48 the lower
  modulus 5.9e−1114 still exceeds the point-enclosure radii ≈ 1e−1120 by 10⁶). Location: z₀ ∈ z* + [−1e−48, 1e−48]².

## E. Cross-checks (not load-bearing; `crosscheck.py X1 X2` / `X3` → `logs/crosscheck-X1X2.log` / `-X3.log`; `selftest.py`)

- **X3 — a second rigorous route for H1/H4.** The literal sum (13), Σ_{n≤27} Φ_n, at 4400 bits: Φ₁…Φ₂₇ via B4 (and B3 where it
  converges), Γ via B1; no ζ, no Euler–Maclaurin, no identity (12). The terms are ≈ 1e−9 and cancel over ≈ 1061 digits:

| x | literal (13), radius ≈ 1–2e−1171 | tail route, radius ≤ 6e−1121 | overlap / same sign |
|---|---|---|---|
| 3144.8946 | −1.760194631277516e−1070 | −1.760194631277516e−1070 | yes / yes |
| 3144.8947 | +1.068716492261707e−1070 | +1.068716492261707e−1070 | yes / yes |
| 3145.5998 | +1.129756942916642e−1070 | +1.129756942916642e−1070 | yes / yes |
| 3145.5999 | −1.149139153627783e−1070 | −1.149139153627783e−1070 | yes / yes |

  They also agree with the specification's Arb reference values (−1.76019463128e−1070, +1.06871649226e−1070, +1.12975694292e−1070,
  −1.14913915363e−1070) to all 12 digits given. X4 (`cert27.py`): at the specification's 22-digit point z₂₂ the enclosure is
  Ξ₂₇(z₂₂) ∈ 2.57878203163e−1085 + 1.7049877229e−1084 i (specification: 2.58e−1085 + 1.70e−1084 i; = D₁·(z₂₂ − z*) to 4 digits).
- **X1.** The Ξ boxes (Stirling + E–M) contain mpmath's ordinary 400-bit ζ·Γ values at the four points and at c.
- **X2.** h at X = 784π (the four arguments of Φ₂₈(c)): B3 at 200 bits (relative radius 2.8e−57) and B4 at 4400 bits (≈ 1e−106,
  the Stirling bound) overlap for all four. (At 1400 bits B4's box was useless: ~5000 box rotations in u_k = u_{k−1}X/(w+k) wrap.)
- **Ladder-level identity checks.** Tail route = literal (13) at N = 1, 2 (16 digits), and for the seed chain tail = defining sum
  at N = 1, 2 (`cert_h5.py` (L)): identity (12) and Riemann's formula behave as used.
- **selftest.py** PASSED: exact Bernoulli numbers vs mpmath, `clog_gen` 0 violations on 15000 samples, and Γ, ζ, h, Ξ, Φ_n
  boxes contain mpmath's ordinary values (low height and N = 27 height).

## H5 (optional, done after H1–H3): the seed chain ξ₂₄ (`cert_h5.py` → `logs/cert_h5.log`, 17 s)

ξ_N(s) = ½ + ½s(s−1)Σ_{n≤N} g_n(s), g_n = h(s/2) + h((1−s)/2) (staircase NOTE §1). Evaluated as ξ₂₄ = ξ − ½s(s−1)Σ_{24<n≤27} g_n − T,
|T| ≤ 4|s(s−1)|e^{−X₀}/X₀, X₀ = 784π (proof as B5: |h| ≤ 2e^{−X}/X, ratio of consecutive bounds < ½), using Riemann's
ξ = ½ + ½s(s−1)Σ_{n≥1} g_n (NOTE §1 derivation; checked: tail = defining sum at N = 1, 2). ξ_N(1−s) = ξ_N(s) and
ξ_N(s̄) = conj ξ_N(s) (X real), so ξ₂₄(½+it) is real. Certified: sign changes on (2510.2026, 2510.2027)
[+2.813175361644763e−854 → −1.65267129214774e−854] and (2510.7086, 2510.7087) [−3.232811395053649e−854 → +6.141840615423139e−855];
winding number 1 of z ↦ ξ₂₄(½+iz) on c5 + [−r, r]², c5 = 2508.2839748053 + 0.3159896243 i, for r = 10⁻³, 10⁻⁶, 10⁻⁹, 10⁻¹⁰
(model R = 0.1, ρ = 0.002, m = 24, K = 12; M_R = 4.07e−849; at r = 10⁻³: min lower modulus 1.16e−852 vs E = 2.6e−871); control
c5 + 0.01: k = 0. Model zero s = 0.184010375695657531105913643468 + 2508.28397480532415320152284309 i (mirror of NOTE §4's ρ₂₄).
Hence ξ₂₄ has a non-real zero in Q (z-variable) with real part < 2508.285 < 2510.2026 < a real zero: the ordering invariant fails.

## F. Reproduction, run times, versions

`cd producer-B && python3 selftest.py && python3 ladder.py && python3 cert27.py && python3 cert_h5.py && python3 crosscheck.py X1 X2
&& python3 crosscheck.py X3` (one process at a time; Apple M4 (Mac16,10), macOS 27.0.1, single core). Times: selftest 2 s, ladder 118 s,
cert27 56 s, cert_h5 17 s, crosscheck X1X2 16 s, X3 664 s. Python 3.9.6; mpmath 1.3.0, backend `python` (no gmpy);
no Arb, no python-flint, no other numerical library. Working precision 200 bits (4400 bits in X2/X3); every truncation bound
targets 2^{−190}. Logs: `logs/selftest.log`, `ladder.log`, `cert27.log`, `cert_h5.log`, `crosscheck-X1X2.log`, `crosscheck-X3.log`
(`crosscheck-run1-X2invalid.log` kept for the record: same X3 values; its X2 used 1400 bits and is void).

What is NOT proved here (scope): correctness of mpmath's primitive interval operations (trusted as the specification allows); Haglund's
identity (12) and Riemann's formula are cited (on disk) and checked numerically, not re-derived; the ladder's R3 "no zero" is by
Haglund's list, and our own k = 0 there is the certified statement.
