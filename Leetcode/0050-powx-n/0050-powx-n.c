double myPow(double x, int n) {
    double c=1.0;
    int N=n/2;
    int N1=N/2;
    int N2=N1/2;
    int z=1;

    if(n<0){
        x=1/x;
        N2=-N2;
    }

    if (N2>0){
        for(int i=1; i<=31; i++){
            z*=2;
            if(N2<=z){
                for(int j=1; j<=N2; j++){
                    c*=x;
                }
                break;
            }
            if(N2>z){
                for(int j=1; j<=z; j++){
                    c*=x;
                }
                N2=N2-z;
            }
            
        }

    }
    if(n%2!=0){
        if(N%2!=0){
            if(N1%2!=0){
                c=(((((((c*c*c*c*c*c*c*c)*x)*x)*x)*x)*x)*x)*x;
            }
            else{
                c=(((c*c*c*c*c*c*c*c)*x)*x)*x;
            }
            
        }
        else{
            if(N1%2!=0){
                c=(((((c*c*c*c*c*c*c*c)*x)*x)*x)*x)*x;
            }
            else{
                c=(c*c*c*c*c*c*c*c)*x;
            }
            
        }
        
    }
    else{
        if(N%2!=0){
            if(N1%2!=0){
                c=((((((c*c*c*c*c*c*c*c)*x)*x)*x)*x)*x)*x;
            }
            else{
                c=((c*c*c*c*c*c*c*c)*x)*x;
            }
            
        }
        else{
            if(N1%2!=0){
                c=((((c*c*c*c*c*c*c*c)*x)*x)*x)*x;
            }
            else{
                c=c*c*c*c*c*c*c*c;
            }
            
        }
        
    }
    return c;
}