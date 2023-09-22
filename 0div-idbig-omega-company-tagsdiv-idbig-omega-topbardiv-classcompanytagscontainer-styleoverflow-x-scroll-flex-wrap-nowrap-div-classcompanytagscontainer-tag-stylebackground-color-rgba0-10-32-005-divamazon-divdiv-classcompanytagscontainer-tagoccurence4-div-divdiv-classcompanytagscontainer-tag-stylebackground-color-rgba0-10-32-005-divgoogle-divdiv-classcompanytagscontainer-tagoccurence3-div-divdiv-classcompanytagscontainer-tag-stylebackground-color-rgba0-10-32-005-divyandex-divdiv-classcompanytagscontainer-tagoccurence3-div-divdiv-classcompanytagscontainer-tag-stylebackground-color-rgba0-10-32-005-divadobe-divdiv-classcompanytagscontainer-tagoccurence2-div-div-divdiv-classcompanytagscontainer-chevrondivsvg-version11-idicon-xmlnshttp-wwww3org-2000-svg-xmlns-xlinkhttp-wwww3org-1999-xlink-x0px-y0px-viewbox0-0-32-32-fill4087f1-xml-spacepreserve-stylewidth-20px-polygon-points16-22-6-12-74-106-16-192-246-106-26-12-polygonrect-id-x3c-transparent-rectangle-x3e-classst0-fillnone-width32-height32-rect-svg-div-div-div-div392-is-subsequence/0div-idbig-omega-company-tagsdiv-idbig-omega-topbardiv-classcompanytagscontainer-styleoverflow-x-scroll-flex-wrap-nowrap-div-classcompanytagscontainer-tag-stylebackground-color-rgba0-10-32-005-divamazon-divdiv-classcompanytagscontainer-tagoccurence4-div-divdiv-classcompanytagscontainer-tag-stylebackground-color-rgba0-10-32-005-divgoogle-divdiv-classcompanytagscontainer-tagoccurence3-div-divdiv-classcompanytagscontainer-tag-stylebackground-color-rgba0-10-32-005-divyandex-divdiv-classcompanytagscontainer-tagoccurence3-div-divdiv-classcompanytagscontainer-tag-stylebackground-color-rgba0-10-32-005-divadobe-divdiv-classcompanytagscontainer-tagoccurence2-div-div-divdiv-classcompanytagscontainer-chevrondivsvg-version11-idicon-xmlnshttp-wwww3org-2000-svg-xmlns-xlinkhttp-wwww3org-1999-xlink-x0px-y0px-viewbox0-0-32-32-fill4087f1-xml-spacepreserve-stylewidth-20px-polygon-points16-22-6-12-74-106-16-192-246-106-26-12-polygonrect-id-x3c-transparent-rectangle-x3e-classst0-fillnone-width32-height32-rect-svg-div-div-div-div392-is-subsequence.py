class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        stack=[]
        for j in t:
            if i<len(s) and j==s[i]:
                stack.append(j)
                i+=1
            
            #print(stack)
        if stack==list(s):
            return True
        else:
            return False
        
            
        