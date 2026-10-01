/* zpoint.c -- D(s) = sum_{n<=X}(a_n - rho) n^{-s} and D'(s) at the points given on argv (pairs sigma t);
   one pass over n for all points. Output: sigma t ReD ImD ReD' ImD'.  Build: cc -O2 -o zpoint zpoint.c -lm
   Usage: zpoint a.u16 X rho sigma1 t1 [sigma2 t2 ...] */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <complex.h>
#include <math.h>
int main(int argc,char**argv){
  uint64_t X=(uint64_t)atof(argv[2]); double rho=atof(argv[3]); int P=(argc-4)/2;
  FILE*f=fopen(argv[1],"rb"); uint16_t*a=malloc(X*2); if(fread(a,2,X,f)!=X){fprintf(stderr,"short\n");return 1;} fclose(f);
  double complex *s=malloc(P*sizeof *s),*D=calloc(P,sizeof *D),*Dp=calloc(P,sizeof *Dp);
  for(int j=0;j<P;j++) s[j]=atof(argv[4+2*j])+I*atof(argv[5+2*j]);
  for(uint64_t n=1;n<=X;n++){ double c=(double)a[n-1]-rho; if(c==0)continue; double L=log((double)n);
    for(int j=0;j<P;j++){ double complex z=c*cexp(-s[j]*L); D[j]+=z; Dp[j]-=L*z; } }
  for(int j=0;j<P;j++) printf("%.10f %.10f %.15e %.15e %.15e %.15e\n",creal(s[j]),cimag(s[j]),creal(D[j]),cimag(D[j]),creal(Dp[j]),cimag(Dp[j]));
  return 0; }
