/* fcount.c -- unit s5-multiplicity-s40, tasks 1-2.  EXACT count of f_G(n) = #{multisets of g-primes q <= 10^9 with product n}
   for S5(4/5), G = the 50,829,666 g-primes <= 10^9 (all m_q = 1), read from a bitset built from gpF_r08_1e9.u32.
   f_G(n) <= a_n for every n (g-primes <= 10^9 are fixed forever by the deterministic rule; later g-primes only add multisets).
   Method: unbounded-knapsack DP over the divisor lattice of n (mixed radix, tau(n) cells, unsigned __int128, every add
   overflow-checked).  Usage: fcount gbits.bin [-l listfile] p1^e1 p2^e2 ...   (primes in any order; ^1 may be omitted)
   Output: n's factorization, log10 n, tau(n), #g-prime divisors, f_G(n) exact (decimal), log f / log n.
   With -l, writes the g-prime divisors used (one per line, decimal) to listfile.  Build: cc -O2 -o fcount fcount.c -lm */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
typedef unsigned __int128 u128;
static uint8_t *gb; static const uint64_t LIM=1000000000ULL;
static int isg(uint64_t v){ return v>=2 && v<=LIM && ((gb[v>>3]>>(v&7))&1); }
static void pr128(u128 x, char *buf){ char t[64]; int k=0; if(!x){strcpy(buf,"0");return;} while(x){t[k++]='0'+(int)(x%10);x/=10;} for(int i=0;i<k;i++)buf[i]=t[k-1-i]; buf[k]=0; }
int main(int argc,char**argv){
  if(argc<3){fprintf(stderr,"usage\n");return 1;}
  FILE *fb=fopen(argv[1],"rb"); gb=malloc(LIM/8+1); if(fread(gb,1,LIM/8+1,fb)!=LIM/8+1){fprintf(stderr,"bitset read\n");return 1;} fclose(fb);
  int ai=2; const char *lf=NULL; if(!strcmp(argv[ai],"-l")){lf=argv[ai+1];ai+=2;}
  int r=argc-ai; uint64_t P[64]; int e[64];
  for(int i=0;i<r;i++){ char *c=strchr(argv[ai+i],'^'); P[i]=strtoull(argv[ai+i],0,10); e[i]=c?atoi(c+1):1; }
  uint64_t w[65]; w[0]=1; for(int i=0;i<r;i++){ w[i+1]=w[i]*(uint64_t)(e[i]+1); }
  uint64_t tau=w[r]; double l10=0; for(int i=0;i<r;i++) l10+=e[i]*log10((double)P[i]);
  /* enumerate divisors <= LIM that are g-primes: DFS */
  uint64_t cap=1<<20, ng=0; uint64_t *gv=malloc(cap*8); int *gx=malloc(cap*sizeof(int)*r);
  int x[64]; memset(x,0,sizeof x);
  /* iterative odometer over exponent vectors, pruning values > LIM */
  uint64_t val=1; int k=0;
  for(;;){
    if(isg(val)){ if(ng==cap){cap*=2; gv=realloc(gv,cap*8); gx=realloc(gx,cap*sizeof(int)*r);} gv[ng]=val; memcpy(gx+ng*r,x,sizeof(int)*r); ng++; }
    /* increment */
    for(k=0;k<r;k++){ if(x[k]<e[k] && val<=LIM/P[k]){ x[k]++; val*=P[k]; break; } while(x[k]>0){ x[k]--; val/=P[k]; } }
    if(k==r) break;
  }
  if(lf){ FILE *fl=fopen(lf,"w"); for(uint64_t t=0;t<ng;t++) fprintf(fl,"%llu\n",(unsigned long long)gv[t]); fclose(fl); }
  u128 *f=calloc(tau,sizeof(u128)); if(!f){fprintf(stderr,"oom tau=%llu\n",(unsigned long long)tau);return 1;}
  f[0]=1; int ovf=0;
  for(uint64_t t=0;t<ng;t++){
    int *v=gx+t*r; uint64_t off=0; for(int i=0;i<r;i++) off+=v[i]*w[i];
    int j[64]; memset(j,0,sizeof(int)*r); uint64_t src=0; int run=e[0]-v[0];
    for(;;){
      u128 *d=f+src+off, *s=f+src;
      for(int q=0;q<=run;q++){ u128 o=d[q]; d[q]+=s[q]; if(d[q]<o) ovf=1; }
      int i; for(i=1;i<r;i++){ if(j[i]<e[i]-v[i]){ j[i]++; src+=w[i]; break; } src-=(uint64_t)j[i]*w[i]; j[i]=0; }
      if(i>=r) break;
    }
  }
  char buf[64]; pr128(f[tau-1],buf);
  printf("n ="); for(int i=0;i<r;i++) printf(" %llu^%d",(unsigned long long)P[i],e[i]);
  printf("\nlog10 n = %.4f  tau = %llu  g-prime divisors = %llu  f_G(n) = %s  overflow = %d  log f/log n = %.5f\n",l10,(unsigned long long)tau,(unsigned long long)ng,buf,ovf,log10((double)f[tau-1])/l10);
  return 0;
}
