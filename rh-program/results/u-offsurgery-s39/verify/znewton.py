"""znewton.py -- Newton refinement of a zero of zeta_P(s) = rho*zeta(s) + D_X(s) (D from zpoint, zeta via mpmath).
Usage: python3 znewton.py a.u16 X rho sigma0 t0 [steps]"""
import sys, subprocess, mpmath as mp
fa, X, rho, s0, t0 = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])
steps = int(sys.argv[6]) if len(sys.argv) > 6 else 6
z = mp.mpc(s0, t0)
for k in range(steps):
    out = subprocess.run(["./zpoint", fa, X, str(rho), repr(float(z.real)), repr(float(z.imag))], capture_output=True, text=True).stdout.split()
    D = mp.mpc(float(out[2]), float(out[3])); Dp = mp.mpc(float(out[4]), float(out[5]))
    F = rho * mp.zeta(z) + D; Fp = rho * mp.zeta(z, derivative=1) + Dp
    print(f"step {k}: s = {mp.nstr(z, 12)}  |F| = {mp.nstr(abs(F), 4)}  |F'| = {mp.nstr(abs(Fp), 4)}", flush=True)
    z = z - F / Fp
print("final", mp.nstr(z, 14))
