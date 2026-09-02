"""ft_mp.py -- the mpmath-ball evaluator layer for Polymath15's effective approximation of
H_t(x+iy) (P15 Theorem 1.3), for the M2a barrier producer (mpmath leg).

D1 M2a work item (d).  UNTRUSTED producer-side code by design: nothing here is inside the trust
boundary; its output enters the certified statement only through the displayed enclosure
hypotheses H2-B of ``results/d1-m2a/SPEC.md`` section 6/8.1.  It is built on the M1 ball layer
``results/d1-m1/ball.py`` (imported; the complex rectangular-interval class ``Ball`` on mpmath's
``iv`` context with outward-inflated transcendental endpoints) and shares NO code with the Arb leg.

SOURCE (standing order 5 -- nothing load-bearing from memory).  P15 = D.H.J. Polymath, "Effective
approximation of heat flow evolution of the Riemann xi function, and a new upper bound for the
de Bruijn-Newman constant", arXiv:1904.12438v2, on disk as
``fetched/p3-22a4-polymath15-2019-upper-bound-debruijn-newman.pdf``; PDF pages = printed pages.
Every formula below is transcribed from that file (pdftotext -layout, page-split; the one place
where the extraction is ambiguous, eq. (14), was read from a page image -- see D-F1).

THE FORMULAS TRANSCRIBED (P15 pages 4, 6, 30-31, 46-48)
======================================================
p4, (6):  M_0(s) := (1/8) (s(s-1)/2) pi^{-s/2} sqrt(2 pi) exp((s/2 - 1/2) Log(s/2) - s/2),
          "where Log denotes the standard branch of the complex logarithm, with branch cut at the
          negative axis and imaginary part in (-pi, pi]".
p4, (7):  log M_0(s) := Log s + Log(s-1) - (s/2) log pi + log(sqrt(2 pi)/16) + (s/2 - 1/2) Log(s/2) - s/2
          ("a holomorphic branch log M_0 : C\\(-inf, 1] -> C of the logarithm of M_0").
p4, (9):  alpha(s) = 1/(2s) + 1/(s-1) + (1/2) Log(s/(2 pi)).
p4, (10): M_t(s) := exp((t/4) alpha(s)^2) M_0(s).
p4, (11): B_t(x+iy) := M_t((1+y-ix)/2).
p6, Theorem 1.3, on the region (5) (p3: 0 < t <= 1/2, 0 <= y <= 1, x >= 200):
   (13) H_t(x+iy)/B_t(x+iy) = f_t(x+iy) + O_<=(e_A + e_B + e_{C,0})
   (14) f_t(x+iy) := sum_{n=1}^{N} b_n^t / n^{s_*} + gamma sum_{n=1}^{N} n^y b_n^t / n^{conj(s_*) + kappa}
        [the overline on s_* in the second sum is in the PDF (page image, verified this session);
         the pdftotext extraction -- and hence the SPEC's quotation of (14) -- loses it; D-F1 below
         shows this is the only reading consistent with (69)-(70) and (92)]
   (15) b_n^t := exp((t/4) log^2 n)
   (16) gamma := M_t((1-y+ix)/2) / M_t((1+y-ix)/2)
   (17) s_* := (1+y-ix)/2 + (t/2) alpha((1+y-ix)/2)
   (18) kappa := (t/2) (alpha((1-y+ix)/2) - alpha((1+y+ix)/2))
   (19) N := floor(sqrt(x/(4 pi) + t/16))
   (20) |gamma| <= e^{0.02 y} (x/(4 pi))^{-y/2}                                [= Prop 6.6(i), p31]
   (22) |kappa| <= t y / (2 (x - 6))                                          [= Prop 6.6(iii), p31]
   p6: "f_t(x+iy) is a holomorphic function of x+iy in the region (5) as long as N is constant".
p31, Proposition 6.6 (iv), (v), (vi) (the explicit majorants of e_A, e_B, e_{C,0} of (71)-(74)):
   (iv) e_A <= |gamma| N^{|kappa|} sum_{n<=N} n^y b_n^t n^{-Re s_*} (exp(((t^2/16) log^2(x/(4 pi n)) + 0.626)/(x - 6.66)) - 1)
   (v)  e_B <= sum_{n<=N} b_n^t n^{-Re s_*} (exp(((t^2/16) log^2(x/(4 pi n)) + 0.626)/(x - 6.66)) - 1)
   (vi) e_{C,0} <= (x/(4 pi))^{-(1+y)/4} exp(-(t/16) log^2(x/(4 pi)) + (3|log(x/(4 pi)) + i pi/2| + 3.58)/(x - 8.52))
                   * (1 + 1.24 (3^y + 3^{-y})/(N - 0.125) + 6.92/(x - 12))
   [(vi) is used AS PRINTED -- SPEC.md D-2.4 permits "the 10.50 form (or 6.6(vi) itself)"; the
    displayed (24) with its 10.44 is never used.]
p46, (92) (proof of Lemma 8.4): f_t = sum b_n^t/n^{s_*} + gamma sum b_n^t/n^{s_**},
   s_** := s_* - y + kappa = (1-y+ix)/2 + (t/2) alpha((1-y+ix)/2).
p47-48, proof of Lemma 8.4 (time derivative): d/dt log b_n^t = (1/4) log^2 n; d/dt s_* = (1/2) alpha(1-s);
   d/dt s_** = (1/2) alpha(s); d/dt log gamma = (1/4)(alpha(s)^2 - alpha(1-s)^2), where s = (1-y+ix)/2.

NOTATION USED HERE.  z = x + iy;  s_+ := (1+y-ix)/2 = (1 - iz)/2;  s_- := (1-y+ix)/2 = (1 + iz)/2 = 1 - s_+.
   A_t(s) := sum_{n=1}^{N} b_n^t n^{-(s + (t/2) alpha(s))}.   Then (D-F1)  f_t(z) = A_t(s_+) + gamma(z) A_t(s_-).

DERIVATIONS (checkable; each is used by the code exactly where cited)
=====================================================================
D-F1 (the second sum of (14) is A_t(s_-)).  conj(s_*) = (1+y+ix)/2 + (t/2) alpha((1+y+ix)/2), because
  conj(alpha(s)) = alpha(conj s) (each of 1/(2s), 1/(s-1), Log(s/2pi) commutes with conjugation off
  the cut).  With (18): conj(s_*) + kappa = (1+y+ix)/2 + (t/2) alpha((1-y+ix)/2).  Hence
  n^y b_n / n^{conj(s_*)+kappa} = b_n n^{-(conj(s_*) + kappa - y)} = b_n n^{-((1-y+ix)/2 + (t/2) alpha(s_-))}
  = b_n n^{-(s_- + (t/2) alpha(s_-))}, i.e. the second sum is A_t(s_-) = the sum of (92).  Without the
  overline the exponent would carry -ix instead of +ix and f_t would not be holomorphic; P15's own
  (69)-(70), derived from Corollary 6.5's A_{t,N} = M_t(s_-) sum b_n/n^{s_- + (t/2) alpha(s_-)}, fix
  the reading.
D-F2 (gamma as one exponential).  exp((7)) = s (s-1) pi^{-s/2} (sqrt(2 pi)/16) exp((s/2-1/2) Log(s/2) - s/2)
  = (1/8)(s(s-1)/2) pi^{-s/2} sqrt(2 pi) exp(...) = M_0(s), since sqrt(2pi)/16 = (1/8)(1/2) sqrt(2pi).
  So by (10), (16): gamma = exp((t/4)(alpha(s_-)^2 - alpha(s_+)^2) + log M_0(s_-) - log M_0(s_+)),
  and d/dt gamma = gamma (alpha(s_-)^2 - alpha(s_+)^2)/4.  Only exp(difference) is formed; the
  choice of branch in (7) is immaterial for the value (exp(log M_0) = M_0 for every branch), and
  the principal Logs are what ``Ball.log`` returns on the half-planes RE+, IM+, IM- (ball.py
  derivations; RE- would not be principal and is refused by ``_plog``).
D-F3 (N constant on the barrier box).  N(x,t) = floor(sqrt(x/(4pi) + t/16)) is nondecreasing in x
  and in t; so N = N_0 on [x_1,x_2] x [0,t_0] iff N(x_1,0) = N(x_2,t_0) = N_0, checked by directed
  rounding (``check_N_constant``).  Also N_0^2 <= x_1/(4pi) (needed by D-F4) is checked the same way.
D-F4 (uniform bound for e_A + e_B on a box, from (iv), (v), (20), (22)).  For 1 <= n <= N and
  N^2 <= x/(4pi):  1 <= x/(4 pi N) <= x/(4 pi n) <= x/(4pi), so 0 <= log(x/(4 pi n)) <= log(x/(4pi)),
  and the n-dependent exponent in (iv)/(v) is <= delta_1 := ((t^2/16) log^2(x/(4pi)) + 0.626)/(x - 6.66).
  Next |gamma| n^y <= e^{0.02y} (x/4pi)^{-y/2} N^y <= e^{0.02 y} by (20) and N <= sqrt(x/4pi).  With
  (22), N^{|kappa|} <= N^{t y/(2(x-6))}.  Hence
     e_A + e_B <= (e^{delta_1} - 1) (1 + e^{0.02 y} N^{t y/(2(x-6))}) F_{N,t}(sigma)   for any sigma <= Re s_*,
  F_{N,t}(sigma) := sum_{n<=N} b_n^t n^{-sigma} being non-increasing in sigma.  Every factor is
  evaluated by interval arithmetic over the box (x, y, t intervals); the upper endpoint is taken.
  Re s_* is enclosed by interval evaluation of (17) on the box (its lower endpoint is sigma).
D-F5 (closed-form majorant of F_{N,t}).  b_n^t = n^{(t/4) log n} <= n^{(t/4) log N} for 1 <= n <= N,
  so F_{N,t}(sigma) <= sum_{n<=N} n^{-rho}, rho := sigma - (t/4) log N.  For rho > 0 the function
  u -> u^{-rho} decreases on [1, inf), so sum_{n=2}^{N} n^{-rho} <= int_1^N u^{-rho} du, i.e.
     F <= 1 + (N^{1-rho} - 1)/(1 - rho)  (rho != 1),   F <= 1 + log N  (rho = 1).
  The code uses the LOWER endpoint of the interval rho (the bound is decreasing in rho); for
  rho <= 0 it falls back to N * N^{-rho}.
D-F6 (time derivative of f_t at fixed z; Lemma 8.4's identities, p47).  With s_*(s) := s + (t/2) alpha(s):
  d/dt [b_n^t n^{-s_*(s)}] = b_n^t n^{-s_*(s)} ((1/4) log^2 n - (1/2) alpha(s) log n), so
  d/dt A_t(s) = sum_n b_n^t n^{-s_*(s)} (log^2 n/4 - alpha(s) log n/2), and (D-F2)
  d/dt f_t(z) = d/dt A_t(s_+) + (d/dt gamma) A_t(s_-) + gamma d/dt A_t(s_-).  For fixed z the map
  t -> f_t(z) is C^1 (finite sum of C^1 functions), so |f_t(z) - f_tau(z)| <= (t - tau) sup_{[tau,t]} |d/dt f|
  (|F(t)-F(tau)| = |int_tau^t F'| <= int |F'|).
D-F7 (the displacement clause of SPEC 4.5).  For z on the boundary and tau <= t <= tau':
  |g_t(z) - g_tau(z)| <= |g_t - f_t| + |f_t - f_tau| + |f_tau - g_tau| <= E(t) + (tau'-tau) sup|d/dt f| + E(tau)
  with E(.) the D-F4 + (vi) bound; E(t) <= E_prism := the same bound evaluated with t the interval
  [tau, tau'].  So D/K := E_prism + (tau'-tau) DT + E(tau) with DT >= sup over the boundary x [tau,tau']
  of |d/dt f_t| suffices.  (H2-B's clause is stated for z on the boundary; every bound here is
  uniform on the closed box, hence on the boundary.)
D-F8 (the frozen-alpha block-Taylor evaluation -- the fast rigorous evaluator).  Fix the series
  center c (c = u := s_+(z_c) for the "+" series, c = 1 - u for the "-" series; z_c the box center)
  and the sign sgn (+1 for "+", -1 for "-"); then s_+(z) = u - i delta/2, s_-(z) = (1-u) + i delta/2
  with delta := z - z_c, i.e. s(z) = c - sgn * i delta/2.  Put a := alpha(c) (a fixed complex
  number, enclosed by a thin Ball), L := log n, and
     q(L) := L^2/4 - a L/2.
  The n-th term of A_t(s(z)) is exp((t/4)L^2 - (s(z) + (t/2) alpha(s(z))) L)
     = exp(-c L + sgn (i delta/2) L + t q(L)) * rho_n,   rho_n := exp(-(t/2)(alpha(s(z)) - a) L).
  (a) Frozen part.  Partition {1..N} into blocks B with an exact dyadic center L_c(B) and
      l := L - L_c in [-lmax(B), lmax(B)].  Since q(L_c + l) = Q_c + p_c l + l^2/4 with
      Q_c := L_c^2/4 - a L_c/2, p_c := (L_c - a)/2 (expand the square), the frozen term equals
         n^{-c} * BF_B * exp(v l + t l^2/4),   BF_B := exp(sgn (i delta/2) L_c + t Q_c),  v := sgn (i delta/2) + t p_c,
      and exp(v l + t l^2/4) = sum_{j<J} sum_{k<K} (v l)^j (t l^2/4)^k/(j! k!) + Rem_n with (Taylor tails
      of exp: for a >= 0, sum_{j>=J} a^j/j! <= a^J/J! e^a =: T_J(a); |S_J| <= e^{|v||l|}, |S_K| <= e^{|t| l^2/4})
         |Rem_n| <= T_J(|v| lmax) e^{|t| lmax^2/4} + e^{|v| lmax} T_K(|t| lmax^2/4) + T_J(.) T_K(.) =: Bnd_B.
      Hence with the STORED MOMENTS m_r(B) := sum_{n in B} n^{-c} l_n^r (r = 0..R) and the real weights
      w(B) := sum_{n in B} n^{-Re c}:
         sum_{n in B} frozen_n = BF_B * sum_{j<J,k<K} v^j t^k m_{j+2k}(B)/(j! k! 4^k) + O_<=(|BF_B| Bnd_B w(B)).
      The same holds with an extra factor l_n^r inside (r = 1, 2; moments shifted by r, weight
      lmax^r w(B)), which gives the frozen time derivative: d/dt of the frozen n-th term is
      q(L) * (frozen term) = (Q_c + p_c l + l^2/4) * (frozen term), so
         d/dt sum_{n in B} frozen_n = BF_B (Q_c P_0 + p_c P_1 + P_2/4),  P_r := sum_{n in B} n^{-c} l_n^r exp(v l_n + t l_n^2/4).
      Everything is an inclusion-monotone interval expression in (delta, t): evaluating it with
      delta and t intervals encloses the frozen sum for every z in the box and t in the interval.
  (b) The alpha-freezing correction.  |rho_n - 1| <= e^{eta} - 1, eta := (t/2) |alpha(s(z)) - a| log N
      (|e^w - 1| <= e^{|w|} - 1), uniformly for n <= N, z in the box, t in the interval; and
      |frozen_n| = b_n^t n^{-sigma_fr}, sigma_fr := Re c + sgn Im(delta)/2 + (t/2) Re a (compute: the real
      part of the exponent is -Re(c)L - sgn Im(delta) L/2 + t(L^2/4 - Re(a) L/2)).  So
         |A_t(s(z)) - frozen sum| <= (e^{eta} - 1) F_{N,t}(sigma_fr)   (D-F5 majorant).
      For the derivative: d/dt(true_n) - d/dt(frozen_n) = q(L) frozen_n (rho_n - 1) - frozen_n ((alpha - a) L/2) rho_n,
      so |.| <= |frozen_n| (Qmax (e^eta - 1) + eta_1 e^eta), eta_1 := |alpha(s(z)) - a| log N/2,
      Qmax >= max_{0 <= L <= log N} |q(L)| (bounded by interval evaluation on subintervals of [0, log N]).
  The evaluator returns the frozen block sums plus these remainders as [-r, r] x [-r, r] boxes.
D-F9 (the seam at t = 0; SPEC P-7).  Theorem 1.3 is stated for t > 0.  For t -> 0+: H_t(z) -> H_0(z)
  (dominated convergence: |e^{t u^2} Phi(u) cos(zu)| <= e^{u^2/2} |Phi(u)| e^{|y| u}, integrable);
  B_t(z) -> B_0(z) (continuity of exp((t/4) alpha^2)); f_t(z) -> f_0(z) (finite sum, continuous in t);
  the majorant of D-F4 + (vi) is continuous in t at t = 0.  Hence |H_0/B_0 - f_0| <= (majorant at t = 0).
  The producer records this in prism 0's ``producer.comment``; it is part of H2-B's discharge.

INTERVAL DISCIPLINE.  All arithmetic is mpmath ``iv`` through ``ball.py`` (ring primitives correctly
directed-rounded; transcendental endpoints outward-inflated by 2^-(prec-16) relative, the stated
platform assumption of ball.py); every emitted number is an exact Fraction endpoint.  No float
touches any bound.  Precision: 288 bits (as M1).

U.S. English throughout.
"""

import json
import math
import os
import sys
import time
from fractions import Fraction

import mpmath
from mpmath import iv

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(_HERE, "..", "d1-m1")))

from ball import (Ball, iv_from_fraction, iv_from_int, ivmpf_bounds, set_prec,  # noqa: E402
                  iv_pi, iv_exp, iv_log, iv_atan, iv_cos, iv_sin, iv_hull,
                  mpf_tuple_to_fraction, iv_from_fraction_pair)

PREC_DEFAULT = 288


# ---------------------------------------------------------------- small interval helpers

def iv_lo(x):
    return ivmpf_bounds(x)[0]


def iv_hi(x):
    return ivmpf_bounds(x)[1]


def iv_abs(x):
    """|x| for a real iv interval: [min |.|, max |.|] (0 if the interval straddles 0)."""
    lo, hi = x._mpi_
    from mpmath.libmp import mpf_neg, mpf_lt, fzero
    nlo, nhi = mpf_neg(hi), mpf_neg(lo)
    # candidates: |lo|, |hi|
    alo = nlo if lo[0] else lo      # |lo|
    ahi = nhi if hi[0] else hi      # |hi|
    mx = ahi if mpf_lt(alo, ahi) else alo
    if mpf_lt(lo, fzero) and mpf_lt(fzero, hi):
        mn = fzero
    else:
        mn = alo if mpf_lt(alo, ahi) else ahi
    return iv.make_mpf((mn, mx))


def iv_max(x, y):
    """Interval max (componentwise on endpoints)."""
    from mpmath.libmp import mpf_lt
    (a1, b1), (a2, b2) = x._mpi_, y._mpi_
    return iv.make_mpf((a2 if mpf_lt(a1, a2) else a1, b2 if mpf_lt(b1, b2) else b1))


def iv_min(x, y):
    from mpmath.libmp import mpf_lt
    (a1, b1), (a2, b2) = x._mpi_, y._mpi_
    return iv.make_mpf((a1 if mpf_lt(a1, a2) else a2, b1 if mpf_lt(b1, b2) else b2))


def iv_thin_hi(x):
    """The thin interval [hi, hi] of x."""
    return iv.make_mpf((x._mpi_[1], x._mpi_[1]))


def iv_thin_lo(x):
    return iv.make_mpf((x._mpi_[0], x._mpi_[0]))


def fr(x):
    """Fraction from int / str / Fraction."""
    return Fraction(x)


def ball_from_fr(re, im):
    return Ball.from_fractions(Fraction(re), Fraction(im))


def ball_abs_hi(b):
    """Fraction upper bound of |b| for a Ball."""
    return iv_hi(b.abs_iv())


def ball_box_pad(b, r):
    """Ball b widened by the real iv r >= 0 in each coordinate (an [-r, r] x [-r, r] box added):
    encloses every point within distance r of b (since |Re w|, |Im w| <= |w|)."""
    pad = iv_hull(-r, r)
    return Ball(b.re + pad, b.im + pad)


def iv_pow_int(x, k):
    """x^k for a real iv and integer k >= 0 (mpmath's mpi power of an interval, true range)."""
    if k == 0:
        return iv_from_int(1)
    return x ** k


def iv_from_fr(x):
    return iv_from_fraction(Fraction(x))


# ---------------------------------------------------------------- the P15 functions on Balls

def _plog(b):
    """Principal Log of a Ball: ball.py's Ball.log on the half-plane RE+, IM+ or IM- (whose branch
    formulas have ranges (-pi/2, pi/2), (0, pi), (-pi, 0) -- all inside the principal range
    (-pi, pi]); refuses RE- (range (pi/2, 3pi/2), not principal) and boxes meeting 0."""
    # tag order IM+, IM-, RE+ (the arguments here have |Im| >= 100, so IM+/IM- always applies;
    # RE- is never accepted because its branch range (pi/2, 3pi/2) is not the principal one)
    if b.im > 0:
        tag = "IM+"
    elif b.im < 0:
        tag = "IM-"
    elif b.re > 0:
        tag = "RE+"
    else:
        raise ValueError("_plog: box not certified in IM+, IM- or RE+ -- principal branch not certified")
    return Ball(iv_log(b.abs2()) / 2, b.arg_branch(tag))


def alpha_ball(s):
    """alpha(s) = 1/(2s) + 1/(s-1) + (1/2) Log(s/(2 pi))   [P15 (9), p4]."""
    two_pi = 2 * iv_pi()
    inv2s = (s + s).recip()
    inv_sm1 = (s - Ball.from_int(1)).recip()
    lg = _plog(Ball(s.re / two_pi, s.im / two_pi))
    return inv2s + inv_sm1 + lg.scale_iv(iv_from_fr(Fraction(1, 2)))


def logM0_ball(s):
    """log M_0(s) by P15 (7), p4:
    Log s + Log(s-1) - (s/2) log pi + log(sqrt(2 pi)/16) + (s/2 - 1/2) Log(s/2) - s/2."""
    pi = iv_pi()
    half = iv_from_fr(Fraction(1, 2))
    one = Ball.from_int(1)
    s_half = s.scale_iv(half)
    t1 = _plog(s)
    t2 = _plog(s - one)
    t3 = s_half.scale_iv(iv_log(pi))                       # (s/2) log pi
    c = iv_log(2 * pi) / 2 - 4 * iv_log(iv_from_int(2))      # log(sqrt(2pi)/16) = (1/2)log(2pi) - 4 log 2
    t4 = (s_half - one.scale_iv(half)) * _plog(s_half)     # (s/2 - 1/2) Log(s/2)
    return t1 + t2 - t3 + Ball.real_interval(c) + t4 - s_half


def s_plus(z):
    """s_+ = (1 + y - i x)/2 = (1 - i z)/2 for the Ball z = x + iy."""
    half = iv_from_fr(Fraction(1, 2))
    return Ball((iv_from_int(1) + z.im) * half, -z.re * half)


def s_minus(z):
    """s_- = (1 - y + i x)/2 = (1 + i z)/2 = 1 - s_+."""
    half = iv_from_fr(Fraction(1, 2))
    return Ball((iv_from_int(1) - z.im) * half, z.re * half)


def gamma_and_dt(z, t_iv, a_plus=None, a_minus=None):
    """gamma(z) and d/dt gamma (D-F2) for the Ball z and real iv t; alpha values may be passed in.
    Returns (gamma, dgamma_dt, alpha(s_+), alpha(s_-))."""
    sp, sm = s_plus(z), s_minus(z)
    ap = alpha_ball(sp) if a_plus is None else a_plus
    am = alpha_ball(sm) if a_minus is None else a_minus
    quarter = iv_from_fr(Fraction(1, 4))
    d = (am * am - ap * ap).scale_iv(quarter)            # (alpha(s_-)^2 - alpha(s_+)^2)/4
    expo = d.scale_iv(t_iv) + logM0_ball(sm) - logM0_ball(sp)
    g = expo.exp()
    return g, g * d, ap, am


# ---------------------------------------------------------------- N and its constancy (D-F3)

def N_of(x_iv, t_iv):
    """Interval enclosure of sqrt(x/(4 pi) + t/16) and the integer floor of its endpoints."""
    r = iv.sqrt(x_iv / (4 * iv_pi()) + t_iv / 16)
    lo, hi = ivmpf_bounds(r)
    return r, lo.numerator // lo.denominator, hi.numerator // hi.denominator


def check_N_constant(x1, x2, t_lo, t_hi):
    """D-F3: returns N0 if floor(sqrt(x/4pi + t/16)) = N0 for all (x,t) in [x1,x2] x [t_lo,t_hi]
    (verified at the two extreme corners by directed rounding, monotonicity in x and t), and
    N0^2 <= x1/(4 pi); raises otherwise."""
    _, n_lo_lo, n_lo_hi = N_of(iv_from_fr(x1), iv_from_fr(t_lo))
    _, n_hi_lo, n_hi_hi = N_of(iv_from_fr(x2), iv_from_fr(t_hi))
    if not (n_lo_lo == n_lo_hi == n_hi_lo == n_hi_hi):
        raise ValueError("N is not certifiably constant on the box: corners give %s"
                         % ((n_lo_lo, n_lo_hi, n_hi_lo, n_hi_hi),))
    N0 = n_lo_lo
    # N0^2 <= x1/(4pi): 4 pi N0^2 <= x1, directed
    lhs_hi = iv_hi(4 * iv_pi() * iv_from_int(N0 * N0))
    if not lhs_hi <= Fraction(x1):
        raise ValueError("N0^2 <= x1/(4 pi) not certified")
    return N0


# ---------------------------------------------------------------- the direct evaluator (validation; small N)

def A_direct(s, t_iv, N):
    """A_t(s) = sum_{n<=N} b_n^t n^{-(s + (t/2) alpha(s))} by direct Ball summation (any Ball s)."""
    st = s + alpha_ball(s).scale_iv(t_iv / 2)
    total = Ball.from_int(1)                      # n = 1: log 1 = 0 -> term 1
    quarter = iv_from_fr(Fraction(1, 4))
    for n in range(2, N + 1):
        L = iv_log(iv_from_int(n))
        expo = Ball(t_iv * quarter * L * L, iv_from_int(0)) - st.scale_iv(L)
        total = total + expo.exp()
    return total


def ft_direct(z, t_iv, N):
    """f_t(z) = A_t(s_+) + gamma A_t(s_-) by direct summation (D-F1); returns (f, gamma)."""
    g, _, _, _ = gamma_and_dt(z, t_iv)
    return A_direct(s_plus(z), t_iv, N) + g * A_direct(s_minus(z), t_iv, N), g


# ---------------------------------------------------------------- the error majorant (D-F4, D-F5, (vi))

def F_majorant(sigma_iv, t_iv, N):
    """D-F5: an iv upper bound of F_{N,t}(sigma) = sum_{n<=N} b_n^t n^{-sigma}, valid for every
    sigma in the interval sigma_iv and t in t_iv (uses the lower endpoint of rho = sigma - (t/4) log N)."""
    logN = iv_log(iv_from_int(N))
    rho = sigma_iv - t_iv * logN / 4
    rho_lo = iv_thin_lo(rho)
    rlo = iv_lo(rho)
    Niv = iv_from_int(N)
    one = iv_from_int(1)
    if rlo <= 0:
        return Niv * iv_exp(-rho_lo * logN)                    # N * N^{-rho}
    if rlo == 1:
        return one + logN
    # 1 + (N^{1-rho} - 1)/(1 - rho); for rho in (0,1) both numerator and denominator positive,
    # for rho > 1 both negative -- the quotient is the true value either way (thin rho_lo).
    return one + (iv_exp((one - rho_lo) * logN) - one) / (one - rho_lo)


def defect_bound(x_iv, y_iv, t_iv, N, s_star_re_iv=None):
    """Upper bound (Fraction) of e_A + e_B + e_{C,0} uniform over the box x in x_iv, y in y_iv,
    t in t_iv, N fixed -- D-F4 + Prop 6.6(vi) as printed (p31).  Also returns the pieces.
    Requires x >= 200, 0 <= y <= 1, 0 <= t <= 1/2 (region (5); t = 0 by D-F9)."""
    pi = iv_pi()
    one = iv_from_int(1)
    if not (iv_lo(x_iv) >= 200 and iv_lo(y_iv) >= 0 and iv_hi(y_iv) <= 1
            and iv_lo(t_iv) >= 0 and iv_hi(t_iv) <= Fraction(1, 2)):
        raise ValueError("defect_bound: box outside region (5)")
    Niv = iv_from_int(N)
    logN = iv_log(Niv)
    lx = iv_log(x_iv / (4 * pi))                              # log(x/4pi) > 0
    # Re s_* enclosure on the box (D-F4: any sigma <= Re s_*)
    if s_star_re_iv is None:
        z = Ball(x_iv, y_iv)
        sp = s_plus(z)
        sstar = sp + alpha_ball(sp).scale_iv(t_iv / 2)
        s_star_re_iv = sstar.re
    sigma = iv_thin_lo(s_star_re_iv)
    F = F_majorant(sigma, t_iv, N)
    delta1 = (t_iv * t_iv / 16 * lx * lx + iv_from_fr(Fraction(626, 1000))) / (x_iv - iv_from_fr(Fraction(666, 100)))
    kap = t_iv * y_iv / (2 * (x_iv - 6))                      # (22) upper bound of |kappa|
    fac = one + iv_exp(iv_from_fr(Fraction(2, 100)) * y_iv) * iv_exp(kap * logN)
    eAB = (iv_exp(delta1) - one) * fac * F
    # (vi)
    ly = (one + y_iv) / 4
    pref = iv_exp(-ly * lx)                                   # (x/4pi)^{-(1+y)/4}
    mod = iv.sqrt(lx * lx + pi * pi / 4)                      # |log(x/4pi) + i pi/2|
    expo = -t_iv / 16 * lx * lx + (3 * mod + iv_from_fr(Fraction(358, 100))) / (x_iv - iv_from_fr(Fraction(852, 100)))
    l3 = iv_log(iv_from_int(3))
    br = one + iv_from_fr(Fraction(124, 100)) * (iv_exp(y_iv * l3) + iv_exp(-y_iv * l3)) / (Niv - iv_from_fr(Fraction(1, 8))) \
        + iv_from_fr(Fraction(692, 100)) / (x_iv - 12)
    eC0 = pref * iv_exp(expo) * br
    total = eAB + eC0
    return iv_hi(total), {"eAB_hi": iv_hi(eAB), "eC0_hi": iv_hi(eC0), "delta1_hi": iv_hi(delta1),
                          "F_hi": iv_hi(F), "sigma_lo": iv_lo(sigma)}


# ---------------------------------------------------------------- blocks and stored moments (D-F8a)

def make_blocks(N):
    """Blocks {1}, [2,3], [4,7], ..., [2^i, min(2^{i+1}-1, N)]; each with an exact dyadic center
    L_c (2^-30 grid) and a certified l_max (Fraction) with |log n - L_c| <= l_max on the block."""
    blocks = [{"n_lo": 1, "n_hi": 1, "Lc": Fraction(0), "lmax": Fraction(0)}]
    i = 1
    while 2 ** i <= N:
        n_lo, n_hi = 2 ** i, min(2 ** (i + 1) - 1, N)
        mid = float(math.log(n_lo) + math.log(n_hi)) / 2
        Lc = Fraction(round(mid * 2 ** 30), 2 ** 30)
        llo = iv_lo(iv_log(iv_from_int(n_lo)))
        lhi = iv_hi(iv_log(iv_from_int(n_hi)))
        lmax = max(Lc - llo, lhi - Lc)
        assert lmax > 0
        blocks.append({"n_lo": n_lo, "n_hi": n_hi, "Lc": Lc, "lmax": lmax})
        i += 1
    return blocks


def _ball_to_json(b):
    rlo, rhi = b.re_bounds()
    ilo, ihi = b.im_bounds()
    return [str(rlo), str(rhi), str(ilo), str(ihi)]


def _ball_from_json(l):
    return Ball.from_fraction_boxes((Fraction(l[0]), Fraction(l[1])), (Fraction(l[2]), Fraction(l[3])))


def compute_moments(series_name, c_re, c_im, N, R, out_path, prec=PREC_DEFAULT, log=print,
                    resume=True):
    """Stored moments m_r(B) = sum_{n in B} n^{-c} l_n^r (r = 0..R) and weights w(B) = sum n^{-Re c}
    for every block B of make_blocks(N), for the series center c = c_re + i c_im (exact Fractions).
    Written to out_path (JSON, exact endpoint Fractions) after every block; resumable."""
    set_prec(prec)
    blocks = make_blocks(N)
    doc = None
    if resume and os.path.exists(out_path):
        with open(out_path) as fh:
            doc = json.load(fh)
        if not (doc.get("series") == series_name and doc.get("N") == N and doc.get("R") == R
                and doc.get("c_re") == str(Fraction(c_re)) and doc.get("c_im") == str(Fraction(c_im))
                and doc.get("prec") == prec):
            log("  existing moment file has different parameters -- starting over")
            doc = None
    if doc is None:
        doc = {"series": series_name, "N": N, "R": R, "c_re": str(Fraction(c_re)), "c_im": str(Fraction(c_im)),
               "prec": prec, "mpmath_version": mpmath.__version__, "blocks": []}
    done = len(doc["blocks"])
    cre = iv_from_fr(c_re)
    cim = iv_from_fr(c_im)
    for bi in range(done, len(blocks)):
        B = blocks[bi]
        tB = time.time()
        Lc = iv_from_fr(B["Lc"])
        moms = [Ball.from_int(0) for _ in range(R + 1)]
        w = iv_from_int(0)
        for n in range(B["n_lo"], B["n_hi"] + 1):
            L = iv_log(iv_from_int(n)) if n > 1 else iv_from_int(0)
            npc = Ball(-cre * L, -cim * L).exp()          # n^{-c} = exp(-c log n)
            w = w + iv_exp(-cre * L)                      # n^{-Re c}
            ell = L - Lc
            pw = iv_from_int(1)
            moms[0] = moms[0] + npc
            for r in range(1, R + 1):
                pw = pw * ell
                moms[r] = Ball(moms[r].re + npc.re * pw, moms[r].im + npc.im * pw)
        doc["blocks"].append({"n_lo": B["n_lo"], "n_hi": B["n_hi"], "Lc": str(B["Lc"]), "lmax": str(B["lmax"]),
                              "w_hi": str(iv_hi(w)), "m": [_ball_to_json(m) for m in moms],
                              "seconds": round(time.time() - tB, 1)})
        tmp = out_path + ".tmp"
        with open(tmp, "w") as fh:
            json.dump(doc, fh)
        os.replace(tmp, out_path)
        log("  %s block %2d [%7d, %7d]: %.1fs  |m_0| ~ %.3e" % (
            series_name, bi, B["n_lo"], B["n_hi"], time.time() - tB, float(ball_abs_hi(moms[0]))))
    return doc


# ---------------------------------------------------------------- the Taylor evaluator (D-F8)

def _T(a_iv, J):
    """T_J(a) = a^J/J! e^a as an iv, for a real iv a >= 0."""
    return iv_pow_int(a_iv, J) / iv_from_int(math.factorial(J)) * iv_exp(a_iv)


class Series(object):
    """One frozen-alpha series (D-F8): center c, sign sgn, moments, and the frozen a = alpha(c)."""

    def __init__(self, doc, sgn):
        self.sgn = sgn
        self.N = doc["N"]
        self.R = doc["R"]
        self.c_re, self.c_im = Fraction(doc["c_re"]), Fraction(doc["c_im"])
        self.c = ball_from_fr(self.c_re, self.c_im)
        self.a = alpha_ball(self.c)                    # thin Ball enclosing alpha(c)
        self.blocks = []
        for B in doc["blocks"]:
            Lc = iv_from_fr(Fraction(B["Lc"]))
            lmax = iv_from_fr(Fraction(B["lmax"]))
            m = [_ball_from_json(x) for x in B["m"]]
            Qc = Ball.real_interval(Lc * Lc / 4) - self.a.scale_iv(Lc / 2)   # L_c^2/4 - a L_c/2
            pc = (Ball.real_interval(Lc) - self.a).scale_iv(iv_from_fr(Fraction(1, 2)))
            self.blocks.append({"Lc": Lc, "lmax": lmax, "w": iv_from_fr(Fraction(B["w_hi"])),
                                "m": m, "Qc": Qc, "pc": pc, "pc_abs_hi": iv_thin_hi(pc.abs_iv())})
        assert len(self.blocks) == len(make_blocks(self.N))
        self.logN = iv_log(iv_from_int(self.N))
        # Qmax >= max_{0<=L<=log N} |L^2/4 - a L/2| (D-F8b), by 64 subintervals
        lo, hi = ivmpf_bounds(self.logN)
        qm = iv_from_int(0)
        for k in range(64):
            Lk = iv_from_fraction_pair(hi * k / 64, hi * (k + 1) / 64)
            q = Ball.real_interval(Lk * Lk / 4) - self.a.scale_iv(Lk / 2)
            qm = iv_max(qm, iv_thin_hi(q.abs_iv()))
        self.Qmax = iv_thin_hi(qm)
        self.prepared = None

    def choose_orders(self, delta_abs_max, t_hi, eps):
        """Per block, the smallest (J, K) with J + 2K + 2 <= R whose D-F8a remainder bound
        (times the block weight, for r = 0) is <= eps at |delta| <= delta_abs_max, t <= t_hi."""
        orders = []
        for B in self.blocks:
            vmax = iv_from_fr(delta_abs_max) / 2 + iv_from_fr(t_hi) * B["pc_abs_hi"]
            a1 = vmax * B["lmax"]
            a2 = iv_from_fr(t_hi) * B["lmax"] * B["lmax"] / 4
            best = None
            for K in range(1, self.R):
                for J in range(1, self.R - 2 * K - 1):
                    TJ, TK = _T(a1, J), _T(a2, K)
                    bnd = (TJ * iv_exp(a2) + iv_exp(a1) * TK + TJ * TK) * B["w"]
                    if iv_hi(bnd) <= eps:
                        if best is None or J + K < best[0] + best[1]:
                            best = (J, K)
                        break
            if best is None:
                raise ValueError("cannot reach eps=%s with R=%d on block Lc=%s" % (eps, self.R, B["Lc"]))
            orders.append(best)
        return orders

    def prepare(self, t_iv, orders, want_dt):
        """Collapse the t-dependence: for each block and r in {0} (or {0,1,2}) the coefficients
        c^{(r)}_j = sum_{k<K} t^k m_{j+2k+r}/(j! k! 4^k), j < J, as Balls (t may be an interval)."""
        prep = []
        rs = (0, 1, 2) if want_dt else (0,)
        for B, (J, K) in zip(self.blocks, orders):
            coeffs = {}
            tpow = [iv_from_int(1)]
            for k in range(1, K):
                tpow.append(tpow[-1] * t_iv)
            for r in rs:
                cj = []
                for j in range(J):
                    acc = Ball.from_int(0)
                    for k in range(K):
                        coef = tpow[k] / iv_from_int(math.factorial(j) * math.factorial(k) * 4 ** k)
                        acc = acc + B["m"][j + 2 * k + r].scale_iv(coef)
                    cj.append(acc)
                coeffs[r] = cj
            prep.append({"J": J, "K": K, "coeffs": coeffs})
        self.prepared = (t_iv, orders, want_dt, prep)

    def evaluate(self, delta, t_iv, alpha_at_s, want_dt):
        """Enclosure of A_t(s(z)) (and of d/dt A_t(s(z)) if want_dt) for z = z_c + delta (delta a Ball),
        t in t_iv; alpha_at_s = alpha(s(z)) on the box (for the freezing correction, D-F8b).
        Requires prepare() with the same t_iv (a superset is also sound) and want_dt."""
        t_prep, orders, prep_dt, prep = self.prepared
        assert prep_dt or not want_dt
        assert iv_lo(t_prep) <= iv_lo(t_iv) and iv_hi(t_iv) <= iv_hi(t_prep)
        i_half = Ball(iv_from_int(0), iv_from_fr(Fraction(self.sgn, 2)))   # sgn * i/2
        idh = i_half * delta                                              # sgn * i delta/2
        dabs = iv_thin_hi(delta.abs_iv())
        thi = iv_thin_hi(t_iv)
        total = Ball.from_int(0)
        total_dt = Ball.from_int(0)
        rem = iv_from_int(0)
        rem_dt = iv_from_int(0)
        for B, P in zip(self.blocks, prep):
            J, K = P["J"], P["K"]
            v = idh + B["pc"].scale_iv(t_iv)
            BF = (idh.scale_iv(B["Lc"]) + B["Qc"].scale_iv(t_iv)).exp()
            # Horner for P_r = sum_j v^j c^{(r)}_j
            Pr = {}
            for r, cj in P["coeffs"].items():
                acc = cj[J - 1]
                for j in range(J - 2, -1, -1):
                    acc = acc * v + cj[j]
                Pr[r] = acc
            total = total + BF * Pr[0]
            # remainder (D-F8a): |BF| Bnd_B w(B) lmax^r
            vmax = iv_thin_hi((dabs / 2 + thi * B["pc_abs_hi"]))
            a1 = vmax * B["lmax"]
            a2 = thi * B["lmax"] * B["lmax"] / 4
            TJ, TK = _T(a1, J), _T(a2, K)
            bnd = iv_thin_hi((TJ * iv_exp(a2) + iv_exp(a1) * TK + TJ * TK) * B["w"] * iv_thin_hi(BF.abs_iv()))
            rem = rem + bnd
            if want_dt:
                dt_blk = BF * (B["Qc"] * Pr[0] + B["pc"] * Pr[1] + Pr[2].scale_iv(iv_from_fr(Fraction(1, 4))))
                total_dt = total_dt + dt_blk
                lm = B["lmax"]
                rem_dt = rem_dt + bnd * (iv_thin_hi(B["Qc"].abs_iv()) + B["pc_abs_hi"] * lm + lm * lm / 4)
        # freezing correction (D-F8b)
        diff = iv_thin_hi((alpha_at_s - self.a).abs_iv())
        eta = thi / 2 * diff * self.logN
        eta1 = diff * self.logN / 2
        # sigma_fr = Re c + sgn Im(delta)/2 + (t/2) Re a
        sigma_fr = iv_from_fr(self.c_re) + iv_from_fr(Fraction(self.sgn, 2)) * delta.im + t_iv / 2 * self.a.re
        Ffr = F_majorant(sigma_fr, t_iv, self.N)
        e_eta = iv_exp(eta)
        corr = iv_thin_hi((e_eta - 1) * Ffr)
        rem = rem + corr
        out = ball_box_pad(total, rem)
        if not want_dt:
            return out, None
        corr_dt = iv_thin_hi((self.Qmax * (e_eta - 1) + eta1 * e_eta) * Ffr)
        rem_dt = rem_dt + corr_dt
        return out, ball_box_pad(total_dt, rem_dt)


class FtEvaluator(object):
    """f_t(z) = A_t(s_+) + gamma A_t(s_-) (D-F1) from the two stored-moment series, on boxes."""

    def __init__(self, plus_doc, minus_doc, zc_re, zc_im):
        self.plus = Series(plus_doc, +1)
        self.minus = Series(minus_doc, -1)
        self.zc_re, self.zc_im = Fraction(zc_re), Fraction(zc_im)
        # consistency: centers must be s_+(z_c) and 1 - s_+(z_c)
        u_re, u_im = (1 + self.zc_im) / 2, -self.zc_re / 2
        assert (self.plus.c_re, self.plus.c_im) == (u_re, u_im), "plus-series center is not s_+(z_c)"
        assert (self.minus.c_re, self.minus.c_im) == (1 - u_re, -u_im), "minus-series center is not 1 - s_+(z_c)"
        assert self.plus.N == self.minus.N
        self.N = self.plus.N
        self.t_prep = None

    def prepare(self, t_iv, delta_abs_max, want_dt, eps=Fraction(1, 10 ** 28)):
        op = self.plus.choose_orders(delta_abs_max, iv_hi(t_iv), eps)
        om = self.minus.choose_orders(delta_abs_max, iv_hi(t_iv), eps)
        self.plus.prepare(t_iv, op, want_dt)
        self.minus.prepare(t_iv, om, want_dt)
        self.t_prep = t_iv
        self.orders = (op, om)

    def evaluate(self, z, t_iv, want_dt=False):
        """(f, dt_f, gamma, extras) on the Ball z (box) and iv t; dt_f is None unless want_dt."""
        delta = z - ball_from_fr(self.zc_re, self.zc_im)
        g, gdt, ap, am = gamma_and_dt(z, t_iv)
        Ap, Apdt = self.plus.evaluate(delta, t_iv, ap, want_dt)
        Am, Amdt = self.minus.evaluate(delta, t_iv, am, want_dt)
        f = Ap + g * Am
        if not want_dt:
            return f, None, g, (Ap, Am)
        fdt = Apdt + gdt * Am + g * Amdt
        return f, fdt, g, (Ap, Am)


# ---------------------------------------------------------------- reference (float) evaluation for validation


def _mpf_fr(v):
    """mp.mpf from an int / Fraction / str exactly (mp.mpf does not accept Fraction)."""
    from mpmath import mp
    v = Fraction(v)
    return mp.mpf(v.numerator) / v.denominator


def ft_mp_reference(x, y, t, N, dps=60):
    """f_t(x+iy) by (14)/(D-F1) in plain mp floating point at the given dps (an INDEPENDENT float
    pipeline, used only to test containment; never inside the producer)."""
    from mpmath import mp
    with mp.workdps(dps):
        x, y, t = _mpf_fr(x), _mpf_fr(y), _mpf_fr(t)

        def alpha(s):
            return 1 / (2 * s) + 1 / (s - 1) + mp.log(s / (2 * mp.pi)) / 2

        def logM0(s):
            return (mp.log(s) + mp.log(s - 1) - s / 2 * mp.log(mp.pi) + mp.log(mp.sqrt(2 * mp.pi) / 16)
                    + (s / 2 - mp.mpf(1) / 2) * mp.log(s / 2) - s / 2)

        sp = (1 + y - 1j * x) / 2
        sm = (1 - y + 1j * x) / 2
        ap, am = alpha(sp), alpha(sm)
        gam = mp.exp(t / 4 * (am ** 2 - ap ** 2) + logM0(sm) - logM0(sp))

        def A(s, a):
            st = s + t / 2 * a
            tot = mp.mpc(0)
            for n in range(1, N + 1):
                L = mp.log(n)
                tot += mp.exp(t / 4 * L * L - st * L)
            return tot

        return A(sp, ap) + gam * A(sm, am), gam


def Ht_over_Bt_reference(x, y, t, dps=120, pieces=None, umax=None):
    """H_t(x+iy)/B_t(x+iy) with H_t by mp.quad of the defining integral (P15 (4): H_t(z) =
    int_0^inf e^{t u^2} Phi(u) cos(zu) du, Phi(u) = sum_{n>=1} (2 pi^2 n^4 e^{9u} - 3 pi n^2 e^{5u}) exp(-pi n^2 e^{4u}))
    and B_t by (11), (10), (6).  Piecewise Gauss-Legendre on [0, umax] cut into `pieces` pieces.
    Returns (g, H, B, Hcheck) where Hcheck is a second quadrature with a different cut for a
    consistency estimate.  Independent float pipeline; validation only."""
    from mpmath import mp
    with mp.workdps(dps):
        x, y, t = _mpf_fr(x), _mpf_fr(y), _mpf_fr(t)
        z = mp.mpc(x, y)
        if umax is None:
            umax = mp.mpf(3) / 2
        # Phi tail: for u >= 0 and n >= n_max+1 the terms are < 3 pi^2 n^4 e^{9u} exp(-pi n^2 e^{4u});
        # with n_max = 14 the first omitted term is ~ 3e4 * exp(-pi*225) ~ 1e-303 at u = 0 and smaller for u > 0.
        n_max = 14

        def Phi(u):
            tot = mp.mpf(0)
            e4 = mp.exp(4 * u)
            e5 = mp.exp(5 * u)
            e9 = mp.exp(9 * u)
            for n in range(1, n_max + 1):
                tot += (2 * mp.pi ** 2 * n ** 4 * e9 - 3 * mp.pi * n ** 2 * e5) * mp.exp(-mp.pi * n * n * e4)
            return tot

        def integrand(u):
            return mp.exp(t * u * u) * Phi(u) * mp.cos(z * u)

        if pieces is None:
            pieces = int(20 + float(x) * float(umax) / 4)      # ~ 1.5 oscillation periods per piece
        pts = [umax * k / pieces for k in range(pieces + 1)]
        H = mp.quad(integrand, pts)
        pts2 = [umax * k / (pieces + 7) for k in range(pieces + 8)]
        H2 = mp.quad(integrand, pts2)

        def alpha(s):
            return 1 / (2 * s) + 1 / (s - 1) + mp.log(s / (2 * mp.pi)) / 2

        def M0(s):
            return (mp.mpf(1) / 8 * (s * (s - 1) / 2) * mp.pi ** (-s / 2) * mp.sqrt(2 * mp.pi)
                    * mp.exp((s / 2 - mp.mpf(1) / 2) * mp.log(s / 2) - s / 2))

        sp = (1 + y - 1j * x) / 2
        B = mp.exp(t / 4 * alpha(sp) ** 2) * M0(sp)
        return H / B, H, B, H2 / B


def point_in_ball_dist(b, zr, zi):
    """Exact distance-bound test helper: returns the smallest r (Fraction, as an upper bound via
    squares) such that the point (zr, zi) is within the box b padded by r, i.e. the max of the
    coordinate distances to the box (a valid bound since |w| >= |Re w|, |Im w| ... we need the
    Euclidean distance <= r: use sqrt of the sum of squared coordinate distances, upper-rounded)."""
    rlo, rhi = b.re_bounds()
    ilo, ihi = b.im_bounds()
    dr = max(Fraction(0), rlo - zr, zr - rhi)
    di = max(Fraction(0), ilo - zi, zi - ihi)
    d2 = dr * dr + di * di
    # upper bound of sqrt(d2) as a Fraction
    num = math.isqrt(d2.numerator * d2.denominator) + 1
    return Fraction(num, d2.denominator)


def _cli(argv):
    import argparse
    ap = argparse.ArgumentParser(description="ft_mp.py -- stored-moment computation (see module docstring)")
    sub = ap.add_subparsers(dest="cmd")
    m = sub.add_parser("moments", help="compute the stored moments of one series (resumable)")
    m.add_argument("--series", choices=("plus", "minus"), required=True)
    m.add_argument("--N", type=int, required=True)
    m.add_argument("--zc-re", required=True, help="box center x_c as an exact rational n/d")
    m.add_argument("--zc-im", required=True, help="box center y_c as an exact rational n/d")
    m.add_argument("--R", type=int, default=48)
    m.add_argument("--prec", type=int, default=PREC_DEFAULT)
    m.add_argument("--out", required=True)
    args = ap.parse_args(argv)
    if args.cmd == "moments":
        xc, yc = Fraction(args.zc_re), Fraction(args.zc_im)
        u_re, u_im = (1 + yc) / 2, -xc / 2
        if args.series == "plus":
            c_re, c_im = u_re, u_im
        else:
            c_re, c_im = 1 - u_re, -u_im
        t0 = time.time()
        print("ft_mp moments: series=%s N=%d c=%s + i(%s) R=%d prec=%d -> %s"
              % (args.series, args.N, c_re, c_im, args.R, args.prec, args.out), flush=True)
        compute_moments(args.series, c_re, c_im, args.N, args.R, args.out, prec=args.prec,
                        log=lambda s: print(s, flush=True))
        print("done in %.1fs" % (time.time() - t0), flush=True)
        return 0
    print(__doc__)
    return 0


if __name__ == "__main__":
    sys.exit(_cli(sys.argv[1:]))
