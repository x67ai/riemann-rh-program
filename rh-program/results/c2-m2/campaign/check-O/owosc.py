from outwin_check import pair
import math
print("L=120: the pair contamination near the builder's u_true = 130.36134 (it OSCILLATES in sign)")
for u in [126.0,127.0,128.0,129.0,129.5,130.0,130.36133764241708,130.8,131.5,132.5]:
    w,v=pair(120,u,86)
    print("   u=%-10.5f u/L=%.5f  pair=%+.6e  |pair|/e^{-L}=%.4f"%(u,u/120,float(w),float(abs(w))/math.exp(-120)))
w,v=pair(120,130.36133764241708,110)
print("   stability at dps=110: |pair|/e^{-L} = %.4f"%(float(abs(w))/math.exp(-120)))
