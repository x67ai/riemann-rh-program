# Dual-model check (Opus 5) of the Session-15 classification of Lamzouri arXiv:2609.02882

**Date.** 2026-09-05 (Session 16). **Checker.** Opus 5, acting as the SECOND model under standing
order 7. **First model.** Fable 5.1, Session 15 (2026-09-03), single-check.
**Method.** Sections 1 and 2 below were derived from the primary sources only (the paper's own text
at `sources-extracted/lamzouri-2609.02882v1.txt` and the PairCeiling definitions quoted in
`results/full-map.md`), and every number in them was recomputed from scratch with mpmath 1.3.0 at
40 decimal digits (`dual-check-O-K2ieps.py`, output in `dual-check-O-K2ieps.out`). The Session-15
files were opened only afterwards; Section 3 is the line-by-line comparison.

---

## 0. Verdict table

| Item | Question | Verdict |
|---|---|---|
| **A** | II.1 membership: is Lamzouri's Prop. 2.1 a bandwidth-one PairCeiling certificate, with value 0.6725007 under the ceiling 0.6818287? | **CONFIRMED-WITH-CORRECTIONS** |
| **B** | II.4 degeneracy: is the double/deep-pair indistinguishability of `lemmaR_tight` reproduced exactly, consuming no invariant outside {tr, ‖·‖²_F, n₊, integer atoms}? | **CONFIRMED-WITH-CORRECTIONS** |
| **C** | Other sentences in the Session-15 dated notes and the A4/riders cross-check | **CONFIRMED-WITH-CORRECTIONS** |
| **Overall** | | **AGREES-WITH-CORRECTIONS** |

**What survives.** The classification is right. Lamzouri's Proposition 2.1 is a bandwidth-one,
configuration-by-configuration certificate in exactly the PairCeiling sense; II.1 binds it; its
value 2 − C_MT = 0.672500703679… sits 0.00934 below the ceiling that its own regularity data
buys (0.681837…); the subclass diagnosis is correct; the II.4 degeneracy is reproduced exactly,
with all three Session-15 numerics confirmed to the digits quoted.

**What must change.** The explicit pair (c₀, r) recorded in the II.1 dated note is wrong under the
program's own PairCeiling normalization: it is not `c₀ = 2, r = −(η²∗η²)` but
`c₀ = 2 − (η²∗η²)(0), r = −2(η²∗η²)` restricted to [0,1]. The stated pair has value ≈ 1.839, not
0.6725, so as written it is not a certificate of the claimed value at all. One characterization in
the II.4 note ("a² + 1 ≥ 2a per basis direction") is also inaccurate — the proof uses three
different per-direction inequalities on the three nested ranges. Exact replacement wording is in
Section 3.

---

## 1. Item A — the explicit certificate, its normalization, its regularity, its value

### 1.1 What the paper proves, in its own notation

Fourier convention, the paper's (2.3): `f̂(ξ) = ∫_R f(u) e^{−2πiξu} du`, extended to ξ ∈ C
(entire, since f is compactly supported). Proposition 2.1: for λ > 0, η ∈ L²(R) real, even,
supp η ⊂ (−λ, λ), with `η̂²(0) = 1`, and Z any non-empty finite multiset of complex numbers
invariant under complex conjugation,

    #{z ∈ Z ∩ R : m_z = 1}  ≥  2 Σ_{z∈Z} 1  −  Σ_{z,s∈Z} K(z−s)²,      K := η̂²,

both sums taken over the multiset (that is, `Σ_{z,s∈Z} K(z−s)² = Σ_{z,s distinct} m_z m_s K(z−s)²`).
Its companion (2.5) bounds the number of distinct elements below by
`(3/2)Σ_{z∈Z} 1 − (1/2)Σ_{z,s∈Z} K(z−s)²`.

Section 3 applies this to `Z_T = { i(ρ − 1/2)·(log T)/(2π) : 0 < γ ≤ T }`, which is
conjugation-invariant by the functional equation, real exactly at the on-line zeros and simple
exactly at the simple zeros. With `f := η² ≥ 0`, `∫f = η̂²(0) = K(0) = 1`, `supp f ⊂ (−1/2, 1/2)`,
and `Q := f ∗ f` (so `Q̂ = K²`, supp Q ⊂ (−1,1)), Lemma 3.2 removes the pair-correlation weight
`w = 4/(4 − z²)` by writing `r_{δ,T} = Q − Q″/(4 log²T)` and applying BGSTB24's Lemma 5
(= his Lemma 3.1) separately to Q and to Q″. The outcome is

    Σ_{ρ,ρ'} K( i(ρ−ρ') (log T)/(2π) )²  =  ( C_η + o(1) ) · (T/2π) log T,
    C_η := Q(0) + 2∫₀¹ α Q(α) dα,      N(T) ~ (T/2π) log T,

hence `liminf N₀ˢ(T)/N(T) ≥ 2 − C_η`, and with the Montgomery–Taylor window `C_η → C_MT`.

### 1.2 Reading the right-hand side as form-factor data

For a real multiset Z of total mass n = Σ_z m_z, with Q̂ = K²,

    (1/n) Σ_{z,s∈Z} K(z−s)²  =  (1/n) ∫_R Q(u) |Σ_z m_z e^{−2πizu}|² du  =  ∫_{−1}^{1} Q(u) F_Z(u) du,

where `F_Z(u) := (1/n)|Σ_z m_z e^{−2πizu}|²` is exactly the configuration's form factor. Q is even,
so `∫_{−1}^{1} Q F_Z = Q(0)·(mass of the α = 0 atom) + 2∫₀¹ Q(x) · (bulk density)(x) dx`. For an
N-periodic marked configuration — which is what the ceiling's 256-law consists of — apply
Proposition 2.1 to the K-fold repetition and let K → ∞: the Fejér kernel `(1/K)|D_K(Nu)|²`
converges weakly to `(1/N)Σ_j δ(u − j/N)`, so the integral becomes the grid sum
`Σ_{j} Q(j/N) S(j)/N` with `S(j) = |Σ_i m_i e^{2πij x_i/N}|²/N`. The j = 0 term has mass
`S(0)/N = (Σ_i m_i)²/N² = 1` whenever the configuration carries total mass N (the law's own
normalization). This is the form factor's coherent **α = 0 atom**: the finite-configuration
counterpart of Montgomery's `T^{−2|α|}log T` spike, and the term that produces the `f(0)` on the
right-hand side of Lemma 3.1. Its mass is 1 at every configuration of the class, so it is a
constant of the class, not a variable one. The remaining j ≥ 1 masses `s_j = S(j)/N` are the ceiling's grid masses; for the
near-CUE law `S(j) = j/N + O(τ)`, hence `s_j ≈ j/N²` and `Σ_{j ≤ Nx} s_j → x²/2 = ∫₀ˣ t dt`,
which is precisely the reference cumulant the ceiling's `D(x) = C(x) − x²/2` measures against.

### 1.3 The certificate, explicitly

Dividing Proposition 2.1 by n and folding as above,

    p₁  ≥  2 − Q(0) − 2∫₀¹ Q(x) · (bulk)(x) dx,     i.e.     c₀ + Σ_{j≥1} s_j r(j/N) ≤ p₁

with

    **c₀ = 2 − Q(0) = 2 − ∫ (η²)² = 2 − ∫ η⁴,      r(x) = −2 Q(x) = −2 (η² ∗ η²)(x)  on [0,1].**

The α = 0 atom sits inside c₀ (its mass is 1 at every configuration of the class, so it contributes
the same constant Q(0) everywhere and cannot be carried by r, which is only ever evaluated at the
bulk grid points j/N, j ≥ 1); the factor 2 sits inside r because the ceiling's value functional
`v = c₀ + ∫₀¹ r(x)·x dx` pairs r against the **one-sided** density `x dx` on [0,1] while the
physical pairing is two-sided over [−1,1]. Then

    v = c₀ + ∫₀¹ r(x) x dx = 2 − Q(0) − 2∫₀¹ x Q(x) dx = 2 − C_η,

which is Lamzouri's proportion, as required. (The distinct-zeros companion (2.5) is the certificate
`c₀ = 3/2 − Q(0)/2`, `r = −Q`, of value `(3 − C_η)/2 = 0.836250…`.)

**Independent pin on the normalization.** The same reading applied to the parent paper's Theorem B
(flat window, λ = 1) must return 2/3. There `f = (1/λ)·1_{[−λ/2,λ/2]}`, `Q(x) = (λ − |x|)₊/λ²`, so
`Q(0) = 1/λ` and `Q(0) + 2∫₀^λ xQ(x)dx = 1/λ + λ/3 = κ(λ)` — the program's own two-moment constant
(full-map: `‖Ĝ‖²_F = (1/λ₁ + λ₁/3)N`, and Remark 5.10's identification
`tr G̃² ↔ ∫_{−λ}^{λ}(λ−|α|)F(α)dα = λ + λ³/3`). At λ = 1 this gives `c₀ = 1`, `r(x) = −2(1−x)`,
and `v = 1 + ∫₀¹ −2(1−x)x dx = 1 − 1/3 = 2/3` **exactly** — matching full-map's recorded gap
`0.68182868746 − 2/3 = 0.01516202…`. No other placement of the diagonal or of the factor 2
reproduces 2/3, so this fixes the convention beyond doubt.

### 1.4 Regularity, at the Montgomery–Taylor extremal itself

Lemma 3.2's extremal window is `f₀(x) = cos(√2 x)/(√2 sin(1/√2))` on `I = [−1/2, 1/2]`, 0 outside;
`∫f₀ = 1` (verified numerically to 30 digits). `f₀` is **not** continuous on R — it jumps at ±1/2,
with `f₀(1/2⁻) = cot(1/√2)/√2` — so `Q₀ = f₀ ∗ f₀` has a corner at 0 and a kink at ±1. That is
irrelevant here, because the ceiling only reads r on the closed interval [0,1], and there Q₀ is
**real-analytic**. Explicitly, for 0 ≤ x ≤ 1,

    Q₀(x) = A² [ sin(√2(1−x))/(2√2) + (1−x) cos(√2 x)/2 ],        A = 1/(√2 sin(1/√2)),

verified against direct numerical convolution at x = 0, 0.25, 0.6, 0.999 (agreement to 25 digits).
Hence `r = −2Q₀|₍₀,₁₎ ∈ C^∞[0,1]`, r″ is continuous and integrable (no exceptional set is even
needed), and the ceiling's regularity hypothesis is met **outright**: no approximation argument,
no continuity-in-(|r′(1)| + ∫|r″|) limiting argument, is required. The same is true of every
admissible `η_δ ∈ C_c^∞` of Lemma 3.2, for which Q_δ ∈ C_c^∞((−1,1)) is smooth everywhere.

Endpoint data, computed exactly and numerically:

* `r(1) = −2Q₀(1) = 0` **exactly** (`Q₀(1) = 0` from the closed form; the supports satisfy
  supp Q₀ = [−1,1] with Q₀ vanishing at the endpoints). So the edge term `|r(1)||D(1)|` is not
  merely dropped by the sign condition r(1) ≥ 0 — it is identically zero, which is stronger and
  independent of the value of D(1).
* `|r′(1)| = 2A² cos²(1/√2) = 1.36951017082213778…`
* `r″` changes sign exactly once on [0,1]; `∫₀¹|r″| = 1.95649621485767629…`
* budget `|r′(1)| + ∫₀¹|r″| = 3.32600638567981407…`

### 1.5 The value, and the ceiling

Recomputed at 40 digits:

    Q₀(0) = ∫ f₀² = 1.00612719086582862264…            (closed form and quadrature agree)
    2∫₀¹ α Q₀(α) dα = 0.32137210545475973162…
    C_MT = Q₀(0) + 2∫₀¹ αQ₀ = 1.32749929632058835426…
    closed form 1/2 + (1/√2)cot(1/√2) = 1.32749929632058835426…   (difference 0.0 at 40 digits)
    c₀ = 2 − Q₀(0) = 0.99387280913417137735…
    v  = c₀ + ∫₀¹ r(x) x dx = 0.67250070367941164573…
    2 − C_MT = 0.67250070367941164573…  =  3/2 − (1/√2)cot(1/√2)  ✓

Ceiling at this r: `0.68182868746 + 2.5431316·10⁻⁶ × 3.326006… = 0.681837145931941…`.

    v = 0.672500703679…  <  0.681837145932…      headroom 0.00933644225252957838

So **the value is under the ceiling**, comfortably, and II.1 binds Lamzouri's certificate. (With
the ceiling quoted in its rounded headline form 0.6818287, the gap is 0.009327983781.)

### 1.6 The subclass statement

Correct in substance, and worth stating more sharply than Session 15 did. The ceiling's class is
all pairs (c₀, r) with r ∈ C¹[0,1], r″ integrable off a countable set, subject only to
configuration-by-configuration validity. Lamzouri's method does not deliver a free pair: it
delivers the **one-function family**

    { ( 2 − (f∗f)(0),  −2 (f∗f)|₍₀,₁₎ )  :  f ≥ 0,  ∫f = 1,  supp f ⊂ (−1/2, 1/2) },

so c₀ is *determined* by r, and r is constrained to be minus twice an autoconvolution of a
non-negative probability density of support ≤ 1/2 — in particular r ≤ 0, r(1) = 0, r convex or
not depending on f but always of positive-definite type (−r/2 has non-negative Fourier transform
K² ≥ 0 on R). That is a very thin subfamily of the ceiling's class. Optimizing inside it is
exactly the one-delta Montgomery–Taylor extremal problem, and the paper's Remark 3.4 says so, in
these words:

> "It follows from Corollary 14 of Carneiro, Chandee, Littmann and Milinovich [6] that C_ηε ⩾ C_MT.
> The corresponding extremal function was originally identified by Montgomery and Taylor [20].
> Together with the preceding construction, this shows that C_MT is the optimal constant that one
> can obtain using our method."

So the family's optimum is exactly 2 − C_MT = 0.6725007…, and the distance to the ceiling is a
subclass-versus-class gap. **One caveat Session 15 did not state:** 0.6818287 is an *upper bound*
on what the full class can certify, not a value known to be attained; the true class optimum lies
somewhere in [0.6725007, 0.6818372], and nothing here shows that any valid certificate beats
0.6725007. The gap is therefore an upper bound on the available headroom, not a promised prize.
(Zoo II.1 already records the neighboring honest number: the RH-conditional Chirre–Gonçalves–de Laat
0.6792 uses a constraint the 256-law violates, so it lives outside this class.)

---

## 2. Item B — the II.4 degeneracy in Hilbert-space form

### 2.1 K at imaginary argument

With the paper's convention (2.3), for real ε,

    K(2iε) = η̂²(2iε) = ∫ η(u)² e^{−2πi(2iε)u} du = ∫ η(u)² e^{4πεu} du = ∫ η(u)² cosh(4πεu) du,

the last step because η is even (the sinh part is odd and integrates to 0). So K(2iε) is real,
K(2iε) ≥ ∫η² = K(0) = 1 by cosh ≥ 1, with equality iff ε = 0 (η ≢ 0). This is the same K the paper
uses: (2.7) reads `K(z−s) = η̂²(z−s) = ∫_{−λ}^{λ} f_z(u) \overline{f_s(u)} du` for complex z, s, and
Proposition 2.1's right-hand side is `2Σ_{z∈Z}1 − Σ_{z,s∈Z}K(z−s)²` with those complex arguments.

### 2.2 The two configurations

**(i) One on-line double at real x (m_x = 2).** Z = {x, x}. Then Σ_{z∈Z}1 = 2 and
Σ_{z,s∈Z}K(z−s)² = m_x² K(0)² = 4. Right-hand side of (2.4) = 2·2 − 4 = **0**. In the proof's own
terms: R₁ = ∅ (n = 0), R₂ = {x} (r = 1), S = ∅ (k = 0); U = V = W = span{f_x}, D_U = D_V = D_W = 1,
ψ₁ = f_x (‖f_x‖² = K(0) = 1), α₁ = m_x|⟨f_x,ψ₁⟩|² = 2. Bessel (2.14) is an **equality**
(F = 2 ψ₁⊗ψ₁), and the first-range inequality a² + 4 ≥ 4a is an **equality** at a = 2. Nothing is
discarded anywhere.

**(ii) An off-line conjugate pair x ± iε, both simple.** Z = {x+iε, x−iε}, m = 1 each. Then
Σ_{z∈Z}1 = 2 and Σ_{z,s∈Z}K(z−s)² = 2K(0)² + K(2iε)² + K(−2iε)² = **2 + 2K(2iε)²**, so the
right-hand side of (2.4) is **2 − 2K(2iε)² ≤ 0**, with equality iff ε = 0. In the proof's terms,
with z = x+iε: g_z(u) = η(u)e^{−2πiux}cosh(2πεu), h_z(u) = −i η(u)e^{−2πiux}sinh(2πεu); these are
orthogonal (the integrand of ⟨g,h⟩ is odd), and

    ‖g_z‖² = (1 + K(2iε))/2,    ‖h_z‖² = (K(2iε) − 1)/2,    ‖g‖² − ‖h‖² = 1  (the paper's (2.9)),

giving D_U = 1 (ψ₁ = g/‖g‖), D_V = 1, D_W = 2 (ψ₂ = h/‖h‖), and
`α₁ = 2‖g‖² = 1 + K(2iε)`, `α₂ = −2‖h‖² = 1 − K(2iε)`. Then `Σα_j = 2 = Σ_{z∈Z}1` (the paper's
(2.21)) and `Σα_j² = (1+K)² + (1−K)² = 2 + 2K²` — Bessel is again an **equality**, because F is
diagonal in this basis. The three per-range slacks are: first range `(α₁ − 2)² = (1−K)²`; middle
range empty; top range `α₂² − 2α₂ = (K−1)² + 2(K−1)`. All vanish as ε → 0.

So both configurations converge, as ε → 0, to the *same point* of the invariant space
`(Σ_z 1, Σ K², D_U, D_V, D_W) = (2, 4, 1, 1, 1)`, and the certificate returns 0 for both. That is
`lemmaR_tight`'s charge-4 degeneracy verbatim: at c = 2 the on-line double carries
`k₂(2) = c² − ((c−2)₊)² = 4` and a single pair block carries `c²·b = 4·1 = 4`. Moreover, for ε > 0
the pair is charged **more** (ΣK² = 2 + 2K² > 4), so the certificate's output moves the wrong way
for separation: it is weakest exactly where a separation would have to be strongest.

### 2.3 What is discarded, and why none of it separates the two

The proof consumes exactly four things: `Σ_j α_j = Σ_{z∈Z} 1` (trace, (2.21)); `∬|F|² =
Σ_{z,s}K(z−s)²` (Hilbert–Schmidt norm, (2.10)); the dimension counts D_U ≤ D_V ≤ D_W with
`D_V − D_U ≤ n` (the rank / positive-index data, supplied by the nesting U ⊂ V ⊂ W and the sign
α_j ≤ 0 above V); and integrality, via `m_{x_ℓ} ≥ 2` for the non-simple real atoms. Discarded:

1. **The off-diagonal Bessel coefficients** `⟨F, ψ_j ⊗ ψ_ℓ⟩, j ≠ ℓ` — dropped when (2.14) keeps
   only the diagonal Ψ_j = ψ_j ⊗ ψ_j. This is the Frobenius-minus-diagonal gap. It **vanishes for
   both** configurations above (F is diagonal in each case), so it cannot separate them.
2. **`a² + 4 ≥ 4a` on 1 ≤ j ≤ D_U**, slack (a−2)²: 0 for the double, (1−K)² → 0 for the pair.
3. **`a² + 1 ≥ 2a` on D_U < j ≤ D_V**, slack (a−1)²: this range is **empty for both**.
4. **`α_j² ≥ 2α_j` on D_V < j ≤ D_W** (using α_j ≤ 0), slack α_j² + 2|α_j|: 0 for the double,
   (K−1)² + 2(K−1) → 0 for the pair.
5. **Bessel for the h_z in the U-range**, `Σ_{j≤D_U}|∫h ψ_j|² ≤ ‖h‖²`: an equality in both cases.
6. **`n ≥ D_V − D_U`**: both sides are 0 in both cases.

Every discarded quantity is zero at the double and tends to zero at the pair. So no reading of any
slack separates them either. Confirmed: nothing outside {tr, ‖·‖²_F, n₊, integer atoms} is consumed.

### 2.4 Numerics (Montgomery–Taylor window η² = f₀), 40-digit mpmath

Script `dual-check-O-K2ieps.py`; output `dual-check-O-K2ieps.out`. `K(2iε)` computed two ways
(direct quadrature and the closed form `A·2[b sin(b/2)cosh(c/2) + c cos(b/2)sinh(c/2)]/(b²+c²)`,
b = √2, c = 4πε), agreeing to < 10⁻²⁵.

| ε | K(2iε) | K(2iε)² | Σ_z 1 | Σ_{z,s} K(z−s)² | RHS of (2.4) |
|---|---|---|---|---|---|
| double (m=2) | — | — | 2 | 4 | 0 |
| 0 (pair) | 1.0 | 1.0 | 2 | 4 | 0 |
| 0.001 | 1.000006119110861499 | 1.000012238259166516 | 2 | 4.000048953036666063 | −2.4476518333·10⁻⁵ |
| 0.01 | 1.000612026858751520 | 1.001224428294378874 | 2 | 4.002448856588757747 | −0.00244885658876 |
| 0.1 | 1.062371152745061533 | 1.128632466184870863 | 2 | 4.257264932369741726 | −0.25726493237 |
| 0.5 | 3.454214544266386062 | 11.93159811782143716 | 2 | 25.86319623564287432 | −21.8631962356 |

Session-15's quoted `1.00122 / 1.1286 / 11.93` are **confirmed** at every digit quoted
(1.0012244…, 1.1286325…, 11.931598…).

---

## 3. Line-by-line comparison with the Session-15 notes, and exact replacement wording

Read only after Sections 1 and 2 were written. Sources compared: `ASSESSMENT.md` §2–§3 and
`README.md` in this directory; `BARRIER-ZOO.md` II.1 and II.4 dated notes; the dated note at the end
of `directions/A4-lindelof-lock.md`; the dated note in `results/arxiv/README.md`; `STATUS.md` line 71.

### 3.1 What is right, and stays

| Session-15 sentence | Verdict |
|---|---|
| Prop. 2.1 holds for every finite conjugation-invariant multiset, hence is a certificate valid configuration-by-configuration | **correct** |
| The II.1 ceiling binds it | **correct** (value 0.672500703679 < ceiling 0.681837145932 for its own r) |
| Lamzouri's admissible r are minus autoconvolutions of non-negative normalized functions of support ≤ 1/2, a subclass | **correct**, and sharper than stated: c₀ is determined by r, so the family is one-function, not a free pair |
| The route lands at 2 − C_MT = 0.6725 because of that subclass, not at 0.6818 | **correct** as a statement about the subclass optimum; needs one caveat (3.3) |
| Remark 3.4: C_MT optimal for the method, by CCLM 2017 Cor. 14 | **correct**; the paper's exact sentence is quoted in §1.6 above |
| Σ_j α_j = Σ_z m_z is a trace (his 2.21); ‖F‖² = Σ K(z−s)² (his 2.10); Bessel ‖F‖² ≥ Σ α_j² | **correct** |
| The U ⊂ V ⊂ W bookkeeping is the integer-atom / n₊ data | **correct** |
| The a²+1 ≥ 2a range is V∖U, the a²+4 ≥ 4a range is U, α_j ≤ 0 on W∖V (`ASSESSMENT.md` §2) | **correct** |
| Double (2, 4) and pair (2, 2 + 2K(2iε)²), K(2iε) = ∫η²cosh(4πεu)du ≥ 1 → 1 | **correct**, re-derived independently |
| For ε > 0 the pair is charged more, the wrong direction for separation | **correct** |
| No invariant outside {tr, ‖·‖²_F, n₊, integer atoms} is consumed; the Bessel slack is the Frobenius-minus-diagonal gap already inside ‖·‖²_F | **correct**, and strengthened in §2.3: that slack is exactly zero at both configurations |
| K(2iε)² = 1.00122, 1.1286, 11.93 at ε = 0.01, 0.1, 0.5 | **correct** to every digit quoted (1.0012244…, 1.1286325…, 11.931598…) |
| ZetaZeros's zeta theorems assume Riemann–von Mangoldt and BGSTB24 Lemma 5 as hypotheses | **correct**, and confirmed against the paper's own Appendix A |
| C₀ = 0.6725007…, C₁ = (C₀+1)/2 = 0.8362503… | **correct** (0.672500703679…, 0.836250351840…) |

### 3.2 What is wrong and must be replaced: the explicit pair (c₀, r)

Session 15 wrote, in `BARRIER-ZOO.md` II.1, in `directions/A4-lindelof-lock.md`, in `STATUS.md`
line 71 and in `ASSESSMENT.md` §3: **"c₀ = 2, r = −(η²∗η²)"**. Under the program's own PairCeiling
normalization this is wrong twice over, and the pair as written is not a certificate of the claimed
value: `2 + ∫₀¹ −Q₀(x)·x dx = 2 − 0.16068… = 1.8393…`, not 0.6725. The two errors:

1. **The α = 0 atom is missing from c₀.** The form factor's coherent atom carries mass 1 at every
   configuration and pairs against Q(0), not against r(0). It must be absorbed: `c₀ = 2 − Q(0)`.
   At the Montgomery–Taylor window `Q₀(0) = ∫f₀² = 1.006127190866…`, so `c₀ = 0.993872809134…`.
2. **The factor 2 is missing from r.** The ceiling's value functional pairs r against the one-sided
   density x dx on [0,1], while the physical pairing runs over [−1,1]. Folding an even Q costs a
   factor 2: `r = −2Q` on [0,1].

The correction is not cosmetic bookkeeping: it is what makes the object a member of the class at
all, and it is pinned independently by the parent paper's own instance (flat window, λ = 1, gives
`c₀ = 1`, `r(x) = −2(1−x)`, value exactly 2/3, matching full-map's recorded gap 0.01516202 to the
ceiling). The classification conclusion is unaffected: with the corrected pair the value is
0.672500703679, the ceiling for that r is 0.681837145932, and II.1 binds.

### 3.3 What is overstated and needs one added clause

**The gap is a bound, not a prize.** "the route lands at 2 − C_MT = 0.6725 rather than 0.6818" reads
as though 0.6818 were available to the wider class. It is not known to be: 0.6818287 is an upper
bound on what any valid bandwidth-one configurationwise certificate can certify, and no certificate
attaining it is known. The honest statement is that the class optimum lies in
[0.672500703679, 0.681837145932] and that nothing here shows any valid certificate beats
0.672500703679. (Zoo II.1's own KILLS paragraph already carries the neighboring honest number, the
RH-conditional 0.6792 of Chirre, Gonçalves and de Laat, which uses a constraint the 256-law
violates and so lives outside this class.)

**Bandwidth one is imposed downstream of Proposition 2.1, not by it.** Proposition 2.1 is stated for
any λ > 0 and is bandwidth-free. The restriction supp(η² ∗ η²) ⊆ [−1,1], that is λ ≤ 1/2, enters
only when Lemma 3.1 (BGSTB24's Lemma 5, whose kernel class is even, L¹, supported in [−1,1],
Lipschitz at 0) is applied in §3. That is exactly the address zoo II.5 records, and it is worth
recording because it says where a Lamzouri-style route would have to pay to go further.

### 3.4 What is inaccurate in the II.4 dated note

The zoo II.4 note compresses the proof's per-direction step to "a² + 1 ≥ 2a per basis direction
standing in for the rank–trace inequality". The proof uses **three** different per-direction
inequalities on the three nested ranges, and at the two configurations in question the a² + 1 ≥ 2a
range is **empty**, so that sentence names the one inequality that does no work there. (The
`ASSESSMENT.md` §2 text gets this right; only the zoo note is wrong. `ASSESSMENT.md` §2's
"where information is discarded" list is merely incomplete: it names the Bessel off-diagonals and
the a² + 1 ≥ 2a slack, but the slacks that actually carry the double-versus-pair comparison are the
first-range (a − 2)² and the third-range α_j² + 2|α_j|.)

### 3.5 Exact replacement wording (final prose, to go verbatim into dated blocks)

**(a) `BARRIER-ZOO.md` II.1 — replace the clause "a Theorem-B-type certificate valid
configuration-by-configuration, c₀ = 2, r = −(η²∗η²) supported in [−1,1] (bandwidth one). This
ceiling therefore binds it." with:**

> a Theorem-B-type certificate valid configuration-by-configuration. In the PairCeiling
> normalization the pair is c₀ = 2 − Q(0) and r = −2Q restricted to [0,1], where Q = η² ∗ η²: the
> form factor's coherent α = 0 atom has mass 1 at every configuration and pairs against Q(0), so it
> is absorbed into c₀, and the factor 2 is the folding of the two-sided pairing on [−1,1] onto the
> ceiling's one-sided density x dx. The value is then c₀ + ∫₀¹ r(x)x dx = 2 − Q(0) − 2∫₀¹ xQ(x)dx
> = 2 − C_MT = 0.672500703679…, and the same reading returns exactly 2/3 for the parent paper's flat
> window at λ = 1 (c₀ = 1, r(x) = −2(1 − x)), which pins the normalization against the recorded gap
> 0.68182868746 − 2/3 = 0.01516202. Bandwidth one is supp Q ⊆ [−1,1], forced by supp η ⊂ (−1/2,1/2);
> note that Proposition 2.1 itself is bandwidth-free, and the restriction enters only at his Lemma
> 3.1, the BGSTB24 Lemma 5 input, which is the address zoo II.5 records. At the Montgomery–Taylor
> extremal η² = f₀ the certificate meets the ceiling's regularity hypothesis outright, with no
> approximation argument: r = −2(f₀ ∗ f₀) is real-analytic on [0,1], r(1) = 0 exactly (so the edge
> term vanishes identically rather than merely dropping by the sign condition r(1) ≥ 0),
> |r′(1)| = 1.369510170822…, and ∫₀¹|r″| = 1.956496214858…, so the ceiling for this certificate is
> 0.68182868746 + 2.5431316·10⁻⁶ × 3.326006385680 = 0.681837145932. This ceiling therefore binds it,
> with headroom 0.009336442253.

**(b) `BARRIER-ZOO.md` II.1 — replace the sentence "His admissible r are minus autoconvolutions of
nonnegative normalized functions of support ≤ 1/2, a subclass, which is why the route lands at
2 − C_MT = 0.6725 (his Remark 3.4: optimal for the method, by CCLM 2017 Cor. 14) and not at 0.6818
— the subclass-versus-class gap the closed A2 direction studied." with:**

> His method does not deliver a free pair (c₀, r): it delivers the one-function family
> { (2 − (f∗f)(0), −2(f∗f)|₍₀,₁₎) : f ≥ 0, ∫f = 1, supp f ⊂ (−1/2, 1/2) }, in which c₀ is determined
> by r and r is minus twice an autoconvolution of a probability density of support at most 1/2, so
> r ≤ 0, r(1) = 0, and −r/2 is of positive-definite type. Optimizing inside that family is the
> one-delta Montgomery–Taylor extremal problem, which is why the route lands at 2 − C_MT = 0.6725007
> (his Remark 3.4: optimal for the method, by Carneiro, Chandee, Littmann and Milinovich 2017,
> Corollary 14) and not higher. The distance to the ceiling is a subclass-versus-class gap, the one
> the closed A2 direction studied, but it is a bound on the available headroom and not a promised
> prize: 0.6818287 is an upper bound on what the full class can certify, no certificate attaining it
> is known, and the class optimum lies somewhere in [0.672500703679, 0.681837145932].

**(c) `BARRIER-ZOO.md` II.4 — replace "with Bessel ‖F‖² ≥ Σ_j α_j² and a² + 1 ≥ 2a per basis
direction standing in for the rank–trace inequality" with:**

> with Bessel ‖F‖² ≥ Σ_j α_j² and three per-direction scalar inequalities standing in for the
> rank–trace inequality (a² + 4 ≥ 4a on 1 ≤ j ≤ D_U, a² + 1 ≥ 2a on D_U < j ≤ D_V, and α_j² ≥ 2α_j
> from α_j ≤ 0 on D_V < j ≤ D_W)

**(d) `BARRIER-ZOO.md` II.4 — replace "the Bessel slack is the Frobenius-minus-diagonal gap already
inside ‖·‖²_F." with:**

> the Bessel slack is the Frobenius-minus-diagonal gap already inside ‖·‖²_F, and at these two
> configurations it is exactly zero, since F is diagonal in the constructed basis in both cases. At
> both configurations the middle range D_U < j ≤ D_V is empty, so the only live slacks are the
> first-range (α_j − 2)², which is 0 for the double and (1 − K(2iε))² for the pair, and the
> third-range α_j² + 2|α_j|, which is 0 for the double and (K − 1)² + 2(K − 1) for the pair. Every
> discarded quantity vanishes at the double and tends to 0 at the pair, so no reading of any slack
> separates them either.

**(e) `BARRIER-ZOO.md` II.4 — replace the numerics sentence "Numeric (Montgomery–Taylor f₀):
K(2iε)² = 1.00122 (ε = 0.01), 1.1286 (0.1), 11.93 (0.5)." with:**

> Numeric (Montgomery–Taylor f₀, recomputed at 40 digits): K(2iε)² = 1.0012244283 (ε = 0.01),
> 1.1286324662 (0.1), 11.9315981178 (0.5); at ε = 0.001 it is already 1.0000122383, and the
> right-hand side of (2.4) is −2.45·10⁻⁵.

**(f) `directions/A4-lindelof-lock.md` dated note — replace "and is bound by the II.1 ceiling as a
Theorem-B-type certificate with r = −(η²∗η²)" with:**

> and is bound by the II.1 ceiling as a Theorem-B-type certificate with (c₀, r) =
> (2 − Q(0), −2Q restricted to [0,1]), Q = η² ∗ η², of value 2 − C_MT = 0.672500703679 against a
> ceiling of 0.681837145932 for that r

**(g) `STATUS.md` line 71 — replace "and is bound by the II.1 ceiling as a Theorem-B-type
certificate with r = −(η²∗η²)" with:**

> and is bound by the II.1 ceiling as a Theorem-B-type certificate with (c₀, r) =
> (2 − Q(0), −2Q restricted to [0,1]), Q = η² ∗ η², value 0.672500703679 against ceiling
> 0.681837145932

**(h) `results/arxiv/README.md` dated note — replace "On a single-check reading it lies inside the
certificate class of the cubic-augmentation paper; nothing in either frozen paper becomes wrong."
with:**

> Dual-model checked on 2026-09-05: it lies inside the two-moment, bandwidth-one certificate class
> whose ceiling the cubic-augmentation paper's no-go is about, as the certificate
> (c₀, r) = (2 − Q(0), −2Q restricted to [0,1]) with Q = η² ∗ η², of value 0.672500703679; nothing
> in either frozen paper becomes wrong.

**(i) `ASSESSMENT.md` §3, first bullet — replace "with c₀ = 2 and r = −(η² ∗ η²) supported in
[−1, 1]" with:**

> with c₀ = 2 − Q(0) and r = −2Q restricted to [0,1], Q = η² ∗ η² supported in [−1,1]

**(j) Relabeling.** Each of the four dated single-check notes should carry, appended, the block:

> **[DUAL-MODEL CHECK, 2026-09-05, Session 16 — Opus 5.]** Independently re-derived from the paper
> text and full-map.md's PairCeiling definition, with all numbers recomputed at 40 digits
> (`results/watch-lamzouri-2609.02882/dual-check-O.md`, script `dual-check-O-K2ieps.py`). Verdict:
> the classification is CONFIRMED; the explicit pair (c₀, r) recorded on 2026-09-03 was corrected
> from (2, −(η²∗η²)) to (2 − Q(0), −2Q restricted to [0,1]); the II.4 per-direction inequality was
> corrected from one to three; all three quoted values of K(2iε)² were confirmed. The line is no
> longer single-check and may be used externally.

---

## 4. Item C, second half — the A4 near-CUE / riders cross-check

Claim under check (`ASSESSMENT.md` §3, A4 bullet; repeated in `directions/A4-lindelof-lock.md`):
"A4's near-CUE section consumes BGSTB24 in its depth-weighted form under its riders 1–3 (main.tex,
'The licensing theorem, and its three riders', ≈ lines 1799–1854), so Lamzouri's weight-removal
device is not needed there."

**CONFIRMED, with one precision.** `results/arxiv/a4-no-go/main.tex` §"The licensing theorem, and
its three riders" begins at line 1799; the three riders are enumerated from line 1826; the closing
sentence "inherits riders 1--3" is at line 1854. The section licenses the pinning rows
`|E_w|c_j|² − j| ≤ τ₂` from **Theorem 1** of BGSTB24, quoted there as
`F(α) = T^{−2α}(log T + O(1)) + α + O(1/√log T)`, "unconditional and pointwise in α, uniform on the
closed band 0 ≤ α ≤ 1", "for the form factor defined with zeros counted with multiplicity and
off-line zeros entering with the depth weight x^{δ+δ′} — exactly the cosh depth-weighting the
model's form factor c_j applies", and each open-band row is licensed "pointwise per row". Riders
1–3 are depth-aggregation only, finite-T slack O(N/√log T), and second-moment scope.

The precision: A4 cites their **Theorem 1 first**, and mentions their Lemma 5 admissible kernel
class only as an alternative route ("directly, or through their Lemma 5 admissible kernel class").
This matters for the claim, and strengthens it. Lamzouri's Lemma 3.2 is a device for converting a
*kernel sum* `Σ f̂(i(ρ−ρ′)L/2π) w(ρ−ρ′)` supplied by Lemma 5 into the *unweighted* sum
`Σ K(i(ρ−ρ′)L/2π)²`, by writing `r_{δ,T} = Q_δ − Q_δ″/(4 log²T)` and applying Lemma 5 twice. A4
never forms such a kernel sum: it pins values of F(α) row by row at α = j/N. So no weight-removal
step arises there, and the device is genuinely not needed. The claim stands as written, and the
citation could be tightened from "BGSTB24" to "BGSTB24 Theorem 1 (pointwise), with their Lemma 5
named only as an alternative route".

One boundary the note does not state, and should not be read as covering: Montgomery's F(α) carries
the weight 4/(4 + (γ−γ′)²) inside its own definition, so pinning F(α) pointwise pins a weighted
statistic; whether A4's model form factor c_j reproduces that weight is A4's internal matter,
settled (or not) elsewhere in that paper, and was not re-derived here.

---

## 5. Honesty section: what was NOT re-derived

1. **The ceiling constants themselves.** 0.68182868746, 0.82395317, 2.5431316·10⁻⁶ and the
   256-periodic law behind them are taken from `results/full-map.md` as given. I did not re-solve
   the LP, re-run the interval arithmetic, or check `EnclOK`. My arithmetic uses them as inputs.
2. **The PairCeiling Lean sources.** `Zeta23/PairCeiling/Defs.lean`, `Ceiling.lean`,
   `Stability.lean`, `NearCUE.lean`, `LawN256.lean` are **not present** in this repository's
   `lean/Zeta23/PairCeiling/` (which holds only GridParseval, GridWitness, GridCorner); the parent
   Zeta23 library is not redistributed here. So the definition of "valid at a configuration" and the
   value functional were read from full-map.md's quotations, and the placement of the α = 0 atom in
   c₀ was **inferred**, then pinned by two independent consistency checks: the integration-by-parts
   boundary term requires D(0) = 0, so j = 0 cannot be in the grid sum; and the flat-window λ = 1
   instance must return exactly 2/3, which it does only under this placement. If the Lean definition
   ever becomes available and places the atom elsewhere, the arithmetic in §1.3 must be redone (the
   conclusion, value ≤ ceiling, would be unaffected, since any consistent placement returns the same
   value 2 − C_MT).
3. **The 256-law's own numbers.** In particular I could not reconcile the recorded
   `|D(1)| ≤ 0.82395317` with `S(j) = j/256`, which gives a cumulant discrepancy of order 10⁻³ (or
   ≈ 1 if the aliased edge row j = N is included). Nothing here depends on it, because r(1) = 0
   exactly for Lamzouri's certificate kills the edge term outright. Flagged as a separate item worth
   a look, not a defect found.
4. **The BGSTB24 papers.** Lemma 5 and Theorem 1 were read only as quoted, in Lamzouri's Lemma 3.1
   and in A4's main.tex. I did not open the Acta Arithmetica paper or arXiv:2306.04799.
5. **CCLM 2017, Corollary 14.** Not opened. Lamzouri's Remark 3.4 is quoted verbatim and the
   optimality claim is attributed to him, not verified.
6. **The Lean build record and the ZetaZeros repository.** Commit `4bcaf70`, the toolchain versions,
   the axiom lists and the "build clean" claim were not re-run; I read only
   `lean-build-record.md`'s summary. The paper's Appendix A does independently confirm the *shape*
   of the claim (Proposition 2.1 unconditional; Theorem 1.1 under the assumptions of BGSTB24's
   Lemma 5 and the Riemann–von Mangoldt asymptotic).
7. **Lamzouri's §3 error terms.** I checked the structure of Lemma 3.2 (the identity
   `r̂_{δ,T}(z) = (1 + π²z²/log²T)K_δ(z)²`, the two applications of Lemma 3.1, the limit
   `C_δ → C_MT`) but did not audit the O_δ(1/√log T) uniformity or the claim
   `f_δ → f₀ in L¹ ∩ L²`. The paper was not refereed here.
8. **Program history claims.** "the subclass-versus-class gap the closed A2 direction studied and A4
   absorbed", and the A2/A4 record generally, were not checked.
9. **The distinct-zeros branch.** (2.5) and the C₁ = 0.8362503 constant were derived structurally
   (c₀ = 3/2 − Q(0)/2, r = −Q, value (3 − C_MT)/2) but the numeric was not independently minimized
   or ceiling-checked, since II.1's ceiling is stated for the simple-zero proportion.
