# meansq_split.py — where the information of a mean-square/Parseval argument lives.
# For S8(pi/16) (own dump, X = 1e5) and the lattice control L (same X), with E = N - T truncated at X:
#   Ehat_X(s) = int_1^X E(u) u^{-s-1} du = (F_X(s) - zeta_c(s))/s,
#   F_X(s) = sum_{n<=X} n^{-s} + rho X^{1-s}/(s-1) - E(X) X^{-s}       (s40 NOTE 1.5).
# (1) Parseval: 2 * sum over windows of int_W |Ehat_X(sig+it)|^2 dt  vs  2 pi int_1^X E^2 u^{-2sig-1} du (exact, piecewise).
# (2) The split by frequency window W = [0,1/4], [2^j, 2^(j+1)]: S8 vs L. (3) Discreteness signal:
#     (1/T) int_T^{2T} |s Ehat + zeta_c - (smooth)|^2 = mean square of the Dirichlet polynomial, vs sum_{n<=T} n^{-2 sig}.
import numpy as np, sys
rho = np.pi/16; t = 1/rho; X = 1e5
g = np.fromfile('/private/tmp/rh-s41-lemmaB-U5-obstruction/g_pi16_1e5.bin', dtype=np.float64)
S8 = np.concatenate([[1.0], g[g <= X]])
k = np.arange(1, int((X - 1)*rho + 0.5) + 2); lat = 1 + (k - 0.5)*t
Lc = np.concatenate([[1.0], lat[lat <= X]])
def EX(at): return len(at) - rho*(X - 1) - 1
def parseval_rhs(at, sig):
    a = np.append(at, X); c = np.arange(1, len(at) + 1) - 1 + rho       # E(u) = c_j - rho u on [a_j, a_{j+1})
    lo, hi = a[:-1], a[1:]; l = hi - lo; e0 = c - rho*lo; w = 2*sig
    tot = 0.0
    for xg, wg in ((0.0, 8/9), (np.sqrt(0.6), 5/9), (-np.sqrt(0.6), 5/9)):  # Gauss-Legendre 3 on each piece
        v = l*(1 + xg)/2; tot += np.sum(wg*l/2*(e0 - rho*v)**2*(lo + v)**(-w - 1))
    return 2*np.pi*tot
def Ehat(at, s):
    lg = np.log(at); e = EX(at); out = np.empty(len(s), complex)
    for j in range(0, len(s), 200):
        ss = s[j:j+200]; out[j:j+200] = np.exp(-np.outer(ss, lg)).sum(1)
    F = out + rho*X**(1 - s)/(s - 1) - e*X**(-s); zc = (s - 1 + rho)/(s - 1)
    return (F - zc)/s, out
rng = np.random.default_rng(1)
wins = [(0.0, 0.25)] + [(2.0**j, 2.0**(j + 1)) for j in range(-2, 11)]
for sig in (0.10, 0.30, 0.45):
    print(f"\n=== sigma = {sig}   (Parseval RHS 2pi int E^2 u^(-2sig-1): S8 {parseval_rhs(S8, sig):.5f}   L {parseval_rhs(Lc, sig):.5f})")
    print(" window          int|Eh|^2:S8    L          ratio   | (1/T)int|D_X|^2: S8   L    sum_{n<=T}n^-2sig (S8)")
    tot = {"S8": 0.0, "L": 0.0}
    for (a, b) in wins:
        m = 1500; ts = a + (b - a)*(np.arange(m) + rng.random(m))/m; s = sig + 1j*ts
        row = []
        for nm, at in (("S8", S8), ("L", Lc)):
            eh, D = Ehat(at, s); I = (b - a)*np.mean(np.abs(eh)**2); tot[nm] += I
            row.append((I, np.mean(np.abs(D)**2)))
        diag = np.sum(S8[S8 <= max(b, 1.0)]**(-2*sig))
        print(f" [{a:7.2f},{b:7.1f}]  {row[0][0]:.4e}  {row[1][0]:.4e}  {row[0][0]/row[1][0]:6.3f}  | {row[0][1]:10.3f} {row[1][1]:10.3f}   {diag:10.3f}")
        sys.stdout.flush()
    print(f" 2*sum over windows [0, 2048]: S8 {2*tot['S8']:.5f}   L {2*tot['L']:.5f}   (tail |t| > 2048 not included)")
# (4) block mean squares (1/U) int_U^{2U} E^2 du — Prop. 3.2: >= 1/12 - o(1) for unit atoms at density rho, = 1/12 for L
g6 = np.fromfile('/private/tmp/rh-s41-lemmaB-U5-obstruction/g_pi16_1e6.bin', dtype=np.float64)
S8b = np.concatenate([[1.0], g6[g6 <= 1e6]]); k6 = np.arange(1, int((1e6 - 1)*rho + 0.5) + 2); L6 = np.concatenate([[1.0], (1 + (k6 - 0.5)*t)])
def blockms(at, U):
    a = at[(at > U) & (at < 2*U)]; edges = np.concatenate([[U], a, [2*U]])
    Nst = np.searchsorted(at, U, 'right') + np.arange(len(edges) - 1)        # N on [edges_j, edges_{j+1})
    c = Nst - 1 + rho; lo, hi = edges[:-1], edges[1:]                       # E = c - rho u
    e0 = c - rho*lo; l = hi - lo                                             # re-centred: E = e0 - rho v, v in [0, l]
    return np.sum(e0*e0*l - e0*rho*l*l + rho*rho*l**3/3)/U
print("\n(4) block mean square of E on [U, 2U]:   U      S8(pi/16)     L       1/12 = 0.083333")
for U in (1e3, 1e4, 1e5, 4.9e5):
    print(f"   {U:9.0f}   {blockms(S8b, U):10.4f}   {blockms(L6, U):9.6f}")
