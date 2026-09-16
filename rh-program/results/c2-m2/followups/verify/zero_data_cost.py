# zero_data_cost.py -- PRICING sanity computation (Session 22/23, C2 M2 follow-ups; <= 10 min).
# Decides prices in PRICING.md §2 and §3: (a) mpmath.zetazero cost at heights 1e3..1e6; (b) zero counts a window
# R = 81 L* needs (RvM count); (c) the truncation radius U that the clause-4 polynomial tail bound licenses;
# (d) the density-model in-window noise log(t/2pi)*||B'||_2^2/L^3; (e) the balance bandwidth L_bal(delta,t)
# against that noise (kappa = 1 and 3) and against the clause-4 BOUND b1 log(3+t)/L^2; (f) the theorem's L*
# and the transcript's L*_ann; (g) prime-side term count exp(L) at L_bal. Nothing here is a proof; every
# number is labeled computed. B, c(lambda), ||B'||_2^2 by mpmath quadrature (same normalization as ../..//verify/).
import mpmath as mp, time, json, signal, math
mp.mp.dps = 20
out = {}
def Braw(v):
    v = mp.mpf(v)
    return mp.exp(-1/(1-4*v*v)) if abs(v) < mp.mpf(1)/2 else mp.mpf(0)
Z = mp.quad(Braw, [-0.5, 0, 0.5])
def B(v): return Braw(v)/Z
def c(lam):  # edge function c(lambda) = int B(v) cosh(lambda v) dv
    return mp.quad(lambda v: B(v)*mp.cosh(lam*v), [-0.5, 0, 0.5])
def Bprime(v):
    v = mp.mpf(v)
    if abs(v) >= mp.mpf(1)/2: return mp.mpf(0)
    return B(v)*(-8*v/(1-4*v*v)**2)
Bp2 = mp.quad(lambda v: Bprime(v)**2, [-0.5, -0.25, 0, 0.25, 0.5])
b1 = 8.70; normB3 = 642.3011963065986; R0 = 81.0
print("Z = %s   ||B'||_2^2 = %s   (b1 = 8.70 record; ||B'''||_1 = 642.30 record)" % (mp.nstr(Z,12), mp.nstr(Bp2,10)))
out['Z'] = float(Z); out['normBprime_L2sq'] = float(Bp2)

def N_rvm(T):  # Riemann-von Mangoldt main term (computed, the O(log T) error ignored -- counts only)
    T = mp.mpf(T); return float((T/(2*mp.pi))*mp.log(T/(2*mp.pi*mp.e)) + mp.mpf(7)/8)
def Lstar(delta, t, C1):
    return max(25.0/delta, 4.0/delta*(math.log(math.log(3+t)) + 2*math.log(1/delta) + math.log(2*b1*C1)))
def Lann(delta, t):  # transcript's annealed fit, C2 line 54 / PRICING-BRIEF §2(a)
    return 1.12*delta**(-0.07)*(math.log(t/(2*math.pi)))**0.89

# (a) zetazero timing, one call per height, 150 s alarm each
print("\n(a) mpmath.zetazero timing (mp.dps=15), one zero near each height")
class TO(Exception): pass
def handler(s, f): raise TO()
signal.signal(signal.SIGALRM, handler)
timing = {}
mp.mp.dps = 15
for t in [1e3, 1e4, 1e5, 1e6]:
    n = int(round(N_rvm(t)))
    signal.alarm(150)
    try:
        t0 = time.time(); z = mp.zetazero(n); dt = time.time()-t0
        signal.alarm(0)
        print("   t~%.0e: index n=%d  zetazero(n) = %s  in %.2f s" % (t, n, mp.nstr(z, 12), dt))
        timing[str(int(t))] = {'n': n, 'gamma': float(mp.im(z)), 'seconds': dt}
    except TO:
        print("   t~%.0e: index n=%d  zetazero(n) TIMED OUT at 150 s" % (t, n)); timing[str(int(t))] = {'n': n, 'seconds': None}
mp.mp.dps = 20
out['zetazero_timing'] = timing

# (b) zero counts in the window |gamma - t| <= R = 81 L*
print("\n(b) zeros in the theorem's window R = 81 L* (RvM count N(t+R)-N(t-R)); C1 = 1 (abstract) and C1 = 2.4e9 (zeta's record)")
counts = {}
for t in [1e3, 1e4, 1e5, 1e6]:
    for C1, lab in [(1.0, 'C1=1'), (2.4e9, 'C1=2.4e9')]:
        for delta in [0.05, 0.1, 0.25]:
            L = Lstar(delta, t, C1); R = R0*L
            cnt = N_rvm(t+R) - N_rvm(max(t-R, 14.0))
            counts["%g,%s,%g" % (t, lab, delta)] = {'Lstar': L, 'R': R, 'zeros_in_window': cnt, 'window_below_zero': t-R < 0}
            print("   t=%.0e %s delta=%.2f: L*=%.1f R=%.0f zeros=%.3g%s" % (t, lab, delta, L, R, cnt, "  [window reaches below t=0]" if t-R<0 else ""))
out['window_counts'] = counts

# (c) truncation radius U for evaluating the on-line sum to absolute 1e-10 via the clause-4 polynomial tail:
#     tail(U) <= 2 C1 l_R ||B'''||_1^2 / L^6 * sum_{k>=U} k^-4 <= 2 C1 l_R ||B'''||_1^2 / (3 L^6 (U-1)^3), C1 = 1 (RvM operative, stated)
print("\n(c) truncation radius U (C1 = 1, l_R = log(4+t+81L)) for tail <= 1e-10, and zeros within +-U")
trunc = {}
for t in [1e3, 1e6]:
    for L in [10, 20, 30, 50, 100, 403.5]:
        lR = math.log(4+t+R0*L)
        U = 1 + (2*lR*normB3**2/(3*L**6*1e-10))**(1/3)
        U = max(U, 2.0)
        cnt = N_rvm(t+U) - N_rvm(max(t-U, 14.0))
        trunc["%g,%g" % (t, L)] = {'U': U, 'zeros': cnt}
        print("   t=%.0e L=%g: U=%.1f  zeros in +-U = %.0f" % (t, L, U, cnt))
out['truncation'] = trunc

# (d)-(g) noise model, balance bandwidth, prime-side cost
print("\n(d)-(g) density-model noise N ~ log(t/2pi) ||B'||_2^2 / L^3 [computed model, not a bound]; signal 2 delta^2 c(delta L)^2;")
print("        L_bal = least L (step 0.5) with signal >= kappa*noise (kappa = 1, 3); L_bnd = least L with signal >= b1 log(3+t)/L^2 (the pricing's balance);")
print("        L* = theorem (C1 = 1); L_ann = transcript fit; X = e^L_bal(kappa=3), terms ~ X, primes ~ X/log X")
bal = {}
cache = {}
def cc(lam):
    k = round(float(lam), 3)
    if k not in cache: cache[k] = c(mp.mpf(k))
    return cache[k]
for t in [1e3, 1e4, 1e5, 1e6, 1e9, 1e12]:
    lt = math.log(t/(2*math.pi))
    for delta in [0.05, 0.1, 0.25]:
        def signal_(L): return 2*delta**2*float(cc(delta*L))**2
        def noise(L): return lt*float(Bp2)/L**3
        def bound(L): return b1*math.log(3+t)/L**2
        res = {}
        for kap in [1.0, 3.0]:
            L = 4.0
            while signal_(L) < kap*noise(L) and L < 2000: L += 0.5
            res['Lbal_k%d' % int(kap)] = L
        L = 4.0
        while signal_(L) < bound(L) and L < 2000: L += 0.5
        res['L_bnd'] = L
        res['Lstar_C1_1'] = Lstar(delta, t, 1.0); res['Lstar_C1_zeta'] = Lstar(delta, t, 2.4e9); res['L_ann'] = Lann(delta, t)
        Lb = res['Lbal_k3']; X = math.exp(Lb)
        res['X_at_Lbal_k3'] = X; res['primes_at_X'] = X/Lb
        res['signal_at_Lbal_k3'] = signal_(Lb); res['noise_at_Lbal_k3'] = noise(Lb)
        res['trivial_prime_side_size'] = 2*math.exp(Lb/2)*float(Bp2)/Lb**3   # sum_{n<=X} Lambda(n) n^{-1/2} |g| <~ 2 sqrt(X) ||f||_2^2
        bal["%g,%g" % (t, delta)] = res
        print("   t=%.0e d=%.2f: L_bal(k=1)=%5.1f  L_bal(k=3)=%5.1f  L_bnd=%5.1f  L*(C1=1)=%6.1f  L*(zeta)=%6.1f  L_ann=%5.1f | at L_bal(3): X=%.2e primes~%.2e signal=%.3g noise=%.3g trivial-size=%.3g"
              % (t, delta, res['Lbal_k1'], res['Lbal_k3'], res['L_bnd'], res['Lstar_C1_1'], res['Lstar_C1_zeta'], res['L_ann'], X, X/Lb, res['signal_at_Lbal_k3'], res['noise_at_Lbal_k3'], res['trivial_prime_side_size']))
out['balance'] = bal

# (h) the bump-only crossing of clause 3: least lambda with 2 c(lambda)^2 >= e^{lambda/2} (height-independent)
lam = 10.0
while 2*float(cc(lam))**2 < math.exp(lam/2) and lam < 40: lam += 0.1
print("\n(h) bump-only crossing: least lambda (step 0.1) with 2 c(lambda)^2 >= e^(lambda/2): %.1f  (proved from 23; contract lambda0 = 25)" % lam)
out['bump_only_crossing_lambda'] = lam
# (i) DH at its own parameters: the sign channel from the on-disk rows (read, not recomputed)
try:
    d = json.load(open('../../verify/dh_negative_control_out.json'))
    rows = [(r['L'], r['W_Z'], r['W_Zprime']) for r in d['rows']]
    print("\n(i) DH control rows (read from ../../verify/dh_negative_control_out.json): L, W_Z, W_Z'")
    for r in rows[:4]: print("   L=%5.1f  W_Z=%.4g  W_Z'=%.4g  -> sign channel %s; prime-side length e^L = %.3g" % (r[0], r[1], r[2], "FIRES" if r[1] < 0 else "silent", math.exp(r[0])))
    out['dh_rows_head'] = rows[:4]
except Exception as e:
    print("   (DH json not readable: %s)" % e)
json.dump(out, open('zero_data_cost_out.json', 'w'), indent=1, default=float)
print("\ndone")
