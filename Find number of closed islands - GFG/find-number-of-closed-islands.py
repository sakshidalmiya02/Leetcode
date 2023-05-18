#User function Template for python3

class Solution:
	def closedIslands(self, matrix, N, M):
		#Code here
		def dfs(i,j):
		    
		    if i<0 or i>=len(matrix) or j<0 or j>=len(matrix[0]):
		        return False
		    
		    if matrix[i][j]==0:
		        return True
		    
		    matrix[i][j]=0
		    left=dfs(i,j-1)
		    right=dfs(i,j+1)
		    up=dfs(i-1,j)
		    down=dfs(i+1,j)
		    return left and right and up and down
		    
	    count=0
	    for i in range(len(matrix)):
	        for j in range(len(matrix[0])):
	            if matrix[i][j]==1:
	                ans=dfs(i,j)
	                if ans==True:
	                    count+=1
	    return count
	                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N, M = map(int,input().split())
        matrix = []
        for i in range(N):
            nums = list(map(int,input().split()))
            matrix.append(nums)
        obj = Solution()
        print(obj.closedIslands(matrix, N, M))
# } Driver Code Ends