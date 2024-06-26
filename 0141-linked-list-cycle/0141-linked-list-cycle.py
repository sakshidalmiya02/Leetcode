# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        f=s=head
        while(f!=None and f.next!=None):
            s=s.next
            f=f.next.next
            if s==f:
                return True
        return False    
            