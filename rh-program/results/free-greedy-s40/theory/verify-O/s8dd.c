/* s8dd.c -- Opus reader's independent generator of S8(rho) (read-O, Session 41).
   Written from CHARTER.md s.1 and NOTE Lemma 1.2 only; no code of the unit was copied or imported.
   Method: BLOCK SWEEP. Composites in (B, U] with U <= p1*B use only g-primes <= U/p1 <= B, so after the
   sweep has passed B they are enumerated by a depth-first walk over multisets of known g-primes, sorted,
   and merged with the deficit thresholds x*(N) = 1 + (N - 1/2) t (Lemma 1.2).  Values are double-double
   (about 106 bits); every composite-vs-threshold decision is audited: the minimum relative margin is
   reported and every decision closer than TIE_TOL is written out for a high-precision recheck.
   Usage: s8dd t_hi t_lo X ratio_cap sigma_lo sigma_hi [sigma ...]   (t = 1/rho as a double-double) */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

typedef struct { double hi, lo; } dd;
static inline dd two_sum(double a, double b){ dd r; r.hi=a+b; double bb=r.hi-a; r.lo=(a-(r.hi-bb))+(b-bb); return r; }
static inline dd qts(double a, double b){ dd r; r.hi=a+b; r.lo=b-(r.hi-a); return r; }
static inline dd dd_add(dd x, dd y){ dd s=two_sum(x.hi,y.hi), t=two_sum(x.lo,y.lo); s.lo+=t.hi; s=qts(s.hi,s.lo); s.lo+=t.lo; return qts(s.hi,s.lo); }
static inline dd dd_neg(dd x){ dd r={-x.hi,-x.lo}; return r; }
static inline dd dd_sub(dd x, dd y){ return dd_add(x, dd_neg(y)); }
static inline dd dd_mul(dd x, dd y){ double p=x.hi*y.hi; double e=fma(x.hi,y.hi,-p); e+= x.hi*y.lo + x.lo*y.hi; return qts(p,e); }
static inline dd dd_muld(dd x, double y){ double p=x.hi*y; double e=fma(x.hi,y,-p); e+= x.lo*y; return qts(p,e); }
static inline dd dd_d(double a){ dd r={a,0.0}; return r; }
static inline int dd_lt(dd a, dd b){ return a.hi<b.hi || (a.hi==b.hi && a.lo<b.lo); }
static inline int dd_le(dd a, dd b){ return a.hi<b.hi || (a.hi==b.hi && a.lo<=b.lo); }
static inline double dd_reldiff(dd a, dd b){ dd d=dd_sub(a,b); return fabs(d.hi)/fabs(b.hi); }

#define TIE_TOL 1e-24
static dd T;                 /* t = 1/rho */
static dd RHO;               /* rho as dd */
static dd *P = NULL; static long nP = 0, capP = 0;   /* g-primes, increasing */
static long *PN = NULL;                              /* lattice index n_k of each g-prime */
static dd *C = NULL; static long nC = 0, capC = 0;   /* composites of the current block */
static dd LO, HI;                                    /* current block (LO, HI] */
static long nodes = 0;
static int maxdepth = 0;

static void push_prime(dd v, long n){
  if (nP==capP){ capP = capP? 2*capP : 1<<16; P=realloc(P,capP*sizeof(dd)); PN=realloc(PN,capP*sizeof(long)); if(!P||!PN){fprintf(stderr,"oom P\n");exit(1);} }
  P[nP]=v; PN[nP]=n; nP++;
}
static void push_comp(dd v){
  if (nC==capC){ capC = capC? 2*capC : 1<<16; C=realloc(C,capC*sizeof(dd)); if(!C){fprintf(stderr,"oom C\n");exit(1);} }
  C[nC++]=v;
}
/* all products of >= 2 g-primes (indices nondecreasing from i0) that lie in (LO, HI] */
static long pathix[128]; static dd *FL = NULL; static long nFL = 0;   /* optional: values whose factorization is printed */
static int is_flagged(dd q){ long a=0,b=nFL-1; while(a<=b){ long m=(a+b)/2; if (FL[m].hi==q.hi && FL[m].lo==q.lo) return 1; if (FL[m].hi<q.hi || (FL[m].hi==q.hi && FL[m].lo<q.lo)) a=m+1; else b=m-1; } return 0; }
static void walk(long i0, dd prod, int depth){
  for (long i=i0; i<nP; i++){
    dd q = dd_mul(prod, P[i]);
    if (!dd_le(q, HI)) break;            /* P increasing: every later factor overshoots too */
    nodes++; pathix[depth] = i;
    if (depth>=1 && dd_lt(LO, q)) { push_comp(q); if (depth+1>maxdepth) maxdepth=depth+1;
      if (nFL && is_flagged(q)){ printf("PATH %.17g %.17g n:", q.hi, q.lo); for (int k=0;k<=depth;k++) printf(" %ld", PN[pathix[k]]); printf("\n"); } }
    walk(i, q, depth+1);
  }
}
static int cmp_dd(const void *a, const void *b){ const dd *x=a, *y=b; if (dd_lt(*x,*y)) return -1; if (dd_lt(*y,*x)) return 1; return 0; }
static dd lattice(long N){ return dd_add(dd_d(1.0), dd_muld(T, (double)N - 0.5)); }   /* x*(N) = 1 + (N - 1/2) t */
/* ---- sweep state ---- */
static long N = 1;                 /* g-integers <= current point (the integer 1 at x = 1 included) */
static dd thr;                     /* live threshold x*(N) */
static double supE = -1e9, supE_at = 0, infEm = 1e9, infEm_at = 0, infEm_comp = 1e9, infEm_comp_at = 0;
static double minmarg = 1.0, minmarg_at = 0; static long nties = 0;
static double minB = 1.0, minB_at = 0, minA = 1.0, minA_at = 0;   /* below-threshold / after-prime minima */
static dd lastP; static int last_was_prime = 0; static double maxgap = 0, maxgap_at = 0;
static double *LG = NULL; static long nLG = 0, capLG = 0;   /* log of every g-integer <= X (for F_X) */
static double Xmax; static double nextck; static int ckexp10 = 6;  /* checkpoints 10^(k/2) */
static double decmarg = 1.0;                                     /* min margin since last checkpoint */
static FILE *tf;                                                 /* near-tie / closest-decision log */

static void push_lg(double v){ if(nLG==capLG){ capLG=capLG?2*capLG:1<<20; LG=realloc(LG,capLG*sizeof(double)); if(!LG){fprintf(stderr,"oom LG\n");exit(1);} } LG[nLG++]=v; }
static double Eval(long n_count, dd x){ dd tx = dd_mul(RHO, dd_sub(x, dd_d(1.0))); dd e = dd_sub(dd_d((double)n_count - 1.0), tx); return e.hi + e.lo; }
static void checkpoint(double x){
  printf("CK x=%.6g N=%ld pi=%ld supE=%.4f (at %.6g) supE/log2x=%.4f maxgap=%.4f (at %.6g) minmargin_sofar=%.3e decade_margin=%.3e\n",
         x, N, nP, supE, supE_at, supE/(log(x)*log(x)), maxgap, maxgap_at, minmarg, decmarg);
  fflush(stdout); decmarg = 1.0;
}
static void margin(double m, dd c, const char *kind){
  if (m < minmarg){ minmarg = m; minmarg_at = c.hi; }
  if (kind[0]=='b'){ if (m < minB){ minB = m; minB_at = c.hi; } } else { if (m < minA){ minA = m; minA_at = c.hi; } }
  if (m < decmarg) decmarg = m;
  if (m < TIE_TOL){ nties++; fprintf(tf, "NEARTIE %s c=%.17g %.17g N=%ld margin=%.3e\n", kind, c.hi, c.lo, N, m); }
  else if (m < 1e-12) fprintf(tf, "CLOSE %s c=%.17g %.17g N=%ld margin=%.3e\n", kind, c.hi, c.lo, N, m);
}
static void event_ck(double x){ while (x > nextck && nextck <= Xmax){ checkpoint(nextck); ckexp10++; nextck = pow(10.0, ckexp10/2.0); } }
static void place_prime(void){
  dd p = thr; event_ck(p.hi);
  double em = Eval(N, p) ; if (em < infEm){ infEm = em; infEm_at = p.hi; }      /* E(p-) = N(p-) - T(p) */
  if (nP>0){ double g = (dd_sub(p, P[nP-1])).hi; if (g > maxgap){ maxgap = g; maxgap_at = p.hi; } }
  push_prime(p, N); N++; push_lg(log(p.hi) + p.lo/p.hi);
  double e = Eval(N, p); if (e > supE){ supE = e; supE_at = p.hi; }
  lastP = p; last_was_prime = 1; thr = lattice(N);
}
static void count_comp(dd c){
  event_ck(c.hi);
  margin(dd_reldiff(thr, c), c, "below-threshold");          /* decision c < x*(N) */
  if (last_was_prime) margin(dd_reldiff(c, lastP), c, "after-prime");  /* decision x* < c */
  double em = Eval(N, c); if (em < infEm_comp){ infEm_comp = em; infEm_comp_at = c.hi; }
  N++; push_lg(log(c.hi) + c.lo/c.hi);
  double e = Eval(N, c); if (e > supE){ supE = e; supE_at = c.hi; }
  last_was_prime = 0; thr = lattice(N);
}
/* ---- F_X(sigma), two forms (NOTE Lemma 1.5) ---- */
static double rho_d, EX;
static void nsum(double *s, double *c, double v){ double t = *s + v; if (fabs(*s) >= fabs(v)) *c += (*s - t) + v; else *c += (v - t) + *s; *s = t; }
static double F1(double sg){                     /* sum_{n<=X} n^-s + rho X^{1-s}/(s-1) - E(X) X^-s */
  double s = 0, c = 0; for (long i=0;i<nLG;i++) nsum(&s,&c, exp(-sg*LG[i]));
  nsum(&s,&c, rho_d*pow(Xmax,1-sg)/(sg-1)); nsum(&s,&c, -EX*pow(Xmax,-sg)); return s + c;
}
static double F2(double sg){                     /* zeta_c(s) + s int_1^X E u^{-s-1} du, E linear between g-integers */
  double s = 0, c = 0; nsum(&s,&c,(sg-1+rho_d)/(sg-1));
  for (long j=0;j<nLG;j++){
    double la = LG[j], lb = (j+1<nLG)? LG[j+1] : log(Xmax); double A = (double)j + rho_d;
    nsum(&s,&c, A*(exp(-sg*la) - exp(-sg*lb)));
    nsum(&s,&c, -rho_d*sg*(exp((1-sg)*lb) - exp((1-sg)*la))/(1-sg));
  }
  return s + c;
}
int main(int argc, char **argv){
  if (argc < 7){ fprintf(stderr,"usage: s8dd t_hi t_lo X ratio_cap sigma_lo sigma_hi [sigma ...]\n"); return 1; }
  T.hi = strtod(argv[1],0); T.lo = strtod(argv[2],0); Xmax = strtod(argv[3],0); double rcap = strtod(argv[4],0);
  double slo = strtod(argv[5],0), shi = strtod(argv[6],0);
  /* rho = 1/t in dd by one Newton step */
  double r0 = 1.0/T.hi; dd e = dd_sub(dd_d(1.0), dd_muld(T, r0)); RHO = dd_add(dd_d(r0), dd_d(e.hi*r0)); rho_d = RHO.hi;
  tf = fopen("s8dd_ties.tmp","w");
  { const char *fn = getenv("S8DD_FLAG"); if (fn){ FILE *ff = fopen(fn,"r"); double h,l; long cap=64; FL = malloc(cap*sizeof(dd));
      while (ff && fscanf(ff,"%lf %lf",&h,&l)==2){ if(nFL==cap){cap*=2; FL=realloc(FL,cap*sizeof(dd));} FL[nFL].hi=h; FL[nFL].lo=l; nFL++; }
      if (ff) fclose(ff); qsort(FL,nFL,sizeof(dd),cmp_dd); } }
  nextck = pow(10.0, ckexp10/2.0);
  printf("s8dd: t = %.17g + %.3g, rho = %.17g, X = %.6g, ratio cap %.4g\n", T.hi, T.lo, rho_d, Xmax, rcap);
  thr = lattice(1);
  double p1 = lattice(1).hi, ratio = fmin(p1*(1-1e-12), rcap);
  LO = dd_d(1.0); push_lg(0.0);                 /* the g-integer 1 */
  while (LO.hi < Xmax){
    HI = dd_muld(LO, ratio); if (HI.hi > Xmax) HI = dd_d(Xmax);
    nC = 0; walk(0, dd_d(1.0), 0);
    qsort(C, nC, sizeof(dd), cmp_dd);
    for (long i=0;i<nC;i++){ while (dd_lt(thr, C[i])) place_prime(); count_comp(C[i]); }
    while (dd_le(thr, HI)) place_prime();
    LO = HI;
  }
  event_ck(2*Xmax);
  EX = (double)N - 1.0 - rho_d*(Xmax - 1.0);
  printf("FINAL X=%.6g N(X)=%ld pi(X)=%ld E(X)=%.6f supE=%.6f at %.8g  inf E(p-)=%.12f  inf E(c-) over composites=%.9f at %.8g\n",
         Xmax, N, nP, EX, supE, supE_at, infEm, infEm_comp, infEm_comp_at);
  printf("FINAL maxgap=%.6f closing at %.8g; walk nodes=%ld; max #factors=%d; first primes:", maxgap, maxgap_at, nodes, maxdepth);
  for (int i=0;i<6 && i<nP;i++) printf(" %.10f", P[i].hi); printf("\n");
  printf("AUDIT min relative decision margin=%.4e at %.8g; decisions below %.0e: %ld\n", minmarg, minmarg_at, TIE_TOL, nties);
  printf("AUDIT by kind: composite below live threshold min=%.4e at %.8g; composite just after a placed prime min=%.4e at %.8g\n", minB, minB_at, minA, minA_at);
  for (int k=7;k<argc;k++){ double sg = strtod(argv[k],0); printf("F sigma=%.6f F1=%.12f F2=%.12f diff=%.2e  halfXs=%.3e\n", sg, F1(sg), F2(sg), F1(sg)-F2(sg), 0.5*pow(Xmax,-sg)); }
  if (shi > slo){ double a=slo,b=shi,fa=F1(a),fb=F1(b);
    if (fa*fb < 0){ for (int it=0; it<42; it++){ double m=0.5*(a+b), fm=F1(m); if ((fm>0)==(fa>0)){a=m;fa=fm;} else {b=m;fb=fm;} }
      printf("ROOT real zero of F_X in [%.12f, %.12f]\n", a, b); }
    else printf("ROOT no sign change on [%g,%g]: F=%.6g, %.6g\n", slo, shi, fa, fb); }
  fclose(tf); return 0;
}
