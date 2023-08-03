class Solution:
    def letterCombinations(self, s: str) -> List[str]:
        d={'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        if s=="":
            return []
        x=len(s)
        ans=[]
        st=""
        if x>=1:
            for i in d[s[0]]:
                st+=i
                # print(st)
                if x>=2:
                    for j in d[s[1]]:
                        st+=j
                        # print(st)
                        if x>=3:
                            for k in d[s[2]]:
                                st+=k
                                # print(st)
                                if x==4:
                                    for l in d[s[3]]:
                                        st+=l
                                        ans.append(st)
                                        st=st[:-1]  
                                if x>3:
                                    st=st[:-1]
                                if x==3:
                                    ans.append(st)
                                    st=st[:-1]
                        if x>2:
                            st=st[:-1]
                        if x==2:
                            ans.append(st)
                            st=st[:-1]
                if x>1:
                    st=st[:-1]
                if x==1:
                    ans.append(st)
                    st=st[:-1]
                
        return ans





            
        