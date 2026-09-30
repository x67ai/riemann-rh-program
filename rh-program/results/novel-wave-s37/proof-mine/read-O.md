# read-O — Opus reader on M2 `proof-mine` (dual-model check, standing orders 5, 7, 11)

Reader: Opus 5.5 (independent of the orchestrator's read; not waited for). Date: 2026-10-01.
Object read: `NOTE.md` (40 535 bytes, 322 lines, CLOSE T, writer Opus 5.5, 2026-09-30), charter §"Seed M2", `SHARED.md` blocks 0–8.
My scripts and logs: `verify-O/` (independent route: no import from `verify/`).

**VERDICT LINE:** (pending — filled when §1–§5 have landed)

Section status: §1 pending · §2 pending · §3 pending · §4 pending · §5 pending · §6 pending · §7 pending

## §1 The 14 rows at the page

Method: each cited passage opened in `sources/` (text layer; page images rendered with `pdftoppm` into `verify-O/*.png` for
Bombieri pp. 234–240 and Deligne pp. 283–285, 298, 301, where the text layer drops the formulas). Page numbers are the printed ones.

| row | source file : line (printed page) | the step named as the line | status |
|---|---|---|---|
| R1 Hasse (D) | `sutherland-18783-hasse-lecture8.txt` : 33–75 (pp. 1–2) | "noting that deg(r − π_E s) ≥ 0 … the discriminant t² − 4q cannot be positive" (l. 68–73) | VERIFIED |
| R2 Weil–Rosati (D) | `milne-…txt` : 1205–1221 (p. 21, Thm 1.27), 1241–1271 (p. 22, Cor 1.29, Thm 1.30), 1282 (p. 23), 294–327 (p. 5) | Thm 1.27, Tr(αα†) = (2g/(D^g))(D^{g−1}·α⁻¹D) > 0 "by dimension theory" | VERIFIED |
| R3 Weil 1941/48a (A) | `milne-…txt` : 358–375 (p. 6), 610–701 (pp. 11–12; σ(D∘D′) = def(D) l. 637–644; Φ l. 669–697; Thm 10 p. 54 l. 700) | effective representative + Φ = det(φ_i(D_j(P))), σ(D∘D′) ≥ 2g d₁(D) | VERIFIED (sketch assumes d₂(D) = g ≥ 2, l. 654; g = 1 is CCM (2.40)) |
| R4 Mattuck–Tate–Grothendieck (A) | `milne-…txt` : 462–600 (pp. 8–10), 744–750 (p. 13) | Thm 1.2 / Cor 1.3 (index 1); Thm 1.5, Cor 1.6, Ex. 1.7, "abs((Δ·Γ_π) − q − 1) ≤ 2gq^{1/2}" (l. 597) | VERIFIED |
| R5 Stepanov / Schmidt (C) | `bombieri-…txt` : 76–81, image p. 234 | quoted sentence only; proofs not read | UNVERIFIED (as the NOTE says; no verdict carried) |
| R6 Bombieri 1973 (C) | images pp. 236 (Thm 1, (5), (i)–(v)), 238–239 ((7), parameters), 239 (§III, ω₁ = q, ω₂ = 1), 240 ((8)–(10)) | §III: separable t, Galois C′ → P¹, twisted counts ν₁(C′, η), (8) + (9) ⇒ (10) | VERIFIED |
| R7 Deligne Weil I (B) | `deligne-…txt` + images: Thm (3.2) p. 284 (not 283), Lemmes 3.3–3.6 p. 284, (3.7) and the Rankin step "abs(α) ≤ q_x^{β/2 + 1/2k}" p. 285, Lemme (7.1) p. 298, (7.2) p. 300, (7.3) p. 301 | (7.1) at X = C × C via (7.3); family form (3.2) | VERIFIED |
| R8 Laumon / Weil II (B) | `laumon-…txt` : 142 (p. 133), 3227 (Thm 4.1.3, p. 204), 3260 (4.2.1.3, p. 205), 3305–3325 (Cor 4.3.1.1, Prop 4.3.2.1, p. 206) | (4.3.2.1) "une fonction méromorphe non constante f : X → D", then Fourier + purity | VERIFIED |
| R9 Kedlaya (B) | `kedlaya-…txt` : 17–21 (abstract), 82 (p. 2, Dwork = rationality), 204–207 (p. 5), 280–281 (p. 7) | R8 transcribed; Rankin squaring on a curve | VERIFIED |
| R10 Davenport–Hasse / Weil 1949 (C) | `milne-…txt` : 1305–1340 (p. 23) | Gauss-sum expression of the counts (at the page); the positivity step abs(g(χ))² = q ⇒ RH is NOT on p. 23 | PARTIAL: route VERIFIED, positivity step recalled (NOTE labels it) |
| R11 automorphic (—) | `milne-…pdf` PDF pp. 49, 51, 58 (checked by `pdftotext`) | not a proof of RH: consumers of RH | VERIFIED as a negative row; it is NOT one of the "12 proofs" (see F3) |
| R12 CCM (A) | `ccm-…txt` : 430–508 (pp. 9–11; (2.35) l. 433, effectivity l. 434, (2.40) l. 473), 530–556 (p. 12 dictionary), 1287–1291 (p. 29, Prop 6.2) | R3's positivity via Riemann–Roch on C | VERIFIED |
| R13 Hrushovski (A) | `hrushovski-…txt` : 156 (printed p. 4), 508–509 (printed p. 11), 6457–6464 (printed p. 115) | Ex. 11.4, Weil's positivity β | VERIFIED in content; pages cited as 3, 10, 114 are each ONE LOW (F1) |
| R14 named-not-read | — | Manin, Igusa, Quigley, Roquette, Kani, Weil II 1980, Stark, Stöhr–Voloch | UNVERIFIED (as labeled) |

**Tally.** Positivity step at the page: R1–R4, R6–R9, R12, R13 (10 rows). Route at the page, positivity step recalled: R10.
Negative row: R11. Not read: R5, R14. Three of the ten are not independent proofs: R9 = R8 transcribed (Kedlaya's abstract),
R12 = R3 restated (CCM p. 9), R13 = R3 for curves (Hrushovski p. 11). Independent proofs verified at the page: **7** (R1, R2, R3, R4, R6, R7, R8).

## §2 The four V-violations, re-derived by hand (numbers checked in §3)

Data: V has t = 5, q = 5, α, β = (5 ± √5)/2, a_n = α^n + β^n with a_n = 5a_{n−1} − 5a_{n−2}: a_1..6 = 5, 15, 50, 175, 625, 2250.

**(A) Surface.** Milne's conventions (pp. 9–10): C₁ = C × pt, C₂ = pt × C, C₁² = C₂² = 0, C₁·C₂ = 1, d₁ = D·C₁, d₂ = D·C₂; for a graph
Γ_f, d₁ = deg f, d₂ = 1 (Ex. 1.7), Γ_f² = (2 − 2g)deg f = 0 at g = 1, Δ² = 0, Δ·Γ_π = N₁. For g = 1, Γ_φ·Γ_ψ = deg(φ − ψ). Gram matrix on
(C₁, C₂, Δ, Γ_π) = [[0,1,1,q],[1,0,1,1],[1,1,0,N₁],[q,1,N₁,0]]; with q = 5: V (N₁ = 1) has inertia **(2, 2)**, E₀ (N₁ = 2) has **(1, 3)**; the
same on (C₁, C₂, Γ_{π⁰..π³}) (rank 4). def(mΔ + nΓ_π) = 2(m + nq)(m + n) − 2mnN₁ = 2(m² + tmn + qn²); at (m, n) = (−2, 1):
**V: 2(4 − 10 + 5) = −2**, E₀: 2(4 − 8 + 5) = 2. Cor 1.6 at (Δ, Γ_π): |N₁ − q − 1| = 5 > 2√5 = 4.472. **CONFIRMED.**

**(B) Family.** Künneth: H²(C × C) carries α², αβ = 5, β², q, q. Lemma (7.1) (p. 298) at d = 2: q^{1/2} ≤ |·| ≤ q^{3/2}.
α² = (15 + 5√5)/2 = 13.090 > 5√5 = 11.180 (exact: ⟺ 3 > √5); β² = (15 − 5√5)/2 = 1.910 < √5 (exact: ⟺ 225 < 245). Both sides fail.
Family form: Deligne p. 285 prints, for a rational point, |1/q^{kβ+1}| ≤ |1/α^{2k}|, i.e. |α|^{2k} ≤ q^{kβ+1}; weight β = 1, q = 5:
2k = 2: 13.090 ≤ 25 holds; 2k = 4: α⁴ = (350 + 150√5)/4 = 171.353 > 125 **fails**. E₀: 5^k ≤ 5^{k+1}. **CONFIRMED.**

**(C) Coordinates.** Bombieri Theorem 1 (p. 236, image): "Assume q = p^α, where α is even. Then if q > (g + 1)⁴ we have (5) ν₁ < q + (2g + 1)q^{1/2} + 1."
It is an **upper** bound only; V's counts sit **below** q^r + 1 (a_r > 0 for all r), so V passes (5) and (7) at every admissible r — the
side V violates is the lower side, which Bombieri says the argument "does not give" (p. 239). (7) (p. 239): ν₁ ≤ ℓ + mq/p^μ + 1 under ℓp^μ < q,
ℓ, m ≥ g, (ℓ + 1 − g)(m + 1 − g) > ℓp^μ + m + 1 − g, with μ = α/2, m = p^μ + 2g, ℓ = [g p^μ/(g + 1)] + g + 1. At Q = 25, g = 1: (μ, m, ℓ) =
(1, 7, 4), hypotheses 20 < 25 and 28 > 27 hold, (7) = 4 + 35 + 1 = **40**; (5) = 25 + 15 + 1 = **41** (strict). For g = 1 with C′ = C → P¹ = x-map,
G = {1, ι}, ν₁(C, ι) = #ker(π_Q + 1) = Q + 1 + a_r (all fixed points; Σ_η ν₁ = 2(Q + 1) exactly for an elliptic curve). V at Q = 25:
26 + 15 = **41**: fails "< 41" and "≤ 40". Q = 5⁴: 801 > 701 ((8) as printed) and > 690 ((7)); Q = 5⁶: 17876 > 16001 and > 15940.
Lower bound 2(Q + 1) − (7): 12, 562, 15312 against N = 11, 451, 13376. **CONFIRMED** (every number in NOTE R6).
Nuance (MINOR m5): at Q = 25 the twist meets (8) as printed with equality (41 ≤ 41); the violation at 5² is of (5)'s strict form and of (7).

**(D) Group.** deg(rπ − s) = r²q − rst + s² (Sutherland l. 61–65); deg(π − 2) = 5 − 10 + 4 = **−1** = (α − 2)(β − 2); α − 2 = (1 + √5)/2 = φ,
a unit of norm −1. (The brief's "q − a + 1" is deg(π − 1) = N₁ = 1, not deg(π − 2).) Rosati: for g = 1 with the principal polarization,
π† = q/π, so (π − 2)(π − 2)† = (α − 2)(β − 2) = −1 as a scalar, trace on the 2-dimensional V_ℓ = **−2**; matrix check with the companion
M = [[0, −5], [1, 5]] and π† = adj(M): Tr((M − 2)(adj M − 2)) = −2. E₀: +1 and +2. **CONFIRMED.**

## §3 Independent re-run (`verify-O/`, no import from `verify/`)

| script → log | route | result |
|---|---|---|
| `o_lines.py` → `o_lines.log` | V, E₀ counts by the a_n recurrence + own Möbius; Gram matrices from Γ_φ·Γ_ψ = deg(φ − ψ) with deg as the norm form of Z[π]; inertia by an exact Faddeev–LeVerrier characteristic polynomial over Fractions + Descartes (exact for real-rooted); Rosati by companion matrix and adjugate | V: N_1..8 = 1, 11, 76, 451, 2501, 13376, 70001, 361251; b_1..8 = 1, 5, 25, 110, 500, 2215, 10000, 45100; min N = min b = 1 (≤ 60). Inertia V (2, 2), E₀ (1, 3), both bases. def = −2 / 2. deg(π − 2) = −1 / 1. Rosati trace −2 / 2. CS on span(Δ, Γ_{πⁿ}) violated for every n = 1..12 (V), none (E₀). Rankin 2k = 2 holds, 2k = 4 fails (171.353 > 125). |
| `o_fields.py` → `o_fields.log` | own F_{5ⁿ} arithmetic (first irreducible modulus found by search), brute-force counts of E₀: y² = x³ + 2x and of its quadratic twist d·y² = x³ + 2x (d a non-square) | F₅: 2 + 10 = 12; F₂₅: 20 + 32 = 52; F₆₂₅: 640 + 612 = 1252 = 2(Q + 1) each. Bombieri (5)/(7) with the printed parameters: V's twist 41 / 801 / 17876 fails at Q = 5², 5⁴, 5⁶; V's N fails the lower bound (12, 562, 15312); E₀ passes all six tests. |
| `o_twin.py` → `o_twin.log` | V₂ by Newton's identities (exact), roots by numpy; genus-2 box search re-implemented | V₂: h = 31; N_1..6 = 5, 47, 143, 507, 2950, 16319; b_1..6 = 5, 21, 46, 115, 589, 2689; min N = min b = 5 (≤ 40), all b_d integral; abs(α) = 2.7138, 1.8425; Re s = 0.6203, 0.3797; x² − x + 1 (disc −3): non-real x_i. Theorem 1 at g = 2 needs Q > 81: Q = 5⁴ passes (N − Q − 1 = −119), **Q = 5⁶: 693 > 625 fails (5)**, and (7) (16319 > 16212). Box: **111** hits (agrees); 105 of 111 are caught by (5) at some Q ∈ {5⁴, 5⁶, 5⁸}, 6 are not. |
| `o_z4.py` → `o_z4.log` | Lemma Z4 object F_x = Π(⌊x/k⌋!)^{c_k}; identity log F_x = Σ Λ(n) g(x/n) at x = 2000; κ = AT/(T − 1); LP (HiGHS) minimizing κ over real c supported on div(M), g ≥ 0 on a period, g ≥ 1 on [1, T), T ≤ 40 | Chebyshev c = (1, −1, −1, −1, +1) on (1, 2, 3, 5, 30): A = 0.921292, T = 6, **κ = 1.105550**; C(2n, n): **κ = 1.386294**; identity 1839.3991 = 1839.3991. LP optimum: div(6) 1.170533, **div(30) 1.105550 (= Chebyshev: his weights are optimal on div 30)**, div(210) 1.073965, div(2310) 1.069854 — all > 1, decreasing. |

**Reading of §3.** Every number in the NOTE's §1 table, R1–R13 NUMBER lines, the V₂ paragraph and Lemma Z4's two constants is reproduced
by a route sharing no code with `verify/`. No numerical FIX-FIRST. The LP adds one fact the NOTE lacks: finite supports push κ down
toward 1 (1.1056 → 1.0740 → 1.0699 as M runs 30 → 210 → 2310), so Z4's "κ > 1 strictly" is a per-support statement, not a gap bounded
away from 1 — see §4 and F4.

## §4 The record check for class C, and Pritsker at the page

**4.1 Grep** (`BARRIER-ZOO.md`, `results/novel-wave-s36/tournament/NOTE.md`, `directions/*.md`; terms Gelfond, Schnirelman, Chebyshev, Nair,
Chudnovsky, Pritsker, integer polynomial, auxiliary polynomial, lcm; case-insensitive). 29 hits in 10 files, **none on the object**:
"Gelfond" is always Gelfond–Schneider (zoo l. 497, 500; C3 l. 181, 213, 223, 281: End(E_p) = Z); "Chebyshev" is always a Chebyshev-strength
INPUT (directions A1, A2, A3, A4, B2, B4, C2; zoo l. 564 a "Chebyshev bound" in a pricing line); "auxiliary polynomial(s)" occurs only in
tournament l. 67, 75, 158 (T24). No hit for Schnirelman, Nair, Chudnovsky, Pritsker, integer polynomial, lcm.
**T24 does not cover the object.** Its A-line is "bound ψ(x) from above by an auxiliary function vanishing at primes"; its kills are (i) no
Frobenius self-map, (ii) "upper-bound prime counting by auxiliary weights is Selberg's sieve" → III.4, (iii) III.20(A). The Gelfond–Schnirelman
object is a LOWER bound through the exact identity ψ(n) = log lcm(1, …, n) (Pritsker p. 2 at the page); III.4 kills routes "whose arithmetic
input is entirely sieve-type (linear forms in Λ with sieve-weight positivity)" and its executable test (does the input distinguish Λ from a
parity-flipped counterfeit?) is passed: lcm(1..n) = e^{ψ(n)} and log⌊y⌋! = Σ Λ(n)⌊y/n⌋ pin Λ = μ ∗ log exactly. (i) and (iii) are about the
Frobenius and the tower, which the integer-polynomial object does not use. **Ruling: the record neither kills nor bounds class C's
integer-polynomial object; the NOTE's "not dead on the record" is CORRECT.** The stop condition "record already kills class C" does not fire.
Two record entries touch its RH-strength form without killing it: T22 (Landau positivity on (ψ − x)^{2k}, EQUIV) and the classical
one-sided oscillation theorem the NOTE re-proves as Z1(c) (Landau; Ingham ch. V `[recalled, unverified]`) — both say only that a sharp
one-sided bound is RH-equivalent, which the NOTE states.

**4.2 Pritsker arXiv:1307.5361v1 at the page** (`sources/pritsker-…txt`, form-feed pages = printed pages):
- p. 1, (1.2): Chebyshev 1852, 0.921 x/log x ≤ π(x) ≤ 1.106 x/log x. ✔ (Z4's nearest object)
- p. 2: (1.5) lcm(1..n+1)∫₀¹p_n ≥ 1; (1.7) PNT would follow from ‖p_n‖^{1/n} → 1/e; "It was found by Gorshkov [15] in 1956 that (1.7) can
  never be achieved. In fact, 0.4213 < t_Z([0, 1]) < 0.4232." ✔ (NOTE §3 quote exact)
- p. 3, (1.11): Nair and Chudnovsky, ∫₁^x ψ ≥ 0.99035 x²/2, α₁ ≈ 0.195; Theorem 1.1, (1.13): ∫ψ ≥ (−2 log c_w/(4α + 3)) x²/2 + O(x log² x). ✔
- p. 4, **Proposition 1.3: B(w) := −2 log c_w/(4α + 3) < 1 for every fixed weight (1.12)** — proved "in such an indirect way" from
  Littlewood's ∫ψ − x²/2 = Ω±(x^{3/2}) against the "too good" error term; "if the Riemann hypothesis is true, then ∫₁^x ψ − x²/2 = O(x^{3/2})
  (see Theorem 30 in [17, p. 83])"; "Although (1.13) cannot provide a proof of the PNT for a fixed weight w, this does not preclude the
  possibility that such a proof can be obtained by finding a sequence of weights w_n with B(w_n) → 1"; "we did not observe a numerical
  improvement of the estimate (1.11) when using further factors of the one-dimensional integer Chebyshev polynomials … beyond the factors x
  and 1 − x"; **Problem 1.4**: find B := sup_w B(w); "If B = 1 then find a sequence of weights that gives this value. If B < 1 then investigate
  whether B is attained". ✔ So what is printed is: fixed weight — PNT impossible (Prop 1.3); sequence of weights — OPEN (Problem 1.4).
  The NOTE's paraphrase "open in print even at PNT strength" is exact; its "fixed-weight form cannot give PNT (ibid.)" is Prop 1.3.

**4.3 Since 2013 (arXiv API, one request at a time, ≥ 3.5 s apart; `verify-O/o_arxiv.py` → `o_arxiv.log`, XML in `verify-O/sources/`).**
14 queries (Gelfond–Schnirelman in all fields and spellings; "integer Chebyshev" with prime; "integer Chebyshev constant"; Nair ∧ Chebyshev ∧
prime; "weighted capacity" ∧ prime; lcm ∧ lower bound ∧ primes; Chebyshev ∧ elementary ∧ PNT; Nair ∧ lcm; three abstracts by id). Only hits
on the object: Pritsker 1307.5361 itself and his same-month companions 1307.5456 (multivariate integer Chebyshev problem — sup norms, no
prime-counting statement in the abstract) and 1307.5362 (monic problem). Other hits are lcm-of-sequences bounds (2012.05828, 1308.6458, …)
and an expository Selberg–Erdős text (2308.07245). **Nothing on arXiv since 2013 settles or advances Problem 1.4.** Journals not searched.

**4.4 One source the NOTE lacked, at the page — Diamond, "Elementary methods in the study of the distribution of prime numbers", Bull. AMS
7 (1982) 553–589** (`verify-O/sources/diamond-1982-bams-elementary-methods.{pdf,txt}`, direct AMS download, no wall), §9 "Improved
Chebyshev-type estimates", pp. 578–579: "Given a positive number ε, is it possible to find a function v, depending on ε, such that the method
of §3 yields (9.2) limsup |ψ(x)/x − 1| < ε, or is there some natural limitation to the method? In this section we shall show that the first
alternative holds … Any direct construction of an appropriate function v for each ε > 0 would give another type of elementary proof of the
P.N.T. We are going to establish the existence of a function v by using the P.N.T. … It was first discovered by J. B. Rosser and independently
by P. Erdös and L. Kalmár in the late 1930's … A proof was reconstructed by H. Diamond and Erdös [DE] and another one was given by Diamond and
K. McCurley [DM]." The construction takes v = μ_T (μ on n < T, corrected at n = T so that Σ v(n)/n = 0).
**Consequence for the NOTE.** The Chebyshev-factorial class is the exact analog of Pritsker's weights, one step further along: FIXED finite
supports cannot reach κ = 1 (Lemma Z4; in Pritsker's class, Prop 1.3), but SEQUENCES of finite supports do reach every 1 + ε (Diamond §9,
existence proved via PNT). So "its finite-support Chebyshev half is killed by Lemma Z4" (NOTE §3 l. 291, §4 l. 318) is wrong for the sequence
form: that form is SETTLED at PNT strength (existence) and, at RH strength, is RH restated (c = μ gives lcm(1..x), as the NOTE says).
My LP (§3) is the quantitative face of Diamond §9: min κ on div(M) = 1.1056, 1.0740, 1.0699 at M = 30, 210, 2310.

**4.5 The T24 flag (task 4).** Bombieri p. 239 (image, `verify-O/bombhi-7a.png`, `-7b.png`): "III. The argument given before does not give
a lower bound for ν₁, while this is needed if we want to deduce the Riemann hypothesis (3). For example, if ν_r = q^r − ω₁^r − ω₂^r + 1 and
ω₁ = q, ω₂ = 1 then (2) is verified, ν_r is always 0 but (3) is false." Then: "we may assume that q is an even power of p, by making a base
field extension … by a well-known approximation argument, it is sufficient to prove ν₁ = q + O(q^{1/2})", and the lower bound comes from the
twists (8)–(10) (p. 240). T24's G-line "the tower over F_{q^n} upgrades the bound to RH" (tournament NOTE l. 75) attributes the upgrade to
the tower acting on the UPPER bound; the page says the upper bound for all r does not give RH (ν_r = 0 satisfies every upper bound) and the
tower upgrades only the TWO-sided q + O(q^{1/2}). **Ruling: the NOTE's flag is RIGHT**; T24's verdict (DEAD) is unaffected. The NOTE's
replacement line drops the tower, which the page keeps — see m2 for the exact wording.

## §5 FIX-FIRST (not applied to NOTE.md)

No number in the NOTE is wrong (§2–§3). The four FIX-FIRST items are two citations/counts and two statements of scope.

**F1 — Hrushovski pages (R13, NOTE l. 206–209).** Printed page = PDF page in math/0406514v2 (`pdftotext -f/-l`); each cite is one low.
OLD: "read at the page: p. 3 ("The fundamental fact is Weil's …"; Theorem 1.1, the twisted Lang–Weil estimate); p. 10 ("§11.4 for a proof
for curves: …"); Example 11.4 p. 114 (…)"
NEW: "read at the page: p. 4 ("The fundamental fact is Weil's …"; Theorem 1.1, the twisted Lang–Weil estimate); p. 11 ("§11.4 for a proof
for curves: …"); Example 11.4 p. 115 (…)"

**F2 — the count of proofs read (§0 l. 17–19; Theorem P(i) l. 258; proof l. 269; CLOSE l. 314).** R11 is not a proof of RH (the NOTE's own
R11 says the automorphic results "CONSUME RH"), and R10's positivity step is recalled (NOTE l. 180–181 labels it).
OLD (l. 17): "14 rows: 12 proofs read at the page (Hasse; … Davenport–Hasse/Weil 1949; CCM; Hrushovski; the automorphic check), 2 named-not-read."
NEW: "14 rows: 10 proofs whose positivity step is read at the page (Hasse; Weil–Rosati; Weil's correspondences; Mattuck–Tate–Grothendieck;
Bombieri–Stepanov; Deligne Weil I; Weil II via Laumon; Kedlaya = Laumon transcribed; CCM = Weil restated; Hrushovski = Weil for curves —
7 independent), 1 read up to a recalled positivity step (Davenport–Hasse/Weil 1949), 1 negative row (automorphic methods consume RH),
2 named-not-read."
OLD (l. 258): "read at the page in this note (R1–R4, R6–R13)" → NEW: "read at the page in this note (R1–R4, R6–R9, R12, R13; R10 with its
positivity step recalled; R11 is not a proof and is vacuous here)". Same change at l. 314 ("12 proofs read at the page" → "10 proofs with
the positivity step at the page, 7 independent").

**F3 — the partition is by INEQUALITY, not by input (§0 l. 19; Theorem P(i) l. 258–259; CLOSE l. 315).** By the NOTE's own lemmas R3
("The proof uses rational functions on C (a basis of L(K_C), the function Φ …)") and R8 ("The proof uses a nonconstant function C → P¹ …"),
the FIRST object V lacks in R3, R12, R13 (class A) and R8, R9 (class B) is a class-C object; Milne pp. 11–12, CCM p. 9 ("using the Riemann–Roch
formula on C to show that one can achieve effectivity") and Laumon p. 206 ("une fonction méromorphe non constante f : X → D") confirm it.
OLD (l. 19): "Each proof separates curves from V at one input:"
NEW: "Each proof derives RH through exactly one of four inequalities (the partition is by inequality; in R3, R8, R9, R12, R13 the first
object V lacks is a class-C object — a function field with Riemann–Roch sections, or a nonconstant function to P¹):"
OLD (l. 258–259): "derives RH through an inequality I_c attached to one of four inputs c ∈ {A surface, B family, C coordinates, D group}:"
NEW: "derives RH through exactly one inequality I_c, c ∈ {A surface, B family, C coordinates, D group} (a partition by inequality; the
classes are not disjoint in the objects used — five of the ten rows need a class-C object upstream of their inequality):"
Effect: none on (ii) or (iii); the Z-side verdicts for A and B stand (their inequalities, not the upstream functions, are what the record kills).

**F4 — Lemma Z4: nearest objects and scope (§4 l. 286–287; l. 290–291; §0 l. 24; CLOSE l. 318).** See §4.2 and §4.4.
OLD (l. 286–287): "`[novelty: single-check]`; nearest published object (10(n)): Chebyshev 1852 via Pritsker (1.2) at the page; Diamond–Erdős
1980 on sharp elementary estimates `[recalled, unverified]` (not load-bearing)."
NEW: "Nearest published objects (10(n)), at the page: Pritsker 2013 Prop 1.3 (p. 4), the same statement for Gelfond–Schnirelman weights,
proved from Littlewood's Ω± theorem — which also gives Z4 at once (κ = 1 would give ψ(x) ≤ x + O(log²x)); Diamond, Bull. AMS 7 (1982) §9
pp. 578–579: for every ε > 0 a finite-support weight with limsup|ψ(x)/x − 1| < ε exists (Rosser; Erdős–Kalmár; Diamond–Erdős 1980;
Diamond–McCurley), proved using the PNT. Z4's own content is the direct proof (κ = 1 ⟺ c = μ ∗ (δ₁ − δ_T)): routine;
`[novelty: single-check]` for that proof only."
OLD (l. 290–291): "its finite-support Chebyshev half is killed by Lemma Z4;"
NEW: "each FIXED finite-support Chebyshev weight is killed by Lemma Z4, but SEQUENCES of them reach every κ = 1 + ε (Diamond 1982 §9,
existence via the PNT), so the Chebyshev sequence form is settled at PNT strength and RH-restated at RH strength (the c = μ limit);"
OLD (l. 24 and l. 318): "its Frobenius and finite-support Chebyshev forms are killed here (Z2; Lemma Z4 …)"
NEW: "its Frobenius form is killed here (Z2), and so is each fixed finite-support Chebyshev weight (Lemma Z4: κ > 1), while sequences of such
weights reach PNT strength (Diamond 1982 §9, via the PNT)"
Effect on the close: the G-content survives — class C's integer-polynomial object is still the one input with an open question in print
(Pritsker Problem 1.4) — but it is now one of two parallel sequence forms, and its Chebyshev twin shows what "B = 1" would and would not buy:
PNT-strength existence, proved through the PNT, with no rate.

## §6 Minor (prose; not applied)

- **m1 (R7, l. 138).** OLD "§3 pp. 283–287 (Thm 3.2, Lemmes 3.3–3.6, (3.7), Cor 3.8–3.9)" → NEW "§3 pp. 283–287 (Thm 3.2 and Lemmes 3.3–3.6
  p. 284; (3.7) and the Rankin step p. 285; Cor 3.8–3.9 p. 286)". The inequality the NOTE calls "Thm 3.2's inequality" (l. 149) is the
  p. 285 step abs(α)^{2k} ≤ q_x^{kβ+1}; Thm 3.2's conclusion is purity ("𝓕 est de poids β", p. 284). Say "the p. 285 Rankin step".
- **m2 (T24 replacement, l. 134–135).** OLD "its G-line should read "upper bounds for all twists of a Galois cover ⇒ lower bound ⇒ RH"" →
  NEW "its G-line should read "an auxiliary function vanishing to order p^μ at the fixed points of each twisted Frobenius η∘φ of a Galois
  cover C′ → P¹ bounds every ν₁(C′, η) ≤ q + O(g′√q) (Bombieri (8)); summing over η (9) gives ν₁(C) = q + O(√q), and base extension plus
  the approximation argument (p. 239) give RH — the upper bound alone does not (p. 239: ω₁ = q, ω₂ = 1)"". The tower is on the page; it
  upgrades the two-sided bound.
- **m3 (V₂, l. 309).** "The first, V₂" — the box's enumeration order is not stated; under (|a₁|, a₁, |a₂|) the first hit is (a₁, a₂) = (0, 11)
  (`o_twin.log`). NEW "One of them, V₂ (the first with a₁ = −1)". Add: 105 of the 111 are caught by Theorem 1 (5) at some Q ∈ {5⁴, 5⁶, 5⁸};
  6 are not, so "non-real off-line roots" does not by itself mean "caught early".
- **m4 (l. 61).** "Milne p. 10's def form 2(gm² + amn + gqn²)" is not printed; it is the expansion of the p. 10 display (proof of Cor 1.6) at
  (D, D′) = (Δ, Γ_π). NEW "the def form 2(gm² + amn + gqn²) (Milne p. 10, Cor 1.6's proof at (Δ, Γ_π))".
- **m5 (Z1(c), l. 236–241).** This is Landau's classical oscillation theorem (a one-sided bound ψ(x) − x ≤ Cx^θ forces Θ ≤ θ; Ingham 1932
  ch. V `[recalled, unverified]`); name it as the nearest object. The NOTE already limits novelty to "the reading".
- **m6 (Theorem P (iii), l. 266–267).** (iii) follows from V's existence alone — any proof using only the zeta datum would prove RH for V;
  the table adds WHERE each proof breaks, not THAT it must. Say so, so that (iii) is not read as the theorem's content.
- **m7 (R13, l. 209–211).** Ex. 11.4's bound as printed has abs(S·S^t); at S = Δ and g ≥ 2 this gives (2g)(2 − (2g − 2)) ≤ 0, impossible, so
  the printed absolute value must be read as the signed S·S^t (then (2g)² and 2g√q). At g = 1 (the NOTE's use) both readings give 2√q = 4.472.
  A reader's note on the source, not an error of the NOTE.
- **m8 (R6).** At Q = 5² the twist meets (8) as printed with equality (41 ≤ 41); the NOTE's "(8) as printed … violated at Q = 5⁴" is
  consistent with this — no change needed; flagged only so no one "fixes" it to 5².
