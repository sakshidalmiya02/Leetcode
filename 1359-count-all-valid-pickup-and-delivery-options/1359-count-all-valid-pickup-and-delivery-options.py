class Solution:
    def countOrders(self, n: int) -> int:
        dp=[0]*(n+1)
        if n==1:
            return 1
        if n==2:
            return 6
        dp[1]=1
    
        dp[2]=6
        
        for i in range(3,n+1):
            
            dp[i]=(i)*dp[i-1]*(2*(i-1)+1)
        return dp[-1]%(10**9 + 7)
        