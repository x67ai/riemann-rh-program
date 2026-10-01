/* s8gen.c — U7-patterns (lemmaB-s41), own generator of S8(rho) with threshold tau and early offset delta.
   Block sweep: composites in lattice cells (x_{K}, x_{K'}] with x_{K'} < p1*x_K use only g-primes < x_K.
   Double-double arithmetic; every cell decision audited: margin of u=(c-1)rho+1-tau from an integer must be
   >= FLAGTOL (1e-15) while the proved arithmetic error is < 1e-17 (see NOTE); smaller margins are written to
   the .flag file and counted (re-decided at 60 digits by redecide.py).
   Lattice x_k = 1 + (k-1+tau) t, cell k = (x_{k-1}, x_k]; prime decided at k iff e_{k-1}=0 and c_k=0,
   placed at value x_k - delta (delta = dfrac*t + dabs, 0 <= delta < tau*t).
   Usage: s8gen th tl rh rl tau dfrac dabs X outprefix [watchfile]   (th tl rh rl = hex dd of t and rho) */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>

typedef struct { double hi, lo; } dd;
static inline dd two_sum(double a, double b){ dd r; double s=a+b, bb=s-a; r.hi=s; r.lo=(a-(s-bb))+(b-bb); return r; }
static inline dd qts(double a, double b){ dd r; double s=a+b; r.hi=s; r.lo=b-(s-a); return r; }
static inline dd ddmul(dd a, dd b){ double p=a.hi*b.hi; double e=fma(a.hi,b.hi,-p); e+=a.hi*b.lo+a.lo*b.hi; return qts(p,e); }
static inline dd ddmuld(dd a, double b){ double p=a.hi*b; double e=fma(a.hi,b,-p); e+=a.lo*b; return qts(p,e); }
static inline dd ddadd(dd a, dd b){ dd s=two_sum(a.hi,b.hi); s.lo+=a.lo+b.lo; return qts(s.hi,s.lo); }
static inline dd ddaddd(dd a, double b){ dd s=two_sum(a.hi,b); s.lo+=a.lo; return qts(s.hi,s.lo); }
static inline int ddlt(dd a, dd b){ return a.hi<b.hi || (a.hi==b.hi && a.lo<b.lo); }

#define FLAGTOL 1e-15
static dd T, RHO, DELTA; static double TAU;
static uint32_t *PK = NULL; static double TH1; /* prime j has value 1 + (PK[j]-1+tau)t - delta */ static long np = 0, npcap = 0, npblock = 0;
static long K0, K1;                 /* current chunk: cells K0..K1 */
static uint8_t *cc, *c1, *c2, *dv[3]; /* per-cell counts in chunk: total, spf = p1, Omega = 2, divisible by p2, p3, p4 */
static float *lastf;                /* largest fractional position of a composite in the cell */
static long nflag = 0, ncomp = 0, nover = 0; static double minmargin = 1.0, minmargin_x = 0;
static FILE *fflag = NULL, *fwatch = NULL;
static int stk[256], depth_max = 0, depth_top = 0;
static long *wa = NULL, *wb = NULL; static int nw = 0;   /* watch windows (cell ranges) */
/* checkpoints */
#define NCK 64
static int nck = 0; static double ckx[NCK]; static long ckcell[NCK]; static double ckf[NCK]; static long ckpart[NCK];

static dd xlat(long k){ return ddaddd(ddmuld(T, (double)(k-1)+TAU), 1.0); }       /* lattice point x_k */
static inline dd pvj(long j){ return ddadd(ddaddd(ddmuld(T, (double)PK[j]-1.0+TAU), 1.0), (dd){-DELTA.hi, -DELTA.lo}); }
static inline double pvh(long j){ return TH1 + ((double)PK[j]-1.0)*T.hi; }
static dd pval(long k){ dd x = xlat(k); return ddadd(x, (dd){-DELTA.hi, -DELTA.lo}); } /* prime placed at cell k */

/* cell of a value c: returns k (cell index) and fractional position f in (0,1); audits the margin */
static inline long cellof(dd c, double *fout){
  dd u = ddaddd(ddmul(ddaddd(c, -1.0), RHO), 1.0 - TAU);
  double k = floor(u.hi); double f = (u.hi - k) + u.lo;
  if (f < 0){ k -= 1; f += 1; } else if (f >= 1){ k += 1; f -= 1; }
  double m = f < 1 - f ? f : 1 - f;
  if (m < minmargin){ minmargin = m; minmargin_x = c.hi; }
  if (m < FLAGTOL){ nflag++; if (fflag){ fprintf(fflag, "%.17g", c.hi); for (int i=0;i<=depth_max;i++) fprintf(fflag, " %d", stk[i]); fprintf(fflag, "\n"); } }
  *fout = f; return (long)k + 1;
}
static int inwatch(long k){ int lo=0, hi=nw-1; while (lo<=hi){ int mid=(lo+hi)/2; if (k<wa[mid]) hi=mid-1; else if (k>wb[mid]) lo=mid+1; else return 1; } return 0; }

static inline void record(dd c, int depth){   /* stk[0..depth] = factor indices, nondecreasing */
  double f; depth_max = depth; if (depth > depth_top) depth_top = depth; long k = cellof(c, &f);
  if (k < K0 || k > K1) return;
  long j = k - K0; ncomp++;
  if (cc[j] == 255) nover++; else cc[j]++;
  if (stk[0] == 0 && c1[j] < 255) c1[j]++;
  if (depth == 1 && c2[j] < 255) c2[j]++;
  { int seen = 0; for (int i = 0; i <= depth && stk[i] <= 3; i++){ int q = stk[i]; if (q >= 1 && !(seen & (1<<q))){ seen |= 1<<q; if (dv[q-1][j] < 255) dv[q-1][j]++; } } }
  if (f > lastf[j]) lastf[j] = (float)f;
  for (int i = 0; i < nck; i++) if (k == ckcell[i] && f < ckf[i]) ckpart[i]++;
  if (fwatch && nw && inwatch(k)){
    fprintf(fwatch, "%ld %.6f %d", k, f, depth+1);
    for (int i=0;i<=depth;i++) fprintf(fwatch, " %d", stk[i]);
    fprintf(fwatch, "\n");
  }
}

static dd LB, RB;
static long lower_idx(double v, long from){ long lo=from, hi=npblock; while (lo<hi){ long mid=(lo+hi)/2; if (pvh(mid) < v) lo=mid+1; else hi=mid; } return lo; }
static void dfs(dd m, long i, int depth){         /* m = product of stk[0..depth-1] */
  if (depth >= 1){
    long j = lower_idx(LB.hi / m.hi * (1 - 1e-13), i);
    for (; j < npblock; j++){ dd c = ddmul(m, pvj(j)); if (c.hi > RB.hi) break; stk[depth] = (int)j; record(c, depth); }
  }
  for (long j = i; j < npblock; j++){
    dd pj = pvj(j); dd mq = ddmul(m, pj); if (mq.hi * pj.hi > RB.hi) break;
    stk[depth] = (int)j; dfs(mq, j, depth + 1);
  }
}
static long cell_plain(dd c){ dd u = ddaddd(ddmul(ddaddd(c, -1.0), RHO), 1.0 - TAU); double k = floor(u.hi); double f = (u.hi-k)+u.lo; if (f<0) k-=1; else if (f>=1) k+=1; return (long)k + 1; }

int main(int argc, char **argv){
  if (argc < 10){ fprintf(stderr, "usage: s8gen th tl rh rl tau dfrac dabs X outprefix [watchfile]\n"); return 1; }
  T.hi = strtod(argv[1],0); T.lo = strtod(argv[2],0); RHO.hi = strtod(argv[3],0); RHO.lo = strtod(argv[4],0);
  TAU = atof(argv[5]); double dfrac = atof(argv[6]), dabs = atof(argv[7]); double X = atof(argv[8]); const char *pre = argv[9];
  DELTA = ddaddd(ddmuld(T, dfrac), dabs);
  double drho = DELTA.hi * RHO.hi;                  /* delta/t: E jump left after an early prime */
  long Kmax = cell_plain((dd){X, 0}) - 1;           /* cells with x_k <= X */
  char fn[1024]; FILE *fc, *fe, *f1, *f2, *fp, *fd[3];
  sprintf(fn, "%s.c.u8", pre); fc = fopen(fn, "wb"); sprintf(fn, "%s.e.u8", pre); fe = fopen(fn, "wb");
  sprintf(fn, "%s.c1.u8", pre); f1 = fopen(fn, "wb"); sprintf(fn, "%s.c2.u8", pre); f2 = fopen(fn, "wb"); for (int q = 0; q < 3; q++){ sprintf(fn, "%s.d%d.u8", pre, q+2); fd[q] = fopen(fn, "wb"); }
  sprintf(fn, "%s.primes.u32", pre); fp = fopen(fn, "wb"); sprintf(fn, "%s.flag", pre); fflag = fopen(fn, "w");
  if (argc > 10){ FILE *fw = fopen(argv[10], "r"); long a, b; int cap = 1024; wa = malloc(cap*sizeof(long)); wb = malloc(cap*sizeof(long));
    while (fscanf(fw, "%ld %ld", &a, &b) == 2){ if (nw == cap){ cap*=2; wa = realloc(wa, cap*sizeof(long)); wb = realloc(wb, cap*sizeof(long)); } wa[nw]=a; wb[nw]=b; nw++; }
    fclose(fw); sprintf(fn, "%s.watch.txt", pre); fwatch = fopen(fn, "w"); }
  for (double lx = 1.0; lx <= log10(X) + 1e-9 && nck < NCK; lx += 0.25){ double x = pow(10.0, lx); if (x > X) x = X;
    dd u = ddaddd(ddmul(ddaddd((dd){x,0}, -1.0), RHO), 1.0 - TAU); double k = floor(u.hi); double f = (u.hi-k)+u.lo; if (f<0){k-=1;f+=1;} else if (f>=1){k+=1;f-=1;}
    ckx[nck] = x; ckcell[nck] = (long)k + 1; ckf[nck] = f; ckpart[nck] = 0; nck++; }
  long W = 1L << 25; cc = malloc(W); c1 = malloc(W); c2 = malloc(W); for (int q = 0; q < 3; q++) dv[q] = malloc(W); lastf = malloc(W*sizeof(float));
  uint8_t *eb = malloc(W);
  double xcap = X / (1.0 + TAU*T.hi - DELTA.hi) * 1.0000001 + 10;   /* store dd values of primes below X/p1 */
  npcap = 1 << 20; PK = malloc(npcap*sizeof(uint32_t)); TH1 = 1.0 + TAU*T.hi - DELTA.hi;
  long e = 0, lastpk = 0, maxgap = 0, maxgap_k = 0, ckdone = 0, npr = 0, busy = 0, maxbusy = 0, maxbusy_k = 0;
  double supE = 0, supE_x = 1; int emax = 0;
  /* cell 1: always a prime */
  { uint8_t z = 0; fwrite(&z,1,1,fc); fwrite(&z,1,1,fe); fwrite(&z,1,1,f1); fwrite(&z,1,1,f2); for (int q = 0; q < 3; q++) fwrite(&z,1,1,fd[q]); uint32_t k1 = 1; fwrite(&k1,4,1,fp);
    PK[np++] = 1; npr = 1; lastpk = 1; supE = (1 - TAU) + drho; }
  long Kdone = 1;
  printf("s8gen: t=%.17g%+.3g rho=%.17g tau=%g delta=%.17g (delta/t=%.6g) X=%.6g Kmax=%ld\n", T.hi, T.lo, RHO.hi, TAU, DELTA.hi, drho, X, Kmax);
  while (Kdone < Kmax){
    npblock = np;
    dd B = xlat(Kdone); dd Bmax = ddmul(pvj(0), B);
    long Knext = cell_plain(Bmax) - 1;
    if (Knext <= Kdone){ Knext = Kdone + 1; dd xn = xlat(Knext); if (!(xn.hi / pvh(0) < xn.hi - DELTA.hi)){ fprintf(stderr, "block guard fails at K=%ld\n", Kdone); return 2; } }
    if (Knext > Kmax) Knext = Kmax;
    for (long a = Kdone + 1; a <= Knext; a += W){
      long b = a + W - 1; if (b > Knext) b = Knext; long n = b - a + 1;
      K0 = a; K1 = b; memset(cc, 0, n); memset(c1, 0, n); memset(c2, 0, n); for (int q = 0; q < 3; q++) memset(dv[q], 0, n); for (long i = 0; i < n; i++) lastf[i] = 0;
      LB = xlat(a - 1); LB.hi *= (1 - 1e-13); RB = xlat(b); RB.hi *= (1 + 1e-13);
      dfs((dd){1.0, 0.0}, 0, 0);
      for (long k = a; k <= b; k++){
        long j = k - a; int c = cc[j];
        double Ecell = (c > 0) ? e + (1 - TAU) + c - lastf[j] : e + (1 - TAU);
        int isp = (e == 0 && c == 0);
        while (ckdone < nck && ckcell[ckdone] == k){
          long Ny = e + k + ckpart[ckdone] + ((isp && ckf[ckdone] >= 1 - drho) ? 1 : 0);
          long piy = npr + ((isp && ckf[ckdone] >= 1 - drho) ? 1 : 0);
          double y = ckx[ckdone], Ey = Ny - (RHO.hi*(y - 1) + 1), L2 = log(y)*log(y);
          printf("CK x=%.6g N=%ld pi=%ld E=%.6f supE=%.6f (at %.10g) supE/log2x=%.4f maxgap=%ld cells (%.4f; at cell %ld) maxbusy=%ld emax=%d minmargin=%.3e nflag=%ld\n",
                 y, Ny, piy, Ey, supE, supE_x, supE/L2, maxgap, maxgap*T.hi, maxgap_k, maxbusy, emax, minmargin, nflag);
          fflush(stdout); ckdone++;
        }
        if (isp){
          Ecell = (1 - TAU) + drho; npr++; uint32_t kk = (uint32_t)k; fwrite(&kk, 4, 1, fp);
          dd pv = pval(k); if (pv.hi < xcap){ if (np == npcap){ npcap *= 2; PK = realloc(PK, npcap*sizeof(uint32_t)); } PK[np++] = (uint32_t)k; }
          long g = k - lastpk; if (g > maxgap){ maxgap = g; maxgap_k = k; } lastpk = k; busy = 0;
        } else { e = e + c - 1; busy++; if (busy > maxbusy){ maxbusy = busy; maxbusy_k = k; } }
        if (Ecell > supE){ supE = Ecell; supE_x = xlat(k - 1).hi + (c > 0 ? lastf[j] : 0) * T.hi; }
        if (e > emax) emax = (int)e;
        if (e > 255){ fprintf(stderr, "e overflow at %ld\n", k); return 3; }
        eb[j] = (uint8_t)e;
      }
      fwrite(cc, 1, n, fc); fwrite(eb, 1, n, fe); fwrite(c1, 1, n, f1); fwrite(c2, 1, n, f2); for (int q = 0; q < 3; q++) fwrite(dv[q], 1, n, fd[q]);
    }
    fprintf(stderr, "block K %ld..%ld (x %.4g..%.4g) primes %ld stored %ld comps %ld minmargin %.3e flags %ld\n", Kdone+1, Knext, xlat(Kdone).hi, xlat(Knext).hi, npr, np, ncomp, minmargin, nflag);
    Kdone = Knext;
  }
  printf("FINAL Kmax=%ld x_K=%.10g N(x_K)=%ld pi=%ld composites=%ld supE=%.6f at %.10g supE/log2X=%.5f maxgap=%ld cells (%.4f) at cell %ld maxbusy=%ld at cell %ld emax=%d e_K=%ld\n",
         Kmax, xlat(Kmax).hi, e + Kmax + 1, npr, ncomp, supE, supE_x, supE/(log(X)*log(X)), maxgap, maxgap*T.hi, maxgap_k, maxbusy, maxbusy_k, emax, e);
  printf("AUDIT minmargin=%.4e at %.10g flagged(<%.0e)=%ld count-overflow=%ld max-factors=%d\n", minmargin, minmargin_x, FLAGTOL, nflag, nover, depth_top + 1);
  printf("first primes:"); for (int i = 0; i < 6 && i < np; i++) printf(" %.10f", pvj(i).hi); printf("\n");
  fclose(fc); fclose(fe); fclose(f1); fclose(f2); for (int q = 0; q < 3; q++) fclose(fd[q]); fclose(fp); fclose(fflag); if (fwatch) fclose(fwatch);
  return 0;
}
