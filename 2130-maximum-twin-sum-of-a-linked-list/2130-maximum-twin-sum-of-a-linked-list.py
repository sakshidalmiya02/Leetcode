# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast=head,head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        
        curr=slow
        prev,forw=None,None
        while(curr):
            forw=curr.next
            curr.next=prev
            prev=curr
            curr=forw
            
        # print(prev)
        m=0
        temp=head
        while(prev!=None):
            m=max(temp.val+prev.val,m)
            temp=temp.next
            prev=prev.next
        return m