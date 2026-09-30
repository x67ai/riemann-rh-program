# SHARED — producer A (Arb / python-flint 0.6.0), unit haglund-cert-s37

## 2026-09-30 22:45 — stage 0: setup
- Read BRIEF.md (all), staircase NOTE.md §4 and §7, Haglund arXiv:0910.5228 text pp. 1–4 (defs (1), (6), (10), (12)–(14),
  Conjecture 1, Prop. 1, Remark 1, table p. 4) and the Appendix p. 15 (zeros of Ξ₁; smallest-modulus non-real zero in Q is
  20.62534600592171760132974 + 2.697151842339519632505712 i).
- Environment: /usr/bin/python3 3.9.6, python-flint 0.6.0 (Arb). caffeinate and the Session-37 watchdogs are running.
- Did NOT read producer-B/. No git commands.
- Plan: hag_core.py (routes L and T, tail bound, winding code) -> ladder.py (R1–R3) -> h1.py -> h2.py -> xcheck.py -> CERT.md.

## 2026-09-30 22:55 — stage 1: ladder R1–R3 PASSED (`ladder.py` -> `ladder.log`, 11.9 s, 256 bits)
- Code: `hag_core.py` = route L (literal (13)–(14)), route T (Xi from acb zeta/gamma minus Phi_{N+1..N+4}, tail n > N+4
  by the proved bound 2U_{M+1}), and the winding code (bisecting cover of ∂S; every piece box's enclosure certified
  in an open half-plane Re>0/Re<0/Im>0/Im<0; increments Arg(F_{k+1}/F_k) with |.| < π checked; sum/2π).
- C0: `acb(x).gamma_upper(s)` = Γ(s, x) confirmed (Γ(1,2) = e^-2, Γ(3,2) = 10e^-2, overlapping balls).
- R1: certified sign changes, BOTH routes: Ξ₁(14.04543957) ∈ +1.347060456e-11 ± 5e-75 (L) / ± 7e-47 (T),
  Ξ₁(14.04543959) ∈ −1.704102125e-11; Ξ₂(39.5324810797) ∈ +3.605517254e-21, Ξ₂(39.5324810799) ∈ −4.593418771e-21.
- R2: Ξ₁, square centre 20.62534600592171760132974 + 2.697151842339519632505712 i (Haglund App. p. 15), r = 1e-10:
  1516 pieces, total ΔArg = 6.28318530717959 ± 3.5e-15, winding = 1 (certified).
- R3: zero-free controls, same code: (a) centre shifted +0.5, r = 0.1 -> winding 0; (b) centre shifted +3e-10, r = 1e-10
  (zero 2e-10 outside) -> winding 0.
