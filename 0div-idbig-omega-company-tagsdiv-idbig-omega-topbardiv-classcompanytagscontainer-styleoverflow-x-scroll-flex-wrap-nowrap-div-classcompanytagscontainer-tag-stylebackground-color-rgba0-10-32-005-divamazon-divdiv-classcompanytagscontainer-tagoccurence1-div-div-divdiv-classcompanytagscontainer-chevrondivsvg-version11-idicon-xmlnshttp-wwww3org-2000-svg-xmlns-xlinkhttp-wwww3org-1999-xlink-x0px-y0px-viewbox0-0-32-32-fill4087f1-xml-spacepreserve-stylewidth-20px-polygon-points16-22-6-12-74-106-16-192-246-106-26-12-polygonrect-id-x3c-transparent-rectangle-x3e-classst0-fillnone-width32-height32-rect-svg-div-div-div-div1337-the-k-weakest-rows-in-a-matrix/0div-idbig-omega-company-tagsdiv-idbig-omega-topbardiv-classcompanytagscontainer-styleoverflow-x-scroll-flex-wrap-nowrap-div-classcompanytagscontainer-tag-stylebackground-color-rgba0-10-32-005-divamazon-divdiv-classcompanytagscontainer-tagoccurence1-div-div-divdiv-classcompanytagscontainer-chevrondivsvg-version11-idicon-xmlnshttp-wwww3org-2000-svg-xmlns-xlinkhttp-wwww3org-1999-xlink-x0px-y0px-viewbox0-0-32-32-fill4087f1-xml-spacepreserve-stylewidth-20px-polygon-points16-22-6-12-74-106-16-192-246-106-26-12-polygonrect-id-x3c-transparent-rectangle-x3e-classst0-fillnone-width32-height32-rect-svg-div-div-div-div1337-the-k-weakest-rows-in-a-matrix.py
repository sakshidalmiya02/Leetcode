class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        d={}
        for i in range(len(mat)):
            c=0
            for j in mat[i]:
                if j==1:
                    c+=1
            d[i]=c  
        print(d)    
        d=sorted(d.items(),key=lambda x:x[1])
        l=[]
        c=0
        for i,j in d:
            if c<k:
                c+=1
                l.append(i)
        return l    