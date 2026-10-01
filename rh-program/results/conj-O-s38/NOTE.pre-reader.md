# NOTE — unit `conj-O-s38`: the relative square-root law for deletions (Conjecture O)

Session 38, 2026-10-01. Agent: Opus. Brief: `BRIEF.md`. Status labels as in the frontier NOTE: **[proved here]**,
**[computed]** (script + log under `verify/`), **[quoted]** (source on disk, file:line), **[recalled, unverified]**
(load-bearing only where §4 lists it: Stirling's formula for |χ|), **[heuristic]**, **[novelty: single-check]**. Paths `fr/` = `results/novel-wave-s37/beurling-frontier/`.

Notation (the brief's). R ⊂ ℙ with Σ_{p∈R}1/p < ∞; α_R := lim sup log π_R(x)/log x; P = ℙ ∖ R; N_P(x) = #{n ≤ x : (n, p) = 1
∀p ∈ R}; ρ = ρ_R = Π_{p∈R}(1 − 1/p); E(x) = E_R(x) = N_P(x) − ρx = −Σ_{m∈⟨R⟩}μ(m){x/m} (⟨R⟩ = squarefree products of
primes of R); β(R) = inf{β : E = O(x^{β+ε})}. D_R(s) = Π_{p∈R}(1 − p^{−s}) = Σ_{m∈⟨R⟩}μ(m)m^{−s} (absolutely convergent
for σ > α_R), ζ_P = ζ·D_R, P_R(s) := Σ_{p∈R}p^{−s} (the prime zeta function of R). β₂(R) := inf{σ : ∫_1^∞E(x)²x^{−2σ−1}dx < ∞}
(the mean-square exponent; β₂ ≤ β, and (1/X)∫_X^{2X}E² ≫ X^{α_R−ε} i.o. ⟹ β₂ ≥ α_R/2).

## §0. Summary (written at the close) and the digest's ranking of this unit

*The digest's ranking* (`results/novel-wave-s37/insights-digest.md`, on disk from 02:17, §F.2, ll. 359–369): this unit is ranked
**2nd** — "2. **U1 — Conjecture O by the Franel/Landau mean-square route, with a structured-R counterexample hunt** … LAUNCHED …
Why second: its proof branch is RELATIVE — by Prop. 2.3 it cannot bear on ζ, whose own α_R is 0 — so only its refutation branch
touches the line α = 2β that contains RH; still the cheapest theorem-grade unit on the table", with consolidator's notes (i) the
refutation corner is read-O A8 (integer c ≥ 2, α < ¾), (ii) task 1's gap "is the classical Carlson obstruction", (iii) the α = 0.75
tension "is decided by the dyadic mean square, not by more sup-slopes".
*Summary.* **Close G with T-parts.** (1) The reflected identity holds after a correction (coprimality factor (1 − p^{2σ−2}); §1.1)
but is formal: F = ζ(1−s)D_R(s) converges nowhere and E only controls its weighted mean; pushed through a quantitative Carlson
argument it gives β₂ ≥ α_R/4 for every R (RH, α_R < ½; Prop. 1.3), and no growth-only mean-value lemma can reach α_R/2 (Remark 1.3′: such a lemma fails on (α/3, α/2)).
(2) The repair is Hilberdink's: take logarithms. **Theorem Z (RH): if the prime zeta function of R continues past α_R/2 off the real
axis, then β₂(R) ≥ α_R/2.** Every regular deletion qualifies, for every c (Corollary Z.1): the A8 corner is closed as a refutation
corner (consolidator's note (i) answered). (3) The exact missing lemma for general R is Lemma G (§1.6); a counterexample must have
π_R irregular at scale x^{α_R/2} and ζ_P/ζ with infinitely many zeros or poles of real part > α_R/2 − ε, for every ε. (4) Resonance: a named
obstruction (sub-polynomial large values); its L² form is Theorem Z. (5) Data: rung 1 exact; the α = 0.75 tension was a four-seed
fluctuation (12 seeds: top-window sup-slope 0.392 ± 0.016, mean-square slope 0.787 ± 0.059; note (iii) answered); greedy sets fall
below X^{α−δ} in pure-power slope but are provably log-powers (κ ≈ 2.3–3), and a new feedback design fails for a proved reason.
Consolidator's note (ii) is sharpened: the Carlson obstruction is real for growth-only inputs and disappears after the logarithm.

## §1. Task 1 — the reflected second moment: the identity, what it proves, and the exact missing lemma

**1.1 The identity, in its two forms** [proved here; computed: `verify/t1_classsums.py` → `verify/logs/t1_classsums.log`].
*Proposition 1.1.* (a) (additive form) With e(y) = e^{2πiy}, E has the formal expansion E(x) = Σ c(a/b)e(ax/b) over reduced
fractions a/b with b ∈ ⟨R⟩, b > 1, a ≠ 0, and c(a/b) = ρμ(b)b/(2πi·a·φ(b)). For finite R this is the Fourier series of the
Q-periodic E (Q = Π_{p∈R}p), and Parseval gives Σ|c|² = (ρ²/12)Π_{p∈R}(1 + (p+1)/(p−1)) = ρ2^{|R|}/12 = fr Prop. 5.1.
(b) (reflected form, the brief's) For Re s = σ the class of n/m = a/b (lowest terms) in ζ(1−s)D_R(s) = Σ_nΣ_{m∈⟨R⟩}μ(m)n^{s−1}m^{−s}
sums to a^{s−1}b^{−s}μ(b)ρ/Π_{p|b}(1 − 1/p) (b ∈ ⟨R⟩, (a, b) = 1), and the formal diagonal is
  Σ_{a/b}|class|² = ρ²ζ(2 − 2σ)·Π_{p∈R}(1 + p^{−2σ}(1 − p^{2σ−2})(1 − 1/p)^{−2})   (0 < σ < ½).
*Proof.* (a) {y} = ½ − Σ_{h≠0}e(hy)/(2πih); the frequency h/m = a/b collects the m ∈ ⟨R⟩ with b | m (h = am/b), and
Σ_{m∈⟨R⟩, b|m}μ(m)b/m = μ(b)Π_{p∈R, p∤b}(1 − 1/p) = μ(b)ρb/φ(b); Σ_{m|Q}μ(m) = 0 kills the constant. Parseval: Σ_{a≠0,(a,b)=1}a^{−2} =
(π²/3)Π_{p|b}(1 − p^{−2}) and (1 − p^{−2})/(1 − 1/p)² = (p+1)/(p−1). (b) Write n = ka, m = kb with k = (n, m); m squarefree forces
k, b ∈ ⟨R⟩ and (k, b) = 1, and the k-sum is Σ_{k∈⟨R⟩,(k,b)=1}μ(k)/k = ρ/Π_{p|b}(1 − 1/p). The a-sum over (a, b) = 1 is
ζ(2−2σ)Π_{p|b}(1 − p^{2σ−2}), and multiplicativity in b gives the product. ∎
*Correction to the brief's sketch* (single-check → checked): the brief omits the coprimality factor (1 − p^{2σ−2}); brute force
over a ≤ 2·10⁵ with an exact Hurwitz tail gives, e.g., R = {2}, σ = 0.2: 6.92914577326 (sum) = 6.92914577326 (corrected
product) ≠ 9.21491143894 (sketch); four sets checked, agreement to 10⁻³¹. The divergence locus is unchanged: for 0 < σ < ½ the
product diverges iff Σ_{p∈R}p^{−2σ} = ∞, i.e. for 2σ < α_R (and possibly at 2σ = α_R). Part (a) is checked exactly on nine sets
R (coefficients to 10⁻¹³ by exact integration of the piecewise-linear E over a period; (1/Q)∫E² = ρ2^{|R|}/12 in rationals).
The two forms index the same reduced fractions a/b (additive frequency a/b, multiplicative frequency log(a/b)); (a) is the one
fr read-F §4(a) states as the contract ("diagonal ≍ #R-numbers ≤ X"), (b) its Mellin twin.

**1.2 In what sense it is a mean value.** (i) *Nowhere convergent.* Σ_n n^{s−1} converges only for σ < 0 and Σ_{m∈⟨R⟩}μ(m)m^{−s}
absolutely only for σ > α_R ≥ 0: the double series defining F(s) := ζ(1−s)D_R(s) has no half-plane of convergence, and in
the additive form Σ|c|² = (ρ²/12)Π_{p∈R}2p/(p−1) = ∞ for infinite R — E is not Besicovitch-B², so "the class sums" are
formal in every form. Carlson's theorem (quoted in Hilberdink 2005, fr `sources/w-18a…txt` p. 336: a Dirichlet series
analytic *of order 0* in a half-plane has Bohr mean square = its diagonal there) needs a Dirichlet series convergent in some
right half-plane; F is not one, and D_R alone is. (ii) *The rigorous identity is weighted.* For β₂ < σ < 1 the Mellin
transform ∫_0^∞E(x)x^{−s−1}dx equals ζ_P(s)/s (E(x) = −ρx on (0, 1)), so Plancherel [standard: Fourier–Plancherel
under x = e^u] gives ∫_0^∞E(x)²x^{−2σ−1}dx = (1/2π)∫|ζ_P(σ+it)|²|σ+it|^{−2}dt = (1/2π)∫|F(σ+it)|²|χ(σ+it)|²|σ+it|^{−2}dt, and
|χ(σ+it)| = (|t|/2π)^{½−σ}(1 + O(1/|t|)) [recalled, unverified; spot-checked to 10⁻⁶ at t = 50…5000, same log]. So the only
mean value of F that E controls is ∫|F(σ+it)|²|t|^{−1−2σ}dt: E = O(x^τ) permits ∫_T^{2T}|F(σ+it)|²dt ≍ T^{1+2σ} on τ < σ < ½,
i.e. a Bohr mean square of F growing like T^{2σ}. The formal diagonal being infinite contradicts no finite growth rate unless one
knows how fast its truncation at height T grows. That is the gap, and §1.3 shows it cannot be closed by growth information.

**1.3 The reflected route pushed to its limit: α_R/4, and why growth information stops there.**
*Proposition 1.3* [proved here; assumes RH; novelty: single-check]. If RH holds and α_R < ½, then β(R) ≥ β₂(R) ≥ α_R/4, for EVERY R.
*Proof.* Suppose β₂ < α_R/2 and fix σ ∈ (β₂, α_R/2), δ > 0 small. (i) For σ′ > β₂, V(σ′) := ∫_0^∞E²x^{−2σ′−1}dx < ∞, so by
Cauchy–Schwarz ∫_1^∞|E|x^{−σ″−1}dx ≤ V(σ′)^{½}(2(σ″ − σ′))^{−½} for σ″ > σ′. So ζ_P(s) = ρs/(s − 1) + s∫_1^∞E(x)x^{−s−1}dx
(an identity for σ > 1) continues ζ_P to σ > β₂ (s ≠ 1) with |ζ_P(s)| ≪_δ |t| on σ ≥ β₂ + δ, |t| ≥ 1; for β₂ < σ < 1 the Mellin
transform ∫_0^∞E(x)x^{−s−1}dx converges absolutely and equals ζ_P(s)/s (E(x) = −ρx on (0, 1)), so Plancherel [standard, for
x^{−σ}E ∈ L¹ ∩ L²(dx/x)] gives ∫_T^{2T}|ζ_P(σ+it)|²dt ≤ 2π(2T+1)²V(σ) ≪ T².
(ii) D_R is analytic for σ > α_R (the product) and equals ζ_P/ζ on β₂ < σ ≤ α_R, where ζ ≠ 0 (RH; the strip lies in (0, ½)).
For σ ≤ α_R + δ < ½: 1/ζ(s) = 1/(χ(s)ζ(1−s)), |1/χ(s)| ≪ |t|^{σ−½} [recalled: Stirling; spot-checked] and |1/ζ(1−s)| ≪ |t|^ε
(RH, Re(1−s) ≥ ½ + δ; [quoted] fr `sources/z-02…txt` ll. 1203–1205, citing Montgomery–Vaughan Th. 13.18, 13.23). So D_R is of
finite order on σ ≥ β₂ + δ and ∫_T^{2T}|D_R(σ+it)|²dt ≪ T^{1+2σ+ε}. (iii) (quantitative Carlson) Let A_N(s) = Σ_{m∈⟨R⟩}μ(m)m^{−s}e^{−m/N}
= (1/2πi)∫_{(2)}D_R(s+w)Γ(w)N^w dw. Move the line to Re w = −η (σ − η > β₂ + δ), picking up D_R(s) at w = 0; the elementary bound
|Γ(u+iv)| ≤ Γ(u+3)/|v|³ (from |Γ(x+iy)| ≤ Γ(x), x > 0, and Γ(w) = Γ(w+3)/(w(w+1)(w+2))) and Cauchy–Schwarz give
∫_T^{2T}|A_N(σ+it)|²dt ≪ T^{1+2σ+ε} + N^{−2η}T^{1+2σ+ε}. (iv) (the diagonal, from the Montgomery–Vaughan inequality (G.27)–(G.28),
[quoted] `sources/mv2-draft.txt` Theorem G.16, p. 427, ll. 23037–23060: for distinct real λ_n with gaps δ_n,
|Σ_{m≠n}x_m ȳ_n/(λ_m − λ_n)| ≤ (3π/2)(Σ|x_n|²/δ_n)^{½}(Σ|y_n|²/δ_n)^{½}) — expanding the square and applying (G.27) to the two
off-diagonal terms: ∫_T^{2T}|Σa_n n^{−it}|²dt ≥ Σ|a_n|²(T − 3π(n+1)). With a_n = μ_R(n)n^{−σ}e^{−n/N}, N = T^{1−η}, the terms
n > T/(10π) are e^{−T^η}-small, so ∫_T^{2T}|A_N|² ≥ (T/2)e^{−2}Σ_{m∈⟨R⟩, m≤N}m^{−2σ} − O(1). Hence Σ_{m∈⟨R⟩,m≤N}m^{−2σ} ≪ N^{(2σ+ε)/(1−η)}
for all N. But Q_R(N) := #⟨R⟩ ∩ [1, N] ≥ π_R(N) ≥ N^{α_R−ε} infinitely often, so N^{α_R−2σ−ε} ≤ N^{(2σ+ε)/(1−η)} i.o., i.e.
α_R ≤ 4σ + O(ε + η). Let σ ↓ β₂. ∎
*Remark 1.3′ (the brief's missing lemma is false as posed).* The route supplies exactly: a Dirichlet series (D_R, coefficients of
modulus 1 on a set of counting exponent α_R) continued with finite order past α_R/2, with Bohr mean square ≪ T^{2σ}. The function
f(s) = η(2s) = (1 − 2^{1−2s})ζ(2s) (coefficients ±1 on the squares: counting exponent ½) is entire, of finite order, and on
1/6 < σ < ¼ has ∫_T^{2T}|f(σ+it)|²dt ≪ T^{2−4σ+ε} ≤ T^{1+2σ} (under RH: f(s) = (1 − 2^{1−2s})χ(2s)ζ(1 − 2s), |χ(2s)| ≍ t^{½−2σ}
(Stirling) and |ζ(1 − 2s)| ≪ t^ε on Re(1 − 2s) > ½ (the quoted RH bound); unconditionally from the mean value of |ζ|² on
Re s > ½ [recalled]), while its diagonal Σ n^{−4σ} diverges for σ ≤ ¼ = ½·½. So "finite order + mean square T^{2σ} ⟹ convergent diagonal"
fails on (α/3, α/2); no mean-value theorem driven by growth alone closes the gap. What Carlson needs is ORDER ZERO (bounded mean
square), which E = O(x^τ) does not supply for D_R or F. The arithmetic input that does supply it is the Euler product: §1.4.

**1.4 The repair: take logarithms — the relative Hilberdink theorem.**
*Theorem Z* [proved here; assumes RH; novelty: single-check]. Let R ⊂ ℙ, Σ_{p∈R}1/p < ∞, α_R > 0. Suppose that for some
τ₀ < α_R/2, T₀ ≥ 1, A ≥ 0 the prime zeta function P_R(s) = Σ_{p∈R}p^{−s} continues analytically to U = {σ > τ₀, |t| > T₀}
with |P_R(s)| ≤ C_η|t|^A on {σ ≥ τ₀ + η, |t| > T₀} for each η > 0. Then β(R) ≥ β₂(R) ≥ α_R/2: ∫_1^∞E²x^{−2σ−1}dx = ∞ for every σ < α_R/2, so for every ε > 0,
(1/X)∫_X^{2X}E(x)²dx ≥ X^{α_R−ε} for infinitely many dyadic X. *Contrapositive (the relative form of Hilberdink's Cor. 2(b)):*
if β₂(R) < α_R/2, then for every τ₀ < α_R/2 the function log(ζ_P/ζ) = −Σ_k P_R(ks)/k has singularities (zeros or poles of
ζ_P/ζ) in {σ > τ₀} at arbitrarily large heights, or is of infinite order there.
Two standard lemmas, proved here so that the only recalled input left is Stirling's formula for |χ| (§4):
*Lemma Z.a (Borel–Carathéodory).* If g is analytic on |z − z₀| ≤ ρ₁ and Re g ≤ M on |z − z₀| = ρ₁, then |g(z)| ≤
2rM/(ρ₁ − r) + ((ρ₁ + r)/(ρ₁ − r))|g(z₀)| for |z − z₀| ≤ r < ρ₁. *Proof.* h = g − g(z₀) has h(z₀) = 0 and Re h ≤ M′ :=
M + |g(z₀)| (M′ ≥ 0 as Re h has mean 0 on the circle); φ = h/(2M′ − h) is analytic with |φ| ≤ 1 (|h| ≤ |2M′ − h| ⟺ Re h ≤ M′)
and φ(z₀) = 0, so Schwarz gives |φ| ≤ r/ρ₁ and |h| ≤ 2M′r/(ρ₁ − r). ∎
*Lemma Z.b (Phragmén–Lindelöf in a half-strip).* If f is analytic near S = {a ≤ σ ≤ b, t ≥ T₁}, |f| ≤ exp(Ce^{ct}) on S
with c < π/(b − a), and |f| ≤ M on ∂S, then |f| ≤ M on S. *Proof.* With m = (a + b)/2, λ ∈ (c, π/(b − a)):
Re cos(λ(s − m)) = cos(λ(σ − m))cosh(λt) ≥ cos(λ(b−a)/2)cosh(λt) > 0, so f_ε = f·exp(−ε cos(λ(s − m))) has |f_ε| ≤ |f| on S and
f_ε → 0 as t → ∞; apply maximum modulus on S ∩ {t ≤ T′}, let T′ → ∞, then ε → 0. ∎
*Proof of Theorem Z.* Suppose β₂ < α_R/2. Fix τ ∈ (max(β₂, τ₀, 0), α_R/2) and δ > 0 with τ + 3δ < α_R/2; σ* := τ + 2δ.
(Z1) As in Prop. 1.3(i): ζ_P continues to σ > β₂ (s ≠ 1) with |ζ_P(s)| ≪ |t| on σ ≥ τ + δ/2, |t| ≥ 1.
(Z2) On U₊ = U ∩ {σ > max(τ₀, 0)}, L(s) := −Σ_{k≥1}P_R(ks)/k is analytic (ks ∈ U₊; the terms with kσ > α_R + 1 are O(2^{−kσ}))
and |L(s)| ≪ |t|^A. L = log Π_{p∈R}(1 − p^{−s}) for σ > α_R, so D_R := e^L is the continuation of the product: analytic and
ZERO-FREE on U₊, and D_R = ζ_P/ζ there (identity theorem on each component of U₊, each of which meets σ > 1).
(Z3) Polynomial bound on U′ = {σ ≥ τ + δ/2, |t| ≥ T₁}. For σ ≥ ½ + δ′: |D_R| ≤ |ζ_P||1/ζ| ≪ |t|^{1+ε} (RH; quoted as in
Prop. 1.3(ii)). For σ ≤ ½ − δ′: |1/ζ(s)| = |1/χ(s)||1/ζ(1 − s)| ≪ |t|^{σ−½+ε}, so |D_R| ≪ |t|^{1+ε}. In the band |σ − ½| ≤ δ′
apply Lemma Z.b to f = D_R(s)(−i(s − ½))^{−2} (principal branch; |−i(s − ½)| ≍ t): |f| ≤ C on the sides and on the compact
bottom edge, |f| ≤ exp(C t^A) inside (Z2); so |D_R| ≪ t². Hence Re L = log|D_R| ≤ 2 log|t| + C on U′ (conjugate for t < 0).
(Z4) Order zero. For |t₀| ≥ T₂ := T₁ + α_R + 2, Lemma Z.a on the disc of centre z₀ = α_R + 2 + it₀ and radius
ρ₁ = α_R + 2 − τ − δ/2 (inside U′), with |L(z₀)| ≤ Σ_{p∈R}Σ_k p^{−k(α_R+2)} = O(1) and r = ρ₁ − δ/2, gives |L(s)| ≪ log|t| on
{σ ≥ τ + δ, |t| ≥ T₂}.
(Z5) The diagonal. L(s) = Σ_n b_n n^{−s}, b_{p^k} = −1/k for p ∈ R, else 0. For s = σ* + it, t ∈ [T, 2T], N = T^{1−η} (η ∈ (0, ⅓)),
A_N(s) := Σ_n b_n n^{−s}e^{−n/N} = (1/2πi)∫_{(2)}L(s + w)Γ(w)N^w dw. Move the line to Re w = −δ except on the piece
|Im(s + w)| ≤ T₂, which stays on Re w = 2 and is joined by horizontal segments at Im(s + w) = ±T₂ (L is bounded there, |Γ(w)| ≤
Γ(Re w + 3)/|Im w|³ ≪ T^{−3}, |N^w| ≤ N²). The residue at w = 0 is L(s); on Re w = −δ, (Z4) gives |L(s + w)| ≪ log(T + |Im w|).
So |A_N(s)| ≤ |L(s)| + O(N^{−δ}log T) + O(N²T^{−3}) ≪ log T, and the Montgomery–Vaughan bound of Prop. 1.3(iv) gives
(T/2)e^{−2}Σ_{n≤N}|b_n|²n^{−2σ*} − O(1) ≤ ∫_T^{2T}|A_N(σ*+it)|²dt ≪ T(log T)². Hence Σ_{p∈R, p≤N}p^{−2σ*} ≪ (log N)² for all large N.
But π_R(N) ≥ N^{α_R−δ} for infinitely many N, where the sum is ≥ N^{α_R−δ−2σ*} = N^{α_R−2τ−5δ} → ∞ (2τ + 6δ < α_R). ∎
*What RH does here.* Only (Z3): a polynomial bound for 1/ζ off the critical line, used to turn |ζ_P| ≪ |t| into |D_R| ≪ |t|^{O(1)}.
The logarithm then converts polynomial growth into log growth (order zero) — exactly the input Prop. 1.3 lacked and Remark 1.3′
shows cannot come from growth alone. The price is analyticity of log D_R, i.e. continuation of P_R.

**1.5 Corollary Z.1 — every regular deletion, every c (the A8 corner)** [proved here; assumes RH; novelty: single-check].
Let 0 < α < 1, c > 0, F(x) = Σ_{p≤x}min(1, c·p^{α−1}), and let R be any set of primes with π_R(x) − F(x) = O(x^θ), θ < α/2 —
e.g. the greedy sets of fr §6.3 for every c (|π_R − F| ≤ 1) and BDR's Broucke–Vindas selection (fr §6.3(iv): c = 1, θ = 0).
Then, under RH, β(R) ≥ β₂(R) ≥ α/2 = α_R/2. With fr Theorem C (unconditional, α/k_c) this settles the pure-deletion Conjecture O
for all regular deletions under RH, including c = 2 and every c/k_c ∈ ℤ pattern — the case the brief lists as open.
*Proof.* Verify Theorem Z's hypothesis with τ₀ = max(θ, α − ½, 0) < α/2 (α < 1) and T₀ = 1. Partial summation (fr §5.5, re-derived):
P_R(s) = c·P(s + 1 − α) − Σ_{p≤p₀}(c p^{α−1} − 1)p^{−s} + H(s), H(s) = s∫_2^∞(π_R − F)(u)u^{−s−1}du analytic for σ > θ with
|H(s)| ≪ |s|/(σ − θ). P(w) = Σ_{m≥1}μ(m)m^{−1}log ζ(mw) (Möbius inversion of log ζ(w) = Σ_k P(kw)/k): under RH, log ζ is analytic
on {Re w > ½, |Im w| ≥ 1}, and the terms m ≥ 2 have Re(mw) > 1 and are O(2^{−m·Re w}); w = s + 1 − α has Re w > ½ iff σ > α − ½.
Growth: on Re w ≥ ½ + δ/2, Re log ζ = log|ζ| ≤ C log|Im w| (ζ ≪ |t|^ε under RH, quoted as above), so Lemma Z.a on discs of centre
2 + i·Im w gives |log ζ(w)| ≪ log|Im w| — the step Broucke–Hilberdink take, fr `sources/t-19a…txt` ll. 200–210. So |P_R(s)| ≪ |t|
on U. ∎
*Where RH enters, and why RH-conditional is the right strength.* (a) Analyticity of P(s + 1 − α) for σ > α − ½ (a zero ρ of ζ with
Re ρ > ½ puts branch points of P_R at ρ − 1 + α; if Re ρ > 1 − α/2 they sit right of α/2, and fr Theorem C(b) then gives β ≥ Θ + α − 1
instead); (b) the polynomial bound for 1/ζ in (Z3). Conjecture U implies RH (fr §7.2(a)); if RH fails, U already fails at (ℙ, ℕ)
(fr read-O §4 A1); if RH holds, no regular deletion refutes U. **So read-O's corner A8 ("the only surgery corner where a
counterexample is not excluded by a theorem") is closed as a refutation corner.**

**1.6 The exact missing lemma for general R, and the anatomy of a counterexample.**
*Lemma G (missing).* If β₂(R) < α_R/2, then P_R continues analytically, with finite order, to {σ > τ₀, |t| > T₀} for some
τ₀ < α_R/2 and T₀. — By Theorem Z, RH + Lemma G ⟹ Conjecture O (mean-square form, pure deletions) for every R. Equivalent form
(RH; given β₂ < α_R/2 ζ_P is analytic on σ > β₂, so D_R = ζ_P/ζ is meromorphic there): *(G′) ζ_P has no zeros in
{τ₀ < σ < ½, |t| > T₀} ∪ {½ < σ, |t| > T₀}, vanishes at every zero of ζ on σ = ½ above T₀ to exactly its order, and ζ_P/ζ has finite
order there.* (For α_R < ½ the critical-line clause is automatic: D_R is the convergent product on σ > α_R.) Lemma G holds for
every R whose prime count admits a decomposition π_R = M + O(x^θ), θ < α_R/2, with ∫u^{−s}dM(u) continuing with finite order past
α_R/2 off the real axis (the proof of 1.5 verbatim); it fails exactly when the continuation of log D_R meets infinitely many
branch points in every half-plane σ > τ₀, τ₀ < α_R/2.
*Proposition 1.6 (anatomy)* [proved here; (i) unconditional, (ii)–(iii) under RH]. Let β₂(R) < α_R/2. Then (i) P_R continues along paths to σ > β₂ with only isolated
logarithmic branch points, located at the zeros/poles of ζ_P/ζ and their images ρ′/m (m ≥ 1); in particular P_R has NO natural
boundary in σ > β₂ — so every R whose P_R has a natural boundary on a line σ = σ_b ≥ α_R/2 satisfies O; (ii) by Theorem Z, for every
τ₀ < α_R/2 there are infinitely many such branch points in σ > τ₀ (or P_R has infinite order there): ζ_P/ζ has infinitely many
zeros or poles with real part > τ₀ — zeros of ζ_P off the critical line (real part in (τ₀, α_R]), or critical zeros of ζ at which
ζ_P vanishes to a different order; (iii) no decomposition as in
Lemma G exists — the prime count of R is irregular at the scale x^{α_R/2}, as for random R, which Theorem B excludes almost surely.
*Proof.* (i) P_R(s) = −Σ_{m≥1}μ(m)m^{−1}L(ms) (Möbius inversion of L = −Σ_k P_R(ks)/k), and L = log D_R continues along any path
avoiding the zeros/poles of the meromorphic D_R, which are isolated; for s in a compact K ⊂ {σ > β₂} only finitely many pairs
(ρ′, m) have ρ′/m ∈ K, because D_R has no zeros or poles on σ > α_R. (ii) is Theorem Z's contrapositive. (iii) as in 1.5. ∎

**1.7 Additions A.** Theorem Z extends to (ℙ ∖ R) ∪ A with L = log(ζ_sys/ζ) = −Σ_{p∈R}Σ_k p^{−ks}/k + Σ_{a∈A}Σ_k a^{−ks}/k if
P_R − P_A continues as in Theorem Z and the frequencies {k log p} ∪ {k log a} satisfy a separation |λ − λ′| ≥ e^{−Kλ} (Hilberdink's
(3.1), w-18a p. 336): (G.27) holds for any distinct reals, the error Σ|a_n|²/δ_n forces N ≤ T^{1/(K+1)}, and the diagonal
Σ_{p∈R, p≤N}p^{−2σ} + Σ_{a∈A, a≤N}a^{−2σ} ≥ Σ_{p∈R, p≤N}p^{−2σ} still beats (log T)²: β₂ ≥ max(α_R, α_A)/2 — additions only add
positive diagonal terms. Without separation no diagonal argument can work: additions a_p = p(1 + ε_p), p ∈ R, with ε_p = e^{−p}
leave at height T only the resolved pairs (ε_p ≥ 1/T, i.e. p ≤ log T) on the diagonal, ≤ (log T)^{α_R}. Such a system is a tiny
perturbation of ℙ [heuristic: β ≈ 0 expected, not checked], so **the A-clause of Conjecture O as stated ("any set A") is probably
false and should carry a separation hypothesis**; it does not bear on U (that system has α = Θ).

**1.8 Nearest published objects.** Theorem Z ↔ Hilberdink 2005 Thm 1 / Cor. 2(b) (w-18a pp. 335–337: Carlson's mean value
for ζ_P − ρφ_P, order 0 from Hilberdink–Lapidus Thm 2.3) — same device; difference: applied to the RELATIVE quotient ζ_P/ζ (the
deleted Euler product), growth from E and RH for ζ, diagonal Σ_{p∈R}p^{−2σ} instead of Σ(1 − ρΛ_P(n))²n^{−2σ}. B–C step ↔
Broucke–Hilberdink 2024 ll. 200–210. Prop. 1.3 ↔ Carlson's theorem (via Hilberdink p. 336) + MV (G.27); difference: polynomial
growth, quantified. Prop. 1.1(a) ↔ Franel's integral (fr Prop. 5.1) and, for infinite B, **Avdeeva 2015** (arXiv 1512.00149, Theorem 1, p. 3,
`sources/avdeeva-2015-1512.00149v1.txt` ll. 94–132): the SHIFT-AVERAGED variance of B-free counts in intervals of length N is
∼ C·N^α when the semigroup generated by B has count A·N^α + O(N^β), β < α < 1, 2 ∉ B — the square-root law proved in its
stationary form, with the constant carrying Γ(2 − α)ζ(2 − α), i.e. the reflected diagonal of 1.1(b) at σ = α/2 (single-check).
Difference: Conjecture O concerns the single interval [0, x] (no average over shifts), where no such theorem is known;
arXiv search (4 queries, `sources/arxiv-O-q*.xml`) found no Ω-result for that case. (b) ↔ none found beyond Avdeeva's
constant. Corollary Z.1 ↔ fr Theorem C (same class). Lemma G ↔ Hilberdink's Remark B(ii) (w-18a p. 336: "if … ζ_P(s) has
finitely many zeros here, then ζ_P(s) and φ_P(s) have zero order in this range") — the same finiteness-of-zeros hypothesis, placed
on ζ_P/ζ instead of ζ_P. New definitions: β₂(R) ↔ the mean-square (Ω₂) exponent, standard; M_diag(X) ↔ fr Prop. 5.1 truncated at
b ≤ X (Avdeeva's constant is its stationary analogue); the feedback deletion ↔ BDR's Broucke–Vindas selection (a deterministic
low-discrepancy choice, fr §6.3(iv)) with the selection rule replaced by error feedback — difference: it steers N_P, not π_R.

## §2. Task 2 — the resonance (large-values) route: a named obstruction; the Parseval form is Theorem Z

(a) *What Kronecker gives.* Since {log p} is ℚ-independent, (p^{−it})_{p∈R, p≤Y} is dense in the torus and
sup_t|Π_{p∈R,p≤Y}(1 − p^{−σ−it})| = Π_{p∈R,p≤Y}(1 + p^{−σ}). The price is height: by Dirichlet's simultaneous approximation
(pigeonhole [standard]) aligning all p ≤ Y to within 1/q costs t up to ≈ q^{π_R(Y)}, so at height T only the primes with
π_R(p) ≲ log T/log q can be aligned, and the resonance value is exp(Σ_{p∈R, π_R(p) ≲ log T}p^{−σ}) = exp((log T)^{1−σ/α_R+o(1)})
= T^{o(1)} for every σ > 0 [heuristic in the o(1); the sub-polynomial size is what matters]. For σ > α_R the full product
converges and |D_R(σ+it)| ≤ Π_{p∈R}(1 + p^{−σ}) < ∞ for all t: resonance produces bounded values there.
(b) *What a converse needs.* E = O(x^τ) (even β₂ < α_R/2) gives only |ζ_P(σ+it)| ≪ |t| on σ > τ (Z1), i.e. |D_R| ≪ |t|^{O(1)}
under RH. A Perron/Mellin converse "large values of D_R ⟹ large E" needs |ζ_P| ≫ |t|^{1+δ} at some points (to break the Mellin
bound), or Bohr mean square ≫ T^{2+δ} (to break Plancherel). Resonance yields T^{o(1)}, and only where the product converges
(σ > α_R, or where Σ_{p∈R}p^{−s} converges); the contradiction has to be found at σ < α_R/2, where D_R is a continuation, not the
product, and Kronecker says nothing about it.
(c) *Named obstruction ("sub-polynomial resonance").* Large values of an Euler product at height T are T^{o(1)} and live in its
region of convergence; every Perron/Parseval converse from E needs polynomial excess (|t|^{1+δ}) at σ < α_R/2. So the sup-form of
the resonance route cannot bound β(R) below by anything — the same defect as the reflected route (§1.3: growth information is
not order-zero information). No theorem is available in the sup form.
(d) *The form that works is L², on log D_R, and it is Theorem Z.* Bohr–Jessen's picture [recalled, unverified; heuristic role
only]: on σ > α_R/2, log D_R(σ + it) is distributed like the random series −Σ_{p∈R}X_p p^{−σ} (X_p independent, uniform on the
circle), whose variance Σ_{p∈R}p^{−2σ}/2 is finite iff 2σ > α_R. Theorem Z is the rigorous converse of exactly this: order zero
(Z4) forces Carlson's mean value, whose diagonal Σ_{p∈R}p^{−2σ} must then converge — false for 2σ < α_R. It is a Parseval
converse, not a sup converse, and it needs the continuation of P_R (Lemma G), which is the resonance route's real missing input.
**Close of task 2: named obstruction (sub-polynomial resonance), with the L² replacement proved as Theorem Z.**

## §3. Task 3 — the dyadic mean square, computed exactly (evidence, not theorems)

**3.1 Statistic and code** [computed]. M(X) := (1/X′)∫_X^{X+X′}E(x)²dx over non-overlapping windows of six bins of the frontier's
20-per-decade grid (X′/X = 10^{0.3} − 1 ≈ 0.995, so "dyadic" means [X, 1.995X]), aligned at 10⁴. It is EXACT from the stored bins:
on [n, n + 1) E is linear of slope −ρ, so ∫_n^{n+1}E² = (N(n) − ρ(n + ½))² + ρ²/12 and a bin contributes sumE2 + count·ρ²/12
(`verify/dyadic_ms.py`). No count on disk is recomputed: T_α seeds 1–8 (10⁹) and 1–4 (10¹⁰), greedy c = 1, 2 are read from
fr `verify/data*/`. New runs use `verify/thin_fr.c` (byte-identical to fr `verify/thin.c`, SHA-256 6d359b51…; re-run of seed 1,
α = 0.75, X = 10⁹ reproduces every fr bin exactly — `verify/data/xcheck_bern_a0.75_s1_1e9.csv`) and `verify/thin2.c` (the same
counting core plus the modes `finite`, `feedback`, `dumpR`). `verify/rnums.c` enumerates the squarefree R-numbers b ≤ X by
depth-first search and gives Q_R(X) = #⟨R⟩ ∩ [1, X] and W(X) = Σ_{b≤X}Π_{p|b}(p+1)/(p−1), hence the truncated Franel diagonal (outputs `verify/rn/*.csv`; the
intermediate R-prime lists, 194 MB, were deleted and are regenerable with `thin2 dumpR` or `RDUMP=…`)
M_diag(X) := ρ²W(X)/12 (= fr Prop. 5.1's value when R is finite and X ≥ Π_{p∈R}p). Fits (`verify/t3_analysis.py`): pure-power
slopes of log M over [10^k, X_max] (k = 4…7) and the top three decades; a log-corrected fit log M = a + b log X − κ log ln X; and the
intercept of the local two-decade slopes regressed on 1/ln X. Why these: a finite window cannot separate X^{α−δ} from
X^α(ln X)^{−κ} (at X ≈ 10⁷, κ = 3 mimics δ ≈ 0.19), and §1 proves that for regular R the exponent IS α (RH), so a pure-power
deficit there measures κ, not a counterexample.

**3.2 Rung 1: finite R reproduces Prop. 5.1** [computed: `verify/t3_rung1.py` → `verify/logs/t3_rung1.log`; data `verify/data/finite_*.csv`
from `thin2 finite 1e8 …`]. R = {2, …, 13} (Q = 30030): the exact one-period mean square (long double, in the header) is
1.022977022977090 against ρ2^{|R|}/12 = 1.022977022977023 (rel. 7·10⁻¹⁴); the dyadic code gives M(X)/(ρ2^{|R|}/12) − 1 =
−7·10⁻⁴, +7·10⁻⁶, −2·10⁻⁵ at X = 6·10⁵, 5·10⁶, 4·10⁷. R = {3, …, 19} (Q = 4 849 845): 3.648512478207 vs 3.648512478234 (7·10⁻¹²),
dyadic −3.9·10⁻³, −6.9·10⁻⁴ at X = 5·10⁶, 4·10⁷ (Q/X = 0.97, 0.12). Pure-power slopes 0.000 ± 0.03. The pipeline is calibrated.

**3.3 Rung 2: random R (T_α), and the α = 0.75 tension** [computed: `verify/t3_seeds.py` → `logs/t3_seeds.log`,
`verify/t3_analysis.py` → `logs/t3_analysis.log`, `verify/t3_ratio.py` → `logs/t3_ratio.log`, `verify/t3_kappa.py` → `logs/t3_kappa.log`].
Mean-square slopes over [10⁴, 10¹⁰] (mean ± s.e. over seeds; in brackets [10⁷, 10¹⁰]): T_0.60 (4 seeds) 0.606 ± 0.034 [0.642 ± 0.067];
T_0.75 (12 seeds: fr 1–4 + new 5–12) 0.723 ± 0.018 [0.787 ± 0.059]; T_0.90 (4) 0.923 ± 0.044 [0.910 ± 0.079]. Against (a) α = 0.60,
0.75, 0.90 (the diagonal); (b) the local exponent of Q_R(X) = #⟨R⟩ ∩ [1, X], computed exactly by `rnums`: 0.602 ± 0.001, 0.750 ± 0.000
(and of W: 0.601, 0.750); (c) the one-scale value X^α/ln X of Theorem B: slope 0.534, 0.684, 0.834 on the same window. On [10⁴, 10¹⁰] the data
sit between (c) and (a); on [10⁶, 10¹⁰] slightly above α (0.674 ± 0.029, 0.783 ± 0.030): M ≍ X^α(ln X)^{O(1)}. M/M_diag shows no
decline (log-power index κ = −2.9 … +0.3, errors 1.2–2.0 per seed; on X ≥ 10⁶ mildly growing, pure-power +0.09 ± 0.02 per decade
across the eight seeds) and sits at 5–70: for random R the mean square EXCEEDS the truncated
Franel diagonal several-fold — the incomplete periods of the R-numbers near X (Theorem B's one-scale block) carry most of it.
*The tension (read-O F5).* Top window [10⁷, 10¹⁰], T_0.75, running-sup slope (fr fit.py convention): seeds 1–4 0.450 ± 0.009 (the
fr value, reproduced); the eight new seeds 0.363 ± 0.014; all twelve **0.392 ± 0.016** — 1.1σ above α/2 = 0.375 and 3.3σ below
1/(3 − α) = 0.444. Side by side, the dyadic mean-square slope on the same window: all twelve 0.787 ± 0.059 against α = 0.75 (0.6σ)
and 2/(3 − α) = 0.889 (1.7σ). Seed by seed (log): the four fr seeds are the four highest top-window sup-slopes of twelve (0.433–0.474
vs 0.313–0.429). **The four-seed excess was a small-sample fluctuation; the tension resolves toward α/2 (sup) and α (mean square).**

**3.4 Rung 3: structured R (greedy c = 1, 2) — below X^{α−δ} in pure-power slope, and why that is not a counterexample.**
| design | X | ms-slope [10⁴,X] / [10⁶,X] / top 3 dec. | sup-slope [10⁴,X] | Q_R slope | M/M_diag: 6·10⁵ → 2.5·10⁹ | κ (X ≥ 10⁶) |
|---|---|---|---|---|---|---|
| greedy c=1, α=0.60 | 10¹⁰ | 0.445 / 0.433 / 0.447 | 0.238 | 0.600 | 0.71 → 0.22 | 3.00 ± 0.15 |
| greedy c=1, α=0.75 | 10¹⁰ | 0.577 / 0.594 / 0.598 | 0.308 | 0.750 | 0.52 → 0.10 | 2.80 ± 0.15 |
| greedy c=2, α=0.60 | 10¹⁰ | 0.497 / 0.522 / 0.527 | 0.278 | 0.656 | 0.81 → 0.22 | 2.32 ± 0.24 |
| greedy c=2, α=0.75 (new run) | 10¹⁰ | 0.676 / 0.467 / 0.442 | 0.354 | 0.805 | 9.7 → 0.92 | 5.9 ± 0.3 |
(κ: fit of log(M/M_diag) = a − κ log ln X; Q_R slope for c = 2 exceeds α by the (ln X)^{c−1} factor; c = 2, α = 0.75 deletes every
prime ≤ 13, and its early windows carry that fundamental-lemma transient — ratio 9.7 at 6·10⁵ — cf. fr §6.3(4).)
*Reading.* Every greedy set has pure-power mean-square slope below α by 0.07–0.31 over ≥ 3 decades and a ratio M/M_diag falling
like X^{−0.13…−0.33} — **the stop line's literal trigger ("dyadic mean square below X^{α_R−δ} over three decades") is met.** It is
met, however, by sets for which β₂ ≥ α/2 is a theorem: for c = 1 UNCONDITIONALLY — fr Theorem C holds in mean-square form, because
β₂ < α/2 would make ζ_P(s) = ρs/(s−1) + s∫_1^∞E(x)x^{−s−1}dx analytic on σ > β₂ (Prop. 1.3(i)), across the branch point s = α/2
[proved here, one line] — and for c = 2 under RH (Corollary Z.1). So on these sets the deficit IS a log-power, κ ≈ 2.3–3 relative
to the diagonal (the c = 1 sets are an unconditional calibration: a pure-power fit over six decades undershoots a proved exponent
by 0.16), and the c = 2 decline has the same form and size as the c = 1 one. For c = 2, α = 0.75 the top-window slope 0.442 is even
below the UNCONDITIONAL mean-square bound 2α/3 = 0.5 from Theorem C (branch point at α/3, c/3 ∉ ℤ): a finite window undershoots a
proved lower bound for the exponent by 0.06 there. **No structured set is a counterexample; the trigger, as phrased, cannot tell one from a log-power.**

**3.5 A new design built to defeat the diagonal: online error-feedback deletion** [computed: `verify/thin2.c` mode `feedback`,
drivers `verify/run_t3.sh`, `run_t3b.sh`, `run_t3c.sh`; logs `logs/t3_kappa.log`, `logs/t3_feedback.log`, `logs/run_t3.log`].
*What was tried and why.* Theorem Z (RH) kills every R whose prime count is regular to within o(x^{α/2}) — even with a smooth
offset — so a counterexample must carry discrepancy D(x) = π_R(x) − F(x) of size ≈ x^{α/2} and use it against the integer error.
Design: sweep n = 1, …, X with the exact R-free count; at each prime p decide deletion, subject to |D| ≤ K·p^{α/2}, so as to minimise
|e|, e := N(p) − ρ̂p (ρ̂ = product over deleted primes so far × the mean tail exp(−c·E₁((1−α)ln p))); variant `corr` minimises
|e − ρ̂D| (the true error if the future D returns to 0; see the identity below). Primes in (X, Y] are decided greedily around the
frozen offset D(X). Runs: plain, α ∈ {0.6, 0.75}, c ∈ {1, 2}, K ∈ {0.5, 2, 8}, X = 10⁹ (12 runs); `corr`, α ∈ {0.6, 0.75}, c = 1,
K ∈ {0.5, 2} at 10⁹ and, for α = 0.75, at 10¹⁰. (A first `corr` build had the sign of the correction reversed; its four runs are
kept as `*_corrplus_*`, labelled, and are not used below.)
*The identity behind it* [proved here]: with ρ̂(x) as above, E(x) = e(x) + ρx∫_x^∞(D(u) − D(x))u^{−2}du + O(1 + D(x)²/x) (expand
Π_{q>x, q∈R}(1 − 1/q) against Π_{q>x}(1 − w_q/q) and integrate by parts). And deleting q changes E(y) by exactly −E(y/q) for all y
(fr Thm B step (2)): a mean-zero sawtooth at the smaller scale, so a decision has no lasting lever on E except through D.
*Results.* Plain: 10 of 12 runs have M/M_diag GROWING (κ from −0.45 to −15.7, top ratios 1.07–5600, mean-square slopes on
[10⁴, X] 0.62–1.31): the band binds (up to 3.6·10⁷ forced decisions) and D rides its edge, which by the identity adds
ρK·x^{α/2}(α/2)/(1 − α/2) to E. The other two (α = 0.75, c = 1, K = 2 and 8 — identical, the band never binds) are flat to 10⁹
(ratio 0.29, κ = −0.5 ± 0.7) and grow at 10¹⁰ (κ = −4.4 ± 1.1; max_p |D(p)|/p^{α/2} reaches 1.37 by 10¹⁰). `corr`, α = 0.6: ratios grow (3.7, 8.5).
`corr`, α = 0.75, X = 10⁹: M/M_diag falls to 0.043 (κ = 4.2 ± 0.5, pure-power slope 0.458 on [10⁴, X]) — BELOW the greedy calibration —
but the SAME controller continued to 10¹⁰ gives M/M_diag = 0.74, 0.19, 0.068, 0.024 (X = 10⁴, 6·10⁵, 10⁷, 1.6·10⁸) and then 0.077,
0.44 (6·10⁸, 2.5·10⁹); mean-square slope on [10⁷, 10¹⁰] 1.23. The 10⁹ "success" came from freezing D beyond X: continuing the
controller moves D(10¹⁰) − D(10⁹) ≈ 3·10³ and ρ by 7.6·10⁻⁸, i.e. E(10⁹) by ≈ 76 — the future term of the identity. K = 0.5 is the same.
*Mechanism of the failure.* An online design sees e, but E also contains ρx∫_x^∞(D(u) − D(x))u^{−2}du, fixed by its own FUTURE
decisions; any lasting control has to go through D, and D enters every scale. Beating the diagonal needs D irregular at scale
x^{α/2} (else Theorem Z applies) and anti-correlated with the integer error at all later scales — by Prop. 1.6, infinitely many
zeros or poles of ζ_P/ζ with real part > τ₀, for every τ₀ < α_R/2. No design here produces that.
**Close of task 3: N** — no structured R below X^{α−δ} beyond the log-power calibration of §3.4 (the one sub-calibration run is an
artefact of a frozen future); the α = 0.75 tension resolved (§3.3); rung 1 reproduced exactly (§3.2).

## §4. Close

**Close: G — the exact missing lemma is Lemma G (§1.6) — with T-parts; task 2 a named obstruction; task 3 N.**
- **T-parts** [proved here; novelty: single-check]: Theorem Z (RH): O in mean-square form (β₂ ≥ α_R/2) for every R whose prime
  zeta P_R continues with finite order to {σ > τ₀, |t| > T₀}, τ₀ < α_R/2. Corollary Z.1 (RH): every regular deletion, every c —
  including c = 2 and every c/k_c ∈ ℤ pattern, the case the brief lists as open — so **read-O's corner A8 is closed as a refutation
  corner** (U ⇒ RH, so RH-conditional is the strength that matters). Prop. 1.3 (RH, α_R < ½): β₂ ≥ α_R/4 for EVERY R — the limit of
  the reflected Carlson route. Remark 1.3′: the brief's gap lemma ("mean value for a function known only as analytic of finite
  order in a strip") is false as posed (η(2s)). §3.4: fr Theorem C holds in mean-square form (unconditional, one line). Prop. 1.1:
  the class-sum identity, with the brief's Euler product corrected by the coprimality factor (1 − p^{2σ−2}).
- **G**: Lemma G — if β₂(R) < α_R/2 then P_R continues (finite order) past α_R/2 off the real axis; equivalently (RH) ζ_P/ζ has only
  finitely many zeros and poles in some σ > τ₀, τ₀ < α_R/2. RH + Lemma G ⟹ Conjecture O for all pure deletions. Anatomy (Prop. 1.6):
  a counterexample needs π_R irregular at scale x^{α_R/2} and ζ_P/ζ with infinitely many zeros or poles of real part > τ₀ for
  every τ₀ < α_R/2 (off-line zeros of ζ_P, or critical zeros where its order differs from ζ's); P_R can have no natural boundary in σ > β₂, so any R with a natural boundary at σ ≥ α_R/2 satisfies O unconditionally.
- **Additions**: covered under a separation hypothesis (§1.7); the A-clause "any A" is probably false as stated (near-cancelling
  additions; heuristic) and should be amended.
- **Task 2**: named obstruction "sub-polynomial resonance" (§2); the working converse is the L² one on log D_R (= Theorem Z).
- **Task 3 (N)**: rung 1 exact; random R at the diagonal exponent; the α = 0.75 tension resolved by 12 seeds (top-window
  sup-slope 0.392 ± 0.016; the fr four seeds are the four highest); greedy sets below X^{α−δ} in pure-power slope but provably not
  counterexamples (log-power κ ≈ 2.3–3, calibrated by the c = 1 sets where β₂ ≥ α/2 is unconditional); the new feedback design fails
  for a proved reason (its error contains its own future discrepancy).
- **K**: none. **Stop line**: task 1 closed (G); the task-3 trigger was met only in pure-power slope, by sets covered by theorems — the
  trigger as phrased cannot separate a counterexample from a log-power and should be restated with the κ-calibration (§3.4).
*Recalled inputs.* Load-bearing and recalled: Stirling's |χ(σ+it)| = (|t|/2π)^{½−σ}(1 + O(1/|t|)) (Prop. 1.3, Theorem Z step Z3;
spot-checked to 10⁻⁶, `logs/t1_classsums.log`); standard analysis used without citation: Plancherel on L¹ ∩ L², maximum modulus,
Schwarz's lemma, Mellin inversion of Γ. Quoted at the line: MV (G.27) (Theorem G.16, MV-II draft p. 427); RH bounds for ζ, 1/ζ (BDR
z-02 ll. 1203–1205); Carlson's theorem as used by Hilberdink (w-18a p. 336); Avdeeva Thm 1. Proved here: Borel–Carathéodory
(Lemma Z.a), the Phragmén–Lindelöf instance (Lemma Z.b). Not load-bearing: Bohr–Jessen (§2(d)), the unconditional form of Remark 1.3′
(it holds under RH from the quoted inputs), the near-cancelling additions (§1.7).
*Next units.* (a) Lemma G for one irregular deterministic class (e.g. hash-defined R: prove a natural boundary of P_R at α/2 —
Prop. 1.6(i) then gives O for it); (b) Theorem Z without RH (quasi-polynomial bounds for 1/ζ on good ordinates); (c) restate the
task-3 stop line with the κ-calibration, and Conjecture O's A-clause with a separation hypothesis; (d) the dual read of Theorem Z.
