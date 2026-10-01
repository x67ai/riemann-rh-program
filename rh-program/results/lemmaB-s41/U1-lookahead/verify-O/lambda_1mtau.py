# read-O, m9: sign of Lambda_{rho,tau}(1 - tau) (is "theta < 1/2 - tau/2" certified?) and (1 - sigma_L)/tau.
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from flint import arb
from lambda_arb import rho_of, pieces, Lam_arb
for rn in ["pi/32", "pi/16", "pi/8", "pi/4", "0.95pi/3"]:
    for (n, d) in [(1, 2), (1, 10), (1, 100), (1, 1000)]:
        if d == 1000 and rn not in ("pi/16", "pi/4"): continue
        rho = rho_of(rn); tau = arb(n)/arb(d); pcs = pieces(rho, tau)
        v = Lam_arb(rho, tau, 1 - tau, pcs)
        print(f"rho={rn:9s} tau={n}/{d:<5d} Lambda(1 - tau) = {v.str(8):>28s}  sign {'+' if v > 0 else ('-' if v < 0 else '?')}", flush=True)
