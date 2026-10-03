from signcheck import *   # re-runs the first prints; harmless
import math
xs = [25.0 + 0.01 * i for i in range(545)]
vals = [cXi(complex(x, 0)).real for x in xs]
i0 = min(range(len(xs)), key=lambda i: vals[i]); xm, vm = xs[i0], vals[i0]
kap = (cXi(complex(xm + 0.01, 0)).real - 2 * vm + cXi(complex(xm - 0.01, 0)).real) / 1e-4
print("second negative lobe: min Xi = %.4e at x = %.2f, curvature %.3e" % (vm, xm, kap))
if -vm < lam:
    y0 = math.sqrt(2 * (lam + vm) / kap)
    b = newton(f, complex(xm, y0))
    fp = (f(b + 1e-6) - f(b - 1e-6)) / 2e-6
    print("off-axis zero of Xi + lam: beta = %.10f%+.10fi  |f| = %.1e   f'(beta) = %.4e%+.4ei" % (b.real, b.imag, abs(f(b)), fp.real, fp.imag))
    for k in (2, 3, 4):
        z0 = pencil_zero(k, 0.0, b); zh = pencil_zero(k, 0.5, b); z1 = pencil_zero(k, 1.0, b)
        print("k=%d: Im z at t=0, 0.5, 1: %.12f  %.12f  %.12f   (Im beta = %.12f)  total change %+.3e" % (k, z0.imag, zh.imag, z1.imag, b.imag, z1.imag - z0.imag))
