# NOTE — Haglund's Conjecture 4: what the pencil Ξ_k + tΦ_{k+1} is, and what decides the motion of its zeros

**Status: the orchestrator's theory note, opened 16:13 IST 2026-10-03. NOT YET READ by a second model; every statement below is "claimed" until `read-O.md` exists (W3). §0 is written last.**

Objects (Haglund, arXiv:0910.5228v1, (1)–(14)): Ξ(z) = ξ(½ + iz); Φ_n; Ξ_N = Σ_{n≤N} Φ_n; Q_N := Σ_{n>N} Φ_n = Ξ − Ξ_N (entire; the series converges locally uniformly, his (12)). The pencil: F_t := Ξ_k + tΦ_{k+1}, 0 ≤ t ≤ 1, k ≥ 1; u := 1 − t. Throughout, "the paper" is `results/arxiv/haglund-counterexample/main.tex`.

The two parts of the target (ORCH-NOTES N0): (D) along a branch of zeros in the open upper half-plane, Im z does not increase with t; (R) a real zero stays real as t increases.

## 1. The kernel form and the level (proved)

From the paper (Theorem sandwich and its proof): Φ_n(z) = 2∫_0^∞ φ̃_n(v) cos(zv) dv for every complex z, where φ̃_n(v) = 2y(2y − 3)e^{v/2 − y}, y = πn²e^{2v}; and for n ≥ 2 the function φ̃_n is positive, strictly decreasing and strictly convex on [0, ∞). (For n = 1 it is positive but not monotone at 0.)

**Lemma 1.1.** For n ≥ 2 and real x, Φ_n(x) > 0.
Proof. The Pólya argument of the paper's Theorem positivity applied to the single kernel φ̃_n: for x ≠ 0, ∫_0^∞ φ̃_n cos(xv) dv = x^{−1}∫_0^∞ (−φ̃_n′)(v) sin(xv) dv with −φ̃_n′ positive and strictly decreasing, so the half-period pieces alternate with strictly decreasing sizes, the first positive; at x = 0 the integral of a positive function. ∎

**Lemma 1.2 (the pencil is Ξ minus a positive level).** For k ≥ 1 and all z,
  F_t(z) = Ξ(z) − L_t(z),  L_t := uΦ_{k+1} + Q_{k+1} = 2∫_0^∞ κ_t(v) cos(zv) dv,  κ_t := uφ̃_{k+1} + Σ_{n>k+1} φ̃_n.
For 0 ≤ u ≤ 1 the kernel κ_t is positive, strictly decreasing and strictly convex, so L_t(x) > 0 for real x; and ∂F_t/∂t = Φ_{k+1}, which is positive on the real axis.
Proof. Ξ_k = Ξ − Q_k and Q_k = Φ_{k+1} + Q_{k+1}; the kernel properties are termwise (all indices are ≥ 2); Lemma 1.1. ∎

**Lemma 1.3 (the quotient form).** Let S_k := Ξ_{k+1}/Φ_{k+1} (meromorphic; real on the real axis, where Φ_{k+1} > 0). Then F_t(z) = 0 ⟺ S_k(z) = u at every z with Φ_{k+1}(z) ≠ 0, and at a common zero of Ξ_{k+1} and Φ_{k+1} the pencil vanishes for every t. Along a branch of simple zeros z(t) with Φ_{k+1}(z) ≠ 0,
  dz/dt = −Φ_{k+1}(z)/∂_zF_t(z) = −1/S_k′(z),  so  d(Im z)/dt = Im S_k′(z)/|S_k′(z)|².
Hence (D) for k is the statement: Im S_k′(z) ≤ 0 at every z with Im z > 0 and S_k(z) ∈ (0, 1) [together with the behavior at multiple zeros].
Proof. F_t = Ξ_{k+1} − uΦ_{k+1}; differentiate S_k(z(t)) = 1 − t. ∎

## 2. The real axis (proved, unconditional), and what (R) needs

**Theorem 2.1.** Let k ≥ 1 and 0 ≤ t ≤ 1.
(a) For real x, F_t(x) = Ξ(x) − L_t(x) with L_t(x) > 0, and t ↦ F_t(x) is strictly increasing.
(b) Every real zero of F_t lies in an open interval on which Ξ > 0. Counted with multiplicity, each positive lobe (γ_j, γ_{j+1}) of Ξ contains an even number of zeros of F_t and the central lobe (0, γ_1) an odd number; the number of zeros of F_t in (0, ∞) is finite and odd.
(c) The sets P_t := {x ∈ ℝ : F_t(x) > 0} increase with t: P_s ⊂ P_t for s < t, and every boundary point of P_s lies in the interior of P_t.
(d) Local picture at a real zero x_0 of F_{t_0} of multiplicity m. If m is odd, F_t has an odd number of real zeros near x_0 for t near t_0. If m = 2 and F_{t_0} ≤ 0 near x_0 (a local maximum with value 0), then for t slightly above t_0 there are two simple real zeros near x_0 and for t slightly below there are none (a conjugate pair ARRIVES: a landing). If m = 2 and F_{t_0} ≥ 0 near x_0 (a local minimum with value 0), then for t slightly below t_0 there are two real zeros near x_0 and for t slightly above there are none (a conjugate pair LEAVES the axis: a lift-off).
(e) Hence (R) holds for k if and only if no F_t, 0 < t < 1, has a real zero of even multiplicity at which it is locally non-negative; equivalently, no two components of P_t merge as t increases; equivalently, x ↦ S_k(x) has no local minimum with value in (0, 1) at which it is locally ≥ that value on both sides.
Proof. (a) Lemma 1.2. (b) Where Ξ ≤ 0, F_t = Ξ − L_t < 0, in particular at every γ_j; at 0, F_t(0) ≥ Ξ_1(0) > 0 because F_t − Ξ_1 = Σ_{2≤n≤k} Φ_n + tΦ_{k+1} ≥ 0 at real points and Ξ_1(0) = Ξ(0) − Q_1(0) ≥ 0.4971 − c_1 > 0 (the paper, Corollary odd); for large x, x²F_t(x) tends to a negative limit — the paper's Proposition tail applied to the kernel κ_t gives lim x²L_t(x) = −2κ_t′(0) > 0 — so the zeros in [0, ∞) lie in a bounded set and are finite in number; parity from the signs at the ends of each lobe. (c) F_s(x) > 0 implies F_t(x) > F_s(x) > 0; a boundary point of P_s has F_s = 0 there, so F_t > 0 there. (d) F_t(x) = F_{t_0}(x) + (t − t_0)Φ_{k+1}(x) with Φ_{k+1}(x_0) > 0: near x_0 this is c(x − x_0)^m(1 + o(1)) + (t − t_0)Φ_{k+1}(x_0)(1 + o(1)), and the three cases are read off (Weierstrass preparation gives exactly m zeros near x_0, real or in conjugate pairs). (e) from (d); in terms of S_k: F_t(x) = Φ_{k+1}(x)(S_k(x) − u) on the real axis. ∎

Remark 2.2 (what the theorem does not give). Zeros of multiplicity ≥ 3 and the case m even ≥ 4 are covered by the same expansion but are not spelled out; they do not occur in any computation so far. Theorem 2.1 does not decide (R): it reduces it to the absence of a local minimum of S_k with value in (0, 1).

**Proposition 2.3 ((R) from the real zeros of Ξ; conditional).** Assume every zero of Ξ is real. If F_{t_0} has a lift-off at x_0 (Theorem 2.1(d), third case), then
  −(log L_{t_0})″(x_0) ≥ Σ_{γ>0} [ (x_0 − γ)^{−2} + (x_0 + γ)^{−2} ].
Proof. At a lift-off Ξ = L, Ξ′ = L′ and Ξ″ ≥ L″ at x_0, with L = L_{t_0} > 0; so (log Ξ)″(x_0) = Ξ″/Ξ − (Ξ′/Ξ)² ≥ L″/L − (L′/L)² = (log L)″(x_0). With only real zeros, Ξ(z) = Ξ(0)∏_{γ>0}(1 − z²/γ²) (Ξ is even, of order 1, and Σγ^{−2} converges), so (log Ξ)″(x) = −Σ_{γ>0}[(x − γ)^{−2} + (x + γ)^{−2}]. ∎
So (R) follows, under that hypothesis, from the inequality −(log L_t)″(x) < Σ_{γ>0}[(x − γ)^{−2} + (x + γ)^{−2}] at the real points where Ξ = L_t. The right side is at least 2Σγ^{−2} = 0.0462… in the central lobe and at least (γ_{j+1} − γ_j)^{−2} in the lobe (γ_j, γ_{j+1}); the left side is of the order of the squared width of the kernel κ_t, about 1/(2π²(k+1)⁴) (HEURISTIC size; a proved bound for −(log L_t)″ is not in this note — it is the one estimate a proof of (R) for a range of k would need, and a hypothesis on the zeros of Ξ up to a finite height would do, the zeros above contributing a small error).

## 3. Off the axis: the frozen-level model (proved under the hypothesis that the zeros of Ξ are real)

**Lemma 3.1 (classical; a printed source is asked of `L-lit`).** Let f be a real entire function of the form f(z) = Cz^m e^{−az² + bz}∏_j(1 − z/a_j)e^{z/a_j} with a ≥ 0, b and the a_j real, Σ a_j^{−2} < ∞, and at least one zero or a > 0. Then Im f′(z)/f(z) < 0 for Im z > 0. If c ≠ 0 is real and z(c) is a branch of simple solutions of f(z) = c in the open upper half-plane, then d(Im z)/d|c| > 0: as |c| decreases, the solution moves toward the real axis.
Proof. f′/f = m/z − 2az + b + Σ_j[1/(z − a_j) + 1/a_j], and each term m/z, −2az, 1/(z − a_j) has non-positive imaginary part for Im z > 0, with strict inequality for at least one. Then dz/dc = 1/f′(z) = (1/c)·(f/f′)(z) because f(z) = c, and Im(f/f′) = −Im(f′/f)/|f′/f|² > 0. ∎

**Proposition 3.2 (the solutions of Ξ = c when the zeros of Ξ are real).** Assume every zero of Ξ is real and simple, 0 < γ_1 < γ_2 < ⋯ the positive ones, and let M_m be the maximum of Ξ over the m-th positive lobe (γ_{2m}, γ_{2m+1}), m ≥ 1.
(i) For every y > 0 the continuous argument of Ξ along the horizontal line through iy, normalized by arg Ξ(iy) = 0, is strictly decreasing in x and tends to −∞; so for each m ≥ 1 there is exactly one point x_m(y) + iy with x_m(y) > 0 and arg Ξ = −2πm. The curves C_m := {x_m(y) + iy : y > 0} are disjoint real-analytic graphs over the y-axis, and {z : Re z > 0, Im z > 0, Ξ(z) > 0} = ∪_{m≥1} C_m.
(ii) Along C_m the positive number Ξ is strictly increasing in y; as y → 0 the curve tends to the critical point of Ξ in the m-th positive lobe and Ξ → M_m.
(iii) Hence for a constant c > 0: the zeros of Ξ − c in the open first quadrant are in bijection with the positive lobes with M_m < c (one zero on each such C_m; none on the others, which carry two real zeros of Ξ − c in the lobe when M_m > c). As c decreases each such zero moves down its own curve C_m, strictly monotonically in Im z, and reaches the real axis exactly when c = M_m, at the critical point of the lobe.
Proof. (i) ∂_x arg Ξ(x + iy) = Im Ξ′/Ξ < 0 by Lemma 3.1 (Ξ(z) = Ξ(0)∏(1 − z²/γ²) under the hypothesis); it is ≤ −Σ_γ y/((x − γ)² + y²), whose integral over x diverges because there are infinitely many γ. Ξ(iy) = 2∫ Σφ̃_n(v) cosh(yv) dv > 0. The implicit function theorem gives the graphs. (ii) Ξ′ ≠ 0 off the real axis (Lemma 3.1), so Ξ, real on C_m, is strictly monotone along it; by Lemma 3.1 applied to the branch through any point of C_m the monotonicity is "increasing with y". A point x* of the real axis that is not a critical point and not a zero of Ξ has a neighborhood on which Ξ is injective and maps the real axis onto the real values, and near a simple zero the same holds; so C_m can only approach the real axis at a critical point with Ξ > 0, and by the value of the argument on the axis (−2πm on the m-th positive lobe) it is the one of that lobe. (iii) from (i), (ii). ∎

**What this says about the pencil.** By Lemma 1.2 the zeros of F_t are the solutions of Ξ(z) = L_t(z). If L_t were a constant c that decreases with t, (D) and (R) would be exactly Proposition 3.2(iii): every non-real zero descends, each lands at the top of its own lobe when the level passes that top, and landed zeros stay real. The order in which the lobes are reached is the order of their heights M_m, not of their positions — which is the failure of Conjecture 1 (a low lobe to the left of a higher one), and it is compatible with (D): the zero over the low lobe is still descending when the zeros of the higher lobe to its right have landed. The true level L_t(z) is not constant: on the real axis it varies on the scale 2π(k+1)², and off the axis it has a small phase. §5 lists what is and is not controlled.

**Exact form of the criterion (no hypothesis).** At a simple zero z of F_t with Im z > 0, Ξ(z) = L_t(z) ≠ 0 (if Φ_{k+1}(z) ≠ 0 … see Lemma 1.3) and
  dz/dt = −ρ(z)/Λ(z),  ρ := Φ_{k+1}/L_t,  Λ := Ξ′/Ξ − L_t′/L_t,
so the zero descends if and only if Im(ρ/Λ) > 0. In the frozen model ρ > 0 and Λ = Ξ′/Ξ.

## 4. What a zero of Ξ off the real axis would do (proved, unconditional)

**Lemma 4.1 (Φ_n is nearly constant on a fixed disc).** Let R > 0 and n ≥ 2 with πn² ≥ R + ½. Then for |z| ≤ R,
  |Φ_n(z)/Φ_n(0) − 1| ≤ 3.1 R²/(π²n⁴).
Proof. Put X = πn². |cos(zv) − 1| ≤ cosh(Rv) − 1 ≤ ½R²v²e^{Rv} for v ≥ 0. With y = Xe^{2v} (so v = ½ log(y/X), dv = dy/2y) one has φ̃_n(v) dv = (2y − 3)(y/X)^{1/4}e^{−y} dy. Hence ∫_0^∞ φ̃_n dv ≥ ∫_X^∞(2y − 3)e^{−y} dy = (2X − 1)e^{−X}. With w = y − X: log(y/X) ≤ w/X and (y/X)^{1/4 + R/2} ≤ e^{(1/4 + R/2)w/X} ≤ e^{w/2} because X ≥ ½ + R; so
  ∫_0^∞ φ̃_n(v)·½R²v²e^{Rv} dv ≤ (R²/8X²) e^{−X}∫_0^∞(2X + 2w)w²e^{−w/2} dw = (R²/8X²)(32X + 192)e^{−X}.
The quotient is at most (R²/8X²)(32X + 192)/(2X − 1) ≤ 3.1R²/X² for X ≥ 4π. ∎

Consequences, for a fixed disc |z| ≤ R and k → ∞, uniformly in 0 ≤ t ≤ 1: Φ_{k+1}(z)/Φ_{k+1}(0) → 1; sup|L_t| ≤ Σ_{n>k} sup|Φ_n| ≤ Φ_{k+1}(0)(1 + o(1)) → 0 (the ratios Φ_{n+1}(0)/Φ_n(0) tend to 0, since (2X − 1)e^{−X} ≤ ½Φ_n(0) ≤ (2X + 3)e^{−X} for X = πn² ≥ 4π — the upper bound from 2y − 3 ≤ 2y and (y/X)^{1/4} ≤ e^{w/4X}, which give e^{−X}[2X/(1 − ε) + 2/(1 − ε)²] with ε = 1/4X ≤ 0.02); and L_t′ → 0 on any smaller disc (Cauchy).

**Proposition 4.2.** Let β be a simple zero of Ξ with Im β > 0 and Im Ξ′(β) ≠ 0. Then there are a disc D about β and k_0 such that for every k ≥ k_0 and every t ∈ [0, 1] the function F_t = Ξ_k + tΦ_{k+1} has exactly one zero z_k(t) in D, it is simple, t ↦ z_k(t) is continuously differentiable, and
  sign d(Im z_k(t))/dt = sign Im Ξ′(β)  for all t ∈ [0, 1].
In particular, if Ξ had a simple zero β in the open upper half-plane with Im Ξ′(β) > 0, then for every k ≥ k_0 the pencil would have a non-real zero whose imaginary part strictly INCREASES on the whole interval 0 ≤ t ≤ 1: statement (D) of Conjecture 4 would fail for all large k.
Proof. Choose D with closure in the open upper half-plane, containing no other zero of Ξ and no zero of Ξ′, and let δ = min_{∂D}|Ξ| > 0. By the consequences of Lemma 4.1, sup_{D̄}|L_t| < δ for k ≥ k_1 and all t, so by Rouché F_t = Ξ − L_t has exactly one zero z_k(t) in D, simple; it depends continuously differentiably on t by the implicit function theorem, with dz_k/dt = −Φ_{k+1}(z_k)/(Ξ′(z_k) − L_t′(z_k)). As k → ∞, uniformly in t: z_k(t) → β (the zero of Ξ − L_t in D tends to the zero of Ξ as sup|L_t| → 0), Ξ′(z_k) − L_t′(z_k) → Ξ′(β) ≠ 0 and Φ_{k+1}(z_k)/Φ_{k+1}(0) → 1. Therefore
  (1/Φ_{k+1}(0))·dz_k/dt → −1/Ξ′(β)  uniformly on [0, 1],
and Im(−1/Ξ′(β)) = Im Ξ′(β)/|Ξ′(β)|² ≠ 0 has the sign of Im Ξ′(β). ∎

Remarks. (1) The mirror pencil Ξ + L_t (the weights 1, …, 1, 2 − t, 2, 2, … on Φ_1, Φ_2, … — still a series of Haglund's form (53) with non-negative coefficients) has dz/dt = +Φ_{k+1}/(Ξ′ + L_t′), so the sign is reversed: a simple off-line zero with Im Ξ′(β) ≠ 0 produces an ascending branch, for all large k, in exactly one of the two pencils. (2) Not covered: Im Ξ′(β) = 0, and multiple zeros off the axis. For a zero of multiplicity m ≥ 2 the m nearby zeros of F_t sit at β + ((L_t(β)/c)^{1/m})-th roots, c = Ξ^{(m)}(β)/m!, and approach β radially as k grows; at least one approaches from below (so ascends in t) when m ≥ 3, and when m = 2 unless c is a positive real number. This is a sketch, not a proof. (3) Proposition 4.2 concerns large k only; it says nothing about a fixed k. (4) On the hypothesis: by the reflection Ξ(−z̄) = conj Ξ(z), the zero −β̄ has Ξ′(−β̄) = −conj Ξ′(β), with the same sign of the imaginary part; the two mirror zeros behave alike.

**Reading.** Statement (D), for all large k, cannot hold unless Ξ has no simple zero β above the real axis with Im Ξ′(β) > 0; and Proposition 3.2 says that, with the level frozen, the reality of the zeros of Ξ makes (D) and (R) hold. So Conjecture 4 is tied to the same property of Ξ that the Riemann hypothesis asserts, from both sides — in contrast with Conjecture 1, which is a sufficient condition that fails for a reason unrelated to the zeros of Ξ (fluctuating lobe heights).

## 5. The true level: what is controlled and what is not (HEURISTIC unless marked)

Three regimes for a zero z = x + iy of F_t in the first quadrant, in terms of a := π(k+1)² (the second argument of the incomplete gamma functions in Φ_{k+1}):
- **(I) the frontier**, x from about 4(k+1)² to 4(k+2)², y from 0 to a few units. Here Ξ and L_t have comparable size (|Ξ(x)| ≈ e^{−πx/4}x^{7/4} against L_t ≈ uΦ_{k+1}(0) ≈ 4ua e^{−a}), all landings happen here, and L_t is far below the height x ≈ 2a where Φ_{k+1} changes regime (for k ≥ 3: 4(k+2)² < 2π(k+1)²; for k = 1, 2 the regimes overlap). L_t is then slowly varying: its logarithmic derivative is of size x·(1/2a²) (from the second moment of the kernel, about 1/(2a²)), against |Ξ′/Ξ| ≈ ½log(x/2π) and −Im Ξ′/Ξ = y·Σ_γ|z − γ|^{−2}. The criterion Im(ρ/Λ) > 0 of §3 holds with a wide margin in this model; the neglected terms are O(xy/a²) in the phase of ρ and O(x/a²) in Λ.
- **(II) the middle**, x between the frontier and about 2a, on the curve where |Ξ(z)| = |L_t(z)| (it rises like (π/2)(x − x_frontier)/log(x/2)). Above height ½, Ξ(z) = A(½ − iz)ζ(½ − iz) with ζ close to 1, Λ ≈ −π/4 − (i/2)log(x/2π), and the zero descends as long as the phase of ρ stays below arctan(2 log(x/2π)/π) ≈ 1.2. The phase of ρ = Φ_{k+1}/L_t is 0 when u ≫ Q_{k+1}/Φ_{k+1} and at most the phase of Φ_{k+2}(z)/Φ_{k+1}(z) otherwise, which the leading terms of the incomplete gamma functions put at a few hundredths to a tenth of a radian there.
- **(III) far out**, x ≫ 2a: all terms n ≤ k+1 are in their oscillatory regime, the zero condition is A(½ − iz)·D(z) = (the algebraic part) with D close to 1, and the algebraic part is c(t)/z² + O(z^{−4}), c(t) = lim x²F_t(x) = 2κ_t′(0) (Theorem 2.1(b)). PROVED: c(t) < 0 and |c(t)| is strictly decreasing in t, because c(t) = −2[uα_{k+1} + Σ_{n>k+1} α_n] with α_n := −φ̃_n′(0) = (8X³ − 30X² + 15X)e^{−X} > 0 for n ≥ 2 (the paper, Proposition tail). HEURISTIC: a far zero then moves by δz ≈ (δc/c)/(T′/T), T the dominant gamma term, and Im(1/(T′/T)) > 0 there, so a decrease of |c| moves it DOWN. (With the signs printed in the conjecture's source — coefficient of 1/x² positive for N ≥ 3 — the far zeros would have to move UP as t increases; the corrected sign, negative for every N, is the one consistent with Conjecture 4.)
What is NOT in this note: a proof of (D) in any regime for the true level; uniform estimates of Φ_n(z) near x ≈ 2πn² (the transition of the incomplete gamma function); any statement for infinitely many k. The census of the units `A-track` and `B-track` tests (D) and (R) directly in stated windows (§6).
