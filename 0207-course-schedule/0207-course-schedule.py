class Solution(object):
    def canFinish(self, numCourses, p):
        adj=[[] for i in range(numCourses)]
        ind=[0]*numCourses
        for i,j in p:
            adj[j].append(i)
            ind[i]+=1
          
        visited=[0]*numCourses    
        def bfs(s):
            visited[s]=1
            q=[]
            q.append(s)
            while(q!=[]):
                x=q.pop(0)
                l=adj[x]
                for y in l:
                    ind[y]-=1
                    if ind[y]==0 and visited[y]==0:
                        visited[y]=1
                        q.append(y)
                      
                        
                        
        for i in range(len(ind)):
            if ind[i]==0 and visited[i]==0:
                bfs(i)
        if visited==[1]*numCourses:
            return True
        return False