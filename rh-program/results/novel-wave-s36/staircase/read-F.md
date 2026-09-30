# read-F — the orchestrator's read at the line of `NOTE.md` (seed N2 `staircase`)

Reader: Fable 5.1 (the orchestrator, in person — standing orders 7, 11(c)). Session 37, 2026-09-30. NOTE read whole (38 168 chars).
Verdict: **AGREES-WITH-CORRECTIONS. Close (K) UPHELD.** Theorems D, D′, A, B re-derived line by line and found correct; one proof gap
(Proposition E(b)) found and filled; three prose corrections. The decisive computation was RE-RUN by an independent route and CONFIRMED.

## 1. Re-derivations (each done by the reader, not taken from the NOTE)

- §1 identity: Riemann's split at x = 1 gives Λ(s) = 1/(s(s−1)) + Σ_n X^{−s/2}Γ(s/2, X) + X^{−(1−s)/2}Γ((1−s)/2, X), X = πn². ✓
- Theorem D: k(u) = exp(u/2 − Xe^{2u}); k′ = k(½ − 2y), k″ = k(4y² − 6y + ¼), larger root (3 + 2√2)/4 = 1.457 < π ≤ y. Pólya's criterion
  by one integration by parts and the alternating-series argument. ✓  P_w = ½(¼ + t²)Σ(1 − w_n)g_n ≥ 0 because s(s−1) = −(¼ + t²) on the line. ✓
- Theorem D′: two integrations by parts give ½(¼+t²)g_n = −2k_n′(0) − 2∫(k_n″ − k_n/4)cos(tu)du, −2k_n′(0) = (4πn² − 1)e^{−πn²};
  φ̃ = 2y(2y − 3)e^{u/2−y}; φ̃′ = e^{u/2−y}·y(−8y² + 30y − 15); φ̃″ = e^{u/2−y}·y(16y³ − 112y² + 165y − 37.5) — both recomputed. ✓
  Tail coefficient: t²Ξ_N^{Hag} → 2Σ_{n>N}φ̃_n′(0) = −2Σ_{n>N}(8X³ − 30X² + 15X)e^{−X}; at N = 1 this is −2φ̃₁′(0) = −2·e^{−π}·π·0.29094 = −0.0790. ✓ (the NOTE's −0.078997)
- Theorem A: (a) growth on the real axis ⟹ not e^{a+bs}P(s) ⟹ infinitely many zeros ✓; (b)(i) liminf on the line > 0 ✓;
  (b)(ii) the u → −∞ expansion coefficient of e^{(5/2+2k)u} recomputed: −π(2k+3)(−π)^k/k!·Σ w_n n^{2k+2} ✓; Vandermonde ✓.
- Theorem B: D = K_w(u) − K_w(−u) odd with D″ = D/4 ⟹ D = 2α sinh(u/2) ⟹ ψ_w(1/x) = √x ψ_w(x) − α(√x − 1); C_w = 0 ⟹ α = −½ ✓;
  δ = ψ_w − ψ has an entire Mellin transform; Hamburger ⟹ f = cζ, f entire ⟹ c = 0 ✓. Hamburger's theorem read at the page:
  Nakamura arXiv:2008.02570 p. 4 "Theorem D (Hamburger [5, Satz 1])" with (H1)–(H3) — on disk `lit/nakamura-2008.02570.txt` lines 170–177. ✓
- Haglund's definitions and statements read at the page by the reader (arXiv:0910.5228 pp. 1–4, `lit/haglund-0910.5228.txt` lines 1–230):
  (1), (6)–(14), "monotonic zeros", Conjecture 1, Proposition 1, Remark 1, the p. 4 table. The NOTE's paraphrases are accurate.

## 2. The decisive computation, re-run (independent route, rigorous balls)

`verify-F/haglund_direct_arb.py`, `verify-F/rerun_N27.py`, log `verify-F/rerun_N27.log`: Haglund's Ξ_N evaluated LITERALLY from his (10), (13), (14)
in Arb ball arithmetic (python-flint 0.6.0) at 4800 bits — a different formula (the NOTE used Ξ − tail) and a different library (the NOTE used mpmath).
Validation against Haglund's table: sign changes of Ξ₁ in (14.04543957, 14.04543959) and of Ξ₂ in (39.5324810797, 39.5324810799). ✓
 Ξ₂₇(3144.8946) = [−1.76019463128e−1070 ± 2.49e−1082],  Ξ₂₇(3144.8947) = [+1.06871649226e−1070 ± 1.71e−1082]  ⟹ a real zero in between — RIGOROUS.
 Ξ₂₇(3145.5998) = [+1.12975694292e−1070 ± 3.36e−1082],  Ξ₂₇(3145.5999) = [−1.14913915363e−1070 ± 2.22e−1082]  ⟹ a second real zero — RIGOROUS.
 Ξ₂₇(3143.220682421536585287 + 0.3152587993782148453823 i) = [2.5788e−1085] + [1.7050e−1084] i, while Ξ₂₇ at a point 1e−6 to the right is 6.1e−1072 in modulus
 (|Ξ₂₇′| ≈ 6.1e−1066): the NOTE's point is within ≈ 3e−19 of a zero — numerical for the complex zero (a point value proves no existence).
 Ξ₂₇ < 0 at t = 3142.95, 3143.2, 3143.5, 3144.0 (rigorous point signs; consistent with no real zero in the box, not a proof of it).
**CONFIRMED.** What is still owed for a theorem: a rigorous winding number (or equivalent) for the complex zero — unit `results/haglund-cert-s37/`.

## 3. Corrections (OLD/NEW pairs)

F1 [prose, Theorem D′ proof, last parenthesis]. OLD: "the factor −8y² + 30y − 15 is +0.9 at y = π". NEW: "the factor −8y² + 30y − 15 is +0.291 at y = π
   (so φ̃₁′(0) = e^{−π}·π·0.291 = +0.0395 > 0)". [8π² = 78.957, 30π = 94.248; 94.248 − 78.957 − 15 = 0.291; the NOTE's 0.9 is y times the factor.]
F2 [factor 2, Theorem A proof (b)(ii)]. OLD: "Φ_w(u) = Σ_n w_n φ_n(u), φ_n(u) = (2π²n⁴e^{9u/2} − 3πn²e^{5u/2})exp(−πn²e^{2u})". NEW: "Φ_w(u) = 2Σ_n w_n φ_n(u), …"
   [K_w″ − K_w/4 = Σ w_n(4π²n⁴e^{9u/2} − 6πn²e^{5u/2})exp(−πn²e^{2u}); Haglund's (3) is 4 times the NOTE's φ_n. The vanishing argument is unaffected.]
F3 [GAP, Proposition E(b) — filled]. The NOTE's proof covers a compact rectangle; W_N → ∞ also needs "no zero of ξ_N with |Im s| ≤ T and Re s ≥ 2
   (or ≤ −1), for N ≥ N₀(T)". Proof (reader's): (regime 1) for 2 ≤ σ ≤ π(N+1)², |t| ≤ T: for n > N, X = πn² ≥ σ, so
   ∫₁^∞e^{−Xx}x^{σ/2−1}dx ≤ e^{−X}/(X − σ/2 + 1) ≤ 2e^{−X}/X and the mirrored term is ≤ e^{−X}/X; hence |ξ_N − ξ| ≤ ½|s(s−1)|·3Σ_{n>N}e^{−πn²}/(πn²), while
   |ξ(s)| ≥ ½|s(s−1)|π^{−σ/2}|Γ(s/2)|(2 − ζ(2)); the ratio → 0 as N → ∞ uniformly in the region, so ξ_N ≠ 0 there. (regime 2) for σ ≥ π(N+1)²:
   ξ_N = ½s(s−1)π^{−s/2}Γ(s/2)ζ_N(s) + ½ − ½s(s−1)Σ_{n≤N}[X^{−s/2}γ(s/2, X) − X^{−(1−s)/2}Γ((1−s)/2, X)], with |X^{−s/2}γ(s/2, X)| ≤ 2/σ and the last term ≤ e^{−X}/X,
   against |π^{−s/2}Γ(s/2)ζ_N(s)| ≥ 0.355·π^{−σ/2}|Γ(s/2)|, which is super-exponentially large at σ ≥ π(N+1)². The left side follows by s ↦ 1 − s. ∎
   (Proposition F lists this as hypothesis (ii) and supports it for C1 by computed exclusion counts; with the paragraph above it is proved for large N.)
F4 [prose, Proposition E(c)]. OLD: "then W_N stays below that zero's height for every N". NEW: "then limsup W_N is at most that zero's height
   (for all large N the cluster is there by Rouché; for small N the window has not reached it)".
F5 [prose, Theorem D′ consequence (1)]. OLD: "plus one in the central lobe (0, γ₁)". NEW: "plus an odd number (observed: one) in the central lobe
   (0, γ₁) — because Ξ_N^{Hag}(0) = Ξ(0) − Q_N(0) ≥ 0.4971 − c₁ > 0 while Ξ_N^{Hag}(γ₁) < 0".

## 4. Status of the NOTE's claims after the read

 Theorems D, D′, A, B, Proposition F: dual-model (Opus writer + this read). Proposition E: (a), (c) as corrected; (b) with the reader's paragraph F3.
 The refutation of Haglund's Conjecture 1 at N = 27: the two real zeros are RIGOROUS (ball sign changes, this read); the off-line zero is numerical,
 confirmed by two independent routes; novelty single-check (Opus sub-agent) until the reader's own search is recorded (unit `haglund-cert-s37`).
 Zoo line owed (K with theorems): staged by the digest/zoo stream — "approximation staircases are height filtrations; Pólya's criterion is RH-false-world-blind".
