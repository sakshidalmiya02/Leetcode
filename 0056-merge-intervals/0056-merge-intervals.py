class Solution:
    def merge(self, interval: List[List[int]]) -> List[List[int]]:
        interval.sort()
        stack=[]
        for i,j in interval:
            x=[9999999,-1]
            while(stack!=[] and i<=stack[-1][1]):
                x=stack.pop()
            stack.append([min(x[0],i),max(x[1],j)])
        return stack
        
        