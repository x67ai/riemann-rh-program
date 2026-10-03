# signcheck.py -- sign convention of NOTE Prop. 4.2 on the control f = Xi + lam (lam = 5e-5), which has zeros off the axis.
# (1) find a zero beta of f in the upper half-plane; (2) Im f'(beta); (3) the zero of the pencil (Xi_k + lam) + t Phi_{k+1}
# near beta at t = 0 and t = 1 for k = 3, 4: Prop. 4.2 says Im z increases with t iff Im f'(beta) > 0.
from c4probe import *
ctx.prec = 300
lam = 5e-5
def cXi(z):
    v = Xi(acb(z.real, z.imag)); return complex(float(v.real.mid()), float(v.imag.mid()))
def newton(g, z, it=60, h=1e-7):
    for _ in range(it):
        d = (g(z + h) - g(z - h)) / (2 * h)
        dz = g(z) / d; z -= dz
        if abs(dz) < 1e-14: break
    return z
f = lambda z: cXi(z) + lam
for guess in (24.5 + 0.8j, 27.5 + 1.5j, 26.0 + 2.0j):
    b = newton(f, guess)
    fp = (f(b + 1e-6) - f(b - 1e-6)) / 2e-6
    print("guess %s -> beta = %.8f%+.8fi  |f(beta)| = %.1e  f'(beta) = %.4e%+.4ei  Im f'(beta) %s 0" % (guess, b.real, b.imag, abs(f(b)), fp.real, fp.imag, ">" if fp.imag > 0 else "<"))
def pencil_zero(k, t, z0):
    def g(z):
        a, bb = pair_T(k, acb(z.real, z.imag))            # a = Xi_{k+1}, bb = Phi_{k+1};  Xi_k + t Phi_{k+1} = a - (1-t) bb
        v = a + lam - (1 - t) * bb
        return complex(float(v.real.mid()), float(v.imag.mid()))
    return newton(g, z0)
b = newton(f, 26.0 + 2.0j)
for k in (3, 4):
    z0 = pencil_zero(k, 0.0, b); z1 = pencil_zero(k, 1.0, b)
    print("k=%d: zero at t=0: %.12f%+.12fi   at t=1: %.12f%+.12fi   change of Im z = %+.3e   (beta: Im = %.12f)" % (k, z0.real, z0.imag, z1.real, z1.imag, z1.imag - z0.imag, b.imag))
