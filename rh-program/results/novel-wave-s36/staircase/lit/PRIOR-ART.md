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
