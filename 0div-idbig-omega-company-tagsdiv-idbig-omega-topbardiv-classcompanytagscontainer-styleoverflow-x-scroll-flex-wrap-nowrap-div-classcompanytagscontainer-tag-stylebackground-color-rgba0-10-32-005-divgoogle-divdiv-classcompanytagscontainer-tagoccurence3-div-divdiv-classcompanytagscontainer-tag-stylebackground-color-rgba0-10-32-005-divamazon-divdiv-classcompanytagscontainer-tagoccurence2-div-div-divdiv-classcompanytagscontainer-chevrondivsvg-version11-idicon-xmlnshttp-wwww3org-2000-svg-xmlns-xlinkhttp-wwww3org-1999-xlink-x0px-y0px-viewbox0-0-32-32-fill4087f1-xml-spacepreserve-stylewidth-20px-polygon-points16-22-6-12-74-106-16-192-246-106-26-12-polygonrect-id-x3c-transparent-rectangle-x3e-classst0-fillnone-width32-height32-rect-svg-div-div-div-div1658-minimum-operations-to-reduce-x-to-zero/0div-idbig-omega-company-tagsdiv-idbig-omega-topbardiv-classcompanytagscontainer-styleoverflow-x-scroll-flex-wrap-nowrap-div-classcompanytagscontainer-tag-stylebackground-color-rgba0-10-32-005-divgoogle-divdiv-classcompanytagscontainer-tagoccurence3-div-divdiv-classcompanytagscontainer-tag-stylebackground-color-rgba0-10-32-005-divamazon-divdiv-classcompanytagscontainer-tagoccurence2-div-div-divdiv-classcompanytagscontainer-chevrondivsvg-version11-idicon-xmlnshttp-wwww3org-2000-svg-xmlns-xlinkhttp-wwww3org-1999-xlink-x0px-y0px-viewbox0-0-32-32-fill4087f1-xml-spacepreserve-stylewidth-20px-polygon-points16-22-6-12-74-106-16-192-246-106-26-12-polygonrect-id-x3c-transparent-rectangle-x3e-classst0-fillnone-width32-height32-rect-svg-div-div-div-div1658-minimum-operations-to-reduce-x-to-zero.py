class Solution:
    def minOperations(self, arr: List[int], x: int) -> int:
        n=len(arr)
        if sum(arr)<x:
            return -1
        elif sum(arr)==x:
            return n
        
        pref=[0]*len(arr)
        rev=[0]*len(arr)
        for i in range(len(arr)):
            if i==0:
                pref[0]=arr[0]
            else:
                pref[i]=pref[i-1]+arr[i]
        for i in range(len(arr)):
            if i==0:
                rev[0]=arr[-1]
            else:
                rev[i]=rev[i-1]+arr[n-1-i]
        def bs(nums,item):
            
            l,r=0,len(nums)-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==item:
                    return mid
                elif nums[mid]>item:
                    r=mid-1
                else:
                    l=mid+1
            return -1
        
        
        
        ans=99999
        for i in range(len(pref)):
            if pref[i]==x:
                ans=min(i+1,ans)
        for i in range(len(rev)):
            if rev[i]>x:
                break
            elif rev[i]==x:
                ans=min(ans,i+1)
            else:
                item=x-rev[i]
                
                indx=bs(pref,item)
            
                if indx==-1:
                    continue
                ans=min(ans,i+indx+2)
        if ans==99999:
            return -1
        return ans
            
                
            