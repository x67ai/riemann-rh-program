# BRIEF — unit `haglund-cert-s37`: an interval-rigorous certificate that Haglund's Conjecture 1 fails at N = 27

Session 37, 2026-09-30. Orchestrator: Fable 5.1. SESSION 37 QUEUE item 2(0). Two independent producers (A, B), each an Opus agent
in its own folder (`producer-A/`, `producer-B/`); neither reads the other's folder before its own CERT.md is final.

## 1. The object (read at the page by the orchestrator: arXiv:0910.5228 pp. 1–4; text on disk
`results/novel-wave-s36/staircase/lit/haglund-0910.5228.txt`, PDF beside it)

- Ξ(z) = ½(½+iz)(−½+iz) π^{−(½+iz)/2} Γ(½(½+iz)) ζ(½+iz)                       (Haglund (1); s = ½ + iz)
- G(z; a, b) = 4∫₀^∞ cos(2zu) exp(2bu − a e^{2u}) du = Γ(b+iz, a)/a^{b+iz} + Γ(b−iz, a)/a^{b−iz}   ((6), (10); Γ(·,a) upper incomplete gamma)
- Φ_n(z) = 2π²n⁴ G(z/2; n²π, 9/4) − 3πn² G(z/2; n²π, 5/4)                      ((14))
- Ξ_N(z) = Σ_{n=1}^N Φ_n(z)  ((13));  Ξ(z) = Σ_{n≥1} Φ_n(z)  ((12)).  Ξ_N is entire, even, real on the real line.
- Q = {Re z ≥ 0, Im z ≥ 0}. "Monotonic zeros in Q": zeros listed by increasing real part have nondecreasing imaginary parts.
- Conjecture 1 (p. 3): for every N, Ξ_N has monotonic zeros in Q.  Remark 1 (p. 4, weak form): no non-real zero of Ξ_N in Q
  has real part less than the largest real zero of Ξ_N.  Proposition 1: Conjecture 1 ⟹ RH.

## 2. The claim to certify (Theorem H) — every clause by rigorous interval/ball arithmetic, no floating-point step trusted

 (H1) Ξ₂₇ has a real zero in the interval (3144.8946, 3144.8947)   [a rigorous sign change at the two endpoints].
 (H2) Ξ₂₇ has at least one zero z₀ in the closed square S centred at c = 3143.2206824215 + 0.3152587994 i with half-width r
      (any r ≤ 10⁻³ you can certify; report the smallest you reach) — by a rigorous winding number ≠ 0 of Ξ₂₇ along ∂S
      (every boundary piece's enclosure excludes 0; the argument increments sum to 2π·k, k ≥ 1; report k — expected 1).
 (H3) Hence: z₀ ∈ Q is non-real (Im z₀ ≥ 0.3152 − r > 0) with Re z₀ ≤ 3143.2217 < 3144.8946 < a real zero of Ξ₂₇ — the
      imaginary parts are NOT nondecreasing, so Conjecture 1 is false at N = 27, and so is the weak form of Remark 1.
 Optional, if cheap: (H4) a second real zero in (3145.5998, 3145.5999); (H5) the sibling statement for the seed's chain
      ξ₂₄ = Ξ₂₄ + c₂₄ (see the N2 NOTE §4; zero near s = 0.8159896243 + 2508.2839748053 i) — only after H1–H3 are done.

Reference values (the orchestrator's own literal-sum evaluation in Arb balls at 4800 bits,
`results/novel-wave-s36/staircase/verify-F/rerun_N27.log`; rigorous enclosures at exact decimal points):
 Ξ₂₇(3144.8946) = −1.76019463128e−1070 ± 2.5e−1082;   Ξ₂₇(3144.8947) = +1.06871649226e−1070 ± 1.8e−1082;
 Ξ₂₇(3145.5998) = +1.12975694292e−1070;  Ξ₂₇(3145.5999) = −1.14913915363e−1070;
 Ξ₂₇(3143.220682421536585287 + 0.3152587993782148453823 i) = (2.58e−1085) + (1.70e−1084) i  (|Ξ₂₇′| ≈ 6.1e−1066 there).
 WARNING: the literal sum Σ_{n≤27} Φ_n cancels about 1060 decimal digits at this height (terms ~1e−9, sum ~1e−1066):
 it is rigorous only at ≥ ~4000 bits and only for POINT inputs; on a wide input ball it is useless. For ball inputs use the
 tail route  Ξ₂₇ = Ξ − Σ_{n≥28} Φ_n  (no cancellation: all terms ~1e−1066), with a PROVED bound for the tail n > M, e.g.
 |G(z; a, b)| ≤ 2·Γ(b + |Im z|, a)/a^{b+|Im z|} and Γ(β, a)/a^β = ∫₁^∞ e^{−ax}x^{β−1}dx ≤ e^{−a}/(a − β + 1) for a > β − 1
 (derive and check these yourself before use; they are the orchestrator's sketch, not a citation).

## 3. The two producers

 PRODUCER A (folder `producer-A/`): python-flint 0.6.0 (Arb) — installed; note `acb(z).gamma_upper(s)` is Γ(s, z): the ORDER is the
  parameter, the lower limit is `self` (the orchestrator's first script had it backwards; `verify-F/haglund_direct_arb.py` is a working
  literal evaluator you may read but must re-derive). Two routes: (L) literal sum at points; (T) tail route on balls with Arb's zeta, gamma.
  H1 by both routes; H2 by route T; cross-check L against T at ≥ 8 exact points on and inside ∂S (balls must overlap).
 PRODUCER B (folder `producer-B/`): NO Arb, NO python-flint anywhere. mpmath.iv (interval arithmetic, outward rounding) and/or exact
  rational arithmetic, with every series truncation and every special-function remainder PROVED in the write-up (incomplete gamma by its
  series/continued fraction/integral with a written tail bound; Γ by Stirling with a stated rigorous remainder; ζ by Euler–Maclaurin with
  a stated rigorous remainder if you use the tail route). At minimum H1 and H2, by whatever rigorous method you can complete.

## 4. Ladder and dress rehearsal (KICKSTART 10(b), 10(l)) — BEFORE N = 27, with the same code

 (R1) Haglund's table p. 4: certify a real zero of Ξ₁ in (14.04543957, 14.04543959) and of Ξ₂ in (39.5324810797, 39.5324810799).
 (R2) one NON-real zero of Ξ₁ from Haglund's appendix (the paper's last pages list the zeros of Ξ₁; take the one of smallest modulus
      with positive imaginary part): certify winding number 1 on a small square, with the same winding-number code used for H2.
 (R3) a negative control for the winding code: a square known to contain no zero returns winding number 0.
 Only then N = 27. A producer that skips the ladder is returned.

## 5. Deliverables (each producer, in its folder)

 scripts (runnable: `python3 <script>` reproduces every printed enclosure); logs with every enclosure printed;
 `CERT.md` (≤ 200 lines): Theorem H with the exact certified numbers, the list of every analytic bound used with its proof or its
 page-cited source READ ON DISK (no recalled bound is load-bearing — standing order 5), the ladder results, run times, versions;
 `SHARED.md`: a dated block after each stage (setup, ladder, H1, H2, cross-checks). SHA-256 of CERT.md and of each log at the end.
 Do NOT run git commands (a watchdog commits). At most ONE CPU-heavy process at a time (thermal cap; another session is also computing).
 The path contains spaces: quote every path in shell commands.

Stop and report when: a rigorous enclosure CONTRADICTS a clause (no sign change at the H1 endpoints; a boundary piece whose enclosure
cannot exclude 0 at any feasible precision; winding number 0) — that is a finding; write it to SHARED.md and stop.

HARD OUTPUT RULE: never write more than about 6 kB of text in a single response or tool call. Build every deliverable incrementally on
disk — create the file, then append one section (or five table rows) at a time — and append a dated block to SHARED.md after each
batch. Keep reasoning between tool calls short; think in the files, not in long messages. Your final report is under 60 lines.
