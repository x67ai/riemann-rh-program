#!/usr/bin/env python3
"""
A4 M2 gate -- SPEC verification computations (standing order 5: re-derive, never recall).

Verifies, by numerical routes independent of the hand derivations recorded in SPEC.md:
  V1. Sine-Gram moments m2(lambda; v), m3(lambda; v) via Fourier-side quadrature
      against the closed forms  m2 = 1/lam + lam/3,  m3 = 1 + 1/lam^2  (flat window),
      and produces the cos-window budget table (theta-scan).
  V2. The recalled v5 SS7.3 margin (2 m2 - m3) at lambda=1 with window v = cos(1.6 sigma)
      (recalled value 0.68524 -- verify).
  V3. The exact isolated pair-block law: eigenvalues m(1 +/- A(w)),
      A(w) = int v(s) cosh(2 w s) ds / int v ds, by direct matrix assembly
      (also verifies position-independence, i.e. the S=0 orthogonality).
  V4. CUE Monte-Carlo cross-check of m2, m3 at lambda in {1, 1/2} (flat window),
      n = 512, with finite-size trend at n = 256.
  V5. The garnish-capacity fuzz constant: continuum optimum (5/sqrt(3)) sqrt(C_led * eps)
      via an explicit LP (HiGHS) on a discretized height grid, vs the adjudicator's
      two-term dyadic value 2 sqrt(C_led * eps).
  V6. The per-zero isolated-block identity  c = 3F - 2 + (m-1)(m-2)  (atoms) and
      c = 3F - 2 (pairs, all depths) -- exact symbolic check on the block law.
  V7. The ppp cubic resonance constant sum_p (log p)^3/(p-1)^2 (sieve to 3e6; expect ~2.3158).

Outputs: verify_out.json + console table. Single process, light memory (thermal-safe).
"""
import json, math, time
import numpy as np

OUT = {}

# ---------------------------------------------------------------- windows
def u_hat(alpha, lam, theta):
    """psi-hat(alpha) = v(alpha/lam)/(lam * int v), support |alpha| <= lam/2.
       v(sigma) = cos(2*theta*sigma) on [-1/2,1/2] (theta=0 -> flat)."""
    alpha = np.asarray(alpha, dtype=float)
    out = np.zeros_like(alpha)
    m = np.abs(alpha) <= lam / 2 + 1e-15
    if theta == 0.0:
        intv = 1.0
        out[m] = 1.0 / lam
    else:
        intv = math.sin(theta) / theta  # int_{-1/2}^{1/2} cos(2 theta s) ds
        out[m] = np.cos(2 * theta * alpha[m] / lam) / (lam * intv)
    return out

# ---------------------------------------------------------------- V1: moments via Fourier quadrature
def moments_fourier(lam, theta, M=6001):
    """m2, m3 for the sine-process Gabor Gram at bandwidth lam, window cos(2 theta s).
    Grid quadrature on alpha in [-1.6, 1.6]."""
    A = 1.6
    al = np.linspace(-A, A, M)
    d = al[1] - al[0]
    u = u_hat(al, lam, theta)
    t = np.clip(1 - np.abs(al), 0, None)          # (S^2)^hat
    b = (np.abs(al) <= 0.5).astype(float)          # S^hat
    def conv(f, g):
        return np.convolve(f, g, mode="same") * d
    uu = conv(u, u)                                # (psi^2)^hat
    int_uu = np.sum(u * u) * d                     # int psi^2 dx = int u(a)^2 da (Parseval)
    int_t_uu = np.sum(t * uu) * d                  # int S^2 psi^2 dx = int t (u*u) da
    m2 = 1.0 + int_uu - int_t_uu
    # T3 pieces
    p1 = np.sum(u ** 3) * d
    tu = conv(t, u)
    p2 = np.sum(tu * u * u) * d
    bu = conv(b, u)
    p3 = np.sum(bu ** 3) * d
    T3 = p1 - 3 * p2 + 2 * p3
    m3 = 1.0 + 3 * (int_uu - int_t_uu) + T3
    return m2, m3

print("== V1/V2: sine-Gram moment budgets (Fourier quadrature) ==")
rows = []
for lam in (1.0, 0.65, 0.6, 0.55, 0.5):
    for theta in (0.0, 0.5, 1 / math.sqrt(2), 0.8, 1.1, 1.35):
        m2, m3 = moments_fourier(lam, theta)
        rows.append(dict(lam=lam, theta=theta, m2=m2, m3=m3,
                         margin_2m2_m3=2 * m2 - m3, excess_G=m3 - (3 * m2 - 2)))
closed = {}
for lam in (1.0, 0.65, 0.6, 0.55, 0.5):
    closed[lam] = dict(m2=1 / lam + lam / 3, m3=1 + 1 / lam ** 2)
for r in rows:
    tag = ""
    if r["theta"] == 0.0:
        c = closed[r["lam"]]
        tag = f"  | closed m2={c['m2']:.6f} m3={c['m3']:.6f} " \
              f"(err {abs(r['m2']-c['m2']):.1e},{abs(r['m3']-c['m3']):.1e})"
    print(f"lam={r['lam']:.2f} theta={r['theta']:.2f}: m2={r['m2']:.6f} m3={r['m3']:.6f} "
          f"2m2-m3={r['margin_2m2_m3']:+.6f} G=m3-(3m2-2)={r['excess_G']:+.6f}{tag}")
OUT["moments"] = rows
OUT["closed_forms_flat"] = closed
m2c, m3c = moments_fourier(1.0, 0.8)
OUT["v5_margin_check"] = dict(lam=1.0, theta=0.8, val=2 * m2c - m3c, recalled=0.68524)
print(f"v5 SS7.3 margin check: 2m2-m3 at lam=1, v=cos(1.6s): {2*m2c-m3c:.6f}  (recalled 0.68524)")

# ---------------------------------------------------------------- V3: pair-block law
print("\n== V3: isolated pair-block law (direct assembly) ==")
def pair_block_check(w, gamma_frac, theta=0.0, Lwin=40.0, nwin=1200):
    """Assemble M = x x^T + conj for one off-line pair at depth delta = w/L', position
    gamma = gamma_frac * window-spacing; compare eigenvalues with L^2 a (1 +/- A(w))."""
    L = Lwin
    # taper phi(s)^2 = v(s/L), flat: phi=1 on [-L/2,L/2]
    # phi-hat(tau) = int_{-L/2}^{L/2} sqrt(v(s/L)) e^{-i tau s} ds  (numeric)
    s = np.linspace(-L / 2, L / 2, 4001)
    ds = s[1] - s[0]
    if theta == 0.0:
        phi = np.ones_like(s)
    else:
        phi = np.sqrt(np.cos(2 * theta * s / L))
    delta = w / L
    spacing = 2 * math.pi / L
    ks = np.arange(-nwin, nwin + 1)
    taus = ks * spacing + gamma_frac * spacing
    z = 0.0 + 1j * delta  # zero at gamma=0 (windows shifted instead), depth delta
    # x_k = phi-hat(z - tau_k) = int phi(s) e^{-i (z-tau_k) s} ds
    E = np.exp(-1j * np.outer(z - taus, s))
    x = (E * phi).sum(axis=1) * ds
    Mmat = np.outer(x, x) + np.conj(np.outer(x, x))
    ev = np.linalg.eigvalsh(Mmat)
    a = (phi ** 2).sum() * ds / L
    if theta == 0.0:
        Aw = math.sinh(2 * w * 0.5) / (2 * w * 0.5) if w > 0 else 1.0  # int cosh(2 w sig) dsig, sig in [-1/2,1/2] = sinh(w)/w
    else:
        sig = np.linspace(-0.5, 0.5, 2001)
        v = np.cos(2 * theta * sig)
        Aw = np.trapz(v * np.cosh(2 * w * sig), sig) / np.trapz(v, sig)
    pred = np.array([L * L * a * (1 - Aw), L * L * a * (1 + Aw)])
    got = np.array([ev[0], ev[-1]])
    return got, pred, L * L * a

tab = []
for w in (0.0, 0.125, 0.25, 0.5, 0.75, 1.0, 2.0):
    got, pred, unit = pair_block_check(w, 0.0)
    got2, _, _ = pair_block_check(w, 0.37)  # generic offset: position-independence
    tab.append(dict(w=w, ev_norm=[got[0] / unit, got[1] / unit],
                    pred_norm=[pred[0] / unit, pred[1] / unit],
                    pos_indep_dev=float(np.max(np.abs(got - got2)) / unit)))
    print(f"w={w:4.2f}: eig/unit=({got[0]/unit:+.5f},{got[1]/unit:+.5f}) "
          f"pred 1+/-A=({pred[0]/unit:+.5f},{pred[1]/unit:+.5f}) "
          f"posdep={tab[-1]['pos_indep_dev']:.1e}  cubic={((got[0]/unit)**3+(got[1]/unit)**3):.4f} "
          f"3F-4={3*((got[0]/unit)**2+(got[1]/unit)**2)-4:.4f}")
OUT["pair_block"] = tab

# ---------------------------------------------------------------- V4: CUE Monte-Carlo
print("\n== V4: CUE MC cross-check (flat window) ==")
rng = np.random.default_rng(20260826)
def cue_angles(n):
    Z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / math.sqrt(2)
    Q, R = np.linalg.qr(Z)
    Q = Q * (np.diagonal(R) / np.abs(np.diagonal(R)))
    ang = np.angle(np.linalg.eigvals(Q))
    return np.sort(ang) * n / (2 * math.pi)  # unfolded to circumference n

def mc_moments(n, lam, R):
    """m2, m3 per zero via the DFT kernel route; flat window."""
    J = int(round(lam * n / 2))
    j = np.arange(-J, J + 1)
    u = np.full(j.shape, 1.0)
    u /= u.sum()                       # sum u_j = 1 -> tr = n exactly
    # precompute U3(k1,k2) = sum_j u_{j+k1} u_{j+k1+k2} u_j  -- flat: counts of overlap
    K = 2 * J
    m2s, m3s = [], []
    # build index helper for c_j
    for r in range(R):
        th = cue_angles(n)
        kk = np.arange(-2 * J, 2 * J + 1)
        c = np.exp(-2j * math.pi * np.outer(kk, th) / n).sum(axis=1)
        cidx = {int(k): c[i] for i, k in enumerate(kk)}
        # m2 = (1/n) sum_{j1,j2} u u |c_{j1+j2}|^2
        # convolution of u with itself: weights w_s = sum_{j1+j2=s} u_{j1} u_{j2}
        w2 = np.convolve(u, u)
        ss = np.arange(-2 * J, 2 * J + 1)
        m2s.append(float(np.sum(w2 * np.abs(c) ** 2)) / n)
        # m3 = (1/n) sum_{k1,k2} U3(k1,k2) c_{k1} c_{k2} c_{-k1-k2}
        # flat window: U3(k1,k2) = (#{j: j, j+k1, j+k1+k2 in [-J,J]}) * u0^3
        u0 = u[0]
        k1v = np.arange(-K, K + 1)
        acc = 0.0
        for k1 in k1v:
            lo = max(-J, -J - k1)
            hi = min(J, J - k1)
            if lo > hi:
                continue
            k2v = np.arange(max(-K, -J - k1 - hi), min(K, J - k1 - lo) + 1)
            # count j in [lo,hi] with j+k1+k2 in [-J,J]: j in [max(lo,-J-k1-k2), min(hi, J-k1-k2)]
            lo2 = np.maximum(lo, -J - k1 - k2v)
            hi2 = np.minimum(hi, J - k1 - k2v)
            cnt = np.clip(hi2 - lo2 + 1, 0, None).astype(float)
            vals = np.array([cidx[int(k1)] * cidx[int(k2)] * cidx[int(-k1 - k2)] for k2 in k2v])
            acc += float(np.real((cnt * vals).sum())) * u0 ** 3
        m3s.append(acc / n)
    return (np.mean(m2s), np.std(m2s) / math.sqrt(len(m2s)),
            np.mean(m3s), np.std(m3s) / math.sqrt(len(m3s)))

mc = {}
t0 = time.time()
for (n, R) in ((256, 120), (512, 60)):
    for lam in (1.0, 0.5):
        m2m, m2e, m3m, m3e = mc_moments(n, lam, R)
        key = f"n{n}_lam{lam}"
        mc[key] = dict(m2=m2m, m2_se=m2e, m3=m3m, m3_se=m3e, R=R)
        cf = closed[lam]
        print(f"n={n} lam={lam}: m2={m2m:.4f}+-{m2e:.4f} (closed {cf['m2']:.4f})   "
              f"m3={m3m:.4f}+-{m3e:.4f} (closed {cf['m3']:.4f})   [{time.time()-t0:.0f}s]")
OUT["cue_mc"] = mc

# ---------------------------------------------------------------- V5: fuzz-row constant
print("\n== V5: garnish-capacity fuzz constant ==")
from scipy.optimize import linprog
def fuzz_lp(h):
    """Scale-free instance C_led = eps = 1 (value scales as sqrt(C_led*eps); h* = sqrt(3)).
    Variables mu_i = n_i h_i^2 (Frobenius mass).  max sum mu_i h_i
    s.t. sum_{h_j >= h_i} mu_j h_j^-2 <= h_i^-4 (ladder), sum mu_i <= 1 (Frobenius)."""
    npts = len(h)
    c = -h
    A, bb = [], []
    for i in range(npts):
        row = np.zeros(npts)
        row[i:] = 1.0 / h[i:] ** 2
        A.append(row); bb.append(h[i] ** -4.0)
    A.append(np.ones(npts)); bb.append(1.0)
    res = linprog(c, A_ub=np.array(A), b_ub=np.array(bb), bounds=[(0, None)] * npts,
                  method="highs")
    assert res.status == 0, res.message
    return -res.fun, res.x

hc = np.geomspace(1.0, 60.0, 3000)
val_c, xc = fuzz_lp(hc)
hd = 2.0 ** np.arange(0, 7)          # dyadic-only heights
val_d, _ = fuzz_lp(hd)
pred = 5 / math.sqrt(3)
print(f"continuum LP (C=eps=1): {val_c:.6f}   predicted 5/sqrt(3) = {pred:.6f}  ratio {val_c/pred:.5f}")
print(f"dyadic-heights LP     : {val_d:.6f}   (adjudicator's two-term value 2.0)")
supp = hc[xc > 1e-9]
print(f"support of optimum: h in [{supp.min():.3f}, {supp.max():.3f}]  (predicted tail start s* = sqrt(3) = {math.sqrt(3):.3f})")
OUT["fuzz"] = dict(continuum=val_c, prediction=pred, dyadic=val_d,
                   support=[float(supp.min()), float(supp.max())])

# ---------------------------------------------------------------- V6: per-zero identity
print("\n== V6: per-zero identity c = 3F - 2 + (m-1)(m-2) ==")
ident = []
for m in (1, 2, 3, 4, 6, 8):
    F = m; C = m * m          # per zero: atom of mult m -> eigenvalue m, per-zero F=m, c=m^2
    ident.append(dict(kind=f"atom m={m}", F=F, c=C, resid=C - (3 * F - 2) - (m - 1) * (m - 2)))
for w in (0.0, 0.25, 0.5, 1.0, 2.0):
    A = math.sinh(w) / w if w > 0 else 1.0
    F = 1 + A * A             # per zero (pair of two mult-1 zeros: block/2)
    C = 1 + 3 * A * A
    ident.append(dict(kind=f"pair w={w}", F=F, c=C, resid=C - (3 * F - 2)))
for r in ident:
    print(f"{r['kind']:12s}: F={r['F']:.4f} c={r['c']:.4f} residual={r['resid']:.2e}")
OUT["per_zero_identity"] = ident

# ---------------------------------------------------------------- V7: ppp constant
print("\n== V7: ppp diagonal constant ==")
Nsieve = 3_000_000
sieve = np.ones(Nsieve + 1, dtype=bool); sieve[:2] = False
for p in range(2, int(Nsieve ** 0.5) + 1):
    if sieve[p]:
        sieve[p * p::p] = False
ps = np.nonzero(sieve)[0].astype(float)
cval = float(np.sum(np.log(ps) ** 3 / (ps - 1) ** 2))
print(f"sum_p (log p)^3/(p-1)^2 (p<=3e6) = {cval:.6f}   (adjudication: 2.315762)")
OUT["ppp_constant"] = cval

with open(__file__.replace("verify_constants.py", "verify_out.json"), "w") as f:
    json.dump(OUT, f, indent=1, default=float)
print("\nwritten verify_out.json")
