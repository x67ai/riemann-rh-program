/* inherit.c — U7-patterns: multiscale quantities along the S8 cell arrays (written by s8gen).
   E_q(k) := E(x_k/p_q) = #{composites <= x_k divisible by p_q} - rho*(x_k/p_q - 1)  (exact, free monoid), q = 1..4.
   r^(1): reflected walk of the arrivals NOT divisible by p1 against service 1 - 1/p1; theorem: e_k <= E_1(k) + tau + r^(1)_k.
   r^(2), r^(4): the same for arrivals with smallest factor > p2 (> p4) against service prod(1 - 1/p_q).
   Usage: inherit prefix t rho tau delta X [peakfile]   (peakfile: cell indices to print in detail) */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <sys/stat.h>
static void *mapf(const char *pre, const char *suf, long *n){
  char fn[1024]; sprintf(fn, "%s%s", pre, suf); int fd = open(fn, O_RDONLY); if (fd < 0){ perror(fn); exit(1); }
  struct stat st; fstat(fd, &st); *n = st.st_size; void *p = mmap(0, st.st_size, PROT_READ, MAP_SHARED, fd, 0);
  if (p == MAP_FAILED){ perror("mmap"); exit(1); } return p; }
int main(int argc, char **argv){
  const char *pre = argv[1]; double t = atof(argv[2]), rho = atof(argv[3]), tau = atof(argv[4]), delta = atof(argv[5]), X = atof(argv[6]);
  long n, m; FILE *fc, *fe, *fdd[5], *fss[4]; char fn[1024];
  sprintf(fn, "%s.c.u8", pre); fc = fopen(fn, "rb"); sprintf(fn, "%s.e.u8", pre); fe = fopen(fn, "rb"); sprintf(fn, "%s.c1.u8", pre); fdd[1] = fopen(fn, "rb");
  for (int q = 2; q <= 4; q++){ sprintf(fn, "%s.d%d.u8", pre, q); fdd[q] = fopen(fn, "rb"); sprintf(fn, "%s.s%d.u8", pre, q-1); fss[q-1] = fopen(fn, "rb"); }
  if (!fc || !fe || !fdd[1] || !fdd[2] || !fss[1]){ fprintf(stderr, "missing input\n"); return 1; }
  fseek(fc, 0, SEEK_END); n = ftell(fc); fseek(fc, 0, SEEK_SET);
  const long BS = 1L << 24; uint8_t *c = malloc(BS), *e = malloc(BS + 1), *d[5], *s[4];
  for (int q = 1; q <= 4; q++) d[q] = malloc(BS); for (int q = 1; q <= 3; q++) s[q] = malloc(BS);
  uint8_t *c1 = d[1]; long base = -BS;   /* block buffers: cells base..base+BS-1 */
  uint32_t *pk = mapf(pre, ".primes.u32", &m); double p[5]; for (int q = 1; q <= 4; q++) p[q] = 1 + (pk[q-1] - 1 + tau)*t - delta;
  double M1 = 1 - 1/p[1], M2 = M1*(1 - 1/p[2]), M4 = M2*(1 - 1/p[3])*(1 - 1/p[4]);
  printf("# inherit %s p1..p4 = %.10g %.10g %.10g %.10g  M1=%.6f M2=%.6f M4=%.6f\n", pre, p[1], p[2], p[3], p[4], M1, M2, M4);
  int nb = 0; long bk[64]; for (double lx = 1.0; lx <= log10(X) + 1e-9; lx += 0.5){ long k = (long)floor((pow(10, lx) - 1)*rho + 1 - tau); bk[nb++] = k > n ? n : k; }
  /* peaks to print */
  long *pc = NULL; int npc = 0; if (argc > 7){ FILE *f = fopen(argv[7], "r"); long v; pc = malloc(100000*sizeof(long)); while (fscanf(f, "%ld", &v) == 1 && npc < 100000) pc[npc++] = v; fclose(f);
    for (int a1 = 0; a1 < npc; a1++) for (int b1 = a1+1; b1 < npc; b1++) if (pc[b1] < pc[a1]){ long tt = pc[a1]; pc[a1] = pc[b1]; pc[b1] = tt; } }
  int zi = 0;
  double Sd[5] = {0}; double r1 = 0, r2 = 0, r4 = 0, maxviol = -1e9; long maxviol_k = 0;
  int band = 0;
  double w[5]; w[1] = 1/p[1]; w[2] = (1/p[2])*(1 - 1/p[1]); w[3] = (1/p[3])*(1 - 1/p[1])*(1 - 1/p[2]); w[4] = (1/p[4])*(1 - 1/p[1])*(1 - 1/p[2])*(1 - 1/p[3]);
  /* excursion decomposition: e_peak = sum_q (C_q - lb*w_q) + (C_rough - lb*M4) exactly (q = spf class p1..p4) */
  static const int HB[9] = {1, 2, 3, 4, 6, 9, 13, 18, 1000}; double XB[8][8]; memset(XB, 0, sizeof XB);
  int inx = 0; long xa = 0; int xh = 0; double cls[5], clsp[5], lbp = 0; memset(cls, 0, sizeof cls); memset(clsp, 0, sizeof clsp);
  double A[64][24]; memset(A, 0, sizeof A);   /* per band accumulators */
  /* block maxima along the p1-chain */
  int nblk = 0; double blkmax[200]; long blkarg[200]; for (int i = 0; i < 200; i++){ blkmax[i] = -1; blkarg[i] = 0; }
  for (long i = 0; i < n; i++){
    if (i - base >= BS){ base += BS; long r = n - base < BS ? n - base : BS;
      if (fread(c, 1, r, fc) != (size_t)r || fread(e, 1, r, fe) != (size_t)r){ fprintf(stderr, "read error\n"); return 1; }
      for (int q = 1; q <= 4; q++) if (fread(d[q], 1, r, fdd[q]) != (size_t)r){ fprintf(stderr, "read d\n"); return 1; }
      for (int q = 1; q <= 3; q++) if (fread(s[q], 1, r, fss[q]) != (size_t)r){ fprintf(stderr, "read s\n"); return 1; } }
    long ii = i - base;
    long k = i + 1; double x = 1 + (k - 1 + tau)*t;
    while (band + 1 < nb && i >= bk[band+1]) band++;
    for (int q = 1; q <= 4; q++) Sd[q] += d[q][ii];
    double E[5]; for (int q = 1; q <= 4; q++) E[q] = (x >= p[q]) ? Sd[q] - rho*(x/p[q] - 1) : 0;
    double rough1 = c[ii] - c1[ii], rough2 = rough1 - s[1][ii], rough4 = rough2 - s[2][ii] - s[3][ii];
    r1 = fmax(r1 + rough1 - M1, 0); r2 = fmax(r2 + rough2 - M2, 0); r4 = fmax(r4 + rough4 - M4, 0);
    double ev = e[ii];
    { double cl[5] = {c1[ii], s[1][ii], s[2][ii], s[3][ii], rough4};
      if (e[ii] > 0){
        if (!inx){ inx = 1; xa = k; xh = e[ii]; for (int q = 0; q < 5; q++) cls[q] = cl[q]; for (int q = 0; q < 5; q++) clsp[q] = cls[q]; lbp = 1; }
        else { for (int q = 0; q < 5; q++) cls[q] += cl[q]; if (e[ii] > xh){ xh = e[ii]; for (int q = 0; q < 5; q++) clsp[q] = cls[q]; lbp = k - xa + 1; } }
      } else if (inx){ inx = 0; int hb = 0; while (hb < 7 && xh >= HB[hb+1]) hb++;
        double ex[5]; for (int q = 0; q < 4; q++) ex[q] = clsp[q] - lbp*w[q+1]; ex[4] = clsp[4] - lbp*M4;
        double sum = ex[0] + ex[1] + ex[2] + ex[3] + ex[4]; if (fabs(sum - xh) > 1e-6 && x > 10*p[4]) fprintf(stderr, "decomp check fails at %ld: %f vs %d\n", k, sum, xh);
        XB[hb][0]++; for (int q = 0; q < 5; q++) XB[hb][1+q] += ex[q]; XB[hb][6] += xh; XB[hb][7] += lbp; } }
    if (x >= p[1]){ double v = ev - (E[1] + tau + r1); if (v > maxviol){ maxviol = v; maxviol_k = k; } }
    int jb = (int)floor(log(x)/log(p[1])); if (jb < 200){ double Ex = ev + 1 - tau; if (Ex > blkmax[jb]){ blkmax[jb] = Ex; blkarg[jb] = k; } if (jb + 1 > nblk) nblk = jb + 1; }
    double *a = A[band];
    a[0]++; a[1] += ev; a[2] += ev*ev; for (int q = 1; q <= 4; q++){ a[2+q] += E[q]; a[6+q] += E[q]*E[q]; a[10+q] += ev*E[q]; }
    a[15] += r1; a[16] += r2; a[17] += r4; if (r1 > a[18]) a[18] = r1; if (r2 > a[19]) a[19] = r2; if (r4 > a[20]) a[20] = r4;
    if (ev > a[21]) a[21] = ev; if (ev > 0){ a[22]++; if (E[1] + tau >= ev) a[23]++; }
    while (zi < npc && pc[zi] < k) zi++;
    while (zi < npc && pc[zi] == k){ zi++;
      printf("PEAK k=%ld x=%.10g e=%d E1+tau=%.4f r1=%.4f r2=%.4f r4=%.4f E2=%.4f E3=%.4f E4=%.4f bound=%.4f\n", k, x, e[ii], E[1] + tau, r1, r2, r4, E[2], E[3], E[4], E[1] + tau + r1); }
  }
  for (int hb = 0; hb < 8; hb++) if (XB[hb][0] > 0){ double N = XB[hb][0];
    printf("XDEC heights [%d,%d) n=%.0f mean_h=%.3f mean_lbuild=%.2f mean excess: spf=p1 %.3f p2 %.3f p3 %.3f p4 %.3f rough(>p4) %.3f\n", HB[hb], HB[hb+1], N, XB[hb][6]/N, XB[hb][7]/N,
      XB[hb][1]/N, XB[hb][2]/N, XB[hb][3]/N, XB[hb][4]/N, XB[hb][5]/N); }
  printf("CHECK max(e - E1 - tau - r1) = %.3e at cell %ld (theorem: <= 0)\n", maxviol, maxviol_k);
  for (int b = 0; b + 1 < nb; b++){ double *a = A[b]; if (a[0] < 10) continue; double N = a[0], me = a[1]/N, ve = a[2]/N - me*me;
    printf("IBAND %d cells=%.0f max_e=%.0f max_r1=%.3f max_r2=%.3f max_r4=%.3f mean_e=%.4f mean_r1=%.4f mean_r2=%.4f mean_r4=%.4f frac(e>0 with E1+tau>=e)=%.4f",
      b, N, a[21], a[18], a[19], a[20], me, a[15]/N, a[16]/N, a[17]/N, a[22] > 0 ? a[23]/a[22] : 0);
    for (int q = 1; q <= 4; q++){ double mq = a[2+q]/N, vq = a[6+q]/N - mq*mq; printf(" corr(e,E%d)=%.4f", q, (a[10+q]/N - me*mq)/sqrt(ve*vq)); }
    printf("\n"); }
  for (int j = 0; j < nblk; j++) if (blkmax[j] >= 0) printf("CHAIN j=%d x in [p1^j, p1^(j+1)) = [%.4g, %.4g) maxE_lattice=%.1f at cell %ld\n", j, pow(p[1], j), pow(p[1], j+1), blkmax[j], blkarg[j]);
  return 0;
}
