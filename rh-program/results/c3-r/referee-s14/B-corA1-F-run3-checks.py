#!/usr/bin/env python3
"""Finite-level machine checks for referee report B-corA1-F.md (run 3, 2026-09-02).
Every check is an elementary, exhaustive computation over small parameters; none is a proof,
each pins one arithmetic or point-set step of the derivation to a concrete instance.
Output: B-corA1-F-run3-checks.json (all 'ok' fields must be True)."""
import json, itertools, math, random
from functools import reduce

def primes_upto(n):
    s=[True]*(n+1); s[0]=s[1]=False
    for i in range(2,int(n**.5)+1):
        if s[i]:
            for j in range(i*i,n+1,i): s[j]=False
    return [i for i in range(n+1) if s[i]]

out={}

# C1: CRT density of N in Z_(p) at finite level: for M prime to p, every residue class mod M
#     contains a positive integer (trivially the least positive representative), and a compatible
#     system of residues mod M_1 | M_2 | ... (a point of Z_(p)) is approximated by n_k ≡ a mod M_k.
p=5
Ms=[2,3,6,12,36,72,144,1008]  # prime to 5, divisibility chain not required
ok=True
for M in Ms:
    assert math.gcd(M,p)==1
    hit=set((n % M) for n in range(1,M+1))
    ok &= (hit==set(range(M)))
out['C1_CRT_density_positive_integers']={'p':p,'moduli':Ms,'ok':ok}

# C2: (Tors) criterion. Exponent b in Z_(p) given by ell-adic valuations v_ell(b_ell) (None = 0 component).
#     kernel of ()^b on the ell-primary part mu_{ell^infty} has order ell^{v_ell(b_ell)} (infinite if b_ell=0).
#     Finite kernel iff every component nonzero AND all but finitely many v_ell = 0.
def kernel_order_truncated(vals, k):
    # vals: dict ell -> valuation or None ; truncate mu_{ell^infty} to mu_{ell^k}; return kernel order
    o=1
    for ell,v in vals.items():
        o*= ell**k if v is None else ell**min(v,k)
    return o
ells=[l for l in primes_upto(60) if l!=p]
b_unit={l:0 for l in ells}                     # a unit: kernel trivial
b_int={l:0 for l in ells}; b_int[2]=3; b_int[3]=1   # b = 24 * unit : kernel order 24
b_zero={l:0 for l in ells}; b_zero[7]=None          # a zero component: kernel contains mu_{7^infty}
b_allell={l:1 for l in ells}                    # b = (ell)_ell : every component nonzero, none a unit
growth={}
for name,b in [('unit',b_unit),('24unit',b_int),('zero7',b_zero),('prod_ell',b_allell)]:
    growth[name]=[kernel_order_truncated(b,k) for k in (1,2,3,4)]
ok = (growth['unit']==[1,1,1,1] and growth['24unit']==[6,12,24,24]
      and growth['zero7'][-1]>growth['zero7'][0] and growth['zero7']==[7,49,343,2401]
      and growth['prod_ell'][0]==reduce(lambda a,b:a*b,ells) and growth['prod_ell'][0]==growth['prod_ell'][3])
# For b=(ell)_ell the truncated kernel is already prod of all ell <= 60 at k=1 and grows with the cutoff:
ells2=[l for l in primes_upto(200) if l!=p]
ok &= kernel_order_truncated({l:1 for l in ells2},1) > kernel_order_truncated(b_allell,1)
out['C2_Tors_criterion_kernel_orders']={'p':p,'kernel_orders_by_truncation':growth,
    'note':'zero component -> kernel grows with k (mu_{7^infty}); b=(ell)_ell -> kernel grows with the prime cutoff; both infinite. Only unit*integer exponents have bounded kernel.','ok':bool(ok)}

# C3: chart membership. P0 = (x, chi^{a0}) with a0 a unit; F_{m/m'}P0 in X•(C) iff chi^{a0 m} trivial on mu_{m'},
#     iff m' | a0*m in Z_(p) iff (prime-to-p part of m') | m; with gcd(m,m')=1 iff prime-to-p part of m' is 1.
ok=True; witnesses=[]
for mp in range(1,40):
    mp_p = mp
    while mp_p % p == 0: mp_p//=p
    for m in range(1,40):
        if math.gcd(m,mp)!=1: continue
        for a0 in range(1,mp_p+1):
            if math.gcd(a0,mp_p)!=1: continue
            trivial_on_mu = ((a0*m) % mp_p == 0)   # zeta^{a0 m} = 1 for zeta of exact order mp_p
            ok &= (trivial_on_mu == (mp_p==1))
            if mp_p==1 and mp>1 and not witnesses: witnesses.append({'m':m,"m'":mp,'note':"p-power denominator allowed"})
out['C3_chart_membership_denominator_criterion']={'p':p,'ok':ok,'witness_p_power_denominator':witnesses}

# C4: un-cut counterexample: n_k = prod_{ell<=k, ell != p} ell^k -> 0 in Z_(p): zeta^{n_k}=1 for every zeta
#     of prime-to-p order M once k >= max(prime factors of M) and k >= max valuation.
def n_k(k):
    return reduce(lambda a,b:a*b,[l**k for l in primes_upto(k) if l!=p],1)
ok=True
for M in [2,3,4,9,12,36,77,100*0+121,1001]:
    if math.gcd(M,p)!=1: continue
    kmin=max(max(l for l in primes_upto(M) if M%l==0), max(v for v in [sum(1 for _ in itertools.takewhile(lambda e:(M % (l**e))==0, range(1,20))) for l in primes_upto(M) if M%l==0]))
    ok &= all( (n_k(k) % M)==0 for k in range(kmin, kmin+3))
out['C4_uncut_limit_n_k_to_zero']={'p':p,'ok':ok,'n_3':n_k(3),'n_4':n_k(4)}

# C5: exact eventual agreement: n_k ≡ â mod M_k gives zeta^{n_k} = zeta^{â} exactly for ord(zeta) | M_k.
ok=True
for ahat in [-1, 2, 7, 11]:   # units of Z_(5) for these small moduli? -1 always; others when coprime to M
    for M in [3,4,9,12,36,72]:
        if math.gcd(ahat,M)!=1: continue
        n=(ahat % M) or M
        ok &= (n>0 and (n-ahat)%M==0)
        for d in [d for d in range(1,M+1) if M%d==0]:
            ok &= ((n - ahat) % d == 0)   # zeta^{n} = zeta^{ahat} for zeta of order d | M
out['C5_exact_eventual_agreement']={'ok':ok}

# C6: point-set lemma f^{-1}(cl A) = cl(f^{-1} A) for an open continuous surjection: brute force on finite
#     spaces (Alexandrov topologies from random preorders) with a finite group of automorphisms; the quotient
#     map is open. Also C8: closure is local on open covers: cl(A) ∩ U = cl_U(A ∩ U) for U open.
random.seed(7)
def alexandrov_opens(n, rel):
    # rel: set of (i,j) meaning i <= j ; open sets = up-sets
    ups=[]
    for mask in range(1<<n):
        S={i for i in range(n) if mask>>i&1}
        if all((j in S) for i in S for (a,j) in rel if a==i): ups.append(frozenset(S))
    return ups
def closure(A, opens, pts):
    # cl(A) = complement of the largest open set missing A
    U=set()
    for O in opens:
        if not (O & A): U|=O
    return pts - U
ok6=True; ok8=True; trials=0
for t in range(40):
    n=random.randint(3,6)
    # random preorder generated by random pairs, closed transitively
    rel={(i,i) for i in range(n)}
    for _ in range(random.randint(0,n)):
        rel.add((random.randrange(n),random.randrange(n)))
    changed=True
    while changed:
        changed=False
        for (a,b) in list(rel):
            for (c,d) in list(rel):
                if b==c and (a,d) not in rel: rel.add((a,d)); changed=True
    pts=set(range(n)); opens=alexandrov_opens(n,rel)
    # C8 on this space
    for U in opens:
        opensU=[O & U for O in opens]
        for mask in range(1<<n):
            A={i for i in range(n) if mask>>i&1}
            lhs=closure(A,opens,pts) & U
            rhs=closure(A & U, opensU, set(U))
            ok8 &= (lhs==rhs)
    # C6: quotient by an automorphism group: pick a permutation preserving rel, of order 2 or 3
    perms=[s for s in itertools.permutations(range(n)) if all((s[a],s[b]) in rel for (a,b) in rel)]
    perms=[s for s in perms if s!=tuple(range(n))]
    if not perms: continue
    s=random.choice(perms)
    # group generated by s
    G=[tuple(range(n))]; g=s
    while g not in G: G.append(g); g=tuple(s[g[i]] for i in range(n))
    orbit={i: frozenset(g[i] for g in G) for i in range(n)}
    Y=list({orbit[i] for i in range(n)}); Yidx={o:k for k,o in enumerate(Y)}
    f={i:Yidx[orbit[i]] for i in range(n)}
    # quotient topology on Y
    opensY=[]
    for mask in range(1<<len(Y)):
        S=frozenset(k for k in range(len(Y)) if mask>>k&1)
        pre={i for i in range(n) if f[i] in S}
        if frozenset(pre) in opens: opensY.append(S)
    ptsY=set(range(len(Y)))
    # openness of f (should hold since G acts by homeomorphisms)
    for O in opens:
        img=frozenset(f[i] for i in O); ok6 &= (img in opensY)
    for mask in range(1<<len(Y)):
        A={k for k in range(len(Y)) if mask>>k&1}
        pre={i for i in range(n) if f[i] in A}
        lhs={i for i in range(n) if f[i] in closure(A,opensY,ptsY)}
        rhs=closure(pre,opens,pts)
        ok6 &= (lhs==rhs)
    trials+=1
out['C6_open_map_closure_identity']={'trials':trials,'ok':ok6}
out['C8_closure_local_on_open_cover']={'ok':ok8}

# C9: p has infinite order in Z_ell^x for ell != p: its order in (Z/ell^k)^x is unbounded in k.
ok=True; orders={}
for ell in [2,3,7,11]:
    if ell==p: continue
    ords=[]
    for k in range(1,7):
        M=ell**k; o=1; x=p%M
        while x!=1: x=(x*p)%M; o+=1
        ords.append(o)
    orders[ell]=ords; ok &= (ords[-1]>ords[0] and all(ords[i+1]>=ords[i] for i in range(len(ords)-1)))
out['C9_p_infinite_order_in_Z_ell_units']={'p':p,'orders_of_p_mod_ell^k':orders,'ok':ok}

# C10: a positive integer is a unit of Z_(p)=prod_{ell!=p} Z_ell iff it is a power of p.
ok=all( ((all(n%l for l in primes_upto(n) if l!=p)) == (n==p**round(math.log(n,p)) and p**round(math.log(n,p))==n)) for n in range(1,400))
out['C10_positive_integer_unit_iff_p_power']={'p':p,'ok':ok}

out['ALL_OK']=all(v.get('ok',True) for v in out.values() if isinstance(v,dict))
json.dump(out,open('B-corA1-F-run3-checks.json','w'),indent=1)
print(json.dumps(out,indent=1))
