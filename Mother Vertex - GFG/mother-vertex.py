
class Solution:
    
    #Function to find a Mother Vertex in the Graph.
	def findMotherVertex(self, V, adj):
		#Code here

		def dfs(i,vis,adj):
		  
		    vis[i]=True
		    for y in adj[i]:
		        if vis[y]==False:
		            dfs(y,vis,adj)
		 
		vis=[False]*V
		for i in range(V):
		    if vis[i]==False:
		        dfs(i,vis,adj)
		        mother=i
		      
		vis=[False]*V
		dfs(mother,vis,adj)
		for i in vis:
		    if i==False:
		        return -1
		return mother
		 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys 

sys.setrecursionlimit(10**6) 
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		obj = Solution()
		ans = obj.findMotherVertex(V, adj)
		print(ans)
# } Driver Code Ends