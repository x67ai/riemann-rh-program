"""Exact rationality check of the half-band rows, using only integer arithmetic."""
from pathlib import Path
import json
base=Path(__file__).resolve().parent
data=json.loads((base/'witness-data.json').read_text())

def trim(p):
    while len(p)>1 and p[-1]==0:p.pop()
    return p

def divide_monic(a,b):
    a=a[:];q=[0]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b) and any(a):
        k=len(a)-len(b);v=a[-1];q[k]=v
        for j,c in enumerate(b):a[j+k]-=v*c
        trim(a)
    return trim(q),trim(a)

# Phi_65=(x^65-1)(x-1)/((x^5-1)(x^13-1)).
num=[0]*67;num[0]=1;num[1]=-1;num[65]=-1;num[66]=1
den=[0]*19;den[0]=1;den[5]=-1;den[13]=-1;den[18]=1
phi,rem=divide_monic(num,den);assert rem==[0] and len(phi)==49
results=[]
for col in data['columns']:
    coeff=[0]*65
    sites=[(k,m) for k,m in enumerate(col['marks']) if m]
    for s in range(-32,33):
        for k,m in sites:
            for l,n in sites:coeff[(-s*(k-l))%65]+=(33-abs(s))*m*n
    _,remainder=divide_monic(trim(coeff),phi)
    results.append({'rational':len(remainder)==1,'remainder_coefficients':remainder,'denominator':1089})
assert [r['rational'] for r in results]==[True,False,False]
(base/'cyclotomic-result.json').write_text(json.dumps({'status':'PASS','rows':results},indent=2)+'\n')
print('PASS: vacancy Fp is rational; columns A1 and A2 have nonconstant remainders modulo Phi_65 and hence irrational Fp.')
