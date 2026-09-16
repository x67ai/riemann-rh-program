#!/usr/bin/env python3
"""Opus dual check (Job 2) -- INDEPENDENT recomputation of every load-bearing constant of
results/c2-m2/separation-note.md.  Written from the note's TEXT, not from the author's scripts.
Deliberately different code path: closed forms + mpmath quadrature, no reuse of verify/*.py."""
import mpmath as mp, math, json
mp.mp.dps = 40
out = {}

# ---------- 0. the bump, Z, and the transform ----------
def Braw(v):
    v = mp.mpf(v)
    return mp.zero if abs(v) >= mp.mpf(1)/2 else mp.e**(-1/(1-4*v*v))
Z = mp.quad(Braw, [-mp.mpf(1)/2, 0, mp.mpf(1)/2])
print("(0) Z = %s   (note: 0.221996908084...)" % mp.nstr(Z, 15))
out["Z"] = float(Z)

def Bhat(eta):                      # real eta; B even so Bhat real
    eta = mp.mpf(eta)
    n = max(8, int(abs(eta))//2 + 8)
    pts = [-mp.mpf(1)/2 + mp.mpf(k)/n for k in range(n+1)]
    return mp.quad(lambda v: Braw(v)*mp.cos(eta*v), pts)/Z

# ---------- 1. clause 2: the edge law ----------
def c_of(lam):                      # c(lam) = int B(v) cosh(lam v) dv, via the Laplace form (3.1)
    lam = mp.mpf(lam)
    I = mp.quad(lambda s: mp.e**(-lam*s - 1/(4*s*(1-s))), [0, mp.mpf(1)/4, mp.mpf(1)/2, 1])
    return mp.e**(lam/2)*I/Z
# direct cross-check of (3.1) against the definition
for lam in (25, 60):
    direct = mp.quad(lambda v: Braw(v)*mp.cosh(mp.mpf(lam)*v), [-mp.mpf(1)/2, 0, mp.mpf(1)/2])/Z
    print("(1a) lam=%d: c direct = %s   c via (3.1) = %s   rel diff = %.2e"
          % (lam, mp.nstr(direct, 12), mp.nstr(c_of(lam), 12), float(abs(direct/c_of(lam)-1))))
kinf = mp.log(mp.sqrt(mp.pi/2)*mp.e**(-mp.mpf(1)/4)/Z)
kplus = kinf + 1/(4*mp.sqrt(mp.mpf(25))) + 1/(128*mp.mpf(25)**mp.mpf(1.5))
print("(1b) kappa_inf = log(sqrt(pi/2) e^{-1/4}/Z) = %s ;  kappa_+ = %s" % (mp.nstr(kinf, 12), mp.nstr(kplus, 12)))
out["kappa_minus"] = float(kinf); out["kappa_plus"] = float(kplus)
def kappa(lam):
    lam = mp.mpf(lam)
    return mp.log(c_of(lam)) - lam/2 + mp.sqrt(lam) + mp.mpf(0.75)*mp.log(lam)
lams = [25, 25.5, 26, 28, 30, 36, 49, 64, 81, 100, 200, 400, 1000, 2500, 10000]
bad = []
for lam in lams:
    k = kappa(lam)
    if not (kinf <= k <= kplus): bad.append((lam, float(k)))
print("(1c) kappa(lam) in [kappa_-, kappa_+] on %d values: %s ; kappa(25)=%s, kappa(1e4)=%s, violations=%s"
      % (len(lams), not bad, mp.nstr(kappa(25), 8), mp.nstr(kappa(10000), 8), bad))
# clause 3: m(lam) = lam/2 - 2 sqrt lam - 1.5 log lam + 2 kappa_inf
m25 = mp.mpf(25)/2 - 2*5 - mp.mpf(1.5)*mp.log(25) + 2*kinf
print("(1d) clause 3: m(25) = %s (>0), m'(25) = %s ; proved margin e^{m(25)} = %s vs computed c(25)^2/e^{12.5} = %s"
      % (mp.nstr(m25, 8), mp.nstr(mp.mpf(0.5)-1/mp.sqrt(mp.mpf(25))-mp.mpf(1.5)/25, 4),
         mp.nstr(mp.e**m25, 6), mp.nstr(c_of(25)**2/mp.e**mp.mpf(12.5), 6)))
out["m25"] = float(m25)

# ---------- 2. Lemma G constants ----------
A1 = 72/mp.e
cB = 2/mp.sqrt(72*mp.e); CB = mp.e**2/Z
cBp = mp.mpf(7)/8*cB; CBp = 4*mp.e**(-mp.mpf(3)/4)*CB
print("(2a) A1 = 72/e = %s ; c_B = 2/sqrt(72e) = %s ; C_B = e^2/Z = %s ; c_B' = %s ; C_B' = %s"
      % (mp.nstr(A1, 8), mp.nstr(cB, 10), mp.nstr(CB, 8), mp.nstr(cBp, 8), mp.nstr(CBp, 8)))
print("     note's D2 prints c_B = 0.14298 ; sec2/sec15 print 0.142961/0.14296 ; exact = %s" % mp.nstr(cB, 8))
out["c_B"] = float(cB); out["C_B"] = float(CB)
# the pricing's number, for the record
print("(2b) 1/(3 sqrt e) = %s  (the pricing's inferred c_B, valid for theta not for B) ; 1/(6 sqrt e) = %s (crude 2^k Leibniz)"
      % (mp.nstr(1/(3*mp.sqrt(mp.e)), 6), mp.nstr(1/(6*mp.sqrt(mp.e)), 6)))
# B_raw = theta(v+1/2)^{1/4} ?
def theta(x):
    x = mp.mpf(x)
    return mp.zero if (x <= 0 or x >= 1) else mp.e**(-1/(x*(1-x)))
d = max(abs(Braw(mp.mpf(k)/100) - theta(mp.mpf(k)/100 + mp.mpf(1)/2)**(mp.mpf(1)/4)) for k in range(-49, 50))
print("(2c) max |B_raw(v) - theta(v+1/2)^{1/4}| on a grid = %.3e   (contract's B IS theta^{1/4})" % float(d))
# Leibniz step (iii): C(k,i) i^i (k-i)^{k-i} <= k^k, and term_i <= k^{2k}
ok = all(mp.binomial(k, i)*mp.mpf(i)**i*mp.mpf(k-i)**(k-i) <= mp.mpf(k)**k*(1+mp.mpf(10)**-30)
         for k in range(1, 40) for i in range(0, k+1))
print("(2d) C(k,i) i^i (k-i)^{k-i} <= k^k for 1<=k<=39, all i: %s" % ok)
# Lemma G1 numerically
worst = 0
for k in range(1, 7):
    r = max(abs(mp.diff(Braw, mp.mpf(x)/100, k))/((k+1)*A1**k*mp.mpf(k)**(2*k)) for x in range(-48, 49, 3))
    worst = max(worst, float(r))
print("(2e) max ratio |B_raw^{(k)}|/((k+1) A1^k k^{2k}) over k<=6 = %.4f  (<=1 required)" % worst)
def G(eta):
    eta = mp.mpf(eta)
    return CB*(1 + cB/2*mp.sqrt(eta))*mp.e**(-cB*mp.sqrt(eta))
mn = min(float(G(e)/abs(Bhat(e))) for e in (0, 1, 4, 16, 64, 256, 1024, 4096, 16384))
print("(2f) min G1(eta)/|Bhat(eta)| over the grid = %.4g  (>=1 required)" % mn)

# ---------- 3. clause 5: R0, independent implementation ----------
a = 2*cB
def Gam(n, s0):          # e^{a s0} * int_{s0}^inf s^n e^{-a s} ds
    return mp.fsum(mp.factorial(n)/mp.factorial(j)*s0**j/a**(n+1-j) for j in range(n+1))
def Pm(m, L, R0, L0):    # the polynomial factor of Sigma_m after the relaxations, divided by e^{-2 c_B sqrt(R0) L}
    L = mp.mpf(L); R0 = mp.mpf(R0); s0 = mp.sqrt(R0)*L; u0 = R0*L
    beta = 1 + 3/(2*(R0*mp.mpf(L0) - 1))
    head = u0**m*(1 + cB/2*s0)**2
    tail = (2/L**(m+1))*(Gam(2*m+1, s0) + cB*Gam(2*m+2, s0) + cB**2/4*Gam(2*m+3, s0))
    return beta**m*CB**2*(head + tail)
def Ft(L, R0, L0, b1, budget=mp.mpf(7)/4):
    L = mp.mpf(L); R0 = mp.mpf(R0)
    P = mp.mpf('1.05')*Pm(2, L, R0, L0) + Pm(3, L, R0, L0)
    return (budget - 2*cB*mp.sqrt(R0))*L + 2*cB/mp.sqrt(R0) + mp.log(P/b1)
b1cert = mp.mpf('8.6981')
print("(3a) F~(50) at R0=81, b1=8.6981: %s ;  at R0=80.5: %s ;  at R0=80: %s"
      % (mp.nstr(Ft(50, 81, 50, b1cert), 6), mp.nstr(Ft(50, 80.5, 50, b1cert), 6), mp.nstr(Ft(50, 80, 50, b1cert), 6)))
print("(3b) F~(50) at R0=81 with b1 = 8.64613 (the note's headline b1): %s" % mp.nstr(Ft(50, 81, 50, mp.mpf('8.64613')), 6))
print("(3c) decrease threshold 5/(2 c_B sqrt R0 - 7/4) at R0=81: %s ; F~ at L=60,100,403,1000,1e4: %s"
      % (mp.nstr(5/(2*cB*mp.sqrt(mp.mpf(81)) - mp.mpf(7)/4), 5),
         [mp.nstr(Ft(L, 81, 50, b1cert), 5) for L in (60, 100, 403, 1000, 10000)]))
print("(3d) asymptotes: (3/(4 c_B))^2 = %s ; (7/(8 c_B))^2 = %s ; (13/(16 c_B))^2 = %s (combined absorption, see check)"
      % (mp.nstr((3/(4*cB))**2, 6), mp.nstr((7/(8*cB))**2, 6), mp.nstr((13/(16*cB))**2, 6)))
# least R0 at L0 = 50 by bisection on the half-integer grid, my own search
R = mp.mpf(1)
while True:
    if Ft(50, R, 50, b1cert) <= 0 and 2*cB*mp.sqrt(R) > mp.mpf(7)/4 and 5/(2*cB*mp.sqrt(R)-mp.mpf(7)/4) <= 50: break
    R += mp.mpf('0.5')
print("(3e) my least R0 (step 1/2, L0=50) = %s" % mp.nstr(R, 5))
out["R0_mine"] = float(R)
# the sharper budget 13/8 available from the SAME hypothesis (one combined absorption)
R2 = mp.mpf(1)
while True:
    if Ft(50, R2, 50, b1cert, budget=mp.mpf(13)/8) <= 0 and 2*cB*mp.sqrt(R2) > mp.mpf(13)/8 and 5/(2*cB*mp.sqrt(R2)-mp.mpf(13)/8) <= 50: break
    R2 += mp.mpf('0.5')
print("(3f) least R0 with the combined absorption (budget 13/8 instead of 7/4) = %s" % mp.nstr(R2, 5))
out["R0_sharper"] = float(R2)

# ---------- 4. clause 1: the reflection condition ----------
kminus = kinf
def margin(t, L):
    t = mp.mpf(t); L = mp.mpf(L); s = mp.sqrt(2*t*L)
    lhs = 2*cB*s - 2*mp.log(1 + cB/2*s)
    rhs = L + mp.sqrt(2*L) + mp.mpf(1.5)*mp.log(L/2) - 2*kminus + mp.log((4*t*t + mp.mpf(1)/4)*CB**2*L**2/625)
    return lhs - rhs
print("(4a) (R') margin at t = 21L: L=50: %s ; L=100: %s ; L=1000: %s ; L=1e5: %s"
      % tuple(mp.nstr(margin(21*L, L), 5) for L in (50, 100, 1000, 100000)))
print("(4b) (R') margin at t = 20L, L=50: %s ;  at t=3, L=50: %s ;  asymptote 1/(8 c_B^2) = %s"
      % (mp.nstr(margin(20*50, 50), 5), mp.nstr(margin(3, 50), 5), mp.nstr(1/(8*cB**2), 6)))
# is the condition vacuous for t>=3 under the NUMERICAL rate 0.85?  same chain with c_B -> 0.85
def margin_num(t, L, c):
    t = mp.mpf(t); L = mp.mpf(L); s = mp.sqrt(2*t*L); C = CB
    return 2*c*s - 2*mp.log(1 + c/2*s) - (L + mp.sqrt(2*L) + mp.mpf(1.5)*mp.log(L/2) - 2*kminus + mp.log((4*t*t+mp.mpf(1)/4)*C**2*L**2/625))
for L in (50, 87, 100):
    tmin = mp.mpf(3)
    while margin_num(tmin, L, mp.mpf('0.85')) < 0 and tmin < 10**6: tmin *= mp.mpf('1.02')
    print("(4c) with rate 0.85: least admissible t at L=%s is %s  (t/L = %s)  -- 'vacuous for t>=3'?"
          % (L, mp.nstr(tmin, 5), mp.nstr(tmin/L, 4)))

# ---------- 5. b1 and the L1 norms, independent ----------
f = lambda e: -abs(mp.mpf(e)*Bhat(e))
best = None
for e in [mp.mpf(k)/20 for k in range(1, 400)]:
    v = abs(e*Bhat(e))
    if best is None or v > best[1]: best = (e, v)
e0 = mp.findroot(lambda e: mp.diff(lambda x: x*Bhat(x), e), best[0])
b1mine = (e0*Bhat(e0))**2
print("(5a) b1 = sup|eta Bhat|^2 = %s at eta* = %s   (note: 8.64613 at 4.6727)" % (mp.nstr(b1mine, 8), mp.nstr(e0, 6)))
out["b1_mine"] = float(b1mine); out["eta_star"] = float(e0)
def dn(n, v): return mp.diff(Braw, v, n)/Z
nrm1 = mp.quad(lambda v: abs(dn(1, v)), [-mp.mpf(0.4999), 0, mp.mpf(0.4999)])
print("(5b) ||B'||_1 ~ %s  => b1 <= ||B'||_1^2 = %s  (fully proved bound on the sup)"
      % (mp.nstr(nrm1, 8), mp.nstr(nrm1**2, 8)))
zeta4 = mp.zeta(4); B3 = mp.mpf('642.301')
print("(5c) L1 = (2 zeta(4) ||B'''||_1^2 / b1)^{1/4} = %s  (with ||B'''||_1 = 642.301, b1 = 8.64613)"
      % mp.nstr((2*zeta4*B3**2/mp.mpf('8.64613'))**(mp.mpf(1)/4), 5))

# ---------- 6. the four-point accounting, independent quadrature ----------
t, dl, L = mp.mpf(30), mp.mpf('0.3'), mp.mpf(40)
def hf(r):                      # h_f(r) = int i (B_L)'(u) e^{-i t u} e^{i r u} du, by direct quadrature
    r = mp.mpc(r)
    dB = lambda u: mp.diff(lambda x: Braw(x/L)/(Z*L), u)
    g = lambda u: mp.j*dB(u)*mp.e**(-mp.j*t*u)*mp.e**(mp.j*r*u)
    pts = [-L/2 + L*mp.mpf(k)/40 for k in range(41)]
    return mp.quad(g, pts)
cl = c_of(dl*L)
q1 = hf(t - mp.j*dl); q2 = hf(t + mp.j*dl)
print("(6a) h_f(t-i d) = %s  vs  -i d c(dL) = %s" % (mp.nstr(q1, 8), mp.nstr(-mp.j*dl*cl, 8)))
print("(6b) h_f(t+i d) = %s  vs  +i d c(dL) = %s" % (mp.nstr(q2, 8), mp.nstr(mp.j*dl*cl, 8)))
term1 = q1*mp.conj(q2); term2 = q2*mp.conj(q1)
print("(6c) the +t PAIR contributes %s ; -2 d^2 c^2 = %s ; rel err %.2e"
      % (mp.nstr(term1+term2, 10), mp.nstr(-2*dl**2*cl**2, 10), float(abs((term1+term2)/(-2*dl**2*cl**2)-1))))
r1 = hf(-t - mp.j*dl); r2 = hf(-t + mp.j*dl)
Em = r1*mp.conj(r2) + r2*mp.conj(r1)
print("(6d) the -t pair contributes E_- = %s ; |E_-|/(2 d^2 c^2) = %.3e ; e^{-L} = %.3e"
      % (mp.nstr(Em, 6), float(abs(Em)/float(2*dl**2*cl**2)), float(mp.e**-L)))
# clause 7: the on-line DOUBLE at -t
hmt = hf(-t)
print("(6e) clause 7: h_f(t) = %s (=0) ; double at -t contributes mult*|h_f(-t)|^2 = 2*%s = %s ;"
      " note's '2*2|h_f(-t)|^2 = 16 t^2 Bhat(2tL)^2' = %s  (a factor 2 too large)"
      % (mp.nstr(hf(t), 6), mp.nstr(abs(hmt)**2, 6), mp.nstr(2*abs(hmt)**2, 6), mp.nstr(16*t**2*Bhat(2*t*L)**2, 6)))
print("(6f) 8 t^2 Bhat(2tL)^2 = %s  (the correct value of 2*|h_f(-t)|^2)" % mp.nstr(8*t**2*Bhat(2*t*L)**2, 6))

json.dump(out, open("opus_independent_out.json", "w"), indent=1)
print("DONE")
