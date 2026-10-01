/* s8u5.c — U5-obstruction's own S8(rho) generator (event heap, double precision).
   Statistics only (no ordering certificate). Each g-integer n = p_i * m with i = index of the
   LARGEST prime factor of n and lpi(m) <= i, so every multiset product is produced once.
   Prime rule (s40 Lemma 1.2): with n = N(x-), the next prime sits at 1 + (n - 1/2) t unless a
   composite comes first.  Output per decade: N, pi, C, sup E, sup Q (Q = composite excess
   sup_{y<=x}[C(x)-C(y-)-rho(x-y)]), largest prime gap in cells, near-tie count.
   Optional dump of all g-integers <= XD (doubles) for the mean-square tests.
   usage: s8u5 rho_num rho_den X XD dumpfile      (rho = pi*num/den)                       */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef struct { double v; int i; } H;
static H *hp; static long hn = 0;
static void push(double v, int i) { long k = hn++; while (k > 0) { long p = (k - 1) / 2;
  if (hp[p].v <= v) break; hp[k] = hp[p]; k = p; } hp[k].v = v; hp[k].i = i; }
static void popfix(void) { H x = hp[--hn]; long k = 0; for (;;) { long c = 2 * k + 1;
  if (c >= hn) break; if (c + 1 < hn && hp[c + 1].v < hp[c].v) c++; if (hp[c].v >= x.v) break;
  hp[k] = hp[c]; k = c; } hp[k] = x; }
int main(int argc, char **argv) {
  double rho = M_PI * atof(argv[1]) / atof(argv[2]), t = 1.0 / rho, X = atof(argv[3]);
  double XD = atof(argv[4]); FILE *fd = fopen(argv[5], "wb");
  long cap = (long)(rho * X * 1.3) + 1000;
  double *G = malloc(cap * sizeof(double)); int *lp = malloc(cap * sizeof(int));
  long pcap = (long)(X / log(X) * 1.2) + 1000;
  double *P = malloc(pcap * sizeof(double)); long *cur = malloc(pcap * sizeof(long));
  hp = malloc(pcap * sizeof(H));
  long n = 1, np = 0, C = 0; G[0] = 1.0; lp[0] = 0;
  double supE = 0, supQ = 0, minW = -rho, lastp = 1.0, maxgap = 0; long ties = 0;
  double dec = 10.0;
  printf("# rho=%.12f t=%.12f X=%.3e\n# x N pi C supE supQ maxgap_cells ties\n", rho, t, X);
  for (;;) {
    double xp = 1.0 + ((double)n - 0.5) * t, x; int isprime;
    if (hn > 0 && hp[0].v < xp) { x = hp[0].v; isprime = 0;
      if (fabs(x - xp) < 1e-9 * x) ties++; } else { x = xp; isprime = 1; }
    while (x > dec && dec <= X) {
      printf("%.0e %ld %ld %ld %.4f %.4f %.1f %ld\n", dec, n, np, C, supE, supQ, maxgap, ties);
      fflush(stdout); dec *= 10.0; }
    if (x > X) break;
    if (isprime) {
      double g = (x - lastp) / t; if (np > 0 && g > maxgap) maxgap = g; lastp = x;
      P[np] = x; cur[np] = 1; G[n] = x; lp[n] = (int)(np + 1); n++;
      push(x * G[1], (int)np); np++;
    } else {
      int i = hp[0].i; popfix();
      double W = (double)C - rho * x; if (W < minW) minW = W;      /* W(x-) */
      C++; if ((double)C - rho * x - minW > supQ) supQ = (double)C - rho * x - minW;
      G[n] = x; lp[n] = i + 1; n++;
      long c = cur[i] + 1; while (lp[c] > i + 1) c++; cur[i] = c;
      push(P[i] * G[c], i);
    }
    double E = (double)n - rho * (x - 1.0) - 1.0; if (E > supE) supE = E;
    if (x <= XD) fwrite(&x, sizeof(double), 1, fd);
    if (n >= cap - 2 || np >= pcap - 2) { fprintf(stderr, "cap\n"); return 1; }
  }
  fclose(fd); return 0;
}
