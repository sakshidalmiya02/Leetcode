# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        th=None
        tt=None
        oh=None
        ot=None
        
        def add_first(th,tt,ptr):
            if tt==None:
                tt=ptr
            if th==None:
                th=ptr
            else:
                ptr.next=th
                th=ptr
            return th,tt
                
        temp=head
        n=0
        
        while(temp):
            n+=1
            temp=temp.next
            
        temp=head
        
        while(n>=k):
            tk=k
            while(tk>0):
                fo=temp.next
                temp.next=None
                th,tt=add_first(th,tt,temp)
                # print(th,tt)
                temp=fo
                tk-=1
            # print(th,tt)
            if oh==None:
                oh=th
                ot=tt
            else:
                ot.next=th
                ot=tt
                
            tt=None
            th=None
            n-=k
            
        if n<k:
            ot.next=temp
        return oh
            
                
                
            
            
            
        