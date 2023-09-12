class Solution:
    def minDeletions(self, s: str) -> int:
        vis=[0]*(len(s)+1)
        d=Counter(s)
        count=0
        print(d)
        if len(d.keys())==len(set(d.values())):
                return count
        for i,j in d.items():
            if vis[j]==0:
                vis[j]=1
            else:
                k=j
                while(vis[k]!=0):
                    k-=1
                if k!=0:
                    count+=j-k
                    vis[k]=1
                    d[i]=k
                else:
                    count+=j
                    d[i]=0
            # print(d,vis,i,j,count)
                        
        return count
                        
                
                
        
            
        
        