#User function Template for python3

class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        prev_yes=0
        prev_no=0
        curr_yes=0
        curr_no=0
        for i in a:
            curr_yes=prev_no+i
            curr_no=max(prev_yes,prev_no)
            prev_yes=curr_yes
            prev_no=curr_no
        return max(curr_yes,curr_no)
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.FindMaxSum(a,n))
# } Driver Code Ends