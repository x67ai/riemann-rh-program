#!/usr/bin/env python3
"""producer_arb.py (M2a) -- the Arb/FLINT leg: UNTRUSTED barrier-transcript producer for the
de Bruijn-Newman instance (Polymath15 Table 1 row 2), per results/d1-m2a/SPEC.md v1.0 and
barrier-schema.json.

ROLE AND TRUST STATUS.  One of the two independent producers of the two-producer rule (D-R3;
SPEC section 10, P-1).  UNTRUSTED BY DESIGN: its numbers enter the trusted statement only through
the displayed hypothesis H2-B (SPEC section 8.1).  An accepted transcript is "kernel-checked
modulo the displayed hypotheses H1, H2 (H2-B, H2-A, H-TAIL) and H3 (producers untrusted)" --
never "fully machine-checked".  Producer correctness is CONDITIONAL on Arb's ball contract
(inclusion isotonicity, D-P0 of the M1 leg, results/d1-m1/producer_arb.py) and on the quoted
Polymath15 estimates.

INDEPENDENCE DISCIPLINE (binding).  Shares SPEC.md / barrier-schema.json (and the checker-side
barrier_ref_checker.py for prevalidation) with the mpmath leg and NOTHING else.  The exact
ball->integer helpers are copied from THIS leg's M1 producer (results/d1-m1/producer_arb.py,
derivations D-P1..D-P5, D-P7 there), not from the mpmath leg.

SOURCE.  P15 = fetched/p3-22a4-polymath15-2019-upper-bound-debruijn-newman.pdf (arXiv:1904.12438v2;
PDF page = printed page).  Every formula below was read from the rendered page images this session
(pages 4, 6, 31, 46 rendered with pdftoppm; the rest from pdftotext -layout).  Nothing load-bearing
is from memory (standing order 5).

================================================================================================
TRANSCRIBED FORMULAS (page-exact)
================================================================================================
(6)  p4   M_0(s) = (1/8) (s(s-1)/2) pi^{-s/2} sqrt(2 pi) exp((s/2 - 1/2) Log(s/2) - s/2),
          Log = principal branch (cut (-inf,0], Im in (-pi,pi]).
(7)  p4   log M_0(s) = Log s + Log(s-1) - (s/2) log pi + log(sqrt(2 pi)/16) + (s/2 - 1/2) Log(s/2) - s/2
          [check: exp of (7) = s(s-1) pi^{-s/2} (sqrt(2pi)/16) exp(...) = (1/8)(s(s-1)/2) pi^{-s/2} sqrt(2pi) exp(...) = (6)].
(8)-(9) p4  alpha(s) = (log M_0)'(s) = 1/(2s) + 1/(s-1) + (1/2) Log(s/(2 pi)).
(10) p4   M_t(s) = exp((t/4) alpha(s)^2) M_0(s).
(11) p4   B_t(x+iy) = M_t((1+y-ix)/2) = M_t(s_+),  s_+ := (1 - i z)/2 for z = x+iy.
(14)-(19) p6 (rendered): f_t(x+iy) = sum_{n<=N} b_n^t / n^{s_*} + gamma sum_{n<=N} n^y b_n^t / n^{conj(s_*) + kappa},
          b_n^t = exp((t/4) log^2 n);  gamma = M_t((1-y+ix)/2)/M_t((1+y-ix)/2) = M_t(s_-)/M_t(s_+),
          s_- := (1 + i z)/2 = 1 - s_+;  s_* = s_+ + (t/2) alpha(s_+);
          kappa = (t/2)(alpha((1-y+ix)/2) - alpha((1+y+ix)/2)) = (t/2)(alpha(s_-) - alpha(conj s_+));
          N = floor(sqrt(x/(4 pi) + t/16)).
     p46 (Lemma 8.4 proof, rendered): s_** := conj(s_*) - y + kappa = (1-y+ix)/2 + (t/2) alpha((1-y+ix)/2)
          = s_- + (t/2) alpha(s_-), and (92): f_t = sum b_n^t / n^{s_*} + gamma sum b_n^t / n^{s_**}.
     DERIVATION D-A1 (the form implemented).  (92) is the form used here.  Check against (14):
          conj(s_*) + kappa - y = conj(s_+) + (t/2) alpha(conj s_+) + (t/2)(alpha(s_-) - alpha(conj s_+)) - y
          = (conj(s_+) - y) + (t/2) alpha(s_-) = s_- + (t/2) alpha(s_-)  since conj(s_+) - y = (1+y+ix)/2 - y = s_-.
          [alpha(conj s) = conj(alpha(s)) was NOT needed.]  So n^y / n^{conj(s_*)+kappa} = 1/n^{s_**} and (14) = (92).
          (92) is also exactly (A_{t,N} + B_{t,N})/B_t of Corollary 6.5 (p30) divided by M_t(s_+), which is what
          Theorem 1.3's proof (p30, (69)-(70)) bounds.  f_t is holomorphic in z for fixed N (p6, p46).
(20) p6   |gamma| <= e^{0.02 y} (x/(4 pi))^{-y/2}.
(21) p6   Re s_* >= (1+y)/2 + (t/4) log(x/(4 pi)) - (t/(2x^2)) (1 - 3y + 4y(1+y)/x^2)_+.   [not used: Re s_* is
          computed as a ball from the definition; (21) is a consistency check only]
(22) p6   |kappa| <= t y / (2 (x - 6)).
Prop 6.6 p31 (rendered):
   (iv)  e_A <= |gamma| N^{|kappa|} sum_{n<=N} n^y b_n^t / n^{Re s_*} ( exp( ((t^2/16) log^2(x/(4 pi n^2)) + 0.626)/(x - 6.66) ) - 1 )
   (v)   e_B <= sum_{n<=N} b_n^t / n^{Re s_*} ( exp( ((t^2/16) log^2(x/(4 pi n^2)) + 0.626)/(x - 6.66) ) - 1 )
   (vi)  e_{C,0} <= (x/4pi)^{-(1+y)/4} exp(-(t/16) log^2(x/4pi) + (3|log(x/4pi) + i pi/2| + 3.58)/(x - 8.52))
                    (1 + 1.24 (3^y + 3^{-y})/(N - 0.125) + 6.92/(x - 12)).
   Theorem 1.3 (13), p6: H_t/B_t = f_t + O_<=(e_A + e_B + e_{C,0}) in the region (5) (p3): 0 < t <= 1/2, 0 <= y <= 1, x >= 200.
(80) p38  x_N <= x < x_{N+1},  x_N := 4 pi N^2 - pi t/4.
(84) p40  delta_1 := ((t^2/16) log^2(x/(4 pi)) + 0.626)/(x - 6.66)   [the n = 1 case of (iv)/(v)'s exponent].

================================================================================================
DERIVATIONS (each numbered; the producer relies on nothing else)
================================================================================================
D-A2 (the defect bound E, SPEC P-6, D-2.4).  For 1 <= n <= N:  4 pi n^2 <= 4 pi N^2 <= x + pi t/4 (by (19):
  N^2 <= x/(4 pi) + t/16), so x/(4 pi n^2) >= 1/(1 + pi t/(4x)) and x/(4 pi n^2) <= x/(4 pi); hence
  |log(x/(4 pi n^2))| <= log(x/(4 pi)) as soon as log(1 + pi t/(4x)) <= log(x/(4pi)), true for x >= 200.  So the
  exponent in (iv)/(v) is <= delta_1 for every n, and (exp(.)-1) <= exp(delta_1) - 1.  Next, with
  Re s_** = Re s_* - y + Re kappa (real parts of s_** = conj(s_*) - y + kappa), n^{y - Re s_*} = n^{-Re s_** + Re kappa}
  <= n^{-Re s_**} N^{|kappa|}.  Therefore
     e_A + e_B <= (exp(delta_1) - 1) [ F + N^{2|kappa|} G ],   F := sum b_n^t n^{-Re s_*},  G := |gamma| sum b_n^t n^{-Re s_**}.
  e_{C,0}: the D-2.4 weld of SPEC section 2.4 (1 + a + b <= (1+a) e^b, 1/(x-8.52) <= 1/(x-12) for x > 12):
     e_{C,0} <= (x/4pi)^{-(1+y)/4} exp(-(t/16) log^2(x/4pi) + (3|log(x/4pi) + i pi/2| + 10.50)/(x - 12)) (1 + 1.24 (3^y + 3^{-y})/(N - 0.125)).
  Uniformity over a box: every factor is evaluated by ball arithmetic with the box's coordinate INTERVALS as inputs
  (Arb's inclusion isotonicity, D-P0), so the ball's upper bound dominates the supremum; F and G are bounded by D-A9.
D-A3 (sup of the two Dirichlet sums over the box, (20) used; SPEC section 5.2 monotonicities).  On the box
  B = [x1,x2] x [y1,y2] and 0 <= t <= t0, with a_+ := inf_B Re alpha(s_+(z)), a_- := inf_B Re alpha(s_-(z)) (ball lower bounds):
     Re s_*(z,t) = (1+y)/2 + (t/2) Re alpha(s_+(z)) >= (1+y1)/2 + (t/2) a_+ =: sigma_+(t),
     |gamma(z)| n^{-Re s_**(z,t)} <= e^{0.02 y} (x/4pi)^{-y/2} n^{-(1-y)/2 - (t/2) a_-}
                                   = e^{0.02 y} (n/(x/4pi))^{y/2} n^{-1/2 - (t/2) a_-}
                                   <= e^{0.02} (x1/4pi)^{-y1/2} n^{-(1-y1)/2 - (t/2) a_-}      (n <= N < x/(4pi) makes the
                                      base < 1, so the power is decreasing in y and largest at y = y1; e^{0.02y} <= e^{0.02}).
  Hence for k >= 0:  sup_B sum_n b_n^t n^{-Re s_*} log^k n <= R_k^+(t) := sum_n n^{-(1+y1)/2} exp(t r_n^+) log^k n,
       r_n^+ := (1/4) log^2 n - (1/2) a_+ log n   [b_n^t n^{-(t/2) a_+} = exp(t r_n^+)],
  and sup_B |gamma| sum_n b_n^t n^{-Re s_**} log^k n <= R_k^-(t) := e^{0.02} (x1/4pi)^{-y1/2} sum_n n^{-(1-y1)/2} exp(t r_n^-) log^k n,
       r_n^- := (1/4) log^2 n - (1/2) a_- log n.
D-A9 (monotonicity in t).  If log N <= 2 a_+ (resp. 2 a_-) then r_n^{+-} <= 0 for all 1 <= n <= N, so every term of
  R_k^{+-}(t) is non-increasing in t and sup_{t in [tau, tau']} R_k(t) = R_k(tau).  The producer CHECKS log N <= 2 a_{+-}
  as certified ball inequalities (instance: log 630783 = 13.35 against 2 a = 26.7).
D-A4 (the two-variable Taylor evaluator on the box; the "stored sum").  Fix the box centre z_c and time centre t_c, and
  write z = z_c + delta, t = t_c + tau.  With alpha_c^+ := alpha(s_+(z_c)) (a tight ball) and d^+(z) := alpha(s_+(z)) - alpha_c^+,
     b_n^t n^{-s_*(z,t)} = n^{-s_+(z_c)} exp(i delta L/2) exp(t q_n^+) exp(-(t/2) d^+(z) L),     L := log n,
     q_n^+ := L^2/4 - alpha_c^+ L/2,                                                                    [since s_+(z) = s_+(z_c) - i delta/2]
  and likewise for s_** with s_-(z) = s_-(z_c) + i delta/2, alpha_c^- := alpha(s_-(z_c)), q_n^-, d^-(z), and exp(-i delta L/2).
  Put c_n^{+-} := n^{-s_{+-}(z_c)} exp(t_c q_n^{+-}) and the MOMENTS M_m^{+-} := sum_{n<=N} c_n^{+-} L^m (m <= K + 2J), computed once.
  Then, with (q_n)^j = L^j (L/4 - alpha_c/2)^j = sum_{i<=j} C(j,i) 4^{-i} (-alpha_c/2)^{j-i} L^{j+i},
     S_1(z,t) := sum_n b_n^t n^{-s_*} = P^+(delta,tau) + Rem^+ + Eps^+,
     P^+ := sum_{k<=K} sum_{j<=J} (i delta/2)^k tau^j / (k! j!) M_{k,j}^+,   M_{k,j}^+ := sum_{i<=j} C(j,i) 4^{-i} (-alpha_c^+/2)^{j-i} M_{k+j+i}^+,
  where Rem^+ is the truncation remainder and Eps^+ the d^+-correction, bounded in D-A5/D-A6.  Same for S_2 with the
  minus data and (-i delta/2)^k.  Per seam tau the coefficients A_k(tau) := sum_j tau^j/j! M_{k,j} collapse the tau-sum;
  per point the delta-sum is a Horner evaluation.  The z- and t-derivatives are the derivatives of the polynomial
  (with D-A6's corrections); the tau-derivative uses sum_{j>=1} tau^{j-1}/(j-1)! M_{k,j}.
D-A5 (truncation remainders).  For complex a, b and K, J >= 0:
     e^{a+b} - T_K(a) T_J(b) = e^a (e^b - T_J(b)) + T_J(b)(e^a - T_K(a)),  |T_J(b)| <= e^{|b|},
     |e^b - T_J(b)| = |sum_{m>J} b^m/m!| <= |b|^{J+1}/(J+1)! sum_{i>=0} |b|^i/i! = |b|^{J+1} e^{|b|}/(J+1)!   [(J+1+i)! >= (J+1)! i!],
  so |e^{a+b} - T_K(a)T_J(b)| <= e^{|a|+|b|} ( |a|^{K+1}/(K+1)! + |b|^{J+1}/(J+1)! ).  With a = i delta L/2, b = tau q_n,
  U := |delta| L_N/2, V := |tau| Q (Q := max_n |q_n|, L_N := log N; both certified upper bounds), and C := sum_n |c_n|:
     |Rem| <= C e^{U+V} ( U^{K+1}/(K+1)! + V^{J+1}/(J+1)! ).
  Derivatives: the delta-derivative multiplies each term by i L/2 and truncates at K-1; the tau-derivative by q_n and
  truncates at J-1; hence |Rem_delta| <= C (L_N/2) e^{U+V}(U^K/K! + V^{J+1}/(J+1)!),  |Rem_tau| <= C Q e^{U+V}(U^{K+1}/(K+1)! + V^J/J!).
D-A6 (the d-corrections).  Let dA^{+-} := sup_B |alpha(s_{+-}(z)) - alpha_c^{+-}| (certified from the box ball).  For
  w := -(t/2) d(z) L, |w| <= (t0/2) dA L_N =: w_max and |e^w - 1| <= |w| e^{|w|} <= eta := w_max e^{w_max}.  Since the
  true term equals the expanded term times e^w, and the sum of the moduli of the expanded terms as well as of the true
  terms is <= R_0(t) (D-A3, both exponents lie in the range covered by sigma(t)), |Eps| <= eta R_0(t).  For the
  derivatives: d/dz of the true term carries the extra factor (1 + (t/2) alpha'(s_+(z))) on i L/2, so
  |S_1' - dP^+/ddelta| <= (eta + (t0/2) A1') (1/2) R_1(t) + |Rem_delta| with A1' := sup_B |alpha'(s_+)|; d/dt of the true term
  is the term times q_n(z) = q_n^+ - (1/2) d(z) L, so |dS_1/dt - dP^+/dtau| <= eta Q R_0(t) + (1/2) dA L_N ... more precisely
  eta Q R_0(t) + (1/2) dA R_1(t) + |Rem_tau|.  The minus-sum corrections are multiplied by |gamma|; D-A3's R^- already carries |gamma|.
D-A7 (gamma on the box).  Lambda(z) := log M_0(s_-(z)) - log M_0(s_+(z)) by (7) is holomorphic on the box (Im s_+ = -x/2 < 0,
  Im s_- = x/2 > 0: every Log argument is off the cut), and gamma = exp(Lambda(z) + t w(z)), w(z) := (alpha(s_-)^2 - alpha(s_+)^2)/4
  (from (10),(16)).  With ds_-/dz = i/2, ds_+/dz = -i/2 and (8): Lambda' = (i/2)(alpha(s_-) + alpha(s_+)),
  Lambda'' = -(1/4)(alpha'(s_-) - alpha'(s_+)),  w' = (i/4)(alpha(s_-)alpha'(s_-) + alpha(s_+)alpha'(s_+)),
  w'' = -(1/8)((alpha'(s_-)^2 + alpha(s_-)alpha''(s_-)) - (alpha'(s_+)^2 + alpha(s_+)alpha''(s_+))).
  Taylor with remainder along the segment z_c -> z (convex box): Lambda(z) in Lambda_c + Lambda'_c delta + ball((1/2) sup|Lambda''| |delta|^2),
  w(z) in w_c + ball(sup|w'| |delta|); d/dz log gamma in Lambda'_c + ball(sup|Lambda''| |delta| + t sup|w'|); d/dt log gamma = w(z).
  Box-uniform: |l| := sup|d/dz log gamma| <= |Lambda'_c| + sup|Lambda''| rho + t0 sup|w'|,  |l_z| <= sup|Lambda''| + t0 sup|w''|,
  |w| <= sup_B |w|, |w_z| <= sup|w'|, with rho := max_B |delta| (all sups as ball upper bounds over the box ball).
D-A8 (box-uniform second derivatives; the calculus of Lemma 8.4's proof, p46-48, with the box balls in place of the paper's
  constants).  Terms T_n = b_n^t n^{-s_*}: d s_*/dz = (-i/2)(1 + (t/2) alpha'(s_+)), |.| <= A1 := (1/2)(1 + (t0/2) A1');
  d^2 s_*/dz^2 = -(t/8) alpha''(s_+), |.| <= A2 := (t0/8) A2'' (A2'' := sup|alpha''(s_+)|);  dT/dt = T q, q = L^2/4 - alpha(s_+) L/2,
  |q| <= L^2/4 + |alpha|_B L/2;  d q/dz = (i/4) L alpha'(s_+).  Hence with R_k = R_k^+(t):
     |S_1,zz| <= A1^2 R_2 + A2 R_1;  |S_1,tt| <= R_4/16 + |alpha|_B R_3/4 + |alpha|_B^2 R_2/4;  |S_1,zt| <= A1 (R_3/4 + |alpha|_B R_2/2) + A1' R_1/4.
  For gamma S_2 (Leibniz; R^- carries |gamma|; A1^-, A2^- from alpha'(s_-), alpha''(s_-)):
     |(gamma S_2)_zz| <= (|l|^2 + |l_z|) R_0^- + 2 |l| A1^- R_1^- + A1^{-2} R_2^- + A2^- R_1^-,
     |(gamma S_2)_tt| <= |w|^2 R_0^- + 2|w| (R_2^-/4 + |alpha^-|_B R_1^-/2) + R_4^-/16 + |alpha^-|_B R_3^-/4 + |alpha^-|_B^2 R_2^-/4,
     |(gamma S_2)_zt| <= (|l||w| + |w_z|) R_0^- + |l| (R_2^-/4 + |alpha^-|_B R_1^-/2) + |w| A1^- R_1^- + A1^- (R_3^-/4 + |alpha^-|_B R_2^-/2) + A1'^- R_1^-/4.
  D_zz, D_tt, D_zt := the sums of the S_1 and gamma S_2 bounds, valid on B x [tau, t0] when evaluated at tau (D-A9).
D-A10 (hull boxes, SPEC P-4).  For z on the closed segment of half-length h and midpoint z_m (inside the convex box), Taylor's
  theorem for holomorphic f along the segment: |f(z) - f(z_m) - f'(z_m)(z - z_m)| <= (1/2) D_zz |z - z_m|^2, hence
  |f(z) - f(z_m)| <= |f'(z_m)| h + D_zz h^2/2 =: r.  With f(z_m), f'(z_m) enclosed by balls, the box [Re f(z_m) -+ r] x [Im f(z_m) -+ r]
  (exact rational arithmetic on the ball's mid/rad, outward at scale K by D-P2) encloses f on the whole segment: the H2-B row
  quantifier of SPEC section 4.2.  Argument rows: M1's D-P5 (same-rotation endpoint atan2) on the endpoint balls.
D-A11 (the displacement D, SPEC P-8 / section 4.5).  For z on segment k and tau <= t <= tau':
     |g_t(z) - g_tau(z)| <= |g_t - f_t| + |f_t(z) - f_tau(z)| + |f_tau - g_tau| <= E(t) + E(tau) + (t - tau) sup |d f/dt|
  (Theorem 1.3 at both times, mean value theorem in t), and for t' in [tau, tau']:
     |f_t(z, t') - f_t(z_m, tau)| <= D_zt |z - z_m| + D_tt (t' - tau)  (mean value along (z_m,tau)->(z,tau)->(z,t') inside B x [tau,tau']).
  So with Mt := max_k ( |f_t(z_{m,k}, tau)| + D_zt h_k ) and E_p := sup_{prism} E (= E at tau, D-A9 + delta_1 at t0):
     D/K := 2 E_p + Delta ( Mt + D_tt Delta ),  Delta := tau' - tau,
  and the gate C-B12 with E := ceil(K E_p) reads 3 E_p + Delta(Mt + D_tt Delta) < Fn/Fd.  Delta is chosen (rounded DOWN to an
  exact rational) so that this holds with a margin; the integer gate is re-verified before writing.
D-A12 (Theorem 1.3 at t = 0, SPEC P-7).  Theorem 1.3 is stated for 0 < t <= 1/2.  For fixed z with Im z > 0: H_t(z) -> H_0(z)
  as t -> 0+ by dominated convergence (|e^{tu^2} Phi(u) cos(zu)| <= e^{u^2/2} |Phi(u)| e^{|Im z| u}, integrable, P15 p1-2:
  Phi decays super-exponentially); B_t(z) -> B_0(z) (continuity of (10) in t, B_0 =/= 0); f_t -> f_0 (finite sum, continuous
  in t); the majorant e_A + e_B + e_{C,0} of D-A2 is continuous in t at 0 (with delta_1 taken at t0 it is even constant).
  Passing to the limit in the closed inequality |H_t/B_t - f_t| <= majorant gives it at t = 0.  Recorded in prism 0's
  producer.comment as this leg's discharge of P-7.
D-A13 (N constant on the box, SPEC P-3).  N(x,t) = floor(sqrt(x/4pi + t/16)) is non-decreasing in x and in t; the producer
  certifies sqrt(x/4pi + t/16) in (N0, N0+1) at the two extreme corners (x1, 0) and (x2, t0) by ball arithmetic, hence
  N = N0 on the closed box for all 0 <= t <= t0 and f_t is the same finite sum (holomorphic, p6) throughout.

Exact arithmetic discipline (M1 D-P1/D-P2): every ball is converted to an exact rational interval [mid-rad, mid+rad]
from the exact dyadic mid/rad, and integers are obtained by floor/ceil on Fractions; lower()/upper() are used only as
a redundant bracketing assert.  No float enters any checked number.

USAGE
  python3 producer_arb.py selftest                       # alpha/box constants, N-constancy (D-A13), moment self-consistency
  python3 producer_arb.py crosscheck --points 8          # Taylor evaluator vs direct summation at the instance (D-A4 check)
  python3 producer_arb.py instance --out-dir transcripts [--max-seconds S] [--max-prisms J] [--resume]
  python3 producer_arb.py point --x N/D --y N/D --t N/D  # direct f_t ball + E at one point (validation hook)
"""

import argparse
import datetime
import json
import math
import os
import subprocess
import sys
import time
from fractions import Fraction

import flint
from flint import acb, arb, ctx, fmpq

HERE = os.path.dirname(os.path.abspath(__file__))
PREC = 320          # bits; the moment sums lose ~45 bits to the phase x/2 * log n ~ 3e13 and ~60 bits to the
                    # alternating (q_n)^j expansion (D-A4); 320 leaves > 200 bits, far beyond the 1e-12 targets.
ctx.prec = PREC

TRUST_LABEL = ("kernel-checked modulo the displayed hypotheses H1, H2 (H2-B, H2-A, H-TAIL) and H3 "
               "(producers untrusted)")

# ---------------------------------------------------------------- instance (SPEC section 9, exact)
X_INST = 5000000194858
T0_INST = Fraction(93, 500)
Y0_INST = Fraction(16733, 100000)
N0_INST = 630783


class ProducerError(Exception):
    pass


# ---------------------------------------------------------------- exact ball <-> rational (M1 leg, D-P1/D-P2/D-P3/D-P4)

def _dyadic(man_exp_pair):
    m, e = int(man_exp_pair[0]), int(man_exp_pair[1])
    if e >= 0:
        return Fraction(m * (1 << e))
    return Fraction(m, 1 << (-e))


def ball_interval(x):
    """arb ball -> exact rational interval [mid - rad, mid + rad] (D-P1)."""
    m, r = x.mid(), x.rad()
    if not (m.is_exact() and r.is_exact()):
        raise ProducerError("mid/rad not exact -- non-finite ball?")
    mv, rv = _dyadic(m.man_exp()), _dyadic(r.man_exp())
    if rv < 0:
        raise ProducerError("negative radius")
    return (mv - rv, mv + rv)


def upper(x):
    """Exact rational upper bound of an arb ball."""
    return ball_interval(x)[1]


def lower(x):
    return ball_interval(x)[0]


def floor_frac(q):
    return q.numerator // q.denominator


def ceil_frac(q):
    return -((-q.numerator) // q.denominator)


def out_int_bounds_frac(lo, hi, scale):
    return floor_frac(lo * scale), ceil_frac(hi * scale)


def out_int_bounds(x, scale):
    """Integer (lo, hi) with lo <= scale*x_true <= hi for every x_true in the ball (D-P2), cross-checked
    against the library's directed lower()/upper()."""
    lo, hi = ball_interval(x)
    ilo, ihi = floor_frac(lo * scale), ceil_frac(hi * scale)
    dlo, dhi = ball_interval(x.lower())[0], ball_interval(x.upper())[1]
    if not (dlo <= lo and hi <= dhi):
        raise ProducerError("lower()/upper() inconsistent with mid/rad interval")
    return ilo, ihi


def rat_ball(q):
    """Ball containing the exact rational q, containment re-verified (D-P3)."""
    q = Fraction(q)
    b = arb(fmpq(q.numerator, q.denominator))
    lo, hi = ball_interval(b)
    if not (lo <= q <= hi):
        raise ProducerError(f"rat_ball containment failed for {q}")
    return b


def hull_ball(a, b):
    """Ball containing the whole rational interval [min(a,b), max(a,b)] (D-P4)."""
    u = rat_ball(a).union(rat_ball(b))
    lo, hi = ball_interval(u)
    if not (lo <= min(a, b) and max(a, b) <= hi):
        raise ProducerError("hull containment failed")
    return u


def cpoint(x, y):
    return acb(rat_ball(x), rat_ball(y))


def to_arb(t):
    """Exact rational (or arb) -> arb ball."""
    return t if isinstance(t, arb) else rat_ball(Fraction(t))


def frac_json(q):
    q = Fraction(q)
    return {"n": str(q.numerator), "d": str(q.denominator)}


def absup(z):
    """Exact rational upper bound of |z| for an acb (or arb) ball."""
    return upper(abs(z))


def certified_lt(a, b):
    """True only if a < b is certain (Arb's certified comparison)."""
    return bool(a < b)


# ---------------------------------------------------------------- Polymath15 building blocks (6)-(11)

def PI():
    return arb.pi()


def alpha(s):
    """(9): 1/(2s) + 1/(s-1) + (1/2) Log(s/(2 pi))."""
    return 1 / (2 * s) + 1 / (s - 1) + (s / (2 * PI())).log() / 2


def alpha1(s):
    """alpha'(s) = -1/(2 s^2) - 1/(s-1)^2 + 1/(2 s)  (termwise derivative of (9))."""
    return -1 / (2 * s * s) - 1 / ((s - 1) * (s - 1)) + 1 / (2 * s)


def alpha2(s):
    """alpha''(s) = 1/s^3 + 2/(s-1)^3 - 1/(2 s^2)."""
    return 1 / (s * s * s) + 2 / ((s - 1) * (s - 1) * (s - 1)) - 1 / (2 * s * s)


def logM0(s):
    """(7): Log s + Log(s-1) - (s/2) log pi + log(sqrt(2 pi)/16) + (s/2 - 1/2) Log(s/2) - s/2."""
    pi = PI()
    return (s.log() + (s - 1).log() - (s / 2) * pi.log() + ((2 * pi).sqrt() / 16).log()
            + (s / 2 - arb(1) / 2) * (s / 2).log() - s / 2)


def M0(s):
    """(6) literally (product form, as Defs.lean's M0): used for B_t in the validation hook only."""
    pi = PI()
    return (acb(1) / 8) * (s * (s - 1) / 2) * (acb(pi) ** (-s / 2)) * (2 * pi).sqrt() \
        * ((s / 2 - arb(1) / 2) * (s / 2).log() - s / 2).exp()


def Mt(t, s):
    """(10)."""
    return (to_arb(t) / 4 * alpha(s) ** 2).exp() * M0(s)


def s_plus(z):
    return (1 - acb(0, 1) * z) / 2


def s_minus(z):
    return (1 + acb(0, 1) * z) / 2


def Bt_point(z, t):
    """(11): B_t(z) = M_t(s_+(z)).  t an arb."""
    return Mt(t, s_plus(z))


def log_gamma(z, t):
    """log gamma = Lambda(z) + t w(z)  (D-A7)."""
    sp, sm = s_plus(z), s_minus(z)
    return logM0(sm) - logM0(sp) + (to_arb(t) / 4) * (alpha(sm) ** 2 - alpha(sp) ** 2)


def N_of(x, t):
    """(19) with certification that the ball does not straddle an integer (D-A13)."""
    v = (rat_ball(x) / (4 * PI()) + rat_ball(t) / 16).sqrt()
    lo, hi = ball_interval(v)
    nlo, nhi = floor_frac(lo), floor_frac(hi)
    if nlo != nhi:
        raise ProducerError(f"N(x,t) undecided: sqrt ball [{float(lo)}, {float(hi)}] straddles an integer")
    return nlo


# ---------------------------------------------------------------- direct evaluator (any x): D-A1

def ft_direct(z, t, N, want_sums=False):
    """f_t(z) by direct summation of (92) with s_* = s_+ + (t/2) alpha(s_+), s_** = s_- + (t/2) alpha(s_-).
    Returns (f, gamma, S1, S2, F, G) where F = sum b_n n^{-Re s_*}, G = |gamma| sum b_n n^{-Re s_**} (for D-A2)."""
    t = to_arb(t)
    sp, sm = s_plus(z), s_minus(z)
    sstar = sp + (t / 2) * alpha(sp)
    sstar2 = sm + (t / 2) * alpha(sm)
    gam = log_gamma(z, t).exp()
    S1 = acb(0); S2 = acb(0); F = arb(0); G = arb(0)
    re1, re2 = sstar.real, sstar2.real
    for n in range(1, N + 1):
        L = arb(n).log()
        bt = (t / 4 * L * L)
        S1 += (-sstar * L + bt).exp()
        S2 += (-sstar2 * L + bt).exp()
        F += (-re1 * L + bt).exp()
        G += (-re2 * L + bt).exp()
    G = abs(gam) * G
    return S1 + gam * S2, gam, S1, S2, F, G


def E_bound(xb, yb, tb, N, F_sup, G_sup):
    """D-A2: exact-rational UPPER bound of e_A + e_B + e_{C,0} on the box with coordinate balls xb, yb, tb (arb intervals),
    given upper bounds F_sup, G_sup (arb) of the two Dirichlet sums over the box."""
    pi = PI()
    q = xb / (4 * pi)
    lq = q.log()
    # e_{C,0}, the 10.50 form (SPEC D-2.4)
    modterm = abs(acb(lq, pi / 2))
    eC0 = (q ** (-(1 + yb) / 4)) * (-(tb / 16) * lq * lq + (3 * modterm + arb(21) / 2) / (xb - 12)).exp() \
        * (1 + arb("1.24") * (arb(3) ** yb + arb(3) ** (-yb)) / (arb(N) - arb(1) / 8))
    # e_A + e_B
    delta1 = ((tb * tb / 16) * lq * lq + arb("0.626")) / (xb - arb("6.66"))
    kap = tb * yb / (2 * (xb - 6))
    eAB = (delta1.exp() - 1) * (F_sup + (arb(N) ** (2 * kap)) * G_sup)
    tot = eC0 + eAB
    return upper(tot), upper(eC0), upper(eAB)


# ---------------------------------------------------------------- the box evaluator (D-A3..D-A9)

class BoxEvaluator:
    """Taylor/moment evaluator of f_t, df/dz, df/dt on the closed box [x1,x2] x [y1,y2] x [0,t0] with N fixed."""

    def __init__(self, x1, x2, y1, y2, t0, N, K=36, J=40, log=print):
        self.x1, self.x2, self.y1, self.y2 = map(Fraction, (x1, x2, y1, y2))
        self.t0 = Fraction(t0); self.N = N; self.K = K; self.J = J; self.log = log
        self.zc = ((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2)
        self.tc = self.t0 / 2
        self.rho = None  # max |delta| over the box (Fraction upper bound), set below
        zc = cpoint(*self.zc)
        # box hull ball
        ZB = acb(hull_ball(self.x1, self.x2), hull_ball(self.y1, self.y2))
        spB, smB = s_plus(ZB), s_minus(ZB)
        spc, smc = s_plus(zc), s_minus(zc)
        # centre values (tight balls)
        self.spc, self.smc = spc, smc
        self.alc_p, self.alc_m = alpha(spc), alpha(smc)
        # box balls and sups
        alB_p, alB_m = alpha(spB), alpha(smB)
        self.a_p = lower(alB_p.real); self.a_m = lower(alB_m.real)         # inf Re alpha (D-A3)
        self.abs_al_p = absup(alB_p); self.abs_al_m = absup(alB_m)        # sup |alpha|
        self.dA_p = absup(alB_p - self.alc_p); self.dA_m = absup(alB_m - self.alc_m)   # D-A6
        self.A1p_p = absup(alpha1(spB)); self.A1p_m = absup(alpha1(smB))  # sup |alpha'|
        self.A2p_p = absup(alpha2(spB)); self.A2p_m = absup(alpha2(smB))  # sup |alpha''|
        t0b = rat_ball(self.t0)
        self.A1_p = Fraction(1, 2) * (1 + self.t0 / 2 * self.A1p_p)       # D-A8
        self.A1_m = Fraction(1, 2) * (1 + self.t0 / 2 * self.A1p_m)
        self.A2_p = self.t0 / 8 * self.A2p_p
        self.A2_m = self.t0 / 8 * self.A2p_m
        # gamma data (D-A7)
        self.Lam_c = logM0(smc) - logM0(spc)
        self.Lam1_c = acb(0, 1) / 2 * (self.alc_m + self.alc_p)
        self.w_c = (self.alc_m ** 2 - self.alc_p ** 2) / 4
        Lam2_B = -(alpha1(smB) - alpha1(spB)) / 4
        w1_B = acb(0, 1) / 4 * (alB_m * alpha1(smB) + alB_p * alpha1(spB))
        w2_B = -(alpha1(smB) ** 2 + alB_m * alpha2(smB) - alpha1(spB) ** 2 - alB_p * alpha2(spB)) / 8
        wB = (alB_m ** 2 - alB_p ** 2) / 4
        self.sup_Lam2 = absup(Lam2_B); self.sup_w1 = absup(w1_B); self.sup_w2 = absup(w2_B)
        self.sup_w = absup(wB)
        # rho = max |z - z_c| over the box (corners)
        hx, hy = (self.x2 - self.x1) / 2, (self.y2 - self.y1) / 2
        self.rho = upper((rat_ball(hx) ** 2 + rat_ball(hy) ** 2).sqrt())
        self.sup_l = absup(self.Lam1_c) + self.sup_Lam2 * self.rho + self.t0 * self.sup_w1
        self.sup_lz = self.sup_Lam2 + self.t0 * self.sup_w2
        # D-A3 prefactor for R^-
        self.pref_m = (arb("0.02")).exp() * (rat_ball(self.x1) / (4 * PI())) ** (-rat_ball(self.y1) / 2)
        self.L_N = arb(N).log()
        # D-A9 check: log N <= 2 a_+-
        if not (certified_lt(self.L_N, 2 * rat_ball(self.a_p)) and certified_lt(self.L_N, 2 * rat_ball(self.a_m))):
            raise ProducerError("D-A9 monotonicity precondition log N <= 2 inf Re alpha fails")
        self.log(f"[box] a+={float(self.a_p):.6f} a-={float(self.a_m):.6f} |alpha+|<={float(self.abs_al_p):.4f} "
                 f"dA+={float(self.dA_p):.3e} dA-={float(self.dA_m):.3e} A1'+={float(self.A1p_p):.3e} A2''+={float(self.A2p_p):.3e} "
                 f"rho={float(self.rho):.4f} sup|l|={float(self.sup_l):.4f} sup|w|={float(self.sup_w):.4f} sup|w'|={float(self.sup_w1):.3e}")
        self._moments()
        self._tables()

    # ---- the one pass over n (D-A4, D-A3)
    def _moments(self):
        K, J, N = self.K, self.J, self.N
        Mmax = K + 2 * J
        Wmax = 4 + 2 * J
        tc = rat_ball(self.tc)
        spc, smc = self.spc, self.smc
        qp_coef = -self.alc_p / 2; qm_coef = -self.alc_m / 2      # q_n = L^2/4 + coef * L
        rp_coef = -rat_ball(self.a_p) / 2; rm_coef = -rat_ball(self.a_m) / 2
        sig_p0 = rat_ball((1 + self.y1) / 2); sig_m0 = rat_ball((1 - self.y1) / 2)
        Mp = [acb(0) for _ in range(Mmax + 1)]; Mm = [acb(0) for _ in range(Mmax + 1)]
        Wp = [arb(0) for _ in range(Wmax + 1)]; Wm = [arb(0) for _ in range(Wmax + 1)]
        Cp = arb(0); Cm = arb(0)
        Qp = arb(0); Qm = arb(0); Rp = arb(0); Rm = arb(0)
        t_start = time.time()
        for n in range(1, N + 1):
            L = arb(n).log(); L2 = L * L
            qp = L2 / 4 + qp_coef * L; qm = L2 / 4 + qm_coef * L
            rp = L2 / 4 + rp_coef * L; rm = L2 / 4 + rm_coef * L
            cp = (-spc * L + tc * qp).exp(); cm = (-smc * L + tc * qm).exp()
            wp = (-sig_p0 * L + tc * rp).exp(); wm = (-sig_m0 * L + tc * rm).exp()
            Cp += abs(cp); Cm += abs(cm)
            aq = abs(qp)
            if not certified_lt(aq, Qp): Qp = Qp.union(aq) if n > 1 else aq
            aq = abs(qm)
            if not certified_lt(aq, Qm): Qm = Qm.union(aq) if n > 1 else aq
            ar = abs(rp)
            if not certified_lt(ar, Rp): Rp = Rp.union(ar) if n > 1 else ar
            ar = abs(rm)
            if not certified_lt(ar, Rm): Rm = Rm.union(ar) if n > 1 else ar
            p = arb(1)
            for m in range(Wmax + 1):
                Mp[m] += cp * p; Mm[m] += cm * p
                Wp[m] += wp * p; Wm[m] += wm * p
                p = p * L
            for m in range(Wmax + 1, Mmax + 1):
                Mp[m] += cp * p; Mm[m] += cm * p
                p = p * L
            if n % 100000 == 0:
                self.log(f"[moments] n={n}/{N} {time.time()-t_start:.1f}s")
        self.Mp, self.Mm, self.Wp, self.Wm = Mp, Mm, Wp, Wm
        self.Cp, self.Cm = upper(Cp), upper(Cm)
        self.Qp, self.Qm = upper(Qp), upper(Qm)          # max_n |q_n^+-|
        self.Rp_max, self.Rm_max = upper(Rp), upper(Rm)  # max_n |r_n^+-|
        self.log(f"[moments] done in {time.time()-t_start:.1f}s: C+={float(self.Cp):.4e} C-={float(self.Cm):.4e} "
                 f"Q+={float(self.Qp):.3f} Q-={float(self.Qm):.3f} r+max={float(self.Rp_max):.3f} r-max={float(self.Rm_max):.3f}")

    def _tables(self):
        """M_{k,j} = sum_i C(j,i) 4^{-i} (-alpha_c/2)^{j-i} M_{k+j+i}  (D-A4), and the real analogue with a_+-."""
        K, J = self.K, self.J
        def build(M, coef):
            # powers of coef = -alpha_c/2
            pw = [acb(1) if isinstance(coef, acb) else arb(1)]
            for _ in range(J):
                pw.append(pw[-1] * coef)
            T = []
            for k in range(K + 1):
                row = []
                for j in range(J + 1):
                    s = acb(0) if isinstance(coef, acb) else arb(0)
                    for i in range(j + 1):
                        s += rat_ball(Fraction(math.comb(j, i), 4 ** i)) * pw[j - i] * M[k + j + i]
                    row.append(s)
                T.append(row)
            return T
        self.Tp = build(self.Mp, -self.alc_p / 2)
        self.Tm = build(self.Mm, -self.alc_m / 2)
        # real tables for k <= 4
        Kreal = 4
        def buildr(W, coef):
            pw = [arb(1)]
            for _ in range(J):
                pw.append(pw[-1] * coef)
            T = []
            for k in range(Kreal + 1):
                row = []
                for j in range(J + 1):
                    s = arb(0)
                    for i in range(j + 1):
                        s += rat_ball(Fraction(math.comb(j, i), 4 ** i)) * pw[j - i] * W[k + j + i]
                    row.append(s)
                T.append(row)
            return T
        self.TWp = buildr(self.Wp, -rat_ball(self.a_p) / 2)
        self.TWm = buildr(self.Wm, -rat_ball(self.a_m) / 2)
        self.fact = [arb(math.factorial(j)) for j in range(max(K, J) + 2)]

    # ---- real sums R_k^{+-}(t) (D-A3) by the tau-expansion with a positive-term remainder
    def R_sums(self, t):
        tau = rat_ball(Fraction(t) - self.tc)
        atau = abs(tau)
        out = {}
        for sign, TW, W, rmax, pref in (("+", self.TWp, self.Wp, self.Rp_max, arb(1)),
                                        ("-", self.TWm, self.Wm, self.Rm_max, self.pref_m)):
            V = atau * rat_ball(rmax)
            rem_factor = (V ** (self.J + 1)) / self.fact[self.J + 1] * V.exp()   # sum_n w_n L^k |tau r_n|^{J+1}/(J+1)! e^{|tau r_n|} <= W_k * this
            vals = []
            for k in range(5):
                s = arb(0); tp = arb(1)
                for j in range(self.J + 1):
                    s += tp / self.fact[j] * TW[k][j]
                    tp = tp * tau
                s = s + rem_factor * W[k]
                vals.append(pref * s)
            out[sign] = vals
        return out

    def seam(self, t):
        return SeamContext(self, Fraction(t))


class SeamContext:
    """Everything needed to evaluate f, f', f_t at points of the box at the fixed time t = tau (D-A4..D-A8)."""

    def __init__(self, box, t):
        self.box = box; self.t = t
        K, J = box.K, box.J
        tau = rat_ball(t - box.tc)
        tb = rat_ball(t)
        self.tb = tb
        # collapse the tau-sums: A_k = sum_j tau^j/j! M_{k,j};  Adot_k = sum_{j>=1} tau^{j-1}/(j-1)! M_{k,j}
        def collapse(T):
            A = []; Ad = []
            for k in range(K + 1):
                s = acb(0); sd = acb(0); tp = arb(1)
                for j in range(J + 1):
                    s += tp / box.fact[j] * T[k][j]
                    if j >= 1:
                        sd += tpm / box.fact[j - 1] * T[k][j]
                    tpm = tp
                    tp = tp * tau
                A.append(s); Ad.append(sd)
            return A, Ad
        self.Ap, self.Adp = collapse(box.Tp)
        self.Am, self.Adm = collapse(box.Tm)
        # real sums at this seam (valid as sups for all t' in [t, t0], D-A9)
        R = box.R_sums(t)
        self.Rp = [upper(v) for v in R["+"]]; self.Rm = [upper(v) for v in R["-"]]
        # D-A5 remainder constants
        U = rat_ball(box.rho) * box.L_N / 2
        Vp = abs(tau) * rat_ball(box.Qp); Vm = abs(tau) * rat_ball(box.Qm)
        def rems(C, V, Q):
            E = (U + V).exp()
            base = C * E
            r_f = base * (U ** (K + 1) / box.fact[K + 1] + V ** (J + 1) / box.fact[J + 1])
            r_dz = base * (box.L_N / 2) * (U ** K / box.fact[K] + V ** (J + 1) / box.fact[J + 1])
            r_dt = base * Q * (U ** (K + 1) / box.fact[K + 1] + V ** J / box.fact[J])
            return upper(r_f), upper(r_dz), upper(r_dt)
        self.rem_p = rems(rat_ball(box.Cp), Vp, rat_ball(box.Qp))
        self.rem_m = rems(rat_ball(box.Cm), Vm, rat_ball(box.Qm))
        # D-A6 corrections
        def eta(dA):
            wmax = rat_ball(box.t0) / 2 * rat_ball(dA) * box.L_N
            return upper(wmax * wmax.exp())
        self.eta_p, self.eta_m = eta(box.dA_p), eta(box.dA_m)
        LN = upper(box.L_N)
        self.corr_f_p = self.eta_p * self.Rp[0];  self.corr_f_m = self.eta_m * self.Rm[0]
        self.corr_dz_p = (self.eta_p + box.t0 / 2 * box.A1p_p) * self.Rp[1] / 2
        self.corr_dz_m = (self.eta_m + box.t0 / 2 * box.A1p_m) * self.Rm[1] / 2
        self.corr_dt_p = self.eta_p * box.Qp * self.Rp[0] + box.dA_p * self.Rp[1] / 2
        self.corr_dt_m = self.eta_m * box.Qm * self.Rm[0] + box.dA_m * self.Rm[1] / 2
        # D-A8 box-uniform second derivatives (valid on B x [t, t0])
        Rp, Rm = self.Rp, self.Rm
        al_p, al_m = box.abs_al_p, box.abs_al_m
        A1p, A1m, A2p, A2m = box.A1_p, box.A1_m, box.A2_p, box.A2_m
        l, lz, w, wz = box.sup_l, box.sup_lz, box.sup_w, box.sup_w1
        S1zz = A1p ** 2 * Rp[2] + A2p * Rp[1]
        S1tt = Rp[4] / 16 + al_p * Rp[3] / 4 + al_p ** 2 * Rp[2] / 4
        S1zt = A1p * (Rp[3] / 4 + al_p * Rp[2] / 2) + box.A1p_p * Rp[1] / 4
        G2zz = (l ** 2 + lz) * Rm[0] + 2 * l * A1m * Rm[1] + A1m ** 2 * Rm[2] + A2m * Rm[1]
        G2tt = w ** 2 * Rm[0] + 2 * w * (Rm[2] / 4 + al_m * Rm[1] / 2) + Rm[4] / 16 + al_m * Rm[3] / 4 + al_m ** 2 * Rm[2] / 4
        G2zt = (l * w + wz) * Rm[0] + l * (Rm[2] / 4 + al_m * Rm[1] / 2) + w * A1m * Rm[1] \
            + A1m * (Rm[3] / 4 + al_m * Rm[2] / 2) + box.A1p_m * Rm[1] / 4
        self.Dzz = S1zz + G2zz; self.Dtt = S1tt + G2tt; self.Dzt = S1zt + G2zt
        # E over the box at this seam (D-A2; delta_1 at t0 -> valid on [t, t0]); D-A9 makes F, G sups at t
        xb = hull_ball(box.x1, box.x2); yb = hull_ball(box.y1, box.y2)
        tb_prism = hull_ball(t, box.t0)
        self.E, self.E_C0, self.E_AB = E_bound(xb, yb, tb_prism, box.N, rat_ball(Rp[0]), rat_ball(Rm[0]))
        # the e_{C,0} factor exp(-(t/16) log^2) is decreasing in t: E_bound with the interval t already takes the sup
        # (the ball's upper bound); F_sup, G_sup at t (D-A9).
        self.cache = {}

    def gamma_data(self, dz):
        """gamma, dlog gamma/dz, dlog gamma/dt as balls at z = z_c + dz (D-A7)."""
        box = self.box
        ad = abs(dz)
        lam = box.Lam_c + box.Lam1_c * dz + self.tb * box.w_c
        rad_lam = rat_ball(box.sup_Lam2) / 2 * ad * ad + self.tb * rat_ball(box.sup_w1) * ad
        lam = lam + acb(arb(0).union(rad_lam).union(-rad_lam), arb(0).union(rad_lam).union(-rad_lam))
        gam = lam.exp()
        r1 = rat_ball(box.sup_Lam2) * ad + self.tb * rat_ball(box.sup_w1)
        lg_z = box.Lam1_c + acb(arb(0).union(r1).union(-r1), arb(0).union(r1).union(-r1))
        r2 = rat_ball(box.sup_w1) * ad
        lg_t = box.w_c + acb(arb(0).union(r2).union(-r2), arb(0).union(r2).union(-r2))
        return gam, lg_z, lg_t

    def eval(self, x, y):
        """f, df/dz, df/dt at the exact rational point (x, y), as acb balls containing the true values."""
        key = (x, y)
        if key in self.cache:
            return self.cache[key]
        box = self.box
        dz = cpoint(Fraction(x) - box.zc[0], Fraction(y) - box.zc[1])
        u_p = acb(0, 1) * dz / 2      # i delta/2
        u_m = -u_p
        def horner(A, u):
            # sum_k A_k u^k / k!  and  its u-derivative sum_k A_{k+1} u^k / k!
            K = len(A) - 1
            s = acb(0); sd = acb(0)
            for k in range(K, -1, -1):
                s = s * u / (k + 1) + A[k]          # builds sum_k A_k u^k/k!  (Horner with the 1/(k+1) factors)
                if k >= 1:
                    sd = sd * u / k + A[k]           # sum_{k>=1} A_k u^{k-1}/(k-1)!
            return s, sd
        P_p, dP_p = horner(self.Ap, u_p)
        Pd_p, _ = horner(self.Adp, u_p)
        P_m, dP_m = horner(self.Am, u_m)
        Pd_m, _ = horner(self.Adm, u_m)
        # derivatives w.r.t. delta: d/d delta of sum A_k u^k/k! with u = +- i delta/2 is (+- i/2) * sd
        dS1 = dP_p * (acb(0, 1) / 2)
        dS2 = dP_m * (-acb(0, 1) / 2)
        gam, lg_z, lg_t = self.gamma_data(dz)
        def infl(z, r):
            r = rat_ball(r)
            return z + acb(arb(0).union(r).union(-r), arb(0).union(r).union(-r))
        S1 = infl(P_p, self.rem_p[0] + self.corr_f_p)
        S2 = infl(P_m, self.rem_m[0])                    # its d-correction is added below with |gamma| folded in (R^- carries |gamma|)
        f = infl(S1 + gam * S2, self.corr_f_m)
        S1z = infl(dS1, self.rem_p[1] + self.corr_dz_p)
        S2z = infl(dS2, self.rem_m[1])
        fz = infl(S1z + gam * (lg_z * S2 + S2z), self.corr_dz_m)
        S1t = infl(Pd_p, self.rem_p[2] + self.corr_dt_p)
        S2t = infl(Pd_m, self.rem_m[2])
        ft = infl(S1t + gam * (lg_t * S2 + S2t), self.corr_dt_m)
        self.cache[key] = (f, fz, ft)
        return f, fz, ft


# ---------------------------------------------------------------- rows (D-A10, D-P5, D-P7)

ROTATIONS = {
    0: lambda z: (z.real, z.imag),
    1: lambda z: (z.imag, -z.real),
    2: lambda z: (-z.real, -z.imag),
    3: lambda z: (-z.imag, z.real),
}


def rotation_index(box):
    reLo, reHi, imLo, imHi = box
    if reLo > 0: return 0
    if imLo > 0: return 1
    if reHi < 0: return 2
    if imHi < 0: return 3
    raise ProducerError("rotation_index on a C6-failing box")


def c6_holds(box):
    reLo, reHi, imLo, imHi = box
    return reLo > 0 or reHi < 0 or imLo > 0 or imHi < 0


def two_pi_interval():
    lo, hi = ball_interval(2 * PI())
    return lo, hi


def div_interval_by_pos(num_lo, num_hi, den_lo, den_hi):
    lo = num_lo / den_hi if num_lo >= 0 else num_lo / den_lo
    hi = num_hi / den_lo if num_hi >= 0 else num_hi / den_hi
    return lo, hi


def seg_box(seam, seg, K):
    """Hull box for one segment (D-A10): seg = ('h', a, b, c) or ('v', a, b, c) as in the M1 producer."""
    kind, a, b, c = seg
    h = abs(b - a) / 2
    mid = (a + b) / 2
    xm, ym = (mid, c) if kind == "h" else (c, mid)
    f, fz, ft = seam.eval(xm, ym)
    r = absup(fz) * h + seam.Dzz * h * h / 2
    re_lo, re_hi = ball_interval(f.real); im_lo, im_hi = ball_interval(f.imag)
    reLo, reHi = out_int_bounds_frac(re_lo - r, re_hi + r, K)
    imLo, imHi = out_int_bounds_frac(im_lo - r, im_hi + r, K)
    return (reLo, reHi, imLo, imHi), (xm, ym, h, f, fz, ft, r)


def seg_endpoints(seg):
    kind, a, b, c = seg
    return ((a, c), (b, c)) if kind == "h" else ((c, a), (c, b))


def theta(seam, point, rot_idx):
    f, _, _ = seam.eval(*point)
    rot_re, rot_im = ROTATIONS[rot_idx](f)
    if not bool(rot_re > arb(0)):
        raise ProducerError(f"endpoint {point}: rotated value not certified positive (rotation {rot_idx}); refine")
    return ball_interval(arb.atan2(rot_im, rot_re))


def argument_row(seam, seg, box, A):
    rot_idx = rotation_index(box)
    p, q = seg_endpoints(seg)
    tp_lo, tp_hi = theta(seam, p, rot_idx)
    tq_lo, tq_hi = theta(seam, q, rot_idx)
    d_lo, d_hi = tq_lo - tp_hi, tq_hi - tp_lo
    tp2_lo, tp2_hi = two_pi_interval()
    t_lo, t_hi = div_interval_by_pos(d_lo, d_hi, tp2_lo, tp2_hi)
    argLo, argHi = floor_frac(t_lo * A), ceil_frac(t_hi * A)
    argLo = max(argLo, -(A // 2)); argHi = min(argHi, A // 2)
    if argLo > argHi:
        raise ProducerError("clamp produced an empty argument row")
    return argLo, argHi


def refine_edge(seam, seg, K, n_init, max_depth):
    """Split the edge into n_init equal exact-rational pieces, then bisect any piece whose box fails C6."""
    kind, a, b, c = seg
    pieces = []
    for i in range(n_init):
        aa = a + (b - a) * Fraction(i, n_init); bb = a + (b - a) * Fraction(i + 1, n_init)
        pieces.append(((kind, aa, bb, c), 0))
    out = []
    stack = list(reversed(pieces))
    while stack:
        sg, depth = stack.pop()
        box, info = seg_box(seam, sg, K)
        if c6_holds(box):
            out.append((sg, box, info))
            continue
        if depth >= max_depth:
            raise ProducerError(f"C6 unreachable at depth {depth} on {sg}: |f| too small near this boundary piece")
        k2, a2, b2, c2 = sg
        m = (a2 + b2) / 2
        stack.append(((k2, m, b2, c2), depth + 1))
        stack.append(((k2, a2, m, c2), depth + 1))
    return out


# ---------------------------------------------------------------- the prism chain (D-A11)

def produce_prism(box, tau, K, A, r_frac, max_depth, log=print):
    """One seam + prism at tau; returns (prism_dict, tau_next, stats)."""
    t_s = time.time()
    seam = box.seam(tau)
    # pre-scan: |f| and |f'| on a coarse grid to size the mesh
    x1, x2, y1, y2 = box.x1, box.x2, box.y1, box.y2
    edges = {"bottom": ("h", x1, x2, y1), "right": ("v", y1, y2, x2), "top": ("h", x2, x1, y2), "left": ("v", y2, y1, x1)}
    m_est = None; fp_max = Fraction(0)
    for name, (kind, a, b, c) in edges.items():
        for i in range(41):
            p = a + (b - a) * Fraction(i, 40)
            pt = (p, c) if kind == "h" else (c, p)
            f, fz, ft = seam.eval(*pt)
            m = lower(abs(f))
            m_est = m if m_est is None else min(m_est, m)
            fp_max = max(fp_max, absup(fz))
    if m_est <= 0:
        raise ProducerError(f"pre-scan found |f| not certified positive at seam {tau}")
    # target hull radius r_target = r_frac * m_est: solve fp_max*h + Dzz*h^2/2 = r_target for h (positive root)
    r_target = m_est * r_frac
    Dzz = seam.Dzz
    # floats pick the mesh size h; no checked number depends on this choice
    fpm = float(fp_max); dzz = float(Dzz); rt = float(r_target)
    hf = (-fpm + math.sqrt(fpm * fpm + 2 * dzz * rt)) / dzz if dzz > 0 else rt / max(fpm, 1e-30)
    ell = 2 * hf
    mesh = {}; rows = []; infos = []
    for name in ("bottom", "right", "top", "left"):
        kind, a, b, c = edges[name]
        n_init = max(2, int(math.ceil(float(abs(b - a)) / ell)))
        pieces = refine_edge(seam, edges[name], K, n_init, max_depth)
        mesh[name] = [pieces[0][0][1]] + [sg[2] for sg, _, _ in pieces]
        for sg, bx, info in pieces:
            argLo, argHi = argument_row(seam, sg, bx, A)
            rows.append(bx + (argLo, argHi))
            infos.append((sg, info))
    S_lo = sum(r[4] for r in rows); S_hi = sum(r[5] for r in rows)
    if 2 * (S_hi - S_lo) >= A or not (S_lo <= 0 <= S_hi):
        raise ProducerError(f"winding enclosure [{S_lo},{S_hi}]/{A} does not pin m = 0 at seam {tau}")
    def mcoord(lo, hi):
        return 0 if lo <= 0 <= hi else min(abs(lo), abs(hi))
    m2_min = min(mcoord(r[0], r[1]) ** 2 + mcoord(r[2], r[3]) ** 2 for r in rows)
    Fn = math.isqrt(m2_min); Fd = K
    floor = Fraction(Fn, Fd)
    # displacement (D-A11)
    E_p = seam.E
    Mt = max(absup(info[5]) + seam.Dzt * info[2] for _, info in infos)   # |f_t(z_m)| + D_zt * h
    slack = floor - 3 * E_p
    if slack <= 0:
        raise ProducerError(f"gate impossible at seam {tau}: floor {float(floor):.4e} <= 3E = {float(3*E_p):.4e}")
    s_target = slack * Fraction(9, 10)
    Dtt = seam.Dtt
    # solve Delta*(Mt + Dtt*Delta) = s_target  (float pick, exact verify)
    mt = float(Mt); dtt = float(Dtt); st = float(s_target)
    d_f = (-mt + math.sqrt(mt * mt + 4 * dtt * st)) / (2 * dtt) if dtt > 0 else st / mt
    grid = 10 ** 9
    Delta = Fraction(max(1, int(math.floor(d_f * grid))), grid)
    tau_next = min(tau + Delta, box.t0)
    Delta = tau_next - tau
    E_int = ceil_frac(K * E_p)
    while True:
        D_val = 2 * E_p + Delta * (Mt + Dtt * Delta)
        D_int = ceil_frac(K * D_val)
        if (E_int + D_int) * Fd < Fn * K:
            break
        Delta = Delta / 2
        if Delta < Fraction(1, 10 ** 12):
            raise ProducerError("cannot satisfy the gate C-B12 even with a tiny prism")
        tau_next = tau + Delta
    prism = {
        "format": "M2a-barrier-transcript", "version": "1.0", "kind": "prism",
        "index": None, "seam": frac_json(tau), "scales": {"K": str(K), "A": str(A)},
        "mesh": {name: [frac_json(q) for q in mesh[name]] for name in ("bottom", "right", "top", "left")},
        "segments": [{"reLo": str(r[0]), "reHi": str(r[1]), "imLo": str(r[2]), "imHi": str(r[3]),
                      "argLo": str(r[4]), "argHi": str(r[5])} for r in rows],
        "modulus_floor": {"Fn": str(Fn), "Fd": str(Fd)},
        "approx_defect": str(E_int),
        "displacement": str(D_int),
        "producer": {
            "leg": "arb",
            "implementation": "producer_arb.py (results/d1-m2a/), python-flint " + flint.__version__ + f", prec {PREC} bits",
            "evaluator": "D-A4 two-variable Taylor/moment evaluator (K=%d, J=%d) of (92) with D-A5/D-A6 remainders; gamma by D-A7" % (box.K, box.J),
            "seam_time": str(tau), "prism_end": str(tau_next), "delta_t": str(Delta),
            "E_seam": {"total": str(E_p), "e_C0": str(seam.E_C0), "e_A_plus_e_B": str(seam.E_AB)},
            "D_parts": {"two_E": str(2 * E_p), "Mt_sup_dfdt": str(Mt), "D_tt": str(Dtt), "D_zt": str(seam.Dzt), "D_zz": str(seam.Dzz)},
            "R_sums_at_seam": {"plus": [str(v) for v in seam.Rp], "minus": [str(v) for v in seam.Rm]},
            "remainders": {"plus(f,dz,dt)": [str(v) for v in seam.rem_p], "minus(f,dz,dt)": [str(v) for v in seam.rem_m],
                           "eta_plus": str(seam.eta_p), "eta_minus": str(seam.eta_m)},
            "mesh_policy": f"uniform exact-rational pieces sized by |f'|h + D_zz h^2/2 = {r_frac} * min|f| (pre-scan), bisection on C6 failure",
            "prescan": {"min_abs_f": str(m_est), "max_abs_fz": str(fp_max)},
            "segments": len(rows), "winding_sum": {"S_lo": str(S_lo), "S_hi": str(S_hi)},
            "floor_rational": str(floor),
            "seconds": round(time.time() - t_s, 2),
            "timestamp_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "trust": "UNTRUSTED producer; output enters the trusted statement only via H2-B",
        },
    }
    if tau == 0:
        prism["producer"]["comment"] = ("t = 0 seam: Theorem 1.3 at t = 0 by the limit argument D-A12 (dominated convergence for H_t, "
                                        "continuity of B_t, f_t and of the D-A2 majorant in t); this is the Arb leg's discharge of SPEC P-7.")
    stats = dict(tau=tau, tau_next=tau_next, Delta=Delta, segments=len(rows), floor=floor, E=E_p, Mt=Mt, Dtt=Dtt,
                 Dzz=seam.Dzz, Dzt=seam.Dzt, m_est=m_est, fp_max=fp_max, seconds=time.time() - t_s)
    return prism, tau_next, stats


def check_prism_locally(rect, p):
    """Inline replica of barrier_ref_checker.check_prism (prevalidation; the shared checker is also run at the end)."""
    sys.path.insert(0, HERE)
    import barrier_ref_checker as brc
    return brc.check_prism(rect, p, p.get("index", "?"))


def run_instance(out_dir, max_seconds, max_prisms, resume, K, A, r_frac, max_depth, KK, JJ, log=print):
    os.makedirs(out_dir, exist_ok=True)
    X, t0, y0, N = X_INST, T0_INST, Y0_INST, N0_INST
    x1, x2, y1, y2 = Fraction(X), Fraction(X + 1), y0, Fraction(1)
    # D-A13
    for (xx, tt) in ((x1, Fraction(0)), (x2, t0)):
        if N_of(xx, tt) != N:
            raise ProducerError("N is not constant on the box")
    log(f"[D-A13] N = {N} at both extreme corners; N constant on [X, X+1] x [0, t0]")
    box = BoxEvaluator(x1, x2, y1, y2, t0, N, K=KK, J=JJ, log=log)
    manifest_path = os.path.join(out_dir, "instance02-barrier-manifest.json")
    state_path = os.path.join(out_dir, "instance02-progress.json")
    prisms = []; tau = Fraction(0)
    if resume and os.path.exists(state_path):
        with open(state_path) as fh:
            st = json.load(fh)
        prisms = st["prisms"]; tau = Fraction(st["next_seam"])
        log(f"[resume] {len(prisms)} prisms on disk; next seam {tau}")
    t_start = time.time(); j = len(prisms)
    rect = ((X, 1), (X + 1, 1), (y0.numerator, y0.denominator), (1, 1))
    while tau < t0:
        if max_prisms and j >= max_prisms:
            log("[stop] max prisms reached"); break
        if max_seconds and time.time() - t_start > max_seconds:
            log("[stop] time budget reached"); break
        prism, tau_next, stats = produce_prism(box, tau, K, A, r_frac, max_depth, log=log)
        prism["index"] = str(j)
        check_prism_locally(rect, prism)
        fname = f"instance02-prism-{j:04d}.json"
        with open(os.path.join(out_dir, fname + ".tmp"), "w") as fh:
            json.dump(prism, fh, separators=(",", ":"))
            fh.write("\n")
        os.replace(os.path.join(out_dir, fname + ".tmp"), os.path.join(out_dir, fname))
        prisms.append({"index": str(j), "file": fname, "seam": frac_json(tau)})
        log(f"[prism {j}] seam={float(tau):.9f} -> {float(tau_next):.9f} (dt={float(stats['Delta']):.3e}) segs={stats['segments']} "
            f"floor={float(stats['floor']):.4f} min|f|~{float(stats['m_est']):.4f} max|f'|~{float(stats['fp_max']):.1f} "
            f"E={float(stats['E']):.3e} Mt={float(stats['Mt']):.3e} Dtt={float(stats['Dtt']):.3e} Dzz={float(stats['Dzz']):.3e} "
            f"{stats['seconds']:.1f}s")
        tau = tau_next; j += 1
        with open(state_path + ".tmp", "w") as fh:
            json.dump({"prisms": prisms, "next_seam": str(tau)}, fh, indent=1)
        os.replace(state_path + ".tmp", state_path)
        write_manifest(manifest_path, prisms, x1, x2, y1, y2, tau if tau < t0 else t0, complete=(tau >= t0), log=log)
    complete = tau >= t0
    write_manifest(manifest_path, prisms, x1, x2, y1, y2, tau if not complete else t0, complete=complete, log=log)
    log(f"[done] {len(prisms)} prisms; certified t-range [0, {tau}] {'COMPLETE' if complete else 'PARTIAL (cut line = last prism end)'}")
    return manifest_path, complete, tau


def write_manifest(path, prisms, x1, x2, y1, y2, t_end, complete, log=print):
    man = {
        "format": "M2a-barrier-transcript", "version": "1.0", "kind": "manifest", "lane": "barrier",
        "trust_label": TRUST_LABEL,
        "rect": {"x1": frac_json(x1), "x2": frac_json(x2), "y1": frac_json(y1), "y2": frac_json(y2)},
        "t0": frac_json(t_end),
        "prisms": prisms,
        "producer": {
            "leg": "arb", "implementation": "producer_arb.py (results/d1-m2a/), python-flint " + flint.__version__,
            "instance": "Polymath15 Table 1 row 2: X = 5000000194858, t0 = 93/500, y0 = 16733/100000, N0 = 630783 (SPEC section 9)",
            "status": "COMPLETE chain to t0 = 93/500" if complete else
                      f"PARTIAL chain: the manifest's t0 field is the last certified prism end {t_end} (< 93/500); "
                      "the certificate covers the barrier for 0 <= t <= this value only (cut line stated honestly)",
            "trust": "UNTRUSTED producer; output enters the trusted statement only via H2-B",
        },
        "comment": ("Lane B barrier certificate for the row-2 instance, Arb/FLINT leg. Each prism's rows enclose the seam "
                    "approximant f = f_tau of (92) at N = 630783; E and D per SPEC sections 4.4-4.5 (derivations D-A2, D-A11 in producer_arb.py)."),
    }
    with open(path + ".tmp", "w") as fh:
        json.dump(man, fh, indent=1)
        fh.write("\n")
    os.replace(path + ".tmp", path)


# ---------------------------------------------------------------- self tests and cross-checks

def selftest(log=print):
    X, t0, y0, N = X_INST, T0_INST, Y0_INST, N0_INST
    for (xx, tt) in ((Fraction(X), Fraction(0)), (Fraction(X + 1), t0), (Fraction(X), t0), (Fraction(X + 1), Fraction(0))):
        log(f"N({xx}, {tt}) = {N_of(xx, tt)}")
    # small-box self-consistency of the Taylor evaluator against direct summation (moderate x)
    Xs = Fraction(10 ** 7 + 12345)
    Ns = N_of(Xs, Fraction(0))
    log(f"[selftest] small box at X={Xs}, N={Ns}")
    box = BoxEvaluator(Xs, Xs + 1, y0, 1, t0, Ns, K=36, J=40, log=log)
    worst = 0.0
    for tt in (Fraction(0), Fraction(7, 100), t0):
        seam = box.seam(tt)
        for (xx, yy) in ((Xs, y0), (Xs + 1, Fraction(1)), (Xs + Fraction(1, 3), Fraction(1, 2)), (Xs + Fraction(9, 10), y0)):
            f, fz, ft = seam.eval(xx, yy)
            fd, gam, S1, S2, F, G = ft_direct(cpoint(xx, yy), tt, Ns)
            # containment: the direct ball must intersect the Taylor ball (both enclose the true value); report widths
            dlo, dhi = ball_interval(fd.real); tlo, thi = ball_interval(f.real)
            ok_re = not (dhi < tlo or thi < dlo)
            dlo2, dhi2 = ball_interval(fd.imag); tlo2, thi2 = ball_interval(f.imag)
            ok_im = not (dhi2 < tlo2 or thi2 < dlo2)
            wid = float(max(thi - tlo, thi2 - tlo2))
            worst = max(worst, wid)
            log(f"  t={float(tt):.3f} z=({float(xx):.3f},{float(yy):.5f}) taylor={complex(float(f.real.mid()), float(f.imag.mid())):.12g} "
                f"direct={complex(float(fd.real.mid()), float(fd.imag.mid())):.12g} width={wid:.2e} overlap={ok_re and ok_im}")
            if not (ok_re and ok_im):
                raise ProducerError("Taylor and direct enclosures are disjoint -- BUG")
    log(f"[selftest] worst Taylor width {worst:.2e}; PASS")


def crosscheck(points, log=print):
    X, t0, y0, N = X_INST, T0_INST, Y0_INST, N0_INST
    box = BoxEvaluator(X, X + 1, y0, 1, t0, N, log=log)
    pts = []
    import random
    random.seed(2)
    for i in range(points):
        tt = Fraction(random.randint(0, 186), 1000)
        edge = random.choice("brtl")
        if edge == "b": pt = (Fraction(X) + Fraction(random.randint(0, 1000), 1000), y0)
        elif edge == "t": pt = (Fraction(X) + Fraction(random.randint(0, 1000), 1000), Fraction(1))
        elif edge == "r": pt = (Fraction(X + 1), y0 + (1 - y0) * Fraction(random.randint(0, 1000), 1000))
        else: pt = (Fraction(X), y0 + (1 - y0) * Fraction(random.randint(0, 1000), 1000))
        pts.append((tt, pt))
    for tt, (xx, yy) in pts:
        seam = box.seam(tt)
        t_a = time.time(); f, fz, ft = seam.eval(xx, yy); t_a = time.time() - t_a
        t_b = time.time(); fd, gam, S1, S2, F, G = ft_direct(cpoint(xx, yy), tt, N); t_b = time.time() - t_b
        dlo, dhi = ball_interval(fd.real); tlo, thi = ball_interval(f.real)
        dlo2, dhi2 = ball_interval(fd.imag); tlo2, thi2 = ball_interval(f.imag)
        ok = not (dhi < tlo or thi < dlo) and not (dhi2 < tlo2 or thi2 < dlo2)
        log(f"t={float(tt):.3f} z=({float(xx-X):.3f}+X,{float(yy):.5f}) taylor={complex(float(f.real.mid()), float(f.imag.mid())):.15g} "
            f"(w={float(thi-tlo):.2e}, {t_a*1e3:.1f} ms) direct={complex(float(fd.real.mid()), float(fd.imag.mid())):.15g} "
            f"(w={float(dhi-dlo):.2e}, {t_b:.1f} s) overlap={ok} |f_t|={float(abs(ft).mid()):.3e} |f'|={float(abs(fz).mid()):.3e}")
        if not ok:
            raise ProducerError("cross-check FAILED: disjoint enclosures")
    log("[crosscheck] PASS")


def point_hook(x, y, t, log=print):
    """Direct f_t ball and the D-A2 defect at one point in region (5): the validation hook."""
    x, y, t = Fraction(x), Fraction(y), Fraction(t)
    N = N_of(x, t)
    z = cpoint(x, y)
    f, gam, S1, S2, F, G = ft_direct(z, t, N)
    E, EC0, EAB = E_bound(rat_ball(x), rat_ball(y), rat_ball(t), N, F, G)
    B = Bt_point(z, rat_ball(t))
    return {"N": N, "f": f, "E": E, "E_C0": EC0, "E_AB": EAB, "B": B, "gamma": gam}


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("selftest")
    cc = sub.add_parser("crosscheck"); cc.add_argument("--points", type=int, default=8)
    ins = sub.add_parser("instance")
    ins.add_argument("--out-dir", default=os.path.join(HERE, "transcripts"))
    ins.add_argument("--max-seconds", type=float, default=0)
    ins.add_argument("--max-prisms", type=int, default=0)
    ins.add_argument("--resume", action="store_true")
    ins.add_argument("--K", type=int, default=10 ** 20)
    ins.add_argument("--A", type=int, default=10 ** 6)
    ins.add_argument("--r-frac", type=Fraction, default=Fraction(1, 6))
    ins.add_argument("--max-depth", type=int, default=30)
    ins.add_argument("--KK", type=int, default=36)
    ins.add_argument("--JJ", type=int, default=40)
    pt = sub.add_parser("point")
    for fld in ("x", "y", "t"):
        pt.add_argument("--" + fld, type=Fraction, required=True)
    args = ap.parse_args()
    if args.cmd == "selftest":
        selftest()
    elif args.cmd == "crosscheck":
        crosscheck(args.points)
    elif args.cmd == "instance":
        if args.A % 2:
            raise SystemExit("A must be even")
        path, complete, tau = run_instance(args.out_dir, args.max_seconds, args.max_prisms, args.resume, args.K, args.A,
                                           args.r_frac, args.max_depth, args.KK, args.JJ)
        r = subprocess.run([sys.executable, os.path.join(HERE, "barrier_ref_checker.py"), path], capture_output=True, text=True)
        print(r.stdout[-2000:]); print(r.stderr[-2000:])
        print("REF CHECKER EXIT", r.returncode)
    elif args.cmd == "point":
        d = point_hook(args.x, args.y, args.t)
        print(json.dumps({k: (str(v) if not isinstance(v, int) else v) for k, v in d.items()}, indent=1))


if __name__ == "__main__":
    main()
