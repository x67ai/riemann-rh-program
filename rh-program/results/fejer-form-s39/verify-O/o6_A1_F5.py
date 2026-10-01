"""o6_A1_F5.py — read-O addition A1, a check of the RH-free argument: over F_5, no cubic x^3 + ax + b (any a, b, discriminant
or not) is a non-square at every x in F_5, because sum_x f(x) = 0 in F_5 forces such an f to be constant on F_5 (values in {2, 3}:
15 - k = 0 mod 5 => k in {0, 5}), and a monic cubic minus a constant has at most 3 roots. Hence #E(F_5) >= 2 for every elliptic curve."""
q = 5; nonsq = {2, 3}
bad = [(a, b) for a in range(q) for b in range(q) if all((x ** 3 + a * x + b) % q in nonsq for x in range(q))]
sums = {(a, b): sum((x ** 3 + a * x + b) for x in range(q)) % q for a in range(q) for b in range(q)}
const = [(a, b) for a in range(q) for b in range(q) if len({(x ** 3 + a * x + b) % q for x in range(q)}) == 1]
out = ["cubics x^3+ax+b over F_5 non-square at every x: %s" % bad,
       "sum_x f(x) mod 5 over all (a,b): %s" % sorted(set(sums.values())),
       "cubics constant on F_5: %s" % const]
open("o6_A1_F5.log", "w").write("\n".join(out) + "\n"); print("\n".join(out))
