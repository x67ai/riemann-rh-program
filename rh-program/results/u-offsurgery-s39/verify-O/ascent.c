/* ascent.c -- greedy ascent for lower bounds a_n >= f(n) = #factorizations of n into the g-primes <= 1e9 (read-O, S40, C3/C4).
   Pre-extracts the g-primes that are smooth over the first K0 primes, then from a start vector repeatedly multiplies n by the
   prime p maximizing the marginal exponent log(f(np)/f(n))/log p (candidates: primes dividing n, plus the two smallest absent).
   Exact uint64 DP over the divisor lattice (overflow flagged). Stops at lattice cap, log10 n cap, or time cap.
   usage: ascent file.gp "e1,e2,...,eK0" log10cap latticecap seconds */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#include <time.h>
#define K0 18
static const uint64_t PR[K0]={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61};
typedef struct { uint8_t v[K0]; } GV; static GV *gv; static int ng=0;
static int ovf;
static uint64_t evalf(const int *E, uint64_t cap, int *toolarge){
  uint64_t st[K0+1]; st[0]=1; for(int i=0;i<K0;i++) st[i+1]=st[i]*(uint64_t)(E[i]+1);
  uint64_t L=st[K0]; if(L>cap){*toolarge=1; return 0;} *toolarge=0;
  uint64_t *f=calloc(L,8); f[0]=1; int e[K0];
  for(int g=0; g<ng; g++){ const uint8_t *v=gv[g].v; int ok=1; for(int i=0;i<K0;i++) if(v[i]>E[i]){ok=0;break;} if(!ok) continue;
    uint64_t off=0; for(int i=0;i<K0;i++) off+=v[i]*st[i];
    for(int i=0;i<K0;i++) e[i]=v[i];
    for(;;){ uint64_t base=0; for(int i=1;i<K0;i++) base+=e[i]*st[i];
      for(int x=v[0];x<=E[0];x++){ uint64_t d=base+x, s=f[d]+f[d-off]; if(s<f[d]) ovf=1; f[d]=s; }
      int i=1; while(i<K0){ if(++e[i]<=E[i]) break; e[i]=v[i]; i++; } if(i>=K0) break; }
  }
  uint64_t r=f[L-1]; free(f); return r;
}
static void pr_n(const int *E){ int first=1; for(int i=0;i<K0;i++) if(E[i]){ printf("%s%llu",first?"":"*",(unsigned long long)PR[i]); if(E[i]>1) printf("^%d",E[i]); first=0; } }
int main(int argc,char**argv){
  FILE *fp=fopen(argv[1],"rb"); uint32_t q; uint8_t m; int cap=1<<16; gv=malloc(cap*sizeof(GV));
  while(fread(&q,4,1,fp)==1 && fread(&m,1,1,fp)==1){ uint64_t t=q; GV g; for(int i=0;i<K0;i++){ g.v[i]=0; while(t%PR[i]==0){t/=PR[i]; g.v[i]++;} }
    if(t!=1) continue; if(m!=1){fprintf(stderr,"multiplicity %d at %u not handled\n",m,q); return 1;} if(ng==cap){cap*=2; gv=realloc(gv,cap*sizeof(GV));} gv[ng++]=g; }
  fclose(fp); fprintf(stderr,"%d g-primes <= 1e9 smooth over primes <= 61\n",ng);
  int E[K0]={0}; { char *s=strdup(argv[2]); int i=0; for(char*t=strtok(s,",");t&&i<K0;t=strtok(0,",")) E[i++]=atoi(t); }
  double l10cap=atof(argv[3]); uint64_t Lcap=(uint64_t)atof(argv[4]); double tcap=atof(argv[5]); time_t t0=time(0);
  int tl; uint64_t f=evalf(E,Lcap,&tl); double l10=0; for(int i=0;i<K0;i++) l10+=E[i]*log10((double)PR[i]);
  printf("step 0  log10n %.4f  f %llu  exp %.5f  n = ",l10,(unsigned long long)f,log10((double)f)/l10); pr_n(E); printf("\n"); fflush(stdout);
  for(int step=1;;step++){
    int best=-1; double bm=-1; uint64_t bf=0; int absent=0;
    for(int j=0;j<K0;j++){ if(E[j]==0){ if(absent>=2) continue; absent++; }
      E[j]++; uint64_t fj=evalf(E,Lcap,&tl); E[j]--; if(tl) continue;
      double mg=(log((double)fj)-log((double)f))/log((double)PR[j]); if(mg>bm){bm=mg;best=j;bf=fj;} }
    if(best<0){ printf("# stop: lattice cap\n"); break; }
    E[best]++; f=bf; l10+=log10((double)PR[best]);
    printf("step %d  x%llu  log10n %.4f  f %llu  exp %.5f  marg %.4f  2n^.35 %.4g  n = ",step,(unsigned long long)PR[best],l10,(unsigned long long)f,log10((double)f)/l10,bm,2*pow(10,0.35*l10)); pr_n(E);
    printf("  ovf=%d  t=%lds\n",ovf,(long)(time(0)-t0)); fflush(stdout);
    if(l10>l10cap || difftime(time(0),t0)>tcap) { printf("# stop: cap\n"); break; }
  }
  return 0;
}
