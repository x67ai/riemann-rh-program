/* stats.c — U7-patterns: streaming statistics of the S8 cell arrays written by s8gen.
   Usage: stats prefix t rho tau p1 X [ntop]
   Bands: half-decades in x. Per band: moments of c, c1 (spf = p1), c2 (two factors), e; histograms of e and c; autocorrelation
   of c, c1 and of the prime indicator at a lag list; window sums of length h = b*2^i (b = 1,3,5,7) for c, c1, c-c1, c2, primes:
   mean, variance, covariance(c1, c-c1); e-excursions (maximal runs e>0): height, length, build-up sums; prime-gap histogram.
   Global top excursions by height. Output: text lines tagged BAND/LAG/WIN/EXC/GAP/TOP. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <sys/stat.h>

static uint8_t *mapf(const char *pre, const char *suf, long *n){
  char fn[1024]; sprintf(fn, "%s%s", pre, suf); int fd = open(fn, O_RDONLY); if (fd < 0){ perror(fn); exit(1); }
  struct stat st; fstat(fd, &st); *n = st.st_size; void *p = mmap(0, st.st_size, PROT_READ, MAP_SHARED, fd, 0);
  if (p == MAP_FAILED){ perror("mmap"); exit(1); } return (uint8_t*)p; }

#define NB 4
#define NLEV 30
static const int BASES[NB] = {1, 3, 5, 7};
typedef struct { double n, s, ss, s1, ss1, sr, ssr, s1r, s2, ss2, sp, ssp; } wacc;   /* window accumulators */
typedef struct { long a, peak, b, h, lb; long sc, sc1, sc2; } exc;
#define NLAG 27
static const long LAGS[NLAG] = {1,2,3,4,5,6,8,10,12,16,20,24,32,48,64,96,128,192,256,512,1024,2048,4096,8192,16384,32768,65536};

int main(int argc, char **argv){
  if (argc < 7){ fprintf(stderr, "usage: stats prefix t rho tau p1 X [ntop]\n"); return 1; }
  const char *pre = argv[1]; double t = atof(argv[2]), rho = atof(argv[3]), tau = atof(argv[4]), p1 = atof(argv[5]), X = atof(argv[6]);
  int ntop = argc > 7 ? atoi(argv[7]) : 400;
  long n, n2; uint8_t *c = mapf(pre, ".c.u8", &n), *e = mapf(pre, ".e.u8", &n2), *c1 = mapf(pre, ".c1.u8", &n2), *c2 = mapf(pre, ".c2.u8", &n2);
  /* cell k (1-based) is array index k-1 */
  int nband = 0; long bk[64]; double bx[64];
  for (double lx = 1.0; lx <= log10(X) + 1e-9; lx += 0.5){ double x = pow(10, lx); long k = (long)floor((x - 1)*rho + 1 - tau); if (k > n) k = n; bx[nband] = x; bk[nband++] = k; }
  exc *top = calloc(ntop, sizeof(exc)); int ntopn = 0;
  printf("# stats %s n=%ld t=%.10g rho=%.10g tau=%g p1=%.10g bands=%d\n", pre, n, t, rho, tau, p1, nband - 1);
  for (int bi = 0; bi + 1 < nband; bi++){
    long ka = bk[bi], kb = bk[bi+1];          /* band = cells ka+1..kb (indices ka..kb-1) */
    if (kb - ka < 16) continue;
    double S[8] = {0}; long he[256] = {0}, hc[256] = {0}; long np = 0;
    for (long i = ka; i < kb; i++){ double cv = c[i], ev = e[i], v1 = c1[i];
      S[0] += cv; S[1] += cv*cv; S[2] += v1; S[3] += v1*v1; S[4] += c2[i]; S[5] += ev; S[6] += ev*ev; he[e[i]]++; hc[c[i]]++;
      int isp = (c[i] == 0) && (i == 0 || e[i-1] == 0); np += isp; S[7] += v1*(cv - v1); }
    double m = kb - ka;
    printf("BAND %d x=[%.4g,%.4g) cells=%ld mean_c=%.6f var_c=%.6f mean_c1=%.6f var_c1=%.6f mean_c2=%.6f mean_e=%.6f var_e=%.6f prime_frac=%.6f cov_c1_rest=%.6f\n",
      bi, bx[bi], bx[bi+1], kb - ka, S[0]/m, S[1]/m - (S[0]/m)*(S[0]/m), S[2]/m, S[3]/m - (S[2]/m)*(S[2]/m), S[4]/m, S[5]/m, S[6]/m - (S[5]/m)*(S[5]/m), np/m,
      S[7]/m - (S[2]/m)*((S[0]-S[2])/m));
    printf("EHIST %d", bi); for (int h = 0; h < 256; h++) if (he[h]) printf(" %d:%ld", h, he[h]); printf("\n");
    printf("CHIST %d", bi); for (int h = 0; h < 256; h++) if (hc[h]) printf(" %d:%ld", h, hc[h]); printf("\n");
    /* lags */
    double mc = S[0]/m, vc = S[1]/m - mc*mc, mc1 = S[2]/m, vc1 = S[3]/m - mc1*mc1, mp = np/m, vp = mp - mp*mp;
    for (int li = 0; li < NLAG; li++){ long L = LAGS[li]; if (L >= (kb - ka)/4) break;
      uint64_t s = 0, s1 = 0, sp = 0; long cnt = kb - ka - L;
      for (long i = ka; i < kb - L; i++){ s += (uint32_t)c[i]*c[i+L]; s1 += (uint32_t)c1[i]*c1[i+L]; }
      for (long i = ka > 0 ? ka : 1; i < kb - L; i++){ int a = (c[i]==0 && e[i-1]==0), b = (c[i+L]==0 && e[i+L-1]==0); sp += a & b; }
      printf("LAG %d %ld r_c=%.6f r_c1=%.6f r_p=%.6f\n", bi, L, ((double)s/cnt - mc*mc)/vc, ((double)s1/cnt - mc1*mc1)/vc1, ((double)sp/cnt - mp*mp)/vp);
    }
    /* windows: hierarchical sums for bases b*2^i */
    for (int bb = 0; bb < NB; bb++){
      int B = BASES[bb]; wacc W[NLEV]; memset(W, 0, sizeof W);
      long cur[NLEV][4]; int have[NLEV]; memset(have, 0, sizeof have);
      long acc[4] = {0}; int fill = 0;
      for (long i = ka; i < kb; i++){
        int isp = (c[i] == 0) && (i == 0 || e[i-1] == 0);
        acc[0] += c[i]; acc[1] += c1[i]; acc[2] += c2[i]; acc[3] += isp; fill++;
        if (fill < B) continue;
        long v[4] = {acc[0], acc[1], acc[2], acc[3]}; acc[0]=acc[1]=acc[2]=acc[3]=0; fill = 0;
        for (int lev = 0; lev < NLEV; lev++){
          double A = v[0], A1 = v[1], R = v[0]-v[1], A2 = v[2], P = v[3];
          W[lev].n++; W[lev].s += A; W[lev].ss += A*A; W[lev].s1 += A1; W[lev].ss1 += A1*A1; W[lev].sr += R; W[lev].ssr += R*R; W[lev].s1r += A1*R;
          W[lev].s2 += A2; W[lev].ss2 += A2*A2; W[lev].sp += P; W[lev].ssp += P*P;
          if (!have[lev]){ memcpy(cur[lev], v, sizeof v); have[lev] = 1; break; }
          for (int q = 0; q < 4; q++) v[q] += cur[lev][q]; have[lev] = 0;
        }
      }
      for (int lev = 0; lev < NLEV; lev++){ if (W[lev].n < 8) break; double N = W[lev].n;
        double mA = W[lev].s/N, vA = W[lev].ss/N - mA*mA, m1 = W[lev].s1/N, v1 = W[lev].ss1/N - m1*m1, mR = W[lev].sr/N, vR = W[lev].ssr/N - mR*mR;
        double c1r = W[lev].s1r/N - m1*mR, m2 = W[lev].s2/N, v2 = W[lev].ss2/N - m2*m2, mP = W[lev].sp/N, vP = W[lev].ssp/N - mP*mP;
        printf("WIN %d h=%ld nwin=%.0f mean=%.4f var=%.4f fano=%.5f mean1=%.4f var1=%.4f meanR=%.4f varR=%.4f cov1R=%.4f mean2=%.4f var2=%.4f meanP=%.4f varP=%.4f\n",
          bi, (long)B << lev, N, mA, vA, vA/mA, m1, v1, mR, vR, c1r, m2, v2, mP, vP);
      }
    }
  }
  /* excursions (maximal runs with e > 0), prime gaps: one global pass */
  static long exh[64][256], exl[64][32], gh[64][1025]; static double xs[64][6];
  long Cc = 0, Cc1 = 0, Cc2 = 0, bC = 0, bC1 = 0, bC2 = 0, pC = 0, pC1 = 0, pC2 = 0, lastp = -1, minh = -1; int mini = 0;
  int inexc = 0, band = 0; exc cur = {0};
  for (long i = 0; i < n; i++){
    while (band + 1 < nband && i >= bk[band+1]) band++;
    long cb = Cc, cb1 = Cc1, cb2 = Cc2; Cc += c[i]; Cc1 += c1[i]; Cc2 += c2[i];
    int isp = (c[i] == 0) && (i == 0 || e[i-1] == 0);
    if (isp){ if (lastp >= 0){ long g = i - lastp; gh[band][g > 1024 ? 1024 : g]++; } lastp = i; }
    if (e[i] > 0){
      if (!inexc){ inexc = 1; cur.a = i; cur.h = e[i]; cur.peak = i; bC = cb; bC1 = cb1; bC2 = cb2; pC = Cc; pC1 = Cc1; pC2 = Cc2; }
      else if (e[i] > cur.h){ cur.h = e[i]; cur.peak = i; pC = Cc; pC1 = Cc1; pC2 = Cc2; }
    } else if (inexc){
      inexc = 0; cur.b = i; cur.lb = cur.peak - cur.a + 1; cur.sc = pC - bC; cur.sc1 = pC1 - bC1; cur.sc2 = pC2 - bC2;
      if (cur.sc - cur.lb != cur.h){ fprintf(stderr, "identity h = sum(c-1) fails at %ld\n", i); }
      int ba = 0; while (ba + 1 < nband && cur.a >= bk[ba+1]) ba++;
      exh[ba][cur.h]++; long L = cur.b - cur.a; int lg = 0; while ((1L << (lg+1)) <= L && lg < 31) lg++; exl[ba][lg]++;
      double X1 = cur.sc1 - cur.lb / p1; xs[ba][0]++; xs[ba][1] += cur.h; xs[ba][2] += (double)cur.h*cur.h; xs[ba][3] += X1; xs[ba][4] += X1*X1; xs[ba][5] += cur.h*X1;
      if (ntopn < ntop){ top[ntopn++] = cur; if (ntopn == ntop){ minh = 1L<<60; for (int q = 0; q < ntop; q++){ long key = top[q].h*100000 + (top[q].b - top[q].a); if (key < minh){ minh = key; mini = q; } } } }
      else { long key = cur.h*100000 + (cur.b - cur.a); if (key > minh){ top[mini] = cur; minh = 1L<<60; for (int q = 0; q < ntop; q++){ long k2 = top[q].h*100000 + (top[q].b - top[q].a); if (k2 < minh){ minh = k2; mini = q; } } } }
    }
  }
  for (int bi = 0; bi + 1 < nband; bi++){
    if (xs[bi][0] < 1) continue; double N = xs[bi][0], mh = xs[bi][1]/N, mx = xs[bi][3]/N, vh = xs[bi][2]/N - mh*mh, vx = xs[bi][4]/N - mx*mx;
    printf("EXC %d nexc=%.0f mean_h=%.4f var_h=%.4f mean_X1=%.4f var_X1=%.4f corr_h_X1=%.4f hhist", bi, N, mh, vh, mx, vx, (xs[bi][5]/N - mh*mx)/sqrt(vh*vx));
    for (int h = 0; h < 256; h++) if (exh[bi][h]) printf(" %d:%ld", h, exh[bi][h]);
    printf(" lhist"); for (int l = 0; l < 32; l++) if (exl[bi][l]) printf(" %d:%ld", 1 << l, exl[bi][l]); printf("\n");
    printf("GAP %d", bi); for (int g = 0; g <= 1024; g++) if (gh[bi][g]) printf(" %d:%ld", g, gh[bi][g]); printf("\n");
  }
  /* top excursions, sorted by height then length */
  for (int a = 0; a < ntopn; a++) for (int b = a + 1; b < ntopn; b++){ long ka2 = top[a].h*100000 + (top[a].b - top[a].a), kb2 = top[b].h*100000 + (top[b].b - top[b].a); if (kb2 > ka2){ exc tmp = top[a]; top[a] = top[b]; top[b] = tmp; } }
  for (int a = 0; a < ntopn; a++){ exc *x = &top[a];
    printf("TOP %d h=%ld cell_a=%ld cell_peak=%ld cell_b=%ld x_a=%.10g len=%ld lbuild=%ld sumc=%ld sumc1=%ld sumc2=%ld X1=%.4f\n", a, x->h, x->a + 1, x->peak + 1, x->b + 1,
      1 + (x->a + tau)*t, x->b - x->a, x->lb, x->sc, x->sc1, x->sc2, x->sc1 - x->lb/p1); }
  return 0;
}
