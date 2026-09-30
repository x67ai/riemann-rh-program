# Opus reader: R10's number. Gauss and Jacobi sums over F_5 (generator 2 of F_5^*), and E0's Frobenius 2+i vs Jacobi sums.
import cmath
p, gen = 5, 2
log = {pow(gen, k, p): k for k in range(p - 1)}
chi = lambda j: (lambda x: 0 if x % p == 0 else cmath.exp(2j * cmath.pi * j * log[x % p] / (p - 1)))
psi = lambda x: cmath.exp(2j * cmath.pi * x / p)
for j in (1, 2, 3):
    g = sum(chi(j)(x) * psi(x) for x in range(p)); print(f'order {(p-1)//__import__("math").gcd(j, p-1)} char j={j}: |g|^2 = {abs(g)**2:.12f}')
J = {}
for a in (1, 2, 3):
    for b in (1, 2, 3):
        if (a + b) % 4:
            s = sum(chi(a)(x) * chi(b)(1 - x) for x in range(p)); J[(a, b)] = complex(round(s.real, 9), round(s.imag, 9))
print('Jacobi sums J(chi^a, chi^b), a+b != 0 mod 4:', sorted(set(J.values()), key=lambda z: (z.real, z.imag)))
units = (1, -1, 1j, -1j)
print('2+i is a unit multiple of some Jacobi sum:', any(abs(u * z - (2 + 1j)) < 1e-9 for z in J.values() for u in units))
