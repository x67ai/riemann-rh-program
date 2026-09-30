# read-O.md — Opus reader, seed M1b `beurling-frontier` (dual-model check, standing orders 5, 7, 11)

Reader: Opus 5.5 (independent of the orchestrator's read; not waited for). Started 2026-10-01.
Object: `NOTE.md` (50,809 bytes, read whole), charter §M1b, `SHARED.md` blocks 0–7, `verify/`, `sources/`.

**Verdict line:** (filled in at the close of this file — see the last section)

Status marks used below: ✓ = re-derived at the line and correct; GAP = a step that does not follow as written (FIX-FIRST
pair in §5); MINOR = prose/constant (pair in §6); UNVERIFIED = a tool or fact I could not read at the page in any source
on disk or online.

## §1. Re-derivations at the line

**1.1 Proposition 3.2 / Proposition 4.2 (the mean of a deletion carries ζ's zeros) — the K item.**
- log ζ_P = log ζ − Σ_{p∈R}p^{−s} − Q_R(s) for Re s > α (Σ_{p∈R}p^{−σ} < ∞ a.s. iff σ > α). ✓
- Σ_{p∈R}p^{−s} = Σ_p w_p p^{−s} + X(s) = P(s+1−α) + X(s), since w_p p^{−s} = p^{−(s+1−α)}. ✓
- P(w) = log ζ(w) − Σ_{k≥2}P(kw)/k (from log ζ(w) = Σ_k P(kw)/k). For Re s > α/2: Re(k(s+1−α)) > k(1−α/2) ≥ 2−α > 1
  for k ≥ 2, so that sum is absolutely convergent and bounded. ✓ Hence ζ_P = ζ(s)·ζ(s+1−α)^{−1}·U(s), U = exp(analytic). ✓
- Poles of ζ(s+1−α)^{−1} sit at s₀ = ρ−1+α. With ζ(s₀) ≠ 0 (the stated coincidence clause), U(s₀) ≠ 0 (U is an
  exponential), s₀ ≠ 1: ζ_P has a genuine pole at s₀ of order = mult(ρ). ✓ The Mellin step (N_P − ρ_P x = O(x^σ) ⇒
  ζ_P − ρ_P s/(s−1) analytic in Re s > σ) and uniqueness of continuation on the connected set {Re s > max(σ, α/2)} ∖ poles:
  ✓. So β ≥ Re ρ + α − 1 whenever Re ρ > 1 − α/2. ✓
- Converse: if ζ has no zero with Re ρ > 1 − α/2, then ζ(s+1−α)^{−1} is analytic on Re s > α/2 apart from its zero at s = α. ✓
- "E[added − removed] = dν impossible as stated": the deleted mean Σ r(p)δ_p is atomic, the Poisson additions absolutely
  continuous, dν absolutely continuous; the difference can only equal dν if r ≡ 0. ✓
- **Verdict on K: AGREES, with one FIX-FIRST (F1, §5).** The NOTE says the pre-derivation's analyticity claim is
  "false unconditionally". It is not false: it holds under RH (then 1 − β₀/2 > ½ ≥ Re ρ). What 3.2 proves is that the claim
  is *equivalent* (up to the coincidence clause) to "ζ(s) ≠ 0 for Re s > 1 − β₀/2", a quasi-RH, so it cannot be asserted
  unconditionally, and the pre-derivation's variance argument covers only the fluctuating part X. That is the correct K.
- 3.3 (zero at s = α unconditionally; α(P) ≥ α via −ζ_P′/ζ_P): ✓ (ζ(α) < 0; no real zero of ζ(s+1−α) on the path).
- 3.5 (complex-zero variant): the pure-deletion weights w_p = min(1, p^{β₀−1}(2 + 2cos(γ₀ log p))) give
  ζ(s)ζ(s+1−β₀)^{−2}ζ(s+1−β₀−iγ₀)^{−1}ζ(s+1−β₀+iγ₀)^{−1}U: ✓. (The (cos)₊ bookkeeping is a sketch, fine as labeled.)

**1.2 Lemma 4.1 (random part).** Dyadic blocks + Bernstein + nets + Borel–Cantelli: ✓ (grid count 2^{3(j+k)+3}, L = 4(j+k)log 2,
failure sum Σ2^{−(j+k)+5} < ∞; small primes cut at y₀ = j^{2/α} give j^{1−2δ/α}; large blocks give O(√j)). A simpler
route to (a) exists (a Dirichlet series converging at σ₀ converges on Re s > σ₀; Kolmogorov's three-series theorem at
rational σ₀ > α/2). Two constants off (MINOR m1, m2): |∂Y_k| ≤ (k+1)2^{k(1−α/2)+1}; |Q_R| ≤ C_α Σ_{p∈R}p^{−α−2δ} with
C_α = 1/(1 − 2^{−α/2}) rather than 2. Neither affects anything.

**1.3 Theorem B (β(T_α) ≥ α/2 a.s., unconditional).**
- (1) N_P(x) = Σ_m μ_R(m)⌊x/m⌋, ρ_P = Σ_m μ_R(m)/m, E(x) = −Σ_m μ_R(m){x/m}: ✓.
- **GAP (F2):** "μ_R = μ_w * μ_η" is false as a Dirichlet convolution: Σ(μ_w*μ_η)(n)n^{−s} = Π_p(1 − ε_p p^{−s} + w_pη_p p^{−2s})
  ≠ Π_p(1 − ε_p p^{−s}); the convolution has extra mass w_pη_p at p²∣n. On squarefree m the identity holds only with d, k
  coprime, so the correct formula is E(x) = −Σ_d μ_η(d)·T_d(x/d), T_d(y) := Σ_{(k,d)=1} μ_w(k){y/k}.
- Redone with T_d: for p ∈ B = ℙ∩(x/2, x], d = pe (e B-free), x/(pek) < 1 unless ek = 1, so
  c_p = Σ_e μ_η(e)[(x/pe)Π_{q∤pe}(1 − w_q/q) − 1_{e=1}] = κ_p·(x/p) − 1, **κ_p = Π_{q∈B, q≠p}(1 − w_q/q)·Π_{q∉B}(1 − ε_q/q)**
  (using (1 − w_q/q)(1 − η_q/(q − w_q)) = 1 − ε_q/q). κ_p is G-measurable, positive, and κ_p → ρ_P a.s. (not ρ_wΠ(1 − η_q/q)).
  Z (≥ 2 B-primes) keeps E[Z²] ≪ x²(Σ_{p∈B}v_p/p²)² ≪ x^{2α−2}. So the structure c_p = κx/p − 1 survives and the rest of
  the proof goes through with κ_∞ = ρ_P. ✓ after F2.
- (3) Anti-concentration: σ_B² ≥ c·min(κ,1)²x^α/log x (fraction ≤ 4θ/κ + o(1) of B has |κx/p − 1| < θ; this uses the PNT
  for intervals of length ≍ x only) ✓; Esseen's non-i.i.d. Berry–Esseen with E|η_pc_p|³ ≤ max|c|·v_pc_p² ✓; P(|Z| > x^{α/3})
  ≤ x^{α−1−α/3} → 0 ✓.
- (2) 0–1 law: E′(x) = E(x) − E(x/q), E(x) = Σ_j E′(x/q^j) ✓ (for τ > 0). Not even needed: the bound in (3) can be made
  ≤ δ for any δ > 0 (shrink η₀, λ₀), which already gives probability 0.
- **Answer to the brief's question:** the mechanism is the conditional variance of the degree-1 chaos of the top dyadic
  block of primes (x/2, x] (each deleted prime there moves N_P by the sawtooth κx/p − 1); the per-x statement is *in
  probability* (P(|E(x)| ≤ λx^{α/2}(log x)^{−1/2}) ≤ ½ for large x), and it upgrades to an **almost-sure** Ω-statement
  "E ≠ O(x^τ) for every τ < α/2". It is not an a.s. Ω(x^{α/2}(log x)^{−1/2}) with a constant, nor a mean-square statement.
- **Theorem B stands as stated** (the stop condition "a FIX-FIRST that makes Theorem B false" is NOT met).

**1.4 Theorem A (RH ⇒ a.s. α/2 ≤ β(T_α) ≤ 1/(3−α)).**
- (i) primes: mean Σ_{p≤x}p^{α−1}log p = ∫u^{α−1}dθ = x^α/α + O(x^{α−½+ε}) ✓ (partial summation from θ(u) = u + O(u^{½+ε}));
  prime powers O(√x log x) ✓; so ψ_P = x − x^α/α + O(x^{½+ε}) and α(P) = α exactly ✓.
  **GAP (F3):** "Bernstein plus Borel–Cantelli along x = 2^j (monotone pieces between)" does not control the centered sum
  between dyadic points: the two monotone pieces Σε_p log p and Σw_p log p each grow by ≍ 2^{jα} on [2^j, 2^{j+1}], far more
  than 2^{jα/2}. Fix: a grid of mesh x^{1−α/2} (≍ x^{α/2} points per dyadic block; Bernstein tail e^{−x^{ε}} per point,
  summable), between grid points the mean piece moves by ≪ x^{α/2}log x. Conclusion unchanged.
- (ii) integers: truncated Perron with κ = 1 + 1/log x, |a_n| ≤ 1: error O(x log x/T + 1) ✓. Rectangle [c′, κ]×[−T, T],
  c′ = α/2 + δ: under RH the only singularity is s = 1 with residue ρ_P x (poles ρ−1+α have real part α−½ < c′) ✓.
  On Re s = c′: |χ(c′+it)| ≍ |t|^{½−c′}, 1 − c′ > ½ so |ζ(1−c′−it)| ≪ |t|^δ (RH), Re(s+1−α) = 1 − α/2 + δ > ½ so
  |ζ(s+1−α)^{−1}| ≪ |t|^δ (RH), |U| ≪ |t|^δ (Lemma 4.1(b)) ✓. Vertical integral ≪ x^{c′}T^{½−c′+3δ} ✓; horizontals by
  Phragmén–Lindelöf (finite order holds: all three factors are polynomially bounded on the strip) ✓.
  T = x^{(1−c′)/(3/2−c′)} ⇒ error x^{1/(3−2c′)} → x^{1/(3−α)} ✓ (checked: x/T = x^{(1/2)/(3/2−c′)}).
- Textbook tools (task 1 asks that each be named and its hypotheses checked). None of the books is on disk
  (`fetched*/` holds Montgomery–Vaughan vol. II only, and the Diamond–Zhang book, whose Perron lemma 17.9 is the untruncated
  limit form). So all are **UNVERIFIED at the page**, standard, hypotheses checked here:
  truncated Perron = MV I Cor. 5.3 (σ₀ > max(0, σ_a); |a_n| ≤ 1) ✓ hyp.; RH ⇒ ζ, 1/ζ ≪ |t|^ε on σ ≥ ½+ε = MV I Th. 13.18,
  13.23 (**quoted secondarily** in BDR z-02 lines 1203–1205) ✓ hyp.; |χ(σ+it)| ≍ |t|^{½−σ} = Titchmarsh (4.12.3) / MV I
  Cor. 10.5 (σ bounded, |t| ≥ 1) ✓ hyp.; Phragmén–Lindelöf = Titchmarsh §5.65 (finite order in the strip) ✓ hyp.;
  Bernstein's inequality (independent, centered, |X| ≤ M) ✓ hyp.; Esseen's Berry–Esseen for non-identical summands ✓ hyp.;
  Kolmogorov's 0–1 law (events invariant under finite changes of independent coordinates are tail events) ✓ hyp.
- **Theorem A: AGREES-WITH-CORRECTIONS (F3).**

**1.5 Corollary A′.** BDR Lemma 5.1 read at the page (z-02 lines 1024–1040): hypotheses 0 ≤ γ, δ < β < 1, and
I(β) = lim_R(Σ_{n≤R,n∈N}n^{−β} − aR^{1−β}/(1−β)) = value at β of the continuation of Σ_{n∈N}n^{−s} — so I(β) = ζ_P(β) ✓.
L = ℕ^{1/β}: ⌊x^β⌋ = x^β + O(1), b = 1, δ = 0, H(1) = ζ(1/β) ✓; error x^{β/(1+β−γ)}, below x^β iff γ < β ✓.
ζ_P(β) = ζ(β)ζ(β+1−α)^{−1}U(β) ≠ 0 (both ζ values negative, U(β) = e^{real}; β > 1/(3−α) > α/2 ⟺ (α−1)(α−2) > 0) ✓.
Added primes change ψ by β^{−1}ψ(x^β) = O(x^β) ✓. Inclusion 2α/(α+2) > 1/(3−α) ⟺ (2α−1)(α−2) < 0 on (½, 2) ✓.
**AGREES** (conditional on Theorem A after F3).

**1.6 Theorem C (structured deletion).** S₁ = cP(s+1−α) + H (H analytic on Re s > θ; finitely many w_p = 1 give an entire
correction) ✓; greedy set |π_R − F| < 1 by induction ✓. At s = α/k: j > k terms analytic ✓; j < k terms analytic
because P(w) = Σμ(m)log ζ(mw)/m is analytic near real w ∈ (0,1) off w = 1/m (ζ has no zeros on (0,1), and complex
singularities ρ/m stay a bounded distance from the real axis there) ✓; j = k gives (ks−α)^{c/k} ✓; ζ(α/k) ≠ 0 ✓.
**GAP (F4):** the continuation "along the real segment from s = α" ignores the j = 1 term, which contributes (s−α)^c at
s = α itself. For c ∈ ℤ this is a zero of order c (harmless, as for T_α). For **c ∉ ℤ, s = α is already a branch point**,
the path argument fails there, and the correct (stronger) conclusion is β ≥ α. So the theorem's content is for integer
c, where k_c is as stated (c = 1 → α/2, c = 2 → α/3, c = 6 → α/4 ✓). The real point α − ½ from −½log ζ(2w) gives
(2s+1−2α)^{−c/2} ✓ (simple pole for c = 2 ✓); the path from α down to α−½ crosses only α/j with c/j ∈ ℤ when α/k_c < α−½ ✓.
BDR's own deleted set is of Theorem-C type (π_S − F within 1, z-02 lines 1117–1118; dE moves each excess to the next prime,
lines 1126–1133) ✓ — so their unpadded §5 systems have β ≥ α/2 unconditionally ✓. **Theorem C: AGREES-WITH-CORRECTIONS (F4).**

**1.7 Corollary 2.2, Propositions 2.1, 2.3, 5.1.** 2.1 dichotomy ✓. 2.2(a) ✓; (b) ✓ (inf over α ↓ ½ of 2α/(α+2) is 2/5;
the same cap from Theorem A's 1/(3−α)). 2.3 ✓, with the direction α(ℕ) ≤ Θ (ψ(x) − x ≪ x^{Θ+ε}, Ingham Th. 30 /
MV I §15) **UNVERIFIED at the page**; the direction α(ℕ) ≥ Θ is proved in 2.1 ✓. Prop 5.1 re-derived independently:
E = −Σ_{m|Q}μ(m)ψ(x/m) ✓; Franel ∫₀¹ψ(au)ψ(bu)du = (a,b)²/(12ab) (Franel 1924, UNVERIFIED at page) with (Q/m, Q/m′)²/((Q/m)(Q/m′))
= (m,m′)²/(mm′) ✓; J₂-expansion ✓; Π_{p|Q}(1 + (p+1)/(p−1)) = Π 2p/(p−1) ✓; hand check R = {2}: mean square 1/12 = ½·2/12 ✓.

## §2. Simulation audit and independent re-run

**2.1 What was counted (audit of `verify/thin.c`, `thin_aux.c`, `run_all.sh`, `run_big.sh`, `fit.py`).**
- System simulated = **pure deletion T_α** (p deleted iff hash-uniform(p, seed, α) < min(1, p^{α−1})). **No generalized primes
  are added** in any T_α or greedy run: the pre-derivation's add/delete surgery was never simulated (the NOTE replaced it by
  T_α after 3.2; T_α needs no additions since ζ(s+1−α)^{−1} already carries the zero at α). The NOTE should say so (m5).
- Integer count = exact R-free count on 1..X by a bitset sieve (clear multiples of every deleted p ≤ X). By unique
  factorization this IS the full multiplicative-semigroup count of ℙ∖R, multiplicity 1 ✓. sup|E| per bin is exact over real
  x (E+ at n, E− at n+1⁻) ✓; RMS at half-integers ✓.
- ρ = Π_{p∈R,p≤Y}(1−1/p)·exp(−E₁((1−α)log Y)). I re-computed all six printed tails with mpmath: agreement to ≤ 5·10⁻⁸
  relative ✓. ρ from the X = 10⁹ (Y = 4·10⁹) and X = 10¹⁰ (Y = 2·10¹⁰) runs agree seed by seed to ~10⁻⁷ relative ✓
  (e.g. α = .75 s1: 0.173550948508 vs 0.173550936751), so the linear-drift error δρ·x ≲ 1–4% of sup|E| at the top.
- Seeds: splitmix64 hash of (p, seed, round(10⁶α)); seeds 1–8 (10⁹) and 1–4 (10¹⁰) ✓ independent. Controls: none (ℙ),
  Cramér (β = ½ expected), mean system T(y) ✓.
- **Fit:** least-squares slope of log₁₀ M(x) (running sup over 20 bins/decade) vs log₁₀ x on [10^k, X]; the quoted ± is the
  **standard error over seeds** (a seed-to-seed spread), not a regression error and not a systematic ✓ as stated in 6.1.
- **Reporting error (F5).** `verify/logs/fit_big.log` prints four windows; the NOTE's 6.4 uses three. The omitted
  [10⁷, 10¹⁰] window at α = 0.75 gives sup-slope **0.4504 ± 0.0094** (RMS 0.495 ± 0.045): 8σ above α/2 = 0.375 and 0.7σ
  from Theorem A's 1/(3−α) = 0.444. So "agreement with α/2 within 1.6σ in every window" and "1/(3−α) excluded at α = 0.75
  by > 4σ in every window" are false as written. (At 10⁹ the [10⁷, 10⁹] window at α = 0.9 is 0.524 ± 0.030, above even the
  proved RH bound 0.476 — a finite-range artefact, which shows the seed s.e. understates the real uncertainty.)
- Local two-decade RMS slopes (`verify-O/local_O.py`, log `verify-O/logs/local_O.log`) swing by ±0.1–0.15 between
  adjacent windows in every data set (writer 10¹⁰, α = .75: 0.47, 0.50, 0.27, 0.37, 0.22, 0.46, 0.54). E also stays of one
  sign over whole decades in several seeds (e.g. α = .75 s3 on [10⁹, 10¹⁰]: max E = −727): a slowly varying component of
  size x^{α/2}, not a ρ error. Honest systematic on a 5–6-decade slope: ≈ ±0.03–0.05.

**2.2 Independent re-run (reader O).** `verify-O/thin_O.py` (numpy odd-only sieve; numpy PCG64 seeded by (seed, 10⁶α), no
hash; ρ tail by scipy quad, equal to mpmath E₁ to 15 digits; RMS at x = n + U, U uniform), driver `verify-O/run_O.sh`,
fits `verify-O/fit_O.py` → `verify-O/logs/fit_O_1e8.log`. X = 10⁸, Y = 4·10⁸, seeds 1–8, 10 bins/decade. Estimators:
RS = writer-comparable running-sup slope (mean ± s.e. over seeds); BS = slope of the seed-mean of log(per-bin sup);
RMS = same with per-bin RMS; BS/RMS errors = bootstrap over seeds (2000).

| α | window | RS | BS | RMS | α/2 | 1/(4−2α) | 1/(3−α) |
|---|---|---|---|---|---|---|---|
| 0.60 | [10⁴, 10⁸] | 0.313 ± 0.011 | 0.308 ± 0.008 | 0.309 ± 0.013 | 0.300 | 0.357 | 0.417 |
| 0.60 | [10⁶, 10⁸] | 0.284 ± 0.011 | 0.272 ± 0.007 | 0.246 ± 0.014 | | | |
| 0.75 | [10⁴, 10⁸] | 0.363 ± 0.014 | 0.378 ± 0.012 | 0.375 ± 0.019 | 0.375 | 0.400 | 0.444 |
| 0.75 | [10⁶, 10⁸] | 0.402 ± 0.031 | 0.405 ± 0.036 | 0.398 ± 0.060 | | | |
| 0.90 | [10⁴, 10⁸] | 0.456 ± 0.014 | 0.465 ± 0.016 | 0.469 ± 0.022 | 0.450 | 0.455 | 0.476 |
| 0.90 | [10⁶, 10⁸] | 0.482 ± 0.030 | 0.488 ± 0.037 | 0.511 ± 0.057 | | | |

Controls (same code): ℙ itself — sup|E| ≡ 1 on every bin (slope 0), RMS 0.5773 = 1/√3 ✓. Finite R = {2,…,13}: sup|E| ≡ 3.547
(bounded), mean square 1.02299 vs Prop 5.1's ρ·2⁶/12 = 1.022977 ✓ (an independent numerical check of Prop 5.1).
**Verdict on the simulation:** on full windows my exponents agree with β₀/2 at β₀ = 0.6 and 0.9 (and 0.75) within 1–1.3σ
of my errors, reproducing the writer's numbers by an independent route; the prediction is NOT contradicted. At β₀ = 0.6,
1/(4−2α) and 1/(3−α) are excluded (≥ 4σ with any honest systematic). At β₀ = 0.75, the top windows of both data sets drift
up toward 1/(3−α); α/2 is favored on full windows only. At β₀ = 0.9 the candidates are inseparable. AGREES-WITH-CORRECTIONS (F5).
