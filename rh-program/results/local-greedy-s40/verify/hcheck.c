/* hcheck.c -- the growth hypothesis H_theta on the computed range: for C(u) = N(u) - rho*floor(u) (constant on [n, n+1)),
   prints max_{n in decade} |C(n)|/n^theta for theta = 0.28 ... 0.40 and C(X).  Usage: hcheck a.u16 X num den   Build: cc -O2 -o hcheck hcheck.c -lm */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <sys/mman.h>
#include <fcntl.h>
int main(int argc, char **argv){
  if(argc < 5){ fprintf(stderr, "usage: hcheck a.u16 X num den\n"); return 1; }
  uint64_t X = strtoull(argv[2], 0, 10); int64_t num = atoll(argv[3]), den = atoll(argv[4]);
  int fd = open(argv[1], O_RDONLY); const uint16_t *a = mmap(NULL, (X + 1)*2, PROT_READ, MAP_PRIVATE, fd, 0);
  const int NT = 7; double th[7] = {0.28, 0.30, 0.32, 0.34, 0.35, 0.38, 0.40}; double mx[12][7] = {{0}}, all[7] = {0}; double cmax[12] = {0};
  int64_t N = 0; int dec = 0; uint64_t dn = 10;
  for(uint64_t n = 1; n <= X; n++){
    N += a[n]; if(n == dn){ dec++; dn *= 10; }
    double C = (double)((__int128)den*N - (__int128)num*(int64_t)n)/(double)den, aC = fabs(C), ln = log((double)n);
    if(aC > cmax[dec]) cmax[dec] = aC;
    if(n >= 1000) for(int j = 0; j < NT; j++){ double r = aC*exp(-th[j]*ln); if(r > mx[dec][j]) mx[dec][j] = r; if(r > all[j]) all[j] = r; }
  }
  printf("# hcheck X=%llu rho=%lld/%lld  C(X)=%.4f\n# decade  max|C|  max|C|/n^theta for theta =", (unsigned long long)X, (long long)num, (long long)den,
         (double)((__int128)den*N - (__int128)num*(int64_t)X)/(double)den);
  for(int j = 0; j < NT; j++) printf(" %.2f", th[j]); printf("\n");
  for(int d = 3; d <= dec; d++){ printf("[1e%d] %.2f", d, cmax[d]); for(int j = 0; j < NT; j++) printf(" %.4f", mx[d][j]); printf("\n"); }
  printf("all n in [1e3, X]:"); for(int j = 0; j < NT; j++) printf(" %.4f", all[j]); printf("\n");
  return 0;
}
