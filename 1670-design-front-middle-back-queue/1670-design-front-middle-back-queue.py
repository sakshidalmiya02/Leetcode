class FrontMiddleBackQueue:

    def __init__(self):
        self.q=[]
        

    def pushFront(self, val: int) -> None:
        self.q=[val]+self.q
        

    def pushMiddle(self, val: int) -> None:
        x=len(self.q)//2
        self.q.insert(x,val)
        
        

    def pushBack(self, val: int) -> None:
        self.q=self.q+[val]

    def popFront(self) -> int:
        if self.q==[]:
            return -1
        else:
            x=self.q[0]
            self.q=self.q[1:]
            return x
        

    def popMiddle(self) -> int:
        x=(len(self.q)-1)//2
        if self.q==[]:
            return -1
        return self.q.pop(x)
        
        
        

    def popBack(self) -> int:
        if self.q==[]:
            return -1
        x=self.q.pop()
        return x
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()