#!/usr/bin/env python3
"""four_point_accounting.py -- the two section-0 accounting points, by direct quadrature.
f_{t,L}(u) = i (B_L)'(u) e^{-i t u},  B_L(u) = B(u/L)/L,  h_f(z) = int f(u) e^{i z u} du  (paperFT, Zeta23/Defs.lean 44).
W_Z(f) = sum_{gamma in Z} h_f(gamma) conj(h_f(conj gamma))   (Zeta23/Defs.lean 164-170, f = g).
Checks: (1) h_f(r) = (r - t) Bhat_L(r - t) at real and complex r, by direct quadrature of f;
        (2) the four orbit points: h_f(t -+ i delta) = -+ i delta c(delta L), each of the +t pair contributes -delta^2 c^2,
            the -t pair contributes E_- (tiny), total = -2 delta^2 c^2 + E_-;
        (3) sign/normalization on a small conjugation- and reflection-invariant Z: W_Z real, on-line terms = |h_f|^2 >= 0;
        (4) the Weil-test identity paperFT(f * f~)(z) = h_f(z) conj(h_f(conj z)) at one complex z by a double quadrature
            (EF.paperFT_weilTest, ExplicitFormula.lean 189-191), and that g = f * f~ is Hermitian, not real.
Budget: < 10 min."""
import time, json, sys
import mpmath as mp
t0 = time.time(); mp.mp.dps = 20
out = {}
def Braw(v):
    v = mp.mpf(v)
    if abs(v) >= mp.mpf(1)/2: return mp.mpf(0)
    return mp.e**(-1/(1-4*v*v))
Z = mp.quad(Braw, [-0.5, -0.25, 0, 0.25, 0.5])
B = lambda v: Braw(v)/Z
def dB(v):
    v = mp.mpf(v)
    if abs(v) >= mp.mpf(1)/2: return mp.mpf(0)
    return mp.e**(-1/(1-4*v*v))*(-8*v/(1-4*v*v)**2)/Z
t = mp.mpf(30); delta = mp.mpf('0.3'); L = mp.mpf(40)
out["params"] = dict(t=30, delta=0.3, L=40)
BL = lambda u: B(u/L)/L
dBL = lambda u: dB(u/L)/L**2
f = lambda u: 1j*dBL(u)*mp.e**(-1j*t*u)
def quad_osc(fn, a, b, n=400):
    pts = [a + (b-a)*k/n for k in range(n+1)]
    return mp.quad(fn, pts)
def h_f(z):     # direct quadrature of f against e^{izu}
    z = mp.mpc(z)
    return quad_osc(lambda u: f(u)*mp.e**(1j*z*u), -L/2, L/2)
def Bhat_L(z):  # int B_L(u) e^{izu} du = Bhat(L z)
    z = mp.mpc(z)
    return quad_osc(lambda u: BL(u)*mp.e**(1j*z*u), -L/2, L/2)
def c_of(lam): return mp.quad(lambda v: B(v)*mp.cosh(lam*v), [-0.5, -0.25, 0, 0.25, 0.5])
# (1)
print("(1) h_f(r) = (r - t) Bhat_L(r - t):")
for r in (t + mp.mpf('0.7'), t - 2, mp.mpc(t, -delta), mp.mpc(-t, delta)):
    lhs = h_f(r); rhs = (r - t)*Bhat_L(r - t)
    print(f"    r = {mp.nstr(r,6)}: direct {mp.nstr(lhs,10)}   closed form {mp.nstr(rhs,10)}   |diff| = {mp.nstr(abs(lhs-rhs),3)}")
out["check1_maxdiff"] = float(max(abs(h_f(r) - (r-t)*Bhat_L(r-t)) for r in (t + mp.mpf('0.7'), mp.mpc(t, -delta))))
# (2) the four points
c = c_of(delta*L)
g1, g2, g3, g4 = mp.mpc(t, -delta), mp.mpc(t, delta), mp.mpc(-t, -delta), mp.mpc(-t, delta)
H = {name: h_f(gm) for name, gm in (("t-id", g1), ("t+id", g2), ("-t-id", g3), ("-t+id", g4))}
print(f"(2) c(delta L) = Bhat_L(i delta) = {mp.nstr(c,12)};  -i delta c = {mp.nstr(-1j*delta*c,12)}")
for name, val in H.items(): print(f"    h_f({name}) = {mp.nstr(val, 12)}")
contrib = {"t-id": H["t-id"]*mp.conj(H["t+id"]), "t+id": H["t+id"]*mp.conj(H["t-id"]), "-t-id": H["-t-id"]*mp.conj(H["-t+id"]), "-t+id": H["-t+id"]*mp.conj(H["-t-id"])}
for name, val in contrib.items(): print(f"    contribution of {name}: h_f(gamma) conj(h_f(conj gamma)) = {mp.nstr(val, 12)}")
main = contrib["t-id"] + contrib["t+id"]; Em = contrib["-t-id"] + contrib["-t+id"]
print(f"    pair at +t: {mp.nstr(main,12)}   vs  -2 delta^2 c^2 = {mp.nstr(-2*delta**2*c**2,12)}   |diff| = {mp.nstr(abs(main + 2*delta**2*c**2),3)}")
print(f"    reflected pair at -t (E_-): {mp.nstr(Em,6)};  |E_-| / (2 delta^2 c^2) = {mp.nstr(abs(Em)/(2*delta**2*c**2),4)};  e^(-L) = {mp.nstr(mp.e**(-L),4)}")
out["c_deltaL"] = float(c); out["pair_plus_t"] = [float(main.real), float(main.imag)]; out["minus_2d2c2"] = float(-2*delta**2*c**2)
out["E_minus"] = [float(Em.real), float(Em.imag)]; out["E_minus_over_main"] = float(abs(Em)/(2*delta**2*c**2))
# (3) small invariant Z: orbit + real points +-r1, +-r2
r1, r2 = t + mp.mpf('0.55'), t - mp.mpf('1.3')
Zset = [g1, g2, g3, g4, r1, -r1, r2, -r2]
terms = [h_f(gm)*mp.conj(h_f(mp.conj(gm))) for gm in Zset]
W = mp.fsum(terms)
print(f"(3) W_Z(f) over the 8-point Z = orbit + {{+-r1, +-r2}}: {mp.nstr(W,12)}  (imaginary part {mp.nstr(W.imag,3)});")
print(f"    real points: |h_f(r1)|^2 = {mp.nstr(terms[4].real,8)}, |h_f(-r1)|^2 = {mp.nstr(terms[5].real,3)}, |h_f(r2)|^2 = {mp.nstr(terms[6].real,8)}, |h_f(-r2)|^2 = {mp.nstr(terms[7].real,3)};  b1/L^2 = {8.647/1600:.6f}")
print(f"    W_Z = -2 delta^2 c^2 + E_- + sum|h_f|^2:  {mp.nstr(-2*delta**2*c**2 + Em + terms[4]+terms[5]+terms[6]+terms[7],12)}")
out["W_8point"] = [float(W.real), float(W.imag)]
# (4) Weil-test identity at one complex z, double quadrature: g(x) = int f(y) conj(f(y - x)) dy,  ghat(z) = int g(x) e^{izx} dx
z0 = mp.mpc(t + mp.mpf('0.4'), -mp.mpf('0.2'))
def gconv(x):
    x = mp.mpf(x)
    a = max(-L/2, x - L/2); b = min(L/2, x + L/2)
    if a >= b: return mp.mpc(0)
    return mp.quad(lambda y: f(y)*mp.conj(f(y - x)), [a, (a+b)/2, b])
mp.mp.dps = 12
xs = [-L + 2*L*k/160 for k in range(161)]
gv = [gconv(x) for x in xs]
herm = max(abs(gv[k] - mp.conj(gv[160-k])) for k in range(161)); realpart = max(abs(gv[k].imag) for k in range(161))
print(f"(4) g = f*f~ on a 161-point grid: max|g(-x) - conj g(x)| = {mp.nstr(herm,3)} (Hermitian), max|Im g(x)| = {mp.nstr(realpart,3)} (NOT real)")
# transform of g at z0 by trapezoid on the grid (smooth compactly supported integrand -> spectrally accurate), against h_f(z0) conj(h_f(conj z0))
gz = mp.fsum(gv[k]*mp.e**(1j*z0*xs[k]) for k in range(161))*(2*L/160)
mp.mp.dps = 20
rhs = h_f(z0)*mp.conj(h_f(mp.conj(z0)))
print(f"    ghat(z0) by grid transform = {mp.nstr(gz,8)}   h_f(z0) conj(h_f(conj z0)) = {mp.nstr(rhs,8)}   rel diff = {mp.nstr(abs(gz-rhs)/abs(rhs),3)}")
out["weil_identity_reldiff_z0"] = float(abs(gz-rhs)/abs(rhs)); out["g_hermitian_maxdev"] = float(herm); out["g_max_imag"] = float(realpart)
out["runtime_s"] = time.time() - t0
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "four_point_accounting_out.json", "w"), indent=1)
print(f"done in {time.time()-t0:.1f}s")
