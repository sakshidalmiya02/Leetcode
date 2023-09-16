#User function Template for python3

class Solution:
    #Function to count the number of ways in which frog can reach the top.
    def countWays(self,n):
        if n==1:
            return 1
        elif n==2:
            return 2
        elif n==3:
            return 4
        first=1
        second=2
        third=4
        for i in range(4,n+1):
            temp=first+second+third
            first=second
            second=third
            third=temp
        return temp%1000000007
            
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
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))
# } Driver Code Ends