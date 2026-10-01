"""v3 (qtwin-s39): route (ii) -- the Pisot model-set measures of Q(sqrt5).
O_K = Z[phi], sigma: sqrt5 -> -sqrt5, c = 5^{1/4}.  mu_k := sum_{x in O_K} k(x^sigma/c) delta_{x/c}.  Poisson on the unimodular
lattice {(x/c, x^sigma/c)} gives mu_k^ = mu_{k^}; so mu_k is EXACTLY self-dual iff k^ = k (NOTE §5).
Part A: the acceptance test on k = exp(-pi t^2): theta pairing <mu,g_y> = <mu,g_y^> at 40 digits (whole lattice, terms < 1e-60
        dropped) and the Fejer pairing <mu,phi_L> = <mu,phi_L^> with an explicit xi^{-2} tail bound.
Part B: the gap at q = sqrt5*phi^{2j}: atoms of mu_k in (0, r), r = q^{-1/2} (must all vanish; for the Gaussian they do not).
Part C: the zero set Z_j = {n^sigma*phi^j/c : n in O_K, 0 < |n| < 1} that an admissible k must vanish on: first points, separation, density.
Part D: Beurling probe for the Gaussian family (normalized so the atom '1' has mass 1): Pi = log*(c) on O_K ∩ [1, X], |n^sigma| <= T.
"""
import mpmath as mp
import math
mp.mp.dps = 50
PHI = (1 + mp.sqrt(5))/2
C = mp.mpf(5)**(mp.mpf(1)/4)
def val(a, b): return a + b*PHI
def conj(a, b): return a + b*(1 - PHI)

def lattice_points(U, V):
    """all (a,b) with |x| <= U, |x^sigma| <= V (x = a + b phi)."""
    out = []
    s5 = math.sqrt(5.0)
    bmin, bmax = int(math.floor(-(U + V)/s5)) - 1, int(math.ceil((U + V)/s5)) + 1
    for b in range(bmin, bmax + 1):
        # x = a + b phi in [-U, U] and a + b(1-phi) in [-V, V]
        lo = max(-U - b*1.618033988749895, -V - b*(1 - 1.618033988749895))
        hi = min(U - b*1.618033988749895, V - b*(1 - 1.618033988749895))
        for a in range(int(math.floor(lo)) - 1, int(math.ceil(hi)) + 2):
            if abs(a + b*1.618033988749895) <= U + 1e-9 and abs(a + b*(1 - 1.618033988749895)) <= V + 1e-9:
                out.append((a, b))
    return out

def k_gauss(t): return mp.e**(-mp.pi*t*t)

def partA():
    print("Part A: acceptance test, k = exp(-pi t^2)")
    pts = lattice_points(40.0, 40.0)
    for y in (mp.mpf('0.37'), mp.mpf(1), mp.mpf('2.2')):
        lhs = mp.fsum(k_gauss(conj(a, b)/C)*mp.e**(-mp.pi*y*(val(a, b)/C)**2) for a, b in pts)
        rhs = mp.fsum(k_gauss(conj(a, b)/C)*mp.e**(-mp.pi*(val(a, b)/C)**2/y) for a, b in pts)/mp.sqrt(y)
        print(f"   theta y={mp.nstr(y,4)}: <mu,g> = {mp.nstr(lhs, 25)}  <mu,g^> = {mp.nstr(rhs, 25)}  diff = {mp.nstr(lhs - rhs, 3)}")
    X = 400.0
    pts = lattice_points(X*float(C), 12.0)
    for L in (mp.mpf('0.3'), mp.mpf('0.7'), mp.mpf('1.3')):
        left = mp.fsum(k_gauss(conj(a, b)/C)*max(mp.mpf(0), 1 - abs(val(a, b)/C)/L) for a, b in pts)
        def S(u): return mp.mpf(1) if u == 0 else (mp.sin(mp.pi*u)/(mp.pi*u))**2
        right = mp.fsum(k_gauss(conj(a, b)/C)*L*S(L*val(a, b)/C) for a, b in pts)
        tail = 2*1.05/(mp.pi**2*L*X)   # mass density of mu is int k = 1 per unit length (+5% margin); sum_{|u|>X} L S(Lu) <= 2 dens/(pi^2 L X)
        print(f"   Fejer L={mp.nstr(L,3)}: left = {mp.nstr(left, 15)} right = {mp.nstr(right, 15)} diff = {mp.nstr(left - right, 3)} (tail bound {mp.nstr(tail, 3)})")

def partB():
    print("Part B: the gap (-r, r), r = q^{-1/2}, q = sqrt5*phi^{2j}: atoms of mu_k (Gaussian k) inside (0, r), largest first")
    for j in range(0, 4):
        q = mp.sqrt(5)*PHI**(2*j); r = 1/mp.sqrt(q)
        pts = [(a, b) for a, b in lattice_points(float(r*C), 30.0) if 0 < val(a, b)/C < r]
        masses = sorted(((k_gauss(conj(a, b)/C), a, b) for a, b in pts), reverse=True)[:4]
        one = k_gauss(conj(0, 0)/C)  # placeholder
        x1 = (PHI**(-j))  # the atom '1' is x = phi^{-j}
        m1 = k_gauss(x1**(-1)*(-1)**j/C) if j else k_gauss(mp.mpf(1)/C)
        print(f"   j={j}: q = {mp.nstr(q, 8)}, r = {mp.nstr(r, 8)}; mass of the atom '1' (x = phi^-{j}) = {mp.nstr(m1, 6)}; "
              f"largest masses in (0,r): " + ", ".join(f"{mp.nstr(m, 4)} at x={a}+{b}phi" for m, a, b in masses))

def partC():
    print("Part C: the zero set Z_j (in the variable of k): an admissible k must vanish on {n^sigma phi^j / c : 0 < |n| < 1}")
    for j in range(0, 4):
        pts = lattice_points(1.0, 60.0)
        Z = sorted(set(round(float(conj(a, b)*PHI**j/C), 12) for a, b in pts if 0 < abs(float(val(a, b))) < 1))
        Zp = [z for z in Z if z > 0]
        gaps = [Zp[i+1] - Zp[i] for i in range(len(Zp) - 1)]
        cnt = len([z for z in Z if abs(z) <= 40*float(PHI**j/C)])
        dens = cnt/(2*40*float(PHI**j/C))
        print(f"   j={j}: first positive zeros {[round(z, 5) for z in Zp[:8]]}; min gap {min(gaps):.5f}, max gap (|z|<20) "
              f"{max(g for g, z in zip(gaps, Zp) if z < 20):.5f}; density {dens:.4f} per unit length (predicted 2/(c phi^j) = {2/float(C*PHI**j):.4f})")

if __name__ == "__main__":
    partA(); partB(); partC()
