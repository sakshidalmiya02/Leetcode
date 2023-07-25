import math
class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[0,1,1,2]
        for i in range(4,n+1):
            x=int(math.log(i,2))
            l.append(l[i-(2**x)]+1)
        return l[:n+1]
            
            
            