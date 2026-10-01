# read-F — the orchestrator's read of `results/lemmaB-s41/U6-certificate/NOTE.md` (Fable 5.1, Session 41, 17:35 IST 2026-10-01)

NOTE at 9f4bd0f4e3a6f8e7… (335 lines). §0 and §1 (lines 39–100) read at the line; §2–§6 (the generator, the interval evaluation, the certificates, the concavity bracket) NOT read here — they are the second producer's job (`read-O.md`, launched the same hour), and the orchestrator has no interval code of its own.

## §1 re-derived — every statement ✓
- **Lemma 1.1** ✓. With w(u) = ρ(u − 1) + ½: E(u) = N(u) − w(u) − ½, and E > −½ means N(u) > w(u); N is an integer, so N(u) ≥ ⌊w(u)⌋ + 1 and E(u) ≥ ½ − {w(u)}.
- **Lemma 1.2** ✓. On a lattice cell [x_k, x_{k+1}) the floor is ½ − ρ(u − x_k), antisymmetric about the midpoint; against the strictly decreasing weight u^{−σ−1} its integral is positive.
- **Theorem 1.3** ✓. ζ_P(σ₁) = F_X(σ₁) + σ₁∫_X^∞ E u^{−σ₁−1}du > F_X(σ₁) ≥ 0 at a lattice point X, under (B) or the mean-square (B₂); then the pole at 1 and the intermediate value theorem; the last step as in Theorem 1.6. The term ½X^{−σ₁} of the Session-40 criterion is gone.
- **Cor. 1.4** ✓, including (b) (Lemma L: a value |E(x)| = H ≤ ρx keeps |E| ≥ H/2 on a window of length H/(2ρ) inside [x/2, 2x]).
- **Prop. 1.6** ✓. F_{x_{k+1}}(σ) − F_{x_k}(σ) = σ∫_{x_k}^{x_{k+1}} E u^{−σ−1}du ≥ the floor's integral over one cell > 0, with no hypothesis on E; (ii), (iii) follow.
- Arithmetic: σ₁/2 = 0.39737768505 (π/16), 0.44753825880 (π/32); (3σ₁ − 2)/4 = 0.09606653 and 0.17130739. The report's "θ ≤ 0.3973776850" is σ₁/2 rounded down, so the non-strict sign is correct.

## Status after this read
The criterion (Lemmas 1.1–1.2, Theorem 1.3, Cor. 1.4, Prop. 1.6) is re-derived by the orchestrator: **T, one read; the Opus read is running.** The two inequalities F_X(σ₁) > 0 at X ≈ 10¹⁰ are [computed, ONE producer]; they become certificates when the second producer's independent run agrees. No correction pairs from this read.

## Reconciliation with the second producer (18:19 IST 2026-10-01)
`read-O.md` (7eaedaf69f0e8140…): CONFIRMED. An independent generator with NO floating point in any ordering decision (every decision reduced to integers through the elementary symmetric functions of the odd numbers 2n_i − 1; a 320-bit exact fallback never needed) and an Arb evaluator on integer block moments reproduce both certificates: the zero of F_X at X = x_K ≈ 10¹⁰ lies in (0.794755370097380, …381) for π/16 and (0.895076517592160, …161) for π/32; N, π_P, E equal at all 56 checkpoint integers; every F_X ball of the first producer contains the second's value. The one mathematical correction was re-derived before applying: in Cor. 1.4(b) the case split is at H = 2ρx, not ρx (E(u) ≥ H − ρx on [x, 2x] is ≥ H/2 only when H ≥ 2ρx; below that the window [x, x + H/(2ρ)] lies in [x, 2x]). The other pairs are scope and wording (σ = 1 excluded in Prop. 1.6(i); "first real zero" versus "largest real zero"; one table entry at 10⁸ that was a lower bound, not the zero). 8/8 pairs applied; pre-reader copy `NOTE.pre-reader.md`.
**Unit CLOSED: the criterion T (dual-read); the certificates CERTIFIED BY TWO INDEPENDENT PRODUCERS.**
