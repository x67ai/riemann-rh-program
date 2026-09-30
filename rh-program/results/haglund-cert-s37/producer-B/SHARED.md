# SHARED — producer B, unit `haglund-cert-s37` (independent of producer A; no Arb, no python-flint)

## 2026-09-30 22:50 — setup
- Read: `../BRIEF.md` (binding), staircase NOTE §4/§6/§7, Haglund arXiv:0910.5228 text pp. 1–4 and the Appendix
  (zeros of Ξ₁, p. 15 of the text file, line ~730). Did NOT open `../producer-A/`.
- Environment: Python 3.9.6, mpmath 1.3.0 (`mp.iv`, outward-rounded interval arithmetic). No Arb/flint imported anywhere.
- Sources saved to disk for every cited identity/bound (`lit/`, fetched 2026-09-30 from dlmf.nist.gov, text via `lit/html2txt.py`):
  DLMF 2.10.1 (Euler–Maclaurin with remainder ∫(B_{2m} − B̃_{2m}(x))/(2m)! f^{(2m)}), 24.9.2 (|B_{2n}(x) − B_{2n}| ≤ (2 − 2^{1−2n})|B_{2n}|),
  5.11.1 + 5.11(ii) (Stirling series; complex remainder ≤ sec^{2n}(½ ph z) × first neglected term), 25.2.9 (ζ by E–M, cross-reference).
- Plan: tail route Ξ_N = Ξ − Σ_{n>N} Φ_n (Haglund (12)); Ξ = ξ(½+iz) by Stirling + Euler–Maclaurin; Φ_n by its literal form (14) with
  h(w) = X^{−w}Γ(w,X) = ∫₁^∞ e^{−Xu}u^{w−1}du enclosed by repeated integration by parts (large X) or Γ(w) − lower series (small X),
  each with a remainder proved in CERT.md; explicit tail bound for n > M. Winding numbers by a Taylor model
  (DFT of tight point enclosures on a circle + Cauchy bound from a crude box enclosure on a larger circle), piecewise along ∂S.

## 2026-09-30 23:00 — ladder (R1–R3), `python3 ladder.py` → `logs/ladder.log` (118 s, one process)
- Code: `ivc.py` (complex boxes over mp.iv), `specfun.py` (Stirling Γ, Euler–Maclaurin ζ, h by integration by parts / lower
  series), `xin.py` (Ξ, Φ_n literal (14), tail route, proved tail bound), `winding.py` (Taylor model + boundary walk). iv.prec = 200.
- R1 CERTIFIED: Ξ₁(14.04543957) ∈ +1.347060456146727e−11 (±2e−55 imag. noise), Ξ₁(14.04543959) ∈ −1.704102125314551e−11;
  Ξ₂(39.5324810797) ∈ +3.605517254360067e−21, Ξ₂(39.5324810799) ∈ −4.5934187710153e−21. Tail route (Ξ − Σ_{N<n≤7} Φ_n − tail)
  and literal sum (13) overlap at all four points (16 printed digits agree).
- R2 CERTIFIED: Ξ₁ around Haglund's Appendix zero 20.62534600592171760132974 + 2.697151842339519632505712 i: winding k = 1 at
  r = 1e−3 and at r = 1e−8 (32 pieces each, every piece's enclosure excludes 0; E = 8.7e−26 resp. 5.5e−36 vs min|F| 8.1e−8 resp. 8.2e−13).
  Model zero (non-rigorous) 20.62534600592171685 + 2.69715184233951977 i: Haglund's value good to ~7e−16.
- R3 CERTIFIED control: square 17 + i, r = 1/4 (no zero of Ξ₁ by Haglund's list): winding k = 0 (sum/2π ∈ ±1.3e−5).
- Kernel h used: lower series for n ≤ 7 (small X), integration by parts for n = 7 on some inputs; both routes exercised.

## 2026-09-30 23:04 — N = 27: H1, H4, H2, control; `python3 cert27.py` → `logs/cert27.log` (57 s incl. H2*, one process)
- Same code as the ladder. Tail route Ξ₂₇ = Ξ − Φ₂₈ − Φ₂₉ − Φ₃₀ − T₃₀ (|T₃₀| ≤ 18·900π·e^{−900π}); ζ by E–M with N = 1012,
  m = 94 (remainder ≤ 2.6e−58); h(w) for n = 28–30 by integration by parts (all 732 kernel calls; no fallback needed).
- H1 CERTIFIED: Ξ₂₇(3144.8946) ∈ −1.760194631277516e−1070 (radius ~1e−1121), Ξ₂₇(3144.8947) ∈ +1.068716492261707e−1070.
  Agrees with the brief's Arb literal-sum reference values (−1.76019463128e−1070, +1.06871649226e−1070) to all 12 digits given.
- H4 CERTIFIED: Ξ₂₇(3145.5998) ∈ +1.129756942916642e−1070, Ξ₂₇(3145.5999) ∈ −1.149139153627783e−1070 (reference agrees).
- H2 CERTIFIED: model at c = 3143.2206824215 + 0.3152587994 i (R = 0.1, M_R = 2.09e−1065 from 32 boxes; ρ = 0.002, m = 24, K = 12);
  direct f(c) = D₀ = (1.65573706402 + 2.01786756791 i)e−1076 (consistent); D₁ = (−0.91645674419 − 6.06123185485 i)e−1066.
  Winding k = 1 for r = 1e−3 (32 pieces, min|F| ≥ 5.9e−1069 vs E = 1.4e−1087), 1e−5, 1e−7, 1e−9, 1e−10, 5e−11, 4e−11, 3.7e−11;
  k = 0 at r = 3.5e−11 (zero just outside). Smallest certified half-width at the brief's centre: r = 3.7e−11.
- Control C27 (square at c + 0.01, r = 1e−3, same model): k = 0.
- H3 HOLDS: z₀ ∈ S(r = 1e−3) ⇒ Im z₀ ≥ 0.3142587994 > 0, Re z₀ ≤ 3143.2216824215 < 3144.8946 < real zero of H1.
- Next: refined tiny square around the Newton-refined zero; cross-checks (mpmath reference for Ξ; h by both routes at
  X = 784π; literal sum (13) at N = 27 at the H1/H4 points at ~4600 bits, if affordable); then CERT.md.

## 2026-09-30 23:11 — H2* (refined square) and cross-check launch
- H2* CERTIFIED (in `cert27.py`, same log): second model centred at the Newton zero z* of the first model (ρ = 0.001, m = 40,
  E = 2.1e−1145): winding k = 1 on z* + [−r, r]² for r = 1e−30, 1e−40, 1e−45, 1e−48, so
  z₀ = 3143.220682421536585287281295989417800119257644961983569 + 0.3152587993782148453822863730092717652956513976685290909 i ± 1e−48
  (NOTE §4's 22-digit value agrees).
- Cross-checks running (`crosscheck.py` → `logs/crosscheck.log`): X1 (Ξ boxes contain mpmath's ordinary ζ·Γ values at the four
  H1/H4 points and at c — PASSED); X2 (h at X = 784π by integration by parts vs lower series) — FIRST RUN INVALID as a check:
  the lower-series route was stopped at 190 relative bits against a partial sum that cancels by ~1e135, so its boxes were 1e105×
  too wide (overlap trivially true). Script fixed (relbits = prec − 40); X2 will be re-run. X3 (literal sum (13) at 4400 bits):
  first point Ξ₂₇(3144.8946) literal = −1.760194631277516e−1070 ± 1.8e−1171, identical to the tail route.

## 2026-09-30 23:26 — cross-checks (run 1), selftest, optional H5
- X3 (run 1, `logs/crosscheck-run1-X2invalid.log`, 670 s): the LITERAL sum (13) Σ_{n≤27} Φ_n at 4400 bits (no ζ, no E–M, no (12);
  Φ_n by B3/B4 with Γ by B1) equals the tail route at all four H1/H4 points to 16 digits, boxes overlap, same strict signs:
  3144.8946 → −1.760194631277516e−1070, 3144.8947 → +1.068716492261707e−1070, 3145.5998 → +1.129756942916642e−1070,
  3145.5999 → −1.149139153627783e−1070 (literal radii ≈ 1–2e−1171). H1 and H4 therefore hold by two independent routes.
- `selftest.py` → `logs/selftest.log` (2 s): PASSED (exact Bernoulli, clog_gen 0/15000 violations, Γ/ζ/h/Ξ/Φ_n boxes contain
  mpmath's ordinary values at low height and at the N = 27 height).
- H5 CERTIFIED (`cert_h5.py` → `logs/cert_h5.log`, 17 s): seed chain ξ₂₄ = ξ − ½s(s−1)Σ_{n>24} g_n (tail route; ladder: tail vs
  defining sum overlap at N = 1, 2 at four points). ξ₂₄(½+it) changes sign on (2510.2026, 2510.2027) [+2.813175361644763e−854 →
  −1.65267129214774e−854] and on (2510.7086, 2510.7087) [−3.232811395053649e−854 → +6.141840615423139e−855]; winding number 1 of
  z ↦ ξ₂₄(½+iz) on c5 + [−r, r]², c5 = 2508.2839748053 + 0.3159896243 i, for r = 1e−3, 1e−6, 1e−9, 1e−10; control c5 + 0.01: k = 0.
  Model zero s = 0.184010375695657531105913643468 + 2508.28397480532415320152284309 i (mirror of NOTE's 0.8159896243043424688941 + …).
  So the ordering invariant fails for ξ₂₄ (non-real zero in Q with real part < 2508.285 < 2510.2026 < a real zero).
- Cross-check run 2 launched (fixed X2; X1 and X3 repeated) → `logs/crosscheck.log`.
