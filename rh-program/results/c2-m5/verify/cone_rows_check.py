#!/usr/bin/env python3
"""
C2 M5 pricing -- sanity computation (<= 10 minutes), Session 21, 2026-09-10.

Implements PRICING.md eq. (1.3): for an N-periodic marked configuration embedded at height T
(ell = log(T/2 pi), lattice u_k = k ell / N), the height-T cone row of C2's Sector I reads

    E_T(h) <= P(h) + 2 hhat(T),
    E_T(h) = (ell/N) sum_{k>=1} Re[c_k^on + c_k^pr cosh(u_k y)] h(u_k)/cosh(u_k/2),

for h in the strip-positive (Boas-Kac) cone Sigma_L: h >= 0, hhat >= 0, supp h in [-L, L].
We discretize h as an even piecewise-linear function on the lattice (variables h_0..h_{K-1},
h_K = 0, K = floor(N L / ell)), impose h_k >= 0 and the cosine polynomial
h_0 + 2 sum_k h_k cos(k phi) >= 0 on a phi-grid (hhat >= 0), normalize h_0 = 1, and MAXIMIZE
E_T(h) - P(h) - 2 hhat(T) as a linear program (HiGHS via scipy).  A positive maximum at some
rotation of the configuration = some cone row EXCLUDES the configuration at that (T, L).

P(h) = 4 sum_n Lambda(n) h(log n)/(n+1): exact sieve for n <= NP, PNT integral beyond
(4 int h(u) e^u/(e^u+1) du) -- labeled.  hhat(T) is the exact transform of the hat basis.

Configurations (all N_d/N = 5/6, marks {0,1,2} on the psi_1-zero grid, N in 6Z):
  crystal : 2 at s = 0 mod 6, 0 at s = 3 mod 6, 1 elsewhere     (c_k = 0 unless N/6 | k)
  dipole  : 2 at s = 0 mod 6, 0 at s = 1 mod 6, 1 elsewhere
  random  : 2 at N/6 random sites, 0 at N/6 other random sites (seeded)
  crystal_pairs_y : the crystal with each double replaced by an off-line pair at depth y

Outputs: verify/cone_rows_out.json and a printed summary.  No new mathematics; standing order 5.
"""
import json, math, sys, time
import numpy as np
from scipy.optimize import linprog

t_start = time.time()
OUT = {}

# ---------------------------------------------------------------- von Mangoldt sieve
NP = 2_000_000
def mangoldt(n_max):
    """Lambda(n) = log p for n = p^k, else 0 (numpy prime sieve, then prime powers)."""
    is_p = np.ones(n_max + 1, dtype=bool); is_p[:2] = False
    for i in range(2, int(n_max ** 0.5) + 1):
        if is_p[i]:
            is_p[i * i::i] = False
    lam = np.zeros(n_max + 1)
    for p in np.nonzero(is_p)[0]:
        q = int(p); lp = math.log(q)
        while q <= n_max:
            lam[q] = lp; q *= int(p)
    return lam
LAM = mangoldt(NP)
NN = np.arange(NP + 1, dtype=float)
LOGN = np.zeros(NP + 1); LOGN[1:] = np.log(NN[1:])
WPRIME = np.zeros(NP + 1); WPRIME[2:] = 4.0 * LAM[2:] / (NN[2:] + 1.0)
U_CUT = math.log(NP)   # exact prime sum below, PNT integral above

# ---------------------------------------------------------------- hat basis helpers
def hat_vals(u, k, D):
    """even piecewise-linear hat centered at u_k = k D (and -k D), width D, evaluated at |u|."""
    a = np.abs(u)
    v = np.clip(1.0 - np.abs(a - k * D) / D, 0.0, None)
    if k == 0:
        return v            # the k=0 hat is symmetric about 0 already (|u| <= D)
    return v

def prime_share_vector(K, D):
    """p_k with P(h) = sum_k h_k p_k for h = sum_k h_k Hat_k."""
    p = np.zeros(K)
    # exact part
    for k in range(K):
        lo, hi = max(0.0, (k - 1) * D), (k + 1) * D
        if lo >= U_CUT:
            break
        sel = (LOGN >= lo) & (LOGN <= min(hi, U_CUT)) & (NN >= 2)
        p[k] += np.sum(WPRIME[sel] * hat_vals(LOGN[sel], k, D))
    # PNT part for u > U_CUT: 4 int Hat_k(u) e^u/(e^u+1) du
    ug = np.linspace(U_CUT, (K + 1) * D, 20001) if (K + 1) * D > U_CUT else None
    if ug is not None:
        dens = 4.0 / (1.0 + np.exp(-ug))
        for k in range(K):
            if (k + 1) * D <= U_CUT:
                continue
            p[k] += np.trapezoid(hat_vals(ug, k, D) * dens, ug)
    return p

def pole_vector(K, D):
    """2 int h du = sum_k h_k q_k: hat_0 (base 2D, height 1) has area D -> q_0 = 2D;
    hat_k, k>=1, is two triangles (at +-u_k) of area D each -> q_k = 4D."""
    q = np.full(K, 4.0 * D)
    q[0] = 2.0 * D
    return q

def hhatT_vector(K, D, T):
    """2 hhat(T) = 2 int h(u) cos(T u) du = sum_k h_k r_k."""
    s = D * np.sinc(T * D / (2 * math.pi)) ** 2   # transform of one hat at 0 with the numpy sinc convention: sinc(x)=sin(pi x)/(pi x)
    r = np.zeros(K)
    r[0] = 2.0 * s
    for k in range(1, K):
        r[k] = 2.0 * 2.0 * s * math.cos(T * k * D)
    return r

# ---------------------------------------------------------------- configurations
def make_marks(N, kind, rng=None):
    m = np.ones(N, dtype=int)
    if kind == "crystal":
        m[0::6] = 2; m[3::6] = 0
    elif kind == "dipole":
        m[0::6] = 2; m[1::6] = 0
    elif kind == "random":
        idx = rng.permutation(N)
        m[idx[:N // 6]] = 2; m[idx[N // 6:N // 3]] = 0
    else:
        raise ValueError(kind)
    assert m.sum() == N and (m == 2).sum() == N // 6
    return m

def fourier_coeffs(marks, N, K, theta0, pairs=False):
    """c_k^on and c_k^pr for k = 1..K-1 (index k), rotation theta0 (gap units)."""
    s = np.arange(N)
    on_sites = np.where(marks == 1)[0]
    dbl_sites = np.where(marks == 2)[0]
    k = np.arange(K)
    def coeff(sites, weight):
        return weight * np.exp(-2j * math.pi * np.outer(k, sites + theta0) / N).sum(axis=1)
    c_on = coeff(on_sites, 1.0)
    if pairs:
        c_pr = coeff(dbl_sites, 2.0)
    else:
        c_on = c_on + coeff(dbl_sites, 2.0)
        c_pr = np.zeros(K, dtype=complex)
    return c_on, c_pr

def E_vector(N, ell, K, D, c_on, c_pr, y):
    """e_k with E_T(h) = sum_k h_k e_k (k>=1)."""
    k = np.arange(K)
    u = k * D
    e = (ell / N) * np.real(c_on + c_pr * np.cosh(u * y)) / np.cosh(u / 2.0)
    e[0] = 0.0
    return e

# ---------------------------------------------------------------- the cone-test LP
def cone_lp(obj, K, ngrid=None):
    """maximize sum_k h_k obj_k  s.t. h_0 = 1, h_k >= 0, h_0 + 2 sum_{k>=1} h_k cos(k phi) >= 0 on grid."""
    if ngrid is None:
        ngrid = 4 * K + 1
    phi = np.linspace(0.0, math.pi, ngrid)
    kk = np.arange(1, K)
    A = -np.ones((ngrid, K))
    A[:, 1:] = -2.0 * np.cos(np.outer(phi, kk))
    b = np.zeros(ngrid)
    bounds = [(1.0, 1.0)] + [(0.0, None)] * (K - 1)
    res = linprog(-obj, A_ub=A, b_ub=b, bounds=bounds, method="highs")
    if res.status != 0:
        return None, None, res.message
    h = res.x
    if not np.all(np.isfinite(h)) or np.max(np.abs(h)) > 1e6:
        return None, None, "non-finite or huge h (unbounded direction?)"
    # a-posteriori check of hhat >= 0 on a 4x finer grid
    phi2 = np.linspace(0.0, math.pi, 4 * ngrid)
    C = h[0] + 2.0 * (h[1:] @ np.cos(np.outer(kk, phi2)))
    return h, float(C.min()), None

def fejer(K, D, L):
    u = np.arange(K) * D
    return np.clip(1.0 - u / L, 0.0, None)

# ---------------------------------------------------------------- driver
N = 192
Ts = [1e6, 1e20]
L_list_rel = ["log2-", "1.0", "2.0", "4.0", "ell/6", "ell/3", "ell/2", "ell"]
rng = np.random.default_rng(20260910)
OUT["N"] = N
OUT["runs"] = []
summary_lines = []

for T in Ts:
    ell = math.log(T / (2 * math.pi))
    D = ell / N
    Ls = []
    for tag in L_list_rel:
        if tag == "log2-": L = math.log(2) * 0.999
        elif tag.startswith("ell") or tag.endswith("ell"):
            L = eval(tag.replace("ell", str(ell)))
        else: L = float(tag)
        Ls.append((tag, L))
    configs = {"crystal": make_marks(N, "crystal"), "dipole": make_marks(N, "dipole"),
               "random": make_marks(N, "random", rng)}
    for cname, marks in configs.items():
        variants = [("doubles", False, 0.0)]
        if cname == "crystal":
            variants += [("pairs_y=0.08", True, 0.08)]
        for vname, pairs, y in variants:
            if T > 1e13 and cname != "crystal":
                continue   # keep under the time cap; the large-T run is the asymptotic check
            if cname == "random":
                rots = np.linspace(0, N, 8, endpoint=False)
            else:
                rots = np.arange(0, 6, 1.0)
            for tag, L in Ls:
                if T > 1e13 and tag in ("1.0", "4.0"):
                    continue
                K = int(math.floor(L / D))
                if K < 2:
                    continue
                pvec = prime_share_vector(K, D)
                rvec = hhatT_vector(K, D, T)
                qvec = pole_vector(K, D)
                best = {"max_violation": -1e99}
                fejer_ratio_max = -1e99
                for th in rots:
                    c_on, c_pr = fourier_coeffs(marks, N, K, th, pairs=pairs)
                    evec = E_vector(N, ell, K, D, c_on, c_pr, y)
                    obj = evec - pvec - rvec
                    h, cmin, msg = cone_lp(obj, K)
                    if h is None:
                        best = {"error": msg}; break
                    val = float(obj @ h)
                    if val > best["max_violation"]:
                        best = {"max_violation": val, "rotation": float(th), "E_T": float(evec @ h),
                                "P": float(pvec @ h), "two_hhatT": float(rvec @ h), "pole_2inth": float(qvec @ h),
                                "hhat_min_check": cmin, "K": K}
                    hf = fejer(K, D, L)
                    Pf = float(pvec @ hf)
                    Ef = float(evec @ hf)
                    fejer_ratio_max = max(fejer_ratio_max, Ef / Pf if Pf > 0 else (math.inf if Ef > 1e-12 else 0.0))
                best.update({"T": T, "ell": ell, "config": cname, "variant": vname, "L_tag": tag, "L": L,
                             "fejer_E_over_P_max": fejer_ratio_max,
                             "fejer_P_over_pole": float((pvec @ fejer(K, D, L)) / (qvec @ fejer(K, D, L)))})
                OUT["runs"].append(best)
                flag = "VIOLATED" if best.get("max_violation", -1) > 1e-9 else "holds"
                summary_lines.append(f"T=1e{int(round(math.log10(T)))} {cname:8s} {vname:13s} L={tag:6s} ({L:6.2f}) K={K:4d} "
                                     f"maxLP[E-P-2hhat]={best.get('max_violation', float('nan')):+.4e} {flag:8s} "
                                     f"Fejer E/P max={fejer_ratio_max:.3e} P/pole={best['fejer_P_over_pole']:.3f}")
                print(summary_lines[-1], flush=True)
                with open(__file__.replace("cone_rows_check.py", "cone_rows_out.json"), "w") as f:
                    json.dump(OUT, f, indent=1, default=float)

# ---------------------------------------------------------------- depth-blindness table (Sec. 1.3)
depth = []
for yv in [0.01, 0.02, 0.05, 0.08, 0.1, 0.2, 0.3, 0.4, 0.45]:
    row = {"y": yv, "limit_2pi(1/cos(pi y)-1)": 2 * math.pi * (1 / math.cos(math.pi * yv) - 1)}
    for L in [5, 10, 20, 40, 80]:
        u = np.linspace(0, L, 200001)
        row[f"L={L}"] = float(np.trapezoid(2 * (1 - u / L) * (np.cosh(u * yv) - 1) / np.cosh(u / 2), u))
    depth.append(row)
OUT["depth_blindness_Delta_over_h0_Fejer"] = depth

# ---------------------------------------------------------------- prime share vs pole for Fejer(L) (exact primes to NP)
ps = []
for L in [0.5, 1.0, 2.0, 3.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0]:
    sel = (NN >= 2) & (LOGN <= L)
    P = float(np.sum(WPRIME[sel] * (1 - LOGN[sel] / L)))
    ps.append({"L": L, "P_Fejer_exact_primes": P, "pole_2intw": 2 * L, "ratio": P / (2 * L)})
OUT["prime_share_vs_pole_Fejer"] = ps

# ---------------------------------------------------------------- low-mode witness for the random config at L < log 2
OUT["elapsed_s"] = time.time() - t_start
OUT["summary"] = summary_lines
with open(__file__.replace("cone_rows_check.py", "cone_rows_out.json"), "w") as f:
    json.dump(OUT, f, indent=1, default=float)
print("\nDEPTH BLINDNESS Delta/h0 for Fejer(L) vs limit 2pi(1/cos(pi y)-1):")
for r in depth:
    print(f"  y={r['y']:.2f}  " + "  ".join(f"L={L}: {r[f'L={L}']:.4e}" for L in [5, 10, 20, 40, 80]) + f"   limit={r['limit_2pi(1/cos(pi y)-1)']:.4e}")
print("\nPRIME SHARE P(Fejer_L) vs pole 2L (exact primes to 2e6):")
for r in ps:
    print(f"  L={r['L']:5.1f}  P={r['P_Fejer_exact_primes']:8.4f}  2L={r['pole_2intw']:6.2f}  ratio={r['ratio']:.4f}")
print(f"\nelapsed {OUT['elapsed_s']:.1f} s")
