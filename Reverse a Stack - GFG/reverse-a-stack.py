#User function Template for python3

from typing import List

class Solution:
    def reverse(self,St): 
        #code here
        ans=[]
        while(St):
            ans.append(St.pop())
        
        for i in ans:
            St.append(i)
            
        
                

#{ 
 # Driver Code Starts

#Initial Template for Python 3

 
for _ in range(int(input())):
    N = int(input())
    St = list(map(int, input().split()))
    ob = Solution()
    ob.reverse(St)
    print(*St)
# } Driver Code Ends