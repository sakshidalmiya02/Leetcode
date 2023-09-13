#User function Template for python3

class Solution:
    def findLargest(self, N, S):
        # code here
        
        if S==0 and N==1:
            return 0
        if S==0 or S>N*9:
            return -1
        ans=['0']*N
        for i in range(N):
            if S>=9:
                ans[i]=str(9)
                S-=9
            else:
                ans[i]=str(S)
                S=0
        
        return int("".join(ans))
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, S = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.findLargest(N, S))
# } Driver Code Ends