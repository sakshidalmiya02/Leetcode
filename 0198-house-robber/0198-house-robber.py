class Solution:
    def rob(self, nums: List[int]) -> int:
        yes,no=0,0
        for i in range(len(nums)):
            temp=max(yes,no)
            yes=no+nums[i]
            no=temp
        return max(yes,no)