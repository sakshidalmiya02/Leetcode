class Solution:
    def search(self, a: List[int], target: int) -> int:
        def findmin(a):
            if len(a)==1 or a[0]<a[len(a)-1]:
                return 0
            l,r=0,len(a)-1
            while(l<=r):
                mid=(l+r)//2
                if a[mid]>a[mid+1]:
                    return mid+1
                if a[mid]<a[mid-1]:
                    return mid
                if a[mid]>a[l]:
                    l=mid+1
                else:
                    r=mid-1
             
           
        def binarysearch(a,l,r,target):
            while(l<=r):
                mid=(l+r)//2
                if a[mid]==target:
                    return mid
                elif target<a[mid]:
                    r=mid-1
                else:
                    l=mid+1
            return -1 
        
        i=findmin(a)
        print(i)
        x=binarysearch(a,0,i-1,target)
        y=binarysearch(a,i,len(a)-1,target)
        if x==-1:
            return y
        else:
            return x
        