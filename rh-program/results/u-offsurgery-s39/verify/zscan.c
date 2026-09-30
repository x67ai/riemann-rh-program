/* zscan.c -- evaluate zeta_P(s) = rho*zeta(s) + sum_{n<=X} (a_n - rho) n^{-s} for an N-supported system
   (a_n = multiplicity of the g-integer n, uint16 dump, a[i] = a_{i+1}); also prints the tail bound
   B(s) = (|C(X)| + |s| Cmax / sigma) X^{-sigma}, C(u) = N(u) - rho*floor(u), Cmax supplied by the user (sup of |C| beyond X).
   Modes: v sigma t0 t1 dt   (vertical line, recurrence in t)   |   h t sig0 sig1 dsig (horizontal segment)
   Usage: zscan a.u16 X rho Cmax mode ...        Build: cc -O2 -o zscan zscan.c -lm */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <complex.h>
#include <math.h>
static double B2k[11]={0,1.0/6,-1.0/30,1.0/42,-1.0/30,5.0/66,-691.0/2730,7.0/6,-3617.0/510,43867.0/798,-174611.0/330};
static double complex zeta_em(double complex s){ int M=60; double complex z=0; for(int n=1;n<M;n++) z+=cpow((double)n,-s);
  z+=cpow((double)M,1-s)/(s-1)+0.5*cpow((double)M,-s); double complex fac=s*cpow((double)M,-s-1); double f2=1;
  for(int k=1;k<=10;k++){ f2*= (2.0*k-1)*(2.0*k); z+=B2k[k]/f2*fac; fac*= (s+2*k-1)*(s+2*k)/((double)M*M); } return z; }
int main(int argc,char**argv){
  if(argc<7){fprintf(stderr,"usage\n");return 1;}
  uint64_t X=(uint64_t)atof(argv[2]); double rho=atof(argv[3]), Cmax=atof(argv[4]); char mode=argv[5][0];
  FILE*f=fopen(argv[1],"rb"); uint16_t*a=malloc(X*2); if(fread(a,2,X,f)!=X){fprintf(stderr,"short\n");return 1;} fclose(f);
  double NX=0; for(uint64_t i=0;i<X;i++) NX+=a[i]; double CX=NX-rho*(double)X;
  int J; double complex *S, *pts;
  if(mode=='v'){ double sg=atof(argv[6]),t0=atof(argv[7]),t1=atof(argv[8]),dt=atof(argv[9]); J=(int)floor((t1-t0)/dt+0.5)+1;
    S=calloc(J,sizeof *S); pts=malloc(J*sizeof *pts); for(int j=0;j<J;j++) pts[j]=sg+I*(t0+j*dt);
    for(uint64_t n=1;n<=X;n++){ double c=(double)a[n-1]-rho; double L=log((double)n);
      double complex z=exp(-sg*L)*cexp(-I*t0*L), w=cexp(-I*dt*L);
      for(int j=0;j<J;j++){ S[j]+=c*z; z*=w; } }
  } else { double t=atof(argv[6]),s0=atof(argv[7]),s1=atof(argv[8]),ds=atof(argv[9]); J=(int)floor((s1-s0)/ds+0.5)+1;
    S=calloc(J,sizeof *S); pts=malloc(J*sizeof *pts); for(int j=0;j<J;j++) pts[j]=(s0+j*ds)+I*t;
    for(uint64_t n=1;n<=X;n++){ double c=(double)a[n-1]-rho; double L=log((double)n); double complex ph=cexp(-I*t*L);
      double e0=exp(-s0*L), r=exp(-ds*L); double complex z=e0*ph; for(int j=0;j<J;j++){ S[j]+=c*z; z*=r; } } }
  printf("# X=%.3g rho=%.12g C(X)=%.4g Cmax=%.4g mode=%c\n# sigma t Re Im |F| tailbound\n",(double)X,rho,CX,Cmax,mode);
  for(int j=0;j<J;j++){ double complex s=pts[j], F=rho*zeta_em(s)+S[j]; double sg=creal(s);
    double B=(fabs(CX)+cabs(s)*Cmax/sg)*exp(-sg*log((double)X));
    printf("%.6f %.6f %.10e %.10e %.6e %.3e\n",creal(s),cimag(s),creal(F),cimag(F),cabs(F),B); }
  return 0; }
