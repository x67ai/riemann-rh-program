/* search2.c -- unit s5-multiplicity-s40, task 2.  Fast exploration of f_G(n), G = g-primes <= 10^9 of S5(4/5).
   One divisor-lattice DP (float) per accepted move; every candidate move is SCORED from that one array by the
   p-adic derivation identity (proved in NOTE §2):  v_p(m) f(m) = sum_{g in G, p | g} sum_{k>=1, g^k | m} v_p(g) f(m/g^k),
   whose right side only needs f at divisors of n when m = n*p or m = n*p/q.  Exploration only: every reported bound is
   recounted exactly (fcount / modular code).  Build: cc -O3 -o search2 search2.c -lm
   Usage: search2 gbits.bin K taucap maxlog10 mode e_1 ... e_K      mode: rate | xtau ;  polish swaps always on */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#include <time.h>
static uint8_t *gb; static const uint64_t LIM=1000000000ULL;
static int isg(uint64_t v){ return v>=2 && v<=LIM && ((gb[v>>3]>>(v&7))&1); }
static int K; static uint64_t PR[512]; static double LP[512];
static int E[512];                      /* current exponents */
static int r, dim2p[512], p2dim[512]; static uint64_t w[513], tau;
static float *F=NULL; static uint64_t Fcap=0;
static uint64_t nd, dcap=0; static uint64_t *dval=NULL, *didx=NULL; static uint8_t *dvec=NULL;  /* divisors <= LIM */
#define MAXR 64
static void build(void){
  r=0; for(int i=0;i<K;i++){ p2dim[i]=-1; if(E[i]>0){ dim2p[r]=i; p2dim[i]=r; r++; } }
  w[0]=1; for(int d=0;d<r;d++) w[d+1]=w[d]*(uint64_t)(E[dim2p[d]]+1); tau=w[r];
  if(tau>Fcap){ free(F); F=malloc(tau*sizeof(float)); Fcap=tau; if(!F){fprintf(stderr,"oom\n");exit(1);} }
  memset(F,0,tau*sizeof(float)); F[0]=1;
  nd=0; int x[MAXR]; memset(x,0,sizeof x); uint64_t val=1, idx=0; int k;
  for(;;){
    if(nd==dcap){ dcap=dcap?2*dcap:1<<16; dval=realloc(dval,dcap*8); didx=realloc(didx,dcap*8); dvec=realloc(dvec,dcap*MAXR); }
    dval[nd]=val; didx[nd]=idx; for(int d=0;d<r;d++) dvec[nd*MAXR+d]=(uint8_t)x[d]; nd++;
    for(k=0;k<r;k++){ uint64_t p=PR[dim2p[k]]; if(x[k]<E[dim2p[k]] && val<=LIM/p){ x[k]++; val*=p; idx+=w[k]; break; }
      while(x[k]>0){ x[k]--; val/=p; idx-=w[k]; } }
    if(k==r) break;
  }
  for(uint64_t t=0;t<nd;t++){ if(!isg(dval[t])) continue;
    uint8_t *v=dvec+t*MAXR; uint64_t off=didx[t]; int j[MAXR]; memset(j,0,sizeof(int)*r); uint64_t s=0; int run=E[dim2p[0]]-v[0];
    for(;;){ float *d=F+s+off, *q=F+s; for(int z=0;z<=run;z++) d[z]+=q[z];
      int i; for(i=1;i<r;i++){ if(j[i]<E[dim2p[i]]-v[i]){ j[i]++; s+=w[i]; break; } s-=(uint64_t)j[i]*w[i]; j[i]=0; } if(i>=r) break; }
  }
}
/* f(n * p / q) (q = -1: no removal), from F by the v_p identity.  Returns natural log (or -inf). */
static double score(int pi, int qi){
  uint64_t p=PR[pi]; int ep=E[pi]; int dp=p2dim[pi], dq=(qi>=0)?p2dim[qi]:-1;
  if(qi>=0 && E[qi]==0) return -INFINITY;
  int mexp[MAXR+1]; for(int d=0;d<r;d++) mexp[d]=E[dim2p[d]]; if(dq>=0) mexp[dq]--;
  double tot=0;
  for(uint64_t t=0;t<nd;t++){ uint64_t dv=dval[t]; if(dv>LIM/p) continue; uint64_t g=dv*p; if(!isg(g)) continue;
    uint8_t *v=dvec+t*MAXR; int ok=1; for(int d=0;d<r;d++) if(v[d]>mexp[d]){ok=0;break;} if(!ok) continue;
    int gv[MAXR+1]; for(int d=0;d<r;d++) gv[d]=v[d]; int vpg=1+(dp>=0?v[dp]:0);  /* v_p(g) */
    /* m = n p / q ; exponents of m: mexp (with p coordinate ep+1) */
    for(int k=1;;k++){ int ok2=1; if(k*vpg>ep+1) break; for(int d=0;d<r;d++){ int need=k*gv[d]+((d==dp)?k:0); int have=mexp[d]+((d==dp)?1:0); if(need>have){ok2=0;break;} } if(!ok2) break;
      uint64_t idx=0; for(int d=0;d<r;d++){ int ex=mexp[d]+((d==dp)?1:0)-k*gv[d]-((d==dp)?k:0); idx+=(uint64_t)ex*w[d]; }
      tot+=(double)vpg*F[idx]; }
  }
  if(tot<=0) return -INFINITY; return log(tot/(double)(ep+1));
}
static double lnn(void){ double s=0; for(int i=0;i<K;i++) s+=E[i]*LP[i]; return s; }
static void show(const char *tag,double lf,double extra,double t0){
  double ln=lnn(); uint64_t ng=0; for(uint64_t t=0;t<nd;t++) if(isg(dval[t])) ng++;
  printf("%s log10n=%7.3f log10f=%8.4f expo=%.5f excess35=%+.4f x=%.3f tau=%llu gdiv=%llu t=%.0fs n=",tag,ln/log(10),lf/log(10),lf/ln,(lf-0.35*ln-log(3.76))/log(10),extra,(unsigned long long)tau,(unsigned long long)ng,(double)clock()/CLOCKS_PER_SEC-t0);
  for(int i=0;i<K;i++) if(E[i]) printf("%llu^%d ",(unsigned long long)PR[i],E[i]); printf("\n"); fflush(stdout); }
int main(int argc,char**argv){
  FILE *fb=fopen(argv[1],"rb"); gb=malloc(LIM/8+1); if(fread(gb,1,LIM/8+1,fb)!=LIM/8+1) return 1; fclose(fb);
  K=atoi(argv[2]); uint64_t cap=strtoull(argv[3],0,10); double maxlog=atof(argv[4]); const char *mode=argv[5];
  int np=0; for(uint64_t c=2;np<K;c++){ int ok=1; for(uint64_t d=2;d*d<=c;d++) if(c%d==0){ok=0;break;} if(ok){ PR[np]=c; LP[np]=log((double)c); np++; } }
  for(int i=0;i<K;i++) E[i]=(6+i<argc)?atoi(argv[6+i]):0;
  double t0=(double)clock()/CLOCKS_PER_SEC; build(); double lf=log((double)F[tau-1]); show("start",lf,0,t0);
  while(lnn()/log(10)<maxlog){
    int bi=-1; double bo=-1e300, bs=0;
    for(int i=0;i<K;i++){ double t2=(double)tau*(E[i]+2)/(E[i]+1); if(t2>cap) continue; double s=score(i,-1); if(!isfinite(s)) continue;
      double o = !strcmp(mode,"rate") ? (s-lf)/LP[i] : (s-lf-0.35*LP[i])/log(t2/(double)tau);
      if(o>bo){bo=o;bi=i;bs=s;} }
    if(bi<0){ printf("cap reached\n"); break; }
    E[bi]++; build(); double chk=log((double)F[tau-1]); lf=chk; show("step ",lf,bo,t0);
    if(fabs(chk-bs)>1e-3) printf("  WARNING score %.6f vs DP %.6f\n",bs,chk);
    for(int round=0;round<50;round++){
      int bq=-1,bp=-1; double bd=1e-7;
      for(int q=0;q<K;q++) if(E[q]>0) for(int p=0;p<K;p++) if(p!=q){
        double t2=(double)tau/(E[q]+1)*E[q]/(E[p]+1)*(E[p]+2); if(t2>(double)tau*1.0000001) continue;
        double s=score(p,q); if(!isfinite(s)) continue; double dX=(s-lf)-0.35*(LP[p]-LP[q]);
        if(dX>bd){bd=dX;bq=q;bp=p;} }
      if(bq<0) break;
      E[bq]--; E[bp]++; build(); lf=log((double)F[tau-1]); show("swap ",lf,bd,t0);
    }
  }
  return 0;
}
