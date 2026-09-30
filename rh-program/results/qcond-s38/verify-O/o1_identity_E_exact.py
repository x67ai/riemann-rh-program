"""o1 (read-O, qcond-s38): the measure identity (E) of NOTE §2.1, checked EXACTLY (symbolic, no floating point),
by a route independent of verify/v2.

(E): for sigma = nu + nu^v (nu = dN scaled by q^{-1/2}), mu_q = rho delta_0 + sigma self-dual, and ANY finite measure
w = sum_m w_m delta_m on [1, oo) (positivity NOT needed for the identity), sigma_2 := int D_u sigma dw(u) has
    FT(sigma_2) = int u^{-1} D_{1/u} sigma dw(u) + rho m1 delta_0 - rho m0 lambda.
Pair both sides with the triangle phi_L(x) = (1 - |x|/L)_+ of ARBITRARY width L = ell/sqrt(q) (NOTE's Prop. E is ell = 1 only):
  LHS = <sigma_2, FT phi_L> = 2 L sum_m w_m sum_j a_j T(ell m b_j / q),   T(e) := sum_{n>=1} S(n e),
  RHS = <FT sigma_2, phi_L> = sum_m (w_m/m) 2 sum_{x atom of dN} c(x) (1 - x/(m ell))_+  + rho m1 - rho m0 L.
Route for T (NOT Poisson, which v2 used): the Fourier series sum_{n>=1} cos(2 pi n th)/n^2 = pi^2 (th^2 - th + 1/6), 0<=th<=1,
gives sum_{n>=1} sin^2(pi n e)/n^2 = (pi^2/2) f (1 - f), f = frac(e); hence T(e) = f(1 - f)/(2 e^2)  (exact for algebraic e).
Examples: dN = sum_j a_j sum_{n>=1} delta_{b_j n} with Riemann's FE at conductor q (Poisson combs; none is Beurling).
"""
import sympy as sp

R = sp.Rational
s2, s3, s6 = sp.sqrt(2), sp.sqrt(3), sp.sqrt(6)

def T(e):
    e = sp.nsimplify(e)
    f = e - sp.floor(e)
    return sp.simplify(f*(1 - f)/(2*e**2))

EXAMPLES = {   # name: (q, [(b_j, a_j)])  -- F(s) = sum_j a_j b_j^{-s} zeta(s)
    "zeta (q=1)": (1, [(1, 1)]),
    "zeta(1+3^{1/2-s}) (q=3) [new]": (3, [(1, 1), (3, s3)]),
    "zeta(1+2^{1/2-s}) (q=2)": (2, [(1, 1), (2, s2)]),
    "zeta(1+2^{1-2s}) (q=4)": (4, [(1, 1), (4, 2)]),
    "zeta(1+9^{1/2-s}) (q=9)": (9, [(1, 1), (9, 3)]),
    "F55 (q=25)": (25, [(1, 1), (5, 5), (25, 5)]),
    "zeta(1+2^-s+(sqrt6/2)3^-s+sqrt6 6^-s) (q=6) [new]": (6, [(1, 1), (2, 1), (3, s6/2), (6, s6)]),
    "zeta(1+2^{-s/2}+sqrt2 2^-s) (q=2, radical) [new]": (2, [(1, 1), (s2, 1), (2, s2)]),
}
SIEVES = {
    "d1": {1: 1},
    "d1-d2": {1: 1, 2: -1},
    "d1-d3": {1: 1, 3: -1},
    "(d1-d2)(d1-d3)(d1-d5)": {1: 1, 2: -1, 3: -1, 5: -1, 6: 1, 10: 1, 15: 1, 30: -1},
    "signed d1-2d3+d7/2+3d(5/2) [not admissible; (E) needs none]": {1: 1, 3: -2, 7: R(1, 2), R(5, 2): 3},
}
ELLS = [R(1), R(1, 2), R(2), R(3, 2), R(3), R(7, 3)]

def fe_check(q, combs):
    """Riemann's FE at conductor q for F = zeta*D, D = sum a_j b_j^{-s}: D(1-s) = q^{s-1/2} D(s) as exponential sums."""
    s = sp.Symbol('s')
    D = sum(a*b**(-s) for b, a in combs)
    lhs = sp.expand(D.subs(s, 1 - s)); rhs = sp.expand(q**(s - R(1, 2))*D)
    pts = [R(3, 10) + 2*sp.I, R(-7, 5) + sp.I/3]
    return max(abs(sp.N((lhs - rhs).subs(s, p), 60)) for p in pts)

def atoms(combs, X):
    """atoms x < X of dN = sum_j a_j sum_n delta_{b_j n}, merged: dict x -> c(x)."""
    out = {}
    for b, a in combs:
        n = 1
        while sp.N(b*n, 50) < sp.N(X, 50):
            x = sp.nsimplify(b*n); out[x] = out.get(x, 0) + a; n += 1
    return out

def check(q, combs, w, ell):
    sq = sp.sqrt(q); L = ell/sq
    rho = sq*sum(sp.S(a)/sp.S(b) for b, a in combs)
    m1 = sum(wm/sp.nsimplify(m) for m, wm in w.items()); m0 = sum(w.values())
    lhs = 2*L*sum(wm*a*T(ell*sp.nsimplify(m)*b/q) for m, wm in w.items() for b, a in combs)
    rhs = rho*m1 - rho*m0*L
    for m, wm in w.items():
        m = sp.nsimplify(m)
        for x, cx in atoms(combs, m*ell).items():
            rhs += (wm/m)*2*cx*(1 - x/(m*ell))
    return sp.simplify(sp.radsimp(lhs - rhs)), sp.nsimplify(sp.simplify(lhs))

if __name__ == "__main__":
    print(__doc__.strip().splitlines()[0])
    print("sanity: T(3/2) =", T(R(3, 2)), "(Poisson closed form of v2 gives 1/18);  T(1) =", T(1), "; T(1/2) =", T(R(1, 2)))
    total = bad = 0
    for name, (q, combs) in EXAMPLES.items():
        print(f"== {name}: FE residual (60 digits, 2 points) = {sp.N(fe_check(q, combs), 3)}; rho_q = {sp.nsimplify(sp.sqrt(q)*sum(sp.S(a)/sp.S(b) for b, a in combs))}")
        for sname, w in SIEVES.items():
            diffs, vals = [], []
            for ell in ELLS:
                d, v = check(q, combs, w, ell); total += 1
                if d != 0: bad += 1
                diffs.append(d); vals.append(v)
            print(f"   w={sname:48s} LHS-RHS over ell={[str(e) for e in ELLS]}: {['0' if d == 0 else str(d) for d in diffs]}")
            print(f"      LHS at ell=1 (Prop. E left side): {vals[0]}")
    print(f"TOTAL exact checks: {total}; nonzero differences: {bad}")
