"""v3d (qtwin-s39): route (ii), Part D -- Beurling probe on the Gaussian Pisot family (NOT admissible: it violates the gap,
v3 Part B); it shows what the multiplicative condition Pi = log*(c) >= 0 looks like on the monoid O_K ∩ [1, X].
c(n) = K_j(n^sigma)/K_j(1), K_j(t) = exp(-pi (t phi^j / c)^2)  (q = sqrt5 phi^{2j}; generalized integers n in O_K, n >= 1).
Pi from c(n) log n = sum_{n1 n2 = n} c(n1) Pi(n2) log n2 (all factorizations inside O_K ∩ [1, X], |n_i^sigma| <= T).
"""
import math
PHI = (1 + 5**0.5)/2; C = 5**0.25

def elems(X, T):
    out = []
    s5 = 5**0.5
    for b in range(int(math.floor((1 - T)/s5)) - 1, int(math.ceil((X + T)/s5)) + 2):
        for a in range(int(math.floor(1 - b*PHI)) - 1, int(math.ceil(X - b*PHI)) + 2):
            x, xs = a + b*PHI, a + b*(1 - PHI)
            if 1 - 1e-12 <= x <= X and abs(xs) <= T:
                out.append((a, b))
    return out

def mul(p, q):
    a, b = p; c, d = q
    return (a*c + b*d, a*d + b*c + b*d)

def probe(j, X=60.0, T=None):
    lam = PHI**j/C
    if T is None:
        T = math.sqrt(75/math.pi)/lam      # weights below e^-75 dropped
    E = elems(X, T)
    idx = {e: i for i, e in enumerate(E)}
    x = {e: e[0] + e[1]*PHI for e in E}
    xs = {e: e[0] + e[1]*(1 - PHI) for e in E}
    w = {e: math.exp(-math.pi*((xs[e]*lam)**2 - lam**2)) for e in E}   # c(1) = 1
    order = sorted(E, key=lambda e: x[e])
    fac = {e: [] for e in E}
    for i, e1 in enumerate(order):
        if x[e1] <= 1 + 1e-12:
            continue
        for e2 in order:
            if x[e1]*x[e2] > X + 1e-9:
                break
            p = mul(e1, e2)
            if p in fac:
                fac[p].append((e1, e2))     # ordered: n1 = e1 > 1, n2 = e2 (any)
    Pi = {}
    for e in order:
        if x[e] <= 1 + 1e-12:
            Pi[e] = 0.0
            continue
        L = math.log(x[e])
        s = w[e]*L - sum(w[n1]*Pi[n2]*math.log(x[n2]) for n1, n2 in fac[e] if x[n2] > 1 + 1e-12)
        Pi[e] = s/L
    neg = sorted(((Pi[e], e) for e in order if Pi[e] < -1e-12), key=lambda t: t[0])
    rho = math.exp(math.pi*lam**2)
    print(f"j={j}: q = {5**0.5*PHI**(2*j):.6f}, rho = c at n^sigma = 0: {rho:.6g}; #elements in [1,{X:g}] with |n^sigma| <= {T:.2f}: {len(E)}")
    small = [e for e in order if x[e] < 4][:12]
    print("   smallest generalized integers (n, c(n), Pi(n)): " + "; ".join(f"{x[e]:.4f}:{w[e]:.3g}:{Pi[e]:.3g}" for e in small))
    if neg:
        print(f"   NEGATIVE Pi at {len(neg)} elements; worst: " + "; ".join(f"n={x[e]:.6f} (={e[0]}+{e[1]}phi, n^sigma={xs[e]:.4f}) Pi={p:.4g}" for p, e in neg[:5]))
        first = min(neg, key=lambda t: x[t[1]])
        print(f"   first negative (smallest n): n = {x[first[1]]:.6f} = {first[1][0]}+{first[1][1]}phi, Pi = {first[0]:.4g}, c(n) = {w[first[1]]:.4g}")
    else:
        print("   Pi >= 0 on all computed elements")

if __name__ == "__main__":
    for j in range(0, 4):
        probe(j)
