class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        l=[]
        arr.sort()
        for i in range(1,len(arr)):
            l.append(arr[i]-arr[i-1])
        if l==[l[0]]*len(l):
            
            return True
        return False