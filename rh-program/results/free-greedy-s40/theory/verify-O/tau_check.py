# Opus reader: the tail factor tau_X(s) = s X^-s (L^2/s + 2L/s^2 + 2/s^3), L = log X (NOTE 4.1), and the K-thresholds
# of Theorems 4.1(ii), 4.2(ii), using F_X values from this folder's s8dd runs (s8dd_pi16_1e7.log, s8dd_pi4_1e7.log).
import mpmath as mp
mp.mp.dps = 30
def tau(X, s):
    L = mp.log(X); return s * X**(-s) * (L**2/s + 2*L/s**2 + 2/s**3)
X = mp.mpf(10)**7
# closed form check of the integral itself at one point
s0 = mp.mpf('0.8'); I = mp.quad(lambda u: mp.log(u)**2 * u**(-s0-1), [X, mp.inf]); print("integral check:", mp.nstr(s0*I, 12), mp.nstr(tau(X, s0), 12))
for name, s, F in [("pi16", '0.80', '-0.025711158284'), ("pi16", '0.81', '-0.078544745823'),
                   ("pi4", '0.55', '-0.173679388824'), ("pi4", '0.52', '-0.025933000162')]:
    s = mp.mpf(s); F = mp.mpf(F); t = tau(X, s)
    print(f"{name} sigma={s}: F_X={F}  tau={mp.nstr(t, 6)}  K_max=|F|/tau={mp.nstr(-F/t, 6)}")
print("half X^-0.79 =", mp.nstr(0.5*X**(-mp.mpf('0.79')), 6), " half X^-0.5 =", mp.nstr(0.5*X**(-mp.mpf('0.5')), 6))
print("half 1e6^-0.89 =", mp.nstr(0.5*mp.mpf(10)**(-6*mp.mpf('0.89')), 6))
print("1/2 - pi/32 =", mp.nstr(0.5 - mp.pi/32, 10), " 1/2 - pi/16 =", mp.nstr(0.5 - mp.pi/16, 10))
