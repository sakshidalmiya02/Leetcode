class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited=[0]*len(nums)
        ans=[]
        n=len(nums)
        def f(indx,nums,l,n):
            # print(nums,l,n,visited)
            if len(l)==n:
                ans.append(l)
                return
            for i in range(len(nums)):
                if visited[i]==0:
                    visited[i]=1
                    # print('hi',visited)
                    f(indx,nums,l+[nums[i]],n)
                    f(indx,nums,l,n)
                    visited[i]=0
        f(0,nums,[],n)
        return ans
                
        
            