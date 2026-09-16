#!/usr/bin/env python3
"""campaign_lib.py -- ONE code path for the zero-side numerics campaign of Theorem M2 (C2, Session 22/23).
Contract: results/c2-m2/followups/PRICING.md section 2; operating rules: results/c2-m2/campaign/BRIEF.md.
The campaign is an INSTRUMENT (standing order 4): it decides constants and the detection-bandwidth law; nothing here
is a statement about RH.

Objects (separation-note.md section 0.1):
  B(v) = Z^-1 exp(-1/(1-4v^2)) on |v| < 1/2;  Bhat(z) = int B(v) e^{izv} dv;  c(lam) = Bhat(i lam) = int B cosh(lam v).
  h_f(r) = (r - t) Bhat(L (r - t));   W_Z(f) = sum_{gamma in Z} h_f(gamma) conj(h_f(conj gamma)).
  On-line noise N_Z = sum_{real gamma} (gamma - t)^2 Bhat(L (gamma - t))^2 >= 0;  orbit {+-t +- i delta}: -2 delta^2 c(delta L)^2 + E_-.

Primitives (the same functions as verify/dh_negative_control.py and verify/four_point_accounting.py, vectorized):
  * Bhat at real arguments: the trapezoid rule on M = 16384 uniform nodes in (-1/2, 1/2).  B is C^infinity with compact
    support, so the trapezoid rule is spectrally accurate; by Poisson summation its error is sum_{m != 0} Bhat(eta - 2 pi m M),
    below 1e-16 for |eta| <= ETA_SAFE = 4e4 (checked against mpmath quadrature in the rehearsal log).
  * c(lam) by the same rule with cosh (all terms positive: no cancellation).
  * Bhat at complex arguments and at large |eta| (the reflected term E_-, the reflected on-line points, the out-window
    orbit of PRICING 2(a) item (6)): the same Poisson-trapezoid rule in mpmath at a precision and node count chosen from
    the requested absolute target (bhat_mp).
  * Zeros: mpmath.zetazero(n) at mp.dps = 15, stored as (index n, gamma, |Z(gamma)| by mpmath.siegelz).

Truncation (PRICING 2(b), the clause-4 polynomial route, generalized): k integrations by parts give
  |Bhat(eta)| <= ||B^(k)||_1 / |eta|^k, so a real point at distance u contributes at most ||B^(k)||_1^2 / (L^{2k} u^{2k-2});
  with the shell count 2 C1 l_R per unit shell (note section 5, C1 = 1 operative for zeta -- stated as such, PRICING 2(b))
  the tail beyond radius U is  <= 2 l_R ||B^(k)||_1^2 L^{-2k} sum_{j >= floor(U)} j^{2-2k} <= 2 l_R N_k^2 L^{-2k} (U-2)^{3-2k}/(2k-3).
  The contract's radius is the k = 3 case with the record's ||B'''||_1 = 642.301; the campaign minimizes over 2 <= k <= 13
  with the norms computed by derivative_norms() (exact polynomial recursion + 30-digit quadrature on sign-constant pieces;
  k = 1, 2, 3 reproduce the record's 3.31428, 28.7726, 642.301).  Both radii are printed per row.
"""
import math, time, json, os, sys, datetime
import numpy as np
import mpmath as mp

# ----------------------------------------------------------------------------------------------------------------------
# record constants (separation-note.md, corrections sections; PRICING.md preamble)
B1 = 8.70                 # b_1 = sup |eta Bhat(eta)|^2, certified upper end
C1_ZETA = 2.4e9           # zeta's recorded density constant (MAJOR-1)
C_B = 2/math.sqrt(72*math.e)          # 0.14296065 (Lemma G1)
CB_BIG = None             # e^2/Z, set below once Z is known
R0 = 81.0
LAMBDA0 = 25.0
C0 = 4.0
REFL_C = 21.0             # reflection condition t >= 21 L
NORM_BPRIME_L2SQ = 16.62196535       # ||B'||_2^2 (zero_data_cost_run.log line 1)
NORM_B3_L1_RECORD = 642.3011963065986
DELTAS = (0.05, 0.1, 0.25)
L_GRID = [float(L) for L in range(4, 121, 2)]
DERIV_NORMS_RECORD = {   # ||B^(k)||_1, computed 2026-09-16 by derivative_norms(13) (30 digits); k = 1..3 match the record
    1: 3.31427535948, 2: 28.7726440417, 3: 642.301196307, 4: 38779.9672465, 5: 4291724.35138, 6: 766365507.977,
    7: 201117898544.0, 8: 7.28650765558e+13, 9: 3.48429007153e+16, 10: 2.12573067064e+19, 11: 1.61134800942e+22,
    12: 1.48562110881e+25, 13: 1.63707485619e+28}

def now(): return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %Z").strip()

# ----------------------------------------------------------------------------------------------------------------------
# the bump on the trapezoid nodes (double precision, vectorized)
M_NODES = 16384
ETA_SAFE = 4.0e4
_v = (np.arange(1, M_NODES) / M_NODES) - 0.5            # nodes strictly inside (-1/2, 1/2), step 1/M
with np.errstate(over='ignore', divide='ignore', invalid='ignore'):
    _Braw = np.exp(-1.0/(1.0 - 4.0*_v*_v))
_Braw[~np.isfinite(_Braw)] = 0.0
Z_TRAP = float(_Braw.sum()/M_NODES)                       # = Z to spectral accuracy (0.2219969080840397)
_wB = _Braw/(_Braw.sum())                                  # weights: sum = 1, so bhat_real(0) = 1 exactly
CB_BIG = math.e**2/Z_TRAP

def bhat_real(eta):
    """Bhat(eta) = int B(v) cos(eta v) dv for a real array eta (|eta| <= ETA_SAFE), vectorized, chunked."""
    eta = np.atleast_1d(np.asarray(eta, dtype=float))
    if np.any(np.abs(eta) > ETA_SAFE):
        raise ValueError("bhat_real: |eta| > ETA_SAFE = %g (aliasing region of the M = %d trapezoid rule)" % (ETA_SAFE, M_NODES))
    out = np.empty_like(eta)
    step = max(1, int(6e7 // M_NODES))
    with np.errstate(all='ignore'):        # Accelerate BLAS raises spurious FP flags on this matmul; the values are checked below
        for i in range(0, len(eta), step):
            out[i:i+step] = np.cos(np.outer(eta[i:i+step], _v)) @ _wB
    if not np.all(np.isfinite(out)): raise FloatingPointError("bhat_real: non-finite output")
    return out

# ---------------------------------------------------------------------------------------------------------------------
# tabulated transform for the center ensemble (many centers x many L): Bhat on a uniform eta-grid by ONE FFT of the bump's
# samples (the same trapezoid rule, M_FAST = 4096 nodes, aliasing at 2 pi M_FAST = 25736 >> ETA_FAST), then a cubic spline.
# Interpolation error <= h^4 max|Bhat''''|/384 <= (1.5e-3)^4/(16*384) ~ 1e-15 absolute; |Bhat(eta)| < 1e-18 beyond ETA_FAST
# = 2500 and is set to 0 there (a term u^2 Bhat^2 with u = 2500/L is then < 1e-30).  Checked against bhat_real in the log.
M_FAST = 4096
ETA_FAST = 2500.0
_fast = {}
def _build_fast():
    from scipy.interpolate import CubicSpline
    v = (np.arange(1, M_FAST)/M_FAST) - 0.5
    with np.errstate(all='ignore'):
        b = np.exp(-1.0/(1.0 - 4.0*v*v))
    b[~np.isfinite(b)] = 0.0
    w = b/b.sum()
    N = 1 << 24
    s = np.zeros(N); s[1:M_FAST] = w                      # sample j sits at v_j = -1/2 + j/M_FAST
    F = np.fft.rfft(s)                                     # F_k = sum_j w_j exp(-2 pi i j k/N)
    eta = 2*np.pi*M_FAST*np.arange(len(F))/N               # eta_k = 2 pi k M/N;  exp(-i eta_k v_j) = exp(i eta_k/2) exp(-2 pi i jk/N)
    keep = eta <= ETA_FAST + 5
    vals = np.real(np.exp(1j*eta[keep]/2)*F[keep])
    _fast['eta'] = eta[keep]; _fast['spline'] = CubicSpline(eta[keep], vals); _fast['h'] = eta[1] - eta[0]

def bhat_fast(eta):
    """Bhat(eta) for a real array by the tabulated cubic spline (|eta| <= ETA_FAST; 0 beyond).  For the ensemble only."""
    if not _fast: _build_fast()
    eta = np.abs(np.atleast_1d(np.asarray(eta, dtype=float)))
    out = np.zeros_like(eta)
    m = eta <= ETA_FAST
    out[m] = _fast['spline'](eta[m])
    return out

def noise_fast(t, gammas, L, U):
    """N_Z(t, L) over the zeros within U of t, with bhat_fast (ensemble use)."""
    u = gammas - t
    m = np.abs(u) <= U
    uu = u[m]
    bh = bhat_fast(L*uu)
    return float((uu*uu*bh*bh).sum())

def c_edge(lam):
    """c(lam) = int B(v) cosh(lam v) dv = Bhat(i lam), vectorized (positive terms, no cancellation); lam <= ~1400 in double."""
    lam = np.atleast_1d(np.asarray(lam, dtype=float))
    out = np.empty_like(lam)
    step = max(1, int(6e7 // M_NODES))
    with np.errstate(all='ignore'):
        for i in range(0, len(lam), step):
            out[i:i+step] = np.cosh(np.outer(lam[i:i+step], _v)) @ _wB
    if not np.all(np.isfinite(out)): raise FloatingPointError("c_edge: non-finite output (lam too large for double?)")
    return out

def G1(eta):
    """Lemma G majorant (G1): |Bhat(eta)| <= C_B (1 + (c_B/2) sqrt eta) exp(-c_B sqrt eta), eta >= 0 (rigorous)."""
    eta = np.asarray(eta, dtype=float)
    s = np.sqrt(np.maximum(eta, 0.0))
    return CB_BIG*(1 + C_B/2*s)*np.exp(-C_B*s)

def log_G1(eta):
    s = math.sqrt(max(eta, 0.0))
    return math.log(CB_BIG) + math.log1p(C_B/2*s) - C_B*s

# numerical envelope of |Bhat(eta)| for the estimates that are labeled [computed envelope, not proved]:
# saddle-point form A eta^{-3/4} exp(-sqrt(eta/2)) (endpoint singularity e^{-1/(2(1-x))} at x = 2v -> 1); A is fitted by
# fit_envelope() in the rehearsal and stored in ENVELOPE_A (default from the 2026-09-16 rehearsal run).
ENVELOPE_A = 9.0            # fitted 2026-09-16 (libtest / rehearsal log): 8.6-8.9 on eta = 1e3..5e4; the local rate falls 0.82 -> 0.73 toward 1/sqrt2
def log_env(eta):
    """log of the envelope estimate of |Bhat(eta)| [computed envelope, not proved]; eta >= 1."""
    eta = max(float(eta), 1.0)
    return math.log(ENVELOPE_A) - 0.75*math.log(eta) - math.sqrt(eta/2)

# ----------------------------------------------------------------------------------------------------------------------
# high-precision Poisson-trapezoid transform at complex argument (the reflected terms, the out-window orbit)
def bhat_mp(z, abs_target, max_work=4.0e7, check=False, alias_rate=0.6):
    """Bhat(z) = int B(v) e^{i z v} dv for complex z = xi - i y, by the trapezoid rule in mpmath.
    Error by Poisson summation = sum_{m != 0} Bhat(z - 2 pi m M); nodes M are chosen so that the nearest alias
    (at real distance 2 pi M - |xi|) is below abs_target by the envelope exp(-alias_rate sqrt eta') with the strip
    weight e^{|y|/2} (alias_rate = 0.6 is below the computed rates 0.85 -> 0.71; the rigorous G1 with c_B = 0.143
    would multiply the node count by 25 -- so this is a numerical evaluation, checked, not a proved enclosure), and
    the working precision covers the cancellation e^{|y|/2}/abs_target.  With check=True the value is recomputed
    with 3/2 the nodes and the difference is returned as the fourth item.  Returns (value, M, dps[, diff]) or
    (None, M, dps[, None]) when M*dps exceeds max_work (the caller then reports a bound instead of a value)."""
    xi = float(mp.re(z)); y = float(mp.im(z))
    need = math.log(1/abs_target) + abs(y)/2 + 3
    eta_alias = (need/alias_rate)**2
    M = int(math.ceil((abs(xi) + eta_alias)/(2*math.pi))) + 16
    if M % 2: M += 1
    dps = int(math.ceil((abs(y)/2 + 1)/math.log(10) + math.log10(1/abs_target) + 8))
    if M*dps > max_work:
        return (None, M, dps, None) if check else (None, M, dps)
    def run(Mn):
        with mp.workdps(dps):
            zz = mp.mpc(z); h = mp.mpf(1)/Mn
            s = mp.mpf(0); Zn = mp.mpf(0)
            for j in range(-Mn//2 + 1, Mn//2):
                v = j*h
                b = mp.exp(-1/(1 - 4*v*v))
                Zn += b
                s += b*mp.exp(1j*zz*v)
            return mp.mpc(s/Zn)          # the trapezoid normalization (Z by the same rule), as in bhat_real
    val = run(M)
    if not check: return val, M, dps
    M2 = M + M//2 + (M//2) % 2
    val2 = run(M2)
    return val, M, dps, abs(val - val2)

# ----------------------------------------------------------------------------------------------------------------------
# derivative norms and the truncation radius
def derivative_norms(kmax=13, dps=30):
    """||B^(k)||_1, k = 1..kmax: B_raw^(k) = exp(phi) Q_k(v)/(1-4v^2)^{2k}, phi = -1/(1-4v^2), with the exact integer
    polynomial recursion Q_{k+1} = -8v Q_k + Q_k' (1-4v^2)^2 + 16 k v Q_k (1-4v^2); sign changes of Q_k on (-1/2, 1/2)
    located by a fine scan + bisection (v = 0 always a breakpoint: odd k are odd functions), quadrature on each piece."""
    def pmul(a, b):
        r = [0]*(len(a)+len(b)-1)
        for i, x in enumerate(a):
            for j, y in enumerate(b): r[i+j] += x*y
        return r
    def padd(a, b):
        r = [0]*max(len(a), len(b))
        for i, x in enumerate(a): r[i] += x
        for i, x in enumerate(b): r[i] += x
        return r
    def pder(a): return [i*a[i] for i in range(1, len(a))] or [0]
    w = [1, 0, -4]; Q = [[1]]
    for k in range(0, kmax):
        q = Q[-1]
        Q.append(padd(padd(pmul([0, -8], q), pmul(pder(q), pmul(w, w))), pmul([0, 16*k], pmul(q, w))))
    norms = {}
    with mp.workdps(dps):
        Zn = mp.quad(lambda v: mp.exp(-1/(1-4*v*v)), [-0.5, -0.25, 0, 0.25, 0.5])
        for k in range(1, kmax+1):
            coeffs = list(reversed([mp.mpf(c) for c in Q[k]]))
            qk = lambda v: mp.polyval(coeffs, v)
            def Bk(v):
                v = mp.mpf(v)
                if abs(v) >= mp.mpf(1)/2: return mp.mpf(0)
                return mp.exp(-1/(1-4*v*v))*qk(v)/(1-4*v*v)**(2*k)/Zn
            grid = [mp.mpf(i)/4000 - mp.mpf(1)/2 for i in range(1, 4000)]
            vals = [qk(v) for v in grid]
            roots = []
            for i in range(len(grid)-1):
                if vals[i]*vals[i+1] < 0 and grid[i] != 0 and grid[i+1] != 0:
                    a, b = grid[i], grid[i+1]; fa = vals[i]
                    for _ in range(90):
                        m = (a+b)/2; fm = qk(m)
                        if fa*fm <= 0: b = m
                        else: a, fa = m, fm
                    roots.append((a+b)/2)
            pts = sorted(set([mp.mpf(-1)/2, mp.mpf(0), mp.mpf(1)/2] + roots))
            tot = mp.mpf(0)
            for i in range(len(pts)-1):
                tot += abs(mp.quad(Bk, [pts[i], pts[i+1]]))
            norms[k] = float(tot)
    return norms

def ell_R(t, L): return math.log(4 + t + R0*L)

def tail_bound(L, t, U, k, norms=DERIV_NORMS_RECORD, C1=1.0):
    """rigorous tail of N_Z beyond radius U >= 3 with the k-th derivative norm (C1 = 1 operative for zeta, stated as such)."""
    p = 2*k - 3
    return 2*C1*ell_R(t, L)*norms[k]**2/(L**(2*k))*(U-2)**(-p)/p

def U_kopt(L, t, target=1e-10, norms=DERIV_NORMS_RECORD, C1=1.0):
    """least radius U (over 2 <= k <= 13) with tail_bound <= target; returns (U, k)."""
    best = None
    for k in range(2, 14):
        p = 2*k - 3
        U = 2 + (2*C1*ell_R(t, L)*norms[k]**2/(L**(2*k))/(p*target))**(1.0/p)
        if best is None or U < best[0]: best = (U, k)
    return best

def U_contract3(L, t, target=1e-10):
    """the contract's radius (PRICING 2(b) (c)): U = 1 + (2 l_R ||B'''||_1^2/(3 L^6 target))^{1/3}, C1 = 1."""
    return max(2.0, 1 + (2*ell_R(t, L)*NORM_B3_L1_RECORD**2/(3*L**6*target))**(1/3))

def Lstar(delta, t, C1=1.0):
    return max(LAMBDA0/delta, C0/delta*(math.log(math.log(3+t)) + 2*math.log(1/delta) + math.log(2*B1*C1)))

def L_ann(delta, t):
    return 1.12*delta**(-0.07)*(math.log(t/(2*math.pi)))**0.89

def N_rvm(T):
    T = float(T)
    if T < 14: return 0.0
    return (T/(2*math.pi))*math.log(T/(2*math.pi*math.e)) + 7/8

# ----------------------------------------------------------------------------------------------------------------------
# zeros
def fetch_zeros(t, U, log=None, progress_every=500, dps=15):
    """all zeros gamma_n with |gamma_n - t| <= U, by mpmath.zetazero at mp.dps = dps; returns list of (n, gamma, |Z(gamma)|)
    plus a dict of checks (monotone, RvM count).  A progress line every progress_every zeros."""
    def say(s):
        if log: log(s)
    lo, hi = t - U, t + U
    t0 = time.time()
    with mp.workdps(dps):
        n = max(1, int(math.floor(N_rvm(lo))) - 6)
        g = float(mp.zetazero(n).imag)
        while g >= lo and n > 1:
            n -= 1; g = float(mp.zetazero(n).imag)
        while g < lo:
            n += 1; g = float(mp.zetazero(n).imag)
        # now gamma_n is the first zero >= lo
        zs = []; prev = -1.0; monotone = True
        while g <= hi:
            r = abs(float(mp.siegelz(g)))
            zs.append((n, g, r))
            if g <= prev: monotone = False
            prev = g
            if len(zs) % progress_every == 0:
                say("   [%s] %d zeros so far (n = %d, gamma = %.6f, |Z| = %.1e), %.1f s elapsed, %.3f s/zero"
                    % (now(), len(zs), n, g, r, time.time()-t0, (time.time()-t0)/len(zs)))
            n += 1; g = float(mp.zetazero(n).imag)
    dt = time.time() - t0
    checks = dict(monotone=monotone, count=len(zs), rvm_expected=N_rvm(hi) - N_rvm(lo),
                  index_lo=zs[0][0] if zs else None, index_hi=zs[-1][0] if zs else None,
                  seconds=dt, seconds_per_zero=dt/max(1, len(zs)), max_residual=max(z[2] for z in zs) if zs else None)
    say("   [%s] zeros done: %d zeros in [%.3f, %.3f], indices %s..%s, RvM count %.1f, monotone %s, max |Z(gamma)| %.1e, %.1f s (%.3f s/zero)"
        % (now(), len(zs), lo, hi, checks['index_lo'], checks['index_hi'], checks['rvm_expected'], monotone, checks['max_residual'], dt, checks['seconds_per_zero']))
    return zs, checks

# ----------------------------------------------------------------------------------------------------------------------
# the rows
def noise_at(t, gammas, L, U_data):
    """N_Z(L) over the zeros within U_row = min(U_data, ETA_SAFE/L); returns dict."""
    U_row = min(U_data, ETA_SAFE/L)
    u = gammas - t
    m = np.abs(u) <= U_row
    uu = u[m]
    bh = bhat_real(L*uu)
    terms = uu*uu*bh*bh
    N = float(terms.sum())
    j = int(np.argmin(np.abs(uu))) if len(uu) else None
    Uk, k = U_kopt(L, t)
    return dict(U_row=U_row, n_used=int(m.sum()), N_Z=N, near_gamma=float(t + uu[j]) if j is not None else None,
                near_term=float(terms[j]) if j is not None else None, U_kopt=Uk, k_opt=k,
                tail_at_U_row=tail_bound(L, t, U_row, k) if U_row >= 3 else float('nan'), U_contract3=U_contract3(L, t),
                tail_ok=(U_row >= Uk))

def reflected_online_bound(t, gammas, L):
    """rigorous Lemma-G bound on the sum over the reflected on-line points -gamma: sum 4 gamma^2 G1(L (gamma + t))^2 (log10)."""
    eta = L*(gammas + t)
    logs = 2*np.array([log_G1(e) for e in eta]) + np.log(4*gammas*gammas)
    mx = logs.max()
    return float((mx + math.log(np.exp(logs - mx).sum()))/math.log(10))

def reflected_online_estimate(t, gammas, L):
    eta = L*(gammas + t)
    logs = 2*np.array([log_env(e) for e in eta]) + np.log(4*gammas*gammas)
    mx = logs.max()
    return float((mx + math.log(np.exp(logs - mx).sum()))/math.log(10))

def E_minus_bound_log10(t, delta, L):
    """clause 1: |E_-| <= 2 (4t^2 + delta^2) e^{delta L} G1(2tL)^2  (rigorous), as log10."""
    return (math.log(2*(4*t*t + delta*delta)) + delta*L + 2*log_G1(2*t*L))/math.log(10)

def E_minus_estimate_log10(t, delta, L):
    """|E_-| ~ 2 (4t^2 + delta^2) e^{delta L} |Bhat(2tL)|_env^2 [computed envelope, not proved], as log10."""
    return (math.log(2*(4*t*t + delta*delta)) + delta*L + 2*log_env(2*t*L))/math.log(10)

def E_minus_direct(t, delta, L, rel=1e-6, max_work=4.0e7):
    """E_- = 2 Re[h_f(-t - i delta) conj(h_f(-t + i delta))], h_f(-t -+ i delta) = (-2t -+ i delta) Bhat(L(-2t -+ i delta)),
    by bhat_mp at one complex point (the other is its conjugate: B real and even).  Returns (E_-, M, dps) or (None, M, dps)."""
    est = 10**E_minus_estimate_log10(t, delta, L)
    # the target for Bhat: relative rel on the product ~ |Bhat|^2 -> absolute rel * |Bhat_est| on each factor
    bh_est = math.exp(log_env(2*t*L) + delta*L/2)
    val, M, dps = bhat_mp(mp.mpc(-2*t*L, -delta*L), max(bh_est*rel, 1e-300), max_work=max_work)
    if val is None: return None, M, dps
    with mp.workdps(dps):
        h1 = mp.mpc(-2*t, -delta)*val                     # h_f(-t - i delta)
        h2 = mp.mpc(-2*t, delta)*mp.conj(val)             # h_f(-t + i delta) = conj pattern
        Em = 2*mp.re(h1*mp.conj(h2))
    return float(Em), M, dps

def compute_rows(t, gammas, U_data, deltas=DELTAS, L_rows=None, log=None):
    """the row table: every measured quantity (1)-(7) of PRICING 2(a) at each (delta, L) on the L-grid plus the record points."""
    def say(s):
        if log: log(s)
    if L_rows is None: L_rows = list(L_GRID)
    rows = []
    Lset = sorted(set(L_rows) | {Lstar(d, t, 1.0) for d in deltas} | {Lstar(d, t, C1_ZETA) for d in deltas})
    cache = {}
    for L in Lset:
        cache[L] = noise_at(t, gammas, L, U_data)
        cache[L]['refl_online_bound_log10'] = reflected_online_bound(t, gammas, L)
        cache[L]['refl_online_est_log10'] = reflected_online_estimate(t, gammas, L)
        cache[L]['double_refl_bound_log10'] = (math.log(8*t*t) + 2*log_G1(2*t*L))/math.log(10)    # 8 t^2 Bhat(2tL)^2 (II.4 double at -t)
    lt = math.log(t/(2*math.pi))
    for d in deltas:
        Ls1 = Lstar(d, t, 1.0); Lsz = Lstar(d, t, C1_ZETA)
        for L in Lset:
            if L not in L_rows and L not in (Ls1, Lsz): continue
            c = float(c_edge(d*L)[0])
            nz = cache[L]
            N = nz['N_Z']
            main = -2*d*d*c*c
            WZ = N + main                          # E_- excluded from the sum (bounded / estimated / measured separately, item (7))
            WZp = N
            WZrep = N - nz['near_term'] + main
            bound6 = d*d*math.exp(d*L/2)
            clause4 = 2*B1*1.0*ell_R(t, L)/L**2
            model = lt*NORM_BPRIME_L2SQ/L**3
            refl_ok = (t >= REFL_C*L)
            inside = (L >= Ls1) and refl_ok
            inside_zeta = (L >= Lsz) and refl_ok
            row = dict(t=t, delta=d, L=L, is_record_point_C1_1=(L == Ls1), is_record_point_C1_zeta=(L == Lsz),
                       Lstar_C1_1=Ls1, Lstar_C1_zeta=Lsz, L_ann=L_ann(d, t),
                       inside_hypotheses=inside, inside_hypotheses_zeta_C1=inside_zeta, reflection_ok=refl_ok, deltaL=d*L, deltaL_ge_25=(d*L >= 25),
                       n_zeros_used=nz['n_used'], U_row=nz['U_row'], U_kopt=nz['U_kopt'], k_opt=nz['k_opt'], tail_bound_at_U_row=nz['tail_at_U_row'],
                       tail_le_1e_10=bool(nz['tail_ok']), U_contract_k3=nz['U_contract3'],
                       c_deltaL=c, main_term=main, N_Z=N, W_Zprime=WZp, W_Z=WZ, W_Zrep=WZrep, near_gamma=nz['near_gamma'], near_term=nz['near_term'],
                       W_Zdouble_minus_Zprime_bound_log10=nz['double_refl_bound_log10'],
                       clause6_bound=bound6, sep_over_clause6=(2*d*d*c*c)/bound6, W_Z_negative=(WZ < 0), bal3=(2*d*d*c*c >= 3*N),
                       clause4_bound_C1_1=clause4, clause4_over_N=(clause4/N if N > 0 else float('inf')), clause4_asserted=(L >= 50),
                       density_model=model, N_over_model=(N/model if model > 0 else float('nan')),
                       E_minus_bound_log10=E_minus_bound_log10(t, d, L), E_minus_est_log10=E_minus_estimate_log10(t, d, L),
                       E_minus_over_main_bound_log10=E_minus_bound_log10(t, d, L) - math.log10(2*d*d*c*c),
                       log10_exp_minus_L=-L/math.log(10), E_minus_direct=None,
                       refl_online_bound_log10=nz['refl_online_bound_log10'], refl_online_est_log10=nz['refl_online_est_log10'])
            rows.append(row)
    return rows

def fine_scan(t, gammas, U_data, deltas=DELTAS, L_lo=3.0, L_hi=120.0, step=0.1):
    """the derived bandwidths L_sign (least L with W_Z < 0, i.e. 2 delta^2 c^2 > N_Z) and L_bal3 (2 delta^2 c^2 >= 3 N_Z)
    on a fine L-grid; also L_bal(kappa) for kappa = 1 (= L_sign), 3, and the number of sign flips after the first crossing."""
    Ls = np.round(np.arange(L_lo, L_hi + step/2, step), 6)
    N = np.empty(len(Ls))
    for i, L in enumerate(Ls):
        N[i] = noise_at(t, gammas, float(L), U_data)['N_Z']
    out = dict(L_grid=[float(x) for x in Ls], N_Z=[float(x) for x in N], per_delta={})
    for d in deltas:
        c = c_edge(d*Ls)
        sig = 2*d*d*c*c
        res = {}
        for kap, name in ((1.0, 'L_sign'), (3.0, 'L_bal3')):
            ok = sig >= kap*N if kap > 1 else sig > N
            idx = np.argmax(ok) if ok.any() else None
            if idx is None:
                res[name] = None; res[name + '_flips_after'] = None
            else:
                res[name] = float(Ls[idx]); res[name + '_at_grid_bottom'] = bool(idx == 0)
                res[name + '_flips_after'] = int(np.sum(np.diff(ok[idx:].astype(int)) != 0))
        out['per_delta'][str(d)] = res
    return out

# ----------------------------------------------------------------------------------------------------------------------
# io
def sha256(path):
    import hashlib
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''): h.update(chunk)
    return h.hexdigest()

def write_rows(rows, prefix):
    import csv
    keys = list(rows[0].keys())
    with open(prefix + '.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=keys); w.writeheader()
        for r in rows: w.writerow(r)
    with open(prefix + '.json', 'w') as f:
        json.dump(rows, f, indent=0, default=float)
