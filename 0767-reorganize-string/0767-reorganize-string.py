class Solution:
    def reorganizeString(self, s: str) -> str:
        d={}
        ans=[None]*len(s)
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        x=max(d.values())
        
        if x>math.ceil(len(s)/2):
            return ""
        else:
            d=sorted(d.items(),key=lambda x:x[1],reverse=True)
            k=1
            for i in range(len(d)):
                key=d[i][0]
                value=d[i][1]
                if ans[0]==None:
                    ans[0]=key
                    value-=1
                # print(ans,key,value)
                while value!=0:
                    if ans[k]==None and ans[k-1]!=key:
                        ans[k]=key
                        value-=1
                        if k+2<len(s):
                            k=k+2
                        else:
                            k=0
                    else:
                        k+=1
                        if k==len(s):
                            k=0

                    # print(ans)
            return "".join(ans)
                            
            
            
                
                
                
            
        