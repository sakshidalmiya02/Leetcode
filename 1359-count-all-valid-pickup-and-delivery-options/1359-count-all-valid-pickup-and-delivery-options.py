class Solution:
    def countOrders(self, n: int) -> int:
        
        if n==1:
            return 1
        if n==2:
            return 6
        prev=6
        for i in range(3,n+1):
            ans=i*prev*(2*(i-1)+1)
            prev=ans
        return ans%(10**9 + 7)
        