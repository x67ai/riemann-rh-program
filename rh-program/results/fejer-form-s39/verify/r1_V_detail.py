"""Unit fejer-form-s39, rung 1, step 4: V (q, t) = (5, 5) and V2 = 1 - u + 11u^2 - 5u^3 + 25u^4 in detail; closed forms vs LP.
Closed form (NOTE §3): for g = 1 and theta = i y (V: e^y = phi), T_M = u v^T + v u^T with u_k = e^{-ky}, v_k = e^{ky}, so
lambda_min(T_M) = (M+1) - |u||v|, and min over f = |P|^2 >= 0 of degree M with mean 1 of f(theta_V) is ((M+1) - |u||v|)/2."""
import json, math
import numpy as np
from scipy.optimize import linprog
phi = (1 + 5**0.5) / 2; y = math.log(phi); q = 5
print("cos(theta_V) = cosh(log phi) = %.15f ; sqrt5/2 = %.15f" % (math.cosh(y), 5**0.5 / 2))
TH = np.linspace(0, math.pi, 20001)
for M in range(1, 9):
    u = np.array([math.exp(-k * y) for k in range(M + 1)]); v = 1 / u
    closed = ((M + 1) - np.linalg.norm(u) * np.linalg.norm(v)) / 2
    p = np.array([2 * math.cosh(n * y) for n in range(1, M + 1)])       # p_n(V) = L_n (Lucas numbers)
    T = np.array([[([2.0] + list(p))[abs(a - b)] for b in range(M + 1)] for a in range(M + 1)])
    lam = np.linalg.eigvalsh(T)[0]
    A = np.array([[-2 * math.cos(n * t) for n in range(1, M + 1)] for t in TH])
    res = linprog(p, A_ub=A, b_ub=np.ones(len(TH)), bounds=[(-1, 1)] * M, method='highs')
    print("M=%d  lambda_min(T_M(V)) = %+.10f (closed %+.10f)   LP(A) min f(theta_V) = %+.10f (closed %+.10f)  c = %s"
          % (M, lam, (M + 1) - np.linalg.norm(u) * np.linalg.norm(v), 1 + res.fun, closed, np.round(res.x, 4).tolist()))
print("Lucas check p_n(V) = 5^{-n/2} s_n:", [round(2 * math.cosh(n * y), 9) for n in range(1, 6)],
      "s_n from L:", [5, 15, 50, 175, 625])
# M = 1 test: f = 1 - cos theta  <=>  I(Z) = g - p_1/2 = g - (q+1-N_1)/(2 sqrt q) >= 0  <=>  N_1 >= q + 1 - 2 g sqrt q
for name, N1, g in (("V", 1, 1), ("E0", 2, 1), ("P1", 6, 0)):
    print("%s: I_{1-cos}(Z) = %+.10f   Weil lower bound q+1-2g sqrt q = %.6f vs N_1 = %d" % (name, g - (q + 1 - N1) / (2 * 5**0.5), q + 1 - 2 * g * 5**0.5, N1))
# norm form: (1/2) x^T T_1 x with x = (m, n sqrt5) is m^2 + t m n + q n^2 (proof-mine §1, B7)
for (m, n) in ((1, 0), (2, -1), (1, -1)):
    x = np.array([m, n * 5**0.5]); T1 = np.array([[2, 5**0.5], [5**0.5, 2]])
    print("(m,n)=(%d,%d): (1/2) x^T T_1(V) x = %+.6f ; m^2 + 5mn + 5n^2 = %d" % (m, n, 0.5 * x @ T1 @ x, m * m + 5 * m * n + 5 * n * n))
# class (B) at q=5, g=1: f >= 0 only at the 9 genuine angles
gen = [math.acos(t / (2 * 5**0.5)) for t in range(-4, 5)]
for M in (1, 2, 8):
    p = np.array([2 * math.cosh(n * y) for n in range(1, M + 1)])
    A = np.array([[-2 * math.cos(n * t) for n in range(1, M + 1)] for t in gen])
    res = linprog(p, A_ub=A, b_ub=np.ones(len(gen)), bounds=[(-1, 1)] * M, method='highs')
    f = lambda t: 1 + 2 * sum(res.x[n - 1] * math.cos(n * t) for n in range(1, M + 1))
    fm = min(f(t) for t in TH)
    print("class B, M=%d: min f(theta_V) = %+.6f ; min of f on the real circle = %+.6f (%s)" % (M, 1 + res.fun, fm, "a Weil test" if fm > -1e-9 else "NOT >= 0 on the circle: uses the discrete genuine spectrum"))
# V2 (q=5, g=2, a1=-1, a2=11)
Z = json.load(open('r1_zeta_data.json'))
r = [r for r in Z['5'] if r['g'] == 2 and r['a1'] == -1 and r['a2'] == 11][0]
p = np.array([r['s'][n] / 5**(n / 2) for n in range(1, 9)])
for M in range(1, 5):
    P = np.concatenate([[4.0], p[:M]]); T = np.array([[P[abs(a - b)] for b in range(M + 1)] for a in range(M + 1)])
    w, V = np.linalg.eigh(T)
    print("V2: M=%d lambda_min = %+.6f  eigvec = %s" % (M, w[0], np.round(V[:, 0], 4).tolist()))
fe = lambda M, tw: 2 + sum((1 - n / (M + 1)) * ((-1)**n if tw else 1) * p[n - 1] for n in range(1, M + 1))
print("V2 Fejer untwisted K_M, M=1..8:", [round(fe(M, False), 4) for M in range(1, 9)])
print("V2 Fejer twisted   K_M(.+pi):   ", [round(fe(M, True), 4) for M in range(1, 9)])
