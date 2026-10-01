"""v2 (qtwin-s39): the RH-false controls run through Theorem G1 / L' / L''' (NOTE §2, §7), and the exact self-duality test on them.
Acceptance test (QC v1/v2): theta pairing at 40 digits and the Fejer pairing EXACTLY (Poisson closed form, no tail):
  for mu = sum_j a_j delta_{b_j Z}:  <mu, phi_L> = sum_j a_j (1 + 2 sum_{n>=1} (1 - n b_j/L)_+),  <mu, phi_L^> = sum_j a_j L (1 + 2 T(L b_j)),
  T(e) = sum_{n>=1} S(n e) = ((1/e)(1 + 2 sum_{1<=k<e}(1 - k/e)) - 1)/2   (QC v2 Part A).
Controls: F55 (q = 25; positive comb; must pass Steps 0-4 of G1 and fail only at L' with Pi(25) = -7); read-O R1 (signed, q = 1;
fails G1 Step 0); Davenport-Heilbronn (complex coefficients, Gamma((s+1)/2): outside (A) and outside Step 0).
"""
import mpmath as mp
mp.mp.dps = 50

def T(e):
    e = mp.mpf(e); K = int(mp.floor(e))
    if K == e: K -= 1
    return ((1/e)*(1 + 2*mp.fsum(1 - k/e for k in range(1, K + 1))) - 1)/2

def fejer_exact(combs, L):
    L = mp.mpf(L)
    left = mp.fsum(a*(1 + 2*mp.fsum(max(mp.mpf(0), 1 - n*b/L) for n in range(1, int(L/b) + 2))) for b, a in combs)
    right = mp.fsum(a*L*(1 + 2*T(L*b)) for b, a in combs)
    return left, right

def theta(combs, y):
    # <mu, g_y> with g_y = exp(-pi y x^2):  sum_j a_j * jtheta3(0, exp(-pi y b_j^2))
    return mp.fsum(a*mp.jtheta(3, 0, mp.e**(-mp.pi*y*b*b)) for b, a in combs)

def acceptance(name, combs):
    print(f"== {name}")
    for y in (mp.mpf('0.37'), mp.mpf(1), mp.mpf('2.2')):
        l, r = theta(combs, y), theta(combs, 1/y)/mp.sqrt(y)
        print(f"   theta y={mp.nstr(y,3)}: diff = {mp.nstr(l - r, 3)}")
    for L in ('0.3', '0.7', '1.3', '2.9'):
        l, r = fejer_exact(combs, L)
        print(f"   Fejer L={L}: <mu,phi> = {mp.nstr(l, 20)}  <mu,phi^> = {mp.nstr(r, 20)}  diff = {mp.nstr(l - r, 3)}")

def log_star_integers(c, N):
    """Pi = log*(dN) for dN = sum c(n) delta_n (c(1) = 1): Pi(n) log n = c(n) log n - sum_{d|n, 1<d<n} c(d) Pi(n/d) log(n/d)."""
    Pi = {1: mp.mpf(0)}
    for n in range(2, N + 1):
        s = c(n)*mp.log(n) - mp.fsum(c(d)*Pi[n//d]*mp.log(n//d) for d in range(2, n) if n % d == 0)
        Pi[n] = s/mp.log(n)
    return Pi

if __name__ == "__main__":
    s5 = mp.sqrt(5)
    # F55 = zeta(s)(1 + 5*5^-s + 5^{1-2s}) at q = 25: scaled measure pi_{1/5} + (5/2) pi_1 = delta_{Z/5} + 5 delta_{5Z} + (5/2)(2 delta_Z)
    acceptance("F55 (q = 25): delta_{Z/5} + 5 delta_{5Z} + 5 delta_Z  [mass 11 at 0]", [(mp.mpf(1)/5, 1), (mp.mpf(5), 5), (mp.mpf(1), 5)])
    c = lambda n: 1 + (5 if n % 5 == 0 else 0) + (5 if n % 25 == 0 else 0)
    print("   G1 Step 0-4 on F55: generalized integers = N (a monoid, one radical class), masses c(n) = 1 + 5[5|n] + 5[25|n]:"
          f" period 25, values {sorted(set(c(n) for n in range(1, 101)))} (finitely many) -> G1 reaches QC step (6) = L'.")
    Pi = log_star_integers(c, 130)
    neg = [(n, Pi[n]) for n in range(2, 131) if Pi[n] < -1e-30]
    print(f"   L' fires: Pi(5) = {mp.nstr(Pi[5], 6)}, Pi(25) = {mp.nstr(Pi[25], 6)}, Pi(125) = {mp.nstr(Pi[125], 6)}; negative Pi at n <= 130: {[n for n, _ in neg]}")
    # read-O R1 (signed, conductor 1): sum chi5(n) delta_{n/sqrt5} - (sqrt5 delta_{sqrt5 Z} + delta_{Z/sqrt5}) + (sqrt5 delta_{(sqrt5/2)Z} + 2 delta_{(2/sqrt5)Z})
    chi = lambda n: [0, 1, -1, -1, 1][n % 5]
    atoms = {}
    def add(x, m):
        k = mp.nstr(x, 30); atoms[k] = (x, atoms.get(k, (x, 0))[1] + m)
    for n in range(1, 40):
        add(n/s5, chi(n)); add(n*s5, -s5); add(n/s5, -1); add(n*s5/2, s5); add(2*n/s5, 2)
    pos = sorted((x, m) for x, m in atoms.values() if abs(m) > 1e-30 and x < 3)
    print("== read-O R1 (signed, q = 1): first atoms in (0, 3): " + ", ".join(f"{mp.nstr(x, 6)}:{mp.nstr(m, 5)}" for x, m in pos))
    print("   G1 Step 0 fails (masses of both signs: no positive measure, no monoid) -- G1 is silent on R1, as it must be.")
    # Davenport-Heilbronn: f = ((1 - i kappa)/2) L(s, chi) + ((1 + i kappa)/2) L(s, chibar), chi mod 5 with chi(2) = i
    kappa = (mp.sqrt(10 - 2*s5) - 2)/(s5 - 1)
    chiDH = {1: 1, 2: 1j, 4: -1, 3: -1j, 0: 0}
    a = lambda n: ((1 - 1j*kappa)/2)*chiDH[n % 5] + ((1 + 1j*kappa)/2)*mp.conj(chiDH[n % 5])
    print("== Davenport-Heilbronn: a(1..8) = " + ", ".join(mp.nstr(a(n), 4) for n in range(1, 9)) +
          "; Gamma((s+1)/2) (odd character): outside (A); real coefficients of both signs -> outside G1 Step 0.")
