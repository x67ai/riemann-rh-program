/* s7gen.c -- S7(rho): integer-level feedback that may act only at prime powers (unit local-greedy-s40).
   Rule (BRIEF): walk n = 2,3,...; A(n) = #representations of n by the g-primes chosen so far; if n = p^k,
     m_n = max(0, floor(rho(n-1) + 1 - N(n-1) - A(n) + 1/2)), else m_n = 0;  a_n = A(n) + m_n,  N(n) = N(n-1) + a_n.
   Every g-prime is a prime power, so a_n = prod_{p^e || n} c_p(e), c_p(e) = [u^e] prod_k (1-u^k)^(-m_{p^k}) (multiplicative).
   Exact integer arithmetic for the rule: rho = num/den, int128.  Segmented: segment [L, R) with R - L <= L, so every
   composite non-prime-power n in it has all prime-power factors <= n/2 < L, i.e. already decided; prime powers in the
   segment are decided in increasing order (their A(n) = c_p^{old}(e) depends only on m_{p^k}, k < e).
   g = mu * a (multiplicative): g(p^e) = c_p(e) - c_p(e-1).  E(n) := N(n) - rho(n-1) - 1 (sup over [n,n+1) at n,
   inf = E(n) - rho);  psi_P(x) = sum_{p^e <= x} Lambda_P(p^e), Lambda_P(p^e) = log p * sum_{k|e} k m_{p^k}.
   Exact decomposition at integers: E(n) = Tt(n) + W(n) + rho - 1, Tt(n) = n(S1(n) - rho), S1(n) = sum_{d<=n} g(d)/d,
   W(n) = -sum_{d<=n} g(d){n/d}  (W is obtained as E - Tt - rho + 1; S1 by double-double accumulation).
   Variants: 0 standard; 1 act only at primes (m_{p^k} = 0, k >= 2); 2 cap m <= 2; 3 look-ahead at primes
   (m_p in 0..4 minimizing |Ep(2p)| + |Ep(3p)|, Ep(kp) = E(p-1) + sum_{j<=k}(m a_j - rho)); 4 lambda-rule (m_p in {0,2};
   a refused p gets m_{p^2} = 1, so g is completely multiplicative with g(p) = -1 or +1).
   Usage: s7gen num den X variant label outdir [dump]
     dump bit 1: a_n as uint16 -> outdir/a_<label>.u16 ; bit 2: g_n as int16 -> outdir/g_<label>.i16 ;
     bit 4: non-default prime-power decisions (uint32 n, uint32 m) -> outdir/x_<label>.u32
   Build: cc -O2 -o s7gen s7gen.c -lm */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
typedef __int128 i128;
#define KM 34
#define BPD 20
static int64_t NUM, DEN; static uint64_t X; static int VAR;
static uint32_t *sp; static long nsp;           /* small primes <= sqrt(X) */
static int32_t *spi;                             /* index of small prime p, or -1 */
static uint64_t (*poly)[KM]; static uint16_t (*mloc)[KM]; static int *kmax;
static uint8_t *mq;                              /* m_q for odd primes q <= X/2, index q>>1 */
static long hm[66]; static int64_t maxm = 0; static uint64_t maxmn = 0; static double summ[12];
static double s1hi = 0, s1lo = 0, pshi = 0, pslo = 0;
static inline void dd(double *hi, double *lo, double x){ double s = *hi + x, bp = s - *hi; *lo += (*hi - (s - bp)) + (x - bp); *hi = s; }
static uint64_t isqrt64(uint64_t v){ uint64_t r = (uint64_t)sqrt((double)v); while(r*r > v) r--; while((r+1)*(r+1) <= v) r++; return r; }
static int64_t floordiv(i128 t, i128 d){ return (int64_t)(t >= 0 ? t/d : -((-t + d - 1)/d)); }
/* E(n-1)*den as exact integer given N = N(n-1) */
static inline i128 Eden_prev(uint64_t n, int64_t N){ return (i128)DEN*N - (i128)NUM*(int64_t)(n-2) - DEN; }
/* decision at the prime power n = p^e, A = A(n), N = N(n-1); ip = small-prime index or -1 */
static int64_t decide(uint64_t n, uint64_t p, int e, int64_t A, int64_t N, int ip){
  i128 t = (i128)2*NUM*(int64_t)(n-1) + (i128)2*DEN*(1 - N - A) + DEN;
  int64_t m = floordiv(t, (i128)2*DEN); if(m < 0) m = 0;
  if(VAR == 1 && e >= 2) m = 0;
  if(VAR == 2 && m > 2) m = 2;
  if(VAR == 4){
    if(e == 1){ i128 D1 = (i128)NUM*(int64_t)(n-1) - (i128)DEN*N; m = (D1 >= 0) ? 2 : 0; } /* D = rho(n-1)+1-N >= 1 -> 2 */
    else if(e == 2) m = (mloc[ip][1] == 0) ? 1 : 0;
    else m = 0;
  }
  if(VAR == 3 && e == 1 && p > 3){
    int64_t a2 = (int64_t)poly[spi[2]][1], a3 = (int64_t)poly[spi[3]][1];
    i128 E0 = Eden_prev(n, N), best = -1, bt = 0; int64_t bm = 0;
    for(int64_t mm = 0; mm <= 4; mm++){
      i128 e1 = E0 + (i128)DEN*mm - NUM, e2 = e1 + (i128)DEN*mm*a2 - NUM, e3 = e2 + (i128)DEN*mm*a3 - NUM;
      i128 c = (e2 < 0 ? -e2 : e2) + (e3 < 0 ? -e3 : e3), tb = e1 < 0 ? -e1 : e1;
      if(best < 0 || c < best || (c == best && tb < bt)){ best = c; bm = mm; bt = tb; }
    }
    m = bm;
  }
  return m;
}
int main(int argc, char **argv){
  if(argc < 7){ fprintf(stderr, "usage: s7gen num den X variant label outdir [dump]\n"); return 1; }
  NUM = atoll(argv[1]); DEN = atoll(argv[2]); X = strtoull(argv[3], 0, 10); VAR = atoi(argv[4]);
  const char *lab = argv[5], *od = argv[6]; int dump = argc > 7 ? atoi(argv[7]) : 0;
  double rho = (double)NUM/(double)DEN; uint64_t sq = isqrt64(X);
  uint8_t *cmp = calloc(sq + 2, 1); spi = malloc((sq + 2)*sizeof(int32_t)); sp = malloc((sq + 2)*sizeof(uint32_t)); nsp = 0;
  for(uint64_t i = 0; i <= sq + 1; i++) spi[i] = -1;
  for(uint64_t i = 2; i <= sq; i++) if(!cmp[i]){ spi[i] = (int32_t)nsp; sp[nsp++] = (uint32_t)i; for(uint64_t j = i*i; j <= sq; j += i) cmp[j] = 1; }
  poly = calloc(nsp, sizeof *poly); mloc = calloc(nsp, sizeof *mloc); kmax = malloc(nsp*sizeof(int));
  for(long i = 0; i < nsp; i++){ poly[i][0] = 1; uint64_t q = 1; int k = 0; while(q <= X/sp[i]){ q *= sp[i]; k++; } kmax[i] = k; }
  mq = calloc((X/2)/2 + 2, 1); if(!mq){ fprintf(stderr, "oom mq\n"); return 1; }
  const uint64_t SMAX = 1ull << 22;
  uint32_t *rem = malloc(SMAX*4), *ppp = malloc(SMAX*4), *dv = malloc(SMAX*4); uint64_t *av = malloc(SMAX*8); int64_t *gv = malloc(SMAX*8);
  uint8_t *ppe = malloc(SMAX), *nd = malloc(SMAX);
  uint16_t *abuf = malloc(SMAX*2); int16_t *gbuf = malloc(SMAX*2);
  FILE *fa = NULL, *fg = NULL, *fx = NULL; char fn[4096];
  if(dump & 1){ snprintf(fn, sizeof fn, "%s/a_%s.u16", od, lab); fa = fopen(fn, "wb"); uint16_t z[2] = {0, 1}; fwrite(z, 2, 2, fa); }
  if(dump & 2){ snprintf(fn, sizeof fn, "%s/g_%s.i16", od, lab); fg = fopen(fn, "wb"); int16_t z[2] = {0, 1}; fwrite(z, 2, 2, fg); }
  if(dump & 4){ snprintf(fn, sizeof fn, "%s/x_%s.u32", od, lab); fx = fopen(fn, "wb"); }
  int nb = (int)(BPD*log10((double)X)) + 2;
  double *Emax = malloc(nb*8), *Emin = malloc(nb*8), *E2 = malloc(nb*8), *Pmax = malloc(nb*8), *Gmx = malloc(nb*8), *Gmn = malloc(nb*8);
  double *Tmax = malloc(nb*8), *Wmax = malloc(nb*8), *T2 = malloc(nb*8), *W2 = malloc(nb*8); long *cnt = calloc(nb, sizeof(long));
  for(int i = 0; i < nb; i++){ Emax[i] = -1e300; Emin[i] = 1e300; E2[i] = T2[i] = W2[i] = 0; Pmax[i] = Tmax[i] = Wmax[i] = 0; Gmx[i] = -1e300; Gmn[i] = 1e300; }
  long pm[12][7], pk[12][7]; memset(pm, 0, sizeof pm); memset(pk, 0, sizeof pk);
  int64_t N = 1, Mg = 1; s1hi = 1.0; uint64_t maxa = 1, maxan = 1, nover = 0, ngp = 0, totm = 0; double maxrat = 1; int sat = 0;
  int b = (int)(BPD*log10(2.0)); uint64_t bnext = (uint64_t)ceil(pow(10.0, (b + 1.0)/BPD)); int dec = 0; uint64_t dnext = 10;
  double supE = -1e300, infE = 1e300, supMg = 0;
  printf("# s7gen num=%lld den=%lld rho=%.12g X=%llu variant=%d label=%s\n", (long long)NUM, (long long)DEN, rho, (unsigned long long)X, VAR, lab);
  uint64_t L = 2;
  while(L <= X){
    uint64_t S = L < SMAX ? L : SMAX, R = L + S; if(R > X + 1) R = X + 1; uint64_t len = R - L;
    for(uint64_t i = 0; i < len; i++){ rem[i] = (uint32_t)(L + i); av[i] = 1; gv[i] = 1; ppp[i] = 0; ppe[i] = 0; nd[i] = 0; dv[i] = 1; }
    uint64_t sr = isqrt64(R - 1);
    for(long ip = 0; ip < nsp && sp[ip] <= sr; ip++){
      uint32_t p = sp[ip]; uint64_t st = ((L + p - 1)/p)*p;
      for(uint64_t n = st; n < R; n += p){
        uint64_t i = n - L; int e = 0; uint32_t r = rem[i];
        do { r /= p; e++; } while(r % p == 0);
        rem[i] = r;
        if(r == 1 && nd[i] == 0){ ppp[i] = p; ppe[i] = (uint8_t)e; }
        else { nd[i]++; av[i] *= poly[ip][e]; gv[i] *= (int64_t)poly[ip][e] - (int64_t)poly[ip][e-1]; dv[i] *= (uint32_t)(e + 1); }
      }
    }
    for(uint64_t i = 0; i < len; i++){
      if(ppp[i]) continue; uint32_t r = rem[i];
      if(r > 1){ if(nd[i] == 0){ ppp[i] = r; ppe[i] = 1; }
                 else { uint64_t v = mq[r >> 1]; av[i] *= v; gv[i] *= (int64_t)v - 1; dv[i] *= 2; } }
    }
    for(uint64_t i = 0; i < len; i++){
      uint64_t n = L + i; int64_t a, g; double lam = 0; uint64_t dn;
      if(ppp[i]){
        uint64_t p = ppp[i]; int e = ppe[i]; int ip = (p <= sq) ? spi[p] : -1;
        int64_t A = (ip >= 0) ? (int64_t)poly[ip][e] : 0, cprev = (ip >= 0) ? (int64_t)poly[ip][e-1] : 1;
        int64_t m = decide(n, p, e, A, N, ip);
        if(ip >= 0){ mloc[ip][e] = (uint16_t)m; for(int64_t c = 0; c < m; c++) for(int j = e; j <= kmax[ip]; j++) poly[ip][j] += poly[ip][j-e];
                     int64_t s = 0; for(int k = 1; k <= e; k++) if(e % k == 0) s += (int64_t)k*mloc[ip][k]; lam = log((double)p)*(double)s; }
        else lam = log((double)p)*(double)m;
        if(e == 1 && (p & 1) && p <= X/2){ if(m > 255){ fprintf(stderr, "m > 255 at %llu\n", (unsigned long long)n); return 2; } mq[p >> 1] = (uint8_t)m; }
        a = A + m; g = a - cprev; dn = (uint64_t)e + 1;
        if(m > 0){ ngp++; totm += m; }
        if(e == 1){ pm[dec][m < 6 ? m : 6]++; hm[m < 65 ? m : 65]++; summ[dec] += (double)m; if(m > maxm){ maxm = m; maxmn = n; } } else pk[dec][m < 6 ? m : 6]++;
        if(fx && ((e == 1 && m != 1) || (e >= 2 && m != 0))){ uint32_t pr[2] = {(uint32_t)n, (uint32_t)m}; fwrite(pr, 4, 2, fx); }
      } else { a = (int64_t)av[i]; g = gv[i]; dn = dv[i]; }
      N += a; Mg += g; dd(&s1hi, &s1lo, (double)g/(double)n); if(lam != 0) dd(&pshi, &pslo, lam);
      if((uint64_t)a > maxa){ maxa = (uint64_t)a; maxan = n; }
      if((uint64_t)a > dn) nover++; if((double)a/(double)dn > maxrat) maxrat = (double)a/(double)dn;
      if(fa){ abuf[i] = a > 65535 ? (sat = 1, 65535) : (uint16_t)a; }
      if(fg){ gbuf[i] = (g > 32767 || g < -32768) ? (sat |= 2, (int16_t)(g > 0 ? 32767 : -32768)) : (int16_t)g; }
      if(n >= bnext){ b = (int)(BPD*log10((double)n)); if(b >= nb) b = nb - 1; bnext = (uint64_t)ceil(pow(10.0, (b + 1.0)/BPD)); }
      i128 Ed = (i128)DEN*N - (i128)NUM*(int64_t)(n - 1) - DEN; double E = (double)Ed/(double)DEN;
      if(E > Emax[b]) Emax[b] = E; if(E - rho < Emin[b]) Emin[b] = E - rho; E2[b] += E*E; cnt[b]++;
      if(E > supE){ if(E > 50 && E > 1.02*supE) printf("rec n=%llu E=%.2f a_n=%lld\n", (unsigned long long)n, E, (long long)a); supE = E; }
      if(E - rho < infE) infE = E - rho;
      double psi = pshi + pslo, d1 = fabs(psi - (double)n), d2 = fabs(psi - (double)(n + 1)); if(d2 > d1) d1 = d2; if(d1 > Pmax[b]) Pmax[b] = d1;
      if((double)Mg > Gmx[b]) Gmx[b] = (double)Mg; if((double)Mg < Gmn[b]) Gmn[b] = (double)Mg; if(fabs((double)Mg) > supMg) supMg = fabs((double)Mg);
      double Tt = (double)n*((s1hi - rho) + s1lo), W = E - Tt - rho + 1.0;
      if(fabs(Tt) > Tmax[b]) Tmax[b] = fabs(Tt); if(fabs(W) > Wmax[b]) Wmax[b] = fabs(W); T2[b] += Tt*Tt; W2[b] += W*W;
      if(n == dnext - 1 || n == X){
        printf("# n=%llu N=%lld E=%.4f supE=%.4f infE=%.4f Mg=%lld psi-x=%.2f Tt=%.4f W=%.4f gp=%llu maxa=%llu@%llu\n", (unsigned long long)n, (long long)N, E, supE, infE,
               (long long)Mg, psi - (double)n, Tt, W, (unsigned long long)ngp, (unsigned long long)maxa, (unsigned long long)maxan); fflush(stdout);
      }
      if(n == dnext - 1){ dec++; dnext *= 10; }
    }
    if(fa) fwrite(abuf, 2, len, fa); if(fg) fwrite(gbuf, 2, len, fg);
    L = R;
  }
  if(fa) fclose(fa); if(fg) fclose(fg); if(fx) fclose(fx);
  printf("# summary: X=%llu N(X)=%lld g-prime sites=%llu total mult=%llu max a_n=%llu at n=%llu  #(a_n>d(n))=%llu  max a_n/d(n)=%.4f sat=%d\n",
         (unsigned long long)X, (long long)N, (unsigned long long)ngp, (unsigned long long)totm, (unsigned long long)maxa, (unsigned long long)maxan,
         (unsigned long long)nover, maxrat, sat);
  printf("# summary: supE=%.6f infE=%.6f sup|Mg|=%.0f Mg(X)=%lld S1(X)-rho=%.6e psi(X)-X=%.4f\n", supE, infE, supMg, (long long)Mg, (s1hi - rho) + s1lo, pshi + pslo - (double)X);
  printf("# max m_p=%lld at p=%llu; histogram of m_p over all primes (m=0..64, >=65):", (long long)maxm, (unsigned long long)maxmn);
  for(int j = 0; j < 66; j++) printf(" %ld", hm[j]); printf("\n");
  for(int d = 0; d < 12; d++){ long s = 0; for(int j = 0; j < 7; j++) s += pm[d][j]; if(s) printf("# decade %d: primes %ld, mean m_p %.4f\n", d, s, summ[d]/s); }
  printf("# primes by decade: dec  m=0 m=1 m=2 m=3 m=4 m=5 m>=6 | higher powers p^k (k>=2): m=0 m=1 m=2 m=3 m=4 m=5 m>=6\n");
  for(int d = 0; d < 12; d++){ long s = 0; for(int j = 0; j < 7; j++) s += pm[d][j] + pk[d][j]; if(!s) continue;
    printf("D %d", d); for(int j = 0; j < 7; j++) printf(" %ld", pm[d][j]); printf(" |"); for(int j = 0; j < 7; j++) printf(" %ld", pk[d][j]); printf("\n"); }
  printf("# bin_lo Emax Emin Erms sup|psi-x| Mgmax Mgmin sup|Tt| sup|W| Ttrms Wrms\n");
  for(int i = 0; i < nb; i++) if(cnt[i]) printf("%.4e %.6g %.6g %.6g %.6g %.6g %.6g %.6g %.6g %.6g %.6g\n", pow(10.0, (double)i/BPD), Emax[i], Emin[i], sqrt(E2[i]/cnt[i]),
      Pmax[i], Gmx[i], Gmn[i], Tmax[i], Wmax[i], sqrt(T2[i]/cnt[i]), sqrt(W2[i]/cnt[i]));
  return 0;
}
