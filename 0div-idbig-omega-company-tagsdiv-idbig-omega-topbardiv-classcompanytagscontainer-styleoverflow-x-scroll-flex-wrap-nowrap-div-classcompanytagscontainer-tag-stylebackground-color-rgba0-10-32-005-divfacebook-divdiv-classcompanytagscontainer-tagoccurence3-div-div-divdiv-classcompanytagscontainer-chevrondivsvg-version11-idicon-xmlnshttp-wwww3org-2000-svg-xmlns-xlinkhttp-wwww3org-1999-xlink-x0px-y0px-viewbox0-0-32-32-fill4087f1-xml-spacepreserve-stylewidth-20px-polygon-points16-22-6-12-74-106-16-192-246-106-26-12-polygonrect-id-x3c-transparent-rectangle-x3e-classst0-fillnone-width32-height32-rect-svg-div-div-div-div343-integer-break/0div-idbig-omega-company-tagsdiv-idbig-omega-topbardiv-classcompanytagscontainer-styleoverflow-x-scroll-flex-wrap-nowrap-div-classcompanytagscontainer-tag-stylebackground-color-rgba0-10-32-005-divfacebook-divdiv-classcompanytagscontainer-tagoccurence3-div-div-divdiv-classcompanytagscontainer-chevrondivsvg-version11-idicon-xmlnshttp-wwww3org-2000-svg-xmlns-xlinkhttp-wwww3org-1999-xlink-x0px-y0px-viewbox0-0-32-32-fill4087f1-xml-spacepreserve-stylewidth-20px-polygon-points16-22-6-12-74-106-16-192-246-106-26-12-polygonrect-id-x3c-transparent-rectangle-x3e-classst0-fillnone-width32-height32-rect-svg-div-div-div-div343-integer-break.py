class Solution:
    def integerBreak(self, n: int) -> int:
        if n==1 or n==2:
            return 1
        if n==3:
            return 2
        dp=[0]*(n+1)
        dp[1]=1
        dp[2]=2
        dp[3]=3
        dp[4]=4
        for i in range(5,n+1):
            for j in range(1,i//2 +1):
                dp[i]=max(dp[i],dp[j]*dp[i-j])
                # print(dp)
        return dp[-1]
                
            
# 1->1
# 2->1
# 3->2
# 4->4
# 5->6
# 6->9
# 7->12
# 8->18
# 9->27
