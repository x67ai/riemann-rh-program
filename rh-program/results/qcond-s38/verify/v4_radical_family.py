"""v4 (qcond-s38): Theorem L' on a RADICAL (two-class) family, q = 2.
F = zeta(s) * D(s), D = 1 + a 2^{-s/2} + sqrt2 2^{-s}: frequencies 1 <-> 2 paired (coefficient sqrt2 = sqrt q), sqrt2 self-paired (free a),
so D(1-s) = 2^{s-1/2} D(s) for every real a (checked numerically below). Integers: N ∪ sqrt2·N (two radical classes, not u.d.).
dN >= 0 <=> a >= 0.  Pi >= 0 on the monoid <sqrt2> <=> log h >= 0 coefficientwise, h = D/(1 - 2^{-s}) = (1 + a u + sqrt2 u^2)/(1 - u^2),
u = 2^{-s/2}.  Certificate: for every a >= 0 some coefficient of log h is negative (interval arithmetic, as in v2).
Also: the Beurling-but-not-FE neighbour zeta(s)(1 + b 2^{-s/2}) is Beurling iff 0 <= b <= 1 (P = primes minus {2} plus {sqrt2}
at b = 1), while its FE at conductor sqrt2 needs b = 2^{1/4} > 1 (NOTE §2.3 coverage).
"""
import mpmath as mp, sympy as sp
import importlib.util, os
spec = importlib.util.spec_from_file_location("v2", os.path.join(os.path.dirname(os.path.abspath(__file__)), "v2_euler_identity_and_ud_family.py"))
v2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(v2)
mp.mp.dps = 40
a = sp.Symbol('a', real=True)
K = 16
l = v2.log_coeffs_1var([1, a, sp.sqrt(2)], K)
polys = []
for k in range(1, K+1):
    extra = sp.Rational(2, k) if k % 2 == 0 else 0   # -log(1-u^2) = sum_j u^{2j}/j  -> coefficient at u^k (k=2j) is 1/j = 2/k
    polys.append((f"u^{k} (freq 2^({k}/2))", sp.expand(l[k] + extra)))
print("FE check D(1-s) = 2^{s-1/2} D(s) at a = 0.7, s = 0.3+2.1i:",
      mp.nstr(abs((lambda s: 1 + 0.7*2**(-s/2) + mp.sqrt(2)*2**(-s))(1 - mp.mpc(0.3, 2.1)) - 2**(mp.mpc(0.3, 2.1) - 0.5)*(1 + 0.7*2**(-mp.mpc(0.3, 2.1)/2) + mp.sqrt(2)*2**(-mp.mpc(0.3, 2.1)))), 5))
E0 = mp.sqrt(2 + 2*mp.sqrt(2)) + mp.mpf('0.01')
print("coefficient u^2 =", polys[1][1], "< 0 for a >", mp.nstr(E0, 8), "(decreasing in a >= 0)")
cover, fails = v2.certify(polys, a, 0, E0)
print(f"[0, {mp.nstr(E0,6)}] covered: {len(cover)} pieces, failures {len(fails)}")
for lo, hi, lab in v2.summarize(cover):
    print(f"   a in [{mp.nstr(lo,8)}, {mp.nstr(hi,8)}]: negative coefficient {lab}")
b = sp.Symbol('b', real=True)
lb = v2.log_coeffs_1var([1, b], 12)
cb = [sp.expand(lb[k] + (sp.Rational(2, k) if k % 2 == 0 else 0)) for k in range(1, 13)]
for bv in (sp.Rational(1, 2), 1, sp.Rational(2)**sp.Rational(1, 4)):
    vals = [float(c.subs(b, bv)) for c in cb]
    print(f"zeta(1 + b 2^(-s/2)), b = {bv}: Pi(2^(k/2)) k=1..12 min = {min(vals):.4f}; first negative k = {next((k+1 for k, v in enumerate(vals) if v < -1e-15), None)}")
