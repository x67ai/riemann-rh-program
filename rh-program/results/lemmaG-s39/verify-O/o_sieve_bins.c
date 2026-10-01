/* read-O independent sieve (own code, written from the NOTE/cO definitions; nothing taken from verify/lg.c).
   usage: o_sieve_bins X Rfile binsfile rho_hi rho_lo > out.tsv
   Segmented sieve of the R-free integers n <= X (R read from Rfile, any order). For each bin [lo,hi] (from binsfile, contiguous,
   covering 1..X) it prints EXACT integer sums: cnt, S1 = sum N(n), S2 = sum N(n)^2, SN = sum N(n)(2n+1), with N(n) = #{R-free m <= n},
   plus maxE = max N(n) - rho n and minE = min N(n) - rho (n+1) in double-double (E on [n,n+1) is N(n) - rho x).
   The exact sum of (N(n) - rho(n+1/2))^2 = S2 - rho*SN + rho^2 * sum (n+1/2)^2 is formed afterwards in high precision. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
typedef __int128 i128;
static void p128(i128 v) { char b[64]; int k = 63; b[k] = 0; int neg = v < 0; if (neg) v = -v;
  do { b[--k] = '0' + (int)(v % 10); v /= 10; } while (v); if (neg) b[--k] = '-'; fputs(b + k, stdout); }
static int cmpu(const void *a, const void *b) { uint64_t x = *(const uint64_t *)a, y = *(const uint64_t *)b; return x < y ? -1 : x > y; }
int main(int argc, char **argv) {
  if (argc < 6) { fprintf(stderr, "usage\n"); return 1; }
  uint64_t X = (uint64_t)strtod(argv[1], 0); double rh = strtod(argv[4], 0), rl = strtod(argv[5], 0);
  FILE *f = fopen(argv[2], "r"); size_t cap = 1 << 16, nR = 0; uint64_t *R = malloc(cap * 8), v;
  while (fscanf(f, "%llu", (unsigned long long *)&v) == 1) { if (v > X) continue; if (nR == cap) R = realloc(R, (cap *= 2) * 8); R[nR++] = v; }
  fclose(f); qsort(R, nR, 8, cmpu);
  for (size_t i = 1; i < nR; i++) if (R[i] == R[i - 1]) { fprintf(stderr, "duplicate %llu\n", (unsigned long long)R[i]); return 1; }
  f = fopen(argv[3], "r"); size_t nb = 0, bcap = 4096; uint64_t *blo = malloc(bcap * 8), *bhi = malloc(bcap * 8), a, b;
  while (fscanf(f, "%llu %llu", (unsigned long long *)&a, (unsigned long long *)&b) == 2) { blo[nb] = a; bhi[nb] = b; nb++; }
  fclose(f);
  uint64_t *nxt = malloc(nR * 8); for (size_t i = 0; i < nR; i++) nxt[i] = R[i];
  const uint64_t L = 1ULL << 24; uint8_t *mark = malloc(L);
  uint64_t N = 0; size_t bi = 0; uint64_t cnt = 0; i128 S1 = 0, S2 = 0, SN = 0; double mx = -1e300, mn = 1e300;
  if (blo[0] != 1) { fprintf(stderr, "bins must start at 1\n"); return 1; }
  for (uint64_t s = 1; s <= X; s += L) {
    uint64_t e = s + L - 1; if (e > X) e = X; memset(mark, 1, L);
    for (size_t i = 0; i < nR && R[i] <= e; i++) { uint64_t m = nxt[i]; for (; m <= e; m += R[i]) mark[m - s] = 0; nxt[i] = m; }
    for (uint64_t n = s; n <= e; n++) {
      N += mark[n - s];
      double dn = (double)n, p = rh * dn, er = fma(rh, dn, -p);
      double E0 = (((double)N - p) - er) - rl * dn;           /* N(n) - rho n */
      double E1 = E0 - rh - rl;                               /* N(n) - rho (n+1) */
      if (E0 > mx) mx = E0; if (E1 < mn) mn = E1;
      cnt++; S1 += N; S2 += (i128)N * N; SN += (i128)N * (2 * (i128)n + 1);
      if (n == bhi[bi]) {
        printf("%llu\t%llu\t%llu\t", (unsigned long long)blo[bi], (unsigned long long)bhi[bi], (unsigned long long)cnt);
        p128(S1); putchar('\t'); p128(S2); putchar('\t'); p128(SN); printf("\t%.9f\t%.9f\n", mx, mn);
        bi++; cnt = 0; S1 = S2 = SN = 0; mx = -1e300; mn = 1e300;
        if (bi < nb && blo[bi] != n + 1) { fprintf(stderr, "bins not contiguous at %llu\n", (unsigned long long)n); return 1; }
      }
    }
  }
  fprintf(stderr, "done: X=%llu nR=%zu N(X)=%llu bins=%zu\n", (unsigned long long)X, nR, (unsigned long long)N, bi);
  return 0;
}
