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

---

## §3 g = 1 — the two-spin identity re-derived blind, and the regularized rung decided for every m

### 3.1 The identity (script `O/g1_identity.py`, log `O/g1_identity.log`; sympy)
Two ±1 spins, H = −Jσ₁σ₂, fugacity z per up spin: summing the four states gives Z(z) = e^{J}(1 + z²) + 2e^{−J}z, i.e. Z/e^{J} = z² + 2e^{−2J}z + 1 (log lines 1–2). Matching 1 + cz + z², c = a₁/√q (P(T) = 1 + a₁T + qT², the pricing's convention, PRICING line 118): 2e^{−2J} = c, J = −½ log(c/2) (log line 3). The roots of z² + 2xz + 1 lie on |z| = 1 iff the discriminant 4x² − 4 ≤ 0 (log line 4); with x = e^{−2J} > 0 this is J ≥ 0, and c = 2x ∈ (0, 2] ⟺ 0 < a₁ ≤ 2√q (log line 5). So **J ≥ 0 ⟺ |a₁| ≤ 2√q ⟺ Hasse ⟺ Weil's RH for E, once the orientation makes the middle coefficient positive** — reproduced. On my 60 enumerated classes (p ∈ {2, 3, 5, 7, 11, 13}, `O/enum_curves.log` lines 1–7; every a₁ with |a₁| ≤ 2√p occurs) every a₁ ≠ 0 gives a finite J ≥ 0 in the right orientation (`O/g1_identity.log` line 66); the non-curve data (13, 8) and (5, 5) give J < 0 (lines 67–68) — the negative control fires.

**Stop line (b) does not fire**, with three precisions the record lacks: (1) PRICING line 120 says "after the flip z ↦ −z when a₁ > 0"; in the pricing's own convention (a₁ is the T-coefficient, line 118) the flip is needed when **a₁ < 0**; (2) the flip z ↦ −z replaces P(T) by P(−T), which is the Weil polynomial of the **quadratic twist** — so "realized after the flip" means "the twist is realized", not the curve (my enumeration contains both members of every twist pair: for each p the a₁-list in `O/enum_curves.log` lines 2–7 is symmetric); (3) at a₁ = 0 (6 of 60 classes; supersingular) the identity needs J = +∞ (`O/g1_identity.log` lines 8, 14, 22, …): the minimal two-spin realization exists only in the closure J ∈ [0, +∞].

### 3.2 The regularized rung at g = 1, literal orientation, every m (§5 has the lemma)
Target T_m = (1 + cz + z²)(1 + z)^m on 2 + m sites. **Realized ⟺ a₁ > −√q (c > −1), for every m ≥ 0:** sufficiency by explicit realizations (c > 0: the two-spin system, m = 0; −1 < c ≤ 0: the symmetric triangle, m = 1, Q₁ = 3x² = 1 + c, x = e^{−2J} = √((1 + c)/3) ∈ (0, 1) — J finite); necessity by the functional φ_{−1} = b₂ + b₁ = 1 + c of §5.3, which must be > 0 for every m. Computed agreement on all 60 classes: 45 realized (at m ≤ 1), 15 certified unrealizable for every m — exactly the classes with a₁ < −√q (`O/phi_certify.log` lines 1–4; `O/summary.log` line 10 "g=1: noflip realized ⟺ a1 > −sqrt(p) on all 60 classes: True"); the realizations were re-checked at 40 digits (`O/cluster_polytope_g1.log`, e.g. line 15, p = 5, a₁ = −2: n = 3, mpErr 1.4·10⁻¹⁵), and the LP certificates agree for m ≤ 38 (e.g. line 7, p = 3, a₁ = −2; line 49, p = 13, a₁ = −4). With the twist allowed, all 60 are realized (`O/summary.log` line 2).

**So at g = 1 the ferromagnet with decoupled-spin regularization is STRICTLY STRONGER than RH** (it misses the RH-true classes with −2√q ≤ a₁ < −√q, i.e. q + 1 − 2√q ≤ N₁ < q + 1 − √q), while the **minimal** realization (two spins, orientation chosen) is EQUAL to RH — a reparametrization (J = −½ log(|N₁ − q − 1|/(2√q))). Neither is a new generator: the minimal one is Hasse rewritten, the regularized one is a sufficient condition that fails on a quarter of the RH-true classes.

---

## §4 g = 2 — the enumeration (own), and what the record's counts count

### 4.1 My enumeration (`O/enum_curves.py`, log `O/enum_curves.log`, 3.0 s)
All y² = f(x), f squarefree of degree 5 or 6 over F_p, p ∈ {3, 5, 7}, leading coefficient in {1, ν} (ν a non-square — scaling f by a square gives an isomorphic curve, so both leading-coefficient classes are covered): 1 296 / 30 000 / 230 496 smooth models (log lines 8–10). N₁ over F_p and N₂ over F_{p²} (quadratic character on F_{p²} computed through the norm to F_p), a₁ = N₁ − p − 1, a₂ = (N₂ − p² − 1 + a₁²)/2. **357 distinct (p, a₁, a₂) classes (50 / 115 / 192), all satisfying Weil's RH by an exact integer test** (w-roots of w² + c₁w + c₂ − 2 real and in [−2, 2]: a₁² − 4a₂ + 8p ≥ 0, 2p + a₂ ≥ 0, (2p + a₂)² ≥ 4pa₁², a₁² ≤ 16p) (log lines 11–13).

**Check against the record's classes.** Parsing the 587 data rows of `verify/genus2_signed_kernel.log` (lines 2–588) gives **349 distinct (p, a₁, a₂)**, all contained in mine; mine adds 8 classes from non-square leading coefficients (e.g. (3, −4, 8), (5, −6, 17), (7, −8, 29)) (`O/enum_curves.log` lines 14–16).

**Record correction (C3) — "587 classes" are 587 (p, degree, a₁, a₂) rows.** `verify/genus2_signed_kernel.py` resets its `seen` set inside the degree loop (lines 82–83: `for d in [5, 6]:` / `seen = set()`), so a class found in degree 5 and degree 6 is counted twice; the log's line 588 "distinct (p,a1,a2) found: 587" is a count of rows. De-duplicated: **587 rows → 349 classes; the 97 "SIGNED" rows → 57 classes; the 77 "a₁ = 0" rows → 53 classes** (my parse of the log, run in-session; the dedup is reproducible from the log alone). The numbers "97/587" and "77/587" in PRICING lines 118, 133 and 266 (banked statement 4) and in the prepared NO close (line 133) should read **57 of 349** and **53 of 349** (or, on my enumeration, per §6).

### 4.2 What "signed" does and does not obstruct
The pricing's example p = 3, a₁ = 0, a₂ = −2 (log line 590; b = (1, 0, −2/3, 0, 1)) has all coefficients of P(z/√3)(1 + z)^m positive from m = 7 (the record's regularization, PRICING line 118). **It is nevertheless not a ferromagnet partition function for ANY m**: a₂ < 0 violates φ₀ = b₂ > 0 of §5.3. Positivity of coefficients is necessary, far from sufficient.

---

## §5 The g = 2 feasibility method — two lemmas (proved here), a search, and an LP cross-check

### 5.1 Set-up
n = 2g + m sites, x_ij = e^{−2J_ij} ∈ (0, 1] (J_ij ∈ [0, ∞), finite). Dividing by e^{ΣJ}, Z(z)/Z(0) = Σ_{S ⊆ [n]} z^{|S|} Π_{i∈S, j∉S} x_ij =: Σ_k Q_k(x) z^k, Q₀ = Q_n = 1, Q_k = Q_{n−k}. The target is T_m(z) = P(sz/√q)(1 + z)^m, s = +1 (literal) or s = −1 (the twist, §3.1); T_m(0) = 1, so "Z ∝ T_m with a positive constant" is the exact system Q_k(x) = [z^k]T_m, k = 1, …, ⌊n/2⌋ — C(n, 2) unknowns against ⌊n/2⌋ equations (PRICING line 129).

### 5.2 Lemma A (percolation / vertex representation) — proved here, elementary
Each Q_k is **multiaffine** in x (every cut product contains each x_ij at most once). Multiaffine interpolation on [0, 1]^E gives the identity
  Z(z)/Z(0) = Σ_{v ∈ {0,1}^E} w_v(x) · Π_{C cluster of v} (1 + z^{|C|}),  w_v(x) = Π_{e free in v} x_e · Π_{e locked in v} (1 − x_e),
where at a vertex v an edge is "free" (x_e = 1, J = 0) or "locked" (x_e = 0, J = ∞) and the clusters are the components of the locked edges (a locked cluster of size c contributes 1 + z^c). Equivalently: **Z/Z(0) is the expectation of Π_C(1 + z^{|C|}) under independent bond percolation with P(edge locked) = 1 − e^{−2J_e}** (check at n = 2: x(1 + z)² + (1 − x)(1 + z²) = 1 + 2xz + z²). Consequences: (i) the coefficient vector lies in the **cluster polytope** K_n := conv{coeffs of Π_{c∈λ}(1 + z^c) : λ ⊢ n}; (ii) **face lemma** — for finite J every x_e > 0, so the all-free vertex (1 + z)^n carries weight Π x_e > 0; hence any linear functional L with L ≥ 0 on all cluster vertices and L((1 + z)^n) > 0 satisfies L(Z/Z(0)) > 0. A target with L(T) ≤ 0 is the partition function of no finite ferromagnet. (Newman's Remark 3.1, text lines 684–690, extends Theorem 3.1 to x ∈ [−1, 1]; Lemma A is specific to x ∈ [0, 1], which is what separates the plain ferromagnet from the twisted class of §2.2.)

### 5.3 Lemma B (the closed-form obstruction, every m) — proved here from Lemma A
For an integer r let L_r(Z) := [z²](Z(z)(1 + z)^{−r}) (a linear functional of Q₀, Q₁, Q₂). At a cluster vertex with s singletons and d two-clusters, Z(1 + z)^{−r} = (1 + z)^{s−r} Π_{c≥2}(1 + z^c), so L_r = C(s − r, 2) + d, and C(e, 2) = e(e − 1)/2 ≥ 0 for EVERY integer e — so L_r ≥ 0 on all vertices; at the all-free vertex L_r = C(n − r, 2) > 0 unless n − r ∈ {0, 1}. At the target, with r = m + j: L_r(T_m) = [z²] P(sz/√q)(1 + z)^{−j} =
  **φ_j := b₂ − j·b₁ + j(j + 1)/2,  b₁ = s·a₁/√q, b₂ = a₂/q (g = 2); b₂ = 1 (g = 1)** — independent of m.
**THEOREM (scout O, `[novelty: single-check]`).** If φ_j ≤ 0 for some integer j with 2g − j ∉ {0, 1}, then P(sz/√q)(1 + z)^m is the partition function of no finite ±1 ferromagnet with uniform fugacity on 2g + m sites, **for every m ≥ 0**. In point counts (a₁ = N₁ − q − 1, a₂ = (N₂ − q² − 1 + a₁²)/2) the three conditions that fire on my data are j = 0: **a₂ ≤ 0**, i.e. N₂ ≤ q² + 1 − (N₁ − q − 1)², which excludes the class in BOTH orientations; j = −1: a₂/q + s·a₁/√q ≤ 0; j = −2: a₂/q + 2s·a₁/√q + 1 ≤ 0. At g = 1, j = −1 gives 1 + s·a₁/√q > 0, the exact threshold of §3.2.
Also exact and weaker: a root at z = 1 (T_m(1) = 0 while Z(1) > 0) excludes every m; it occurs for (5, 0, −10) and (7, 0, −14) (P = (1 − qT²)², in both orientations; `O/cluster_polytope_g2p5.log`, `…p7.log`), which φ₀ also excludes.

### 5.4 The search (realizations) and the LP (cross-check) — `O/cluster_polytope.py` with `O/feasibility.py`
Per class and orientation: m_pos (least m with every coefficient of T_m positive, decided exactly — each coefficient is X + Y/√q with X, Y rational, sign by an integer comparison); then, for m = m_pos … up to n = 40, an LP over the vertices of K_n with the face-lemma normalization (L((1 + z)^n) = 1), whose optimal functional is rationalized and **re-checked exactly** (integer vertex values; exact sign of L(T)); m_poly = the first m the LP cannot separate. Then bounded least squares on r_k = log Q_k(J) − log T_k, J ∈ [0, 12], 16 random starts per m, m = m_poly … m_poly + 4 while n ≤ 13; success = max|r_k| < 10⁻¹¹, followed by an independent recomputation of the coefficients at 40 digits from the found J and a root check. One process, numpy threads pinned to 1; run times 32 s (g = 1), 93 s / 145 s / 319 s (p = 3 / 5 / 7).
**Controls (zoo V.4)**, `O/controls.log` lines 1–3: the non-RH datum (13, 8) is certified outside for all m ≤ 38; the non-RH datum (p, a₁, a₂) = (5, 0, 12) (w² + 2/5 has no real root) is inside K_n but the search does not realize it (best residual 4.4·10⁻², as Lee–Yang requires); a planted 4-site ferromagnet J = (0.3, 0.1, 0.7, 0.2, 0.5, 0.4) is recovered (residual 2.2·10⁻¹⁵). The detector fires on known-false and stays silent on known-true.
**Agreement.** Lemma B, run exactly on every record (`O/phi_certify.py`, j ∈ [−80, 80]), agrees with the LP/search on 120/120 records at g = 1 and 682/682 at g = 2 — no LP certificate that Lemma B misses, no realization that Lemma B forbids (`O/phi_certify.log` lines 1, 5). Lemma B also settles 16 records the LP left open near a face (the a₂ = 0 classes, where the LP's bounded functional stops separating at m ≈ 15; one of them had been "realized" in a first run only with J ≈ 12 at the bound — rejected by the rerun with the face lemma; §8 honesty). The two realizations with Jmax > 10 — (7, −3, 15) at m = 2 and (7, 0, 14) at m = 1 — were re-solved with J ≤ 6: (7, −3, 15) at m = 2 to 3.7·10⁻¹³ (`O/probe_boundary.log` line 7); (7, 0, 14) reaches only 4.5·10⁻¹⁰ at m = 1 with J ≤ 6 but 1.0·10⁻¹⁴ at m = 2 (lines 1–2; the same for the (q, 0, 2q) polynomial at q = 5, 3, lines 3–6). Counted as realized; robustly so at m = 2.
**Upgrade to exact solutions** (`O/newton_certify.py`, log `O/newton_certify.log` lines 24–50): from each stored J, with the edges J < 10⁻⁷ set to J = 0 exactly, minimum-norm Newton on Q_k(J) = T_k at 50 digits. 469 of the 492 realized orientation-records (g = 1 and g = 2, both orientations) converge to relative residual < 10⁻⁴⁰ with displacement ≤ 6.1·10⁻⁸ and every refined free J ≥ 1.3·10⁻⁷ > 0 — an exact finite ferromagnet next to each numerical one (line 25). All 23 others are double-zero targets (a₁² − 4a₂ + 8q = 0); 10 of those have an exact realization anyway (two identical untwisted pairs, cos θ < 0, m = 0), and 13 remain numerical only (10⁻¹¹), of which 7 are literal g = 2 records: (3, −2, 7), (5, −4, 14), (5, −2, 11), (5, 0, 10), (7, −4, 18), (7, −2, 15), (7, 0, 14).

### 5.5 m_max
- For the unrealized set, **m_max = ∞**: Lemma B is a statement for every m (exactly computed; LP certificates agree independently for every m ≤ 36, n ≤ 40).
- For the realized set: every realization found needs **m ≤ 2** (129 at m = 0, 64 at m = 1, 8 at m = 2; 197 of 201 at m = m_pos) (`O/realized_stats.log` lines 1–2).
- For the 16 open records: searched in full generality to m = 6 (n = 10) for all, and to m = 12 (n = 16) for (7, −3, 14): best residual 6.6·10⁻⁴ → 2.5·10⁻⁴, decreasing slowly, not zero (`O/probe_large_n.log` lines 1–4). They are the missing datum of this rung (OPEN-NAMED inside the count; they do not move the return — §6).

---

## §6 The counts

**g = 2, my 357 RH-true classes (p ∈ {3, 5, 7}), literal target P(z/√q)(1 + z)^m, plain ±1 ferromagnet, J_ij ∈ [0, ∞), uniform fugacity** (`O/phi_certify.log` line 6; the LP/search-only tallies in `O/summary.log` lines 3–6 read 201 / 132 / 24 — Lemma B moves the 8 a₂ = 0 records the LP left open near a face into the unrealized row):

| outcome | classes | how decided |
|---|---|---|
| **realized** (finite J found, 40-digit re-check) | **201** | at m = 0 / 1 / 2: 129 / 64 / 8; **194** upgraded to exact solutions (50-digit Newton, quadratic convergence, or an exact product), **7** numerical only (10⁻¹¹) — all 7 double-zero classes (a₁² − 4a₂ + 8q = 0) where the Jacobian degenerates (`O/newton_certify.log` lines 24–50) |
| **unrealized for EVERY m** | **140** | Lemma B exactly (φ₀ = a₂/q ≤ 0: 70; φ₋₁ or φ₋₂ ≤ 0: 70); LP certificates agree for m ≤ 36 |
| open (φ_j > 0 for all j; not realized to n = 10) | 16 | the missing datum; all have c₁ = a₁/√q ≤ −1.13 and min φ at j = −2 |

**Of the 140 unrealized, every one IS realized in Newman's twisted class 𝒥 by the per-zero construction of §2.2 (C2)** — two spins per pair of zeros, couplings J_j = −½ log|cos θ_j|, i.e. **only realizable with the zeros θ_j as input** among the realizations exhibited here (`O/summary.log` lines 12–14: the twisted product reproduces all 357 to 8·10⁻⁵¹; the untwisted product exists for only 41 of 357, those with both cos θ_j < 0).

**With the twist allowed** (class or its quadratic twist): realized 287, unrealized in both orientations 70 (exactly the classes with a₂ ≤ 0), open 0 (`O/phi_certify.log` line 6).

**g = 1, 60 classes (p ≤ 13):** literal — realized 45, unrealized for every m 15 (exactly a₁ < −√q), open 0; with the twist — realized 60 (`O/phi_certify.log` line 2).

**Uniqueness / canonicity.** None of the realizations is unique: the solution set at the realizing n has dimension C(n, 2) − ⌊n/2⌋ = 4, 8 or 12 (`O/realized_stats.log` line 5); the search returns one random point of it. No canonical choice with couplings that are explicit functions of (N₁, N₂) was found or is suggested by the data; what IS explicit in (N₁, N₂) is the EXCLUSION (Lemma B).

---

## §7 The (R-b) return, the "dissolves S3" point, and the zoo gate

### 7.1 The (R-b) return: **NO** (PRICING §2(c), line 128, "NO if some RH-true class is not in the image for any m ≤ m_max")
- **Is the regularized kernel measure the total-spin distribution of a ±1 ferromagnet?** For 201 of 357 g = 2 classes yes (m ≤ 2); for **140 no, for every m** (Lemma B, exact; m_max = ∞); 16 open (§6). At g = 1: yes ⟺ a₁ > −√q, for every m (§3.2).
- **Are the couplings explicit in (N₁, N₂), canonical?** No: the realizations are points of a 4-, 8- or 12-dimensional solution set, not canonical (§6). What is explicit in the point counts is the exclusion φ_j ≤ 0 (§5.3).
- **Is coupling positivity strictly stronger than, or equal to, Weil's RH?** Both, according to the size of the system, and neither is a new generator: **equal** at minimal size (g = 1 two spins: J = −½ log(|N₁ − q − 1|/(2√q)) ≥ 0 ⟺ Hasse; any g in Newman's twisted 𝒥: J_j = −½ log|cos θ_j| ≥ 0 ⟺ θ_j real — reparametrizations, the second with the zeros as input); **strictly stronger** once adjoined decoupled spins are used without twists (Lee–Yang gives realized ⟹ RH, Theorem 2.5 line 428; Lemma B removes RH-true classes: 15/60 at g = 1, 140/357 at g = 2).
- **Why NO and not NO-by-IV.1:** realizations that do not take the zeros as input WERE found (201 classes, generic couplings); the return is carried by stop line (c) (RH-true classes outside the image for every m), not by (d). The IV.1 half is recorded as a rider: the only realization I exhibit that covers EVERY RH-true class is Newman's per-zero twisted construction.

**Refutation-shaped close (10(c)):** *A Lee–Yang realization of the de Bruijn–Newman kernel by finite ferromagnets cannot be priced above instrument, because on the function-field rung the plain ±1 ferromagnet with uniform fugacity and any number of adjoined decoupled spins provably excludes RH-true curves for every m — by the percolation functional φ_j = a₂/q − j·a₁/√q + j(j+1)/2 ≤ 0, explicit in (N₁, N₂), which removes 15 of 60 classes at g = 1 (exactly N₁ < q + 1 − √q) and 140 of 357 at g = 2 (the 70 with a₂ ≤ 0 in both twists) — while Newman 1974's twisted class 𝒥, which realizes every RH-true curve, does so only by one two-spin pair per zero with J_j = −½ log|cos θ_j| (Lemma 2.3's shape), and the existence of Ising approximants with Newman's bounds (i)–(ii) is equivalent to RH by Theorem 2.3 — so every content of the interface sits in an unspecified Euler-factor-to-coupling map into the twisted class.*

**What NO does to the grade (PRICING line 133):** the instrument grade 0.72 is restored on internal grounds; the prime-data instantiation is Untried (ii) with the missing input named — sharpened by this rung to **"a specified Euler-factor-to-coupling map into Newman's twisted class 𝒥 (n_k ∈ {0, 1}) that is not the per-zero construction"** (the plain class cannot carry it: Lemma B excludes RH-true data). Nothing pulls budget until one is written (PRICING line 283, 10(d)).

### 7.2 The "dissolves S3" point (PRICING line 137), restated with what the rung adds
Lee–Yang (Theorem 2.5, line 428) gives "every zero on the circle" and forbids an off-line pair by forbidding everything off the circle; it says nothing about multiplicity. The rung shows both halves concretely: an **on-line double** is realized (P = (1 + z²)², the classes (q, 0, 2q), cos θ₁ = cos θ₂ = 0 double — realized at m = 2 with J ≤ 0.89, `O/probe_boundary.log` lines 2, 4, 6), and an off-line pair is never realized (Theorem 2.5); the realization certifies reality of all zeros, multiplicities included, **without seeing** the multiplicity. A partial certificate with multiplicity visibility would be "on the circle AND simple, uniformly in P" — not a Lee–Yang statement (PRICING line 137, `I infer` there; nothing on the rung contradicts it). Recorded as Untried (ii), missing input "a Lee–Yang-type simplicity theorem". One addition from this rung: **non-realizability is not a detector** — the plain class fails on 140 RH-true classes, so "no realization" carries no information about an off-line zero; only "realization exists ⟹ RH" is sound.

### 7.3 Zoo gate (PRICING §2(d) re-run in my own words, plus IV.18 and IV.19, plus IV.1, V.4, V.5)

| Entry | What it returns now |
|---|---|
| **III.15** Fisher-zero wall (BARRIER-ZOO lines 280–282) | Variable MATCH on the rung: Z(z) is a polynomial in the fugacity and Ξ_C(u) is its restriction to \|z\| = 1 (PRICING line 143); Lemma B also acts in the fugacity variable. The wall does not bind this interface; what binds it is §7.1 (the plain positivity is not the RH condition). |
| **III.6** Rodgers–Tao (lines 205–207) | Condition met by any scheme with no backward claim: Proposition 2.4 (text lines 412–414) gives the forward flow exp{bS²}μ, b ≥ 0; the rung makes no claim at b < 0. Newman 1976 Theorem 3 (`verify/newman1976-text.txt` lines 180–184) is the finiteness of b₀ — the entry's own theorem on the page. |
| **I.1** DH / Epstein (lines 47–50) | Unrunnable: its EXECUTABLE TEST lists the inputs a proposal consumes, and no coupling map consumes Euler-factor data — on the rung the plain realizations consume (a₁, a₂) through a non-canonical solve, the twisted ones consume the zeros. The DH inputs are on disk for when a map exists (digest §D(ii) item 5: Λ_DH(3) = −0.3120927285, Λ_DH(4) = −1.4422319646, Λ_DH(6) = +1.9363560766, Λ_DH(12) = −0.7628774720; 26 off-line orbits to T = 900, 85.699 at δ = 0.3085; "the on-line zeros of DH must be located on the rescaled S(u) … never by an absolute-tolerance root find on Ξ_DH"). Against the M2 instance (digest §D(ii) item 2: "an S2 instrument that is S1-blind by construction, and any branch offering an S1 witness must show what input of ITS object DH violates"): this branch names no such input on the rung. |
| **I.5** random multiplicative model (lines 80–82) | Couplings must be deterministic functions of the Euler factors (Wintner); unchanged. |
| **III.16** not-PF₅ (lines 290–292) | Silent on ferromagnetic constructions. Adjacent page fact: Newman's Remark 2.2 (text lines 570–575) — GHS and Griffiths' second inequality FAIL for the twisted Example 2.3 measure; so GHS-type necessary conditions (the report's live entry "Newman's unclosed GHS gap", `reports[26].live_entry_points[2]`) test plain, not twisted, representability — and plain representability fails for RH-true curves (Lemma B). |
| **III.20** doubled-object rule (lines 327–329) | Observation, not construction: Newman's per-zero twisted realization has exactly 2g spins (one pair per conjugate pair of zeros) — the H¹ count PRICING line 148 names; but it takes the zeros as input, and the plain realizations need 2g + m sites with no doubled structure. Item 1 (the doubled object) stays unnamed over Q. |
| **IV.9** visibility pricing (lines 417–419) | Every finite approximant is real-zeroed (Theorem 2.5); a hypothetical off-line zero of ζ appears only as failure of (i)/(ii) in the limit. The threshold "at what P a zero at height T, offset δ breaks (i)" is not computable until a map is fixed (PRICING line 149). The rung adds: non-realizability has false positives (140 RH-true classes), so no finite-stage failure can be read as a detection. |
| **IV.18** Sector-I confinement (lines 487–491) | A Lee–Yang coupling-positivity certificate, if it ever yielded a zero-free point for ζ at height t and depth δ, would do so through Theorem 2.5 applied to an approximant in 𝒥 with the uniform bound (i) — a statement that the entire function E_{μ_P} has no zero off the line, **not** the value of a strip-positive linear functional (w ≥ 0, ŵ ≥ 0) of first-order explicit-formula data. **Different invariant, named: membership of the approximants in Newman's 𝒥 with the uniform exp{c\|z\|²} bound (i) — a global all-zeros property.** Rider (I infer): if a future coupling map drew its positivity from Λ(n) ≥ 0 (axiom P), IV.18's EXECUTABLE TEST must then be run on the linear content that map extracts. |
| **IV.19** Kronecker sharpness (lines 520–522) | Adds, as the digest says (§D(ii) item 4): if the IV.9 pricing is ever made through a height-uniform prime-side estimate it is returned, and the cost currency is the term count. On the rung there is no prime sum (the inputs are N₁, N₂); nothing to evaluate until a map exists. |
| **IV.1** Weil positivity in disguise (lines 348–350) | HIT for the twisted route: J_j ≥ 0 ⟺ \|cos θ_j\| ≤ 1 ⟺ RH, a reparametrization with the zeros as input (the pricing's NO-by-IV.1 shape, PRICING line 129). The plain route escapes IV.1 but is not a generator of RH (it excludes RH-true curves). |
| **V.4** negative control (lines 553–556) | Run: controls fire on two non-RH data and stay silent on a planted ferromagnet (`O/controls.log` lines 1–3; §5.4). |
| **V.5** Grossmann rule (lines 560–563) | Every verdict sentence is labeled in §8 `refinement_compliance`; none uses absence of literature. |

### 7.4 Distance from upstream (10(n))
Lemma A is the multiaffine interpolation of the Ising weights, which reads as an independent-bond percolation expansion; I recall (`[recalled, unverified]`, not load-bearing) that random-cluster representations of the Ising model are classical, so Lemma A's *identity* is likely known in some form; the cluster-polytope and face-lemma *use* of it, and Lemma B with its point-count form, have nearest on-disk object "none" (Newman 1974's Theorem 3.1 / Remark 3.1 are the nearest on-disk statements, and they hold for x ∈ [−1, 1], i.e. they do not separate the plain class from the twisted one). `[novelty: single-check]` for Lemma B and the counts; a dual-model check is owed before either leaves this file (PRICING line 134).

---

## §8 The wave-1 schema (Markdown), per `SCOUT-BRIEF.md` line 6

**branch:** lee-yang-stat-mech (W1-26).

**verdict:** **instrument** (restored on internal grounds). **confidence:** 0.78.

**fit** (0–5, internal properties only; S1/S2 stated against the M2 instance, digest §D(ii) item 2):
- **S1: 1/5** — On the rung the branch's object consumes either (a₁, a₂) through a non-canonical solve (plain class) or the zeros θ_j (twisted class, §2.2 C2), never Euler-factor data, so no input that DH violates can be named (the question digest §D(ii) item 2 puts to any S1 claimant); Dobner's S♯ theorem (PRICING line 106; `verify/dobner2021-text.txt` lines 311–329, no Euler product in the axioms) still binds the dBN/LP wing as built.
- **S2: 2/5** — "Realization exists ⟹ all zeros on the line" is sound (Theorem 2.5), so an off-line zero forbids every realization; but non-realizability fires on 140 RH-true classes (§6), so absence of a realization is no detection, and no finite stage sees a zero (IV.9) — weaker than M2's explicit-bandwidth separation (digest §D(ii) item 2).
- **S3: 2/5** — It dissolves the question (§7.2): on-line doubles are realized, off-line pairs never, multiplicity unseen; no partial certificate with multiplicity visibility exists in the branch's inventory on the rung.
- **S4: 2/5** — At minimal size the coupling positivity is RH reparametrized (Hasse at g = 1; J_j = −½ log|cos θ_j| in Newman's twisted class); with adjoined spins it is a genuine non-Weil sufficient condition, but one that EXCLUDES RH-true curves (Lemma B), so it cannot be the generator of RH for them.
- **S5: 3/5** — Survives III.6 (no backward claim; Proposition 2.4), I.5 (deterministic couplings), IV.18 (a different invariant, §7.3) and IV.19 (no prime sum on the rung); exact criticality remains its flank (`reports[26].fit.S5`).

**key_objects:**
1. Newman 1974's classes on the page: 𝒩 (even/odd **signed** measures with (A), (B); text line 184), 𝒥 (Ising-built with λ > 0, twists n_k ∈ {0, 1}, K real; eq. (2.3), p. 147 by vision), 𝒥̄ (limits with bounds (i)–(ii); lines 268–274); **Theorem 2.3: 𝒥̄ = 𝒩** (p. 148); Lemma 2.3 (per-zero pairs, p. 149).
2. The kernel measure of a curve, μ_C = Σ b_k δ_{g−k}: in 𝒩 ⟺ RH for C (signed or not), and in 𝒥 exactly, via twisted per-zero pairs (§2.2 C1–C2).
3. Lemma A (percolation/vertex representation of the plain ferromagnet; cluster polytope K_n; face lemma) and Lemma B (φ_j = a₂/q − j a₁/√q + j(j+1)/2 ≤ 0 ⟹ no plain ferromagnet for any m), §5.2–5.3, `[novelty: single-check]`.
4. The g = 1 identity J = −½ log(|N₁ − q − 1|/(2√q)) ≥ 0 ⟺ Hasse, and the regularized threshold a₁ > −√q (§3).

**prior_attacks** (as recorded in `reports[26].prior_attacks`, indices 0–13; nothing added by this scout): Newman 1976 (index 2) is the Λ = −∞ class, not the Lee–Yang class (PRICING line 108; `verify/newman1976-text.txt` lines 121–123, 180–184); Newman 1991 GHS (index 3) concerns plain Ising representability of Φ — the rung shows plain representability already fails for RH-true curves (Lemma B), while the twisted class escapes GHS (Newman's Remark 2.2, lines 570–575).

**live_entry_points:** (1) the 16 open records (§6) — decide them (a sharper necessary condition than Lemma B, or realizations at n > 16); (2) a characterization of the plain image (is it exactly {φ_j > 0 ∀ j} ∩ Lee–Yang? the 402 realized and 32 open orientation-records all satisfy φ_j > 0; the certified 264 all violate it — `O/phi_certify.log` lines 5–7); (3) the sharpened Untried (ii): a coupling map from Euler-factor data INTO the twisted class 𝒥 that is not per-zero.

**first_interface (restated for the next brief, from §2.3 and §7.1):** *For each finite P, an Ising-built μ_P ∈ 𝒥 (Newman 1974 eq. (2.3): ±1 spins, J ≥ 0, λ > 0, twists n_k ∈ {0, 1}) whose couplings are an explicit function of the Euler factors at p ∈ P and NOT of the zeros of Ξ, with |E_{μ_P}(z)| ≤ C e^{c|z|²} uniformly in P and E_{μ_P} → E_Φ uniformly on compacts; then Φ dx ∈ 𝒩 (𝒥̄ ⊆ 𝒩, p. 148), i.e. RH. Referee checks: (i) the uniform bound on the transforms, not on tails; (ii) the twisted class is necessary — on the function-field rung the untwisted class excludes RH-true curves (Lemma B); (iii) the map must not factor through the zeros (IV.1; Lemma 2.3 is the per-zero map); (iv) I.1 on the map's inputs with the DH datum of digest §D(ii) item 5.*

**access_failures:** none (every source needed was on disk; the PDF was read by vision where the text layer garbled symbols).

**verified_online:** none (no web access used).

**recalled_unverified:** (1) that random-cluster (bond-percolation) expansions of the Ising model are classical — used only in §7.4's distance line, not load-bearing; (2) the GHS inequality's content beyond what Newman's Remark 2.2 states at the page — not used; a numerical GHS monotonicity test on the g = 1 targets was run during exploration and did not separate anything, and is not cited as evidence.

---

## §9 Headline — verdict, the (R-b) return, the four stop lines, refinement_compliance

### 9.1 The verdict (these sentences are the ones `refinement_compliance` labels)
V1. The (R-b) rung returns **NO**: at g = 2, 140 of my 357 RH-true classes (p ∈ {3, 5, 7}) are outside the plain ±1-ferromagnet image for every number m of adjoined decoupled spins, by an exact linear obstruction explicit in (N₁, N₂); 201 are realized (m ≤ 2; 194 exactly, 7 double-zero classes numerically), 16 are open.
V2. At g = 1 the minimal two-spin realization reproduces J ≥ 0 ⟺ Hasse (a reparametrization), and the regularized plain ferromagnet realizes exactly the classes with a₁ > −√q, for every m, so it is strictly stronger than RH.
V3. Newman 1974's twisted class 𝒥 realizes every RH-true class exactly, but only by one two-spin pair per zero with J_j = −½ log|cos θ_j|, which takes the zeros as input.
V4. By Newman 1974 Theorem 2.3 (𝒥̄ = 𝒩), the existence of Ising approximants of Φ with bounds (i)–(ii) is equivalent to RH, so the interface's only content beyond that theorem is its unspecified coupling map, which this rung shows must land in the twisted class.
V5. Verdict: **instrument**, grade restored on internal grounds; the prime-data instantiation is Untried (ii) with the missing input "a specified Euler-factor-to-coupling map into Newman's twisted class that is not the per-zero construction".

**The (R-b) return in one line:** NO — g = 2 (357 classes, p ≤ 7): realized 201 (194 exact + 7 numerical) / unrealized for every m 140 (all realizable only in Newman's twisted 𝒥 with the zeros as input) / open 16; m_max = ∞ for the unrealized (Lemma B, every m; LP cross-check to m = 36), m ≤ 2 for the realized; g = 1 (60 classes): 45 / 15 / 0.

**Refutation-shaped close** — verbatim from §7.1.

### 9.2 The four stop lines of PRICING §4(i) (line 249)
- **(a)** Theorem 2.3 not 𝒩 = 𝒟 — **did not fire** (p. 148 by vision: 𝒥̄ = 𝒩; the record's 𝒟 is Newman's 𝒥̄; §2.1).
- **(b)** the g = 1 identity fails to reproduce J ≥ 0 ⟺ |a₁| ≤ 2√q — **did not fire** (reproduced symbolically and on 60 classes; precisions: the flip is needed for a₁ < 0, it is the quadratic twist, and a₁ = 0 needs J = +∞; §3.1).
- **(c)** some RH-true g = 2 class outside the image for every m ≤ m_max — **FIRED** (140 classes, every m; the first found in run order was p = 3, a₁ = −4, a₂ = 8, `O/cluster_polytope_g2p3.log` line 1). Return NO; I stopped the rung there — no second rung was priced or built. The remaining work in this file (counts, zoo gate, schema) is the report the stop line asks for.
- **(d)** the only realizations found take the zeros as input — **did not fire as written** (201 classes were realized with couplings that are not per-zero); recorded as the rider of §7.1: the only realization covering every RH-true class is the per-zero twisted one.

### 9.3 refinement_compliance (V.5; `SCOUT-BRIEF.md` line 6)
| Sentence | Label | Ground |
|---|---|---|
| V1 | internal | computed exclusion (Lemma B, §5.3) and computed realizations (§5.4), logs cited in §6 |
| V2 | internal | symbolic derivation and exact threshold (§3; `O/g1_identity.log`, `O/phi_certify.log` lines 1–4) |
| V3 | internal | read at the page (Newman 1974 pp. 147, 149 by vision) and computed on 357 classes (`O/summary.log` lines 13–14) |
| V4 | internal | an equivalence in print (Theorem 2.3, p. 148) — V.5's admissible "equivalence" ground |
| V5 | internal | follows from V1–V4; no sentence rests on the absence of a published connection |
No sentence of the verdict is an absence sentence; "no canonical choice … was found" (§6) is a statement about this rung's computed solution sets, not about literature.

### 9.4 Honesty note
- **Read at the page:** everything in §1. **Computed:** `O/enum_curves.py` (3 s), `O/g1_identity.py`, `O/feasibility.py` + `O/cluster_polytope.py` (runs of 32 s, 93 s, 145 s, 319 s; one process; numpy threads pinned to 1 for the final runs — an earlier p = 3 run used ~5.7 cores through BLAS for 4 min before I pinned them), `O/phi_certify.py`, `O/summary.py`, `O/realized_stats.py`, `O/newton_certify.py`, `O/probe_large_n.py` (logs beside each; `O/probe_boundary.log` is `probe_large_n.py` run at J ≤ 6). Superseded runs: the first `feasibility_g1.log` (plain search without LP) and the first p = 3 runs (J bound 40, then without the face lemma) were overwritten or left as `feasibility_g1.{log,json}`; the J-bound-40 run had "realized" (3, −1, 0)-twist and (3, 1, 0) at J ≈ 40 and ≈ 12 — both are a₂ = 0 classes that Lemma B excludes; the final runs do not realize them.
- **Exploration not kept:** before Lemma A, I mapped the 4- and 5-site images by sampling and constrained optimization, and tested GHS monotonicity numerically, in throw-away scripts outside `O/`; they motivated Lemma A (the 5-site lower boundary Q₂ = Q₁ − 1 is the cluster-polytope facet through {4,1} and {3,1,1}) and nothing in the verdict rests on them.
- **Inferred (marked "I infer" where used):** the tail-bound-to-(i) implication (§2.3); the IV.18 rider (§7.3).
- **Novelty, single-check:** Lemma B and its point-count form, and every count in §6. Dual-model check owed (PRICING line 134).
- **Files touched:** `pair2-lee-yang/scout-O.md` (this file), `pair2-lee-yang/O/*` (scripts, logs, JSON, page renders), one appended block in `pair2-lee-yang/SHARED.md`. Nothing else modified; nothing committed.
