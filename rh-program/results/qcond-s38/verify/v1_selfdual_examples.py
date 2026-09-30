"""v1 (qcond-s38, task 1): self-duality checks for the positive self-dual measures with a gap used in NOTE §1.

A measure mu = sum_x m_x delta_x (even) is tested for mu^ = mu in two ways:
 (G) Gaussian pairing  <mu, g_y> = <mu, g_y^>,  g_y(x) = exp(-pi y x^2), g_y^ = y^{-1/2} g_{1/y}   (theta relation)
 (F) Fejer pairing     <mu, phi_L> = <mu, phi_L^>, phi_L(x) = (1-|x|/L)_+, phi_L^(xi) = L*S(L xi), S(u)=(sin pi u/pi u)^2.
     The right side decays only like xi^-2, so every atom counts; it is summed to X with an explicit tail bound
     tail <= sup-density * 2 * L/(pi^2 L^2 X) (atoms of each lattice comb are spaced >= spacing).
Examples: (a) Poisson pairs pi_a = delta_{aZ} + a^-1 delta_{Z/a}; the q=4 example delta_{Z/2} + 2 delta_{2Z} = pi_{1/2};
(b) twisted combs tau_chi = sum chi(n) delta_{n/sqrt m}, chi real even primitive (m = 5, 8, 12, 13);
(c) F_{5,5} measure = pi_{1/5} + (5/2) pi_1 (conductor 25, scaled by 1/5);
(d) the Bohr-mean multiplicity bound: every non-zero atom mass <= mass at 0 (rho), with equality exactly on a period lattice.
"""
import mpmath as mp
mp.mp.dps = 40

def S(u):
    u = mp.mpf(u)
    if u == 0:
        return mp.mpf(1)
    return (mp.sin(mp.pi*u)/(mp.pi*u))**2

def comb_atoms(spacing, weight_fn, X):
    """atoms x = n*spacing, 0 < x <= X, with weight weight_fn(n) (even measure; returns positive side)."""
    out = []
    n = 1
    while n*spacing <= X:
        w = weight_fn(n)
        if w != 0:
            out.append((n*spacing, w))
        n += 1
    return out

def pair_gauss(mass0, pos_atoms, y):
    return mass0 + 2*mp.fsum(w*mp.e**(-mp.pi*y*x*x) for x, w in pos_atoms)

def pair_fejer_left(mass0, pos_atoms, L):
    return mass0 + 2*mp.fsum(w*max(mp.mpf(0), 1-x/L) for x, w in pos_atoms)

def pair_fejer_right(mass0, pos_atoms, L):
    return mass0*L + 2*mp.fsum(w*L*S(L*x) for x, w in pos_atoms)

def report(name, mass0, combs, Ls=(0.3, 0.7, 1.3, 2.9), ys=(0.37, 1.0, 2.2), X=4000):
    # combs: list of (spacing, weight_fn, |weight| bound)
    atoms = []
    for sp, wf, wb in combs:
        atoms += comb_atoms(sp, wf, X)
    print(f"== {name}: mass at 0 = {mp.nstr(mass0, 12)}")
    for y in ys:
        lhs = pair_gauss(mass0, atoms, y); rhs = pair_gauss(mass0, atoms, 1/mp.mpf(y))/mp.sqrt(y)
        print(f"   Gauss y={y}: <mu,g> - <mu,g^> = {mp.nstr(lhs-rhs, 5)}")
    for L in Ls:
        lhs = pair_fejer_left(mass0, atoms, L); rhs = pair_fejer_right(mass0, atoms, L)
        tail = sum(2*wb*2/(mp.pi**2*L*X*sp) for sp, wf, wb in combs)  # sum_{x>X} L*S(Lx) <= 1/(pi^2 L x^2), spacing sp
        print(f"   Fejer L={L}: left={mp.nstr(lhs,14)} right={mp.nstr(rhs,14)} diff={mp.nstr(lhs-rhs,4)} (tail bound {mp.nstr(tail,3)})")
    return atoms

def merged_masses(atoms, digits=20):
    """merge atoms at the same position (key = rounded position); returns dict pos-key -> total mass."""
    d = {}
    for x, w in atoms:
        k = mp.nstr(x, digits)
        d[k] = d.get(k, 0) + w
    return d

def kronecker(d, n):
    # Kronecker symbol (d/n) for n >= 1, d a fundamental discriminant
    if n == 0:
        return 0
    res = 1
    # factor n
    k = n
    p = 2
    while p*p <= k:
        while k % p == 0:
            res *= kron_prime(d, p)
            k //= p
        p += 1
    if k > 1:
        res *= kron_prime(d, k)
    return res

def kron_prime(d, p):
    if p == 2:
        if d % 2 == 0:
            return 0
        return 1 if d % 8 in (1, 7) else -1
    if d % p == 0:
        return 0
    return 1 if pow(d % p, (p-1)//2, p) == 1 else -1

if __name__ == "__main__":
    print("(a) Poisson pairs pi_a = delta_{aZ} + (1/a) delta_{Z/a}, mass at 0 = 1 + 1/a")
    for a in (mp.mpf(1)/2, mp.mpf(1)/mp.sqrt(3), mp.mpf(1)/mp.sqrt(2), mp.mpf(2)/3):
        report(f"pi_a, a={mp.nstr(a,8)}", 1+1/a, [(a, lambda n: 1, 1), (1/a, lambda n, a=a: 1/a, 1/a)])
    print("   q=4 example: delta_{Z/2} + 2 delta_{2Z} is pi_{1/2} (same atoms and masses) -- see first block above.")
    print("(b) twisted combs tau_chi = sum_n chi(n) delta_{n/sqrt(m)}, chi = Kronecker (m/.) real even primitive; mass at 0 = chi(0) = 0")
    for m in (5, 8, 12, 13):
        sm = mp.sqrt(m)
        report(f"tau_chi, m={m}", mp.mpf(0), [(1/sm, lambda n, m=m: kronecker(m, n), 1)])
    print("(c) F_{5,5} = zeta(s)(1 + 5*5^-s + 5^{1-2s}) at q=25: measure = pi_{1/5} + (5/2) pi_1, mass at 0 = 6 + 5 = 11 = rho_q")
    report("F55 measure", mp.mpf(11), [(mp.mpf(1)/5, lambda n: 1, 1), (mp.mpf(5), lambda n: 5, 5), (mp.mpf(1), lambda n: 5, 5)])
    print("(d) multiplicity bound (Lemma B/C): every nonzero-atom mass <= rho (mass at 0); equality <=> period lattice.")
    for a in (mp.mpf(1)/2, mp.mpf(1)/mp.sqrt(2), mp.mpf(1)/mp.sqrt(3)):
        atoms = comb_atoms(a, lambda n: 1, 60) + comb_atoms(1/a, lambda n, a=a: 1/a, 60)
        mm = merged_masses(atoms)
        mx = max(mm.values()); rho = 1 + 1/a
        nmax = sum(1 for v in mm.values() if abs(v - rho) < mp.mpf(10)**-25)
        print(f"   pi_a a={mp.nstr(a,8)}: max nonzero-atom mass = {mp.nstr(mx,10)}, rho = {mp.nstr(rho,10)}, #atoms in (0,60] with mass = rho: {nmax}")
    atoms = comb_atoms(mp.mpf(1)/5, lambda n: 1, 60) + comb_atoms(mp.mpf(5), lambda n: 5, 60) + comb_atoms(mp.mpf(1), lambda n: 5, 60)
    mm = merged_masses(atoms)
    print(f"   F55: max nonzero-atom mass = {mp.nstr(max(mm.values()),10)} (at multiples of 5), rho = 11 (equality: mu is 5-periodic)")
