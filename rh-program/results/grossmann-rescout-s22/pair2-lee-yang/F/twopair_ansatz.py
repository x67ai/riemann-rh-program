# Scout F: the "explicit in (N1, N2)" point at m = 0.  Two-pair ansatz on 4 sites: J_12 = J_34 = J_in, all four cross bonds
# J_out; u = e^{-2 J_in}, v = e^{-4 J_out}.  r_1 = 4 u v, r_2 = 2 (v^2 + 2 u^2 v)  [subsets {1,2},{3,4}: cut = 4 cross bonds -> v^2;
# {1,3},{1,4},{2,3},{2,4}: cut = both inner bonds + 2 cross bonds -> u^2 v].  Target (b1, b2) = (a1/sqrt q, a2/q).
import sympy as sp, math, json
u, v, b1, b2 = sp.symbols('u v b1 b2', positive=True)
eqs = [sp.Eq(4 * u * v, b1), sp.Eq(2 * (v ** 2 + 2 * u ** 2 * v), b2)]
usol = sp.solve(eqs[0], u)[0]
cubic = sp.simplify((2 * (v ** 2 + 2 * usol ** 2 * v) - b2) * 4 * v)
print("u = b1/(4v);  v satisfies", sp.expand(cubic), "= 0   (a cubic in v with coefficients in Q(b1, b2) = Q(sqrt q)(N1, N2))")
cl = json.load(open("g2_classes.json"))
shown = 0
for c in cl:
    p, a1, a2 = c['p'], c['a1'], c['a2']
    if a1 <= 0 or a2 <= 0: continue
    B1 = a1 / math.sqrt(p); B2 = a2 / p
    roots = [r for r in sp.Poly(cubic.subs({b1: B1, b2: B2}), v).nroots() if abs(sp.im(r)) < 1e-12 and 0 < sp.re(r) <= 1]
    ok = [(float(r), B1 / (4 * float(r))) for r in roots if 0 < B1 / (4 * float(r)) <= 1]
    if ok:
        vv, uu = ok[0]
        Jin = -0.5 * math.log(uu); Jout = -0.25 * math.log(vv)
        r1 = 4 * uu * vv; r2 = 2 * (vv ** 2 + 2 * uu ** 2 * vv)
        print(f"class (p,a1,a2)=({p},{a1},{a2}), N1={c['N1']}, N2={c['N2']}: b=({B1:.6f},{B2:.6f}); v={vv:.6f}, u={uu:.6f} -> J_in={Jin:.6f}, J_out={Jout:.6f}; check r=({r1:.6f},{r2:.6f}); admissible real roots of the cubic in (0,1]: {len(ok)}")
        shown += 1
    if shown >= 4: break
# Non-uniqueness: at m = 0 the map J in R^6 -> (r_1, r_2) has generic rank 2, so a realized interior class has a 4-dimensional
# family of realizations; the two-pair ansatz picks one, the uniform-J family another (t_2 = 6 (t_1/4)^{4/3}) — a design choice.
print("generic Jacobian rank of J -> (r_1, r_2) at N = 4 (random J):", end=" ")
import numpy as np, itertools
from ferro_core import structure, make_funcs
fun, jac, K, E, edges = make_funcs(4, np.zeros(2))
rng = np.random.default_rng(1)
print(sorted(set(np.linalg.matrix_rank(jac(rng.uniform(0.05, 1.0, 6))) for _ in range(20))), "=> solution families of dimension 6 - 2 = 4 at interior points")
