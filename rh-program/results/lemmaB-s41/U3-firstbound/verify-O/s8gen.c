/* s8gen.c -- read-O's independent generator of S8(rho) (U3-firstbound read, 2026-10-01).
   Written from the s40 charter definition only. Double-double arithmetic (fma), segmented exact sweep:
   all composites in (B(Ma), B(Mb)] have every g-prime factor <= B(Ma) because B(Mb) <= p1*B(Ma); B(M) = 1 + M t
   (midpoints between lattice points x_k = 1 + (k - 1/2) t, t = 1/rho). A g-prime is placed at x_k iff N(x_k-) == k.
   Every composite c gets u(c) = (c-1) rho + 1/2; its lattice margin min(frac u, 1 - frac u) is recorded (certifies c vs x_k).
   Usage: s8gen <pi_div|dec> <X0>   e.g.  s8gen 16 3e7   (rho = pi/16);  s8gen d0.3 1e7  (rho = 0.3)            */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>

typedef struct { double hi, lo; } dd;
static inline dd qts(double a, double b){ double s=a+b; return (dd){s, b-(s-a)}; }
static inline dd ts(double a, double b){ double s=a+b, bb=s-a; return (dd){s, (a-(s-bb))+(b-bb)}; }
static inline dd dadd(dd a, dd b){ dd s=ts(a.hi,b.hi), t=ts(a.lo,b.lo); s.lo+=t.hi; s=qts(s.hi,s.lo); s.lo+=t.lo; return qts(s.hi,s.lo); }
static inline dd dneg(dd a){ return (dd){-a.hi,-a.lo}; }
static inline dd dmul(dd a, dd b){ double p=a.hi*b.hi, e=fma(a.hi,b.hi,-p); e+=a.hi*b.lo+a.lo*b.hi; return qts(p,e); }
static dd ddiv(dd a, dd b){ double q1=a.hi/b.hi; dd r=dadd(a,dneg(dmul((dd){q1,0},b))); double q2=r.hi/b.hi;
  r=dadd(r,dneg(dmul((dd){q2,0},b))); double q3=r.hi/b.hi; return dadd(qts(q1,q2),(dd){q3,0}); }
static inline int dlt(dd a, dd b){ return a.hi<b.hi || (a.hi==b.hi && a.lo<b.lo); }

static dd RHO, T;                 /* rho and t = 1/rho in double-double */
static double rho, tt, TAU = 0.5;   /* threshold tau (S8 = 1/2): lattice x_k = 1 + (k - 1 + tau) t */
/* G: sorted g-integers <= current boundary */
static double *Ghi, *Glo; static int32_t *Glp; static int64_t Gn, Gcap;
/* primes */
static double *Phi, *Plo; static int64_t *Pk; static int64_t Pn, Pcap;
static double min_margin = 1e9; static double min_margin_at = 0;
static int64_t ncomp_total = 0;

typedef struct { double hi, lo; int32_t lp; int64_t kc; } comp_t;
static int ccmp(const void *a, const void *b){ const comp_t *x=a, *y=b;
  if (x->hi < y->hi) return -1; if (x->hi > y->hi) return 1; if (x->lo < y->lo) return -1; if (x->lo > y->lo) return 1; return 0; }

static dd lattice(int64_t k){ return dadd((dd){1.0,0}, dmul(dadd((dd){(double)k-1.0,0},(dd){TAU,0}), T)); }
static dd bnd(int64_t M){ return dadd((dd){1.0,0}, dmul(dadd((dd){(double)M-0.5,0},(dd){TAU,0}), T)); }

/* floor and frac of a dd value of moderate size */
static int64_t dfloor(dd a, double *frac){ double f=floor(a.hi); if (f==a.hi && a.lo<0) f-=1.0;
  double fr=(a.hi-f)+a.lo; if (fr>=1.0){ f+=1.0; fr-=1.0; } if (fr<0){ f-=1.0; fr+=1.0; } *frac=fr; return (int64_t)f; }

static int64_t lb_index(double v){ /* first index i with Ghi[i] >= v (coarse, double) */
  int64_t lo=0, hi=Gn; while (lo<hi){ int64_t m=(lo+hi)/2; if (Ghi[m]<v) lo=m+1; else hi=m; } return lo; }

static void Gpush(double h, double l, int32_t lp){ if (Gn==Gcap){ Gcap=Gcap*2+1024; Ghi=realloc(Ghi,Gcap*8); Glo=realloc(Glo,Gcap*8); Glp=realloc(Glp,Gcap*4);} Ghi[Gn]=h; Glo[Gn]=l; Glp[Gn]=lp; Gn++; }
static void Ppush(dd v, int64_t k){ if (Pn==Pcap){ Pcap=Pcap*2+1024; Phi=realloc(Phi,Pcap*8); Plo=realloc(Plo,Pcap*8); Pk=realloc(Pk,Pcap*8);} Phi[Pn]=v.hi; Plo[Pn]=v.lo; Pk[Pn]=k; Pn++; }


/* Small-scale step when p1*B(Ma) <= B(Ma+1) (only for B(Ma) < 1/tau): one lattice point, products closed by brute force. */
static void slow_step(int64_t Ma){
  dd Ba = bnd(Ma), Bb = bnd(Ma+1), xk = lattice(Ma+1);
  comp_t Q[4096]; int nq = 0;
  for (int pass = 0; pass < 2; pass++){
    int changed = 1;
    while (changed){ changed = 0;
      for (int64_t qi = 0; qi < Pn; qi++){ dd q = {Phi[qi], Plo[qi]};
        for (int src = 0; src < 2; src++){ int64_t lim = src ? nq : Gn;
          for (int64_t i = 0; i < lim; i++){ dd m = src ? (dd){Q[i].hi,Q[i].lo} : (dd){Ghi[i],Glo[i]}; int32_t lp = src ? Q[i].lp : Glp[i];
            if (lp < 0 || lp > qi) continue;
            dd c = dmul(q, m); if (!dlt(Ba, c) || dlt(Bb, c)) continue;
            int dup = 0; for (int r = 0; r < nq; r++) if (fabs(Q[r].hi - c.hi) < 1e-20*c.hi) { dup = 1; break; }
            if (dup) continue;
            double fr; dd u = dadd(dmul(dadd(c,(dd){-1.0,0}), RHO), (dd){1.0-TAU,0}); int64_t fl = dfloor(u, &fr);
            double mg = fr < 1-fr ? fr : 1-fr; if (mg < min_margin){ min_margin = mg; min_margin_at = c.hi; }
            Q[nq++] = (comp_t){c.hi, c.lo, (int32_t)qi, fl+1}; changed = 1; } } } }
    if (pass == 0){ int64_t below = 0; for (int r = 0; r < nq; r++) if (Q[r].kc <= Ma+1) below++;
      int64_t Nb = Gn + below; if (Nb == Ma+1){ Ppush(xk, Ma+1); Q[nq++] = (comp_t){xk.hi, xk.lo, (int32_t)(Pn-1), -1}; }
      else if (Nb < Ma+1){ fprintf(stderr, "slow_step: N < k\n"); exit(1); } else break; } }
  qsort(Q, nq, sizeof(comp_t), ccmp);
  for (int r = 0; r < nq; r++) Gpush(Q[r].hi, Q[r].lo, Q[r].lp);
  ncomp_total += nq;
}

static void generate(double X0){
  dd p1 = lattice(1);
  Gpush(1.0, 0.0, -1); Ppush(p1, 1); Gpush(p1.hi, p1.lo, 0);
  { dd pw = dmul(p1, p1), B1 = bnd(1); while (!dlt(B1, pw)){ Gpush(pw.hi, pw.lo, 0); pw = dmul(pw, p1); } } /* powers of p1 <= B(1) */
  int64_t Ma = 1, Mend = (int64_t)ceil((X0 - 1.0)*rho + 0.5 - TAU) + 1;          /* B(Mend) >= X0 */
  int64_t ties = 0;
  while (Ma < Mend){
    dd Ba = bnd(Ma), lim = dmul(p1, Ba);
    int64_t Mb = (int64_t)floor((lim.hi - 1.0)*rho + 0.5 - TAU) + 1;
    while (!dlt(bnd(Mb), lim)) Mb--;                                   /* B(Mb) < p1 B(Ma) */
    if (Mb > Mend) Mb = Mend;
    if (Mb <= Ma){ slow_step(Ma); Ma = Ma + 1; continue; }
    dd Bb = bnd(Mb);
    comp_t *C = NULL; int64_t nc = 0, ccap = 0;
    for (int64_t qi = 0; qi < Pn; qi++){
      dd q = (dd){Phi[qi], Plo[qi]};
      double mlo = Ba.hi/q.hi*(1-1e-12), mhi = Bb.hi/q.hi*(1+1e-12);
      if (mhi < p1.hi*(1-1e-12)) break;
      for (int64_t i = lb_index(mlo); i < Gn && Ghi[i] <= mhi; i++){
        if (Glp[i] < 0 || Glp[i] > qi) continue;                         /* m = 1, or q not the largest factor */
        dd c = dmul(q, (dd){Ghi[i], Glo[i]});
        if (!dlt(Ba, c) || dlt(Bb, c)) continue;                         /* need Ba < c <= Bb */
        double fr; dd u = dadd(dmul(dadd(c, (dd){-1.0,0}), RHO), (dd){1.0-TAU,0});
        int64_t fl = dfloor(u, &fr);
        double mg = fr < 1-fr ? fr : 1-fr;
        if (mg < min_margin){ min_margin = mg; min_margin_at = c.hi; }
        if (nc == ccap){ ccap = ccap*2 + 4096; C = realloc(C, ccap*sizeof(comp_t)); }
        C[nc++] = (comp_t){c.hi, c.lo, (int32_t)qi, fl + 1};
      }
    }
    qsort(C, nc, sizeof(comp_t), ccmp);
    for (int64_t i = 1; i < nc; i++){ dd a = {C[i-1].hi, C[i-1].lo}, b = {C[i].hi, C[i].lo};
      dd df = dadd(b, dneg(a)); if (fabs(df.hi) < 1e-22*b.hi) ties++;
      if (C[i].kc < C[i-1].kc){ fprintf(stderr, "kc order violated\n"); exit(1); } }
    int64_t Nbase = Gn, j = 0, np = 0, P0n = Pn;
    for (int64_t k = Ma+1; k <= Mb; k++){
      while (j < nc && C[j].kc <= k) j++;
      int64_t Nb = Nbase + j + np;
      if (Nb == k){ Ppush(lattice(k), k); np++; }
      else if (Nb < k){ fprintf(stderr, "N(x_k-) < k at k=%lld: impossible\n", (long long)k); exit(1); }
    }
    int64_t a = 0, b = P0n;                                             /* merge C and new primes into G */
    while (a < nc || b < Pn){
      int takeC;
      if (a >= nc) takeC = 0; else if (b >= Pn) takeC = 1;
      else takeC = dlt((dd){C[a].hi, C[a].lo}, (dd){Phi[b], Plo[b]});
      if (takeC){ Gpush(C[a].hi, C[a].lo, C[a].lp); a++; } else { Gpush(Phi[b], Plo[b], (int32_t)b); b++; }
    }
    ncomp_total += nc; free(C);
    Ma = Mb;
  }
  printf("generated: G=%lld g-integers, %lld g-primes, %lld composites, up to B=%.6f; ties(rel<1e-22)=%lld\n",
         (long long)Gn, (long long)Pn, (long long)ncomp_total, bnd(Ma).hi, (long long)ties);
  printf("min lattice margin of a composite (lattice units) = %.3e at c = %.6f  [dd error bound ~1e-22 units]\n",
         min_margin, min_margin_at);
}

typedef struct { double v, lg; int j; } pp_t;
static int ppcmp(const void *a, const void *b){ double x=((const pp_t*)a)->v, y=((const pp_t*)b)->v; return x<y?-1:(x>y?1:0); }
static int64_t Gcount(double y){ int64_t lo=0, hi=Gn; while(lo<hi){ int64_t m=(lo+hi)/2; if (Ghi[m]<=y) lo=m+1; else hi=m; } return lo; }
static int64_t Pcount(double y){ int64_t lo=0, hi=Pn; while(lo<hi){ int64_t m=(lo+hi)/2; if (Phi[m]<=y) lo=m+1; else hi=m; } return lo; }
typedef struct { double s, c; } ks_t;                      /* Kahan sum */
static void kadd(ks_t *k, double x){ double y=x-k->c, t=k->s+y; k->c=(t-k->s)-y; k->s=t; }

int main(int argc, char **argv){
  if (argc < 3){ fprintf(stderr, "usage: s8gen <div|dRHO> <X0>\n"); return 1; }
  if (argv[1][0]=='d'){ rho = atof(argv[1]+1); RHO = (dd){rho, 0}; }
  else { dd PI = {3.141592653589793116, 1.224646799147353207e-16}; RHO = ddiv(PI, (dd){atof(argv[1]), 0}); rho = RHO.hi; }
  T = ddiv((dd){1,0}, RHO); tt = T.hi;
  double X0 = atof(argv[2]); if (argc > 3) TAU = atof(argv[3]);
  printf("rho = %.17g (+%.3e), t = %.17g, X0 = %.6g, tau = %.4g\n", RHO.hi, RHO.lo, T.hi, X0, TAU);
  generate(X0);
  printf("first g-primes:"); for (int i=0;i<8 && i<Pn;i++) printf(" %.6f", Phi[i]); printf("\n");
  /* --- records of E(u)/(u-1) and E(u)/u over g-integers <= X0 --- */
  int64_t n0 = Gcount(X0);
  double r1max=-1e9,r1u=0,r1sec=-1e9,r1secu=0,r2max=-1e9,r2u=0,Emax=-1e9,Eu=0;
  double cps[] = {1e3,1e4,1e5,1e6,1e7,3e7,1e8}; int ci = 0;
  for (int64_t i = 1; i < n0; i++){
    double v = Ghi[i], E = (double)i - rho*(v-1.0);
    while (ci < 7 && cps[ci] < v){ if (cps[ci] <= X0) printf("x=%.0e: N=%lld pi=%lld supE=%.4f (at %.3f)\n", cps[ci],
        (long long)Gcount(cps[ci]), (long long)Pcount(cps[ci]), Emax, Eu); ci++; }
    double r1 = E/(v-1.0), r2 = E/v;
    if (r1 > r1max){ r1max = r1; r1u = v; }
    if (i > 1 && r1 > r1sec){ r1sec = r1; r1secu = v; }
    if (r2 > r2max){ r2max = r2; r2u = v; }
    if (E > Emax){ Emax = E; Eu = v; }
  }
  printf("sup_{1<u<=X0} E/(u-1) = %.10f at u = %.6f (rho = %.10f); largest over g-integers other than p1 = %.6f at u = %.4f\n", r1max, r1u, rho, r1sec, r1secu);
  printf("sup_{u<=X0} E/u = %.6f at u = %.6f; sup E = %.4f at %.2f; N(X0) = %lld\n", r2max, r2u, Emax, Eu, (long long)n0);
  /* --- prime powers <= X0, B1 margin at every g-prime, psi, S, D(X0) --- */
  int64_t np0 = Pcount(X0), npp = 0, cap = np0*2 + 64; pp_t *PP = malloc(cap*sizeof(pp_t));
  for (int64_t i = 0; i < np0; i++){ double p = Phi[i], v = p; int j = 1;
    while (v <= X0){ if (npp == cap){ cap *= 2; PP = realloc(PP, cap*sizeof(pp_t)); } PP[npp++] = (pp_t){v, log(p), j}; v *= p; j++; } }
  qsort(PP, npp, sizeof(pp_t), ppcmp);
  ks_t psi = {0,0}, S = {0,0}; double b1max = -1e9, b1u = 0;
  for (int64_t i = 0; i < npp; i++){ kadd(&psi, PP[i].lg); kadd(&S, PP[i].lg/PP[i].v);
    if (PP[i].j == 1){ double y = PP[i].v, Pt = S.s - psi.s/y;
      double F = (1.0-TAU)*psi.s/y + rho*Pt - rho*(log(y)-1.0), m = F - (log(y)+rho)/y;
      if (m > b1max){ b1max = m; b1u = y; } } }
  double P0 = Phi[np0-1], DX0 = log(X0) - 1.0 - (S.s - psi.s/X0);
  printf("B1: max over g-primes y <= X0 of F(y) - (log y + rho)/y = %.6f (at y = %.4f)\n", b1max, b1u);
  printf("psi(X0) = %.6f (psi/X0 = %.6f), S(X0) = %.8f, S - log X0 = %.6f, D(X0) = %.6f, P0 = %.6f, #primes<=X0 = %lld\n",
         psi.s, psi.s/X0, S.s, S.s - log(X0), DX0, P0, (long long)np0);
  /* --- T(P0): exact over g-primes <= X0 + lattice bound for g-primes > X0; also a lattice-uniform bound --- */
  ks_t Tp = {0,0}, Tl = {0,0};
  for (int64_t i = 0; i < np0; i++){ double p = Phi[i], pw = p*p; while (pw <= P0) pw *= p; kadd(&Tp, log(p)/pw/(1.0-1.0/p)); }
  int64_t kmax = (int64_t)floor((X0-1.0)*rho + 1.0 - TAU);
  for (int64_t k = 1; k <= kmax; k++){ double p = 1.0 + ((double)k-1.0+TAU)*tt; if (p > X0) break; double pw = p*p; while (pw <= P0) pw *= p;
    kadd(&Tl, log(p)/pw/(1.0-1.0/p)); }
  double a = X0 - tt, tail = rho*(log(a)+1.0)/(a-1.0);
  double TP0 = Tp.s + tail, TL0 = Tl.s + tail, eta0 = (log(P0)+rho)/P0;
  double eps0 = eta0 + (1.0-TAU)*TP0, epsL = eta0 + (1.0-TAU)*TL0, r0 = 1.0 - rho - TAU;
  printf("T(P0) = %.6e (exact part %.6e + tail bound %.3e); lattice-uniform T <= %.6e; eta(P0) = %.3e\n", TP0, Tp.s, tail, TL0, eta0);
  for (int pass = 0; pass < 2; pass++){ double e0 = pass ? epsL : eps0;
    double D0 = fmin(DX0, (1.0-TAU)/rho - e0/rho), c1p = rho*TAU/(1.0-TAU) + e0/((1.0-TAU)*D0);
    double De0 = (r0*D0 - e0)/(1.0-TAU), c1 = rho*TAU/r0 + (1-rho)*e0/(r0*De0);
    printf("%s: eps0 = %.6e, D0 = %.6f, T1' constant = %.8f (= rho + %.4e); Delta0 = %.6f, T1 record bound = %.6f\n",
           pass ? "lattice-uniform" : "exact primes  ", e0, D0, c1p, c1p - rho, De0, c1);
    printf("   => E(x) <= %.6f (x-1) for all x>1 iff sup_{u<=X0} E/(u-1) <= that; N(x) <= %.6f (x-1) + 1\n",
           fmax(c1p, r1max), rho + fmax(c1p, r1max)); }
  /* --- identity (*) and (A1) at three values of x --- */
  double xs[3] = {1000.5, 123456.7, 9876543.21};
  for (int q = 0; q < 3; q++){ double x = xs[q]; if (x > X0) continue;
    int64_t nx = Gcount(x); double Ex = (double)(nx) - rho*(x-1.0) - 1.0;
    ks_t I = {0,0}, L = {0,0};
    for (int64_t i = 0; i < nx; i++){ double aa = Ghi[i], bb = (i+1 < nx) ? Ghi[i+1] : x;
      kadd(&I, ((double)i + rho)*log(bb/aa) - rho*(bb-aa)); if (i > 0) kadd(&L, log(Ghi[i])); }
    ks_t ps = {0,0}, Ss = {0,0}, SE = {0,0}, SN = {0,0};
    for (int64_t i = 0; i < npp && PP[i].v <= x; i++){ double d = PP[i].v, y = x/d; int64_t Ny = Gcount(y);
      kadd(&ps, PP[i].lg); kadd(&Ss, PP[i].lg/d); kadd(&SE, PP[i].lg*((double)Ny - rho*(y-1.0) - 1.0)); kadd(&SN, PP[i].lg*(double)Ny); }
    double Pt = Ss.s - ps.s/x, lhs = Ex*log(x) - I.s, rhs = ps.s + rho*x*Pt - rho*x*(log(x)-1.0) - rho + SE.s;
    printf("(*) at x = %.2f: LHS = %.9f, RHS = %.9f, diff = %.2e | (A1): sum log n = %.6f, sum Lambda N(x/d) = %.6f, diff = %.2e\n",
           x, lhs, rhs, lhs - rhs, L.s, SN.s, L.s - SN.s);
    printf("    E(x) = %.6f, psi/x = %.6f, D(x) = %.6f, psi/(xD) - rho = %.6f, W(x) = %.6f\n", Ex, ps.s/x, log(x)-1.0-Pt,
           ps.s/(x*(log(x)-1.0-Pt)) - rho, SE.s/x); }
  /* --- Mertens II (Cor. 1.9) --- */
  ks_t R = {0,0}, T2 = {0,0}; double nxt = 100;
  for (int64_t i = 0; i < np0; i++){ double p = Phi[i];
    while (p > nxt && nxt <= X0){ printf("  sum_{p<=%.0e} 1/p - loglog = %.6f\n", nxt, R.s - log(log(nxt))); nxt *= 10; }
    kadd(&R, 1.0/p); kadd(&T2, 1.0/(p*(p-1.0))); }
  double T2b = T2.s + rho*log(a/(a-1.0));
  printf("T2 <= %.6f; proved asymptotic floor log rho - T2 - 1/e - E1(1) = %.6f\n", T2b, log(rho) - T2b - exp(-1.0) - 0.21938393439552);
  return 0;
}
