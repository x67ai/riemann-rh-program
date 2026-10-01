# read-F — the orchestrator's read of `results/lemmaB-s41/U7-patterns/NOTE.md` (Fable 5.1, Session 41, 17:49 IST 2026-10-01)

NOTE at de201538a73d9417…. Read at the line: §5 Theorem 5.1, Theorem 5.2, 5.3, Corollary 5.4, Theorem 5.5 (statement), and (I1) of §4.1. NOT read: §1 (the generator's error bound), §3–§4 statistics, §6–§9 — computed, one producer; the headline counts agree with the Session-40 and Session-41 generators as the unit reports.

## Re-derived — ✓
- **(I1)** ✓. For a g-prime d and x_j ≥ d, the composites in (x_j, x_k] divisible by d are d·m with m a g-integer in (x_j/d, x_k/d] (free monoid; m > 1 because x_j/d ≥ 1), so their number is N(x_k/d) − N(x_j/d) = (k − j)/d + E(x_k/d) − E(x_j/d).
- **Theorem 5.1** ✓. Lindley: e_k = max_j Σ_{i=j+1}^k (c_i − 1); split c_i − 1 = (c_i^{(d)} − 1/d) + (c_i − c_i^{(d)} − (1 − 1/d)); the first sums are E(x_k/d) − E(x_j/d) ≤ E(x_k/d) + τ by (I1) and E ≥ −τ (the case x_j < d checked: the sum is E(x_k/d) − ρ(1 − x_j/d)); the second sums are ≤ r_k^{(d)} by Lindley for r^{(d)}.
- **Corollary 5.4** ✓. M(x) ≤ M(x/p₁) + 2 + R(x), iterated along x/p₁^j; a power bound for R passes to M through a geometric sum. So Lemma B_ρ is equivalent in strength to the same bound for the queue r^{(1)} of the arrivals coprime to p₁ (served at 1 − 1/p₁).
- **Theorem 5.5** is the relation the orchestrator derived independently in `../ORCH-NOTES.md` O9 (correction block): two derivations, one identity.

## What it means for the stream
The multiples of p₁ are "free" (the system one scale down). The whole difficulty sits in the p₁-rough arrivals — on data a Poisson-like fringe carried mostly by semiprimes with both factors large — which is where `ORCH-NOTES.md` O4 put the parity barrier. The reduction does not lower the difficulty; it names the object: a queue fed by rough composites. No correction pairs from this read.
