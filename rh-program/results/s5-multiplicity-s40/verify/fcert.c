/* fcert.c -- unit s5-multiplicity-s40, close K.  EXACT f_G(n), G = g-primes <= 10^9 of S5(4/5), for n = n0 * p_1 * ... * p_j
   (p_i distinct primes not dividing n0, j <= 4), with memory tau(n0) only:
     (1) F[T] = f_G(T) for every T | n0: unbounded-knapsack DP on the divisor lattice of n0, unsigned __int128, adds checked;
     (2) top primes by the p-adic derivation identity at exponent 1 (NOTE §2):  f(m) = sum_{g in G, p | g | m} f(m/g)  for p || m,
         applied to the largest remaining top prime, memoized on (divisor of n0, subset of top primes).
   Writes every g-prime divisor of n (decimal, one per line) to the list file.  Prints f_G(n) exactly and the K test
   f > 2*1.88*n^0.35 + 3 (evaluated with mpmath-free long double logs AND an exact integer comparison in the log file
   produced by the Python checker).  Build: cc -O3 -o fcert fcert.c -lm
   Usage: fcert gbits.bin listfile n0-items... / top-primes...      (items p or p^e)  */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
typedef unsigned __int128 u128; static int ovf=0;
static uint8_t *gb; static const uint64_t LIM=1000000000ULL;
static int isg(uint64_t v){ return v>=2 && v<=LIM && ((gb[v>>3]>>(v&7))&1); }
static int r, e[64]; static uint64_t P[64], w[65], tau; static u128 *F;
static uint64_t nd=0,dcap=0,*dv=0,*di=0; static uint8_t *dx=0;
static int nt; static uint64_t TP[8];
static void pr(FILE *o,u128 x){ char t[64]; int k=0; if(!x){fputc('0',o);return;} while(x){t[k++]='0'+(int)(x%10);x/=10;} while(k) fputc(t[--k],o); }
/* memo: open addressing on key (idx<<8 | mask) */
static uint64_t *LS[256], LN[256];
static uint64_t HM=1<<22; static uint64_t *hk; static u128 *hv;
static u128 ftop(uint64_t idx, int mask){
  if(!mask) return F[idx];
  uint64_t key=(idx<<8)|(uint64_t)mask, h=(key*0x9E3779B97F4A7C15ULL)>>40; h&=HM-1;
  while(hk[h]){ if(hk[h]==key+1) return hv[h]; h=(h+1)&(HM-1); }
  int i=31-__builtin_clz(mask); uint64_t p=TP[i]; int rest=mask&~(1<<i);
  /* exponents of T from idx */
  int x[64]; uint64_t t=idx; for(int d=0;d<r;d++){ x[d]=(int)(t%(uint64_t)(e[d]+1)); t/=(uint64_t)(e[d]+1); }
  u128 tot=0;
  for(int sub=rest;;sub=(sub-1)&rest){           /* g = p * prod_{k in sub} TP[k] * d0, d0 | T, from the precomputed list */
    int B=sub|(1<<i); for(uint64_t c=0;c<LN[B];c++){ uint64_t s=LS[B][c];
      uint8_t *v=dx+s*64; int ok=1; for(int d=0;d<r;d++) if(v[d]>x[d]){ok=0;break;} if(!ok) continue;
      u128 add=ftop(idx-di[s], rest&~sub); u128 o=tot; tot+=add; if(tot<o) ovf=1; }
    if(!sub) break;
  }
  hk[h]=key+1; hv[h]=tot; return tot;
}
int main(int argc,char**argv){
  FILE *fb=fopen(argv[1],"rb"); gb=malloc(LIM/8+1); if(fread(gb,1,LIM/8+1,fb)!=LIM/8+1) return 1; fclose(fb);
  FILE *fl=fopen(argv[2],"w"); int ai=3, top=0; r=0; nt=0;
  for(;ai<argc;ai++){ if(!strcmp(argv[ai],"/")){top=1;continue;} char *c=strchr(argv[ai],'^'); uint64_t p=strtoull(argv[ai],0,10); int ee=c?atoi(c+1):1;
    if(top) TP[nt++]=p; else { P[r]=p; e[r]=ee; r++; } }
  w[0]=1; for(int d=0;d<r;d++) w[d+1]=w[d]*(uint64_t)(e[d]+1); tau=w[r];
  long double l10=0; for(int d=0;d<r;d++) l10+=e[d]*log10l((long double)P[d]); for(int k=0;k<nt;k++) l10+=log10l((long double)TP[k]);
  { int x[64]; memset(x,0,sizeof x); uint64_t val=1,idx=0; int k;
    for(;;){ if(nd==dcap){dcap=dcap?2*dcap:1<<16; dv=realloc(dv,dcap*8); di=realloc(di,dcap*8); dx=realloc(dx,dcap*64);}
      dv[nd]=val; di[nd]=idx; for(int d=0;d<r;d++) dx[nd*64+d]=(uint8_t)x[d]; nd++;
      for(k=0;k<r;k++){ if(x[k]<e[k] && val<=LIM/P[k]){ x[k]++; val*=P[k]; idx+=w[k]; break; } while(x[k]>0){ x[k]--; val/=P[k]; idx-=w[k]; } }
      if(k==r) break; } }
  F=calloc(tau,sizeof(u128)); if(!F){fprintf(stderr,"oom\n");return 1;} F[0]=1; uint64_t ng=0;
  for(uint64_t t=0;t<nd;t++){ if(!isg(dv[t])) continue; ng++; fprintf(fl,"%llu\n",(unsigned long long)dv[t]);
    uint8_t *v=dx+t*64; uint64_t off=di[t]; int j[64]; memset(j,0,sizeof(int)*r); uint64_t s=0; int run=e[0]-v[0];
    for(;;){ u128 *d=F+s+off, *q=F+s; for(int z=0;z<=run;z++){ u128 o=d[z]; d[z]+=q[z]; if(d[z]<o) ovf=1; }
      int i; for(i=1;i<r;i++){ if(j[i]<e[i]-v[i]){ j[i]++; s+=w[i]; break; } s-=(uint64_t)j[i]*w[i]; j[i]=0; } if(i>=r) break; } }
  /* g-prime divisors involving top primes, for the list */
  for(int sub=1;sub<(1<<nt);sub++){ uint64_t pp=1; int okp=1; LN[sub]=0; LS[sub]=NULL; uint64_t cp=0;
    for(int k=0;k<nt;k++) if(sub&(1<<k)){ if(pp>LIM/TP[k]){okp=0;break;} pp*=TP[k]; }
    if(okp) for(uint64_t t=0;t<nd;t++){ if(dv[t]>LIM/pp) continue; if(isg(dv[t]*pp)){ ng++; fprintf(fl,"%llu\n",(unsigned long long)(dv[t]*pp));
      if(LN[sub]==cp){ cp=cp?2*cp:1024; LS[sub]=realloc(LS[sub],cp*8); } LS[sub][LN[sub]++]=t; } } }
  fclose(fl);
  hk=calloc(HM,8); hv=calloc(HM,sizeof(u128));
  u128 f=ftop(tau-1,(1<<nt)-1);
  printf("n0 ="); for(int d=0;d<r;d++) printf(" %llu^%d",(unsigned long long)P[d],e[d]); printf("  top ="); for(int k=0;k<nt;k++) printf(" %llu",(unsigned long long)TP[k]);
  printf("\nlog10 n = %.6Lf  tau(n0) = %llu  g-prime divisors of n = %llu  f_G(n) = ",l10,(unsigned long long)tau,(unsigned long long)ng); pr(stdout,f);
  long double lf=log10l((long double)f), thr=log10l(3.76L)+0.35L*l10;
  printf("\noverflow = %d  log10 f = %.6Lf  log10(3.76 n^0.35) = %.6Lf  margin = %+.6Lf  exponent = %.6Lf\n",ovf,lf,thr,lf-thr,lf/l10);
  return 0;
}
