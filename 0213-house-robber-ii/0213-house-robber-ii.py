class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1 or len(nums)==2:
            return max(nums)
        yes,no=0,0 
        for i in range(1,len(nums)):
            temp=max(yes,no)
            yes=no+nums[i]
            no=temp
        ans1=max(yes,no)
        
        yes,no=0,0
        for i in range(len(nums)-2,-1,-1):
            temp=max(yes,no)
            yes=no+nums[i]
            no=temp
        ans2=max(yes,no)
        return max(ans1,ans2)
        