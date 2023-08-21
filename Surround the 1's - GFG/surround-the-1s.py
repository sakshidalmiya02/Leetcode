#User function Template for python3

class Solution:
	def Count(self, matrix):
		# Code here
		n=len(matrix)
		m=len(matrix[0])
		z=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
		ans=0
		for i in range(n):
		    for j in range(m):
		        if matrix[i][j]==1:
		            flag=0
		            for x,y in z:
		                X=x+i
		                Y=y+j
		                if 0<=X<n and 0<=Y<m and matrix[X][Y]==0:
		                    flag+=1
		            if flag%2==0 and flag!=0:
		                
		                ans+=1
		return ans
		                    
		                    
		                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int,input().split())))
		ob = Solution()
		ans = ob.Count(matrix)
		print(ans)

# } Driver Code Ends