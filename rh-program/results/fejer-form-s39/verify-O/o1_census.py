"""o1_census.py — read-O independent census of rung-1 zeta data (exact integers only).
Written from NOTE.md §1-§2 definitions, nothing imported from verify/.
Zeta datum: L(u) in Z[u], deg 2g, L(0)=1, L(u) = q^g u^{2g} L(1/(qu)); s_n from Newton; N_n = q^n+1-s_n;
b_d = (1/d) sum_{e|d} mu(d/e) N_e >= 0 (d <= DMAX); h = L(1) >= 1.
Kinds: RH (all |alpha| = sqrt q), REAL-OFF (all x_j real, some |x_j| > 2 sqrt q), NONREAL-X (x_j non-real).
Also: (R), D_k, class-number window, Clifford N_1 <= h, exact. Output: o1_census.log, o1_data.json."""
import json, sys

def mobius(n):
    r, p = 1, 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            if n % p == 0: return 0
            r = -r
        p += 1
    return -r if n > 1 else r

MU = [0] + [mobius(n) for n in range(1, 200)]

def L_coeffs(q, g, a):  # a = (a1,..,ag); FE fills the rest
    c = [1] + list(a) + [0] * g
    for k in range(g + 1, 2 * g + 1):
        c[k] = q ** (k - g) * c[2 * g - k]
    return c

def power_sums(c, nmax):  # s_k = -k c_k - sum_{j<k} s_j c_{k-j}
    s = [0] * (nmax + 1)
    for k in range(1, nmax + 1):
        ck = c[k] if k < len(c) else 0
        acc = -k * ck
        for j in range(1, k):
            if k - j < len(c): acc -= s[j] * c[k - j]
        s[k] = acc
    return s

def admissible(q, c, dmax):
    s = power_sums(c, dmax)
    N = [None] + [q ** n + 1 - s[n] for n in range(1, dmax + 1)]
    for d in range(1, dmax + 1):
        tot = sum(MU[d // e] * N[e] for e in range(1, d + 1) if d % e == 0)
        if tot % d != 0: raise RuntimeError("non-integral b_d")
        if tot < 0: return False, N
    return True, N

def kind(q, g, c):
    if g == 1:
        a = c[1]
        return "RH" if a * a <= 4 * q else "REAL-OFF"
    a1, a2 = c[1], c[2]
    disc = a1 * a1 - 4 * (a2 - 2 * q)        # (x1 - x2)^2
    if disc < 0: return "NONREAL-X"
    ok = (a1 * a1 <= 16 * q) and (2 * q + a2 >= 0) and ((2 * q + a2) ** 2 >= 4 * a1 * a1 * q)
    return "RH" if ok else "REAL-OFF"

def A_coeffs(q, c, nmax):  # coefficients of L(u)/((1-u)(1-qu))
    sig = lambda m: (q ** (m + 1) - 1) // (q - 1) if m >= 0 else 0
    return [sum(c[k] * sig(n - k) for k in range(len(c))) for n in range(nmax + 1)]

def in_window(h, q, g):  # (sqrt q - 1)^{2g} <= h <= (sqrt q + 1)^{2g}, exact: (sqrt q +- 1)^{2g} = A +- B sqrt q
    A, B = (q + 1, 2) if g == 1 else (q * q + 6 * q + 1, 4 * (q + 1))
    lo = (A - h <= 0) or (B * B * q >= (A - h) ** 2)
    hi = (h - A <= 0) or ((h - A) ** 2 <= B * B * q)
    return lo and hi, lo, hi

out, data = [], {}
for q in (5, 7, 11):
    for g in (1, 2):
        R1 = 12 * q; R2 = 40 * q * q
        rng = [(a,) for a in range(-R1, R1 + 1)] if g == 1 else \
              [(a1, a2) for a1 in range(-R1, R1 + 1) for a2 in range(-R2, R2 + 1)]
        rows, maxa = [], [0, 0]
        for a in rng:
            c = L_coeffs(q, g, a)
            h = sum(c)
            if h < 1: continue
            ok8, N = admissible(q, c, 8)
            if not ok8: continue
            ok40, _ = admissible(q, c, 40)
            ok60, _ = admissible(q, c, 60)
            k = kind(q, g, c)
            An = A_coeffs(q, c, 2 * g + 6)
            Th = lambda n: h if n < 0 else (q - 1) * An[n] + h
            Rok = all(Th(n) * q ** max(0, g - 1 - n) == Th(2 * g - 2 - n) * q ** max(0, n - g + 1) for n in range(-4, 2 * g + 3))
            Dok = all(Th(2 * g - 2 + kk) - Th(-kk) == h * (q ** (g - 1 + kk) - 1) for kk in (1, 2, 3))
            win = in_window(h, q, g)
            rows.append(dict(a=list(a), h=h, kind=k, N=N[1:9], ok40=ok40, ok60=ok60, R=Rok, D=Dok,
                             win=win[0], winlo=win[1], winhi=win[2], cliff=(N[1] <= h)))
            for i in range(len(a)): maxa[i] = max(maxa[i], abs(a[i]))
        data["%d_%d" % (q, g)] = rows
        from collections import Counter
        K = Counter(r["kind"] for r in rows)
        bad40 = sum(1 for r in rows if not r["ok40"]); bad60 = sum(1 for r in rows if not r["ok60"])
        false = [r for r in rows if r["kind"] != "RH"]
        out.append("q=%d g=%d: data %d  kinds %s  not-adm-to-40: %d  not-adm-to-60: %d  max|a_i| = %s (box %d, %d)"
                   % (q, g, len(rows), dict(K), bad40, bad60, maxa, R1, R2 if g == 2 else 0))
        out.append("   (R) exact on all: %s ; D_k = h(q^{g-1+k}-1), k=1..3, on all: %s ; D_1 > 0 on all RH-false: %s"
                   % (all(r["R"] for r in rows), all(r["D"] for r in rows), all(r["h"] * (q ** g - 1) > 0 for r in false)))
        out.append("   class-number window: RH-true outside: %d ; RH-false caught: %d of %d (below %d, above %d)"
                   % (sum(1 for r in rows if r["kind"] == "RH" and not r["win"]), sum(1 for r in false if not r["win"]),
                      len(false), sum(1 for r in false if not r["winlo"]), sum(1 for r in false if not r["winhi"])))
        cv = [(r["a"], r["N"][0], r["h"], r["kind"]) for r in rows if not r["cliff"]]
        out.append("   Clifford N_1 > h: %d %s ; NONREAL-X caught: %d" % (len(cv), cv, sum(1 for r in rows if not r["cliff"] and r["kind"] == "NONREAL-X")))
        if g == 1:
            out.append("   admissible t = -a: %s" % sorted(-r["a"][0] for r in rows))
V = [r for r in data["5_1"] if r["a"] == [-5]][0]
out.append("V (q=5, t=5): N_1..8 = %s, h = %d, kind %s" % (V["N"], V["h"], V["kind"]))
V2 = [r for r in data["5_2"] if r["a"] == [-1, 11]]
out.append("V2 (a1,a2)=(-1,11) present: %s %s" % (bool(V2), V2[0]["kind"] if V2 else ""))
# genus 0: P^1, L = 1, h = 1: D_k = q^{k-1} - 1
for q in (5, 7, 11):
    out.append("P1 over F_%d: D_1, D_2, D_3 = %s  (zero only for k = 1)" % (q, [q ** (k - 1) - 1 for k in (1, 2, 3)]))
open("o1_census.log", "w").write("\n".join(out) + "\n")
json.dump(data, open("o1_data.json", "w"))
print("\n".join(out))
