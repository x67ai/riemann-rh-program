# same bound as powerbump_bound.py, for larger densities (the bound never uses rho < 1/4)
import importlib.util, sys
from mpmath import mp, mpf, pi
spec = importlib.util.spec_from_file_location("pb", "powerbump_bound.py")
src = open("powerbump_bound.py").read().split("for rho_name, rho in")[0]; exec(src)
for rho_name, rho in [("pi/8", pi / 8), ("pi/4", pi / 4), ("0.95pi/3", mpf("0.95") * pi / 3)]:
    for tau in [mpf(1) / 2, mpf(1) / 10, mpf(1) / 100]:
        p1 = 1 + tau / rho; sL = root(rho, tau, p1)
        print(f"rho={rho_name} tau={mp.nstr(tau, 3)} p1={mp.nstr(p1, 7)} sigma_L={mp.nstr(sL, 8) if sL else None}  half={mp.nstr(sL / 2, 6) if sL else None}")
