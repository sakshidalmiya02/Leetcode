class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        if arr[-1]>arr[-2]:
            return len(arr)-1
        start=1
        last=len(arr)-2
        while(start<=last):
            mid=start+(last-start)//2
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid]>arr[mid-1]:
                start=mid+1
            else:
                last=mid-1
        
                
        