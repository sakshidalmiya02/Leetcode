class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def f(indx,n,lt,k):
            # print(indx,n,lt,k)
            if len(lt)==k:
                ans.append(lt)
                return
            if indx>n:
                return
            
            f(indx+1,n,lt+[indx],k)
            f(indx+1,n,lt,k)
        f(1,n,[],k)
        return ans
                
            
        