/* zline.c -- F_X(s) = rho*zeta(s) + D_X(s), D_X(s) = sum_{n<=X} (a_n - rho) n^{-s}, for the N-supported system S7
   (dump: uint16 a_n at index n, a_0 = 0).  Adapted from u-offsurgery-s39/verify/zscan.c (same Euler-Maclaurin zeta and the same
   recurrences in t and sigma); new here: memory-mapped input, a point mode with D and D', and a Taylor-moment mode.
   Modes:  v sigma t0 t1 dt      vertical line (recurrence in t)          -> sigma t ReF ImF |F|
           h t s0 s1 ds          horizontal segment (recurrence in sigma)  -> same columns
           p file                points (sigma t per line): ReD ImD ReD' ImD' (D' = dD/ds), and ReF ImF from EM zeta
           m file K              Taylor moments at centers: M_k = sum (a_n - rho) n^{-s0} (-log n)^k / k!, k = 0..K
   Also prints C(X) = N(X) - rho*X.   Usage: zline a.u16 X num den mode ...   Build: cc -O2 -o zline zline.c -lm */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <complex.h>
#include <math.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <unistd.h>
static double B2k[11] = {0, 1.0/6, -1.0/30, 1.0/42, -1.0/30, 5.0/66, -691.0/2730, 7.0/6, -3617.0/510, 43867.0/798, -174611.0/330};
static double complex zeta_em(double complex s){ int M = 60; double complex z = 0; for(int n = 1; n < M; n++) z += cpow((double)n, -s);
  z += cpow((double)M, 1 - s)/(s - 1) + 0.5*cpow((double)M, -s); double complex fac = s*cpow((double)M, -s - 1); double f2 = 1;
  for(int k = 1; k <= 10; k++){ f2 *= (2.0*k - 1)*(2.0*k); z += B2k[k]/f2*fac; fac *= (s + 2*k - 1)*(s + 2*k)/((double)M*M); } return z; }
int main(int argc, char **argv){
  if(argc < 7){ fprintf(stderr, "usage: zline a.u16 X num den mode ...\n"); return 1; }
  uint64_t X = strtoull(argv[2], 0, 10); double rho = atof(argv[3])/atof(argv[4]); char mode = argv[5][0];
  int fd = open(argv[1], O_RDONLY); if(fd < 0){ perror("open"); return 1; }
  const uint16_t *a = mmap(NULL, (X + 1)*2, PROT_READ, MAP_PRIVATE, fd, 0); if(a == MAP_FAILED){ perror("mmap"); return 1; }
  double NX = 0; for(uint64_t n = 1; n <= X; n++) NX += a[n]; double CX = NX - rho*(double)X;
  printf("# zline X=%llu rho=%.12g C(X)=%.6g mode=%c\n", (unsigned long long)X, rho, CX, mode);
  if(mode == 'v' || mode == 'h'){
    int J; double complex *S; double *sg, *tt;
    if(mode == 'v'){ double s = atof(argv[6]), t0 = atof(argv[7]), t1 = atof(argv[8]), dt = atof(argv[9]); J = (int)floor((t1 - t0)/dt + 0.5) + 1;
      S = calloc(J, sizeof *S); sg = malloc(J*8); tt = malloc(J*8); for(int j = 0; j < J; j++){ sg[j] = s; tt[j] = t0 + j*dt; }
      for(uint64_t n = 1; n <= X; n++){ double c = (double)a[n] - rho, L = log((double)n); double complex z = c*exp(-s*L)*cexp(-I*t0*L), w = cexp(-I*dt*L);
        for(int j = 0; j < J; j++){ S[j] += z; z *= w; } } }
    else { double t = atof(argv[6]), s0 = atof(argv[7]), s1 = atof(argv[8]), ds = atof(argv[9]); J = (int)floor((s1 - s0)/ds + 0.5) + 1;
      S = calloc(J, sizeof *S); sg = malloc(J*8); tt = malloc(J*8); for(int j = 0; j < J; j++){ sg[j] = s0 + j*ds; tt[j] = t; }
      for(uint64_t n = 1; n <= X; n++){ double c = (double)a[n] - rho, L = log((double)n); double complex z = c*exp(-s0*L)*cexp(-I*t*L); double r = exp(-ds*L);
        for(int j = 0; j < J; j++){ S[j] += z; z *= r; } } }
    printf("# sigma t ReF ImF |F|\n");
    for(int j = 0; j < J; j++){ double complex s = sg[j] + I*tt[j], F = rho*zeta_em(s) + S[j];
      printf("%.6f %.6f %.12e %.12e %.6e\n", sg[j], tt[j], creal(F), cimag(F), cabs(F)); }
  } else if(mode == 'p' || mode == 'm'){
    FILE *fp = fopen(argv[6], "r"); int K = mode == 'm' ? atoi(argv[7]) : 1; double s0[4096], t0[4096]; int J = 0;
    while(J < 4096 && fscanf(fp, "%lf %lf", &s0[J], &t0[J]) == 2) J++; fclose(fp);
    double complex *M = calloc((size_t)J*(K + 1), sizeof *M); double *pw = malloc((K + 1)*8);
    for(uint64_t n = 1; n <= X; n++){ double c = (double)a[n] - rho; if(c == 0) continue; double L = log((double)n);
      pw[0] = c; for(int k = 1; k <= K; k++) pw[k] = pw[k - 1]*(-L)/(mode == 'm' ? (double)k : 1.0);
      for(int j = 0; j < J; j++){ double complex z = exp(-s0[j]*L)*cexp(-I*t0[j]*L); double complex *Mj = M + (size_t)j*(K + 1);
        for(int k = 0; k <= K; k++) Mj[k] += pw[k]*z; } }
    for(int j = 0; j < J; j++){ double complex *Mj = M + (size_t)j*(K + 1);
      if(mode == 'p'){ double complex s = s0[j] + I*t0[j], F = rho*zeta_em(s) + Mj[0];
        printf("%.10f %.10f %.15e %.15e %.15e %.15e %.15e %.15e\n", s0[j], t0[j], creal(Mj[0]), cimag(Mj[0]), creal(Mj[1]), cimag(Mj[1]), creal(F), cimag(F)); }
      else { printf("C %.10f %.10f %d\n", s0[j], t0[j], K); for(int k = 0; k <= K; k++) printf("%d %.17e %.17e\n", k, creal(Mj[k]), cimag(Mj[k])); } }
  }
  return 0;
}
