/* fsplit.c -- unit s5-multiplicity-s40, task 2.  Rigorous LOWER bound for a_n of S5(4/5) at n = S * prod_{p in L} p^{e_p}, by an
   exact count of a SUBSET of the factorizations of n into g-primes <= 10^9: those in which every factor contains at most one
   prime of L, to the first power ("one-L-prime factorizations").  Every such multiset splits uniquely into (i) its pure part
   (factors dividing S) and (ii) for each p in L, e_p carriers s*p with s | S, s*p a g-prime <= 10^9 (s = 1 iff p itself is a
   g-prime).  So   F_split(n) = sum_{T | S} h(T) f_pure(S/T),   h = *_{p in L} (multisets of e_p carriers of p),  and
   F_split(n) <= f_G(n) <= a_n.   Lattice: divisors of S only (tau(S) cells).
   Build: cc -O3 -o fsplit fsplit.c -lm  (double) ;  cc -O3 -DEXACT -o fsplitx fsplit.c -lm  (unsigned __int128, overflow-checked)
   Usage: fsplit gbits.bin [-l listfile] S-items... / L-items...      items: p or p^e  */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#ifdef EXACT
typedef unsigned __int128 num; static int ovf=0;
#define ADD(d,s) do{ num _o=(d); (d)+=(s); if((d)<_o) ovf=1; }while(0)
#else
typedef double num; static int ovf=0;
#define ADD(d,s) ((d)+=(s))
#endif
static uint8_t *gb; static const uint64_t LIM=1000000000ULL;
static int isg(uint64_t v){ return v>=2 && v<=LIM && ((gb[v>>3]>>(v&7))&1); }
static int r; static int e[64]; static uint64_t P[64], w[65], tau;
static uint64_t nd=0; static uint64_t *dv; static int *dx;   /* divisors of S that are <= LIM: value, exponent vector */
static void shift_add(num *dst, const num *src, const int *v){  /* dst[T] += src[T - v] over the sub-box T >= v, increasing order */
  uint64_t off=0; for(int i=0;i<r;i++) off+=v[i]*w[i];
  int j[64]; memset(j,0,sizeof(int)*r); uint64_t s=0; int run=e[0]-v[0];
  for(;;){ num *d=dst+s+off; const num *q=src+s; for(int t=0;t<=run;t++) ADD(d[t],q[t]);
    int i; for(i=1;i<r;i++){ if(j[i]<e[i]-v[i]){ j[i]++; s+=w[i]; break; } s-=(uint64_t)j[i]*w[i]; j[i]=0; } if(i>=r) break; }
}
static void pr(num x){
#ifdef EXACT
  char t[64]; int k=0; if(!x){printf("0");return;} while(x){t[k++]='0'+(int)(x%10);x/=10;} while(k) putchar(t[--k]);
#else
  printf("%.6e",x);
#endif
}
int main(int argc,char**argv){
  FILE *fb=fopen(argv[1],"rb"); gb=malloc(LIM/8+1); if(fread(gb,1,LIM/8+1,fb)!=LIM/8+1) return 1; fclose(fb);
  int ai=2; FILE *fl=NULL; if(!strcmp(argv[ai],"-l")){ fl=fopen(argv[ai+1],"w"); ai+=2; }
  uint64_t Lp[256]; int Le[256], nl=0; int inL=0; r=0;
  for(;ai<argc;ai++){ if(!strcmp(argv[ai],"/")){inL=1;continue;} char *c=strchr(argv[ai],'^'); uint64_t p=strtoull(argv[ai],0,10); int ee=c?atoi(c+1):1;
    if(inL){Lp[nl]=p;Le[nl]=ee;nl++;} else {P[r]=p;e[r]=ee;r++;} }
  w[0]=1; for(int i=0;i<r;i++) w[i+1]=w[i]*(uint64_t)(e[i]+1); tau=w[r];
  double l10=0; for(int i=0;i<r;i++) l10+=e[i]*log10((double)P[i]); for(int i=0;i<nl;i++) l10+=Le[i]*log10((double)Lp[i]);
  uint64_t cap=1<<16; dv=malloc(cap*8); dx=malloc(cap*64*sizeof(int));
  { int x[64]; memset(x,0,sizeof x); uint64_t val=1; int k;
    for(;;){ if(nd==cap){cap*=2; dv=realloc(dv,cap*8); dx=realloc(dx,cap*64*sizeof(int));} dv[nd]=val; memcpy(dx+nd*64,x,sizeof(int)*r); nd++;
      for(k=0;k<r;k++){ if(x[k]<e[k] && val<=LIM/P[k]){ x[k]++; val*=P[k]; break; } while(x[k]>0){ x[k]--; val/=P[k]; } } if(k==r) break; } }
  num *fp=calloc(tau,sizeof(num)); fp[0]=1; uint64_t npure=0;
  for(uint64_t t=0;t<nd;t++) if(isg(dv[t])){ npure++; if(fl) fprintf(fl,"pure %llu\n",(unsigned long long)dv[t]); shift_add(fp,fp,dx+t*64); }
  int emax=1; for(int i=0;i<nl;i++) if(Le[i]>emax) emax=Le[i];
  num **H=malloc((emax+1)*sizeof(num*)); for(int k=0;k<=emax;k++) H[k]=calloc(tau,sizeof(num));
  H[0][0]=1; uint64_t ncar=0;
  for(int i=0;i<nl;i++){ uint64_t p=Lp[i]; int ee=Le[i]; uint64_t nc=0;
    for(int k=1;k<=ee;k++) memset(H[k],0,tau*sizeof(num));
    for(uint64_t t=0;t<nd;t++){ uint64_t s=dv[t]; if(s>LIM/p) continue; uint64_t c=s*p; if(!isg(c)) continue; nc++;
      if(fl) fprintf(fl,"carrier %llu = %llu*%llu\n",(unsigned long long)c,(unsigned long long)s,(unsigned long long)p);
      for(int k=1;k<=ee;k++) shift_add(H[k],H[k-1],dx+t*64); }
    if(ee>0){ num *tmp=H[0]; H[0]=H[ee]; H[ee]=tmp; }
    ncar+=nc; printf("  L-prime %llu^%d: %llu carriers\n",(unsigned long long)p,ee,(unsigned long long)nc);
  }
  num tot=0;
#ifdef EXACT
  for(uint64_t T=0;T<tau;T++){ if(H[0][T]&&fp[tau-1-T]){ num a=H[0][T], b=fp[tau-1-T]; num m=a*b; if(a && m/a!=b) ovf=1; ADD(tot,m);} }
#else
  for(uint64_t T=0;T<tau;T++) tot+=H[0][T]*fp[tau-1-T];
#endif
  printf("S ="); for(int i=0;i<r;i++) printf(" %llu^%d",(unsigned long long)P[i],e[i]); printf("  L ="); for(int i=0;i<nl;i++) printf(" %llu^%d",(unsigned long long)Lp[i],Le[i]);
  printf("\nlog10 n = %.4f  tau(S) = %llu  pure g-primes = %llu  carriers = %llu  F_split(n) = ",l10,(unsigned long long)tau,(unsigned long long)npure,(unsigned long long)ncar); pr(tot);
#ifdef EXACT
  double dt=(double)tot;
#else
  double dt=tot;
#endif
  printf("  overflow = %d  log f/log n = %.5f  excess35(log10) = %+.4f\n",ovf,log10(dt)/l10,log10(dt)-0.35*l10-log10(3.76));
  if(fl) fclose(fl); return 0;
}
