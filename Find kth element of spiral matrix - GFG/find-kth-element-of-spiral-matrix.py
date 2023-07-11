#User function Template for python3

class Solution:
    def findK(self, a, n, m, k):
        # Write Your Code here
        turns=0
        count=0
        i,j=0,-1
        while(count<=len(a)*len(a[0])):
        
            for j in range(j+1,len(a[0])-turns):
                # print(a[i][j])
                count+=1
                if count==k:
                    return a[i][j]
            if count>len(a)*len(a[0]):
                break
            for i in range(i+1,len(a)-turns):
                # print(a[i][j])
                count+=1
                if count==k:
                    return a[i][j]
            if count>len(a)*len(a[0]):
                break
            for j in range(j-1,turns-1,-1):
                # print(a[i][j])
                count+=1
                if count==k:
                    return a[i][j]
            if count>len(a)*len(a[0]):
                break
            for i in range(i-1,turns,-1):
                # print(a[i][j])
                count+=1
                if count==k:
                    return a[i][j]
            if count>len(a)*len(a[0]):
                break
            turns+=1
                
        
            
    
        


#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n, m, k = map(int,input().split())
    a = [
            list(map(int,input().split()))
            for _ in range(n)
        ]
    
    ob = Solution()
    print(ob.findK(a,n,m,k))
    
# } Driver Code Ends