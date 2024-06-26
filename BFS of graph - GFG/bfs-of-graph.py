#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        
        visited=[]
        
        def bfs(source):
            visited.append(source)
            q=[]
            q.append(source)
            while(q!=[]):
                x=q.pop(0)
                for y in adj[x]:
                    if y not in visited:
                        visited.append(y)
                        q.append(y)
                        
        bfs(0)
        return visited


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends