#!/usr/bin/env python3
"""read-O checks of the zeta inputs of T2 (NOTE ll. 149-162), own code.
(1) argument principle: number of zeros of zeta in the box -0.5<=sigma<=1.5, 0.5<=t<=T for T = 14.0 and 14.3 (box avoids the
    pole and the trivial zeros); (2) rho_1 and zeta'(rho_1); (3) |zeta(rho_1/k)|, k=2..5;
(4) C(rho_1/2) = prod_p (1 - r_p^{-s})/(1 - p^{-2s}) at s = rho_1/2 for r_p = nextprime(p^2), p <= P, P = 1e5 and 1e6
    (own nextprime: deterministic Miller-Rabin for n < 3.3e24)."""
import mpmath as mp, sys
mp.mp.dps = 30

def count_zeros(T):
    f = lambda s: mp.zeta(s, derivative=1) / mp.zeta(s)
    a, b, c, d = mp.mpf(-0.5), mp.mpf(1.5), mp.mpf(0.5), mp.mpf(T)
    I = (mp.quad(lambda x: f(mp.mpc(x, c)), [a, 0, 0.5, 1, b])
         + mp.quad(lambda y: f(mp.mpc(b, y)) * 1j, [c, d])
         - mp.quad(lambda x: f(mp.mpc(x, d)), [a, 0, 0.5, 1, b])
         - mp.quad(lambda y: f(mp.mpc(a, y)) * 1j, [c, d]))
    return I / (2j * mp.pi)

def is_prime(n):
    if n < 2: return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41)
    for p in small:
        if n % p == 0: return n == p
    d, s = n - 1, 0
    while d % 2 == 0: d //= 2; s += 1
    for a in small:
        x = pow(a, d, n)
        if x in (1, n - 1): continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1: break
        else: return False
    return True

def nextprime(n):           # least prime > n  (p^2 itself is never prime)
    m = n + 1
    while not is_prime(m): m += 1
    return m

def primes_upto(P):
    s = bytearray([1]) * (P + 1); s[0:2] = b'\x00\x00'
    for i in range(2, int(P ** 0.5) + 1):
        if s[i]: s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(P + 1) if s[i]]

if __name__ == '__main__':
    for T in (14.0, 14.3):
        print(f"zeros in [-0.5,1.5]x[0.5,{T}] by argument principle: {mp.nstr(count_zeros(T), 8)}")
    r1 = mp.zetazero(1)
    print("rho_1 =", r1, " zeta'(rho_1) =", mp.nstr(mp.zeta(r1, derivative=1), 12))
    for k in range(2, 6):
        print(f"k={k}: |zeta(rho_1/k)| = {mp.nstr(abs(mp.zeta(r1 / k)), 8)}")
    s0 = r1 / 2
    for P in (10 ** 5, 10 ** 6):
        logC = mp.mpc(0); maxgap = 0
        for p in primes_upto(P):
            r = nextprime(p * p); maxgap = max(maxgap, r - p * p)
            logC += mp.log(1 - mp.power(r, -s0)) - mp.log(1 - mp.power(p, -2 * s0))
        print(f"P={P}: C(rho_1/2) = {mp.nstr(mp.e ** logC, 10)}  (max nextprime(p^2)-p^2 = {maxgap})")
        sys.stdout.flush()
