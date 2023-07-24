class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def f(st,opn,close,n):
            if opn==n and close==n:
                ans.append(st)
            elif opn==n and close<n:
                f(st+')',opn,close+1,n)
            elif opn==close or st=='':
                f(st+'(',opn+1,close,n)
            else:
                f(st+'(',opn+1,close,n)
                f(st+')',opn,close+1,n)
                
        f('',0,0,n)
        return ans
        