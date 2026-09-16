# Referee report O (blind) — Theorem M2, the Gevrey-localized single-defect separation theorem with the tight-pair corollary

**Referee:** Opus 5, Job 4 of build stream `c2-m2-s22`, blind (I have not opened `check-O.md`, `verify-O/`, `hashes-O.txt`, `SHARED.md`, or any `referee-*` file).
**Date:** Wed Sep 16 19:29:48 IST 2026.
**Note refereed:** `results/c2-m2/separation-note.md`, SHA-256 `dd06d6913d51ff01a3f706c66cec4049af91053ae02dd55659982ed20313fa84` (486 lines, including the dated "Corrections after the dual check" section, which I treat as part of the record as instructed).
**Read:** the note; `results/c2-m2/verify/` (all scripts, logs, JSON); the theorem block and the Job 3/4 paragraph of `results/c2-m2/BRIEF.md`; `results/c2-m5/PRICING-next-unit.md` §0 and §2; `directions/C2-rigidity-conservation.md`; `BARRIER-ZOO.md` (II.3–II.5, V.3, V.4); `sources-extracted/tx_032.txt`; the Lean tree `~/rh-lean-work/zeta-23-lean-main` (read-only; nothing created, modified or rebuilt); `fetched-r3/r3s-24-…2608.16034v2…pdf` via `verify/sources-read-excerpts.txt`.
**Computed independently** (my own scripts, no import of the author's code, mpmath at 30–60 digits): Z; ‖B′‖₁, ‖B″‖₁, ‖B‴‖₁, ∫|v|B; b₁ and an enclosure; κ_∞, κ±; c_B, C_B, c_B′, C_B′; the whole clause-5 chain and the least R₀; the reflection condition (R′) and its least integer c_R; L₁; the L*-table; the pointwise clause-5 bound at depth ½; the reflected on-line double; an adversarial out-window configuration; and a re-run of the author's `b1_constant.py`, `edge_law_two_sided.py`, `lemma_G_constants.py`, `four_point_accounting.py` and the `#print axioms` scratch file.

---

## Verdict, in one sentence

**With its corrections section, Theorem M2 as stated in §7.1 — clauses 1–7 under the hypotheses L ≥ max(25/δ, 4δ⁻¹(log log(3+t) + 2log(1/δ) + log(2b₁C₁))) and the reflection condition (R) (implied by t ≥ 21L) — is a theorem: I re-derived clause 6's assembly from clauses 1–5 and both clause 2 and clause 5 from scratch, reproduced every constant in the chain to the digits printed, failed to break clause 5 with an adversarial depth-½ configuration saturating 𝒞(C₁), and found no FATAL; one MAJOR remains, and it is a wrong recorded constant for ζ (clause 8), not a defect in clauses 1–7.**

## Per-clause grades

| clause | grade |
|---|---|
| 1 — orbit clause, four-point accounting, reflection condition | **CLOSES** |
| 2 — two-sided edge law | **CLOSES** |
| 3 — slack | **CLOSES** |
| 4 — in-window on-line noise | **CLOSES** |
| 5 — out-window contamination, uniform over depth ≤ ½ | **CLOSES** |
| 6 — the assembly (separation) | **CLOSES** |
| 7 — tight pair | **CLOSES** |
| 8 — scope | **MAJOR** (ζ's C₁ is wrong in the body *and* in the correction; the statement of clause 8 itself is sound) |

No FATAL. The 10(d) trigger is not blocked by this report.

---

## 1. Clause 6's assembly, re-derived from clauses 1–5 — and every constant in the chain

### 1.1 The identity

I re-derived (0.1) and (0.2) independently. With f(u) = i(B_L)′(u)e^{−itu}, integration by parts with no boundary terms gives h_f(r) = i∫(B_L)′(u)e^{i(r−t)u}du = (r − t)B̂_L(r − t) = (r − t)B̂(L(r − t)) for every complex r; ĝ(z) = h_f(z)·conj(h_f(conj z)) is `EF.paperFT_weilTest` at `Zeta23/ExplicitFormula.lean` **line 189** (all complex z, hypotheses: f, g continuous with compact support — satisfied). Both check numerically (`four_point_accounting_run.log` (1), (4); my re-run reproduces them, and the (0.2) check prints `rel diff = 1.0e-9`, not the note's body value 10⁻⁶ — the corrections' §12.13(i) is right).

### 1.2 The chain, independently computed

All values mine, at 30 digits, from the definitions only:

| constant | my value | note |
|---|---|---|
| Z | 0.221996908084040 | ✔ identical |
| ‖B′‖₁ | 3.314275359 | ✔ |
| ‖B″‖₁ | 28.77264369 | ✔ |
| ‖B‴‖₁ | 642.3011259 | ✔ |
| ∫\|v\|B | 0.1672269989 | ✔ |
| b₁ = sup\|ηB̂\|² (grid) | 8.64612831 at η* = 4.67274 | ✔ |
| b₁ certified upper | 8.6980807 (author's cell-wise Lipschitz certificate, which I checked step by step and reproduced by re-running the script; my own cruder *global*-Lipschitz certificate gives only 8.8737, so the author's is the sharper and correct one) | ✔; **8.70 is a valid upper bound**, so §12.2's "state the theorem with b₁ = 8.70" is right and necessary |
| c_B = 2/√(72e) | 0.1429606475 | ✔ (D2's printed 0.14298 is a typo; §12.6 fixes it to 0.14296) |
| C_B = e²/Z | 33.28450005 | ✔ |
| c_B′ = (7/8)c_B, C_B′ = 4e^{−3/4}C_B | 0.12509057, 62.889938 | ✔ |
| κ_∞ = log(√(π/2)e^{−1/4}/Z) | 1.480883177 | ✔ |
| κ₊ = κ_∞ + 1/20 + 1/(128·125) | 1.530945677 | ✔ |
| m(25) = 12.5 − 10 − 1.5log25 + 2κ_∞ | 0.63345262 | ✔ |
| L₁ = (2ζ(4)‖B‴‖₁²/b₁)^{1/4} | 17.8993 (b₁ = 8.70); 17.9271 (b₁ = 8.64613) | ✔ 17.9 |
| R₀ (least, L₀ = 50) | **81.0**, F̃(50) = −0.133615 | ✔ (author −0.133) |
| R₀(L₀) for L₀ = 100, 200, 403, 1000, 10⁴ | 58.5, 48, 43, 40, 38 | ✔ |
| (3/(4c_B))², (7/(8c_B))², (13/(16c_B))² | 27.5226, 37.4613, 32.3008 | ✔ |
| least integer c_R in "t ≥ c_R L" | **21**, margin 0.7171 at L = 50, increasing | ✔ |
| 1/(8c_B²) | 6.11613 | ✔ |
| L*(0.1, 10⁶) | 403.497 | ✔ 403 |
| L*(0.3085172, 85.7) | 86.99 (b₁ = 8.70); 86.906 (b₁ = 8.64613) | the note prints 86.907 — see MINOR-3 |
| C₀ = 2/(1 − c₀) | 4 | ✔ |

**No constant in the chain differs from the author's beyond the b₁-bookkeeping and the ζ-density constant of clause 8.** The dependency order (Z → b₁, ‖B‴‖₁, κ_∞; Lean (18/e) → A₁ = 72/e → c_B, C_B → R₀, c_R, L₁; κ₋ → λ₀; c₀ → C₀) is acyclic, as §7.1 claims.

### 1.3 The assembly, re-derived

Write W_Z = (−2δ²c(δL)² + E₋) + N_Z + O_Z and W_{Z′} = N_{Z′} + O_{Z′}. Since N_{Z′} ≥ 0,
W_{Z′} − W_Z ≥ 2δ²c² − |E₋| − N_Z − |O_Z| − |O_{Z′}| ≥ 2δ²c²(1 − e^{−L}) − N − 2e^{−L},
with N := b₁C₁ℓ_R/L² + T₁ and clause 4 giving N ≤ 2b₁C₁ℓ_R/L² for L ≥ L₁ = 17.9 (so for every admissible L ≥ 50). The note keeps 2N, a safe over-estimate (D8); I confirm one N would do. Then clause 3 at λ = δL ≥ 25 gives c² ≥ e^{δL/2}, and the target δ²e^{δL/2} is reached exactly when

  δ²e^{δL/2}(1 − 2e^{−L}) ≥ 4b₁C₁ℓ_R/L² + 2e^{−L}.  (7.1)

I re-derived (7.1)'s proof line by line: δL/2 ≥ 2(log log(3+t) + 2log(1/δ) + log(2b₁C₁)) ⟹ δ²e^{δL/2} ≥ 4b₁²C₁²(log(3+t))²/δ² ≥ 16b₁C₁(log(3+t))²; and ℓ_R ≤ log(4+t) + log(1+R₀L) ≤ 1.1log(3+t) + L (the first step is log(a+b) ≤ log a + log(1+b) for a ≥ 1, valid with a = 4+t ≥ 7), so ℓ_R/L² ≤ 0.00044log(3+t) + 0.02 ≤ 0.02log(3+t) ≤ (log(3+t))² for t ≥ 3, L ≥ 50. Hence 4b₁C₁ℓ_R/L² is at most a quarter of the left side; the two e^{−L} terms are below 10⁻²⁰ of it at L ≥ 50. Finally δ²e^{δL/2} ≥ 1 ⟺ δL/2 ≥ 2log(1/δ), which the L-hypothesis gives with a factor 2 to spare. **The assembly is correct as written, with the margins the note claims.**

Two items on the assembly, neither affecting the conclusion — see MINOR-1 (the decomposition is not a partition when R > 2t) and MINOR-2 (the split at |Re γ − t| = R exactly).

---

## 2. Clause 2, re-derived completely (and clause 3 from it)

I re-derived the whole chain: c(λ) = e^{λ/2}I(λ)/Z with I(λ) = ∫₀¹exp(−λs − 1/(4s(1−s)))ds (substitution v = ½ − s; 1 − 4v² = 4s(1−s)); the splitting 1/(1−s) = 1 + s + s²/(1−s) giving (3.2) with μ = λ + ¼; J(μ) = μ^{−1/2}K₁(√μ) and J₂(μ) = ¼μ^{−3/2}K₃(√μ) by s = σ/√μ then σ = ½e^θ (the odd sinh parts drop). Lemma K: with cosh θ = 1 + 2y², y = sinh(θ/2), dθ = 2dy/√(1+y²),

* upper: (1+2y²)(1+y²)^{−1/2} ≤ 1 + (3/2)y² ⟺ 1 + 4y² + 4y⁴ ≤ 1 + 4y² + (21/4)y⁴ + (9/4)y⁶ ✔;
* lower: (1+y²)^{−1/2} ≥ 1 − y²/2 for y² ≤ 3 because (1−y²/2)²(1+y²) = 1 − (3/4)y⁴ + y⁶/4 ≤ 1 there, and trivially for y² > 2 ✔ (the two ranges cover ℝ₊);
* cosh 3θ = 4c³ − 3c with c = 1 + 2y² equals 1 + 18y² + 48y⁴ + 32y⁶ ✔;
* the Gaussian moments ∫₀^∞y^{2n}e^{−2xy²}dy = ½√(π/(2x))(2n−1)!!/(4x)^n give exactly the three stated bounds ✔.

Upper bound of clause 2: κ(λ) ≤ κ_∞ + (√λ − √μ) + ¾log(λ/μ) + log(1 + 3/(8√μ)) ≤ κ_∞ + 1/(4√λ) + 1/(128λ^{3/2}), using √(1+ε) ≥ 1 + ε/2 − ε²/8 — **I get κ₊ = 1.5309457 at λ = 25, the note's value.**

Lower bound: e^{−s²/(4(1−s))} ≥ 1 − s²/2 on (0,½]; ∫₀^{1/2} ≥ J(μ) − e^{−μ/2}/μ; the s²-term ≤ ½J₂(μ). I recomputed D(25) from the definitions: μ = 25.25, √μ = 5.0249378, 3/(8√μ) = 0.0746280, 3/(16μ) = 0.0074257, E₁(25) = 1.7817·10⁻⁴, E₂(25) = 0.0114410, u = 0.0555831, log(1+u) = 0.0540923, so D(25) = −0.025 − 0.0075 + 0.0540923 = **+0.0215923 > 0**, and the note's uniform chain D(λ) ≥ (0.234√λ − 0.647)/λ − 0.9625E₁(λ) ≥ (0.52 − 0.0045·0.9625)/λ > 0 for λ ≥ 25 reproduces with every printed coefficient (0.9625 from log(1+u) ≥ u(1 − u/2) at u ≤ 0.075; 0.373134 from √μ ≤ 1.005√λ; 0.28889 ≤ 0.29 from E₂). **κ₋ = κ_∞ = 1.4808832 is correct and asymptotically exact** — κ(λ) − κ_∞ ~ 1/(4√λ) > 0, so κ decreases to κ_∞ from above and no larger κ₋ is available for all λ ≥ 25.

The one soft spot the note itself flags (§12.10): the parenthetical justification of λE₁(λ) ≤ 25E₁(25) is weaker than advertised. I confirm the repair: d/dλ log(λE₁) = 1/λ − 1/(4μ) + 1/(2√μ) − ½ = −0.3704 at λ = 25 and negative throughout, so λE₁ is decreasing outright; and even the weak route (λE₁ ≤ 0.0105) leaves 0.52 − 0.9625·0.0105 = 0.510 > 0. **Clause 2 stands either way.**

Clause 3: m(25) = 0.6335 > 0 and m′(λ) = ½ − λ^{−1/2} − 1.5/λ ≥ 0.24 > 0 at λ = 25 and increasing. My re-run of `edge_law_two_sided.py` reproduces the 90-value table, min proved lower bound 1.483326, exact κ(25) = 1.51051, and the proved slack holding from λ = 23. **CLOSES.**

---

## 3. Clause 5, re-derived completely, and the attempt to break it

### 3.1 The re-derivation

(a) γ = x − iy, |y| ≤ ½, u = |x − t|. h_f(γ) = (γ − t)B̂(L(x−t) − iLy) and, by Lemma G's complex case, |B̂(ξ − iη′)| ≤ e^{|η′|/2}G(|ξ|) — which I re-derived: k integrations by parts give |B̂(ζ)| ≤ |ζ|^{−k}e^{|η′|/2}‖B^{(k)}‖₁ and |ζ| ≥ |ξ|, with the small-|ξ| case covered by |B̂| ≤ ∫B = 1 < 1/Z ≤ G. Both factors carry the same u and the same |y|, so the product is ≤ (u²+¼)e^{L|y|}G(Lu)² ≤ (u+½)²e^{L/2}G(Lu)². **The depth enters only through e^{L|y|} ≤ e^{L}… per pair, i.e. e^{L/2}; the bound is uniform in depth, which is the theorem's load-bearing claim and it is correct.**

(b) Shells. A point at u ≥ R lies in k ≤ u < k+1, k ≥ ⌊R⌋ ≥ R − 1 = u₀; each of the two unit intervals [t+k, t+k+1) and (t−k−1, t−k] sits inside one class window, so the shell count is ≤ 2C₁log(3.5+t+k) with multiplicity; log(3.5+t+k) ≤ log(3.5+t) + k since 3.5+t ≥ 1. Hence S_Z ≤ 2C₁e^{L/2}[log(3.5+t)Σ₂ + Σ₃] with Σ_m = Σ_{k≥u₀}(k+3/2)^mG(Lk)². The two absorptions 2C₁ ≤ e^{L/8}/b₁ and log(3.5+t) ≤ 1.05e^{L/8} both follow from the single hypothesis L ≥ 8(log log(3+t) + log(2b₁C₁)) because both bracketed terms are positive; the Σ₃ term then carries e^{5L/8}, which the note over-estimates as e^{3L/4} (safe).

φ_m(u) = u^m(1+(c_B/2)√(Lu))²e^{−2c_B√(Lu)} is decreasing for u > (m+1)²/(c_B²L) — I verified (log φ_m)′ ≤ (m+1)/u − c_B√(L/u), using that the log-derivative of the polynomial prefactor is ≤ 1/u — and at L = 50, m = 3 the threshold is 15.66 against u₀ = 4049. The substitution u = s²/L gives ∫_{u₀}^∞φ_m = (2/L^{m+1})∫_{s₀}^∞s^{2m+1}(1+(c_B/2)s)²e^{−2c_Bs}ds, a combination of three incomplete-Γ sums with a = 2c_B and n = 2m+1, 2m+2, 2m+3, coefficients 1, c_B, c_B²/4 — I re-implemented this from scratch. The relaxations s₀ ≥ √R₀L − 1/√R₀ (from √(1−ε) ≥ 1−ε), u₀ ≤ R₀L and s₀ ≤ √R₀L in polynomial factors, and β ≤ 1 + 3/(2(R₀L₀ − 1)) are all in the safe direction. The result:

  S_Z ≤ e^{2c_B/√R₀}e^{(3/4 − 2c_B√R₀)L}P(L)/b₁, and S_Z ≤ e^{−L} ⟸ F̃(L) := (7/4 − 2c_B√R₀)L + 2c_B/√R₀ + log(P(L)/b₁) ≤ 0.

P is a **Laurent** polynomial (terms L^{j−m−1}, j ≥ 0) with nonnegative coefficients and top degree 5 — §12.7 is right, and (log P)′ ≤ 5/L survives because negative-power terms contribute ja_jL^{j−1} < 0 ≤ 5a_jL^{j−1}. So F̃ decreases from L = 5/(2c_B√R₀ − 7/4) = 6.073.

**My own implementation gives the least half-integer R₀ at L₀ = 50 to be R₀ = 81.0 with F̃(50) = −0.133615** (author: −0.1334), F̃(60) = −7.477, F̃(100) = −37.90, F̃(403) = −280.4, F̃(10⁴) = −8165. The table R₀(L₀) = 58.5, 48, 43, 40, 38 at L₀ = 100, 200, 403, 1000, 10⁴ reproduces exactly, with limit (7/(8c_B))² = 37.461. §12.8's sharper route (spend the hypothesis once, exponent 13/8) gives R₀ = **73** in my implementation too; 81 is valid and conservative.

### 3.2 What the proof uses — I confirm the note's own hypothesis check

Exactly three things: (i) Z lies in the closed strip |Im γ| ≤ ½ (the only place the depth enters); (ii) #{γ : |Re γ − x| ≤ 1} ≤ C₁log(3+|x|) for every real x, with multiplicity (the shell counts); (iii) L ≥ 50 and L ≥ 8(log log(3+t) + log(2b₁C₁)) (the absorption), plus t ≥ 3 for log(3.5+t) ≤ 1.05log(3+t). **Nothing about the points inside the window, nothing about conjugation or reflection invariance, nothing about the orbit, nothing about t beyond t ≥ 3, nothing about C₁ beyond the absorption.** I found no hidden use of anything stronger. Hypothesis (i) is genuinely needed and genuinely restrictive — §12.4's point that DH's zeros with β > 1 are simply not points of any 𝒞(C₁) configuration is correct and is required for the rung-2 reading.

### 3.3 The attempt to break it

I built the worst configuration the class permits: **every point at depth exactly |y| = ½** (the maximal strip weight), every shell saturated at 2C₁log(3.5+t+k) points with multiplicity, every point placed at the *inner* edge of its shell (u = k, the largest term), at the least admissible bandwidth L = 50, the least height t = 3, and C₁ = 1. At depth ½ the summand is (u²+¼)|B̂(Lu − iL/2)|² ≥ 0 — **every out-window term adds with the same sign**, so nothing cancels and this is the true adversary.

* *At the window edge u = R₀L = 4050:* the proved per-point majorant is (u+½)²e^{L/2}G(Lu)² = **1.905·10⁻³²**; times the maximal shell count it is 3.216·10⁻³¹, i.e. **1.7·10⁻⁹ of e^{−L} = 1.929·10⁻²²**.
* *Summed over all shells k = 4049, 4050, …* (I summed to 10⁻⁶⁰ of the first term, shells 4049 … 17621): the adversarial total of the **proved** majorant is **2.159·10⁻²⁹ = 1.1·10⁻⁷ × e^{−L}**. Clause 5 survives by seven orders of magnitude at the worst admissible parameters.
* *The true size* (numerical envelope rate 0.849 in place of c_B): 3.45·10⁻³¹² — the mechanism is stronger than the proof by hundreds of orders.
* *How far in could the adversary come?* Summing the proved majorant with the true shell counts at t = 3, C₁ = 1, the crossing of e^{−L} is between R₀ = 50 (ratio 1.9·10⁴) and R₀ = 81 (ratio 1.1·10⁻⁷). The gap between that and R₀ = 81 is exactly the price of **uniformity in t and C₁**: the chain must survive the extreme case where the L-hypothesis holds with equality, i.e. where 2C₁log(3.5+t) is as large as e^{L/4}/b₁ ≈ 3·10⁴ rather than the 3.74 it is at t = 3, C₁ = 1. So R₀ = 81 is not slack that could be trimmed by a better adversary; it is the honest uniform constant.
* *Other adversaries tried and failed:* (α) large C₁ — F̃ is independent of C₁ because the absorption is exact; (β) large t — same, F̃ is independent of t; (γ) exploiting log(3.5+t+k) ≤ log(3.5+t) + k — this replaces a log by a linear term, i.e. it over-counts the adversary, so it cannot be turned against the proof; (δ) mass at depth just under ½ — strictly worse for the adversary; (ε) points with |Re γ| large on the far side of the origin — covered by the same shells, with the class applied at |t ± (k+½)|.

I verified the pointwise bound numerically at depth ½, L = 50 (true value against the proved majorant): the ratio bound/true is 4.1·10⁹ at u = 1, 2.1·10¹⁴ at u = 5, 1.1·10²³ at u = 20, 5.8·10³⁹ at u = 80. **Clause 5 CLOSES; the failure branch of PRICING §2.9 does not fire, and I could not make it fire.**

---

## 4. Clause 7 against II.4's exact statement

II.4 (`BARRIER-ZOO.md` lines 134–146, read at the page) is a statement about the **rank–trace certificate** 2c·tr(P+Q) − ‖P+Q‖²_F on configurations of orthonormal on-line atoms plus pair-blocks, with tightness "relative to the invariant list {tr, ‖·‖²_F, atom norms ≤ 1, n₊}", and the degeneracy is at c = 2 between an on-line double (k₂(2) = 4) and an off-line pair **at depth → 0** (charge 4). Its executable test demands: name the invariant beyond the list, its unconditional price, run IV.6/IV.7 on it, and make the separation depth-uniform **or price it over the depth family u ∈ [0, 1/L′]**.

* **Does clause 7 claim anything II.4 forbids? No.** The datum W_Z(f_{t,L}) = Σ_Zĝ(γ) is a single first-order (linear-in-the-multiset) sum rule evaluated at one non-lattice atom whose bandwidth is tuned to δ; it is not a function of {tr(P+Q), ‖P+Q‖²_F, atom norms, n₊} at a fixed critical-sampling lattice. So II.4's tightness — which is a theorem *about that list* — is untouched and no formalized no-go is moved. The note says exactly this.
* **The sharper reason there is no conflict, which I recommend the note state:** II.4's degeneracy is a statement at **fixed** bandwidth as δ → 0, and clause 7 requires δL ≥ λ₀ = 25, i.e. δ ≥ 25/L. II.4's own depth family is u ∈ [0, 1/L′]. **Clause 7 is silent on every depth in II.4's window by a factor 25**, so the two statements have disjoint parameter regions; there is no overlap in which they could disagree. This is a strengthening of §7.2 (ii), not a correction.
* **Is the degeneration stated honestly? Yes.** §7.2 (ii) states both halves: L*(t,δ) ≥ max(25/δ, 4δ⁻¹(…)) → ∞ as δ → 0, and at fixed L the orbit's contribution −2δ²c(δL)² → −2δ² → 0 like δ². §9's S3 line and §13's close repeat it. The "tight-pair marketing" minor is answered.
* **The arithmetic of clause 7.** h_f(t) = (t−t)B̂(0) = 0, so the double at +t is invisible — exact. The reflected double at −t is one carrier point of multiplicity 2, whose `Wsummand` is m_ρ·|h_f(−t)|² = 2·(2t)²B̂(2tL)² = **8t²B̂(2tL)²**. I computed it directly at t = 30, L = 40: B̂(2400) = −5.0116·10⁻¹⁸ and 8t²B̂² = **1.8084·10⁻³¹**, exactly half the note's body value 16t²B̂² = 3.617·10⁻³¹. **D9 and §7.2's proof are wrong by a factor 2 in the body; §12.3's correction is right and my computation is independent of the author's.** The term is nonnegative and absorbed into N_{Z′} or O_{Z′} either way, so nothing downstream moves.
* **IV.6/IV.7 on the new invariant:** §12 step 5 dismisses IV.6 (no pair-correlation or averaged-HL input) and IV.7 (no tail row, no cubic) correctly — the datum is one untilted Weil test, not a second-order or cubic trace. I accept the dismissal, and I record that II.4's "name the invariant, price it" is answered by L*(t,δ) as the price.

**CLOSES**, on the record as corrected.

---

## 5. Four-point accounting and the W_Z convention, against `Zeta23/Defs.lean`

Read this session: `paperFT` line **44**, `gammaOf` line **105**, `reflect` line **108**, `structure ZeroConfig` line **120**, `Wsummand` line **164**, `W` line **170**.

* `gammaOf ρ = (ρ − ½)/i`, so ρ = β + iτ ↦ γ = τ − i(β − ½): γ real ⟺ β = ½, and 0 ≤ β ≤ 1 ⟺ |Im γ| ≤ ½ ✔.
* `reflect ρ = 1 − conj ρ` ↦ γ ↦ conj γ; `ρ ↦ conj ρ` ↦ γ ↦ −conj γ; together they generate γ ↦ conj γ and γ ↦ −γ ✔ (§0.1 is right). Since `ZeroConfig` *requires* reflect-invariance with equal multiplicities, W_Z(f) is real for every configuration in the structure ✔.
* `Wsummand f g ρ = m_ρ·h_f(γ_ρ)·conj(h_g(conj γ_ρ))`, `W = ∑' ρ : carrier` — a sum over **distinct** points with multiplicity written explicitly ✔. This is exactly what forces the reflected double to be 8t² and not 16t² (§4 above).
* The orbit of ρ₀ = ½ + δ + it is {t − iδ, t + iδ, −t − iδ, −t + iδ}. h_f(t ∓ iδ) = ∓iδ·B̂(∓iLδ) = ∓iδ·c(δL) with c real; the summand at t − iδ is (−iδc)·conj(iδc) = −δ²c², and at t + iδ likewise −δ²c². **The pair at +t contributes −2δ²c(δL)²: two zeros, −δ²c² each — the contract's constant is correct and the R1 "a pair = two zeros" lesson does not bite.** The reflected pair gives E₋ = 2Re[h_f(−t−iδ)conj(h_f(−t+iδ))]. My re-run of `four_point_accounting.py` reproduces every line: pair at +t = −13.9659126096 against −2δ²c² = −13.9659126096 (diff 6.8·10⁻²⁰), E₋ = −1.094·10⁻²⁵ = 7.83·10⁻²⁷ of the main term at t = 30, δ = 0.3, L = 40, W_Z real on the eight-point instance, g Hermitian and not real (max|Im g| = 2.49·10⁻⁴ — D1 is right, and nothing downstream needs g real since `EF_lit` takes k : ℝ → ℂ).
* Sign: the negativity comes from (−i)² = i² = −1, i.e. from (r − t)² at r − t = ∓iδ, not from any convention ✔.

**Stop condition (c) of the brief does not fire.**

## 6. `verify/` re-run, and the Lean citations

I re-ran `b1_constant.py` (148 s), `edge_law_two_sided.py` (5 s), `lemma_G_constants.py` (53 s) and `four_point_accounting.py` (68 s) in a scratch directory (nothing written into the repo) — **every printed number reproduces**, including b₁'s certificate 8.6980807, the 90-value edge-law table, R₀ = 81 with F̃(50) = −0.13339, c_R = 21 with margin 0.7171, L₁ = 17.9, the Gevrey form of T₁ crossing only at L ≈ 1.1·10⁴, and the L*-table. I did not re-run `dh_negative_control.py` (974 s, over the brief's budget); I checked its headline arithmetic by hand instead: at δ = 0.3085172, L = 86.907, δL = 26.81, clause 2 gives c(δL) ≈ e^{7.270} = 1435, so 2δ²c² ≈ 3.92·10⁵ against the log's 3.943·10⁵, and the clause-6 bound δ²e^{δL/2} = 6.32·10⁴, ratio 6.24 ✔.

I re-ran the `#print axioms` scratch file myself with `lake env lean` from the tree (nothing created or modified inside it): **all nine cited theorems depend on exactly `[propext, Classical.choice, Quot.sound]`** ✔.

Lean line numbers, checked this session: `Defs.lean` 44, 105, 108, 120, 164, 170 ✔; `ExplicitFormula.lean` `tilde` 48, `weilTest` 52, `gammaBracket` 64, `literatureRHS` 70, `EF_lit` 81, `paperFT_weilTest` 189, `prop_EF_of_lit` 703 ✔; `WeilEF/Main.lean` `EF_lit_zetaZeroConfig` 270 ✔; `WeilEF/Effective.lean` `zeta_local_zero_count_explicit` 926 ✔; `Taper/GevreyRamps.lean` `integral_abs_iteratedDeriv_phi_le` 203 ✔. In `Taper/Gevrey.lean` I independently confirm §12.12's four corrections: `GevreyProfile` is at **52** with `bound` at **58** (not 45–52), `def theta` at **61** (not 55), `gb_mul_gb_le` at **248** (not 262–275), `gevreyProfile_rhoTwo` at **401** (not 393); `gevrey_expNegInvGlue` at 185 and `abs_iteratedDeriv_theta_le` at 281 are as quoted. All names exist and all quoted text is verbatim, so stop condition (d) does not fire. §12.12's further point is also right: `prop_EF_of_lit`'s conclusion is a **three**-fold conjunction (`Summable ∧ Integrable ∧ Z.W f g = ∫ …`) and §1 quotes two of the three.

Lemma G itself: I re-derived G1's Leibniz step (C(k,i)i^i(k−i)^{k−i} ≤ k^k from the binomial theorem, and i^i(k−i)^{k−i} ≤ k^k, so each of the k+1 terms is ≤ k^{2k}) and Lemma G's optimization (k = ⌊κ⌋, κ = √(|η|/A₁)/e, giving log(A₁^kk^{2k}/|η|^k) ≤ −2k ≤ −2(κ−1), hence |B̂| ≤ (e²/Z)(1+κ)e^{−2κ} with 2κ = c_B√|η|), the κ < 1 case (RHS ≥ 1/Z = 4.5 > 1 ≥ |B̂|), and (G2)'s sup_{s≥0}(1+s/2)e^{−s/8} = 4e^{−3/4} at s = 6. **All correct; A₁ = 72/e is the right transfer constant (4^k affine × Leibniz) and the pricing's 0.20 = 1/(3√e) is indeed θ's constant, not B's.**

## 7. Reflection condition (clause 1's hypothesis t ≥ 21L)

* **Is it necessary?** Not for the truth of clause 1's conclusion — numerically |E₋|/(2δ²c²) = 7.8·10⁻²⁷ at t = 30, δ = 0.3, L = 40, where e^{−L} = 4.2·10⁻¹⁸, so the conclusion holds far outside (R). It **is** necessary for the *proof* with the on-disk c_B = 0.143: the sufficient condition (R) reduces, for δ ∈ [25/L, ½], to (R′), and I confirm independently that the least admissible t at L = 50, 100, 200, 403, 1000, 10⁴ is 1037, 1378, 2075, 3458, 7352, 6.39·10⁴ (ratios 20.7 → 6.4, limit 1/(8c_B²) = 6.116), and that **21 is the least integer c_R for which t = c_R L works at every L ≥ 50** (c_R = 20 fails at L = 50 by 1.37 nats; c_R = 21 has margin 0.7171). I also checked the note's derivative argument: at t = 21L the margin is 2c_B√42·L − 2log(1+(c_B/2)√42 L) − [L + √(2L) + 1.5log(L/2) − 2κ₋ + log((1764L²+¼)C_B²L²/625)], whose derivative is ≥ 1.853 − 0.9265/(1+0.4632L) − 1 − 1/√(2L) − 1.5/L − 4/L = 0.605 at L = 50 and increasing, so the margin is increasing for **all** L ≥ 50 — the grid check to 1.3·10⁵ is decoration, the statement is proved.
* **Is it stated in the theorem?** Yes, in three places: §7.1's hypothesis line ("and (R) of §4 (implied by t ≥ 21L)"), §7.3's clause 8 ("and if t ≥ 21L"), and §13's close. D3 records the deviation from the contract's "for all t ≥ 3". ✔
* **Does the DH control satisfy it? No**, and the note says so. At t = 85.699, L* = 86.9 the ratio is t/L* = 0.985, a factor 21 short. §8's caveat (ii) states this, and caveat (i) states that the window hypothesis is not verified for DH either. **See MAJOR-2 below: the caveats are correct but the headline that will be quoted downstream is not qualified.**

## 8. Scope (clause 8) and the "cannot"/"never" discipline

* **10(g) lint: clean.** "clearly", "obviously", "easy to see", "well known" do not occur anywhere in the note (grep, case-insensitive, including hyphenated forms).
* **Every "cannot"/"never" sentence.** Five occurrences: §6 line 313 ("polynomial decay cannot beat e^{L/4} at any polynomial |x|") carries its proof inline (the bound is ≥ 1 for |x| ≤ e^{L/12}) ✔; §8 line 364 ("the theorem cannot tell DH from ζ by itself") is supported by rung 2 plus clause 8 ✔; §9 line 372 ("the theorem never consumes Λ ≥ 0") is verifiable by inspection of clauses 1–7 ✔; §12 line 398 ("the theorem cannot decide RH") is supported because DH satisfies every input ✔; and §9 line 372's "**a** separation theorem about configurations cannot, without an arithmetic input, tell which configuration is ζ's" is an unproved general impossibility claim — **§12.11 catches it and supplies the restriction to *this* theorem, which is the right repair.** With the corrections section the discipline holds.
* **Is clause 8 honest about what the theorem does not say?** Yes, and §7.1's "what the theorem says and does not say" plus §14's closing list are more careful than the contract required: no zero is located; nothing about ζ without the prime-side evaluation (M6, named as the wall); nothing when both configurations carry off-line points inside the window; nothing for t < 21L; nothing outside 𝒞(C₁); the constants are called honest and weak, with the numerical/proved gap 0.849/0.143 stated. The prime-side display is exactly `literatureRHS` (`ExplicitFormula.lean` 70) applied to k = g, which is legitimate because g is C^∞ with compact support. **The statement of clause 8 is sound; its ζ-density constant is not (MAJOR-1).**
* **Prior art (V.2/V.3).** I read the Hua–Yang excerpts and the source PDF's presence on disk. (9.1.1) reads ‖u(r−iδ)‖₂² ≤ CL²e^{L|δ|}exp[−c{L dist(r,J)}^{1/s}], proved by "m integrations by parts against the whole complex exponential", m! ≤ m^m, m = ⌊c₀(L|r−τ|)^{1/s}⌋, with "the trivial estimate covers the bounded range omitted by the integer choice of m" — **this is Lemma G's mechanism, with the same strip weight, in print**, and (9.2)/(Prop 9.2) are the local count and the shell summation. The note's §11 reduction of its own novelty claim is accurate and honest; what it claims as new (the single-centre derivative-bump separation *statement* with a bandwidth-proportional window and explicit constants, the two-sided edge law with κ_∞ in closed form, the tight-pair clause with its degeneration) is not in the passages I read. V.5 is satisfied: no verdict rests on a null search.

---

## MAJORs — with the exact repair required

**MAJOR-1 (clause 8; ζ's density constant is wrong in the body *and* in the correction).**
The body (§1, §7.3, §8 rung 4) says ζ's configuration lies in 𝒞(C₁) with C₁ = 5.4·10⁸ "by `zeta_local_zero_count_explicit`". That theorem bounds `Ncount t (t+1)`, i.e. #{ρ : t < γ ≤ t+1} — a **half-open window of length 1**. The class asks for #{γ : |Re γ − x| ≤ 1}, a **closed window of length 2**, which is {x−1} ∪ (x−1, x] ∪ (x, x+1] and therefore needs **three** applications (at t = x−2, x−1, x), not one and not two. §12.5 spots this, says "two (strictly three, to catch the left endpoint)" — and then prints the **two**-window number, 2·5.4·10⁸·(log4/log3) = 1.36·10⁹ ≈ 1.4·10⁹.
*Repair required:* record **C₁(ζ) ≤ 3·5.4·10⁸·(log 5/log 3) = 2.373·10⁹, i.e. C₁ ≤ 2.4·10⁹** (the three windows sit at |t| ≤ |x|+2, so each costs log(|x|+5) ≤ (log 5/log 3)log(3+|x|), with the worst ratio 1.46497 at x = 0). Consequences: log(2b₁C₁) = log(2·8.70·2.373·10⁹) = **24.44** in place of §12.5's 23.91, and rung 4's L*(δ = 0.1, t = 10⁶) becomes **≈ 1267**, not 1246. Nothing else moves, and no clause's truth depends on it — C₁ is a free hypothesis parameter — but the number is quoted as a fact about ζ and must be right.

**MAJOR-2 (the record: §8 rung 2's heading and the §0 summary overstate the DH negative control).**
Rung 2's heading reads "the theorem holds, and the datum FIRES on DH's own off-line orbit", and line 5's summary reads "the datum separates DH's own off-line orbit at height 85.7 from the on-line configuration by a factor above the theorem's bound at the theorem's bandwidth". The body's caveats (i) and (ii) then state that **two of the theorem's hypotheses are not verified at these parameters** — the window hypothesis (DH's further off-line zeros inside |Re γ − t| ≤ R₀L* ≈ 7·10³ were not located) and the reflection condition (t/L* = 0.985 against the required 21). Both caveats are correct and prominent; the headline is what will be lifted into C2's work log, the zoo rider and STATUS, and it is not qualified. Under zoo V.4 the control's status matters: what fired is **the mechanism and the datum**, evaluated at the theorem's bandwidth, not an instance of the theorem.
*Repair required:* the rung-2 heading and the §0 summary sentence each carry the qualification, e.g. — heading: "**the datum FIRES on DH's own off-line orbit at the theorem's bandwidth; the run is at parameters where two of the theorem's hypotheses (the window hypothesis and the reflection condition) are not verified, so it confirms the mechanism, not an instance of the theorem**"; summary: append "**(at parameters where the reflection condition and the window hypothesis are not verified — §8 caveats (i)–(ii))**". No number changes.

---

## MINORs (no repair pass required; recorded for the author's fix pass)

1. **§7.1's proof: the three-way split is not a partition when R > 2t.** Under the theorem's own hypotheses the reflection condition gives only t ≥ 21L, while R = 81L, so for 21L ≤ t < 40.5L the reflected orbit points at −t lie in the region |Re γ − t| ≥ R and are counted **both** in E₋ and in clause 5's S_Z. The displayed equality W_Z = (−2δ²c² + E₋) + N_Z + O_Z is then false as an identity. The conclusion is untouched, because S_Z bounds a sum of absolute values over a superset and dropping two terms only decreases it. *Repair:* define O_Z as the out-window sum **over points other than the orbit**, and note that clause 5's bound applies a fortiori. One sentence.
2. **The window split at |Re γ − t| = R exactly.** Clause 4 covers |γ − t| ≤ R and clause 5 covers |Re γ − t| ≥ R; a point at distance exactly R is in both. Both bounds are upper bounds on nonnegative/absolute quantities, so the assembly is safe; say "< R" in clause 4 or "> R" in clause 5.
3. **b₁ is not carried at one value.** §12.2 correctly rules that the theorem is stated with b₁ = 8.70 (certified upper 8.6980807, which I re-verified). But §13's close still prints log(17.3C₁) — that is 2b₁ at b₁ = 8.65; at 8.70 it is **17.4C₁** — and §15/§8's L*(0.3085172, 85.7) = 86.907 was computed with b₁ = 8.64613 (at 8.70 it is **86.99**; the DH run itself was at L = 86.907, which is fine, it is simply not L*). L*(0.1, 10⁶) = 403 is unaffected. *Repair:* one constant everywhere, and a line saying at which b₁ each logged L* was computed.
4. **§0.3's "relative difference 10⁻⁶"** for the (0.2) double-quadrature check: the log prints `rel diff = 1.0e-9`. (§12.13(i) already says so; I confirm from my own re-run.)
5. **Clause 4's sum should be written with multiplicities** (Σ_{γ real} m_γ|h_f(γ)|²); the shell counts already carry them, so only the notation is loose.
6. **Non-vacuity at small t and C₁ = 1.** The orbit alone puts 2 points in the window at x = t, so 𝒞(C₁) requires C₁log(3+t) ≥ 2, i.e. C₁ ≥ 1.12 at t = 3: at C₁ = 1 the theorem's hypothesis set is empty for small t. Harmless (the theorem is then vacuous there), but §10's illustrative "C₁ = 1" deserves a word.
7. **§12.11's repair is stated as an instruction, not applied** (as are §12.1–§12.10 and §12.12–§12.13). That is the brief's process — the checker does not edit the body — but a reader of §§0–15 alone still meets 16t², "numerically vacuous", C₁ = 5.4·10⁸, b₁ = 8.6461 and the unrestricted "cannot" sentence. The author's one fix pass should apply all thirteen, plus MAJOR-1 and MAJOR-2 above.
8. **Optional, recommended:** §12.8's sharper chain (spend the L-hypothesis once, exponent 13/8) gives R₀ = 73 with the same one-point check; I reproduce it. Taking it would shrink the recorded window by 10 % at no cost in rigor.
9. **Recommended addition to §7.2:** state that clause 7 requires δ ≥ 25/L, so it is silent on II.4's whole depth family u ∈ [0, 1/L′] by a factor 25 — this is the cleanest single sentence showing the two statements cannot collide.

---

## Constants that differ from the author's

* **8t²B̂(2tL)², not 16t²B̂(2tL)²**, for the reflected on-line double of clause 7 (my independent value at t = 30, L = 40: 1.8084·10⁻³¹). The body is wrong; §12.3 is right.
* **C₁(ζ) ≤ 2.4·10⁹**, not 5.4·10⁸ (body) and not 1.4·10⁹ (§12.5); rung-4 L*(0.1, 10⁶) ≈ **1267**, not 1246. (MAJOR-1.)
* **L*(0.3085172, 85.7) = 86.99** at the corrected b₁ = 8.70, not 86.907 (MINOR-3); and §13's **17.4C₁**, not 17.3C₁.
* **c_B = 0.14296065** (D2's 0.14298 is a typo; §12.6 is right).
* Everything else — Z, ‖B′‖₁, ‖B″‖₁, ‖B‴‖₁, ∫|v|B, b₁ and its certificate, κ_∞, κ±, C_B, c_B′, C_B′, R₀ = 81 and its table, F̃(50) = −0.1336, c_R = 21 with margin 0.7171, 1/(8c_B²) = 6.116, L₁ = 17.9, (3/(4c_B))², (7/(8c_B))², (13/(16c_B))², R₀ = 73 under §12.8, L*(0.1, 10⁶) = 403.5, C₀ = 4, λ₀ = 25, c₀ = ½ — **agrees with the note to every digit printed.**

---

*End of referee report O. Written 2026-09-16, 19:29 IST. Note refereed: SHA-256 dd06d6913d51ff01a3f706c66cec4049af91053ae02dd55659982ed20313fa84. No file other than this one was created or modified by this referee; the Lean tree was read only, and the `#print axioms` check compiled a scratch file outside it.*

---

## Re-read after the second corrections section (Wed Sep 16 19:41 IST 2026)

**Read for this re-read:** ONLY the section "Corrections after the two blind referees" (lines 489–497) of `results/c2-m2/separation-note.md`, whose SHA-256 is now `89fba193c985eb610b1c2a7a42d949f3ad1662ea2ab292f6aec0c39c7ee39e81`. I did not open `check-O.md`, `verify-O/`, `hashes-O.txt`, `SHARED.md` or `referee-F.md`; referee F's record items reach me only as quoted inside that section, which is the orchestrator's doing.

### MAJOR-1 (ζ's density constant C₁) — **CLOSES**

The section records my derivation correctly and I re-verified every number independently at 30 digits:

* Three unit windows are indeed needed, and the section states the reason exactly (x − 1 ∉ (x−1, x] ∪ (x, x+1]). With (x−2, x−1], (x−1, x], (x, x+1] the worst Ncount argument has |t| ≤ |x| + 2, so log(|t|+3) ≤ log(|x|+5) ≤ (log 5/log 3)log(|x|+3), the ratio being worst at x = 0. **C₁(ζ) ≤ 3 · 5.4·10⁸ · (log 5/log 3) = 2.373·10⁹ → 2.4·10⁹** ✔.
* **The shifted-window sharpening to 2.1·10⁹ is valid**, and I confirm it on its own terms: with (x−1−ε, x−ε], (x−ε, x+1−ε], (x+1−ε, x+2−ε] the union is (x−1−ε, x+2−ε] ⊃ [x−1, x+1] for every ε > 0, the worst argument has |t| ≤ |x| + 1 + ε, and since the quantity bounded does not depend on ε the infimum over ε > 0 of the upper bounds is itself an upper bound, giving the factor log(|x|+4)/log(|x|+3) ≤ log 4/log 3 = 1.26186 and **C₁(ζ) ≤ 3 · 5.4·10⁸ · (log 4/log 3) = 2.044·10⁹ → 2.1·10⁹** ✔.
* Consequences check out: log(2b₁C₁) = **24.444** at 2.4·10⁹ and 24.295 at 2.1·10⁹ (b₁ = 8.70); **L*(δ = 0.1, t = 10⁶) = 1267.0** and **1261.0** respectively (the section's "≈ 1262" for the sharpened constant is 1261 by my computation — a rounding difference of no consequence).

Recording 2.4·10⁹ as the value and 2.1·10⁹ as a noted valid sharpening is the right call: 2.4·10⁹ is the one whose covering argument needs no ε-limit. **My MAJOR-1 is closed.**

### MAJOR-2 (the DH control's quotable headline) — **still MAJOR, narrowly: one false clause inside the new sentence**

The substance of the repair is **accepted**. The new reading — that the DH control confirms the mechanism and the datum at the theorem's bandwidth on explicit finite configurations, and is **not** an instance of the theorem's hypotheses, with the window hypothesis and the reflection condition named as the two unverified ones — is exactly the qualification I required, and it is now attached to the sentence that will be quoted. Were it not for the following, I would close it.

**The defect.** The parenthetical reads: "*the reflection condition (t/L\* = 0.985 against the proved 21 and the numerical-rate threshold t ≥ 32.9 at L = 87 — this one FAILS)*". DH's height is t = 85.699. **85.699 ≥ 32.9**, so DH *clears* the numerical-rate threshold with 2.6× to spare; it is only the **proved** form (t ≥ 21L = 1825 at L = 87) that fails. I recomputed the numerical-rate thresholds myself, running the same chain with c = 0.849 in place of c_B: least admissible t = **24.6 at L = 50, 32.5 at L = 87, 35.2 at L = 100** (the section's 25.0 / 32.9 / 35.7 from §12.1; the small differences are immaterial). So the clause "this one FAILS" is false on either reading, and it **contradicts §12.1 of the first corrections section**, whose entire purpose was to replace the earlier "numerically vacuous" claim by "satisfied at every parameter this program uses, **including the DH control at t = 85.7, L = 87**". Two corrections sections of the same note would then assert opposite things about the same number, and the false one sits in the headline.

*Exact repair required (deletion or one clause):* strike "and the numerical-rate threshold t ≥ 32.9 at L = 87 — this one FAILS", replacing it by "**— the PROVED form t ≥ 21L = 1825 fails by a factor 21; the numerical-rate threshold at L = 87 is t ≥ 32.9, which DH clears (§12.1)**". Nothing else in the sentence needs to move, and no number elsewhere changes.

*One further wording point, not a MAJOR:* the same sentence asserts "clauses 1–7 are theorems about the class 𝒞(C₁), **of which DH's strip-restricted zero multiset is a member**". Membership is `[recalled, unverified]` in the note itself (§6's hypothesis check and §12.4 both label the Riemann–von Mangoldt-type local count for DH as recalled, with no on-disk source). Write "a member **with some C₁** `[recalled — the RvM-type local count for DH; §6]`".

### Item (d) (the §7.1 non-partition when 21L ≤ t < 40.5L) — **recorded correctly; CLOSES**

Record item (d) states the point exactly as I raised it and prescribes the right fix: R = 81L while the reflection condition gives only t ≥ 21L, so for 21L ≤ t < 40.5L the reflected orbit at −t lies in the region |Re γ − t| ≥ R; **assign the reflected pair to clause 1 explicitly and exclude it from clause 5's sum**, after which the split is a genuine partition and the conclusion is untouched (clause 5's bound is over a superset of absolute values, so dropping two terms only decreases it). That is precisely my MINOR-1, and the prescription is the one I asked for.

### Other record items spot-checked in this re-read

(a) 8t²B̂(2tL)² = 1.8084·10⁻³¹ at t = 30, L = 40 — mine independently, ✔. (b) L*(0.3085, 85.7) = 86.99 at b₁ = 8.70 and 86.907 at 8.6461, §13's close at 17.4C₁ — ✔. (c) c_B = 0.14296065 — ✔. (e) clause 7's silence on II.4's depth family, and F's observation that at δ = 1/L the orbit term 8.3·10⁻⁴ sits below b₁/L² = 3.5·10⁻³ at L = 50 — ✔ (I confirm 2δ²c(δL)²|_{δ=1/L, L=50} ≈ 8.3·10⁻⁴ and b₁/L² = 3.48·10⁻³), and it is the right way to say the datum is blind in II.4's own regime. (g) the direct-summation figures (F's 70, my crossing near 57 at t = 3, C₁ = 1) are consistent: they differ because they fix different (t, C₁), which is exactly the uniformity price; 81 proved-and-uniform, 73 under §12.8, both conservative — ✔. (f) and (h) I did not re-derive, being referee F's items outside my MAJORs; neither bears on any grade of mine.

### Grades after the re-read

Clauses 1–7 **CLOSES** (unchanged). Clause 8 **CLOSES** — MAJOR-1 is repaired and the recorded constant is now correct. The single open item is **MAJOR-2, narrowed to one false clause in the new headline sentence**, with the exact replacement given above; it is a record defect, not a defect in any clause, and it blocks nothing but the quotability of that sentence. **No FATAL, at either reading.**

*Re-read block appended 2026-09-16, 19:41 IST, by referee O. Note re-read at SHA-256 89fba193c985eb610b1c2a7a42d949f3ad1662ea2ab292f6aec0c39c7ee39e81 (new section only).*
