/* search.c -- unit s5-multiplicity-s40, task 2.  Exploration of f_G(n) (G = g-primes <= 10^9 of S5(4/5)) over exponent vectors.
   Evaluation: the divisor-lattice DP of fcount.c in DOUBLE precision (exploration only; every reported bound is recounted
   exactly by fcount).  Modes:
     greedy  : from a start vector, repeatedly apply the +1 move (over the first K primes) of best rate dln f / dln n;
     polish  : at each step also try swap moves (-1 on q, +1 on p) and keep any that raise ln f - theta ln n.
   Usage: search gbits.bin K taumax maxlog10 theta mode e1 e2 ... eK   (start exponents for the first K primes)
   Build: cc -O3 -o search search.c -lm */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#include <time.h>
static uint8_t *gb; static const uint64_t LIM=1000000000ULL;
static int isg(uint64_t v){ return v>=2 && v<=LIM && ((gb[v>>3]>>(v&7))&1); }
static int K; static uint64_t PR[64]; static double *F=NULL; static uint64_t Fcap=0;
static uint64_t gcap=0; static int *gx=NULL;
static double eval(const int *e0, uint64_t taumax, uint64_t *taup, uint64_t *ngp){
  int r=0, e[64]; uint64_t P[64]; for(int i=0;i<K;i++) if(e0[i]>0){ P[r]=PR[i]; e[r]=e0[i]; r++; }
  uint64_t w[65]; w[0]=1; for(int i=0;i<r;i++){ w[i+1]=w[i]*(uint64_t)(e[i]+1); if(w[i+1]>taumax) return -1; }
  uint64_t tau=w[r]; *taup=tau;
  if(tau>Fcap){ free(F); F=malloc(tau*sizeof(double)); Fcap=tau; }
  memset(F,0,tau*sizeof(double)); F[0]=1;
  uint64_t ng=0; int x[64]; memset(x,0,sizeof x); uint64_t val=1; int k;
  for(;;){
    if(isg(val)){ if(ng>=gcap){ gcap=gcap?2*gcap:65536; gx=realloc(gx,gcap*64*sizeof(int)); } memcpy(gx+ng*64,x,sizeof(int)*r); ng++; }
    for(k=0;k<r;k++){ if(x[k]<e[k] && val<=LIM/P[k]){ x[k]++; val*=P[k]; break; } while(x[k]>0){ x[k]--; val/=P[k]; } }
    if(k==r) break;
  }
  *ngp=ng;
  for(uint64_t t=0;t<ng;t++){
    int *v=gx+t*64; uint64_t off=0; for(int i=0;i<r;i++) off+=v[i]*w[i];
    int j[64]; memset(j,0,sizeof(int)*r); uint64_t src=0; int run=e[0]-v[0];
    for(;;){
      double *d=F+src+off, *s=F+src; for(int q=0;q<=run;q++) d[q]+=s[q];
      int i; for(i=1;i<r;i++){ if(j[i]<e[i]-v[i]){ j[i]++; src+=w[i]; break; } src-=(uint64_t)j[i]*w[i]; j[i]=0; }
      if(i>=r) break;
    }
  }
  return log(F[tau-1]);
}
static double lnn(const int *e){ double s=0; for(int i=0;i<K;i++) s+=e[i]*log((double)PR[i]); return s; }
static void show(const char *tag,const int *e,double lf,uint64_t tau,uint64_t ng,double rate,double t0){
  double ln=lnn(e); printf("%s log10n=%7.3f log10f=%8.4f expo=%.5f rate=%.3f excess35=%+.4f tau=%llu gdiv=%llu t=%.0fs n=",tag,ln/log(10),lf/log(10),lf/ln,rate,(lf-0.35*ln-log(3.76))/log(10),(unsigned long long)tau,(unsigned long long)ng,(double)clock()/CLOCKS_PER_SEC-t0);
  for(int i=0;i<K;i++) if(e[i]) printf("%llu^%d ",(unsigned long long)PR[i],e[i]); printf("\n"); fflush(stdout); }
int main(int argc,char**argv){
  FILE *fb=fopen(argv[1],"rb"); gb=malloc(LIM/8+1); fread(gb,1,LIM/8+1,fb); fclose(fb);
  K=atoi(argv[2]); uint64_t taumax=strtoull(argv[3],0,10); double maxlog=atof(argv[4]), theta=atof(argv[5]); const char *mode=argv[6];
  int np=0; for(uint64_t c=2;np<K;c++){ int ok=1; for(uint64_t d=2;d*d<=c;d++) if(c%d==0){ok=0;break;} if(ok) PR[np++]=c; }
  int e[64]; for(int i=0;i<K;i++) e[i]=atoi(argv[7+i]);
  double t0=(double)clock()/CLOCKS_PER_SEC; uint64_t tau,ng; double lf=eval(e,taumax,&tau,&ng); show("start",e,lf,tau,ng,0,t0);
  while(lnn(e)/log(10)<maxlog){
    int bi=-1; double br=-1e9, blf=0; uint64_t bt=0,bg=0;
    for(int i=0;i<K;i++){ e[i]++; uint64_t t2,g2; double l2=eval(e,taumax,&t2,&g2); e[i]--; if(l2<0) continue;
      double rate=(l2-lf)/log((double)PR[i]); if(rate>br){br=rate;bi=i;blf=l2;bt=t2;bg=g2;} }
    if(bi<0){ printf("tau cap reached\n"); break; }
    e[bi]++; lf=blf; tau=bt; ng=bg; show("step ",e,lf,tau,ng,br,t0);
    if(!strcmp(mode,"polish")){
      int improved=1, rounds=0;
      while(improved && rounds<4){ improved=0; rounds++;
        for(int q=0;q<K;q++) if(e[q]>0) for(int p=0;p<K;p++) if(p!=q){
          e[q]--; e[p]++; uint64_t t2,g2; double l2=eval(e,taumax,&t2,&g2);
          double gain=(l2-theta*lnn(e))-(lf-theta*(lnn(e)-log((double)PR[p])+log((double)PR[q])));
          if(l2>=0 && gain>1e-9 && lnn(e)/log(10)<maxlog+1){ lf=l2; tau=t2; ng=g2; improved=1; show("swap ",e,lf,tau,ng,gain,t0); }
          else { e[p]--; e[q]++; } } }
    }
  }
  return 0;
}
