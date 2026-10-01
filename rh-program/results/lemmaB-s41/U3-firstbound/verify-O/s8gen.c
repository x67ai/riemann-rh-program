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
static double rho, tt;
/* G: sorted g-integers <= current boundary */
static double *Ghi, *Glo; static int32_t *Glp; static int64_t Gn, Gcap;
/* primes */
static double *Phi, *Plo; static int64_t *Pk; static int64_t Pn, Pcap;
static double min_margin = 1e9; static double min_margin_at = 0;
static int64_t ncomp_total = 0;

typedef struct { double hi, lo; int32_t lp; int64_t kc; } comp_t;
static int ccmp(const void *a, const void *b){ const comp_t *x=a, *y=b;
  if (x->hi < y->hi) return -1; if (x->hi > y->hi) return 1; if (x->lo < y->lo) return -1; if (x->lo > y->lo) return 1; return 0; }

static dd lattice(int64_t k){ return dadd((dd){1.0,0}, dmul((dd){(double)k-0.5,0}, T)); }
static dd bnd(int64_t M){ return dadd((dd){1.0,0}, dmul((dd){(double)M,0}, T)); }

/* floor and frac of a dd value of moderate size */
static int64_t dfloor(dd a, double *frac){ double f=floor(a.hi); if (f==a.hi && a.lo<0) f-=1.0;
  double fr=(a.hi-f)+a.lo; if (fr>=1.0){ f+=1.0; fr-=1.0; } if (fr<0){ f-=1.0; fr+=1.0; } *frac=fr; return (int64_t)f; }

static int64_t lb_index(double v){ /* first index i with Ghi[i] >= v (coarse, double) */
  int64_t lo=0, hi=Gn; while (lo<hi){ int64_t m=(lo+hi)/2; if (Ghi[m]<v) lo=m+1; else hi=m; } return lo; }

static void Gpush(double h, double l, int32_t lp){ if (Gn==Gcap){ Gcap=Gcap*2+1024; Ghi=realloc(Ghi,Gcap*8); Glo=realloc(Glo,Gcap*8); Glp=realloc(Glp,Gcap*4);} Ghi[Gn]=h; Glo[Gn]=l; Glp[Gn]=lp; Gn++; }
static void Ppush(dd v, int64_t k){ if (Pn==Pcap){ Pcap=Pcap*2+1024; Phi=realloc(Phi,Pcap*8); Plo=realloc(Plo,Pcap*8); Pk=realloc(Pk,Pcap*8);} Phi[Pn]=v.hi; Plo[Pn]=v.lo; Pk[Pn]=k; Pn++; }
