class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        yes=[0]*(n+1)
        no=[0]*(n+1)
        for i in range(len(nums)):
            yes[i+1]=nums[i]+no[i]
            no[i+1]=max(no[i],yes[i])
        return max(yes[-1],no[-1])