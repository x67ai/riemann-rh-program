/* s5gen_O.c -- Opus reader (Session 41), independent exact generator of S5(0.8) on [1, 2e9].
 * Written from the definition in results/u-offsurgery-s39/NOTE.md §2 (not from any unit script):
 *   m_n = max(0, floor(rho(n-1) + 1 - N(n-1) - A(n) + 1/2)),  rho = 4/5,  a_n = A(n) + m_n,  N(n) = N(n-1) + a_n,
 *   A(n) = number of multisets of g-primes < n (copies distinguished) with product n.
 * Method: multiplicative (unbounded-knapsack) sieve. When n is accepted with m copies, the Euler factor (1-n^-s)^-m is
 * applied to the whole array at once (m passes of a[k] += a[k/n], k = n, 2n, ... in increasing k), so when the walk
 * reaches n, a[n] holds exactly A(n). Exact integers throughout (int64 for N; uint16 below 1e9; 9-bit packed above,
 * every addition range-checked; abort on any overflow). General m is allowed (the claim m in {0,1} is tested, not assumed).
 * Outputs (scratch dir argv[1]): gp_O_1e9.u32, gp_O_ext.u32 (uint32 pairs (n, m)); SHA-256 of a[0..1e9] (uint16 LE).
 * Build: clang -O2 -o s5gen_O s5gen_O.c */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <CommonCrypto/CommonDigest.h>

#ifndef X1
#define X1 1000000000ULL
#endif
#define X2 (2 * X1)
static uint16_t *a;      /* a[0..X1] */
static uint8_t *lo;      /* upper half: n in (X1, X2], index n - X1 - 1 */
static uint8_t *hi;      /* bit 8 of the upper values */

static inline uint32_t getv(uint64_t n) {
  if (n <= X1) return a[n];
  uint64_t i = n - X1 - 1;
  return (uint32_t)lo[i] | ((uint32_t)((hi[i >> 3] >> (i & 7)) & 1) << 8);
}
static void die(const char *s, uint64_t n) { fprintf(stderr, "ABORT %s at %llu\n", s, (unsigned long long)n); exit(2); }

static void pass(uint64_t q) { /* apply (1 - q^-s)^-1 once */
  uint64_t jmax1 = X1 / q, jmax2 = X2 / q, j;
  for (j = 1; j <= jmax1; j++) {
    uint32_t v = (uint32_t)a[q * j] + a[j];
    if (v > 65535) die("uint16 overflow", q * j);
    a[q * j] = (uint16_t)v;
  }
  for (j = jmax1 + 1; j <= jmax2; j++) {
    uint64_t k = q * j, i = k - X1 - 1;
    uint32_t v = getv(k) + a[j];  /* j <= X2/q <= X1 for q >= 2 */
    if (v > 511) die("9-bit overflow", k);
    lo[i] = (uint8_t)(v & 255);
    if (v & 256) hi[i >> 3] |= (uint8_t)(1u << (i & 7)); else hi[i >> 3] &= (uint8_t)~(1u << (i & 7));
  }
}

static int64_t floordiv(int64_t x, int64_t d) { int64_t q = x / d; if ((x % d != 0) && ((x < 0) != (d < 0))) q--; return q; }

int main(int argc, char **argv) {
  const char *dir = argc > 1 ? argv[1] : "/private/tmp/rh-s41-read-s5mult";
  char path[512];
  a = calloc(X1 + 1, 2); lo = calloc(X1, 1); hi = calloc(X1 / 8 + 1, 1);
  if (!a || !lo || !hi) die("alloc", 0);
  snprintf(path, sizeof path, "%s/gp_O_1e9.u32", dir); FILE *g1 = fopen(path, "wb");
  snprintf(path, sizeof path, "%s/gp_O_ext.u32", dir); FILE *g2 = fopen(path, "wb");
  if (!g1 || !g2) die("fopen", 0);
  a[1] = 1;
  int64_t N = 1;                 /* N(1) */
  int64_t F = 0;                 /* 5E(1) = 5N(1) - 4 - 1 = 0 */
  int64_t supF = 0, infF = 0; uint64_t supFn = 1, infFn = 1;
  uint32_t amax = 1; uint64_t ngp1 = 0, ngp2 = 0, zero_a = 0, mmax = 0, gp_with_A = 0;
  /* half-decade windows [10^(h/2), 10^((h+1)/2)) for h = 0..17 and the window (1e9, 2e9] */
  uint64_t wlo[19]; uint32_t wmax[19]; uint64_t warg[19];
  for (int h = 0; h < 18; h++) { wlo[h] = (uint64_t)ceil(pow(10.0, h / 2.0) - 1e-9); wmax[h] = 0; warg[h] = 0; }
  wlo[18] = X1 + 1; wmax[18] = 0; warg[18] = 0;
  /* per-decade counts: non-representable (A=0), g-primes */
  uint64_t dec_A0[10] = {0}, dec_gp[10] = {0}, next_dec = 10; int dcur = 0;
  clock_t t0 = clock();
  for (uint64_t n = 2; n <= X2; n++) {
    uint32_t A = getv(n);
    int64_t num = 8 * (int64_t)(n - 1) + 15 - 10 * N - 10 * (int64_t)A;
    int64_t m = floordiv(num, 10); if (m < 0) m = 0;
    if (m > 0) {
      for (int64_t r = 0; r < m; r++) pass(n);
      uint32_t pr[2] = {(uint32_t)n, (uint32_t)m};
      if (n <= X1) { fwrite(pr, 4, 2, g1); ngp1++; } else { fwrite(pr, 4, 2, g2); ngp2++; }
      if ((uint64_t)m > mmax) mmax = (uint64_t)m;
      if (A > 0) gp_with_A++;
    }
    uint32_t an = getv(n);
    if (an != A + (uint32_t)m) die("a_n != A + m", n);
    int64_t Fprev = F;
    N += an; F = 5 * N - 4 * (int64_t)n - 1;
    if (F > supF) {
      supF = F; supFn = n;
      if (n >= 10000000ULL) printf("Erec n=%llu a=%u E(n-1)=%.1f E(n)=%.1f\n", (unsigned long long)n, an, Fprev / 5.0, F / 5.0);
    }
    if (F < infF) { infF = F; infFn = n; }
    if (an > amax) { amax = an; if (n >= 100000ULL) printf("arec n=%llu a=%u exp=%.5f\n", (unsigned long long)n, an, log((double)an) / log((double)n)); }
    if (n <= X1 && an == 0) zero_a++;
    int h = (n > X1) ? 18 : 17; while (h > 0 && h < 18 && n < wlo[h]) h--;
    if (an > wmax[h]) { wmax[h] = an; warg[h] = n; }
    if (n == next_dec) { dcur++; next_dec *= 10; }
    if (A == 0) dec_A0[dcur]++;
    if (m > 0) dec_gp[dcur]++;
    if (n == X1 || n == X2) {
      printf("AT n=%llu N=%lld C=N-0.8n=%lld/5 supE=%lld/5 at %llu infE=%lld/5 at %llu maxa=%u gps=%llu+%llu zero_a(2..1e9)=%llu mmax=%llu gp_with_A>0=%llu t=%.0fs\n",
             (unsigned long long)n, (long long)N, (long long)(5 * N - 4 * (int64_t)n), (long long)supF, (unsigned long long)supFn,
             (long long)infF, (unsigned long long)infFn, amax, (unsigned long long)ngp1, (unsigned long long)ngp2,
             (unsigned long long)zero_a, (unsigned long long)mmax, (unsigned long long)gp_with_A, (double)(clock() - t0) / CLOCKS_PER_SEC);
      fflush(stdout);
    }
    if (n % 100000000ULL == 0) { fprintf(stderr, "n=%llu t=%.0fs\n", (unsigned long long)n, (double)(clock() - t0) / CLOCKS_PER_SEC); }
  }
  fclose(g1); fclose(g2);
  for (int h = 0; h < 19; h++) printf("window h=%d [%llu, ...): max a=%u at %llu\n", h, (unsigned long long)wlo[h], wmax[h], (unsigned long long)warg[h]);
  for (int d = 0; d < 10; d++) printf("decade %d: A=0 count=%llu gprimes=%llu\n", d, (unsigned long long)dec_A0[d], (unsigned long long)dec_gp[d]);
  unsigned char md[32];
  CC_SHA256_CTX c; CC_SHA256_Init(&c);
  uint64_t off = 0, tot = (X1 + 1) * 2; const uint8_t *p = (const uint8_t *)a;
  while (off < tot) { uint64_t ch = tot - off > (1u << 30) ? (1u << 30) : tot - off; CC_SHA256_Update(&c, p + off, (CC_LONG)ch); off += ch; }
  CC_SHA256_Final(md, &c);
  printf("SHA256(a[0..1e9] uint16 LE) = "); for (int i = 0; i < 32; i++) printf("%02x", md[i]); printf("\n");
  if (X1 >= 1000000000ULL) printf("a[902538000]=%u a[478800]=%u a[1805076000]=%u\n", a[902538000], a[478800], getv(1805076000ULL));
  else printf("a[478800]=%u a[957600]=%u\n", a[478800], getv(957600));
  return 0;
}
