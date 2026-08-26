# T4 verification: sine-process moment closed forms (flat window)
#   m2(lam) = 1/lam + lam/3,  m3(lam) = 1 + 1/lam^2   (lam <= 1)
# via (i) Fourier-side quadrature of the SPEC 9.1 integrals, (ii) real-space quadrature
# of the determinantal correlation integrals, (iii) corollary values and the margin root.
import numpy as np, json
from scipy.optimize import brentq

out = {}

# ---------- (i) Fourier-side quadrature ----------
def fourier_moments(lam, dal=2e-4):
    # u = (1/lam) 1_[-lam/2, lam/2]; t = (1-|a|)_+; b = 1_[-1/2,1/2]
    al = np.arange(-2.2, 2.2, dal)
    u = np.where(np.abs(al) <= lam / 2, 1 / lam, 0.0)
    t = np.maximum(1 - np.abs(al), 0.0)
    b = np.where(np.abs(al) <= 0.5, 1.0, 0.0)
    conv = lambda f, g: np.convolve(f, g, mode="same") * dal
    uu = conv(u, u)
    int_u2 = np.sum(u**2) * dal
    int_t_uu = np.sum(t * uu) * dal
    m2 = 1 + int_u2 - int_t_uu
    int_u3 = np.sum(u**3) * dal
    tu = conv(t, u)
    int_tu_u2 = np.sum(tu * u**2) * dal
    bu = conv(b, u)
    int_bu3 = np.sum(bu**3) * dal
    T3 = int_u3 - 3 * int_tu_u2 + 2 * int_bu3
    m3 = 1 + 3 * (int_u2 - int_t_uu) + T3
    return m2, m3

print("Fourier-side quadrature vs closed forms:")
worst2 = worst3 = 0.0
for lam in (0.40, 0.50, 0.55, 0.61, 2/3, 0.75, 1.00):
    m2q, m3q = fourier_moments(lam)
    m2c, m3c = 1/lam + lam/3, 1 + 1/lam**2
    worst2 = max(worst2, abs(m2q - m2c)); worst3 = max(worst3, abs(m3q - m3c))
    print(f"  lam={lam:.4f}: m2 quad {m2q:.6f} vs {m2c:.6f} (dev {abs(m2q-m2c):.1e}); "
          f"m3 quad {m3q:.6f} vs {m3c:.6f} (dev {abs(m3q-m3c):.1e})")
out["fourier_quad_maxdev_m2"] = worst2
out["fourier_quad_maxdev_m3"] = worst3

# ---------- (ii) real-space quadrature ----------
S = lambda x: np.sinc(x)                    # sin(pi x)/(pi x)
psi = lambda x, lam: np.sinc(lam * x)       # flat-window kernel at bandwidth lam

# m2 real-space: 1 + int (1 - S^2) psi^2  (1D, cheap, X large)
def m2_real(lam, X=4000.0, dx=0.01):
    x = np.arange(dx / 2, X, dx)
    integ = (1 - S(x) ** 2) * psi(x, lam) ** 2
    return 1 + 2 * np.sum(integ) * dx

for lam in (0.5, 1.0):
    v = m2_real(lam)
    c = 1/lam + lam/3
    out[f"m2_real_lam{lam}"] = {"quad": v, "closed": c, "dev": abs(v - c)}
    print(f"real-space m2({lam}) = {v:.6f} vs {c:.6f} (dev {abs(v-c):.1e})")

# m3 real-space: 1 + 3 int (1-S^2) psi^2 + iint rho3 * psi(x)psi(y)psi(x+y)
# rho3 factor (points 0, x, x+y): 1 - S(x)^2 - S(y)^2 - S(x+y)^2 + 2 S(x)S(y)S(x+y)
def m3_real(lam, X=40.0, dx=0.05):
    x = np.arange(-X + dx/2, X, dx)
    XX, YY = np.meshgrid(x, x, indexing="ij")
    Sx, Sy, Sxy = S(XX), S(YY), S(XX + YY)
    rho3 = 1 - Sx**2 - Sy**2 - Sxy**2 + 2 * Sx * Sy * Sxy
    P = psi(XX, lam) * psi(YY, lam) * psi(XX + YY, lam)
    T3 = np.sum(rho3 * P) * dx * dx
    two_pt = m2_real(lam) - 1
    return 1 + 3 * two_pt + T3

for lam, X in ((0.5, 40.0), (0.5, 80.0), (1.0, 40.0)):
    v = m3_real(lam, X=X)
    c = 1 + 1/lam**2
    out[f"m3_real_lam{lam}_X{int(X)}"] = {"quad": v, "closed": c, "dev": abs(v - c)}
    print(f"real-space m3({lam}) at truncation X={X}: {v:.4f} vs {c} (dev {abs(v-c):.1e})")

# ---------- (iii) corollaries ----------
m2 = lambda lam: 1/lam + lam/3
m3 = lambda lam: 1 + 1/lam**2
G  = lambda lam: m3(lam) - (3*m2(lam) - 2)          # = 3 + 1/lam^2 - 3/lam - lam
Mg = lambda lam: 2*m2(lam) - m3(lam)                # = 2/lam + 2 lam/3 - 1 - 1/lam^2
checks = {
    "m2(1)": (m2(1), 4/3), "m3(1)": (m3(1), 2.0),
    "m2(1/2)": (m2(0.5), 13/6), "m3(1/2)": (m3(0.5), 5.0),
    "G(1)": (G(1), 0.0), "G(1/2)": (G(0.5), 0.5),
    "margin(1)": (Mg(1), 2/3), "margin(1/2)": (Mg(0.5), -2/3),
}
for k, (v, ref) in checks.items():
    assert abs(v - ref) < 1e-14, (k, v, ref)
    print(f"{k} = {v:.12f} (= {ref})")
out["corollary_checks"] = "all exact"

# G(lam) formula identity check: m3 - (3 m2 - 2) == 3 + 1/lam^2 - 3/lam - lam
lams = np.linspace(0.2, 1.0, 81)
dev = np.max(np.abs((m3(lams) - (3*m2(lams) - 2)) - (3 + 1/lams**2 - 3/lams - lams)))
out["G_formula_identity_dev"] = float(dev)
# margin formula identity
dev2 = np.max(np.abs(Mg(lams) - (2/lams + 2*lams/3 - 1 - 1/lams**2)))
out["margin_formula_identity_dev"] = float(dev2)
print(f"G and margin formula identities on lam-grid: max dev = {dev:.1e}, {dev2:.1e}")

# margin sign change
root = brentq(Mg, 0.55, 0.66, xtol=1e-12)
out["margin_root"] = root
print(f"margin 2 m2 - m3 = 0 at lam = {root:.6f} (sign change near 0.61)")

# kappa identity: (1/lam^2) * int_{-lam}^{lam} (lam - |a|) F(a) da with F = delta_0 + |a|
# = (lam + lam^3/3)/lam^2 = 1/lam + lam/3  (arithmetic identity, checked numerically)
for lam in (0.3, 0.5, 1.0):
    da = 1e-6
    a = np.arange(da/2, lam, da)
    val = (lam + 2*np.sum((lam - a) * a) * da) / lam**2
    assert abs(val - m2(lam)) < 1e-5
print("kappa identity: (lam + lam^3/3)/lam^2 = m2(lam) checked at lam = 0.3, 0.5, 1.0")
out["kappa_identity"] = "pass"

json.dump(out, open("verify_t4_out.json", "w"), indent=1, default=float)
print("WROTE verify_t4_out.json")
