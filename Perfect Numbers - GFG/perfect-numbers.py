#User function Template for python3
import math
class Solution:
    def isPerfectNumber(self, N):
        # code here 
        l=set()
        for i in range(1,int(math.sqrt(N)+1)):
            if N%i==0:
                l.add(i)
                l.add(N//i)
        # print(l)
        if sum(l)==2*N:
            return 1
        else:
            return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.isPerfectNumber(N))
# } Driver Code Ends