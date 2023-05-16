# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        if head==None:
            return None
        if head.next==None:
            return head
        while(temp!=None):
            if (temp==head):
                p=temp
                temp=temp.next
            p.val,temp.val=temp.val,p.val
            p=temp.next
            if temp.next!=None:
                temp=temp.next.next
            else:
                break
        return head
            
        
        