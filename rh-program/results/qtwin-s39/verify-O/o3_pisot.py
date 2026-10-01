# o3 (reader's own code): Pisot model-set measure mu_k = sum_{x in Z[phi]} k(x^s/c) delta_{x/c}, c = 5^{1/4}, k = exp(-pi t^2).
# (1) self-duality test <mu,g_y> = <mu,ghat_y> (Gaussians); (2) first points of Z_j; (3) unit-orbit Pi(phi^2) for j = 1..3.
from mpmath import mp, mpf, sqrt, exp, pi, log
mp.dps = 50
phi = (1 + sqrt(5)) / 2; phs = (1 - sqrt(5)) / 2; c = mpf(5) ** (mpf(1) / 4)
def pair(y, N=45):
    S = mpf(0)
    for a in range(-N, N + 1):
        for b in range(-N, N + 1):
            x = a + b * phi; xs = a + b * phs
            e = pi * ((xs / c) ** 2 + (x / c) ** 2 / y)
            if e < 160: S += exp(-e)
    return S
for y in [mpf('0.37'), mpf(1), mpf('2.2')]:
    l = pair(y); r = sqrt(y) * pair(1 / y)
    print("theta pairing y=%s: <mu,g>=%s <mu,ghat>=%s |diff|=%s" % (y, mp.nstr(l, 20), mp.nstr(r, 20), mp.nstr(abs(l - r), 3)))
# (2) Z_j = { n^s phi^j / c : n in O_K, 0 < |n| < 1 }: smallest |values|
pts = set()
for a in range(-60, 61):
    for b in range(-60, 61):
        n = a + b * phi
        if 0 < abs(n) < 1: pts.add(round(float(abs(a + b * phs)), 10))
srt = sorted(pts)[:4]
for j in range(0, 2):
    print("Z_%d first |points|:" % j, [round(v * float(phi) ** j / float(c), 4) for v in srt])
# (3) unit orbit, k Gaussian, normalized c(1) = 1: c(phi^m) = k(phi^{j-m}/c)/k(phi^j/c); Pi(phi^2) = c(phi^2) - c(phi)^2/2
for j in range(0, 4):
    K = lambda t: exp(-pi * t * t)
    cm = lambda m: K(phi ** (j - m) / c) / K(phi ** j / c)
    print("j=%d q=sqrt5*phi^(2j)=%s  Pi(phi^2) = %s   [criterion exp(pi phi^(2j-2)/sqrt5) = %s vs 2]" % (
        j, mp.nstr(sqrt(5) * phi ** (2 * j), 5), mp.nstr(cm(2) - cm(1) ** 2 / 2, 5), mp.nstr(exp(pi * phi ** (2 * j - 2) / sqrt(5)), 5)))
