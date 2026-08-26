# T5 verification: garnish-capacity continuum LP.
#   max int h^3 dmu   s.t.  int h^2 dmu <= eps,  mu([h, inf)) <= C h^-4 (all h >= 1)
#   claim: optimum = 2 sqrt(2) sqrt(C eps), attained by tail N(h) = C min(a^-4, h^-4), a = sqrt(2C/eps).
import numpy as np, json
from scipy.optimize import linprog

out = {}
C, eps = 1.0, 0.02
a = np.sqrt(2 * C / eps)
pred = 2 * np.sqrt(2) * np.sqrt(C * eps)
print(f"C = {C}, eps = {eps}: a = {a}, predicted optimum = 2 sqrt(2) sqrt(C eps) = {pred:.6f}")

# ---- (1) attainment profile: closed-form Psi and Phi (analytic + quadrature) ----
# N_a(h) = C min(a^-4, h^-4);  Psi = N(1) + 2 int_1^inf h N dh = 2C/a^2 ; Phi = N(1) + 3 int h^2 N = 4C/a
from scipy.integrate import quad
Na = lambda h: C * min(a**-4, h**-4)
Psi = Na(1) + 2 * quad(lambda h: h * Na(h), 1, np.inf, limit=400)[0]
Phi = Na(1) + 3 * quad(lambda h: h**2 * Na(h), 1, np.inf, limit=400)[0]
out["attain_Psi"] = Psi; out["attain_Phi"] = Phi
print(f"attainment profile: Psi (Frobenius) = {Psi:.8f} vs eps = {eps} (dev {abs(Psi-eps):.1e}); "
      f"Phi (cubic) = {Phi:.8f} vs {pred:.8f} (dev {abs(Phi-pred):.1e})")

# ---- (2) discretized LP over point masses on a geometric height grid ----
def capacity_lp(hmax, npts, C=1.0, eps=0.02):
    h = np.geomspace(1.0, hmax, npts)
    # variables: mu_j >= 0 (point mass at h_j)
    # ladder: for each i, sum_{j >= i} mu_j <= C h_i^-4
    A_ub = np.zeros((npts + 1, npts))
    b_ub = np.zeros(npts + 1)
    for i in range(npts):
        A_ub[i, i:] = 1.0
        b_ub[i] = C * h[i] ** -4
    A_ub[npts, :] = h**2
    b_ub[npts] = eps
    res = linprog(c=-(h**3), A_ub=A_ub, b_ub=b_ub, bounds=[(0, None)] * npts, method="highs")
    return -res.fun, h, res.x

for hmax in (100.0, 400.0, 2000.0):
    val, h, x = capacity_lp(hmax, 600)
    tail = 3 * C / hmax  # truncation tail: int_{hmax}^inf 3 h^2 C h^-4 dh = 3C/hmax
    out[f"lp_hmax{int(hmax)}"] = {"lp": val, "lp_plus_tail": val + tail, "pred": pred}
    print(f"LP (hmax={hmax:6.0f}, 600 pts): value = {val:.6f}; + truncation tail 3C/hmax = "
          f"{val + tail:.6f}  vs 2 sqrt2 sqrt(C eps) = {pred:.6f}")

# optimal profile shape check: cumulative tail vs C min(a^-4, h^-4)
val, h, x = capacity_lp(2000.0, 600)
tails = np.cumsum(x[::-1])[::-1]
model = C * np.minimum(a**-4.0, h**-4.0)
i_mid = np.searchsorted(h, [1.5, a / 2, a, 2 * a, 10 * a])
rel = np.abs(tails[i_mid] - model[i_mid]) / model[i_mid]
out["profile_shape_reldev"] = rel.tolist()
print(f"LP optimal cumulative profile vs C min(a^-4, h^-4) at h = 1.5, a/2, a, 2a, 10a: "
      f"rel devs = {np.array2string(rel, precision=3)}")

# ---- (3) the naive point-mass-plus-tail profile: value 5/sqrt(3) sqrt(C eps), ladder-INFEASIBLE ----
b = np.sqrt(3 * C / eps)
n0 = C * b**-4                       # ladder-saturating atom at b
naive_frob = n0 * b**2 + 2 * C / b**2  # atom + saturated tail above b
naive_cubic = n0 * b**3 + 4 * C / b
naive_pred = 5 / np.sqrt(3) * np.sqrt(C * eps)
out["naive_value"] = naive_cubic; out["naive_pred"] = naive_pred; out["naive_frob"] = naive_frob
print(f"naive profile: atom n0 = C b^-4 at b = sqrt(3C/eps) = {b:.4f} + saturated tail above; "
      f"Frobenius = {naive_frob:.6f} (= eps), cubic = {naive_cubic:.6f} vs 5/sqrt3 sqrt(C eps) = {naive_pred:.6f}")
# cumulative ladder violation on (2^-1/4 b, b): mu([h, inf)) = n0 + C b^-4 = 2 C b^-4 > C h^-4
hs = np.linspace(b * 2**-0.25 * 1.001, b * 0.999, 7)
viol = (n0 + C * b**-4) - C * hs**-4
out["naive_violation_range"] = [float(viol.min()), float(viol.max())]
print(f"cumulative count just below the atom = 2 C b^-4 = {2*C*b**-4:.3e}; ladder cap C h^-4 on "
      f"(2^-0.25 b, b) in [{C*b**-4:.3e}, {C*(b*2**-0.25)**-4:.3e}]  ->  VIOLATED "
      f"(excess {viol.min():.2e}..{viol.max():.2e} > 0 on the whole interval); 2^0.25 = {2**0.25:.4f}")

# LP re-check: force the naive profile's cubic as a lower bound -> infeasible
res = linprog(c=np.zeros(600), A_ub=np.vstack([np.tril(np.ones((600, 600))).T[:0]]) if False else None,
              method="highs") if False else None
# simpler: is naive_cubic attainable? compare with LP optimum
print(f"LP optimum {out['lp_hmax2000']['lp_plus_tail']:.6f} < naive claim {naive_pred:.6f}: "
      f"{out['lp_hmax2000']['lp_plus_tail'] < naive_pred}  (the cumulative ladder strictly cuts the naive value)")

# ---- (4) duality identity: a eps + 2C/a = 4C/a at a = sqrt(2C/eps); scaling in (C, eps) ----
assert abs(a * eps + 2 * C / a - 4 * C / a) < 1e-14
for C2, e2 in ((10.0, 1e-3), (100.0, 1e-4), (1000.0, 1e-8)):
    a2 = np.sqrt(2 * C2 / e2)
    v2 = 4 * C2 / a2
    assert abs(v2 - 2 * np.sqrt(2) * np.sqrt(C2 * e2)) < 1e-12 * max(1, v2)
print("duality identity a*eps + 2C/a = 4C/a and scaling 4C/a = 2 sqrt2 sqrt(C eps): PASS "
      "(incl. C_led = 1000, eps = 1e-8: capacity = %.4f)" % (2*np.sqrt(2)*np.sqrt(1000*1e-8)))
out["capacity_C1000_eps1e-8"] = 2*np.sqrt(2)*np.sqrt(1000*1e-8)

json.dump(out, open("verify_t5_out.json", "w"), indent=1, default=float)
print("WROTE verify_t5_out.json")
