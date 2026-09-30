# read-O.md — Opus reader, seed M1b `beurling-frontier` (dual-model check, standing orders 5, 7, 11)

Reader: Opus 5.5 (independent of the orchestrator's read; not waited for). Started 2026-10-01.
Object: `NOTE.md` (50,809 bytes, read whole), charter §M1b, `SHARED.md` blocks 0–7, `verify/`, `sources/`.

**Verdict line (2026-10-01):** close **T — AGREES-WITH-CORRECTIONS**; **K** (pre-derivation's unconditional clause) —
**AGREES**, with its wording fixed (F1). Theorem A: AGREES-WITH-CORRECTIONS (F3), NEW. Cor. A′: AGREES, NEW. Theorem B:
AGREES-WITH-CORRECTIONS (F2), stands as stated, NEW. Theorem C: AGREES-WITH-CORRECTIONS (F4), NEW but a routine
consequence of Landau's non-negative-coefficient argument. Prop 3.2, Cor 2.2, Props 2.1, 2.3, 5.1: AGREE. Simulation:
AGREES-WITH-CORRECTIONS (F5); independent re-run (10⁸, 8 seeds) consistent with β₀/2 at 0.6, 0.75, 0.9. Conjecture U:
NEW, **not refuted** (11 attempts, §4); consistent with every printed discrete system; contradicts BDR's printed
conjecture only. FIX-FIRST: F1–F5 (none falsifies a theorem). MINOR: m1–m11. No stop condition met.

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

## §3. Prior-art gate (read at the page; files under `sources/` unless noted)

| source | location read | what it proves / states | its (α, β) | relation to NOTE; obeys U (α ≤ max{½, 2β})? |
|---|---|---|---|---|
| BDR, arXiv:2309.01567**v2** (26 Jun 2024; latest version per arXiv API 2026-10-01; journal ref **Trans. AMS 378 (2025) 477–501**, published text not read) | z-02 l. 84–87 (p. 2) | "One may conjecture that for all α, β with max{α, β} ≥ 1/2, there must exist a corresponding [α, β]-system. The main goal of this paper is to establish this conjecture in certain ranges" | — | NOTE's reading ✓. U contradicts it on {β < ½, α > 2β} ✓ |
| BDR Thm 1.1, 1.3 | l. 131 (p. 3); l. 183 (p. 4) | 1.1: every α ∈ [0,1), β ∈ [½,1); 1.3 (RH): [½, β] for 0 ≤ β < ½, and [α, β] for ½ < α < 2/3, 2α/(α+2) ≤ β < ½ | as stated | NOTE's region statements exact ✓; all obey U |
| BDR p. 3, footnote 4 | l. 139–141, 165 | a [1, β₀]-system "in [7, Ch. 17] ... for some β₀ ≤ 1/2"; "Most likely the value of β₀ equals 1/2, but in principle it is still possible that β₀ could be smaller." | [1, β₀ ≤ ½] | U ⟺ β₀ = ½ exactly: **a sharp test of U, undecided in print** |
| BDR Rem. 5.3(2),(3); Lemma 5.1 | l. 1366–1395; 1024–1040 | hyperbola method may be improvable; number fields: N_K = a_K x + O(x^{1−2/(n+1)}) and Ω(x^{½−1/(2n)}) (Landau, via BDR's ref. [11]); conjectured [½, ½ − 1/(2n)] | [Θ_K, β_K] | see §4 A2 |
| Diamond–Montgomery–Vorhauer, Math. Ann. 334 (2006) | p1-02 l. 183–207 (pp. 3–4) | Thm 1: for ½ < θ < 1, N_B = κx + O(x^θ), ζ_B zeros on σ = 1 − a/log t, ψ_B − x = Ω±(x e^{−2√(a log x)}). p. 4: continuous examples (Malliavin, Diamond) with (3) and a zero anywhere in (0,1); "**it may still be the case that (3) with θ < 1/2 does imply RH for discrete Beurling generalized numbers**" | [1, β ≤ θ] | the M1b question is DMV's; NOTE does not cite it (m6). Obeys U iff β ≥ ½ (undecided) |
| Diamond–Zhang, *Beurling Generalized Numbers* (AMS Surv. 213, 2016), Ch. 17 (fetched-r2/t-50) | text l. 11483–11560, 12108–12304 (pp. 195–209) | Thm 17.11: N_R = k₁x + O(x^{½}e^{c(log x)^{2/3}}), no zeros in σ > ½, π_R = li + O(x^{½}); Thm 17.14: N_B = k₂x + O(x^{½}e^{c(log x)^{2/3}}), zeros on σ = 1 − 1/log t, ψ_B − x = Ω±(x e^{−2√log x}); p. 196: "(optimality is not known for θ ≤ 1/2)"; g-primes = Bernoulli selection from a dense {v_k} | 17.11: [½, ≤½]; 17.14: [1, ≤½] | 17.11 obeys U; 17.14 = BDR's [1, β₀] (U ⟺ β₀ = ½) |
| Zhang, Math. Ann. 337 (2007) | **not on disk**; read only via DZ Ch. 17 (built on it) and BDR l. 121–123 | first unconditional well-behaved system: ψ = x + O(x^{½+ε}), N = ax + O(x^{½+ε}) | [≤½, ≤½] | obeys U. Primary text UNVERIFIED |
| Broucke–Debruyne–Vindas, arXiv:2004.11501v2 (the task's "1810.05939" is not its number) | z-01 l. 1–25 | primes π = Li + O(√x); integers N = ρx + Ω±(x e^{−c√(log x log log x)}) | [½, 1] | obeys U (α = ½); it is the mirror image, not a [1, ½] system |
| Broucke–Vindas, arXiv:2102.08478v2 | via BDR l. 125–126 | existence of [0, ½]-systems | [0, ½] | obeys U |
| Hilberdink, JNT 112 (2005) | w-18a l. 195–200 (p. 335) | Thm 1: max{α, β} ≥ ½; Cor. 2 | wall | the NOTE's quotes ✓ |
| arXiv sweeps by this reader (saved: `sources/arxiv-search-O-beurling-random.xml` (15 hits), `…-O-genprimes-random.xml` (20), `…-O-random-sieve.xml` (9)) | titles + abstracts | **nothing on Bernoulli/random thinning of the rational primes as a Beurling system**, nor on Ω-bounds for integers free of a random sparse prime set. Nearest: Aymone arXiv:2009.09240 (random ±1 multiplicative functions, fixed P(f(p) = −1) — a different object); Hawkins random sieve (math/0607196) | — | T_α's analysis not in print as far as read |

**Novelty verdicts (task 5), each "not in any source read" unless a page is given:**
- **Theorem A / Cor. A′: NEW** as statements (BDR's §5 reaches only 2α/(α+2) by the hyperbola method and flags possible
  improvement, Rem. 5.3(2)); the technique (truncated Perron + convexity of ζ on Re s = α/2 + ε under RH) is standard —
  BDR themselves run Perron for the *deleted* system N_S on Re s > α/2 (z-02 l. 1205–1208).
- **Theorem B: NEW** (single-check; no printed anti-concentration lower bound for random sparse deletions found).
- **Theorem C: NEW but elementary** — it is Landau's non-negative-coefficient argument (quoted in BDR l. 1072–1090 for
  additions) applied to the prime squares of a deleted set; I would call it a routine consequence of that argument.
- **Conjecture U: NEW** as a conjecture. It contradicts BDR's printed conjecture (l. 84–87) in the corner β < α/2, and it is
  the corrected, quantitative form of DMV's p. 4 speculation (whose literal form is false unconditionally by Prop 2.1).
- Prop 2.1 (dichotomy) answers DMV's speculation negatively and unconditionally; not stated in BDR (their l. 1090 is
  "if RH is true"); routine. Prop 5.1: not located on disk; plausibly classical (Franel-type); no novelty claimed.

## §4. Attack on Conjecture U (every discrete [α, β]-system has α ≤ max{½, 2β})

Preliminary: **a refutation needs no RH input.** If some construction gives, *under RH*, a discrete system with
α > max{½, 2β}, then U is false unconditionally (RH false ⇒ (P, N) is a [Θ, 0]-system with Θ > ½, which already violates U).
So "RH-conditional" is enough for a counterexample; this sharpens what the corner {β < α/2} search must find.
Also: U ⇒ β* = ¼ is a valid threshold (β ≤ ¼ ⇒ α ≤ ½), consistent with Cor. 2.2's cap β* ≤ 2/5.

| # | system (source) | (α, β) on the record | what U asserts there | verdict |
|---|---|---|---|---|
| A1 | (P, N) (Prop 2.1) | [Θ, 0] | Θ = ½ (RH) | undecidable on the record |
| A2 | ideal norms of a quadratic field K (BDR Rem. 5.3(3), quoting Landau) | β_K ∈ [¼, ⅓] (O(x^{1−2/(n+1)}) and Ω(x^{½−1/(2n)}), n = 2); α_K = Θ_K = sup Re ρ over zeros of ζ_K = ζ·L(·, χ_D) (α_K ≥ Θ_K by the Mellin argument of 2.1; ≤ is the classical explicit formula, UNVERIFIED at the page) | ζ_K ≠ 0 on Re s > 2β_K: **no zero of L(s, χ_D) with Re s > ⅔ for every quadratic character** (a quasi-GRH), and **GRH for ζ_K** if the conjectured β_K = ¼ holds (BDR l. 1387: conjectured O(x^{½−1/(2n)+ε})) | consistent with everything printed; undecidable. U is strictly stronger than RH. For n ≥ 3, U gives Θ_K ≤ 2β_K, informative only where β_K < ½ is proved (cubic: Müller, BDR ref. [14], exponent not read) |
| A3 | DZ Thm 17.14 = DMV + Zhang (book pp. 195–209); DMV Thm 1 | [1, β₀], β₀ ≤ ½ (17.14); [1, ≤ θ], θ ∈ (½, 1) (DMV) | β₀ = ½ exactly (resp. β ≥ ½) | undecidable in print (BDR fn. 4). **Reader's sketch, consistent with U:** the DZ g-primes are Bernoulli(p_k) selections from the grid v_k = n + ℓ/2ⁿ (17.13) with p_k = ∫_{v_{k−1}}^{v_k} f ≈ 2^{−n}/log n, so the g-primes in (x/2, x] are ≈ Poisson with mean ≍ x/log x. With no g-primes in (1, 2) (Rem. 17.12), the Theorem-B decomposition applies verbatim with α = 1: c_k = κx/v_k − 1, conditional variance ≍ x/log x ⇒ a.s. N − ρx ≠ O(x^τ) for τ < ½. With 17.14(i), **β₀ = ½ for almost every realization** — the random DMV/DZ systems sit on the line α = 2β. (Single-check sketch; see §7.) |
| A4 | BDR Thm 1.1, 1.3; Cor. A′ | β ≥ ½; 2α/(α+2) ≥ α/2; 1/(3−α) ≥ α/2 | — | consistent |
| A5 | BDV 2004.11501; DZ 17.11; Zhang's first system; Broucke–Vindas | [½, 1]; [½, ≤½]; [≤½, ≤½]; [0, ½] | nothing (α ≤ ½) | consistent |
| A6 | ζ(s)ζ(ks): add {p^k} as g-primes, k ≥ 2 | [Θ, 1/k] (N = Σ_m⌊x/m^k⌋ = ζ(k)x + ζ(1/k)x^{1/k} + smaller: the residue of ζ(s)ζ(ks)x^s/s at s = 1/k; ψ gains kψ(x^{1/k})) | Θ ≤ max(½, 2/k) | consistent under RH; ⇔ RH for k ≥ 4 |
| A7 | finite surgery on ℙ (NOTE 5.3); periodic N − cx (Hilberdink 2012) | [Θ, 0] | RH | same as A1 |
| A8 | structured deletions, integer c (Theorem C) | proved β ≥ max(α/k_c, α − ½); for c = 2, α ∈ (½, ¾): bound α/3 < α/2 | β ≥ α/2 | **the only surgery corner where a counterexample is not excluded by a theorem.** No upper-bound technique reaches it (Theorem C has no Perron companion); the writer's data at c = 2, α = 0.6 climb to α/2 (0.278 → 0.299 on [10⁷, 10¹⁰]); c = 6 runs uninformative. Undecidable; numerically consistent |
| A9 | T_α with RH-false ζ (NOTE Conj. R: β = max(α/2, Θ+α−1)) | — | — | moot: RH false already refutes U via A1 |
| A10 | continuous / weighted systems: G-template ζ = (s−ρ₀)(s−ρ̄₀)/(s(s−1)) gives N = ρx + c log x + c′ (β = 0) with α = β₀; DMV p. 4 cites Malliavin and Diamond for continuous dΠ ≥ 0 with (3) and a zero anywhere in (0,1); the weighted mean system ζ(s)/ζ(s+1−α) has β ≈ α − ½ < α/2 (NOTE data 6.2′) | [β₀, 0]; [α, ≈ α−½] | — | **U fails outside discrete systems** (as Hilberdink's wall does). U must be stated for discrete systems (it is, via the NOTE's definition); any proof of U must use discreteness (m7) |
| A11 | the virtual curve (NOTE 5.4) | not an [α, β]-system over ℝ | — | excluded |

**Outcome of §4:** no system on the record refutes U; every in-print discrete system is consistent with it; the stop
condition (an RH-false-compatible system on the record with β < α/2) is **not** met. U is a strong conjecture: it implies
RH, a quasi-GRH at level ⅔ for every quadratic field, and full GRH for quadratic fields given the Hardy-type conjecture
β_K = ¼. Its sharpest in-print test is BDR's footnote 4 (β₀ of DZ 17.14), which the Theorem-B mechanism answers β₀ = ½ a.s.
(consistent). Its only open surgery corner is A8 (integer c ≥ 2, α < ¾).

## §5. FIX-FIRST items (OLD/NEW pairs against NOTE.md as read: 50,809 bytes, md5 b32d4d57b51c5156886d3799ab4502e4)

Not applied by the reader. None of them makes a theorem false; F2 and F4 repair proofs, F1 and F5 repair verdict sentences.

**F1 — the K verdict is mis-worded (§3.2 l. 126; §7.1(2) l. 419–420).** The analyticity claim holds under RH, so it is not
"false"; Prop 3.2 shows it is equivalent (up to the coincidence clause) to a quasi-RH.
- OLD (l. 126): `So the pre-derivation's "h ... converges a.s. and is analytic for Re s > β₀/2" is **false unconditionally**: it holds iff ζ(s + 1 − β₀)`
- NEW: `So the pre-derivation's "h ... converges a.s. and is analytic for Re s > β₀/2" **cannot be asserted unconditionally** (it is true under RH): it holds iff ζ(s + 1 − β₀)`
- OLD (l. 419–420): `"h analytic for Re s > β₀/2":` / `**false unconditionally** — true for the fluctuation, false for the mean, which carries ζ's zeros shifted by β₀ − 1;`
- NEW: `"h analytic for Re s > β₀/2":` / `**not provable unconditionally** — true for the fluctuation; for the mean, which carries ζ's zeros shifted by β₀ − 1, it is equivalent to a quasi-RH (true under RH);`

**F2 — Theorem B, step (1): μ_R is not the Dirichlet convolution μ_w * μ_η (§4, l. 214–216, 221–223, 228, 239).**
Π_p(1 − w_pp^{−s})(1 − η_pp^{−s}) = Π_p(1 − ε_pp^{−s} + w_pη_pp^{−2s}): the convolution carries extra mass at p²∣n.
- OLD (l. 214): `Write ε_p = w_p + η_p: μ_R = μ_w * μ_η with μ_w(k) = Π_{p|k}(−w_p), μ_η(d) = Π_{p|d}(−η_p), hence`
- NEW: `Write ε_p = w_p + η_p: on squarefree m, μ_R(m) = Σ_{dk=m} μ_w(k)μ_η(d) (d, k coprime; not the Dirichlet convolution μ_w * μ_η, which has extra mass w_pη_p at p²), μ_w(k) = Π_{p|k}(−w_p), μ_η(d) = Π_{p|d}(−η_p), hence`
- OLD (l. 215): `E(x) = −Σ_d μ_η(d)·T(x/d),  T(y) := Σ_k μ_w(k){y/k}  (deterministic; T(y) = ρ_w y for y < 1, ρ_w := Π_p(1 − w_p/p)),`
- NEW: `E(x) = −Σ_d μ_η(d)·T_d(x/d),  T_d(y) := Σ_{(k,d)=1} μ_w(k){y/k}  (deterministic; T_d(y) = yΠ_{p∤d}(1 − w_p/p) for y < 1; T := T_1, ρ_w := Π_p(1 − w_p/p)),`
- OLD (l. 221–222): `give η_p·c_p with c_p = T(x/p) + ρ_w(x/p)(Π′ − 1) = κ·(x/p) − 1, where` / `Π′ = Π_{q∉B}(1 − η_q/q), κ = ρ_wΠ′ > 0 (because for 1 ≤ y < 2, T(y) = ρ_w y − 1, and x/(pe) < 1 for e ≥ 2);`
- NEW: `give η_p·c_p with c_p = κ_p·(x/p) − 1, where` / `κ_p = Π_{q∈B, q≠p}(1 − w_q/q)·Π_{q∉B}(1 − ε_q/q) > 0 is G-measurable (x/(pek) < 1 unless ek = 1, and (1 − w_q/q)(1 − η_q/(q − w_q)) = 1 − ε_q/q);`
- OLD (l. 223): `Z = −ρ_w xΠ′Σ_{f⊂B,|f|≥2}μ_η(f)/f, and E|Z| ≪ x·Σ_{p∈B}v_p p^{−2} ≪ x^{α−1}.`
- NEW: `Z = −xΠ_{q∉B}(1 − ε_q/q)Σ_{f⊂B,|f|≥2}(μ_η(f)/f)Π_{q∈B,q∤f}(1 − w_q/q), and (E Z²)^{1/2} ≪ x·Σ_{p∈B}v_p p^{−2} ≪ x^{α−1}.`
- OLD (l. 227–228): `As x → ∞, κ = κ_x → κ_∞ :=` / `ρ_wΠ_q(1 − η_q/q) ∈ (0, ∞) a.s.`
- NEW: `As x → ∞, κ_p → κ_∞ :=` / `ρ_P = Π_q(1 − ε_q/q) ∈ (0, ∞) a.s., uniformly in p ∈ B.`
- OLD (l. 239): `From (1), E[E(x)] = −T(x) and Var E(x) = Σ_{d>1}V(d)T(x/d)²,`
- NEW: `From (1), E[E(x)] = −T(x) and Var E(x) = Σ_{d>1}V(d)T_d(x/d)²,`

**F3 — Theorem A (i): dyadic Borel–Cantelli does not control the centered prime sum between grid points (l. 188).**
- OLD: `Bernstein plus Borel–Cantelli along x = 2^j (monotone pieces between) give O(x^{α/2+ε}) a.s.`
- NEW: `Bernstein plus Borel–Cantelli on a grid of mesh X^{1−α/2} in each dyadic block [X, 2X] (≍ X^{α/2} points, tail e^{−X^{ε}} each; between grid points Σ_p w_p log p moves by ≪ X^{α/2}log X and Σ_p ε_p log p is monotone) give O(x^{α/2+ε}) a.s.`

**F4 — Theorem C: the continuation ignores the j = 1 term; for c ∉ ℤ, s = α is itself a branch point (l. 294, 302–303).**
The statement stays true (β ≥ α ≥ α/k_c), but the proof as written is wrong for c ∉ ℤ and the bound is not the right one there.
- OLD (l. 294): `listed below, ζ_{ℙ\R} is not analytic at the real point s = α/k, and hence **β(ℙ \ R) ≥ α/k_c**. For c = 1: β ≥ α/2. For c = 2: β ≥ α/3.`
- NEW: `listed below, ζ_{ℙ\R} is not analytic at the real point s = α/k, and hence **β(ℙ \ R) ≥ α/k_c**; if c ∉ ℤ, already s = α is a branch point ((s − α)^c from j = 1) and β ≥ α. For c = 1: β ≥ α/2. For c = 2: β ≥ α/3.`
- OLD (l. 302–303): `The same continuation is reached along the real segment from s = α (where the` / `product converges) because the points α/j, 2 ≤ j < k, are regular (there (js − α)^{c/j} with c/j ∈ ℤ).`
- NEW: `For c ∈ ℤ the same continuation is reached along the real segment from the half-plane Re s > α (where the` / `product converges): the j = 1 term gives (s − α)^c, a zero of order c at s = α, and the points α/j, 2 ≤ j < k, are regular (there (js − α)^{c/j} with c/j ∈ ℤ).`

**F5 — §6.4 and §7.1(3) mis-report the window scan (l. 400–402, 426).** `verify/logs/fit_big.log` prints a fourth
window, [10⁷, 10¹⁰]: sup-slopes 0.3118 ± 0.0145 / **0.4504 ± 0.0094** / 0.4756 ± 0.0260 (α = .6/.75/.9).
- OLD (l. 401–402): `Against α/2 = 0.300 / 0.375 / 0.450: agreement within 1.6σ in every window; 1/(3 − α) = 0.417 / 0.444 / 0.476 is excluded at` / `α = 0.6, 0.75 by > 4σ in every window (6.8σ and 4.2σ in the least favorable one, [10⁶, 10¹⁰]).`
- NEW: `Against α/2 = 0.300 / 0.375 / 0.450: agreement within 1.6σ in the windows [10^k, 10¹⁰], k = 4, 5, 6; the top window [10⁷, 10¹⁰] gives 0.312 ± 0.015 / 0.450 ± 0.009 / 0.476 ± 0.026 — at α = 0.75 8σ above α/2 and within 1σ of 1/(3 − α) = 0.444. So 1/(3 − α) = 0.417 / 0.444 / 0.476 is excluded at` / `α = 0.6 in every window, and at α = 0.75 only in windows starting at ≤ 10⁶ (4.2σ in [10⁶, 10¹⁰]). The ± are seed standard errors; local two-decade slopes swing by ±0.1–0.15 (read-O §2), so the realistic systematic on these slopes is ±0.03–0.05.`
- OLD (l. 426): `0.9 — the prediction β₀/2 holds at all three; controls give 0.000 (ℙ) and 0.497 ± 0.006 (Cramér).`
- NEW: `0.9 — consistent with β₀/2 at all three on full windows (independent numpy re-run to 10⁸, 8 seeds: 0.308 ± 0.008, 0.378 ± 0.012, 0.465 ± 0.016, read-O §2); at β₀ = 0.75 the top window [10⁷, 10¹⁰] (0.450 ± 0.009) sits on Theorem A's bound, so α/2 vs 1/(3 − α) is not settled there; controls give 0.000 (ℙ) and 0.497 ± 0.006 (Cramér).`

## §6. MINOR pairs (prose and constants)

- **m1** (l. 166) OLD `≤ (k+1)2^{k(1−α/2)}` → NEW `≤ (k+1)2^{k(1−α/2)+1}` (Σ_{p∈B_k}(ε_p + w_p) ≤ 2^{k+1}).
- **m2** (l. 170) OLD `(c): |Q_R(s)| ≤ 2Σ_{p∈R} p^{−α−2δ}` → NEW `(c): |Q_R(s)| ≤ C_αΣ_{p∈R} p^{−α−2δ}, C_α = (1 − 2^{−α/2})^{−1}`.
- **m3** (l. 211, after "with no hypothesis on ζ.") add: `Here α is the thinning parameter; α(T_α) = α under RH and α(T_α) ≥ α always (3.3).`
- **m4** (l. 193–194) OLD `and |ζ_P(1 + δ + it)| ≪ 1` → NEW `and |ζ_P(1 + δ + it)| ≪ |t|^δ` (the U factor).
- **m5** (§6.1, first bullet) add: `No generalized primes are added in any run: T_α and the greedy sets are pure deletions (the pre-derivation's add/delete surgery is not simulated; by 3.2 it cannot be realized as stated).`
- **m6** (§1, new item 1.7) add: `DMV, Math. Ann. 334 (2006), p. 4 (sources/p1-02 l. 203–207): "it may still be the case that (3) with θ < 1/2 does imply RH for discrete Beurling generalized numbers" — the M1b question in print. Prop 2.1 answers it negatively and unconditionally; BDR Thm 1.3 answers it under RH.`
- **m7** (§7.2, Conjecture U) OLD `**Every Beurling [α, β]-system satisfies` → NEW `**Every discrete Beurling [α, β]-system satisfies`; add to its status: `(e) it fails for continuous systems (DMV p. 4: Malliavin, Diamond; the G-template of the brief is a continuous [β₀, 0]-system), so any proof must use discreteness, as Hilberdink's does.`
- **m8** (l. 443) OLD `it predicts β₀ = ½ for the DMV–Zhang [1, β₀]-system` → NEW `it predicts β₀ = ½ for the DMV–Zhang [1, β₀]-system (β₀ ≤ ½ is Diamond–Zhang Thm 17.14(i); the Theorem-B mechanism gives β₀ ≥ ½ a.s. for their random construction, read-O §4 A3)`.
- **m9** (§1, l. 14–15) add the journal reference: `published as Trans. Amer. Math. Soc. 378 (2025), 477–501 (arXiv metadata); page/line numbers here refer to v2`.
- **m10** (l. 357) OLD `lies 14σ (α = 0.6) and 7σ (α = 0.75) above the data` → NEW `lies 14σ (α = 0.6) and 7σ (α = 0.75) above the data in seed standard errors (≈ 3σ and 2σ with a ±0.04 systematic)`.
- **m11** (§2, Prop 2.3 l. 94) `[recalled, unverified]` stays: no copy of Ingham or MV I is on disk (reader checked `fetched*/`).

## §7. What the reader adds, and the next unit to fund

**Added by this read.**
1. Two proof repairs that keep the theorems (F2: Theorem B's coprime convolution, with κ_∞ = ρ_P; F4: Theorem C's j = 1
   term, which for c ∉ ℤ strengthens the bound to β ≥ α) and one gap fix (F3).
2. The correct form of K (F1): the pre-derivation's analyticity is *equivalent to a quasi-RH*, true under RH — not false.
3. A data correction (F5): the omitted [10⁷, 10¹⁰] window puts α = 0.75 on Theorem A's bound; an independent numpy re-run
   (different sieve, RNG, ρ tail, estimators; 8 seeds to 10⁸) reproduces α/2 on full windows at α = 0.6, 0.75, 0.9, and a
   local-slope scan shows ±0.1–0.15 swings, so finite-range slopes carry a ±0.03–0.05 systematic the NOTE does not state.
4. Prior art: DMV (2006, p. 4) posed the M1b question in print; Prop 2.1 answers it negatively and unconditionally.
   BDR is published (Trans. AMS 378 (2025)). BDV 2004.11501 is a [½, 1]-system (not [1, ½]).
5. On U: a counterexample needs only RH-conditional input; U ⇒ β* = ¼ threshold, RH, and a quasi-GRH at level ⅔ for
   every quadratic field (GRH for ζ_K if β_K = ¼); U is false for continuous systems (a discreteness statement);
   **the sharpest in-print test (BDR fn. 4: β₀ of Diamond–Zhang Thm 17.14) is answered β₀ = ½ a.s. by the Theorem-B
   mechanism at α = 1** (sketch: Poisson-thin g-primes in (x/2, x] from the grid v_k = n + ℓ/2ⁿ, conditional variance
   ≍ x/log x) — consistent with U, and it settles BDR's "most likely ½" for almost every realization of their construction.

**Next unit I would fund (standing order 10: a construct-or-refute unit).** *"The square-root law for sifted sets"*:
prove, for every set R of primes with Σ_{p∈R}1/p < ∞ and π_R(x) = x^{α_R+o(1)}, the mean-square lower bound
(1/X)∫_X^{2X}(N_{ℙ∖R}(x) − ρx)²dx ≫ X^{α_R−ε} — or refute it by a structured R (the integer-c corner A8, α < ¾, where
Theorem C permits α/3). Why this unit: (i) it is exactly Conjecture O in mean square, i.e. the surgery part of U — the
only part of U not RH-hard (U itself implies RH, so no full proof is fundable); (ii) a refutation would refute U outright
(an RH-conditional corner example suffices, §4 preamble) and would confirm BDR's printed conjecture in the corner β < α/2;
(iii) the tool is concrete: E = −Σ_m μ_R(m)ψ(x/m) with the Franel/GCD kernel (m, m′)²/(mm′), which is positive definite
(Σ_d J₂(d)(·)², Prop 5.1's computation) — a pair (m, m′) whose period lcm(m, m′) is ≤ X averages over [X, 2X] to the
Franel value up to a relative O(lcm(m, m′)/X), so the open analytic step is the pairs with lcm(m, m′) > X (the
near-diagonal Fourier terms |hm′ − h′m| < mm′/X). Companion items, each small: (a) write out the A3 sketch
(DZ 17.14 has β₀ = ½ a.s.) as a lemma; (b) compute side-task: 8 more seeds of `verify/thin` at X = 10¹⁰, α = 0.75, to decide
whether the [10⁷, 10¹⁰] excess (0.450 ± 0.009 on 4 seeds) is a small-sample fluctuation; (c) G1 by Montgomery–Vaughan-type
methods for ζ(s)/ζ(s+1−α) under RH (the squarefree-problem analogue), which would lower Theorem A's 1/(3 − α).
