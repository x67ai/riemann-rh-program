# NOTE — unit `conj-O-s38`: the relative square-root law for deletions (Conjecture O)

Session 38, 2026-10-01. Agent: Opus. Brief: `BRIEF.md`. Status labels as in the frontier NOTE: **[proved here]**,
**[computed]** (script + log under `verify/`), **[quoted]** (source on disk, file:line), **[recalled, unverified]**
(never load-bearing), **[heuristic]**, **[novelty: single-check]**. Paths `fr/` = `results/novel-wave-s37/beurling-frontier/`.

Notation (the brief's). R ⊂ ℙ with Σ_{p∈R}1/p < ∞; α_R := lim sup log π_R(x)/log x; P = ℙ ∖ R; N_P(x) = #{n ≤ x : (n, p) = 1
∀p ∈ R}; ρ = ρ_R = Π_{p∈R}(1 − 1/p); E(x) = E_R(x) = N_P(x) − ρx = −Σ_{m∈⟨R⟩}μ(m){x/m} (⟨R⟩ = squarefree products of
primes of R); β(R) = inf{β : E = O(x^{β+ε})}. D_R(s) = Π_{p∈R}(1 − p^{−s}) = Σ_{m∈⟨R⟩}μ(m)m^{−s} (absolutely convergent
for σ > α_R), ζ_P = ζ·D_R, P_R(s) := Σ_{p∈R}p^{−s} (the prime zeta function of R). β₂(R) := inf{σ : ∫_1^∞E(x)²x^{−2σ−1}dx < ∞}
(the mean-square exponent; β₂ ≤ β, and (1/X)∫_X^{2X}E² ≫ X^{α_R−ε} i.o. ⟹ β₂ ≥ α_R/2).

## §0. Summary (written at the close) and the digest's ranking of this unit

(placeholder — filled at the close, §4)

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
transform ∫_0^∞E(x)x^{−s−1}dx equals ζ_P(s)/s (E(x) = −ρx on (0, 1)), so Plancherel [recalled, unverified: Fourier–Plancherel
under x = e^u] gives ∫_0^∞E(x)²x^{−2σ−1}dx = (1/2π)∫|ζ_P(σ+it)|²|σ+it|^{−2}dt = (1/2π)∫|F(σ+it)|²|χ(σ+it)|²|σ+it|^{−2}dt, and
|χ(σ+it)| = (|t|/2π)^{½−σ}(1 + O(1/|t|)) [recalled, unverified; spot-checked to 10⁻⁶ at t = 50…5000, same log]. So the only
mean value of F that E controls is ∫|F(σ+it)|²|t|^{−1−2σ}dt: E = O(x^τ) permits ∫_T^{2T}|F(σ+it)|²dt ≍ T^{1+2σ} on τ < σ < ½,
i.e. a Bohr mean square of F growing like T^{2σ}. The formal diagonal being infinite contradicts no finite growth rate unless one
knows how fast its truncation at height T grows. That is the gap, and §1.3 shows it cannot be closed by growth information.

**1.3 The reflected route pushed to its limit: α_R/4, and why growth information stops there.**
*Proposition 1.3* [proved here; assumes RH; novelty: single-check]. If RH holds and α_R < ½, then β(R) ≥ β₂(R) ≥ α_R/4, for EVERY R.
*Proof.* Suppose β₂ < α_R/2 and fix σ ∈ (β₂, α_R/2), δ > 0 small. (i) For σ′ > β₂, V(σ′) := ∫_0^∞E²x^{−2σ′−1}dx < ∞, so by
Cauchy–Schwarz ∫_1^∞|E|x^{−σ″−1}dx ≤ V(σ′)^{½}(2(σ″ − σ′))^{−½} for σ″ > σ′: G(s) := ∫_0^∞E(x)x^{−s−1}dx converges absolutely,
is analytic and bounded on β₂ + δ ≤ Re s ≤ 1 − δ, and equals ζ_P(s)/s where both converge (α_R < σ < 1). Hence ζ_P = sG continues
to σ > β₂ (s ≠ 1) with |ζ_P(s)| ≪_δ |t|, and Plancherel [standard] gives ∫_T^{2T}|ζ_P(σ+it)|²dt ≤ 2π(2T+1)²V(σ) ≪ T².
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
1/6 ≤ σ < ¼ has ∫_T^{2T}|f(σ+it)|²dt ≪ T^{2−4σ} ≤ T^{1+2σ} [recalled, unverified: |χ(2s)|² ≍ t^{1−4σ} and the mean value of |ζ|²
on Re s > ½], while its diagonal Σ n^{−4σ} diverges for σ ≤ ¼ = ½·½. So "finite order + mean square T^{2σ} ⟹ convergent diagonal"
fails on (α/3, α/2); no mean-value theorem driven by growth alone closes the gap. What Carlson needs is ORDER ZERO (bounded mean
square), which E = O(x^τ) does not supply for D_R or F. The arithmetic input that does supply it is the Euler product: §1.4.

**1.4 The repair: take logarithms — the relative Hilberdink theorem.**
*Theorem Z* [proved here; assumes RH; novelty: single-check]. Let R ⊂ ℙ, Σ_{p∈R}1/p < ∞, α_R > 0. Suppose that for some
τ₀ < α_R/2, T₀ ≥ 1, A ≥ 0 the prime zeta function P_R(s) = Σ_{p∈R}p^{−s} continues analytically to U = {σ > τ₀, |t| > T₀}
with |P_R(s)| ≤ C|t|^A there. Then β(R) ≥ β₂(R) ≥ α_R/2: ∫_1^∞E²x^{−2σ−1}dx = ∞ for every σ < α_R/2, so for every ε > 0,
(1/X)∫_X^{2X}E(x)²dx ≥ X^{α_R−ε} for infinitely many dyadic X. *Contrapositive (the relative form of Hilberdink's Cor. 2(b)):*
if β₂(R) < α_R/2, then for every τ₀ < α_R/2 the function log(ζ_P/ζ) = −Σ_k P_R(ks)/k has singularities (zeros or poles of
ζ_P/ζ) in {σ > τ₀} at arbitrarily large heights, or is of infinite order there.
Two standard lemmas, proved so that nothing load-bearing is recalled:
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
