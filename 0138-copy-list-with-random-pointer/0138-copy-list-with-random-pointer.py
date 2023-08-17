"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp=head
        dummy=Node(-1)
        new=dummy
        d={}
        pos=1
        while(temp):
            dummy.next=Node(temp.val)
            d[temp]=dummy.next
            temp=temp.next
            pos+=1
            dummy=dummy.next
        new=new.next
        temp=head
        dummy=new
        while(temp):
            if temp.random==None:
                dummy.random=None
            else:
                dummy.random=d[temp.random]
            temp=temp.next
            dummy=dummy.next
        return new
            
            
        