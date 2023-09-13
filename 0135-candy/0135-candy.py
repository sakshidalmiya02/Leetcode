class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        if n==1:
            return 1
        ans=[1]*len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1] and ans[i]<=ans[i-1]:
                ans[i]=ans[i-1]+1
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1] and ans[i]<=ans[i+1]:
                ans[i]=ans[i+1]+1
        return sum(ans)