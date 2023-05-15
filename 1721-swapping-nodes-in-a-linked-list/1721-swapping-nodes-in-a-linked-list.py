# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n=0
        temp=head
        
        while(temp!=None):
            n+=1
            if n==k:
                p=temp
                
            temp=temp.next
        temp=head
        c=0
        while(temp!=None):
            c+=1
            if c==n-k+1:
                q=temp
            temp=temp.next
        
        temp=p.val
        p.val=q.val
        q.val=temp
        return head
        