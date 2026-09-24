# Scout F (Fable 5.1), PAIR 2 W1-26, Session 24 item 2.  OWN enumeration of genus-2 curves over F_p, p in {3,5,7}.
# Model: y^2 = f(x), f squarefree, deg f in {5,6}.  deg 5: f monic (a nonsquare leading coefficient is absorbed by
# x -> d x, y -> d^3 y).  deg 6: leading coefficient in {1, n} with n a fixed nonresidue (the two twist classes of the
# points at infinity: 1 + chi(lead) points over F_p; 2 points over F_{p^2} since every element of F_p is a square there).
# Point counts N_1 (over F_p), N_2 (over F_{p^2}) on the smooth projective model.  Weil polynomial of the Jacobian:
#   P(T) = 1 + a1 T + a2 T^2 + q a1 T^3 + q^2 T^4,  N_n = q^n + 1 - sum_j alpha_j^n,
#   a1 = -sum alpha_j = N_1 - q - 1,  a2 = sum_{i<j} alpha_i alpha_j = (a1^2 - sum alpha_j^2)/2 = (a1^2 + N_2 - q^2 - 1)/2.
# Weil RH check: all four roots of P have |T| = q^{-1/2} (numpy roots, tolerance 1e-6 as in the pricing's caveat on double roots).
# Output: g2_classes.json (list of distinct (p, a1, a2) with one example curve each and the counts) and stdout log.
import itertools, json, sys, time
import numpy as np
t0 = time.time()

def nonresidue(p):
    return next(a for a in range(2, p) if pow(a, (p - 1) // 2, p) == p - 1)

def count_points(f, p, ext):
    """#points of y^2 = f(x) on the smooth projective model over F_{p^ext}, ext in {1,2}. f = [c0, c1, ..., cd]."""
    d = len(f) - 1
    if ext == 1:
        chi = lambda v: 0 if v % p == 0 else (1 if pow(v, (p - 1) // 2, p) == 1 else -1)
        n = 0
        for x in range(p):
            v = 0
            for c in reversed(f):
                v = (v * x + c) % p
            n += 1 + chi(v)
        lead = f[-1] % p
        n += 1 if d == 5 else 1 + chi(lead)
        return n
    # F_{p^2} = F_p[t]/(t^2 - nr)
    nr = nonresidue(p)
    def mul(a, b):
        return ((a[0] * b[0] + nr * a[1] * b[1]) % p, (a[0] * b[1] + a[1] * b[0]) % p)
    def powe(a, e):
        r = (1, 0)
        while e:
            if e & 1: r = mul(r, a)
            a = mul(a, a); e >>= 1
        return r
    q2 = p * p
    def chi2(v):
        if v == (0, 0): return 0
        return 1 if powe(v, (q2 - 1) // 2) == (1, 0) else -1
    n = 0
    for x in [(a, b) for a in range(p) for b in range(p)]:
        v = (0, 0)
        for c in reversed(f):
            v = mul(v, x); v = ((v[0] + c) % p, v[1])
        n += 1 + chi2(v)
    n += 1 if d == 5 else 2   # deg 6: leading coefficient in F_p is a square in F_{p^2}
    return n

def squarefree(f, p):
    """gcd(f, f') = 1 over F_p (Euclid)."""
    def trim(a):
        a = [x % p for x in a]
        while a and a[-1] == 0: a.pop()
        return a
    def mod(a, b):
        a = trim(a); b = trim(b)
        while a and len(a) >= len(b):
            c = (a[-1] * pow(b[-1], p - 2, p)) % p
            s = len(a) - len(b)
            for i in range(len(b)):
                a[s + i] = (a[s + i] - c * b[i]) % p
            a = trim(a)
        return a
    a = trim(f); b = trim([(i * c) % p for i, c in enumerate(f)][1:])
    while b:
        a, b = b, mod(a, b)
    return len(a) == 1

classes = {}
per_p = {}
monic_only = set()
for p in (3, 5, 7):
    nr = nonresidue(p)
    cnt = 0
    for d in (5, 6):
        leads = [1] if d == 5 else [1, nr]
        for lead in leads:
            for low in itertools.product(range(p), repeat=d):
                f = list(low) + [lead]
                if not squarefree(f, p):
                    continue
                cnt += 1
                N1 = count_points(f, p, 1); N2 = count_points(f, p, 2)
                a1 = N1 - p - 1
                num = a1 * a1 + N2 - p * p - 1
                assert num % 2 == 0, (p, f, N1, N2)
                a2 = num // 2
                key = (p, a1, a2)
                if key not in classes:
                    classes[key] = dict(p=p, a1=a1, a2=a2, N1=N1, N2=N2, deg=d, lead=lead, f=f, degs=[])
                if d not in classes[key]['degs']:
                    classes[key]['degs'].append(d)
                if lead == 1:
                    monic_only.add(key)
    per_p[p] = cnt
    print(f"p={p}: squarefree f examined = {cnt}; distinct (p,a1,a2) so far = {len(classes)}; elapsed {time.time()-t0:.1f}s", flush=True)

# Weil RH check and the kernel-measure data b_k = a_k q^{-k/2}
out = []
all_rh = True
for key in sorted(classes):
    c = classes[key]; p, a1, a2 = key
    coeffs = [1, a1, a2, p * a1, p * p]            # P(T), ascending
    roots = np.roots(coeffs[::-1])
    rh = bool(np.all(np.abs(np.abs(roots) - p ** -0.5) < 1e-6))
    all_rh &= rh
    b = [1.0, a1 / p ** 0.5, a2 / p, a1 / p ** 0.5, 1.0]   # P(z/sqrt q) ascending
    c.update(weil_rh=rh, b=b, monic_family=(key in monic_only))
    out.append(c)
print(f"distinct (p,a1,a2) classes (deg 5 monic + deg 6 lead in {{1, nonresidue}}): {len(out)}")
print(f"  of which reachable with lead = 1 only (the template's monic family): {len(monic_only)}")
print(f"  counted as (p, deg, a1, a2) with deg 5 and deg 6 separately (the template log's key): {sum(len(c['degs']) for c in classes.values())}")
print(f"  same, restricted to lead = 1: {sum(len(c['degs']) for k, c in classes.items() if k in monic_only)}  [NB: a deg-6 nonresidue-lead class that also occurs at deg 5 or monic deg 6 is counted in the monic family]")
print(f"all classes satisfy Weil RH (|root| = q^-1/2 to 1e-6): {all_rh}")
print("a1 = 0 classes:", sum(1 for c in out if c['a1'] == 0), " (monic family:", sum(1 for k in monic_only if k[1] == 0), ")")
def signed_both(c):
    b = c['b']; return min(b) < 0 and min([b[0], -b[1], b[2], -b[3], b[4]]) < 0
neg = sum(1 for c in out if signed_both(c))
print("signed under both identity and flip:", neg, " (monic family:", sum(1 for c in out if c['monic_family'] and signed_both(c)), ")")
for p in (3, 5, 7):
    print(f"p={p}: classes {sum(1 for c in out if c['p']==p)}, a1 range [{min(c['a1'] for c in out if c['p']==p)}, {max(c['a1'] for c in out if c['p']==p)}], a2 range [{min(c['a2'] for c in out if c['p']==p)}, {max(c['a2'] for c in out if c['p']==p)}]")
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "g2_classes.json", "w"), indent=0)
print(f"elapsed s: {time.time()-t0:.1f}")
