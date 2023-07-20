class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in asteroids:
            if stack==[]:
                stack.append(i)
            else:
                y=i
                while(1):
                    if stack==[]:
                        stack.append(y)
                        break
                        
                    if (y>0 and stack[-1]>0 )or (y<0 and stack[-1]<0) or stack[-1]<0 and y>0:
                        stack.append(y)
                        break
                    else:
                        x=stack.pop()
                        if abs(x)==abs(y):
                            break
                        elif abs(x)>abs(y):
                            y=x
        return stack