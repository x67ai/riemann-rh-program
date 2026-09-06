#!/usr/bin/env python3
"""plan_rows.py -- UNTRUSTED float64 PLANNING model for Lane A of the M2a certificate (D1, SPEC.md section 5).

NOT A CERTIFICATE.  This script chooses the row partition [N-, N+] of [N_start, N1 - 1], the y-pieces per row and
N1 (Lemma T, SPEC 5.4) with plain numpy float64; the two certified producer legs (p9_mp.py: mpmath-ball; p9_arb.py:
Arb/FLINT) recompute every number with directed rounding from this plan and are the only source of transcript data.
A row this model calls "OK" and a leg finds T <= 0 is a planning miss (re-plan finer), never a certificate error.

THE FLOOR IMPLEMENTED (derivation M, written out in PLAN.md section 2; P15 = arXiv:1904.12438v2, PDF page = printed page):
  f_t(x+iy) = A + gamma C,  A = sum_{n<=N} b_n n^{-s*},  C = sum_{n<=N} b_n n^{-s**},  s** = conj(s*) - y + kappa  (P15 (14), (92) p46)
  Euler-2 mollifier E := 1 - beta2, beta2 := b_2 2^{-s*}  (Lemma 10.1, p65, with alpha_n := b_n n^{-s*}: beta2 alpha_{n/2} = theta_n alpha_n,
  theta_n := b_2 b_{n/2}/b_n = exp(-(t/2)(log 2) log(n/2)) in (0,1]); for the conjugated C-series alpha_n := n^y b_n n^{-s*}:
  beta2 alpha_{n/2} = 2^{-y} theta_n alpha_n.  Lemma 10.1's two bounds give
     |E A| >= 1 - sum_{n=3}^{2N} m_n n^{-sigma},   |E conj(C0)| <= sum_{n=1}^{2N} m'_n n^{-sigma},   sigma := Re s*,
  with m_n, m'_n >= 0 the mollified coefficient moduli (parity cases in floor_sub below), C0 the kappa-free C
  (|C - C0| <= Z := sum n^y b_n n^{-sigma} (n^{|kappa|} - 1), P15 p52/(96)), and |E| <= 1 + b_2 2^{-sigma}.  Hence
     |f| >= (L_A - U_C)/(1 + beta) - Zbar   uniformly on the sub-box N in [N-,N+], y in [ya,yb],
  after bounding every coefficient at its worst corner: sigma >= sigma_{N-}(ya) (P15 (21)/(80); SPEC 5.4 step 2(b)),
  |gamma| n^y <= c (n/N-)^{ya} with c := e^{0.02 yb} rho_{N-} (P15 (20); SPEC step 2(c)), |kappa| <= k := t yb/(2(x_{N-}-6)) ((22)).
The Lemma-T tail row and the Theorem-1.3 defect E are modeled the same way (functions tail() and defect()).
"""
import argparse, json, math, sys, time
import numpy as np

T0 = 0.186; Y0 = 0.16733; YA = 0.7924646; N0 = 630783
PI = math.pi
LOG2 = math.log(2.0)
B2 = math.exp(T0 / 4 * LOG2 * LOG2)

def xN(N):      return 4 * PI * (N * N - T0 / 16)                     # (80)
def epsN(N):    return -(T0 / 4) * math.log1p(-T0 / (16 * N * N)) + T0 / (2 * xN(N) ** 2)
def sigmaN(N, y): return (1 + y) / 2 + (T0 / 2) * math.log(N) - epsN(N)  # SPEC 5.4 step 2(b)
def rhoN(N):    return (1 - T0 / (16 * N * N)) ** -0.5
def kN(N, y):   return T0 * y / (2 * (xN(N) - 6))

class Arrays:
    def __init__(self, nmax):
        self.nmax = nmax
        n = np.arange(1, nmax + 1, dtype=np.float64)
        self.L = np.log(n)
        self.b = np.exp(T0 / 4 * self.L * self.L)
        self.theta = np.ones(nmax)          # theta_n for even n (index n-1); 1 elsewhere (unused)
        ev = np.arange(2, nmax + 1, 2)
        self.theta[ev - 1] = np.exp(-(T0 / 2) * LOG2 * np.log(ev / 2.0))
        self.even = np.zeros(nmax, dtype=bool); self.even[1::2] = True

ARR = None

def floor_sub(Nlo, Nhi, ya, yb, want_parts=False):
    """Float model of the certified sub-box floor T_sub (derivation M)."""
    A = ARR
    N2 = 2 * Nhi
    assert N2 <= A.nmax
    sig = sigmaN(Nlo, ya)
    beta = B2 * 2.0 ** (-sig)
    c = math.exp(0.02 * yb) * rhoN(Nlo)
    k = kN(Nlo, yb)
    L = A.L[:N2]; b = A.b[:N2]; th = A.theta[:N2]; ev = A.even[:N2]
    n = np.arange(1, N2 + 1, dtype=np.float64)
    pw = np.exp(-sig * L)                        # n^{-sigma}
    # ---- A-part: 1 - sum_{n>=3} mbar_n n^{-sigma}
    mA = np.zeros(N2)
    odd = ~ev
    mA[odd & (n <= Nhi)] = b[odd & (n <= Nhi)]
    sel = ev & (n <= Nlo);            mA[sel] = (1 - th[sel]) * b[sel]
    sel = ev & (n > Nlo) & (n <= Nhi); mA[sel] = np.maximum(1 - th[sel], th[sel]) * b[sel]
    sel = ev & (n > Nhi);             mA[sel] = th[sel] * b[sel]
    mA[0] = 0.0; mA[1] = 0.0
    LA = 1.0 - float(np.sum(mA * pw))
    # ---- C-part: sum_{n>=1} mbar'_n n^{-sigma}
    w = c * np.exp(ya * (L - math.log(Nlo))) * b          # c (n/N-)^{ya} b_n, all n <= 2N+ (used only for n <= N+)
    wp = np.zeros(N2)                                     # w'_n = c ((n/2)/N-)^{ya} b_{n/2} b_2 for even n
    half = (np.arange(2, N2 + 1, 2) // 2) - 1
    wp[1::2] = c * np.exp(ya * (A.L[half] - math.log(Nlo))) * A.b[half] * B2
    mC = np.zeros(N2)
    mC[odd & (n <= Nhi)] = w[odd & (n <= Nhi)]
    fac = 1 - 2.0 ** (-yb) * th
    sel = ev & (n <= Nlo);             mC[sel] = w[sel] * fac[sel]
    sel = ev & (n > Nlo) & (n <= Nhi); mC[sel] = np.maximum(w[sel] * fac[sel], wp[sel])
    sel = ev & (n > Nhi);              mC[sel] = wp[sel]
    UC = float(np.sum(mC * pw))
    Zbar = (Nhi ** k - 1.0) * float(np.sum((w * pw)[:Nhi]))
    T = (LA - UC) / (1 + beta) - Zbar
    if want_parts:
        return T, dict(sigma=sig, beta=beta, c=c, k=k, LA=LA, UC=UC, Zbar=Zbar)
    return T

def crude(N, y):
    """SPEC 5.4 step 1 (indicative sanity check against row2_tail_indicative.log)."""
    A = ARR; L = A.L[:N]; b = A.b[:N]
    sig = sigmaN(N, y); x = xN(N)
    g = math.exp(0.02 * y) * (x / (4 * PI)) ** (-y / 2); k = kN(N, y)
    S = float(np.sum(b * np.exp(-sig * L))); B = g * float(np.sum(b * np.exp((y - sig + k) * L)))
    return 2 - S - B, S, B

def defect(Nlo, Nhi, ylo, yhi):
    """Float model of the Theorem-1.3 defect bound on the window x row (P-6/P-9; ft_mp D-F4/D-F5, producer_arb D-A2, Prop 6.6(vi) with SPEC D-2.4)."""
    x = xN(Nlo); q = x / (4 * PI); lq = math.log(q)
    sig = sigmaN(Nlo, ylo)
    d1 = (T0 * T0 / 16 * lq * lq + 0.626) / (x - 6.66)
    kap = T0 * yhi / (2 * (x - 6))
    rho = sig - (T0 / 4) * math.log(Nhi)
    F = 1 + (Nhi ** (1 - rho) - 1) / (1 - rho) if rho != 1 else 1 + math.log(Nhi)
    fac = 1 + math.exp(0.02 * yhi) * rhoN(Nlo) * Nhi ** kap
    eAB = (math.exp(d1) - 1) * fac * F
    mod = math.hypot(lq, PI / 2)
    eC0 = q ** (-(1 + ylo) / 4) * math.exp(-T0 / 16 * lq * lq + (3 * mod + 10.5) / (x - 12)) * (1 + 1.24 * (3 ** yhi + 3 ** (-yhi)) / (Nlo - 0.125))
    return eAB + eC0, eAB, eC0

def tail(N1):
    """Float model of the Lemma-T row (SPEC 5.4, P-10)."""
    A = ARR
    u1 = math.log(N1); eps = epsN(N1); sig1 = sigmaN(N1, Y0); rho1 = rhoN(N1)
    cg = math.exp(0.02) * rho1; k1 = kN(N1, YA)
    a = (1 - Y0) / 2 + eps; a2 = (1 + Y0) / 2 + eps + k1
    kT = max(math.sqrt(2 / (math.e * T0)), 2 / (math.e * T0 * u1))
    L = A.L[:N1]; b = A.b[:N1]
    Q1 = float(np.sum(b * np.exp(-sig1 * L)))
    sig2 = sig1 - Y0 - k1
    Q2 = cg * N1 ** (-Y0) * float(np.sum(b * np.exp(-sig2 * L)))
    Q3 = math.exp(a * u1 - T0 / 4 * u1 * u1) * kT
    Q4 = cg * N1 ** (-Y0) * math.exp(a2 * u1 - T0 / 4 * u1 * u1) * kT
    # E1 (derivation M-T in PLAN.md): x >= x_{N1}, N >= N1, y in [y0, yA]
    x = xN(N1); q = x / (4 * PI); lq = math.log(q)
    d1 = (T0 * T0 / 16 * lq * lq + 0.626) / (x - 6.66)
    rhoF = (1 + Y0) / 2 + (T0 / 4) * u1 - eps
    Fmax = 1 + 1 / (rhoF - 1)
    fac = 1 + math.exp(0.02 * YA) * rho1 * N1 ** k1
    eAB = (math.exp(d1) - 1) * fac * Fmax
    mod = math.hypot(lq, PI / 2)
    eC0 = q ** (-(1 + Y0) / 4) * math.exp(-T0 / 16 * lq * lq + (3 * mod + 10.5) / (x - 12)) * (1 + 1.24 * (3 ** YA + 3 ** (-YA)) / (N1 - 0.125))
    E1 = eAB + eC0
    S = Q1 + Q2 + Q3 + Q4 + E1
    side = dict(S1=eps < (1 + Y0) / 2, S2=u1 >= 2 * a / T0, S3=(1 - Y0) / 2 > eps + k1, S4=u1 >= 2 * a2 / T0)
    return S, dict(Q1=Q1, Q2=Q2, Q3=Q3, Q4=Q4, E1=E1, eps=eps, sigma1=sig1, sigma2=sig2, rho1=rho1, k1=k1, a=a, a2=a2, kT=kT, rhoF=rhoF, u1=u1), side

def main():
    global ARR
    ap = argparse.ArgumentParser()
    ap.add_argument("--nstart", type=int, default=N0)
    ap.add_argument("--nmax", type=int, default=12_000_000)
    ap.add_argument("--tmin", type=float, default=0.012, help="planning safety floor for T (certified legs need T > E ~ 1e-7; margin covers float+enclosure slack)")
    ap.add_argument("--margin", type=float, default=0.003, help="Lemma T: require Q1+..+E1 < 2 - margin")
    ap.add_argument("--out", default="rows-plan.json")
    ap.add_argument("--ypieces", default="0.16733,0.18,0.2,0.23,0.27,0.32,0.40,0.55,0.7924646")
    args = ap.parse_args()
    t0 = time.time()
    ARR = Arrays(args.nmax)
    print(f"arrays up to n = {args.nmax:,} built in {time.time()-t0:.1f} s", flush=True)
    # 1. sanity: the SPEC's indicative crude numbers
    for N in (630783, 1500000, 3000000, 6000000):
        for y in (Y0, YA):
            v, S, B = crude(N, y)
            print(f"  crude N={N:8d} y={y:.7f}  A={S:.4f} B={B:.4e}  2-A-B={v:+.4f}")
    # 1b. singleton probes at N0 (the paper's Table-1 row-2 floor is 0.0376 at (N0, y0) by Lemma 10.1, p64-66)
    for (ya, yb) in ((Y0, Y0 + 1e-9), (Y0, 0.18), (0.18, 0.20), (0.20, 0.23), (0.30, 0.32), (0.55, YA)):
        v, parts = floor_sub(N0, N0, ya, yb, want_parts=True)
        print(f"  singleton N0 piece [{ya:.5f},{yb:.5f}]: T={v:+.5f}  LA={parts['LA']:.4f} UC={parts['UC']:.4f} beta={parts['beta']:.4f} Zbar={parts['Zbar']:.2e}")
    for N in (700000, 1000000, 2000000, 5000000):
        v = floor_sub(N, N, Y0, 0.18); print(f"  singleton N={N} piece [y0,0.18]: T={v:+.5f}")
    # 2. N1 by bisection on Lemma T (float), then round UP to a multiple of 1000
    lo, hi = 1_000_000, args.nmax // 2
    Slo = tail(lo)[0]; Shi = tail(hi)[0]
    print(f"  Lemma T sum: N={lo}: {Slo:.4f}   N={hi}: {Shi:.4f}")
    assert Slo >= 2 - args.margin and Shi < 2 - args.margin
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if tail(mid)[0] < 2 - args.margin: hi = mid
        else: lo = mid
    N1_exact = hi
    N1 = ((N1_exact + 999) // 1000) * 1000
    S, parts, side = tail(N1)
    print(f"  N1 (least, margin {args.margin}) = {N1_exact:,}; rounded up N1 = {N1:,}: sum = {S:.5f}  parts = " +
          ", ".join(f"{k}={v:.5g}" for k, v in parts.items() if k in ('Q1','Q2','Q3','Q4','E1')) + f"  side {side}", flush=True)
    # 3. row partition from nstart to N1-1, adaptive N+ (largest with min-over-pieces floor >= tmin)
    yp = [float(v) for v in args.ypieces.split(",")]
    pieces = list(zip(yp[:-1], yp[1:]))
    rows = []
    Nlo = args.nstart
    nrow = 0
    while Nlo <= N1 - 1:
        # first piece only for the search (the lowest y-piece is the binding one), then confirm all pieces
        def ok(Nhi):
            return floor_sub(Nlo, Nhi, *pieces[0]) >= args.tmin
        if not ok(Nlo):
            print(f"  ROW {nrow}: singleton N={Nlo} fails piece {pieces[0]} with T={floor_sub(Nlo, Nlo, *pieces[0]):.5f}; refining y-piece")
            # refine the first piece by bisection until ok or width < 0.002
            ya, yb = pieces[0]
            while floor_sub(Nlo, Nlo, ya, yb) < args.tmin and yb - ya > 0.002:
                yb = (ya + yb) / 2
            if floor_sub(Nlo, Nlo, ya, yb) < args.tmin:
                print("  STOP: cannot certify even a singleton window with the finest y-piece; plan fails"); sys.exit(2)
            pieces = [(ya, yb), (yb, pieces[0][1])] + pieces[1:]
            continue
        # snap to the end if the whole remainder is one row; else geometric doubling then bisection on the width
        if ok(N1 - 1):
            Nhi = N1 - 1
        else:
            w = 1
            while Nlo + 2 * w <= N1 - 1 and ok(Nlo + 2 * w): w *= 2
            a, b_ = w, min(2 * w, N1 - 1 - Nlo)
            while b_ - a > max(1, w // 256):
                m = (a + b_) // 2
                if ok(Nlo + m): a = m
                else: b_ = m
            Nhi = min(Nlo + a, N1 - 1)
        Ts = [(p, floor_sub(Nlo, Nhi, *p)) for p in pieces]
        Tmin = min(v for _, v in Ts)
        while Tmin < args.tmin and Nhi > Nlo:          # a higher piece bound (rare): shrink
            Nhi = Nlo + max(1, (Nhi - Nlo) // 2)
            Ts = [(p, floor_sub(Nlo, Nhi, *p)) for p in pieces]; Tmin = min(v for _, v in Ts)
        E, eAB, eC0 = defect(Nlo, Nhi, Y0, YA)
        rows.append(dict(Nlo=Nlo, Nhi=Nhi, ypieces=[list(p) for p in pieces], T_float=Tmin, T_by_piece=[v for _, v in Ts], E_float=E))
        print(f"  ROW {nrow:3d}: [{Nlo:>8d}, {Nhi:>8d}] width {Nhi-Nlo+1:>7d}  T_min={Tmin:.5f} (piece {Ts[0][1]:.5f} .. {Ts[-1][1]:.5f})  E={E:.3e}  [{time.time()-t0:.0f}s]", flush=True)
        Nlo = Nhi + 1; nrow += 1
    plan = dict(kind="lane-a-row-plan", generated=time.strftime("%Y-%m-%d %H:%M:%S %Z"), model="float64 numpy (UNTRUSTED planning only)",
                t0="93/500", y0="16733/100000", yA="3962323/5000000", N_start=args.nstart, N1=N1, N1_least_float=N1_exact,
                tmin=args.tmin, margin=args.margin, nrows=len(rows), windows=N1 - args.nstart, rows=rows,
                tail=dict(N1=N1, sum_float=S, parts=parts, side=side))
    json.dump(plan, open(args.out, "w"), indent=1)
    print(f"plan written: {args.out}: {len(rows)} rows covering {N1 - args.nstart:,} windows [{args.nstart}, {N1-1}], N1 = {N1:,}; {time.time()-t0:.0f} s total")

if __name__ == "__main__":
    main()
