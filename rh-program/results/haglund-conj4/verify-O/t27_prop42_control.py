# verify-O 2.7a (single-check addition): Proposition 4.2's mechanism on the control f = Xi + lam (lam = 5e-5), an even real
# entire function WITH zeros off the axis. Its Haglund-type pencil is (Xi_k + lam) + t Phi_{k+1} = f - L_t (NOTE N4).
# For the zero beta of f above the 2nd negative lobe: Im f'(beta) (Prop. 4.2 predicts ascent iff > 0), then for k = 1..8 the
# pencil zero near beta at t = 0, 0.5, 1 by Newton, and d(Im z)/dt = Im(-Phi_{k+1}(z)/g'(z)), g = f - L_t.
from core import *
mp.mp.dps = 25
lam = mp.mpf('5e-5')
f = lambda z: Xi(z) + lam
beta = mp.findroot(f, mp.mpc(27.7, 7.2))
fp = mp.diff(f, beta)
print("beta =", mp.nstr(beta, 15), " |f(beta)| =", mp.nstr(abs(f(beta)), 3), " f'(beta) =", mp.nstr(fp, 8), " Im f'(beta) > 0:", fp.imag > 0)
print("Xi(beta) = -lam check:", mp.nstr(Xi(beta), 8))
for k in range(1, 9):
    out = []
    for t in (mp.mpf(0), mp.mpf('0.5'), mp.mpf(1)):
        g = lambda z, t=t: mp.fsum(Phi_G(n, z) for n in range(1, k+1)) + lam + t*Phi_G(k+1, z)
        try:
            z = mp.findroot(g, beta)
        except Exception as e:
            out.append("t=%s: no convergence" % mp.nstr(t, 2)); continue
        gp = mp.diff(g, z)
        dz = -Phi_G(k+1, z)/gp
        out.append("t=%s: |z-beta|=%s dIm/dt=%s" % (mp.nstr(t, 2), mp.nstr(abs(z-beta), 3), mp.nstr(dz.imag, 4)))
    ph = mp.arg(Phi_G(k+1, beta))
    print("k=%d  arg Phi_{k+1}(beta)=%s  |Phi_{k+1}(beta)|/lam=%s  |  %s" % (k, mp.nstr(ph, 4), mp.nstr(abs(Phi_G(k+1, beta))/lam, 3), " ; ".join(out)), flush=True)
