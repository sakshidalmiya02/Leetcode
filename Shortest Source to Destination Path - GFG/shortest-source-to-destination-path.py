#User function Template for python3

class Solution:
    def shortestDistance(self,N,M,A,X,Y):
        #code here
        
        visited=set()
        visited.add((0,0))
        if A[0][0]==0 or A[X][Y]==0:
            return -1
        if A[0][0]==1 and X==0 and Y==0:
            return 0
        def traverse(A,X,Y):
            dist=[[0 for i in range(M)] for j in range(N)]
            q=[]
            q.append([0,0])
            z=[(0,1),(0,-1),(1,0),(-1,0)]
            while(q):
                i,j=q.pop(0)
                
                for x,y in z:
                    if 0<=(i+x)<N and 0<=(y+j)<M and (i+x,y+j) not in visited and A[i+x][j+y]==1:
                        dist[i+x][y+j]=dist[i][j]+1
                        visited.add((i+x,y+j))
                        q.append([i+x,y+j])
            return dist
                        
                        
                        
        dist=traverse(A,X,Y)
        if dist[X][Y]==0:
            return -1
        return dist[X][Y]
                
                
        
        
        
        

#{ 
 # Driver Code Starts

#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split())
        a=[]
        for i in range(N):
            s=list(map(int,input().strip().split()))
            a.append(s)
        x,y=map(int,input().strip().split())    
        ob=Solution()
        print(ob.shortestDistance(N,M,a,x,y))
        
# } Driver Code Ends