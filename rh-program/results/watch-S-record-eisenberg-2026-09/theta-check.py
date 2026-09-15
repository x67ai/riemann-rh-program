from mpmath import mp, mpf, log, pi, loggamma, im, mpc
mp.dps=60
def theta(t):
    # exact Riemann-Siegel theta via loggamma
    return im(loggamma(mpc(mpf(1)/4, t/2))) - t/2*log(pi)
for name,t,N,dg in [("t1",mpf("763173730199776587433631628770"),mpf("8012833507866431746081933196518"),(mpf("-.068203"),mpf("-.068103"))),
                    ("t2",mpf("201016554543249943627430143193"),mpf("2067863069844908517322813360229"),(mpf(".078398"),mpf(".078428")))]:
    th=theta(t); S_t = N - th/pi - 1
    print(name,"log(t/2pi)=",mp.nstr(log(t/(2*pi)),6),"S(t)=",mp.nstr(S_t,8))
    for g in dg:
        gam=t+g; Sg = N - theta(gam)/pi - 1   # N constant on the gap if no zero between
        print("  at t+%s: N-theta/pi-1 = %s"%(mp.nstr(g,6),mp.nstr(Sg,8)))
