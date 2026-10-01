# o2 (reader's own code): positive self-dual finite comb WITH an irrational frequency -- control for G1 Step 3.
# mu_c = sum_n (c + 2cos(2 pi theta n)) delta_n + delta_{theta+Z} + delta_{-theta+Z}.
# Self-duality test: <mu, g_y> = <mu, ghat_y> for g_y(x) = exp(-pi x^2 / y), ghat_y(xi) = sqrt(y) exp(-pi y xi^2).
from mpmath import mp, mpf, exp, cos, pi, sqrt, nsum, inf
mp.dps = 60
def pair(theta, c, y):
    a = nsum(lambda n: (c + 2*cos(2*pi*theta*n))*exp(-pi*n**2/y), [-inf, inf])
    b = nsum(lambda m: exp(-pi*(m+theta)**2/y) + exp(-pi*(m-theta)**2/y), [-inf, inf])
    return a + b
theta = sqrt(2) - 1          # irrational, frac = 0.4142 in [r, 1-r] for r = 1/2 (q = 4) and r = 1/3 (q = 9)
c = mpf(2)
for y in [mpf('0.37'), mpf(1), mpf('2.2'), mpf('5.1')]:
    lhs = pair(theta, c, y); rhs = sqrt(y)*pair(theta, c, 1/y)
    print("y=%s  <mu,g>=%s  <mu,ghat>=%s  diff=%s" % (mp.nstr(y,4), mp.nstr(lhs,25), mp.nstr(rhs,25), mp.nstr(abs(lhs-rhs),3)))
# positivity and gap: masses c + 2cos(.) >= 0; atoms of theta+Z nearest 0 are theta = 0.4142 and theta - 1 = -0.5858
print("min mass on Z (n<=10^5 sample):", min(float(c + 2*cos(2*pi*theta*n)) for n in range(1, 100001)))
print("nearest atoms of +-theta+Z to 0:", float(theta), float(1-theta), "(gap (-r,r) holds for r <= 0.4142, i.e. q >= 5.83)")
# monoid test (G1 Step 0/1): support of nu = mu_c on (0,inf) scaled by sqrt(q): 1 must be an atom and the support a monoid.
print("support meets each Q-line {beta Q} in at most one point of theta+Z: (theta+m)-(theta+m') in Z, so two points in beta*Q")
print("force beta*Q = Q and theta in Q -- impossible; so supp is in no finite union of Q-lines: not Beurling (G1 Step 1).")
