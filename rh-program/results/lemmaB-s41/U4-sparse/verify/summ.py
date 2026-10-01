import sys
for fn in sys.argv[1:]:
    rows=[l.split('|')[0].split() for l in open(fn) if not l.startswith('#')]
    np_=sum(int(r[4]) for r in rows); nc=sum(int(r[5]) for r in rows); Em=max(float(r[13]) for r in rows); em=max(int(r[11]) for r in rows)
    hdr=open(fn).readline().strip()
    print(f"{fn}: idle/primes={np_} comps={nc} N=1+p+c={1+np_+nc} supE={Em:.4f} max e={em}\n   {hdr[:160]}")
