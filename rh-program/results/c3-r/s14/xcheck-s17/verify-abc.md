# Second-model verification — witnesses (a), (b), (c): Prop. 3.2, Cor. 3.4 (both assertions), completeness of S′^m

**Role.** Second-model verifier, hostile referee. Item: note §3 witnesses (a), (b), (c); companion §§2–4.
First referee's report: `refute-abc.md` (verdict HOLDS). **Nothing in it was accepted.** Every ruling below
was re-derived from the printed definitions before the first referee's file was opened for comparison.

**Machine clock at start:** Sun Sep  6 12:33:00 IST 2026 (close: 12:45:41 IST 2026).

## Verdict

**HOLDS.** Witnesses (a), (b), (c) of `alkl23-note.tex` §3 are correct as written. Prop. 3.2 FALLS for every
m ∈ R, every nonempty open U, every l ≥ 1 (true, not vacuous, for l = 0 — the note's quantifier is sharp).
"Hence S′^m(U × R^l) is complete" (p. 17) FALLS, and the first false step is exactly where the note puts it:
the identity ‖φ(a)‖′_{K,α,β,m} = ‖a‖′_{K,α,β,m} in printed lines 1–2 of p. 17. Both assertions of Cor. 3.4
FALL, the second for every m, by a 0-neighborhood of S^∞ = ind_k S^k built from the definition of the
inductive-limit topology alone. The external assessment is accurate on (a) and (b) and silent — not wrong —
on (c). **I AGREE with all four rulings of the first referee (`refute-abc.md`) and overturn none.**
Four additions it does not have (A1–A4 in Item 5), chief among them: **φ is not injective**, so the p.-17
identity fails in *both* directions and "a ≡ φ(a)" is not even well defined; and **witness (c) is logically
indispensable** — the printed derivation of Cor. 3.4's second assertion from its first is valid, so (a) does
not refute the second assertion. No repair to the note is required.

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

---

## Item 2. Witness (b): (b_j) Cauchy in S′^m with no limit; the failing sentence on p. 17

**Setup as printed.** R > 2r, c_i = (1+iR)^{m+1}, b_j = Σ_{i=1}^{j} c_i θ(ξ − iRe_1). Supports of the
translates are B̄(iRe_1, r); centers are R apart, radii r, so R > 2r gives **pairwise disjoint** supports.
Each b_j is a finite sum of terms of witness-(a) type, so b_j ∈ S^{−∞} ⊂ S^m. **Verified.**

**(i) (b_j) is Cauchy in S′^m.** For i < j, b_j − b_i = Σ_{k=i+1}^{j} c_k θ(ξ − kRe_1), which is smooth,
independent of x, has **compact** ξ-support, and that support lies in {|ξ| ≥ (i+1)R − r}.
 • (3.5): compact ξ-support ⟹ every ∂_x^α∂_ξ^β(b_j−b_i)(x,·) vanishes identically for large |ξ| ⟹
   limsup_{|ξ|→∞} = 0 for each x ⟹ ‖b_j − b_i‖′_{K,α,β,m} = 0 **for all i < j** (not merely for large i).
 • (3.4): given compact Q ⊂ K × B̄(0,ρ), once (i+1)R − r > ρ the support misses Q, so ‖b_j−b_i‖_{Q,C^k} = 0.
Every defining seminorm of S′^m is one of these; countably many suffice (paper, p. 16). Hence for each
continuous seminorm p there is i_0 with p(b_j − b_i) = 0 for j > i ≥ i_0. **Cauchy — verified**, in the strong
sense of being eventually exactly 0 on each seminorm.

**(ii) The C^∞-limit and b ∉ S^m.** The full sum b = Σ_{i≥1} c_i θ(ξ − iRe_1) is locally finite (each compact
ξ-set meets finitely many balls), hence smooth; and on each compact Q, b_j = b for j large, so b_j → b in
C^∞(U × R^l). By disjointness, b(x, iRe_1) = c_i θ(0) = c_i. Then, with the (3.1) convention of Item 0,

  |b(x, iRe_1)| · (1 + |iRe_1|)^{0−m} = (1+iR)^{m+1}(1+iR)^{−m} = 1 + iR → ∞,

so ‖b‖_{K,0,0,m} = ∞ and **b ∉ S^m**. Checked numerically for m ∈ {−3, −1, 0, 2.5}, i up to 10^3 (script
`chk_b.py`): the (3.1) quotient at ξ = iRe_1 is exactly 1+iR in every case, independent of m. **Verified.**

**(iii) No other limit is possible.** (3.4) *are* the C^∞ seminorms, so the identity S′^m → C^∞(U×R^l) is
continuous. If b_j → b̃ in S′^m with b̃ ∈ S^m, then b_j → b̃ in C^∞; C^∞ is Hausdorff and b_j → b there, so
b̃ = b, contradicting b ∉ S^m. So **(b_j) has no limit in S′^m**; S′^m is metrizable and not complete.
The printed "Hence S′^m(U × R^l) is complete, and therefore it is a Fréchet space" (p. 17) is **false**, and
with it the open-mapping step that follows it ("a continuous linear isomorphism between Fréchet spaces").
**Verified.** (Hausdorffness of S′^m is not even needed for the argument, though the paper's "LCHS" label is
correct: the (3.4) seminorms separate points.)

**(iv) The failing sentence, located and quoted verbatim.** Published p. 17, first two printed lines of the
page body (byte-level extraction with the ‖ and ′ glyphs restored from \x0f and \x02):

> "C^∞(U × R^l) is complete. **For any a ∈ S̄′^m(U × R^l), and K, α and β like in (3.5), since
> ‖φ(a)‖′_{K,α,β,m} = ‖a‖′_{K,α,β,m} < ∞,** there are C, R > 0 so that, if x ∈ K and |ξ| ≥ R, then …"

The note points at exactly this identity, and says it is "at the top of p. 17". Correct: it is the second
sentence of the page, spanning printed lines 1–2. The primes are textually confirmed (both norms in the
identity are the **(3.5)** seminorms, not (3.1) — the extraction distinguishes them).

**(v) The identity is false, and it fails in BOTH directions.**
 • *Direction ‖φ(a)‖′ > ‖a‖′ (the note's).* Let a ∈ S̄′^m be the class of (b_j). The continuous extension of
   ‖·‖′_{K,0,0,m} to the completion gives ‖a‖′ = lim_j ‖b_j‖′_{K,0,0,m} = 0 (each b_j has compact ξ-support).
   φ(a) = lim_{C^∞} b_j = b, and ‖b‖′_{K,0,0,m} = sup_x limsup_{|ξ|→∞}|b|/|ξ|^m ≥ lim_i (1+iR)^{m+1}/(iR)^m = ∞.
   So ∞ = ‖φ(a)‖′ ≠ ‖a‖′ = 0. Checked numerically for m ∈ {−3,−1,0,2.5}: the (3.5) quotient at ξ = iRe_1 is
   (1+iR)^{m+1}/(iR)^m, e.g. 2498.0 at i = 1000, m = −3, and 2503.5 at i = 1000, m = 2.5 — divergent for every
   real m, since (1+iR)^{m+1}/(iR)^m = iR·(1+1/(iR))^{m+1} → ∞.
 • *Direction ‖φ(a)‖′ < ‖a‖′ — NOT in the note, NOT in the first referee's report; this is new here.*
   Let ρ ∈ C^∞(R) with ρ = 0 on (−∞,1], ρ = 1 on [2,∞), and set u_j(x,ξ) := ρ(|ξ|/j)·(1+|ξ|²)^{m/2}
   (smooth: ρ(|ξ|/j) vanishes near ξ = 0). Then u_j ∈ S^m. For i < j, u_j − u_i vanishes on {|ξ| ≤ i} and on
   {|ξ| ≥ 2j}, so all its (3.5) seminorms are 0 and its (3.4) seminorms over Q ⊂ K × B̄(0,ρ_0) are 0 once
   i > ρ_0: **(u_j) is Cauchy in S′^m**. It converges to 0 in C^∞ (u_j ≡ 0 on |ξ| ≤ j), so φ([u_j]) = 0 and
   ‖φ([u_j])‖′_{K,0,0,m} = 0. But ‖u_j‖′_{K,0,0,m} = limsup_{|ξ|→∞}(1+|ξ|²)^{m/2}/|ξ|^m = **1** for every j
   (verified numerically to 8 places for m ∈ {−2, 0, 1.5}, j ∈ {3,10,50}), so the extended seminorm at the
   class a′ := [(u_j)] equals 1. Hence ‖φ(a′)‖′ = 0 ≠ 1 = ‖a′‖′.
   **Corollary (a strictly stronger defect than the note reports):** a′ ≠ 0 in S̄′^m (a continuous seminorm is
   nonzero on it) while φ(a′) = 0, so **φ is not injective**. The proof's conclusion "a ≡ φ(a) ∈ S^m" therefore
   does not merely have a false hypothesis — the identification a ≡ φ(a) is not even well defined. The
   completion S̄′^m is not a space of functions.

**(vi) Is the identity really the *first* false step?** The three preceding steps are all correct:
metrizability of S′^m (countably many seminorms, exhausting compacts); existence of continuous extensions of
the seminorms to the completion (uniformly continuous functions extend); existence of φ (the inclusion
S′^m ⊂ C^∞ is continuous and C^∞ is complete). The identity in (iv) is the first false assertion.
**The note's localization is exact.**

**AGREE with the first referee's ruling (Item 2 HOLDS: the note's (b) is correct and its localization exact),
and I add the φ-non-injectivity failure (v, second bullet), which neither the note nor the first referee has.**
It is not a defect in the note — the note's claim is weaker and true — but it should be recorded, because it
means the note could state the failure symmetrically ("neither inequality holds") and could point out that the
completion is not a function space at all. Optional strengthening only; no repair needed.

**Ruling: HOLDS.**

---

## Item 3. Witness (c): the second assertion of Cor. 3.4

**What has to be refuted, verbatim (p. 17).** "Corollary 3.4 For m < m′, the topologies of S^{m′}(U × R^l)
and C^∞(U × R^l) coincide on S^m(U × R^l). **Therefore the topologies of S^∞(U × R^l) and C^∞(U × R^l)
coincide on S^m(U × R^l).**"

**(0) Witness (c) is not redundant given witness (a).** The printed proof derives the second assertion FROM
the first ("For every open O ⊂ S^∞ and m′ > m, since O ∩ S^{m′} is open in S^{m′}, it follows from the first
assertion that there is some open P ⊂ C^∞ such that O ∩ S^m = P ∩ S^m") — and that derivation is **logically
valid** (O ∩ S^{m′} is S^{m′}-open by continuity of S^{m′} → S^∞; intersecting with S^m ⊂ S^{m′} and applying
the first assertion gives a C^∞-open P). [The printed sentence "it is enough to show that the topology of
S^∞ is *finer* or equal than the topology of C^∞ on S^m" is a slip for *coarser* — (3.3) already gives finer —
but the argument that follows proves the right inclusion.] Since first ⟹ second is valid, refuting the first
(witness (a)) does **not** refute the second. So (c) is doing indispensable work. **The note's structure is
correct here, and this is exactly the point the external assessment does not touch.**

**(1) The witness.** c_j(x,ξ) := e^j θ(ξ − je_1). Each c_j is a witness-(a)-type object with amplitude e^j, so
c_j ∈ S^{−∞} ⊂ S^m for every m. supp c_j ⊂ U × {|ξ| ≥ j − r}, so on any compact Q ⊂ K × B̄(0,ρ) we have
c_j ≡ 0 for j > ρ + r: **c_j → 0 in C^∞(U × R^l)** (identically 0 eventually on each compact — the amplitude
e^j is irrelevant). **Verified.**

**(2) ε_k > 0.** ε_k := ½ inf_{j≥1} e^j(1+j)^{−k}. For fixed k the sequence j ↦ e^j(1+j)^{−k} is positive and
→ ∞, so the inf is a positive minimum. Computed (mpmath, 60 dps): the minimizing integer is j = k−1 for
k ≥ 2 and j = 1 for k = 1; ε_1 = 0.6795704571, ε_5 = 8.7357e−3, ε_10 = 4.0515e−7, ε_20 = 8.5107e−19,
ε_30 = 9.5471e−33 — all strictly positive. **Verified.**

**(3) W_k is a 0-neighborhood of the step S^k.** K = {x_0} is compact ⊂ U (singletons are compact; (3.1) is
indexed by *all* compact K ⊂ U), so ‖·‖_{K,0,0,k} is one of the defining (3.1) seminorms of S^k (α = 0, β = 0,
order index m := k), and W_k = {a ∈ S^k : ‖a‖_{K,0,0,k} < ε_k} is a basic 0-neighborhood. **Verified.**

**(4) W is a 0-neighborhood of S^∞ — re-proved, not assumed.**
The paper's own definition: p. 16, "S^∞(U × R^l) = ∪_m S^m(U × R^l)"; "The LF-space S^∞(U × R^l)…";
"Since S^∞(U × R^l) is an LF-space…". p. 4, Sect. 2.1: "when the inductive/projective spectrum consists of
a sequence of continuous inclusions, their union/intersection is endowed with the inductive/projective limit
topology"; and "LF-spaces are not assumed to be strict" (so: the **locally convex** inductive limit).
Let E = ∪_k E_k with continuous inclusions, τ_ind the finest locally convex topology making all E_k → E
continuous, and 𝒰 := {W ⊂ E absolutely convex : W ∩ E_k is a 0-nbhd of E_k for every k}. Then:
 • every W ∈ 𝒰 is absorbing (each x lies in some E_k, and W ∩ E_k absorbs x there), 𝒰 is stable under finite
   intersections and nonzero scalar multiples and contains ½W with W ∈ 𝒰, so 𝒰 is a base of 0-neighborhoods
   of a locally convex topology τ_𝒰 for which each E_k → E is continuous; hence **τ_𝒰 ≤ τ_ind**;
 • conversely τ_ind is locally convex, so it has a base of absolutely convex 0-neighborhoods V, and each such
   V has V ∩ E_k a 0-nbhd of E_k, i.e. V ∈ 𝒰; hence **τ_ind ≤ τ_𝒰**.
So 𝒰 is exactly a 0-neighborhood base of τ_ind. Our W is absolutely convex by construction and
W ∩ S^k ⊇ W_k, so **W is a 0-neighborhood of S^∞**. **Verified.**
*Index set.* The note writes S^∞ = ind_k S^k over k ∈ N while the paper's union is over m ∈ R. {S^k}_{k∈N} is
cofinal in {S^m}_{m∈R} (S^m ⊂ S^{⌈m⌉} by (3.2)), and a cofinal subsystem gives the same locally convex
inductive limit; the paper grants this itself on p. 5 ("The above concepts and properties also apply to an
inductive/projective spectrum consisting of continuous inclusions X_r ⊂ X_{r′} for r < r′ in R because
∪_r X_r = ∪_k X_{r_k} and ∩_r X_r = ∩_k X_{s_k} for sequences r_k ↓ −∞ and s_k ↑ ∞"). **Observation the
first referee did not make:** that printed sentence has its two sequences **swapped** — a cofinal sequence for
the *union* of an increasing family must have r_k ↑ ∞, and for the *intersection* s_k ↓ −∞. It is a harmless
typo in ÁLKL (re-checked in the byte stream and in a raw reading-order re-extraction of p. 5, so it is not an
artifact), and the note does not depend on it: cofinality is a standard fact. Recording it only so that a
reader who chases the note's citation is not confused.

**(5) The absolutely convex hull, and the evaluation bound (sign of the exponent).**
The absolutely convex hull of a set A is exactly {Σ_{i=1}^n λ_i a_i : n ∈ N, a_i ∈ A, Σ|λ_i| ≤ 1} — this set
is balanced and convex, contains A, and is contained in every absolutely convex set containing A. So a
general element of W is Σ_i λ_i w_i with Σ|λ_i| ≤ 1 and each w_i ∈ W_{k_i} for some k_i. **Verified.**
From ‖w‖_{K,0,0,k} = sup_ξ |w(x_0,ξ)|/(1+|ξ|)^{k} < ε_k (Item 0 convention: weight in the **denominator**)
one gets |w(x_0,ξ)| < ε_k (1+|ξ|)^{**+k**} for every ξ — the exponent is **positive**, as the note has it.
At ξ = je_1 (so |ξ| = j): |w(x_0, je_1)| < ε_k (1+j)^{k}. And, taking j′ = j in the infimum defining ε_k
(legitimate for integer j ≥ 1),
  ε_k (1+j)^k ≤ ½ e^j (1+j)^{−k} (1+j)^k = ½ e^j.
Machine-checked over all 1 ≤ k ≤ 30 and 1 ≤ j ≤ 599 at 60 decimal digits: **17 970 pairs, zero violations**;
the bound is an exact equality precisely at the minimizing j (as it must be), never exceeded. Script `chk_c.py`.

**(6) The contradiction.** c_j(x_0, je_1) = e^j θ(0) = e^j. If c_j = Σ_i λ_i w_i ∈ W then
  e^j = |c_j(x_0,je_1)| ≤ Σ_i |λ_i| |w_i(x_0,je_1)| < Σ_i |λ_i| ε_{k_i}(1+j)^{k_i} ≤ (Σ_i|λ_i|)·½e^j ≤ ½ e^j,
impossible. (The strict step uses that some λ_i ≠ 0, which holds because c_j ≠ 0; but the argument does not
need strictness at all — e^j ≤ ½ e^j is already false.) So **c_j ∉ W for every j ≥ 1**. **Verified.**

**(7) Conclusion, and "for every m".** W is a 0-neighborhood of S^∞, so W ∩ S^m is a 0-neighborhood of S^m
in the topology induced from S^∞, for **every** m ∈ R (continuity of S^m → S^∞ — no separate argument
needed). All c_j lie in S^{−∞} ⊂ S^m, c_j → 0 in the C^∞-induced topology, c_j ∉ W ∩ S^m. So the two induced
topologies on the set S^m differ, for **every** m ∈ R, every nonempty open U, every l ≥ 1.
**The second assertion of Cor. 3.4 is false for every m.** **Verified.**

**(8) "No regularity of S^∞ is used" — correct.** The proof used only (i) the definition of the locally convex
inductive-limit topology, re-proved in (4); (ii) one (3.1) seminorm of each step; (iii) the definition of the
absolutely convex hull. It uses no acyclicity, regularity, retractivity or completeness of S^∞ — in particular
it does not use Cor. 3.6, which is itself derived from Cor. 3.4 and would be circular. This is the contrast
with the paper's own Remark 3.8, whose argument does invoke "S^∞(U × R^l) is sequentially retractive
(Corollary 3.6)". **Verified.**

**AGREE with the first referee: Item 3 HOLDS.**

**Ruling: HOLDS.**

---

## Item 4. Does the external assessment describe witnesses (a), (b), (c) accurately?

**The reader's copy.** The external reader had arXiv:2304.00798**v3**. I re-extracted that PDF myself
(`pdftotext -raw fetched-r3/r3s-38-…v3….pdf`) and read the relevant block (lines ≈1170–1365 of my
extraction). (3.1) is printed there as `kakK,α,β,m := sup_{x∈K, ξ∈Rl} |∂α_x ∂β_ξ a(x,ξ)| / (1 + |ξ|)^{m−|β|}`
— same denominator convention; (3.4), (3.5), Prop. 3.2 and its whole proof (including
`kφ(a)k′_{K,α,β,m} = kak′_{K,α,β,m} < ∞`, the case split `C′ if |β| ≤ m / C′(1+R)^{|β|−m} if |β| ≥ m`,
"Hence S′m(U ×Rl) is complete, and therefore it is a Fréchet space", and the open-mapping sentence),
Prop. 3.3 and Cor. 3.4 with its proof are **verbatim identical** to the published pp. 15–17. v3 also
prints the completion with a hat (`b S′m`), confirming the Ŝ′^m reading. So the reader was looking at
the same statements. **Verified independently of the first referee.**

**Clause by clause.**
 • "The paper defines the full symbol topology using the seminorms (3.1), then introduces the weaker-looking
   seminorms (3.4) and (3.5), and claims that those latter seminorms still describe the topology." — **accurate**.
 • On (a): "…goes to zero for the local C^∞-type seminorms and for the tail seminorms (3.5), while a
   sufficiently high ξ-derivative makes the genuine symbol seminorm blow up. Thus g_N→0 in the proposed weaker
   topology but is unbounded in S^m. That directly contradicts Proposition 3.2 and the first assertion of
   Corollary 3.4." — **accurate in every clause**, and correctly restricted to the *first* assertion.
 • On (b): "…are Cauchy for the weaker topology, but their C^∞-limit is not in S^m. The paper's proof of
   completeness explicitly extends the proposed seminorms to the completion and then asserts that the image
   remains in S^m. Your construction attacks exactly that step." — **accurate**. Its localization names the
   conclusion "a ≡ φ(a) ∈ S^m" rather than the seminorm identity one sentence earlier; that is coarser than
   the note's, not wrong. It does not address whether (b_j) might converge in S′^m to some *other* element —
   a real hole in its reasoning, closed by Item 2(iii) here.
 • On (c): the assessment **never mentions** c_j = e^jθ(ξ − je_1), the absolutely convex hull W, S^∞, or the
   second assertion of Cor. 3.4. Its bottom line lists "Corollary 3.4" undifferentiated. So it is **silent, not
   wrong**, on (c): it endorses a conclusion whose mechanism it neither states nor checks. Item 3 here shows
   the conclusion is correct, so the endorsement is not misleading — but the assessment must **not** be read as
   an independent verification of the second assertion's refutation, which is the harder of the two and does
   not follow from (a) (Item 3(0)).
 • "The paper really does make those topology-coincidence claims." — **accurate** for Prop. 3.2 and both
   assertions of Cor. 3.4 (verbatim in Item 0 and above).

**AGREE with the first referee. Ruling: HOLDS.**

---

## Item 5. Deltas: where I add to, or correct, the first referee

The first referee's four rulings are all **AGREE**. Independent additions and two small corrections:

**A1 (new; Item 2(v), second bullet). φ: Ŝ′^m → C^∞ is not injective, and the p.-17 identity fails in the
other direction too.** With ρ ∈ C^∞(R), ρ = 0 on (−∞,1], ρ = 1 on [2,∞), put u_j(x,ξ) = ρ(|ξ|/j)(1+|ξ|²)^{m/2}
∈ S^m. Then (u_j) is Cauchy in S′^m (u_j − u_i vanishes on {|ξ| ≤ min(i,j)} ∪ {|ξ| ≥ 2max(i,j)}, so *all* its
(3.5) seminorms are 0 and its (3.4) seminorms over Q ⊂ K × B̄(0,ρ_0) are 0 once min(i,j) > ρ_0), u_j → 0 in
C^∞, so φ([u_j]) = 0; but ‖u_j‖′_{K,0,0,m} = limsup_{|ξ|→∞}(1+|ξ|²)^{m/2}/|ξ|^m = 1 for every j (numerically
1.00000000 to 8 places for m ∈ {−2,0,1.5}, j ∈ {3,10,50}), so the extended seminorm at a′ := [(u_j)] is 1 and
a′ ≠ 0. Hence ‖φ(a′)‖′ = 0 < 1 = ‖a′‖′. Combined with the note's b-example (∞ > 0), **neither inequality
between ‖φ(a)‖′ and ‖a‖′ holds**, and the proof's identification "a ≡ φ(a)" is not well defined at all: the
completion Ŝ′^m is not a space of functions. This strengthens, and does not disturb, the note.
The first referee wrote "not even the inequality ‖φ(a)‖′ ≤ ‖a‖′ survives"; the symmetric failure is new here.

**A2 (new; Item 3(0)). Witness (c) is indispensable.** The printed derivation of the second assertion of
Cor. 3.4 *from* the first is valid, so refuting the first (witness (a)) leaves the second standing. This is why
the external assessment's silence on (c) matters, and why (c) is not a duplicate of (a). Neither the note nor
the first referee states this explicitly; it is the strongest argument that (c) earns its place.

**A3 (new). The printed proof of Cor. 3.4's second assertion contains a wording slip**: "by (3.3), it is
enough to show that the topology of S^∞(U × R^l) is **finer** or equal than the topology of C^∞(U × R^l) on
S^m(U × R^l)" — (3.3) already gives *finer*; what remains to prove, and what the argument that follows
actually proves, is *coarser or equal*. Harmless to the paper's logic, and irrelevant to the note; recorded so
that nobody mistakes it for the error.

**A4 (new). The p. 5 "real-index license" the note's companion cites is misprinted in ÁLKL**: "∪_r X_r =
∪_k X_{r_k} and ∩_r X_r = ∩_k X_{s_k} for sequences r_k ↓ −∞ and s_k ↑ ∞" has the two sequences swapped
(an increasing family needs r_k ↑ ∞ to be cofinal for the union). Confirmed in both a layout and a raw
reading-order extraction, so it is not a pdftotext artifact. The note does not depend on it — cofinality of
{S^k}_{k∈N} in {S^m}_{m∈R} is standard and re-proved in Item 3(4).

**A5 (correction to the first referee, cosmetic).** Its Item 1 says "for l = 0 the statements are vacuous".
They are not vacuous — they are **true**: for l = 0, β ranges over N_0^0 = {0} and |ξ| ≡ 0, so (3.1) reduces to
sup_K|∂^α a|, which is exactly (3.4). So Prop. 3.2 and Cor. 3.4 hold for l = 0, and the note's quantifier
"every l ≥ 1" is sharp rather than merely cautious. No consequence for any verdict.

**A6 (correction to the first referee's "cosmetic remarks", cosmetic).** It lists "the (a) bound needs N ≥ r".
It does not: for N < r one still has 1 + |η + Ne_1| ≥ 1 > 1 + N − r, so the displayed inequality holds for
every N with 1 + N − r > 0, and the only genuinely needed hypothesis is N > r − 1, implied by N → ∞.

**A7 (observation, no consequence).** In witness (c) the translates θ(ξ − je_1) are spaced by 1, so their
supports overlap when r ≥ ½. This is harmless: c_j is a *single* term, not a sum, and c_j(x_0, je_1) = e^jθ(0)
= e^j regardless. (Disjointness is needed only in witness (b), where R > 2r is imposed.)

**A8 (observation about the paper, not the note).** Prop. 3.3 is stated only "For m, m′ ∈ N_0", while Cor. 3.4
("For m < m′") is deduced from it for arbitrary reals. Prop. 3.3 is in fact true for all real m < m′ (for
a ∈ S^m the limsup defining ‖a‖′_{K,α,β,m} is finite, and multiplying by |ξ|^{m−m′} → 0 kills it), so this is a
harmless under-statement in the paper, not an additional error, and the note is right not to list Prop. 3.3.

---

## Verdict (final)

**HOLDS.** Independently re-derived: witness (a) refutes Prop. 3.2 and the first assertion of Cor. 3.4 for
every m ∈ R, every nonempty open U, every l ≥ 1 (and the statements are *true* for l = 0, so the note's
quantifier is sharp); witness (b) refutes "Hence S′^m(U × R^l) is complete" (p. 17) and localizes the first
false step exactly at the identity ‖φ(a)‖′_{K,α,β,m} = ‖a‖′_{K,α,β,m} in printed lines 1–2 of p. 17; witness
(c) refutes the second assertion of Cor. 3.4 for every m, using nothing but the definition of the locally
convex inductive limit. The (3.1) convention on which everything turns (weight in the denominator) is fixed
by three mutually independent readings of the source. Every ruling of the first referee is **AGREED**; nothing
in it is overturned. Additions A1–A4 strengthen the case (chiefly: φ is not injective, and witness (c) is
logically indispensable rather than a duplicate of (a)); A5–A8 are cosmetic corrections and observations.
**No repair to the note is required.**

Machine clock at close: appended below.
Sun Sep  6 12:45:41 IST 2026

**Scripts** (durable copies): `results/c3-r/s14/xcheck-s17/verify-abc-scripts/{chk_a,chk_b,chk_c}.py`.
