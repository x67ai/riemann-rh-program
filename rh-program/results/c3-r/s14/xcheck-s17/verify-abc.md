# Second-model verification — witnesses (a), (b), (c): Prop. 3.2, Cor. 3.4 (both assertions), completeness of S′^m

**Role.** Second-model verifier, hostile referee. Item: note §3 witnesses (a), (b), (c); companion §§2–4.
First referee's report: `refute-abc.md` (verdict HOLDS). **Nothing in it was accepted.** Every ruling below
was re-derived from the printed definitions before the first referee's file was opened for comparison.

**Machine clock at start:** (stamped below per item.)

---

## Item 0. The printed definitions, re-extracted (this is where the whole thing lives or dies)

**(3.1), published p. 15.** Raw reading-order extraction (`pdftotext -f 15 -l 15 -raw`) of the published PDF
gives, in order:

    aK,α,β,m := sup
    x∈K, ξ∈Rl
    |∂α x ∂β ξ a(x,ξ)|
    (1 + |ξ|)m−|β|
    < ∞ .                                                                  (3.1)

and the `-layout` extraction places `|∂xα ∂ξβ a(x, ξ )|` on the line **above** `‖a‖_{K,α,β,m} := sup … < ∞`
and `(1 + |ξ |)^{m−|β|}` on the line **below** it. So

> **‖a‖_{K,α,β,m} = sup_{x∈K, ξ∈R^l} |∂_x^α∂_ξ^β a(x,ξ)| / (1+|ξ|)^{m−|β|}
> = sup |∂_x^α∂_ξ^β a| · (1+|ξ|)^{|β|−m}.**

The weight is in the **denominator**. I did not rely on the layout alone. Two *internal, textual* cross-checks
in the paper itself pin the convention beyond argument, and they are independent of any rendering:

1. **Proof of Prop. 3.2, p. 17 (verbatim, control glyphs restored):**
   "For any a ∈ S̄′^m(U × R^l), and K, α and β like in (3.5), since ‖φ(a)‖′_{K,α,β,m} = ‖a‖′_{K,α,β,m} < ∞,
   there are C, R > 0 so that, if x ∈ K and |ξ| ≥ R, then |∂_x^α∂_ξ^β φ(a)(x,ξ)| / (1+|ξ|)^{m−|β|} ≤ C."
   Then, for Q = K × B_R and |∂_x^α∂_ξ^β φ(a)| < C′ on Q, the paper prints
   `|∂_x^α∂_ξ^β φ(a)(x,ξ)| / (1+|ξ|)^{m−|β|} ≤ { C′  if |β| ≤ m ;  C′(1+R)^{|β|−m}  if |β| ≥ m }`.
   The **exponent +(|β|−m) on the bounded-ξ piece** is possible only if the weight is in the denominator:
   |∂a| ≤ C′ and |ξ| ≤ R give |∂a|(1+|ξ|)^{|β|−m} ≤ C′(1+R)^{|β|−m} when |β| ≥ m, and ≤ C′ when |β| ≤ m.
   Exactly the printed case split. Under the reversed convention the split would go the other way.
2. **Proof of Prop. 3.3, p. 17:** "‖a‖′_{K,α,β,m′} = ‖a‖′_{K,α,β,m} lim_{|ξ|→∞}|ξ|^{m−m′} = 0."
   With (3.5) = sup_x limsup |∂a|/|ξ|^{m−|β|}, dividing by |ξ|^{m′−|β|} instead of |ξ|^{m−|β|} multiplies by
   |ξ|^{m−m′} → 0 for m < m′. Consistent only with the denominator convention.

**(3.4), p. 16:** ‖a‖_{Q,C^k} = sup_{(x,ξ)∈Q, |α|+|β|≤k} |∂_x^α∂_ξ^β a(x,ξ)| — these are literally the C^∞(U×R^l)
seminorms (2.1) of p. 5. **(3.5), p. 16:** ‖a‖′_{K,α,β,m} = sup_{x∈K} limsup_{|ξ|→∞} |∂_x^α∂_ξ^β a(x,ξ)| / |ξ|^{m−|β|}
(again denominator; the `′` and the `‖` survive in the byte stream as \x02 and \x0f, so the primed/unprimed
distinction on p. 17 is textually certain, not inferred).

**AGREE** with the first referee on the sign convention, by a different and stronger route (its page-image check
is corroborated here by two in-text consistency checks it did not use). **Ruling: HOLDS.**

---

## Item 1. Witness (a): g_N(x,ξ) = θ(ξ − Ne_1). Prop. 3.2 and the first assertion of Cor. 3.4

**Setup as printed.** θ ∈ C_c^∞(R^l), θ(0) = 1, supp θ ⊂ B(0,r). g_N(x,ξ) := θ(ξ − Ne_1), N ∈ N.

**(i) g_N ∈ S^{−∞}.** ∂_x^α g_N = 0 for α ≠ 0. For α = 0 and any β, m:
‖g_N‖_{K,0,β,m} = sup_ξ |∂^βθ(ξ − Ne_1)|·(1+|ξ|)^{|β|−m}. The integrand vanishes off the compact set
{|ξ − Ne_1| ≤ r}; on that set it is continuous, so the sup is finite. Finite for **every** m, so
g_N ∈ ∩_m S^m = S^{−∞} ⊂ S^m. **Verified.**

**(ii) Every (3.4) seminorm vanishes for large N.** Any compact Q ⊂ U × R^l sits in K × B̄(0,ρ). Every
∂_x^α∂_ξ^β g_N is supported in U × {|ξ − Ne_1| ≤ r} ⊂ U × {|ξ| ≥ N − r}. If N > ρ + r then N − r > ρ, so
Q ∩ supp = ∅ and ‖g_N‖_{Q,C^k} = 0. **Verified**, with the note's threshold N > ρ + r exactly right.
Since (3.4) *are* the C^∞ seminorms (2.1) of p. 5 transported to U × R^l, this is also the statement
g_N → 0 in C^∞(U × R^l).

**(iii) Every (3.5) seminorm vanishes, for every N.** Fix x. ∂_x^α∂_ξ^β g_N(x,ξ) = 0 for |ξ| > N + r, so the
quotient |∂_x^α∂_ξ^β g_N|/|ξ|^{m−|β|} is **identically 0** for |ξ| > N+r (numerator exactly 0 — no cancellation
argument needed, so the sign of m−|β| is irrelevant), hence limsup_{|ξ|→∞} = 0 for each x and
‖g_N‖′_{K,α,β,m} = 0. **Verified**, for every N, not just large N.

**(iv) The displayed lower bound, re-derived from the printed (3.1).** With α = 0 and the substitution
η = ξ − Ne_1 (a bijection of R^l, so the sup is unchanged):

  ‖g_N‖_{K,0,β,m} = sup_{η∈R^l} |∂^βθ(η)| (1+|η + Ne_1|)^{|β|−m} = sup_{|η|≤r} |∂^βθ(η)| (1+|η + Ne_1|)^{|β|−m},

the second equality because supp ∂^βθ ⊆ supp θ ⊂ B(0,r) and the expression is ≥ 0. That is the note's display
verbatim. For |η| ≤ r, |η + Ne_1| ≥ N − |η| ≥ N − r, so 1 + |η+Ne_1| ≥ max(1, 1+N−r) ≥ 1+N−r. When
**|β| > m** the map t ↦ t^{|β|−m} is strictly increasing on (0,∞), so

  ‖g_N‖_{K,0,β,m} ≥ (1 + N − r)^{|β|−m} · sup|∂^βθ| → ∞   (N → ∞),

provided ∂^βθ ≢ 0. **Verified.** (The referee note that "the bound needs N ≥ r": in fact it needs nothing —
if N < r then 1+N−r < 1 ≤ 1+|η+Ne_1| and the inequality still holds; if 1+N−r ≤ 0 the right side is not
real for non-integer exponents, so read the bound for N > r−1, which is implied by N → ∞. Cosmetic either way.)

**Numerical corroboration** (l = 1, θ(t) = e·exp(−1/(1−t²)) on |t|<1 so r = 1, θ(0)=1; ∂^βθ by 4×10^5-point
finite differences; β ∈ {1,2,3}, m ∈ {−1, 0, 0.5, 2} with |β| > m; N ∈ {2,5,10,20,40,80}): the **printed**
seminorm exceeds the note's lower bound in all 54 cases and grows like N^{|β|−m}; the **reversed-convention**
quantity sup|∂^βθ|(1+|η+Ne_1|)^{m−|β|} decays in all 54 cases. So the witness is convention-critical and the
convention established in Item 0 is the one that makes it work. Script: scratchpad `chk_a.py`.

**(v) Existence of β with |β| > m and ∂^βθ ≢ 0.** Suppose for some k ∈ N every β with |β| = k had
∂^βθ ≡ 0 on R^l. R^l is connected, so θ is a polynomial of degree ≤ k−1. A polynomial vanishing outside
B(0,r) is the zero polynomial (a nonzero polynomial has nowhere-dense zero set), contradicting θ(0) = 1.
So for **every** k there is β with |β| = k and ∂^βθ ≢ 0; take any integer k > m. **Verified.**

**(vi) Consequences.** g_N → 0 in S′^m (all (3.4) and (3.5) seminorms → 0) and in C^∞, yet (g_N) is
**unbounded** in S^m, so g_N ↛ 0 in S^m and the identity S^m → S′^m is **not** a homeomorphism.
Prop. 3.2 ("The semi-norms (3.4) and (3.5) together describe the topology of S^m(U × R^l)") is **false**,
for every m ∈ R, every nonempty open U ⊂ R^n (n ≥ 0, including U = R^0 = {0}), every l ≥ 1.
For Cor. 3.4 first assertion ("For m < m′, the topologies of S^{m′} and C^∞ coincide on S^m"): pick an
integer |β| > m′; then g_N ∈ S^{−∞} ⊂ S^m, g_N → 0 in C^∞, ‖g_N‖_{K,0,β,m′} ≥ (1+N−r)^{|β|−m′}sup|∂^βθ| → ∞,
so g_N ↛ 0 in S^{m′}. Both subspace topologies on the *set* S^m are compared and they differ. **False for
every m < m′.**

**Rescue readings tested and rejected.**
- "(3.4) and (3.5) *together with* (3.1)": excluded by the proof, which *defines* S′^m as S^m carrying only
  the (3.4)+(3.5) topology and then concludes "the identity map S^m → S′^m … is indeed a homeomorphism".
- "describe the topology" in some weaker sense (on bounded sets, say): excluded by the same sentence.
- m restricted to N_0 (as Prop. 3.3 is): the witness works verbatim for m ∈ N_0.
- l = 0: here Prop. 3.2 is **true** — β ranges over N_0^0 = {0}, |ξ| ≡ 0, so (3.1) reduces to sup_K|∂^αa| and
  (3.4) gives the same seminorms. So the note's quantifier "every l ≥ 1" is **sharp**, not sloppy. (The first
  referee did not check the l = 0 boundary; it confirms rather than damages the note.)

**AGREE with the first referee: Item 1 HOLDS.** Prop. 3.2 and the first assertion of Cor. 3.4 genuinely FALL,
and the note's derivation is correct line by line.

**Ruling: HOLDS.**
