# verify-O 2.3: 2*sum_{gamma>0} gamma^-2 (NOTE l. 41, "0.0462..."), assuming the zeros used are on the line.
# Route: unconditional identity sum_rho 1/(rho(1-rho)) = 2 + gamma_E - log(4 pi); on the line rho(1-rho) = 1/4 + gamma^2,
# so sum_{gamma>0} 1/(1/4+gamma^2) = (2 + gamma_E - log 4pi)/2; then add sum (1/gamma^2 - 1/(1/4+gamma^2)) over 300 zeros
# plus a tail bound  sum_{gamma>T} 1/(4 gamma^4) <= int_T^inf (log(t/2pi)/(2pi)) /(4 t^4) dt + O(log T / T^4).
from core import *
mp.mp.dps = 25
A = (2 + mp.euler - mp.log(4*PI))/2
corr = mp.mpf(0); M = 300
for n in range(1, M+1):
    g = mp.zetazero(n).imag
    corr += 1/g**2 - 1/(mp.mpf(1)/4 + g**2)
T = mp.zetazero(M).imag
tail = mp.quad(lambda t: mp.log(t/(2*PI))/(2*PI)/(4*t**4), [T, mp.inf])
S = A + corr + tail
print("sum 1/(1/4+g^2) =", mp.nstr(A, 15), " correction(300 zeros) =", mp.nstr(corr, 12), " tail ~", mp.nstr(tail, 3))
print("sum_{g>0} g^-2 =", mp.nstr(S, 12), "   2*sum =", mp.nstr(2*S, 12))
