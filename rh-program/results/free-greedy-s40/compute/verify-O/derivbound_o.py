# derivbound_o.py -- a derivative bound for F_X on the Rouche box that does not sample F': |F_X'(s)| <= S1 + M1 with
# S1 = sum_{n<=X} n^{-smin} log n <= rho int_1^X u^{-smin} log u du + supE_abs * TV_[1,X](u^{-smin} log u)   (parts; |E| <= Eabs on [1, X])
# M1 = max |d/ds (rho X^{1-s}/(s-1) - E(X) X^{-s})| on the box. Then min|F| >= min_sampled - (S1 + M1) h / 2. Opus reader.
import math, cmath
X = 1e10; rho = math.pi / 4; Eabs = 113.2048359644; EX = 4.810915          # proved run to 1e10 (o_pi4_1e10.log)
c = complex(0.8962124913, 14.5499355887); r = 0.03; smin = c.real - r; n = 4000; h = 2 * r / n
a = 1 - smin; L = math.log(X)
I = rho * (X ** a * (L / a - 1 / a ** 2) + 1 / a ** 2)                   # rho int_1^X u^{-smin} log u du
TV = 2 * (1 / (math.e * smin))                                              # u^{-s} log u rises to 1/(e s) then falls to >= 0
S1 = I + Eabs * TV
M1 = 0
for k in range(4 * 400):
    u = -r + 2 * r * (k % 400) / 400
    s = [complex(c.real + r, c.imag + u), complex(c.real - u, c.imag + r), complex(c.real - r, c.imag - u), complex(c.real + u, c.imag - r)][k // 400]
    Xs = cmath.exp(-s * L); main = rho * X * Xs / (s - 1)
    M1 = max(M1, abs(main * (-L - 1 / (s - 1)) + EX * L * Xs))
Fmin = 0.123786                                                             # sampled min |F_X| at 4000/side (rouche_o_pi4_X.txt)
low = Fmin - (S1 + M1) * h / 2
Kmax = 0.123747 / 5752.4                                                   # max K on the box at X = 1e10 (rouche_o_pi4_X.txt)
print(f"S1 <= {S1:.1f} (integral {I:.1f} + E-term {Eabs*TV:.1f}); M1 = {M1:.2f}; |F'| <= {S1+M1:.1f} (sampled max 5.218)")
print(f"gap (S1+M1) h/2 = {(S1+M1)*h/2:.4f}; min|F_1e10| >= {low:.4f}; max arg step <= {math.asin(min(1,(S1+M1)*h/low)):.3f} rad (< pi)")
print(f"B_max (log^2, u > 1e10) >= {low / Kmax:.0f} with this rigorous derivative bound (sampled-gap version: 6531)")
