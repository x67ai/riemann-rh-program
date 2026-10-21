"""Finite exact diagnostics for the Tate v2 manuscript; no external packages.
Run python3 check_exact.py. The theorems are proved in main.tex; no finite
scan here decides the open rational-product coincidence for distinct primes.
"""
from pathlib import Path
from fractions import Fraction
import json

def determinant(columns):
    n=len(columns)
    a=[[Fraction(columns[j][i]) for j in range(n)] for i in range(n)]
    value=Fraction(1)
    for i in range(n):
        pivot=next((j for j in range(i,n) if a[j][i]),None)
        if pivot is None:return 0
        if pivot!=i:a[i],a[pivot]=a[pivot],a[i];value=-value
        d=a[i][i];value*=d
        for k in range(i,n):a[i][k]/=d
        for j in range(i+1,n):
            d=a[j][i]
            for k in range(i,n):a[j][k]-=d*a[i][k]
    assert value.denominator==1
    return value.numerator

def graph(m):return [(1,0,m,0),(0,1,0,m)]
xi1=[(0,0,1,0),(0,0,0,1)]
xi2=[(1,0,0,0),(0,1,0,0)]
checked=0
for m in range(-20,21):
    assert determinant(graph(m)+xi1)==1
    assert determinant(graph(m)+xi2)==m*m
    for n in range(-20,21):
        assert determinant(graph(m)+graph(n))==(m-n)**2
        checked+=1
for u in range(1,41):
    for v in range(1,41):
        # lambda sends the source lattice basis to (0,v),(-u,0).
        assert determinant([(0,v),(-u,0)])==u*v
        checked+=1
result={'status':'PASS','integer_determinants_checked':checked+82,
        'synthetic_map_matrix':'[[0,-u],[v,0]], determinant=uv; the map is the Hom generator when gcd(u,v)=1',
        'graph_profiles':'Gamma_m.xi1=1; Gamma_m.xi2=m^2; Gamma_m.Gamma_n=(m-n)^2',
        'scope':'Exact finite diagnostics; no transcendence decision is inferred.'}
Path(__file__).with_name('check-result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
