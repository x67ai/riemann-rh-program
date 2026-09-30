/* pseudoN.c -- S5: integer-greedy ("self-regulated") N-supported Beurling system of density rho.
   g-primes are integers n >= 2 with multiplicity m_n >= 0 chosen greedily so that
   N(n) = sum_{k<=n} a(k) tracks T(n) = rho*(n-1)+1 (a(k) = #representations of k by g-primes).
   Output: log-binned stats of E(x)=N(x)-rho*x-(1-rho) and of psi_P(x)-x; optional dumps
   (a_n uint16 = final multiplicity of the g-integer n; g-prime list (n,m) uint32 pairs) into DUMPDIR.
   Usage: pseudoN rho X label [dumpdir|-] [delta]  (target rho(n-1)+1+delta)            Build: cc -O2 -o pseudoN pseudoN.c -lm */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <string.h>
typedef struct { uint64_t pos; double w; } PW;
static PW *hp; static long hn = 0, hcap = 0;
static void hpush(uint64_t pos, double w){ if(hn==hcap){hcap=hcap?2*hcap:1024;hp=realloc(hp,hcap*sizeof(PW));}
  long i=hn++; hp[i].pos=pos; hp[i].w=w; while(i>0){long p=(i-1)/2; if(hp[p].pos<=hp[i].pos)break; PW t=hp[p];hp[p]=hp[i];hp[i]=t;i=p;} }
static PW hpop(void){ PW r=hp[0]; hp[0]=hp[--hn]; long i=0; for(;;){long l=2*i+1,rr=l+1,s=i;
  if(l<hn&&hp[l].pos<hp[s].pos)s=l; if(rr<hn&&hp[rr].pos<hp[s].pos)s=rr; if(s==i)break; PW t=hp[s];hp[s]=hp[i];hp[i]=t;i=s;} return r; }
int main(int argc, char **argv){
  if(argc<4){fprintf(stderr,"usage\n");return 1;}
  double rho=atof(argv[1]); uint64_t X=(uint64_t)atof(argv[2]); const char *lab=argv[3];
  const char *dd = (argc>4 && argv[4][0]!='-')? argv[4]:NULL; double off = argc>5? atof(argv[5]):0.0;  /* target offset delta */
  uint16_t *a=calloc(X+1,sizeof(uint16_t)); if(!a){fprintf(stderr,"oom\n");return 1;}
  a[1]=1;
  FILE *fe=NULL,*fg=NULL; char fn[4096];
  if(dd){ snprintf(fn,sizeof fn,"%s/a_%s.u16",dd,lab); fe=fopen(fn,"wb");
          snprintf(fn,sizeof fn,"%s/gp_%s.u32",dd,lab); fg=fopen(fn,"wb"); }
  const int BPD=20; int nb=(int)(BPD*log10((double)X))+2;
  double *Emax=malloc(nb*8),*Emin=malloc(nb*8),*E2=malloc(nb*8),*Pmax=malloc(nb*8),*Pend=malloc(nb*8),*Pmx=malloc(nb*8),*Pmn=malloc(nb*8); long *cnt=calloc(nb,sizeof(long));
  for(int i=0;i<nb;i++){Emax[i]=-1e300;Emin[i]=1e300;E2[i]=0;Pmax[i]=0;Pend[i]=0;Pmx[i]=-1e300;Pmn[i]=1e300;}
  long double N=1.0L, psi=0.0L; uint64_t ngp=0, nmult=0, maxm=0, maxa=0; int sat=0;
  uint16_t *ebuf=malloc(sizeof(uint16_t)*(1<<20)); long eb=0;
  if(fe){ uint16_t a1=1; fwrite(&a1,2,1,fe);}  /* a_1 = 1 */
  for(uint64_t n=2;n<=X;n++){
    uint32_t A=a[n]; if(A>maxa)maxa=A;
    long double T=(long double)rho*(n-1)+1.0L+off;
    long double need=T-(N+A); long m = (need>0)? (long)floorl(need+0.5L):0;
    if(m>0){
      if(m>maxm)maxm=m; ngp++; nmult+=m;
      for(long c=0;c<m;c++) for(uint64_t k=1;k*n<=X;k++){ uint32_t v=(uint32_t)a[k*n]+a[k]; if(v>0xFFFFu){sat=1;v=0xFFFFu;} a[k*n]=(uint16_t)v; }
      if(fg){ uint32_t pr[2]={(uint32_t)n,(uint32_t)m}; fwrite(pr,4,2,fg);}
      double lw=m*log((double)n); psi+=lw;
      if((double)n*(double)n<=(double)X){ uint64_t q=n*n; for(;;){ hpush(q,lw); if((double)q*(double)n>(double)X)break; q*=n; } }
    }
    while(hn>0 && hp[0].pos==n){ PW r=hpop(); psi+=r.w; }
    N+=A+m;
    double E=(double)(N-T);
    if(fe){ ebuf[eb++]=(uint16_t)(A+m); if(eb==(1<<20)){fwrite(ebuf,2,eb,fe);eb=0;} }
    int b=(int)(BPD*log10((double)n)); if(b>=nb)b=nb-1;
    if(E>Emax[b])Emax[b]=E; if(E-rho<Emin[b])Emin[b]=E-rho; E2[b]+=E*E; cnt[b]++;
    double d1=fabs((double)(psi-(long double)n)), d2=fabs((double)(psi-(long double)(n+1)));
    double d=d1>d2?d1:d2; if(d>Pmax[b])Pmax[b]=d; double sp=(double)(psi-(long double)n); Pend[b]=sp; if(sp>Pmx[b])Pmx[b]=sp; if(sp-1<Pmn[b])Pmn[b]=sp-1;
  }
  if(fe){ if(eb)fwrite(ebuf,2,eb,fe); fclose(fe);} if(fg)fclose(fg);
  printf("# pseudoN rho=%.12g X=%.3g label=%s  g-prime sites=%llu total mult=%llu max m=%llu max a=%llu sat=%d\n",
         rho,(double)X,lab,(unsigned long long)ngp,(unsigned long long)nmult,(unsigned long long)maxm,(unsigned long long)maxa,sat);
  printf("# bin_lo  Emax  Emin  Erms  sup|psi-x|  max(psi-x)  min(psi-x)  (psi-x)@end\n");
  for(int i=0;i<nb;i++) if(cnt[i]) printf("%.4e %.6g %.6g %.6g %.6g %.6g %.6g %.6g\n",pow(10.0,(double)i/BPD),Emax[i],Emin[i],sqrt(E2[i]/cnt[i]),Pmax[i],Pmx[i],Pmn[i],Pend[i]);
  return 0;
}
