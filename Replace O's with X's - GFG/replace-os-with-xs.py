#User function Template for python3

class Solution:
    def fill(self, n, m, mat):
        # code here
        def dfs(i,j,vis,l):
            
            if i<0 or j<0 or i>=n or j>=m:
                return False
            if mat [i][j]=='X':
                return True
            mat[i][j]='X'
            vis.add((i,j))
            l.append((i,j))
            left=dfs(i,j-1,vis,l)
            right=dfs(i,j+1,vis,l)
            top=dfs(i-1,j,vis,l)
            bottom=dfs(i+1,j,vis,l)
            return left and right and top and bottom
        
        s=set()    
        
        for i in range(n):
            for j in range(m):
                if mat[i][j]=='O' and (i,j)not in s:
                    lt=[]
                    if not dfs(i,j,s,lt):
                        # print(mat)
                        for item in lt:
                            mat[item[0]][item[1]]='O'
                    
        return mat
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = []
        for i in range(n):
            s = list(map(str,input().split()))
            mat.append(s)
        
        ob = Solution()
        ans = ob.fill(n, m, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends