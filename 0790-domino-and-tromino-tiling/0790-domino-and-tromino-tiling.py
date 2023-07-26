class Solution:
    def numTilings(self, n: int) -> int:
        if n==1:
            return 1
        
        f1=[0]*(n+1)
        f2=[0]*(n+1)
        f1[1]=1
        f1[2]=2
        f2[2]=1
        
        
        for k in range(3,n+1):
            f1[k]=f1[k-1]+f1[k-2]+2*f2[k-1]
            f2[k]=f2[k-1]+f1[k-2]
        return f1[n]%(10**9+7)
            
        