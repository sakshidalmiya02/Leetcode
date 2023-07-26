class Solution {
public:
    int numTilings(int n) {
        int M=1e9+7;
        if (n==1) return 1;
        vector<int>f1(n+1),f2(n+1);
        f1[1]=1,f1[2]=2,f2[2]=1;
        for (int k=3;k<=n;k++){
            f1[k]=((f1[k-1]+f1[k-2])%M + (2*f2[k-1])%M)%M;
            f2[k]=(f2[k-1]+f1[k-2])%M;
        }
        return f1[n];
            
        
    }
};