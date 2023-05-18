class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        adj=[[] for i in range(n)]
        for i,j in edges:
            adj[j].append(i)
        ans=[]
        for i in range(len(adj)):
            if adj[i]==[]:
                ans.append(i)
        return ans
            
            
        