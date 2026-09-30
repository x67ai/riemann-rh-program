# PRIOR-ART — staircase seed (N2): truncations of Riemann's incomplete-gamma series

Literature sub-agent, 2026-09-30. Every quote was read on a page on disk in `lit/` unless tagged
**[recalled, unverified]**. Pages are the PDF's printed pages; "[...]" marks a cut inside a quote. Formula decorations
lost by text extraction were checked on page renders in `img/`. `queries.log` lists every query with its hit count.

## 0. Summary — Haglund, answers to 1(a)–(d)
J. Haglund, "Some conjectures on the zeros of approximates to the Riemann Ξ-function and incomplete gamma functions",
arXiv:0910.5228v1 (27 Oct 2009; `haglund-0910.5228.pdf/.txt`); Cent. Eur. J. Math. 9 (2011) 302–318, DOI
10.2478/s11533-010-0095-3 (open access; full text with page markers: `haglund-CEJM-2011-degruyter-fulltext.md`). Pages
below are arXiv pages. The journal text is the same, renumbered (Conj. 2.1 and Prop. 2.2 p. 304, table p. 305, Conj. 3.1
p. 306, Conj. 3.2 p. 307, Conj. 5.1 p. 311), plus a Cauchy–Riemann remark on "M-curves" (p. 311).

**(a) Definition.** s = 1/2 + iz: "Ξ(z) = ½(.5 + iz)(−.5 + iz)π^{−(.5+iz)/2}Γ(½(.5 + iz))ζ(.5 + iz)" (1), p. 1. Riemann's
"Ξ(z) = ∫_0^∞ cos(zt)φ(t) dt, (2) where φ(t) = Σ_{n=1}^∞ φ_n(t) with φ_n(t) = exp(−n²π exp(2t))(8π²n⁴ exp(4.5t) − 12πn²
exp(2.5t)). (3)" (p. 1); "a natural question to ask is what happens if we replace φ(t) by Σ_{n=1}^N φ_n(t)." (p. 2). With
"G(z; a, b) = 4 ∫_0^∞ cos(2zu) exp(2bu − a exp(2u)) du" (6) "= Γ(b + iz, a)/a^{b+iz} + Γ(b − iz, a)/a^{b−iz}" (10) (p. 2):
"the Ξ-approximates Ξ_N(z) := Σ_{n=1}^N Φ_n(z), (13) where Φ_n(z) := 2π²n⁴ G(z/2; n²π, 9/4) − 3πn² G(z/2; n²π, 5/4), (14)" (p. 3).

**Relation to the seed's C1 truncation (derived here, not in Haglund).** With a = πn² and Γ(w+1, a) = wΓ(w, a) + a^w e^{−a}:
Φ_n(z) = ½s(s−1)g_n(s) + (4πn² − 1)e^{−πn²}, hence

    Ξ_N(z) = ξ_N(s) − c_N,   ξ_N(s) := ½ + ½s(s−1)Σ_{n≤N} g_n(s),   c_N := Σ_{n>N} (4πn² − 1)e^{−πn²} > 0,

by Σ_{n≥1}(4πn² − 1)e^{−πn²} = 1/2 (θ(1/x) = √x θ(x) differentiated at x = 1); c_1 = 1.71805662585×10⁻⁴, c_2 =
5.8912588544×10⁻¹¹, c_3 = 2.959×10⁻²⁰. `tools/check_haglund.py` (40 digits; log `tools/check_haglund.log`) confirms the
identity to 10⁻⁴¹ at four complex points (n = 1, 2) and (14) against the integral (2); at Haglund's listed zeros of Ξ_1,
|Ξ_1| ≈ 10⁻²⁶ while ξ_1 = c_1. **So Ξ_N is the seed's ξ_N minus its limit c_N on the critical line; Haglund's zero tables
are the c_N-level set of ξ_N, not its zeros.** On the line Ξ_N(x) ~ C_N/x² → 0 ((50)–(52), p. 10), whereas ξ_N → c_N > 0.

**(b) Proved.** Only: "Proposition 1 Conjecture 1 implies the Riemann Hypothesis." (p. 3; proof pp. 3–4, see (c)); an
informal asymptotic section with no theorem (pp. 8–9): "the zeros of Γ(z, a) in Q satisfy y ∼ (2/π) x ln x as |z| → ∞"
(p. 8), "the zeros of any function of the form (48) also satisfy x ∼ (2/π) y ln y as |z| → ∞" (p. 9), (48) being any
finite ℂ-combination Σ u_k G(z; a_k, b_k), so every Ξ_N (in the variable z/2); and "Φ_1(x) = −.01974938206/x² + O(1/x⁴) [...] Φ_2(x) =
.01974934121/x² [...] Φ_3(x) = .4132639753 × 10⁻⁷/x²" (52) with "the coefficient of 1/x² in Ξ_N(x) is positive for k ≥ 3 and
negative for 1 ≤ k < 3" (p. 10; his k is N): each Ξ_N keeps one sign far out on the real axis. **Nothing is proved for
N = 1.** His N = 1 data ("zeros of first Ξ-approximate Ξ_1(z) in rectangle with corners (0, −.1), (100, 500)", p. 16): ONE
real zero "14.04543957882981756479858", then 18 non-real zeros from "20.62534600592171760132974 + 2.697151842339519632505712 I"
to "96.90904939663401491219210 + 40.51951660155401879741380 I", imaginary parts increasing. So Ξ_1 does not have all zeros
real; the N = 1 claim is numerical monotonicity. In s, 20.625 + 2.697i is s = −2.197 + 20.625i: left of the strip.

**(c) Conjectured.** "We say that a given function F(z) has monotonic zeros in a region D of the complex plane if, when
we list the zeros of F in D by increasing real part, the imaginary parts of the zeros are monotone nondecreasing." (p. 3).
"Conjecture 1 For N ∈ ℕ, Ξ_N(z) has monotonic zeros in Q." (p. 3; Q = closed first quadrant, p. 1). NOT "all zeros real".
Weak form, Remark 1 (p. 4): "there are no non-real zeros of Ξ_N(z) in Q whose real part is less than the largest real zero
of Ξ_N(z)". Why RH follows (p. 3): "This follows from the argument principle, combined with the simple fact that a
function with infinitely many positive real zeros, and with monotonic zeros in Q, has only real zeros in Q." Proof
(pp. 3–4): take τ = σ + it, the non-real zero of Ξ in Q of least real part; "choose N sufficiently large so that Ξ_N(z) has
a real zero γ with γ > 2σ"; then Ξ_N has no non-real zero in Q with real part < 2σ, so its winding number on a small
circle about τ is 0 while Ξ's is 1, contradicting uniform convergence (Hurwitz). Also: Conjecture 2 (p. 5, Ramanujan
Ξ_{Δ,N}); "Conjecture 3 For any fixed positive real number a, the incomplete gamma function Γ(z, a) has monotonic zeros in
Q." (p. 7); "Conjecture 4 For k ≥ 1, the imaginary part of each non-real zero of Ξ_k(z)+t Φ_{k+1}(z) decreases
monotonically (i.e. continuously) as t goes from 0 to 1." (p. 11). He shows tΦ_1 + Φ_2 has non-monotone zeros at
"t = .999997907459" (p. 10).

**(d) Numerics.** Maple, "Digits [...] typically set to 20N − 10", rechecked at 20N; "no attempt has been made to establish
rigorous error bounds" (p. 3). "Computations along these lines indicate this weaker form of Conjecture 1 is true at least
for N ≤ 10." (p. 4). Table, p. 4 (N | largest real zero | number of real zeros): 1 | 14.0454395788 | 1; 2 | 39.5324810798
| 7; 3 | 65.0320737720 | 15; 4 | 103.3679880094 | 32; 5 | 149.0026994921 | 53; 6 | 197.9575955732 | 79; 7 |
258.5304836632 | 113; 8 | 327.3794646017 | 155; 9 | 406.8174206801 | 207; 10 | 489.3900649445 | 263. Appendix: Ξ_1 (above,
p. 16); Ξ_2 in [0,102]×[−.1,100]: 7 real ("14.1347251016..." to "39.5324810797..."), then 15 non-real from
"43.1389080680988950956236929709951507 + 3.28097100306881350163884998294539870 I" to "100.087228624602886284768301012877784 +
32.4941324878154139135000560357642324 I" (pp. 16–17); Ξ_3 in [0,66]×[−.1,67]: 15 real zeros ("14.1347251417..." to
"65.0320737719..."), none non-real (p. 17). Limits (p. 12): Maple on Ξ_2 "never finished even after running for over two
days"; continuation to Ξ_3 failed near "t = .99". No zero above Re z ≈ 102 is listed. Pattern noticed here, not by
Haglund: largest real zero ≈ 4(N+1)².

## 1–2. Follow-ups to Haglund (task 2)
Citers: Semantic Scholar 12 records, OpenAlex 8. None of them, and no search hit, studies the zeros of Ξ_N further or
extends Conjecture 1.
- **Lagarias–Montague, arXiv:1106.4348** (Jun 2011; Comment. Math. Univ. St. Pauli 60 (2011) 143–169; on disk). Abstract:
  "Members of this family are shown to have only finitely many zeros on the critical line, with ξ^{(−1)}(s) having exactly
  one zero on the critical line, at s = 1/2." p. 24: "For an possibly related situation involving the ξ-function, where
  such a monotonicity implies the RH, see Haglund [23]." Relevance: a Fourier-integral family with finitely many zeros
  on the line, as for ξ_N.
- **Matiyasevich–Saidak–Zvengrowski, arXiv:1205.2773** (May 2012; Acta Arith. 166 (2014) 189–200; on disk). Abstract: "the
  absolute values of Riemann's zeta function and two related functions strictly decrease when the imaginary part of the
  argument is fixed to any number with absolute value at least 8 and the real part of the argument is negative and
  increases up to 0". Cites only Haglund §6 (p. 5). Low relevance.
- Claimed RH proofs (listed, not assessed): Y. Shi arXiv:1706.08868 (math.GM); C.-M. Chen arXiv:2005.12525 (+ Adv. Pure
  Math. 2020–22); J. Breslaw arXiv:1002.0352v9 (abstract: "depicts the Xi function as the weighted sum of incomplete gamma
  functions [...] thus validating the Riemann hypothesis").
- Other: G. Iurato arXiv:1410.6450 and J. Korevaar, Indag. Math. 2013 (history); M. DeFranco arXiv:1909.06941 (abstract:
  "We then apply this series to obtain a formula for the Riemann xi function valid at any s ∈ ℂ"); a 2012 nuclear-kinetics
  paper (irrelevant).

## 3. Related theorems (task 3)
**3(a) Lagarias–Suzuki, arXiv:math/0412039v4; J. Number Theory 118 (2006) 98–122** (on disk). ζ*(s) := π^{−s/2}Γ(s/2)ζ(s)
(p. 2). "Theorem 3. For each y ≥ 1 the constant term of the Eisenstein series a_0(y, s) := ζ*(2s)y^s + ζ*(2 − 2s)y^{1−s}
[...] satisfies the modified Riemann hypothesis. There is a critical value y* := 4πe^{−γ} = 7.055507+ [...] (1) All zeros of
a_0(y, s) lie on the critical line for 1 ≤ y ≤ y*. (2) For y > y* there are exactly two zeros off the critical line. These
are real simple zeros ρ_y, 1 − ρ_y with 1/2 < ρ_y < 1." (p. 5). "Hejhal [12, p. 89] noted that for 0 < y < 1 the function
a_0(y, s) has complex zeros off the critical line, with arbitrarily large real part." (p. 5). Theorem 2 (p. 4): I(T, s) =
−ζ*(2s)T^{s−1}/(s − 1) + ζ*(2 − 2s)T^{−s}/s "has all its zeros in the critical line" for T ≥ 1; "The hypothesis T ≥ 1 cannot
be relaxed". Theorem 4 (p. 7, after Pólya's "Hilfssatz II"): for F entire of genus ≤ 1, real, F(s) = ±F(1 − s), zeros in
|ℜ(s) − 1/2| < a, "Then for any real c ≥ a, |F(s + c)/F(s − c)| > 1 if ℜ(s) > 1/2". Announced, not proved there (p. 6): for
H(y, s) = p(s)ζ*(s)y^s + p(1 − s)ζ*(2 − 2s)y^{1−s}, "all but finitely many of the zeros of H(y, s) lie on the critical line".
Relevance: a_0(y, s) is an "E + E^#" function built from ζ*; RH for it needs the shift y ≥ 1, as h ≥ 1/2 in 3(c).

**3(b) H. Ki.** "Zeros of the constant term in the Chowla–Selberg formula", Acta Arith. 124 (2006) 197–204 (on disk):
C(z; s) = ζ(2s)y^s + √π(Γ(s − 1/2)/Γ(s))ζ(2s − 1)y^{1−s} (p. 197); "Theorem. For any y ≥ 1 all complex zeros of C(z; s) are
simple and lie on Re(s) = 1/2." (p. 198); method: "we apply a variant of Hermite–Biehler theorem" (p. 198), on F(z) =
(z + i/2)Ξ(2z − i/2)Y^{iz} + (z − i/2)Ξ(2z + i/2)Y^{−iz} (p. 199). **His Proc. LMS theorem, as he restates it (p. 198):**
"the author [6, Corollary 1] has shown that for any y ≥ 1 and any N = 1, 2, 3, . . ., all but finitely many complex zeros of
any Nth partial sum in the Chowla–Selberg formula are simple and on Re(s) = 1/2. Since E_0(i; s) = 2ζ(s)L(s, χ_{−4}), the
Riemann hypothesis would follow if, for infinitely many N, one was somehow able to remove the "but finitely many" clause
in this corollary in the (very special) case where z = i." For 0 < Y < 1 (p. 203): "it is known (see [6, Theorem 2]) that for any δ > 0 all but
finitely many zeros of f(s) in {s : |Re(s) − 1/2| < δ} are simple and lie on Re(s) = 1/2." [6] = Ki, Proc. London Math. Soc. 90 (2005) 321–344 (corrig. 94 (2007)
543–544); paywalled, not read. Also "On the nontrivial zeros of modified Epstein zeta functions", C. R. Acad.
Sci. Paris 342 (2006) 79–81 (on disk): the truncation result holds "if √Δ/(2a) ⩾ 1" (p. 80); "Theorem 1.1. Let δ > 0. Then
all but finitely many zeros of Z(s; y, α, β, L_1, . . . , L_n) in {s ∈ ℂ: |Re(s) − 1/2| < δ} are simple and on Re(s) = 1/2."
(p. 81, needs deg α ≥ deg β + 1); the RH case "cannot say anything about the function Z_{u²+v²,1,1}(s) because α(s) = 1 and
β(s) = 1 do not satisfy assumption (ii)" (p. 81). Relevance: closest proved analog; truncation gives "all but finitely
many", never "all".

**3(c) Lagarias, "Zero spacing distributions for differenced L-functions", Acta Arith. 120 (2005) 159–184,
arXiv:math/0601653** (on disk). A_h(s) := ½(ξ(s + h) + ξ(s − h)), B_h(s) := −(1/2i)(ξ(s + h) − ξ(s − h)) (p. 163). "Lemma 2.1.
(1) If h ≥ 1/2, then |ξ(h + s)| > |ξ(h + 1 − s)| for ℜ(s) > 1/2. (2) Assuming the Riemann hypothesis, the inequality (2.3)
holds for each h > 0." (p. 164). "Theorem 2.1. (1) For |h| ≥ 1/2 and any 0 ≤ θ < 2π, the entire functions A_{h,θ}(s) and
B_{h,θ}(s) have all their zeros on the critical line ℜ(s) = 1/2. These zeros are all simple zeros, and they interlace."
(p. 168; (2) = same for 0 < |h| < 1/2 under RH). "Lemma 6.1. (i) For h ≥ 1/2 the function E_h(z) := ξ(1/2 + h − iz) is a de
Branges structure function" (p. 179). History (p. 162): results "known to de Branges in the late 1980's"; analogous results
for ζ̂ = π^{−s/2}Γ(s/2)ζ(s) by Ki (J. Number Theory 107 (2004)). Relevance: the HB/de Branges template; the unconditional range starts where ξ(s + h) is zero-free for ℜs > 1/2.
"Hilbert spaces of entire functions and Dirichlet
L-functions" (Frontiers in Number Theory, Physics and Geometry I, 2006, DOI 10.1007/978-3-540-31347-2_10): not found on
arXiv, not read.

**3(d) Taylor, Quart. J. Math. os-16 (1945) 1–21** (not read). Both secondary sources say ζ* and MINUS, not
ξ(s+½) + ξ(s−½): Lagarias–Suzuki p. 6: "He showed that ζ*(s + 1/2) − ζ*(s − 1/2) has all its zeros on the critical line.";
Nakamura–Pańkowski, "Any non-monomial polynomial of the Riemann zeta-function has complex zeros off the critical line",
arXiv:1212.5890v4 (Dec 2012), p. 4: "Taylor [41] showed that ζ*(s + 1/2) − ζ*(s − 1/2), ζ*(s) := π^{−s/2}Γ(s/2)ζ(s) has
all its zeros on the critical line ℜ(s) = 1/2." The ξ-form ½(ξ(s+½) + ξ(s−½)) is Lagarias's Theorem 2.1 at h = 1/2. Relevance: the one-step "shift and add" instance.

**3(e) Pólya, Acta Math. 48 (1926) 305–317** (paywalled). Gasper, "Using integrals of squares of certain real-valued special functions to prove that the Pólya Ξ*(z)
function, [...] have only real zeros", arXiv:0801.2996 (Jan 2008), p. 2: "Pólya [18] observed that Φ(u) ∼
8π² cosh(9u/2) e^{−2π cosh(2u)} as u → ±∞ (1.3) [...] Ξ*(z) = 16π² ∫_0^∞ cosh(9u/2) e^{−2π cosh(2u)} cos(zu) du (1.4) [...]
Pólya was able to prove that Ξ*(z) has only real zeros", via "Ξ*(z) = 4π²[K_{iz/2−9/4}(2π) + K_{iz/2+9/4}(2π)]" and the
"Lemma. If −∞ < c < ∞ and G(z) is an entire function of genus 0 or 1 that assumes real values for real z, has only real
zeros and has at least one real zero, then the function G(z − ic) + G(z + ic) also has only real zeros." Haglund p. 2
writes the kernel with "exp(−π cosh(2t))"; Gasper's e^{−2π cosh(2u)} is the one consistent with Φ's asymptotics. Relevance:
a real-rooted one-term (n = 1) kernel; it symmetrizes the n = 1 term, which Haglund's half-line Ξ_1 does not.

**3(f) Other approximants and "h(s) ± h(1−s)" tools.** Hejhal, J. Anal. Math. 55 (1990) 59–95 (not read): per Haglund
(journal p. 303), with Pólya approximates Σ_{n≤N} "the resulting function asymptotically has 100% of its zeros on the real
line (but, for N > 1, infinitely many zeros off the line)". Ki, Ramanujan J. 17 (2008) (not read): per Chirre–Velásquez Castañón,
"A note on the zeros of approximations of the Ramanujan Ξ-function", arXiv:2004.14465 (Apr 2020), p. 2, "all but finitely many zeros of C_F(s) which lie in |Re s| ≤ δ are on the line Re s = 0" provided
ψ_F(s − k) has finitely many zeros in a strip, ψ_F(s) = π^{−s}Σ_{m=0}^n a_m(2m + 1)^{−s} a Dirichlet polynomial; their
Theorem 3 (p. 3) adds simplicity. Velásquez Castañón, "Majoration du nombre de zéros d'une fonction méromorphe en dehors d'une droite
verticale et applications", arXiv:0712.1266 (Dec 2007), abstract: for f = h(s) ± h(2a − s), "all but finitely
many of the zeros of f(s) lie on the line Re s = a [...] given that all but finitely many of the zeros of h(s) lie on the
half-plane Re s < a" (ξ_N has this shape, a = 1/2). Klinger-Logan, "A spectral interpretation of zeros of certain functions",
arXiv:1706.08552 (Jun 2017), abstract: for h "with no zeros in
Re(s)>1/2 and no poles in Re(s)<1/2, real-valued on ℝ, h(1−s)/h(s) ≪ |s|^{1−ε} in Re(s)>1/2 and h(1−s)/h(s) ∉ L²(1/2+iℝ), the
only zeros of h(s)±h(1−s) are on the critical line." Zero hits: "partial theta"∧zeta; "de Bruijn-Newman"∧"incomplete gamma".

## 4. Novelty of the prime chain C2 (Σ g_n over S-smooth n)
The idea is in print as Matiyasevich's "regularized truncated Euler products" (Proc. Steklov Inst. 299 (2017); not on
arXiv, not read). For L(s, χ), cusp forms and elliptic curves the published approximant IS the incomplete-gamma series
over smooth n. For ζ the published approximant is a different regularization; the literal ½ + ½s(s−1)Σ_{n S-smooth} g_n(s)
was not found in print.
- **Alzergani, "Family of approximations for Dirichlet L-functions", arXiv:2311.18816** (Nov 2023; on disk), Theorem 1 (p. 6): "Let χ be a fixed primitive Dirichlet character
  of conductor q. Fix s_0 ∈ ℂ and let A_u be the set of all positive integers with at least one prime factor greater than
  u. Then ξ(s_0, χ) − ξ_u^≈(s_0, χ) = Σ_{n∈A_u} J(n)", J(n) = χ(n)n^κ(q/(n²π))^{(κ+s_0)/2}Γ((κ+s_0)/2, n²π/q) + ε(χ)χ̄(n)n^κ
  (q/(n²π))^{(κ+1−s_0)/2}Γ((κ+1−s_0)/2, n²π/q). As ξ(s, χ) = Σ_{all n} J(n), ξ_u^≈ = Σ over u-smooth n: C2 for L(s, χ).
- **Huang–Spinelli, "Approximation of L-functions associated to Hecke cusp eigenforms", arXiv:2406.08608v2** (Jun 2024): "Proposition 6. For all s ∈ ℂ, Λ_N(s) = ∫_1^∞ (t^{s−1} + (−1)^P t^{k−1−s})
  f_N(it/√C) dt." (p. 12), f_N keeping a_n when "n is a product of primes ≤ p_N" (p. 11); Corollary 4, the incomplete-gamma
  error series (p. 12).
- **Nastasescu–Stoica–Zaharescu, "A visual perspective on the Birch and Swinnerton-Dyer conjecture through a family of
  approximations of L-functions", arXiv:2311.07641** (Nov 2023): Theorem 5 (p. 18), error = incomplete-gamma series over n
  with "p|n for some prime p > p_N". p. 1: "In the case of the Riemann zeta function, the approximations introduced in [9]
  are conjectured to satisfy a Bounded Riemann Hypothesis [9, 10]. This means that for any integer k ⩾ 1, there exists a
  level of the approximation (i.e. a number of primes included in the approximation) such that the first k zeros of the
  approximation [...] are on the critical line." and "for L-functions associated to elliptic curves, we will show that
  the Bounded Riemann Hypothesis does not hold for our approximations".
- **Liu–Matiyasevich–Oesterlé–Zaharescu, "Euler Product Sieve", arXiv:2406.00786** (Jun 2024). ζ-construction (p. 3): ζ_B = Π_{p∈B}(1 − p^{−s})^{−1},
  ξ_B = g(s)ζ_B, multiply by s^m(1 − s)^m (m = |B|), remove the principal parts at the "ghost poles" 2nπi/log p and at −2n,
  symmetrize, divide by s^m(1 − s)^m ((2.6)). Error, from Nastasescu–Zaharescu JMAA 514 (2022) Thm 1 (not read): "ξ(s) −
  ξ_u^≈(s) = 2(−1)^m(2πp²_{m+1})^{2m+2}e^{−πp²_{m+1}} / (s^m(1 − s)^m) · a(2πp²_{m+1}, s)(1 + O(1/log u))" (6.2), p. 13 (render
  `img/lmoz-p-13.png`). C2's error is exactly ½s(s−1)Σ_{n not S-smooth} g_n(s) (from C1), led by n = p = p_{m+1}, and g_p(s) ≈ 2e^{−πp²}a(2πp² + 2, s)
  (derived here; within 0.3% for p = 3, `tools/check_haglund.log`). Taking (6.2) at face value, the two errors differ by
  a factor ≈ 2(2πp²)^{2m+2}/(s(1−s))^{m+1}, so C2 is not Matiyasevich's ζ-approximant. "Theorem 1.7. The Bounded Riemann Hypothesis is
  equivalent to the Riemann Hypothesis plus the Simplicity Conjecture." (p. 3).
- Queries (counts in `queries.log`): "smooth numbers"∧{"incomplete gamma", "theta function", "Riemann xi", zeros∧"functional
  equation"} 0,0,0,0; "S-units"∧{"theta function", "incomplete gamma"} 0,0; "partial Euler product"∧{"Riemann xi",
  "incomplete gamma", theta} 0,0,0, ∧zeros∧"critical line" 2 (irrelevant); "finite Euler product"∧"functional
  equation"∧zeros 0; "Euler product"∧"incomplete gamma" 1 (2406.08608); "truncated Euler product"∧approximation∧zeta 0;
  "Euler product"∧"theta function"∧zeros∧"critical line" 0; au:Matiyasevich 21; au:Nastasescu 22; au:Alzergani 1.

## 5. Hamburger's theorem (added at the seed agent's request)
- **Burnol, "Deux extensions de Théorèmes de Hamburger", arXiv:1106.4749v2** (Expo. Math. 30 (2012) 295–308; on disk; renders `img/burnol-p-02.png`, `-03.png`), p. 2,
  the original: "Théorème (Hamburger, [7]). Soit f une fonction méromorphe dans le plan complexe tout entier, et d'ordre
  fini (f est O(e^{|s|^k}) avec un certain entier k pour |s| → ∞, en particulier ne possède au plus qu'un nombre fini de
  pôles). Si f(s) est représentée pour Re(s) > 1 par une série de Dirichlet Σ a_n n^{−s} absolument convergente, et si la
  fonction méromorphe g(s) = χ(s)f(1 − s) admet elle aussi, pour Re(s) ≫ 1, une représentation sous la forme d'une série de
  Dirichlet convergente Σ b_n n^{−s}, alors f est un multiple de la fonction zêta." χ(s) = π^{−(1−s)/2}Γ((1−s)/2)/(π^{−s/2}Γ(s/2));
  [7] = Hamburger, Math. Z. 10 (1921) 240–254.
- **Nakamura, "Dirichlet series with periodic coefficients, Riemann's functional equation and real zeros of Dirichlet
  L-functions", arXiv:2008.02570v4** (Aug 2020), p. 4: "Theorem D (Hamburger [5, Satz 1]). Suppose that F(s) satisfies F(s) = Σ a(n)n^{−s},
  where a(n) ∈ ℂ, converges absolutely for σ > 1, (H1) P(s)F(s) is an entire function of finite order for some polynomial
  P(s), (H2) ξ_F(1 − s) = ξ_F(s), where ξ_F(s) := π^{−s/2}Γ(s/2)F(s). (H3) Then, one has F(s) = Cζ(s), where C is a constant."
- **Only SOME half-plane:** fails as stated. Nakamura p. 4: "In [7, Theorem 1], Knopp showed that there are infinitely
  many linearly independent solutions which satisfy (H2), (H3) and F(s) = Σ a(n)n^{−s}, where a(n) ∈ ℂ, converges absolutely
  in some half-plane. (K)" (Knopp, Invent. Math. 117 (1994); not read). Burnol's version (pp. 2–3) needs only "une série de
  Dirichlet qui converge pour Re(s) suffisamment grand", finitely many poles, f = O(e^{exp ε|s|}) in strips, and "∃ N ∈ ℕ,
  ∃ y > 1/2, g(s) = O(|s|^N y^{−s}) pour Re(s) → +∞"; conclusion "f(s) = Σ_{k∈ℤ} c_k ζ(s − 2k)" (finite). Corollaire 2 (p. 3):
  adding "g(σ) = c + O(σ^{−k}) pour tout k ∈ ℕ" gives "f(s) = cζ(s)". Titchmarsh §2.13's form is [recalled, unverified].

## 6. Files in lit/
PDFs + `.txt` (pdftotext -layout): haglund-0910.5228, ki-AA-124-2006-chowla-selberg, ki-CRAS-342-2006-modified-epstein,
lagarias-AA-120-2005-differenced, lagarias-suzuki-math0412039, nakamura-pankowski-1212.5890, gasper-0801.2996,
lagarias-montague-1106.4348, matiyasevich-saidak-zvengrowski-1205.2773, chirre-velasquez-2004.14465, huang-spinelli-2406.08608,
liu-matiyasevich-oesterle-zaharescu-2406.00786, shi-1502.06844, shi-1706.08868, alzergani-2311.18816,
nastasescu-stoica-zaharescu-2311.07641, nastasescu-robles-stoica-zaharescu-2311.07657, burnol-1106.4749, nakamura-2008.02570.
Also `haglund-CEJM-2011-degruyter-fulltext.md`; `api/` (raw API/Crossref/S2/OpenAlex/Firecrawl responses); `img/`; `tools/`
(aq.py query helper, abs.py, fc.sh, check_haglund.py + log); `queries.log`.
