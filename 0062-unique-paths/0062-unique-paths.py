class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        mem = [[0 for i in range(n)] for j in range(m)]
        #print(mem)
        mem[0][0] = 1
        for i in range(m):
            for j in range(n):
                if j < n - 1:
                    mem[i][j+1] += mem[i][j]
                if i < m - 1:
                    mem[i+1][j] += mem[i][j]
                #print(mem)    
        return mem[m-1][n-1]
        