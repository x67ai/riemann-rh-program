# PRIOR-ART — unit L-lit, stream haglund-conj4

Created: 16:10 IST 2026-10-03

## Plan (order fixed by the orchestrator: task 3, task 2, task 1, task 4)
1. Read BRIEF-L-lit.md, BRIEF-WARNINGS.md, CHARTER.md, SOURCES.md, ORCH-NOTES.md.
2. Task 3: fetch arXiv:0910.5228 v1 and the author's corrected copy on his Penn page; save under lit/, SHA-256 both;
   compare the table entry at N = 4, the 1/x^2 paragraph, and Conjecture 4 (p. 11); list every other difference found.
3. Task 2: fetch Baccaro 2026 (Zenodo 10.5281/zenodo.22059236), read whole, report claims page by page;
   mark which parts of ORCH-NOTES N1 are already in it.
4. Task 1: search for prior work on Haglund's Conjecture 4 and on zero trajectories of Xi_k + t Phi_{k+1}
   (citations of 0910.5228, MathSciNet/zbMATH, Google Scholar, arXiv full text).
5. Task 4: Im f'/f < 0 in the upper half-plane for real entire f with only real zeros (Laguerre-Polya class);
   is its consequence for the solutions of f(z) = c (real c) in print? Find the earliest printed statement.
6. NOT REACHED: every source that would not fetch, with the attempts.
Each section is appended as finished; a dated block goes to SHARED.md after each.

## §3 (task 3) — the author's web-page copy against arXiv v1 (written 16:17 IST 2026-10-03)

**Sources fetched this session** (files under `results/haglund-conj4/lit/`, git-ignored):
- **W** — J. Haglund, "Some conjectures on the zeros of approximates to the Riemann Ξ-function and incomplete gamma functions", the PDF linked as "PDF" from his publications page (https://www2.math.upenn.edu/~jhaglund/ → "Publications and Preprints" = `research.html` → `preprints/rh8.pdf`). 24 pp.; title-page date "February 9, 2011"; server Last-Modified 09 Feb 2011 17:32:20 GMT. SHA-256 `a8daaab8a5b68920aeb68c038acb8d8d35e79e6ba2143494aab074fc2f3988df` (`haglund-rh8-penn.pdf`; text `haglund-rh8-penn.txt`).
- **V** — arXiv:0910.5228v1, the only version (abs page, submission history: v1, 27 Oct 2009). 23 pp.; title-page date "October 16, 2009". SHA-256 `a28f73369e952e04341434da4cad939d92923d41c4440b663177fb466650e18c`, byte-identical to S1's PDF on disk (`haglund-0910.5228v1.pdf`).
- **J** — the journal text on disk (S2, Cent. Eur. J. Math. 9 (2011) 302–318; received 12 July 2010, accepted 1 Dec 2010), used only to say which changes predate W. SHA-256 of the markdown file `69eda4e70ec4887daf01e8870e0cd3fdf16dee63e71881c29be6b76702e7e9bd`.

**Method.** pdftotext of V and W, line diff (`lit/diff-v1-vs-penn.txt`, 108 hunks; most are extraction noise: fractions, sums, page numbers, box symbols); every hunk read, and every substantive one checked on the rendered page (`lit/img/`: V and W p. 9 top, p. 10, p. 11 top). The two formulas that differ were recomputed: `L-lit/check_task3.py`, log `L-lit/check_task3.log`.

**Differences, V → W** (page = page of V; W's page is the same unless stated; "J =" says which wording the journal has):

| # | where | V (arXiv v1) | W (web copy) | J |
|---|---|---|---|---|
| 1 | p. 1, title block | "October 16, 2009" | "February 9, 2011" | — |
| 2 | p. 4, table of Ξ_N (N ≤ 10), N = 4 | number of real zeros **32** | **31** (largest real zero 103.3679880094 unchanged) | 32 |
| 3 | p. 9, eq. (47), coefficient of z⁻⁴ | 2(b³ − 2ab² − ab + 3a²b + 3a² − a³)/(e^a z⁴) | 2((b − a)³ + 3a² − 3ab − a)/(e^a z⁴) | = V (its (15)) |
| 4 | p. 10, eq. (52) | Φ₁: −.01974938206; Φ₂: .01974934121; Φ₃: .4132639753×10⁻⁷ (each /x²) | −.0197493826339; .0197493413075; .4132639781905×10⁻⁷ | = V |
| 5 | p. 10, the 1/x² paragraph | see the wordings below | see the wordings below | = V |
| 6 | p. 10, eq. (53), upper limit of Σ c_kΦ_k | ∞ | N | = V |
| 7 | p. 11, before (54) | "requiring c1 = c2 = c3" | "requiring c1 = 1, 0 ≤ ci ≤ 1 for i > 1" ((54) itself, "c/x² + O(1/x⁴) for some c > 0", unchanged) | = V |
| 8 | p. 11 (W pp. 11–12), §6, the M-curve paragraph | "the (as yet unexplained) property"; last sentence: other computations suggest the property may hold for any real polynomial with no two zeros in the upper half-plane of equal real part | "(as yet unexplained)" and that sentence removed; a new heuristic via the Cauchy–Riemann equations, new eqs. (57)–(60); V's (57)–(60) become W's (61)–(64); every later page shifts by one (W has 24 pp.) | = W (its (18)–(20)) |
| 9 | p. 2, Hejhal paragraph; references | "Hejhal [Hej90] investigated what happens if we replace φ(t) by a 'Pólya approximate'", then a sentence on Bombieri–Hejhal [BH87] under GRH | "Hejhal [Hej90] showed that if we replace φ(t) in (2) by a 'Pólya approximate'" … 100% of zeros real "(but, for N > 1, infinitely many zeros off the line)"; the [BH87] sentence and its reference entry gone | = W |
| 10 | p. 4, lead-in of the Ξ_Δ,N table | "Below we list the number of real zeros …" | "Here is a small table of the number of real zeros …" (table values: no difference in the extracted text) | = W |
| 11 | typography | ".5" (pp. 1–2), "4.5t", "2.5t" (p. 2); "ℜ(αi+1" without ")" (p. 5); "G(x; a, b, 1, 1) = 0" (p. 11) | 1/2, (9/2)t, (5/2)t; ")" restored; "G(x; a, b) = 0" | = W for the last |
| 12 | p. 11, lead-in and Conjecture 4 | — | **identical word for word** (whitespace-normalized comparison of V l. 1005–1011 with W l. 1010–1016 of the extracted texts); both on p. 11 | Conjecture 5.1, same words except "for k high enough" (p. 310 by the running heads of S2's text) |

**Item 5, the two wordings (p. 10).** V, right after (52): "For k > 3 the coefficient of 1/x² in Φk(x) is positive." and then "Thus the coefficient of 1/x² in ΞN(x) is positive for k ≥ 3 and negative for 1 ≤ k < 3." — followed by the paragraph "It follows that tΦ1(x) + Φ2(x) …" (real zero between x = 10⁵ and 10⁶ at t = .999997907459, arriving at 39.53248 at t = 1). W keeps the "It follows …" paragraph word for word (including "travels travels") but moves it directly after (52), then adds a new paragraph: "Note that for k > 3 the coefficient of 1/x² in Φk(x) is positive." followed by the exponential decay of |Ξ(x)| along the positive real axis (the gamma factor; |ζ(.5 + ix)| = o(x)), ending: "Thus the coefficient of 1/x² in ΞN(x) approaches zero from below as N → ∞."

**Checks by this unit** (`L-lit/check_task3.py`, log beside it):
- (47): a sympy series of the left side of (47) (as printed identically in V and W) gives z⁻² coefficient 2(a − b)/e^a (both copies) and z⁻⁴ coefficient equal to **W's**, not V's.
- (52): (51) evaluated at 120 digits gives −0.019749382633875, 0.0197493413074771, 4.13263978190504×10⁻⁸ — **W's** digits; V's are wrong from the 9th, 10th and 8th significant digit. The partial sums Σ_{n≤N} (the 1/x² coefficient of Ξ_N) are negative for N = 1, …, 7 (−4.1×10⁻⁸ at N = 2, −7.0×10⁻¹⁷ at N = 3, …), as W says and as S3's Prop. tail proves (x²Ξ_N(x) → negative limit); V's "positive for N ≥ 3" is false.
- Item 2: with 31 every count in the table is odd (1, 7, 15, 31, 53, 79, 113, 155, 207, 263), in line with S3's Cor. odd; 32 was the only even entry.
- Item 7 (this unit's reading, in neither copy): under W's own item 5, c1 = 1 and 0 ≤ ci ≤ 1 give c = Σ c_k·coef_k ≤ Σ_{k≤N} coef_k < 0, so W's "(54) … for some c > 0" reads as a sign not updated (it should be c < 0); the point of the sentence (no sign change of the 1/x² coefficient, hence no real zero forced in from infinity) stands.

**Bearing on the pencil (this unit's deduction from W p. 10 and (51)).** For 0 ≤ t ≤ 1 the 1/x² coefficient of Ξ_k + tΦ_{k+1} is Σ_{n≤k} coef_n + t·coef_{k+1}, which lies between the coefficients of Ξ_k and Ξ_{k+1}, both negative: no member of the pencil has a real zero forced in from +∞ by a sign change at infinity. Haglund's example (tΦ1 + Φ2, p. 10) is the k = 1 pencil continued past t = 1: tΦ1 + Φ2 = t(Φ1 + sΦ2) with s = 1/t, so the real zero entering between 10⁵ and 10⁶ at t = .999997907459 is the k = 1 pencil at s ≈ 1.0000020925 (= coef₁/(−coef₂)), just outside the conjecture's range.

**Verdict (task 3).** W is a later state than both V and the journal: it carries every journal change (items 8–11) and seven of its own (items 1–7). The N = 4 entry is 31 in W only (32 in V and J); the 1/x² paragraph is corrected in W only; eq. (47)'s z⁻⁴ term and the constants of (52) are corrected in W only, and both corrections check. Conjecture 4 and its lead-in are unchanged in W.

## §2 (task 2) — M. L. Baccaro, Zenodo 10.5281/zenodo.22059236, read whole (opened 16:22 IST 2026-10-03)

**The file.** "Haglund's Zero-Trajectory Conjecture for the First Riemann Xi Approximant", M. L. Baccaro, 5 pp., dated "22 August 2026" on p. 1 (PDF metadata: created 25 Aug 2026, MiKTeX pdfTeX). Zenodo refused every direct download from this machine (HTTP 403, "unusual traffic", 4 attempts, `lit/zenodo-file-403-attempt.html`); the same file was taken from the GitHub repository named on the Zenodo record (`mbaccaro-dev/mathematical-proofs`, `MathematicalProofs/HaglundK1ZeroTrajectory/Manuscript/hc4_k1_zero_trajectory_theorem_baccaro_20260822.pdf`): **md5 66e55682cf8aa6ca1992d038a1ffbb17 = the md5 the Zenodo record lists for its file** (record page on disk, `results/arxiv/haglund-counterexample/lit/zenodo-22059236.md`), so it is the Zenodo PDF. SHA-256 `c915171b58973e3eba39d1107a9d0157e706228ce75e81edd16016e8eba3d27d`; `lit/baccaro-hc4-k1-20260822.pdf`, text `.txt` beside it. It cites Haglund's **journal** version [3] (CEJM 2011), not the web copy.

**Statements, at the page.**
- p. 2, (4): F(z, t) = Φ1(z) + tΦ2(z), (z, t) ∈ ℂ × [0, 1]; (5) z′(t) = −Φ2(z(t))/F_z(z(t), t) at a simple zero; (6) "descends" means Im z′(t) < 0.
- p. 2, **Theorem 2.1** (Haglund's Conjecture 4 for k = 1): (i) every zero with Re z ≥ 0 and Im z > 0 is simple and its local analytic branch satisfies (6) (one-sided at t = 0, 1); (ii) a nonreal zero branch cannot escape to infinity as t increases through a bounded subinterval of [0, 1]; (iii) at a real zero where finitely many branches meet at t = t0, every local branch, counted with full Weierstrass multiplicity, stays real for t > t0 close to t0. Evenness and conjugation give the rest of the zero multiset.
- p. 3, **Proposition 3.1** (certified first-quadrant theorem): for every t ∈ [0, 1], every zero of F(·, t) in {Re z ≥ 0, Im z > 0} is simple with Im z′(t) < 0, uniformly on the unbounded quadrant.
- p. 3, (12): Φ2(x) > 0 for real x, and F(iy, t) ≠ 0 for y > 0, 0 ≤ t ≤ 1 ("the certificate also verifies the two axis facts").
- p. 4, **Lemma 4.1** (no forward escape): a nonreal branch on [t0, T) stays in the disk of radius max{256, e^{2H/3}}, H = Im z(t0). **Lemma 4.2**: a bounded branch has a unique limit z_T with F(z_T, T) = 0, and continues analytically if z_T is nonreal. **Lemma 4.3** (right-real persistence): at a real zero of finite multiplicity m ≥ 2, the m Weierstrass roots are real for small s = t − t0 > 0.
- p. 5, proof of Theorem 2.1: (i) from Prop. 3.1, (ii) from Lemma 4.1, (iii) and global continuation from Lemmas 4.2–4.3, uniqueness of continuation of a simple real zero, the outer zero-free bound on the real axis, compactness of [0, 1].
