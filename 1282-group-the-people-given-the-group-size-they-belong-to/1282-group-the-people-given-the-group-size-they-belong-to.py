class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d={}
        for i,x in enumerate(groupSizes):
            d[i]=x
        k=sorted(d.items(),key=lambda x:x[1])
        ans=[]
        lt=[]
        for i,j in k:
            if j==1:
                ans.append([i])
            else:
                if len(lt)<j:
                    lt.append(i)
                    if len(lt)==j:
                        ans.append(lt)
                        lt=[]
                
        return ans
                    
        