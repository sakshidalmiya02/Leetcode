# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(lt_root):
            prev=nxt=None
            curr=lt_root
            while(curr):
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            
            return prev
        l1=reverse(l1)
        l2=reverse(l2)
        # print(l1,l2)
        temp1=l1
        temp2=l2
        l3=None
        temp3=None
        c=0
        while(temp1 and temp2):
            sm=temp1.val+temp2.val+c
            if sm>=10:
                c=1
                sm=sm%10
            else:
                c=0
            if l3==None:
                l3=ListNode(sm)
                temp3=l3
            else:
                temp3.next=ListNode(sm)
                temp3=temp3.next
            temp1=temp1.next
            temp2=temp2.next
            
        while temp1:
            sm=temp1.val+c
            if sm>=10:
                c=1
                sm=sm%10
            else:
                c=0
            temp3.next=ListNode(sm)
            temp3=temp3.next
            temp1=temp1.next
        while temp2:
            sm=temp2.val+c
            if sm>=10:
                c=1
                sm=sm%10
            else:
                c=0
            temp3.next=ListNode(sm)
            temp3=temp3.next
            temp2=temp2.next
        
        if c==1:
            temp3.next=ListNode(1)
        return reverse(l3)
            
            