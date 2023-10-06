from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1=0
        m=-1
        n=-1
        c2=0
        i=0
        l=[]
        while i<len(nums):
            if nums[i]==m:
                c1+=1
            elif nums[i]==n:
                c2+=1
            elif c1==0:
                m=nums[i]
                c1=1
            elif c2==0 :
                n=nums[i]
                c2=1
            else:
                c1-=1
                c2-=1
            i+=1 
        count=0
        count2=0
        for i in nums:
            if i==m:
                count+=1
            elif i==n:
                count2+=1
        if count>len(nums)/3:
            l.append(m)
        if count2>len(nums)/3 :
            l.append(n)
        return l    
            
      