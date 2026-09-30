# PRIOR-ART — staircase seed (N2), literature read

Written by the literature sub-agent, 2026-09-30. Everything quoted below was read on a page on disk in
this folder unless it carries the tag **[recalled, unverified]**. Page numbers are the PDF's printed page
numbers. `queries.log` lists every API query with its hit count. (Draft in progress; sections are appended as
they are read.)

## 0. Summary — answers to 1(a)–(d) (Haglund)

Source: J. Haglund, "Some conjectures on the zeros of approximates to the Riemann Ξ-function and incomplete
gamma functions", arXiv:0910.5228v1 [math.NT], 27 Oct 2009 (dated October 16, 2009), 23 pp.; published
Cent. Eur. J. Math. 9 (2011) 302–318, DOI 10.2478/s11533-010-0095-3 (online 29 Dec 2010; Crossref).
On disk: `haglund-0910.5228.pdf`, `haglund-0910.5228.txt`; page renders `img/haglund-p-08.png`, `-09.png`.
Page numbers below are arXiv v1 pages. The published version is open access at De Gruyter; its full text (page
markers 302–318 included) is in `haglund-CEJM-2011-degruyter-fulltext.md` (Firecrawl scrape; the Springer copy is
paywalled). It has the same content, renumbered: Conjecture 2.1 and Proposition 2.2 on p. 304, proof pp. 304–305,
Remark 2.3 and the N ≤ 10 table p. 305, Conjecture 3.1 p. 306, Conjecture 3.2 p. 307, Section 4 pp. 308–309, the
Φ_1, Φ_2, Φ_3 expansions p. 310, Conjecture 5.1 p. 311, notes on computations p. 312, appendix from p. 313. Two
differences found: the Hejhal sentence becomes "then the resulting function asymptotically has 100% of its zeros on
the real line (but, for N > 1, infinitely many zeros off the line)" (p. 303), and Section 6 gains a Cauchy–Riemann
heuristic for why zeros sit at local maxima of the "M-curve" (eqs. (18)–(20), p. 311).

**(a) Definition.** Variable z, with s = 1/2 + iz: "Ξ(z) = ½(.5 + iz)(−.5 + iz)π^{−(.5+iz)/2}Γ(½(.5 + iz))ζ(.5 + iz)"
(eq. (1), p. 1), so Ξ(z) = ξ(1/2 + iz) and "RH says that all the zeros of Ξ are real" (p. 1). Riemann's
"Ξ(z) = ∫_0^∞ cos(zt)φ(t) dt, (2) where φ(t) = Σ_{n=1}^∞ φ_n(t) with φ_n(t) = exp(−n²π exp(2t))(8π²n⁴ exp(4.5t) −
12πn² exp(2.5t)). (3)" (p. 1). The truncation is of the kernel series inside the half-line integral: "a natural
question to ask is what happens if we replace φ(t) by Σ_{n=1}^N φ_n(t)." (p. 2). With the "hyperbolic gamma
function" "G(z; a, b) = 4 ∫_0^∞ cos(2zu) exp(2bu − a exp(2u)) du" (6) "= Γ(b + iz, a)/a^{b+iz} + Γ(b − iz, a)/a^{b−iz}" (10)
(p. 2; Γ(z, a) the upper incomplete gamma function, (11), p. 3), he defines "the Ξ-approximates
Ξ_N(z) := Σ_{n=1}^N Φ_n(z), (13) where Φ_n(z) := 2π²n⁴ G(z/2; n²π, 9/4) − 3πn² G(z/2; n²π, 5/4), (14)" (p. 3).

**Relation to the seed's C1 truncation (derived here, not in Haglund; checked numerically).** Using
Γ(w+1, a) = wΓ(w, a) + a^w e^{−a} twice, with a = πn², s = 1/2 + iz and
g_n(s) = a^{−s/2}Γ(s/2, a) + a^{−(1−s)/2}Γ((1−s)/2, a):

    Φ_n(z) = ½ s(s−1) g_n(s) + (4πn² − 1) e^{−πn²},
    Ξ_N(z) = ξ_N(s) − c_N,   ξ_N(s) := ½ + ½ s(s−1) Σ_{n≤N} g_n(s),   c_N := Σ_{n>N} (4πn² − 1) e^{−πn²} > 0,

because Σ_{n≥1}(4πn² − 1)e^{−πn²} = 1/2 (the derivative of θ(1/x) = √x θ(x) at x = 1). c_1 = 1.71805662585×10⁻⁴,
c_2 ≈ 5.9×10⁻¹¹. `tools/check_haglund.py` (log `tools/check_haglund.log`) confirms the identity to 10⁻⁴¹ at four
complex points for n = 1, 2, confirms (14) against the integral (2), and evaluates Haglund's listed zeros of Ξ_1:
|Ξ_1| ≈ 10⁻²⁶ there, while |ξ_1| = c_1 there. **So Haglund's Ξ_N is the seed's ξ_N minus its limiting constant
c_N on the critical line; Haglund's zero tables are tables of the c_N-level set of ξ_N, not of its zeros.** On
the critical line Ξ_N(x) → 0 like C_N/x² (his (50)–(52), p. 10), while ξ_N(x) → c_N > 0.

**(b) What is proved.** Only (i) Proposition 1 (p. 3): "Conjecture 1 implies the Riemann Hypothesis.", with a
proof (pp. 3–4) by the argument principle and uniform convergence; (ii) an informal asymptotic analysis
(Section 4, pp. 8–9, no theorem environment) concluding "the zeros of Γ(z, a) in Q satisfy y ∼ (2/π) x ln x as
|z| → ∞" (p. 8) and "the zeros of any function of the form (48) also satisfy x ∼ (2/π) y ln y as |z| → ∞" (p. 9),
(48) being any finite ℂ-linear combination Σ u_k G(z; a_k, b_k), which includes every Ξ_N; (iii) the real-axis
expansion "Φ_1(x) = −.01974938206/x² + O(1/x⁴) ... Φ_2(x) = .01974934121/x² + O(1/x⁴) ... Φ_3(x) = .4132639753 × 10⁻⁷/x² +
O(1/x⁴)" (52), p. 10, with "the coefficient of 1/x² in Ξ_N(x) is positive for k ≥ 3 and negative for 1 ≤ k < 3" (p. 10;
his k means N), so each Ξ_N has constant sign far out on the real axis. **Nothing is proved about N = 1.** For
N = 1 the paper's own data (Appendix, p. 16, "Digits := 25, zeros of first Ξ-approximate Ξ_1(z) in rectangle with
corners (0, −.1), (100, 500)") show ONE real zero, "14.04543957882981756479858", followed by 18 non-real zeros
"20.62534600592171760132974 + 2.697151842339519632505712 I", "26.05616693357829946749575 + 7.125359707612690330897455 I",
…, "96.90904939663401491219210 + 40.51951660155401879741380 I", with increasing imaginary parts. So Ξ_1 does NOT have
all zeros real; the statement for N = 1 is numerical monotonicity of imaginary parts. (In s = 1/2 + iz, the
zero 20.625 + 2.697i sits at s = −2.197 + 20.625i: the non-real zeros lie far LEFT of the critical strip.)

**(c) What is conjectured.** Definition (p. 3): "We say that a given function F(z) has monotonic zeros in a region
D of the complex plane if, when we list the zeros of F in D by increasing real part, the imaginary parts of the
zeros are monotone nondecreasing." Then: "Conjecture 1 For N ∈ ℕ, Ξ_N(z) has monotonic zeros in Q." (p. 3; Q is the
closed first quadrant, p. 1). He does NOT conjecture that the zeros of Ξ_N are real. Weak form, "Remark 1 A weaker
form of Conjecture 1, which still implies RH, is that there are no non-real zeros of Ξ_N(z) in Q whose real part is
less than the largest real zero of Ξ_N(z)." (p. 4). How it implies RH (p. 3): "This follows from the argument
principle, combined with the simple fact that a function with infinitely many positive real zeros, and with
monotonic zeros in Q, has only real zeros in Q." The proof (pp. 3–4): if τ = σ + it is the non-real zero of Ξ in Q
of least real part, "choose N sufficiently large so that Ξ_N(z) has a real zero γ with γ > 2σ ... By assumption Ξ_N(z)
has monotonic zeros in Q, hence has no non-real zeros in Q with real part less than 2σ", so the winding number of Ξ_N
around a small circle about τ is 0 while that of Ξ is 1, contradicting uniform convergence (Hurwitz). Also:
Conjecture 2 (p. 5, Ramanujan Ξ_{Δ,N}), Conjecture 3 (p. 7, "For any fixed positive real number a, the incomplete
gamma function Γ(z, a) has monotonic zeros in Q."), Conjecture 4 (p. 11, "For k ≥ 1, the imaginary part of each
non-real zero of Ξ_k(z)+t Φ_{k+1}(z) decreases monotonically (i.e. continuously) as t goes from 0 to 1.").

**(d) Numerical evidence.** Maple, "Digits ... typically set to 20N − 10", re-run at 20N, "no attempt has been made
to establish rigorous error bounds" (p. 3). Weak form: "Computations along these lines indicate this weaker form of
Conjecture 1 is true at least for N ≤ 10." (p. 4). Table (p. 4), verbatim:

    N   largest real zero   number of real zeros
    1    14.0454395788        1
    2    39.5324810798        7
    3    65.0320737720       15
    4   103.3679880094       32
    5   149.0026994921       53
    6   197.9575955732       79
    7   258.5304836632      113
    8   327.3794646017      155
    9   406.8174206801      207
   10   489.3900649445      263

Appendix (pp. 16–17): Ξ_1 zeros in [0,100]×[−0.1,500] (1 real + 18 non-real, first differences of imaginary parts
listed, all positive); Ξ_2 zeros in [0,102]×[−0.1,100]: 7 real ("14.1347251016...", "21.0220425550...",
"25.0108186655...", "30.4267684045...", "32.9244008910...", "37.8603410698...", "39.5324810797..."), then non-real from
"43.1389080680988950956236929709951507 + 3.28097100306881350163884998294539870 I" up to "100.087228624602886284768301012877784
+ 32.4941324878154139135000560357642324 I" (15 non-real, imaginary parts increasing); Ξ_3 in [0,66]×[−0.1,67]: 15 real
zeros from "14.13472514173469376946955013374227983392383419451107438" to "65.03207377198913910137679883482704065081967504834437506",
no non-real zero listed. Computation limits (p. 12): the direct Maple root finder "failed however to compute the zeros
of Ξ_2(z), as the program never finished even after running for over two days"; Ξ_2 was reached by continuation in
Ξ_1 + tΦ_2; for Ξ_3 continuation "worked well until t became very close to 1, about t = .99, at which point Newton's
method no longer converged." Heights: no zero of any Ξ_N above Re z ≈ 102 is listed; the table's heights are those of
the largest real zero. Side observation: the largest real zero of Ξ_N is close to 4(N+1)² (16, 36, 64, 100, 144, 196,
256, 324, 400, 484 vs the table) — this pattern is ours, not stated by Haglund.

## 3. Related theorems (task 3)

### 3(b) H. Ki — Chowla–Selberg constant term, and truncations of the Chowla–Selberg formula
**Ki, "Zeros of the constant term in the Chowla–Selberg formula", Acta Arith. 124 (2006) 197–204,
DOI 10.4064/aa124-3-1** (IMPAN open copy on disk: `ki-AA-124-2006-chowla-selberg.pdf/.txt`). Setting (p. 197):
C(z; s) = ζ(2s)y^s + √π (Γ(s − 1/2)/Γ(s)) ζ(2s − 1)y^{1−s}, the constant term of E_0(z; s), z = x + iy.
PROVED: "Theorem. For any y ≥ 1 all complex zeros of C(z; s) are simple and lie on Re(s) = 1/2." (p. 198). Prior
art it records (p. 198): "Hejhal [5, Proposition 5.3] used the Maass–Selberg formula to prove that, for any y ≥ 1,
all complex zeros of C(z; s) are on Re(s) = 1/2" ([5] = Hejhal, J. Anal. Math. 55 (1990) 59–95). Method (p. 198):
"we apply a variant of Hermite–Biehler theorem"; in z-form (p. 199) "F(z) = (z + i/2)Ξ(2z − i/2)Y^{iz} +
(z − i/2)Ξ(2z + i/2)Y^{−iz}", with f(s) = (s − 1)ξ(2s)Y^s + sξ(2 − 2s)Y^{1−s} (p. 198). For 0 < Y < 1 (Remark,
p. 203): "on Re(s) = 1/2 the assertion of our theorem may not be valid. But it is known (see [6, Theorem 2]) that
for any δ > 0 all but finitely many zeros of f(s) in {s : |Re(s) − 1/2| < δ} are simple and lie on Re(s) = 1/2."
**Secondary statement of Ki's Proc. LMS theorem (read here, p. 198, verbatim):** "It should be noted that the author
[6, Corollary 1] has shown that for any y ≥ 1 and any N = 1, 2, 3, . . ., all but finitely many complex zeros of any
N th partial sum in the Chowla–Selberg formula are simple and on Re(s) = 1/2. Since E_0(i; s) = 2ζ(s)L(s, χ_{−4}),
the Riemann hypothesis would follow if, for infinitely many N, one was somehow able to remove the "but finitely
many" clause in this corollary in the (very special) case where z = i."

**Ki, "All but finitely many non-trivial zeros of the approximations of the Epstein zeta function are simple and on
the critical line", Proc. London Math. Soc. (3) 90 (2005) 321–344, DOI 10.1112/S0024611504015060; corrigendum
Proc. LMS 94 (2007) 543–544, DOI 10.1112/plms/pdl019.** Paywalled; primary text not read. Statements available on
disk only through Ki's own later papers: the Acta Arith. quote above, and **Ki, "On the nontrivial zeros of modified
Epstein zeta functions", C. R. Acad. Sci. Paris Ser. I 342 (2006) 79–81, DOI 10.1016/j.crma.2005.11.015** (Numdam
copy: `ki-CRAS-342-2006-modified-epstein.pdf/.txt`; page renders `img/ki-cras-p-2.png`, `-3.png`), p. 80: "In [2],
the author investigated the distribution of zeros of truncations of the Epstein zeta function using the
Chowla–Selberg formula. In particular, the author showed that for any positive integer N, all but finitely many
nontrivial zeros of [the Chowla–Selberg formula with the Bessel sum cut at n ≤ N] are simple and on the line
Re(s) = 1/2 if √Δ/(2a) ⩾ 1." (Q = au² + buv + cv², Δ = 4ac − b².) The C. R. note itself PROVES (p. 81): "Theorem 1.1.
Let δ > 0. Then all but finitely many zeros of Z(s; y, α, β, L_1, . . . , L_n) in {s ∈ ℂ: |Re(s) − 1/2| < δ} are simple
and on Re(s) = 1/2." and "Corollary 1.2. All but finitely many nontrivial zeros of Z(s; y, α, β, L_1, . . . , L_n) are
simple and on Re(s) = 1/2, provided that y ⩾ 1.", where Z = α(s)ζ(2s) + α(1−s)√π(Γ(s−1/2)/Γ(s))ζ(2s−1)y^{1−2s} +
y^{−s}β(s)Σ a_k L_k(s) with real polynomials α, β, deg α ≥ deg β + 1 (p. 80). The case that would matter for RH is
excluded: "Corollary 1.4 cannot say anything about the function Z_{u²+v²,1,1}(s) because α(s) = 1 and β(s) = 1 do not
satisfy assumption (ii) above." (p. 81; Z_{u²+v²} = 4ζ(s)L(s, χ_{−4})).
Relevance: the closest proved analog of our question. For truncations of the Chowla–Selberg expansion (a Bessel-K
tail, not an incomplete-gamma tail) Ki proves "all but finitely many zeros on the line", never "all zeros"; the
exceptional finite set is exactly the obstruction he names.

### 3(c) J. C. Lagarias — differenced ξ and de Branges structure
**Lagarias, "Zero spacing distributions for differenced L-functions", Acta Arith. 120 (2005) 159–184, DOI
10.4064/aa120-2-4, arXiv:math/0601653** (IMPAN copy on disk: `lagarias-AA-120-2005-differenced.pdf/.txt`).
Definitions (p. 163): "A_h(s) := ½(ξ(s + h) + ξ(s − h)), B_h(s) := −(1/2i)(ξ(s + h) − ξ(s − h))". PROVED: "Lemma 2.1.
(1) If h ≥ 1/2, then (2.3) |ξ(h + s)| > |ξ(h + 1 − s)| for ℜ(s) > 1/2. (2) Assuming the Riemann hypothesis, the
inequality (2.3) holds for each h > 0." (p. 164; proof factor by factor in the Hadamard product, pp. 164–165).
"Lemma 2.2. Let E(s) be an entire function that satisfies (2.6) |E(s)| > |E(1 − s)| when ℜ(s) > 1/2. ... Then A(s) and
B(s) have all their zeros lying on the critical line ℜ(s) = 1/2, and these zeros interlace." (p. 165; due to de
Branges). "Theorem 2.1. (1) For |h| ≥ 1/2 and any 0 ≤ θ < 2π, the entire functions A_{h,θ}(s) and B_{h,θ}(s) have all
their zeros on the critical line ℜ(s) = 1/2. These zeros are all simple zeros, and they interlace. (2) Assuming the
Riemann hypothesis, for 0 < |h| < 1/2 ... [the same]" (p. 168). De Branges form: "Lemma 6.1. (i) For h ≥ 1/2 the
function (6.6) E_h(z) := ξ(1/2 + h − iz) is a de Branges structure function, i.e. |E_h(z̄)| < |E_h(z)| when ℑ(z) > 0.
(ii) If the Riemann hypothesis holds, then for all h ≠ 0 the function E_h(z) is a de Branges structure function."
(p. 179; the bar is lost in the text layer). History (p. 162): "Xian-Jin Li informs me that the results in §2 and §5
were known to de Branges in the late 1980's"; and "Recently Haseo Ki [14] obtained results analogous to those in §2
for averagings of the meromorphic function ζ̂(s) = π^{−s/2}Γ(s/2)ζ(s) = 2ξ(s)/s(s − 1), e.g. for h ≥ 1/2 all zeros of
Ã_h(s) = ½(ζ̂(s + h) + ζ̂(s − h)) lie on the critical line." ([14] = Ki, "On a theorem of Levinson", J. Number Theory
107 (2004) 287–297.) Relevance: the unconditional Hermite–Biehler range is h ≥ 1/2 because the zero-free half-plane
ℜs > 1 is what makes ξ(s + h) an HB function; this is the standard template for "E + E^#" real-rootedness.

### 3(a) Lagarias–Suzuki — constant term of the Eisenstein series
**J. C. Lagarias, M. Suzuki, "The Riemann hypothesis for certain integrals of Eisenstein series", arXiv:math/0412039v4
(3 Nov 2005); J. Number Theory 118 (2006) 98–122** (on disk: `lagarias-suzuki-math0412039.pdf/.txt`; pages = arXiv v4).
ζ*(s) := π^{−s/2}Γ(s/2)ζ(s) (eq. (11), p. 2). PROVED: "Theorem 3. For each y ≥ 1 the constant term of the Eisenstein
series a_0(y, s) := ζ*(2s)y^s + ζ*(2 − 2s)y^{1−s} (22) is a meromorphic function that satisfies the modified Riemann
hypothesis. There is a critical value y* := 4πe^{−γ} = 7.055507+ (23) such that the following hold: (1) All zeros of
a_0(y, s) lie on the critical line for 1 ≤ y ≤ y*. (2) For y > y* there are exactly two zeros off the critical line.
These are real simple zeros ρ_y, 1 − ρ_y with 1/2 < ρ_y < 1." (p. 5). "Theorem 2. For each fixed T ≥ 1, the
meromorphic function I(T, s) = −ζ*(2s)T^{s−1}/(s − 1) + ζ*(2 − 2s)T^{−s}/s (20) has all its zeros in the critical line"
and "The hypothesis T ≥ 1 cannot be relaxed" (p. 4). For y < 1 (p. 5): "Hejhal [12, p. 89] noted that for 0 < y < 1 the
function a_0(y, s) has complex zeros off the critical line, with arbitrarily large real part." Tool (Theorem 4, p. 7,
after Pólya 1926 "Hilfssatz II", footnote p. 7): for F entire of genus ≤ 1, real, F(s) = ±F(1 − s), zeros in
|ℜ(s) − 1/2| < a, "Then for any real c ≥ a, |F(s + c)/F(s − c)| > 1 if ℜ(s) > 1/2". Relevance: the y ≥ 1 threshold
is the same phenomenon as h ≥ 1/2 in 3(c): an HB inequality needs a shift past the zero-free region.

### 3(d) P. R. Taylor (1945) — secondary statements only
**P. R. Taylor, "On the Riemann zeta function", Quart. J. Math. os-16 (1945) 1–21, DOI 10.1093/qmath/os-16.1.1**
(paywalled, not read). Two independent secondary statements on disk agree, and neither matches the task's form
"ξ(s+1/2) + ξ(s−1/2)": Lagarias–Suzuki p. 6: "In the early 1940's P. R. Taylor, a student of E. C. Titchmarsh, proved a
result similar in form to Theorem 3 for y = 1. His work was published posthumously [21]. He showed that
ζ*(s + 1/2) − ζ*(s − 1/2) has all its zeros on the critical line." Nakamura–Pańkowski, arXiv:1212.5890v4, p. 4 (on disk):
"Taylor [41] showed that ζ*(s + 1/2) − ζ*(s − 1/2), ζ*(s) := π^{−s/2}Γ(s/2)ζ(s) has all its zeros on the critical line
ℜ(s) = 1/2." So Taylor's function uses the meromorphic ζ* (not ξ) and a MINUS sign. The ξ-form A_{1/2}(s) =
½(ξ(s+½) + ξ(s−½)) is instead covered by Lagarias's Theorem 2.1 (h = 1/2), 3(c).

### 3(e) Pólya's Ξ* (1926) — secondary statements only
**G. Pólya, "Bemerkung über die Integraldarstellung der Riemannschen ξ-Funktion", Acta Math. 48 (1926) 305–317,
DOI 10.1007/BF02565336** (Springer paywall; not read). Secondary, **G. Gasper, arXiv:0801.2996v1** (on disk), p. 2:
"In a 1926 paper Pólya [18] observed that Φ(u) ∼ 8π² cosh(9u/2) e^{−2π cosh(2u)} as u → ±∞ (1.3) and ... considered the
problem of determining whether or not the entire function Ξ*(z) = 16π² ∫_0^∞ cosh(9u/2) e^{−2π cosh(2u)} cos(zu) du (1.4)
has only real zeros. ... Pólya was able to prove that Ξ*(z) has only real zeros by using ... a difference equation in z
for the modified Bessel function of the third kind", via "Ξ*(z) = 4π²[K_{iz/2−9/4}(2π) + K_{iz/2+9/4}(2π)] (1.6)" and
"Lemma. If −∞ < c < ∞ and G(z) is an entire function of genus 0 or 1 that assumes real values for real z, has only real
zeros and has at least one real zero, then the function G(z − ic) + G(z + ic) also has only real zeros." Haglund's own
account (p. 2, his eq. (4)) uses "exp(−π cosh(2t))(8π² cosh(4.5t) − 12π cosh(2.5t))" and in (5) "exp(−n²π cosh(2t))";
Gasper's e^{−2π cosh(2u)} is the form consistent with Φ's asymptotics (e^{−πe^{2u}} ~ e^{−2π cosh 2u}), so Haglund's
factor looks like a slip. Y. Shi, arXiv:1706.08868 (math.GM, a claimed RH proof; on disk) p. 3 gives both Pólya kernels
"Φ_P(t) = 4π² cosh(9t/2) exp(−2π cosh(2t))" and "Φ_P2(t) = (4π² cosh(9t/2) − 6π cosh(5t/2)) exp(−2π cosh(2t))" and says
"Pólya proved that ∫ Φ_P(t) exp(izt)dt and ∫ Φ_P2(t) exp(izt)dt have only real zeros" [secondary, low-reliability source].
