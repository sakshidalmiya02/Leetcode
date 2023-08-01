#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        ans=[]
        def dfs(q,V,adj,visited):
            visited.add(V)
            q.append(V)
            while(q):
                x=q.pop()
                ans.append(x)
                for y in adj[x]:
                    if y not in visited:
                        dfs(q,y,adj,visited)
                    
        dfs([],0,adj,set())
        return ans


#{ 
 # Driver Code Starts

if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends