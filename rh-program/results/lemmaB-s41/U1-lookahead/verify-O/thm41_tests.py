# read-O: Theorem 4.1 tested on explicit systems. (a) template vs Lambda; (b) N (rho = tau = 1, p* = 2): zeta(sigma) >= Lambda_{1,1}(sigma)
# on (0,1), with zeta from mpmath; (c) Lambda_{1,1} < 0 on (0,1) (Remark 4.5's contrapositive for N).
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from flint import arb
import mpmath as mp
from lambda_arb import rho_of, pieces, Lam_arb
mp.mp.dps = 30
rho = rho_of("pi/16"); tau = arb(1)/100; pcs = pieces(rho, tau)
for s in ["0.95", "0.98", "0.985", "0.989"]:
    print(f"(a) pi/16 tau=1/100 sigma={s}: Lambda={Lam_arb(rho, tau, arb(s), pcs).str(8)}  zeta_c={1 - float(rho.mid())/(1 - float(s)):.4f}")
r1 = arb(1); t1 = arb(1); p1 = pieces(r1, t1)
print("(b) pieces for N (rho=tau=1):", [(k, a.str(5), b.str(5)) for k, a, b in p1])
worst = None
for i in range(1, 200):
    s = i/200
    L = float(Lam_arb(r1, t1, arb(s), p1).mid()); z = float(mp.zeta(s))
    if worst is None or z - L < worst[0]: worst = (z - L, s, z, L)
    if L >= 0: print("(c) Lambda_{1,1} >= 0 at", s)
print(f"(b) min over sigma in (0,1) grid of zeta - Lambda_(1,1) = {worst[0]:.6f} at sigma = {worst[1]} (zeta {worst[2]:.6f}, Lambda {worst[3]:.6f})")
for s in [0.1, 0.5, 0.9, 0.99]:
    print(f"    sigma={s}: zeta={float(mp.zeta(s)):+.6f}  Lambda_11={float(Lam_arb(r1, t1, arb(s), p1).mid()):+.6f}")
