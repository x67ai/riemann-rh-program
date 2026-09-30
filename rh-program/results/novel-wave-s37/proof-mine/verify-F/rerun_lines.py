#!/usr/bin/env python3
"""read-F re-run (orchestrator, Fable 5.1, Session 38): the M2 NOTE's four lines on V=(5,5) and E0=(5,4), V2's data, and
Lemma Z4's constants — by an independent route (sympy exact arithmetic; numpy eigenvalues for the signature)."""
import sympy as sp, numpy as np, math
q = 5
def data(L, n_max=12):
    u = sp.symbols('u'); Lp = sp.Poly(L, u)
    roots = [complex(r) for r in sp.Poly(sp.expand(u**Lp.degree()*L.subs(u, 1/u)), u).nroots(n=30)]  # reciprocal roots
    N = [None]+[int(round((q**n + 1 - sum(r**n for r in roots)).real)) for n in range(1, n_max+1)]
    b = [None]*(n_max+1)
    for d in range(1, n_max+1):
        b[d] = (N[d] - sum(e*b[e] for e in range(1, d) if d % e == 0)) // d
    return roots, N, b
u = sp.symbols('u')
for name, L in (("V", 1-5*u+5*u**2), ("E0", 1-4*u+5*u**2)):
    roots, N, b = data(L)
    print(f"{name}: L(1)={L.subs(u,1)}  N_1..8={N[1:9]}  b_1..8={b[1:9]}  |roots|={[round(abs(r),4) for r in roots]}  Re s={[round(math.log(abs(r))/math.log(q),5) for r in roots]}")
    t = [5,4][name=="E0"]
    # (D) deg(pi-2) = norm of (alpha-2): (alpha-2)(beta-2) = 4 - 2t + q ; Rosati trace = 2 deg for g=1
    deg = 4 - 2*t + q; print(f"  deg(pi-2) = {deg}; Tr((pi-2)(pi-2)^dagger) = {2*deg}")
    # (A) Gram on <C1,C2,Delta,Gamma>: C1^2=C2^2=0, C1.C2=1, C1.Delta=C2.Delta=1, Delta^2=0, C1.Gamma=1, C2.Gamma=q, Gamma^2=0, Delta.Gamma=N_1
    G = np.array([[0,1,1,1],[1,0,1,q],[1,1,0,N[1]],[1,q,N[1],0]], dtype=float)
    ev = np.linalg.eigvalsh(G); print(f"  Gram eigenvalues {np.round(ev,4)} -> index (+,-) = ({(ev>0).sum()},{(ev<0).sum()})")
    D2 = 0 - 4*N[1] + 0; d1, d2 = 1-2, q-2; print(f"  def(Gamma-2Delta) = 2*{d1}*{d2} - ({D2}) = {2*d1*d2 - D2}")
    # (B) Weil I (7.1) at C x C: q^{1/2} <= |alpha_i alpha_j| <= q^{3/2}
    a = max(abs(r) for r in roots); print(f"  alpha^2 = {a*a:.3f}  vs [q^0.5, q^1.5] = [{q**0.5:.3f}, {q**1.5:.3f}]")
    # (C) twist over F_25: nu_1(twist) = 2(Q+1) - N_2 ; Bombieri (5): < Q + 3 Q^{1/2} + 1 ; (7) with mu=1,m=7,l=4: <= l + m Q/p + 1
    Q = 25; tw = 2*(Q+1) - N[2]; print(f"  twist over F_25: {tw}  vs (5) < {Q+3*int(Q**0.5)+1}  and (7) <= {4 + 7*Q//5 + 1}")
print("== V2: L = 1 - u + 11u^2 - 5u^3 + 25u^4 ==")
L2 = 1 - u + 11*u**2 - 5*u**3 + 25*u**4
roots, N, b = data(L2, 40)
print(f"  FE check L(u) - 25u^4 L(1/(5u)) = {sp.simplify(L2 - 25*u**4*L2.subs(u, 1/(5*u)))}; h = L(1) = {L2.subs(u,1)}")
print(f"  |roots| = {[round(abs(r),4) for r in roots]}  Re s = {sorted(set(round(math.log(abs(r))/math.log(q),4) for r in roots))}")
print(f"  N_1..6 = {N[1:7]}; b_1..6 = {b[1:7]}; min N = {min(N[1:])}, min b = {min(b[1:])} (n,d <= 40)")
Q = 5**6; print(f"  Bombieri Thm 1 at Q=5^6: N_6 - Q - 1 = {N[6]-Q-1}  vs (2g+1) Q^{{1/2}} = {5*125}  -> violated: {N[6]-Q-1 > 625}")
print("== Lemma Z4: kappa = A T/(T-1), A = -sum c_k log k / k ==")
def kappa(c, T):
    A = -sum(ck*math.log(k)/k for k, ck in c.items()); return A*T/(T-1)
print(f"  Chebyshev c=(1@1,-1@2,-1@3,-1@5,+1@30), T=6: kappa = {kappa({1:1,2:-1,3:-1,5:-1,30:1}, 6):.6f} (NOTE 1.105550)")
print(f"  binomial C(2n,n) c=(1@1,-2@2), T=2: kappa = {kappa({1:1,2:-2}, 2):.6f} (NOTE 1.386294 = 2 log 2)")
# g(t) for Chebyshev: verify g >= 0 and g = 1 on [1,6)
g = lambda t: math.floor(t) - math.floor(t/2) - math.floor(t/3) - math.floor(t/5) + math.floor(t/30)
vals = [g(t/10) for t in range(0, 600)]; print(f"  Chebyshev g: min={min(vals)}, max={max(vals)}, g==1 on [1,6): {all(g(t/100)==1 for t in range(100,600))}")
