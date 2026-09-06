#!/usr/bin/env python3
"""p9_mp.py -- Lane A producer, mpmath-ball leg (UNTRUSTED): window rows (SPEC P-9) and the Lemma-T tail row (P-10)
for the M2a certificate of Polymath15 Table 1 row 2 (results/d1-m2a/SPEC.md sections 5, 7.2, 7.4).

TRUST STATUS.  Producer-side code, outside the trust boundary (D-R3).  Its integers enter the trusted statement only
through the displayed hypotheses H2-A (`AsymEnclOK`: the row floors) and H-TAIL (`TailOK`: the Lemma-T reduction);
the kernel checks only C-A1..C-A6 on the emitted integers.  Never "fully machine-checked".  Platform trust is the
M1/M2a mpmath-ball assumption (results/d1-m1/ball.py `_inflate`: ring primitives correctly directed-rounded,
transcendental endpoints within 2^-(prec-16) relative of the truth).  This leg imports ball.py and ft_mp.py helpers
(its own leg) and NOTHING from the Arb leg; the only shared input is the UNTRUSTED row plan (rows-plan.json, data).

SOURCES (P15 = arXiv:1904.12438v2, PDF page = printed page; every formula re-read from pdftotext this session):
  (14)/(92) p6/p46: f_t = A + gamma C, A = sum_{n<=N} b_n n^{-s*}, C = sum_{n<=N} b_n n^{-s**}, s** = conj(s*) - y + kappa
      (the overline on s* in (14) per SPEC section 14 erratum 1; b_n = exp((t/4) log^2 n) (15)).
  (19) p6: N = floor(sqrt(x/4pi + t/16));  (80) p38: x_N <= x < x_{N+1}, x_N = 4 pi N^2 - pi t/4.
  (20) p6: |gamma| <= e^{0.02y} (x/4pi)^{-y/2};  (21) p6 / Prop 6.6(ii) p31: Re s* >= (1+y)/2 + (t/4) log(x/4pi) - (t/(2x^2))(...)_+;
  (22) p6: |kappa| <= t y/(2(x-6)).
  Lemma 10.1 p65 (Euler-2 mollifier): for complex alpha_1..alpha_N and beta_2 with beta_2 alpha_{n/2} on the segment [0, alpha_n]
      for every even n <= N:  |1-beta_2| |sum alpha_n| >= 2|alpha_1| - sum_{n=1}^{2N} |1_{n<=N} alpha_n - 1_{2|n} alpha_{n/2} beta_2|
      and  |1-beta_2| |sum alpha_n| <= sum_{n=1}^{2N} |...| (the proof's two displays, p65).
  Lemma 8.2 p42-43 (proof): b_n n^{-sigma} is decreasing in n for n <= N when sigma > (t/2) log N; the integral test (90);
      the substitution a = e^u turns the integral into int exp((1-sigma)u + (t/4)u^2) du, whose integrand is convex in u.
  Prop 6.6(iv),(v),(vi) p31 and (82)-(86) p39-41 for the defect (ft_mp.py D-F4/D-F5 and producer_arb.py D-A2 as the window form).
  p52 (96): n^{-kappa} = 1 + O_<=(n^{|kappa|} - 1).
  SPEC section 5.4 (Lemma T): the tail row Q1..Q4, E1 and (S1)-(S4), with sigma_N(y), eps_N, rho_N, k_N, c_gamma, a, a'', kappa_T.

DERIVATION M (the mollified triangle-inequality floor; PLAN.md section 2 carries the same text):
  M-1  Setting: t = t0, y in [ya, yb] subset [y0, yA], N = N(x) in [N-, N+], sigma := Re s*.  From (80) x >= x_N, so by (21)
       sigma >= sigma_N(y) := (1+y)/2 + (t/2) log N - eps_N with eps_N := -(t/4) log(1 - t/(16 N^2)) + t/(2 x_N^2) > 0 (SPEC 5.4
       step 2(b): log(x/4pi) >= 2 log N + log(1 - t/(16N^2)); the positive part in (21) or in 6.6(ii) is <= 1 for x >= 200, y <= 1).
       sigma_N(y) increases in N and y, so sigma >= sigma_lo := sigma_{N-}(ya) on the sub-box.
  M-2  Mollifier: E := 1 - beta_2, beta_2 := b_2 2^{-s*}.  With alpha_n := b_n n^{-s*}: beta_2 alpha_{n/2} = theta_n alpha_n,
       theta_n := b_2 b_{n/2}/b_n = exp(-(t/2)(log 2) log(n/2)) in (0, 1] (n even), so Lemma 10.1 applies to A, and
       |E A| >= 1 - sum_{n=3}^{2N} m_n n^{-sigma},  m_n := b_n (odd n <= N), (1-theta_n) b_n (even n <= N), theta_n b_n (even n in (N, 2N]);
       the n = 1 term is 1 and the n = 2 term vanishes (theta_2 = 1).  [|alpha_n - theta_n alpha_n| = (1-theta_n)|alpha_n|.]
  M-3  The C-series: C = C0 + R, C0 := sum n^y b_n n^{-conj(s*)}, |R| <= Z := sum n^y b_n n^{-sigma}(n^{|kappa|}-1) (p52).
       |E C0| = |E conj(C0)| (moduli multiply) and conj(C0) = sum alpha'_n, alpha'_n := n^y b_n n^{-s*} (real coefficients);
       beta_2 alpha'_{n/2} = 2^{-y} theta_n alpha'_n with 2^{-y} theta_n in (0,1), so Lemma 10.1's upper bound gives
       |E conj C0| <= sum_{n=1}^{2N} m'_n n^{-sigma},  m'_n := n^y b_n (odd n <= N), n^y b_n (1 - 2^{-y} theta_n) (even n <= N),
       2^{-y} theta_n n^y b_n (even n in (N, 2N]).
  M-4  |E f| >= |E A| - |gamma| |E C0| - |gamma| |E| Z and |E| <= 1 + b_2 2^{-sigma} <= 1 + beta_hi, beta_hi := b_2 2^{-sigma_lo};
       hence, when L_A - U_C >= 0:  |f| = |E f|/|E| >= (L_A - U_C)/(1 + beta_hi) - Zbar, with L_A <= |EA|-type lower bound,
       U_C >= |gamma||E C0|, Zbar >= |gamma| Z, all uniform on the sub-box (M-5..M-7).
  M-5  Uniformity in N: for theta_n <= 1/2 on n > N- (i.e. N- + 1 >= 2 e^{2/t}, certified), m_n(N) <= m_n(N+) and m'_n(N,.) <= m'_n(N+,.)
       for every N in [N-, N+] (even n in (N, N+]: theta_n b_n <= (1-theta_n) b_n; odd n in (N, N+]: 0 <= b_n; n > 2N: 0);
       and n^{-sigma} <= n^{-sigma_lo}.  So the N = N+ sums at sigma_lo bound every N in the row.
  M-6  Uniformity in y (the C-part): |gamma| n^y <= e^{0.02 y} (x/4pi)^{-y/2} n^y <= e^{0.02 yb} rho_{N-} (n/N-)^{ya} =: w_n / b_n
       for n <= N, since (x/4pi)^{-y/2} <= (N/rho_N)^{-y} with rho_N := (1 - t/(16N^2))^{-1/2} (SPEC step 2(c)), rho_N^y <= rho_N <= rho_{N-},
       (n/N)^y <= (n/N)^{ya} <= (n/N-)^{ya}; and (1 - 2^{-y} theta_n) <= (1 - 2^{-yb} theta_n).  |kappa| <= k := t yb/(2(x_{N-}-6)) (22).
  M-7  The parity re-indexing (n = 2m): b_{2m} = b_2 b_m m^{(t/2) log 2} and theta_{2m} b_{2m} = b_2 b_m, hence with
       G(s', a, b) := sum_{a<n<=b} b_n n^{-s'}:
         sum_{n=3}^{2N+} m_n n^{-sigma_lo} = G(sigma_lo,0,N+) - 1 - b_2 2^{-sigma_lo} G(sigma_lo,0,floor(N+/2)) + b_2 2^{-sigma_lo} G(sigma_lo,floor(N+/2),N+),
         sum_{n=1}^{2N+} mbar'_n n^{-sigma_lo} = c N-^{-ya} [ G(s',0,N+) - 2^{-yb} b_2 2^{-s'} G(s',0,floor(N+/2)) + b_2 2^{-sigma_lo} G(s',floor(N+/2),N+) ],
         s' := sigma_lo - ya, c := e^{0.02 yb} rho_{N-};   Zbar := (N+^k - 1) c N-^{-ya} G(s', 0, N+).
       Upper bounds use G_hi on the added terms and G_lo on the subtracted ones (all coefficients positive).
  M-8  G enclosure: exact ball summation for n <= Nc; for the range (M, b] with M >= Nc and (t/2) log b < s' (certified, Lemma 8.2's
       monotonicity):  sum_{n=M+1}^{b} phi(n) <= int_M^b phi = int_{log M}^{log b} psi(u) du <= trapezoid sum (psi = exp((1-s')u + (t/4)u^2)
       convex), and  sum_{n=M+1}^{b} phi(n) >= int_{M+1}^{b+1} phi >= midpoint sum (convexity, Jensen).  Evaluated in interval
       arithmetic with the exact rational s'.
  M-E  The row defect E (P-6/P-9 at the window's worst corner): e_A + e_B <= (e^{delta_1} - 1)(1 + e^{0.02 y} rho_{N-} N+^{t y/(2(x-6))}) F_{N+,t}(sigma_lo)
       with delta_1 of (84) (D-F4 with N <= rho_N sqrt(x/4pi) in place of N <= sqrt(x/4pi); |log(x/4pi n^2)| <= log(x/4pi) since
       x/(4pi n^2) >= 1 - t/(16N^2), D-A2), F by D-F5 (ft_mp.F_majorant, this leg); e_{C,0} by Prop 6.6(vi) AS PRINTED (this leg's
       convention) with x, y as intervals over the row x [y0, yA] and N = N- in the (N - 0.125) term; all inclusion-monotone.
  M-T  The tail row: Q1..Q4 exactly as SPEC 5.4 (sigma_{N1} = sigma_{N1}(y0), sigma'' = sigma_{N1} - y0 - k1, c_gamma = e^{0.02} rho_{N1},
       a = (1-y0)/2 + eps, a'' = (1+y0)/2 + eps + k1, kappa_T = max(sqrt(2/(e t)), 2/(e t u1)), Q3 = e^{psi(u1)} kappa_T,
       Q4 = c_gamma N1^{-y0} e^{psi''(u1)} kappa_T); E1 >= sup_{x >= x_{N1}, N >= N1, y in [y0,yA]} (e_A + e_B + e_{C,0}) by
       (82)-(84) p39-40: delta_1 decreasing in x (p40, Lemma 5.1(vi)); |gamma| N^{|kappa|} F(sigma - y) <= e^{0.02 yA} rho_{N1} N1^{k1} F(sigma)
       (p40 chain; N^{k_N} decreasing in N); F_{N,t}(sigma) <= 1 + 1/(rho_F - 1), rho_F := sigma - (t/4) log N >= (1+y0)/2 + (t/4) log N1 - eps_{N1} > 1
       (D-F5 with rho > 1); e_{C,0}: every factor of the 10.50 form is decreasing in x and in N (p41; SPEC 5.2), so its value at
       (x_{N1}, y in [y0,yA], N1) is the sup.
  M-Z  n^{|kappa|} - 1 <= N+^k - 1 for n <= N+ (k >= |kappa|), so Zbar := (N+^k - 1) c N-^{-ya} G(s', 0, N+) >= |gamma| Z.

ROUNDING (M1 D-P1/D-P2 discipline): every emitted integer is floor(K * lower endpoint) for floors and ceil(K * upper endpoint) for
error terms, computed on exact Fractions from the iv endpoints; no float touches an emitted number.

usage:
  p9_mp.py rows --plan PLAN.json --out DIR [--resume] [--rows i,j,...] [--K 1000000000000000000000000] [--Nc 10000] [--m 2000] [--prec 288]
  p9_mp.py tail --plan PLAN.json --out DIR [--K ...]
  p9_mp.py assemble --plan PLAN.json --out DIR --name asym-mp.json
  p9_mp.py selftest
U.S. English throughout.
"""
import argparse, json, math, os, sys, time
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(_HERE, "..", "..", "d1-m1")))
sys.path.insert(0, os.path.normpath(os.path.join(_HERE, "..")))
from ball import set_prec, iv_from_int, iv_from_fraction, ivmpf_bounds, iv_exp, iv_log, iv_pi, iv_hull  # noqa: E402
from ft_mp import iv_lo, iv_hi, iv_thin_lo, iv_thin_hi, F_majorant  # noqa: E402
from mpmath import iv  # noqa: E402

T0 = Fraction(93, 500); Y0 = Fraction(16733, 100000); YA = Fraction(3962323, 5000000); N0 = 630783
TRUST_LABEL = "kernel-checked modulo the displayed hypotheses H1, H2 (H2-B, H2-A, H-TAIL) and H3 (producers untrusted)"

def fr(x):
    return Fraction(x)

def ivf(x):
    return iv_from_fraction(Fraction(x))

def frac_str(q):
    q = Fraction(q); return f"{q.numerator}/{q.denominator}"

def floor_frac(q): return q.numerator // q.denominator
def ceil_frac(q): return -((-q.numerator) // q.denominator)

class Tables:
    """log n and b_n = exp((t/4) log^2 n) as iv for 1 <= n <= Nc (thin intervals; built once per run)."""
    def __init__(self, Nc, t_iv):
        self.Nc = Nc
        self.L = [None] * (Nc + 1)
        self.b = [None] * (Nc + 1)
        q = t_iv / 4
        for n in range(1, Nc + 1):
            L = iv_log(iv_from_int(n)) if n > 1 else iv_from_int(0)
            self.L[n] = L
            self.b[n] = iv_exp(q * L * L) if n > 1 else iv_from_int(1)

class Leg:
    def __init__(self, Nc=10000, m=2000, prec=288):
        set_prec(prec)
        self.prec = prec; self.Nc = Nc; self.m = m
        self.t = ivf(T0)
        self.pi = iv_pi()
        self.tab = Tables(Nc, self.t)
        self.log2 = iv_log(iv_from_int(2))
        self.b2 = self.tab.b[2]

    # ---- instance functions (M-1, M-6)
    def xN(self, N):
        return 4 * self.pi * (iv_from_int(N * N) - self.t / 16)
    def epsN(self, N):
        """eps_N = -(t/4) log(1 - t/(16 N^2)) + t/(2 x_N^2)  (> 0); returns the iv."""
        one = iv_from_int(1)
        return -(self.t / 4) * iv_log(one - self.t / (16 * iv_from_int(N * N))) + self.t / (2 * self.xN(N) ** 2)
    def sigma_lo(self, N, y):
        """exact Fraction lower bound of Re s* for N(x) >= N, y' >= y: (1+y)/2 + (t/2) log N - eps_N (M-1)."""
        s = (iv_from_int(1) + ivf(y)) / 2 + (self.t / 2) * iv_log(iv_from_int(N)) - self.epsN(N)
        return iv_lo(s)
    def rho_hi(self, N):
        one = iv_from_int(1)
        return iv_hi(one / iv.sqrt(one - self.t / (16 * iv_from_int(N * N))))
    def k_hi(self, N, y):
        return iv_hi(self.t * ivf(y) / (2 * (self.xN(N) - 6)))
    def theta(self, n):
        """theta_n = exp(-(t/2) log 2 log(n/2)), even n >= 2 (M-2)."""
        return iv_exp(-(self.t / 2) * self.log2 * iv_log(ivf(Fraction(n, 2))))

    # ---- M-8: G(s', a, b) = sum_{a<n<=b} b_n n^{-s'}, s' an exact Fraction; returns (lo, hi) Fractions
    def term(self, n, sp_iv):
        return self.tab.b[n] * iv_exp(-sp_iv * self.tab.L[n])
    def psi(self, u, sp_iv):
        return iv_exp((iv_from_int(1) - sp_iv) * u + (self.t / 4) * u * u)
    def I_upper(self, sp_iv, u0, u1):
        m = self.m; h = (u1 - u0) / m
        tot = self.psi(u0, sp_iv) + self.psi(u1, sp_iv)
        for i in range(1, m):
            tot = tot + 2 * self.psi(u0 + i * h, sp_iv)
        return iv_hi(tot * h / 2)
    def I_lower(self, sp_iv, u0, u1):
        m = self.m; h = (u1 - u0) / m
        tot = iv_from_int(0)
        for i in range(m):
            tot = tot + self.psi(u0 + (2 * i + 1) * h / 2, sp_iv)
        return iv_lo(tot * h)
    def G(self, sp, a, b):
        assert 0 <= a <= b
        sp = Fraction(sp); sp_iv = ivf(sp)
        if a == b:
            return Fraction(0), Fraction(0)
        M = min(b, max(a, self.Nc))
        head = iv_from_int(0)
        for n in range(a + 1, M + 1):
            head = head + self.term(n, sp_iv)
        lo, hi = iv_lo(head), iv_hi(head)
        if M < b:
            # Lemma 8.2 monotonicity: (t/2) log b < s'  (certified on endpoints)
            if not (iv_hi((self.t / 2) * iv_log(iv_from_int(b))) < sp):
                raise ValueError(f"G: summand not certified decreasing on ({M}, {b}] at s' = {float(sp)}")
            hi += self.I_upper(sp_iv, iv_log(iv_from_int(M)), iv_log(iv_from_int(b)))
            lo += self.I_lower(sp_iv, iv_log(iv_from_int(M + 1)), iv_log(iv_from_int(b + 1)))
        return lo, hi
    def G_direct(self, sp, a, b):
        """validation only: plain ball summation (needs the tables up to b)."""
        sp_iv = ivf(Fraction(sp)); tot = iv_from_int(0)
        for n in range(a + 1, b + 1):
            L = iv_log(iv_from_int(n)) if n > 1 else iv_from_int(0)
            tot = tot + iv_exp((self.t / 4) * L * L - sp_iv * L)
        return iv_lo(tot), iv_hi(tot)

    # ---- the sub-box floor (M-4..M-7)
    def sub_box(self, Nlo, Nhi, ya, yb):
        ya, yb = Fraction(ya), Fraction(yb)
        assert Y0 <= ya < yb <= YA and Nlo <= Nhi
        # M-5 side condition: theta_{N-+1} <= 1/2 (theta decreasing) -- checked on the first even n > N-
        n_even = Nlo + 1 if (Nlo + 1) % 2 == 0 else Nlo + 2
        if not (iv_hi(self.theta(n_even)) <= Fraction(1, 2)):
            raise ValueError("M-5 needs theta_n <= 1/2 for n > N-")
        sig = self.sigma_lo(Nlo, ya)                       # exact Fraction
        sp = sig - ya
        b2_2s = self.b2 * iv_exp(-ivf(sig) * self.log2)     # b_2 2^{-sigma_lo}
        b2_2sp = self.b2 * iv_exp(-ivf(sp) * self.log2)     # b_2 2^{-s'}
        beta_hi = iv_hi(b2_2s)
        rho = self.rho_hi(Nlo)
        c_iv = iv_exp(ivf(Fraction(2, 100) * yb)) * ivf(rho)
        cN = c_iv * iv_exp(-ivf(ya) * iv_log(iv_from_int(Nlo)))   # c N-^{-ya}
        k = self.k_hi(Nlo, yb)
        half = Nhi // 2
        GA_all = self.G(sig, 0, Nhi); GA_head = self.G(sig, 0, half); GA_tail = self.G(sig, half, Nhi)
        GC_all = self.G(sp, 0, Nhi); GC_head = self.G(sp, 0, half); GC_tail = self.G(sp, half, Nhi)
        # L_A lower bound (M-7): 2 - G_hi + lo(b2 2^-s) G_lo(head) - hi(b2 2^-s) G_hi(tail)
        LA_lo = 2 - GA_all[1] + iv_lo(b2_2s) * GA_head[0] - iv_hi(b2_2s) * GA_tail[1]
        # U_C upper bound: hi(cN) [ G_hi - lo(2^-yb b2 2^-s') G_lo(head) + hi(b2 2^-sigma) G_hi(tail) ]
        two_yb = iv_exp(-ivf(yb) * self.log2)
        UC_hi = iv_hi(cN) * (GC_all[1] - iv_lo(two_yb * b2_2sp) * GC_head[0] + iv_hi(b2_2s) * GC_tail[1])
        # Zbar (M-Z)
        Nk = iv_exp(ivf(k) * iv_log(iv_from_int(Nhi))) - iv_from_int(1)
        Zbar = iv_hi(Nk) * iv_hi(cN) * GC_all[1]
        num = LA_lo - UC_hi
        T_lo = (num / (1 + beta_hi) - Zbar) if num >= 0 else (num - Zbar)   # negative => the sub-box fails (recorded)
        return dict(Nlo=Nlo, Nhi=Nhi, ya=frac_str(ya), yb=frac_str(yb), T_lo=frac_str(T_lo), T_lo_float=float(T_lo),
                    sigma_lo=frac_str(sig), beta_hi=frac_str(beta_hi), c_hi=frac_str(iv_hi(c_iv)), rho_hi=frac_str(rho), k_hi=frac_str(k),
                    LA_lo=float(LA_lo), UC_hi=float(UC_hi), Zbar=float(Zbar),
                    G=dict(A_all=[float(GA_all[0]), float(GA_all[1])], A_head=[float(GA_head[0]), float(GA_head[1])], A_tail=[float(GA_tail[0]), float(GA_tail[1])],
                           C_all=[float(GC_all[0]), float(GC_all[1])], C_head=[float(GC_head[0]), float(GC_head[1])], C_tail=[float(GC_tail[0]), float(GC_tail[1])]))

    # ---- M-E: the row defect
    def defect_window(self, Nlo, Nhi, ylo=Y0, yhi=YA):
        one = iv_from_int(1); pi = self.pi; t = self.t
        x_iv = iv_hull(self.xN(Nlo), self.xN(Nhi + 1))
        y_iv = iv_hull(ivf(ylo), ivf(yhi))
        lx = iv_log(x_iv / (4 * pi))
        sig = self.sigma_lo(Nlo, ylo)
        F = F_majorant(iv_thin_lo(ivf(sig)), t, Nhi)                                   # D-F5, N = N+
        delta1 = (t * t / 16 * lx * lx + ivf(Fraction(626, 1000))) / (x_iv - ivf(Fraction(666, 100)))   # (84)
        kap = t * y_iv / (2 * (x_iv - 6))                                                # (22)
        fac = one + iv_exp(ivf(Fraction(2, 100)) * y_iv) * ivf(self.rho_hi(Nlo)) * iv_exp(kap * iv_log(iv_from_int(Nhi)))  # D-F4 + rho
        eAB = (iv_exp(delta1) - one) * fac * F
        # Prop 6.6(vi) as printed, x and y intervals, N = N-
        Nlo_iv = iv_from_int(Nlo)
        pref = iv_exp(-((one + y_iv) / 4) * lx)
        mod = iv.sqrt(lx * lx + pi * pi / 4)
        expo = -t / 16 * lx * lx + (3 * mod + ivf(Fraction(358, 100))) / (x_iv - ivf(Fraction(852, 100)))
        l3 = iv_log(iv_from_int(3))
        br = one + ivf(Fraction(124, 100)) * (iv_exp(y_iv * l3) + iv_exp(-y_iv * l3)) / (Nlo_iv - ivf(Fraction(1, 8))) + ivf(Fraction(692, 100)) / (x_iv - 12)
        eC0 = pref * iv_exp(expo) * br
        tot = eAB + eC0
        return iv_hi(tot), dict(eAB_hi=float(iv_hi(eAB)), eC0_hi=float(iv_hi(eC0)), delta1_hi=float(iv_hi(delta1)), F_hi=float(iv_hi(F)), sigma_lo=frac_str(sig))

    # ---- M-T: the tail row
    def tail_row(self, N1):
        one = iv_from_int(1); t = self.t; pi = self.pi
        u1 = iv_log(iv_from_int(N1))
        eps = self.epsN(N1); eps_hi = iv_hi(eps)
        sig1 = self.sigma_lo(N1, Y0)
        rho1 = self.rho_hi(N1)
        k1 = self.k_hi(N1, YA)
        cg = iv_exp(ivf(Fraction(2, 100))) * ivf(rho1)                       # c_gamma = e^{0.02} rho_1 (SPEC 5.4)
        a = (one - ivf(Y0)) / 2 + ivf(eps_hi)
        a2 = (one + ivf(Y0)) / 2 + ivf(eps_hi) + ivf(k1)
        e_iv = iv_exp(one)
        kT_1 = iv.sqrt(2 / (e_iv * t)); kT_2 = 2 / (e_iv * t * u1)
        kT_hi = max(iv_hi(kT_1), iv_hi(kT_2))
        psi1 = a * u1 - (t / 4) * u1 * u1
        psi2 = a2 * u1 - (t / 4) * u1 * u1
        N1_y0 = iv_exp(-ivf(Y0) * u1)
        Q1 = self.G(sig1, 0, N1)[1]
        sig2 = sig1 - Y0 - k1
        Q2 = iv_hi(cg * N1_y0) * self.G(sig2, 0, N1)[1]
        Q3 = iv_hi(iv_exp(psi1)) * kT_hi
        Q4 = iv_hi(cg * N1_y0 * iv_exp(psi2)) * kT_hi
        # E1 (M-T)
        x1 = self.xN(N1); lx = iv_log(x1 / (4 * pi))
        delta1 = (t * t / 16 * lx * lx + ivf(Fraction(626, 1000))) / (x1 - ivf(Fraction(666, 100)))
        rhoF = (one + ivf(Y0)) / 2 + (t / 4) * u1 - ivf(eps_hi)
        if not (iv_lo(rhoF) > 1):
            raise ValueError("M-T needs rho_F > 1")
        Fmax = one + one / (rhoF - one)
        fac = one + iv_exp(ivf(Fraction(2, 100) * YA)) * ivf(rho1) * iv_exp(ivf(k1) * u1)
        eAB = (iv_exp(delta1) - one) * fac * Fmax
        y_iv = iv_hull(ivf(Y0), ivf(YA))
        pref = iv_exp(-((one + y_iv) / 4) * lx)
        mod = iv.sqrt(lx * lx + pi * pi / 4)
        expo = -t / 16 * lx * lx + (3 * mod + ivf(Fraction(1050, 100))) / (x1 - 12)          # the 10.50 form (SPEC D-2.4)
        l3 = iv_log(iv_from_int(3))
        br = one + ivf(Fraction(124, 100)) * (iv_exp(y_iv * l3) + iv_exp(-y_iv * l3)) / (iv_from_int(N1) - ivf(Fraction(1, 8)))
        E1 = iv_hi(eAB + pref * iv_exp(expo) * br)
        side = dict(S1=bool(eps_hi < (1 + Y0) / 2), S2=bool(iv_lo(u1) >= iv_hi(2 * a / t)),
                    S3=bool((1 - Y0) / 2 > eps_hi + k1), S4=bool(iv_lo(u1) >= iv_hi(2 * a2 / t)))
        S = Q1 + Q2 + Q3 + Q4 + E1
        return dict(N1=N1, Q1=frac_str(Q1), Q2=frac_str(Q2), Q3=frac_str(Q3), Q4=frac_str(Q4), E1=frac_str(E1),
                    sum_float=float(S), sum_lt_2=bool(S < 2), side=side,
                    consts=dict(sigma1=frac_str(sig1), sigma2=frac_str(sig2), eps_hi=frac_str(eps_hi), k1=frac_str(k1), rho1=frac_str(rho1),
                                a_hi=frac_str(iv_hi(a)), a2_hi=frac_str(iv_hi(a2)), kappaT_hi=frac_str(kT_hi), rhoF_lo=frac_str(iv_lo(rhoF)),
                                u1=[frac_str(iv_lo(u1)), frac_str(iv_hi(u1))]),
                    floats=dict(Q1=float(Q1), Q2=float(Q2), Q3=float(Q3), Q4=float(Q4), E1=float(E1)))

# ---------------------------------------------------------------- driver: batches, STATUS, resume, assemble

def now():
    return time.strftime("%Y-%m-%d %H:%M:%S %Z")

def atomic_json(path, obj):
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(obj, f, indent=1)
    os.replace(tmp, path)

def update_status(out_dir, leg, st):
    atomic_json(os.path.join(out_dir, f"STATUS-{leg}.json"), st)
    merged = os.path.join(out_dir, "STATUS.json")
    try:
        cur = json.load(open(merged)) if os.path.exists(merged) else {}
    except Exception:
        cur = {}
    cur[leg] = st; cur["updated"] = now()
    atomic_json(merged, cur)

def load_plan(path):
    plan = json.load(open(path))
    rows = []
    for r in plan["rows"]:
        yp = [(Fraction(str(a)), Fraction(str(b))) for a, b in r["ypieces"]]
        rows.append(dict(Nlo=int(r["Nlo"]), Nhi=int(r["Nhi"]), ypieces=yp))
    return plan, rows

def run_rows(args):
    plan, rows = load_plan(args.plan)
    os.makedirs(os.path.join(args.out, "batches"), exist_ok=True)
    sel = list(range(len(rows))) if not args.rows else [int(v) for v in args.rows.split(",")]
    K = int(args.K)
    leg = Leg(Nc=args.Nc, m=args.m, prec=args.prec)
    started = now(); t_start = time.time()
    total_windows = sum(rows[i]["Nhi"] - rows[i]["Nlo"] + 1 for i in sel)
    done_windows = 0; errors = []; times = []
    for j, i in enumerate(sel):
        r = rows[i]
        path = os.path.join(args.out, "batches", f"mp-row_{i:04d}.json")
        if args.resume and os.path.exists(path):
            done_windows += r["Nhi"] - r["Nlo"] + 1
            print(f"[resume] row {i} present, skipped", flush=True); continue
        t0 = time.time()
        pieces = []; T_lo = None
        try:
            for (ya, yb) in r["ypieces"]:
                sb = leg.sub_box(r["Nlo"], r["Nhi"], ya, yb)
                pieces.append(sb)
                v = Fraction(sb["T_lo"])
                T_lo = v if T_lo is None else min(T_lo, v)
            E_hi, E_parts = leg.defect_window(r["Nlo"], r["Nhi"])
            T_int = floor_frac(K * T_lo); E_int = ceil_frac(K * E_hi)
            ok = (T_lo > 0) and (E_int < T_int)
            rec = dict(leg="mp", row_index=i, Nlo=str(r["Nlo"]), Nhi=str(r["Nhi"]), T=str(T_int), E=str(E_int), K=str(K), ok=ok,
                       T_lo=frac_str(T_lo), T_lo_float=float(T_lo), E_hi=frac_str(E_hi), E_hi_float=float(E_hi), E_parts=E_parts,
                       pieces=pieces, seconds=time.time() - t0, prec=args.prec, Nc=args.Nc, m=args.m, stamp=now())
            if not ok:
                errors.append(f"row {i}: T_lo={float(T_lo)} E_hi={float(E_hi)} -- floor not positive or E >= T")
        except Exception as ex:  # record and continue
            rec = dict(leg="mp", row_index=i, Nlo=str(r["Nlo"]), Nhi=str(r["Nhi"]), ok=False, error=repr(ex), seconds=time.time() - t0, stamp=now())
            errors.append(f"row {i}: {ex!r}")
        atomic_json(path, rec)
        times.append(time.time() - t0); done_windows += r["Nhi"] - r["Nlo"] + 1
        el = time.time() - t_start
        rem = len(sel) - j - 1
        eta = rem * (sum(times) / len(times)) / 3600 if times else None
        st = dict(phase="rows", leg="mp", rows_done=j + 1, rows_total=len(sel), windows_done=done_windows, windows_total=total_windows,
                  started=started, updated=now(), elapsed_s=el, eta_hours=eta, errors=errors, last_row=rec.get("row_index"),
                  last_T=rec.get("T_lo_float"), last_E=rec.get("E_hi_float"), last_seconds=rec.get("seconds"))
        update_status(args.out, "mp", st)
        print(f"row {i:3d} [{r['Nlo']},{r['Nhi']}] pieces={len(r['ypieces'])}  T_lo={rec.get('T_lo_float')}  E_hi={rec.get('E_hi_float')}  ok={rec.get('ok')}  {rec['seconds']:.1f}s", flush=True)
    st = dict(phase="rows-done", leg="mp", rows_done=len(sel), rows_total=len(sel), windows_done=done_windows, windows_total=total_windows,
              started=started, updated=now(), elapsed_s=time.time() - t_start, eta_hours=0.0, errors=errors)
    update_status(args.out, "mp", st)
    print("rows done:", json.dumps(st), flush=True)

def run_tail(args):
    plan, rows = load_plan(args.plan)
    os.makedirs(os.path.join(args.out, "batches"), exist_ok=True)
    K = int(args.K)
    leg = Leg(Nc=args.Nc, m=args.m, prec=args.prec)
    N1 = int(plan["N1"])
    t0 = time.time()
    tr = leg.tail_row(N1)
    ints = {k: str(ceil_frac(K * Fraction(tr[k]))) for k in ("Q1", "Q2", "Q3", "Q4", "E1")}
    ssum = sum(int(v) for v in ints.values())
    ok = tr["sum_lt_2"] and all(tr["side"].values()) and ssum < 2 * K
    rec = dict(leg="mp", N1=str(N1), K=str(K), ints=ints, sum_int=str(ssum), lt_2K=bool(ssum < 2 * K), ok=ok, seconds=time.time() - t0, stamp=now(), **tr)
    atomic_json(os.path.join(args.out, "batches", "mp-tail.json"), rec)
    update_status(args.out, "mp", dict(phase="tail-done", leg="mp", N1=N1, ok=ok, seconds=rec["seconds"], updated=now(), errors=[] if ok else ["tail row failed"]))
    print("tail:", json.dumps({k: rec[k] for k in ("N1", "ints", "sum_int", "lt_2K", "sum_float", "side", "ok", "seconds")}), flush=True)

def assemble(args):
    plan, rows = load_plan(args.plan)
    recs = []
    for i in range(len(rows)):
        p = os.path.join(args.out, "batches", f"mp-row_{i:04d}.json")
        if not os.path.exists(p):
            print(f"missing row {i}; not assembling"); sys.exit(1)
        recs.append(json.load(open(p)))
    tail = json.load(open(os.path.join(args.out, "batches", "mp-tail.json")))
    K = recs[0]["K"]
    doc = {"format": "M2a-barrier-transcript", "version": "1.0", "kind": "asymptotic", "lane": "asymptotic", "trust_label": TRUST_LABEL,
           "scales": {"K": K}, "t0": {"n": "93", "d": "500"}, "y0": {"n": "16733", "d": "100000"}, "yA": {"n": "3962323", "d": "5000000"},
           "rows": [{"Nlo": r["Nlo"], "Nhi": r["Nhi"], "T": r["T"], "E": r["E"]} for r in recs],
           "tail": {"N1": tail["N1"], **tail["ints"]},
           "producer": {"leg": "mpmath-ball (p9_mp.py)", "plan": os.path.basename(args.plan), "prec": recs[0].get("prec"), "Nc": recs[0].get("Nc"), "m": recs[0].get("m"),
                        "rows": [{k: r[k] for k in ("row_index", "T_lo", "E_hi", "E_parts", "pieces", "seconds", "ok")} for r in recs],
                        "tail": {k: tail[k] for k in ("Q1", "Q2", "Q3", "Q4", "E1", "consts", "side", "sum_float", "seconds", "ok")},
                        "stamp": now()}}
    atomic_json(os.path.join(args.out, args.name), doc)
    print("assembled", args.name, "rows", len(recs), "all ok:", all(r["ok"] for r in recs) and tail["ok"])

def selftest(args):
    leg = Leg(Nc=args.Nc, m=args.m, prec=args.prec)
    # (a) G enclosure vs direct ball summation at three exponents and ranges
    for sp, a, b in ((Fraction(18257, 10000), 0, 30000), (Fraction(18257, 10000) - Y0, 0, 30000), (Fraction(19, 10), 15000, 40000)):
        lo, hi = leg.G(sp, a, b); dlo, dhi = leg.G_direct(sp, a, b)
        ok = lo <= dlo and dhi <= hi
        print(f"G({float(sp):.5f},{a},{b}) = [{float(lo):.12f}, {float(hi):.12f}]  direct [{float(dlo):.12f}, {float(dhi):.12f}]  width {float(hi-lo):.2e}  contains: {ok}")
        assert ok
    # (b) the SPEC's indicative crude number at N0, y0 (row2_tail_indicative.log: A = 2.2789)
    sig = leg.sigma_lo(N0, Y0)
    lo, hi = leg.G(sig, 0, N0)
    print(f"sum_{{n<=N0}} b_n n^-sigma at sigma_lo={float(sig):.6f}: [{float(lo):.6f}, {float(hi):.6f}]  (indicative 2.2789)")
    print("selftest OK")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["rows", "tail", "assemble", "selftest"])
    ap.add_argument("--plan"); ap.add_argument("--out", default=".")
    ap.add_argument("--resume", action="store_true"); ap.add_argument("--rows", default="")
    ap.add_argument("--K", default=str(10 ** 24)); ap.add_argument("--Nc", type=int, default=10000); ap.add_argument("--m", type=int, default=2000)
    ap.add_argument("--prec", type=int, default=288); ap.add_argument("--name", default="asym-mp.json")
    args = ap.parse_args()
    {"rows": run_rows, "tail": run_tail, "assemble": assemble, "selftest": selftest}[args.mode](args)

if __name__ == "__main__":
    main()
