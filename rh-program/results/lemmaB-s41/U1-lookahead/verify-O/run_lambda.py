# read-O driver: certify Lambda(sigma_1) > 0 at the NOTE's table points; locate the largest root sigma_L.
import sys, time
from flint import arb
import mpmath as mp
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from lambda_arb import rho_of, pieces, Lam_arb, Lam_quad

TAU = {"1/2": (1, 2), "1/4": (1, 4), "1/10": (1, 10), "1/20": (1, 20), "1/50": (1, 50), "1/100": (1, 100), "1/1000": (1, 1000), "1": (1, 1)}
def tau_of(s): n, d = TAU[s]; return arb(n)/arb(d), mp.mpf(n)/d

rows = [("pi/16","1/2","0.763"),("pi/16","1/10","0.911"),("pi/16","1/50","0.979"),("pi/16","1/100","0.989"),
        ("pi/32","1/2","0.888"),("pi/32","1/100","0.990"),("pi/8","1/100","0.989"),("pi/4","1/10","0.869"),
        ("pi/4","1/100","0.989"),("0.95pi/3","1/100","0.989"),("pi/4","1/1000","0.998")]

def root(rname, tname, pcs, lo=0.30, hi=0.99999, n=4000):
    rho = rho_of(rname); tau, _ = tau_of(tname)
    f = lambda x: Lam_arb(rho, tau, arb(x), pcs).mid()
    # scan downward from hi for the first sign change (largest root)
    xs = [hi - (hi - lo)*i/n for i in range(n + 1)]
    prev = float(f(xs[0]))
    for x in xs[1:]:
        v = float(f(x))
        if v > 0 and prev < 0:
            a, b = x, x + (hi - lo)/n   # Lambda(a) > 0 > Lambda(b)
            for _ in range(60):
                m = (a + b)/2
                if float(f(m)) > 0: a = m
                else: b = m
            return a, b
        prev = v
    return None

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "cert"
    if mode == "cert":
        for (rn, tn, s1) in rows:
            t0 = time.time()
            rho = rho_of(rn); tau, tauf = tau_of(tn)
            pcs = pieces(rho, tau)
            v = Lam_arb(rho, tau, arb(s1), pcs)
            q = Lam_quad(mp.mpf(rho.mid().str(40, radius=False)), tauf, mp.mpf(s1), pcs)
            lower = v.lower() if hasattr(v, "lower") else v.mid() - v.rad()
            print(f"rho={rn:9s} tau={tn:7s} sigma1={s1}  pieces={len(pcs):5d}  Lambda(arb)={v.str(12)}  "
                  f"lower>0:{bool(v > 0)}  quad={mp.nstr(q, 12)}  sigma1/2={float(s1)/2}  [{time.time()-t0:.1f}s]", flush=True)
    else:
        for (rn, tn) in [("pi/16","1/2"),("pi/16","1/4"),("pi/16","1/10"),("pi/16","1/20"),("pi/16","1/50"),("pi/16","1/100"),
                         ("pi/32","1/2"),("pi/32","1/100"),("pi/8","1/100"),("pi/4","1/10"),("pi/4","1/100"),("0.95pi/3","1/100"),
                         ("pi/4","1/1000"),("pi/4","1/2")]:
            rho = rho_of(rn); tau, _ = tau_of(tn); pcs = pieces(rho, tau)
            r = root(rn, tn, pcs, n=(800 if tn != "1/1000" else 200))
            print(f"rho={rn:9s} tau={tn:7s} sigma_L in {('[%.10f, %.10f]' % r) if r else 'NO ROOT in (0.30, 0.99999)'}", flush=True)
