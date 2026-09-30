# read-F — the orchestrator's read at the line of `NOTE.md` (seed N1 `ly-infinity`)

Reader: Fable 5.1 (the orchestrator, in person — standing orders 7, 11(c)). Session 37, 2026-09-30. NOTE read whole (32 538 chars).
Verdict: **AGREES. Close (K) UPHELD — Theorem K kills the orchestrator's own Session-36 seed in its class.** No FIX-FIRST item.

## 1. Re-derivations (done by the reader)

- Theorem 1, step 2: along the coordinate path 0 → v each one-variable restriction has all roots |ω| ≥ 1, Re(1 − v_j/ω) > 0, so each root moves Im log P by
  less than π/2: |Im L(v) − Im L(0)| < |d|π/2 on Dᵐ. ✓  Step 3: P(v) = v^d P†(1/v) on Eᵐ with P† Schur stable. ✓
  Step 4: the thin-rectangle count. The monotonicity "arg v_j(½+it) decreases in t" holds for EVERY inner function of Re s > ½, not only p^{−it}:
  ∂_t arg v = ∂_σ log|v| ≤ 0 on the line (Cauchy–Riemann; |v| < 1 to the right). The NOTE states it with one example; the general reason is this line. ✓
  Result: |N_F(t₁,t₂) − (1/2π)Σ d_j|Δ arg v_j|| < |d|. ✓
- Corollary 2: 28.2·log 2/2π = 3.1110, so N > 2.111|d| ≥ 3 (no archimedean channel); with one degree-one channel N > 2.111|d_fin| − 1 ⟹ N ≥ 2. ✓
- Theorem K: Hurwitz on the closed box [−14.11, 14.11] × [−¼, ¼] (Ξ zero-free there; first zero 14.1347251417…) against ≥ 2 real zeros of f_k in (−14.1, 14.1). ✓
- E2 (the seed's sign): arg b_p(p^{−it}) = −t log p − 2 arg(1 − p^{−1/2−it}); zeros of 1 + B at t log P − 2πS_X(t) ≡ π, against ζ's 2ϑ + 2πS ≡ π. ✓
  The Session-36 seed's product Π(1 − p^{−s}) IS anti-aligned; the orchestrator's error stands recorded.
- Proposition 3: e^{−iεt}n^{−it} sin(ε(γ − t)) = (e^{iεγ}m^{−it} − e^{−iεγ}n^{−it})/2i with 2ε = log(m/n). ✓ (the ACV class is tautological.)
- Quotations read at the page by the reader: Kurasov–Sarnak arXiv:2004.05678 p. 1 ("his example 4 page 264 coming from the explicit formula in the theory of
  primes does not give a Fourier quasicrystal, even assuming the Riemann hypothesis" — `sources/u-20b-…txt` lines 38–40); Alon–Vinzant arXiv:2307.13498
  Theorem 1.9 (density ⟨d,ℓ⟩T/2π with |err| ≤ |d|; gaps ≤ 2π|d|/⟨d,ℓ⟩ — `sources/u-27b-…txt` lines 253–260). ✓

## 2. The decisive computation, re-run (independent method)

`verify-F/rerun_theoremK.py` (+ `.log`): 40 Haar-random unitary couplings U with 1–8 prime slots drawn from {2,…,23} (repetition allowed); zeros of
det(I − Z(t)U) in (−14.1, 14.1) counted by sign changes of the real function det(I − W)·e^{itW_tot/2}·const on a 400 001-point grid (the NOTE's script
counts differently). Every trial: N ≥ 3, |N − W·L/2π| < |d| (worst ratio 0.785), every gap ≤ 2π|d|/W. Ξ: one zero in 0 < t < 14.2 (14.13472514…). **CONFIRMED.**

## 3. What the reader adds (not corrections)

(a) The kill is a statement about WHERE the primes may sit, and it is sharper than the NOTE's §6(4) last bullet says: in any unitary-secular/inner
    construction the zero density is the total winding of the inner channels; ξ's density (1/2π)log(t/2π) is the winding of ONE archimedean inner function
    e^{−2iϑ(t)} (the scattering phase of the Γ-factor). So the primes must enter with ZERO net winding — as a phase arg ζ(½+it) = πS(t) that is a boundary
    value of log of an OUTER function on Re s > ½ (that is what RH says: ζ(s)(s−1) outer there). "Primes in the outer part" is therefore not a design choice
    but a restatement of RH; the design problem is to find a positivity generator that FORCES outerness. This sentence goes to the digest.
(b) The open edge (§8, several slow archimedean channels) is a finite-rank question; by (a) even a YES there would still need the prime winding to cancel
    exactly, which the counting error |d| cannot do at large height (density W/2π ≫ log(t/2π)/2π for W → ∞ at fixed t). Priority: LOW unless a rung-1 model appears.

## 4. Status after the read

 Theorem 1 (inner-channel extension of Alon–Vinzant 1.9), Corollary 2, Theorem K, Propositions 3–4, Lemma F: dual-model (Opus writer + this read).
 Novelty of the application to Ξ: single-check (Opus) — null searches logged; not for external use without the second check.
 Zoo line owed (K with a theorem; Group-IV candidate "prime channels add density; ξ's density is archimedean"): staged for the s37 zoo stream.
