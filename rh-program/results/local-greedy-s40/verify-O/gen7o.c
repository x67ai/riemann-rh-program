// gen7o.c -- read-O (Session 41) independent generator of S7(rho) and its capped variant.
// Written from NOTE.md §1 Definition only (no code from verify/ consulted or copied).
// Walk n = 2,3,...: A(n) = #representations of n by g-primes chosen so far; if n = p^k,
// m_n = max(0, floor(rho(n-1) + 1 - N(n-1) - A(n) + 1/2)), then (cap>0) m_n = min(m_n, cap); else m_n = 0.
// a_n = A(n) + m_n, N(n) = N(n-1) + a_n. All g-primes are prime powers => a multiplicative:
// a(p^e) = c_p(e) = [u^e] prod_k (1-u^k)^(-m_{p^k}).  Method: segmented multiplicative sieve on [L,R), R <= 2L.
// rho = num/den: m = floor(Y / (2 den)), Y = 2 num (n-1) + 2 den (1 - N - A) + den (exact __int128).
// E(n) = N(n) - rho(n-1) - 1 kept exactly as den*E (int64). C(n) = N(n) - rho n, den*C = den*N - num*n.
// usage: gen7o num den cap X dumpfile|-   (dump: uint16 a_n, n = 0..X, a_0 = 0)
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
typedef __int128 i128;
#define EMAX 34
static int64_t num, den; static int cap; static uint64_t X;
static uint32_t *sp; static int nsp; static int32_t *sidx; static uint64_t SQ;
static uint64_t *cS; static int64_t *gS, *muS; static uint16_t *mS; static int *emaxS; // per small prime local data
static uint8_t *mtab; // m_P for odd P <= X/2, index P>>1
static int64_t N = 1, denE_max = INT64_MIN, denE_min = INT64_MAX, Mg = 1, MP = 1;
static double psi = 0, psic = 0; // Neumaier sum
static void addpsi(double v){ double t = psi + v; if (fabs(psi) >= fabs(v)) psic += (psi - t) + v; else psic += (v - t) + psi; psi = t; }
static uint64_t maxa = 0, maxa_n = 0, maxm = 0, maxm_n = 0;
// stats
static double b20_supE[400], b20_infE[400], b20_absE[400], b20_psi[400], b20_mg[400], b20_mp[400]; static uint64_t b20_maxa[400];
static double fineC[20000]; static uint64_t fineC_n[20000];
static uint64_t dcnt[12][6], dsum[12], dhpp[12], dmaxm[12];
static int bin20(uint64_t n){ return (int)floor(20.0*log10((double)n) + 1e-12); }
static uint64_t ceilpow(double e){ double v = pow(10.0, e); uint64_t r = (uint64_t)ceil(v - 1e-9); return r; }
static int64_t rulem(uint64_t n, uint64_t A){
  i128 Y = (i128)2*num*(i128)(n-1) + (i128)2*den*((i128)1 - (i128)N - (i128)A) + (i128)den;
  if (Y < 0) return 0; i128 m = Y / (2*den); if (cap > 0 && m > cap) m = cap; return (int64_t)m; }
static void small_primes(void){
  SQ = (uint64_t)sqrt((double)X); while ((SQ+1)*(SQ+1) <= X) SQ++; while (SQ*SQ > X) SQ--;
  uint8_t *c = calloc(SQ+2, 1); sp = malloc(sizeof(uint32_t)*(SQ+2)); sidx = malloc(sizeof(int32_t)*(SQ+2));
  for (uint64_t i = 0; i <= SQ+1; i++) sidx[i] = -1;
  for (uint64_t i = 2; i <= SQ; i++) if (!c[i]) { sidx[i] = nsp; sp[nsp++] = (uint32_t)i; for (uint64_t j = i*i; j <= SQ; j += i) c[j] = 1; }
  free(c);
  cS = calloc((size_t)nsp*EMAX, 8); gS = calloc((size_t)nsp*EMAX, 8); muS = calloc((size_t)nsp*EMAX, 8);
  mS = calloc((size_t)nsp*EMAX, 2); emaxS = calloc(nsp, sizeof(int));
  for (int i = 0; i < nsp; i++) { uint64_t q = 1; int e = 0; while (q <= X / sp[i]) { q *= sp[i]; e++; } emaxS[i] = e;
    cS[(size_t)i*EMAX] = 1; muS[(size_t)i*EMAX] = 1; gS[(size_t)i*EMAX] = 1; }
}
static int b20cur = -1; static uint64_t b20next = 0; static int fcur = -1; static uint64_t fnext = 0;
static void advance_bins(uint64_t n){
  while (n >= b20next) { b20cur++; b20next = ceilpow((b20cur+1)/20.0); }
  while (n >= fnext) { fcur++; fnext = ceilpow((fcur+1)/1000.0); }
}
static int dec_of(uint64_t n){ int d = 0; while (n >= 10) { n /= 10; d++; } return d; }
static uint64_t ppstep(uint64_t n, uint64_t p, int si, int e, int64_t *g, int64_t *mu){
  uint64_t A = (si >= 0) ? cS[(size_t)si*EMAX + e] : 0;
  if (si < 0 && e != 1) { fprintf(stderr, "bad ppstep\n"); exit(2); }
  int64_t m = rulem(n, A); double lam;
  if (si >= 0) {
    size_t o = (size_t)si*EMAX; int em = emaxS[si]; mS[o+e] = (uint16_t)m;
    for (int t = 0; t < m; t++) for (int j = e; j <= em; j++) cS[o+j] += cS[o+j-e];
    for (int t = 0; t < m; t++) for (int j = em; j >= e; j--) muS[o+j] -= muS[o+j-e];
    for (int j = 1; j <= em; j++) gS[o+j] = (int64_t)cS[o+j] - (int64_t)cS[o+j-1];
    *g = gS[o+e]; *mu = muS[o+e];
    int64_t s = 0; for (int k = 1; k <= e; k++) if (e % k == 0) s += (int64_t)k * mS[o+k];
    lam = (double)s * log((double)p);
  } else { *g = m - 1; *mu = -m; lam = (double)m * log((double)p); }
  if (e == 1 && (p & 1) && p <= X/2) { if (m > 255) { fprintf(stderr, "m>255 at %llu\n", (unsigned long long)p); exit(3); } mtab[p>>1] = (uint8_t)m; }
  int d = dec_of(n);
  if (e == 1) { dcnt[d][m < 4 ? m : 4]++; dcnt[d][5]++; dsum[d] += m; if ((uint64_t)m > dmaxm[d]) dmaxm[d] = m;
    if ((uint64_t)m > maxm) { maxm = m; maxm_n = n; } }
  else if (m > 0) dhpp[d]++;
  // psi: value just before n, then after the jump
  double before = fabs((psi + psic) - (double)n); if (before > b20_psi[b20cur]) b20_psi[b20cur] = before;
  addpsi(lam);
  double after = fabs((psi + psic) - (double)n); if (after > b20_psi[b20cur]) b20_psi[b20cur] = after;
  return A + (uint64_t)m;
}
static uint32_t *rem; static uint64_t *av; static int64_t *gv, *muv; static uint8_t *om, *ex; static uint16_t *pid; static uint16_t *dbuf;
static uint64_t chk[16]; static int nchk = 0;
static void segment(uint64_t L, uint64_t R, FILE *dump){
  size_t S = R - L;
  for (size_t i = 0; i < S; i++) { rem[i] = (uint32_t)(L+i); av[i] = 1; gv[i] = 1; muv[i] = 1; om[i] = 0; }
  uint64_t B = (uint64_t)sqrt((double)(R-1)); while ((B+1)*(B+1) <= R-1) B++; while (B*B > R-1) B--;
  for (int k = 0; k < nsp && sp[k] <= B; k++) { uint64_t p = sp[k]; uint64_t j = ((L + p - 1)/p)*p; size_t o = (size_t)k*EMAX;
    for (; j < R; j += p) { size_t i = j - L; uint32_t r = rem[i]; int e = 0; do { r /= (uint32_t)p; e++; } while (r % p == 0);
      rem[i] = r; av[i] *= cS[o+e]; gv[i] *= gS[o+e]; muv[i] *= muS[o+e]; om[i]++; pid[i] = (uint16_t)k; ex[i] = (uint8_t)e; } }
  for (uint64_t n = L; n < R; n++) {
    size_t i = n - L; int omt = om[i] + (rem[i] > 1); uint64_t a; int64_t g, mu;
    advance_bins(n);
    if (omt == 1) { if (rem[i] > 1) { int si = (n <= SQ) ? sidx[n] : -1; a = ppstep(n, n, si, 1, &g, &mu); }
                    else { int si = pid[i]; a = ppstep(n, sp[si], si, ex[i], &g, &mu); } }
    else { a = av[i]; g = gv[i]; mu = muv[i];
      if (rem[i] > 1) { uint64_t P = rem[i]; int64_t m = mtab[P>>1]; a *= (uint64_t)m; g *= (m - 1); mu *= -m; } }
    N += (int64_t)a; Mg += g; MP += mu;
    if (a > maxa) { maxa = a; maxa_n = n; } if (a > b20_maxa[b20cur]) b20_maxa[b20cur] = a;
    int64_t dE = den*N - num*(int64_t)(n-1) - den; if (dE > denE_max) denE_max = dE; if (dE < denE_min) denE_min = dE;
    double E = (double)dE/(double)den, Ei = (double)(dE - num)/(double)den;
    if (E > b20_supE[b20cur]) b20_supE[b20cur] = E; if (Ei < b20_infE[b20cur]) b20_infE[b20cur] = Ei;
    double aE = E > -Ei ? E : -Ei; if (aE > b20_absE[b20cur]) b20_absE[b20cur] = aE;
    double aMg = fabs((double)Mg), aMP = fabs((double)MP); if (aMg > b20_mg[b20cur]) b20_mg[b20cur] = aMg; if (aMP > b20_mp[b20cur]) b20_mp[b20cur] = aMP;
    int64_t dC = den*N - num*(int64_t)n; double aC = fabs((double)dC/(double)den);
    if (aC > fineC[fcur]) { fineC[fcur] = aC; fineC_n[fcur] = n; }
    for (int c = 0; c < nchk; c++) if (n == chk[c]) printf("CHK n=%llu N=%lld denE=%lld denC=%lld psi-n=%.3f Mg=%lld MP=%lld\n",
      (unsigned long long)n, (long long)N, (long long)dE, (long long)dC, (psi+psic) - (double)n, (long long)Mg, (long long)MP);
    if (dump) { if (a > 65535) { fprintf(stderr, "a>65535\n"); exit(4); } dbuf[i] = (uint16_t)a; }
  }
  if (dump) fwrite(dbuf, 2, S, dump);
}
