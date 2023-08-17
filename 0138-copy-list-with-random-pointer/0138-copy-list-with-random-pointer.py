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
        ptr=head
        while(ptr):
            temp=Node(ptr.val)
            temp.next=ptr.next
            ptr.next=temp
            ptr=temp.next
            
        ptr=head
        while(ptr):
            if ptr.random==None:
                ptr.next.random=None
            else:
                ptr.next.random=ptr.random.next
            ptr=ptr.next.next
        dummy=Node(-1)
        ptr=head
        new=dummy
        while(ptr):
            dummy.next=ptr.next
            dummy=dummy.next
            x=dummy.next
            if x:
                dummy.next=x.next
                ptr=x
            else:
                ptr=None
        return new.next
#         dummy=Node(-1)
#         new=dummy
#         ptr=head
#         while(ptr):
#             dummy.next=ptr.next
#             dummy=dummy.next
#             if ptr.next.next:
#                 x=dummy.next
#                 dummy.next=dummy.next.next
#                 ptr.next=x
#             ptr=ptr.next
#         return new.next
        
        
        
            
        