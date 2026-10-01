"""cert7.py -- winding-number box for a zero of F_X (K'-type certificate, floating point), by Taylor moments at the box centre
(one pass over the a_n: `zline ... m`), validated against direct sums at the four corners (`zline ... p`).
F(s) = rho*zeta(s) + sum_k M_k (s - s0)^k on the boundary of B = [s0r - h, s0r + h] x [s0i - h, s0i + h].
Tail bound under H_theta (|C(u)| <= u^theta, u > X): |zeta_P - F_X| <= |C(X)| X^-sigma + |s| X^(theta - sigma)/(sigma - theta).
Usage: python3 cert7.py a.u16 X num den s0r s0i h K npts"""
import sys, subprocess, numpy as np, mpmath as mp
A, X, num, den = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
s0 = complex(float(sys.argv[5]), float(sys.argv[6])); h = float(sys.argv[7]); K = int(sys.argv[8]); npts = int(sys.argv[9])
rho = num / den; ZL = "/private/tmp/rh-s40-local-greedy/zline"; PF = "/private/tmp/rh-s40-local-greedy/cert_pts.txt"
open(PF, "w").write("%.15f %.15f\n" % (s0.real, s0.imag))
out = subprocess.run([ZL, A, X, str(num), str(den), "m", PF, str(K)], capture_output=True, text=True).stdout.split("\n")
CX = float(out[0].split("C(X)=")[1].split()[0]); M = np.array([complex(float(l.split()[1]), float(l.split()[2])) for l in out[2:2 + K + 1]])
def F(s): return complex(rho * mp.zeta(s)) + np.polyval(M[::-1], s - s0)
q = npts // 4; c = [s0 + complex(-h, -h), s0 + complex(h, -h), s0 + complex(h, h), s0 + complex(-h, h)]
path = np.concatenate([np.linspace(c[i], c[(i + 1) % 4], q, endpoint=False) for i in range(4)] + [np.array([c[0]])])
vals = np.array([F(s) for s in path]); d = np.diff(np.angle(vals)); d = (d + np.pi) % (2 * np.pi) - np.pi
print("# cert7 X=%s rho=%d/%d centre %.10f%+.10fi  h=%.4f K=%d  C(X)=%.4g" % (X, num, den, s0.real, s0.imag, h, K, CX))
print("winding number %.6f, min|F| on boundary %.5f, largest phase step %.4f rad, |M_K| h^K = %.2e" % (d.sum() / (2 * np.pi), np.abs(vals).min(), np.abs(d).max(), abs(M[-1]) * h**K))
open(PF, "w").write("".join("%.15f %.15f\n" % (s.real, s.imag) for s in c))
out = subprocess.run([ZL, A, X, str(num), str(den), "p", PF], capture_output=True, text=True).stdout.split("\n")
for s, l in zip(c, [l for l in out if l and l[0] != '#']):
    Fd = complex(float(l.split()[6]), float(l.split()[7])); print("corner %.4f%+.4fi: direct F = %.10f%+.10fi, Taylor F = %.10f%+.10fi, |diff| = %.2e" % (s.real, s.imag, Fd.real, Fd.imag, F(s).real, F(s).imag, abs(Fd - F(s))))
Xf = float(X)
for th in (0.30, 0.35, 0.40, 0.45):
    tb = max(abs(CX) * Xf**(-s.real) + abs(s) * Xf**(th - s.real) / (s.real - th) for s in path)
    print("theta=%.2f: tail bound max over boundary %.5f  (ratio min|F|/tail = %.2f)" % (th, tb, np.abs(vals).min() / tb))
