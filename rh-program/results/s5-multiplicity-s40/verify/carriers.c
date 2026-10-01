/* carriers.c -- unit s5-multiplicity-s40, task 5 / 2(ii).  Carriers of refused primes in S5(4/5) up to X = 10^9, from the dump.
   For the first NR refused primes l: c_l(x) = #{composite g-primes q <= x with l | q}, per decade x = 10^3..10^9, and
   the acceptance statistics of the multiples of l: #{n = l k <= x : A(n) = 0} (non-representable) and how many of them are g-primes.
   Global per decade: #non-representable n, #g-primes, acceptance ratio, times log(midpoint).  A(n) = a(n) - m_n.
   Build: cc -O3 -o carriers carriers.c -lm     Usage: carriers a.u16 gp.u32 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <sys/stat.h>
#define X 1000000000ULL
#define NR 30
int main(int argc,char**argv){
  int fd=open(argv[1],O_RDONLY); struct stat st; fstat(fd,&st); const uint16_t *a=mmap(0,st.st_size,PROT_READ,MAP_SHARED,fd,0);
  FILE *fg=fopen(argv[2],"rb"); fseek(fg,0,SEEK_END); uint64_t ng=ftell(fg)/8; fseek(fg,0,SEEK_SET);
  uint8_t *isg=calloc(X/8+1,1); uint32_t pr[2]; for(uint64_t i=0;i<ng;i++){ if(fread(pr,4,2,fg)!=2) return 1; isg[pr[0]>>3]|=1<<(pr[0]&7); }
  uint8_t *cmp=calloc(X/16+1,1);   /* odd composites */
  for(uint64_t i=3;i*i<=X;i+=2) if(!(cmp[i>>4]&(1<<((i>>1)&7)))) for(uint64_t j=i*i;j<=X;j+=2*i) cmp[j>>4]|=1<<((j>>1)&7);
  #define PRIME(n) ((n)==2 || ((n)>2 && ((n)&1) && !(cmp[(n)>>4]&(1<<(((n)>>1)&7)))))
  #define G(n) ((isg[(n)>>3]>>((n)&7))&1)
  uint64_t L[NR]; int nl=0; for(uint64_t p=2;nl<NR;p++) if(PRIME(p) && !G(p)) L[nl++]=p;
  uint64_t car[NR][10]={{0}}, nonrep[NR][10]={{0}}, acc[NR][10]={{0}};
  uint64_t gnon[10]={0}, gacc[10]={0}, gtot[10]={0}, gcomp[10]={0}, grefp[10]={0}, gaccp[10]={0};
  for(uint64_t n=2;n<=X;n++){
    int d=(int)floor(log10((double)n)); if(d>9) d=9; int g=G(n); uint64_t A=a[n]-g;
    gtot[d]++; if(A==0){ gnon[d]++; if(g) gacc[d]++; }
    if(PRIME(n)){ if(g) gaccp[d]++; else grefp[d]++; } else if(g) gcomp[d]++;
  }
  for(int i=0;i<nl;i++) for(uint64_t n=L[i];n<=X;n+=L[i]){ int d=(int)floor(log10((double)n)); if(d>9) d=9; int g=G(n); uint64_t A=a[n]-g;
    if(A==0){ nonrep[i][d]++; if(g) acc[i][d]++; } if(g && n!=L[i]) car[i][d]++; }
  printf("decade [10^d,10^(d+1)): non-representable n (A=0), g-primes, acceptance = g/non-rep, acceptance*ln(10^(d+0.5)); accepted primes, refused primes, composite g-primes\n");
  for(int d=1;d<=8;d++) printf("  d=%d  nonrep=%llu (%.4f of n)  g=%llu  acc=%.5f  acc*ln=%.3f  accepted primes=%llu refused primes=%llu composite g-primes=%llu\n",d,(unsigned long long)gnon[d],(double)gnon[d]/gtot[d],(unsigned long long)gacc[d],(double)gacc[d]/gnon[d],(double)gacc[d]/gnon[d]*log(pow(10,d+0.5)),(unsigned long long)gaccp[d],(unsigned long long)grefp[d],(unsigned long long)gcomp[d]);
  printf("refused prime l: carriers per decade d=3..8 (composite g-primes q in [10^d,10^(d+1)) with l | q), cumulative to 10^9; acceptance of non-representable multiples of l in decade 8 (x ln 10^8.5)\n");
  for(int i=0;i<nl;i++){ uint64_t cum=0; printf("  l=%4llu:",(unsigned long long)L[i]); for(int d=0;d<=8;d++){ cum+=car[i][d]; if(d>=3) printf(" %8llu",(unsigned long long)car[i][d]); }
    printf("  cum=%9llu  l*cum/1e9=%.3f  acc8=%.5f (x ln=%.3f)  nonrep8/mult8=%.4f\n",(unsigned long long)cum,(double)L[i]*cum/1e9,(double)acc[i][8]/nonrep[i][8],(double)acc[i][8]/nonrep[i][8]*log(pow(10,8.5)),(double)nonrep[i][8]/(9e8/L[i])); }
  return 0;
}
