/* dump_records.c -- unit s5-multiplicity-s40, task 1.  Exact integer scan of the S5(4/5) dump.
   Inputs: a-file (uint16 a_n, n = 0..X), gp-file (uint32 pairs (q, m_q)).  All arithmetic in int64, E in units of 1/5:
     E5(n) = 5 N(n) - 4 (n-1) - 5   [E(n) = N(n) - 0.8(n-1) - 1],   C5(n) = 5 N(n) - 4 n   [C(n) = N(n) - 0.8 n].
   Checks: gp strictly increasing, every m_q = 1, a_q >= 1 at every g-prime q, a_n >= 1 count, N(X).
   Reports: records of a_n and of E (late ones), per half-decade max a_n / sup E / inf E / sup|C| with their n,
   and the identity E5(n) - E5(n-1) = 5 a_n - 4 at every record of E (is the record a single spike?).
   Build: cc -O2 -o dump_records dump_records.c     Usage: dump_records a.u16 gp.u32 X */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <sys/stat.h>
static void *mapf(const char *p, size_t *len){ int fd=open(p,O_RDONLY); if(fd<0){perror(p);exit(1);} struct stat st; fstat(fd,&st);
  *len=st.st_size; void *m=mmap(0,*len,PROT_READ,MAP_SHARED,fd,0); if(m==MAP_FAILED){perror("mmap");exit(1);} return m; }
int main(int argc,char**argv){
  if(argc<4){fprintf(stderr,"usage\n");return 1;}
  size_t la,lg; const uint16_t *a=mapf(argv[1],&la); const uint32_t *g=mapf(argv[2],&lg); uint64_t X=strtoull(argv[3],0,10);
  if(la!=2*(X+1)){fprintf(stderr,"a-file length %zu != 2(X+1)\n",la);return 1;}
  uint64_t ng=lg/8, bad=0, prev=0, badq=0;
  for(uint64_t i=0;i<ng;i++){ uint32_t q=g[2*i], m=g[2*i+1]; if(q<=prev||m!=1) bad++; if(a[q]<1) badq++; prev=q; }
  printf("gp entries %llu, last %u, not-increasing-or-m!=1: %llu, g-primes with a_q=0: %llu\n",(unsigned long long)ng,g[2*(ng-1)],(unsigned long long)bad,(unsigned long long)badq);
  int64_t N=1, E5, prevE5=5*1-0-5, supE5=-1000000000, infE5=1000000000; uint64_t maxa=1, zeros=0;
  /* half-decade windows: [10^(k/2), 10^((k+1)/2)) */
  double edge=pow(10.0,0.5); int hk=0; int64_t wsup=-1000000000, winf=1000000000, wsupC=0; uint64_t wmaxa=0,wan=0,wsn=0,win=0,wcn=0;
  printf("records of a_n (n, a_n, log a/log n) for n >= 10^5, and records of E >= 30 that are single spikes:\n");
  for(uint64_t n=2;n<=X;n++){
    uint64_t an=a[n]; N+=an; if(an==0) zeros++;
    E5=5*N-4*(int64_t)(n-1)-5; int64_t C5=5*N-4*(int64_t)n;
    if(an>maxa){ maxa=an; if(n>=100000) printf("  a-record n=%llu a_n=%llu exponent=%.4f\n",(unsigned long long)n,(unsigned long long)an,log((double)an)/log((double)n)); }
    if(E5>supE5){ supE5=E5; if(E5>=150) printf("  E-record n=%llu E=%lld/5 a_n=%llu E(n-1)=%lld/5 jump=5a_n-4=%lld ok=%d\n",(unsigned long long)n,(long long)E5,(unsigned long long)an,(long long)prevE5,(long long)(5*an-4),(int)(E5-prevE5==5*(int64_t)an-4)); }
    if(E5<infE5) infE5=E5;
    if((double)n>=edge){ printf("  window %d [10^%.1f,10^%.1f): max a_n=%llu at %llu; sup E=%lld/5 at %llu; inf E=%lld/5 at %llu; sup|C|=%lld/5 at %llu\n",hk,hk*0.5,(hk+1)*0.5,(unsigned long long)wmaxa,(unsigned long long)wan,(long long)wsup,(unsigned long long)wsn,(long long)winf,(unsigned long long)win,(long long)wsupC,(unsigned long long)wcn);
      hk++; edge=pow(10.0,0.5*(hk+1)); wsup=-1000000000; winf=1000000000; wsupC=0; wmaxa=0; }
    if(an>wmaxa){wmaxa=an;wan=n;} if(E5>wsup){wsup=E5;wsn=n;} if(E5<winf){winf=E5;win=n;} if(llabs(C5)>wsupC){wsupC=llabs(C5);wcn=n;}
    prevE5=E5;
  }
  printf("  window %d [10^%.1f, X]: max a_n=%llu at %llu; sup E=%lld/5 at %llu; inf E=%lld/5 at %llu; sup|C|=%lld/5 at %llu\n",hk,hk*0.5,(unsigned long long)wmaxa,(unsigned long long)wan,(long long)wsup,(unsigned long long)wsn,(long long)winf,(unsigned long long)win,(long long)wsupC,(unsigned long long)wcn);
  printf("N(X)=%lld  C(X)=%lld/5  max a_n=%llu  sup E=%lld/5  inf E=%lld/5  #(a_n=0, 2<=n<=X)=%llu\n",(long long)N,(long long)(5*N-4*(int64_t)X),(unsigned long long)maxa,(long long)supE5,(long long)infE5,(unsigned long long)zeros);
  return 0;
}
