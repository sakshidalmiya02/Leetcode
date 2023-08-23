#User function Template for python3

class Solution:
	def searchWord(self, grid, word):
		# Code here
		ans=[]
		def check(i,j,x,y,ln):
		  #  print('hi')
		    X=i
		    Y=j
		    for k in range(1,ln):
		        i=i+x
		        j=j+y
		      #  print(i,j)
		        if 0<=i<n and 0<=j<m:
		            if grid[i][j]==word[k]:
		                continue
		            else:
		                return False
		        else:
		            return False
		    ans.append([X,Y])
		  #  print(ans)
		    return True
		    
		    
		z=[[0,1],[1,0],[1,1],[1,-1],[0,-1],[-1,1],[-1,0],[-1,-1]]
		ln=len(word)
		for i in range(n):
		    for j in range(m):
		        if grid[i][j]==word[0]:
		            for x,y in z:
		                if check(i,j,x,y,ln):
		                    break
		return ans
		           

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		grid = []
		for _ in range(n):
			cur  = input()
			temp = []
			for __ in cur:
				temp.append(__)
			grid.append(temp)
		word = input()
		obj = Solution()
		ans = obj.searchWord(grid, word)
		for _ in ans:
			for __ in _:
				print(__, end = " ")
			print()
		if len(ans)==0:
		    print(-1)

# } Driver Code Ends