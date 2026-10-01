/* zmom.c -- Taylor moments of S_X(s) = sum_{n<=X} a_n n^-s at a center s0 (read-O, Session 40).
   M_k(X) = sum_{n<=X} a_n n^-s0 (-log n)^k / k!,  k = 0..KM, written at checkpoints X_c.  Then
   F_X(s) := 0.8 zeta(s) + sum_{n<=X}(a_n - 0.8) n^-s = S_X(s) + 0.8 zeta(s, X+1)  (Hurwitz), S_X(s0+h) = sum_k M_k h^k.
   Different method from the unit's (vertical/horizontal recurrences): per-term exp/log/sincos, block-compensated sums.
   Mode D (direct): also evaluates S_X at a few given points by direct summation, to validate the Taylor route.
   usage: zmom file.a16 sigma0 t0 Xc1,Xc2,... [s1re s1im s2re s2im ...] */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <unistd.h>
#define KM 28
#define MAXP 8
int main(int argc,char**argv){
  int fd=open(argv[1],O_RDONLY); off_t sz=lseek(fd,0,SEEK_END); const uint16_t *a=mmap(0,sz,PROT_READ,MAP_SHARED,fd,0);
  uint64_t Xmax=sz/2-1; double s0=atof(argv[2]), t0=atof(argv[3]);
  uint64_t Xc[32]; int nc=0; { char *s=strdup(argv[4]); for(char*t=strtok(s,",");t;t=strtok(0,",")) Xc[nc++]=(uint64_t)atof(t); }
  int np=(argc-5)/2; double pre[MAXP],pim[MAXP]; for(int i=0;i<np;i++){pre[i]=atof(argv[5+2*i]); pim[i]=atof(argv[6+2*i]);}
  double Tr[KM+1]={0},Ti[KM+1]={0},Cr[KM+1]={0},Ci[KM+1]={0}; /* totals with Kahan compensation */
  double Br[KM+1],Bi[KM+1]; double Dr[MAXP]={0},Di[MAXP]={0},DBr[MAXP],DBi[MAXP];
  int ic=0; uint64_t n=1;
  printf("# zmom s0 = %.10f + %.10fi, KM = %d\n",s0,t0,KM);
  while(ic<nc){
    uint64_t end=n+65536; if(end>Xc[ic]+1) end=Xc[ic]+1; if(end>Xmax+1) end=Xmax+1;
    memset(Br,0,sizeof Br); memset(Bi,0,sizeof Bi); memset(DBr,0,sizeof DBr); memset(DBi,0,sizeof DBi);
    for(;n<end;n++){ unsigned an=a[n]; if(!an) continue; double L=log((double)n);
      double w=an*exp(-s0*L), ph=-t0*L; double zr=w*cos(ph), zi=w*sin(ph); double c=1.0;
      for(int k=0;k<=KM;k++){ Br[k]+=zr*c; Bi[k]+=zi*c; c*=-L/(k+1); }
      for(int i=0;i<np;i++){ double ww=an*exp(-pre[i]*L), pp=-pim[i]*L; DBr[i]+=ww*cos(pp); DBi[i]+=ww*sin(pp); }
    }
    for(int k=0;k<=KM;k++){ double y=Br[k]-Cr[k], t=Tr[k]+y; Cr[k]=(t-Tr[k])-y; Tr[k]=t; y=Bi[k]-Ci[k]; t=Ti[k]+y; Ci[k]=(t-Ti[k])-y; Ti[k]=t; }
    for(int i=0;i<np;i++){ Dr[i]+=DBr[i]; Di[i]+=DBi[i]; }
    if(n==Xc[ic]+1){ printf("X %llu\n",(unsigned long long)Xc[ic]);
      for(int k=0;k<=KM;k++) printf("M %d %.17g %.17g\n",k,Tr[k],Ti[k]);
      for(int i=0;i<np;i++) printf("D %.10f %.10f %.17g %.17g\n",pre[i],pim[i],Dr[i],Di[i]);
      fflush(stdout); ic++; }
  }
  return 0;
}
