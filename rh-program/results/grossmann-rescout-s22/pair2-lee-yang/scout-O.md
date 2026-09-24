# PAIR 2 — W1-26 lee-yang-stat-mech — scout O (Opus 5), blind — the (R-b) rung by computation at genus ≤ 2

**Written 2026-09-24, from 17:33 IST (machine clock), in chunks as sections finished.** Operating note: `pair2-lee-yang/LAUNCH-NOTE.md`. Contract: `SCOUT-BRIEF.md` lines 5–6 and 13–16; `PRICING.md` §0 (lines 11–22), §2 (lines 96–162), §4(i) (line 249), §4(iii)–(v) (lines 259–283). Blind: I did not open `scout-F.md`, the folder `F/`, any block of `SHARED.md` other than my own, or any `adjudication.md`. Every script and log is under `pair2-lee-yang/O/`. Nothing committed. Paths below are relative to `results/grossmann-rescout-s22/` unless they start with `results/`, `fetched`, or `BARRIER-ZOO.md`.

(The headline — verdict, the (R-b) return, the close — is §9; the sections before it are the record it rests on.)

---

## §1 What was read, and in what order

1. `pair2-lee-yang/LAUNCH-NOTE.md` lines 1–18 (the rung, blindness, the digest additions 1–4, the deliverable schema).
2. `SCOUT-BRIEF.md` lines 5–6 ("The refinement") and 13–16 ("PAIR 2").
3. `PRICING.md` lines 11–22 (§0), 96–162 (§2 in full), 246–249 (§4(i)), 259–283 (§4(iii)–(v)), and the record-correction block at the end of the file (lines 176–177, which is PAIR 1's; read, not used).
4. Newman 1974 (`fetched-r2/r-06a-newman-1974-zeros-partition-function-generalized-ising-cpa27.pdf`): text layer `verify/newman1974-text.txt` lines 1–128, 131–440, 560–700; journal pages 146–149 read BY VISION (rendered to `pair2-lee-yang/O/pages/p-04.png` … `p-07.png` with `pdftoppm -r 110`), because the text layer garbles the class symbols.
5. Newman 1976 text `verify/newman1976-text.txt` lines 119–124, 178–199.
6. `verify/dobner2021-text.txt` lines 309–329.
7. `verify/genus2_signed_kernel.log` lines 1–5 and 585–619, and `verify/genus2_signed_kernel.py` lines 78–100 — as a record, to check what its counts count (§4.1). My own derivation and enumeration do not import it.
8. `BARRIER-ZOO.md` entries I.1 (lines 45–52), I.5 (78–84), III.6 (203–209), III.15 (278–284), III.16 (288–294), III.20 (325–331), IV.1 (346–352), IV.9 (415–421), IV.18 (485–491), IV.19 (518–524), V.4 (551–556), V.5 (558–566) — STATEMENT / KILLS / EXECUTABLE TEST / STATUS bullets.
9. `results/grossmann-sweep.json` `reports[26]` (all eleven fields, extracted with Python's `json` module).
10. `results/c2-followups/insights-digest.md` §D(ii) (lines 200–207).

No web access was used (§8 `verified_online` is empty). Nothing was installed.

---

## §2 The Newman-1974 read (part of the rung's slot, PRICING line 130)

### 2.1 What the page says (symbols read by vision)

- **Ising system** (p. 146, `pages/p-04.png`; text line 149): a pair (N, ρ^N) with ρ^N(σ) = e^{𝒥(σ,σ)} Π_j ½(δ(σ_j − 1) + δ(σ_j + 1)) and 𝒥 ≥ 0 — i.e. ±1 spins, ferromagnetic pair couplings. Theorem 2.1 (p. 146): ∫ e^{z·σ} dρ^N(σ) ≠ 0 when Re z > 0 (the Lee–Yang theorem in Newman's field variable).
- **The class 𝒩** (p. 146; text lines 184–186): "the set of all even or odd **signed** measures … satisfying conditions (A) and (B)". (A) is ∫ exp{bS²} d|μ|(S) < ∞ for all b ≥ 0; (B) is that the characteristic function has only real zeros (text lines 63–67 and Remark 1.2, lines 98–104).
- **The class 𝒥** (script J; p. 147, `pages/p-05.png`; text lines 198–208 garble it as "9"): signed measures μ with E_μ(z) = ∫ e^{zS} dμ(S) = K exp{−i½π Σ n_k} ∫ exp{z(λ·σ) + i½π n·σ} dρ^N(σ) for some Ising system with **λ > 0, n_k ∈ {0, 1}, K real** (eq. (2.3)). Examples (p. 147): 2.1 (N = 1, n = 0) E = K cosh(z/a); 2.2 (N = 1, n = 1) E = K sinh(z/a); **2.3 (N = 2, λ₁ = λ₂ = 1/a, n₁ = n₂ = 1) E = ½K exp{J₁₂}(cosh(2z/a) − exp{−2J₁₂})** (eq. (2.6)).
- **The class 𝒥̄** (J-bar; p. 148, `pages/p-06.png`; text lines 268–274): measures with (A) that are limits of μ_n ∈ 𝒥 with (i) |E_{μ_n}(z)| ≤ C exp{c|z|²}, C, c independent of n, and (ii) E_{μ_n} → E_μ uniformly on compacts. Hurwitz gives 𝒥̄ ⊆ 𝒩 (p. 148, lines 276–278).
- **Theorem 2.3** (p. 148; text lines 281–282): "If μ is an even or odd signed measure satisfying (A) and (B), then μ ∈ 𝒥̄." With the preceding inclusion: **𝒥̄ = 𝒩** ("The next theorem states that in fact 𝒥̄ = 𝒩", p. 148, lines 278–279). The record's "𝒩 = 𝒟" (PRICING line 110) is this statement with 𝒟 standing for Newman's 𝒥̄.
- **Lemma 2.2** (p. 149, `pages/p-07.png`; text lines 322–326): μ₁, μ₂ ∈ 𝒥 ⟹ μ₁ ∗ μ₂ ∈ 𝒥 (disjoint union of Ising systems).
- **Lemma 2.3** (p. 149; text lines 328–335): for the zeros ±iα_j of E_μ, the measure μ_{n,a} ∈ 𝒥 with E = K[a sinh(z/a)]^m Π_{j=1}^n ½(a/α_j)²[cosh(2z/a) − (1 − 2(α_j/a)²)] — **one Example-2.3 pair per zero, its coupling set by the zero: e^{−2J_j} = 1 − 2(α_j/a)²**. The proof of Theorem 2.3 (p. 149, lines 340–407) sends a = a_n → ∞ along this family.
- **Proposition 2.4** (text lines 412–414): μ ∈ 𝒩 ⟹ exp{bS²}μ ∈ 𝒩 for b ≥ 0, and Q(S)μ ∈ 𝒩 for even/odd Q with only imaginary zeros.
- **Theorem 2.5** (text lines 427–428): 𝒩 (= 𝒥̄) has the Lee–Yang property.
- Two further items used below: **Theorem 3.1** (text lines 630–682) — for an Ising system, all multi-Taylor coefficients of x ↦ |Z_N(x + iy)|² at 0 are ≥ 0; **Remark 3.1** (lines 684–690) — its conclusions persist when each exp{−2J_kj} is replaced by any real number in [−1, 1]. **Remark 2.2** (lines 570–575) — the GHS inequality, and Griffiths' second inequality, FAIL for the Example-2.3 measure.

**Stop line (a) does not fire.** Theorem 2.3 states 𝒥̄ = 𝒩 at the page (read by vision, p. 148); the record's 𝒟 is Newman's 𝒥̄; 2(b)(iii) (PRICING line 110) stands.

### 2.2 Two record corrections this read forces (internal)

**(C1) 𝒩 contains signed measures.** PRICING 2(b)(vii) (line 118) writes "Newman's class 𝒩 — nonnegative measures — does not contain the naive kernel measure of an RH-true curve in general". The definition at p. 146 (text line 184) is "all even or odd **signed** measures … satisfying (A) and (B)". For a curve C/F_q the kernel measure μ_C = Σ_k b_k δ_{g−k} (b_k = a_k q^{−k/2}, the pricing's own convention, line 118) is even (P(z/√q) is palindromic), finite (so (A) holds), and its transform Ξ_C has only real zeros ⟺ Weil's RH for C (line 118). Hence **μ_C ∈ 𝒩 ⟺ RH for C, signed or not** — the signedness of 97 log rows (§4.1) is not an obstruction to membership in 𝒩; it is an obstruction only to the *untwisted ±1 ferromagnet with uniform fugacity* the rung asks about.

**(C2) μ_C lies in 𝒥 itself — exactly, at finite size, with the zeros as input.** By Lemma 2.2 and Examples 2.1/2.3 (p. 147): Ξ_C = Π_j (2cosh z − 2cos θ_j) in Newman's variable; each factor with cos θ_j > 0 is Example 2.3 with the twist n₁ = n₂ = 1 and e^{−2J_j} = cos θ_j; each factor with cos θ_j < 0 is the same pair untwisted (n = 0), e^{−2J_j} = −cos θ_j; cos θ_j = 0 is Example 2.1. So every RH-true class is realized in 𝒥 with 2g spins, couplings **J_j = −½ log|cos θ_j| ≥ 0**, and J_j ≥ 0 ⟺ |cos θ_j| ≤ 1 ⟺ θ_j real — a reparametrization of RH, one pair per zero. Checked numerically on all 357 of my g = 2 classes: the product reproduces P(z/√q) to 8.0·10⁻⁵¹, J_j ∈ [0, 1.6567], with 22 cos θ_j = 0 factors (a₂ = 2q) (`O/summary.log` lines 13–14). This is exactly Lemma 2.3's shape (one pair per zero, coupling = function of the zero) at a = finite: **Newman's own proof of 𝒩 ⊆ 𝒥̄ is a zeros-as-input construction.** PRICING 2(e) (line 153) says Newman's approximants "are built from the target measure, not from primes"; the page sharpens it to: built from the *zeros of the target's transform*.

### 2.3 The interface's COROLLARY, restated with Newman 1974's hypotheses in place of "tight weak limits"

`reports[26].first_interface` (extracted) reads: "COROLLARY (via Newman's closure of L under tight weak limits): Ξ ∈ LP, i.e. RH." Restated on the page:

> **COROLLARY (Newman 1974, 𝒥̄ ⊆ 𝒩, p. 148 lines 276–278).** Let μ_P ∈ 𝒥 (Ising-built, eq. (2.3): ±1 spins, 𝒥 ≥ 0, λ > 0, n_k ∈ {0,1}, K real) satisfy **(i)** |E_{μ_P}(z)| ≤ C exp{c|z|²} for all z ∈ ℂ with C, c independent of P, and **(ii)** E_{μ_P} → E_Φ uniformly on compact subsets of ℂ, where E_Φ(z) = ∫ e^{zx} Φ(x) dx. Then Φ dx ∈ 𝒩, i.e. E_Φ has only imaginary zeros, i.e. Ξ has only real zeros — RH. Conversely (Theorem 2.3, lines 281–282), **if RH holds such μ_P exist** (Lemma 2.3's pairs, one per zero of Ξ), and if RH fails none exist (Hurwitz, lines 276–278).

The implication the corollary needs is (i)+(ii); a uniform sub-Gaussian tail sup_P μ_P(|x| > R) ≤ Ce^{−cR²} (the interface's wording) gives (i) only together with a uniform total-variation bound, since |E_μ(z)| ≤ ∫ e^{|Re z||x|} d|μ| (I infer; for positive μ_P of mass 1 the tail bound gives ∫ e^{r|x|}dμ_P ≤ C′e^{c′r²}, which is (i)); weak convergence is not (ii) and is blind to zeros (PRICING line 110, 2(b)(iii)(1)). Note the λ, n_k and K freedoms of 𝒥: the interface's "finite ferromagnetic Ising systems (single-site even measures, pair couplings J_ij ≥ 0)" is narrower than 𝒥 when it drops the twists n_k — and the twists are what (C2) uses for every factor with cos θ_j > 0.

