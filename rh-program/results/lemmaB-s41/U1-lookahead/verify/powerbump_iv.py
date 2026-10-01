# U1-lookahead: interval-arithmetic proof that Lam_{rho,tau}(sigma1) > 0 (NOTE §4, Theorem 4.1 / Corollary 4.2).
# Lower bound used: on [lo_k, hi_k] with lo_k >= p1^k (rounded up) and hi_k <= min(p1^{k+1}, c_k) (rounded down), c_k = 1 + (k+tau)/rho,
# the function g_k(u) = k + tau - rho(u-1) satisfies 0 <= g_k <= (k(u) - rho(u-1) + tau)^+ ; elsewhere the integrand is replaced by 0.
# So Lam >= 1 - tau - rho/(1-sigma) + sigma * sum_k Int_{lo_k}^{hi_k} g_k(u) u^{-sigma-1} du, each integral in closed form, in iv arithmetic.
from mpmath import iv, mpf, mp
iv.dps = 50; mp.dps = 50
def lam_lower(rho, tau, sigma):
    s = iv.mpf(sigma); p1 = 1 + tau / rho; tot = iv.mpf(0); k = 0
    while True:
        pk = p1 ** k; pk1 = p1 ** (k + 1); ck = 1 + (k + tau) / rho
        lo = mpf(pk.b); hi = min(mpf(pk1.a), mpf(ck.a))
        if k > 0 and mpf(pk.a) > mpf(ck.b) and mpf(p1.a) > mpf((1 + 1 / (k + rho + tau)).b): break
        if hi > lo:
            A = k + tau + rho
            F = lambda u: -A * iv.exp(-s * iv.log(iv.mpf(u))) / s - rho * iv.exp((1 - s) * iv.log(iv.mpf(u))) / (1 - s)
            tot += F(hi) - F(lo)
        k += 1
    return 1 - tau - rho / (1 - s) + s * tot
pi_iv = iv.pi
cases = [("pi/16", pi_iv / 16, "1/2", "0.763"), ("pi/16", pi_iv / 16, "1/10", "0.911"), ("pi/16", pi_iv / 16, "1/50", "0.979"),
         ("pi/16", pi_iv / 16, "1/100", "0.989"), ("pi/32", pi_iv / 32, "1/2", "0.888"), ("pi/32", pi_iv / 32, "1/100", "0.990"),
         ("pi/8", pi_iv / 8, "1/100", "0.989"), ("pi/4", pi_iv / 4, "1/10", "0.869"), ("pi/4", pi_iv / 4, "1/100", "0.989"),
         ("0.95pi/3", iv.mpf("0.95") * pi_iv / 3, "1/100", "0.989"), ("pi/4", pi_iv / 4, "1/1000", "0.998")]
for name, rho, tau_s, s1 in cases:
    tau = iv.mpf(tau_s.split("/")[0]) / iv.mpf(tau_s.split("/")[1])
    L = lam_lower(rho, tau, mpf(s1))
    print(f"rho={name} tau={tau_s} sigma1={s1}: Lam_lower in [{mp.nstr(mpf(L.a), 8)}, {mp.nstr(mpf(L.b), 8)}]  "
          f"{'POSITIVE (proved)' if mpf(L.a) > 0 else 'not certified'}  -> U refuted by (B) with theta < {mpf(s1) / 2}")
