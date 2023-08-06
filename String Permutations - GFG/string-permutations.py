#User function Template for python3

class Solution:
    def permutation(self,s):
        ans=[]
        visited=[0]*len(s)
        def f(indx,s,n,lt):
            if len(lt)==n:
                ans.append("".join(lt))
            for i in range(len(s)):
                if visited[i]==0:
                    visited[i]=1
                    f(indx+1,s,n,lt+[s[i]])
                    
                    f(indx+1,s,n,lt)
                    visited[i]=0
        f(0,s,len(s),[])
        return sorted(ans)
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    while(T>0):
        s=input()
        ob=Solution()
        ans=ob.permutation(s)
        for i in ans:
            print(i,end=" ")
        print()
        
        T-=1
# } Driver Code Ends