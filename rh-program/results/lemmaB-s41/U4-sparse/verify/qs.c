/* qs.c -- unit U4-sparse, 2026-10-01. Exact enumeration, for the lattice x_k = 1 + (k - 1/2) t, t = D/pi, of
   S(z) = sum of 1/m' and Q(z) = #{m'} over lattice-monoid cofactors m' (multisets of >= 1 lattice points) with
   m' * P+(m') <= z, P+ = largest factor; split by the number j of factors of m' (j = 1..7, 8 = "8 or more").
   These are the load and the "+1" count of Theorem 2.3 of NOTE.md. Usage: qs D z1 z2 ... (increasing). */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define NZ 32
#define NJ 9
static double t, zs[NZ]; static int nz;
static double S[NZ][NJ]; static long long Q[NZ][NJ];
static inline double xl(long k){ return 1.0 + ((double)k - 0.5) * t; }
static void dfs(double prod, long a, int j){
  for (long b = a; ; b++){
    double xb = xl(b), m2 = prod * xb, key = m2 * xb;
    if (key > zs[nz - 1]) break;
    int jj = j + 1 < NJ - 1 ? j + 1 : NJ - 1;
    for (int i = 0; i < nz; i++) if (key <= zs[i]){ S[i][jj] += 1.0 / m2; Q[i][jj]++; }
    dfs(m2, b, j + 1);
  }
}
int main(int argc, char **argv){
  double D = atof(argv[1]); t = D / 3.14159265358979323846; nz = argc - 2;
  for (int i = 0; i < nz; i++) zs[i] = atof(argv[i + 2]);
  dfs(1.0, 1, 0);
  printf("# qs D=%g t=%.12g rho=%.12g  columns: z  S_total  Q_total  rhosqrt(z)  | S_j (j=1..8+) | Q_j (j=1..8+)\n", D, t, 1.0/t);
  for (int i = 0; i < nz; i++){ double st = 0; long long qt = 0;
    for (int j = 1; j < NJ; j++){ st += S[i][j]; qt += Q[i][j]; }
    printf("%.3e %.6f %lld %.1f |", zs[i], st, qt, sqrt(zs[i]) / t);
    for (int j = 1; j < NJ; j++) printf(" %.5f", S[i][j]); printf(" |");
    for (int j = 1; j < NJ; j++) printf(" %lld", Q[i][j]); printf("\n"); }
  return 0;
}
