#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):

        # code here
        A.sort()
        m=999999
    
        for i in range(len(A)-M+1):
            diff=(A[M+i-1]-A[i])
            # print(diff)
            if diff<m:
                m=A[M+i-1]-A[i]
                
        return m
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends