# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l=[]
        temp=head
        while(temp!=None):
            l.append(temp.val)
            temp=temp.next
        
        m=0
        for i in range(len(l)//2):
            s=l[i]+l[-(i+1)]
            if s>m:
                m=s
        return m
        