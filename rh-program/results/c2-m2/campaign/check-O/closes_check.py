#!/usr/bin/env python3
"""CHECK-O items (4), (5) positive control, (6) stop conditions, (7) lint: all of CAMPAIGN.md's close arithmetic,
recomputed from the row/summary files and from the checker's own transform (ind_transform.py).  campaign_lib.py is NOT imported."""
import json, math, sys, os, warnings, numpy as np
warnings.filterwarnings("ignore")
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import ind_transform as T
BASE=os.path.dirname(HERE)
tags=["t1e3","t1e4","t1e5","t1e6"]; ts=[1e3,1e4,1e5,1e6]; ds=[0.05,0.1,0.25]
B1=8.70; R0=81.0; LAM0=25.; C0=4.; BP2=16.62196535
def ellR(t,L): return math.log(4+t+R0*L)
def Lstar(d,t,C1=1.0): return max(LAM0/d, C0/d*(math.log(math.log(3+t))+2*math.log(1/d)+math.log(2*B1*C1)))
S={tg:json.load(open(f"{BASE}/summary_{tg}.json")) for tg in tags}
at={(tg,d):S[tg]["derived"][str(d)] for tg in tags for d in ds}
md={(tg,d):S[tg]["ensemble"]["per_delta"][str(d)] for tg in tags for d in ds}
print("="*118); print("CHECK-O closes_check.py")
print("\n(1) twelve-point tables of CAMPAIGN section 2, read back from summary_*.json")
camp={("L_sign",0.05):[32.1,25.1,25.8,33.3],("L_sign",0.1):[19.4,13.5,20.1,22.4],("L_sign",0.25):[6.7,8.8,9.5,11.0],
      ("L_bal3",0.05):[37.6,58.8,29.2,38.5],("L_bal3",0.1):[28.5,22.2,23.9,28.9],("L_bal3",0.25):[11.6,11.1,13.4,13.3]}
cmed={("L_sign",0.05):[20.6,27.8,29.0,31.4],("L_sign",0.1):[15.4,18.0,19.2,20.6],("L_sign",0.25):[8.4,9.2,10.2,10.8],
      ("L_bal3",0.05):[24.0,35.0,36.2,42.2],("L_bal3",0.1):[19.4,25.0,26.0,27.2],("L_bal3",0.25):[11.2,12.8,13.8,14.4]}
ok=True
for nm in ["L_sign","L_bal3"]:
    for d in ds:
        a=[at[(tg,d)][nm] for tg in tags]; m=[md[(tg,d)][nm+"_median"] for tg in tags]
        ok&= a==camp[(nm,d)] and m==cmed[(nm,d)]
        print("   %-7s d=%-5g at t %s  median %s  -> match %s / %s"%(nm,d,a,m,a==camp[(nm,d)],m==cmed[(nm,d)]))
print("   ALL 24 CELLS MATCH:",ok)
print("\n(1b) least squares log L = a + b log(1/delta) + c log log(t/2pi)")
def fit(v):
    A=[];y=[]
    for tg,t in zip(tags,ts):
        for d in ds: A.append([1.,math.log(1/d),math.log(math.log(t/(2*math.pi)))]); y.append(math.log(v[(tg,d)]))
    A=np.array(A);y=np.array(y); c,_,_,_=np.linalg.lstsq(A,y,rcond=None); return c, math.exp(np.abs(A@c-y).max())
for nm,key,tab in [("L_sign at t","L_sign",at),("L_bal3 at t","L_bal3",at),
                   ("L_sign median","L_sign_median",md),("L_bal3 median","L_bal3_median",md)]:
    v={k:tab[k][key] for k in tab}; c,mx=fit(v)
    print("   %-16s b = %.3f, c = %.3f, max residual factor %.3f"%(nm,c[1],c[2],mx))
print("   CAMPAIGN section 3: (0.737,0.262)/1.281, (0.732,0.003)/1.443, (0.642,0.368)/1.119, (0.596,0.434)/1.179")
print("\n(1c) the three laws with a free (geometric-mean) prefactor")
laws={"density  d^-2/3 (log t/2pi)^1/3":(2/3,1/3),"theorem  d^-1 (t-flat)":(1.,0.),"transcript d^-0.07 (log)^0.89":(0.07,0.89)}
for nm,key,tab in [("L_sign at t","L_sign",at),("L_sign median","L_sign_median",md),
                   ("L_bal3 at t","L_bal3",at),("L_bal3 median","L_bal3_median",md)]:
    for ln,(b,c) in laws.items():
        num=[];pr=[]
        for tg,t in zip(tags,ts):
            for d in ds: num.append(tab[(tg,d)][key]); pr.append((1/d)**b*(math.log(t/(2*math.pi)))**c)
        num=np.array(num);pr=np.array(pr);A=math.exp(np.mean(np.log(num/pr)));r=num/(A*pr)
        print("   %-14s %-34s prefactor %.3f ratio [%.3f, %.3f] -> %s"%(nm,ln,A,r.min(),r.max(),"YES" if r.min()>=1/1.5 and r.max()<=1.5 else "NO"))
    # the theorem's OWN L*(delta,t) shape, not the pure delta^-1 idealization
    num=[];pr=[]
    for tg,t in zip(tags,ts):
        for d in ds: num.append(tab[(tg,d)][key]); pr.append(Lstar(d,t))
    num=np.array(num);pr=np.array(pr);A=math.exp(np.mean(np.log(num/pr)));r=num/(A*pr)
    print("   %-14s %-34s prefactor %.5f ratio [%.3f, %.3f] -> %s"%(nm,"theorem  exact L*(delta,t) shape",A,r.min(),r.max(),"YES" if r.min()>=1/1.5 and r.max()<=1.5 else "NO"))
print("   the theorem's own delta-ratio L*(0.05)/L*(0.25): t=1e3 %.3f ; t=1e6 %.3f  (CAMPAIGN quotes the law-ratio as 5)"
      %(Lstar(0.05,1e3)/Lstar(0.25,1e3),Lstar(0.05,1e6)/Lstar(0.25,1e6)))
print("   measured delta-ratios at t  : L_sign %s ; L_bal3 %s"%(["%.2f"%(at[(tg,0.05)]["L_sign"]/at[(tg,0.25)]["L_sign"]) for tg in tags],
                                                                ["%.2f"%(at[(tg,0.05)]["L_bal3"]/at[(tg,0.25)]["L_bal3"]) for tg in tags]))
print("   measured delta-ratios median: L_sign %s ; L_bal3 %s"%(["%.2f"%(md[(tg,0.05)]["L_sign_median"]/md[(tg,0.25)]["L_sign_median"]) for tg in tags],
                                                                ["%.2f"%(md[(tg,0.05)]["L_bal3_median"]/md[(tg,0.25)]["L_bal3_median"]) for tg in tags]))
print("\n(2) close 2: L* spend, and the clause-4 looseness")
l3=math.log(math.log(3+1e6)); l2=2*math.log(10); lb=math.log(2*B1)
print("   L*(0.1, 1e6) = 40*(%.4f + %.4f + %.4f) = %.2f ; shares %.1f / %.1f / %.1f %% ; floor 40*%.4f = %.1f"
      %(l3,l2,lb,40*(l3+l2+lb),100*l3/(l3+l2+lb),100*l2/(l3+l2+lb),100*lb/(l3+l2+lb),l2+lb,40*(l2+lb)))
q={1e3:(2.56,4.54),1e4:(1.32,1.57),1e5:(1.42,1.83),1e6:(0.93,1.16)}
for tg,t in zip(tags,ts):
    g=S[tg]["ensemble"]["grid"]
    v=np.array([(2*B1*ellR(t,x["L"])/x["L"]**2)/x["mean"]/x["L"] for x in g if x["L"]>=50])
    vs=np.array([(2*B1*ellR(t,x["L"])/x["L"]**2)/x["N_Z_at_t"]/x["L"] for x in g if x["L"]>=50])
    print("   t=%-8g (bound/mean N_Z)/L in [%.2f, %.2f] (CAMPAIGN [%.2f, %.2f]) ; single-t [%.2f, %.0f]"%(t,v.min(),v.max(),q[t][0],q[t][1],vs.min(),vs.max()))
    for r in json.load(open(f"{BASE}/rows_{tg}.json")):
        if abs(r["delta"]-0.1)<1e-12 and r.get("is_record_point_C1_1"):
            print("      record point L* = %.2f: N_Z = %.3e vs clause-4 bound %.3e -> %.3e"%(r["L"],r["N_Z"],r["clause4_bound_C1_1"],r["clause4_bound_C1_1"]/r["N_Z"]))
print("\n(3) close 3: bump-only crossing with the CHECKER's own c(lambda)")
f=lambda l: 2*float(T.cedge(l,16000)[0])**2-math.exp(l/2)
a,b=18.,19.
for _ in range(45):
    m=(a+b)/2
    a,b=(m,b) if f(m)<0 else (a,m)
print("   least lambda with 2 c(lambda)^2 >= e^{lambda/2}: exact %.6f -> 18.6 on a 0.1 grid (record 18.6; proved from 23; contract 25)"%((a+b)/2))
print("   c(25)^2/e^{12.5} = %.6f (note section 3.3 quotes 2.00)"%(float(T.cedge(25.,16000)[0])**2/math.exp(12.5)))
print("\n(4) close 4 arithmetic")
cB=2/math.sqrt(72*math.e)
print("   (7/(8*0.85))^2 = %.4f ; (7/(8/sqrt2))^2 = %.4f ; (7/(8 c_B))^2 = %.4f with c_B = %.8f"%((7/(8*.85))**2,(7/(8/math.sqrt(2)))**2,(7/(8*cB))**2,cB))
print("   factor in R_0 from c_B to the numerical rate: (0.7071/c_B)^2 = %.1f ; (0.85/c_B)^2 = %.1f (CAMPAIGN 'approx 25-35')"%((0.70710678/cB)**2,(0.85/cB)**2))
print("\n(5) V.4 positive control: W_{Z'} >= 0 at every row of every height")
for tg,t in zip(tags,ts):
    rows=json.load(open(f"{BASE}/rows_{tg}.json")); v=np.array([r["W_Zprime"] for r in rows])
    fs=json.load(open(f"{BASE}/finescan_{tg}.json")); fv=np.array(fs["N_Z"])
    print("   t=%-8g rows %d min %.4e (>=0 %s) ; fine grid %d min %.4e (>=0 %s) ; clause-4 violations (L>=50) %d"
          %(t,len(v),v.min(),bool(v.min()>=0),len(fv),fv.min(),bool(fv.min()>=0),S[tg]["controls"]["positive_clause4_violations"]))
print("\n(6) stop condition (iv): the contract's literal form (single t) against the builder's restatement (center mean)")
for tg,t in zip(tags,ts):
    rows=[r for r in json.load(open(f"{BASE}/rows_{tg}.json")) if abs(r["delta"]-0.1)<1e-12 and r["L"] in [float(L) for L in range(4,121,2)]]
    v=np.array([r["N_over_model"] for r in rows]); sc=S[tg]["stop_conditions"]["iv"]
    print("   t=%-8g LITERAL single-t N_Z/model: min %.4f max %.4f geomean %.4f ; rows outside [0.1,10]: %d of %d -> %s"
          %(t,v.min(),v.max(),math.exp(np.mean(np.log(v))),int(((v<0.1)|(v>10)).sum()),len(v),"FIRES" if ((v<0.1)|(v>10)).any() else "does not fire"))
    print("            RESTATED center-mean N_Z/model: min %.4f max %.4f geomean %.4f ; outside: %d -> does not fire"%(sc["min"],sc["max"],sc["geomean"],sc["outside_10x"]))
print("\nDONE")
