# read-O (U1-lookahead), own code. Lambda_{rho,tau}(sigma) of NOTE Thm 4.1, written from the definition:
#   Lambda = 1 - tau - rho/(1-sigma) + sigma * Int_1^inf (k(u) - rho(u-1) + tau)^+ u^{-sigma-1} du,
#   k(u) = floor(log u / log p*), p* = 1 + tau/rho.
# Method A (rigorous): python-flint arb balls; piece k lives on [p*^k, min(p*^{k+1}, c_k)], c_k = 1 + (k+tau)/rho,
#   integrand (k + tau + rho - rho u) u^{-sigma-1}; every comparison is decided on balls (abort if undecidable).
# Method B (independent of the closed form): mpmath.quad on each piece, 30 digits.
import sys
from flint import arb, ctx
import mpmath as mp

ctx.prec = 256

def rho_of(name):
    tab = {"pi/32": arb.pi()/32, "pi/16": arb.pi()/16, "pi/8": arb.pi()/8, "pi/4": arb.pi()/4,
           "0.95pi/3": arb.pi()*arb(95)/arb(300), "1": arb(1)}
    return tab[name]

def lt(x, y):   # decided strict comparison of balls
    if x < y: return True
    if x >= y: return False
    raise RuntimeError("undecidable comparison")

def pieces(rho, tau):
    ps = 1 + tau/rho
    out = []; k = 0; a = arb(1)
    while True:
        ck = 1 + (k + tau)/rho
        nxt = a*ps
        if k == 0:                      # p*^1 = c_0 = 1 + tau/rho exactly
            out.append((0, arb(1), ps))
        elif lt(a, ck):
            b = nxt if lt(nxt, ck) else ck
            out.append((k, a, b))
        # stop when piece empty AND (p*-1)(k+rho+tau) >= 1 (then all later pieces are empty)
        elif not lt((ps - 1)*(k + rho + tau), arb(1)):
            break
        k += 1; a = nxt
        if k > 10**6: raise RuntimeError("too many pieces")
    return out

def Lam_arb(rho, tau, s, pcs=None):
    if pcs is None: pcs = pieces(rho, tau)
    tot = 1 - tau - rho/(1 - s)
    for (k, a, b) in pcs:
        A = k + tau + rho
        tot += A*(a**(-s) - b**(-s)) - (rho*s/(1 - s))*(b**(1 - s) - a**(1 - s))
    return tot

def Lam_quad(rho_f, tau_f, s, pcs):
    mp.mp.dps = 30
    tot = 1 - tau_f - rho_f/(1 - s)
    for (k, a, b) in pcs:
        af = mp.mpf(a.mid().str(40, radius=False)); bf = mp.mpf(b.mid().str(40, radius=False))
        f = lambda u: (k + tau_f + rho_f - rho_f*u) * u**(-s - 1)
        tot += s*mp.quad(f, [af, bf])
    return tot

if __name__ == "__main__":
    pass
